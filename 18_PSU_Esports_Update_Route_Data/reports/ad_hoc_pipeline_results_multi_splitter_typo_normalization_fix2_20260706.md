# Ad Hoc Pipeline Test Log

- Generated: 2026-07-06T03:08:21
- JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\ad_hoc_pipeline_results_multi_splitter_typo_normalization_fix2_20260706.jsonl`
- Total questions: 8

## Summary

- games/competition_game_list: 1
- games/game_availability_lookup: 1
- multi_question/multi_question_split: 4
- schedule/schedule_query: 1
- service_fee/service_fee_query: 1

## Results

### 1. วันนี้เปิดไหม แล้ว VR ราคาเท่าไหร่

- mode: `pipeline:multi_question_splitter`
- route: `multi_question/multi_question_split`
- confidence: `0.97`
- elapsed: `0.0373` sec

คำตอบ:

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

1. วันนี้เปิดไหม
วันนี้ 06/07/2026 (วันจันทร์): วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*
วันที่อ้างอิงของระบบ: วันนี้คือ 06/07/2026 (วันจันทร์) ตามเวลาไทย

รายละเอียดจากตาราง:
- วันจันทร์ช่วงเช้า 09:00-12:00 เป็น Maintenance* และเปิดช่วงบ่าย 13:00-16:00
- วันอังคาร-พฤหัสบดีเปิด 09:00-12:00 และ 13:00-16:00
- วันศุกร์เปิดช่วงเช้า 09:00-12:00 และช่วงบ่าย 13:00-16:00 เป็น Maintenance
- วันหยุดราชการ/วันปิดพิเศษในไฟล์ปฏิทินจะมีผลก่อนตารางปกติ
แหล่งข้อมูลตารางบริการ: https://esports.computing.psu.ac.th/reservation

2. VR ราคาเท่าไหร่
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

แหล่งข้อมูล:
- Reservation | https://esports.computing.psu.ac.th/reservation
- service_fee_image_2026 | https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### 2. มีอุปกรณ์อะไรให้เล่นบ้าง และ VR มีเกมอะไรบ้าง

- mode: `pipeline:multi_question_splitter`
- route: `multi_question/multi_question_split`
- confidence: `0.9`
- elapsed: `0.021` sec

คำตอบ:

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

1. มีอุปกรณ์อะไรให้เล่นบ้าง
อุปกรณ์บนหน้า Home:
- PC Zone: Gaming PC รุ่น MSI MAG Infinite S3 14th 10 Units, Gaming Monitor 10 Units, Gaming Chair 10 Units, Gaming Keyboard, Gaming Mouse และ Gaming Headset
- Cockpit Zone: TV 65" 2 Units, Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 Units, Racezone Full Cockpit V3 2 Units และ Pulse Elite Wireless Headset 2 Units
- Nintendo Switch Zone: TV 86" 1 Units, Sofa 2 seats 2 Units และ Nintendo Switch OLED 1 Units
- PlayStation 5 Zone: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 2 Units
- VR Zone: PlayStation 5 Slim 1 Units และ Sony PlayStation VR2 1 Unit
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

2. VR มีเกมอะไรบ้าง
สรุปเกมที่เล่นได้ในโซนที่ถาม:
- VR Zone: Beat Saber และ Horizon Call of the Mountain
  อุปกรณ์หลัก: PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive 1 เครื่อง (1 Unit) และ Sony PlayStation VR2 1 ชุด (1 Unit)
  วิธีใช้งานโดยสรุป: จอง VR Zone แล้วสวม PlayStation VR2 ใช้คอนโทรลเลอร์ VR ตามคำแนะนำของเกมหรือเจ้าหน้าที่ และควรเล่นในพื้นที่ที่จัดไว้เท่านั้น
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

แหล่งข้อมูล:
- home | https://esports.phuket.psu.ac.th/home
- our_games | https://esports.phuket.psu.ac.th/Services/our-games
- Reservation | https://esports.computing.psu.ac.th/reservation

### 3. ตอนนี้รายการแข่งมเกมอะไรบ้าง

- mode: `pipeline:competition_game_list_fast_path`
- route: `games/competition_game_list`
- confidence: `0.95`
- elapsed: `0.0073` sec

คำตอบ:

เกม/รายการแข่งขันที่มีข้อมูลกติกาในฐานข้อมูลตอนนี้:
- Counter-Strike 2: PSU Phuket CS2 2026 Tournament
- VALORANT: PSU Phuket VALORANT 2026 Tournament
- Arena of Valor (RoV): Blueket Games 2025 ประเภททีมชาย
- TEKKEN 8: PSU Esports / Tekken 8 Tournament
หมายเหตุ: นี่คือรายการที่มีเอกสารกติกาหรือข้อมูลการแข่งขันในฐานข้อมูล ไม่ได้ยืนยันว่าเปิดรับสมัครอยู่ตอนนี้
แหล่งข้อมูล: data/competition_rules

แหล่งข้อมูล:
- our_games | https://esports.phuket.psu.ac.th/Services/our-games
- Reservation | https://esports.computing.psu.ac.th/reservation

### 4. Beat Saber คือเกมอะไรแล้วเล่นยังไง

- mode: `pipeline:game_detail_fast_path`
- route: `games/game_availability_lookup`
- confidence: `0.96`
- elapsed: `0.0107` sec

คำตอบ:

Beat Saber: Beat Saber คือเกม VR จังหวะดนตรีที่ผู้เล่นใช้ดาบแสงฟันบล็อกตามจังหวะเพลง
แนวเกม: เกม VR Rhythm
วิธีเล่นโดยสรุป: สวมแว่น VR ถือคอนโทรลเลอร์ แล้วฟันบล็อกตามทิศทาง หลบสิ่งกีดขวาง และพยายามทำคะแนนตามจังหวะเพลง
เล่นได้ที่: VR Zone
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

แหล่งข้อมูล:
- our_games | https://esports.phuket.psu.ac.th/Services/our-games
- Reservation | https://esports.computing.psu.ac.th/reservation

### 5. VR 30 นาที กับ VR 1 ชั่วโมงต่างกันเท่าไหร่

- mode: `pipeline:deterministic_calculator_fast`
- route: `service_fee/service_fee_query`
- confidence: `0.97`
- elapsed: `0.0415` sec

คำตอบ:

ต่างกัน 185 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
- VR 1 ชั่วโมง ราคา 375 บาท
ดังนั้น VR 1 ชั่วโมงแพงกว่า VR 30 นาที 185 บาท

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

แหล่งข้อมูล:
- service_fee_image_2026 | https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### 6. วันจัทนร์เปิดให้เล่นได้กี่โมง

- mode: `pipeline:schedule_fast_path`
- route: `schedule/schedule_query`
- confidence: `0.98`
- elapsed: `0.0039` sec

คำตอบ:

วันจันทร์เปิดให้เล่นช่วง 13:00-16:00 ส่วนช่วงเช้า 09:00-12:00 เป็น Maintenance*

รายละเอียดจากตาราง:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
- Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
- Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
- Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
- Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

แหล่งข้อมูล:
- Reservation | https://esports.computing.psu.ac.th/reservation

### 7. สอนจองได้ไหม แล้วเช็คอินล่วงหน้าได้กี่นาที

- mode: `pipeline:multi_question_splitter`
- route: `multi_question/multi_question_split`
- confidence: `0.9`
- elapsed: `0.0228` sec

คำตอบ:

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

1. สอนจองได้ไหม
ได้ครับ ขั้นตอนจองโดยสรุปคือ 1) เลือกบริการและรอบเวลาที่ต้องการ 2) กรอก Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล และเบอร์โทรศัพท์ 3) ชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง 4) แนบสลิปและยืนยันการจอง โดยต้องจองล่วงหน้าอย่างน้อย 1 ชั่วโมง และหลังจองต้องชำระเงินภายใน 10 นาที
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

2. เช็คอินล่วงหน้าได้กี่นาที
เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

แหล่งข้อมูล:
- Reservation | https://esports.computing.psu.ac.th/reservation

### 8. Minecraft เล่นได้ไหม และตอนนี้มีเกมแข่งอะไรบ้าง

- mode: `pipeline:multi_question_splitter`
- route: `multi_question/multi_question_split`
- confidence: `0.94`
- elapsed: `0.0211` sec

คำตอบ:

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

1. Minecraft เล่นได้ไหม
ยังไม่พบ Minecraft ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ
ถ้าต้องการเล่นเกมนอกเหนือจากรายการนี้ ควรสอบถามเจ้าหน้าที่ก่อนจองหรือก่อนเข้าใช้บริการ

เกมที่มีข้อมูลยืนยันตอนนี้:
- PC Zone: VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, TEKKEN 8 และ League of Legends
- PlayStation 5 Zone: Marvel's Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกม PS5 อื่น ๆ ในรายการ
- Nintendo Switch Zone: Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกม Switch อื่น ๆ ในรายการ
- Cockpit Zone: Gran Turismo 7
- VR Zone: Beat Saber และ Horizon Call of the Mountain
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

2. ตอนนี้มีเกมแข่งอะไรบ้าง
เกม/รายการแข่งขันที่มีข้อมูลกติกาในฐานข้อมูลตอนนี้:
- Counter-Strike 2: PSU Phuket CS2 2026 Tournament
- VALORANT: PSU Phuket VALORANT 2026 Tournament
- Arena of Valor (RoV): Blueket Games 2025 ประเภททีมชาย
- TEKKEN 8: PSU Esports / Tekken 8 Tournament
หมายเหตุ: นี่คือรายการที่มีเอกสารกติกาหรือข้อมูลการแข่งขันในฐานข้อมูล ไม่ได้ยืนยันว่าเปิดรับสมัครอยู่ตอนนี้
แหล่งข้อมูล: data/competition_rules

แหล่งข้อมูล:
- our_games | https://esports.phuket.psu.ac.th/Services/our-games
- Reservation | https://esports.computing.psu.ac.th/reservation
