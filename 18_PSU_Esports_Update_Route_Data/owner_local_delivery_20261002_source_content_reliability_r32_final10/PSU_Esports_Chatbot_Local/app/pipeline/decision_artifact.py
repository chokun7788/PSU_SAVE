from __future__ import annotations

from typing import Any

from app.pipeline.schemas import EntityBundle, PipelineRoute, PipelineTrace, UniversalIntent, ValidationResult


def _trace_by_stage(trace: list[PipelineTrace], stage: str) -> PipelineTrace | None:
    for item in reversed(trace):
        if item.stage == stage:
            return item
    return None


def _traces_by_stage(trace: list[PipelineTrace], stage: str) -> list[PipelineTrace]:
    return [item for item in trace if item.stage == stage]


def _trace_dict(item: PipelineTrace | None) -> dict[str, Any] | None:
    if item is None:
        return None
    return {
        "stage": item.stage,
        "decision": item.decision,
        "confidence": item.confidence,
        "detail": item.detail,
        "metadata": item.metadata,
    }


def _source_ids(hits: list[dict[str, Any]]) -> list[str]:
    output: list[str] = []
    seen: set[str] = set()
    for hit in hits:
        metadata = hit.get("metadata", {}) if isinstance(hit, dict) else {}
        source_ids = metadata.get("source_ids")
        if isinstance(source_ids, list):
            raw_ids = [str(value) for value in source_ids]
        else:
            raw_ids = [str(hit.get("id") or metadata.get("title") or "")]
        for source_id in raw_ids:
            if source_id and source_id not in seen:
                seen.add(source_id)
                output.append(source_id)
    return output[:12]


def _execution_step_for_mode(mode: str) -> str:
    clean = mode.removeprefix("pipeline:")
    if clean.startswith("structured_"):
        return "execute_structured_tool"
    if "calculator" in clean or "fast_path" in clean:
        return "execute_fast_path"
    if "rule" in clean:
        return "execute_rulebase"
    if "hybrid" in clean:
        return "execute_hybrid_retrieval"
    if "vector" in clean:
        return "execute_vector_retrieval"
    if "rag" in clean or "curated" in clean or "fact_card" in clean:
        return "execute_retrieval"
    if "general_llm" in clean:
        return "execute_general_llm"
    if "clarification" in clean:
        return "ask_clarification"
    if "no_answer" in clean:
        return "answer_no_verified_data"
    return "execute_pipeline_fallback"


def _capability_for_mode(mode: str, trace: list[PipelineTrace]) -> str:
    clean = mode.removeprefix("pipeline:")
    if clean.startswith("structured_"):
        precondition = _trace_by_stage(trace, "tool_precondition")
        if precondition is not None:
            capability_id = str((precondition.metadata or {}).get("capability_id") or "")
            if capability_id.startswith("structured."):
                return capability_id
        if clean.startswith("structured_members"):
            return "structured.members"
        if clean.startswith("structured_game_controls"):
            return "structured.game_controls"
        if clean.startswith("structured_game") or clean.startswith("structured_games"):
            return "structured.games"
        if clean.startswith("structured_equipment"):
            return "structured.equipment"
        if clean.startswith("structured_booking") or clean.startswith("structured_reservation"):
            return "structured.reservation"
        if clean.startswith("structured_schedule"):
            return "structured.schedule"
        if clean.startswith("structured_service_fee"):
            return "structured.service_fee"
    if "calculator" in clean:
        return "fast.price_calculator"
    if "fast_path" in clean:
        return "fast.domain_handlers"
    if "rule" in clean:
        return "rulebase.category_rules"
    if "fact_card" in clean:
        return "retrieval.competition_fact_cards"
    if "hybrid" in clean:
        return "retrieval.hybrid_guarded"
    if "vector" in clean:
        return "retrieval.vector_guarded"
    if "rag" in clean or "curated" in clean:
        return "retrieval.hybrid_guarded"
    if "general_llm" in clean:
        return "llm.general_answer"
    if "clarification" in clean:
        return "clarification.ask_user"
    if "no_answer" in clean:
        return "fallback.no_answer"
    return "pipeline.unknown"


def _outcome_for_mode(mode: str) -> str:
    clean = mode.removeprefix("pipeline:")
    if "timeout" in clean:
        return "timeout"
    if "clarification" in clean or clean.endswith("missing_game_context"):
        return "clarification"
    if "no_answer" in clean or clean == "general_llm_disabled":
        return "no_answer"
    return "answered"


def build_decision_artifact(
    *,
    mode: str,
    confidence: float,
    route: PipelineRoute,
    entities: EntityBundle,
    validation: ValidationResult,
    trace: list[PipelineTrace],
    hits: list[dict[str, Any]],
    universal_intent: UniversalIntent | None,
) -> dict[str, Any]:
    candidates_trace = _trace_by_stage(trace, "decision_candidates")
    tool_router_trace = _trace_by_stage(trace, "tool_router")
    structured_trace = _trace_by_stage(trace, "structured_tool")
    validation_trace = _trace_by_stage(trace, "validation")
    tool_preconditions = [_trace_dict(item) for item in _traces_by_stage(trace, "tool_precondition")]
    candidate_execution = [_trace_dict(item) for item in _traces_by_stage(trace, "candidate_execution")]
    repair_traces = _traces_by_stage(trace, "repair_controller")
    ambiguity_trace = _trace_by_stage(trace, "ambiguity_gate")
    llm_calls = [
        {"stage": item.stage, "decision": item.decision, **dict(item.metadata.get("llm_call") or {})}
        for item in trace
        if isinstance(item.metadata.get("llm_call"), dict) and item.metadata.get("llm_call")
    ]
    final_step = _execution_step_for_mode(mode)
    executed_capability = _capability_for_mode(mode, trace)

    selected_candidate = None
    candidates: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    policy: dict[str, Any] = {}
    if candidates_trace is not None:
        selected_candidate = candidates_trace.metadata.get("selected")
        raw_candidates = candidates_trace.metadata.get("candidates")
        raw_rejected = candidates_trace.metadata.get("rejected")
        raw_policy = candidates_trace.metadata.get("policy")
        if isinstance(raw_candidates, list):
            candidates = [item for item in raw_candidates if isinstance(item, dict)]
        if isinstance(raw_rejected, list):
            rejected = [item for item in raw_rejected if isinstance(item, dict)]
        if isinstance(raw_policy, dict):
            policy = raw_policy

    selection = candidates_trace.metadata.get("selection", {}) if candidates_trace is not None else {}
    selection = selection if isinstance(selection, dict) else {}
    outcome = _outcome_for_mode(mode)
    repair_attempted = bool(repair_traces)
    selected_matches_execution = (
        isinstance(selected_candidate, dict)
        and str(selected_candidate.get("capability_id") or "") == executed_capability
    )
    quality_gate_status = (
        "safe_abstain"
        if outcome in {"clarification", "no_answer", "timeout"}
        else "pass"
        if validation.ok
        else "reject"
    )
    shadow_reasons: list[str] = []
    if repair_attempted:
        shadow_reasons.append("repair_attempted")
    if not selected_matches_execution:
        shadow_reasons.append("selected_execution_mismatch")
    if outcome != "answered":
        shadow_reasons.append(outcome)
    if validation.warnings:
        shadow_reasons.append("validation_warning")
    if llm_calls:
        shadow_reasons.append("llm_used")

    return {
        "intent": {
            "domain": universal_intent.domain if universal_intent else route.category,
            "operation": universal_intent.operation if universal_intent else route.intent,
            "target": universal_intent.target if universal_intent else "",
            "confidence": universal_intent.confidence if universal_intent else route.confidence,
            "method": universal_intent.method if universal_intent else "route",
        },
        "route": {
            "category": route.category,
            "intent": route.intent,
            "confidence": route.confidence,
            "answer_type": route.answer_type,
            "risk": route.risk,
            "reason": route.reason,
        },
        "tool_router": _trace_dict(tool_router_trace),
        "selected_candidate": selected_candidate,
        "candidates": candidates,
        "rejected": rejected,
        "policy": policy,
        "execution_plan": [
            "normalize_and_extract_entities",
            "route_and_resolve_universal_intent",
            "generate_capability_candidates",
            "apply_policy_and_rank",
            "apply_tool_preconditions",
            final_step,
            "format_validate_and_record",
        ],
        "final": {
            "mode": mode,
            "confidence": confidence,
            "execution_step": final_step,
            "executed_capability": executed_capability,
            "selected_matches_execution": selected_matches_execution,
            "validation_ok": validation.ok,
            "validation_errors": list(validation.errors),
            "validation_warnings": list(validation.warnings),
            "evidence_count": len(hits),
            "source_ids": _source_ids(hits),
        },
        "production_metrics": {
            "policy_version": "correctness_control_flow_v2",
            "outcome": outcome,
            "quality_gate_status": quality_gate_status,
            "candidate_margin": selection.get("margin"),
            "selection_status": selection.get("status", ""),
            "ambiguity_decision": ambiguity_trace.decision if ambiguity_trace is not None else "",
            "repair_attempted": repair_attempted,
            "repair_recovered": repair_attempted and outcome == "answered" and validation.ok,
            "llm_call_count": len(llm_calls),
            "requires_shadow_review": bool(shadow_reasons),
            "shadow_review_reasons": shadow_reasons,
        },
        "entities": {
            "day": entities.day,
            "time_slots": list(entities.time_slots),
            "service": entities.service,
            "user_group": entities.user_group,
            "duration": entities.duration,
            "price_intent": entities.price_intent,
        },
        "structured_tool": _trace_dict(structured_trace),
        "tool_preconditions": [item for item in tool_preconditions if item is not None],
        "candidate_execution": [item for item in candidate_execution if item is not None],
        "validation": _trace_dict(validation_trace),
        "llm_calls": llm_calls,
    }
