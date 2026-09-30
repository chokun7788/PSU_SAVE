#!/usr/bin/env python3
"""Summarize an intent-trap run without treating candidate passes as human QA."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CORPUS = ROOT / "data/eval/intent_trap_bilingual_1000_v1.jsonl"


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def analyze(corpus: Path, detail: Path) -> tuple[str, dict]:
    cases = {row["id"]: row for row in load_jsonl(corpus)}
    results = json.loads(detail.read_text(encoding="utf-8"))
    if len(cases) != len(results) or len({row["id"] for row in results}) != len(results):
        raise ValueError("Corpus/result IDs are incomplete or duplicated")
    if set(cases) != {row["id"] for row in results}:
        raise ValueError("Result IDs do not match corpus")
    grouped: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for result in results:
        grouped[(result["locale"], result["domain"])].append(result)
    lines = [
        "# Intent-trap bilingual evaluation",
        "",
        f"Corpus: `{corpus}`  ",
        f"Results: `{detail}`  ",
        "Status: scenario-curated paraphrases pending human review; a passing automated check is not proof of factual correctness.",
        "",
        "| Locale | Theme | Passed | Total | Route fails | Status fails | Content fails | >10s | >20s |",
        "|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    machine = {"total": len(results), "passed": sum(bool(row["passed"]) for row in results), "groups": {}}
    for (locale, theme), rows in sorted(grouped.items()):
        passed = sum(bool(row["passed"]) for row in rows)
        route_fails = sum(not row["route_ok"] for row in rows)
        status_fails = sum(not row["status_ok"] for row in rows)
        content_fails = sum(not row["content_ok"] for row in rows)
        over10 = sum(row["elapsed_sec"] > 10 for row in rows)
        over20 = sum(row["elapsed_sec"] > 20 for row in rows)
        key = f"{locale}/{theme}"
        machine["groups"][key] = {
            "passed": passed, "total": len(rows), "route_fails": route_fails,
            "status_fails": status_fails, "content_fails": content_fails,
            "over10": over10, "over20": over20,
            "failure_modes": dict(Counter(row["mode"] for row in rows if not row["passed"])),
        }
        lines.append(f"| {locale} | {theme} | {passed} | {len(rows)} | {route_fails} | {status_fails} | {content_fails} | {over10} | {over20} |")
    lines.extend(["", "## Representative failures", ""])
    for (locale, theme), rows in sorted(grouped.items()):
        failures = [row for row in rows if not row["passed"]]
        if not failures:
            continue
        lines.append(f"### {locale} / {theme}")
        lines.append("")
        seen_scenarios: set[str] = set()
        for row in failures:
            scenario = str(cases[row["id"]]["metadata"]["scenario_id"])
            if scenario in seen_scenarios:
                continue
            seen_scenarios.add(scenario)
            answer = " ".join(str(row["answer"]).split())[:260]
            lines.append(f"- `{row['id']}` ({row['elapsed_sec']:.2f}s, `{row['mode']}`): {row['question']}")
            lines.append(f"  - Failures: {'; '.join(row['failures'])}")
            lines.append(f"  - Answer excerpt: {answer}")
            if len(seen_scenarios) == 3:
                break
        lines.append("")
    lines.extend([
        "## Interpretation limits", "",
        "- Each locale has 100 distinct scenarios with five framing variants, not 500 independent intents.",
        "- The shared evaluator checks route, status, latency, and string contracts. It does not judge semantic correctness or source support.",
        "- `route_only` cases intentionally make no correctness claim beyond avoiding an obviously wrong route or forbidden catalog response; manually review their full answers.",
        "- Weekday live-slot dates are relative to the manifest reference date. Rebuild the corpus before rerunning on a later date.",
    ])
    return "\n".join(lines) + "\n", machine


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("detail", type=Path)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report, machine = analyze(args.corpus, args.detail)
    output = args.output or args.detail.with_name(args.detail.stem + "_analysis.md")
    output.write_text(report, encoding="utf-8")
    output.with_suffix(".json").write_text(json.dumps(machine, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{machine['passed']}/{machine['total']} automated checks passed; report {output}")


if __name__ == "__main__":
    main()
