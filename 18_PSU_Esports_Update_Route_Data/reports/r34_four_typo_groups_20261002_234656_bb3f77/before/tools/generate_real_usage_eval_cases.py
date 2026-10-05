from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
ROUTING_OUT = ROOT / "data" / "routing" / "routing_eval_real_usage.jsonl"
ANSWER_OUT = ROOT / "data" / "eval" / "answer_quality_cases.jsonl"


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "\n".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) for row in rows)
    path.write_text(text + "\n", encoding="utf-8")


def _route_case(
    case_id: str,
    question: str,
    category: str,
    intent: str,
    domain: str,
    operation: str,
    *,
    must_not_category: list[str] | None = None,
    notes: str = "",
) -> dict[str, Any]:
    return {
        "id": case_id,
        "question": question,
        "expected_category": category,
        "expected_intent": intent,
        "expected_domain": domain,
        "expected_operation": operation,
        "must_not_category": must_not_category or [],
        "notes": notes,
    }


def _answer_case(
    case_id: str,
    question: str,
    *,
    category: str,
    must_contain: list[str],
    must_not_contain: list[str] | None = None,
    source_keywords: list[str] | None = None,
    format_rules: list[str] | None = None,
    notes: str = "",
    min_score: float = 8.0,
) -> dict[str, Any]:
    return {
        "id": case_id,
        "question": question,
        "expected_category": category,
        "must_contain": must_contain,
        "must_not_contain": must_not_contain or [],
        "source_keywords": source_keywords or [],
        "format_rules": format_rules or [],
        "notes": notes,
        "min_score": min_score,
    }


def build_routing_cases() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []

    service_fee_questions = [
        "นักศึกษา PSU เล่น Nintendo Switch ราคาเท่าไหร่",
        "เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท",
        "คนนอกเล่น VR กี่บาท",
        "ต่างมหาลัยเล่น VR ครึ่งชั่วโมงราคาเท่าไหร่",
        "บุคคลทั่วไปจอง Cockpit ราคาเท่าไหร่",
        "นักศึกษาจุฬาเล่น PS5 เท่าไหร่",
        "เด็กลาดกระบังเล่น VR 30 นาทีราคาเท่าไหร่",
        "Nintendo Switch 3 คนราคาเท่าไหร่",
        "ค่าเล่นแต่ละเครื่องมีอะไรบ้าง",
        "service fee table มีอะไรบ้าง",
        "PS5 ฟรีไหมถ้าเป็นนักศึกษา PSU",
        "ไม่มีบัตรนักศึกษา เล่นเพลย์ห้าจ่ายกี่บาท",
        "ถ้าจอง PS5 9โมงถึง11โมงเสียกี่บาท",
        "วันจันทร์เล่น PS5 9โมงถึง12โมงเสียเท่าไหร่",
        "VR 2 ชั่วโมงคนนอกเสียเงินเท่าไหร่",
        "นักศึกษาต่างมหาลัยเล่น Nintendo Switch 3 คน 2 ชั่วโมงเสียเท่าไหร่",
        "เด็ก สจล เล่น VR พี่บาท",
        "ค่าเล่นคอมเท่าไหร่",
        "PC ราคาเท่าไร",
        "นักศึกษา PSU เล่น Cockpit ต้องจ่ายไหม",
    ]
    for idx, question in enumerate(service_fee_questions, 1):
        operation = "list" if any(term in question.lower() for term in ["table", "แต่ละเครื่อง"]) else "price_calculate"
        rows.append(_route_case(f"RU-SF-{idx:03d}", question, "service_fee", "service_fee_query", "service_fee", operation, must_not_category=["games", "equipment"]))

    game_list_questions = [
        "เกมทั้งหมดมีอะไรบ้าง",
        "ตอนนี้มีเกมอะไรบ้าง",
        "PS5 มีเกมอะไรบ้าง",
        "เกมใน PS5 มีอะไรมั่ง",
        "Nintendo Switch มีเกมอะไร",
        "VR มีเกมอะไรบ้าง",
        "Cockpit มีเกมอะไรบ้าง",
        "PC Zone มีเกมอะไร",
        "เกมแนว MOBA มีอะไรบ้าง",
        "มีเกมแข่งอะไรบ้าง",
        "รายการแข่งขันมีเกมอะไร",
        "มีเกมใน Nintendo อะไรบ้าง",
        "เกมบน PlayStation มีอะไร",
        "มีเกมรถแข่งอะไร",
        "มีเกม VR อะไรให้เล่น",
    ]
    for idx, question in enumerate(game_list_questions, 1):
        category = "games"
        intent = "competition_game_list" if any(term in question for term in ("รายการแข่ง", "รายการแข่งขัน", "เกมแข่งอะไร", "ทัวร์")) else ""
        operation = "list"
        rows.append(_route_case(f"RU-GM-{idx:03d}", question, category, intent, "games", operation, must_not_category=["service_fee"]))

    game_availability_questions = [
        "มี TEKKEN 8 ไหม",
        "อยากเล่น Mario Kart ต้องไปโซนไหน",
        "Fortnite เล่นได้ที่ไหน",
        "Beat Saber อยู่โซนไหน",
        "มี Minecraft ให้เล่นไหม",
        "ROV มีข้อมูลไหม",
        "อยากเล่น Gran Turismo ใช้อะไร",
        "มีเกมมายคราฟไหม",
        "Mario Party อยู่เครื่องไหน",
        "Valorant เล่นได้ไหม",
    ]
    for idx, question in enumerate(game_availability_questions, 1):
        if question == "อยากเล่น Gran Turismo ใช้อะไร":
            rows.append(_route_case(f"RU-GA-{idx:03d}", question, "games", "game_detail_lookup", "games", "how_to", must_not_category=["service_fee"]))
        else:
            rows.append(_route_case(f"RU-GA-{idx:03d}", question, "games", "game_availability_lookup", "games", "availability", must_not_category=["service_fee"]))

    control_questions = [
        "TEKKEN 8 ปุ่มทั้งหมดมีอะไรบ้าง",
        "Mario Kart กดปุ่มอะไร",
        "Mario Kart Live ปุ่มเร่งกดอะไร",
        "Overcooked ใช้ controller ยังไง",
        "ปุ่ม R1 ใน TEKKEN 8 ทำอะไร",
        "Call of Duty ปุ่มกระโดดกดอะไร",
        "ปุ่มทั้งหมดของเทคเคน 8 มีอะไรบ้าง",
        "Beat Saber ใช้ปุ่มอะไร",
        "เกมนี้มีปุ่มอะไรบ้าง",
        "เล่นยังไง",
    ]
    for idx, question in enumerate(control_questions, 1):
        intent = "game_control_lookup"
        domain = "general" if question == "เล่นยังไง" else "game_controls"
        operation = "how_to" if question == "เล่นยังไง" else "control"
        rows.append(_route_case(f"RU-CTRL-{idx:03d}", question, "games", intent, domain, operation, must_not_category=["service_fee"]))

    booking_questions = [
        "จอง PS5 ยังไง",
        "ถ้าจะเล่น Nintendo Switch ต้องจองยังไง",
        "จองแล้วต้องเช็คอินไหม",
        "ไม่มีบัตรนักศึกษาตอนจองทำยังไง",
        "สอนจองได้รึเปล่า",
        "จอง Nintendo Switch ต้องเลือกอะไรบ้าง",
        "จอง Nintendo Switch ต้องระบุจำนวนผู้เล่นไหม",
        "อยากเล่นพวงมาลัยต้องจองโซนอะไร",
        "คนนึงเล่นได้กี่ชั่วโมงต่อวัน",
        "PS5 เล่นได้กี่ชั่วโมงต่อวัน",
        "ต้องจ่ายภายในกี่นาที",
        "จองผิดแก้ยังไง",
        "ยกเลิกการจองได้ไหม",
        "จองล่วงหน้าได้ไหม",
        "เช็คอินล่วงหน้าได้กี่นาที",
    ]
    for idx, question in enumerate(booking_questions, 1):
        operation = "count" if "กี่ชั่วโมง" in question else "how_to"
        intent = "booking_policy"
        if question in {"สอนจองได้รึเปล่า", "จองผิดแก้ยังไง"}:
            intent = "how_to"
        elif question in {"ต้องจ่ายภายในกี่นาที"}:
            intent = "count"
            operation = "count"
        elif question in {"จอง Nintendo Switch ต้องระบุจำนวนผู้เล่นไหม", "เช็คอินล่วงหน้าได้กี่นาที"}:
            operation = "count"
        rows.append(_route_case(f"RU-RSV-{idx:03d}", question, "reservation", intent, "reservation", operation, must_not_category=["games", "service_fee"]))

    member_questions = [
        "สมาชิก PSU Esport มีกี่หมวด",
        "ตอนนี้สตาฟมีใครบ้าง",
        "ใครเป็นผู้จัดการ",
        "ตำแหน่ง Game and 3D Developer คือใคร",
        "cooperative education มีใครบ้าง",
        "PSU Phuket Esports Club มีใครบ้าง",
        "Internship Student มีใครบ้าง",
        "ใครเป็น Web & AI Developer",
        "สมาชิกหน้า Members มีทั้งหมดกี่คน",
        "แต่ละหมวดสมาชิกมีใครบ้าง",
    ]
    for idx, question in enumerate(member_questions, 1):
        if "กี่หมวด" in question:
            intent, operation = "group_count", "group_count"
        elif "ใครเป็น" in question or "คือใคร" in question:
            intent, operation = "members_lookup", "role_lookup"
        else:
            intent, operation = "list", "list"
        if question == "Internship Student มีใครบ้าง":
            intent = "members_lookup"
        if question == "สมาชิกหน้า Members มีทั้งหมดกี่คน":
            intent, operation = "group_count", "count"
        rows.append(_route_case(f"RU-MEM-{idx:03d}", question, "overview", intent, "members", operation, must_not_category=["games"]))

    equipment_questions = [
        "Home มีอุปกรณ์อะไรบ้าง",
        "PC Zone มีอุปกรณ์อะไร",
        "PS5 ใช้เครื่องรุ่นไหน",
        "Cockpit มีพวงมาลัยอะไร",
        "Nintendo Switch Zone มีทีวีกี่นิ้ว",
        "VR ใช้แว่นอะไร",
        "มีเมาส์คีย์บอร์ดไหม",
        "PC มีสเปคอะไร",
        "มีจอกี่ตัว",
        "PlayStation 5 Zone มีอะไรบ้าง",
    ]
    for idx, question in enumerate(equipment_questions, 1):
        operation = "count" if "กี่" in question else ("detail" if any(term in question for term in ["รุ่นไหน", "พวงมาลัยอะไร", "สเปค", "แว่นอะไร"]) else "list")
        intent = "equipment_item_lookup" if any(term in question for term in ["รุ่นไหน", "พวงมาลัยอะไร", "กี่นิ้ว", "สเปค", "แว่นอะไร"]) else "list"
        rows.append(_route_case(f"RU-EQ-{idx:03d}", question, "equipment", intent, "equipment", operation, must_not_category=["service_fee"]))

    schedule_questions = [
        "วันจันทร์เปิดกี่โมง",
        "ศุกร์บ่ายเล่นได้ไหม",
        "ช่วงเช้าเปิดไหม",
        "วันนี้เปิดไหม",
        "พรุ่งนี้เปิดหรือเปล่า",
        "วันไหน maintenance",
        "วันพุธช่วงเช้าเล่นได้ไหม",
        "พฤหัสปิดกี่โมง",
        "เดือนนี้ศูนย์ปิดวันไหนบ้าง",
        "28 กรกฎา เปิดไหม",
    ]
    for idx, question in enumerate(schedule_questions, 1):
        operation = "availability" if "ได้ไหม" in question or "เปิดไหม" in question else "schedule_lookup"
        if question in {"ช่วงเช้าเปิดไหม", "วันนี้เปิดไหม", "28 กรกฎา เปิดไหม"}:
            operation = "schedule_lookup"
        rows.append(_route_case(f"RU-SCH-{idx:03d}", question, "schedule", "schedule_query", "schedule", operation, must_not_category=["games", "service_fee"]))

    rules_questions = [
        "เอาอาหารเข้าได้ไหม",
        "เอาน้ำเข้าไปได้ไหม",
        "ของหายทำยังไง",
        "ทำเมาส์พังต้องเสียค่าปรับไหม",
        "ทำจอยพังโดนปรับเท่าไหร่",
        "จอแตกต้องชดเชยไหม",
        "สูบบุหรี่ได้ไหม",
        "เอาแอลกอฮอล์เข้าได้ไหม",
        "ทิ้งขยะไม่เป็นที่โดนอะไร",
        "อุปกรณ์เสียหายต้องทำยังไง",
    ]
    for idx, question in enumerate(rules_questions, 1):
        penalty = any(term in question for term in ["พัง", "เสียหาย", "ปรับ", "จอแตก", "ชดเชย"])
        rows.append(_route_case(
            f"RU-RULE-{idx:03d}",
            question,
            "penalty" if penalty else "rules",
            "penalty_policy" if penalty else "studio_rules",
            "penalty" if penalty else "rules",
            "rule_lookup",
            must_not_category=["service_fee", "games"],
        ))

    general_questions = [
        "เมืองหลวงของประเทศไทยคืออะไร",
        "นายเป็นใคร",
        "ทำอะไรได้บ้าง",
        "สวัสดี",
        "วันนี้อากาศดีไหม",
    ]
    for idx, question in enumerate(general_questions, 1):
        if question in {"นายเป็นใคร", "ทำอะไรได้บ้าง", "สวัสดี"}:
            rows.append(_route_case(f"RU-GEN-{idx:03d}", question, "knowledge", "detail", "knowledge", "detail", must_not_category=["games", "service_fee"]))
        else:
            expected_intent = "detail" if question == "วันนี้อากาศดีไหม" else "general_knowledge_query"
            rows.append(_route_case(f"RU-GEN-{idx:03d}", question, "general", expected_intent, "general", "detail", must_not_category=["games", "service_fee"]))

    return rows


def build_answer_cases() -> list[dict[str, Any]]:
    return [
        _answer_case("AQ-SF-001", "PS5 ราคาเท่าไหร่", category="service_fee", must_contain=["PlayStation 5", "PSU Student and Staff", "General Adult", "150 บาท"], source_keywords=["SERVICE-FEE"], format_rules=["bullet"]),
        _answer_case("AQ-SF-002", "นักศึกษา PSU เล่น Nintendo Switch ราคาเท่าไหร่", category="service_fee", must_contain=["Nintendo Switch", "PSU Student and Staff", "0 บาท"], must_not_contain=["Nintendo Switch Zone มีเกม"], source_keywords=["SERVICE-FEE"], format_rules=["bullet"]),
        _answer_case("AQ-SF-003", "คนนอกเล่น VR กี่บาท", category="service_fee", must_contain=["VR 30 นาที", "525 บาท", "VR 1 ชั่วโมง", "1,050 บาท"], source_keywords=["SERVICE-FEE"], format_rules=["bullet"]),
        _answer_case("AQ-SF-004", "ถ้าจอง PS5 ตั้งแต่ 9โมงถึง11โมงเสียกี่บาท", category="service_fee", must_contain=["2 ชั่วโมง", "2 session", "09:00-10:00", "10:00-11:00"], source_keywords=["SERVICE-FEE"], format_rules=["bullet"]),
        _answer_case("AQ-SF-005", "ค่าเล่นแต่ละเครื่องมีอะไรบ้าง", category="service_fee", must_contain=["ตาราง Service Fee", "PlayStation 5", "Nintendo Switch", "Cockpit", "VR"], source_keywords=["SERVICE-FEE"], format_rules=["bullet"]),
        _answer_case("AQ-GM-001", "เกมทั้งหมดมีอะไรบ้าง", category="games", must_contain=["PC Zone", "PlayStation 5 Zone", "Nintendo Switch Zone", "VR Zone"], source_keywords=["our-games"], format_rules=["bullet"]),
        _answer_case("AQ-GM-002", "PS5 มีเกมอะไรบ้าง", category="games", must_contain=["PlayStation 5 Zone", "TEKKEN 8", "Marvel's Spider-Man 2"], must_not_contain=["ค่าบริการ"], source_keywords=["our-games"], format_rules=["bullet"]),
        _answer_case("AQ-GM-003", "มี TEKKEN 8 ไหม", category="games", must_contain=["TEKKEN 8", "PlayStation 5"], source_keywords=["our-games"]),
        _answer_case("AQ-GM-004", "มี Minecraft ให้เล่นไหม", category="games", must_contain=["ยังไม่พบ", "Minecraft"], must_not_contain=["NARUTO X BORUTO"], source_keywords=["our-games"]),
        _answer_case("AQ-CTRL-001", "TEKKEN 8 ปุ่มทั้งหมดมีอะไรบ้าง", category="games", must_contain=["TEKKEN 8", "Square", "Triangle", "Circle", "Cross"], source_keywords=["local://control_game"], format_rules=["bullet"]),
        _answer_case("AQ-CTRL-002", "Mario Kart Live ปุ่มเร่งกดอะไร", category="games", must_contain=["Mario Kart", "เร่ง"], source_keywords=["local://control_game"]),
        _answer_case("AQ-RSV-001", "จอง PS5 ยังไง", category="reservation", must_contain=["เลือกบริการ", "PlayStation 5", "รอบเวลา"], source_keywords=["esports"]),
        _answer_case("AQ-RSV-002", "ถ้าจะเล่น Nintendo Switch ต้องจองยังไง", category="reservation", must_contain=["Nintendo Switch", "1-2 Persons", "3-4 Persons"], must_not_contain=["Mario Kart 8 Deluxe"], source_keywords=["esports"], format_rules=["bullet"]),
        _answer_case("AQ-RSV-003", "PS5 เล่นได้กี่ชั่วโมงต่อวัน", category="reservation", must_contain=["สูงสุด 3 Sessions", "PlayStation 5"], must_not_contain=["Friday"], source_keywords=["esports"]),
        _answer_case("AQ-MEM-001", "สมาชิก PSU Esport มีกี่หมวด", category="overview", must_contain=["3 หมวด", "Members", "cooperative education", "PSU Phuket Esports Club"], source_keywords=["Members"], format_rules=["bullet"]),
        _answer_case("AQ-MEM-002", "ใครเป็นผู้จัดการ", category="overview", must_contain=["นายชนะชัย สิริพันธ์วราภรณ์", "ผู้จัดการ"], source_keywords=["Members"]),
        _answer_case("AQ-MEM-003", "ตำแหน่ง Game and 3D Developer คือใคร", category="overview", must_contain=["นายณภัทร เชื้อเหล่าวานิช", "Game and 3D Developer"], source_keywords=["Members"]),
        _answer_case("AQ-EQ-001", "อุปกรณ์บนหน้า Home มีอะไรบ้าง", category="equipment", must_contain=["PC Zone", "Gaming PC", "Cockpit Zone", "Nintendo Switch Zone", "VR Zone"], source_keywords=["Home"], format_rules=["bullet"]),
        _answer_case("AQ-EQ-002", "PC มีสเปคอะไร", category="equipment", must_contain=["Intel Core i5-14400", "DDR5 32GB", "RTX 5060"], source_keywords=["Home"]),
        _answer_case("AQ-EQ-003", "Cockpit มีพวงมาลัยอะไร", category="equipment", must_contain=["Logitech G923", "Driving Force Shifter"], source_keywords=["Home"]),
        _answer_case("AQ-SCH-001", "วันจันทร์เปิดกี่โมง", category="schedule", must_contain=["วันจันทร์", "09:00-12:00", "13:00-16:00"], source_keywords=["Reservation"]),
        _answer_case("AQ-SCH-002", "ศุกร์บ่ายเล่นได้ไหม", category="schedule", must_contain=["วันศุกร์", "Afternoon", "Maintenance"], source_keywords=["Reservation"]),
        _answer_case("AQ-RULE-001", "เอาอาหารเข้าได้ไหม", category="rules", must_contain=["อาหาร", "เครื่องดื่ม", "พื้นที่ที่กำหนด"], source_keywords=["reservation"]),
        _answer_case("AQ-RULE-002", "ทำจอยพังโดนปรับเท่าไหร่", category="penalty", must_contain=["ค่าปรับ", "100-500", "500-2,000"], must_not_contain=["ปุ่ม"], source_keywords=["reservation"]),
        _answer_case("AQ-GEN-001", "นายเป็นใคร", category="knowledge", must_contain=["PSU Esports Assistant", "PSU Esports Studio - Phuket"], format_rules=["bullet"]),
        _answer_case("AQ-GEN-002", "เมืองหลวงของประเทศไทยคืออะไร", category="general", must_contain=["Local LLM", "ยังไม่ได้เปิด"], min_score=7.0),
    ]


def main() -> int:
    routing_cases = build_routing_cases()
    answer_cases = build_answer_cases()
    _write_jsonl(ROUTING_OUT, routing_cases)
    _write_jsonl(ANSWER_OUT, answer_cases)
    print(f"Wrote {len(routing_cases)} routing cases -> {ROUTING_OUT}")
    print(f"Wrote {len(answer_cases)} answer quality cases -> {ANSWER_OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
