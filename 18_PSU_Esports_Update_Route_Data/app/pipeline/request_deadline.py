from __future__ import annotations

import os
import time
from contextlib import contextmanager
from contextvars import ContextVar, Token
from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class RequestDeadline:
    started: float
    timeout_sec: float
    deadline: float


@dataclass
class LlmCallBudget:
    max_calls: int
    used_calls: int = 0
    kinds: list[str] | None = None


_CURRENT_DEADLINE: ContextVar[RequestDeadline | None] = ContextVar("psu_request_deadline", default=None)
_CURRENT_LLM_BUDGET: ContextVar[LlmCallBudget | None] = ContextVar("psu_llm_call_budget", default=None)


def configured_llm_max_calls() -> int:
    try:
        return max(0, int(os.getenv("PSU_LLM_MAX_CALLS", "2")))
    except ValueError:
        return 2


def configured_global_timeout_sec() -> float:
    try:
        return max(0.0, float(os.getenv("PSU_PIPELINE_GLOBAL_TIMEOUT_SEC", "0")))
    except ValueError:
        return 0.0


def configured_finalizer_reserve_sec() -> float:
    """Keep enough time for validation, fallback formatting, and response I/O."""
    try:
        return max(0.0, float(os.getenv("PSU_PIPELINE_FINALIZER_RESERVE_SEC", "1.0")))
    except ValueError:
        return 1.0


@contextmanager
def request_deadline(timeout_sec: float | None = None) -> Iterator[RequestDeadline | None]:
    existing = current_deadline()
    if timeout_sec is None and existing is not None:
        # Preserve the outer API deadline and its LLM budget when the pipeline
        # is called from a request that already started the clock.
        yield existing
        return

    timeout = configured_global_timeout_sec() if timeout_sec is None else max(0.0, float(timeout_sec))
    if timeout <= 0:
        yield None
        return

    started = time.perf_counter()
    deadline = RequestDeadline(started=started, timeout_sec=timeout, deadline=started + timeout)
    token: Token[RequestDeadline | None] = _CURRENT_DEADLINE.set(deadline)
    budget_token: Token[LlmCallBudget | None] = _CURRENT_LLM_BUDGET.set(
        LlmCallBudget(max_calls=configured_llm_max_calls(), kinds=[])
    )
    try:
        yield deadline
    finally:
        _CURRENT_LLM_BUDGET.reset(budget_token)
        _CURRENT_DEADLINE.reset(token)


def current_deadline() -> RequestDeadline | None:
    return _CURRENT_DEADLINE.get()


def deadline_enabled() -> bool:
    return current_deadline() is not None


def elapsed_sec() -> float:
    deadline = current_deadline()
    if deadline is None:
        return 0.0
    return max(0.0, time.perf_counter() - deadline.started)


def remaining_sec() -> float | None:
    deadline = current_deadline()
    if deadline is None:
        return None
    return max(0.0, deadline.deadline - time.perf_counter())


def deadline_exceeded() -> bool:
    remaining = remaining_sec()
    return remaining is not None and remaining <= 0


def timeout_for_call(configured_timeout_sec: float, *, min_timeout_sec: float = 0.05) -> float:
    remaining = remaining_sec()
    if remaining is None:
        return configured_timeout_sec
    available = remaining - configured_finalizer_reserve_sec()
    if available <= min_timeout_sec:
        return 0.0
    return max(0.0, min(configured_timeout_sec, available))


def reserve_llm_call(kind: str) -> tuple[bool, dict[str, int | bool | str]]:
    """Reserve one LLM attempt for the current request.

    This is a request-level budget, not a socket cancellation mechanism. It
    prevents planner/intent/general calls from stacking without a bound.
    """
    budget = _CURRENT_LLM_BUDGET.get()
    if budget is None:
        return True, {
            "llm_budget_enabled": False,
            "llm_budget_allowed": True,
            "llm_budget_max_calls": 0,
            "llm_budget_used_calls": 0,
        }
    if budget.max_calls <= 0:
        return False, {
            "llm_budget_enabled": True,
            "llm_budget_allowed": False,
            "llm_budget_max_calls": budget.max_calls,
            "llm_budget_used_calls": budget.used_calls,
            "llm_budget_reason": "max LLM calls configured as zero",
        }
    if budget.used_calls >= budget.max_calls:
        return False, {
            "llm_budget_enabled": True,
            "llm_budget_allowed": False,
            "llm_budget_max_calls": budget.max_calls,
            "llm_budget_used_calls": budget.used_calls,
            "llm_budget_reason": "per-request LLM call budget exhausted",
        }
    budget.used_calls += 1
    if budget.kinds is not None:
        budget.kinds.append(str(kind or "unknown"))
    return True, {
        "llm_budget_enabled": True,
        "llm_budget_allowed": True,
        "llm_budget_max_calls": budget.max_calls,
        "llm_budget_used_calls": budget.used_calls,
        "llm_budget_kind": str(kind or "unknown"),
    }


def deadline_metadata() -> dict[str, float | bool]:
    deadline = current_deadline()
    if deadline is None:
        return {
            "global_timeout_enabled": False,
            "global_timeout_sec": 0.0,
            "global_elapsed_sec": 0.0,
            "global_remaining_sec": 0.0,
            "finalizer_reserve_sec": configured_finalizer_reserve_sec(),
            "work_remaining_sec": 0.0,
        }
    remaining = remaining_sec()
    reserve = configured_finalizer_reserve_sec()
    return {
        "global_timeout_enabled": True,
        "global_timeout_sec": round(deadline.timeout_sec, 4),
        "global_elapsed_sec": round(elapsed_sec(), 4),
        "global_remaining_sec": round(remaining if remaining is not None else 0.0, 4),
        "finalizer_reserve_sec": round(reserve, 4),
        "work_remaining_sec": round(max(0.0, (remaining or 0.0) - reserve), 4),
    }
