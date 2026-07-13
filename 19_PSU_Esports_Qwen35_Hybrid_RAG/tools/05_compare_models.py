from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

from app.rag.hybrid_engine import HybridRagEngine

REPORT_DIR = PROJECT_ROOT / "reports"


DEFAULT_QUESTIONS = [
    "CS2 แข่งทีมละกี่คน",
    "สรุปกฎ RoV เรื่อง pause และมาสายให้หน่อย",
    "ต่างมหาลัยเล่น VR 30 นาทีเท่าไหร่",
    "วันไหนหยุดบ้างในเดือนนี้",
    "ทำเมาส์พังต้องเสียค่าปรับไหม",
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--models", nargs="+", default=["qwen2.5:3b", "qwen3:4b", "qwen3.5:4b"])
    parser.add_argument("--timeout-sec", type=float, default=10.0)
    parser.add_argument("--output", default="model_compare_results.jsonl")
    args = parser.parse_args()

    engine = HybridRagEngine()
    rows = []
    for question in DEFAULT_QUESTIONS:
        for model in args.models:
            result = engine.answer(question, model=model, timeout_sec=args.timeout_sec, top_k=5)
            rows.append(
                {
                    "question": question,
                    "model": model,
                    "mode": result.get("mode"),
                    "elapsed_sec": result.get("elapsed_sec"),
                    "answer": result.get("answer"),
                    "top_hit": result.get("hits", [{}])[0].get("id") if result.get("hits") else None,
                    "error": result.get("error", ""),
                }
            )
            print(f"{model} | {question} | {result.get('mode')} | {result.get('elapsed_sec')}s")

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = REPORT_DIR / args.output
    output_path.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
