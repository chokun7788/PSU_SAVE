from __future__ import annotations

import re
import time

from app.core.normalization import normalize_text
from app.core.thai_style import format_thai_response_style
from app.pipeline.formatter import format_answer, format_no_answer
from app.pipeline.guard import guard_scope
from app.pipeline.hybrid_retrieval import (
    answer_from_hybrid_hits,
    retrieve_hybrid_guarded,
    should_skip_legacy_curated_after_hybrid,
    should_use_hybrid_retrieval,
)
from app.pipeline.preprocess import extract_entities, preprocess_input
from app.pipeline.experimental_fallback import (
    build_experimental_fallback,
    env_experimental_llm_default,
    env_experimental_rag_fallback_default,
)
from app.pipeline.retrieval import (
    answer_from_competition_fact_hits,
    answer_from_curated_hits,
    retrieve_competition_fact_cards,
    retrieve_curated,
)
from app.pipeline.router import route_intent
from app.pipeline.schemas import PipelineAnswer, PipelineRoute, PipelineTrace, ValidationResult
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


def _has(q: str, *terms: str) -> bool:
    return any(term in q for term in terms)


def _looks_like_standalone_question(q: str) -> bool:
    q = normalize_text(q)
    has_question_signal = _has(
        q,
        "ไหม", "มั้ย", "หรือเปล่า", "รึเปล่า", "อะไร", "กี่", "เท่าไหร่", "เท่าไร",
        "ยังไง", "อย่างไร", "ได้ไหม", "เปิด", "ปิด", "ราคา", "ค่าบริการ", "จอง",
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
    )
    return has_question_signal and has_domain_signal


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

    parts = [
        part.strip(" \t\r\n?？")
        for part in re.split(r"\s*(?:[?？]|แล้ว|และ|ส่วน|อีกอย่าง)\s*", clean)
        if part.strip(" \t\r\n?？")
    ]
    if len(parts) <= 1 or len(parts) > 3:
        return [clean]
    if not all(_looks_like_standalone_question(part) for part in parts):
        return [clean]
    return parts


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


def _select_active_preprocessed_query(pre) -> tuple:
    entities = extract_entities(pre)
    route, route_trace = route_intent(pre, entities)
    selected_pre = pre
    selected_entities = entities
    selected_route = route
    selected_trace = route_trace
    candidates: list[dict] = []

    for variant in pre.query_variants:
        if not variant or variant == pre.clean_query:
            continue
        variant_pre = preprocess_input(variant)
        variant_entities = extract_entities(variant_pre)
        variant_route, variant_trace = route_intent(variant_pre, variant_entities)
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
    ) -> PipelineAnswer:
        experimental_rag_fallback = env_experimental_rag_fallback_default() if experimental_rag_fallback is None else experimental_rag_fallback
        experimental_allow_llm = env_experimental_llm_default() if experimental_allow_llm is None else experimental_allow_llm
        parts = _split_multi_question(question)
        if len(parts) > 1:
            return self._answer_multi(
                question,
                parts,
                experimental_rag_fallback=experimental_rag_fallback,
                experimental_allow_llm=experimental_allow_llm,
            )
        return self._answer_single(
            question,
            experimental_rag_fallback=experimental_rag_fallback,
            experimental_allow_llm=experimental_allow_llm,
        )

    def _answer_multi(
        self,
        question: str,
        parts: list[str],
        *,
        experimental_rag_fallback: bool,
        experimental_allow_llm: bool,
    ) -> PipelineAnswer:
        started = time.perf_counter()
        results = [
            self._answer_single(
                part,
                experimental_rag_fallback=experimental_rag_fallback,
                experimental_allow_llm=experimental_allow_llm,
            )
            for part in parts
        ]
        answer_blocks = ["คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:"]
        for index, (part, result) in enumerate(zip(parts, results), 1):
            answer_blocks.append(f"{index}. {part}\n{result.answer}")

        pre = preprocess_input(question)
        entities = extract_entities(pre)
        route = PipelineRoute("multi_question", "multi_question_split", 0.92, "summary", "medium", "split clear multi-intent question")
        validation = ValidationResult(
            ok=all(result.validation.ok for result in results),
            errors=tuple(error for result in results for error in result.validation.errors),
            warnings=tuple(warning for result in results for warning in result.validation.warnings),
        )
        confidence = min(result.confidence for result in results)
        hits = _dedupe_hits([hit for result in results for hit in result.hits])
        trace = [
            PipelineTrace(
                "multi_question",
                "split",
                0.92,
                f"parts={len(parts)}",
                {"parts": parts},
            )
        ]
        for part, result in zip(parts, results):
            trace.append(PipelineTrace(
                "multi_question_child",
                f"{result.route.category}/{result.route.intent}",
                result.confidence,
                part,
                {"mode": result.mode, "elapsed": result.elapsed},
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

    def _answer_single(
        self,
        question: str,
        *,
        experimental_rag_fallback: bool,
        experimental_allow_llm: bool,
    ) -> PipelineAnswer:
        started = time.perf_counter()
        trace: list[PipelineTrace] = []

        original_pre = preprocess_input(question)
        trace.append(PipelineTrace(
            "preprocess",
            "normalized",
            1.0,
            original_pre.normalized_query,
            {"language_hint": original_pre.language_hint, "query_variants": list(original_pre.query_variants)},
        ))
        pre, entities, route, route_trace, variant_candidates = _select_active_preprocessed_query(original_pre)
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

        guard_answer, guard_confidence, guard_trace = guard_scope(pre, entities)
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

        if route.category in {"games", "equipment", "general", "unknown"} and looks_like_game_control_query(pre.clean_query):
            control_route = route
            if route.category in {"general", "unknown"}:
                control_route = PipelineRoute("games", "game_control_lookup", 0.82, "fact", "low", "control/button terms use guarded game control vector")
            vector_hits, vector_trace = retrieve_vector_guarded(pre.clean_query, control_route, limit=8)
            trace.append(vector_trace)
            control_hits = [hit for hit in vector_hits if hit.get("category") == "game_controls"]
            vector_answer, vector_raw_hits, vector_confidence = answer_from_vector_hits(control_hits, pre.clean_query)
            if vector_answer and vector_confidence >= 0.68:
                formatted = format_answer(vector_answer, vector_raw_hits, control_route, entities)
                validation = validate_answer(question, formatted, control_route, entities)
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

        deterministic = self._try_deterministic(pre.clean_query, route, started, trace)
        if deterministic is not None and deterministic.confidence >= 0.75:
            if route.category == "games" and deterministic.mode in {"games_unknown_fast_path", "games_detail_unknown_no_answer_fast_path"}:
                vector_hits, vector_trace = retrieve_vector_guarded(pre.clean_query, route)
                trace.append(vector_trace)
                vector_answer, vector_raw_hits, vector_confidence = answer_from_vector_hits(vector_hits, pre.clean_query)
                if vector_answer and vector_confidence >= 0.68:
                    formatted = format_answer(vector_answer, vector_raw_hits, route, entities)
                    validation = validate_answer(question, formatted, route, entities)
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
                formatted = format_answer(deterministic.answer, deterministic.hits, route, entities)
                validation = validate_answer(question, formatted, route, entities)
                trace.append(PipelineTrace("validation", "ok" if validation.ok else "failed", 1.0 if validation.ok else 0.30, "; ".join(validation.errors + validation.warnings)))
                if validation.ok or deterministic.confidence >= 0.90:
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
            fact_hits, fact_trace = retrieve_competition_fact_cards(pre.clean_query)
            trace.append(fact_trace)
            fact_answer, fact_raw_hits, fact_confidence = answer_from_competition_fact_hits(fact_hits, pre.clean_query)
            if fact_answer and fact_confidence >= 0.72:
                formatted = format_answer(fact_answer, fact_raw_hits, route, entities)
                validation = validate_answer(question, formatted, route, entities)
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

        if should_use_hybrid_retrieval(route):
            hybrid_hits, hybrid_trace = retrieve_hybrid_guarded(pre.clean_query, route)
            trace.append(hybrid_trace)
            hybrid_answer, hybrid_raw_hits, hybrid_confidence = answer_from_hybrid_hits(hybrid_hits, pre.clean_query)
            if hybrid_answer and hybrid_confidence >= 0.68:
                formatted = format_answer(hybrid_answer, hybrid_raw_hits, route, entities)
                validation = validate_answer(question, formatted, route, entities)
                trace.append(PipelineTrace("llm_rewrite", "skipped_hybrid_rerank", hybrid_confidence, "LLM not needed for guarded hybrid candidate"))
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
            if experimental_rag_fallback:
                fallback = build_experimental_fallback(
                    pre.clean_query,
                    route,
                    started=started,
                    allow_llm=experimental_allow_llm,
                )
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

        rag_hits, rag_trace = retrieve_curated(pre.clean_query, route.category)
        trace.append(rag_trace)
        rag_answer, rag_raw_hits, rag_confidence = answer_from_curated_hits(rag_hits, pre.clean_query)
        if rag_answer and rag_confidence >= 0.65:
            formatted = format_answer(rag_answer, rag_raw_hits, route, entities)
            validation = validate_answer(question, formatted, route, entities)
            trace.append(PipelineTrace("llm_rewrite", "skipped_curated_direct", rag_confidence, "LLM not needed for curated fact"))
            trace.append(PipelineTrace("validation", "ok" if validation.ok else "failed", 1.0 if validation.ok else 0.30, "; ".join(validation.errors + validation.warnings)))
            if validation.ok:
                return self._build_result(formatted, rag_raw_hits, started, "pipeline:rag_direct_curated", rag_confidence, route, entities, validation, trace)

        vector_hits, vector_trace = retrieve_vector_guarded(pre.clean_query, route)
        trace.append(vector_trace)
        vector_answer, vector_raw_hits, vector_confidence = answer_from_vector_hits(vector_hits, pre.clean_query)
        if vector_answer and vector_confidence >= 0.68:
            formatted = format_answer(vector_answer, vector_raw_hits, route, entities)
            validation = validate_answer(question, formatted, route, entities)
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
            experimental = build_experimental_fallback(
                pre.clean_query,
                route,
                started=started,
                allow_llm=experimental_allow_llm,
            )
            trace.append(experimental.trace)
            validation = ValidationResult(ok=True, warnings=("experimental_rag_fallback_no_verified_context",))
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

        handlers = self._handlers_for_route(route.category)
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
    def _handlers_for_route(category: str):
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
        return PipelineAnswer(
            answer=format_thai_response_style(answer),
            hits=hits,
            elapsed=round(time.perf_counter() - started, 4),
            mode=mode,
            confidence=confidence,
            route=route,
            entities=entities,
            validation=validation,
            trace=trace,
        )


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
) -> PipelineAnswer:
    return get_pipeline().answer(
        question,
        experimental_rag_fallback=experimental_rag_fallback,
        experimental_allow_llm=experimental_allow_llm,
    )


def answer_question_pipeline(question: str) -> tuple[str, list[dict], float, str]:
    result = answer_question_pipeline_debug(question)
    return result.answer, result.hits, result.elapsed, result.mode
