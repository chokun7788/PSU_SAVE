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


def main() -> int:
    result = answer_question_pipeline_debug(
        "Tekken 8 เล่นที่ไหนและมีปุ่มอะไร",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    assert result.mode == "pipeline:multi_question_splitter", result.mode
    assert_contains(result.answer, ["Tekken 8 เล่นที่ไหน", "PC Zone", "PlayStation 5 Zone", "Tekken 8 มีปุ่มอะไร", "Square"], "same-subject location and controls")
    print("OK same-subject game location + controls")

    result = answer_question_pipeline_debug(
        "VR เปิดกี่โมง ราคาเท่าไหร่ และมีเกมอะไร",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    assert result.mode == "pipeline:multi_question_splitter", result.mode
    assert_contains(result.answer, ["VR เปิดกี่โมง", "09:00-12:00", "VR ราคาเท่าไหร่", "525 บาท", "VR มีเกมอะไร", "Beat Saber"], "same-subject schedule price games")
    assert_not_contains(result.answer, ["เกมที่ยืนยันได้ทั้งหมด 44 เกม"], "VR game follow-up should keep VR context")
    print("OK same-subject VR schedule + price + games")

    result = answer_question_pipeline_debug(
        "Tekken 8 ราคาเท่าไหร่",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    assert result.mode == "pipeline:structured_service_fee_by_game", result.mode
    assert_contains(result.answer, ["ไม่มีราคาแยกตามชื่อเกม", "PC Zone", "70 บาท", "PlayStation 5 Zone", "150 บาท"], "game price maps to service zones")
    assert_not_contains(result.answer, ["PlayStation 5 Zone มีเกมที่ยืนยันได้ดังนี้"], "game price must not become game list")
    print("OK game price maps to zone service fees")

    result = answer_question_pipeline_debug(
        "Mario มีปุ่มอะไรและจองยังไง",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    assert result.mode == "pipeline:multi_question_splitter", result.mode
    assert_contains(result.answer, ["Mario มีหลายเกม", "จะเล่น Mario จองยังไง", "Nintendo Switch Zone", "Mario Kart 8 Deluxe"], "broad mario controls + booking")
    assert_not_contains(result.answer, ["ถ้าจะเล่น New Super Mario Bros. U Deluxe"], "broad mario booking must not pick arbitrary title")
    print("OK broad Mario booking does not pick one arbitrary game")

    result = answer_question_pipeline_debug(
        "Tekken 8 จองยังไง",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    assert result.mode == "pipeline:structured_booking_game_service_selection", result.mode
    assert_contains(result.answer, ["TEKKEN 8", "PC #01-#02", "PlayStation 5 #01-#02", "เลือกวัน"], "short game booking maps to current services")
    print("OK short game booking maps to current services")

    result = answer_question_pipeline_debug(
        "จองยังไง แล้ว PS5 มีเกมอะไรบ้าง",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    assert result.mode == "pipeline:multi_question_splitter", result.mode
    assert_contains(result.answer, ["จองยังไง", "ขั้นตอนจอง", "PS5 มีเกมอะไรบ้าง", "TEKKEN 8"], "different-domain compound")
    print("OK different-domain compound remains split")

    print("COMPOUND QUESTION PLANNER SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
