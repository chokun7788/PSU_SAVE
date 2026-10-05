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


def source_ids(result) -> set[str]:
    ids: set[str] = set()
    for hit in result.hits:
        ids.add(str(hit.get("id") or ""))
        metadata = hit.get("metadata", {}) if isinstance(hit, dict) else {}
        for source_id in metadata.get("source_ids") or []:
            ids.add(str(source_id))
    return ids


def main() -> int:
    result = answer_question_pipeline_debug(
        "ราคาเท่าไหร่",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    assert result.mode == "pipeline:ambiguity_clarification", result.mode
    assert_contains(result.answer, ["ขอรู้บริการหรือโซนก่อน", "PS5 ราคาเท่าไหร่", "Tekken 8 ราคาเท่าไหร่"], "bare price clarification")
    assert_not_contains(result.answer, ["Free หรือ 0 บาท", "ราคา PC:"], "bare price must not borrow unrelated price facts")
    print("OK bare price requires target")

    result = answer_question_pipeline_debug(
        "แล้วราคาเท่าไหร่",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    assert result.mode == "pipeline:ambiguity_clarification", result.mode
    assert_contains(result.answer, ["ขอรู้บริการหรือโซนก่อน"], "short price follow-up clarification")
    print("OK short price follow-up requires resolved context")

    result = answer_question_pipeline_debug(
        "มีอะไรบ้าง",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    assert result.mode == "pipeline:ambiguity_clarification", result.mode
    assert_contains(result.answer, ["ยังกว้างเกินไป", "มีเกมอะไรบ้าง", "มีอุปกรณ์อะไรบ้าง"], "broad query clarification")
    assert_not_contains(result.answer, ["Gaming PC รุ่น"], "broad query must not default to equipment catalog")
    print("OK broad query requires domain")

    result = answer_question_pipeline_debug(
        "PC มีอะไรบ้าง",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    assert result.mode == "pipeline:ambiguity_clarification", result.mode
    assert_contains(
        result.answer,
        [
            "หมายถึงเรื่องไหนของ PC Zone",
            "เกม: มี 6 เกม",
            "อุปกรณ์: มี 6 รายการ",
            "PSU 0 บาท",
            "General Student 25 บาท",
            "General Adult 70 บาท",
            "PC มีเกมอะไรบ้าง",
            "PC มีอุปกรณ์อะไรบ้าง",
            "PC ราคาเท่าไหร่",
            "PC จองยังไง",
        ],
        "broad service target hybrid clarification",
    )
    ids = source_ids(result)
    for expected_source_id in {"our_games", "home_equipment", "service_fee_image_2026", "pc_service_fee_local_update_20260727", "reservation"}:
        if expected_source_id not in ids:
            raise AssertionError(f"PC hybrid clarification missing source {expected_source_id}: {ids}")
    assert_not_contains(result.answer, ["อุปกรณ์ใน PC Zone:", "PC Zone มีเกมที่ยืนยันได้ดังนี้"], "broad service target must not become a full catalog answer")
    print("OK broad service target uses hybrid clarification preview")

    result = answer_question_pipeline_debug(
        "ปุ่มอะไร",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    assert result.mode in {"pipeline:ambiguity_clarification", "pipeline:game_control_missing_game_context"}, result.mode
    assert_contains(result.answer, ["ขอชื่อเกมก่อน", "TEKKEN 8"], "control query missing game clarification")
    print("OK control query requires game target")

    result = answer_question_pipeline_debug(
        "เล่นยังไง",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    assert result.mode in {"pipeline:ambiguity_clarification", "pipeline:game_control_missing_game_context"}, result.mode
    assert_contains(result.answer, ["วิธีเข้าใช้บริการ/จอง", "วิธีเล่นเกมไหน"], "bare play how-to clarification")
    print("OK bare play how-to asks domain/game")

    result = answer_question_pipeline_debug(
        "PS5 ราคาเท่าไหร่",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    assert result.mode == "pipeline:deterministic_calculator_fast", result.mode
    assert_contains(result.answer, ["PlayStation 5", "150 บาท"], "specific service price remains deterministic")
    print("OK specific service price still answers")

    result = answer_question_pipeline_debug(
        "Tekken 8 ราคาเท่าไหร่",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    assert result.mode == "pipeline:structured_service_fee_by_game", result.mode
    assert_contains(result.answer, ["TEKKEN 8", "ไม่มีราคาแยกตามชื่อเกม", "PlayStation 5 Zone"], "known game price still maps to zone")
    print("OK known game price still answers")

    result = answer_question_pipeline_debug(
        "จองยังไง",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    assert result.mode == "pipeline:structured_reservation_fact", result.mode
    assert_contains(result.answer, ["ขั้นตอนจอง", "แนบสลิป"], "booking how-to should not be blocked")
    print("OK booking how-to not blocked")

    result = answer_question_pipeline_debug(
        "แล้วจะเล่นต้องทำไง",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    assert result.mode == "pipeline:structured_booking_selection", result.mode
    assert_contains(result.answer, ["ต้องจองผ่านระบบก่อน", "เลือกบริการหรือโซน"], "booking access wording should still answer")
    print("OK access-to-play question remains booking")

    result = answer_question_pipeline_debug(
        "PC มีอุปกรณ์อะไรบ้าง",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    assert result.mode == "pipeline:structured_equipment_catalog", result.mode
    assert_contains(result.answer, ["อุปกรณ์ใน PC Zone", "Gaming PC รุ่น"], "explicit PC equipment should still answer")
    print("OK explicit PC equipment still answers")

    result = answer_question_pipeline_debug(
        "PC มีเกมอะไรบ้าง",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    assert result.mode in {
        "pipeline:structured_games_catalog",
        "pipeline:structured_service_game_availability",
    }, result.mode
    assert_contains(result.answer, ["PC Zone", "TEKKEN 8", "VALORANT"], "explicit PC games should still answer")
    print("OK explicit PC games still answers")

    result = answer_question_pipeline_debug(
        "เกมใน PC มีอะไรบ้าง",
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    assert result.mode in {
        "pipeline:structured_games_catalog",
        "pipeline:structured_service_game_availability",
    }, result.mode
    assert_contains(result.answer, ["PC Zone", "TEKKEN 8", "VALORANT"], "explicit PC games phrased with prefix should still answer")
    print("OK explicit PC games prefix phrasing still answers")

    print("AMBIGUITY GATE SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
