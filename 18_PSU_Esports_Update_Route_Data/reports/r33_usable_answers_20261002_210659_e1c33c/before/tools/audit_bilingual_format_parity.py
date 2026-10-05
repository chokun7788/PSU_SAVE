from __future__ import annotations

"""Compare Thai and English response shape for representative public FAQ routes."""

import argparse
import os
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
os.environ.setdefault("PSU_BILINGUAL_EN_ENABLED", "1")
os.environ.setdefault("PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW", "1")
os.environ.setdefault(
    "PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW_PATH",
    str(ROOT / "data" / "locales" / "en" / "localization_review_drafts_machine_20260909_verified.jsonl"),
)

from app.pipeline.engine import AnswerQualityPipeline  # noqa: E402


PAIRS = (
    ("catalog", "มีเกมอะไรบ้าง", "What games are available?"),
    ("price", "PC ราคาเท่าไหร่", "What is the price of the PC?"),
    ("schedule_tomorrow", "พรุ่งนี้ตอน 13:00 เปิดไหม", "Is it open tomorrow at 13:00?"),
    ("booking", "จองยังไง", "How do I make a booking?"),
    ("studio_rules", "กติกาในศูนย์มีอะไรบ้าง", "What are the studio rules?"),
    ("member_role", "ใครเป็นผู้จัดการ", "Who is the manager?"),
    ("vr_equipment", "VR Zone มีอุปกรณ์อะไรบ้าง", "What equipment is available in VR Zone?"),
    ("unknown_game", "มี Minecraft ไหม", "Can I play Minecraft at the studio?"),
)


def _shape(result: Any) -> dict[str, Any]:
    answer = str(result.answer or "")
    lines = [line.strip() for line in answer.splitlines() if line.strip()]
    return {
        "route": f"{result.route.category}/{result.route.intent}",
        "mode": str(result.mode),
        "lines": len(lines),
        "bullets": sum(line.startswith(("•", "-")) for line in lines),
        "source": "Source:" in answer or "แหล่งข้อมูล" in answer,
        "localization_pending": "missing_english_localization" in str(result.mode),
        "preview": " / ".join(lines[:2])[:220],
    }


def _parity_status(th: dict[str, Any], en: dict[str, Any]) -> str:
    if en["localization_pending"]:
        return "content_gap"
    if th["route"].split("/", 1)[0] != en["route"].split("/", 1)[0]:
        return "route_mismatch"
    if th["source"] != en["source"]:
        return "source_format_gap"
    if abs(int(th["bullets"]) - int(en["bullets"])) >= 3:
        return "list_format_gap"
    if abs(int(th["lines"]) - int(en["lines"])) >= 5:
        return "detail_depth_gap"
    return "format_aligned"


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit Thai-English response-format parity for core FAQ routes.")
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "reports" / "bilingual_english" / "format_parity_20260910.md",
    )
    args = parser.parse_args()

    pipeline = AnswerQualityPipeline()
    rows: list[dict[str, Any]] = []
    for case_id, question_th, question_en in PAIRS:
        thai = pipeline.answer(
            question_th,
            locale="th",
            experimental_allow_llm=False,
            experimental_rag_fallback=True,
            global_timeout_sec=10.0,
        )
        english = pipeline.answer(
            question_en,
            locale="en",
            experimental_allow_llm=False,
            experimental_rag_fallback=True,
            global_timeout_sec=10.0,
        )
        th_shape = _shape(thai)
        en_shape = _shape(english)
        rows.append(
            {
                "id": case_id,
                "question_th": question_th,
                "question_en": question_en,
                "thai": th_shape,
                "english": en_shape,
                "status": _parity_status(th_shape, en_shape),
            }
        )

    status_counts: dict[str, int] = {}
    for row in rows:
        status_counts[row["status"]] = status_counts.get(row["status"], 0) + 1

    lines = [
        "# Thai-English Format Parity Audit",
        "",
        "> Scope: representative core FAQ pairs. This checks route and response shape, not translation quality.",
        "",
        "## Summary",
        f"- Pairs checked: {len(rows)}",
        f"- Status counts: {status_counts}",
        "",
        "## Pair Results",
        "",
        "| Case | Thai route/mode | English route/mode | Thai shape | English shape | Status |",
        "|---|---|---|---:|---:|---|",
    ]
    for row in rows:
        thai = row["thai"]
        english = row["english"]
        lines.append(
            f"| {row['id']} | {thai['route']} / {thai['mode']} | "
            f"{english['route']} / {english['mode']} | "
            f"{thai['lines']} lines, {thai['bullets']} bullets | "
            f"{english['lines']} lines, {english['bullets']} bullets | {row['status']} |"
        )

    lines.extend(["", "## Answer Previews", ""])
    for row in rows:
        lines.extend(
            [
                f"### {row['id']}",
                f"- Thai: {row['thai']['preview']}",
                f"- English: {row['english']['preview']}",
                f"- Assessment: {row['status']}",
                "",
            ]
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {args.output}")
    for row in rows:
        print(
            f"{row['id']}: {row['status']} | "
            f"TH={row['thai']['route']} ({row['thai']['lines']} lines) | "
            f"EN={row['english']['route']} ({row['english']['lines']} lines)"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
