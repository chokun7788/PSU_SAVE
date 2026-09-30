# Intent-trap bilingual evaluation

Corpus: `data\eval\intent_trap_bilingual_1000_v2.jsonl`  
Results: `reports\master_ground_truth_eval\master_gt_eval_20260924_150915.json`  
Status: scenario-curated paraphrases pending human review; a passing automated check is not proof of factual correctness.

| Locale | Theme | Passed | Total | Route fails | Status fails | Content fails | >10s | >20s |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| en | booking_days_hours | 50 | 50 | 0 | 0 | 0 | 0 | 0 |
| en | damage_responsibility | 50 | 50 | 0 | 0 | 0 | 0 | 0 |
| en | equipment_access_trap | 47 | 50 | 3 | 0 | 0 | 0 | 0 |
| en | fee_without_service | 50 | 50 | 0 | 0 | 0 | 0 | 0 |
| en | food_bring_scope | 49 | 50 | 1 | 0 | 0 | 0 | 0 |
| en | food_consumption | 45 | 50 | 5 | 4 | 5 | 0 | 0 |
| en | identity_typo | 50 | 50 | 0 | 0 | 0 | 0 | 0 |
| en | outsider_eligibility | 44 | 50 | 6 | 0 | 0 | 0 | 0 |
| en | unclear_or_outside_scope | 45 | 50 | 5 | 0 | 0 | 0 | 0 |
| en | weekday_live_slots | 0 | 50 | 0 | 0 | 50 | 0 | 0 |
| th | booking_days_hours | 50 | 50 | 0 | 0 | 0 | 0 | 0 |
| th | damage_responsibility | 44 | 50 | 6 | 6 | 6 | 1 | 0 |
| th | equipment_access_trap | 50 | 50 | 0 | 0 | 0 | 0 | 0 |
| th | fee_without_service | 50 | 50 | 0 | 0 | 0 | 0 | 0 |
| th | food_bring_scope | 50 | 50 | 0 | 0 | 0 | 0 | 0 |
| th | food_consumption | 50 | 50 | 0 | 0 | 0 | 0 | 0 |
| th | identity_typo | 50 | 50 | 0 | 0 | 0 | 0 | 0 |
| th | outsider_eligibility | 50 | 50 | 0 | 0 | 0 | 2 | 0 |
| th | unclear_or_outside_scope | 39 | 50 | 11 | 0 | 5 | 7 | 0 |
| th | weekday_live_slots | 0 | 50 | 0 | 0 | 50 | 0 | 0 |

## Representative failures

### en / equipment_access_trap

- `INTENT-TRAP-EN-0422` (0.10s, `pipeline:rule_en`): A question about the studio: Can a non-student access the Cockpit?
  - Failures: route expected ['clarification', 'no_answer', 'reservation', 'rules'], got overview
  - Answer excerpt: PSU Esports Studio - Phuket is an esports learning development studio for excellence and economic advancement in Southern Thailand, Phuket branch, under Prince of Songkla University and operated by the College of Computing. Source: https://esports.phuket.psu.a
- `INTENT-TRAP-EN-0432` (0.13s, `pipeline:rule_en`): A question about the studio: Are the PCs for public visitors or students only?
  - Failures: route expected ['clarification', 'no_answer', 'reservation', 'rules'], got overview
  - Answer excerpt: PSU Esports Studio - Phuket is an esports learning development studio for excellence and economic advancement in Southern Thailand, Phuket branch, under Prince of Songkla University and operated by the College of Computing. Source: https://esports.phuket.psu.a
- `INTENT-TRAP-EN-0447` (0.06s, `pipeline:rule_en`): A question about the studio: Who is eligible to use the studio stations?
  - Failures: route expected ['clarification', 'no_answer', 'reservation', 'rules'], got overview
  - Answer excerpt: PSU Esports Studio - Phuket is an esports learning development studio for excellence and economic advancement in Southern Thailand, Phuket branch, under Prince of Songkla University and operated by the College of Computing. Source: https://esports.phuket.psu.a

### en / food_bring_scope

- `INTENT-TRAP-EN-0247` (0.07s, `pipeline:rule_en`): A question about the studio: Can I bring my own beverage onto the premises?
  - Failures: route expected ['clarification', 'no_answer', 'rules'], got overview
  - Answer excerpt: PSU Esports Studio - Phuket is an esports learning development studio for excellence and economic advancement in Southern Thailand, Phuket branch, under Prince of Songkla University and operated by the College of Computing. Source: https://esports.phuket.psu.a

### en / food_consumption

- `INTENT-TRAP-EN-0296` (0.06s, `pipeline:english_no_answer`): Is eating restricted to designated spaces?
  - Failures: none of required alternatives found: ['พื้นที่ที่กำหนด', 'designated area']; route expected ['rules'], got no_answer; status expected answer_available, got no_answer
  - Answer excerpt: I could not find verified PSU Esports Studio - Phuket information for this question.

### en / outsider_eligibility

- `INTENT-TRAP-EN-0107` (0.14s, `pipeline:rule_en`): A question about the studio: Can someone who is not a PSU student play there?
  - Failures: route expected ['clarification', 'no_answer', 'reservation', 'rules', 'service_fee'], got overview
  - Answer excerpt: PSU Esports Studio - Phuket is an esports learning development studio for excellence and economic advancement in Southern Thailand, Phuket branch, under Prince of Songkla University and operated by the College of Computing. Source: https://esports.phuket.psu.a
- `INTENT-TRAP-EN-0116` (0.07s, `pipeline:structured_members_source_th`): Does a public visitor need membership before entering?
  - Failures: route expected ['clarification', 'no_answer', 'reservation', 'rules', 'service_fee'], got overview
  - Answer excerpt: Official Thai source member record(s): Names and role titles below are shown exactly as published by PSU. - ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี - มหาวิทยาลัยสงขลานครินทร์ - รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี - มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต - รศ.ดร.อซ
- `INTENT-TRAP-EN-0137` (0.08s, `pipeline:rule_en`): A question about the studio: Can an alumnus without a student card use the studio?
  - Failures: route expected ['clarification', 'no_answer', 'reservation', 'rules', 'service_fee'], got overview
  - Answer excerpt: PSU Esports Studio - Phuket is an esports learning development studio for excellence and economic advancement in Southern Thailand, Phuket branch, under Prince of Songkla University and operated by the College of Computing. Source: https://esports.phuket.psu.a

### en / unclear_or_outside_scope

- `INTENT-TRAP-EN-0496` (0.06s, `pipeline:structured_games_catalog_en`): umm games or something idk
  - Failures: route expected ['clarification', 'general', 'knowledge', 'no_answer', 'overview'], got games
  - Answer excerpt: There are currently 42 verified games available. PC Zone (6 games) • Call of Duty: Warzone • Counter-Strike 2 • League of Legends • PUBG: BATTLEGROUNDS • TEKKEN 8 • VALORANT PlayStation 5 Zone (17 games) • Call of Duty: Modern Warfare III • Delta Force • EA Sp

### en / weekday_live_slots

- `INTENT-TRAP-EN-0301` (2.11s, `pipeline:live_booking_status_unavailable`): Which PC stations are free on Monday at 1 pm?
  - Failures: missing required text: ['2026-09-28']
  - Answer excerpt: I cannot confirm the live opening or booking status right now because the Booking Dashboard is unavailable. I will not present a saved schedule as live availability. Please check the reservation page or try again shortly. Source: https://esports.computing.psu.
- `INTENT-TRAP-EN-0306` (2.10s, `pipeline:live_booking_status_unavailable`): Is PC 2 free on Tuesday at 2 pm?
  - Failures: missing required text: ['2026-09-29']
  - Answer excerpt: I cannot confirm the live opening or booking status right now because the Booking Dashboard is unavailable. I will not present a saved schedule as live availability. Please check the reservation page or try again shortly. Source: https://esports.computing.psu.
- `INTENT-TRAP-EN-0311` (2.07s, `pipeline:live_booking_status_unavailable`): Is VR available Wednesday at 13:00?
  - Failures: missing required text: ['2026-09-30']
  - Answer excerpt: I cannot confirm the live opening or booking status right now because the Booking Dashboard is unavailable. I will not present a saved schedule as live availability. Please check the reservation page or try again shortly. Source: https://esports.computing.psu.

### th / damage_responsibility

- `INTENT-TRAP-TH-0158` (17.39s, `pipeline:no_answer`): ก่อนเดินทางไปใช้บริการ อยากทราบว่า ทำจอยเกมพังต้องรับผิดชอบยังไง
  - Failures: none of required alternatives found: ['ค่าปรับ', 'ชดเชย', 'รับผิดชอบ', 'fine', 'compensation', 'responsible']; route expected ['penalty', 'rules'], got equipment; status expected answer_available, got no_answer
  - Answer excerpt: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด equipment ตอนนี้ครับ
- `INTENT-TRAP-TH-0191` (1.02s, `pipeline:no_answer`): ทำเมาส์เกมมิ่งเสียหายต้องชดเชยไหม
  - Failures: none of required alternatives found: ['ค่าปรับ', 'ชดเชย', 'รับผิดชอบ', 'fine', 'compensation', 'responsible']; route expected ['penalty', 'rules'], got equipment; status expected answer_available, got no_answer
  - Answer excerpt: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด equipment ตอนนี้ครับ

### th / unclear_or_outside_scope

- `INTENT-TRAP-TH-0467` (2.19s, `pipeline:no_answer`): ขอถามเกี่ยวกับศูนย์หน่อยครับ: แนะนำหุ้นให้หน่อย
  - Failures: route expected ['clarification', 'general', 'knowledge', 'no_answer', 'overview'], got equipment
  - Answer excerpt: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด equipment ตอนนี้ครับ
- `INTENT-TRAP-TH-0486` (5.02s, `pipeline:structured_equipment_catalog`): ถ้าบอกแค่ว่าเครื่องล่ะ
  - Failures: forbidden text present: ['อุปกรณ์บนหน้า Home']; route expected ['clarification', 'general', 'knowledge', 'no_answer', 'overview'], got equipment
  - Answer excerpt: อุปกรณ์บนหน้า Home: PC Zone • Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง) • Gaming Monitor (จำนวน 10 จอ) • Gaming Chair (จำนวน 10 ตัว) • Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset Cockpit Zone • TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง) • Racez
- `INTENT-TRAP-TH-0496` (0.27s, `pipeline:game_meta_clarification`): มั่วๆๆ เรื่องเกมมั้ง
  - Failures: route expected ['clarification', 'general', 'knowledge', 'no_answer', 'overview'], got games
  - Answer excerpt: ถามเรื่องเกมได้ครับ แต่คำถามนี้ยังกว้างเกินไป เลยไม่ขอดึงเกมใดเกมหนึ่งมาตอบแทน ตัวอย่างที่ถามได้: • `มีเกมอะไรบ้าง` • `PS5 มีเกมอะไรบ้าง` • `TEKKEN 8 คือเกมอะไร` • `TEKKEN 8 มีปุ่มอะไรบ้าง` • `Nintendo Switch มีเกมแนวปาร์ตี้ไหม`

### th / weekday_live_slots

- `INTENT-TRAP-TH-0301` (2.16s, `pipeline:live_booking_status_unavailable`): วันจันทร์มี PC เครื่องไหนว่างบ้างตอนบ่ายโมง
  - Failures: missing required text: ['2026-09-28']
  - Answer excerpt: ขณะนี้ยังยืนยันสถานะเปิด-ปิดและ Slot แบบสดไม่ได้ เพราะ Booking Dashboard ไม่พร้อมใช้งานครับ ผมจะไม่เอาตารางเก่ามาแสดงว่าเป็นข้อมูลจองแบบสด กรุณาลองใหม่อีกครั้งหรือดูหน้าจองโดยตรง แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- `INTENT-TRAP-TH-0306` (2.12s, `pipeline:live_booking_status_unavailable`): วันอังคารบ่ายสอง PC 2 ว่างไหม
  - Failures: missing required text: ['2026-09-29']
  - Answer excerpt: ขณะนี้ยังยืนยันสถานะเปิด-ปิดและ Slot แบบสดไม่ได้ เพราะ Booking Dashboard ไม่พร้อมใช้งานครับ ผมจะไม่เอาตารางเก่ามาแสดงว่าเป็นข้อมูลจองแบบสด กรุณาลองใหม่อีกครั้งหรือดูหน้าจองโดยตรง แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- `INTENT-TRAP-TH-0311` (2.13s, `pipeline:live_booking_status_unavailable`): วันพุธเวลา 13:00 VR ว่างหรือเปล่า
  - Failures: missing required text: ['2026-09-30']
  - Answer excerpt: ขณะนี้ยังยืนยันสถานะเปิด-ปิดและ Slot แบบสดไม่ได้ เพราะ Booking Dashboard ไม่พร้อมใช้งานครับ ผมจะไม่เอาตารางเก่ามาแสดงว่าเป็นข้อมูลจองแบบสด กรุณาลองใหม่อีกครั้งหรือดูหน้าจองโดยตรง แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

## Interpretation limits

- Each locale has 100 distinct scenarios with five framing variants, not 500 independent intents.
- The shared evaluator checks route, status, latency, and string contracts. It does not judge semantic correctness or source support.
- `route_only` cases intentionally make no correctness claim beyond avoiding an obviously wrong route or forbidden catalog response; manually review their full answers.
- Weekday live-slot dates are relative to the manifest reference date. Rebuild the corpus before rerunning on a later date.
