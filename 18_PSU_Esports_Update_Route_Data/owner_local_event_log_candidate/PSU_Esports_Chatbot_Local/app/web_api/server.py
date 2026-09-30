from __future__ import annotations

import argparse
import json
import mimetypes
import os
import sys
import threading
import time
import uuid
from dataclasses import asdict, is_dataclass
from datetime import UTC, datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, unquote, urlparse

from app.calendar.service_calendar import calendar_context
from app.core.locale import (
    LocaleDecision,
    bilingual_english_enabled,
    normalize_requested_locale,
    resolve_locale,
)
from app.core.runtime_input_quality_guard import (
    InputQualityDecision,
    RuntimeInputQualityGuard,
    keyboard_guard_enabled,
)
from app.pipeline.input_recovery import inspect_surface_input
from app.pipeline.llm_health import llm_health_snapshot, llm_preflight_enabled, preflight_ollama
from app.pipeline.request_deadline import deadline_metadata, request_deadline
from app.pipeline.semantic_embeddings import embedding_model_name, semantic_retrieval_enabled
from app.pipeline.warmup import WarmupResult, pipeline_warmup_enabled, warm_pipeline_caches
from app.runtime.pipeline_answer import answer_question_pipeline_debug
from app.session.context_resolver import resolve_question_with_context
from app.session.chat_logger import is_valid_session_id, read_sqlite_session_history, write_chat_log
from app.session.intent_feedback import write_intent_feedback
from app.web_api.pipeline_supervisor import PipelineWorkerSupervisor, worker_supervisor_enabled


PROJECT_ROOT = Path(__file__).resolve().parents[2]
WEB_ROOT = PROJECT_ROOT / "web_chat"
LOG_DIR = PROJECT_ROOT / "data" / "logs"
MAX_BODY_BYTES = 128 * 1024
MAX_QUESTION_CHARS = 4000


def _env_int(name: str, default: int, *, minimum: int = 0) -> int:
    try:
        return max(minimum, int(os.getenv(name, str(default))))
    except ValueError:
        return default


def _env_float(name: str, default: float, *, minimum: float = 0.0) -> float:
    try:
        return max(minimum, float(os.getenv(name, str(default))))
    except ValueError:
        return default


def _env_bool(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


MAX_ACTIVE_REQUESTS = _env_int("PSU_MAX_ACTIVE_REQUESTS", 16, minimum=1)
SESSION_LOCK_WAIT_SEC = _env_float("PSU_SESSION_LOCK_WAIT_SEC", 0.10)
LOCAL_LLM_ASSIST_ENABLED = _env_bool("PSU_LOCAL_LLM_ASSIST_ENABLED", True)
STARTUP_WARMUP: WarmupResult | None = None
STARTUP_LLM_PREFLIGHT: dict[str, Any] | None = None
STARTUP_INPUT_QUALITY_GUARD: dict[str, Any] | None = None
INPUT_QUALITY_GUARD: RuntimeInputQualityGuard | None = None
PIPELINE_SUPERVISOR: PipelineWorkerSupervisor | None = None
_ACTIVE_REQUESTS = threading.BoundedSemaphore(MAX_ACTIVE_REQUESTS)
_SESSION_LOCKS: dict[str, threading.Lock] = {}
_SESSION_LOCKS_GUARD = threading.Lock()
SERVER_STARTED_AT = datetime.now(UTC)


def _product_backend_timeout_sec() -> float:
    try:
        return max(1.0, float(os.getenv("PSU_PRODUCT_BACKEND_TIMEOUT_SEC", "9.0")))
    except ValueError:
        return 9.0


def _supervisor_worker_timeout_sec() -> float:
    """Reserve parent time for termination, replacement, and the HTTP reply.

    The product deadline covers the whole request, not only pipeline work.
    A worker therefore cannot consume the final response window.
    """
    try:
        reserve = max(0.5, float(os.getenv("PSU_SUPERVISOR_RESPONSE_RESERVE_SEC", "1.5")))
    except ValueError:
        reserve = 1.5
    return max(0.1, _product_backend_timeout_sec() - reserve)


def _runtime_status() -> dict[str, Any]:
    """Return non-sensitive runtime facts so local testers know which profile is live."""
    semantic_rag = semantic_retrieval_enabled()
    return {
        "profile": os.getenv("PSU_RUNTIME_PROFILE", "ad-hoc"),
        "version": os.getenv("PSU_RUNTIME_VERSION", "dev"),
        "started_at": SERVER_STARTED_AT.isoformat(),
        "answer_timeout_sec": _product_backend_timeout_sec(),
        "pipeline_timeout_sec": _env_float("PSU_PIPELINE_GLOBAL_TIMEOUT_SEC", 9.0, minimum=1.0),
        "intent_timeout_sec": _env_float("PSU_INTENT_LLM_TIMEOUT_SEC", 5.5, minimum=0.1),
        "local_llm": {
            "enabled": LOCAL_LLM_ASSIST_ENABLED,
            "model": os.getenv("PSU_CHATBOT_OLLAMA_MODEL", "scb10x/typhoon2.5-qwen3-4b"),
            "intent_timeout_sec": _env_float("PSU_INTENT_LLM_TIMEOUT_SEC", 5.5, minimum=0.1),
            "planner_timeout_sec": _env_float("PSU_QUERY_PLANNER_TIMEOUT_SEC", 1.2, minimum=0.1),
            "general_timeout_sec": _env_float("PSU_GENERAL_LLM_TIMEOUT_SEC", 4.0, minimum=0.1),
            "high_assist_profile": os.getenv("PSU_MODEL_FIRST_PREFLIGHT_CONFIDENCE", "0.90") == "0.99",
        },
        "semantic_rag": {
            "enabled": semantic_rag,
            "embedding_model": embedding_model_name(),
        },
        "english": {
            "enabled": bilingual_english_enabled(),
            "draft_preview": os.getenv("PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW", "0").strip().lower() in {"1", "true", "yes", "on"},
        },
        "input_quality": {
            "mode": os.getenv("PSU_INPUT_QUALITY_GUARD_MODE", "shadow"),
            "keyboard_layout": "request_retype",
            "repeated_characters": os.getenv("PSU_INPUT_QUALITY_REPEAT_POLICY", "ask_retype"),
        },
    }


def _session_lock(session_id: str) -> threading.Lock | None:
    if not session_id:
        return None
    with _SESSION_LOCKS_GUARD:
        return _SESSION_LOCKS.setdefault(session_id, threading.Lock())


def _write_chat_log_async(record: dict[str, Any]) -> None:
    def write() -> None:
        try:
            write_chat_log(record)
        except Exception as exc:  # pragma: no cover - logging must not break responses.
            print(f"Async chat log warning: {exc!r}", file=sys.stderr)

    # Keep the logger non-daemon so a normal server shutdown does not discard
    # the final completed exchange after the browser has already received it.
    threading.Thread(target=write, name="psu-chat-log", daemon=False).start()


def _json_default(value: Any) -> Any:
    if is_dataclass(value):
        return asdict(value)
    if isinstance(value, Path):
        return str(value)
    return str(value)


def _json_bytes(payload: dict[str, Any], status: int = 200) -> tuple[int, bytes]:
    return status, json.dumps(payload, ensure_ascii=False, default=_json_default).encode("utf-8")


def _source_list(hits: list[dict[str, Any]]) -> list[dict[str, str]]:
    sources: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for hit in hits or []:
        # Pipeline paths may return dictionaries or immutable Hit dataclasses.
        # Normalize both shapes so the answer text and the side-panel source
        # list never disagree merely because a worker crossed a process boundary.
        if is_dataclass(hit):
            item = asdict(hit)
        elif isinstance(hit, dict):
            item = hit
        else:
            item = {
                "id": getattr(hit, "id", ""),
                "metadata": getattr(hit, "metadata", {}),
                "source_url": getattr(hit, "source_url", ""),
            }
        metadata = item.get("metadata", {})
        if is_dataclass(metadata):
            metadata = asdict(metadata)
        elif not isinstance(metadata, dict):
            metadata = vars(metadata) if hasattr(metadata, "__dict__") else {}
        source_id = str(item.get("id") or metadata.get("title") or metadata.get("source_id") or "")
        url = str(
            metadata.get("source_url")
            or metadata.get("url")
            or item.get("source_url")
            or item.get("url")
            or ""
        )
        if not url:
            continue
        key = (source_id, url)
        if key in seen:
            continue
        seen.add(key)
        sources.append({"id": source_id, "url": url})
    return sources


def _trace_query_debug(result: Any, question: str, resolved_question: str) -> dict[str, Any]:
    traces: list[dict[str, Any]] = []
    for item in getattr(result, "trace", []) or []:
        stage = getattr(item, "stage", "")
        decision = getattr(item, "decision", "")
        if stage == "preprocess" or decision in {"selected_query_variant", "kept_original_query"}:
            traces.append({
                "stage": stage,
                "decision": decision,
                "confidence": getattr(item, "confidence", 0.0),
                "detail": getattr(item, "detail", ""),
                "metadata": getattr(item, "metadata", {}),
            })

    selected_trace = next((item for item in traces if item["decision"] == "selected_query_variant"), None)
    normalized_trace = next((item for item in traces if item["decision"] == "normalized"), None)
    query_variants = []
    if normalized_trace:
        query_variants = list((normalized_trace.get("metadata") or {}).get("query_variants") or [])

    return {
        "original_question": question,
        "resolved_question": resolved_question,
        "normalized_query": normalized_trace["detail"] if normalized_trace else "",
        "query_variants": query_variants,
        "active_query": selected_trace["detail"] if selected_trace else resolved_question,
        "active_query_changed": selected_trace is not None,
        "trace": traces,
    }


def _input_guard_response(
    *,
    request_id: str,
    decision: InputQualityDecision,
    started: float,
    locale: LocaleDecision,
) -> dict[str, Any]:
    if locale.effective == "en":
        if "keyboard_layout_mismatch" in decision.flags:
            message = "The keyboard layout may not match the language you intended. Please check the keyboard language and type the question again."
        else:
            message = "This message may contain unintentionally repeated characters. Please check it and type the question again."
    else:
        message = decision.message
    return {
        "ok": True,
        "request_id": request_id,
        "answer": message,
        "mode": decision.mode,
        "route_category": "input_guard",
        "route_intent": decision.flags[0] if decision.flags else "input_quality",
        "confidence": max(decision.features.layout_score, decision.features.repeat_score),
        "latency_sec": round(decision.elapsed_ms / 1000, 4),
        "wall_sec": round(time.perf_counter() - started, 4),
        "deadline": deadline_metadata(),
        "timing_status": "input_guard",
        "timed_out": False,
        "timeout_stage": "",
        "retryable": False,
        "sources": [],
        "validation_ok": True,
        "input_quality": _localized_input_quality_public(decision, locale.effective),
        "language": locale.to_dict(),
    }


def _localized_input_quality_public(decision: InputQualityDecision, locale: str) -> dict[str, object]:
    payload = decision.to_public_dict()
    if locale != "en" or "notice" not in payload:
        return payload
    if "keyboard_layout_mismatch" in decision.flags:
        payload["notice"] = (
            "The keyboard layout may not match the language you intended. "
            "Please check the keyboard language and type the question again."
        )
    elif "repeated_character_typo" in decision.flags:
        payload["notice"] = (
            "This message may contain unintentionally repeated characters. "
            "Please check it before continuing."
        )
    return payload


def _supervisor_timeout_response(*, request_id: str, started: float, worker_id: int, locale: LocaleDecision) -> dict[str, Any]:
    answer = (
        "This request reached the processing time limit, so it was stopped to keep the service responsive.\n"
        "Please try a more specific question, such as naming the zone, game, or topic directly."
        if locale.effective == "en"
        else (
            "ขออภัยครับ คำถามนี้ใช้เวลาประมวลผลเกินเวลาที่กำหนด เลยหยุดไว้ก่อนเพื่อไม่ให้ระบบค้าง\n"
            "ลองถามใหม่ให้เฉพาะเจาะจงขึ้น เช่น ระบุโซน เกม หรือเรื่องที่ต้องการถามโดยตรงครับ"
        )
    )
    return {
        "ok": True,
        "request_id": request_id,
        "answer": answer,
        "mode": "pipeline:request_timeout_no_answer",
        "route_category": "no_answer",
        "route_intent": "request_timeout",
        "confidence": 0.45,
        "latency_sec": round(time.perf_counter() - started, 4),
        "wall_sec": round(time.perf_counter() - started, 4),
        "deadline": deadline_metadata(),
        "timing_status": "controlled_timeout",
        "timed_out": True,
        "timeout_stage": "pipeline_worker_supervision",
        "retryable": False,
        "worker_id": worker_id,
        "sources": [],
        "validation_ok": True,
        "language": locale.to_dict(),
    }


class ChatHandler(BaseHTTPRequestHandler):
    server_version = "PSUEsportsChat/0.1"

    def log_message(self, fmt: str, *args: Any) -> None:
        sys.stderr.write("[%s] %s\n" % (self.log_date_time_string(), fmt % args))

    def _send_bytes(self, status: int, body: bytes, content_type: str, *, content_language: str | None = None) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "content-type")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        if content_language in {"th", "en"}:
            self.send_header("Content-Language", content_language)
        self.end_headers()
        self.wfile.write(body)

    def _send_json(self, payload: dict[str, Any], status: int = 200, *, content_language: str | None = None) -> None:
        code, body = _json_bytes(payload, status)
        self._send_bytes(code, body, "application/json; charset=utf-8", content_language=content_language)

    def do_OPTIONS(self) -> None:
        self._send_bytes(204, b"", "text/plain; charset=utf-8")

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        path = unquote(parsed.path)
        if path == "/health":
            self._send_json({
                "ok": True,
                "service": "psu-esports-chat-web",
                "time": datetime.now(UTC).isoformat(),
                "warmup": STARTUP_WARMUP,
                "llm_preflight": STARTUP_LLM_PREFLIGHT,
                "input_quality_guard": STARTUP_INPUT_QUALITY_GUARD,
                "llm_health": llm_health_snapshot(),
                "pipeline_workers": PIPELINE_SUPERVISOR.health() if PIPELINE_SUPERVISOR else {"enabled": False},
                "runtime": _runtime_status(),
                "features": {
                    "bilingual_english": bilingual_english_enabled(),
                    "local_llm_assist": LOCAL_LLM_ASSIST_ENABLED,
                    "semantic_rag": semantic_retrieval_enabled(),
                    "embedding_model": embedding_model_name(),
                },
            })
            return
        if path == "/api/calendar":
            self._send_json({"ok": True, "calendar": calendar_context()})
            return
        if path == "/api/session-history":
            session_id = str((parse_qs(parsed.query).get("session_id") or [""])[0]).strip()
            if not is_valid_session_id(session_id):
                self._send_json({"ok": False, "error": "invalid_session_id"}, 400)
                return
            try:
                history = read_sqlite_session_history(session_id)
            except ValueError:
                self._send_json({"ok": False, "error": "invalid_session_id"}, 400)
                return
            self._send_json({
                "ok": True,
                "session_id": session_id,
                "messages": history,
                "storage": "local_sqlite",
            })
            return
        self._serve_static(path)

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path not in {"/api/chat", "/api/intent-feedback"}:
            self._send_json({"ok": False, "error": "not_found"}, 404)
            return

        content_length = int(self.headers.get("Content-Length", "0") or "0")
        if content_length <= 0 or content_length > MAX_BODY_BYTES:
            self._send_json({"ok": False, "error": "invalid_body_size"}, 413)
            return

        try:
            raw_body = self.rfile.read(content_length)
            payload = json.loads(raw_body.decode("utf-8"))
        except Exception:
            self._send_json({"ok": False, "error": "invalid_json"}, 400)
            return

        if parsed.path == "/api/intent-feedback":
            try:
                self._send_json(write_intent_feedback(payload))
            except ValueError as exc:
                self._send_json({"ok": False, "error": "invalid_feedback", "detail": str(exc)}, 400)
            return

        question = str(payload.get("question") or "").strip()
        client_session_id = str(payload.get("client_session_id") or "").strip()
        if not is_valid_session_id(client_session_id):
            client_session_id = f"session-{uuid.uuid4()}"
        recent_history = payload.get("recent_history") or []
        requested_locale = normalize_requested_locale(payload.get("locale"))
        debug = bool(payload.get("debug", False))
        experimental_rag_fallback = bool(payload.get("experimental_rag_fallback", False))
        # Local-model assistance is a server policy. It must not depend on
        # whether the browser happens to be served from localhost.
        experimental_allow_llm = LOCAL_LLM_ASSIST_ENABLED

        if not question:
            self._send_json({"ok": False, "error": "question_required"}, 400)
            return
        if len(question) > MAX_QUESTION_CHARS:
            self._send_json({"ok": False, "error": "question_too_long", "max_chars": MAX_QUESTION_CHARS}, 413)
            return

        started = time.perf_counter()
        request_id = uuid.uuid4().hex
        exchange_id = uuid.uuid4().hex
        with request_deadline(_product_backend_timeout_sec()):
            input_quality = INPUT_QUALITY_GUARD.inspect(question) if INPUT_QUALITY_GUARD else None
            input_recovery = inspect_surface_input(question)
            layout_direction = input_quality.features.layout_direction if input_quality else None
            locale_decision = resolve_locale(
                question,
                requested=requested_locale,
                recent_history=recent_history,
                keyboard_layout_direction=layout_direction,
                surface_language=input_recovery.language if input_recovery.should_review_intent else None,
            )
            if not _ACTIVE_REQUESTS.acquire(blocking=False):
                self._send_json({
                    "ok": False,
                    "error": "server_busy",
                    "request_id": request_id,
                    "retry_after_ms": 250,
                    "message": "The server is busy. Please try again shortly." if locale_decision.effective == "en" else "ขณะนี้มีผู้ใช้งานพร้อมกันจำนวนมาก กรุณาลองใหม่อีกครั้งในอีกสักครู่ครับ",
                    "language": locale_decision.to_dict(),
                }, 503, content_language=locale_decision.effective)
                return

            session_lock = _session_lock(client_session_id)
            session_acquired = session_lock is None or session_lock.acquire(timeout=SESSION_LOCK_WAIT_SEC)
            if not session_acquired:
                _ACTIVE_REQUESTS.release()
                self._send_json({
                    "ok": False,
                    "error": "session_busy",
                    "request_id": request_id,
                    "retry_after_ms": 150,
                    "message": "A previous message in this conversation is still processing." if locale_decision.effective == "en" else "ข้อความก่อนหน้าในบทสนทนานี้กำลังประมวลผลอยู่ครับ",
                    "language": locale_decision.to_dict(),
                }, 409, content_language=locale_decision.effective)
                return

            try:
                if input_quality and input_quality.should_short_circuit:
                    response = _input_guard_response(
                        request_id=request_id,
                        decision=input_quality,
                        started=started,
                        locale=locale_decision,
                    )
                    _write_chat_log_async({
                        "event_type": "chat_exchange",
                        "exchange_id": exchange_id,
                        "channel": "web",
                        "request_id": request_id,
                        "client_session_id": client_session_id,
                        "question": question,
                        "input_quality": input_quality.to_log_dict(),
                        "answer": response["answer"],
                        "mode": response["mode"],
                        "route_category": response["route_category"],
                        "route_intent": response["route_intent"],
                        "confidence": response["confidence"],
                        "latency_sec": response["latency_sec"],
                        "wall_sec": response["wall_sec"],
                        "deadline": response["deadline"],
                        "sources": [],
                        "validation_ok": True,
                        "language": locale_decision.to_dict(),
                    })
                    self._send_json(response, content_language=locale_decision.effective)
                    return

                resolved = resolve_question_with_context(question, recent_history, locale=locale_decision.effective)
                worker_id = -1
                if PIPELINE_SUPERVISOR is not None:
                    supervised = PIPELINE_SUPERVISOR.answer(
                        resolved.resolved_question,
                        timeout_sec=_supervisor_worker_timeout_sec(),
                        experimental_rag_fallback=experimental_rag_fallback,
                        experimental_allow_llm=experimental_allow_llm,
                        request_id=request_id,
                        locale=requested_locale,
                        locale_decision=locale_decision.to_dict(),
                    )
                    worker_id = supervised.worker_id
                    if supervised.status == "timeout":
                        timeout_response = _supervisor_timeout_response(
                            request_id=request_id,
                            started=started,
                            worker_id=worker_id,
                            locale=locale_decision,
                        )
                        _write_chat_log_async({
                            "event_type": "chat_exchange",
                            "exchange_id": exchange_id,
                            "channel": "web",
                            "request_id": request_id,
                            "client_session_id": client_session_id,
                            "question": question,
                            "answer": timeout_response["answer"],
                            "mode": timeout_response["mode"],
                            "route_category": timeout_response["route_category"],
                            "route_intent": timeout_response["route_intent"],
                            "confidence": timeout_response["confidence"],
                            "latency_sec": timeout_response["latency_sec"],
                            "wall_sec": timeout_response["wall_sec"],
                            "timing_status": timeout_response["timing_status"],
                            "timed_out": True,
                            "timeout_stage": timeout_response["timeout_stage"],
                            "worker_id": worker_id,
                            "sources": [],
                            "validation_ok": True,
                            "language": locale_decision.to_dict(),
                        })
                        self._send_json(timeout_response, content_language=locale_decision.effective)
                        return
                    if supervised.status == "busy":
                        self._send_json({
                            "ok": False,
                            "request_id": request_id,
                            "error": "server_busy",
                            "retry_after_ms": 250,
                            "retryable": True,
                            "timing_status": "worker_queue_busy",
                            "timed_out": False,
                            "timeout_stage": "",
                            "message": "The server is handling other requests. Please try again shortly." if locale_decision.effective == "en" else "ขณะนี้ระบบกำลังตอบคำถามอื่นอยู่ กรุณาลองใหม่อีกสักครู่ครับ",
                            "language": locale_decision.to_dict(),
                        }, 503, content_language=locale_decision.effective)
                        return
                    if supervised.status != "ok" or supervised.result is None:
                        self._send_json({
                            "ok": False,
                            "request_id": request_id,
                            "error": "pipeline_worker_restarting",
                            "detail": supervised.error,
                            "diagnostics": supervised.diagnostics or {},
                            "retryable": True,
                            "timing_status": "worker_restarting",
                            "timed_out": False,
                            "timeout_stage": "",
                            "message": "The answer worker is restarting. Please retry this question." if locale_decision.effective == "en" else "ระบบตอบคำถามกำลังเริ่มทำงานใหม่ กรุณาลองส่งคำถามนี้อีกครั้งครับ",
                            "language": locale_decision.to_dict(),
                        }, 503, content_language=locale_decision.effective)
                        return
                    result = supervised.result
                else:
                    result = answer_question_pipeline_debug(
                        resolved.resolved_question,
                        experimental_rag_fallback=experimental_rag_fallback,
                        experimental_allow_llm=experimental_allow_llm,
                        locale=requested_locale,
                        locale_decision=locale_decision,
                        recent_history=recent_history,
                        keyboard_layout_direction=layout_direction,
                    )
                sources = _source_list(result.hits)
                query_debug = _trace_query_debug(result, question, resolved.resolved_question)
                calendar = calendar_context()
                response: dict[str, Any] = {
                    "ok": True,
                    "request_id": request_id,
                    "session_id": client_session_id,
                    "answer": result.answer,
                    "mode": result.mode,
                    "route_category": result.route.category,
                    "route_intent": result.route.intent,
                    "universal_intent": result.universal_intent,
                    "confidence": result.confidence,
                    "latency_sec": result.elapsed,
                    "wall_sec": round(time.perf_counter() - started, 4),
                    "deadline": deadline_metadata(),
                    "timing_status": (
                        "controlled_timeout"
                        if result.mode == "pipeline:request_timeout_no_answer"
                        else "completed"
                    ),
                    "timed_out": result.mode == "pipeline:request_timeout_no_answer",
                    "timeout_stage": next(
                        (
                            str(item.detail)
                            for item in reversed(getattr(result, "trace", []) or [])
                            if getattr(item, "decision", "") == "request_timeout_no_answer"
                        ),
                        "",
                    ),
                    "retryable": False,
                    "worker_id": worker_id,
                    "sources": sources,
                    "validation_ok": result.validation.ok,
                    "language": (result.language or locale_decision).to_dict(),
                    "experimental_rag_fallback": experimental_rag_fallback,
                    "experimental_allow_llm": experimental_allow_llm,
                    "input_recovery": input_recovery.as_dict(),
                    "server_date": {
                        "iso": calendar["date"],
                        "label": calendar["label"],
                        "time": calendar["time"],
                        "datetime_iso": calendar["datetime_iso"],
                        "timezone": calendar["timezone"],
                        "service_slot": calendar["service_slot"],
                        "thai_holidays": calendar["thai_holidays"],
                        "upcoming_thai_holidays": calendar["upcoming_thai_holidays"],
                    },
                    "calendar": calendar,
                }
                if input_quality:
                    response["input_quality"] = _localized_input_quality_public(
                        input_quality,
                        (result.language or locale_decision).effective,
                    )
                if debug:
                    response["context_resolution"] = resolved.to_dict()
                    response["query_debug"] = query_debug
                    response["decision_artifact"] = result.decision_artifact
                    response["entities"] = result.entities
                    response["validation"] = result.validation
                    response["trace"] = result.trace

                log_record = {
                    "event_type": "chat_exchange",
                    "exchange_id": exchange_id,
                    "channel": "web",
                    "request_id": request_id,
                    "client_session_id": client_session_id,
                    "question": question,
                    "resolved_question": resolved.resolved_question,
                    "context_resolution": resolved.to_dict(),
                    "query_debug": query_debug,
                    "recent_history_count": len(recent_history) if isinstance(recent_history, list) else 0,
                    "experimental": {
                        "rag_fallback": experimental_rag_fallback,
                        "allow_llm": experimental_allow_llm,
                    },
                    "answer": result.answer,
                    "mode": result.mode,
                    "route_category": result.route.category,
                    "route_intent": result.route.intent,
                    "universal_intent": result.universal_intent,
                    "decision_artifact": result.decision_artifact,
                    "confidence": result.confidence,
                    "latency_sec": result.elapsed,
                    "wall_sec": round(time.perf_counter() - started, 4),
                    "deadline": deadline_metadata(),
                    "timing_status": response["timing_status"],
                    "timed_out": response["timed_out"],
                    "timeout_stage": response["timeout_stage"],
                    "retryable": False,
                    "worker_id": worker_id,
                    "sources": sources,
                    "validation_ok": result.validation.ok,
                    "language": (result.language or locale_decision).to_dict(),
                    "input_recovery": input_recovery.as_dict(),
                }
                if input_quality:
                    log_record["input_quality"] = input_quality.to_log_dict()
                if debug:
                    response["log_sinks"] = {"status": "queued"}
                self._send_json(response, content_language=(result.language or locale_decision).effective)
                _write_chat_log_async(log_record)
            except Exception as exc:
                _write_chat_log_async({
                    "event_type": "chat_exchange_error",
                    "exchange_id": exchange_id,
                    "channel": "web",
                    "request_id": request_id,
                    "client_session_id": client_session_id,
                    "question": question,
                    "resolved_question": resolved.resolved_question if "resolved" in locals() else question,
                    "error": repr(exc),
                    "wall_sec": round(time.perf_counter() - started, 4),
                })
                self._send_json({
                    "ok": False,
                    "request_id": request_id,
                    "error": "server_error",
                    "detail": repr(exc),
                    "message": "The server could not complete this request." if locale_decision.effective == "en" else "ระบบไม่สามารถประมวลผลคำขอนี้ได้ครับ",
                    "language": locale_decision.to_dict(),
                }, 500, content_language=locale_decision.effective)
            finally:
                if session_lock is not None and session_acquired:
                    session_lock.release()
                _ACTIVE_REQUESTS.release()

    def _serve_static(self, path: str) -> None:
        if path in {"", "/", "/chat"}:
            target = WEB_ROOT / "index.html"
        else:
            relative = path.lstrip("/")
            target = (WEB_ROOT / relative).resolve()
            try:
                target.relative_to(WEB_ROOT.resolve())
            except ValueError:
                self._send_json({"ok": False, "error": "invalid_static_path"}, 400)
                return

        if not target.exists() or not target.is_file():
            self._send_json({"ok": False, "error": "static_not_found"}, 404)
            return

        content_type = mimetypes.guess_type(str(target))[0] or "application/octet-stream"
        if target.suffix.lower() in {".html", ".css", ".js"}:
            content_type += "; charset=utf-8"
        self._send_bytes(200, target.read_bytes(), content_type)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the PSU Esports chatbot web/API MVP.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8018)
    args = parser.parse_args()

    if not WEB_ROOT.exists():
        raise SystemExit(f"Web folder not found: {WEB_ROOT}")

    global STARTUP_INPUT_QUALITY_GUARD
    global INPUT_QUALITY_GUARD
    if keyboard_guard_enabled():
        try:
            INPUT_QUALITY_GUARD = RuntimeInputQualityGuard.from_environment()
            STARTUP_INPUT_QUALITY_GUARD = INPUT_QUALITY_GUARD.startup_status()
            print(
                "Input-quality guard ready "
                f"({STARTUP_INPUT_QUALITY_GUARD['mode']}, corpus={STARTUP_INPUT_QUALITY_GUARD['corpus_size']})."
            )
        except Exception as exc:  # pragma: no cover - guard must not prevent the web server from starting.
            INPUT_QUALITY_GUARD = None
            STARTUP_INPUT_QUALITY_GUARD = {"enabled": False, "error": repr(exc)}
            print(f"Input-quality guard warning: {exc!r}", file=sys.stderr)
    else:
        STARTUP_INPUT_QUALITY_GUARD = {"enabled": False, "reason": "disabled_by_environment"}
        print("Input-quality guard disabled by PSU_INPUT_QUALITY_GUARD_ENABLED.")

    global PIPELINE_SUPERVISOR
    if worker_supervisor_enabled():
        PIPELINE_SUPERVISOR = PipelineWorkerSupervisor()
        PIPELINE_SUPERVISOR.start()
        print("Pipeline worker supervisor ready.")
    else:
        print("Pipeline worker supervisor disabled by PSU_PIPELINE_WORKER_SUPERVISOR.")

    global STARTUP_WARMUP
    if pipeline_warmup_enabled():
        print("Warming PSU Esports chatbot caches...")
        STARTUP_WARMUP = warm_pipeline_caches()
        status = "ok" if STARTUP_WARMUP.ok else "partial"
        print(f"Warmup {status} in {STARTUP_WARMUP.elapsed_sec:.4f}s: {', '.join(STARTUP_WARMUP.warmed)}")
        if STARTUP_WARMUP.errors:
            for error in STARTUP_WARMUP.errors:
                print(f"Warmup warning: {error}", file=sys.stderr)
    else:
        print("Pipeline warmup disabled by PSU_PIPELINE_WARMUP.")

    global STARTUP_LLM_PREFLIGHT
    if llm_preflight_enabled():
        model = os.getenv("PSU_CHATBOT_OLLAMA_MODEL", "scb10x/typhoon2.5-qwen3-4b")
        print("Checking Local LLM health...")
        STARTUP_LLM_PREFLIGHT = preflight_ollama(
            model=model,
            kind="preflight",
            timeout_sec=float(os.getenv("PSU_LLM_PREFLIGHT_TIMEOUT_SEC", "90")),
            num_predict=int(os.getenv("PSU_LLM_PREFLIGHT_NUM_PREDICT", "1")),
            num_ctx=int(os.getenv("PSU_LLM_PREFLIGHT_NUM_CTX", os.getenv("PSU_GENERAL_LLM_NUM_CTX", "3072"))),
        )
        status = "ok" if STARTUP_LLM_PREFLIGHT.get("ok") else "unhealthy"
        print(f"LLM preflight {status} in {float(STARTUP_LLM_PREFLIGHT.get('elapsed_ms', 0.0)) / 1000:.3f}s")
        if not STARTUP_LLM_PREFLIGHT.get("ok"):
            print(
                f"LLM warning: {STARTUP_LLM_PREFLIGHT.get('error_type')}: {STARTUP_LLM_PREFLIGHT.get('error')}",
                file=sys.stderr,
            )
    else:
        print("LLM preflight disabled by PSU_LLM_PREFLIGHT.")

    server = ThreadingHTTPServer((args.host, args.port), ChatHandler)
    print(f"PSU Esports Chat Web is running at http://{args.host}:{args.port}/")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
    finally:
        if PIPELINE_SUPERVISOR is not None:
            PIPELINE_SUPERVISOR.shutdown()
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
