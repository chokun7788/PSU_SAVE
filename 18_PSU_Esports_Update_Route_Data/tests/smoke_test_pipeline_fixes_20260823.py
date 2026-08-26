from __future__ import annotations

import os
import sys
from pathlib import Path


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import app.pipeline.experimental_fallback as experimental_fallback  # noqa: E402
import app.pipeline.engine as pipeline_engine  # noqa: E402
import app.pipeline.structured_tools as structured_tools  # noqa: E402
import app.pipeline.universal_intent as universal_intent  # noqa: E402
from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402
from app.pipeline.experimental_fallback import (  # noqa: E402
    ExperimentalFallback,
    _general_output_contract,
    _shape_general_output,
    select_general_generation_profile,
)
from app.pipeline.model_gateway import preflight_llm_allowed  # noqa: E402
from app.pipeline.query_signals import (  # noqa: E402
    contains_ascii_bounded,
    looks_like_game_zone_ranking_query,
    looks_like_general_concept_definition,
    looks_like_price_amount_query,
)
from app.pipeline.schemas import EntityBundle, PipelineRoute, PipelineTrace, UniversalIntent  # noqa: E402
from app.pipeline.validator import validate_answer  # noqa: E402


def ask(question: str, *, allow_llm: bool = False):
    return answer_question_pipeline_debug(
        question,
        experimental_rag_fallback=True,
        experimental_allow_llm=allow_llm,
        global_timeout_sec=20.0,
    )


def test_request_state_is_initialized_on_all_single_paths() -> None:
    original_fallback = pipeline_engine.build_experimental_fallback
    previous_intent_llm = os.environ.get("PSU_UNIVERSAL_INTENT_LLM")
    fallback_calls: list[bool] = []

    def fake_fallback(_question, route, *, started, allow_llm, limit=5):
        del started, limit
        fallback_calls.append(bool(allow_llm))
        return ExperimentalFallback(
            "ยังไม่มีข้อมูลที่ยืนยันได้สำหรับคำถามนี้ครับ",
            [],
            "test_no_context",
            0.42,
            PipelineTrace("experimental_rag_fallback", "test_no_context", 0.42, route.category),
        )

    pipeline_engine.build_experimental_fallback = fake_fallback
    os.environ["PSU_UNIVERSAL_INTENT_LLM"] = "0"
    try:
        result = ask("ROV ถ้าใช้ bug จะโดนอะไร", allow_llm=True)
    finally:
        pipeline_engine.build_experimental_fallback = original_fallback
        if previous_intent_llm is None:
            os.environ.pop("PSU_UNIVERSAL_INTENT_LLM", None)
        else:
            os.environ["PSU_UNIVERSAL_INTENT_LLM"] = previous_intent_llm

    assert result.mode != "exception", (result.mode, result.answer)
    assert result.answer.strip()
    assert fallback_calls == [True], fallback_calls

    booking = ask("จอง")
    assert booking.mode != "exception", (booking.mode, booking.answer)
    assert booking.answer.strip()


def test_competition_rag_does_not_substitute_a_different_rule() -> None:
    result = ask("ROV ถ้าใช้ bug จะโดนอะไร")
    assert "15 นาที" not in result.answer, (result.mode, result.answer)
    assert "ล่าช้า" not in result.answer, (result.mode, result.answer)
    assert "ยังไม่มี" in result.answer or "ยังไม่พบ" in result.answer, (result.mode, result.answer)


def test_price_signal_uses_phrase_context() -> None:
    for question in (
        "API คืออะไร อธิบายข้อดีข้อเสียสั้น ๆ",
        "GPU คืออะไรแบบเข้าใจง่าย อธิบายข้อดีข้อเสียสั้น ๆ",
        "server กับ client ต่างกันยังไง อธิบายข้อดีข้อเสียสั้น ๆ",
    ):
        assert not looks_like_price_amount_query(question), question
        result = ask(question)
        assert result.route.category == "general", (question, result.route, result.answer)
        assert result.mode != "pipeline:ambiguity_clarification", (question, result.answer)
        assert "ขอรู้บริการหรือโซนก่อน" not in result.answer

    assert looks_like_price_amount_query("PS5 เสียกี่บาท")
    assert looks_like_price_amount_query("PC ต้องจ่ายเท่าไหร่")


def test_general_definition_does_not_use_psu_equipment_inventory() -> None:
    question = "คีย์บอร์ด mechanical คืออะไรแบบสั้น"
    assert looks_like_general_concept_definition(question)
    result = ask(question)
    assert result.route.category == "general", (result.route, result.answer)
    assert "structured_equipment" not in result.mode
    assert "อุปกรณ์บนหน้า Home" not in result.answer

    inventory = ask("PC มีอุปกรณ์คีย์บอร์ดอะไรบ้าง")
    assert inventory.route.category == "equipment", (inventory.route, inventory.answer)
    assert "structured_equipment" in inventory.mode


def test_ascii_control_token_does_not_match_inside_game_title() -> None:
    assert contains_ascii_bounded("press cross now", "cross")
    assert not contains_ascii_bounded("animal crossing", "cross")

    result = ask("Animal Crossing: New Horizons คือเกมอะไร")
    assert result.route.category == "games", (result.route, result.answer)
    assert result.mode == "pipeline:structured_game_detail", (result.mode, result.answer)
    assert "Animal Crossing: New Horizons" in result.answer
    assert "หลายความหมาย" not in result.answer

    llm_on = ask("Animal Crossing: New Horizons คือเกมอะไร", allow_llm=True)
    assert llm_on.mode == "pipeline:structured_game_detail", (llm_on.mode, llm_on.answer)
    assert llm_on.decision_artifact.get("llm_calls") == [], llm_on.decision_artifact.get("llm_calls")


def test_game_zone_ranking_is_deterministic_structured_path() -> None:
    for question in (
        "อุปกรณ์ไหนเกมเยอะสุด",
        "โซนไหนมีเกมเยอะที่สุด",
        "ช่วยจัดอันดับจำนวนเกมตามโซน",
    ):
        assert looks_like_game_zone_ranking_query(question), question
        result = ask(question)
        assert result.route.category == "games", (question, result.route, result.answer)
        assert result.mode == "pipeline:structured_game_zone_ranking", (question, result.mode, result.answer)
        assert "จำนวนเกมตามโซน" in result.answer

    original_intent_call = universal_intent._llm_intent
    attempted = 0

    def fail_intent_call(*_args, **_kwargs):
        nonlocal attempted
        attempted += 1
        raise AssertionError("exact game-zone ranking must not call LLM intent")

    universal_intent._llm_intent = fail_intent_call
    try:
        llm_on = ask("อุปกรณ์ไหนเกมเยอะสุด", allow_llm=True)
    finally:
        universal_intent._llm_intent = original_intent_call

    assert llm_on.mode == "pipeline:structured_game_zone_ranking", (llm_on.mode, llm_on.answer)
    assert attempted == 0
    assert llm_on.decision_artifact.get("llm_calls") == [], llm_on.decision_artifact.get("llm_calls")


def test_dynamic_freshness_requires_live_evidence() -> None:
    result = ask("เพลงฮิตตอนนี้คืออะไร", allow_llm=True)
    assert result.mode == "pipeline:freshness_live_source_required", (result.mode, result.answer)
    assert result.route.category == "no_answer"
    assert "ยังไม่มีแหล่งข้อมูลสด" in result.answer
    assert "Flowers" not in result.answer

    validation = validate_answer(
        "เพลงฮิตตอนนี้คืออะไร",
        "เพลง Example Song กำลังฮิตที่สุดตอนนี้",
        PipelineRoute("general", "general_knowledge_query", 0.8, "general", "low", "test"),
        EntityBundle(),
        hits=[],
        mode="pipeline:general_llm_fallback",
    )
    assert not validation.ok
    assert "freshness_claim_without_live_evidence" in validation.errors


def test_clear_general_reserves_one_llm_call_for_final_answer() -> None:
    route = PipelineRoute("general", "general_knowledge_query", 0.94, "general", "low", "test")
    allowed, reason = preflight_llm_allowed(route, True, "แปลคำว่า reservation เป็นภาษาไทย ตอบแบบประโยคเดียว")
    assert allowed is False
    assert "final answer" in reason

    original_intent_call = universal_intent._llm_intent
    original_general_call = experimental_fallback._general_llm_answer_with_metadata
    calls = {"intent": 0, "general": 0}

    def fail_intent_call(*_args, **_kwargs):
        calls["intent"] += 1
        raise AssertionError("clear general request must not spend an LLM call on intent review")

    def fake_general_call(_question: str):
        calls["general"] += 1
        return "reservation แปลว่า การจอง", {
            "llm_kind": "general_llm",
            "llm_model": "fake",
            "llm_elapsed_ms": 1.0,
            "llm_num_predict": 48,
            "llm_budget_used_calls": 1,
        }

    universal_intent._llm_intent = fail_intent_call
    experimental_fallback._general_llm_answer_with_metadata = fake_general_call
    try:
        result = ask("แปลคำว่า reservation เป็นภาษาไทย ตอบแบบประโยคเดียว", allow_llm=True)
    finally:
        universal_intent._llm_intent = original_intent_call
        experimental_fallback._general_llm_answer_with_metadata = original_general_call

    assert result.mode == "pipeline:general_llm_fallback", (result.mode, result.answer)
    assert calls == {"intent": 0, "general": 1}, calls
    intent_traces = [item for item in result.trace if item.stage == "universal_intent"]
    assert intent_traces and intent_traces[-1].metadata.get("llm_attempted") is False


def test_general_generation_budget_is_adaptive() -> None:
    previous = os.environ.get("PSU_GENERAL_LLM_NUM_PREDICT")
    previous_adaptive = os.environ.get("PSU_GENERAL_LLM_ADAPTIVE_NUM_PREDICT")
    os.environ["PSU_GENERAL_LLM_NUM_PREDICT"] = "256"
    os.environ["PSU_GENERAL_LLM_ADAPTIVE_NUM_PREDICT"] = "1"
    try:
        translation = select_general_generation_profile("แปลคำว่า reservation เป็นภาษาไทย")
        one_sentence = select_general_generation_profile("เขียนประโยคประชาสัมพันธ์หนึ่งประโยค")
        two_sentences = select_general_generation_profile("ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค")
        concise = select_general_generation_profile("latency คืออะไรแบบสั้น")
        tradeoffs = select_general_generation_profile("API คืออะไร อธิบายข้อดีข้อเสียสั้น ๆ")
        translated_tradeoffs = select_general_generation_profile(
            "แปลคำว่า reservation เป็นภาษาไทย อธิบายข้อดีข้อเสียสั้น ๆ"
        )
        general = select_general_generation_profile("อธิบายแนวคิดระบบ distributed computing")
    finally:
        if previous is None:
            os.environ.pop("PSU_GENERAL_LLM_NUM_PREDICT", None)
        else:
            os.environ["PSU_GENERAL_LLM_NUM_PREDICT"] = previous
        if previous_adaptive is None:
            os.environ.pop("PSU_GENERAL_LLM_ADAPTIVE_NUM_PREDICT", None)
        else:
            os.environ["PSU_GENERAL_LLM_ADAPTIVE_NUM_PREDICT"] = previous_adaptive

    assert translation.name == "translation" and translation.num_predict <= 48
    assert one_sentence.name == "short_creation" and one_sentence.num_predict <= 96
    assert two_sentences.name == "two_sentences" and two_sentences.num_predict <= 96
    assert concise.name == "concise_definition" and concise.num_predict <= 96
    assert tradeoffs.name == "definition_with_tradeoffs" and tradeoffs.num_predict <= 112
    assert translated_tradeoffs.name == "definition_with_tradeoffs" and translated_tradeoffs.num_predict <= 112
    assert general.name == "general_concise" and general.num_predict <= 128
    assert "ไม่เกิน 35 คำ" in general.instruction

    ok, reason = _general_output_contract(
        "คำตอบ: API คือช่องทางให้โปรแกรมสื่อสารกัน\nข้อดี: เชื่อมระบบได้เร็ว\nข้อเสีย: ต้องดูแลความปลอดภัย",
        tradeoffs,
        {"ollama_done_reason": "stop"},
    )
    assert ok and reason == "ok"

    ok, reason = _general_output_contract(
        "คำตอบ: API คือช่องทางให้โปรแกรมสื่อสารกัน\nข้อดี: เชื่อมระบบได้เร็ว\nข้อเสีย: ต้องดูแล",
        tradeoffs,
        {"ollama_done_reason": "length"},
    )
    assert not ok and reason == "token_limit_truncation"

    provider = {"ollama_done_reason": "stop"}
    shaped = _shape_general_output(
        "ขอบคุณสำหรับความช่วยเหลือครับ\nขอขอบพระคุณอีกครั้งครับ\nต้องการข้อมูลเพิ่มไหมครับ",
        two_sentences,
        provider,
    )
    assert shaped.count("\n") == 1
    ok, reason = _general_output_contract(shaped, two_sentences, provider)
    assert ok and reason == "ok"

    bullets = select_general_generation_profile("อธิบาย latency ตอบแบบ bullet สั้น ๆ")
    provider = {"ollama_done_reason": "length"}
    shaped = _shape_general_output(
        "- Latency คือเวลาหน่วงของระบบครับ\n- ค่ายิ่งต่ำยิ่งตอบสนองเร็วครับ\n- รายการที่ถูกตัดกลาง",
        bullets,
        provider,
    )
    assert provider.get("llm_output_bounded_prefix_complete") is True
    ok, reason = _general_output_contract(shaped, bullets, provider)
    assert ok and reason == "ok"


def test_clear_control_and_bare_booking_do_not_spend_llm_budget() -> None:
    control = ask(
        "Horizon Call of the Mountain ปุ่มเคลื่อนที่ด้วยท่าทางร่างกายกดอะไร",
        allow_llm=True,
    )
    assert control.mode == "pipeline:structured_game_controls", (control.mode, control.answer)
    assert control.decision_artifact.get("llm_calls") == [], control.decision_artifact.get("llm_calls")

    catalog = ask("เกม", allow_llm=True)
    assert catalog.mode == "pipeline:structured_games_catalog", (catalog.mode, catalog.answer)
    assert catalog.decision_artifact.get("llm_calls") == [], catalog.decision_artifact.get("llm_calls")

    booking = ask("จอง", allow_llm=True)
    assert booking.mode == "pipeline:ambiguity_clarification", (booking.mode, booking.answer)
    assert "ต้องการถามเรื่องการจองส่วนไหน" in booking.answer
    assert booking.decision_artifact.get("llm_calls") == [], booking.decision_artifact.get("llm_calls")

    homework = ask("ช่วยทำการบ้านคณิตให้หน่อย", allow_llm=True)
    assert homework.mode == "pipeline:general_input_clarification", (homework.mode, homework.answer)
    assert "ยังไม่มีโจทย์คณิต" in homework.answer
    assert homework.decision_artifact.get("llm_calls") == [], homework.decision_artifact.get("llm_calls")


def test_service_catalog_does_not_run_fuzzy_game_target_scan() -> None:
    intent = UniversalIntent(
        domain="games",
        operation="list",
        target="Nintendo Switch",
        filters={},
        needs=(),
        answer_style="direct",
        confidence=0.9,
        method="test",
        reason="service catalog regression",
    )
    original_detect_game = structured_tools._detect_game

    def fail_if_called(*_args, **_kwargs):
        raise AssertionError("catalog request must not scan fuzzy game-title aliases")

    structured_tools._detect_game = fail_if_called
    try:
        result = structured_tools._service_game_availability_answer(
            "Nintendo Switch (1-4 Persons) มีเกมอะไรบ้าง",
            intent,
        )
    finally:
        structured_tools._detect_game = original_detect_game

    assert result is not None
    assert result.mode == "structured_service_game_availability"
    assert "Nintendo Switch" in result.answer


def test_exact_reservation_fact_does_not_run_fuzzy_alias_scan() -> None:
    intent = UniversalIntent(
        domain="reservation",
        operation="how_to",
        target="Cockpit Zone",
        filters={},
        needs=(),
        answer_style="direct",
        confidence=0.9,
        method="test",
        reason="reservation exact-match regression",
    )
    original_contains_alias = structured_tools.contains_alias

    def reject_fuzzy(query, aliases, *, fuzzy=True, threshold=0.84):
        if fuzzy:
            raise AssertionError("exact reservation phrase must not enter fuzzy alias matching")
        return original_contains_alias(query, aliases, fuzzy=False, threshold=threshold)

    structured_tools.contains_alias = reject_fuzzy
    try:
        result = structured_tools._reservation_answer(
            "จะเล่น นักศึกษาต่างมหาลัย เล่น Cockpit 1 ชั่วโมง เสีย จองยังไง",
            intent,
        )
    finally:
        structured_tools.contains_alias = original_contains_alias

    assert result is not None
    assert result.mode == "structured_reservation_fact"
    assert result.evidence.get("fact_key") == "booking_steps"
    assert result.evidence.get("match_method") == "exact"


def test_zone_booking_does_not_run_fuzzy_game_target_scan() -> None:
    intent = UniversalIntent(
        domain="reservation",
        operation="how_to",
        target="Cockpit Zone",
        filters={},
        needs=(),
        answer_style="direct",
        confidence=0.9,
        method="test",
        reason="zone booking target regression",
    )
    original_detect_game = structured_tools._detect_game
    fuzzy_flags: list[bool] = []

    def capture_detect_game(*_args, allow_fuzzy=True, **_kwargs):
        fuzzy_flags.append(bool(allow_fuzzy))
        return None

    structured_tools._detect_game = capture_detect_game
    try:
        structured_tools._service_game_availability_answer(
            "จะเล่น นักศึกษาต่างมหาลัย เล่น Cockpit 1 ชั่วโมง เสีย จองยังไง",
            intent,
        )
    finally:
        structured_tools._detect_game = original_detect_game

    assert fuzzy_flags == [False], fuzzy_flags


def main() -> int:
    tests = (
        test_request_state_is_initialized_on_all_single_paths,
        test_competition_rag_does_not_substitute_a_different_rule,
        test_price_signal_uses_phrase_context,
        test_general_definition_does_not_use_psu_equipment_inventory,
        test_ascii_control_token_does_not_match_inside_game_title,
        test_game_zone_ranking_is_deterministic_structured_path,
        test_dynamic_freshness_requires_live_evidence,
        test_clear_general_reserves_one_llm_call_for_final_answer,
        test_general_generation_budget_is_adaptive,
        test_clear_control_and_bare_booking_do_not_spend_llm_budget,
        test_service_catalog_does_not_run_fuzzy_game_target_scan,
        test_exact_reservation_fact_does_not_run_fuzzy_alias_scan,
        test_zone_booking_does_not_run_fuzzy_game_target_scan,
    )
    for test in tests:
        test()
        print(f"OK {test.__name__}")
    print("PIPELINE FIXES 20260823 SMOKE TEST OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
