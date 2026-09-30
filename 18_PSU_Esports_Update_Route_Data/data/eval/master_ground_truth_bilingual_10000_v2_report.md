# PSU Esports Master Ground Truth Candidate v1

ชุดนี้ครอบคลุมความสามารถทั้งหมดของ Chatbot โดยแยก Static Answer, Live Lookup, Clarification และ Safe No-answer.
Generated paraphrase เป็น Gold candidate ที่ต้องผ่าน Pipeline evaluation และ Human Review ก่อนใช้เป็น Release Gate แบบ strict.

## Summary

- Total: 10,000
- Thai: 5,000
- English: 5,000

## Domain Distribution Per Locale

| Domain | Thai | English |
|---|---:|---:|
| `service_fee` | 400 | 400 |
| `reservation_policy` | 450 | 450 |
| `live_booking` | 400 | 400 |
| `schedule_calendar` | 350 | 350 |
| `games_catalog_availability` | 600 | 600 |
| `game_detail` | 450 | 450 |
| `game_controls` | 650 | 650 |
| `equipment` | 350 | 350 |
| `studio_rules_penalties` | 350 | 350 |
| `competition_rules` | 500 | 500 |
| `members_overview_contact` | 250 | 250 |
| `compound_context_boundary` | 250 | 250 |

## Answer Status

- `en/answer_available`: 3809
- `en/clarification_required`: 61
- `en/live_lookup_required`: 404
- `en/localization_pending`: 543
- `en/no_answer_expected`: 157
- `en/safe_clarification`: 9
- `en/safe_no_answer`: 17
- `th/answer_available`: 4234
- `th/clarification_required`: 80
- `th/live_lookup_required`: 458
- `th/no_answer_expected`: 228

## Review Status

- `en/generated_paraphrase_pending_review`: 2356
- `en/inherited_gold_candidate`: 1567
- `en/source_grounded_gold_candidate`: 1077
- `th/generated_paraphrase_pending_review`: 2640
- `th/inherited_gold_candidate`: 1283
- `th/source_grounded_gold_candidate`: 1077

## Safety Contract

- Live booking and date-aware questions never freeze a current availability result into Gold.
- Source-gap and unsupported questions test abstention, not a fabricated answer.
- English source contracts do not authorize runtime translation of facts.
- Every generated paraphrase remains pending review until independently checked.
