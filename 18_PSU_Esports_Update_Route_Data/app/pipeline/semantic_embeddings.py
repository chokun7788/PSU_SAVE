from __future__ import annotations

import json
import math
import os
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from functools import lru_cache
from typing import Any, Iterable

from app.pipeline.request_deadline import timeout_for_call


DEFAULT_OLLAMA_URL = "http://127.0.0.1:11434"
DEFAULT_EMBEDDING_MODEL = "psu-bge-m3:q8_0"


def _truthy(value: str | None, *, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


def semantic_retrieval_enabled() -> bool:
    return _truthy(os.getenv("PSU_SEMANTIC_RETRIEVAL"), default=False)


def embedding_model_name() -> str:
    return os.getenv("PSU_EMBEDDING_MODEL", DEFAULT_EMBEDDING_MODEL).strip() or DEFAULT_EMBEDDING_MODEL


def embedding_base_url() -> str:
    return (
        os.getenv("PSU_EMBEDDING_OLLAMA_URL")
        or os.getenv("OLLAMA_URL")
        or DEFAULT_OLLAMA_URL
    ).rstrip("/")


def embedding_num_ctx() -> int:
    return max(256, int(os.getenv("PSU_EMBEDDING_NUM_CTX", "1024")))


def embedding_dimensions() -> int:
    return max(0, int(os.getenv("PSU_EMBEDDING_DIMENSIONS", "0")))


@dataclass(frozen=True)
class EmbeddingBatch:
    vectors: tuple[tuple[float, ...], ...]
    model: str
    dimensions: int
    elapsed_sec: float
    total_duration_ms: float
    load_duration_ms: float
    prompt_eval_count: int

    def metadata(self) -> dict[str, Any]:
        return {
            "model": self.model,
            "dimensions": self.dimensions,
            "elapsed_sec": round(self.elapsed_sec, 4),
            "total_duration_ms": round(self.total_duration_ms, 2),
            "load_duration_ms": round(self.load_duration_ms, 2),
            "prompt_eval_count": self.prompt_eval_count,
        }


def _normalized(vector: Iterable[float]) -> tuple[float, ...]:
    values = tuple(float(value) for value in vector)
    norm = math.sqrt(sum(value * value for value in values))
    if norm <= 0:
        raise ValueError("embedding vector has zero norm")
    return tuple(value / norm for value in values)


def embed_texts(
    texts: list[str] | tuple[str, ...],
    *,
    model: str | None = None,
    timeout_sec: float | None = None,
    keep_alive: str | int | None = None,
    apply_request_deadline: bool = True,
) -> EmbeddingBatch:
    clean_texts = [str(text or "").strip() for text in texts]
    if not clean_texts or any(not text for text in clean_texts):
        raise ValueError("embedding input must contain non-empty text")

    selected_model = (model or embedding_model_name()).strip()
    configured_timeout = float(
        timeout_sec
        if timeout_sec is not None
        else os.getenv("PSU_EMBEDDING_TIMEOUT_SEC", "2.5")
    )
    effective_timeout = (
        timeout_for_call(configured_timeout)
        if apply_request_deadline
        else configured_timeout
    )
    if effective_timeout <= 0:
        raise TimeoutError("request deadline exhausted before semantic embedding call")

    payload: dict[str, Any] = {
        "model": selected_model,
        "input": clean_texts,
        "truncate": True,
        "keep_alive": (
            keep_alive
            if keep_alive is not None
            else os.getenv("PSU_EMBEDDING_KEEP_ALIVE", "10m")
        ),
        "options": {"num_ctx": embedding_num_ctx()},
    }
    requested_dimensions = embedding_dimensions()
    if requested_dimensions:
        payload["dimensions"] = requested_dimensions

    request = urllib.request.Request(
        f"{embedding_base_url()}/api/embed",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    started = time.perf_counter()
    try:
        with urllib.request.urlopen(request, timeout=effective_timeout) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Ollama embedding HTTP {exc.code}: {detail[:500]}") from exc
    elapsed = time.perf_counter() - started

    raw_vectors = data.get("embeddings")
    if not isinstance(raw_vectors, list) or len(raw_vectors) != len(clean_texts):
        raise ValueError(
            f"embedding response count mismatch: expected {len(clean_texts)}, got "
            f"{len(raw_vectors) if isinstance(raw_vectors, list) else 'invalid'}"
        )
    vectors = tuple(_normalized(vector) for vector in raw_vectors)
    dimensions = len(vectors[0])
    if dimensions <= 0 or any(len(vector) != dimensions for vector in vectors):
        raise ValueError("embedding response contains inconsistent dimensions")
    if requested_dimensions and dimensions != requested_dimensions:
        raise ValueError(
            f"embedding dimension mismatch: requested {requested_dimensions}, got {dimensions}"
        )

    return EmbeddingBatch(
        vectors=vectors,
        model=str(data.get("model") or selected_model),
        dimensions=dimensions,
        elapsed_sec=elapsed,
        total_duration_ms=float(data.get("total_duration") or 0) / 1_000_000,
        load_duration_ms=float(data.get("load_duration") or 0) / 1_000_000,
        prompt_eval_count=int(data.get("prompt_eval_count") or 0),
    )


@lru_cache(maxsize=256)
def _cached_query_embedding(
    model: str,
    base_url: str,
    num_ctx: int,
    dimensions: int,
    text: str,
) -> tuple[tuple[float, ...], dict[str, Any]]:
    # The explicit config values are part of the cache key. The function reads
    # the same environment values when it calls Ollama.
    del base_url, num_ctx, dimensions
    result = embed_texts([text], model=model)
    return result.vectors[0], result.metadata()


def embed_query(text: str) -> tuple[tuple[float, ...], dict[str, Any]]:
    clean = str(text or "").strip()
    if not clean:
        raise ValueError("query text is empty")
    return _cached_query_embedding(
        embedding_model_name(),
        embedding_base_url(),
        embedding_num_ctx(),
        embedding_dimensions(),
        clean,
    )


def clear_embedding_cache() -> None:
    _cached_query_embedding.cache_clear()


def warm_semantic_embedding_model() -> EmbeddingBatch:
    return embed_texts(
        ["PSU Esports Studio Phuket semantic retrieval warmup"],
        timeout_sec=float(os.getenv("PSU_EMBEDDING_WARMUP_TIMEOUT_SEC", "120")),
        keep_alive=os.getenv("PSU_EMBEDDING_KEEP_ALIVE", "10m"),
        apply_request_deadline=False,
    )
