# Pipeline Ground Truth Evaluation

วันที่: 2026-07-02

## Summary

- Total: 360
- PASS: 358
- FAIL: 2
- ERROR: 0
- Pass rate: 99.44%
- Average latency: 0.0153s
- P95 latency: 0.0395s
- Keyword fail: 0
- Source fail: 0
- Quality fail: 2
- Validation fail: 0

## Mode Distribution

- `pipeline:deterministic_calculator_fast`: 139
- `pipeline:schedule_fast_path`: 47
- `pipeline:games_fast_path`: 26
- `pipeline:guard_no_answer`: 22
- `pipeline:rules_fast_path`: 21
- `pipeline:booking_fast_path`: 20
- `pipeline:checkin_fast_path`: 12
- `pipeline:equipment_fast_path`: 10
- `pipeline:contact_fast_path`: 10
- `pipeline:payment_fast_path`: 9
- `pipeline:penalty_fast_path`: 9
- `pipeline:knowledge_fast_path`: 7
- `pipeline:category_rule_fast_path`: 6
- `pipeline:overview_fast_path`: 5
- `pipeline:news_fast_path`: 5
- `pipeline:members_fast_path`: 5
- `pipeline:mixed_reservation_fast`: 3
- `pipeline:no_answer`: 2
- `pipeline:mixed_rules_fast`: 2

## Route Category Distribution

- `service_fee`: 144
- `schedule`: 47
- `reservation`: 47
- `games`: 28
- `rules`: 22
- `no_answer`: 22
- `equipment`: 9
- `penalty`: 9
- `knowledge`: 9
- `overview`: 9
- `contact`: 8
- `events_news`: 5
- `general`: 1

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| v2_136 | service_fee | `service_fee` | service_fee direct answer missing: 0, 0 | ราคา 375 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน - VR 1 ชั่วโมง ราคา 375 บาท กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น ราย... |
| v2_137 | service_fee | `service_fee` | service_fee direct answer missing: 0, 0 | ราคา 375 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน - VR 1 ชั่วโมง ราคา 375 บาท กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน / มหาลัยอื่น ราย... |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_quality_pipeline_round12_psu_vs_external_policy_20260702.jsonl`
