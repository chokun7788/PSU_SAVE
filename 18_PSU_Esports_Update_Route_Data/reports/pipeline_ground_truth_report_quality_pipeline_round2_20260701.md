# Pipeline Ground Truth Evaluation

วันที่: 2026-07-01

## Summary

- Total: 360
- PASS: 317
- FAIL: 43
- ERROR: 0
- Pass rate: 88.06%
- Average latency: 0.0003s
- P95 latency: 0.0006s
- Keyword fail: 43
- Source fail: 43
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:deterministic_calculator_fast`: 96
- `pipeline:schedule_fast_path`: 47
- `pipeline:no_answer`: 39
- `pipeline:games_fast_path`: 26
- `pipeline:guard_no_answer`: 22
- `pipeline:rules_fast_path`: 21
- `pipeline:booking_fast_path`: 20
- `pipeline:checkin_fast_path`: 12
- `pipeline:payment_fast_path`: 10
- `pipeline:equipment_fast_path`: 10
- `pipeline:contact_fast_path`: 10
- `pipeline:penalty_fast_path`: 9
- `pipeline:knowledge_fast_path`: 7
- `pipeline:rag_direct_curated`: 6
- `pipeline:overview_fast_path`: 5
- `pipeline:news_fast_path`: 5
- `pipeline:members_fast_path`: 5
- `pipeline:category_rule_fast_path`: 4
- `pipeline:mixed_reservation_fast`: 4
- `pipeline:mixed_rules_fast`: 2

## Route Category Distribution

- `service_fee`: 97
- `reservation`: 89
- `schedule`: 45
- `general`: 28
- `no_answer`: 22
- `games`: 21
- `rules`: 19
- `equipment`: 9
- `contact`: 8
- `penalty`: 7
- `knowledge`: 7
- `overview`: 5
- `events_news`: 3

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| v2_042 | service_fee | `reservation` | PlayStation 5; 60; 0; 0; บาท; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_048 | service_fee | `reservation` | PlayStation 5; 60; 50; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_050 | service_fee | `reservation` | PlayStation 5; 60; 50; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_052 | service_fee | `reservation` | PlayStation 5; 60; 50; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_054 | service_fee | `reservation` | PlayStation 5; 60; 150; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_057 | service_fee | `reservation` | PlayStation 5; 60; 150; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_058 | service_fee | `reservation` | PlayStation 5; 60; 150; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_060 | service_fee | `reservation` | Nintendo Switch; 1-2; 0; 0; บาท; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_066 | service_fee | `reservation` | Nintendo Switch; 1-2; 50; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_068 | service_fee | `reservation` | Nintendo Switch; 1-2; 50; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_070 | service_fee | `reservation` | Nintendo Switch; 1-2; 50; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_072 | service_fee | `reservation` | Nintendo Switch; 1-2; 140; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_075 | service_fee | `reservation` | Nintendo Switch; 1-2; 140; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_076 | service_fee | `reservation` | Nintendo Switch; 1-2; 140; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_078 | service_fee | `reservation` | Nintendo Switch; 3-4; 0; 0; บาท; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_084 | service_fee | `reservation` | Nintendo Switch; 3-4; 100; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_086 | service_fee | `reservation` | Nintendo Switch; 3-4; 100; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_088 | service_fee | `reservation` | Nintendo Switch; 3-4; 100; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_090 | service_fee | `reservation` | Nintendo Switch; 3-4; 280; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_093 | service_fee | `reservation` | Nintendo Switch; 3-4; 280; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_094 | service_fee | `reservation` | Nintendo Switch; 3-4; 280; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_096 | service_fee | `reservation` | Cockpit; 60; 0; 0; บาท; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_102 | service_fee | `reservation` | Cockpit; 60; 65; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_104 | service_fee | `reservation` | Cockpit; 60; 65; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_106 | service_fee | `reservation` | Cockpit; 60; 65; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_108 | service_fee | `reservation` | Cockpit; 60; 200; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_111 | service_fee | `reservation` | Cockpit; 60; 200; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_112 | service_fee | `reservation` | Cockpit; 60; 200; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_114 | service_fee | `reservation` | VR; บาท; service_fee | ผู้ใช้งานต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง โดยสามารถเช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนถึงเวลาเริ่มต้นของรอบ แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| v2_120 | service_fee | `reservation` | VR; 190; service_fee | ผู้ใช้งานต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง โดยสามารถเช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนถึงเวลาเริ่มต้นของรอบ แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| v2_122 | service_fee | `reservation` | VR; 190; service_fee | ผู้ใช้งานต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง โดยสามารถเช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนถึงเวลาเริ่มต้นของรอบ แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| v2_124 | service_fee | `reservation` | VR; 190; service_fee | ผู้ใช้งานต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง โดยสามารถเช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนถึงเวลาเริ่มต้นของรอบ แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| v2_126 | service_fee | `reservation` | VR; 525; service_fee | ผู้ใช้งานต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง โดยสามารถเช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนถึงเวลาเริ่มต้นของรอบ แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| v2_129 | service_fee | `reservation` | VR; 30; 525; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_130 | service_fee | `reservation` | VR; 525; service_fee | ผู้ใช้งานต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง โดยสามารถเช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนถึงเวลาเริ่มต้นของรอบ แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| v2_132 | service_fee | `reservation` | VR; 1 ชั่วโมง; 0; 0; บาท; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_138 | service_fee | `reservation` | VR; 1 ชั่วโมง; 375; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_140 | service_fee | `reservation` | VR; 1 ชั่วโมง; 375; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_142 | service_fee | `reservation` | VR; 1 ชั่วโมง; 375; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_144 | service_fee | `reservation` | VR; 1 ชั่วโมง; 1050; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_147 | service_fee | `reservation` | VR; 1 ชั่วโมง; 1050; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_148 | service_fee | `reservation` | VR; 1 ชั่วโมง; 1050; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |
| v2_155 | service_fee | `reservation` | PC; Service Fee; service_fee | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_quality_pipeline_round2_20260701.jsonl`
