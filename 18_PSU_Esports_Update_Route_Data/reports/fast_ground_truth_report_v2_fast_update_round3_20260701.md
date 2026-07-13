# Fast Ground Truth Evaluation - PSU Esports Update Runtime

วันที่: 2026-07-01

## Summary

- Total: 360
- PASS: 357
- FAIL: 3
- ERROR: 0
- Pass rate: 99.17%
- Average latency: 0.0001s
- P95 latency: 0.0001s
- Keyword fail: 3
- Source fail: 0

## Mode Distribution

- `deterministic_calculator_fast`: 139
- `schedule_fast_path`: 47
- `no_answer_fast`: 25
- `games_fast_path`: 23
- `rules_fast_path`: 21
- `booking_fast_path`: 20
- `equipment_fast_path`: 13
- `checkin_fast_path`: 12
- `penalty_fast_path`: 11
- `payment_fast_path`: 10
- `contact_fast_path`: 10
- `knowledge_fast_path`: 7
- `overview_fast_path`: 5
- `news_fast_path`: 5
- `members_fast_path`: 5
- `mixed_reservation_fast`: 4
- `mixed_rules_fast`: 2
- `rule_fast_path`: 1

## By Category

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| about_us | 5 | 5 | 100.00% |
| contact | 10 | 10 | 100.00% |
| equipment | 10 | 10 | 100.00% |
| events_news | 5 | 5 | 100.00% |
| knowledge | 7 | 7 | 100.00% |
| no_answer | 25 | 25 | 100.00% |
| overview | 5 | 5 | 100.00% |
| penalty | 11 | 11 | 100.00% |
| reservation | 94 | 94 | 100.00% |
| rules | 23 | 23 | 100.00% |
| service_fee | 139 | 139 | 100.00% |
| games | 23 | 26 | 88.46% |

## By Answer Type

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| calculation | 113 | 113 | 100.00% |
| multi_fact | 10 | 10 | 100.00% |
| no_answer | 33 | 33 | 100.00% |
| summary | 12 | 12 | 100.00% |
| fact | 171 | 173 | 98.84% |
| list | 18 | 19 | 94.74% |

## By Difficulty

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| hard | 89 | 89 | 100.00% |
| medium | 268 | 271 | 98.89% |

## By Mode

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| booking_fast_path | 20 | 20 | 100.00% |
| checkin_fast_path | 12 | 12 | 100.00% |
| contact_fast_path | 10 | 10 | 100.00% |
| deterministic_calculator_fast | 139 | 139 | 100.00% |
| games_fast_path | 23 | 23 | 100.00% |
| knowledge_fast_path | 7 | 7 | 100.00% |
| members_fast_path | 5 | 5 | 100.00% |
| mixed_reservation_fast | 4 | 4 | 100.00% |
| mixed_rules_fast | 2 | 2 | 100.00% |
| news_fast_path | 5 | 5 | 100.00% |
| no_answer_fast | 25 | 25 | 100.00% |
| overview_fast_path | 5 | 5 | 100.00% |
| payment_fast_path | 10 | 10 | 100.00% |
| penalty_fast_path | 11 | 11 | 100.00% |
| rule_fast_path | 1 | 1 | 100.00% |
| rules_fast_path | 21 | 21 | 100.00% |
| schedule_fast_path | 47 | 47 | 100.00% |
| equipment_fast_path | 10 | 13 | 76.92% |

## Failed Cases

| ID | Category | Mode | Problem | Answer Short |
|---|---|---|---|---|
| v2_214 | games | `equipment_fast_path` | missing keywords: Warzone | อุปกรณ์บนหน้า Home: - PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset - Cockpit Zone: TV 65" 2 Units, Logitech G... |
| v2_217 | games | `equipment_fast_path` | missing keywords: Horizon | อุปกรณ์บนหน้า Home: - PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset - Cockpit Zone: TV 65" 2 Units, Logitech G... |
| v2_219 | games | `equipment_fast_path` | missing keywords: Gran Turismo 7 | อุปกรณ์บนหน้า Home: - PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset - Cockpit Zone: TV 65" 2 Units, Logitech G... |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\fast_ground_truth_results_v2_fast_update_round3_20260701.jsonl`
