from __future__ import annotations

import sys
import time
from dataclasses import asdict, is_dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from flask import Flask, jsonify, request

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.calendar.service_calendar import calendar_context  # noqa: E402
from app.runtime.pipeline_answer import answer_question_pipeline_debug  # noqa: E402
from app.session.context_resolver import resolve_question_with_context  # noqa: E402
from app.session.chat_logger import write_chat_log  # noqa: E402


app = Flask(__name__)
MAX_BODY_BYTES = 128 * 1024


def _plain(value: Any) -> Any:
    if is_dataclass(value):
        return asdict(value)
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(key): _plain(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_plain(item) for item in value]
    return value


def _source_list(hits: list[dict[str, Any]]) -> list[dict[str, str]]:
    sources: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for hit in hits or []:
        metadata = hit.get("metadata", {}) if isinstance(hit, dict) else {}
        source_id = str(hit.get("id") or metadata.get("title") or metadata.get("source_id") or "")
        url = str(metadata.get("source_url") or metadata.get("url") or "")
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


@app.after_request
def add_common_headers(response):
    response.headers["Cache-Control"] = "no-store"
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "content-type"
    response.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    return response


@app.route("/", methods=["POST", "OPTIONS"])
@app.route("/api/chat", methods=["POST", "OPTIONS"])
def chat():
    if request.method == "OPTIONS":
        return ("", 204)

    if request.content_length and request.content_length > MAX_BODY_BYTES:
        return jsonify({"ok": False, "error": "invalid_body_size"}), 413

    payload = request.get_json(silent=True) or {}
    question = str(payload.get("question") or "").strip()
    client_session_id = str(payload.get("client_session_id") or payload.get("session_id") or "").strip()
    recent_history = payload.get("recent_history") or []
    debug = bool(payload.get("debug", False))
    experimental_rag_fallback = bool(payload.get("experimental_rag_fallback", False))
    experimental_allow_llm = bool(payload.get("experimental_allow_llm", False))

    if not question:
        return jsonify({"ok": False, "error": "question_required"}), 400

    started = time.perf_counter()
    try:
        resolved = resolve_question_with_context(question, recent_history)
        result = answer_question_pipeline_debug(
            resolved.resolved_question,
            experimental_rag_fallback=experimental_rag_fallback,
            experimental_allow_llm=experimental_allow_llm,
        )
        sources = _source_list(result.hits)
        query_debug = _trace_query_debug(result, question, resolved.resolved_question)
        calendar = calendar_context()
        response: dict[str, Any] = {
            "ok": True,
            "answer": result.answer,
            "mode": result.mode,
            "route_category": result.route.category,
            "route_intent": result.route.intent,
            "confidence": result.confidence,
            "latency_sec": result.elapsed,
            "sources": sources,
            "validation_ok": result.validation.ok,
            "experimental_rag_fallback": experimental_rag_fallback,
            "experimental_allow_llm": experimental_allow_llm,
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
        if debug:
            response["recent_history_count"] = len(recent_history) if isinstance(recent_history, list) else 0
            response["context_resolution"] = resolved.to_dict()
            response["query_debug"] = query_debug
            response["experimental"] = {
                "rag_fallback": experimental_rag_fallback,
                "allow_llm": experimental_allow_llm,
            }
            response["entities"] = _plain(result.entities)
            response["validation"] = _plain(result.validation)
            response["trace"] = _plain(result.trace)
        log_sinks = write_chat_log({
            "channel": "vercel",
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
            "confidence": result.confidence,
            "latency_sec": result.elapsed,
            "wall_sec": round(time.perf_counter() - started, 4),
            "sources": sources,
            "validation_ok": result.validation.ok,
        })
        if debug:
            response["log_sinks"] = log_sinks
        return jsonify(response)
    except Exception as exc:
        write_chat_log({
            "channel": "vercel",
            "client_session_id": client_session_id,
            "question": question,
            "resolved_question": resolved.resolved_question if "resolved" in locals() else question,
            "error": repr(exc),
            "wall_sec": round(time.perf_counter() - started, 4),
        })
        return jsonify({
            "ok": False,
            "error": "server_error",
            "detail": repr(exc),
            "time": datetime.now(UTC).isoformat(),
        }), 500
