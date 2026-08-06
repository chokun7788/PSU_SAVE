from __future__ import annotations

import json
import os
import re
import time
import unicodedata
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from functools import lru_cache
from pathlib import Path
from typing import Any

from app.core.normalization import normalize_text


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
    if _has(query, "ราคา", "กี่บาท", "ค่าบริการ", "เท่าไหร่", "เท่าไร", "จ่าย", "เสีย"):
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
    family = _family_match(q)
    scored = [
        candidate
        for row in _current_game_rows()
        if (candidate := _score_game_candidate(q, row, operation)) is not None
    ]
    explicit_title_id = _explicit_current_title_id(q)
    scored.sort(
        key=lambda item: (
            item.entity_id == explicit_title_id,
            item.score,
            len(_compact(item.matched_alias)),
        ),
        reverse=True,
    )

    if family is not None and not explicit_title_id:
        label, _aliases, specifics = family
        has_specific = any(normalize_text(term) in q for term in specifics)
        family_candidates = _family_candidates(label)
        if family_candidates and not has_specific:
            status = "ambiguous" if len(family_candidates) > 1 else "exact"
            top = family_candidates[0] if family_candidates else None
            return _apply_entity_reranker(q, operation, EntityResolution(
                status,
                top_candidate=top,
                candidates=family_candidates,
                top_score=top.score if top else 0.0,
                margin=0.0 if len(family_candidates) > 1 else 1.0,
                reason="family_name_has_multiple_current_candidates" if len(family_candidates) > 1 else "family_name_has_single_candidate",
                operation=operation,
                metadata={"family": label},
            ))

    if not scored:
        return _apply_entity_reranker(q, operation, EntityResolution("unknown", reason="no_game_candidate", operation=operation))

    top = scored[0]
    second = scored[1] if len(scored) > 1 else None
    margin = top.score - second.score if second else 1.0
    if top.match_type == "exact_alias" and top.score >= 0.98:
        status = "exact"
        reason = "top_exact_alias_overrides_parent_match"
    elif top.score >= 0.92 and margin >= 0.10:
        status = "exact"
        reason = "top_candidate_high_confidence"
    elif top.score >= 0.78 and margin < 0.12:
        status = "ambiguous"
        reason = "top_candidates_low_margin"
    elif top.score >= 0.78:
        status = "exact"
        reason = "top_candidate_acceptable"
    else:
        status = "unknown"
        reason = "top_candidate_below_threshold"
    return _apply_entity_reranker(q, operation, EntityResolution(
        status,
        top_candidate=top if status != "unknown" else None,
        candidates=tuple(scored[:8]),
        top_score=top.score,
        margin=margin,
        reason=reason,
        operation=operation,
    ))


def operation_requires_exact_game(operation: str) -> bool:
    return operation in {"controls", "gameplay", "detail", "booking", "price"}


def operation_allows_family_list(operation: str) -> bool:
    return operation in {"list", "availability", "count"}
