from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.knowledge.canonical_content import CONTENT_ROOT, load_records, validate_records


def main() -> int:
    records = load_records()
    validation = validate_records(records)
    assert validation.ok, "\n".join(validation.errors)
    manifest = json.loads((CONTENT_ROOT / "manifest.json").read_text(encoding="utf-8"))
    assert manifest["record_count"] == len(records)
    assert len({record["content_id"] for record in records}) == len(records)
    assert all(record["locales"]["en"]["status"] != "approved" for record in records)
    projection = CONTENT_ROOT / "projections" / "manifest.json"
    projection_manifest = json.loads(projection.read_text(encoding="utf-8"))
    assert projection_manifest["structured_records"] == len(records)
    assert projection_manifest["rag_th_records"] >= len(records)
    assert projection_manifest["rag_en_approved_records"] == 0
    print(f"OK canonical content records={len(records)} english_approved=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
