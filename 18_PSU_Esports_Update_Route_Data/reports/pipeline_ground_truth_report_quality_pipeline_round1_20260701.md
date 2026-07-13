# Pipeline Ground Truth Evaluation

วันที่: 2026-07-01

## Summary

- Total: 360
- PASS: 339
- FAIL: 21
- ERROR: 0
- Pass rate: 94.17%
- Average latency: 0.0002s
- P95 latency: 0.0003s
- Keyword fail: 18
- Source fail: 7
- Quality fail: 0
- Validation fail: 0

## Mode Distribution

- `pipeline:deterministic_calculator_fast`: 139
- `pipeline:schedule_fast_path`: 48
- `pipeline:games_fast_path`: 29
- `pipeline:guard_no_answer`: 21
- `pipeline:rules_fast_path`: 19
- `pipeline:booking_fast_path`: 18
- `pipeline:equipment_fast_path`: 14
- `pipeline:checkin_fast_path`: 11
- `pipeline:contact_fast_path`: 10
- `pipeline:payment_fast_path`: 9
- `pipeline:category_rule_fast_path`: 8
- `pipeline:no_answer`: 7
- `pipeline:penalty_fast_path`: 6
- `pipeline:overview_fast_path`: 5
- `pipeline:members_fast_path`: 5
- `pipeline:knowledge_fast_path`: 4
- `pipeline:mixed_reservation_fast`: 3
- `pipeline:news_fast_path`: 2
- `pipeline:rag_direct_curated`: 1
- `pipeline:mixed_rules_fast`: 1

## Route Category Distribution

- `service_fee`: 144
- `schedule`: 42
- `reservation`: 42
- `general`: 36
- `games`: 26
- `no_answer`: 21
- `equipment`: 14
- `rules`: 13
- `contact`: 8
- `overview`: 6
- `penalty`: 4
- `knowledge`: 4

## Failed Cases

| ID | Category | Route | Problem | Answer Short |
|---|---|---|---|---|
| v2_019 | reservation | `overview` | 09:00; 16:00; Monday; Friday; Maintenance | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด overview ตอนนี้ครับ |
| v2_040 | reservation | `equipment` | 13:00; 16:00; Maintenance; Weekly hardware inspection; cleaning | อุปกรณ์บนหน้า Home: - PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset - Cockpit Zone: TV 65" 2 Units, Logitech G... |
| v2_041 | reservation | `equipment` | 13:00; 16:00; Maintenance; Weekly hardware inspection; cleaning | อุปกรณ์บนหน้า Home: - PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset - Cockpit Zone: TV 65" 2 Units, Logitech G... |
| v2_181 | reservation | `schedule` | ยกเลิก; 1 ชั่วโมง; จองใหม่; สลิป | เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน รายละเอียดจากตาราง: - Morning คือ 09:00-12:00 - Afternoon คือ 13:00-16:00 - Monday ช่วง Morning 09:00-12:00 เป็น Maint... |
| v2_190 | reservation | `schedule` | 30 นาที | เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน รายละเอียดจากตาราง: - Morning คือ 09:00-12:00 - Afternoon คือ 13:00-16:00 - Monday ช่วง Morning 09:00-12:00 เป็น Maint... |
| v2_201 | games | `rules` | PlayStation 5; TEKKEN 8 | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด rules ตอนนี้ครับ |
| v2_241 | rules | `equipment` | ห้าม | อุปกรณ์บนหน้า Home: - PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset - Cockpit Zone: TV 65" 2 Units, Logitech G... |
| v2_247 | penalty | `service_fee` | ชดเชย; เต็มจำนวน | PC: ไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png |
| v2_266 | knowledge | `games` | MOBA; Knowledge | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ |
| v2_268 | knowledge | `games` | การทำงานเป็นทีม; สื่อสาร; Knowledge | Nintendo Switch มี Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกมอื่น ๆ แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| v2_269 | knowledge | `games` | ไหวพริบ; การตัดสินใจ; Knowledge | Nintendo Switch มี Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกมอื่น ๆ แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| v2_270 | events_news | `games` | News | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ |
| v2_271 | events_news | `games` | News | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| v2_274 | events_news | `schedule` | News | โดยทั่วไปเวลาสิ้นสุดช่วงบริการคือ 16:00 แต่วันศุกร์ช่วงบ่าย 13:00-16:00 เป็น Maintenance จึงควรดูวันประกอบ รายละเอียดจากตาราง: - Morning คือ 09:00-12:00 - Afternoon คือ 13:00-16:00 - Monday ช่วง Morning 09:00-12:00 เป็น... |
| v2_290 | no_answer | `games` | ไม่พบข้อมูล | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation |
| v2_303 | reservation | `schedule` | 1 ชั่วโมง | เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน รายละเอียดจากตาราง: - Morning คือ 09:00-12:00 - Afternoon คือ 13:00-16:00 - Monday ช่วง Morning 09:00-12:00 เป็น Maint... |
| v2_304 | service_fee | `reservation` | บาท; service_fee | ผู้ใช้งานต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง โดยสามารถเช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนถึงเวลาเริ่มต้นของรอบ แหล่งข้อมูล: https://esports.computing.psu.ac.th/ |
| v2_310 | rules | `equipment` | ไม่รับผิดชอบ; รับผิดชอบ | อุปกรณ์บนหน้า Home: - PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset - Cockpit Zone: TV 65" 2 Units, Logitech G... |
| v2_312 | rules | `games` | คืน; หลังจากใช้งานเสร็จ | ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ |
| v2_315 | service_fee | `service_fee` | PlayStation 5 | ราคา 0 บาท สำหรับกลุ่ม PSU Student and Staff แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png |
| v2_316 | service_fee | `service_fee` | VR | ราคา 190 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_quality_pipeline_round1_20260701.jsonl`
