# Competition Rules RAG: Automated Failure Triage

## Input Reports

- `competition_rules_rag_eval_20260921_220602.json`

## Summary

| Locale | Passed | Total | Failed |
| --- | ---: | ---: | ---: |
| en | 156 | 264 | 108 |
| th | 209 | 264 | 55 |

## Failure Taxonomy

| Classification | Count | Meaning |
| --- | ---: | --- |
| `gold_or_section_contract_gap` | 83 | The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list. |
| `source_coverage_gap` | 74 | The selected rulebook has no retrieved section that directly proves the requested facet. |
| `routing_or_target_failure` | 6 | The request did not retain the expected competition route or rulebook target. |

## Review Queue

### en / gold_or_section_contract_gap / conduct (1 cases)

- `COMP-RAG-EN-171` — I am preparing for a T8 match. What is the policy for player conduct and sportsmanship?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Tekken 8 competition rules: - Competition Rules * Offline mode * PlayStation 5 console used * Singles (1v1) format * Match format: * FT2: Winner is the first to win two games * Each game uses R3 rules (3 rounds per game) and 60S...

### en / gold_or_section_contract_gap / disconnect (6 cases)

- `COMP-RAG-EN-121` — What do the RoV tournament rules say about disconnections and reconnects?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - Competition Rules: 4.5.1.2 In cases where the game is paused due to technical issues, not caused by player actions, the event staff may order a pause and require players to rejoin the ga...
- `COMP-RAG-EN-122` — For Arena of Valor, can you verify the rule on disconnections and reconnects?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - Competition Rules: 4.5.1.2 In cases where the game is paused due to technical issues, not caused by player actions, the event staff may order a pause and require players to rejoin the ga...
- `COMP-RAG-EN-123` — I am preparing for a AOV match. What is the policy for disconnections and reconnects?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - Competition Rules: 4.5.1.2 In cases where the game is paused due to technical issues, not caused by player actions, the event staff may order a pause and require players to rejoin the ga...
- `COMP-RAG-EN-124` — Please retrieve the official RoV rulebook evidence for disconnections and reconnects.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - Competition Rules: 4.5.1.2 In cases where the game is paused due to technical issues, not caused by player actions, the event staff may order a pause and require players to rejoin the ga...
- `COMP-RAG-EN-125` — How is disconnections and reconnects handled in the Arena of Valor tournament rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - Competition Rules: 4.5.1.2 In cases where the game is paused due to technical issues, not caused by player actions, the event staff may order a pause and require players to rejoin the ga...
- `COMP-RAG-EN-126` — Could you cite the AOV rule concerning disconnections and reconnects?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - Competition Rules: 4.5.1.2 In cases where the game is paused due to technical issues, not caused by player actions, the event staff may order a pause and require players to rejoin the ga...

### en / gold_or_section_contract_gap / dispute (11 cases)

- `COMP-RAG-EN-013` — What do the CS2 tournament rules say about protests and disputes?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - PSU Phuket CS2 2026 Tournament - Overview of Document: Competition Rules and Format for Counter-Strike 2 - 1. General Information Source: https://esports.computing.psu.ac.th/ (original sourc...
- `COMP-RAG-EN-014` — For Counter-Strike 2, can you verify the rule on protests and disputes?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Overview of Document: Competition Rules and Format for Counter-Strike 2 - PSU Phuket CS2 2026 Tournament - 1. General Information Source: https://esports.computing.psu.ac.th/ (original sourc...
- `COMP-RAG-EN-015` — I am preparing for a Counter Strike 2 match. What is the policy for protests and disputes?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Overview of Document: Competition Rules and Format for Counter-Strike 2 - PSU Phuket CS2 2026 Tournament - 1. General Information Source: https://esports.computing.psu.ac.th/ (original sourc...
- `COMP-RAG-EN-016` — Please retrieve the official CS2 rulebook evidence for protests and disputes.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Overview of Document: Competition Rules and Format for Counter-Strike 2 - PSU Phuket CS2 2026 Tournament - 1. General Information Source: https://esports.computing.psu.ac.th/ (original sourc...
- `COMP-RAG-EN-017` — How is protests and disputes handled in the Counter-Strike 2 tournament rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - PSU Phuket CS2 2026 Tournament - Overview of Document: Competition Rules and Format for Counter-Strike 2 - 1. General Information Source: https://esports.computing.psu.ac.th/ (original sourc...
- `COMP-RAG-EN-018` — Could you cite the Counter Strike 2 rule concerning protests and disputes?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Overview of Document: Competition Rules and Format for Counter-Strike 2 - PSU Phuket CS2 2026 Tournament - 1. General Information Source: https://esports.computing.psu.ac.th/ (original sourc...
- `COMP-RAG-EN-175` — What do the TEKKEN 8 tournament rules say about protests and disputes?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Tekken 8 competition rules: - Overview of Document: Competition Rules and Format for Tekken 8 Event PSU Esports Clash - Competition Rules * Offline mode * PlayStation 5 console used * Singles (1v1) format * Match format: * FT2: ...
- `COMP-RAG-EN-176` — For Tekken 8, can you verify the rule on protests and disputes?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Tekken 8 competition rules: - Overview of Document: Competition Rules and Format for Tekken 8 Event PSU Esports Clash - Competition Rules * Offline mode * PlayStation 5 console used * Singles (1v1) format * Match format: * FT2: ...
- `COMP-RAG-EN-177` — I am preparing for a T8 match. What is the policy for protests and disputes?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Tekken 8 competition rules: - Competition Rules * Offline mode * PlayStation 5 console used * Singles (1v1) format * Match format: * FT2: Winner is the first to win two games * Each game uses R3 rules (3 rounds per game) and 60S...
- `COMP-RAG-EN-178` — Please retrieve the official TEKKEN 8 rulebook evidence for protests and disputes.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Tekken 8 competition rules: - Overview of Document: Competition Rules and Format for Tekken 8 Event PSU Esports Clash - Competition Rules * Offline mode * PlayStation 5 console used * Singles (1v1) format * Match format: * FT2: ...
- `COMP-RAG-EN-179` — How is protests and disputes handled in the Tekken 8 tournament rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Tekken 8 competition rules: - Overview of Document: Competition Rules and Format for Tekken 8 Event PSU Esports Clash - Competition Rules * Offline mode * PlayStation 5 console used * Singles (1v1) format * Match format: * FT2: ...

### en / gold_or_section_contract_gap / equipment (5 cases)

- `COMP-RAG-EN-212` — For Valorant, can you verify the rule on competition equipment and devices?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Organizers reserve the right to amend or modify competition rules without prior notice: The Organizer reserves the right to modify or amend the regulations without prior notice. - Competition Area a...
- `COMP-RAG-EN-213` — I am preparing for a Valo match. What is the policy for competition equipment and devices?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Organizers reserve the right to amend or modify competition rules without prior notice: The Organizer reserves the right to modify or amend the regulations without prior notice. - Competition Area a...
- `COMP-RAG-EN-214` — Please retrieve the official VALORANT rulebook evidence for competition equipment and devices.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Organizers reserve the right to amend or modify competition rules without prior notice: The Organizer reserves the right to modify or amend the regulations without prior notice. - Competition Area a...
- `COMP-RAG-EN-215` — How is competition equipment and devices handled in the Valorant tournament rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Organizers reserve the right to amend or modify competition rules without prior notice: The Organizer reserves the right to modify or amend the regulations without prior notice. - Competition Area a...
- `COMP-RAG-EN-216` — Could you cite the Valo rule concerning competition equipment and devices?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Organizers reserve the right to amend or modify competition rules without prior notice: The Organizer reserves the right to modify or amend the regulations without prior notice. - Competition Area a...

### en / gold_or_section_contract_gap / fair_play_conduct (6 cases)

- `COMP-RAG-EN-031` — What do the CS2 tournament rules say about fair play and prohibited conduct?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Player Etiquette: Prohibit aggressive behavior, offensive language (including racial/religious slurs), and actions lacking sportsmanship: Player etiquette: Prohibited behaviors include aggre...
- `COMP-RAG-EN-032` — For Counter-Strike 2, can you verify the rule on fair play and prohibited conduct?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Player Etiquette: Prohibit aggressive behavior, offensive language (including racial/religious slurs), and actions lacking sportsmanship: Player etiquette: Prohibited behaviors include aggre...
- `COMP-RAG-EN-033` — I am preparing for a Counter Strike 2 match. What is the policy for fair play and prohibited conduct?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Player Etiquette: Prohibit aggressive behavior, offensive language (including racial/religious slurs), and actions lacking sportsmanship: Player etiquette: Prohibited behaviors include aggre...
- `COMP-RAG-EN-034` — Please retrieve the official CS2 rulebook evidence for fair play and prohibited conduct.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Player Etiquette: Prohibit aggressive behavior, offensive language (including racial/religious slurs), and actions lacking sportsmanship: Player etiquette: Prohibited behaviors include aggre...
- `COMP-RAG-EN-035` — How is fair play and prohibited conduct handled in the Counter-Strike 2 tournament rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Player Etiquette: Prohibit aggressive behavior, offensive language (including racial/religious slurs), and actions lacking sportsmanship: Player etiquette: Prohibited behaviors include aggre...
- `COMP-RAG-EN-036` — Could you cite the Counter Strike 2 rule concerning fair play and prohibited conduct?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Player Etiquette: Prohibit aggressive behavior, offensive language (including racial/religious slurs), and actions lacking sportsmanship: Player etiquette: Prohibited behaviors include aggre...

### en / gold_or_section_contract_gap / penalty (9 cases)

- `COMP-RAG-EN-067` — What do the CS2 tournament rules say about penalties?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - PSU Phuket CS2 2026 Tournament - Section Title: 8. - Overview of Document: Competition Rules and Format for Counter-Strike 2 Source: https://esports.computing.psu.ac.th/ (original source in ...
- `COMP-RAG-EN-068` — For Counter-Strike 2, can you verify the rule on penalties?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. - Overview of Document: Competition Rules and Format for Counter-Strike 2 - PSU Phuket CS2 2026 Tournament Source: https://esports.computing.psu.ac.th/ (original source in ...
- `COMP-RAG-EN-069` — I am preparing for a Counter Strike 2 match. What is the policy for penalties?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. - Overview of Document: Competition Rules and Format for Counter-Strike 2 - PSU Phuket CS2 2026 Tournament Source: https://esports.computing.psu.ac.th/ (original source in ...
- `COMP-RAG-EN-070` — Please retrieve the official CS2 rulebook evidence for penalties.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. - Overview of Document: Competition Rules and Format for Counter-Strike 2 - PSU Phuket CS2 2026 Tournament Source: https://esports.computing.psu.ac.th/ (original source in ...
- `COMP-RAG-EN-071` — How is penalties handled in the Counter-Strike 2 tournament rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - PSU Phuket CS2 2026 Tournament - Section Title: 8. - Overview of Document: Competition Rules and Format for Counter-Strike 2 Source: https://esports.computing.psu.ac.th/ (original source in ...
- `COMP-RAG-EN-072` — Could you cite the Counter Strike 2 rule concerning penalties?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. - Overview of Document: Competition Rules and Format for Counter-Strike 2 - PSU Phuket CS2 2026 Tournament Source: https://esports.computing.psu.ac.th/ (original source in ...
- `COMP-RAG-EN-242` — For Valorant, can you verify the rule on penalties?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Organizers reserve the right to amend or modify competition rules without prior notice: The Organizer reserves the right to modify or amend the regulations without prior notice. - Post-Match Procedu...
- `COMP-RAG-EN-244` — Please retrieve the official VALORANT rulebook evidence for penalties.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Organizers reserve the right to amend or modify competition rules without prior notice: The Organizer reserves the right to modify or amend the regulations without prior notice. - Pre-Game Process (...
- `COMP-RAG-EN-246` — Could you cite the Valo rule concerning penalties?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - A bug is an in-game error that causes unintended outcomes. Bugs are classified as follows: Using teammates to boost to locations higher than normal jump height is prohibited. Penalties Officials wil...

### en / gold_or_section_contract_gap / penalty_matrix (6 cases)

- `COMP-RAG-EN-073` — What do the CS2 tournament rules say about the penalty matrix?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. - PSU Phuket CS2 2026 Tournament - 1. General Information Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- `COMP-RAG-EN-074` — For Counter-Strike 2, can you verify the rule on the penalty matrix?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. - PSU Phuket CS2 2026 Tournament - 1. General Information Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- `COMP-RAG-EN-075` — I am preparing for a Counter Strike 2 match. What is the policy for the penalty matrix?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. - PSU Phuket CS2 2026 Tournament - 1. General Information Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- `COMP-RAG-EN-076` — Please retrieve the official CS2 rulebook evidence for the penalty matrix.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. - PSU Phuket CS2 2026 Tournament - 1. General Information Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- `COMP-RAG-EN-077` — How is the penalty matrix handled in the Counter-Strike 2 tournament rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. - PSU Phuket CS2 2026 Tournament - 1. General Information Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- `COMP-RAG-EN-078` — Could you cite the Counter Strike 2 rule concerning the penalty matrix?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. - PSU Phuket CS2 2026 Tournament - 1. General Information Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### en / gold_or_section_contract_gap / pre_match_on_site (4 cases)

- `COMP-RAG-EN-247` — What do the VALORANT tournament rules say about check-in and the competition area?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Venue and Regulations * During Match Prep, the number of personnel allowed on-site shall not exceed six players. * Electronic devices: Mobile phones, tablets, or smartwatches are prohibi...
- `COMP-RAG-EN-248` — For Valorant, can you verify the rule on check-in and the competition area?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Venue and Regulations * During Match Prep, the number of personnel allowed on-site shall not exceed six players. * Electronic devices: Mobile phones, tablets, or smartwatches are prohibi...
- `COMP-RAG-EN-250` — Please retrieve the official VALORANT rulebook evidence for check-in and the competition area.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Venue and Regulations * During Match Prep, the number of personnel allowed on-site shall not exceed six players. * Electronic devices: Mobile phones, tablets, or smartwatches are prohibi...
- `COMP-RAG-EN-251` — How is check-in and the competition area handled in the Valorant tournament rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Venue and Regulations * During Match Prep, the number of personnel allowed on-site shall not exceed six players. * Electronic devices: Mobile phones, tablets, or smartwatches are prohibi...

### en / gold_or_section_contract_gap / protest_dispute (12 cases)

- `COMP-RAG-EN-085` — What do the CS2 tournament rules say about dispute resolution?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Players may customize brightness, resolution, and crosshair settings only within the game and computer display: Players may customize brightness, resolution, and crosshair settings only with...
- `COMP-RAG-EN-086` — For Counter-Strike 2, can you verify the rule on dispute resolution?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Players may customize brightness, resolution, and crosshair settings only within the game and computer display: Players may customize brightness, resolution, and crosshair settings only with...
- `COMP-RAG-EN-087` — I am preparing for a Counter Strike 2 match. What is the policy for dispute resolution?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Players may customize brightness, resolution, and crosshair settings only within the game and computer display: Players may customize brightness, resolution, and crosshair settings only with...
- `COMP-RAG-EN-088` — Please retrieve the official CS2 rulebook evidence for dispute resolution.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Players may customize brightness, resolution, and crosshair settings only within the game and computer display: Players may customize brightness, resolution, and crosshair settings only with...
- `COMP-RAG-EN-089` — How is dispute resolution handled in the Counter-Strike 2 tournament rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Players may customize brightness, resolution, and crosshair settings only within the game and computer display: Players may customize brightness, resolution, and crosshair settings only with...
- `COMP-RAG-EN-090` — Could you cite the Counter Strike 2 rule concerning dispute resolution?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Players may customize brightness, resolution, and crosshair settings only within the game and computer display: Players may customize brightness, resolution, and crosshair settings only with...
- `COMP-RAG-EN-193` — What do the TEKKEN 8 tournament rules say about dispute resolution?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Tekken 8 competition rules: - Competition Rules * Offline mode * PlayStation 5 console used * Singles (1v1) format * Match format: * FT2: Winner is the first to win two games * Each game uses R3 rules (3 rounds per game) and 60S...
- `COMP-RAG-EN-194` — For Tekken 8, can you verify the rule on dispute resolution?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Tekken 8 competition rules: - Competition Rules * Offline mode * PlayStation 5 console used * Singles (1v1) format * Match format: * FT2: Winner is the first to win two games * Each game uses R3 rules (3 rounds per game) and 60S...
- `COMP-RAG-EN-195` — I am preparing for a T8 match. What is the policy for dispute resolution?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Tekken 8 competition rules: - Competition Rules * Offline mode * PlayStation 5 console used * Singles (1v1) format * Match format: * FT2: Winner is the first to win two games * Each game uses R3 rules (3 rounds per game) and 60S...
- `COMP-RAG-EN-196` — Please retrieve the official TEKKEN 8 rulebook evidence for dispute resolution.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Tekken 8 competition rules: - Competition Rules * Offline mode * PlayStation 5 console used * Singles (1v1) format * Match format: * FT2: Winner is the first to win two games * Each game uses R3 rules (3 rounds per game) and 60S...
- `COMP-RAG-EN-197` — How is dispute resolution handled in the Tekken 8 tournament rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Tekken 8 competition rules: - Competition Rules * Offline mode * PlayStation 5 console used * Singles (1v1) format * Match format: * FT2: Winner is the first to win two games * Each game uses R3 rules (3 rounds per game) and 60S...
- `COMP-RAG-EN-198` — Could you cite the T8 rule concerning dispute resolution?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Tekken 8 competition rules: - Dispute Resolution * Any issues must be reported to the competition organizer immediately. * In cases of disputes or protests, the decision of the supervisors or referees shall be final. Note: The c...

### en / gold_or_section_contract_gap / rulebook_identity (2 cases)

- `COMP-RAG-EN-201` — I am preparing for a T8 match. What is the policy for the rulebook scope and tournament identity?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Tekken 8 competition rules: - Competition Rules * Offline mode * PlayStation 5 console used * Singles (1v1) format * Match format: * FT2: Winner is the first to win two games * Each game uses R3 rules (3 rounds per game) and 60S...
- `COMP-RAG-EN-204` — Could you cite the T8 rule concerning the rulebook scope and tournament identity?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Tekken 8 competition rules: - Competition Rules * Offline mode * PlayStation 5 console used * Singles (1v1) format * Match format: * FT2: Winner is the first to win two games * Each game uses R3 rules (3 rounds per game) and 60S...

### en / gold_or_section_contract_gap / team_size (4 cases)

- `COMP-RAG-EN-253` — What do the VALORANT tournament rules say about team size and roster composition?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Emergency Pause Clause (Player Emergency Pause): Emergency Pause (Player Emergency Pause) * One emergency pause allowed per map * Total duration per match cannot exceed 10 minutes. If exceeded, the ...
- `COMP-RAG-EN-254` — For Valorant, can you verify the rule on team size and roster composition?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Emergency Pause Clause (Player Emergency Pause): Emergency Pause (Player Emergency Pause) * One emergency pause allowed per map * Total duration per match cannot exceed 10 minutes. If exceeded, the ...
- `COMP-RAG-EN-256` — Please retrieve the official VALORANT rulebook evidence for team size and roster composition.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Emergency Pause Clause (Player Emergency Pause): Emergency Pause (Player Emergency Pause) * One emergency pause allowed per map * Total duration per match cannot exceed 10 minutes. If exceeded, the ...
- `COMP-RAG-EN-257` — How is team size and roster composition handled in the Valorant tournament rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Emergency Pause Clause (Player Emergency Pause): Emergency Pause (Player Emergency Pause) * One emergency pause allowed per map * Total duration per match cannot exceed 10 minutes. If exceeded, the ...

### en / routing_or_target_failure / pause_timeout (2 cases)

- `COMP-RAG-EN-263` — How do CS2 and VALORANT technical pause rules differ?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The request did not retain the expected competition route or rulebook target.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Technical Game Pauses: Each team may pause the game twice, each pause not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.: Technical game pauses allowed pe...
- `COMP-RAG-EN-264` — Compare the pause penalty rules for RoV and TEKKEN 8.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The request did not retain the expected competition route or rulebook target.
  - Output: English draft translation of ROV competition rules: - Competition Rules: 4.5.1.2 In cases where the game is paused due to technical issues, not caused by player actions, the event staff may order a pause and require players to rejoin the game after all disc...

### en / routing_or_target_failure / rulebook_identity (1 cases)

- `COMP-RAG-EN-152` — For Arena of Valor, can you verify the rule on the rulebook scope and tournament identity?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The request did not retain the expected competition route or rulebook target.
  - Output: English draft translation of VALORANT competition rules: - Organizers reserve the right to amend or modify competition rules without prior notice: The Organizer reserves the right to modify or amend the regulations without prior notice. - Pre-Game Process (...

### en / routing_or_target_failure / safe_outcome (1 cases)

- `COMP-RAG-EN-260` — How many players can a team have?
  - Expected: `clarification_required`; actual: `no_answer` via `pipeline:english_no_answer`
  - Reason: The request did not retain the expected competition route or rulebook target.
  - Output: I could not find verified PSU Esports Studio - Phuket information for this question.

### en / source_coverage_gap / conduct (6 cases)

- `COMP-RAG-EN-205` — What do the VALORANT tournament rules say about player conduct and sportsmanship?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-206` — For Valorant, can you verify the rule on player conduct and sportsmanship?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-207` — I am preparing for a Valo match. What is the policy for player conduct and sportsmanship?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-208` — Please retrieve the official VALORANT rulebook evidence for player conduct and sportsmanship.
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-209` — How is player conduct and sportsmanship handled in the Valorant tournament rules?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-210` — Could you cite the Valo rule concerning player conduct and sportsmanship?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.

### en / source_coverage_gap / eligibility_registration (6 cases)

- `COMP-RAG-EN-019` — What do the CS2 tournament rules say about eligibility, roster, and registration?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-020` — For Counter-Strike 2, can you verify the rule on eligibility, roster, and registration?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-021` — I am preparing for a Counter Strike 2 match. What is the policy for eligibility, roster, and registration?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-022` — Please retrieve the official CS2 rulebook evidence for eligibility, roster, and registration.
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-023` — How is eligibility, roster, and registration handled in the Counter-Strike 2 tournament rules?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-024` — Could you cite the Counter Strike 2 rule concerning eligibility, roster, and registration?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.

### en / source_coverage_gap / fair_play_conduct (6 cases)

- `COMP-RAG-EN-217` — What do the VALORANT tournament rules say about fair play and prohibited conduct?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-218` — For Valorant, can you verify the rule on fair play and prohibited conduct?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-219` — I am preparing for a Valo match. What is the policy for fair play and prohibited conduct?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-220` — Please retrieve the official VALORANT rulebook evidence for fair play and prohibited conduct.
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-221` — How is fair play and prohibited conduct handled in the Valorant tournament rules?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-222` — Could you cite the Valo rule concerning fair play and prohibited conduct?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.

### en / source_coverage_gap / in_match_operations (6 cases)

- `COMP-RAG-EN-223` — What do the VALORANT tournament rules say about in-match procedure?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-224` — For Valorant, can you verify the rule on in-match procedure?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-225` — I am preparing for a Valo match. What is the policy for in-match procedure?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-226` — Please retrieve the official VALORANT rulebook evidence for in-match procedure.
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-227` — How is in-match procedure handled in the Valorant tournament rules?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-228` — Could you cite the Valo rule concerning in-match procedure?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.

### en / source_coverage_gap / pre_match_on_site (12 cases)

- `COMP-RAG-EN-079` — What do the CS2 tournament rules say about check-in and the competition area?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-080` — For Counter-Strike 2, can you verify the rule on check-in and the competition area?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-081` — I am preparing for a Counter Strike 2 match. What is the policy for check-in and the competition area?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-082` — Please retrieve the official CS2 rulebook evidence for check-in and the competition area.
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-083` — How is check-in and the competition area handled in the Counter-Strike 2 tournament rules?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-084` — Could you cite the Counter Strike 2 rule concerning check-in and the competition area?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-139` — What do the RoV tournament rules say about check-in and the competition area?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-140` — For Arena of Valor, can you verify the rule on check-in and the competition area?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-141` — I am preparing for a AOV match. What is the policy for check-in and the competition area?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-142` — Please retrieve the official RoV rulebook evidence for check-in and the competition area.
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-143` — How is check-in and the competition area handled in the Arena of Valor tournament rules?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-144` — Could you cite the AOV rule concerning check-in and the competition area?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.

### en / source_coverage_gap / team_size (2 cases)

- `COMP-RAG-EN-255` — I am preparing for a Valo match. What is the policy for team size and roster composition?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
- `COMP-RAG-EN-258` — Could you cite the Valo rule concerning team size and roster composition?
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer_en`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.

### th / gold_or_section_contract_gap / disconnect (3 cases)

- `COMP-RAG-TH-123` — ขออ้างอิงกติกา อารีน่าออฟเวเลอร์ ในหัวข้อการหลุดจากเกมหรือการเชื่อมต่อ หน่อย
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ  รายละเอียดที่เกี่ยวข้อง: •    4.5.2....
- `COMP-RAG-TH-124` — กำลังจะลงแข่ง RoV อยากรู้เรื่องการหลุดจากเกมหรือการเชื่อมต่อ
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ  รายละเอียดที่เกี่ยวข้อง: •    4.3.2....
- `COMP-RAG-TH-125` — Arena of Valor มีข้อกำหนดเรื่องการหลุดจากเกมหรือการเชื่อมต่อ ไหม
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: 4.5.2.หากเกมหยุดลงเป็นเวลาเกินกว่า 10 นาที ทางทีมงานมีสิทธิสั่งให้เริ่มเกมใหม่ เว้นแต่ทีมผู้เข้าร่วมแข่งขันทีมใดทีมหนึ่งมีคะแนนมากกว่าอีกทีมเป็นจำนวนมาก ทางทีมงานอาจใช้ดุลยพินิจในการสั่งให้ทีมที่มีคะแนนมากกว่าดังกล่าวเป็นผู้ชนะในเกมที่หยุดลงนั้นตามที...

### th / gold_or_section_contract_gap / penalty_matrix (6 cases)

- `COMP-RAG-TH-073` — กติกา CS2 เรื่องตารางบทลงโทษ ว่าอย่างไร
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: ตารางบทลงโทษระบุผลตามประเภทการละเมิดที่ยืนยันได้ เช่น  รายละเอียดที่เกี่ยวข้อง: •    การด่าทอ/ใช้ความรุนแรงทางวาจา -> ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์ •    การโกงทุกรูปแบบ -> ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน •    ดูสตรีมระหว่างแข่ง ->...
- `COMP-RAG-TH-074` — Counter-Strike 2 แข่งจริง กฎเกี่ยวกับตารางบทลงโทษ เป็นแบบไหน
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: ตารางบทลงโทษระบุผลตามประเภทการละเมิดที่ยืนยันได้ เช่น  รายละเอียดที่เกี่ยวข้อง: •    การด่าทอ/ใช้ความรุนแรงทางวาจา -> ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์ •    การโกงทุกรูปแบบ -> ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน •    ดูสตรีมระหว่างแข่ง ->...
- `COMP-RAG-TH-075` — ขออ้างอิงกติกา เคาน์เตอร์สไตรก์ 2 ในหัวข้อตารางบทลงโทษ หน่อย
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: ตารางบทลงโทษระบุผลตามประเภทการละเมิดที่ยืนยันได้ เช่น  รายละเอียดที่เกี่ยวข้อง: •    การด่าทอ/ใช้ความรุนแรงทางวาจา -> ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์ •    การโกงทุกรูปแบบ -> ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน •    ดูสตรีมระหว่างแข่ง ->...
- `COMP-RAG-TH-076` — กำลังจะลงแข่ง CS2 อยากรู้เรื่องตารางบทลงโทษ
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: ตารางบทลงโทษระบุผลตามประเภทการละเมิดที่ยืนยันได้ เช่น  รายละเอียดที่เกี่ยวข้อง: •    การด่าทอ/ใช้ความรุนแรงทางวาจา -> ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์ •    การโกงทุกรูปแบบ -> ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน •    ดูสตรีมระหว่างแข่ง ->...
- `COMP-RAG-TH-077` — Counter-Strike 2 มีข้อกำหนดเรื่องตารางบทลงโทษ ไหม
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: ตารางบทลงโทษระบุผลตามประเภทการละเมิดที่ยืนยันได้ เช่น  รายละเอียดที่เกี่ยวข้อง: •    การด่าทอ/ใช้ความรุนแรงทางวาจา -> ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์ •    การโกงทุกรูปแบบ -> ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน •    ดูสตรีมระหว่างแข่ง ->...
- `COMP-RAG-TH-078` — ตาม rulebook เคาน์เตอร์สไตรก์ 2 ตารางบทลงโทษ ต้องทำยังไง
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: ตารางบทลงโทษระบุผลตามประเภทการละเมิดที่ยืนยันได้ เช่น  รายละเอียดที่เกี่ยวข้อง: •    การด่าทอ/ใช้ความรุนแรงทางวาจา -> ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์ •    การโกงทุกรูปแบบ -> ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน •    ดูสตรีมระหว่างแข่ง ->...

### th / gold_or_section_contract_gap / pre_match_on_site (5 cases)

- `COMP-RAG-TH-247` — กติกา VALORANT เรื่องการรายงานตัวและพื้นที่แข่งขัน ว่าอย่างไร
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: * เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง  รายละเอียดที่เกี่ยวข้อง: •    Check-in time  อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_p...
- `COMP-RAG-TH-248` — Valorant แข่งจริง กฎเกี่ยวกับการรายงานตัวและพื้นที่แข่งขัน เป็นแบบไหน
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: * เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง  รายละเอียดที่เกี่ยวข้อง: •    Check-in time  อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_p...
- `COMP-RAG-TH-249` — ขออ้างอิงกติกา วาโล ในหัวข้อการรายงานตัวและพื้นที่แข่งขัน หน่อย
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: * เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง  รายละเอียดที่เกี่ยวข้อง: •    Check-in time  อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_p...
- `COMP-RAG-TH-250` — กำลังจะลงแข่ง VALORANT อยากรู้เรื่องการรายงานตัวและพื้นที่แข่งขัน
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: * เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง  รายละเอียดที่เกี่ยวข้อง: •    Check-in time  อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_p...
- `COMP-RAG-TH-252` — ตาม rulebook วาโล การรายงานตัวและพื้นที่แข่งขัน ต้องทำยังไง
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: * เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง  รายละเอียดที่เกี่ยวข้อง: •    Check-in time  อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_p...

### th / gold_or_section_contract_gap / team_size (3 cases)

- `COMP-RAG-TH-254` — Valorant แข่งจริง กฎเกี่ยวกับจำนวนผู้เล่นและองค์ประกอบทีม เป็นแบบไหน
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: 3. การหยุดกรณีฉุกเฉิน (Player Emergency Pause)  รายละเอียดที่เกี่ยวข้อง: •    ขอได้ 1 ครั้งต่อแผนที่ •    รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน •    กฎเกี่ยวกับบั๊ก •    บั๊กคือข...
- `COMP-RAG-TH-256` — กำลังจะลงแข่ง VALORANT อยากรู้เรื่องจำนวนผู้เล่นและองค์ประกอบทีม
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: 3. การหยุดกรณีฉุกเฉิน (Player Emergency Pause)  รายละเอียดที่เกี่ยวข้อง: •    ขอได้ 1 ครั้งต่อแผนที่ •    รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน •    กฎเกี่ยวกับบั๊ก •    บั๊กคือข...
- `COMP-RAG-TH-257` — Valorant มีข้อกำหนดเรื่องจำนวนผู้เล่นและองค์ประกอบทีม ไหม
  - Expected: `answer_available`; actual: `answer` via `pipeline:competition_source_rag`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: คำตอบ: 3. การหยุดกรณีฉุกเฉิน (Player Emergency Pause)  รายละเอียดที่เกี่ยวข้อง: •    ขอได้ 1 ครั้งต่อแผนที่ •    รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน •    กฎเกี่ยวกับบั๊ก •    บั๊กคือข...

### th / routing_or_target_failure / match_settings (2 cases)

- `COMP-RAG-TH-189` — ขออ้างอิงกติกา เทคเค่น 8 ในหัวข้อการตั้งค่าในเกม หน่อย
  - Expected: `answer_available`; actual: `clarification` via `pipeline:competition_target_clarification`
  - Reason: The request did not retain the expected competition route or rulebook target.
  - Output: ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT
- `COMP-RAG-TH-192` — ตาม rulebook เทคเค่น 8 การตั้งค่าในเกม ต้องทำยังไง
  - Expected: `answer_available`; actual: `clarification` via `pipeline:competition_target_clarification`
  - Reason: The request did not retain the expected competition route or rulebook target.
  - Output: ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT

### th / source_coverage_gap / conduct (6 cases)

- `COMP-RAG-TH-205` — กติกา VALORANT เรื่องมารยาทและพฤติกรรมผู้เล่น ว่าอย่างไร
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-206` — Valorant แข่งจริง กฎเกี่ยวกับมารยาทและพฤติกรรมผู้เล่น เป็นแบบไหน
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-207` — ขออ้างอิงกติกา วาโล ในหัวข้อมารยาทและพฤติกรรมผู้เล่น หน่อย
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-208` — กำลังจะลงแข่ง VALORANT อยากรู้เรื่องมารยาทและพฤติกรรมผู้เล่น
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-209` — Valorant มีข้อกำหนดเรื่องมารยาทและพฤติกรรมผู้เล่น ไหม
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-210` — ตาม rulebook วาโล มารยาทและพฤติกรรมผู้เล่น ต้องทำยังไง
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### th / source_coverage_gap / fair_play_conduct (6 cases)

- `COMP-RAG-TH-217` — กติกา VALORANT เรื่องfair play และข้อห้าม ว่าอย่างไร
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-218` — Valorant แข่งจริง กฎเกี่ยวกับfair play และข้อห้าม เป็นแบบไหน
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-219` — ขออ้างอิงกติกา วาโล ในหัวข้อfair play และข้อห้าม หน่อย
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-220` — กำลังจะลงแข่ง VALORANT อยากรู้เรื่องfair play และข้อห้าม
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-221` — Valorant มีข้อกำหนดเรื่องfair play และข้อห้าม ไหม
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-222` — ตาม rulebook วาโล fair play และข้อห้าม ต้องทำยังไง
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### th / source_coverage_gap / in_match_operations (6 cases)

- `COMP-RAG-TH-223` — กติกา VALORANT เรื่องขั้นตอนระหว่างการแข่งขัน ว่าอย่างไร
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-224` — Valorant แข่งจริง กฎเกี่ยวกับขั้นตอนระหว่างการแข่งขัน เป็นแบบไหน
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-225` — ขออ้างอิงกติกา วาโล ในหัวข้อขั้นตอนระหว่างการแข่งขัน หน่อย
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-226` — กำลังจะลงแข่ง VALORANT อยากรู้เรื่องขั้นตอนระหว่างการแข่งขัน
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-227` — Valorant มีข้อกำหนดเรื่องขั้นตอนระหว่างการแข่งขัน ไหม
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-228` — ตาม rulebook วาโล ขั้นตอนระหว่างการแข่งขัน ต้องทำยังไง
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### th / source_coverage_gap / match_configuration (6 cases)

- `COMP-RAG-TH-049` — กติกา CS2 เรื่องเวอร์ชันเกมและการตั้งค่าแมตช์ ว่าอย่างไร
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-050` — Counter-Strike 2 แข่งจริง กฎเกี่ยวกับเวอร์ชันเกมและการตั้งค่าแมตช์ เป็นแบบไหน
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-051` — ขออ้างอิงกติกา เคาน์เตอร์สไตรก์ 2 ในหัวข้อเวอร์ชันเกมและการตั้งค่าแมตช์ หน่อย
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-052` — กำลังจะลงแข่ง CS2 อยากรู้เรื่องเวอร์ชันเกมและการตั้งค่าแมตช์
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-053` — Counter-Strike 2 มีข้อกำหนดเรื่องเวอร์ชันเกมและการตั้งค่าแมตช์ ไหม
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-054` — ตาม rulebook เคาน์เตอร์สไตรก์ 2 เวอร์ชันเกมและการตั้งค่าแมตช์ ต้องทำยังไง
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### th / source_coverage_gap / pre_match_on_site (12 cases)

- `COMP-RAG-TH-079` — กติกา CS2 เรื่องการรายงานตัวและพื้นที่แข่งขัน ว่าอย่างไร
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-080` — Counter-Strike 2 แข่งจริง กฎเกี่ยวกับการรายงานตัวและพื้นที่แข่งขัน เป็นแบบไหน
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-081` — ขออ้างอิงกติกา เคาน์เตอร์สไตรก์ 2 ในหัวข้อการรายงานตัวและพื้นที่แข่งขัน หน่อย
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-082` — กำลังจะลงแข่ง CS2 อยากรู้เรื่องการรายงานตัวและพื้นที่แข่งขัน
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-083` — Counter-Strike 2 มีข้อกำหนดเรื่องการรายงานตัวและพื้นที่แข่งขัน ไหม
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-084` — ตาม rulebook เคาน์เตอร์สไตรก์ 2 การรายงานตัวและพื้นที่แข่งขัน ต้องทำยังไง
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-139` — กติกา RoV เรื่องการรายงานตัวและพื้นที่แข่งขัน ว่าอย่างไร
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-140` — Arena of Valor แข่งจริง กฎเกี่ยวกับการรายงานตัวและพื้นที่แข่งขัน เป็นแบบไหน
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-141` — ขออ้างอิงกติกา อารีน่าออฟเวเลอร์ ในหัวข้อการรายงานตัวและพื้นที่แข่งขัน หน่อย
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-142` — กำลังจะลงแข่ง RoV อยากรู้เรื่องการรายงานตัวและพื้นที่แข่งขัน
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-143` — Arena of Valor มีข้อกำหนดเรื่องการรายงานตัวและพื้นที่แข่งขัน ไหม
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
- `COMP-RAG-TH-144` — ตาม rulebook อารีน่าออฟเวเลอร์ การรายงานตัวและพื้นที่แข่งขัน ต้องทำยังไง
  - Expected: `answer_available`; actual: `no_answer` via `pipeline:competition_facet_not_covered_no_answer`
  - Reason: The selected rulebook has no retrieved section that directly proves the requested facet.
  - Output: ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

## Next Action by Class

- `routing_or_target_failure`: inspect Question Frame and target lock before touching retrieval.
- `source_coverage_gap`: add or approve a source section; keep the safe no-answer until then.
- `gold_or_section_contract_gap`: review section bundles and create reviewed Gold, without widening current Gold silently.
- `english_localization_gap`: approve an English overlay tied to the current Thai source hash.
- `safe_outcome_contract_gap`: decide whether the corpus expects clarification or no-answer, then make that distinction explicit.
- `answer_contract_failure`: inspect the validator error and evidence metadata before changing wording.
