from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date

from app.core.normalization import normalize_text


_PRICE_AMOUNT_TERMS = (
    "ราคา",
    "ค่าบริการ",
    "ค่าใช้จ่าย",
    "กี่บาท",
    "เท่าไหร่",
    "เท่าไร",
    "บาท",
    "เสียเงิน",
    "เสียกี่บาท",
    "เสียค่า",
    "ต้องจ่าย",
    "จ่ายเท่า",
    "คิดเงิน",
    "คำนวณราคา",
    "service fee",
    "price",
    "cost",
    "fee",
)

_DEFINITION_TERMS = (
    "คืออะไร",
    "หมายถึงอะไร",
    "แปลว่าอะไร",
    "อธิบาย",
    "คำจำกัดความ",
    "ต่างกันยังไง",
    "ต่างกันอย่างไร",
    "เปรียบเทียบ",
)

_PSU_INVENTORY_TERMS = (
    "psu",
    "สงขลานครินทร์",
    "esports studio",
    "อีสปอร์ตสตูดิโอ",
    "ที่ศูนย์",
    "ของศูนย์",
    "ในศูนย์",
    "ที่ร้าน",
    "ของร้าน",
    "ที่นี่",
    "มีรุ่นอะไร",
    "ใช้รุ่นอะไร",
    "มีไหม",
    "มีหรือเปล่า",
    "อยู่โซนไหน",
    "อยู่ที่ไหน",
    "กี่เครื่อง",
    "จำนวนกี่",
    "อุปกรณ์ใน",
)

_GENERAL_CONCEPT_TERMS = (
    "mechanical keyboard",
    "คีย์บอร์ด mechanical",
    "mechanical คีย์บอร์ด",
    "คีย์บอร์ดแมคคานิคอล",
    "แมคคานิคอลคีย์บอร์ด",
    "เมคานิคอลคีย์บอร์ด",
)

_GAME_ZONE_RANKING_TERMS = (
    "เกมเยอะสุด",
    "เกมเยอะที่สุด",
    "เกมมากสุด",
    "เกมมากที่สุด",
    "เกมน้อยสุด",
    "เกมน้อยที่สุด",
    "เกมเยอะกว่า",
    "จำนวนเกมตามโซน",
    "เกมกี่เกมแต่ละโซน",
    "จัดอันดับจำนวนเกม",
    "เรียงจำนวนเกม",
)

_RANKING_OPERATION_TERMS = (
    "เยอะสุด",
    "เยอะที่สุด",
    "มากสุด",
    "มากที่สุด",
    "น้อยสุด",
    "น้อยที่สุด",
    "เยอะกว่า",
    "มากกว่า",
    "อันดับ",
    "จัดอันดับ",
    "เรียง",
)

_RANKING_TARGET_TERMS = (
    "อุปกรณ์",
    "เครื่อง",
    "โซน",
    "zone",
    "บริการ",
    "ที่ไหน",
    "ไหน",
)

_GENERAL_CREATION_TERMS = (
    "ช่วยเขียน",
    "เขียนประโยค",
    "ช่วยแต่ง",
    "แต่งประโยค",
    "ช่วยร่าง",
    "ร่างข้อความ",
    "ช่วยคิดข้อความ",
    "แคปชั่น",
    "caption",
    "คำโปรย",
)

_GENERAL_TRANSLATION_TERMS = (
    "แปลคำว่า",
    "ช่วยแปล",
    "แปลเป็นภาษา",
    "แปลเป็นไทย",
    "แปลเป็นภาษาไทย",
    "translate",
)

_DYNAMIC_FRESHNESS_TERMS = (
    "ล่าสุด",
    "ตอนนี้",
    "ปัจจุบัน",
    "วันนี้",
    "สัปดาห์นี้",
    "เดือนนี้",
    "ปีนี้",
    "ขณะนี้",
    "ล่าสุดวันนี้",
    "current",
    "latest",
    "today",
    "right now",
)

_DYNAMIC_TOPIC_TERMS = (
    "ข่าว",
    "เพลง",
    "เพลงฮิต",
    "ชาร์ตเพลง",
    "เทรนด์",
    "กระแส",
    "หนังเข้าใหม่",
    "หนังน่าดู",
    "นายก",
    "ประธานาธิบดี",
    "รัฐมนตรี",
    "ผู้บริหาร",
    "ceo",
    "คะแนน",
    "ผลแข่ง",
    "ผลบอล",
    "ตารางแข่ง",
    "ราคาหุ้น",
    "ราคาทอง",
    "คริปโต",
    "bitcoin",
    "บิตคอยน์",
    "ค่าเงิน",
    "อากาศ",
    "พยากรณ์",
    "สถานการณ์",
    "อันดับโลก",
    "ยอดนิยม",
    "มาแรง",
)


def contains_ascii_bounded(text: str, term: str) -> bool:
    """Match ASCII terms as tokens while preserving Thai substring matching."""
    query = normalize_text(text)
    value = normalize_text(term)
    if not value:
        return False
    if re.fullmatch(r"[a-z0-9][a-z0-9 ._+/#:-]*", value):
        return re.search(rf"(?<![a-z0-9]){re.escape(value)}(?![a-z0-9])", query) is not None
    return value in query


def has_any_signal(text: str, *terms: str) -> bool:
    return any(contains_ascii_bounded(text, term) for term in terms)


def looks_like_price_amount_query(text: str) -> bool:
    """Detect an amount/fee question without treating bare `เสีย` as price."""
    return has_any_signal(text, *_PRICE_AMOUNT_TERMS)


def looks_like_general_concept_definition(text: str) -> bool:
    query = normalize_text(text)
    return (
        has_any_signal(query, *_GENERAL_CONCEPT_TERMS)
        and has_any_signal(query, *_DEFINITION_TERMS)
        and not has_any_signal(query, *_PSU_INVENTORY_TERMS)
    )


def looks_like_game_zone_ranking_query(text: str) -> bool:
    query = normalize_text(text)
    if has_any_signal(query, *_GAME_ZONE_RANKING_TERMS):
        return True
    return (
        has_any_signal(query, "เกม", "game", "games")
        and has_any_signal(query, *_RANKING_OPERATION_TERMS)
        and has_any_signal(query, *_RANKING_TARGET_TERMS)
    )


def looks_like_explicit_definition_question(text: str) -> bool:
    return has_any_signal(text, *_DEFINITION_TERMS)


def looks_like_clear_general_request(text: str) -> bool:
    query = normalize_text(text)
    if looks_like_dynamic_freshness_query(query):
        return False
    if has_any_signal(query, *_PSU_INVENTORY_TERMS):
        return False
    if has_any_signal(query, *_GENERAL_TRANSLATION_TERMS, *_GENERAL_CREATION_TERMS):
        return True
    if has_any_signal(
        query,
        "ข้อดีข้อเสีย",
        "ข้อดี",
        "ข้อเสีย",
        "ประโยชน์",
        "แตกต่างกันยังไง",
        "ต่างกันยังไง",
        "เปรียบเทียบแบบทั่วไป",
    ):
        return True
    if looks_like_general_concept_definition(query):
        return True
    return has_any_signal(
        query,
        "ช่วยทำการบ้าน",
        "ช่วยอธิบาย",
        "อธิบายคำว่า",
        "นิยามคำว่า",
        "ยกตัวอย่างคำว่า",
    )


def looks_like_missing_task_input(text: str) -> bool:
    """Detect task requests that omit the content required to perform them."""
    query = normalize_text(text)
    if not has_any_signal(query, "ช่วยทำการบ้าน", "ทำการบ้านให้หน่อย", "ช่วยแก้การบ้าน"):
        return False
    if has_any_signal(query, "โจทย์คือ", "โจทย์ว่า", "กำหนดให้", "จงหา", "จงคำนวณ", "สมการ"):
        return False
    if re.search(r"\d|[=+*/^]", query):
        return False
    return True


def looks_like_dynamic_freshness_query(text: str) -> bool:
    query = normalize_text(text)
    return has_any_signal(query, *_DYNAMIC_FRESHNESS_TERMS) and has_any_signal(query, *_DYNAMIC_TOPIC_TERMS)


def has_live_evidence(hits: list[dict] | None) -> bool:
    for hit in hits or []:
        if not isinstance(hit, dict):
            continue
        metadata = hit.get("metadata") if isinstance(hit.get("metadata"), dict) else {}
        live = bool(hit.get("live_evidence") or metadata.get("live_evidence"))
        retrieved_at = str(hit.get("retrieved_at") or metadata.get("retrieved_at") or "").strip()
        if live and retrieved_at:
            return True
        freshness_verified = bool(
            hit.get("freshness_verified") or metadata.get("freshness_verified")
        )
        valid_until = str(
            hit.get("valid_until") or metadata.get("valid_until") or ""
        ).strip()
        try:
            current_until = date.fromisoformat(valid_until[:10]) if valid_until else None
        except ValueError:
            current_until = None
        if freshness_verified and retrieved_at and current_until and current_until >= date.today():
            return True
    return False


@dataclass(frozen=True)
class FreshnessDecision:
    requires_live_evidence: bool
    reason: str
    answer: str = ""


def evaluate_freshness_requirement(text: str) -> FreshnessDecision:
    if not looks_like_dynamic_freshness_query(text):
        return FreshnessDecision(False, "query does not require live dynamic evidence")
    return FreshnessDecision(
        True,
        "dynamic current-state query requires a live provider with retrieval timestamp",
        (
            "ตอนนี้ยังไม่มีแหล่งข้อมูลสดที่ใช้ยืนยันคำตอบปัจจุบันสำหรับเรื่องนี้ครับ "
            "จึงไม่ควรระบุชื่อหรือข้อมูลล่าสุดจากความรู้เดิม เพราะอาจไม่ตรงกับสถานการณ์ตอนนี้"
        ),
    )
