from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Any

from app.pipeline.request_deadline import remaining_sec
from app.pipeline.query_signals import looks_like_clear_general_request
from app.pipeline.schemas import PipelineRoute


def _truthy(value: str | None, *, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


def model_first_enabled() -> bool:
    return _truthy(os.getenv("PSU_MODEL_FIRST_FLOW"), default=False)


def preflight_llm_allowed(route: PipelineRoute, allow_llm: bool, query: str = "") -> tuple[bool, str]:
    """Gate optional intent/router reviews before they consume the request budget."""
    if not allow_llm:
        return False, "request did not allow LLM"
    if route.category == "general" and looks_like_clear_general_request(query):
        return False, "clear general request reserves one LLM call for final answer generation"

    exact_categories = {
        "games",
        "service_fee",
        "schedule",
        "competition_rules",
        "members",
        "reservation",
    }
    exact_intents = {
        "list",
        "games_lookup",
        "game_catalog_lookup",
        "game_availability_lookup",
        "price_lookup",
        "price_calculate",
        "schedule_lookup",
        "competition_rules_lookup",
        "members_lookup",
    }
    confidence_floor = max(0.0, float(os.getenv("PSU_MODEL_FIRST_PREFLIGHT_CONFIDENCE", "0.90")))
    if route.confidence >= confidence_floor and (
        route.category in exact_categories or route.intent in exact_intents
    ):
        return False, "high-confidence deterministic route"
    if not model_first_enabled():
        return True, "model-first flow disabled; preserve existing policy for ambiguous routes"
    if route.category in {"knowledge", "events_news"} and route.confidence >= 0.72:
        return False, "model-first RAG reserves budget for evidence and grounded composition"
    return True, "ambiguous route may benefit from model review"


@dataclass(frozen=True)
class ModelPlan:
    path: str
    use_llm: bool
    use_rag: bool
    use_rerank: bool
    reason: str
    min_remaining_sec: float

    def as_dict(self) -> dict[str, Any]:
        return {
            "path": self.path,
            "use_llm": self.use_llm,
            "use_rag": self.use_rag,
            "use_rerank": self.use_rerank,
            "reason": self.reason,
            "min_remaining_sec": self.min_remaining_sec,
        }


def retrieval_budget(query: str, route: PipelineRoute) -> dict[str, Any]:
    """Choose retrieval width before any expensive reranker/model call."""
    clean = str(query or "").strip().lower()
    complex_signals = (
        len(clean) >= 80,
        any(token in clean for token in ("แล้ว", "และ", "เปรียบเทียบ", "สรุป", "รายละเอียด", "ทั้งหมด")),
        route.intent in {"knowledge_lookup", "game_detail_lookup", "game_control_lookup"},
    )
    broad = sum(bool(item) for item in complex_signals) >= 2
    candidate_limit = 12 if broad else 8
    final_limit = 5 if broad else 4
    return {
        "candidate_limit": candidate_limit,
        "final_limit": final_limit,
        "broad_or_complex": broad,
        "rerank_requested": model_first_enabled() and (broad or candidate_limit > final_limit),
        "reason": "broad_or_complex_query" if broad else "clear_retrieval_budget",
    }


def plan_rag_model_path(
    *,
    query: str,
    route: PipelineRoute,
    allow_llm: bool,
    hit_count: int,
    retrieval_confidence: float,
    source_conflict: bool = False,
) -> ModelPlan:
    remaining = remaining_sec()
    # A grounded composer needs enough time to finish generation and leave the
    # finalizer reserve intact; calling it with a nearly exhausted deadline
    # only creates a timeout followed by a deterministic fallback.
    minimum = max(0.0, float(os.getenv("PSU_MODEL_FIRST_MIN_REMAINING_SEC", "6.0")))
    if not model_first_enabled():
        return ModelPlan("deterministic_rag", False, True, False, "model-first flow disabled", minimum)
    if not allow_llm:
        return ModelPlan("deterministic_rag", False, True, False, "request did not allow LLM", minimum)
    if remaining is not None and remaining < minimum:
        return ModelPlan("deterministic_rag", False, True, False, "insufficient remaining request budget", minimum)
    if source_conflict:
        return ModelPlan("deterministic_rag", False, True, False, "source conflict requires deterministic review", minimum)
    if route.category in {"service_fee", "schedule", "competition_rules", "members"} and retrieval_confidence >= 0.82:
        return ModelPlan("structured_first", False, True, False, "exact PSU fact should stay deterministic", minimum)
    if hit_count <= 1 and retrieval_confidence >= 0.86:
        return ModelPlan(
            "deterministic_rag",
            False,
            True,
            False,
            "single high-confidence evidence item does not need generative rewriting",
            minimum,
        )
    return ModelPlan(
        "rag_grounded_composer",
        True,
        hit_count > 0,
        hit_count >= 2,
        "model-first RAG path has evidence and enough budget",
        minimum,
    )
