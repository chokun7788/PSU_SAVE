from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    sys.path.insert(0, str(ROOT))
    from app.pipeline.vector_retrieval import VECTOR_INDEX_PATH, write_vector_index

    payload = write_vector_index(VECTOR_INDEX_PATH)
    print("VECTOR INDEX OK")
    print(f"- path: {VECTOR_INDEX_PATH}")
    print(f"- backend: {payload.get('backend')}")
    print(f"- docs: {payload.get('doc_count')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
