# Broad Usage Eval v1

- Generated at: 2026-07-30T17:13:50
- Cases: 667
- Turn checks: 679
- Passed: 651
- Failed: 28
- Pass rate: 0.9588
- Total wall sec: 91.325
- Allow LLM: False
- RAG fallback: False

## By Group
- ambiguity_no_answer: 18/25 pass, 7 fail
- competition_rules: 64/75 pass, 11 fail
- compound: 12/15 pass, 3 fail
- equipment: 58/58 pass, 0 fail
- game_controls: 153/159 pass, 6 fail
- games: 158/158 pass, 0 fail
- members: 47/47 pass, 0 fail
- reservation: 20/20 pass, 0 fail
- schedule: 10/10 pass, 0 fail
- service_fee: 88/88 pass, 0 fail
- session_followup: 23/24 pass, 1 fail

## By Strategy
- clarification: 15
- compound: 14
- fast/rule: 120
- pipeline: 9
- rag/retrieval: 25
- structured: 496

## Common Problems
- missing any of ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']: 7
- mode expected prefix ['pipeline: 6
- route_category expected ['competition_rules'], got reservation: 5
- missing any of ['ยังไม่พบ', 'ไม่มี', 'ไม่ได้อยู่', 'ตอบจากข้อมูล']: 4
- route_category expected ['clarification', 'games', 'equipment', 'service_fee', 'reservation', 'no_answer'], got general: 3
- route_category expected ['games'], got multi_question: 2
- route_category expected ['multi_question'], got games: 2
- missing 'God of War Ragnarök': 1
- missing 'PC': 1
- missing 'Resident Evil 4 (Remake)': 1
- missing 'Super Smash Bros. Ultimate': 1
- missing any of ['CS2', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']: 1
- missing any of ['L3 (Click Left Stick)', 'มาร์กตำแหน่งศัตรู']: 1
- missing any of ['ROV', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']: 1
- missing any of ['TEKKEN', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']: 1
- missing any of ['VALORANT', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']: 1
- missing any of ['คำถามที่', 'ราคา', 'ปุ่ม', 'Zone', 'จอง']: 1
- route_category expected ['games'], got overview: 1
- route_category expected ['multi_question'], got overview: 1
- route_category expected ['no_answer', 'games', 'general'], got events_news: 1
- route_category expected ['no_answer', 'games', 'general'], got knowledge: 1
- route_category expected ['no_answer', 'games', 'general'], got overview: 1

## Top Failures

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

### CR-003 competition_rules
- Question: VALORANT มาสายจะโดนอะไร
- Resolved: -
- Mode: `pipeline:structured_reservation_fact`
- Route: `reservation/booking_policy`
- Problems: route_category expected ['competition_rules'], got reservation, missing any of ['VALORANT', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: ถ้าไม่เช็คอินก่อนเวลาเริ่มต้นของรอบ ระบบจะยกเลิกการจองทันที และไม่มีการคืนเงิน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### CR-018 competition_rules
- Question: CS2 มาสายจะโดนอะไร
- Resolved: -
- Mode: `pipeline:structured_reservation_fact`
- Route: `reservation/booking_policy`
- Problems: route_category expected ['competition_rules'], got reservation, missing any of ['CS2', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: ถ้าไม่เช็คอินก่อนเวลาเริ่มต้นของรอบ ระบบจะยกเลิกการจองทันที และไม่มีการคืนเงิน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### CR-032 competition_rules
- Question: Counter-Strike 2 ใช้ผู้เล่นกี่คน
- Resolved: -
- Mode: `pipeline:competition_generic_fast_path`
- Route: `competition_rules/competition_rules_lookup`
- Problems: missing any of ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: CS2 ใช้ผู้เล่นทีมละ 5 คนครับ แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### CR-033 competition_rules
- Question: Counter-Strike 2 มาสายจะโดนอะไร
- Resolved: -
- Mode: `pipeline:structured_reservation_fact`
- Route: `reservation/booking_policy`
- Problems: route_category expected ['competition_rules'], got reservation, missing any of ['Counter-Strike', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: ถ้าไม่เช็คอินก่อนเวลาเริ่มต้นของรอบ ระบบจะยกเลิกการจองทันที และไม่มีการคืนเงิน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

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

### CR-048 competition_rules
- Question: TEKKEN 8 มาสายจะโดนอะไร
- Resolved: -
- Mode: `pipeline:structured_reservation_fact`
- Route: `reservation/booking_policy`
- Problems: route_category expected ['competition_rules'], got reservation, missing any of ['TEKKEN', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: ถ้าไม่เช็คอินก่อนเวลาเริ่มต้นของรอบ ระบบจะยกเลิกการจองทันที และไม่มีการคืนเงิน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### CR-063 competition_rules
- Question: ROV มาสายจะโดนอะไร
- Resolved: -
- Mode: `pipeline:structured_reservation_fact`
- Route: `reservation/booking_policy`
- Problems: route_category expected ['competition_rules'], got reservation, missing any of ['ROV', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']
- Answer: ถ้าไม่เช็คอินก่อนเวลาเริ่มต้นของรอบ ระบบจะยกเลิกการจองทันที และไม่มีการคืนเงิน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

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
