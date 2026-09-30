# Competition Rules RAG: Automated Failure Triage

## Input Reports

- `competition_rules_rag_eval_20260921_225158.json`

## Summary

| Locale | Passed | Total | Failed |
| --- | ---: | ---: | ---: |
| en | 198 | 264 | 66 |

## Failure Taxonomy

| Classification | Count | Meaning |
| --- | ---: | --- |
| `gold_or_section_contract_gap` | 62 | The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list. |
| `routing_or_target_failure` | 4 | The request did not retain the expected competition route or rulebook target. |

## Review Queue

### en / gold_or_section_contract_gap / conduct (1 cases)

- `COMP-RAG-EN-207` — I am preparing for a Valo match. What is the policy for player conduct and sportsmanship?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - English translation 3. Player Emergency Pause * Each team may request one pause per map. * Total emergency pause time may not exceed 10 minutes per match. If the time limit is exceeded, the affected...

### en / gold_or_section_contract_gap / disconnect (5 cases)

- `COMP-RAG-EN-121` — What do the RoV tournament rules say about disconnections and reconnects?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - Competition Rules: 4.5.1.2 In cases where the game is paused due to technical issues, not caused by player actions, the event staff may order a pause and require players to rejoin the ga...
- `COMP-RAG-EN-123` — I am preparing for a AOV match. What is the policy for disconnections and reconnects?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - Competition Schedule 1.1. - Competition Rules: 4.5.1.2 In cases where the game is paused due to technical issues, not caused by player actions, the event staff may order a pause and requ...
- `COMP-RAG-EN-124` — Please retrieve the official RoV rulebook evidence for disconnections and reconnects.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - Offenses and Penalties: 6. Misconduct and Penalties 6.1. No competitor shall engage in any of the following acts: 6.1.1. No player shall use inappropriate language or display disrespectf...
- `COMP-RAG-EN-125` — How is disconnections and reconnects handled in the Arena of Valor tournament rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - Competition Rules: 4.5.1.2 In cases where the game is paused due to technical issues, not caused by player actions, the event staff may order a pause and require players to rejoin the ga...
- `COMP-RAG-EN-126` — Could you cite the AOV rule concerning disconnections and reconnects?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - Competition Rules: 4.5.1.2 In cases where the game is paused due to technical issues, not caused by player actions, the event staff may order a pause and require players to rejoin the ga...

### en / gold_or_section_contract_gap / fair_play_conduct (7 cases)

- `COMP-RAG-EN-033` — I am preparing for a Counter Strike 2 match. What is the policy for fair play and prohibited conduct?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Prohibited to bring mobile phones, tablets, or smartwatches into the competition area until the match ends: Mobile phones, tablets, or smartwatches are prohibited in the competition area unt...
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
  - Output: English draft translation of VALORANT competition rules: - Post-Match Procedure * Result recording * Officials will immediately verify and record match results. * Forfeiture * If a forfeit occurs, the result for that map will be recorded as 13-0. Match Paus...
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

### en / gold_or_section_contract_gap / pause_timeout (3 cases)

- `COMP-RAG-EN-062` — For Counter-Strike 2, can you verify the rule on pauses and timeouts?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Technical Game Pauses: Each team may pause the game twice, each pause not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.: Technical game pauses allowed pe...
- `COMP-RAG-EN-064` — Please retrieve the official CS2 rulebook evidence for pauses and timeouts.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Technical Game Pauses: Each team may pause the game twice, each pause not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.: Technical game pauses allowed pe...
- `COMP-RAG-EN-066` — Could you cite the Counter Strike 2 rule concerning pauses and timeouts?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Technical Game Pauses: Each team may pause the game twice, each pause not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.: Technical game pauses allowed pe...

### en / gold_or_section_contract_gap / penalty (8 cases)

- `COMP-RAG-EN-067` — What do the CS2 tournament rules say about penalties?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. - Behavior and Penalties - PSU Phuket CS2 2026 Tournament Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- `COMP-RAG-EN-068` — For Counter-Strike 2, can you verify the rule on penalties?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. - Behavior and Penalties Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- `COMP-RAG-EN-070` — Please retrieve the official CS2 rulebook evidence for penalties.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. - Language: The official language of competition is Thai. All communication, protests, and reporting must be in Thai, unless otherwise specified.: Language: The official la...
- `COMP-RAG-EN-071` — How is penalties handled in the Counter-Strike 2 tournament rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. - Behavior and Penalties - PSU Phuket CS2 2026 Tournament Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- `COMP-RAG-EN-072` — Could you cite the Counter Strike 2 rule concerning penalties?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. - Behavior and Penalties Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- `COMP-RAG-EN-242` — For Valorant, can you verify the rule on penalties?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of VALORANT competition rules: - Post-Match Procedure * Result recording * Officials will immediately verify and record match results. * Forfeiture * If a forfeit occurs, the result for that map will be recorded as 13-0. Match Paus...
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
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. - If any member withdraws, the team may be disqualified. - Competition time: The tournament schedule will be announced at least one day in advance. Participants must confir...
- `COMP-RAG-EN-074` — For Counter-Strike 2, can you verify the rule on the penalty matrix?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. - If any member withdraws, the team may be disqualified. - Competition time: The tournament schedule will be announced at least one day in advance. Participants must confir...
- `COMP-RAG-EN-075` — I am preparing for a Counter Strike 2 match. What is the policy for the penalty matrix?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. - Competition time: The tournament schedule will be announced at least one day in advance. Participants must confirm their attendance before each match begins. Late arrival...
- `COMP-RAG-EN-076` — Please retrieve the official CS2 rulebook evidence for the penalty matrix.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. - Language: The official language of competition is Thai. All communication, protests, and reporting must be in Thai, unless otherwise specified.: Language: The official la...
- `COMP-RAG-EN-077` — How is the penalty matrix handled in the Counter-Strike 2 tournament rules?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. - If any member withdraws, the team may be disqualified. - Competition time: The tournament schedule will be announced at least one day in advance. Participants must confir...
- `COMP-RAG-EN-078` — Could you cite the Counter Strike 2 rule concerning the penalty matrix?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Section Title: 8. - If any member withdraws, the team may be disqualified. - Competition time: The tournament schedule will be announced at least one day in advance. Participants must confir...

### en / gold_or_section_contract_gap / pre_match_on_site (4 cases)

- `COMP-RAG-EN-139` — What do the RoV tournament rules say about check-in and the competition area?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - Competition Rules: ... 4.5.5.1 If a player is in a life-threatening situation, such as being unsafe in the competition area or facing other circumstances that prevent continued gameplay....
- `COMP-RAG-EN-140` — For Arena of Valor, can you verify the rule on check-in and the competition area?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - Competition Rules: ... 4.5.5.1 If a player is in a life-threatening situation, such as being unsafe in the competition area or facing other circumstances that prevent continued gameplay....
- `COMP-RAG-EN-141` — I am preparing for a AOV match. What is the policy for check-in and the competition area?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - Competition Schedule 1.1. - Competition Rules: ... 4.5.5.1 If a player is in a life-threatening situation, such as being unsafe in the competition area or facing other circumstances that...
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

### en / gold_or_section_contract_gap / rulebook_identity (3 cases)

- `COMP-RAG-EN-099` — I am preparing for a Counter Strike 2 match. What is the policy for the rulebook scope and tournament identity?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Counter-Strike 2 competition rules: - Scope of Application This regulation applies to all players, teams, and staff members participating officially in any CS2 competition organized by PSU Esports Studio - Phuket. - Competition ...
- `COMP-RAG-EN-153` — I am preparing for a AOV match. What is the policy for the rulebook scope and tournament identity?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - Competition Schedule 1.1. - Competition Rules 4. Regulations and Competition Rules 4.1. Basic Rules 4.1.1. Prohibited to use character names or phrases that are offensive or disrespectfu...
- `COMP-RAG-EN-154` — Please retrieve the official RoV rulebook evidence for the rulebook scope and tournament identity.
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The answer is target-grounded, but its returned section is outside the current Gold allowed-evidence list.
  - Output: English draft translation of Arena of Valor (RoV) competition rules: - Offenses and Penalties: 6. Misconduct and Penalties 6.1. No competitor shall engage in any of the following acts: 6.1.1. No player shall use inappropriate language or display disrespectf...

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
  - Output: English draft translation of ROV competition rules: - Competition Rules 4. Regulations and Competition Rules 4.1. Basic Rules 4.1.1. Prohibited to use character names or phrases that are offensive or disrespectful toward others. 4.1.2. - Competition Rules: ...

### en / routing_or_target_failure / rulebook_identity (1 cases)

- `COMP-RAG-EN-152` — For Arena of Valor, can you verify the rule on the rulebook scope and tournament identity?
  - Expected: `answer_available`; actual: `answer` via `pipeline:structured_competition_rules_en`
  - Reason: The request did not retain the expected competition route or rulebook target.
  - Output: English draft translation of VALORANT competition rules: - Post-Match Procedure * Result recording * Officials will immediately verify and record match results. * Forfeiture * If a forfeit occurs, the result for that map will be recorded as 13-0. Match Paus...

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
