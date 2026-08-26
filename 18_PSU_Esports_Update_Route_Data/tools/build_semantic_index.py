from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.pipeline.semantic_vector_retrieval import SEMANTIC_INDEX_PATH, build_semantic_index


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the Ollama semantic index for guarded RAG.")
    parser.add_argument("--output", type=Path, default=SEMANTIC_INDEX_PATH)
    parser.add_argument("--batch-size", type=int, default=0)
    parser.add_argument("--timeout-sec", type=float, default=0.0)
    args = parser.parse_args()

    result = build_semantic_index(
        path=args.output,
        batch_size=args.batch_size or None,
        timeout_sec=args.timeout_sec or None,
    )
    print(json.dumps(result.as_dict(), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
