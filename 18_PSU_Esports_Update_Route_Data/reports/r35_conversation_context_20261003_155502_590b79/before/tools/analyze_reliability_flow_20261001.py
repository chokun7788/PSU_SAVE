"""Compare immutable results and separate runtime deltas from scoring changes."""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.eval_contract_v2 import rescore_pair


def read(path):
    return [json.loads(line) for line in Path(path).read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def summary(rows):
    return {
        "count": len(rows), "clean_pass": sum(r["clean"]["passed"] for r in rows),
        "noisy_pass": sum(r["noisy"]["passed"] for r in rows),
        "regressions": sum(r["regression"] for r in rows),
        "exceptions": sum(r[k]["mode"] == "pipeline_exception" for r in rows for k in ("clean", "noisy")),
        "latency_failures": sum(not r[k]["latency_ok"] for r in rows for k in ("clean", "noisy")),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", type=Path, nargs=2, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--details", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists() or args.details.exists():
        parser.error("Refusing to overwrite evidence")
    rows = [r for path in args.inputs for r in read(path)]
    baseline_rows = [r for lang in ("th", "en") for r in read(ROOT / f"reports/typo_r16_20260930/paired_{lang}_r18.jsonl")]
    old = {r["id"]: r for r in baseline_rows}
    if len(rows) != 2000 or len({r["id"] for r in rows}) != 2000 or {r["id"] for r in rows} != set(old):
        parser.error("Requires the complete matching frozen 2,000-pair run")
    overlays = {r["id"]: r for r in read(ROOT / "data/eval/typo_r16_contract_overlay_20260930.jsonl")}
    scorer_baseline = [rescore_pair(r, overlays.get(r["id"])) for r in baseline_rows]
    scorer_new = [rescore_pair(r, overlays.get(r["id"])) for r in rows]
    affected_r19 = {r["id"]: r for r in read(ROOT / "reports/target_integrity_step1_20260930/paired_affected_domains_final.jsonl")}
    result = {
        "legacy_r18": summary(baseline_rows), "legacy_candidate": summary(rows),
        "by_locale": {lang: summary([r for r in rows if r["locale"] == lang]) for lang in ("th", "en")},
        "legacy_deltas": {},
        "same_v2_scorer": {
            "r18_clean": sum(r["v2"]["clean"]["passed"] for r in scorer_baseline),
            "r18_noisy": sum(r["v2"]["noisy"]["passed"] for r in scorer_baseline),
            "candidate_clean": sum(r["v2"]["clean"]["passed"] for r in scorer_new),
            "candidate_noisy": sum(r["v2"]["noisy"]["passed"] for r in scorer_new),
            "candidate_regressions": sum(r["v2"]["regression"] for r in scorer_new),
            "positive_contract_count": sum(r["v2"]["clean"]["positive_contract_present"] for r in scorer_new),
            "noisy_evidence_levels": dict(Counter(r["v2"]["noisy"]["evidence_level"] for r in scorer_new)),
        },
        "remaining_regression_domains": dict(Counter(r["domain"] for r in rows if r["regression"])),
        "remaining_regression_modes": dict(Counter(r["noisy"]["mode"] for r in rows if r["regression"])),
        "remaining_review_status": dict(Counter(r["review_status"] for r in rows if r["regression"])),
        "truth_level": "candidate GT; deterministic only; no real WordPress booking oracle or owner approval",
        "r19_affected_domains": {},
    }
    for kind in ("clean", "noisy"):
        result["legacy_deltas"][kind] = {
            "improved_ids": [r["id"] for r in rows if not old[r["id"]][kind]["passed"] and r[kind]["passed"]],
            "worsened_ids": [r["id"] for r in rows if old[r["id"]][kind]["passed"] and not r[kind]["passed"]],
        }
        subset = [r for r in rows if r["id"] in affected_r19]
        result["r19_affected_domains"][kind] = {
            "count": len(subset), "old_pass": sum(affected_r19[r["id"]][kind]["passed"] for r in subset),
            "new_pass": sum(r[kind]["passed"] for r in subset),
            "worsened_ids": [r["id"] for r in subset if affected_r19[r["id"]][kind]["passed"] and not r[kind]["passed"]],
        }
    with args.details.open("x", encoding="utf-8") as stream:
        for row, v2 in zip(rows, scorer_new):
            if row["noisy"]["passed"] and row["clean"]["passed"]:
                continue
            gates = [key for key in ("route_ok", "status_ok", "content_ok", "latency_ok") if not row["noisy"][key]]
            stream.write(json.dumps({
                **row, "v2_score": v2["v2"], "failed_gates": gates,
                "first_failed_gate": gates[0] if gates else "clean_only_failure",
                "root_cause_review": "gate is an observed symptom; inspect trace/source before assigning a single cause",
                "owner_confirmed": False,
            }, ensure_ascii=False) + "\n")
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
