from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import Any

from app.core.normalization import normalize_text
from app.pipeline.query_signals import contains_ascii_bounded
from app.pipeline.schemas import EntityBundle, PipelineRoute, PipelineTrace


MATRIX_PATH = Path(__file__).resolve().parents[2] / "data" / "routing" / "route_priority_matrix.json"


def _has_any(query: str, terms: list[str]) -> list[str]:
    hits: list[str] = []
    for term in terms:
        value = normalize_text(str(term))
        if not value:
            continue
        matched = contains_ascii_bounded(query, value)
        if matched:
            hits.append(str(term))
    return hits


@lru_cache(maxsize=1)
def _load_matrix() -> dict[str, Any]:
    if not MATRIX_PATH.exists():
        return {"rules": []}
    return json.loads(MATRIX_PATH.read_text(encoding="utf-8"))


def apply_routing_priority_policy(
    query: str,
    route: PipelineRoute,
    entities: EntityBundle,
) -> tuple[PipelineRoute, PipelineTrace | None]:
    """Apply small deterministic conflict-resolution rules after the router.

    This layer is intentionally data-driven and narrow: it only changes the
    route when a high-priority operation word conflicts with a broad entity
    route, such as price terms plus Nintendo/PS5 entities.
    """
    q = normalize_text(query)
    matrix = _load_matrix()

    for rule in matrix.get("rules", []):
        priority_over = {str(item) for item in rule.get("priority_over_categories", [])}
        forced = rule.get("force_route") or {}
        forced_category = str(forced.get("category", ""))
        forced_intent = str(forced.get("intent", ""))

        if not forced_category or not forced_intent:
            continue
        if route.category == forced_category and route.intent == forced_intent:
            continue
        if route.category not in priority_over:
            continue

        blocked_hits = _has_any(q, [str(item) for item in rule.get("blocked_by_any", [])])
        if blocked_hits:
            continue

        keyword_hits = _has_any(q, [str(item) for item in rule.get("when_any", [])])
        if not keyword_hits:
            continue

        entity_hits = _has_any(q, [str(item) for item in rule.get("when_any_entity", [])])
        if rule.get("when_any_entity") and not entity_hits:
            if not (entities.service or entities.user_group or entities.price_intent):
                continue

        new_route = PipelineRoute(
            forced_category,
            forced_intent,
            max(route.confidence, float(forced.get("confidence", route.confidence))),
            str(forced.get("answer_type", route.answer_type)),
            str(forced.get("risk", route.risk)),
            f"{route.reason}; routing_policy={rule.get('id')}",
        )
        trace = PipelineTrace(
            "routing_policy",
            f"{route.category}/{route.intent} -> {new_route.category}/{new_route.intent}",
            new_route.confidence,
            str(rule.get("description", rule.get("id", ""))),
            {
                "rule_id": rule.get("id"),
                "keyword_hits": keyword_hits,
                "entity_hits": entity_hits,
                "original_category": route.category,
                "original_intent": route.intent,
                "original_confidence": route.confidence,
                "forced_category": forced_category,
                "forced_intent": forced_intent,
                "entity_service": entities.service,
                "entity_user_group": entities.user_group,
                "entity_price_intent": entities.price_intent,
            },
        )
        return new_route, trace

    return route, None
