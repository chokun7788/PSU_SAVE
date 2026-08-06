from __future__ import annotations

import json
import os
import threading
import time
import urllib.error
import urllib.request
from contextvars import ContextVar
from dataclasses import dataclass, field
from typing import Any

from app.pipeline.request_deadline import remaining_sec, reserve_llm_call


DEFAULT_OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434")


@dataclass
class LlmHealthState:
    failures: int = 0
    successes: int = 0
    last_error: str = ""
    last_error_type: str = ""
    last_elapsed_ms: float = 0.0
    last_checked_at: float = 0.0
    cooldown_until: float = 0.0
    last_success_at: float = 0.0
    events: list[dict[str, Any]] = field(default_factory=list)


_STATES: dict[tuple[str, str], LlmHealthState] = {}
_SLOT_LOCK = threading.Lock()
_SLOT_SEMAPHORE: threading.BoundedSemaphore | None = None
_SLOT_LIMIT: int | None = None
_HELD_SLOT: ContextVar[threading.BoundedSemaphore | None] = ContextVar("psu_llm_slot", default=None)


def _truthy(value: str | None, *, default: bool = True) -> bool:
    if value is None or value == "":
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


def llm_health_enabled() -> bool:
    return _truthy(os.getenv("PSU_LLM_HEALTH_MANAGER"), default=True)


def llm_preflight_enabled() -> bool:
    return _truthy(os.getenv("PSU_LLM_PREFLIGHT"), default=True)


def _failure_threshold() -> int:
    return max(1, int(os.getenv("PSU_LLM_HEALTH_FAILURE_THRESHOLD", "2")))


def _cooldown_sec() -> float:
    return max(1.0, float(os.getenv("PSU_LLM_HEALTH_COOLDOWN_SEC", "90")))


def _now() -> float:
    return time.time()


def _key(kind: str, model: str) -> tuple[str, str]:
    return (str(kind or "unknown"), str(model or "unknown"))


def _model_key(model: str) -> tuple[str, str]:
    return ("model", str(model or "unknown"))


def _state(kind: str, model: str) -> LlmHealthState:
    return _STATES.setdefault(_key(kind, model), LlmHealthState())


def _model_state(model: str) -> LlmHealthState:
    return _STATES.setdefault(_model_key(model), LlmHealthState())


def _concurrency_limit() -> int:
    try:
        return max(1, min(4, int(os.getenv("PSU_LLM_MAX_CONCURRENCY", "1"))))
    except ValueError:
        return 1


def _slot_semaphore() -> threading.BoundedSemaphore:
    global _SLOT_LIMIT, _SLOT_SEMAPHORE
    with _SLOT_LOCK:
        if _SLOT_SEMAPHORE is None:
            _SLOT_LIMIT = _concurrency_limit()
            _SLOT_SEMAPHORE = threading.BoundedSemaphore(_SLOT_LIMIT)
        return _SLOT_SEMAPHORE


def _acquire_llm_slot() -> tuple[bool, dict[str, Any]]:
    if _HELD_SLOT.get() is not None:
        return True, {"llm_concurrency_allowed": True, "llm_concurrency_reused": True}
    semaphore = _slot_semaphore()
    try:
        wait_sec = max(0.0, min(1.0, float(os.getenv("PSU_LLM_CONCURRENCY_WAIT_SEC", "0.20"))))
    except ValueError:
        wait_sec = 0.20
    remaining = remaining_sec()
    if remaining is not None:
        wait_sec = min(wait_sec, max(0.0, remaining - 0.05))
    acquired = semaphore.acquire(timeout=wait_sec)
    if not acquired:
        return False, {
            "llm_concurrency_allowed": False,
            "llm_concurrency_limit": _SLOT_LIMIT or 1,
            "llm_concurrency_wait_sec": round(wait_sec, 3),
            "llm_concurrency_reason": "LLM concurrency limit is busy",
        }
    _HELD_SLOT.set(semaphore)
    return True, {
        "llm_concurrency_allowed": True,
        "llm_concurrency_limit": _SLOT_LIMIT or 1,
        "llm_concurrency_wait_sec": round(wait_sec, 3),
    }


def release_llm_slot() -> None:
    semaphore = _HELD_SLOT.get()
    if semaphore is None:
        return
    _HELD_SLOT.set(None)
    semaphore.release()


def _append_event(state: LlmHealthState, event: dict[str, Any]) -> None:
    state.events.append(event)
    if len(state.events) > 12:
        del state.events[:-12]


def llm_call_allowed(kind: str, model: str) -> tuple[bool, dict[str, Any]]:
    if not llm_health_enabled():
        budget_allowed, budget_metadata = reserve_llm_call(kind)
        metadata = {
            "llm_health_enabled": False,
            "llm_health_status": "disabled",
            "llm_health_allowed": budget_allowed,
        }
        metadata.update(budget_metadata)
        if not budget_allowed:
            metadata["llm_health_reason"] = "request LLM call budget exhausted"
            return False, metadata
        slot_allowed, slot_metadata = _acquire_llm_slot()
        metadata.update(slot_metadata)
        return slot_allowed, metadata

    now = _now()
    model_state = _model_state(model)
    kind_state = _state(kind, model)
    cooldown_until = max(model_state.cooldown_until, kind_state.cooldown_until)
    remaining = max(0.0, cooldown_until - now)
    allowed = remaining <= 0
    metadata = {
        "llm_health_enabled": True,
        "llm_health_allowed": allowed,
        "llm_health_status": "ok" if allowed else "cooldown",
        "llm_health_kind": kind,
        "llm_health_model": model,
        "llm_health_failures": max(model_state.failures, kind_state.failures),
        "llm_health_cooldown_remaining_sec": round(remaining, 2),
        "llm_health_last_error_type": model_state.last_error_type or kind_state.last_error_type,
        "llm_health_last_error": model_state.last_error or kind_state.last_error,
    }
    if not allowed:
        metadata["llm_health_reason"] = "circuit breaker cooldown active"
        return False, metadata

    budget_allowed, budget_metadata = reserve_llm_call(kind)
    metadata.update(budget_metadata)
    if not budget_allowed:
        metadata["llm_health_reason"] = "request LLM call budget exhausted"
        return False, metadata
    slot_allowed, slot_metadata = _acquire_llm_slot()
    metadata.update(slot_metadata)
    return slot_allowed, metadata


def _record_success_for_state(state: LlmHealthState, *, elapsed_ms: float, event: dict[str, Any]) -> None:
    state.successes += 1
    state.failures = 0
    state.last_error = ""
    state.last_error_type = ""
    state.last_elapsed_ms = round(elapsed_ms, 2)
    state.last_checked_at = _now()
    state.last_success_at = state.last_checked_at
    state.cooldown_until = 0.0
    _append_event(state, event)


def record_llm_success(kind: str, model: str, *, elapsed_ms: float, detail: str = "") -> dict[str, Any]:
    release_llm_slot()
    if not llm_health_enabled():
        return {"llm_health_enabled": False}
    event = {
        "event": "success",
        "kind": kind,
        "elapsed_ms": round(elapsed_ms, 2),
        "detail": detail,
        "at": round(_now(), 3),
    }
    _record_success_for_state(_state(kind, model), elapsed_ms=elapsed_ms, event=event)
    _record_success_for_state(_model_state(model), elapsed_ms=elapsed_ms, event=event)
    return {
        "llm_health_enabled": True,
        "llm_health_status": "ok",
        "llm_health_failures": 0,
    }


def _record_failure_for_state(
    state: LlmHealthState,
    *,
    kind: str,
    error_type: str,
    error: str,
    elapsed_ms: float,
) -> None:
    state.failures += 1
    state.last_error_type = error_type
    state.last_error = error[:300]
    state.last_elapsed_ms = round(elapsed_ms, 2)
    state.last_checked_at = _now()
    if state.failures >= _failure_threshold():
        state.cooldown_until = max(state.cooldown_until, _now() + _cooldown_sec())
    _append_event(
        state,
        {
            "event": "failure",
            "kind": kind,
            "error_type": error_type,
            "error": error[:180],
            "elapsed_ms": round(elapsed_ms, 2),
            "failures": state.failures,
            "cooldown_until": round(state.cooldown_until, 3) if state.cooldown_until else 0.0,
            "at": round(_now(), 3),
        },
    )


def record_llm_failure(
    kind: str,
    model: str,
    *,
    error_type: str,
    error: str,
    elapsed_ms: float,
) -> dict[str, Any]:
    release_llm_slot()
    if not llm_health_enabled():
        return {"llm_health_enabled": False}
    kind_state = _state(kind, model)
    model_state = _model_state(model)
    _record_failure_for_state(kind_state, kind=kind, error_type=error_type, error=error, elapsed_ms=elapsed_ms)
    _record_failure_for_state(model_state, kind=kind, error_type=error_type, error=error, elapsed_ms=elapsed_ms)
    cooldown_until = max(kind_state.cooldown_until, model_state.cooldown_until)
    remaining = max(0.0, cooldown_until - _now())
    return {
        "llm_health_enabled": True,
        "llm_health_status": "cooldown" if remaining > 0 else "degraded",
        "llm_health_failures": max(kind_state.failures, model_state.failures),
        "llm_health_cooldown_remaining_sec": round(remaining, 2),
        "llm_health_last_error_type": error_type,
        "llm_health_last_error": error[:300],
    }


def open_llm_circuit(
    kind: str,
    model: str,
    *,
    error_type: str,
    error: str,
    elapsed_ms: float,
    cooldown_sec: float | None = None,
) -> dict[str, Any]:
    release_llm_slot()
    if not llm_health_enabled():
        return {"llm_health_enabled": False}
    now = _now()
    cooldown = max(1.0, float(cooldown_sec if cooldown_sec is not None else _cooldown_sec()))
    for state in (_state(kind, model), _model_state(model)):
        state.failures = max(state.failures + 1, _failure_threshold())
        state.last_error_type = error_type
        state.last_error = error[:300]
        state.last_elapsed_ms = round(elapsed_ms, 2)
        state.last_checked_at = now
        state.cooldown_until = max(state.cooldown_until, now + cooldown)
        _append_event(
            state,
            {
                "event": "circuit_open",
                "kind": kind,
                "error_type": error_type,
                "error": error[:180],
                "elapsed_ms": round(elapsed_ms, 2),
                "failures": state.failures,
                "cooldown_until": round(state.cooldown_until, 3),
                "at": round(now, 3),
            },
        )
    return {
        "llm_health_enabled": True,
        "llm_health_status": "cooldown",
        "llm_health_failures": _failure_threshold(),
        "llm_health_cooldown_remaining_sec": round(cooldown, 2),
        "llm_health_last_error_type": error_type,
        "llm_health_last_error": error[:300],
    }


def reset_llm_health(model: str | None = None) -> None:
    if model is None:
        _STATES.clear()
        return
    target = str(model)
    for key in list(_STATES):
        if key[1] == target:
            _STATES.pop(key, None)


def llm_health_snapshot() -> dict[str, Any]:
    now = _now()
    states: list[dict[str, Any]] = []
    for (kind, model), state in sorted(_STATES.items()):
        remaining = max(0.0, state.cooldown_until - now)
        states.append({
            "kind": kind,
            "model": model,
            "status": "cooldown" if remaining > 0 else "ok" if state.failures == 0 else "degraded",
            "failures": state.failures,
            "successes": state.successes,
            "cooldown_remaining_sec": round(remaining, 2),
            "last_error_type": state.last_error_type,
            "last_error": state.last_error,
            "last_elapsed_ms": state.last_elapsed_ms,
            "last_checked_at": state.last_checked_at,
            "last_success_at": state.last_success_at,
            "events": list(state.events),
        })
    return {
        "enabled": llm_health_enabled(),
        "failure_threshold": _failure_threshold(),
        "cooldown_sec": _cooldown_sec(),
        "states": states,
    }


def preflight_ollama(
    *,
    model: str,
    kind: str = "preflight",
    timeout_sec: float | None = None,
    num_predict: int | None = None,
    ollama_url: str | None = None,
) -> dict[str, Any]:
    timeout = float(timeout_sec if timeout_sec is not None else os.getenv("PSU_LLM_PREFLIGHT_TIMEOUT_SEC", "5"))
    predict = int(num_predict if num_predict is not None else os.getenv("PSU_LLM_PREFLIGHT_NUM_PREDICT", "1"))
    base_url = (ollama_url or os.getenv("OLLAMA_URL", DEFAULT_OLLAMA_URL)).rstrip("/")
    prompt = "ตอบ OK เท่านั้น"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "keep_alive": os.getenv("PSU_OLLAMA_KEEP_ALIVE", "10m"),
        "think": False,
        "options": {
            "temperature": 0,
            "num_predict": predict,
            "num_ctx": 512,
        },
    }
    request = urllib.request.Request(
        f"{base_url}/api/generate",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = json.loads(response.read().decode("utf-8", errors="replace"))
        answer = str(data.get("response") or "").strip()
        elapsed_ms = (time.perf_counter() - started) * 1000
        if answer:
            health = record_llm_success(kind, model, elapsed_ms=elapsed_ms, detail="preflight_ok")
            return {
                "ok": True,
                "model": model,
                "kind": kind,
                "elapsed_ms": round(elapsed_ms, 2),
                "response_chars": len(answer),
                "done_reason": data.get("done_reason") or "",
                "health": health,
            }
        error = "empty response"
        health = open_llm_circuit(kind, model, error_type="EmptyResponse", error=error, elapsed_ms=elapsed_ms)
        return {
            "ok": False,
            "model": model,
            "kind": kind,
            "elapsed_ms": round(elapsed_ms, 2),
            "error_type": "EmptyResponse",
            "error": error,
            "health": health,
        }
    except (OSError, TimeoutError, urllib.error.URLError, json.JSONDecodeError) as exc:
        elapsed_ms = (time.perf_counter() - started) * 1000
        health = open_llm_circuit(
            kind,
            model,
            error_type=type(exc).__name__,
            error=str(exc),
            elapsed_ms=elapsed_ms,
        )
        return {
            "ok": False,
            "model": model,
            "kind": kind,
            "elapsed_ms": round(elapsed_ms, 2),
            "error_type": type(exc).__name__,
            "error": str(exc),
            "health": health,
        }
