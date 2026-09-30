from __future__ import annotations

import os
import time
from contextlib import contextmanager
from contextvars import ContextVar, Token
from dataclasses import dataclass
from typing import Any, Iterator

from app.pipeline.execution_context import request_execution_context


class StageDeadlineExceeded(TimeoutError):
    """Raised before an expensive stage starts or from a cooperative loop."""

    def __init__(self, stage: str, elapsed: float, remaining: float) -> None:
        self.stage = str(stage)
        self.elapsed = max(0.0, float(elapsed))
        self.remaining = max(0.0, float(remaining))
        super().__init__(
            f"request budget exhausted at {self.stage}: "
            f"elapsed={self.elapsed:.4f}s remaining={self.remaining:.4f}s"
        )


@dataclass(frozen=True)
class RequestBudget:
    started: float
    timeout_sec: float
    finalizer_reserve_sec: float
    deadline: float

    def elapsed(self) -> float:
        return max(0.0, time.perf_counter() - self.started)

    def remaining(self) -> float:
        return max(0.0, self.deadline - time.perf_counter())

    def work_remaining(self) -> float:
        return max(0.0, self.remaining() - self.finalizer_reserve_sec)

    def allow_stage(self, required_sec: float = 0.0, *, include_finalizer_reserve: bool = True) -> bool:
        available = self.work_remaining() if include_finalizer_reserve else self.remaining()
        return available >= max(0.0, float(required_sec))

    def checkpoint(self, stage: str, required_sec: float = 0.0) -> None:
        if self.remaining() <= 0.0 or not self.allow_stage(required_sec):
            raise StageDeadlineExceeded(stage, self.elapsed(), self.remaining())

    def metadata(self) -> dict[str, float | bool]:
        return {
            "global_timeout_enabled": True,
            "global_timeout_sec": round(self.timeout_sec, 4),
            "global_elapsed_sec": round(self.elapsed(), 4),
            "global_remaining_sec": round(self.remaining(), 4),
            "finalizer_reserve_sec": round(self.finalizer_reserve_sec, 4),
            "work_remaining_sec": round(self.work_remaining(), 4),
        }


@dataclass(frozen=True)
class RequestDeadline:
    started: float
    timeout_sec: float
    deadline: float
    budget: RequestBudget


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
        # The request context also deduplicates deterministic work when the
        # deadline feature flag is off (for example during local development).
        with request_execution_context():
            yield None
        return

    started = time.perf_counter()
    budget = RequestBudget(
        started=started,
        timeout_sec=timeout,
        finalizer_reserve_sec=configured_finalizer_reserve_sec(),
        deadline=started + timeout,
    )
    deadline = RequestDeadline(
        started=started,
        timeout_sec=timeout,
        deadline=budget.deadline,
        budget=budget,
    )
    token: Token[RequestDeadline | None] = _CURRENT_DEADLINE.set(deadline)
    budget_token: Token[LlmCallBudget | None] = _CURRENT_LLM_BUDGET.set(
        LlmCallBudget(max_calls=configured_llm_max_calls(), kinds=[])
    )
    try:
        with request_execution_context():
            yield deadline
    finally:
        _CURRENT_LLM_BUDGET.reset(budget_token)
        _CURRENT_DEADLINE.reset(token)


def current_deadline() -> RequestDeadline | None:
    return _CURRENT_DEADLINE.get()


def deadline_enabled() -> bool:
    return current_deadline() is not None


def current_budget() -> RequestBudget | None:
    deadline = current_deadline()
    return deadline.budget if deadline is not None else None


def elapsed_sec() -> float:
    budget = current_budget()
    if budget is None:
        return 0.0
    return budget.elapsed()


def remaining_sec() -> float | None:
    budget = current_budget()
    if budget is None:
        return None
    return budget.remaining()


def deadline_exceeded() -> bool:
    remaining = remaining_sec()
    return remaining is not None and remaining <= 0


def allow_stage(required_sec: float = 0.0, *, include_finalizer_reserve: bool = True) -> bool:
    budget = current_budget()
    return budget is None or budget.allow_stage(
        required_sec,
        include_finalizer_reserve=include_finalizer_reserve,
    )


def checkpoint(stage: str, required_sec: float = 0.0) -> None:
    budget = current_budget()
    if budget is not None:
        budget.checkpoint(stage, required_sec)


def timeout_for_call(configured_timeout_sec: float, *, min_timeout_sec: float = 0.05) -> float:
    budget = current_budget()
    if budget is None:
        return configured_timeout_sec
    available = budget.work_remaining()
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


def deadline_metadata() -> dict[str, float | bool | str]:
    budget = current_budget()
    if budget is None:
        return {
            "global_timeout_enabled": False,
            "global_timeout_sec": 0.0,
            "global_elapsed_sec": 0.0,
            "global_remaining_sec": 0.0,
            "finalizer_reserve_sec": configured_finalizer_reserve_sec(),
            "work_remaining_sec": 0.0,
        }
    return {**budget.metadata(), "timing_status": "running"}
