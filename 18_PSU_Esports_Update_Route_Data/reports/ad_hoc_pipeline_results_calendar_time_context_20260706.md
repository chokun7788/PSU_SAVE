# Ad Hoc Pipeline Test Log

- Generated: 2026-07-06T16:43:23
- JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\ad_hoc_pipeline_results_calendar_time_context_20260706.jsonl`
- Total questions: 11

## Summary

- events_news/news_lookup: 1
- games/competition_game_list: 1
- games/game_availability_lookup: 1
- schedule/schedule_query: 7
- service_fee/service_fee_query: 1

## Results

### 1. วันนี้วันที่เท่าไหร่

- mode: `pipeline:rag_direct_curated`
- route: `service_fee/service_fee_query`
- confidence: `0.84`
- elapsed: `0.0151` sec

คำตอบ:

คำถามที่ใช้คำว่า ศิษย์เก่า PSU, alumni, General Student, นักศึกษาทั่วไป, นักเรียนทั่วไป, นักศึกษาต่างมหาวิทยาลัย, นักเรียนต่างมหาวิทยาลัย, นักศึกษาต่างมหาลัย, นักเรียนต่างมหาลัย, เด็กต่างมหาลัย, ต่างมหาลัย, นักศึกษาจากมหาวิทยาลัยอื่น, นักศึกษาจากต่างสถาบัน ให้ตีความเป็นกลุ่ม PSU Alumni and General Student ในตาราง Service Fee 2026
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

แหล่งข้อมูล:
- curated_user_group_alias_general_student | https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
- curated_user_group_alias_general_adult | https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
- curated_service_fee_pc_unknown | https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### 2. ตอนนี้กี่โมง

- mode: `pipeline:current_service_slot_fast_path`
- route: `schedule/schedule_query`
- confidence: `0.99`
- elapsed: `0.0211` sec

คำตอบ:

ตอนนี้เล่นได้ครับ อยู่ช่วง Afternoon 13:00-16:00
เวลาระบบ: 14:30 น. วันที่ 06/07/2026 (วันจันทร์) ตามเวลาไทย

ตารางประจำที่ใช้ตรวจ:
- วันจันทร์: 09:00-12:00 Maintenance*, 13:00-16:00 เปิดให้บริการ
- วันอังคาร-พฤหัสบดี: 09:00-12:00 และ 13:00-16:00 เปิดให้บริการ
- วันศุกร์: 09:00-12:00 เปิดให้บริการ, 13:00-16:00 Maintenance
- วันหยุด/วันปิดพิเศษของศูนย์จะดูจากไฟล์ปิดบริการก่อนตารางประจำ
แหล่งข้อมูลตารางบริการ: https://esports.computing.psu.ac.th/reservation

แหล่งข้อมูล:
- Reservation | https://esports.computing.psu.ac.th/reservation

### 3. ตอนนี้เล่นช่วงไหนได้บ้าง

- mode: `pipeline:current_service_slot_fast_path`
- route: `schedule/schedule_query`
- confidence: `0.99`
- elapsed: `0.0083` sec

คำตอบ:

ตอนนี้เล่นได้ครับ อยู่ช่วง Afternoon 13:00-16:00
เวลาระบบ: 14:30 น. วันที่ 06/07/2026 (วันจันทร์) ตามเวลาไทย

ตารางประจำที่ใช้ตรวจ:
- วันจันทร์: 09:00-12:00 Maintenance*, 13:00-16:00 เปิดให้บริการ
- วันอังคาร-พฤหัสบดี: 09:00-12:00 และ 13:00-16:00 เปิดให้บริการ
- วันศุกร์: 09:00-12:00 เปิดให้บริการ, 13:00-16:00 Maintenance
- วันหยุด/วันปิดพิเศษของศูนย์จะดูจากไฟล์ปิดบริการก่อนตารางประจำ
แหล่งข้อมูลตารางบริการ: https://esports.computing.psu.ac.th/reservation

แหล่งข้อมูล:
- Reservation | https://esports.computing.psu.ac.th/reservation

### 4. ตอนนี้เปิดไหม

- mode: `pipeline:current_service_slot_fast_path`
- route: `schedule/schedule_query`
- confidence: `0.99`
- elapsed: `0.0046` sec

คำตอบ:

ตอนนี้เล่นได้ครับ อยู่ช่วง Afternoon 13:00-16:00
เวลาระบบ: 14:30 น. วันที่ 06/07/2026 (วันจันทร์) ตามเวลาไทย

ตารางประจำที่ใช้ตรวจ:
- วันจันทร์: 09:00-12:00 Maintenance*, 13:00-16:00 เปิดให้บริการ
- วันอังคาร-พฤหัสบดี: 09:00-12:00 และ 13:00-16:00 เปิดให้บริการ
- วันศุกร์: 09:00-12:00 เปิดให้บริการ, 13:00-16:00 Maintenance
- วันหยุด/วันปิดพิเศษของศูนย์จะดูจากไฟล์ปิดบริการก่อนตารางประจำ
แหล่งข้อมูลตารางบริการ: https://esports.computing.psu.ac.th/reservation

แหล่งข้อมูล:
- Reservation | https://esports.computing.psu.ac.th/reservation

### 5. วันนี้เป็นวันหยุดไทยไหม

- mode: `pipeline:calendar_date_context_fast_path`
- route: `schedule/schedule_query`
- confidence: `0.98`
- elapsed: `0.0073` sec

คำตอบ:

วันนี้คือ 06/07/2026 (วันจันทร์)
เวลาระบบตอนนี้: 14:30 น. ตามเวลาไทย
ปฏิทินไทย:
ไม่พบวันหยุดไทยหรือเทศกาลในปฏิทินที่บันทึกไว้สำหรับวันนี้
สถานะศูนย์: ยังไม่พบวันปิดพิเศษของศูนย์สำหรับวันที่นี้ในไฟล์ service_closures.jsonl
หมายเหตุ: วันหยุดไทย/เทศกาลเป็นข้อมูลปฏิทินประกอบ ไม่ได้แปลว่าศูนย์ปิดโดยอัตโนมัติ
แหล่งข้อมูลปฏิทินไทย: https://www.timeanddate.com/holidays/thailand/2026
แหล่งข้อมูลตารางบริการ: https://esports.computing.psu.ac.th/reservation

แหล่งข้อมูล:
- Reservation | https://esports.computing.psu.ac.th/reservation

### 6. เดือนนี้มีวันหยุดไทยอะไรบ้าง

- mode: `pipeline:calendar_month_context_fast_path`
- route: `schedule/schedule_query`
- confidence: `0.98`
- elapsed: `0.0095` sec

คำตอบ:

เดือนกรกฎาคม 2026 มีข้อมูลปฏิทินไทย 3 รายการ:
- 28/07/2026 (วันอังคาร): วันเฉลิมพระชนมพรรษาพระบาทสมเด็จพระเจ้าอยู่หัว (national_holiday) - วันหยุดประจำปีของไทย
- 29/07/2026 (วันพุธ): วันอาสาฬหบูชา (national_holiday) - วันหยุดประจำปีของไทย
- 30/07/2026 (วันพฤหัสบดี): วันเข้าพรรษา (observance) - วันสำคัญทางพระพุทธศาสนา; ศูนย์จะปิดเฉพาะเมื่อมีใน service_closures.jsonl

วันปิดบริการของศูนย์ในเดือนนี้ที่บันทึกไว้: 3 วัน
- 28/07/2026 (วันอังคาร): วันหยุดราชการ - ศูนย์ปิดให้บริการตามวันหยุดราชการ/วันปิดพิเศษที่ระบุไว้ในระบบ
- 29/07/2026 (วันพุธ): วันหยุดราชการ - ศูนย์ปิดให้บริการตามวันหยุดราชการ/วันปิดพิเศษที่ระบุไว้ในระบบ
- 30/07/2026 (วันพฤหัสบดี): วันหยุดราชการ - ศูนย์ปิดให้บริการตามวันหยุดราชการ/วันปิดพิเศษที่ระบุไว้ในระบบ
วันที่อ้างอิงของระบบ: วันนี้คือ 06/07/2026 (วันจันทร์) ตามเวลาไทย
หมายเหตุ: วันหยุดไทย/เทศกาลเป็นข้อมูลปฏิทินประกอบ ส่วนการปิดบริการจริงให้ดู service_closures.jsonl
แหล่งข้อมูลปฏิทินไทย: https://www.timeanddate.com/holidays/thailand/2026
แหล่งข้อมูลตารางบริการ: https://esports.computing.psu.ac.th/reservation

แหล่งข้อมูล:
- Reservation | https://esports.computing.psu.ac.th/reservation

### 7. 29 กรกฎาคม 2026 เป็นวันหยุดอะไร

- mode: `pipeline:rag_direct_curated`
- route: `events_news/news_lookup`
- confidence: `0.84`
- elapsed: `0.0118` sec

คำตอบ:

PSU Phuket VALORANT 2026 Tournament จัดขึ้นเมื่อวันที่ 21 กุมภาพันธ์ 2569 โดยเป็นการแข่งขันเกม VALORANT ณ PSU Esports Studio - Phuket
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

แหล่งข้อมูล:
- curated_news_valorant_2026 | https://esports.phuket.psu.ac.th/events-news/news
- curated_news_cs2_2026 | https://esports.phuket.psu.ac.th/events-news/news
- curated_news_chinese_students_game_based_learning | https://esports.phuket.psu.ac.th/events-news/news

### 8. 28 กรกฎาคม 2026 เปิดไหม

- mode: `pipeline:calendar_closure_fast_path`
- route: `schedule/schedule_query`
- confidence: `0.99`
- elapsed: `0.0124` sec

คำตอบ:

วันที่ 28/07/2026 (วันอังคาร): ศูนย์ปิดให้บริการ (วันหยุดราชการ)
ศูนย์ปิดให้บริการตามวันหยุดราชการ/วันปิดพิเศษที่ระบุไว้ในระบบ
วันที่อ้างอิงของระบบ: วันนี้คือ 06/07/2026 (วันจันทร์) ตามเวลาไทย
หมายเหตุ: วันปิดพิเศษ/วันหยุดราชการจะ override ตารางเปิดปิดปกติ
แหล่งข้อมูลตารางบริการ: https://esports.computing.psu.ac.th/reservation
แหล่งข้อมูลวันปิด: manual_admin_config

แหล่งข้อมูล:
- Reservation | https://esports.computing.psu.ac.th/reservation

### 9. พรุ่งนี้เปิดไหม

- mode: `pipeline:calendar_schedule_fast_path`
- route: `schedule/schedule_query`
- confidence: `0.98`
- elapsed: `0.005` sec

คำตอบ:

พรุ่งนี้ 07/07/2026 (วันอังคาร): วันอังคารเปิดให้เล่น 09:00-12:00 และ 13:00-16:00
วันที่อ้างอิงของระบบ: วันนี้คือ 06/07/2026 (วันจันทร์) ตามเวลาไทย

ปฏิทินไทยของวันที่นี้:
ไม่พบวันหยุดไทยหรือเทศกาลในปฏิทินที่บันทึกไว้สำหรับวันนี้

รายละเอียดจากตาราง:
- วันจันทร์ช่วงเช้า 09:00-12:00 เป็น Maintenance* และเปิดช่วงบ่าย 13:00-16:00
- วันอังคาร-พฤหัสบดีเปิด 09:00-12:00 และ 13:00-16:00
- วันศุกร์เปิดช่วงเช้า 09:00-12:00 และช่วงบ่าย 13:00-16:00 เป็น Maintenance
- วันหยุดราชการ/วันปิดพิเศษในไฟล์ปฏิทินจะมีผลก่อนตารางปกติ
แหล่งข้อมูลตารางบริการ: https://esports.computing.psu.ac.th/reservation

แหล่งข้อมูล:
- Reservation | https://esports.computing.psu.ac.th/reservation

### 10. ตอนนี้รายการแข่งมเกมอะไรบ้าง

- mode: `pipeline:competition_game_list_fast_path`
- route: `games/competition_game_list`
- confidence: `0.95`
- elapsed: `0.006` sec

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

### 11. ตอนนี้อยากเล่น Tekken 8

- mode: `pipeline:games_availability_fast_path`
- route: `games/game_availability_lookup`
- confidence: `0.95`
- elapsed: `0.0115` sec

คำตอบ:

เล่น TEKKEN 8 ได้ครับ
มีให้เล่นที่: PC Zone และ PlayStation 5 Zone
แนะนำให้จองโซนที่ต้องการก่อนเข้าใช้บริการ และถ้าไม่แน่ใจเรื่องเครื่องหรือรอบเวลาให้สอบถามเจ้าหน้าที่ก่อนจองครับ
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

แหล่งข้อมูล:
- our_games | https://esports.phuket.psu.ac.th/Services/our-games
- Reservation | https://esports.computing.psu.ac.th/reservation
