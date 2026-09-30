"""Closed-world target resolution for the supported competition rulebooks."""

from __future__ import annotations

import re
from dataclasses import dataclass

from app.pipeline.competition_taxonomy import (
    FACET_ALIASES,
    competition_search_variants,
    detect_competition_facet,
)


@dataclass(frozen=True)
class CompetitionTarget:
    game_id: str
    label: str
    rulebook_id: str
    aliases: tuple[str, ...]


@dataclass(frozen=True)
class CompetitionTargetResolution:
    status: str  # exact | multiple | unknown_explicit | absent
    targets: tuple[CompetitionTarget, ...] = ()
    explicit_mentions: tuple[str, ...] = ()
    reason: str = ""


_TARGETS = (
    CompetitionTarget(
        "cs2",
        "Counter-Strike 2",
        "competition_rules_cs2_psu_phuket_2026",
        ("cs2", "counter-strike 2", "counter strike 2", "เคาน์เตอร์สไตรก์ 2", "เคาเตอร์สไตรก์ 2"),
    ),
    CompetitionTarget(
        "rov",
        "Arena of Valor (RoV)",
        "competition_rules_rov_blueket_2025_men",
        ("rov", "aov", "arena of valor", "อารีน่าออฟเวเลอร์", "อารีน่า ออฟ เวเลอร์", "อาโอวี"),
    ),
    CompetitionTarget(
        "tekken8",
        "Tekken 8",
        "competition_rules_tekken8_psu_esports",
        ("tekken 8", "tekken8", "เทคเคน 8", "เทคเคน8", "เทคเค่น 8", "เทคเค่น8", "t8"),
    ),
    CompetitionTarget(
        "valorant",
        "VALORANT",
        "competition_rules_valorant_psu_phuket_2026",
        ("valorant", "valo", "วาโล", "วาโลแรนต์"),
    ),
)

_UNSUPPORTED_GAME_ALIASES = (
    "free fire", "freefire", "dota 2", "dota2", "mobile legends", "mlbb",
    "pubg mobile", "honor of kings", "hok",
)

_RULE_SIGNALS = (
    "rulebook", "กติกา", "ระเบียบ", "การแข่งขัน", "แข่งขัน", "แข่ง",
    "competition", "tournament", "bracket", "best of", "bo3", "bo5",
    "roster", "substitute", "forfeit", "anti-cheat", "cheating", "conduct",
    "sportsmanship", "technical pause", "timeout", "pause", "disconnect",
    "มารยาท", "พฤติกรรม", "ตัวสำรอง", "ปรับแพ้", "ประท้วง", "ข้อพิพาท",
    "หลุดเกม", "การเชื่อมต่อ", "การหยุดเกม", "พักเกม", "โกง",
)

# These phrases are not sufficient on their own: a question about a game can
# mention a team or equipment without asking about a tournament.  Together
# with one registered competition-game alias, however, they reliably express
# a rulebook facet and should enter target-grounded competition retrieval.
_RULE_CONTEXT_SIGNALS = (
    "ข้อกำหนด", "ข้อห้าม", "องค์ประกอบทีม", "จำนวนผู้เล่น", "ทีมละ", "ผู้เล่นกี่คน",
    "การสมัคร", "ลงทะเบียน", "รายงานตัว", "พื้นที่แข่งขัน", "อุปกรณ์ที่ใช้แข่งขัน",
    "ตั้งค่าในเกม", "ขั้นตอนระหว่างการแข่งขัน", "ขอบเขต", "ข้อมูลของรายการ",
    "ตารางบทลงโทษ", "แก้ปัญหาข้อพิพาท", "fair play", "match settings",
    "team composition", "team size", "roster composition", "check-in", "on-site",
    "equipment used", "registration requirements", "tournament details",
    # Natural participant wording.  These phrases only activate when the
    # question already names one of the four registered competition games;
    # they therefore do not turn an ordinary game catalogue request into a
    # competition-rule query.
    "การวางตัว", "คุณสมบัติ", "อุปกรณ์หรือการตั้งค่า", "น้ำใจนักกีฬา",
    "ประสานกับกรรมการ", "ใช้แผนที่", "map pool", "ค่าตั้งต้นของแมตช์",
    "เลือกแผนที่", "แบนแผนที่", "เลือกและแบนแผนที่", "map veto", "map selection",
    "มี setting", "โทษระดับไหน", "ผิดกฎ", "โดนโทษ", "คัดค้านผล",
    "ส่งชื่อเข้ารายการ", "รายชื่อทีม", "รวมสำรอง", "ตารางหรือกำหนดการ",
    "กติกา ฉบับนี้", "ก่อนเริ่ม", "หน้างาน", "ระหว่างแมตช์",
    "รายละเอียดการตั้งค่า", "สมัครเข้าร่วม", "ผู้เล่นหลุด", "เกมมีปัญหากลางคัน",
    "setting ที่ผู้เล่น", "setting that players", "settings players must",
    "how many games", "single elimination", "behaviour", "behavior",
    "sportsmanship", "fair-play", "dispute", "disagreement", "conflict",
    "eligible", "eligibility", "register", "registration", "submit an entry",
    "own equipment", "which devices", "equipment rules", "in-match procedure",
    "contact officials", "maps are used", "maps picked", "maps banned", "map pool",
    "match configured", "match configuration", "room setup", "in-game settings",
    "default match settings", "rule is broken", "penalties", "penalty table",
    "check in", "on site", "check-in time", "event schedule", "when is",
    "roster size", "starters and substitutes", "players must", "rulebook cover",
    "event rules", "which tournament", "stop mid-game", "connection loss",
    "should we notify", "match be configured", "settings must be configured",
    "team protest", "raise an objection", "challenging a", "submit a", "entry",
    # English rulebook facets that are precise only when a registered
    # competition-game target is present. Keeping them in this target-bound
    # list prevents ordinary studio questions from being reclassified.
    "overtime", "starting money", "game breaking bug", "exploit adjudication",
    "competition venue", "food and drinks", "chewing gum", "install software",
    "own software", "provided computers", "emergency pause", "round rollback",
    "อายุขั้นต่ำ", "คุณสมบัติผู้สมัคร", "minimum age", "age requirement",
    "ปิดรับรายชื่อ", "กำหนดส่งรายชื่อ", "registration deadline", "roster submission deadline",
)

_FACETS = FACET_ALIASES


def _contains_alias(query: str, alias: str) -> bool:
    query_variants = competition_search_variants(query)
    alias_variants = competition_search_variants(alias)
    for normalized_query in query_variants:
        for normalized_alias in alias_variants:
            if not normalized_alias:
                continue
            if normalized_alias.isascii() and len(normalized_alias) <= 4:
                if re.search(rf"(?<![a-z0-9]){re.escape(normalized_alias)}(?![a-z0-9])", normalized_query):
                    return True
            elif (
                normalized_alias in normalized_query
                or normalized_alias.replace(" ", "") in normalized_query.replace(" ", "")
            ):
                return True
    return False


def resolve_competition_targets(query: str) -> CompetitionTargetResolution:
    # Import lazily to keep the taxonomy usable by low-level tooling without
    # creating an execution-context import cycle.
    from app.pipeline.execution_context import current_execution_context

    context = current_execution_context()
    if context is not None:
        cached = context.get_competition_resolution(query)
        if cached is not None:
            return cached
    result = _resolve_competition_targets_uncached(query)
    if context is not None:
        context.store_competition_resolution(query, result)
    return result


def _resolve_competition_targets_uncached(query: str) -> CompetitionTargetResolution:
    matched: list[tuple[int, CompetitionTarget, str]] = []
    for target in _TARGETS:
        aliases = [(query.casefold().find(alias.casefold()), alias) for alias in target.aliases if _contains_alias(query, alias)]
        if aliases:
            position, alias = min(aliases, key=lambda value: value[0] if value[0] >= 0 else 10**9)
            matched.append((position if position >= 0 else 10**9, target, alias))
    matched.sort(key=lambda value: value[0])
    targets = tuple(item[1] for item in matched)
    mentions = tuple(item[2] for item in matched)
    if len(targets) == 1:
        return CompetitionTargetResolution("exact", targets, mentions, "registered_competition_alias")
    if len(targets) > 1:
        return CompetitionTargetResolution("multiple", targets, mentions, "multiple_registered_competition_aliases")
    unsupported = tuple(alias for alias in _UNSUPPORTED_GAME_ALIASES if _contains_alias(query, alias))
    if unsupported:
        return CompetitionTargetResolution("unknown_explicit", (), unsupported, "unsupported_explicit_game_alias")
    return CompetitionTargetResolution("absent", (), (), "no_competition_game_alias")


def looks_like_competition_rule_query(query: str) -> bool:
    target = resolve_competition_targets(query)
    has_rule_signal = any(_contains_alias(query, signal) for signal in _RULE_SIGNALS)
    has_context_signal = any(_contains_alias(query, signal) for signal in _RULE_CONTEXT_SIGNALS)
    if target.status in {"exact", "multiple", "unknown_explicit"}:
        return has_rule_signal or has_context_signal
    # Generic words such as timeout, check-in, equipment, or payment also
    # occur in studio booking policies. Without a game target they must not
    # open the competition rulebook. Only explicit competition vocabulary may
    # request target clarification.
    strong_unbound_signals = (
        "rulebook", "competition rules", "tournament rules", "competition",
        "tournament", "กติกาการแข่งขัน", "กฎการแข่งขัน", "การแข่งขัน",
        "แข่งขัน", "ทัวร์นาเมนต์",
    )
    return any(_contains_alias(query, signal) for signal in strong_unbound_signals)


def competition_facet(query: str) -> str | None:
    return detect_competition_facet(query)


def target_for_game_id(game_id: str) -> CompetitionTarget | None:
    return next((target for target in _TARGETS if target.game_id == game_id), None)
