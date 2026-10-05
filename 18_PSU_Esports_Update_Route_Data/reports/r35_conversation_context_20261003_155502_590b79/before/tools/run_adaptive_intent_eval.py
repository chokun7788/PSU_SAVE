from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402


REPORT_DIR = ROOT / "reports" / "adaptive_intent_eval"


CASES: list[dict[str, Any]] = [
    {
        "id": "AI-EXACT-001",
        "question": "PS5 ราคาเท่าไหร่",
        "expected_category": "service_fee",
        "expected_domain": "service_fee",
        "expected_operation": "price_calculate",
        "expect_llm_attempted": False,
        "notes": "exact price question should stay deterministic",
    },
    {
        "id": "AI-EXACT-002",
        "question": "TEKKEN 8 ปุ่มทั้งหมดมีอะไรบ้าง",
        "expected_category": "games",
        "expected_domain": "game_controls",
        "expected_operation": "control",
        "expect_llm_attempted": False,
        "notes": "exact game-control question should not wait for LLM",
    },
    {
        "id": "AI-EXACT-003",
        "question": "สมาชิก PSU Esport มีกี่หมวด",
        "expected_category": "overview",
        "expected_domain": "members",
        "expected_operation": "group_count",
        "expect_llm_attempted": False,
        "notes": "exact group count should stay structured",
    },
    {
        "id": "AI-EXACT-004",
        "question": "วันจันทร์เปิดกี่โมง",
        "expected_category": "schedule",
        "expected_domain": "schedule",
        "expected_operation": "schedule_lookup",
        "expect_llm_attempted": False,
        "notes": "exact schedule lookup should stay fast/structured",
    },
    {
        "id": "AI-REVIEW-001",
        "question": "ตอนนี้สตาฟมีใครบ้าง",
        "expected_category": "overview",
        "expected_domain": "members",
        "expected_operation": "list",
        "expect_llm_attempted": True,
        "notes": "broad staff wording benefits from intent review",
    },
    {
        "id": "AI-REVIEW-002",
        "question": "เกมตอนนี้มีเกมอะไรบ้าง",
        "expected_category": "games",
        "expected_domain": "games",
        "expected_operation": "list",
        "expect_llm_attempted": True,
        "notes": "broad game catalog wording should be reviewed",
    },
    {
        "id": "AI-REVIEW-003",
        "question": "อยากเล่นรถแข่งต้องใช้อะไร",
        "expected_category": "equipment",
        "expected_domain": "equipment",
        "expected_operation": "how_to",
        "expect_llm_attempted": True,
        "notes": "ambiguous racing question can mean equipment or games",
    },
    {
        "id": "AI-REVIEW-004",
        "question": "เกมแนว MOBA มีอะไรบ้าง",
        "expected_category": "games",
        "expected_domain": "games",
        "expected_operation": "list",
        "expect_llm_attempted": True,
        "notes": "genre wording should be reviewed instead of falling into equipment",
    },
]


def _universal_trace(result: Any) -> dict[str, Any]:
    for trace in getattr(result, "trace", []) or []:
        if getattr(trace, "stage", "") == "universal_intent":
            return {
                "decision": getattr(trace, "decision", ""),
                "confidence": getattr(trace, "confidence", 0.0),
                "detail": getattr(trace, "detail", ""),
                "metadata": getattr(trace, "metadata", {}) or {},
            }
    return {"decision": "", "confidence": 0.0, "detail": "", "metadata": {}}


def _evaluate_case(case: dict[str, Any]) -> dict[str, Any]:
    result = answer_question_pipeline_debug(
        str(case["question"]),
        experimental_rag_fallback=True,
        experimental_allow_llm=True,
    )
    intent = result.universal_intent
    trace = _universal_trace(result)
    metadata = trace["metadata"]
    llm_attempted = bool(metadata.get("llm_attempted"))
    expected_category = str(case["expected_category"])
    expected_domain = str(case["expected_domain"])
    expected_operation = str(case["expected_operation"])

    route_ok = result.route.category == expected_category
    intent_ok = bool(intent and intent.domain == expected_domain and intent.operation == expected_operation)
    llm_gate_ok = llm_attempted == bool(case["expect_llm_attempted"])
    passed = route_ok and intent_ok and llm_gate_ok and result.validation.ok

    return {
        "id": case["id"],
        "passed": passed,
        "question": case["question"],
        "expected_category": expected_category,
        "expected_domain": expected_domain,
        "expected_operation": expected_operation,
        "expect_llm_attempted": case["expect_llm_attempted"],
        "actual_category": result.route.category,
        "actual_intent": result.route.intent,
        "actual_domain": intent.domain if intent else "",
        "actual_operation": intent.operation if intent else "",
        "actual_method": intent.method if intent else "",
        "llm_attempted": llm_attempted,
        "llm_first": bool(metadata.get("llm_first")),
        "llm_first_skip_reason": str(metadata.get("llm_first_skip_reason") or ""),
        "llm_first_review_reason": str(metadata.get("llm_first_review_reason") or ""),
        "llm_rejected_reason": str(metadata.get("llm_rejected_reason") or ""),
        "intent_candidates": metadata.get("intent_candidates") or [],
        "mode": result.mode,
        "elapsed": result.elapsed,
        "validation_ok": result.validation.ok,
        "answer": result.answer,
        "notes": case.get("notes", ""),
    }


def _write_reports(rows: list[dict[str, Any]]) -> tuple[Path, Path]:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_path = REPORT_DIR / f"adaptive_intent_eval_{stamp}.json"
    csv_path = REPORT_DIR / f"adaptive_intent_eval_{stamp}.csv"
    json_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")

    fields = [
        "id",
        "passed",
        "question",
        "expected_category",
        "expected_domain",
        "expected_operation",
        "expect_llm_attempted",
        "actual_category",
        "actual_intent",
        "actual_domain",
        "actual_operation",
        "actual_method",
        "llm_attempted",
        "llm_first",
        "llm_first_skip_reason",
        "llm_first_review_reason",
        "llm_rejected_reason",
        "mode",
        "elapsed",
        "validation_ok",
        "notes",
        "answer",
    ]
    with csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})
    return json_path, csv_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Run adaptive Intent LLM gate evaluation.")
    parser.add_argument("--model", default=os.getenv("PSU_INTENT_LLM_MODEL") or os.getenv("PSU_CHATBOT_OLLAMA_MODEL", "scb10x/typhoon2.5-qwen3-4b"))
    parser.add_argument("--timeout", type=float, default=float(os.getenv("PSU_INTENT_LLM_TIMEOUT_SEC", "8")))
    parser.add_argument("--num-predict", type=int, default=int(os.getenv("PSU_INTENT_LLM_NUM_PREDICT", "50")))
    parser.add_argument("--fail-on-error", action="store_true")
    args = parser.parse_args()

    os.environ["PSU_UNIVERSAL_INTENT_LLM"] = "1"
    os.environ["PSU_UNIVERSAL_INTENT_LLM_FIRST"] = "1"
    os.environ["PSU_INTENT_LLM_FIRST_ONLY_WEAK"] = "1"
    os.environ["PSU_INTENT_LLM_MODEL"] = args.model
    os.environ["PSU_INTENT_LLM_TIMEOUT_SEC"] = str(args.timeout)
    os.environ["PSU_INTENT_LLM_NUM_PREDICT"] = str(args.num_predict)

    rows = [_evaluate_case(case) for case in CASES]
    for index, row in enumerate(rows, start=1):
        status = "PASS" if row["passed"] else "FAIL"
        print(
            f"[{index}/{len(rows)}] {status} {row['id']} "
            f"llm_attempted={row['llm_attempted']} method={row['actual_method']} "
            f"intent={row['actual_domain']}/{row['actual_operation']} elapsed={row['elapsed']}"
        )

    json_path, csv_path = _write_reports(rows)
    passed_count = sum(1 for row in rows if row["passed"])
    failed_count = len(rows) - passed_count
    print(f"ADAPTIVE INTENT EVAL: {passed_count}/{len(rows)} passed, {failed_count} failed")
    print(f"JSON: {json_path}")
    print(f"CSV: {csv_path}")
    return 1 if failed_count and args.fail_on_error else 0


if __name__ == "__main__":
    raise SystemExit(main())
