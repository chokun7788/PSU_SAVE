from __future__ import annotations

import json
import os
import re
import time
import unicodedata
from collections import defaultdict
from dataclasses import dataclass, field, replace
from difflib import SequenceMatcher
from functools import lru_cache
from hashlib import sha256
from pathlib import Path
from typing import Any

from app.core.normalization import normalize_text
from app.pipeline.execution_context import current_execution_context
from app.pipeline.query_signals import looks_like_price_amount_query
from app.pipeline.request_deadline import StageDeadlineExceeded, checkpoint


ROOT = Path(__file__).resolve().parents[2]
CURATED_DIR = ROOT / "data" / "curated"


@dataclass(frozen=True)
class EntityCandidate:
    entity_id: str
    title: str
    score: float
    match_type: str
    matched_alias: str = ""
    sources: tuple[str, ...] = ()
    zones: tuple[str, ...] = ()
    has_controls: bool = False
    reasons: tuple[str, ...] = ()

    def as_dict(self) -> dict[str, Any]:
        return {
            "entity_id": self.entity_id,
            "title": self.title,
            "score": round(self.score, 3),
            "match_type": self.match_type,
            "matched_alias": self.matched_alias,
            "sources": list(self.sources),
            "zones": list(self.zones),
            "has_controls": self.has_controls,
            "reasons": list(self.reasons),
        }


@dataclass(frozen=True)
class EntityResolution:
    status: str
    entity_type: str = "game"
    top_candidate: EntityCandidate | None = None
    candidates: tuple[EntityCandidate, ...] = ()
    top_score: float = 0.0
    margin: float = 0.0
    reason: str = ""
    operation: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def is_exact(self) -> bool:
        return self.status == "exact" and self.top_candidate is not None

    @property
    def is_ambiguous(self) -> bool:
        return self.status in {"ambiguous", "incomplete"}

    def as_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "entity_type": self.entity_type,
            "top_candidate": self.top_candidate.as_dict() if self.top_candidate else None,
            "candidates": [candidate.as_dict() for candidate in self.candidates[:8]],
            "top_score": round(self.top_score, 3),
            "margin": round(self.margin, 3),
            "reason": self.reason,
            "operation": self.operation,
            **self.metadata,
        }


# Public name for the new contract.  EntityResolution remains supported while
# callers migrate, so existing structured and fast handlers do not break.
GameResolution = EntityResolution


@dataclass(frozen=True)
class _IndexedAlias:
    alias_id: int
    entity_id: str
    alias: str
    normalized: str
    compact: str
    tokens: frozenset[str]
    trigrams: frozenset[str]


@dataclass(frozen=True)
class GameResolverIndex:
    catalog_version: str
    rows_by_id: dict[str, dict[str, Any]]
    aliases: tuple[_IndexedAlias, ...]
    exact_map: dict[str, tuple[int, ...]]
    compact_map: dict[str, tuple[int, ...]]
    trigram_postings: dict[str, tuple[int, ...]]


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _compact(value: str) -> str:
    return re.sub(r"[^0-9a-z\u0E00-\u0E7F]+", "", normalize_text(value or ""))


def _game_key(value: str) -> str:
    clean = (value or "").replace("™", "").replace("®", "")
    clean = unicodedata.normalize("NFKD", clean).encode("ascii", "ignore").decode("ascii")
    clean = re.sub(r"\(\s*remake\s*\)", "", clean, flags=re.IGNORECASE)
    clean = re.sub(r"\bremake\b", "", clean, flags=re.IGNORECASE)
    clean = re.sub(r"\(\s*remastered\s*\)", "", clean, flags=re.IGNORECASE)
    clean = re.sub(r"\bremastered\b", "", clean, flags=re.IGNORECASE)
    clean = re.sub(r"\bstandard edition\b", "", clean, flags=re.IGNORECASE)
    return _compact(clean)


def _ratio(a: str, b: str) -> float:
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, a, b).ratio()


def _tokens(value: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[0-9a-z+.-]+|[\u0E00-\u0E7F]+", normalize_text(value or ""))
        if len(_compact(token)) >= 2
    }


def _is_short_latin_alias(value: str) -> bool:
    compact = _compact(value)
    return bool(compact) and len(compact) <= 3 and compact.isascii()


def _contains_thai_script(value: str) -> bool:
    return bool(re.search(r"[\u0E00-\u0E7F]", value or ""))


def _truthy(value: str | None, *, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


def entity_reranker_enabled() -> bool:
    return _truthy(os.getenv("PSU_ENTITY_RERANKER"), default=False)


def _entity_reranker_model_name() -> str:
    return os.getenv("PSU_ENTITY_RERANKER_MODEL", "BAAI/bge-reranker-v2-m3").strip() or "BAAI/bge-reranker-v2-m3"


def _entity_reranker_cache_dir() -> Path:
    return Path(os.getenv("PSU_ENTITY_RERANKER_CACHE_DIR", "D:/AIModels/huggingface"))


def _entity_reranker_top_k() -> int:
    return max(1, int(os.getenv("PSU_ENTITY_RERANKER_TOP_K", "6")))


def _entity_reranker_margin_threshold() -> float:
    return float(os.getenv("PSU_ENTITY_RERANKER_MARGIN_THRESHOLD", "0.18"))


def _entity_reranker_min_score() -> float:
    return float(os.getenv("PSU_ENTITY_RERANKER_MIN_SCORE", "-10.0"))


def _entity_reranker_batch_size() -> int:
    return max(1, int(os.getenv("PSU_ENTITY_RERANKER_BATCH_SIZE", "4")))


@lru_cache(maxsize=1)
def _load_entity_reranker_model():
    cache_dir = _entity_reranker_cache_dir()
    cache_dir.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("HF_HOME", str(cache_dir))
    os.environ.setdefault("TRANSFORMERS_CACHE", str(cache_dir / "transformers"))
    os.environ.setdefault("HF_HUB_CACHE", str(cache_dir / "hub"))
    os.environ.setdefault("SENTENCE_TRANSFORMERS_HOME", str(cache_dir / "sentence_transformers"))

    from sentence_transformers import CrossEncoder

    return CrossEncoder(_entity_reranker_model_name(), max_length=512)


def _candidate_rerank_text(candidate: EntityCandidate, operation: str) -> str:
    zones = ", ".join(candidate.zones) if candidate.zones else "unknown"
    controls = "has_controls" if candidate.has_controls else "missing_controls"
    return (
        f"game: {candidate.title}\n"
        f"operation: {operation or 'general'}\n"
        f"zones: {zones}\n"
        f"controls: {controls}\n"
        f"matched_alias: {candidate.matched_alias}\n"
        f"sources: {', '.join(candidate.sources)}"
    )


def _has(text: str, *terms: str) -> bool:
    q = normalize_text(text)
    return any(normalize_text(term) in q for term in terms)


def _target_operation_hint(query: str, operation: str) -> str:
    if looks_like_price_amount_query(query):
        return "price"
    if _has(query, "จอง", "booking", "book", "เข้าเล่น", "ใช้บริการ"):
        return "booking"
    return operation


def _cross_domain_target_allows_game_rerank(query: str, operation: str) -> tuple[bool, str, dict[str, Any]]:
    target_operation = _target_operation_hint(query, operation)
    preferred_domains = ("service_fee",) if target_operation in {"price", "booking"} else ("games",)
    try:
        from app.pipeline.target_resolver import resolve_target_candidate

        target_resolution = resolve_target_candidate(
            query,
            operation=target_operation,
            preferred_domains=preferred_domains,
        )
    except Exception as exc:  # pragma: no cover - optional target resolver safety
        return False, f"cross_domain_target_error:{type(exc).__name__}", {}

    metadata = {"cross_domain_target_resolution": target_resolution.as_dict()}
    top = target_resolution.top_candidate
    if top is None:
        return False, "cross_domain_target_unknown", metadata
    if top.domain != "games":
        return False, f"cross_domain_target_not_game:{top.domain}", metadata
    if target_resolution.status != "exact":
        return False, "cross_domain_target_not_exact_game", metadata
    return True, "cross_domain_target_game", metadata


def _generic_family_query_should_skip_rerank(query: str, operation: str, resolution: EntityResolution) -> bool:
    if "family" not in resolution.metadata:
        return False
    q = normalize_text(query)
    if operation in {"list", "availability", "count", "booking"}:
        return True
    if operation == "gameplay":
        return True
    full_control_terms = (
        "ปุ่มทั้งหมด",
        "ทุกปุ่ม",
        "ปุ่มอะไร",
        "มีปุ่มอะไร",
        "controls",
        "controller",
        "ใช้จอยยังไง",
    )
    if operation == "controls" and any(normalize_text(term) in q for term in full_control_terms):
        return True
    return False


def _should_attempt_entity_rerank(query: str, operation: str, resolution: EntityResolution) -> tuple[bool, str, dict[str, Any]]:
    extra_metadata: dict[str, Any] = {}
    if not entity_reranker_enabled():
        return False, "disabled", extra_metadata
    if operation_allows_family_list(operation):
        return False, "operation_allows_family_list", extra_metadata
    target_operation = _target_operation_hint(query, operation)
    if target_operation not in {"controls", "gameplay", "detail", "price", "booking"}:
        return False, "operation_not_supported", extra_metadata
    if target_operation in {"price", "booking"} or _has(query, "nintendo switch", "นินเทนโด", "สวิตช์", "switch"):
        allowed, reason, target_metadata = _cross_domain_target_allows_game_rerank(query, target_operation)
        extra_metadata.update(target_metadata)
        if not allowed:
            return False, reason, extra_metadata
    if not resolution.candidates:
        return False, "no_candidates", extra_metadata
    if len(resolution.candidates) > _entity_reranker_top_k():
        pass
    if _generic_family_query_should_skip_rerank(query, operation, resolution):
        return False, "generic_family_query", extra_metadata
    if resolution.status == "exact" and resolution.top_candidate and resolution.top_candidate.match_type == "exact_alias":
        return False, "already_exact_alias", extra_metadata
    if resolution.status == "exact" and resolution.margin >= 0.10 and resolution.top_score >= 0.92:
        return False, "already_high_confidence", extra_metadata
    if resolution.status == "unknown" and resolution.top_score < 0.68:
        return False, "candidate_score_too_low", extra_metadata
    if len(resolution.candidates) == 1 and resolution.status not in {"unknown", "ambiguous"}:
        return False, "single_candidate_not_needed", extra_metadata
    return True, "eligible", extra_metadata


def _apply_entity_reranker(query: str, operation: str, resolution: EntityResolution) -> EntityResolution:
    should_run, reason, rerank_metadata = _should_attempt_entity_rerank(query, operation, resolution)
    metadata = dict(resolution.metadata)
    if not should_run:
        metadata["reranker"] = {
            "enabled": entity_reranker_enabled(),
            "action": "skipped",
            "reason": reason,
            **rerank_metadata,
        }
        if reason.startswith("cross_domain_target_not_game"):
            return EntityResolution(
                "unknown",
                entity_type=resolution.entity_type,
                top_candidate=None,
                candidates=resolution.candidates,
                top_score=resolution.top_score,
                margin=resolution.margin,
                reason="cross_domain_target_is_not_game",
                operation=resolution.operation,
                metadata=metadata,
            )
        return EntityResolution(
            resolution.status,
            entity_type=resolution.entity_type,
            top_candidate=resolution.top_candidate,
            candidates=resolution.candidates,
            top_score=resolution.top_score,
            margin=resolution.margin,
            reason=resolution.reason,
            operation=resolution.operation,
            metadata=metadata,
        )

    started = time.perf_counter()
    try:
        candidates = resolution.candidates[: _entity_reranker_top_k()]
        model = _load_entity_reranker_model()
        pairs = [(query, _candidate_rerank_text(candidate, operation)) for candidate in candidates]
        raw_scores = model.predict(pairs, batch_size=_entity_reranker_batch_size(), show_progress_bar=False)
        scored = sorted(
            zip(candidates, [float(value) for value in raw_scores]),
            key=lambda item: item[1],
            reverse=True,
        )
    except Exception as exc:  # pragma: no cover - depends on optional local model runtime
        metadata["reranker"] = {
            "enabled": True,
            "action": "error",
            "reason": type(exc).__name__,
            "elapsed_sec": round(time.perf_counter() - started, 4),
            **rerank_metadata,
        }
        return EntityResolution(
            resolution.status,
            entity_type=resolution.entity_type,
            top_candidate=resolution.top_candidate,
            candidates=resolution.candidates,
            top_score=resolution.top_score,
            margin=resolution.margin,
            reason=resolution.reason,
            operation=resolution.operation,
            metadata=metadata,
        )

    top, top_score = scored[0]
    second_score = scored[1][1] if len(scored) > 1 else top_score - 1.0
    margin = float(top_score - second_score)
    threshold = _entity_reranker_margin_threshold()
    min_score = _entity_reranker_min_score()
    ranked_rows = [
        {
            "title": candidate.title,
            "score": round(float(score), 4),
            "base_score": round(candidate.score, 4),
            "match_type": candidate.match_type,
            "matched_alias": candidate.matched_alias,
        }
        for candidate, score in scored
    ]

    if float(top_score) < min_score or margin < threshold:
        metadata["reranker"] = {
            "enabled": True,
            "action": "kept_ambiguous",
            "reason": "below_rerank_threshold",
            "model": _entity_reranker_model_name(),
            "elapsed_sec": round(time.perf_counter() - started, 4),
            "top_score": round(float(top_score), 4),
            "margin": round(margin, 4),
            "ranked": ranked_rows,
            **rerank_metadata,
        }
        return EntityResolution(
            "ambiguous",
            entity_type=resolution.entity_type,
            top_candidate=top,
            candidates=tuple(candidate for candidate, _score in scored),
            top_score=resolution.top_score,
            margin=resolution.margin,
            reason="reranker_kept_ambiguous_low_margin",
            operation=resolution.operation,
            metadata=metadata,
        )

    metadata["reranker"] = {
        "enabled": True,
        "action": "selected_exact",
        "reason": "reranker_margin_passed",
        "model": _entity_reranker_model_name(),
        "elapsed_sec": round(time.perf_counter() - started, 4),
        "top_score": round(float(top_score), 4),
        "margin": round(margin, 4),
        "ranked": ranked_rows,
        **rerank_metadata,
    }
    return EntityResolution(
        "exact",
        entity_type=resolution.entity_type,
        top_candidate=top,
        candidates=tuple(candidate for candidate, _score in scored),
        top_score=top.score,
        margin=max(resolution.margin, margin),
        reason="reranker_selected_exact_candidate",
        operation=resolution.operation,
        metadata=metadata,
    )


def _canonical_zone_label(value: str) -> str:
    q = normalize_text(value)
    if "playstation" in q or "ps5" in q:
        return "PlayStation 5 Zone"
    if "nintendo" in q or "switch" in q:
        return "Nintendo Switch Zone"
    if "cockpit" in q or "คอกพิท" in q or "ค็อกพิท" in q:
        return "Cockpit Zone"
    if "vr" in q:
        return "VR Zone"
    if "pc" in q or "คอม" in q:
        return "PC Zone"
    return value.strip()


@lru_cache(maxsize=1)
def _control_games() -> frozenset[str]:
    games = {
        _game_key(str(row.get("game") or ""))
        for row in _read_jsonl(CURATED_DIR / "game_control_facts.jsonl")
        if row.get("category") == "game_controls" and row.get("button")
    }
    return frozenset(key for key in games if key)


@lru_cache(maxsize=1)
def _current_game_rows() -> tuple[dict[str, Any], ...]:
    alias_rows = {
        _game_key(str(row.get("game") or "")): row
        for row in _read_jsonl(CURATED_DIR / "game_title_aliases.jsonl")
        if row.get("game")
    }
    current: dict[str, dict[str, Any]] = {}
    for service in _read_jsonl(CURATED_DIR / "service_game_availability.jsonl"):
        zone = _canonical_zone_label(str(service.get("zone") or ""))
        source_id = str(service.get("id") or "service_game_availability")
        for raw_game in service.get("games") or []:
            game = str(raw_game or "").strip()
            key = _game_key(game)
            if not game or not key:
                continue
            alias_row = alias_rows.get(key, {})
            row = current.setdefault(
                key,
                {
                    "entity_id": key,
                    "title": game,
                    "aliases": set(),
                    "zones": set(),
                    "sources": set(),
                },
            )
            row["aliases"].add(game)
            for alias in alias_row.get("aliases") or []:
                row["aliases"].add(str(alias))
            row["zones"].add(zone)
            row["sources"].add(source_id)

    # Add aliases only for current games. This avoids stale games such as Mario Kart Live
    # becoming answerable when they are not in the current availability data.
    output: list[dict[str, Any]] = []
    controls = _control_games()
    for row in current.values():
        aliases = {alias for alias in row["aliases"] if _compact(alias)}
        aliases.add(str(row["title"]))
        output.append({
            "entity_id": row["entity_id"],
            "title": row["title"],
            "aliases": tuple(sorted(aliases, key=lambda item: (-len(_compact(item)), item.lower()))),
            "zones": tuple(sorted(zone for zone in row["zones"] if zone)),
            "sources": tuple(sorted(row["sources"])),
            "has_controls": row["entity_id"] in controls,
        })
    output.sort(key=lambda item: str(item["title"]).lower())
    return tuple(output)


def _trigrams(value: str) -> frozenset[str]:
    compact = _compact(value)
    if len(compact) < 3:
        return frozenset()
    padded = f"  {compact}  "
    return frozenset(padded[index:index + 3] for index in range(len(padded) - 2))


def _resolver_stage_sec() -> float:
    try:
        return max(0.01, min(1.0, float(os.getenv("PSU_GAME_RESOLVER_STAGE_SEC", "0.25"))))
    except ValueError:
        return 0.25


def _resolver_candidate_limit() -> int:
    try:
        return max(1, min(16, int(os.getenv("PSU_GAME_RESOLVER_CANDIDATES", "8"))))
    except ValueError:
        return 8


def _resolver_comparison_limit() -> int:
    try:
        return max(1, min(128, int(os.getenv("PSU_GAME_RESOLVER_COMPARISONS", "64"))))
    except ValueError:
        return 64


def _resolver_fuzzy_threshold() -> float:
    try:
        return min(0.98, max(0.80, float(os.getenv("PSU_GAME_FUZZY_THRESHOLD", "0.88"))))
    except ValueError:
        return 0.88


def _resolver_margin_threshold() -> float:
    try:
        return min(0.20, max(0.03, float(os.getenv("PSU_GAME_FUZZY_MARGIN", "0.08"))))
    except ValueError:
        return 0.08


def _catalog_version(rows: tuple[dict[str, Any], ...]) -> str:
    payload = [
        {
            "id": str(row.get("entity_id") or ""),
            "title": str(row.get("title") or ""),
            "aliases": sorted(str(alias) for alias in row.get("aliases") or ()),
            "zones": sorted(str(zone) for zone in row.get("zones") or ()),
        }
        for row in rows
    ]
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return sha256(encoded).hexdigest()[:16]


@lru_cache(maxsize=1)
def _game_resolver_index() -> GameResolverIndex:
    rows = _current_game_rows()
    rows_by_id = {str(row["entity_id"]): row for row in rows}
    aliases: list[_IndexedAlias] = []
    exact_map: dict[str, list[int]] = defaultdict(list)
    compact_map: dict[str, list[int]] = defaultdict(list)
    trigram_postings: dict[str, list[int]] = defaultdict(list)

    for row in rows:
        entity_id = str(row["entity_id"])
        seen_aliases: set[str] = set()
        for raw_alias in row.get("aliases") or ():
            alias = str(raw_alias or "").strip()
            normalized = normalize_text(alias)
            compact = _compact(alias)
            if not normalized or len(compact) < 3 or compact in seen_aliases:
                continue
            seen_aliases.add(compact)
            alias_id = len(aliases)
            record = _IndexedAlias(
                alias_id=alias_id,
                entity_id=entity_id,
                alias=alias,
                normalized=normalized,
                compact=compact,
                tokens=frozenset(_tokens(alias)),
                trigrams=_trigrams(alias),
            )
            aliases.append(record)
            exact_map[normalized].append(alias_id)
            compact_map[compact].append(alias_id)
            for gram in record.trigrams:
                trigram_postings[gram].append(alias_id)

    return GameResolverIndex(
        catalog_version=_catalog_version(rows),
        rows_by_id=rows_by_id,
        aliases=tuple(aliases),
        exact_map={key: tuple(value) for key, value in exact_map.items()},
        compact_map={key: tuple(value) for key, value in compact_map.items()},
        trigram_postings={key: tuple(value) for key, value in trigram_postings.items()},
    )


def clear_game_resolver_index() -> None:
    """Use only after a catalog reload so the next request rebuilds atomically."""

    _current_game_rows.cache_clear()
    _game_resolver_index.cache_clear()


def _bounded_query_windows(compact_query: str, alias_length: int) -> tuple[str, ...]:
    if not compact_query:
        return ()
    width = max(3, min(len(compact_query), alias_length + 2))
    if len(compact_query) <= width:
        return (compact_query,)
    max_windows = 8
    last_start = len(compact_query) - width
    starts = {
        0,
        last_start,
        *(round(last_start * index / max(1, max_windows - 1)) for index in range(max_windows)),
    }
    return tuple(compact_query[start:start + width] for start in sorted(starts)[:max_windows])


def _resolver_metadata(
    *,
    index: GameResolverIndex,
    method: str,
    candidate_count: int,
    comparison_count: int,
    started: float,
    cache_hit: bool = False,
    budget_exceeded: bool = False,
) -> dict[str, Any]:
    return {
        "resolver": "bounded_trigram_v1",
        "catalog_version": index.catalog_version,
        "method": method,
        "candidate_count": candidate_count,
        "comparison_count": comparison_count,
        "elapsed_ms": round((time.perf_counter() - started) * 1000, 3),
        "request_cache_hit": cache_hit,
        "budget_exceeded": budget_exceeded,
    }


def _with_operation_adjustments(candidate: EntityCandidate, row: dict[str, Any], operation: str) -> EntityCandidate:
    score = candidate.score
    reasons = list(candidate.reasons)
    if operation in {"controls", "gameplay"}:
        if row.get("has_controls"):
            score += 0.04
            reasons.append("operation_has_controls")
        elif candidate.match_type not in {"exact_alias", "compact_alias"}:
            score -= 0.05
            reasons.append("operation_missing_controls")
    if operation in {"availability", "booking", "price"} and row.get("zones"):
        score += 0.02
        reasons.append("operation_has_availability")
    return replace(candidate, score=min(1.0, max(0.0, score)), reasons=tuple(reasons))


def _candidate_from_alias(
    *,
    row: dict[str, Any],
    alias: _IndexedAlias,
    score: float,
    match_type: str,
    operation: str,
) -> EntityCandidate:
    candidate = EntityCandidate(
        entity_id=str(row["entity_id"]),
        title=str(row["title"]),
        score=score,
        match_type=match_type,
        matched_alias=alias.alias,
        sources=tuple(row.get("sources") or ()),
        zones=tuple(row.get("zones") or ()),
        has_controls=bool(row.get("has_controls")),
        reasons=(),
    )
    return _with_operation_adjustments(candidate, row, operation)


def _keep_more_specific_direct_match(
    current: EntityCandidate | None,
    candidate: EntityCandidate,
) -> EntityCandidate:
    """Keep the strongest exact alias for one catalog entity.

    A title can intentionally have a short Thai/English nickname shared with a
    sibling title.  For example, ``Overcooked! 2`` also has the colloquial
    alias ``โอเวอคุก``.  Once the user supplies the full title, that full
    title must not be overwritten later in the alias loop by the shorter
    nickname.  The cross-entity margin below can then distinguish a real
    family-level query from an explicit versioned title.
    """
    if current is None:
        return candidate
    current_key = (current.score, len(_compact(current.matched_alias)))
    candidate_key = (candidate.score, len(_compact(candidate.matched_alias)))
    return candidate if candidate_key > current_key else current


def _is_versioned_alias_extension(short_alias: str, long_alias: str) -> bool:
    """Return true when ``long_alias`` explicitly adds a game version.

    This is deliberately narrow.  It is only used after both aliases already
    matched the same user question exactly/compactly, so a generic title such
    as ``Overcooked`` cannot shadow an explicit ``Overcooked 2`` request.
    """
    short_key = _compact(short_alias)
    long_key = _compact(long_alias)
    if len(short_key) < 3 or not long_key.startswith(short_key):
        return False
    suffix = long_key[len(short_key):]
    return bool(re.fullmatch(r"(?:[0-9]+|i{1,3}|iv|v|vi{0,3})", suffix))


def _direct_candidate_sort_key(
    candidate: EntityCandidate,
    candidates: list[EntityCandidate],
) -> tuple[int, int, int, float]:
    versioned = any(
        other.entity_id != candidate.entity_id
        and _is_versioned_alias_extension(other.matched_alias, candidate.matched_alias)
        for other in candidates
    )
    match_rank = 2 if candidate.match_type == "exact_alias" else 1
    return (int(versioned), len(_compact(candidate.matched_alias)), match_rank, candidate.score)


def _shortlisted_aliases(query: str, index: GameResolverIndex) -> list[tuple[_IndexedAlias, float]]:
    normalized = normalize_text(query)
    compact = _compact(query)
    direct_ids = list(index.exact_map.get(normalized, ())) + list(index.compact_map.get(compact, ()))
    postings: dict[int, int] = defaultdict(int)
    for gram in _trigrams(query):
        for alias_id in index.trigram_postings.get(gram, ()):
            postings[alias_id] += 1

    limit = _resolver_comparison_limit()
    ranked_ids = sorted(
        postings,
        key=lambda alias_id: (
            postings[alias_id] / max(1, len(index.aliases[alias_id].trigrams)),
            postings[alias_id],
        ),
        reverse=True,
    )
    selected_ids = list(dict.fromkeys([*direct_ids, *ranked_ids[:limit]]))[:limit]
    return [
        (
            index.aliases[alias_id],
            postings.get(alias_id, len(index.aliases[alias_id].trigrams)),
        )
        for alias_id in selected_ids
    ]


def _bounded_resolution(query: str, operation: str, index: GameResolverIndex, started: float) -> EntityResolution:
    normalized = normalize_text(query)
    compact = _compact(query)
    tokens = _tokens(query)
    shortlist = _shortlisted_aliases(query, index)
    if not shortlist:
        return EntityResolution(
            "unknown",
            reason="no_game_candidate",
            operation=operation,
            metadata=_resolver_metadata(
                index=index,
                method="none",
                candidate_count=0,
                comparison_count=0,
                started=started,
            ),
        )

    direct_candidates: dict[str, EntityCandidate] = {}
    seeded: dict[str, tuple[_IndexedAlias, float]] = {}
    # A mixed Thai sentence can contain an explicit English game title.  In
    # that case, do not also treat a Thai keyboard-layout alias that happens
    # to normalize to the same Latin text as another exact match.
    has_explicit_latin_title = any(
        not _contains_thai_script(alias.alias)
        and len(alias.compact) >= 4
        and alias.normalized in normalized
        for alias, _overlap_count in shortlist
    )
    for alias, overlap_count in shortlist:
        checkpoint("game_resolution")
        if time.perf_counter() - started > _resolver_stage_sec():
            raise StageDeadlineExceeded("game_resolution", time.perf_counter() - started, 0.0)
        row = index.rows_by_id[alias.entity_id]
        # normalize_text can convert a Thai keyboard-layout spelling into a
        # Latin-looking string.  That is useful for a Thai request, but it
        # must not let a Thai alias collide with a genuine English title.
        # Example: the Thai nickname for Overcooked 2 normalizes to
        # ``overcooked`` and used to make ``Overcooked!`` ambiguous.
        alias_language_compatible = not (
            has_explicit_latin_title and _contains_thai_script(alias.alias)
        )
        normalized_match = bool(re.search(rf"{re.escape(alias.normalized)}(?![a-z0-9])", normalized))
        compact_match = bool(re.search(rf"{re.escape(alias.compact)}(?![a-z0-9])", compact)) if len(alias.compact) >= 4 else False
        if normalized_match and (
            not _is_short_latin_alias(alias.alias) or alias.normalized in tokens
        ) and alias_language_compatible:
            candidate = _candidate_from_alias(
                row=row,
                alias=alias,
                score=1.0,
                match_type="exact_alias",
                operation=operation,
            )
            direct_candidates[alias.entity_id] = _keep_more_specific_direct_match(
                direct_candidates.get(alias.entity_id),
                candidate,
            )
            continue
        if compact_match and alias_language_compatible:
            candidate = _candidate_from_alias(
                row=row,
                alias=alias,
                score=0.96,
                match_type="compact_alias",
                operation=operation,
            )
            direct_candidates[alias.entity_id] = _keep_more_specific_direct_match(
                direct_candidates.get(alias.entity_id),
                candidate,
            )
            continue
        token_overlap = len(alias.tokens.intersection(tokens))
        cheap_score = max(
            overlap_count / max(1, len(alias.trigrams)),
            token_overlap / max(1, len(alias.tokens)) if alias.tokens else 0.0,
        )
        current = seeded.get(alias.entity_id)
        if current is None or cheap_score > current[1]:
            seeded[alias.entity_id] = (alias, cheap_score)

    if direct_candidates:
        scored = sorted(
            direct_candidates.values(),
            key=lambda item: _direct_candidate_sort_key(item, list(direct_candidates.values())),
            reverse=True,
        )
        top = scored[0]
        second = scored[1] if len(scored) > 1 else None
        versioned_winner = bool(second) and _is_versioned_alias_extension(
            second.matched_alias,
            top.matched_alias,
        )
        margin = top.score - second.score if second else 1.0
        status = "exact" if second is None or versioned_winner or margin >= _resolver_margin_threshold() else "ambiguous"
        return EntityResolution(
            status,
            top_candidate=top,
            candidates=tuple(scored[:_resolver_candidate_limit()]),
            top_score=top.score,
            margin=margin,
            reason="direct_alias_match" if status == "exact" else "direct_alias_ambiguous",
            operation=operation,
            metadata=_resolver_metadata(
                index=index,
                method="exact",
                candidate_count=len(scored),
                comparison_count=0,
                started=started,
            ),
        )

    comparison_limit = _resolver_comparison_limit()
    comparisons = 0
    fuzzy_candidates: list[EntityCandidate] = []
    for entity_id, (alias, cheap_score) in sorted(
        seeded.items(),
        key=lambda item: item[1][1],
        reverse=True,
    )[:_resolver_candidate_limit()]:
        checkpoint("game_resolution")
        if time.perf_counter() - started > _resolver_stage_sec():
            raise StageDeadlineExceeded("game_resolution", time.perf_counter() - started, 0.0)
        row = index.rows_by_id[entity_id]
        best_fuzzy = 0.0
        for window in _bounded_query_windows(compact, len(alias.compact)):
            checkpoint("game_resolution")
            if comparisons >= comparison_limit:
                break
            best_fuzzy = max(best_fuzzy, _ratio(window, alias.compact))
            comparisons += 1
        score = max(0.0, min(0.86, 0.58 + cheap_score * 0.24))
        match_type = "token_overlap"
        if best_fuzzy >= _resolver_fuzzy_threshold():
            score = best_fuzzy
            match_type = "fuzzy"
        if score >= 0.78:
            fuzzy_candidates.append(_candidate_from_alias(
                row=row,
                alias=alias,
                score=score,
                match_type=match_type,
                operation=operation,
            ))

    if not fuzzy_candidates:
        return EntityResolution(
            "unknown",
            reason="shortlist_below_threshold",
            operation=operation,
            metadata=_resolver_metadata(
                index=index,
                method="trigram_fuzzy",
                candidate_count=len(seeded),
                comparison_count=comparisons,
                started=started,
            ),
        )

    fuzzy_candidates.sort(key=lambda item: (item.score, len(_compact(item.matched_alias))), reverse=True)
    top = fuzzy_candidates[0]
    second = fuzzy_candidates[1] if len(fuzzy_candidates) > 1 else None
    margin = top.score - second.score if second else 1.0
    if top.score < _resolver_fuzzy_threshold():
        status = "unknown"
        top_candidate = None
        reason = "top_candidate_below_threshold"
    elif second is not None and margin < _resolver_margin_threshold():
        status = "ambiguous"
        top_candidate = top
        reason = "top_candidates_low_margin"
    else:
        status = "exact"
        top_candidate = top
        reason = "bounded_fuzzy_match"
    return EntityResolution(
        status,
        top_candidate=top_candidate,
        candidates=tuple(fuzzy_candidates[:_resolver_candidate_limit()]),
        top_score=top.score,
        margin=margin,
        reason=reason,
        operation=operation,
        metadata=_resolver_metadata(
            index=index,
            method="trigram_fuzzy",
            candidate_count=len(seeded),
            comparison_count=comparisons,
            started=started,
        ),
    )


def _family_match(query: str) -> tuple[str, tuple[str, ...], tuple[str, ...]] | None:
    q = normalize_text(query).replace("over cook", "overcook")
    families: tuple[tuple[str, tuple[str, ...], tuple[str, ...]], ...] = (
        ("Mario", ("mario", "มาริโอ", "มาริโอ้"), ("kart", "คาร์ท", "คาท", "party", "odyssey", "bros", "super mario", "8", "live")),
        ("Resident Evil", ("resident evil", "resident", "เรสซิเดนต์", "เรสซิเดนท์", "อีวิล", "อีวิว"), ("4", "village")),
        ("Call of Duty", ("call of duty", "call of", "cod", "คอลออฟ", "คอลออฟดิวตี้", "คอลออฟดูตี้", "ดิวตี้", "ดูตี้"), ("warzone", "วอร์โซน", "วอโซน", "modern warfare", "mw3", "mwiii", "วอร์แฟร์")),
        ("Overcooked", ("overcooked", "overcook", "โอเวอร์คุก", "โอเวอร์คุ๊ก", "โอเวอคุก", "โอเวอคุ๊ก"), ("2", "two", "ทู", "สอง")),
        ("The Last of Us", ("the last of us", "last of us", "tlou", "ลาสออฟอัส"), ("part i", "part ii", "ภาค 1", "ภาค 2", "remastered")),
    )
    for label, aliases, specifics in families:
        if label == "Call of Duty" and any(term in q for term in ("horizon", "ฮอไรซ", "โฮไรซ")):
            continue
        if any(normalize_text(alias) in q for alias in aliases):
            return label, aliases, specifics
    return None


def _family_candidates(label: str) -> tuple[EntityCandidate, ...]:
    label_norm = normalize_text(label)
    candidates: list[EntityCandidate] = []
    for row in _current_game_rows():
        title_norm = normalize_text(str(row.get("title") or ""))
        if label_norm in title_norm or (label == "Mario" and "mario" in title_norm):
            candidates.append(EntityCandidate(
                str(row["entity_id"]),
                str(row["title"]),
                0.82,
                "family",
                label,
                tuple(row.get("sources") or ()),
                tuple(row.get("zones") or ()),
                bool(row.get("has_controls")),
                ("family_candidate",),
            ))
    return tuple(sorted(candidates, key=lambda item: item.title.lower()))


def _explicit_current_title_id(query: str) -> str:
    q = normalize_text(query)
    matches: list[tuple[int, str]] = []
    for row in _current_game_rows():
        title = normalize_text(str(row.get("title") or ""))
        if not title:
            continue
        pattern = rf"(?<![0-9a-z]){re.escape(title)}(?![0-9a-z])"
        if re.search(pattern, q):
            matches.append((len(_compact(title)), str(row.get("entity_id") or "")))
    if not matches:
        return ""
    matches.sort(reverse=True)
    top_length = matches[0][0]
    top_ids = {entity_id for length, entity_id in matches if length == top_length}
    return next(iter(top_ids)) if len(top_ids) == 1 else ""


def _score_game_candidate(query: str, row: dict[str, Any], operation: str) -> EntityCandidate | None:
    q_norm = normalize_text(query)
    q_compact = _compact(query)
    q_tokens = _tokens(query)
    best_score = 0.0
    best_alias = ""
    match_type = ""
    reasons: list[str] = []

    for alias in row.get("aliases") or ():
        alias = str(alias or "").strip()
        alias_norm = normalize_text(alias)
        alias_compact = _compact(alias)
        if len(alias_compact) < 3:
            continue
        score = 0.0
        current_match_type = ""
        if alias_norm and (
            alias_norm in q_norm
            and (not _is_short_latin_alias(alias) or alias_norm in q_tokens)
        ):
            score = 1.0
            current_match_type = "exact_alias"
        elif len(alias_compact) >= 4 and alias_compact in q_compact:
            score = 0.96
            current_match_type = "compact_alias"
        else:
            alias_tokens = _tokens(alias)
            overlap = alias_tokens.intersection(q_tokens)
            if overlap and len(overlap) >= max(1, min(2, len(alias_tokens))):
                score = min(0.86, 0.58 + (len(overlap) / max(1, len(alias_tokens))) * 0.24)
                current_match_type = "token_overlap"
            elif len(alias_compact) >= 5:
                fuzzy = _ratio(q_compact, alias_compact)
                if fuzzy >= 0.84:
                    score = fuzzy - 0.06
                    current_match_type = "fuzzy"
        if score > best_score:
            best_score = score
            best_alias = alias
            match_type = current_match_type

    if not best_score:
        return None

    if operation in {"controls", "gameplay"}:
        if row.get("has_controls"):
            best_score += 0.04
            reasons.append("operation_has_controls")
        else:
            # Missing capability data must not make a different title beat an
            # exact game-name match. The executor can safely return no-data.
            if match_type not in {"exact_alias", "compact_alias"}:
                best_score -= 0.05
            reasons.append("operation_missing_controls")
    if operation in {"availability", "booking", "price"} and row.get("zones"):
        best_score += 0.02
        reasons.append("operation_has_availability")

    return EntityCandidate(
        str(row["entity_id"]),
        str(row["title"]),
        min(best_score, 1.0),
        match_type,
        best_alias,
        tuple(row.get("sources") or ()),
        tuple(row.get("zones") or ()),
        bool(row.get("has_controls")),
        tuple(reasons),
    )


def resolve_game_entity(query: str, *, operation: str = "") -> EntityResolution:
    q = normalize_text(query)
    # The catalog index is a startup/reload concern.  Measure the bounded
    # per-request lookup after it is available so a cold index build is not
    # misreported as fuzzy-match work or turned into a false unknown answer.
    index = _game_resolver_index()
    started = time.perf_counter()
    context = current_execution_context()
    if context is not None:
        cached = context.get_game_resolution(query, operation, index.catalog_version)
        if cached is not None:
            context.increment("game_resolution_cache_hits")
            return replace(
                cached,
                metadata={
                    **cached.metadata,
                    **_resolver_metadata(
                        index=index,
                        method=str(cached.metadata.get("method") or "request_cache"),
                        candidate_count=len(cached.candidates),
                        comparison_count=int(cached.metadata.get("comparison_count") or 0),
                        started=started,
                        cache_hit=True,
                    ),
                },
            )
        context.increment("game_resolution_calls")

    family = _family_match(q)
    explicit_title_id = _explicit_current_title_id(q)
    if family is not None and not explicit_title_id:
        label, _aliases, specifics = family
        has_specific = any(normalize_text(term) in q for term in specifics)
        family_candidates = _family_candidates(label)
        if family_candidates and not has_specific:
            status = "ambiguous" if len(family_candidates) > 1 else "exact"
            top = family_candidates[0] if family_candidates else None
            result = EntityResolution(
                status,
                top_candidate=top,
                candidates=family_candidates,
                top_score=top.score if top else 0.0,
                margin=0.0 if len(family_candidates) > 1 else 1.0,
                reason="family_name_has_multiple_current_candidates" if len(family_candidates) > 1 else "family_name_has_single_candidate",
                operation=operation,
                metadata={
                    "family": label,
                    **_resolver_metadata(
                        index=index,
                        method="family",
                        candidate_count=len(family_candidates),
                        comparison_count=0,
                        started=started,
                    ),
                },
            )
            if context is not None:
                context.store_game_resolution(query, operation, index.catalog_version, result)
            return _apply_entity_reranker(q, operation, result)

    try:
        result = _bounded_resolution(q, operation, index, started)
    except StageDeadlineExceeded:
        result = EntityResolution(
            "unknown",
            reason="game_resolution_budget_exceeded",
            operation=operation,
            metadata=_resolver_metadata(
                index=index,
                method="trigram_fuzzy",
                candidate_count=0,
                comparison_count=0,
                started=started,
                budget_exceeded=True,
            ),
        )
    if context is not None:
        context.store_game_resolution(query, operation, index.catalog_version, result)
    return _apply_entity_reranker(q, operation, result)


def operation_requires_exact_game(operation: str) -> bool:
    return operation in {"controls", "gameplay", "detail", "booking", "price"}


def operation_allows_family_list(operation: str) -> bool:
    return operation in {"list", "availability", "count"}
