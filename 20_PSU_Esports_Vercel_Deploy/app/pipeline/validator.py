from __future__ import annotations

import re

from app.pipeline.schemas import EntityBundle, PipelineRoute, ValidationResult


def _first_line(answer: str) -> str:
    for line in (answer or "").splitlines():
        if line.strip():
            return line.strip()
    return ""


def validate_answer(question: str, answer: str, route: PipelineRoute, entities: EntityBundle) -> ValidationResult:
    q = question.lower()
    first = _first_line(answer).lower()
    text = (answer or "").lower()
    errors: list[str] = []
    warnings: list[str] = []

    if route.category == "schedule" and "24" not in q and ("24 ชั่วโมง" in text or "24 hours" in text):
        errors.append("schedule_answer_mentions_24h_without_user_asking")

    if ("ต่างกัน" in q or "ต่างกันเท่า" in q) and "ต่างกัน" not in first:
        warnings.append("comparison_question_should_start_with_difference")

    if route.category == "service_fee" and entities.price_intent:
        if "บาท" not in first and not re.search(r"\d", first):
            warnings.append("price_question_should_start_with_price_or_number")

    if route.category == "schedule" and entities.day == "monday" and {"morning", "afternoon"}.issubset(set(entities.time_slots)):
        if not (("morning" in first or "ช่วงเช้า" in first) and ("afternoon" in first or "ช่วงบ่าย" in first or "13:00" in first)):
            warnings.append("monday_morning_afternoon_question_should_answer_both_slots_first")

    line_count = len([line for line in answer.splitlines() if line.strip()])
    if route.answer_type in {"fact", "calculation"} and line_count > 14:
        warnings.append("fact_answer_may_be_too_verbose")

    if "ไม่พบข้อมูล" in text and route.confidence >= 0.90 and route.category not in {"no_answer", "general"}:
        warnings.append("high_confidence_route_returned_no_answer")

    return ValidationResult(ok=not errors, errors=tuple(errors), warnings=tuple(warnings))
