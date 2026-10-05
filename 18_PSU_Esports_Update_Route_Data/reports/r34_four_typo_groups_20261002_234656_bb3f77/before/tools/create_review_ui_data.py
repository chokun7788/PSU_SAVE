from __future__ import annotations

import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCE_JSONL = ROOT / "data" / "human_review" / "human_review_pipeline_quality_round7_new_patterns_fix_full_360.jsonl"
OUTPUT_JS = ROOT / "review_ui" / "review_data.js"


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def main() -> int:
    rows = read_jsonl(SOURCE_JSONL)
    OUTPUT_JS.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(rows, ensure_ascii=False, indent=2)
    OUTPUT_JS.write_text(
        "window.REVIEW_ITEMS = " + payload + ";\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"Wrote {len(rows)} review items: {OUTPUT_JS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
