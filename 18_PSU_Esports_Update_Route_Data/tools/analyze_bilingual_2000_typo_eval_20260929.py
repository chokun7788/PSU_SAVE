"""Summarize paired typo results without treating unreviewed labels as verified truth."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "reports/bilingual_typo_2000_20260929"


def load(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def rates(rows: list[dict]) -> dict:
    total = len(rows)
    return {
        "total": total,
        "clean_pass": sum(row["clean"]["passed"] for row in rows),
        "noisy_pass": sum(row["noisy"]["passed"] for row in rows),
        "clean_pass_pct": round(100 * sum(row["clean"]["passed"] for row in rows) / total, 2) if total else None,
        "noisy_pass_pct": round(100 * sum(row["noisy"]["passed"] for row in rows) / total, 2) if total else None,
        "regressions": sum(row["regression"] for row in rows),
        "recoveries": sum(row["recovery"] for row in rows),
        "both_fail": sum(not row["clean"]["passed"] and not row["noisy"]["passed"] for row in rows),
        "both_pass": sum(row["clean"]["passed"] and row["noisy"]["passed"] for row in rows),
        "route_changed": sum(row["route_changed"] for row in rows),
        "status_changed": sum(row["status_changed"] for row in rows),
        "noisy_route_fail": sum(not row["noisy"]["route_ok"] for row in rows),
        "noisy_status_fail": sum(not row["noisy"]["status_ok"] for row in rows),
        "noisy_content_fail": sum(not row["noisy"]["content_ok"] for row in rows),
        "noisy_latency_fail": sum(not row["noisy"]["latency_ok"] for row in rows),
    }


def grouped(rows: list[dict], key: str) -> dict:
    groups = defaultdict(list)
    for row in rows:
        groups[str(row[key])].append(row)
    return {group: rates(values) for group, values in sorted(groups.items())}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--th", type=Path, default=REPORT_DIR / "paired_th_r15.jsonl")
    parser.add_argument("--en", type=Path, default=REPORT_DIR / "paired_en_r15.jsonl")
    parser.add_argument("--output", type=Path, default=REPORT_DIR / "analysis_r15.json")
    args = parser.parse_args()
    if args.output.exists():
        parser.error(f"Output already exists: {args.output}")
    rows = load(args.th) + load(args.en)
    if len(rows) != 2000 or Counter(row["locale"] for row in rows) != {"th": 1000, "en": 1000}:
        parser.error("Expected exactly 1,000 Thai and 1,000 English completed cases")
    result = {
        "sources": [str(args.th), str(args.en)],
        "overall": rates(rows),
        "by_locale": grouped(rows, "locale"),
        "by_recipe": grouped(rows, "edit_recipe"),
        "by_domain": grouped(rows, "domain"),
        "by_locale_and_recipe": {
            locale: grouped([row for row in rows if row["locale"] == locale], "edit_recipe")
            for locale in ("th", "en")
        },
        "by_locale_and_domain": {
            locale: grouped([row for row in rows if row["locale"] == locale], "domain")
            for locale in ("th", "en")
        },
        "review_status": dict(Counter(row["review_status"] for row in rows)),
        "regression_failure_dimensions": {
            locale: dict(Counter(
                dimension
                for row in rows if row["locale"] == locale and row["regression"]
                for dimension, key in (("route", "route_ok"), ("status", "status_ok"),
                                       ("content", "content_ok"), ("latency", "latency_ok"))
                if not row["noisy"][key]
            )) for locale in ("th", "en")
        },
        "deterministic_only": True,
        "ground_truth_is_candidate": True,
    }
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"output": str(args.output), "overall": result["overall"],
                      "by_locale": result["by_locale"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
