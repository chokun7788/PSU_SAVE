from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class SourceRef:
    source_id: str
    url: str = ""
    title: str = ""


@dataclass
class RouteDecision:
    route: str
    confidence: float
    reason: str
    answer_type: str = "unknown"
    category: str = "unknown"
    sources: list[SourceRef] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class AnswerResult:
    answer: str
    route: RouteDecision
    elapsed_sec: float | None = None
    raw_hits: list[dict[str, Any]] = field(default_factory=list)
