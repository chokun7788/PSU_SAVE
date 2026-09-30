from __future__ import annotations

import re

from app.core.normalization import normalize_text
from app.core.typo_similarity import osa_distance


_POLITE = r"(?:ครับ|คับ|ค่ะ|คะ)?"
_SOCIAL_PATTERNS = (
    ("social_thanks", re.compile(rf"(?:ขอบคุ[ณน]+|ขอบใจ+|แต๊งกิ้ว|แต้งกิ้ว)(?:\s*มาก+)?{_POLITE}")),
    ("social_apology", re.compile(rf"ขอโท[ษด]+{_POLITE}")),
    ("social_ack", re.compile(rf"(?:โอเค+|เค+|รับทราบ|ได้เลย){_POLITE}")),
    ("social_farewell", re.compile(rf"(?:บาย+|บ๊ายบาย+|ฝันดี|ไปก่อนนะ|เจอกัน){_POLITE}")),
)

_ANSWERS = {
    "social_thanks": ("ยินดีครับ ถ้ามีคำถามเกี่ยวกับศูนย์ ถามต่อได้เลยครับ", "You're welcome. Feel free to ask another question about the studio."),
    "social_apology": ("ไม่เป็นไรครับ ถามต่อได้เลยครับ", "No problem. Feel free to continue."),
    "social_ack": ("ได้ครับ ถ้ามีคำถามเพิ่มเติม ถามได้เลยครับ", "Okay. Feel free to ask another question."),
    "social_farewell": ("แล้วพบกันครับ", "See you again."),
}

_SOCIAL_PROTOTYPES = {
    "social_thanks": ("ขอบคุณ", "ขอบคุณครับ", "ขอบคุณคับ", "ขอบคุณค่ะ", "แต๊งกิ้ว", "แต้งกิ้ว"),
    "social_apology": ("ขอโทษ", "ขอโทษครับ", "ขอโทษค่ะ"),
    "social_ack": ("โอเค", "รับทราบ", "ได้เลย"),
    "social_farewell": ("บาย", "บ๊ายบาย", "ฝันดี", "เจอกัน"),
}


def social_dialogue_reply(value: str, *, locale: str = "th") -> tuple[str, str] | None:
    """Answer only a complete, short social utterance; never consume a task question."""
    query = normalize_text(value).strip(" !?.ฯ")
    query = re.sub(r"([ก-ฮ])\1+$", r"\1", query)
    if not query or len(query) > 40 or not re.fullmatch(r"[\u0E00-\u0E7F ]+", query):
        return None
    for intent, pattern in _SOCIAL_PATTERNS:
        if pattern.fullmatch(query):
            answers = _ANSWERS[intent]
            return intent, answers[1] if locale == "en" else answers[0]
    # A complete short utterance may contain two local errors. Collapse obvious
    # repeated consonants for comparison only, then require a clear winner.
    if len(query) <= 18 and not any(term in query for term in ("เกม", "ราคา", "จอง", "เวลา", "อุปกรณ์", "ศูนย์")):
        compact = re.sub(r"\s+", "", query)
        candidates = (compact, re.sub(r"([ก-ฮ])\1+", r"\1", compact))
        ranked = sorted(
            (
                min(
                    (osa_distance(candidate, prototype) for candidate in candidates for prototype in prototypes
                     if candidate and candidate[0] == prototype[0]),
                    default=99,
                ),
                intent,
            )
            for intent, prototypes in _SOCIAL_PROTOTYPES.items()
        )
        distance, intent = ranked[0]
        limit = 1 if len(compact) <= 4 else 2
        if intent == "social_apology" and compact.startswith("ขอโท"):
            limit = 3
        if distance <= limit and ranked[1][0] - distance >= 2:
            answers = _ANSWERS[intent]
            return intent, answers[1] if locale == "en" else answers[0]
    return None
