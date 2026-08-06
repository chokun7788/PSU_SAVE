from __future__ import annotations

import os
from dataclasses import dataclass

from app.core.normalization import normalize_text


@dataclass(frozen=True)
class CompoundProfile:
    """Deterministic policy for a multi-part request.

    The profile decides whether children are independent enough for bounded
    parallel execution. It does not decide the answer or replace routing.
    """

    level: str
    score: float
    signals: tuple[str, ...]
    can_parallelize: bool
    requires_planner: bool
    max_workers: int
    reason: str

    def as_dict(self) -> dict[str, object]:
        return {
            "level": self.level,
            "score": self.score,
            "signals": list(self.signals),
            "can_parallelize": self.can_parallelize,
            "requires_planner": self.requires_planner,
            "max_workers": self.max_workers,
            "reason": self.reason,
        }


@dataclass(frozen=True)
class CompoundNode:
    index: int
    question: str
    depends_on: tuple[int, ...] = ()

    def as_dict(self) -> dict[str, object]:
        return {
            "index": self.index,
            "question": self.question,
            "depends_on": list(self.depends_on),
        }


@dataclass(frozen=True)
class CompoundPlan:
    profile: CompoundProfile
    nodes: tuple[CompoundNode, ...]

    def as_dict(self) -> dict[str, object]:
        return {
            "profile": self.profile.as_dict(),
            "nodes": [node.as_dict() for node in self.nodes],
        }


_DEPENDENCY_TERMS = (
    "แล้วค่อย", "จากนั้น", "ต่อจาก", "ผลลัพธ์", "อันนั้น", "เครื่องนั้น",
    "เกมนั้น", "โซนนั้น", "รายการนั้น", "ดังกล่าว", "เยอะสุด", "มากที่สุด",
    "อันดับ", "เรียง", "คำนวณ", "รวมทั้งหมด", "เฉลี่ย", "เปรียบเทียบ",
    "then", "after that", "the result", "that one", "most", "rank", "calculate",
    "compare",
)

_BROAD_TERMS = (
    "ทำไรได้บ้าง", "ทำอะไรได้บ้าง", "ช่วยอะไรได้บ้าง", "ถามอะไรได้บ้าง",
    "อธิบาย", "แนะนำ", "ภาพรวม", "ทั้งหมด", "หลายอย่าง", "ทั่วไป",
    "what can you do", "explain", "recommend", "overview",
)

_CALCULATION_TERMS = (
    "เยอะสุด", "มากที่สุด", "น้อยที่สุด", "อันดับ", "รวม", "เฉลี่ย", "เทียบ",
    "เปรียบเทียบ", "ต่างกัน", "คำนวณ", "กี่เครื่อง", "กี่เกม",
    "most", "least", "rank", "total", "average", "compare",
)


def _has_any(query: str, terms: tuple[str, ...]) -> bool:
    return any(term in query for term in terms)


def _max_workers() -> int:
    try:
        value = int(os.getenv("PSU_COMPOUND_MAX_WORKERS", "2"))
    except ValueError:
        value = 2
    return max(1, min(3, value))


def classify_compound(question: str, parts: list[str]) -> CompoundProfile:
    """Classify compound complexity before planner/child execution.

    Clear independent operations are eligible for a small worker pool. Any
    dependency, ranking/calculation, broad request, or 3+ parts stays ordered
    so the system can preserve context and use the constrained planner.
    """
    if len(parts) <= 1:
        return CompoundProfile("simple", 0.0, (), False, False, 1, "single question")

    normalized = normalize_text(question or "")
    signals: list[str] = []
    if _has_any(normalized, _DEPENDENCY_TERMS):
        signals.append("dependency_or_reference")
    if _has_any(normalized, _BROAD_TERMS):
        signals.append("broad_or_open_ended")
    if _has_any(normalized, _CALCULATION_TERMS):
        signals.append("calculation_or_comparison")
    if len(parts) >= 3:
        signals.append("three_or_more_parts")

    score = min(1.0, 0.18 * len(parts) + 0.30 * len(signals))
    requires_planner = bool(signals)
    can_parallelize = not requires_planner
    if len(parts) >= 3:
        level = "complex"
    elif requires_planner:
        level = "complex"
    else:
        level = "simple"

    reason = "independent child operations" if can_parallelize else "; ".join(signals)
    return CompoundProfile(
        level=level,
        score=round(score, 3),
        signals=tuple(signals),
        can_parallelize=can_parallelize,
        requires_planner=requires_planner,
        max_workers=_max_workers(),
        reason=reason,
    )


def build_compound_plan(question: str, parts: list[str], profile: CompoundProfile | None = None) -> CompoundPlan:
    active_profile = profile or classify_compound(question, parts)
    if active_profile.can_parallelize:
        nodes = tuple(CompoundNode(index=index, question=part) for index, part in enumerate(parts, 1))
    else:
        # A conservative dependency chain is safer than guessing a partial DAG.
        # The planner can later enrich this without changing the executor API.
        nodes = tuple(
            CompoundNode(index=index, question=part, depends_on=(index - 1,) if index > 1 else ())
            for index, part in enumerate(parts, 1)
        )
    return CompoundPlan(active_profile, nodes)
