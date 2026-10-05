from __future__ import annotations

import json
import re
from dataclasses import dataclass
from difflib import SequenceMatcher
from functools import lru_cache
from pathlib import Path
from typing import Any

from app.core.normalization import THAI_DIGIT_TRANS


ROOT = Path(__file__).resolve().parents[2]
CURATED_DIR = ROOT / "data" / "curated"

GAME_TITLE_FILES = (
    "game_title_aliases.jsonl",
    "game_item_details.jsonl",
    "our_games_scraped_details.jsonl",
    "game_control_facts.jsonl",
)

# Broad franchise/family labels. These are canonical targets, not typo aliases.
# They let a typo such as "msrio" become "Mario" so the family answer can list all Mario games.
BROAD_TITLE_ALIASES = {
    "Mario": ("Mario", "มาริโอ", "มาริโอ้"),
    "Resident Evil": ("Resident Evil", "เรสซิเดนต์อีวิล", "เรสซิเดนท์อีวิล", "เรสซิเดนต์", "เรสซิเดนท์"),
    "Call of Duty": ("Call of Duty", "คอลออฟดิวตี้", "คอลออฟดูตี้", "ดิวตี้", "ดูตี้"),
    "Overcooked": ("Overcooked", "โอเวอร์คุก", "โอเวอร์คุ๊ก", "โอเวอคุก", "โอเวอคุ๊ก"),
}
BROAD_TITLE_ALIASES["Overcooked"] = (
    *BROAD_TITLE_ALIASES["Overcooked"],
    "Overcook",
    "Over cook",
)

# Keep short abbreviations exact-only. Fuzzy matching these creates false positives too easily.
FUZZY_SHORT_ALIAS_BLOCKLIST = {
    "acnh",
    "aov",
    "cod",
    "cs2",
    "fc24",
    "gt7",
    "lol",
    "mk8",
    "mw3",
    "pc",
    "ps5",
    "rov",
    "ssb",
    "tk8",
    "vlr",
    "vr",
    "wz",
}

TOKEN_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9:+.'_-]*|[\u0E00-\u0E7F]+")


@dataclass(frozen=True)
class GameAliasEntry:
    game: str
    alias: str
    compact: str


@dataclass(frozen=True)
class GameTitleCorrection:
    original_text: str
    corrected_text: str
    matched_text: str
    game: str
    alias: str
    score: float


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(value, dict):
                rows.append(value)
    return rows


@lru_cache(maxsize=8192)
def _compact(value: str) -> str:
    normalized = (value or "").strip().translate(THAI_DIGIT_TRANS).lower()
    return re.sub(r"[^0-9a-z\u0E00-\u0E7F]+", "", normalized)


def _canonical_game_name(value: str) -> str:
    clean = re.sub(r"\s+", " ", (value or "").strip())
    clean = re.sub(r"\s+Standard Edition$", "", clean, flags=re.IGNORECASE)
    return clean


def _looks_like_game_alias(alias: str, game: str) -> bool:
    alias_compact = _compact(alias)
    game_compact = _compact(game)
    if not alias_compact or not game_compact:
        return False
    if alias_compact in game_compact or game_compact in alias_compact:
        return True
    if len(alias_compact) <= 4:
        return True
    alias_words = re.findall(r"[A-Za-z0-9]+", alias)
    game_words = re.findall(r"[A-Za-z0-9]+", game)
    if alias_words and game_words and len(alias_words) >= 2:
        return alias_words[0].lower() == game_words[0].lower()
    return False


def _aliases_from_row(row: dict[str, Any]) -> tuple[str, set[str]]:
    game = _canonical_game_name(str(row.get("game") or row.get("title") or "").strip())
    aliases: set[str] = set()
    if game:
        aliases.add(game)
    title = str(row.get("title") or "").strip()
    if title:
        aliases.add(title)
    for alias in row.get("aliases") or []:
        alias_text = str(alias or "").strip()
        if alias_text:
            if row.get("category") == "game_controls":
                if re.search(r"[:=]", alias_text) or "controls on" in alias_text.lower():
                    continue
                if not _looks_like_game_alias(alias_text, game or title):
                    continue
            aliases.add(alias_text)
    for alias in tuple(aliases):
        if re.search(r"\bpart ii\b", alias, flags=re.IGNORECASE):
            aliases.add(re.sub(r"\bpart ii\b", "Part 2", alias, flags=re.IGNORECASE))
            aliases.add(re.sub(r"\bpart ii\b", "Part ll", alias, flags=re.IGNORECASE))
            aliases.add(re.sub(r"\bpart ii\b", "Part OI", alias, flags=re.IGNORECASE))
        if re.search(r"\bpart i\b", alias, flags=re.IGNORECASE):
            aliases.add(re.sub(r"\bpart i\b", "Part 1", alias, flags=re.IGNORECASE))
    return game or title, aliases


@lru_cache(maxsize=1)
def game_alias_entries() -> tuple[GameAliasEntry, ...]:
    entries: dict[tuple[str, str], GameAliasEntry] = {}
    for filename in GAME_TITLE_FILES:
        for row in _read_jsonl(CURATED_DIR / filename):
            game, aliases = _aliases_from_row(row)
            if not game:
                continue
            for alias in aliases:
                compact = _compact(alias)
                if compact:
                    entries[(game.lower(), compact)] = GameAliasEntry(game, alias, compact)
    for label, aliases in BROAD_TITLE_ALIASES.items():
        for alias in aliases:
            compact = _compact(alias)
            if compact:
                entries[(label.lower(), compact)] = GameAliasEntry(label, alias, compact)
    return tuple(sorted(entries.values(), key=lambda item: len(item.compact), reverse=True))


@lru_cache(maxsize=1)
def _broad_compacts() -> frozenset[str]:
    values: set[str] = set()
    for aliases in BROAD_TITLE_ALIASES.values():
        values.update(_compact(alias) for alias in aliases if _compact(alias))
    return frozenset(values)


@lru_cache(maxsize=1)
def _specific_alias_needles() -> tuple[str, ...]:
    needles: list[str] = []
    seen: set[str] = set()
    for entry in game_alias_entries():
        if _is_broad_entry(entry) or len(entry.compact) < 8:
            continue
        if entry.compact in seen:
            continue
        seen.add(entry.compact)
        needles.append(entry.compact)
    return tuple(sorted(needles, key=len, reverse=True))


def _ratio(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


def _char_ngrams(value: str, n: int = 3) -> set[str]:
    if not value:
        return set()
    padded = f" {value} "
    if len(padded) <= n:
        return {padded}
    return {padded[index:index + n] for index in range(len(padded) - n + 1)}


def _ngram_score(a: str, b: str) -> float:
    grams_a = _char_ngrams(a)
    grams_b = _char_ngrams(b)
    if not grams_a or not grams_b:
        return 0.0
    return len(grams_a & grams_b) / len(grams_a | grams_b)


def _delete_depth(value: str) -> int:
    if len(value) <= 6:
        return 1
    return 2


@lru_cache(maxsize=4096)
def _delete_keys(value: str, max_deletes: int) -> frozenset[str]:
    if not value:
        return frozenset()
    keys = {value}
    current = {value}
    for _step in range(max_deletes):
        next_values: set[str] = set()
        for item in current:
            if len(item) <= 2:
                continue
            for index in range(len(item)):
                deleted = item[:index] + item[index + 1:]
                if len(deleted) >= 3:
                    next_values.add(deleted)
        keys.update(next_values)
        current = next_values
    return frozenset(keys)


@lru_cache(maxsize=1)
def _delete_index() -> dict[str, tuple[GameAliasEntry, ...]]:
    index: dict[str, dict[tuple[str, str], GameAliasEntry]] = {}
    for entry in game_alias_entries():
        if not _eligible_alias(entry):
            continue
        if len(entry.compact) > 32:
            continue
        for key in _delete_keys(entry.compact, _delete_depth(entry.compact)):
            if len(key) < 4:
                continue
            bucket = index.setdefault(key, {})
            bucket[(entry.game.lower(), entry.compact)] = entry
    return {key: tuple(bucket.values()) for key, bucket in index.items()}


def _delete_hit_score(candidate_compact: str, alias_compact: str) -> float:
    candidate_keys = _delete_keys(candidate_compact, _delete_depth(candidate_compact))
    alias_keys = _delete_keys(alias_compact, _delete_depth(alias_compact))
    if not candidate_keys or not alias_keys:
        return 0.0
    overlap = candidate_keys & alias_keys
    if not overlap:
        return 0.0
    overlap_ratio = len(overlap) / max(1, min(len(candidate_keys), len(alias_keys)))
    return min(0.94, 0.80 + (overlap_ratio * 0.20))


def _candidate_entries(candidate_compact: str) -> tuple[GameAliasEntry, ...]:
    hits: dict[tuple[str, str], GameAliasEntry] = {}
    for key in _delete_keys(candidate_compact, _delete_depth(candidate_compact)):
        for entry in _delete_index().get(key, ()):
            hits[(entry.game.lower(), entry.compact)] = entry
    if not hits:
        first = candidate_compact[:1]
        for entry in game_alias_entries():
            if not entry.compact.startswith(first):
                continue
            if abs(len(entry.compact) - len(candidate_compact)) > max(5, len(entry.compact) // 2):
                continue
            hits[(entry.game.lower(), entry.compact)] = entry
    return tuple(hits.values())


def _combined_score(candidate_compact: str, alias_compact: str) -> float:
    ratio_score = _ratio(candidate_compact, alias_compact)
    ngram_score = _ngram_score(candidate_compact, alias_compact)
    delete_score = _delete_hit_score(candidate_compact, alias_compact)
    combined = ratio_score
    if ngram_score >= 0.45 and ratio_score >= 0.68:
        combined = max(combined, min(0.96, (ratio_score * 0.70) + (ngram_score * 0.30) + 0.05))
    if delete_score and ratio_score >= 0.66:
        combined = max(combined, min(0.96, max(delete_score, ratio_score + 0.04)))
    return combined


def _threshold(alias_len: int, candidate_len: int) -> float:
    if alias_len <= 6:
        base = 0.80
    elif alias_len <= 9:
        base = 0.78
    else:
        base = 0.74
    if abs(alias_len - candidate_len) > max(3, alias_len // 3):
        base += 0.04
    return base


def _eligible_alias(entry: GameAliasEntry) -> bool:
    compact = entry.compact
    if len(compact) < 5:
        return False
    if compact in FUZZY_SHORT_ALIAS_BLOCKLIST:
        return False
    return bool(re.search(r"[A-Za-z]", entry.alias) and re.search(r"[a-z]", compact)) or bool(re.search(r"[\u0E00-\u0E7F]", entry.alias))


def _eligible_candidate(compact: str) -> bool:
    if len(compact) < 5:
        return False
    if not re.search(r"[a-z\u0E00-\u0E7F]", compact):
        return False
    if compact in FUZZY_SHORT_ALIAS_BLOCKLIST:
        return False
    return True


def _has_thai(value: str) -> bool:
    return bool(re.search(r"[\u0E00-\u0E7F]", value or ""))


@lru_cache(maxsize=1)
def _thai_alias_prefixes() -> frozenset[str]:
    prefixes: set[str] = set()
    generic_prefixes = {"เกม", "เกมส์", "เล่น", "วิธี"}
    for entry in game_alias_entries():
        if not _eligible_alias(entry) or not _has_thai(entry.compact):
            continue
        if len(entry.compact) >= 6:
            prefix = entry.compact[:4]
            if prefix not in generic_prefixes and not prefix.startswith("เกม"):
                prefixes.add(prefix)
    return frozenset(prefixes)


def _has_plausible_thai_title_signal(compact: str) -> bool:
    if not _has_thai(compact):
        return False
    return any(prefix in compact for prefix in _thai_alias_prefixes())


def _compact_windows(value: str, alias_len: int) -> tuple[str, ...]:
    if not value or alias_len <= 0:
        return ()
    min_len = max(5, alias_len - 2)
    max_len = min(len(value), alias_len + 2)
    if min_len > max_len:
        return ()
    windows: set[str] = set()
    if min_len <= len(value) <= max_len:
        windows.add(value)
    for size in range(min_len, max_len + 1):
        if size > len(value):
            continue
        for start in range(0, len(value) - size + 1):
            windows.add(value[start:start + size])
    return tuple(windows)


def _compact_thai_correction(raw: str) -> GameTitleCorrection | None:
    q_compact = _compact(raw)
    if not _has_thai(q_compact):
        return None
    best: tuple[float, int, str, GameAliasEntry] | None = None
    second_best_score = 0.0
    for entry in game_alias_entries():
        if not _eligible_alias(entry) or not _has_thai(entry.compact):
            continue
        alias_compact = entry.compact
        if len(alias_compact) < 5:
            continue
        if len(alias_compact) >= 6 and alias_compact[:4] not in q_compact:
            continue
        if _is_exact_broad_compact(q_compact):
            continue
        for window in _compact_windows(q_compact, len(alias_compact)):
            if not re.match(r"[\u0E00-\u0E7F]", window):
                continue
            if window == alias_compact:
                score = 1.0
            else:
                if abs(len(alias_compact) - len(window)) > 2:
                    continue
                score = _combined_score(window, alias_compact)
            if score < 0.82:
                continue
            if score < 0.90 and window[0] != alias_compact[0]:
                continue
            rank = (round(score, 3), len(window), len(alias_compact))
            best_rank = (-1.0, -1, -1) if best is None else (round(best[0], 3), len(best[2]), len(best[3].compact))
            if best is None or rank > best_rank:
                if best is not None and not _same_game_or_family(best[3], entry):
                    second_best_score = max(second_best_score, best[0])
                best = (score, len(alias_compact), window, entry)
            elif best is not None and not _same_game_or_family(best[3], entry):
                second_best_score = max(second_best_score, score)
    if best is None:
        return None
    score, _alias_len, matched_text, entry = best
    if score < 0.90 and second_best_score and score - second_best_score < 0.04:
        return None
    corrected = f"{raw} {entry.game}".strip()
    return GameTitleCorrection(
        original_text=raw,
        corrected_text=corrected,
        matched_text=matched_text,
        game=entry.game,
        alias=entry.alias,
        score=score,
    )


def _is_broad_entry(entry: GameAliasEntry) -> bool:
    aliases = BROAD_TITLE_ALIASES.get(entry.game)
    return bool(aliases and entry.alias in aliases)


def _same_game_or_family(left: GameAliasEntry, right: GameAliasEntry) -> bool:
    if left.game == right.game:
        return True
    if _is_broad_entry(left) and left.game.lower() in right.game.lower():
        return True
    if _is_broad_entry(right) and right.game.lower() in left.game.lower():
        return True
    return False


def _is_exact_broad_compact(compact: str) -> bool:
    return compact in _broad_compacts()


def _contains_exact_specific_alias(raw: str) -> bool:
    q_compact = _compact(raw)
    for needle in _specific_alias_needles():
        if needle in q_compact:
            return True
    return False


def _token_windows(text: str) -> list[tuple[int, int, str, str]]:
    tokens = list(TOKEN_RE.finditer(text))
    windows: list[tuple[int, int, str, str]] = []
    for start_index, start_token in enumerate(tokens):
        for end_index in range(start_index, min(len(tokens), start_index + 4)):
            end_token = tokens[end_index]
            raw = text[start_token.start():end_token.end()]
            compact = _compact(raw)
            if _eligible_candidate(compact):
                windows.append((start_token.start(), end_token.end(), raw, compact))
    return windows


def _passes_shape_guard(candidate_compact: str, alias_compact: str, score: float) -> bool:
    if (
        alias_compact.startswith(candidate_compact)
        and 0 < len(alias_compact) - len(candidate_compact) <= 2
    ):
        return False
    if len(alias_compact) <= 6:
        if candidate_compact[0] != alias_compact[0]:
            return False
        same_tail = candidate_compact[-1] == alias_compact[-1]
        same_prefix = len(candidate_compact) >= 4 and candidate_compact[:4] == alias_compact[:4]
        same_digit_shape = any(ch.isdigit() for ch in candidate_compact) and any(ch.isdigit() for ch in alias_compact)
        if not (same_tail or same_prefix or same_digit_shape or score >= 0.90):
            return False
    if score >= 0.90:
        return True
    if candidate_compact[0] == alias_compact[0]:
        return True
    candidate_has_digit = any(ch.isdigit() for ch in candidate_compact)
    alias_has_digit = any(ch.isdigit() for ch in alias_compact)
    return candidate_has_digit and alias_has_digit and score >= 0.82


def detect_game_title_correction(query: str) -> GameTitleCorrection | None:
    raw = re.sub(r"\s+", " ", (query or "").strip())
    if not raw:
        return None
    q_compact = _compact(raw)
    has_latin = bool(re.search(r"[A-Za-z]", raw))
    if _has_thai(q_compact) and not has_latin and not _has_plausible_thai_title_signal(q_compact):
        return None
    if _contains_exact_specific_alias(raw):
        return None

    compact_correction = _compact_thai_correction(raw)
    if compact_correction is not None:
        return compact_correction

    best: tuple[float, int, int, int, str, GameAliasEntry] | None = None
    second_best_score = 0.0
    for start, end, matched_text, candidate_compact in _token_windows(raw):
        for entry in _candidate_entries(candidate_compact):
            if not _eligible_alias(entry):
                continue
            alias_compact = entry.compact
            if candidate_compact == alias_compact:
                continue
            if _is_exact_broad_compact(candidate_compact) and not _is_broad_entry(entry):
                continue
            if abs(len(alias_compact) - len(candidate_compact)) > max(5, len(alias_compact) // 2):
                continue
            score = _combined_score(candidate_compact, alias_compact)
            if score < _threshold(len(alias_compact), len(candidate_compact)):
                continue
            if not _passes_shape_guard(candidate_compact, alias_compact, score):
                continue
            broad_bonus = 1 if _is_broad_entry(entry) and not any(ch.isdigit() for ch in candidate_compact) else 0
            candidate_rank = (round(score, 3), broad_bonus, len(candidate_compact), len(alias_compact))
            best_broad_bonus = 0
            if best is not None:
                best_broad_bonus = 1 if _is_broad_entry(best[5]) and not any(ch.isdigit() for ch in candidate_compact) else 0
            best_rank = (-1.0, -1, -1, -1) if best is None else (round(best[0], 3), best_broad_bonus, best[3], len(best[5].compact))
            same_game_longer_match = (
                best is not None
                and best[5].game == entry.game
                and len(candidate_compact) > best[3]
                and score >= best[0] - 0.05
            )
            if best is None or same_game_longer_match or candidate_rank > best_rank:
                if best is not None and not _same_game_or_family(best[5], entry):
                    second_best_score = max(second_best_score, best[0])
                best = (score, start, end, len(candidate_compact), matched_text, entry)
            elif best is not None and not _same_game_or_family(best[5], entry):
                second_best_score = max(second_best_score, score)

    if best is None:
        return None
    score, start, end, _candidate_len, matched_text, entry = best
    protected_service_entities = {
        "nintendoswitch",
        "playstation",
        "playstation5",
        "ps5",
        "pc",
        "vr",
        "cockpit",
    }
    if _compact(matched_text) in protected_service_entities:
        return None
    if score < 0.90 and second_best_score and score - second_best_score < 0.03:
        return None
    corrected = (raw[:start] + entry.game + raw[end:]).strip()
    if corrected.lower() == raw.lower():
        return None
    return GameTitleCorrection(
        original_text=raw,
        corrected_text=corrected,
        matched_text=matched_text,
        game=entry.game,
        alias=entry.alias,
        score=score,
    )


def build_game_title_query_variants(query: str, *, limit: int = 3) -> tuple[str, ...]:
    correction = detect_game_title_correction(query)
    if correction is None:
        return ()
    variants = [
        correction.corrected_text,
        f"{correction.original_text} {correction.game}",
    ]
    output: list[str] = []
    seen: set[str] = set()
    for variant in variants:
        clean = re.sub(r"\s+", " ", variant).strip()
        key = clean.lower()
        if clean and key not in seen:
            seen.add(key)
            output.append(clean)
        if len(output) >= limit:
            break
    return tuple(output)
