from __future__ import annotations

import os
import re
from functools import lru_cache


SAFE_CORRECTION_TARGETS = {
    "ไหม",
    "มั้ย",
    "รายการ",
    "แข่ง",
    "แข่งขัน",
    "เกม",
    "จอง",
    "ขั้น",
    "ขั้นที่",
    "อาหาร",
    "ขนม",
    "เครื่องดื่ม",
    "นักศึกษา",
    "นักเรียน",
    "บัตร",
    "ราคา",
    "ค่าบริการ",
    "ค่าใช้จ่าย",
    "จันทร์",
    "วันจันทร์",
    "อังคาร",
    "พุธ",
    "พฤหัส",
    "ศุกร์",
    "เสาร์",
    "อาทิตย์",
    "ชั่วโมง",
    "นาที",
    "อุปกรณ์",
    "กติกา",
    "กฎ",
    "รางวัล",
}


PROTECTED_TERMS = {
    "rov",
    "aov",
    "valorant",
    "valo",
    "cs2",
    "counter-strike",
    "counter",
    "strike",
    "tekken",
    "ps5",
    "playstation",
    "nintendo",
    "switch",
    "vr",
    "pc",
    "pubg",
    "warzone",
    "fortnite",
    "minecraft",
    "roblox",
    "beat",
    "saber",
    "horizon",
    "gran",
    "turismo",
    "mario",
    "psu",
    "esports",
    "studio",
    "phuket",
}


def _enabled() -> bool:
    return os.getenv("PSU_ENABLE_PYTHAINLP", "0").strip().lower() in {"1", "true", "yes", "y", "on"}


@lru_cache(maxsize=1)
def _load_pythainlp():
    if not _enabled():
        return None, None
    try:
        from pythainlp.spell import correct
        from pythainlp.tokenize import word_tokenize
    except Exception:
        return None, None
    return correct, word_tokenize


def pythainlp_available() -> bool:
    correct, word_tokenize = _load_pythainlp()
    return correct is not None and word_tokenize is not None


def _is_protected_token(token: str) -> bool:
    lowered = token.lower()
    if re.search(r"[a-z0-9]", lowered):
        return True
    return any(term in lowered for term in PROTECTED_TERMS)


def _safe_to_correct(token: str, corrected: str) -> bool:
    if not token or not corrected or token == corrected:
        return False
    if len(token) <= 1:
        return False
    if _is_protected_token(token) or _is_protected_token(corrected):
        return False
    if corrected not in SAFE_CORRECTION_TARGETS:
        return False
    if abs(len(corrected) - len(token)) > 4:
        return False
    return True


@lru_cache(maxsize=8192)
def safe_thai_spell_normalize(text: str) -> str:
    correct, word_tokenize = _load_pythainlp()
    if correct is None or word_tokenize is None:
        return text

    try:
        tokens = word_tokenize(text, engine="newmm", keep_whitespace=True)
    except Exception:
        return text

    changed = False
    normalized: list[str] = []
    for token in tokens:
        if not token.strip() or not re.search(r"[\u0E00-\u0E7F]", token):
            normalized.append(token)
            continue
        try:
            corrected = correct(token)
        except Exception:
            normalized.append(token)
            continue
        if _safe_to_correct(token, corrected):
            normalized.append(corrected)
            changed = True
        else:
            normalized.append(token)

    return "".join(normalized) if changed else text
