"""Read-only store and bounded lexical ranking for approved V2.1 claims.

The store is inactive until an owner-approved runtime release exists.  It
applies the hard claim contract before ranking, so semantic retrieval can be
added later without gaining permission to cross game/facet boundaries.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any, Mapping

from app.pipeline.competition_claim_contract import (
    CompetitionClaimSelection,
    select_eligible_claims,
)
from app.pipeline.competition_taxonomy import conservative_text


_STOPWORDS = {
    "กติกา", "การแข่งขัน", "คือ", "อะไร", "อย่างไร", "ยังไง", "ครับ", "ค่ะ",
    "the", "a", "an", "is", "are", "what", "how", "rules", "rule", "tournament",
}


@dataclass(frozen=True)
class RankedCompetitionClaim:
    claim: dict[str, Any]
    score: float
    lexical_score: float
    semantic_score: float


@dataclass(frozen=True)
class CompetitionClaimRetrieval:
    ranked: tuple[RankedCompetitionClaim, ...]
    selection: CompetitionClaimSelection


def _tokens(value: str) -> set[str]:
    normalized = conservative_text(value)
    return {
        token for token in re.findall(r"[a-z0-9]+|[ก-๙]+", normalized)
        if token and token not in _STOPWORDS
    }


@lru_cache(maxsize=8)
def _load_cached(path_text: str, modified_ns: int) -> tuple[dict[str, Any], ...]:
    del modified_ns
    path = Path(path_text)
    return tuple(
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    )


def load_runtime_claims(path: Path) -> tuple[dict[str, Any], ...]:
    if not path.exists():
        return ()
    return _load_cached(str(path.resolve()), path.stat().st_mtime_ns)


def retrieve_runtime_claims(
    query: str,
    rows: tuple[dict[str, Any], ...] | list[dict[str, Any]],
    *,
    release_id: str,
    game_id: str,
    facet: str,
    locale: str,
    semantic_scores: Mapping[str, float] | None = None,
    limit: int = 8,
) -> CompetitionClaimRetrieval:
    selection = select_eligible_claims(
        rows,
        release_id=release_id,
        game_id=game_id,
        facet=facet,
        locale=locale,
    )
    query_tokens = _tokens(query)
    semantic = semantic_scores or {}
    ranked: list[RankedCompetitionClaim] = []
    for row in selection.accepted:
        retrieval = row["retrieval"]
        claim = row["claim"]
        source = row["source"]
        locale_text = claim.get("answer_en") if locale == "en" else claim.get("answer_th")
        aliases = retrieval.get("aliases_en") if locale == "en" else retrieval.get("aliases_th")
        patterns = retrieval.get("question_patterns_en") if locale == "en" else retrieval.get("question_patterns_th")
        text = " ".join(
            str(value or "") for value in (
                locale_text,
                source.get("heading_th"),
                source.get("clause_th"),
                " ".join(aliases or []),
                " ".join(patterns or []),
            )
        )
        candidate_tokens = _tokens(text)
        overlap = len(query_tokens & candidate_tokens)
        lexical_score = overlap / max(1, len(query_tokens))
        semantic_score = max(0.0, min(1.0, float(semantic.get(str(row["claim_id"]), 0.0))))
        # Metadata has already passed as a hard gate. Scores only order the
        # remaining same-game/same-facet claims.
        score = 0.65 * lexical_score + 0.35 * semantic_score
        ranked.append(RankedCompetitionClaim(row, score, lexical_score, semantic_score))
    ranked.sort(key=lambda item: (item.score, item.lexical_score, item.claim["claim_id"]), reverse=True)
    bounded = max(1, min(8, int(limit)))
    return CompetitionClaimRetrieval(tuple(ranked[:bounded]), selection)
