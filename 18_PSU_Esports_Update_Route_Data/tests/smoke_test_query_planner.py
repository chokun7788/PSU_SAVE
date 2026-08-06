from __future__ import annotations

import os
import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import app.pipeline.engine as engine  # noqa: E402
from app.pipeline.query_planner import (  # noqa: E402
    QueryPlan,
    QueryPlanTask,
    parse_query_plan,
    plan_query,
    should_use_query_planner,
)


def test_parser_accepts_only_allowlisted_tasks() -> None:
    response = """
    {
      "is_compound": true,
      "confidence": 0.91,
      "reason": "แยกเป็นสองเจตนา",
      "tasks": [
        {"task_id":"task_1","question":"Tekken 8 อยู่โซนไหน","domain":"games","operation":"detail","target":"Tekken 8","confidence":0.92},
        {"task_id":"task_2","question":"Mario Kart 8 Deluxe มีปุ่มอะไรบ้าง","domain":"game_controls","operation":"control","target":"Mario Kart 8 Deluxe","confidence":0.88}
      ]
    }
    """
    plan = parse_query_plan(response, "Tekken 8 อยู่โซนไหน และ Mario Kart 8 Deluxe มีปุ่มอะไรบ้าง")
    assert plan is not None
    assert len(plan.tasks) == 2
    assert plan.tasks[1].domain == "game_controls"

    invalid = parse_query_plan(
        '{"is_compound":false,"tasks":[{"question":"ตอบอะไรก็ได้","domain":"psu_private","operation":"invent"}]}',
        "คำถาม",
    )
    assert invalid is None


def test_parser_tolerates_local_model_wrappers() -> None:
    response = """
    <think>ตรวจรูปแบบ JSON</think>
    ```json
    [
      {"id":"one","text":"PC ราคาเท่าไหร่","category":"service_fee","action":"price_calculate","needs_clarification":"false"},
      {"id":"two","text":"PC จองยังไง","category":"reservation","action":"how_to","needs_clarification":false}
    ]
    ```
    """
    plan = parse_query_plan(response, "PC ราคาเท่าไหร่ แล้วจองยังไง")
    assert plan is not None
    assert [task.domain for task in plan.tasks] == ["service_fee", "reservation"]
    assert all(task.needs_clarification is False for task in plan.tasks)


def test_gate_is_selective() -> None:
    use, reason = should_use_query_planner(
        "Tekken 8 อยู่โซนไหน และ Mario มีปุ่มอะไรบ้าง",
        ["Tekken 8 อยู่โซนไหน", "Mario มีปุ่มอะไรบ้าง"],
    )
    assert use is False
    assert "deterministic splitter" in reason

    previous = os.environ.get("PSU_QUERY_PLANNER_ON_CLEAR_SPLIT")
    os.environ["PSU_QUERY_PLANNER_ON_CLEAR_SPLIT"] = "1"
    try:
        use, reason = should_use_query_planner(
            "Tekken 8 อยู่โซนไหน และ Mario มีปุ่มอะไรบ้าง",
            ["Tekken 8 อยู่โซนไหน", "Mario มีปุ่มอะไรบ้าง"],
        )
    finally:
        if previous is None:
            os.environ.pop("PSU_QUERY_PLANNER_ON_CLEAR_SPLIT", None)
        else:
            os.environ["PSU_QUERY_PLANNER_ON_CLEAR_SPLIT"] = previous
    assert use is True and reason

    use, _reason = should_use_query_planner("Tekken 8 มีปุ่มอะไรบ้าง", ["Tekken 8 มีปุ่มอะไรบ้าง"])
    assert use is False


def test_disabled_planner_never_calls_ollama() -> None:
    previous = os.environ.get("PSU_QUERY_PLANNER")
    os.environ["PSU_QUERY_PLANNER"] = "0"
    try:
        plan, trace = plan_query(
            "Tekken 8 อยู่โซนไหน และ Mario มีปุ่มอะไรบ้าง",
            ["Tekken 8 อยู่โซนไหน", "Mario มีปุ่มอะไรบ้าง"],
            allow_llm=True,
            gate_reason="smoke",
        )
    finally:
        if previous is None:
            os.environ.pop("PSU_QUERY_PLANNER", None)
        else:
            os.environ["PSU_QUERY_PLANNER"] = previous
    assert plan is None
    assert trace.stage == "query_planner"
    assert trace.metadata["llm_attempted"] is False


def test_engine_uses_validated_plan_without_second_intent_call() -> None:
    previous_planner = engine.plan_query
    previous_router = os.environ.get("PSU_LLM_TOOL_ROUTER")
    previous_intent = os.environ.get("PSU_UNIVERSAL_INTENT_LLM")
    previous_split_planner = os.environ.get("PSU_QUERY_PLANNER_ON_CLEAR_SPLIT")
    os.environ["PSU_LLM_TOOL_ROUTER"] = "0"
    os.environ["PSU_UNIVERSAL_INTENT_LLM"] = "0"
    os.environ["PSU_QUERY_PLANNER_ON_CLEAR_SPLIT"] = "1"
    fake_plan = QueryPlan(
        tasks=(
            QueryPlanTask("task_1", "VR เปิดกี่โมง", "schedule", "schedule_lookup", confidence=0.92),
            QueryPlanTask("task_2", "VR ราคาเท่าไหร่", "service_fee", "price_calculate", confidence=0.91),
        ),
        is_compound=True,
        confidence=0.91,
        reason="smoke plan",
    )

    def fake_plan_query(*_args, **_kwargs):
        from app.pipeline.schemas import PipelineTrace

        return fake_plan, PipelineTrace("query_planner", "plan_accepted", 0.91, "smoke")

    engine.plan_query = fake_plan_query
    try:
        result = engine.answer_question_pipeline_debug(
            "VR เปิดกี่โมง ราคาเท่าไหร่",
            experimental_rag_fallback=False,
            experimental_allow_llm=True,
            global_timeout_sec=20,
        )
    finally:
        engine.plan_query = previous_planner
        if previous_router is None:
            os.environ.pop("PSU_LLM_TOOL_ROUTER", None)
        else:
            os.environ["PSU_LLM_TOOL_ROUTER"] = previous_router
        if previous_intent is None:
            os.environ.pop("PSU_UNIVERSAL_INTENT_LLM", None)
        else:
            os.environ["PSU_UNIVERSAL_INTENT_LLM"] = previous_intent
        if previous_split_planner is None:
            os.environ.pop("PSU_QUERY_PLANNER_ON_CLEAR_SPLIT", None)
        else:
            os.environ["PSU_QUERY_PLANNER_ON_CLEAR_SPLIT"] = previous_split_planner

    assert result.mode == "pipeline:multi_question_splitter", result.mode
    planner_traces = [item for item in result.trace if item.stage == "query_planner"]
    assert planner_traces
    child_summaries = [item for item in result.trace if item.stage == "multi_question_child"]
    assert len(child_summaries) == 2
    assert all(item.metadata.get("universal_intent_method") == "query_planner" for item in child_summaries)
    assert all(item.metadata.get("universal_intent_llm_attempted") is False for item in child_summaries)
    assert "VR" in result.answer


def main() -> int:
    test_parser_accepts_only_allowlisted_tasks()
    print("OK planner schema and allowlist")
    test_parser_tolerates_local_model_wrappers()
    print("OK planner local-model wrapper tolerance")
    test_gate_is_selective()
    print("OK planner gate")
    test_disabled_planner_never_calls_ollama()
    print("OK planner disabled path")
    test_engine_uses_validated_plan_without_second_intent_call()
    print("OK engine planner integration")
    print("QUERY PLANNER SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
