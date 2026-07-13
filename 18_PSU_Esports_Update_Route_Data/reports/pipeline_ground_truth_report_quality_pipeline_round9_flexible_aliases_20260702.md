# Pipeline Ground Truth Evaluation

วันที่: 2026-07-02

## Summary

- Total: 360
- PASS: 357
- FAIL: 3
- ERROR: 0
- Pass rate: 99.17%
- Average latency: 0.0148s
- P95 latency: 0.0415s
- Keyword fail: 0
- Source fail: 0
- Quality fail: 3
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
| v2_150 | service_fee | `service_fee` | quality forbidden: ยังไม่ทราบกลุ่มผู้ใช้ | ยังไม่ทราบกลุ่มผู้ใช้ PC: ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง ข้อมูลราคาที่พบในภาพมี PlayStation 5, Nintendo Switch, Cockpit และ VR แหล่งข้อมูล: https://esports.compu... |
| v2_153 | service_fee | `service_fee` | quality forbidden: ยังไม่ทราบกลุ่มผู้ใช้ | ยังไม่ทราบกลุ่มผู้ใช้ PC: ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง ข้อมูลราคาที่พบในภาพมี PlayStation 5, Nintendo Switch, Cockpit และ VR แหล่งข้อมูล: https://esports.compu... |
| v2_155 | service_fee | `service_fee` | quality forbidden: ยังไม่ทราบกลุ่มผู้ใช้ | ยังไม่ทราบกลุ่มผู้ใช้ PC: ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง ข้อมูลราคาที่พบในภาพมี PlayStation 5, Nintendo Switch, Cockpit และ VR แหล่งข้อมูล: https://esports.compu... |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_quality_pipeline_round9_flexible_aliases_20260702.jsonl`
