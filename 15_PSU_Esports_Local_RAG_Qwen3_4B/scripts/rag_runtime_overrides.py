from __future__ import annotations

import re
from difflib import SequenceMatcher


SERVICE_SCHEDULE_QUERY_KEYWORDS = [
    "เปิดถึง",
    "เปิดกี่โมง",
    "ปิดถึงกี่โมง",
    "ปิดกี่โมง",
    "เปิดปิดกี่โมง",
    "เปิด-ปิดกี่โมง",
    "เวลาเปิด",
    "เวลาปิด",
    "เวลาทำการ",
    "เวลาให้บริการ",
    "ตารางบริการ",
    "รอบเช้า",
    "ช่วงเช้า",
    "ตอนเช้า",
    "รอบบ่าย",
    "ช่วงบ่าย",
    "24 ชั่วโมง",
    "เปิด 24",
    "service hours",
    "opening hours",
    "closing hours",
    "morning",
    "afternoon",
    "24 hours",
]

SERVICE_SCHEDULE_DOC_IDS = {
    "curated_schedule_morning",
    "curated_schedule_afternoon",
    "curated_reservation_schedule_monday_morning",
    "curated_reservation_schedule_friday_maintenance",
}

PRICE_QUERY_KEYWORDS = [
    "ราคา",
    "ค่าบริการ",
    "กี่บาท",
    "ต้องจ่าย",
    "จ่ายเท่าไหร่",
    "เสียเงิน",
    "เสียค่า",
    "ค่าเล่น",
    "ค่าใช้จ่าย",
    "เท่าไหร่",
    "ต่อชั่วโมง",
    "ต่อชม",
    "ต่อรอบ",
    "ฟรี",
    "service fee",
    "price",
    "cost",
    "fee",
    "free",
    "per hour",
    "hourly",
]

GAME_QUERY_KEYWORDS = ["เกม", "game", "เล่นอะไร", "มีอะไรให้เล่น"]

EQUIPMENT_QUERY_KEYWORDS = [
    "อุปกรณ์",
    "กี่เครื่อง",
    "รุ่นอะไร",
    "zone",
    "โซน",
    "จอหรือทีวี",
    "จออะไร",
    "ทีวี",
    "monitor",
    "chair",
    "keyboard",
    "headset",
    "mouse",
    "msi mag",
    "logitech",
    "racezone",
    "playstation vr2",
]

SERVICE_QUERY_KEYWORDS = [
    "กี่คน",
    "กี่นาที",
    "กี่ชั่วโมง",
    "รองรับ",
    "duration",
    "persons",
    "60 min",
    "30 min",
    "รอบ",
]

NEWS_QUERY_KEYWORDS = [
    "ข่าว",
    "จัดการแข่งขัน",
    "แข่งขัน",
    "tournament",
    "valorant 2026",
    "cs 2 2026",
    "surat smash",
    "game-based learning",
    "นักศึกษาชาวจีน",
    "game on",
    "เปิดโลกอีสปอร์ต",
    "วันที่ 25 เมษายน",
    "21 กุมภาพันธ์",
    "27 กุมภาพันธ์",
]

ABOUT_QUERY_KEYWORDS = [
    "สมาชิก",
    "คณบดี",
    "อธิการบดี",
    "ผู้จัดการ",
    "ประธาน",
    "gallery",
    "หน้าสมาชิก",
    "ใครเป็น",
]

KNOWLEDGE_QUERY_KEYWORDS = [
    "esports คืออะไร",
    "อีสปอร์ตคืออะไร",
    "อีสปอร์ตเกิด",
    "ประวัติของ esports",
    "ประเภทเกม",
    "ประเภทเกมที่นิยม",
    "เกมที่นิยมในปัจจุบัน",
    "อาชีพ",
    "ตามบทความ",
    "บทความ",
    "spacewar",
    "moba",
    "fps",
]

STUDIO_QUERY_KEYWORDS = [
    "psu esports studio",
    "psu esports studio phuket",
    "ศูนย์นี้",
    "ศูนย์อีสปอร์ต",
    "mission",
    "ก่อตั้ง",
    "ก่อตั้งโดย",
    "หน่วยงาน",
    "ดำเนินการ",
    "วิทยาลัยการคอมพิวเตอร์",
    "มหาวิทยาลัยสงขลานครินทร์",
]

PSU_REFERENCE_RE = re.compile(r"psu|p\.?s\.?u\.?|ม\.?\s*อ\.?|มหาวิทยาลัยสงขลานครินทร์", re.I)

PSU_STUDENT_WORDS = [
    "นักศึกษา",
    "นักเรียน",
    "เด็ก",
    "นิสิต",
    "student",
    "staff",
    "บุคลากร",
]

GENERAL_STUDENT_ALIAS_KEYWORDS = [
    "ศิษย์เก่า",
    "alumni",
    "general student",
    "นักศึกษาทั่วไป",
    "นักเรียนทั่วไป",
    "นักศึกษาต่าง",
    "นักเรียนต่าง",
    "นักศึกษาต่างมหาลัย",
    "นักเรียนต่างมหาลัย",
    "เด็กต่างมหาลัย",
    "นักศึกษาจาก",
    "นักเรียนจาก",
    "มหาวิทยาลัยอื่น",
    "มหาลัยอื่น",
    "ต่างมหาวิทยาลัย",
    "ต่างมหาลัย",
    "ต่างสถาบัน",
]

GENERAL_ADULT_ALIAS_KEYWORDS = [
    "บุคคลทั่วไป",
    "คนทั่วไป",
    "คนนอก",
    "ผู้ใหญ่ทั่วไป",
    "general adult",
    "adult",
]

SERVICE_ALIAS_GROUPS = [
    ("playstation 5 ps5 เพลย์สเตชั่น เพลย์ Playstation 5", ["ps5", "playstation", "เพลย์"]),
    ("nintendo switch นินเทนโด สวิตช์ switch", ["nintendo", "switch", "สวิตช์", "นินเทนโด"]),
    ("cockpit racing simulator พวงมาลัย ขับรถ", ["cockpit", "พวงมาลัย", "ขับรถ"]),
    ("vr virtual reality playstation vr2", ["vr", "virtual reality"]),
    ("pc gaming pc คอม คอมพิวเตอร์", ["pc", "gaming pc", "คอม", "คอมพิวเตอร์"]),
]

RESERVATION_PAYMENT_KEYWORDS = [
    "จ่ายภายใน",
    "ชำระภายใน",
    "หลังจองต้องจ่าย",
    "หลังจองต้องชำระ",
    "ลืมจ่าย",
    "ลืมชำระ",
    "payment timeout",
    "timeout",
]

RESERVATION_KEYWORDS = [
    "จอง",
    "booking",
    "reservation",
    "เช็คอิน",
    "เชคอิน",
    "check in",
    "check-in",
    "checkin",
    "ยกเลิก",
    "ชำระ",
    "โอน",
    "บัญชี",
    "สลิป",
    "กรอกข้อมูล",
]


def normalize_thai_digits(text: str) -> str:
    return (text or "").translate(str.maketrans("๐๑๒๓๔๕๖๗๘๙", "0123456789"))


def normalize_alias_text(text: str) -> str:
    q = normalize_thai_digits(text or "").lower()
    q = re.sub(r"p\s*\.?\s*s\s*\.?\s*u\.?", "psu", q)
    replacements = {
        "ม.อ.": "มอ",
        "ม.อ": "มอ",
        "ม. อ.": "มอ",
        "กีโมง": "กี่โมง",
        "เช็คอิน": "เชคอิน",
        "check-in": "checkin",
        "check in": "checkin",
        "ช.ม.": "ชม",
        "ชม.": "ชม",
        "ชั่วโมง": "ชม",
        "ชัวโมง": "ชม",
        "ครึ่งชั่วโมง": "ครึ่งชม",
        "ครึ่ง ชม": "ครึ่งชม",
        "เพลย์สเตชั่น": "playstation",
        "เพลสเตชั่น": "playstation",
        "เพลย์ห้า": "ps5",
        "เพลห้า": "ps5",
        "พีซี": "pc",
        "คอมพิวเตอร์": "คอม",
        "วีอาร์": "vr",
        "นินเทนโด": "nintendo",
    }
    for old, new in replacements.items():
        q = q.replace(old, new)
    q = re.sub(r"\bhrs?\b|\bhours?\b", "ชม", q)
    q = re.sub(r"\bmins?\b|\bminutes?\b", "นาที", q)
    return re.sub(r"[\s\._\-/()]+", "", q)


def fuzzy_contains_alias(normalized_query: str, normalized_alias: str, threshold: float = 0.88) -> bool:
    if not normalized_query or not normalized_alias:
        return False
    if normalized_alias in normalized_query:
        return True
    if len(normalized_alias) < 4 or len(normalized_query) < 4:
        return False
    min_len = max(4, len(normalized_alias) - 2)
    max_len = min(len(normalized_query), len(normalized_alias) + 2)
    for size in range(min_len, max_len + 1):
        for start in range(0, len(normalized_query) - size + 1):
            segment = normalized_query[start:start + size]
            if SequenceMatcher(None, segment, normalized_alias).ratio() >= threshold:
                return True
    return False


def alias_match(query: str, aliases: list[str] | tuple[str, ...] | set[str], threshold: float = 0.88) -> bool:
    nq = normalize_alias_text(query)
    # Retrieval expansion runs many times during ranking, so keep it deterministic and fast.
    # Fuzzy matching is reserved for the price calculator where the entity set is tiny and high value.
    return any((na := normalize_alias_text(alias)) and na in nq for alias in aliases)


def has_psu_reference(text: str) -> bool:
    return bool(PSU_REFERENCE_RE.search(text)) or alias_match(text, ["มอ", "ม.อ", "psu"], threshold=0.95)


def expand_query(query: str) -> str:
    """Add domain synonyms before embedding/search so Thai wording variants retrieve the same facts."""
    q = query.lower()
    additions: list[str] = []

    if has_psu_reference(q) and alias_match(q, PSU_STUDENT_WORDS, threshold=0.86):
        additions.append(
            "PSU Student and Staff นักศึกษา ม.อ. นักเรียน ม.อ. เด็ก ม.อ. "
            "นักศึกษา PSU บุคลากร PSU ฟรี 0 บาท"
        )
    if alias_match(q, GENERAL_STUDENT_ALIAS_KEYWORDS, threshold=0.86):
        additions.append(
            "PSU Alumni and General Student ศิษย์เก่า PSU นักศึกษาทั่วไป "
            "นักเรียนทั่วไป นักศึกษาต่างมหาวิทยาลัย นักศึกษาต่างมหาลัย ต่างมหาลัย general student"
        )
    if alias_match(q, GENERAL_ADULT_ALIAS_KEYWORDS, threshold=0.88):
        additions.append("General Adult บุคคลทั่วไป คนทั่วไป คนนอก adult")

    if alias_match(q, PRICE_QUERY_KEYWORDS + ["กีบาท", "กี่บาด", "เท่าไร", "เท่ารัย"], threshold=0.86):
        additions.append("service fee ค่าบริการ ราคา กี่บาท fee cost ต่อชั่วโมง ต่อรอบ")

    for canonical, variants in SERVICE_ALIAS_GROUPS:
        if alias_match(q, variants, threshold=0.9):
            additions.append(canonical)

    if not additions:
        return query
    return query + " " + " ".join(dict.fromkeys(additions))


def has_any(text: str, keywords: list[str] | tuple[str, ...] | set[str]) -> bool:
    return any(keyword in text for keyword in keywords)


def has_service_alias(text: str) -> bool:
    return any(alias_match(text, variants, threshold=0.9) for _canonical, variants in SERVICE_ALIAS_GROUPS)


def is_service_fee_query(query: str) -> bool:
    q = query.lower()
    if has_any(q, ["service fee", "ตารางราคา", "ตารางค่าบริการ", "เรทราคา", "ค่าบริการทั้งหมด", "ราคาทั้งหมด", "ค่าเล่นแต่ละ", "ค่าเล่นทั้งหมด", "ค่าใช้จ่าย"]):
        return True
    return has_service_alias(q) and alias_match(q, PRICE_QUERY_KEYWORDS + ["กีบาท", "กี่บาด", "เท่าไร", "เท่ารัย"], threshold=0.86)


def is_service_schedule_query(query: str) -> bool:
    q = expand_query(query).lower()
    return has_any(q, SERVICE_SCHEDULE_QUERY_KEYWORDS)


def route_category(query: str) -> str | None:
    raw_q = query.lower()
    q = expand_query(query).lower()

    if has_any(raw_q, RESERVATION_PAYMENT_KEYWORDS):
        return "reservation"
    if is_service_fee_query(raw_q):
        return "service_fee"
    if has_any(q, ["ค่าปรับ", "เสียหาย", "ชดเชย", "ระงับ", "อุทธรณ์", "ละเมิดกฎ", "damage", "fine", "penalty", "suspension"]):
        return "penalty"
    if is_service_schedule_query(query):
        return "reservation"
    if has_any(q, RESERVATION_KEYWORDS):
        return "reservation"
    if has_any(q, ["กฎ", "ห้าม", "rule", "regulation", "สูบบุหรี่", "แอลกอฮอล์", "การพนัน", "ฝากสัมภาระ", "ทิ้งขยะ", "แผ่นเกม", "ย้ายอุปกรณ์", "เคลื่อนย้าย", "ปลั๊กไฟ", "ทรัพย์สินส่วนตัว", "สูญหาย"]):
        return "rules"
    if has_any(q, ABOUT_QUERY_KEYWORDS):
        return "about_us"
    if has_any(q, KNOWLEDGE_QUERY_KEYWORDS):
        return "knowledge"
    if has_any(q, NEWS_QUERY_KEYWORDS):
        return "events_news"
    if has_any(q, STUDIO_QUERY_KEYWORDS) or ("คืออะไร" in q and has_any(q, ["psu", "studio", "ศูนย์"])):
        return "overview"
    if has_any(q, GAME_QUERY_KEYWORDS):
        return "games"
    if has_any(q, SERVICE_QUERY_KEYWORDS):
        return "services"
    if has_any(q, EQUIPMENT_QUERY_KEYWORDS):
        return "equipment"
    if has_any(q, ["ติดต่อ", "contact", "โทร", "email", "facebook", "ที่ตั้ง", "อยู่ที่ไหน"]):
        return "contact"
    return None


def tokenize_for_lexical(text: str) -> list[str]:
    return re.findall("[A-Za-z0-9_]+|[\u0E00-\u0E7F]+", text.lower())


def lexical_score(query: str, doc: str) -> float:
    terms = tokenize_for_lexical(expand_query(query))
    if not terms:
        return 0.0
    d = doc.lower()
    return sum(1 for term in terms if term in d) / len(terms)


def direct_curated_max_items(question: str, category: str) -> int:
    q = expand_query(question).lower()
    if category == "reservation" and is_service_schedule_query(question):
        return 2
    if category == "contact":
        return 4
    if category == "overview":
        return 2
    if category == "games":
        if has_any(q, ["ps5", "playstation", "switch", "nintendo", "pc", "vr", "cockpit"]):
            return 1
        return 4
    if category == "equipment":
        if has_any(q, ["มีอะไรบ้าง", "ทั้งหมด", "สรุป", "summary"]):
            return 3
        return 1
    if category == "services":
        if has_any(q, ["vr", "ps5", "playstation", "switch", "nintendo", "pc", "cockpit", "พวงมาลัย", "ขับรถ"]):
            return 1
        if has_any(q, ["มีอะไรบ้าง", "ทั้งหมด", "บริการ", "รอบ", "summary"]):
            return 3
        return 1
    if category == "service_fee":
        if has_any(q, ["มีอะไรบ้าง", "ทั้งหมด", "สรุป", "summary", "list", "ตาราง", "service fee"]):
            return 4
        return 1
    if category in {"events_news", "about_us", "knowledge"}:
        if has_any(q, ["มีอะไรบ้าง", "ทั้งหมด", "สรุป", "summary", "list"]):
            return 3
        return 1
    if category == "rules":
        if has_any(q, ["มีอะไรบ้าง", "ทั้งหมด", "สรุป", "summary"]):
            return 4
        return 1
    if category in {"reservation", "penalty"}:
        if has_any(q, ["มีอะไรบ้าง", "ทั้งหมด", "ขั้นตอน", "สรุป", "summary"]):
            return 4
        return 1
    return 1
