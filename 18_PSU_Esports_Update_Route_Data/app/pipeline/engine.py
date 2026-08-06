from __future__ import annotations

import os
import re
import time
from concurrent.futures import ThreadPoolExecutor
from contextvars import copy_context

from app.core.normalization import normalize_text
from app.core.thai_style import format_thai_response_style
from app.pipeline.ambiguity_gate import evaluate_ambiguity_gate
from app.pipeline.boundary_guard import evaluate_boundary
from app.pipeline.capability_registry import build_candidate_decisions
from app.pipeline.compound_execution import CompoundProfile, build_compound_plan, classify_compound
from app.pipeline.decision_artifact import build_decision_artifact
from app.pipeline.formatter import format_answer, format_no_answer
from app.pipeline.guard import guard_scope
from app.pipeline.hybrid_retrieval import (
    answer_from_hybrid_hits,
    retrieve_hybrid_guarded,
    should_skip_legacy_curated_after_hybrid,
    should_use_hybrid_retrieval,
)
from app.pipeline.llm_tool_router import resolve_tool_routing
from app.pipeline.preprocess import extract_entities, preprocess_input
from app.pipeline.query_planner import (
    QueryPlanTask,
    plan_query,
    planner_skip_trace,
    should_use_query_planner,
)
from app.pipeline.question_frame import build_question_frame
from app.pipeline.request_deadline import deadline_exceeded, deadline_metadata, request_deadline
from app.pipeline.experimental_fallback import (
    build_experimental_fallback,
    env_experimental_llm_default,
    env_experimental_rag_fallback_default,
)
from app.pipeline.facts_composer import compose_structured_answer
from app.pipeline.evidence_packer import pack_evidence
from app.pipeline.model_gateway import plan_rag_model_path, preflight_llm_allowed
from app.pipeline.retrieval import (
    answer_from_competition_fact_hits,
    answer_from_curated_hits,
    retrieve_competition_fact_cards,
    retrieve_curated,
)
from app.pipeline.router import route_intent
from app.pipeline.routing_policy import apply_routing_priority_policy
from app.pipeline.schemas import EntityBundle, PipelineAnswer, PipelineRoute, PipelineTrace, UniversalIntent, ValidationResult
from app.pipeline.structured_tools import answer_with_structured_tool
from app.pipeline.tool_preconditions import evaluate_structured_tool_precondition
from app.pipeline.universal_intent import refine_route_with_universal_intent, resolve_universal_intent
from app.pipeline.validator import validate_answer
from app.pipeline.vector_retrieval import (
    answer_from_vector_hits,
    has_explicit_game_hint,
    looks_like_game_control_query,
    retrieve_vector_guarded,
)
from app.rules.matcher import RuleMatcher
from app.runtime.fast_answer import (
    COMPETITION_GAME_SUMMARY,
    HITS,
    FastAnswer,
    answer_equipment,
    answer_competition_rules,
    answer_games,
    answer_price,
    answer_schedule,
    answer_static_domain,
)


RULE_CATEGORY_MAP = {
    "checkin": {"reservation"},
    "payment": {"reservation"},
    "cancel": {"reservation"},
    "reservation": {"reservation"},
    "rules": {"rules"},
    "penalty": {"penalty"},
    "games": {"games"},
    "equipment": {"equipment"},
    "contact": {"contact"},
    "overview": {"overview"},
}

TOOL_ROUTER_DOMAIN_ROUTE_MAP = {
    "competition_rules": ("competition_rules", "competition_rules_lookup", "fact", "medium"),
    "contact": ("contact", "contact_lookup", "fact", "low"),
    "knowledge": ("knowledge", "knowledge_lookup", "summary", "low"),
    "games": ("games", "games_lookup", "list", "low"),
    "equipment": ("equipment", "equipment_lookup", "list", "low"),
    "reservation": ("reservation", "booking_policy", "fact", "medium"),
    "schedule": ("schedule", "schedule_query", "fact", "medium"),
    "service_fee": ("service_fee", "service_fee_query", "fact", "medium"),
}


def _has(q: str, *terms: str) -> bool:
    return any(term in q for term in terms)


def _timing_trace(
    decision: str,
    started: float,
    *,
    detail: str = "",
    metadata: dict | None = None,
    confidence: float = 1.0,
) -> PipelineTrace:
    elapsed = time.perf_counter() - started
    timing_metadata = {
        "elapsed_ms": round(elapsed * 1000, 2),
        "elapsed_sec": round(elapsed, 4),
    }
    if metadata:
        timing_metadata.update(metadata)
    return PipelineTrace("timing", decision, confidence, detail, timing_metadata)


def _looks_like_standalone_question(q: str) -> bool:
    q = normalize_text(q)
    has_question_signal = _has(
        q,
        "ไหม", "มั้ย", "หรือเปล่า", "รึเปล่า", "อะไร", "กี่", "เท่าไหร่", "เท่าไร",
        "ยังไง", "อย่างไร", "ได้ไหม", "ใคร", "ที่ไหน", "ไหน", "เปิด", "ปิด", "ราคา", "ค่าบริการ", "จอง",
    )
    has_domain_signal = _has(
        q,
        "วันนี้", "พรุ่งนี้", "วันจัน", "จันทร์", "อังคาร", "พุธ", "พฤหัส", "ศุกร์",
        "เปิด", "ปิด", "ราคา", "ค่าบริการ", "บาท", "vr", "วีอาร์", "ps5", "เพลย์",
        "pc", "คอม", "cockpit", "คอกพิท", "ค็อกพิท", "nintendo", "switch",
        "อุปกรณ์", "เกม", "แข่ง", "แข่งขัน", "กติกา", "กฎ", "จอง", "เช็คอิน",
        "ยกเลิก", "จ่าย", "ชำระ", "ติดต่อ", "เบอร์", "facebook", "ที่ตั้ง",
        "เมาส์", "คีย์บอร์ด", "หูฟัง", "พวงมาลัย", "beat saber", "gran turismo",
        "minecraft", "roblox", "valorant", "วาโล", "cs2", "rov", "tekken",
        "call of duty", "warzone", "modern warfare", "mario", "resident evil",
        "horizon", "overcooked", "naruto", "fortnite", "สมาชิก", "member", "members",
    )
    return has_question_signal and has_domain_signal


def _split_boundary_compound_question(query: str) -> list[str]:
    """Split a supported PSU request from an unrelated or sensitive tail."""
    clean = re.sub(r"\s+", " ", query or "").strip()
    if not clean:
        return []
    boundary_tail_terms = (
        "รหัสผ่าน", "password", "พิกัด", "พิกัดบ้าน", "ส่งพิกัด", "ข้อมูลส่วนตัว",
        "คุณชอบ", "ชอบสี", "อากาศ", "การเมือง", "นายก", "ทำนายดวง", "เมนูอาหาร",
        "วิธีโกง", "โกงเกม", "แฮกเกม", "ไฟไหม้", "อาเจียน",
    )
    parts = [clean]
    # Keep the existing splitter as the primary parser. This extra pass is only
    # for boundary tails that could otherwise contaminate a valid PSU answer.
    for separator in ("แต่", "แล้ว", "และ", "ส่วน", "อีกอย่าง"):
        next_parts: list[str] = []
        for part in parts:
            chunks = [chunk.strip(" \t\r\n?？") for chunk in re.split(rf"\s+{re.escape(separator)}\s*", part) if chunk.strip(" \t\r\n?？")]
            if len(chunks) != 2:
                next_parts.append(part)
                continue
            left, right = chunks
            right_norm = normalize_text(right)
            left_norm = normalize_text(left)
            has_left_boundary = _has(left_norm, *boundary_tail_terms)
            has_right_boundary = _has(right_norm, *boundary_tail_terms)
            has_question_like_left = _looks_like_standalone_question(left_norm) or _has(left_norm, "หน่อย", "ขอ", "บอก")
            has_question_like_right = _looks_like_standalone_question(right_norm) or _has(right_norm, "หน่อย", "ขอ", "บอก")
            split_supported_and_boundary = (
                has_right_boundary and has_question_like_left
            ) or (
                has_left_boundary and has_question_like_right
            )
            if split_supported_and_boundary:
                next_parts.extend(chunks)
            else:
                next_parts.append(part)
        parts = next_parts
    if len(parts) <= 1 or len(parts) > 3:
        return [clean]
    return parts


def _looks_like_game_play_followup(query: str) -> bool:
    q = normalize_text(query)
    return any(term in q for term in (
        "เล่นยังไง",
        "เล่นอย่างไร",
        "วิธีเล่น",
        "สอนเล่น",
        "เล่นแบบไหน",
        "เล่นยังไงบ้าง",
        "เล่นยังไงได้บ้าง",
    ))


def _looks_like_equipment_location_query(query: str) -> bool:
    q = normalize_text(query)
    if not _has(q, "โซนไหน", "อยู่โซน", "อยู่ที่ไหน", "อยู่ไหน", "มีที่ไหน", "อยู่ในโซน"):
        return False
    return _has(
        q,
        "playstation vr2", "ps vr2", "psvr2", "vr2", "แว่น", "logitech", "g923",
        "racezone", "full cockpit", "pulse elite", "headset", "ทีวี", "tv", "โซฟา",
        "sofa", "พวงมาลัย", "คันเกียร์", "nintendo switch oled", "switch oled",
        "playstation 5 slim", "ps5 slim",
    )


def _known_named_game_without_control_data(query: str) -> str | None:
    q = normalize_text(query)
    aliases = (
        ("Minecraft", ("minecraft", "มายคราฟ")),
        ("RoV / Arena of Valor", ("rov", "arena of valor", "aov", "อาร์โอวี", "อาโอวี", "เอโอวี", "เกมตีป้อม")),
    )
    for name, terms in aliases:
        if _has(q, *terms):
            return name
    return None


def _looks_like_unclear_game_meta_query(query: str) -> bool:
    q = normalize_text(query)
    if "เกม" not in q and "game" not in q:
        return False
    return any(term in q for term in (
        "ถาม",
        "ถามได้",
        "ถามอะไร",
        "ถามอะไรได้บ้าง",
        "เกี่ยวกับเกม",
        "เรื่องเกม",
        "อยากรู้เรื่องเกม",
        "หลายๆอย่าง",
        "หลายอย่าง",
    ))


def _split_multi_question(query: str) -> list[str]:
    clean = re.sub(r"\s+", " ", query or "").strip()
    if not clean:
        return []
    normalized = normalize_text(clean)
    if _has(normalized, "จองแล้ว") and _has(normalized, "เช็คอิน", "เชคอิน", "ลืม"):
        return [clean]
    if _has(normalized, "จองแล้ว") and _has(normalized, "ยกเลิก", "ไม่สามารถยกเลิก", "แก้ไข", "แก้ข้อมูล"):
        return [clean]
    boundary_parts = _split_boundary_compound_question(clean)
    if len(boundary_parts) > 1:
        return boundary_parts
    if (
        "และ" in normalized
        and not _has(normalized, "แล้ว", "ส่วน", "อีกอย่าง")
        and has_explicit_game_hint(normalized)
        and looks_like_game_control_query(normalized)
        and not _has(normalized, "เล่นที่ไหน", "อยู่โซนไหน", "อยู่ที่ไหน", "ราคา", "กี่บาท", "จอง", "มีปุ่มอะไร", "ปุ่มอะไรบ้าง")
    ):
        return [clean]
    shared_tail_parts = _split_shared_tail_multi_entity_question(clean)
    if len(shared_tail_parts) > 1:
        return shared_tail_parts
    shared_subject_parts = _split_shared_subject_multi_operation_question(clean)
    if len(shared_subject_parts) > 1:
        return shared_subject_parts

    if (
        "และ" in normalized
        and not _has(normalized, "แล้ว", "ส่วน", "อีกอย่าง")
        and has_explicit_game_hint(normalized)
        and looks_like_game_control_query(normalized)
        and not _has(normalized, "เล่นที่ไหน", "อยู่โซนไหน", "อยู่ที่ไหน", "ราคา", "กี่บาท", "จอง", "มีปุ่มอะไร", "ปุ่มอะไรบ้าง")
    ):
        return [clean]

    parts = [
        part.strip(" \t\r\n?？")
        for part in re.split(r"\s*(?:[?？]|แล้ว|และ|ส่วน|อีกอย่าง)\s*", clean)
        if part.strip(" \t\r\n?？")
    ]
    parts = _carry_subject_to_short_followup_parts(parts)
    if len(parts) <= 1 or len(parts) > 3:
        return [clean]
    if not all(_looks_like_standalone_question(part) for part in parts):
        return [clean]
    return parts


_MULTI_OPERATION_PHRASES = (
    "ปุ่มทั้งหมดมีอะไรบ้าง",
    "มีปุ่มอะไรบ้าง",
    "ปุ่มอะไรบ้าง",
    "มีปุ่มอะไร",
    "ปุ่มอะไร",
    "กดอะไร",
    "เล่นที่ไหน",
    "อยู่โซนไหน",
    "อยู่ที่ไหน",
    "จองยังไง",
    "จองไง",
    "ต้องจองยังไง",
    "ต้องทำยังไง",
    "ต้องทำไง",
    "ราคาเท่าไหร่",
    "ราคาเท่าไร",
    "กี่บาท",
    "เปิดกี่โมง",
    "มีอุปกรณ์อะไรบ้าง",
    "อุปกรณ์อะไรบ้าง",
    "มีอุปกรณ์อะไร",
    "อุปกรณ์อะไร",
    "มีเกมอะไรบ้าง",
    "เกมอะไรบ้าง",
    "มีเกมอะไร",
    "มีเกมกี่เกม",
    "กี่เกม",
)

_SUBJECT_INFERENCE_PHRASES = (
    "เล่นยังไง",
    "เล่นอย่างไร",
    "วิธีเล่น",
    "มีกี่คน",
    "ใครเป็น",
    "ใครทำ",
    "เล่นได้ที่ไหน",
)


def _split_shared_subject_multi_operation_question(query: str) -> list[str]:
    clean = re.sub(r"\s+", " ", query or "").strip()
    if not clean:
        return [clean]
    lowered = clean.lower()
    matches: list[tuple[int, int, str]] = []
    for phrase in _MULTI_OPERATION_PHRASES:
        start = lowered.find(phrase.lower())
        if start >= 0:
            matches.append((start, start + len(phrase), phrase))
    if len(matches) < 2:
        return [clean]
    matches.sort(key=lambda item: (item[0], -(item[1] - item[0])))
    selected: list[tuple[int, int, str]] = []
    cursor = -1
    for match in matches:
        if match[0] < cursor:
            continue
        selected.append(match)
        cursor = match[1]
    if len(selected) < 2 or len(selected) > 4:
        return [clean]

    subject = _clean_shared_subject(clean[:selected[0][0]])
    if len(_compact_question_part(subject)) < 2:
        return [clean]
    for previous, current in zip(selected, selected[1:]):
        bridge = clean[previous[1]:current[0]]
        if _has_explicit_compound_subject(bridge):
            return [clean]
    parts = [_build_subject_operation_part(subject, phrase) for _start, _end, phrase in selected]
    if len(set(_compact_question_part(part) for part in parts)) != len(parts):
        return [clean]
    return parts


def _carry_subject_to_short_followup_parts(parts: list[str]) -> list[str]:
    if len(parts) <= 1 or len(parts) > 4:
        return parts
    subject = _infer_shared_subject_from_part(parts[0])
    if len(_compact_question_part(subject)) < 2:
        return parts
    enriched = [parts[0]]
    changed = False
    for part in parts[1:]:
        if _looks_like_short_operation_only(part) and (
            not _has_explicit_compound_subject(part) or _looks_like_subjectless_followup_operation(part)
        ):
            enriched.append(_build_subject_operation_part(subject, part))
            changed = True
        else:
            enriched.append(part)
    return enriched if changed else parts


def _looks_like_subjectless_followup_operation(part: str) -> bool:
    normalized = normalize_text(part).strip()
    return (
        normalized.startswith("ปุ่ม")
        or normalized.startswith("ใครเป็น")
        or normalized.startswith("ใครทำ")
        or normalized in {"เล่นได้ที่ไหน", "เล่นที่ไหน", "อยู่โซนไหน", "อยู่ที่ไหน"}
    )


def _infer_shared_subject_from_part(part: str) -> str:
    lowered = (part or "").lower()
    best_index = -1
    for phrase in (*_MULTI_OPERATION_PHRASES, *_SUBJECT_INFERENCE_PHRASES):
        index = lowered.find(phrase.lower())
        if index > 0 and (best_index < 0 or index < best_index):
            best_index = index
    if best_index < 0:
        match = re.search(r"\sปุ่ม.+?(?:อะไร|กดอะไร)", part, flags=re.IGNORECASE)
        if match and match.start() > 0:
            best_index = match.start()
    if best_index < 0:
        return ""
    return _clean_shared_subject(part[:best_index])


def _clean_shared_subject(subject: str) -> str:
    subject = re.sub(r"^\s*(?:ถ้าเล่น|ถ้าจะเล่น|ถ้าถาม|จะเล่น|เล่น|เกม|ของ|ถาม)\s+", "", subject or "", flags=re.IGNORECASE)
    subject = re.sub(r"\s*(?:แล้ว|และ|ส่วน|อีกอย่าง)\s*$", "", subject, flags=re.IGNORECASE)
    return subject.strip(" ,")


def _looks_like_short_operation_only(part: str) -> bool:
    compact = _compact_question_part(part)
    if len(compact) > 24:
        return False
    normalized = normalize_text(part)
    return any(normalize_text(phrase) in normalized for phrase in (*_MULTI_OPERATION_PHRASES, *_SUBJECT_INFERENCE_PHRASES))


def _has_explicit_compound_subject(part: str) -> bool:
    normalized = normalize_text(part)
    remainder = normalized
    for phrase in _MULTI_OPERATION_PHRASES:
        remainder = remainder.replace(normalize_text(phrase), " ")
    for term in (
        "zone", "โซน", "ราคา", "ค่า", "บริการ", "บาท", "เกม", "ปุ่ม", "จอง",
        "มี", "อะไร", "บ้าง", "เท่าไหร่", "เท่าไร", "กี่", "ยังไง", "อย่างไร",
        "แล้ว", "และ", "กับ", "ส่วน", "อีกอย่าง",
    ):
        remainder = remainder.replace(normalize_text(term), " ")
    return len(_compact_question_part(remainder)) >= 2


def _build_subject_operation_part(subject: str, operation: str) -> str:
    operation_norm = normalize_text(operation)
    if any(term in operation_norm for term in ("จอง", "ต้องทำ")):
        return f"จะเล่น {subject} {operation}".strip()
    return f"{subject} {operation}".strip()


def _split_shared_tail_multi_entity_question(query: str) -> list[str]:
    clean = re.sub(r"\s+", " ", query or "").strip()
    if not clean:
        return [clean]
    tails = (
        "ปุ่มทั้งหมดมีอะไรบ้าง",
        "มีปุ่มอะไรบ้าง",
        "ปุ่มอะไรบ้าง",
        "ปุ่มอะไร",
        "กดอะไร",
        "มีเกมอะไรบ้าง",
        "เกมอะไรบ้าง",
        "มีเกมกี่เกม",
        "กี่เกม",
        "คืออะไร",
        "มีข้อมูลไหม",
        "เล่นยังไง",
        "จองยังไง",
        "ต้องทำยังไง",
        "ต้องทำไง",
        "ราคาเท่าไหร่",
        "ราคาเท่าไร",
        "กี่บาท",
        "เปิดกี่โมง",
    )
    lower = clean.lower()
    tail = ""
    tail_index = -1
    for candidate in tails:
        index = lower.rfind(candidate.lower())
        if index > 0 and index + len(candidate) == len(clean):
            tail = clean[index:].strip()
            tail_index = index
            break
    if tail_index <= 0:
        return [clean]

    subject = clean[:tail_index].strip(" ,")
    if not re.search(r"\s*(?:กับ|และ)\s*", subject):
        return [clean]
    tail_norm = normalize_text(tail)
    subject_norm = normalize_text(subject)
    if (
        "และ" in subject_norm
        and _has(tail_norm, "กดอะไร", "ปุ่มอะไร", "มีปุ่มอะไร", "ปุ่มทั้งหมดมีอะไรบ้าง", "ปุ่มอะไรบ้าง")
        and _has(subject_norm, "ปุ่ม")
    ):
        return [clean]
    raw_items = [
        item.strip(" ,")
        for item in re.split(r"\s*(?:กับ|และ)\s*", subject)
        if item.strip(" ,")
    ]
    if len(raw_items) < 2 or len(raw_items) > 3:
        return [clean]

    items: list[str] = []
    for index, item in enumerate(raw_items):
        if index == 0:
            item = re.sub(r"^(?:ถ้าเล่น|ถ้าจะเล่น|ถ้าถาม|เล่น|เกม|ของ|ถาม)\s+", "", item, flags=re.IGNORECASE).strip()
        if len(_compact_question_part(item)) < 3:
            return [clean]
        items.append(item)
    if len(set(item.lower() for item in items)) != len(items):
        return [clean]
    return [f"{item} {tail}".strip() for item in items]


def _compact_question_part(value: str) -> str:
    return re.sub(r"[^0-9a-z\u0E00-\u0E7F]+", "", normalize_text(value or ""))


def _dedupe_hits(rows: list[dict]) -> list[dict]:
    unique: list[dict] = []
    seen: set[tuple[str, str]] = set()
    for row in rows:
        metadata = row.get("metadata", {}) if isinstance(row, dict) else {}
        key = (str(row.get("id", "")), str(metadata.get("source_url", "")))
        if key in seen:
            continue
        seen.add(key)
        unique.append(row)
    return unique


def _hit_for_url(source_id: str, category: str, url: str) -> dict:
    return {
        "id": source_id,
        "metadata": {
            "source_url": url,
            "category": category,
            "title": source_id,
            "source_ids": [source_id],
        },
    }


def _route_variant_is_better(current: PipelineRoute, candidate: PipelineRoute) -> bool:
    weak_categories = {"general", "unknown"}
    if current.category in weak_categories and candidate.category not in weak_categories:
        return candidate.confidence >= 0.70
    if current.category == "games" and current.intent in {"games_lookup", "game_availability_lookup"} and candidate.category == "knowledge":
        return candidate.confidence >= current.confidence
    if candidate.category == current.category and candidate.intent != current.intent:
        return candidate.confidence >= current.confidence + 0.08
    if candidate.category != current.category and candidate.category not in weak_categories:
        return candidate.confidence >= current.confidence + 0.12
    return False


def _should_evaluate_query_variants(route: PipelineRoute) -> bool:
    if route.category in {"general", "unknown"}:
        return True
    if route.category in {"games", "knowledge"}:
        return True
    return route.confidence < 0.94


def _select_active_preprocessed_query(pre) -> tuple:
    entities = extract_entities(pre)
    route, route_trace = route_intent(pre, entities)
    route, policy_trace = apply_routing_priority_policy(pre.normalized_query, route, entities)
    if policy_trace is not None:
        route_trace = policy_trace
    selected_pre = pre
    selected_entities = entities
    selected_route = route
    selected_trace = route_trace
    candidates: list[dict] = []

    if not _should_evaluate_query_variants(selected_route):
        return selected_pre, selected_entities, selected_route, selected_trace, candidates

    for variant in pre.query_variants:
        if not variant or variant == pre.clean_query:
            continue
        variant_pre = preprocess_input(variant)
        variant_entities = extract_entities(variant_pre)
        variant_route, variant_trace = route_intent(variant_pre, variant_entities)
        variant_route, variant_policy_trace = apply_routing_priority_policy(variant_pre.normalized_query, variant_route, variant_entities)
        if variant_policy_trace is not None:
            variant_trace = variant_policy_trace
        candidates.append({
            "query": variant,
            "category": variant_route.category,
            "intent": variant_route.intent,
            "confidence": variant_route.confidence,
        })
        if _route_variant_is_better(selected_route, variant_route):
            selected_pre = variant_pre
            selected_entities = variant_entities
            selected_route = variant_route
            selected_trace = variant_trace

    return selected_pre, selected_entities, selected_route, selected_trace, candidates


class AnswerQualityPipeline:
    def __init__(self) -> None:
        self.matcher = RuleMatcher.default()

    def answer(
        self,
        question: str,
        *,
        experimental_rag_fallback: bool | None = None,
        experimental_allow_llm: bool | None = None,
        global_timeout_sec: float | None = None,
    ) -> PipelineAnswer:
        with request_deadline(global_timeout_sec):
            started = time.perf_counter()
            experimental_rag_fallback = env_experimental_rag_fallback_default() if experimental_rag_fallback is None else experimental_rag_fallback
            experimental_allow_llm = env_experimental_llm_default() if experimental_allow_llm is None else experimental_allow_llm
            split_started = time.perf_counter()
            parts = _split_multi_question(question)
            initial_trace = [
                _timing_trace(
                    "split_multi_question",
                    split_started,
                    detail=f"parts={len(parts)}",
                    metadata={**deadline_metadata(), "parts": parts[:3]},
                )
            ]
            compound_profile = classify_compound(question, parts)
            initial_trace.append(PipelineTrace(
                "compound_complexity",
                compound_profile.level,
                compound_profile.score,
                compound_profile.reason,
                compound_profile.as_dict(),
            ))
            if self._deadline_is_exceeded(initial_trace, "after_split"):
                return self._timeout_result(
                    started=started,
                    trace=initial_trace,
                    stage="after_split",
                )
            planner_gate, planner_reason = should_use_query_planner(
                question,
                parts,
                force_complex=compound_profile.requires_planner,
            )
            if planner_gate:
                planner_started = time.perf_counter()
                planner, planner_trace = plan_query(
                    question,
                    parts,
                    allow_llm=experimental_allow_llm,
                    gate_reason=planner_reason,
                    timeout_cap_sec=4.0 if compound_profile.requires_planner else None,
                )
                initial_trace.append(_timing_trace(
                    "query_planner",
                    planner_started,
                    detail="accepted" if planner is not None else "fallback_to_existing_splitter",
                    metadata={"gate_reason": planner_reason},
                ))
                initial_trace.append(planner_trace)
                if planner is not None and planner.tasks:
                    planned_parts = [task.question for task in planner.tasks]
                    if len(planned_parts) > 1:
                        return self._answer_multi(
                            question,
                            planned_parts,
                            planned_tasks=list(planner.tasks),
                            experimental_rag_fallback=experimental_rag_fallback,
                            experimental_allow_llm=experimental_allow_llm,
                            pipeline_started=started,
                            initial_trace=initial_trace,
                            compound_profile=compound_profile,
                        )
                    if len(planned_parts) == 1 and planner.tasks[0].operation != "unknown":
                        return self._answer_single(
                            planned_parts[0],
                            planned_task=planner.tasks[0],
                            experimental_rag_fallback=experimental_rag_fallback,
                            experimental_allow_llm=experimental_allow_llm,
                            pipeline_started=started,
                            initial_trace=initial_trace,
                        )
            else:
                initial_trace.append(planner_skip_trace(planner_reason, allow_llm=experimental_allow_llm))
            if len(parts) > 1:
                return self._answer_multi(
                    question,
                    parts,
                    experimental_rag_fallback=experimental_rag_fallback,
                    experimental_allow_llm=experimental_allow_llm,
                    pipeline_started=started,
                    initial_trace=initial_trace,
                    compound_profile=compound_profile,
                )
            return self._answer_single(
                question,
                experimental_rag_fallback=experimental_rag_fallback,
                experimental_allow_llm=experimental_allow_llm,
                pipeline_started=started,
                initial_trace=initial_trace,
            )

    def _answer_multi(
        self,
        question: str,
        parts: list[str],
        *,
        planned_tasks: list[QueryPlanTask] | None = None,
        experimental_rag_fallback: bool,
        experimental_allow_llm: bool,
        pipeline_started: float | None = None,
        initial_trace: list[PipelineTrace] | None = None,
        compound_profile: CompoundProfile | None = None,
    ) -> PipelineAnswer:
        started = pipeline_started if pipeline_started is not None else time.perf_counter()
        trace: list[PipelineTrace] = list(initial_trace or [])
        rag_llm_attempted = False
        rag_source_conflict = False
        compound_plan = build_compound_plan(question, parts, compound_profile)
        if not any(item.stage == "compound_complexity" for item in trace):
            trace.append(PipelineTrace(
                "compound_complexity",
                compound_plan.profile.level,
                compound_plan.profile.score,
                compound_plan.profile.reason,
                compound_plan.profile.as_dict(),
            ))
        trace.append(PipelineTrace(
            "compound_plan",
            "bounded_parallel_candidate" if compound_plan.profile.can_parallelize else "ordered_dependency_chain",
            compound_plan.profile.score,
            compound_plan.profile.reason,
            compound_plan.as_dict(),
        ))
        children_started = time.perf_counter()
        display_parts = list(parts)
        parallel_allowed = (
            planned_tasks is None
            and compound_plan.profile.can_parallelize
            and self._compound_children_are_deterministic(parts)
        )
        if parallel_allowed:
            results = self._answer_multi_parallel(
                parts,
                trace=trace,
                max_workers=compound_plan.profile.max_workers,
            )
            trace.append(PipelineTrace(
                "compound_child_execution",
                "bounded_parallel",
                0.92,
                "deterministic child preflight passed; child LLM paths disabled",
                {"children": len(parts), "max_workers": compound_plan.profile.max_workers},
            ))
        else:
            results = []
            child_allow_llm = experimental_allow_llm and not compound_plan.profile.requires_planner
            previous_results: list[PipelineAnswer] = []
            for index, part in enumerate(parts, 1):
                if self._deadline_is_exceeded(trace, f"before_multi_child_{index}"):
                    return self._timeout_result(
                        started=started,
                        trace=trace,
                        stage=f"before_multi_child_{index}",
                    )
                child_question = part
                dependency_answer = self._resolve_compound_dependency(part, previous_results)
                if dependency_answer is not None:
                    if dependency_answer[0] == "clarification":
                        child_result = self._compound_dependency_clarification(
                            part,
                            dependency_answer[1],
                        )
                        trace.append(PipelineTrace(
                            "compound_dependency",
                            "clarification",
                            0.88,
                            dependency_answer[1],
                            {"part_index": index, "original_question": part},
                        ))
                        results.append(child_result)
                        previous_results.append(child_result)
                        continue
                    child_question = dependency_answer[1]
                    display_parts[index - 1] = child_question
                    trace.append(PipelineTrace(
                        "compound_dependency",
                        "reference_resolved",
                        0.86,
                        child_question,
                        {"part_index": index, "original_question": part},
                    ))
                child_result = self._answer_single(
                    child_question,
                    planned_task=(planned_tasks[index - 1] if planned_tasks and index <= len(planned_tasks) else None),
                    experimental_rag_fallback=experimental_rag_fallback,
                    experimental_allow_llm=child_allow_llm,
                )
                results.append(child_result)
                previous_results.append(child_result)
            trace.append(PipelineTrace(
                "compound_child_execution",
                "ordered_sequential",
                0.92,
                "dependency, broad query, planner output, or non-deterministic child requires ordered execution",
                {
                    "children": len(parts),
                    "max_workers": 1,
                    "child_llm_allowed": child_allow_llm,
                    "child_llm_policy": "disabled_after_complex_planner_attempt" if compound_plan.profile.requires_planner else "inherited",
                },
            ))
        if self._deadline_is_exceeded(trace, "after_multi_children"):
            return self._timeout_result(
                started=started,
                trace=trace,
                stage="after_multi_children",
            )
        trace.append(_timing_trace(
            "multi_question_children_total",
            children_started,
            detail=f"children={len(results)}",
            metadata={
                "child_elapsed_sec": [result.elapsed for result in results],
                "child_modes": [result.mode for result in results],
            },
        ))
        answer_blocks = ["คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:"]
        for index, (part, result) in enumerate(zip(display_parts, results), 1):
            answer_blocks.append(f"คำถามที่ {index}: {part}\n{result.answer}")

        parent_preprocess_started = time.perf_counter()
        pre = preprocess_input(question)
        trace.append(_timing_trace("multi_question_parent_preprocess", parent_preprocess_started))
        parent_entities_started = time.perf_counter()
        entities = extract_entities(pre)
        trace.append(_timing_trace("multi_question_parent_entities", parent_entities_started))
        route = PipelineRoute("multi_question", "multi_question_split", 0.92, "summary", "medium", "split clear multi-intent question")
        validation = ValidationResult(
            ok=all(result.validation.ok for result in results),
            errors=tuple(error for result in results for error in result.validation.errors),
            warnings=tuple(warning for result in results for warning in result.validation.warnings),
        )
        confidence = min(result.confidence for result in results)
        hits = _dedupe_hits([hit for result in results for hit in result.hits])
        trace.append(PipelineTrace(
            "multi_question",
            "split",
            0.92,
            f"parts={len(parts)}",
            {"parts": parts},
        ))
        for part, result in zip(parts, results):
            child_intent_trace = next(
                (item for item in reversed(result.trace) if item.stage == "universal_intent"),
                None,
            )
            trace.append(PipelineTrace(
                "multi_question_child",
                f"{result.route.category}/{result.route.intent}",
                result.confidence,
                part,
                {
                    "mode": result.mode,
                    "elapsed": result.elapsed,
                    "universal_intent_method": (child_intent_trace.metadata or {}).get("method") if child_intent_trace else "",
                    "universal_intent_llm_attempted": (child_intent_trace.metadata or {}).get("llm_attempted") if child_intent_trace else False,
                    "universal_intent": child_intent_trace.decision if child_intent_trace else "",
                },
            ))

        return self._build_result(
            "\n\n".join(answer_blocks),
            hits,
            started,
            "pipeline:multi_question_splitter",
            confidence,
            route,
            entities,
            validation,
            trace,
        )

    @staticmethod
    def _compound_children_are_deterministic(parts: list[str]) -> bool:
        """Preflight each child before allowing parallel execution.

        Only high-confidence, data-backed categories enter the worker pool.
        This prevents an ambiguous child from silently losing its LLM/RAG
        fallback just because another child looked simple.
        """
        safe_categories = {
            "games", "game_controls", "equipment", "reservation", "service_fee",
            "schedule", "members", "rules", "penalty", "competition_rules", "contact",
        }
        for part in parts:
            pre = preprocess_input(part)
            entities = extract_entities(pre)
            route, _route_trace = route_intent(pre, entities)
            route, _policy_trace = apply_routing_priority_policy(pre.clean_query, route, entities)
            if route.category not in safe_categories or route.confidence < 0.78:
                return False
        return True

    def _answer_multi_parallel(
        self,
        parts: list[str],
        *,
        trace: list[PipelineTrace],
        max_workers: int,
    ) -> list[PipelineAnswer]:
        if self._deadline_is_exceeded(trace, "before_bounded_parallel_children"):
            return []
        worker_count = max(1, min(max_workers, len(parts)))
        contexts = [copy_context() for _ in parts]
        executor = ThreadPoolExecutor(max_workers=worker_count, thread_name_prefix="psu-compound")
        futures = []
        try:
            for index, part in enumerate(parts):
                futures.append(executor.submit(
                    contexts[index].run,
                    self._answer_single,
                    part,
                    experimental_rag_fallback=False,
                    experimental_allow_llm=False,
                ))
            results = [future.result() for future in futures]
        finally:
            executor.shutdown(wait=False, cancel_futures=True)
        return results

    @staticmethod
    def _resolve_compound_dependency(
        question: str,
        previous_results: list[PipelineAnswer],
    ) -> tuple[str, str] | None:
        if not previous_results:
            return None
        normalized = normalize_text(question)
        reference_terms = ("เครื่องนั้น", "โซนนั้น", "เกมนั้น", "ของเกมนั้น", "อันนั้น", "อันเดิม", "รายการนั้น")
        if not _has(normalized, *reference_terms):
            return None
        previous_answer = previous_results[-1].answer
        if _has(normalized, "เกมนั้น", "ของเกมนั้น", "อันเดิม"):
            game_candidates: list[str] = []
            for hit in previous_results[-1].hits:
                metadata = hit.get("metadata") if isinstance(hit, dict) else {}
                title = str((metadata or {}).get("title") or hit.get("title") or "").strip()
                if title and not _has(normalize_text(title), "zone", "เครื่อง", "#"):
                    game_candidates.append(title)
            game_candidates = list(dict.fromkeys(game_candidates))
            if len(game_candidates) == 1:
                resolved = question
                for reference in ("ของเกมนั้น", "เกมนั้น", "อันเดิม"):
                    resolved = resolved.replace(reference, game_candidates[0])
                return "resolved", resolved
            if len(game_candidates) > 1:
                return "clarification", f"จากคำตอบข้อก่อนหน้าพบหลายเกมครับ ({' หรือ '.join(game_candidates[:5])}) ต้องการหมายถึงเกมไหนครับ?"
            return "clarification", "คำถามส่วนนี้อ้างถึงเกมจากข้อก่อนหน้า แต่ยังระบุชื่อเกมที่แน่ชัดไม่ได้ครับ ต้องการหมายถึงเกมไหนครับ?"
        labels = (
            "PlayStation 5 Zone", "Nintendo Switch Zone", "PC Zone", "VR Zone", "Cockpit Zone",
        )
        counts: dict[str, int] = {}
        for label in labels:
            match = re.search(rf"{re.escape(label)}\s*:\s*(\d+)\s*เกม", previous_answer, flags=re.IGNORECASE)
            if match:
                counts[label] = int(match.group(1))
        if counts:
            highest = max(counts.values())
            winners = [label for label, count in counts.items() if count == highest]
            if len(winners) == 1:
                resolved = question
                for reference in ("เครื่องนั้น", "โซนนั้น", "อันนั้น", "รายการนั้น"):
                    resolved = resolved.replace(reference, winners[0])
                return "resolved", resolved
            if len(winners) > 1:
                joined = " หรือ ".join(winners)
                return "clarification", f"จากคำตอบข้อก่อนหน้า มีโซนที่เกมเยอะสุดเท่ากันหลายโซนครับ ({joined}) ต้องการให้คำนวณราคาของโซนไหนครับ?"
        return "clarification", "คำถามส่วนนี้อ้างถึงผลจากข้อก่อนหน้า แต่ยังระบุเครื่องหรือโซนให้แน่ชัดไม่ได้ครับ ต้องการหมายถึงเครื่องหรือโซนไหนครับ?"

    def _compound_dependency_clarification(self, question: str, answer: str) -> PipelineAnswer:
        started = time.perf_counter()
        trace = [PipelineTrace("clarification", "compound_dependency_clarification", 0.88, question)]
        route = PipelineRoute(
            "clarification",
            "compound_dependency_clarification",
            0.88,
            "clarification",
            "low",
            "dependent child references an ambiguous prior result",
        )
        return self._build_result(
            answer,
            [],
            started,
            "pipeline:compound_dependency_clarification",
            0.88,
            route,
            EntityBundle(),
            ValidationResult(ok=True, warnings=("compound_dependency_requires_target",)),
            trace,
        )

    def _answer_single(
        self,
        question: str,
        *,
        planned_task: QueryPlanTask | None = None,
        experimental_rag_fallback: bool,
        experimental_allow_llm: bool,
        pipeline_started: float | None = None,
        initial_trace: list[PipelineTrace] | None = None,
    ) -> PipelineAnswer:
        started = pipeline_started if pipeline_started is not None else time.perf_counter()
        trace: list[PipelineTrace] = list(initial_trace or [])

        preprocess_started = time.perf_counter()
        original_pre = preprocess_input(question)
        preprocess_elapsed = time.perf_counter() - preprocess_started
        trace.append(PipelineTrace(
            "preprocess",
            "normalized",
            1.0,
            original_pre.normalized_query,
            {
                "language_hint": original_pre.language_hint,
                "query_variants": list(original_pre.query_variants),
                "elapsed_ms": round(preprocess_elapsed * 1000, 2),
                "elapsed_sec": round(preprocess_elapsed, 4),
            },
        ))
        trace.append(_timing_trace("preprocess", preprocess_started))
        route_started = time.perf_counter()
        pre, entities, route, route_trace, variant_candidates = _select_active_preprocessed_query(original_pre)
        trace.append(_timing_trace(
            "active_route_selection",
            route_started,
            detail=f"{route.category}/{route.intent}",
            metadata={
                "route_category": route.category,
                "route_intent": route.intent,
                "variant_count": len(variant_candidates),
            },
        ))
        if pre.clean_query != original_pre.clean_query:
            trace.append(PipelineTrace(
                "preprocess",
                "selected_query_variant",
                route.confidence,
                pre.clean_query,
                {
                    "original_query": original_pre.clean_query,
                    "selected_normalized": pre.normalized_query,
                    "route_category": route.category,
                    "route_intent": route.intent,
                    "candidates": variant_candidates,
                },
            ))
        elif variant_candidates:
            trace.append(PipelineTrace(
                "preprocess",
                "kept_original_query",
                route.confidence,
                pre.clean_query,
                {"candidates": variant_candidates[:4]},
            ))
        trace.append(PipelineTrace("entities", "extracted", 0.90, "", {
            "day": entities.day,
            "time_slots": list(entities.time_slots),
            "service": entities.service,
            "user_group": entities.user_group,
            "duration": entities.duration,
            "price_intent": entities.price_intent,
        }))
        if self._deadline_is_exceeded(trace, "after_route_selection"):
            return self._timeout_result(
                started=started,
                trace=trace,
                stage="after_route_selection",
                route=route,
                entities=entities,
            )

        boundary = evaluate_boundary(pre.normalized_query)
        trace.append(PipelineTrace(
            "boundary_guard",
            boundary.action,
            boundary.confidence,
            boundary.reason,
            {"flags": list(boundary.flags)},
        ))
        if boundary.action != "allow":
            boundary_route = PipelineRoute(
                "no_answer",
                f"boundary_{boundary.action}",
                boundary.confidence,
                "no_answer",
                "low",
                boundary.reason,
            )
            validation = ValidationResult(ok=True, warnings=boundary.flags)
            return self._build_result(
                boundary.answer,
                [],
                started,
                f"pipeline:boundary_{boundary.action}",
                boundary.confidence,
                boundary_route,
                entities,
                validation,
                trace,
            )

        guard_started = time.perf_counter()
        guard_answer, guard_confidence, guard_trace = guard_scope(pre, entities)
        trace.append(_timing_trace("guard_scope", guard_started))
        trace.append(guard_trace)
        if guard_answer and guard_confidence >= 0.90:
            route = PipelineRoute("no_answer", "guard_no_answer", guard_confidence, "no_answer", "low", guard_trace.detail)
            if experimental_rag_fallback:
                fallback = build_experimental_fallback(
                    pre.clean_query,
                    route,
                    started=started,
                    allow_llm=experimental_allow_llm,
                )
                trace.append(fallback.trace)
                validation = ValidationResult(ok=True, warnings=("experimental_rag_fallback_bypassed_guard_no_answer",))
                return self._build_result(
                    fallback.answer,
                    fallback.hits,
                    started,
                    "pipeline:" + fallback.mode,
                    fallback.confidence,
                    route,
                    entities,
                    validation,
                    trace,
                )
            validation = ValidationResult(ok=True)
            return self._build_result(guard_answer, HITS["reservation"], started, "pipeline:guard_no_answer", guard_confidence, route, entities, validation, trace)

        trace.append(route_trace)
        if self._deadline_is_exceeded(trace, "before_universal_intent"):
            return self._timeout_result(
                started=started,
                trace=trace,
                stage="before_universal_intent",
                route=route,
                entities=entities,
            )
        universal_started = time.perf_counter()
        preflight_allow_llm, preflight_reason = preflight_llm_allowed(route, experimental_allow_llm)
        trace.append(PipelineTrace(
            "model_gateway",
            "allow_preflight_llm" if preflight_allow_llm else "skip_preflight_llm",
            route.confidence,
            preflight_reason,
            {
                "allow_llm": experimental_allow_llm,
                "preflight_allow_llm": preflight_allow_llm,
                "route_category": route.category,
                "route_intent": route.intent,
            },
        ))
        if (
            planned_task is not None
            and planned_task.operation != "unknown"
            and planned_task.confidence >= 0.55
            and self._planned_task_matches_route(planned_task, route)
        ):
            universal_intent = planned_task.to_universal_intent()
            universal_trace = PipelineTrace(
                "universal_intent",
                f"{universal_intent.domain}/{universal_intent.operation}",
                universal_intent.confidence,
                universal_intent.reason,
                {
                    "method": "query_planner",
                    "llm_attempted": False,
                    "planner_task_id": planned_task.task_id,
                    "planner_target": planned_task.target,
                    "planner_filters": planned_task.filters,
                    "planner_needs_clarification": planned_task.needs_clarification,
                },
            )
        else:
            if planned_task is not None:
                trace.append(PipelineTrace(
                    "query_planner",
                    "task_rejected_by_route_cross_check",
                    planned_task.confidence,
                    f"planner={planned_task.domain}/{planned_task.operation}; route={route.category}/{route.intent}",
                    {"planner_task_id": planned_task.task_id},
                ))
            universal_intent, universal_trace = resolve_universal_intent(
                pre.clean_query,
                route,
                allow_llm=preflight_allow_llm,
            )
        trace.append(_timing_trace(
            "universal_intent",
            universal_started,
            detail=f"{universal_intent.domain}/{universal_intent.operation}",
            metadata={
                "method": universal_intent.method,
                "confidence": universal_intent.confidence,
            },
        ))
        trace.append(universal_trace)
        route, refined_trace = refine_route_with_universal_intent(route, universal_intent)
        if refined_trace is not None:
            trace.append(refined_trace)
        if self._deadline_is_exceeded(trace, "after_universal_intent"):
            return self._timeout_result(
                started=started,
                trace=trace,
                stage="after_universal_intent",
                route=route,
                entities=entities,
            )

        if route.intent in {"chatbot_greeting", "chatbot_identity"}:
            chatbot_fast = self._try_deterministic(pre.clean_query, route, started, trace)
            if chatbot_fast is not None:
                trace.append(PipelineTrace(
                    "chatbot_role",
                    "deterministic_fast_path",
                    chatbot_fast.confidence,
                    route.intent,
                    {"mode": chatbot_fast.mode, "llm_attempted": False},
                ))
                return self._build_result(
                    chatbot_fast.answer,
                    chatbot_fast.hits,
                    started,
                    "pipeline:" + chatbot_fast.mode,
                    chatbot_fast.confidence,
                    route,
                    entities,
                    ValidationResult(ok=True),
                    trace,
                )

        tool_router_started = time.perf_counter()
        tool_decision, tool_trace = resolve_tool_routing(
            pre.clean_query,
            route,
            universal_intent,
            allow_llm=preflight_allow_llm,
        )
        trace.append(_timing_trace(
            "tool_router",
            tool_router_started,
            detail=f"{tool_decision.action}/{tool_decision.domain}",
            metadata={
                "method": tool_decision.method,
                "confidence": tool_decision.confidence,
            },
        ))
        trace.append(tool_trace)
        if self._deadline_is_exceeded(trace, "after_tool_router"):
            return self._timeout_result(
                started=started,
                trace=trace,
                stage="after_tool_router",
                route=route,
                entities=entities,
            )
        early_candidate_rejected = False
        if (
            tool_decision.action in {"retrieval", "rag_llm", "vector"}
            and route.category in {"general", "unknown", "no_answer"}
            and tool_decision.confidence >= 0.68
            and tool_decision.domain in TOOL_ROUTER_DOMAIN_ROUTE_MAP
        ):
            mapped_category, mapped_intent, mapped_answer_type, mapped_risk = TOOL_ROUTER_DOMAIN_ROUTE_MAP[tool_decision.domain]
            old_route = route
            route = PipelineRoute(
                mapped_category,
                mapped_intent,
                max(route.confidence, min(tool_decision.confidence, 0.84)),
                mapped_answer_type,
                mapped_risk,
                f"{route.reason}; tool_router={tool_decision.action}/{tool_decision.domain}",
            )
            trace.append(PipelineTrace(
                "tool_route_refine",
                f"{old_route.category}/{old_route.intent} -> {route.category}/{route.intent}",
                tool_decision.confidence,
                "route refined by LLM tool router for retrieval",
                {
                    "action": tool_decision.action,
                    "domain": tool_decision.domain,
                    "operation": tool_decision.operation,
                    "method": tool_decision.method,
                },
            ))
        elif (
            tool_decision.action == "clarification"
            and tool_decision.method == "llm"
            and tool_decision.confidence >= 0.78
            and route.confidence < 0.86
        ):
            clarify_route = PipelineRoute("clarification", "tool_router_clarification", tool_decision.confidence, "clarification", "low", tool_decision.reason)
            answer = "ขอรายละเอียดเพิ่มนิดนึงครับ คำถามนี้หมายถึงเรื่องไหนใน PSU Esports Studio เช่น เกม อุปกรณ์ การจอง ตารางเวลา หรือกติกาการแข่งขัน?"
            validation = ValidationResult(ok=True, warnings=("tool_router_requested_clarification",))
            trace.append(PipelineTrace("clarification", "tool_router_clarification", tool_decision.confidence, tool_decision.reason))
            candidates_started = time.perf_counter()
            _accepted_candidates, _rejected_candidates, candidate_trace = build_candidate_decisions(
                clarify_route,
                universal_intent,
                tool_decision,
                pre.clean_query,
            )
            trace.append(_timing_trace("candidate_decisions", candidates_started, detail="tool_router_clarification"))
            trace.append(candidate_trace)
            return self._build_result(
                answer,
                [],
                started,
                "pipeline:tool_router_clarification",
                tool_decision.confidence,
                clarify_route,
                entities,
                validation,
                trace,
            )

        ambiguity_started = time.perf_counter()
        ambiguity = evaluate_ambiguity_gate(
            pre.clean_query,
            route=route,
            intent=universal_intent,
            entities=entities,
            tool_decision=tool_decision,
        )
        trace.append(_timing_trace(
            "ambiguity_gate",
            ambiguity_started,
            detail=ambiguity.action,
            metadata={
                "flags": list(ambiguity.flags),
                "confidence": ambiguity.confidence,
            },
        ))
        trace.append(ambiguity.trace())
        if not ambiguity.allows_answer:
            is_control_missing_game = (
                "control_query_missing_game_target" in ambiguity.flags
                or "bare_play_howto_missing_domain_or_game" in ambiguity.flags
            )
            clarify_route = PipelineRoute(
                "games" if is_control_missing_game else "clarification",
                "game_control_lookup" if is_control_missing_game else "ambiguity_gate_clarification",
                ambiguity.confidence,
                "clarification",
                "low",
                ambiguity.reason,
            )
            validation = ValidationResult(ok=True, warnings=tuple(ambiguity.flags))
            return self._build_result(
                ambiguity.answer,
                ambiguity.hits,
                started,
                "pipeline:game_control_missing_game_context" if is_control_missing_game else "pipeline:ambiguity_clarification",
                ambiguity.confidence,
                clarify_route,
                entities,
                validation,
                trace,
            )
        if self._deadline_is_exceeded(trace, "after_ambiguity_gate"):
            return self._timeout_result(
                started=started,
                trace=trace,
                stage="after_ambiguity_gate",
                route=route,
                entities=entities,
            )

        frame_started = time.perf_counter()
        question_frame = build_question_frame(pre.clean_query, route, universal_intent)
        trace.append(_timing_trace(
            "question_frame",
            frame_started,
            detail=f"{question_frame.domain}/{question_frame.operation}",
            metadata=question_frame.as_dict(),
            confidence=question_frame.confidence,
        ))
        if (
            not universal_intent.target
            and question_frame.target_status == "exact"
            and len(question_frame.targets) == 1
        ):
            resolved_target = question_frame.targets[0]
            universal_intent = UniversalIntent(
                domain=universal_intent.domain,
                operation=universal_intent.operation,
                target=resolved_target.label,
                filters={
                    **universal_intent.filters,
                    "resolved_target_id": resolved_target.target_id,
                    "resolved_target_type": resolved_target.target_type,
                },
                needs=universal_intent.needs,
                answer_style=universal_intent.answer_style,
                confidence=universal_intent.confidence,
                method=universal_intent.method,
                reason=universal_intent.reason,
            )
            trace.append(PipelineTrace(
                "target_context",
                "enrich_universal_intent",
                resolved_target.score,
                "exact Question Frame target propagated to structured execution",
                resolved_target.as_dict(),
            ))

        operation_route_map = {
            "reservation": ("reservation", "booking_policy", "fact", "medium"),
            "service_fee": ("service_fee", "service_fee_query", "fact", "medium"),
            "schedule": ("schedule", "schedule_query", "fact", "medium"),
            "games": ("games", "games_lookup", "list", "low"),
            "game_controls": ("games", "game_control_lookup", "fact", "low"),
            "equipment": ("equipment", "equipment_lookup", "list", "low"),
            "members": ("members", "members_lookup", "fact", "low"),
            "competition_rules": ("competition_rules", "competition_rules_lookup", "fact", "medium"),
        }
        if (
            route.category in {"general", "unknown", "no_answer"}
            and question_frame.domain in operation_route_map
            and question_frame.confidence >= 0.85
        ):
            old_route = route
            category, route_intent, answer_type, risk = operation_route_map[question_frame.domain]
            route = PipelineRoute(
                category,
                route_intent,
                max(route.confidence, min(question_frame.confidence, 0.92)),
                answer_type,
                risk,
                f"{route.reason}; operation_first={question_frame.operation}",
            )
            trace.append(PipelineTrace(
                "operation_route_refine",
                f"{old_route.category}/{old_route.intent} -> {route.category}/{route.intent}",
                question_frame.confidence,
                "question frame supplied a clear PSU operation domain",
                question_frame.as_dict(),
            ))

        candidates_started = time.perf_counter()
        accepted_candidates, _rejected_candidates, candidate_trace = build_candidate_decisions(
            route,
            universal_intent,
            tool_decision,
            pre.clean_query,
        )
        trace.append(_timing_trace("candidate_decisions", candidates_started))
        trace.append(candidate_trace)
        selected_candidate = accepted_candidates[0] if accepted_candidates else None
        selected_capability_id = selected_candidate.capability_id if selected_candidate is not None else "fallback.no_answer"
        selected_action = selected_candidate.action if selected_candidate is not None else "no_answer"
        selection = candidate_trace.metadata.get("selection", {})
        if (
            selected_capability_id == "retrieval.competition_fact_cards"
            and route.category != "competition_rules"
        ):
            old_route = route
            route = PipelineRoute(
                "competition_rules",
                "competition_rules_lookup",
                max(route.confidence, question_frame.confidence, 0.78),
                "fact",
                "medium",
                f"{route.reason}; candidate_selector=competition_fact_cards",
            )
            trace.append(PipelineTrace(
                "candidate_route_refine",
                f"{old_route.category}/{old_route.intent} -> competition_rules/competition_rules_lookup",
                route.confidence,
                "operation-first frame selected competition fact retrieval",
                {"selected_capability_id": selected_capability_id},
            ))
        if self._deadline_is_exceeded(trace, "after_candidate_decisions"):
            return self._timeout_result(
                started=started,
                trace=trace,
                stage="after_candidate_decisions",
                route=route,
                entities=entities,
            )
        if not bool(selection.get("execution_allowed", True)) and question_frame.operation == "unknown":
            clarify_route = PipelineRoute(
                "clarification",
                "candidate_margin_clarification",
                0.62,
                "clarification",
                "low",
                "capability candidates are too close and operation is unknown",
            )
            answer = "ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?"
            validation = ValidationResult(ok=True, warnings=("candidate_selection_abstained",))
            trace.append(PipelineTrace(
                "candidate_selector",
                "abstain_and_clarify",
                0.62,
                str(selection.get("status") or "review_required"),
                {"selected_capability_id": selected_capability_id, "selection": selection},
            ))
            return self._build_result(
                answer,
                [],
                started,
                "pipeline:candidate_margin_clarification",
                0.62,
                clarify_route,
                entities,
                validation,
                trace,
            )

        if (
            route.category == "service_fee"
            and entities.service
            and universal_intent.operation in {"price_calculate", "price_lookup"}
            and not has_explicit_game_hint(pre.clean_query)
            and selected_capability_id == "fast.price_calculator"
        ):
            early_started = time.perf_counter()
            deterministic = self._try_deterministic(pre.clean_query, route, started, trace)
            trace.append(_timing_trace(
                "early_price_deterministic",
                early_started,
                detail=deterministic.mode if deterministic is not None else "no_match",
                metadata={"confidence": deterministic.confidence if deterministic is not None else 0.0},
            ))
            if deterministic is not None and deterministic.confidence >= 0.75:
                format_started = time.perf_counter()
                formatted = format_answer(deterministic.answer, deterministic.hits, route, entities)
                trace.append(_timing_trace("format_answer", format_started, detail=deterministic.mode))
                validation_started = time.perf_counter()
                validation = validate_answer(
                    pre.clean_query,
                    formatted,
                    route,
                    entities,
                    hits=deterministic.hits,
                    mode="pipeline:" + deterministic.mode,
                    intent=universal_intent,
                )
                trace.append(_timing_trace(
                    "validation",
                    validation_started,
                    detail="ok" if validation.ok else "failed",
                    metadata={
                        "error_count": len(validation.errors),
                        "warning_count": len(validation.warnings),
                    },
                    confidence=1.0 if validation.ok else 0.30,
                ))
                trace.append(PipelineTrace(
                    "candidate_execution",
                    "early_price_fast_path",
                    deterministic.confidence,
                    "clear service fee query selected by candidate scoring",
                    {
                        "service": entities.service,
                        "mode": deterministic.mode,
                        "selected_capability_id": selected_capability_id,
                    },
                ))
                trace.append(PipelineTrace("validation", "ok" if validation.ok else "failed", 1.0 if validation.ok else 0.30, "; ".join(validation.errors + validation.warnings)))
                if validation.ok:
                    return self._build_result(
                        formatted,
                        deterministic.hits,
                        started,
                        "pipeline:" + deterministic.mode,
                        deterministic.confidence,
                        route,
                        entities,
                        validation,
                        trace,
                    )
                early_candidate_rejected = True
                trace.append(PipelineTrace(
                    "repair_controller",
                    "retry_next_candidate",
                    0.55,
                    "fast price draft rejected by answer contract",
                    {
                        "attempt": 1,
                        "max_attempts": 1,
                        "rejected_capability_id": selected_capability_id,
                        "errors": list(validation.errors),
                    },
                ))

        precondition_started = time.perf_counter()
        structured_precondition = evaluate_structured_tool_precondition(pre.clean_query, route, universal_intent)
        selector_allows_structured = selected_action == "structured" or early_candidate_rejected
        trace.append(_timing_trace(
            "tool_precondition",
            precondition_started,
            detail=structured_precondition.capability_id,
            metadata={"ok": structured_precondition.ok},
        ))
        trace.append(PipelineTrace(
            "tool_precondition",
            "allow_structured" if structured_precondition.ok and selector_allows_structured else "reject_structured",
            0.90 if structured_precondition.ok and selector_allows_structured else 0.20,
            structured_precondition.reason if selector_allows_structured else "candidate_selector_preferred_non_structured_action",
            {
                **structured_precondition.as_dict(),
                "selector_allows_structured": selector_allows_structured,
                "selected_capability_id": selected_capability_id,
            },
        ))
        structured_started = time.perf_counter()
        structured = None
        if structured_precondition.ok and selector_allows_structured:
            structured = answer_with_structured_tool(pre.clean_query, route, universal_intent, started=started)
        trace.append(_timing_trace(
            "structured_tool_execution",
            structured_started,
            detail=structured.mode if structured is not None else "no_result",
            metadata={
                "precondition_ok": structured_precondition.ok,
                "selector_allows_structured": selector_allows_structured,
                "selected_capability_id": selected_capability_id,
                "confidence": structured.confidence if structured is not None else 0.0,
            },
        ))
        if structured_precondition.ok and selector_allows_structured and structured is None:
            trace.append(PipelineTrace(
                "candidate_execution",
                "structured_no_result",
                0.42,
                "structured tool passed precondition but returned no answer",
                {"capability_id": structured_precondition.capability_id},
            ))
        if structured is not None and structured.confidence >= 0.82:
            structured_route = self._route_for_structured_result(route, universal_intent, structured.mode)
            composer_started = time.perf_counter()
            composed = compose_structured_answer(
                question=pre.clean_query,
                draft_answer=structured.answer,
                evidence=structured.evidence,
                route=structured_route,
                intent=universal_intent,
                mode=structured.mode,
                allow_llm=experimental_allow_llm,
            )
            trace.append(_timing_trace(
                "facts_composer",
                composer_started,
                detail=composed.trace.decision,
                metadata={"used_llm": composed.used_llm},
            ))
            if composed.trace.decision != "disabled":
                trace.append(composed.trace)
            format_started = time.perf_counter()
            formatted = format_answer(composed.answer, structured.hits, structured_route, entities)
            trace.append(_timing_trace("format_answer", format_started, detail=structured.mode))
            validation_started = time.perf_counter()
            validation = validate_answer(
                pre.clean_query,
                formatted,
                structured_route,
                entities,
                hits=structured.hits,
                mode="pipeline:" + structured.mode,
                intent=universal_intent,
            )
            trace.append(_timing_trace(
                "validation",
                validation_started,
                detail="ok" if validation.ok else "failed",
                metadata={
                    "error_count": len(validation.errors),
                    "warning_count": len(validation.warnings),
                },
                confidence=1.0 if validation.ok else 0.30,
            ))
            trace.append(PipelineTrace(
                "structured_tool",
                structured.mode,
                structured.confidence,
                str(structured.evidence.get("tool") or structured.mode),
                {**structured.evidence, "facts_composer_used": composed.used_llm},
            ))
            trace.append(PipelineTrace("validation", "ok" if validation.ok else "failed", 1.0 if validation.ok else 0.30, "; ".join(validation.errors + validation.warnings)))
            if validation.ok:
                return self._build_result(
                    formatted,
                    structured.hits,
                    started,
                    "pipeline:" + structured.mode,
                    structured.confidence,
                    structured_route,
                    entities,
                    validation,
                    trace,
                )
            trace.append(PipelineTrace(
                "candidate_execution",
                "structured_rejected_by_validator",
                0.30,
                "; ".join(validation.errors),
                {
                    "mode": structured.mode,
                    "capability_id": structured_precondition.capability_id,
                    "validation_errors": list(validation.errors),
                    "validation_warnings": list(validation.warnings),
                },
            ))
            trace.append(PipelineTrace(
                "repair_controller",
                "retry_next_candidate",
                0.55,
                "structured draft rejected by answer contract",
                {
                    "attempt": 1,
                    "max_attempts": 1,
                    "rejected_capability_id": selected_capability_id,
                    "errors": list(validation.errors),
                },
            ))
            # Mark the rejected draft as exhausted so the single bounded retry
            # can execute the next deterministic candidate.
            structured = None

        if _looks_like_unclear_game_meta_query(pre.clean_query) and not has_explicit_game_hint(pre.clean_query):
            game_route = PipelineRoute("games", "game_meta_clarification", 0.74, "clarification", "low", "broad game meta query without specific game")
            answer = (
                "ถามเรื่องเกมได้ครับ แต่คำถามนี้ยังกว้างเกินไป เลยไม่ขอดึงเกมใดเกมหนึ่งมาตอบแทน\n\n"
                "ตัวอย่างที่ถามได้:\n"
                "- `มีเกมอะไรบ้าง`\n"
                "- `PS5 มีเกมอะไรบ้าง`\n"
                "- `TEKKEN 8 คือเกมอะไร`\n"
                "- `TEKKEN 8 มีปุ่มอะไรบ้าง`\n"
                "- `Nintendo Switch มีเกมแนวปาร์ตี้ไหม`"
            )
            validation = ValidationResult(ok=True, warnings=("game_meta_query_needs_specific_intent",))
            trace.append(PipelineTrace("clarification", "game_meta_query_missing_intent", 0.74, "broad game meta query skips retrieval"))
            return self._build_result(
                answer,
                HITS["our_games"],
                started,
                "pipeline:game_meta_clarification",
                0.74,
                game_route,
                entities,
                validation,
                trace,
            )

        if (
            (looks_like_game_control_query(pre.clean_query) or _looks_like_game_play_followup(pre.clean_query))
            and not has_explicit_game_hint(pre.clean_query)
            and not _looks_like_equipment_location_query(pre.clean_query)
            and route.category not in {"rules", "penalty"}
            and universal_intent.domain not in {"rules", "penalty"}
        ):
            named_game = _known_named_game_without_control_data(pre.clean_query)
            if named_game is not None:
                control_route = PipelineRoute("games", "game_control_lookup", 0.78, "no_answer", "low", "named game has no verified control data")
                answer = (
                    f"ยังไม่พบข้อมูลปุ่มควบคุมของ {named_game} ที่ยืนยันได้ในฐานข้อมูลของศูนย์ตอนนี้ครับ\n"
                    "ถ้าต้องการถามว่าเกมนี้มีให้เล่นในศูนย์ไหม หรือเป็นเกมแนวไหน สามารถถามต่อได้เลย"
                )
                validation = ValidationResult(ok=True, warnings=("game_control_named_game_no_verified_data",))
                trace.append(PipelineTrace("clarification", "named_game_without_control_data", 0.78, named_game))
                return self._build_result(
                    answer,
                    [],
                    started,
                    "pipeline:game_control_named_no_data",
                    0.78,
                    control_route,
                    entities,
                    validation,
                    trace,
                )
            control_route = PipelineRoute("games", "game_control_lookup", 0.72, "clarification", "low", "control query without explicit game")
            answer = (
                "ยังไม่แน่ใจว่าหมายถึงเกมไหนครับ จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน\n"
                "ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III\n"
                "ให้พิมพ์ชื่อเกมมาด้วย เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง`, `Mario Kart 8 Deluxe ใช้จอยยังไง` "
                "หรือถ้าเพิ่งถามชื่อเกมไปก่อนหน้า ให้ถามต่อใน session เดิมได้ครับ"
            )
            validation = ValidationResult(ok=True, warnings=("game_control_needs_game_context",))
            trace.append(PipelineTrace("clarification", "game_control_missing_game", 0.72, "control query has no explicit game hint"))
            return self._build_result(
                answer,
                [],
                started,
                "pipeline:game_control_missing_game_context",
                0.72,
                control_route,
                entities,
                validation,
                trace,
            )

        if (
            route.category in {"games", "equipment", "general", "unknown"}
            and looks_like_game_control_query(pre.clean_query)
            and universal_intent.domain not in {"rules", "penalty"}
        ):
            control_route = route
            if route.category in {"general", "unknown"}:
                control_route = PipelineRoute("games", "game_control_lookup", 0.82, "fact", "low", "control/button terms use guarded game control vector")
            vector_started = time.perf_counter()
            vector_hits, vector_trace = retrieve_vector_guarded(pre.clean_query, control_route, limit=8)
            trace.append(_timing_trace(
                "vector_retrieval",
                vector_started,
                detail="game_control_vector_first",
                metadata={"hit_count": len(vector_hits)},
            ))
            trace.append(vector_trace)
            control_hits = [hit for hit in vector_hits if hit.get("category") == "game_controls"]
            vector_answer_started = time.perf_counter()
            vector_answer, vector_raw_hits, vector_confidence = answer_from_vector_hits(control_hits, pre.clean_query)
            trace.append(_timing_trace(
                "vector_answer",
                vector_answer_started,
                detail="game_control_vector_first",
                metadata={"raw_hit_count": len(vector_raw_hits), "confidence": vector_confidence},
            ))
            if vector_answer and vector_confidence >= 0.68:
                formatted = format_answer(vector_answer, vector_raw_hits, control_route, entities)
                validation = validate_answer(
                    pre.clean_query,
                    formatted,
                    control_route,
                    entities,
                    hits=vector_raw_hits,
                    mode="pipeline:game_control_vector_first",
                    intent=universal_intent,
                )
                trace.append(PipelineTrace("llm_rewrite", "skipped_game_control_vector_first", vector_confidence, "control/button query uses guarded vector before deterministic game summary"))
                trace.append(PipelineTrace("validation", "ok" if validation.ok else "failed", 1.0 if validation.ok else 0.30, "; ".join(validation.errors + validation.warnings)))
                if validation.ok:
                    return self._build_result(
                        formatted,
                        vector_raw_hits,
                        started,
                        "pipeline:game_control_vector_first",
                        vector_confidence,
                        control_route,
                        entities,
                        validation,
                        trace,
                    )

        deterministic_started = time.perf_counter()
        selector_allows_deterministic = (
            (selected_action in {"fast_path", "rulebase"} and not early_candidate_rejected)
            or (selector_allows_structured and structured is None)
            or selected_action == "no_answer"
        )
        deterministic = self._try_deterministic(pre.clean_query, route, started, trace) if selector_allows_deterministic else None
        trace.append(_timing_trace(
            "deterministic",
            deterministic_started,
            detail=deterministic.mode if deterministic is not None else "no_match",
            metadata={
                "confidence": deterministic.confidence if deterministic is not None else 0.0,
                "selector_allows_deterministic": selector_allows_deterministic,
                "selected_capability_id": selected_capability_id,
            },
        ))
        if deterministic is not None and deterministic.confidence >= 0.75:
            if route.category == "games" and deterministic.mode in {"games_unknown_fast_path", "games_detail_unknown_no_answer_fast_path"}:
                vector_started = time.perf_counter()
                vector_hits, vector_trace = retrieve_vector_guarded(pre.clean_query, route)
                trace.append(_timing_trace(
                    "vector_retrieval",
                    vector_started,
                    detail="unknown_game_override",
                    metadata={"hit_count": len(vector_hits)},
                ))
                trace.append(vector_trace)
                vector_answer_started = time.perf_counter()
                vector_answer, vector_raw_hits, vector_confidence = answer_from_vector_hits(vector_hits, pre.clean_query)
                trace.append(_timing_trace(
                    "vector_answer",
                    vector_answer_started,
                    detail="unknown_game_override",
                    metadata={"raw_hit_count": len(vector_raw_hits), "confidence": vector_confidence},
                ))
                if vector_answer and vector_confidence >= 0.68:
                    formatted = format_answer(vector_answer, vector_raw_hits, route, entities)
                    validation = validate_answer(
                        pre.clean_query,
                        formatted,
                        route,
                        entities,
                        hits=vector_raw_hits,
                        mode="pipeline:guarded_vector_override_unknown_game",
                        intent=universal_intent,
                    )
                    trace.append(PipelineTrace("llm_rewrite", "skipped_guarded_vector_override_unknown_game", vector_confidence, deterministic.mode))
                    trace.append(PipelineTrace("validation", "ok" if validation.ok else "failed", 1.0 if validation.ok else 0.30, "; ".join(validation.errors + validation.warnings)))
                    if validation.ok:
                        return self._build_result(
                            formatted,
                            vector_raw_hits,
                            started,
                            "pipeline:guarded_vector_override_unknown_game",
                            vector_confidence,
                            route,
                            entities,
                            validation,
                            trace,
                        )
            deterministic_no_answerish = (
                "no_answer" in deterministic.mode
            )
            if experimental_rag_fallback and deterministic_no_answerish and deterministic.confidence < 0.90:
                trace.append(PipelineTrace("experimental_rag_fallback", "skip_deterministic_no_answer", 0.62, deterministic.mode))
            else:
                format_started = time.perf_counter()
                formatted = format_answer(deterministic.answer, deterministic.hits, route, entities)
                trace.append(_timing_trace("format_answer", format_started, detail=deterministic.mode))
                validation_started = time.perf_counter()
                validation = validate_answer(
                    pre.clean_query,
                    formatted,
                    route,
                    entities,
                    hits=deterministic.hits,
                    mode="pipeline:" + deterministic.mode,
                    intent=universal_intent,
                )
                trace.append(_timing_trace(
                    "validation",
                    validation_started,
                    detail="ok" if validation.ok else "failed",
                    metadata={
                        "error_count": len(validation.errors),
                        "warning_count": len(validation.warnings),
                    },
                    confidence=1.0 if validation.ok else 0.30,
                ))
                trace.append(PipelineTrace("validation", "ok" if validation.ok else "failed", 1.0 if validation.ok else 0.30, "; ".join(validation.errors + validation.warnings)))
                if validation.ok:
                    return self._build_result(
                        formatted,
                        deterministic.hits,
                        started,
                        "pipeline:" + deterministic.mode,
                        deterministic.confidence,
                        route,
                        entities,
                        validation,
                        trace,
                    )

        if route.category == "competition_rules":
            fact_retrieval_started = time.perf_counter()
            fact_hits, fact_trace = retrieve_competition_fact_cards(pre.clean_query)
            trace.append(_timing_trace(
                "competition_fact_retrieval",
                fact_retrieval_started,
                metadata={"hit_count": len(fact_hits)},
            ))
            trace.append(fact_trace)
            fact_answer_started = time.perf_counter()
            fact_answer, fact_raw_hits, fact_confidence = answer_from_competition_fact_hits(fact_hits, pre.clean_query)
            trace.append(_timing_trace(
                "competition_fact_answer",
                fact_answer_started,
                metadata={"raw_hit_count": len(fact_raw_hits), "confidence": fact_confidence},
            ))
            if fact_answer and fact_confidence >= 0.72:
                formatted = format_answer(fact_answer, fact_raw_hits, route, entities)
                validation = validate_answer(
                    pre.clean_query,
                    formatted,
                    route,
                    entities,
                    hits=fact_raw_hits,
                    mode="pipeline:competition_fact_card",
                    intent=universal_intent,
                )
                trace.append(PipelineTrace("llm_rewrite", "skipped_fact_card", fact_confidence, "LLM not needed for competition fact card"))
                trace.append(PipelineTrace("validation", "ok" if validation.ok else "failed", 1.0 if validation.ok else 0.30, "; ".join(validation.errors + validation.warnings)))
                if validation.ok:
                    return self._build_result(
                        formatted,
                        fact_raw_hits,
                        started,
                        "pipeline:competition_fact_card",
                        fact_confidence,
                        route,
                        entities,
                        validation,
                        trace,
                    )

        hybrid_retrieval_ran = False
        hybrid_hits_for_reuse: list[dict[str, Any]] = []
        if should_use_hybrid_retrieval(route):
            hybrid_retrieval_ran = True
            hybrid_retrieval_started = time.perf_counter()
            hybrid_hits, hybrid_trace = retrieve_hybrid_guarded(pre.clean_query, route)
            hybrid_hits_for_reuse = list(hybrid_hits)
            trace.append(_timing_trace(
                "hybrid_retrieval",
                hybrid_retrieval_started,
                metadata={"hit_count": len(hybrid_hits)},
            ))
            trace.append(hybrid_trace)
            hybrid_timings = hybrid_trace.metadata.get("timings_ms") if isinstance(hybrid_trace.metadata, dict) else {}
            for stage_name, stage_ms in (hybrid_timings or {}).items():
                trace.append(PipelineTrace(
                    "timing",
                    str(stage_name),
                    0.70,
                    "hybrid retrieval substage",
                    {"elapsed_ms": round(float(stage_ms or 0.0), 2)},
                ))
            hybrid_answer_started = time.perf_counter()
            hybrid_answer, hybrid_raw_hits, hybrid_confidence = answer_from_hybrid_hits(hybrid_hits, pre.clean_query)
            trace.append(_timing_trace(
                "hybrid_answer",
                hybrid_answer_started,
                metadata={"raw_hit_count": len(hybrid_raw_hits), "confidence": hybrid_confidence},
            ))
            if hybrid_answer and hybrid_confidence >= 0.68:
                source_quality = hybrid_trace.metadata.get("source_quality") or {}
                rag_source_conflict = bool(source_quality.get("conflict"))
                model_plan = plan_rag_model_path(
                    query=pre.clean_query,
                    route=route,
                    allow_llm=experimental_allow_llm,
                    hit_count=len(hybrid_hits),
                    retrieval_confidence=hybrid_confidence,
                    source_conflict=bool((hybrid_trace.metadata.get("source_quality") or {}).get("conflict")),
                )
                trace.append(PipelineTrace(
                    "model_gateway",
                    model_plan.path,
                    0.88 if model_plan.use_llm else 0.76,
                    model_plan.reason,
                    model_plan.as_dict(),
                ))
                evidence_started = time.perf_counter()
                evidence = pack_evidence(
                    pre.clean_query,
                    hybrid_hits,
                    max_items=max(1, int(os.getenv("PSU_RAG_EVIDENCE_MAX_ITEMS", "4"))),
                    max_chars=max(1200, int(os.getenv("PSU_RAG_EVIDENCE_MAX_CHARS", "4200"))),
                )
                trace.append(_timing_trace(
                    "evidence_packer",
                    evidence_started,
                    metadata={"item_count": evidence["item_count"]},
                ))
                trace.append(PipelineTrace(
                    "evidence_packer",
                    "packed",
                    min(0.95, 0.60 + (evidence["item_count"] / 10)),
                    f"items={evidence['item_count']} chars={sum(len(str(item.get('text') or '')) for item in evidence['items'])}",
                    evidence,
                ))
                composer = None
                if model_plan.use_llm:
                    rag_llm_attempted = True
                    composer_started = time.perf_counter()
                    composer = compose_structured_answer(
                        question=pre.clean_query,
                        draft_answer=hybrid_answer,
                        evidence=evidence,
                        route=route,
                        intent=universal_intent,
                        mode="hybrid_guarded_rerank",
                        allow_llm=True,
                    )
                    trace.append(_timing_trace(
                        "rag_llm_composer",
                        composer_started,
                        detail=composer.trace.decision,
                        metadata={"used_llm": composer.used_llm, "model_path": model_plan.path},
                    ))
                    trace.append(composer.trace)
                answer = composer.answer if composer is not None else hybrid_answer
                formatted = format_answer(answer, hybrid_raw_hits, route, entities)
                validation = validate_answer(
                    pre.clean_query,
                    formatted,
                    route,
                    entities,
                    hits=hybrid_raw_hits,
                    mode="pipeline:hybrid_guarded_rerank",
                    intent=universal_intent,
                )
                trace.append(PipelineTrace(
                    "llm_rewrite",
                    "grounded_composer" if composer is not None and composer.used_llm else "skipped_hybrid_rerank",
                    hybrid_confidence,
                    "RAG evidence was packed and optionally composed by the gated Local LLM",
                    {"composer_used": bool(composer is not None and composer.used_llm)},
                ))
                trace.append(PipelineTrace("validation", "ok" if validation.ok else "failed", 1.0 if validation.ok else 0.30, "; ".join(validation.errors + validation.warnings)))
                if validation.ok:
                    return self._build_result(
                        formatted,
                        hybrid_raw_hits,
                        started,
                        "pipeline:hybrid_guarded_rerank",
                        hybrid_confidence,
                        route,
                        entities,
                        validation,
                        trace,
                    )
            if should_skip_legacy_curated_after_hybrid(route):
                fallback = format_no_answer(route.category)
                validation = ValidationResult(ok=True, warnings=("hybrid_guard_no_verified_context",))
                trace.append(PipelineTrace("fallback", "hybrid_guard_no_verified_context", 0.56, "high-risk category skips legacy curated direct answer when hybrid guard fails"))
                return self._build_result(fallback, HITS["reservation"], started, "pipeline:no_answer", 0.56, route, entities, validation, trace)

        if route.category == "general":
            if self._deadline_is_exceeded(trace, "before_general_fallback"):
                return self._timeout_result(
                    started=started,
                    trace=trace,
                    stage="before_general_fallback",
                    route=route,
                    entities=entities,
                )
            if experimental_rag_fallback:
                experimental_started = time.perf_counter()
                fallback = build_experimental_fallback(
                    pre.clean_query,
                    route,
                    started=started,
                    allow_llm=experimental_allow_llm,
                )
                trace.append(_timing_trace(
                    "experimental_fallback",
                    experimental_started,
                    detail=fallback.mode,
                    metadata={"confidence": fallback.confidence},
                ))
                trace.append(fallback.trace)
                validation = ValidationResult(ok=True, warnings=("experimental_rag_fallback_general_route",))
                return self._build_result(
                    fallback.answer,
                    fallback.hits,
                    started,
                    "pipeline:" + fallback.mode,
                    fallback.confidence,
                    route,
                    entities,
                    validation,
                    trace,
                )
            fallback = format_no_answer(route.category)
            validation = ValidationResult(ok=True, warnings=("fallback_general_route_no_curated_guessing",))
            trace.append(PipelineTrace("fallback", "general_route_no_curated_guessing", 0.55, "general route skips curated retrieval to avoid weak-context guessing"))
            return self._build_result(fallback, [], started, "pipeline:no_answer", 0.55, route, entities, validation, trace)

        curated_started = time.perf_counter()
        rag_hits, rag_trace = retrieve_curated(pre.clean_query, route.category)
        trace.append(_timing_trace(
            "curated_retrieval",
            curated_started,
            metadata={"hit_count": len(rag_hits), "category": route.category},
        ))
        trace.append(rag_trace)
        curated_answer_started = time.perf_counter()
        rag_answer, rag_raw_hits, rag_confidence = answer_from_curated_hits(rag_hits, pre.clean_query)
        trace.append(_timing_trace(
            "curated_answer",
            curated_answer_started,
            metadata={"raw_hit_count": len(rag_raw_hits), "confidence": rag_confidence},
        ))
        if rag_answer and rag_confidence >= 0.65:
            formatted = format_answer(rag_answer, rag_raw_hits, route, entities)
            validation = validate_answer(
                pre.clean_query,
                formatted,
                route,
                entities,
                hits=rag_raw_hits,
                mode="pipeline:rag_direct_curated",
                intent=universal_intent,
            )
            trace.append(PipelineTrace("llm_rewrite", "skipped_curated_direct", rag_confidence, "LLM not needed for curated fact"))
            trace.append(PipelineTrace("validation", "ok" if validation.ok else "failed", 1.0 if validation.ok else 0.30, "; ".join(validation.errors + validation.warnings)))
            if validation.ok:
                return self._build_result(formatted, rag_raw_hits, started, "pipeline:rag_direct_curated", rag_confidence, route, entities, validation, trace)

        vector_started = time.perf_counter()
        if hybrid_retrieval_ran:
            vector_hits = hybrid_hits_for_reuse
            vector_trace = PipelineTrace(
                "vector_retrieval",
                "reused_hybrid_hits",
                0.70 if vector_hits else 0.0,
                "reuse guarded hybrid retrieval results; avoid duplicate vector scan",
                {"reused": True, "hit_count": len(vector_hits)},
            )
        else:
            vector_hits, vector_trace = retrieve_vector_guarded(pre.clean_query, route)
        trace.append(_timing_trace(
            "vector_retrieval",
            vector_started,
            detail="guarded_vector_direct",
            metadata={"hit_count": len(vector_hits)},
        ))
        trace.append(vector_trace)
        vector_answer_started = time.perf_counter()
        vector_answer, vector_raw_hits, vector_confidence = answer_from_vector_hits(vector_hits, pre.clean_query)
        trace.append(_timing_trace(
            "vector_answer",
            vector_answer_started,
            detail="guarded_vector_direct",
            metadata={"raw_hit_count": len(vector_raw_hits), "confidence": vector_confidence},
        ))
        if vector_answer and vector_confidence >= 0.68:
            formatted = format_answer(vector_answer, vector_raw_hits, route, entities)
            validation = validate_answer(
                pre.clean_query,
                formatted,
                route,
                entities,
                hits=vector_raw_hits,
                mode="pipeline:guarded_vector_direct",
                intent=universal_intent,
            )
            trace.append(PipelineTrace("llm_rewrite", "skipped_guarded_vector_direct", vector_confidence, "LLM not needed for guarded vector context"))
            trace.append(PipelineTrace("validation", "ok" if validation.ok else "failed", 1.0 if validation.ok else 0.30, "; ".join(validation.errors + validation.warnings)))
            if validation.ok:
                return self._build_result(
                    formatted,
                    vector_raw_hits,
                    started,
                    "pipeline:guarded_vector_direct",
                    vector_confidence,
                    route,
                    entities,
                    validation,
                    trace,
                )

        fallback = format_no_answer(route.category)
        if experimental_rag_fallback:
            if self._deadline_is_exceeded(trace, "before_experimental_fallback"):
                return self._timeout_result(
                    started=started,
                    trace=trace,
                    stage="before_experimental_fallback",
                    route=route,
                    entities=entities,
                )
            experimental_started = time.perf_counter()
            experimental = build_experimental_fallback(
                pre.clean_query,
                route,
                started=started,
                allow_llm=experimental_allow_llm and not rag_llm_attempted and not rag_source_conflict,
            )
            trace.append(_timing_trace(
                "experimental_fallback",
                experimental_started,
                detail=experimental.mode,
                metadata={"confidence": experimental.confidence},
            ))
            trace.append(experimental.trace)
            validation = validate_answer(
                pre.clean_query,
                experimental.answer,
                route,
                entities,
                hits=experimental.hits,
                mode="pipeline:" + experimental.mode,
                intent=universal_intent,
            )
            if validation.ok:
                validation = ValidationResult(
                    ok=True,
                    warnings=tuple(dict.fromkeys((*validation.warnings, "experimental_rag_fallback_no_verified_context"))),
                )
            return self._build_result(
                experimental.answer,
                experimental.hits or HITS["reservation"],
                started,
                "pipeline:" + experimental.mode,
                experimental.confidence,
                route,
                entities,
                validation,
                trace,
            )
        validation = ValidationResult(ok=True, warnings=("fallback_no_verified_context",))
        trace.append(PipelineTrace("fallback", "no_verified_context", 0.55, "deterministic and curated retrieval did not pass confidence gate"))
        return self._build_result(fallback, HITS["reservation"], started, "pipeline:no_answer", 0.55, route, entities, validation, trace)

    @staticmethod
    def _deadline_is_exceeded(trace: list[PipelineTrace], stage: str) -> bool:
        if not deadline_exceeded():
            return False
        trace.append(PipelineTrace(
            "deadline",
            "exceeded",
            1.0,
            stage,
            deadline_metadata(),
        ))
        return True

    def _timeout_result(
        self,
        *,
        started: float,
        trace: list[PipelineTrace],
        stage: str,
        route: PipelineRoute | None = None,
        entities: EntityBundle | None = None,
    ) -> PipelineAnswer:
        timeout_route = route or PipelineRoute(
            "no_answer",
            "request_timeout",
            0.45,
            "no_answer",
            "low",
            "global request deadline exceeded",
        )
        if timeout_route.category != "no_answer":
            timeout_route = PipelineRoute(
                "no_answer",
                "request_timeout",
                min(timeout_route.confidence, 0.55),
                "no_answer",
                "low",
                f"{timeout_route.reason}; global request deadline exceeded at {stage}",
            )
        trace.append(PipelineTrace(
            "deadline",
            "request_timeout_no_answer",
            1.0,
            stage,
            deadline_metadata(),
        ))
        validation = ValidationResult(ok=True, warnings=("global_request_timeout", stage))
        answer = (
            "ขออภัยครับ คำถามนี้ใช้เวลาประมวลผลเกินเวลาที่กำหนด เลยหยุดไว้ก่อนเพื่อไม่ให้ระบบค้าง\n"
            "ลองถามใหม่ให้เฉพาะเจาะจงขึ้น เช่น ระบุโซน เกม หรือเรื่องที่ต้องการถามโดยตรงครับ"
        )
        return self._build_result(
            answer,
            [],
            started,
            "pipeline:request_timeout_no_answer",
            0.45,
            timeout_route,
            entities or EntityBundle(),
            validation,
            trace,
        )

    def _try_deterministic(self, question: str, route: PipelineRoute, started: float, trace: list[PipelineTrace]) -> FastAnswer | None:
        if route.category == "games" and route.intent == "competition_game_list":
            game_result = answer_games(question, started)
            if game_result is not None and game_result.mode != "competition_game_list_fast_path":
                trace.append(PipelineTrace("deterministic", "answer_games_before_competition_list", game_result.confidence, game_result.mode))
                return game_result
            trace.append(PipelineTrace("deterministic", "semantic_competition_game_list", route.confidence, route.intent))
            return FastAnswer(
                answer=f"{COMPETITION_GAME_SUMMARY}\nแหล่งข้อมูล: data/competition_rules",
                hits=HITS["our_games"],
                mode="competition_game_list_fast_path",
                elapsed=round(time.perf_counter() - started, 4),
                confidence=max(route.confidence, 0.95),
            )

        handlers = self._handlers_for_route(route)
        for handler in handlers:
            result = handler(question, started)
            if result is not None:
                trace.append(PipelineTrace("deterministic", handler.__name__, result.confidence, result.mode))
                return result

        if route.category == "general":
            trace.append(PipelineTrace("deterministic", "skip_rule_matcher_for_general_route", 0.0, "general route must not borrow PSU rule answers"))
            return None

        if route.category == "competition_rules":
            trace.append(PipelineTrace("category_rule_base", "skipped", 0.0, "competition_rules uses curated competition data"))
            return None

        rule_categories = RULE_CATEGORY_MAP.get(route.category)
        rule = self.matcher.match(question, category=rule_categories) if rule_categories else self.matcher.match(question)
        if rule is not None:
            trace.append(PipelineTrace("category_rule_base", str(rule.get("rule_id")), 0.90, str(rule.get("matched_pattern")), {"category": rule.get("category")}))
            source_url = str(rule.get("source_url", ""))
            hits = [_hit_for_url(str(rule.get("rule_id", "rule")), str(rule.get("category", "rule")), source_url)] if source_url else HITS["reservation"]
            return FastAnswer(
                answer=str(rule.get("answer", "")),
                hits=hits,
                mode="category_rule_fast_path",
                elapsed=round(time.perf_counter() - started, 4),
                confidence=0.90,
            )

        trace.append(PipelineTrace("deterministic", "no_match", 0.0, route.category))
        return None

    @staticmethod
    def _route_for_structured_result(route: PipelineRoute, intent: UniversalIntent, mode: str) -> PipelineRoute:
        if mode == "structured_game_detail" and intent.operation == "availability":
            return PipelineRoute(
                "games",
                "game_availability_lookup",
                max(route.confidence, intent.confidence, 0.82),
                "fact",
                "low",
                f"{route.reason}; structured_mode={mode}; intent_operation=availability",
            )
        forced_by_mode = {
            "structured_booking_selection": ("reservation", "booking_policy"),
            "structured_reservation_fact": ("reservation", "booking_policy"),
            "structured_service_fee": ("service_fee", "service_fee_query"),
            "structured_service_fee_by_game": ("service_fee", "service_fee_query"),
            "structured_schedule": ("schedule", "schedule_query"),
            "structured_games_catalog": ("games", "list"),
            "structured_game_zone_ranking": ("games", "list"),
            "structured_games_family": ("games", "list"),
            "structured_game_detail": ("games", "game_detail_lookup"),
            "structured_game_controls": ("games", "game_control_lookup"),
            "structured_game_controls_family_summary": ("games", "game_control_lookup"),
            "structured_game_controls_no_data": ("games", "game_control_lookup"),
            "structured_equipment_catalog": ("equipment", "list"),
            "structured_equipment_item": ("equipment", "equipment_item_lookup"),
            "structured_members_group_count": ("overview", "group_count"),
            "structured_members_group_list": ("overview", "list"),
            "structured_members_role_lookup": ("overview", "members_lookup"),
            "structured_members_person_lookup": ("overview", "members_lookup"),
            "structured_members_game_relation_no_data": ("overview", "members_lookup"),
        }
        if mode in forced_by_mode:
            category, route_intent = forced_by_mode[mode]
            return PipelineRoute(
                category,
                route_intent,
                max(route.confidence, intent.confidence, 0.82),
                "fact",
                "medium" if category in {"reservation", "service_fee", "schedule"} else route.risk,
                f"{route.reason}; structured_mode={mode}",
            )
        if route.category not in {"general", "unknown", "no_answer"}:
            return route
        category_by_domain = {
            "members": ("overview", "members_lookup"),
            "games": ("games", "games_lookup"),
            "game_controls": ("games", "game_control_lookup"),
            "equipment": ("equipment", "equipment_lookup"),
            "reservation": ("reservation", "booking_policy"),
            "service_fee": ("service_fee", "service_fee_query"),
            "schedule": ("schedule", "schedule_query"),
        }
        mapped = category_by_domain.get(intent.domain)
        if mapped is None:
            return route
        category, fallback_intent = mapped
        route_intent = {
            "structured_equipment_item": "equipment_item_lookup",
            "structured_equipment_catalog": "equipment_catalog",
            "structured_service_fee": "service_fee_query",
            "structured_service_fee_by_game": "service_fee_query",
            "structured_schedule": "schedule_query",
            "structured_reservation_fact": "booking_policy",
            "structured_booking_selection": "booking_policy",
            "structured_game_controls": "game_control_lookup",
            "structured_game_controls_family_summary": "game_control_lookup",
            "structured_games_catalog": "games_lookup",
            "structured_game_zone_ranking": "games_lookup",
            "structured_games_family": "games_lookup",
            "structured_game_detail": "game_detail_lookup",
            "structured_members_group_count": "group_count",
            "structured_members_group_list": "members_lookup",
        }.get(mode, fallback_intent)
        return PipelineRoute(
            category,
            route_intent,
            max(route.confidence, intent.confidence, 0.82),
            "fact",
            "low",
            f"{route.reason}; structured_tool_domain={intent.domain}",
        )

    @staticmethod
    def _planned_task_matches_route(task: QueryPlanTask, route: PipelineRoute) -> bool:
        if route.category in {"general", "unknown", "no_answer"}:
            return True
        allowed_categories = {
            "members": {"overview"},
            "games": {"games"},
            "game_controls": {"games"},
            "equipment": {"equipment"},
            "reservation": {"reservation"},
            "service_fee": {"service_fee"},
            "schedule": {"schedule"},
            "rules": {"rules"},
            "penalty": {"penalty"},
            "competition_rules": {"competition_rules"},
            "contact": {"contact"},
            "knowledge": {"knowledge", "general"},
            "general": {"general", "knowledge"},
        }
        return route.category in allowed_categories.get(task.domain, set())

    @staticmethod
    def _handlers_for_route(route: PipelineRoute):
        category = route.category
        if route.intent == "service_fee_query":
            return (answer_price,)
        if category == "general":
            return ()
        if category == "service_fee":
            return (answer_price,)
        if category == "schedule":
            return (answer_schedule,)
        if category == "equipment":
            return (answer_equipment, answer_games)
        if category == "games":
            return (answer_games, answer_equipment)
        if category == "competition_rules":
            return (answer_competition_rules,)
        if category in {"reservation", "rules", "penalty", "contact", "overview", "knowledge", "events_news"}:
            return (answer_static_domain,)
        return (answer_price, answer_schedule, answer_equipment, answer_games, answer_static_domain)

    @staticmethod
    def _build_result(
        answer: str,
        hits: list[dict],
        started: float,
        mode: str,
        confidence: float,
        route: PipelineRoute,
        entities,
        validation: ValidationResult,
        trace: list[PipelineTrace],
    ) -> PipelineAnswer:
        build_started = time.perf_counter()
        final_validation_started = time.perf_counter()
        source_validation = validate_answer("", answer, route, entities, hits=hits)
        merged_errors = tuple(dict.fromkeys((*validation.errors, *source_validation.errors)))
        merged_warnings = tuple(dict.fromkeys((*validation.warnings, *source_validation.warnings)))
        final_validation = ValidationResult(ok=not merged_errors, errors=merged_errors, warnings=merged_warnings)
        if source_validation.errors or source_validation.warnings:
            trace.append(_timing_trace(
                "validation_final",
                final_validation_started,
                detail="ok" if final_validation.ok else "failed",
                metadata={
                    "added_error_count": len(source_validation.errors),
                    "added_warning_count": len(source_validation.warnings),
                    "added_errors": list(source_validation.errors),
                    "added_warnings": list(source_validation.warnings),
                    "merged_error_count": len(final_validation.errors),
                    "merged_warning_count": len(final_validation.warnings),
                },
                confidence=1.0 if final_validation.ok else 0.30,
            ))
        validation = final_validation
        if not final_validation.ok:
            rejected_mode = mode
            rejected_route = f"{route.category}/{route.intent}"
            rejected_errors = list(final_validation.errors)
            trace.append(PipelineTrace(
                "answer_contract",
                "hard_veto_to_no_answer",
                1.0,
                "; ".join(rejected_errors),
                {
                    "rejected_mode": rejected_mode,
                    "rejected_route": rejected_route,
                    "errors": rejected_errors,
                },
            ))
            answer = format_no_answer(route.category)
            hits = []
            mode = "pipeline:answer_contract_no_answer"
            confidence = min(confidence, 0.45)
            route = PipelineRoute(
                "no_answer",
                "answer_contract_rejected",
                confidence,
                "no_answer",
                "low",
                f"draft rejected by answer contract: {rejected_route}",
            )
            validation = ValidationResult(
                ok=True,
                warnings=tuple(dict.fromkeys((
                    "draft_rejected_by_answer_contract",
                    *rejected_errors,
                    *final_validation.warnings,
                ))),
            )
        universal_intent = AnswerQualityPipeline._universal_intent_from_trace(trace)
        decision_artifact = build_decision_artifact(
            mode=mode,
            confidence=confidence,
            route=route,
            entities=entities,
            validation=validation,
            trace=trace,
            hits=hits,
            universal_intent=universal_intent,
        )
        style_started = time.perf_counter()
        styled_answer = format_thai_response_style(answer)
        style_elapsed = time.perf_counter() - style_started
        total_elapsed = time.perf_counter() - started
        trace.append(_timing_trace(
            "build_result",
            build_started,
            detail=mode,
            metadata={
                "format_thai_style_ms": round(style_elapsed * 1000, 2),
                "total_elapsed_ms": round(total_elapsed * 1000, 2),
                "total_elapsed_sec": round(total_elapsed, 4),
            },
        ))
        return PipelineAnswer(
            answer=styled_answer,
            hits=hits,
            elapsed=round(time.perf_counter() - started, 4),
            mode=mode,
            confidence=confidence,
            route=route,
            entities=entities,
            validation=validation,
            trace=trace,
            universal_intent=universal_intent,
            decision_artifact=decision_artifact,
        )

    @staticmethod
    def _universal_intent_from_trace(trace: list[PipelineTrace]) -> UniversalIntent | None:
        resolved_target = ""
        resolved_target_filters: dict[str, str] = {}
        for item in reversed(trace):
            if item.stage == "target_context" and item.decision == "enrich_universal_intent":
                metadata = item.metadata or {}
                resolved_target = str(metadata.get("label") or resolved_target)
                if metadata.get("target_id"):
                    resolved_target_filters["resolved_target_id"] = str(metadata["target_id"])
                if metadata.get("target_type"):
                    resolved_target_filters["resolved_target_type"] = str(metadata["target_type"])
                continue
            if item.stage != "universal_intent":
                continue
            domain, _, operation = item.decision.partition("/")
            metadata = item.metadata or {}
            needs = metadata.get("needs") if isinstance(metadata.get("needs"), list) else []
            filters = metadata.get("filters") if isinstance(metadata.get("filters"), dict) else {}
            return UniversalIntent(
                domain=domain or "general",
                operation=operation or "unknown",
                target=str(metadata.get("target") or resolved_target),
                filters={**filters, **resolved_target_filters},
                needs=tuple(str(value) for value in needs),
                answer_style=str(metadata.get("answer_style") or "direct"),
                confidence=item.confidence,
                method=str(metadata.get("method") or "heuristic"),
                reason=item.detail,
            )
        return None


_PIPELINE: AnswerQualityPipeline | None = None


def get_pipeline() -> AnswerQualityPipeline:
    global _PIPELINE
    if _PIPELINE is None:
        _PIPELINE = AnswerQualityPipeline()
    return _PIPELINE


def answer_question_pipeline_debug(
    question: str,
    *,
    experimental_rag_fallback: bool | None = None,
    experimental_allow_llm: bool | None = None,
    global_timeout_sec: float | None = None,
) -> PipelineAnswer:
    return get_pipeline().answer(
        question,
        experimental_rag_fallback=experimental_rag_fallback,
        experimental_allow_llm=experimental_allow_llm,
        global_timeout_sec=global_timeout_sec,
    )


def answer_question_pipeline(question: str) -> tuple[str, list[dict], float, str]:
    result = answer_question_pipeline_debug(question)
    return result.answer, result.hits, result.elapsed, result.mode
