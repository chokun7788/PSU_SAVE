from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
SOURCE_URL = "https://esports.phuket.psu.ac.th/Services/our-games"
RAW_OUTPUT = ROOT / "data" / "sources" / "our_games_raw.jsonl"
CURATED_OUTPUT = ROOT / "data" / "curated" / "our_games_scraped_details.jsonl"


ZONE_TITLES = {
    "Nintendo Switch": "Nintendo Switch",
    "PlayStation 5": "PlayStation 5",
}

STOP_MARKERS = (
    "ศูนย์พัฒนาการเรียนรู้ด้านอีสปอร์ตเพื่อความเป็นเลิศ",
    "Report abuse",
    "Page details",
)


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._parts: list[str] = []

    def handle_data(self, data: str) -> None:
        text = " ".join((data or "").split())
        if text:
            self._parts.append(text)

    @property
    def lines(self) -> list[str]:
        return [part.strip() for part in self._parts if part.strip()]


def _fetch_html(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "psu-esports-chatbot-data-ingestion/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", "replace")


def _extract_lines_with_bs4(html: str) -> list[str] | None:
    try:
        from bs4 import BeautifulSoup  # type: ignore
    except Exception:
        return None
    soup = BeautifulSoup(html, "html.parser")
    return [line.strip() for line in soup.get_text("\n").splitlines() if line.strip()]


def _extract_lines_stdlib(html: str) -> list[str]:
    parser = TextExtractor()
    parser.feed(html)
    return parser.lines


def extract_text_lines(html: str) -> list[str]:
    return _extract_lines_with_bs4(html) or _extract_lines_stdlib(html)


def _find_main_content_start(lines: list[str]) -> int:
    for index in range(len(lines) - 2):
        if lines[index] == "Our Games" and lines[index + 1] == "Nintendo Switch":
            return index + 1
    raise RuntimeError("Could not locate main Our Games content block")


def _is_title(line: str, next_line: str | None = None) -> bool:
    if line in ZONE_TITLES:
        return False
    if not line or any(marker in line for marker in STOP_MARKERS):
        return False
    if len(line) > 72:
        return False
    if not re.search(r"[A-Za-z0-9]", line):
        return False
    if line.endswith((".", "!", "?", ":", ",")):
        return False
    if next_line and next_line in ZONE_TITLES:
        return False
    # Game names from the page are short title-like lines, while descriptions are long sentences.
    return True


def _slug(value: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "_", value.lower()).strip("_")
    if cleaned:
        return cleaned[:80]
    digest = hashlib.blake2b(value.encode("utf-8"), digest_size=5).hexdigest()
    return f"game_{digest}"


def _aliases_for(title: str) -> list[str]:
    aliases = {title}
    normalized = title.replace("™", "").replace("®", "").strip()
    aliases.add(normalized)
    aliases.add(re.sub(r"\s+", " ", normalized).strip())
    aliases.add(re.sub(r"[:™®]", "", normalized).strip())
    if "Standard Edition" in normalized:
        aliases.add(normalized.replace("Standard Edition", "").strip(" :-"))
    if "(Remastered)" in normalized:
        aliases.add(normalized.replace("(Remastered)", "").strip())
    if "+" in normalized:
        for part in normalized.split("+"):
            if part.strip():
                aliases.add(part.strip())
    if "Call of Duty" in normalized:
        aliases.add("Call of Duty")
        aliases.add("Modern Warfare III")
        aliases.add("MW3")
    if "Resident Evil" in normalized:
        aliases.add("Resident Evil")
    if "The Last of Us" in normalized:
        aliases.add("The Last of Us")
    return sorted(alias for alias in aliases if alias)


def _source_summary(paragraphs: list[str], max_chars: int = 460) -> str:
    text = " ".join(paragraphs).strip()
    if len(text) <= max_chars:
        return text
    clipped = text[:max_chars].rstrip()
    clipped = re.sub(r"\s+\S*$", "", clipped).rstrip()
    return clipped + "..."


def parse_games(lines: list[str]) -> list[dict]:
    start = _find_main_content_start(lines)
    rows: list[dict] = []
    source_section = ""
    current: dict | None = None

    def flush_current() -> None:
        nonlocal current
        if current is None:
            return
        current["description"] = " ".join(current.pop("_paragraphs")).strip()
        rows.append(current)
        current = None

    index = start
    while index < len(lines):
        line = lines[index]
        if any(marker in line for marker in STOP_MARKERS):
            break
        if line in ZONE_TITLES:
            flush_current()
            source_section = ZONE_TITLES[line]
            index += 1
            continue
        next_line = lines[index + 1] if index + 1 < len(lines) else None
        if source_section and _is_title(line, next_line):
            flush_current()
            current = {
                "game": line,
                "source_section": source_section,
                "source_url": SOURCE_URL,
                "source_page": "Our Games",
                "_paragraphs": [],
            }
        elif current is not None:
            current["_paragraphs"].append(line)
        index += 1
    flush_current()
    return [row for row in rows if row.get("description")]


def to_raw_rows(rows: Iterable[dict]) -> list[dict]:
    scraped_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    output = []
    for row in rows:
        title = str(row["game"]).strip()
        output.append({
            "id": f"our_games_raw_{_slug(title)}",
            "category": "games",
            "game": title,
            "source_section": row["source_section"],
            "listed_under": row["source_section"],
            "description": row["description"],
            "aliases": _aliases_for(title),
            "source_url": row["source_url"],
            "source_page": row["source_page"],
            "scraped_at_utc": scraped_at,
        })
    return output


def to_curated_rows(raw_rows: Iterable[dict]) -> list[dict]:
    output = []
    for row in raw_rows:
        title = str(row["game"]).strip()
        description = str(row["description"]).strip()
        source_section = str(row["source_section"])
        summary = _source_summary([description])
        output.append({
            "id": f"our_games_scraped_{_slug(title)}",
            "category": "games",
            "title": title,
            "text": f"{title}: {summary}\nอยู่ในรายการเกมหน้า Our Games ส่วน: {source_section}",
            "game": title,
            "source_section": source_section,
            "listed_under": source_section,
            "summary_th": summary,
            "aliases": row["aliases"],
            "tags": ["games", "our_games", "scraped", source_section, title, *_aliases_for(title)],
            "source_url": row["source_url"],
            "priority": 16,
        })
    return output


def write_jsonl(path: Path, rows: Iterable[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False, sort_keys=True) for row in rows) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Scrape PSU Esports Our Games into JSONL")
    parser.add_argument("--url", default=SOURCE_URL)
    parser.add_argument("--raw-output", default=str(RAW_OUTPUT))
    parser.add_argument("--curated-output", default=str(CURATED_OUTPUT))
    args = parser.parse_args()

    html = _fetch_html(args.url)
    rows = parse_games(extract_text_lines(html))
    raw_rows = to_raw_rows(rows)
    curated_rows = to_curated_rows(raw_rows)
    write_jsonl(Path(args.raw_output), raw_rows)
    write_jsonl(Path(args.curated_output), curated_rows)

    by_zone: dict[str, int] = {}
    for row in raw_rows:
        zone = row["source_section"]
        by_zone[zone] = by_zone.get(zone, 0) + 1

    print("OUR GAMES SCRAPE OK")
    print(f"- source: {args.url}")
    print(f"- games: {len(raw_rows)}")
    for zone, count in sorted(by_zone.items()):
        print(f"- {zone}: {count}")
    print(f"- raw: {args.raw_output}")
    print(f"- curated: {args.curated_output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
