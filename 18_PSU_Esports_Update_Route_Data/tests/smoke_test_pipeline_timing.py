from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402


def _timing_decisions(result) -> set[str]:
    return {item.decision for item in result.trace if item.stage == "timing"}


def _assert_timing_metadata(result) -> None:
    timing_items = [item for item in result.trace if item.stage == "timing"]
    assert timing_items, "pipeline result should include timing trace entries"
    for item in timing_items:
        assert "elapsed_ms" in item.metadata, item
        assert item.metadata["elapsed_ms"] >= 0, item


def test_single_question_timing_trace() -> None:
    result = answer_question_pipeline_debug(
        "Tekken 8",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    decisions = _timing_decisions(result)
    _assert_timing_metadata(result)
    assert "split_multi_question" in decisions
    assert "preprocess" in decisions
    assert "active_route_selection" in decisions
    assert "structured_tool_execution" in decisions
    assert "build_result" in decisions


def test_multi_question_timing_trace() -> None:
    result = answer_question_pipeline_debug(
        "ถ้าเล่น Tekken 8 กับ Mario มีปุ่มอะไรบ้าง",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    decisions = _timing_decisions(result)
    _assert_timing_metadata(result)
    assert result.mode == "pipeline:multi_question_splitter"
    assert "multi_question_children_total" in decisions
    assert "multi_question_parent_preprocess" in decisions
    assert "multi_question_parent_entities" in decisions


if __name__ == "__main__":
    test_single_question_timing_trace()
    test_multi_question_timing_trace()
    print("OK pipeline timing trace")
