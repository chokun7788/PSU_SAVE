#!/usr/bin/env python3
"""Build and validate a bilingual, adversarial RAG evaluation corpus.

The corpus intentionally evaluates route selection and safe outcome before
answer wording. Dynamic availability questions therefore require a live-data
path instead of a frozen answer, while ambiguous and out-of-scope questions
must clarify or decline rather than hallucinate.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "data" / "eval"
OUT_PATH = OUT_DIR / "rag_robustness_ground_truth_v1.jsonl"
REPORT_PATH = OUT_DIR / "rag_robustness_ground_truth_v1_report.md"
MANIFEST_PATH = OUT_DIR / "rag_robustness_ground_truth_v1_manifest.json"
SUITE = "rag_robustness_ground_truth_v1"


def seed(
    key: str,
    group: str,
    th: str,
    en: str,
    categories: tuple[str, ...],
    status: str,
    source: str,
    *,
    target: str = "",
    difficulty: str = "medium",
    tags: tuple[str, ...] = (),
) -> dict[str, Any]:
    return {
        "key": key,
        "group": group,
        "th": th,
        "en": en,
        "categories": categories,
        "status": status,
        "source": source,
        "target": target,
        "difficulty": difficulty,
        "tags": tags,
    }


# Each seed is one semantic intention, rendered in four distinct user styles.
# All facts are constrained to known product domains; ambiguous cases assert a
# safe outcome instead of inventing a fact that is not present in the source.
SEEDS = (
    # Games: 12
    seed("games_all", "games", "ตอนนี้มีเกมอะไรบ้าง", "What games are currently available?", ("games",), "answer_available", "verified_catalog", tags=("broad", "catalog")),
    seed("games_pc", "games", "PC Zone มีเกมอะไรให้เล่น", "Which games are available in the PC Zone?", ("games",), "answer_available", "verified_catalog", target="PC Zone"),
    seed("games_ps5", "games", "PS5 มีเกมอะไรบ้าง", "What can I play on PS5?", ("games",), "answer_available", "verified_catalog", target="PlayStation 5 Zone"),
    seed("games_vr", "games", "VR มีเกมอะไรให้เล่น", "Which games are available in the VR Zone?", ("games",), "answer_available", "verified_catalog", target="VR Zone"),
    seed("games_beat_saber", "games", "Beat Saber เล่นโซนไหน", "Which zone has Beat Saber?", ("games",), "answer_available", "verified_catalog", target="Beat Saber"),
    seed("games_gran_turismo", "games", "Gran Turismo 7 เล่นกับ cockpit ได้ไหม", "Can I play Gran Turismo 7 in the cockpit?", ("games",), "answer_available", "verified_catalog", target="Gran Turismo 7"),
    seed("games_valorant_detail", "games", "VALORANT คือเกมอะไร", "What kind of game is VALORANT?", ("games",), "answer_available", "game_detail", target="VALORANT", tags=("detail",)),
    seed("games_overcooked_how", "games", "Overcooked! 2 เล่นยังไง", "How do I play Overcooked! 2?", ("games",), "answer_available", "game_detail", target="Overcooked! 2", tags=("how_to",)),
    seed("games_minecraft_unknown", "games", "ที่ศูนย์มี Minecraft ไหม", "Is Minecraft available at the studio?", ("games",), "no_answer_expected", "verified_catalog", target="Minecraft", difficulty="hard", tags=("unknown_entity",)),
    seed("games_hades_unknown", "games", "Hades II มีให้เล่นไหม", "Do you have Hades II?", ("games",), "no_answer_expected", "verified_catalog", target="Hades II", difficulty="hard", tags=("unknown_entity",)),
    seed("games_unspecified", "clarification", "เกมนี้เล่นที่ไหน", "Where can I play this game?", ("games", "general"), "clarification_required", "none", difficulty="hard", tags=("ambiguous_reference",)),
    seed("games_two_titles", "games", "Tekken 8 กับ Minecraft มีให้เล่นทั้งคู่ไหม", "Are both TEKKEN 8 and Minecraft available?", ("games",), "answer_available", "verified_catalog", difficulty="hard", tags=("compound", "mixed_known_unknown")),
    # Equipment: 8
    seed("equipment_pc", "equipment", "PC Zone มีอุปกรณ์อะไรบ้าง", "What equipment is in the PC Zone?", ("equipment",), "answer_available", "verified_equipment", target="PC Zone"),
    seed("equipment_vr", "equipment", "VR Zone มีอุปกรณ์อะไร", "What equipment is available in the VR Zone?", ("equipment",), "answer_available", "verified_equipment", target="VR Zone"),
    seed("equipment_ps5_controller", "equipment", "PS5 ใช้จอยแบบไหน", "What controller is used for PS5?", ("equipment", "game_controls"), "answer_available", "verified_equipment", target="PlayStation 5 Zone"),
    seed("equipment_headset", "equipment", "มีหูฟังให้ใช้ไหม", "Do you provide headsets?", ("equipment",), "answer_available", "verified_equipment", difficulty="medium", tags=("short",)),
    seed("equipment_own_keyboard", "equipment", "เอาคีย์บอร์ดตัวเองมาใช้ได้ไหม", "May I bring and use my own keyboard?", ("equipment", "rules"), "answer_available", "verified_equipment", difficulty="hard", tags=("policy_edge",)),
    seed("equipment_mouse", "equipment", "มีเมาส์เกมมิ่งให้ไหม", "Is a gaming mouse provided?", ("equipment",), "answer_available", "verified_equipment", difficulty="medium"),
    seed("equipment_unknown_gpu", "equipment", "เครื่อง PC ใช้การ์ดจอรุ่นอะไร", "What GPU model is inside the PCs?", ("equipment",), "no_answer_expected", "verified_equipment", difficulty="hard", tags=("unsupported_detail",)),
    seed("equipment_ambiguous", "clarification", "อันนั้นใช้อะไรเล่น", "What do I use to play that?", ("equipment", "games", "general"), "clarification_required", "none", difficulty="hard", tags=("ambiguous_reference",)),
    # Prices: 8
    seed("price_pc", "service_fee", "PC ชั่วโมงละเท่าไหร่", "How much is one hour on PC?", ("service_fee",), "answer_available", "service_fee", target="PC Zone", tags=("price",)),
    seed("price_pc_two_hours", "service_fee", "เล่น PC 2 ชั่วโมง บุคคลทั่วไปคิดยังไง", "What does two hours on PC cost for a general adult?", ("service_fee",), "answer_available", "service_fee", target="PC Zone", difficulty="hard", tags=("calculation",)),
    seed("price_vr_half_hour", "service_fee", "VR ครึ่งชั่วโมงกี่บาท", "How much is VR for 30 minutes?", ("service_fee",), "answer_available", "service_fee", target="VR Zone"),
    seed("price_ps5_student", "service_fee", "นักศึกษา PSU เล่น PS5 เสียเงินไหม", "Does a PSU student pay for PS5?", ("service_fee",), "answer_available", "service_fee", target="PlayStation 5 Zone"),
    seed("price_game_zone", "service_fee", "Tekken 8 ราคาเท่าไหร่", "How much does TEKKEN 8 cost?", ("service_fee", "games"), "answer_available", "service_fee", target="TEKKEN 8", difficulty="hard", tags=("game_to_zone",)),
    seed("price_compare", "service_fee", "PC กับ VR อันไหนแพงกว่า", "Which is more expensive, PC or VR?", ("service_fee",), "answer_available", "service_fee", difficulty="hard", tags=("comparison",)),
    seed("price_payment", "booking", "จ่ายเงินยังไงตอนจอง", "How do I pay for a booking?", ("reservation", "service_fee"), "answer_available", "booking_policy", tags=("payment",)),
    seed("price_ambiguous", "clarification", "ราคาเท่าไหร่", "How much is it?", ("service_fee", "general"), "clarification_required", "none", difficulty="hard", tags=("ambiguous_reference",)),
    # Booking and live availability: 10
    seed("booking_how", "booking", "ต้องการจองเครื่องทำยังไง", "How do I book a machine?", ("reservation",), "answer_available", "booking_policy"),
    seed("booking_cancel", "booking", "ยกเลิกการจองยังไง", "How can I cancel a reservation?", ("reservation",), "answer_available", "booking_policy"),
    seed("booking_checkin", "booking", "ไปถึงแล้วต้องเช็กอินไหม", "Do I need to check in when I arrive?", ("reservation",), "answer_available", "booking_policy"),
    seed("live_pc2_now", "live_availability", "PC เครื่อง 2 ว่างไหมตอนนี้", "Is PC 2 available right now?", ("reservation",), "live_lookup_required", "live_booking_api", target="PC #02", tags=("live", "machine")),
    seed("live_pc3_future", "live_availability", "PC3 ตอนบ่ายโมงว่างไหม", "Will PC 3 be available at 1 PM?", ("reservation",), "live_lookup_required", "live_booking_api", target="PC #03", difficulty="hard", tags=("live", "future_time")),
    seed("live_multi_zone", "live_availability", "PC กับ VR ตอนสามโมงว่างไหม", "Are both PC and VR available at 3 PM?", ("reservation",), "live_lookup_required", "live_booking_api", difficulty="hard", tags=("live", "compound")),
    seed("live_slot", "live_availability", "มี slot ว่างช่วง 14:00-15:00 ไหม", "Is there any free slot from 14:00 to 15:00?", ("reservation",), "live_lookup_required", "live_booking_api", tags=("live", "time_range")),
    seed("booking_same_day", "booking", "จองวันนี้เลยได้ไหม", "Can I make a booking for today?", ("reservation",), "answer_available", "booking_policy", difficulty="medium"),
    seed("booking_group", "booking", "จองพร้อมกัน 4 คนต้องทำยังไง", "How do four people book together?", ("reservation",), "answer_available", "booking_policy", difficulty="hard", tags=("group_booking",)),
    seed("booking_unspecified", "clarification", "อันนี้จองได้ไหม", "Can I book this?", ("reservation", "general"), "clarification_required", "none", difficulty="hard", tags=("ambiguous_reference",)),
    # Schedule: 8
    seed("schedule_weekday", "schedule", "วันอังคารศูนย์เปิดกี่โมง", "What are Tuesday opening hours?", ("schedule",), "answer_available", "service_schedule", target="Tuesday"),
    seed("schedule_friday_pm", "schedule", "วันศุกร์บ่ายโมงเปิดไหม", "Is the studio open at 1 PM on Friday?", ("schedule",), "answer_available", "service_schedule", target="Friday 13:00", difficulty="hard", tags=("maintenance",)),
    seed("schedule_monday_am", "schedule", "วันจันทร์เช้าเปิดหรือปิด", "Is the studio open on Monday morning?", ("schedule",), "answer_available", "service_schedule", target="Monday morning", difficulty="hard", tags=("maintenance",)),
    seed("schedule_now", "live_schedule", "ตอนนี้ศูนย์เปิดไหม", "Is the studio open right now?", ("schedule", "reservation"), "live_lookup_required", "time_api", tags=("live",)),
    seed("schedule_tomorrow", "live_schedule", "พรุ่งนี้เปิดไหม", "Will the studio be open tomorrow?", ("schedule", "reservation"), "live_lookup_required", "time_api", difficulty="hard", tags=("live", "relative_date")),
    seed("schedule_holiday", "live_schedule", "วันหยุดราชการเปิดไหม", "Is the studio open on public holidays?", ("schedule",), "clarification_required", "calendar_exception", difficulty="hard", tags=("holiday", "needs_date")),
    seed("schedule_maintenance", "schedule", "Maintenance คือช่วงไหน", "When is maintenance scheduled?", ("schedule",), "answer_available", "service_schedule", tags=("maintenance",)),
    seed("schedule_ambiguous", "clarification", "เปิดปะ", "Are you open?", ("schedule", "general"), "clarification_required", "none", difficulty="hard", tags=("short", "ambiguous_time")),
    # Competition: 12
    seed("comp_cs2_team", "competition", "CS2 แข่งทีมละกี่คน", "How many players are on a CS2 team?", ("competition_rules",), "answer_available", "competition_rag", target="Counter-Strike 2", tags=("competition", "team_size")),
    seed("comp_cs2_map", "competition", "CS2 แบนแมพยังไง", "How does CS2 map veto work?", ("competition_rules",), "answer_available", "competition_rag", target="Counter-Strike 2", difficulty="hard", tags=("competition", "map_veto")),
    seed("comp_cs2_overtime", "competition", "CS2 ต่อเวลายังไง", "What are the CS2 overtime rules?", ("competition_rules",), "answer_available", "competition_rag", target="Counter-Strike 2", difficulty="hard", tags=("competition", "overtime")),
    seed("comp_cs2_late", "competition", "CS2 มาสายโดนอะไร", "What happens if a CS2 team is late?", ("competition_rules",), "answer_available", "competition_rag", target="Counter-Strike 2", tags=("competition", "penalty")),
    seed("comp_val_pause", "competition", "VALORANT ขอ pause ได้ตอนไหน", "When can a VALORANT team request a pause?", ("competition_rules",), "answer_available", "competition_rag", target="VALORANT", difficulty="hard", tags=("competition", "pause")),
    seed("comp_val_agent", "competition", "VALORANT Agent ใหม่ใช้แข่งได้เลยไหม", "Can a newly released VALORANT Agent be used immediately?", ("competition_rules",), "answer_available", "competition_rag", target="VALORANT", difficulty="hard", tags=("competition", "agent")),
    seed("comp_rov_format", "competition", "RoV แข่งแบบ BO อะไร", "What best-of format is used for RoV?", ("competition_rules",), "answer_available", "competition_rag", target="Arena of Valor (RoV)", tags=("competition", "format")),
    seed("comp_rov_skin", "competition", "RoV ใช้สกินพิเศษได้ไหม", "Are special skins allowed in RoV?", ("competition_rules",), "answer_available", "competition_rag", target="Arena of Valor (RoV)", tags=("competition", "skin")),
    seed("comp_tekken_format", "competition", "Tekken 8 แข่ง 1v1 ใช่ไหม", "Is Tekken 8 played as 1v1?", ("competition_rules",), "answer_available", "competition_rag", target="Tekken 8", tags=("competition", "format")),
    seed("comp_tekken_stage", "competition", "Tekken 8 เลือกด่านยังไง", "How is the Tekken 8 stage selected?", ("competition_rules",), "answer_available", "competition_rag", target="Tekken 8", difficulty="hard", tags=("competition", "stage")),
    seed("comp_broad", "clarification", "กติกาแข่งเป็นยังไง", "What are the competition rules?", ("competition_rules", "general"), "clarification_required", "competition_rag", difficulty="hard", tags=("competition", "missing_game_event")),
    seed("comp_event_ambiguous", "clarification", "กติกา Valorant งานล่าสุดใช้อะไร", "Which VALORANT event rules do you mean?", ("competition_rules", "general"), "clarification_required", "competition_rag", difficulty="hard", tags=("competition", "missing_event")),
    # Members, contact, studio rules: 9
    seed("overview_identity", "overview", "นายเป็นใคร", "Who are you?", ("overview", "general", "knowledge"), "answer_available", "chatbot_identity", tags=("identity",)),
    seed("overview_typo_identity", "overview", "นายเปนไค", "who r u", ("overview", "general", "knowledge"), "answer_available", "chatbot_identity", difficulty="hard", tags=("typo", "slang")),
    seed("members_list", "members", "มีทีมงานใครบ้าง", "Who are the staff members?", ("overview", "members"), "answer_available", "members_directory"),
    seed("members_role", "members", "ใครดูแลศูนย์", "Who manages the studio?", ("overview", "members"), "answer_available", "members_directory", difficulty="hard", tags=("role_lookup",)),
    seed("contact", "contact", "ติดต่อศูนย์ยังไง", "How can I contact the studio?", ("contact", "overview"), "answer_available", "official_contact"),
    seed("location", "contact", "ศูนย์อยู่ที่ไหน", "Where is the studio located?", ("contact", "overview"), "answer_available", "official_contact"),
    seed("studio_rules", "rules", "เอาอาหารเข้าไปได้ไหม", "Can I bring food into the studio?", ("rules", "overview"), "answer_available", "studio_rules", difficulty="hard", tags=("policy",)),
    seed("recording_rules", "rules", "อัดวิดีโอในศูนย์ได้ไหม", "May I record video inside the studio?", ("rules", "overview"), "no_answer_expected", "studio_rules", difficulty="hard", tags=("unsupported_detail",)),
    seed("special_request", "clarification", "ขอทำเรื่องพิเศษได้ไหม", "Can I make a special request?", ("general", "reservation"), "clarification_required", "none", difficulty="hard", tags=("underspecified",)),
    # Safety, malformed, mixed language: 8
    seed("greeting", "general", "หวัดดี", "helllo", ("general", "overview", "knowledge"), "answer_available", "chatbot_identity", difficulty="easy", tags=("greeting", "typo")),
    seed("keyboard_layout_th", "input_quality", "g]jo", "g]jo", ("general", "unknown", "clarification", "no_answer"), "clarification_required", "input_quality_guard", difficulty="hard", tags=("keyboard_layout",)),
    seed("keyboard_layout_en", "input_quality", "ะ้ฟะ รน ะฟ ไำืะ", "ะ้ฟะ รน ะฟ ไำืะ", ("general", "unknown", "clarification", "no_answer"), "clarification_required", "input_quality_guard", difficulty="hard", tags=("keyboard_layout",)),
    seed("mixed_game_query", "games", "มีเกม shooting บน PC ไหม", "มีเกมยิงบน PC ไหม", ("games",), "answer_available", "verified_catalog", difficulty="hard", tags=("mixed_language", "semantic")),
    seed("mixed_booking_query", "booking", "pc2 available ตอน 3pm ไหม", "pc2 ว่างไหม at 3pm", ("reservation",), "live_lookup_required", "live_booking_api", difficulty="hard", tags=("mixed_language", "live")),
    seed("external_weather", "out_of_scope", "พรุ่งนี้ฝนตกไหม", "Will it rain tomorrow?", ("general", "unknown"), "no_answer_expected", "none", difficulty="hard", tags=("out_of_scope",)),
    seed("external_cheat", "out_of_scope", "สอนใช้ Cheat Engine หน่อย", "Teach me how to use Cheat Engine.", ("general", "unknown"), "no_answer_expected", "none", difficulty="hard", tags=("out_of_scope", "safety")),
    seed("nonsense", "input_quality", "asdfghjkl", "zxqv qqq ???", ("general", "unknown"), "clarification_required", "input_quality_guard", difficulty="hard", tags=("nonsense",)),
)


VARIANTS = {
    "th": (
        ("direct", "{question}"),
        ("polite", "ขอข้อมูลที่ยืนยันได้หน่อยครับ: {question}"),
        ("contextual", "กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า {question}"),
        ("informal_noisy", "{question_noisy}"),
    ),
    "en": (
        ("direct", "{question}"),
        ("polite", "Could you check this using verified information: {question}"),
        ("contextual", "I am planning a visit and need to know: {question}"),
        ("informal_noisy", "{question_noisy}"),
    ),
}


def noisy_th(question: str) -> str:
    value = question.replace("เป็น", "เปน").replace("ไหม", "มั้ย").replace("อย่างไร", "ยังไง")
    return value if value != question else f"{question} อะ"


def noisy_en(question: str) -> str:
    value = question
    replacements = (("What are", "what r"), ("What is", "whats"), ("How do I", "how do i"), ("Can I", "can i"), ("Is ", "is "))
    for old, new in replacements:
        if old in value:
            value = value.replace(old, new, 1)
            break
    value = value.lower().replace("?", " ?")
    # A noisy variant must remain a distinct user utterance after normalization.
    # Some intentionally short inputs (for example, "who r u" and "helllo")
    # have no replacement above, so mark them as informal rather than duplicating
    # the direct variant.
    if _question_key(value) == _question_key(question):
        value = f"{value} pls"
    return value


def build_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for language in ("th", "en"):
        for item in SEEDS:
            base = str(item[language])
            for variant_index, (variant, template) in enumerate(VARIANTS[language], start=1):
                noisy = noisy_th(base) if language == "th" else noisy_en(base)
                question = template.format(question=base, question_noisy=noisy)
                row_id = f"RAG-ROBUST-{language.upper()}-{len([row for row in rows if row['locale'] == language]) + 1:03d}"
                expected_categories = list(item["categories"])
                # These are explicit safe runtime routes, not a replacement for
                # domain routing. They are valid only when the case expects the
                # matching safe outcome.
                if item["status"] == "clarification_required" and "clarification" not in expected_categories:
                    expected_categories.append("clarification")
                if item["status"] == "no_answer_expected" and "no_answer" not in expected_categories:
                    expected_categories.append("no_answer")
                rows.append({
                    "id": row_id,
                    "suite": SUITE,
                    "scenario_id": item["key"],
                    "locale": language,
                    "variant": variant,
                    "group": item["group"],
                    "question": question,
                    "expected_route_categories": expected_categories,
                    "expected_answer_status": item["status"],
                    "expected_source_requirement": item["source"],
                    "expected_target": item["target"],
                    "difficulty": item["difficulty"],
                    "behavior_tags": list(item["tags"]),
                    "critical": item["status"] in {"live_lookup_required", "clarification_required", "no_answer_expected"} or "competition" in item["tags"],
                    "review_status": "gold_candidate",
                    "latency_ceiling_sec": 20.0,
                    "notes": "Route/outcome ground truth. Do not require a frozen textual answer for live or clarification cases.",
                })
    return rows


def _question_key(value: str) -> str:
    return re.sub(r"\s+", " ", value.casefold()).strip()


def validate(rows: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    allowed_statuses = {"answer_available", "live_lookup_required", "clarification_required", "no_answer_expected"}
    required = {
        "id", "suite", "scenario_id", "locale", "variant", "group", "question",
        "expected_route_categories", "expected_answer_status", "expected_source_requirement",
        "difficulty", "behavior_tags", "critical", "review_status", "latency_ceiling_sec",
    }
    if len(rows) < 500:
        errors.append(f"Expected at least 500 rows, found {len(rows)}.")
    ids = [str(row.get("id")) for row in rows]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate IDs found.")
    for locale in ("th", "en"):
        locale_rows = [row for row in rows if row.get("locale") == locale]
        if len(locale_rows) < 250:
            errors.append(f"Expected at least 250 {locale} rows, found {len(locale_rows)}.")
        question_keys = [_question_key(str(row.get("question", ""))) for row in locale_rows]
        if len(question_keys) != len(set(question_keys)):
            errors.append(f"Duplicate normalized questions found for locale={locale}.")
    for row in rows:
        missing = required - row.keys()
        if missing:
            errors.append(f"{row.get('id')} missing {sorted(missing)}.")
        if row.get("suite") != SUITE:
            errors.append(f"{row.get('id')} has a wrong suite name.")
        if row.get("expected_answer_status") not in allowed_statuses:
            errors.append(f"{row.get('id')} has an invalid answer status.")
        if not str(row.get("question") or "").strip():
            errors.append(f"{row.get('id')} has an empty question.")
        if not row.get("expected_route_categories"):
            errors.append(f"{row.get('id')} has no expected route category.")
        if row.get("expected_answer_status") == "live_lookup_required" and row.get("expected_source_requirement") not in {"live_booking_api", "time_api"}:
            errors.append(f"{row.get('id')} is live but has no live source requirement.")
    expected_pair_count = len(SEEDS) * len(VARIANTS["th"])
    if sum(1 for row in rows if row["locale"] == "th") != expected_pair_count:
        errors.append("Thai scenario/variant matrix is incomplete.")
    if sum(1 for row in rows if row["locale"] == "en") != expected_pair_count:
        errors.append("English scenario/variant matrix is incomplete.")
    return errors


def report(rows: list[dict[str, Any]]) -> str:
    by_group = Counter(str(row["group"]) for row in rows)
    by_status = Counter(str(row["expected_answer_status"]) for row in rows)
    by_tag = Counter(tag for row in rows for tag in row["behavior_tags"])
    lines = [
        "# RAG Robustness Ground Truth v1",
        "",
        "ชุดทดสอบนี้วัด routing, target handling, source requirement และ safe outcome ก่อนวัดสำนวนคำตอบ เพื่อรองรับคำถามใหม่ คำถามกำกวม ภาษาพูด และภาษาไทย/อังกฤษที่ไม่เป็นทางการ.",
        "",
        f"- Total: {len(rows)}",
        f"- Thai: {sum(row['locale'] == 'th' for row in rows)}",
        f"- English: {sum(row['locale'] == 'en' for row in rows)}",
        f"- Critical safety cases: {sum(bool(row['critical']) for row in rows)}",
        "",
        "## Expected Outcome",
        "",
    ]
    lines.extend(f"- `{key}`: {value}" for key, value in sorted(by_status.items()))
    lines.extend(["", "## Coverage by Group", "", "| Group | Cases |", "| --- | ---: |"])
    lines.extend(f"| {key} | {value} |" for key, value in sorted(by_group.items()))
    lines.extend(["", "## Adversarial Coverage", ""])
    lines.extend(f"- `{key}`: {value}" for key, value in sorted(by_tag.items()))
    lines.extend([
        "",
        "## Evaluation Rules",
        "",
        "- `answer_available`: route ต้องถูก และคำตอบต้องไม่เป็น no-answer/clarification โดยไม่มีเหตุผล.",
        "- `live_lookup_required`: ต้องไปเส้นทางข้อมูลสด; ห้ามใช้คำตอบ snapshot เก่าเป็น Ground Truth.",
        "- `clarification_required`: ต้องขอข้อมูลที่ขาด เช่น เกม รายการแข่ง เวลา หรือ object อ้างอิง.",
        "- `no_answer_expected`: ต้องไม่แต่งข้อเท็จจริงหรือแสดง catalog ทั้งหมดเพื่อตอบ unknown entity.",
        "- ใช้ชุดนี้เป็น gold candidate ก่อนใช้นับคะแนน release: ข้อที่เป็น policy/time-sensitive ต้อง owner review ก่อน promote เป็น strict gold.",
    ])
    return "\n".join(lines) + "\n"


def write(rows: list[dict[str, Any]]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text("\n".join(json.dumps(row, ensure_ascii=False, sort_keys=True) for row in rows) + "\n", encoding="utf-8")
    REPORT_PATH.write_text(report(rows), encoding="utf-8")
    manifest = {
        "suite": SUITE,
        "generated_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "path": str(OUT_PATH),
        "total": len(rows),
        "locale_counts": dict(Counter(str(row["locale"]) for row in rows)),
        "group_counts": dict(Counter(str(row["group"]) for row in rows)),
        "schema": {
            "expected_route_categories": "one or more acceptable route categories",
            "expected_answer_status": "answer_available | live_lookup_required | clarification_required | no_answer_expected",
            "expected_source_requirement": "static source family required for a safe answer",
        },
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Generate corpus and reports.")
    parser.add_argument("--check", action="store_true", help="Validate generated corpus.")
    args = parser.parse_args()
    if not args.write and not args.check:
        parser.error("choose --write or --check")
    rows = build_rows()
    errors = validate(rows)
    if errors:
        print("Ground truth validation failed:", file=sys.stderr)
        print("\n".join(f"- {item}" for item in errors), file=sys.stderr)
        return 1
    if args.write:
        write(rows)
        print(f"Generated {len(rows)} bilingual RAG robustness cases at {OUT_PATH}")
    if args.check:
        if not OUT_PATH.exists():
            print("Generated corpus is missing; run with --write first.", file=sys.stderr)
            return 1
        existing = [json.loads(line) for line in OUT_PATH.read_text(encoding="utf-8").splitlines() if line.strip()]
        existing_errors = validate(existing)
        if existing_errors:
            print("Written corpus validation failed:", file=sys.stderr)
            print("\n".join(f"- {item}" for item in existing_errors), file=sys.stderr)
            return 1
        print(f"Ground truth is valid: {len(existing)} cases ({sum(row['locale'] == 'th' for row in existing)} TH / {sum(row['locale'] == 'en' for row in existing)} EN).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
