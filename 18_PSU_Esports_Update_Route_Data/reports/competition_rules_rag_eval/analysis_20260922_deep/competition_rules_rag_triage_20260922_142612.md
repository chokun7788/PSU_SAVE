# Competition Rules RAG: Automated Failure Triage

## Input Reports

- `competition_rules_rag_eval_20260922_133558.json`
- `competition_rules_rag_eval_20260922_134131.json`

## Summary

| Locale | Passed | Total | Failed |
| --- | ---: | ---: | ---: |
| en | 203 | 264 | 61 |
| th | 211 | 264 | 53 |

## Failure Taxonomy

| Classification | Count | Meaning |
| --- | ---: | --- |
| `gold_or_section_contract_gap` | 72 | The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list. |
| `source_coverage_gap` | 36 | The selected rulebook has no retrieved section that directly proves the requested facet. |
| `routing_or_target_failure` | 4 | The request did not retain the expected competition route or rulebook target. |
| `english_localization_gap` | 2 | The Thai target source was found, but no approved English overlay was available. |

## Review Queue

### en / english_localization_gap / rulebook_identity (2 cases)

- `COMP-RAG-EN-201` — I am preparing for a T8 match. What is the policy for the rulebook scope and tournament identity?
  - Expected: `answer_available`; actual: `localization_pending` via `pipeline:missing_english_localization`
  - Reason: The Thai target source was found, but no approved English overlay was available.
  - Output: This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation. Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- `COMP-RAG-EN-204` — Could you cite the T8 rule concerning the rulebook scope and tournament identity?
  - Expected: `answer_available`; actual: `localization_pending` via `pipeline:missing_english_localization`
  - Reason: The Thai target source was found, but no approved English overlay was available.
  - Output: This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation. Source: https://esports.computing.psu.ac.th/ (original source in Thai)

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

### en / gold_or_section_contract_gap / fair_play_conduct (6 cases)

- `COMP-RAG-EN-217` — What do the VALORANT tournament rules say about fair play and prohibited conduct?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Overview of Document: Equipment and peripherals In LAN competitions, players must strictly adhere to equipment requirements for fairness. - Competition Area and Regulations * Personnel during Match ...
- `COMP-RAG-EN-218` — For Valorant, can you verify the rule on fair play and prohibited conduct?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Overview of Document: Equipment and peripherals In LAN competitions, players must strictly adhere to equipment requirements for fairness. - A bug is an in-game error that causes unintended outcomes....
- `COMP-RAG-EN-219` — I am preparing for a Valo match. What is the policy for fair play and prohibited conduct?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Area and Regulations * Personnel during Match Preparation * No more than 6 players are allowed in the match preparation area. * Electronic devices * Mobile phones, tablets, and smartwatc...
- `COMP-RAG-EN-220` — Please retrieve the official VALORANT rulebook evidence for fair play and prohibited conduct.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Overview of Document: Equipment and peripherals In LAN competitions, players must strictly adhere to equipment requirements for fairness. - Competition Area and Regulations * Personnel during Match ...
- `COMP-RAG-EN-221` — How is fair play and prohibited conduct handled in the Valorant tournament rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Overview of Document: Equipment and peripherals In LAN competitions, players must strictly adhere to equipment requirements for fairness. - Competition Area and Regulations * Personnel during Match ...
- `COMP-RAG-EN-222` — Could you cite the Valo rule concerning fair play and prohibited conduct?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Area and Regulations * Personnel during Match Preparation * No more than 6 players are allowed in the match preparation area. * Electronic devices * Mobile phones, tablets, and smartwatc...

### en / gold_or_section_contract_gap / in_match_operations (6 cases)

- `COMP-RAG-EN-223` — What do the VALORANT tournament rules say about in-match procedure?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Area and Regulations: ... * Only drinking water in a sealed container and chewing gum are permitted. Match Procedure - Post-Match Procedure * Result recording * Officials will immediatel...
- `COMP-RAG-EN-224` — For Valorant, can you verify the rule on in-match procedure?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Area and Regulations: ... * Only drinking water in a sealed container and chewing gum are permitted. Match Procedure - Post-Match Procedure * Result recording * Officials will immediatel...
- `COMP-RAG-EN-225` — I am preparing for a Valo match. What is the policy for in-match procedure?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Area and Regulations: ... * Only drinking water in a sealed container and chewing gum are permitted. Match Procedure - Post-Match Procedure * Result recording * Officials will immediatel...
- `COMP-RAG-EN-226` — Please retrieve the official VALORANT rulebook evidence for in-match procedure.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Area and Regulations: ... * Only drinking water in a sealed container and chewing gum are permitted. Match Procedure - Post-Match Procedure * Result recording * Officials will immediatel...
- `COMP-RAG-EN-227` — How is in-match procedure handled in the Valorant tournament rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Area and Regulations: ... * Only drinking water in a sealed container and chewing gum are permitted. Match Procedure - Post-Match Procedure * Result recording * Officials will immediatel...
- `COMP-RAG-EN-228` — Could you cite the Valo rule concerning in-match procedure?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Competition Area and Regulations: ... * Only drinking water in a sealed container and chewing gum are permitted. Match Procedure - Post-Match Procedure * Result recording * Officials will immediatel...

### en / gold_or_section_contract_gap / penalty (10 cases)

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
  - Output: English draft translation of VALORANT competition rules: - A bug is an in-game error that causes unintended outcomes. Bugs are classified as follows: Using teammates to boost to locations higher than normal jump height is prohibited. Penalties Officials wil...
- `COMP-RAG-EN-243` — I am preparing for a Valo match. What is the policy for penalties?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Using bugs caused by the player themselves to gain unintended advantages is considered a violation. - A bug is an in-game error that causes unintended outcomes. Bugs are classified as follows: Using...
- `COMP-RAG-EN-244` — Please retrieve the official VALORANT rulebook evidence for penalties.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - A bug is an in-game error that causes unintended outcomes. Bugs are classified as follows: Using teammates to boost to locations higher than normal jump height is prohibited. Penalties Officials wil...
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

### en / gold_or_section_contract_gap / pre_match_on_site (2 cases)

- `COMP-RAG-EN-141` — I am preparing for a AOV match. What is the policy for check-in and the competition area?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - Competition Schedule 1.1. Offline event on September 11, 2025 · Registration: 8:00–8:30 AM · Draw of brackets: 8:30–8:40 AM · Round of 5 teams, Single Elimination BO3: 8:40–10:00 AM · Se...
- `COMP-RAG-EN-142` — Please retrieve the official RoV rulebook evidence for check-in and the competition area.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - Competition Rules: ... If there is evidence that a competitor intentionally pauses the game, whether at a critical moment or to disrupt play, the offending team immediately forfeits the ...

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
  - Output: English draft translation of Tekken 8 competition rules: - Dispute Resolution * Any issues must be reported to the competition organizer immediately. * In cases of disputes or protests, the decision of the supervisors or referees shall be final. Note: The c...
- `COMP-RAG-EN-194` — For Tekken 8, can you verify the rule on dispute resolution?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Tekken 8 competition rules: - Dispute Resolution * Any issues must be reported to the competition organizer immediately. * In cases of disputes or protests, the decision of the supervisors or referees shall be final. Note: The c...
- `COMP-RAG-EN-195` — I am preparing for a T8 match. What is the policy for dispute resolution?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Tekken 8 competition rules: - Dispute Resolution * Any issues must be reported to the competition organizer immediately. * In cases of disputes or protests, the decision of the supervisors or referees shall be final. Note: The c...
- `COMP-RAG-EN-196` — Please retrieve the official TEKKEN 8 rulebook evidence for dispute resolution.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Tekken 8 competition rules: - Dispute Resolution * Any issues must be reported to the competition organizer immediately. * In cases of disputes or protests, the decision of the supervisors or referees shall be final. Note: The c...
- `COMP-RAG-EN-197` — How is dispute resolution handled in the Tekken 8 tournament rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Tekken 8 competition rules: - Dispute Resolution * Any issues must be reported to the competition organizer immediately. * In cases of disputes or protests, the decision of the supervisors or referees shall be final. Note: The c...
- `COMP-RAG-EN-198` — Could you cite the T8 rule concerning dispute resolution?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Tekken 8 competition rules: - Dispute Resolution * Any issues must be reported to the competition organizer immediately. * In cases of disputes or protests, the decision of the supervisors or referees shall be final. Note: The c...

### en / gold_or_section_contract_gap / rulebook_identity (1 cases)

- `COMP-RAG-EN-154` — Please retrieve the official RoV rulebook evidence for the rulebook scope and tournament identity.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - Competition Rules: 4.3.2. If a competitor disconnects because of force majeure (such as an internet-service outage across the area or a game-server error), the affected team must notify ...

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
  - Output: English draft translation of ROV competition rules: - Competition Rules 4. Regulations and Competition Rules 4.1. Basic Rules 4.1.1. Prohibited to use character names or phrases that are offensive or disrespectful toward others. - Competition Rules: ... If ...

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
