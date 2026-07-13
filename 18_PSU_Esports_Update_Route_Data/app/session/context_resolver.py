from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

from app.core.normalization import normalize_text


ROOT = Path(__file__).resolve().parents[2]
CURATED_DIR = ROOT / "data" / "curated"

FOLLOWUP_TERMS = (
    "เกมนี้", "อันนี้", "ตัวนี้", "มัน", "แล้ว", "ต่อ", "อันเมื่อกี้",
    "เล่นยังไง", "เล่นอย่างไร", "วิธีเล่น", "แนวอะไร", "เกี่ยวกับอะไร",
    "อยู่โซนไหน", "โซนไหน", "เล่นได้ที่ไหน", "มีปุ่มอะไร", "ปุ่มอะไร",
    "ปุ่มทั้งหมด", "มีปุ่มอะไรบ้าง", "ใช้จอยยังไง", "controller", "controls",
    "กดอะไร", "กดยังไง", "ปุ่มไหน",
)

TOPIC_SHIFT_TERMS = (
    "จอง", "booking", "reserve", "คิว", "ชำระ", "จ่ายเงิน", "ยกเลิก", "คืนเงิน",
    "ราคา", "ค่าบริการ", "กี่บาท", "เท่าไหร่", "เท่าไร", "เสียเงิน",
    "เปิด", "ปิด", "เวลา", "วันหยุด", "วันนี้", "พรุ่งนี้", "ตาราง",
    "กฎ", "กติกา", "แข่งขัน", "แข่ง", "ทัวร์", "สมัคร",
)


@dataclass(frozen=True)
class ResolvedQuestion:
    original_question: str
    resolved_question: str
    used_context: bool
    context_game: str | None = None
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


def latest_game_from_history(recent_history: Any) -> str | None:
    for text in reversed(_history_text_items(recent_history)):
        game = detect_game(text)
        if game:
            return game
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


def resolve_question_with_context(question: str, recent_history: Any) -> ResolvedQuestion:
    original = str(question or "").strip()
    if not original:
        return ResolvedQuestion(original, original, False, reason="empty")

    explicit_game = detect_game(original)
    if explicit_game:
        return ResolvedQuestion(original, original, False, explicit_game, "question_has_explicit_game")

    if _looks_like_topic_shift(original):
        return ResolvedQuestion(original, original, False, reason="topic_shift")

    if not _looks_like_followup(original):
        return ResolvedQuestion(original, original, False, reason="not_followup")

    context_game = latest_game_from_history(recent_history)
    if not context_game:
        return ResolvedQuestion(original, original, False, reason="no_context_game")

    resolved = f"{context_game} {original}"
    return ResolvedQuestion(original, resolved, True, context_game, "inherited_game_from_recent_history")
