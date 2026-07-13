from __future__ import annotations

import os
import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402


def check(
    question: str,
    must_contain: list[str],
    *,
    must_not_contain: list[str] | None = None,
    route_category: str | None = None,
    mode_prefix: str | None = None,
) -> None:
    result = answer_question_pipeline_debug(question)
    answer_lower = result.answer.lower()
    missing = [item for item in must_contain if item.lower() not in answer_lower]
    if missing:
        raise AssertionError(f"{question}: missing {missing}\n{result.answer}")
    forbidden = [item for item in (must_not_contain or []) if item.lower() in answer_lower]
    if forbidden:
        raise AssertionError(f"{question}: forbidden {forbidden}\n{result.answer}")
    if route_category and result.route.category != route_category:
        raise AssertionError(f"{question}: expected category {route_category}, got {result.route.category}")
    if mode_prefix and not result.mode.startswith(mode_prefix):
        raise AssertionError(f"{question}: expected mode prefix {mode_prefix}, got {result.mode}")
    if not result.validation.ok:
        raise AssertionError(f"{question}: validation errors {result.validation.errors}\n{result.answer}")
    print(f"OK {result.mode} {result.route.category} {result.elapsed:.4f}s | {question}")


def main() -> int:
    os.environ["PSU_ESPORTS_TODAY"] = "2026-07-02"
    check(
        "วันจันทร์ morning เล่นได้ไหม afternoon เปิดไหม",
        ["Morning เล่นไม่ได้", "Afternoon เปิด", "13:00", "16:00"],
        must_not_contain=["24 ชั่วโมง", "24 hours"],
        route_category="schedule",
    )
    check(
        "วันอังคารเล่นได้กี่โมง",
        ["วันอังคาร", "09:00-12:00", "13:00-16:00"],
        must_not_contain=["ไม่พบข้อมูล"],
        route_category="schedule",
    )
    check(
        "วันนี้เปิดไหม",
        ["วันนี้", "02/07/2026", "วันพฤหัสบดี", "09:00-12:00", "13:00-16:00"],
        must_not_contain=["ไม่พบข้อมูล"],
        route_category="schedule",
    )
    check(
        "พรุ่งนี้เปิดไหม",
        ["พรุ่งนี้", "03/07/2026", "วันศุกร์", "09:00-12:00", "Maintenance"],
        must_not_contain=["ไม่พบข้อมูล"],
        route_category="schedule",
    )
    check(
        "28 กรกฎา เปิดไหม",
        ["28/07/2026", "วันหยุดราชการ", "ปิดให้บริการ"],
        must_not_contain=["เปิดให้เล่น 09:00-12:00", "ไม่พบข้อมูล"],
        route_category="schedule",
    )
    check(
        "30/7/2026 ศูนย์เปิดรึเปล่า",
        ["30/07/2026", "วันหยุดราชการ", "ปิดให้บริการ"],
        must_not_contain=["ไม่พบข้อมูล"],
        route_category="schedule",
    )
    check(
        "วันไหนหยุดบ้างในเดือนนี้",
        ["เดือนกรกฎาคม 2026", "28/07/2026", "29/07/2026", "30/07/2026", "มีวันปิดให้บริการ 3 วัน"],
        must_not_contain=["ไม่พบข้อมูล"],
        route_category="schedule",
    )
    check(
        "เดือนนี้ศูนย์ปิดวันไหนบ้าง",
        ["เดือนกรกฎาคม 2026", "28/07/2026", "29/07/2026", "30/07/2026"],
        must_not_contain=["ไม่พบข้อมูล"],
        route_category="schedule",
    )
    check(
        "วันพุธช่วงเช้าเล่นได้ไหม",
        ["วันพุธ", "09:00-12:00", "เปิดให้เล่น"],
        must_not_contain=["ไม่พบข้อมูล", "Maintenance*"],
        route_category="schedule",
    )
    check(
        "พฤหัสปิดกี่โมง",
        ["วันพฤหัสบดี", "16:00"],
        must_not_contain=["ไม่พบข้อมูล"],
        route_category="schedule",
    )
    check(
        "ต่างมหาลัยเล่น VR 30 นาที กับ VR 1 ชั่วโมงต่างกันเท่าไหร่",
        ["ต่างกัน", "185", "190", "375"],
        route_category="service_fee",
    )
    check(
        "เช็คอินล่วงหน้าได้กี่นาที",
        ["30 นาที"],
        route_category="reservation",
    )
    check(
        "มีให้เช่าจอไปบ้านไหม",
        ["ไม่พบข้อมูล"],
        route_category="no_answer",
    )
    check(
        "คอมมีวาโลไหม",
        ["VALORANT"],
        route_category="games",
    )
    check(
        "CS2 แข่งทีมละกี่คน",
        ["คำตอบ:", "ผู้เล่น 5 คน", "อ้างอิงจากกติกา"],
        must_not_contain=["ไม่พบข้อมูล"],
        route_category="competition_rules",
        mode_prefix="pipeline:competition_fact_card",
    )
    check(
        "VALORANT Tactical Timeout ขอได้กี่ครั้ง",
        ["คำตอบ:", "2 ครั้ง", "60 วินาที", "อ้างอิงจากกติกา"],
        must_not_contain=["ไม่พบข้อมูล"],
        route_category="competition_rules",
        mode_prefix="pipeline:competition_fact_card",
    )
    check(
        "RoV ใช้สกินได้ไหม",
        ["คำตอบ:", "Default"],
        must_not_contain=["ไม่พบข้อมูล"],
        route_category="competition_rules",
        mode_prefix="pipeline:competition_fact_card",
    )
    check(
        "สมาชิกในทีม ROV ต้องมีกี่คน",
        ["คำตอบ:", "5v5", "ฝ่ายละ 5 คน", "ยังไม่พบจำนวนสมาชิกทีม"],
        must_not_contain=["4. ระเบียบและกติกาการแข่งขัน", "ไม่พบข้อมูล"],
        route_category="competition_rules",
        mode_prefix="pipeline:competition_fact_card",
    )
    check(
        "Tekken 8 ใช้เครื่องอะไรแข่ง",
        ["คำตอบ:", "PlayStation 5"],
        must_not_contain=["ไม่พบข้อมูล"],
        route_category="competition_rules",
        mode_prefix="pipeline:competition_fact_card",
    )
    check(
        "VALORANT แผนที่ที่ใช้แข่งมีอะไรบ้าง",
        ["คำตอบ:", "Abyss", "Ascent"],
        must_not_contain=["ไม่พบข้อมูล"],
        route_category="competition_rules",
        mode_prefix="pipeline:competition_fact_card",
    )
    check(
        "RoV ถ้าเริ่มแข่งช้าเกิน 15 นาทีโดนอะไร",
        ["คำตอบ:", "15 นาที", "ปรับแพ้"],
        must_not_contain=["ไม่พบข้อมูล"],
        route_category="competition_rules",
        mode_prefix="pipeline:competition_fact_card",
    )
    check(
        "CS2 technical pause ได้กี่ครั้ง",
        ["คำตอบ:", "Technical Pause", "2 ครั้ง", "10 นาที"],
        must_not_contain=["ไม่พบข้อมูล"],
        route_category="competition_rules",
        mode_prefix="pipeline:competition_fact_card",
    )
    check(
        "Tekken 8 ใช้ DLC character ได้ไหม",
        ["คำตอบ:", "ยกเว้นตัวละคร DLC", "Customization"],
        must_not_contain=["ไม่พบข้อมูล"],
        route_category="competition_rules",
        mode_prefix="pipeline:competition_fact_card",
    )
    check(
        "RoV ใช้ iPad แข่งได้ไหม",
        ["คำตอบ:", "ไม่อนุญาต", "Tablet", "iPad"],
        must_not_contain=["ไม่พบข้อมูล"],
        route_category="competition_rules",
        mode_prefix="pipeline:competition_fact_card",
    )
    check(
        "เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท แบบภาษาคนทั่วไป",
        ["ราคา 0 บาท", "PlayStation 5"],
        must_not_contain=["ราคา 150 บาท สำหรับกลุ่ม General Adult"],
        route_category="service_fee",
    )
    check(
        "ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่ แบบภาษาคนทั่วไป",
        ["ราคา 190 บาท", "VR 30 นาที"],
        must_not_contain=["ราคา 525 บาท สำหรับกลุ่ม General Adult"],
        route_category="service_fee",
    )
    check(
        "เป็นนักศึกษา สจล อยากเล่น PC เสียเท่าไหร่",
        ["General Student", "PC", "ยังไม่พบราคา"],
        must_not_contain=["ไม่พบข้อมูล"],
        route_category="service_fee",
    )
    check(
        "เด็กจุฬา เล่น PC กี่บาท",
        ["ราคา PC", "ยังไม่พบราคา", "General Student", "มหาลัยอื่น"],
        must_not_contain=["จากคำว่า", "สจล", "ไม่พบข้อมูล"],
        route_category="service_fee",
    )
    check(
        "เด็กลาดกระบังเล่น VR ครึ่งชั่วโมงราคาเท่าไหร่",
        ["ราคา 190 บาท", "General Student", "VR 30 นาที"],
        must_not_contain=["ราคา 525 บาท สำหรับกลุ่ม General Adult"],
        route_category="service_fee",
    )
    check(
        "เด็ก สจล เล่น VR พี่บาท",
        ["ราคา VR", "190 บาท", "375 บาท", "General Student", "มหาลัยอื่น"],
        must_not_contain=["จากคำว่า", "ให้ดูราคา General Student", "ไม่พบข้อมูล"],
        route_category="service_fee",
    )
    check(
        "นักศึกษาจุฬาเล่นเพลย์ห้าเท่าไหร่",
        ["ราคา 50 บาท", "General Student", "PlayStation 5"],
        must_not_contain=["ราคา 0 บาท"],
        route_category="service_fee",
    )
    check(
        "ทำเมาส์พังต้องเสียค่าปรับไหม",
        ["ต้องรับผิดชอบ", "100-500", "500-2,000"],
        route_category="penalty",
    )
    check(
        "สอนจองได้รึเปล่า",
        ["ขั้นตอนจอง", "กรอก", "แนบสลิป", "10 นาที"],
        route_category="reservation",
    )
    check(
        "สเป็ค PC เป็นยังไง",
        ["Intel Core i5-14400", "DDR5 32GB", "RTX 5060"],
        route_category="equipment",
    )
    print("ANSWER QUALITY PIPELINE SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
