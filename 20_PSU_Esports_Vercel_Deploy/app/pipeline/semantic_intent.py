from __future__ import annotations

import json
import math
import re
from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

from app.core.normalization import normalize_text


CATALOG_PATH = Path(__file__).resolve().parents[2] / "data" / "intent" / "semantic_intents.jsonl"


@dataclass(frozen=True)
class SemanticIntentMatch:
    intent_id: str
    category: str
    answer_type: str
    risk: str
    confidence: float
    margin: float
    matched_example: str
    runner_up: str
    reason: str
    metadata: dict[str, Any]


def _compact(text: str) -> str:
    value = normalize_text(text)
    value = re.sub(r"[\s\W_]+", "", value, flags=re.UNICODE)
    return value


def _char_ngrams(text: str) -> Counter[str]:
    compact = _compact(text)
    grams: Counter[str] = Counter()
    if not compact:
        return grams

    for n in (2, 3, 4):
        if len(compact) < n:
            continue
        for index in range(0, len(compact) - n + 1):
            grams[compact[index:index + n]] += 1
    if not grams:
        grams[compact] = 1
    return grams


def _cosine(a: Counter[str], b: Counter[str]) -> float:
    if not a or not b:
        return 0.0
    dot = sum(value * b.get(key, 0) for key, value in a.items())
    if dot <= 0:
        return 0.0
    norm_a = math.sqrt(sum(value * value for value in a.values()))
    norm_b = math.sqrt(sum(value * value for value in b.values()))
    if norm_a <= 0 or norm_b <= 0:
        return 0.0
    return dot / (norm_a * norm_b)


@lru_cache(maxsize=1)
def _load_catalog() -> tuple[dict[str, Any], ...]:
    if not CATALOG_PATH.exists():
        return ()

    rows: list[dict[str, Any]] = []
    for line in CATALOG_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        row = json.loads(line)
        examples = [str(example) for example in row.get("examples", []) if str(example).strip()]
        if not examples:
            continue
        row["_example_vectors"] = tuple((example, _char_ngrams(example)) for example in examples)
        rows.append(row)
    return tuple(rows)


def match_semantic_intent(query: str) -> SemanticIntentMatch | None:
    query_vector = _char_ngrams(query)
    if not query_vector:
        return None

    ranked: list[dict[str, Any]] = []
    for row in _load_catalog():
        best_example = ""
        best_score = 0.0
        scores: list[float] = []
        for example, example_vector in row.get("_example_vectors", ()):
            score = _cosine(query_vector, example_vector)
            scores.append(score)
            if score > best_score:
                best_score = score
                best_example = example
        top_scores = sorted(scores, reverse=True)[:3]
        blended_score = (best_score * 0.82) + ((sum(top_scores) / len(top_scores)) * 0.18 if top_scores else 0.0)
        ranked.append({
            "row": row,
            "score": blended_score,
            "best_score": best_score,
            "example": best_example,
        })

    if not ranked:
        return None

    ranked.sort(key=lambda item: item["score"], reverse=True)
    best = ranked[0]
    second = ranked[1] if len(ranked) > 1 else None
    row = best["row"]
    confidence = float(best["score"])
    runner_up_id = str(second["row"].get("intent_id", "")) if second else ""
    runner_up_score = float(second["score"]) if second else 0.0
    margin = confidence - runner_up_score
    min_confidence = float(row.get("min_confidence", 0.60))
    min_margin = float(row.get("min_margin", 0.04))

    if confidence < min_confidence or margin < min_margin:
        return None

    return SemanticIntentMatch(
        intent_id=str(row["intent_id"]),
        category=str(row["category"]),
        answer_type=str(row.get("answer_type", "fact")),
        risk=str(row.get("risk", "medium")),
        confidence=round(confidence, 4),
        margin=round(margin, 4),
        matched_example=str(best["example"]),
        runner_up=runner_up_id,
        reason=f"semantic intent matched example: {best['example']}",
        metadata={
            "method": "local_char_ngram_semantic_intent",
            "best_raw_score": round(float(best["best_score"]), 4),
            "runner_up": runner_up_id,
            "runner_up_score": round(runner_up_score, 4),
            "min_confidence": min_confidence,
            "min_margin": min_margin,
        },
    )
