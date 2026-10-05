from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_jsonl(path: Path) -> list[dict]:
    rows = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise AssertionError(f"Invalid JSONL {path}:{line_no}: {exc}") from exc
    return rows


def main() -> int:
    problems = []
    rule_count = 0
    for path in sorted((ROOT / "data" / "rules").glob("*.jsonl")):
        rows = read_jsonl(path)
        rule_count += len(rows)
        for row in rows:
            for key in ["id", "category", "intent", "patterns", "answer_th"]:
                if key not in row:
                    problems.append(f"{path.name}: missing {key} in {row.get('id')}")
            if not isinstance(row.get("patterns", []), list):
                problems.append(f"{path.name}: patterns must be list in {row.get('id')}")

    curated_count = 0
    for path in sorted((ROOT / "data" / "curated").glob("*.jsonl")):
        curated_count += len(read_jsonl(path))

    sys.path.insert(0, str(ROOT))
    from app.calculator.service_fee import answer_service_fee
    fee_case = answer_service_fee("ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่")
    if "190" not in fee_case.get("answer", ""):
        problems.append("service_fee calculator did not return 190 for external student VR 30min")

    if problems:
        print("VALIDATION FAILED")
        for problem in problems:
            print("-", problem)
        return 1

    print("VALIDATION OK")
    print(f"- rule files: {len(list((ROOT / 'data' / 'rules').glob('*.jsonl')))}")
    print(f"- rules: {rule_count}")
    print(f"- curated rows: {curated_count}")
    print("- service fee sanity: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
