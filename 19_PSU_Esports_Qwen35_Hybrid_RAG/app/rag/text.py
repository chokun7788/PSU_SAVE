from __future__ import annotations

import re
from collections import Counter


THAI_DIGIT_TRANS = str.maketrans("๐๑๒๓๔๕๖๗๘๙", "0123456789")

STOPWORDS = {
    "คือ",
    "อะไร",
    "ไหม",
    "มั้ย",
    "ครับ",
    "ค่ะ",
    "คะ",
    "หน่อย",
    "ได้",
    "หรือ",
    "และ",
    "ของ",
    "ใน",
    "ที่",
    "the",
    "is",
    "are",
    "can",
    "do",
    "does",
    "what",
    "how",
}


def normalize_text(text: str) -> str:
    value = (text or "").lower().strip().translate(THAI_DIGIT_TRANS)
    replacements = {
        "ม.อ.": "มอ",
        "ม.อ": "มอ",
        "ม. อ.": "มอ",
        "p.s.u.": "psu",
        "p s u": "psu",
        "check-in": "checkin",
        "check in": "checkin",
        "ช.ม.": "ชม",
        "ชม.": "ชม",
        "น.ท.": "นาที",
        "เพลย์ห้า": "playstation 5",
        "เพลย์ 5": "playstation 5",
        "พีซี": "pc",
        "วีอาร์": "vr",
        "วาโล": "valorant",
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    return re.sub(r"\s+", " ", value)


def tokenize(text: str) -> list[str]:
    q = normalize_text(text)
    tokens = [tok for tok in re.split(r"[\s,./|()\[\]{}:;!?\"'<>]+", q) if len(tok) >= 2]
    expanded: list[str] = [tok for tok in tokens if tok not in STOPWORDS]

    # Thai text often has no whitespace. Character n-grams improve recall for fuzzy Thai wording.
    thai_spans = re.findall(r"[\u0E00-\u0E7F]{3,}", q)
    for span in thai_spans:
        if len(span) > 70:
            continue
        for size in (2, 3, 4):
            for index in range(0, len(span) - size + 1):
                gram = span[index : index + size]
                if gram not in STOPWORDS:
                    expanded.append(gram)
    return expanded


def token_counts(text: str) -> dict[str, int]:
    return dict(Counter(tokenize(text)))


def compact_text(text: str, limit: int = 900) -> str:
    value = " ".join((text or "").split())
    if len(value) <= limit:
        return value
    return value[:limit].rstrip() + "..."
