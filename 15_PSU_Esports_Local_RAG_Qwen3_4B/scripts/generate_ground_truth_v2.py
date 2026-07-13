from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PROJECT_DIR = Path(__file__).resolve().parents[1]
OUTPUT_PATH = PROJECT_DIR / "ground_truth" / "ground_truth_v2_360.jsonl"
README_PATH = PROJECT_DIR / "ground_truth" / "README_v2.md"


rows: list[dict[str, Any]] = []
seen_questions: set[str] = set()


def add(
    category: str,
    question: str,
    expected_keywords: list[str],
    expected_source_keywords: list[str] | None = None,
    answer_type: str = "fact",
    difficulty: str = "medium",
    variant_type: str = "normal",
) -> None:
    question = " ".join(question.split())
    if question in seen_questions:
        return
    seen_questions.add(question)
    rows.append(
        {
            "id": f"v2_{len(rows) + 1:03d}",
            "category": category,
            "question": question,
            "expected_keywords": expected_keywords,
            "expected_source_keywords": expected_source_keywords or [],
            "answer_type": answer_type,
            "difficulty": difficulty,
            "variant_type": variant_type,
        }
    )


def add_many(category: str, questions: list[str], keywords: list[str], source: list[str], **kwargs: Any) -> None:
    for question in questions:
        add(category, question, keywords, source, **kwargs)


def build_schedule_cases() -> None:
    add_many(
        "reservation",
        [
            "วันจันทร์เปิดให้เล่นกีโมง ปิดกี่โมง",
            "วันจันทร์เปิดให้เล่นกี่โมงถึงกี่โมง",
            "จันทร์เปิดปิดยังไง",
            "วันจันทร์เล่นได้ตั้งแต่กี่โมง",
            "วันจันทร์มีรอบเล่นช่วงไหนบ้าง",
            "Monday open close time?",
            "monday hours for play",
            "ถ้าไปวันจันทร์เช้าเล่นได้ไหม แล้วเปิดจริงกี่โมง",
            "วันจันทร์ morning เล่นได้ไหม afternoon เปิดไหม",
            "จันทร์เช้า maintenance แล้วบ่ายเปิดกี่โมง",
        ],
        ["13:00", "16:00", "Maintenance"],
        ["Reservation"],
        variant_type="schedule_day_specific",
    )
    add_many(
        "reservation",
        [
            "วันจันทร์ช่วงเช้าเปิดไหม",
            "จันทร์ 9 โมงเล่นได้ไหม",
            "Monday morning available?",
            "วันจันทร์ 09:00-12:00 เป็นอะไร",
            "เช้าวันจันทร์เป็น maintenance ใช่ไหม",
        ],
        ["09:00", "12:00", "Maintenance"],
        ["Reservation"],
        variant_type="schedule_morning_maintenance",
    )
    add_many(
        "reservation",
        [
            "ศูนย์เปิดกีโมงปิดกี่โมง",
            "เปิดปิดกี่โมงนะ",
            "เวลาเปิดให้บริการคืออะไร",
            "service hours คืออะไร",
            "เปิดถึง 16:00 ใช่ไหม",
            "เปิด 24 ชม ไหม",
        ],
        ["09:00", "16:00", "Monday", "Friday", "Maintenance"],
        ["Reservation"],
        variant_type="schedule_general",
    )
    add_many(
        "reservation",
        [
            "ช่วงเช้าของตารางคือเวลาไหน",
            "Morning คือกี่โมงถึงกี่โมง",
            "รอบเช้า 09 ถึง 12 ใช่ไหม",
            "ช่วงเช้าเปิดตั้งแต่กี่โมงถึงเที่ยงไหม",
            "ตอนเช้าเปิดกี่โมง",
            "รอบเช้าเริ่มตอนไหน",
            "morning session time?",
            "morning slot time",
        ],
        ["09:00", "12:00", "Monday", "Friday", "Maintenance"],
        ["Reservation"],
        variant_type="schedule_morning",
    )
    add_many(
        "reservation",
        [
            "ช่วงบ่ายของตารางคือเวลาไหน",
            "Afternoon คือกี่โมงถึงกี่โมง",
            "รอบบ่าย 13 ถึง 16 ใช่ไหม",
            "ช่วงบ่ายเปิดกี่โมงปิดกี่โมง",
            "รอบบ่ายปิดกี่โมง",
            "afternoon session time?",
            "afternoon slot time",
        ],
        ["13:00", "16:00", "Monday", "Friday", "Maintenance"],
        ["Reservation"],
        variant_type="schedule_afternoon",
    )
    add_many(
        "reservation",
        [
            "วันศุกร์ maintenance คืออะไร",
            "Friday maintenance ทำอะไร",
            "maintenance weekly hardware inspection คืออะไร",
            "วันศุกร์มีตรวจอุปกรณ์ไหม",
            "ศุกร์ทำความสะอาดอุปกรณ์ใช่ไหม",
        ],
        ["13:00", "16:00", "Maintenance", "Weekly hardware inspection", "cleaning"],
        ["Reservation"],
        variant_type="schedule_maintenance",
    )


def build_price_cases() -> None:
    services = [
        ("ps5", ["PS5", "PlayStation 5", "เพลย์ห้า"], {"psu": 0, "general_student": 50, "adult": 150}, ["PlayStation 5", "60"]),
        ("nintendo_1_2", ["Nintendo 1-2 คน", "Switch 1-2", "นินเทนโด 2 คน"], {"psu": 0, "general_student": 50, "adult": 140}, ["Nintendo Switch", "1-2"]),
        ("nintendo_3_4", ["Nintendo 3-4 คน", "Switch 3-4", "นินเทนโด 4 คน"], {"psu": 0, "general_student": 100, "adult": 280}, ["Nintendo Switch", "3-4"]),
        ("cockpit", ["Cockpit", "พวงมาลัยขับรถ", "เครื่องขับรถ"], {"psu": 0, "general_student": 65, "adult": 200}, ["Cockpit", "60"]),
        ("vr_30", ["VR 30 นาที", "VR ครึ่งชั่วโมง", "แว่น VR 30 mins"], {"psu": 0, "general_student": 190, "adult": 525}, ["VR", "30"]),
        ("vr_60", ["VR 1 ชั่วโมง", "VR 60 นาที", "แว่น VR 1 hr"], {"psu": 0, "general_student": 375, "adult": 1050}, ["VR", "1 ชั่วโมง"]),
    ]
    groups = [
        ("psu", ["นักศึกษา มอ", "นักเรียน ม.อ.", "เด็ก PSU", "PSU student"], ["0", "บาท"]),
        ("general_student", ["นักศึกษาทั่วไป", "นักศึกษาต่างมหาลัย", "ศิษย์เก่า PSU", "General Student"], []),
        ("adult", ["บุคคลทั่วไป", "คนนอก", "General Adult", "adult"], []),
    ]
    phrasings = [
        "{group} เล่น {service} กี่บาทต่อชั่วโมง",
        "ถ้าเป็น{group} จอง {service} ราคาเท่าไหร่",
        "{service} สำหรับ{group} ต้องจ่ายกี่บาท",
    ]
    for _service_id, aliases, rates, service_keywords in services:
        for group_key, group_aliases, extra_keywords in groups:
            for alias in group_aliases[:3]:
                for service_name in aliases[:2]:
                    question = phrasings[(len(rows) + len(question := alias)) % len(phrasings)].format(
                        group=alias, service=service_name
                    )
                    add(
                        "service_fee",
                        question,
                        service_keywords + [str(rates[group_key])] + extra_keywords,
                        ["service_fee"],
                        answer_type="calculation",
                        difficulty="medium",
                        variant_type="price_synonym",
                    )
    add_many(
        "service_fee",
        [
            "ราคา PC ต่อชั่วโมงเท่าไหร่",
            "นักเรียน มอ เล่น PC ฟรีไหม",
            "คนนอกเล่นคอมต้องจ่ายเท่าไหร่",
            "PC มีราคาใน service fee ไหม",
            "ทำไมคำนวณ PC ไม่ได้",
            "จอง PC 9 ถึง 11 ต้องเสียกี่บาท",
            "ถ้าเล่น PC 2 ชั่วโมงคิดเงินยังไง",
            "PC price for general student?",
        ],
        ["PC", "ไม่พบ", "Service Fee"],
        ["service_fee"],
        answer_type="no_answer",
        difficulty="hard",
        variant_type="price_missing_data",
    )
    add_many(
        "service_fee",
        [
            "ราคาค่าบริการทั้งหมดมีอะไรบ้าง",
            "สรุป service fee ให้หน่อย",
            "ตารางราคา 2026 มีอะไร",
            "ค่าเล่นแต่ละเครื่องเท่าไหร่",
            "service fee table includes what",
            "ขอเรทราคา PS5 Switch Cockpit VR",
        ],
        ["PlayStation 5", "Nintendo Switch", "Cockpit", "VR"],
        ["service_fee"],
        answer_type="list",
        difficulty="medium",
        variant_type="price_summary",
    )


def build_booking_cases() -> None:
    add_many(
        "reservation",
        [
            "จองต้องล่วงหน้ากี่ชั่วโมง",
            "ถ้าจะเล่นบ่ายสองต้องจองก่อนอย่างน้อยกี่โมง",
            "ต้อง book ล่วงหน้ากี่ hr",
            "จองก่อน 1 ชั่วโมงใช่ไหม",
            "walk in ได้ไหมหรือต้องจองก่อน",
        ],
        ["1 ชั่วโมง"],
        ["Reservation"],
        variant_type="booking_advance",
    )
    add_many(
        "reservation",
        [
            "จองได้สูงสุดกี่ session",
            "ครั้งนึงจองได้กี่รอบ",
            "one booking max sessions?",
            "จองทีเดียว 4 sessions ได้ไหม",
            "จองสามรอบได้ไหม",
        ],
        ["3 Sessions"],
        ["Reservation"],
        variant_type="booking_max_session",
    )
    add_many(
        "reservation",
        [
            "หลังจองต้องจ่ายภายในกี่นาที",
            "ไม่จ่ายใน 10 นาทีจะเกิดอะไร",
            "payment timeout กี่นาที",
            "จองแล้วลืมจ่ายเงิน ระบบจะยกเลิกไหม",
            "ชำระเงินหลัง booking ต้องเร็วแค่ไหน",
        ],
        ["10 นาที", "ยกเลิก", "จองใหม่"],
        ["Reservation"],
        variant_type="payment_timeout",
    )
    add_many(
        "reservation",
        [
            "กดจองแล้วแก้ไขได้ไหม",
            "ถ้ากรอกข้อมูลผิดหลังจองต้องทำยังไง",
            "แก้เวลา booking ได้ไหม",
            "ต้องยกเลิกแล้วจองใหม่ใช่ไหม",
            "แนบสลิปเดิมตอนจองใหม่ได้ไหม",
        ],
        ["ยกเลิก", "1 ชั่วโมง", "จองใหม่", "สลิป"],
        ["Reservation"],
        variant_type="booking_edit",
    )
    add_many(
        "reservation",
        [
            "สิทธิ์การจองโอนให้เพื่อนได้ไหม",
            "ให้คนอื่นมาใช้ booking แทนได้ไหม",
            "transfer booking ได้ไหม",
            "จองแทนกันได้ไหม",
        ],
        ["ไม่สามารถโอนสิทธิ์"],
        ["Reservation"],
        variant_type="booking_transfer",
    )
    add_many(
        "reservation",
        [
            "เช็คอินล่วงหน้าได้กี่นาที",
            "check in ได้เร็วสุดกี่นาที",
            "เช็คอินก่อนเวลาได้ 1800 วินาทีไหม",
            "ต้องเช็คอินก่อนเริ่มรอบใช่ไหม",
        ],
        ["30 นาที"],
        ["Reservation"],
        variant_type="checkin_advance",
    )
    add(
        "reservation",
        "ถ้า check-in ไม่ทันจะโดนอะไร",
        ["ยกเลิก", "ไม่มีการคืนเงิน"],
        ["Reservation"],
        variant_type="checkin_late",
    )
    add_many(
        "reservation",
        [
            "เช็คอินต้องใช้บัตรอะไร",
            "แสดงบัตรประชาชนได้ไหมตอนเช็คอิน",
        ],
        ["บัตรประชาชน"],
        ["Reservation"],
        variant_type="checkin_id",
    )
    add_many(
        "reservation",
        [
            "ชำระเงินผ่านอะไร",
            "โอนเงินไปบัญชีไหน",
            "ชื่อบัญชีจ่ายค่าจองคืออะไร",
            "เลขบัญชีธนาคารสำหรับจองคืออะไร",
            "ธนาคารที่ใช้รับเงินคืออะไร",
        ],
        ["ธนาคารไทยพาณิชย์", "795-276244-1"],
        ["Reservation"],
        variant_type="payment_method",
    )


def build_games_equipment_cases() -> None:
    add("games", "PS5 มี Spider-Man 2 ไหม", ["PlayStation 5", "Spider-Man 2"], ["Reservation"], answer_type="fact", variant_type="game_ps5_specific")
    add("games", "เพลย์ห้ามี tekken 8 หรือเปล่า", ["PlayStation 5", "TEKKEN 8"], ["Reservation"], answer_type="fact", variant_type="game_ps5_specific")
    add("games", "เกมบน PlayStation มีอะไรบ้าง", ["PlayStation 5", "TEKKEN 8"], ["Reservation"], answer_type="list", variant_type="game_ps5_list")
    add("games", "PS5 เล่น Fortnite ได้ไหม", ["PlayStation 5", "Fortnite"], ["Reservation"], answer_type="fact", variant_type="game_ps5_specific")
    add("games", "มี God of War Ragnarok ไหม", ["PlayStation 5", "God of War Ragnarok"], ["Reservation"], answer_type="fact", variant_type="game_ps5_specific")
    add("games", "Switch มี Mario Kart ไหม", ["Nintendo Switch", "Mario Kart"], ["Reservation"], answer_type="list", variant_type="game_switch")
    add("games", "นินเทนโดมี Overcooked 2 ไหม", ["Nintendo Switch", "Overcooked 2"], ["Reservation"], answer_type="list", variant_type="game_switch")
    add("games", "เกม Nintendo มีอะไรบ้าง", ["Nintendo Switch", "Mario Kart"], ["Reservation"], answer_type="list", variant_type="game_switch")
    add("games", "เล่น Super Smash Bros ที่ศูนย์ได้ไหม", ["Nintendo Switch", "Super Smash"], ["Reservation"], answer_type="list", variant_type="game_switch")
    add("games", "Switch Sports มีไหม", ["Nintendo Switch", "Switch Sports"], ["Reservation"], answer_type="list", variant_type="game_switch")
    add("games", "PC มี valorant ไหม", ["PC", "VALORANT"], ["Reservation"], answer_type="list", variant_type="game_pc")
    add("games", "คอมเล่น CS2 ได้ไหม", ["PC", "Counter-Strike 2"], ["Reservation"], answer_type="list", variant_type="game_pc")
    add("games", "PC games list", ["PC", "VALORANT"], ["Reservation"], answer_type="list", variant_type="game_pc")
    add("games", "มี PUBG บน PC ไหม", ["PC", "PUBG"], ["Reservation"], answer_type="list", variant_type="game_pc")
    add("games", "Warzone อยู่เครื่อง PC ไหน", ["PC", "Warzone"], ["Reservation"], answer_type="list", variant_type="game_pc")
    add("games", "VR เล่นเกมอะไร", ["VR", "Beat Saber"], ["Reservation"], answer_type="list", variant_type="game_vr")
    add("games", "Beat Saber มีไหม", ["VR", "Beat Saber"], ["Reservation"], answer_type="fact", variant_type="game_vr")
    add("games", "แว่น VR มี Horizon ไหม", ["VR", "Horizon"], ["Reservation"], answer_type="fact", variant_type="game_vr")
    add("games", "Cockpit เล่นเกมอะไร", ["Cockpit", "Gran Turismo 7"], ["Reservation"], answer_type="fact", variant_type="game_cockpit")
    add("games", "พวงมาลัยใช้เล่น Gran Turismo ใช่ไหม", ["Gran Turismo 7"], ["Reservation"], answer_type="fact", variant_type="game_cockpit")
    add("equipment", "PC Zone มีอุปกรณ์อะไรบ้าง", ["Gaming PC", "Gaming Monitor", "Gaming Chair"], ["home"], answer_type="list", variant_type="equipment_pc")
    add("equipment", "คอมที่ศูนย์มีทั้งหมดกี่เครื่อง", ["Gaming PC", "10 Units"], ["home"], answer_type="fact", variant_type="equipment_pc")
    add("equipment", "Gaming PC รุ่นอะไร", ["MSI MAG Infinite S3", "10 Units"], ["home"], answer_type="fact", variant_type="equipment_pc")
    add("equipment", "เก้าอี้เกมมิ่งมีไหมใน PC zone", ["Gaming Chair", "10 Units"], ["home"], answer_type="fact", variant_type="equipment_pc")
    add("equipment", "เมาส์กับหูฟังมีให้ไหม", ["Gaming Mouse", "Gaming Headset"], ["home"], answer_type="fact", variant_type="equipment_pc")
    add_many(
        "equipment",
        [
            "Cockpit zone มีทีวีขนาดกี่นิ้ว",
            "พวงมาลัยใช้รุ่นอะไร",
            "Nintendo zone มีทีวีกี่นิ้ว",
            "PS5 zone มีเครื่องกี่เครื่อง",
            "VR zone ใช้แว่นรุ่นอะไร",
        ],
        ["Units"],
        ["home"],
        answer_type="fact",
        variant_type="equipment_zone",
    )


def build_rules_cases() -> None:
    add("rules", "เอาขนมเข้าไปกินตรงโต๊ะได้ไหม", ["เฉพาะ", "พื้นที่ที่กำหนด"], ["Reservation"], answer_type="fact", variant_type="food_drink_rule")
    add("rules", "กินน้ำในพื้นที่เล่นได้ไหม", ["เฉพาะ", "พื้นที่ที่กำหนด"], ["Reservation"], answer_type="fact", variant_type="food_drink_rule")
    add("rules", "ต้องฝากกระเป๋าก่อนไหม", ["ฝากสัมภาระ"], ["Reservation"], answer_type="fact", variant_type="belongings_rule")
    add("rules", "ใช้เสียงดังได้ไหม", ["งด", "เสียงดัง"], ["Reservation"], answer_type="fact", variant_type="noise_rule")
    add("rules", "พูดจาเสียดสีคนอื่นได้ไหม", ["ห้าม", "เสียดสี"], ["Reservation"], answer_type="fact", variant_type="noise_rule")
    add("rules", "ทิ้งขยะไว้ในโซนเล่นได้ไหม", ["ห้าม", "ทิ้งขยะ"], ["Reservation"], answer_type="fact", variant_type="trash_rule")
    add_many(
        "rules",
        [
            "สูบบุหรี่ในศูนย์ได้ไหม",
            "เอาแอลกอฮอล์เข้าได้ไหม",
            "พกมีดเข้าไปได้ไหม",
            "เล่นพนันในห้องได้ไหม",
            "เอาปลั๊กไฟส่วนตัวมาใช้ได้ไหม",
            "ย้ายอุปกรณ์เองได้ไหม",
        ],
        ["ห้าม"],
        ["Reservation"],
        answer_type="fact",
        variant_type="prohibited",
    )
    add("penalty", "ทำอุปกรณ์เสียหายต้องจ่ายไหม", ["รับผิดชอบ", "ค่าปรับ"], ["Reservation"], answer_type="fact", variant_type="damage_responsibility")
    add_many(
        "penalty",
        [
            "รอยขีดข่วนเล็กน้อยโดนปรับเท่าไหร่",
            "เบาะขาดต้องจ่ายกี่บาท",
            "หูฟังสายขาดค่าปรับเท่าไหร่",
        ],
        ["บาท"],
        ["Reservation"],
        answer_type="fact",
        variant_type="damage_fine",
    )
    add_many(
        "penalty",
        [
            "จอแตกต้องชดเชยยังไง",
            "คอมพังต้องจ่ายเต็มไหม",
        ],
        ["ชดเชย", "เต็มจำนวน"],
        ["Reservation"],
        answer_type="fact",
        variant_type="damage_severe",
    )
    add("penalty", "ละเมิดกฎจะโดนระงับสิทธิ์กี่วัน", ["ระงับสิทธิ์"], ["Reservation"], answer_type="fact", variant_type="penalty")
    add("penalty", "โดนแบนชั่วคราวกี่วัน", ["ระงับสิทธิ์", "1-7 วัน"], ["Reservation"], answer_type="fact", variant_type="penalty_temp")
    add("penalty", "กรณีไหนแบนถาวร", ["ระงับสิทธิ์", "ถาวร"], ["Reservation"], answer_type="fact", variant_type="penalty_permanent")
    add("penalty", "อุทธรณ์การลงโทษได้ภายในกี่วัน", ["7 วัน"], ["Reservation"], answer_type="fact", variant_type="penalty_appeal")
    add("penalty", "ศูนย์เก็บประวัติคนทำผิดไหม", ["บันทึก", "ประวัติ"], ["Reservation"], answer_type="fact", variant_type="penalty_record")


def build_info_cases() -> None:
    add_many(
        "overview",
        [
            "ศูนย์นี้คืออะไรแบบสั้นๆ",
            "PSU Esports Studio Phuket คืออะไร",
            "ใครเป็นคนก่อตั้งศูนย์นี้",
            "หน่วยงานที่ดำเนินการคือใคร",
            "mission ของศูนย์คืออะไร",
        ],
        ["มหาวิทยาลัยสงขลานครินทร์", "วิทยาลัยการคอมพิวเตอร์"],
        ["home"],
        answer_type="summary",
        variant_type="overview",
    )
    add_many(
        "contact",
        [
            "ศูนย์อยู่ตรงไหน",
            "ที่ตั้งของ studio คือที่ไหน",
            "ขอ email ติดต่อ",
            "Facebook ศูนย์ชื่ออะไร",
            "เบอร์โทรระบบจองมีเบอร์อะไร",
        ],
        ["PSU"],
        ["Contact"],
        answer_type="fact",
        variant_type="contact",
    )
    add("knowledge", "อีสปอร์ตคืออะไรแบบเข้าใจง่าย", ["อีสปอร์ต"], ["Knowledge"], answer_type="summary", variant_type="knowledge_definition")
    add("knowledge", "esports เริ่มครั้งแรกที่ไหน", ["Stanford", "1972"], ["Knowledge"], answer_type="summary", variant_type="knowledge_origin")
    add("knowledge", "Spacewar เกี่ยวกับประวัติอีสปอร์ตยังไง", ["Spacewar", "1972"], ["Knowledge"], answer_type="summary", variant_type="knowledge_origin")
    add("knowledge", "เกมประเภท MOBA คืออะไร", ["MOBA"], ["Knowledge"], answer_type="summary", variant_type="knowledge_moba")
    add("knowledge", "อาชีพในวงการ esports มีอะไรบ้าง", ["อีสปอร์ต"], ["Knowledge"], answer_type="summary", variant_type="knowledge_career")
    add("knowledge", "Overcooked 2 ฝึกทักษะอะไร", ["การทำงานเป็นทีม", "สื่อสาร"], ["Knowledge"], answer_type="summary", variant_type="knowledge_game_skill")
    add("knowledge", "Mario Kart 8 Deluxe ฝึกอะไร", ["ไหวพริบ", "การตัดสินใจ"], ["Knowledge"], answer_type="summary", variant_type="knowledge_game_skill")
    add_many(
        "events_news",
        [
            "วันที่ 25 เมษายน 2569 แข่งเกมอะไร",
            "VALORANT 2026 จัดวันไหน",
            "SURAT SMASH ส่งตัวแทนกี่คน",
            "นักศึกษาชาวจีนมีกี่คน",
            "GAME ON เปิดโลกอีสปอร์ตจัดให้ใคร",
        ],
        ["PSU"],
        ["News"],
        answer_type="fact",
        variant_type="news",
    )
    add_many(
        "about_us",
        [
            "อธิการบดีในหน้าสมาชิกคือใคร",
            "คณบดีวิทยาลัยการคอมพิวเตอร์คือใคร",
            "ผู้จัดการศูนย์คือใคร",
            "ประธาน PSU Phuket Esports Club คือใคร",
            "Gallery มีหมวดภาพอะไร",
        ],
        ["PSU"],
        ["Members"],
        answer_type="fact",
        variant_type="about",
    )


def build_no_answer_cases() -> None:
    add_many(
        "no_answer",
        [
            "มีบริการซ่อมคอมส่วนตัวไหม",
            "ส่งอาหารถึงโต๊ะเกมได้ไหม",
            "เอาแมวเข้าได้ไหม",
            "สมัครสมาชิกรายปีราคาเท่าไหร่",
            "เช่าโน้ตบุ๊กกลับบ้านได้ไหม",
            "มีห้องนอนพักค้างคืนไหม",
            "ขายคีย์บอร์ดเกมมิ่งไหม",
            "รับซ่อมจอย PS5 ไหม",
            "มีบริการส่งเครื่องเกมไปบ้านไหม",
            "ซื้อเกม Steam ผ่านศูนย์ได้ไหม",
            "มีคอร์สสอนเล่น Valorant ส่วนตัวไหม",
            "จ่ายด้วยคริปโตได้ไหม",
            "ผ่อนชำระค่าเล่นได้ไหม",
            "มีส่วนลดวันเกิดไหม",
            "จองแบบเหมาทั้งวันได้ไหม",
            "เอาเครื่อง PC ตัวเองมาตั้งได้ไหม",
            "มีบริการถ่ายรูปโปรไฟล์เกมเมอร์ไหม",
            "มีอาหารบุฟเฟต์ไหม",
            "รับจัดงานแต่งในศูนย์ไหม",
        ],
        ["ไม่พบข้อมูล"],
        [],
        answer_type="no_answer",
        difficulty="hard",
        variant_type="unknown_or_out_of_scope",
    )


def build_mixed_cases() -> None:
    add("reservation", "ถ้าจองแล้วไม่จ่ายใน 10 นาที แล้วไปเช็คอินช้าจะเกิดอะไรบ้าง", ["10 นาที", "ยกเลิก", "ไม่มีการคืนเงิน"], ["Reservation"], answer_type="multi_fact", difficulty="hard", variant_type="mixed_reservation")
    add("reservation", "ช่วยบอกทั้งจองล่วงหน้า เช็คอิน และยกเลิกแบบสั้นๆ", ["1 ชั่วโมง", "30 นาที", "ยกเลิก"], ["Reservation"], answer_type="multi_fact", difficulty="hard", variant_type="mixed_reservation")
    add("reservation", "จอง 1 ครั้งได้กี่ session แล้วต้องจ่ายภายในกี่นาที", ["3 Sessions", "10 นาที"], ["Reservation"], answer_type="multi_fact", difficulty="hard", variant_type="mixed_reservation")
    add("reservation", "กรอกข้อมูลอะไรบ้าง แล้วต้องแนบสลิปไหม", ["สลิป", "โอนเงิน"], ["Reservation"], answer_type="multi_fact", difficulty="hard", variant_type="mixed_reservation")
    add("reservation", "ถ้าจองผิดเวลา ต้องแก้ยังไงและต้องแจ้งก่อนกี่ชั่วโมง", ["1 ชั่วโมง"], ["Reservation"], answer_type="multi_fact", difficulty="hard", variant_type="mixed_reservation")
    add_many(
        "service_fee",
        [
            "นักเรียน มอ เล่น PS5 แล้วต่อด้วย VR 30 นาที ค่าใช้จ่ายเป็นยังไง",
            "คนนอกเล่น Switch 3-4 คนกับ Cockpit ราคาอะไรแพงกว่า",
            "General Student เล่น PS5 กับ Nintendo 1-2 ราคาเท่ากันไหม",
            "ถ้าเป็น PSU staff เล่น VR 1 ชั่วโมงต้องจ่ายไหม",
            "ต่างมหาลัยเล่น VR 30 นาที กับ VR 1 ชั่วโมงต่างกันเท่าไหร่",
        ],
        ["บาท"],
        ["service_fee"],
        answer_type="calculation",
        difficulty="hard",
        variant_type="mixed_price",
    )
    add("rules", "ถ้ากินข้าวเสียงดังแล้วทำจอยพัง จะเกี่ยวกับกฎไหนบ้าง", ["เฉพาะ", "เสียงดัง"], ["Reservation"], answer_type="multi_fact", difficulty="hard", variant_type="mixed_rules")
    add("rules", "ถ้าของหายกับทำอุปกรณ์เปียก ศูนย์รับผิดชอบไหม", ["ไม่รับผิดชอบ", "รับผิดชอบ"], ["Reservation"], answer_type="multi_fact", difficulty="hard", variant_type="mixed_rules")
    add("rules", "ถ้าสูบบุหรี่และเล่นพนันในศูนย์ผิดกฎไหม", ["ห้าม"], ["Reservation"], answer_type="multi_fact", difficulty="hard", variant_type="mixed_rules")
    add("rules", "ถ้ายืมแผ่นเกมแล้วไม่คืน หลังใช้งานต้องทำยังไง", ["คืน", "หลังจากใช้งานเสร็จ"], ["Reservation"], answer_type="multi_fact", difficulty="hard", variant_type="mixed_rules")
    add("rules", "ถ้าพบปัญหาเครื่องตอนเล่นควรแจ้งใคร", ["แจ้งเจ้าหน้าที่"], ["Reservation"], answer_type="multi_fact", difficulty="hard", variant_type="mixed_rules")


def main() -> None:
    build_schedule_cases()
    build_price_cases()
    build_booking_cases()
    build_games_equipment_cases()
    build_rules_cases()
    build_info_cases()
    build_no_answer_cases()
    build_mixed_cases()

    # Repeat selected categories with additional typo/casual variants until exactly 360 cases.
    filler = [
        ("reservation", "เปิดปิด วันจัน กีโมงอะ", ["13:00", "16:00", "Maintenance"], ["Reservation"], "typo_schedule"),
        ("service_fee", "เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท", ["0", "PlayStation 5"], ["service_fee"], "typo_price"),
        ("service_fee", "ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่", ["190", "VR"], ["service_fee"], "typo_price"),
        ("games", "คอมมีวาโลไหม", ["VALORANT"], ["Reservation"], "typo_games"),
        ("reservation", "เชคอินก่อนกี่นาที", ["30 นาที"], ["Reservation"], "typo_checkin"),
        ("rules", "สูบบุหรี่ได้ปะ", ["ห้าม"], ["Reservation"], "casual_rules"),
        ("no_answer", "มีให้เช่าจอไปบ้านไหม", ["ไม่พบข้อมูล"], [], "unknown_or_out_of_scope"),
        ("contact", "ขอเฟสศูนย์หน่อย", ["facebook.com/psuesportsphuket"], ["Contact"], "casual_contact"),
    ]
    natural_suffixes = [
        "ตอบสั้นๆ",
        "ในเว็บบอกว่าไง",
        "ถามแทนเพื่อน",
        "แบบภาษาคนทั่วไป",
        "ขอสรุปเร็วๆ",
        "ถ้าจะไปวันนี้ต้องรู้ว่าไง",
        "เอาแบบไม่ยาว",
        "ช่วยเช็คจากข้อมูลให้หน่อย",
    ]
    idx = 0
    while len(rows) < 360:
        category, question, keywords, source, variant = filler[idx % len(filler)]
        add(
            category,
            f"{question} {natural_suffixes[(idx // len(filler)) % len(natural_suffixes)]}",
            keywords,
            source,
            answer_type="fact" if category != "no_answer" else "no_answer",
            difficulty="hard",
            variant_type=variant,
        )
        idx += 1

    if len(rows) != 360:
        raise RuntimeError(f"Expected 360 rows, got {len(rows)}")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    README_PATH.write_text(
        "\n".join(
            [
                "# Ground Truth v2",
                "",
                f"- File: `{OUTPUT_PATH.name}`",
                "- Total: 360 cases",
                "- Focus: typo, casual Thai, Thai/English mixed, synonyms, multi-intent questions, price/service fee, schedule edge cases, and no-answer safety.",
                "- Evaluation note: this set is harder than `ground_truth_full.jsonl`; some cases intentionally test future improvements.",
                "",
                "Run example:",
                "",
                "```powershell",
                "py -3 scripts\\run_ground_truth_eval.py --ground-truth ground_truth\\ground_truth_v2_360.jsonl --label v2 --limit 40",
                "```",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(f"Wrote {len(rows)} rows to {OUTPUT_PATH}")
    print(f"Wrote README to {README_PATH}")


if __name__ == "__main__":
    main()
