"""Shared closed-world taxonomy for competition-rule understanding.

This module is deliberately data-only and conservative.  Runtime components
must share these identifiers instead of maintaining independent facet lists.
"""

from __future__ import annotations

import re
import unicodedata
from typing import Iterable

from app.core.normalization import THAI_DIGIT_TRANS, normalize_text


COMPETITION_GAME_IDS = ("cs2", "rov", "tekken8", "valorant")
COMPETITION_TAXONOMY_VERSION = "competition-taxonomy-v2.1-20260922"

CANONICAL_FACETS = (
    "rulebook_identity",
    "eligibility_registration",
    "registration",
    "pre_match_on_site",
    "team_size",
    "roster_composition",
    "competition_format",
    "match_configuration",
    "match_settings",
    "map_pool",
    "equipment",
    "in_match_operations",
    "pause_timeout",
    "disconnect",
    "fair_play_conduct",
    "conduct",
    "penalty",
    "penalty_matrix",
    "dispute",
    "protest_dispute",
    "schedule",
)

REVIEW_MODULES = (
    "common",
    "cs2_map_veto_and_side_selection",
    "cs2_overtime",
    "rov_break_time",
    "rov_hero_and_skin",
    "tekken8_character_and_stage",
    "valorant_agent_selection",
    "valorant_pause_taxonomy",
)

# Ordered from the most specific proposition to broader concepts.  The first
# match is used only as a query-frame hint; the evidence contract still proves
# whether a selected claim answers the requested proposition.
FACET_ALIASES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("rulebook_identity", (
        "ภาพรวมข้อกำหนด", "กติกาฉบับนี้", "กติกา ฉบับนี้", "ขอบเขต",
        "rulebook cover", "rulebook scope", "tournament identity", "event rules", "which tournament",
    )),
    ("protest_dispute", (
        "ยื่นประท้วง", "คัดค้านผล", "ข้อพิพาท", "โต้แย้งผล", "ประท้วง",
        "team protest", "raise an objection", "appeal", "protest", "dispute",
    )),
    ("pre_match_on_site", (
        "รายงานตัว", "หน้างาน", "ก่อนเริ่ม", "ก่อนแข่ง", "check-in", "check in",
        "on-site", "on site", "venue requirement", "มาถึงสนาม", "ก่อนเวลาแข่ง",
        "arrive at the venue", "minutes before a match",
    )),
    ("in_match_operations", (
        "ประสานกับกรรมการ", "แจ้งใคร", "ขั้นตอนระหว่างการแข่งขัน",
        "ขั้นตอนทำงานระหว่าง", "contact officials", "who should we notify",
        "in-match procedure", "match operations", "who should a player contact",
        "general issue during", "procedure must officials follow", "unspecified incident",
    )),
    ("roster_composition", (
        "จำนวนตัวจริง", "ตัวจริงและตัวสำรอง", "รวมสำรอง", "roster composition",
        "roster size", "starters and substitutes", "ลงทะเบียนตัวสำรอง",
        "ตัวสำรองได้กี่คน", "how many substitute players", "how many substitutes",
    )),
    ("team_size", (
        "team size", "team composition", "how many players", "players can a team have",
        "ผู้เล่นกี่คน", "จำนวนผู้เล่น", "ทีมละ", "5v5", "how many starting players",
        "starting players", "players must a team field",
    )),
    ("map_pool", (
        "map pool", "map veto", "map selection", "maps, vetoes", "maps are used",
        "maps picked", "maps banned", "เลือกแผนที่", "แบนแผนที่", "ใช้แผนที่",
    )),
    ("match_configuration", (
        "match configuration", "room setup", "กำหนดค่าแมตช์", "ตั้งค่าห้องแข่ง",
        "เวอร์ชันเกมและการตั้งค่าแมตช์",
    )),
    ("match_settings", (
        "match settings", "in-game settings", "default settings", "ตั้งค่าในเกม",
        "ค่าตั้งต้นของแมตช์", "รายละเอียดการตั้งค่า",
    )),
    ("penalty_matrix", (
        "ตารางบทลงโทษ", "รายการบทลงโทษ", "penalty matrix", "penalty table",
        "penalties listed",
    )),
    ("penalty", (
        "บทลงโทษ", "โดนโทษ", "ปรับแพ้", "ตัดสิทธิ์", "penalty", "violation",
        "penalties", "rule is broken", "forfeit",
    )),
    ("disconnect", (
        "หลุดเกม", "เน็ตหลุด", "การเชื่อมต่อ", "connection loss", "disconnect",
        "reconnect", "rematch", "restart",
    )),
    ("pause_timeout", (
        "technical pause", "emergency pause", "timeout", "pause", "หยุดเกม",
        "พักเกม", "เวลานอก",
    )),
    ("equipment", (
        "อุปกรณ์ที่ใช้แข่งขัน", "อุปกรณ์ของตัวเอง", "equipment rules", "own equipment",
        "which devices", "provided computers", "competition equipment", "equipment and devices",
    )),
    ("eligibility_registration", (
        "คุณสมบัติและการลงทะเบียน", "eligibility and registration",
        "อายุขั้นต่ำ", "คุณสมบัติผู้สมัคร", "minimum age", "age requirement",
    )),
    ("registration", (
        "สมัครเข้าร่วม", "ลงทะเบียน", "ส่งชื่อเข้ารายการ", "register", "registration",
        "submit an entry", "ปิดรับรายชื่อ", "กำหนดส่งรายชื่อ", "registration deadline",
        "roster registration deadline", "roster submission deadline",
    )),
    ("fair_play_conduct", (
        "fair-play", "fair play", "น้ำใจนักกีฬา", "sportsmanship",
    )),
    ("conduct", (
        "การวางตัว", "มารยาท", "ความประพฤติ", "พฤติกรรม", "พูดหยาบ", "คำหยาบ",
        "conduct", "behavior", "behaviour", "profanity", "inappropriate conduct", "toxic",
    )),
    ("competition_format", (
        "รูปแบบการแข่งขัน", "competition format", "single elimination", "bracket", "best of", "bo3", "bo5",
        "แพ้คัดออก",
    )),
    ("schedule", (
        "กำหนดการแข่งขัน", "ตารางการแข่งขัน", "ตารางและเวลาแข่งขัน", "แข่งวันไหน",
        "event schedule", "competition schedule", "tournament schedule",
    )),
)

# This is a small, reviewed correction set for target matching. It does not
# rewrite the user query and is not used by general NLP or answer rendering.
SAFE_TARGET_VARIANT_REPLACEMENTS = (
    ("เทคเล่น 8", "เทคเค่น 8"),
    ("เทคเล่น8", "เทคเค่น8"),
)


def conservative_text(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", str(value or ""))
    normalized = normalized.translate(THAI_DIGIT_TRANS).casefold().strip()
    return re.sub(r"\s+", " ", normalized)


def competition_search_variants(value: str, *, limit: int = 5) -> tuple[str, ...]:
    """Return bounded target-matching variants without altering display text."""
    raw = conservative_text(value)
    if not raw:
        return ()
    candidates = [raw]
    normalized = normalize_text(value)
    if normalized:
        candidates.append(conservative_text(normalized))
    for old, new in SAFE_TARGET_VARIANT_REPLACEMENTS:
        if old in raw:
            candidates.append(raw.replace(old, new))
    result: list[str] = []
    seen: set[str] = set()
    for candidate in candidates:
        clean = conservative_text(candidate)
        if clean and clean not in seen:
            seen.add(clean)
            result.append(clean)
        if len(result) >= limit:
            break
    return tuple(result)


def canonical_facet(value: str | None) -> str | None:
    facet = str(value or "").strip()
    if facet in CANONICAL_FACETS:
        return facet
    legacy = {
        "eligibility": "eligibility_registration",
        "format": "competition_format",
        "game_setting": "match_settings",
        "pause": "pause_timeout",
        "fair_play": "fair_play_conduct",
        "protest": "protest_dispute",
    }
    return legacy.get(facet)


def detect_competition_facet(query: str) -> str | None:
    variants = competition_search_variants(query)
    # "pause penalty" asks about the consequence/handling of a pause, not a
    # generic tournament penalty table.  Preserve that narrower operational
    # target before the ordered alias scan reaches ``penalty``.
    if any(
        _contains_phrase(variant, pause_term)
        for variant in variants
        for pause_term in ("pause", "timeout", "technical pause", "หยุดเกม", "พักเกม")
    ):
        return "pause_timeout"
    # When a user asks for the penalty caused by misconduct, the proposition
    # still requires a conduct clause. A generic penalty table for exploits
    # cannot establish that profanity or unsportsmanlike behavior is an
    # offense in this rulebook.
    conduct_aliases = dict(FACET_ALIASES)["conduct"]
    fair_play_aliases = dict(FACET_ALIASES)["fair_play_conduct"]
    if any(_contains_phrase(variant, alias) for variant in variants for alias in fair_play_aliases):
        return "fair_play_conduct"
    if any(_contains_phrase(variant, alias) for variant in variants for alias in conduct_aliases):
        return "conduct"
    for facet, aliases in FACET_ALIASES:
        if any(_contains_phrase(variant, alias) for variant in variants for alias in aliases):
            return facet
    return None


def _contains_phrase(haystack: str, needle: str) -> bool:
    candidate = conservative_text(needle)
    if not candidate:
        return False
    if candidate.isascii() and len(candidate) <= 4:
        return bool(re.search(rf"(?<![a-z0-9]){re.escape(candidate)}(?![a-z0-9])", haystack))
    return candidate in haystack or candidate.replace(" ", "") in haystack.replace(" ", "")


def validate_taxonomy_values(values: Iterable[str]) -> tuple[str, ...]:
    allowed = set(CANONICAL_FACETS)
    return tuple(sorted({str(value) for value in values if str(value) not in allowed}))
