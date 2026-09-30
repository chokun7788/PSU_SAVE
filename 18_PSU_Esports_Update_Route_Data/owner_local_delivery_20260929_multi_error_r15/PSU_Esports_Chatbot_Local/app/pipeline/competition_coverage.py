from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from app.pipeline.competition_targets import competition_facet, resolve_competition_targets
from app.pipeline.retrieval import competition_hits_cover_intent


ROOT = Path(__file__).resolve().parents[2]
SOURCE_COVERAGE_MANIFEST = ROOT / "data" / "competition_rules" / "source_coverage_manifest.jsonl"


@dataclass(frozen=True)
class CompetitionEvidenceCoverage:
    covered: bool
    facet: str
    target_game_ids: tuple[str, ...]
    matched_chunk_ids: tuple[str, ...]
    reason: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "covered": self.covered,
            "facet": self.facet,
            "target_game_ids": list(self.target_game_ids),
            "matched_chunk_ids": list(self.matched_chunk_ids),
            "reason": self.reason,
        }


def _intent_facet(query: str) -> str:
    facet = competition_facet(query)
    # Preserve the active source-coverage contract while the V2.1 taxonomy is
    # introduced. The manifest currently records broad fair-play gaps under
    # ``conduct``; the runtime projection will later migrate this explicitly.
    if facet == "fair_play_conduct":
        return "conduct"
    return facet or "unspecified"


def _known_source_gap(game_id: str, facet: str) -> str | None:
    if not SOURCE_COVERAGE_MANIFEST.exists():
        return None
    try:
        rows = (
            json.loads(line)
            for line in SOURCE_COVERAGE_MANIFEST.read_text(encoding="utf-8").splitlines()
            if line.strip()
        )
    except (OSError, json.JSONDecodeError):
        return None
    for row in rows:
        if (
            str(row.get("game_id") or "") == game_id
            and str(row.get("facet") or "") == facet
            and str(row.get("status") or "") == "unsupported_in_active_source"
        ):
            return str(row.get("reason") or "active rulebook has no direct clause")
    return None


def assess_competition_evidence(query: str, hits: list[dict[str, Any]]) -> CompetitionEvidenceCoverage:
    """Explain whether current source chunks prove the requested proposition.

    This is deliberately an evidence check, not a model-confidence score. It
    gives routing, logs and evaluation one stable explanation for a safe
    no-answer, and makes known source gaps visible instead of indistinguishable
    from a weak semantic retrieval result.
    """
    target_resolution = resolve_competition_targets(query)
    target_game_ids = tuple(target.game_id for target in target_resolution.targets)
    facet = _intent_facet(query)
    chunk_ids = tuple(str(row.get("id") or "") for row in hits if row.get("id"))
    if competition_hits_cover_intent(query, hits):
        return CompetitionEvidenceCoverage(True, facet, target_game_ids, chunk_ids, "direct_target_facet_evidence")
    # A direct clause in the active source wins over stale coverage metadata.
    # The manifest remains authoritative only when current chunks do not prove
    # the requested proposition.
    known_gaps = [
        _known_source_gap(game_id, facet)
        for game_id in target_game_ids
    ]
    known_gaps = [item for item in known_gaps if item]
    if known_gaps:
        return CompetitionEvidenceCoverage(False, facet, target_game_ids, chunk_ids, f"known_source_gap:{known_gaps[0]}")
    if not hits:
        reason = "no_competition_source_retrieved"
    elif not chunk_ids:
        reason = "retrieved_rows_missing_source_identifiers"
    else:
        reason = "retrieved_source_does_not_prove_requested_facet"
    return CompetitionEvidenceCoverage(False, facet, target_game_ids, chunk_ids, reason)
