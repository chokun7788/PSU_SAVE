"""Conservative multi-facet classification for competition source chunks.

The legacy canonical migration assigns one facet to each source chunk.  That
is too lossy for headings that contain several rules and too brittle for
sentences such as "two pauses per team", where the word ``team`` does not
make the clause a team-size rule.  Runtime retrieval and the evaluation Gold
contract use this module so they agree on what a source passage can prove.
"""

from __future__ import annotations

from typing import Any

from app.core.normalization import normalize_text
from app.pipeline.competition_taxonomy import canonical_facet


CANONICAL_TO_SOURCE_FACETS: dict[str, tuple[str, ...]] = {
    "rulebook_identity": ("rulebook_identity",),
    "eligibility_registration": ("eligibility_registration",),
    "registration": ("registration",),
    "pre_match_on_site": ("pre_match_on_site",),
    "team_size": ("team_size",),
    "roster_composition": ("roster_composition",),
    "competition_format": ("competition_format",),
    "match_configuration": ("match_configuration", "match_settings"),
    "match_settings": ("match_settings", "match_configuration"),
    "map_pool": ("map_pool",),
    "equipment": ("equipment",),
    "in_match_operations": ("in_match_operations",),
    "pause_timeout": ("pause_timeout",),
    "disconnect": ("disconnect",),
    "fair_play_conduct": ("fair_play_conduct", "conduct"),
    "conduct": ("conduct", "fair_play_conduct"),
    "penalty": ("penalty", "penalty_matrix"),
    "penalty_matrix": ("penalty_matrix",),
    "dispute": ("dispute", "protest_dispute"),
    "protest_dispute": ("protest_dispute", "dispute"),
    "schedule": ("schedule",),
}


def source_facet_equivalents(facet: str | None) -> tuple[str, ...]:
    value = canonical_facet(facet) or str(facet or "").strip()
    return CANONICAL_TO_SOURCE_FACETS.get(value, (value,) if value else ())


def competition_source_facets(row: dict[str, Any]) -> frozenset[str]:
    """Return every proposition directly supported by one source chunk.

    This classifier intentionally favors precision.  Generic words such as
    ``team``, ``player``, ``match`` and ``referee`` never establish a facet on
    their own.  A chunk may support multiple facets when its literal text does
    so, for example a penalty table or a technical-pause clause that also
    describes disconnection handling.
    """
    title = normalize_text(str(row.get("section_title") or row.get("title") or ""))
    text = normalize_text(str(row.get("text") or row.get("content_th") or row.get("answer") or ""))
    combined = f"{title} {text}".strip()
    facets: set[str] = set()

    def has(*phrases: str) -> bool:
        return any(normalize_text(phrase) in combined for phrase in phrases)

    def title_has(*phrases: str) -> bool:
        return any(normalize_text(phrase) in title for phrase in phrases)

    if title_has("ภาพรวมเอกสาร", "ข้อมูลทั่วไป", "general information") or has(
        "ขอบเขตการบังคับใช้", "rulebook scope", "tournament identity"
    ):
        facets.add("rulebook_identity")
    if title_has("รายการ psu", "ประเภททีมชาย") and len(text) < 180:
        facets.add("rulebook_identity")

    if has("คุณสมบัติ", "มีสิทธิ์", "รับเฉพาะ", "eligible"):
        facets.add("eligibility_registration")
    if has("ลงทะเบียน", "รับสมัคร", "สมัครแข่งขัน", "registration", "registration deadline", "roster submission"):
        facets.update(("eligibility_registration", "registration"))

    # Team size needs a literal roster-size proposition.  "ทีมละ 2 pauses"
    # and "one timeout per team" are pause quotas, not team composition.
    if has("องค์ประกอบทีม", "ผู้เล่น 5 คน", "5 คนต่อทีม", "5v5", "team size"):
        facets.add("team_size")
    if title_has("องค์ประกอบทีม", "รายชื่อทีม", "roster composition") or has(
        "ตัวจริงและตัวสำรอง", "starters and substitutes", "roster composition"
    ) or (has("ตัวจริง", "starters") and has("ตัวสำรอง", "substitutes")):
        facets.add("roster_composition")

    if title_has("รูปแบบการแข่งขัน", "กติกาการแข่งขัน") or has(
        "single elimination", "double elimination", "best of 3", "best-of-3", "bo3", "bo5", "ft2"
    ):
        facets.add("competition_format")

    if has("เวอร์ชันของเกม", "match configuration", "room setup"):
        facets.add("match_configuration")
    if title_has("การตั้งค่าในเกม", "การตั้งค่าเกม", "game settings") or has(
        "competitive (5v5)", "freeze time", "เงินเริ่มต้น", "เวลาต่อรอบ", "จำนวนรอบสูงสุด", "overtime", "advantage:"
    ):
        facets.update(("match_configuration", "match_settings"))
    if title_has("แผนที่ในการแข่งขัน", "map pool") or has(
        "mapban.gg", "map veto", "map pool", "การเลือกแผนที่", "map ban", "ban maps", "แบนแผนที่"
    ):
        facets.add("map_pool")

    if title_has("อุปกรณ์", "competition area and regulations") or has(
        "คีย์บอร์ด", "เมาส์", "headset", "playstation 5", "โทรศัพท์มือถือ", "smartwatch", "controller"
    ):
        facets.add("equipment")

    if title_has("pre-game process") or has(
        "ต้องมาถึงสนามแข่ง", "arrive at the venue", "รายงานตัว", "check-in time", "ก่อนการแข่งขันทุกครั้ง"
    ) or (
        has("พื้นที่แข่ง", "competition area")
        and has("ห้าม", "อนุญาต", "not allowed", "prohibited", "only")
    ):
        facets.add("pre_match_on_site")
    if title_has("ขั้นตอนการดำเนินการแข่งขัน", "in-match procedure", "match operations") or has(
        "ต้องรีบแจ้งกรรมการ", "แจ้งผู้จัดการแข่งขันทันที"
    ):
        facets.add("in_match_operations")

    if title_has("หยุดเกม", "pause", "timeout") or has(
        "technical pause", "emergency pause", "ขอเวลานอก", "หยุดพักเกม", "การกดหยุดเกม"
    ):
        facets.add("pause_timeout")
    if has("หลุดจากการเชื่อมต่อ", "ผู้เข้าแข่งขันหลุด", "connection loss", "disconnection", "reconnect"):
        facets.add("disconnect")

    if title_has("มารยาท", "พฤติกรรม") or has(
        "น้ำใจนักกีฬา", "ก้าวร้าว", "ความรุนแรงทางวาจา", "hate speech", "sportsmanship", "toxic"
    ):
        facets.update(("conduct", "fair_play_conduct"))

    if title_has("ตารางบทลงโทษ", "penalty table", "penalty matrix") or (
        has("การละเมิด", "violation") and has("บทลงโทษ", "penalty")
    ):
        facets.update(("penalty", "penalty_matrix"))
    elif title_has("บทลงโทษ", "ประเภทบทลงโทษ", "in-game penalty types") or has(
        "ปรับแพ้ทันที", "ถูกตัดสิทธิ์", "round loss", "map forfeit", "match forfeit", "disqualification"
    ):
        facets.add("penalty")

    if title_has("ข้อพิพาท", "dispute resolution") or has(
        "กรณีเกิดข้อโต้แย้ง", "การประท้วง", "raise an objection", "protest", "dispute"
    ):
        facets.update(("dispute", "protest_dispute"))

    if title_has("กำหนดการแข่งขัน", "ตารางเวลา", "competition schedule", "event schedule") or has(
        "สายการแข่งขันจะประกาศ", "วันแข่งขัน", "แข่งขันออฟไลน์ วันที่"
    ):
        facets.add("schedule")

    return frozenset(facets)


def source_row_supports_facet(row: dict[str, Any], facet: str | None) -> bool:
    required = set(source_facet_equivalents(facet))
    return bool(required and required.intersection(competition_source_facets(row)))
