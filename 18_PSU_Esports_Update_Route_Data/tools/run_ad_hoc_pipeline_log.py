from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict, is_dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.runtime.pipeline_answer import answer_question_pipeline_debug  # noqa: E402


DEFAULT_QUESTIONS = [
    "Sony PlayStation VR2 คืออะไร",
    "Sony PlayStation VR2 เล่นยังไง",
    "Logitech G923 คืออะไร",
    "พวงมาลัย Logitech G923 เล่นยังไง",
    "Racezone Full Cockpit V3 คืออะไร",
    "Driving Force Shifter ใช้ทำอะไร",
    "Pulse Elite Wireless Headset คืออะไร",
    "Nintendo Switch OLED คืออะไร",
    "PlayStation 5 Slim คืออะไร",
    "Gaming Mouse คืออะไร",
    "Gaming Keyboard ใช้ยังไง",
    "TV 65 นิ้ว ใช้ทำอะไร",
    "VR Zone คืออะไร",
    "Cockpit Zone คืออะไร",
    "เล่น Minecraft ได้ไหม",
    "Roblox เล่นได้ไหม",
]


def json_default(value: Any) -> Any:
    if is_dataclass(value):
        return asdict(value)
    if isinstance(value, Path):
        return str(value)
    return str(value)


def source_list(hits: list[dict[str, Any]]) -> list[dict[str, str]]:
    sources: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for hit in hits or []:
        metadata = hit.get("metadata", {}) if isinstance(hit, dict) else {}
        source_id = str(hit.get("id") or metadata.get("title") or metadata.get("source_id") or "")
        url = str(metadata.get("source_url") or metadata.get("url") or "")
        key = (source_id, url)
        if key in seen:
            continue
        seen.add(key)
        sources.append({"id": source_id, "url": url})
    return sources


def load_questions(path: Path | None, cli_questions: list[str]) -> list[str]:
    questions: list[str] = []
    questions.extend(q.strip() for q in cli_questions if q.strip())
    if path is not None:
        for line in path.read_text(encoding="utf-8").splitlines():
            clean = line.strip()
            if clean and not clean.startswith("#"):
                questions.append(clean)
    return questions or DEFAULT_QUESTIONS


def build_markdown(rows: list[dict[str, Any]], jsonl_path: Path) -> str:
    lines = [
        "# Ad Hoc Pipeline Test Log",
        "",
        f"- Generated: {datetime.now().isoformat(timespec='seconds')}",
        f"- JSONL: `{jsonl_path}`",
        f"- Total questions: {len(rows)}",
        "",
        "## Summary",
        "",
    ]
    by_route: dict[str, int] = {}
    for row in rows:
        key = f"{row['route_category']}/{row['route_intent']}"
        by_route[key] = by_route.get(key, 0) + 1
    for key, count in sorted(by_route.items()):
        lines.append(f"- {key}: {count}")

    lines.extend(["", "## Results", ""])
    for index, row in enumerate(rows, 1):
        lines.extend([
            f"### {index}. {row['question']}",
            "",
            f"- mode: `{row['mode']}`",
            f"- route: `{row['route_category']}/{row['route_intent']}`",
            f"- confidence: `{row['confidence']}`",
            f"- elapsed: `{row['elapsed']}` sec",
            "",
            "คำตอบ:",
            "",
            row["answer"],
            "",
            "แหล่งข้อมูล:",
        ])
        for source in row["sources"]:
            lines.append(f"- {source['id']} | {source['url']}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Run ad hoc PSU Esports chatbot questions and save JSONL/Markdown logs.")
    parser.add_argument("--label", default=datetime.now().strftime("adhoc_%Y%m%d_%H%M%S"))
    parser.add_argument("--question", action="append", default=[], help="Question to test. Can be repeated.")
    parser.add_argument("--questions-file", type=Path, default=None, help="UTF-8 text file with one question per line.")
    args = parser.parse_args()

    questions = load_questions(args.questions_file, args.question)
    report_dir = ROOT / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    jsonl_path = report_dir / f"ad_hoc_pipeline_results_{args.label}.jsonl"
    md_path = report_dir / f"ad_hoc_pipeline_results_{args.label}.md"

    rows: list[dict[str, Any]] = []
    for question in questions:
        result = answer_question_pipeline_debug(question)
        rows.append({
            "question": question,
            "answer": result.answer,
            "mode": result.mode,
            "route_category": result.route.category,
            "route_intent": result.route.intent,
            "confidence": result.confidence,
            "elapsed": result.elapsed,
            "sources": source_list(result.hits),
            "entities": result.entities,
            "validation": result.validation,
            "trace": result.trace,
        })

    with jsonl_path.open("w", encoding="utf-8", newline="\n") as file:
        for row in rows:
            file.write(json.dumps(row, ensure_ascii=False, default=json_default) + "\n")
    md_path.write_text(build_markdown(rows, jsonl_path), encoding="utf-8", newline="\n")

    print(f"questions={len(rows)}")
    print(f"jsonl={jsonl_path}")
    print(f"markdown={md_path}")
    print("routes:")
    counts: dict[str, int] = {}
    for row in rows:
        key = f"{row['route_category']}/{row['route_intent']}"
        counts[key] = counts.get(key, 0) + 1
    for key, count in sorted(counts.items()):
        print(f"- {key}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
