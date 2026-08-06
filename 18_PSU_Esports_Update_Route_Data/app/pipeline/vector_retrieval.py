from __future__ import annotations

import hashlib
import json
import math
import re
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
from typing import Any

from app.core.normalization import normalize_text
from app.pipeline.retrieval import hit_from_curated, load_curated_rows
from app.pipeline.schemas import PipelineRoute, PipelineTrace


ROOT = Path(__file__).resolve().parents[2]
VECTOR_DIR = ROOT / "data" / "vector"
VECTOR_INDEX_PATH = VECTOR_DIR / "psu_hybrid_vector_index.json"

VECTOR_BACKEND = "local_hash_char_ngram_v1"
VECTOR_DIM = 2048

DOMAIN_STOP_TOKENS = {
    "psu", "esports", "studio", "phuket", "game", "games", "เกม", "เล่น", "วิธี", "สอน",
    "คือ", "อะไร", "ยังไง", "อย่างไร", "ได้", "ไหม", "มั้ย", "ครับ", "ค่ะ", "คะ",
    "zone", "โซน", "pc", "vr", "ps5", "playstation", "nintendo", "switch",
}

DETAIL_INTENT_TERMS = (
    "คืออะไร", "อะไรคือ", "เกมอะไร", "แนวอะไร", "เกี่ยวกับอะไร",
    "เล่นยังไง", "เล่นอย่างไร", "วิธีเล่น", "เล่นแบบไหน", "สอนเล่น",
)

GAME_CONTROL_TERMS = (
    "ปุ่ม", "กดปุ่ม", "กดอะไร", "กดยังไง", "กดอย่างไร", "บังคับ", "ควบคุม",
    "จอย", "คอนโทรล", "คอนโทรลเลอร์", "อนาล็อก", "ปุ่มไหน", "ปุ่มอะไร",
    "button", "buttons", "control", "controls", "controller", "key mapping",
    "l1", "l2", "r1", "r2", "l3", "r3", "d-pad", "dpad", "analog",
)

SHORT_GAME_CONTROL_TOKENS = {"l1", "l2", "r1", "r2", "l3", "r3"}

FULL_GAME_CONTROL_TERMS = (
    "ปุ่มทั้งหมด", "ทั้งหมด", "ทุกปุ่ม", "ปุ่มครบ", "ปุ่มควบคุม", "มีอะไรบ้าง",
    "มีปุ่มอะไร", "มีปุ่มอะไรบ้าง", "ปุ่มอะไร", "ปุ่มอะไรบ้าง", "ปุ่มไหนบ้าง",
    "ปุ่มหลัก", "ปุ่มหลักๆ", "ปุ่มหลัก ๆ", "ปุ่มของเกม", "ปุ่มในเกม",
    "ใช้จอยยังไง", "ใช้จอยอย่างไร", "วิธีใช้จอย", "วิธีใช้ controller",
    "วิธีใช้คอนโทรล", "controller", "controllers", "controls", "buttons",
    "key mapping", "button mapping",
)


def _stable_bucket(text: str) -> str:
    digest = hashlib.blake2b(text.encode("utf-8"), digest_size=4).digest()
    return str(int.from_bytes(digest, "big") % VECTOR_DIM)


def _char_ngrams(text: str) -> list[str]:
    compact = re.sub(r"\s+", "", normalize_text(text))
    grams: list[str] = []
    for size in (3, 4, 5):
        if len(compact) < size:
            continue
        grams.extend(compact[index:index + size] for index in range(len(compact) - size + 1))
    return grams


def _word_tokens(text: str) -> list[str]:
    normalized = normalize_text(text)
    return [
        token
        for token in re.split(r"[\s,./|()\[\]{}:;!?\"'’+-]+", normalized)
        if token and token not in DOMAIN_STOP_TOKENS
    ]


def embed_text(text: str) -> dict[str, float]:
    weights: dict[str, float] = {}
    for token in _word_tokens(text):
        bucket = "w:" + _stable_bucket(token)
        weights[bucket] = weights.get(bucket, 0.0) + 2.0
    for gram in _char_ngrams(text):
        bucket = "c:" + _stable_bucket(gram)
        weights[bucket] = weights.get(bucket, 0.0) + 1.0

    norm = math.sqrt(sum(value * value for value in weights.values()))
    if norm <= 0:
        return {}
    return {key: round(value / norm, 6) for key, value in weights.items()}


def _cosine_sparse(a: dict[str, float], b: dict[str, float]) -> float:
    if not a or not b:
        return 0.0
    if len(a) > len(b):
        a, b = b, a
    return sum(value * b.get(key, 0.0) for key, value in a.items())


def _doc_text(row: dict[str, Any]) -> str:
    parts = [
        str(row.get("title", "")),
        str(row.get("text", "")),
        str(row.get("game", "")),
        str(row.get("item", "")),
        str(row.get("zone", "")),
        " ".join(str(alias) for alias in row.get("aliases", []) if alias),
        " ".join(str(tag) for tag in row.get("tags", []) if tag),
    ]
    return "\n".join(part for part in parts if part.strip())


def _source_file(row: dict[str, Any]) -> str:
    return str(row.get("_source_file", "")).strip()


def _build_index_payload() -> dict[str, Any]:
    docs: list[dict[str, Any]] = []
    for row in load_curated_rows():
        text = _doc_text(row)
        vector = embed_text(text)
        if not vector:
            continue
        docs.append({
            "id": str(row.get("id", "")),
            "category": str(row.get("category", "")),
            "title": str(row.get("title") or row.get("game") or row.get("item") or row.get("id", "")),
            "text": str(row.get("text") or row.get("what_th") or ""),
            "source_url": str(row.get("source_url", "")),
            "source_file": _source_file(row),
            "game": str(row.get("game", "")),
            "aliases": [str(alias) for alias in row.get("aliases", []) if alias],
            "tags": [str(tag) for tag in row.get("tags", []) if tag],
            "priority": row.get("priority", 0),
            "vector": vector,
            "row": row,
        })
    return {
        "version": 1,
        "backend": VECTOR_BACKEND,
        "dim": VECTOR_DIM,
        "doc_count": len(docs),
        "docs": docs,
    }


def write_vector_index(path: Path = VECTOR_INDEX_PATH) -> dict[str, Any]:
    payload = _build_index_payload()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return payload


@lru_cache(maxsize=1)
def load_vector_index() -> dict[str, Any]:
    if VECTOR_INDEX_PATH.exists():
        try:
            return json.loads(VECTOR_INDEX_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return _build_index_payload()


def _query_terms(query: str) -> set[str]:
    terms = set(_word_tokens(query))
    compact = normalize_text(query).replace(" ", "")
    for term in list(terms):
        if len(term) >= 4:
            terms.add(term.replace(" ", ""))
    if compact:
        terms.add(compact)
    return {term for term in terms if term and term not in DOMAIN_STOP_TOKENS}


def _entity_score(query: str, doc: dict[str, Any]) -> float:
    q = normalize_text(query)
    query_terms = _query_terms(query)
    candidates = [
        str(doc.get("title", "")),
        str(doc.get("game", "")),
        *[str(alias) for alias in doc.get("aliases", [])],
    ]
    best = 0.0
    for raw in candidates:
        value = normalize_text(raw)
        if not value:
            continue
        value_compact = value.replace(" ", "")
        value_terms = set(_word_tokens(value))
        if value in q or value_compact in q.replace(" ", ""):
            exact_bonus = min(0.25, len(value_compact) / 80)
            best = max(best, 1.0 + exact_bonus)
        for term in query_terms:
            if len(term) < 3:
                continue
            if term in value or term in value_compact:
                best = max(best, min(0.96, max(0.45, len(term) / max(len(value_compact), 1))))
            elif term in value_terms:
                best = max(best, 0.9)
    return best


def _lexical_overlap(query: str, doc: dict[str, Any]) -> float:
    query_terms = _query_terms(query)
    if not query_terms:
        return 0.0
    doc_terms = _query_terms(_doc_text(doc.get("row", doc)))
    if not doc_terms:
        return 0.0
    return len(query_terms & doc_terms) / max(1, len(query_terms))


def _is_game_detail_intent(query: str, route: PipelineRoute) -> bool:
    q = normalize_text(query)
    return route.category == "games" and (
        route.intent in {"game_detail_lookup", "games_lookup"}
        or any(term in q for term in DETAIL_INTENT_TERMS)
    )


def looks_like_game_control_query(query: str) -> bool:
    q = normalize_text(query)
    if any(term in q for term in GAME_CONTROL_TERMS if term not in SHORT_GAME_CONTROL_TOKENS):
        return True
    # Short button names must be standalone tokens. Substring matching would
    # misread equipment names such as "PlayStation VR2" as the R2 button.
    return any(
        re.search(rf"(?<![0-9a-z]){re.escape(term)}(?![0-9a-z])", q) is not None
        for term in SHORT_GAME_CONTROL_TOKENS
    )


def _looks_like_full_game_control_query(query: str) -> bool:
    q = normalize_text(query)
    return any(normalize_text(term) in q for term in FULL_GAME_CONTROL_TERMS)


def _category_allowed(route: PipelineRoute, doc_category: str) -> bool:
    if route.category in {"general", "unknown", "no_answer"}:
        return False
    if route.category == doc_category:
        return True
    if doc_category == "game_controls" and route.category in {"games", "equipment"}:
        return True
    if route.category == "games" and doc_category == "knowledge" and route.intent == "knowledge_lookup":
        return True
    return False


def _guard_doc(query: str, route: PipelineRoute, doc: dict[str, Any], vector_score: float, lexical: float, entity: float) -> tuple[bool, str]:
    category = str(doc.get("category", ""))
    if not _category_allowed(route, category):
        return False, "category_mismatch"
    if category == "competition_rules" and route.category != "competition_rules":
        return False, "competition_context_blocked"
    if category == "game_controls":
        if not looks_like_game_control_query(query):
            return False, "game_controls_requires_control_terms"
        if entity < 0.35 and (vector_score < 0.35 or lexical < 0.18):
            return False, "weak_game_control_entity"
        if vector_score < 0.16 and lexical < 0.18:
            return False, "weak_game_control_similarity"
        return True, "ok_game_control"
    if _is_game_detail_intent(query, route):
        if category != "games":
            return False, "game_detail_requires_game_doc"
        if entity < 0.45:
            return False, "weak_game_entity"
        if vector_score < 0.20 and lexical < 0.20:
            return False, "weak_game_similarity"
        return True, "ok_game_entity"
    if route.category == "games" and route.intent in {"game_availability_lookup", "game_catalog_lookup"}:
        if category != "games":
            return False, "game_route_requires_game_doc"
        if entity < 0.40 and vector_score < 0.32:
            return False, "weak_game_route_match"
        return True, "ok_game_route"
    if vector_score >= 0.30 or lexical >= 0.34:
        return True, "ok_context"
    return False, "below_threshold"


def retrieve_vector_guarded(query: str, route: PipelineRoute, limit: int = 3) -> tuple[list[dict[str, Any]], PipelineTrace]:
    index = load_vector_index()
    query_vector = embed_text(query)
    scored: list[tuple[float, dict[str, Any], str]] = []
    blocked: dict[str, int] = {}

    for doc in index.get("docs", []):
        vector_score = _cosine_sparse(query_vector, doc.get("vector", {}))
        lexical = _lexical_overlap(query, doc)
        entity = _entity_score(query, doc)
        ok, reason = _guard_doc(query, route, doc, vector_score, lexical, entity)
        if not ok:
            blocked[reason] = blocked.get(reason, 0) + 1
            continue
        priority = float(doc.get("priority", 0) or 0) / 100.0
        score = (vector_score * 10.0) + (lexical * 3.0) + (entity * 5.0) + priority
        row = dict(doc.get("row", {}))
        row.update({
            "_score": round(score, 3),
            "_vector_score": round(vector_score, 4),
            "_lexical_score": round(lexical, 4),
            "_entity_score": round(entity, 4),
            "_source_file": doc.get("source_file", ""),
            "_vector_backend": VECTOR_BACKEND,
        })
        scored.append((score, row, reason))

    scored.sort(key=lambda item: item[0], reverse=True)
    hits = [row for _, row, _ in scored[:limit]]
    confidence = min(0.90, 0.50 + (hits[0]["_score"] / 20 if hits else 0.0))
    detail = f"hits={len(hits)} backend={VECTOR_BACKEND}"
    if hits:
        detail += (
            f" top={hits[0].get('id')} score={hits[0].get('_score')} "
            f"v={hits[0].get('_vector_score')} e={hits[0].get('_entity_score')}"
        )
    elif blocked:
        top_blocks = ", ".join(f"{key}:{value}" for key, value in sorted(blocked.items())[:4])
        detail += f" blocked={top_blocks}"
    return hits, PipelineTrace(
        "vector_retrieval",
        "guarded_hybrid_vector",
        confidence,
        detail,
        {"category": route.category, "intent": route.intent, "backend": VECTOR_BACKEND},
    )


def answer_from_vector_hits(hits: list[dict[str, Any]], query: str = "") -> tuple[str | None, list[dict[str, Any]], float]:
    if not hits:
        return None, [], 0.0
    best = hits[0]
    score = float(best.get("_score", 0.0))
    if score < 4.0:
        return None, [], min(0.55, score / 10)
    if best.get("category") == "game_controls":
        answer = _answer_from_game_control_hits(hits, query)
    else:
        answer = str(best.get("text", "")).strip()
    if not answer:
        return None, [], 0.0
    if answer.startswith("ยังไม่แน่ใจว่าหมายถึงเกมไหน"):
        return answer, [], 0.56
    source_url = str(best.get("source_url", "")).strip()
    if (
        source_url
        and "แหล่งข้อมูล:" not in answer
        and not answer.startswith("ยังไม่พบข้อมูลปุ่มควบคุม")
        and not answer.startswith("ยังไม่แน่ใจว่าหมายถึงเกมไหน")
    ):
        answer = answer.rstrip() + f"\nแหล่งข้อมูล: {source_url}"
    confidence = min(0.88, 0.58 + score / 24)
    return answer, [hit_from_curated(row) for row in hits[:2]], confidence


def _all_game_control_rows(game: str, platform: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row in load_curated_rows():
        if row.get("category") != "game_controls":
            continue
        row_game = str(row.get("game") or "").strip()
        if row_game != game and not _same_game(row_game, game):
            continue
        if platform and str(row.get("platform") or "").strip() != platform:
            continue
        if not row.get("button"):
            continue
        rows.append(row)
    return rows


@lru_cache(maxsize=1)
def _game_alias_index() -> tuple[tuple[str, str, str], ...]:
    entries: list[tuple[str, str, str]] = []
    for row in load_curated_rows():
        game = str(row.get("game") or row.get("title") or "").strip()
        if not game:
            continue
        aliases = [game, *[str(alias) for alias in row.get("aliases", []) if alias]]
        for alias in aliases:
            normalized = normalize_text(alias)
            compact = normalized.replace(" ", "")
            if len(compact) < 4:
                continue
            entries.append((game, normalized, compact))
    entries.sort(key=lambda item: len(item[2]), reverse=True)
    seen: set[tuple[str, str]] = set()
    unique: list[tuple[str, str, str]] = []
    for game, normalized, compact in entries:
        key = (game, compact)
        if key in seen:
            continue
        seen.add(key)
        unique.append((game, normalized, compact))
    return tuple(unique)


def _explicit_game_hint(query: str) -> str | None:
    q = normalize_text(query)
    q_compact = q.replace(" ", "")
    for game, normalized, compact in _game_alias_index():
        if normalized and normalized in q:
            return game
        if compact and compact in q_compact:
            return game
    return None


def has_explicit_game_hint(query: str) -> bool:
    return _explicit_game_hint(query) is not None


def _same_game(left: str, right: str) -> bool:
    return normalize_text(left).replace(" ", "") == normalize_text(right).replace(" ", "")


def _section_label(section: str) -> str:
    value = str(section or "").strip()
    labels = {
        "Driving Controls": "ขณะขับ",
        "Pause Menu Shortcuts": "เมนู Pause",
    }
    return labels.get(value, value)


def _format_game_control_line(row: dict[str, Any]) -> str:
    button = str(row.get("button") or "").strip()
    action = str(row.get("action_th") or row.get("action_en") or "").strip()
    description = str(row.get("description_th") or "").strip()
    line = f"- {button}: {action}" if action else f"- {button}"
    if description:
        line += f" - {description}"
    return line


def _format_game_control_rows(game: str, platform: str, rows: list[dict[str, Any]], source_url: str = "") -> str:
    lines = [f"{game} บน {platform} มีปุ่มควบคุมดังนี้:"]
    has_sections = any(str(row.get("section") or "").strip() for row in rows)
    if has_sections:
        current_section = ""
        for row in rows:
            section = _section_label(str(row.get("section") or "").strip())
            if section and section != current_section:
                if len(lines) > 1:
                    lines.append("")
                lines.append(f"{section}:")
                current_section = section
            lines.append(_format_game_control_line(row))
    else:
        for row in rows:
            lines.append(_format_game_control_line(row))
    if source_url:
        lines.append(f"แหล่งข้อมูล: {source_url}")
    return "\n".join(lines)


def _control_match_fragments(value: str) -> list[str]:
    normalized = normalize_text(value)
    if not normalized:
        return []
    fragments = [normalized]
    fragments.extend(
        part.strip()
        for part in re.split(r"[/,|()]+", normalized)
        if len(part.strip()) >= 2
    )
    for prefix in ("ลูก", "ปุ่ม", "การ"):
        if normalized.startswith(prefix) and len(normalized) > len(prefix) + 1:
            fragments.append(normalized[len(prefix):].strip())
    return _unique_fragments(fragments)


def _unique_fragments(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if not value or value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result


def _focused_game_control_rows(rows: list[dict[str, Any]], query: str) -> list[dict[str, Any]]:
    q = normalize_text(query)
    if not q:
        return []
    focused: list[dict[str, Any]] = []
    for row in rows:
        fragments: list[str] = []
        fragments.extend(_control_match_fragments(str(row.get("action_th") or "")))
        fragments.extend(_control_match_fragments(str(row.get("action_en") or "")))
        button = normalize_text(str(row.get("button") or ""))
        if button and (len(button) > 1 or f"ปุ่ม{button}" in q or f"button{button}" in q):
            fragments.append(button)
        description = normalize_text(str(row.get("description_th") or ""))
        fragments = _unique_fragments([fragment for fragment in fragments if len(fragment) >= 2])
        if any(fragment in q for fragment in fragments) or (description and any(fragment in description for fragment in fragments if fragment in q)):
            focused.append(row)
    return focused


def _answer_from_game_control_hits(hits: list[dict[str, Any]], query: str = "") -> str:
    explicit_game = _explicit_game_hint(query)
    if explicit_game:
        explicit_rows = _all_game_control_rows(explicit_game, "")
        if not explicit_rows:
            return (
                f"ยังไม่พบข้อมูลปุ่มควบคุมของ {explicit_game} ที่ยืนยันได้ในฐานข้อมูลตอนนี้ครับ\n"
                "ถ้าต้องการข้อมูลเกมนี้เพิ่มเติม สามารถถามเรื่องแนวเกม วิธีเล่นโดยสรุป หรือโซนที่เล่นได้แทนได้ครับ"
            )
        explicit_game = str(explicit_rows[0].get("game") or explicit_game).strip()
        explicit_platform = str(explicit_rows[0].get("platform") or "").strip()
        wants_full_list = _looks_like_full_game_control_query(query)
        if wants_full_list:
            return _format_game_control_rows(explicit_game, explicit_platform, explicit_rows, str(explicit_rows[0].get("source_url") or ""))
        focused_rows = _focused_game_control_rows(explicit_rows, query)
        if focused_rows:
            lines = [f"{explicit_game} บน {explicit_platform} ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้:"]
            lines.extend(_format_game_control_line(row) for row in focused_rows)
            source_url = str(focused_rows[0].get("source_url") or "").strip()
            if source_url:
                lines.append(f"แหล่งข้อมูล: {source_url}")
            return "\n".join(lines)

    if not explicit_game:
        return (
            "ยังไม่แน่ใจว่าหมายถึงเกมไหนครับ จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน\n"
            "ให้พิมพ์ชื่อเกมมาด้วย เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง`, `Mario Kart 8 Deluxe ใช้จอยยังไง` "
            "หรือถ้าเพิ่งถามชื่อเกมไปก่อนหน้า ให้ถามต่อใน session เดิมได้ครับ"
        )

    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for hit in hits:
        game_key = str(hit.get("game") or "").strip()
        platform_key = str(hit.get("platform") or "").strip()
        if game_key:
            grouped[(game_key, platform_key)].append(hit)

    if grouped:
        selected_hits = max(
            grouped.values(),
            key=lambda rows: (
                sum(float(row.get("_score", 0.0)) for row in rows[:6]),
                max(float(row.get("_entity_score", 0.0)) for row in rows),
                len(rows),
            ),
        )
        hits = sorted(selected_hits, key=lambda row: float(row.get("_score", 0.0)), reverse=True)

    best = hits[0]
    game = str(best.get("game") or "").strip()
    platform = str(best.get("platform") or "").strip()
    source_url = str(best.get("source_url") or "").strip()
    wants_full_list = _looks_like_full_game_control_query(query)

    if wants_full_list or (best.get("control_count") and not best.get("button")):
        rows = _all_game_control_rows(game, platform)
        if rows:
            return _format_game_control_rows(game, platform, rows, source_url)

    if best.get("control_count") and not best.get("button"):
        answer = f"{game} บน {platform} มีข้อมูลปุ่มควบคุม {best.get('control_count')} รายการ"
        note = str(best.get("note") or "").strip()
        if note:
            answer += f"\nหมายเหตุ: {note}"
        answer += "\nถ้าต้องการถามปุ่มเฉพาะ ให้ถามได้ เช่น ปุ่มกระโดด ปุ่มโจมตี หรือปุ่มเปิดเมนู"
        return answer

    rows = [
        row for row in hits
        if row.get("category") == "game_controls"
        and str(row.get("game") or "").strip() == game
        and row.get("button")
    ]
    if not rows:
        return str(best.get("text") or "").strip()
    focused_rows = _focused_game_control_rows(rows, query)
    if focused_rows:
        rows = focused_rows

    lines = [f"{game} บน {platform} ใช้ปุ่มหลักที่เกี่ยวข้องดังนี้:"]
    for row in rows:
        lines.append(_format_game_control_line(row))
    if source_url:
        lines.append(f"แหล่งข้อมูล: {source_url}")
    return "\n".join(lines)
