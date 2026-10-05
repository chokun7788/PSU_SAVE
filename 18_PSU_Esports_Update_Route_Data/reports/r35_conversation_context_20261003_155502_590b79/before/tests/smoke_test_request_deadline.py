from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402


def test_global_deadline_can_stop_request() -> None:
    result = answer_question_pipeline_debug(
        "Tekken 8 มีปุ่มอะไรบ้าง",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
        global_timeout_sec=0.000001,
    )
    assert result.mode == "pipeline:request_timeout_no_answer", result.mode
    assert result.route.category == "no_answer"
    assert result.route.intent == "request_timeout"
    assert any(item.stage == "deadline" and item.decision == "request_timeout_no_answer" for item in result.trace)
    assert "global_request_timeout" in result.validation.warnings


def test_no_global_deadline_keeps_normal_fast_answer() -> None:
    result = answer_question_pipeline_debug(
        "Tekken 8 มีปุ่มอะไรบ้าง",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
        global_timeout_sec=0,
    )
    assert result.mode != "pipeline:request_timeout_no_answer"
    assert result.route.category == "games"


if __name__ == "__main__":
    test_global_deadline_can_stop_request()
    test_no_global_deadline_keeps_normal_fast_answer()
    print("OK request deadline")
