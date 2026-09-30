# Competition Rules RAG: Automated Failure Triage

## Input Reports

- `competition_rules_rag_eval_20260921_201453.json`

## Summary

| Locale | Passed | Total | Failed |
| --- | ---: | ---: | ---: |
| en | 91 | 141 | 50 |

## Failure Taxonomy

| Classification | Count | Meaning |
| --- | ---: | --- |
| `gold_or_section_contract_gap` | 27 | The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list. |
| `source_coverage_gap` | 18 | The selected rulebook has no retrieved section that directly proves the requested facet. |
| `routing_or_target_failure` | 3 | The request did not retain the expected competition route or rulebook target. |
| `english_localization_gap` | 2 | The Thai target source was found, but no approved English overlay was available. |

## Review Queue

### en / english_localization_gap / team_size (2 cases)

- `COMP-RAG-V2-EN-139` — How many players must a VALORANT team have?
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_localization_pending_en`
  - Reason: The Thai target source was found, but no approved English overlay was available.
  - Output: Verified VALORANT competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition_rules_v...
- `COMP-RAG-V2-EN-141` — What is the permitted roster size for VALORANT?
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_localization_pending_en`
  - Reason: The Thai target source was found, but no approved English overlay was available.
  - Output: Verified VALORANT competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition_rules_v...

### en / gold_or_section_contract_gap / competition_format (3 cases)

- `COMP-RAG-V2-EN-067` — What competition format does Arena of Valor use?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - 4. Competition rules and regulations 4.3 Disconnect and rematch 4.3.1 If a participant disconnects, pause the game temporarily. Each team may pause up to five times, for no more than one...
- `COMP-RAG-V2-EN-068` — How many games are played in a Arena of Valor match?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - 4. Competition rules and regulations 4.3 Disconnect and rematch 4.3.1 If a participant disconnects, pause the game temporarily. Each team may pause up to five times, for no more than one...
- `COMP-RAG-V2-EN-069` — Is the Arena of Valor event single elimination or does it use another format?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - 4. Competition rules and regulations 4.3 Disconnect and rematch 4.3.1 If a participant disconnects, pause the game temporarily. Each team may pause up to five times, for no more than one...

### en / gold_or_section_contract_gap / disconnect (3 cases)

- `COMP-RAG-V2-EN-070` — What happens if someone disconnects in Arena of Valor?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - 4. Competition rules and regulations 4.3 Disconnect and rematch 4.3.1 If a participant disconnects, pause the game temporarily. Each team may pause up to five times, for no more than one...
- `COMP-RAG-V2-EN-071` — Can a Arena of Valor match restart after a connection loss?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - 4. Competition rules and regulations 4.3 Disconnect and rematch 4.3.1 If a participant disconnects, pause the game temporarily. Each team may pause up to five times, for no more than one...
- `COMP-RAG-V2-EN-072` — How do Arena of Valor rules handle an internet disconnection?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - 4. Competition rules and regulations 4.3 Disconnect and rematch 4.3.1 If a participant disconnects, pause the game temporarily. Each team may pause up to five times, for no more than one...

### en / gold_or_section_contract_gap / dispute (3 cases)

- `COMP-RAG-V2-EN-007` — What happens if there is a dispute about a Counter-Strike 2 result?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - 8. Penalty table: 8. Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- `COMP-RAG-V2-EN-008` — Who decides a disagreement in a Counter-Strike 2 match?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - 8. Penalty table: 8. Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- `COMP-RAG-V2-EN-009` — How do the Counter-Strike 2 rules resolve a conflict after a match?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - 8. Penalty table: 8. Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### en / gold_or_section_contract_gap / fair_play_conduct (3 cases)

- `COMP-RAG-V2-EN-016` — What fair-play rules apply to Counter-Strike 2?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - 1. Player conduct: Aggressive behaviour, hateful speech (including racial or religious discrimination), and unsportsmanlike conduct are prohibited. - 8. Penalty table: 8. Source: https://esp...
- `COMP-RAG-V2-EN-017` — Which unsporting behaviours are prohibited in Counter-Strike 2?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - 1. Player conduct: Aggressive behaviour, hateful speech (including racial or religious discrimination), and unsportsmanlike conduct are prohibited. - 8. Penalty table: 8. Source: https://esp...
- `COMP-RAG-V2-EN-018` — Where can I check the sportsmanship rules for Counter-Strike 2?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - 1. Player conduct: Aggressive behaviour, hateful speech (including racial or religious discrimination), and unsportsmanlike conduct are prohibited. - 8. Penalty table: 8. Source: https://esp...

### en / gold_or_section_contract_gap / pause_timeout (3 cases)

- `COMP-RAG-V2-EN-076` — When may a Arena of Valor match be paused?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - 4. Competition rules and regulations 4.3 Disconnect and rematch 4.3.1 If a participant disconnects, pause the game temporarily. Each team may pause up to five times, for no more than one...
- `COMP-RAG-V2-EN-077` — How do timeout and technical pause rules work in Arena of Valor?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - 4. Competition rules and regulations 4.3 Disconnect and rematch 4.3.1 If a participant disconnects, pause the game temporarily. Each team may pause up to five times, for no more than one...
- `COMP-RAG-V2-EN-078` — What should we do if a Arena of Valor match needs to stop mid-game?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - 4. Competition rules and regulations 4.3 Disconnect and rematch 4.3.1 If a participant disconnects, pause the game temporarily. Each team may pause up to five times, for no more than one...

### en / gold_or_section_contract_gap / penalty_matrix (3 cases)

- `COMP-RAG-V2-EN-037` — Is there a penalty table for Counter-Strike 2?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - 8. Penalty table: 8. Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- `COMP-RAG-V2-EN-038` — How do penalties differ by violation in Counter-Strike 2?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - 8. Penalty table: 8. Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- `COMP-RAG-V2-EN-039` — Where are the Counter-Strike 2 tournament penalties listed?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - 8. Penalty table: 8. Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### en / gold_or_section_contract_gap / protest_dispute (3 cases)

- `COMP-RAG-V2-EN-043` — How can a team protest a Counter-Strike 2 result?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - 8. Penalty table: 8. Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- `COMP-RAG-V2-EN-044` — When may we raise an objection in the Counter-Strike 2 event?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - 8. Penalty table: 8. Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- `COMP-RAG-V2-EN-045` — What is the process for challenging a Counter-Strike 2 decision?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - 8. Penalty table: 8. Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### en / gold_or_section_contract_gap / rulebook_identity (3 cases)

- `COMP-RAG-V2-EN-085` — What does this Arena of Valor rulebook cover?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - 4. Competition rules and regulations 4.3 Disconnect and rematch 4.3.1 If a participant disconnects, pause the game temporarily. Each team may pause up to five times, for no more than one...
- `COMP-RAG-V2-EN-086` — Can you give an overview of the Arena of Valor event rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - 4. Competition rules and regulations 4.3 Disconnect and rematch 4.3.1 If a participant disconnects, pause the game temporarily. Each team may pause up to five times, for no more than one...
- `COMP-RAG-V2-EN-087` — Which tournament does this Arena of Valor rulebook apply to?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - 4. Competition rules and regulations 4.3 Disconnect and rematch 4.3.1 If a participant disconnects, pause the game temporarily. Each team may pause up to five times, for no more than one...

### en / gold_or_section_contract_gap / schedule (3 cases)

- `COMP-RAG-V2-EN-052` — Where can I find the Counter-Strike 2 event schedule?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - 7. Match schedule: The bracket will be announced at least one day in advance. Teams must confirm participation before the match begins. Late arrival may result in disqualification. Source: h...
- `COMP-RAG-V2-EN-053` — When is Counter-Strike 2 played and how is the time announced?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - 7. Match schedule: The bracket will be announced at least one day in advance. Teams must confirm participation before the match begins. Late arrival may result in disqualification. Source: h...
- `COMP-RAG-V2-EN-054` — Please check the competition schedule for Counter-Strike 2.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - 7. Match schedule: The bracket will be announced at least one day in advance. Teams must confirm participation before the match begins. Late arrival may result in disqualification. Source: h...

### en / routing_or_target_failure / pause_timeout (3 cases)

- `COMP-RAG-V2-EN-064` — Could you compare the pause rules for CS2 and VALORANT?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The request did not retain the expected competition route or rulebook target.
  - Output: English draft translation of Counter-Strike 2 competition rules: - 8. Penalty table: 8. Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- `COMP-RAG-V2-EN-065` — Do CS2 and VALORANT handle an in-match pause differently?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The request did not retain the expected competition route or rulebook target.
  - Output: English draft translation of Counter-Strike 2 competition rules: - 8. Penalty table: 8. Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- `COMP-RAG-V2-EN-066` — I want to compare timeout rules between CS2 and VALORANT.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The request did not retain the expected competition route or rulebook target.
  - Output: English draft translation of Counter-Strike 2 competition rules: - 8. Penalty table: 8. Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### en / source_coverage_gap / conduct (3 cases)

- `COMP-RAG-V2-EN-115` — What conduct is expected from VALORANT players?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-116` — What behaviour is not allowed during a VALORANT match?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-117` — What do the VALORANT rules say about player sportsmanship?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.

### en / source_coverage_gap / fair_play_conduct (3 cases)

- `COMP-RAG-V2-EN-121` — What fair-play rules apply to VALORANT?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-122` — Which unsporting behaviours are prohibited in VALORANT?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-123` — Where can I check the sportsmanship rules for VALORANT?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.

### en / source_coverage_gap / in_match_operations (3 cases)

- `COMP-RAG-V2-EN-124` — How should players contact officials during a VALORANT match?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-125` — What is the in-match procedure for VALORANT?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-126` — Who should we notify if an issue occurs during VALORANT?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.

### en / source_coverage_gap / pre_match_on_site (6 cases)

- `COMP-RAG-V2-EN-040` — How do players check in for Counter-Strike 2?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-041` — What must players do on site before a Counter-Strike 2 match?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-042` — Does the Counter-Strike 2 event have a check-in time or venue requirement?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-079` — How do players check in for Arena of Valor?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-080` — What must players do on site before a Arena of Valor match?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-081` — Does the Arena of Valor event have a check-in time or venue requirement?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.

### en / source_coverage_gap / team_size (3 cases)

- `COMP-RAG-V2-EN-056` — How many starters and substitutes can a Counter-Strike 2 roster include?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-089` — How many starters and substitutes can a Arena of Valor roster include?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-V2-EN-140` — How many starters and substitutes can a VALORANT roster include?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.

## Next Action by Class

- `routing_or_target_failure`: inspect Question Frame and target lock before touching retrieval.
- `source_coverage_gap`: add or approve a source section; keep the safe no-answer until then.
- `gold_or_section_contract_gap`: review section bundles and create reviewed Gold, without widening current Gold silently.
- `english_localization_gap`: approve an English overlay tied to the current Thai source hash.
- `safe_outcome_contract_gap`: decide whether the corpus expects clarification or no-answer, then make that distinction explicit.
- `answer_contract_failure`: inspect the validator error and evidence metadata before changing wording.
