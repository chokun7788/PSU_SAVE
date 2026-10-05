from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "reports/master_ground_truth_eval"
DEFAULT_BASELINE = REPORT_DIR / "master_gt_eval_20260924_195543.json"
DEFAULT_REVIEW = REPORT_DIR / "intent_trap_review_bilingual_assisted_20260924.json"


def _read_rows(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"Expected a raw evaluation list: {path}")
    return data


def _percentile(values: list[float], percentile: int) -> float:
    ordered = sorted(values)
    return ordered[max(0, (len(ordered) * percentile + 99) // 100 - 1)] if ordered else 0.0


def _check_protected(row: dict) -> list[str]:
    domain = row["domain"]
    locale = row["locale"]
    answer = row["answer"]
    lowered = answer.casefold()
    failures = []
    if domain == "food_bring_scope":
        if row["actual_route"] != "rules" or row["mode"] != "pipeline:protected_food_bring_permission":
            failures.append("wrong_food_facet_or_route")
        if locale == "th":
            if "นำอาหารหรือเครื่องดื่มเข้ามาได้" not in answer or "พื้นที่ที่ศูนย์กำหนด" not in answer:
                failures.append("missing_direct_bring_answer_or_area_limit")
        elif "you may bring" not in lowered or "designated areas" not in lowered:
            failures.append("missing_direct_bring_answer_or_area_limit")
    else:
        if row["actual_route"] != "reservation" or row["mode"] != "pipeline:protected_public_access":
            failures.append("wrong_eligibility_facet_or_route")
        if locale == "th":
            if not any(token in answer for token in ("ได้ครับ", "จองได้", "ไม่จำเป็น")):
                failures.append("missing_direct_access_answer")
        elif not any(token in lowered for token in ("yes.", "you do not need")):
            failures.append("missing_direct_access_answer")
        if re.search(r"\b\d+[,.]?\d*\s*(?:thb|baht)\b|\d+[,.]?\d*\s*บาท", lowered):
            failures.append("unrequested_specific_price")
        if 146 <= int(row["id"].rsplit("-", 1)[-1]) <= 150:
            if ("บัตรประชาชน" if locale == "th" else "national id card") not in lowered:
                failures.append("missing_requested_checkin_id")
    if "https://esports.computing.psu.ac.th/" not in answer:
        failures.append("missing_source_url")
    if any(token in lowered for token in ("verified equipment:", "อุปกรณ์บนหน้า home", "ยังยืนยันไม่ได้", "cannot verify")):
        failures.append("generic_inventory_or_unverified_fallback")
    if row["elapsed_sec"] > 20:
        failures.append("over_20_seconds")
    return failures


def analyze(protected_path: Path, unclear_path: Path, *, baseline_path: Path = DEFAULT_BASELINE,
            review_path: Path = DEFAULT_REVIEW) -> dict:
    protected = _read_rows(protected_path)
    unclear = _read_rows(unclear_path)
    baseline = {row["id"]: row for row in _read_rows(baseline_path)}
    review = json.loads(review_path.read_text(encoding="utf-8"))
    feedback = {row["id"]: row for row in review["decisions"]}
    if len(protected) != 300 or len(unclear) != 100 or len(feedback) != 400:
        raise ValueError("Expected 300 protected, 100 unclear, and 400 feedback cases")
    rows = protected + unclear
    if len({row["id"] for row in rows}) != 400 or any(row["id"] not in baseline or row["id"] not in feedback for row in rows):
        raise ValueError("Run IDs do not match baseline and feedback")
    checks = []
    for row in rows:
        previous = baseline[row["id"]]
        failures = _check_protected(row) if row in protected else []
        if row in unclear:
            if row["answer"] != previous["answer"] or row["actual_route"] != previous["actual_route"]:
                failures.append("unclear_answer_or_route_changed")
            if row["elapsed_sec"] > 20:
                failures.append("over_20_seconds")
        checks.append({
            "id": row["id"], "locale": row["locale"], "domain": row["domain"],
            "route": row["actual_route"], "mode": row["mode"], "elapsed_sec": row["elapsed_sec"],
            "feedback_decision": feedback[row["id"]]["decision"],
            "feedback_origin": feedback[row["id"]]["origin"],
            "contract_ok": not failures, "failures": failures,
        })
    by_domain = {}
    for domain in sorted({row["domain"] for row in checks}):
        subset = [row for row in checks if row["domain"] == domain]
        by_domain[domain] = {"total": len(subset), "contract_ok": sum(row["contract_ok"] for row in subset)}
    times = [float(row["elapsed_sec"]) for row in rows]
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "protected_run": str(protected_path), "unclear_run": str(unclear_path),
        "baseline_sha256": hashlib.sha256(baseline_path.read_bytes()).hexdigest(),
        "feedback_file": str(review_path),
        "feedback_origins": dict(Counter(row["origin"] for row in feedback.values())),
        "total": 400,
        "contract_ok": sum(row["contract_ok"] for row in checks),
        "by_domain": by_domain,
        "latency_sec": {"p50": _percentile(times, 50), "p95": _percentile(times, 95), "max": max(times)},
        "checks": checks,
        "warning": "Contract alignment is not human-verified answer accuracy; food-bring permission still needs explicit owner policy wording.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Analyze review-grounded intent-trap runs without changing raw gold.")
    parser.add_argument("--protected-run", required=True, type=Path)
    parser.add_argument("--unclear-run", required=True, type=Path)
    parser.add_argument("--baseline", type=Path, default=DEFAULT_BASELINE)
    parser.add_argument("--review", type=Path, default=DEFAULT_REVIEW)
    parser.add_argument("--output", type=Path, default=REPORT_DIR / "review_grounded_400_analysis_20260924.json")
    args = parser.parse_args()
    report = analyze(args.protected_run, args.unclear_run, baseline_path=args.baseline, review_path=args.review)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Contract-aligned {report['contract_ok']}/{report['total']}; P95 {report['latency_sec']['p95']}s; max {report['latency_sec']['max']}s")
    print(f"Report: {args.output}")
    return 0 if report["contract_ok"] == report["total"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
