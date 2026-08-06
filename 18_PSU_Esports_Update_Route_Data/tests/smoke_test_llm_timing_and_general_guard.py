from __future__ import annotations

import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import app.pipeline.experimental_fallback as experimental_fallback
import app.pipeline.facts_composer as facts_composer
import app.pipeline.universal_intent as universal_intent
from app.pipeline.engine import answer_question_pipeline_debug
from app.pipeline.experimental_fallback import build_experimental_fallback
from app.pipeline.facts_composer import compose_structured_answer
from app.pipeline.schemas import PipelineRoute, UniversalIntent
from app.pipeline.universal_intent import resolve_universal_intent


def _route(category: str = "general", intent: str = "unknown_domain_query", confidence: float = 0.55) -> PipelineRoute:
    return PipelineRoute(category, intent, confidence, "general" if category == "general" else "fact", "low", "smoke")


def _intent(domain: str = "general", operation: str = "general_answer", confidence: float = 0.72) -> UniversalIntent:
    return UniversalIntent(domain=domain, operation=operation, confidence=confidence, method="smoke")


def test_universal_intent_trace_includes_llm_call_metadata() -> None:
    previous_env = os.environ.get("PSU_UNIVERSAL_INTENT_LLM_FIRST")
    previous_llm_intent = universal_intent._llm_intent
    os.environ["PSU_UNIVERSAL_INTENT_LLM_FIRST"] = "1"

    def fake_llm_intent(_query: str, _route: PipelineRoute, _fallback: UniversalIntent):
        return (
            UniversalIntent(domain="general", operation="general_answer", confidence=0.80, method="llm", reason="fake"),
            {
                "llm_kind": "universal_intent",
                "llm_model": "fake",
                "llm_elapsed_ms": 12.34,
                "llm_parsed": True,
            },
        )

    universal_intent._llm_intent = fake_llm_intent
    try:
        _intent_result, trace = resolve_universal_intent(
            "คำถามนี้ยังไม่ชัดว่าต้องใช้ข้อมูลอะไร",
            _route("general", "unknown_domain_query", 0.55),
            allow_llm=True,
        )
    finally:
        universal_intent._llm_intent = previous_llm_intent
        if previous_env is None:
            os.environ.pop("PSU_UNIVERSAL_INTENT_LLM_FIRST", None)
        else:
            os.environ["PSU_UNIVERSAL_INTENT_LLM_FIRST"] = previous_env

    assert trace.metadata["llm_attempted"] is True
    assert trace.metadata["llm_call"]["llm_elapsed_ms"] == 12.34
    assert trace.metadata["llm_call"]["llm_kind"] == "universal_intent"


def test_facts_composer_trace_includes_llm_call_metadata() -> None:
    previous_env = os.environ.get("PSU_FACTS_LLM_COMPOSER")
    previous_call = facts_composer._call_ollama
    os.environ["PSU_FACTS_LLM_COMPOSER"] = "1"
    facts_composer._call_ollama = lambda _prompt: (
        "PS5 มีเกมทั้งหมด 2 เกม\n"
        "•    TEKKEN 8\n"
        "•    Minecraft\n"
        "แหล่งข้อมูล: local://games.json"
    )
    try:
        result = compose_structured_answer(
            question="PS5 มีเกมอะไรบ้าง",
            draft_answer=(
                "PS5 มีเกมทั้งหมด 2 เกม:\n"
                "•    TEKKEN 8\n"
                "•    Minecraft\n"
                "แหล่งข้อมูล: local://games.json"
            ),
            evidence={"platform": "ps5", "games": ["TEKKEN 8", "Minecraft"]},
            route=PipelineRoute("games", "list", 0.9, "list", "low", "smoke"),
            intent=UniversalIntent(domain="games", operation="list", confidence=0.9, method="smoke"),
            mode="structured_games_catalog",
            allow_llm=True,
        )
    finally:
        facts_composer._call_ollama = previous_call
        if previous_env is None:
            os.environ.pop("PSU_FACTS_LLM_COMPOSER", None)
        else:
            os.environ["PSU_FACTS_LLM_COMPOSER"] = previous_env

    assert result.used_llm
    assert result.trace.metadata["llm_call"]["llm_kind"] == "facts_composer"
    assert result.trace.metadata["llm_call"]["llm_elapsed_ms"] >= 0
    assert result.trace.metadata["llm_call"]["llm_response_chars"] > 0


def test_general_llm_blocked_for_psu_signal() -> None:
    fallback = build_experimental_fallback(
        "PS5 ราคาเท่าไหร่",
        _route("general", "unknown_domain_query", 0.55),
        started=0.0,
        allow_llm=True,
    )

    assert fallback.mode == "general_psu_scope_no_answer"
    assert fallback.trace.decision == "blocked_general_llm_for_psu_signal"
    assert fallback.trace.metadata["llm_attempted"] is False


def test_general_llm_trace_includes_llm_call_metadata() -> None:
    previous_call = experimental_fallback._general_llm_answer_with_metadata
    experimental_fallback._general_llm_answer_with_metadata = lambda _question: (
        "กรุงเทพมหานคร",
        {
            "llm_kind": "general_llm",
            "llm_model": "fake",
            "llm_elapsed_ms": 9.87,
            "llm_response_chars": 13,
        },
    )
    try:
        fallback = build_experimental_fallback(
            "เมืองหลวงประเทศไทยคืออะไร",
            _route("general", "general_knowledge_query", 0.55),
            started=0.0,
            allow_llm=True,
        )
    finally:
        experimental_fallback._general_llm_answer_with_metadata = previous_call

    assert fallback.mode == "general_llm_fallback"
    assert fallback.trace.metadata["llm_attempted"] is True
    assert fallback.trace.metadata["llm_call"]["llm_kind"] == "general_llm"
    assert fallback.trace.metadata["llm_call"]["llm_elapsed_ms"] == 9.87


def test_general_technical_explanation_does_not_route_to_games() -> None:
    result = answer_question_pipeline_debug(
        "อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ อธิบายแบบใช้กับวงการเกม",
        experimental_rag_fallback=True,
        experimental_allow_llm=False,
        global_timeout_sec=5.0,
    )

    assert result.route.category == "general", (result.route, result.answer)
    assert result.mode == "pipeline:general_llm_disabled", (result.mode, result.answer)
    assert result.elapsed < 5.0, result.elapsed


if __name__ == "__main__":
    test_universal_intent_trace_includes_llm_call_metadata()
    print("OK universal intent LLM timing metadata")
    test_facts_composer_trace_includes_llm_call_metadata()
    print("OK facts composer LLM timing metadata")
    test_general_llm_blocked_for_psu_signal()
    print("OK general LLM blocked for PSU signal")
    test_general_llm_trace_includes_llm_call_metadata()
    print("OK general LLM timing metadata")
    test_general_technical_explanation_does_not_route_to_games()
    print("OK technical explanation stays on general route")
    print("LLM TIMING AND GENERAL GUARD SMOKE TEST OK")
