"""Recover a high-confidence Thai character-order typo in chatbot capability questions.

Thai leading vowels are written before a consonant. An adjacent key-order
transposition can therefore leave a familiar word visually close but outside
the existing spelling and intent matchers (for example, ดไ้ instead of ได้).
Only a short capability-question frame is accepted here.
"""

from __future__ import annotations

import re
from dataclasses import dataclass


_TARGET = "ได้"
_LEFT_CONTEXT = re.compile(r"(?:ถาม|ทำ|ช่วย|ตอบ)(?:อะไร|ไร)\s*$")
_RIGHT_CONTEXT = re.compile(r"^\s*บ้าง(?:ครับ|ค่ะ|คับ|คะ)?[!?.ฯ\s]*$")
_OTHER_SUBJECT = re.compile(
    r"เกม|ps5|\bpc\s*\d*\b|\bvr\b|nintendo|switch|cockpit|"
    r"ศูนย์|เจ้าหน้าที่|พนักงาน|ผู้จัดการ|อุปกรณ์|เครื่อง|โซน",
    re.IGNORECASE,
)


def _one_adjacent_transposition(observed: str, intended: str) -> bool:
    if observed == intended or len(observed) != len(intended):
        return False
    return any(
        observed == intended[:index] + intended[index + 1] + intended[index] + intended[index + 2 :]
        for index in range(len(intended) - 1)
    )


@dataclass(frozen=True)
class ThaiTranspositionRecovery:
    original: str
    candidate: str
    observed: str
    intended: str
    start: int


def detect_thai_transposition_recovery(value: str) -> ThaiTranspositionRecovery | None:
    text = str(value or "").strip()
    if not text or len(text) > 96 or _TARGET in text:
        return None
    candidates: list[ThaiTranspositionRecovery] = []
    for start in range(len(text) - len(_TARGET) + 1):
        end = start + len(_TARGET)
        observed = text[start:end]
        if not _one_adjacent_transposition(observed, _TARGET):
            continue
        left, right = text[:start], text[end:]
        if not _LEFT_CONTEXT.search(left) or not _RIGHT_CONTEXT.fullmatch(right):
            continue
        if _OTHER_SUBJECT.search(left):
            continue
        candidates.append(ThaiTranspositionRecovery(
            original=text,
            candidate=left + _TARGET + right,
            observed=observed,
            intended=_TARGET,
            start=start,
        ))
        if len(candidates) > 1:
            return None
    return candidates[0] if candidates else None


def recover_thai_transposition_query(value: str) -> str:
    recovery = detect_thai_transposition_recovery(value)
    return recovery.candidate if recovery is not None else value
