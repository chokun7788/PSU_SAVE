from __future__ import annotations

import os
import time
from functools import lru_cache
from pathlib import Path
from typing import Any

from app.pipeline.request_deadline import remaining_sec
from app.pipeline.schemas import PipelineTrace


def _truthy(value: str | None, *, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


def document_reranker_enabled() -> bool:
    return _truthy(os.getenv("PSU_DOCUMENT_RERANKER"), default=_truthy(os.getenv("PSU_MODEL_FIRST_FLOW")))


def _cache_dir() -> Path:
    return Path(os.getenv("PSU_DOCUMENT_RERANKER_CACHE_DIR") or os.getenv("PSU_ENTITY_RERANKER_CACHE_DIR", "D:/AIModels/huggingface"))


@lru_cache(maxsize=1)
def _load_model():
    cache_dir = _cache_dir()
    cache_dir.mkdir(parents=True, exist_ok=True)
    os.environ.setdefault("HF_HOME", str(cache_dir))
    os.environ.setdefault("TRANSFORMERS_CACHE", str(cache_dir / "transformers"))
    os.environ.setdefault("HF_HUB_CACHE", str(cache_dir / "hub"))
    os.environ.setdefault("SENTENCE_TRANSFORMERS_HOME", str(cache_dir / "sentence_transformers"))
    from sentence_transformers import CrossEncoder

    model_name = os.getenv("PSU_DOCUMENT_RERANKER_MODEL") or os.getenv("PSU_ENTITY_RERANKER_MODEL", "BAAI/bge-reranker-v2-m3")
    return CrossEncoder(model_name, max_length=512)


def _model_is_loaded() -> bool:
    cache_info = getattr(_load_model, "cache_info", None)
    if cache_info is None:
        return False
    try:
        return int(cache_info().currsize) > 0
    except Exception:  # noqa: BLE001 - cache inspection must never affect retrieval.
        return False


def _doc_text(hit: dict[str, Any]) -> str:
    metadata = hit.get("metadata") if isinstance(hit.get("metadata"), dict) else {}
    return "\n".join(
        str(value)
        for value in (
            hit.get("title"),
            hit.get("text"),
            hit.get("game"),
            hit.get("item"),
            metadata.get("title"),
            metadata.get("text"),
        )
        if str(value or "").strip()
    )


def rerank_documents(query: str, hits: list[dict[str, Any]], *, limit: int = 5) -> tuple[list[dict[str, Any]], PipelineTrace]:
    candidates = list(hits or [])
    if not document_reranker_enabled():
        return candidates[:limit], PipelineTrace("document_reranker", "skipped", 0.0, "disabled")
    if len(candidates) < 2:
        return candidates[:limit], PipelineTrace("document_reranker", "skipped", 0.0, "fewer_than_two_candidates")
    minimum_remaining = max(0.0, float(os.getenv("PSU_DOCUMENT_RERANKER_MIN_REMAINING_SEC", "3.0")))
    remaining = remaining_sec()
    if remaining is not None and remaining < minimum_remaining:
        return candidates[:limit], PipelineTrace("document_reranker", "skipped_deadline", 0.0, f"remaining={remaining:.3f}s")
    cold_start_minimum = max(0.0, float(os.getenv("PSU_DOCUMENT_RERANKER_COLD_START_MIN_REMAINING_SEC", "30.0")))
    if remaining is not None and not _model_is_loaded() and remaining < cold_start_minimum:
        return candidates[:limit], PipelineTrace(
            "document_reranker",
            "skipped_cold_start",
            0.0,
            f"model is not warm; remaining={remaining:.3f}s cold_start_minimum={cold_start_minimum:.3f}s",
            {"warm_model": False, "cold_start_min_remaining_sec": cold_start_minimum},
        )

    max_candidates = max(2, min(12, int(os.getenv("PSU_DOCUMENT_RERANKER_MAX_CANDIDATES", "8"))))
    candidates = candidates[:max_candidates]
    started = time.perf_counter()
    try:
        model = _load_model()
        pairs = [(query, _doc_text(hit)) for hit in candidates]
        raw_scores = model.predict(pairs, batch_size=max(1, int(os.getenv("PSU_DOCUMENT_RERANKER_BATCH_SIZE", "4"))), show_progress_bar=False)
        ranked = []
        for hit, raw_score in zip(candidates, raw_scores):
            row = dict(hit)
            row["_document_rerank_score"] = round(float(raw_score), 5)
            row["_document_rerank_model"] = os.getenv("PSU_DOCUMENT_RERANKER_MODEL") or os.getenv("PSU_ENTITY_RERANKER_MODEL", "BAAI/bge-reranker-v2-m3")
            ranked.append(row)
        ranked.sort(key=lambda item: float(item.get("_document_rerank_score", 0.0)), reverse=True)
        top = float(ranked[0].get("_document_rerank_score", 0.0))
        second = float(ranked[1].get("_document_rerank_score", 0.0)) if len(ranked) > 1 else 0.0
        elapsed = time.perf_counter() - started
        return ranked[:limit], PipelineTrace(
            "document_reranker",
            "bge_reranked",
            min(0.95, 0.60 + max(0.0, top - second) / 4),
            f"candidates={len(candidates)} top={top:.4f} margin={top - second:.4f}",
            {"elapsed_sec": round(elapsed, 4), "candidate_count": len(candidates), "margin": round(top - second, 5)},
        )
    except Exception as exc:  # noqa: BLE001 - reranker must degrade to hybrid score.
        return candidates[:limit], PipelineTrace(
            "document_reranker",
            "fallback_hybrid_score",
            0.35,
            f"{type(exc).__name__}: {exc}",
            {"fallback": True, "candidate_count": len(candidates)},
        )
