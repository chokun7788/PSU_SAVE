from __future__ import annotations

import json
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[2]
RULE_DIR = PROJECT_DIR / "data" / "rules"


def read_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    if not path.exists():
        return rows
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"Invalid JSONL {path}:{line_no}: {exc}") from exc
    return rows


def load_rule_files(rule_dir: Path = RULE_DIR) -> list[dict]:
    rules: list[dict] = []
    for path in sorted(rule_dir.glob("*.jsonl")):
        for row in read_jsonl(path):
            row.setdefault("_rule_file", path.name)
            rules.append(row)
    return sorted(rules, key=lambda r: int(r.get("priority", 0)), reverse=True)
