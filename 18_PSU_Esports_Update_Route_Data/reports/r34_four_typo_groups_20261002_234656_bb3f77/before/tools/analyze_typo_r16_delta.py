"""Compare paired deterministic runs without rewriting either run."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def compare(old_rows: list[dict], new_rows: list[dict]) -> dict:
    old = {row["id"]: row for row in old_rows}
    new = {row["id"]: row for row in new_rows}
    if old.keys() != new.keys():
        raise ValueError("paired runs contain different case IDs")
    fixed = []
    new_regressions = []
    clean_worsened = []
    noisy_worsened = []
    route_fixed = []
    summary_by_locale = {}
    for locale in ("th", "en"):
        current = [row for row in new.values() if row["locale"] == locale]
        baseline = [old[row["id"]] for row in current]
        summary_by_locale[locale] = {
            "count": len(current),
            "old_clean_pass": sum(row["clean"]["passed"] for row in baseline),
            "new_clean_pass": sum(row["clean"]["passed"] for row in current),
            "old_noisy_pass": sum(row["noisy"]["passed"] for row in baseline),
            "new_noisy_pass": sum(row["noisy"]["passed"] for row in current),
            "old_regressions": sum(row["regression"] for row in baseline),
            "new_regressions": sum(row["regression"] for row in current),
        }
    for case_id in sorted(new):
        before, after = old[case_id], new[case_id]
        if before["regression"] and after["clean"]["passed"] and after["noisy"]["passed"]:
            fixed.append(case_id)
        if not before["regression"] and after["regression"]:
            new_regressions.append(case_id)
        if before["clean"]["passed"] and not after["clean"]["passed"]:
            clean_worsened.append(case_id)
        if before["noisy"]["passed"] and not after["noisy"]["passed"]:
            noisy_worsened.append(case_id)
        if not before["noisy"]["route_ok"] and after["noisy"]["route_ok"]:
            route_fixed.append(case_id)
    return {
        "summary_by_locale": summary_by_locale,
        "fixed_regressions": fixed,
        "new_regressions": new_regressions,
        "clean_worsened": clean_worsened,
        "noisy_worsened": noisy_worsened,
        "noisy_route_fixed": route_fixed,
        "fixed_by_domain": dict(Counter(new[case_id]["domain"] for case_id in fixed)),
        "new_regressions_by_domain": dict(Counter(new[case_id]["domain"] for case_id in new_regressions)),
        "interpretation": "Automated candidate GT only; changes require case-level review.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--old-th", type=Path, required=True)
    parser.add_argument("--old-en", type=Path, required=True)
    parser.add_argument("--new-th", type=Path, required=True)
    parser.add_argument("--new-en", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error(f"output exists: {args.output}")
    report = compare(
        read_jsonl(args.old_th) + read_jsonl(args.old_en),
        read_jsonl(args.new_th) + read_jsonl(args.new_en),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(report, stream, ensure_ascii=False, indent=2)
    print(json.dumps({
        "summary_by_locale": report["summary_by_locale"],
        "fixed_regressions": len(report["fixed_regressions"]),
        "new_regressions": len(report["new_regressions"]),
        "clean_worsened": len(report["clean_worsened"]),
        "noisy_worsened": len(report["noisy_worsened"]),
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
