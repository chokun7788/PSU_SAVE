from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402


def assert_contains(text: str, expected: list[str], label: str) -> None:
    missing = [item for item in expected if item.lower() not in text.lower()]
    if missing:
        raise AssertionError(f"{label}: missing {missing}\n{text}")


def assert_not_contains(text: str, forbidden: list[str], label: str) -> None:
    found = [item for item in forbidden if item.lower() in text.lower()]
    if found:
        raise AssertionError(f"{label}: forbidden {found}\n{text}")


def check(question: str, expected: list[str]) -> None:
    result = answer_question_pipeline_debug(
        question,
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    assert result.route.category == "service_fee", result.route.category
    assert_contains(result.answer, expected, question)
    assert_not_contains(result.answer, ["ยังไม่พบราคา", "ยังไม่ควรคำนวณ"], question)
    print(f"OK {result.mode} | {question}")


def main() -> int:
    check("นักศึกษา PSU เล่น PC ราคาเท่าไหร่", ["PC", "0 บาท", "PSU Student and Staff"])
    check("นักศึกษา สจล อยากเล่น PC เสียเท่าไหร่", ["PC", "25 บาท", "General Student"])
    check("บุคคลทั่วไปเล่น PC กี่บาท", ["PC", "70 บาท", "General Adult"])
    check("ราคา PC ต่อชั่วโมงเท่าไหร่", ["PC", "0 บาท", "25 บาท", "70 บาท"])
    check("เล่น PC 2 ชั่วโมง บุคคลทั่วไปกี่บาท", ["2 ชั่วโมง", "2 session", "140 บาท"])
    print("PC SERVICE FEE SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
