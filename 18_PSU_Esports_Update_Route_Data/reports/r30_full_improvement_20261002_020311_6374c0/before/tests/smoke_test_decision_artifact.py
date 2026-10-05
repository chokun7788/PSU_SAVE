from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.pipeline.engine import answer_question_pipeline_debug


def _candidate_ids(artifact: dict) -> set[str]:
    return {str(item.get("capability_id")) for item in artifact.get("candidates") or []}


def _rejected_ids(artifact: dict) -> set[str]:
    return {str(item.get("capability_id")) for item in artifact.get("rejected") or []}


def test_structured_question_has_decision_artifact() -> None:
    result = answer_question_pipeline_debug(
        "สมาชิก PSU Esport มีกี่หมวด",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    artifact = result.decision_artifact
    assert artifact is not None
    assert artifact["intent"]["domain"] == "members"
    assert artifact["final"]["mode"] == result.mode
    assert artifact["final"]["evidence_count"] == len(result.hits)
    assert artifact["final"]["executed_capability"] == "structured.members"
    assert artifact["final"]["selected_matches_execution"] is True
    assert "structured.members" in _candidate_ids(artifact)
    assert artifact["policy"]["general_llm_requires_non_psu"] is True
    assert artifact["tool_preconditions"]
    assert artifact["execution_plan"][-1] == "format_validate_and_record"
    assert "apply_tool_preconditions" in artifact["execution_plan"]
    metrics = artifact["production_metrics"]
    assert metrics["policy_version"] == "correctness_control_flow_v2"
    assert metrics["outcome"] == "answered"
    assert metrics["quality_gate_status"] == "pass"
    assert metrics["llm_call_count"] == 0


def test_general_question_can_rank_general_llm() -> None:
    result = answer_question_pipeline_debug(
        "เมืองหลวงประเทศไทยคืออะไร",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    artifact = result.decision_artifact
    assert artifact is not None
    assert artifact["policy"]["psu_specific"] is False
    assert "llm.general_answer" in _candidate_ids(artifact)
    assert artifact["final"]["executed_capability"] in {"fallback.no_answer", "llm.general_answer"}
    assert artifact["production_metrics"]["quality_gate_status"] == "safe_abstain"


def test_repair_is_visible_in_production_metrics() -> None:
    result = answer_question_pipeline_debug(
        "ROV คือเกมอะไร",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    artifact = result.decision_artifact
    assert artifact is not None
    metrics = artifact["production_metrics"]
    assert metrics["repair_attempted"] is True
    assert metrics["repair_recovered"] is True
    assert metrics["quality_gate_status"] == "pass"
    assert "repair_attempted" in metrics["shadow_review_reasons"]


if __name__ == "__main__":
    test_structured_question_has_decision_artifact()
    print("OK structured artifact")
    test_general_question_can_rank_general_llm()
    print("OK general artifact")
    test_repair_is_visible_in_production_metrics()
    print("OK repair metrics")
    print("DECISION ARTIFACT SMOKE TEST OK")
