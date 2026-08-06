# Broad Usage Eval v1

- Generated at: 2026-07-30T16:26:11
- Cases: 667
- Turn checks: 679
- Passed: 625
- Failed: 54
- Pass rate: 0.9205
- Total wall sec: 121.022
- Allow LLM: True
- RAG fallback: False

## By Group
- ambiguity_no_answer: 18/25 pass, 7 fail
- competition_rules: 69/75 pass, 6 fail
- compound: 12/15 pass, 3 fail
- equipment: 43/58 pass, 15 fail
- game_controls: 153/159 pass, 6 fail
- games: 154/158 pass, 4 fail
- members: 45/47 pass, 2 fail
- reservation: 15/20 pass, 5 fail
- schedule: 8/10 pass, 2 fail
- service_fee: 85/88 pass, 3 fail
- session_followup: 23/24 pass, 1 fail

## By Strategy
- clarification: 19
- compound: 15
- fast/rule: 137
- pipeline: 9
- rag/retrieval: 40
- structured: 459

## Common Problems
- route_category expected ['equipment'], got general: 10
- mode expected prefix ['pipeline: 8
- missing any of ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']: 6
- missing any of ['Gaming', 'PC']: 6
- missing any of ['จอง', 'เช็คอิน', 'ชำระ', 'session', 'ยกเลิก']: 4
- missing any of ['ยังไม่พบ', 'ไม่มี', 'ไม่ได้อยู่', 'ตอบจากข้อมูล']: 4
- route_category expected ['clarification', 'games', 'equipment', 'service_fee', 'reservation', 'no_answer'], got general: 3
- missing any of ['บาท', 'ต่างกัน', 'ฟรี', '0 บาท']: 2
- missing any of ['เปิด', 'ปิด', 'เวลา', 'วัน', 'ไม่เปิด']: 2
- route_category expected ['equipment'], got knowledge: 2
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
- route_category expected ['equipment', 'games'], got knowledge: 1
- route_category expected ['equipment'], got games: 1
- route_category expected ['games'], got clarification: 1
- route_category expected ['games'], got equipment: 1
- route_category expected ['games'], got overview: 1
- route_category expected ['members', 'overview'], got clarification: 1
- route_category expected ['members', 'overview'], got general: 1
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

### E-014 equipment
- Question: Gaming Monitor คืออะไร
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Problems: route_category expected ['equipment'], got general, missing any of ['Gaming', 'PC']
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### E-017 equipment
- Question: Gaming Keyboard คืออะไร
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Problems: route_category expected ['equipment'], got general, missing any of ['Gaming', 'PC']
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### E-020 equipment
- Question: Gaming Mouse คืออะไร
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Problems: route_category expected ['equipment'], got general, missing any of ['Gaming', 'PC']
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### E-023 equipment
- Question: Gaming Headset คืออะไร
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Problems: route_category expected ['equipment'], got general, missing any of ['Gaming', 'PC']
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### E-026 equipment
- Question: Gaming Chair คืออะไร
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Problems: route_category expected ['equipment'], got general, missing any of ['Gaming', 'PC']
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

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
- Problems: route_category expected ['equipment', 'games'], got knowledge, mode expected prefix ['pipeline:structured_equipment_item', 'pipeline:equipment_item_location_fast_path'], got pipeline:chatbot_greeting_fast_path, missing any of ['Cockpit', 'Zone']
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
- Problems: mode expected prefix ['pipeline:structured_equipment_item', 'pipeline:equipment_item_location_fast_path'], got pipeline:structured_game_detail
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

### M-004 members
- Question: แต่ละหมวดมีใครบ้าง
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/unknown_domain_query`
- Problems: route_category expected ['members', 'overview'], got general, missing any of ['Members', 'สมาชิก', 'คน', 'หมวด']
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### M-041 members
- Question: นางสาวชญาภา จันทร์เอิบ ทำตำแหน่งอะไร
- Resolved: -
- Mode: `pipeline:ambiguity_clarification`
- Route: `clarification/ambiguity_gate_clarification`
- Problems: route_category expected ['members', 'overview'], got clarification, missing any of ['กรรมการ', 'นางสาวชญาภา']
- Answer: คำถามนี้มีได้หลายความหมายครับ ขอระบุเพิ่มนิดหนึ่งว่าต้องการถามเรื่องไหน: สมาชิกทีม, เวลาเปิด-ปิด

### CR-032 competition_rules
- Question: Counter-Strike 2 ใช้ผู้เล่นกี่คน
- Resolved: -
- Mode: `pipeline:competition_generic_fast_path`
- Route: `competition_rules/competition_rules_lookup`
- Problems: missing any of ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: CS2 ใช้ผู้เล่นทีมละ 5 คนครับ แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### CR-034 competition_rules
- Question: Counter-Strike 2 pause ได้ไหม
- Resolved: -
- Mode: `pipeline:competition_generic_fast_path`
- Route: `competition_rules/competition_rules_lookup`
- Problems: missing any of ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: CS2 มีทั้ง Technical Pause และ Tactical Timeout ครับ •    Technical Pause ใช้กรณีปัญหาขัดข้อง •    Tactical Timeout ใช้ตามเงื่อนไขช่วง Freeze time แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### CR-041 competition_rules
- Question: Counter-Strike 2 ถ้าใช้ bug จะโดนอะไร
- Resolved: -
- Mode: `pipeline:competition_generic_fast_path`
- Route: `competition_rules/competition_rules_lookup`
- Problems: missing any of ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: CS2 มีบทลงโทษครับ •    ตัวอย่าง: ใช้บัค/โกง/พฤติกรรมไม่เหมาะสม อาจถูกปรับแพ้เป็นรอบ แมตช์ หรือตัดสิทธิ์ตามความรุนแรง แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### CR-042 competition_rules
- Question: Counter-Strike 2 ต้องเช็คอินก่อนแข่งไหม
- Resolved: -
- Mode: `pipeline:competition_generic_fast_path`
- Route: `competition_rules/competition_rules_lookup`
- Problems: missing any of ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: CS2 ต้องยืนยัน/รายงานตัวตามเวลาที่ผู้จัดกำหนดครับ •    หากไม่ยืนยันก่อนแมตช์มีความเสี่ยงถูกตัดสิทธิ์ แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### CR-044 competition_rules
- Question: Counter-Strike 2 แผนที่มีอะไรบ้าง
- Resolved: -
- Mode: `pipeline:competition_generic_fast_path`
- Route: `competition_rules/competition_rules_lookup`
- Problems: missing any of ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: CS2 มีข้อมูล map pool ครับ •    แผนที่ที่พบ: Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### CR-045 competition_rules
- Question: Counter-Strike 2 สรุปกติกาสั้นๆ
- Resolved: -
- Mode: `pipeline:competition_fact_card`
- Route: `competition_rules/competition_rules_lookup`
- Problems: missing any of ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### C-004 compound
- Question: Gran Turismo 7 เล่นยังไง แล้วปุ่มเร่งกดอะไร
- Resolved: -
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Problems: route_category expected ['multi_question'], got games, mode expected prefix ['pipeline:multi_question_splitter'], got pipeline:structured_game_controls
- Answer: Gran Turismo 7 ปุ่มที่ตรงกับคำถาม: PlayStation / PS5 •    R2: คันเร่ง - กดเพื่อเร่งเครื่อง •    R3: ไนตรัส / เร่งแซง - ใช้งานระบบเพิ่มความเร็วพิเศษที่มีติดตั้งในรถบางรุ่น แหล่งข้อมูล: https://gameinputdatabase.com/game/135

### C-007 compound
- Question: สมาชิกมีกี่คน แล้วใครเป็นอธิการบดี
- Resolved: -
- Mode: `pipeline:structured_members_role_lookup`
- Route: `overview/members_lookup`
- Problems: route_category expected ['multi_question'], got overview, mode expected prefix ['pipeline:multi_question_splitter'], got pipeline:structured_members_role_lookup, missing any of ['คำถามที่', 'ราคา', 'ปุ่ม', 'Zone', 'จอง']
- Answer: ตำแหน่ง อธิการบดี มี 1 คนครับ •    ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี (มหาวิทยาลัยสงขลานครินทร์)   ◦    หมวด: Members แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### C-011 compound
- Question: Call of Duty ปุ่มยิงอะไร แล้วเล่นได้ที่ไหน
- Resolved: -
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Problems: route_category expected ['multi_question'], got games, mode expected prefix ['pipeline:multi_question_splitter'], got pipeline:structured_game_controls
- Answer: Call of Duty: Modern Warfare III ปุ่มที่ตรงกับคำถาม: PlayStation / PS5 •    R2: ยิงอาวุธ - กดยิงปืน แหล่งข้อมูล: https://www.gamepur.com/guides/best-modern-warfare-3-controller-settings-aim-assist-deadzones-button-layout

### ANA-006 ambiguity_no_answer
- Question: เครื่องไหนดีที่สุด
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/unknown_domain_query`
- Problems: route_category expected ['clarification', 'games', 'equipment', 'service_fee', 'reservation', 'no_answer'], got general
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### ANA-008 ambiguity_no_answer
- Question: มีอะไรแนะนำไหม
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/general_knowledge_query`
- Problems: route_category expected ['clarification', 'games', 'equipment', 'service_fee', 'reservation', 'no_answer'], got general
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### ANA-015 ambiguity_no_answer
- Question: สรุปคือทำยังไง
- Resolved: -
- Mode: `pipeline:no_answer`
- Route: `general/unknown_domain_query`
- Problems: route_category expected ['clarification', 'games', 'equipment', 'service_fee', 'reservation', 'no_answer'], got general
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### ANA-020 ambiguity_no_answer
- Question: เกม Valorant Mobile มีไหม
- Resolved: -
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_availability_lookup`
- Problems: missing any of ['ยังไม่พบ', 'ไม่มี', 'ไม่ได้อยู่', 'ตอบจากข้อมูล']
- Answer: VALORANT: VALORANT คือเกมยิงเชิงกลยุทธ์ที่ผู้เล่นเลือก Agent ที่มีสกิลเฉพาะ แล้วเล่นเป็นฝ่ายบุก/รับในแต่ละรอบ แนวเกม: เกมยิง Tactical FPS แบบทีม 5v5 วิธีเล่นโดยสรุป: ฝ่ายบุกต้องวาง Spike ส่วนฝ่ายรับต้องป้องกันพื้นที่หรือกู้ Spike การเล่นเน้นการเล็ง การสื่อสาร...

### ANA-021 ambiguity_no_answer
- Question: ขอเบอร์โทรส่วนตัวเจ้าหน้าที่
- Resolved: -
- Mode: `pipeline:structured_members_group_list`
- Route: `overview/list`
- Problems: route_category expected ['no_answer', 'games', 'general'], got overview, missing any of ['ยังไม่พบ', 'ไม่มี', 'ไม่ได้อยู่', 'ตอบจากข้อมูล']
- Answer: สมาชิกจากหน้า Members แยกตามหมวด รวม 25 คน: Members (7 คน): •    ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี •    รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี •    รศ.ดร.อซีส นันทอมรพงศ์: คณบดี •    ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ •    นายพฤทธิ์ เกษตรสมบูรณ์:...

### ANA-022 ambiguity_no_answer
- Question: ขอข้อมูลที่ไม่ได้อยู่ในเว็บ PSU Esports
- Resolved: -
- Mode: `pipeline:hybrid_guarded_rerank`
- Route: `knowledge/knowledge_lookup`
- Problems: route_category expected ['no_answer', 'games', 'general'], got knowledge, missing any of ['ยังไม่พบ', 'ไม่มี', 'ไม่ได้อยู่', 'ตอบจากข้อมูล']
- Answer: บทความ Overcooked! 2 เกมสุดมันส์ที่ได้มากกว่าความสนุก ระบุว่าเกมนี้ไม่ได้มีแค่ความสนุก แต่ช่วยพัฒนาทักษะชีวิตหลายด้าน เช่น การสื่อสาร การทำงานเป็นทีม การวางแผน และการจัดการสถานการณ์กดดัน แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Knowledge

### ANA-023 ambiguity_no_answer
- Question: วันนี้มีข่าว esports อะไรล่าสุด
- Resolved: -
- Mode: `pipeline:rag_direct_curated`
- Route: `events_news/news_lookup`
- Problems: route_category expected ['no_answer', 'games', 'general'], got events_news, missing any of ['ยังไม่พบ', 'ไม่มี', 'ไม่ได้อยู่', 'ตอบจากข้อมูล']
- Answer: เมื่อวันที่ 25 เมษายน 2569 PSU Esports Studio - Phuket จัดการแข่งขัน PSU Phuket CS 2 2026 Tournament ในเกม Counter-Strike 2 แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

### SF-007 session_followup
- Question: จอง
- Resolved: PC จองยังไง
- Mode: `pipeline:structured_reservation_fact`
- Route: `reservation/booking_policy`
- Problems: missing 'PC'
- Answer: ขั้นตอนจองโดยสรุป: •    เลือกบริการหรือโซนที่ต้องการใช้ •    เลือกวันและรอบเวลาที่ต้องการ •    กรอก Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล และเบอร์โทรศัพท์ •    ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง •    แนบสลิปและยืนยันการจอง แหล่ง...
