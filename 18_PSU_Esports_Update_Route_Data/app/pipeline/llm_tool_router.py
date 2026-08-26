from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any

from app.pipeline.chatbot_role import CHATBOT_ROLE_TH, TOOL_ROUTER_ROLE
from app.pipeline.llm_health import llm_call_allowed, record_llm_failure, record_llm_success, release_llm_slot
from app.pipeline.request_deadline import deadline_metadata, timeout_for_call
from app.pipeline.schemas import PipelineRoute, PipelineTrace, UniversalIntent


ROUTE_ACTIONS = {
    "structured",
    "fast_path",
    "rulebase",
    "retrieval",
    "vector",
    "general_llm",
    "rag_llm",
    "clarification",
    "no_answer",
}

HIGH_TRUST_DOMAINS = {
    "members",
    "games",
    "game_controls",
    "equipment",
    "reservation",
    "service_fee",
    "schedule",
}


@dataclass(frozen=True)
class ToolRoutingDecision:
    action: str
    domain: str
    operation: str
    confidence: float
    needs_retrieval: bool
    allow_general_llm: bool
    reason: str
    method: str = "heuristic"


def _truthy(value: str | None) -> bool:
    return (value or "").strip().lower() in {"1", "true", "yes", "y", "on"}


def env_llm_tool_router_default() -> bool:
    return _truthy(os.getenv("PSU_LLM_TOOL_ROUTER", "0"))


def _extract_json_object(text: str) -> dict[str, Any] | None:
    text = text.strip()
    if not text:
        return None
    try:
        value = json.loads(text)
        return value if isinstance(value, dict) else None
    except json.JSONDecodeError:
        pass
    start = text.find("{")
    end = text.rfind("}")
    if start < 0 or end <= start:
        return None
    try:
        value = json.loads(text[start:end + 1])
        return value if isinstance(value, dict) else None
    except json.JSONDecodeError:
        return None


def _heuristic_decision(route: PipelineRoute, intent: UniversalIntent) -> ToolRoutingDecision:
    if intent.domain in HIGH_TRUST_DOMAINS and intent.operation != "unknown" and intent.confidence >= 0.78:
        return ToolRoutingDecision(
            "structured",
            intent.domain,
            intent.operation,
            intent.confidence,
            False,
            False,
            "high-confidence structured domain",
        )
    if route.category == "general":
        return ToolRoutingDecision(
            "general_llm",
            intent.domain,
            intent.operation,
            max(intent.confidence, route.confidence),
            False,
            True,
            "general route can use local LLM fallback",
        )
    if route.category in {"competition_rules", "knowledge", "contact"}:
        return ToolRoutingDecision(
            "retrieval",
            intent.domain,
            intent.operation,
            max(intent.confidence, 0.62),
            True,
            False,
            "domain likely needs retrieval or curated facts",
        )
    return ToolRoutingDecision(
        "fast_path",
        intent.domain,
        intent.operation,
        max(intent.confidence, 0.55),
        False,
        False,
        "default deterministic pipeline order",
    )


def _should_call_llm(route: PipelineRoute, intent: UniversalIntent, heuristic: ToolRoutingDecision) -> bool:
    if route.risk in {"medium", "high"} and route.confidence >= 0.94:
        return False
    if intent.domain in HIGH_TRUST_DOMAINS and intent.operation != "unknown" and intent.confidence >= float(os.getenv("PSU_TOOL_ROUTER_SKIP_CONFIDENCE", "0.86")):
        return False
    if heuristic.action in {"structured", "fast_path"} and intent.confidence >= 0.82:
        return False
    return (
        route.category in {"general", "unknown", "no_answer"}
        or intent.operation == "unknown"
        or intent.confidence < float(os.getenv("PSU_TOOL_ROUTER_CALL_CONFIDENCE", "0.76"))
    )


def _build_prompt(question: str, route: PipelineRoute, intent: UniversalIntent) -> str:
    actions = ", ".join(sorted(ROUTE_ACTIONS))
    return f"""{CHATBOT_ROLE_TH}

{TOOL_ROUTER_ROLE}
Choose the next answer strategy. Return compact JSON only.

Allowed route_action values: {actions}

Definitions:
- structured: use structured facts/tools for members, games, controls, equipment, schedule, reservation, service_fee.
- fast_path: use deterministic Python handlers/calculators before retrieval.
- rulebase: use pattern rules from data/rules.
- retrieval: use curated/hybrid/BM25/vector retrieval for PSU documents.
- vector: use guarded vector search, especially game controls.
- general_llm: answer general knowledge outside PSU without PSU context.
- rag_llm: summarize retrieved PSU context with the model.
- clarification: ask a short clarifying question because target/context is missing.
- no_answer: answer that verified PSU data is unavailable.

Rules:
- Do not choose general_llm for PSU-specific questions about price, schedule, reservation, members, equipment, games, controls, or competition rules.
- Prefer structured for clear domains with facts.
- Prefer fast_path for calculations such as price/time.
- Prefer retrieval for competition rules, contact, knowledge, or unclear document questions.
- Prefer clarification if the question asks controls/how-to but does not name a game and no context is available.

Question: {question}
Current router: category={route.category}, intent={route.intent}, confidence={route.confidence}, risk={route.risk}
Universal intent: domain={intent.domain}, operation={intent.operation}, confidence={intent.confidence}, target={intent.target}

Return JSON:
{{"route_action":"structured|fast_path|rulebase|retrieval|vector|general_llm|rag_llm|clarification|no_answer","domain":"...","operation":"...","needs_retrieval":false,"allow_general_llm":false,"confidence":0.0,"reason":"..."}}"""


def _call_ollama(prompt: str) -> dict[str, Any] | None:
    url = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434").rstrip("/") + "/api/generate"
    model = os.getenv("PSU_TOOL_ROUTER_MODEL") or os.getenv("PSU_CHATBOT_OLLAMA_MODEL", "scb10x/typhoon2.5-qwen3-4b")
    num_ctx = max(
        1024,
        int(os.getenv("PSU_TOOL_ROUTER_NUM_CTX", os.getenv("PSU_GENERAL_LLM_NUM_CTX", "3072"))),
    )
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "think": False,
        "keep_alive": os.getenv("PSU_OLLAMA_KEEP_ALIVE", "10m"),
        "options": {
            "temperature": 0,
            "num_predict": int(os.getenv("PSU_TOOL_ROUTER_NUM_PREDICT", "160")),
            "num_ctx": num_ctx,
        },
    }
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    timeout = timeout_for_call(float(os.getenv("PSU_TOOL_ROUTER_TIMEOUT_SEC", "1.2")))
    if timeout <= 0:
        raise TimeoutError("global request deadline exhausted before tool router LLM call")
    with urllib.request.urlopen(request, timeout=timeout) as response:
        data = json.loads(response.read().decode("utf-8", errors="replace"))
    return _extract_json_object(str(data.get("response") or ""))


def _coerce_decision(data: dict[str, Any], fallback: ToolRoutingDecision) -> ToolRoutingDecision:
    action = str(data.get("route_action") or data.get("action") or fallback.action).strip().lower()
    if action not in ROUTE_ACTIONS:
        action = fallback.action
    try:
        confidence = float(data.get("confidence", fallback.confidence))
    except (TypeError, ValueError):
        confidence = fallback.confidence
    confidence = max(0.0, min(0.98, confidence))
    return ToolRoutingDecision(
        action=action,
        domain=str(data.get("domain") or fallback.domain).strip().lower(),
        operation=str(data.get("operation") or fallback.operation).strip().lower(),
        confidence=round(confidence, 3),
        needs_retrieval=bool(data.get("needs_retrieval", fallback.needs_retrieval)),
        allow_general_llm=bool(data.get("allow_general_llm", fallback.allow_general_llm)),
        reason=str(data.get("reason") or fallback.reason),
        method="llm",
    )


def _sanitize_decision(decision: ToolRoutingDecision, route: PipelineRoute, intent: UniversalIntent) -> tuple[ToolRoutingDecision, str]:
    if decision.action == "general_llm" and (route.category != "general" or intent.domain not in {"general", "knowledge"}):
        return (
            ToolRoutingDecision(
                action="retrieval" if decision.needs_retrieval else _heuristic_decision(route, intent).action,
                domain=decision.domain,
                operation=decision.operation,
                confidence=min(decision.confidence, 0.60),
                needs_retrieval=decision.needs_retrieval,
                allow_general_llm=False,
                reason=f"{decision.reason}; blocked unsafe general_llm for PSU route",
                method=decision.method,
            ),
            "blocked_general_llm_for_psu_route",
        )
    if route.risk in {"medium", "high"} and route.confidence >= 0.94 and decision.action not in {"fast_path", "structured", "retrieval"}:
        heuristic = _heuristic_decision(route, intent)
        return (
            ToolRoutingDecision(
                action=heuristic.action,
                domain=decision.domain,
                operation=decision.operation,
                confidence=min(decision.confidence, route.confidence),
                needs_retrieval=heuristic.needs_retrieval,
                allow_general_llm=False,
                reason=f"{decision.reason}; kept high-risk deterministic route",
                method=decision.method,
            ),
            "kept_high_risk_route",
        )
    return decision, ""


def resolve_tool_routing(
    question: str,
    route: PipelineRoute,
    intent: UniversalIntent,
    *,
    allow_llm: bool,
) -> tuple[ToolRoutingDecision, PipelineTrace]:
    heuristic = _heuristic_decision(route, intent)
    if not allow_llm:
        return heuristic, PipelineTrace(
            "tool_router",
            f"heuristic:{heuristic.action}",
            heuristic.confidence,
            "experimental_allow_llm is false",
            {"method": "heuristic", "llm_attempted": False},
        )
    if not env_llm_tool_router_default():
        return heuristic, PipelineTrace(
            "tool_router",
            f"heuristic:{heuristic.action}",
            heuristic.confidence,
            "PSU_LLM_TOOL_ROUTER is not enabled",
            {"method": "heuristic", "llm_attempted": False},
        )
    if not _should_call_llm(route, intent, heuristic):
        return heuristic, PipelineTrace(
            "tool_router",
            f"heuristic:{heuristic.action}",
            heuristic.confidence,
            "heuristic route is confident enough",
            {"method": "heuristic", "llm_attempted": False},
        )

    prompt = _build_prompt(question, route, intent)
    model = os.getenv("PSU_TOOL_ROUTER_MODEL") or os.getenv("PSU_CHATBOT_OLLAMA_MODEL", "scb10x/typhoon2.5-qwen3-4b")
    configured_timeout_sec = float(os.getenv("PSU_TOOL_ROUTER_TIMEOUT_SEC", "1.2"))
    timeout_sec = timeout_for_call(configured_timeout_sec)
    num_predict = int(os.getenv("PSU_TOOL_ROUTER_NUM_PREDICT", "96"))
    allowed, health = llm_call_allowed("tool_router", model)
    if not allowed:
        return heuristic, PipelineTrace(
            "tool_router",
            f"heuristic:{heuristic.action}",
            heuristic.confidence,
            "LLM circuit breaker cooldown active",
            {
                "method": "heuristic",
                "llm_attempted": False,
                "llm_skipped_by_health": True,
                "llm_call": {
                    "llm_kind": "tool_router",
                    "llm_model": model,
                    "llm_timeout_sec": timeout_sec,
                    "llm_configured_timeout_sec": configured_timeout_sec,
                    "llm_num_predict": num_predict,
                    "llm_prompt_chars": len(prompt),
                    "llm_elapsed_ms": 0.0,
                    "llm_parsed": False,
                    "llm_skipped_by_health": True,
                    **health,
                },
            },
        )
    call_started = time.perf_counter()
    if timeout_sec <= 0:
        release_llm_slot()
        return heuristic, PipelineTrace(
            "tool_router",
            f"heuristic:{heuristic.action}",
            heuristic.confidence,
            "global request deadline exhausted before LLM tool router",
            {
                "method": "heuristic",
                "llm_attempted": False,
                "llm_call": {
                    "llm_kind": "tool_router",
                    "llm_model": model,
                    "llm_timeout_sec": timeout_sec,
                    "llm_configured_timeout_sec": configured_timeout_sec,
                    "llm_num_predict": num_predict,
                    "llm_prompt_chars": len(prompt),
                    "llm_elapsed_ms": 0.0,
                    "llm_parsed": False,
                    "llm_skipped_by_deadline": True,
                    **deadline_metadata(),
                },
            },
        )
    try:
        parsed = _call_ollama(prompt)
    except (OSError, TimeoutError, urllib.error.URLError, json.JSONDecodeError) as exc:
        elapsed_ms = (time.perf_counter() - call_started) * 1000
        health = record_llm_failure(
            "tool_router",
            model,
            error_type=type(exc).__name__,
            error=str(exc),
            elapsed_ms=elapsed_ms,
        )
        return heuristic, PipelineTrace(
            "tool_router",
            f"heuristic:{heuristic.action}",
            heuristic.confidence,
            f"llm_unavailable: {type(exc).__name__}: {exc}",
            {
                "method": "heuristic",
                "llm_attempted": True,
                "llm_call": {
                    "llm_kind": "tool_router",
                    "llm_model": model,
                    "llm_timeout_sec": timeout_sec,
                    "llm_configured_timeout_sec": configured_timeout_sec,
                    "llm_num_predict": num_predict,
                    "llm_prompt_chars": len(prompt),
                    "llm_elapsed_ms": round(elapsed_ms, 2),
                    "llm_parsed": False,
                    "llm_error_type": type(exc).__name__,
                    "llm_error": str(exc),
                    **health,
                },
            },
        )
    llm_elapsed_ms = round((time.perf_counter() - call_started) * 1000, 2)
    if parsed:
        health = record_llm_success("tool_router", model, elapsed_ms=llm_elapsed_ms)
    else:
        health = record_llm_failure(
            "tool_router",
            model,
            error_type="NoParse",
            error="llm returned no parseable JSON",
            elapsed_ms=llm_elapsed_ms,
        )
    llm_call = {
        "llm_kind": "tool_router",
        "llm_model": model,
        "llm_timeout_sec": timeout_sec,
        "llm_configured_timeout_sec": configured_timeout_sec,
        "llm_num_predict": num_predict,
        "llm_prompt_chars": len(prompt),
        "llm_elapsed_ms": llm_elapsed_ms,
        "llm_parsed": bool(parsed),
        **deadline_metadata(),
        **health,
    }
    if not parsed:
        return heuristic, PipelineTrace(
            "tool_router",
            f"heuristic:{heuristic.action}",
            heuristic.confidence,
            "llm returned no parseable JSON",
            {"method": "heuristic", "llm_attempted": True, "llm_call": llm_call},
        )

    decision, sanitizer = _sanitize_decision(_coerce_decision(parsed, heuristic), route, intent)
    return decision, PipelineTrace(
        "tool_router",
        f"{decision.method}:{decision.action}",
        decision.confidence,
        decision.reason,
        {
            "method": decision.method,
            "llm_attempted": True,
            "domain": decision.domain,
            "operation": decision.operation,
            "needs_retrieval": decision.needs_retrieval,
            "allow_general_llm": decision.allow_general_llm,
            "heuristic_action": heuristic.action,
            "sanitizer": sanitizer,
            "llm_call": llm_call,
        },
    )
