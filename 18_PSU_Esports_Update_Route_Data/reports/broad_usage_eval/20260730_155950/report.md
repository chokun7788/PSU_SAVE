# Broad Usage Eval v1

- Generated at: 2026-07-30T16:02:11
- Cases: 667
- Turn checks: 679
- Passed: 573
- Failed: 106
- Pass rate: 0.8439
- Total wall sec: 140.77
- Allow LLM: False
- RAG fallback: False

## By Group
- ambiguity_no_answer: 18/25 pass, 7 fail
- competition_rules: 69/75 pass, 6 fail
- compound: 12/15 pass, 3 fail
- equipment: 36/58 pass, 22 fail
- game_controls: 153/159 pass, 6 fail
- games: 154/158 pass, 4 fail
- members: 0/47 pass, 47 fail
- reservation: 15/20 pass, 5 fail
- schedule: 8/10 pass, 2 fail
- service_fee: 85/88 pass, 3 fail
- session_followup: 23/24 pass, 1 fail

## By Strategy
- clarification: 19
- compound: 15
- fast/rule: 137
- llm: 9
- rag/retrieval: 40
- structured: 459

## Common Problems
- route_category expected ['members'], got overview: 45
- route_category expected ['equipment'], got general: 10
- route_category expected ['equipment'], got games: 9
- missing any of ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']: 6
- missing any of ['Gaming', 'PC']: 6
- mode expected prefix ['pipeline: 6
- missing any of ['จอง', 'เช็คอิน', 'ชำระ', 'session', 'ยกเลิก']: 4
- missing any of ['ยังไม่พบ', 'ไม่มี', 'ไม่ได้อยู่', 'ตอบจากข้อมูล']: 4
- route_category expected ['clarification', 'games', 'equipment', 'service_fee', 'reservation', 'no_answer'], got general: 3
- route_category expected ['equipment'], got knowledge: 3
- missing any of ['บาท', 'ต่างกัน', 'ฟรี', '0 บาท']: 2
- missing any of ['เปิด', 'ปิด', 'เวลา', 'วัน', 'ไม่เปิด']: 2
- route_category expected ['games'], got multi_question: 2
- route_category expected ['games'], got schedule: 2
- route_category expected ['multi_question'], got games: 2
- route_category expected ['reservation'], got clarification: 2
- route_category expected ['reservation'], got general: 2
- route_category expected ['schedule', 'reservation'], got general: 2
- missing 'God of War Ragnarök': 1
- missing 'Nintendo Switch Sports': 1
- missing 'PC': 1
- missing 'Resident Evil 4 (Remake)': 1
- missing 'Super Smash Bros. Ultimate': 1
- missing any of ['Cockpit', 'Zone']: 1
- missing any of ['Driving', 'Cockpit']: 1
- missing any of ['Driving', 'ใช้', 'Zone']: 1
- missing any of ['L3 (Click Left Stick)', 'มาร์กตำแหน่งศัตรู']: 1
- missing any of ['Members', 'สมาชิก', 'คน', 'หมวด']: 1
- missing any of ['PC', 'เล่นได้ที่']: 1
- missing any of ['Pulse', 'Cockpit']: 1
- missing any of ['Sofa', 'Nintendo Switch']: 1
- missing any of ['TV', 'Cockpit']: 1
- missing any of ['TV', 'Nintendo Switch']: 1
- missing any of ['กรรมการ', 'นางสาวชญาภา']: 1
- missing any of ['คำถามที่', 'ราคา', 'ปุ่ม', 'Zone', 'จอง']: 1
- missing any of ['เกม', 'Zone', 'TEKKEN', 'Mario', 'Gran Turismo']: 1
- route_category expected ['games'], got clarification: 1
- route_category expected ['games'], got equipment: 1
- route_category expected ['games'], got overview: 1
- route_category expected ['members'], got clarification: 1
- route_category expected ['members'], got general: 1
- route_category expected ['multi_question'], got overview: 1
- route_category expected ['no_answer', 'games', 'general'], got events_news: 1
- route_category expected ['no_answer', 'games', 'general'], got knowledge: 1
- route_category expected ['no_answer', 'games', 'general'], got overview: 1
- route_category expected ['reservation'], got multi_question: 1
- route_category expected ['service_fee'], got equipment: 1
- route_category expected ['service_fee'], got overview: 1

## Top Failures

### SF-053 service_fee
- Question: VR 30 นาทีกับ VR 1 ชั่วโมงต่างกันยังไง
- Resolved: -
- Mode: `pipeline:structured_equipment_catalog`
- Route: `equipment/list`
- Problems: route_category expected ['service_fee'], got equipment, missing any of ['บาท', 'ต่างกัน', 'ฟรี', '0 บาท']
- Answer: อุปกรณ์ใน VR Zone: PlayStation 5 Zone / VR Zone •    PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive (2 Units in PlayStation 5 Zone and 1 Unit in VR Zone) VR Zone •    Sony PlayStation VR2 (1 Unit) แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### SF-058 service_fee
- Question: PSU Staff เล่น PC ต้องเสียเงินไหม
- Resolved: -
- Mode: `pipeline:structured_members_game_relation_no_data`
- Route: `overview/members_lookup`
- Problems: route_category expected ['service_fee'], got overview, missing any of ['บาท', 'ต่างกัน', 'ฟรี', '0 บาท']
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ว่าสมาชิกหรือสตาฟแต่ละคนเล่นเกม/ดูแลเกมหรือโซนไหนครับ ข้อมูลที่มีตอนนี้ยืนยันได้เฉพาะรายชื่อสมาชิก หมวด และตำแหน่งในหน้า Members แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### SF-083 service_fee
- Question: Nintendo Switch Sports ราคาเท่าไหร่
- Resolved: -
- Mode: `pipeline:deterministic_calculator_fast`
- Route: `service_fee/service_fee_query`
- Problems: missing 'Nintendo Switch Sports'
- Answer: Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง) •    PSU Student and Staff: 0 บาท •    PSU Alumni and General Student: 50 บาท •    General Adult: 140 บาท  Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง) •    PSU Student and Staff: 0 บาท •    PSU Alumni and General Stude...

### G-010 games
- Question: PUBG: BATTLEGROUNDS เล่นได้ที่ไหน
- Resolved: -
- Mode: `pipeline:schedule_fast_path`
- Route: `schedule/schedule_query`
- Problems: route_category expected ['games'], got schedule, missing any of ['PC', 'เล่นได้ที่']
- Answer: เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน  รายละเอียดจากตาราง: •    Morning คือ 09:00-12:00 •    Afternoon คือ 13:00-16:00 •    Monday ช่วง Morning 09:00-12:00 เป็น Maintenance* •    Monday ช่วง After...

### G-153 games
- Question: เกมไหนเล่นได้หลายโซน
- Resolved: -
- Mode: `pipeline:schedule_fast_path`
- Route: `schedule/schedule_query`
- Problems: route_category expected ['games'], got schedule, missing any of ['เกม', 'Zone', 'TEKKEN', 'Mario', 'Gran Turismo']
- Answer: เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน  รายละเอียดจากตาราง: •    Morning คือ 09:00-12:00 •    Afternoon คือ 13:00-16:00 •    Monday ช่วง Morning 09:00-12:00 เป็น Maintenance* •    Monday ช่วง After...

### G-155 games
- Question: เกมยิงมีอะไรบ้าง
- Resolved: -
- Mode: `pipeline:structured_equipment_catalog`
- Route: `equipment/list`
- Problems: route_category expected ['games'], got equipment
- Answer: อุปกรณ์บนหน้า Home: PC Zone •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง) •    Gaming Monitor (จำนวน 10 จอ) •    Gaming Chair (จำนวน 10 ตัว) •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset  Cockpit Zone •    TV ขนาด 65 นิ้ว (จำนวน 2...

### G-158 games
- Question: Tekken 8 มีในเครื่องไหน
- Resolved: -
- Mode: `pipeline:ambiguity_clarification`
- Route: `clarification/ambiguity_gate_clarification`
- Problems: route_category expected ['games'], got clarification
- Answer: คำถามนี้มีได้หลายความหมายครับ ขอระบุเพิ่มนิดหนึ่งว่าต้องการถามเรื่องไหน: อุปกรณ์, รายชื่อเกม/ข้อมูลเกม

### GC-033 game_controls
- Question: God of War Ragnarök ปุ่มทั้งหมดมีอะไรบ้าง
- Resolved: -
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Problems: missing 'God of War Ragnarök'
- Answer: God of War Ragnarok มีข้อมูลปุ่มควบคุมดังนี้: PlayStation / PS5 •    L: เคลื่อนที่ - บังคับทิศทางการเดิน •    L3: วิ่งสปรินต์ - กดเพื่อวิ่ง •    L3 + R3: พลังสปาร์ตัน - ระเบิดความโกรธของเครโทสเพื่อเพิ่มพลังโจมตีและฟื้นฟูพลังชีวิต •    R: มุมกล้อง - ควบคุมการหม...

### GC-075 game_controls
- Question: Mario Party Superstars ปุ่มเล่นบอร์ดและมินิเกมด้วยปุ่มกดอะไร
- Resolved: -
- Mode: `pipeline:multi_question_splitter`
- Route: `multi_question/multi_question_split`
- Problems: route_category expected ['games'], got multi_question, mode expected prefix ['pipeline:structured_game_controls'], got pipeline:multi_question_splitter
- Answer: คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:  •    Mario Party Superstars ปุ่มเล่นบอร์ด กดอะไร Mario Party Superstars มีข้อมูลปุ่มควบคุมดังนี้: Nintendo Switch •    Button controls: เล่นบอร์ดและมินิเกมด้วยปุ่ม - แหล่งทางการยืนยันว่า 100 มินิเกมรองรับ button control...

### GC-096 game_controls
- Question: New Super Mario Bros. U Deluxe ปุ่มวิ่ง กระโดด และเหยียบศัตรูกดอะไร
- Resolved: -
- Mode: `pipeline:multi_question_splitter`
- Route: `multi_question/multi_question_split`
- Problems: route_category expected ['games'], got multi_question, mode expected prefix ['pipeline:structured_game_controls'], got pipeline:multi_question_splitter
- Answer: คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:  •    New Super Mario Bros. U Deluxe ปุ่มวิ่ง กระโดด กดอะไร New Super Mario Bros. U Deluxe ปุ่มที่ตรงกับคำถาม: Nintendo Switch •    Simple controls: วิ่ง กระโดด และเหยียบศัตรู - หน้า Nintendo อธิบายการเล่นเป็นเกม 2D side...

### GC-109 game_controls
- Question: Resident Evil 4 (Remake) ปุ่มทั้งหมดมีอะไรบ้าง
- Resolved: -
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Problems: missing 'Resident Evil 4 (Remake)'
- Answer: Resident Evil 4 มีข้อมูลปุ่มควบคุมดังนี้: PlayStation / PS5 •    L (Left Stick): เคลื่อนที่ •    L3: วิ่งสปรินต์ •    R (Right Stick): มุมกล้อง •    L2 (Hold): เล็ง •    L1: ปัดป้อง •    R1: วิ่ง / กลับหลังหัน •    R2: ยิง / โจมตีด้วยมีด •    Triangle: คลังไอเ...

### GC-125 game_controls
- Question: Super Smash Bros. Ultimate ปุ่มทั้งหมดมีอะไรบ้าง
- Resolved: -
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Problems: missing 'Super Smash Bros. Ultimate'
- Answer: Super Smash Bros Ultimate มีข้อมูลปุ่มควบคุมดังนี้: Nintendo Switch •    L (Left Stick): เคลื่อนที่ - ใช้เดิน วิ่ง หรือย่อตัว รวมถึงกำหนดทิศทางการโจมตีท่าต่าง ๆ •    R (Right Stick): โจมตีสแมช - ก้านอนาล็อกขวาใช้สำหรับปล่อยท่า Smash Attack ไปตามทิศทางที่ดันอย่...

### GC-148 game_controls
- Question: Uncharted: Legacy of Thieves Collection ปุ่มมาร์กตำแหน่งศัตรูกดอะไร
- Resolved: -
- Mode: `pipeline:structured_members_group_list`
- Route: `overview/list`
- Problems: route_category expected ['games'], got overview, mode expected prefix ['pipeline:structured_game_controls'], got pipeline:structured_members_group_list, missing any of ['L3 (Click Left Stick)', 'มาร์กตำแหน่งศัตรู']
- Answer: สมาชิกจากหน้า Members แยกตามหมวด รวม 25 คน: Members (7 คน): •    ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี •    รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี •    รศ.ดร.อซีส นันทอมรพงศ์: คณบดี •    ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ •    นายพฤทธิ์ เกษตรสมบูรณ์:...

### E-011 equipment
- Question: Gaming PC รุ่น MSI MAG Infinite S3 14th คืออะไร
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Problems: route_category expected ['equipment'], got general, missing any of ['Gaming', 'PC']
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### E-012 equipment
- Question: Gaming PC รุ่น MSI MAG Infinite S3 14th อยู่โซนไหน
- Resolved: -
- Mode: `pipeline:equipment_item_location_fast_path`
- Route: `games/game_availability_lookup`
- Problems: route_category expected ['equipment'], got games
- Answer: Gaming PC รุ่น MSI MAG Infinite S3 14th อยู่ที่ PC Zone ครับ •    รายละเอียด: หน้า Home ระบุ Gaming PC 10 Units; สเปกที่บันทึกไว้ในโปรเจกต์: Intel Core i5-14400, RAM DDR5 32GB, NVIDIA GeForce RTX 5060 8GB แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### E-014 equipment
- Question: Gaming Monitor คืออะไร
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Problems: route_category expected ['equipment'], got general, missing any of ['Gaming', 'PC']
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### E-015 equipment
- Question: Gaming Monitor อยู่โซนไหน
- Resolved: -
- Mode: `pipeline:equipment_item_location_fast_path`
- Route: `games/game_availability_lookup`
- Problems: route_category expected ['equipment'], got games
- Answer: Gaming Monitor อยู่ที่ PC Zone ครับ •    รายละเอียด: หน้า Home ระบุว่ามี Gaming Monitor 10 เครื่อง แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### E-017 equipment
- Question: Gaming Keyboard คืออะไร
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Problems: route_category expected ['equipment'], got general, missing any of ['Gaming', 'PC']
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### E-018 equipment
- Question: Gaming Keyboard อยู่โซนไหน
- Resolved: -
- Mode: `pipeline:equipment_item_location_fast_path`
- Route: `games/game_availability_lookup`
- Problems: route_category expected ['equipment'], got games
- Answer: Gaming Keyboard อยู่ที่ PC Zone ครับ •    รายละเอียด: อยู่ในรายการอุปกรณ์ PC Zone บนหน้า Home แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### E-020 equipment
- Question: Gaming Mouse คืออะไร
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Problems: route_category expected ['equipment'], got general, missing any of ['Gaming', 'PC']
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### E-021 equipment
- Question: Gaming Mouse อยู่โซนไหน
- Resolved: -
- Mode: `pipeline:equipment_item_location_fast_path`
- Route: `games/game_availability_lookup`
- Problems: route_category expected ['equipment'], got games
- Answer: Gaming Mouse อยู่ที่ PC Zone ครับ •    รายละเอียด: อยู่ในรายการอุปกรณ์ PC Zone บนหน้า Home แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### E-023 equipment
- Question: Gaming Headset คืออะไร
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Problems: route_category expected ['equipment'], got general, missing any of ['Gaming', 'PC']
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### E-024 equipment
- Question: Gaming Headset อยู่โซนไหน
- Resolved: -
- Mode: `pipeline:equipment_item_location_fast_path`
- Route: `games/game_availability_lookup`
- Problems: route_category expected ['equipment'], got games
- Answer: Gaming Headset อยู่ที่ PC Zone ครับ •    รายละเอียด: อยู่ในรายการอุปกรณ์ PC Zone บนหน้า Home แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### E-026 equipment
- Question: Gaming Chair คืออะไร
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Problems: route_category expected ['equipment'], got general, missing any of ['Gaming', 'PC']
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### E-027 equipment
- Question: Gaming Chair อยู่โซนไหน
- Resolved: -
- Mode: `pipeline:equipment_item_location_fast_path`
- Route: `games/game_availability_lookup`
- Problems: route_category expected ['equipment'], got games
- Answer: Gaming Chair อยู่ที่ PC Zone ครับ •    รายละเอียด: หน้า Home ระบุว่ามี Gaming Chair 10 ตัว แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### E-032 equipment
- Question: Driving Force Shifter คืออะไร
- Resolved: -
- Mode: `pipeline:chatbot_greeting_fast_path`
- Route: `knowledge/detail`
- Problems: route_category expected ['equipment'], got knowledge, missing any of ['Driving', 'Cockpit']
- Answer: สวัสดีครับ ผมคือ PSU Esports Assistant ผู้ช่วยของ PSU Esports Studio - Phuket ถามเรื่องเกม อุปกรณ์ วิธีจอง เวลาเปิด-ปิด ค่าบริการ ปุ่มควบคุม กติกา หรือสมาชิกทีมได้เลยครับ แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### E-033 equipment
- Question: Driving Force Shifter อยู่โซนไหน
- Resolved: -
- Mode: `pipeline:chatbot_greeting_fast_path`
- Route: `knowledge/detail`
- Problems: route_category expected ['equipment'], got knowledge, missing any of ['Cockpit', 'Zone']
- Answer: สวัสดีครับ ผมคือ PSU Esports Assistant ผู้ช่วยของ PSU Esports Studio - Phuket ถามเรื่องเกม อุปกรณ์ วิธีจอง เวลาเปิด-ปิด ค่าบริการ ปุ่มควบคุม กติกา หรือสมาชิกทีมได้เลยครับ แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### E-034 equipment
- Question: Driving Force Shifter ใช้ทำอะไร
- Resolved: -
- Mode: `pipeline:chatbot_greeting_fast_path`
- Route: `knowledge/detail`
- Problems: route_category expected ['equipment'], got knowledge, missing any of ['Driving', 'ใช้', 'Zone']
- Answer: สวัสดีครับ ผมคือ PSU Esports Assistant ผู้ช่วยของ PSU Esports Studio - Phuket ถามเรื่องเกม อุปกรณ์ วิธีจอง เวลาเปิด-ปิด ค่าบริการ ปุ่มควบคุม กติกา หรือสมาชิกทีมได้เลยครับ แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### E-038 equipment
- Question: Pulse Elite Wireless Headset คืออะไร
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Problems: route_category expected ['equipment'], got general, missing any of ['Pulse', 'Cockpit']
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### E-041 equipment
- Question: Nintendo Switch OLED คืออะไร
- Resolved: -
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_detail_lookup`
- Problems: route_category expected ['equipment'], got games
- Answer: Nintendo Switch Sports: Nintendo Switch Sports คือเกมกีฬาที่ใช้การขยับ Joy-Con จำลองการเล่นกีฬาหลายประเภท แนวเกม: เกมกีฬา Motion Control วิธีเล่นโดยสรุป: ถือ Joy-Con แล้วขยับตามกีฬาที่เลือก เช่น ตี โยน หรือแกว่งตามท่าทางในเกม เล่นได้ที่: Nintendo Switch Zone แ...

### E-042 equipment
- Question: Nintendo Switch OLED อยู่โซนไหน
- Resolved: -
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_detail_lookup`
- Problems: route_category expected ['equipment'], got games
- Answer: Nintendo Switch Sports: Nintendo Switch Sports คือเกมกีฬาที่ใช้การขยับ Joy-Con จำลองการเล่นกีฬาหลายประเภท แนวเกม: เกมกีฬา Motion Control วิธีเล่นโดยสรุป: ถือ Joy-Con แล้วขยับตามกีฬาที่เลือก เช่น ตี โยน หรือแกว่งตามท่าทางในเกม เล่นได้ที่: Nintendo Switch Zone แ...

### E-050 equipment
- Question: TV 65 นิ้ว คืออะไร
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Problems: route_category expected ['equipment'], got general, missing any of ['TV', 'Cockpit']
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### E-053 equipment
- Question: TV 86 นิ้ว คืออะไร
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Problems: route_category expected ['equipment'], got general, missing any of ['TV', 'Nintendo Switch']
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### E-056 equipment
- Question: Sofa 2 seats คืออะไร
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Problems: route_category expected ['equipment'], got general, missing any of ['Sofa', 'Nintendo Switch']
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### E-057 equipment
- Question: Sofa 2 seats อยู่โซนไหน
- Resolved: -
- Mode: `pipeline:equipment_item_location_fast_path`
- Route: `games/game_availability_lookup`
- Problems: route_category expected ['equipment'], got games
- Answer: Sofa 2 seats อยู่ที่ Nintendo Switch Zone ครับ •    รายละเอียด: หน้า Home ระบุว่ามี Sofa 2 seats 2 ชุด แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### R-010 reservation
- Question: หลังจองต้องจ่ายภายในกี่นาที
- Resolved: -
- Mode: `pipeline:ambiguity_clarification`
- Route: `clarification/ambiguity_gate_clarification`
- Problems: route_category expected ['reservation'], got clarification, missing any of ['จอง', 'เช็คอิน', 'ชำระ', 'session', 'ยกเลิก']
- Answer: ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`

### R-015 reservation
- Question: ถ้าไปช้าจะเป็นอะไรไหม
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/unknown_domain_query`
- Problems: route_category expected ['reservation'], got general, missing any of ['จอง', 'เช็คอิน', 'ชำระ', 'session', 'ยกเลิก']
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### R-016 reservation
- Question: walk in ได้ไหม
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Problems: route_category expected ['reservation'], got general, missing any of ['จอง', 'เช็คอิน', 'ชำระ', 'session', 'ยกเลิก']
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### R-018 reservation
- Question: จองแล้วไม่สามารถยกเลิกได้ใช่ไหม
- Resolved: -
- Mode: `pipeline:multi_question_splitter`
- Route: `multi_question/multi_question_split`
- Problems: route_category expected ['reservation'], got multi_question
- Answer: คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:  •    จอง ผู้ใช้งานต้องจองล่วงหน้าผ่านระบบออนไลน์ก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แหล่งข้อมูล: https://esports.computing.psu.ac.th/  •    ไม่สามารถยกเลิกได้ใช่ไหม เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต...

### R-020 reservation
- Question: จ่ายเงินผ่านช่องทางไหน
- Resolved: -
- Mode: `pipeline:ambiguity_clarification`
- Route: `clarification/ambiguity_gate_clarification`
- Problems: route_category expected ['reservation'], got clarification, missing any of ['จอง', 'เช็คอิน', 'ชำระ', 'session', 'ยกเลิก']
- Answer: ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`

### S-006 schedule
- Question: ช่วงเช้าเล่นได้ไหม
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Problems: route_category expected ['schedule', 'reservation'], got general, missing any of ['เปิด', 'ปิด', 'เวลา', 'วัน', 'ไม่เปิด']
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### S-010 schedule
- Question: ตารางเวลาให้บริการเป็นยังไง
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/unknown_domain_query`
- Problems: route_category expected ['schedule', 'reservation'], got general, missing any of ['เปิด', 'ปิด', 'เวลา', 'วัน', 'ไม่เปิด']
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### M-001 members
- Question: สมาชิกมีใครบ้าง
- Resolved: -
- Mode: `pipeline:structured_members_group_list`
- Route: `overview/list`
- Problems: route_category expected ['members'], got overview
- Answer: สมาชิกจากหน้า Members แยกตามหมวด รวม 25 คน: Members (7 คน): •    ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี •    รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี •    รศ.ดร.อซีส นันทอมรพงศ์: คณบดี •    ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ •    นายพฤทธิ์ เกษตรสมบูรณ์:...

### M-002 members
- Question: สมาชิก PSU Esports มีกี่คน
- Resolved: -
- Mode: `pipeline:structured_members_group_count`
- Route: `overview/group_count`
- Problems: route_category expected ['members'], got overview
- Answer: สมาชิกในหน้า Members แบ่งเป็น 3 หมวดครับ •    Members: 7 คน •    cooperative education and Internship student: 5 คน •    PSU Phuket Esports Club - PSU Phuket: 13 คน รวมทั้งหมด 25 คน แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### M-003 members
- Question: สมาชิกแบ่งเป็นกี่หมวด
- Resolved: -
- Mode: `pipeline:structured_members_group_count`
- Route: `overview/group_count`
- Problems: route_category expected ['members'], got overview
- Answer: สมาชิกในหน้า Members แบ่งเป็น 3 หมวดครับ •    Members: 7 คน •    cooperative education and Internship student: 5 คน •    PSU Phuket Esports Club - PSU Phuket: 13 คน รวมทั้งหมด 25 คน แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### M-004 members
- Question: แต่ละหมวดมีใครบ้าง
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/unknown_domain_query`
- Problems: route_category expected ['members'], got general, missing any of ['Members', 'สมาชิก', 'คน', 'หมวด']
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### M-005 members
- Question: cooperative education มีใครบ้าง
- Resolved: -
- Mode: `pipeline:structured_members_group_list`
- Route: `overview/list`
- Problems: route_category expected ['members'], got overview
- Answer: สมาชิกในหมวด cooperative education and Internship student: cooperative education and Internship student (5 คน): •    นายณภัทร เชื้อเหล่าวานิช: นักศึกษาสหกิจ Game and 3D Developer (วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต; ระยะเวลา: 6/1/20...

### M-006 members
- Question: PSU Phuket Esports Club มีใครบ้าง
- Resolved: -
- Mode: `pipeline:structured_members_group_list`
- Route: `overview/list`
- Problems: route_category expected ['members'], got overview
- Answer: สมาชิกในหมวด PSU Phuket Esports Club - PSU Phuket: PSU Phuket Esports Club - PSU Phuket (13 คน): •    นายษุภากรณ์ จิราจินดากุล: ประธาน •    นายนพัทธ์ ฝอยทอง: รองประธาน •    นายปัณณวิชญ์ หนูเรือง: เลขานุการ •    นายภูจิตร จิรวิริยาภรณ์: เหรัญญิก •    นายธนชาติ...

### M-007 members
- Question: ผศ.ดร.นิวัติ แก้วประดับ ทำตำแหน่งอะไร
- Resolved: -
- Mode: `pipeline:structured_members_person_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี หมวด: Members สังกัด/รายละเอียด: มหาวิทยาลัยสงขลานครินทร์ แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### M-008 members
- Question: ใครเป็นอธิการบดี
- Resolved: -
- Mode: `pipeline:structured_members_role_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: ตำแหน่ง อธิการบดี มี 1 คนครับ •    ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี (มหาวิทยาลัยสงขลานครินทร์)   ◦    หมวด: Members แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### M-009 members
- Question: รศ.ดร.พันธ์ ทองชุมนุม ทำตำแหน่งอะไร
- Resolved: -
- Mode: `pipeline:structured_members_person_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี หมวด: Members สังกัด/รายละเอียด: มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### M-010 members
- Question: ใครเป็นรองอธิการบดี
- Resolved: -
- Mode: `pipeline:structured_members_role_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: ตำแหน่ง รองอธิการบดี มี 1 คนครับ •    รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี (มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต)   ◦    หมวด: Members แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### M-011 members
- Question: รศ.ดร.อซีส นันทอมรพงศ์ ทำตำแหน่งอะไร
- Resolved: -
- Mode: `pipeline:structured_members_person_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: รศ.ดร.อซีส นันทอมรพงศ์: คณบดี หมวด: Members สังกัด/รายละเอียด: วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### M-012 members
- Question: ใครเป็นคณบดี
- Resolved: -
- Mode: `pipeline:structured_members_role_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: ตำแหน่ง คณบดี มี 1 คนครับ •    รศ.ดร.อซีส นันทอมรพงศ์: คณบดี (วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต)   ◦    หมวด: Members แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### M-013 members
- Question: ผศ.ดร.ณัฐพงศ์ ทองเทพ ทำตำแหน่งอะไร
- Resolved: -
- Mode: `pipeline:structured_members_person_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ หมวด: Members สังกัด/รายละเอียด: มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### M-014 members
- Question: ใครเป็นผู้ช่วยอธิการบดีฝ่ายวิชาการ
- Resolved: -
- Mode: `pipeline:structured_members_role_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: ตำแหน่ง ผู้ช่วยอธิการบดีฝ่ายวิชาการ มี 1 คนครับ •    ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ (มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต)   ◦    หมวด: Members แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### M-015 members
- Question: นายพฤทธิ์ เกษตรสมบูรณ์ ทำตำแหน่งอะไร
- Resolved: -
- Mode: `pipeline:structured_members_person_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: นายพฤทธิ์ เกษตรสมบูรณ์: นักวิชาการคอมพิวเตอร์ หมวด: Members สังกัด/รายละเอียด: วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### M-016 members
- Question: ใครเป็นนักวิชาการคอมพิวเตอร์
- Resolved: -
- Mode: `pipeline:structured_members_role_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: ตำแหน่ง นักวิชาการคอมพิวเตอร์ มี 2 คนครับ •    นายพฤทธิ์ เกษตรสมบูรณ์: นักวิชาการคอมพิวเตอร์ (วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต)   ◦    หมวด: Members •    นายณัฐวัฒน์ นิธิคุณานนต์: นักวิชาการคอมพิวเตอร์ (วิทยาลัยการคอมพิวเตอร์ มหาว...

### M-017 members
- Question: นายณัฐวัฒน์ นิธิคุณานนต์ ทำตำแหน่งอะไร
- Resolved: -
- Mode: `pipeline:structured_members_person_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: นายณัฐวัฒน์ นิธิคุณานนต์: นักวิชาการคอมพิวเตอร์ หมวด: Members สังกัด/รายละเอียด: วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### M-018 members
- Question: นายชนะชัย สิริพันธ์วราภรณ์ ทำตำแหน่งอะไร
- Resolved: -
- Mode: `pipeline:structured_members_person_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: นายชนะชัย สิริพันธ์วราภรณ์: ผู้จัดการ หมวด: Members สังกัด/รายละเอียด: PSU Esports Studio - Phuket วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### M-019 members
- Question: ใครเป็นผู้จัดการ
- Resolved: -
- Mode: `pipeline:structured_members_role_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: ตำแหน่ง ผู้จัดการ มี 1 คนครับ •    นายชนะชัย สิริพันธ์วราภรณ์: ผู้จัดการ (PSU Esports Studio - Phuket วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต)   ◦    หมวด: Members แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### M-020 members
- Question: นายณภัทร เชื้อเหล่าวานิช ทำตำแหน่งอะไร
- Resolved: -
- Mode: `pipeline:structured_members_person_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: นายณภัทร เชื้อเหล่าวานิช: นักศึกษาสหกิจ Game and 3D Developer หมวด: cooperative education and Internship student สังกัด/รายละเอียด: วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต ระยะเวลา: 6/1/2025 - 30/4/2025 แหล่งข้อมูล: https://esports.phuke...

### M-021 members
- Question: ใครเป็นนักศึกษาสหกิจ Game and 3D Developer
- Resolved: -
- Mode: `pipeline:structured_members_role_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: ตำแหน่ง นักศึกษาสหกิจ Game and 3D Developer มี 1 คนครับ •    นายณภัทร เชื้อเหล่าวานิช: นักศึกษาสหกิจ Game and 3D Developer (วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต; ระยะเวลา: 6/1/2025 - 30/4/2025)   ◦    หมวด: cooperative education and I...

### M-022 members
- Question: Mr. Amine Abidellaoui ทำตำแหน่งอะไร
- Resolved: -
- Mode: `pipeline:structured_members_person_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: Mr. Amine Abidellaoui: Internship Student หมวด: cooperative education and Internship student สังกัด/รายละเอียด: High School Bristol Cannes, France ระยะเวลา: 10/11/2025 - 19/12/2025 แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### M-023 members
- Question: ใครเป็นInternship Student
- Resolved: -
- Mode: `pipeline:structured_members_role_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: ตำแหน่ง Internship Student มี 2 คนครับ •    Mr. Amine Abidellaoui: Internship Student (High School Bristol Cannes, France; ระยะเวลา: 10/11/2025 - 19/12/2025)   ◦    หมวด: cooperative education and Internship student •    Mr. Yanis Igoudjil: Internship Student...

### M-024 members
- Question: นายสุพศิน อะนะฝรั่ง ทำตำแหน่งอะไร
- Resolved: -
- Mode: `pipeline:structured_members_person_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: นายสุพศิน อะนะฝรั่ง: นักศึกษาสหกิจ Web & AI Developer หมวด: cooperative education and Internship student สังกัด/รายละเอียด: วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต ระยะเวลา: 12/1/2026 - 8/5/2026 แหล่งข้อมูล: https://esports.phuket.psu.ac...

### M-025 members
- Question: ใครเป็นนักศึกษาสหกิจ Web & AI Developer
- Resolved: -
- Mode: `pipeline:structured_members_role_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: ตำแหน่ง นักศึกษาสหกิจ Web & AI Developer มี 1 คนครับ •    นายสุพศิน อะนะฝรั่ง: นักศึกษาสหกิจ Web & AI Developer (วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต; ระยะเวลา: 12/1/2026 - 8/5/2026)   ◦    หมวด: cooperative education and Internship s...

### M-026 members
- Question: Mr. Yanis Igoudjil ทำตำแหน่งอะไร
- Resolved: -
- Mode: `pipeline:structured_members_person_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: Mr. Yanis Igoudjil: Internship Student หมวด: cooperative education and Internship student สังกัด/รายละเอียด: Industrial Engineering and Information Systems, EPF Graduate School of Engineering, Cachan Val-De-Marne, France ระยะเวลา: 29/06/2026 - 18/09/2026 แหล่ง...

### M-027 members
- Question: นายภาสวุฒิ ชูติประชากิจ ทำตำแหน่งอะไร
- Resolved: -
- Mode: `pipeline:structured_members_person_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: นายภาสวุฒิ ชูติประชากิจ: นักศึกษาฝึกงานโครงการ Super AI SS6 ตำแหน่ง AI Chat Bot Developer หมวด: cooperative education and Internship student สังกัด/รายละเอียด: วิศวกรรมระบบไอโอทีและสารสนเทศ สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง ระยะเวลา: 07/2026 - 08/...

### M-028 members
- Question: ใครเป็นนักศึกษาฝึกงานโครงการ Super AI SS6 ตำแหน่ง AI Chat Bot Developer
- Resolved: -
- Mode: `pipeline:structured_members_role_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: ตำแหน่ง นักศึกษาฝึกงานโครงการ Super AI SS6 ตำแหน่ง AI Chat Bot Developer มี 1 คนครับ •    นายภาสวุฒิ ชูติประชากิจ: นักศึกษาฝึกงานโครงการ Super AI SS6 ตำแหน่ง AI Chat Bot Developer (วิศวกรรมระบบไอโอทีและสารสนเทศ สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง; ร...

### M-029 members
- Question: นายษุภากรณ์ จิราจินดากุล ทำตำแหน่งอะไร
- Resolved: -
- Mode: `pipeline:structured_members_person_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: นายษุภากรณ์ จิราจินดากุล: ประธาน หมวด: PSU Phuket Esports Club - PSU Phuket แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### M-030 members
- Question: ใครเป็นประธาน
- Resolved: -
- Mode: `pipeline:structured_members_role_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: ตำแหน่ง ประธาน มี 1 คนครับ •    นายษุภากรณ์ จิราจินดากุล: ประธาน   ◦    หมวด: PSU Phuket Esports Club - PSU Phuket แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### M-031 members
- Question: นายนพัทธ์ ฝอยทอง ทำตำแหน่งอะไร
- Resolved: -
- Mode: `pipeline:structured_members_person_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: นายนพัทธ์ ฝอยทอง: รองประธาน หมวด: PSU Phuket Esports Club - PSU Phuket แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### M-032 members
- Question: ใครเป็นรองประธาน
- Resolved: -
- Mode: `pipeline:structured_members_role_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: ตำแหน่ง รองประธาน มี 1 คนครับ •    นายนพัทธ์ ฝอยทอง: รองประธาน   ◦    หมวด: PSU Phuket Esports Club - PSU Phuket แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### M-033 members
- Question: นายปัณณวิชญ์ หนูเรือง ทำตำแหน่งอะไร
- Resolved: -
- Mode: `pipeline:structured_members_person_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: นายปัณณวิชญ์ หนูเรือง: เลขานุการ หมวด: PSU Phuket Esports Club - PSU Phuket แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### M-034 members
- Question: ใครเป็นเลขานุการ
- Resolved: -
- Mode: `pipeline:structured_members_role_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: ตำแหน่ง เลขานุการ มี 1 คนครับ •    นายปัณณวิชญ์ หนูเรือง: เลขานุการ   ◦    หมวด: PSU Phuket Esports Club - PSU Phuket แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### M-035 members
- Question: นายภูจิตร จิรวิริยาภรณ์ ทำตำแหน่งอะไร
- Resolved: -
- Mode: `pipeline:structured_members_person_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: นายภูจิตร จิรวิริยาภรณ์: เหรัญญิก หมวด: PSU Phuket Esports Club - PSU Phuket แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### M-036 members
- Question: ใครเป็นเหรัญญิก
- Resolved: -
- Mode: `pipeline:structured_members_role_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: ตำแหน่ง เหรัญญิก มี 1 คนครับ •    นายภูจิตร จิรวิริยาภรณ์: เหรัญญิก   ◦    หมวด: PSU Phuket Esports Club - PSU Phuket แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### M-037 members
- Question: นายธนชาติ เอ่งฉ้วน ทำตำแหน่งอะไร
- Resolved: -
- Mode: `pipeline:structured_members_person_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: นายธนชาติ เอ่งฉ้วน: ประชาสัมพันธ์ หมวด: PSU Phuket Esports Club - PSU Phuket แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### M-038 members
- Question: ใครเป็นประชาสัมพันธ์
- Resolved: -
- Mode: `pipeline:structured_members_role_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['members'], got overview
- Answer: ตำแหน่ง ประชาสัมพันธ์ มี 1 คนครับ •    นายธนชาติ เอ่งฉ้วน: ประชาสัมพันธ์   ◦    หมวด: PSU Phuket Esports Club - PSU Phuket แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members
