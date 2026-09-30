from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "reports/master_ground_truth_eval/master_gt_eval_20260924_195543_intent_trap_manual_review_v2.jsonl"
OUTPUT = ROOT / "reports/master_ground_truth_eval/intent_trap_review_bilingual_assisted_20260924.json"

# These are translations of the reviewer's comments, not approved policy text.
NOTE_EN = {
    "": "",
    "จริงๆมีแต่จะมีค่าบริการตามสถานะว่าเป็นใคร": "Visitors may use the studio, but fees depend on their user group.",
    "สามารถจองได้แต่อาจมีค่าบริการ": "Visitors can book, but a service fee may apply.",
    "ไม่จำเป็นสามารถจองได้เลย แต่อาจเสียค่าใช้บริการ": "Membership is not required; visitors can book, though a service fee may apply.",
    "สามารถใช้ได้หมด แต่อาจมีค่าบริการตามสถานะต่างๆ": "Visitors may use the services, though fees may vary by user group.",
    "แค่จองกับโอนเงินก็สามารถใช้ได้เลย": "Booking and making the required bank transfer are enough to use the service.",
    "สามารถเอาเข้าไปได้": "You may bring it inside.",
    "ได้เฉพาะตามที่กำหนดเท่านั้น": "Only in the designated areas.",
    "ตอบคำตอบหลักไปก่อนว่าเค้าต้องการอะไร แล้วค่อยเสริมรายละเอียด/กฏไปให้อ่านอีกที": "Answer the specific question first, then add relevant details or rules.",
    "สามารถใช้ได้ แต่อาจมีราคา/ค่าใช้จ่ายตามสถานะ": "Visitors may use it, but fees may depend on their user group.",
    "สามารถใช้ได้ทุกคน แต่อาจมีราคา/ค่าใช้จ่ายตามสถานะ": "Anyone may use it, though fees may vary by user group.",
    "ควรตอบให้มันจัดการปัญหานี้อ่ะ ประมาณว่ามันสามารถถามตอบได้แค่ที่อยู่ในขอบเขตของตัวเองเท่านั้น": "Explain that this assistant answers only questions within its PSU Esports scope, then offer relevant topics.",
    "สามารถจองได้แต่อาจมีค่าบริการตามสถานะ": "Visitors can book, but fees may depend on their user group.",
}

GUIDANCE_NOTES = {
    "ตอบคำตอบหลักไปก่อนว่าเค้าต้องการอะไร แล้วค่อยเสริมรายละเอียด/กฏไปให้อ่านอีกที",
    "ควรตอบให้มันจัดการปัญหานี้อ่ะ ประมาณว่ามันสามารถถามตอบได้แค่ที่อยู่ในขอบเขตของตัวเองเท่านั้น",
}


def _case_number(case_id: str) -> int:
    return int(case_id.rsplit("-", 1)[-1])


def _question_warnings(item: dict, note: str) -> list[str]:
    number = _case_number(item["id"])
    warnings = []
    if 201 <= number <= 202 and note == "แค่จองกับโอนเงินก็สามารถใช้ได้เลย":
        warnings.append("note_about_booking_on_food_question")
    if 146 <= number <= 150 and note == "แค่จองกับโอนเงินก็สามารถใช้ได้เลย":
        warnings.append("note_does_not_specify_requested_id")
    return warnings


def project(review_path: Path, corpus_path: Path = CORPUS) -> dict:
    raw = corpus_path.read_bytes()
    corpus = [json.loads(line) for line in raw.decode("utf-8").splitlines() if line.strip()]
    by_id = {item["id"]: item for item in corpus}
    review = json.loads(review_path.read_text(encoding="utf-8"))
    if len(corpus) != 400 or len(by_id) != 400:
        raise ValueError("Expected 400 unique corpus cases")
    if review.get("source_sha256") != hashlib.sha256(raw).hexdigest():
        raise ValueError("Review file does not match the frozen 400-case corpus")

    manual = {entry["id"]: entry for entry in review["decisions"]}
    if len(manual) != len(review["decisions"]) or any(case_id not in by_id for case_id in manual):
        raise ValueError("Review contains a duplicate or unknown case ID")
    if any(entry.get("decision") not in {"correct", "partial", "incorrect"} for entry in manual.values()):
        raise ValueError("Review contains an unsupported decision")
    unknown_notes = {entry.get("note", "") for entry in manual.values()} - NOTE_EN.keys()
    if unknown_notes:
        raise ValueError(f"Translate new reviewer notes before projection: {unknown_notes}")

    now = datetime.now(timezone.utc).isoformat()
    decisions = {case_id: {**entry, "origin": "user_manual"} for case_id, entry in manual.items()}

    # The sole unmarked Thai case belongs to a five-wrapper scenario. Only infer
    # it if all four sibling decisions and notes agree exactly.
    for item in corpus:
        if item["locale"] != "th" or item["id"] in decisions:
            continue
        number = _case_number(item["id"])
        first = number - (number - 1) % 5
        siblings = [decisions.get(f"INTENT-TRAP-TH-{index:04d}") for index in range(first, first + 5) if index != number]
        if len(siblings) == 4 and all(siblings) and len({(row["decision"], row.get("note", "")) for row in siblings}) == 1:
            sibling = siblings[0]
            decisions[item["id"]] = {
                "id": item["id"], "decision": sibling["decision"], "note": sibling.get("note", ""),
                "origin": "assistant_projected", "source_id": f"INTENT-TRAP-TH-{first + 1:04d}",
                "updated_at": now, "warnings": ["not_manually_reviewed_in_thai"],
            }

    for item in corpus:
        if item["locale"] != "en":
            continue
        thai_id = item["id"].replace("-EN-", "-TH-")
        thai = decisions.get(thai_id)
        if not thai:
            continue
        source_item = by_id[thai_id]
        note_th = thai.get("note", "")
        warnings = _question_warnings(item, note_th)
        if (source_item["actual_route"], source_item["actual_status"]) != (item["actual_route"], item["actual_status"]):
            warnings.append("english_route_or_status_differs_from_thai")
        decision = thai["decision"]
        if 451 <= _case_number(item["id"]) <= 455 or 471 <= _case_number(item["id"]) <= 475:
            decision = "partial"
            warnings.append("english_answer_less_helpful_than_thai")
        note_en = NOTE_EN[note_th]
        display_note = note_en
        if "note_about_booking_on_food_question" in warnings:
            display_note = "The Thai reviewer note concerns booking/payment, not bringing food. Confirm the intended food policy before using it as an answer."
        elif "note_does_not_specify_requested_id" in warnings:
            display_note = "The Thai reviewer note mentions booking/payment but does not identify which ID or documents are required. Confirm the document policy."
        if item["id"] in decisions:
            # Keep the one English decision the user already made.
            existing = decisions[item["id"]]
            existing["reference_note_en"] = note_en
            existing["reference_note_th"] = note_th
            existing["warnings"] = warnings
            continue
        decisions[item["id"]] = {
            "id": item["id"], "decision": decision, "note": display_note,
            "origin": "assistant_projected", "source_id": thai_id,
            "source_note_th": note_th, "translated_source_note_en": note_en,
            "note_kind": "response_guidance" if note_th in GUIDANCE_NOTES else "reviewer_feedback",
            "updated_at": now, "warnings": warnings,
        }

    ordered = [decisions[item["id"]] for item in corpus if item["id"] in decisions]
    origins = Counter(entry["origin"] for entry in ordered)
    by_locale = {locale: dict(Counter(decisions[item["id"]]["decision"] for item in corpus if item["locale"] == locale and item["id"] in decisions)) for locale in ("th", "en")}
    return {
        "schema_version": 1,
        "source_file": corpus_path.name,
        "source_sha256": hashlib.sha256(raw).hexdigest(),
        "source_review_file": review_path.name,
        "exported_at": now,
        "total": len(corpus),
        "reviewed": len(ordered),
        "manual_reviewed": origins["user_manual"],
        "assistant_projected": origins["assistant_projected"],
        "policy_claims_require_source_approval": True,
        "counts_by_locale": by_locale,
        "decisions": ordered,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Translate and project the Thai intent-trap review onto paired English cases.")
    parser.add_argument("--review", type=Path, required=True)
    parser.add_argument("--corpus", type=Path, default=CORPUS)
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    result = project(args.review, args.corpus)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {args.output}: {result['manual_reviewed']} manual, {result['assistant_projected']} projected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
