# Pipeline Ground Truth Evaluation

วันที่: 2026-07-04

## Summary

- Total: 360
- PASS: 357
- FAIL: 3
- ERROR: 0
- Pass rate: 99.17%
- Average latency: 0.0117s
- P95 latency: 0.0332s
- Keyword fail: 2
- Source fail: 2
- Quality fail: 1
- Validation fail: 0

## Mode Distribution

- `pipeline:deterministic_calculator_fast`: 138
- `pipeline:schedule_fast_path`: 46
- `pipeline:guard_no_answer`: 25
- `pipeline:rules_fast_path`: 21
- `pipeline:booking_fast_path`: 20
- `pipeline:games_availability_fast_path`: 19
- `pipeline:checkin_fast_path`: 12
- `pipeline:penalty_fast_path`: 11
- `pipeline:payment_fast_path`: 10
- `pipeline:contact_fast_path`: 10
- `pipeline:knowledge_fast_path`: 7
- `pipeline:equipment_game_catalog_fast_path`: 6
- `pipeline:equipment_zone_fast_path`: 5
- `pipeline:overview_fast_path`: 5
- `pipeline:news_fast_path`: 5
- `pipeline:members_fast_path`: 5
- `pipeline:mixed_reservation_fast`: 4
- `pipeline:equipment_item_fast_path`: 3
- `pipeline:mixed_rules_fast`: 2
- `pipeline:calendar_schedule_fast_path`: 2
- `pipeline:rag_direct_curated`: 1
- `pipeline:category_rule_fast_path`: 1
- `pipeline:games_fast_path`: 1
- `pipeline:equipment_fast_path`: 1

## Route Category Distribution

- `service_fee`: 138
- `schedule`: 48
- `reservation`: 47
- `no_answer`: 25
- `games`: 22
- `rules`: 22
- `equipment`: 14
- `penalty`: 11
- `contact`: 10
- `knowledge`: 9
- `overview`: 9
- `events_news`: 5

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| v2_153 | service_fee | `games` | ไม่พบ; Service Fee; service_fee; service_fee direct answer missing: ไม่พบ, Service Fee | Counter-Strike 2: Counter-Strike 2 คือเกมยิงแข่งขันแบบทีมที่แบ่งเป็นฝ่ายบุกและฝ่ายรับ โดยมีเป้าหมายหลักเกี่ยวกับการวาง/กู้ระเบิดหรือจัดการฝ่ายตรงข้าม ??????: เกมยิง Tactical FPS ???????????????: เล่นเป็นรอบ ๆ ต้องซื้ออาว... |
| v2_220 | equipment | `equipment` | home | สรุปเกมที่เล่นได้ในโซนที่ถาม: - PC Zone: VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, TEKKEN 8 และ League of Legends อุปกรณ์หลัก: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 เครื่อง (10 Units),... |
| v2_229 | equipment | `equipment` | Units | Sony PlayStation VR2: ชุดแว่น VR สำหรับเล่นเกมเสมือนจริงใน VR Zone ใช้ทำอะไร/เล่นอะไรได้: เล่น Beat Saber และ Horizon Call of the Mountain วิธีใช้งานโดยสรุป: จอง VR Zone แล้วสวมแว่น PlayStation VR2 และใช้คอนโทรลเลอร์ตามค... |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_gt360_equipment_game_catalog_fix2_20260704.jsonl`
