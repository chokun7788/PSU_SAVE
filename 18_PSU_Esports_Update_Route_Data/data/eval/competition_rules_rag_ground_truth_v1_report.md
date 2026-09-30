# Competition Rules RAG Ground Truth v1

ชุดนี้แยกจาก `rag_robustness_ground_truth_v1` และทดสอบเฉพาะกติกา CS2, RoV, TEKKEN 8 และ VALORANT.
ทุก positive case ล็อก game, rulebook, facet และ canonical rule IDs ที่อนุญาตให้ RAG ใช้เป็นหลักฐาน.

- Total: 548
- Thai: 274
- English: 274
- Current canonical records remain `pending_owner_review`; this suite is retrieval gold candidate, not a release-approval bypass.

## Game Coverage

- `cs2`: 228
- `dota2`: 2
- `freefire`: 2
- `multi`: 4
- `multi_or_unspecified`: 4
- `rov`: 100
- `tekken8`: 84
- `valorant`: 124

## Facet Coverage

- `competition_format`: 36
- `conduct`: 38
- `disconnect`: 12
- `dispute`: 24
- `eligibility_registration`: 14
- `equipment`: 48
- `fair_play_conduct`: 26
- `in_match_operations`: 28
- `map_pool`: 24
- `match_configuration`: 12
- `match_settings`: 24
- `pause_timeout`: 40
- `penalty`: 24
- `penalty_matrix`: 12
- `pre_match_on_site`: 40
- `protest_dispute`: 24
- `registration`: 26
- `roster_composition`: 2
- `rulebook_identity`: 36
- `safe_outcome`: 8
- `schedule`: 12
- `team_size`: 38

## Evaluation Contract

- Positive case: route must be `competition_rules`; retrieval must stay in the named rulebook and facet; returned evidence must intersect `allowed_evidence_fact_ids` (legacy fact-card path) or `allowed_evidence_rule_ids` (canonical RAG path).
- Cross-rulebook comparison: retrieve evidence from every named rulebook; do not use one game to answer the other.
- Missing game: ask for the game or tournament; do not guess from a similarly named fact.
- Unknown game: return a safe no-answer; do not substitute CS2/RoV/TEKKEN 8/VALORANT.
- Known source gap: return a safe no-answer with no attached evidence; do not borrow another facet or game.
