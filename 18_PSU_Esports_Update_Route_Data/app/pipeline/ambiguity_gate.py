from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any

from app.calculator.service_fee import GROUP_ORDER, SERVICE_FEES
from app.core.normalization import SERVICE_ALIASES, detect_from_aliases, normalize_text
from app.core.source_registry import (
    PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID,
    SERVICE_FEE_IMAGE_2026_ID,
    make_source_hits,
)
from app.pipeline.entity_resolver import (
    EntityResolution,
    operation_allows_family_list,
    operation_requires_exact_game,
    resolve_game_entity,
)
from app.pipeline.game_title_correction import game_alias_entries
from app.pipeline.schemas import EntityBundle, PipelineRoute, PipelineTrace, UniversalIntent


ROOT = Path(__file__).resolve().parents[2]
CURATED_DIR = ROOT / "data" / "curated"
HOME_URL = "https://esports.phuket.psu.ac.th/home"
OUR_GAMES_URL = "https://esports.phuket.psu.ac.th/Services/our-games"
RESERVATION_URL = "https://esports.computing.psu.ac.th/"


@dataclass(frozen=True)
class AmbiguityGateResult:
    action: str
    confidence: float
    reason: str
    flags: tuple[str, ...] = ()
    answer: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)
    hits: list[dict[str, Any]] = field(default_factory=list)

    @property
    def allows_answer(self) -> bool:
        return self.action == "allow"

    def trace(self) -> PipelineTrace:
        return PipelineTrace(
            "ambiguity_gate",
            self.action,
            self.confidence,
            self.reason,
            {"flags": list(self.flags), **self.metadata},
        )


@dataclass(frozen=True)
class IntentCandidateScore:
    domain: str
    operation: str
    score: float
    reasons: tuple[str, ...] = ()


_PRICE_TERMS = ("ราคา", "กี่บาท", "ค่าบริการ", "เท่าไหร่", "เท่าไร", "จ่าย", "เสีย")
_BOOKING_TERMS = ("จอง", "booking", "book", "เข้าใช้", "ใช้บริการ", "เข้าเล่น", "จะเล่นต้องทำไง", "เล่นต้องทำไง")
_CANCEL_TERMS = ("ยกเลิก", "คืนเงิน", "cancel")
_GAME_LIST_TERMS = ("มีเกม", "เกมอะไร", "รายชื่อเกม", "รายการเกม", "เกมทั้งหมด", "กี่เกม")
_GAME_DETAIL_TERMS = ("รายละเอียดเกม", "ข้อมูลเกม", "อยู่โซนไหน", "อยู่เครื่องไหน", "เครื่องไหน", "โซนไหน", "เล่นที่ไหน", "เล่นได้ที่ไหน")
_CONTROL_TERMS = ("ปุ่ม", "กดอะไร", "controls", "control", "จอย", "คอนโทรล", "บังคับ")
_EQUIPMENT_TERMS = ("อุปกรณ์", "เครื่อง", "สเปค", "spec", "หน้าจอ", "มอนิเตอร์", "monitor", "เมาส์", "คีย์บอร์ด", "หูฟัง", "เก้าอี้")
_SCHEDULE_TERMS = ("เปิด", "ปิด", "กี่โมง", "เวลา", "วันไหน", "วันนี้", "พรุ่งนี้", "จันทร์", "อังคาร", "พุธ", "พฤหัส", "ศุกร์", "เสาร์", "อาทิตย์")
_COMPETITION_TERMS = ("แข่ง", "แข่งขัน", "กติกา", "รอบชิง", "bo3", "bo5", "ทีมละ", "ทัวร์นาเมนต์")
_MEMBER_TERMS = ("สมาชิก", "ทีม", "ตำแหน่ง", "ประธาน", "รองประธาน", "ฝ่าย", "ใคร")
_BROAD_TARGET_TERMS = ("มีอะไรบ้าง", "มีอะไรมั่ง", "มีไรบ้าง", "มีไรมั่ง", "มีอะไร")
_SERVICE_ZONE_LABELS = {
    "pc": "PC Zone",
    "ps5": "PlayStation 5 Zone",
    "nintendo_switch": "Nintendo Switch Zone",
    "cockpit": "Cockpit Zone",
    "vr": "VR Zone",
}
_SERVICE_EXAMPLE_LABELS = {
    "pc": "PC",
    "ps5": "PS5",
    "nintendo_switch": "Nintendo Switch",
    "cockpit": "Cockpit",
    "vr": "VR",
}
_SERVICE_PRICE_KEYS = {
    "pc": ("pc",),
    "ps5": ("ps5",),
    "nintendo_switch": ("nintendo_switch_1_2", "nintendo_switch_3_4"),
    "cockpit": ("cockpit",),
    "vr": ("vr_30", "vr_60"),
}


def _has(text: str, *terms: str) -> bool:
    q = normalize_text(text)
    return any(normalize_text(term) in q for term in terms)


def _looks_like_damage_penalty_query(query: str) -> bool:
    return _has(
        query,
        "เสียหาย",
        "พัง",
        "ค่าปรับ",
        "โดนปรับ",
        "ปรับเท่าไหร่",
        "ค่าซ่อม",
        "ชดเชย",
        "จอแตก",
        "จอยพัง",
        "เมาส์พัง",
        "คีย์บอร์ดพัง",
        "อุปกรณ์เสีย",
    )


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _source_hit(source_id: str, category: str, source_url: str, title: str) -> dict[str, Any]:
    return {
        "id": source_id,
        "metadata": {
            "source_url": source_url,
            "category": category,
            "title": title,
            "source_ids": [source_id],
        },
    }


def _dedupe_hits(hits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for hit in hits:
        metadata = hit.get("metadata", {}) if isinstance(hit, dict) else {}
        key = (str(hit.get("id", "")), str(metadata.get("source_url", "")))
        if key in seen:
            continue
        seen.add(key)
        output.append(hit)
    return output


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


def _game_key(value: str) -> str:
    clean = (value or "").replace("™", "").replace("®", "")
    clean = unicodedata.normalize("NFKD", clean).encode("ascii", "ignore").decode("ascii")
    clean = re.sub(r"\bstandard edition\b", "", clean, flags=re.IGNORECASE)
    return _compact(clean)


@lru_cache(maxsize=1)
def _game_catalog_rows() -> tuple[dict[str, Any], ...]:
    rows_by_game: dict[str, dict[str, Any]] = {}
    for path in (CURATED_DIR / "game_item_details.jsonl", CURATED_DIR / "our_games_scraped_details.jsonl"):
        for row in _read_jsonl(path):
            game = str(row.get("game") or row.get("title") or "").strip()
            if not game:
                continue
            key = _game_key(game)
            if not key:
                continue
            current = rows_by_game.setdefault(key, {"game": game, "zones": set()})
            for zone in row.get("zones") or []:
                current["zones"].add(str(zone))
            listed_under = str(row.get("listed_under") or row.get("source_section") or "").strip()
            if listed_under:
                current["zones"].add(_canonical_zone_label(listed_under))
    for row in _read_jsonl(CURATED_DIR / "game_control_facts.jsonl"):
        game = str(row.get("game") or row.get("title") or "").strip()
        if not game:
            continue
        key = _game_key(game)
        if not key:
            continue
        current = rows_by_game.setdefault(key, {"game": game, "zones": set()})
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
    for row in rows_by_game.values():
        output.append({"game": row["game"], "zones": tuple(sorted(zone for zone in row["zones"] if zone))})
    output.sort(key=lambda item: str(item["game"]).lower())
    return tuple(output)


@lru_cache(maxsize=1)
def _equipment_rows() -> tuple[dict[str, Any], ...]:
    return tuple(_read_jsonl(CURATED_DIR / "equipment_item_details.jsonl"))


def _compact(value: str) -> str:
    return "".join(ch for ch in normalize_text(value or "") if ch.isalnum() or "\u0E00" <= ch <= "\u0E7F")


def _has_known_game(query: str) -> bool:
    q_key = _compact(query)
    if not q_key:
        return False
    for entry in game_alias_entries():
        alias_key = entry.compact
        if len(alias_key) >= 4 and alias_key in q_key:
            return True
        if len(alias_key) >= 3 and any(ch.isdigit() for ch in alias_key) and alias_key in q_key:
            return True
    return False


def _has_service_or_zone(query: str, entities: EntityBundle) -> bool:
    if entities.service:
        return True
    service = detect_from_aliases(query, SERVICE_ALIASES)
    if service.get("key"):
        return True
    return _has(
        query,
        "ps5",
        "playstation",
        "nintendo",
        "switch",
        "vr",
        "วีอาร์",
        "cockpit",
        "ค็อกพิท",
        "คอกพิท",
        "pc",
        "คอม",
    )


def _looks_like_price_query(query: str, entities: EntityBundle) -> bool:
    if _has(
        query,
        "จ่ายภายใน", "ชำระภายใน", "จ่ายเงินผ่าน", "ช่องทางไหน", "โอนเงิน",
        "สลิป", "เลขบัญชี", "ธนาคาร", "ไม่จ่าย", "ลืมจ่าย", "หลังจอง",
        "payment timeout",
    ):
        return False
    return entities.price_intent or _has(query, *_PRICE_TERMS)


def _looks_like_booking_query(query: str) -> bool:
    return _has(query, *_BOOKING_TERMS)


def _looks_like_control_query(query: str) -> bool:
    return _has(query, *_CONTROL_TERMS)


def _looks_like_bare_play_howto(query: str) -> bool:
    return _has(query, "เล่นยังไง", "เล่นอย่างไร", "วิธีเล่น")


def _looks_like_explicit_domain_query(query: str) -> bool:
    return _has(
        query,
        *_PRICE_TERMS,
        *_BOOKING_TERMS,
        *_CANCEL_TERMS,
        *_GAME_LIST_TERMS,
        *_GAME_DETAIL_TERMS,
        *_CONTROL_TERMS,
        *_EQUIPMENT_TERMS,
        *_SCHEDULE_TERMS,
        *_COMPETITION_TERMS,
        *_MEMBER_TERMS,
    )


def _looks_like_short_followup(query: str) -> bool:
    q = normalize_text(query)
    return q.startswith(("แล้ว", "ละ", "ล่ะ", "อันนี้", "อันนั้น", "ต่อ", "สรุป"))


def _looks_too_broad(query: str) -> bool:
    q = normalize_text(query).strip()
    broad_exact = {
        "มีอะไรบ้าง",
        "มีอะไรมั่ง",
        "มีไรบ้าง",
        "มีไรมั่ง",
        "มีอะไร",
        "ขอข้อมูล",
        "บอกหน่อย",
    }
    return q in broad_exact


def _looks_like_service_game_list_query(query: str, entities: EntityBundle) -> bool:
    q = normalize_text(query)
    if not _has_service_or_zone(q, entities):
        return False
    return "เกม" in q and (_has(q, *_BROAD_TARGET_TERMS) or _has(q, *_GAME_LIST_TERMS))


def _route_domain(route: PipelineRoute) -> str:
    if "service_fee" in route.intent or "price" in route.intent:
        return "service_fee"
    if "control" in route.intent:
        return "game_controls"
    return route.category


def _add_candidate(
    scores: dict[tuple[str, str], tuple[float, list[str]]],
    domain: str,
    operation: str,
    amount: float,
    reason: str,
) -> None:
    key = (domain, operation)
    score, reasons = scores.get(key, (0.0, []))
    scores[key] = (score + amount, [*reasons, reason])


def _score_intent_candidates(
    query: str,
    *,
    route: PipelineRoute,
    intent: UniversalIntent,
    entities: EntityBundle,
    has_known_game: bool,
    has_service_or_zone: bool,
    price_query: bool,
) -> tuple[IntentCandidateScore, ...]:
    scores: dict[tuple[str, str], tuple[float, list[str]]] = {}
    game_location_query = has_known_game and _has(
        query,
        "เครื่องไหน", "โซนไหน", "zone ไหน", "เล่นที่ไหน", "เล่นได้ที่ไหน",
        "อยู่โซน", "อยู่เครื่อง", "มีในเครื่อง", "มีในโซน",
    )

    if price_query:
        _add_candidate(scores, "service_fee", "price_calculate", 0.45, "price_terms")
    if has_service_or_zone:
        _add_candidate(scores, "service_fee", "price_calculate", 0.18, "service_or_zone_target")
        _add_candidate(scores, "equipment", "list", 0.16, "service_or_zone_target")
        _add_candidate(scores, "games", "list", 0.15, "service_or_zone_target")
    if has_known_game and price_query:
        _add_candidate(scores, "service_fee", "price_calculate", 0.25, "known_game_price_target")
    if entities.duration or entities.user_group:
        _add_candidate(scores, "service_fee", "price_calculate", 0.10, "price_filters")

    if _looks_like_booking_query(query):
        _add_candidate(scores, "reservation", "booking_policy", 0.45, "booking_terms")
    if _has(query, *_CANCEL_TERMS):
        _add_candidate(scores, "reservation", "cancel_policy", 0.45, "cancel_terms")
    if has_service_or_zone and _looks_like_booking_query(query):
        _add_candidate(scores, "reservation", "booking_policy", 0.20, "booking_target")

    if _has(query, *_GAME_LIST_TERMS):
        _add_candidate(scores, "games", "list", 0.45, "game_list_terms")
    if _has(query, *_GAME_DETAIL_TERMS):
        _add_candidate(scores, "games", "detail", 0.35, "game_detail_terms")
    if has_known_game:
        _add_candidate(scores, "games", "detail", 0.30, "known_game_target")
    if game_location_query:
        _add_candidate(scores, "games", "availability", 0.42, "known_game_location_query")
    if _looks_too_broad(query):
        _add_candidate(scores, "games", "list", 0.20, "broad_list_phrase")
        _add_candidate(scores, "equipment", "list", 0.20, "broad_list_phrase")

    if _looks_like_control_query(query):
        _add_candidate(scores, "game_controls", "control", 0.50, "control_terms")
    if _looks_like_control_query(query) and has_known_game:
        _add_candidate(scores, "game_controls", "control", 0.25, "control_game_target")
    if _looks_like_bare_play_howto(query) and not has_known_game:
        _add_candidate(scores, "game_controls", "control", 0.28, "bare_play_howto")
        _add_candidate(scores, "reservation", "booking_policy", 0.28, "bare_play_howto")

    if _has(query, *_EQUIPMENT_TERMS) and not game_location_query:
        _add_candidate(scores, "equipment", "list", 0.45, "equipment_terms")
    if _has(query, *_EQUIPMENT_TERMS) and has_service_or_zone and not game_location_query:
        _add_candidate(scores, "equipment", "list", 0.20, "equipment_target")

    if _has(query, *_SCHEDULE_TERMS):
        _add_candidate(scores, "schedule", "schedule_query", 0.45, "schedule_terms")
    if _has(query, *_COMPETITION_TERMS):
        _add_candidate(scores, "competition_rules", "competition_rules_lookup", 0.50, "competition_terms")
    if _has(query, *_COMPETITION_TERMS) and (has_known_game or has_service_or_zone):
        _add_candidate(scores, "competition_rules", "competition_rules_lookup", 0.20, "competition_target")
    if _has(query, "ใช้เครื่องอะไรแข่ง", "เครื่องอะไรแข่ง", "ใช้อุปกรณ์อะไรแข่ง"):
        _add_candidate(scores, "competition_rules", "competition_rules_lookup", 0.10, "competition_equipment_phrase")
    if _has(query, *_MEMBER_TERMS):
        _add_candidate(scores, "members", "list", 0.45, "member_terms")

    route_domain = _route_domain(route)
    for (domain, operation) in list(scores):
        if route_domain == domain:
            _add_candidate(scores, domain, operation, 0.18, "route_prior")
        if intent.domain == domain:
            _add_candidate(scores, domain, operation, 0.12, "intent_domain_prior")
        if intent.operation == operation:
            _add_candidate(scores, domain, operation, 0.08, "intent_operation_prior")

    candidates = [
        IntentCandidateScore(domain, operation, min(score, 0.99), tuple(dict.fromkeys(reasons)))
        for (domain, operation), (score, reasons) in scores.items()
    ]
    return tuple(sorted(candidates, key=lambda item: item.score, reverse=True))


def _candidate_metadata(candidates: tuple[IntentCandidateScore, ...]) -> dict[str, Any]:
    return {
        "intent_candidates": [
            {
                "domain": item.domain,
                "operation": item.operation,
                "score": round(item.score, 3),
                "reasons": list(item.reasons),
            }
            for item in candidates[:5]
        ]
    }


def _detect_service_key(query: str, entities: EntityBundle) -> str | None:
    if entities.service in _SERVICE_ZONE_LABELS:
        return entities.service
    service = detect_from_aliases(query, SERVICE_ALIASES)
    key = str(service.get("key") or "")
    return key if key in _SERVICE_ZONE_LABELS else None


def _preview_games_for_zone(zone: str) -> str:
    games = [str(row.get("game") or "") for row in _game_catalog_rows() if zone in (row.get("zones") or ())]
    games = [game for game in games if game]
    if not games:
        return ""
    examples = ", ".join(games[:4])
    if len(games) > 4:
        examples += " และอื่น ๆ"
    return f"มี {len(games)} เกม เช่น {examples}"


def _preview_equipment_for_zone(zone: str) -> str:
    items = [
        str(row.get("item") or "").strip()
        for row in _equipment_rows()
        if _canonical_zone_label(str(row.get("zone") or "")) == zone
    ]
    items = [item for item in items if item]
    if not items:
        return ""
    examples = ", ".join(items[:5])
    if len(items) > 5:
        examples += " และอื่น ๆ"
    return f"มี {len(items)} รายการ เช่น {examples}"


def _preview_price_for_service(service_key: str) -> str:
    package_keys = [key for key in _SERVICE_PRICE_KEYS.get(service_key, ()) if key in SERVICE_FEES]
    if not package_keys:
        return ""
    if len(package_keys) > 1:
        package_labels = ", ".join(
            f"{SERVICE_FEES[key]['label']} {SERVICE_FEES[key]['unit_label']} ({SERVICE_FEES[key]['capacity']})"
            for key in package_keys
        )
        return f"มีหลายแพ็กเกจตามเวลา/จำนวนผู้เล่น: {package_labels}"
    fee = SERVICE_FEES[package_keys[0]]
    prices = [fee["prices"][group] for group in GROUP_ORDER]
    return (
        f"{fee['label']} {fee['unit_label']} ({fee['capacity']}): "
        f"PSU {prices[0]} บาท, General Student {prices[1]} บาท, General Adult {prices[2]} บาท"
    )


def _target_broad_clarification(query: str, entities: EntityBundle) -> tuple[str, list[dict[str, Any]]]:
    service_key = _detect_service_key(query, entities)
    if service_key is None:
        return (
            "คำถามนี้ยังตีได้หลายทางครับ ขอระบุเพิ่มนิดหนึ่งว่าหมายถึงเรื่องไหน\n"
            "เช่น `PC มีเกมอะไรบ้าง`, `PC มีอุปกรณ์อะไรบ้าง`, `PC ราคาเท่าไหร่` หรือ `PC จองยังไง`",
            [],
        )

    zone = _SERVICE_ZONE_LABELS[service_key]
    label = _SERVICE_EXAMPLE_LABELS[service_key]
    preview_lines: list[str] = []
    hits: list[dict[str, Any]] = []

    games_preview = _preview_games_for_zone(zone)
    if games_preview:
        preview_lines.append(f"•    เกม: {games_preview} | พิมพ์ `{label} มีเกมอะไรบ้าง`")
        hits.append(_source_hit("our_games", "games", OUR_GAMES_URL, "Our Games"))

    equipment_preview = _preview_equipment_for_zone(zone)
    if equipment_preview:
        preview_lines.append(f"•    อุปกรณ์: {equipment_preview} | พิมพ์ `{label} มีอุปกรณ์อะไรบ้าง`")
        hits.append(_source_hit("home_equipment", "equipment", HOME_URL, "Home Equipment"))

    price_preview = _preview_price_for_service(service_key)
    if price_preview:
        preview_lines.append(f"•    ราคา: {price_preview} | พิมพ์ `{label} ราคาเท่าไหร่`")
        source_ids = [SERVICE_FEE_IMAGE_2026_ID]
        if service_key == "pc":
            source_ids.append(PC_SERVICE_FEE_LOCAL_UPDATE_20260727_ID)
        hits.extend(make_source_hits(source_ids))

    preview_lines.append(f"•    จอง: ต้องจองผ่านระบบก่อนเข้าใช้ | พิมพ์ `{label} จองยังไง`")
    hits.append(_source_hit("reservation", "reservation", RESERVATION_URL, "Reservation"))

    if not preview_lines:
        return (
            f"คำถามนี้ยังตีได้หลายทางครับ ขอระบุเพิ่มนิดหนึ่งว่าหมายถึงเรื่องไหนของ {zone}\n"
            f"เช่น `{label} มีเกมอะไรบ้าง`, `{label} มีอุปกรณ์อะไรบ้าง`, `{label} ราคาเท่าไหร่` หรือ `{label} จองยังไง`",
            [],
        )

    answer = "\n".join([
        f"คำถามนี้ยังตีได้หลายทางครับ หมายถึงเรื่องไหนของ {zone}?",
        "",
        "ข้อมูลย่อที่ยืนยันได้ตอนนี้:",
        *preview_lines,
        "",
        "พิมพ์ต่อสั้น ๆ ได้ เช่น `เกม`, `อุปกรณ์`, `ราคา` หรือ `จอง`",
    ])
    return answer, _dedupe_hits(hits)


def _control_missing_target_answer() -> str:
    return (
        "ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน\n"
        "ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III\n"
        "เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`"
    )


def _margin_clarification_answer(candidates: tuple[IntentCandidateScore, ...]) -> str:
    labels = {
        "service_fee": "ราคา",
        "reservation": "วิธีจอง",
        "games": "รายชื่อเกม/ข้อมูลเกม",
        "game_controls": "ปุ่มควบคุม",
        "equipment": "อุปกรณ์",
        "schedule": "เวลาเปิด-ปิด",
        "competition_rules": "กติกาการแข่งขัน",
        "members": "สมาชิกทีม",
    }
    domains = []
    for item in candidates[:3]:
        label = labels.get(item.domain, item.domain)
        if label not in domains:
            domains.append(label)
    domain_text = ", ".join(domains) if domains else "ราคา, วิธีจอง, เกม, อุปกรณ์ หรือปุ่มควบคุม"
    return f"คำถามนี้มีได้หลายความหมายครับ ขอระบุเพิ่มนิดหนึ่งว่าต้องการถามเรื่องไหน: {domain_text}"


def _should_margin_clarify(
    candidates: tuple[IntentCandidateScore, ...],
    *,
    query: str,
    route: PipelineRoute,
    has_known_game: bool,
    has_service_or_zone: bool,
    price_query: bool,
) -> bool:
    if len(candidates) < 2:
        return False
    top, second = candidates[0], candidates[1]
    margin = top.score - second.score
    if top.score < 0.50 or second.score < 0.42 or margin >= 0.14:
        return False
    if route.category == "multi_question":
        return False
    if price_query and (has_known_game or has_service_or_zone):
        return False
    if has_known_game and _has(query, "เครื่องไหน", "โซนไหน", "zone ไหน", "เล่นที่ไหน", "เล่นได้ที่ไหน", "อยู่โซน", "อยู่เครื่อง", "มีในเครื่อง"):
        return False
    if route.category == "competition_rules" and _has(query, *_COMPETITION_TERMS):
        return False
    if route.category == "overview":
        return False
    if _looks_like_booking_query(query) and not price_query:
        return False
    if has_service_or_zone and _has(query, *_GAME_LIST_TERMS):
        return False
    if has_known_game and _looks_like_control_query(query):
        return False
    return True


def _price_missing_target_answer() -> str:
    return (
        "ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง\n"
        "เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` "
        "หรือ `Tekken 8 ราคาเท่าไหร่`"
    )


def _broad_missing_target_answer() -> str:
    return (
        "คำถามนี้ยังกว้างเกินไปครับ ยังไม่แน่ใจว่าต้องการถามเรื่องไหนของ PSU Esports Studio - Phuket\n"
        "ถามให้เจาะจงได้ เช่น `มีเกมอะไรบ้าง`, `มีอุปกรณ์อะไรบ้าง`, `จองยังไง`, `ราคา PS5 เท่าไหร่` "
        "หรือ `TEKKEN 8 มีปุ่มอะไรบ้าง`"
    )


def _entity_operation_hint(query: str, route: PipelineRoute, intent: UniversalIntent, entities: EntityBundle) -> str:
    q = normalize_text(query)
    if _looks_like_control_query(q):
        return "controls"
    if _looks_like_bare_play_howto(q):
        return "gameplay"
    if _looks_like_price_query(q, entities):
        return "price"
    if _looks_like_booking_query(q):
        return "booking"
    if _has(q, *_GAME_LIST_TERMS):
        return "list"
    if _has(q, "กี่เกม", "จำนวนเกม"):
        return "count"
    if _has(q, *_GAME_DETAIL_TERMS):
        return "availability"
    if route.category == "games" and route.intent in {"game_detail_lookup", "games_lookup"}:
        return "detail"
    if intent.domain == "game_controls" or intent.operation == "control":
        return "controls"
    if intent.domain == "games":
        return str(intent.operation or "detail")
    return ""


def _game_entity_clarification_answer(resolution: EntityResolution, operation: str) -> str:
    operation_labels = {
        "controls": "ปุ่ม/วิธีควบคุม",
        "gameplay": "วิธีเล่น",
        "detail": "ข้อมูลเกม",
        "booking": "การจอง",
        "price": "ราคา",
    }
    label = operation_labels.get(operation, "ข้อมูลของเกม")
    candidates = [candidate for candidate in resolution.candidates if candidate.title]
    if not candidates:
        return "ยังไม่แน่ใจว่าหมายถึงเกมไหนครับ ขอชื่อเกมให้ชัดเจนก่อน จะได้ไม่ดึงข้อมูลของเกมอื่นมาตอบแทน"

    family = str(resolution.metadata.get("family") or "").strip()
    if family:
        opening = (
            f"{family} มีหลายเกมในรายการปัจจุบันครับ คำถามนี้จึงยังไม่ชัดว่าหมายถึงเกมไหน "
            f"ถ้าต้องการถามเรื่อง{label} ขอเลือกเกมก่อน:"
        )
    else:
        opening = f"คำถามนี้ยังไม่ชัดว่าหมายถึงเกมไหนครับ เพราะมีหลายเกมที่ตรงกับคำถาม ถ้าต้องการถามเรื่อง{label} ขอเลือกเกมก่อน:"
    lines = [opening]
    for index, candidate in enumerate(candidates[:6], 1):
        zones = " / ".join(candidate.zones)
        suffix = f" ({zones})" if zones else ""
        lines.append(f"{index}. {candidate.title}{suffix}")
    if operation == "controls":
        lines.append("")
        example = candidates[0].title
        alt_example = candidates[1].title if len(candidates) > 1 else example
        lines.append(f"พิมพ์ต่อได้ เช่น `{example} ปุ่มอะไร` หรือ `{alt_example} ปุ่มอะไร`")
    elif operation == "gameplay":
        lines.append("")
        lines.append(f"พิมพ์ต่อได้ เช่น `{candidates[0].title} เล่นยังไง`")
    elif operation == "booking":
        lines.append("")
        lines.append(f"พิมพ์ต่อได้ เช่น `{candidates[0].title} ต้องจองอะไร`")
    return "\n".join(lines)


def _should_clarify_ambiguous_game_entity(query: str, operation: str, resolution: EntityResolution) -> bool:
    if not resolution.is_ambiguous or not operation_requires_exact_game(operation):
        return False
    q = normalize_text(query)
    if operation == "booking":
        # Booking family questions have a structured data answer that lists the valid services.
        return False
    if operation == "controls":
        return _looks_like_control_query(q)
    if operation == "gameplay":
        return True
    if operation == "detail":
        return _has(q, "คืออะไร", "แนวอะไร", "แนวไหน", "ข้อมูล", "รายละเอียด", "เกี่ยวกับอะไร")
    if operation == "price":
        return True
    return False


def evaluate_ambiguity_gate(
    query: str,
    *,
    route: PipelineRoute,
    intent: UniversalIntent,
    entities: EntityBundle,
    tool_decision: Any | None = None,
) -> AmbiguityGateResult:
    q = normalize_text(query)
    flags: list[str] = []

    has_known_game = _has_known_game(q)
    has_service_or_zone = _has_service_or_zone(q, entities)
    has_target = has_known_game or has_service_or_zone
    price_query = _looks_like_price_query(q, entities)
    candidates = _score_intent_candidates(
        q,
        route=route,
        intent=intent,
        entities=entities,
        has_known_game=has_known_game,
        has_service_or_zone=has_service_or_zone,
        price_query=price_query,
    )
    candidate_metadata = _candidate_metadata(candidates)
    entity_operation = _entity_operation_hint(q, route, intent, entities)
    game_resolution = resolve_game_entity(q, operation=entity_operation)
    entity_metadata = {"game_entity_resolution": game_resolution.as_dict()}

    if _looks_like_damage_penalty_query(q):
        flags.append("damage_penalty_query_allowed")
        return AmbiguityGateResult(
            "allow",
            0.92,
            "damage/penalty query should use policy facts instead of control/price clarification",
            tuple(flags),
            None,
            {
                "route": f"{route.category}/{route.intent}",
                "intent": f"{intent.domain}/{intent.operation}",
                **entity_metadata,
                **candidate_metadata,
            },
        )

    if (
        _should_clarify_ambiguous_game_entity(q, entity_operation, game_resolution)
        and not operation_allows_family_list(entity_operation)
    ):
        flags.append("game_entity_ambiguous_requires_clarification")
        return AmbiguityGateResult(
            "clarify",
            0.86,
            game_resolution.reason,
            tuple(flags),
            _game_entity_clarification_answer(game_resolution, entity_operation),
            {
                "route": f"{route.category}/{route.intent}",
                "intent": f"{intent.domain}/{intent.operation}",
                **entity_metadata,
                **candidate_metadata,
            },
        )

    if price_query and not has_target and not _looks_like_damage_penalty_query(q):
        flags.append("price_missing_service_or_game_target")
        if _looks_like_short_followup(q):
            flags.append("short_followup_missing_context")
        return AmbiguityGateResult(
            "clarify",
            0.88,
            "price query is missing service/zone/game target",
            tuple(flags),
            _price_missing_target_answer(),
            {
                "route": f"{route.category}/{route.intent}",
                "intent": f"{intent.domain}/{intent.operation}",
                "tool_action": getattr(tool_decision, "action", ""),
                "tool_domain": getattr(tool_decision, "domain", ""),
                **entity_metadata,
                **candidate_metadata,
            },
        )

    if _looks_too_broad(q) and route.category not in {"reservation", "schedule", "contact"}:
        flags.append("broad_query_missing_domain_target")
        return AmbiguityGateResult(
            "clarify",
            0.82,
            "query is too broad to choose one PSU domain safely",
            tuple(flags),
            _broad_missing_target_answer(),
            {
                "route": f"{route.category}/{route.intent}",
                "intent": f"{intent.domain}/{intent.operation}",
                **entity_metadata,
                **candidate_metadata,
            },
        )

    if _looks_like_short_followup(q) and not has_target and intent.operation in {"price_calculate", "control", "detail", "list"}:
        flags.append("short_followup_missing_context")
        return AmbiguityGateResult(
            "clarify",
            0.80,
            "short follow-up has no resolved target",
            tuple(flags),
            _broad_missing_target_answer(),
            {
                "route": f"{route.category}/{route.intent}",
                "intent": f"{intent.domain}/{intent.operation}",
                **entity_metadata,
                **candidate_metadata,
            },
        )

    if _looks_like_control_query(q) and not has_known_game:
        flags.append("control_query_missing_game_target")
        return AmbiguityGateResult(
            "clarify",
            0.84,
            "control query is missing game target",
            tuple(flags),
            _control_missing_target_answer(),
            {
                "route": f"{route.category}/{route.intent}",
                "intent": f"{intent.domain}/{intent.operation}",
                **entity_metadata,
                **candidate_metadata,
            },
        )

    if _looks_like_bare_play_howto(q) and not has_known_game and not _looks_like_booking_query(q):
        flags.append("bare_play_howto_missing_domain_or_game")
        return AmbiguityGateResult(
            "clarify",
            0.76,
            "bare play-how question can mean booking/access or game controls",
            tuple(flags),
            (
                "ยังไม่แน่ใจว่าหมายถึงเกมไหนครับ หรือหมายถึงวิธีเล่นเกมไหน/วิธีเข้าใช้บริการ/จอง\n"
                "ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III\n"
                "ถ้าถามวิธีเล่น/ปุ่ม ให้พิมพ์ชื่อเกมมาด้วย เช่น `TEKKEN 8 เล่นยังไง` หรือ `Mario Kart 8 Deluxe เล่นยังไง`"
            ),
            {
                "route": f"{route.category}/{route.intent}",
                "intent": f"{intent.domain}/{intent.operation}",
                **entity_metadata,
                **candidate_metadata,
            },
        )

    if (
        has_service_or_zone
        and not has_known_game
        and _has(q, *_BROAD_TARGET_TERMS)
        and not _looks_like_service_game_list_query(q, entities)
        and not _looks_like_explicit_domain_query(q.replace("มีอะไรบ้าง", "").replace("มีอะไรมั่ง", "").replace("มีไรบ้าง", "").replace("มีไรมั่ง", "").replace("มีอะไร", ""))
    ):
        flags.append("service_target_broad_missing_operation")
        clarification_answer, clarification_hits = _target_broad_clarification(q, entities)
        return AmbiguityGateResult(
            "clarify",
            0.78,
            "service/zone target is present but requested operation is broad",
            tuple(flags),
            clarification_answer,
            {
                "route": f"{route.category}/{route.intent}",
                "intent": f"{intent.domain}/{intent.operation}",
                **entity_metadata,
                **candidate_metadata,
            },
            clarification_hits,
        )

    if _should_margin_clarify(
        candidates,
        query=q,
        route=route,
        has_known_game=has_known_game,
        has_service_or_zone=has_service_or_zone,
        price_query=price_query,
    ):
        flags.append("low_margin_between_intent_candidates")
        top = candidates[0]
        second = candidates[1]
        return AmbiguityGateResult(
            "clarify",
            0.74,
            "top intent candidates are too close",
            tuple(flags),
            _margin_clarification_answer(candidates),
            {
                "route": f"{route.category}/{route.intent}",
                "intent": f"{intent.domain}/{intent.operation}",
                "top_candidate": f"{top.domain}/{top.operation}",
                "second_candidate": f"{second.domain}/{second.operation}",
                "margin": round(top.score - second.score, 3),
                **entity_metadata,
                **candidate_metadata,
            },
        )

    if price_query and has_known_game:
        flags.append("price_query_with_game_target_requires_zone_mapping")
    if route.category != intent.domain and intent.domain not in {"members", "game_controls"}:
        flags.append("route_intent_domain_difference")

    return AmbiguityGateResult(
        "allow",
        0.94 if not flags else 0.76,
        "ambiguity risk acceptable",
        tuple(dict.fromkeys(flags)),
        metadata={
            "route": f"{route.category}/{route.intent}",
            "intent": f"{intent.domain}/{intent.operation}",
            "has_known_game": has_known_game,
            "has_service_or_zone": has_service_or_zone,
            **entity_metadata,
            **candidate_metadata,
        },
    )
