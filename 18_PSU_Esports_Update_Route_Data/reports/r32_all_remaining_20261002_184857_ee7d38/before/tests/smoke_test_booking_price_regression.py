from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402


def check_case(
    question: str,
    *,
    category: str,
    mode_contains: str | tuple[str, ...],
    must_contain: list[str],
    must_not_contain: list[str],
) -> None:
    result = answer_question_pipeline_debug(
        question,
        experimental_rag_fallback=True,
        experimental_allow_llm=True,
    )
    answer_lower = result.answer.lower()
    missing = [text for text in must_contain if text.lower() not in answer_lower]
    forbidden = [text for text in must_not_contain if text.lower() in answer_lower]
    if result.route.category != category:
        raise AssertionError(f"{question}: category {result.route.category} != {category}\n{result.answer}")
    allowed_modes = (mode_contains,) if isinstance(mode_contains, str) else mode_contains
    if not any(mode in result.mode for mode in allowed_modes):
        raise AssertionError(f"{question}: mode {result.mode} does not contain {mode_contains}\n{result.answer}")
    if missing:
        raise AssertionError(f"{question}: missing {missing}\n{result.answer}")
    if forbidden:
        raise AssertionError(f"{question}: forbidden {forbidden}\n{result.answer}")
    print(f"OK {result.mode} {result.route.category}/{result.route.intent} | {question}")


def main() -> int:
    check_case(
        "ถ้าจอง PS5 ตั้งแต่ 9โมงถึง11โมงเสียกี่บาท",
        category="service_fee",
        mode_contains="deterministic_calculator_fast",
        must_contain=["2 ชั่วโมง", "2 session", "0 บาท/session x 2 = 0 บาท", "50 บาท/session x 2 = 100 บาท"],
        must_not_contain=["ไม่มีการคืนเงิน", "เช็คอิน"],
    )
    check_case(
        "วันจัทร์เล่น PS5 9โมงถึง12โมง เสียกี่บาท",
        category="service_fee",
        mode_contains="deterministic_calculator_fast",
        must_contain=["3 ชั่วโมง", "3 session", "09:00-10:00", "10:00-11:00", "11:00-12:00", "50 บาท/session x 3 = 150 บาท", "Maintenance"],
        must_not_contain=["ไม่มีการคืนเงิน"],
    )
    check_case(
        "PS5 เล่นได้กี่ชั่วโมงต่อวัน",
        category="reservation",
        mode_contains=("booking_session_limit_fast_path", "structured_reservation_fact"),
        must_contain=["สูงสุด 3 Sessions", "PlayStation 5", "สูงสุด 3 ชั่วโมง"],
        must_not_contain=["Weekly hardware inspection", "เวลาบริการที่มีในข้อมูล"],
    )
    check_case(
        "คนนึงเล่นได้กี่ชั่วโมงต่อวัน",
        category="reservation",
        mode_contains=("booking_session_limit_fast_path", "structured_reservation_fact"),
        must_contain=["สูงสุด 3 Sessions", "ต่อการจอง 1 ครั้ง"],
        must_not_contain=["Weekly hardware inspection", "เวลาบริการที่มีในข้อมูล"],
    )
    print("BOOKING PRICE REGRESSION SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
