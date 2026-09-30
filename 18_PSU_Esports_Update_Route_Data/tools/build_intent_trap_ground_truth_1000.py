#!/usr/bin/env python3
"""Build review-candidate cases for wrong-intent answers seen in live chat."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data/eval/intent_trap_bilingual_1000_v2.jsonl"
MANIFEST = ROOT / "data/eval/intent_trap_bilingual_1000_v2_manifest.json"

WRAPPERS = {
    "th": (
        "{q}",
        "ขอถามเกี่ยวกับศูนย์หน่อยครับ: {q}",
        "ก่อนเดินทางไปใช้บริการ อยากทราบว่า {q}",
        "{q} ตอบเฉพาะประเด็นที่ถามได้ไหม",
        "ช่วยอ้างอิงข้อมูลที่ยืนยันได้: {q}",
    ),
    "en": (
        "{q}",
        "A question about the studio: {q}",
        "Before visiting, I need to know: {q}",
        "{q} Please answer only that point.",
        "Please use verified studio information: {q}",
    ),
}

# Each row is one distinct scenario with a Thai and English rendering. Variants
# below change conversational framing, not the factual claim under test.
SCENARIOS = {
    "fee_without_service": [
        ("บุคคลภายนอกใช้อุปกรณ์คิดราคาเท่าไหร่", "How much does equipment use cost for an outsider?"),
        ("คนทั่วไปเข้าไปเล่นคิดเงินยังไง", "What would a member of the public pay to play?"),
        ("ค่าใช้บริการสำหรับคนนอกเท่าไหร่", "What is the service fee for a non-PSU visitor?"),
        ("ถ้าไม่ใช่นักศึกษาใช้อุปกรณ์ราคาเท่าไหร่", "How much is equipment use if I am not a student?"),
        ("มีราคาเดียวสำหรับทุกอุปกรณ์ไหม คนภายนอกจ่ายเท่าไหร่", "Is there one price for all equipment for external visitors?"),
        ("อยากรู้ราคาเล่นเกมของบุคคลทั่วไป", "I need the gaming price for a general visitor."),
        ("ค่าบริการของศูนย์สำหรับคนนอกเริ่มต้นเท่าไหร่", "What is the starting price for an outsider?"),
        ("ผมไม่ได้เรียน PSU อยากทราบราคาการใช้งาน", "I do not study at PSU; what would I pay to use the studio?"),
        ("ถ้ามาใช้เครื่องเล่นแต่ยังไม่รู้โซน ต้องจ่ายเท่าไหร่", "What would I pay to use a station if I have not chosen a zone?"),
        ("ถ้าผมเป็นบุคคลภายนอกต้องจ่ายเท่าไหร่เมื่อใช้อุปกรณ์", "As an outsider, how much would I pay to use the equipment?"),
    ],
    "booking_days_hours": [
        ("การจองเครื่องเล่นเกมเปิดจองวันไหนและช่วงเวลาไหนบ้าง", "On which days and at what hours can I book a gaming station?"),
        ("จอง PC ได้วันอะไร ช่วงกี่โมง", "Which days and time periods are available for PC booking?"),
        ("มีรอบให้จองช่วงเช้ากับบ่ายวันไหนบ้าง", "On which days can I book morning and afternoon slots?"),
        ("เวลาเปิดให้จองเครื่อง PS5 เป็นช่วงไหน", "What hours are PS5 stations available to book?"),
        ("วันจันทร์จองช่วงเช้าได้ไหมหรือมีแต่บ่าย", "Can I book Monday morning, or only the afternoon?"),
        ("วันศุกร์ช่วงบ่ายจองได้หรือเป็นเวลาปิดดูแลเครื่อง", "Can I book Friday afternoon, or is it maintenance time?"),
        ("ตารางเวลาให้จองอุปกรณ์รายสัปดาห์เป็นอย่างไร", "What is the weekly schedule for booking equipment?"),
        ("อยากทราบวันและเวลาที่ศูนย์ให้บริการสำหรับการจอง", "What are the studio service days and hours for reservations?"),
        ("จอง VR ได้ในวันทำการช่วงเวลาไหน", "During which service hours can I book VR?"),
        ("เสาร์อาทิตย์เปิดรอบให้จองเครื่องเกมไหม", "Are gaming stations bookable on weekends?"),
    ],
    "outsider_eligibility": [
        ("บุคคลภายนอกเข้าใช้ศูนย์ได้ไหม", "Can members of the public use the studio?"),
        ("คนที่ไม่ใช่นักศึกษา PSU เข้าไปเล่นได้หรือเปล่า", "Can someone who is not a PSU student play there?"),
        ("แขกจากมหาวิทยาลัยอื่นมีสิทธิ์จองไหม", "Can a visitor from another university make a booking?"),
        ("คนทั่วไปต้องเป็นสมาชิกก่อนเข้าศูนย์หรือไม่", "Does a public visitor need membership before entering?"),
        ("ผู้ปกครองเข้าไปใช้อุปกรณ์ได้ไหม", "May a parent use the studio equipment?"),
        ("คนนอกที่ไม่มีรหัสนักศึกษาจองเครื่องได้ไหม", "Can an outsider without a student ID reserve a station?"),
        ("บุคคลทั่วไปเข้าใช้ PC Zone ได้หรือไม่", "Is the PC Zone open to the general public?"),
        ("ศิษย์เก่าที่ไม่มีบัตรนักศึกษาเข้าใช้ได้ไหม", "Can an alumnus without a student card use the studio?"),
        ("ผู้มาเยือนต่างจังหวัดจองใช้เครื่องได้หรือเปล่า", "Can a visitor from outside Phuket book a station?"),
        ("คนภายนอกต้องใช้เอกสารอะไรเพื่อเข้าใช้", "What ID does an external visitor need to use the studio?"),
    ],
    "damage_responsibility": [
        ("ถ้าทำ PS5 ของศูนย์เสียหายต้องเสียค่าปรับไหม", "If I damage a studio PS5, is there a penalty?"),
        ("ทำจอยเกมพังต้องรับผิดชอบยังไง", "What happens if I break a game controller?"),
        ("จอคอมแตกตอนใช้งานต้องชดใช้เท่าไหร่", "What compensation applies if I break a PC monitor?"),
        ("เผลอทำอุปกรณ์ของศูนย์เสียต้องแจ้งใครและจ่ายไหม", "If I accidentally damage studio equipment, must I report and pay?"),
        ("อุปกรณ์เสียหายเล็กน้อยคิดค่าปรับอย่างไร", "What fine applies to minor equipment damage?"),
        ("ทำพวงมาลัย Cockpit พังมีความรับผิดชอบอะไร", "What am I responsible for if the Cockpit wheel breaks?"),
        ("แว่น VR เสียเพราะผู้เล่นต้องจ่ายค่าซ่อมหรือเปล่า", "Must a player pay repair costs for damaging the VR headset?"),
        ("ถ้าทำเครื่อง Nintendo Switch ตกจะมีค่าปรับไหม", "Is there a fine if I drop a Nintendo Switch?"),
        ("ทำเมาส์เกมมิ่งเสียหายต้องชดเชยไหม", "Would I owe compensation for damaging a gaming mouse?"),
        ("ใครรับผิดชอบค่าเสียหายเมื่อผู้ใช้ทำเก้าอี้พัง", "Who pays when a user damages a gaming chair?"),
    ],
    "food_bring_scope": [
        ("นำอาหารและเครื่องดื่มเข้าศูนย์ได้ไหม", "May I bring food and drinks into the studio?"),
        ("ถือขวดน้ำเข้าไปได้หรือเปล่า ไม่ได้ถามเรื่องกิน", "Can I carry a water bottle inside? I am not asking about drinking."),
        ("เอาขนมติดกระเป๋าเข้าไปในศูนย์ได้ไหม", "May I carry a snack in my bag into the studio?"),
        ("อนุญาตให้นำกาแฟเข้าอาคารหรือไม่", "Is bringing coffee into the building allowed?"),
        ("เอาอาหารจากข้างนอกเข้าไปแต่ไม่กินในห้องเล่นได้ไหม", "Can I bring outside food in without eating in the gaming area?"),
        ("พกเครื่องดื่มเข้าประตูศูนย์ได้ไหม", "May I take a drink through the studio entrance?"),
        ("นำอาหารกลับบ้านผ่านพื้นที่ศูนย์ได้หรือเปล่า", "Can I carry takeaway food through the studio?"),
        ("มีข้อห้ามเรื่องนำขวดน้ำเข้าศูนย์ไหม", "Is there a rule against bringing a water bottle inside?"),
        ("ถ้าแค่นำขนมเข้าไป ไม่รับประทาน ถือว่าผิดกฎไหม", "Is carrying a snack without eating it against the rules?"),
        ("นำเครื่องดื่มส่วนตัวเข้าพื้นที่ได้หรือไม่", "Can I bring my own beverage onto the premises?"),
    ],
    "food_consumption": [
        ("รับประทานอาหารในศูนย์ได้ตรงไหน", "Where in the studio may I eat food?"),
        ("กินข้าวที่โต๊ะเกมได้ไหม", "May I eat at a gaming desk?"),
        ("ดื่มน้ำในโซนเล่นเกมได้หรือเปล่า", "Can I drink in the gaming zone?"),
        ("พื้นที่ไหนอนุญาตให้กินขนม", "Which area allows snacks to be eaten?"),
        ("กาแฟดื่มได้เฉพาะจุดที่กำหนดใช่ไหม", "Must coffee be consumed only in a designated area?"),
        ("มีกฎเรื่องการรับประทานเครื่องดื่มอย่างไร", "What is the rule for consuming drinks?"),
        ("กินอาหารระหว่างเล่น PC ได้ไหม", "May I eat while playing on a PC?"),
        ("ถ้าหิวต้องไปกินอาหารตรงไหน", "Where should I go to eat if I get hungry?"),
        ("เครื่องดื่มกินที่โต๊ะ Nintendo ได้หรือไม่", "May I drink at a Nintendo station?"),
        ("อาหารต้องกินในบริเวณที่จัดไว้เท่านั้นหรือเปล่า", "Is eating restricted to designated spaces?"),
    ],
    "weekday_live_slots": [
        ("วันจันทร์มี PC เครื่องไหนว่างบ้างตอนบ่ายโมง", "Which PC stations are free on Monday at 1 pm?", 0),
        ("วันอังคารบ่ายสอง PC 2 ว่างไหม", "Is PC 2 free on Tuesday at 2 pm?", 1),
        ("วันพุธเวลา 13:00 VR ว่างหรือเปล่า", "Is VR available Wednesday at 13:00?", 2),
        ("วันพฤหัสฯ ตอนบ่ายสาม PS5 เครื่อง 1 ว่างไหม", "Is PS5 station 1 free Thursday at 3 pm?", 3),
        ("วันศุกร์บ่ายโมงมี Nintendo ว่างไหม", "Is a Nintendo station free Friday at 1 pm?", 4),
        ("จันทร์หน้า 14:00 Cockpit ถูกจองแล้วหรือยัง", "Is the Cockpit booked next Monday at 14:00?", 0),
        ("อังคารนี้ช่วง 09:00 PC เครื่องไหนยังไม่ถูกจอง", "Which PCs are unbooked this Tuesday at 09:00?", 1),
        ("พุธหน้าบ่ายโมงมี PS5 ว่างกี่เครื่อง", "How many PS5 stations are free next Wednesday at 1 pm?", 2),
        ("พฤหัสบดีตอน 15:00 Nintendo เครื่อง 2 ว่างไหม", "Is Nintendo station 2 free Thursday at 15:00?", 3),
        ("ศุกร์นี้ 10:00 VR มีรอบว่างหรือไม่", "Is a VR slot open this Friday at 10:00?", 4),
    ],
    "identity_typo": [
        ("นายเปนไค", "who r u"),
        ("นายเปนใคร", "who are u"),
        ("นายนี่คือใคร", "who is this bot"),
        ("บอทนีคือใคร", "what bot is this"),
        ("คุณเปนผู้ช่วยอะไร", "wat assistant is this"),
        ("ไครตอบอยู่", "who is answering me"),
        ("นี่คนหรือบอท", "is this a bot or a person"),
        ("บอกหน่อยคุนเป็นใคร", "tell me who u are"),
        ("นายทำหน้าที่อะไล", "what do u do here"),
        ("บอทนี้ชื่ออาราย", "what is this chat assistant called"),
    ],
    "equipment_access_trap": [
        ("บุคคลภายนอกเข้าใช้อุปกรณ์ในห้องอีสปอร์ตได้มั้ย", "Can outsiders come in and use the equipment?"),
        ("คนทั่วไปมีสิทธิ์เล่นเครื่อง PC ของศูนย์ไหม", "Are public visitors permitted to use the studio PCs?"),
        ("ถ้าไม่มีรหัส PSU ใช้เครื่อง PS5 ได้หรือเปล่า", "May someone without a PSU ID use the PS5?"),
        ("คนภายนอกเข้าไปใช้แว่น VR ได้ไหม", "Can an external visitor use the VR headset?"),
        ("คนที่ไม่ได้เรียนที่นี่เข้าใช้ Cockpit ได้หรือไม่", "Can a non-student access the Cockpit?"),
        ("ผู้ปกครองใช้อุปกรณ์ Nintendo ได้ไหม", "May a parent use the Nintendo equipment?"),
        ("เครื่อง PC เปิดให้บุคคลทั่วไปเข้าใช้หรือเฉพาะนักศึกษา", "Are the PCs for public visitors or students only?"),
        ("นักท่องเที่ยวเข้ามาใช้อุปกรณ์ของศูนย์ได้ไหม", "Can a tourist use the studio's equipment?"),
        ("คนนอกเข้าใช้เก้าอี้กับเครื่องเล่นได้ไหม", "Can an outsider use the gaming stations and chairs?"),
        ("มีข้อจำกัดว่าใครเข้าใช้เครื่องในศูนย์ได้บ้าง", "Who is eligible to use the studio stations?"),
    ],
    "unclear_or_outside_scope": [
        ("ไก่กับไข่อะไรเกดก่อน", "wich came first chicken or egg"),
        ("พิมพ์ผิดแหละ ช่วยเดาหน่อยว่าอยากถามไร", "I typed nonsense; guess my question"),
        ("วันนี้อากาศดีไหม", "Is the weather good today?"),
        ("แนะนำหุ้นให้หน่อย", "Which stock should I buy?"),
        ("ถามเรื่องอื่นได้ปะ", "Can I ask about something unrelated?"),
        ("ฮัลโหลลล", "helllooo"),
        ("ขอเรื่องที่ยังไม่บอกก็ได้ เดาเอา", "Make up an answer about the studio"),
        ("ถ้าบอกแค่ว่าเครื่องล่ะ", "What if I only say 'station'?"),
        ("ไม่รู้จะถามอะไร", "I do not know what to ask"),
        ("มั่วๆๆ เรื่องเกมมั้ง", "umm games or something idk"),
    ],
}

THEME_CONTRACTS = {
    "fee_without_service": ("clarification_required", ["clarification", "service_fee"], [], ["อุปกรณ์บนหน้า Home", "Verified equipment:"]),
    "booking_days_hours": ("answer_available", ["schedule", "reservation"], [], ["ขั้นตอนโดยสรุปคือ 1)"]),
    "outsider_eligibility": ("route_only", ["reservation", "rules", "no_answer", "clarification", "service_fee"], [], ["อุปกรณ์บนหน้า Home", "Verified equipment:"]),
    "damage_responsibility": ("answer_available", ["penalty", "rules"], ["ค่าปรับ", "ชดเชย", "รับผิดชอบ", "fine", "compensation", "responsible"], ["โหมดทดลอง RAG", "closest information"]),
    "food_bring_scope": ("route_only", ["rules", "no_answer", "clarification"], [], ["อนุญาตให้นำอาหารเข้า", "You may bring food inside"]),
    "food_consumption": ("answer_available", ["rules"], ["พื้นที่ที่กำหนด", "designated area"], []),
    "weekday_live_slots": ("live_lookup_required", ["schedule", "reservation", "clarification"], [], []),
    "identity_typo": ("answer_available", ["general", "overview", "home", "knowledge"], [], []),
    "equipment_access_trap": ("route_only", ["reservation", "rules", "no_answer", "clarification"], [], ["อุปกรณ์บนหน้า Home", "Verified equipment:"]),
    "unclear_or_outside_scope": ("route_only", ["general", "clarification", "no_answer", "overview", "knowledge"], [], ["อุปกรณ์บนหน้า Home", "Verified equipment:"]),
}


def _next_weekday(today, weekday: int):
    delta = (weekday - today.weekday()) % 7 or 7
    return today + timedelta(days=delta)


def build(today) -> list[dict]:
    rows: list[dict] = []
    for locale in ("th", "en"):
        serial = 0
        for theme, scenarios in SCENARIOS.items():
            status, routes, required_any, forbidden = THEME_CONTRACTS[theme]
            assert len(scenarios) == 10, theme
            for scenario_index, scenario in enumerate(scenarios, start=1):
                base = scenario[0 if locale == "th" else 1]
                for style_index, wrapper in enumerate(WRAPPERS[locale], start=1):
                    serial += 1
                    question = wrapper.format(q=base)
                    contract = {"must_contain": [], "must_contain_any": required_any, "must_not_contain": forbidden}
                    target_date = ""
                    if theme == "booking_days_hours":
                        if scenario_index == 5:
                            contract = {**contract, "must_contain_any": ["13:00", "maintenance", "Maintenance"]}
                        elif scenario_index == 6:
                            contract = {**contract, "must_contain_any": ["maintenance", "Maintenance", "09:00"]}
                        elif scenario_index == 10:
                            contract = {**contract, "must_contain_any": ["ไม่ได้", "ไม่พบ", "closed", "weekend", "not open"]}
                        else:
                            contract = {**contract, "must_contain_any": ["09:00", "13:00", "9:00", "1 pm"]}
                    if theme == "weekday_live_slots":
                        target_date = _next_weekday(today, scenario[2]).isoformat()
                        contract = {**contract, "must_contain": [target_date]}
                    rows.append({
                        "id": f"INTENT-TRAP-{locale.upper()}-{serial:04d}",
                        "suite": "psu_esports_intent_trap_candidate_v2",
                        "locale": locale,
                        "domain": theme,
                        "question": question,
                        "review_status": "scenario_curated_paraphrase_pending_review",
                        "expected_route_categories": routes,
                        "expected_answer_status": status,
                        "answer_contract": contract,
                        "expected_target": target_date,
                        "expected_facet": theme,
                        "latency_ceiling_sec": 20.0,
                        "metadata": {"scenario_id": f"{theme}_{scenario_index:02d}", "style_index": style_index, "reference_date": today.isoformat()},
                    })
        assert serial == 500, (locale, serial)
    questions = [row["question"].casefold() for row in rows]
    assert len(set(questions)) == 1000, "duplicate questions"
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    today = datetime.now(ZoneInfo("Asia/Bangkok")).date()
    rows = build(today)
    payload = "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows)
    if args.check:
        assert OUTPUT.read_text(encoding="utf-8") == payload
    else:
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(payload, encoding="utf-8")
        MANIFEST.write_text(json.dumps({
            "suite": "psu_esports_intent_trap_candidate_v2",
            "reference_date": today.isoformat(),
            "total": len(rows),
            "by_locale": dict(Counter(row["locale"] for row in rows)),
            "by_theme": dict(Counter(row["domain"] for row in rows)),
            "distinct_scenarios_per_locale": 100,
            "variants_per_scenario": 5,
            "sha256": hashlib.sha256(payload.encode("utf-8")).hexdigest(),
            "note": "Weekday live-slot expected dates are relative to reference_date. Rebuild before testing on another date; all cases require human review before promotion to approved Gold.",
        }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(rows)} cases; reference date {today}; corpus {OUTPUT}")


if __name__ == "__main__":
    main()
