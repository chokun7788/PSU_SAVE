from __future__ import annotations

import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import app.pipeline.facts_composer as facts_composer
import app.pipeline.llm_health as llm_health
import app.pipeline.llm_tool_router as tool_router
from app.pipeline.experimental_fallback import build_experimental_fallback
from app.pipeline.facts_composer import compose_structured_answer
from app.pipeline.llm_health import (
    llm_call_allowed,
    open_llm_circuit,
    record_llm_failure,
    release_llm_slot,
    reset_llm_health,
)
from app.pipeline.llm_tool_router import resolve_tool_routing
from app.pipeline.schemas import PipelineRoute, UniversalIntent
from app.pipeline.universal_intent import resolve_universal_intent


MODEL = os.getenv("PSU_CHATBOT_OLLAMA_MODEL", "scb10x/typhoon2.5-qwen3-4b")


def _route(category: str = "general", intent: str = "unknown_domain_query", confidence: float = 0.55) -> PipelineRoute:
    return PipelineRoute(category, intent, confidence, "general" if category == "general" else "fact", "low", "smoke")


def _intent(domain: str = "general", operation: str = "unknown", confidence: float = 0.45) -> UniversalIntent:
    return UniversalIntent(domain=domain, operation=operation, confidence=confidence, method="smoke")


def _trip_model_circuit(kind: str = "general_llm") -> None:
    reset_llm_health(MODEL)
    record_llm_failure(kind, MODEL, error_type="TimeoutError", error="timed out", elapsed_ms=5000)
    record_llm_failure(kind, MODEL, error_type="TimeoutError", error="timed out", elapsed_ms=5000)


def test_model_circuit_opens_after_failures() -> None:
    previous_threshold = os.environ.get("PSU_LLM_HEALTH_FAILURE_THRESHOLD")
    previous_cooldown = os.environ.get("PSU_LLM_HEALTH_COOLDOWN_SEC")
    os.environ["PSU_LLM_HEALTH_FAILURE_THRESHOLD"] = "2"
    os.environ["PSU_LLM_HEALTH_COOLDOWN_SEC"] = "60"
    try:
        _trip_model_circuit()
        allowed, health = llm_call_allowed("general_llm", MODEL)
    finally:
        reset_llm_health(MODEL)
        if previous_threshold is None:
            os.environ.pop("PSU_LLM_HEALTH_FAILURE_THRESHOLD", None)
        else:
            os.environ["PSU_LLM_HEALTH_FAILURE_THRESHOLD"] = previous_threshold
        if previous_cooldown is None:
            os.environ.pop("PSU_LLM_HEALTH_COOLDOWN_SEC", None)
        else:
            os.environ["PSU_LLM_HEALTH_COOLDOWN_SEC"] = previous_cooldown

    assert allowed is False
    assert health["llm_health_status"] == "cooldown"


def test_general_fallback_skips_when_circuit_open() -> None:
    _trip_model_circuit()
    try:
        fallback = build_experimental_fallback(
            "เมืองหลวงประเทศไทยคืออะไร",
            _route("general", "general_knowledge_query", 0.55),
            started=0.0,
            allow_llm=True,
        )
    finally:
        reset_llm_health(MODEL)

    assert fallback.mode == "general_llm_unavailable"
    assert fallback.trace.metadata["llm_call"]["llm_skipped_by_health"] is True
    assert fallback.trace.metadata["llm_call"]["llm_health_status"] == "cooldown"


def test_preflight_failure_opens_circuit_immediately() -> None:
    reset_llm_health(MODEL)
    try:
        health = open_llm_circuit(
            "preflight",
            MODEL,
            error_type="TimeoutError",
            error="preflight timed out",
            elapsed_ms=5000,
            cooldown_sec=60,
        )
        allowed, state = llm_call_allowed("general_llm", MODEL)
    finally:
        reset_llm_health(MODEL)

    assert health["llm_health_status"] == "cooldown"
    assert allowed is False
    assert state["llm_health_status"] == "cooldown"


def test_optional_planner_circuit_does_not_block_general_answer() -> None:
    previous_threshold = os.environ.get("PSU_LLM_HEALTH_FAILURE_THRESHOLD")
    previous_cooldown = os.environ.get("PSU_LLM_HEALTH_COOLDOWN_SEC")
    os.environ["PSU_LLM_HEALTH_FAILURE_THRESHOLD"] = "2"
    os.environ["PSU_LLM_HEALTH_COOLDOWN_SEC"] = "60"
    reset_llm_health(MODEL)
    try:
        record_llm_failure("query_planner", MODEL, error_type="TimeoutError", error="timed out", elapsed_ms=4000)
        record_llm_failure("query_planner", MODEL, error_type="TimeoutError", error="timed out", elapsed_ms=4000)
        planner_allowed, planner_health = llm_call_allowed("query_planner", MODEL)
        general_allowed, general_health = llm_call_allowed("general_llm", MODEL)
        if general_allowed:
            release_llm_slot()
    finally:
        reset_llm_health(MODEL)
        if previous_threshold is None:
            os.environ.pop("PSU_LLM_HEALTH_FAILURE_THRESHOLD", None)
        else:
            os.environ["PSU_LLM_HEALTH_FAILURE_THRESHOLD"] = previous_threshold
        if previous_cooldown is None:
            os.environ.pop("PSU_LLM_HEALTH_COOLDOWN_SEC", None)
        else:
            os.environ["PSU_LLM_HEALTH_COOLDOWN_SEC"] = previous_cooldown

    assert planner_allowed is False
    assert planner_health["llm_health_status"] == "cooldown"
    assert planner_health["llm_health_failure_scope"] == "kind_only"
    assert general_allowed is True
    assert general_health["llm_health_status"] == "ok"


def test_failures_outside_window_are_not_consecutive() -> None:
    previous_threshold = os.environ.get("PSU_LLM_HEALTH_FAILURE_THRESHOLD")
    previous_window = os.environ.get("PSU_LLM_HEALTH_FAILURE_WINDOW_SEC")
    previous_cooldown = os.environ.get("PSU_LLM_HEALTH_COOLDOWN_SEC")
    original_now = llm_health._now
    clock = {"value": 100.0}
    os.environ["PSU_LLM_HEALTH_FAILURE_THRESHOLD"] = "2"
    os.environ["PSU_LLM_HEALTH_FAILURE_WINDOW_SEC"] = "30"
    os.environ["PSU_LLM_HEALTH_COOLDOWN_SEC"] = "60"
    llm_health._now = lambda: clock["value"]
    reset_llm_health(MODEL)
    try:
        record_llm_failure("general_llm", MODEL, error_type="TimeoutError", error="first", elapsed_ms=8000)
        clock["value"] = 131.0
        health = record_llm_failure("general_llm", MODEL, error_type="TimeoutError", error="second", elapsed_ms=8000)
        allowed, state = llm_call_allowed("general_llm", MODEL)
        if allowed:
            release_llm_slot()
    finally:
        llm_health._now = original_now
        reset_llm_health(MODEL)
        if previous_threshold is None:
            os.environ.pop("PSU_LLM_HEALTH_FAILURE_THRESHOLD", None)
        else:
            os.environ["PSU_LLM_HEALTH_FAILURE_THRESHOLD"] = previous_threshold
        if previous_window is None:
            os.environ.pop("PSU_LLM_HEALTH_FAILURE_WINDOW_SEC", None)
        else:
            os.environ["PSU_LLM_HEALTH_FAILURE_WINDOW_SEC"] = previous_window
        if previous_cooldown is None:
            os.environ.pop("PSU_LLM_HEALTH_COOLDOWN_SEC", None)
        else:
            os.environ["PSU_LLM_HEALTH_COOLDOWN_SEC"] = previous_cooldown

    assert health["llm_health_status"] == "degraded"
    assert health["llm_health_failures"] == 1
    assert allowed is True
    assert state["llm_health_status"] == "ok"


def test_facts_composer_skips_when_circuit_open() -> None:
    previous_env = os.environ.get("PSU_FACTS_LLM_COMPOSER")
    os.environ["PSU_FACTS_LLM_COMPOSER"] = "1"
    _trip_model_circuit()
    try:
        result = compose_structured_answer(
            question="PS5 มีเกมอะไรบ้าง",
            draft_answer="PS5 มีเกมทั้งหมด 1 เกม\n•    TEKKEN 8",
            evidence={"games": ["TEKKEN 8"]},
            route=PipelineRoute("games", "list", 0.9, "list", "low", "smoke"),
            intent=UniversalIntent(domain="games", operation="list", confidence=0.9, method="smoke"),
            mode="structured_games_catalog",
            allow_llm=True,
        )
    finally:
        reset_llm_health(MODEL)
        if previous_env is None:
            os.environ.pop("PSU_FACTS_LLM_COMPOSER", None)
        else:
            os.environ["PSU_FACTS_LLM_COMPOSER"] = previous_env

    assert result.used_llm is False
    assert result.trace.decision == "llm_skipped_health"
    assert result.trace.metadata["llm_call"]["llm_skipped_by_health"] is True


def test_tool_router_skips_when_circuit_open() -> None:
    previous_env = os.environ.get("PSU_LLM_TOOL_ROUTER")
    previous_call = tool_router._call_ollama
    os.environ["PSU_LLM_TOOL_ROUTER"] = "1"
    called = {"value": False}

    def fake_call(_prompt: str):
        called["value"] = True
        return {"route_action": "general_llm"}

    tool_router._call_ollama = fake_call
    _trip_model_circuit()
    try:
        decision, trace = resolve_tool_routing(
            "คำถามนี้ยังไม่ชัด",
            _route("general", "unknown_domain_query", 0.55),
            _intent("general", "unknown", 0.45),
            allow_llm=True,
        )
    finally:
        tool_router._call_ollama = previous_call
        reset_llm_health(MODEL)
        if previous_env is None:
            os.environ.pop("PSU_LLM_TOOL_ROUTER", None)
        else:
            os.environ["PSU_LLM_TOOL_ROUTER"] = previous_env

    assert called["value"] is False
    assert decision.method == "heuristic"
    assert trace.metadata["llm_skipped_by_health"] is True


def test_universal_intent_skips_when_circuit_open() -> None:
    previous_env = os.environ.get("PSU_UNIVERSAL_INTENT_LLM_FIRST")
    os.environ["PSU_UNIVERSAL_INTENT_LLM_FIRST"] = "1"
    _trip_model_circuit("universal_intent")
    try:
        _intent_result, trace = resolve_universal_intent(
            "คำถามนี้ยังไม่ชัด",
            _route("general", "unknown_domain_query", 0.55),
            allow_llm=True,
        )
    finally:
        reset_llm_health(MODEL)
        if previous_env is None:
            os.environ.pop("PSU_UNIVERSAL_INTENT_LLM_FIRST", None)
        else:
            os.environ["PSU_UNIVERSAL_INTENT_LLM_FIRST"] = previous_env

    assert trace.metadata["llm_attempted"] is True
    assert trace.metadata["llm_call"]["llm_skipped_by_health"] is True


if __name__ == "__main__":
    test_model_circuit_opens_after_failures()
    print("OK model circuit opens")
    test_general_fallback_skips_when_circuit_open()
    print("OK general fallback skips on health cooldown")
    test_preflight_failure_opens_circuit_immediately()
    print("OK preflight failure opens circuit immediately")
    test_optional_planner_circuit_does_not_block_general_answer()
    print("OK optional planner circuit is isolated from general answer")
    test_failures_outside_window_are_not_consecutive()
    print("OK stale failures do not count as consecutive")
    test_facts_composer_skips_when_circuit_open()
    print("OK facts composer skips on health cooldown")
    test_tool_router_skips_when_circuit_open()
    print("OK tool router skips on health cooldown")
    test_universal_intent_skips_when_circuit_open()
    print("OK universal intent skips real Ollama on health cooldown")
    print("LLM HEALTH CIRCUIT BREAKER SMOKE TEST OK")
