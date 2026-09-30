from __future__ import annotations

from difflib import SequenceMatcher
import re

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


def _within_one_edit(value: str, expected: str) -> bool:
    """Allow one inserted, missing, or substituted code point in a short greeting."""
    if abs(len(value) - len(expected)) > 1:
        return False
    if len(value) == len(expected):
        return sum(left != right for left, right in zip(value, expected)) == 1
    shorter, longer = sorted((value, expected), key=len)
    offset = 0
    for index, character in enumerate(shorter):
        if character == longer[index + offset]:
            continue
        if offset:
            return False
        offset = 1
        if character != longer[index + offset]:
            return False
    return True


def is_chatbot_greeting_query(value: str) -> bool:
    query = normalize_text(value).strip()
    if not query or len(query) > 40:
        return False
    thai = re.sub(r"([ก-ฮ])\1+", r"\1", query).strip(" !?.ฯ")
    if re.fullmatch(r"(?:สวัสดี|หวัดดี|ฮัลโหล)(?:ครับ|ค่ะ|คับ|คะ)?|ดี(?:ครับ|ค่ะ|คับ)|ทัก(?:ครับ|ค่ะ)", thai):
        return True
    # Only recover a stand-alone Thai greeting. Never fuzzily consume a
    # following booking, price, time, or equipment question.
    if re.fullmatch(r"[ก-๙]+", thai):
        stem = thai
        for suffix in ("ครับ", "ค่ะ", "คับ", "คะ"):
            if stem.endswith(suffix):
                stem = stem[:-len(suffix)]
                break
        if any(_within_one_edit(stem, greeting) for greeting in ("สวัสดี", "หวัดดี", "ฮัลโหล")):
            return True
    return bool(re.fullmatch(r"(?:hello|hi|hey)(?:\s+there)?[!?.]*", query))


def is_chatbot_identity_query(value: str) -> bool:
    """Recognize the small, closed chatbot identity/capability intent safely.

    The fuzzy fallback is deliberately subject-gated and short-query-only. It is
    not a general spelling corrector, so ordinary user questions cannot be
    routed to the chatbot identity answer by broad similarity matching.
    """
    query = normalize_text(value).strip()
    if not query:
        return False
    # Compose subject and predicate signals instead of listing every chatty
    # spelling. A real staff/person target vetoes this closed chatbot intent.
    if len(query) <= 96 and not re.search(r"\b(?:manager|director|staff|developer|president|rector)\b|ผู้จัดการ|ผู้อำนวยการ|บุคลากร|ผู้พัฒนา", query):
        en_identity = bool(re.search(
            r"\b(?:who|what|wat)\s+(?:(?:are|r|is)\s+(?:you|u|this\s+(?:bot|assistant|chatbot))"
            r"|(?:can|could)\s+(?:you|u)\s+do|do\s+(?:you|u)\s+do)\b"
            r"|\b(?:is|are)\s+this\s+(?:a\s+)?(?:bot|assistant|chatbot)\s+or\s+(?:a\s+)?person\b"
            r"|\b(?:who|what|wat)\s+(?:bot|assistant|chat\s+assistant)\s+is\s+this\b"
            r"|\btell\s+me\s+who\s+(?:you|u)\s+(?:are|r)\b"
            r"|\bwhat\s+is\s+this\s+(?:chat\s+)?(?:bot|assistant|chatbot)\s+called\b",
            query,
        ))
        en_answering = bool(re.search(r"\bwho\s+is\s+answering\s+me\b", query))
        th_subject = any(token in query for token in ("นาย", "คุณ", "คุน", "บอท", "ผู้ช่วย", "คนตอบ", "ตอบอยู่"))
        th_predicate = any(token in query for token in ("ใคร", "ไคร", "เปน", "เป็น", "หน้าที่", "ชื่อ", "คนหรือบอท", "ตอบอยู่"))
        if en_identity or en_answering or (th_subject and th_predicate):
            return True
    if any(term in query for term in _IDENTITY_TERMS):
        return True
    if len(query) > 18 or not any(subject in query for subject in ("นาย", "คุณ", "แก", "เธอ", "บอท", "เอไอ")):
        return False
    return max(SequenceMatcher(None, query, term).ratio() for term in _THAI_IDENTITY_TERMS) >= 0.76
