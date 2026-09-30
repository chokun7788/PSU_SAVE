from __future__ import annotations

import os
import re
from dataclasses import dataclass
from functools import lru_cache

from app.core.keyboard_input_anomaly import KeyboardInputAnomalyDetector
from app.core.runtime_input_quality_guard import load_runtime_clean_texts


THAI_RE = re.compile(r"[\u0E00-\u0E7F]")
LATIN_RE = re.compile(r"[A-Za-z]")
CHAT_STYLE_RE = re.compile(r"\b(?:u|ur|pls|plz|r)\b", re.IGNORECASE)
# Only identify *extra* letters between the game word and the ordinary
# catalogue forms.  The earlier broad pattern accidentally matched normal
# phrases such as "มีเกมอะไรบ้าง" by treating part of "อะไร" as an inserted
# character, forcing a needless Intent LLM call for a deterministic list.
THAI_GAME_CATALOG_SURFACE_VARIANT_RE = re.compile(
    r"(?:เกม|เกมส์)(?:ออะไร|อไร|มอะไร|มไร|สอะไร|สไร|อออะไร|ออไร|ไรร)(?:บ้าง|มั่ง)?"
)


@dataclass(frozen=True)
class InputRecoverySignal:
    """A non-mutating signal that a short message may contain surface typos.

    This is deliberately a routing signal, not a spell corrector. It must not
    replace user text, modify numbers, names, game titles, prices, or dates.
    """

    score: float
    language: str
    language_quality: float
    should_review_intent: bool
    reason: str

    def as_dict(self) -> dict[str, object]:
        return {
            "score": self.score,
            "language": self.language,
            "language_quality": self.language_quality,
            "should_review_intent": self.should_review_intent,
            "reason": self.reason,
            "action": "bounded_llm_intent_review" if self.should_review_intent else "continue",
        }


def _threshold() -> float:
    try:
        return max(0.0, min(1.0, float(os.getenv("PSU_SURFACE_TYPO_REVIEW_THRESHOLD", "0.43"))))
    except ValueError:
        return 0.43


@lru_cache(maxsize=1)
def _runtime_detector() -> KeyboardInputAnomalyDetector:
    # The corpus contains published knowledge only. It is intentionally not
    # fitted on chat logs, so one user's text cannot influence another user's
    # routing decision.
    return KeyboardInputAnomalyDetector().fit(load_runtime_clean_texts())


def has_thai_game_catalog_surface_variant(value: str) -> bool:
    """Detect a small inserted/repeated Thai character in a catalog request.

    This is intentionally a routing signal only. The original user text remains
    unchanged and the model is asked to review intent before any verified
    catalog renderer is selected.
    """
    compact = re.sub(r"\s+", "", str(value or ""))
    return bool(THAI_GAME_CATALOG_SURFACE_VARIANT_RE.search(compact))


def inspect_surface_input(value: str) -> InputRecoverySignal:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    thai_count = len(THAI_RE.findall(text))
    latin_count = len(LATIN_RE.findall(text))
    if not text:
        return InputRecoverySignal(0.0, "unknown", 1.0, False, "empty input")

    detector = _runtime_detector()
    if thai_count >= 4:
        quality = detector.thai_profile.quality(text)
        score = 1.0 - quality
        language = "th" if not latin_count else "mixed"
        reason = f"Thai character n-gram quality={quality:.3f}"
    elif latin_count >= 4:
        quality = detector.english_profile.quality(text)
        score = 1.0 - quality
        if CHAT_STYLE_RE.search(text):
            score = max(score, 0.45)
            reason = "English chat-style shorthand is present"
        else:
            reason = f"English character n-gram quality={quality:.3f}"
        language = "en"
    else:
        return InputRecoverySignal(0.0, "mixed", 1.0, False, "too short for surface analysis")

    catalog_surface_variant = thai_count >= 4 and has_thai_game_catalog_surface_variant(text)
    if catalog_surface_variant:
        score = max(score, _threshold())
        reason = "Thai game-catalog surface variant is present"

    score = round(max(0.0, min(1.0, score)), 4)
    # Names, codes, URLs, and longer documents are not candidates for surface
    # recovery. The user should receive normal target clarification instead.
    should_review = len(text) <= 48 and (score >= _threshold() or catalog_surface_variant)
    return InputRecoverySignal(score, language, round(quality, 4), should_review, reason)


def surface_input_clarification(locale: str) -> str:
    if locale == "en":
        return (
            "I may not have read the wording completely. Which topic do you mean: "
            "games or equipment, service price, booking, opening hours, rules, or this chatbot?"
        )
    return (
        "ผมอาจอ่านคำนี้ได้ไม่ครบครับ ต้องการถามเรื่องไหน: "
        "เกมหรืออุปกรณ์, ราคา, การจอง, เวลาเปิด-ปิด, กฎ หรือถามเกี่ยวกับแชทบอทนี้ครับ?"
    )
