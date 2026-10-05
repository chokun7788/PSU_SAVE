#!/usr/bin/env python3
"""Build a RAG-first bilingual ground-truth suite for the four rulebooks.

The suite intentionally evaluates evidence targeting, not a frozen response
sentence. Every positive case identifies the rulebook, game, facet and a set
of canonical evidence records that are valid for the answer.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CANONICAL_PATH = ROOT / "data" / "competition_rules" / "canonical" / "competition_rule_records.jsonl"
FACT_PATH = ROOT / "data" / "competition_rules" / "canonical" / "competition_rule_fact_projections.jsonl"
SOURCE_CHUNKS_PATH = ROOT / "data" / "competition_rules" / "competition_rule_chunks.jsonl"
SOURCE_COVERAGE_PATH = ROOT / "data" / "competition_rules" / "source_coverage_manifest.jsonl"
OUT_DIR = ROOT / "data" / "eval"
OUT_PATH = OUT_DIR / "competition_rules_rag_ground_truth_v1.jsonl"
REPORT_PATH = OUT_DIR / "competition_rules_rag_ground_truth_v1_report.md"
MANIFEST_PATH = OUT_DIR / "competition_rules_rag_ground_truth_v1_manifest.json"
SUITE = "competition_rules_rag_ground_truth_v1"

sys.path.insert(0, str(ROOT))
from app.pipeline.competition_source_facets import source_row_supports_facet  # noqa: E402

GAME_ALIASES = {
    "cs2": {"th": ("CS2", "Counter-Strike 2", "เคาน์เตอร์สไตรก์ 2"), "en": ("CS2", "Counter-Strike 2", "Counter Strike 2")},
    "rov": {"th": ("RoV", "Arena of Valor", "อารีน่าออฟเวเลอร์"), "en": ("RoV", "Arena of Valor", "AOV")},
    "tekken8": {"th": ("TEKKEN 8", "Tekken 8", "เทคเค่น 8"), "en": ("TEKKEN 8", "Tekken 8", "T8")},
    "valorant": {"th": ("VALORANT", "Valorant", "วาโล"), "en": ("VALORANT", "Valorant", "Valo")},
}

FACET_TOPIC = {
    "competition_format": ("รูปแบบการแข่งขัน", "the competition format"),
    "conduct": ("มารยาทและพฤติกรรมผู้เล่น", "player conduct and sportsmanship"),
    "disconnect": ("การหลุดจากเกมหรือการเชื่อมต่อ", "disconnections and reconnects"),
    "dispute": ("การประท้วงและข้อพิพาท", "protests and disputes"),
    "eligibility_registration": ("คุณสมบัติ รายชื่อผู้เล่น และการลงทะเบียน", "eligibility, roster, and registration"),
    "equipment": ("อุปกรณ์ที่ใช้แข่งขัน", "competition equipment and devices"),
    "fair_play_conduct": ("fair play และข้อห้าม", "fair play and prohibited conduct"),
    "in_match_operations": ("ขั้นตอนระหว่างการแข่งขัน", "in-match procedure"),
    "map_pool": ("แผนที่และการเลือกแผนที่", "maps, vetoes, and map selection"),
    "match_configuration": ("เวอร์ชันเกมและการตั้งค่าแมตช์", "game version and match configuration"),
    "match_settings": ("การตั้งค่าในเกม", "in-game settings"),
    "pause_timeout": ("การ pause และ timeout", "pauses and timeouts"),
    "penalty": ("บทลงโทษ", "penalties"),
    "penalty_matrix": ("ตารางบทลงโทษ", "the penalty matrix"),
    "pre_match_on_site": ("ข้อกำหนดก่อนแข่งและหน้างาน", "pre-match and on-site requirements"),
    "protest_dispute": ("การแก้ปัญหาข้อพิพาท", "dispute resolution"),
    "registration": ("การสมัครและการลงทะเบียน", "registration"),
    "rulebook_identity": ("ขอบเขตและข้อมูลของรายการ", "the rulebook scope and tournament identity"),
    "schedule": ("ตารางและเวลาแข่งขัน", "the tournament schedule"),
    "team_size": ("จำนวนผู้เล่นต่อทีม", "team size"),
}

# Stable evaluation matrix.  The previous builder inferred this matrix from
# unreviewed migration metadata, which made incorrect labels become Gold
# truth.  The questions remain stable, while allowed evidence is now derived
# from literal source chunks through the same conservative classifier used by
# runtime retrieval.
GAME_FACETS = {
    "cs2": (
        "competition_format", "conduct", "dispute", "eligibility_registration", "equipment",
        "fair_play_conduct", "in_match_operations", "map_pool", "match_configuration",
        "match_settings", "pause_timeout", "penalty", "penalty_matrix", "pre_match_on_site",
        "protest_dispute", "registration", "rulebook_identity", "schedule", "team_size",
    ),
    "rov": (
        "competition_format", "disconnect", "equipment", "pause_timeout", "pre_match_on_site",
        "registration", "rulebook_identity", "team_size",
    ),
    "tekken8": (
        "competition_format", "conduct", "dispute", "equipment", "match_settings",
        "protest_dispute", "rulebook_identity",
    ),
    "valorant": (
        "conduct", "equipment", "fair_play_conduct", "in_match_operations", "map_pool",
        "pause_timeout", "penalty", "pre_match_on_site", "team_size",
    ),
}

RULEBOOKS = {
    "cs2": ("competition_rules_cs2_psu_phuket_2026", "Counter-Strike 2"),
    "rov": ("competition_rules_rov_blueket_2025_men", "Arena of Valor (RoV)"),
    "tekken8": ("competition_rules_tekken8_psu_esports", "Tekken 8"),
    "valorant": ("competition_rules_valorant_psu_phuket_2026", "VALORANT"),
}
FACT_FACET_ALIASES = {
    "competition_format": {"competition_format", "format"},
    "conduct": {"conduct", "sportsmanship"},
    "disconnect": {"disconnect", "reconnect"},
    "dispute": {"dispute", "protest"},
    "eligibility_registration": {"eligibility_registration", "eligibility", "registration", "roster"},
    "equipment": {"equipment", "device"},
    "fair_play_conduct": {"fair_play_conduct", "fair_play", "conduct"},
    "in_match_operations": {"in_match_operations", "match_operations"},
    "map_pool": {"map_pool", "map", "map_veto"},
    "match_configuration": {"match_configuration", "configuration"},
    "match_settings": {"match_settings", "settings"},
    "pause_timeout": {"pause_timeout", "pause", "timeout"},
    "penalty": {"penalty", "penalties"},
    "penalty_matrix": {"penalty_matrix", "penalty"},
    "pre_match_on_site": {"pre_match_on_site", "checkin", "on_site"},
    "protest_dispute": {"protest_dispute", "dispute", "protest"},
    "registration": {"registration"},
    "rulebook_identity": {"rulebook_identity", "identity"},
    "schedule": {"schedule"},
    "team_size": {"team_size", "roster"},
}

TH_TEMPLATES = (
    "กติกา {game} เรื่อง{topic} ว่าอย่างไร",
    "{game} แข่งจริง กฎเกี่ยวกับ{topic} เป็นแบบไหน",
    "ขออ้างอิงกติกา {game} ในหัวข้อ{topic} หน่อย",
    "กำลังจะลงแข่ง {game} อยากรู้เรื่อง{topic}",
    "{game} มีข้อกำหนดเรื่อง{topic} ไหม",
    "ตาม rulebook {game} {topic} ต้องทำยังไง",
)
EN_TEMPLATES = (
    "What do the {game} tournament rules say about {topic}?",
    "For {game}, can you verify the rule on {topic}?",
    "I am preparing for a {game} match. What is the policy for {topic}?",
    "Please retrieve the official {game} rulebook evidence for {topic}.",
    "How is {topic} handled in the {game} tournament rules?",
    "Could you cite the {game} rule concerning {topic}?",
)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def question_key(value: str) -> str:
    return re.sub(r"\s+", " ", value.casefold()).strip()


def topic_for(facet: str) -> tuple[str, str]:
    return FACET_TOPIC.get(facet, (facet.replace("_", " "), facet.replace("_", " ")))


def positive_rows(chunks: list[dict[str, Any]], facts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    del facts  # Fact-card links are not source Gold until their review is complete.
    coverage_rows = read_jsonl(SOURCE_COVERAGE_PATH)
    unsupported = {
        (str(row.get("game_id") or ""), str(row.get("facet") or ""))
        for row in coverage_rows
        if str(row.get("status") or "") == "unsupported_in_active_source"
    }
    rows: list[dict[str, Any]] = []
    counters = Counter()
    for game_id, facets in GAME_FACETS.items():
        rulebook_id, _game_label = RULEBOOKS[game_id]
        game_chunks = [row for row in chunks if str(row.get("document_id")) == rulebook_id]
        for facet in facets:
            facet_records = [row for row in game_chunks if source_row_supports_facet(row, facet)]
            manifest_facet = "conduct" if facet == "fair_play_conduct" else facet
            if (game_id, manifest_facet) in unsupported and not facet_records:
                facet_records = []
            th_topic, en_topic = topic_for(facet)
            allowed_rule_ids = sorted(f"canonical::{row['id']}" for row in facet_records)
            answer_available = bool(allowed_rule_ids)
            for locale, templates, topic in (("th", TH_TEMPLATES, th_topic), ("en", EN_TEMPLATES, en_topic)):
                aliases = GAME_ALIASES[game_id][locale]
                for index, template in enumerate(templates):
                    counters[locale] += 1
                    game_alias = aliases[index % len(aliases)]
                    question = template.format(game=game_alias, topic=topic)
                    rows.append({
                        "id": f"COMP-RAG-{locale.upper()}-{counters[locale]:03d}",
                        "suite": SUITE,
                        "locale": locale,
                        "case_type": "facet_targeted_retrieval",
                        "question_style": ("direct" if index == 0 else "contextual" if index in {2, 3} else "natural_variant"),
                        "question": question,
                        "expected_route_categories": ["competition_rules"] if answer_available else ["competition_rules", "no_answer"],
                        "expected_answer_status": "answer_available" if answer_available else "no_answer_expected",
                        "rag_required": answer_available,
                        "target_locked": True,
                        "expected_game_id": game_id,
                        "expected_rulebook_ids": [rulebook_id],
                        "expected_facet": facet,
                        "allowed_evidence_rule_ids": allowed_rule_ids,
                        "allowed_evidence_fact_ids": [],
                        "allowed_source_urls": sorted({str(record.get("source_url") or "") for record in facet_records if record.get("source_url")}),
                        "evidence_statuses": ["pending_owner_review"] if answer_available else ["unsupported_in_active_source"],
                        "answer_language_requirement": "source_grounded_th" if locale == "th" else "source_grounded_en_or_translation_pending",
                        "review_status": "retrieval_gold_candidate",
                        "latency_ceiling_sec": 20.0,
                    })
    return rows


def adversarial_rows(start_th: int, start_en: int) -> list[dict[str, Any]]:
    cases = (
        ("th", "clarification_required", "กติกา timeout เป็นยังไง", ["competition_rules", "clarification"], "", [], "missing_game"),
        ("th", "clarification_required", "แข่งทีมละกี่คนอะ", ["competition_rules", "clarification"], "", [], "missing_game"),
        ("th", "no_answer_expected", "Dota 2 แข่งตามกติกาศูนย์นี้ pause ได้กี่ครั้ง", ["competition_rules", "no_answer"], "dota2", [], "unknown_game"),
        ("th", "no_answer_expected", "กติกา Free Fire ของรายการนี้เรื่องโกงว่าไง", ["competition_rules", "no_answer"], "freefire", [], "unknown_game"),
        ("th", "answer_available", "CS2 กับ VALORANT เรื่อง technical pause ต่างกันยังไง", ["competition_rules"], "multi", ["cs2", "valorant"], "comparison"),
        ("th", "answer_available", "RoV กับ Tekken 8 ถ้ากด pause ผิดมีผลยังไง", ["competition_rules"], "multi", ["rov", "tekken8"], "comparison"),
        ("en", "clarification_required", "What are the timeout rules?", ["competition_rules", "clarification"], "", [], "missing_game"),
        ("en", "clarification_required", "How many players can a team have?", ["competition_rules", "clarification"], "", [], "missing_game"),
        ("en", "no_answer_expected", "What are the Dota 2 tournament rules for pauses here?", ["competition_rules", "no_answer"], "dota2", [], "unknown_game"),
        ("en", "no_answer_expected", "Does this studio have Free Fire anti-cheat tournament rules?", ["competition_rules", "no_answer"], "freefire", [], "unknown_game"),
        ("en", "answer_available", "How do CS2 and VALORANT technical pause rules differ?", ["competition_rules"], "multi", ["cs2", "valorant"], "comparison"),
        ("en", "answer_available", "Compare the pause penalty rules for RoV and TEKKEN 8.", ["competition_rules"], "multi", ["rov", "tekken8"], "comparison"),
    )
    rows: list[dict[str, Any]] = []
    counters = {"th": start_th, "en": start_en}
    for locale, status, question, categories, game_id, game_ids, style in cases:
        counters[locale] += 1
        rulebooks = {
            "cs2": "competition_rules_cs2_psu_phuket_2026",
            "rov": "competition_rules_rov_blueket_2025_men",
            "tekken8": "competition_rules_tekken8_psu_esports",
            "valorant": "competition_rules_valorant_psu_phuket_2026",
        }
        rows.append({
            "id": f"COMP-RAG-{locale.upper()}-{counters[locale]:03d}",
            "suite": SUITE,
            "locale": locale,
            "case_type": "adversarial_safe_outcome" if status != "answer_available" else "cross_rulebook_comparison",
            "question_style": style,
            "question": question,
            "expected_route_categories": categories,
            "expected_answer_status": status,
            "rag_required": status == "answer_available",
            "target_locked": status != "clarification_required",
            "expected_game_id": game_id,
            "expected_rulebook_ids": [rulebooks[item] for item in game_ids],
            "expected_facet": "pause_timeout" if game_ids else "",
            "allowed_evidence_rule_ids": [],
            "allowed_source_urls": [],
            "evidence_statuses": ["pending_owner_review"] if game_ids else [],
            "answer_language_requirement": "source_grounded_th" if locale == "th" else "source_grounded_en_or_translation_pending",
            "review_status": "retrieval_gold_candidate",
            "latency_ceiling_sec": 20.0,
        })
    return rows


SOURCE_GAP_CASES = (
    {
        "game_id": "rov",
        "facet": "pre_match_on_site",
        "th": "แข่ง RoV ต้องมาถึงสนามก่อนเวลาแข่งอย่างน้อยกี่นาที",
        "en": "How many minutes before a RoV match must a team arrive at the venue?",
    },
    {
        "game_id": "rov",
        "facet": "pre_match_on_site",
        "th": "ไปถึงหน้างานแข่ง RoV แล้วต้องเช็กอินหรือรายงานตัวตามขั้นตอนอะไรบ้าง",
        "en": "What is the on-site check-in procedure after arriving for a RoV match?",
    },
    {
        "game_id": "valorant",
        "facet": "team_size",
        "th": "ทีม VALORANT ต้องส่งผู้เล่นตัวจริงลงแข่งกี่คน",
        "en": "How many starting players must a VALORANT team field?",
    },
    {
        "game_id": "valorant",
        "facet": "roster_composition",
        "th": "ทีม VALORANT ลงทะเบียนตัวสำรองได้กี่คน",
        "en": "How many substitute players may a VALORANT team register?",
    },
    {
        "game_id": "valorant",
        "facet": "eligibility_registration",
        "th": "รายการ VALORANT กำหนดอายุขั้นต่ำของผู้สมัครไว้เท่าไร",
        "en": "What is the minimum age requirement to enter this VALORANT tournament?",
    },
    {
        "game_id": "valorant",
        "facet": "registration",
        "th": "รายการ VALORANT ปิดรับรายชื่อทีมวันและเวลาใด",
        "en": "What is the roster registration deadline for this VALORANT tournament?",
    },
    {
        "game_id": "valorant",
        "facet": "conduct",
        "th": "ถ้าผู้เล่น VALORANT พูดหยาบหรือแสดงพฤติกรรมไม่เหมาะสมจะโดนโทษอะไร",
        "en": "What penalty applies to profanity or inappropriate conduct in VALORANT?",
    },
    {
        "game_id": "valorant",
        "facet": "fair_play_conduct",
        "th": "กติกา VALORANT กำหนดเรื่องน้ำใจนักกีฬาไว้อย่างไร",
        "en": "What do the VALORANT rules require for sportsmanship and fair play?",
    },
    {
        "game_id": "valorant",
        "facet": "in_match_operations",
        "th": "ถ้ามีปัญหาทั่วไประหว่างแข่ง VALORANT ผู้เล่นต้องติดต่อใคร",
        "en": "Who should a player contact for a general issue during a VALORANT match?",
    },
    {
        "game_id": "valorant",
        "facet": "in_match_operations",
        "th": "ถ้าเกิดเหตุที่ไม่ได้ระบุไว้ระหว่างแข่ง VALORANT กรรมการต้องดำเนินการตามขั้นตอนอะไร",
        "en": "What procedure must officials follow for an unspecified incident during a VALORANT match?",
    },
)


def source_gap_rows(start_th: int, start_en: int) -> list[dict[str, Any]]:
    coverage = {
        (str(row.get("game_id") or ""), str(row.get("facet") or "")): row
        for row in read_jsonl(SOURCE_COVERAGE_PATH)
        if str(row.get("status") or "") == "unsupported_in_active_source"
    }
    counters = {"th": start_th, "en": start_en}
    rows: list[dict[str, Any]] = []
    for case in SOURCE_GAP_CASES:
        game_id = str(case["game_id"])
        facet = str(case["facet"])
        manifest_facet = "conduct" if facet == "fair_play_conduct" else facet
        manifest = coverage.get((game_id, manifest_facet), {})
        rulebook_id = RULEBOOKS[game_id][0]
        for locale in ("th", "en"):
            counters[locale] += 1
            rows.append({
                "id": f"COMP-RAG-{locale.upper()}-{counters[locale]:03d}",
                "suite": SUITE,
                "locale": locale,
                "case_type": "source_gap_safe_no_answer",
                "question_style": "human_written_source_gap",
                "question": str(case[locale]),
                "expected_route_categories": ["competition_rules", "no_answer"],
                "expected_answer_status": "no_answer_expected",
                "rag_required": False,
                "target_locked": True,
                "expected_game_id": game_id,
                "expected_rulebook_ids": [rulebook_id],
                "expected_facet": facet,
                "allowed_evidence_rule_ids": [],
                "allowed_evidence_fact_ids": [],
                "allowed_source_urls": [],
                "evidence_statuses": ["unsupported_in_active_source"],
                "source_gap_manifest_key": f"{game_id}:{manifest_facet}",
                "source_gap_reason": str(manifest.get("reason") or ""),
                "answer_language_requirement": "safe_no_answer_th" if locale == "th" else "safe_no_answer_en",
                "review_status": "source_gap_negative_gold",
                "latency_ceiling_sec": 20.0,
            })
    return rows


def build_rows() -> list[dict[str, Any]]:
    chunks = read_jsonl(SOURCE_CHUNKS_PATH)
    facts = read_jsonl(FACT_PATH)
    positive = positive_rows(chunks, facts)
    adversarial = adversarial_rows(
        sum(row["locale"] == "th" for row in positive),
        sum(row["locale"] == "en" for row in positive),
    )
    base = positive + adversarial
    return base + source_gap_rows(
        sum(row["locale"] == "th" for row in base),
        sum(row["locale"] == "en" for row in base),
    )


def validate(rows: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    if len(rows) < 500:
        errors.append(f"Expected at least 500 cases, found {len(rows)}.")
    ids = [str(row.get("id")) for row in rows]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate IDs found.")
    required = {
        "id", "suite", "locale", "case_type", "question", "expected_route_categories",
        "expected_answer_status", "rag_required", "target_locked", "expected_rulebook_ids",
        "expected_facet", "allowed_evidence_rule_ids", "review_status", "latency_ceiling_sec",
    }
    for locale in ("th", "en"):
        locale_rows = [row for row in rows if row.get("locale") == locale]
        if len(locale_rows) < 250:
            errors.append(f"Expected at least 250 {locale} cases, found {len(locale_rows)}.")
        keys = [question_key(str(row.get("question", ""))) for row in locale_rows]
        if len(keys) != len(set(keys)):
            errors.append(f"Duplicate normalized questions found for locale={locale}.")
    for row in rows:
        missing = required - row.keys()
        if missing:
            errors.append(f"{row.get('id')} missing {sorted(missing)}.")
        if row.get("suite") != SUITE:
            errors.append(f"{row.get('id')} has the wrong suite.")
        if row.get("rag_required") and not row.get("expected_rulebook_ids"):
            errors.append(f"{row.get('id')} requires RAG but does not name a rulebook.")
        if (
            row.get("case_type") == "facet_targeted_retrieval"
            and row.get("expected_answer_status") == "answer_available"
            and not row.get("allowed_evidence_rule_ids")
        ):
            errors.append(f"{row.get('id')} has no allowed evidence IDs for an answerable case.")
        if row.get("case_type") == "source_gap_safe_no_answer":
            if row.get("expected_answer_status") != "no_answer_expected":
                errors.append(f"{row.get('id')} source-gap case must expect no-answer.")
            if row.get("rag_required"):
                errors.append(f"{row.get('id')} source-gap case must not require RAG evidence.")
            if row.get("allowed_evidence_rule_ids") or row.get("allowed_evidence_fact_ids"):
                errors.append(f"{row.get('id')} source-gap case must not allow evidence IDs.")
            if not row.get("target_locked") or not row.get("expected_rulebook_ids"):
                errors.append(f"{row.get('id')} source-gap case must lock its target rulebook.")
            if not row.get("source_gap_manifest_key") or not row.get("source_gap_reason"):
                errors.append(f"{row.get('id')} source-gap case is not bound to a coverage-manifest reason.")
    games = {game_id for row in rows for game_id in ([row.get("expected_game_id")] if row.get("expected_game_id") else [])}
    for expected in GAME_ALIASES:
        if expected not in games:
            errors.append(f"No positive target case exists for {expected}.")
    return errors


def report(rows: list[dict[str, Any]]) -> str:
    by_locale = Counter(row["locale"] for row in rows)
    by_game = Counter(row["expected_game_id"] or "multi_or_unspecified" for row in rows)
    by_facet = Counter(row["expected_facet"] or "safe_outcome" for row in rows)
    return "\n".join([
        "# Competition Rules RAG Ground Truth v1",
        "",
        "ชุดนี้แยกจาก `rag_robustness_ground_truth_v1` และทดสอบเฉพาะกติกา CS2, RoV, TEKKEN 8 และ VALORANT.",
        "ทุก positive case ล็อก game, rulebook, facet และ canonical rule IDs ที่อนุญาตให้ RAG ใช้เป็นหลักฐาน.",
        "",
        f"- Total: {len(rows)}",
        f"- Thai: {by_locale['th']}",
        f"- English: {by_locale['en']}",
        "- Current canonical records remain `pending_owner_review`; this suite is retrieval gold candidate, not a release-approval bypass.",
        "",
        "## Game Coverage",
        "",
        *[f"- `{game}`: {count}" for game, count in sorted(by_game.items())],
        "",
        "## Facet Coverage",
        "",
        *[f"- `{facet}`: {count}" for facet, count in sorted(by_facet.items())],
        "",
        "## Evaluation Contract",
        "",
        "- Positive case: route must be `competition_rules`; retrieval must stay in the named rulebook and facet; returned evidence must intersect `allowed_evidence_fact_ids` (legacy fact-card path) or `allowed_evidence_rule_ids` (canonical RAG path).",
        "- Cross-rulebook comparison: retrieve evidence from every named rulebook; do not use one game to answer the other.",
        "- Missing game: ask for the game or tournament; do not guess from a similarly named fact.",
        "- Unknown game: return a safe no-answer; do not substitute CS2/RoV/TEKKEN 8/VALORANT.",
        "- Known source gap: return a safe no-answer with no attached evidence; do not borrow another facet or game.",
    ]) + "\n"


def write(rows: list[dict[str, Any]]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text("\n".join(json.dumps(row, ensure_ascii=False, sort_keys=True) for row in rows) + "\n", encoding="utf-8")
    REPORT_PATH.write_text(report(rows), encoding="utf-8")
    digest = hashlib.sha256(OUT_PATH.read_bytes()).hexdigest()
    manifest = {
        "suite": SUITE,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "total": len(rows),
        "locale_counts": dict(Counter(row["locale"] for row in rows)),
        "sha256": digest,
        "source": str(SOURCE_CHUNKS_PATH),
        "source_sha256": hashlib.sha256(SOURCE_CHUNKS_PATH.read_bytes()).hexdigest(),
        "fact_projection_source": str(FACT_PATH),
        "fact_projection_source_sha256": hashlib.sha256(FACT_PATH.read_bytes()).hexdigest(),
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build four-rulebook RAG ground truth.")
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rows = build_rows()
    errors = validate(rows)
    if errors:
        print("Ground truth validation failed:\n- " + "\n- ".join(errors))
        return 1
    if args.write:
        write(rows)
        print(f"Generated {len(rows)} competition-rule RAG cases at {OUT_PATH}")
    if args.check or not args.write:
        print(f"Competition-rule RAG ground truth is valid: {len(rows)} cases.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
