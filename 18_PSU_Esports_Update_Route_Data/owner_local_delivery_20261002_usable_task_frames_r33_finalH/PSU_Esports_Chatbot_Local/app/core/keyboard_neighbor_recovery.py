"""Conservative Thai keyboard-neighbor recovery for well-formed intents.

This is a candidate generator, not a general spell checker. A correction is
used for routing only when one adjacent-key substitution and a narrow sentence
context agree on a single canonical intent word.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass

from app.core.normalization import KEYBOARD_EN_TO_THAI


_ROWS = ("1234567890-=", "qwertyuiop[]\\", "asdfghjkl;'", "zxcvbnm,./")
_ROW_OFFSETS = (0.0, 0.5, 0.75, 1.25)
_TARGETS = ("สวัสดี", "จอง", "ว่าง", "เกม")
# A valid domain word must not be treated as a typo just because its last key
# sits next to the intended key. "ใช้จอยยังไง" is about game controls.
_KNOWN_VALID_OBSERVATIONS = {"จอย"}
_RESOURCE_CONTEXT = re.compile(
    r"\b(?:pc|ps5|vr)\s*#?\s*\d{0,2}\b|\b(?:cockpit|nintendo|switch|playstation)\b"
    r"|คอม|เครื่อง|โซน|ค็อกพิท|คอกพิท|นินเทนโด|วีอาร์|เพลย์",
    re.IGNORECASE,
)


def _key_positions() -> dict[str, tuple[int, float]]:
    positions: dict[str, tuple[int, float]] = {}
    for row_index, row in enumerate(_ROWS):
        for column, key in enumerate(row):
            character = KEYBOARD_EN_TO_THAI.get(key, "")
            if len(character) == 1 and "\u0e00" <= character <= "\u0e7f":
                positions[character] = (row_index, column + _ROW_OFFSETS[row_index])
    return positions


_KEY_POSITIONS = _key_positions()


def adjacent_key_substitution(observed: str, intended: str) -> bool:
    """Whether two Thai characters occupy neighboring unshifted Kedmanee keys."""
    if observed == intended or observed not in _KEY_POSITIONS or intended not in _KEY_POSITIONS:
        return False
    if (unicodedata.category(observed) == "Mn") != (unicodedata.category(intended) == "Mn"):
        return False
    observed_row, observed_col = _KEY_POSITIONS[observed]
    intended_row, intended_col = _KEY_POSITIONS[intended]
    return abs(observed_row - intended_row) <= 1 and abs(observed_col - intended_col) <= 1.25


def _one_neighbor_error(observed: str, intended: str) -> bool:
    if len(observed) != len(intended):
        return False
    differences = [(a, b) for a, b in zip(observed, intended) if a != b]
    return len(differences) == 1 and adjacent_key_substitution(*differences[0])


def _context_agrees(text: str, target: str, start: int, end: int) -> bool:
    left, right = text[:start], text[end:]
    if target == "สวัสดี":
        return not left.strip() and bool(re.fullmatch(r"\s*(?:ครับ|ค่ะ|คับ|คะ)?[!?.ฯ\s]*", right))
    if target == "จอง":
        return bool(re.match(r"\s*(?:ยังไง|อย่างไร|ไง|ได้ไหม|ได้มั้ย|ล่วงหน้า|กี่วัน|กี่โมง)", right))
    if target == "ว่าง":
        return bool(re.match(r"\s*(?:ไหม|มั้ย|หรือเปล่า|รึเปล่า)", right)) and bool(_RESOURCE_CONTEXT.search(text))
    if target == "เกม":
        return left.rstrip().endswith("มี") and bool(re.match(r"\s*(?:อะไร|ไหน|กี่เกม)", right))
    return False


@dataclass(frozen=True)
class KeyboardNeighborRecovery:
    original: str
    candidate: str
    observed: str
    intended: str
    start: int


def detect_keyboard_neighbor_recovery(value: str) -> KeyboardNeighborRecovery | None:
    text = str(value or "").strip()
    if not text or len(text) > 120 or not re.search(r"[\u0e00-\u0e7f]", text):
        return None
    candidates: list[KeyboardNeighborRecovery] = []
    for target in _TARGETS:
        if target in text:
            continue
        for start in range(len(text) - len(target) + 1):
            end = start + len(target)
            observed = text[start:end]
            if observed in _KNOWN_VALID_OBSERVATIONS:
                continue
            if _one_neighbor_error(observed, target) and _context_agrees(text, target, start, end):
                candidates.append(KeyboardNeighborRecovery(
                    original=text,
                    candidate=text[:start] + target + text[end:],
                    observed=observed,
                    intended=target,
                    start=start,
                ))
                if len(candidates) > 1:
                    return None
    return candidates[0] if candidates else None


def recover_keyboard_neighbor_query(value: str) -> str:
    recovery = detect_keyboard_neighbor_recovery(value)
    return recovery.candidate if recovery is not None else value
