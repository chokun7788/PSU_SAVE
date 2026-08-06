from __future__ import annotations

import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import app.pipeline.llm_tool_router as tool_router
import app.pipeline.engine as engine
from app.pipeline.llm_tool_router import ToolRoutingDecision, resolve_tool_routing
from app.pipeline.schemas import PipelineRoute, PipelineTrace, UniversalIntent


def _route(category: str = "general", intent: str = "unknown_domain_query", confidence: float = 0.55, risk: str = "low") -> PipelineRoute:
    return PipelineRoute(category, intent, confidence, "fact", risk, "smoke")


def _intent(domain: str = "general", operation: str = "unknown", confidence: float = 0.45) -> UniversalIntent:
    return UniversalIntent(domain=domain, operation=operation, confidence=confidence, method="smoke")


def test_disabled_uses_heuristic() -> None:
    previous = os.environ.get("PSU_LLM_TOOL_ROUTER")
    os.environ["PSU_LLM_TOOL_ROUTER"] = "0"
    try:
        decision, trace = resolve_tool_routing(
            "เมืองหลวงของประเทศไทยคืออะไร",
            _route("general", "general_knowledge_query", 0.86),
            _intent("general", "general_answer", 0.72),
            allow_llm=True,
        )
    finally:
        if previous is None:
            os.environ.pop("PSU_LLM_TOOL_ROUTER", None)
        else:
            os.environ["PSU_LLM_TOOL_ROUTER"] = previous
    assert decision.action == "general_llm"
    assert trace.metadata["llm_attempted"] is False


def test_enabled_accepts_retrieval_decision() -> None:
    previous = os.environ.get("PSU_LLM_TOOL_ROUTER")
    previous_call = tool_router._call_ollama
    os.environ["PSU_LLM_TOOL_ROUTER"] = "1"
    tool_router._call_ollama = lambda _prompt: {
        "route_action": "retrieval",
        "domain": "competition_rules",
        "operation": "rule_lookup",
        "needs_retrieval": True,
        "allow_general_llm": False,
        "confidence": 0.82,
        "reason": "asks about competition rules",
    }
    try:
        decision, trace = resolve_tool_routing(
            "Tekken 8 pause โดนลงโทษอะไร",
            _route("general", "unknown_domain_query", 0.55),
            _intent("general", "unknown", 0.45),
            allow_llm=True,
        )
    finally:
        tool_router._call_ollama = previous_call
        if previous is None:
            os.environ.pop("PSU_LLM_TOOL_ROUTER", None)
        else:
            os.environ["PSU_LLM_TOOL_ROUTER"] = previous
    assert decision.action == "retrieval"
    assert decision.domain == "competition_rules"
    assert decision.needs_retrieval is True
    assert trace.metadata["llm_attempted"] is True


def test_blocks_general_llm_for_psu_route() -> None:
    previous = os.environ.get("PSU_LLM_TOOL_ROUTER")
    previous_call = tool_router._call_ollama
    os.environ["PSU_LLM_TOOL_ROUTER"] = "1"
    tool_router._call_ollama = lambda _prompt: {
        "route_action": "general_llm",
        "domain": "general",
        "operation": "general_answer",
        "needs_retrieval": False,
        "allow_general_llm": True,
        "confidence": 0.90,
        "reason": "bad suggestion",
    }
    try:
        decision, trace = resolve_tool_routing(
            "PS5 อันนี้คืออะไร",
            _route("equipment", "equipment_lookup", 0.62, "low"),
            _intent("equipment", "unknown", 0.45),
            allow_llm=True,
        )
    finally:
        tool_router._call_ollama = previous_call
        if previous is None:
            os.environ.pop("PSU_LLM_TOOL_ROUTER", None)
        else:
            os.environ["PSU_LLM_TOOL_ROUTER"] = previous
    assert decision.action != "general_llm"
    assert decision.allow_general_llm is False
    assert trace.metadata["sanitizer"] == "blocked_general_llm_for_psu_route"


def test_engine_can_refine_general_to_retrieval_route() -> None:
    previous = engine.resolve_tool_routing

    def fake_resolve(_question: str, _route: PipelineRoute, _intent: UniversalIntent, *, allow_llm: bool):
        return (
            ToolRoutingDecision(
                action="retrieval",
                domain="competition_rules",
                operation="rule_lookup",
                confidence=0.82,
                needs_retrieval=True,
                allow_general_llm=False,
                reason="fake retrieval route",
                method="llm",
            ),
            PipelineTrace(
                "tool_router",
                "llm:retrieval",
                0.82,
                "fake retrieval route",
                {"method": "llm", "llm_attempted": True},
            ),
        )

    engine.resolve_tool_routing = fake_resolve
    try:
        result = engine.answer_question_pipeline_debug(
            "ขอข้อมูลเอกสารกติกาที่เกี่ยวข้อง",
            experimental_rag_fallback=False,
            experimental_allow_llm=True,
        )
    finally:
        engine.resolve_tool_routing = previous

    assert any(item.stage == "tool_route_refine" for item in result.trace)
    assert result.route.category == "competition_rules"


if __name__ == "__main__":
    test_disabled_uses_heuristic()
    print("OK tool router disabled heuristic")
    test_enabled_accepts_retrieval_decision()
    print("OK tool router accepts retrieval decision")
    test_blocks_general_llm_for_psu_route()
    print("OK tool router blocks unsafe general LLM")
    test_engine_can_refine_general_to_retrieval_route()
    print("OK engine can refine route from tool router")
    print("LLM TOOL ROUTER SMOKE TEST OK")
