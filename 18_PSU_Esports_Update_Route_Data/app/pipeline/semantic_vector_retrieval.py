from __future__ import annotations

import hashlib
import json
import math
import os
import time
from dataclasses import dataclass
from datetime import date, datetime
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable

from app.core.normalization import normalize_text
from app.pipeline.request_deadline import remaining_sec
from app.pipeline.retrieval import hit_from_curated, load_curated_rows
from app.pipeline.schemas import PipelineRoute, PipelineTrace
from app.pipeline.semantic_embeddings import (
    embed_query,
    embed_texts,
    embedding_model_name,
    semantic_retrieval_enabled,
)
from app.pipeline.vector_retrieval import _lexical_overlap


ROOT = Path(__file__).resolve().parents[2]
SEMANTIC_INDEX_PATH = ROOT / "data" / "vector" / "psu_semantic_vector_index.json"
DYNAMIC_KNOWLEDGE_FILE = "dynamic_knowledge.jsonl"

DEFAULT_INDEX_CATEGORIES = {
    "games",
    "equipment",
    "knowledge",
    "events_news",
    "about_us",
}
TRUST_RANK = {
    "official": 4,
    "user_confirmed": 3,
    "internal_verified": 2,
    "secondary": 1,
    "": 0,
}


@dataclass(frozen=True)
class SemanticIndexBuildResult:
    path: Path
    doc_count: int
    dimensions: int
    model: str
    elapsed_sec: float
    embedding_elapsed_sec: float
    source_fingerprint: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "path": str(self.path),
            "doc_count": self.doc_count,
            "dimensions": self.dimensions,
            "model": self.model,
            "elapsed_sec": round(self.elapsed_sec, 4),
            "embedding_elapsed_sec": round(self.embedding_elapsed_sec, 4),
            "source_fingerprint": self.source_fingerprint,
        }


def _configured_categories() -> set[str]:
    raw = os.getenv("PSU_SEMANTIC_INDEX_CATEGORIES", "")
    if not raw.strip():
        return set(DEFAULT_INDEX_CATEGORIES)
    return {value.strip() for value in raw.split(",") if value.strip()}


def _doc_text(row: dict[str, Any]) -> str:
    parts = [
        str(row.get("title") or ""),
        str(row.get("text") or row.get("answer") or row.get("what_th") or ""),
        str(row.get("game") or ""),
        str(row.get("item") or ""),
        str(row.get("zone") or ""),
        " ".join(str(alias) for alias in row.get("aliases", []) if alias),
        " ".join(str(tag) for tag in row.get("tags", []) if tag),
    ]
    return "\n".join(part.strip() for part in parts if part.strip())


def _source_fingerprint(rows: Iterable[dict[str, Any]]) -> str:
    digest = hashlib.sha256()
    for row in rows:
        digest.update(str(row.get("id") or "").encode("utf-8"))
        digest.update(b"\0")
        digest.update(_doc_text(row).encode("utf-8"))
        digest.update(b"\0")
    return digest.hexdigest()


def _atomic_write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    temporary.replace(path)


def _eligible_rows(rows: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    categories = _configured_categories()
    selected: list[dict[str, Any]] = []
    seen: set[str] = set()
    for source_row in rows:
        row = dict(source_row)
        row_id = str(row.get("id") or "").strip()
        category = str(row.get("category") or "").strip()
        status = str(row.get("status") or "published").strip().lower()
        text = _doc_text(row)
        if not row_id or row_id in seen or category not in categories or not text:
            continue
        if status != "published":
            continue
        seen.add(row_id)
        selected.append(row)
    selected.sort(key=lambda row: str(row.get("id") or ""))
    return selected


def build_semantic_index(
    *,
    path: Path = SEMANTIC_INDEX_PATH,
    rows: Iterable[dict[str, Any]] | None = None,
    batch_size: int | None = None,
    timeout_sec: float | None = None,
) -> SemanticIndexBuildResult:
    started = time.perf_counter()
    selected = _eligible_rows(rows if rows is not None else load_curated_rows())
    if not selected:
        raise ValueError("no eligible rows found for semantic index")

    size = max(1, int(batch_size or os.getenv("PSU_EMBEDDING_BATCH_SIZE", "16")))
    configured_timeout = float(
        timeout_sec
        if timeout_sec is not None
        else os.getenv("PSU_EMBEDDING_INDEX_TIMEOUT_SEC", "180")
    )
    vectors: list[tuple[float, ...]] = []
    embedding_elapsed = 0.0
    dimensions = 0
    resolved_model = embedding_model_name()
    texts = [_doc_text(row) for row in selected]
    for offset in range(0, len(texts), size):
        batch = embed_texts(
            texts[offset:offset + size],
            timeout_sec=configured_timeout,
            keep_alive=os.getenv("PSU_EMBEDDING_KEEP_ALIVE", "10m"),
            apply_request_deadline=False,
        )
        embedding_elapsed += batch.elapsed_sec
        resolved_model = batch.model
        if dimensions and batch.dimensions != dimensions:
            raise ValueError("embedding dimensions changed while building semantic index")
        dimensions = batch.dimensions
        vectors.extend(batch.vectors)

    documents: list[dict[str, Any]] = []
    for row, text, vector in zip(selected, texts, vectors):
        documents.append({
            "id": str(row.get("id") or ""),
            "category": str(row.get("category") or ""),
            "title": str(row.get("title") or row.get("id") or ""),
            "text": str(row.get("text") or row.get("answer") or ""),
            "source_url": str(row.get("source_url") or ""),
            "source_file": str(row.get("_source_file") or ""),
            "dynamic": bool(
                row.get("dynamic_knowledge")
                or str(row.get("_source_file") or "") == DYNAMIC_KNOWLEDGE_FILE
            ),
            "embedding_text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            "vector": [round(float(value), 7) for value in vector],
            "row": row,
        })

    fingerprint = _source_fingerprint(selected)
    payload = {
        "version": 1,
        "backend": "ollama_dense_embedding_v1",
        "model": resolved_model,
        "dimensions": dimensions,
        "num_ctx": int(os.getenv("PSU_EMBEDDING_NUM_CTX", "1024")),
        "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "source_fingerprint": fingerprint,
        "doc_count": len(documents),
        "categories": sorted(_configured_categories()),
        "docs": documents,
    }
    _atomic_write_json(path, payload)
    load_semantic_index.cache_clear()
    return SemanticIndexBuildResult(
        path=path,
        doc_count=len(documents),
        dimensions=dimensions,
        model=resolved_model,
        elapsed_sec=time.perf_counter() - started,
        embedding_elapsed_sec=embedding_elapsed,
        source_fingerprint=fingerprint,
    )


@lru_cache(maxsize=1)
def load_semantic_index() -> dict[str, Any]:
    if not SEMANTIC_INDEX_PATH.exists():
        return {}
    return json.loads(SEMANTIC_INDEX_PATH.read_text(encoding="utf-8"))


def _cosine(left: Iterable[float], right: Iterable[float]) -> float:
    left_values = tuple(float(value) for value in left)
    right_values = tuple(float(value) for value in right)
    if len(left_values) != len(right_values) or not left_values:
        return -1.0
    return sum(a * b for a, b in zip(left_values, right_values))


def _parse_date(value: Any) -> date | None:
    text = str(value or "").strip()
    if not text:
        return None
    try:
        return date.fromisoformat(text[:10])
    except ValueError:
        return None


def _is_dynamic_doc(doc: dict[str, Any], row: dict[str, Any]) -> bool:
    return bool(
        doc.get("dynamic")
        or row.get("dynamic_knowledge")
        or str(row.get("_source_file") or doc.get("source_file") or "") == DYNAMIC_KNOWLEDGE_FILE
    )


def _trust_level(row: dict[str, Any]) -> str:
    value = str(row.get("trust_level") or "").strip()
    if value:
        return value
    source_url = normalize_text(str(row.get("source_url") or ""))
    if "esports.phuket.psu.ac.th" in source_url:
        return "official"
    return ""


def _temporal_state(row: dict[str, Any], *, today: date) -> tuple[bool, bool, str]:
    status = str(row.get("status") or "published").strip().lower()
    if status != "published":
        return False, False, f"status={status or 'missing'}"
    valid_from = _parse_date(row.get("valid_from"))
    valid_until = _parse_date(row.get("valid_until") or row.get("expires_at"))
    time_sensitive = bool(row.get("time_sensitive"))
    if valid_from and today < valid_from:
        return False, False, "not_yet_valid"
    if time_sensitive and valid_until and today > valid_until:
        return False, False, "expired"

    freshness_verified = bool(row.get("freshness_verified"))
    retrieved_at = str(row.get("retrieved_at") or "").strip()
    current = bool(
        freshness_verified
        and retrieved_at
        and valid_until is not None
        and today <= valid_until
    )
    return True, current, "current_verified" if current else "published"


def _category_allowed(route: PipelineRoute, doc: dict[str, Any], row: dict[str, Any]) -> bool:
    category = str(row.get("category") or doc.get("category") or "")
    if route.category in {"general", "unknown"}:
        return _is_dynamic_doc(doc, row)
    if category == route.category:
        return True
    if route.category == "equipment" and route.intent == "equipment_game_catalog" and category == "games":
        return True
    if route.category == "games" and route.intent == "knowledge_lookup" and category == "knowledge":
        return True
    return False


def _minimum_score(route: PipelineRoute) -> float:
    if route.category in {"general", "unknown"}:
        return float(os.getenv("PSU_SEMANTIC_GENERAL_MIN_SCORE", "0.62"))
    if route.category in {"knowledge", "events_news"}:
        return float(os.getenv("PSU_SEMANTIC_KNOWLEDGE_MIN_SCORE", "0.48"))
    return float(os.getenv("PSU_SEMANTIC_MIN_SCORE", "0.50"))


def _route_discovery_category_allowed(doc: dict[str, Any], row: dict[str, Any]) -> bool:
    category = str(row.get("category") or doc.get("category") or "")
    return category in {"knowledge", "events_news", "about_us"}


def retrieve_semantic_guarded(
    query: str,
    route: PipelineRoute,
    *,
    limit: int = 5,
    require_current: bool = False,
    discover_route: bool = False,
    query_vector: Iterable[float] | None = None,
    index: dict[str, Any] | None = None,
) -> tuple[list[dict[str, Any]], PipelineTrace]:
    if not semantic_retrieval_enabled() and index is None:
        return [], PipelineTrace("semantic_retrieval", "skipped", 0.0, "disabled")

    selected_index = index if index is not None else load_semantic_index()
    if not selected_index or not selected_index.get("docs"):
        return [], PipelineTrace("semantic_retrieval", "skipped", 0.0, "semantic index missing or empty")
    configured_model = embedding_model_name()
    index_model = str(selected_index.get("model") or "")
    if index is None and index_model and index_model != configured_model:
        return [], PipelineTrace(
            "semantic_retrieval",
            "skipped_model_mismatch",
            0.0,
            f"index_model={index_model} configured_model={configured_model}",
        )
    minimum_remaining = max(0.0, float(os.getenv("PSU_SEMANTIC_MIN_REMAINING_SEC", "1.0")))
    remaining = remaining_sec()
    if remaining is not None and remaining < minimum_remaining:
        return [], PipelineTrace(
            "semantic_retrieval",
            "skipped_deadline",
            0.0,
            f"remaining={remaining:.3f}s",
        )

    started = time.perf_counter()
    embedding_metadata: dict[str, Any] = {"provided_query_vector": query_vector is not None}
    try:
        if query_vector is None:
            resolved_vector, embedding_metadata = embed_query(query)
        else:
            resolved_vector = tuple(float(value) for value in query_vector)
    except Exception as exc:  # noqa: BLE001 - semantic retrieval must degrade safely.
        return [], PipelineTrace(
            "semantic_retrieval",
            "fallback_no_semantic",
            0.0,
            f"{type(exc).__name__}: {exc}",
            {"fallback": True, "elapsed_sec": round(time.perf_counter() - started, 4)},
        )

    today = date.today()
    scored: list[tuple[float, dict[str, Any]]] = []
    blocked: dict[str, int] = {}
    for doc in selected_index.get("docs", []):
        row = dict(doc.get("row") or {})
        if discover_route:
            category_allowed = _route_discovery_category_allowed(doc, row)
        else:
            category_allowed = _category_allowed(route, doc, row)
        if not category_allowed:
            blocked["category_mismatch"] = blocked.get("category_mismatch", 0) + 1
            continue
        allowed, current, temporal_reason = _temporal_state(row, today=today)
        if not allowed:
            blocked[temporal_reason] = blocked.get(temporal_reason, 0) + 1
            continue
        if require_current and not current:
            blocked["not_current_verified"] = blocked.get("not_current_verified", 0) + 1
            continue
        trust = _trust_level(row)
        trust_rank = TRUST_RANK.get(trust, 0)
        if (route.category in {"general", "unknown"} or discover_route) and trust_rank < 2:
            blocked["dynamic_source_trust_too_low"] = blocked.get("dynamic_source_trust_too_low", 0) + 1
            continue

        semantic_score = _cosine(resolved_vector, doc.get("vector") or ())
        lexical_score = _lexical_overlap(query, row)
        priority = float(row.get("priority") or 0.0) / 100.0
        trust_bonus = trust_rank * 0.04
        combined = semantic_score + (lexical_score * 0.16) + priority + trust_bonus
        candidate = dict(row)
        candidate.update({
            "_score": round((semantic_score * 10.0) + (lexical_score * 3.0) + priority + trust_bonus, 4),
            "_semantic_score": round(semantic_score, 6),
            "_semantic_combined_score": round(combined, 6),
            "_semantic_model": index_model or configured_model,
            "_semantic_backend": str(selected_index.get("backend") or "ollama_dense_embedding_v1"),
            "_semantic_current_verified": current,
            "_semantic_temporal_state": temporal_reason,
            "_semantic_dynamic": _is_dynamic_doc(doc, row),
            "trust_level": trust,
        })
        scored.append((combined, candidate))

    scored.sort(key=lambda item: item[0], reverse=True)
    minimum = (
        float(os.getenv("PSU_SEMANTIC_ROUTE_MIN_SCORE", "0.48"))
        if discover_route
        else _minimum_score(route)
    )
    filtered = [row for _, row in scored if float(row.get("_semantic_score") or -1.0) >= minimum]
    top_score = float(filtered[0].get("_semantic_score") or 0.0) if filtered else 0.0
    second_score = float(filtered[1].get("_semantic_score") or 0.0) if len(filtered) > 1 else 0.0
    margin = top_score - second_score
    if (route.category in {"general", "unknown"} or discover_route) and len(filtered) > 1:
        required_margin = float(os.getenv(
            "PSU_SEMANTIC_ROUTE_MIN_MARGIN" if discover_route else "PSU_SEMANTIC_GENERAL_MIN_MARGIN",
            "0.025" if discover_route else "0.035",
        ))
        if margin < required_margin:
            blocked["general_margin_too_small"] = blocked.get("general_margin_too_small", 0) + 1
            filtered = []

    hits = filtered[:max(1, limit)]
    confidence = min(0.93, 0.52 + max(0.0, top_score) * 0.42 + max(0.0, margin) * 0.50) if hits else 0.0
    elapsed = time.perf_counter() - started
    detail = (
        f"hits={len(hits)} model={index_model or configured_model} "
        f"top={top_score:.4f} margin={margin:.4f} require_current={require_current} "
        f"discover_route={discover_route}"
    )
    if blocked:
        detail += " blocked=" + ",".join(
            f"{key}:{value}" for key, value in sorted(blocked.items())[:6]
        )
    return hits, PipelineTrace(
        "semantic_retrieval",
        "ollama_dense_guarded" if hits else "no_accepted_candidate",
        confidence,
        detail,
        {
            "model": index_model or configured_model,
            "dimensions": int(selected_index.get("dimensions") or len(tuple(resolved_vector))),
            "doc_count": int(selected_index.get("doc_count") or len(selected_index.get("docs") or [])),
            "minimum_score": minimum,
            "top_score": round(top_score, 6),
            "second_score": round(second_score, 6),
            "margin": round(margin, 6),
            "require_current": require_current,
            "discover_route": discover_route,
            "blocked": blocked,
            "embedding": embedding_metadata,
            "elapsed_sec": round(elapsed, 4),
        },
    )


_EXPLICIT_RULE_SIGNALS = (
    "กติกา",
    "กฎ",
    "ข้อห้าม",
    "บทลงโทษ",
    "โดนอะไร",
    "โดนปรับ",
    "ปรับแพ้",
    "ตัดสิทธิ์",
    "ทีมละกี่คน",
    "timeout",
    "pause",
    "bo3",
    "bo5",
    "map pool",
    "แผนที่ที่ใช้แข่ง",
    "ใช้สกิน",
    "ใช้อุปกรณ์อะไรแข่ง",
)

_GAME_OPERATION_SIGNALS = (
    "มีเกม",
    "เกมอะไรบ้าง",
    "เล่นได้ไหม",
    "เล่นได้ที่",
    "โซนไหน",
    "ปุ่ม",
    "ควบคุม",
    "จอย",
    "ติดตั้ง",
)

_SEMANTIC_DOMAIN_SIGNALS = (
    "psu",
    "esports",
    "อีสปอร์ต",
    "studio",
    "สตูดิโอ",
    "กิจกรรม",
    "ข่าว",
    "การแข่งขัน",
    "ทัวร์นาเมนต์",
    "ประวัติ",
    "ครั้งแรก",
    "บทความ",
    "ทักษะ",
    "อาชีพ",
)


def refine_route_with_semantic_evidence(
    query: str,
    route: PipelineRoute,
) -> tuple[PipelineRoute, PipelineTrace]:
    if not semantic_retrieval_enabled():
        return route, PipelineTrace("semantic_route_refiner", "skipped", 0.0, "semantic retrieval disabled")
    if route.category not in {"general", "unknown", "knowledge", "events_news", "games", "competition_rules", "overview"}:
        return route, PipelineTrace(
            "semantic_route_refiner",
            "skipped_protected_route",
            route.confidence,
            f"protected={route.category}/{route.intent}",
        )

    normalized = normalize_text(query)
    domain_anchored = any(term in normalized for term in _SEMANTIC_DOMAIN_SIGNALS)
    if route.category in {"general", "unknown"} and not domain_anchored:
        index = load_semantic_index()
        has_dynamic_docs = any(
            _is_dynamic_doc(doc, dict(doc.get("row") or {}))
            for doc in index.get("docs", [])
        )
        if not has_dynamic_docs:
            return route, PipelineTrace(
                "semantic_route_refiner",
                "skipped_no_dynamic_documents",
                route.confidence,
                "general query has no PSU semantic anchor and the index has no dynamic documents",
            )
    if route.category == "competition_rules" and any(term in normalized for term in _EXPLICIT_RULE_SIGNALS):
        return route, PipelineTrace(
            "semantic_route_refiner",
            "kept_explicit_rule_route",
            route.confidence,
            "explicit competition rule signal",
        )
    if route.category == "games" and any(term in normalized for term in _GAME_OPERATION_SIGNALS):
        return route, PipelineTrace(
            "semantic_route_refiner",
            "kept_explicit_game_route",
            route.confidence,
            "explicit game operation signal",
        )

    hits, retrieval_trace = retrieve_semantic_guarded(
        query,
        route,
        limit=4,
        discover_route=True,
    )
    if not hits:
        return route, PipelineTrace(
            "semantic_route_refiner",
            "no_route_candidate",
            route.confidence,
            retrieval_trace.detail,
            {"retrieval": retrieval_trace.metadata},
        )
    top = hits[0]
    category = str(top.get("category") or "")
    score = float(top.get("_semantic_score") or 0.0)
    second_score = float(hits[1].get("_semantic_score") or 0.0) if len(hits) > 1 else 0.0
    margin = score - second_score
    dynamic = bool(top.get("_semantic_dynamic"))
    category_support = sum(1 for hit in hits[:3] if str(hit.get("category") or "") == category)
    if route.category in {"general", "unknown"} and not (dynamic or domain_anchored):
        return route, PipelineTrace(
            "semantic_route_refiner",
            "rejected_unanchored_general",
            route.confidence,
            f"top={top.get('id')} score={score:.4f}",
        )
    if category_support < 2 and len(hits) >= 3 and not dynamic:
        return route, PipelineTrace(
            "semantic_route_refiner",
            "rejected_weak_category_support",
            route.confidence,
            f"category={category} support={category_support}/3",
        )
    if category == route.category:
        lock_confirmed_route = category in {"knowledge", "events_news", "about_us"}
        return route, PipelineTrace(
            "semantic_route_refiner",
            "confirmed_existing_route",
            max(route.confidence, retrieval_trace.confidence),
            f"category={category} top={top.get('id')} score={score:.4f}",
            {
                "route_lock": lock_confirmed_route,
                "top_id": top.get("id"),
                "top_score": round(score, 6),
                "margin": round(margin, 6),
                "dynamic": dynamic,
                "category_support_top3": category_support,
                "retrieval": retrieval_trace.metadata,
            },
        )

    intent = {
        "knowledge": "knowledge_lookup",
        "events_news": "news_lookup",
        "about_us": "overview_lookup",
    }.get(category, "semantic_dynamic_lookup")
    refined = PipelineRoute(
        category,
        intent,
        min(0.95, max(0.84, retrieval_trace.confidence)),
        "summary",
        "medium" if category == "events_news" else "low",
        "semantic evidence resolved a likely category mismatch",
    )
    return refined, PipelineTrace(
        "semantic_route_refiner",
        "route_refined",
        refined.confidence,
        f"{route.category}/{route.intent} -> {refined.category}/{refined.intent}",
        {
            "route_lock": True,
            "top_id": top.get("id"),
            "top_score": round(score, 6),
            "margin": round(margin, 6),
            "dynamic": dynamic,
            "category_support_top3": category_support,
            "retrieval": retrieval_trace.metadata,
        },
    )


def semantic_hits_have_current_evidence(hits: list[dict[str, Any]]) -> bool:
    return any(bool(hit.get("_semantic_current_verified")) for hit in hits)


def answer_from_semantic_hits(
    hits: list[dict[str, Any]],
    *,
    query: str = "",
) -> tuple[str | None, list[dict[str, Any]], float]:
    del query
    if not hits:
        return None, [], 0.0
    best = hits[0]
    answer = str(best.get("text") or best.get("answer") or "").strip()
    if not answer:
        return None, [], 0.0
    source_url = str(best.get("source_url") or "").strip()
    if source_url and "แหล่งข้อมูล:" not in answer:
        answer = answer.rstrip() + f"\nแหล่งข้อมูล: {source_url}"
    score = float(best.get("_semantic_score") or 0.0)
    second = float(hits[1].get("_semantic_score") or 0.0) if len(hits) > 1 else 0.0
    confidence = min(0.91, 0.54 + max(0.0, score) * 0.42 + max(0.0, score - second) * 0.35)
    return answer, [hit_from_curated(row) for row in hits[:3]], confidence
