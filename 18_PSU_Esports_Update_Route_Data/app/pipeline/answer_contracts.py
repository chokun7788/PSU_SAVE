from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass
from typing import Any

from app.core.normalization import normalize_text
from app.pipeline.question_frame import QuestionFrame, build_question_frame
from app.pipeline.schemas import PipelineRoute, UniversalIntent


@dataclass(frozen=True)
class ContractValidation:
    ok: bool
    errors: tuple[str, ...] = ()
    warnings: tuple[str, ...] = ()
    answer_types: tuple[str, ...] = ()
    frame: QuestionFrame | None = None


def _has(text: str, *terms: str) -> bool:
    clean = normalize_text(text)
    return any(normalize_text(term) in clean for term in terms)


def _compact(value: str) -> str:
    clean = unicodedata.normalize("NFKD", normalize_text(value or ""))
    clean = "".join(char for char in clean if not unicodedata.combining(char))
    return re.sub(r"[^0-9a-z\u0E00-\u0E7F]+", "", clean)


def _answer_types(answer: str, route: PipelineRoute, mode: str = "") -> set[str]:
    types: set[str] = set()
    mode_key = mode.removeprefix("pipeline:")
    safe_control_mode = any(
        term in mode_key
        for term in ("structured_game_controls_no_current_game", "structured_game_controls_no_data")
    )
    if safe_control_mode:
        types.add("no_answer")
    if "structured_service_game_availability_no_match" in mode_key:
        types.add("no_answer")
    typed_modes: tuple[tuple[tuple[str, ...], tuple[str, ...]], ...] = (
        (("structured_game_controls", "game_control_vector"), ("controls", "list", "how_to")),
        (("structured_service_fee", "deterministic_calculator", "price_calculator"), ("price", "calculation")),
        (("structured_booking", "structured_reservation"), ("booking", "how_to")),
        (("structured_schedule", "schedule_fast", "calendar_closure_fast", "calendar_upcoming_holidays_fast"), ("schedule",)),
        (("structured_game_zone_ranking",), ("ranking", "list", "calculation")),
        (("structured_games_genre_list",), ("game_catalog", "list")),
        (("structured_games_catalog", "structured_games_family", "games_catalog"), ("game_catalog", "list")),
        (("structured_game_detail", "game_detail_fast"), ("game_detail", "how_to")),
        (("structured_equipment", "equipment_fast"), ("equipment", "list")),
        (("structured_members", "member"), ("member", "list")),
        (("competition_fact_card", "competition_rule"), ("competition_rule",)),
        (("penalty_fast", "penalty_rule"), ("penalty", "rule")),
        (("semantic_rag_dynamic", "semantic_grounded"), ("fact", "summary")),
    )
    if not safe_control_mode:
        for mode_terms, inferred_types in typed_modes:
            if any(term in mode_key for term in mode_terms):
                types.update(inferred_types)
    if route.category in {"no_answer", "clarification"} or _has(
        answer,
        "ยังไม่พบ",
        "ยังไม่พบข้อมูล",
        "ไม่พบข้อมูล",
        "ยังไม่มีข้อมูล",
        "ยังไม่แน่ใจ",
        "ขอชื่อเกมก่อน",
        "ขอรายละเอียดเพิ่ม",
        "คำถามนี้ยังไม่ชัด",
        "คำถามนี้ยังตีได้หลายทาง",
    ):
        types.add("no_answer" if route.category == "no_answer" or _has(answer, "ยังไม่พบ", "ไม่พบข้อมูล") else "clarification")
    if _has(answer, "ปุ่มควบคุม", "กดเพื่อ", "Square", "Triangle", "Cross", "Circle", "Joy-Con", "ZR", "ZL"):
        types.update({"controls", "list", "how_to"})
    if _has(answer, "บาท", "ค่าบริการ", "service fee", "General Adult") or re.search(r"\d+\s*บาท", answer):
        types.update({"price", "calculation"})
    if _has(
        answer,
        "ขั้นตอนจอง",
        "ให้จอง",
        "เลือกวัน",
        "รอบเวลา",
        "แนบสลิป",
        "ยืนยันการจอง",
        "เลือกบริการ",
        "จำนวนผู้เล่น",
    ):
        types.update({"booking", "how_to"})
    if _has(answer, "เปิดเวลา", "ปิดเวลา", "เปิดให้บริการ", "ปิดให้บริการ", "วันหยุดราชการ", "ช่วงเช้า", "ช่วงบ่าย"):
        types.add("schedule")
    if _has(answer, "จำนวนเกมตามโซน", "เกมเยอะสุด", "เกมมากที่สุด"):
        types.update({"ranking", "list", "calculation"})
    if _has(answer, "มีเกมที่ยืนยันได้ทั้งหมด", "รายชื่อเกม", "PC Zone (", "PlayStation 5 Zone ("):
        types.update({"game_catalog", "list"})
    if "structured_service_game_availability" in mode_key:
        if _has(answer, "เล่นได้ที่") and not _has(answer, "มีเกมที่ยืนยันได้ดังนี้"):
            types.add("game_detail")
        else:
            types.update({"game_catalog", "list"})
    if _has(answer, "แนวเกม:", "วิธีเล่นโดยสรุป:", "เล่นได้ที่:"):
        types.update({"game_detail", "how_to"})
    if _has(answer, "อุปกรณ์ใน", "จำนวน:", "ใช้สำหรับ:", "Gaming PC", "PlayStation 5 Slim"):
        types.update({"equipment", "list"})
    if _has(answer, "สมาชิก", "ตำแหน่ง", "ทีมงาน", "ผู้จัดการ", "สหกิจ", "ฝึกงาน"):
        types.update({"member", "list"})
    if _has(answer, "กติกา", "การแข่งขัน", "รอบชิง", "BO1", "BO3"):
        types.add("competition_rule")
    if _has(answer, "ค่าปรับ", "ต้องรับผิดชอบ", "ความเสียหาย", "ชดใช้"):
        types.update({"penalty", "rule"})
    if not types:
        types.update({"fact", "summary"})
    return types


def _source_categories(hits: list[dict[str, Any]] | None) -> set[str]:
    categories: set[str] = set()
    for hit in hits or []:
        if not isinstance(hit, dict):
            continue
        metadata = hit.get("metadata", {}) if isinstance(hit.get("metadata"), dict) else {}
        for value in (hit.get("category"), metadata.get("category"), hit.get("source_type"), metadata.get("source_type")):
            clean = str(value or "").strip().lower()
            if clean:
                categories.add(clean)
    return categories


def _allowed_source_categories(operation: str) -> set[str]:
    return {
        "control_lookup": {"game_controls"},
        "price_lookup": {"service_fee", "official_image", "local_fact_update"},
        "price_calculate": {"service_fee", "official_image", "local_fact_update"},
        "booking_lookup": {"reservation", "games"},
        "booking_session_limit": {"reservation"},
        "schedule_lookup": {"schedule", "reservation"},
        "game_zone_rank": {"games"},
        "game_catalog": {"games"},
        "game_detail": {"games", "knowledge", "competition_rules"},
        "game_how_to": {"games", "game_controls"},
        "equipment_lookup": {"equipment"},
        "member_lookup": {"members", "overview"},
        "studio_rule_lookup": {"rules", "reservation", "penalty"},
        "competition_rule_lookup": {"competition_rules", "rules"},
        "penalty_lookup": {"penalty", "rules"},
        "semantic_evidence_lookup": {"knowledge", "events_news", "about_us", "overview"},
    }.get(operation, set())


def validate_answer_contract(
    question: str,
    answer: str,
    route: PipelineRoute,
    *,
    hits: list[dict[str, Any]] | None = None,
    mode: str = "",
    intent: UniversalIntent | None = None,
    frame: QuestionFrame | None = None,
) -> ContractValidation:
    if not question.strip():
        return ContractValidation(ok=True)

    frame = frame or build_question_frame(question, route, intent)
    actual_types = _answer_types(answer, route, mode)
    safe_types = {"no_answer", "clarification"}
    errors: list[str] = []
    warnings: list[str] = []

    if not actual_types.intersection(frame.expected_answer_types) and not actual_types.intersection(safe_types):
        errors.append(
            "answer_contract_type_mismatch:"
            f"expected={','.join(frame.expected_answer_types)};actual={','.join(sorted(actual_types))}"
        )

    if frame.needs_clarification and not actual_types.intersection(safe_types):
        errors.append("answer_contract_ambiguous_target_must_clarify")

    if frame.targets and not actual_types.intersection(safe_types):
        target = frame.targets[0]
        target_text = _compact(target.label)
        answer_text = _compact(answer)
        if target.target_type == "game" and frame.operation in {
            "control_lookup",
            "game_detail",
            "game_how_to",
            "booking_lookup",
        }:
            target_parts = [part for part in re.findall(r"[0-9a-z]+|[\u0E00-\u0E7F]+", normalize_text(target.label)) if len(_compact(part)) >= 3]
            target_present = bool(target_text and target_text in answer_text)
            if not target_present and target_parts:
                target_present = all(_compact(part) in answer_text for part in target_parts[:3])
            if not target_present:
                errors.append(f"answer_contract_target_missing:{target.target_id}")

    if hits is not None and not actual_types.intersection(safe_types) and route.category not in {"general", "unknown"}:
        if not hits:
            errors.append("answer_contract_missing_evidence")
        else:
            allowed_categories = _allowed_source_categories(frame.operation)
            source_categories = _source_categories(hits)
            if allowed_categories and source_categories and allowed_categories.isdisjoint(source_categories):
                errors.append(
                    "answer_contract_source_domain_mismatch:"
                    f"expected={','.join(sorted(allowed_categories))};actual={','.join(sorted(source_categories))}"
                )

    if frame.operation == "game_zone_rank" and "ranking" not in actual_types:
        errors.append("answer_contract_game_ranking_missing_ranked_result")

    if mode and mode.startswith("pipeline:structured_game_controls") and "controls" not in actual_types and not actual_types.intersection(safe_types):
        errors.append("answer_contract_control_mode_without_controls")

    return ContractValidation(
        ok=not errors,
        errors=tuple(dict.fromkeys(errors)),
        warnings=tuple(dict.fromkeys(warnings)),
        answer_types=tuple(sorted(actual_types)),
        frame=frame,
    )
