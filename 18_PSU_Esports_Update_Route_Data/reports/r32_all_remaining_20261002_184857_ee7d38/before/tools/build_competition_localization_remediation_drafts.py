#!/usr/bin/env python3
"""Create a narrow, reviewable English draft batch for proven rule sections.

The batch deliberately contains only source chunks that were verified during
the competition-RAG remediation. It is not a publishing tool: every record is
written as ``draft`` and must still pass the normal review/approval workflow.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.knowledge.localization import source_text_sha256  # noqa: E402


SOURCE_PATH = ROOT / "data" / "competition_rules" / "competition_rule_chunks.jsonl"
OUTPUT_PATH = ROOT / "data" / "locales" / "en" / "localization_review_drafts_competition_remediation_20260921.jsonl"


# Each translation mirrors the corresponding Thai source section. Do not add
# context or policy that is not present in that source row.
TRANSLATIONS: dict[tuple[str, str], str] = {
    (
        "competition_rules_cs2_psu_phuket_2026_s15_c01",
        "section_title",
    ): "7. Match schedule",
    (
        "competition_rules_cs2_psu_phuket_2026_s15_c01",
        "text",
    ): "7. Match schedule: The bracket will be announced at least one day in advance. Teams must confirm participation before the match begins. Late arrival may result in disqualification.",
    (
        "competition_rules_cs2_psu_phuket_2026_s36_c01",
        "section_title",
    ): "1. Player conduct",
    (
        "competition_rules_cs2_psu_phuket_2026_s36_c01",
        "text",
    ): "1. Player conduct: Aggressive behaviour, hateful speech (including racial or religious discrimination), and unsportsmanlike conduct are prohibited.",
    (
        "competition_rules_cs2_psu_phuket_2026_s54_c01",
        "section_title",
    ): "8. Penalty table",
    (
        "competition_rules_cs2_psu_phuket_2026_s54_c01",
        "text",
    ): "8. Penalty table:\nViolation | Penalty\nAbusive or violent language | Warning, then round loss, then disqualification\nCheating of any kind | Round loss or disqualification\nWatching a stream during a match | Match loss\nPausing without permission | Round loss\nUsing a bug | Round or match loss\nUnethical conduct | Round loss, then disqualification\nIgnoring an official decision | Round loss or disqualification\nInappropriate in-game chat | Round or match loss",
    (
        "competition_rules_rov_blueket_2025_men_s06_c01",
        "section_title",
    ): "4. Competition rules and regulations",
    (
        "competition_rules_rov_blueket_2025_men_s06_c01",
        "text",
    ): "4. Competition rules and regulations\n4.3 Disconnect and rematch\n4.3.1 If a participant disconnects, pause the game temporarily. Each team may pause up to five times, for no more than one minute each. After that limit, the other team may resume play immediately.",
}


def _read_rows(path: Path) -> dict[str, dict[str, Any]]:
    return {
        str(row["id"]): row
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
        for row in (json.loads(line),)
    }


def main() -> int:
    sources = _read_rows(SOURCE_PATH)
    output: list[dict[str, Any]] = []
    for (content_id, field), text in sorted(TRANSLATIONS.items()):
        source = sources.get(content_id)
        if source is None:
            raise SystemExit(f"Unknown source chunk: {content_id}")
        source_text = source.get(field)
        if not source_text:
            raise SystemExit(f"Missing source field: {content_id}/{field}")
        output.append({
            "content_id": content_id,
            "field": field,
            "locale": "en",
            "text": text,
            "source_text": source_text,
            "source_text_sha256": source_text_sha256(source_text),
            "status": "draft",
            "version": 1,
            "approved_by": "",
            "approved_at": "",
            "source_path": "data/competition_rules/competition_rule_chunks.jsonl",
            "category": "competition_rules",
            "title": source.get("title") or content_id,
        })
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    temporary = OUTPUT_PATH.with_suffix(".jsonl.tmp")
    temporary.write_text(
        "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in output),
        encoding="utf-8",
    )
    os.replace(temporary, OUTPUT_PATH)
    print(json.dumps({"ok": True, "records": len(output), "output": str(OUTPUT_PATH)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
