from __future__ import annotations

import re

from app.core.normalization import CUSTOMER_GROUP_ALIASES, SERVICE_ALIASES, build_query_variants, detect_from_aliases, normalize_text
from app.pipeline.game_title_correction import build_game_title_query_variants
from app.pipeline.schemas import EntityBundle, PreprocessedInput


SHORT_ANSWER_TERMS = ("ตอบสั้น", "สั้นๆ", "สั้น ๆ", "brief", "short answer")
COMPARISON_TERMS = ("ต่างกัน", "แพงกว่า", "ถูกกว่า", "เท่ากันไหม", "เทียบ", "compare")


def _has(q: str, *terms: str) -> bool:
    return any(term in q for term in terms)


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


def _should_build_game_title_variants(query: str) -> bool:
    q = re.sub(r"\s+", " ", (query or "").lower()).strip()
    if not q:
        return False

    service_terms = (
        "ps5", "playstation", "เพลย์", "nintendo", "switch", "นินเทนโด", "สวิตช์", "สวิทช์",
        "cockpit", "ค็อกพิท", "คอกพิท", "พวงมาลัย", "vr", "วีอาร์", "แว่น", "pc", "คอม",
        "zone", "โซน",
    )
    price_terms = (
        "ราคา", "ค่าบริการ", "กี่บาท", "เท่าไหร่", "เท่าไร", "เสียเงิน", "ค่าใช้จ่าย",
        "fee", "price", "cost", "บาท",
    )
    equipment_terms = (
        "อุปกรณ์", "รุ่น", "สเปค", "สเป็ค", "spec", "กี่เครื่อง", "มีอะไรบ้าง",
    )
    known_equipment_terms = (
        "gaming pc", "msi mag infinite", "gaming monitor", "gaming keyboard", "gaming mouse",
        "gaming headset", "gaming chair", "logitech g923", "trueforce", "racing wheel",
        "driving force shifter", "gear shifter", "shifter", "racezone", "full cockpit",
        "pulse elite", "wireless headset", "nintendo switch oled", "switch oled",
        "playstation 5 slim", "ultra hd blu-ray", "playstation vr2", "psvr2", "vr2",
        "tv 65", "tv 86", "ทีวี 65", "ทีวี 86", "65 นิ้ว", "86 นิ้ว",
        "sofa 2", "sofa", "โซฟา",
    )
    game_catalog_terms = (
        "มีเกมอะไร", "เกมอะไร", "รายชื่อเกม", "เกมทั้งหมด", "กี่เกม", "เกมใน", "เกมบน",
    )
    game_detail_terms = (
        "ปุ่ม", "กด", "button", "buttons", "control", "controls",
        "กติกา", "แข่ง", "แข่งขัน", "ทัวร์", "tournament",
    )

    has_service = _has(q, *service_terms)
    if _has(q, *known_equipment_terms):
        return False
    if has_service and _has(q, *price_terms):
        return False
    if has_service and _has(q, *equipment_terms) and not _has(q, *game_detail_terms):
        return False
    if has_service and _has(q, *game_catalog_terms) and not _has(q, *game_detail_terms):
        return False
    return True


def preprocess_input(query: str) -> PreprocessedInput:
    raw = query or ""
    original_clean = re.sub(r"\s+", " ", raw).strip()
    game_variants = build_game_title_query_variants(original_clean) if _should_build_game_title_variants(original_clean) else ()
    clean = game_variants[0] if game_variants else original_clean

    variant_candidates: list[str] = [clean, original_clean]
    variant_candidates.extend(build_query_variants(original_clean))
    variant_candidates.extend(game_variants)
    variant_candidates.extend(build_query_variants(clean))
    variants: list[str] = []
    seen: set[str] = set()
    for candidate in variant_candidates:
        candidate_clean = re.sub(r"\s+", " ", str(candidate or "")).strip()
        key = candidate_clean.lower()
        if not candidate_clean or key in seen:
            continue
        seen.add(key)
        variants.append(candidate_clean)
        if len(variants) >= 8:
            break
    return PreprocessedInput(
        raw_query=raw,
        clean_query=clean,
        normalized_query=normalize_text(clean),
        language_hint=language_hint(clean),
        query_variants=tuple(variants),
    )


def _maybe_has_service_entity(q: str) -> bool:
    return _has(
        q,
        "ps5", "playstation", "เพลย์", "nintendo", "switch", "นินเทนโด", "สวิตช์", "สวิทช์",
        "cockpit", "ค็อกพิท", "คอกพิท", "ขับรถ", "พวงมาลัย", "racing",
        "vr", "วีอาร์", "แว่น", "pc", "คอม", "คอมพิวเตอร์",
    )


def _maybe_needs_service_detection(q: str) -> bool:
    if _maybe_has_service_entity(q):
        return True
    return _has(
        q,
        "ราคา", "ค่าบริการ", "กี่บาท", "เท่าไหร่", "เท่าไร", "เสียเงิน",
        "ค่าใช้จ่าย", "service fee", "price", "cost",
    )


def _maybe_needs_group_detection(q: str) -> bool:
    return _has(
        q,
        "นักศึกษา", "นักเรียน", "นิสิต", "เด็ก", "student", "staff", "บุคลากร",
        "psu", "สงขลานครินทร์", "บุคคลทั่วไป", "คนทั่วไป", "ผู้ใหญ่",
        "คนออก", "ประชาชน", "ต่างมหาลัย", "มหาลัย", "มหาวิทยาลัย", "สจล",
        "ลาดกระบัง", "จุฬา", "ธรรมศาสตร์", "เกษตร", "เชียงใหม่", "ขอนแก่น",
        "มหิดล", "ราชภัฏ", "ราชมงคล", "เทคนิค", "อาชีวะ", "kmitl", "chula",
        "tu", "ku", "cmu", "kku", "mahidol",
    )


def _without_style_phrases(q: str) -> str:
    for phrase in ("แบบภาษาคนทั่วไป", "ภาษาคนทั่วไป", "พูดแบบคนทั่วไป", "ตอบแบบคนทั่วไป"):
        q = q.replace(phrase, "")
    return q


def _has_specific_group_hint(q: str) -> bool:
    return _has(
        q,
        "มอ", "psu", "สงขลานครินทร์", "บุคลากร",
        "ต่างมหาลัย", "ต่างมหาวิทยาลัย", "ต่างสถาบัน", "ศิษย์เก่า",
        "สจล", "ลาดกระบัง", "จุฬา", "ธรรมศาสตร์", "เกษตร", "เชียงใหม่", "ขอนแก่น",
        "มหิดล", "ราชภัฏ", "ราชมงคล", "เทคนิค", "อาชีวะ",
        "kmitl", "chula", "tu", "ku", "cmu", "kku", "mahidol",
        "บุคคลทั่วไป", "คนทั่วไป", "ผู้ใหญ่", "general adult", "adult", "คนออก", "ประชาชน",
    )


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
    if _maybe_needs_service_detection(q):
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
    if user_group is None and _has(group_query, "นักเรียน", "นักศึกษา", "นิสิต", "เด็ก", "student") and not _has_specific_group_hint(group_query):
        group_match = {"key": "general_student"}
    else:
        group_match = (
            detect_from_aliases(group_query, CUSTOMER_GROUP_ALIASES)
            if _maybe_needs_group_detection(group_query)
            else {"key": None}
        )
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

    payment_deadline_intent = _has(q, "จ่ายภายใน", "ชำระภายใน", "โอนเงิน", "สลิป", "เลขบัญชี", "ธนาคาร", "ลืมจ่าย", "ไม่จ่าย", "หลังจองต้องจ่าย")
    price_intent = _has(q, "ราคา", "ค่าบริการ", "ค่าใช้จ่าย", "กี่บาท", "เท่าไหร่", "เท่าไร", "บาท", "เสียเงิน", "fee", "price", "cost")
    price_intent = price_intent or (_has(q, "ต้องจ่าย", "จ่ายไหม") and not payment_deadline_intent)
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
