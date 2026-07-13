from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.rag.ollama_client import ollama_embed
from app.rag.text import compact_text

CORPUS_PATH = PROJECT_ROOT / "data" / "unified" / "unified_knowledge.jsonl"
OUTPUT_PATH = PROJECT_ROOT / "data" / "index" / "vector_index_ollama.json"


def read_jsonl(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def vector_text(row: dict) -> str:
    return compact_text(
        "\n".join(
            str(row.get(key, ""))
            for key in ("title", "search_text", "text", "answer", "evidence")
            if row.get(key)
        ),
        1600,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="qwen3-embedding:0.6b")
    parser.add_argument("--batch-size", type=int, default=8)
    parser.add_argument("--timeout-sec", type=float, default=60.0)
    args = parser.parse_args()

    rows = read_jsonl(CORPUS_PATH)
    vectors = []
    for start in range(0, len(rows), args.batch_size):
        batch = rows[start : start + args.batch_size]
        texts = [vector_text(row) for row in batch]
        embeddings = ollama_embed(texts, model=args.model, timeout_sec=args.timeout_sec)
        for row, embedding in zip(batch, embeddings):
            vectors.append(
                {
                    "id": row["id"],
                    "embedding": embedding,
                }
            )
        print(f"embedded {min(start + args.batch_size, len(rows))}/{len(rows)}")

    output = {
        "meta": {
            "model": args.model,
            "corpus_path": str(CORPUS_PATH),
            "total_vectors": len(vectors),
            "dimension": len(vectors[0]["embedding"]) if vectors else 0,
        },
        "vectors": vectors,
    }
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(output, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote vector index -> {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
