# Intent-trap bilingual evaluation

Corpus: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\intent_trap_bilingual_1000_v1.jsonl`  
Results: `reports\master_ground_truth_eval\master_gt_eval_20260924_134028.json`  
Status: scenario-curated paraphrases pending human review; a passing automated check is not proof of factual correctness.

| Locale | Theme | Passed | Total | Route fails | Status fails | Content fails | >10s | >20s |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| en | booking_days_hours | 0 | 50 | 5 | 14 | 50 | 0 | 0 |
| en | damage_responsibility | 5 | 50 | 45 | 22 | 41 | 0 | 0 |
| en | equipment_access_trap | 24 | 50 | 26 | 0 | 10 | 0 | 0 |
| en | fee_without_service | 15 | 50 | 35 | 35 | 20 | 0 | 0 |
| en | food_bring_scope | 38 | 50 | 12 | 0 | 0 | 0 | 0 |
| en | food_consumption | 20 | 50 | 30 | 20 | 30 | 0 | 0 |
| en | identity_typo | 9 | 50 | 41 | 35 | 0 | 0 | 0 |
| en | outsider_eligibility | 27 | 50 | 23 | 0 | 5 | 0 | 0 |
| en | unclear_or_outside_scope | 40 | 50 | 10 | 0 | 0 | 0 | 0 |
| en | weekday_live_slots | 0 | 50 | 0 | 0 | 50 | 0 | 0 |
| th | booking_days_hours | 10 | 50 | 20 | 20 | 40 | 9 | 7 |
| th | damage_responsibility | 29 | 50 | 14 | 9 | 21 | 0 | 0 |
| th | equipment_access_trap | 11 | 50 | 39 | 0 | 19 | 2 | 0 |
| th | fee_without_service | 34 | 50 | 2 | 16 | 0 | 0 | 0 |
| th | food_bring_scope | 46 | 50 | 4 | 0 | 0 | 2 | 0 |
| th | food_consumption | 19 | 50 | 31 | 2 | 31 | 0 | 0 |
| th | identity_typo | 9 | 50 | 37 | 30 | 0 | 5 | 0 |
| th | outsider_eligibility | 31 | 50 | 19 | 0 | 0 | 6 | 0 |
| th | unclear_or_outside_scope | 39 | 50 | 11 | 0 | 5 | 7 | 0 |
| th | weekday_live_slots | 0 | 50 | 0 | 0 | 50 | 0 | 0 |

## Representative failures

### en / booking_days_hours

- `INTENT-TRAP-EN-0051` (0.04s, `pipeline:rule_en`): On which days and at what hours can I book a gaming station?
  - Failures: none of required alternatives found: ['09:00', '13:00', '9:00', '1 pm']
  - Answer excerpt: Booking steps: • Select a service. • Choose a date and time. • Fill in your user information. • Review the details. • Pay by bank transfer. • Upload the payment slip. Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)
- `INTENT-TRAP-EN-0056` (2.15s, `pipeline:live_booking_status_unavailable`): Which days and time periods are available for PC booking?
  - Failures: none of required alternatives found: ['09:00', '13:00', '9:00', '1 pm']; status expected answer_available, got no_answer
  - Answer excerpt: I cannot confirm the live opening or booking status right now because the Booking Dashboard is unavailable. I will not present a saved schedule as live availability. Please check the reservation page or try again shortly. Source: https://esports.computing.psu.
- `INTENT-TRAP-EN-0061` (0.03s, `pipeline:rule_en`): On which days can I book morning and afternoon slots?
  - Failures: none of required alternatives found: ['09:00', '13:00', '9:00', '1 pm']
  - Answer excerpt: Booking steps: • Select a service. • Choose a date and time. • Fill in your user information. • Review the details. • Pay by bank transfer. • Upload the payment slip. Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

### en / damage_responsibility

- `INTENT-TRAP-EN-0151` (0.40s, `pipeline:games_unknown_target_en`): If I damage a studio PS5, is there a penalty?
  - Failures: none of required alternatives found: ['ค่าปรับ', 'ชดเชย', 'รับผิดชอบ', 'fine', 'compensation', 'responsible']; route expected ['penalty', 'rules'], got games; status expected answer_available, got no_answer
  - Answer excerpt: I could not find penalty in the verified PSU game records. I will not substitute another game. Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- `INTENT-TRAP-EN-0156` (0.06s, `pipeline:structured_games_catalog_en`): What happens if I break a game controller?
  - Failures: none of required alternatives found: ['ค่าปรับ', 'ชดเชย', 'รับผิดชอบ', 'fine', 'compensation', 'responsible']; route expected ['penalty', 'rules'], got games
  - Answer excerpt: There are currently 42 verified games available. PC Zone (6 games) • Call of Duty: Warzone • Counter-Strike 2 • League of Legends • PUBG: BATTLEGROUNDS • TEKKEN 8 • VALORANT PlayStation 5 Zone (17 games) • Call of Duty: Modern Warfare III • Delta Force • EA Sp
- `INTENT-TRAP-EN-0161` (0.40s, `pipeline:english_no_answer`): What compensation applies if I break a PC monitor?
  - Failures: none of required alternatives found: ['ค่าปรับ', 'ชดเชย', 'รับผิดชอบ', 'fine', 'compensation', 'responsible']; route expected ['penalty', 'rules'], got no_answer; status expected answer_available, got no_answer
  - Answer excerpt: I could not find verified PSU Esports Studio - Phuket information for equipment.

### en / equipment_access_trap

- `INTENT-TRAP-EN-0401` (0.04s, `pipeline:structured_equipment_catalog_en`): Can outsiders come in and use the equipment?
  - Failures: forbidden text present: ['Verified equipment:']; route expected ['clarification', 'no_answer', 'reservation', 'rules'], got equipment
  - Answer excerpt: Verified equipment: - Gaming PC model MSI MAG Infinite S3 14th (PC Zone) - 10 Units - Gaming Monitor (PC Zone) - 10 Units - Gaming Keyboard (PC Zone) - Gaming Mouse (PC Zone) - Gaming Headset (PC Zone) - Gaming Chair (PC Zone) - 10 Units - Logitech G923 TRUEFO
- `INTENT-TRAP-EN-0407` (0.11s, `pipeline:rule_en`): A question about the studio: Are public visitors permitted to use the studio PCs?
  - Failures: route expected ['clarification', 'no_answer', 'reservation', 'rules'], got overview
  - Answer excerpt: PSU Esports Studio - Phuket is an esports learning development studio for excellence and economic advancement in Southern Thailand, Phuket branch, under Prince of Songkla University and operated by the College of Computing. Source: https://esports.phuket.psu.a
- `INTENT-TRAP-EN-0412` (0.10s, `pipeline:rule_en`): A question about the studio: May someone without a PSU ID use the PS5?
  - Failures: route expected ['clarification', 'no_answer', 'reservation', 'rules'], got overview
  - Answer excerpt: PSU Esports Studio - Phuket is an esports learning development studio for excellence and economic advancement in Southern Thailand, Phuket branch, under Prince of Songkla University and operated by the College of Computing. Source: https://esports.phuket.psu.a

### en / fee_without_service

- `INTENT-TRAP-EN-0001` (0.19s, `pipeline:structured_equipment_catalog_en`): How much does equipment use cost for an outsider?
  - Failures: forbidden text present: ['Verified equipment:']; route expected ['clarification', 'service_fee'], got equipment; status expected clarification_required, got answer
  - Answer excerpt: Verified equipment: - Gaming PC model MSI MAG Infinite S3 14th (PC Zone) - 10 Units - Gaming Monitor (PC Zone) - 10 Units - Gaming Keyboard (PC Zone) - Gaming Mouse (PC Zone) - Gaming Headset (PC Zone) - Gaming Chair (PC Zone) - 10 Units - Logitech G923 TRUEFO
- `INTENT-TRAP-EN-0006` (0.10s, `pipeline:structured_members_source_th`): What would a member of the public pay to play?
  - Failures: route expected ['clarification', 'service_fee'], got overview; status expected clarification_required, got answer
  - Answer excerpt: Official Thai source member record(s): Names and role titles below are shown exactly as published by PSU. - ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี - มหาวิทยาลัยสงขลานครินทร์ - รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี - มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต - รศ.ดร.อซ
- `INTENT-TRAP-EN-0011` (0.91s, `pipeline:english_no_answer`): What is the service fee for a non-PSU visitor?
  - Failures: route expected ['clarification', 'service_fee'], got no_answer; status expected clarification_required, got no_answer
  - Answer excerpt: I could not find verified PSU Esports Studio - Phuket information for service_fee.

### en / food_bring_scope

- `INTENT-TRAP-EN-0207` (0.06s, `pipeline:rule_en`): A question about the studio: Can I carry a water bottle inside? I am not asking about drinking.
  - Failures: route expected ['clarification', 'no_answer', 'rules'], got overview
  - Answer excerpt: PSU Esports Studio - Phuket is an esports learning development studio for excellence and economic advancement in Southern Thailand, Phuket branch, under Prince of Songkla University and operated by the College of Computing. Source: https://esports.phuket.psu.a
- `INTENT-TRAP-EN-0212` (0.06s, `pipeline:rule_en`): A question about the studio: May I carry a snack in my bag into the studio?
  - Failures: route expected ['clarification', 'no_answer', 'rules'], got overview
  - Answer excerpt: PSU Esports Studio - Phuket is an esports learning development studio for excellence and economic advancement in Southern Thailand, Phuket branch, under Prince of Songkla University and operated by the College of Computing. Source: https://esports.phuket.psu.a
- `INTENT-TRAP-EN-0217` (0.05s, `pipeline:rule_en`): A question about the studio: Is bringing coffee into the building allowed?
  - Failures: route expected ['clarification', 'no_answer', 'rules'], got overview
  - Answer excerpt: PSU Esports Studio - Phuket is an esports learning development studio for excellence and economic advancement in Southern Thailand, Phuket branch, under Prince of Songkla University and operated by the College of Computing. Source: https://esports.phuket.psu.a

### en / food_consumption

- `INTENT-TRAP-EN-0261` (0.05s, `pipeline:structured_equipment_catalog_en`): Can I drink in the gaming zone?
  - Failures: none of required alternatives found: ['พื้นที่ที่กำหนด', 'designated area']; route expected ['rules'], got equipment
  - Answer excerpt: Verified equipment: - Gaming PC model MSI MAG Infinite S3 14th (PC Zone) - 10 Units - Gaming Monitor (PC Zone) - 10 Units - Gaming Keyboard (PC Zone) - Gaming Mouse (PC Zone) - Gaming Headset (PC Zone) - Gaming Chair (PC Zone) - 10 Units - Logitech G923 TRUEFO
- `INTENT-TRAP-EN-0266` (0.05s, `pipeline:english_no_answer`): Which area allows snacks to be eaten?
  - Failures: none of required alternatives found: ['พื้นที่ที่กำหนด', 'designated area']; route expected ['rules'], got no_answer; status expected answer_available, got no_answer
  - Answer excerpt: I could not find verified PSU Esports Studio - Phuket information for this question.
- `INTENT-TRAP-EN-0271` (0.05s, `pipeline:english_no_answer`): Must coffee be consumed only in a designated area?
  - Failures: none of required alternatives found: ['พื้นที่ที่กำหนด', 'designated area']; route expected ['rules'], got no_answer; status expected answer_available, got no_answer
  - Answer excerpt: I could not find verified PSU Esports Studio - Phuket information for service_fee.

### en / identity_typo

- `INTENT-TRAP-EN-0351` (0.02s, `pipeline:chatbot_identity_en`): who r u
  - Failures: route expected ['general', 'home', 'overview'], got knowledge
  - Answer excerpt: I am PSU Esports Assistant, the chatbot for PSU Esports Studio - Phuket. I can help with verified information about games, equipment, booking, opening hours, service fees, rules, competitions, and studio contacts.
- `INTENT-TRAP-EN-0356` (0.02s, `pipeline:chatbot_identity_en`): who are u
  - Failures: route expected ['general', 'home', 'overview'], got knowledge
  - Answer excerpt: I am PSU Esports Assistant, the chatbot for PSU Esports Studio - Phuket. I can help with verified information about games, equipment, booking, opening hours, service fees, rules, competitions, and studio contacts.
- `INTENT-TRAP-EN-0361` (0.04s, `pipeline:english_no_answer`): who is this bot
  - Failures: route expected ['general', 'home', 'overview'], got no_answer; status expected answer_available, got no_answer
  - Answer excerpt: I could not find verified PSU Esports Studio - Phuket information for this question.

### en / outsider_eligibility

- `INTENT-TRAP-EN-0101` (0.04s, `pipeline:structured_members_source_th`): Can members of the public use the studio?
  - Failures: route expected ['clarification', 'no_answer', 'reservation', 'rules', 'service_fee'], got overview
  - Answer excerpt: Official Thai source member record(s): Names and role titles below are shown exactly as published by PSU. - ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี - มหาวิทยาลัยสงขลานครินทร์ - รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี - มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต - รศ.ดร.อซ
- `INTENT-TRAP-EN-0107` (0.10s, `pipeline:rule_en`): A question about the studio: Can someone who is not a PSU student play there?
  - Failures: route expected ['clarification', 'no_answer', 'reservation', 'rules', 'service_fee'], got overview
  - Answer excerpt: PSU Esports Studio - Phuket is an esports learning development studio for excellence and economic advancement in Southern Thailand, Phuket branch, under Prince of Songkla University and operated by the College of Computing. Source: https://esports.phuket.psu.a
- `INTENT-TRAP-EN-0116` (0.04s, `pipeline:structured_members_source_th`): Does a public visitor need membership before entering?
  - Failures: route expected ['clarification', 'no_answer', 'reservation', 'rules', 'service_fee'], got overview
  - Answer excerpt: Official Thai source member record(s): Names and role titles below are shown exactly as published by PSU. - ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี - มหาวิทยาลัยสงขลานครินทร์ - รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี - มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต - รศ.ดร.อซ

### en / unclear_or_outside_scope

- `INTENT-TRAP-EN-0476` (0.03s, `pipeline:chatbot_greeting_en`): helllooo
  - Failures: route expected ['clarification', 'general', 'no_answer', 'overview'], got knowledge
  - Answer excerpt: Hello. I am PSU Esports Assistant for PSU Esports Studio - Phuket. Ask me about games, equipment, booking, opening hours, fees, rules, or studio contacts.
- `INTENT-TRAP-EN-0496` (0.05s, `pipeline:structured_games_catalog_en`): umm games or something idk
  - Failures: route expected ['clarification', 'general', 'no_answer', 'overview'], got games
  - Answer excerpt: There are currently 42 verified games available. PC Zone (6 games) • Call of Duty: Warzone • Counter-Strike 2 • League of Legends • PUBG: BATTLEGROUNDS • TEKKEN 8 • VALORANT PlayStation 5 Zone (17 games) • Call of Duty: Modern Warfare III • Delta Force • EA Sp

### en / weekday_live_slots

- `INTENT-TRAP-EN-0301` (2.09s, `pipeline:live_booking_status_unavailable`): Which PC stations are free on Monday at 1 pm?
  - Failures: missing required text: ['2026-09-28']
  - Answer excerpt: I cannot confirm the live opening or booking status right now because the Booking Dashboard is unavailable. I will not present a saved schedule as live availability. Please check the reservation page or try again shortly. Source: https://esports.computing.psu.
- `INTENT-TRAP-EN-0306` (0.04s, `pipeline:live_booking_status_unavailable`): Is PC 2 free on Tuesday at 2 pm?
  - Failures: missing required text: ['2026-09-29']
  - Answer excerpt: I cannot confirm the live opening or booking status right now because the Booking Dashboard is unavailable. I will not present a saved schedule as live availability. Please check the reservation page or try again shortly. Source: https://esports.computing.psu.
- `INTENT-TRAP-EN-0311` (0.04s, `pipeline:live_booking_status_unavailable`): Is VR available Wednesday at 13:00?
  - Failures: missing required text: ['2026-09-30']
  - Answer excerpt: I cannot confirm the live opening or booking status right now because the Booking Dashboard is unavailable. I will not present a saved schedule as live availability. Please check the reservation page or try again shortly. Source: https://esports.computing.psu.

### th / booking_days_hours

- `INTENT-TRAP-TH-0051` (14.69s, `pipeline:booking_howto_fast_path`): การจองเครื่องเล่นเกมเปิดจองวันไหนและช่วงเวลาไหนบ้าง
  - Failures: none of required alternatives found: ['09:00', '13:00', '9:00', '1 pm']; forbidden text present: ['ขั้นตอนโดยสรุปคือ 1)']
  - Answer excerpt: จองคิวเล่นเกม/ใช้อุปกรณ์ได้ผ่านระบบจองออนไลน์ครับ ขั้นตอนโดยสรุปคือ 1) เลือกบริการหรือโซนที่ต้องการใช้ 2) เลือกวันและรอบเวลา 3) กรอก Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล และเบอร์โทรศัพท์ 4) ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง 5) แน
- `INTENT-TRAP-TH-0056` (2.13s, `pipeline:live_booking_status_unavailable`): จอง PC ได้วันอะไร ช่วงกี่โมง
  - Failures: none of required alternatives found: ['09:00', '13:00', '9:00', '1 pm']
  - Answer excerpt: ขณะนี้ยังยืนยันสถานะเปิด-ปิดและ Slot แบบสดไม่ได้ เพราะ Booking Dashboard ไม่พร้อมใช้งานครับ ผมจะไม่เอาตารางเก่ามาแสดงว่าเป็นข้อมูลจองแบบสด กรุณาลองใหม่อีกครั้งหรือดูหน้าจองโดยตรง แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- `INTENT-TRAP-TH-0061` (2.43s, `pipeline:answer_contract_no_answer`): มีรอบให้จองช่วงเช้ากับบ่ายวันไหนบ้าง
  - Failures: none of required alternatives found: ['09:00', '13:00', '9:00', '1 pm']; route expected ['reservation', 'schedule'], got no_answer; status expected answer_available, got no_answer
  - Answer excerpt: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด schedule ตอนนี้ครับ

### th / damage_responsibility

- `INTENT-TRAP-TH-0159` (0.35s, `pipeline:game_meta_clarification`): ทำจอยเกมพังต้องรับผิดชอบยังไง ตอบเฉพาะประเด็นที่ถามได้ไหม
  - Failures: none of required alternatives found: ['ค่าปรับ', 'ชดเชย', 'รับผิดชอบ', 'fine', 'compensation', 'responsible']; route expected ['penalty', 'rules'], got games; status expected answer_available, got clarification
  - Answer excerpt: ถามเรื่องเกมได้ครับ แต่คำถามนี้ยังกว้างเกินไป เลยไม่ขอดึงเกมใดเกมหนึ่งมาตอบแทน ตัวอย่างที่ถามได้: • `มีเกมอะไรบ้าง` • `PS5 มีเกมอะไรบ้าง` • `TEKKEN 8 คือเกมอะไร` • `TEKKEN 8 มีปุ่มอะไรบ้าง` • `Nintendo Switch มีเกมแนวปาร์ตี้ไหม`
- `INTENT-TRAP-TH-0161` (2.23s, `pipeline:answer_contract_no_answer`): จอคอมแตกตอนใช้งานต้องชดใช้เท่าไหร่
  - Failures: none of required alternatives found: ['ค่าปรับ', 'ชดเชย', 'รับผิดชอบ', 'fine', 'compensation', 'responsible']; route expected ['penalty', 'rules'], got no_answer; status expected answer_available, got no_answer
  - Answer excerpt: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด service_fee ตอนนี้ครับ
- `INTENT-TRAP-TH-0166` (0.86s, `pipeline:multi_question_splitter`): เผลอทำอุปกรณ์ของศูนย์เสียต้องแจ้งใครและจ่ายไหม
  - Failures: none of required alternatives found: ['ค่าปรับ', 'ชดเชย', 'รับผิดชอบ', 'fine', 'compensation', 'responsible']; route expected ['penalty', 'rules'], got multi_question
  - Answer excerpt: คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ: คำถามที่ 1: เผลอทำอุปกรณ์ของศูนย์เสียต้องแจ้งใคร อุปกรณ์บนหน้า Home: PC Zone • Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง) • Gaming Monitor (จำนวน 10 จอ) • Gaming Chair (จำนวน 10 ตัว) • Gaming Gear ครบชุด 

### th / equipment_access_trap

- `INTENT-TRAP-TH-0401` (0.53s, `pipeline:structured_equipment_catalog`): บุคคลภายนอกเข้าใช้อุปกรณ์ในห้องอีสปอร์ตได้มั้ย
  - Failures: forbidden text present: ['อุปกรณ์บนหน้า Home']; route expected ['clarification', 'no_answer', 'reservation', 'rules'], got equipment
  - Answer excerpt: อุปกรณ์บนหน้า Home: PC Zone • Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง) • Gaming Monitor (จำนวน 10 จอ) • Gaming Chair (จำนวน 10 ตัว) • Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset Cockpit Zone • TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง) • Racez
- `INTENT-TRAP-TH-0406` (0.34s, `pipeline:structured_equipment_catalog`): คนทั่วไปมีสิทธิ์เล่นเครื่อง PC ของศูนย์ไหม
  - Failures: route expected ['clarification', 'no_answer', 'reservation', 'rules'], got equipment
  - Answer excerpt: อุปกรณ์ใน PC Zone: PC Zone • Gaming PC รุ่น MSI MAG Infinite S3 14th (10 Units) • Gaming Monitor (10 Units) • Gaming Keyboard • Gaming Mouse • Gaming Headset • Gaming Chair (10 Units) แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
- `INTENT-TRAP-TH-0411` (0.69s, `pipeline:structured_equipment_catalog`): ถ้าไม่มีรหัส PSU ใช้เครื่อง PS5 ได้หรือเปล่า
  - Failures: route expected ['clarification', 'no_answer', 'reservation', 'rules'], got equipment
  - Answer excerpt: อุปกรณ์ใน PlayStation 5 Zone / VR Zone: PlayStation 5 Zone / VR Zone • PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive (2 Units in PlayStation 5 Zone and 1 Unit in VR Zone) แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### th / fee_without_service

- `INTENT-TRAP-TH-0002` (0.69s, `pipeline:multi_question_splitter`): ขอถามเกี่ยวกับศูนย์หน่อยครับ: บุคคลภายนอกใช้อุปกรณ์คิดราคาเท่าไหร่
  - Failures: route expected ['clarification', 'service_fee'], got multi_question; status expected clarification_required, got answer
  - Answer excerpt: คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ: คำถามที่ 1: ขอถามเกี่ยว ราคาเท่าไหร่ ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่` คำถามที่ 2: ศูนย์หน่อยครับ: บุคคล
- `INTENT-TRAP-TH-0008` (0.46s, `pipeline:rag_direct_curated`): ก่อนเดินทางไปใช้บริการ อยากทราบว่า คนทั่วไปเข้าไปเล่นคิดเงินยังไง
  - Failures: status expected clarification_required, got answer
  - Answer excerpt: บริการ PC ในระบบจองมีระยะเวลา 60 min แต่ในข้อมูลที่ดึงมาและในรูป Service Fee 2026 ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ จึงยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-S
- `INTENT-TRAP-TH-0013` (0.60s, `pipeline:rag_direct_curated`): ก่อนเดินทางไปใช้บริการ อยากทราบว่า ค่าใช้บริการสำหรับคนนอกเท่าไหร่
  - Failures: status expected clarification_required, got answer
  - Answer excerpt: คำถามที่ใช้คำว่า นักศึกษา ม.อ., นักเรียน ม.อ., เด็ก ม.อ., นักศึกษา PSU, นักเรียน PSU, บุคลากร PSU, staff PSU, PSU student, PSU staff ให้ตีความเป็นกลุ่ม PSU Student and Staff ในตาราง Service Fee 2026 ซึ่งเป็นกลุ่มที่ค่าบริการในภาพระบุว่า Free หรือ 0 บาท สำหรับบ

### th / food_bring_scope

- `INTENT-TRAP-TH-0216` (6.37s, `pipeline:general_llm_after_rag_miss`): อนุญาตให้นำกาแฟเข้าอาคารหรือไม่
  - Failures: route expected ['clarification', 'no_answer', 'rules'], got general
  - Answer excerpt: ขออนุญาตยืนยันว่าอนุญาตให้นำกาแฟเข้าอาคารได้ครับ หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket

### th / food_consumption

- `INTENT-TRAP-TH-0251` (0.27s, `pipeline:rag_direct_curated`): รับประทานอาหารในศูนย์ได้ตรงไหน
  - Failures: none of required alternatives found: ['พื้นที่ที่กำหนด', 'designated area']; route expected ['rules'], got contact
  - Answer excerpt: ติดต่อศูนย์ได้ทางอีเมล psuesportspkt@gmail.com โทร +66 7627 6004 หรือ +66 7627 6045 และ Facebook PSU Esports Phuket แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Contact-Us
- `INTENT-TRAP-TH-0259` (0.30s, `pipeline:game_meta_clarification`): กินข้าวที่โต๊ะเกมได้ไหม ตอบเฉพาะประเด็นที่ถามได้ไหม
  - Failures: none of required alternatives found: ['พื้นที่ที่กำหนด', 'designated area']; route expected ['rules'], got games; status expected answer_available, got clarification
  - Answer excerpt: ถามเรื่องเกมได้ครับ แต่คำถามนี้ยังกว้างเกินไป เลยไม่ขอดึงเกมใดเกมหนึ่งมาตอบแทน ตัวอย่างที่ถามได้: • `มีเกมอะไรบ้าง` • `PS5 มีเกมอะไรบ้าง` • `TEKKEN 8 คือเกมอะไร` • `TEKKEN 8 มีปุ่มอะไรบ้าง` • `Nintendo Switch มีเกมแนวปาร์ตี้ไหม`
- `INTENT-TRAP-TH-0261` (0.34s, `pipeline:structured_service_game_availability`): ดื่มน้ำในโซนเล่นเกมได้หรือเปล่า
  - Failures: none of required alternatives found: ['พื้นที่ที่กำหนด', 'designated area']; route expected ['rules'], got games
  - Answer excerpt: บริการที่ถาม มีเกมที่ยืนยันได้ดังนี้ PC #01-#02 (60 นาที, 1 คน) • TEKKEN 8 • Counter-Strike 2 • League of Legends • PUBG: BATTLEGROUNDS • VALORANT หมายเหตุ: PC #01-#02 มี TEKKEN 8 แต่ไม่มี Call of Duty: Warzone หมายเหตุ: PC #01-#02 และ PC #03-#10 มี Counter-St

### th / identity_typo

- `INTENT-TRAP-TH-0351` (0.02s, `pipeline:chatbot_identity_fast_path`): นายเปนไค
  - Failures: route expected ['general', 'home', 'overview'], got knowledge
  - Answer excerpt: ผมคือ PSU Esports Assistant แชทบอทผู้ช่วยของ PSU Esports Studio - Phuket ครับ ผมช่วยตอบคำถามเกี่ยวกับ: • เกมที่มีให้เล่นและเกมที่เกี่ยวข้องกับการแข่งขัน • ปุ่มควบคุมและวิธีเล่นของเกมที่มีข้อมูลยืนยัน • อุปกรณ์และโซนบริการ เช่น PC, PS5, Nintendo Switch, VR และ 
- `INTENT-TRAP-TH-0356` (0.05s, `pipeline:chatbot_identity_fast_path`): นายเปนใคร
  - Failures: route expected ['general', 'home', 'overview'], got knowledge
  - Answer excerpt: ผมคือ PSU Esports Assistant แชทบอทผู้ช่วยของ PSU Esports Studio - Phuket ครับ ผมช่วยตอบคำถามเกี่ยวกับ: • เกมที่มีให้เล่นและเกมที่เกี่ยวข้องกับการแข่งขัน • ปุ่มควบคุมและวิธีเล่นของเกมที่มีข้อมูลยืนยัน • อุปกรณ์และโซนบริการ เช่น PC, PS5, Nintendo Switch, VR และ 
- `INTENT-TRAP-TH-0361` (4.43s, `pipeline:chatbot_identity_fast_path`): นายนี่คือใคร
  - Failures: route expected ['general', 'home', 'overview'], got knowledge
  - Answer excerpt: ผมคือ PSU Esports Assistant แชทบอทผู้ช่วยของ PSU Esports Studio - Phuket ครับ ผมช่วยตอบคำถามเกี่ยวกับ: • เกมที่มีให้เล่นและเกมที่เกี่ยวข้องกับการแข่งขัน • ปุ่มควบคุมและวิธีเล่นของเกมที่มีข้อมูลยืนยัน • อุปกรณ์และโซนบริการ เช่น PC, PS5, Nintendo Switch, VR และ 

### th / outsider_eligibility

- `INTENT-TRAP-TH-0106` (0.46s, `pipeline:schedule_fast_path`): คนที่ไม่ใช่นักศึกษา PSU เข้าไปเล่นได้หรือเปล่า
  - Failures: route expected ['clarification', 'no_answer', 'reservation', 'rules', 'service_fee'], got schedule
  - Answer excerpt: เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน รายละเอียดจากตาราง: • Morning คือ 09:00-12:00 • Afternoon คือ 13:00-16:00 • Monday ช่วง Morning 09:00-12:00 เป็น Maintenance* • Monday ช่วง Afternoon 13:00-16
- `INTENT-TRAP-TH-0116` (0.20s, `pipeline:structured_members_group_list`): คนทั่วไปต้องเป็นสมาชิกก่อนเข้าศูนย์หรือไม่
  - Failures: route expected ['clarification', 'no_answer', 'reservation', 'rules', 'service_fee'], got overview
  - Answer excerpt: สมาชิกจากหน้า Members แยกตามหมวด รวม 25 คน: Members (7 คน): • ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี • รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี • รศ.ดร.อซีส นันทอมรพงศ์: คณบดี • ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ • นายพฤทธิ์ เกษตรสมบูรณ์: นักวิชาการคอมพิ
- `INTENT-TRAP-TH-0131` (0.29s, `pipeline:structured_equipment_catalog`): บุคคลทั่วไปเข้าใช้ PC Zone ได้หรือไม่
  - Failures: route expected ['clarification', 'no_answer', 'reservation', 'rules', 'service_fee'], got equipment
  - Answer excerpt: อุปกรณ์ใน PC Zone: PC Zone • Gaming PC รุ่น MSI MAG Infinite S3 14th (10 Units) • Gaming Monitor (10 Units) • Gaming Keyboard • Gaming Mouse • Gaming Headset • Gaming Chair (10 Units) แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### th / unclear_or_outside_scope

- `INTENT-TRAP-TH-0467` (1.45s, `pipeline:no_answer`): ขอถามเกี่ยวกับศูนย์หน่อยครับ: แนะนำหุ้นให้หน่อย
  - Failures: route expected ['clarification', 'general', 'no_answer', 'overview'], got equipment
  - Answer excerpt: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด equipment ตอนนี้ครับ
- `INTENT-TRAP-TH-0486` (4.73s, `pipeline:structured_equipment_catalog`): ถ้าบอกแค่ว่าเครื่องล่ะ
  - Failures: forbidden text present: ['อุปกรณ์บนหน้า Home']; route expected ['clarification', 'general', 'no_answer', 'overview'], got equipment
  - Answer excerpt: อุปกรณ์บนหน้า Home: PC Zone • Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง) • Gaming Monitor (จำนวน 10 จอ) • Gaming Chair (จำนวน 10 ตัว) • Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset Cockpit Zone • TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง) • Racez
- `INTENT-TRAP-TH-0496` (0.19s, `pipeline:game_meta_clarification`): มั่วๆๆ เรื่องเกมมั้ง
  - Failures: route expected ['clarification', 'general', 'no_answer', 'overview'], got games
  - Answer excerpt: ถามเรื่องเกมได้ครับ แต่คำถามนี้ยังกว้างเกินไป เลยไม่ขอดึงเกมใดเกมหนึ่งมาตอบแทน ตัวอย่างที่ถามได้: • `มีเกมอะไรบ้าง` • `PS5 มีเกมอะไรบ้าง` • `TEKKEN 8 คือเกมอะไร` • `TEKKEN 8 มีปุ่มอะไรบ้าง` • `Nintendo Switch มีเกมแนวปาร์ตี้ไหม`

### th / weekday_live_slots

- `INTENT-TRAP-TH-0301` (2.17s, `pipeline:live_booking_status_unavailable`): วันจันทร์มี PC เครื่องไหนว่างบ้างตอนบ่ายโมง
  - Failures: missing required text: ['2026-09-28']
  - Answer excerpt: ขณะนี้ยังยืนยันสถานะเปิด-ปิดและ Slot แบบสดไม่ได้ เพราะ Booking Dashboard ไม่พร้อมใช้งานครับ ผมจะไม่เอาตารางเก่ามาแสดงว่าเป็นข้อมูลจองแบบสด กรุณาลองใหม่อีกครั้งหรือดูหน้าจองโดยตรง แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- `INTENT-TRAP-TH-0306` (0.07s, `pipeline:live_booking_status_unavailable`): วันอังคารบ่ายสอง PC 2 ว่างไหม
  - Failures: missing required text: ['2026-09-29']
  - Answer excerpt: ขณะนี้ยังยืนยันสถานะเปิด-ปิดและ Slot แบบสดไม่ได้ เพราะ Booking Dashboard ไม่พร้อมใช้งานครับ ผมจะไม่เอาตารางเก่ามาแสดงว่าเป็นข้อมูลจองแบบสด กรุณาลองใหม่อีกครั้งหรือดูหน้าจองโดยตรง แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- `INTENT-TRAP-TH-0311` (0.08s, `pipeline:live_booking_status_unavailable`): วันพุธเวลา 13:00 VR ว่างหรือเปล่า
  - Failures: missing required text: ['2026-09-30']
  - Answer excerpt: ขณะนี้ยังยืนยันสถานะเปิด-ปิดและ Slot แบบสดไม่ได้ เพราะ Booking Dashboard ไม่พร้อมใช้งานครับ ผมจะไม่เอาตารางเก่ามาแสดงว่าเป็นข้อมูลจองแบบสด กรุณาลองใหม่อีกครั้งหรือดูหน้าจองโดยตรง แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

## Interpretation limits

- Each locale has 100 distinct scenarios with five framing variants, not 500 independent intents.
- The shared evaluator checks route, status, latency, and string contracts. It does not judge semantic correctness or source support.
- `route_only` cases intentionally make no correctness claim beyond avoiding an obviously wrong route or forbidden catalog response; manually review their full answers.
- Weekday live-slot dates are relative to the manifest reference date. Rebuild the corpus before rerunning on a later date.
