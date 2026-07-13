from __future__ import annotations

import re

from app.core.normalization import CUSTOMER_GROUP_ALIASES, SERVICE_ALIASES, build_query_variants, detect_from_aliases, normalize_text
from app.pipeline.schemas import EntityBundle, PreprocessedInput


SHORT_ANSWER_TERMS = ("ตอบสั้น", "สั้นๆ", "สั้น ๆ", "brief", "short answer")
COMPARISON_TERMS = ("ต่างกัน", "แพงกว่า", "ถูกกว่า", "เท่ากันไหม", "เทียบ", "compare")


def language_hint(text: str) -> str:
    thai_chars = sum(1 for ch in text if "\u0E00" <= ch <= "\u0E7F")
    latin_chars = sum(1 for ch in text if "a" <= ch.lower() <= "z")
    if thai_chars and latin_chars:
        return "mixed_th_en"
    if thai_chars:
        return "th"
    if latin_chars:
        return "en"
    return "unknown"


def preprocess_input(query: str) -> PreprocessedInput:
    raw = query or ""
    clean = re.sub(r"\s+", " ", raw).strip()
    return PreprocessedInput(
        raw_query=raw,
        clean_query=clean,
        normalized_query=normalize_text(clean),
        language_hint=language_hint(clean),
        query_variants=build_query_variants(clean),
    )


def _has(q: str, *terms: str) -> bool:
    return any(term in q for term in terms)


def _without_style_phrases(q: str) -> str:
    for phrase in ("แบบภาษาคนทั่วไป", "ภาษาคนทั่วไป", "พูดแบบคนทั่วไป", "ตอบแบบคนทั่วไป"):
        q = q.replace(phrase, "")
    return q


def extract_entities(pre: PreprocessedInput) -> EntityBundle:
    q = pre.normalized_query

    day = None
    if _has(q, "วันจัน", "จันทร์", "monday", "mon"):
        day = "monday"
    elif _has(q, "ศุกร์", "friday", "fri"):
        day = "friday"
    elif _has(q, "อังคาร", "tuesday", "tue"):
        day = "tuesday"
    elif _has(q, "พุธ", "wednesday", "wed"):
        day = "wednesday"
    elif _has(q, "พฤหัส", "thursday", "thu"):
        day = "thursday"

    slots: list[str] = []
    if _has(q, "morning", "รอบเช้า", "ช่วงเช้า", "ตอนเช้า", "09:00", "9:00"):
        slots.append("morning")
    if _has(q, "afternoon", "รอบบ่าย", "ช่วงบ่าย", "ตอนบ่าย", "13:00"):
        slots.append("afternoon")

    service = None
    service_match = detect_from_aliases(q, SERVICE_ALIASES)
    if service_match["key"] is not None:
        service = service_match["key"]

    user_group = None
    group_query = _without_style_phrases(q)
    if _has(
        group_query,
        "นักศึกษา มอ", "นักเรียน มอ", "เด็ก มอ", "นิสิต มอ",
        "นักศึกษา psu", "นักเรียน psu", "เด็ก psu", "psu student", "psu staff",
        "บุคลากร psu", "บุคลากร มอ", "มหาวิทยาลัยสงขลานครินทร์", "สงขลานครินทร์",
    ):
        user_group = "psu"
    group_match = detect_from_aliases(group_query, CUSTOMER_GROUP_ALIASES)
    if user_group is None and group_match["key"] == "psu_student_staff":
        user_group = "psu"
    elif user_group is None and group_match["key"] == "general_student":
        user_group = "general_student"
    elif user_group is None and group_match["key"] == "general_adult":
        user_group = "adult"
    elif user_group is None and _has(group_query, "นักเรียน", "นักศึกษา", "นิสิต", "เด็ก", "student"):
        user_group = "general_student"

    duration = None
    if _has(q, "30 นาที", "ครึ่ง", "ครึ่งชม", "ครึ่งชั่วโมง"):
        duration = "30_minutes"
    elif _has(q, "1 ชั่วโมง", "หนึ่งชั่วโมง", "60 นาที", "1 ชม"):
        duration = "60_minutes"

    price_intent = _has(q, "ราคา", "ค่าบริการ", "ค่าใช้จ่าย", "กี่บาท", "เท่าไหร่", "เท่าไร", "บาท", "ต้องจ่าย", "เสียเงิน", "fee", "price", "cost")
    comparison_intent = _has(q, *COMPARISON_TERMS)
    short_answer = _has(q, *SHORT_ANSWER_TERMS)

    return EntityBundle(
        day=day,
        time_slots=tuple(slots),
        service=service,
        user_group=user_group,
        duration=duration,
        price_intent=price_intent,
        short_answer=short_answer,
        comparison_intent=comparison_intent,
        raw={
            "normalized_query": q,
            "language_hint": pre.language_hint,
        },
    )
