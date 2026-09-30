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

from app.core.normalization import SERVICE_ALIASES, normalize_text


ROOT = Path(__file__).resolve().parents[2]
CURATED_DIR = ROOT / "data" / "curated"


@dataclass(frozen=True)
class TargetCandidate:
    target_id: str
    domain: str
    target_type: str
    label: str
    score: float
    match_type: str
    matched_alias: str = ""
    evidence: str = ""
    sources: tuple[str, ...] = ()
    metadata: dict[str, Any] = field(default_factory=dict)

    def as_dict(self) -> dict[str, Any]:
        return {
            "target_id": self.target_id,
            "domain": self.domain,
            "target_type": self.target_type,
            "label": self.label,
            "score": round(self.score, 3),
            "match_type": self.match_type,
            "matched_alias": self.matched_alias,
            "evidence": self.evidence,
            "sources": list(self.sources),
            "metadata": self.metadata,
        }


@dataclass(frozen=True)
class TargetResolution:
    status: str
    top_candidate: TargetCandidate | None = None
    candidates: tuple[TargetCandidate, ...] = ()
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
        return self.status == "ambiguous"

    def as_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
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


def _key(value: str) -> str:
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


def target_reranker_enabled() -> bool:
    return _truthy(os.getenv("PSU_TARGET_RERANKER"), default=False)


def _target_reranker_model_name() -> str:
    return os.getenv("PSU_TARGET_RERANKER_MODEL") or os.getenv("PSU_ENTITY_RERANKER_MODEL", "BAAI/bge-reranker-v2-m3")


def _target_reranker_cache_dir() -> Path:
    return Path(os.getenv("PSU_TARGET_RERANKER_CACHE_DIR") or os.getenv("PSU_ENTITY_RERANKER_CACHE_DIR", "D:/AIModels/huggingface"))


@lru_cache(maxsize=1)
def _load_target_reranker_model():
    cache_dir = _target_reranker_cache_dir()
    cache_dir.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("HF_HOME", str(cache_dir))
    os.environ.setdefault("TRANSFORMERS_CACHE", str(cache_dir / "transformers"))
    os.environ.setdefault("HF_HUB_CACHE", str(cache_dir / "hub"))
    os.environ.setdefault("SENTENCE_TRANSFORMERS_HOME", str(cache_dir / "sentence_transformers"))

    from sentence_transformers import CrossEncoder

    return CrossEncoder(_target_reranker_model_name(), max_length=512)


def _zone_aliases(zone: str, service_label: str) -> tuple[str, ...]:
    zone_norm = normalize_text(zone)
    aliases: list[str] = [zone, service_label]
    if "pc" in zone_norm:
        aliases.extend(SERVICE_ALIASES.get("pc", ()))
    elif "playstation" in zone_norm or "ps5" in zone_norm:
        aliases.extend(SERVICE_ALIASES.get("ps5", ()))
    elif "nintendo" in zone_norm or "switch" in zone_norm:
        aliases.extend(SERVICE_ALIASES.get("nintendo_switch", ()))
    elif "cockpit" in zone_norm:
        aliases.extend(SERVICE_ALIASES.get("cockpit", ()))
    elif "vr" in zone_norm:
        aliases.extend(SERVICE_ALIASES.get("vr", ()))
    return tuple(dict.fromkeys(alias for alias in aliases if alias))


@lru_cache(maxsize=1)
def _service_targets() -> tuple[dict[str, Any], ...]:
    rows: list[dict[str, Any]] = []
    for row in _read_jsonl(CURATED_DIR / "service_game_availability.jsonl"):
        label = str(row.get("service_label") or row.get("zone") or "").strip()
        zone = str(row.get("zone") or "").strip()
        if not label:
            continue
        rows.append({
            "id": str(row.get("id") or _key(label)),
            "label": label,
            "domain": "service_fee",
            "target_type": "service",
            "aliases": _zone_aliases(zone, label),
            "evidence": f"service={label}; zone={zone}; duration={row.get('duration_minutes')} minutes; capacity={row.get('capacity_persons')}",
            "sources": tuple(str(source_id) for source_id in row.get("source_ids") or [] if source_id),
            "metadata": {"zone": zone, "duration_minutes": row.get("duration_minutes"), "capacity_persons": row.get("capacity_persons")},
        })
    return tuple(rows)


@lru_cache(maxsize=1)
def _game_targets() -> tuple[dict[str, Any], ...]:
    alias_rows = {
        _key(str(row.get("game") or "")): row
        for row in _read_jsonl(CURATED_DIR / "game_title_aliases.jsonl")
        if row.get("game")
    }
    games: dict[str, dict[str, Any]] = {}
    for row in _read_jsonl(CURATED_DIR / "service_game_availability.jsonl"):
        zone = str(row.get("zone") or "").strip()
        source_ids = tuple(str(source_id) for source_id in row.get("source_ids") or [] if source_id)
        for raw_game in row.get("games") or []:
            game = str(raw_game or "").strip()
            key = _key(game)
            if not game or not key:
                continue
            current = games.setdefault(
                key,
                {
                    "id": key,
                    "label": game,
                    "domain": "games",
                    "target_type": "game",
                    "aliases": set(),
                    "zones": set(),
                    "sources": set(),
                },
            )
            current["aliases"].add(game)
            if ":" in game:
                suffix = game.split(":", 1)[1].strip()
                if suffix:
                    current["aliases"].add(suffix)
            for alias in alias_rows.get(key, {}).get("aliases") or []:
                current["aliases"].add(str(alias))
            if zone:
                current["zones"].add(zone)
            for source_id in source_ids:
                current["sources"].add(source_id)
    output: list[dict[str, Any]] = []
    for row in games.values():
        zones = tuple(sorted(row["zones"]))
        output.append({
            "id": row["id"],
            "label": row["label"],
            "domain": "games",
            "target_type": "game",
            "aliases": tuple(sorted(row["aliases"], key=lambda item: (-len(_compact(item)), item.lower()))),
            "evidence": f"game={row['label']}; zones={', '.join(zones)}",
            "sources": tuple(sorted(row["sources"])),
            "metadata": {"zones": zones},
        })
    output.sort(key=lambda item: str(item["label"]).lower())
    return tuple(output)


@lru_cache(maxsize=1)
def _competition_only_game_targets() -> tuple[dict[str, Any], ...]:
    current_ids = {str(row["id"]) for row in _game_targets()}
    grouped: dict[str, dict[str, Any]] = {}
    for row in _read_jsonl(CURATED_DIR / "curated_competition_rules.jsonl"):
        game = str(row.get("game") or "").strip()
        key = _key(game)
        if not game or not key or key in current_ids:
            continue
        current = grouped.setdefault(
            key,
            {"label": game, "aliases": {game}, "sources": set()},
        )
        parenthetical = re.findall(r"\(([^)]+)\)", game)
        current["aliases"].update(value.strip() for value in parenthetical if value.strip())
        without_parenthetical = re.sub(r"\s*\([^)]*\)\s*", " ", game).strip()
        if without_parenthetical:
            current["aliases"].add(without_parenthetical)
        for source_id in row.get("source_ids") or []:
            if source_id:
                current["sources"].add(str(source_id))
        if row.get("source_url"):
            current["sources"].add(str(row["source_url"]))

    targets: list[dict[str, Any]] = []
    for key, row in grouped.items():
        targets.append({
            "id": f"competition_game_{key}",
            "label": row["label"],
            "domain": "games",
            "target_type": "game",
            "aliases": tuple(sorted(row["aliases"], key=lambda item: (-len(_compact(item)), item.lower()))),
            "evidence": f"competition-known game={row['label']}; current service availability is not asserted",
            "sources": tuple(sorted(row["sources"])),
            "metadata": {"scope": "competition_rules", "current_availability": False},
        })
    targets.sort(key=lambda item: str(item["label"]).lower())
    return tuple(targets)


@lru_cache(maxsize=1)
def _equipment_targets() -> tuple[dict[str, Any], ...]:
    rows: list[dict[str, Any]] = []
    for row in _read_jsonl(CURATED_DIR / "equipment_item_details.jsonl"):
        item = str(row.get("item") or "").strip()
        if not item:
            continue
        zone = str(row.get("zone") or "").strip()
        aliases = {item, zone}
        for value in row.get("use_cases_th") or []:
            aliases.add(str(value))
        rows.append({
            "id": str(row.get("id") or _key(item)),
            "label": item,
            "domain": "equipment",
            "target_type": "equipment",
            "aliases": tuple(alias for alias in aliases if alias),
            "evidence": f"equipment={item}; zone={zone}; what={row.get('what_th') or ''}",
            "sources": (str(row.get("source_url") or ""),),
            "metadata": {"zone": zone},
        })
    return tuple(rows)


def _domain_bias(domain: str, operation: str, preferred_domains: tuple[str, ...]) -> float:
    bias = 0.0
    if domain in preferred_domains:
        bias += 0.22
    if operation in {"price", "price_lookup", "price_calculate"}:
        if domain == "service_fee":
            bias += 0.26
        elif domain == "games":
            bias += 0.04
        else:
            bias -= 0.08
    elif operation in {"booking", "reservation"}:
        if domain == "service_fee":
            bias += 0.18
        elif domain == "games":
            bias += 0.04
    elif operation in {"controls", "gameplay", "detail"}:
        if domain == "games":
            bias += 0.22
        elif domain == "equipment":
            bias += 0.02
        else:
            bias -= 0.24
    elif operation in {"equipment", "equipment_lookup"}:
        if domain == "equipment":
            bias += 0.24
        elif domain != "equipment":
            bias -= 0.10
    return bias


def _score_alias_match(query: str, target: dict[str, Any], operation: str, preferred_domains: tuple[str, ...]) -> TargetCandidate | None:
    q_norm = normalize_text(query)
    q_compact = _compact(query)
    q_tokens = _tokens(query)
    best_score = 0.0
    best_alias = ""
    match_type = ""
    for alias in target.get("aliases") or ():
        alias = str(alias or "").strip()
        alias_norm = normalize_text(alias)
        alias_compact = _compact(alias)
        if len(alias_compact) < 3 and not (target.get("target_type") == "service" and alias_compact in {"pc", "vr"}):
            continue
        score = 0.0
        current_match = ""
        if alias_norm and (
            alias_norm in q_norm
            and (not _is_short_latin_alias(alias) or alias_norm in q_tokens)
        ):
            score = 1.0
            current_match = "exact_alias"
        elif len(alias_compact) >= 4 and alias_compact in q_compact:
            score = 0.96
            current_match = "compact_alias"
        else:
            alias_tokens = _tokens(alias)
            overlap = alias_tokens.intersection(q_tokens)
            if overlap and len(overlap) >= max(1, min(2, len(alias_tokens))):
                score = min(0.86, 0.58 + (len(overlap) / max(1, len(alias_tokens))) * 0.24)
                current_match = "token_overlap"
            elif len(alias_compact) >= 5:
                fuzzy = _ratio(q_compact, alias_compact)
                if fuzzy >= 0.84:
                    score = fuzzy - 0.06
                    current_match = "fuzzy"
        if score > best_score:
            best_score = score
            best_alias = alias
            match_type = current_match
    if not best_score:
        return None
    score_ceiling = {
        "exact_alias": 1.0,
        "compact_alias": 0.97,
        "token_overlap": 0.91,
        "fuzzy": 0.90,
    }.get(match_type, 0.90)
    score = max(
        0.0,
        min(score_ceiling, best_score + _domain_bias(str(target["domain"]), operation, preferred_domains)),
    )
    return TargetCandidate(
        str(target["id"]),
        str(target["domain"]),
        str(target["target_type"]),
        str(target["label"]),
        score,
        match_type,
        best_alias,
        str(target.get("evidence") or ""),
        tuple(str(source) for source in target.get("sources") or () if source),
        dict(target.get("metadata") or {}),
    )


def _candidate_text(candidate: TargetCandidate, operation: str) -> str:
    return (
        f"domain: {candidate.domain}\n"
        f"type: {candidate.target_type}\n"
        f"label: {candidate.label}\n"
        f"operation: {operation or 'general'}\n"
        f"matched_alias: {candidate.matched_alias}\n"
        f"evidence: {candidate.evidence}"
    )


def _explicit_label_length(query: str, candidate: TargetCandidate) -> int:
    if candidate.target_type != "game":
        return 0
    q = normalize_text(query)
    label = normalize_text(candidate.label)
    if not label:
        return 0
    pattern = rf"(?<![0-9a-z]){re.escape(label)}(?![0-9a-z])"
    return len(_compact(label)) if re.search(pattern, q) else 0


def _rerank_targets(query: str, operation: str, candidates: tuple[TargetCandidate, ...]) -> tuple[TargetCandidate, ...] | None:
    if not target_reranker_enabled() or len(candidates) < 2:
        return None
    started = time.perf_counter()
    try:
        model = _load_target_reranker_model()
        pairs = [(query, _candidate_text(candidate, operation)) for candidate in candidates[:8]]
        raw_scores = model.predict(pairs, batch_size=max(1, int(os.getenv("PSU_TARGET_RERANKER_BATCH_SIZE", "4"))), show_progress_bar=False)
    except Exception:
        return None
    rescored: list[TargetCandidate] = []
    for candidate, raw_score in zip(candidates[:8], raw_scores):
        # Keep the rule-first score in the final ranking. Raw cross-encoder scores
        # are useful as a semantic tiebreaker, not as an unrestricted override.
        semantic = max(-8.0, min(8.0, float(raw_score)))
        blended = max(0.0, min(1.0, candidate.score + semantic * 0.035))
        rescored.append(TargetCandidate(
            candidate.target_id,
            candidate.domain,
            candidate.target_type,
            candidate.label,
            blended,
            f"{candidate.match_type}+rerank",
            candidate.matched_alias,
            candidate.evidence,
            candidate.sources,
            {**candidate.metadata, "target_rerank_score": round(float(raw_score), 4), "target_rerank_elapsed_sec": round(time.perf_counter() - started, 4)},
        ))
    rescored.extend(candidates[8:])
    rescored.sort(key=lambda item: (item.score, len(_compact(item.matched_alias))), reverse=True)
    return tuple(rescored)


def resolve_target_candidate(
    query: str,
    *,
    operation: str = "",
    preferred_domains: tuple[str, ...] = (),
) -> TargetResolution:
    targets = (*_service_targets(), *_game_targets(), *_competition_only_game_targets(), *_equipment_targets())
    scored = [
        candidate
        for target in targets
        if (candidate := _score_alias_match(query, target, operation, preferred_domains)) is not None
    ]
    # Prefer the most specific exact alias when parent and sequel aliases tie,
    # for example "Overcooked 2" over the parent alias "Overcooked".
    scored.sort(
        key=lambda item: (
            _explicit_label_length(query, item),
            item.score,
            len(_compact(item.matched_alias)),
        ),
        reverse=True,
    )
    if not scored:
        return TargetResolution("unknown", reason="no_target_candidate", operation=operation)

    candidates = tuple(scored[:8])
    top_explicit_length = _explicit_label_length(query, candidates[0])
    second_explicit_length = _explicit_label_length(query, candidates[1]) if len(candidates) > 1 else 0
    explicit_label_is_unique = top_explicit_length > second_explicit_length
    reranked = None if explicit_label_is_unique else _rerank_targets(query, operation, candidates)
    if reranked is not None:
        candidates = reranked
    top = candidates[0]
    second = candidates[1] if len(candidates) > 1 else None
    margin = top.score - second.score if second else 1.0

    exact_alias_is_more_specific = (
        second is None
        or not second.match_type.startswith(("exact_alias", "compact_alias"))
        or len(_compact(top.matched_alias)) > len(_compact(second.matched_alias))
    )
    if top_explicit_length and explicit_label_is_unique and top.score >= 0.90:
        status = "exact"
        reason = "explicit_canonical_title_overrides_normalized_alias_tie"
    elif top.match_type.startswith("exact_alias") and top.score >= 0.98 and exact_alias_is_more_specific:
        status = "exact"
        reason = "top_exact_alias_overrides_parent_match"
    elif top.score >= 0.92 and margin >= 0.10:
        status = "exact"
        reason = "top_target_high_confidence"
    elif top.score >= 0.76 and margin < 0.12:
        status = "ambiguous"
        reason = "top_targets_low_margin"
    elif top.score >= 0.76:
        status = "exact"
        reason = "top_target_acceptable"
    else:
        status = "unknown"
        reason = "top_target_below_threshold"

    return TargetResolution(
        status,
        top_candidate=top if status != "unknown" else None,
        candidates=candidates,
        top_score=top.score,
        margin=margin,
        reason=reason,
        operation=operation,
        metadata={"target_reranker_enabled": target_reranker_enabled(), "target_reranked": reranked is not None},
    )
