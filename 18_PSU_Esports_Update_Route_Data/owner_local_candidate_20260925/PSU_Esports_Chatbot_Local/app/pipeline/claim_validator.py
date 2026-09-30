from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from app.core.normalization import normalize_text


@dataclass(frozen=True)
class GroundingValidation:
    ok: bool
    unsupported_claims: tuple[str, ...] = ()
    unsupported_numbers: tuple[str, ...] = ()
    warnings: tuple[str, ...] = ()

    def as_dict(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "unsupported_claims": list(self.unsupported_claims),
            "unsupported_numbers": list(self.unsupported_numbers),
            "warnings": list(self.warnings),
        }


def _evidence_text(evidence: dict[str, Any]) -> str:
    parts: list[str] = []
    for item in evidence.get("items", []) if isinstance(evidence, dict) else []:
        if isinstance(item, dict):
            parts.append(str(item.get("text") or ""))
            parts.append(str(item.get("title") or ""))
    return normalize_text("\n".join(parts))


def validate_grounded_claims(answer: str, evidence: dict[str, Any]) -> GroundingValidation:
    answer_text = normalize_text(answer)
    source_text = _evidence_text(evidence)
    if not answer_text or not source_text:
        return GroundingValidation(True, warnings=("claim_check_skipped_missing_text",))

    answer_numbers = set(re.findall(r"(?<![A-Za-z])\d+(?:[.,]\d+)?", answer_text))
    evidence_numbers = set(re.findall(r"(?<![A-Za-z])\d+(?:[.,]\d+)?", source_text))
    unsupported_numbers = tuple(sorted(answer_numbers - evidence_numbers))

    claims: list[str] = []
    for raw in re.split(r"[\n.!?]+", answer_text):
        claim = raw.strip(" -•\t")
        if len(claim) < 18 or claim.startswith("แหล่งข้อมูล:"):
            continue
        claims.append(claim)

    unsupported_claims: list[str] = []
    for claim in claims:
        tokens = [token for token in re.findall(r"[A-Za-z0-9\u0E00-\u0E7F]+", claim) if len(token) >= 3]
        if not tokens:
            continue
        overlap = sum(1 for token in tokens if token in source_text) / len(tokens)
        if overlap < 0.08 and not re.search(r"\d", claim):
            unsupported_claims.append(claim[:160])

    warnings: list[str] = []
    if unsupported_claims:
        warnings.append("low_evidence_overlap_claims")
    if unsupported_numbers:
        warnings.append("unsupported_numeric_claims")
    return GroundingValidation(
        ok=not unsupported_numbers,
        unsupported_claims=tuple(unsupported_claims[:3]),
        unsupported_numbers=unsupported_numbers,
        warnings=tuple(warnings),
    )
