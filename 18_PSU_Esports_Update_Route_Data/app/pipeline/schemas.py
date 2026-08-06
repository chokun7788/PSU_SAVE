from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class PreprocessedInput:
    raw_query: str
    clean_query: str
    normalized_query: str
    language_hint: str
    query_variants: tuple[str, ...] = ()


@dataclass(frozen=True)
class EntityBundle:
    day: str | None = None
    time_slots: tuple[str, ...] = ()
    service: str | None = None
    user_group: str | None = None
    duration: str | None = None
    price_intent: bool = False
    short_answer: bool = False
    comparison_intent: bool = False
    raw: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class PipelineRoute:
    category: str
    intent: str
    confidence: float
    answer_type: str
    risk: str
    reason: str


@dataclass(frozen=True)
class PipelineTrace:
    stage: str
    decision: str
    confidence: float
    detail: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class UniversalIntent:
    domain: str
    operation: str
    target: str = ""
    filters: dict[str, Any] = field(default_factory=dict)
    needs: tuple[str, ...] = ()
    answer_style: str = "direct"
    confidence: float = 0.0
    method: str = "heuristic"
    reason: str = ""


@dataclass(frozen=True)
class ValidationResult:
    ok: bool
    errors: tuple[str, ...] = ()
    warnings: tuple[str, ...] = ()


@dataclass(frozen=True)
class PipelineAnswer:
    answer: str
    hits: list[dict[str, Any]]
    elapsed: float
    mode: str
    confidence: float
    route: PipelineRoute
    entities: EntityBundle
    validation: ValidationResult
    trace: list[PipelineTrace] = field(default_factory=list)
    universal_intent: UniversalIntent | None = None
    decision_artifact: dict[str, Any] | None = None
