from __future__ import annotations

import json
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = PROJECT_ROOT / "data" / "source_18"
OUTPUT_PATH = PROJECT_ROOT / "data" / "unified" / "unified_knowledge.jsonl"
REPORT_PATH = PROJECT_ROOT / "reports" / "unified_corpus_report.md"


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if not path.exists():
        return rows
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSONL at {path}:{line_number}: {exc}") from exc
        row["_source_file"] = str(path.relative_to(PROJECT_ROOT))
        rows.append(row)
    return rows


def unique_id(base: str, seen: set[str]) -> str:
    value = base
    index = 2
    while value in seen:
        value = f"{base}_{index}"
        index += 1
    seen.add(value)
    return value


def make_row(
    *,
    seen: set[str],
    row_id: str,
    source_kind: str,
    category: str,
    title: str,
    text: str,
    source_url: str = "",
    source_ids: list[str] | None = None,
    tags: list[str] | None = None,
    priority: int = 50,
    answer: str = "",
    evidence: str = "",
    answer_type: str = "fact",
    question_patterns: list[str] | None = None,
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    source_ids = source_ids or []
    tags = tags or []
    question_patterns = question_patterns or []
    metadata = metadata or {}
    search_parts = [
        title,
        text,
        answer,
        evidence,
        " ".join(tags),
        " ".join(question_patterns),
        str(metadata.get("game", "")),
        str(metadata.get("tournament", "")),
        str(metadata.get("intent", "")),
    ]
    return {
        "id": unique_id(row_id, seen),
        "source_kind": source_kind,
        "category": category,
        "title": title,
        "text": text.strip(),
        "answer": answer.strip(),
        "evidence": evidence.strip(),
        "answer_type": answer_type,
        "question_patterns": question_patterns,
        "source_url": source_url,
        "source_ids": source_ids,
        "tags": tags,
        "priority": int(priority or 0),
        "metadata": metadata,
        "search_text": "\n".join(part for part in search_parts if part),
    }


def build_curated(seen: set[str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    curated_dir = SOURCE_DIR / "curated"
    for path in sorted(curated_dir.glob("*.jsonl")):
        if path.name == "rule_patterns.jsonl":
            continue
        for raw in read_jsonl(path):
            text = str(raw.get("text", "")).strip()
            if not text:
                continue
            rows.append(
                make_row(
                    seen=seen,
                    row_id=str(raw.get("id", path.stem)),
                    source_kind="curated_fact",
                    category=str(raw.get("category", "general")),
                    title=str(raw.get("title", raw.get("id", ""))),
                    text=text,
                    answer=text,
                    source_url=str(raw.get("source_url", "")),
                    source_ids=[str(item) for item in raw.get("source_ids", [raw.get("id", "")]) if item],
                    tags=[str(item) for item in raw.get("tags", [])],
                    priority=int(raw.get("priority", 50)),
                    answer_type="fact",
                    metadata={
                        "source_file": raw.get("_source_file"),
                        "game": raw.get("game", ""),
                        "tournament": raw.get("tournament", ""),
                        "section_title": raw.get("section_title", ""),
                    },
                )
            )
    return rows


def build_rulebase(seen: set[str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    rules_dir = SOURCE_DIR / "rules"
    for path in sorted(rules_dir.glob("*.jsonl")):
        for raw in read_jsonl(path):
            answer = str(raw.get("answer_th") or raw.get("answer") or "").strip()
            if not answer:
                continue
            patterns = [str(item) for item in raw.get("patterns", [])]
            title = str(raw.get("intent") or raw.get("id") or path.stem)
            rows.append(
                make_row(
                    seen=seen,
                    row_id=str(raw.get("id", path.stem)),
                    source_kind="rulebase",
                    category=str(raw.get("category", path.stem.replace("_rules", ""))),
                    title=title,
                    text=answer,
                    answer=answer,
                    evidence="; ".join(patterns[:12]),
                    source_url=str(raw.get("source_url", "")),
                    source_ids=[str(item) for item in raw.get("source_ids", [raw.get("id", "")]) if item],
                    tags=[str(raw.get("intent", "")), "rulebase"],
                    priority=int(raw.get("priority", 90)),
                    answer_type="rule_answer",
                    question_patterns=patterns,
                    metadata={"source_file": raw.get("_source_file"), "intent": raw.get("intent", "")},
                )
            )
    return rows


def build_competition_fact_cards(seen: set[str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    path = SOURCE_DIR / "competition_rules" / "competition_rule_fact_cards.jsonl"
    for raw in read_jsonl(path):
        answer = str(raw.get("answer", "")).strip()
        evidence = str(raw.get("evidence", "")).strip()
        if not answer and not evidence:
            continue
        text = answer
        if evidence:
            text += f"\nหลักฐาน: {evidence}"
        rows.append(
            make_row(
                seen=seen,
                row_id=str(raw.get("id", "competition_fact")),
                source_kind="competition_fact_card",
                category="competition_rules",
                title=f"{raw.get('game', '')}: {raw.get('intent', raw.get('id', ''))}",
                text=text,
                answer=answer,
                evidence=evidence,
                source_url=str(raw.get("source_url", "")),
                source_ids=[str(item) for item in raw.get("source_ids", [])],
                tags=[str(item) for item in raw.get("tags", [])],
                priority=int(raw.get("priority", 120)),
                answer_type=str(raw.get("answer_type", "explicit_fact")),
                question_patterns=[str(item) for item in raw.get("question_patterns", [])],
                metadata={
                    "source_file": raw.get("_source_file"),
                    "game": raw.get("game", ""),
                    "tournament": raw.get("tournament", ""),
                    "intent": raw.get("intent", ""),
                },
            )
        )
    return rows


def build_competition_chunks(seen: set[str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    path = SOURCE_DIR / "competition_rules" / "competition_rule_chunks.jsonl"
    for raw in read_jsonl(path):
        text = str(raw.get("text", "")).strip()
        if not text:
            continue
        rows.append(
            make_row(
                seen=seen,
                row_id=str(raw.get("id", "competition_chunk")),
                source_kind="competition_chunk",
                category="competition_rules",
                title=str(raw.get("title") or raw.get("section_title") or raw.get("id", "")),
                text=text,
                answer="",
                evidence="",
                source_url=str(raw.get("source_url", "")),
                source_ids=[str(item) for item in raw.get("source_ids", [])],
                tags=[str(item) for item in raw.get("tags", [])],
                priority=int(raw.get("priority", 55)),
                answer_type="source_chunk",
                metadata={
                    "source_file": raw.get("_source_file"),
                    "game": raw.get("game", ""),
                    "tournament": raw.get("tournament", ""),
                    "section_title": raw.get("section_title", ""),
                },
            )
        )
    return rows


def build_calendar(seen: set[str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    path = SOURCE_DIR / "calendar" / "service_closures.jsonl"
    for raw in read_jsonl(path):
        date = str(raw.get("date", ""))
        title = str(raw.get("title", "วันปิดพิเศษ"))
        status = str(raw.get("status", "closed"))
        note = str(raw.get("note", ""))
        text = f"{date}: {title} สถานะ {status}. {note}".strip()
        rows.append(
            make_row(
                seen=seen,
                row_id=f"calendar_{date}",
                source_kind="calendar_closure",
                category="schedule",
                title=f"วันปิดบริการ {date}",
                text=text,
                answer=text,
                evidence=note,
                source_url=str(raw.get("source", "manual_admin_config")),
                source_ids=[f"calendar_{date}"],
                tags=["calendar", "closure", "holiday", "schedule", date],
                priority=120,
                answer_type="calendar_fact",
                metadata={"source_file": raw.get("_source_file"), "date": date, "status": status},
            )
        )
    return rows


def main() -> None:
    seen: set[str] = set()
    rows: list[dict[str, Any]] = []
    builders = [
        ("curated", build_curated),
        ("rulebase", build_rulebase),
        ("competition_fact_cards", build_competition_fact_cards),
        ("competition_chunks", build_competition_chunks),
        ("calendar", build_calendar),
    ]
    counts: dict[str, int] = {}
    for label, builder in builders:
        built = builder(seen)
        rows.extend(built)
        counts[label] = len(built)

    rows.sort(key=lambda row: (str(row["category"]), str(row["source_kind"]), str(row["id"])))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) for row in rows) + "\n",
        encoding="utf-8",
    )

    category_counts: dict[str, int] = {}
    kind_counts: dict[str, int] = {}
    for row in rows:
        category_counts[str(row["category"])] = category_counts.get(str(row["category"]), 0) + 1
        kind_counts[str(row["source_kind"])] = kind_counts.get(str(row["source_kind"]), 0) + 1

    report = [
        "# Unified Corpus Report",
        "",
        f"- Output: `{OUTPUT_PATH}`",
        f"- Total rows: {len(rows)}",
        "",
        "## Source Counts",
    ]
    report.extend(f"- {key}: {value}" for key, value in counts.items())
    report.extend(["", "## Category Counts"])
    report.extend(f"- {key}: {value}" for key, value in sorted(category_counts.items()))
    report.extend(["", "## Source Kind Counts"])
    report.extend(f"- {key}: {value}" for key, value in sorted(kind_counts.items()))
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(report) + "\n", encoding="utf-8")

    print(f"Wrote {len(rows)} rows -> {OUTPUT_PATH}")
    print(f"Report -> {REPORT_PATH}")


if __name__ == "__main__":
    main()
