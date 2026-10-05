from __future__ import annotations

import argparse
import json
import statistics
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402


DEFAULT_FIXTURE = ROOT / "data" / "eval" / "thai_noisy_input_pairs_20260929.jsonl"


def _answer(question: str) -> dict:
    result = answer_question_pipeline_debug(
        question,
        experimental_allow_llm=False,
        experimental_rag_fallback=False,
    )
    chosen = question
    for item in result.trace:
        if item.stage == "preprocess" and item.decision == "selected_query_variant":
            chosen = str(item.detail)
    return {
        "intent": result.route.intent,
        "category": result.route.category,
        "mode": result.mode,
        "answer_preview": result.answer[:260].replace("\n", " "),
        "elapsed_sec": round(result.elapsed, 4),
        "selected_query": chosen,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        parser.error(f"Output already exists: {args.output}")

    cases = [json.loads(line) for line in args.fixture.read_text(encoding="utf-8").splitlines() if line.strip()]
    results: list[dict] = []
    for case in cases:
        clean = _answer(case["clean"])
        noisy = _answer(case["noisy"])
        expected = case["expected_intent"]
        protected = case.get("protected", [])
        row = {
            **case,
            "clean_result": clean,
            "noisy_result": noisy,
            "clean_intent_ok": clean["intent"] == expected,
            "noisy_intent_ok": noisy["intent"] == expected,
            "pair_intent_equal": clean["intent"] == noisy["intent"],
            "protected_preserved": all(value in noisy["selected_query"] for value in protected),
        }
        results.append(row)
        print(f"{case['id']} {int(row['clean_intent_ok'])}/{int(row['noisy_intent_ok'])} {clean['intent']} -> {noisy['intent']}", flush=True)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in results),
        encoding="utf-8",
    )
    durations = [row["noisy_result"]["elapsed_sec"] for row in results]
    summary = {
        "count": len(results),
        "clean_intent_ok": sum(row["clean_intent_ok"] for row in results),
        "noisy_intent_ok": sum(row["noisy_intent_ok"] for row in results),
        "pair_intent_equal": sum(row["pair_intent_equal"] for row in results),
        "protected_preserved": sum(row["protected_preserved"] for row in results),
        "noisy_errors_by_group": dict(Counter(row["group"] for row in results if not row["noisy_intent_ok"])),
        "noisy_p50_sec": round(statistics.median(durations), 4),
        "noisy_p95_sec": round(sorted(durations)[min(len(durations) - 1, int(len(durations) * 0.95))], 4),
        "output": str(args.output),
        "note": "Manually expected intents; no live booking occupied/free oracle; LLM disabled for deterministic diagnostic run.",
    }
    summary_path = args.output.with_suffix(".summary.json")
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
