from __future__ import annotations

import json
import math
import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

from app.knowledge.localization import active_release_dir
from app.pipeline.request_deadline import allow_stage


_TOKEN_RE = re.compile(r"[a-z0-9]+", flags=re.IGNORECASE)
_STOP = frozenset({
    "a", "an", "and", "are", "at", "be", "can", "do", "does", "for", "from",
    "how", "i", "in", "is", "it", "of", "on", "or", "the", "this", "to",
    "what", "when", "where", "which", "who", "with", "you", "your",
})
CANONICAL_EN_PROJECTION = Path(__file__).resolve().parents[2] / "data" / "content" / "projections" / "rag_en_approved_projection.jsonl"


@dataclass(frozen=True)
class EnglishEvidence:
    content_id: str
    field: str
    category: str
    title: str
    text: str
    source_url: str
    score: float
    method: str
    row: dict[str, Any]


def _tokens(value: str) -> set[str]:
    return {token.lower() for token in _TOKEN_RE.findall(value or "") if token.lower() not in _STOP}


@lru_cache(maxsize=8)
def _load_projection(path_text: str) -> tuple[dict[str, Any], ...]:
    path = Path(path_text)
    if not path.exists():
        return ()
    return tuple(json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip())


def active_rag_projection() -> tuple[dict[str, Any], ...]:
    release = active_release_dir()
    if release is not None:
        release_projection = release / "rag_projection.jsonl"
        if release_projection.exists():
            return _load_projection(str(release_projection))
    # Canonical Content is the current English source of truth. The projection
    # contains only reviewed records; generated drafts never reach this file.
    return _load_projection(str(CANONICAL_EN_PROJECTION))


def _cosine(left: list[float], right: list[float]) -> float:
    if not left or len(left) != len(right):
        return -1.0
    left_norm = math.sqrt(sum(value * value for value in left))
    right_norm = math.sqrt(sum(value * value for value in right))
    if not left_norm or not right_norm:
        return -1.0
    return sum(a * b for a, b in zip(left, right)) / (left_norm * right_norm)


def _semantic_scores(query: str, rows: tuple[dict[str, Any], ...]) -> dict[str, float]:
    release = active_release_dir()
    index_path = release / "semantic_index.json" if release is not None else None
    if index_path is None or not index_path.exists() or not allow_stage(1.0):
        return {}
    try:
        from app.pipeline.semantic_embeddings import embed_query

        index = json.loads(index_path.read_text(encoding="utf-8"))
        embedded = embed_query(query, timeout_sec=0.75)
        query_vector = list(embedded.vector)
        return {
            str(doc.get("id") or ""): _cosine(query_vector, [float(value) for value in doc.get("vector") or []])
            for doc in index.get("docs") or []
        }
    except (OSError, RuntimeError, ValueError, json.JSONDecodeError):
        return {}


def retrieve_approved_english(
    query: str,
    *,
    categories: set[str] | None = None,
    target: str = "",
    limit: int = 4,
) -> list[EnglishEvidence]:
    rows = active_rag_projection()
    if not rows:
        return []
    query_tokens = _tokens(query)
    if not query_tokens:
        return []
    target_key = target.casefold().strip()
    filtered = []
    for row in rows:
        category = str(row.get("category") or "")
        if categories and category not in categories:
            continue
        row_target = str(row.get("game") or row.get("target") or "").casefold().strip()
        if target_key and row_target and row_target != target_key:
            continue
        filtered.append(row)
    semantic = _semantic_scores(query, tuple(filtered))
    candidates: list[EnglishEvidence] = []
    for row in filtered:
        text = str(row.get("text") or "")
        row_tokens = _tokens(" ".join((str(row.get("title") or ""), text, str(row.get("game") or ""))))
        overlap = len(query_tokens & row_tokens) / max(1, len(query_tokens))
        doc_id = str(row.get("projection_id") or "")
        semantic_score = semantic.get(doc_id)
        if semantic_score is None:
            score, method = overlap, "approved_lexical"
        else:
            score, method = (0.72 * semantic_score) + (0.28 * overlap), "approved_bge"
        if score < 0.18:
            continue
        candidates.append(EnglishEvidence(
            content_id=str(row.get("content_id") or ""),
            field=str(row.get("field") or ""),
            category=str(row.get("category") or "knowledge"),
            title=str(row.get("title") or row.get("content_id") or ""),
            text=text,
            source_url=str(row.get("source_url") or ""),
            score=round(score, 5),
            method=method,
            row=row,
        ))
    candidates.sort(key=lambda item: item.score, reverse=True)
    return candidates[: max(1, min(limit, 4))]
