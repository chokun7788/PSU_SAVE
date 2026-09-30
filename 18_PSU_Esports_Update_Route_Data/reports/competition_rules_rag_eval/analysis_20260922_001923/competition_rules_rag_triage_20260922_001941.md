# Competition Rules RAG: Automated Failure Triage

## Input Reports

- `competition_rules_rag_eval_20260922_001923.json`

## Summary

| Locale | Passed | Total | Failed |
| --- | ---: | ---: | ---: |
| en | 178 | 264 | 86 |

## Failure Taxonomy

| Classification | Count | Meaning |
| --- | ---: | --- |
| `gold_or_section_contract_gap` | 82 | The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list. |
| `routing_or_target_failure` | 4 | The request did not retain the expected competition route or rulebook target. |

## Review Queue

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

### en / gold_or_section_contract_gap / dispute (10 cases)

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

### en / gold_or_section_contract_gap / fair_play_conduct (11 cases)

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
- `COMP-RAG-EN-217` — What do the VALORANT tournament rules say about fair play and prohibited conduct?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Overview of Document: Equipment and peripherals In LAN competitions, players must strictly adhere to equipment requirements for fairness. - Competition Venue and Regulations: Competition Area and Re...
- `COMP-RAG-EN-218` — For Valorant, can you verify the rule on fair play and prohibited conduct?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Overview of Document: Equipment and peripherals In LAN competitions, players must strictly adhere to equipment requirements for fairness. - Competition Venue and Regulations: Competition Area and Re...
- `COMP-RAG-EN-219` — I am preparing for a Valo match. What is the policy for fair play and prohibited conduct?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Venue and Regulations: Competition Area and Regulations * Personnel: During Match Prep, no more than 6 players may be present. * Electronic devices: Mobile phones, tablets, and smartwatc...
- `COMP-RAG-EN-220` — Please retrieve the official VALORANT rulebook evidence for fair play and prohibited conduct.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Overview of Document: Equipment and peripherals In LAN competitions, players must strictly adhere to equipment requirements for fairness. - Competition Venue and Regulations: Competition Area and Re...
- `COMP-RAG-EN-221` — How is fair play and prohibited conduct handled in the Valorant tournament rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Overview of Document: Equipment and peripherals In LAN competitions, players must strictly adhere to equipment requirements for fairness. - Competition Venue and Regulations: Competition Area and Re...

### en / gold_or_section_contract_gap / in_match_operations (6 cases)

- `COMP-RAG-EN-223` — What do the VALORANT tournament rules say about in-match procedure?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Venue and Regulations: Competition Area and Regulations * Personnel: During Match Prep, no more than 6 players may be present. * Electronic devices: Mobile phones, tablets, and smartwatc...
- `COMP-RAG-EN-224` — For Valorant, can you verify the rule on in-match procedure?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Venue and Regulations: Competition Area and Regulations * Personnel: During Match Prep, no more than 6 players may be present. * Electronic devices: Mobile phones, tablets, and smartwatc...
- `COMP-RAG-EN-225` — I am preparing for a Valo match. What is the policy for in-match procedure?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Venue and Regulations: Competition Area and Regulations * Personnel: During Match Prep, no more than 6 players may be present. * Electronic devices: Mobile phones, tablets, and smartwatc...
- `COMP-RAG-EN-226` — Please retrieve the official VALORANT rulebook evidence for in-match procedure.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Venue and Regulations: Competition Area and Regulations * Personnel: During Match Prep, no more than 6 players may be present. * Electronic devices: Mobile phones, tablets, and smartwatc...
- `COMP-RAG-EN-227` — How is in-match procedure handled in the Valorant tournament rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Venue and Regulations: Competition Area and Regulations * Personnel: During Match Prep, no more than 6 players may be present. * Electronic devices: Mobile phones, tablets, and smartwatc...
- `COMP-RAG-EN-228` — Could you cite the Valo rule concerning in-match procedure?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Area and Regulations: ... * Only drinking water in a sealed container and chewing gum are permitted. Match Procedure - Post-Match Procedure * Result recording * Officials will immediatel...

### en / gold_or_section_contract_gap / penalty (9 cases)

- `COMP-RAG-EN-067` — What do the CS2 tournament rules say about penalties?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. Penalty Table (Penalties) Violation Penalty Insulting / using verbal aggression Warning → Loss in that round → Disqualification Cheating in any form Loss in that round / Di...
- `COMP-RAG-EN-068` — For Counter-Strike 2, can you verify the rule on penalties?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. Penalty Table (Penalties) Violation Penalty Insulting / using verbal aggression Warning → Loss in that round → Disqualification Cheating in any form Loss in that round / Di...
- `COMP-RAG-EN-069` — I am preparing for a Counter Strike 2 match. What is the policy for penalties?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. Penalty Table (Penalties) Violation Penalty Insulting / using verbal aggression Warning → Loss in that round → Disqualification Cheating in any form Loss in that round / Di...
- `COMP-RAG-EN-070` — Please retrieve the official CS2 rulebook evidence for penalties.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. Penalty Table (Penalties) Violation Penalty Insulting / using verbal aggression Warning → Loss in that round → Disqualification Cheating in any form Loss in that round / Di...
- `COMP-RAG-EN-071` — How is penalties handled in the Counter-Strike 2 tournament rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. Penalty Table (Penalties) Violation Penalty Insulting / using verbal aggression Warning → Loss in that round → Disqualification Cheating in any form Loss in that round / Di...
- `COMP-RAG-EN-072` — Could you cite the Counter Strike 2 rule concerning penalties?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. Penalty Table (Penalties) Violation Penalty Insulting / using verbal aggression Warning → Loss in that round → Disqualification Cheating in any form Loss in that round / Di...
- `COMP-RAG-EN-242` — For Valorant, can you verify the rule on penalties?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Post-Match Procedure * Result recording * Officials will immediately verify and record match results. * Forfeiture * If a forfeit occurs, the result for that map will be recorded as 13-0. Match Paus...
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
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. Penalty Table (Penalties) Violation Penalty Insulting / using verbal aggression Warning → Loss in that round → Disqualification Cheating in any form Loss in that round / Di...
- `COMP-RAG-EN-074` — For Counter-Strike 2, can you verify the rule on the penalty matrix?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. Penalty Table (Penalties) Violation Penalty Insulting / using verbal aggression Warning → Loss in that round → Disqualification Cheating in any form Loss in that round / Di...
- `COMP-RAG-EN-075` — I am preparing for a Counter Strike 2 match. What is the policy for the penalty matrix?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. Penalty Table (Penalties) Violation Penalty Insulting / using verbal aggression Warning → Loss in that round → Disqualification Cheating in any form Loss in that round / Di...
- `COMP-RAG-EN-076` — Please retrieve the official CS2 rulebook evidence for the penalty matrix.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. Penalty Table (Penalties) Violation Penalty Insulting / using verbal aggression Warning → Loss in that round → Disqualification Cheating in any form Loss in that round / Di...
- `COMP-RAG-EN-077` — How is the penalty matrix handled in the Counter-Strike 2 tournament rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. Penalty Table (Penalties) Violation Penalty Insulting / using verbal aggression Warning → Loss in that round → Disqualification Cheating in any form Loss in that round / Di...
- `COMP-RAG-EN-078` — Could you cite the Counter Strike 2 rule concerning the penalty matrix?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. Penalty Table (Penalties) Violation Penalty Insulting / using verbal aggression Warning → Loss in that round → Disqualification Cheating in any form Loss in that round / Di...

### en / gold_or_section_contract_gap / pre_match_on_site (10 cases)

- `COMP-RAG-EN-079` — What do the CS2 tournament rules say about check-in and the competition area?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Players are not allowed to bring notes or documents into the arena, but team leaders may bring them in and must provide their documents to the referees prior to each match: Players are not a...
- `COMP-RAG-EN-080` — For Counter-Strike 2, can you verify the rule on check-in and the competition area?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Players are not allowed to bring notes or documents into the arena, but team leaders may bring them in and must provide their documents to the referees prior to each match: Players are not a...
- `COMP-RAG-EN-081` — I am preparing for a Counter Strike 2 match. What is the policy for check-in and the competition area?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Players are not allowed to bring notes or documents into the arena, but team leaders may bring them in and must provide their documents to the referees prior to each match: Players are not a...
- `COMP-RAG-EN-082` — Please retrieve the official CS2 rulebook evidence for check-in and the competition area.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Players are not allowed to bring notes or documents into the arena, but team leaders may bring them in and must provide their documents to the referees prior to each match: Players are not a...
- `COMP-RAG-EN-083` — How is check-in and the competition area handled in the Counter-Strike 2 tournament rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Players are not allowed to bring notes or documents into the arena, but team leaders may bring them in and must provide their documents to the referees prior to each match: Players are not a...
- `COMP-RAG-EN-084` — Could you cite the Counter Strike 2 rule concerning check-in and the competition area?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Players are not allowed to bring notes or documents into the arena, but team leaders may bring them in and must provide their documents to the referees prior to each match: Players are not a...
- `COMP-RAG-EN-247` — What do the VALORANT tournament rules say about check-in and the competition area?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Venue and Regulations: ... * Electronic devices: Mobile phones, tablets, and smartwatches may not be brought into the competition area until the match ends. * Documents and notes: Player...
- `COMP-RAG-EN-248` — For Valorant, can you verify the rule on check-in and the competition area?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Venue and Regulations: ... * Electronic devices: Mobile phones, tablets, and smartwatches may not be brought into the competition area until the match ends. * Documents and notes: Player...
- `COMP-RAG-EN-250` — Please retrieve the official VALORANT rulebook evidence for check-in and the competition area.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Venue and Regulations: ... * Electronic devices: Mobile phones, tablets, and smartwatches may not be brought into the competition area until the match ends. * Documents and notes: Player...
- `COMP-RAG-EN-251` — How is check-in and the competition area handled in the Valorant tournament rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Venue and Regulations: ... * Electronic devices: Mobile phones, tablets, and smartwatches may not be brought into the competition area until the match ends. * Documents and notes: Player...

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
  - Output: English draft translation of Tekken 8 competition rules: - Dispute Resolution * Any issues must be reported to the competition organizer immediately. * In cases of disputes or protests, the decision of the supervisors or referees shall be final. Note: The c...
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

### en / gold_or_section_contract_gap / schedule (1 cases)

- `COMP-RAG-EN-105` — I am preparing for a Counter Strike 2 match. What is the policy for the tournament schedule?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Competition time: The tournament schedule will be announced at least one day in advance. Participants must confirm their attendance before each match begins. Late arrivals may be disqualifie...

### en / gold_or_section_contract_gap / team_size (6 cases)

- `COMP-RAG-EN-253` — What do the VALORANT tournament rules say about team size and roster composition?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Emergency Pause Clause (Player Emergency Pause): 3. Player Emergency Pause * One request per map is allowed. * Total emergency-pause time may not exceed 10 minutes per match. If that limit is exceed...
- `COMP-RAG-EN-254` — For Valorant, can you verify the rule on team size and roster composition?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Emergency Pause Clause (Player Emergency Pause): 3. Player Emergency Pause * One request per map is allowed. * Total emergency-pause time may not exceed 10 minutes per match. If that limit is exceed...
- `COMP-RAG-EN-255` — I am preparing for a Valo match. What is the policy for team size and roster composition?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Area and Regulations * Personnel during Match Preparation * No more than 6 players are allowed in the match preparation area. * Electronic devices * Mobile phones, tablets, and smartwatc...
- `COMP-RAG-EN-256` — Please retrieve the official VALORANT rulebook evidence for team size and roster composition.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Emergency Pause Clause (Player Emergency Pause): 3. Player Emergency Pause * One request per map is allowed. * Total emergency-pause time may not exceed 10 minutes per match. If that limit is exceed...
- `COMP-RAG-EN-257` — How is team size and roster composition handled in the Valorant tournament rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Emergency Pause Clause (Player Emergency Pause): 3. Player Emergency Pause * One request per map is allowed. * Total emergency-pause time may not exceed 10 minutes per match. If that limit is exceed...
- `COMP-RAG-EN-258` — Could you cite the Valo rule concerning team size and roster composition?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Area and Regulations * Personnel during Match Preparation * No more than 6 players are allowed in the match preparation area. * Electronic devices * Mobile phones, tablets, and smartwatc...

### en / routing_or_target_failure / pause_timeout (2 cases)

- `COMP-RAG-EN-263` — How do CS2 and VALORANT technical pause rules differ?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The request did not retain the expected competition route or rulebook target.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Technical Game Pauses: Each team may pause the game twice, each pause not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.: Technical game pauses allowed pe...
- `COMP-RAG-EN-264` — Compare the pause penalty rules for RoV and TEKKEN 8.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The request did not retain the expected competition route or rulebook target.
  - Output: English draft translation of ROV competition rules: - Competition Rules 4. Regulations and Competition Rules 4.1. Basic Rules 4.1.1. Prohibited to use character names or phrases that are offensive or disrespectful toward others. - Competition Rules: ... 4.5...

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

## Next Action by Class

- `routing_or_target_failure`: inspect Question Frame and target lock before touching retrieval.
- `source_coverage_gap`: add or approve a source section; keep the safe no-answer until then.
- `gold_or_section_contract_gap`: review section bundles and create reviewed Gold, without widening current Gold silently.
- `english_localization_gap`: approve an English overlay tied to the current Thai source hash.
- `safe_outcome_contract_gap`: decide whether the corpus expects clarification or no-answer, then make that distinction explicit.
- `answer_contract_failure`: inspect the validator error and evidence metadata before changing wording.
