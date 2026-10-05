from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.schemas import EntityBundle, PipelineRoute  # noqa: E402
from app.pipeline.validator import validate_answer  # noqa: E402
from app.core.source_registry import (  # noqa: E402
    PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID,
    SERVICE_FEE_IMAGE_2026_ID,
    make_source_hits,
)


def route(category: str, intent: str = "test") -> PipelineRoute:
    return PipelineRoute(category, intent, 0.95, "fact", "low", "validator smoke test")


def main() -> int:
    result = validate_answer(
        "จอง Nintendo Switch ต้องระบุจำนวนผู้เล่นไหม",
        "Nintendo Switch OLED: เครื่องเกม Nintendo Switch รุ่น OLED\nจำนวน: 1 Unit\nอยู่ที่: Nintendo Switch Zone",
        route("equipment", "count"),
        EntityBundle(),
    )
    assert not result.ok
    assert "booking_question_answered_as_equipment_or_game_catalog" in result.errors
    print("OK validator rejects booking answered as equipment")

    result = validate_answer(
        "ROV คือเกมอะไร",
        "ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 44 เกมครับ\n\nPlayStation 5 Zone (23 เกม)\n•    TEKKEN 8",
        route("games", "list"),
        EntityBundle(),
    )
    assert not result.ok
    assert "specific_game_detail_answered_as_game_catalog" in result.errors
    print("OK validator rejects specific game detail answered as catalog")

    result = validate_answer(
        "ROV รอบชิงเล่นกี่เกม",
        "ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 44 เกมครับ\n\nNintendo Switch Zone (18 เกม)\n•    Mario Kart 8 Deluxe",
        route("games", "list"),
        EntityBundle(),
    )
    assert not result.ok
    assert "competition_rule_answered_as_game_catalog" in result.errors
    print("OK validator rejects competition rule answered as catalog")

    result = validate_answer(
        "จอง Nintendo Switch ต้องเลือกอะไรบ้าง",
        "จอง Nintendo Switch ต้องเลือกบริการตามจำนวนผู้เล่นครับ\n•    ถ้าเล่น 1-2 คน ให้เลือก Nintendo Switch แบบ 1-2 Persons\n•    ถ้าเล่น 3-4 คน ให้เลือก Nintendo Switch แบบ 3-4 Persons",
        route("reservation", "booking_policy"),
        EntityBundle(),
    )
    assert result.ok, result.errors
    print("OK validator accepts correct booking answer")

    result = validate_answer(
        "TEKKEN 8 ปุ่มทั้งหมดมีอะไรบ้าง",
        "TEKKEN 8: TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว\nแนวเกม: เกมต่อสู้ 1v1\nวิธีเล่นโดยสรุป: เลือกตัวละครและใช้คอมโบเพื่อชนะคู่แข่ง\nเล่นได้ที่: PC Zone และ PlayStation 5 Zone",
        route("games", "game_detail_lookup"),
        EntityBundle(),
    )
    assert not result.ok
    assert "control_question_answered_as_game_detail" in result.errors
    print("OK validator rejects controls answered as game detail")

    result = validate_answer(
        "จองยังไง",
        "การยกเลิกการจองต้องทำล่วงหน้าอย่างน้อย 1 ชั่วโมงครับ หากต้องการแก้ไขข้อมูลหรือเวลาใช้งาน ต้องยกเลิกการจองเดิมก่อนแล้วจองใหม่",
        route("reservation", "booking_policy"),
        EntityBundle(),
    )
    assert not result.ok
    assert "booking_howto_question_answered_as_cancellation_policy" in result.errors
    print("OK validator rejects booking how-to answered as cancellation policy")

    result = validate_answer(
        "Tekken 8 ราคาเท่าไหร่",
        "ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 44 เกมครับ\n\nPlayStation 5 Zone (23 เกม)\n•    TEKKEN 8",
        route("games", "list"),
        EntityBundle(price_intent=True),
    )
    assert not result.ok
    assert "price_question_answered_as_game_catalog" in result.errors
    print("OK validator rejects price answered as game catalog")

    result = validate_answer(
        "ราคา PC ต่อชั่วโมงเท่าไหร่",
        "ราคา PC 1 ชั่วโมง (1 คน)\n•    PSU Student and Staff: 0 บาท\n•    PSU Alumni and General Student: 25 บาท\n•    General Adult: 70 บาท",
        route("service_fee", "service_fee_query"),
        EntityBundle(price_intent=True),
        hits=make_source_hits([SERVICE_FEE_IMAGE_2026_ID]),
    )
    assert not result.ok
    assert "pc_price_answer_missing_pc_local_update_source" in result.errors
    print("OK validator rejects PC price without local source")

    result = validate_answer(
        "ราคา PC ต่อชั่วโมงเท่าไหร่",
        "ราคา PC 1 ชั่วโมง (1 คน)\n•    PSU Student and Staff: 0 บาท\n•    PSU Alumni and General Student: 25 บาท\n•    General Adult: 70 บาท",
        route("service_fee", "service_fee_query"),
        EntityBundle(price_intent=True),
        hits=make_source_hits([SERVICE_FEE_IMAGE_2026_ID, PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID]),
    )
    assert result.ok, result.errors
    print("OK validator accepts PC price with local source")

    print("ANSWER VALIDATOR SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
