from __future__ import annotations

import os
import re
from dataclasses import asdict, dataclass
from typing import Any, Iterable


SUPPORTED_LOCALES = frozenset({"auto", "th", "en"})

_THAI_RE = re.compile(r"[\u0E00-\u0E7F]")
_LATIN_TOKEN_RE = re.compile(r"[A-Za-z]+(?:'[A-Za-z]+)?")
_THAI_TOKEN_RE = re.compile(r"[\u0E00-\u0E7F]+")
_EN_GREETING_SHAPE_RE = re.compile(r"^(?:h(?:e|i)+l+o+|hey+|hi+)$", flags=re.IGNORECASE)
_PROTECTED_RE = re.compile(
    r"https?://\S+|www\.\S+|[\w.+-]+@[\w.-]+\.\w+|"
    r"\b(?:PC|PS5|PSVR2|VR|API|QR|ID)\b|#[0-9]+",
    flags=re.IGNORECASE,
)
_UPPER_ID_RE = re.compile(r"\b(?=[A-Z0-9_-]{5,}\b)(?=[A-Z0-9_-]*\d)[A-Z0-9_-]+\b")

_EN_FUNCTION_WORDS = frozenset({
    "a", "an", "and", "are", "at", "be", "book", "booking", "can", "could",
    "about", "do", "does", "for", "from", "give", "have", "how", "i", "in",
    "is", "it", "many", "me", "much", "need", "of", "on", "open", "or", "please",
    "show", "tell", "the", "there", "this", "to", "want", "what", "when", "where",
    "which", "who", "why", "with", "would", "you", "your",
})
_THAI_FUNCTION_WORDS = (
    "กี่", "ขอ", "ของ", "คือ", "จอง", "จาก", "ได้", "ต้อง", "ที่", "เท่าไหร่",
    "เท่าไร", "เป็น", "เปิด", "มี", "ยังไง", "อย่างไร", "ราคา", "หรือ", "อะไร",
    "อยู่", "ไหม", "ให้", "ใคร", "ไหน",
)
_THAI_NATURAL_TERMS = frozenset({
    *_THAI_FUNCTION_WORDS,
    "สวัสดี", "ครับ", "ค่ะ", "คับ", "เกม", "เล่น", "อุปกรณ์", "ศูนย์",
    "กฎ", "กติกา", "จอง", "ราคา", "เวลา", "ข้อมูล", "ช่วย", "หน่อย",
})
_SHORT_EN_FOLLOWUPS = frozenset({
    "and price", "price", "and how much", "how much", "and when", "when",
    "and where", "where", "what about it", "and booking", "booking", "why",
})
_SHORT_TH_FOLLOWUPS = (
    "แล้วราคา", "ราคา", "แล้วจอง", "จอง", "แล้วที่ไหน", "ที่ไหน", "แล้วกี่โมง",
    "กี่โมง", "แล้วล่ะ", "อันนี้ล่ะ", "ทำไม",
)


@dataclass(frozen=True)
class LocaleDecision:
    requested: str
    detected: str
    effective: str
    confidence: float
    reason: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def bilingual_english_enabled() -> bool:
    return os.getenv("PSU_BILINGUAL_EN_ENABLED", "1").strip().lower() in {"1", "true", "yes", "on"}


def normalize_requested_locale(value: str | None) -> str:
    requested = str(value or "auto").strip().lower()
    return requested if requested in SUPPORTED_LOCALES else "auto"


def _history_language(recent_history: Any) -> str | None:
    if not isinstance(recent_history, list):
        return None
    for item in reversed(recent_history[-16:]):
        if not isinstance(item, dict):
            continue
        candidate = str(item.get("answer_language") or "").strip().lower()
        language = item.get("language")
        if not candidate and isinstance(language, dict):
            candidate = str(language.get("effective") or "").strip().lower()
        if candidate in {"th", "en"}:
            return candidate
    return None


def _without_protected_spans(text: str) -> str:
    return _UPPER_ID_RE.sub(" ", _PROTECTED_RE.sub(" ", text or ""))


def _is_short_followup(text: str) -> bool:
    clean = re.sub(r"\s+", " ", (text or "").strip().lower()).strip(" ?!.,")
    if not clean:
        return False
    if clean in _SHORT_EN_FOLLOWUPS or any(term == clean for term in _SHORT_TH_FOLLOWUPS):
        return True
    token_count = len(_LATIN_TOKEN_RE.findall(clean)) + len(_THAI_TOKEN_RE.findall(clean))
    return token_count <= 4 and (
        clean.startswith("and ")
        or clean.startswith("แล้ว")
        or clean in {"it", "that", "this", "อันนี้", "อันนั้น"}
    )


def _count_thai_function_words(text: str) -> int:
    return sum(1 for word in _THAI_FUNCTION_WORDS if word in text)


def _has_natural_thai_signal(text: str) -> bool:
    """Distinguish real Thai prose from English typed with a Thai layout.

    A layout detector can produce an English-intended hypothesis for Thai text
    containing a Latin game title.  Only let that hypothesis override when the
    Thai surface has no ordinary Thai words at all (for example ``ฟสสนไำก``).
    """
    clean = _without_protected_spans(text)
    return any(term in clean for term in _THAI_NATURAL_TERMS)


def _detected_from_text(text: str) -> tuple[str, float, str]:
    clean = _without_protected_spans(text)
    thai_chars = len(_THAI_RE.findall(clean))
    latin_tokens = [token.lower() for token in _LATIN_TOKEN_RE.findall(clean)]
    latin_chars = sum(len(token) for token in latin_tokens)
    en_function_count = sum(token in _EN_FUNCTION_WORDS for token in latin_tokens)
    th_function_count = _count_thai_function_words(clean)

    if thai_chars and latin_chars:
        if en_function_count >= 2 and en_function_count > th_function_count:
            return "mixed", 0.88, "mixed_english_function_words"
        if th_function_count >= 1 and th_function_count >= en_function_count:
            return "mixed", 0.88, "mixed_thai_function_words"
        return "mixed", 0.62, "mixed_scripts_uncertain"
    if thai_chars:
        return "th", min(0.99, 0.82 + min(thai_chars, 20) / 120), "thai_script"
    if latin_chars:
        if en_function_count:
            return "en", min(0.99, 0.88 + min(en_function_count, 5) * 0.02), "english_sentence_structure"
        if len(latin_tokens) == 1 and _EN_GREETING_SHAPE_RE.fullmatch(latin_tokens[0]):
            return "en", 0.84, "english_greeting_shape"
        # A bare game title, product name, acronym, or identifier is not an
        # English sentence. Keep Auto on Thai in that case; the user can still
        # choose English explicitly with the language control.
        return "unknown", 0.45, "latin_identifier_or_title"
    return "unknown", 0.30, "no_language_signal"


def resolve_locale(
    text: str,
    *,
    requested: str | None = "auto",
    recent_history: Any = None,
    keyboard_layout_direction: str | None = None,
    surface_language: str | None = None,
) -> LocaleDecision:
    requested_locale = normalize_requested_locale(requested)
    detected, confidence, reason = _detected_from_text(text)

    direction = str(keyboard_layout_direction or "").strip().lower()
    surface = str(surface_language or "").strip().lower()
    # A malformed Thai sentence can resemble English typed on a Thai keyboard.
    # When the non-mutating surface detector still sees Thai script, preserve
    # Thai as the response language and let the intent-recovery flow decide the
    # topic. Keyboard mismatch remains available as an input-quality signal.
    if requested_locale == "auto" and surface == "th":
        detected, confidence, reason = "th", max(confidence, 0.55), "surface_detector_thai_script"
    elif direction == "thai_intended_english_active" and not (detected == "en" and confidence >= 0.84):
        detected, confidence, reason = "th", 0.99, "keyboard_guard_thai_intended"
    elif direction == "english_intended_thai_active" and not _has_natural_thai_signal(text):
        detected, confidence, reason = "en", 0.99, "keyboard_guard_english_intended"

    history_language = _history_language(recent_history)
    if requested_locale in {"th", "en"}:
        effective = requested_locale
        reason = f"toggle_override_{requested_locale};{reason}"
        confidence = 1.0
    elif _is_short_followup(text) and history_language:
        effective = history_language
        reason = f"session_followup_{history_language};{reason}"
        confidence = max(confidence, 0.94)
    elif detected == "th":
        effective = "th"
    elif detected == "en":
        effective = "en"
    elif detected == "mixed":
        if reason == "mixed_english_function_words":
            effective = "en"
        elif reason == "mixed_thai_function_words":
            effective = "th"
        else:
            effective = history_language or "th"
            reason = f"{reason};{'session' if history_language else 'default'}_{effective}"
    else:
        effective = history_language or "th"
        reason = f"{reason};{'session' if history_language else 'default'}_{effective}"

    if effective == "en" and not bilingual_english_enabled():
        effective = "th"
        reason = f"english_feature_disabled;{reason}"

    return LocaleDecision(
        requested=requested_locale,
        detected=detected,
        effective=effective,
        confidence=round(max(0.0, min(1.0, confidence)), 4),
        reason=reason,
    )


def locale_from_mapping(value: Any) -> LocaleDecision | None:
    if isinstance(value, LocaleDecision):
        return value
    if not isinstance(value, dict):
        return None
    try:
        return LocaleDecision(
            requested=normalize_requested_locale(value.get("requested")),
            detected=str(value.get("detected") or "unknown"),
            effective=str(value.get("effective") or "th"),
            confidence=float(value.get("confidence") or 0.0),
            reason=str(value.get("reason") or "provided_locale_decision"),
        )
    except (TypeError, ValueError):
        return None


def latest_answer_language(recent_history: Any) -> str | None:
    return _history_language(recent_history)


def contains_thai_prose(text: str, *, allowed_fragments: Iterable[str] = ()) -> bool:
    clean = text or ""
    for fragment in allowed_fragments:
        clean = clean.replace(str(fragment), "")
    return bool(_THAI_RE.search(clean))
