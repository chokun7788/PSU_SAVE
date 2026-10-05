from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EVAL_DIR = ROOT / "data" / "eval"
DEFAULT_MANIFEST = ROOT / "reports" / "current_flow_regression" / "20260901_full_model_enabled" / "cases_manifest.json"

PREFIXES = (
    "",
    "Please tell me: ",
    "Could you confirm: ",
    "I need to know: ",
    "Quick question: ",
)
SUFFIXES = (
    "",
    " Please answer briefly.",
    " Please use verified information.",
    " I need the official answer.",
    " Could you check this for me?",
)


@dataclass(frozen=True)
class GroupSpec:
    key: str
    count: int
    cases: tuple[dict[str, Any], ...]


def _case(
    question: str,
    categories: tuple[str, ...],
    *,
    contains: tuple[str, ...] = (),
    contains_any: tuple[str, ...] = (),
    excludes: tuple[str, ...] = (),
    status: str = "answer_available",
    critical: bool = False,
) -> dict[str, Any]:
    return {
        "question": question,
        "expected_categories": list(categories),
        "must_contain": list(contains),
        "must_contain_any": list(contains_any),
        "must_not_contain": list(excludes),
        "expected_answer_status": status,
        "critical_fact": critical,
    }


GROUPS = (
    GroupSpec("service_fee", 50, (
        _case("How much is one hour on PC for a PSU student?", ("service_fee",), contains=("0 THB",), critical=True),
        _case("What is the one-hour PC price for a general adult?", ("service_fee",), contains=("70 THB",), critical=True),
        _case("How much does PS5 cost for PSU staff?", ("service_fee",), contains=("0 THB",), critical=True),
        _case("What is the Nintendo Switch price for four players?", ("service_fee",), contains=("Nintendo", "THB"), critical=True),
        _case("How much is VR for 30 minutes?", ("service_fee",), contains=("30 minutes", "THB"), critical=True),
        _case("How much is VR for one hour for an alumnus?", ("service_fee",), contains=("1 hour", "THB"), critical=True),
        _case("What does the cockpit cost for two hours?", ("service_fee",), contains=("2 sessions", "THB"), critical=True),
    )),
    GroupSpec("schedule", 45, (
        _case("Is the studio open on Monday morning?", ("schedule", "reservation"), contains=("maintenance", "09:00-12:00"), critical=True),
        _case("When can I play on Monday afternoon?", ("schedule", "reservation"), contains=("13:00-16:00",), critical=True),
        _case("What are the opening hours on Wednesday?", ("schedule", "reservation"), contains=("Wednesday", "09:00-12:00", "13:00-16:00"), critical=True),
        _case("Is Friday afternoon open?", ("schedule", "reservation"), contains=("maintenance", "13:00-16:00"), critical=True),
        _case("Is the studio open 24 hours?", ("schedule", "reservation"), contains=("not open 24 hours",), critical=True),
        _case("What time is the morning session?", ("schedule", "reservation"), contains=("09:00-12:00",), critical=True),
        _case("What time is the afternoon session?", ("schedule", "reservation"), contains=("13:00-16:00",), critical=True),
    )),
    GroupSpec("games", 60, (
        _case("What games are available?", ("games",), contains=("Verified game catalog",)),
        _case("What PC games are available?", ("games",), contains_any=("VALORANT", "Counter-Strike 2")),
        _case("Which games can I play on PS5?", ("games",), contains=("PlayStation 5",)),
        _case("What games are on Nintendo Switch?", ("games",), contains=("Nintendo Switch",)),
        _case("Can I play Beat Saber in the VR Zone?", ("games",), contains=("Beat Saber",)),
        _case("Can I play Gran Turismo 7 with the cockpit?", ("games",), contains=("Gran Turismo 7",)),
        _case("Can I play Minecraft at the studio?", ("games",), contains=("Minecraft",), excludes=("Verified game catalog",)),
        _case("Tell me about VALORANT", ("games",), contains=("English localization",), status="localization_pending"),
        _case("How do I play Overcooked 2?", ("games",), contains=("English localization",), status="localization_pending"),
    )),
    GroupSpec("equipment", 45, (
        _case("What equipment is available in the PC Zone?", ("equipment",), contains=("Verified equipment", "PC Zone")),
        _case("What equipment is available in the VR Zone?", ("equipment",), contains=("Verified equipment", "VR Zone")),
        _case("What equipment is in the Nintendo Switch Zone?", ("equipment",), contains=("Nintendo Switch",)),
        _case("Does the PC Zone have gaming monitors?", ("equipment",), contains_any=("Gaming Monitor", "Gaming Monitors")),
        _case("What is the Gaming PC used for?", ("equipment",), contains=("English localization",), status="localization_pending"),
    )),
    GroupSpec("booking", 55, (
        _case("How do I make a booking?", ("reservation",), contains=("select a service", "upload the payment slip"), critical=True),
        _case("What information do I need to book?", ("reservation",), contains=("Student ID", "phone number"), critical=True),
        _case("How do I pay for my booking?", ("reservation",), contains=("Siam Commercial Bank", "795-276244-1"), critical=True),
        _case("How long do I have to pay after booking?", ("reservation",), contains=("10 minutes",), critical=True),
        _case("When should I check in?", ("reservation",), contains=("30 minutes",), critical=True),
        _case("Can I cancel my booking?", ("reservation",), contains=("1 hour",), critical=True),
        _case("Can I get a refund?", ("reservation",), contains=("refund",), critical=True),
        _case("How many sessions can one booking include?", ("reservation",), contains=("3 sessions",), critical=True),
        _case("Which PC is available now?", ("no_answer",), contains=("not connected",), status="safe_no_answer", critical=True),
    )),
    GroupSpec("rules_penalty", 45, (
        _case("Can I bring food into the studio?", ("rules",), contains=("designated areas",), critical=True),
        _case("Are drinks allowed?", ("rules",), contains=("designated areas",), critical=True),
        _case("Can I smoke inside the studio?", ("rules",), contains=("prohibited",), critical=True),
        _case("What are the studio rules?", ("rules",), contains=("Key studio rules",), critical=True),
        _case("What happens if I damage equipment?", ("penalty",), contains=("100-500 THB", "500-2,000 THB"), critical=True),
        _case("What are the damage penalties?", ("penalty",), contains=("full compensation",), critical=True),
        _case("Who should I tell if a machine has a problem?", ("rules",), contains=("notify staff",), critical=True),
        _case("Are pets allowed in the studio?", ("no_answer",), contains=("No information",), status="safe_no_answer"),
    )),
    GroupSpec("competition", 35, (
        _case("What are the competition rules?", ("competition_rules",), contains=("English localization",), status="localization_pending", critical=True),
        _case("What happens if a player is late for a match?", ("competition_rules",), contains=("English localization",), status="localization_pending", critical=True),
        _case("Are substitutes allowed in the tournament?", ("competition_rules",), contains=("English localization",), status="localization_pending", critical=True),
        _case("What is the pause rule during a competition?", ("competition_rules",), contains=("English localization",), status="localization_pending", critical=True),
        _case("How does the tournament bracket work?", ("competition_rules",), contains=("English localization",), status="localization_pending"),
    )),
    GroupSpec("members_about_contact", 25, (
        _case("What is PSU Esports Studio - Phuket?", ("overview",), contains=("esports learning development studio",)),
        _case("Who operates PSU Esports Studio?", ("overview",), contains=("College of Computing",)),
        _case("Where is the studio?", ("contact",), contains=("Phuket Campus",)),
        _case("How can I contact the studio?", ("contact",), contains=("psuesportspkt@gmail.com",)),
        _case("Who are the studio members?", ("overview",), contains=("English localization",), status="localization_pending"),
    )),
    GroupSpec("rag_knowledge", 25, (
        _case("Explain the latest verified studio announcement.", ("no_answer", "events_news", "knowledge"), status="localization_pending"),
        _case("Summarize the detailed game policy from the knowledge base.", ("no_answer", "knowledge", "rules"), status="localization_pending"),
        _case("What does the studio document say about esports learning?", ("no_answer", "knowledge", "overview"), status="localization_pending"),
        _case("Give me the verified long-form guidance for using the studio.", ("no_answer", "knowledge", "rules"), status="localization_pending"),
    )),
    GroupSpec("clarification_no_answer", 15, (
        _case("How much does it cost?", ("no_answer", "service_fee"), status="safe_clarification"),
        _case("Where can I play it?", ("no_answer", "games"), status="safe_clarification"),
        _case("Tell me more about that.", ("no_answer",), status="safe_clarification"),
        _case("Can I use an unknown game called Example Quest?", ("games",), contains=("Example Quest",), excludes=("Verified game catalog",), status="safe_no_answer"),
        _case("Do you offer overnight accommodation?", ("no_answer",), contains=("No information",), status="safe_no_answer"),
    )),
)


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in rows)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    temporary.replace(path)


def build_gold() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    seen_questions: set[str] = set()
    for group in GROUPS:
        variants: list[dict[str, Any]] = []
        # Cover every semantic base question before adding another wording
        # variant. This prevents a large group from being filled by the first
        # one or two base questions only.
        for prefix in PREFIXES:
            for suffix in SUFFIXES:
                for source in group.cases:
                    question = f"{prefix}{source['question']}{suffix}".strip()
                    if question.casefold() in seen_questions:
                        continue
                    variants.append({**source, "question": question, "base_question": source["question"], "variant_index": len(variants) + 1})
        if len(variants) < group.count:
            raise RuntimeError(f"Not enough unique variants for {group.key}: {len(variants)} < {group.count}")
        for index, variant in enumerate(variants[: group.count], 1):
            seen_questions.add(variant["question"].casefold())
            rows.append({
                "id": f"EN-GOLD-{len(rows) + 1:04d}",
                "suite": "english_gold",
                "group": group.key,
                "locale": "en",
                "review_status": "gold_candidate",
                "question": variant["question"],
                "base_question": variant["base_question"],
                "expected_categories": variant["expected_categories"],
                "must_contain": variant["must_contain"],
                "must_contain_any": variant["must_contain_any"],
                "must_not_contain": variant["must_not_contain"],
                "expected_answer_status": variant["expected_answer_status"],
                "critical_fact": variant["critical_fact"],
                "latency_ceiling_sec": 10.0,
            })
        covered_bases = {row["base_question"] for row in rows if row["group"] == group.key}
        expected_bases = {case["question"] for case in group.cases}
        if covered_bases != expected_bases:
            missing = sorted(expected_bases - covered_bases)
            raise RuntimeError(f"English Gold group {group.key} misses base questions: {missing}")
    if len(rows) != 400:
        raise RuntimeError(f"English Gold must contain 400 rows, got {len(rows)}")
    if len({row["id"] for row in rows}) != 400 or len({row["question"].casefold() for row in rows}) != 400:
        raise RuntimeError("English Gold contains duplicate IDs or questions")
    return rows


def build_shadow(manifest_path: Path) -> list[dict[str, Any]]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    faq = [row["case"] for row in manifest if row.get("suite") == "faq"]
    if len(faq) != 1600:
        raise RuntimeError(f"Expected 1,600 FAQ source cases, got {len(faq)}")
    rows = []
    for index, case in enumerate(faq, 1):
        question_th = str(case.get("question") or "")
        source_hash = hashlib.sha256(question_th.encode("utf-8")).hexdigest()
        rows.append({
            "id": f"EN-SHADOW-{index:04d}",
            "suite": "english_shadow",
            "source_case_id": case.get("id"),
            "question_th": question_th,
            "question_en": "",
            "translation_status": "needs_human_review",
            "source_question_sha256": source_hash,
            "expected_category": case.get("expected_category"),
            "expected_mode_prefix": case.get("expected_mode_prefix"),
            "quality_bucket": case.get("quality_bucket"),
            "risk": case.get("risk"),
            "source": case.get("source"),
        })
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate the English Gold candidate and the 1,600-case reviewed-shadow queue.")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--gold-output", type=Path, default=EVAL_DIR / "english_gold_400_20260902.jsonl")
    parser.add_argument("--shadow-output", type=Path, default=EVAL_DIR / "english_shadow_1600_20260902.jsonl")
    args = parser.parse_args()

    gold = build_gold()
    shadow = build_shadow(args.manifest)
    _write_jsonl(args.gold_output, gold)
    _write_jsonl(args.shadow_output, shadow)
    counts = {group.key: group.count for group in GROUPS}
    print(json.dumps({
        "ok": True,
        "gold_count": len(gold),
        "gold_groups": counts,
        "gold_output": str(args.gold_output),
        "shadow_count": len(shadow),
        "shadow_review_ready": sum(row["translation_status"] == "approved" for row in shadow),
        "shadow_output": str(args.shadow_output),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
