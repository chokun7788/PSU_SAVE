from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402
from app.session.context_resolver import resolve_question_with_context  # noqa: E402


def answer_with_context(question: str, recent_history: list[dict[str, str]]):
    resolved = resolve_question_with_context(question, recent_history)
    result = answer_question_pipeline_debug(resolved.resolved_question)
    return resolved, result


def history_after(question: str) -> list[dict]:
    result = answer_question_pipeline_debug(
        question,
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    return [
        {"role": "user", "text": question},
        {
            "role": "assistant",
            "text": result.answer,
            "universal_intent": result.universal_intent.__dict__ if result.universal_intent else None,
            "route_category": result.route.category,
            "route_intent": result.route.intent,
            "resolved_text": question,
        },
    ]


def assert_contains(text: str, expected: list[str], label: str) -> None:
    missing = [item for item in expected if item.lower() not in text.lower()]
    if missing:
        raise AssertionError(f"{label}: missing {missing}\n{text}")


def assert_not_contains(text: str, forbidden: list[str], label: str) -> None:
    found = [item for item in forbidden if item.lower() in text.lower()]
    if found:
        raise AssertionError(f"{label}: forbidden {found}\n{text}")


def main() -> int:
    pc_ambiguity_history = history_after("PC มีอะไรบ้าง")

    resolved, result = answer_with_context("เกม", pc_ambiguity_history)
    assert resolved.used_context, resolved
    assert resolved.context_domain == "games", resolved
    assert_contains(resolved.resolved_question, ["PC", "มีเกมอะไรบ้าง"], "resolved PC games choice")
    assert result.mode == "pipeline:structured_service_game_availability", result.mode
    assert_contains(result.answer, ["PC Zone", "TEKKEN 8", "VALORANT"], "answer PC games choice")
    print("OK clarification choice: PC games")

    resolved, result = answer_with_context("อุปกรณ์", pc_ambiguity_history)
    assert resolved.used_context, resolved
    assert resolved.context_domain == "equipment", resolved
    assert_contains(resolved.resolved_question, ["PC", "มีอุปกรณ์อะไรบ้าง"], "resolved PC equipment choice")
    assert result.mode == "pipeline:structured_equipment_catalog", result.mode
    assert_contains(result.answer, ["อุปกรณ์ใน PC Zone", "Gaming PC รุ่น"], "answer PC equipment choice")
    print("OK clarification choice: PC equipment")

    resolved, result = answer_with_context("ราคา", pc_ambiguity_history)
    assert resolved.used_context, resolved
    assert resolved.context_domain == "service_fee", resolved
    assert_contains(resolved.resolved_question, ["PC", "ราคาเท่าไหร่"], "resolved PC price choice")
    assert result.mode == "pipeline:deterministic_calculator_fast", result.mode
    assert_contains(result.answer, ["ราคา PC", "25 บาท", "70 บาท"], "answer PC price choice")
    print("OK clarification choice: PC price")

    resolved, result = answer_with_context("จอง", pc_ambiguity_history)
    assert resolved.used_context, resolved
    assert resolved.context_domain == "reservation", resolved
    assert_contains(resolved.resolved_question, ["PC", "จองยังไง"], "resolved PC booking choice")
    assert result.route.category == "reservation", result.route
    assert_contains(result.answer, ["ขั้นตอนจอง", "เลือกบริการ", "แนบสลิป"], "answer PC booking choice")
    print("OK clarification choice: PC booking")

    resolved, result = answer_with_context("ปุ่ม", pc_ambiguity_history)
    if resolved.used_context:
        raise AssertionError(f"button choice should not inherit preview example game: {resolved}")
    assert result.mode in {"pipeline:ambiguity_clarification", "pipeline:game_control_missing_game_context"}, result.mode
    assert_contains(result.answer, ["ยังไม่แน่ใจว่าหมายถึงเกมไหน"], "button after broad PC clarification should ask game")
    assert_not_contains(result.answer, ["Counter-Strike", "มีข้อมูลปุ่มควบคุมดังนี้"], "button should not use preview example game")
    print("OK clarification choice: no fake game context for buttons")

    resolved, result = answer_with_context("ราคา Nintendo", pc_ambiguity_history)
    if resolved.used_context:
        raise AssertionError(f"explicit Nintendo target should not inherit PC context: {resolved}")
    assert_contains(resolved.resolved_question, ["ราคา Nintendo"], "explicit service target should stay original")
    assert result.route.category == "service_fee", result.route
    assert_contains(result.answer, ["Nintendo Switch", "140 บาท", "280 บาท"], "answer explicit Nintendo price")
    assert_not_contains(result.answer, ["ราคา PC", "General Adult / บุคคลทั่วไป: 70 บาท"], "Nintendo price must not borrow PC")
    print("OK clarification safety: explicit service target wins over pending context")

    resolved, result = answer_with_context("เครื่อง", pc_ambiguity_history)
    if resolved.used_context:
        raise AssertionError(f"ambiguous word should not resolve as PC equipment choice: {resolved}")
    assert_not_contains(resolved.resolved_question, ["PC มีอุปกรณ์"], "ambiguous equipment-like word should stay original")
    assert_not_contains(result.answer, ["อุปกรณ์ใน PC Zone"], "ambiguous word must not become PC equipment catalog")
    print("OK clarification safety: ambiguous word is not a choice")

    expired_pc_history = [
        *pc_ambiguity_history,
        {"role": "user", "text": "ขอบคุณ"},
        {"role": "assistant", "text": "ครับ"},
    ]
    resolved, result = answer_with_context("เกม", expired_pc_history)
    if resolved.used_context:
        raise AssertionError(f"expired clarification should not resolve short choice: {resolved}")
    assert_not_contains(resolved.resolved_question, ["PC มีเกมอะไรบ้าง"], "expired clarification should not keep PC")
    assert_contains(result.answer, ["เกมที่ยืนยันได้ทั้งหมด", "PC Zone", "Nintendo Switch Zone"], "expired choice becomes normal game query")
    print("OK clarification safety: pending context expires after latest assistant turn")

    mario_party_history = [
        {"role": "user", "text": "เกมมาริโอ้ปาตี้"},
        {
            "role": "assistant",
            "text": "Mario Party Superstars คือเกมปาร์ตี้ที่เล่นบนกระดานและแข่งมินิเกมกับเพื่อน",
        },
    ]

    resolved, result = answer_with_context("เล่นยังไง", mario_party_history)
    assert resolved.used_context, resolved
    assert resolved.context_game == "Mario Party Superstars", resolved
    assert_contains(resolved.resolved_question, ["Mario Party Superstars", "เล่นยังไง"], "resolved play")
    assert_contains(result.answer, ["Mario Party Superstars", "ข้อมูลปุ่มควบคุม", "มินิเกม"], "answer play")
    print("OK context follow-up: Mario Party เล่นยังไง")

    naruto_history = [
        {"role": "user", "text": "เกม Naruto"},
        {"role": "assistant", "text": "NARUTO X BORUTO Ultimate Ninja Storm Connections เล่นได้ที่ PlayStation 5 Zone"},
    ]
    resolved, result = answer_with_context("แล้วจะเล่นต้องทำไง", naruto_history)
    assert resolved.used_context, resolved
    assert resolved.context_game and "NARUTO" in resolved.context_game, resolved
    assert result.mode in {"pipeline:structured_booking_selection", "pipeline:structured_booking_game_service_selection"}, result.mode
    assert_contains(result.answer, ["NARUTO X BORUTO", "PlayStation 5 #01-#02", "เลือกวัน", "รอบเวลา"], "naruto access follow-up")
    assert_not_contains(result.answer, ["วิธีเล่นโดยสรุป", "คอมโบ", "สกิลนินจา"], "naruto access should not become gameplay")
    print("OK context follow-up: Naruto play access becomes booking")

    resolved, result = answer_with_context("มีปุ่มอะไรบ้าง", mario_party_history)
    assert resolved.used_context, resolved
    assert_contains(resolved.resolved_question, ["Mario Party Superstars", "มีปุ่มอะไรบ้าง"], "resolved controls")
    assert_contains(
        result.answer,
        ["Mario Party Superstars", "มีข้อมูลปุ่มควบคุม", "Nintendo Switch"],
        "answer controls",
    )
    assert_not_contains(result.answer, ["Super Mario Odyssey", "Mario Kart 8 Deluxe"], "answer no wrong game")
    print("OK context follow-up: Mario Party controls")

    gran_turismo_history = history_after("Gran Turismo เล่นยังไง")
    resolved, result = answer_with_context("ปุ่ม", gran_turismo_history)
    assert resolved.used_context, resolved
    assert resolved.context_game == "Gran Turismo 7", resolved
    assert_contains(resolved.resolved_question, ["Gran Turismo 7", "ปุ่ม"], "resolved bare controls")
    assert_contains(result.answer, ["Gran Turismo 7", "มีข้อมูลปุ่ม"], "answer Gran Turismo controls")
    assert_not_contains(result.answer, ["ขอชื่อเกมก่อน"], "bare controls should inherit game context")
    print("OK context follow-up: Gran Turismo bare controls")

    resolved = resolve_question_with_context("จองเครื่องยังไง", mario_party_history)
    if resolved.used_context:
        raise AssertionError(f"booking topic shift should not inherit context: {resolved}")
    if "Mario Party" in resolved.resolved_question:
        raise AssertionError(f"booking topic shift leaked game context: {resolved}")
    print("OK topic shift: booking does not inherit game")

    live_history = [
        {"role": "user", "text": "มาริโอคาร์ทไลฟ์คือเกมอะไร"},
        {"role": "assistant", "text": "Mario Kart Live: Home Circuit เล่นได้ที่ Nintendo Switch Zone"},
    ]
    resolved, result = answer_with_context("ปุ่มเร่งเครื่องกดอะไร", live_history)
    assert resolved.used_context, resolved
    assert_contains(result.answer, ["Mario Kart Live: Home Circuit", "รายการเกมปัจจุบัน", "ไม่ดึงปุ่มของเกมอื่น"], "answer live no-current")
    assert_not_contains(result.answer, ["Left Stick"], "answer live not mk8 controls")
    print("OK context follow-up: Mario Kart Live controls")

    member_history = [
        {"role": "user", "text": "สมาชิกใน PSU Esport มีกี่หมวด"},
        {
            "role": "assistant",
            "text": "สมาชิกในหน้า Members แบ่งเป็น 3 หมวดครับ",
            "universal_intent": {"domain": "members", "operation": "group_count"},
            "route_category": "overview",
            "route_intent": "group_count",
        },
    ]
    resolved, result = answer_with_context("แล้วแต่ละหมวดมีใครบ้าง", member_history)
    assert resolved.used_context, resolved
    assert resolved.context_domain == "members", resolved
    assert_contains(resolved.resolved_question, ["สมาชิก", "แต่ละหมวด", "มีใครบ้าง"], "resolved member groups")
    assert_contains(result.answer, ["Members", "cooperative education", "PSU Phuket Esports Club"], "answer member groups")
    print("OK context follow-up: member group list")

    resolved, result = answer_with_context("สมาชิก PSU Esport มีกี่หมวด", member_history)
    assert resolved.used_context, resolved
    assert resolved.context_domain == "members", resolved
    assert_contains(resolved.resolved_question, ["สมาชิก", "กี่หมวด"], "resolved member group count")
    assert "structured_members_group_count" in result.mode, result.mode
    assert_contains(result.answer, ["แบ่งเป็น 3 หมวด", "Members: 7 คน", "รวมทั้งหมด 25 คน"], "answer member group count")
    assert_not_contains(result.answer, ["ผศ.ดร.นิวัติ", "นายชนะชัย"], "answer member count should not list people")
    print("OK context explicit member group count does not become member list")

    ps5_history = [
        {"role": "user", "text": "PS5 มีเกมกี่เกม"},
        {
            "role": "assistant",
            "text": "PlayStation 5 Zone มีเกมที่ยืนยันได้ 18 เกมครับ",
            "universal_intent": {"domain": "games", "operation": "count"},
            "route_category": "games",
            "route_intent": "count",
        },
    ]
    resolved, result = answer_with_context("แล้วมีเกมอะไรบ้าง", ps5_history)
    assert resolved.used_context, resolved
    assert resolved.context_domain == "games", resolved
    assert_contains(resolved.resolved_question, ["PlayStation 5", "มีเกมอะไรบ้าง"], "resolved PS5 games")
    assert_contains(result.answer, ["PlayStation 5 Zone"], "answer PS5 games")
    print("OK context follow-up: PS5 game list")

    resolved, result = answer_with_context("เกมทั้งหมดมีกี่เกม", ps5_history)
    if resolved.used_context:
        raise AssertionError(f"explicit all-games question should not inherit PS5 context: {resolved}")
    assert_contains(result.answer, ["เกมที่ยืนยันได้ทั้งหมด", "PC Zone", "Nintendo Switch Zone"], "answer all games count")
    assert_not_contains(result.answer, ["PlayStation 5 Zone มีเกมที่ยืนยันได้"], "all games should not become PS5-only")
    print("OK context topic reset: explicit all games ignores PS5 context")

    resolved, result = answer_with_context("เกมตอนนี้มีเกมอะไรบ้าง", ps5_history)
    if resolved.used_context:
        raise AssertionError(f"current all-games question should not inherit PS5 context: {resolved}")
    assert_contains(result.answer, ["เกมที่ยืนยันได้ทั้งหมด", "PC Zone", "Nintendo Switch Zone"], "answer current all games")
    assert_not_contains(result.answer, ["PlayStation 5 Zone มีเกมที่ยืนยันได้"], "current all games should not become PS5-only")
    print("OK context topic reset: current game catalog ignores PS5 context")

    reservation_history = [
        {"role": "user", "text": "แล้วจองไง"},
        {
            "role": "assistant",
            "text": "ขั้นตอนจองโดยสรุป: เลือกบริการ เลือกวันและรอบเวลา กรอกข้อมูล ชำระเงิน แนบสลิปและยืนยันการจอง",
            "universal_intent": {"domain": "reservation", "operation": "how_to"},
            "route_category": "reservation",
            "route_intent": "how_to",
        },
    ]
    resolved, result = answer_with_context("สรุปคือทำยังไง", reservation_history)
    assert resolved.used_context, resolved
    assert resolved.context_domain == "reservation", resolved
    assert_contains(resolved.resolved_question, ["สรุปขั้นตอนจอง"], "resolved reservation summary")
    assert result.route.category == "reservation", result.route
    assert "general" not in result.mode, result.mode
    assert_contains(result.answer, ["ขั้นตอนจอง", "เลือกบริการ", "แนบสลิป"], "answer reservation summary follow-up")
    print("OK context follow-up: reservation summary how-to")

    print("SESSION CONTEXT SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
