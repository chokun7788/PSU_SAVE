from __future__ import annotations

import hashlib
import os
from contextlib import contextmanager
from contextvars import ContextVar, Token
from dataclasses import dataclass, field
from typing import Any, Iterator

from app.core.normalization import normalize_text
from app.core.locale import LocaleDecision


@dataclass
class RequestExecutionContext:
    """Bounded, request-local state shared by Pipeline stages.

    The context must never cross an HTTP request or a session boundary.  It is
    deliberately small: it prevents duplicate deterministic work but is not a
    general cache.
    """

    catalog_version: str = ""
    game_resolutions: dict[tuple[str, str, str], Any] = field(default_factory=dict)
    attempted_capabilities: set[tuple[str, str, tuple[str, ...]]] = field(default_factory=set)
    retrieval_results: dict[tuple[str, str, str], Any] = field(default_factory=dict)
    competition_resolutions: dict[str, Any] = field(default_factory=dict)
    trace_sequence: int = 0
    counters: dict[str, int] = field(default_factory=dict)
    locale_decision: LocaleDecision | None = None

    def next_sequence(self) -> int:
        self.trace_sequence += 1
        return self.trace_sequence

    def increment(self, name: str) -> int:
        value = self.counters.get(name, 0) + 1
        self.counters[name] = value
        return value

    def game_key(self, query: str, operation: str, catalog_version: str) -> tuple[str, str, str]:
        digest = hashlib.sha256(normalize_text(query).encode("utf-8")).hexdigest()
        return digest, str(operation or ""), str(catalog_version or self.catalog_version)

    def get_game_resolution(self, query: str, operation: str, catalog_version: str) -> Any | None:
        return self.game_resolutions.get(self.game_key(query, operation, catalog_version))

    def store_game_resolution(self, query: str, operation: str, catalog_version: str, result: Any) -> None:
        if len(self.game_resolutions) >= _env_int("PSU_REQUEST_CONTEXT_MAX_RESOLUTIONS", 4):
            self.increment("game_resolution_cache_store_skipped")
            return
        self.game_resolutions[self.game_key(query, operation, catalog_version)] = result

    def begin_capability(
        self,
        capability_id: str,
        operation: str,
        target_ids: tuple[str, ...] = (),
    ) -> bool:
        key = (str(capability_id), str(operation or ""), tuple(target_ids))
        if key in self.attempted_capabilities:
            self.increment("duplicate_capability_skipped")
            return False
        if len(self.attempted_capabilities) >= _env_int("PSU_REQUEST_CONTEXT_MAX_ATTEMPTS", 16):
            self.increment("capability_attempt_limit_reached")
            return False
        self.attempted_capabilities.add(key)
        self.increment("capability_attempts")
        return True

    def competition_key(self, query: str) -> str:
        # Competition target matching preserves the original surface form.
        # General normalize_text() may intentionally rewrite ordinary FAQ
        # language, so it is not used to identify this request-local cache.
        value = " ".join(str(query or "").casefold().split())
        return hashlib.sha256(value.encode("utf-8")).hexdigest()

    def get_competition_resolution(self, query: str) -> Any | None:
        result = self.competition_resolutions.get(self.competition_key(query))
        if result is not None:
            self.increment("competition_resolution_reused")
        return result

    def store_competition_resolution(self, query: str, result: Any) -> None:
        if len(self.competition_resolutions) >= _env_int("PSU_REQUEST_CONTEXT_MAX_COMPETITION_RESOLUTIONS", 4):
            self.increment("competition_resolution_cache_store_skipped")
            return
        self.competition_resolutions[self.competition_key(query)] = result
        self.increment("competition_resolution_computed")

    def as_metadata(self) -> dict[str, Any]:
        return {
            "request_context": True,
            "request_context_catalog_version": self.catalog_version,
            "request_context_game_resolution_count": len(self.game_resolutions),
            "request_context_attempted_capability_count": len(self.attempted_capabilities),
            "request_context_competition_resolution_count": len(self.competition_resolutions),
            "request_context_counters": dict(self.counters),
            "request_context_locale": (
                self.locale_decision.to_dict() if self.locale_decision is not None else None
            ),
        }


def _env_int(name: str, default: int) -> int:
    try:
        return max(1, int(os.getenv(name, str(default))))
    except ValueError:
        return default


_CURRENT_CONTEXT: ContextVar[RequestExecutionContext | None] = ContextVar(
    "psu_request_execution_context",
    default=None,
)


@contextmanager
def request_execution_context(*, catalog_version: str = "") -> Iterator[RequestExecutionContext]:
    context = RequestExecutionContext(catalog_version=catalog_version)
    token: Token[RequestExecutionContext | None] = _CURRENT_CONTEXT.set(context)
    try:
        yield context
    finally:
        _CURRENT_CONTEXT.reset(token)


def current_execution_context() -> RequestExecutionContext | None:
    return _CURRENT_CONTEXT.get()


def current_locale_decision() -> LocaleDecision | None:
    context = current_execution_context()
    return context.locale_decision if context is not None else None


def set_current_locale_decision(decision: LocaleDecision) -> None:
    context = current_execution_context()
    if context is not None:
        context.locale_decision = decision
