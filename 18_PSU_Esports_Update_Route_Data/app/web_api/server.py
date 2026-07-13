from __future__ import annotations

import argparse
import json
import mimetypes
import sys
import time
from dataclasses import asdict, is_dataclass
from datetime import UTC, datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse

from app.calendar.service_calendar import calendar_context
from app.runtime.pipeline_answer import answer_question_pipeline_debug
from app.session.context_resolver import resolve_question_with_context
from app.session.chat_logger import write_chat_log


PROJECT_ROOT = Path(__file__).resolve().parents[2]
WEB_ROOT = PROJECT_ROOT / "web_chat"
LOG_DIR = PROJECT_ROOT / "data" / "logs"
MAX_BODY_BYTES = 128 * 1024


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


class ChatHandler(BaseHTTPRequestHandler):
    server_version = "PSUEsportsChat/0.1"

    def log_message(self, fmt: str, *args: Any) -> None:
        sys.stderr.write("[%s] %s\n" % (self.log_date_time_string(), fmt % args))

    def _send_bytes(self, status: int, body: bytes, content_type: str) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "content-type")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.end_headers()
        self.wfile.write(body)

    def _send_json(self, payload: dict[str, Any], status: int = 200) -> None:
        code, body = _json_bytes(payload, status)
        self._send_bytes(code, body, "application/json; charset=utf-8")

    def do_OPTIONS(self) -> None:
        self._send_bytes(204, b"", "text/plain; charset=utf-8")

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        path = unquote(parsed.path)
        if path == "/health":
            self._send_json({"ok": True, "service": "psu-esports-chat-web", "time": datetime.now(UTC).isoformat()})
            return
        if path == "/api/calendar":
            self._send_json({"ok": True, "calendar": calendar_context()})
            return
        self._serve_static(path)

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path != "/api/chat":
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

        question = str(payload.get("question") or "").strip()
        client_session_id = str(payload.get("client_session_id") or "").strip()
        recent_history = payload.get("recent_history") or []
        debug = bool(payload.get("debug", False))
        experimental_rag_fallback = bool(payload.get("experimental_rag_fallback", False))
        experimental_allow_llm = bool(payload.get("experimental_allow_llm", False))

        if not question:
            self._send_json({"ok": False, "error": "question_required"}, 400)
            return

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
                response["context_resolution"] = resolved.to_dict()
                response["query_debug"] = query_debug
                response["entities"] = result.entities
                response["validation"] = result.validation
                response["trace"] = result.trace

            log_sinks = write_chat_log({
                "channel": "web",
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
            self._send_json(response)
        except Exception as exc:
            write_chat_log({
                "channel": "web",
                "client_session_id": client_session_id,
                "question": question,
                "resolved_question": resolved.resolved_question if "resolved" in locals() else question,
                "error": repr(exc),
                "wall_sec": round(time.perf_counter() - started, 4),
            })
            self._send_json({"ok": False, "error": "server_error", "detail": repr(exc)}, 500)

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

    server = ThreadingHTTPServer((args.host, args.port), ChatHandler)
    print(f"PSU Esports Chat Web is running at http://{args.host}:{args.port}/")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
