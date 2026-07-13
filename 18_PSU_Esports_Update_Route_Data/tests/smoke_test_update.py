from __future__ import annotations

import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.calculator.service_fee import answer_service_fee
from app.core.router import route_question
from app.rules.matcher import RuleMatcher


def assert_contains(text: str, expected: str, label: str) -> None:
    if expected not in text:
        raise AssertionError(f"{label}: expected {expected!r} in {text!r}")


def main() -> int:
    cases = [
        ("ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่", "190"),
        ("นักเรียน มอ. เล่น ps5 เท่าไหร่", "0"),
        ("pc ชั่วโมงละเท่าไหร่", "ราคา PC"),
        ("นักศึกษา สจล อยากเล่น PC เสียเท่าไหร่", "General Student"),
        ("เด็กจุฬา เล่น PC กี่บาท", "มหาลัยอื่น"),
        ("เด็กลาดกระบังเล่น VR ครึ่งชั่วโมงราคาเท่าไหร่", "190"),
        ("เด็ก สจล เล่น VR พี่บาท", "375"),
        ("นักศึกษาจุฬาเล่นเพลย์ห้าเท่าไหร่", "50"),
        ("นักเรียนเล่น VR เท่าไหร่", "375"),
    ]
    for question, expected in cases:
        result = answer_service_fee(question)
        assert result["matched"], question
        assert_contains(result["answer"], expected, question)
        print(f"OK calculator: {question} -> contains {expected}")

    matcher = RuleMatcher.default()
    decision = route_question("ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่", matcher=matcher)
    assert decision.route == "deterministic_calculator"
    print(f"OK route: service fee -> {decision.route}")

    decision = route_question("ช่วยสรุปขั้นตอนการจองให้หน่อย", matcher=matcher)
    assert decision.route in {"rule_fast_path", "rag_llm", "rag_direct_curated"}
    print(f"OK route: booking summary -> {decision.route}")

    print("SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
