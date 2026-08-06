from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

from app.core.normalization import SERVICE_ALIASES, detect_from_aliases, normalize_text


ROOT = Path(__file__).resolve().parents[2]
CURATED_DIR = ROOT / "data" / "curated"

FOLLOWUP_TERMS = (
    "เกมนี้", "อันนี้", "ตัวนี้", "มัน", "แล้ว", "ต่อ", "อันเมื่อกี้",
    "สรุป", "สรุปคือ", "ทำไง", "ทำยังไง", "ทำอย่างไร", "ต้องทำไง", "ต้องทำยังไง", "จะเล่น",
    "เล่นยังไง", "เล่นอย่างไร", "วิธีเล่น", "แนวอะไร", "เกี่ยวกับอะไร",
    "อยู่โซนไหน", "โซนไหน", "เล่นได้ที่ไหน", "มีปุ่มอะไร", "ปุ่มอะไร",
    "ปุ่ม", "ปุ่มกด", "คอนโทรล", "การควบคุม",
    "ปุ่มทั้งหมด", "มีปุ่มอะไรบ้าง", "ใช้จอยยังไง", "controller", "control", "controls",
    "button", "buttons", "กดอะไร", "กดยังไง", "ปุ่มไหน",
    "แต่ละหมวด", "แต่ละกลุ่ม", "หมวดนี้", "กลุ่มนี้", "หมวดอะไร", "กลุ่มอะไร",
    "มีใครบ้าง", "รายชื่อ", "ทั้งหมดมีใครบ้าง", "มีเกมอะไรบ้าง", "มีกี่เกม",
    "แล้วกี่คน", "กี่คน", "กี่หมวด", "กี่กลุ่ม",
)

TOPIC_SHIFT_TERMS = (
    "จอง", "booking", "reserve", "คิว", "ชำระ", "จ่ายเงิน", "ยกเลิก", "คืนเงิน",
    "ราคา", "ค่าบริการ", "กี่บาท", "เท่าไหร่", "เท่าไร", "เสียเงิน",
    "เปิด", "ปิด", "เวลา", "วันหยุด", "วันนี้", "พรุ่งนี้", "ตาราง",
    "กฎ", "กติกา", "แข่งขัน", "แข่ง", "ทัวร์", "สมัคร",
)

CLARIFICATION_CHOICE_TERMS = (
    "เกม", "game", "games", "รายชื่อเกม", "มีเกมอะไรบ้าง", "เกมอะไรบ้าง",
    "อุปกรณ์", "equipment", "มีอุปกรณ์อะไรบ้าง",
    "ราคา", "price", "ค่าบริการ", "กี่บาท", "เท่าไหร่", "เท่าไร",
    "จอง", "booking", "book", "วิธีจอง", "จองยังไง", "จองไง",
)

ZONE_LABELS = {
    "PC Zone": "PC",
    "PlayStation 5 Zone": "PS5",
    "Nintendo Switch Zone": "Nintendo Switch",
    "VR Zone": "VR",
    "Cockpit Zone": "Cockpit",
}


@dataclass(frozen=True)
class ResolvedQuestion:
    original_question: str
    resolved_question: str
    used_context: bool
    context_game: str | None = None
    context_domain: str | None = None
    context_operation: str | None = None
    context_topic: str | None = None
    reason: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _alias_key(value: str) -> str:
    return re.sub(r"[^0-9a-z\u0E00-\u0E7F]+", "", normalize_text(value))


@lru_cache(maxsize=1)
def _game_alias_index() -> tuple[tuple[str, str, str], ...]:
    by_game: dict[str, set[str]] = {}
    alias_paths = (
        CURATED_DIR / "game_title_aliases.jsonl",
        CURATED_DIR / "game_item_details.jsonl",
        CURATED_DIR / "our_games_scraped_details.jsonl",
    )
    for path in (*alias_paths, CURATED_DIR / "game_control_facts.jsonl"):
        for row in _read_jsonl(path):
            game = str(row.get("game") or row.get("title") or "").strip()
            if not game:
                continue
            values = by_game.setdefault(game, set())
            values.add(game)
            if path not in alias_paths:
                continue
            for alias in row.get("aliases") or []:
                alias_text = str(alias or "").strip()
                if alias_text:
                    values.add(alias_text)

    entries: list[tuple[str, str, str]] = []
    for game, aliases in by_game.items():
        for alias in aliases:
            normalized = normalize_text(alias)
            compact = _alias_key(alias)
            if len(compact) >= 4:
                entries.append((game, normalized, compact))
    entries.sort(key=lambda item: len(item[2]), reverse=True)
    return tuple(entries)


def detect_game(text: str) -> str | None:
    q = normalize_text(text)
    q_compact = _alias_key(text)
    for game, normalized, compact in _game_alias_index():
        if normalized and normalized in q:
            return game
        if compact and compact in q_compact:
            return game
    return None


def detect_service(text: str) -> str | None:
    service = detect_from_aliases(text, SERVICE_ALIASES)
    key = str(service.get("key") or "").strip()
    return key or None


def _history_text_items(recent_history: Any) -> list[str]:
    if not isinstance(recent_history, list):
        return []
    texts: list[str] = []
    for item in recent_history[-12:]:
        if isinstance(item, dict):
            text = str(item.get("text") or item.get("content") or "").strip()
        else:
            text = str(item or "").strip()
        if text:
            texts.append(text)
    return texts


def _history_dict_items(recent_history: Any) -> list[dict[str, Any]]:
    if not isinstance(recent_history, list):
        return []
    items: list[dict[str, Any]] = []
    for item in recent_history[-16:]:
        if not isinstance(item, dict):
            continue
        copied = dict(item)
        text = str(copied.get("text") or copied.get("content") or "").strip()
        if text:
            copied["text"] = text
        items.append(copied)
    return items


def latest_game_from_history(recent_history: Any) -> str | None:
    for text in reversed(_history_text_items(recent_history)):
        game = detect_game(text)
        if game:
            return game
    return None


def _latest_universal_intent_from_history(recent_history: Any) -> dict[str, Any]:
    for item in reversed(_history_dict_items(recent_history)):
        intent = item.get("universal_intent")
        if isinstance(intent, dict):
            domain = str(intent.get("domain") or "").strip()
            operation = str(intent.get("operation") or "").strip()
            if domain or operation:
                return {
                    "domain": domain,
                    "operation": operation,
                    "target": str(intent.get("target") or "").strip(),
                    "filters": intent.get("filters") if isinstance(intent.get("filters"), dict) else {},
                    "source": "universal_intent",
                }
        domain = str(item.get("domain") or "").strip()
        operation = str(item.get("operation") or "").strip()
        if domain or operation:
            return {"domain": domain, "operation": operation, "target": "", "filters": {}, "source": "history_fields"}
    return {}


def _infer_domain_from_history_text(recent_history: Any) -> dict[str, Any]:
    for text in reversed(_history_text_items(recent_history)):
        q = normalize_text(text)
        if "สมาชิกในหน้า members แบ่งเป็น" in q or "สมาชิกจากหน้า members" in q:
            return {"domain": "members", "operation": "group_count", "target": "PSU Esports members", "source": "answer_text"}
        if "playstation 5 zone มีเกม" in q or "nintendo switch zone" in q or "สรุปเกมที่เล่นได้" in q:
            return {"domain": "games", "operation": "list", "target": _latest_zone_from_history(recent_history) or "", "source": "answer_text"}
        if "มีปุ่มควบคุมดังนี้" in q:
            return {"domain": "game_controls", "operation": "control", "target": latest_game_from_history(recent_history) or "", "source": "answer_text"}
    return {}


def _latest_pending_clarification_from_history(recent_history: Any) -> dict[str, Any]:
    for item in reversed(_history_dict_items(recent_history)):
        text = str(item.get("text") or item.get("content") or "").strip()
        if not text:
            continue
        role = str(item.get("role") or "").strip().lower()
        if role and role != "assistant":
            return {}
        route_category = str(item.get("route_category") or "").strip()
        route_intent = str(item.get("route_intent") or "").strip()
        if route_category != "clarification" and "clarification" not in route_intent and "หมายถึงเรื่องไหนของ" not in text:
            return {}
        if "หมายถึงเรื่องไหนของ" not in text or "พิมพ์ต่อสั้น" not in text:
            return {}
        match = re.search(r"หมายถึงเรื่องไหนของ\s+(.+?)(?:\?|\\n|\n)", text)
        target = match.group(1).strip() if match else ""
        service = ZONE_LABELS.get(target, target.replace(" Zone", "").strip())
        if not service:
            return {}
        return {
            "domain": "clarification",
            "operation": "service_broad_choice",
            "target": target,
            "zone": service,
            "service": service,
            "pending_clarification": True,
            "allowed_choices": ("games", "equipment", "price", "booking"),
            "ttl_policy": "latest_assistant_only",
            "source": "ambiguity_clarification_preview",
        }
    return {}


def latest_context_state(recent_history: Any) -> dict[str, Any]:
    pending_clarification = _latest_pending_clarification_from_history(recent_history)
    state = pending_clarification or _latest_universal_intent_from_history(recent_history) or _infer_domain_from_history_text(recent_history)
    if not state:
        state = {}
    if state.get("pending_clarification"):
        return state
    game = latest_game_from_history(recent_history)
    zone = _latest_zone_from_history(recent_history)
    if game and not state.get("game"):
        state["game"] = game
    if zone and not state.get("zone"):
        state["zone"] = zone
    return state


def _latest_zone_from_history(recent_history: Any) -> str | None:
    for text in reversed(_history_text_items(recent_history)):
        q = normalize_text(text)
        if any(term in q for term in ("playstation 5 zone", "ps5", "playstation", "เพลย์")):
            return "PlayStation 5"
        if any(term in q for term in ("nintendo switch zone", "nintendo", "switch", "นินเทนโด")):
            return "Nintendo Switch"
        if any(term in q for term in ("pc zone", "คอม", "pc")):
            return "PC"
        if any(term in q for term in ("vr zone", "vr", "วีอาร์", "แว่น")):
            return "VR"
        if any(term in q for term in ("cockpit zone", "cockpit", "คอกพิท", "ค็อกพิท")):
            return "Cockpit"
    return None


def _has_any(query: str, terms: tuple[str, ...]) -> bool:
    q = normalize_text(query)
    return any(normalize_text(term) in q for term in terms)


def _looks_like_followup(question: str) -> bool:
    q = normalize_text(question)
    if len(q.split()) <= 4 and _has_any(q, FOLLOWUP_TERMS):
        return True
    return _has_any(q, FOLLOWUP_TERMS)


def _looks_like_topic_shift(question: str) -> bool:
    return _has_any(question, TOPIC_SHIFT_TERMS)


def _looks_like_explicit_all_game_catalog(question: str) -> bool:
    q = normalize_text(question)
    return (
        _has_any(q, ("เกมทั้งหมด", "ทั้งหมด", "ทุกโซน", "ทุกเครื่อง", "ทุกแพลตฟอร์ม", "all games", "all game"))
        or (_has_any(q, ("เกมตอนนี้", "ตอนนี้มีเกม", "ตอนนี้เกม")) and _has_any(q, ("มีเกมอะไร", "เกมอะไรบ้าง", "กี่เกม", "มีกี่เกม")))
    )


def _resolve_member_followup(original: str, state: dict[str, Any]) -> ResolvedQuestion | None:
    q = normalize_text(original)
    domain = str(state.get("domain") or "")
    if domain != "members":
        return None
    if _has_any(q, ("กี่หมวด", "กี่กลุ่ม", "มีกี่หมวด", "มีกี่กลุ่ม", "แบ่งเป็นกี่", "จำนวนหมวด", "จำนวนกลุ่ม")):
        return ResolvedQuestion(
            original,
            "สมาชิกใน PSU Esports มีกี่หมวด",
            True,
            context_domain="members",
            context_operation="group_count",
            context_topic="PSU Esports members",
            reason="inherited_members_group_count_from_recent_history",
        )
    if _has_any(q, ("หมวดอะไร", "กลุ่มอะไร", "หัวข้ออะไร", "มีหมวดอะไร", "มีกลุ่มอะไร")):
        return ResolvedQuestion(
            original,
            "สมาชิกใน PSU Esports มีหมวดอะไรบ้าง",
            True,
            context_domain="members",
            context_operation="group_count",
            context_topic="PSU Esports members",
            reason="inherited_members_group_names_from_recent_history",
        )
    if _has_any(q, ("แต่ละหมวดมีใคร", "แต่ละกลุ่มมีใคร", "มีใครบ้าง", "รายชื่อ", "รายชื่อสมาชิก")):
        return ResolvedQuestion(
            original,
            "สมาชิกใน PSU Esports แต่ละหมวดมีใครบ้าง",
            True,
            context_domain="members",
            context_operation="group_list",
            context_topic="PSU Esports members",
            reason="inherited_members_domain_from_recent_history",
        )
    if _has_any(q, ("กี่คน", "ทั้งหมดกี่คน", "จำนวนคน")):
        return ResolvedQuestion(
            original,
            "สมาชิกใน PSU Esports มีทั้งหมดกี่คน",
            True,
            context_domain="members",
            context_operation="count",
            context_topic="PSU Esports members",
            reason="inherited_members_count_from_recent_history",
        )
    return None


def _resolve_games_followup(original: str, state: dict[str, Any]) -> ResolvedQuestion | None:
    q = normalize_text(original)
    domain = str(state.get("domain") or "")
    if domain not in {"games", "equipment"}:
        return None
    if _looks_like_explicit_all_game_catalog(q):
        return None
    zone = str(state.get("zone") or state.get("target") or "").strip()
    if _has_any(q, ("มีเกมอะไร", "เกมอะไรบ้าง", "มีอะไรบ้าง", "รายชื่อเกม", "list game")) and zone:
        return ResolvedQuestion(
            original,
            f"{zone} มีเกมอะไรบ้าง",
            True,
            context_domain="games",
            context_operation=str(state.get("operation") or ""),
            context_topic=zone,
            reason="inherited_game_zone_from_recent_history",
        )
    if _has_any(q, ("กี่เกม", "มีกี่เกม", "จำนวนเกม")) and zone:
        return ResolvedQuestion(
            original,
            f"{zone} มีเกมกี่เกม",
            True,
            context_domain="games",
            context_operation=str(state.get("operation") or ""),
            context_topic=zone,
            reason="inherited_game_zone_count_from_recent_history",
        )
    return None


def _clarification_choice(original: str) -> str:
    q = normalize_text(original).strip()
    q = re.sub(r"\s+", " ", q)
    q = q.strip(" ?？!！.")
    q = re.sub(r"^(ขอ|ดู|เอา|เรื่อง|ถามเรื่อง)\s*", "", q).strip()
    q = re.sub(r"\s*(ครับ|ค่ะ|คับ|ฮะ|หน่อย|ให้หน่อย)$", "", q).strip()
    if not q or len(q) > 24:
        return ""
    if q in {"เกม", "เกมส์", "game", "games", "รายชื่อเกม", "เกมอะไร", "เกมอะไรบ้าง", "มีเกมอะไรบ้าง"}:
        return "games"
    if q in {"อุปกรณ์", "equipment", "มีอุปกรณ์อะไรบ้าง"}:
        return "equipment"
    if q in {"ราคา", "price", "ค่าบริการ", "กี่บาท", "เท่าไหร่", "เท่าไร"}:
        return "price"
    if q in {"จอง", "booking", "book", "วิธีจอง", "จองยังไง", "จองไง"}:
        return "booking"
    return ""


def _resolve_clarification_choice_followup(original: str, state: dict[str, Any]) -> ResolvedQuestion | None:
    if not state.get("pending_clarification"):
        return None
    if detect_game(original) or detect_service(original) or _looks_like_explicit_all_game_catalog(original):
        return None
    choice = _clarification_choice(original)
    if not choice:
        return None
    service = str(state.get("service") or state.get("zone") or state.get("target") or "").strip()
    if not service:
        return None
    if choice == "games":
        resolved = f"{service} มีเกมอะไรบ้าง"
        domain = "games"
        operation = "list"
    elif choice == "equipment":
        resolved = f"{service} มีอุปกรณ์อะไรบ้าง"
        domain = "equipment"
        operation = "list"
    elif choice == "price":
        resolved = f"{service} ราคาเท่าไหร่"
        domain = "service_fee"
        operation = "price_calculate"
    else:
        resolved = f"{service} จองยังไง"
        domain = "reservation"
        operation = "how_to"
    return ResolvedQuestion(
        original,
        resolved,
        True,
        context_domain=domain,
        context_operation=operation,
        context_topic=service,
        reason="resolved_pending_ambiguity_clarification_choice",
    )


def _resolve_reservation_followup(original: str, state: dict[str, Any]) -> ResolvedQuestion | None:
    q = normalize_text(original)
    domain = str(state.get("domain") or "")
    if domain != "reservation":
        return None
    if _has_any(q, ("สรุป", "สรุปคือ", "ทำยังไง", "ทำอย่างไร", "ต้องทำยังไง", "ยังไง", "อย่างไร")):
        return ResolvedQuestion(
            original,
            "สรุปขั้นตอนจองทำยังไง",
            True,
            context_domain="reservation",
            context_operation="how_to",
            context_topic="booking_steps",
            reason="inherited_reservation_how_to_from_recent_history",
        )
    return None


def _resolve_game_control_followup(original: str, state: dict[str, Any]) -> ResolvedQuestion | None:
    if _looks_like_topic_shift(original):
        return None
    context_game = str(state.get("game") or latest_game_from_history([state]) or "").strip()
    if not context_game:
        return None
    if not _looks_like_followup(original):
        return None
    resolved = f"{context_game} {original}"
    return ResolvedQuestion(
        original,
        resolved,
        True,
        context_game,
        context_domain=str(state.get("domain") or "games"),
        context_operation=str(state.get("operation") or ""),
        context_topic=context_game,
        reason="inherited_game_from_recent_history",
    )


def resolve_question_with_context(question: str, recent_history: Any) -> ResolvedQuestion:
    original = str(question or "").strip()
    if not original:
        return ResolvedQuestion(original, original, False, reason="empty")

    explicit_game = detect_game(original)
    if explicit_game:
        return ResolvedQuestion(original, original, False, explicit_game, reason="question_has_explicit_game")

    state = latest_context_state(recent_history)

    clarification_followup = _resolve_clarification_choice_followup(original, state)
    if clarification_followup is not None:
        return clarification_followup

    if not _looks_like_followup(original):
        return ResolvedQuestion(original, original, False, reason="not_followup")

    member_followup = _resolve_member_followup(original, state)
    if member_followup is not None:
        return member_followup

    games_followup = _resolve_games_followup(original, state)
    if games_followup is not None:
        return games_followup

    reservation_followup = _resolve_reservation_followup(original, state)
    if reservation_followup is not None:
        return reservation_followup

    if _looks_like_topic_shift(original):
        return ResolvedQuestion(
            original,
            original,
            False,
            context_domain=str(state.get("domain") or "") or None,
            context_operation=str(state.get("operation") or "") or None,
            context_topic=str(state.get("target") or "") or None,
            reason="topic_shift",
        )

    game_followup = _resolve_game_control_followup(original, state)
    if game_followup is not None:
        return game_followup

    return ResolvedQuestion(
        original,
        original,
        False,
        context_domain=str(state.get("domain") or "") or None,
        context_operation=str(state.get("operation") or "") or None,
        context_topic=str(state.get("target") or "") or None,
        reason="no_matching_context_resolution",
    )
