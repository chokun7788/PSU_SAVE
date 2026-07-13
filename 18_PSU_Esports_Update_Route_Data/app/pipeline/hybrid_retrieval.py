from __future__ import annotations

from typing import Any

from app.core.normalization import normalize_text
from app.pipeline.retrieval import (
    _game_row_entity_match,
    answer_from_curated_hits,
    hit_from_curated,
    retrieve_curated,
)
from app.pipeline.schemas import PipelineRoute, PipelineTrace
from app.pipeline.vector_retrieval import retrieve_vector_guarded


HYBRID_CATEGORIES = {"games", "equipment", "knowledge", "events_news"}
LEGACY_CURATED_SKIP_CATEGORIES = {"games", "equipment"}

GAME_DETAIL_TERMS = (
    "คืออะไร", "อะไรคือ", "วิธีเล่น", "สอนเล่น", "เล่นยังไง", "เล่นอย่างไร",
    "แนวอะไร", "เกี่ยวกับอะไร",
)
BROAD_GAME_LIST_TERMS = (
    "มีเกมอะไร", "เกมอะไรบ้าง", "เกมอะไรให้เล่น", "เกมทั้งหมด", "รายชื่อเกม",
    "รายการเกม", "แนวเกม", "ประเภทเกม", "มีอะไรบ้าง",
)
COMPETITION_TERMS = (
    "แข่ง", "แข่งขัน", "กติกา", "กฎ", "ทัวร์", "tournament", "ลงแข่ง",
    "รางวัล", "ทีม", "ผู้เล่น", "match", "round",
)


def should_use_hybrid_retrieval(route: PipelineRoute) -> bool:
    return route.category in HYBRID_CATEGORIES


def should_skip_legacy_curated_after_hybrid(route: PipelineRoute) -> bool:
    return route.category in LEGACY_CURATED_SKIP_CATEGORIES


def _has(q: str, *terms: str) -> bool:
    return any(term in q for term in terms)


def _row_key(row: dict[str, Any]) -> tuple[str, str, str]:
    return (
        str(row.get("id", "")),
        str(row.get("_source_file", "")),
        str(row.get("source_url", "")),
    )


def _route_allows_category(route: PipelineRoute, row: dict[str, Any]) -> bool:
    category = str(row.get("category", ""))
    if category == route.category:
        return True
    if route.category == "equipment" and route.intent == "equipment_game_catalog" and category == "games":
        return True
    return False


def _looks_like_game_detail(query: str) -> bool:
    q = normalize_text(query)
    return _has(q, *GAME_DETAIL_TERMS)


def _looks_like_broad_game_list(query: str) -> bool:
    q = normalize_text(query)
    return _has(q, *BROAD_GAME_LIST_TERMS)


def _guard_candidate(query: str, route: PipelineRoute, row: dict[str, Any]) -> tuple[bool, str]:
    category = str(row.get("category", ""))
    q = normalize_text(query)

    if not _route_allows_category(route, row):
        return False, "category_mismatch"
    if category == "competition_rules" and route.category != "competition_rules":
        return False, "competition_blocked"
    if _has(q, *COMPETITION_TERMS) and category != "competition_rules" and route.category == "competition_rules":
        return False, "competition_route_requires_rules"

    if route.category in {"games", "equipment"} and category == "games":
        if _looks_like_broad_game_list(q):
            return False, "broad_game_list_needs_fast_path"
        if _looks_like_game_detail(q) and not _game_row_entity_match(q, row):
            entity_score = float(row.get("_entity_score", 0.0) or 0.0)
            if entity_score < 0.45:
                return False, "weak_game_entity"

    if route.category == "equipment" and category == "equipment":
        if _has(q, "เกม", "game", "games") and not _has(q, "อุปกรณ์", "เครื่อง", "ใช้งาน", "วิธีใช้"):
            return False, "equipment_doc_for_game_query_blocked"

    return True, "ok"


def _hybrid_score(row: dict[str, Any], origin_count: int) -> float:
    score = float(row.get("_score", 0.0) or 0.0)
    vector_score = float(row.get("_vector_score", 0.0) or 0.0)
    lexical_score = float(row.get("_lexical_score", 0.0) or 0.0)
    entity_score = float(row.get("_entity_score", 0.0) or 0.0)
    priority = float(row.get("priority", 0.0) or 0.0) / 100.0
    return score + (vector_score * 6.0) + (lexical_score * 3.0) + (entity_score * 5.0) + priority + (origin_count - 1) * 1.5


def retrieve_hybrid_guarded(query: str, route: PipelineRoute, limit: int = 4) -> tuple[list[dict[str, Any]], PipelineTrace]:
    curated_hits, curated_trace = retrieve_curated(query, route.category, limit=8)
    vector_hits, vector_trace = retrieve_vector_guarded(query, route, limit=8)

    merged: dict[tuple[str, str, str], dict[str, Any]] = {}
    origins: dict[tuple[str, str, str], set[str]] = {}
    blocked: dict[str, int] = {}

    for origin, rows in (("curated", curated_hits), ("vector", vector_hits)):
        for row in rows:
            ok, reason = _guard_candidate(query, route, row)
            if not ok:
                blocked[reason] = blocked.get(reason, 0) + 1
                continue
            key = _row_key(row)
            if key not in merged:
                merged[key] = dict(row)
                origins[key] = set()
            origins[key].add(origin)
            if float(row.get("_score", 0.0) or 0.0) > float(merged[key].get("_score", 0.0) or 0.0):
                merged[key].update(row)

    scored: list[tuple[float, dict[str, Any]]] = []
    for key, row in merged.items():
        origin_set = origins.get(key, set())
        score = _hybrid_score(row, len(origin_set))
        row = dict(row)
        row["_hybrid_score"] = round(score, 3)
        row["_hybrid_origins"] = sorted(origin_set)
        scored.append((score, row))

    scored.sort(key=lambda item: item[0], reverse=True)
    hits = [row for _, row in scored[:limit]]
    confidence = min(0.91, 0.50 + (hits[0]["_hybrid_score"] / 24 if hits else 0.0))
    detail = f"hits={len(hits)} curated={len(curated_hits)} vector={len(vector_hits)}"
    if hits:
        detail += f" top={hits[0].get('id')} score={hits[0].get('_hybrid_score')} origins={','.join(hits[0].get('_hybrid_origins', []))}"
    elif blocked:
        detail += " blocked=" + ", ".join(f"{key}:{value}" for key, value in sorted(blocked.items())[:4])

    return hits, PipelineTrace(
        "hybrid_retrieval",
        "guarded_candidate_rerank",
        confidence,
        detail,
        {
            "category": route.category,
            "intent": route.intent,
            "curated_trace": curated_trace.detail,
            "vector_trace": vector_trace.detail,
        },
    )


def answer_from_hybrid_hits(hits: list[dict[str, Any]], query: str = "") -> tuple[str | None, list[dict[str, Any]], float]:
    if not hits:
        return None, [], 0.0
    score = float(hits[0].get("_hybrid_score", 0.0) or 0.0)
    category = str(hits[0].get("category", ""))
    minimum = 5.0
    if category in {"knowledge", "events_news"}:
        minimum = 6.0
    if category == "games" and _looks_like_game_detail(query):
        minimum = 5.5
    if score < minimum:
        return None, [], min(0.58, score / 12)

    answer, raw_hits, confidence = answer_from_curated_hits(hits, query)
    if answer is None:
        return None, [], confidence
    if not raw_hits:
        raw_hits = [hit_from_curated(row) for row in hits[:2]]
    return answer, raw_hits, min(0.89, max(confidence, 0.58 + score / 26))
