from __future__ import annotations

"""Privacy-preserving performance events shared by pipeline workers and parent API.

Events intentionally omit raw questions, answers, prompts, retrieved document
bodies, booking information, and chat/session content.  The parent process is
the only JSONL writer so a child crash still leaves the last reported stage.
"""

import json
import os
import queue
import threading
import time
import uuid
from contextlib import contextmanager
from contextvars import ContextVar, Token
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Iterator

from app.pipeline.request_deadline import deadline_metadata


ROOT = Path(__file__).resolve().parents[2]
PERFORMANCE_LOG_DIR = ROOT / "data" / "logs" / "performance"
_EVENT_QUEUE: ContextVar[Any | None] = ContextVar("psu_performance_event_queue", default=None)
_EVENT_CONTEXT: ContextVar[dict[str, str] | None] = ContextVar("psu_performance_event_context", default=None)
_SEQUENCE: ContextVar[int] = ContextVar("psu_performance_event_sequence", default=0)

_SENSITIVE_KEYS = frozenset({
    "answer", "question", "query", "prompt", "raw_query", "resolved_question",
    "original_question", "text", "body", "message", "content", "evidence",
    "client_session_id", "email", "phone", "student_id", "slip", "parts",
    "candidates", "aliases", "targets", "documents",
})

# Trace metadata is assembled by many pipeline components.  String values are
# therefore opt-in: this prevents a later component from accidentally adding
# an input fragment, document title, or a booking field to performance logs.
_SAFE_STRING_ATTRIBUTE_KEYS = frozenset({
    "backend", "catalog_version", "decision_reason", "error_type", "fallback",
    "language_hint", "llm_health_status", "llm_kind", "llm_model", "method",
    "mode", "operation", "route_category", "route_intent", "runtime_route",
    "stage_kind", "status", "target_status", "timing_status",
})


def _truthy(value: str | None, *, default: bool = True) -> bool:
    if value is None or value == "":
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


def performance_trace_enabled() -> bool:
    return _truthy(os.getenv("PSU_PERFORMANCE_TRACE"), default=True)


def _safe_attributes(metadata: dict[str, Any] | None) -> dict[str, str | int | float | bool | None]:
    safe: dict[str, str | int | float | bool | None] = {}
    for key, value in (metadata or {}).items():
        normalized = str(key).lower()
        if normalized in _SENSITIVE_KEYS or any(token in normalized for token in ("prompt", "answer", "query", "content", "evidence", "session")):
            continue
        if isinstance(value, str):
            if normalized in _SAFE_STRING_ATTRIBUTE_KEYS:
                safe[str(key)] = value[:96]
        elif isinstance(value, (int, float, bool)) or value is None:
            safe[str(key)] = value
    return safe


def emit_performance_event(
    event: str,
    stage: str,
    *,
    status: str = "ok",
    attributes: dict[str, Any] | None = None,
    counters: dict[str, int | float] | None = None,
) -> None:
    if not performance_trace_enabled():
        return
    event_queue = _EVENT_QUEUE.get()
    context = _EVENT_CONTEXT.get()
    if event_queue is None or context is None:
        return
    sequence = _SEQUENCE.get() + 1
    _SEQUENCE.set(sequence)
    deadline = deadline_metadata()
    payload = {
        "schema_version": "performance_event_v1",
        "run_id": context["run_id"],
        "trace_id": context["trace_id"],
        "request_id": context["request_id"],
        "worker_id": context["worker_id"],
        "sequence": sequence,
        "event": str(event),
        "stage": str(stage),
        "status": str(status),
        "wall_time_utc": datetime.now(UTC).isoformat(),
        "monotonic_ns": time.perf_counter_ns(),
        "elapsed_ms": round(float(deadline.get("global_elapsed_sec") or 0.0) * 1000, 3),
        "remaining_ms": round(float(deadline.get("global_remaining_sec") or 0.0) * 1000, 3),
        "attributes": _safe_attributes(attributes),
        "counters": dict(counters or {}),
    }
    try:
        # Progress can be dropped under pressure. Terminal stage events receive
        # a tiny bounded wait so a worker cannot overrun the request deadline.
        event_queue.put(payload, block=event != "stage_progress", timeout=0.01 if event != "stage_progress" else 0.0)
    except (queue.Full, OSError, ValueError):
        pass


@contextmanager
def performance_event_context(
    event_queue: Any,
    *,
    run_id: str,
    request_id: str,
    worker_id: int | str,
) -> Iterator[None]:
    context = {
        "run_id": str(run_id),
        "trace_id": uuid.uuid4().hex,
        "request_id": str(request_id),
        "worker_id": str(worker_id),
    }
    queue_token: Token[Any | None] = _EVENT_QUEUE.set(event_queue)
    context_token: Token[dict[str, str] | None] = _EVENT_CONTEXT.set(context)
    sequence_token: Token[int] = _SEQUENCE.set(0)
    try:
        emit_performance_event("request_started", "pipeline", status="started")
        yield
    finally:
        _SEQUENCE.reset(sequence_token)
        _EVENT_CONTEXT.reset(context_token)
        _EVENT_QUEUE.reset(queue_token)


def emit_trace_finished(trace: Any) -> None:
    """Send a sanitized PipelineTrace event from the worker while it is alive."""
    metadata = getattr(trace, "metadata", {})
    emit_performance_event(
        "stage_finished",
        str(getattr(trace, "stage", "unknown")),
        status=str(getattr(trace, "decision", "ok")),
        attributes={
            "confidence": getattr(trace, "confidence", 0.0),
            **(metadata if isinstance(metadata, dict) else {}),
        },
    )


class ObservedTraceList(list[Any]):
    """List-compatible trace collector that mirrors completed stages to IPC."""

    def append(self, item: Any) -> None:
        super().append(item)
        emit_trace_finished(item)

    def extend(self, values: Any) -> None:
        for item in values:
            self.append(item)


class ParentPerformanceLogger:
    def __init__(self, event_queue: Any, *, run_id: str | None = None, path: Path | None = None) -> None:
        self.event_queue = event_queue
        self.run_id = run_id or datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
        self.path = path or PERFORMANCE_LOG_DIR / f"pipeline_{self.run_id}.jsonl"
        self._stop = threading.Event()
        self._thread: threading.Thread | None = None
        self._count = 0
        self._dropped = 0
        self._lock = threading.Lock()

    def start(self) -> None:
        if self._thread is not None:
            return
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._thread = threading.Thread(target=self._run, name="psu-performance-logger", daemon=True)
        self._thread.start()

    def stop(self) -> None:
        self._stop.set()
        if self._thread is not None:
            self._thread.join(timeout=1.5)

    def emit_parent(self, event: str, stage: str, *, request_id: str, worker_id: int | str, status: str, attributes: dict[str, Any] | None = None) -> None:
        payload = {
            "schema_version": "performance_event_v1",
            "run_id": self.run_id,
            "trace_id": "parent",
            "request_id": str(request_id),
            "worker_id": str(worker_id),
            "sequence": 0,
            "event": event,
            "stage": stage,
            "status": status,
            "wall_time_utc": datetime.now(UTC).isoformat(),
            "monotonic_ns": time.perf_counter_ns(),
            "elapsed_ms": 0.0,
            "remaining_ms": 0.0,
            "attributes": _safe_attributes(attributes),
            "counters": {},
        }
        try:
            self.event_queue.put(payload, block=False)
        except (queue.Full, OSError, ValueError):
            with self._lock:
                self._dropped += 1

    def snapshot(self) -> dict[str, Any]:
        with self._lock:
            return {"run_id": self.run_id, "path": str(self.path), "events_written": self._count, "events_dropped": self._dropped}

    def _run(self) -> None:
        with self.path.open("a", encoding="utf-8", buffering=1) as handle:
            while not self._stop.is_set() or not self.event_queue.empty():
                try:
                    event = self.event_queue.get(timeout=0.15)
                except queue.Empty:
                    continue
                event["received_at_utc"] = datetime.now(UTC).isoformat()
                handle.write(json.dumps(event, ensure_ascii=False, separators=(",", ":")) + "\n")
                if event.get("event") in {"request_started", "worker_exit", "worker_timeout", "worker_replaced", "stage_failed"}:
                    handle.flush()
                with self._lock:
                    self._count += 1
