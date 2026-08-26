from __future__ import annotations

import re

from app.core.normalization import normalize_text
from app.pipeline.answer_contracts import validate_answer_contract
from app.pipeline.query_signals import has_live_evidence, looks_like_dynamic_freshness_query, looks_like_price_amount_query
from app.core.source_registry import (
    PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID,
    SERVICE_FEE_IMAGE_2026_ID,
)
from app.pipeline.schemas import EntityBundle, PipelineRoute, UniversalIntent, ValidationResult


def _first_line(answer: str) -> str:
    for line in (answer or "").splitlines():
        if line.strip():
            return line.strip()
    return ""


def _has(text: str, *terms: str) -> bool:
    clean = normalize_text(text)
    return any(normalize_text(term) in clean for term in terms)


def _looks_like_booking_query(question: str) -> bool:
    return _has(
        question,
        "จอง",
        "booking",
        "book",
        "เลือกบริการ",
        "ต้องเลือก",
        "ต้องระบุ",
        "จำนวนผู้เล่น",
        "รอบเวลา",
        "จองโซน",
        "ต้องจอง",
    )


def _looks_like_price_query(question: str) -> bool:
    if _has(question, "ค่าปรับ", "ทำพัง", "เสียหาย", "ชำรุด", "ชดใช้", "รับผิดชอบ"):
        return False
    return looks_like_price_amount_query(question)


def _looks_like_control_query(question: str) -> bool:
    return _has(
        question,
        "ปุ่ม",
        "button",
        "controls",
        "control",
        "จอย",
        "กดอะไร",
        "กดปุ่มไหน",
        "ปุ่มอะไร",
        "ควบคุม",
    )


def _looks_like_cancel_policy_query(question: str) -> bool:
    return _has(
        question,
        "ยกเลิก",
        "cancel",
        "เลื่อนวัน",
        "เปลี่ยนเวลา",
        "เปลี่ยนวัน",
        "คืนเงิน",
        "refund",
    )


def _looks_like_bare_broad_query(question: str) -> bool:
    q = normalize_text(question).strip()
    return q in {"มีอะไรบ้าง", "มีอะไร", "อะไรบ้าง", "ทั้งหมดมีอะไรบ้าง"}


def _looks_like_specific_game_detail_query(question: str) -> bool:
    if _has(question, "มีเกมอะไร", "เกมอะไรบ้าง", "รายชื่อเกม", "เกมทั้งหมด", "เล่นเกมอะไรได้บ้าง"):
        return False
    return _has(question, "คือเกมอะไร", "อะไรคือเกม", "เป็นเกมแนวไหน", "แนวอะไร", "แนวไหน", "เกี่ยวกับอะไร")


def _looks_like_competition_rule_query(question: str) -> bool:
    return _has(
        question,
        "รอบชิง",
        "รอบรอง",
        "กติกา",
        "แข่ง",
        "แข่งขัน",
        "ทัวร์",
        "bo1",
        "bo3",
        "best of",
        "ทีมละ",
        "ตัวสำรอง",
        "มาสาย",
        "voice chat",
        "บัญชี",
        "เช็คอิน",
    )


def _looks_like_people_or_role_query(question: str) -> bool:
    return _has(
        question,
        "สมาชิก",
        "member",
        "members",
        "staff",
        "สตาฟ",
        "เจ้าหน้าที่",
        "คนดูแล",
        "ทีมงาน",
        "บุคลากร",
        "ตำแหน่ง",
        "ผู้จัดการ",
        "สหกิจ",
        "ฝึกงาน",
        "ใคร",
        "ใครบ้าง",
        "ใครทำ",
        "ใครเป็น",
    )


def _answer_looks_like_game_catalog(answer: str) -> bool:
    return _has(
        answer,
        "มีเกมที่ยืนยันได้ทั้งหมด",
        "มีเกมที่ยืนยันได้ดังนี้",
        "PC Zone (",
        "PlayStation 5 Zone (",
        "Nintendo Switch Zone (",
        "Cockpit Zone (",
        "VR Zone (",
    )


def _answer_looks_like_equipment_detail_or_catalog(answer: str) -> bool:
    return _has(
        answer,
        "อุปกรณ์ใน",
        "จำนวน:",
        "อยู่ที่:",
        "ใช้สำหรับ:",
        "Gaming PC",
        "Nintendo Switch OLED:",
        "PlayStation 5 Slim",
        "Logitech G923:",
    )


def _answer_looks_like_booking_selection(answer: str) -> bool:
    return _has(
        answer,
        "จอง",
        "เลือกบริการ",
        "จำนวนผู้เล่น",
        "1-2 Persons",
        "3-4 Persons",
        "รอบเวลา",
        "Cockpit Zone",
        "แนบสลิป",
    )


def _answer_looks_like_price_table_or_calculation(answer: str) -> bool:
    return _has(
        answer,
        "บาท",
        "ราคา",
        "ค่าบริการ",
        "service fee",
        "PSU Student and Staff",
        "General Adult",
    ) or bool(re.search(r"\d+\s*บาท", answer))


def _answer_looks_like_game_detail(answer: str) -> bool:
    return _has(answer, "แนวเกม", "วิธีเล่นโดยสรุป", "เล่นได้ที่:")


def _answer_looks_like_control_facts(answer: str) -> bool:
    return _has(
        answer,
        "มีข้อมูลปุ่มควบคุม",
        "Square",
        "Triangle",
        "Circle",
        "Cross",
        "Joy-Con",
        "ZR",
        "ZL",
        "ปุ่ม",
        "กด",
    )


def _answer_looks_like_clarification(answer: str) -> bool:
    return _has(answer, "ขอรู้", "ยังไม่แน่ใจ", "ยังกว้างเกินไป", "ถามให้เจาะจง", "ระบุ")


def _hit_source_ids(hits: list[dict] | None) -> set[str]:
    ids: set[str] = set()
    for hit in hits or []:
        if not isinstance(hit, dict):
            continue
        metadata = hit.get("metadata", {}) if isinstance(hit.get("metadata"), dict) else {}
        source_ids = metadata.get("source_ids")
        values = source_ids if isinstance(source_ids, list) else [hit.get("id") or metadata.get("title")]
        for value in values:
            text = str(value or "").strip()
            if text:
                ids.add(text)
    return ids


def _hit_source_blob(hits: list[dict] | None) -> str:
    chunks: list[str] = []
    for hit in hits or []:
        if not isinstance(hit, dict):
            continue
        metadata = hit.get("metadata", {}) if isinstance(hit.get("metadata"), dict) else {}
        for key in ("id", "category", "source_url", "title", "source_type", "trust_level", "updated_at"):
            chunks.append(str(hit.get(key, "")))
            chunks.append(str(metadata.get(key, "")))
        source_ids = metadata.get("source_ids")
        if isinstance(source_ids, list):
            chunks.extend(str(item) for item in source_ids)
    return " ".join(chunks)


def validate_answer(
    question: str,
    answer: str,
    route: PipelineRoute,
    entities: EntityBundle,
    hits: list[dict] | None = None,
    *,
    mode: str = "",
    intent: UniversalIntent | None = None,
) -> ValidationResult:
    q = question.lower()
    first = _first_line(answer).lower()
    text = (answer or "").lower()
    errors: list[str] = []
    warnings: list[str] = []
    source_ids = _hit_source_ids(hits)
    source_blob = _hit_source_blob(hits).lower()

    if looks_like_dynamic_freshness_query(question) and not has_live_evidence(hits):
        safe_freshness_abstention = _has(
            answer,
            "ยังไม่มีแหล่งข้อมูลสด",
            "ยืนยันข้อมูลปัจจุบันไม่ได้",
            "ไม่สามารถยืนยันข้อมูลล่าสุด",
            "จึงไม่ควรระบุ",
        )
        if not safe_freshness_abstention:
            errors.append("freshness_claim_without_live_evidence")

    if route.category == "schedule" and "24" not in q and ("24 ชั่วโมง" in text or "24 hours" in text):
        errors.append("schedule_answer_mentions_24h_without_user_asking")

    if ("ต่างกัน" in q or "ต่างกันเท่า" in q) and "ต่างกัน" not in first:
        warnings.append("comparison_question_should_start_with_difference")

    if route.category == "service_fee" and entities.price_intent:
        if "บาท" not in first and not re.search(r"\d", first):
            warnings.append("price_question_should_start_with_price_or_number")

    if _looks_like_price_query(question):
        if _answer_looks_like_game_catalog(answer):
            errors.append("price_question_answered_as_game_catalog")
        if route.category == "games" and _answer_looks_like_game_detail(answer) and not _answer_looks_like_price_table_or_calculation(answer):
            errors.append("price_question_answered_as_game_detail_without_price")

    if route.category == "schedule" and entities.day == "monday" and {"morning", "afternoon"}.issubset(set(entities.time_slots)):
        if not (("morning" in first or "ช่วงเช้า" in first) and ("afternoon" in first or "ช่วงบ่าย" in first or "13:00" in first)):
            warnings.append("monday_morning_afternoon_question_should_answer_both_slots_first")

    line_count = len([line for line in answer.splitlines() if line.strip()])
    if route.answer_type in {"fact", "calculation"} and line_count > 14:
        warnings.append("fact_answer_may_be_too_verbose")

    if "ไม่พบข้อมูล" in text and route.confidence >= 0.90 and route.category not in {"no_answer", "general"}:
        warnings.append("high_confidence_route_returned_no_answer")

    if _looks_like_booking_query(question) and not _looks_like_price_query(question):
        if _answer_looks_like_equipment_detail_or_catalog(answer) or _answer_looks_like_game_catalog(answer):
            errors.append("booking_question_answered_as_equipment_or_game_catalog")
        elif route.category in {"equipment", "games"} and _answer_looks_like_booking_selection(answer):
            warnings.append("booking_answer_has_non_booking_route_label")
        if not _looks_like_cancel_policy_query(question) and _has(answer, "ยกเลิกการจอง", "ยกเลิกการจองเดิม", "คืนเงิน"):
            if not _has(answer, "เลือกบริการ", "รอบเวลา", "แนบสลิป"):
                errors.append("booking_howto_question_answered_as_cancellation_policy")

    if _looks_like_control_query(question):
        if _answer_looks_like_game_catalog(answer):
            errors.append("control_question_answered_as_game_catalog")
        elif _answer_looks_like_game_detail(answer) and not _answer_looks_like_control_facts(answer):
            errors.append("control_question_answered_as_game_detail")

    if _looks_like_specific_game_detail_query(question) and _answer_looks_like_game_catalog(answer):
        errors.append("specific_game_detail_answered_as_game_catalog")

    if _looks_like_competition_rule_query(question) and _answer_looks_like_game_catalog(answer):
        errors.append("competition_rule_answered_as_game_catalog")

    if _looks_like_people_or_role_query(question) and _answer_looks_like_game_catalog(answer):
        errors.append("people_or_role_question_answered_as_game_catalog")

    if _looks_like_price_query(question) and route.category not in {"service_fee", "reservation"}:
        if not re.search(r"\d", first) and "บาท" not in first:
            warnings.append("price_question_may_have_wrong_route")

    if _looks_like_bare_broad_query(question) and route.category != "clarification" and not _answer_looks_like_clarification(answer):
        errors.append("bare_broad_query_should_clarify_before_answering")

    if hits is not None:
        price_context = (
            route.category == "service_fee"
            or _looks_like_price_query(question)
            or (
                route.category not in {"penalty", "rules", "competition_rules"}
                and _answer_looks_like_price_table_or_calculation(answer)
            )
        )
        if price_context:
            if SERVICE_FEE_IMAGE_2026_ID not in source_ids and "service-fee" not in source_blob and "service_fee" not in source_blob:
                warnings.append("service_fee_answer_missing_service_fee_source")
        pc_price_context = (
            price_context
            and (route.category == "service_fee" or _looks_like_price_query(question))
            and _has(question, "PC", "คอม", "คอมพิวเตอร์")
        )
        if pc_price_context:
            if PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID not in source_ids:
                errors.append("pc_price_answer_missing_pc_local_update_source")
        if PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID in source_ids and not _has(question + "\n" + answer, "PC", "คอม", "คอมพิวเตอร์"):
            warnings.append("pc_local_update_source_present_without_pc_price_context")

    contract = validate_answer_contract(
        question,
        answer,
        route,
        hits=hits,
        mode=mode,
        intent=intent,
    )
    errors.extend(contract.errors)
    warnings.extend(contract.warnings)

    return ValidationResult(
        ok=not errors,
        errors=tuple(dict.fromkeys(errors)),
        warnings=tuple(dict.fromkeys(warnings)),
    )
