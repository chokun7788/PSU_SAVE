from __future__ import annotations

import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[1]
RAW_SECTIONS_DIR = PROJECT_DIR / "data" / "raw_sections"
CURATED_DIR = PROJECT_DIR / "data" / "curated"
OUTPUT_PATH = PROJECT_DIR / "data" / "processed" / "optimized_chunks.jsonl"
MANIFEST_PATH = PROJECT_DIR / "data" / "processed" / "optimization_manifest.json"

MAX_CHARS = 900
HARD_MAX_CHARS = 1200
OVERLAP_LINES = 1


SECTION_CATEGORY = {
    "Home": "overview",
    "Reservation": "reservation",
    "Services": "games",
    "Contact_Us": "contact",
    "Knowledge": "knowledge",
    "Events_and_News": "events_news",
    "About_Us": "about_us",
}

SECTION_PRIORITY = {
    "reservation": 10,
    "booking_rules": 10,
    "service_fee": 10,
    "rules": 9,
    "penalty": 9,
    "equipment": 9,
    "services": 8,
    "games": 8,
    "contact": 8,
    "overview": 7,
    "events_news": 7,
    "about_us": 7,
    "knowledge": 6,
    "general": 3,
}

BOILERPLATE_LINES = {
    "Skip to content",
    "Reserve Now",
    "Learn More",
    "Read more",
    "Book an appointment on",
    "Your local time",
    "Back Next",
    "Click to copy",
}

FOOTER_STARTS = [
    "ศูนย์พัฒนาการเรียนรู้ด้านอีสปอร์ตเพื่อความเป็นเลิศ",
    "มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1",
]

MONTH_RE = (
    r"January|February|Febuary|March|April|May|June|July|August|September|"
    r"October|November|December"
)
DATE_LINE_RE = re.compile(rf"^\d{{1,2}}(?:\s+\d)?\s+(?:{MONTH_RE})\s+202\s*\d$", re.I)


def count_thai(text: str) -> int:
    return sum(1 for ch in text if "\u0E00" <= ch <= "\u0E7F")


def mojibake_score(text: str) -> int:
    markers = ["à¸", "à¹", "Â", "â€", "ðŸ"]
    return sum(text.count(marker) for marker in markers)


def repair_mojibake(text: str) -> str:
    if not isinstance(text, str):
        return ""
    original = text.replace("\xa0", " ")
    if mojibake_score(original) <= 2:
        return original
    try:
        fixed = original.encode("latin1", errors="ignore").decode("utf-8", errors="ignore")
        if count_thai(fixed) > count_thai(original):
            return fixed.replace("\xa0", " ")
    except Exception:
        pass
    return original


def normalize_text(text: str) -> str:
    text = repair_mojibake(text)
    text = text.replace("\u2028", "\n").replace("\u2029", "\n").replace("\ufeff", "")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9\u0E00-\u0E7F]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value[:80] or "chunk"


def split_pages(section_text: str) -> list[str]:
    pages = re.split(r"\n\s*---\s*\n", section_text)
    if len(pages) == 1:
        pages = re.split(r"\s+\|\s+---\s+\|\s+", section_text)
    return [page.strip() for page in pages if page.strip()]


def extract_source_url(page_text: str) -> str:
    match = re.search(r"^Source URL:\s*(.*?)\s*$", page_text, flags=re.M)
    if match:
        return match.group(1).strip()
    match = re.search(r"Source URL:\s*(.*?)\s*(?:\||\n)", page_text)
    return match.group(1).strip() if match else ""


def extract_title(page_text: str, fallback: str) -> str:
    first_line = page_text.splitlines()[0].strip() if page_text.splitlines() else ""
    if first_line.startswith("#"):
        first_line = first_line.lstrip("#").strip()
    first_piece = first_line.split("|", 1)[0].strip()
    return first_piece or fallback


def clean_lines(text: str, *, keep_footer: bool = False) -> list[str]:
    lines: list[str] = []
    for raw_line in normalize_text(text).splitlines():
        line = raw_line.strip(" -")
        if not line:
            continue
        if line.startswith("# "):
            line = line[2:].strip()
        if line.startswith("Source URL:") or line.startswith("Final URL:"):
            continue
        if line in BOILERPLATE_LINES:
            continue
        if not keep_footer and any(line.startswith(prefix) for prefix in FOOTER_STARTS):
            continue
        lines.append(line)
    return lines


def line_index(lines: list[str], needle: str, start: int = 0) -> int:
    needle_lower = needle.lower()
    for idx in range(start, len(lines)):
        if needle_lower in lines[idx].lower():
            return idx
    return -1


def slice_lines(lines: list[str], start_needle: str, end_needle: str | None = None) -> list[str]:
    start = line_index(lines, start_needle)
    if start < 0:
        return []
    end = len(lines)
    if end_needle:
        end_idx = line_index(lines, end_needle, start + 1)
        if end_idx >= 0:
            end = end_idx
    return lines[start:end]


def hard_split_text(text: str, max_chars: int = HARD_MAX_CHARS) -> list[str]:
    text = normalize_text(text)
    if len(text) <= max_chars:
        return [text] if text else []

    pieces: list[str] = []
    parts = re.split(r"(?<=[.!?。])\s+|\n+", text)
    current: list[str] = []
    current_len = 0
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if len(part) > max_chars:
            if current:
                pieces.append(" ".join(current).strip())
                current = []
                current_len = 0
            for start in range(0, len(part), max_chars):
                pieces.append(part[start : start + max_chars].strip())
            continue
        projected = current_len + len(part) + 1
        if current and projected > max_chars:
            pieces.append(" ".join(current).strip())
            current = []
            current_len = 0
        current.append(part)
        current_len += len(part) + 1
    if current:
        pieces.append(" ".join(current).strip())
    return [piece for piece in pieces if piece]


def chunk_lines(lines: list[str], max_chars: int = MAX_CHARS, overlap_lines: int = OVERLAP_LINES) -> list[str]:
    chunks: list[str] = []
    current: list[str] = []
    current_len = 0

    def flush() -> None:
        nonlocal current, current_len
        if current:
            text = "\n".join(current).strip()
            for piece in hard_split_text(text):
                if len(piece) >= 40:
                    chunks.append(piece)
            current = current[-overlap_lines:] if overlap_lines > 0 else []
            current_len = sum(len(x) + 1 for x in current)

    for line in lines:
        line = normalize_text(line)
        if not line:
            continue
        line_len = len(line) + 1
        if current and current_len + line_len > max_chars:
            flush()
        if line_len > HARD_MAX_CHARS:
            flush()
            for piece in hard_split_text(line):
                chunks.append(piece)
            current = []
            current_len = 0
        else:
            current.append(line)
            current_len += line_len
    if current:
        text = "\n".join(current).strip()
        for piece in hard_split_text(text):
            if len(piece) >= 40:
                chunks.append(piece)
    return chunks


def infer_fine_category(text: str, base_category: str, *, section_name: str = "", title: str = "") -> str:
    hay = f"{title}\n{text}".lower()

    if section_name == "Events_and_News":
        return "events_news"
    if section_name == "About_Us":
        return "about_us"
    if section_name == "Knowledge":
        return "knowledge"
    if section_name == "Contact_Us":
        return "contact"

    if any(k in hay for k in ["service fee", "ค่าบริการ", "ราคา", "กี่บาท", "fee", "rates"]):
        return "service_fee"
    if any(k in hay for k in ["gaming monitor", "gaming chair", "logitech g923", "racezone", "playstation vr2", "msi mag", "equipment", "equipments", "zone"]):
        return "equipment"
    if any(k in hay for k in ["ค่าปรับ", "ชดเชย", "เสียหาย", "ระงับสิทธิ์", "penalty", "damage", "suspension", "อุทธรณ์", "ละเมิดกฎ"]):
        return "penalty"
    if any(k in hay for k in ["กฎ", "ห้าม", "สูบบุหรี่", "แอลกอฮอล์", "การพนัน", "regulation", "rules", "ฝากสัมภาระ"]):
        return "rules"
    if any(k in hay for k in ["เช็คอิน", "จอง", "ชำระ", "ยกเลิก", "booking", "reservation", "payment", "refund", "bank account"]):
        return "reservation"
    if any(k in hay for k in ["1 person", "persons", "60 min", "30 min", "select a service"]):
        return "services"
    if any(k in hay for k in ["ps5", "playstation", "nintendo", "switch", "vr", "pc #", "เกม", "games", "tekken", "valorant"]):
        return "games"
    return base_category


def make_chunks(
    *,
    chunk_id_prefix: str,
    title: str,
    source_url: str,
    category: str,
    section: str,
    lines: list[str],
    tags: list[str] | None = None,
    priority: int | None = None,
) -> list[dict]:
    chunks: list[dict] = []
    tags = tags or []
    for chunk_index, chunk_text in enumerate(chunk_lines(lines), 1):
        final_category = category or infer_fine_category(chunk_text, SECTION_CATEGORY.get(section, "general"), section_name=section, title=title)
        chunks.append(
            {
                "id": f"{chunk_id_prefix}-{chunk_index:03d}",
                "source_type": "webscraping_structured",
                "source_url": source_url,
                "title": title,
                "category": final_category,
                "section": section,
                "chunk_index": chunk_index - 1,
                "priority": priority if priority is not None else SECTION_PRIORITY.get(final_category, 5),
                "tags": tags,
                "text": chunk_text,
                "char_count": len(chunk_text),
                "thai_chars": count_thai(chunk_text),
                "mojibake_score": mojibake_score(chunk_text),
            }
        )
    return chunks


def build_home_chunks(page: str) -> list[dict]:
    section = "Home"
    source_url = extract_source_url(page)
    lines = clean_lines(page, keep_footer=True)
    chunks: list[dict] = []

    chunks += make_chunks(
        chunk_id_prefix="home-overview",
        title="Home - Overview and Mission",
        source_url=source_url,
        category="overview",
        section=section,
        lines=slice_lines(lines, "PSU Esports Studio - Phuket", "Equipments"),
        tags=["home", "overview", "mission"],
    )

    zones = [
        ("home-equipment-cockpit", "Home - Cockpit Zone Equipment", "Cockpit Zone", "Nintendo switch Zone", ["equipment", "cockpit"]),
        ("home-equipment-nintendo", "Home - Nintendo Switch Zone Equipment", "Nintendo switch Zone", "PC Zone", ["equipment", "nintendo"]),
        ("home-equipment-pc", "Home - PC Zone Equipment", "PC Zone", "PLAYstation5 Zone", ["equipment", "pc"]),
        ("home-equipment-ps5", "Home - PlayStation 5 Zone Equipment", "PLAYstation5 Zone", "VR Zone", ["equipment", "ps5"]),
        ("home-equipment-vr", "Home - VR Zone Equipment", "VR Zone", "Popular Games", ["equipment", "vr"]),
    ]
    for prefix, title, start, end, tags in zones:
        chunks += make_chunks(
            chunk_id_prefix=prefix,
            title=title,
            source_url=source_url,
            category="equipment",
            section=section,
            lines=slice_lines(lines, start, end),
            tags=tags,
        )

    chunks += make_chunks(
        chunk_id_prefix="home-popular-games",
        title="Home - Popular Games",
        source_url=source_url,
        category="games",
        section=section,
        lines=slice_lines(lines, "Popular Games", "Regulation for Using"),
        tags=["home", "popular_games"],
    )

    chunks += make_chunks(
        chunk_id_prefix="home-studio-rules",
        title="Home - Regulation for Using the Esports Studio",
        source_url=source_url,
        category="rules",
        section=section,
        lines=slice_lines(lines, "Regulation for Using", "Related agencies"),
        tags=["home", "rules"],
    )

    chunks += make_chunks(
        chunk_id_prefix="home-contact-agencies",
        title="Home - Related Agencies and Contact",
        source_url=source_url,
        category="contact",
        section=section,
        lines=slice_lines(lines, "Related agencies"),
        tags=["home", "contact", "agency"],
    )
    return chunks


def build_reservation_chunks(page: str) -> list[dict]:
    section = "Reservation"
    source_url = extract_source_url(page)
    lines = clean_lines(page, keep_footer=True)
    chunks: list[dict] = []

    blocks = [
        ("reservation-intro-schedule", "Reservation - Service Schedule", "Gaming Equipment Schedule", "Rules and Regulations", "reservation", ["schedule", "opening_hours"]),
        ("reservation-booking-rules", "Reservation - Booking Rules", "1. การจองการใช้บริการ", "2. การเช็คอิน", "reservation", ["booking_rules"]),
        ("reservation-checkin", "Reservation - Check-in Rules", "2. การเช็คอิน", "3. การยกเลิก", "reservation", ["checkin"]),
        ("reservation-cancel-change", "Reservation - Cancellation and Time Change", "3. การยกเลิก", "4. ระเบียบ", "reservation", ["cancellation", "time_change"]),
        ("reservation-studio-rules", "Reservation - Studio Rules", "4. ระเบียบ", "5. การลงโทษ", "rules", ["studio_rules"]),
        ("reservation-penalty", "Reservation - Penalties for Rule Violations", "5. การลงโทษ", "6. ข้อกำหนดเพิ่มเติม", "penalty", ["penalty"]),
        ("reservation-additional-terms", "Reservation - Additional Terms", "6. ข้อกำหนดเพิ่มเติม", "How to Use", "rules", ["terms"]),
        ("reservation-howto", "Reservation - How to Use Booking System", "How to Use", "Bank Account", "reservation", ["how_to", "booking_steps"]),
        ("reservation-bank-account", "Reservation - Bank Account", "Bank Account", "Make a Reservation", "reservation", ["payment", "bank_account"]),
        ("reservation-service-list", "Reservation - Service List", "Select a service", "Book an appointment on", "services", ["services", "duration"]),
        ("reservation-contact", "Reservation - Contact", "Contact Us", "Website Security Policy", "contact", ["contact"]),
    ]
    for prefix, title, start, end, category, tags in blocks:
        chunks += make_chunks(
            chunk_id_prefix=prefix,
            title=title,
            source_url=source_url,
            category=category,
            section=section,
            lines=slice_lines(lines, start, end),
            tags=tags,
        )

    service_lines = slice_lines(lines, "Select a service", "Book an appointment on")
    service_blocks = [
        ("reservation-service-cockpit", "Reservation - Cockpit Services and Games", "Cockpit #1", "Nintendo Swich", "services", ["cockpit", "games"]),
        ("reservation-service-nintendo", "Reservation - Nintendo Switch Services and Games", "Nintendo Swich", "PC #01", "services", ["nintendo", "games"]),
        ("reservation-service-pc", "Reservation - PC Services and Games", "PC #01", "PlayStation 5 #1", "services", ["pc", "games"]),
        ("reservation-service-ps5", "Reservation - PlayStation 5 Services and Games", "PlayStation 5 #1", "VR Station", "services", ["ps5", "games"]),
        ("reservation-service-vr", "Reservation - VR Station Services and Games", "VR Station", None, "services", ["vr", "games"]),
    ]
    for prefix, title, start, end, category, tags in service_blocks:
        block = slice_lines(service_lines, start, end)
        chunks += make_chunks(
            chunk_id_prefix=prefix,
            title=title,
            source_url=source_url,
            category=category,
            section=section,
            lines=block,
            tags=tags,
        )
    return chunks


def build_events_chunks(page: str, page_idx: int) -> list[dict]:
    section = "Events_and_News"
    source_url = extract_source_url(page)
    title = extract_title(page, "Events and News")
    lines = clean_lines(page)
    chunks: list[dict] = []

    if title.lower() == "news":
        start = line_index(lines, "News")
        body = lines[start + 1 :] if start >= 0 else lines
        current: list[str] = []
        article_idx = 1
        for line in body:
            if DATE_LINE_RE.match(line) and current:
                chunks += make_chunks(
                    chunk_id_prefix=f"events-news-article-{article_idx:03d}",
                    title="News Article",
                    source_url=source_url,
                    category="events_news",
                    section=section,
                    lines=current,
                    tags=["news", "article"],
                )
                article_idx += 1
                current = []
            current.append(line)
        if current:
            chunks += make_chunks(
                chunk_id_prefix=f"events-news-article-{article_idx:03d}",
                title="News Article",
                source_url=source_url,
                category="events_news",
                section=section,
                lines=current,
                tags=["news", "article"],
            )
        return chunks

    return make_chunks(
        chunk_id_prefix=f"events-news-page-{page_idx:02d}",
        title=f"Events and News - {title}",
        source_url=source_url,
        category="events_news",
        section=section,
        lines=lines,
        tags=["events_news", slugify(title)],
    )


def build_about_chunks(page: str, page_idx: int) -> list[dict]:
    section = "About_Us"
    source_url = extract_source_url(page)
    title = extract_title(page, "About Us")
    lines = clean_lines(page, keep_footer=True)

    if title.lower() == "members":
        chunks: list[dict] = []
        chunks += make_chunks(
            chunk_id_prefix="about-members-leadership",
            title="About Us - Members Leadership",
            source_url=source_url,
            category="about_us",
            section=section,
            lines=slice_lines(lines, "ผศ.ดร.นิวัติ", "cooperative education"),
            tags=["members", "leadership"],
        )
        chunks += make_chunks(
            chunk_id_prefix="about-members-interns",
            title="About Us - Cooperative Education and Internship Students",
            source_url=source_url,
            category="about_us",
            section=section,
            lines=slice_lines(lines, "cooperative education", "PSU Phuket Esports Club"),
            tags=["members", "internship"],
        )
        chunks += make_chunks(
            chunk_id_prefix="about-members-club",
            title="About Us - PSU Phuket Esports Club",
            source_url=source_url,
            category="about_us",
            section=section,
            lines=slice_lines(lines, "PSU Phuket Esports Club"),
            tags=["members", "club"],
        )
        return chunks

    return make_chunks(
        chunk_id_prefix=f"about-us-{slugify(title)}-{page_idx:02d}",
        title=f"About Us - {title}",
        source_url=source_url,
        category="about_us",
        section=section,
        lines=lines,
        tags=["about_us", slugify(title)],
    )


def split_services_or_knowledge_page(page: str, section_name: str, page_idx: int) -> list[dict]:
    source_url = extract_source_url(page)
    title = extract_title(page, section_name)
    lines = clean_lines(page)
    category = SECTION_CATEGORY.get(section_name, "general")
    if section_name == "Services" and title.lower() == "our games":
        category = "games"
    elif section_name == "Services":
        category = "services"
    return make_chunks(
        chunk_id_prefix=f"{slugify(section_name)}-{slugify(title)}-{page_idx:02d}",
        title=f"{section_name} - {title}",
        source_url=source_url,
        category=category,
        section=section_name,
        lines=lines,
        tags=[slugify(section_name), slugify(title)],
    )


def build_section_chunks() -> list[dict]:
    chunks: list[dict] = []
    for section_dir in sorted(RAW_SECTIONS_DIR.iterdir()):
        section_file = section_dir / "section_text.txt"
        if not section_file.exists():
            continue
        section_name = section_dir.name
        raw_text = section_file.read_text(encoding="utf-8", errors="replace")
        pages = split_pages(normalize_text(raw_text))
        for page_idx, page in enumerate(pages, 1):
            if section_name == "Home":
                chunks.extend(build_home_chunks(page))
            elif section_name == "Reservation":
                chunks.extend(build_reservation_chunks(page))
            elif section_name == "Events_and_News":
                chunks.extend(build_events_chunks(page, page_idx))
            elif section_name == "About_Us":
                chunks.extend(build_about_chunks(page, page_idx))
            else:
                chunks.extend(split_services_or_knowledge_page(page, section_name, page_idx))
    return chunks


def curated_fact_paths() -> list[Path]:
    paths = sorted(CURATED_DIR.glob("curated_facts*.jsonl"))
    return [path for path in paths if path.is_file()]


def load_curated_chunks() -> list[dict]:
    chunks: list[dict] = []
    for path in curated_fact_paths():
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            fact = json.loads(line)
            text = normalize_text(f"{fact.get('title', '')}\n{fact.get('text', '')}")
            category = fact.get("category", "curated")
            chunks.append(
                {
                    "id": fact["id"],
                    "source_type": "curated_fact",
                    "source_url": fact.get("source_url", ""),
                    "title": fact.get("title", fact["id"]),
                    "category": category,
                    "section": "curated",
                    "chunk_index": len(chunks),
                    "priority": int(fact.get("priority", SECTION_PRIORITY.get(category, 10)) or 10),
                    "tags": fact.get("tags", []),
                    "text": text,
                    "char_count": len(text),
                    "thai_chars": count_thai(text),
                    "mojibake_score": mojibake_score(text),
                    "curated_file": path.name,
                    "source_ids": fact.get("source_ids", []),
                }
            )
    return chunks


def dedupe_chunks(chunks: list[dict]) -> list[dict]:
    seen_ids: set[str] = set()
    seen_texts: set[str] = set()
    deduped: list[dict] = []
    for chunk in chunks:
        chunk_id = chunk["id"]
        if chunk_id in seen_ids:
            suffix = 2
            base_id = chunk_id
            while f"{base_id}-{suffix}" in seen_ids:
                suffix += 1
            chunk["id"] = f"{base_id}-{suffix}"
        seen_ids.add(chunk["id"])

        key = re.sub(r"\s+", " ", chunk["text"].lower()).strip()[:800]
        if key in seen_texts:
            continue
        seen_texts.add(key)
        deduped.append(chunk)
    return deduped


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    section_chunks = build_section_chunks()
    curated_chunks = load_curated_chunks()
    all_chunks = dedupe_chunks(curated_chunks + section_chunks)

    with OUTPUT_PATH.open("w", encoding="utf-8") as f:
        for chunk in all_chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")

    lengths = [len(chunk["text"]) for chunk in all_chunks]
    manifest = {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "output_path": str(OUTPUT_PATH),
        "raw_sections_dir": str(RAW_SECTIONS_DIR),
        "curated_fact_paths": [str(path) for path in curated_fact_paths()],
        "total_chunks": len(all_chunks),
        "curated_chunks": len(curated_chunks),
        "web_chunks": len(section_chunks),
        "deduped_removed": len(curated_chunks) + len(section_chunks) - len(all_chunks),
        "category_counts": dict(sorted(Counter(chunk["category"] for chunk in all_chunks).items())),
        "source_type_counts": dict(sorted(Counter(chunk["source_type"] for chunk in all_chunks).items())),
        "section_counts": dict(sorted(Counter(chunk["section"] for chunk in all_chunks).items())),
        "max_chars_target": MAX_CHARS,
        "hard_max_chars": HARD_MAX_CHARS,
        "max_actual_chars": max(lengths) if lengths else 0,
        "chunks_over_900": sum(1 for length in lengths if length > 900),
        "chunks_over_1200": sum(1 for length in lengths if length > 1200),
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
