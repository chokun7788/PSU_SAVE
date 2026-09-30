#!/usr/bin/env python3
"""Build a non-destructive canonical view of existing competition-rule data.

The existing chunks and fact-card JSONL files stay untouched because they are
current runtime inputs.  This tool creates a governed, common-schema view in
data/competition_rules/canonical so new rulebooks can follow one shape before
they are published to Structured facts and RAG.
"""

from __future__ import annotations

import argparse
from difflib import SequenceMatcher
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
RULES_DIR = ROOT / "data" / "competition_rules"
OUT_DIR = RULES_DIR / "canonical"
SCHEMA_VERSION = "competition_rule_canonical_v1"
RELEASE_OVERRIDES_PATH = OUT_DIR / "release_overrides.jsonl"

CORE_SECTIONS = (
    ("rulebook_identity", "ข้อมูลเอกสารและขอบเขต"),
    ("eligibility_registration", "คุณสมบัติและการลงทะเบียน"),
    ("competition_format", "รูปแบบการแข่งขัน"),
    ("match_configuration", "การตั้งค่าแมตช์"),
    ("pre_match_on_site", "ก่อนแข่งและหน้างาน"),
    ("in_match_operations", "ระหว่างการแข่งขัน"),
    ("fair_play_conduct", "ความเป็นธรรมและพฤติกรรม"),
    ("penalty_matrix", "บทลงโทษ"),
    ("protest_dispute", "การประท้วงและข้อพิพาท"),
    ("references_change_history", "แหล่งอ้างอิงและประวัติการแก้ไข"),
)
SECTION_LABELS = dict(CORE_SECTIONS)

GAME_IDS = {
    "Counter-Strike 2": "cs2",
    "VALORANT": "valorant",
    "Arena of Valor (RoV)": "rov",
    "Tekken 8": "tekken8",
}

INTENT_SECTION = {
    "team_size": "eligibility_registration",
    "player_count": "eligibility_registration",
    "eligibility": "eligibility_registration",
    "registration": "eligibility_registration",
    "roster_change": "eligibility_registration",
    "substitute": "eligibility_registration",
    "format": "competition_format",
    "bracket": "competition_format",
    "best_of": "competition_format",
    "schedule": "pre_match_on_site",
    "schedule_location": "pre_match_on_site",
    "late_start": "pre_match_on_site",
    "check_in": "pre_match_on_site",
    "equipment": "pre_match_on_site",
    "game_version": "match_configuration",
    "game_setting": "match_configuration",
    "map_pool": "match_configuration",
    "map_ban": "match_configuration",
    "side_selection": "match_configuration",
    "character": "match_configuration",
    "hero_rule": "match_configuration",
    "skin_rule": "match_configuration",
    "skin": "match_configuration",
    "break_time": "in_match_operations",
    "summary": "match_configuration",
    "pause": "in_match_operations",
    "timeout": "in_match_operations",
    "rematch": "in_match_operations",
    "restart": "in_match_operations",
    "disconnect": "in_match_operations",
    "policy": "fair_play_conduct",
    "fair_play": "fair_play_conduct",
    "bug_rule": "fair_play_conduct",
    "penalty": "penalty_matrix",
    "protest": "protest_dispute",
    "dispute": "protest_dispute",
}


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSONL at {path}:{line_number}: {exc}") from exc
    return rows


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    text = "\n".join(json.dumps(row, ensure_ascii=False, sort_keys=True) for row in rows)
    path.write_text(text + ("\n" if text else ""), encoding="utf-8")


def text_hash(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.casefold()).strip()


def has_any(haystack: str, needles: Iterable[str]) -> bool:
    return any(needle in haystack for needle in needles)


def source_year(value: str) -> int | None:
    # A word boundary does not exist between Thai letters and digits, so use
    # digit boundaries rather than \b for source names such as "รายการปี2026".
    years = re.findall(r"(?<!\d)(20\d{2})(?!\d)", value)
    return int(years[-1]) if years else None


def content_key(value: str) -> str:
    """A stable comparison form; it retains Thai characters and numbers."""
    return re.sub(r"[^\wก-๙]+", "", normalize(value))


def classify_rule_type(text: str) -> str:
    source = normalize(text)
    if has_any(source, ("บทลงโทษ", "ตัดสิทธิ์", "ปรับแพ้", "แบน", "forfeit", "warning")):
        return "penalty"
    if has_any(source, ("ห้าม", "ไม่อนุญาต", "strictly prohibited", "must not")):
        return "prohibition"
    if has_any(source, ("อนุญาต", "permitted", "allowed")):
        return "allowance"
    if has_any(source, ("ขั้นตอน", "procedure", "ต้อง", "must", "จะต้อง")):
        return "requirement_or_procedure"
    return "information_or_context"


def extract_conditions(game_id: str, tournament: str | None, text: str) -> dict[str, Any]:
    """Extract only safe, visible conditions; unknown values remain null/empty."""
    source = normalize(text)
    best_of = re.search(r"(?:best\s*of|bo)\s*([1357])\b", source)
    team_size = re.search(r"\b([2-6])\s*v\s*\1\b", source)
    maps = [
        name for name in ("Ancient", "Anubis", "Dust 2", "Inferno", "Mirage", "Nuke", "Train", "Abyss")
        if name.casefold() in source
    ]
    platforms = [
        label for label, signals in {
            "Steam": ("steam",),
            "PC": (" pc", "computer"),
            "PlayStation": ("playstation", "ps5"),
            "Nintendo Switch": ("nintendo switch",),
        }.items() if has_any(source, signals)
    ]
    return {
        "game_id": game_id,
        "tournament": tournament,
        "competition_phase": None,
        "match_format": f"BO{best_of.group(1)}" if best_of else None,
        "team_size": int(team_size.group(1)) if team_size else None,
        "platforms": platforms,
        "maps": maps,
        "exceptions_present": has_any(source, ("ยกเว้น", "except", "unless")),
    }


def source_locator(chunk: dict[str, Any]) -> dict[str, Any]:
    return {
        "source_document_id": chunk.get("document_id"),
        "source_chunk_id": chunk.get("id"),
        "section_title_th": chunk.get("section_title"),
        "section_index": chunk.get("section_index"),
        "chunk_index": chunk.get("chunk_index"),
        "source_file": chunk.get("source_file"),
        "source_url": chunk.get("source_url"),
    }


def fact_evidence_links(fact: dict[str, Any], candidates: list[dict[str, Any]]) -> tuple[str, list[dict[str, Any]]]:
    """Return conservative candidate links, never silently upgrading a paraphrase.

    Existing fact cards usually reference a document, not a precise chunk.  The
    links produced here are review candidates unless a full statement is found
    verbatim in the original chunk.
    """
    query = content_key(f"{fact.get('evidence', '')} {fact.get('answer', '')}")
    scored: list[tuple[float, bool, dict[str, Any]]] = []
    for candidate in candidates:
        candidate_text = content_key(f"{candidate.get('section_title_th', '')} {candidate.get('content_th', '')}")
        if not query or not candidate_text:
            continue
        direct = len(query) >= 20 and (query in candidate_text or candidate_text in query)
        score = SequenceMatcher(None, query[:2400], candidate_text[:2400], autojunk=False).ratio()
        scored.append((score, direct, candidate))
    scored.sort(key=lambda item: (item[1], item[0]), reverse=True)
    links = [
        {
            "rule_id": row[2]["rule_id"],
            "source_chunk_id": row[2]["source_chunk_id"],
            "source_locator": row[2]["source_locator"],
            "match_method": "verbatim_containment" if row[1] else "similarity_candidate",
            "similarity": round(row[0], 4),
        }
        for row in scored[:3]
    ]
    if links and links[0]["match_method"] == "verbatim_containment":
        return "verified_direct", links
    if links and links[0]["similarity"] >= 0.35:
        return "candidate_review_required", links
    return "document_level_only", []


def classify_section(game: str, section_title: str, text: str) -> str:
    """Map source prose to a stable cross-game section, conservatively."""
    source = normalize(f"{section_title} {text}")
    # Compact source chunks can contain only a heading and one rule. Resolve
    # distinctive operational terms before broad words such as "ห้าม" or
    # "ผู้ตัดสิน" pull them into a less useful category.
    if has_any(source, (
        "เวอร์ชันของเกม", "competitive (5v5)", "เวลาต่อรอบ", "freeze time",
        "เงินเริ่มต้น", "เวลาของระเบิด", "จำนวนรอบสูงสุด", "การต่อเวลา",
        "map pool", "map ban", "แผนที่", "เลือกฝั่ง", "side selection",
        "ตัวละคร", "hero", "skin", "agent", "stage", "ancient, anubis",
    )):
        return "match_configuration"
    if has_any(source, ("ขอเวลานอก", "timeout", "pause", "หยุดเกม", "rematch", "restart", "rollback", "disconnect", "หลุด", "ขั้นตอนการดำเนินการแข่งขัน")):
        return "in_match_operations"
    if has_any(source, ("การแข่งขันทั้งหมด 1 วัน", "แข่งขัน ณ", "competition area", "พื้นที่แข่ง", "จัดเตรียม pc", "จอภาพ", "หูฟัง")):
        return "pre_match_on_site"
    if has_any(source, ("เปลี่ยนแปลงสมาชิก", "สมาชิกในทีม", "ผู้เล่น 5 คน", "ตัวสำรอง", "ลงทะเบียน", "สมัคร")):
        return "eligibility_registration"
    if has_any(source, ("ห้ามติดตั้งโปรแกรม", "โซเชียลมีเดีย", "โทรศัพท์มือถือ", "แท็บเล็ต", "สมาร์ทวอทช์", "ข้อจำกัด", "การสื่อสาร", "น้ำดื่ม", "หมากฝรั่ง")):
        return "fair_play_conduct"
    if has_any(source, ("แบนถาวร", "ปรับให้แพ้", "ตัดสิทธิ์", "บทลงโทษ")):
        return "penalty_matrix"
    if has_any(source, ("อำนาจตัดสิน", "ผู้ตัดสิน", "คำตัดสินของกรรมการ", "ข้อตกลงและข้อปฏิบัติ")):
        return "protest_dispute"
    if has_any(source, ("รายการ psu", "ประเภททีมชาย")):
        return "rulebook_identity"
    if has_any(source, ("อ้างอิง", "แหล่งข้อมูล", "แก้ไขล่าสุด", "revision", "version history")):
        return "references_change_history"
    if has_any(source, ("ประท้วง", "ข้อพิพาท", "ผู้ตัดสินมีสิทธิ์", "คำตัดสินของผู้ตัดสิน")):
        return "protest_dispute"
    if has_any(source, ("บทลงโทษ", "ตัดสิทธิ์", "ปรับแพ้", "forfeit", "warning", "ลงโทษ")):
        return "penalty_matrix"
    if has_any(source, ("มารยาท", "บัค", "bug", "มาโคร", "macro", "โกง", "สตรีม", "เหยียด", "พฤติกรรม")):
        return "fair_play_conduct"
    if has_any(source, ("pause", "timeout", "หยุดเกม", "rematch", "restart", "rollback", "disconnect", "หลุด")):
        return "in_match_operations"
    if has_any(source, ("สถานที่", "ตารางเวลา", "check-in", "check in", "ก่อนเริ่ม", "อุปกรณ์", "พื้นที่แข่งขัน", "มาถึง")):
        return "pre_match_on_site"
    if has_any(source, ("แผนที่", "map pool", "map ban", "overtime", "เวอร์ชันเกม", "โหมดเกม", "ตั้งค่า", "ตัวละคร", "hero", "skin", "agent", "stage", "side selection")):
        return "match_configuration"
    if has_any(source, ("รูปแบบการแข่งขัน", "single elimination", "double elimination", "best of", "bo1", "bo3", "bo5", "สายการแข่งขัน", "รอบการแข่งขัน")):
        return "competition_format"
    if has_any(source, ("คุณสมบัติ", "ลงทะเบียน", "สมาชิกทีม", "ผู้เล่น", "รายชื่อ", "ตัวสำรอง", "ถอนตัว", "สมัคร")):
        return "eligibility_registration"
    if has_any(source, ("ข้อมูลทั่วไป", "ภาพรวม", "ชื่อรายการ", "general information", "competition rules", "กฎระเบียบ")):
        return "rulebook_identity"
    return "other_or_unclassified"


def classify_module(game: str, section: str, section_title: str, text: str) -> tuple[str, str]:
    source = normalize(f"{section_title} {text}")
    if game == "Counter-Strike 2":
        if has_any(source, ("map pool", "map ban", "แผนที่", "side selection", "เลือกฝั่ง")):
            return "cs2_map_veto_and_side_selection", "CS2: Map veto และการเลือกฝั่ง"
        if has_any(source, ("overtime", "การต่อเวลา")):
            return "cs2_overtime", "CS2: Overtime"
    elif game == "VALORANT":
        if has_any(source, ("agent", "เอเจนต์", "ตัวละคร")):
            return "valorant_agent_selection", "VALORANT: การเลือก Agent"
        if has_any(source, ("pause", "timeout", "หยุดเกม")):
            return "valorant_pause_taxonomy", "VALORANT: ประเภทการพักเกม"
    elif game == "Arena of Valor (RoV)":
        if has_any(source, ("hero", "ฮีโร่", "skin", "สกิน")):
            return "rov_hero_and_skin", "RoV: Hero และ Skin"
        if has_any(source, ("พัก", "break time")):
            return "rov_break_time", "RoV: เวลาพัก"
    elif game == "Tekken 8":
        if has_any(source, ("ตัวละคร", "character", "stage", "ด่าน")):
            return "tekken8_character_and_stage", "Tekken 8: Character และ Stage"
        if has_any(source, ("controller", "จอย", "อุปกรณ์ควบคุม")):
            return "tekken8_controller_settings", "Tekken 8: Controller settings"
    return "common", "หัวข้อกลางใช้ร่วมกัน"


def classify_facet(section: str, section_title: str, text: str) -> str:
    source = normalize(f"{section_title} {text}")
    checks = (
        ("team_size", ("ทีมละ", "ผู้เล่น 5", "จำนวนผู้เล่น")),
        ("registration", ("ลงทะเบียน", "สมัคร", "รายชื่อ")),
        ("schedule", ("ตารางเวลา", "กำหนดการ", "วันแข่งขัน")),
        ("equipment", ("อุปกรณ์", "controller", "จอย")),
        ("map_pool", ("map pool", "แผนที่")),
        ("match_settings", ("ตั้งค่า", "เวอร์ชันเกม", "โหมดเกม")),
        ("pause_timeout", ("pause", "timeout", "หยุดเกม")),
        ("disconnect", ("disconnect", "หลุด")),
        ("rematch", ("rematch", "แข่งใหม่")),
        ("conduct", ("มารยาท", "พฤติกรรม", "โกง", "บัค", "bug")),
        ("penalty", ("บทลงโทษ", "ตัดสิทธิ์", "ปรับแพ้", "warning")),
        ("dispute", ("ประท้วง", "ข้อพิพาท", "ผู้ตัดสิน")),
    )
    for facet, signals in checks:
        if has_any(source, signals):
            return facet
    return section


def build() -> dict[str, Any]:
    documents = read_jsonl(RULES_DIR / "competition_rule_documents.jsonl")
    chunks = read_jsonl(RULES_DIR / "competition_rule_chunks.jsonl")
    fact_files = sorted(RULES_DIR.glob("competition_rule_fact_cards*.jsonl"))
    facts = [row for path in fact_files for row in read_jsonl(path)]
    docs_by_id = {str(row["id"]): row for row in documents}
    chunks_by_document: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for chunk in chunks:
        chunks_by_document[str(chunk.get("document_id", ""))].append(chunk)
    document_content_hashes = {
        document_id: text_hash(json.dumps(
            [
                {"id": chunk.get("id"), "text": chunk.get("text")}
                for chunk in document_chunks
            ],
            ensure_ascii=False,
            sort_keys=True,
        ))
        for document_id, document_chunks in chunks_by_document.items()
    }
    overrides = {
        str(row.get("rulebook_id")): row
        for row in read_jsonl(RELEASE_OVERRIDES_PATH)
        if row.get("rulebook_id")
    }

    registry: list[dict[str, Any]] = []
    releases: list[dict[str, Any]] = []
    for doc in documents:
        game = str(doc.get("game", ""))
        rulebook_id = str(doc["id"])
        document_hash = document_content_hashes.get(rulebook_id, "")
        override = overrides.get(rulebook_id, {})
        approved_hash = override.get("approved_source_document_sha256")
        hash_matches_approval = bool(approved_hash and approved_hash == document_hash)
        review_status = "approved" if override.get("review_status") == "approved" and hash_matches_approval else "pending_owner_review"
        has_effective_period = bool(override.get("effective_from"))
        activation_requested = override.get("activation_status") == "active"
        runtime_eligible = review_status == "approved" and has_effective_period and activation_requested
        lifecycle_status = "active" if runtime_eligible else "review_required"
        registry.append({
            "schema_version": SCHEMA_VERSION,
            "rulebook_id": rulebook_id,
            "game_id": GAME_IDS.get(game, "unknown"),
            "game": game,
            "tournament": doc.get("tournament"),
            "title_th": doc.get("title"),
            "scope": "tournament_specific",
            "source_year": source_year(" ".join(str(doc.get(key, "")) for key in ("title", "tournament", "source_file"))),
            "source_language": doc.get("language", "th/mixed"),
            "source_file": doc.get("source_file"),
            "source_url": doc.get("source_url"),
            "source_document_sha256": document_hash,
            "effective_from": override.get("effective_from"),
            "effective_to": override.get("effective_to"),
            "supersedes_rulebook_id": override.get("supersedes_rulebook_id"),
            "approval": {
                "review_status": review_status,
                "approved_by": override.get("approved_by"),
                "approved_at": override.get("approved_at"),
                "approved_source_document_sha256": approved_hash,
                "source_hash_matches_approval": hash_matches_approval,
            },
            "lifecycle_status": lifecycle_status,
            "runtime_eligible": runtime_eligible,
            "canonical_status": "migrated_from_existing_content",
            "review_status": review_status,
            "publish_eligible": runtime_eligible,
        })
        releases.append({
            "schema_version": SCHEMA_VERSION,
            "release_id": rulebook_id,
            "rulebook_id": rulebook_id,
            "game_id": GAME_IDS.get(game, "unknown"),
            "scope": "tournament_specific",
            "source_year": source_year(" ".join(str(doc.get(key, "")) for key in ("title", "tournament", "source_file"))),
            "source_document_sha256": document_hash,
            "effective_from": override.get("effective_from"),
            "effective_to": override.get("effective_to"),
            "review_status": review_status,
            "activation_status": "active" if runtime_eligible else "inactive",
            "runtime_eligible": runtime_eligible,
            "inactive_reason": None if runtime_eligible else "Requires owner approval, approved source hash, and an effective_from date.",
            "conflict_policy": "use_newest_owner_approved_release_or_ask_for_tournament_context",
        })

    records: list[dict[str, Any]] = []
    chunk_section: dict[str, str] = {}
    for chunk in chunks:
        game = str(chunk.get("game", ""))
        section_title = str(chunk.get("section_title", ""))
        content = str(chunk.get("text", ""))
        section = classify_section(game, section_title, content)
        module, module_label = classify_module(game, section, section_title, content)
        source_id = str(chunk["id"])
        chunk_section[source_id] = section
        records.append({
            "schema_version": SCHEMA_VERSION,
            "rule_id": f"canonical::{source_id}",
            "rulebook_id": chunk.get("document_id"),
            "game_id": GAME_IDS.get(game, "unknown"),
            "game": game,
            "tournament": chunk.get("tournament"),
            "scope": "tournament_specific",
            "canonical_section": section,
            "canonical_section_label_th": SECTION_LABELS.get(section, "อื่น ๆ / ต้องจัดหมวด"),
            "module": module,
            "module_label_th": module_label,
            "facet": classify_facet(section, section_title, content),
            "rule_type": classify_rule_type(content),
            "conditions": extract_conditions(GAME_IDS.get(game, "unknown"), chunk.get("tournament"), content),
            "conflict_policy": "use_newest_owner_approved_release_or_ask_for_tournament_context",
            "title_th": chunk.get("title"),
            "section_title_th": section_title,
            "content_th": content,
            "source_chunk_id": source_id,
            "source_document_id": chunk.get("document_id"),
            "source_file": chunk.get("source_file"),
            "source_url": chunk.get("source_url"),
            "source_locator": source_locator(chunk),
            "source_text_sha256": text_hash(content),
            "source_language": "th/mixed",
            "localization": {"th": "source", "en": "missing_approved_localization"},
            "canonical_status": "migrated_from_existing_content",
            "review_status": "pending_owner_review",
            "publish_eligible": False,
        })

    releases_by_id = {row["release_id"]: row for row in releases}
    records_by_rulebook: dict[str, list[dict[str, Any]]] = defaultdict(list)
    records_by_source_chunk = {str(record["source_chunk_id"]): record for record in records}
    for record in records:
        records_by_rulebook[str(record["rulebook_id"])].append(record)
    fact_fingerprints = Counter(
        (str(fact.get("game", "")), str(fact.get("intent", "")).casefold(), content_key(str(fact.get("answer", ""))))
        for fact in facts
    )

    facts_projection: list[dict[str, Any]] = []
    for fact in facts:
        game = str(fact.get("game", ""))
        intent = str(fact.get("intent", "")).casefold()
        section = INTENT_SECTION.get(intent, "other_or_unclassified")
        answer = str(fact.get("answer", ""))
        module, module_label = classify_module(game, section, intent, answer)
        source_reference_ids = [str(item) for item in fact.get("source_ids", [])]
        rulebook_ids = [item for item in source_reference_ids if item in releases_by_id]
        candidate_records = [
            record for rulebook_id in rulebook_ids for record in records_by_rulebook.get(rulebook_id, [])
        ]
        declared_records = [
            records_by_source_chunk[source_id]
            for source_id in source_reference_ids
            if source_id in records_by_source_chunk
        ]
        if declared_records:
            evidence_status = "declared_chunk_reference_pending_text_check"
            evidence_links = [{
                "rule_id": record["rule_id"],
                "source_chunk_id": record["source_chunk_id"],
                "source_locator": record["source_locator"],
                "match_method": "declared_by_legacy_fact_card",
                "similarity": None,
            } for record in declared_records]
        else:
            evidence_status, evidence_links = fact_evidence_links(fact, candidate_records)
        fingerprint = (game, intent, content_key(answer))
        facts_projection.append({
            "schema_version": SCHEMA_VERSION,
            "fact_id": fact.get("id"),
            "rulebook_ids": rulebook_ids,
            "release_ids": rulebook_ids,
            "source_reference_ids": source_reference_ids,
            "game_id": GAME_IDS.get(game, "unknown"),
            "game": game,
            "tournament": fact.get("tournament"),
            "scope": "tournament_specific",
            "canonical_section": section,
            "canonical_section_label_th": SECTION_LABELS.get(section, "อื่น ๆ / ต้องจัดหมวด"),
            "module": module,
            "module_label_th": module_label,
            "facet": intent or section,
            "answer_type": fact.get("answer_type"),
            "answer_th": answer,
            "evidence_th": fact.get("evidence"),
            "evidence_status": evidence_status,
            "evidence_links": evidence_links,
            "question_patterns_th": fact.get("question_patterns", []),
            "source_url": fact.get("source_url"),
            "source_answer_sha256": text_hash(answer),
            "content_fingerprint": text_hash("|".join(fingerprint)),
            "duplicate_answer_count": fact_fingerprints[fingerprint],
            "conditions": extract_conditions(GAME_IDS.get(game, "unknown"), fact.get("tournament"), answer),
            "localization": {"th": "source", "en": "missing_approved_localization"},
            "canonical_status": "migrated_from_existing_content",
            "review_status": "pending_owner_review",
            "publish_eligible": False,
        })

    rag_projections: list[dict[str, Any]] = []
    en_localization_queue: list[dict[str, Any]] = []
    for record in records:
        release = releases_by_id.get(str(record["rulebook_id"]), {})
        retrieval_text = "\n".join((
            f"เกม: {record['game']}",
            f"รายการแข่งขัน: {record['tournament']}",
            f"ขอบเขต: {record['scope']}",
            f"หัวข้อกลาง: {record['canonical_section_label_th']}",
            f"โมดูล: {record['module_label_th']}",
            f"หัวข้อย่อย: {record['section_title_th']}",
            f"กติกา: {record['content_th']}",
        ))
        rag_projections.append({
            "schema_version": SCHEMA_VERSION,
            "chunk_id": f"canonical_rag::{record['source_chunk_id']}",
            "rule_id": record["rule_id"],
            "release_id": record["rulebook_id"],
            "category": "competition_rules",
            "game_id": record["game_id"],
            "game": record["game"],
            "tournament": record["tournament"],
            "scope": record["scope"],
            "canonical_section": record["canonical_section"],
            "module": record["module"],
            "facet": record["facet"],
            "conditions": record["conditions"],
            "text_th": retrieval_text,
            "source_locator": record["source_locator"],
            "source_text_sha256": record["source_text_sha256"],
            "runtime_eligible": bool(release.get("runtime_eligible")),
            "retrieval_status": "inactive_pending_release_approval",
        })
        en_localization_queue.append({
            "schema_version": SCHEMA_VERSION,
            "localization_id": f"en::{record['rule_id']}::content_th",
            "rule_id": record["rule_id"],
            "field": "content_th",
            "target_locale": "en",
            "source_text_sha256": record["source_text_sha256"],
            "status": "missing_human_approved_localization",
            "approved_text": None,
            "approved_by": None,
            "approved_at": None,
        })

    fact_evidence_review_queue = [
        {
            "fact_id": fact["fact_id"],
            "game": fact["game"],
            "tournament": fact["tournament"],
            "canonical_section": fact["canonical_section"],
            "facet": fact["facet"],
            "answer_th": fact["answer_th"],
            "evidence_th": fact["evidence_th"],
            "evidence_status": fact["evidence_status"],
            "source_reference_ids": fact["source_reference_ids"],
            "suggested_evidence_links": fact["evidence_links"],
            "review_action": "Confirm one source chunk, correct the answer/evidence, or retire this fact before release activation.",
        }
        for fact in facts_projection
        if fact["evidence_status"] != "verified_direct"
    ]
    release_owner_review_queue = [
        {
            "rulebook_id": release["rulebook_id"],
            "game_id": release["game_id"],
            "source_document_sha256": release["source_document_sha256"],
            "required_before_activation": [
                "owner approval with matching source hash",
                "effective_from date",
                "activation_status=active in release_overrides.jsonl",
            ],
        }
        for release in releases
        if not release["runtime_eligible"]
    ]

    coverage: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "migration_note_th": "เป็นมุมมองกลางที่สร้างจากข้อมูล runtime เดิม ไม่ได้แทนที่ไฟล์ต้นทาง และยังต้องให้เจ้าของตรวจทานก่อน publish เป็น release ใหม่",
        "rulebooks": [],
        "release_summary": {
            "active_release_count": sum(row["runtime_eligible"] for row in releases),
            "inactive_release_count": sum(not row["runtime_eligible"] for row in releases),
            "english_localization_queue_count": len(en_localization_queue),
        },
    }
    records_by_game: dict[str, list[dict[str, Any]]] = defaultdict(list)
    facts_by_game: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in records:
        records_by_game[row["game"]].append(row)
    for row in facts_projection:
        facts_by_game[row["game"]].append(row)
    for doc in documents:
        game = str(doc.get("game", ""))
        game_records = records_by_game[game]
        game_facts = facts_by_game[game]
        sections = []
        for code, label in CORE_SECTIONS:
            record_count = sum(row["canonical_section"] == code for row in game_records)
            fact_count = sum(row["canonical_section"] == code for row in game_facts)
            status = "present" if record_count and fact_count else "partial" if record_count or fact_count else "not_found"
            sections.append({
                "section": code,
                "label_th": label,
                "status": status,
                "rule_record_count": record_count,
                "fact_projection_count": fact_count,
            })
        module_counts = Counter(row["module"] for row in game_records if row["module"] != "common")
        coverage["rulebooks"].append({
            "rulebook_id": doc["id"],
            "game": game,
            "tournament": doc.get("tournament"),
            "rule_record_count": len(game_records),
            "fact_projection_count": len(game_facts),
            "sections": sections,
            "game_specific_modules": [
                {"module": module, "rule_record_count": count}
                for module, count in sorted(module_counts.items())
            ],
            "unclassified_rule_record_count": sum(
                row["canonical_section"] == "other_or_unclassified" for row in game_records
            ),
            "unclassified_fact_projection_count": sum(
                row["canonical_section"] == "other_or_unclassified" for row in game_facts
            ),
            "fact_evidence_status": dict(Counter(row["evidence_status"] for row in game_facts)),
            "duplicate_fact_count": sum(row["duplicate_answer_count"] > 1 for row in game_facts),
        })

    return {
        "registry": registry,
        "releases": releases,
        "records": records,
        "facts_projection": facts_projection,
        "rag_projections": rag_projections,
        "en_localization_queue": en_localization_queue,
        "fact_evidence_review_queue": fact_evidence_review_queue,
        "release_owner_review_queue": release_owner_review_queue,
        "coverage": coverage,
        "source_counts": {"documents": len(documents), "chunks": len(chunks), "facts": len(facts), "fact_files": len(fact_files)},
        "docs_by_id": docs_by_id,
    }


def report_markdown(model: dict[str, Any]) -> str:
    coverage = model["coverage"]
    lines = [
        "# Competition Rule Canonical Coverage",
        "",
        "เอกสารนี้สร้างอัตโนมัติจากข้อมูลกติกาที่ระบบใช้อยู่เดิม เพื่อแสดงความครอบคลุมของรูปแบบกลาง ไม่ได้ยืนยันว่ากติกาแต่ละรายการได้รับการอนุมัติใหม่แล้ว.",
        "",
        "## สถานะข้อมูล",
        "",
        "- `present`: พบทั้ง Rule Record และ Fact Projection",
        "- `partial`: พบอย่างน้อยหนึ่งชั้นข้อมูล แต่ควรเติมอีกชั้นก่อน publish release ใหม่",
        "- `not_found`: ยังไม่พบข้อมูลหัวข้อนั้นในเอกสารที่นำเข้า ไม่ได้หมายความว่ากติกาอนุญาตหรือห้ามโดยปริยาย",
        "",
        "## Release Safety",
        "",
        f"- Active releases: {coverage['release_summary']['active_release_count']}",
        f"- Inactive releases awaiting review: {coverage['release_summary']['inactive_release_count']}",
        f"- English fields awaiting approved localization: {coverage['release_summary']['english_localization_queue_count']}",
        "- Release ที่ยัง inactive ห้ามถูกใช้ตอบว่าเป็นกติกาปัจจุบัน; ระบบต้องขอชื่อรายการ/ช่วงเวลาหรือ no-answer.",
        "",
        "## หลักการใช้งาน",
        "",
        "- `common` คือหัวข้อที่ทุกเกมใช้โครงเดียวกันได้",
        "- โมดูลชื่อเกม เช่น `cs2_map_veto_and_side_selection` คือรายละเอียดเฉพาะเกมและเป็น optional module",
        "- ไฟล์ต้นทางใน `data/competition_rules` ไม่ถูกแก้ไข; runtime เดิมยังอ่านไฟล์เดิมจนกว่าจะมีการอนุมัติและสลับ release แบบ atomic",
        "",
    ]
    for rulebook in coverage["rulebooks"]:
        lines.extend([
            f"## {rulebook['game']}",
            "",
            f"- Rule records: {rulebook['rule_record_count']}",
            f"- Fact projections: {rulebook['fact_projection_count']}",
            f"- ต้องจัดหมวดเพิ่ม: Rule {rulebook['unclassified_rule_record_count']} / Fact {rulebook['unclassified_fact_projection_count']}",
            f"- Evidence: {', '.join(f'{key}={value}' for key, value in sorted(rulebook['fact_evidence_status'].items())) or 'ไม่มี Fact'}",
            f"- Fact คำตอบซ้ำที่ต้องรวม/ตรวจ: {rulebook['duplicate_fact_count']}",
            "",
            "| หัวข้อกลาง | สถานะ | Rule | Fact |",
            "| --- | --- | ---: | ---: |",
        ])
        for section in rulebook["sections"]:
            lines.append(f"| {section['label_th']} | {section['status']} | {section['rule_record_count']} | {section['fact_projection_count']} |")
        modules = rulebook["game_specific_modules"]
        if modules:
            lines.extend(["", "โมดูลเฉพาะเกมที่ตรวจพบ:"])
            lines.extend(f"- `{item['module']}` ({item['rule_record_count']} rule records)" for item in modules)
        lines.append("")
    lines.extend([
        "## ขั้นตอนเมื่อต้องเพิ่มกติกาใหม่",
        "",
        "1. เพิ่มเอกสารต้นทางและสร้าง chunk/fact card ตามกระบวนการเดิมใน staging.",
        "2. รัน `py -3 tools/build_competition_rule_canonical.py --write` เพื่อสร้างมุมมองกลางใหม่.",
        "3. ตรวจ `competition_rule_coverage.json`, `competition_rule_fact_projections.jsonl` และ evidence status; Fact ที่เป็น candidate/document-level ต้องได้รับ owner review ก่อน.",
        "4. เติมวันที่มีผลและ approval ที่ hash ตรงกันใน `release_overrides.jsonl`; ห้ามแก้ generated registry โดยตรง.",
        "5. สร้าง Structured/RAG projection จาก active release เดียวกัน แล้วจึงสลับ runtime แบบ atomic.",
    ])
    return "\n".join(lines) + "\n"


def readme_markdown() -> str:
    return """# Canonical Competition Rule Format\n\nโฟลเดอร์นี้เป็น **canonical layer** ของกติกาการแข่งขัน: เก็บกติกาเดิมในรูปแบบกลางที่อ่านได้เหมือนกันทุกเกม โดยไม่แทนที่ source chunks หรือ fact cards ที่ runtime ปัจจุบันใช้.\n\n## ไฟล์\n\n- `rulebook_registry.jsonl` - metadata ระดับเอกสาร/รายการแข่งขัน\n- `competition_rule_releases.jsonl` - release lifecycle, approval และ eligibility ของแต่ละ rulebook\n- `competition_rule_records.jsonl` - กติกาแต่ละส่วนจาก RAG chunks พร้อม conditions, rule type และ source locator\n- `competition_rule_fact_projections.jsonl` - คำตอบ structured พร้อม evidence links และสถานะการตรวจหลักฐาน\n- `competition_rule_rag_projections.jsonl` - text สำหรับ RAG ที่เติมชื่อเกม รายการ และบริบทให้ครบ\n- `en_localization_review_queue.jsonl` - รายการข้อความที่ยังต้องมี English localization ที่อนุมัติแล้ว\n- `active_release_manifest.json` - release ที่ Runtime อนุญาตให้อ่านได้\n- `release_overrides.jsonl` และ `release_override_template.json` - owner-controlled approval/effective date overlay\n- `competition_rule_coverage.json` และ `competition_rule_coverage_report.md` - ความครอบคลุมและรายการที่ต้องตรวจ\n- `competition_rule_submission_template.json` - แบบฟอร์มเพิ่ม rulebook ใหม่ พร้อม common sections และ optional modules\n\n## Schema กลาง\n\nทุก Rule Record มี `rulebook_id`, `game_id`, `scope`, `canonical_section`, `module`, `facet`, `rule_type`, `conditions`, `content_th`, source locator และ hash ของข้อความต้นทาง. หัวข้อกลางมี 10 ส่วน: `rulebook_identity`, `eligibility_registration`, `competition_format`, `match_configuration`, `pre_match_on_site`, `in_match_operations`, `fair_play_conduct`, `penalty_matrix`, `protest_dispute`, และ `references_change_history`.\n\n`module=common` ใช้ซ้ำได้ทุกเกม ส่วน module อื่นเป็น optional game-specific module เช่น map veto ของ CS2 หรือ Hero/Skin ของ RoV. ห้ามสร้าง runtime route ตามชื่อเกม; route ควรเลือก `competition_rules` แล้ว filter จาก `game_id`, `canonical_section`, `module`, `facet`, conditions, วันที่มีผล และ source trust.\n\n## สถานะและการ publish\n\nข้อมูลที่ย้ายจาก runtime เดิมถูกติดสถานะ `migrated_from_existing_content` และ `pending_owner_review` เพื่อไม่อ้างว่าได้รับ human approval ใหม่. Release จะเป็น `runtime_eligible` ได้ก็ต่อเมื่อ owner approval มี source hash ที่ตรงกัน, มี `effective_from` และตั้ง `activation_status=active` ใน `release_overrides.jsonl`. ถ้า source เปลี่ยน hash จะไม่สามารถ publish ต่อได้จนกว่าจะ review ใหม่. Structured facts และ RAG chunks ต้องใช้ active release/version เดียวกันและสลับพร้อมกัน.\n\nFact card ที่ไม่ได้มีข้อความตรงกับ source chunk จะถูกติด `candidate_review_required` หรือ `document_level_only`; ห้ามตีความว่าเป็นหลักฐานยืนยันจนกว่าจะ review.\n\n## สร้าง/ตรวจ\n\n```powershell\npy -3 tools/build_competition_rule_canonical.py --write\npy -3 tools/build_competition_rule_canonical.py --check\n```\n"""


def write_outputs(model: dict[str, Any]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_jsonl(OUT_DIR / "rulebook_registry.jsonl", model["registry"])
    write_jsonl(OUT_DIR / "competition_rule_releases.jsonl", model["releases"])
    write_jsonl(OUT_DIR / "competition_rule_records.jsonl", model["records"])
    write_jsonl(OUT_DIR / "competition_rule_fact_projections.jsonl", model["facts_projection"])
    write_jsonl(OUT_DIR / "competition_rule_rag_projections.jsonl", model["rag_projections"])
    write_jsonl(OUT_DIR / "en_localization_review_queue.jsonl", model["en_localization_queue"])
    write_jsonl(OUT_DIR / "fact_evidence_review_queue.jsonl", model["fact_evidence_review_queue"])
    write_jsonl(OUT_DIR / "release_owner_review_queue.jsonl", model["release_owner_review_queue"])
    (OUT_DIR / "competition_rule_coverage.json").write_text(
        json.dumps(model["coverage"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (OUT_DIR / "competition_rule_coverage_report.md").write_text(report_markdown(model), encoding="utf-8")
    (OUT_DIR / "README.md").write_text(readme_markdown(), encoding="utf-8")
    submission_template = {
        "schema_version": SCHEMA_VERSION,
        "release": {
            "release_id": "competition_rules_<game>_<event>_<yyyy>",
            "status": "draft",
            "scope": "tournament_specific",
            "game_id": "<game_slug>",
            "game": "<official_game_name>",
            "tournament": "<official_event_name>",
            "effective_from": "<ISO-8601 date or null>",
            "effective_to": "<ISO-8601 date or null>",
            "source_url": "<official_source_url_or_local_reference>",
            "owner_review": {"status": "pending", "reviewed_by": None, "reviewed_at": None},
        },
        "common_sections": {code: [] for code, _label in CORE_SECTIONS},
        "optional_game_modules": [{
            "module": "<game_specific_module_slug>",
            "module_label_th": "<ชื่อโมดูลเฉพาะเกม>",
            "rules": [],
        }],
        "rule_record_shape": {
            "facet": "<stable_facet_name>",
            "title_th": "<หัวข้อกติกา>",
            "content_th": "<ข้อความกติกาเต็มจากต้นทาง>",
            "source_text_sha256": "<sha256 of content_th>",
            "source_reference": "<section/page/heading in the source>",
        },
    }
    (OUT_DIR / "competition_rule_submission_template.json").write_text(
        json.dumps(submission_template, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    release_override_template = {
        "rulebook_id": "<rulebook_id from rulebook_registry.jsonl>",
        "review_status": "approved",
        "approved_by": "<owner identifier>",
        "approved_at": "<ISO-8601 timestamp>",
        "approved_source_document_sha256": "<current source_document_sha256>",
        "effective_from": "<ISO-8601 date>",
        "effective_to": None,
        "supersedes_rulebook_id": None,
        "activation_status": "active",
    }
    (OUT_DIR / "release_override_template.json").write_text(
        json.dumps(release_override_template, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    if not RELEASE_OVERRIDES_PATH.exists():
        RELEASE_OVERRIDES_PATH.write_text("", encoding="utf-8")
    active_manifest = {
        "schema_version": SCHEMA_VERSION,
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "active_release_ids": [row["release_id"] for row in model["releases"] if row["runtime_eligible"]],
        "selection_policy": "Only active, owner-approved releases with a matching source hash and effective_from date may be loaded by runtime.",
        "safe_behavior_when_empty": "Ask for tournament context or return no-answer; do not infer a current rule from an inactive release.",
    }
    (OUT_DIR / "active_release_manifest.json").write_text(
        json.dumps(active_manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def validate(model: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = {
        "rule_id", "rulebook_id", "game_id", "canonical_section", "module", "content_th",
        "source_chunk_id", "source_text_sha256", "source_locator", "conditions", "rule_type",
    }
    records = model["records"]
    release_ids = {row["release_id"] for row in model["releases"]}
    if len(release_ids) != len(model["releases"]):
        errors.append("Release IDs are duplicated.")
    source_ids = [row["source_chunk_id"] for row in records]
    if len(source_ids) != len(set(source_ids)):
        errors.append("Canonical rule records contain duplicate source_chunk_id values.")
    if len(records) != model["source_counts"]["chunks"]:
        errors.append("Canonical record count does not match source chunk count.")
    for row in records:
        missing = required - row.keys()
        if missing:
            errors.append(f"{row.get('rule_id', '<unknown>')} is missing {sorted(missing)}.")
        if row["source_text_sha256"] != text_hash(row["content_th"]):
            errors.append(f"{row['rule_id']} has a source hash mismatch.")
        if row["rulebook_id"] not in release_ids:
            errors.append(f"{row['rule_id']} references an unknown release.")
    fact_ids = [str(row.get("fact_id")) for row in model["facts_projection"]]
    if len(fact_ids) != len(set(fact_ids)):
        errors.append("Fact projection IDs are duplicated across source card files.")
    valid_evidence_statuses = {
        "verified_direct", "declared_chunk_reference_pending_text_check",
        "candidate_review_required", "document_level_only",
    }
    for fact in model["facts_projection"]:
        if fact["evidence_status"] not in valid_evidence_statuses:
            errors.append(f"{fact['fact_id']} has an invalid evidence status.")
        if fact["evidence_status"] != "document_level_only" and not fact["evidence_links"]:
            errors.append(f"{fact['fact_id']} has an evidence status without a link.")
        if any(release_id not in release_ids for release_id in fact["release_ids"]):
            errors.append(f"{fact['fact_id']} references an unknown release.")
    for projection in model["rag_projections"]:
        if projection["release_id"] not in release_ids:
            errors.append(f"{projection['chunk_id']} references an unknown release.")
    return errors


def check_existing(model: dict[str, Any]) -> list[str]:
    errors = validate(model)
    expected_paths = {
        "rulebook_registry.jsonl": model["registry"],
        "competition_rule_releases.jsonl": model["releases"],
        "competition_rule_records.jsonl": model["records"],
        "competition_rule_fact_projections.jsonl": model["facts_projection"],
        "competition_rule_rag_projections.jsonl": model["rag_projections"],
        "en_localization_review_queue.jsonl": model["en_localization_queue"],
        "fact_evidence_review_queue.jsonl": model["fact_evidence_review_queue"],
        "release_owner_review_queue.jsonl": model["release_owner_review_queue"],
    }
    for filename, expected in expected_paths.items():
        path = OUT_DIR / filename
        actual = read_jsonl(path)
        if actual != expected:
            errors.append(f"{filename} is stale or missing; run with --write.")
    coverage_path = OUT_DIR / "competition_rule_coverage.json"
    if not coverage_path.exists():
        errors.append("competition_rule_coverage.json is missing; run with --write.")
    else:
        actual_coverage = json.loads(coverage_path.read_text(encoding="utf-8"))
        # generated_at changes on every build, so compare the content that matters.
        actual_coverage.pop("generated_at_utc", None)
        expected_coverage = dict(model["coverage"])
        expected_coverage.pop("generated_at_utc", None)
        if actual_coverage != expected_coverage:
            errors.append("competition_rule_coverage.json is stale; run with --write.")
    if not (OUT_DIR / "competition_rule_submission_template.json").exists():
        errors.append("competition_rule_submission_template.json is missing; run with --write.")
    if not (OUT_DIR / "release_override_template.json").exists():
        errors.append("release_override_template.json is missing; run with --write.")
    if not RELEASE_OVERRIDES_PATH.exists():
        errors.append("release_overrides.jsonl is missing; run with --write.")
    if not (OUT_DIR / "active_release_manifest.json").exists():
        errors.append("active_release_manifest.json is missing; run with --write.")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="Generate the canonical files.")
    mode.add_argument("--check", action="store_true", help="Validate source data and generated files.")
    args = parser.parse_args()
    model = build()
    errors = validate(model)
    if errors:
        print("Validation failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    if args.write:
        write_outputs(model)
        print(
            "Generated canonical competition-rule data: "
            f"{model['source_counts']['documents']} rulebooks, "
            f"{model['source_counts']['chunks']} rule records, "
            f"{model['source_counts']['facts']} fact projections."
        )
        return 0
    errors = check_existing(model)
    if errors:
        print("Check failed:", file=sys.stderr)
        print("\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1
    print("Canonical competition-rule data is current and valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
