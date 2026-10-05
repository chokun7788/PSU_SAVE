from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOWNLOADS = Path.home() / "Downloads"
OUT_DIR = ROOT / "data" / "competition_rules"
CURATED_OUT = ROOT / "data" / "curated" / "curated_competition_rules.jsonl"


@dataclass(frozen=True)
class RuleSource:
    document_id: str
    game: str
    tournament: str
    pattern: str
    aliases: tuple[str, ...]


SOURCES = (
    RuleSource(
        "competition_rules_cs2_psu_phuket_2026",
        "Counter-Strike 2",
        "PSU Phuket CS2 2026 Tournament",
        "*Counter-Strike 2*.txt",
        ("cs2", "counter-strike 2", "counter strike 2", "psu phuket cs2 2026"),
    ),
    RuleSource(
        "competition_rules_rov_blueket_2025_men",
        "Arena of Valor (RoV)",
        "Blueket Games 2025 ประเภททีมชาย",
        "*Arena of Valor*.txt",
        ("rov", "arena of valor", "blueket games 2025", "aov"),
    ),
    RuleSource(
        "competition_rules_tekken8_psu_esports",
        "Tekken 8",
        "PSU Esports ปะทะมันส์ สนั่นจอ",
        "*Tekken 8*.txt",
        ("tekken 8", "tekken8", "psu esports ปะทะมันส์"),
    ),
    RuleSource(
        "competition_rules_valorant_psu_phuket_2026",
        "VALORANT",
        "PSU Phuket VALORANT 2026 Tournament",
        "*VALORANT*.txt",
        ("valorant", "psu phuket valorant 2026", "วาโล"),
    ),
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").replace("\r", "\n").strip()


def clean_lines(text: str) -> list[str]:
    lines: list[str] = []
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip():
            continue
        if line.lower().startswith("may be a graphic of text"):
            continue
        line = re.sub(r"[ \t]+", " ", line).strip()
        lines.append(line)
    return lines


def is_top_number_heading(line: str) -> bool:
    # Top-level document headings: "1. Title", "2. Title".
    return bool(re.match(r"^\d+\.\s+\S", line))


def is_plain_heading(line: str, next_line: str | None) -> bool:
    if not next_line:
        return False
    if len(line) > 90:
        return False
    if re.match(r"^(\*|-|·|\d+[\.\)])", line):
        return False
    if line.endswith((".", ":", "ๆ")):
        return False
    return bool(re.match(r"^(\*|-|·|\d+[\.\)])", next_line))


def split_sections(lines: list[str]) -> list[tuple[str, list[str]]]:
    sections: list[tuple[str, list[str]]] = []
    current_title = "ภาพรวมเอกสาร"
    current: list[str] = []

    for index, line in enumerate(lines):
        next_line = lines[index + 1] if index + 1 < len(lines) else None
        is_heading = is_top_number_heading(line) or is_plain_heading(line, next_line)
        if is_heading:
            if current:
                sections.append((current_title, current))
            current_title = line
            current = [line]
        else:
            current.append(line)

    if current:
        sections.append((current_title, current))
    return sections


def chunk_section(lines: list[str], max_chars: int = 1400) -> list[str]:
    chunks: list[str] = []
    current: list[str] = []
    current_len = 0
    for line in lines:
        extra = len(line) + 1
        if current and current_len + extra > max_chars:
            chunks.append("\n".join(current).strip())
            current = []
            current_len = 0
        current.append(line)
        current_len += extra
    if current:
        chunks.append("\n".join(current).strip())
    return chunks


def infer_tags(source: RuleSource, title: str, text: str) -> list[str]:
    haystack = f"{source.game} {source.tournament} {title} {text}".lower()
    tags = ["competition_rules", "tournament_rules", source.document_id, source.game.lower()]
    tags.extend(source.aliases)
    keyword_tags = {
        "schedule": ("กำหนดการแข่งขัน", "schedule", "เวลา", "วันที่"),
        "eligibility": ("คุณสมบัติ", "ผู้เล่น", "ทีม", "ลงทะเบียน"),
        "format": ("รูปแบบการแข่งขัน", "single elimination", "best of", "bo3", "ft2", "1v1", "5v5"),
        "equipment": ("อุปกรณ์", "keyboard", "mouse", "playstation", "pc", "โทรศัพท์"),
        "map": ("แผนที่", "map", "map pool", "mapban"),
        "pause": ("pause", "หยุดเกม", "เวลานอก", "technical pause", "timeout"),
        "penalty": ("บทลงโทษ", "ปรับแพ้", "ตัดสิทธิ์", "แบน", "penalty", "forfeit"),
        "bug": ("bug", "บัค", "glitch", "exploit"),
        "settings": ("settings", "การตั้งค่า", "resolution", "crosshair", "blood", "fps"),
        "protest": ("ประท้วง", "ข้อพิพาท", "challenge"),
    }
    for tag, words in keyword_tags.items():
        if any(word.lower() in haystack for word in words):
            tags.append(tag)
    return sorted(set(tags))


def find_source_file(source: RuleSource) -> Path:
    matches = sorted(DOWNLOADS.glob(source.pattern), key=lambda path: path.stat().st_mtime, reverse=True)
    if not matches:
        raise FileNotFoundError(f"No file matched {source.pattern} in {DOWNLOADS}")
    return matches[0]


def build_rows() -> tuple[list[dict], list[dict], list[dict]]:
    documents: list[dict] = []
    chunks: list[dict] = []
    curated: list[dict] = []

    for source in SOURCES:
        path = find_source_file(source)
        text = read_text(path)
        lines = clean_lines(text)
        title = lines[0] if lines else source.tournament
        source_url = f"local://competition_rules/{source.document_id}"

        documents.append({
            "id": source.document_id,
            "category": "competition_rules_document",
            "title": title,
            "game": source.game,
            "tournament": source.tournament,
            "source_file": path.name,
            "source_path": str(path),
            "source_url": source_url,
            "language": "th/mixed",
            "char_count": len(text),
            "line_count": len(lines),
            "tags": ["competition_rules", "document", *source.aliases],
        })

        sections = split_sections(lines)
        section_index = 0
        for section_title, section_lines in sections:
            section_index += 1
            for chunk_index, chunk_text in enumerate(chunk_section(section_lines), start=1):
                chunk_id = f"{source.document_id}_s{section_index:02d}_c{chunk_index:02d}"
                tags = infer_tags(source, section_title, chunk_text)
                chunk_row = {
                    "id": chunk_id,
                    "document_id": source.document_id,
                    "category": "competition_rules",
                    "title": f"{source.game}: {section_title}",
                    "game": source.game,
                    "tournament": source.tournament,
                    "section_title": section_title,
                    "section_index": section_index,
                    "chunk_index": chunk_index,
                    "text": chunk_text,
                    "source_file": path.name,
                    "source_path": str(path),
                    "source_url": source_url,
                    "tags": tags,
                    "priority": 90,
                }
                chunks.append(chunk_row)
                curated.append({
                    "id": chunk_id,
                    "category": "competition_rules",
                    "title": chunk_row["title"],
                    "text": chunk_text,
                    "source_url": source_url,
                    "source_ids": [source.document_id, chunk_id],
                    "tags": tags,
                    "priority": 90,
                    "game": source.game,
                    "tournament": source.tournament,
                    "section_title": section_title,
                })

    return documents, chunks, curated


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as file:
        for row in rows:
            file.write(json.dumps(row, ensure_ascii=False) + "\n")


def main() -> int:
    documents, chunks, curated = build_rows()
    write_jsonl(OUT_DIR / "competition_rule_documents.jsonl", documents)
    write_jsonl(OUT_DIR / "competition_rule_chunks.jsonl", chunks)
    write_jsonl(CURATED_OUT, curated)

    summary = {
        "documents": len(documents),
        "chunks": len(chunks),
        "curated_rows": len(curated),
        "output_dir": str(OUT_DIR),
        "curated_output": str(CURATED_OUT),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
