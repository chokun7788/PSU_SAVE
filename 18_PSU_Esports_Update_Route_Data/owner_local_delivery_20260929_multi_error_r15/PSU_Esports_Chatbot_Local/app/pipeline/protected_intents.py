from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date, timedelta

from app.calendar.service_calendar import regular_service_slots, today_bangkok
from app.core.normalization import normalize_text
from app.pipeline.service_policy_claims import get_service_policy_answer


RESERVATION_URL = "https://esports.computing.psu.ac.th/reservation"

_NONSEMANTIC_PREFACE = re.compile(
    r"^\s*(?:ขอถามเกี่ยวกับศูนย์หน่อยครับ|ช่วยอ้างอิงข้อมูลที่ยืนยันได้"
    r"|a question about the studio|before visiting,? i need to know"
    r"|please use verified studio information)\s*:\s*",
    flags=re.IGNORECASE,
)
_NONSEMANTIC_SUFFIX = re.compile(
    r"\s*(?:ตอบเฉพาะประเด็นที่ถามได้ไหม|please answer only that point)\s*[.!?ฯ]*\s*$",
    flags=re.IGNORECASE,
)


def strip_nonsemantic_preface(question: str) -> str:
    main = _NONSEMANTIC_PREFACE.sub("", question or "", count=1).strip()
    return _NONSEMANTIC_SUFFIX.sub("", main, count=1).strip()


@dataclass(frozen=True)
class ProtectedAnswer:
    operation: str
    category: str
    status: str
    answer: str
    source_id: str = ""
    source_url: str = ""
    basis: str = ""


def _has(text: str, *terms: str) -> bool:
    return any(term in text for term in terms)


def _asks_same_day_booking_policy(q: str) -> bool:
    """A policy question without a station and time is not a live slot check."""
    if re.search(r"\b\d{1,2}(?::\d{2})?\s*(?:โมง|am|pm)\b|\b\d{1,2}:\d{2}\b", q):
        return False
    if _has(q, "ว่าง", "ถูกจอง", "available", "availability", "booked"):
        return False
    return _has(q, "วันนี้จองได้ไหม", "จองวันนี้ได้ไหม", "เล่นวันนี้ได้ไหม", "วันนี้ยังจองได้ไหม") or bool(re.search(
        r"\b(?:can i|may i|is it possible to)\s+(?:book|reserve)\s+(?:for\s+)?today\b", q
    ))


def _tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z]+", text))


def is_weekly_booking_window_query(query: str) -> bool:
    q = normalize_text(query)
    tokens = _tokens(q)
    asks_booking = _has(q, "จอง", "รอบที่เปิด", "book", "booking", "reserve", "reservation")
    asks_weekly_period = _has(
        q, "วันไหน", "วันอะไร", "วันใด", "วันและเวลา", "ช่วงเวลาไหน", "ช่วงเวลาใด",
        "กี่โมง", "ช่วงไหน", "เปิดจอง", "ตาราง", "ตามปกติ", "รอบเช้า", "รอบบ่าย", "เสาร์", "อาทิตย์",
    ) or bool(tokens & {"days", "weekday", "weekdays", "hours", "weekends", "weekend", "schedule", "maintenance", "morning", "afternoon"}) or bool(re.search(
        r"\b(?:which|what)\s+day\b|\b(?:morning|afternoon)\s+(?:and|or)\s+(?:afternoon|morning)\b",
        q,
    ))
    asks_current_slot = _has(q, "ตอนนี้", "ขณะนี้", "เวลานี้", "วันนี้", "พรุ่งนี้", "right now", "currently", "today", "tomorrow")
    asks_current_slot = asks_current_slot or bool(re.search(r"\b\d{4}-\d{2}-\d{2}\b|\b\d{1,2}:\d{2}\b", q))
    # A named weekday is a concrete slot request only with an availability
    # predicate and a time; otherwise it asks about the regular schedule.
    asks_slot = _has(q, "ว่างไหม", "ว่างหรือเปล่า", "ถูกจอง", "slotว่าง", "slot available") or bool(re.search(
        r"\b(?:is|are|which)\b.{0,45}\b(?:free|booked|vacant|slot\s+available)\b",
        q,
    ))
    return asks_booking and asks_weekly_period and not (asks_slot and asks_current_slot)


def _weekly_schedule(locale: str) -> str:
    base = today_bangkok()
    monday = base - timedelta(days=base.weekday())
    grouped = [("Monday", "วันจันทร์", 0), ("Tuesday-Thursday", "วันอังคาร-พฤหัสบดี", 1), ("Friday", "วันศุกร์", 4)]
    lines = []
    for en_label, th_label, offset in grouped:
        slots = regular_service_slots(monday + timedelta(days=offset))
        open_periods = [slot["time_range"] for slot in slots if slot["state"] == "open"]
        maintenance_periods = [slot["time_range"] for slot in slots if slot["state"] == "maintenance"]
        if locale == "en":
            lines.append(f"- {en_label}: open {', '.join(open_periods)}; maintenance {', '.join(maintenance_periods)}" if maintenance_periods else f"- {en_label}: open {', '.join(open_periods)}")
        else:
            lines.append(f"- {th_label}: เปิด {', '.join(open_periods)}; Maintenance {', '.join(maintenance_periods)}" if maintenance_periods else f"- {th_label}: เปิด {', '.join(open_periods)}")
    if locale == "en":
        return "Regular booking/service periods (not live station availability):\n" + "\n".join(lines) + "\n- Weekend (Saturday-Sunday): no regular service or booking period is listed.\nSpecial closures override this weekly schedule. A bookable period does not confirm that a station is free."
    return "วันและช่วงเวลาให้บริการตามตารางปกติ (ไม่ใช่สถานะเครื่องว่างแบบสด):\n" + "\n".join(lines) + "\n- วันเสาร์-อาทิตย์: ไม่มีรอบให้บริการหรือจองตามตารางปกติ\nวันปิดพิเศษมีผลก่อนตารางปกติ และช่วงที่เปิดไม่ได้ยืนยันว่าเครื่องยังว่างครับ"


def _is_damage_policy(q: str) -> bool:
    tokens = _tokens(q)
    damage = _has(q, "เสียหาย", "ทำพัง", "ทำแตก", "จอแตก", "ของพัง", "ของศูนย์เสีย", "แว่น vr เสีย") or bool(re.search(r"(?:จอ|จอย|เครื่อง).{0,15}พัง|จอ.{0,10}แตก|\b(?:damag\w*|break\w*|brok\w*|drop\w*)\b", q))
    responsibility = _has(q, "ค่าปรับ", "ชดใช้", "ชดเชย", "รับผิดชอบ", "บทลงโทษ", "ค่าซ่อม", "ค่าเสียหาย", "ถ้า", "หาก", "ต้องจ่าย", "จ่ายไหม", "เกิดอะไรขึ้น", "ต้องแจ้งใคร") or bool(tokens & {"penalty", "fine", "compensation", "responsible", "responsibility", "policy", "happen", "happens", "if", "pay", "pays", "owe", "cost", "costs"})
    studio_target = _has(q, "อุปกรณ์", "จอย", "จอ", "คอม", "เมาส์", "เครื่อง", "ศูนย์", "ps5", "pc", "vr", "monitor", "controller", "headset", "studio", "equipment", "screen", "switch", "nintendo", "cockpit", "wheel", "mouse", "chair", "เก้าอี้", "แว่น")
    competition = _has(q, "กติกาการแข่ง", "กฎการแข่งขัน", "tournament", "competition rules", "match penalty")
    return damage and responsibility and studio_target and not competition


def is_damage_policy_query(query: str) -> bool:
    return _is_damage_policy(normalize_text(query))


def _asks_ps5_controller_model(q: str) -> bool:
    """Distinguish the controller hardware from a game's button mapping."""
    if not _has(q, "ps5", "playstation 5", "เพลย์ 5", "เพลย์ห้า", "เพล5"):
        return False
    if not _has(q, "จอย", "คอนโทรลเลอร์"):
        return False
    if not _has(q, "แบบไหน", "รุ่น", "ยี่ห้อ", "ประเภท", "ชนิด", "จอยอะไร"):
        return False
    return not _has(q, "ปุ่ม", "กด", "วิธีเล่น", "เล่นยังไง", "ควบคุม", "ซ่อม", "พัง", "เสีย", "ราคา", "กี่บาท")


def _food_facet(q: str) -> str:
    food = _has(q, "อาหาร", "ขนม", "เครื่องดื่ม", "น้ำดื่ม", "ขวดน้ำ", "น้ำเปล่า", "กาแฟ") or (_has(q, "ดื่ม", "กิน") and "น้ำ" in q) or bool(_tokens(q) & {"food", "snack", "snacks", "drink", "drinks", "water", "coffee", "beverage", "beverages", "hungry"}) or bool(re.search(r"\b(?:eat\w*|consum\w*)\b", q))
    if not food:
        return ""
    if (_has(q, "กิน", "รับประทาน", "ดื่ม") or bool(re.search(r"\b(?:eat|drink|consume)\b", q))) and (
        _has(q, "โต๊ะเกม", "โต๊ะเล่น", "โต๊ะคอม") or bool(re.search(r"\b(?:gaming\s+desk|game\s+desk)\b", q))
    ):
        return "food_consumption"
    bringing = _has(q, "นำ", "เอา", "พก", "หิ้ว", "เข้าไป", "เข้าอาคาร") or bool(re.search(r"\b(?:bring\w*|carry\w*|take)\b", q))
    if bringing:
        return "food_bring_permission"
    eating = _has(q, "กิน", "รับประทาน", "ดื่ม", "พื้นที่", "โต๊ะ") or bool(re.search(r"\b(?:eat\w*|consum\w*|drink\w*|allow\w*|permit\w*)\b", q))
    return "food_consumption" if eating else ""


def _is_public_access(q: str) -> bool:
    tokens = _tokens(q)
    public = _has(q, "บุคคลภายนอก", "คนภายนอก", "คนนอก", "คนทั่วไป", "บุคคลทั่วไป", "ผู้ปกครอง", "นักท่องเที่ยว", "ผู้มาเยือน", "แขกจาก", "มหาวิทยาลัยอื่น", "ต่างมหาวิทยาลัย", "ศิษย์เก่า", "ไม่ใช่สมาชิก", "ต้องเป็นสมาชิก", "ไม่มีรหัส psu", "ไม่มีบัตรนักศึกษา", "ไม่ใช่นักศึกษา psu") or bool(tokens & {"outsider", "outsiders", "visitor", "visitors", "guest", "guests", "membership", "parent", "tourist", "tourists", "alumni", "alumnus"}) or bool(re.search(r"\b(?:member|members)\s+of\s+the\s+public\b|\b(?:without|no)\s+(?:a\s+)?psu\s+id\b|\bgeneral\s+public\b|\b(?:non[- ]?students?|not\s+a\s+psu\s+student|only\s+psu\s+students?)\b", q))
    public = public or bool(re.search(r"ไม่(?:ได้|ใช่).{0,8}(?:เรียนที่นี่|เป็นนักศึกษา)", q))
    access = _has(q, "เข้า", "ใช้", "เล่น", "จอง", "อนุญาต", "สิทธิ์") or bool(re.search(r"\b(?:enter\w*|us(?:e|ing)|play\w*|book\w*|reserv\w*|access\w*|allow\w*|permit\w*|eligib\w*|open)\b", q))
    access = access or bool(re.search(r"\bwho\s+(?:can|may)\s+use\b", q))
    access = access or bool(re.search(r"\bfor\s+(?:the\s+)?(?:public\s+)?visitors?\s+or\s+students?\s+only\b", q))
    access = access or _has(q, "สมัครสมาชิก", "ต้องเป็นสมาชิก", "ใช้บัตรอะไร", "ต้องใช้เอกสารอะไร")
    access = access or bool(re.search(r"\b(?:need|require|have)\s+(?:a\s+)?(?:membership|national\s+id|student\s+id)\b", q))
    return public and access


def _has_price_signal(q: str) -> bool:
    return (
        _has(q, "ราคา", "ค่าบริการ", "ค่าใช้บริการ", "ค่าใช้จ่าย", "กี่บาท", "คิดเงิน", "เสียเงิน", "ต้องจ่าย", "ฟรี", "ไม่เสียเงิน")
        or "how much" in q
        or bool(_tokens(q) & {"price", "cost", "fee", "fees", "charge", "charges", "rate", "rates"})
        or bool(re.search(r"\b(?:pay|paying|paid)\s+(?:to\s+(?:play|use|enter|visit)|for\s+(?:using|playing|access))\b", q))
        or bool(re.search(r"\b(?:what|how\s+much)\b.{0,55}\b(?:pay|paying|paid)\b", q))
        or bool(re.search(r"\b(?:for\s+free|free\s+(?:of\s+charge|to\s+use))\b", q))
    )


def _asks_age_requirement(q: str) -> bool:
    age = _has(q, "อายุ", "กี่ขวบ", "เด็กกี่ขวบ") or bool(re.search(r"\b(?:age|ages|aged|years?\s+old|minimum\s+age|minor)\b", q))
    access = _has(q, "เข้าใช้", "ใช้บริการ", "เล่น", "จอง", "ศูนย์", "pc", "ps5", "vr", "nintendo", "cockpit") or bool(_tokens(q) & {"use", "play", "book", "visit", "studio", "equipment"})
    return age and access


def _asks_temporal_access(q: str) -> bool:
    if _has(q, "บัตร", "เอกสาร", "สมัครสมาชิก") or bool(_tokens(q) & {"id", "document", "documents", "membership"}):
        return False
    time_target = _has(q, "ตอนนี้", "วันนี้", "พรุ่งนี้", "มะรืน", "โมง", "ช่วงเช้า", "ช่วงบ่าย") or bool(re.search(r"\b(?:now|today|tomorrow|monday|tuesday|wednesday|thursday|friday|saturday|sunday|\d{1,2}:\d{2}|\d{4}-\d{2}-\d{2})\b", q))
    service_status = _has(q, "ว่าง", "เปิด", "ปิด", "เล่น", "ใช้") or bool(_tokens(q) & {"open", "closed", "available", "play", "use"})
    return time_target and service_status


def _asks_personal_power(q: str) -> bool:
    own_device = _has(q, "อุปกรณ์ส่วนตัว", "โน้ตบุ๊ก", "แล็ปท็อป", "โทรศัพท์", "laptop") or bool(re.search(r"\b(?:(?:my|own|personal|their)\s+)?(?:laptop|phone|mobile|charger)\b|\b(?:my|own|personal)\s+(?:device|computer)\b", q))
    power = _has(q, "ปลั๊ก", "เสียบไฟ", "ชาร์จ") or bool(re.search(r"\b(?:plug\s+in|charge|charging|power\s+outlet|socket)\b", q))
    return own_device and power


def _asks_alcohol(q: str) -> bool:
    return _has(q, "แอลกอฮอล์", "เหล้า", "เบียร์", "ไวน์") or bool(_tokens(q) & {"alcohol", "beer", "wine", "liquor"})


def _asks_open_eligibility(q: str) -> bool:
    return bool(re.search(r"ใคร.{0,18}(?:เข้าใช้ศูนย์|ใช้บริการศูนย์|ใช้อุปกรณ์ของศูนย์|มีสิทธิ์เข้าใช้บริการ)", q)) or bool(re.search(
        r"\b(?:who\s+(?:can|may|is\s+allowed\s+to)\s+(?:use|visit|enter)|can\s+anyone\s+use)\b.{0,28}\b(?:studio|center|equipment)\b", q
    ))


def _asks_offsite_equipment(q: str) -> bool:
    equipment = _has(q, "เครื่อง", "อุปกรณ์", "ps5", "pc", "vr", "nintendo", "จอย") or bool(_tokens(q) & {"equipment", "console", "ps5", "pc", "controller", "vr"})
    offsite = _has(q, "กลับบ้าน", "ออกนอกศูนย์", "เอาออกไป", "นำออกไป") or bool(re.search(r"\b(?:take|bring)\b.{0,35}\b(?:home|off[- ]?site|outside\s+the\s+studio)\b", q))
    return equipment and offsite


def _asks_all_games_entitlement(q: str) -> bool:
    return bool(re.search(r"(?:ทุกเกม|เกมทั้งหมด).{0,10}(?:เล่น|ใช้|ได้)|(?:เล่น|ใช้).{0,15}(?:ทุกเกม|เกมทั้งหมด)", q)) or bool(re.search(
        r"\b(?:play|access|use)\b.{0,25}\b(?:every|all)\s+(?:listed\s+)?games?\b", q
    ))


def _asks_visit_only_fee(q: str) -> bool:
    visit_only = _has(q, "ดูเฉยๆ", "ชมเฉยๆ", "แวะชม", "ไม่เล่น", "ไม่ใช้เครื่อง") or bool(re.search(r"\b(?:just\s+to\s+(?:look\s+around|visit|watch)|only\s+to\s+(?:look|visit)|without\s+using\s+equipment)\b", q))
    return visit_only and _has_price_signal(q)


def _payment_rule_id(q: str) -> str:
    method = _has(q, "จ่ายยังไง", "จ่ายอย่างไร", "วิธีชำระ", "วิธีจ่าย", "โอนเงิน", "เลขบัญชี") or bool(re.search(
        r"\b(?:how\s+(?:do|can)\s+(?:i|we)\s+pay|payment\s+method|bank\s+account)\b", q
    ))
    if method:
        return "rule_payment_bank"
    if _has(q, "ชำระเงินหลัง booking", "ชำระเงินหลังจอง", "หลังจองต้องชำระ"):
        return "rule_payment_10_minutes"
    return ""


def _studio_rule_topics(q: str) -> list[str]:
    topics = []
    if _has(q, "อาหาร", "เครื่องดื่ม") or bool(_tokens(q) & {"food", "drink", "drinks"}):
        topics.append("rule_food_drink")
    if _has(q, "เสียงดัง", "คำพูดไม่เหมาะสม", "ดูหมิ่น", "เสียดสี") or bool(_tokens(q) & {"noise", "offensive", "insult"}):
        topics.append("rule_noise_language")
    if _has(q, "อุปกรณ์เสียหาย", "ทำอุปกรณ์พัง") or bool(_tokens(q) & {"damage", "damaged"}):
        topics.append("rule_damage_responsibility")
    return topics


def _single_studio_rule(q: str) -> str:
    if _has(q, "ของหาย", "ทรัพย์สินส่วนตัวสูญหาย") and _has(q, "อุปกรณ์เสียหาย", "อุปกรณ์เปียก", "ทำอุปกรณ์พัง"):
        return "rule_mixed_lost_and_damage"
    if _has(q, "ทรัพย์สินส่วนตัว", "ของหาย") and _has(q, "สูญหาย", "หาย"):
        return "rule_lost_personal_items"
    if bool(re.search(r"\b(?:lost|missing)\b.{0,30}\b(?:belongings|property|items)\b", q)):
        return "rule_lost_personal_items"
    if _has(q, "คำพูดไม่เหมาะสม", "พูดจาดูหมิ่น", "เสียงดังเกิน") or bool(re.search(r"\b(?:offensive\s+language|insulting\s+speech)\b", q)):
        return "rule_noise_language"
    if (_has(q, "คืน", "นำมาคืน") and _has(q, "อุปกรณ์", "แผ่นเกม")) or bool(re.search(r"\breturn\b.{0,35}\b(?:equipment|game\s+discs?|games)\b", q)):
        return "rule_return_equipment_games"
    return ""


def _asks_checkin_required(q: str) -> bool:
    checkin = _has(q, "เช็กอิน", "เช็คอิน", "เชคอิน") or bool(re.search(r"\bcheck[- ]?in\b", q))
    required = _has(q, "ต้อง", "จำเป็น", "ไหม", "มั้ย") or bool(re.search(r"\b(?:need|must|have\s+to|required)\b", q))
    specific = _has(q, "ล่วงหน้ากี่", "เช็กอินช้า", "เช็คอินช้า", "ไม่เช็คอิน", "ไม่เช็กอิน") or bool(re.search(r"\b(?:how\s+early|late|miss)\b", q))
    return checkin and required and not specific


def _is_price_without_service(q: str, service: str | None) -> bool:
    if service:
        return False
    price = _has_price_signal(q)
    usage = _has(q, "เล่น", "ใช้", "เข้าศูนย์", "อุปกรณ์", "เครื่อง") or bool(_tokens(q) & {"play", "use", "enter", "access", "visit", "equipment", "studio", "service", "station", "rate", "rates"})
    return price and usage


def _is_explicitly_underspecified(q: str) -> bool:
    if _has(q, "เดาเอา", "ช่วยเดาหน่อยว่าอยากถาม", "บอกแค่ว่าเครื่อง", "เรื่องเกมมั้ง"):
        return True
    return bool(re.search(
        r"\b(?:guess\s+my\s+question|only\s+say\s+['\"]?station|games?\s+or\s+something\s+idk)\b",
        q,
    ))


def _is_unverified_advice_or_fabrication(q: str) -> bool:
    finance = _has(q, "หุ้น", "ลงทุน", "ซื้อกองทุน") or bool(_tokens(q) & {"stock", "stocks", "shares", "invest", "investment"})
    finance_request = _has(q, "แนะนำ", "ควรซื้อ", "ซื้ออะไร", "เลือกตัวไหน") or bool(_tokens(q) & {"recommend", "buy", "pick", "choose", "invest"})
    fabrication = _has(q, "เดาคำตอบ", "แต่งคำตอบ", "ตอบมั่ว", "สร้างข้อมูลขึ้นมา") or bool(re.search(
        r"\b(?:make up|invent|fabricate)\s+(?:an?\s+)?(?:answer|fact|source|policy)\b", q
    ))
    return (finance and finance_request) or fabrication


def _service_for_policy(service: str | None, english: bool) -> str:
    names = {
        "pc": ("บริการ PC Zone ", "a PC Zone station"),
        "ps5": ("บริการ PlayStation 5 ", "a PlayStation 5 station"),
        "nintendo": ("บริการ Nintendo Switch ", "a Nintendo Switch station"),
        "cockpit": ("บริการ Cockpit ", "a Cockpit station"),
        "vr": ("บริการ VR ", "a VR station"),
    }
    thai, english_name = names.get(service or "", ("บริการของศูนย์", "studio services"))
    return english_name if english else thai


def _policy_result(claim_id: str, *, locale: str, variant: str, service: str | None,
                   operation: str, category: str) -> ProtectedAnswer | None:
    try:
        claim = get_service_policy_answer(
            claim_id, locale=locale, variant=variant, service=_service_for_policy(service, locale == "en")
        )
    except (OSError, ValueError, KeyError, TypeError):
        return None
    if claim is None:
        return None
    source_label = "Source" if locale == "en" else "แหล่งข้อมูล"
    return ProtectedAnswer(
        operation, category, "answer", f"{claim.answer}\n{source_label}: {claim.source_url}",
        claim.source_id, claim.source_url, claim.basis,
    )


def answer_protected_intent(query: str, *, locale: str, service: str | None, rules: list[dict]) -> ProtectedAnswer | None:
    q = normalize_text(query)
    english = locale == "en"
    if _is_unverified_advice_or_fabrication(q):
        answer = (
            "I can answer questions about PSU Esports Studio - Phuket using verified sources, but I cannot recommend investments or invent studio facts. Please ask a question about the studio."
            if english else
            "ผมตอบเรื่อง PSU Esports Studio - Phuket จากข้อมูลที่ตรวจสอบได้ครับ ไม่แนะนำการลงทุนหรือแต่งข้อมูลของศูนย์ขึ้นเอง หากมีคำถามเกี่ยวกับศูนย์ พิมพ์ถามได้เลยครับ"
        )
        return ProtectedAnswer("unsupported_advice_or_fabrication", "no_answer", "no_answer", answer)
    if not english and _asks_ps5_controller_model(q):
        answer = (
            "ข้อมูลอุปกรณ์ที่บันทึกไว้ระบุเครื่อง PlayStation 5 Slim แต่ยังไม่ระบุรุ่นจอยที่ศูนย์จัดให้ "
            "จึงยังยืนยันรุ่นจอย PS5 ไม่ได้ครับ หากต้องการถามว่าปุ่มในเกมทำอะไร กรุณาระบุชื่อเกม"
        )
        url = "https://esports.phuket.psu.ac.th/home"
        return ProtectedAnswer(
            "ps5_controller_model_unverified", "equipment", "no_answer",
            f"{answer}\nแหล่งข้อมูล: {url}",
            "equipment_playstation_5_slim", url, "equipment_record_does_not_specify_controller_model",
        )
    if _asks_offsite_equipment(q):
        answer = (
            "The published reservation information covers use at the studio, not taking equipment home. I cannot confirm permission to remove this equipment; please ask staff before making plans."
            if english else
            "ข้อมูลการจองที่เผยแพร่เป็นการใช้บริการภายในศูนย์ ไม่ได้ยืนยันสิทธิ์ยืมอุปกรณ์กลับบ้านครับ กรุณาสอบถามเจ้าหน้าที่ก่อน"
        )
        return ProtectedAnswer("offsite_equipment_unverified", "no_answer", "no_answer",
                               f"{answer}\n{'Source' if english else 'แหล่งข้อมูล'}: {RESERVATION_URL}",
                               "reservation_on_site_scope", RESERVATION_URL, "site_explicit")
    if _asks_visit_only_fee(q):
        answer = (
            "The published fee table covers reservable services; it does not confirm whether a visit just to look around is free or has an entry fee. Please check with staff."
            if english else
            "ตารางค่าบริการที่เผยแพร่เป็นค่าบริการของโซนที่จองครับ ยังไม่พบข้อมูลยืนยันว่าการเข้าไปดูเฉย ๆ ฟรีหรือมีค่าเข้า กรุณาสอบถามเจ้าหน้าที่"
        )
        return ProtectedAnswer("visit_only_fee_unverified", "no_answer", "no_answer",
                               f"{answer}\n{'Source' if english else 'แหล่งข้อมูล'}: {RESERVATION_URL}",
                               "reservation_service_fee_scope", RESERVATION_URL, "site_explicit")
    if _asks_same_day_booking_policy(q):
        rule = next((row for row in rules if row.get("id") == "rule_booking_advance"), None)
        if rule:
            policy = str(rule.get("answer_en" if english else "answer_th") or "").strip()
            source = str(rule.get("source_url") or RESERVATION_URL)
            if policy:
                condition = (
                    "A booking for today is possible only if a suitable slot is still available and the one-hour advance rule can be met. This does not confirm live availability."
                    if english else
                    "การจองเพื่อใช้วันนี้ทำได้ต่อเมื่อยังมีรอบที่ต้องการว่างและจองทันเงื่อนไขล่วงหน้า 1 ชั่วโมง ข้อความนี้ยังไม่ได้ยืนยันว่ารอบใดว่างอยู่ครับ"
                )
                return ProtectedAnswer(
                    "booking_same_day_policy", "reservation", "answer",
                    f"{policy}\n{condition}\n{'Source' if english else 'แหล่งข้อมูล'}: {source}",
                    "rule_booking_advance", source, "site_explicit",
                )
    payment_rule_id = _payment_rule_id(q)
    if payment_rule_id:
        rule = next((row for row in rules if row.get("id") == payment_rule_id), None)
        if rule:
            answer = str(rule.get("answer_en" if english else "answer_th") or "").strip()
            url = str(rule.get("source_url") or RESERVATION_URL)
            if answer:
                return ProtectedAnswer("payment_method" if payment_rule_id == "rule_payment_bank" else "payment_deadline",
                                       "reservation", "answer", f"{answer}\n{'Source' if english else 'แหล่งข้อมูล'}: {url}",
                                       payment_rule_id, url, "site_explicit")
    if _asks_checkin_required(q):
        policy = _policy_result("checkin_required", locale=locale, variant="general", service=None,
                                operation="checkin_required", category="reservation")
        if policy is not None:
            return policy
    if _asks_all_games_entitlement(q) and (_is_public_access(q) or _asks_open_eligibility(q)):
        answer = (
            "Public visitors can book studio services, but that does not establish access to every game. Game availability depends on the zone and published catalog; please name a game or zone to check."
            if english else
            "บุคคลทั่วไปจองใช้บริการได้ครับ แต่ยังยืนยันไม่ได้ว่าเล่นได้ทุกเกม เพราะรายการเกมแยกตามโซน ระบุเกมหรือโซนที่สนใจได้ครับ"
        )
        return ProtectedAnswer("all_games_scope_unverified", "no_answer", "no_answer",
                               f"{answer}\n{'Source' if english else 'แหล่งข้อมูล'}: {RESERVATION_URL}",
                               "public_access_not_game_entitlement", RESERVATION_URL, "reviewer_interpretation_with_site_context")
    if is_weekly_booking_window_query(q):
        return ProtectedAnswer(
            "booking_window", "schedule", "answer",
            _weekly_schedule(locale) + (f"\nSource: {RESERVATION_URL} (original source in Thai)" if english else f"\nแหล่งข้อมูล: {RESERVATION_URL}"),
            "service_schedule", RESERVATION_URL,
        )
    rule_topics = _studio_rule_topics(q)
    if len(rule_topics) >= 2 and _has(q, "กฎ", "นโยบาย", "สรุป", "policy", "rules"):
        selected = [next((row for row in rules if row.get("id") == rule_id), None) for rule_id in rule_topics]
        if all(selected):
            lines = [str(row.get("answer_en" if english else "answer_th") or "").strip() for row in selected]
            if all(lines):
                answer = "\n".join(f"- {line}" for line in lines)
                answer += f"\n{'Source' if english else 'แหล่งข้อมูล'}: {RESERVATION_URL}"
                return ProtectedAnswer("multi_studio_rules", "rules", "answer", answer,
                                       "studio_rules_4_2_4_5_4_6", RESERVATION_URL, "site_explicit")
    direct_rule_id = _single_studio_rule(q)
    if direct_rule_id:
        rule = next((row for row in rules if row.get("id") == direct_rule_id), None)
        if rule:
            answer = str(rule.get("answer_en" if english else "answer_th") or "").strip()
            url = str(rule.get("source_url") or RESERVATION_URL)
            if answer:
                answer += f"\n{'Source' if english else 'แหล่งข้อมูล'}: {url}"
                return ProtectedAnswer("studio_rule_direct", "rules", "answer", answer,
                                       direct_rule_id, url, "site_explicit")
    if _is_damage_policy(q):
        rule = next((row for row in rules if row.get("id") == "rule_damage_responsibility"), None)
        if rule:
            answer = str(rule.get("answer_en" if english else "answer_th") or "").strip()
            if answer:
                url = str(rule.get("source_url") or "")
                answer += (f"\nSource: {url} (original source in Thai)" if english else f"\nแหล่งข้อมูล: {url}")
                return ProtectedAnswer("damage_responsibility", "penalty", "answer", answer, str(rule.get("id")), url)
    if _has(q, "ระงับสิทธิ์ชั่วคราว", "แบนชั่วคราว", "temporary suspension"):
        rule = next((row for row in rules if row.get("id") == "rule_penalty_temp_suspension"), None)
        if rule:
            url = str(rule.get("source_url") or "")
            answer = str(rule.get("answer_en" if english else "answer_th") or "").strip()
            if answer:
                answer += (f"\nSource: {url} (original source in Thai)" if english else f"\nแหล่งข้อมูล: {url}")
                return ProtectedAnswer("temporary_suspension", "penalty", "answer", answer, str(rule.get("id")), url)
    if _asks_alcohol(q):
        rule = next((row for row in rules if row.get("id") == "rule_smoking_alcohol"), None)
        if rule:
            url = str(rule.get("source_url") or RESERVATION_URL)
            answer = str(rule.get("answer_en" if english else "answer_th") or "").strip()
            if answer:
                asks_bringing = _has(q, "นำ", "เอา", "พก", "หิ้ว") or bool(re.search(r"\b(?:bring|carry|take)\b", q))
                asks_drinking = _has(q, "ดื่ม") or bool(re.search(r"\b(?:drink|consume)\b", q))
                negated_drinking = _has(q, "ไม่ดื่ม") or bool(re.search(r"\b(?:not|without)\s+(?:drink|drinking|consuming)\b", q))
                if asks_bringing and (not asks_drinking or negated_drinking):
                    caveat = (
                        "The published rule does not separately confirm whether carrying alcohol inside is allowed. "
                        if english else
                        "กฎที่เผยแพร่ยังไม่ได้ระบุแยกว่าพกเครื่องดื่มแอลกอฮอล์เข้าไปได้หรือไม่ แต่"
                    )
                    answer = caveat + answer
                answer += f"\n{'Source' if english else 'แหล่งข้อมูล'}: {url}"
                return ProtectedAnswer("alcohol_rule", "rules", "answer", answer, str(rule.get("id")), url, "site_explicit")
    if _asks_personal_power(q):
        policy = _policy_result("personal_power", locale=locale, variant="general", service=None,
                                operation="personal_power", category="rules")
        if policy is not None:
            return policy
    food_facet = _food_facet(q)
    if food_facet == "food_bring_permission":
        policy = _policy_result("food_bring", locale=locale, variant="general", service=None,
                                operation="food_bring_permission", category="rules")
        if policy is not None:
            return policy
        rule = next((row for row in rules if row.get("id") == "rule_food_drink"), None)
        url = str((rule or {}).get("source_url") or RESERVATION_URL)
        answer = (
            "The verified rule only says food and drinks may be consumed in designated areas. It does not confirm whether you may bring them into the studio; please check with staff."
            if english else
            "ข้อมูลที่ยืนยันได้ระบุเพียงว่ารับประทานอาหารและเครื่องดื่มได้เฉพาะพื้นที่ที่กำหนด ยังยืนยันไม่ได้ว่าสามารถนำเข้าศูนย์ได้หรือไม่ กรุณาสอบถามเจ้าหน้าที่ครับ"
        )
        answer += f"\n{'Source' if english else 'แหล่งข้อมูล'}: {url}"
        return ProtectedAnswer(food_facet, "no_answer", "no_answer", answer, str((rule or {}).get("id") or ""), url)
    if food_facet == "food_consumption":
        rule = next((row for row in rules if row.get("id") == "rule_food_drink"), None)
        if rule:
            url = str(rule.get("source_url") or "")
            answer = str(rule.get("answer_en" if english else "answer_th") or "").strip()
            at_station = _has(q, "โต๊ะเกม", "โต๊ะเล่น", "โต๊ะคอม", "หน้า pc", "หน้าเครื่อง") or bool(re.search(r"\b(?:gaming|game|pc|ps5)\s+(?:desk|station)\b", q))
            if at_station:
                answer = (
                    "I cannot confirm that this gaming station is a designated eating or drinking area. "
                    if english else
                    "ยังยืนยันไม่ได้ว่าโต๊ะเล่นเกมเป็นพื้นที่รับประทานที่กำหนดครับ "
                ) + answer
            answer += (f"\nSource: {url} (original source in Thai)" if english else f"\nแหล่งข้อมูล: {url}")
            return ProtectedAnswer(food_facet, "rules", "answer", answer, str(rule.get("id")), url)
    if _asks_age_requirement(q):
        answer = (
            "The published studio rules do not specify a minimum age for this service. I cannot confirm eligibility from age alone; please check with the studio before booking."
            if english else
            "กฎการใช้บริการที่เผยแพร่ไม่ได้ระบุอายุขั้นต่ำสำหรับบริการนี้ครับ จึงยังยืนยันสิทธิ์จากอายุอย่างเดียวไม่ได้ กรุณาตรวจสอบกับศูนย์ก่อนจอง"
        )
        answer += f"\n{'Source' if english else 'แหล่งข้อมูล'}: {RESERVATION_URL}"
        return ProtectedAnswer("age_requirement_unverified", "no_answer", "no_answer", answer, "published_service_rules", RESERVATION_URL, "site_explicit")
    service_undecided = _has(q, "ยังไม่รู้โซน", "ไม่รู้โซน", "ไม่ระบุโซน", "ไม่แน่ใจโซน", "not sure which service", "not sure which zone")
    if _is_price_without_service(q, None if service_undecided else service):
        answer = (
            "Which service would you like the fee for: PC, PlayStation 5, Nintendo Switch, Cockpit, or VR? The rate depends on the service and user group."
            if english else
            "ต้องการทราบค่าบริการของ PC, PlayStation 5, Nintendo Switch, Cockpit หรือ VR ครับ? ราคาแตกต่างตามบริการและกลุ่มผู้ใช้ จึงยังระบุราคาเดียวไม่ได้ครับ"
        )
        return ProtectedAnswer("price_missing_service", "clarification", "clarification", answer)
    explicit_price = _has_price_signal(q)
    if not explicit_price and not _asks_temporal_access(q) and (_is_public_access(q) or _asks_open_eligibility(q) or _has(q, "มีข้อจำกัดว่าใครเข้าใช้", "who can use the studio equipment") or bool(re.search(r"\bwho\s+is\s+eligible\s+to\s+use\b", q))):
        documents = _has(q, "เอกสาร", "บัตร", "รหัสนักศึกษา", "student id", "national id") or bool(re.search(r"\b(?:what|which)\s+(?:id|documents?|identification)\b", q))
        membership = _has(q, "ต้องเป็นสมาชิก", "สมัครสมาชิก") or bool(re.search(r"\b(?:need|require|have)\s+(?:a\s+)?membership\b", q))
        booking = _has(q, "จอง") or bool(_tokens(q) & {"book", "booking", "reserve", "reservation"})
        without_booking = _has(q, "ไม่จอง", "ไม่ต้องจอง", "ไม่ได้จอง", "walk-in", "walk in") or bool(re.search(r"\bwithout\s+(?:a\s+)?(?:booking|reservation)\b", q))
        variant = "booking_required" if without_booking else "membership" if membership else "documents" if documents else "booking" if booking else "general"
        policy = _policy_result("public_access", locale=locale, variant=variant, service=service,
                                operation="public_access", category="reservation")
        if policy is not None:
            return policy
        answer = (
            "I cannot verify from the available policy whether members of the public may use this service. Please confirm the eligibility requirements with the studio; an equipment list does not establish permission."
            if english else
            "ข้อมูลที่มีอยู่ยังยืนยันสิทธิ์เข้าใช้บริการของบุคคลภายนอกสำหรับกรณีนี้ไม่ได้ครับ กรุณาตรวจสอบเงื่อนไขกับศูนย์โดยตรง รายการอุปกรณ์ไม่ได้ยืนยันสิทธิ์การใช้งานครับ"
        )
        return ProtectedAnswer("public_access", "no_answer", "no_answer", answer)
    if _is_explicitly_underspecified(q):
        answer = (
            "Which specific game, station, service, or rule do you mean? I cannot infer a missing target from this message."
            if english else
            "หมายถึงเกม เครื่อง บริการ หรือกฎเรื่องใดครับ? ข้อความนี้ยังไม่มีเป้าหมายพอให้ตอบโดยไม่เดาครับ"
        )
        return ProtectedAnswer("missing_target", "clarification", "clarification", answer)
    return None
