from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.compound_execution import build_compound_plan, classify_compound  # noqa: E402
from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402


def _decisions(result, stage: str) -> list[str]:
    return [item.decision for item in result.trace if item.stage == stage]


def main() -> int:
    independent = classify_compound(
        "PC ราคาเท่าไหร่ แล้วจองยังไง",
        ["PC ราคาเท่าไหร่", "PC จองยังไง"],
    )
    assert independent.can_parallelize is True
    assert independent.requires_planner is False
    assert build_compound_plan(
        "PC ราคาเท่าไหร่ แล้วจองยังไง",
        ["PC ราคาเท่าไหร่", "PC จองยังไง"],
        independent,
    ).nodes[1].depends_on == ()

    dependent = classify_compound(
        "อุปกรณ์ไหนเกมเยอะสุด แล้วราคาเครื่องนั้นเท่าไหร่",
        ["อุปกรณ์ไหนเกมเยอะสุด", "ราคาเครื่องนั้นเท่าไหร่"],
    )
    assert dependent.can_parallelize is False
    assert dependent.requires_planner is True
    dependent_plan = build_compound_plan(
        "อุปกรณ์ไหนเกมเยอะสุด แล้วราคาเครื่องนั้นเท่าไหร่",
        ["อุปกรณ์ไหนเกมเยอะสุด", "ราคาเครื่องนั้นเท่าไหร่"],
        dependent,
    )
    assert dependent_plan.nodes[1].depends_on == (1,)

    result = answer_question_pipeline_debug(
        "PC ราคาเท่าไหร่ แล้วจองยังไง",
        experimental_allow_llm=False,
        experimental_rag_fallback=False,
        global_timeout_sec=10,
    )
    assert "bounded_parallel" in _decisions(result, "compound_child_execution"), result.trace
    assert "ordered_dependency_chain" not in _decisions(result, "compound_plan")
    assert "PC" in result.answer
    print("OK independent compound uses bounded parallel")

    result = answer_question_pipeline_debug(
        "อุปกรณ์ไหนเกมเยอะสุด แล้วราคาเครื่องนั้นเท่าไหร่",
        experimental_allow_llm=False,
        experimental_rag_fallback=False,
        global_timeout_sec=10,
    )
    assert "ordered_dependency_chain" in _decisions(result, "compound_plan"), result.trace
    assert "ordered_sequential" in _decisions(result, "compound_child_execution"), result.trace
    assert "ต้องการให้คำนวณราคาของโซนไหน" in result.answer
    print("OK dependent compound remains ordered")

    result = answer_question_pipeline_debug(
        "Tekken 8 เล่นที่ไหน แล้วเกมนั้นมีปุ่มอะไร",
        experimental_allow_llm=False,
        experimental_rag_fallback=False,
        global_timeout_sec=10,
    )
    assert "TEKKEN 8 มีข้อมูลปุ่ม" in result.answer
    assert "ขอชื่อเกมก่อน" not in result.answer
    print("OK compound game reference resolves from prior evidence")
    print("COMPOUND EXECUTION SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
