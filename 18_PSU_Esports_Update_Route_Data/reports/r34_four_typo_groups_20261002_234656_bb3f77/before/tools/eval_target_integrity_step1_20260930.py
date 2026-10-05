"""Compare the affected r18 equipment/member pairs with the first target fix."""
from __future__ import annotations

import json
import argparse
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.run_bilingual_2000_typo_eval_20260929 import read_rows, run_case


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "reports/target_integrity_step1_20260930/paired_affected_domains.jsonl")
    output = parser.parse_args().output
    summary_path = output.with_suffix(".summary.json")
    if output.exists() or summary_path.exists():
        raise SystemExit("Refusing to overwrite existing target-integrity evidence")
    fixture = read_rows(ROOT / "data/eval/master_gt_bilingual_multi_error_2000_20260929_r15.jsonl")
    baseline = {
        row["id"]: row
        for locale in ("th", "en")
        for row in read_rows(ROOT / f"reports/typo_r16_20260930/paired_{locale}_r18.jsonl")
    }
    cases = [row for row in fixture if row["domain"] in {"equipment", "members_overview_contact"}]
    results = []
    with output.open("x", encoding="utf-8") as stream:
        for index, case in enumerate(cases, 1):
            clean, noisy = run_case(case, "clean_question"), run_case(case, "noisy_question")
            old = baseline[case["id"]]
            record = {
                "id": case["id"], "locale": case["locale"], "domain": case["domain"],
                "review_status": case["review_status"],
                "clean": clean, "noisy": noisy,
                "r18_clean_passed": old["clean"]["passed"],
                "r18_noisy_passed": old["noisy"]["passed"],
                "clean_worsened": bool(old["clean"]["passed"] and not clean["passed"]),
                "noisy_worsened": bool(old["noisy"]["passed"] and not noisy["passed"]),
                "noisy_improved": bool(not old["noisy"]["passed"] and noisy["passed"]),
            }
            results.append(record)
            stream.write(json.dumps(record, ensure_ascii=False) + "\n")
            stream.flush()
            if index % 25 == 0 or index == len(cases):
                print(f"{index}/{len(cases)} clean_worsened={sum(r['clean_worsened'] for r in results)} "
                      f"noisy_worsened={sum(r['noisy_worsened'] for r in results)}", flush=True)
    report = {
        "count": len(results), "by_locale": dict(Counter(r["locale"] for r in results)),
        "old_clean_pass": sum(r["r18_clean_passed"] for r in results),
        "new_clean_pass": sum(r["clean"]["passed"] for r in results),
        "old_noisy_pass": sum(r["r18_noisy_passed"] for r in results),
        "new_noisy_pass": sum(r["noisy"]["passed"] for r in results),
        "clean_worsened": [r["id"] for r in results if r["clean_worsened"]],
        "noisy_worsened": [r["id"] for r in results if r["noisy_worsened"]],
        "noisy_improved": [r["id"] for r in results if r["noisy_improved"]],
        "interpretation": "Frozen candidate GT with deterministic paths; no live/owner truth asserted.",
    }
    with summary_path.open("x", encoding="utf-8") as stream:
        json.dump(report, stream, ensure_ascii=False, indent=2)
    print(json.dumps(report, ensure_ascii=False), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
