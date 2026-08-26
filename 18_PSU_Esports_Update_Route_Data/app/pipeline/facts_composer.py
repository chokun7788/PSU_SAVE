from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from contextvars import ContextVar
from dataclasses import dataclass
from typing import Any

from app.pipeline.claim_validator import validate_grounded_claims
from app.pipeline.llm_health import llm_call_allowed, record_llm_failure, record_llm_success, release_llm_slot
from app.pipeline.request_deadline import deadline_metadata, timeout_for_call
from app.pipeline.schemas import PipelineRoute, PipelineTrace, UniversalIntent


DEFAULT_OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434")
DEFAULT_MODEL = os.getenv("PSU_CHATBOT_OLLAMA_MODEL", "scb10x/typhoon2.5-qwen3-4b")
DEFAULT_TIMEOUT_SEC = float(os.getenv("PSU_FACTS_LLM_TIMEOUT_SEC", "5.0"))
DEFAULT_NUM_PREDICT = int(os.getenv("PSU_FACTS_LLM_NUM_PREDICT", "192"))

COMPOSABLE_MODES = {
    "structured_members_group_count",
    "structured_members_group_list",
    "structured_games_catalog",
    "structured_game_detail",
    "structured_equipment_catalog",
    "structured_equipment_item",
    "structured_schedule",
    "structured_reservation_fact",
    "structured_service_fee",
}

RAG_COMPOSABLE_MODES = {
    "rag_direct_curated",
    "hybrid_guarded_rerank",
    "guarded_vector_direct",
    "semantic_rag_dynamic",
}
ALL_COMPOSABLE_MODES = COMPOSABLE_MODES | RAG_COMPOSABLE_MODES
_LAST_CALL_METADATA: ContextVar[dict[str, Any]] = ContextVar("facts_composer_call_metadata", default={})


@dataclass(frozen=True)
class FactsComposerResult:
    answer: str
    used_llm: bool
    trace: PipelineTrace


def _truthy(value: str | None) -> bool:
    return (value or "").strip().lower() in {"1", "true", "yes", "y", "on"}


def env_facts_composer_default() -> bool:
    return _truthy(os.getenv("PSU_FACTS_LLM_COMPOSER"))


def env_rag_composer_default() -> bool:
    explicit = os.getenv("PSU_RAG_LLM_COMPOSER")
    if explicit is not None:
        return _truthy(explicit)
    return _truthy(os.getenv("PSU_MODEL_FIRST_FLOW"))


def _ollama_think_value() -> bool | str:
    raw = os.getenv("PSU_OLLAMA_THINK", "false").strip().lower()
    if raw in {"1", "true", "yes", "y", "on"}:
        return True
    if raw in {"low", "medium", "high", "max"}:
        return raw
    return False


def _json_compact(value: Any, max_chars: int = 2600) -> str:
    text = json.dumps(value, ensure_ascii=False, default=str, indent=2)
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rstrip() + "\n... truncated"


def _composer_evidence(evidence: dict[str, Any]) -> dict[str, Any]:
    items: list[dict[str, Any]] = []
    for item in evidence.get("items") or []:
        if not isinstance(item, dict):
            continue
        items.append({
            "title": str(item.get("title") or ""),
            "text": str(item.get("text") or ""),
            "source_url": str(item.get("source_url") or ""),
        })
    return {"item_count": len(items), "items": items}


def _build_prompt(
    *,
    question: str,
    draft_answer: str,
    evidence: dict[str, Any],
    route: PipelineRoute,
    intent: UniversalIntent,
) -> str:
    compact_evidence = _composer_evidence(evidence)
    return f"""เรียบเรียงคำตอบภาษาไทยสำหรับ PSU Esports Studio - Phuket จากหลักฐานเท่านั้น
กฎ: ห้ามเพิ่มข้อเท็จจริง ตัวเลข ชื่อ ราคา เวลา หรือกฎใหม่ รักษาข้อมูลเดิม และตอบคำตอบหลักก่อน
ถ้ามีหลายหลักฐาน ให้สรุปแต่ละประเด็นเป็น bullet ไม่เกิน 15 คำ ตัดรายละเอียดรอง และไม่ต้องพิมพ์แหล่งข้อมูลเพราะระบบจะเติมให้

คำถาม:
{question}

เส้นทาง:
{route.category}/{route.intent}

เจตนา:
{intent.domain}/{intent.operation}

หลักฐาน JSON:
{_json_compact(compact_evidence, max_chars=3200)}

ร่างคำตอบ:
{draft_answer}

คำตอบสุดท้าย:"""


def _call_ollama(prompt: str) -> str:
    timeout = timeout_for_call(float(os.getenv("PSU_FACTS_LLM_TIMEOUT_SEC", str(DEFAULT_TIMEOUT_SEC))))
    if timeout <= 0:
        raise TimeoutError("global request deadline exhausted before facts composer LLM call")
    payload = {
        "model": os.getenv("PSU_FACTS_LLM_MODEL", DEFAULT_MODEL),
        "prompt": prompt,
        # Streaming lets the client close the response socket when the stage
        # budget expires instead of waiting for one large buffered response.
        "stream": True,
        "keep_alive": os.getenv("PSU_OLLAMA_KEEP_ALIVE", "10m"),
        "think": _ollama_think_value(),
        "options": {
            "temperature": 0.05,
            "top_p": 0.75,
            "num_predict": int(os.getenv("PSU_FACTS_LLM_NUM_PREDICT", str(DEFAULT_NUM_PREDICT))),
            "num_ctx": int(os.getenv("PSU_FACTS_LLM_NUM_CTX", "3072")),
        },
    }
    request = urllib.request.Request(
        f"{os.getenv('OLLAMA_URL', DEFAULT_OLLAMA_URL).rstrip('/')}/api/generate",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    response = None
    chunks: list[str] = []
    call_metadata: dict[str, Any] = {}
    try:
        response = urllib.request.urlopen(request, timeout=timeout)
        for raw_line in response:
            line = raw_line.decode("utf-8", errors="replace").strip()
            if not line:
                continue
            data = json.loads(line)
            chunks.append(str(data.get("response") or ""))
            if data.get("done"):
                call_metadata = {
                    "llm_done_reason": str(data.get("done_reason") or "stop"),
                    "llm_prompt_eval_count": int(data.get("prompt_eval_count") or 0),
                    "llm_eval_count": int(data.get("eval_count") or 0),
                    "llm_load_duration_ms": round(float(data.get("load_duration") or 0) / 1_000_000, 2),
                    "llm_prompt_eval_duration_ms": round(float(data.get("prompt_eval_duration") or 0) / 1_000_000, 2),
                    "llm_eval_duration_ms": round(float(data.get("eval_duration") or 0) / 1_000_000, 2),
                }
                break
        _LAST_CALL_METADATA.set(call_metadata)
        return "".join(chunks).strip()
    finally:
        # Closing the streaming response is the strongest cancellation Ollama
        # exposes through the local HTTP API when a request budget expires.
        if response is not None:
            response.close()


def _looks_unsafe(answer: str, draft_answer: str) -> str:
    if not answer.strip():
        return "empty_answer"
    if "FINAL_ANSWER" in answer or "FACTS_JSON" in answer:
        return "prompt_leak"
    source_markers = [line for line in draft_answer.splitlines() if line.strip().startswith("แหล่งข้อมูล:")]
    if source_markers and not any(marker in answer for marker in source_markers):
        return "missing_source_line"
    for line in source_markers:
        if line not in answer:
            return "source_line_changed"
    return ""


def _restore_exact_source_markers(answer: str, draft_answer: str) -> tuple[str, int]:
    source_markers = [line.strip() for line in draft_answer.splitlines() if line.strip().startswith("แหล่งข้อมูล:")]
    answer_source_markers = [line.strip() for line in answer.splitlines() if line.strip().startswith("แหล่งข้อมูล:")]
    if any(marker not in source_markers for marker in answer_source_markers):
        return answer, 0
    missing = [marker for marker in source_markers if marker not in answer]
    if not answer.strip() or not missing:
        return answer, 0
    return answer.rstrip() + "\n" + "\n".join(missing), len(missing)


def compose_structured_answer(
    *,
    question: str,
    draft_answer: str,
    evidence: dict[str, Any],
    route: PipelineRoute,
    intent: UniversalIntent,
    mode: str,
    allow_llm: bool,
) -> FactsComposerResult:
    if not allow_llm:
        return FactsComposerResult(
            draft_answer,
            False,
            PipelineTrace("facts_composer", "disabled", 0.0, "experimental_allow_llm is false"),
        )
    is_rag_mode = mode in RAG_COMPOSABLE_MODES
    if is_rag_mode and not env_rag_composer_default():
        return FactsComposerResult(
            draft_answer,
            False,
            PipelineTrace("facts_composer", "disabled_rag", 0.0, "PSU_RAG_LLM_COMPOSER is not enabled"),
        )
    if not is_rag_mode and not env_facts_composer_default():
        return FactsComposerResult(
            draft_answer,
            False,
            PipelineTrace("facts_composer", "disabled", 0.0, "PSU_FACTS_LLM_COMPOSER is not enabled"),
        )
    if mode not in ALL_COMPOSABLE_MODES:
        return FactsComposerResult(
            draft_answer,
            False,
            PipelineTrace("facts_composer", "skipped_mode", 0.0, mode),
        )

    prompt = _build_prompt(
            question=question,
            draft_answer=draft_answer,
            evidence=evidence,
            route=route,
            intent=intent,
        )
    model = os.getenv("PSU_FACTS_LLM_MODEL", DEFAULT_MODEL)
    configured_timeout_sec = float(os.getenv("PSU_FACTS_LLM_TIMEOUT_SEC", str(DEFAULT_TIMEOUT_SEC)))
    timeout_sec = timeout_for_call(configured_timeout_sec)
    num_predict = int(os.getenv("PSU_FACTS_LLM_NUM_PREDICT", str(DEFAULT_NUM_PREDICT)))
    allowed, health = llm_call_allowed("facts_composer", model)
    if not allowed:
        return FactsComposerResult(
            draft_answer,
            False,
            PipelineTrace(
                "facts_composer",
                "llm_skipped_health",
                0.35,
                "LLM circuit breaker cooldown active",
                {
                    "model": model,
                    "llm_call": {
                        "llm_kind": "facts_composer",
                        "llm_model": model,
                        "llm_timeout_sec": timeout_sec,
                        "llm_configured_timeout_sec": configured_timeout_sec,
                        "llm_num_predict": num_predict,
                        "llm_prompt_chars": len(prompt),
                        "llm_elapsed_ms": 0.0,
                        "llm_response_chars": 0,
                        "llm_skipped_by_health": True,
                        **deadline_metadata(),
                        **health,
                    },
                },
            ),
        )
    call_started = time.perf_counter()
    if timeout_sec <= 0:
        release_llm_slot()
        return FactsComposerResult(
            draft_answer,
            False,
            PipelineTrace(
                "facts_composer",
                "llm_skipped_deadline",
                0.35,
                "global request deadline exhausted before facts composer",
                {
                    "model": model,
                    "llm_call": {
                        "llm_kind": "facts_composer",
                        "llm_model": model,
                        "llm_timeout_sec": timeout_sec,
                        "llm_configured_timeout_sec": configured_timeout_sec,
                        "llm_num_predict": num_predict,
                        "llm_prompt_chars": len(prompt),
                        "llm_elapsed_ms": 0.0,
                        "llm_response_chars": 0,
                        "llm_skipped_by_deadline": True,
                        **deadline_metadata(),
                    },
                },
            ),
        )
    try:
        _LAST_CALL_METADATA.set({})
        answer = _call_ollama(prompt)
    except (urllib.error.URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
        elapsed_ms = (time.perf_counter() - call_started) * 1000
        health = record_llm_failure(
            "facts_composer",
            model,
            error_type=type(exc).__name__,
            error=str(exc),
            elapsed_ms=elapsed_ms,
        )
        return FactsComposerResult(
            draft_answer,
            False,
            PipelineTrace(
                "facts_composer",
                "llm_unavailable",
                0.35,
                f"{type(exc).__name__}: {exc}",
                {
                    "model": model,
                    "llm_call": {
                        "llm_kind": "facts_composer",
                        "llm_model": model,
                        "llm_timeout_sec": timeout_sec,
                        "llm_configured_timeout_sec": configured_timeout_sec,
                        "llm_num_predict": num_predict,
                        "llm_prompt_chars": len(prompt),
                        "llm_elapsed_ms": round(elapsed_ms, 2),
                        "llm_response_chars": 0,
                        "llm_error_type": type(exc).__name__,
                        "llm_error": str(exc),
                        **health,
                    },
                },
            ),
        )

    ollama_call_metadata = dict(_LAST_CALL_METADATA.get())
    answer, restored_source_marker_count = _restore_exact_source_markers(answer, draft_answer)
    elapsed_ms = (time.perf_counter() - call_started) * 1000
    if answer:
        health = record_llm_success("facts_composer", model, elapsed_ms=elapsed_ms)
    else:
        health = record_llm_failure(
            "facts_composer",
            model,
            error_type="EmptyResponse",
            error="empty response",
            elapsed_ms=elapsed_ms,
        )
    llm_call = {
        "llm_kind": "facts_composer",
        "llm_model": model,
        "llm_timeout_sec": timeout_sec,
        "llm_configured_timeout_sec": configured_timeout_sec,
        "llm_num_predict": num_predict,
        "llm_prompt_chars": len(prompt),
        "llm_elapsed_ms": round(elapsed_ms, 2),
        "llm_response_chars": len(answer),
        "llm_source_markers_restored": restored_source_marker_count,
        **ollama_call_metadata,
        **deadline_metadata(),
        **health,
    }
    unsafe_reason = _looks_unsafe(answer, draft_answer)
    if not unsafe_reason and ollama_call_metadata.get("llm_done_reason") in {"length", "timeout_partial"}:
        unsafe_reason = "incomplete_generation"
    if not unsafe_reason and is_rag_mode:
        grounding = validate_grounded_claims(answer, evidence)
        llm_call["grounding_validation"] = grounding.as_dict()
        if not grounding.ok:
            unsafe_reason = "unsupported_grounded_claim"
    if unsafe_reason:
        return FactsComposerResult(
            draft_answer,
            False,
            PipelineTrace("facts_composer", "rejected", 0.35, unsafe_reason, {"llm_call": llm_call}),
        )
    return FactsComposerResult(
        answer,
        True,
        PipelineTrace(
            "facts_composer",
            "llm_composed",
            0.72,
            "facts-only composer rewrote structured draft",
            {"model": model, "mode": mode, "llm_call": llm_call},
        ),
    )
