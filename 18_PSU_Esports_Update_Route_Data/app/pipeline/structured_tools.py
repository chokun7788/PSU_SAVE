from __future__ import annotations

import json
import re
import time
import unicodedata
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any

from app.calculator.service_fee import answer_service_fee
from app.core.normalization import contains_alias, normalize_text
from app.core.source_registry import (
    SERVICE_FEE_IMAGE_2026_ID,
    make_source_hits,
)
from app.pipeline.entity_resolver import resolve_game_entity
from app.pipeline.query_signals import looks_like_game_zone_ranking_query
from app.pipeline.schemas import PipelineRoute, UniversalIntent


ROOT = Path(__file__).resolve().parents[2]
CURATED_DIR = ROOT / "data" / "curated"

MEMBERS_URL = "https://esports.phuket.psu.ac.th/about-us/Members"
OUR_GAMES_URL = "https://esports.phuket.psu.ac.th/Services/our-games"
HOME_URL = "https://esports.phuket.psu.ac.th/home"
RESERVATION_URL = "https://esports.computing.psu.ac.th/"

MEMBER_GROUP_ORDER = (
    "Members",
    "cooperative education and Internship student",
    "PSU Phuket Esports Club - PSU Phuket",
)

ZONE_ALIASES = {
    "PC Zone": ["pc", "pc zone", "คอม", "คอมพิวเตอร์"],
    "PlayStation 5 Zone": ["ps5", "playstation", "playstation 5", "เพลย์", "เพลย์ห้า"],
    "Nintendo Switch Zone": ["nintendo", "switch", "nintendo switch", "นินเทนโด", "สวิตช์", "สวิทช์"],
    "Cockpit Zone": ["cockpit", "คอกพิท", "ค็อกพิท", "พวงมาลัย", "ขับรถ"],
    "VR Zone": ["vr", "วีอาร์", "แว่น", "แว่น vr"],
}


@dataclass(frozen=True)
class StructuredToolResult:
    answer: str
    hits: list[dict[str, Any]]
    mode: str
    confidence: float
    evidence: dict[str, Any] = field(default_factory=dict)


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


@lru_cache(maxsize=1)
def _equipment_rows() -> tuple[dict[str, Any], ...]:
    return tuple(_read_jsonl(CURATED_DIR / "equipment_item_details.jsonl"))


@lru_cache(maxsize=1)
def _equipment_alias_entries() -> tuple[tuple[dict[str, Any], str, frozenset[str]], ...]:
    entries: list[tuple[dict[str, Any], str, frozenset[str]]] = []
    for row in _equipment_rows():
        aliases = [
            str(row.get("item") or ""),
            str(row.get("what_th") or ""),
            str(row.get("zone") or ""),
            *(str(item) for item in (row.get("use_cases_th") or [])),
        ]
        for alias in aliases:
            alias_compact = _compact(alias)
            if len(alias_compact) < 3:
                continue
            alias_tokens = frozenset(
                token
                for token in re.findall(r"[0-9a-z+.-]+|[\u0E00-\u0E7F]+", normalize_text(alias))
                if len(_compact(token)) >= 3 and token not in {"zone", "gaming", "เล่น", "สำหรับ", "อุปกรณ์"}
            )
            entries.append((row, alias_compact, alias_tokens))
    return tuple(entries)


def _hit(source_id: str, category: str, source_url: str, title: str | None = None) -> dict[str, Any]:
    source_type = "control_game" if category == "game_controls" else category
    return {
        "id": source_id,
        "metadata": {
            "source_url": source_url,
            "category": category,
            "source_type": source_type,
            "title": title or source_id,
            "source_ids": [source_id],
        },
    }


def _dedupe_hits(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    unique: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for row in rows:
        metadata = row.get("metadata", {}) if isinstance(row, dict) else {}
        key = (str(row.get("id", "")), str(metadata.get("source_url", "")))
        if key in seen:
            continue
        seen.add(key)
        unique.append(row)
    return unique


def _source_hits_from_service_fee_result(result: dict[str, Any]) -> list[dict[str, Any]]:
    source_ids = result.get("source_ids")
    if isinstance(source_ids, list) and source_ids:
        return make_source_hits([str(source_id) for source_id in source_ids])
    source_url = str(result.get("source_url") or "")
    if source_url:
        return [_hit(SERVICE_FEE_IMAGE_2026_ID, "service_fee", source_url, "Service Fee 2026")]
    return []


def _compact(value: str) -> str:
    return re.sub(r"[^0-9a-z\u0E00-\u0E7F]+", "", normalize_text(value or ""))


def _game_key(value: str) -> str:
    clean = (value or "").replace("™", "").replace("®", "")
    clean = unicodedata.normalize("NFKD", clean).encode("ascii", "ignore").decode("ascii")
    clean = re.sub(r"\bstandard edition\b", "", clean, flags=re.IGNORECASE)
    clean = re.sub(r"\(\s*remake\s*\)", "", clean, flags=re.IGNORECASE)
    clean = re.sub(r"\bremake\b", "", clean, flags=re.IGNORECASE)
    clean = re.sub(r"\(\s*remastered\s*\)", "", clean, flags=re.IGNORECASE)
    clean = re.sub(r"\bremastered\b", "", clean, flags=re.IGNORECASE)
    return _compact(clean)


def _normalize_game_title_roman_typos(value: str) -> str:
    clean = value or ""
    clean = re.sub(r"\bpart\s+(?:oi|0i|ll|2)\b", "Part II", clean, flags=re.IGNORECASE)
    clean = re.sub(r"\bpart\s+1\b", "Part I", clean, flags=re.IGNORECASE)
    return clean


def _has(q: str, *terms: str) -> bool:
    q_norm = normalize_text(q)
    return any(normalize_text(term) in q_norm for term in terms)


def _has_normalized(q_norm: str, *terms: str) -> bool:
    return any(str(term).strip().lower() in q_norm for term in terms if str(term).strip())


def _looks_like_specific_game_detail_query(query: str) -> bool:
    """True when "game what" asks about one detected title, not the whole catalog."""
    q = normalize_text(query)
    if _has(q, "มีเกมอะไร", "เกมอะไรบ้าง", "เกมไรบ้าง", "รายชื่อเกม", "เกมทั้งหมด", "เล่นเกมอะไรได้บ้าง"):
        return False
    return _has(q, "คือเกมอะไร", "อะไรคือเกม", "คืออะไร", "แนวอะไร", "แนวไหน", "เป็นเกมแนวไหน", "เกี่ยวกับอะไร")


def _looks_like_game_info_query(query: str) -> bool:
    q = normalize_text(query)
    if _has(q, "มีเกมอะไร", "เกมอะไรบ้าง", "เกมไรบ้าง", "รายชื่อเกม", "เกมทั้งหมด", "เล่นเกมอะไรได้บ้าง"):
        return False
    return _has(q, "มีข้อมูลไหม", "มีข้อมูล", "มีไหม", "มีในร้านไหม", "เล่นได้ไหม", "เล่นได้รึเปล่า")


def _looks_like_competition_rule_query(query: str) -> bool:
    q = normalize_text(query)
    return _has(
        q,
        "รอบชิง",
        "รอบรอง",
        "รอบแบ่งกลุ่ม",
        "กติกา",
        "แข่ง",
        "แข่งขัน",
        "ทัวร์",
        "tournament",
        "bo1",
        "bo3",
        "best of",
        "ทีมละ",
        "แบน",
        "ban",
        "เลือกตัว",
        "format",
    )


def _looks_like_booking_selection_query(query: str) -> bool:
    q = normalize_text(query)
    if _looks_like_play_access_query(q):
        return True
    return _has(
        q,
        "จอง",
        "booking",
        "book",
        "เลือกบริการ",
        "ต้องเลือก",
        "ต้องระบุ",
        "จำนวนผู้เล่น",
        "ผู้เล่น",
        "รอบเวลา",
        "เลือกอะไร",
        "จองโซน",
        "ต้องจอง",
    )


def _looks_like_play_access_query(query: str) -> bool:
    q = normalize_text(query)
    if _has(q, "ปุ่ม", "กดอะไร", "controller", "controls", "ใช้จอย"):
        return False
    if _has(q, "เล่นยังไง", "เล่นอย่างไร", "วิธีเล่น", "สอนเล่น"):
        return False
    has_play_access_signal = _has(
        q,
        "จะเล่น",
        "ถ้าจะเล่น",
        "เข้าเล่น",
        "ไปเล่น",
        "อยากเล่น",
        "เล่นต้องทำ",
        "เล่น ต้องทำ",
        "ต้องการเล่น",
    )
    has_how_to_action = _has(
        q,
        "ต้องทำไง",
        "ต้องทำยังไง",
        "ต้องทำอย่างไร",
        "ทำไง",
        "ทำยังไง",
        "ทำอย่างไร",
        "ต้องจอง",
        "จองยังไง",
    )
    return has_play_access_signal and has_how_to_action


def _looks_like_control_or_gameplay_query(query: str) -> bool:
    return _has(
        query,
        "ปุ่ม",
        "กดอะไร",
        "controller",
        "controls",
        "ใช้จอย",
        "เล่นยังไง",
        "เล่นอย่างไร",
        "วิธีเล่น",
        "สอนเล่น",
    )


def _looks_like_explicit_control_query(query: str) -> bool:
    return _has(
        query,
        "ปุ่ม",
        "กดอะไร",
        "กดปุ่มไหน",
        "ปุ่มอะไร",
        "ควบคุม",
        "controller",
        "control",
        "controls",
        "button",
        "buttons",
        "จอย",
        "ใช้จอย",
    )


@lru_cache(maxsize=1)
def _member_rows() -> tuple[dict[str, Any], ...]:
    return tuple(_read_jsonl(CURATED_DIR / "member_profiles.jsonl"))


@lru_cache(maxsize=1)
def _game_rows() -> tuple[dict[str, Any], ...]:
    rows: dict[str, dict[str, Any]] = {}
    for path in (CURATED_DIR / "game_item_details.jsonl", CURATED_DIR / "our_games_scraped_details.jsonl"):
        for row in _read_jsonl(path):
            game = str(row.get("game") or row.get("title") or "").strip()
            if not game:
                continue
            key = _game_key(game)
            current = rows.setdefault(key, {"game": game, "aliases": set(), "zones": set()})
            current["summary_th"] = current.get("summary_th") or row.get("summary_th") or row.get("text") or ""
            current["how_to_play_th"] = current.get("how_to_play_th") or row.get("how_to_play_th") or ""
            current["genre"] = current.get("genre") or row.get("genre") or ""
            current["source_url"] = current.get("source_url") or row.get("source_url") or OUR_GAMES_URL
            for alias in row.get("aliases") or []:
                if alias:
                    current["aliases"].add(str(alias))
            current["aliases"].add(game)
            for zone in row.get("zones") or []:
                current["zones"].add(str(zone))
            listed_under = str(row.get("listed_under") or "").strip()
            if listed_under:
                current["zones"].add(_canonical_zone_label(listed_under))

    for path in (CURATED_DIR / "game_title_aliases.jsonl", CURATED_DIR / "game_control_facts.jsonl"):
        for row in _read_jsonl(path):
            game = str(row.get("game") or "").strip()
            if not game:
                continue
            key = _game_key(game)
            current = rows.setdefault(key, {"game": game, "aliases": set(), "zones": set()})
            current["source_url"] = current.get("source_url") or row.get("source_url") or OUR_GAMES_URL
            current["aliases"].add(game)
            if path.name != "game_control_facts.jsonl":
                for alias in row.get("aliases") or []:
                    if alias:
                        current["aliases"].add(str(alias))
            platform_key = str(row.get("platform_key") or "").strip()
            if platform_key == "nintendo":
                current["zones"].add("Nintendo Switch Zone")
            elif platform_key == "ps5":
                current["zones"].add("PlayStation 5 Zone")
            elif platform_key == "pc":
                current["zones"].add("PC Zone")
            elif platform_key == "vr":
                current["zones"].add("VR Zone")

    output: list[dict[str, Any]] = []
    for row in rows.values():
        output.append({
            **row,
            "aliases": sorted(row["aliases"]),
            "zones": sorted(zone for zone in row["zones"] if zone),
        })
    output.sort(key=lambda item: str(item["game"]).lower())
    return tuple(output)


@lru_cache(maxsize=1)
def _game_alias_entries() -> tuple[tuple[str, str, int, dict[str, Any]], ...]:
    entries: list[tuple[str, str, int, dict[str, Any]]] = []
    for row in _current_game_rows():
        for alias in row.get("aliases") or []:
            alias_norm = normalize_text(str(alias))
            alias_compact = _compact(str(alias))
            if alias_norm and len(alias_compact) >= 3:
                entries.append((alias_norm, alias_compact, len(alias_compact), row))
    entries.sort(key=lambda item: item[2], reverse=True)
    return tuple(entries)


@lru_cache(maxsize=1)
def _control_rows() -> tuple[dict[str, Any], ...]:
    return tuple(
        row for row in _read_jsonl(CURATED_DIR / "game_control_facts.jsonl")
        if row.get("category") == "game_controls" and row.get("button")
    )


@lru_cache(maxsize=1)
def _service_game_availability_rows() -> tuple[dict[str, Any], ...]:
    return tuple(_read_jsonl(CURATED_DIR / "service_game_availability.jsonl"))


def _current_game_rows() -> tuple[dict[str, Any], ...]:
    availability_rows = _service_game_availability_rows()
    if not availability_rows:
        return _game_rows()

    existing_by_key = {_game_key(str(row.get("game") or "")): row for row in _game_rows()}
    current: dict[str, dict[str, Any]] = {}
    for service in availability_rows:
        zone = str(service.get("zone") or "").strip()
        source_url = str(service.get("source_url") or OUR_GAMES_URL)
        for game in service.get("games") or []:
            title = str(game).strip()
            if not title:
                continue
            key = _game_key(title)
            base = existing_by_key.get(key, {})
            aliases = set(base.get("aliases") or [title])
            if normalize_text(title).startswith("call of duty"):
                aliases = {
                    alias for alias in aliases
                    if _compact(str(alias)) not in {"callofduty", "cod", "คอลออฟ", "ดิวตี้", "ดูตี้"}
                }
            row = current.setdefault(
                key,
                {
                    "game": title,
                    "aliases": aliases,
                    "zones": set(),
                    "summary_th": base.get("summary_th") or "",
                    "how_to_play_th": base.get("how_to_play_th") or "",
                    "genre": base.get("genre") or "",
                    "source_url": base.get("source_url") or source_url,
                },
            )
            row["aliases"].add(title)
            row["zones"].add(zone)
            row["source_url"] = row.get("source_url") or source_url

    output: list[dict[str, Any]] = []
    for row in current.values():
        output.append({
            **row,
            "aliases": sorted(row["aliases"]),
            "zones": sorted(zone for zone in row["zones"] if zone),
        })
    output.sort(key=lambda item: str(item["game"]).lower())
    return tuple(output)


def _current_game_keys() -> set[str]:
    return {_game_key(str(row.get("game") or "")) for row in _current_game_rows()}


def _non_current_control_game_answer(query: str) -> StructuredToolResult | None:
    q = normalize_text(query)
    known_games = {
        "Mario Kart Live: Home Circuit": (
            "mario kart live",
            "home circuit",
            "mk live",
            "มาริโอคาร์ทไลฟ์",
            "มาริโอคาทไลฟ์",
        ),
    }
    for game_name, aliases in known_games.items():
        if _game_key(game_name) in _current_game_keys():
            continue
        if _has(q, *aliases) or contains_alias(q, list(aliases), fuzzy=True, threshold=0.90)[0]:
            current_mario = [
                str(row.get("game"))
                for row in _current_game_rows()
                if "mario" in normalize_text(str(row.get("game") or ""))
            ]
            suffix = ""
            if current_mario:
                suffix = "\nเกมตระกูล Mario ที่อยู่ในรายการปัจจุบันคือ: " + ", ".join(current_mario)
            answer = (
                f"ตอนนี้ยังไม่พบ {game_name} ในรายการเกมปัจจุบันของ PSU Esports Studio - Phuket ครับ\n"
                "จึงไม่ดึงปุ่มของเกมอื่น เช่น Mario Kart 8 Deluxe มาตอบแทน"
                f"{suffix}\n"
                f"แหล่งข้อมูล: {RESERVATION_URL}"
            )
            return StructuredToolResult(
                answer,
                [_hit("service_game_availability", "games", RESERVATION_URL, "Current service game availability")],
                "structured_game_controls_no_current_game",
                0.93,
                {"tool": "current_game_availability_guard", "game": game_name},
            )
    return None


def _machine_numbers_from_query(query: str) -> list[int]:
    q = normalize_text(query)
    numbers: list[int] = []
    for start, end in re.findall(r"(?:#|เครื่อง|pc)\s*0?(\d{1,2})\s*[-–]\s*(?:#|เครื่อง|pc)?\s*0?(\d{1,2})", q):
        low, high = int(start), int(end)
        for number in range(min(low, high), max(low, high) + 1):
            if 1 <= number <= 99:
                numbers.append(number)
    for number in re.findall(r"(?:#|เครื่อง|pc)\s*0?(\d{1,2})", q):
        value = int(number)
        if 1 <= value <= 99:
            numbers.append(value)
    return list(dict.fromkeys(numbers))


def _service_matches_zone(service: dict[str, Any], zone: str | None) -> bool:
    return zone is None or _canonical_zone_label(str(service.get("zone") or "")) == zone


def _service_matches_duration(service: dict[str, Any], q: str) -> bool:
    if "vr" not in normalize_text(str(service.get("service_label") or "")):
        return True
    minutes = service.get("duration_minutes")
    if _has(q, "30 นาที", "ครึ่งชั่วโมง", "half hour", "30 min"):
        return minutes == 30
    if _has(q, "1 ชั่วโมง", "หนึ่งชั่วโมง", "60 นาที", "1 hr", "1 hour"):
        return minutes == 60
    return True


def _service_matches_people(service: dict[str, Any], q: str) -> bool:
    if "nintendo switch" not in normalize_text(str(service.get("service_label") or "")):
        return True
    people_match = re.search(r"(\d+)\s*(?:คน|persons?|players?)", q)
    if not people_match:
        return True
    people = int(people_match.group(1))
    capacity = str(service.get("capacity_persons") or "")
    if people >= 3:
        return "1-4" in capacity or "3-4" in capacity
    return "1-2" in capacity


def _service_matches_machine(service: dict[str, Any], numbers: list[int]) -> bool:
    if not numbers:
        return True
    machine_numbers = [int(value) for value in service.get("machine_numbers") or []]
    return any(number in machine_numbers for number in numbers)


def _availability_source_hits(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    hits: list[dict[str, Any]] = []
    for row in rows:
        hits.append(_hit(str(row.get("id") or "service_game_availability"), "games", str(row.get("source_url") or RESERVATION_URL), str(row.get("service_label") or "Service game availability")))
    return _dedupe_hits(hits)


def _format_service_availability(rows: list[dict[str, Any]], intro: str) -> str:
    lines = [intro]
    for row in rows:
        lines.append("")
        lines.append(f"{row.get('service_label')} ({row.get('duration_minutes')} นาที, {row.get('capacity_persons')})")
        for game in row.get("games") or []:
            lines.append(f"•    {game}")
        notes = [str(note) for note in row.get("notes") or [] if note]
        for note in notes[:2]:
            lines.append(f"หมายเหตุ: {note}")
    lines.append(f"แหล่งข้อมูล: {RESERVATION_URL}")
    return "\n".join(lines)


def _looks_like_service_capacity_query(query: str) -> bool:
    q = normalize_text(query)
    return _has(
        q,
        "เล่นได้กี่คน",
        "รองรับกี่คน",
        "รับได้กี่คน",
        "นั่งได้กี่คน",
        "ได้กี่คน",
        "กี่คน",
        "กี่ player",
        "กี่ players",
        "กี่ person",
        "กี่ persons",
        "จำนวนผู้เล่น",
    )


def _looks_like_game_presence_or_location_query(query: str) -> bool:
    q = normalize_text(query)
    return _has(
        q,
        "มีไหม",
        "มีมั้ย",
        "เล่นได้ไหม",
        "เล่นได้มั้ย",
        "เครื่องไหน",
        "อยู่เครื่องไหน",
        "โซนไหน",
        "อยู่โซนไหน",
        "อยู่ที่ไหน",
        "เล่นได้ที่ไหน",
        "มีที่ไหน",
    ) or (
        _has(q, "มี", "เล่นได้")
        and _has(q, "ไหม", "มั้ย", "หรือเปล่า", "รึเปล่า", "ปะ")
    )


def _looks_like_specific_calendar_query(query: str) -> bool:
    q = normalize_text(query)
    if re.search(r"\b\d{1,2}[/-]\d{1,2}(?:[/-]\d{2,4})?\b", q):
        return True
    if re.search(r"(?:อีก|หลังจากนี้)\s*\d{1,4}\s*(?:วัน|สัปดาห์|อาทิตย์)|\d{1,4}\s*วัน(?:ข้างหน้า|ถัดไป|ก่อน)", q):
        return True
    return _has(
        q,
        "วันนี้",
        "พรุ่งนี้",
        "มะรืน",
        "วันหยุด",
        "ปฏิทิน",
        "เดือนนี้",
        "เดือนหน้า",
        "เดือนที่แล้ว",
        "เดือนก่อน",
        "ปีนี้",
        "ปีหน้า",
        "ปีที่แล้ว",
        "ปีก่อน",
        "มกราคม",
        "มกรา",
        "กุมภาพันธ์",
        "กุมภา",
        "มีนาคม",
        "มีนา",
        "เมษายน",
        "เมษา",
        "พฤษภาคม",
        "พฤษภา",
        "มิถุนายน",
        "มิถุนา",
        "กรกฎาคม",
        "กรกฎา",
        "ก.ค.",
        "กค",
        "สิงหาคม",
        "สิงหา",
        "กันยายน",
        "กันยา",
        "ตุลาคม",
        "ตุลา",
        "พฤศจิกายน",
        "พฤศจิกา",
        "ธันวาคม",
        "ธันวา",
    )


def _looks_like_known_unsupported_game_query(query: str) -> bool:
    return _has(
        query,
        "minecraft",
        "มายคราฟ",
        "ไมน์คราฟต์",
        "ไมน์คราฟ",
        "roblox",
        "โรบล็อก",
        "โรบอก",
    )


def _format_service_capacity(rows: list[dict[str, Any]]) -> str:
    lines = ["บริการที่ถามรองรับผู้เล่นตามข้อมูลนี้ครับ"]
    for row in rows:
        lines.append(f"•    {row.get('service_label')}: {row.get('capacity_persons')} ต่อรอบ {row.get('duration_minutes')} นาที")
    lines.append(f"แหล่งข้อมูล: {RESERVATION_URL}")
    return "\n".join(lines)


def _service_labels(rows: list[dict[str, Any]]) -> str:
    return ", ".join(str(row.get("service_label")) for row in rows if row.get("service_label"))


def _format_service_game_no_match(
    game_name: str,
    requested_rows: list[dict[str, Any]],
    available_rows: list[dict[str, Any]],
) -> str:
    requested_label = _service_labels(requested_rows) or "บริการ/เครื่องที่ถาม"
    lines = [f"{requested_label} ไม่มี {game_name} ครับ"]
    if available_rows:
        lines.append(f"{game_name} เล่นได้ที่ {_service_labels(available_rows)}")
    if requested_rows:
        lines.append("")
        lines.append(f"เกมที่มีใน {requested_label}:")
        for row in requested_rows:
            for game in row.get("games") or []:
                lines.append(f"•    {game}")
    lines.append(f"แหล่งข้อมูล: {RESERVATION_URL}")
    return "\n".join(lines)


def _service_game_availability_answer(query: str, intent: UniversalIntent) -> StructuredToolResult | None:
    rows = list(_service_game_availability_rows())
    if not rows:
        return None
    q = normalize_text(query)
    if _looks_like_known_unsupported_game_query(q):
        return None
    zone = _detect_zone(query, intent.target)
    numbers = _machine_numbers_from_query(query)
    machine_related = bool(numbers) or _has(q, "เครื่องไหน", "อยู่เครื่องไหน", "เครื่องอะไร", "#")
    service_scope_related = bool(zone) or machine_related or _has(q, "โซน", "zone", "บริการ", "แต่ละเครื่อง", "แต่ละโซน", "ตามเครื่อง", "ตามโซน")
    if _has(q, "กี่ชั่วโมง", "ชั่วโมงต่อวัน", "เล่นกี่ชั่วโมง", "session", "sessions") and not _has(q, "กี่เกม", "จำนวนเกม"):
        return None
    explicit_game_catalog_terms = _has(q, "มีเกม", "เกมอะไร", "กี่เกม", "รายชื่อเกม", "รายการเกม", "เกมทั้งหมด")
    catalog_related = explicit_game_catalog_terms or (intent.domain == "games" and intent.operation in {"count", "list"})
    if _looks_like_specific_game_detail_query(query) or _has(q, "แนวอะไร", "แนวไหน", "เป็นเกมแนวไหน", "คือเกมอะไร", "คืออะไร"):
        catalog_related = False
    if catalog_related and not service_scope_related:
        return None
    wants_game_location = _looks_like_game_presence_or_location_query(q)
    booking_selection = _looks_like_booking_selection_query(query)
    # A service catalog request has no game target. Scanning every fuzzy title
    # here adds seconds and can mistake ordinary request words for a game name.
    should_detect_game = wants_game_location or booking_selection
    allow_fuzzy_game = wants_game_location or (
        booking_selection and _has(q, "เกม", "game")
    )
    game = _detect_game(query, intent.target, allow_fuzzy=allow_fuzzy_game) if should_detect_game else None
    game_key = _game_key(str(game.get("game") or "")) if game else ""
    game_related = bool(game and wants_game_location)
    capacity_related = _looks_like_service_capacity_query(query)
    if capacity_related and not service_scope_related:
        return None
    service_detail_related = catalog_related or machine_related or game_related or capacity_related
    if not service_detail_related:
        return None

    selected = [
        row for row in rows
        if _service_matches_zone(row, zone)
        and _service_matches_duration(row, q)
        and _service_matches_people(row, q)
        and _service_matches_machine(row, numbers)
    ]
    base_selected = list(selected)

    if capacity_related and not game_related and selected:
        return StructuredToolResult(
            _format_service_capacity(selected),
            _availability_source_hits(selected),
            "structured_service_capacity",
            0.97,
            {"tool": "get_service_capacity", "zone": zone or "all", "services": [row.get("id") for row in selected]},
        )

    if game_key:
        selected = [
            row for row in selected
            if any(_game_key(str(item)) == game_key for item in row.get("games") or [])
        ]
        if selected:
            service_displays: list[str] = []
            for row in selected:
                service = str(row.get("service_label") or row.get("machine_label") or row.get("zone") or "").strip()
                zone_label = str(row.get("zone") or "").strip()
                display = service
                if zone_label and zone_label.lower() not in service.lower():
                    display = f"{zone_label} - {service}"
                if display and display not in service_displays:
                    service_displays.append(display)
            services = ", ".join(service_displays)
            answer = (
                f"ได้ครับ {game.get('game')} เล่นได้ที่ {services}\n"
                f"แหล่งข้อมูล: {RESERVATION_URL}"
            )
            return StructuredToolResult(
                answer,
                _availability_source_hits(selected),
                "structured_service_game_availability",
                0.97,
                {"tool": "get_service_game_availability", "game": game.get("game"), "services": [row.get("id") for row in selected]},
            )
        if game_related:
            same_zone_available = [
                row for row in rows
                if (not zone or _service_matches_zone(row, zone))
                and any(_game_key(str(item)) == game_key for item in row.get("games") or [])
            ]
            available_rows = same_zone_available or [
                row for row in rows
                if any(_game_key(str(item)) == game_key for item in row.get("games") or [])
            ]
            return StructuredToolResult(
                _format_service_game_no_match(str(game.get("game") or ""), base_selected, available_rows),
                _availability_source_hits([*base_selected, *available_rows]),
                "structured_service_game_availability_no_match",
                0.91,
                {
                    "tool": "get_service_game_availability",
                    "game": game.get("game"),
                    "matched": False,
                    "requested_services": [row.get("id") for row in base_selected],
                    "available_services": [row.get("id") for row in available_rows],
                },
            )

    if not selected:
        return None
    if zone == "PC Zone" and not numbers and catalog_related:
        selected = [row for row in rows if row.get("id") in {"availability_pc_01_02", "availability_pc_03_10"}]
        intro = "PC Zone แยกรายการเกมตามเลขเครื่องดังนี้"
    elif zone == "VR Zone" and not _has(q, "30 นาที", "ครึ่งชั่วโมง", "1 ชั่วโมง", "60 นาที"):
        selected = [row for row in rows if row.get("id") == "availability_vr_30"]
        intro = "VR Station มีเกมที่ยืนยันได้ดังนี้ (รอบ 30 นาทีและ 1 ชั่วโมงใช้รายการเกมเดียวกัน)"
    else:
        label = zone or "บริการที่ถาม"
        if intent.operation == "count" or _has(q, "กี่เกม", "จำนวนเกม"):
            unique_games = {str(game) for row in selected for game in row.get("games") or []}
            intro = f"{label} มีเกมที่ยืนยันได้ {len(unique_games)} เกมครับ"
        else:
            intro = f"{label} มีเกมที่ยืนยันได้ดังนี้"
    return StructuredToolResult(
        _format_service_availability(selected, intro),
        _availability_source_hits(selected),
        "structured_service_game_availability",
        0.97,
        {"tool": "get_service_game_availability", "zone": zone or "all", "services": [row.get("id") for row in selected]},
    )


def _canonical_zone_label(value: str) -> str:
    q = normalize_text(value)
    if "playstation" in q or "ps5" in q:
        return "PlayStation 5 Zone"
    if "nintendo" in q or "switch" in q:
        return "Nintendo Switch Zone"
    if "cockpit" in q or "คอกพิท" in q or "ค็อกพิท" in q:
        return "Cockpit Zone"
    if "vr" in q:
        return "VR Zone"
    if "pc" in q or "คอม" in q:
        return "PC Zone"
    return value.strip()


def _detect_zone(query: str, target: str = "") -> str | None:
    text = f"{query} {target}".strip()
    for zone, aliases in ZONE_ALIASES.items():
        if contains_alias(text, aliases, fuzzy=True, threshold=0.84)[0]:
            return zone
    return None


def _detect_game(query: str, target: str = "", *, allow_fuzzy: bool = True) -> dict[str, Any] | None:
    text = _normalize_game_title_roman_typos(f"{query} {target}".strip())
    q_norm = normalize_text(text)
    q_compact = _compact(text)
    best: tuple[float, int, dict[str, Any]] | None = None
    for alias_norm, alias_compact, alias_len, row in _game_alias_entries():
        score = 0.0
        if alias_norm and alias_norm in q_norm:
            score = 1.0
        elif alias_compact and len(alias_compact) >= 4 and alias_compact in q_compact:
            score = 0.97
        if score and (best is None or (score, alias_len) > (best[0], best[1])):
            best = (score, alias_len, row)
    if best is not None:
        return best[2]

    if not allow_fuzzy:
        return None

    for alias_norm, _alias_compact, alias_len, row in _game_alias_entries():
        if alias_len < 5:
            continue
        ok, _alias, fuzzy_score = contains_alias(text, [alias_norm], fuzzy=True, threshold=0.90)
        if ok and (best is None or (fuzzy_score, alias_len) > (best[0], best[1])):
            best = (fuzzy_score, alias_len, row)
    return best[2] if best else None


def _detect_equipment_item(query: str, target: str = "") -> dict[str, Any] | None:
    text = f"{query} {target}".strip()
    q_norm = normalize_text(text)
    q_tokens = set(re.findall(r"[0-9a-z+.-]+|[\u0E00-\u0E7F]+", q_norm))
    q_compact = _compact(text)
    direct_id = ""
    if _has_normalized(q_norm, "pc", "คอม", "สเปค", "สเป็ค", "spec"):
        direct_id = "equipment_gaming_pc"
    elif _has_normalized(q_norm, "playstation vr2", "sony playstation vr2", "ps vr2", "psvr2", "vr2", "vr", "วีอาร์", "แว่น"):
        direct_id = "equipment_sony_playstation_vr2"
    elif _has_normalized(q_norm, "ps5", "playstation", "เพลย์ห้า", "เพล5", "เพลย์ 5"):
        direct_id = "equipment_playstation_5_slim"
    elif _has_normalized(q_norm, "cockpit", "ค็อกพิท", "คอกพิท", "พวงมาลัย"):
        direct_id = "equipment_logitech_g923" if _has_normalized(q_norm, "พวงมาลัย", "wheel", "g923", "logitech") else "equipment_racezone_cockpit_v3"
    elif _has_normalized(q_norm, "nintendo", "switch", "นินเทนโด", "สวิตช์", "สวิทช์"):
        direct_id = "equipment_nintendo_switch_oled"
    if direct_id:
        for row in _equipment_rows():
            if str(row.get("id") or "") == direct_id:
                return row

    best: tuple[float, int, dict[str, Any]] | None = None
    for row, alias_compact, _alias_tokens in _equipment_alias_entries():
        if alias_compact in q_compact:
            score = 1.0
            if best is None or (score, len(alias_compact)) > (best[0], best[1]):
                best = (score, len(alias_compact), row)
    if best is not None:
        return best[2]

    for row, _alias_compact, alias_tokens in _equipment_alias_entries():
        overlap = alias_tokens.intersection(q_tokens)
        if overlap and (len(overlap) >= 2 or any(re.search(r"\d", token) for token in overlap)):
            score = min(0.96, 0.70 + 0.09 * len(overlap))
            if best is None or (score, len("".join(overlap))) > (best[0], best[1]):
                best = (score, len("".join(overlap)), row)
    if best is not None:
        return best[2]

    for row, alias_compact, _alias_tokens in _equipment_alias_entries():
        ok, _matched, score = contains_alias(text, [alias_compact], fuzzy=True, threshold=0.84)
        if ok and (best is None or (score, len(alias_compact)) > (best[0], best[1])):
            best = (score, len(alias_compact), row)
    return best[2] if best else None


def _format_home_equipment_catalog(rows: list[dict[str, Any]], zone: str | None = None) -> str | None:
    by_id = {str(row.get("id") or ""): row for row in rows}
    if zone:
        return None
    if not by_id:
        return None
    lines = [
        "อุปกรณ์บนหน้า Home:",
        "PC Zone",
        "• Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)",
        "• Gaming Monitor (จำนวน 10 จอ)",
        "• Gaming Chair (จำนวน 10 ตัว)",
        "• Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset",
        "",
        "Cockpit Zone",
        "• TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)",
        "• Racezone Full Cockpit V3 (จำนวน 2 ชุด)",
        "• Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)",
        "• Pulse Elite Wireless Headset (จำนวน 2 อัน)",
        "",
        "Nintendo Switch Zone",
        "• TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)",
        "• Nintendo Switch OLED (จำนวน 1 เครื่อง)",
        "• Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)",
        "",
        "PlayStation 5 Zone",
        "• PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)",
        "",
        "VR Zone",
        "• PlayStation 5 Slim (จำนวน 1 เครื่อง)",
        "• Sony PlayStation VR2 (จำนวน 1 ชุด)",
        f"แหล่งข้อมูล: {HOME_URL}",
    ]
    expected_ids = {
        "equipment_gaming_pc",
        "equipment_gaming_monitor",
        "equipment_gaming_keyboard",
        "equipment_gaming_mouse",
        "equipment_gaming_headset",
        "equipment_gaming_chair",
        "equipment_logitech_g923",
        "equipment_racezone_cockpit_v3",
        "equipment_nintendo_switch_oled",
        "equipment_playstation_5_slim",
        "equipment_sony_playstation_vr2",
    }
    if not expected_ids.intersection(by_id):
        return None
    return "\n".join(lines)


def _member_grouped(rows: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = {group: [] for group in MEMBER_GROUP_ORDER}
    for row in rows:
        grouped.setdefault(str(row.get("group") or "Members"), []).append(row)
    return grouped


def _member_person_match(query: str, rows: list[dict[str, Any]]) -> dict[str, Any] | None:
    q_key = _compact(query)
    q_norm = normalize_text(query)
    best: tuple[int, int, dict[str, Any]] | None = None
    for row in rows:
        name = str(row.get("name") or "")
        name_key = _compact(name)
        if name_key and name_key in q_key:
            return row
        parts = [part for part in re.split(r"\s+", normalize_text(name)) if len(_compact(part)) >= 4]
        score = sum(1 for part in parts if part and part in q_norm)
        if score:
            rank = (score, len(name_key), row)
            if best is None or rank[:2] > best[:2]:
                best = rank
    return best[2] if best else None


def _member_role_matches(query: str, rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    q_norm = normalize_text(query)
    q_key = _compact(query)
    if not q_key:
        return []
    group_keys = {_compact(group) for group in MEMBER_GROUP_ORDER}
    if any(group_key and group_key in q_key for group_key in group_keys):
        return []

    role_query_signals = (
        "ใคร", "คนไหน", "คนใด", "ตำแหน่ง", "หน้าที่", "เป็น", "ทำ", "รับผิดชอบ",
        "who", "position", "role",
    )
    known_role_signal = any(_compact(str(row.get("role") or "")) in q_key for row in rows if row.get("role"))
    if not (any(term in q_norm for term in role_query_signals) or known_role_signal):
        return []

    scored: list[tuple[int, int, dict[str, Any]]] = []
    chatbot_role_aliases = ("แชทบอท", "chatbot", "chat bot")
    query_tokens = {
        token.lower()
        for token in re.findall(r"[a-z0-9]+", q_norm)
        if len(token) >= 2
    }
    for row in rows:
        role = str(row.get("role") or "").strip()
        if not role:
            continue
        role_norm = normalize_text(role)
        role_key = _compact(role)
        score = 0
        is_chatbot_developer_role = (
            any(alias in q_norm for alias in chatbot_role_aliases)
            and any(term in role_norm for term in ("ai chat bot developer", "chat bot developer", "chatbot developer"))
        )
        if is_chatbot_developer_role:
            score = 100 + len(role_key)
        elif role_key and role_key in q_key:
            score = 100 + len(role_key)
        elif role_norm and role_norm in q_norm:
            score = 95 + len(role_key)
        else:
            role_tokens = {
                token.lower()
                for token in re.findall(r"[a-z0-9]+", role_norm)
                if len(token) >= 2
            }
            overlap = query_tokens.intersection(role_tokens)
            if overlap and (len(overlap) >= 2 or any(token in {"ai", "web", "3d"} for token in overlap)):
                score = 50 + len(overlap) * 8 + len("".join(overlap))
        if score:
            scored.append((score, len(role_key), row))

    if not scored:
        return []
    best_score = max(score for score, _role_len, _row in scored)
    direct_scores = [score for score, _role_len, _row in scored if score >= 100]
    if direct_scores:
        longest_direct_len = max(role_len for score, role_len, _row in scored if score >= 100)
        return [
            row for score, role_len, row in scored
            if score >= 100 and role_len == longest_direct_len
        ]
    return [row for score, _role_len, row in scored if score >= max(50, best_score - 4)]


def _format_member_role_lookup(rows: list[dict[str, Any]]) -> str:
    unique_roles = sorted({str(row.get("role") or "").strip() for row in rows if row.get("role")})
    role_text = unique_roles[0] if len(unique_roles) == 1 else " / ".join(unique_roles)
    lines = [f"ตำแหน่ง {role_text} มี {len(rows)} คนครับ"]
    for row in rows:
        lines.append(_format_member_row(row, include_details=True))
        group = str(row.get("group") or "").strip()
        if group:
            lines.append(f"    ◦ หมวด: {group}")
    lines.append(f"แหล่งข้อมูล: {MEMBERS_URL}")
    return "\n".join(lines)


def _format_member_row(row: dict[str, Any], *, include_details: bool = False) -> str:
    line = f"•    {row.get('name')}: {row.get('role')}"
    if include_details:
        affiliation = str(row.get("affiliation") or "").strip()
        period = str(row.get("period") or "").strip()
        details = [item for item in (affiliation, f"ระยะเวลา: {period}" if period else "") if item]
        if details:
            line += f" ({'; '.join(details)})"
    return line


def _looks_like_member_game_relation_query(query: str) -> bool:
    q = normalize_text(query)
    if _has(q, "ตำแหน่ง", "position", "role"):
        return False
    has_people = _has(
        q,
        "สมาชิก", "member", "members", "staff", "สตาฟ", "เจ้าหน้าที่", "คนดูแล",
        "ทีมงาน", "บุคลากร", "ใคร", "ใครบ้าง",
    )
    has_relation = _has(q, "เล่น", "ดูแล", "รับผิดชอบ", "ประจำ", "คุม")
    has_game_or_zone = _has(
        q,
        "เกม", "game", "games", "ps5", "playstation", "nintendo", "switch",
        "pc", "vr", "cockpit", "โซน", "เครื่อง",
    )
    return has_people and has_relation and has_game_or_zone


def _member_answer(query: str, intent: UniversalIntent) -> StructuredToolResult | None:
    rows = list(_member_rows())
    if not rows:
        return None
    grouped = _member_grouped(rows)
    groups = [(group, grouped.get(group) or []) for group in MEMBER_GROUP_ORDER if grouped.get(group)]
    q = normalize_text(query)

    evidence = {
        "tool": "get_member_groups",
        "source_url": MEMBERS_URL,
        "total_members": len(rows),
        "groups": [{"name": group, "count": len(group_rows)} for group, group_rows in groups],
    }

    if _looks_like_member_game_relation_query(query):
        answer = (
            "ยังไม่พบข้อมูลที่ยืนยันได้ว่าสมาชิกหรือสตาฟแต่ละคนเล่นเกม/ดูแลเกมหรือโซนไหนครับ\n"
            "ข้อมูลที่มีตอนนี้ยืนยันได้เฉพาะรายชื่อสมาชิก หมวด และตำแหน่งในหน้า Members\n"
            f"แหล่งข้อมูล: {MEMBERS_URL}"
        )
        return StructuredToolResult(
            answer,
            [_hit("Members", "members", MEMBERS_URL, "Members")],
            "structured_members_game_relation_no_data",
            0.94,
            {**evidence, "missing_relation": "member_to_game_or_zone"},
        )

    person = _member_person_match(query, rows)
    if person is not None and not _has(q, "กี่หมวด", "กี่กลุ่ม", "หมวดอะไร", "กลุ่มอะไร", "แต่ละหมวด", "แต่ละกลุ่ม"):
        lines = [
            f"{person.get('name')}: {person.get('role')}",
            f"หมวด: {person.get('group') or 'Members'}",
        ]
        affiliation = str(person.get("affiliation") or "").strip()
        period = str(person.get("period") or "").strip()
        if affiliation:
            lines.append(f"สังกัด/รายละเอียด: {affiliation}")
        if period:
            lines.append(f"ระยะเวลา: {period}")
        lines.append(f"แหล่งข้อมูล: {MEMBERS_URL}")
        return StructuredToolResult(
            "\n".join(lines),
            [_hit("Members", "members", MEMBERS_URL, "Members")],
            "structured_members_person_lookup",
            0.98,
            {**evidence, "selected_member": person.get("name")},
        )

    role_matches = _member_role_matches(query, rows)
    if role_matches and not _has(q, "กี่หมวด", "กี่กลุ่ม", "หมวดอะไร", "กลุ่มอะไร", "แต่ละหมวด", "แต่ละกลุ่ม"):
        return StructuredToolResult(
            _format_member_role_lookup(role_matches),
            [_hit("Members", "members", MEMBERS_URL, "Members")],
            "structured_members_role_lookup",
            0.97,
            {
                **evidence,
                "selected_roles": sorted({str(row.get("role") or "") for row in role_matches}),
                "returned_members": len(role_matches),
            },
        )

    if intent.operation in {"group_count", "count"} or _has(q, "กี่หมวด", "กี่กลุ่ม", "หมวดอะไร", "กลุ่มอะไร"):
        lines = [f"สมาชิกในหน้า Members แบ่งเป็น {len(groups)} หมวดครับ"]
        lines.extend(f"•    {group}: {len(group_rows)} คน" for group, group_rows in groups)
        lines.append(f"รวมทั้งหมด {len(rows)} คน")
        lines.append(f"แหล่งข้อมูล: {MEMBERS_URL}")
        return StructuredToolResult(
            "\n".join(lines),
            [_hit("Members", "members", MEMBERS_URL, "Members")],
            "structured_members_group_count",
            0.98,
            evidence,
        )

    group_filter = None
    if _has(q, "สหกิจ", "ฝึกงาน", "intern", "internship", "cooperative"):
        group_filter = "cooperative education and Internship student"
    elif _has(q, "ชมรม", "esports club", "ประธาน", "รองประธาน", "เลขานุการ", "เหรัญญิก", "กรรมการ"):
        group_filter = "PSU Phuket Esports Club - PSU Phuket"
    elif _has(q, "ผู้บริหาร", "อธิการบดี", "คณบดี", "ผู้จัดการ", "นักวิชาการ"):
        group_filter = "Members"

    filtered_groups = [(group, grouped.get(group) or []) for group, _ in groups if group_filter in {None, group}]
    if not filtered_groups:
        return None

    total = sum(len(group_rows) for _group, group_rows in filtered_groups)
    header = (
        f"สมาชิกในหมวด {group_filter}:"
        if group_filter
        else f"สมาชิกจากหน้า Members แยกตามหมวด รวม {total} คน:"
    )
    lines = [header]
    for group, group_rows in filtered_groups:
        lines.append(f"{group} ({len(group_rows)} คน):")
        include_details = group_filter is not None and len(group_rows) <= 6
        lines.extend(_format_member_row(row, include_details=include_details) for row in group_rows)
        lines.append("")
    if lines and not lines[-1]:
        lines.pop()
    lines.append(f"แหล่งข้อมูล: {MEMBERS_URL}")
    return StructuredToolResult(
        "\n".join(lines),
        [_hit("Members", "members", MEMBERS_URL, "Members")],
        "structured_members_group_list",
        0.96,
        {**evidence, "selected_group": group_filter or "all", "returned_members": total},
    )


@lru_cache(maxsize=8)
def _games_by_zone(zone: str | None = None) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = {zone_name: [] for zone_name in ZONE_ALIASES}
    for row in _current_game_rows():
        zones = row.get("zones") or []
        if not zones:
            continue
        for row_zone in zones:
            canonical = _canonical_zone_label(str(row_zone))
            grouped.setdefault(canonical, []).append(row)
    for zone_rows in grouped.values():
        zone_rows.sort(key=lambda item: str(item.get("game") or "").lower())
    if zone:
        return {zone: grouped.get(zone, [])}
    return grouped


def _format_game_list(grouped: dict[str, list[dict[str, Any]]], intro: str) -> str:
    lines = [intro]
    for zone, rows in grouped.items():
        if not rows:
            continue
        lines.append("")
        lines.append(f"{zone} ({len(rows)} เกม)")
        lines.extend(f"•    {row.get('game')}" for row in rows)
    lines.append(f"แหล่งข้อมูล: {OUR_GAMES_URL}")
    return "\n".join(lines)


def _game_catalog_result(q: str, zone: str | None, intent: UniversalIntent) -> StructuredToolResult:
    grouped = _games_by_zone(zone)
    if zone:
        rows = grouped.get(zone, [])
        if intent.operation == "count" or _has(q, "กี่เกม", "จำนวนเกม"):
            intro = f"{zone} มีเกมที่ยืนยันได้ {len(rows)} เกมครับ"
        else:
            intro = f"{zone} มีเกมที่ยืนยันได้ดังนี้"
        confidence = 0.97
    else:
        unique_games = {str(row.get("game")) for rows in grouped.values() for row in rows}
        intro = f"ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด {len(unique_games)} เกมครับ"
        confidence = 0.95
    return StructuredToolResult(
        _format_game_list(grouped, intro),
        [_hit("our_games", "games", OUR_GAMES_URL, "Our Games")],
        "structured_games_catalog",
        confidence,
        {
            "tool": "get_games_by_zone",
            "zone": zone or "all",
            "count": sum(len(rows) for rows in grouped.values()),
        },
    )


def _game_zone_ranking_answer(query: str) -> StructuredToolResult | None:
    q = normalize_text(query)
    if not looks_like_game_zone_ranking_query(q):
        return None

    grouped = _games_by_zone()
    counts = {
        zone: len(rows)
        for zone, rows in grouped.items()
        if rows
    }
    if not counts:
        return None
    ascending = _has(q, "น้อยสุด", "น้อยที่สุด")
    ordered = sorted(counts.items(), key=lambda item: (item[1], item[0]), reverse=not ascending)
    best_count = ordered[0][1]
    best_zones = [zone for zone, count in counts.items() if count == best_count]
    best_text = " และ ".join(best_zones)
    direction = "น้อยสุด" if ascending else "เยอะสุด"
    lines = [
        f"ถ้านับตามโซน/บริการที่มีรายชื่อเกมยืนยันได้ {best_text} มีเกม{direction}ครับ ({best_count} เกม)",
        "",
        "จำนวนเกมตามโซน:",
    ]
    for zone, count in ordered:
        lines.append(f"•    {zone}: {count} เกม")
    lines.append(f"แหล่งข้อมูล: {OUR_GAMES_URL}")
    return StructuredToolResult(
        "\n".join(lines),
        [_hit("our_games_zone_game_counts", "games", OUR_GAMES_URL, "Game counts by zone")],
        "structured_game_zone_ranking",
        0.96,
        {"tool": "rank_game_counts_by_zone", "counts": counts, "direction": "asc" if ascending else "desc"},
    )


GAME_GENRE_GROUPS = {
    "fps": {
        "label": "FPS / เกมยิง",
        "aliases": ("fps", "เอฟพีเอส", "ยิง", "เกมยิง", "เกมปืน", "ปืน"),
        "keywords": ("fps", "ยิง"),
    },
    "battle_royale": {
        "label": "Battle Royale / Survival",
        "aliases": ("battle royale", "แบทเทิลรอยัล", "แบตเทิลรอยัล", "เอาชีวิตรอด", "survival"),
        "keywords": ("battle royale", "survival", "เอาชีวิตรอด"),
    },
    "fighting": {
        "label": "Fighting / เกมต่อสู้",
        "aliases": ("fighting", "ไฟท์ติ้ง", "ไฟติ้ง", "ต่อสู้", "เกมต่อสู้"),
        "keywords": ("fighting", "ต่อสู้"),
    },
    "racing": {
        "label": "Racing / เกมแข่งรถ",
        "aliases": ("racing", "เรซซิ่ง", "แข่งรถ", "ขับรถ", "รถ"),
        "keywords": ("racing", "แข่งรถ", "driving"),
    },
    "sports": {
        "label": "Sports / เกมกีฬา",
        "aliases": ("sports", "กีฬา", "เกมกีฬา", "ฟุตบอล"),
        "keywords": ("sports", "กีฬา", "ฟุตบอล"),
    },
    "party": {
        "label": "Party / Co-op",
        "aliases": ("party", "ปาร์ตี้", "co-op", "coop", "เล่นด้วยกัน", "หลายคน"),
        "keywords": ("party", "co-op", "coop"),
    },
    "rhythm": {
        "label": "Rhythm / เกมจังหวะ",
        "aliases": ("rhythm", "จังหวะ", "เพลง", "เกมจังหวะ"),
        "keywords": ("rhythm", "จังหวะ"),
    },
    "rpg": {
        "label": "RPG / Action RPG",
        "aliases": ("rpg", "อาร์พีจี", "ล่ามอนสเตอร์"),
        "keywords": ("rpg", "ล่ามอนสเตอร์"),
    },
    "horror": {
        "label": "Horror / เกมสยองขวัญ",
        "aliases": ("horror", "สยอง", "ผี", "เกมผี"),
        "keywords": ("horror", "สยอง"),
    },
}


def _genre_group_for_query(q: str) -> dict[str, Any] | None:
    if not _has(q, "เกม", "game", "games", "แนว", "ประเภท", "fps", "racing", "sports", "party"):
        return None
    for group in GAME_GENRE_GROUPS.values():
        if _has(q, *group["aliases"]):
            return group
    return None


def _game_genre_answer(query: str) -> StructuredToolResult | None:
    q = normalize_text(query)
    group = _genre_group_for_query(q)
    if group is None:
        return None
    if _has(q, "คือเกมอะไร", "เป็นเกมแนวไหน", "แนวไหน", "แนวอะไร") and _detect_game(query):
        return None

    rows: list[dict[str, Any]] = []
    keywords = tuple(normalize_text(str(item)) for item in group["keywords"])
    for row in _current_game_rows():
        genre = normalize_text(str(row.get("genre") or ""))
        summary = normalize_text(str(row.get("summary_th") or ""))
        if any(keyword in genre for keyword in keywords) or (not genre and any(keyword in summary for keyword in keywords)):
            rows.append(row)

    if not rows:
        return StructuredToolResult(
            f"ยังไม่พบเกมแนว {group['label']} ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ\n"
            f"แหล่งข้อมูล: {OUR_GAMES_URL}",
            [_hit("our_games", "games", OUR_GAMES_URL, "Our Games")],
            "structured_games_genre_no_data",
            0.90,
            {"tool": "filter_games_by_genre", "genre": group["label"], "count": 0},
        )

    lines = [f"เกมแนว {group['label']} ที่พบในรายการเกมที่ยืนยันได้:"]
    for row in rows:
        zones = " และ ".join(row.get("zones") or [])
        lines.append("")
        lines.append(str(row.get("game") or ""))
        if row.get("genre"):
            lines.append(f"•    แนวเกม: {row.get('genre')}")
        if zones:
            lines.append(f"•    เล่นได้ที่: {zones}")
    lines.append(f"แหล่งข้อมูล: {OUR_GAMES_URL}")
    return StructuredToolResult(
        "\n".join(lines),
        [_hit("our_games_genre", "games", OUR_GAMES_URL, "Games by genre")],
        "structured_games_genre_list",
        0.95,
        {"tool": "filter_games_by_genre", "genre": group["label"], "count": len(rows)},
    )


def _cross_zone_game_answer(query: str) -> StructuredToolResult | None:
    q = normalize_text(query)
    if not (
        _has(q, "หลายโซน", "หลายเครื่อง", "อยู่หลายโซน", "เล่นได้หลายโซน", "มีหลายโซน")
        or (_has(q, "ทั้ง pc", "pc และ ps5", "pc กับ ps5", "pc/ps5", "คอมและ ps5", "คอมกับ ps5") and _has(q, "เกมไหน", "เกมอะไร", "เล่นได้", "มีเกม"))
    ):
        return None

    rows = [row for row in _current_game_rows() if len(row.get("zones") or []) > 1]
    if not rows:
        return StructuredToolResult(
            f"ตอนนี้ยังไม่พบเกมที่ยืนยันว่าเล่นได้หลายโซนในฐานข้อมูลครับ\nแหล่งข้อมูล: {OUR_GAMES_URL}",
            [_hit("our_games_cross_zone", "games", OUR_GAMES_URL, "Cross-zone games")],
            "structured_games_cross_zone",
            0.92,
            {"tool": "list_cross_zone_games", "count": 0},
        )

    lines = ["เกมที่ยืนยันว่าเล่นได้มากกว่า 1 โซน:"]
    for row in rows:
        zones = " และ ".join(row.get("zones") or [])
        lines.append(f"•    {row.get('game')}: {zones}")
    lines.append(f"แหล่งข้อมูล: {OUR_GAMES_URL}")
    return StructuredToolResult(
        "\n".join(lines),
        [_hit("our_games_cross_zone", "games", OUR_GAMES_URL, "Cross-zone games")],
        "structured_games_cross_zone",
        0.96,
        {"tool": "list_cross_zone_games", "count": len(rows)},
    )


def _game_family_answer(query: str) -> StructuredToolResult | None:
    q = normalize_text(query)
    q = q.replace("over cook", "overcook")
    resolution = resolve_game_entity(query, operation="detail")
    if (
        resolution.status == "exact"
        and resolution.top_candidate is not None
        and resolution.top_candidate.match_type != "family"
    ):
        return None
    families = {
        "Mario": {
            "aliases": ("mario", "มาริโอ", "มาริโอ้"),
            "specific": ("kart", "คาร์ท", "คาท", "คาส", "party", "odyssey", "bros", "super mario", "8", "live"),
        },
        "Resident Evil": {
            "aliases": ("resident evil", "resident", "เรสซิเดนต์", "เรสซิเดนท์", "อีวิล", "อีวิว"),
            "specific": ("4", "village"),
        },
        "Call of Duty": {
            "aliases": (
                "call of duty",
                "คอลออฟดิวตี้",
                "คอลออฟดูตี้",
                "ดิวตี้",
                "ดูตี้",
            ),
            "specific": ("warzone", "วอร์โซน", "วอโซน", "modern warfare", "mw3", "mwiii", "วอร์แฟร์"),
        },
        "Overcooked": {
            "aliases": ("overcooked", "overcook", "โอเวอร์คุก", "โอเวอร์คุ๊ก", "โอเวอคุก", "โอเวอคุ๊ก"),
            "specific": ("2", "two", "ทู", "สอง"),
        },
    }
    for label, meta in families.items():
        if not _has(q, *meta["aliases"]) or _has(q, *meta["specific"]):
            continue
        rows = [
            row for row in _current_game_rows()
            if label.lower() in str(row.get("game") or "").lower()
        ]
        if not rows:
            continue
        lines = [f"พบเกมที่เกี่ยวข้องกับ {label} ในรายการที่ยืนยันได้ครับ"]
        for row in sorted(rows, key=lambda item: str(item.get("game") or "")):
            zones = " และ ".join(row.get("zones") or [])
            lines.append(f"• {row.get('game')}: เล่นได้ที่ {zones}")
        lines.append(f"แหล่งข้อมูล: {OUR_GAMES_URL}")
        return StructuredToolResult(
            "\n".join(lines),
            [_hit("our_games", "games", OUR_GAMES_URL, "Our Games")],
            "structured_games_family",
            0.94,
            {"tool": "get_game_family", "family": label, "count": len(rows)},
        )
    return None


def _control_row_query_overlap_score(query: str, row: dict[str, Any]) -> int:
    q_norm = normalize_text(query)
    exact_score = 0
    for value in (row.get("action_th"), row.get("action_en")):
        value_norm = normalize_text(str(value or ""))
        if value_norm and value_norm in q_norm:
            exact_score += 20
    q_tokens = {
        token for token in re.findall(r"[0-9a-z+.-]+|[\u0E00-\u0E7F]+", q_norm)
        if len(_compact(token)) >= 3
        and token not in {"call", "duty", "cod", "ปุ่ม", "กด", "อะไร", "ต้อง", "ถ้า", "จะ", "เกม", "controller", "controls"}
    }
    searchable = normalize_text(
        " ".join(
            str(value or "")
            for value in (
                row.get("button"),
                row.get("action_th"),
                row.get("action_en"),
                row.get("description_th"),
                " ".join(str(alias) for alias in (row.get("aliases") or [])),
            )
        )
    )
    return exact_score + sum(1 for token in q_tokens if token in searchable)


def _best_control_game_for_query(query: str, rows: list[dict[str, Any]], preferred_game: str = "") -> str:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        game = str(row.get("game") or "").strip()
        if game:
            grouped.setdefault(game, []).append(row)
    if not grouped:
        return str(rows[0].get("game") or "") if rows else ""
    preferred_key = _compact(preferred_game)
    best: tuple[int, int, int, int, str] | None = None
    for index, (game, game_rows) in enumerate(grouped.items()):
        score = sum(_control_row_query_overlap_score(query, row) for row in game_rows)
        preferred = 1 if preferred_key and _compact(game) == preferred_key else 0
        candidate = (score, preferred, len(game_rows), -index, game)
        if best is None or candidate > best:
            best = candidate
    return best[4] if best else str(rows[0].get("game") or "")


def _game_control_family_answer(query: str) -> StructuredToolResult | None:
    q = normalize_text(query).replace("over cook", "overcook")
    if not _looks_like_control_or_gameplay_query(q):
        return None
    resolution = resolve_game_entity(query, operation="controls")
    if (
        resolution.status == "exact"
        and resolution.top_candidate is not None
        and resolution.top_candidate.match_type != "family"
    ):
        return None
    families = {
        "Mario": {
            "aliases": ("mario", "มาริโอ", "มาริโอ้"),
            "specific": ("kart", "คาร์ท", "คาท", "คาส", "party", "odyssey", "bros", "super mario", "8", "live"),
        },
        "Resident Evil": {
            "aliases": ("resident evil", "resident", "เรสซิเดนต์", "เรสซิเดนท์", "อีวิล", "อีวิว"),
            "specific": ("4", "village"),
        },
        "Overcooked": {
            "aliases": ("overcooked", "overcook", "โอเวอร์คุก", "โอเวอร์คุ๊ก", "โอเวอคุก", "โอเวอคุ๊ก"),
            "specific": ("2", "two", "ทู", "สอง"),
        },
        "Call of Duty": {
            "aliases": ("call of duty", "cod", "คอลออฟดิวตี้", "คอลออฟดูตี้", "ดิวตี้", "ดูตี้"),
            "specific": ("warzone", "วอร์โซน", "วอโซน", "modern warfare", "mw3", "mwiii", "วอร์แฟร์"),
            "default_control_game": "Call of Duty: Modern Warfare III",
        },
    }
    control_counts: dict[str, int] = {}
    for row in _control_rows():
        game_name = str(row.get("game") or "").strip()
        if game_name:
            control_counts[_compact(game_name)] = control_counts.get(_compact(game_name), 0) + 1

    for label, meta in families.items():
        if not _has(q, *meta["aliases"]) or _has(q, *meta["specific"]):
            continue
        rows = [
            row for row in _current_game_rows()
            if label.lower() in str(row.get("game") or "").lower()
        ]
        if not rows:
            continue
        family_game_keys = {_compact(str(row.get("game") or "")) for row in rows}
        family_control_rows = [
            row for row in _control_rows()
            if _compact(str(row.get("game") or "")) in family_game_keys
        ]
        default_control_game = str(meta.get("default_control_game") or "").strip()
        if default_control_game and _has(q, "ทั้งหมด", "ทุกปุ่ม", "ปุ่มทั้งหมด", "มีปุ่มอะไร", "controller", "controls", "ใช้จอยยังไง"):
            default_rows = [
                row for row in family_control_rows
                if _compact(str(row.get("game") or "")) == _compact(default_control_game)
            ]
            if default_rows:
                platform_groups: dict[str, list[dict[str, Any]]] = {}
                for row in default_rows:
                    platform_groups.setdefault(str(row.get("platform") or "ไม่ระบุแพลตฟอร์ม"), []).append(row)
                lines = [f"{default_control_game} มีข้อมูลปุ่มควบคุมดังนี้:"]
                for platform, platform_rows in platform_groups.items():
                    lines.append(f"{platform}")
                    for row in platform_rows:
                        button = str(row.get("button") or "").strip()
                        action = str(row.get("action_th") or row.get("action_en") or "").strip()
                        description = str(row.get("description_th") or "").strip()
                        line = f"•    {button}: {action}" if action else f"•    {button}"
                        if description:
                            line += f" - {description}"
                        lines.append(line)
                source_url = str(default_rows[0].get("source_url") or "")
                if source_url:
                    lines.append(f"แหล่งข้อมูล: {source_url}")
                return StructuredToolResult(
                    "\n".join(lines),
                    [_hit(f"game_controls_{_compact(default_control_game)}", "game_controls", source_url, f"{default_control_game} controls")],
                    "structured_game_controls",
                    0.92,
                    {
                        "tool": "get_game_controls",
                        "game": default_control_game,
                        "family": label,
                        "defaulted_from_family": True,
                        "returned_control_count": len(default_rows),
                    },
                )
        if family_control_rows and not _has(q, "ทั้งหมด", "ทุกปุ่ม", "ปุ่มทั้งหมด", "มีปุ่มอะไร", "controller", "controls", "ใช้จอยยังไง"):
            selected_rows = _select_control_rows(query, family_control_rows)
            if selected_rows and len(selected_rows) < len(family_control_rows):
                selected_game = _best_control_game_for_query(query, selected_rows, default_control_game)
                selected_rows = [
                    row for row in selected_rows
                    if _compact(str(row.get("game") or "")) == _compact(selected_game)
                ]
                platform_groups: dict[str, list[dict[str, Any]]] = {}
                for row in selected_rows:
                    platform_groups.setdefault(str(row.get("platform") or "ไม่ระบุแพลตฟอร์ม"), []).append(row)
                lines = [f"{selected_game} ปุ่มที่ตรงกับคำถาม:"]
                for platform, platform_rows in platform_groups.items():
                    lines.append(f"{platform}")
                    for row in platform_rows:
                        button = str(row.get("button") or "").strip()
                        action = str(row.get("action_th") or row.get("action_en") or "").strip()
                        description = str(row.get("description_th") or "").strip()
                        line = f"•    {button}: {action}" if action else f"•    {button}"
                        if description:
                            line += f" - {description}"
                        lines.append(line)
                source_url = str(selected_rows[0].get("source_url") or "")
                if source_url:
                    lines.append(f"แหล่งข้อมูล: {source_url}")
                return StructuredToolResult(
                    "\n".join(lines),
                    [_hit(f"game_controls_{_compact(selected_game)}", "game_controls", source_url, f"{selected_game} controls")],
                    "structured_game_controls",
                    0.92,
                    {
                        "tool": "get_game_controls",
                        "game": selected_game,
                        "family": label,
                        "returned_control_count": len(selected_rows),
                    },
                )
        with_controls = [
            (row, control_counts.get(_compact(str(row.get("game") or "")), 0))
            for row in sorted(rows, key=lambda item: str(item.get("game") or ""))
        ]
        available = [(row, count) for row, count in with_controls if count]
        missing = [row for row, count in with_controls if not count]
        lines = [
            f"{label} มีหลายเกมในรายการที่ยืนยันได้ครับ ถ้าต้องการปุ่มแบบละเอียดควรระบุชื่อภาค/ชื่อเกมให้ชัดเจน",
        ]
        if available:
            lines.append("เกมที่มีข้อมูลปุ่มแล้ว:")
            for row, count in available:
                zones = " และ ".join(row.get("zones") or [])
                zone_suffix = f" ({zones})" if zones else ""
                lines.append(f"•    {row.get('game')}: มีข้อมูลปุ่ม {count} รายการ{zone_suffix}")
        if missing:
            lines.append("เกมที่ยังไม่มีข้อมูลปุ่มในฐานข้อมูล:")
            for row in missing:
                lines.append(f"•    {row.get('game')}")
        lines.append(f"แหล่งข้อมูล: {OUR_GAMES_URL}")
        return StructuredToolResult(
            "\n".join(lines),
            [_hit("our_games", "games", OUR_GAMES_URL, f"{label} controls summary")],
            "structured_game_controls_family_summary",
            0.90,
            {
                "tool": "summarize_family_control_availability",
                "family": label,
                "available_count": len(available),
                "missing_count": len(missing),
            },
        )
    return None


def _last_of_us_aggregate_answer(query: str) -> StructuredToolResult | None:
    q = normalize_text(query)
    if not _has(q, "the last of us", "last of us", "tlou", "ลาสออฟอัส"):
        return None
    if not (_has(q, "part i / part ii", "part i", "part ii", "ภาค 1", "ภาค 2", "ภาคแรก", "ภาคสอง") or "/" in query):
        return None
    if not (
        _looks_like_specific_game_detail_query(query)
        or _has(q, "เล่นยังไง", "เล่นอย่างไร", "วิธีเล่น", "สอนเล่น", "แนวอะไร", "แนวไหน", "คือเกมอะไร", "คืออะไร")
    ):
        return None
    aggregate = next(
        (row for row in _game_rows() if _game_key(str(row.get("game") or "")) == _game_key("The Last of Us Part I / Part II")),
        None,
    )
    if aggregate is None:
        return None
    current_parts = [
        row for row in _current_game_rows()
        if normalize_text(str(row.get("game") or "")).startswith("the last of us part")
    ]
    part_names = ", ".join(str(row.get("game")) for row in current_parts) or "The Last of Us Part I / Part II"
    lines = [
        "The Last of Us Part I / Part II:",
        str(aggregate.get("summary_th") or "มีข้อมูลเกมนี้ในฐานข้อมูลของศูนย์"),
    ]
    if aggregate.get("genre"):
        lines.append(f"แนวเกม: {aggregate.get('genre')}")
    if aggregate.get("how_to_play_th"):
        lines.append(f"วิธีเล่นโดยสรุป: {aggregate.get('how_to_play_th')}")
    lines.append(f"เล่นได้ที่: PlayStation 5 Zone")
    lines.append(f"รายการปัจจุบันในระบบจอง: {part_names}")
    lines.append(f"แหล่งข้อมูล: {aggregate.get('source_url') or OUR_GAMES_URL}")
    return StructuredToolResult(
        "\n".join(lines),
        [_hit("The Last of Us Part I / Part II", "games", str(aggregate.get("source_url") or OUR_GAMES_URL), "The Last of Us Part I / Part II")],
        "structured_game_detail",
        0.94,
        {"tool": "get_game_detail_aggregate", "game": "The Last of Us Part I / Part II", "parts": part_names},
    )


def _game_answer(query: str, intent: UniversalIntent) -> StructuredToolResult | None:
    q = normalize_text(query)
    if _has(q, "ถามหลาย", "หลายๆอย่าง", "หลายอย่าง", "ถามอะไร", "ถามได้", "เกี่ยวกับเกม", "เรื่องเกม") and not _has(
        q, "มีเกม", "เกมอะไร", "กี่เกม", "รายชื่อเกม"
    ):
        return None
    non_current_answer = _non_current_control_game_answer(query)
    if non_current_answer is not None and not _has(q, "มีเกม", "เกมอะไร", "กี่เกม", "รายชื่อเกม", "รายการเกม", "เกมทั้งหมด"):
        return non_current_answer
    zone = _detect_zone(query, intent.target)
    last_of_us_result = _last_of_us_aggregate_answer(query)
    if last_of_us_result is not None:
        return last_of_us_result
    family_result = _game_family_answer(query)
    if family_result is not None:
        return family_result
    availability_result = None
    if intent.domain in {"games", "reservation"} or route.category == "games":
        availability_result = _service_game_availability_answer(query, intent)
    if availability_result is not None:
        return availability_result
    cross_zone_result = _cross_zone_game_answer(query)
    if cross_zone_result is not None:
        return cross_zone_result
    genre_result = _game_genre_answer(query)
    if genre_result is not None:
        return genre_result
    asks_catalog = intent.operation in {"count", "list"} or _has(q, "มีเกม", "เกมอะไร", "กี่เกม", "รายชื่อเกม")
    if _looks_like_specific_game_detail_query(query) or _looks_like_competition_rule_query(query):
        asks_catalog = False
    if asks_catalog:
        return _game_catalog_result(q, zone, intent)
    game = _detect_game(query, intent.target)

    unsupported_games = {
        "Minecraft": ("minecraft", "มายคราฟ", "ไมน์คราฟต์", "ไมน์คราฟ"),
        "Roblox": ("roblox", "โรบล็อก", "โรบอก"),
    }
    if game is None and intent.operation == "availability":
        for name, aliases in unsupported_games.items():
            if _has(q, *aliases):
                return None

    if game and (
        intent.operation in {"detail", "how_to", "availability"}
        or _looks_like_specific_game_detail_query(query)
        or _looks_like_game_info_query(query)
    ):
        zones = " และ ".join(game.get("zones") or [])
        lines = [
            f"{game['game']}: {game.get('summary_th') or 'มีข้อมูลเกมนี้ในฐานข้อมูลของศูนย์'}",
        ]
        if game.get("genre"):
            lines.append(f"แนวเกม: {game.get('genre')}")
        if game.get("how_to_play_th"):
            lines.append(f"วิธีเล่นโดยสรุป: {game.get('how_to_play_th')}")
        if zones:
            lines.append(f"เล่นได้ที่: {zones}")
        lines.append(f"แหล่งข้อมูล: {game.get('source_url') or OUR_GAMES_URL}")
        return StructuredToolResult(
            "\n".join(lines),
            [_hit(str(game.get("game")), "games", str(game.get("source_url") or OUR_GAMES_URL), str(game.get("game")))],
            "structured_game_detail",
            0.94,
            {"tool": "get_game_detail", "game": game.get("game"), "zones": game.get("zones") or []},
        )

    asks_catalog = intent.operation in {"count", "list"} or _has(q, "มีเกม", "เกมอะไร", "กี่เกม", "รายชื่อเกม")
    if _looks_like_specific_game_detail_query(query) or _looks_like_competition_rule_query(query):
        asks_catalog = False
    if game and _looks_like_specific_game_detail_query(query):
        asks_catalog = False
    if game and _looks_like_competition_rule_query(query):
        asks_catalog = False

    if asks_catalog:
        grouped = _games_by_zone(zone)
        if zone:
            rows = grouped.get(zone, [])
            if intent.operation == "count" or _has(q, "กี่เกม", "จำนวนเกม"):
                intro = f"{zone} มีเกมที่ยืนยันได้ {len(rows)} เกมครับ"
            else:
                intro = f"{zone} มีเกมที่ยืนยันได้ดังนี้"
            confidence = 0.97
        else:
            unique_games = {str(row.get("game")) for rows in grouped.values() for row in rows}
            intro = f"ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด {len(unique_games)} เกมครับ"
            confidence = 0.95
        return StructuredToolResult(
            _format_game_list(grouped, intro),
            [_hit("our_games", "games", OUR_GAMES_URL, "Our Games")],
            "structured_games_catalog",
            confidence,
            {
                "tool": "get_games_by_zone",
                "zone": zone or "all",
                "counts": {zone_name: len(rows) for zone_name, rows in grouped.items() if rows},
            },
        )
    return None


def _format_known_game_without_controls(game: dict[str, Any], game_name: str) -> str:
    zones = " และ ".join(game.get("zones") or [])
    lines = [
        f"{game_name} มีอยู่ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ",
    ]
    if game.get("summary_th"):
        lines.append(str(game.get("summary_th")))
    if game.get("genre"):
        lines.append(f"แนวเกม: {game.get('genre')}")
    if game.get("how_to_play_th"):
        lines.append(f"วิธีเล่นโดยสรุป: {game.get('how_to_play_th')}")
    if zones:
        lines.append(f"เล่นได้ที่: {zones}")
    lines.append(f"ยังไม่พบข้อมูลปุ่มควบคุมของ {game_name} ที่ยืนยันได้ในฐานข้อมูลตอนนี้ครับ")
    lines.append(f"แหล่งข้อมูล: {OUR_GAMES_URL}")
    return "\n".join(lines)


def _control_answer(query: str, intent: UniversalIntent) -> StructuredToolResult | None:
    non_current_answer = _non_current_control_game_answer(query)
    if non_current_answer is not None:
        return non_current_answer
    family_result = _game_control_family_answer(query)
    if family_result is not None:
        return family_result
    game = _detect_game(query, intent.target)
    if game is None:
        return None
    game_name = str(game.get("game") or "")
    game_key = _game_key(game_name)
    rows = [
        row for row in _control_rows()
        if _game_key(str(row.get("game") or "")) == game_key
    ]
    if not rows:
        if _compact(game_name) == _compact("The Last of Us Part I / Part II"):
            part_rows_by_game: dict[str, list[dict[str, Any]]] = {}
            for row in _control_rows():
                row_game = str(row.get("game") or "").strip()
                if row_game in {"The Last of Us Part I", "The Last of Us Part II"}:
                    part_rows_by_game.setdefault(row_game, []).append(row)
            if part_rows_by_game:
                lines = [
                    "The Last of Us Part I / Part II เป็นรายการชื่อรวมครับ ตอนนี้มีข้อมูลปุ่มแยกตามภาคดังนี้:",
                ]
                hits: list[dict[str, Any]] = []
                for part_name in ("The Last of Us Part I", "The Last of Us Part II"):
                    part_rows = part_rows_by_game.get(part_name) or []
                    if not part_rows:
                        continue
                    platforms = " / ".join(sorted({str(row.get("platform") or "") for row in part_rows if row.get("platform")}))
                    lines.append(f"•    {part_name}: มีข้อมูลปุ่ม {len(part_rows)} รายการ" + (f" ({platforms})" if platforms else ""))
                    source_url = str(part_rows[0].get("source_url") or "")
                    if source_url:
                        hits.append(_hit(f"game_controls_{_compact(part_name)}", "game_controls", source_url, f"{part_name} controls"))
                lines.append("ถ้าต้องการปุ่มละเอียด ให้ระบุภาค เช่น `The Last of Us Part I ปุ่มทั้งหมด` หรือ `The Last of Us Part II ปุ่มทั้งหมด`")
                return StructuredToolResult(
                    "\n".join(lines),
                    _dedupe_hits(hits),
                    "structured_game_controls_family_summary",
                    0.91,
                    {
                        "tool": "summarize_aggregate_game_control_availability",
                        "game": game_name,
                        "available_games": list(part_rows_by_game),
                    },
                )
        return StructuredToolResult(
            _format_known_game_without_controls(game, game_name),
            [_hit(str(game_name), "games", OUR_GAMES_URL, str(game_name))],
            "structured_game_controls_no_data",
            0.88,
            {
                "tool": "get_game_controls",
                "game": game_name,
                "control_count": 0,
                "game_found": True,
                "zones": game.get("zones") or [],
            },
        )

    display_game_name = str(rows[0].get("game") or game_name).strip() or game_name
    selected_rows = _select_control_rows(query, rows)
    platform_groups: dict[str, list[dict[str, Any]]] = {}
    for row in selected_rows:
        platform_groups.setdefault(str(row.get("platform") or "ไม่ระบุแพลตฟอร์ม"), []).append(row)

    lines = [
        f"{display_game_name} มีข้อมูลปุ่มควบคุมดังนี้:"
        if len(selected_rows) == len(rows)
        else f"{display_game_name} ปุ่มที่ตรงกับคำถาม:"
    ]
    for platform, platform_rows in platform_groups.items():
        lines.append(f"{platform}")
        for row in platform_rows:
            button = str(row.get("button") or "").strip()
            action = str(row.get("action_th") or row.get("action_en") or "").strip()
            description = str(row.get("description_th") or "").strip()
            line = f"•    {button}: {action}" if action else f"•    {button}"
            if description:
                line += f" - {description}"
            lines.append(line)
    source_url = str(rows[0].get("source_url") or "")
    if source_url:
        lines.append(f"แหล่งข้อมูล: {source_url}")
    return StructuredToolResult(
        "\n".join(lines),
        [_hit(f"game_controls_{_compact(display_game_name)}", "game_controls", source_url, f"{display_game_name} controls")],
        "structured_game_controls",
        0.96,
        {
            "tool": "get_game_controls",
            "game": display_game_name,
            "control_count": len(rows),
            "returned_control_count": len(selected_rows),
            "platforms": {platform: len(platform_rows) for platform, platform_rows in platform_groups.items()},
        },
    )


def _select_control_rows(query: str, rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    q = normalize_text(query)
    if _has(q, "ทั้งหมด", "ทุกปุ่ม", "ปุ่มทั้งหมด", "มีปุ่มอะไร", "controller", "controls", "ใช้จอยยังไง"):
        return rows

    matches: list[dict[str, Any]] = []
    for row in rows:
        values = {
            "button": [str(row.get("button") or ""), *(str(item) for item in (row.get("buttons") or []))],
            "action": [str(row.get("action_th") or ""), str(row.get("action_en") or "")],
            "description": [str(row.get("description_th") or "")],
        }
        if _control_values_match(query, values):
            matches.append(row)
    return matches or rows


def _equipment_answer(query: str, intent: UniversalIntent) -> StructuredToolResult | None:
    q = normalize_text(query)
    rows = list(_equipment_rows())
    if not rows:
        return None
    asks_catalog = _has_normalized(q, "มีอุปกรณ์อะไร", "อุปกรณ์อะไร", "มีอะไรบ้าง", "อุปกรณ์บน", "อุปกรณ์ใน", "รายการอุปกรณ์")
    item = None if asks_catalog else _detect_equipment_item(query, intent.target)
    zone = str(item.get("zone") or "") if item is not None else _detect_zone(query, intent.target)
    zone = zone or None
    if zone and _has_normalized(q, "ทีวี", "tv", "จอ", "กี่นิ้ว"):
        display_rows = [
            row for row in rows
            if zone in str(row.get("zone") or "") and _has(str(row.get("item") or ""), "ทีวี", "tv", "monitor", "จอ")
        ]
        if display_rows:
            item = display_rows[0]

    if item is not None and _has_normalized(q, "คืออะไร", "อะไร", "ใช้ยังไง", "ใช้ทำอะไร", "วิธีใช้", "อยู่ไหน", "โซนไหน", "กี่", "จำนวน", "รุ่นไหน", "เครื่องรุ่นไหน", "สเปค", "สเป็ค", "spec"):
        lines = [f"{item.get('item')}: {item.get('what_th')}"]
        quantity = str(item.get("quantity") or "").strip()
        if quantity:
            lines.append(f"จำนวน: {quantity}")
        lines.append(f"อยู่ที่: {item.get('zone')}")
        if _has_normalized(q, "ใช้ยังไง", "วิธีใช้", "เล่นยังไง", "ใช้งาน"):
            lines.append(f"วิธีใช้โดยสรุป: {item.get('how_to_use_th')}")
        use_cases = [str(value) for value in (item.get("use_cases_th") or []) if value]
        if use_cases:
            lines.append("ใช้สำหรับ:")
            lines.extend(f"•    {value}" for value in use_cases[:8])
        note = str(item.get("note_th") or "").strip()
        if note:
            lines.append(f"หมายเหตุ: {note}")
        source_url = str(item.get("source_url") or HOME_URL)
        lines.append(f"แหล่งข้อมูล: {source_url}")
        return StructuredToolResult(
            "\n".join(lines),
            [_hit(str(item.get("id") or item.get("item")), "equipment", source_url, str(item.get("item")))],
            "structured_equipment_item",
            0.95,
            {"tool": "get_equipment_item", "item": item.get("item"), "zone": item.get("zone"), "quantity": quantity},
        )

    formatted_home = _format_home_equipment_catalog(rows, zone)
    if formatted_home is not None:
        return StructuredToolResult(
            formatted_home,
            [_hit("home_equipment", "equipment", HOME_URL, "Home Equipment")],
            "structured_equipment_catalog",
            0.96,
            {"tool": "get_equipment_by_zone", "zone": "all", "equipment_count": len(rows)},
        )

    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        row_zone = str(row.get("zone") or "ไม่ระบุโซน")
        if zone and zone not in row_zone:
            continue
        grouped.setdefault(row_zone, []).append(row)
    if not grouped:
        return None
    total = sum(len(values) for values in grouped.values())
    intro = f"อุปกรณ์ใน {zone}:" if zone else "อุปกรณ์ในศูนย์แยกตามโซน:"
    lines = [intro]
    for group, group_rows in grouped.items():
        lines.append(f"{group}")
        for row in group_rows:
            quantity = str(row.get("quantity") or "").strip()
            suffix = f" ({quantity})" if quantity else ""
            lines.append(f"•    {row.get('item')}{suffix}")
    lines.append(f"แหล่งข้อมูล: {HOME_URL}")
    return StructuredToolResult(
        "\n".join(lines),
        [_hit("home_equipment", "equipment", HOME_URL, "Home Equipment")],
        "structured_equipment_catalog",
        0.95,
        {"tool": "get_equipment_by_zone", "zone": zone or "all", "equipment_count": total},
    )


def _service_fee_answer(query: str, intent: UniversalIntent) -> StructuredToolResult | None:
    if intent.domain != "service_fee":
        return None
    by_game = _service_fee_by_game_answer(query, intent)
    if by_game is not None:
        return by_game
    q = normalize_text(query)
    if _has(q, "ตั้งแต่", "ถึง", "ถึงกี่โมง") and re.search(r"\d", q):
        return None
    result = answer_service_fee(query)
    if not result.get("matched"):
        return None
    answer = str(result.get("answer") or "").strip()
    if not answer:
        return None
    return StructuredToolResult(
        answer,
        _source_hits_from_service_fee_result(result),
        "structured_service_fee",
        float(result.get("confidence") or 0.90),
        {
            "tool": "calculate_service_fee",
            "service_key": result.get("service_key"),
            "group_key": result.get("group_key"),
            "requested_minutes": result.get("requested_minutes"),
            "sessions": result.get("sessions"),
            "answer_type": result.get("answer_type"),
            "reason": result.get("reason"),
        },
    )


def _service_fee_by_game_answer(query: str, intent: UniversalIntent) -> StructuredToolResult | None:
    q = normalize_text(query)
    if not _has(q, "ราคา", "กี่บาท", "ค่าบริการ", "เสีย", "จ่าย", "เท่าไหร่", "เท่าไร"):
        return None
    game = _detect_game(query, intent.target)
    if not game:
        return None
    game_name = str(game.get("game") or "").strip()
    zones = [str(zone) for zone in (game.get("zones") or []) if str(zone).strip()]
    if not game_name or not zones:
        return None

    service_by_zone = {
        "PlayStation 5 Zone": "PS5",
        "Nintendo Switch Zone": "Nintendo",
        "VR Zone": "VR",
        "Cockpit Zone": "Cockpit",
        "PC Zone": "PC",
    }
    service_queries: list[tuple[str, str]] = []
    for zone in zones:
        service = service_by_zone.get(zone)
        if service:
            service_queries.append((zone, service))
    if not service_queries:
        return None

    display_game_name = "Overcooked 2 / Overcooked! 2" if _game_key(game_name) == _game_key("Overcooked 2") else game_name
    lines = [
        f"{display_game_name} ไม่มีราคาแยกตามชื่อเกมครับ ต้องดูราคาตามโซน/บริการที่ใช้เล่นเกมนี้",
    ]
    hits = [
        _hit(str(game_name), "games", str(game.get("source_url") or OUR_GAMES_URL), game_name),
        *make_source_hits([SERVICE_FEE_IMAGE_2026_ID]),
    ]
    confidence = 0.90
    for zone, service in service_queries:
        result = answer_service_fee(f"{service} {query}")
        answer = str(result.get("answer") or "").strip()
        if not result.get("matched") or not answer:
            continue
        confidence = min(confidence, float(result.get("confidence") or 0.86))
        hits.extend(_source_hits_from_service_fee_result(result))
        lines.append("")
        lines.append(f"{zone}")
        lines.extend(answer.splitlines())

    if len(lines) <= 1:
        return None
    return StructuredToolResult(
        "\n".join(lines),
        _dedupe_hits(hits),
        "structured_service_fee_by_game",
        max(confidence, 0.86),
        {
            "tool": "calculate_service_fee_by_game_zone",
            "game": game_name,
            "zones": zones,
            "services": [service for _zone, service in service_queries],
        },
    )


WEEKLY_SERVICE = {
    "monday": {
        "label": "วันจันทร์",
        "summary": "เปิดให้เล่นช่วง 13:00-16:00 ส่วน 09:00-12:00 เป็น Maintenance*",
        "slots": [
            {"label": "Morning", "time": "09:00-12:00", "status": "maintenance"},
            {"label": "Afternoon", "time": "13:00-16:00", "status": "open"},
        ],
    },
    "tuesday": {
        "label": "วันอังคาร",
        "summary": "เปิดให้เล่น 09:00-12:00 และ 13:00-16:00",
        "slots": [
            {"label": "Morning", "time": "09:00-12:00", "status": "open"},
            {"label": "Afternoon", "time": "13:00-16:00", "status": "open"},
        ],
    },
    "wednesday": {
        "label": "วันพุธ",
        "summary": "เปิดให้เล่น 09:00-12:00 และ 13:00-16:00",
        "slots": [
            {"label": "Morning", "time": "09:00-12:00", "status": "open"},
            {"label": "Afternoon", "time": "13:00-16:00", "status": "open"},
        ],
    },
    "thursday": {
        "label": "วันพฤหัสบดี",
        "summary": "เปิดให้เล่น 09:00-12:00 และ 13:00-16:00",
        "slots": [
            {"label": "Morning", "time": "09:00-12:00", "status": "open"},
            {"label": "Afternoon", "time": "13:00-16:00", "status": "open"},
        ],
    },
    "friday": {
        "label": "วันศุกร์",
        "summary": "เปิดให้เล่นช่วง 09:00-12:00 ส่วน 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning",
        "slots": [
            {"label": "Morning", "time": "09:00-12:00", "status": "open"},
            {"label": "Afternoon", "time": "13:00-16:00", "status": "maintenance"},
        ],
    },
}


def _detect_weekday(query: str) -> str | None:
    q = normalize_text(query)
    aliases = {
        "monday": ("จันทร์", "วันจันทร์", "monday", "mon"),
        "tuesday": ("อังคาร", "วันอังคาร", "tuesday", "tue"),
        "wednesday": ("พุธ", "วันพุธ", "wednesday", "wed"),
        "thursday": ("พฤหัส", "พฤหัสบดี", "วันพฤหัส", "thursday", "thu"),
        "friday": ("ศุกร์", "วันศุกร์", "friday", "fri"),
    }
    for key, terms in aliases.items():
        if any(normalize_text(term) in q for term in terms):
            return key
    return None


def _schedule_answer(query: str, intent: UniversalIntent) -> StructuredToolResult | None:
    if intent.domain not in {"schedule", "reservation"}:
        return None
    q = normalize_text(query)
    if not _has(q, "เปิด", "ปิด", "เวลา", "วัลา", "ตารางเวลา", "ตารางวัลา", "ให้บริการ", "กี่โมง", "รอบ", "ช่วงเช้า", "ช่วงบ่าย", "schedule", "hours", "morning", "afternoon", "24"):
        return None
    if _looks_like_specific_calendar_query(query) or _has(q, "ตอนนี้"):
        return None

    weekday = _detect_weekday(query)
    if _has(q, "24 ชั่วโมง", "24 ชม", "24 hours", "เปิด 24"):
        first = "ไม่ได้เปิด 24 ชั่วโมงครับ ศูนย์ใช้รอบ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมี Maintenance บางช่วง"
    elif weekday:
        has_morning = _has(q, "รอบเช้า", "ช่วงเช้า", "ตอนเช้า", "morning", "09:00", "9:00", "09 ถึง 12", "9 ถึง 12")
        has_afternoon = _has(q, "รอบบ่าย", "ช่วงบ่าย", "ตอนบ่าย", "afternoon", "13:00", "13 ถึง 16")
        if weekday == "monday" and has_morning and has_afternoon:
            first = "วันจันทร์ Morning เล่นไม่ได้/ปิด/ไม่เปิดให้จองเล่น เพราะ 09:00-12:00 เป็น Maintenance* ส่วน Afternoon เปิดให้เล่น 13:00-16:00"
        elif weekday == "friday" and has_morning and has_afternoon:
            first = "วันศุกร์ Morning เปิดให้เล่น 09:00-12:00 ส่วน Afternoon เล่นไม่ได้/ปิด/ไม่เปิดให้จองเล่น เพราะ 13:00-16:00 เป็น Maintenance"
        elif weekday == "monday" and has_morning:
            first = "วันจันทร์ Morning เล่นไม่ได้/ปิด/ไม่เปิดให้จองเล่น เพราะ 09:00-12:00 เป็น Maintenance*"
        elif weekday == "monday" and has_afternoon:
            first = "วันจันทร์ Afternoon เปิดให้เล่น 13:00-16:00"
        elif weekday == "friday" and has_afternoon:
            first = "วันศุกร์ Afternoon เล่นไม่ได้/ปิด/ไม่เปิดให้จองเล่น เพราะ 13:00-16:00 เป็น Maintenance"
        elif weekday == "friday" and has_morning:
            first = "วันศุกร์ Morning เปิดให้เล่น 09:00-12:00"
        else:
            first = f"{WEEKLY_SERVICE[weekday]['label']}: {WEEKLY_SERVICE[weekday]['summary']}"
    elif _has(q, "รอบเช้า", "ช่วงเช้า", "morning"):
        first = "รอบเช้า Morning คือ 09:00-12:00 แต่วันจันทร์ช่วงนี้เป็น Maintenance*"
    elif _has(q, "รอบบ่าย", "ช่วงบ่าย", "afternoon"):
        first = "รอบบ่าย Afternoon คือ 13:00-16:00 แต่วันศุกร์ช่วงนี้เป็น Maintenance"
    else:
        first = "เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00"

    lines = [first, "", "รายละเอียดจากตาราง:"]
    selected = {weekday: WEEKLY_SERVICE[weekday]} if weekday else WEEKLY_SERVICE
    for item in selected.values():
        slot_text = ", ".join(f"{slot['label']} {slot['time']} = {slot['status']}" for slot in item["slots"])
        lines.append(f"•    {item['label']}: {slot_text}")
    lines.append(f"แหล่งข้อมูล: {RESERVATION_URL}")
    return StructuredToolResult(
        "\n".join(lines),
        [_hit("reservation_schedule", "reservation", RESERVATION_URL, "Reservation Schedule")],
        "structured_schedule",
        0.96,
        {"tool": "get_service_schedule", "weekday": weekday or "weekly", "slots": selected},
    )


RESERVATION_FACTS = (
    {
        "key": "booking_steps",
        "aliases": (
            "วิธีจอง", "จองยังไง", "จองไง", "แล้วจองไง", "จองทำยังไง",
            "ขั้นตอนจอง", "สรุปขั้นตอนจอง", "สรุปการจอง", "how to book", "booking steps",
        ),
        "answer": (
            "ขั้นตอนจองโดยสรุป:\n"
            "•    เลือกบริการหรือโซนที่ต้องการใช้\n"
            "•    เลือกวันและรอบเวลาที่ต้องการ\n"
            "•    กรอก Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล และเบอร์โทรศัพท์\n"
            "•    ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง\n"
            "•    หลังจองต้องชำระเงินภายใน 10 นาที\n"
            "•    แนบสลิปและยืนยันการจอง"
        ),
    },
    {
        "key": "booking_advance",
        "aliases": ("จองล่วงหน้า", "ต้องจองก่อน", "จองก่อนกี่", "book advance"),
        "answer": "ต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง",
    },
    {
        "key": "booking_max_sessions",
        "aliases": ("สูงสุดกี่ session", "กี่ sessions", "จองได้กี่ session", "กี่ชั่วโมงต่อวัน", "เล่นได้กี่ชั่วโมง"),
        "answer": "การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions สำหรับ PlayStation 5: 1 session = 1 ชั่วโมง ดังนั้น 3 sessions = สูงสุด 3 ชั่วโมงต่อการจอง 1 ครั้ง",
    },
    {
        "key": "payment_timeout",
        "aliases": ("จ่ายภายในกี่นาที", "ชำระภายในกี่นาที", "หลังจองต้องจ่ายภายในกี่นาที", "หลังจองต้องชำระภายในกี่นาที", "ไม่จ่าย", "ลืมจ่าย", "ชำระ 10", "จ่าย 10"),
        "answer": "หลังจองต้องชำระเงินทันที หากไม่ชำระภายใน 10 นาที การจองจะถูกยกเลิกและต้องจองใหม่",
    },
    {
        "key": "payment_bank",
        "aliases": ("เลขบัญชี", "บัญชีธนาคาร", "โอนเงิน", "ธนาคารอะไร", "จ่ายเงินผ่านช่องทางไหน", "ชำระเงินผ่านช่องทางไหน", "ช่องทางชำระเงิน", "account number"),
        "answer": "ชำระเงินโดยโอนผ่านธนาคารไทยพาณิชย์ ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และต้องแนบสลิปการโอนเงิน",
    },
    {
        "key": "checkin_advance",
        "aliases": ("เช็คอินล่วงหน้า", "เชคอินล่วงหน้า", "เช็คอินได้กี่นาที", "checkin"),
        "answer": "เช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง",
    },
    {
        "key": "late_checkin",
        "aliases": ("ไม่เช็คอิน", "เช็คอินไม่ทัน", "เชคอินไม่ทัน", "ไปช้า", "ไปถึงช้า", "ถ้าไปช้า", "มาสาย", "late checkin"),
        "answer": "ถ้าไม่เช็คอินก่อนเวลาเริ่มต้นของรอบ ระบบจะยกเลิกการจองทันที และไม่มีการคืนเงิน",
    },
    {
        "key": "walk_in_policy",
        "aliases": ("walk in", "walk-in", "วอล์คอิน", "ไม่จองล่วงหน้า", "ไปเลยได้ไหม"),
        "answer": "ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง จึงไม่ควร walk in โดยไม่จองก่อน",
    },
    {
        "key": "cancel_booking",
        "aliases": ("ยกเลิกการจอง", "ยกเลิกจอง", "cancel booking", "แก้ไขการจอง", "แก้ข้อมูลจอง"),
        "answer": "การยกเลิกหรือแก้ไขการจองควรทำล่วงหน้าอย่างน้อย 1 ชั่วโมง หากกดจองแล้วจะแก้ข้อมูลเดิมไม่ได้ ต้องยกเลิกแล้วจองใหม่ตามเงื่อนไข",
    },
    {
        "key": "refund_policy",
        "aliases": ("คืนเงิน", "refund", "ได้เงินคืน", "ขอเงินคืน"),
        "answer": "โดยทั่วไปไม่มีการคืนเงิน ยกเว้นกรณีที่ศูนย์เป็นฝ่ายผิดพลาด เช่น อุปกรณ์ขัดข้อง หรือมีเหตุสุดวิสัยที่ทำให้ศูนย์ต้องปิดให้บริการ",
    },
    {
        "key": "transfer_booking",
        "aliases": ("โอนสิทธิ์", "จองแทนกัน", "คนอื่นใช้ booking", "transfer booking"),
        "answer": "ไม่สามารถโอนสิทธิ์การจองให้ผู้อื่นได้",
    },
)


def _reservation_answer(query: str, intent: UniversalIntent) -> StructuredToolResult | None:
    if intent.domain != "reservation":
        return None
    q = normalize_text(query)
    if _has(q, "เปิด", "ปิด", "เวลา", "กี่โมง", "รอบ", "วันนี้", "พรุ่งนี้", "วันจันทร์", "วันศุกร์"):
        return None
    best: tuple[float, int, dict[str, Any], str] | None = None
    for fact in RESERVATION_FACTS:
        ok, alias, score = contains_alias(q, list(fact["aliases"]), fuzzy=False, threshold=0.84)
        alias_length = len(normalize_text(alias).replace(" ", ""))
        if ok and (best is None or (score, alias_length) > (best[0], best[1])):
            best = (score, alias_length, fact, alias)

    match_method = "exact"
    if best is None:
        match_method = "fuzzy"
        flattened_aliases = [
            str(alias)
            for fact in RESERVATION_FACTS
            for alias in fact["aliases"]
        ]
        ok, alias, score = contains_alias(q, flattened_aliases, fuzzy=True, threshold=0.84)
        if not ok:
            return None
        owner = next(
            (
                fact for fact in RESERVATION_FACTS
                if alias in fact["aliases"]
            ),
            None,
        )
        if owner is None:
            return None
        best = (score, len(normalize_text(alias).replace(" ", "")), owner, alias)

    fact = best[2]
    fact_answer = str(fact["answer"])
    if fact["key"] == "booking_steps" and _has(q, "pc", "คอม", "computer"):
        fact_answer = "สำหรับ PC ให้เลือกบริการ/โซน PC ในระบบจอง แล้วทำตามขั้นตอนนี้ครับ\n" + fact_answer
    answer = f"{fact_answer}\nแหล่งข้อมูล: {RESERVATION_URL}"
    return StructuredToolResult(
        answer,
        [_hit(str(fact["key"]), "reservation", RESERVATION_URL, str(fact["key"]))],
        "structured_reservation_fact",
        0.94,
        {
            "tool": "get_reservation_fact",
            "fact_key": fact["key"],
            "score": best[0],
            "match_method": match_method,
            "matched_alias": best[3],
        },
    )


def _booking_services_for_game(game_name: str) -> list[dict[str, Any]]:
    target_key = _game_key(game_name)
    if not target_key:
        return []
    rows: list[dict[str, Any]] = []
    for row in _service_game_availability_rows():
        for game in row.get("games") or []:
            if _game_key(str(game)) == target_key:
                rows.append(row)
                break
    return rows


def _booking_selection_for_detected_game(query: str, game: dict[str, Any]) -> StructuredToolResult | None:
    game_name = str(game.get("game") or "").strip()
    if not game_name:
        return None
    rows = _booking_services_for_game(game_name)
    if not rows:
        return None

    q = normalize_text(query)
    if _has(q, "30 นาที", "ครึ่งชั่วโมง"):
        filtered = [row for row in rows if int(row.get("duration_minutes") or 0) == 30]
        if filtered:
            rows = filtered
    elif _has(q, "1 ชั่วโมง", "หนึ่งชั่วโมง", "60 นาที", "ชั่วโมง"):
        filtered = [row for row in rows if int(row.get("duration_minutes") or 0) == 60]
        if filtered:
            rows = filtered

    services: list[str] = []
    service_displays: list[str] = []
    zones: list[str] = []
    details: list[str] = []
    for row in rows:
        label = str(row.get("service_label") or row.get("machine_label") or row.get("zone") or "").strip()
        zone = str(row.get("zone") or "").strip()
        if label and label not in services:
            services.append(label)
        if zone and zone not in zones:
            zones.append(zone)
        display = label
        if zone and zone.lower() not in label.lower():
            display = f"{zone} - {label}"
        if display and display not in service_displays:
            service_displays.append(display)
        duration = row.get("duration_minutes")
        capacity = str(row.get("capacity_persons") or "").strip()
        suffix_parts = []
        if duration:
            suffix_parts.append(f"{duration} นาที")
        if capacity:
            suffix_parts.append(capacity)
        if label:
            detail = f"•    {display}"
            if suffix_parts:
                detail += f" ({', '.join(suffix_parts)})"
            details.append(detail)

    if not services:
        return None
    service_text = " หรือ ".join(service_displays or services)
    lines = [
        f"ถ้าจะเล่น {game_name} ให้จอง {service_text} ครับ",
        *details,
        "จากนั้นเลือกวัน รอบเวลา กรอกข้อมูลผู้ใช้บริการ ชำระเงิน และแนบสลิปเพื่อยืนยันการจอง",
        f"แหล่งข้อมูล: {RESERVATION_URL}",
    ]
    return StructuredToolResult(
        "\n".join(lines),
        _availability_source_hits(rows),
        "structured_booking_game_service_selection",
        0.97,
        {
            "tool": "get_booking_selection",
            "fact_key": "booking_selection_by_game",
            "game": game_name,
            "services": services,
            "zones": zones,
        },
    )


def _booking_selection_answer(query: str) -> StructuredToolResult | None:
    if not _looks_like_booking_selection_query(query):
        return None
    q = normalize_text(query)
    if _has(q, "กี่บาท", "ราคา", "ค่าบริการ", "เสีย", "จ่าย", "คิดเงิน", "คำนวณ"):
        return None

    lines: list[str] | None = None
    key = "booking_selection_general"
    play_access_query = _looks_like_play_access_query(query)
    booking_signal = _has(q, "จอง", "booking", "book")
    detected_booking_game = (
        _detect_game(query, allow_fuzzy=_has(q, "เกม", "game"))
        if play_access_query or booking_signal
        else None
    )
    access_query = play_access_query or (
        booking_signal and detected_booking_game is not None
    ) or (
        booking_signal and _has(q, "call of duty", "cod", "คอลออฟดิวตี้", "คอล ออฟ ดิวตี้")
    )
    if access_query:
        cod_family = _call_of_duty_booking_family_answer(query)
        if cod_family is not None:
            return cod_family
    if access_query and _looks_like_broad_mario_query(query):
        q = normalize_text(f"{query} Nintendo Switch Zone")
        lines = [
            "ถ้าจะเล่นเกมตระกูล Mario ที่มีในรายการยืนยันได้ ให้จอง Nintendo Switch Zone ครับ",
            "•    เกม Mario ที่พบมีหลายเกม เช่น Mario Kart 8 Deluxe, Mario Party Superstars, New Super Mario Bros. U Deluxe และ Super Mario Odyssey",
            "•    ถ้าเล่น 1-2 คน ให้เลือก Nintendo Switch แบบ 1-2 Persons",
            "•    ถ้าเล่น 3-4 คน ให้เลือก Nintendo Switch แบบ 3-4 Persons",
            "•    จากนั้นเลือกวัน รอบเวลา กรอกข้อมูลผู้ใช้บริการ ชำระเงิน และแนบสลิปเพื่อยืนยันการจอง",
        ]
        key = "booking_selection_mario_family"
    access_game = detected_booking_game if access_query else None
    if lines is None and access_game is not None:
        by_game_result = _booking_selection_for_detected_game(query, access_game)
        if by_game_result is not None:
            return by_game_result
    access_game_name = str(access_game.get("game") or "").strip() if access_game else ""
    access_zones = list(access_game.get("zones") or []) if access_game else []
    access_intro = ""
    if lines is not None:
        pass
    elif access_game_name and len(access_zones) == 1:
        q = normalize_text(f"{query} {access_zones[0]}")
        access_intro = f"ถ้าจะเล่น {access_game_name} ให้จอง {access_zones[0]} ครับ"
    elif access_game_name and access_zones:
        zone_text = " และ ".join(access_zones)
        lines = [
            f"ถ้าจะเล่น {access_game_name} ให้เลือกบริการหรือโซนที่ตรงกับเกมนี้: {zone_text} ครับ",
            "•    จากนั้นเลือกวัน รอบเวลา กรอกข้อมูลผู้ใช้บริการ ชำระเงิน และแนบสลิปเพื่อยืนยันการจอง",
        ]
    if lines is None and _has(q, "nintendo", "switch", "นินเทนโด", "สวิตช์", "สวิทช์"):
        key = "booking_selection_nintendo"
        lines = [
            "จอง Nintendo Switch ต้องเลือกบริการตามจำนวนผู้เล่นครับ",
            "•    ถ้าเล่น 1-2 คน ให้เลือก Nintendo Switch แบบ 1-2 Persons",
            "•    ถ้าเล่น 3-4 คน ให้เลือก Nintendo Switch แบบ 3-4 Persons",
            "•    จากนั้นเลือกวัน รอบเวลา กรอกข้อมูลผู้ใช้บริการ ชำระเงิน และแนบสลิปเพื่อยืนยันการจอง",
        ]
    elif lines is None and _has(q, "cockpit", "ค็อกพิท", "คอกพิท", "พวงมาลัย", "ขับรถ"):
        key = "booking_selection_cockpit"
        lines = [
            "ถ้าอยากเล่นเกมขับรถหรือใช้พวงมาลัย ให้จอง Cockpit Zone / Cockpit ครับ",
            "•    โซนนี้ใช้กับชุด Racezone Full Cockpit V3 และ Logitech G923 TRUEFORCE Racing Wheel",
            "•    เกมที่ยืนยันได้คือ Gran Turismo 7",
        ]
    elif lines is None and _has(q, "ps5", "playstation", "เพลย์", "เพลย์ห้า"):
        key = "booking_selection_ps5"
        lines = [
            "จอง PlayStation 5 ต้องเลือกบริการ PlayStation 5 และเลือกรอบเวลาที่ต้องการครับ",
            "•    ข้อมูลค่าบริการที่มีระบุ PlayStation 5 ต่อ 60 นาที สำหรับ 1-2 คน",
            "•    จากนั้นกรอกข้อมูลผู้ใช้บริการ ชำระเงิน และแนบสลิปเพื่อยืนยันการจอง",
        ]
    elif lines is None and _has(q, "vr", "วีอาร์", "แว่น"):
        key = "booking_selection_vr"
        lines = [
            "ถ้าต้องการเล่น VR ให้เลือกบริการหรือโซน VR ตามที่ระบบจองเปิดให้เลือกครับ",
            "•    โซนนี้เกี่ยวข้องกับ PlayStation VR2 และ PlayStation 5 Slim",
            "•    จากนั้นเลือกวัน รอบเวลา กรอกข้อมูลผู้ใช้บริการ ชำระเงิน และแนบสลิปเพื่อยืนยันการจอง",
        ]
    elif lines is None and _has(q, "เลือกอะไร", "ต้องเลือก", "ต้องระบุ", "จำนวนผู้เล่น"):
        lines = [
            "ตอนจองต้องเลือกบริการหรือโซน วัน และรอบเวลาที่ต้องการครับ",
            "•    บางบริการต้องเลือกจำนวนผู้เล่น เช่น Nintendo Switch แบบ 1-2 Persons หรือ 3-4 Persons",
            "•    จากนั้นกรอกข้อมูลผู้ใช้บริการ ชำระเงิน และแนบสลิปเพื่อยืนยันการจอง",
        ]
    elif lines is None and access_query:
        lines = [
            "ถ้าจะเข้าใช้บริการเพื่อเล่นเกมที่ PSU Esports Studio - Phuket ต้องจองผ่านระบบก่อนครับ",
            "•    เลือกบริการหรือโซนที่ต้องการใช้",
            "•    เลือกวันและรอบเวลา กรอกข้อมูลผู้ใช้บริการ ชำระเงิน และแนบสลิปเพื่อยืนยันการจอง",
        ]

    if not lines:
        return None
    if access_intro:
        lines = [access_intro, *lines]
    lines.append(f"แหล่งข้อมูล: {RESERVATION_URL}")
    return StructuredToolResult(
        "\n".join(lines),
        [_hit(key, "reservation", RESERVATION_URL, key)],
        "structured_booking_selection",
        0.96,
        {"tool": "get_booking_selection", "fact_key": key},
    )


def _looks_like_broad_mario_query(query: str) -> bool:
    q = normalize_text(query)
    if "mario" not in q and "มาริโอ" not in q:
        return False
    specific_terms = (
        "kart",
        "live",
        "home circuit",
        "party",
        "superstars",
        "odyssey",
        "bros",
        "deluxe",
    )
    return not any(term in q for term in specific_terms)


def _call_of_duty_booking_family_answer(query: str) -> StructuredToolResult | None:
    q = normalize_text(query)
    if not _has(q, "call of duty", "cod", "คอลออฟดิวตี้", "คอล ออฟ ดิวตี้"):
        return None
    if _has(q, "warzone", "วอร์โซน", "modern warfare", "mw3", "mwiii", "มอดเดิร์น"):
        return None

    rows = list(_service_game_availability_rows())
    family: dict[str, list[str]] = {}
    for row in rows:
        for game in row.get("games") or []:
            game_name = str(game)
            if "call of duty" in normalize_text(game_name):
                family.setdefault(game_name, []).append(str(row.get("service_label")))
    if not family:
        return None

    lines = ["Call of Duty ในข้อมูลตอนนี้มีมากกว่า 1 เกมครับ ต้องเลือกให้ตรงกับเกมที่จะเล่น"]
    for game_name, services in sorted(family.items()):
        lines.append(f"•    ถ้าหมายถึง {game_name} ให้จอง {', '.join(services)}")
    lines.append("พิมพ์ต่อได้เลยว่า Warzone หรือ Modern Warfare III ถ้าต้องการให้ช่วยเจาะจง")
    lines.append(f"แหล่งข้อมูล: {RESERVATION_URL}")
    return StructuredToolResult(
        "\n".join(lines),
        _availability_source_hits(rows),
        "structured_booking_game_family_clarification",
        0.94,
        {"tool": "get_booking_selection", "fact_key": "booking_selection_call_of_duty_family"},
    )


def _control_values_match(query: str, values: dict[str, list[str]]) -> bool:
    q_norm = normalize_text(query)
    q_tokens = set(re.findall(r"[0-9a-z+.-]+|[\u0E00-\u0E7F]+", q_norm))

    for button in values.get("button", []):
        button_norm = normalize_text(button)
        button_compact = _compact(button)
        if not button_compact:
            continue
        if len(button_compact) <= 2:
            if button_norm in q_tokens or f"ปุ่ม{button_norm}" in q_norm or f"ปุ่ม {button_norm}" in q_norm:
                return True
            continue
        if button_norm in q_norm:
            return True

    semantic_values = [value for value in values.get("action", []) if value]
    for value in semantic_values:
        value_norm = normalize_text(value)
        if value_norm and value_norm in q_norm:
            return True
        if _semantic_overlap_match(q_norm, value_norm):
            return True
        for phrase in _significant_query_phrases(q_norm):
            if phrase in value_norm:
                return True
    return False


def _semantic_overlap_match(q_norm: str, value_norm: str) -> bool:
    q_compact = _compact(q_norm)
    value_compact = _compact(value_norm)
    if len(value_compact) < 4:
        return False
    blocked = {"ปุ่ม", "กดอะไร", "อะไร", "บังคับ", "คำสั่ง", "รายละเอียด"}
    for length in range(min(len(value_compact), 10), 3, -1):
        for start in range(0, len(value_compact) - length + 1):
            piece = value_compact[start:start + length]
            if piece in blocked:
                continue
            if piece and piece in q_compact:
                return True
    return False


def _significant_query_phrases(q_norm: str) -> list[str]:
    stop = {
        "ปุ่ม", "กด", "กดอะไร", "อะไร", "ไหน", "มี", "บ้าง", "ทั้งหมด", "เกม", "controller", "controls",
        "tekken", "mario", "kart", "live", "home", "circuit", "deluxe", "call", "duty",
    }
    chunks = re.findall(r"[0-9a-z+.-]+|[\u0E00-\u0E7F]+", q_norm)
    phrases: list[str] = []
    for chunk in chunks:
        if chunk in stop or len(_compact(chunk)) < 4:
            continue
        phrases.append(chunk)
    for i in range(len(chunks) - 1):
        phrase = f"{chunks[i]}{chunks[i + 1]}"
        if len(_compact(phrase)) >= 4 and chunks[i] not in stop and chunks[i + 1] not in stop:
            phrases.append(phrase)
    return list(dict.fromkeys(phrases))


def answer_with_structured_tool(
    query: str,
    route: PipelineRoute,
    intent: UniversalIntent | None,
    *,
    started: float,
) -> StructuredToolResult | None:
    if intent is None:
        return None

    booking_first = _looks_like_play_access_query(query) or _has(
        normalize_text(query),
        "จอง",
        "booking",
        "book",
        "เลือกบริการ",
        "ต้องเลือก",
        "ต้องระบุ",
        "รอบเวลา",
        "ต้องจอง",
    )
    booking_selection_result = _booking_selection_answer(query) if booking_first else None
    if booking_selection_result is not None:
        return StructuredToolResult(
            answer=booking_selection_result.answer,
            hits=booking_selection_result.hits,
            mode=booking_selection_result.mode,
            confidence=booking_selection_result.confidence,
            evidence={**booking_selection_result.evidence, "elapsed": round(time.perf_counter() - started, 4)},
        )

    if intent.domain == "games":
        family_result = _game_family_answer(query)
        if family_result is not None:
            return StructuredToolResult(
                answer=family_result.answer,
                hits=family_result.hits,
                mode=family_result.mode,
                confidence=family_result.confidence,
                evidence={**family_result.evidence, "elapsed": round(time.perf_counter() - started, 4)},
            )

    structured_scope = (
        intent.domain
        if intent.domain not in {"", "unknown", "general"}
        else route.category
    )
    # Ranking is a narrower operation than a generic zone/game availability
    # lookup, so it must get first refusal when both signals are present.
    ranking_result = _game_zone_ranking_answer(query) if structured_scope == "games" else None
    if ranking_result is not None:
        return StructuredToolResult(
            answer=ranking_result.answer,
            hits=ranking_result.hits,
            mode=ranking_result.mode,
            confidence=ranking_result.confidence,
            evidence={**ranking_result.evidence, "elapsed": round(time.perf_counter() - started, 4)},
        )

    availability_result = (
        _service_game_availability_answer(query, intent)
        if structured_scope in {"games", "reservation"}
        else None
    )
    if availability_result is not None:
        return StructuredToolResult(
            answer=availability_result.answer,
            hits=availability_result.hits,
            mode=availability_result.mode,
            confidence=availability_result.confidence,
            evidence={**availability_result.evidence, "elapsed": round(time.perf_counter() - started, 4)},
        )

    booking_selection_result = (
        _booking_selection_answer(query)
        if intent.domain == "reservation" or route.category == "reservation"
        else None
    )
    if booking_selection_result is not None:
        return StructuredToolResult(
            answer=booking_selection_result.answer,
            hits=booking_selection_result.hits,
            mode=booking_selection_result.mode,
            confidence=booking_selection_result.confidence,
            evidence={**booking_selection_result.evidence, "elapsed": round(time.perf_counter() - started, 4)},
        )

    domain = intent.domain
    if route.category == "competition_rules" and domain == "games" and _looks_like_competition_rule_query(query):
        return None
    if domain == "equipment" and _looks_like_booking_selection_query(query):
        return None

    if domain == "members" or route.category == "members":
        result = _member_answer(query, intent)
    elif _looks_like_control_or_gameplay_query(query):
        if domain == "games" and not _looks_like_explicit_control_query(query):
            game_result = _game_answer(query, intent)
            if game_result is not None and "วิธีเล่นโดยสรุป:" in game_result.answer:
                result = game_result
            else:
                result = _control_answer(query, intent) or game_result
        else:
            result = _control_answer(query, intent)
    elif domain == "game_controls":
        result = _control_answer(query, intent)
    elif domain == "games":
        result = _game_answer(query, intent)
    elif domain == "equipment" or route.category == "equipment":
        result = _equipment_answer(query, intent)
    elif domain == "service_fee" or route.category == "service_fee":
        result = _service_fee_answer(query, intent)
    elif domain == "schedule" or route.category == "schedule":
        result = _schedule_answer(query, intent)
    elif domain == "reservation" or route.category == "reservation":
        result = _schedule_answer(query, intent) or _reservation_answer(query, intent)
    else:
        result = None

    if result is None:
        return None
    return StructuredToolResult(
        answer=result.answer,
        hits=result.hits,
        mode=result.mode,
        confidence=result.confidence,
        evidence={**result.evidence, "elapsed": round(time.perf_counter() - started, 4)},
    )
