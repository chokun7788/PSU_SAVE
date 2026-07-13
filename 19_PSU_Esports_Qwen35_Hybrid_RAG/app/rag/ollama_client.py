from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any


DEFAULT_OLLAMA_URL = "http://127.0.0.1:11434"


def ollama_generate(
    prompt: str,
    *,
    model: str,
    timeout_sec: float = 10.0,
    ollama_url: str = DEFAULT_OLLAMA_URL,
    num_predict: int = 180,
    temperature: float = 0.1,
) -> dict[str, Any]:
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": temperature,
            "top_p": 0.85,
            "top_k": 20,
            "repeat_penalty": 1.08,
            "num_predict": num_predict,
            "num_ctx": 4096,
        },
    }
    return _post_json(f"{ollama_url.rstrip('/')}/api/generate", payload, timeout_sec=timeout_sec)


def ollama_embed(
    texts: list[str],
    *,
    model: str,
    timeout_sec: float = 30.0,
    ollama_url: str = DEFAULT_OLLAMA_URL,
) -> list[list[float]]:
    payload = {"model": model, "input": texts}
    try:
        data = _post_json(f"{ollama_url.rstrip('/')}/api/embed", payload, timeout_sec=timeout_sec)
        embeddings = data.get("embeddings")
        if isinstance(embeddings, list):
            return embeddings
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError):
        pass

    # Older Ollama endpoint fallback: one request per text.
    vectors: list[list[float]] = []
    for text in texts:
        legacy = _post_json(
            f"{ollama_url.rstrip('/')}/api/embeddings",
            {"model": model, "prompt": text},
            timeout_sec=timeout_sec,
        )
        embedding = legacy.get("embedding")
        if not isinstance(embedding, list):
            raise RuntimeError(f"Ollama did not return an embedding for model {model}")
        vectors.append(embedding)
    return vectors


def _post_json(url: str, payload: dict[str, Any], *, timeout_sec: float) -> dict[str, Any]:
    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout_sec) as response:
        return json.loads(response.read().decode("utf-8"))
