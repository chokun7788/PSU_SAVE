"""Audit benchmark failure dimensions without changing the original results."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "reports/bilingual_typo_2000_20260929"
OUTPUT = BASE / "failure_taxonomy_20260930.json"


def read(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def primary_failure(result: dict) -> str:
    for name, key in (("route", "route_ok"), ("status", "status_ok"),
                      ("content", "content_ok"), ("latency", "latency_ok")):
        if not result[key]:
            return name
    return "pass"


def no_positive_contract(row: dict) -> bool:
    contract = row["answer_contract"]
    return not contract.get("must_contain") and not contract.get("must_contain_any")


def summary(rows: list[dict]) -> dict:
    regressions = [row for row in rows if row["regression"]]
    baseline_failures = [row for row in rows if not row["clean"]["passed"]]
    route_only = [row for row in regressions if not row["noisy"]["route_ok"]
                  and row["noisy"]["status_ok"] and row["noisy"]["content_ok"]
                  and row["noisy"]["latency_ok"]]
    return {
        "rows": len(rows), "regressions": len(regressions),
        "regression_primary_failure": dict(Counter(primary_failure(row["noisy"]) for row in regressions)),
        "clean_failure_primary": dict(Counter(primary_failure(row["clean"]) for row in baseline_failures)),
        "no_positive_content_contract": sum(no_positive_contract(row) for row in rows),
        "regressions_with_no_positive_content_contract": sum(no_positive_contract(row) for row in regressions),
        "route_only_regression_count": len(route_only),
        "route_only_safe_no_answer_ids": [row["id"] for row in route_only
            if row["expected_answer_status"] in {"no_answer_expected", "safe_no_answer"}
            and row["noisy"]["actual_status"] == "no_answer"],
        "noisy_ambiguous_game_mode_scored_as_answer_ids": [row["id"] for row in rows
            if row["noisy"]["mode"] == "pipeline:game_target_ambiguous"
            and row["noisy"]["actual_status"] == "answer"],
        "baseline_failure_by_domain": dict(Counter(row["domain"] for row in baseline_failures)),
        "regression_by_domain": dict(Counter(row["domain"] for row in regressions)),
        "regression_by_edit_recipe": dict(Counter(row["edit_recipe"] for row in regressions)),
        "regression_route_transitions": [
            {"from": source, "to": target, "count": count}
            for (source, target), count in Counter(
                (row["clean"]["actual_route"], row["noisy"]["actual_route"])
                for row in regressions
            ).most_common(15)
        ],
        "review_status": dict(Counter(row["review_status"] for row in rows)),
    }


def main() -> int:
    if OUTPUT.exists():
        raise SystemExit(f"Refusing to overwrite: {OUTPUT}")
    by_locale = {locale: read(BASE / f"paired_{locale}_r15.jsonl") for locale in ("th", "en")}
    if any(len(rows) != 1000 for rows in by_locale.values()):
        raise SystemExit("Expected 1,000 completed cases per language")
    result = {"overall": summary(by_locale["th"] + by_locale["en"]),
              "by_locale": {locale: summary(rows) for locale, rows in by_locale.items()}}
    OUTPUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"output": str(OUTPUT), "overall": result["overall"]["regression_primary_failure"],
                      "th": result["by_locale"]["th"]["regression_primary_failure"],
                      "en": result["by_locale"]["en"]["regression_primary_failure"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
