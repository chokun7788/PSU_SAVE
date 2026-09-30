from __future__ import annotations

from difflib import SequenceMatcher

from app.core.normalization import normalize_text


_IDENTITY_TERMS = (
    "นายเป็นใคร", "คุณเป็นใคร", "แกเป็นใคร", "เธอเป็นใคร", "ตัวเองเป็นใคร",
    "เป็น ai อะไร", "เป็น ai จริงหรือเปล่า", "เป็น ai ไหม",
    "เป็นคนแอบพิมพ์", "คนแอบพิมพ์",
    "เป็น model อะไร", "เป็นโมเดลอะไร", "ชื่ออะไร",
    "ทำอะไรได้บ้าง", "ทำไรได้บ้าง", "ช่วยอะไรได้บ้าง", "ช่วยไรได้บ้าง",
    "ตอบอะไรได้บ้าง", "ตอบไรได้บ้าง", "ถามอะไรได้บ้าง", "ถามไรได้บ้าง",
    "แชทบอทนี้", "chatbot นี้", "bot นี้", "บอทนี้", "assistant นี้",
    "who are you", "who r u", "what are you",
    "what can you do", "what can u do", "what u can do",
)

_THAI_IDENTITY_TERMS = (
    "นายเป็นใคร", "คุณเป็นใคร", "แกเป็นใคร", "เธอเป็นใคร", "ตัวเองเป็นใคร",
    "นายทำอะไรได้บ้าง", "คุณทำอะไรได้บ้าง", "บอทนี้ทำอะไรได้บ้าง",
)


def is_chatbot_identity_query(value: str) -> bool:
    """Recognize the small, closed chatbot identity/capability intent safely.

    The fuzzy fallback is deliberately subject-gated and short-query-only. It is
    not a general spelling corrector, so ordinary user questions cannot be
    routed to the chatbot identity answer by broad similarity matching.
    """
    query = normalize_text(value).strip()
    if not query:
        return False
    if any(term in query for term in _IDENTITY_TERMS):
        return True
    if len(query) > 18 or not any(subject in query for subject in ("นาย", "คุณ", "แก", "เธอ", "บอท", "เอไอ")):
        return False
    return max(SequenceMatcher(None, query, term).ratio() for term in _THAI_IDENTITY_TERMS) >= 0.76
