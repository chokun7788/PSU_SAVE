# Pipeline Ground Truth Evaluation

วันที่: 2026-07-04

## Summary

- Total: 360
- PASS: 356
- FAIL: 4
- ERROR: 0
- Pass rate: 98.89%
- Average latency: 0.0118s
- P95 latency: 0.0332s
- Keyword fail: 1
- Source fail: 4
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:deterministic_calculator_fast`: 139
- `pipeline:schedule_fast_path`: 46
- `pipeline:guard_no_answer`: 25
- `pipeline:games_fast_path`: 21
- `pipeline:rules_fast_path`: 21
- `pipeline:booking_fast_path`: 20
- `pipeline:checkin_fast_path`: 12
- `pipeline:penalty_fast_path`: 11
- `pipeline:payment_fast_path`: 10
- `pipeline:equipment_fast_path`: 10
- `pipeline:contact_fast_path`: 10
- `pipeline:knowledge_fast_path`: 7
- `pipeline:overview_fast_path`: 5
- `pipeline:news_fast_path`: 5
- `pipeline:members_fast_path`: 5
- `pipeline:mixed_reservation_fast`: 4
- `pipeline:competition_fact_card`: 2
- `pipeline:mixed_rules_fast`: 2
- `pipeline:rag_direct_curated`: 2
- `pipeline:calendar_schedule_fast_path`: 2
- `pipeline:category_rule_fast_path`: 1

## Route Category Distribution

- `service_fee`: 139
- `schedule`: 48
- `reservation`: 47
- `no_answer`: 25
- `games`: 22
- `rules`: 22
- `penalty`: 11
- `contact`: 10
- `equipment`: 9
- `knowledge`: 9
- `overview`: 9
- `events_news`: 5
- `competition_rules`: 4

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| v2_201 | games | `competition_rules` | Reservation | คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที หลักฐานจากกติกา: - เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วิน... |
| v2_211 | games | `competition_rules` | PC; Reservation | คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10... |
| v2_333 | games | `competition_rules` | Reservation | คำตอบ: * รวมเวลาทั้งหมดไม่เกิน 10 นาที ต่อหนึ่งแมตช์ หากเกินเวลาผู้เล่นรายนั้นอาจหมดสิทธิ์แข่งต่อและต้องใช้ตัวสำรองแทน รายละเอียดที่เกี่ยวข้อง: - บั๊กคือข้อผิดพลาดในเกมที่ทำให้เกิดผลลัพธ์ที่ไม่ตั้งใจ โดยแบ่งประเภทเพื่อกำ... |
| v2_341 | games | `competition_rules` | Reservation | คำตอบ: * อุปกรณ์ที่นำมาเองได้ คีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) รายละเอียดที่เกี่ยวข้อง: - กฎระเบียบและรูปแบบการแข่งขัน VA... |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_notebook_manual_test.jsonl`
