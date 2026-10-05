"""Capture comparable decision traces for representative r15 typo failures."""

from __future__ import annotations

import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.pipeline.engine import answer_question_pipeline_debug  # noqa: E402
from app.pipeline.preprocess import extract_entities, preprocess_input  # noqa: E402
from app.pipeline.router import route_intent  # noqa: E402

REPORT_DIR = ROOT / "reports/bilingual_typo_2000_20260929"
OUTPUT = REPORT_DIR / "forensic_trace_selected_20260930_r15.jsonl"
IDS = (
    "MASTER-GT-TH-00890", "MASTER-GT-TH-00085", "MASTER-GT-TH-04867",
    "MASTER-GT-EN-03895", "MASTER-GT-EN-02806", "MASTER-GT-EN-02255",
    "MASTER-GT-EN-04469",
)


def main() -> int:
    if OUTPUT.exists():
        raise SystemExit(f"Refusing to overwrite: {OUTPUT}")
    rows = {}
    for locale in ("th", "en"):
        for line in (REPORT_DIR / f"paired_{locale}_r15.jsonl").read_text(encoding="utf-8").splitlines():
            row = json.loads(line)
            if row["id"] in IDS:
                rows[row["id"]] = row
    if set(rows) != set(IDS):
        raise SystemExit(f"Selected IDs missing: {set(IDS) - set(rows)}")

    with OUTPUT.open("x", encoding="utf-8") as stream:
        for case_id in IDS:
            case = rows[case_id]
            for variant in ("clean", "noisy"):
                question = case[f"{variant}_question"]
                pre = preprocess_input(question)
                entities = extract_entities(pre)
                initial_route, initial_route_trace = route_intent(pre, entities)
                result = answer_question_pipeline_debug(
                    question, locale=case["locale"], experimental_allow_llm=False,
                    experimental_rag_fallback=False, global_timeout_sec=20.0,
                )
                output = {
                    "id": case_id, "variant": variant, "locale": case["locale"],
                    "question": question, "preprocessed": asdict(pre),
                    "entities": asdict(entities),
                    "initial_route": asdict(initial_route),
                    "initial_route_trace": asdict(initial_route_trace),
                    "final_route": asdict(result.route), "mode": result.mode,
                    "answer": result.answer, "elapsed_sec": result.elapsed,
                    "answer_confidence": result.confidence,
                    "trace": [asdict(item) for item in result.trace],
                }
                stream.write(json.dumps(output, ensure_ascii=False, default=str) + "\n")
                stream.flush()
                print(case_id, variant, result.route.category, result.mode, flush=True)
    print(OUTPUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
