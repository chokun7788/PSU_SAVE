from __future__ import annotations

import json
import re
import time
import unicodedata
from dataclasses import dataclass
from datetime import date, timedelta
from functools import lru_cache
from pathlib import Path

from app.calendar.service_calendar import (
    closure_for,
    closures_for_month,
    closures_for_year,
    current_service_slot,
    format_thai_date,
    has_date_or_holiday_intent,
    holidays_for_date,
    holidays_for_month,
    holidays_for_year,
    next_holidays,
    now_bangkok,
    regular_service_summary,
    resolve_date_from_text,
    resolve_month_from_text,
    resolve_year_from_text,
    THAI_HOLIDAY_SOURCE_URL,
    thai_weekday_name,
    today_bangkok,
)
from app.calculator.service_fee import SOURCE_URL as SERVICE_FEE_URL
from app.core.normalization import CUSTOMER_GROUP_ALIASES, contains_alias, detect_from_aliases, normalize_text
from app.core.source_registry import (
    PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID,
    SERVICE_FEE_IMAGE_2026_ID,
    make_source_hit,
)
from app.pipeline.chatbot_role import CHATBOT_NAME_TH, CHATBOT_ORG_TH
from app.rules.matcher import RuleMatcher


RESERVATION_URL = "https://esports.computing.psu.ac.th/reservation"
HOME_URL = "https://esports.phuket.psu.ac.th/home"
CONTACT_URL = "https://esports.computing.psu.ac.th/contact-us"
KNOWLEDGE_URL = "https://esports.computing.psu.ac.th/knowledge"
NEWS_URL = "https://esports.computing.psu.ac.th/events-news/news"
MEMBERS_URL = "https://esports.phuket.psu.ac.th/about-us/Members"
OUR_GAMES_URL = "https://esports.phuket.psu.ac.th/Services/our-games"
EQUIPMENT_HOW_TO_URL = "https://esports.phuket.psu.ac.th/Services/how-to-use-equipment-in-studio"
POPULAR_GAMES_KNOWLEDGE_URL = "https://esports.phuket.psu.ac.th/Knowledge/%E0%B9%80%E0%B8%81%E0%B8%A1%E0%B8%97%E0%B8%99%E0%B8%A2%E0%B8%A1%E0%B9%83%E0%B8%99%E0%B8%9B%E0%B8%88%E0%B8%88%E0%B8%9A%E0%B8%99"
ESPORTS_GAME_TYPES_URL = "https://esports.phuket.psu.ac.th/Knowledge/%E0%B8%9B%E0%B8%A3%E0%B8%B0%E0%B9%80%E0%B8%A0%E0%B8%97%E0%B9%80%E0%B8%81%E0%B8%A1%E0%B8%97%E0%B8%99%E0%B8%A2%E0%B8%A1%E0%B9%83%E0%B8%99%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%81%E0%B8%82%E0%B8%87%E0%B8%82%E0%B8%99%E0%B8%AD%E0%B8%AA%E0%B8%9B%E0%B8%AD%E0%B8%A3%E0%B8%95"

ROOT_DIR = Path(__file__).resolve().parents[2]
GAME_TITLE_ALIASES_PATH = ROOT_DIR / "data" / "curated" / "game_title_aliases.jsonl"
GAME_ITEM_DETAILS_PATH = ROOT_DIR / "data" / "curated" / "game_item_details.jsonl"
OUR_GAMES_SCRAPED_DETAILS_PATH = ROOT_DIR / "data" / "curated" / "our_games_scraped_details.jsonl"
GAME_CONTROL_FACTS_PATH = ROOT_DIR / "data" / "curated" / "game_control_facts.jsonl"
SERVICE_GAME_AVAILABILITY_PATH = ROOT_DIR / "data" / "curated" / "service_game_availability.jsonl"
MEMBER_PROFILES_PATH = ROOT_DIR / "data" / "curated" / "member_profiles.jsonl"


def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows: list[dict] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _compact_key(value: str) -> str:
    return re.sub(r"[^0-9a-z\u0E00-\u0E7F]+", "", normalize_text(value))


def _game_control_key(value: str) -> str:
    clean = (value or "").replace("™", "").replace("®", "")
    clean = unicodedata.normalize("NFKD", clean).encode("ascii", "ignore").decode("ascii")
    clean = re.sub(r"\bstandard edition\b", "", clean, flags=re.IGNORECASE)
    clean = re.sub(r"\(\s*remake\s*\)", "", clean, flags=re.IGNORECASE)
    clean = re.sub(r"\bremake\b", "", clean, flags=re.IGNORECASE)
    clean = re.sub(r"\(\s*remastered\s*\)", "", clean, flags=re.IGNORECASE)
    clean = re.sub(r"\bremastered\b", "", clean, flags=re.IGNORECASE)
    return _compact_key(clean)


def _zone_from_source_section(value: str) -> str:
    normalized = normalize_text(value)
    if "nintendo" in normalized or "switch" in normalized:
        return "Nintendo Switch Zone"
    if "playstation" in normalized or "ps5" in normalized:
        return "PlayStation 5 Zone"
    if "cockpit" in normalized:
        return "Cockpit Zone"
    if "vr" in normalized:
        return "VR Zone"
    if "pc" in normalized:
        return "PC Zone"
    return ""


def _zone_from_control_platform(value: str) -> str:
    normalized = normalize_text(value)
    if "nintendo" in normalized or "switch" in normalized:
        return "Nintendo Switch Zone"
    if "playstation" in normalized or "ps5" in normalized:
        return "PlayStation 5 Zone"
    if "pc" in normalized:
        return "PC Zone"
    return ""


def _merge_unique(current: list[str], values: list[str]) -> list[str]:
    for value in values:
        text = str(value or "").strip()
        if text and text not in current:
            current.append(text)
    return current


@lru_cache(maxsize=1)
def _service_game_availability_rows() -> tuple[dict, ...]:
    return tuple(_read_jsonl(SERVICE_GAME_AVAILABILITY_PATH))


@lru_cache(maxsize=1)
def _verified_game_catalog() -> tuple[dict, ...]:
    availability_rows = _service_game_availability_rows()
    if availability_rows:
        detail_rows = _read_jsonl(GAME_ITEM_DETAILS_PATH) + _read_jsonl(OUR_GAMES_SCRAPED_DETAILS_PATH)
        details_by_key: dict[str, dict] = {}
        aliases_by_key: dict[str, list[str]] = {}
        for row in detail_rows + _read_jsonl(GAME_TITLE_ALIASES_PATH):
            name = str(row.get("game") or row.get("title") or "").strip()
            if not name:
                continue
            keys = [_compact_key(name)]
            alias_values = [name, *[str(alias) for alias in row.get("aliases") or []]]
            for alias in alias_values:
                key = _compact_key(alias)
                if key:
                    keys.append(key)
            for key in keys:
                if key:
                    details_by_key.setdefault(key, row)
                    aliases_by_key.setdefault(key, [])
                    _merge_unique(aliases_by_key[key], alias_values)

        current: dict[str, dict] = {}
        for service in availability_rows:
            zone = str(service.get("zone") or "").strip()
            source_url = str(service.get("source_url") or RESERVATION_URL)
            for game in service.get("games") or []:
                name = str(game).strip()
                if not name:
                    continue
                key = _compact_key(name)
                detail = details_by_key.get(key, {})
                entry = current.setdefault(
                    key,
                    {
                        "name": name,
                        "zones": [],
                        "genre": str(detail.get("genre") or ""),
                        "summary": str(detail.get("summary_th") or detail.get("text") or ""),
                        "how": str(detail.get("how_to_play_th") or ""),
                        "source_url": str(detail.get("source_url") or source_url),
                        "aliases": [],
                    },
                )
                _merge_unique(entry["zones"], [zone])
                _merge_unique(entry["aliases"], [name, *aliases_by_key.get(key, [])])
        return tuple(
            {
                **entry,
                "zones": tuple(entry["zones"]),
                "aliases": tuple(entry["aliases"] or [entry["name"]]),
            }
            for entry in sorted(current.values(), key=lambda item: str(item["name"]).lower())
        )

    details_by_alias: dict[str, dict] = {}
    for row in _read_jsonl(GAME_ITEM_DETAILS_PATH):
        aliases = [str(row.get("game") or row.get("title") or "")]
        aliases.extend(str(alias) for alias in row.get("aliases") or [])
        for alias in aliases:
            key = _compact_key(alias)
            if key:
                details_by_alias[key] = row

    scraped_by_alias: dict[str, dict] = {}
    for row in _read_jsonl(OUR_GAMES_SCRAPED_DETAILS_PATH):
        aliases = [str(row.get("game") or row.get("title") or "")]
        aliases.extend(str(alias) for alias in row.get("aliases") or [])
        for alias in aliases:
            key = _compact_key(alias)
            if key:
                scraped_by_alias[key] = row

    control_zones: dict[str, list[str]] = {}
    for row in _read_jsonl(GAME_CONTROL_FACTS_PATH):
        game = str(row.get("game") or "").strip()
        zone = _zone_from_control_platform(str(row.get("platform") or ""))
        if game and zone:
            control_zones.setdefault(_compact_key(game), [])
            _merge_unique(control_zones[_compact_key(game)], [zone])

    entries: list[dict] = []
    seen_names: set[str] = set()
    for alias_row in _read_jsonl(GAME_TITLE_ALIASES_PATH):
        name = str(alias_row.get("game") or "").strip()
        if not name or name in seen_names:
            continue
        seen_names.add(name)
        alias_values = [name, *[str(alias) for alias in alias_row.get("aliases") or []]]
        keys = [_compact_key(alias) for alias in alias_values if _compact_key(alias)]
        detail = next((details_by_alias[key] for key in keys if key in details_by_alias), None)
        scraped = next((scraped_by_alias[key] for key in keys if key in scraped_by_alias), None)

        zones: list[str] = []
        if detail:
            _merge_unique(zones, [str(zone) for zone in detail.get("zones") or []])
        if scraped:
            _merge_unique(zones, [_zone_from_source_section(str(scraped.get("listed_under") or scraped.get("source_section") or ""))])
        for key in keys:
            _merge_unique(zones, control_zones.get(key, []))
        if not zones:
            zones = ["ไม่ระบุโซน"]

        entries.append({
            "name": name,
            "zones": tuple(zones),
            "genre": str((detail or {}).get("genre") or ""),
            "summary": str((detail or scraped or {}).get("summary_th") or ""),
            "how": str((detail or {}).get("how_to_play_th") or ""),
            "source_url": str((detail or scraped or {}).get("source_url") or OUR_GAMES_URL),
            "aliases": tuple(alias_values),
        })
    return tuple(entries)


def _catalog_entries_by_zone() -> dict[str, list[dict]]:
    by_zone = {zone: [] for zone in CATALOG_ZONE_LABELS}
    for entry in _verified_game_catalog():
        for zone in entry["zones"]:
            if zone in by_zone and entry not in by_zone[zone]:
                by_zone[zone].append(entry)
    return by_zone


def _hit(source_id: str, category: str, url: str, title: str = "") -> dict:
    return {
        "id": source_id,
        "metadata": {
            "source_url": url,
            "category": category,
            "title": title or source_id,
            "source_ids": [source_id],
        },
    }


HITS = {
    "reservation": [_hit("Reservation", "reservation", RESERVATION_URL, "Reservation")],
    "penalty": [_hit("Reservation", "penalty", RESERVATION_URL, "Reservation - damage and penalty policy")],
    "service_fee": [make_source_hit(SERVICE_FEE_IMAGE_2026_ID)],
    "service_fee_pc": [
        make_source_hit(SERVICE_FEE_IMAGE_2026_ID),
        make_source_hit(PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID),
    ],
    "home": [_hit("home", "home", HOME_URL, "Home")],
    "contact": [_hit("Contact", "contact", CONTACT_URL, "Contact")],
    "knowledge": [_hit("Knowledge", "knowledge", KNOWLEDGE_URL, "Knowledge")],
    "knowledge_popular_games": [_hit("popular_games", "knowledge", POPULAR_GAMES_KNOWLEDGE_URL, "เกมที่นิยมในปัจจุบัน")],
    "knowledge_game_types": [_hit("esports_game_types", "knowledge", ESPORTS_GAME_TYPES_URL, "ประเภทเกมที่นิยมในการแข่งขันอีสปอร์ต")],
    "equipment_how_to": [_hit("equipment_how_to", "equipment", EQUIPMENT_HOW_TO_URL, "How to Use Equipment in Studio")],
    "news": [_hit("News", "events_news", NEWS_URL, "News")],
    "members": [_hit("Members", "about_us", MEMBERS_URL, "Members")],
    "competition_rules": [_hit("competition_rules", "competition_rules", "data/competition_rules", "Competition Rules")],
    "our_games": [
        _hit("our_games", "games", OUR_GAMES_URL, "Our Games"),
        _hit("Reservation", "reservation", RESERVATION_URL, "Reservation"),
    ],
    "home_our_games": [
        _hit("home", "home", HOME_URL, "Home"),
        _hit("our_games", "games", OUR_GAMES_URL, "Our Games"),
    ],
}


SERVICE_FEE_SUMMARY = """ตาราง Service Fee 2026

PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 50 บาท
•    General Adult: 150 บาท

Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 50 บาท
•    General Adult: 140 บาท

Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 100 บาท
•    General Adult: 280 บาท

Cockpit 60 นาที (1 ชั่วโมง, 1 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 65 บาท
•    General Adult: 200 บาท

VR 30 นาที (1-5 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 190 บาท
•    General Adult: 525 บาท

VR 1 ชั่วโมง (60 นาที, 1-5 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 375 บาท
•    General Adult: 1,050 บาท

PC 1 ชั่วโมง (1 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 25 บาท
•    General Adult: 70 บาท
หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27"""


PRICE_ROWS = {
    "pc": "PC 1 ชั่วโมง (1 คน)\n•    PSU Student and Staff: 0 บาท\n•    PSU Alumni and General Student: 25 บาท\n•    General Adult: 70 บาท\nหมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27",
    "ps5": "PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน)\n•    PSU Student and Staff: 0 บาท\n•    PSU Alumni and General Student: 50 บาท\n•    General Adult: 150 บาท",
    "switch_1_2": "Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง)\n•    PSU Student and Staff: 0 บาท\n•    PSU Alumni and General Student: 50 บาท\n•    General Adult: 140 บาท",
    "switch_3_4": "Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง)\n•    PSU Student and Staff: 0 บาท\n•    PSU Alumni and General Student: 100 บาท\n•    General Adult: 280 บาท",
    "cockpit": "Cockpit 60 นาที (1 ชั่วโมง, 1 คน)\n•    PSU Student and Staff: 0 บาท\n•    PSU Alumni and General Student: 65 บาท\n•    General Adult: 200 บาท",
    "vr_30": "VR 30 นาที (1-5 คน)\n•    PSU Student and Staff: 0 บาท\n•    PSU Alumni and General Student: 190 บาท\n•    General Adult: 525 บาท",
    "vr_60": "VR 1 ชั่วโมง (60 นาที, 1-5 คน)\n•    PSU Student and Staff: 0 บาท\n•    PSU Alumni and General Student: 375 บาท\n•    General Adult: 1,050 บาท",
}

PRICE_VALUES = {
    "pc": {"psu": 0, "general_student": 25, "adult": 70},
    "ps5": {"psu": 0, "general_student": 50, "adult": 150},
    "switch_1_2": {"psu": 0, "general_student": 50, "adult": 140},
    "switch_3_4": {"psu": 0, "general_student": 100, "adult": 280},
    "cockpit": {"psu": 0, "general_student": 65, "adult": 200},
    "vr_30": {"psu": 0, "general_student": 190, "adult": 525},
    "vr_60": {"psu": 0, "general_student": 375, "adult": 1050},
}

PRICE_LABELS = {
    "pc": "PC 1 ชั่วโมง",
    "ps5": "PlayStation 5 60 นาที",
    "switch_1_2": "Nintendo Switch 1-2 คน 60 นาที",
    "switch_3_4": "Nintendo Switch 3-4 คน 60 นาที",
    "cockpit": "Cockpit 60 นาที",
    "vr_30": "VR 30 นาที",
    "vr_60": "VR 1 ชั่วโมง",
}

GROUP_NAMES = {
    "psu": "PSU Student and Staff",
    "general_student": "PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน",
    "adult": "General Adult / บุคคลทั่วไป",
}

SUPPORTED_GAME_CATALOG = {
    "VALORANT": {
        "zones": ("PC Zone",),
        "aliases": ("valorant", "วาโล", "valo", "วาโลแรนท์", "วาโลแรน"),
    },
    "Counter-Strike 2": {
        "zones": ("PC Zone",),
        "aliases": ("counter-strike 2", "counter strike 2", "counter-strike", "counter strike", "cs2", "cs 2"),
    },
    "PUBG: BATTLEGROUNDS": {
        "zones": ("PC Zone",),
        "aliases": ("pubg", "battlegrounds"),
    },
    "Call of Duty: Warzone": {
        "zones": ("PC Zone",),
        "aliases": ("warzone", "call of duty warzone"),
    },
    "League of Legends": {
        "zones": ("PC Zone",),
        "aliases": ("league of legends", "lol"),
    },
    "TEKKEN 8": {
        "zones": ("PC Zone", "PlayStation 5 Zone"),
        "aliases": ("tekken 8", "tekken", "เทคเคน", "เทคเคน 8", "เทคเคน8", "เทกเคน"),
    },
    "Marvel's Spider-Man 2": {
        "zones": ("PlayStation 5 Zone",),
        "aliases": ("spider-man", "spider man", "spider", "สไปเดอร์"),
    },
    "Fortnite": {
        "zones": ("PlayStation 5 Zone",),
        "aliases": ("fortnite", "ฟอร์ทไนท์"),
    },
    "God of War Ragnarok": {
        "zones": ("PlayStation 5 Zone",),
        "aliases": ("god of war", "ragnarok"),
    },
    "Mario Kart 8 Deluxe": {
        "zones": ("Nintendo Switch Zone",),
        "aliases": ("mario kart", "มาริโอคาร์ท"),
    },
    "Overcooked 2": {
        "zones": ("Nintendo Switch Zone",),
        "aliases": ("overcooked 2", "overcooked"),
    },
    "Super Smash Bros Ultimate": {
        "zones": ("Nintendo Switch Zone",),
        "aliases": ("super smash", "smash bros", "smash"),
    },
    "Nintendo Switch Sports": {
        "zones": ("Nintendo Switch Zone",),
        "aliases": ("switch sports", "nintendo switch sports"),
    },
    "Beat Saber": {
        "zones": ("VR Zone",),
        "aliases": ("beat saber",),
    },
    "Horizon Call of the Mountain": {
        "zones": ("VR Zone",),
        "aliases": ("horizon call of the mountain", "horizon"),
    },
    "Gran Turismo 7": {
        "zones": ("Cockpit Zone",),
        "aliases": ("gran turismo 7", "gran turismo", "gt7"),
    },
}


GAME_DETAILS = {
    "rov": {
        "name": "RoV / Arena of Valor",
        "aliases": ("rov", "arena of valor", "aov", "อาร์โอวี", "อาโอวี", "เอโอวี", "เกมตีป้อม"),
        "zones": ("มีข้อมูลกติกาการแข่งขัน แต่ยังไม่พบในรายการเกมให้เล่นของศูนย์",),
        "genre": "เกม MOBA แบบทีม",
        "summary": "RoV หรือ Arena of Valor คือเกม MOBA บนมือถือที่ผู้เล่นแบ่งเป็นทีม เลือกฮีโร่ และร่วมกันทำลายป้อม/ฐานของฝ่ายตรงข้าม",
        "how": "โดยทั่วไปผู้เล่นต้องเลือกตำแหน่งและฮีโร่ให้เหมาะกับทีม เก็บเลเวล คุมแผนที่ ช่วยทีมไฟต์ และดันเลนเพื่อทำลายฐานคู่แข่ง ในฐานข้อมูลของศูนย์มีข้อมูลฝั่งกติกาการแข่งขัน แต่ยังไม่พบว่าอยู่ในรายการเกมให้เล่นของศูนย์",
        "source": "competition_rules",
    },
    "minecraft": {
        "name": "Minecraft",
        "aliases": ("minecraft", "มายคราฟ", "ไมน์คราฟต์", "ไมน์คราฟ"),
        "zones": ("ยังไม่พบในรายการเกมให้เล่นของศูนย์",),
        "genre": "เกม Sandbox / Survival / Creative",
        "summary": "Minecraft คือเกมแซนด์บ็อกซ์ที่ผู้เล่นสำรวจโลกบล็อก ขุดทรัพยากร สร้างสิ่งปลูกสร้าง คราฟต์ของ และเลือกเล่นได้ทั้งแนวเอาชีวิตรอดหรือสร้างสรรค์",
        "how": "โดยทั่วไปเริ่มจากเก็บทรัพยากร สร้างเครื่องมือ สร้างที่พัก สำรวจโลก และตั้งเป้าหมายเอง เช่น เอาชีวิตรอด สร้างเมือง เล่นกับเพื่อน หรือทำมินิเกม หมายเหตุ: คำอธิบายนี้เป็นความรู้ทั่วไปของเกม ไม่ใช่ข้อมูลยืนยันว่าเกมนี้มีให้เล่นในศูนย์",
        "source": "our_games",
    },
    "valorant": {
        "name": "VALORANT",
        "aliases": ("valorant", "วาโล", "valo", "วาโลแรนท์", "วาโลแรน"),
        "zones": ("PC Zone",),
        "genre": "เกมยิง Tactical FPS แบบทีม 5v5",
        "summary": "VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ",
        "how": "ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือกู้ Spike การเล่นเน้นการเล็ง การสื่อสาร การใช้สกิล และการเล่นเป็นทีม",
        "source": "reservation",
    },
    "cs2": {
        "name": "Counter-Strike 2",
        "aliases": ("counter-strike 2", "counter strike 2", "counter-strike", "counter strike", "cs2", "cs 2", "เคาเตอร์"),
        "zones": ("PC Zone",),
        "genre": "เกมยิง Tactical FPS",
        "summary": "Counter-Strike 2 คือเกมยิงแข่งขันแบบทีมที่แบ่งเป็นฝ่ายบุกและฝ่ายรับ โดยมีเป้าหมายหลักเกี่ยวกับการวาง/กู้ระเบิดหรือจัดการฝ่ายตรงข้าม",
        "how": "เล่นเป็นรอบ ๆ ต้องซื้ออาวุธ วางแผนกับทีม คุมพื้นที่ และใช้การเล็งกับการสื่อสารเพื่อชนะรอบ",
        "source": "reservation",
    },
    "pubg": {
        "name": "PUBG: BATTLEGROUNDS",
        "aliases": ("pubg", "battlegrounds", "พับจี"),
        "zones": ("PC Zone",),
        "genre": "เกม Battle Royale",
        "summary": "PUBG: BATTLEGROUNDS คือเกมเอาชีวิตรอดที่ผู้เล่นลงสนาม ค้นหาอาวุธและอุปกรณ์ แล้วพยายามอยู่รอดเป็นคนหรือทีมสุดท้าย",
        "how": "เลือกจุดลง หาอาวุธ เข้าโซนปลอดภัย วางตำแหน่ง และต่อสู้กับทีมอื่นจนเหลือผู้ชนะท้ายเกม",
        "source": "reservation",
    },
    "warzone": {
        "name": "Call of Duty: Warzone",
        "aliases": ("warzone", "call of duty warzone", "cod warzone"),
        "zones": ("PC Zone",),
        "genre": "เกมยิง Battle Royale",
        "summary": "Call of Duty: Warzone คือเกมยิงแนว Battle Royale ที่เน้นการยิงรวดเร็ว การเก็บอุปกรณ์ และการเอาตัวรอดในแผนที่ขนาดใหญ่",
        "how": "ลงพื้นที่ หาอาวุธ ใช้ loadout/อุปกรณ์ช่วยทีม เคลื่อนตามวง และพยายามอยู่รอดจนจบเกม",
        "source": "reservation",
    },
    "league_of_legends": {
        "name": "League of Legends",
        "aliases": ("league of legends", "lol", "league", "ลีกออฟ"),
        "zones": ("PC Zone",),
        "genre": "เกม MOBA แบบทีม 5v5",
        "summary": "League of Legends คือเกมวางแผนต่อสู้แบบทีม ผู้เล่นเลือก Champion และร่วมกันทำลายฐานหลักของฝ่ายตรงข้าม",
        "how": "แบ่งเลน ฟาร์มเงินและเลเวล คุม objective ช่วยทีมไฟต์ และดันเข้าไปทำลาย Nexus ของศัตรู",
        "source": "reservation",
    },
    "tekken_8": {
        "name": "TEKKEN 8",
        "aliases": ("tekken 8", "tekken", "เทคเคน", "เทคเคน 8", "เทคเคน8", "เทกเคน"),
        "zones": ("PC Zone", "PlayStation 5 Zone"),
        "genre": "เกมต่อสู้ 1v1",
        "summary": "TEKKEN 8 คือเกมต่อสู้แบบตัวต่อตัว ผู้เล่นเลือกตัวละครแล้วใช้คอมโบ การป้องกัน และจังหวะสวนกลับเพื่อชนะคู่แข่ง",
        "how": "เล่นเป็นรอบ เลือกตัวละคร ฝึกท่าพื้นฐาน/คอมโบ อ่านจังหวะคู่ต่อสู้ และทำให้พลังชีวิตอีกฝ่ายหมดก่อน",
        "source": "our_games",
    },
    "spider_man_2": {
        "name": "Marvel's Spider-Man 2",
        "aliases": ("marvel's spider-man 2", "spider-man 2", "spider man 2", "spider-man", "spider man", "spider", "สไปเดอร์แมน", "สไปเดอร์"),
        "zones": ("PlayStation 5 Zone",),
        "genre": "เกม Action-Adventure",
        "summary": "Marvel's Spider-Man 2 คือเกมแอ็กชันผจญภัยที่ผู้เล่นรับบท Spider-Man ต่อสู้กับศัตรูและสำรวจเมือง",
        "how": "โหนใยเดินทาง ทำภารกิจ ใช้การต่อสู้แบบคอมโบ หลบหลีก และอัปเกรดสกิลระหว่างเนื้อเรื่อง",
        "source": "our_games",
    },
    "fortnite": {
        "name": "Fortnite",
        "aliases": ("fortnite", "ฟอร์ทไนท์"),
        "zones": ("PlayStation 5 Zone",),
        "genre": "เกม Battle Royale / Action",
        "summary": "Fortnite คือเกมต่อสู้เอาชีวิตรอดที่ผู้เล่นแข่งกันในแผนที่ขนาดใหญ่และพยายามอยู่เป็นคนสุดท้าย",
        "how": "เก็บอาวุธ เคลื่อนตามวง ต่อสู้กับผู้เล่นอื่น และใช้การสร้างหรือโหมดไม่สร้างตามรูปแบบที่เลือก",
        "source": "reservation",
    },
    "god_of_war_ragnarok": {
        "name": "God of War Ragnarok",
        "aliases": ("god of war ragnarok", "god of war", "ragnarok"),
        "zones": ("PlayStation 5 Zone",),
        "genre": "เกม Action-Adventure",
        "summary": "God of War Ragnarok คือเกมแอ็กชันผจญภัยที่เน้นเนื้อเรื่อง การต่อสู้ และการสำรวจในโลกตำนานนอร์ส",
        "how": "ควบคุมตัวละครหลัก ต่อสู้กับศัตรู แก้ปริศนา สำรวจพื้นที่ และพัฒนาอาวุธ/สกิลตามเนื้อเรื่อง",
        "source": "our_games",
    },
    "beat_saber": {
        "name": "Beat Saber",
        "aliases": ("beat saber", "บีทเซเบอร์"),
        "zones": ("VR Zone",),
        "genre": "เกม VR Rhythm",
        "summary": "Beat Saber คือเกม VR จังหวะดนตรีที่ผู้เล่นใช้ดาบแสงฟันบล็อกตามจังหวะเพลง",
        "how": "สวมแว่น VR ถือคอนโทรลเลอร์ แล้วฟันบล็อกตามทิศทาง หลบสิ่งกีดขวาง และพยายามทำคะแนนตามจังหวะเพลง",
        "source": "our_games",
    },
    "horizon_call_of_the_mountain": {
        "name": "Horizon Call of the Mountain",
        "aliases": ("horizon call of the mountain", "horizon"),
        "zones": ("VR Zone",),
        "genre": "เกม VR Action-Adventure",
        "summary": "Horizon Call of the Mountain คือเกม VR ผจญภัยในโลก Horizon ที่เน้นการปีนป่าย สำรวจ และต่อสู้กับจักรกล",
        "how": "สวมแว่น VR ใช้คอนโทรลเลอร์ปีน เคลื่อนที่ เล็งธนู และทำภารกิจตามฉาก",
        "source": "reservation",
    },
    "gran_turismo_7": {
        "name": "Gran Turismo 7",
        "aliases": ("gran turismo 7", "gran turismo", "gt7", "จีที 7"),
        "zones": ("Cockpit Zone", "PlayStation 5 Zone"),
        "genre": "เกมแข่งรถ / Driving Simulator",
        "summary": "Gran Turismo 7 คือเกมแข่งรถที่เน้นการขับรถสมจริง การเลือกสนาม รถ และการควบคุมจังหวะเข้าโค้ง",
        "how": "ใน Cockpit Zone เล่นโดยใช้พวงมาลัย คันเร่ง เบรก และชุดเบาะจำลองการขับรถ เป้าหมายคือขับให้เร็วและควบคุมรถให้แม่นในแต่ละสนาม",
        "source": "our_games",
    },
    "call_of_duty_mw3": {
        "name": "Call of Duty: Modern Warfare III",
        "aliases": ("call of duty modern warfare iii", "modern warfare iii", "mwiii", "mw3", "call of duty mw3"),
        "zones": ("PlayStation 5 Zone",),
        "genre": "เกมยิง FPS",
        "summary": "Call of Duty: Modern Warfare III คือเกมยิงมุมมองบุคคลที่หนึ่งที่เน้นภารกิจและการยิงต่อสู้แบบรวดเร็ว",
        "how": "เล็ง ยิง เคลื่อนที่ ใช้อุปกรณ์ และทำ objective ของโหมดเกมหรือภารกิจให้สำเร็จ",
        "source": "our_games",
    },
    "ea_sports_fc_24": {
        "name": "EA Sports FC 24",
        "aliases": ("ea sports fc 24", "fc 24", "fifa", "เกมบอล"),
        "zones": ("PlayStation 5 Zone",),
        "genre": "เกมฟุตบอล",
        "summary": "EA Sports FC 24 คือเกมฟุตบอลที่ให้ผู้เล่นควบคุมทีม แข่งขัน ยิงประตู และวางแผนเกมเหมือนการแข่งขันฟุตบอล",
        "how": "เลือกทีม จัดตัว ควบคุมการส่งบอล เลี้ยง ยิง และตั้งรับเพื่อทำประตูให้มากกว่าคู่แข่ง",
        "source": "our_games",
    },
    "final_fantasy_xvi": {
        "name": "FINAL FANTASY XVI",
        "aliases": ("final fantasy xvi", "final fantasy 16", "final fantasy", "ff16", "ff xvi"),
        "zones": ("PlayStation 5 Zone",),
        "genre": "เกม Action RPG",
        "summary": "FINAL FANTASY XVI คือเกมแอ็กชัน RPG แฟนตาซีที่เน้นเนื้อเรื่อง การต่อสู้ และการพัฒนาตัวละคร",
        "how": "เล่นตามเนื้อเรื่อง ต่อสู้ด้วยสกิล/คอมโบ ทำภารกิจ และพัฒนาความสามารถของตัวละคร",
        "source": "our_games",
    },
    "hogwarts_legacy": {
        "name": "Hogwarts Legacy",
        "aliases": ("hogwarts legacy", "hogwarts", "ฮอกวอตส์"),
        "zones": ("PlayStation 5 Zone",),
        "genre": "เกม Open-world Action RPG",
        "summary": "Hogwarts Legacy คือเกมผจญภัยในโลกเวทมนตร์ ผู้เล่นเรียนคาถา สำรวจ และทำภารกิจในฮอกวอตส์และพื้นที่รอบ ๆ",
        "how": "สำรวจพื้นที่ ใช้คาถา ต่อสู้ แก้ปริศนา และทำเควสต์เพื่อพัฒนาตัวละคร",
        "source": "our_games",
    },
    "resident_evil_4": {
        "name": "Resident Evil 4",
        "aliases": ("resident evil 4", "re4"),
        "zones": ("PlayStation 5 Zone",),
        "genre": "เกม Survival Horror / Action",
        "summary": "Resident Evil 4 คือเกมเอาตัวรอดสยองขวัญที่เน้นการต่อสู้ การสำรวจ และการบริหารกระสุน/ไอเทม",
        "how": "สำรวจพื้นที่ เก็บทรัพยากร ต่อสู้กับศัตรู แก้ปริศนา และเอาตัวรอดตามเนื้อเรื่อง",
        "source": "our_games",
    },
    "resident_evil_village": {
        "name": "Resident Evil Village",
        "aliases": ("resident evil village", "re village", "re8"),
        "zones": ("PlayStation 5 Zone",),
        "genre": "เกม Survival Horror",
        "summary": "Resident Evil Village คือเกมสยองขวัญเอาตัวรอดที่เน้นบรรยากาศ การสำรวจ และการต่อสู้กับศัตรูหลากหลายรูปแบบ",
        "how": "สำรวจฉาก เก็บไอเทม จัดการทรัพยากร ต่อสู้ และแก้ปริศนาเพื่อดำเนินเรื่อง",
        "source": "our_games",
    },
    "naruto_x_boruto": {
        "name": "NARUTO X BORUTO Ultimate Ninja Storm Connections",
        "aliases": ("naruto x boruto", "ultimate ninja storm connections", "naruto", "boruto", "นารูโตะ", "โบรูโตะ"),
        "zones": ("PlayStation 5 Zone",),
        "genre": "เกมต่อสู้จากอนิเมะ",
        "summary": "NARUTO X BORUTO Ultimate Ninja Storm Connections คือเกมต่อสู้ที่ใช้ตัวละครจากจักรวาล Naruto/Boruto",
        "how": "เลือกตัวละคร ใช้คอมโบ สกิลนินจา และจังหวะหลบ/สวนกลับเพื่อเอาชนะคู่ต่อสู้",
        "source": "our_games",
    },
    "the_last_of_us": {
        "name": "The Last of Us Part I / Part II",
        "aliases": ("the last of us", "last of us", "tlou"),
        "zones": ("PlayStation 5 Zone",),
        "genre": "เกม Action-Adventure / Survival",
        "summary": "The Last of Us คือเกมผจญภัยเอาตัวรอดที่เน้นเนื้อเรื่อง การลอบเร้น และการจัดการทรัพยากร",
        "how": "สำรวจ ฉวยโอกาสลอบเร้น ต่อสู้ เก็บทรัพยากร และดำเนินเรื่องผ่านภารกิจต่าง ๆ",
        "source": "our_games",
    },
    "uncharted": {
        "name": "Uncharted: Legacy of Thieves Collection",
        "aliases": ("uncharted", "legacy of thieves"),
        "zones": ("PlayStation 5 Zone",),
        "genre": "เกม Action-Adventure",
        "summary": "Uncharted คือเกมผจญภัยแนวล่าสมบัติที่เน้นปีนป่าย สำรวจ แก้ปริศนา และฉากแอ็กชัน",
        "how": "สำรวจฉาก ปีนป่าย แก้ปริศนา ยิงต่อสู้ และดำเนินเรื่องผ่านภารกิจ",
        "source": "our_games",
    },
    "mario_kart_8": {
        "name": "Mario Kart 8 Deluxe",
        "aliases": ("mario kart 8 deluxe", "mario kart", "มาริโอคาร์ท"),
        "zones": ("Nintendo Switch Zone",),
        "genre": "เกมแข่งรถ Party Racing",
        "summary": "Mario Kart 8 Deluxe คือเกมแข่งรถสไตล์ปาร์ตี้ที่ใช้ตัวละคร Nintendo ขับรถแข่งกันในสนามหลากหลายแบบ",
        "how": "เลือกตัวละครและรถ ขับเข้าเส้นชัย ใช้ไอเทมช่วยโจมตี/ป้องกัน และเล่นสนุกได้หลายคน",
        "source": "our_games",
    },
    "mario_kart_live": {
        "name": "Mario Kart Live: Home Circuit",
        "aliases": ("mario kart live: home circuit", "mario kart live", "home circuit"),
        "zones": ("Nintendo Switch Zone",),
        "genre": "เกมแข่งรถผสมของเล่นจริงกับ Nintendo Switch",
        "summary": "Mario Kart Live: Home Circuit คือเกมที่ใช้รถ Mario Kart จริงควบคุมผ่าน Nintendo Switch แล้วแสดงสนามแข่งบนหน้าจอ",
        "how": "จัดสนามในพื้นที่จริง ควบคุมรถผ่าน Nintendo Switch ขับ เก็บไอเทม บูสต์ และแข่งผ่านภาพจากกล้องบนรถ",
        "source": "our_games",
    },
    "overcooked_2": {
        "name": "Overcooked 2",
        "aliases": ("overcooked 2", "overcooked", "โอเวอร์คุก"),
        "zones": ("Nintendo Switch Zone",),
        "genre": "เกม Co-op ทำอาหาร",
        "summary": "Overcooked 2 คือเกมทำอาหารแบบร่วมมือกัน ผู้เล่นต้องแบ่งหน้าที่ เตรียมอาหาร เสิร์ฟ และจัดการครัวที่วุ่นวาย",
        "how": "ช่วยกันหั่นวัตถุดิบ ปรุง เสิร์ฟ ล้างจาน และสื่อสารกับทีมให้ทันเวลา",
        "source": "our_games",
    },
    "super_smash_bros": {
        "name": "Super Smash Bros Ultimate",
        "aliases": ("super smash bros ultimate", "super smash", "smash bros", "smash"),
        "zones": ("Nintendo Switch Zone",),
        "genre": "เกมต่อสู้แบบ Platform Fighter",
        "summary": "Super Smash Bros Ultimate คือเกมต่อสู้ที่ใช้ตัวละครจากหลายเกม ผลักคู่ต่อสู้ออกจากฉากเพื่อทำคะแนน",
        "how": "เลือกตัวละคร ใช้ท่าโจมตี หลบ กระโดด และพยายามทำให้คู่แข่งกระเด็นออกนอกสนาม",
        "source": "our_games",
    },
    "switch_sports": {
        "name": "Nintendo Switch Sports",
        "aliases": ("nintendo switch sports", "switch sports"),
        "zones": ("Nintendo Switch Zone",),
        "genre": "เกมกีฬา Motion Control",
        "summary": "Nintendo Switch Sports คือเกมกีฬาที่ใช้การขยับ Joy-Con จำลองการเล่นกีฬาหลายประเภท",
        "how": "ถือ Joy-Con แล้วขยับตามกีฬาที่เลือก เช่น ตี โยน หรือแกว่งตามท่าทางในเกม",
        "source": "our_games",
    },
    "animal_crossing": {
        "name": "Animal Crossing: New Horizons",
        "aliases": ("animal crossing new horizons", "animal crossing", "new horizons"),
        "zones": ("Nintendo Switch Zone",),
        "genre": "เกม Life Simulation",
        "summary": "Animal Crossing: New Horizons คือเกมใช้ชีวิตบนเกาะ ผู้เล่นตกแต่งบ้าน เก็บของ สร้างพื้นที่ และพูดคุยกับชาวเกาะ",
        "how": "เล่นแบบสบาย ๆ โดยเก็บทรัพยากร ตกปลา จับแมลง ตกแต่งเกาะ และทำกิจกรรมประจำวัน",
        "source": "our_games",
    },
    "it_takes_two": {
        "name": "It Takes Two",
        "aliases": ("it takes two",),
        "zones": ("Nintendo Switch Zone",),
        "genre": "เกม Co-op Adventure",
        "summary": "It Takes Two คือเกมผจญภัยสำหรับเล่นร่วมกันสองคน ที่ต้องช่วยกันแก้ปริศนาและผ่านด่าน",
        "how": "ผู้เล่นสองคนต้องสื่อสาร แบ่งหน้าที่ ใช้ความสามารถของตัวละคร และช่วยกันผ่านอุปสรรค",
        "source": "our_games",
    },
    "luigis_mansion_3": {
        "name": "Luigi's Mansion 3",
        "aliases": ("luigi's mansion 3", "luigis mansion 3", "luigi mansion", "ลุยจิ"),
        "zones": ("Nintendo Switch Zone",),
        "genre": "เกม Action Puzzle",
        "summary": "Luigi's Mansion 3 คือเกมผจญภัยจับผีที่ผู้เล่นสำรวจโรงแรมและแก้ปริศนา",
        "how": "ใช้เครื่องดูดผี สำรวจห้อง แก้ปริศนา และจับผีเพื่อผ่านด่าน",
        "source": "our_games",
    },
    "mario_party": {
        "name": "Mario Party Superstars",
        "aliases": ("mario party superstars", "mario party"),
        "zones": ("Nintendo Switch Zone",),
        "genre": "เกม Party / Mini-games",
        "summary": "Mario Party Superstars คือเกมปาร์ตี้ที่เล่นบนกระดานและแข่งมินิเกมกับเพื่อน",
        "how": "ทอยลูกเต๋าเดินบนกระดาน เก็บดาว และเล่นมินิเกมเพื่อทำคะแนน",
        "source": "our_games",
    },
    "monster_hunter_rise": {
        "name": "Monster Hunter Rise",
        "aliases": ("monster hunter rise", "monster hunter"),
        "zones": ("Nintendo Switch Zone",),
        "genre": "เกม Action RPG ล่ามอนสเตอร์",
        "summary": "Monster Hunter Rise คือเกมล่ามอนสเตอร์ที่ผู้เล่นเลือกอาวุธ ทำภารกิจ และเก็บวัตถุดิบมาสร้างอุปกรณ์",
        "how": "เลือกอาวุธ รับเควสต์ ตามหามอนสเตอร์ หลบ/โจมตีให้ถูกจังหวะ และคราฟต์อุปกรณ์จากวัตถุดิบ",
        "source": "our_games",
    },
    "moving_out_2": {
        "name": "Moving Out 2",
        "aliases": ("moving out 2", "moving out"),
        "zones": ("Nintendo Switch Zone",),
        "genre": "เกม Co-op Puzzle / Party",
        "summary": "Moving Out 2 คือเกมย้ายของแบบร่วมมือกันที่ต้องช่วยกันขนของผ่านฉากวุ่น ๆ",
        "how": "ช่วยกันยก โยน วางแผนเส้นทาง และขนของให้เสร็จภายในเวลา",
        "source": "our_games",
    },
    "new_super_mario_bros": {
        "name": "New Super Mario Bros. U Deluxe",
        "aliases": ("new super mario bros u deluxe", "new super mario bros", "mario bros", "มาริโอ้"),
        "zones": ("Nintendo Switch Zone",),
        "genre": "เกม Platformer 2D",
        "summary": "New Super Mario Bros. U Deluxe คือเกมมาริโอแบบเดินลุยด่าน กระโดด หลบศัตรู และเก็บเหรียญ",
        "how": "วิ่ง กระโดด ใช้ power-up ผ่านด่าน และร่วมมือกับเพื่อนได้หลายคน",
        "source": "our_games",
    },
    "ring_fit_adventure": {
        "name": "Ring Fit Adventure",
        "aliases": ("ring fit adventure", "ring fit", "ริงฟิต"),
        "zones": ("Nintendo Switch Zone",),
        "genre": "เกมออกกำลังกาย Adventure",
        "summary": "Ring Fit Adventure คือเกมออกกำลังกายที่ใช้ Ring-Con และท่าทางร่างกายเพื่อผจญภัยในเกม",
        "how": "ใส่ Joy-Con กับ Ring-Con แล้วทำท่าออกกำลังกาย เช่น วิ่ง บีบ ดัน หรือยืด เพื่อโจมตีและผ่านด่าน",
        "source": "our_games",
    },
    "super_mario_odyssey": {
        "name": "Super Mario Odyssey",
        "aliases": ("super mario odyssey", "mario odyssey"),
        "zones": ("Nintendo Switch Zone",),
        "genre": "เกม Platformer 3D",
        "summary": "Super Mario Odyssey คือเกมผจญภัย 3D ที่ Mario สำรวจโลกต่าง ๆ และเก็บ Power Moon",
        "how": "วิ่ง กระโดด ใช้หมวก Cappy จับ/ควบคุมบางสิ่ง และสำรวจฉากเพื่อเก็บเป้าหมาย",
        "source": "our_games",
    },
    "zelda_breath_of_the_wild": {
        "name": "The Legend of Zelda: Breath of the Wild",
        "aliases": ("the legend of zelda breath of the wild", "zelda breath of the wild", "breath of the wild", "zelda", "เซลด้า"),
        "zones": ("Nintendo Switch Zone",),
        "genre": "เกม Open-world Adventure",
        "summary": "The Legend of Zelda: Breath of the Wild คือเกมผจญภัยโลกเปิดที่ให้ผู้เล่นสำรวจ ต่อสู้ แก้ปริศนา และทดลองวิธีผ่านสถานการณ์ต่าง ๆ",
        "how": "สำรวจแผนที่ เก็บอาวุธ/อาหาร แก้ shrine ต่อสู้ และเลือกเส้นทางการผจญภัยเองได้มาก",
        "source": "our_games",
    },
    "little_nightmares_2": {
        "name": "Little Nightmares II",
        "aliases": ("little nightmares ii", "little nightmares 2", "little nightmares"),
        "zones": ("Nintendo Switch Zone",),
        "genre": "เกม Puzzle Platform / Horror",
        "summary": "Little Nightmares II คือเกมผจญภัยบรรยากาศสยองที่เน้นการหลบหนี แก้ปริศนา และผ่านฉากอันตราย",
        "how": "เดิน สำรวจ หลบศัตรู ใช้สิ่งของในฉากแก้ปริศนา และหาจังหวะผ่านอุปสรรค",
        "source": "our_games",
    },
}


COMPETITION_GAME_SUMMARY = (
    "เกม/รายการแข่งขันที่มีข้อมูลกติกาในฐานข้อมูลตอนนี้:\n"
    "- Counter-Strike 2: PSU Phuket CS2 2026 Tournament\n"
    "- VALORANT: PSU Phuket VALORANT 2026 Tournament\n"
    "- Arena of Valor (RoV): Blueket Games 2025 ประเภททีมชาย\n"
    "- TEKKEN 8: PSU Esports / Tekken 8 Tournament\n"
    "หมายเหตุ: นี่คือรายการที่มีเอกสารกติกาหรือข้อมูลการแข่งขันในฐานข้อมูล ไม่ได้ยืนยันว่าเปิดรับสมัครอยู่ตอนนี้"
)


ZONE_DETAILS = {
    "pc": {
        "title": "PC Zone",
        "summary": "PC Zone คือโซนคอมพิวเตอร์เกมมิ่งสำหรับเล่นเกมบน PC และใช้ฝึกซ้อม/เรียนรู้ด้านอีสปอร์ต",
        "how": "จอง PC Zone ตามรอบบริการ เข้าใช้งานเครื่องที่ศูนย์จัดไว้ แล้วเปิดเกมหรือโปรแกรมที่ต้องการตามรายการที่มี",
        "equipment": "Gaming PC รุ่น MSI MAG Infinite S3 14th 10 เครื่อง (10 Units), Gaming Monitor 10 เครื่อง (10 Units), Gaming Chair 10 ตัว (10 Units), Gaming Keyboard, Gaming Mouse และ Gaming Headset",
        "games": "VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, TEKKEN 8 และ League of Legends",
    },
    "cockpit": {
        "title": "Cockpit Zone",
        "summary": "Cockpit Zone คือโซนจำลองการขับรถ/เกมแข่งรถ ใช้เล่น Gran Turismo 7 ด้วยชุดพวงมาลัยและเบาะขับ",
        "how": "จอง Cockpit Zone แล้วนั่งในชุด Cockpit ใช้พวงมาลัย Logitech G923 พร้อมคันเร่ง/เบรก/คันเกียร์เพื่อควบคุมรถในเกม",
        "equipment": "TV 65 นิ้ว 2 เครื่อง (2 Units), Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 ชุด (2 Units), Racezone Full Cockpit V3 2 ชุด (2 Units) และ Pulse Elite Wireless Headset 2 ชุด (2 Units)",
        "games": "Gran Turismo 7 (Single Player)",
    },
    "nintendo": {
        "title": "Nintendo Switch Zone",
        "summary": "Nintendo Switch Zone คือโซนเล่นเกม Nintendo Switch สำหรับเล่นเป็นกลุ่ม/ครอบครัว/กิจกรรมสนุก ๆ",
        "how": "จอง Nintendo Switch Zone แล้วเล่นผ่าน Nintendo Switch OLED กับ TV 86 นิ้ว ใช้จอย Joy-Con/Controller ตามเกมที่เลือก",
        "equipment": "TV 86 นิ้ว 1 เครื่อง (1 Unit), Sofa 2 seats 2 ชุด (2 Units) และ Nintendo Switch OLED 1 เครื่อง (1 Unit)",
        "games": "Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกม Nintendo Switch อื่น ๆ ในรายการ",
    },
    "ps5": {
        "title": "PlayStation 5 Zone",
        "summary": "PlayStation 5 Zone คือโซนเล่นเกมคอนโซล PS5 สำหรับ 1-2 คนต่อรอบตามบริการที่มีในระบบ",
        "how": "จอง PlayStation 5 Zone แล้วเล่นเกมผ่านเครื่อง PS5 และจอ/อุปกรณ์ที่ศูนย์จัดไว้ เลือกเกมตามรายการที่มีให้บริการ",
        "equipment": "PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 เครื่อง (2 Units)",
        "games": "Marvel's Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกม PlayStation 5 อื่น ๆ ในรายการ",
    },
    "vr": {
        "title": "VR Zone",
        "summary": "VR Zone คือโซนเล่นเกม VR โดยใช้ PlayStation VR2 เหมาะกับประสบการณ์เกมเสมือนจริง",
        "how": "จอง VR Zone แล้วสวม PlayStation VR2 ใช้คอนโทรลเลอร์ VR ตามคำแนะนำของเกมหรือเจ้าหน้าที่ และควรเล่นในพื้นที่ที่จัดไว้เท่านั้น",
        "equipment": "PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 1 เครื่อง (1 Unit) และ Sony PlayStation VR2 1 ชุด (1 Unit)",
        "games": "Beat Saber และ Horizon Call of the Mountain",
    },
}


EQUIPMENT_BY_ZONE = {
    "pc": [
        "Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)",
        "Gaming Monitor (จำนวน 10 จอ)",
        "Gaming Chair (จำนวน 10 ตัว)",
        "Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset",
    ],
    "cockpit": [
        "TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)",
        "Racezone Full Cockpit V3 (จำนวน 2 ชุด)",
        "Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)",
        "Pulse Elite Wireless Headset (จำนวน 2 อัน)",
    ],
    "nintendo": [
        "TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)",
        "Nintendo Switch OLED (จำนวน 1 เครื่อง)",
        "Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)",
    ],
    "ps5": [
        "PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)",
    ],
    "vr": [
        "PlayStation 5 Slim (จำนวน 1 เครื่อง)",
        "Sony PlayStation VR2 (จำนวน 1 ชุด)",
    ],
}


ZONE_ORDER = ("pc", "cockpit", "nintendo", "ps5", "vr")


def _format_bulleted_sections(sections: list[tuple[str, list[str]]]) -> str:
    lines: list[str] = []
    for title, items in sections:
        if lines:
            lines.append("")
        lines.append(title)
        lines.extend(f"•    {item}" for item in items)
    return "\n".join(lines)


def _equipment_home_summary(keys: list[str] | None = None) -> str:
    selected_keys = keys or list(ZONE_ORDER)
    sections = [
        (ZONE_DETAILS[key]["title"], EQUIPMENT_BY_ZONE[key])
        for key in selected_keys
        if key in ZONE_DETAILS and key in EQUIPMENT_BY_ZONE
    ]
    return _format_bulleted_sections(sections)


EQUIPMENT_ITEM_DETAILS = {
    "gaming_pc": {
        "title": "Gaming PC รุ่น MSI MAG Infinite S3 14th",
        "aliases": ("gaming pc", "msi mag infinite", "pc", "คอม", "คอมพิวเตอร์", "เครื่องคอม"),
        "zone": "PC Zone",
        "what": "เครื่องคอมพิวเตอร์เกมมิ่งของ PC Zone สำหรับเล่นเกมบนคอมและฝึกซ้อมอีสปอร์ต",
        "how": "เลือก PC Zone ในระบบจอง แล้วเข้าใช้งานตามรอบเวลาที่จองไว้ จากนั้นเปิดเกม/โปรแกรมที่ศูนย์จัดเตรียมไว้ให้",
        "use": "เล่น VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, TEKKEN 8, League of Legends และเกม PC ที่มีในรายการ",
        "note": "หน้า Home ระบุ Gaming PC 10 Units; สเปกที่บันทึกไว้ในโปรเจกต์: Intel Core i5-14400, RAM DDR5 32GB, NVIDIA GeForce RTX 5060 8GB",
    },
    "gaming_monitor": {
        "title": "Gaming Monitor",
        "aliases": ("gaming monitor", "monitor", "จอ", "จอเกม", "จอคอม", "จอ gaming"),
        "zone": "PC Zone",
        "what": "จอภาพสำหรับใช้คู่กับ Gaming PC ใน PC Zone",
        "how": "ใช้งานพร้อมเครื่อง PC ที่จองไว้ โดยปกติผู้ใช้ไม่ต้องตั้งค่าฮาร์ดแวร์เอง หากจอหรือภาพมีปัญหาควรแจ้งเจ้าหน้าที่",
        "use": "แสดงผลเกมและโปรแกรมบน PC Zone",
        "note": "หน้า Home ระบุว่ามี Gaming Monitor 10 เครื่อง",
    },
    "gaming_keyboard": {
        "title": "Gaming Keyboard",
        "aliases": ("gaming keyboard", "keyboard", "คีย์บอร์ด", "แป้นพิมพ์"),
        "zone": "PC Zone",
        "what": "คีย์บอร์ดสำหรับควบคุมเกมและพิมพ์บน Gaming PC",
        "how": "ใช้งานกับเครื่อง PC ที่จองไว้ หลีกเลี่ยงการแกะ ย้าย หรือปรับอุปกรณ์เอง หากมีปุ่มเสียควรแจ้งเจ้าหน้าที่",
        "use": "ใช้ควบคุมเกม PC และพิมพ์ข้อมูล",
        "note": "อยู่ในรายการอุปกรณ์ PC Zone บนหน้า Home",
    },
    "gaming_mouse": {
        "title": "Gaming Mouse",
        "aliases": ("gaming mouse", "mouse", "เมาส์", "เม้า", "เม้าส์"),
        "zone": "PC Zone",
        "what": "เมาส์สำหรับเล่นเกมบน Gaming PC",
        "how": "ใช้งานกับ PC ที่จองไว้ และควรแจ้งเจ้าหน้าที่หากคลิกไม่ติด เซนเซอร์รวน หรือพบความเสียหาย",
        "use": "ใช้ควบคุมเกม PC โดยเฉพาะเกมแนว FPS/MOBA",
        "note": "อยู่ในรายการอุปกรณ์ PC Zone บนหน้า Home",
    },
    "gaming_headset": {
        "title": "Gaming Headset",
        "aliases": ("gaming headset", "headset", "หูฟัง", "เฮดเซ็ต", "ไมค์"),
        "zone": "PC Zone",
        "what": "หูฟังเกมมิ่งสำหรับฟังเสียงเกมและสื่อสารระหว่างเล่น",
        "how": "ใช้งานคู่กับ PC ที่จองไว้ ปรับระดับเสียงอย่างเหมาะสม และแจ้งเจ้าหน้าที่ถ้าเสียง/ไมค์มีปัญหา",
        "use": "ฟังเสียงเกมและสื่อสารในเกมหรือกิจกรรมอีสปอร์ต",
        "note": "อยู่ในรายการอุปกรณ์ PC Zone บนหน้า Home",
    },
    "gaming_chair": {
        "title": "Gaming Chair",
        "aliases": ("gaming chair", "chair", "เก้าอี้", "เก้าอี้เกม", "เก้าอี้เกมมิ่ง"),
        "zone": "PC Zone",
        "what": "เก้าอี้เกมมิ่งสำหรับนั่งใช้งาน PC Zone",
        "how": "ใช้นั่งระหว่างเล่นเกม/ฝึกซ้อม และไม่ควรย้ายหรือใช้งานผิดประเภท",
        "use": "รองรับการนั่งเล่น PC Zone เป็นรอบเวลา",
        "note": "หน้า Home ระบุว่ามี Gaming Chair 10 ตัว",
    },
    "logitech_g923": {
        "title": "Logitech G923 TRUEFORCE Racing Wheel",
        "aliases": ("logitech g923", "g923", "trueforce", "racing wheel", "พวงมาลัย", "พวงมาลัยรถ", "พวงมาลัยขับรถ"),
        "zone": "Cockpit Zone",
        "what": "ชุดพวงมาลัยแข่งรถสำหรับเล่นเกมขับรถใน Cockpit Zone",
        "how": "จอง Cockpit Zone แล้วใช้พวงมาลัย เหยียบคันเร่ง/เบรก และควบคุมรถตามเกมที่ศูนย์จัดไว้",
        "use": "ใช้เล่น Gran Turismo 7 ร่วมกับชุด Cockpit และ TV 65 นิ้ว",
        "note": "หน้า Home ระบุว่ามี Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 ชุด (2 Units)",
    },
    "driving_force_shifter": {
        "title": "Driving Force Shifter",
        "aliases": ("driving force shifter", "shifter", "gear shifter", "เกียร์", "คันเกียร์", "เกียร์รถ"),
        "zone": "Cockpit Zone",
        "what": "คันเกียร์เสริมสำหรับชุดพวงมาลัยขับรถ",
        "how": "ใช้งานร่วมกับ Logitech G923 และ Cockpit ในเกมขับรถ หากไม่คุ้นเคยควรให้เจ้าหน้าที่แนะนำก่อนเริ่มเล่น",
        "use": "เพิ่มความสมจริงให้เกมขับรถ เช่น Gran Turismo 7",
        "note": "อยู่ในชุด Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 ชุด",
    },
    "racezone_cockpit": {
        "title": "Racezone Full Cockpit V3",
        "aliases": ("racezone full cockpit v3", "racezone", "full cockpit", "cockpit v3", "เบาะขับรถ"),
        "zone": "Cockpit Zone",
        "what": "ชุดเบาะ/โครงจำลองการขับรถสำหรับเกมแข่งรถ",
        "how": "นั่งใน Cockpit แล้วใช้พวงมาลัย/คันเร่ง/เบรกตามที่ตั้งค่าไว้ในเกม",
        "use": "ใช้เล่นเกมขับรถ Gran Turismo 7 แบบจำลองการขับจริงมากขึ้น",
        "note": "หน้า Home ระบุว่ามี Racezone Full Cockpit V3 2 ชุด",
    },
    "pulse_elite": {
        "title": "Pulse Elite Wireless Headset",
        "aliases": ("pulse elite", "pulse elite wireless headset", "wireless headset", "หูฟังไร้สาย", "หูฟัง pulse"),
        "zone": "Cockpit Zone",
        "what": "หูฟังไร้สายสำหรับใช้งานกับชุดเกมใน Cockpit Zone",
        "how": "ใช้งานตามอุปกรณ์ที่เจ้าหน้าที่จัดเตรียมไว้ ถ้าเชื่อมต่อเสียงไม่ได้ควรแจ้งเจ้าหน้าที่",
        "use": "ฟังเสียงเกมขับรถและเพิ่มความสมจริงระหว่างเล่น",
        "note": "หน้า Home ระบุว่ามี Pulse Elite Wireless Headset 2 ชุด",
    },
    "nintendo_switch_oled": {
        "title": "Nintendo Switch OLED",
        "aliases": ("nintendo switch oled", "switch oled", "nintendo switch", "nintendo", "switch", "นินเทนโด", "สวิตช์", "สวิทช์"),
        "zone": "Nintendo Switch Zone",
        "what": "เครื่องเกม Nintendo Switch รุ่น OLED สำหรับเล่นเกมคอนโซลแบบกลุ่ม/ครอบครัว",
        "how": "จอง Nintendo Switch Zone แล้วเล่นผ่าน TV 86 นิ้วและจอยที่ศูนย์จัดไว้ตามรอบบริการ",
        "use": "เล่น Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกม Switch ในรายการ",
        "note": "หน้า Home ระบุว่ามี Nintendo Switch OLED 1 เครื่อง",
    },
    "playstation_5_slim": {
        "title": "PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive",
        "aliases": ("playstation 5 slim", "playstation 5", "ps5 slim", "ps5", "เพลย์ห้า", "เพลย์ 5", "เครื่องเพลย์"),
        "zone": "PlayStation 5 Zone / VR Zone",
        "what": "เครื่องเกม PlayStation 5 สำหรับเล่นเกมคอนโซล และใช้เป็นฐานสำหรับ VR Zone บางชุด",
        "how": "จอง PlayStation 5 Zone หรือ VR Zone ตามบริการที่ต้องการ แล้วเล่นเกมที่ศูนย์จัดเตรียมไว้ตามรอบเวลา",
        "use": "เล่น Marvel's Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และรองรับ VR Zone ที่ใช้ PlayStation VR2",
        "note": "หน้า Home ระบุว่ามี PS5 Slim 2 เครื่องใน PlayStation 5 Zone และ 1 เครื่องใน VR Zone",
    },
    "sony_playstation_vr2": {
        "title": "Sony PlayStation VR2",
        "aliases": ("sony playstation vr2", "playstation vr2", "ps vr2", "psvr2", "vr2", "แว่น vr", "แว่นวีอาร์", "แว่น"),
        "zone": "VR Zone",
        "what": "ชุดแว่น VR สำหรับเล่นเกมเสมือนจริงใน VR Zone",
        "how": "จอง VR Zone แล้วสวมแว่น PlayStation VR2 และใช้คอนโทรลเลอร์ตามคำแนะนำของเจ้าหน้าที่/เกม",
        "use": "เล่น Beat Saber และ Horizon Call of the Mountain",
        "note": "หน้า Home ระบุว่ามี Sony PlayStation VR2 1 ชุด (1 Unit / Units)",
    },
    "tv_65": {
        "title": "TV 65 นิ้ว",
        "aliases": ("tv 65", "tv 65 นิ้ว", "ทีวี 65", "ทีวี 65 นิ้ว", "65 นิ้ว"),
        "zone": "Cockpit Zone",
        "what": "จอทีวีขนาด 65 นิ้วสำหรับแสดงภาพเกมขับรถใน Cockpit Zone",
        "how": "ใช้งานพร้อมชุด Cockpit และพวงมาลัยที่ศูนย์จัดไว้ ผู้ใช้ไม่จำเป็นต้องปรับสายหรือเคลื่อนย้ายทีวีเอง",
        "use": "แสดงผลเกม Gran Turismo 7 ใน Cockpit Zone",
        "note": "หน้า Home ระบุว่ามี TV 65 นิ้ว 2 เครื่อง",
    },
    "tv_86": {
        "title": "TV 86 นิ้ว",
        "aliases": ("tv 86", "tv 86 นิ้ว", "ทีวี 86", "ทีวี 86 นิ้ว", "86 นิ้ว"),
        "zone": "Nintendo Switch Zone",
        "what": "จอทีวีขนาด 86 นิ้วสำหรับเล่นเกม Nintendo Switch เป็นกลุ่ม",
        "how": "ใช้งานพร้อม Nintendo Switch OLED ใน Nintendo Switch Zone ตามรอบบริการ",
        "use": "แสดงผลเกม Nintendo Switch เช่น Mario Kart, Overcooked, Super Smash Bros และ Switch Sports",
        "note": "หน้า Home ระบุว่ามี TV 86 นิ้ว 1 เครื่อง",
    },
    "sofa_2_seats": {
        "title": "Sofa 2 seats",
        "aliases": ("sofa", "sofa 2 seats", "โซฟา", "โซฟา 2 ที่นั่ง"),
        "zone": "Nintendo Switch Zone",
        "what": "โซฟาสำหรับนั่งเล่นเกมใน Nintendo Switch Zone",
        "how": "ใช้นั่งระหว่างเล่น Nintendo Switch และไม่ควรเคลื่อนย้ายหรือใช้งานผิดประเภท",
        "use": "รองรับการเล่นเกมเป็นกลุ่มใน Nintendo Switch Zone",
        "note": "หน้า Home ระบุว่ามี Sofa 2 seats 2 ชุด",
    },
}


@dataclass(frozen=True)
class FastAnswer:
    answer: str
    hits: list[dict]
    mode: str
    elapsed: float
    confidence: float = 0.90


def _has(q: str, *terms: str) -> bool:
    return any(term in q for term in terms)


def _game_alias_key(value: str) -> str:
    normalized = normalize_text(str(value or "")).replace("™", "").replace("®", "")
    normalized = re.sub(r"\(\s*remastered\s*\)", "", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bremastered\b", "", normalized, flags=re.IGNORECASE)
    return re.sub(r"[^0-9a-z\u0E00-\u0E7F]+", "", normalized)


def _unique_aliases(values: list[str] | tuple[str, ...]) -> tuple[str, ...]:
    seen: set[str] = set()
    aliases: list[str] = []
    for value in values:
        alias = str(value or "").strip()
        if not alias:
            continue
        key = _game_alias_key(alias)
        if not key or key in seen:
            continue
        seen.add(key)
        aliases.append(alias)
    return tuple(aliases)


@lru_cache(maxsize=1)
def _external_game_title_aliases() -> dict[str, tuple[str, ...]]:
    aliases_by_game: dict[str, list[str]] = {}
    if not GAME_TITLE_ALIASES_PATH.exists():
        return {}
    for line in GAME_TITLE_ALIASES_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        game = str(row.get("game") or "").strip()
        aliases = row.get("aliases") or []
        if not game or not isinstance(aliases, list):
            continue
        key = _game_alias_key(game)
        if not key:
            continue
        bucket = aliases_by_game.setdefault(key, [])
        bucket.append(game)
        bucket.extend(str(alias) for alias in aliases if str(alias or "").strip())
    return {key: _unique_aliases(tuple(values)) for key, values in aliases_by_game.items()}


def _aliases_for_game(name: str, base_aliases: list[str] | tuple[str, ...]) -> tuple[str, ...]:
    aliases = list(base_aliases)
    extras = _external_game_title_aliases().get(_game_alias_key(name), ())
    aliases.extend(extras)
    if normalize_text(name).startswith("call of duty"):
        aliases = [
            alias for alias in aliases
            if _compact_key(str(alias)) not in {"callofduty", "cod", "คอลออฟ", "ดิวตี้", "ดูตี้"}
        ]
    return _unique_aliases(tuple(aliases))


def _game_alias_direct_match(q: str, alias: str) -> bool:
    alias_norm = normalize_text(alias)
    if not alias_norm:
        return False
    ascii_body = re.sub(r"[^a-z0-9]", "", alias_norm)
    is_ascii_alias = bool(ascii_body) and not re.search(r"[\u0E00-\u0E7F]", alias_norm)
    if is_ascii_alias and len(ascii_body) <= 3:
        pattern = re.escape(alias_norm).replace(r"\ ", r"\s+")
        return re.search(rf"(?<![a-z0-9]){pattern}(?![a-z0-9])", q) is not None
    return alias_norm in q


def _game_alias_match(q: str, aliases: tuple[str, ...], *, threshold: float = 0.88) -> bool:
    for alias in aliases:
        if _game_alias_direct_match(q, alias):
            return True
    fuzzy_aliases = [
        alias
        for alias in aliases
        if len(normalize_text(str(alias)).replace(" ", "")) >= 4
    ]
    return bool(fuzzy_aliases and contains_alias(q, fuzzy_aliases, fuzzy=True, threshold=threshold)[0])


def _answer(text: str, source: str, mode: str, start: float, confidence: float = 0.90) -> FastAnswer:
    return FastAnswer(
        answer=text.strip(),
        hits=HITS[source],
        mode=mode,
        elapsed=round(time.perf_counter() - start, 4),
        confidence=confidence,
    )


def _no_answer(start: float) -> FastAnswer:
    return _answer(
        "ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ",
        "reservation",
        "no_answer_fast",
        start,
        0.92,
    )


def _chatbot_identity_answer(start: float) -> FastAnswer:
    return _answer(
        (
            f"ผมคือ {CHATBOT_NAME_TH} แชทบอทผู้ช่วยของ {CHATBOT_ORG_TH} ครับ\n\n"
            "ผมช่วยตอบคำถามเกี่ยวกับ:\n"
            "•    เกมที่มีให้เล่นและเกมที่เกี่ยวข้องกับการแข่งขัน\n"
            "•    ปุ่มควบคุมและวิธีเล่นของเกมที่มีข้อมูลยืนยัน\n"
            "•    อุปกรณ์และโซนบริการ เช่น PC, PS5, Nintendo Switch, VR และ Cockpit\n"
            "•    วิธีจอง เช็คอิน ค่าบริการ เวลาเปิด-ปิด และกฎการใช้งาน\n"
            "•    สมาชิกทีม ตำแหน่ง และหมวดสมาชิกของ PSU Esports Studio - Phuket\n\n"
            "ถ้าเป็นข้อมูลของศูนย์ ผมจะตอบจากฐานข้อมูลที่ยืนยันได้ก่อนเสมอ ถ้ายังไม่มีข้อมูลยืนยัน ผมจะบอกตรง ๆ ครับ"
        ),
        "home",
        "chatbot_identity_fast_path",
        start,
        0.98,
    )


def _looks_like_chatbot_greeting_query(q: str) -> bool:
    clean = q.strip().lower()
    if not clean:
        return False
    greeting_terms = (
        "สวัสดี", "หวัดดี", "ดีครับ", "ดีค่ะ", "ดีคับ", "ทักครับ", "ทักค่ะ",
        "hello", "hi", "hey",
    )
    if clean in greeting_terms:
        return True
    if len(clean) <= 40 and _has(clean, *greeting_terms):
        return True
    return False


def _chatbot_greeting_answer(start: float) -> FastAnswer:
    return _answer(
        (
            f"สวัสดีครับ ผมคือ {CHATBOT_NAME_TH} ผู้ช่วยของ {CHATBOT_ORG_TH}\n"
            "ถามเรื่องเกม อุปกรณ์ วิธีจอง เวลาเปิด-ปิด ค่าบริการ ปุ่มควบคุม กติกา หรือสมาชิกทีมได้เลยครับ"
        ),
        "home",
        "chatbot_greeting_fast_path",
        start,
        0.99,
    )


UNKNOWN_TERMS = [
    "ซ่อมคอมส่วนตัว", "ส่งอาหาร", "แมว", "สมาชิกรายปี", "เช่าโน้ตบุ๊ก", "ห้องนอน", "พักค้างคืน",
    "ขายคีย์บอร์ด", "รับซ่อมจอย", "ส่งเครื่องเกมไปบ้าน", "ซื้อเกม steam", "คอร์สสอนเล่น",
    "จ่ายด้วยคริปโต", "ผ่อนชำระ", "ส่วนลดวันเกิด", "เหมาทั้งวัน", "pc ตัวเอง", "ถ่ายรูปโปรไฟล์",
    "อาหารบุฟเฟต์", "งานแต่ง", "เช่าจอไปบ้าน",
]


def _schedule_details() -> str:
    return f"""รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: {RESERVATION_URL}"""


def _schedule_text(first: str, q: str) -> str:
    if _has(q, "ตอบสั้น", "สั้นๆ", "สั้น ๆ", "brief"):
        return f"{first}\nแหล่งข้อมูล: {RESERVATION_URL}"
    return first + "\n\n" + _schedule_details()


def _regular_weekday_schedule_text(first: str, q: str) -> str:
    if _has(q, "ตอบสั้น", "สั้นๆ", "สั้น ๆ", "brief"):
        return f"{first}\nแหล่งข้อมูล: {RESERVATION_URL}"
    return f"""{first}

รายละเอียดจากตาราง:
- วันอังคาร-พฤหัสบดีเปิดตามรอบปกติ
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
แหล่งข้อมูล: {RESERVATION_URL}"""


def _regular_weekday_label(q: str) -> str | None:
    labels: list[str] = []
    if _has(q, "อังคาร", "tuesday", "tue"):
        labels.append("วันอังคาร")
    if _has(q, "พุธ", "wednesday", "wed"):
        labels.append("วันพุธ")
    if _has(q, "พฤหัส", "พฤหัสบดี", "thursday", "thu"):
        labels.append("วันพฤหัสบดี")
    if len(labels) >= 2:
        return "วันอังคาร-พฤหัสบดี"
    return labels[0] if labels else None


def _game_context_for_schedule(q: str) -> str | None:
    if _has(q, "วาโล", "valorant", "cs2", "counter-strike", "pubg", "warzone", "pc games", "เกมบน pc", "คอมมี"):
        return "ข้อมูลเกม: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends"
    if _has(q, "spider-man", "spider", "tekken", "fortnite", "god of war", "playstation", "ps5", "เพลย์"):
        return "ข้อมูลเกม: PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5"
    if _has(q, "mario kart", "overcooked", "super smash", "switch sports", "nintendo", "switch", "นินเทนโด"):
        return "ข้อมูลเกม: Nintendo Switch มี Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกมอื่น ๆ"
    if _has(q, "beat saber", "horizon", "vr", "แว่น"):
        return "ข้อมูลเกม: VR มีเกม Beat Saber และ Horizon Call of the Mountain"
    if _has(q, "gran turismo", "cockpit", "พวงมาลัย"):
        return "ข้อมูลเกม: Cockpit ใช้เล่นเกม Gran Turismo 7"
    return None


def _holiday_text(items: list[object]) -> str:
    if not items:
        return "ไม่พบวันหยุดไทยหรือเทศกาลในปฏิทินที่บันทึกไว้สำหรับวันที่นี้"
    lines: list[str] = []
    for item in items:
        title = getattr(item, "title", "")
        item_type = getattr(item, "type", "")
        note = getattr(item, "note", "")
        suffix = f" ({item_type})" if item_type else ""
        line = f"- {title}{suffix}"
        if note:
            line += f": {note}"
        lines.append(line)
    return "\n".join(lines)


def _current_service_answer(q: str, start: float) -> FastAnswer:
    current = now_bangkok()
    slot = current_service_slot(current)
    label = format_thai_date(current.date())
    time_label = current.strftime("%H:%M")
    current_slot = slot.get("slot")
    next_open = slot.get("next_open_slot")

    if slot.get("status") == "open" and isinstance(current_slot, dict):
        first = f"ตอนนี้เล่นได้ครับ อยู่ช่วง {current_slot['label']} {current_slot['time_range']}"
    elif slot.get("status") == "maintenance" and isinstance(current_slot, dict):
        first = f"ตอนนี้ยังไม่ใช่ช่วงเล่นครับ อยู่ช่วง {current_slot['label']} {current_slot['time_range']} ซึ่งเป็น Maintenance"
    elif slot.get("status") == "closed":
        first = f"ตอนนี้ยังเล่นไม่ได้ครับ วันนี้ศูนย์ปิดให้บริการ ({slot.get('reason')})"
    elif isinstance(next_open, dict):
        first = f"ตอนนี้ยังเล่นไม่ได้ครับ รอบเปิดถัดไปของวันนี้คือ {next_open['label']} {next_open['time_range']}"
    else:
        first = "ตอนนี้ยังเล่นไม่ได้ครับ อยู่นอกช่วงเวลาให้บริการตามตารางที่มี"

    lines = [
        first,
        f"เวลาระบบ: {time_label} น. วันที่ {label} ตามเวลาไทย",
        "",
        "ตารางประจำที่ใช้ตรวจ:",
        "- วันจันทร์: 09:00-12:00 Maintenance*, 13:00-16:00 เปิดให้บริการ",
        "- วันอังคาร-พฤหัสบดี: 09:00-12:00 และ 13:00-16:00 เปิดให้บริการ",
        "- วันศุกร์: 09:00-12:00 เปิดให้บริการ, 13:00-16:00 Maintenance",
        "- วันหยุด/วันปิดพิเศษของศูนย์จะดูจากไฟล์ปิดบริการก่อนตารางประจำ",
        f"แหล่งข้อมูลตารางบริการ: {RESERVATION_URL}",
    ]
    holidays = holidays_for_date(current.date())
    if holidays:
        lines.insert(2, "ปฏิทินไทยวันนี้:\n" + _holiday_text(holidays))
    return _answer("\n".join(lines), "reservation", "current_service_slot_fast_path", start, 0.99)


def _date_calendar_answer(q: str, start: float, target: date | None = None, label_prefix: str | None = None) -> FastAnswer:
    today = today_bangkok()
    current = now_bangkok()
    value = target or today
    holidays = holidays_for_date(value)
    closure = closure_for(value)
    first = label_prefix or f"{'วันนี้คือ' if value == today else 'วันที่ที่ถามคือ'} {format_thai_date(value)}"
    lines = [
        first,
        f"เวลาระบบตอนนี้: {current.strftime('%H:%M')} น. ตามเวลาไทย",
        "ปฏิทินไทย:",
        _holiday_text(holidays),
    ]
    if closure and closure.status == "closed":
        lines.extend([
            "",
            f"สถานะศูนย์ตามไฟล์ปิดบริการ: ปิดให้บริการ ({closure.title})",
            closure.note,
        ])
    else:
        lines.extend([
            "",
            "สถานะศูนย์: ยังไม่พบวันปิดพิเศษของศูนย์สำหรับวันที่นี้ในไฟล์ service_closures.jsonl",
            "หมายเหตุ: วันหยุดไทย/เทศกาลเป็นข้อมูลปฏิทินประกอบ ไม่ได้แปลว่าศูนย์ปิดโดยอัตโนมัติ",
        ])
    lines.extend([
        f"แหล่งข้อมูลปฏิทินไทย: {THAI_HOLIDAY_SOURCE_URL}",
        f"แหล่งข้อมูลตารางบริการ: {RESERVATION_URL}",
    ])
    return _answer("\n".join(line for line in lines if line), "reservation", "calendar_date_context_fast_path", start, 0.98)


def _month_holiday_answer(q: str, start: float, year: int, month: int, label: str) -> FastAnswer:
    today = today_bangkok()
    holidays = holidays_for_month(year, month)
    closures = closures_for_month(year, month)
    count_only = _has(q, "กี่วัน", "กี่รายการ", "จำนวน", "ทั้งหมดกี่", "นับ") and not _has(q, "อะไรบ้าง", "ไหนบ้าง", "วันไหน", "รายชื่อ")
    lines = [f"{label} มีข้อมูลปฏิทินไทย {len(holidays)} รายการ:"]
    if holidays and not count_only:
        for item in holidays:
            value = date.fromisoformat(item.date)
            note = f" - {item.note}" if item.note else ""
            lines.append(f"- {format_thai_date(value)}: {item.title} ({item.type}){note}")
    elif not holidays:
        lines.append("- ยังไม่พบรายการวันหยุดไทย/เทศกาลในไฟล์ปฏิทินที่บันทึกไว้")

    lines.extend([
        "",
        f"{label} มีวันปิดให้บริการ {len(closures)} วันในไฟล์ service_closures.jsonl",
    ])
    if not count_only:
        for item in closures:
            value = date.fromisoformat(item.date)
            note = f" - {item.note}" if item.note else ""
            lines.append(f"- {format_thai_date(value)}: {item.title}{note}")
    lines.extend([
        f"วันที่อ้างอิงของระบบ: วันนี้คือ {format_thai_date(today)} ตามเวลาไทย",
        "หมายเหตุ: วันหยุดไทย/เทศกาลเป็นข้อมูลปฏิทินประกอบ ส่วนการปิดบริการจริงให้ดู service_closures.jsonl",
        f"แหล่งข้อมูลปฏิทินไทย: {THAI_HOLIDAY_SOURCE_URL}",
        f"แหล่งข้อมูลตารางบริการ: {RESERVATION_URL}",
    ])
    return _answer("\n".join(lines), "reservation", "calendar_month_context_fast_path", start, 0.98)


def _holiday_type_counts(items: list[object]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for item in items:
        item_type = str(getattr(item, "type", "unknown"))
        counts[item_type] = counts.get(item_type, 0) + 1
    return dict(sorted(counts.items(), key=lambda row: row[0]))


def _year_holiday_answer(q: str, start: float, year: int, label: str) -> FastAnswer:
    today = today_bangkok()
    holidays = holidays_for_year(year)
    closures = closures_for_year(year)
    count_only = _has(q, "กี่วัน", "กี่รายการ", "จำนวน", "ทั้งหมดกี่", "นับ")
    asks_list = _has(q, "อะไรบ้าง", "ไหนบ้าง", "วันไหน", "มีอะไร", "รายชื่อ", "ลิสต์", "list")
    counts = _holiday_type_counts(holidays)
    official_like_count = sum(counts.get(kind, 0) for kind in ("national_holiday", "government_holiday", "bank_holiday_bangkok"))

    if not holidays:
        lines = [
            f"{label} ยังไม่พบข้อมูลวันหยุดไทย/เทศกาลในไฟล์ปฏิทินที่บันทึกไว้",
            "ตอนนี้ระบบตอบได้จากข้อมูล local ที่มีอยู่เท่านั้น จึงไม่ควรเดาวันหยุดของปีที่ยังไม่มีข้อมูล",
            f"วันที่อ้างอิงของระบบ: วันนี้คือ {format_thai_date(today)} ตามเวลาไทย",
            f"แหล่งข้อมูลปฏิทินไทย: {THAI_HOLIDAY_SOURCE_URL}",
        ]
        return _answer("\n".join(lines), "reservation", "calendar_year_context_no_data_fast_path", start, 0.94)

    if count_only:
        lines = [f"{label} มีวันหยุด/วันหยุดราชการในข้อมูลที่บันทึกไว้ {official_like_count} รายการ และมีรายการปฏิทินไทยรวม {len(holidays)} รายการ"]
    else:
        lines = [f"{label} มีข้อมูลปฏิทินไทย {len(holidays)} รายการ"]
    if counts:
        counts_text = ", ".join(f"{key} {value} รายการ" for key, value in counts.items())
        lines.append(f"แยกตามประเภท: {counts_text}")
    lines.append(f"มีวันปิดให้บริการของศูนย์ในไฟล์ service_closures.jsonl {len(closures)} วัน")

    if asks_list or not count_only:
        lines.append("")
        lines.append("รายการในปฏิทิน:")
        for item in holidays:
            value = date.fromisoformat(item.date)
            note = f" - {item.note}" if item.note else ""
            lines.append(f"- {format_thai_date(value)}: {item.title} ({item.type}){note}")

    if closures:
        lines.append("")
        lines.append("วันปิดให้บริการของศูนย์ที่บันทึกไว้:")
        for item in closures:
            value = date.fromisoformat(item.date)
            note = f" - {item.note}" if item.note else ""
            lines.append(f"- {format_thai_date(value)}: {item.title}{note}")

    lines.extend([
        f"วันที่อ้างอิงของระบบ: วันนี้คือ {format_thai_date(today)} ตามเวลาไทย",
        "หมายเหตุ: วันหยุดไทย/เทศกาลเป็นข้อมูลปฏิทินประกอบ ส่วนการปิดบริการจริงให้ดู service_closures.jsonl",
        f"แหล่งข้อมูลปฏิทินไทย: {THAI_HOLIDAY_SOURCE_URL}",
        f"แหล่งข้อมูลตารางบริการ: {RESERVATION_URL}",
    ])
    return _answer("\n".join(lines), "reservation", "calendar_year_context_fast_path", start, 0.98)


def _is_next_week_query(q: str) -> bool:
    return _has(q, "สัปดาห์หน้า", "อาทิตย์หน้า", "weekหน้า", "next week")


def _next_week_bounds(today: date) -> tuple[date, date]:
    next_monday = today + timedelta(days=(7 - today.weekday()))
    return next_monday, next_monday + timedelta(days=6)


def _week_calendar_answer(q: str, start: float) -> FastAnswer | None:
    if not _is_next_week_query(q):
        return None
    today = today_bangkok()
    start_date, end_date = _next_week_bounds(today)
    asks_service = _has(q, "เล่น", "เปิด", "ปิด", "ให้บริการ", "จอง", "รอบ")
    holidays: list[object] = []
    closures: list[object] = []
    current = start_date
    while current <= end_date:
        holidays.extend(holidays_for_date(current))
        closure = closure_for(current)
        if closure and closure.status == "closed":
            closures.append(closure)
        current += timedelta(days=1)

    lines = [
        f"อาทิตย์หน้าในระบบนี้คือ {format_thai_date(start_date)} ถึง {format_thai_date(end_date)}",
    ]
    if holidays:
        lines.append("วันหยุดไทย/เทศกาลที่พบในช่วงนี้:")
        for item in holidays:
            value = date.fromisoformat(getattr(item, "date"))
            lines.append(f"- {format_thai_date(value)}: {getattr(item, 'title')} ({getattr(item, 'type')})")
    else:
        lines.append("ยังไม่พบวันหยุดไทย/เทศกาลในปฏิทินที่บันทึกไว้สำหรับอาทิตย์หน้า")

    if closures:
        lines.append("วันปิดให้บริการของศูนย์ที่บันทึกไว้ในช่วงนี้:")
        for item in closures:
            value = date.fromisoformat(getattr(item, "date"))
            note = f" - {getattr(item, 'note')}" if getattr(item, "note", "") else ""
            lines.append(f"- {format_thai_date(value)}: {getattr(item, 'title')}{note}")
    else:
        lines.append("ยังไม่พบวันปิดพิเศษของศูนย์ในไฟล์ service_closures.jsonl สำหรับอาทิตย์หน้า")

    if asks_service:
        lines.extend([
            "",
            "ถ้าไม่มีวันปิดพิเศษ ให้ดูตามตารางประจำ:",
        ])
        current = start_date
        while current <= end_date:
            lines.append(f"- {format_thai_date(current)}: {regular_service_summary(current)}")
            current += timedelta(days=1)

    lines.extend([
        f"วันที่อ้างอิงของระบบ: วันนี้คือ {format_thai_date(today)} ตามเวลาไทย",
        "หมายเหตุ: วันหยุดไทย/เทศกาลเป็นข้อมูลปฏิทินประกอบ ไม่ได้แปลว่าศูนย์ปิดโดยอัตโนมัติ",
        f"แหล่งข้อมูลปฏิทินไทย: {THAI_HOLIDAY_SOURCE_URL}",
        f"แหล่งข้อมูลตารางบริการ: {RESERVATION_URL}",
    ])
    return _answer("\n".join(lines), "reservation", "calendar_week_context_fast_path", start, 0.98)


def _calendar_schedule_answer(q: str, start: float) -> FastAnswer | None:
    if not has_date_or_holiday_intent(q):
        return None

    today = today_bangkok()
    if _has(q, "ตอนนี้", "ขณะนี้", "เวลานี้", "กี่โมงแล้ว", "ตอนนี้กี่โมง"):
        return _current_service_answer(q, start)

    asks_calendar_only = _has(q, "วันที่เท่าไหร่", "วันที่เท่าไร", "วันอะไร", "วันหยุดอะไร", "วันหยุดไทยไหม", "เทศกาลอะไร", "ปฏิทิน")
    asks_service_status = _has(q, "เปิด", "ปิด", "เล่นได้", "ให้บริการ", "จอง", "รอบ")

    week_answer = _week_calendar_answer(q, start)
    if week_answer is not None:
        return week_answer

    asks_list = _has(q, "วันไหน", "วันอะไร", "วันหยุดบ้าง", "วันหยุดอะไรบ้าง", "หยุดบ้าง", "ปิดบ้าง", "หยุดวันไหน", "ปิดวันไหน", "มีวันหยุด", "มีวันหยุดอะไร", "เทศกาลบ้าง", "อะไรบ้าง", "กี่วัน", "กี่รายการ", "จำนวน")
    month_resolution = resolve_month_from_text(q, today=today)
    if month_resolution is not None and _has(q, "วันหยุด", "วันหยุดไทย", "เทศกาล", "ปฏิทิน", "วันหยุดบ้าง", "มีวันหยุด", "เดือนนี้", "เดือนหน้า", "เดือนที่แล้ว", "เดือนก่อน", "อะไรบ้าง", "กี่วัน", "กี่รายการ"):
        return _month_holiday_answer(q, start, month_resolution.year, month_resolution.month, month_resolution.label)

    year_resolution = resolve_year_from_text(q, today=today)
    if year_resolution is not None and _has(q, "วันหยุด", "วันหยุดไทย", "เทศกาล", "ปฏิทิน", "กี่วัน", "กี่รายการ", "อะไรบ้าง", "วันไหน"):
        return _year_holiday_answer(q, start, year_resolution.year, year_resolution.label)

    if asks_list and month_resolution is not None:
        closures = closures_for_month(month_resolution.year, month_resolution.month)
        current_line = f"วันที่อ้างอิงของระบบ: วันนี้คือ {format_thai_date(today)} ตามเวลาไทย"
        if closures:
            lines = [f"{month_resolution.label} มีวันปิดให้บริการ {len(closures)} วัน:"]
            for item in closures:
                value = date.fromisoformat(item.date)
                note = f" - {item.note}" if item.note else ""
                lines.append(f"- {format_thai_date(value)}: {item.title}{note}")
            lines.extend([
                current_line,
                "หมายเหตุ: รายการนี้มาจากไฟล์วันปิดพิเศษ/วันหยุดราชการของระบบ และจะ override ตารางเปิดปิดปกติ",
                f"แหล่งข้อมูลตารางบริการ: {RESERVATION_URL}",
                "แหล่งข้อมูลวันปิด: data/calendar/service_closures.jsonl",
            ])
            return _answer("\n".join(lines), "reservation", "calendar_closure_list_fast_path", start, 0.99)
        lines = [
            f"{month_resolution.label} ยังไม่พบวันปิดพิเศษ/วันหยุดราชการในไฟล์ปฏิทินของระบบ",
            current_line,
            "ถ้าไม่มีวันปิดพิเศษ ให้ดูตามตารางปกติ: จันทร์บ่ายเปิด, อังคาร-พฤหัสเปิดทั้งเช้า/บ่าย, ศุกร์เช้าเปิดและบ่าย Maintenance",
            f"แหล่งข้อมูลตารางบริการ: {RESERVATION_URL}",
            "แหล่งข้อมูลวันปิด: data/calendar/service_closures.jsonl",
        ]
        return _answer("\n".join(lines), "reservation", "calendar_closure_list_fast_path", start, 0.97)

    resolved = resolve_date_from_text(q, today=today)
    if resolved is None:
        if _has(q, "วันนี้", "today"):
            resolved = resolve_date_from_text("วันนี้", today=today)
        elif _has(q, "วันหยุด", "เทศกาล"):
            upcoming = next_holidays(today, limit=5)
            lines = ["วันหยุดไทย/เทศกาลถัดไปที่มีในปฏิทิน:"]
            for item in upcoming:
                value = date.fromisoformat(item.date)
                lines.append(f"- {format_thai_date(value)}: {item.title} ({item.type})")
            lines.extend([
                "หมายเหตุ: รายการนี้เป็นข้อมูลปฏิทินไทยประกอบ ไม่ได้แปลว่าศูนย์ปิดโดยอัตโนมัติ",
                f"แหล่งข้อมูลปฏิทินไทย: {THAI_HOLIDAY_SOURCE_URL}",
            ])
            return _answer("\n".join(lines), "reservation", "calendar_upcoming_holidays_fast_path", start, 0.96)
        else:
            return None

    target = resolved.target_date
    if asks_calendar_only and not asks_service_status:
        return _date_calendar_answer(q, start, target, label_prefix=resolved.label)

    closure = closure_for(target)
    current_line = f"วันที่อ้างอิงของระบบ: วันนี้คือ {format_thai_date(today)} ตามเวลาไทย"

    if closure and closure.status == "closed":
        first = f"{resolved.label}: ศูนย์ปิดให้บริการ ({closure.title})"
        lines = [
            first,
            closure.note,
            current_line,
            "หมายเหตุ: วันปิดพิเศษ/วันหยุดราชการจะ override ตารางเปิดปิดปกติ",
            f"แหล่งข้อมูลตารางบริการ: {RESERVATION_URL}",
            f"แหล่งข้อมูลวันปิด: {closure.source}",
        ]
        return _answer("\n".join(line for line in lines if line), "reservation", "calendar_closure_fast_path", start, 0.99)

    weekday = target.weekday()
    summary = regular_service_summary(target)
    if weekday <= 4:
        first = f"{resolved.label}: {summary}"
    else:
        first = f"{resolved.label}: {summary}"

    if _has(q, "เปิดไหม", "เปิดรึเปล่า", "เปิดหรือเปล่า", "เล่นได้ไหม", "ให้บริการไหม", "ปิดไหม"):
        lines = [first]
    else:
        lines = [first]

    lines.extend([
        current_line,
        "",
        "ปฏิทินไทยของวันที่นี้:",
        _holiday_text(holidays_for_date(target)),
        "",
        "รายละเอียดจากตาราง:",
        "- วันจันทร์ช่วงเช้า 09:00-12:00 เป็น Maintenance* และเปิดช่วงบ่าย 13:00-16:00",
        "- วันอังคาร-พฤหัสบดีเปิด 09:00-12:00 และ 13:00-16:00",
        "- วันศุกร์เปิดช่วงเช้า 09:00-12:00 และช่วงบ่าย 13:00-16:00 เป็น Maintenance",
        "- วันหยุดราชการ/วันปิดพิเศษในไฟล์ปฏิทินจะมีผลก่อนตารางปกติ",
        f"แหล่งข้อมูลตารางบริการ: {RESERVATION_URL}",
    ])
    game_context = _game_context_for_schedule(q)
    if game_context:
        lines = [game_context, ""] + lines
    return _answer("\n".join(lines), "reservation", "calendar_schedule_fast_path", start, 0.98)


def answer_schedule(query: str, start: float) -> FastAnswer | None:
    q = normalize_text(query)
    schedule_terms = [
        "เปิด", "ปิด", "เล่นได้", "เล่นกี่โมง", "กี่โมง", "ช่วงไหน", "เวลา", "service hours", "opening", "closing", "morning", "afternoon",
        "รอบเช้า", "ช่วงเช้า", "ตอนเช้า", "รอบบ่าย", "ช่วงบ่าย", "maintenance", "hardware inspection",
        "cleaning", "24 ชม", "24 ชั่วโมง", "24 hours", "วันจัน", "จันทร์", "monday",
        "อังคาร", "tuesday", "tue", "พุธ", "wednesday", "wed", "พฤหัส", "พฤหัสบดี", "thursday", "thu",
        "ศุกร์", "friday", "วันนี้", "พรุ่งนี้", "มะรืน", "today", "วันหยุด", "หยุด", "หยุดบ้าง", "ราชการ", "ปฏิทิน", "เดือนนี้", "เดือนหน้า",
        "เดือนที่แล้ว", "เดือนก่อน", "ปีนี้", "ปีหน้า", "ปีที่แล้ว", "ปีก่อน", "วันที่เท่าไหร่", "วันที่เท่าไร", "วันอะไร", "อีก", "ข้างหน้า", "ถัดไป",
        "มกราคม", "มกรา", "กุมภาพันธ์", "กุมภา", "มีนาคม", "มีนา", "เมษายน", "เมษา", "พฤษภาคม", "พฤษภา", "มิถุนายน", "มิถุนา",
        "กรกฎาคม", "กรกฎา", "สิงหาคม", "สิงหา", "กันยายน", "กันยา", "ตุลาคม", "ตุลา", "พฤศจิกายน", "พฤศจิกา", "ธันวาคม", "ธันวา",
        "ก.ค.", "กค",
    ]
    if not _has(q, *schedule_terms):
        return None
    if _match_supported_game(q) and _looks_like_game_availability(q) and not has_date_or_holiday_intent(q):
        return None

    calendar_answer = _calendar_schedule_answer(q, start)
    if calendar_answer is not None:
        return calendar_answer

    has_monday = _has(q, "วันจัน", "จันทร์", "monday")
    has_friday = _has(q, "ศุกร์", "friday")
    regular_weekday = _regular_weekday_label(q)
    has_morning = _has(q, "รอบเช้า", "ช่วงเช้า", "ตอนเช้า", "morning", "09:00", "9:00", "09 ถึง 12", "9 ถึง 12")
    has_afternoon = _has(q, "รอบบ่าย", "ช่วงบ่าย", "ตอนบ่าย", "afternoon", "13:00", "13 ถึง 16")

    if has_monday:
        if has_morning and not has_afternoon:
            first = "วันจันทร์ช่วงเช้า 09:00-12:00 ยังไม่เปิดให้เล่น เพราะเป็นช่วง Maintenance*"
        elif has_afternoon and not has_morning:
            first = "วันจันทร์ช่วงบ่ายเปิดให้เล่น 13:00-16:00"
        elif has_morning and has_afternoon:
            first = "วันจันทร์ Morning เล่นไม่ได้ เพราะ 09:00-12:00 เป็น Maintenance* ส่วน Afternoon เปิดให้เล่น 13:00-16:00"
        else:
            first = "วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*"
        text = _schedule_text(first, q)
        return _answer(text, "reservation", "schedule_fast_path", start, 0.98)

    if regular_weekday:
        if has_morning and not has_afternoon:
            first = f"{regular_weekday}ช่วงเช้าเปิดให้เล่น 09:00-12:00"
        elif has_afternoon and not has_morning:
            first = f"{regular_weekday}ช่วงบ่ายเปิดให้เล่น 13:00-16:00"
        elif has_morning and has_afternoon:
            first = f"{regular_weekday}เปิดทั้งรอบเช้า 09:00-12:00 และรอบบ่าย 13:00-16:00"
        else:
            first = f"{regular_weekday}เล่นได้ 09:00-12:00 และ 13:00-16:00 โดยรอบสุดท้ายสิ้นสุด 16:00"
        text = _regular_weekday_schedule_text(first, q)
        return _answer(text, "reservation", "schedule_fast_path", start, 0.98)

    if has_friday:
        if has_afternoon and not has_morning:
            first = "วันศุกร์ช่วงบ่าย 13:00-16:00 เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์ จึงไม่ควรนับเป็นช่วงเล่นปกติ"
        elif has_morning and not has_afternoon:
            first = "วันศุกร์ช่วงเช้าใช้ช่วงเวลา 09:00-12:00 ส่วนช่วงบ่าย 13:00-16:00 เป็น Maintenance"
        elif has_morning and has_afternoon:
            first = "วันศุกร์ Morning ใช้ช่วงเวลา 09:00-12:00 ส่วน Afternoon 13:00-16:00 เป็น Maintenance จึงไม่ใช่ช่วงเล่นปกติ"
        else:
            first = "วันศุกร์ให้ดูเป็นพิเศษ: ช่วงบ่าย 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning"
        text = _schedule_text(first, q)
        return _answer(text, "reservation", "schedule_fast_path", start, 0.98)

    if _has(q, "24 ชม", "24 ชั่วโมง", "24 hours", "เปิด 24"):
        first = "ไม่เปิด 24 ชั่วโมง ตามข้อมูลที่มี ศูนย์ใช้ช่วงเวลา Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยต้องดูวัน Maintenance ประกอบ"
        text = _schedule_text(first, q)
        return _answer(text, "reservation", "schedule_fast_path", start, 0.98)

    if has_morning and not has_afternoon:
        first = "รอบเช้า/Morning คือ 09:00-12:00 แต่ถ้าเป็นวันจันทร์ช่วงนี้เป็น Maintenance*"
        text = _schedule_text(first, q)
        return _answer(text, "reservation", "schedule_fast_path", start, 0.97)

    if has_afternoon and not has_morning:
        first = "รอบบ่าย/Afternoon คือ 13:00-16:00 แต่ถ้าเป็นวันศุกร์ช่วงนี้เป็น Maintenance สำหรับตรวจเช็คและทำความสะอาดอุปกรณ์"
        text = _schedule_text(first, q)
        return _answer(text, "reservation", "schedule_fast_path", start, 0.97)

    q_without_open = q.replace("เปิด", "")
    has_open_intent = _has(q, "เปิด", "opening", "service hours")
    has_close_intent = _has(q_without_open, "ปิด", "closing", "ถึงกี่โมง")
    if has_open_intent and has_close_intent:
        first = "เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยวันจันทร์ช่วงเช้าเป็น Maintenance* และวันศุกร์ช่วงบ่ายเป็น Maintenance"
    elif has_close_intent:
        first = "โดยทั่วไปเวลาสิ้นสุดช่วงบริการคือ 16:00 แต่วันศุกร์ช่วงบ่าย 13:00-16:00 เป็น Maintenance จึงควรดูวันประกอบ"
    elif has_open_intent:
        first = "เวลาที่มีในตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 แต่วันจันทร์ช่วงเช้าเป็น Maintenance*"
    else:
        first = "เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน"
    text = _schedule_text(first, q)
    return _answer(text, "reservation", "schedule_fast_path", start, 0.96)


def _detect_group(q: str) -> str | None:
    # User may add style phrases such as "แบบภาษาคนทั่วไป". Do not let that
    # override an explicit group like "เด็ก มอ", "สจล", or "ต่างมหาลัย".
    for phrase in ("แบบภาษาคนทั่วไป", "ภาษาคนทั่วไป", "พูดแบบคนทั่วไป", "ตอบแบบคนทั่วไป"):
        q = q.replace(phrase, "")
    if _has(
        q,
        "นักศึกษา มอ", "นักเรียน มอ", "เด็ก มอ", "นิสิต มอ",
        "นักศึกษา psu", "นักเรียน psu", "เด็ก psu", "psu student", "psu staff",
        "บุคลากร psu", "บุคลากร มอ", "มหาวิทยาลัยสงขลานครินทร์", "สงขลานครินทร์",
    ):
        return "psu"
    if _has(q, "ไม่ใช่มอ", "ไม่ใช่ มอ", "ไม่ได้เรียนมอ", "ไม่ได้เรียน มอ"):
        return "general_student"
    if not _has(
        q,
        "นักศึกษา", "นักเรียน", "นิสิต", "เด็ก", "student", "staff",
        "psu", "สงขลานครินทร์", "บุคคลทั่วไป", "คนทั่วไป",
        "ต่างมหาลัย", "มหาลัย", "มหาวิทยาลัย", "สจล", "ลาดกระบัง",
        "จุฬา", "ธรรมศาสตร์", "เกษตร", "เชียงใหม่", "ขอนแก่น",
        "kmitl", "chula", "tu", "ku", "cmu", "kku", "mahidol",
    ):
        return None
    if (
        _has(q, "นักเรียน", "นักศึกษา", "นิสิต", "เด็ก", "student")
        and not _has(
            q,
            "มอ", "psu", "สงขลานครินทร์", "บุคลากร",
            "ต่างมหาลัย", "ต่างมหาวิทยาลัย", "ต่างสถาบัน", "ศิษย์เก่า",
            "สจล", "ลาดกระบัง", "จุฬา", "ธรรมศาสตร์", "เกษตร", "เชียงใหม่", "ขอนแก่น",
            "มหิดล", "ราชภัฏ", "ราชมงคล", "เทคนิค", "อาชีวะ",
            "kmitl", "chula", "tu", "ku", "cmu", "kku", "mahidol",
            "บุคคลทั่วไป", "คนทั่วไป", "ผู้ใหญ่", "general adult", "adult", "คนออก", "ประชาชน",
        )
    ):
        return "general_student"
    group = detect_from_aliases(q, CUSTOMER_GROUP_ALIASES)
    if group["key"] == "psu_student_staff" and not group["ambiguous"]:
        return "psu"
    if group["key"] == "general_student" and not group["ambiguous"]:
        return "general_student"
    if group["key"] == "general_adult" and not group["ambiguous"]:
        return "adult"
    if _has(q, "นักเรียน", "นักศึกษา", "นิสิต", "เด็ก", "student"):
        return "general_student"
    return None


def _pc_price_text(q: str) -> str:
    group = _detect_group(q)
    if group == "psu":
        group_line = "กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff"
    elif group == "general_student":
        group_line = "กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น"
    elif group == "adult":
        group_line = "กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป"
    elif "นักเรียน" in q or "นักศึกษา" in q:
        group_line = "กลุ่มผู้ใช้ยังไม่ชัดว่าเป็น PSU หรือต่างสถาบัน"
    else:
        group_line = ""
    if group:
        lines = [f"ราคา PC 1 ชั่วโมง สำหรับ {GROUP_NAMES[group]}: {PRICE_VALUES['pc'][group]:,} บาท"]
    else:
        lines = ["ราคา PC 1 ชั่วโมง (1 คน)"]
        for group_key in ("psu", "general_student", "adult"):
            lines.append(f"•    {GROUP_NAMES[group_key]}: {PRICE_VALUES['pc'][group_key]:,} บาท")
    if group_line:
        lines.append(group_line)
    lines.append("หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27")
    return "\n".join(lines)


def _service_rows_for_query(q: str) -> list[str]:
    rows: list[str] = []
    if _has(q, "pc", "คอม", "คอมพิวเตอร์"):
        rows.append(PRICE_ROWS["pc"])
    if _has(q, "ps5", "playstation", "เพลย์", "เพลย์ห้า"):
        rows.append(PRICE_ROWS["ps5"])
    if _has(q, "nintendo", "switch", "สวิตช์", "สวิทช์", "นินเทนโด"):
        if _has(q, "3-4", "3 ถึง 4", "3 คน", "4 คน"):
            rows.append(PRICE_ROWS["switch_3_4"])
        elif _has(q, "1-2", "1 ถึง 2", "1 คน", "2 คน"):
            rows.append(PRICE_ROWS["switch_1_2"])
        else:
            rows.extend([PRICE_ROWS["switch_1_2"], PRICE_ROWS["switch_3_4"]])
    if _has(q, "cockpit", "พวงมาลัย", "ขับรถ"):
        rows.append(PRICE_ROWS["cockpit"])
    if _has(q, "vr", "วีอาร์", "แว่น"):
        has_vr_30 = _has(q, "30 นาที", "ครึ่ง", "ครึ่งชม", "ครึ่งชั่วโมง")
        has_vr_60 = _has(q, "1 ชั่วโมง", "60 นาที", "หนึ่งชั่วโมง")
        if has_vr_30 and has_vr_60:
            rows.extend([PRICE_ROWS["vr_30"], PRICE_ROWS["vr_60"]])
        elif has_vr_60:
            rows.append(PRICE_ROWS["vr_60"])
        elif has_vr_30:
            rows.append(PRICE_ROWS["vr_30"])
        else:
            rows.extend([PRICE_ROWS["vr_30"], PRICE_ROWS["vr_60"]])
    return rows


def _service_keys_for_query(q: str) -> list[str]:
    keys: list[str] = []
    if _has(q, "pc", "คอม", "คอมพิวเตอร์"):
        keys.append("pc")
    if _has(q, "ps5", "playstation", "เพลย์", "เพลย์ห้า"):
        keys.append("ps5")
    if _has(q, "nintendo", "switch", "สวิตช์", "สวิทช์", "นินเทนโด"):
        if _has(q, "3-4", "3 ถึง 4", "3 คน", "4 คน"):
            keys.append("switch_3_4")
        elif _has(q, "1-2", "1 ถึง 2", "1 คน", "2 คน"):
            keys.append("switch_1_2")
        else:
            keys.extend(["switch_1_2", "switch_3_4"])
    if _has(q, "cockpit", "พวงมาลัย", "ขับรถ"):
        keys.append("cockpit")
    if _has(q, "vr", "วีอาร์", "แว่น"):
        has_vr_30 = _has(q, "30 นาที", "ครึ่ง", "ครึ่งชม", "ครึ่งชั่วโมง")
        has_vr_60 = _has(q, "1 ชั่วโมง", "60 นาที", "หนึ่งชั่วโมง")
        if has_vr_30 and has_vr_60:
            keys.extend(["vr_30", "vr_60"])
        elif has_vr_60:
            keys.append("vr_60")
        elif has_vr_30:
            keys.append("vr_30")
        else:
            keys.extend(["vr_30", "vr_60"])
    return keys


def _student_fee_overview_answer(q: str, group: str | None) -> str | None:
    if not _has(q, "บัตรนักศึกษา", "นักศึกษา", "นักเรียน", "นิสิต", "student", "บัตร"):
        return None
    if not _has(q, "ฟรี", "0 บาท", "ไม่เสียเงิน", "ต้องจ่ายไหม", "จ่ายไหม", "เสียเงินไหม", "ค่าใช้จ่าย", "ค่าบริการ"):
        return None
    if not _has(q, "เล่น", "ใช้บริการ", "เข้าใช้", "จอง"):
        return None

    return (
        "ไม่ใช่ทุกบัตรนักศึกษาจะเล่นฟรีครับ ต้องดูว่าเป็นกลุ่มผู้ใช้แบบไหน\n"
        "•    PSU Student and Staff: ตาราง Service Fee 2026 ระบุราคา 0 บาทสำหรับ PlayStation 5, Nintendo Switch, Cockpit และ VR\n"
        "•    PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน: ยังมีค่าบริการ เช่น PlayStation 5 50 บาท, Nintendo Switch 50/100 บาท, Cockpit 65 บาท, VR 190/375 บาท\n"
        "•    General Adult: มีค่าบริการตามตารางผู้ใหญ่ทั่วไป\n"
        "•    PC 1 ชั่วโมง: PSU Student and Staff 0 บาท, PSU Alumni and General Student 25 บาท, General Adult 70 บาท"
    )


def _price_answer_focus(q: str, group: str | None) -> str | None:
    selected_group = group or "general_student"
    group_name = GROUP_NAMES[selected_group]
    service_keys = _service_keys_for_query(q)

    if _has(q, "ต่างกัน", "ต่างกันเท่าไหร่", "ต่างกันเท่าไร", "ห่างกันกี่บาท", "แพงกว่ากี่บาท") and len(service_keys) == 2:
        first_key, second_key = service_keys
        first_label = PRICE_LABELS[first_key]
        second_label = PRICE_LABELS[second_key]
        if group:
            first_price = PRICE_VALUES[first_key][group]
            second_price = PRICE_VALUES[second_key][group]
            diff = abs(first_price - second_price)
            if first_price == second_price:
                verdict = f"{first_label} กับ {second_label} ราคาเท่ากันที่ {first_price:,} บาท"
            else:
                higher_label = first_label if first_price > second_price else second_label
                lower_label = second_label if first_price > second_price else first_label
                verdict = f"ต่างกัน {diff:,} บาท โดย {higher_label} แพงกว่า {lower_label}"
            return (
                f"{verdict} สำหรับกลุ่ม {group_name}\n"
                f"•    {first_label}: {first_price:,} บาท\n"
                f"•    {second_label}: {second_price:,} บาท"
            )
        lines = [f"ราคา {first_label} กับ {second_label} ต่างกันดังนี้:"]
        for group_key in ("psu", "general_student", "adult"):
            first_price = PRICE_VALUES[first_key][group_key]
            second_price = PRICE_VALUES[second_key][group_key]
            diff = abs(first_price - second_price)
            if first_price == second_price:
                verdict = f"ราคาเท่ากันที่ {first_price:,} บาท"
            else:
                higher_label = first_label if first_price > second_price else second_label
                verdict = f"{higher_label} แพงกว่า {diff:,} บาท"
            lines.append(f"•    {GROUP_NAMES[group_key]}: {verdict} ({first_label} {first_price:,} บาท / {second_label} {second_price:,} บาท)")
        return "\n".join(lines)

    if _has(q, "vr") and _has(q, "ต่างกัน", "ต่างกันเท่าไหร่", "ต่างกันเท่าไร") and _has(q, "30", "ครึ่ง") and _has(q, "1 ชั่วโมง", "60"):
        short_price = PRICE_VALUES["vr_30"][selected_group]
        long_price = PRICE_VALUES["vr_60"][selected_group]
        diff = long_price - short_price
        return (
            f"ต่างกัน {diff} บาท สำหรับกลุ่ม {group_name}\n"
            f"- VR 30 นาที ราคา {short_price} บาท\n"
            f"- VR 1 ชั่วโมง ราคา {long_price} บาท\n"
            f"ดังนั้น VR 1 ชั่วโมงแพงกว่า VR 30 นาที {diff} บาท"
        )

    if _has(q, "แพงกว่า") and _has(q, "switch", "nintendo") and _has(q, "cockpit", "พวงมาลัย"):
        switch_key = "switch_3_4" if _has(q, "3-4", "3 คน", "4 คน") else "switch_1_2"
        switch_price = PRICE_VALUES[switch_key][selected_group]
        cockpit_price = PRICE_VALUES["cockpit"][selected_group]
        if switch_price == cockpit_price:
            verdict = f"ราคาเท่ากันที่ {switch_price} บาท"
        else:
            higher = "Nintendo Switch 3-4 คน" if switch_price > cockpit_price else "Cockpit"
            diff = abs(switch_price - cockpit_price)
            verdict = f"{higher} แพงกว่า {diff} บาท"
        return (
            f"{verdict} สำหรับกลุ่ม {group_name}\n"
            f"- Nintendo Switch 3-4 คน ราคา {switch_price} บาท\n"
            f"- Cockpit ราคา {cockpit_price} บาท"
        )

    if _has(q, "เท่ากันไหม") and _has(q, "ps5", "playstation") and _has(q, "nintendo", "switch"):
        ps5_price = PRICE_VALUES["ps5"][selected_group]
        switch_price = PRICE_VALUES["switch_1_2"][selected_group]
        verdict = "เท่ากัน" if ps5_price == switch_price else f"ไม่เท่ากัน ต่างกัน {abs(ps5_price - switch_price)} บาท"
        return (
            f"{verdict} สำหรับกลุ่ม {group_name}\n"
            f"- PlayStation 5 ราคา {ps5_price} บาท\n"
            f"- Nintendo Switch 1-2 คน ราคา {switch_price} บาท"
        )

    if _has(q, "ต้องจ่ายไหม", "ฟรีไหม") and _has(q, "vr") and _has(q, "1 ชั่วโมง", "60"):
        price = PRICE_VALUES["vr_60"][selected_group]
        verdict = "ไม่ต้องจ่าย ราคา 0 บาท" if price == 0 else f"ต้องจ่าย {price} บาท"
        return (
            f"{verdict} สำหรับกลุ่ม {group_name}\n"
            f"- VR 1 ชั่วโมง ราคา {price} บาท"
        )

    return None


def _group_context_line(q: str, group: str) -> str:
    if group == "general_student":
        return "กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น"
    if group == "psu":
        return "กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff"
    if group == "adult":
        return "กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป"
    return ""


def _detect_price_duration_minutes(q: str) -> int | None:
    range_match = re.search(
        r"(\d{1,2})(?::(\d{2}))?\s*(?:โมง|น\.?)?\s*(?:ถึง|จนถึง|-|to)\s*(\d{1,2})(?::(\d{2}))?\s*(?:โมง|น\.?)?",
        q,
    )
    if range_match:
        start_total = int(range_match.group(1)) * 60 + int(range_match.group(2) or 0)
        end_total = int(range_match.group(3)) * 60 + int(range_match.group(4) or 0)
        if end_total > start_total:
            return end_total - start_total

    hour_match = re.search(r"(\d+(?:\.\d+)?)\s*(?:ชั่วโมง|ชม|hour|hr)", q)
    if hour_match:
        return int(float(hour_match.group(1)) * 60)
    minute_match = re.search(r"(\d+)\s*(?:นาที|min|minutes?)", q)
    if minute_match:
        return int(minute_match.group(1))
    return None


def _session_count_for_price_key(key: str, minutes: int) -> int:
    unit_minutes = 30 if key == "vr_30" else 60
    return max(1, (minutes + unit_minutes - 1) // unit_minutes)


def _time_range_overlap(q: str, start_hour: int, end_hour: int) -> bool:
    range_match = re.search(
        r"(\d{1,2})(?::(\d{2}))?\s*(?:โมง|น\.?)?\s*(?:ถึง|จนถึง|-|to)\s*(\d{1,2})(?::(\d{2}))?\s*(?:โมง|น\.?)?",
        q,
    )
    if not range_match:
        return False
    ask_start = int(range_match.group(1)) * 60 + int(range_match.group(2) or 0)
    ask_end = int(range_match.group(3)) * 60 + int(range_match.group(4) or 0)
    return ask_start < end_hour * 60 and ask_end > start_hour * 60


def _time_range_session_labels(q: str) -> list[str]:
    range_match = re.search(
        r"(\d{1,2})(?::(\d{2}))?\s*(?:โมง|น\.?)?\s*(?:ถึง|จนถึง|-|to)\s*(\d{1,2})(?::(\d{2}))?\s*(?:โมง|น\.?)?",
        q,
    )
    if not range_match:
        return []
    start_total = int(range_match.group(1)) * 60 + int(range_match.group(2) or 0)
    end_total = int(range_match.group(3)) * 60 + int(range_match.group(4) or 0)
    if end_total <= start_total:
        return []
    labels: list[str] = []
    current = start_total
    while current < end_total and len(labels) < 12:
        next_value = min(current + 60, end_total)
        labels.append(f"{current // 60:02d}:{current % 60:02d}-{next_value // 60:02d}:{next_value % 60:02d}")
        current = next_value
    return labels


def _booking_window_note(q: str) -> str:
    monday = _has(q, "วันจัน", "จันทร์", "จัน", "จัทร์", "monday")
    friday = _has(q, "ศุกร์", "friday")
    if monday and _time_range_overlap(q, 9, 12):
        return "ช่วงที่ถามจองไม่ได้ครับ เพราะวันจันทร์ 09:00-12:00 เป็นช่วง Maintenance ไม่ใช่ Open for Service"
    if friday and _time_range_overlap(q, 13, 16):
        return "ช่วงที่ถามจองไม่ได้ครับ เพราะวันศุกร์ 13:00-16:00 เป็นช่วง Maintenance สำหรับ Weekly hardware inspection and cleaning"
    return ""


def _duration_price_answer(q: str, group: str | None) -> str | None:
    minutes = _detect_price_duration_minutes(q)
    if minutes is None:
        return None
    keys = _service_keys_for_query(q)
    if len(keys) != 1:
        return None

    key = keys[0]
    sessions = _session_count_for_price_key(key, minutes)
    label = PRICE_LABELS[key]
    window_note = _booking_window_note(q)
    session_labels = _time_range_session_labels(q)
    hours_label = f"{minutes // 60} ชั่วโมง" if minutes % 60 == 0 else f"{minutes} นาที"
    lines: list[str] = []

    lines.append(f"ระยะเวลาที่ถามคือ {hours_label} ใช้ {sessions} session ตามแพ็กเกจ {label}")
    if session_labels:
        lines.append("แบ่งช่วงเวลาเป็น: " + ", ".join(session_labels))

    if group:
        price = PRICE_VALUES[key][group]
        total = price * sessions
        lines.append(f"คำตอบราคา: {total} บาท สำหรับกลุ่ม {GROUP_NAMES[group]}")
        lines.append(f"- คำนวณจาก {price} บาท/session x {sessions} session = {total} บาท")
        group_context = _group_context_line(q, group)
        if group_context:
            lines.append(group_context)
    else:
        lines.append("ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน:")
        for group_key in ("psu", "general_student", "adult"):
            price = PRICE_VALUES[key][group_key]
            total = price * sessions
            lines.append(f"- {GROUP_NAMES[group_key]}: {price} บาท/session x {sessions} = {total} บาท")

    if window_note:
        lines.append(f"หมายเหตุ: {window_note} ราคาด้านบนเป็นยอดเทียบตามแพ็กเกจเท่านั้น")
    return "\n".join(lines)


def _booking_session_limit_answer(q: str, start: float) -> FastAnswer | None:
    asks_limit = (
        _has(q, "สูงสุดกี่ session", "กี่ sessions", "จองได้กี่ session", "จองได้กี่รอบ")
        or (_has(q, "เล่นได้กี่ชั่วโมง", "กี่ชั่วโมงต่อวัน", "เล่นกี่ชั่วโมง") and _has(q, "คน", "คนนึง", "หนึ่งคน", "ต่อวัน", "ps5", "playstation", "เพลย์", "จอง"))
    )
    if not asks_limit:
        return None

    lines = ["การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions"]
    if _has(q, "ps5", "playstation", "เพลย์"):
        lines.append("- สำหรับ PlayStation 5: 1 session = 1 ชั่วโมง ดังนั้น 3 sessions = สูงสุด 3 ชั่วโมงต่อการจอง 1 ครั้ง")
    else:
        lines.append("- จำนวนชั่วโมงขึ้นกับบริการที่เลือก เช่น PlayStation 5/Nintendo Switch/Cockpit ใช้แพ็กเกจ 1 ชั่วโมงต่อ session")
        lines.append("- ถ้าหมายถึงบริการแบบ 1 ชั่วโมงต่อ session จะเท่ากับสูงสุด 3 ชั่วโมงต่อการจอง 1 ครั้ง")
    lines.extend([
        "- ข้อมูลที่มีระบุ limit เป็น “ต่อการจอง 1 ครั้ง” ยังไม่พบกฎแยกแบบฟันธงว่า 1 คนจำกัดกี่ชั่วโมงต่อวัน",
        f"แหล่งข้อมูล: {RESERVATION_URL}",
    ])
    return _answer("\n".join(lines), "reservation", "booking_session_limit_fast_path", start, 0.98)


def _direct_price_answer(q: str, group: str | None) -> str | None:
    if not group:
        return None
    keys = _service_keys_for_query(q)
    group_context = _group_context_line(q, group)
    if len(keys) > 1:
        if keys == ["vr_30", "vr_60"]:
            price_30 = PRICE_VALUES["vr_30"][group]
            price_60 = PRICE_VALUES["vr_60"][group]
            return (
                f"ราคา VR สำหรับกลุ่ม {GROUP_NAMES[group]}\n"
                f"•    VR 30 นาที: {price_30:,} บาท\n"
                f"•    VR 1 ชั่วโมง: {price_60:,} บาท\n"
                f"{group_context}\n"
                "หมายเหตุ: คำถามยังไม่ระบุระยะเวลา จึงแสดงทั้งราคา 30 นาทีและ 1 ชั่วโมง"
            )
        if keys == ["switch_1_2", "switch_3_4"]:
            price_1_2 = PRICE_VALUES["switch_1_2"][group]
            price_3_4 = PRICE_VALUES["switch_3_4"][group]
            return (
                f"ราคา Nintendo Switch สำหรับกลุ่ม {GROUP_NAMES[group]}\n"
                f"•    Nintendo Switch 1-2 คน: {price_1_2:,} บาท\n"
                f"•    Nintendo Switch 3-4 คน: {price_3_4:,} บาท\n"
                f"{group_context}\n"
                "หมายเหตุ: คำถามยังไม่ระบุจำนวนผู้เล่น จึงแสดงทั้งราคา 1-2 คนและ 3-4 คน"
            )
        lines = [f"ราคาสำหรับกลุ่ม {GROUP_NAMES[group]}:"]
        for key in keys:
            lines.append(f"•    {PRICE_LABELS[key]}: {PRICE_VALUES[key][group]:,} บาท")
        if group_context:
            lines.append(group_context)
        return "\n".join(lines)
    if len(keys) != 1:
        return None
    key = keys[0]
    price = PRICE_VALUES[key][group]
    answer = (
        f"ราคา {price} บาท สำหรับกลุ่ม {GROUP_NAMES[group]}\n"
        f"•    {PRICE_LABELS[key]}: {price:,} บาท"
    )
    if group_context:
        answer += f"\n{group_context}"
    return answer


def answer_price(query: str, start: float) -> FastAnswer | None:
    q = normalize_text(query)
    price_intent = _has(
        q, "ราคา", "ค่าบริการ", "กี่บาท", "เท่าไหร่", "เท่าไร", "เสียกี่บาท", "เสียเงิน",
        "เสียค่า", "ต้องจ่าย", "จ่ายไหม", "บาท", "ฟรี", "คิดเงิน", "คำนวณ", "ต่อชั่วโมง", "service fee", "price",
        "cost", "fee", "แพงกว่า", "ต่างกัน", "ค่าใช้จ่าย",
    )
    service_hint = _has(q, "ps5", "playstation", "เพลย์", "nintendo", "switch", "cockpit", "พวงมาลัย", "vr", "pc", "คอม")
    summary_intent = _has(q, "service fee", "service fee table", "ตารางราคา", "เรทราคา", "ค่าบริการทั้งหมด", "ค่าเล่นแต่ละเครื่อง")
    group = _detect_group(q)
    student_fee_answer = _student_fee_overview_answer(q, group)
    if not ((service_hint and price_intent) or summary_intent or student_fee_answer):
        return None

    rows = _service_rows_for_query(q)
    duration_price_answer = _duration_price_answer(q, group)
    focus_answer = _price_answer_focus(q, group)
    direct_price_answer = _direct_price_answer(q, group)
    if student_fee_answer and not rows:
        text = student_fee_answer
    elif not rows:
        text = SERVICE_FEE_SUMMARY
    elif duration_price_answer:
        text = duration_price_answer + "\n\nรายละเอียดจากตาราง:\n" + "\n\n".join(rows)
    elif rows == [PRICE_ROWS["pc"]]:
        text = _pc_price_text(q)
    elif focus_answer:
        text = focus_answer + "\n\nรายละเอียดจากตาราง:\n" + "\n\n".join(rows)
    elif direct_price_answer:
        text = direct_price_answer + "\n\nรายละเอียดจากตาราง:\n" + "\n\n".join(rows)
    else:
        prefix = ""
        if group == "psu":
            prefix = "กลุ่ม PSU Student and Staff ให้ดูราคา 0 บาทในแถวบริการที่เกี่ยวข้อง\n"
        elif group == "general_student":
            prefix = "กลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน ให้ดูราคา General Student ในแถวบริการที่เกี่ยวข้อง\n"
        elif group == "adult":
            prefix = "กลุ่ม General Adult / บุคคลทั่วไป ให้ดูราคา General Adult ในแถวบริการที่เกี่ยวข้อง\n"
        elif "นักเรียน" in q:
            prefix = "คำว่า “นักเรียน” ยังไม่ชัดว่าเป็น PSU หรือต่างสถาบัน จึงแสดงราคาที่เกี่ยวข้องให้เทียบก่อน\n"
        text = prefix + "\n\n".join(rows)
    text += f"\nแหล่งข้อมูล: {SERVICE_FEE_URL}"
    source_key = "service_fee_pc" if "local service fee update 2026-07-27" in text else "service_fee"
    return _answer(text, source_key, "deterministic_calculator_fast", start, 0.97 if service_hint else 0.88)


def _catalog_summary() -> str:
    return _format_game_zone_sections(
        intro=f"เกมที่มีข้อมูลยืนยันตอนนี้ทั้งหมด {len(_verified_game_catalog())} เกม:"
    )


CATALOG_ZONE_LABELS = ("PC Zone", "PlayStation 5 Zone", "Nintendo Switch Zone", "Cockpit Zone", "VR Zone")
CATALOG_ZONE_BY_KEY = {
    "pc": "PC Zone",
    "ps5": "PlayStation 5 Zone",
    "nintendo": "Nintendo Switch Zone",
    "cockpit": "Cockpit Zone",
    "vr": "VR Zone",
}


def _game_catalog_by_zone() -> dict[str, list[str]]:
    by_zone = {zone: [] for zone in CATALOG_ZONE_LABELS}
    for zone, entries in _catalog_entries_by_zone().items():
        by_zone[zone] = [str(entry["name"]) for entry in entries]
    return by_zone


def _join_game_names(names: list[str]) -> str:
    if len(names) <= 1:
        return "".join(names)
    return ", ".join(names[:-1]) + " และ " + names[-1]


def _format_game_zone_sections(keys: list[str] | None = None, intro: str = "") -> str:
    by_zone = _game_catalog_by_zone()
    if keys is None:
        zone_labels = list(CATALOG_ZONE_LABELS)
    else:
        zone_labels = [CATALOG_ZONE_BY_KEY[key] for key in keys if key in CATALOG_ZONE_BY_KEY]

    lines: list[str] = []
    if intro:
        lines.append(intro)

    for zone in zone_labels:
        names = by_zone.get(zone, [])
        if not names:
            continue
        if lines:
            lines.append("")
        lines.append(f"{zone} ({len(names)} เกม)")
        lines.extend(f"•    {name}" for name in names)
    return "\n".join(lines)


def _full_game_catalog_summary() -> str:
    unique_names = [str(entry["name"]) for entry in _verified_game_catalog()]
    lines = [_format_game_zone_sections(intro=f"ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด {len(unique_names)} เกมครับ")]
    lines.append("หมายเหตุ: จำนวนรวมด้านบนนับชื่อเกมไม่ซ้ำ แม้บางเกมจะอยู่ได้มากกว่า 1 โซน")
    return "\n".join(lines)


def _game_catalog_count_summary(q: str) -> str:
    by_zone = _game_catalog_by_zone()
    zone_keys = _zone_keys_for_query(q)
    zone_labels = [CATALOG_ZONE_BY_KEY[key] for key in zone_keys if key in CATALOG_ZONE_BY_KEY]
    if not zone_labels:
        return _full_game_catalog_summary()

    unique_names: list[str] = []
    for zone in zone_labels:
        for name in by_zone.get(zone, []):
            if name not in unique_names:
                unique_names.append(name)

    if len(zone_labels) == 1:
        zone = zone_labels[0]
        names = by_zone.get(zone, [])
        return _format_game_zone_sections(
            keys=zone_keys,
            intro=f"{zone} มีเกมที่ยืนยันได้ {len(names)} เกมครับ",
        )

    lines = [
        _format_game_zone_sections(
            keys=zone_keys,
            intro=f"โซนที่ถามมีเกมที่ยืนยันได้รวม {len(unique_names)} เกมครับ",
        )
    ]
    lines.append("หมายเหตุ: จำนวนรวมด้านบนนับชื่อเกมไม่ซ้ำ แม้บางเกมจะอยู่ได้มากกว่า 1 โซน")
    return "\n".join(lines)


def _looks_like_game_total_count(q: str) -> bool:
    if not _has(q, "เกม", "game", "games"):
        return False
    total_terms = (
        "ทั้งหมดกี่เกม", "มีทั้งหมดกี่เกม", "มีกี่เกม", "กี่เกม", "จำนวนเกม",
        "เกมทั้งหมด", "ทั้งหมดมีเกม", "total games", "how many games",
    )
    return _has(q, *total_terms)


def _match_game_detail(q: str) -> tuple[str, dict] | None:
    candidates = sorted(
        (
            (len(normalize_text(str(alias)).replace(" ", "")), key, meta, str(alias))
            for key, meta in GAME_DETAILS.items()
            for alias in _aliases_for_game(str(meta["name"]), meta["aliases"])
        ),
        reverse=True,
    )
    for _, key, meta, alias in candidates:
        if _game_alias_direct_match(q, alias):
            return key, meta
    grouped: dict[str, list[str]] = {}
    for length, key, _meta, alias in candidates:
        if length >= 4:
            grouped.setdefault(key, []).append(alias)
    for key, aliases in grouped.items():
        meta = GAME_DETAILS[key]
        if contains_alias(q, aliases, fuzzy=True, threshold=0.88)[0]:
            return key, meta
    return None


def _has_likely_named_game_detail(q: str) -> bool:
    if not _looks_like_game_detail(q):
        return False
    blocked = {
        "psu", "esports", "studio", "phuket", "pc", "vr", "ps5", "playstation",
        "nintendo", "switch", "game", "games", "zone",
    }
    for token in re.findall(r"\b[a-z][a-z0-9'’:-]{2,}\b", q):
        if token not in blocked:
            return True
    return False


def _match_supported_game(q: str) -> tuple[str, dict] | None:
    for entry in _verified_game_catalog():
        aliases = _aliases_for_game(str(entry["name"]), entry.get("aliases") or ())
        if any(_game_alias_direct_match(q, alias) for alias in aliases):
            return str(entry["name"]), {"zones": entry["zones"], "aliases": aliases}
    detail = _match_game_detail(q)
    if detail is not None:
        _, meta = detail
        aliases = _aliases_for_game(str(meta["name"]), meta["aliases"])
        current_by_name = {str(entry["name"]): entry for entry in _verified_game_catalog()}
        current = current_by_name.get(str(meta["name"]))
        zones = current["zones"] if current else meta["zones"]
        return str(meta["name"]), {"zones": zones, "aliases": aliases}
    for name, meta in SUPPORTED_GAME_CATALOG.items():
        aliases = _aliases_for_game(name, meta["aliases"])
        if any(_game_alias_direct_match(q, alias) for alias in aliases):
            return name, meta
    for entry in _verified_game_catalog():
        aliases = _aliases_for_game(str(entry["name"]), entry.get("aliases") or ())
        fuzzy_aliases = [alias for alias in aliases if len(normalize_text(str(alias)).replace(" ", "")) >= 4]
        if fuzzy_aliases and contains_alias(q, fuzzy_aliases, fuzzy=True, threshold=0.88)[0]:
            return str(entry["name"]), {"zones": entry["zones"], "aliases": aliases}
    for name, meta in SUPPORTED_GAME_CATALOG.items():
        aliases = _aliases_for_game(name, meta["aliases"])
        fuzzy_aliases = [alias for alias in aliases if len(normalize_text(str(alias)).replace(" ", "")) >= 4]
        if fuzzy_aliases and contains_alias(q, fuzzy_aliases, fuzzy=True, threshold=0.88)[0]:
            return name, meta
    return None


GAME_FAMILY_MATCHES = {
    "mario": {
        "label": "Mario",
        "aliases": ("mario", "มาริโอ", "มาริโอ้"),
        "game_keys": ("mario_kart_8", "mario_kart_live", "mario_party", "new_super_mario_bros", "super_mario_odyssey"),
    },
    "resident_evil": {
        "label": "Resident Evil",
        "aliases": (
            "resident evil", "resident", "เรสซิเดนต์อีวิล", "เรสซิเดนต์", "เรสซิเดนท์",
            "เรสิเด้นอีวิล", "เรสสิเด้นอีวิว", "เรสสิเด้นอีวิล", "เรสซิเดนอีวิว", "เรสซิเดนอีวิล",
            "เรสสิเด้น", "เรสสิเดน", "เลสซิเดน", "เลสซิเดนท์", "อีวิล", "อีวิว",
        ),
        "game_keys": ("resident_evil_4", "resident_evil_village"),
    },
    "call_of_duty": {
        "label": "Call of Duty",
        "aliases": ("call of duty", "call of dity", "cod", "คอลออฟดิวตี้", "คอลออฟ", "คอด"),
        "game_keys": ("warzone", "call_of_duty_mw3"),
    },
}


KNOWN_UNSUPPORTED_GAME_ALIASES = {
    "RoV / Arena of Valor": ("rov", "aov", "arena of valor", "อาโอวี", "เอโอวี", "อาร์โอวี", "เกมตีป้อม"),
    "PUBG Mobile": ("pubg mobile", "pubgโมบาย", "พับจีโมบาย", "พับจี mobile", "pubg m"),
    "Minecraft": ("minecraft", "มายคราฟ", "ไมน์คราฟต์", "ไมน์คราฟ"),
    "Roblox": ("roblox", "โรบล็อก", "โรบลอก"),
}


def _match_known_unsupported_game(q: str) -> str | None:
    for label, aliases in KNOWN_UNSUPPORTED_GAME_ALIASES.items():
        if _has(q, *aliases):
            return label
    return None


def _match_game_family(q: str) -> dict | None:
    for family in GAME_FAMILY_MATCHES.values():
        if _has(q, *family["aliases"]) or contains_alias(q, list(family["aliases"]), fuzzy=True, threshold=0.88)[0]:
            current_by_name = {str(entry["name"]): entry for entry in _verified_game_catalog()}
            games: list[dict] = []
            for key in family["game_keys"]:
                item = GAME_DETAILS.get(key)
                if item is None:
                    continue
                current_entry = current_by_name.get(str(item["name"]))
                if current_entry is None:
                    continue
                games.append({
                    "name": current_entry["name"],
                    "zones": current_entry["zones"],
                    "genre": item.get("genre") or current_entry.get("genre") or "",
                    "summary": item.get("summary") or current_entry.get("summary") or "",
                    "how": item.get("how") or current_entry.get("how") or "",
                    "source": item.get("source") or "our_games",
                })
            if games:
                return {"label": family["label"], "games": games}
    return None


def _has_specific_supported_game_alias(q: str, name: str, meta: dict) -> bool:
    q_key = _compact_key(q)
    name_key = _compact_key(name)
    if name_key and name_key in q_key:
        return True
    for alias in _aliases_for_game(name, meta.get("aliases") or ()):
        alias_key = _compact_key(str(alias))
        if len(alias_key) < 8:
            continue
        if alias_key and alias_key in q_key:
            return True
    return False


def _game_family_availability_answer(q: str, start: float) -> FastAnswer | None:
    family = _match_game_family(q)
    if family is None:
        return None
    supported = _match_supported_game(q)
    if supported is not None:
        supported_name, _supported_meta = supported
        if _has_specific_supported_game_alias(q, str(supported_name), _supported_meta):
            return None

    example_names = " หรือ ".join(item["name"] for item in family["games"][:2])
    broad_family_list = _has(q, "มีเกม", "เกมอะไรบ้าง", "เกมไรบ้าง", "อะไรบ้าง", "รายชื่อ", "รายการเกม")
    if _looks_like_game_detail(q) and not broad_family_list:
        lines = [f"พบเกมในกลุ่ม {family['label']} ในรายการที่ยืนยันได้ครับ"]
        for item in family["games"]:
            zones = " และ ".join(item["zones"])
            lines.append(
                f"- {item['name']}: {item['summary']} "
                f"แนวเกม: {item['genre']} "
                f"วิธีเล่นโดยสรุป: {item['how']} "
                f"เล่นได้ที่ {zones}"
            )
        if example_names:
            lines.append(f"ถ้าหมายถึงภาคใดภาคหนึ่งโดยเฉพาะ ให้ถามด้วยชื่อเกมนั้นได้เลย เช่น {example_names} ครับ")
    else:
        lines = [f"พบเกมที่เกี่ยวข้องกับ {family['label']} ในรายการที่ยืนยันได้ครับ"]
        for item in family["games"]:
            zones = " และ ".join(item["zones"])
            lines.append(f"- {item['name']}: เล่นได้ที่ {zones}")
        if example_names:
            lines.append(f"ถ้าหมายถึงเกมไหนเป็นพิเศษ ให้ถามด้วยชื่อเกมนั้นได้เลย เช่น {example_names} ครับ")
    lines.append(f"แหล่งข้อมูล: {OUR_GAMES_URL}")
    return _answer("\n".join(lines), "our_games", "games_family_availability_fast_path", start, 0.94)


GAME_GENRE_GROUPS = {
    "action": {
        "label": "Action / Action-Adventure",
        "aliases": ("action", "แอ็กชัน", "แอคชั่น", "บู๊", "ผจญภัย"),
        "keywords": ("action", "adventure", "แอ็กชัน", "ผจญภัย"),
    },
    "moba": {
        "label": "MOBA",
        "aliases": ("moba", "โมบา", "โมบ้า", "โมบะ", "ตีป้อม", "เกมตีป้อม", "multiplayer online battle arena"),
        "keywords": ("moba",),
    },
    "fps": {
        "label": "FPS / Tactical FPS",
        "aliases": ("fps", "เอฟพีเอส", "เอฟ พี เอส", "ยิง", "เกมยิง", "ปืน", "first-person shooter", "first person shooter"),
        "keywords": ("fps", "ยิง"),
    },
    "battle_royale": {
        "label": "Battle Royale / Survival",
        "aliases": ("battle royale", "แบทเทิลรอยัล", "แบทเทิล โรยัล", "แบตเทิลรอยัล", "survival", "เอาชีวิตรอด"),
        "keywords": ("battle royale", "survival", "เอาชีวิตรอด"),
    },
    "fighting": {
        "label": "Fighting",
        "aliases": ("fighting", "ไฟท์ติ้ง", "ไฟติ้ง", "ต่อสู้", "เกมต่อสู้"),
        "keywords": ("ต่อสู้ 1v1", "fighting"),
    },
    "racing": {
        "label": "Racing",
        "aliases": ("racing", "เรซซิ่ง", "เรซิ่ง", "แข่งรถ", "รถ"),
        "keywords": ("racing", "แข่งรถ"),
    },
    "sports": {
        "label": "Sports",
        "aliases": ("sports", "สปอร์ต", "กีฬา", "เกมกีฬา"),
        "keywords": ("sports", "กีฬา"),
    },
    "digital_card": {
        "label": "Digital Card",
        "aliases": ("digital card", "card game", "การ์ดเกม", "เกมการ์ด"),
        "keywords": ("digital card", "card"),
    },
    "rts": {
        "label": "Real-Time Strategy (RTS)",
        "aliases": ("rts", "real-time strategy", "real time strategy", "อาร์ทีเอส", "เรียลไทม์สตราทีจี"),
        "keywords": ("rts", "real-time strategy", "real time strategy"),
    },
    "rhythm": {
        "label": "Rhythm",
        "aliases": ("rhythm", "ริทึ่ม", "จังหวะ", "เพลง"),
        "keywords": ("rhythm", "จังหวะ"),
    },
    "party": {
        "label": "Party / Co-op",
        "aliases": ("party", "ปาร์ตี้", "co-op", "coop", "เล่นด้วยกัน", "หลายคน"),
        "keywords": ("party", "co-op", "coop"),
    },
    "rpg": {
        "label": "RPG / Action RPG",
        "aliases": ("rpg", "อาร์พีจี", "action rpg", "เกมบทบาทสมมติ", "ล่ามอนสเตอร์"),
        "keywords": ("rpg", "ล่ามอนสเตอร์"),
    },
    "horror": {
        "label": "Horror",
        "aliases": ("horror", "สยองขวัญ", "ผี"),
        "keywords": ("horror", "สยองขวัญ"),
    },
}


POPULAR_GAMES_BY_GENRE = {
    "moba": {
        "title": "MOBA",
        "items": ["League of Legends", "Dota 2", "Mobile Legends: Bang Bang", "Honor of Kings", "Wild Rift", "Arena of Valor"],
    },
    "fps": {
        "title": "FPS",
        "items": ["Call of Duty", "Battlefield", "Counter-Strike 2", "VALORANT", "Apex Legends"],
    },
    "battle_royale": {
        "title": "Battle Royale",
        "items": ["Fortnite", "PUBG", "Apex Legends", "Call of Duty: Warzone"],
    },
    "fighting": {
        "title": "Fighting",
        "items": ["Street Fighter", "Mortal Kombat", "TEKKEN", "Super Smash Bros."],
    },
    "sports": {
        "title": "Sports",
        "items": ["EA SPORTS FC", "NBA 2K", "eFootball", "Rocket League"],
    },
    "racing": {
        "title": "Racing",
        "items": ["Gran Turismo", "Forza Motorsport", "F1", "Mario Kart"],
    },
    "digital_card": {
        "title": "Digital Card",
        "items": ["Hearthstone", "Legends of Runeterra", "Marvel Snap", "Magic: The Gathering Arena"],
    },
    "rts": {
        "title": "Real-Time Strategy (RTS)",
        "items": ["StarCraft II", "Age of Empires", "Warcraft III"],
    },
}


ESPORTS_GAME_TYPE_SECTIONS = {
    "moba": {
        "title": "MOBA",
        "items": [
            "เป็นเกมกลยุทธ์แบบทีม เน้นยึดพื้นที่ ทำ objective และทำลายฐานฝ่ายตรงข้าม",
            "ตัวอย่าง: League of Legends, Dota 2, Arena of Valor",
        ],
    },
    "fps": {
        "title": "FPS",
        "items": [
            "เป็นเกมยิงมุมมองบุคคลที่ 1 เน้นการเล็ง การสื่อสาร และการคุมพื้นที่",
            "ตัวอย่าง: Counter-Strike 2, VALORANT, Call of Duty",
        ],
    },
    "battle_royale": {
        "title": "Battle Royale",
        "items": [
            "เป็นเกมเอาชีวิตรอด ผู้เล่น/ทีมต้องอยู่รอดเป็นคนสุดท้ายในพื้นที่ที่ค่อย ๆ แคบลง",
            "ตัวอย่าง: Fortnite, PUBG, Apex Legends, Call of Duty: Warzone",
        ],
    },
    "fighting": {
        "title": "Fighting",
        "items": [
            "เป็นเกมต่อสู้ที่วัดจังหวะ คอมโบ การป้องกัน และการอ่านคู่ต่อสู้",
            "ตัวอย่าง: TEKKEN, Street Fighter, Super Smash Bros.",
        ],
    },
    "sports": {
        "title": "Sports",
        "items": [
            "เป็นเกมกีฬาจำลอง ใช้ทักษะการวางแผนและการควบคุมตามชนิดกีฬา",
            "ตัวอย่าง: EA SPORTS FC, NBA 2K, eFootball",
        ],
    },
    "racing": {
        "title": "Racing",
        "items": [
            "เป็นเกมแข่งรถหรือจำลองการขับขี่ เน้นไลน์การขับ เบรก เข้าโค้ง และเวลา",
            "ตัวอย่าง: Gran Turismo, Forza Motorsport, F1, Mario Kart",
        ],
    },
    "digital_card": {
        "title": "Digital Card",
        "items": [
            "เป็นเกมการ์ดดิจิทัล เน้นการจัดเด็ค การอ่านเกม และการบริหารทรัพยากร",
            "ตัวอย่าง: Hearthstone, Legends of Runeterra, Magic: The Gathering Arena",
        ],
    },
    "rts": {
        "title": "Real-Time Strategy (RTS)",
        "items": [
            "เป็นเกมวางแผนแบบเวลาจริง เน้นสร้างฐาน เก็บทรัพยากร และควบคุมยูนิตพร้อมกัน",
            "ตัวอย่าง: StarCraft II, Age of Empires, Warcraft III",
        ],
    },
}


def _popular_games_by_genre_summary(keys: list[str] | None = None, intro: str = "เกมยอดนิยมตามหมวดที่หน้า Knowledge ระบุ:") -> str:
    selected_keys = keys or list(POPULAR_GAMES_BY_GENRE)
    sections = [
        (POPULAR_GAMES_BY_GENRE[key]["title"], POPULAR_GAMES_BY_GENRE[key]["items"])
        for key in selected_keys
        if key in POPULAR_GAMES_BY_GENRE
    ]
    return "\n\n".join([intro, _format_bulleted_sections(sections)])


def _esports_game_types_summary() -> str:
    sections = [
        (section["title"], section["items"])
        for section in ESPORTS_GAME_TYPE_SECTIONS.values()
    ]
    return "\n\n".join([
        "ประเภทเกมที่นิยมในการแข่งขันอีสปอร์ต:",
        _format_bulleted_sections(sections),
    ])


def _genre_group_for_query(q: str) -> dict | None:
    if not _has(q, "เกม", "game", "games", "แนว", "ประเภท"):
        return None
    for group in GAME_GENRE_GROUPS.values():
        if _has(q, *group["aliases"]):
            return group
    return None


def _game_genre_list_answer(q: str, start: float) -> FastAnswer | None:
    group = _genre_group_for_query(q)
    if group is None:
        return None
    if _has(q, "คือเกมอะไร", "เป็นเกมแนวไหน", "แนวไหน", "แนวอะไร") and _match_supported_game(q):
        return None
    rows: list[dict] = []
    keywords = tuple(str(item).lower() for item in group["keywords"])
    for meta in _verified_game_catalog():
        genre = normalize_text(str(meta.get("genre", "")))
        summary = normalize_text(str(meta.get("summary", "")))
        if any(keyword in genre for keyword in keywords) or (not genre and any(keyword in summary for keyword in keywords)):
            rows.append(meta)
    if not rows:
        return _answer(
            f"ยังไม่พบเกมแนว {group['label']} ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ\n"
            f"{_catalog_summary()}\n"
            f"แหล่งข้อมูล: {OUR_GAMES_URL}",
            "our_games",
            "games_genre_no_answer_fast_path",
            start,
            0.92,
        )
    lines = [f"เกมแนว {group['label']} ที่พบในรายการเกมที่ยืนยันได้:"]
    for meta in rows:
        zones = " และ ".join(meta["zones"])
        genre = str(meta.get("genre") or "ยังไม่ระบุแนวเกม")
        lines.append("")
        lines.append(str(meta["name"]))
        lines.append(f"•    แนวเกม: {genre}")
        lines.append(f"•    เล่นได้ที่: {zones}")
    lines.append(f"แหล่งข้อมูล: {OUR_GAMES_URL}")
    return _answer("\n".join(lines), "our_games", "games_genre_list_fast_path", start, 0.95)


def _looks_like_competition_game_list(q: str) -> bool:
    return _has(
        q,
        "เกมแข่งอะไรบ้าง", "เกมแข่งขันอะไรบ้าง", "เกมที่แข่ง", "มีเกมแข่ง", "มีเกมแข่งขัน",
        "รายการแข่งขันอะไรบ้าง", "รายการแข่งอะไรบ้าง", "รายการแข่งมีอะไรบ้าง", "รายการแข่งขันมีอะไรบ้าง", "แข่งเกมอะไร", "แข่งขันเกมอะไร",
        "ทัวร์นาเมนต์อะไรบ้าง", "tournament อะไรบ้าง",
    ) or (_has(q, "รายการแข่ง", "รายการแข่งขัน", "แข่ง", "แข่งขัน", "ทัวร์", "tournament") and _has(q, "เกมอะไร", "เกมไหน", "อะไรบ้าง"))


def _looks_like_game_detail(q: str) -> bool:
    return _has(
        q,
        "คืออะไร", "อะไรคือ", "เกมอะไร", "แนวอะไร", "เกี่ยวกับอะไร",
        "เล่นยังไง", "เล่นอย่างไร", "วิธีเล่น", "เล่นแบบไหน", "เล่นยังไงบ้าง",
        "สอนเล่น", "สอนเล่นเกม", "สอนหน่อย", "เล่นยังไงดี", "เล่นเกมยังไง",
    )


GAME_CATALOG_TERMS = (
    "มีเกมอะไร", "มีเกมไร", "เกมอะไรบ้าง", "เกมไรบ้าง", "เกมอะไรให้เล่น",
    "เกมทั้งหมด", "รายชื่อเกม", "รายการเกม", "list game", "games",
    "มีอะไรให้เล่น", "เล่นเกมอะไรได้บ้าง", "เล่นเกมไรได้บ้าง",
    "เล่นอะไรได้บ้าง", "เล่นไรได้บ้าง",
)


def _has_strong_game_catalog_terms(q: str) -> bool:
    return _has(q, *GAME_CATALOG_TERMS)


def _looks_like_game_catalog(q: str) -> bool:
    if _has(q, "ราคา", "ค่าบริการ", "กี่บาท", "เท่าไหร่", "เท่าไร", "เสียเงิน", "service fee"):
        return False
    if _has(
        q,
        "กติกา", "กฎ", "แข่ง", "แข่งขัน", "การแข่งขัน", "ลงแข่ง", "ทัวร์", "tournament",
        "ทีม", "สมาชิก", "ผู้เล่น", "ตัวจริง", "ตัวสำรอง", "ลงทะเบียน", "สมัคร",
    ):
        return False
    if _has_strong_game_catalog_terms(q):
        return True
    if _match_supported_game(q) or _match_game_family(q) or _match_known_unsupported_game(q):
        return False
    if _has_likely_named_game_detail(q):
        return False
    return False


def _looks_like_game_availability(q: str) -> bool:
    if _has(q, "ราคา", "ค่าบริการ", "กี่บาท", "เท่าไหร่", "เท่าไร", "เสียเงิน", "service fee"):
        return False
    if _has(q, "คือเกมอะไร", "เป็นเกมอะไร", "เกมแนวไหน", "เกมแนวอะไร", "แนวเกม", "เกี่ยวกับอะไร"):
        return False
    if _has(
        q,
        "กติกา", "กฎ", "แข่ง", "แข่งขัน", "การแข่งขัน", "ลงแข่ง", "ทัวร์", "tournament",
        "ทีม", "สมาชิก", "ผู้เล่น", "ตัวจริง", "ตัวสำรอง", "ลงทะเบียน", "สมัคร",
        "แผนที่", "map", "pause", "timeout", "technical", "บทลงโทษ", "ปรับแพ้",
        "ข้อห้าม", "อุปกรณ์", "โปรแกรม", "โปรแกรมช่วยเล่น", "บัญชี", "บัญชีส่วนตัว", "บัญชีที่จัดให้",
        "round", "rounds", "รอบ", "1 ต่อ 1", "1v1", "ft2", "r3", "decider", "เกมตัดสิน",
    ):
        return False
    if _has(
        q,
        "เล่นได้ไหม", "เล่นได้มั้ย", "เล่นได้รึเปล่า", "เล่นได้หรือเปล่า",
        "มีให้เล่นไหม", "มีให้เล่นมั้ย", "มีเกม", "เกมอะไร", "เกมทั้งหมด",
        "มีข้อมูลไหม", "มีข้อมูลมั้ย", "มีข้อมูลรึเปล่า", "มีข้อมูลหรือเปล่า",
        "ข้อมูลไหม", "ข้อมูลมั้ย", "อยู่ในฐานข้อมูลไหม", "อยู่ในฐานข้อมูลมั้ย",
        "list game", "อยากเล่น", "อยากลองเล่น", "จะเล่น", "ขอเล่น",
    ) or (_has(q, "เล่น") and _has(q, "ได้ไหม", "ได้มั้ย", "ได้รึเปล่า", "ได้หรือเปล่า", "มีไหม", "มีมั้ย")):
        return True
    if _match_supported_game(q) and (
        (_has(q, "มี", "อยู่", "อยู่ที่", "อยู่เครื่อง", "อยู่โซน") and _has(q, "ไหม", "มั้ย", "หรือเปล่า", "รึเปล่า", "ไหน", "บ้าง"))
        or _has(q, "เครื่องไหน", "โซนไหน", "zone ไหน", "เล่นที่ไหน", "เล่นได้ที่ไหน")
    ):
        return True
    return False


def _looks_like_equipment_game_catalog(q: str) -> bool:
    if _has(
        q,
        "\u0e23\u0e32\u0e04\u0e32", "\u0e04\u0e48\u0e32\u0e1a\u0e23\u0e34\u0e01\u0e32\u0e23", "\u0e01\u0e35\u0e48\u0e1a\u0e32\u0e17", "\u0e40\u0e17\u0e48\u0e32\u0e44\u0e2b\u0e23\u0e48", "\u0e40\u0e2a\u0e35\u0e22\u0e40\u0e07\u0e34\u0e19",
    ):
        return False
    if _has(q, "\u0e2d\u0e38\u0e1b\u0e01\u0e23\u0e13\u0e4c") and not _has(q, "\u0e40\u0e01\u0e21", "\u0e40\u0e25\u0e48\u0e19", "game", "games"):
        return False
    equipment_terms = (
        "\u0e2d\u0e38\u0e1b\u0e01\u0e23\u0e13\u0e4c", "\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07", "\u0e42\u0e0b\u0e19", "zone",
        "pc", "\u0e04\u0e2d\u0e21", "cockpit", "\u0e04\u0e47\u0e2d\u0e01\u0e1e\u0e34\u0e17", "\u0e04\u0e2d\u0e01\u0e1e\u0e34\u0e17", "\u0e1e\u0e27\u0e07\u0e21\u0e32\u0e25\u0e31\u0e22",
        "vr", "\u0e41\u0e27\u0e48\u0e19", "ps5", "playstation", "\u0e40\u0e1e\u0e25\u0e22\u0e4c", "nintendo", "switch", "\u0e19\u0e34\u0e19\u0e40\u0e17\u0e19\u0e42\u0e14", "\u0e2a\u0e27\u0e34\u0e15\u0e0a\u0e4c", "\u0e2a\u0e27\u0e34\u0e17\u0e0a\u0e4c",
    )
    game_list_terms = (
        "\u0e40\u0e25\u0e48\u0e19\u0e40\u0e01\u0e21\u0e2d\u0e30\u0e44\u0e23", "\u0e40\u0e25\u0e48\u0e19\u0e40\u0e01\u0e21\u0e44\u0e23", "\u0e21\u0e35\u0e40\u0e01\u0e21\u0e2d\u0e30\u0e44\u0e23", "\u0e21\u0e35\u0e40\u0e01\u0e21\u0e44\u0e23",
        "\u0e40\u0e01\u0e21\u0e2d\u0e30\u0e44\u0e23\u0e1a\u0e49\u0e32\u0e07", "\u0e40\u0e01\u0e21\u0e44\u0e23\u0e1a\u0e49\u0e32\u0e07", "\u0e40\u0e25\u0e48\u0e19\u0e2d\u0e30\u0e44\u0e23\u0e44\u0e14\u0e49\u0e1a\u0e49\u0e32\u0e07", "\u0e40\u0e25\u0e48\u0e19\u0e44\u0e23\u0e44\u0e14\u0e49\u0e1a\u0e49\u0e32\u0e07",
        "\u0e40\u0e25\u0e48\u0e19\u0e2d\u0e30\u0e44\u0e23", "\u0e40\u0e25\u0e48\u0e19\u0e44\u0e23", "\u0e21\u0e35\u0e2d\u0e30\u0e44\u0e23\u0e43\u0e2b\u0e49\u0e40\u0e25\u0e48\u0e19", "\u0e21\u0e35\u0e2d\u0e30\u0e44\u0e23\u0e1a\u0e49\u0e32\u0e07", "\u0e2d\u0e30\u0e44\u0e23\u0e1a\u0e49\u0e32\u0e07", "\u0e40\u0e01\u0e21\u0e1a\u0e19", "\u0e40\u0e01\u0e21\u0e17\u0e31\u0e49\u0e07\u0e2b\u0e21\u0e14", "list game", "games",
    )
    return _has(q, *equipment_terms) and _has(q, *game_list_terms)


def _requested_unknown_game_name(q: str) -> str:
    known_unsupported = _match_known_unsupported_game(q)
    if known_unsupported:
        return known_unsupported
    blocked = {
        "psu", "esports", "studio", "phuket", "pc", "vr", "ps5", "playstation", "nintendo", "switch",
        "zone", "local", "api", "today", "monday", "tuesday", "wednesday", "thursday", "friday",
        "game", "games",
    }
    for token in re.findall(r"\b[a-z][a-z0-9'’:-]{2,}\b", q):
        if token not in blocked and not _match_supported_game(token):
            return token.title()
    if "minecraft" in q:
        return "Minecraft"
    if "roblox" in q:
        return "Roblox"
    return "เกมนี้"


def _known_unsupported_game_answer(q: str, start: float) -> FastAnswer | None:
    requested = _match_known_unsupported_game(q)
    if not requested:
        return None
    if _looks_like_game_detail(q) and not _looks_like_game_availability(q):
        return None
    if not (_looks_like_game_detail(q) or _looks_like_game_availability(q) or _has(q, "เล่น", "อยาก", "มีไหม", "มีมั้ย")):
        return None
    note = ""
    if requested == "RoV / Arena of Valor":
        note = "ในฐานข้อมูลมีข้อมูลกติกาการแข่งขันของเกมนี้ แต่ยังไม่พบว่าอยู่ในรายการเกมให้เล่นของศูนย์\n"
    return _answer(
        f"ยังไม่พบ {requested} ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ\n"
        f"{note}"
        f"ถ้าต้องการเล่นเกมนี้ ควรสอบถามเจ้าหน้าที่ก่อนจองหรือก่อนเข้าใช้บริการ\n\n"
        f"{_catalog_summary()}\n"
        f"แหล่งข้อมูล: {OUR_GAMES_URL}",
        "our_games",
        "games_known_unsupported_fast_path",
        start,
        0.94,
    )


def _known_non_current_game_answer(q: str, start: float) -> FastAnswer | None:
    if not _has(q, "mario kart live", "home circuit", "mk live", "มาริโอคาร์ทไลฟ์", "มาริโอคาทไลฟ์"):
        return None
    current_names = {str(entry.get("name") or "") for entry in _verified_game_catalog()}
    if "Mario Kart Live: Home Circuit" in current_names:
        return None
    current_mario = [name for name in sorted(current_names) if "mario" in normalize_text(name)]
    suffix = ""
    if current_mario:
        suffix = "\nเกมตระกูล Mario ที่อยู่ในรายการปัจจุบันคือ: " + ", ".join(current_mario)
    return _answer(
        "ตอนนี้ยังไม่พบ Mario Kart Live: Home Circuit ในรายการเกมปัจจุบันของ PSU Esports Studio - Phuket ครับ\n"
        "จึงไม่ดึงปุ่มของเกมอื่น เช่น Mario Kart 8 Deluxe มาตอบแทน"
        f"{suffix}\n"
        f"แหล่งข้อมูล: {RESERVATION_URL}",
        "our_games",
        "games_non_current_availability_guard_fast_path",
        start,
        0.93,
    )


def _game_popularity_no_answer(q: str, start: float) -> FastAnswer | None:
    if _has(q, "ประเภทเกม", "แนวเกม", "อะไรบ้าง", "มีอะไรบ้าง") and not _has(q, "อันดับ", "ที่สุด", "คนเล่น", "most played", "ranking", "rank"):
        return None
    popularity_terms = (
        "คนเล่นมากที่สุด", "คนเล่นเยอะที่สุด", "คนเล่นเยอะ", "เล่นมากที่สุด",
        "ยอดนิยมที่สุด", "นิยมที่สุด", "ฮิตที่สุด", "เกมฮิต", "เกมยอดนิยม",
        "อันดับ", "rank", "ranking", "popular", "most played", "most popular",
    )
    game_terms = ("เกม", "game", "games", "เล่น")
    if not (_has(q, *game_terms) and _has(q, *popularity_terms)):
        return None
    return _answer(
        "ยังไม่มีข้อมูลสถิติยืนยันว่าเกมไหนมีคนเล่นมากที่สุดของ PSU Esports Studio - Phuket ครับ\n"
        "ข้อมูลที่มีตอนนี้ยืนยันได้เฉพาะรายชื่อเกมที่ให้บริการ/อยู่ในรายการเกม และข้อมูลกติกาการแข่งขันบางรายการ ไม่ใช่สถิติยอดผู้เล่นหรือความนิยม\n\n"
        f"{_catalog_summary()}\n"
        f"แหล่งข้อมูล: {OUR_GAMES_URL}",
        "our_games",
        "games_popularity_no_answer_fast_path",
        start,
        0.94,
    )


def _game_missing_data_answer(q: str, start: float) -> FastAnswer | None:
    if not _has(q, "เกม", "game", "games"):
        return None
    if not _has(
        q,
        "ยังไม่มีข้อมูล", "ไม่มีข้อมูล", "ไม่พบข้อมูล", "ข้อมูลไม่ครบ", "ขาดข้อมูล",
        "เกมไหนยังไม่มี", "เกมอะไรยังไม่มี", "เกมที่ยังไม่มี", "เกมที่ไม่มี",
    ):
        return None

    lines = [
        "ตอนนี้ระบบยังไม่สามารถสรุปรายชื่อเกมที่ไม่มีข้อมูลทั้งหมดได้แบบครบถ้วนครับ",
        "เพราะฐานข้อมูลยืนยันได้เฉพาะเกม/รายการที่มีข้อมูลอยู่แล้ว ไม่ได้มี master list ของทุกเกมที่ควรมีแต่ยังขาดข้อมูล",
        "",
        "สิ่งที่ยืนยันได้ตอนนี้คือรายการเกมที่มีข้อมูลแล้ว:",
        _format_game_zone_sections(),
        "",
        "ถ้าต้องการเช็กเกมที่สงสัย ให้ถามชื่อเกมนั้นตรง ๆ ได้ เช่น “Minecraft มีไหม” หรือ “RoV มีข้อมูลไหม” ระบบจะตอบว่าอยู่ในรายการยืนยันได้หรือยังไม่พบข้อมูล",
        f"แหล่งข้อมูล: {OUR_GAMES_URL}",
    ]
    return _answer("\n".join(lines), "our_games", "games_missing_data_fast_path", start, 0.96)


def _control_rows_for_game_name(game_name: str) -> list[dict]:
    game_key = _game_control_key(game_name)
    rows: list[dict] = []
    for row in _read_jsonl(GAME_CONTROL_FACTS_PATH):
        if row.get("category") != "game_controls" or not row.get("button"):
            continue
        row_game = str(row.get("game") or "").strip()
        if _game_control_key(row_game) == game_key:
            rows.append(row)
    return rows


def _game_control_section_lines(game_name: str) -> list[str]:
    rows = _control_rows_for_game_name(game_name)
    if not rows:
        return []

    grouped: dict[str, list[dict]] = {}
    for row in rows:
        platform = str(row.get("platform") or "ไม่ระบุแพลตฟอร์ม").strip()
        grouped.setdefault(platform, []).append(row)

    lines = ["ปุ่มการเล่น:"]
    for platform, platform_rows in grouped.items():
        lines.append(f"{platform}")
        for row in platform_rows:
            button = str(row.get("button") or "").strip()
            action = str(row.get("action_th") or row.get("action_en") or "").strip()
            description = str(row.get("description_th") or "").strip()
            text = f"{button}: {action}" if action else button
            if description:
                text += f" - {description}"
            lines.append(f"  - {text}")
    return lines


def _looks_like_play_method_query(q: str) -> bool:
    return _has(
        q,
        "วิธีเล่น", "เล่นยังไง", "เล่นอย่างไร", "เล่นแบบไหน", "สอนเล่น",
        "สอนเล่นเกม", "เล่นยังไงดี", "เล่นเกมยังไง",
    )


def _game_detail_lines(meta: dict, *, include_controls: bool = False) -> list[str]:
    zones = " และ ".join(meta["zones"])
    lines = [
        f"{meta['name']}: {meta['summary']}",
        f"แนวเกม: {meta['genre']}",
        f"วิธีเล่นโดยสรุป: {meta['how']}",
        f"เล่นได้ที่: {zones}",
    ]
    if include_controls:
        control_lines = _game_control_section_lines(str(meta["name"]))
        if control_lines:
            lines.append("")
            lines.extend(control_lines)
    return lines


def _source_url_for_game(meta: dict) -> str:
    source_key = str(meta.get("source") or "our_games")
    if source_key == "our_games":
        return OUR_GAMES_URL
    if source_key == "competition_rules":
        return "data/competition_rules"
    return RESERVATION_URL


MEMBER_GROUP_ORDER = (
    "Members",
    "cooperative education and Internship student",
    "PSU Phuket Esports Club - PSU Phuket",
)


COMPETITION_RULE_GAME_ALIASES = {
    "rov": ("rov", "aov", "arena of valor", "อาโอวี", "เอโอวี", "อาร์โอวี"),
    "valorant": ("valorant", "valo", "วาโล", "วาโลแรนท์", "วาโลแรน"),
    "cs2": ("cs2", "counter-strike", "counter strike", "counter-strike 2", "counter strike 2", "เคาเตอร์"),
    "tekken8": ("tekken 8", "tekken", "เทคเคน", "เทคเคน 8", "เทคเคน8", "เทกเคน"),
}

COMPETITION_RULE_GAME_LABELS = {
    "rov": "RoV / Arena of Valor",
    "valorant": "VALORANT",
    "cs2": "Counter-Strike 2",
    "tekken8": "TEKKEN 8",
}

COMPETITION_RULE_SOURCES = {
    "rov": "local://competition_rules/competition_rules_rov_blueket_2025_men",
    "valorant": "local://competition_rules/competition_rules_valorant_psu_phuket_2026",
    "cs2": "local://competition_rules/competition_rules_cs2_psu_phuket_2026",
    "tekken8": "local://competition_rules/competition_rules_tekken8_psu_esports",
}

COMPETITION_RULE_GENERIC_ANSWERS = {
    "rov": {
        "data_exists": "มีข้อมูลกติกาการแข่งขัน RoV ครับ\n- ข้อมูลที่ยืนยันได้: แข่งขันแบบ 5v5 และมีรายละเอียดเรื่องการมาสาย การหยุดเกม อุปกรณ์มือถือ และการเริ่มเกมใหม่\n- หมายเหตุ: เป็นข้อมูลกติกาการแข่งขัน ไม่ใช่รายการเกมให้เล่นในโซนของศูนย์",
        "team_size": "RoV ลงแข่งพร้อมกันฝ่ายละ 5 คนครับ\n- หลักฐานที่พบระบุโหมดการแข่งขัน 5v5\n- ยังไม่พบจำนวน roster รวม/ตัวสำรองที่ระบุเป็นตัวเลขแยกชัดเจน",
        "substitute": "RoV ยังไม่พบข้อมูลตัวสำรองที่ระบุชัดเจนครับ\n- ข้อมูลที่ยืนยันได้คือแข่งแบบ 5v5\n- ถ้าจะใช้ตัวสำรองควรยึดประกาศผู้จัดหรือสอบถามกรรมการก่อนแข่ง",
        "late": "RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที ทีมที่ทำให้ล่าช้าเสี่ยงถูกปรับแพ้ครับ",
        "disconnect": "RoV ถ้าเกิดปัญหาหลุดเกมให้หยุดเกมตามสิทธิ์ pause และแจ้งผู้ตัดสิน/ทีมงานครับ\n- ข้อมูลที่พบ: แต่ละทีมขอหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที",
        "pause": "RoV ขอ pause ได้ครับ\n- แต่ละทีมขอหยุดเกมได้สูงสุด 5 ครั้ง\n- ครั้งละไม่เกิน 1 นาที\n- ใช้กรณีปัญหา เช่น หลุดเกมหรือขัดข้อง",
        "penalty": "RoV มีบทลงโทษตามกติกาครับ\n- ตัวอย่างที่พบ: กรณีใช้ pause ผิดเจตนาอาจถูกตักเตือน แบนฮีโร่ หรือปรับแพ้ตามดุลยพินิจกรรมการ",
        "program": "RoV ยังไม่พบข้อมูลชัดเจนเรื่องโปรแกรมช่วยเล่นในไฟล์กติกาที่มีครับ\n- ข้อมูลอุปกรณ์ที่ยืนยันได้: ใช้โทรศัพท์มือถือในการแข่งขัน และไม่อนุญาต Tablet/iPad\n- ถ้าเป็นโปรแกรมช่วยเล่นควรถือว่าเสี่ยงผิดกติกาและถามกรรมการก่อนแข่ง",
        "team_incomplete": "RoV ควรมีผู้เล่นครบ 5 คนก่อนลงแข่งครับ\n- ข้อมูลที่ยืนยันได้คือโหมด 5v5\n- ยังไม่พบข้อยกเว้นสำหรับทีมที่คนไม่ครบ",
        "format": "RoV มีข้อมูลรูปแบบการแข่งขันในกติกาครับ\n- ข้อมูลที่พบในชุดกติกา: แข่งแบบ BO3 ในรอบที่ระบุของรายการ\n- ถ้าถามรอบเฉพาะ ควรระบุรอบการแข่งขันเพิ่ม",
        "final_round": "RoV ยังไม่พบข้อมูลรอบชิงแบบครบถ้วนจากคำถามนี้ครับ\n- ข้อมูลที่พบเด่นคือรูปแบบ BO3 ในกติกาที่มี",
        "ban": "RoV มีข้อมูลเรื่อง Global Ban/Pick ในกติกาครับ\n- ฮีโร่ที่เกี่ยวข้องกับการเลือก/แบนควรยึดตามกติกา Global Ban/Pick ของรายการ",
        "account": "RoV ยังไม่พบข้อมูลชัดเจนว่าใช้บัญชีส่วนตัวหรือบัญชีที่ผู้จัดเตรียมให้ครับ",
        "roster_change": "RoV ยังไม่พบข้อมูลชัดเจนเรื่องเปลี่ยนสมาชิกทีมจากคำถามนี้ครับ\n- ควรยืนยันกับผู้จัดก่อนแข่ง",
        "bug": "RoV ถ้าพบ bug หรือปัญหาระหว่างแข่งให้แจ้งผู้ตัดสิน/ทีมงานครับ\n- ไม่ควรเล่นต่อโดยใช้ข้อผิดพลาดให้ได้เปรียบ",
        "voice": "RoV ยังไม่พบข้อมูลชัดเจนเรื่อง voice chat ในไฟล์กติกาที่มีครับ",
        "opponent_missing": "RoV ยังไม่พบข้อมูลชัดเจนว่าถ้าคู่แข่งไม่มาต้องดำเนินการอย่างไรครับ\n- ควรแจ้งกรรมการหรือผู้จัดการแข่งขัน",
        "checkin": "RoV มีข้อมูลการลงทะเบียน/รายงานตัวครับ\n- ข้อมูลที่พบ: ช่วงลงทะเบียนระบุเวลา 8.00-8.30 น. ในกติกาที่มี",
        "equipment": "RoV มีข้อกำหนดอุปกรณ์ครับ\n- ใช้โทรศัพท์มือถือในการแข่งขัน\n- ไม่อนุญาตให้ใช้ Tablet หรือ iPad",
        "remake": "RoV มีเงื่อนไขเริ่มเกมใหม่ครับ\n- โดยสรุป ขอแข่งใหม่ได้เฉพาะช่วงต้นเกมตามเงื่อนไข First Blood/เวลาเกมที่กติกากำหนด",
        "network": "RoV ถ้าเน็ตหรือเซิร์ฟเวอร์มีปัญหาให้แจ้งทีมงาน/ผู้ตัดสินครับ\n- ไม่ควรตัดสินเองโดยไม่มีการยืนยันจากกรรมการ",
    },
    "valorant": {
        "data_exists": "มีข้อมูลกติกาการแข่งขัน VALORANT ครับ\n- ข้อมูลครอบคลุมผู้เล่น อุปกรณ์ การตั้งค่าเกม pause แผนที่ และบทลงโทษ",
        "team_size": "VALORANT ใช้ผู้เล่นตัวจริงทีมละ 5 คนครับ",
        "substitute": "VALORANT มีข้อมูลช่วงเตรียมตัวว่าในพื้นที่ Match Prep มีผู้เล่นได้ไม่เกิน 6 คนครับ\n- ตีความได้ว่ามีพื้นที่สำหรับตัวสำรอง/บุคลากรจำกัด แต่การเปลี่ยนตัวต้องยึดกติกาผู้จัด",
        "late": "VALORANT ต้องรายงานตัวก่อนแข่งครับ\n- ข้อมูลที่พบ: ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาทีก่อนเวลาแข่ง",
        "disconnect": "VALORANT หากเกิดปัญหาหลุดหรืออุปกรณ์ขัดข้องให้ใช้ Technical/Emergency Pause ตามกติกาและแจ้งเจ้าหน้าที่ครับ",
        "pause": "VALORANT มี Pause หลัก 3 ประเภทครับ\n- Tactical Timeout\n- Technical Pause\n- Emergency Pause",
        "penalty": "VALORANT มีบทลงโทษหลายระดับครับ\n- ตัวอย่าง: Round Loss, Map Forfeit, Match Forfeit และโทษกรณี Cheating/Match fixing",
        "program": "VALORANT ห้ามใช้โปรแกรมช่วยเล่นหรือดัดแปลงเพื่อสร้างความได้เปรียบครับ\n- ห้ามติดตั้งโปรแกรมเองบนเครื่องแข่งขัน\n- ห้ามใช้ cheat/macro/script ที่ผิดกติกา",
        "team_incomplete": "VALORANT ควรมีผู้เล่นครบทีมละ 5 คนครับ\n- ข้อมูลที่ยืนยันได้คือทีมละ 5 คน",
        "format": "VALORANT มีรูปแบบการแข่งขันตามเอกสารกติกาครับ\n- ถ้าต้องการรูปแบบรอบใดรอบหนึ่ง ควรถามระบุรอบเพิ่มเติม",
        "final_round": "VALORANT ยังไม่พบข้อมูลรอบชิงแบบฟันธงจากคำถามนี้ครับ\n- ควรดูประกาศ bracket/format ของรายการประกอบ",
        "ban": "VALORANT มีข้อมูลเรื่อง map pool และการแบนแผนที่ครับ\n- map pool ที่พบ: Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset",
        "account": "VALORANT ยังไม่พบข้อมูลชัดเจนว่าใช้บัญชีส่วนตัวหรือบัญชีที่ผู้จัดเตรียมให้ครับ",
        "roster_change": "VALORANT ยังไม่พบข้อมูลชัดเจนเรื่องเปลี่ยนสมาชิกทีมจากคำถามนี้ครับ\n- ควรยืนยันกับผู้จัดก่อนแข่ง",
        "bug": "VALORANT มีข้อมูลเรื่อง bug/challenge/rollback ครับ\n- โดยสรุป หากเกิดบัคต้องแจ้งเจ้าหน้าที่ และการ rollback ขึ้นกับเงื่อนไขกติกา",
        "voice": "VALORANT ระหว่าง Technical Pause ห้ามสื่อสารกัน เว้นแต่ได้รับอนุญาตจากเจ้าหน้าที่ครับ",
        "opponent_missing": "VALORANT ยังไม่พบข้อมูลชัดเจนว่าถ้าคู่แข่งไม่มาต้องดำเนินการอย่างไรครับ\n- ควรแจ้งกรรมการหรือผู้จัดการแข่งขัน",
        "checkin": "VALORANT ต้องรายงานตัวก่อนแข่งครับ\n- ข้อมูลที่พบ: ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาทีก่อนเวลาแข่ง",
        "equipment": "VALORANT มีข้อกำหนดอุปกรณ์ครับ\n- ห้ามนำโทรศัพท์มือถือ/แท็บเล็ตหรืออุปกรณ์สื่อสารเข้าพื้นที่ที่กติกาห้าม\n- การใช้อุปกรณ์ควรยึดรายการที่กติกาอนุญาต",
        "remake": "VALORANT มีข้อมูลเรื่อง bug/challenge/rollback ครับ\n- ถ้าเกิดปัญหาต้องแจ้งเจ้าหน้าที่ และการย้อนรอบขึ้นกับเงื่อนไขในกติกา",
        "network": "VALORANT ถ้าเน็ต/อุปกรณ์ขัดข้องให้แจ้งเจ้าหน้าที่และใช้ Technical/Emergency Pause ตามกติกาครับ",
    },
    "cs2": {
        "data_exists": "มีข้อมูลกติกาการแข่งขัน Counter-Strike 2 ครับ\n- ข้อมูลครอบคลุมทีม แผนที่ pause อุปกรณ์ และบทลงโทษ",
        "team_size": "CS2 ใช้ผู้เล่นทีมละ 5 คนครับ",
        "substitute": "CS2 ยังไม่พบข้อมูลตัวสำรองแบบแยกชัดเจนจากคำถามนี้ครับ\n- ข้อมูลที่ยืนยันได้คือทีมละ 5 คน",
        "late": "CS2 ถ้ามาสายหรือไม่ยืนยันเข้าแข่งขันก่อนแมตช์ ทีมเสี่ยงถูกตัดสิทธิ์ครับ",
        "disconnect": "CS2 ถ้าเกิดปัญหาเครื่อง/การเชื่อมต่อ ให้ใช้ Technical Pause ตามกติกาและแจ้งเจ้าหน้าที่ครับ",
        "pause": "CS2 มีทั้ง Technical Pause และ Tactical Timeout ครับ\n- Technical Pause ใช้กรณีปัญหาขัดข้อง\n- Tactical Timeout ใช้ตามเงื่อนไขช่วง Freeze time",
        "penalty": "CS2 มีบทลงโทษครับ\n- ตัวอย่าง: ใช้บัค/โกง/พฤติกรรมไม่เหมาะสม อาจถูกปรับแพ้เป็นรอบ แมตช์ หรือตัดสิทธิ์ตามความรุนแรง",
        "program": "CS2 ห้ามใช้โปรแกรมช่วยเล่นหรือการดัดแปลงที่ผิดกติกาครับ\n- รวมถึง cheat, macro/script หรือ config ที่ทำให้ได้เปรียบโดยไม่ชอบ",
        "team_incomplete": "CS2 ควรมีผู้เล่นครบ 5 คนครับ\n- ข้อมูลที่ยืนยันได้คือทีมละ 5 คน",
        "format": "CS2 มีรูปแบบการแข่งขันตามเอกสารกติกาครับ\n- ถ้าต้องการรอบเฉพาะ ให้ถามระบุรอบหรือ bracket เพิ่ม",
        "final_round": "CS2 ยังไม่พบข้อมูลรอบชิงแบบฟันธงจากคำถามนี้ครับ\n- ควรดูประกาศ bracket/format ของรายการประกอบ",
        "ban": "CS2 มีข้อมูล map pool ครับ\n- แผนที่ที่พบ: Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train",
        "account": "CS2 ยังไม่พบข้อมูลชัดเจนว่าใช้บัญชีส่วนตัวหรือบัญชีที่ผู้จัดเตรียมให้ครับ",
        "roster_change": "CS2 หลังยืนยันรายชื่อไม่ควรเปลี่ยนสมาชิกนอกกติกาครับ\n- ข้อมูล audit เดิมระบุว่าไม่มีการเปลี่ยนแปลงสมาชิกหลังยืนยันรายชื่อ",
        "bug": "CS2 ห้ามใช้บัคครับ\n- หากใช้บัคอาจถูกปรับแพ้เป็นรอบหรือแมตช์ และกรณีร้ายแรงอาจถูกตัดสิทธิ์",
        "voice": "CS2 ยังไม่พบข้อมูลชัดเจนเรื่อง voice chat จากคำถามนี้ครับ",
        "opponent_missing": "CS2 ยังไม่พบข้อมูลชัดเจนว่าถ้าคู่แข่งไม่มาต้องดำเนินการอย่างไรครับ\n- ควรแจ้งกรรมการหรือผู้จัดการแข่งขัน",
        "checkin": "CS2 ต้องยืนยัน/รายงานตัวตามเวลาที่ผู้จัดกำหนดครับ\n- หากไม่ยืนยันก่อนแมตช์มีความเสี่ยงถูกตัดสิทธิ์",
        "equipment": "CS2 มีข้อกำหนดอุปกรณ์ครับ\n- ผู้เล่นต้องรับผิดชอบความพร้อมของอุปกรณ์ตนเอง\n- ห้ามใช้อุปกรณ์/โปรแกรมที่ทำให้ได้เปรียบผิดกติกา",
        "remake": "CS2 ยังไม่พบข้อมูล remake/restart แบบฟันธงจากคำถามนี้ครับ\n- หากเกิดปัญหาให้แจ้งผู้ตัดสินและยึด Technical Pause/คำตัดสินกรรมการ",
        "network": "CS2 ถ้าเน็ตหรือเครื่องมีปัญหาให้แจ้งเจ้าหน้าที่และใช้ Technical Pause ตามกติกาครับ",
    },
    "tekken8": {
        "data_exists": "มีข้อมูลกติกาการแข่งขัน TEKKEN 8 ครับ\n- ข้อมูลครอบคลุมรูปแบบ 1v1, FT2, Round 3, เวลา 60 วินาที, Stage Random และอุปกรณ์ PlayStation 5",
        "team_size": "TEKKEN 8 แข่งขันแบบ 1v1 ครับ",
        "substitute": "TEKKEN 8 ยังไม่พบข้อมูลตัวสำรองจากคำถามนี้ครับ\n- ข้อมูลที่ยืนยันได้คือแข่งแบบ 1v1",
        "late": "TEKKEN 8 ยังไม่พบข้อมูลมาสายแบบฟันธงจากคำถามนี้ครับ\n- ควรยึดกำหนดการและคำตัดสินผู้จัด",
        "disconnect": "TEKKEN 8 ถ้าเกิดเหตุขัดข้องหรือฉุกเฉินให้แจ้งผู้จัด/กรรมการครับ\n- การหยุดเกมต้องอยู่ภายใต้เงื่อนไขที่กติกาอนุญาต",
        "pause": "TEKKEN 8 ห้าม pause เองหลังเริ่มเกมโดยไม่มีเหตุอันควรครับ\n- อาจถูกปรับแพ้ 1 รอบตามกติกา",
        "penalty": "TEKKEN 8 มีบทลงโทษเรื่อง pause/ข้อโต้แย้งครับ\n- ตัวอย่าง: pause เองหลังเริ่มเกมอาจถูกปรับแพ้ 1 รอบ",
        "program": "TEKKEN 8 ยังไม่พบข้อมูลชัดเจนเรื่องโปรแกรมช่วยเล่นในไฟล์กติกาที่มีครับ\n- ข้อมูลที่ยืนยันได้คือแข่งขันบน PlayStation 5 และห้าม customization บางประเภท",
        "team_incomplete": "TEKKEN 8 เป็นการแข่งขัน 1v1 จึงต้องมีผู้เล่นของคู่แข่งขันครบตามแมตช์ครับ",
        "format": "TEKKEN 8 แข่งขันแบบ 1v1 และใช้รูปแบบ First to 2 (FT2) ครับ\n- ตั้งค่า Round 3\n- เวลา 60 วินาที",
        "final_round": "TEKKEN 8 ใช้รูปแบบ FT2 โดยผู้ชนะต้องชนะครบ 2 เกมครับ",
        "ban": "TEKKEN 8 มีข้อมูลเรื่อง Stage Random และข้อจำกัด customization ครับ\n- ยังไม่ใช่ระบบแบนตัวละครแบบเกมทีม",
        "account": "TEKKEN 8 ยังไม่พบข้อมูลชัดเจนว่าใช้บัญชีส่วนตัวหรือบัญชีที่ผู้จัดเตรียมให้ครับ",
        "roster_change": "TEKKEN 8 ยังไม่พบข้อมูลเปลี่ยนสมาชิกทีมจากคำถามนี้ครับ\n- เพราะข้อมูลหลักเป็นการแข่งขัน 1v1",
        "bug": "TEKKEN 8 หากพบปัญหาควรแจ้งผู้จัด/กรรมการครับ\n- คำตัดสินของผู้จัดถือเป็นที่สุดตามกติกา",
        "voice": "TEKKEN 8 ยังไม่พบข้อมูลชัดเจนเรื่อง voice chat จากคำถามนี้ครับ",
        "opponent_missing": "TEKKEN 8 ยังไม่พบข้อมูลชัดเจนว่าถ้าคู่แข่งไม่มาต้องดำเนินการอย่างไรครับ\n- ควรแจ้งกรรมการหรือผู้จัดการแข่งขัน",
        "checkin": "TEKKEN 8 ยังไม่พบข้อมูลเช็คอินแบบฟันธงจากคำถามนี้ครับ\n- ควรยึดกำหนดการและคำสั่งผู้จัด",
        "equipment": "TEKKEN 8 แข่งขันบน PlayStation 5 ครับ\n- ข้อมูลที่พบ: Platform คือ PlayStation 5\n- มีข้อจำกัดเรื่อง customization และการ pause เองหลังเริ่มเกม",
        "remake": "TEKKEN 8 ยังไม่พบข้อมูล remake/restart แบบฟันธงจากคำถามนี้ครับ\n- ถ้าเกิดเหตุฉุกเฉินหรืออุปกรณ์ขัดข้องต้องให้ผู้จัด/กรรมการตัดสิน",
        "network": "TEKKEN 8 ยังไม่พบข้อมูลเน็ตล่มแบบฟันธงจากคำถามนี้ครับ\n- หากเกิดปัญหาระหว่างแข่งให้แจ้งผู้จัด/กรรมการ",
    },
}


def _competition_rule_game_key(q: str) -> str | None:
    for key, aliases in COMPETITION_RULE_GAME_ALIASES.items():
        if _has(q, *aliases):
            return key
    return None


def _competition_rule_generic_intent(q: str) -> str | None:
    if _has(q, "แหล่งข้อมูล", "อ้างอิง", "มาจากไหน", "source"):
        return "source"
    if _has(q, "มีข้อมูลกติกา", "มีกติกา", "ข้อมูลกติกา"):
        return "data_exists"
    if _has(q, "ผู้เล่นกี่คน", "ใช้ผู้เล่นกี่คน", "แข่งใช้ผู้เล่นกี่คน", "ทีมละกี่คน", "กี่คน"):
        return "team_size"
    if _has(q, "ตัวสำรอง", "สำรอง"):
        return "substitute"
    if _has(q, "มาสาย", "ล่าช้า", "late"):
        return "late"
    if _has(q, "เกมหลุด", "หลุด", "disconnect"):
        return "disconnect"
    if _has(q, "pause", "หยุดเกม", "เวลานอก"):
        return "pause"
    if _has(q, "บทลงโทษ", "ลงโทษ", "โดนอะไร"):
        return "penalty"
    if _has(q, "โปรแกรมช่วยเล่น", "ช่วยเล่น", "macro", "script", "cheat"):
        return "program"
    if _has(q, "ทีมไม่ครบ", "คนไม่ครบ", "ไม่ครบ"):
        return "team_incomplete"
    if _has(q, "รูปแบบการแข่งขัน", "รูปแบบ", "เล่นแบบไหน"):
        return "format"
    if _has(q, "รอบชิง", "ชิง", "กี่เกม"):
        return "final_round"
    if _has(q, "แบน", "ตัวละคร", "แผนที่", "map"):
        return "ban"
    if _has(q, "บัญชีส่วนตัว", "บัญชีที่จัดให้", "บัญชี"):
        return "account"
    if _has(q, "เปลี่ยนสมาชิก", "เปลี่ยนตัว", "roster"):
        return "roster_change"
    if _has(q, "bug", "บัค", "บั๊ก", "แจ้งใคร"):
        return "bug"
    if _has(q, "voice chat", "discord", "สื่อสาร"):
        return "voice"
    if _has(q, "คู่แข่งไม่มา", "ไม่มา"):
        return "opponent_missing"
    if _has(q, "เช็คอิน", "เชคอิน", "checkin", "check in", "รายงานตัว"):
        return "checkin"
    if _has(q, "ข้อห้ามเรื่องอุปกรณ์", "อุปกรณ์"):
        return "equipment"
    if _has(q, "remake", "restart", "เริ่มใหม่", "แข่งใหม่"):
        return "remake"
    if _has(q, "เน็ตล่ม", "อินเทอร์เน็ต", "server", "เซิร์ฟเวอร์"):
        return "network"
    return None


def answer_competition_rules(query: str, start: float) -> FastAnswer | None:
    q = normalize_text(query)
    game_key = _competition_rule_game_key(q)
    intent = _competition_rule_generic_intent(q)
    if game_key is None or intent is None:
        return None
    if intent not in {"data_exists", "source"}:
        return None

    label = COMPETITION_RULE_GAME_LABELS[game_key]
    source = COMPETITION_RULE_SOURCES[game_key]
    if intent == "source":
        answer = f"แหล่งข้อมูลกติกาของ {label}: {source}"
    else:
        answer = COMPETITION_RULE_GENERIC_ANSWERS.get(game_key, {}).get(intent)
        if not answer:
            return None
        if label not in answer:
            answer = f"{label}: {answer}"
    answer = f"{answer}\nแหล่งข้อมูล: {source}"
    return _answer(answer, "competition_rules", "competition_generic_fast_path", start, 0.94)


@lru_cache(maxsize=1)
def _member_profiles() -> tuple[dict, ...]:
    return tuple(_read_jsonl(MEMBER_PROFILES_PATH))


def _looks_like_member_query(q: str) -> bool:
    if _looks_like_text_generation_request(q):
        return False
    return _has(
        q,
        "member", "members", "staff", "สตาฟ", "เจ้าหน้าที่", "คนดูแล", "สมาชิก", "สมาชิกทีม", "ทีมงาน", "บุคลากร", "ตำแหน่ง",
        "ผู้จัดการ", "อธิการบดี", "รองอธิการบดี", "คณบดี", "ผู้ช่วยอธิการบดี",
        "นักวิชาการคอมพิวเตอร์", "สหกิจ", "ฝึกงาน", "internship", "intern", "cooperative",
        "psu phuket esports club", "esports club", "ชมรม", "ประธาน", "รองประธาน",
        "เลขานุการ", "เหรัญญิก", "ประชาสัมพันธ์", "กรรมการ",
    )


def _looks_like_text_generation_request(q: str) -> bool:
    if not _has(
        q,
        "เขียน", "ช่วยเขียน", "แต่ง", "ช่วยแต่ง", "ร่าง", "ช่วยร่าง",
        "ประโยค", "แคปชั่น", "caption", "ข้อความ", "คำโปรย",
        "ประชาสัมพันธ์กิจกรรม", "โปรโมต", "โปรโมท", "ประกาศ", "โพสต์",
    ):
        return False
    return not _has(
        q,
        "ใคร", "ใครบ้าง", "ใครเป็น", "ใครทำ", "คนไหน", "รายชื่อ",
        "สมาชิก", "ทีมงาน", "ตำแหน่ง", "ทำตำแหน่ง", "ผู้รับผิดชอบ",
    )


def _member_group_for_query(q: str) -> str | None:
    if _has(q, "สหกิจ", "ฝึกงาน", "internship", "intern", "cooperative", "ai chat bot developer", "web & ai", "game and 3d"):
        return "cooperative education and Internship student"
    if _has(q, "psu phuket esports club", "esports club", "ชมรม", "ประธาน", "รองประธาน", "เลขานุการ", "เหรัญญิก", "ประชาสัมพันธ์", "กรรมการ"):
        return "PSU Phuket Esports Club - PSU Phuket"
    if _has(q, "อธิการบดี", "รองอธิการบดี", "คณบดี", "ผู้ช่วยอธิการบดี", "ผู้จัดการ", "นักวิชาการคอมพิวเตอร์", "ผู้บริหาร", "members หลัก"):
        return "Members"
    return None


def _member_role_for_query(q: str) -> str | None:
    roles = (
        "AI Chat Bot Developer",
        "Game and 3D Developer",
        "Web & AI Developer",
        "Internship Student",
        "นักศึกษาสหกิจ",
        "นักศึกษาฝึกงาน",
        "อธิการบดี",
        "รองอธิการบดี",
        "คณบดี",
        "ผู้ช่วยอธิการบดีฝ่ายวิชาการ",
        "ผู้จัดการ",
        "นักวิชาการคอมพิวเตอร์",
        "ประธาน",
        "รองประธาน",
        "เลขานุการ",
        "เหรัญญิก",
        "ประชาสัมพันธ์",
        "กรรมการ",
    )
    q_norm = normalize_text(q)
    for role in roles:
        if normalize_text(role) in q_norm:
            return role
    return None


def _looks_like_member_group_summary_query(q: str) -> bool:
    if not _has(q, "สมาชิก", "member", "members", "ทีมงาน", "บุคลากร"):
        return False
    return _has(
        q,
        "กี่หมวด", "กี่กลุ่ม", "กี่หัวข้อ", "มีกี่หมวด", "มีกี่กลุ่ม", "มีกี่หัวข้อ",
        "หมวดอะไร", "หมวดอะไรบ้าง", "กลุ่มอะไร", "กลุ่มอะไรบ้าง",
        "หัวข้ออะไร", "หัวข้ออะไรบ้าง", "แยกหมวด", "แยกกลุ่ม",
    )


def _looks_like_member_game_relation_query(q: str) -> bool:
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


def _member_group_summary(rows: list[dict]) -> str:
    grouped: dict[str, list[dict]] = {group: [] for group in MEMBER_GROUP_ORDER}
    for row in rows:
        grouped.setdefault(str(row.get("group") or "Members"), []).append(row)

    groups = [(group, grouped.get(group) or []) for group in MEMBER_GROUP_ORDER if grouped.get(group)]
    lines = [f"สมาชิกในหน้า Members แบ่งเป็น {len(groups)} หมวดครับ"]
    for group, group_rows in groups:
        lines.append(f"- {group}: {len(group_rows)} คน")
    lines.append(f"รวมทั้งหมด {len(rows)} คน")
    lines.append(f"แหล่งข้อมูล: {MEMBERS_URL}")
    return "\n".join(lines)


def _member_name_match(q: str) -> dict | None:
    q_key = _game_alias_key(q)
    q_norm = normalize_text(q)
    best: tuple[int, dict] | None = None
    for row in _member_profiles():
        name = str(row.get("name") or "")
        name_key = _game_alias_key(name)
        if name_key and name_key in q_key:
            return row
        parts = [part for part in re.split(r"\s+", normalize_text(name)) if len(_game_alias_key(part)) >= 4]
        score = sum(1 for part in parts if part and part in q_norm)
        if score and (best is None or score > best[0]):
            best = (score, row)
    return best[1] if best else None


def _format_member_row(row: dict, *, include_details: bool = False) -> str:
    line = f"- {row.get('name')}: {row.get('role')}"
    if not include_details:
        return line
    affiliation = str(row.get("affiliation") or "").strip()
    period = str(row.get("period") or "").strip()
    if affiliation:
        line += f" ({affiliation})"
    if period:
        line += f" | ระยะเวลา: {period}"
    return line


def _format_member_groups(rows: list[dict], *, include_details: bool = False) -> str:
    grouped: dict[str, list[dict]] = {group: [] for group in MEMBER_GROUP_ORDER}
    for row in rows:
        grouped.setdefault(str(row.get("group") or "Members"), []).append(row)
    lines: list[str] = []
    for group in MEMBER_GROUP_ORDER:
        group_rows = grouped.get(group) or []
        if not group_rows:
            continue
        if lines:
            lines.append("")
        lines.append(f"{group} ({len(group_rows)} คน):")
        lines.extend(_format_member_row(row, include_details=include_details) for row in group_rows)
    return "\n".join(lines)


def answer_members(query: str, start: float) -> FastAnswer | None:
    q = normalize_text(query)
    if _looks_like_text_generation_request(q):
        return None
    if not _looks_like_member_query(q):
        return None

    rows = list(_member_profiles())
    if not rows:
        return None

    if _looks_like_member_game_relation_query(q):
        answer = (
            "ยังไม่พบข้อมูลที่ยืนยันได้ว่าสมาชิกหรือสตาฟแต่ละคนเล่นเกม/ดูแลเกมหรือโซนไหนครับ\n"
            "ข้อมูลที่มีตอนนี้ยืนยันได้เฉพาะรายชื่อสมาชิก หมวด และตำแหน่งในหน้า Members\n"
            f"แหล่งข้อมูล: {MEMBERS_URL}"
        )
        return _answer(answer, "members", "members_game_relation_no_data_fast_path", start, 0.90)

    if _looks_like_member_group_summary_query(q):
        return _answer(_member_group_summary(rows), "members", "members_group_summary_fast_path", start, 0.97)

    name_match = _member_name_match(q)
    role = _member_role_for_query(q)
    group = _member_group_for_query(q)
    if group == "cooperative education and Internship student" and _has(q, "cooperative", "สหกิจ", "ฝึกงาน") and _has(q, "มีใครบ้าง", "รายชื่อ", "ทั้งหมด"):
        role = None

    if name_match is not None:
        answer = (
            f"{name_match.get('name')} อยู่ในหมวด {name_match.get('group')}\n"
            f"ตำแหน่ง: {name_match.get('role')}"
        )
        affiliation = str(name_match.get("affiliation") or "").strip()
        period = str(name_match.get("period") or "").strip()
        if affiliation:
            answer += f"\nสังกัด/รายละเอียด: {affiliation}"
        if period:
            answer += f"\nระยะเวลา: {period}"
        answer += f"\nแหล่งข้อมูล: {MEMBERS_URL}"
        return _answer(answer, "members", "members_person_lookup_fast_path", start, 0.96)

    filtered = rows
    if group:
        filtered = [row for row in filtered if str(row.get("group") or "") == group]
    if role:
        role_norm = normalize_text(role)
        filtered = [row for row in filtered if role_norm in normalize_text(str(row.get("role") or ""))]

    if not filtered:
        return _answer(
            f"ยังไม่พบสมาชิกที่ตรงกับเงื่อนไขนี้ในหน้า Members ครับ\nแหล่งข้อมูล: {MEMBERS_URL}",
            "members",
            "members_no_match_fast_path",
            start,
            0.82,
        )

    if role:
        header = f"สมาชิกที่มีตำแหน่งเกี่ยวกับ `{role}`:"
    elif group:
        header = f"สมาชิกในหมวด {group}:"
    else:
        header = f"สมาชิกจากหน้า Members แยกตามหมวด รวม {len(filtered)} คน:"
    include_details = bool(group and len(filtered) <= 6)
    answer = f"{header}\n{_format_member_groups(filtered, include_details=include_details)}\nแหล่งข้อมูล: {MEMBERS_URL}"
    return _answer(answer, "members", "members_lookup_fast_path", start, 0.95)


def _match_all_game_details(q: str) -> list[tuple[str, dict]]:
    matches: list[tuple[str, dict]] = []
    for key, meta in GAME_DETAILS.items():
        aliases = _aliases_for_game(str(meta["name"]), meta["aliases"])
        if _game_alias_match(q, aliases, threshold=0.88):
            matches.append((key, meta))
    return matches


def _game_detail_answer(q: str, start: float) -> FastAnswer | None:
    if not _looks_like_game_detail(q):
        return None
    match = _match_game_detail(q)
    if match is None:
        return None

    _, meta = match
    lines = _game_detail_lines(meta, include_controls=_looks_like_play_method_query(q))
    source_key = str(meta.get("source") or "our_games")
    lines.append(f"แหล่งข้อมูล: {_source_url_for_game(meta)}")
    return _answer("\n".join(lines), source_key, "game_detail_fast_path", start, 0.96)


def _game_name_mention_answer(q: str, start: float) -> FastAnswer | None:
    if not _has(q, "เกม", "game"):
        return None
    if _looks_like_game_catalog(q) or _looks_like_game_availability(q):
        return None
    if _has(
        q,
        "ราคา", "ค่าบริการ", "กี่บาท", "เท่าไหร่", "เท่าไร", "เสียเงิน",
        "กติกา", "กฎ", "แข่ง", "แข่งขัน", "การแข่งขัน", "ลงแข่ง", "ทัวร์", "tournament",
    ):
        return None
    matches = _match_all_game_details(q)
    if not matches:
        return None

    if len(matches) == 1:
        _, meta = matches[0]
        source_key = str(meta.get("source") or "our_games")
        lines = _game_detail_lines(meta, include_controls=_looks_like_play_method_query(q))
        lines.append(f"แหล่งข้อมูล: {_source_url_for_game(meta)}")
        return _answer("\n".join(lines), source_key, "game_name_mention_detail_fast_path", start, 0.94)

    lines = ["พบชื่อเกมที่ตรงกับคำถามมากกว่า 1 เกมครับ"]
    sources: set[str] = set()
    for _key, meta in matches[:4]:
        zones = " และ ".join(meta["zones"])
        lines.append(f"- {meta['name']}: {meta['summary']} เล่นได้ที่: {zones}")
        sources.add(_source_url_for_game(meta))
    if len(matches) > 4:
        lines.append(f"- และอีก {len(matches) - 4} เกมที่ชื่อใกล้เคียงกัน")
    lines.append(f"แหล่งข้อมูล: {', '.join(sorted(sources))}")
    return _answer("\n".join(lines), "our_games", "game_multi_name_mention_fast_path", start, 0.93)


def _game_detail_unknown_no_answer(q: str, start: float) -> FastAnswer | None:
    if not _looks_like_game_detail(q):
        return None
    if _match_supported_game(q) or _match_game_family(q) or _match_known_unsupported_game(q):
        return None
    if _has_likely_named_game_detail(q):
        return None
    generic_detail_only = _has(q, "เกมอะไร", "แนวอะไร", "เกี่ยวกับอะไร") and not _has(q, "วิธีเล่น", "สอนเล่น", "เล่นยังไง", "เล่นอย่างไร")
    if generic_detail_only:
        return None
    return _answer(
        "ยังไม่แน่ใจว่าหมายถึงเกมไหนครับ จึงไม่ขอดึงเกมอื่นมาตอบแทน\n"
        "ถ้าต้องการถามวิธีเล่น ให้พิมพ์ชื่อเกมที่อยู่ในรายการ เช่น Beat Saber, VALORANT, PUBG, Super Smash Bros Ultimate หรือ Overcooked 2\n\n"
        f"{_catalog_summary()}\n"
        f"แหล่งข้อมูล: {OUR_GAMES_URL}",
        "our_games",
        "games_detail_unknown_no_answer_fast_path",
        start,
        0.93,
    )


def _zone_keys_for_query(q: str) -> list[str]:
    keys: list[str] = []
    if _has(q, "pc zone", "คอม", "คอมพิวเตอร์", "pc"):
        keys.append("pc")
    if _has(q, "cockpit zone", "cockpit", "ค็อกพิท", "คอกพิท", "พวงมาลัย", "ขับรถ"):
        keys.append("cockpit")
    if _has(q, "nintendo", "switch", "นินเทนโด"):
        keys.append("nintendo")
    if _has(q, "playstation", "ps5", "เพลย์", "เพลย์ห้า"):
        keys.append("ps5")
    if _has(q, "vr", "แว่น"):
        keys.append("vr")
    return list(dict.fromkeys(keys))


def _machine_numbers_from_query(q: str) -> list[int]:
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


def _service_rows_for_game_catalog_query(q: str) -> list[dict]:
    rows = list(_service_game_availability_rows())
    if not rows:
        return []
    keys = _zone_keys_for_query(q)
    numbers = _machine_numbers_from_query(q)
    selected: list[dict] = rows
    if keys:
        zone_labels = {CATALOG_ZONE_BY_KEY[key] for key in keys if key in CATALOG_ZONE_BY_KEY}
        selected = [row for row in selected if row.get("zone") in zone_labels]
    if numbers:
        selected = [
            row for row in selected
            if any(number in [int(value) for value in row.get("machine_numbers") or []] for number in numbers)
        ]
    if "nintendo" in keys:
        people = re.search(r"(\d+)\s*(?:คน|persons?|players?)", q)
        if people and int(people.group(1)) >= 3:
            selected = [row for row in selected if row.get("id") == "availability_nintendo_1_4"]
        elif people:
            selected = [row for row in selected if row.get("id") == "availability_nintendo_1_2"]
    if "vr" in keys:
        if _has(q, "30 นาที", "ครึ่งชั่วโมง", "30 min"):
            selected = [row for row in selected if row.get("duration_minutes") == 30]
        elif _has(q, "1 ชั่วโมง", "หนึ่งชั่วโมง", "60 นาที", "1 hour", "1 hr"):
            selected = [row for row in selected if row.get("duration_minutes") == 60]
        elif selected:
            selected = [row for row in selected if row.get("id") == "availability_vr_30"]
    if "pc" in keys and not numbers:
        selected = [row for row in rows if row.get("id") in {"availability_pc_01_02", "availability_pc_03_10"}]
    return selected


def _format_service_game_availability(rows: list[dict], intro: str) -> str:
    lines = [intro]
    for row in rows:
        lines.append("")
        lines.append(f"{row.get('service_label')} ({row.get('duration_minutes')} นาที, {row.get('capacity_persons')})")
        for game in row.get("games") or []:
            lines.append(f"•    {game}")
        for note in (row.get("notes") or [])[:2]:
            lines.append(f"หมายเหตุ: {note}")
    lines.append(f"แหล่งข้อมูล: {rows[0].get('source_url') if rows else RESERVATION_URL}")
    return "\n".join(lines)


def _looks_like_service_capacity_query(q: str) -> bool:
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


def _looks_like_game_presence_or_location_query(q: str) -> bool:
    return _has(
        q,
        "มีไหม",
        "มีมั้ย",
        "เล่นได้ไหม",
        "เล่นได้มั้ย",
        "เครื่องไหน",
        "อยู่เครื่องไหน",
        "เล่นได้ที่ไหน",
        "มีที่ไหน",
    ) or (
        _has(q, "มี", "เล่นได้")
        and _has(q, "ไหม", "มั้ย", "หรือเปล่า", "รึเปล่า", "ปะ")
    )


def _format_service_capacity_fast(rows: list[dict]) -> str:
    lines = ["บริการที่ถามรองรับผู้เล่นตามข้อมูลนี้ครับ"]
    for row in rows:
        lines.append(f"•    {row.get('service_label')}: {row.get('capacity_persons')} ต่อรอบ {row.get('duration_minutes')} นาที")
    lines.append(f"แหล่งข้อมูล: {rows[0].get('source_url') if rows else RESERVATION_URL}")
    return "\n".join(lines)


def _service_labels_fast(rows: list[dict]) -> str:
    return ", ".join(str(row.get("service_label")) for row in rows if row.get("service_label"))


def _service_game_availability_fast_answer(q: str, start: float) -> FastAnswer | None:
    rows = list(_service_game_availability_rows())
    if not rows:
        return None
    catalog_signal = _looks_like_equipment_game_catalog(q) or _looks_like_game_catalog(q) or _looks_like_game_total_count(q)
    service_scope_related = bool(_zone_keys_for_query(q) or _machine_numbers_from_query(q)) or _has(q, "โซน", "zone", "บริการ", "แต่ละเครื่อง", "แต่ละโซน", "ตามเครื่อง", "ตามโซน")
    if catalog_signal and not service_scope_related:
        return None
    if _has(q, "กี่ชั่วโมง", "ชั่วโมงต่อวัน", "เล่นกี่ชั่วโมง", "session", "sessions") and not _has(q, "กี่เกม", "จำนวนเกม"):
        return None
    capacity_signal = _looks_like_service_capacity_query(q) and bool(_zone_keys_for_query(q) or _machine_numbers_from_query(q))
    if capacity_signal:
        selected_capacity = _service_rows_for_game_catalog_query(q)
        if selected_capacity:
            return _answer(
                _format_service_capacity_fast(selected_capacity),
                "our_games",
                "service_capacity_fast_path",
                start,
                0.97,
            )

    wants_game_location = _looks_like_game_presence_or_location_query(q)
    game_match = _match_supported_game(q) if wants_game_location or not catalog_signal else None
    asks_game_location = game_match is not None and wants_game_location
    if asks_game_location:
        name, _meta = game_match
        key = _compact_key(name)
        zone_keys = _zone_keys_for_query(q)
        zone_labels = {CATALOG_ZONE_BY_KEY[item] for item in zone_keys if item in CATALOG_ZONE_BY_KEY}
        machine_numbers = _machine_numbers_from_query(q)
        matches = [
            row for row in rows
            if any(_compact_key(str(game)) == key for game in row.get("games") or [])
            and (not zone_labels or row.get("zone") in zone_labels)
            and (
                not machine_numbers
                or any(number in [int(value) for value in row.get("machine_numbers") or []] for number in machine_numbers)
            )
        ]
        if matches:
            services = ", ".join(str(row.get("service_label")) for row in matches)
            return _answer(
                f"ได้ครับ {name} เล่นได้ที่ {services}\nแหล่งข้อมูล: {matches[0].get('source_url') or RESERVATION_URL}",
                "our_games",
                "service_game_availability_fast_path",
                start,
                0.97,
            )
        requested_rows = _service_rows_for_game_catalog_query(q)
        same_zone_available = [
            row for row in rows
            if any(_compact_key(str(game)) == key for game in row.get("games") or [])
            and (not zone_labels or row.get("zone") in zone_labels)
        ]
        available_rows = same_zone_available or [
            row for row in rows
            if any(_compact_key(str(game)) == key for game in row.get("games") or [])
        ]
        if requested_rows or available_rows:
            requested_label = _service_labels_fast(requested_rows) or "บริการ/เครื่องที่ถาม"
            lines = [f"{requested_label} ไม่มี {name} ครับ"]
            if available_rows:
                lines.append(f"{name} เล่นได้ที่ {_service_labels_fast(available_rows)}")
            if requested_rows:
                lines.append("")
                lines.append(f"เกมที่มีใน {requested_label}:")
                for row in requested_rows:
                    for game in row.get("games") or []:
                        lines.append(f"•    {game}")
            lines.append(f"แหล่งข้อมูล: {available_rows[0].get('source_url') if available_rows else RESERVATION_URL}")
            return _answer(
                "\n".join(lines),
                "our_games",
                "service_game_availability_no_match_fast_path",
                start,
                0.91,
            )

    if not catalog_signal:
        return None
    selected = _service_rows_for_game_catalog_query(q)
    if not selected:
        return None
    keys = _zone_keys_for_query(q)
    if _looks_like_game_total_count(q):
        unique_games = {str(game) for row in selected for game in row.get("games") or []}
        zone_labels = [CATALOG_ZONE_BY_KEY[key] for key in keys if key in CATALOG_ZONE_BY_KEY]
        label = zone_labels[0] if len(zone_labels) == 1 else "บริการที่ถาม"
        intro = f"{label} มีเกมที่ยืนยันได้ {len(unique_games)} เกมครับ"
    elif keys == ["pc"]:
        intro = "PC Zone แยกรายการเกมตามเลขเครื่องดังนี้"
    elif keys == ["vr"] and not _has(q, "30 นาที", "ครึ่งชั่วโมง", "1 ชั่วโมง", "60 นาที"):
        intro = "VR Station มีเกมที่ยืนยันได้ดังนี้ (รอบ 30 นาทีและ 1 ชั่วโมงใช้รายการเกมเดียวกัน)"
    else:
        intro = "เกมที่ยืนยันได้ตามบริการที่ถามมีดังนี้"
    return _answer(
        _format_service_game_availability(selected, intro),
        "our_games",
        "service_game_availability_fast_path",
        start,
        0.97,
    )


def _equipment_game_catalog_answer(q: str, start: float) -> FastAnswer | None:
    if not _looks_like_equipment_game_catalog(q):
        return None

    keys = _zone_keys_for_query(q)
    if not keys:
        keys = ["pc", "ps5", "nintendo", "cockpit", "vr"]
        intro = "\u0e2a\u0e23\u0e38\u0e1b\u0e40\u0e01\u0e21\u0e17\u0e35\u0e48\u0e40\u0e25\u0e48\u0e19\u0e44\u0e14\u0e49\u0e15\u0e32\u0e21\u0e2d\u0e38\u0e1b\u0e01\u0e23\u0e13\u0e4c/\u0e42\u0e0b\u0e19\u0e02\u0e2d\u0e07 PSU Esports Studio - Phuket:"
    else:
        intro = "\u0e2a\u0e23\u0e38\u0e1b\u0e40\u0e01\u0e21\u0e17\u0e35\u0e48\u0e40\u0e25\u0e48\u0e19\u0e44\u0e14\u0e49\u0e43\u0e19\u0e42\u0e0b\u0e19\u0e17\u0e35\u0e48\u0e16\u0e32\u0e21:"

    lines = [_format_game_zone_sections(keys=keys, intro=intro)]
    if len(keys) <= 2:
        for key in keys:
            item = ZONE_DETAILS[key]
            lines.append("")
            lines.append(f"อุปกรณ์หลักของ {item['title']}")
            for equipment in EQUIPMENT_BY_ZONE.get(key, []):
                lines.append(f"•    {equipment}")
            lines.append("")
            lines.append(f"วิธีใช้งานโดยสรุป: {item['how']}")
    lines.append(f"\u0e41\u0e2b\u0e25\u0e48\u0e07\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25: {OUR_GAMES_URL}")
    return _answer("\n".join(lines), "our_games", "equipment_game_catalog_fast_path", start, 0.96)


def _zone_play_request_answer(q: str, start: float) -> FastAnswer | None:
    if not _has(q, "อยากเล่น", "อยากลองเล่น", "จะเล่น", "ขอเล่น", "เล่นได้ไหม", "เล่นได้มั้ย", "เล่นอะไร"):
        return None
    keys = _zone_keys_for_query(q)
    if not keys:
        return None
    lines = ["เล่นได้ครับ เลือกจองโซนที่ต้องการใช้งานก่อนเข้าใช้บริการ"]
    lines.append("")
    lines.append(_format_game_zone_sections(keys=keys[:2], intro="เกมที่มีข้อมูลยืนยันในโซนที่ถาม"))
    if "vr" in keys:
        lines.append("หมายเหตุ: VR Zone มีข้อมูลค่าบริการแยก 30 นาทีและ 1 ชั่วโมงตามกลุ่มผู้ใช้")
    lines.append(f"แหล่งข้อมูล: {OUR_GAMES_URL}")
    return _answer("\n".join(lines), "our_games", "zone_play_request_fast_path", start, 0.95)


def _related_guidance_answer(q: str, start: float) -> FastAnswer | None:
    guidance_signal = _has(
        q,
        "แนะนำ", "ควรเลือก", "เลือกอะไร", "เลือกโซน", "เหมาะกับ", "เหมาะไหม", "เหมาะมั้ย",
        "ต่างกันยังไง", "ต่างกันอย่างไร", "เปรียบเทียบ", "เทียบให้", "ไปกับเพื่อน",
        "มากับเพื่อน", "ไปกัน", "เล่นกับเพื่อน", "สาย", "แนว", "อยากเล่น",
        "มือใหม่", "มือไหม่", "เด็ก", "สำหรับเด็ก", "ครั้งแรก", "ไม่เคยเล่น",
    )
    if not guidance_signal:
        return None

    lines: list[str] = []
    source_note = f"แหล่งข้อมูล: {HOME_URL} และ {OUR_GAMES_URL}"

    if _has(q, "vr") and _has(q, "cockpit", "คอกพิท", "ค็อกพิท", "ขับรถ", "พวงมาลัย"):
        vr = ZONE_DETAILS["vr"]
        cockpit = ZONE_DETAILS["cockpit"]
        lines.extend([
            "ถ้าเทียบ VR กับ Cockpit:",
            f"- VR Zone: {vr['summary']} เกมที่ยืนยันได้คือ {vr['games']}",
            f"- Cockpit Zone: {cockpit['summary']} เกมที่ยืนยันได้คือ {cockpit['games']}",
            "เลือก VR ถ้าอยากได้ประสบการณ์เสมือนจริง/เกม VR; เลือก Cockpit ถ้าอยากเล่นเกมขับรถด้วยพวงมาลัยและเบาะจำลอง",
            "หมายเหตุ: ถ้าถามเรื่องราคา ต้องดูตาม Service Fee แยกตามกลุ่มผู้ใช้และระยะเวลา",
            source_note,
        ])
        return _answer("\n".join(lines), "home_our_games", "related_guidance_fast_path", start, 0.92)

    if _has(q, "เพื่อน", "ไปกัน", "มากัน", "กลุ่ม", "ครอบครัว", "4 คน", "สี่คน", "3 คน", "สามคน"):
        nintendo = ZONE_DETAILS["nintendo"]
        vr = ZONE_DETAILS["vr"]
        pc = ZONE_DETAILS["pc"]
        lines.extend([
            "ถ้าไปกับเพื่อน แนะนำให้เลือกตามสไตล์การเล่น:",
            f"- เล่นเป็นกลุ่ม/ครอบครัวหน้าจอเดียว: {nintendo['title']} เพราะมีเกม {nintendo['games']}",
            f"- อยากลอง VR เป็นกลุ่มเล็ก: {vr['title']} มีเกม {vr['games']} และตารางค่าบริการระบุ VR 1-5 คนต่อรอบ",
            f"- อยากเล่นเกม PC/FPS/MOBA แยกเครื่อง: {pc['title']} มี Gaming PC 10 เครื่อง และเกม {pc['games']}",
            "หมายเหตุ: PC 1 ชั่วโมง ราคา PSU Student and Staff 0 บาท, PSU Alumni and General Student 25 บาท, General Adult 70 บาท",
            source_note,
        ])
        return _answer("\n".join(lines), "home_our_games", "related_guidance_fast_path", start, 0.92)

    if _has(q, "ขยับตัว", "ออกกำลัง", "ออกกำลังกาย", "active", "จังหวะ", "เพลง", "rhythm"):
        lines.extend([
            "ถ้าอยากเล่นเกมที่ได้ขยับตัวหรือเล่นตามจังหวะ แนะนำเริ่มจาก VR Zone",
            "- เกมที่ยืนยันได้: Beat Saber เป็นเกม VR Rhythm ใช้ดาบแสงฟันบล็อกตามจังหวะเพลง",
            "- อีกทางเลือกในรายการเกมคือ Nintendo Switch Zone ที่มี Nintendo Switch Sports และ Ring Fit Adventure ใน catalog เกม",
            "ควรเลือกตามความถนัดและสอบถามเจ้าหน้าที่ก่อนเล่นถ้าไม่คุ้นกับอุปกรณ์ VR",
            source_note,
        ])
        return _answer("\n".join(lines), "home_our_games", "related_guidance_fast_path", start, 0.92)

    if _has(q, "ขับรถ", "รถ", "พวงมาลัย", "แข่งรถ", "racing", "sim"):
        cockpit = ZONE_DETAILS["cockpit"]
        lines.extend([
            "ถ้าอยากเล่นเกมขับรถ แนะนำ Cockpit Zone",
            f"- เหตุผล: {cockpit['summary']}",
            f"- อุปกรณ์หลัก: {cockpit['equipment']}",
            f"- เกมที่ยืนยันได้: {cockpit['games']}",
            source_note,
        ])
        return _answer("\n".join(lines), "home_our_games", "related_guidance_fast_path", start, 0.92)

    if _has(q, "นักเรียน", "นักศึกษา", "มือใหม่", "มือไหม่", "เด็ก", "ไม่เคยเล่น", "ครั้งแรก", "เริ่มต้น"):
        lines.extend([
            "ถ้าเป็นนักเรียน/นักศึกษาหรือมือใหม่ แนะนำเลือกจากความอยากลองก่อน:",
            "- อยากเล่นง่ายกับเพื่อน: Nintendo Switch Zone",
            "- อยากลอง VR: VR Zone มี Beat Saber และ Horizon Call of the Mountain",
            "- อยากเล่นเกมคอนโซล 1-2 คน: PlayStation 5 Zone",
            "- อยากฝึกเกม PC/eSports: PC Zone",
            "ข้อมูลค่าบริการมีแยกกลุ่ม PSU Student and Staff, PSU Alumni and General Student และ General Adult; ถ้าระบุกลุ่มผู้ใช้กับโซน ผมจะคำนวณราคาให้ได้",
            source_note,
        ])
        return _answer("\n".join(lines), "home_our_games", "related_guidance_fast_path", start, 0.91)

    if _has(q, "เกมแนว", "แนวเกม", "เล่นแนว", "อยากเล่นเกม", "มีเกมแนว"):
        lines.extend([
            "สรุปแนวเกมที่มีข้อมูลยืนยันได้:",
            "- FPS/Tactical/PC: VALORANT, Counter-Strike 2, Call of Duty: Warzone",
            "- MOBA: League of Legends",
            "- Fighting: TEKKEN 8",
            "- Racing/ขับรถ: Gran Turismo 7 ใน Cockpit Zone",
            "- VR/Rhythm: Beat Saber ใน VR Zone",
            "- Party/เล่นกับเพื่อน: Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports",
            source_note,
        ])
        return _answer("\n".join(lines), "home_our_games", "related_guidance_fast_path", start, 0.91)

    return None


def _zone_detail_answer(q: str, start: float) -> FastAnswer | None:
    keys = _zone_keys_for_query(q)
    if not keys:
        return None
    wants_zone_detail = _has(
        q,
        "zone", "โซน", "คืออะไร", "อะไรคือ", "มีอะไร", "ทำอะไร", "ใช้ทำอะไร", "อุปกรณ์",
        "เล่นอะไร", "เล่นยังไง", "เล่นอย่างไร", "วิธีเล่น", "กี่เครื่อง", "รุ่นอะไร", "พวงมาลัย", "แว่น",
    )
    if not wants_zone_detail:
        return None

    parts: list[str] = []
    for key in keys:
        item = ZONE_DETAILS[key]
        parts.append(str(item["summary"]))
        parts.append(f"วิธีใช้งานโดยสรุป: {item['how']}")
        parts.append("")
        parts.append(f"อุปกรณ์หลักของ {item['title']}")
        for equipment in EQUIPMENT_BY_ZONE.get(key, []):
            parts.append(f"•    {equipment}")
        parts.append("")
        parts.append(_format_game_zone_sections(keys=[key], intro="เกม/การใช้งานที่ยืนยันได้"))
        if len(keys) > 1:
            parts.append("")
    text = "\n".join(line for line in parts if line != "")
    text += "\nแหล่งข้อมูล: https://esports.phuket.psu.ac.th/home"
    return _answer(text, "home", "equipment_zone_fast_path", start, 0.95)


def _equipment_item_matches(q: str) -> list[dict]:
    matches: list[dict] = []
    for item in EQUIPMENT_ITEM_DETAILS.values():
        if _has(q, *item["aliases"]):
            matches.append(item)
    return matches


def _equipment_item_location_answer(q: str, start: float) -> FastAnswer | None:
    wants_location = _has(
        q,
        "โซนไหน", "อยู่โซน", "อยู่ที่ไหน", "อยู่ไหน", "มีที่ไหน", "เครื่องไหน", "อยู่ในโซน",
        "which zone", "where",
    )
    if not wants_location:
        return None

    matches = _equipment_item_matches(q)
    if not matches:
        return None

    if (
        len(matches) == 1
        and matches[0].get("title", "").startswith("Gaming PC")
        and _has(q, "เกม", "game", "fps", "moba", "ปาร์ตี้", "party", "แนว")
        and not _has(q, "เครื่อง", "สเปก", "สเป็ค", "spec", "อุปกรณ์", "รุ่น")
    ):
        return None

    if _has(q, "65"):
        matches = [item for item in matches if "65" in str(item.get("title", "")) or "65" in str(item.get("note", ""))]
    if _has(q, "86"):
        matches = [item for item in matches if "86" in str(item.get("title", "")) or "86" in str(item.get("note", ""))]
    if _has(q, "pulse elite"):
        matches = [item for item in matches if "pulse elite" in str(item.get("title", "")).lower()]
    if _has(q, "racezone", "full cockpit", "cockpit v3"):
        matches = [item for item in matches if "racezone" in str(item.get("title", "")).lower()]
    if _has(q, "logitech", "g923", "trueforce"):
        matches = [item for item in matches if "logitech" in str(item.get("title", "")).lower()]
    if _has(q, "sofa", "โซฟา"):
        matches = [item for item in matches if "sofa" in str(item.get("title", "")).lower()]

    if not matches:
        return None

    if len(matches) == 1:
        item = matches[0]
        detail = item.get("note") or item.get("what") or ""
        text = (
            f"{item['title']} อยู่ที่ {item['zone']} ครับ\n"
            f"• รายละเอียด: {detail}\n"
            f"แหล่งข้อมูล: {HOME_URL}"
        )
        return _answer(text, "home", "equipment_item_location_fast_path", start, 0.97)

    lines = ["อุปกรณ์ที่ถามอยู่ในโซนเหล่านี้ครับ"]
    for item in matches[:6]:
        lines.append(f"• {item['title']}: {item['zone']}")
    lines.append(f"แหล่งข้อมูล: {HOME_URL}")
    return _answer("\n".join(lines), "home", "equipment_item_location_fast_path", start, 0.95)


def _zone_tv_size_answer(q: str, start: float) -> FastAnswer | None:
    if not _has(q, "ทีวี", "tv") or not _has(q, "ขนาด", "กี่นิ้ว", "เท่าไหร่", "เท่าไร", "size"):
        return None
    keys = _zone_keys_for_query(q)
    if not keys:
        return None

    tv_items = [
        item
        for item in EQUIPMENT_ITEM_DETAILS.values()
        if str(item.get("title", "")).lower().startswith("tv ")
    ]
    lines: list[str] = []
    for key in keys:
        zone_title = ZONE_DETAILS.get(key, {}).get("title", CATALOG_ZONE_BY_KEY.get(key, key))
        zone_tvs = [item for item in tv_items if item.get("zone") == zone_title]
        if not zone_tvs:
            continue
        if len(zone_tvs) == 1:
            item = zone_tvs[0]
            lines.append(f"{zone_title} มี {item['title']} ครับ")
            if item.get("note"):
                lines.append(f"• {item['note']}")
        else:
            lines.append(f"{zone_title} มีทีวีตามข้อมูลนี้ครับ")
            for item in zone_tvs:
                lines.append(f"• {item['title']}: {item.get('note', '')}")
        lines.append("")

    if not lines:
        return None
    text = "\n".join(line for line in lines if line != "")
    text += f"\nแหล่งข้อมูล: {HOME_URL}"
    return _answer(text, "home", "equipment_tv_size_fast_path", start, 0.97)


def _equipment_item_detail_answer(q: str, start: float) -> FastAnswer | None:
    wants_item_detail = _has(
        q,
        "คืออะไร", "อะไรคือ", "มีอะไร", "ทำอะไร", "ใช้ทำอะไร", "เล่นอะไร", "เล่นยังไง", "เล่นอย่างไร",
        "ใช้ยังไง", "ใช้อย่างไร", "วิธีเล่น", "วิธีใช้", "อุปกรณ์", "รุ่นอะไร",
    )
    if not wants_item_detail:
        return None

    if _has(q, "zone", "โซน") and not _has(
        q,
        "g923", "trueforce", "driving force", "shifter", "racezone", "pulse elite",
        "vr2", "psvr2", "playstation vr2", "แว่น", "oled", "slim", "gaming ",
        "เมาส์", "คีย์บอร์ด", "หูฟัง", "เก้าอี้", "จอ", "ทีวี 65", "ทีวี 86",
    ):
        return None

    matches = _equipment_item_matches(q)
    if not matches:
        return None

    wants_how = _has(q, "เล่นยังไง", "เล่นอย่างไร", "ใช้ยังไง", "ใช้อย่างไร", "วิธีเล่น", "วิธีใช้", "ยังไง")
    wants_games = _has(q, "เล่นอะไร", "ทำอะไร", "ใช้ทำอะไร")
    parts: list[str] = []
    for item in matches[:3]:
        parts.append(f"{item['title']}: {item['what']}")
        if wants_how:
            parts.append(f"วิธีใช้งาน/เล่นโดยสรุป: {item['how']}")
        if wants_games or wants_how:
            parts.append(f"ใช้ทำอะไร/เล่นอะไรได้: {item['use']}")
        else:
            parts.append(f"ใช้ทำอะไร/เล่นอะไรได้: {item['use']}")
            parts.append(f"วิธีใช้งานโดยสรุป: {item['how']}")
        parts.append(f"อยู่ใน: {item['zone']}")
        if item.get("note"):
            parts.append(f"หมายเหตุข้อมูล: {item['note']}")
        parts.append("")

    text = "\n".join(line for line in parts if line != "")
    text += "\nแหล่งข้อมูล: https://esports.phuket.psu.ac.th/home"
    return _answer(text, "home", "equipment_item_fast_path", start, 0.96)


def _equipment_usage_guide_answer(q: str, start: float) -> FastAnswer | None:
    wants_usage = _has(
        q,
        "วิธีใช้", "วิธีใช้งาน", "ใช้งานยังไง", "ใช้ยังไง", "ใช้อย่างไร",
        "สอนใช้", "สอนเล่น", "เริ่มเล่น", "start", "how to use", "how to play",
        "เปิดเครื่อง", "เมนูเกม", "ต่อจอย", "second controller", "ยังไง", "อย่างไร",
    )
    if not wants_usage:
        return None

    keys = _zone_keys_for_query(q)
    if not keys and _has(q, "พวงมาลัย", "ขับรถ", "gran turismo", "gt7"):
        keys = ["cockpit"]
    if not keys:
        return None

    key = keys[0]
    if key == "cockpit":
        text = (
            "วิธีเริ่มใช้งาน Cockpit / Gran Turismo 7:\n"
            "ภาษาไทย:\n"
            "1. กดปุ่ม Home บนจอย PS5 เพื่อเปิดเครื่อง\n"
            "2. กดปุ่ม X เพื่อเลือกโปรไฟล์ Cockpitone CoC PSU หรือ Cockpittwo CoC PSU ตามสถานีที่ใช้\n"
            "3. ใช้ปุ่มลูกศรเลือก Gran Turismo 7 แล้วกด X เพื่อเริ่มเกม\n"
            "4. กดปุ่ม O เพื่อข้ามวิดีโอแนะนำเกม\n"
            "5. กดปุ่ม Home บนพวงมาลัย แล้วกด X เพื่อเลือกโปรไฟล์ของ Cockpit\n"
            "6. ในเมนู ใช้ปุ่มลูกศรบนพวงมาลัยเลื่อนรายการ, กด X เพื่อยืนยัน และกด O เพื่อย้อนกลับ\n"
            "7. เวลาเล่น ใช้แป้นเบรก แป้นคันเร่ง และพวงมาลัยควบคุมรถ\n\n"
            "English:\n"
            "1. Press the Home button on the PS5 controller to power on the console\n"
            "2. Press X to select the Cockpit profile for the station\n"
            "3. Use the arrow buttons to select Gran Turismo 7, then press X to start\n"
            "4. Press O to skip the introduction video\n"
            "5. Press Home on the steering wheel, then press X to select the profile\n"
            "6. In menus, use arrow buttons to navigate, X to confirm, and O to go back\n"
            "7. Drive with the brake pedal, accelerator pedal, and steering wheel\n"
            f"แหล่งข้อมูล: {EQUIPMENT_HOW_TO_URL}"
        )
        return _answer(text, "equipment_how_to", "equipment_usage_cockpit_fast_path", start, 0.97)

    if key == "ps5":
        text = (
            "วิธีเริ่มใช้งาน PlayStation 5:\n"
            "ภาษาไทย:\n"
            "1. กดปุ่ม Home บนจอย PS5 เพื่อเปิดเครื่อง\n"
            "2. กดปุ่ม X เพื่อเลือกโปรไฟล์ของสถานี PS5 ที่ใช้งาน\n"
            "3. ใช้ปุ่มลูกศรเลือกเกม แล้วกด X เพื่อเริ่มเกม\n"
            "4. ในเมนูเกม ใช้ปุ่มลูกศรเพื่อเลื่อนรายการ, กด X เพื่อยืนยัน และกด O เพื่อย้อนกลับ\n"
            "5. ถ้าต้องต่อจอยที่สอง ให้กดปุ่ม Home บนจอยที่สอง เลือกโปรไฟล์ของจอยที่สอง แล้วกด X เพื่อยืนยัน\n\n"
            "English:\n"
            "1. Press the Home button on the PS5 controller to power on the console\n"
            "2. Press X to select the station profile\n"
            "3. Use the arrow buttons to choose a game, then press X to start\n"
            "4. In game menus, use arrow buttons to navigate, X to confirm, and O to go back\n"
            "5. To connect a second controller, press Home on the second controller, select its profile, then press X\n"
            f"แหล่งข้อมูล: {EQUIPMENT_HOW_TO_URL}"
        )
        return _answer(text, "equipment_how_to", "equipment_usage_ps5_fast_path", start, 0.97)

    if key == "vr":
        text = (
            "วิธีเริ่มใช้งาน VR / Beat Saber:\n"
            "ภาษาไทย:\n"
            "1. กดปุ่ม Home บนจอย PS5 เพื่อเปิดเครื่อง\n"
            "2. กด X เพื่อเลือกโปรไฟล์ VR CoC PSU\n"
            "3. ใช้ปุ่มลูกศรเลือก Beat Saber แล้วกด X เพื่อเริ่มเกม\n"
            "4. กดปุ่ม Power ใต้แว่น VR\n"
            "5. กดปุ่มบนแว่นแล้วดึงส่วนหน้าของแว่นออก วางส่วนรองจมูกให้เข้าที่ก่อน แล้วหมุนปุ่ม Dial เพื่อปรับความกระชับ\n"
            "6. กดปุ่ม Home บนคอนโทรลเลอร์ VR ทั้งสองข้าง แล้วเลือก Yes ด้วยปุ่ม X เมื่อระบบถาม\n"
            "7. ปรับเลนส์ด้วย Slider\n"
            "8. ใช้คอนโทรลเลอร์ VR ขวาชี้ปุ่ม OK บนหน้าจอ แล้วกด R2 เพื่อยืนยัน\n"
            "9. ในเมนูเกม ใช้คอนโทรลเลอร์ VR ขวาเลื่อนเมนู และกด R2 เพื่อยืนยัน\n\n"
            "English:\n"
            "1. Press Home on the PS5 controller to power on the console\n"
            "2. Press X to select the VR CoC PSU profile\n"
            "3. Select Beat Saber with the arrow buttons, then press X to start\n"
            "4. Press the power button under the VR headset\n"
            "5. Press the headset button and pull it outward, place your nose support first, then tighten with the dial\n"
            "6. Press Home on both VR controllers and select Yes with X when prompted\n"
            "7. Adjust the lenses using the slider\n"
            "8. Point at OK with the right VR controller and press R2\n"
            "9. In game menus, use the right VR controller to navigate and press R2 to confirm\n"
            f"แหล่งข้อมูล: {EQUIPMENT_HOW_TO_URL}"
        )
        return _answer(text, "equipment_how_to", "equipment_usage_vr_fast_path", start, 0.97)

    if key == "nintendo":
        text = (
            "วิธีเริ่มใช้งาน Nintendo Switch:\n"
            "ภาษาไทย:\n"
            "1. กดปุ่ม Power เพื่อเปิดเครื่อง\n"
            "2. กดปุ่ม Release ค้างไว้ แล้วเลื่อน Joy-Con ขึ้นเพื่อถอดออกจากเครื่อง\n"
            "3. กดปุ่ม A เพื่อเข้า Home screen แล้วใช้ Analog Stick ไปที่ไอคอน Controller และกด A สองครั้ง\n"
            "4. หมุน Joy-Con แนวนอน แล้วกดปุ่ม SL และ SR พร้อมกัน ทำซ้ำกับจอยที่ต้องการใช้\n"
            "5. กดปุ่มด้านขวาเพื่อยืนยันการตั้งค่า แล้วกดปุ่มด้านล่างเพื่อออกจากหน้าตั้งค่า\n"
            "6. ใช้ Analog Stick เลื่อนในเกม และกดปุ่มด้านขวาเพื่อเริ่มเกม/ยืนยัน\n"
            "7. ในเมนูเกม ใช้ Analog Stick เลื่อน, กดปุ่มด้านขวาเพื่อยืนยัน และกดปุ่มด้านล่างเพื่อย้อนกลับ\n\n"
            "English:\n"
            "1. Press the Power button to turn on the console\n"
            "2. Press and hold the release button, then slide the Joy-Con upward to detach it\n"
            "3. Press A to open the Home screen, go to the controller icon, and press A twice\n"
            "4. Rotate the Joy-Con horizontally and press SL + SR together for each controller\n"
            "5. Press the right button to confirm setup, then press the bottom button to exit settings\n"
            "6. Use the analog stick to navigate and press the right button to start/confirm\n"
            "7. In menus, use the analog stick to navigate, the right button to confirm, and the bottom button to go back\n"
            f"แหล่งข้อมูล: {EQUIPMENT_HOW_TO_URL}"
        )
        return _answer(text, "equipment_how_to", "equipment_usage_nintendo_fast_path", start, 0.97)

    return None


def _cross_zone_game_answer(q: str, start: float) -> FastAnswer | None:
    wants_cross_zone = (
        _has(q, "ทั้ง pc", "pc และ ps5", "pc กับ ps5", "pc/ps5", "คอมและ ps5", "คอมกับ ps5")
        and _has(q, "เกมไหน", "เกมอะไร", "เล่นได้", "มีเกม")
    )
    if not wants_cross_zone:
        return None

    pc_ps5_games = [
        meta
        for meta in GAME_DETAILS.values()
        if "PC Zone" in meta.get("zones", ()) and "PlayStation 5 Zone" in meta.get("zones", ())
    ]
    if not pc_ps5_games:
        return _answer(
            f"ตอนนี้ยังไม่พบเกมที่ยืนยันว่าเล่นได้ทั้ง PC Zone และ PlayStation 5 Zone ในฐานข้อมูลครับ\n"
            f"แหล่งข้อมูล: {OUR_GAMES_URL}",
            "our_games",
            "games_cross_zone_fast_path",
            start,
            0.94,
        )

    lines = ["เกมที่เล่นได้ทั้ง PC Zone และ PlayStation 5 Zone คือ"]
    for meta in sorted(pc_ps5_games, key=lambda item: item.get("name", "")):
        zones = " และ ".join(meta.get("zones", ()))
        lines.append(f"• {meta['name']}: {zones}")
    lines.append(f"แหล่งข้อมูล: {OUR_GAMES_URL}")
    return _answer("\n".join(lines), "our_games", "games_cross_zone_fast_path", start, 0.97)


def _zone_suitability_answer(q: str, start: float) -> FastAnswer | None:
    keys = _zone_keys_for_query(q)
    if not keys:
        return None
    if not _has(q, "เหมาะกับ", "เหมาะไหม", "เหมาะมั้ย", "แนวไหน", "แนวอะไร", "มือใหม่", "มือไหม่", "ครั้งแรก", "ไม่เคยเล่น"):
        return None

    lines: list[str] = []
    for key in keys[:2]:
        zone = ZONE_DETAILS[key]
        games = [
            meta
            for meta in GAME_DETAILS.values()
            if CATALOG_ZONE_BY_KEY.get(key) in meta.get("zones", ())
        ]
        if _has(q, "มือใหม่", "มือไหม่", "ครั้งแรก", "ไม่เคยเล่น"):
            if key == "vr":
                lines.append("VR Zone เหมาะกับมือใหม่ที่อยากลองประสบการณ์ VR ครับ")
                lines.append("• แนะนำเริ่มจาก Beat Saber เพราะรูปแบบการเล่นเข้าใจง่ายกว่าเกมผจญภัย VR")
                lines.append("• ควรให้เจ้าหน้าที่ช่วยแนะนำการใส่แว่นและคอนโทรลเลอร์ก่อนเริ่มเล่น")
            elif key == "nintendo":
                lines.append("Nintendo Switch Zone เหมาะกับมือใหม่และเล่นกับเพื่อนครับ")
                lines.append("• จุดเด่นคือเกมเล่นง่าย/เล่นเป็นกลุ่ม เช่น Mario Kart, Overcooked และ Switch Sports")
            elif key == "cockpit":
                lines.append("Cockpit Zone เหมาะกับคนที่อยากลองเกมขับรถมากกว่ามือใหม่ทั่วไปครับ")
                lines.append("• ถ้าไม่เคยเล่นควรให้เจ้าหน้าที่แนะนำพวงมาลัย เบรก คันเร่ง และเมนูเกมก่อน")
            elif key == "ps5":
                lines.append("PlayStation 5 Zone เหมาะกับคนที่อยากเล่นเกมคอนโซลครับ")
                lines.append("• มือใหม่ควรเริ่มจากเกมที่คุ้นแนวหรือให้เจ้าหน้าที่ช่วยแนะนำจอย/เมนูก่อน")
            else:
                lines.append("PC Zone เหมาะกับคนที่คุ้นเมาส์คีย์บอร์ดหรืออยากเล่นเกม FPS/MOBA ครับ")
                lines.append("• มือใหม่ควรเริ่มจากเกมที่คุ้นแนวและสอบถามเจ้าหน้าที่เรื่องบัญชี/โปรแกรมก่อนเล่น")
        else:
            lines.append(f"{zone['title']} เหมาะกับแนวนี้ครับ")
            genres: list[str] = []
            for meta in games:
                genre = str(meta.get("genre") or "ยังไม่ระบุแนวเกม")
                if genre not in genres:
                    genres.append(genre)
            for genre in genres[:6]:
                lines.append(f"• {genre}")

        if games:
            lines.append("เกมที่ยืนยันได้ในโซนนี้")
            for meta in games[:10]:
                genre = str(meta.get("genre") or "ยังไม่ระบุแนวเกม")
                lines.append(f"• {meta['name']}: {genre}")
        lines.append("")

    lines.append(f"แหล่งข้อมูล: {HOME_URL} และ {OUR_GAMES_URL}")
    return _answer("\n".join(line for line in lines if line != ""), "home_our_games", "zone_suitability_fast_path", start, 0.95)


def answer_games(query: str, start: float) -> FastAnswer | None:
    q = normalize_text(query)
    booking_howto = _booking_howto_answer(q, start)
    if booking_howto is not None:
        return booking_howto
    equipment_location_answer = _equipment_item_location_answer(q, start)
    if equipment_location_answer is not None:
        return equipment_location_answer
    tv_size_answer = _zone_tv_size_answer(q, start)
    if tv_size_answer is not None:
        return tv_size_answer
    zone_suitability_answer = _zone_suitability_answer(q, start)
    if zone_suitability_answer is not None:
        return zone_suitability_answer
    cross_zone_answer = _cross_zone_game_answer(q, start)
    if cross_zone_answer is not None:
        return cross_zone_answer
    if _genre_group_for_query(q) is None and _looks_like_competition_game_list(q):
        return _answer(
            f"{COMPETITION_GAME_SUMMARY}\nแหล่งข้อมูล: data/competition_rules",
            "our_games",
            "competition_game_list_fast_path",
            start,
            0.95,
        )
    popularity_answer = _game_popularity_no_answer(q, start)
    if popularity_answer is not None:
        return popularity_answer
    missing_data_answer = _game_missing_data_answer(q, start)
    if missing_data_answer is not None:
        return missing_data_answer
    non_current_answer = _known_non_current_game_answer(q, start)
    if non_current_answer is not None:
        return non_current_answer
    unsupported_answer = _known_unsupported_game_answer(q, start)
    if unsupported_answer is not None:
        return unsupported_answer
    zone_play_answer = _zone_play_request_answer(q, start)
    if zone_play_answer is not None:
        return zone_play_answer
    service_availability_answer = _service_game_availability_fast_answer(q, start)
    if service_availability_answer is not None:
        return service_availability_answer
    equipment_catalog_answer = _equipment_game_catalog_answer(q, start)
    if equipment_catalog_answer is not None:
        return equipment_catalog_answer
    genre_answer = _game_genre_list_answer(q, start)
    if genre_answer is not None:
        return genre_answer
    if _looks_like_game_total_count(q):
        return _answer(f"{_game_catalog_count_summary(q)}\nแหล่งข้อมูล: {OUR_GAMES_URL}", "our_games", "games_full_catalog_count_fast_path", start, 0.96)
    if _looks_like_game_catalog(q):
        return _answer(f"{_catalog_summary()}\nแหล่งข้อมูล: {OUR_GAMES_URL}", "our_games", "games_catalog_fast_path", start, 0.95)
    if _match_game_family(q) and (_looks_like_game_availability(q) or _has(q, "มีเกม", "เกมอะไรบ้าง", "เกมอะไร", "อะไรบ้าง", "รายชื่อ")):
        family_answer = _game_family_availability_answer(q, start)
        if family_answer is not None:
            return family_answer
    detail_answer = _game_detail_answer(q, start)
    if detail_answer is not None:
        return detail_answer
    family_answer = _game_family_availability_answer(q, start)
    if family_answer is not None:
        return family_answer
    unsupported_answer = _known_unsupported_game_answer(q, start)
    if unsupported_answer is not None:
        return unsupported_answer
    name_mention_answer = _game_name_mention_answer(q, start)
    if name_mention_answer is not None:
        return name_mention_answer
    detail_unknown_answer = _game_detail_unknown_no_answer(q, start)
    if detail_unknown_answer is not None:
        return detail_unknown_answer
    supported = _match_supported_game(q)
    if supported and _looks_like_game_availability(q):
        name, meta = supported
        zones = " และ ".join(meta["zones"])
        return _answer(
            f"เล่น {name} ได้ครับ\n"
            f"มีให้เล่นที่: {zones}\n"
            f"แนะนำให้จองโซนที่ต้องการก่อนเข้าใช้บริการ และถ้าไม่แน่ใจเรื่องเครื่องหรือรอบเวลาให้สอบถามเจ้าหน้าที่ก่อนจองครับ\n"
            f"แหล่งข้อมูล: {OUR_GAMES_URL}",
            "our_games",
            "games_availability_fast_path",
            start,
            0.95,
        )
    if _looks_like_game_availability(q):
        known_unsupported = _match_known_unsupported_game(q)
        family_answer = _game_family_availability_answer(q, start)
        if family_answer is not None:
            return family_answer
        requested = _requested_unknown_game_name(q)
        note = ""
        if known_unsupported:
            note = "\nหมายเหตุ: ในฐานข้อมูลมีข้อมูลกติกาการแข่งขันของเกมนี้ แต่ยังไม่พบว่าอยู่ในรายการเกมให้เล่นของศูนย์"
        return _answer(
            f"ยังไม่พบ {requested} ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ\n"
            f"ถ้าต้องการเล่นเกมนอกเหนือจากรายการนี้ ควรสอบถามเจ้าหน้าที่ก่อนจองหรือก่อนเข้าใช้บริการ{note}\n\n"
            f"{_catalog_summary()}\n"
            f"แหล่งข้อมูล: {OUR_GAMES_URL}",
            "our_games",
            "games_unknown_fast_path",
            start,
            0.94,
        )
    related_answer = _related_guidance_answer(q, start)
    if related_answer is not None:
        return related_answer
    if _looks_like_game_detail(q):
        family_answer = _game_family_availability_answer(q, start)
        if family_answer is not None:
            return family_answer
    if _has(q, "เกมอะไร", "เกมทั้งหมด", "รายชื่อเกม", "รายการเกม", "list game", "games"):
        if _looks_like_game_total_count(q):
            return _answer(f"{_game_catalog_count_summary(q)}\nแหล่งข้อมูล: {OUR_GAMES_URL}", "our_games", "games_full_catalog_count_fast_path", start, 0.95)
        return _answer(f"{_catalog_summary()}\nแหล่งข้อมูล: {OUR_GAMES_URL}", "our_games", "games_catalog_fast_path", start, 0.94)
    if _has(q, "วาโล", "valorant", "cs2", "counter-strike", "pubg", "warzone", "pc games", "เกมบน pc", "คอมมี"):
        return _answer(f"{_format_game_zone_sections(keys=['pc'], intro='PC Zone มีเกมที่ยืนยันได้ดังนี้')}\nแหล่งข้อมูล: {OUR_GAMES_URL}", "our_games", "games_fast_path", start)
    if _has(q, "spider-man", "spider", "tekken", "fortnite", "god of war", "playstation", "ps5", "เพลย์"):
        return _answer(f"{_format_game_zone_sections(keys=['ps5'], intro='PlayStation 5 Zone มีเกมที่ยืนยันได้ดังนี้')}\nแหล่งข้อมูล: {OUR_GAMES_URL}", "our_games", "games_fast_path", start)
    if _has(q, "mario kart", "overcooked", "super smash", "switch sports", "nintendo", "switch", "นินเทนโด"):
        return _answer(f"{_format_game_zone_sections(keys=['nintendo'], intro='Nintendo Switch Zone มีเกมที่ยืนยันได้ดังนี้')}\nแหล่งข้อมูล: {OUR_GAMES_URL}", "our_games", "games_fast_path", start)
    if _has(q, "beat saber", "horizon", "vr", "แว่น"):
        return _answer(f"{_format_game_zone_sections(keys=['vr'], intro='VR Zone มีเกมที่ยืนยันได้ดังนี้')}\nแหล่งข้อมูล: {OUR_GAMES_URL}", "our_games", "games_fast_path", start)
    if _has(q, "gran turismo", "cockpit", "พวงมาลัย"):
        return _answer(f"{_format_game_zone_sections(keys=['cockpit'], intro='Cockpit Zone มีเกมที่ยืนยันได้ดังนี้')}\nแหล่งข้อมูล: {OUR_GAMES_URL}", "our_games", "games_fast_path", start)
    return None


def answer_equipment(query: str, start: float) -> FastAnswer | None:
    q = normalize_text(query)
    service_availability_answer = _service_game_availability_fast_answer(q, start)
    if service_availability_answer is not None:
        return service_availability_answer
    booking_howto = _booking_howto_answer(q, start)
    if booking_howto is not None:
        return booking_howto
    if _looks_like_game_total_count(q):
        return None
    usage_answer = _equipment_usage_guide_answer(q, start)
    if usage_answer is not None:
        return usage_answer
    equipment_location_answer = _equipment_item_location_answer(q, start)
    if equipment_location_answer is not None:
        return equipment_location_answer
    tv_size_answer = _zone_tv_size_answer(q, start)
    if tv_size_answer is not None:
        return tv_size_answer
    zone_suitability_answer = _zone_suitability_answer(q, start)
    if zone_suitability_answer is not None:
        return zone_suitability_answer
    cross_zone_answer = _cross_zone_game_answer(q, start)
    if cross_zone_answer is not None:
        return cross_zone_answer
    genre_answer = _game_genre_list_answer(q, start)
    if genre_answer is not None:
        return genre_answer
    related_answer = _related_guidance_answer(q, start)
    if related_answer is not None:
        return related_answer
    equipment_catalog_answer = _equipment_game_catalog_answer(q, start)
    if equipment_catalog_answer is not None:
        return equipment_catalog_answer
    if _match_supported_game(q) and _looks_like_game_availability(q):
        return None
    item_answer = _equipment_item_detail_answer(q, start)
    if item_answer is not None:
        return item_answer
    zone_answer = _zone_detail_answer(q, start)
    if zone_answer is not None:
        return zone_answer
    if _match_supported_game(q):
        return None
    if _has(q, "warzone", "horizon", "gran turismo"):
        return None
    if _has(q, "pc", "คอม", "คอมพิวเตอร์") and _has(q, "มี", "ให้เล่น", "เล่นได้", "ใช้ได้", "เข้าใช้", "เปิดให้เล่น"):
        text = "\n\n".join([
            "มีครับ ศูนย์มี PC Zone สำหรับเล่นเกมบนคอมพิวเตอร์",
            _equipment_home_summary(["pc"]),
            _format_game_zone_sections(keys=["pc"], intro="เกมที่มีข้อมูลยืนยันใน PC Zone"),
            "แนะนำให้จอง PC Zone ตามรอบบริการก่อนเข้าใช้งานครับ",
            f"แหล่งข้อมูล: {HOME_URL} และ {OUR_GAMES_URL}",
        ])
        return _answer(text, "home_our_games", "pc_availability_fast_path", start, 0.96)
    if _has(q, "pc", "คอม", "คอมพิวเตอร์") and _has(q, "สเป็ค", "สเปค", "spec", "specs", "cpu", "gpu", "การ์ดจอ", "แรม", "ram", "รุ่นอะไร"):
        text = """สเปก PC ที่บันทึกไว้ตอนนี้: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, CPU Intel Core i5-14400, RAM DDR5 32GB, GPU NVIDIA GeForce RTX 5060 8GB, Mainboard MSI PRO H610M-G และใน PC Zone มี Gaming PC ทั้งหมด 10 เครื่อง

หมายเหตุ: ข้อมูลนี้มาจากสเปกเครื่อง/ภาพ CPU-Z ที่บันทึกไว้ในโปรเจกต์ ส่วนหน้า Home ระบุรายการอุปกรณ์ PC Zone เช่น Gaming PC, Gaming Monitor, Gaming Chair, Gaming Keyboard, Gaming Mouse และ Gaming Headset"""
        return _answer(text, "home", "equipment_fast_path", start)
    if not _has(q, " zone", "โซน", "อุปกรณ์", "กี่เครื่อง", "รุ่นอะไร", "สเป็ค", "สเปค", "spec", "specs", "cpu", "gpu", "การ์ดจอ", "แรม", "ram", "ทีวี", "จออะไร", "จอกี่", "monitor", "เก้าอี้", "เมาส์", "หูฟัง", "พวงมาลัย", "แว่น"):
        return None
    text = f"อุปกรณ์บนหน้า Home:\n\n{_equipment_home_summary()}"
    return _answer(text, "home", "equipment_fast_path", start)


def _booking_step_fast_answer(q: str, start: float) -> FastAnswer | None:
    if not _has(q, "จอง", "booking"):
        return None
    match = re.search(r"(?:ขั้น|ขั้นที่)\s*(?:ที่)?\s*([1-5])", q)
    if not match:
        return None
    step = int(match.group(1))
    steps = {
        1: "ขั้นที่ 1 คือเลือกบริการหรือโซนที่ต้องการใช้ เช่น PlayStation 5, Nintendo Switch, Cockpit, VR หรือโซนที่ระบบจองมีให้เลือก",
        2: "ขั้นที่ 2 คือเลือกวันและรอบเวลาที่ต้องการเข้าใช้บริการจากรอบที่ระบบเปิดให้จอง",
        3: "ขั้นที่ 3 คือกรอกข้อมูลผู้ใช้บริการ เช่น Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล และเบอร์โทรศัพท์",
        4: "ขั้นที่ 4 คือตรวจสอบข้อมูลการจองและชำระเงินโดยโอนเข้าบัญชีธนาคารที่ระบบแจ้ง",
        5: "ขั้นที่ 5 คือแนบสลิปการโอนเงินและยืนยันการจองในระบบ",
    }
    answer = (
        f"{steps[step]}\n"
        "โดยภาพรวมต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง และหลังจองต้องชำระเงินภายใน 10 นาที\n"
        f"แหล่งข้อมูล: {RESERVATION_URL}"
    )
    return _answer(answer, "reservation", "booking_step_fast_path", start, 0.96)


def _looks_like_booking_howto(q: str) -> bool:
    if not _has(q, "จอง", "booking", "book", "reservation"):
        return False
    if _has(
        q,
        "ยกเลิก", "แก้ไข", "แก้เวลา", "จองผิด", "คืนเงิน", "refund",
        "ไม่จ่าย", "ลืมจ่าย", "ชำระ", "โอนเงิน", "สลิป", "เลขบัญชี",
        "เช็คอิน", "เชคอิน", "checkin",
    ):
        return False
    return _has(
        q,
        "สอน", "วิธี", "วิธีการ", "ขั้นตอน", "ทำยังไง", "ต้องทำยังไง",
        "ทำอย่างไร", "ยังไง", "อย่างไร", "อยากจอง", "จองคิว",
        "จองเครื่อง", "จองอุปกรณ์", "จองเล่น", "จองใช้", "จองบริการ",
    )


def _booking_howto_answer(q: str, start: float) -> FastAnswer | None:
    if _has_strong_game_catalog_terms(q) or _looks_like_game_total_count(q):
        return None
    if not _looks_like_booking_howto(q):
        return None
    service_hint = ""
    if _has(q, "vr", "วีอาร์", "แว่น"):
        service_hint = "ถ้าต้องการจอง VR ให้เลือกบริการ VR Station และเลือกรอบ 30 นาทีหรือ 1 ชั่วโมงตามที่ระบบมีให้เลือก\n"
    elif _has(q, "ps5", "playstation", "เพลย์"):
        service_hint = "ถ้าต้องการจอง PlayStation 5 ให้เลือกบริการ PlayStation 5 และเลือกรอบเวลาที่ต้องการ\n"
    elif _has(q, "nintendo", "switch", "สวิตช์", "สวิทช์", "นินเทนโด"):
        service_hint = "ถ้าต้องการจอง Nintendo Switch ให้เลือกบริการ Nintendo Switch และเลือกจำนวนผู้เล่น/รอบเวลาตามที่ระบบมีให้เลือก\n"
    elif _has(q, "cockpit", "ค็อกพิท", "คอกพิท", "พวงมาลัย"):
        service_hint = "ถ้าต้องการจอง Cockpit ให้เลือกบริการ Cockpit และเลือกรอบเวลาที่ต้องการ\n"
    elif _has(q, "pc", "คอม", "คอมพิวเตอร์"):
        service_hint = "ถ้าต้องการจอง PC ให้เลือกเครื่อง PC/บริการ PC ที่ต้องการและเลือกรอบเวลา\n"

    answer = (
        "จองคิวเล่นเกม/ใช้อุปกรณ์ได้ผ่านระบบจองออนไลน์ครับ\n"
        f"{service_hint}"
        "ขั้นตอนโดยสรุปคือ 1) เลือกบริการหรือโซนที่ต้องการใช้ 2) เลือกวันและรอบเวลา "
        "3) กรอก Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล และเบอร์โทรศัพท์ "
        "4) ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง 5) แนบสลิปและยืนยันการจอง\n"
        "ต้องจองล่วงหน้าอย่างน้อย 1 ชั่วโมง และหลังจองต้องชำระเงินภายใน 10 นาทีครับ\n"
        f"แหล่งข้อมูล: {RESERVATION_URL}"
    )
    return _answer(answer, "reservation", "booking_howto_fast_path", start, 0.97)


def _booking_specific_answer(q: str, start: float) -> FastAnswer | None:
    if _has_strong_game_catalog_terms(q) or _looks_like_game_total_count(q):
        return None
    if _has(q, "จ่ายเงินผ่าน", "ชำระเงินผ่าน", "ช่องทางชำระ", "ช่องทางการชำระ", "ช่องทางไหน", "โอนเงิน", "เลขบัญชี", "บัญชีธนาคาร", "ชื่อบัญชี", "ธนาคารอะไร", "บัญชีไหน"):
        return _answer(
            "ชำระเงินโดยโอนเข้าบัญชีธนาคารไทยพาณิชย์ (Siam Commercial Bank) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และแนบสลิปการโอนเงินครับ\n"
            f"แหล่งข้อมูล: {RESERVATION_URL}",
            "reservation",
            "payment_fast_path",
            start,
            0.97,
        )

    if _has(q, "จองแล้วลืมเช็คอิน", "ลืมเช็คอิน", "ลืมเชคอิน", "ไปถึงช้า", "ช้ากว่าเวลาจอง"):
        return _answer(
            "ถ้าลืมเช็คอินหรือไปถึงช้ากว่าเวลาเริ่มรอบ มีความเสี่ยงที่การจองจะถูกยกเลิกครับ\n"
            "• ผู้ใช้งานต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง\n"
            "• สามารถเช็คอินได้ล่วงหน้าสูงสุด 30 นาที\n"
            "• หากไม่เช็คอินก่อนเริ่มรอบ ระบบอาจยกเลิกการจองและไม่มีการคืนเงิน\n"
            f"แหล่งข้อมูล: {RESERVATION_URL}",
            "reservation",
            "booking_late_checkin_fast_path",
            start,
            0.96,
        )

    if _has(q, "เปลี่ยนคนเล่น", "เปลี่ยนผู้เล่น", "เปลี่ยนคนใช้", "โอนให้เพื่อน", "ให้เพื่อนเล่นแทน"):
        return _answer(
            "จองแล้วไม่ควรเปลี่ยนคนเล่นหรือโอนสิทธิ์ให้ผู้อื่นครับ\n"
            "• ข้อมูลการจองผูกกับข้อมูลผู้ใช้บริการที่กรอกไว้\n"
            "• หากต้องแก้ไขข้อมูล ควรยกเลิกการจองเดิมตามเงื่อนไขแล้วจองใหม่\n"
            f"แหล่งข้อมูล: {RESERVATION_URL}",
            "reservation",
            "booking_transfer_fast_path",
            start,
            0.95,
        )

    if _has(q, "ต้องชำระเงินก่อนเล่น", "ชำระเงินก่อนเล่น", "จ่ายเงินก่อนเล่น", "ต้องจ่ายก่อนเล่น"):
        return _answer(
            "ต้องชำระเงินก่อนเข้าใช้บริการครับ\n"
            "• หลังจองต้องชำระเงินภายใน 10 นาที\n"
            "• ชำระโดยโอนเข้าบัญชีที่ระบบแจ้ง แล้วแนบสลิปเพื่อยืนยันการจอง\n"
            f"แหล่งข้อมูล: {RESERVATION_URL}",
            "reservation",
            "booking_payment_before_play_fast_path",
            start,
            0.96,
        )

    if _has(q, "จองแล้วต้องตรวจสอบอีเมล", "ตรวจสอบอีเมล", "เช็คอีเมล", "เช็คเมล") and _has(q, "จอง", "booking"):
        return _answer(
            "ควรตรวจสอบอีเมลที่ใช้จองครับ\n"
            "• ใช้ติดตามข้อมูล/หลักฐานการจองและการติดต่อจากระบบหรือเจ้าหน้าที่\n"
            "• หากต้องยกเลิกหรือแก้ไขการจอง ระบบมีขั้นตอนที่เกี่ยวข้องกับอีเมลและควรทำล่วงหน้าอย่างน้อย 1 ชั่วโมง\n"
            f"แหล่งข้อมูล: {RESERVATION_URL}",
            "reservation",
            "booking_email_check_fast_path",
            start,
            0.94,
        )

    if _has(q, "vr", "วีอาร์", "แว่น"):
        if _has(q, "1 ชั่วโมง", "หนึ่งชั่วโมง", "60 นาที", "30 นาที", "ต่างกัน") and _has(q, "ต่างกัน", "เทียบ", "กับ"):
            return _answer(
                "VR มีรอบ 30 นาทีและ 1 ชั่วโมงครับ\n"
                "• 30 นาที: เหมาะกับการลองเล่นครั้งแรกหรือเล่นสั้น ๆ\n"
                "• 1 ชั่วโมง: เหมาะกับเล่นนานขึ้นหรือเล่นหลายคนในรอบเดียว\n"
                "• ทั้งสองแบบให้เลือกบริการ VR Station และเลือกรอบเวลาที่ว่างในระบบจอง\n"
                f"แหล่งข้อมูล: {RESERVATION_URL}",
                "reservation",
                "booking_vr_duration_fast_path",
                start,
                0.97,
            )
        if _has(q, "ครึ่งชั่วโมง", "30 นาที", "สามสิบ") and _has(q, "จอง", "ได้ไหม"):
            return _answer(
                "จอง VR ครึ่งชั่วโมงได้ครับ\n"
                "• ในระบบจองมี VR Station แบบ 30 นาที และแบบ 1 ชั่วโมง\n"
                "• ถ้าเป็นครั้งแรกหรืออยากลองสั้น ๆ แนะนำเริ่มที่ 30 นาที\n"
                "• ถ้าต้องการเล่นนานขึ้นหรือเล่นหลายคน ค่อยเลือก 1 ชั่วโมงตามรอบที่ว่าง\n"
                f"แหล่งข้อมูล: {RESERVATION_URL}",
                "reservation",
                "booking_vr_duration_fast_path",
                start,
                0.97,
            )
        if _has(q, "ครั้งแรก", "มือใหม่", "ลอง"):
            return _answer(
                "ถ้าอยากลอง VR ครั้งแรก แนะนำจอง VR Station แบบ 30 นาทีก่อนครับ\n"
                "• เลือกบริการ VR Station ในระบบจอง\n"
                "• เลือกรอบ 30 นาทีหรือ 1 ชั่วโมงตามที่ต้องการ\n"
                "• ก่อนเล่นควรให้เจ้าหน้าที่ช่วยแนะนำการใส่แว่นและคอนโทรลเลอร์\n"
                f"แหล่งข้อมูล: {RESERVATION_URL}",
                "reservation",
                "booking_vr_first_time_fast_path",
                start,
                0.96,
            )

    if _has(q, "playstation", "ps5", "เพลย์") and _has(q, "รอบละกี่นาที", "กี่นาที", "ใช้เวลา"):
        return _answer(
            "PlayStation 5 ในระบบจองเป็นรอบ 60 นาทีครับ\n"
            "• มี PlayStation 5 #1 และ PlayStation 5 #2 สำหรับ 1-2 คนต่อรอบ\n"
            f"แหล่งข้อมูล: {RESERVATION_URL}",
            "reservation",
            "booking_ps5_duration_fast_path",
            start,
            0.96,
        )

    if _has(q, "nintendo", "switch", "นินเทนโด", "สวิตช์", "สวิทช์") and _has(q, "4 คน", "สี่คน", "จำนวนผู้เล่น", "กี่คน"):
        return _answer(
            "Nintendo Switch ต้องเลือกบริการตามจำนวนผู้เล่นครับ\n"
            "• ถ้าเล่น 1-2 คน ให้เลือก Nintendo Switch แบบ 1-2 Persons\n"
            "• ถ้าเล่น 3-4 คน ให้เลือก Nintendo Switch แบบ 3-4 Persons\n"
            "• จากนั้นเลือกวัน/รอบเวลา กรอกข้อมูล ชำระเงิน และแนบสลิปตามขั้นตอนจอง\n"
            f"แหล่งข้อมูล: {RESERVATION_URL}",
            "reservation",
            "booking_nintendo_players_fast_path",
            start,
            0.96,
        )
    if _has(q, "nintendo", "switch", "นินเทนโด", "สวิตช์", "สวิทช์") and _has(q, "ต้องเลือกอะไร", "เลือกอะไรบ้าง", "จอง"):
        return _answer(
            "จอง Nintendo Switch ต้องเลือกบริการ จำนวนผู้เล่น วัน และรอบเวลาครับ\n"
            "• เลือก Nintendo Switch แบบ 1-2 Persons หรือ 3-4 Persons ตามจำนวนคนเล่น\n"
            "• เลือกวันและรอบเวลาที่ต้องการ\n"
            "• กรอกข้อมูลผู้ใช้บริการ ชำระเงิน และแนบสลิปเพื่อยืนยันการจอง\n"
            f"แหล่งข้อมูล: {RESERVATION_URL}",
            "reservation",
            "booking_nintendo_choice_fast_path",
            start,
            0.96,
        )

    if _has(q, "ระบบจองไม่ขึ้น", "จองไม่ขึ้น", "เว็บจองไม่ขึ้น", "ระบบล่ม", "เข้าเว็บจองไม่ได้"):
        return _answer(
            "ถ้าระบบจองไม่ขึ้น ให้ติดต่อเจ้าหน้าที่หรือช่องทางติดต่อของ PSU Esports Studio - Phuket ก่อนครับ\n"
            "• อย่าชำระเงินเองถ้ายังไม่มีรายการจองในระบบ\n"
            "• ถ้าต้องการใช้บริการวันเดียวกัน ยังต้องยึดเงื่อนไขจองล่วงหน้าอย่างน้อย 1 ชั่วโมงและรอบที่ว่าง\n"
            f"แหล่งข้อมูล: {RESERVATION_URL}",
            "reservation",
            "booking_support_fast_path",
            start,
            0.95,
        )

    if _has(q, "เล่นวันนี้", "วันนี้") and _has(q, "จอง", "ทันที", "ได้ไหม"):
        return _answer(
            "ถ้าอยากเล่นวันนี้ทำได้เมื่อยังมีรอบว่างและจองล่วงหน้าได้ทันอย่างน้อย 1 ชั่วโมงครับ\n"
            "• ต้องจองผ่านระบบออนไลน์ก่อนเข้าใช้บริการ\n"
            "• หลังจองต้องชำระเงินภายใน 10 นาที\n"
            "• ถ้ารอบใกล้เกินไปหรือไม่มีรอบว่าง ระบบอาจจองไม่ได้\n"
            f"แหล่งข้อมูล: {RESERVATION_URL}",
            "reservation",
            "booking_same_day_fast_path",
            start,
            0.96,
        )

    if _has(q, "ขับรถ", "พวงมาลัย", "gran turismo") and _has(q, "จอง", "ต้องจองอะไร", "เลือกอะไร"):
        return _answer(
            "ถ้าอยากเล่นเกมขับรถ ให้จอง Cockpit Zone / Cockpit ครับ\n"
            "• โซนนี้มี Racezone Full Cockpit V3, Logitech G923 TRUEFORCE Racing Wheel และ Driving Force Shifter\n"
            "• เกมที่ยืนยันได้คือ Gran Turismo 7\n"
            f"แหล่งข้อมูล: {RESERVATION_URL}",
            "reservation",
            "booking_cockpit_fast_path",
            start,
            0.96,
        )

    if _has(q, "สลิปผิด", "แนบสลิปผิด", "สลิปไม่ถูก", "อัปสลิปผิด", "อัพสลิปผิด"):
        return _answer(
            "ถ้าแนบสลิปผิด ให้ติดต่อเจ้าหน้าที่และทำตามขั้นตอนแก้ไข/ยกเลิกการจองครับ\n"
            "• เมื่อกดจองแล้วระบบไม่ให้แก้ไขข้อมูลโดยตรง\n"
            "• หากต้องแก้ไข ควรยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ตามขั้นตอน\n"
            f"แหล่งข้อมูล: {RESERVATION_URL}",
            "reservation",
            "booking_slip_fix_fast_path",
            start,
            0.95,
        )

    return None


def answer_static_domain(query: str, start: float) -> FastAnswer | None:
    q = normalize_text(query)

    if _looks_like_chatbot_greeting_query(q):
        return _chatbot_greeting_answer(start)

    if _has(
        q,
        "นายเป็นใคร", "คุณเป็นใคร", "แกเป็นใคร", "เธอเป็นใคร", "ตัวเองเป็นใคร",
        "เป็น ai อะไร", "เป็น ai จริงหรือเปล่า", "เป็น ai ไหม", "เป็นคนแอบพิมพ์", "คนแอบพิมพ์",
        "เป็น model อะไร", "เป็นโมเดลอะไร", "ชื่ออะไร",
        "ทำอะไรได้บ้าง", "ทำไรได้บ้าง", "ช่วยอะไรได้บ้าง", "ช่วยไรได้บ้าง", "ตอบอะไรได้บ้าง", "ตอบไรได้บ้าง", "ถามอะไรได้บ้าง", "ถามไรได้บ้าง",
        "แชทบอทนี้", "chatbot นี้", "bot นี้", "บอทนี้", "assistant นี้",
        "who are you", "what are you", "what can you do",
    ):
        return _chatbot_identity_answer(start)

    if _has(q, *UNKNOWN_TERMS):
        return _no_answer(start)

    booking_limit = _booking_session_limit_answer(q, start)
    if booking_limit is not None:
        return booking_limit

    booking_specific = _booking_specific_answer(q, start)
    if booking_specific is not None:
        return booking_specific

    booking_howto = _booking_howto_answer(q, start)
    if booking_howto is not None:
        return booking_howto

    members_answer = answer_members(q, start)
    if members_answer is not None:
        return members_answer

    popularity_answer = _game_popularity_no_answer(q, start)
    if popularity_answer is not None:
        return popularity_answer

    if _has(q, "spacewar", "เริ่มครั้งแรก"):
        return _answer("ประวัติอีสปอร์ตเริ่มจากการแข่งขันเกม Spacewar ที่ Stanford University ในปี 1972", "knowledge", "knowledge_fast_path", start)
    if _has(q, "จองแล้วไม่จ่าย", "เช็คอินช้า", "เชคอินช้า"):
        return _answer("ถ้าจองแล้วไม่ชำระภายใน 10 นาที ระบบจะยกเลิกและต้องจองใหม่ หากเช็คอินไม่ทันก่อนเริ่มรอบ การจองจะถูกยกเลิกและไม่มีการคืนเงิน", "reservation", "mixed_reservation_fast", start)
    if _has(q, "จองล่วงหน้า") and _has(q, "เช็คอิน", "เชคอิน") and _has(q, "ยกเลิก"):
        return _answer("สรุป: ต้องจองล่วงหน้าอย่างน้อย 1 ชั่วโมง, เช็คอินได้ล่วงหน้าสูงสุด 30 นาที และหากต้องยกเลิกหรือแก้ไขต้องแจ้งล่วงหน้าอย่างน้อย 1 ชั่วโมง", "reservation", "mixed_reservation_fast", start)
    if _has(q, "กี่ session", "กี่ sessions") and _has(q, "จ่ายภายใน", "กี่นาที"):
        return _answer("การจอง 1 ครั้งจองได้สูงสุด 3 Sessions และต้องชำระเงินภายใน 10 นาทีหลังจอง", "reservation", "mixed_reservation_fast", start)
    if _has(q, "กรอกข้อมูลผิด", "แก้เวลา", "แก้ไข", "จองผิดเวลา", "ยกเลิกแล้วจองใหม่", "สลิปเดิม"):
        return _answer("เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปการโอนเงินเดิม", "reservation", "booking_fast_path", start)
    if _has(q, "ยกเลิกการจอง", "ยกเลิก booking", "cancel booking", "cancel reservation") or (_has(q, "ยกเลิก") and _has(q, "จอง", "booking", "reservation")):
        return _answer(
            "การยกเลิกการจองต้องทำล่วงหน้าอย่างน้อย 1 ชั่วโมงครับ หากต้องการแก้ไขข้อมูลหรือเวลาใช้งาน ต้องยกเลิกการจองเดิมก่อนแล้วจองใหม่ตามขั้นตอนของระบบ\n"
            f"แหล่งข้อมูล: {RESERVATION_URL}",
            "reservation",
            "booking_cancel_fast_path",
            start,
            0.96,
        )
    if _has(q, "จ่ายเงินผ่าน", "ชำระเงินผ่าน", "ช่องทางชำระ", "ช่องทางการชำระ", "ช่องทางไหน", "โอนเงิน", "เลขบัญชี", "ธนาคาร", "ชื่อบัญชี", "บัญชีไหน"):
        return _answer("ชำระเงินโดยโอนเข้าบัญชีธนาคารไทยพาณิชย์ (Siam Commercial Bank) ชื่อบัญชี PSU Esports Studio - Phuket เลขบัญชี 795-276244-1 และแนบสลิปการโอนเงิน", "reservation", "payment_fast_path", start)
    if _has(q, "หลังจอง", "ไม่จ่ายใน 10", "ลืมจ่าย", "payment timeout", "ชำระเงินหลัง booking"):
        return _answer("หลังจองต้องชำระเงินภายใน 10 นาที หากไม่ชำระ ระบบจะยกเลิกการจอง และถ้าต้องการใช้บริการต้องจองใหม่", "reservation", "payment_fast_path", start)
    booking_step = _booking_step_fast_answer(q, start)
    if booking_step is not None:
        return booking_step
    if _has(q, "ไม่มีบัตรนักศึกษา", "ไม่มีบัตร") and _has(q, "จอง", "ตอนจอง", "booking"):
        return _answer(
            "ตอนจองไม่จำเป็นต้องมีเฉพาะบัตรนักศึกษาอย่างเดียวครับ ระบบให้กรอก Student ID/Staff ID/National ID พร้อมชื่อ นามสกุล อีเมล และเบอร์โทรศัพท์\n"
            "ถ้าไม่มีบัตรนักศึกษา ให้ใช้ National ID/บัตรประชาชนตามข้อมูลที่ระบบจองรองรับ และตอนเช็คอินควรนำบัตรที่ตรงกับข้อมูลจองไปแสดง\n"
            f"แหล่งข้อมูล: {RESERVATION_URL}",
            "reservation",
            "booking_identity_fast_path",
            start,
            0.96,
        )
    if _has(q, "สอนจอง", "วิธีจอง", "จองยังไง", "จองอย่างไร", "ขั้นตอนการจอง", "ช่วยสรุปขั้นตอนการจอง", "จองได้ยังไง", "จองทำยังไง"):
        return _answer("ได้ครับ ขั้นตอนจองโดยสรุปคือ 1) เลือกบริการและรอบเวลาที่ต้องการ 2) กรอก Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล และเบอร์โทรศัพท์ 3) ชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง 4) แนบสลิปและยืนยันการจอง โดยต้องจองล่วงหน้าอย่างน้อย 1 ชั่วโมง และหลังจองต้องชำระเงินภายใน 10 นาที", "reservation", "booking_fast_path", start)
    if _has(q, "จองต้องล่วงหน้า", "จองต้อง", "จองก่อน", "book ล่วงหน้า", "walk in"):
        return _answer("ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง", "reservation", "booking_fast_path", start)
    if (_has(q, "จอง", "booking", "one booking") and _has(q, "session", "sessions", "รอบ", "4 sessions", "สามรอบ")):
        return _answer("การจอง 1 ครั้งสามารถจองได้สูงสุด 3 Sessions", "reservation", "booking_fast_path", start)
    if _has(q, "โอนให้เพื่อน", "ใช้ booking แทน", "transfer booking", "จองแทน"):
        return _answer("ไม่สามารถโอนสิทธิ์การจองให้ผู้อื่นได้", "reservation", "booking_fast_path", start)
    if _has(q, "บัตร") and _has(q, "เช็คอิน", "เชคอิน", "checkin"):
        return _answer("ตอนเช็คอินต้องนำบัตรประจำตัวนักศึกษา บัตรประจำตัวบุคลากร หรือบัตรประชาชนมาแสดง", "reservation", "checkin_fast_path", start)
    if _has(q, "เช็คอิน", "เชคอิน", "checkin") and _has(q, "กี่นาที", "ล่วงหน้า", "ก่อน", "เร็วสุด", "1800"):
        return _answer("เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง", "reservation", "checkin_fast_path", start)

    if _has(q, "จองล่วงหน้า", "เช็คอิน", "เชคอิน", "ยกเลิกแบบสั้น"):
        return _answer("สรุป: ต้องจองล่วงหน้าอย่างน้อย 1 ชั่วโมง, เช็คอินได้ล่วงหน้าสูงสุด 30 นาที และหากต้องยกเลิกหรือแก้ไขต้องแจ้งล่วงหน้าอย่างน้อย 1 ชั่วโมง", "reservation", "mixed_reservation_fast", start)
    if _has(q, "กี่ session", "กี่รอบ") and _has(q, "จ่าย", "นาที"):
        return _answer("การจอง 1 ครั้งจองได้สูงสุด 3 Sessions และต้องชำระเงินภายใน 10 นาทีหลังจอง", "reservation", "mixed_reservation_fast", start)
    if _has(q, "กรอกข้อมูล", "แนบสลิป"):
        return _answer("ตอนจองต้องกรอก Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล เบอร์โทรศัพท์ และชำระโดยโอนเงินพร้อมแนบสลิป", "reservation", "mixed_reservation_fast", start)
    if _has(q, "จองผิดเวลา", "แก้เวลา", "แก้ไข"):
        return _answer("หลังจองแล้วแก้ไขข้อมูลไม่ได้ ต้องยกเลิกผ่านอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปเดิม", "reservation", "mixed_reservation_fast", start)

    if (
        _has(q, "กติกาในศูนย์", "กฎในศูนย์", "กติกาการใช้บริการ", "กฎการใช้บริการ", "ข้อห้ามในศูนย์", "ในศูนย์ห้าม", "ศูนย์ห้าม", "ระเบียบในศูนย์", "กฎของศูนย์")
        or (_has(q, "กติกา", "กฎ", "ข้อห้าม", "ห้าม", "ระเบียบ") and _has(q, "ศูนย์", "studio", "ใช้บริการ", "มีอะไรบ้าง", "อะไรบ้าง"))
    ):
        return _answer(
            "กติกาการใช้บริการในศูนย์โดยสรุปครับ\n"
            "•    ฝากสัมภาระก่อนเข้าใช้บริการ และศูนย์ไม่รับผิดชอบทรัพย์สินสูญหาย\n"
            "•    รับประทานอาหารและเครื่องดื่มได้เฉพาะพื้นที่ที่กำหนด\n"
            "•    คืนอุปกรณ์และแผ่นเกมหลังใช้งานเสร็จ\n"
            "•    งดส่งเสียงดังเกินควร และห้ามพูดจาดูหมิ่นหรือเสียดสีผู้อื่น\n"
            "•    ห้ามเคลื่อนย้ายอุปกรณ์/สิ่งของโดยไม่ได้รับอนุญาต และห้ามใช้ปลั๊กไฟส่วนตัวโดยไม่ได้รับอนุญาต\n"
            "•    ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ ทะเลาะวิวาท หรือเล่นการพนัน\n"
            "•    หากทำอุปกรณ์เสียหาย อาจมีค่าปรับ/ค่าซ่อมหรือชดเชยตามระดับความเสียหาย",
            "reservation",
            "studio_rules_overview_fast_path",
            start,
            0.94,
        )

    if _has(q, "กินข้าวเสียงดัง"):
        return _answer("เกี่ยวกับกฎอาหารและเสียงดัง: อาหาร/เครื่องดื่มทำได้เฉพาะพื้นที่ที่กำหนด, กรุณางดส่งเสียงดัง และหากทำอุปกรณ์เสียหายต้องรับผิดชอบค่าปรับ", "reservation", "mixed_rules_fast", start)
    if _has(q, "เมาส์", "mouse", "คีย์บอร์ด", "keyboard", "จอย", "หูฟัง") and _has(q, "พัง", "เสีย", "เสียหาย", "ค่าปรับ", "ชดเชย", "ค่าซ่อม"):
        return _answer("ต้องรับผิดชอบค่าปรับ/ค่าซ่อมครับ หากทำเมาส์หรืออุปกรณ์ของศูนย์เสียหาย โดยข้อมูลกฎที่มีระบุว่า ความเสียหายเล็กน้อยคิด 100-500 บาท และความเสียหายปานกลางคิด 500-2,000 บาทหรือตามราคาซ่อมจริง หากเสียหายร้ายแรงอาจต้องชดเชยเต็มจำนวนตามราคากลาง", "penalty", "penalty_fast_path", start)
    if _has(q, "ของหาย", "อุปกรณ์เปียก"):
        return _answer("ทรัพย์สินสูญหายศูนย์ไม่รับผิดชอบ แต่ถ้าผู้ใช้ทำอุปกรณ์เสียหายหรือเปียก ผู้ใช้ต้องรับผิดชอบค่าปรับ/ค่าซ่อม", "reservation", "mixed_rules_fast", start)
    if _has(q, "สูบบุหรี่", "แอลกอฮอล์", "มีด", "พนัน", "ปลั๊ก", "ย้ายอุปกรณ์"):
        return _answer("ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต", "reservation", "rules_fast_path", start)
    if _has(q, "แผ่นเกม", "ไม่คืน"):
        return _answer("อุปกรณ์และแผ่นเกมที่เบิกไปใช้งานต้องคืนหลังจากใช้งานเสร็จ", "reservation", "rules_fast_path", start)
    if _has(q, "ปัญหาเครื่อง", "พบปัญหา"):
        return _answer("หากพบปัญหาการใช้งานหรือเครื่องมีปัญหา โปรดแจ้งเจ้าหน้าที่ทันที", "reservation", "rules_fast_path", start)

    if _has(q, "ฝากกระเป๋า", "ฝากสัมภาระ"):
        return _answer("กรุณาฝากสัมภาระก่อนเข้าใช้บริการ", "reservation", "rules_fast_path", start)
    if _has(q, "ขนม", "กินน้ำ", "อาหาร", "เครื่องดื่ม"):
        return _answer("อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น", "reservation", "rules_fast_path", start)
    if _has(q, "เสียงดัง", "เสียดสี"):
        return _answer("กรุณางดส่งเสียงดังเกินควร และห้ามพูดจาดูหมิ่นหรือเสียดสีผู้อื่น", "reservation", "rules_fast_path", start)
    if _has(q, "ทิ้งขยะ"):
        return _answer("ห้ามทิ้งขยะหรือสิ่งของใด ๆ ในบริเวณที่ไม่ได้กำหนด", "reservation", "rules_fast_path", start)
    if _has(q, "อุปกรณ์เสียหาย", "อุปกรณ์พัง", "รอยขีดข่วน", "เบาะขาด", "หูฟังสายขาด"):
        return _answer("ผู้ใช้ต้องรับผิดชอบค่าปรับหากทำอุปกรณ์เสียหาย: ความเสียหายเล็กน้อย 100-500 บาท และปานกลาง 500-2,000 บาทหรือตามราคาซ่อมจริง", "penalty", "penalty_fast_path", start)
    if _has(q, "จอแตก", "คอมพัง"):
        return _answer("กรณีเสียหายร้ายแรง เช่น จอแตกหรือคอมพัง ต้องชดเชยราคาทรัพย์สินเต็มจำนวนตามราคากลาง", "reservation", "penalty_fast_path", start)
    if _has(q, "ระงับสิทธิ์", "แบน", "ถาวร", "อุทธรณ์", "ประวัติ"):
        return _answer("หากละเมิดกฎอาจถูกระงับสิทธิ์ชั่วคราว 1-7 วันหรือถาวร มีการบันทึกประวัติ และสามารถอุทธรณ์ได้ภายใน 7 วัน", "reservation", "penalty_fast_path", start)

    if _has(q, "ศูนย์นี้", "studio phuket", "ก่อตั้ง", "หน่วยงาน", "mission"):
        return _answer("PSU Esports Studio - Phuket เป็นศูนย์การเรียนรู้ด้านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์ ดำเนินการโดยวิทยาลัยการคอมพิวเตอร์ เพื่อยกระดับการศึกษาและความเป็นเลิศด้านอีสปอร์ต", "home", "overview_fast_path", start)
    if _has(q, "อยู่ตรงไหน", "ที่ตั้ง", "email", "facebook", "เฟส", "เบอร์โทร"):
        return _answer("PSU Esports Studio - Phuket อยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต อีเมล psuesportspkt@gmail.com Facebook https://www.facebook.com/psuesportsphuket เบอร์โทร +66 7627 6004 และ +66 7627 6045", "contact", "contact_fast_path", start)

    if _has(q, "อีสปอร์ตคือ"):
        return _answer("อีสปอร์ตคือกีฬาอิเล็กทรอนิกส์ เป็นการแข่งขันวิดีโอเกมที่ใช้ทักษะและความสามารถ", "knowledge", "knowledge_fast_path", start)
    if _has(q, "เริ่มครั้งแรก", "spacewar"):
        return _answer("ประวัติอีสปอร์ตเริ่มจากการแข่งขันเกม Spacewar ที่ Stanford University ในปี 1972", "knowledge", "knowledge_fast_path", start)
    if _has(q, "moba", "โมบา", "โมบ้า", "โมบะ", "multiplayer online battle arena", "เกมตีป้อม"):
        if _has(q, "ยอดนิยม", "เกมไหน", "อะไรบ้าง", "รายชื่อ", "นิยม"):
            return _answer(
                f"{_popular_games_by_genre_summary(['moba'], 'เกม Multiplayer Online Battle Arena (MOBA) ยอดนิยมที่หน้า Knowledge ระบุ:')}\n"
                f"แหล่งข้อมูล: {POPULAR_GAMES_KNOWLEDGE_URL}",
                "knowledge_popular_games",
                "knowledge_moba_popular_games_fast_path",
                start,
                0.96,
            )
        return _answer(
            "MOBA หรือ Multiplayer Online Battle Arena เป็นเกมที่ผู้เล่นสองทีมต่อสู้กันเชิงกลยุทธ์ โดยทั่วไปทีมละ 5 คน เป้าหมายคือทำลายฐานฝ่ายตรงข้ามผ่านการทำงานเป็นทีม การประสานงาน และการใช้ตัวละครที่มีความสามารถเฉพาะตัว\n"
            f"แหล่งข้อมูล: {ESPORTS_GAME_TYPES_URL}",
            "knowledge_game_types",
            "knowledge_moba_definition_fast_path",
            start,
            0.96,
        )
    if _has(q, "ประเภทเกม", "แนวเกม") and _has(q, "อีสปอร์ต", "แข่งขัน", "ยอดนิยม"):
        return _answer(
            f"{_esports_game_types_summary()}\n"
            f"แหล่งข้อมูล: {ESPORTS_GAME_TYPES_URL}",
            "knowledge_game_types",
            "knowledge_esports_game_types_fast_path",
            start,
            0.96,
        )
    if _has(q, "เกมยอดนิยม", "เกมที่นิยม", "เกมนิยม") and _has(q, "ปัจจุบัน", "อะไรบ้าง", "แนว", "คือเกมอะไร", "เกมอะไร"):
        return _answer(
            f"{_popular_games_by_genre_summary()}\n"
            f"แหล่งข้อมูล: {POPULAR_GAMES_KNOWLEDGE_URL}",
            "knowledge_popular_games",
            "knowledge_popular_games_by_genre_fast_path",
            start,
            0.96,
        )
    if _has(q, "อาชีพ"):
        return _answer("อาชีพในวงการอีสปอร์ตมีนักกีฬาอีสปอร์ต โค้ช ผู้จัดการทีม นักพากย์ ผู้จัดการแข่งขัน นักวิเคราะห์ และสายสนับสนุนอื่น ๆ", "knowledge", "knowledge_fast_path", start)
    if _has(q, "overcooked 2") and _has(q, "ฝึก", "ทักษะ"):
        return _answer("Overcooked 2 ช่วยฝึกการทำงานเป็นทีม การสื่อสาร การวางแผน และการจัดการสถานการณ์กดดัน", "knowledge", "knowledge_fast_path", start)
    if _has(q, "mario kart") and _has(q, "ฝึก", "ทักษะ"):
        return _answer("Mario Kart 8 Deluxe ช่วยฝึกไหวพริบ การตัดสินใจ และการตอบสนองระหว่างเล่น", "knowledge", "knowledge_fast_path", start)

    if _has(q, "25 เมษายน"):
        return _answer("วันที่ 25 เมษายน 2569 เป็นข่าว PSU Phuket CS 2 2026", "news", "news_fast_path", start)
    if _has(q, "valorant 2026"):
        return _answer("PSU Phuket VALORANT 2026 จัดวันที่ 21 กุมภาพันธ์ 2569", "news", "news_fast_path", start)
    if _has(q, "surat smash"):
        return _answer("SURAT SMASH ส่งตัวแทน 4 คน", "news", "news_fast_path", start)
    if _has(q, "นักศึกษาชาวจีน"):
        return _answer("ข่าวระบุว่านักศึกษาชาวจีนมี 11 คน", "news", "news_fast_path", start)
    if _has(q, "game on"):
        return _answer("กิจกรรม GAME ON จัดให้นักเรียน ม.3 โรงเรียนท้ายเหมืองวิทยา", "news", "news_fast_path", start)

    if _has(q, "อธิการบดี"):
        return _answer("ผศ.ดร.นิวัติ แก้วประดับ เป็นอธิการบดี มหาวิทยาลัยสงขลานครินทร์ (PSU)", "members", "members_fast_path", start)
    if _has(q, "คณบดี"):
        return _answer("รศ.ดร.อซีส นันทอมรพงศ์ เป็นคณบดี วิทยาลัยการคอมพิวเตอร์ PSU", "members", "members_fast_path", start)
    if _has(q, "ผู้จัดการศูนย์"):
        return _answer("นายชนะชัย สิริพันธ์วราภรณ์ เป็นผู้จัดการ PSU Esports Studio - Phuket", "members", "members_fast_path", start)
    if _has(q, "ประธาน psu", "ประธาน psu phuket esports club"):
        return _answer("นายษุภากรณ์ จิราจินดากุล เป็นประธาน PSU Phuket Esports Club - PSU Phuket", "members", "members_fast_path", start)
    if _has(q, "gallery"):
        return _answer("หน้า Gallery ของ PSU Esports Studio - Phuket มีหมวดภาพ Nintendo Switch และ PlayStation 5", "members", "members_fast_path", start)

    return None


class FastAnswerEngine:
    def __init__(self) -> None:
        self.matcher = RuleMatcher.default()

    def answer(self, question: str) -> FastAnswer:
        start = time.perf_counter()

        for handler in (
            answer_static_domain,
            answer_price,
            answer_schedule,
            answer_equipment,
            answer_games,
        ):
            result = handler(question, start)
            if result is not None:
                return result

        rule = self.matcher.match(question)
        if rule is not None:
            return FastAnswer(
                answer=str(rule.get("answer", "")),
                hits=HITS["reservation"],
                mode="rule_fast_path",
                elapsed=round(time.perf_counter() - start, 4),
                confidence=0.90,
            )

        return _no_answer(start)


_ENGINE: FastAnswerEngine | None = None


def get_engine() -> FastAnswerEngine:
    global _ENGINE
    if _ENGINE is None:
        _ENGINE = FastAnswerEngine()
    return _ENGINE


def answer_question_fast(question: str) -> tuple[str, list[dict], float, str]:
    result = get_engine().answer(question)
    return result.answer, result.hits, result.elapsed, result.mode
