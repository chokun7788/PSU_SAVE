"""Bounded request grammar for competition conversations; no factual inference."""
from __future__ import annotations

import re
import unicodedata


def _clean(query: str) -> str:
    q = unicodedata.normalize("NFC", str(query or "")).casefold().strip(" ?!.,")
    return re.sub(r"(?:รายการ)+(?=แข่ง)", "รายการ", q).replace("กฏ", "กฎ")


def is_rulebook_catalog_request(query: str) -> bool:
    q = re.sub(r"\s+", "", _clean(query))
    thai = re.fullmatch(
        r"(?:ตอนนี้)?(?:มี)?(?:รายการแข่ง|รายการแข่งขัน|เกมแข่ง|เกมแข่งขัน)(?:มี)?(?:อะไรบ้าง|อะไรมั่ง|ไหนบ้าง)(?:ครับ|ค่ะ|คับ)?"
        r"|(?:ตอนนี้)?(?:มี)?เกม(?:อะไร|ไหน)(?:ให้|ที่)?(?:รายการ)?(?:แข่ง|แข่งขัน)(?:บ้าง|มั่ง)?(?:ครับ|ค่ะ|คับ)?", q,
    )
    english = re.fullmatch(
        r"(?:what|which) (?:tournaments|competitions|competition games)(?: are (?:there|available|recorded))?"
        r"|list (?:the )?(?:tournaments|competitions|competition games)"
        r"|(?:what|which) games (?:can (?:we|i) compete in|are (?:there|available) for competition)", _clean(query),
    )
    return bool(thai or english)


def _generic_rule_text(query: str) -> str:
    from app.pipeline.competition_targets import resolve_competition_targets, replace_competition_target_mentions
    from app.core.typo_similarity import osa_distance

    resolution = resolve_competition_targets(query)
    if resolution.status == "exact":
        query = replace_competition_target_mentions(query, resolution, "")
    elif resolution.status != "absent":
        return ""
    q = _clean(query)
    if re.search(r"กฎ|กติกา", q):
        # Correct only the courtesy tail after an explicit rule request.
        # Do not rewrite unknown topic words or infer a different game.
        q = re.sub(r"(?:ครับ|ค่ะ|คับ)\s*$", "", q).rstrip()
        for size in (5, 4, 6):
            suffix = q[-size:]
            prefix = q[:-size].rstrip()
            complete_request = re.fullmatch(
                r"(?:ขอ|ดู|เอา|แล้ว|อยากรู้|อยากดู|บอก|สรุป|มี|ของ|เกมนี้|เกม|กฎ|กติกา|การ|ตอน|แข่งขัน|แข่ง|อะไร|บ้าง|มั่ง|อื่น|เพิ่มเติม|อีก|ทั้งหมด|ไหม|มั้ย|\s)+", prefix,
            ) and re.search(r"กฎ|กติกา", prefix)
            if complete_request and suffix and osa_distance(suffix, "หน่อย") <= 1:
                q = q[:-size].rstrip()
                break
    return q.strip(" ?!.,")


def is_broad_rule_request(query: str) -> bool:
    q = _generic_rule_text(query)
    if not q or not re.search(r"กฎ|กติกา|\brules?\b|\bregulations\b", q):
        return False
    thai = re.fullmatch(
        r"(?:ขอ|ดู|เอา|แล้ว|อยากรู้|อยากดู|บอก|สรุป|มี|เรื่อง|ของ|เกมนี้|เกม|กฎ|กติกา|ระเบียบ|การ|ตอน|แข่งขัน|แข่ง|ทัวร์นาเมนต์|อะไร|บ้าง|มั่ง|อื่น|เพิ่มเติม|อีก|ทั้งหมด|ไหม|มั้ย|หน่อย|ครับ|ค่ะ|คับ|\s|[?!.,])+", q,
    )
    english = re.fullmatch(
        r"(?:can|could|i|we|you|see|show|tell|give|me|please|what|which|are|is|the|a|an|and|any|about|it|its|this|game|of|for|tournament|competition|rules|rule|regulations|other|more|additional|all|overview|summarize|\s|[?!.,])+", q,
    )
    return bool(thai or english)


def is_more_rule_request(query: str) -> bool:
    q = _generic_rule_text(query)
    return is_broad_rule_request(query) and bool(re.search(r"อื่น|เพิ่มเติม|อีก|\b(?:more|other|additional)\b", q))
