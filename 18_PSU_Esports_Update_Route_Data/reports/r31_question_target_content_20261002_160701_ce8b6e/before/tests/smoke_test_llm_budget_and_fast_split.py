from __future__ import annotations

import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.pipeline.query_planner import should_use_query_planner  # noqa: E402
from app.pipeline.request_deadline import request_deadline, reserve_llm_call  # noqa: E402


def test_request_llm_budget_limits_attempts() -> None:
    previous = os.environ.get("PSU_LLM_MAX_CALLS")
    os.environ["PSU_LLM_MAX_CALLS"] = "2"
    try:
        with request_deadline(10):
            first, first_meta = reserve_llm_call("planner")
            second, second_meta = reserve_llm_call("general")
            third, third_meta = reserve_llm_call("composer")
    finally:
        if previous is None:
            os.environ.pop("PSU_LLM_MAX_CALLS", None)
        else:
            os.environ["PSU_LLM_MAX_CALLS"] = previous

    assert first is True and first_meta["llm_budget_used_calls"] == 1
    assert second is True and second_meta["llm_budget_used_calls"] == 2
    assert third is False
    assert third_meta["llm_budget_reason"] == "per-request LLM call budget exhausted"


def test_clear_split_skips_planner_by_default() -> None:
    previous = os.environ.get("PSU_QUERY_PLANNER_ON_CLEAR_SPLIT")
    os.environ.pop("PSU_QUERY_PLANNER_ON_CLEAR_SPLIT", None)
    try:
        use, reason = should_use_query_planner(
            "PC ราคาเท่าไหร่ แล้วจองยังไง",
            ["PC ราคาเท่าไหร่", "PC จองยังไง"],
        )
    finally:
        if previous is None:
            os.environ.pop("PSU_QUERY_PLANNER_ON_CLEAR_SPLIT", None)
        else:
            os.environ["PSU_QUERY_PLANNER_ON_CLEAR_SPLIT"] = previous

    assert use is False
    assert "planner skipped" in reason


def test_complex_compound_can_force_planner_gate() -> None:
    use, reason = should_use_query_planner(
        "อุปกรณ์ไหนเกมเยอะสุด แล้วราคาเครื่องนั้นเท่าไหร่",
        ["อุปกรณ์ไหนเกมเยอะสุด", "ราคาเครื่องนั้นเท่าไหร่"],
        force_complex=True,
    )
    assert use is True
    assert "complexity gate" in reason


if __name__ == "__main__":
    test_request_llm_budget_limits_attempts()
    test_clear_split_skips_planner_by_default()
    test_complex_compound_can_force_planner_gate()
    print("OK LLM budget and fast split")
