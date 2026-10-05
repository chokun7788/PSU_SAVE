"""Bounded whole-phrase candidates for repeated errors in common Thai requests.

Candidates are ordinary verified request forms, not answers or facility facts.
Resource names and numbers are kept verbatim; uncertain matches are ignored.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from app.core.typo_similarity import osa_distance


_DAYS = ("จันทร์", "อังคาร", "พุธ", "พฤหัส", "ศุกร์", "เสาร์", "อาทิตย์")
_SERVICE_PREFIX = re.compile(
    r"^\s*(?P<resource>pc(?:\s*#\s*\d{1,2}|\d{1,2})?|"
    r"ps5(?:\s*#\s*\d{1,2})?|vr(?:\s*#\s*\d{1,2}|\d{1,2})?|"
    r"nintendo(?:\s+switch)?|cockpit(?:\s*#\s*\d{1,2}|\d{1,2})?|เพลย์ห้า|เพลย์5|"
    r"คอม|พีซี|วีอาร์|คอกพิท|ค็อกพิท)\s*(?P<request>.+)$",
    re.IGNORECASE,
)
_DURATION_PREFIX = re.compile(r"^(?P<duration>\d{1,3}\s*(?:นาที|ชั่วโมง))\s*(?P<request>.+)$")
_SIMPLE_REQUESTS = (
    ("เปิดกี่โมง", 2, "schedule"),
    ("ปิดกี่โมง", 2, "schedule"),
    *((f"วัน{day}เปิดกี่โมง", 2, "schedule") for day in _DAYS),
    *((f"วัน{day}ปิดกี่โมง", 2, "schedule") for day in _DAYS),
    ("มีเกมอะไรบ้าง", 2, "games"),
    ("มีไรเล่นมั่ง", 2, "games"),
    ("มีเกมแข่งรถมั้ย", 3, "games"),
    ("มีอุปกรณ์อะไรบ้าง", 4, "equipment"),
    ("มีหูฟังไหม", 2, "equipment"),
    ("ติดต่อทางไหน", 2, "contact"),
)
_PRICE_REQUESTS = (
    ("ราคาเท่าไหร่", 2),
    ("คิดตังเท่าไหรอะ", 3),
    ("ค่าบริการเท่าไหร่", 2),
)


@dataclass(frozen=True)
class MultiErrorPhraseRecovery:
    original: str
    candidate: str
    distance: int
    category: str


def _compact(value: str) -> str:
    return re.sub(r"\s+", "", value.lower())


def _accept_simple(observed: str, category: str) -> bool:
    if category == "schedule":
        return "โม" in observed and not any(term in observed for term in ("กี่วัน", "กี่เดือน"))
    if category == "games":
        if observed.startswith("มีเกมแข่ง"):
            return "มั้ย" in observed and "กติกา" not in observed
        if "เล่น" in observed:
            return observed.startswith("มี") and "มั่ง" in observed
        return observed.startswith("มี") and "บ้าง" in observed and "เมนู" not in observed
    if category == "equipment":
        return (observed.startswith("มีอุป") and "บ้าง" in observed) or (
            observed.startswith("มีหู") and "ไหม" in observed
        )
    if category == "contact":
        return observed.startswith("ติดต่") and not any(term in observed for term in ("โทร", "เฟส", "อีเมล", "ไลน์"))
    return False


def detect_multi_error_phrase_recovery(value: str) -> MultiErrorPhraseRecovery | None:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    if not text or len(text) > 70 or re.search(r"https?://|\d{1,2}:\d{2}|\d{4}-\d{2}-\d{2}", text, re.I):
        return None
    observed = _compact(text)
    candidates: list[MultiErrorPhraseRecovery] = []
    if re.fullmatch(r"[\u0e00-\u0e7f]+", observed):
        if any(observed == _compact(expected) for expected, _, _ in _SIMPLE_REQUESTS):
            return None
        for expected, maximum, category in _SIMPLE_REQUESTS:
            if not _accept_simple(observed, category):
                continue
            distance = osa_distance(observed, _compact(expected))
            if 0 < distance <= maximum:
                candidates.append(MultiErrorPhraseRecovery(text, expected, distance, category))
    service = _SERVICE_PREFIX.fullmatch(text)
    if service is not None:
        resource = service.group("resource").strip()
        request_text = service.group("request").strip()
        duration_match = _DURATION_PREFIX.fullmatch(request_text)
        duration = duration_match.group("duration").strip() if duration_match else ""
        if duration_match:
            request_text = duration_match.group("request").strip()
        request = _compact(request_text)
        if "เท่า" in request:
            for expected, maximum in _PRICE_REQUESTS:
                if expected.startswith("คิดตัง") and osa_distance(request[:4], "คิดต") > 1:
                    continue
                distance = osa_distance(request, _compact(expected))
                if 0 < distance <= maximum:
                    candidates.append(MultiErrorPhraseRecovery(
                        text, " ".join(part for part in (resource, duration, expected) if part), distance, "service_fee"
                    ))
    if not candidates:
        return None
    candidates.sort(key=lambda item: (item.distance, item.category, item.candidate))
    best = candidates[0]
    if len(candidates) > 1 and candidates[1].distance - best.distance < 2:
        return None
    return best


def recover_multi_error_phrase_query(value: str) -> str:
    recovery = detect_multi_error_phrase_recovery(value)
    return recovery.candidate if recovery is not None else value
