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
    result = answer_question_pipeline_debug("สมาชิกใน PSU Esport มีกี่หมวด")
    assert result.mode == "pipeline:structured_members_group_count", result.mode
    assert_contains(result.answer, ["3 หมวด", "Members", "cooperative education", "PSU Phuket Esports Club"], "member groups")
    print("OK structured members group count")

    result = answer_question_pipeline_debug("Nintendo มีเกมอะไรบ้าง")
    assert result.mode == "pipeline:structured_service_game_availability", result.mode
    assert_contains(result.answer, ["Nintendo Switch Zone", "Pokémon Champions", "Mario Kart 8 Deluxe", "Mario Party Superstars"], "nintendo games")
    assert_not_contains(result.answer, ["Mario Party™ Superstars", "Luigi's Mansion™ 3"], "deduped game titles")
    print("OK structured games catalog")

    result = answer_question_pipeline_debug("อุปกรณ์ไหนเกมเยอะสุด")
    assert result.mode == "pipeline:structured_game_zone_ranking", result.mode
    assert_contains(result.answer, ["PlayStation 5 Zone", "17 เกม", "Nintendo Switch Zone: 17 เกม"], "game count ranking")
    assert_not_contains(result.answer, ["อุปกรณ์บนหน้า Home"], "ranking should not become equipment catalog")
    print("OK game count ranking does not become equipment catalog")

    result = answer_question_pipeline_debug("Tekken 8")
    assert result.mode == "pipeline:structured_game_detail", result.mode
    assert_contains(result.answer, ["TEKKEN 8", "PlayStation 5 Zone"], "bare tekken detail")
    assert_not_contains(result.answer, ["44", "Local LLM"], "bare tekken should not list all games or use fallback")
    print("OK bare game title stays game detail")

    result = answer_question_pipeline_debug("Over cook")
    assert result.mode == "pipeline:structured_games_family", result.mode
    assert_contains(result.answer, ["Overcooked", "Overcooked! 2"], "spaced overcook family")
    assert_not_contains(result.answer, ["44", "Local LLM"], "spaced overcook should not list all games or use fallback")
    print("OK spaced Over cook stays Overcooked family")

    result = answer_question_pipeline_debug("Mario มีปุ่มอะไรบ้าง")
    assert result.mode == "pipeline:ambiguity_clarification", result.mode
    assert_contains(result.answer, ["ยังไม่ชัด", "Mario Kart 8 Deluxe", "Mario Party Superstars", "Super Mario Odyssey"], "broad mario controls summary")
    assert_not_contains(result.answer, ["New Super Mario Bros. U Deluxe มีอยู่ในรายการเกมที่ยืนยันได้"], "broad mario controls should not pick one arbitrary game")
    print("OK broad Mario controls ask for specific game")

    result = answer_question_pipeline_debug("ถ้าเล่น Tekken 8 กับ Mario มีปุ่มอะไรบ้าง")
    assert result.mode == "pipeline:multi_question_splitter", result.mode
    assert_contains(result.answer, ["TEKKEN 8 มีข้อมูลปุ่ม", "ยังไม่ชัด", "Mario Kart 8 Deluxe", "Super Mario Odyssey"], "multi game controls")
    print("OK shared-tail multi-game controls split into answers")

    result = answer_question_pipeline_debug("PS5 กับ Nintendo มีเกมอะไรบ้าง")
    assert result.mode == "pipeline:multi_question_splitter", result.mode
    assert_contains(result.answer, ["PlayStation 5 Zone", "Nintendo Switch Zone", "TEKKEN 8", "Mario Kart 8 Deluxe"], "multi zone games")
    print("OK shared-tail multi-zone game list split into answers")

    result = answer_question_pipeline_debug("ถ้าจะเล่น Naruto ต้องทำไง")
    assert result.mode in {"pipeline:structured_booking_selection", "pipeline:structured_booking_game_service_selection"}, result.mode
    assert_contains(result.answer, ["NARUTO X BORUTO", "PlayStation 5 #01-#02", "เลือกวัน", "รอบเวลา"], "naruto play access should become booking")
    assert_not_contains(result.answer, ["วิธีเล่นโดยสรุป", "คอมโบ", "สกิลนินจา"], "naruto play access should not become gameplay")
    print("OK specific game play access becomes booking selection")

    result = answer_question_pipeline_debug("แล้วจะเล่นต้องทำไง")
    assert result.mode == "pipeline:structured_booking_selection", result.mode
    assert_contains(result.answer, ["ต้องจองผ่านระบบก่อน", "เลือกบริการหรือโซน", "แนบสลิป"], "generic play access should become booking")
    print("OK generic play access becomes booking selection")

    result = answer_question_pipeline_debug("Mario Kart Live ปุ่มเร่งเครื่องกดอะไร")
    assert result.mode == "pipeline:structured_game_controls_no_current_game", result.mode
    assert_contains(result.answer, ["Mario Kart Live: Home Circuit", "รายการเกมปัจจุบัน", "ไม่ดึงปุ่มของเกมอื่น"], "mario kart live no current")
    assert_not_contains(result.answer, ["Left Stick"], "specific control does not list wrong game/all controls")
    print("OK structured specific game control")

    result = answer_question_pipeline_debug("mario kart liveเล่นยังไง")
    assert result.mode == "pipeline:structured_game_controls_no_current_game", result.mode
    assert_contains(result.answer, ["Mario Kart Live: Home Circuit", "รายการเกมปัจจุบัน", "ไม่ดึงปุ่มของเกมอื่น"], "mario kart live gameplay should no-current")
    assert_not_contains(result.answer, ["Left Stick"], "specific gameplay control does not list wrong Mario game")
    print("OK named game gameplay asks controls")

    result = answer_question_pipeline_debug("call of เล่นยังไง")
    assert result.mode == "pipeline:ambiguity_clarification", result.mode
    assert_contains(result.answer, ["Call of Duty", "Call of Duty: Modern Warfare III", "Call of Duty: Warzone"], "short call of gameplay should clarify Call of Duty family")
    assert_not_contains(result.answer, ["NARUTO X BORUTO", "นารูโตะ"], "short call of gameplay must not drift to Naruto controls")
    print("OK short Call of gameplay does not drift to Naruto")

    result = answer_question_pipeline_debug("TEKKEN 8 ปุ่มเตะขวากดอะไร")
    assert result.mode == "pipeline:structured_game_controls", result.mode
    assert_contains(result.answer, ["Circle", "ลูกเตะขวา"], "tekken right kick")
    assert_not_contains(result.answer, ["L1: สเปเชียลสไตล์"], "specific control does not include unrelated fuzzy match")
    print("OK structured tekken specific control")

    result = answer_question_pipeline_debug("Overcooked 2 มีปุ่มอะไรบ้าง")
    assert result.mode == "pipeline:structured_game_controls_no_data", result.mode
    assert_contains(
        result.answer,
        ["Overcooked 2", "Nintendo Switch Zone", "ยังไม่พบข้อมูลปุ่มควบคุม"],
        "known game without version-matched controls should not borrow another title's controls",
    )
    assert_not_contains(result.answer, ["L (Left Stick)", "Cross", "หยิบ / วาง"], "controls must stay version-matched")
    print("OK known game does not borrow controls from another title")

    result = answer_question_pipeline_debug("VALORANT ปุ่มอะไร")
    assert result.mode == "pipeline:structured_game_controls", result.mode
    assert_contains(
        result.answer,
        ["VALORANT", "W / A / S / D", "Left Mouse Button", "Q / E / C / X"],
        "known pc game with controls should answer controls",
    )
    print("OK known PC game with controls answers controls")

    result = answer_question_pipeline_debug("PC Zone มีอุปกรณ์อะไรบ้าง")
    assert result.mode == "pipeline:structured_equipment_catalog", result.mode
    assert result.route.category == "equipment", result.route
    assert_contains(result.answer, ["PC Zone", "Gaming PC", "Gaming Monitor", "Gaming Keyboard"], "pc equipment catalog")
    print("OK structured equipment catalog")

    result = answer_question_pipeline_debug("Logitech G923 คืออะไร ใช้ยังไง")
    assert result.mode == "pipeline:structured_equipment_item", result.mode
    assert result.route.category == "equipment", result.route
    assert_contains(result.answer, ["Logitech G923", "Cockpit Zone", "Gran Turismo 7"], "logitech equipment item")
    print("OK structured equipment item")

    result = answer_question_pipeline_debug("วันจันทร์เปิดกี่โมง")
    assert result.mode == "pipeline:structured_schedule", result.mode
    assert_contains(result.answer, ["วันจันทร์", "13:00-16:00", "Maintenance"], "monday schedule")
    print("OK structured schedule")

    result = answer_question_pipeline_debug("วิธีจองทำยังไง")
    assert result.mode == "pipeline:structured_reservation_fact", result.mode
    assert_contains(result.answer, ["ขั้นตอนจอง", "เลือกบริการ", "แนบสลิป"], "booking steps")
    print("OK structured reservation fact")

    result = answer_question_pipeline_debug("แล้วจองไง")
    assert result.mode == "pipeline:structured_reservation_fact", result.mode
    assert_contains(result.answer, ["ขั้นตอนจอง", "เลือกบริการ", "แนบสลิป"], "short booking steps")
    assert_not_contains(result.answer, ["ยกเลิกผ่าน", "จองใหม่"], "short booking should not become cancellation policy")
    print("OK short booking how-to does not become cancellation policy")

    result = answer_question_pipeline_debug("VR 30 นาที บุคคลทั่วไปกี่บาท")
    assert result.mode == "pipeline:deterministic_calculator_fast", result.mode
    assert_contains(result.answer, ["VR", "30 นาที", "525 บาท"], "vr adult price")
    print("OK price calculator priority")

    result = answer_question_pipeline_debug("ถ้าจอง PS5 ตั้งแต่ 9โมงถึง11โมงเสียกี่บาท")
    assert result.mode == "pipeline:deterministic_calculator_fast", result.mode
    assert_contains(result.answer, ["2 ชั่วโมง", "2 session", "09:00-10:00", "10:00-11:00"], "time range price remains deterministic")
    print("OK time range price stays deterministic")

    print("STRUCTURED TOOLS SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
