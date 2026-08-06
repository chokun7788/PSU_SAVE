from __future__ import annotations

import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402


def check(
    question: str,
    *,
    category: str,
    mode_contains: str,
    must_contain: list[str],
    must_not_contain: list[str] | None = None,
) -> None:
    result = answer_question_pipeline_debug(
        question,
        experimental_rag_fallback=False,
        experimental_allow_llm=False,
    )
    answer_lower = result.answer.lower()
    missing = [item for item in must_contain if item.lower() not in answer_lower]
    forbidden = [item for item in (must_not_contain or []) if item.lower() in answer_lower]
    if result.route.category != category:
        raise AssertionError(f"{question}: category {result.route.category} != {category}\n{result.answer}")
    if mode_contains not in result.mode:
        raise AssertionError(f"{question}: mode {result.mode} does not contain {mode_contains}\n{result.answer}")
    if missing:
        raise AssertionError(f"{question}: missing {missing}\n{result.answer}")
    if forbidden:
        raise AssertionError(f"{question}: forbidden {forbidden}\n{result.answer}")
    if not result.validation.ok:
        raise AssertionError(f"{question}: validation errors {result.validation.errors}\n{result.answer}")
    print(f"OK {result.mode} {result.route.category}/{result.route.intent} {result.elapsed:.4f}s | {question}")


def main() -> int:
    check(
        "PC #01 มี Call of Duty: Warzone ไหม",
        category="games",
        mode_contains="structured_service_game_availability_no_match",
        must_contain=["PC #01-#02 ไม่มี Call of Duty: Warzone", "Call of Duty: Warzone เล่นได้ที่ PC #03-#10"],
        must_not_contain=["วิธีเล่นโดยสรุป", "เล่นได้ที่: PC Zone"],
    )
    check(
        "PC #03 มี TEKKEN 8 ไหม",
        category="games",
        mode_contains="structured_service_game_availability_no_match",
        must_contain=["PC #03-#10 ไม่มี TEKKEN 8", "TEKKEN 8 เล่นได้ที่ PC #01-#02"],
        must_not_contain=["วิธีเล่นโดยสรุป", "เล่นได้ที่: PC Zone และ PlayStation 5 Zone"],
    )
    check(
        "PC #01-#02 เล่นได้กี่คน",
        category="reservation",
        mode_contains="structured_service_capacity",
        must_contain=["PC #01-#02", "1 คน", "60 นาที"],
        must_not_contain=["Gaming PC รุ่น"],
    )
    check(
        "PlayStation 5 #01-#02 เล่นได้กี่คน",
        category="reservation",
        mode_contains="structured_service_capacity",
        must_contain=["PlayStation 5 #01-#02", "1-2 คน", "60 นาที"],
        must_not_contain=["09:00-12:00", "Maintenance"],
    )
    check(
        "VR Station 30 นาที เล่นได้กี่คน",
        category="reservation",
        mode_contains="structured_service_capacity",
        must_contain=["VR Station 30 นาที", "1-5 คน", "30 นาที"],
        must_not_contain=["09:00-12:00", "Maintenance"],
    )
    check(
        "PC Zone รายการเกมมีอะไรบ้าง",
        category="games",
        mode_contains="structured_service_game_availability",
        must_contain=["PC #01-#02", "PC #03-#10", "TEKKEN 8", "Call of Duty: Warzone"],
        must_not_contain=["ยังไม่แน่ใจ", "ถามให้เจาะจง"],
    )
    check(
        "PC เครื่อง 1 รายการเกมมีอะไรบ้าง",
        category="games",
        mode_contains="structured_service_game_availability",
        must_contain=["PC #01-#02", "TEKKEN 8", "VALORANT"],
        must_not_contain=["ยังไม่แน่ใจ", "ถามให้เจาะจง"],
    )
    check(
        "ทำจอยพังโดนปรับเท่าไหร่",
        category="penalty",
        mode_contains="penalty_fast_path",
        must_contain=["100-500", "500-2,000", "ชดเชยเต็มจำนวน"],
        must_not_contain=["ยังไม่แน่ใจว่าหมายถึงเกมไหน", "ราคา PS5"],
    )
    check(
        "กติกาในศูนย์มีอะไรบ้าง",
        category="rules",
        mode_contains="studio_rules_overview_fast_path",
        must_contain=["ฝากสัมภาระ", "อาหารและเครื่องดื่ม", "งดส่งเสียงดัง", "อุปกรณ์เสียหาย"],
        must_not_contain=["แข่งขัน", "BO3", "ผู้เล่น 5 คน"],
    )
    check(
        "ในศูนย์ห้ามอะไรบ้าง",
        category="rules",
        mode_contains="studio_rules_overview_fast_path",
        must_contain=["ห้าม", "อุปกรณ์", "แอลกอฮอล์", "การพนัน"],
        must_not_contain=["แข่งขัน", "BO3", "ผู้เล่น 5 คน"],
    )
    check(
        "ถ้าจะเล่น Call of Duty ต้องจองอะไร",
        category="reservation",
        mode_contains="structured_booking_game_family_clarification",
        must_contain=["Call of Duty: Warzone", "PC #03-#10", "Call of Duty: Modern Warfare III", "PlayStation 5 #01-#02"],
        must_not_contain=["เลือกบริการหรือโซนที่ต้องการใช้"],
    )
    check(
        "Call of Duty จองอะไร",
        category="reservation",
        mode_contains="structured_booking_game_family_clarification",
        must_contain=["Call of Duty: Warzone", "PC #03-#10", "Call of Duty: Modern Warfare III", "PlayStation 5 #01-#02"],
        must_not_contain=["ยกเลิกการจอง", "สลิปการโอนเงินเดิม"],
    )
    print("AVAILABILITY POLICY REGRESSION SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
