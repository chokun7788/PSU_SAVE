from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from app.pipeline.llm_tool_router import ToolRoutingDecision
from app.pipeline.question_frame import QuestionFrame, build_question_frame
from app.pipeline.schemas import PipelineRoute, PipelineTrace, UniversalIntent
from app.pipeline.tool_preconditions import evaluate_capability_precondition


PSU_DOMAINS = {
    "members",
    "games",
    "game_controls",
    "equipment",
    "reservation",
    "service_fee",
    "schedule",
    "competition_rules",
    "rules",
    "penalty",
    "contact",
    "overview",
    "knowledge",
    "events_news",
}


@dataclass(frozen=True)
class Capability:
    capability_id: str
    domain: str
    action: str
    answer_types: tuple[str, ...]
    risk: str
    requires_evidence: bool
    base_score: float
    timeout_ms: int
    description: str


@dataclass(frozen=True)
class CandidateDecision:
    capability_id: str
    action: str
    domain: str
    score: float
    status: str
    reason: str
    requires_evidence: bool
    risk: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "capability_id": self.capability_id,
            "action": self.action,
            "domain": self.domain,
            "score": round(self.score, 3),
            "status": self.status,
            "reason": self.reason,
            "requires_evidence": self.requires_evidence,
            "risk": self.risk,
        }


CAPABILITIES: tuple[Capability, ...] = (
    Capability("structured.members", "members", "structured", ("fact", "list", "count"), "low", True, 0.88, 250, "member group and profile facts"),
    Capability("structured.games", "games", "structured", ("fact", "list", "count", "how_to"), "low", True, 0.88, 300, "game catalog and game detail facts"),
    Capability("structured.game_controls", "game_controls", "structured", ("fact", "list", "how_to"), "low", True, 0.90, 350, "verified game control facts"),
    Capability("structured.equipment", "equipment", "structured", ("fact", "list"), "low", True, 0.88, 300, "equipment and zone facts"),
    Capability("structured.reservation", "reservation", "structured", ("fact", "how_to"), "medium", True, 0.86, 300, "booking policy facts"),
    Capability("structured.schedule", "schedule", "structured", ("fact", "list"), "medium", True, 0.86, 300, "service schedule facts"),
    Capability("structured.service_fee", "service_fee", "structured", ("fact", "calculation"), "medium", True, 0.86, 350, "service fee facts"),
    Capability("fast.price_calculator", "service_fee", "fast_path", ("calculation",), "medium", True, 0.93, 120, "deterministic price and time-range calculator"),
    Capability("fast.domain_handlers", "multi", "fast_path", ("fact", "list", "summary"), "medium", True, 0.78, 180, "deterministic domain fast answers"),
    Capability("rulebase.category_rules", "multi", "rulebase", ("fact", "how_to"), "medium", True, 0.74, 150, "pattern rules from data/rules"),
    Capability("retrieval.competition_fact_cards", "competition_rules", "retrieval", ("fact", "list"), "medium", True, 0.82, 600, "competition rule fact cards"),
    Capability("retrieval.hybrid_guarded", "multi", "retrieval", ("fact", "summary"), "medium", True, 0.72, 900, "guarded BM25/vector hybrid retrieval"),
    Capability("retrieval.vector_guarded", "multi", "vector", ("fact", "list"), "medium", True, 0.70, 900, "guarded vector retrieval"),
    Capability("llm.facts_composer", "multi", "rag_llm", ("fact", "list", "summary", "how_to"), "medium", True, 0.62, 8000, "local LLM rewrites verified facts only"),
    Capability("llm.general_answer", "general", "general_llm", ("general",), "low", False, 0.66, 40000, "local LLM for non-PSU general knowledge"),
    Capability("clarification.ask_user", "clarification", "clarification", ("clarification",), "low", False, 0.58, 100, "ask for missing target or context"),
    Capability("fallback.no_answer", "no_answer", "no_answer", ("no_answer",), "low", False, 0.50, 100, "verified data unavailable response"),
)


def _route_domain(route: PipelineRoute, intent: UniversalIntent | None) -> str:
    if (
        intent
        and intent.domain
        and intent.domain not in {"unknown", "general"}
    ):
        return intent.domain
    return route.category


def _is_psu_specific(route: PipelineRoute, intent: UniversalIntent | None) -> bool:
    domain = _route_domain(route, intent)
    if route.category in PSU_DOMAINS or domain in PSU_DOMAINS:
        return True
    return route.risk in {"medium", "high"}


def _score_capability(
    capability: Capability,
    route: PipelineRoute,
    intent: UniversalIntent | None,
    tool_decision: ToolRoutingDecision | None,
    frame: QuestionFrame | None,
) -> tuple[float, list[str]]:
    score = capability.base_score
    reasons: list[str] = [f"base={capability.base_score:.2f}"]
    domain = _route_domain(route, intent)
    operation = intent.operation if intent else ""

    if capability.domain == domain:
        score += 0.12
        reasons.append("domain_match")
    elif capability.domain == "multi" and domain in PSU_DOMAINS:
        score += 0.04
        reasons.append("multi_domain")

    if capability.action == route.answer_type:
        score += 0.03
        reasons.append("answer_type_action_match")

    if route.answer_type in capability.answer_types:
        score += 0.06
        reasons.append("answer_type_match")

    if tool_decision is not None and capability.action == tool_decision.action:
        score += 0.10 * max(0.0, tool_decision.confidence)
        reasons.append(f"tool_router_action={tool_decision.action}")

    if tool_decision is not None and capability.domain == tool_decision.domain:
        score += 0.06
        reasons.append(f"tool_router_domain={tool_decision.domain}")

    if operation in {"price_calculate", "price_lookup"} and capability.capability_id == "fast.price_calculator":
        score += 0.18
        reasons.append("price_calculation_priority")

    if operation in {"control", "how_to_play"} and capability.capability_id == "structured.game_controls":
        score += 0.16
        reasons.append("game_control_priority")

    if operation in {"list", "count", "group_count", "lookup"} and capability.action == "structured" and capability.domain == domain:
        score += 0.10
        reasons.append("structured_operation_priority")

    if route.category == "general" and capability.capability_id == "llm.general_answer":
        score += 0.18
        reasons.append("general_route_priority")

    if route.category == "competition_rules" and capability.capability_id == "retrieval.competition_fact_cards":
        score += 0.18
        reasons.append("competition_fact_card_priority")

    if frame is not None:
        if capability.domain == frame.domain:
            score += 0.20
            reasons.append("question_frame_domain_match")
        elif (
            capability.action == "structured"
            and capability.domain not in {"multi", "general", "clarification", "no_answer"}
            and frame.domain not in {"general", "unknown"}
        ):
            score -= 0.10
            reasons.append("question_frame_domain_mismatch")

        operation_priority: dict[str, tuple[str, float]] = {
            "control_lookup": ("structured.game_controls", 0.30),
            "price_lookup": ("fast.price_calculator", 0.32),
            "price_calculate": ("fast.price_calculator", 0.32),
            "booking_lookup": ("structured.reservation", 0.28),
            "booking_session_limit": ("structured.reservation", 0.30),
            "schedule_lookup": ("structured.schedule", 0.28),
            "game_zone_rank": ("structured.games", 0.32),
            "game_catalog": ("structured.games", 0.28),
            "game_detail": ("structured.games", 0.28),
            "game_how_to": ("structured.games", 0.28),
            "equipment_lookup": ("structured.equipment", 0.28),
            "member_lookup": ("structured.members", 0.28),
            "studio_rule_lookup": ("fast.domain_handlers", 0.30),
        }
        preferred = operation_priority.get(frame.operation)
        if preferred and capability.capability_id == preferred[0]:
            score += preferred[1]
            reasons.append(f"question_frame_operation={frame.operation}")
        if frame.operation == "game_how_to" and capability.capability_id == "structured.game_controls":
            score -= 0.14
            reasons.append("explicit_control_terms_missing")
        if frame.operation == "game_zone_rank" and capability.capability_id == "structured.equipment":
            score -= 0.18
            reasons.append("ranking_is_about_game_count")
        if (
            frame.operation in {"price_lookup", "price_calculate"}
            and frame.targets
            and frame.targets[0].target_type == "game"
        ):
            if capability.capability_id == "structured.service_fee":
                score += 0.38
                reasons.append("game_price_requires_service_mapping")
            elif capability.capability_id == "fast.price_calculator":
                score -= 0.36
                reasons.append("game_price_not_direct_calculator_input")

    return score, reasons


def _normalize_ranking_score(score: float) -> float:
    # Keep ranking margins after all boosts instead of clipping many candidates at 0.99.
    return max(0.0, min(0.999, score / 1.80))


def build_candidate_decisions(
    route: PipelineRoute,
    intent: UniversalIntent | None,
    tool_decision: ToolRoutingDecision | None = None,
    question: str = "",
) -> tuple[list[CandidateDecision], list[CandidateDecision], PipelineTrace]:
    accepted: list[CandidateDecision] = []
    rejected: list[CandidateDecision] = []
    psu_specific = _is_psu_specific(route, intent)
    frame = build_question_frame(question, route, intent) if question else None

    for capability in CAPABILITIES:
        score, reasons = _score_capability(capability, route, intent, tool_decision, frame)
        status = "accepted"
        reason = "; ".join(reasons)

        if capability.capability_id == "llm.general_answer" and psu_specific:
            status = "rejected"
            score = min(score, 0.25)
            reason = "policy_veto: PSU-specific or medium/high-risk route cannot use general LLM"
        elif capability.requires_evidence and route.category == "general" and capability.action != "retrieval":
            status = "rejected"
            score = min(score, 0.35)
            reason = "policy_veto: general route has no verified PSU evidence target"
        elif route.risk == "high" and capability.action in {"general_llm", "rag_llm"}:
            status = "rejected"
            score = min(score, 0.30)
            reason = "policy_veto: high-risk route cannot be model-only"

        if status == "accepted" and question:
            precondition = evaluate_capability_precondition(capability.capability_id, question, route, intent)
            if not precondition.ok:
                status = "rejected"
                score = min(score, 0.28)
                reason = f"precondition_veto: {precondition.reason}"
            else:
                if precondition.reason in {
                    "reservation_or_booking_query",
                    "price_calculator_applicable",
                    "competition_fast_handler_applicable",
                    "competition_rule_retrieval_applicable",
                    "specific_game_detail_allowed",
                    "game_domain_or_catalog_query",
                }:
                    score += 0.16
                reason = f"{reason}; precondition={precondition.reason}"

        score = _normalize_ranking_score(score)

        decision = CandidateDecision(
            capability_id=capability.capability_id,
            action=capability.action,
            domain=capability.domain,
            score=score,
            status=status,
            reason=reason,
            requires_evidence=capability.requires_evidence,
            risk=capability.risk,
        )
        if status == "accepted":
            accepted.append(decision)
        else:
            rejected.append(decision)

    accepted.sort(key=lambda item: item.score, reverse=True)
    rejected.sort(key=lambda item: item.score, reverse=True)
    selected = accepted[0] if accepted else CandidateDecision(
        "fallback.no_answer",
        "no_answer",
        "no_answer",
        0.50,
        "accepted",
        "no accepted candidate",
        False,
        "low",
    )
    second = accepted[1] if len(accepted) > 1 else None
    margin = selected.score - second.score if second is not None else 1.0
    same_action = second is not None and selected.action == second.action
    if not accepted:
        selection_status = "no_candidate"
        execution_allowed = False
    elif selected.score < 0.45:
        selection_status = "abstain_low_score"
        execution_allowed = False
    elif margin < 0.035 and not same_action and (frame is None or frame.operation == "unknown"):
        selection_status = "review_required"
        execution_allowed = False
    elif margin < 0.035:
        selection_status = "selected_low_margin"
        execution_allowed = True
    else:
        selection_status = "selected"
        execution_allowed = True
    trace = PipelineTrace(
        "decision_candidates",
        selected.capability_id,
        min(selected.score, 0.999),
        selected.reason,
        {
            "selected": selected.as_dict(),
            "selection": {
                "status": selection_status,
                "execution_allowed": execution_allowed,
                "margin": round(margin, 3),
                "same_action_as_second": same_action,
                "second": second.as_dict() if second is not None else None,
            },
            "question_frame": frame.as_dict() if frame is not None else None,
            "candidates": [item.as_dict() for item in accepted[:8]],
            "rejected": [item.as_dict() for item in rejected[:8]],
            "policy": {
                "psu_specific": psu_specific,
                "route_risk": route.risk,
                "general_llm_requires_non_psu": True,
            },
        },
    )
    return accepted, rejected, trace
