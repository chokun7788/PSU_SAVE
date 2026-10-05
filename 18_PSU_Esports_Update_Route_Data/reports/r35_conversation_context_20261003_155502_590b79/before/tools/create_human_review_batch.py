from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT.parents[0]
DEFAULT_EVAL = BASE / "16_PSU_Esports_RAG_Experiment_Timeline" / "ground_truth_eval_results_v2_alias_fuzzy_20260701.jsonl"


def read_jsonl(path: Path) -> list[dict]:
    rows = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--eval-path", default=str(DEFAULT_EVAL))
    parser.add_argument("--limit", type=int, default=120)
    parser.add_argument("--output", default=str(ROOT / "data" / "human_review" / "human_review_from_eval_sample.jsonl"))
    args = parser.parse_args()

    eval_path = Path(args.eval_path)
    rows = read_jsonl(eval_path)
    if not rows:
        print(f"No eval rows found: {eval_path}")
        return 1

    review_rows = []
    for idx, row in enumerate(rows[: args.limit], 1):
        question = row.get("question") or row.get("query") or row.get("input") or ""
        ai_answer = row.get("answer") or row.get("ai_answer") or row.get("actual") or ""
        expected = (
            row.get("expected")
            or row.get("expected_answer")
            or row.get("criteria")
            or row.get("required_keywords")
            or row.get("expected_keywords")
            or ""
        )
        if isinstance(expected, list):
            expected = "ต้องมีคำสำคัญ: " + ", ".join(str(item) for item in expected)
        route = row.get("mode") or row.get("route") or row.get("used_route") or ""
        auto_result = row.get("result") or row.get("status") or row.get("passed") or ""
        review_rows.append({
            "review_id": f"review_{idx:04d}",
            "created_at": datetime.now().isoformat(timespec="seconds"),
            "source_eval_file": str(eval_path),
            "question_id": row.get("id") or row.get("question_id") or f"row_{idx}",
            "question": question,
            "ai_answer": ai_answer,
            "expected_answer": expected,
            "route": route,
            "auto_result": auto_result,
            "human_decision": "",
            "correctness_score": None,
            "grounding_score": None,
            "completeness_score": None,
            "tone_score": None,
            "route_score": None,
            "actionability_score": None,
            "error_tags": [],
            "reviewer_notes": "",
            "fix_suggestion": "",
        })

    out_path = Path(args.output)
    write_jsonl(out_path, review_rows)
    print(f"Wrote {len(review_rows)} review rows: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
