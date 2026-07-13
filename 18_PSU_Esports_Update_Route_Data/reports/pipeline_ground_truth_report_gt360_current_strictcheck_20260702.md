# Pipeline Ground Truth Evaluation

วันที่: 2026-07-02

## Summary

- Total: 360
- PASS: 357
- FAIL: 3
- ERROR: 0
- Pass rate: 99.17%
- Average latency: 0.0144s
- P95 latency: 0.0412s
- Keyword fail: 3
- Source fail: 0
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:deterministic_calculator_fast`: 139
- `pipeline:schedule_fast_path`: 46
- `pipeline:games_fast_path`: 25
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
- `pipeline:rag_direct_curated`: 2
- `pipeline:mixed_rules_fast`: 2
- `pipeline:calendar_schedule_fast_path`: 2

## Route Category Distribution

- `service_fee`: 144
- `schedule`: 48
- `reservation`: 47
- `games`: 27
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
| v2_282 | no_answer | `general` | ไม่พบข้อมูล | คำตอบ: พื้นที่การแข่งขันและกฎระเบียบ รายละเอียดที่เกี่ยวข้อง: - จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน - อุปกรณ์อิเล็กทรอนิกส์ ห้ามนำโทรศัพท์มือถือ, แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่... |
| v2_296 | no_answer | `games` | ไม่พบข้อมูล | Cockpit ใช้เล่นเกม Gran Turismo 7 (Single Player) ได้ โดยปรากฏในรายการบริการ Cockpit #1 (1 Person) 60 min ของระบบจอง แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| v2_357 | games | `schedule` | VALORANT | วันนี้ 02/07/2026 (วันพฤหัสบดี): วันพฤหัสบดีเปิดให้เล่น 09:00-12:00 และ 13:00-16:00 วันที่อ้างอิงของระบบ: วันนี้คือ 02/07/2026 (วันพฤหัสบดี) ตามเวลาไทย รายละเอียดจากตาราง: - วันจันทร์ช่วงเช้า 09:00-12:00 เป็น Maintenance... |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_gt360_current_strictcheck_20260702.jsonl`
