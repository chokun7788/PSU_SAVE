#!/usr/bin/env python3
"""Compare completed r8 master evaluation chunks with the 27 Sep snapshot."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding="utf-8")


def component_key(row: dict) -> str:
    if row.get("evaluation_error"):
        return "evaluation_error"
    parts = []
    for field, label in (
        ("route_ok", "route"), ("status_ok", "status"),
        ("content_ok", "content"), ("latency_ok", "latency"),
    ):
        if row.get(field) is False:
            parts.append(label)
    return "+".join(parts) or "unknown"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-root", type=Path, required=True)
    parser.add_argument("--old-root", type=Path, required=True)
    args = parser.parse_args()
    run_root = args.run_root.resolve()
    old_root = args.old_root.resolve()
    chunk_names = ["chunk_0000", "chunk_2500", "chunk_5000", "chunk_7500"]
    old_names = [
        "master_v2_current.jsonl", "master_v2_2500_5000.jsonl",
        "master_v2_5000_7500.jsonl", "master_v2_7500_10000.jsonl",
    ]
    for name in chunk_names:
        if not (run_root / name / "summary.json").exists():
            raise SystemExit(f"Incomplete chunk: {name}")
    manifests = [json.loads((run_root / name / "manifest.json").read_text(encoding="utf-8")) for name in chunk_names]
    for key in ("corpus_sha256", "engine_sha256", "english_sha256", "router_sha256", "runtime_version"):
        if len({manifest[key] for manifest in manifests}) != 1:
            raise SystemExit(f"Chunk manifests disagree on {key}")
    current = [row for name in chunk_names for row in read_jsonl(run_root / name / "results.jsonl")]
    old = [row for name in old_names for row in read_jsonl(old_root / name)]
    current_by_id = {str(row["id"]): row for row in current}
    old_by_id = {str(row["id"]): row for row in old}
    if len(current) != 10000 or len(current_by_id) != 10000 or set(current_by_id) != set(old_by_id):
        raise SystemExit("Expected exactly 10,000 unique case IDs matching the baseline")

    by_locale: dict[str, dict] = {}
    by_domain: dict[str, dict] = {}
    for field, target in (("locale", by_locale), ("domain", by_domain)):
        for key in sorted({str(row[field]) for row in current}):
            rows = [row for row in current if str(row[field]) == key]
            failed = [row for row in rows if not row.get("passed")]
            target[key] = {
                "total": len(rows), "passed": len(rows) - len(failed), "failed": len(failed),
                "failure_components": dict(Counter(component_key(row) for row in failed)),
                "actual_status": dict(Counter(str(row.get("actual_status")) for row in rows)),
                "passed_pending": sum(row.get("passed") and row.get("actual_status") == "localization_pending" for row in rows),
                "passed_no_answer": sum(row.get("passed") and row.get("actual_status") == "no_answer" for row in rows),
            }

    newly_passed = [row for row in current if row["passed"] and not old_by_id[row["id"]]["passed"]]
    regressed = [row for row in current if not row["passed"] and old_by_id[row["id"]]["passed"]]
    transition_rows = []
    for kind, cases in (("newly_passed", newly_passed), ("regressed", regressed)):
        for row in cases:
            before = old_by_id[row["id"]]
            transition_rows.append({
                "kind": kind, "id": row["id"], "locale": row["locale"],
                "domain": row["domain"], "question": row["question"],
                "old_route": before.get("actual_route"), "new_route": row.get("actual_route"),
                "old_status": before.get("actual_status"), "new_status": row.get("actual_status"),
                "old_failures": before.get("failures"), "new_failures": row.get("failures"),
                "old_answer": before.get("answer"), "new_answer": row.get("answer"),
            })
    analysis = {
        "current_total": len(current),
        "current_passed": sum(bool(row.get("passed")) for row in current),
        "current_failed": sum(not row.get("passed") for row in current),
        "old_passed": sum(bool(row.get("passed")) for row in old),
        "newly_passed": len(newly_passed), "regressed": len(regressed),
        "answer_changed": sum(row.get("answer") != old_by_id[row["id"]].get("answer") for row in current),
        "route_changed": sum(row.get("actual_route") != old_by_id[row["id"]].get("actual_route") for row in current),
        "status_changed": sum(row.get("actual_status") != old_by_id[row["id"]].get("actual_status") for row in current),
        "evaluation_errors": sum(bool(row.get("evaluation_error")) for row in current),
        "by_locale": by_locale, "by_domain": by_domain,
        "manifest": manifests[0],
        "interpretation_limits": [
            "Automated contracts include generated or inherited candidate gold; pass does not mean a human verified every answer.",
            "This run disables the local LLM and RAG fallback for deterministic comparison; the owner launcher enables local LLM assistance.",
            "Localization-pending and no-answer can pass status contracts without supplying the requested fact.",
            "Booking cases cannot certify real per-resource vacancy without an independent WordPress oracle.",
        ],
    }
    analysis_dir = run_root / "analysis"
    analysis_dir.mkdir(exist_ok=False)
    write_json(analysis_dir / "summary.json", analysis)
    with (analysis_dir / "pass_transitions.jsonl").open("x", encoding="utf-8") as handle:
        for row in transition_rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(json.dumps({key: analysis[key] for key in ("current_total", "current_passed", "current_failed", "old_passed", "newly_passed", "regressed", "evaluation_errors")}, ensure_ascii=False))
    print(f"Analysis: {analysis_dir}")


if __name__ == "__main__":
    main()
