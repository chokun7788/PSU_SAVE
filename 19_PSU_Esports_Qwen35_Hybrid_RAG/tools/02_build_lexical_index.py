from __future__ import annotations

import json
import math
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.rag.text import token_counts

CORPUS_PATH = PROJECT_ROOT / "data" / "unified" / "unified_knowledge.jsonl"
OUTPUT_PATH = PROJECT_ROOT / "data" / "index" / "lexical_index.json"


def read_jsonl(path: Path) -> list[dict]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def main() -> None:
    rows = read_jsonl(CORPUS_PATH)
    documents = []
    document_frequency: dict[str, int] = {}

    for row in rows:
        text = "\n".join(
            str(row.get(key, ""))
            for key in ("title", "search_text", "text", "answer", "evidence")
            if row.get(key)
        )
        counts = token_counts(text)
        documents.append({"id": row["id"], "tokens": counts})
        for token in counts:
            document_frequency[token] = document_frequency.get(token, 0) + 1

    total = max(1, len(documents))
    idf = {
        token: round(math.log((1 + total) / (1 + df)) + 1.0, 6)
        for token, df in document_frequency.items()
    }
    output = {
        "meta": {
            "corpus_path": str(CORPUS_PATH),
            "total_documents": total,
            "vocabulary_size": len(idf),
            "index_type": "tf_idf_cosine_lightweight",
        },
        "idf": idf,
        "documents": documents,
    }
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(json.dumps(output, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote lexical index -> {OUTPUT_PATH}")
    print(f"documents={total} vocabulary={len(idf)}")


if __name__ == "__main__":
    main()
