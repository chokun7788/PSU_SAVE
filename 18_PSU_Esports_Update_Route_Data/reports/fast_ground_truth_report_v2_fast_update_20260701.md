# Fast Ground Truth Evaluation - PSU Esports Update Runtime

วันที่: 2026-07-01

## Summary

- Total: 360
- PASS: 311
- FAIL: 49
- ERROR: 0
- Pass rate: 86.39%
- Average latency: 0.0001s
- P95 latency: 0.0002s
- Keyword fail: 49
- Source fail: 12

## Mode Distribution

- `deterministic_calculator_fast`: 153
- `schedule_fast_path`: 51
- `games_fast_path`: 36
- `no_answer_fast`: 26
- `rules_fast_path`: 19
- `equipment_fast_path`: 17
- `mixed_reservation_fast`: 15
- `contact_fast_path`: 10
- `rule_fast_path`: 8
- `penalty_fast_path`: 7
- `overview_fast_path`: 5
- `members_fast_path`: 5
- `knowledge_fast_path`: 4
- `news_fast_path`: 3
- `mixed_rules_fast`: 1

## By Category

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| about_us | 5 | 5 | 100.00% |
| contact | 10 | 10 | 100.00% |
| games | 26 | 26 | 100.00% |
| overview | 5 | 5 | 100.00% |
| service_fee | 137 | 139 | 98.56% |
| rules | 20 | 23 | 86.96% |
| no_answer | 21 | 25 | 84.00% |
| penalty | 9 | 11 | 81.82% |
| reservation | 66 | 94 | 70.21% |
| events_news | 3 | 5 | 60.00% |
| knowledge | 4 | 7 | 57.14% |
| equipment | 5 | 10 | 50.00% |

## By Answer Type

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| calculation | 113 | 113 | 100.00% |
| list | 19 | 19 | 100.00% |
| no_answer | 27 | 33 | 81.82% |
| fact | 137 | 173 | 79.19% |
| summary | 9 | 12 | 75.00% |
| multi_fact | 6 | 10 | 60.00% |

## By Difficulty

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| hard | 79 | 89 | 88.76% |
| medium | 232 | 271 | 85.61% |

## By Mode

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| contact_fast_path | 10 | 10 | 100.00% |
| knowledge_fast_path | 4 | 4 | 100.00% |
| members_fast_path | 5 | 5 | 100.00% |
| mixed_rules_fast | 1 | 1 | 100.00% |
| news_fast_path | 3 | 3 | 100.00% |
| overview_fast_path | 5 | 5 | 100.00% |
| rule_fast_path | 8 | 8 | 100.00% |
| rules_fast_path | 19 | 19 | 100.00% |
| schedule_fast_path | 47 | 51 | 92.16% |
| deterministic_calculator_fast | 140 | 153 | 91.50% |
| penalty_fast_path | 6 | 7 | 85.71% |
| no_answer_fast | 21 | 26 | 80.77% |
| mixed_reservation_fast | 11 | 15 | 73.33% |
| games_fast_path | 26 | 36 | 72.22% |
| equipment_fast_path | 5 | 17 | 29.41% |

## Failed Cases

| ID | Category | Mode | Problem | Answer Short |
|---|---|---|---|---|
| v2_154 | service_fee | `no_answer_fast` | missing keywords: PC, Service Fee; missing sources: service_fee | ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ |
| v2_156 | service_fee | `no_answer_fast` | missing keywords: PC, Service Fee; missing sources: service_fee | ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ |
| v2_164 | reservation | `equipment_fast_path` | missing keywords: 1 ชั่วโมง | อุปกรณ์บนหน้า Home: - PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset - Cockpit Zone: TV 65" 2 Units, Logitech G... |
| v2_165 | reservation | `equipment_fast_path` | missing keywords: 1 ชั่วโมง | อุปกรณ์บนหน้า Home: - PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset - Cockpit Zone: TV 65" 2 Units, Logitech G... |
| v2_167 | reservation | `equipment_fast_path` | missing keywords: 1 ชั่วโมง | อุปกรณ์บนหน้า Home: - PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset - Cockpit Zone: TV 65" 2 Units, Logitech G... |
| v2_168 | reservation | `equipment_fast_path` | missing keywords: 1 ชั่วโมง | อุปกรณ์บนหน้า Home: - PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset - Cockpit Zone: TV 65" 2 Units, Logitech G... |
| v2_169 | reservation | `equipment_fast_path` | missing keywords: 3 Sessions | อุปกรณ์บนหน้า Home: - PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset - Cockpit Zone: TV 65" 2 Units, Logitech G... |
| v2_170 | reservation | `equipment_fast_path` | missing keywords: 3 Sessions | อุปกรณ์บนหน้า Home: - PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset - Cockpit Zone: TV 65" 2 Units, Logitech G... |
| v2_171 | reservation | `no_answer_fast` | missing keywords: 3 Sessions | ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ |
| v2_172 | reservation | `equipment_fast_path` | missing keywords: 3 Sessions | อุปกรณ์บนหน้า Home: - PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset - Cockpit Zone: TV 65" 2 Units, Logitech G... |
| v2_173 | reservation | `equipment_fast_path` | missing keywords: 3 Sessions | อุปกรณ์บนหน้า Home: - PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset - Cockpit Zone: TV 65" 2 Units, Logitech G... |
| v2_174 | reservation | `deterministic_calculator_fast` | missing keywords: 10 นาที, ยกเลิก, จองใหม่ | ตาราง Service Fee 2026: - PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท - Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and... |
| v2_175 | reservation | `deterministic_calculator_fast` | missing keywords: 10 นาที, ยกเลิก, จองใหม่ | ตาราง Service Fee 2026: - PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท - Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and... |
| v2_177 | reservation | `deterministic_calculator_fast` | missing keywords: 10 นาที, ยกเลิก, จองใหม่ | ตาราง Service Fee 2026: - PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท - Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and... |
| v2_180 | reservation | `mixed_reservation_fast` | missing keywords: ยกเลิก, 1 ชั่วโมง, จองใหม่ | ตอนจองต้องกรอก Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล เบอร์โทรศัพท์ และชำระโดยโอนเงินพร้อมแนบสลิป |
| v2_181 | reservation | `schedule_fast_path` | missing keywords: ยกเลิก, 1 ชั่วโมง, จองใหม่, สลิป | ตารางบริการที่มีในข้อมูล: - Morning คือ 09:00-12:00 - Afternoon คือ 13:00-16:00 - Monday ช่วง Morning 09:00-12:00 เป็น Maintenance* และช่วง Afternoon 13:00-16:00 เป็น Open for Service - Friday มี Maintenance ช่วง 13:00-1... |
| v2_182 | reservation | `equipment_fast_path` | missing keywords: ยกเลิก, 1 ชั่วโมง, จองใหม่, สลิป | อุปกรณ์บนหน้า Home: - PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset - Cockpit Zone: TV 65" 2 Units, Logitech G... |
| v2_183 | reservation | `mixed_reservation_fast` | missing keywords: ยกเลิก, 1 ชั่วโมง, จองใหม่ | ตอนจองต้องกรอก Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล เบอร์โทรศัพท์ และชำระโดยโอนเงินพร้อมแนบสลิป |
| v2_184 | reservation | `equipment_fast_path` | missing keywords: ไม่สามารถโอนสิทธิ์ | อุปกรณ์บนหน้า Home: - PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset - Cockpit Zone: TV 65" 2 Units, Logitech G... |
| v2_187 | reservation | `equipment_fast_path` | missing keywords: ไม่สามารถโอนสิทธิ์ | อุปกรณ์บนหน้า Home: - PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset - Cockpit Zone: TV 65" 2 Units, Logitech G... |
| v2_189 | reservation | `no_answer_fast` | missing keywords: 30 นาที | ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ |
| v2_190 | reservation | `schedule_fast_path` | missing keywords: 30 นาที | ตารางบริการที่มีในข้อมูล: - Morning คือ 09:00-12:00 - Afternoon คือ 13:00-16:00 - Monday ช่วง Morning 09:00-12:00 เป็น Maintenance* และช่วง Afternoon 13:00-16:00 เป็น Open for Service - Friday มี Maintenance ช่วง 13:00-1... |
| v2_193 | reservation | `mixed_reservation_fast` | missing keywords: บัตรประชาชน | สรุป: ต้องจองล่วงหน้าอย่างน้อย 1 ชั่วโมง, เช็คอินได้ล่วงหน้าสูงสุด 30 นาที และหากต้องยกเลิกหรือแก้ไขต้องแจ้งล่วงหน้าอย่างน้อย 1 ชั่วโมง |
| v2_194 | reservation | `mixed_reservation_fast` | missing keywords: บัตรประชาชน | สรุป: ต้องจองล่วงหน้าอย่างน้อย 1 ชั่วโมง, เช็คอินได้ล่วงหน้าสูงสุด 30 นาที และหากต้องยกเลิกหรือแก้ไขต้องแจ้งล่วงหน้าอย่างน้อย 1 ชั่วโมง |
| v2_195 | reservation | `no_answer_fast` | missing keywords: ธนาคารไทยพาณิชย์, 795-276244-1 | ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ |
| v2_197 | reservation | `deterministic_calculator_fast` | missing keywords: ธนาคารไทยพาณิชย์, 795-276244-1 | ตาราง Service Fee 2026: - PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท - Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and... |
| v2_198 | reservation | `equipment_fast_path` | missing keywords: ธนาคารไทยพาณิชย์, 795-276244-1 | อุปกรณ์บนหน้า Home: - PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset - Cockpit Zone: TV 65" 2 Units, Logitech G... |
| v2_225 | equipment | `games_fast_path` | missing keywords: Units; missing sources: home | Cockpit ใช้เล่นเกม Gran Turismo 7 |
| v2_226 | equipment | `games_fast_path` | missing keywords: Units; missing sources: home | Cockpit ใช้เล่นเกม Gran Turismo 7 |
| v2_227 | equipment | `games_fast_path` | missing keywords: Units; missing sources: home | Nintendo Switch มี Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกมอื่น ๆ |
| v2_228 | equipment | `games_fast_path` | missing keywords: Units; missing sources: home | PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 |
| v2_229 | equipment | `games_fast_path` | missing keywords: Units; missing sources: home | VR มีเกม Beat Saber และ Horizon Call of the Mountain |
| v2_233 | rules | `deterministic_calculator_fast` | missing keywords: งด, เสียงดัง | ตาราง Service Fee 2026: - PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท - Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and... |
| v2_234 | rules | `deterministic_calculator_fast` | missing keywords: ห้าม, เสียดสี | ตาราง Service Fee 2026: - PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท - Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and... |
| v2_242 | penalty | `deterministic_calculator_fast` | missing keywords: รับผิดชอบ, ค่าปรับ | ตาราง Service Fee 2026: - PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท - Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and... |
| v2_247 | penalty | `deterministic_calculator_fast` | missing keywords: ชดเชย, เต็มจำนวน | PC: ไม่พบราคาค่าบริการ PC ที่ยืนยันได้ใน Service Fee 2026 จึงยังไม่ควรคำนวณยอด PC แบบฟันธง แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png |
| v2_265 | knowledge | `penalty_fast_path` | missing keywords: Spacewar, 1972; missing sources: Knowledge | หากละเมิดกฎอาจถูกระงับสิทธิ์ชั่วคราว 1-7 วันหรือถาวร มีการบันทึกประวัติ และสามารถอุทธรณ์ได้ภายใน 7 วัน |
| v2_268 | knowledge | `games_fast_path` | missing keywords: การทำงานเป็นทีม, สื่อสาร; missing sources: Knowledge | Nintendo Switch มี Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกมอื่น ๆ |
| v2_269 | knowledge | `games_fast_path` | missing keywords: ไหวพริบ, การตัดสินใจ; missing sources: Knowledge | Nintendo Switch มี Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกมอื่น ๆ |
| v2_271 | events_news | `games_fast_path` | missing keywords: PSU; missing sources: News | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends |
| v2_274 | events_news | `schedule_fast_path` | missing keywords: PSU; missing sources: News | ตารางบริการที่มีในข้อมูล: - Morning คือ 09:00-12:00 - Afternoon คือ 13:00-16:00 - Monday ช่วง Morning 09:00-12:00 เป็น Maintenance* และช่วง Afternoon 13:00-16:00 เป็น Open for Service - Friday มี Maintenance ช่วง 13:00-1... |
| v2_283 | no_answer | `deterministic_calculator_fast` | missing keywords: ไม่พบข้อมูล | ตาราง Service Fee 2026: - PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท - Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and... |
| v2_287 | no_answer | `games_fast_path` | missing keywords: ไม่พบข้อมูล | PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 |
| v2_290 | no_answer | `games_fast_path` | missing keywords: ไม่พบข้อมูล | PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends |
| v2_291 | no_answer | `deterministic_calculator_fast` | missing keywords: ไม่พบข้อมูล | ตาราง Service Fee 2026: - PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท - Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and... |
| v2_299 | reservation | `deterministic_calculator_fast` | missing keywords: 10 นาที, ยกเลิก, ไม่มีการคืนเงิน | ตาราง Service Fee 2026: - PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท - Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and... |
| v2_301 | reservation | `deterministic_calculator_fast` | missing keywords: 3 Sessions, 10 นาที | ตาราง Service Fee 2026: - PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท - Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and... |
| v2_303 | reservation | `schedule_fast_path` | missing keywords: 1 ชั่วโมง | ตารางบริการที่มีในข้อมูล: - Morning คือ 09:00-12:00 - Afternoon คือ 13:00-16:00 - Monday ช่วง Morning 09:00-12:00 เป็น Maintenance* และช่วง Afternoon 13:00-16:00 เป็น Open for Service - Friday มี Maintenance ช่วง 13:00-1... |
| v2_309 | rules | `deterministic_calculator_fast` | missing keywords: เฉพาะ, เสียงดัง | ตาราง Service Fee 2026: - PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท - Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง): PSU Student and... |

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\fast_ground_truth_results_v2_fast_update_20260701.jsonl`
