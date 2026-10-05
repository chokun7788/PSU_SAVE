from __future__ import annotations

import argparse
import csv
import json
import statistics
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.runtime.pipeline_answer import answer_question_pipeline_debug  # noqa: E402


DEFAULT_CASES = [
    "PS5 ราคาเท่าไหร่",
    "PC ราคาเท่าไหร่",
    "นักศึกษาเล่น VR 30 นาทีเท่าไหร่",
    "Tekken 8 ราคาเท่าไหร่",
    "PS5 มีเกมอะไรกับราคาเท่าไหร่",
    "Tekken 8 ปุ่มอะไร แล้ว PC ราคาเท่าไหร่",
    "Naruto เล่นยังไง",
]

REPORT_DIR = ROOT / "reports" / "latency_profile"


def _timing_by_stage(result: Any) -> dict[str, float]:
    stages: dict[str, float] = defaultdict(float)
    for item in result.trace:
        if getattr(item, "stage", "") != "timing":
            continue
        stages[str(item.decision)] += float(item.metadata.get("elapsed_ms") or 0.0)
    return dict(stages)


def _percentile(values: list[float], pct: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = min(len(ordered) - 1, max(0, round((len(ordered) - 1) * pct)))
    return ordered[index]


def _load_questions(path: Path | None) -> list[str]:
    if path is None:
        return DEFAULT_CASES
    questions: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        text = line.strip()
        if text:
            questions.append(text)
    return questions


def profile_question(question: str, *, repeats: int, allow_llm: bool) -> dict[str, Any]:
    runs: list[dict[str, Any]] = []
    for index in range(repeats):
        result = answer_question_pipeline_debug(question, experimental_allow_llm=allow_llm)
        stages = _timing_by_stage(result)
        slowest = sorted(stages.items(), key=lambda item: item[1], reverse=True)[:8]
        runs.append({
            "index": index,
            "elapsed_ms": round(result.elapsed * 1000, 2),
            "mode": result.mode,
            "route_category": result.route.category,
            "route_intent": result.route.intent,
            "validation_ok": result.validation.ok,
            "stage_ms": stages,
            "slowest_stages": slowest,
        })
    warm_elapsed = [run["elapsed_ms"] for run in runs[1:]] or [run["elapsed_ms"] for run in runs]
    return {
        "question": question,
        "runs": runs,
        "cold_ms": runs[0]["elapsed_ms"] if runs else 0.0,
        "warm_avg_ms": round(statistics.mean(warm_elapsed), 2),
        "warm_median_ms": round(statistics.median(warm_elapsed), 2),
        "warm_p95_ms": round(_percentile(warm_elapsed, 0.95), 2),
        "mode": runs[-1]["mode"] if runs else "",
        "route": f"{runs[-1]['route_category']}/{runs[-1]['route_intent']}" if runs else "",
        "validation_ok": all(run["validation_ok"] for run in runs),
        "top_warm_stage": max(
            (
                (sum(run["stage_ms"].get(stage, 0.0) for run in runs[1:]), stage)
                for stage in {key for run in runs[1:] for key in run["stage_ms"]}
            ),
            default=(0.0, ""),
        )[1],
    }


def _write_reports(rows: list[dict[str, Any]]) -> tuple[Path, Path]:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_path = REPORT_DIR / f"pipeline_latency_profile_{stamp}.json"
    csv_path = REPORT_DIR / f"pipeline_latency_profile_{stamp}.csv"
    json_path.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    with csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "question",
                "mode",
                "route",
                "cold_ms",
                "warm_avg_ms",
                "warm_median_ms",
                "warm_p95_ms",
                "top_warm_stage",
                "validation_ok",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in writer.fieldnames or []})
    return json_path, csv_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Profile PSU Esports chatbot pipeline latency by question and trace stage.")
    parser.add_argument("--questions", type=Path, default=None, help="UTF-8 text file, one question per line")
    parser.add_argument("--repeats", type=int, default=6)
    parser.add_argument("--allow-llm", action="store_true")
    parser.add_argument("--fail-warm-ms", type=float, default=0.0, help="fail when any warm median exceeds this value")
    args = parser.parse_args()

    rows = [profile_question(question, repeats=max(1, args.repeats), allow_llm=args.allow_llm) for question in _load_questions(args.questions)]
    for row in rows:
        print(
            f"{row['warm_median_ms']:8.2f} ms warm | {row['cold_ms']:8.2f} ms cold | "
            f"{row['mode']} | {row['question']} | slow={row['top_warm_stage']}"
        )

    json_path, csv_path = _write_reports(rows)
    print(f"JSON: {json_path}")
    print(f"CSV: {csv_path}")

    if args.fail_warm_ms > 0:
        failed = [row for row in rows if float(row["warm_median_ms"]) > args.fail_warm_ms or not row["validation_ok"]]
        if failed:
            print("LATENCY PROFILE FAILED")
            for row in failed:
                print(f"- {row['question']}: warm_median={row['warm_median_ms']} validation_ok={row['validation_ok']}")
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
