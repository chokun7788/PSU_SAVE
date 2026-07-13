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
from app.rag.ollama_client import ollama_embed

VECTOR_INDEX_PATH = PROJECT_ROOT / "data" / "index" / "vector_index_ollama.json"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("question", nargs="?", default="")
    parser.add_argument("--model", default="qwen3.5:4b")
    parser.add_argument("--embedding-model", default="qwen3-embedding:0.6b")
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--timeout-sec", type=float, default=10.0)
    parser.add_argument("--no-llm", action="store_true")
    parser.add_argument("--use-vector", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    question = args.question.strip() or input("พิมพ์คำถาม: ").strip()
    query_embedding = None
    if args.use_vector:
        if not VECTOR_INDEX_PATH.exists():
            print("ยังไม่มี vector index ให้รัน tools\\03_build_vector_index_ollama.py ก่อน หรือเอา --use-vector ออก")
        else:
            query_embedding = ollama_embed([question], model=args.embedding_model, timeout_sec=args.timeout_sec)[0]

    engine = HybridRagEngine()
    result = engine.answer(
        question,
        model=args.model,
        top_k=args.top_k,
        query_embedding=query_embedding,
        use_llm=not args.no_llm,
        timeout_sec=args.timeout_sec,
    )

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    print("=" * 92)
    print(f"คำถาม: {result['question']}")
    print(f"mode: {result['mode']} | model: {result.get('model') or '-'} | elapsed: {result['elapsed_sec']} sec")
    if result.get("error"):
        print(f"error: {result['error']}")
    print("-" * 92)
    print(result["answer"])
    print("-" * 92)
    print("Top hits:")
    for hit in result.get("hits", []):
        print(f"- {hit['id']} | score={hit['score']} | lexical={hit['lexical_score']} | vector={hit['vector_score']}")
        print(f"  {hit['category']} / {hit['source_kind']} / {hit['source_url']}")
        print(f"  {hit['text_preview']}")


if __name__ == "__main__":
    main()
