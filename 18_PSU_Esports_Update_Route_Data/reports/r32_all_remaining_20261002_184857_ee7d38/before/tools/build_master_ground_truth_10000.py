#!/usr/bin/env python3
"""Build a deterministic bilingual master ground-truth candidate corpus.

The corpus distinguishes static answer contracts from live lookups and safe
outcomes. Generated paraphrases remain review candidates; the builder never
promotes machine-generated text to human-approved Gold.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
EVAL = DATA / "eval"
SUITE = "psu_esports_master_ground_truth_candidate_v2"
TH_PATH = EVAL / "master_ground_truth_th_5000_v2.jsonl"
EN_PATH = EVAL / "master_ground_truth_en_5000_v2.jsonl"
COMBINED_PATH = EVAL / "master_ground_truth_bilingual_10000_v2.jsonl"
MANIFEST_PATH = EVAL / "master_ground_truth_bilingual_10000_v2_manifest.json"
REPORT_PATH = EVAL / "master_ground_truth_bilingual_10000_v2_report.md"

DOMAIN_TARGETS = {
    "service_fee": 400,
    "reservation_policy": 450,
    "live_booking": 400,
    "schedule_calendar": 350,
    "games_catalog_availability": 600,
    "game_detail": 450,
    "game_controls": 650,
    "equipment": 350,
    "studio_rules_penalties": 350,
    "competition_rules": 500,
    "members_overview_contact": 250,
    "compound_context_boundary": 250,
}
assert sum(DOMAIN_TARGETS.values()) == 5000

SOURCE_PATHS = {
    "thai_benchmark": EVAL / "model_benchmark_1500.jsonl",
    "english_shadow": EVAL / "english_shadow_1600_machine_20260908.jsonl",
    "english_gold": EVAL / "english_gold_400_20260902.jsonl",
    "rag_robustness": EVAL / "rag_robustness_ground_truth_v1.jsonl",
    "competition": EVAL / "competition_rules_rag_ground_truth_v1.jsonl",
    "real_usage": EVAL / "real_usage_golden_v1.jsonl",
    "rules": DATA / "curated" / "rule_patterns.jsonl",
    "game_details": DATA / "curated" / "game_item_details.jsonl",
    "game_controls": DATA / "curated" / "game_control_facts.jsonl",
    "equipment": DATA / "curated" / "equipment_item_details.jsonl",
    "members": DATA / "curated" / "member_profiles.jsonl",
    "availability": DATA / "curated" / "service_game_availability.jsonl",
    "closures": DATA / "calendar" / "service_closures.jsonl",
    "holidays_2026": DATA / "calendar" / "thai_holidays_2026.jsonl",
    "holidays_2027": DATA / "calendar" / "thai_holidays_2027.jsonl",
}

TH_WRAPPERS = (
    "{q}",
    "ขอสอบถามหน่อยครับ {q}",
    "ช่วยตอบจากข้อมูลที่ยืนยันได้หน่อย: {q}",
    "กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า {q}",
    "รบกวนเช็กข้อมูลของศูนย์ให้หน่อยครับ {q}",
    "{q} ขอรายละเอียดแบบสั้น ๆ",
    "{q} ช่วยแนบแหล่งข้อมูลด้วย",
    "สอบถามครับ {q}",
    "อยากรู้ว่า {q}",
    "{q} ครับ",
    "ถ้าจะไปใช้บริการจริง {q}",
    "ช่วยยืนยันให้ทีว่า {q}",
    "ขอข้อมูลล่าสุดที่ระบบยืนยันได้: {q}",
    "ถามแบบตรง ๆ นะ {q}",
    "พอดีไม่แน่ใจว่า {q}",
    "ช่วยอธิบายให้เข้าใจง่ายหน่อยว่า {q}",
    "ก่อนเดินทางไปศูนย์ อยากเช็กว่า {q}",
    "ขอคำตอบโดยไม่เดาข้อมูลนะครับ: {q}",
    "{q} ตอบเฉพาะประเด็นนี้ก็พอ",
    "{q} มีข้อมูลอ้างอิงไหม",
    "ขอเช็กอีกทีครับ {q}",
    "ถ้าดูตามข้อมูลทางการ {q}",
    "ช่วยดูให้หน่อยได้ไหมว่า {q}",
    "คำถามของผมคือ {q}",
    "{q} อยากได้คำตอบที่ยืนยันได้ครับ",
    "ผมกำลังตัดสินใจอยู่ เลยอยากรู้ว่า {q}",
    "ขอถามในบริบทของ PSU Esports Studio - Phuket: {q}",
    "{q} ช่วยแยกข้อมูลที่มีและไม่มีให้ด้วย",
    "อย่าคาดเดานะครับ ถามว่า {q}",
    "{q} ตอนนี้ระบบมีข้อมูลว่าอย่างไร",
)

EN_WRAPPERS = (
    "{q}",
    "Could you please help me with this: {q}",
    "Please answer from verified studio information: {q}",
    "I am planning a visit and would like to know: {q}",
    "Could you check the studio information for me? {q}",
    "{q} Please keep the answer concise.",
    "{q} Please include the source.",
    "Quick question: {q}",
    "I would like to know: {q}",
    "{q} Thanks.",
    "Before I use the service, {q}",
    "Could you confirm this for me: {q}",
    "Please use the latest verified information: {q}",
    "To ask directly, {q}",
    "I am not sure about this: {q}",
    "Could you explain this simply: {q}",
    "Before travelling to the studio, I want to check: {q}",
    "Please do not guess; answer this only if verified: {q}",
    "{q} Please answer only this point.",
    "{q} Is there a supporting source?",
    "Let me verify this again: {q}",
    "According to the official information: {q}",
    "Could you look this up for me: {q}",
    "My question is: {q}",
    "{q} I need a verified answer.",
    "I am deciding whether to visit, so {q}",
    "For PSU Esports Studio - Phuket, {q}",
    "{q} Please distinguish confirmed and unavailable information.",
    "Please avoid assumptions. My question is: {q}",
    "{q} What does the current knowledge base confirm?",
)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def clean_question(value: str) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    return text.rstrip(" .?!。")


def text_key(value: str) -> str:
    return re.sub(r"\s+", " ", value.casefold()).strip()


def list_value(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value if str(item).strip()]
    return [str(value)] if str(value).strip() else []


def route_categories(value: Any, fallback: str) -> list[str]:
    values = list_value(value)
    return values or [fallback]


def is_english_game_detail_question(question: str) -> bool:
    q = text_key(question)
    return any(
        re.search(pattern, q)
        for pattern in (
            r"\bwhat (?:is|kind of game is|genre is)\b",
            r"\bhow (?:do|can) (?:i|you) play\b",
            r"\bhow to play\b",
            r"\btell me about\b",
            r"\bdescribe\b",
            r"\bgame details?\b",
        )
    )


def benchmark_expected_status(locale: str, domain: str, question: str, category: Any) -> str:
    """Adjudicate legacy benchmark labels into answer-outcome contracts."""
    categories = set(list_value(category))
    q = text_key(question)
    if locale == "en" and domain in {"game_detail", "games_catalog_availability"} and is_english_game_detail_question(question):
        return "localization_pending"
    if domain != "compound_context_boundary":
        return "answer_available"
    if "multi_question" in categories:
        return "answer_available"
    explicit_catalog = bool(re.search(
        r"\b(?:pc hardware|what does (?:ps5|nintendo) have|vr options|what(?:'s| is) in the cockpit|\bgame\b|\bequipment\b)",
        q,
    ))
    if "clarification" in categories and explicit_catalog:
        return "answer_available"
    if "clarification" in categories:
        return "clarification_required"
    if "no_answer" in categories:
        return "no_answer_expected"
    if categories and categories <= {"general", "knowledge", "overview"}:
        if re.search(r"\b(?:hel+l+o+|hi|hey|who are you|what are you)\b", q):
            return "answer_available"
        if re.search(r"\b(?:api|json|latency|gpu|mechanical keyboard|frame rate|server and client)\b", q):
            return "answer_available"
        return "no_answer_expected"
    return "answer_available"


def domain_for_group(group: str) -> str:
    value = group.casefold().strip()
    mapping = {
        "service_fee": "service_fee",
        "booking": "reservation_policy",
        "reservation": "reservation_policy",
        "live_availability": "live_booking",
        "availability_machine_split": "live_booking",
        "schedule": "schedule_calendar",
        "live_schedule": "schedule_calendar",
        "policy_schedule_rules": "schedule_calendar",
        "games": "games_catalog_availability",
        "availability_game": "games_catalog_availability",
        "availability_service": "games_catalog_availability",
        "game_detail": "game_detail",
        "game_controls": "game_controls",
        "ambiguous_controls": "game_controls",
        "equipment": "equipment",
        "rules": "studio_rules_penalties",
        "rules_penalty": "studio_rules_penalties",
        "penalty": "studio_rules_penalties",
        "competition": "competition_rules",
        "competition_rules": "competition_rules",
        "members": "members_overview_contact",
        "members_about_contact": "members_overview_contact",
        "overview": "members_overview_contact",
        "contact": "members_overview_contact",
        "compound": "compound_context_boundary",
        "clarification": "compound_context_boundary",
        "clarification_no_answer": "compound_context_boundary",
        "ambiguity_no_answer": "compound_context_boundary",
        "input_quality": "compound_context_boundary",
        "out_of_scope": "compound_context_boundary",
        "general": "compound_context_boundary",
        "general_llm": "compound_context_boundary",
    }
    return mapping.get(value, "compound_context_boundary")


def make_seed(
    *, locale: str, domain: str, question: str, origin: str, origin_id: str,
    routes: Iterable[str], status: str = "answer_available", intent: str = "",
    target: str = "", facet: str = "", must: Iterable[str] = (),
    must_any: Iterable[str] = (), must_not: Iterable[str] = (),
    source_ids: Iterable[str] = (), source_urls: Iterable[str] = (),
    source_requirement: str = "verified_static", live: bool = False,
    critical: bool = False, priority: int = 1, metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    normalized_routes = {str(item) for item in routes if str(item)}
    if domain == "live_booking" or live or status == "live_lookup_required":
        normalized_routes.update(("reservation", "schedule"))
    return {
        "locale": locale,
        "domain": domain,
        "question": clean_question(question),
        "origin": origin,
        "origin_id": origin_id,
        "expected_route_categories": sorted(normalized_routes),
        "expected_answer_status": status,
        "expected_intent": intent,
        "expected_target": target,
        "expected_facet": facet,
        "must_contain": list(must),
        "must_contain_any": list(must_any),
        "must_not_contain": list(must_not),
        "source_ids": list(source_ids),
        "source_urls": list(source_urls),
        "source_requirement": source_requirement,
        "live_dependency": live,
        "critical": critical,
        "priority": priority,
        "metadata": metadata or {},
    }


def benchmark_seeds(locale: str) -> list[dict[str, Any]]:
    thai = read_jsonl(SOURCE_PATHS["thai_benchmark"])
    if locale == "th":
        source_rows = [(row, str(row.get("question") or ""), str(row.get("id") or "")) for row in thai]
    else:
        thai_by_id = {str(row.get("id") or ""): row for row in thai}
        source_rows = []
        for row in read_jsonl(SOURCE_PATHS["english_shadow"]):
            parent = thai_by_id.get(str(row.get("source_case_id") or ""), {})
            source_rows.append((parent | row, str(row.get("question_en") or ""), str(row.get("id") or "")))
    seeds = []
    for row, question, row_id in source_rows:
        if not question:
            continue
        if locale == "en" and row_id == "EN-SHADOW-1255":
            # The unreviewed machine translation changed Thai "book/open"
            # into product pre-order/release, which is a different intent.
            question = "How do I book PS5, and which days is the studio open?"
        group = str(row.get("group") or "general_llm")
        domain = domain_for_group(group)
        normalized_question = text_key(question)
        if group == "games" and (
            any(phrase in normalized_question for phrase in ("คือเกมอะไร", "เล่นยังไง"))
            or (locale == "en" and is_english_game_detail_question(question))
        ):
            domain = "game_detail"
        category = row.get("expected_category") or row.get("expected_categories") or []
        fallback = {
            "service_fee": "service_fee", "reservation_policy": "reservation",
            "live_booking": "reservation", "schedule_calendar": "schedule",
            "games_catalog_availability": "games", "game_detail": "games",
            "game_controls": "games", "equipment": "equipment",
            "studio_rules_penalties": "rules", "competition_rules": "competition_rules",
            "members_overview_contact": "overview", "compound_context_boundary": "clarification",
        }[domain]
        inherited_must = list_value(row.get("must_contain")) if locale == "th" else []
        inherited_must_any = list_value(row.get("must_contain_any")) if locale == "th" else []
        status = benchmark_expected_status(locale, domain, question, category)
        if locale == "en" and row_id == "EN-SHADOW-0615":
            status = "localization_pending"
        if locale == "en" and row_id == "EN-SHADOW-0622":
            status = "clarification_required"
            category = sorted(set(route_categories(category, fallback)) | {"clarification"})
        if locale == "en" and row_id == "EN-SHADOW-1320":
            category = sorted(set(route_categories(category, fallback)) | {"service_fee"})
        if status in {"clarification_required", "safe_clarification"}:
            category = sorted(set(route_categories(category, fallback)) | {"clarification"})
        elif status in {"no_answer_expected", "safe_no_answer"}:
            category = sorted(set(route_categories(category, fallback)) | {"no_answer"})
        seeds.append(make_seed(
            locale=locale, domain=domain, question=question, origin="model_benchmark_1600",
            origin_id=row_id, routes=route_categories(category, fallback),
            status=status, must=inherited_must if status == "answer_available" else [],
            must_any=inherited_must_any, must_not=list_value(row.get("must_not_contain")),
            source_ids=list_value(row.get("source")), source_requirement="inherited_answer_contract",
            critical=str(row.get("risk") or "").casefold() == "high", priority=2,
            metadata={"group": group, "quality_bucket": row.get("quality_bucket"), "risk": row.get("risk")},
        ))
    return seeds


def robustness_seeds(locale: str) -> list[dict[str, Any]]:
    seeds = []
    for row in read_jsonl(SOURCE_PATHS["rag_robustness"]):
        if row.get("locale") != locale:
            continue
        domain = domain_for_group(str(row.get("group") or "general"))
        normalized_question = text_key(str(row.get("question") or ""))
        if str(row.get("group") or "") == "games" and any(
            phrase in normalized_question
            for phrase in ("คือเกมอะไร", "เล่นยังไง", "what kind of game", "how do you play")
        ):
            domain = "game_detail"
        question = str(row["question"])
        normalized_question = text_key(question)
        status = str(row.get("expected_answer_status") or "answer_available")
        routes = list(row.get("expected_route_categories") or [])
        if locale == "en" and re.search(r"\bare you open\b", normalized_question):
            status = "answer_available"
        if locale == "en" and re.search(r"\bhow do four people book together\b", normalized_question):
            status = "clarification_required"
            routes = sorted(set(routes) | {"clarification"})
        if locale == "en" and "booking for today" in normalized_question:
            routes = sorted(set(routes) | {"schedule"})
        seeds.append(make_seed(
            locale=locale, domain=domain, question=question, origin="rag_robustness_v1",
            origin_id=str(row["id"]), routes=routes,
            status=status,
            target=str(row.get("expected_target") or ""),
            source_ids=[str(row.get("expected_source_requirement") or "")],
            source_requirement=str(row.get("expected_source_requirement") or "route_and_outcome_contract"),
            live=str(row.get("expected_answer_status")) == "live_lookup_required",
            critical=bool(row.get("critical")), priority=1,
            metadata={"scenario_id": row.get("scenario_id"), "behavior_tags": row.get("behavior_tags", [])},
        ))
    return seeds


def competition_seeds(locale: str) -> list[dict[str, Any]]:
    seeds = []
    for row in read_jsonl(SOURCE_PATHS["competition"]):
        if row.get("locale") != locale:
            continue
        seeds.append(make_seed(
            locale=locale, domain="competition_rules", question=str(row["question"]),
            origin="competition_rules_rag_ground_truth_v1", origin_id=str(row["id"]),
            routes=row.get("expected_route_categories") or ["competition_rules"],
            status=str(row.get("expected_answer_status") or "answer_available"),
            target=str(row.get("expected_game_id") or ""), facet=str(row.get("expected_facet") or ""),
            source_ids=(row.get("allowed_evidence_rule_ids") or []) + (row.get("expected_rulebook_ids") or []),
            source_urls=row.get("allowed_source_urls") or [], source_requirement="target_and_facet_grounded_rulebook",
            critical=True, priority=0, metadata={
                "case_type": row.get("case_type"), "rag_required": row.get("rag_required"),
                "source_gap_manifest_key": row.get("source_gap_manifest_key", ""),
            },
        ))
    return seeds


def english_gold_seeds() -> list[dict[str, Any]]:
    seeds = []
    for row in read_jsonl(SOURCE_PATHS["english_gold"]):
        status = str(row.get("expected_answer_status") or "answer_available")
        domain = domain_for_group(str(row.get("group") or "general"))
        routes = row.get("expected_categories") or []
        if status in {"safe_clarification", "clarification_required", "safe_no_answer", "no_answer_expected"}:
            domain = "compound_context_boundary"
        if status in {"safe_clarification", "clarification_required"}:
            routes = sorted(set(routes) | {"clarification"})
        elif status in {"safe_no_answer", "no_answer_expected"}:
            routes = sorted(set(routes) | {"no_answer"})
        if str(row.get("id") or "") == "EN-GOLD-0301":
            # The current closed-world rulebook contract requires a game
            # target. This older localization-pending label is obsolete.
            status = "clarification_required"
            domain = "compound_context_boundary"
            routes = ["competition_rules", "clarification"]
        must = row.get("must_contain") or []
        must_any = row.get("must_contain_any") or []
        normalized_question = text_key(str(row.get("question") or ""))
        if "minecraft" in normalized_question:
            status = "no_answer_expected"
            routes = sorted(set(routes) | {"games", "no_answer"})
            must, must_any = [], []
        elif is_english_game_detail_question(str(row.get("question") or "")):
            status = "localization_pending"
            must, must_any = [], []
        if any(text_key(str(item)) == "select a service" for item in must):
            must = [
                "Booking steps"
                if text_key(str(item)) == "select a service"
                else item
                for item in must
            ]
        if any(text_key(str(item)) == "verified game catalog" for item in must):
            must = [
                "There are currently 42 verified games available."
                if text_key(str(item)) == "verified game catalog"
                else item
                for item in must
            ]
        if "latest verified studio announcement" in normalized_question:
            status = "no_answer_expected"
            routes = sorted(set(routes) | {"no_answer", "events_news", "knowledge"})
            must, must_any = [], []
        if status == "safe_no_answer" and any(
            phrase in normalized_question
            for phrase in ("available now", "free now", "live slot", "available slot")
        ):
            routes = sorted(set(routes) | {"no_answer", "reservation", "schedule"})
            must, must_any = [], []
        if status == "localization_pending":
            # The old 400-case suite used literal localization-pending text as
            # its answer contract. Current approved/draft overlays may now
            # answer those cases, so retain the status but remove stale prose.
            must, must_any = [], []
        seeds.append(make_seed(
            locale="en", domain=domain, question=str(row["question"]), origin="english_gold_400",
            origin_id=str(row["id"]), routes=routes,
            status=status,
            must=must, must_any=must_any,
            must_not=row.get("must_not_contain") or [], source_requirement="reviewed_english_answer_contract",
            critical=bool(row.get("critical_fact")), priority=1,
        ))
    return seeds


def plain_pattern(patterns: list[Any], locale: str, fallback: str) -> str:
    candidates = []
    for value in patterns:
        text = str(value)
        has_thai = bool(re.search(r"[\u0E00-\u0E7F]", text))
        if (locale == "th") != has_thai:
            continue
        cleaned = re.sub(r"[.*+?^$(){}\[\]|\\]", " ", text)
        cleaned = re.sub(r"\s+", " ", cleaned).strip(" -")
        if len(cleaned) >= 4:
            candidates.append(cleaned)
    return max(candidates, key=len, default=fallback.replace("_", " "))


def rule_record_seeds(locale: str) -> list[dict[str, Any]]:
    seeds = []
    for row in read_jsonl(SOURCE_PATHS["rules"]):
        category = str(row.get("category") or "rules")
        domain = domain_for_group(category)
        intent = str(row.get("intent") or "")
        routes = [category]
        # The source file keeps opening-hour records under the broad
        # reservation category, but runtime behavior and user meaning are
        # schedule/calendar. Keep reservation as a compatible secondary route
        # while evaluating schedule as the primary domain.
        if intent.startswith("schedule_") or intent in {"service_schedule", "schedule_not_24_hours"}:
            domain = "schedule_calendar"
            routes = ["schedule", "reservation"]
        phrase = plain_pattern(row.get("patterns") or [], locale, str(row.get("intent") or "policy"))
        question = f"ขอข้อมูลเรื่อง{phrase}" if locale == "th" else f"What is the studio policy for {phrase}?"
        game_rule_questions = {
            "rule_cockpit_games": "Which game is available in the Cockpit Zone?",
            "rule_cockpit_gran_turismo": "Can I play Gran Turismo 7 in the Cockpit Zone?",
            "rule_pc_specific_games": "Which games are available in the PC Zone?",
            "rule_ps5_specific_games": "Which games are available in the PlayStation 5 Zone?",
            "rule_switch_specific_games": "Which games are available in the Nintendo Switch Zone?",
            "rule_vr_specific_games": "Which games are available in the VR Zone?",
        }
        if locale == "en" and str(row.get("id") or "") in game_rule_questions:
            question = game_rule_questions[str(row.get("id") or "")]
        elif str(row.get("id") or "") == "rule_cockpit_games":
            question = "Cockpit Zone มีเกมอะไรให้เล่นบ้าง" if locale == "th" else "Which game is available in the Cockpit Zone?"
        answer = str(row.get("answer_th" if locale == "th" else "answer_en") or "")
        seeds.append(make_seed(
            locale=locale, domain=domain, question=question, origin="rule_patterns",
            origin_id=str(row.get("id") or ""), routes=routes, intent=intent,
            status="no_answer_expected" if category == "no_answer" else "answer_available",
            source_ids=row.get("source_ids") or [],
            source_urls=[str(row.get("source_url") or "")], source_requirement="verified_rule_record",
            critical=category in {"reservation", "penalty", "rules"}, priority=0,
            metadata={"reference_answer": answer, "reference_answer_is_exact_match_required": False},
        ))
    return seeds


def game_detail_seeds(locale: str) -> list[dict[str, Any]]:
    seeds = []
    for row in read_jsonl(SOURCE_PATHS["game_details"]):
        game = str(row.get("game") or row.get("title") or "")
        url = str(row.get("source_url") or "")
        variants = (
            (f"{game} คือเกมอะไร", f"What kind of game is {game}?", "summary", [str(row.get("summary_th") or game)] if locale == "th" else [game]),
            (f"{game} เล่นยังไง", f"How do you play {game}?", "how_to_play", [str(row.get("how_to_play_th") or game)] if locale == "th" else [game]),
            (f"{game} เล่นได้ที่โซนไหน", f"Which studio zone has {game}?", "zone", list_value(row.get("zones"))),
        )
        for th_q, en_q, facet, must_any in variants:
            seeds.append(make_seed(
                locale=locale, domain="game_detail", question=th_q if locale == "th" else en_q,
                origin="game_item_details", origin_id=str(row.get("id") or ""), routes=["games"],
                intent="game_detail_lookup", target=game, facet=facet, must_any=must_any,
                status="localization_pending" if locale == "en" else "answer_available",
                source_ids=[str(row.get("id") or "")], source_urls=[url],
                source_requirement="verified_game_detail", priority=0,
            ))
    return seeds


def game_control_seeds(locale: str) -> list[dict[str, Any]]:
    seeds = []
    for row in read_jsonl(SOURCE_PATHS["game_controls"]):
        game = str(row.get("game") or "")
        platform = str(row.get("platform") or "")
        button = str(row.get("button") or "")
        if button:
            question = (
                f"ในเกม {game} บน {platform} ปุ่ม {button} ใช้ทำอะไร"
                if locale == "th" else f"What does the {button} button do in {game} on {platform}?"
            )
            must_any = [button, str(row.get("action_th" if locale == "th" else "action_en") or "")]
            facet = "button_action"
        else:
            question = (
                f"ปุ่มควบคุมของ {game} บน {platform} มีอะไรบ้าง"
                if locale == "th" else f"What are the controls for {game} on {platform}?"
            )
            must_any = [game, platform]
            facet = "control_summary"
        seeds.append(make_seed(
            locale=locale, domain="game_controls", question=question, origin="game_control_facts",
            origin_id=str(row.get("id") or ""), routes=["games"], intent="game_control_lookup",
            target=game, facet=facet, must_any=[item for item in must_any if item],
            source_ids=[str(row.get("id") or "")], source_urls=list_value(row.get("source_urls") or row.get("source_url")),
            source_requirement=str(row.get("coverage_status") or "control_source"), priority=0,
            metadata={"platform": platform, "button": button},
        ))
    return seeds


def equipment_seeds(locale: str) -> list[dict[str, Any]]:
    seeds = []
    for row in read_jsonl(SOURCE_PATHS["equipment"]):
        item, zone = str(row.get("item") or ""), str(row.get("zone") or "")
        english_item = re.sub(r"\b(\d+)\s*นิ้ว\b", r"\1-inch", item).replace("รุ่น", "model")
        variants = (
            (f"{item} คืออุปกรณ์อะไร", f"What is the {item}?", "description", [item] if locale == "th" else [item, english_item]),
            (f"{item} ใช้งานยังไง", f"How do I use the {item}?", "usage", [item] if locale == "th" else [item, english_item]),
            (f"{item} อยู่โซนไหน", f"Which zone has the {item}?", "zone", [zone]),
        )
        for th_q, en_q, facet, required in variants:
            seeds.append(make_seed(
                locale=locale, domain="equipment", question=th_q if locale == "th" else en_q,
                origin="equipment_item_details", origin_id=str(row.get("id") or ""), routes=["equipment"],
                intent="equipment_detail_lookup", target=item, facet=facet, must_any=[x for x in required if x],
                source_ids=[str(row.get("id") or "")], source_urls=[str(row.get("source_url") or "")],
                source_requirement="verified_equipment_record", priority=0,
            ))
    return seeds


def member_seeds(locale: str) -> list[dict[str, Any]]:
    seeds = []
    for index, row in enumerate(read_jsonl(SOURCE_PATHS["members"]), start=1):
        name, role = str(row.get("name") or ""), str(row.get("role") or "")
        questions = (
            (f"{name} มีตำแหน่งอะไร", f"What is {name}'s role?"),
            (f"ใครมีตำแหน่ง{role}", f"Who holds the role of {role}?"),
        )
        for th_q, en_q in questions:
            seeds.append(make_seed(
                locale=locale, domain="members_overview_contact", question=th_q if locale == "th" else en_q,
                origin="member_profiles", origin_id=f"member-{index:03d}", routes=["overview", "members"],
                intent="member_role_lookup", target=name, must_any=[name, role],
                source_ids=[f"member-{index:03d}"], source_urls=[str(row.get("source_url") or "")],
                source_requirement="verified_member_profile", priority=0,
            ))
    return seeds


def availability_seeds(locale: str) -> list[dict[str, Any]]:
    seeds = []
    for row in read_jsonl(SOURCE_PATHS["availability"]):
        label, zone = str(row.get("machine_label") or ""), str(row.get("zone") or "")
        games = list_value(row.get("games"))
        static_questions = (
            (f"{label} มีเกมอะไรบ้าง", f"Which games are installed on {label}?"),
            (f"{zone} รอบละกี่นาที", f"How long is one {zone} booking slot?"),
        )
        for th_q, en_q in static_questions:
            seeds.append(make_seed(
                locale=locale, domain="games_catalog_availability", question=th_q if locale == "th" else en_q,
                origin="service_game_availability", origin_id=str(row.get("id") or ""), routes=["games", "reservation"],
                intent="service_game_availability", target=label,
                must_any=games[:3] + [str(row.get("duration_minutes") or "")],
                source_ids=row.get("source_ids") or [], source_urls=[str(row.get("source_url") or "")],
                source_requirement="verified_static_service_catalog", priority=0,
            ))
        live_questions = (
            (f"ตอนนี้ {label} ว่างไหม", f"Is {label} available right now?"),
            (f"พรุ่งนี้ 13:00 {label} ว่างหรือเปล่า", f"Will {label} be available tomorrow at 13:00?"),
            (f"ช่วง 14:00-15:00 {zone} เครื่องไหนว่างบ้าง", f"Which {zone} units are free from 14:00 to 15:00?"),
        )
        for th_q, en_q in live_questions:
            seeds.append(make_seed(
                locale=locale, domain="live_booking", question=th_q if locale == "th" else en_q,
                origin="service_game_availability_live", origin_id=str(row.get("id") or ""), routes=["reservation", "schedule"],
                status="live_lookup_required", intent="live_booking_status", target=label,
                source_ids=["wordpress_booking_api"], source_urls=[str(row.get("source_url") or "")],
                source_requirement="live_wordpress_booking_api", live=True, critical=True, priority=0,
            ))
    return seeds


def schedule_seeds(locale: str) -> list[dict[str, Any]]:
    th_questions = (
        "วันนี้ศูนย์เปิดไหม", "พรุ่งนี้ศูนย์เปิดหรือเปล่า", "วันจันทร์ช่วงเช้าเปิดไหม",
        "วันศุกร์บ่ายโมงเปิดให้บริการไหม", "ช่วง Maintenance จองได้ไหม",
        "วันนี้ 13:00 ศูนย์เปิดหรือปิด", "สัปดาห์นี้มีวันปิดพิเศษไหม",
        "วันหยุดราชการศูนย์เปิดไหม", "เวลาเปิดปิดปกติเป็นอย่างไร", "ตอนนี้ศูนย์เปิดอยู่ไหม",
    )
    en_questions = (
        "Is the studio open today?", "Will the studio be open tomorrow?", "Is it open on Monday morning?",
        "Is the studio open at 13:00 on Friday?", "Can I book during maintenance?",
        "Is the studio open or closed today at 13:00?", "Are there any special closures this week?",
        "Is the studio open on public holidays?", "What are the regular opening hours?", "Is the studio open right now?",
    )
    seeds = []
    for index, question in enumerate(th_questions if locale == "th" else en_questions, start=1):
        live = index in {1, 2, 6, 7, 10}
        seeds.append(make_seed(
            locale=locale, domain="schedule_calendar", question=question, origin="calendar_schedule_contract",
            origin_id=f"schedule-{index:02d}", routes=["schedule", "reservation"],
            status="live_lookup_required" if live else "answer_available", intent="date_aware_schedule",
            source_ids=["service_schedule", "service_closures", "thai_holidays"],
            source_urls=["https://esports.computing.psu.ac.th/reservation"],
            source_requirement="date_aware_calendar" if live else "verified_schedule_policy",
            live=live, critical=True, priority=0,
        ))
    return seeds


def all_seeds(locale: str) -> list[dict[str, Any]]:
    seeds = (
        rule_record_seeds(locale) + game_detail_seeds(locale) + game_control_seeds(locale)
        + equipment_seeds(locale) + member_seeds(locale) + availability_seeds(locale)
        + schedule_seeds(locale) + competition_seeds(locale) + robustness_seeds(locale)
        + benchmark_seeds(locale)
    )
    if locale == "en":
        seeds += english_gold_seeds()
    # The source-grounded competition suite supersedes older benchmark and
    # localization labels. It is large enough to generate the full 500-case
    # allocation while retaining target, facet, and evidence contracts.
    seeds = [
        seed for seed in seeds
        if seed["domain"] != "competition_rules"
        or seed["origin"] == "competition_rules_rag_ground_truth_v1"
    ]
    unique: dict[tuple[str, str], dict[str, Any]] = {}
    for seed in seeds:
        if not seed["question"]:
            continue
        key = (seed["domain"], text_key(seed["question"]))
        existing = unique.get(key)
        if existing is None:
            unique[key] = seed
            continue
        merged_ids = sorted(set(existing["source_ids"]) | set(seed["source_ids"]))
        merged_urls = sorted(set(existing["source_urls"]) | set(seed["source_urls"]))
        merged_origins = sorted(set(existing["metadata"].get("merged_origin_ids", [existing["origin_id"]])) | {seed["origin_id"]})
        preferred = seed if seed["priority"] < existing["priority"] else existing
        preferred = dict(preferred)
        preferred["source_ids"] = merged_ids
        preferred["source_urls"] = merged_urls
        preferred["metadata"] = dict(preferred["metadata"])
        preferred["metadata"]["merged_origin_ids"] = merged_origins
        unique[key] = preferred
    return sorted(unique.values(), key=lambda row: (row["domain"], row["priority"], row["origin"], row["origin_id"], row["question"]))


def expand_domain(locale: str, domain: str, seeds: list[dict[str, Any]], target: int) -> list[dict[str, Any]]:
    if not seeds:
        raise ValueError(f"No seeds for {locale}/{domain}")
    wrappers = TH_WRAPPERS if locale == "th" else EN_WRAPPERS
    result: list[dict[str, Any]] = []
    seen: set[str] = set()
    # Source-backed records are always represented before inherited cases.
    for wrapper_index in range(len(wrappers)):
        for seed in seeds:
            question = clean_question(wrappers[wrapper_index].format(q=seed["question"]))
            key = text_key(question)
            if key in seen:
                continue
            seen.add(key)
            row = dict(seed)
            row["question"] = question
            row["question_style"] = "source_form" if wrapper_index == 0 else f"paraphrase_wrapper_{wrapper_index:02d}"
            row["review_status"] = (
                "source_grounded_gold_candidate"
                if wrapper_index == 0 and seed["priority"] == 0
                else "inherited_gold_candidate"
                if wrapper_index == 0
                else "generated_paraphrase_pending_review"
            )
            result.append(row)
            if len(result) == target:
                return result
    raise ValueError(f"Only generated {len(result)}/{target} unique questions for {locale}/{domain}")


def build_locale(locale: str) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for seed in all_seeds(locale):
        grouped[seed["domain"]].append(seed)
    rows: list[dict[str, Any]] = []
    locale_prefix = locale.upper()
    for domain, target in DOMAIN_TARGETS.items():
        rows.extend(expand_domain(locale, domain, grouped[domain], target))
    for index, row in enumerate(rows, start=1):
        row["id"] = f"MASTER-GT-{locale_prefix}-{index:05d}"
        row["suite"] = SUITE
        row["answer_contract"] = {
            "must_contain": row.pop("must_contain"),
            "must_contain_any": row.pop("must_contain_any"),
            "must_not_contain": row.pop("must_not_contain"),
        }
        row["source_contract"] = {
            "source_ids": row.pop("source_ids"),
            "source_urls": [url for url in row.pop("source_urls") if url],
            "requirement": row.pop("source_requirement"),
            "live_dependency": row.pop("live_dependency"),
        }
        row["latency_ceiling_sec"] = 20.0
        row["generation_version"] = "master-gt-builder-v2-20260923"
        row.pop("priority", None)
    return rows


def validate(rows: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    required = {
        "id", "suite", "locale", "domain", "question", "question_style", "origin", "origin_id",
        "expected_route_categories", "expected_answer_status", "answer_contract", "source_contract",
        "review_status", "critical", "latency_ceiling_sec", "generation_version",
    }
    if len(rows) != 10000:
        errors.append(f"Expected 10000 rows, found {len(rows)}")
    ids = [str(row.get("id")) for row in rows]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate IDs found")
    for locale in ("th", "en"):
        locale_rows = [row for row in rows if row.get("locale") == locale]
        if len(locale_rows) != 5000:
            errors.append(f"Expected 5000 {locale} rows, found {len(locale_rows)}")
        questions = [text_key(str(row.get("question") or "")) for row in locale_rows]
        if len(questions) != len(set(questions)):
            errors.append(f"Duplicate normalized questions found for {locale}")
        counts = Counter(str(row.get("domain")) for row in locale_rows)
        if counts != Counter(DOMAIN_TARGETS):
            errors.append(f"Wrong domain distribution for {locale}: {dict(counts)}")
    for row in rows:
        missing = required - row.keys()
        if missing:
            errors.append(f"{row.get('id')} missing {sorted(missing)}")
        if not row.get("expected_route_categories"):
            errors.append(f"{row.get('id')} has no expected route")
        source = row.get("source_contract") or {}
        if row.get("expected_answer_status") in {"answer_available", "live_lookup_required"} and not (
            source.get("source_ids") or source.get("source_urls") or source.get("requirement")
        ):
            errors.append(f"{row.get('id')} has no source contract")
        if source.get("live_dependency") and row.get("expected_answer_status") != "live_lookup_required":
            errors.append(f"{row.get('id')} live dependency must use live_lookup_required")
    return errors


def source_hashes() -> dict[str, str]:
    return {
        name: hashlib.sha256(path.read_bytes()).hexdigest()
        for name, path in SOURCE_PATHS.items()
        if path.exists()
    }


def report(rows: list[dict[str, Any]]) -> str:
    lines = [
        "# PSU Esports Master Ground Truth Candidate v1",
        "",
        "ชุดนี้ครอบคลุมความสามารถทั้งหมดของ Chatbot โดยแยก Static Answer, Live Lookup, Clarification และ Safe No-answer.",
        "Generated paraphrase เป็น Gold candidate ที่ต้องผ่าน Pipeline evaluation และ Human Review ก่อนใช้เป็น Release Gate แบบ strict.",
        "",
        "## Summary",
        "",
        f"- Total: {len(rows):,}",
        f"- Thai: {sum(row['locale'] == 'th' for row in rows):,}",
        f"- English: {sum(row['locale'] == 'en' for row in rows):,}",
        "",
        "## Domain Distribution Per Locale",
        "",
        "| Domain | Thai | English |",
        "|---|---:|---:|",
    ]
    for domain in DOMAIN_TARGETS:
        lines.append(
            f"| `{domain}` | {sum(row['locale'] == 'th' and row['domain'] == domain for row in rows)} "
            f"| {sum(row['locale'] == 'en' and row['domain'] == domain for row in rows)} |"
        )
    statuses = Counter((row["locale"], row["expected_answer_status"]) for row in rows)
    reviews = Counter((row["locale"], row["review_status"]) for row in rows)
    lines += ["", "## Answer Status", ""]
    for (locale, status), count in sorted(statuses.items()):
        lines.append(f"- `{locale}/{status}`: {count}")
    lines += ["", "## Review Status", ""]
    for (locale, status), count in sorted(reviews.items()):
        lines.append(f"- `{locale}/{status}`: {count}")
    lines += [
        "", "## Safety Contract", "",
        "- Live booking and date-aware questions never freeze a current availability result into Gold.",
        "- Source-gap and unsupported questions test abstention, not a fabricated answer.",
        "- English source contracts do not authorize runtime translation of facts.",
        "- Every generated paraphrase remains pending review until independently checked.",
    ]
    return "\n".join(lines) + "\n"


def write(rows: list[dict[str, Any]]) -> None:
    EVAL.mkdir(parents=True, exist_ok=True)
    th = [row for row in rows if row["locale"] == "th"]
    en = [row for row in rows if row["locale"] == "en"]
    for path, subset in ((TH_PATH, th), (EN_PATH, en), (COMBINED_PATH, rows)):
        path.write_text("\n".join(json.dumps(row, ensure_ascii=False, sort_keys=True) for row in subset) + "\n", encoding="utf-8")
    REPORT_PATH.write_text(report(rows), encoding="utf-8")
    manifest = {
        "suite": SUITE,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "counts": {"th": len(th), "en": len(en), "combined": len(rows)},
        "domain_targets_per_locale": DOMAIN_TARGETS,
        "output_sha256": {
            "th": hashlib.sha256(TH_PATH.read_bytes()).hexdigest(),
            "en": hashlib.sha256(EN_PATH.read_bytes()).hexdigest(),
            "combined": hashlib.sha256(COMBINED_PATH.read_bytes()).hexdigest(),
        },
        "source_sha256": source_hashes(),
        "review_policy": "generated_paraphrases_require_pipeline_evaluation_and_human_review_before_strict_release_gate",
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build() -> list[dict[str, Any]]:
    return build_locale("th") + build_locale("en")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the 5,000 Thai + 5,000 English master GT candidate corpus.")
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    rows = build()
    errors = validate(rows)
    if errors:
        print("Master ground truth validation failed:\n- " + "\n- ".join(errors[:100]))
        return 1
    if args.write:
        write(rows)
        print(f"Generated {len(rows)} rows: {TH_PATH.name}, {EN_PATH.name}, {COMBINED_PATH.name}")
    if args.check or not args.write:
        print(f"Master ground truth is structurally valid: {len(rows)} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
