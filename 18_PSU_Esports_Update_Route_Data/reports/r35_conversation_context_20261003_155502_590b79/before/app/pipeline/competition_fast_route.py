"""Resolve a closed rulebook route; answering still requires source coverage."""
from __future__ import annotations

from app.pipeline.competition_targets import competition_facet, looks_like_competition_rule_query, resolve_competition_targets
from app.pipeline.schemas import UniversalIntent


def exact_competition_intent(query: str) -> UniversalIntent | None:
    target = resolve_competition_targets(query)
    facet = competition_facet(query)
    if target.status != 'exact' or not facet or not looks_like_competition_rule_query(query):
        return None
    return UniversalIntent(
        domain='competition_rules', operation='rule_lookup', target=target.targets[0].game_id,
        filters={'competition_facet': facet, 'competition_rulebook_id': target.targets[0].rulebook_id},
        needs=('lookup_competition_rule',), answer_style='direct', confidence=0.97,
        method='competition_target_first', reason='one registered game and an explicit rule facet; source coverage remains required',
    )
