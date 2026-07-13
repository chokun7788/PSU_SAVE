# Competition Ground Truth By Game V2 - Item Cause Audit

วันที่: 2026-07-03

รายงานนี้ไล่ดูผลรัน Ground Truth ชุด `competition_by_game_v2` แบบเรียงข้อ เพื่อแยกว่าสาเหตุผิดเกิดจากอะไร ปัญหาคืออะไร และลักษณะคำตอบของ AI เป็นแบบไหน

## Summary

- Total: 184
- PASS: 41
- FAIL: 143
- Pass rate: 22.28%

## Cause Counts

- `wrong_fact_card_intent`: 53
- `wrong_route`: 47
- `pass`: 41
- `partial_or_strict_keyword`: 36
- `no_answer_despite_data`: 6
- `rag_partial_answer`: 1

## Cause By Game

### Counter-Strike 2
- `wrong_route`: 17
- `wrong_fact_card_intent`: 16
- `pass`: 9
- `partial_or_strict_keyword`: 4
- `no_answer_despite_data`: 1
- `rag_partial_answer`: 1

### Arena of Valor (RoV)
- `wrong_fact_card_intent`: 14
- `pass`: 13
- `partial_or_strict_keyword`: 11
- `wrong_route`: 8
- `no_answer_despite_data`: 2

### VALORANT
- `wrong_fact_card_intent`: 15
- `wrong_route`: 13
- `pass`: 10
- `partial_or_strict_keyword`: 9
- `no_answer_despite_data`: 1

### Tekken 8
- `partial_or_strict_keyword`: 12
- `pass`: 9
- `wrong_route`: 9
- `wrong_fact_card_intent`: 8
- `no_answer_despite_data`: 2

## Item Audit

## Counter-Strike 2

### 1. [FAIL] competition_cs2_v2_001 - ผิด/ต้องแก้

- คำถาม: PSU Phuket CS2 2026 รับเฉพาะนักศึกษาแบบไหน
- Intent ที่คาด: `eligibility`
- Route/Mode: `events_news` / `pipeline:rag_direct_curated`
- Retrieved: `curated_news_chinese_students_game_based_learning, curated_news_game_on_thaimuang, curated_news_cs2_2026`
- Expected keywords: `นักศึกษา, มหาวิทยาลัยสงขลานครินทร์, ภูเก็ต`
- Missing keywords: `มหาวิทยาลัยสงขลานครินทร์, ภูเก็ต`
- Missing source: `competition_rules_cs2_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็น events_news เพราะเจอคำว่า PSU/รายการ/2026 แล้วไปค้นข่าวแทนเอกสารกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Counter-Strike 2 แต่ถูกส่งไป `events_news`
- ลักษณะคำตอบ: ตอบจากข่าวหรือกิจกรรม ทำให้คำตอบกลายเป็นข่าว ไม่ใช่กติกาของรายการแข่งขัน
- คำตอบย่อจาก AI: เมื่อวันที่ 27 กุมภาพันธ์ 2569 นักศึกษาชาวจีนระดับปริญญาโท คณะการบริการและการท่องเที่ยว จำนวน 11 คน เข้าร่วมกิจกรรมการเรียนรู้โดยใช้เกมเป็นฐาน (Game-based Learning) ณ PSU Esports Studio - Phuket แหล่งข้อมูล: https://espo...
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 2. [FAIL] competition_cs2_v2_002 - ผิด/ต้องแก้

- คำถาม: คนนอก PSU Phuket ลงแข่ง CS2 รายการนี้ได้ไหม
- Intent ที่คาด: `eligibility`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_pause_policy`
- Expected keywords: `เฉพาะ, นักศึกษา, ภูเก็ต`
- Missing keywords: `เฉพาะ, นักศึกษา, ภูเก็ต`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `cs2_pause_policy` คนละ intent กับที่ถาม (`eligibility`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `cs2_pause_policy` แต่คำถามต้องการ intent `eligibility`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_pause_policy`
- คำตอบย่อจาก AI: คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 3. [PASS] competition_cs2_v2_003 - ผ่าน

- คำถาม: CS2 แข่งทีมละกี่คน
- Intent ที่คาด: `team_size`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_team_size_players`
- Expected keywords: `CS2, ผู้เล่น 5 คน`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_team_size_players`
- คำตอบย่อจาก AI: คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน หลักฐานจากกติกา: - เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_ru...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 4. [PASS] competition_cs2_v2_004 - ผ่าน

- คำถาม: Counter-Strike 2 ต้องส่งผู้เล่นหลักกี่คน
- Intent ที่คาด: `team_size`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_team_size_players`
- Expected keywords: `5 คน`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_team_size_players`
- คำตอบย่อจาก AI: คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน หลักฐานจากกติกา: - เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_ru...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 5. [FAIL] competition_cs2_v2_005 - ผิด/ต้องแก้

- คำถาม: CS2 ใช้แพลตฟอร์มอะไรและห้ามดัดแปลงตัวเกมไหม
- Intent ที่คาด: `game_version`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `Steam, ห้าม, ดัดแปลง`
- Missing keywords: `Steam, ห้าม, ดัดแปลง`
- Missing source: `competition_rules_cs2_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Counter-Strike 2 แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 6. [FAIL] competition_cs2_v2_006 - ผิด/ต้องแก้

- คำถาม: รายการ CS2 ใช้เวอร์ชันเกมแบบไหน
- Intent ที่คาด: `game_version`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `ล่าสุด, CS2, Steam`
- Missing keywords: `ล่าสุด, CS2, Steam`
- Missing source: `competition_rules_cs2_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Counter-Strike 2 แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 7. [FAIL] competition_cs2_v2_007 - ผิด/ต้องแก้

- คำถาม: ภาษาทางการของการแข่งขัน CS2 คือภาษาอะไร
- Intent ที่คาด: `language`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_map_pool`
- Expected keywords: `ภาษาไทย`
- Missing keywords: `ภาษาไทย`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `cs2_map_pool` คนละ intent กับที่ถาม (`language`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `cs2_map_pool` แต่คำถามต้องการ intent `language`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_map_pool`
- คำตอบย่อจาก AI: คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train หลักฐานจากกติกา: - เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train อ้างอิงจากกติกา: C...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 8. [FAIL] competition_cs2_v2_008 - ผิด/ต้องแก้

- คำถาม: ถ้าจะประท้วงผล CS2 ต้องใช้ภาษาอะไรในเอกสาร
- Intent ที่คาด: `language`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `ภาษาไทย`
- Missing keywords: `ภาษาไทย`
- Missing source: `competition_rules_cs2_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Counter-Strike 2 แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 9. [FAIL] competition_cs2_v2_009 - ผิด/ต้องแก้

- คำถาม: CS2 แข่งกี่วันและแข่งที่ไหน
- Intent ที่คาด: `schedule_location`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_team_size_players`
- Expected keywords: `1 วัน, PSU Esports Studio, Phuket`
- Missing keywords: `1 วัน, PSU Esports Studio`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `cs2_team_size_players` คนละ intent กับที่ถาม (`schedule_location`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `cs2_team_size_players` แต่คำถามต้องการ intent `schedule_location`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_team_size_players`
- คำตอบย่อจาก AI: คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน หลักฐานจากกติกา: - เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_ru...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 10. [FAIL] competition_cs2_v2_010 - ผิด/ต้องแก้

- คำถาม: สถานที่จัด PSU Phuket CS2 2026 คือที่ไหน
- Intent ที่คาด: `schedule_location`
- Route/Mode: `events_news` / `pipeline:category_rule_fast_path`
- Retrieved: `rule_contact_location`
- Expected keywords: `PSU Esports Studio, Phuket`
- Missing keywords: `-`
- Missing source: `competition_rules_cs2_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็น events_news เพราะเจอคำว่า PSU/รายการ/2026 แล้วไปค้นข่าวแทนเอกสารกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Counter-Strike 2 แต่ถูกส่งไป `events_news`
- ลักษณะคำตอบ: ตอบจากข่าวหรือกิจกรรม ทำให้คำตอบกลายเป็นข่าว ไม่ใช่กติกาของรายการแข่งขัน
- คำตอบย่อจาก AI: PSU Esports Studio - Phuket ตั้งอยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120 แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Contact-Us
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 11. [FAIL] competition_cs2_v2_011 - ผิด/ต้องแก้

- คำถาม: CS2 ใช้ช่องทางสื่อสารหลักอะไร
- Intent ที่คาด: `communication`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `Discord`
- Missing keywords: `Discord`
- Missing source: `competition_rules_cs2_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Counter-Strike 2 แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 12. [FAIL] competition_cs2_v2_012 - ผิด/ต้องแก้

- คำถาม: ผู้เข้าแข่ง CS2 ต้องใช้เซิร์ฟเวอร์ไหนในการสื่อสาร
- Intent ที่คาด: `communication`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_team_size_players`
- Expected keywords: `Discord, ศูนย์`
- Missing keywords: `Discord, ศูนย์`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `cs2_team_size_players` คนละ intent กับที่ถาม (`communication`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `cs2_team_size_players` แต่คำถามต้องการ intent `communication`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_team_size_players`
- คำตอบย่อจาก AI: คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน หลักฐานจากกติกา: - เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_ru...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 13. [FAIL] competition_cs2_v2_013 - ผิด/ต้องแก้

- คำถาม: CS2 เปลี่ยนสมาชิกทีมระหว่างทัวร์นาเมนต์ได้ไหม
- Intent ที่คาด: `roster_change`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_team_size_players`
- Expected keywords: `ไม่มีการเปลี่ยนแปลง, สมาชิก`
- Missing keywords: `ไม่มีการเปลี่ยนแปลง, สมาชิก`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `cs2_team_size_players` คนละ intent กับที่ถาม (`roster_change`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `cs2_team_size_players` แต่คำถามต้องการ intent `roster_change`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_team_size_players`
- คำตอบย่อจาก AI: คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน หลักฐานจากกติกา: - เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_ru...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 14. [FAIL] competition_cs2_v2_014 - ผิด/ต้องแก้

- คำถาม: หลังปิดรับสมัคร CS2 ลงทะเบียนผู้เล่นเพิ่มได้ไหม
- Intent ที่คาด: `registration`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_pause_policy`
- Expected keywords: `ไม่อนุญาต, ปิดรับสมัคร`
- Missing keywords: `ไม่อนุญาต, ปิดรับสมัคร`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `cs2_pause_policy` คนละ intent กับที่ถาม (`registration`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `cs2_pause_policy` แต่คำถามต้องการ intent `registration`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_pause_policy`
- คำตอบย่อจาก AI: คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 15. [FAIL] competition_cs2_v2_015 - ผิด/ต้องแก้

- คำถาม: ถ้าผู้เล่น CS2 ถอนตัวทีมจะเป็นยังไง
- Intent ที่คาด: `eligibility`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_team_size_players`
- Expected keywords: `ถอนตัว, ตัดสิทธิ์`
- Missing keywords: `ถอนตัว, ตัดสิทธิ์`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `cs2_team_size_players` คนละ intent กับที่ถาม (`eligibility`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `cs2_team_size_players` แต่คำถามต้องการ intent `eligibility`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_team_size_players`
- คำตอบย่อจาก AI: คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน หลักฐานจากกติกา: - เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_ru...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 16. [FAIL] competition_cs2_v2_016 - ผิด/ต้องแก้

- คำถาม: ผู้เล่น CS2 เล่นให้สองทีมได้ไหม
- Intent ที่คาด: `eligibility`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_team_size_players`
- Expected keywords: `ทีมเดียว`
- Missing keywords: `ทีมเดียว`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_team_size_players`
- คำตอบย่อจาก AI: คำตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน หลักฐานจากกติกา: - เอกสารระบุว่าองค์ประกอบทีมแต่ละทีมประกอบด้วยผู้เล่น 5 คน อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล่งข้อมูล: local://competition_ru...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 17. [FAIL] competition_cs2_v2_017 - ผิด/ต้องแก้

- คำถาม: สายการแข่งขัน CS2 จะประกาศก่อนแข่งนานแค่ไหน
- Intent ที่คาด: `schedule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_map_pool`
- Expected keywords: `ล่วงหน้า, 1 วัน`
- Missing keywords: `ล่วงหน้า, 1 วัน`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `cs2_map_pool` คนละ intent กับที่ถาม (`schedule`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `cs2_map_pool` แต่คำถามต้องการ intent `schedule`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_map_pool`
- คำตอบย่อจาก AI: คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train หลักฐานจากกติกา: - เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train อ้างอิงจากกติกา: C...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 18. [PASS] competition_cs2_v2_018 - ผ่าน

- คำถาม: CS2 มาสายหรือไม่ยืนยันเข้าแข่งก่อนแมตช์เสี่ยงอะไร
- Intent ที่คาด: `late_start`
- Route/Mode: `competition_rules` / `pipeline:rag_direct_curated`
- Retrieved: `competition_rules_cs2_psu_phuket_2026_s15_c01, competition_rules_cs2_psu_phuket_2026_s37_c01, competition_rules_cs2_psu_phuket_2026_s54_c01`
- Expected keywords: `มาสาย, ตัดสิทธิ์`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบจาก curated/chunk retrieval โดยตรงจาก `competition_rules_cs2_psu_phuket_2026_s15_c01, competition_rules_cs2_psu_phuket_2026_s37_c01, competition_rules_cs2_psu_phuket_2026_s54_c01` อาจตรงบางส่วนหรือดึง source ผิด
- คำตอบย่อจาก AI: คำตอบ: 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์ รายละเอียดที่เกี่ยวข้อง: - 2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 19. [PASS] competition_cs2_v2_019 - ผ่าน

- คำถาม: รูปแบบทัวร์นาเมนต์ CS2 เป็นแบบไหน
- Intent ที่คาด: `format`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_format_single_elim_bo3`
- Expected keywords: `Single Elimination`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_format_single_elim_bo3`
- คำตอบย่อจาก AI: คำตอบ: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3) หลักฐานจากกติกา: - เอกสารระบุรูปแบบทัวร์นาเมนต์ Single Elimination และกำหนดรอบรอง/รอบชิงเป็น BO3 อ้างอิงจากกติกา: Counter-Strike 2 / P...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 20. [PASS] competition_cs2_v2_020 - ผ่าน

- คำถาม: CS2 รอบรองกับรอบชิงแข่ง BO อะไร
- Intent ที่คาด: `format`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_format_single_elim_bo3`
- Expected keywords: `รอบรอง, รอบชิง, BO3`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_format_single_elim_bo3`
- คำตอบย่อจาก AI: คำตอบ: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3) หลักฐานจากกติกา: - เอกสารระบุรูปแบบทัวร์นาเมนต์ Single Elimination และกำหนดรอบรอง/รอบชิงเป็น BO3 อ้างอิงจากกติกา: Counter-Strike 2 / P...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 21. [FAIL] competition_cs2_v2_021 - ผิด/ต้องแก้

- คำถาม: โหมดในเกม CS2 ใช้โหมดอะไร
- Intent ที่คาด: `game_setting`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `Competitive, 5v5`
- Missing keywords: `Competitive, 5v5`
- Missing source: `competition_rules_cs2_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Counter-Strike 2 แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 22. [FAIL] competition_cs2_v2_022 - ผิด/ต้องแก้

- คำถาม: CS2 เวลาต่อรอบกับ Freeze time เท่าไหร่
- Intent ที่คาด: `game_setting`
- Route/Mode: `service_fee` / `pipeline:rag_direct_curated`
- Retrieved: `curated_service_fee_pc_unknown, curated_service_fee_ps5_rates, curated_service_fee_nintendo_1_2_rates`
- Expected keywords: `1:55, 15 วินาที`
- Missing keywords: `1:55, 15 วินาที`
- Missing source: `competition_rules_cs2_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็น service_fee เพราะเจอคำคล้ายราคา/เวลา/ชั่วโมง ทำให้ไปดึงข้อมูลราคาแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Counter-Strike 2 แต่ถูกส่งไป `service_fee`
- ลักษณะคำตอบ: ตอบจากหมวดราคา/ค่าบริการ ซึ่งเป็นคนละ domain กับกติกาการแข่งขัน
- คำตอบย่อจาก AI: บริการ PC ในระบบจองมีระยะเวลา 60 min แต่ในข้อมูลที่ดึงมาและในรูป Service Fee 2026 ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ จึงยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/upl...
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 23. [FAIL] competition_cs2_v2_023 - ผิด/ต้องแก้

- คำถาม: CS2 เงินเริ่มต้นกับเวลาระเบิดตั้งไว้เท่าไหร่
- Intent ที่คาด: `game_setting`
- Route/Mode: `service_fee` / `pipeline:rag_direct_curated`
- Retrieved: `curated_service_fee_pc_unknown, curated_service_fee_2026_full_table, curated_user_group_alias_psu_student_staff`
- Expected keywords: `$800, 40 วินาที`
- Missing keywords: `$800, 40 วินาที`
- Missing source: `competition_rules_cs2_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็น service_fee เพราะเจอคำคล้ายราคา/เวลา/ชั่วโมง ทำให้ไปดึงข้อมูลราคาแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Counter-Strike 2 แต่ถูกส่งไป `service_fee`
- ลักษณะคำตอบ: ตอบจากหมวดราคา/ค่าบริการ ซึ่งเป็นคนละ domain กับกติกาการแข่งขัน
- คำตอบย่อจาก AI: บริการ PC ในระบบจองมีระยะเวลา 60 min แต่ในข้อมูลที่ดึงมาและในรูป Service Fee 2026 ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ จึงยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/upl...
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 24. [FAIL] competition_cs2_v2_024 - ผิด/ต้องแก้

- คำถาม: CS2 ชนะกี่รอบก่อนถึงชนะในแผนที่
- Intent ที่คาด: `game_setting`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_map_pool`
- Expected keywords: `13 รอบ`
- Missing keywords: `13 รอบ`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `cs2_map_pool` คนละ intent กับที่ถาม (`game_setting`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `cs2_map_pool` แต่คำถามต้องการ intent `game_setting`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_map_pool`
- คำตอบย่อจาก AI: คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train หลักฐานจากกติกา: - เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train อ้างอิงจากกติกา: C...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 25. [FAIL] competition_cs2_v2_025 - ผิด/ต้องแก้

- คำถาม: CS2 เล่นสูงสุดกี่รอบก่อน overtime
- Intent ที่คาด: `game_setting`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `24 รอบ, 12 รอบ`
- Missing keywords: `24 รอบ, 12 รอบ`
- Missing source: `competition_rules_cs2_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Counter-Strike 2 แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 26. [FAIL] competition_cs2_v2_026 - ผิด/ต้องแก้

- คำถาม: CS2 overtime เล่นยังไง
- Intent ที่คาด: `game_setting`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `ฝั่งละ 3 รอบ, 4 ใน 6, $10,000`
- Missing keywords: `ฝั่งละ 3 รอบ, 4 ใน 6, $10,000`
- Missing source: `competition_rules_cs2_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Counter-Strike 2 แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 27. [FAIL] competition_cs2_v2_027 - ผิด/ต้องแก้

- คำถาม: CS2 ต่อเวลาได้จำกัดกี่ครั้ง
- Intent ที่คาด: `game_setting`
- Route/Mode: `schedule` / `pipeline:schedule_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `ไม่จำกัด`
- Missing keywords: `ไม่จำกัด`
- Missing source: `competition_rules_cs2_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็น schedule ของศูนย์ เพราะเจอคำถามเวลา/รอบ ทำให้ตอบเวลาเปิด-ปิดศูนย์แทนตารางแข่งขัน
- ปัญหา: คำถามควรเป็น competition_rules ของ Counter-Strike 2 แต่ถูกส่งไป `schedule`
- ลักษณะคำตอบ: ตอบเป็นเวลาเปิด-ปิด/ตารางบริการของศูนย์ ทำให้หลุดจากตารางหรือกติกาการแข่งขัน
- คำตอบย่อจาก AI: เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน รายละเอียดจากตาราง: - Morning คือ 09:00-12:00 - Afternoon คือ 13:00-16:00 - Monday ช่วง Morning 09:00-12:00 เป็น Maint...
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 28. [PASS] competition_cs2_v2_028 - ผ่าน

- คำถาม: CS2 map pool มีอะไรบ้าง
- Intent ที่คาด: `map_pool`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_map_pool`
- Expected keywords: `Ancient, Anubis, Dust 2, Train`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_map_pool`
- คำตอบย่อจาก AI: คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train หลักฐานจากกติกา: - เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train อ้างอิงจากกติกา: C...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 29. [PASS] competition_cs2_v2_029 - ผ่าน

- คำถาม: CS2 มี Mirage กับ Nuke ในแผนที่แข่งไหม
- Intent ที่คาด: `map_pool`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_map_pool`
- Expected keywords: `Mirage, Nuke`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_map_pool`
- คำตอบย่อจาก AI: คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train หลักฐานจากกติกา: - เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train อ้างอิงจากกติกา: C...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 30. [FAIL] competition_cs2_v2_030 - ผิด/ต้องแก้

- คำถาม: CS2 เลือกแผนที่ผ่านอะไร
- Intent ที่คาด: `map_pool`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_map_pool`
- Expected keywords: `MAPBAN.GG`
- Missing keywords: `MAPBAN.GG`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_map_pool`
- คำตอบย่อจาก AI: คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train หลักฐานจากกติกา: - เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train อ้างอิงจากกติกา: C...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 31. [FAIL] competition_cs2_v2_031 - ผิด/ต้องแก้

- คำถาม: CS2 เลือกฝั่งด้วยวิธีไหน
- Intent ที่คาด: `side_selection`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `ดวลมีด, เลือกฝั่ง`
- Missing keywords: `ดวลมีด, เลือกฝั่ง`
- Missing source: `competition_rules_cs2_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Counter-Strike 2 แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 32. [PASS] competition_cs2_v2_032 - ผ่าน

- คำถาม: CS2 technical pause ขอได้กี่ครั้งและนานเท่าไหร่
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_pause_policy`
- Expected keywords: `2 ครั้ง, 10 นาที`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_pause_policy`
- คำตอบย่อจาก AI: คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 33. [FAIL] competition_cs2_v2_033 - ผิด/ต้องแก้

- คำถาม: CS2 เครื่องมีปัญหาต้องแจ้งใครตอน technical pause
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_pause_policy`
- Expected keywords: `กรรมการ, ทันที`
- Missing keywords: `กรรมการ, ทันที`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_pause_policy`
- คำตอบย่อจาก AI: คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 34. [PASS] competition_cs2_v2_034 - ผ่าน

- คำถาม: CS2 tactical timeout ได้กี่ครั้ง ครั้งละกี่วินาที
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_pause_policy`
- Expected keywords: `4 ครั้ง, 30 วินาที`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_pause_policy`
- คำตอบย่อจาก AI: คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 35. [FAIL] competition_cs2_v2_035 - ผิด/ต้องแก้

- คำถาม: CS2 ขอเวลานอกใช้ได้ช่วงไหน
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_pause_policy`
- Expected keywords: `Freeze time`
- Missing keywords: `Freeze time`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_pause_policy`
- คำตอบย่อจาก AI: คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 36. [FAIL] competition_cs2_v2_036 - ผิด/ต้องแก้

- คำถาม: CS2 ใช้บัคแผนที่หรือ Engine ได้ไหม
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_map_pool`
- Expected keywords: `ห้าม, บัค, ปรับแพ้`
- Missing keywords: `ห้าม, บัค, ปรับแพ้`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `cs2_map_pool` คนละ intent กับที่ถาม (`penalty`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `cs2_map_pool` แต่คำถามต้องการ intent `penalty`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_map_pool`
- คำตอบย่อจาก AI: คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train หลักฐานจากกติกา: - เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train อ้างอิงจากกติกา: C...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 37. [FAIL] competition_cs2_v2_037 - ผิด/ต้องแก้

- คำถาม: CS2 ดูสตรีมสดระหว่างแข่งได้ไหม
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_pause_policy`
- Expected keywords: `ห้าม, สตรีม`
- Missing keywords: `ห้าม, สตรีม`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `cs2_pause_policy` คนละ intent กับที่ถาม (`penalty`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `cs2_pause_policy` แต่คำถามต้องการ intent `penalty`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_pause_policy`
- คำตอบย่อจาก AI: คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 38. [FAIL] competition_cs2_v2_038 - ผิด/ต้องแก้

- คำถาม: CS2 พฤติกรรมเหยียดหรือวาจาสร้างความเกลียดชังผิดกติกาไหม
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:no_answer`
- Retrieved: `Reservation`
- Expected keywords: `ห้าม, เกลียดชัง`
- Missing keywords: `ห้าม, เกลียดชัง`
- Missing source: `competition_rules_cs2_psu_phuket_2026`
- สาเหตุ: `no_answer_despite_data` - Route เข้า competition_rules แล้ว แต่ retrieval/fact card ไม่เจอ context ที่มั่นใจพอ จึงตอบไม่พบข้อมูล
- ปัญหา: ระบบตอบไม่พบข้อมูล ทั้งที่ข้อมูลน่าจะอยู่ใน competition chunks
- ลักษณะคำตอบ: ตอบว่าไม่พบข้อมูล ทั้งที่หลายข้อมีข้อมูลอยู่ใน competition chunks แต่ pipeline ดึงไม่ถึง
- คำตอบย่อจาก AI: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด competition_rules ตอนนี้ครับ
- แนวแก้: ให้ fallback ไปค้น `competition_rule_chunks.jsonl` และใช้ RAG/LLM สรุปเมื่อ fact card ไม่ครอบคลุม

### 39. [FAIL] competition_cs2_v2_039 - ผิด/ต้องแก้

- คำถาม: CS2 นำคีย์บอร์ดเมาส์ส่วนตัวไปเองได้ไหม
- Intent ที่คาด: `equipment`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `คีย์บอร์ด, เมาส์, มาเองได้`
- Missing keywords: `คีย์บอร์ด, เมาส์, มาเองได้`
- Missing source: `competition_rules_cs2_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Counter-Strike 2 แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 40. [FAIL] competition_cs2_v2_040 - ผิด/ต้องแก้

- คำถาม: CS2 ผู้จัดเตรียมอุปกรณ์อะไรให้บ้าง
- Intent ที่คาด: `equipment`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_map_pool`
- Expected keywords: `PC, จอภาพ, โต๊ะ, เก้าอี้`
- Missing keywords: `PC, จอภาพ, โต๊ะ, เก้าอี้`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `cs2_map_pool` คนละ intent กับที่ถาม (`equipment`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `cs2_map_pool` แต่คำถามต้องการ intent `equipment`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_map_pool`
- คำตอบย่อจาก AI: คำตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train หลักฐานจากกติกา: - เอกสารระบุ map pool สำหรับการแข่งขัน CS2 ได้แก่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train อ้างอิงจากกติกา: C...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 41. [FAIL] competition_cs2_v2_041 - ผิด/ต้องแก้

- คำถาม: CS2 ปรับ crosshair หรือ resolution ได้ไหม
- Intent ที่คาด: `game_setting`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `Crosshair, Resolution, Brightness`
- Missing keywords: `Crosshair, Resolution, Brightness`
- Missing source: `competition_rules_cs2_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Counter-Strike 2 แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 42. [FAIL] competition_cs2_v2_042 - ผิด/ต้องแก้

- คำถาม: CS2 ใช้ macro หรือ script ได้หรือเปล่า
- Intent ที่คาด: `equipment`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `ห้าม, สคริปต์, มาโคร`
- Missing keywords: `ห้าม, สคริปต์, มาโคร`
- Missing source: `competition_rules_cs2_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Counter-Strike 2 แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 43. [FAIL] competition_cs2_v2_043 - ผิด/ต้องแก้

- คำถาม: CS2 ติดตั้งโปรแกรมเองบนคอมแข่งได้ไหม
- Intent ที่คาด: `equipment`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_pause_policy`
- Expected keywords: `ห้าม, ติดตั้งโปรแกรม`
- Missing keywords: `ห้าม, ติดตั้งโปรแกรม`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `cs2_pause_policy` คนละ intent กับที่ถาม (`equipment`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `cs2_pause_policy` แต่คำถามต้องการ intent `equipment`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_pause_policy`
- คำตอบย่อจาก AI: คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 44. [FAIL] competition_cs2_v2_044 - ผิด/ต้องแก้

- คำถาม: CS2 เข้าโซเชียลบนคอมแข่งได้ไหม
- Intent ที่คาด: `equipment`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_pause_policy`
- Expected keywords: `ห้าม, โซเชียลมีเดีย`
- Missing keywords: `ห้าม, โซเชียลมีเดีย`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `cs2_pause_policy` คนละ intent กับที่ถาม (`equipment`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `cs2_pause_policy` แต่คำถามต้องการ intent `equipment`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_pause_policy`
- คำตอบย่อจาก AI: คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 45. [FAIL] competition_cs2_v2_045 - ผิด/ต้องแก้

- คำถาม: CS2 ช่วงเตรียมตัวมีคนในพื้นที่ได้ไม่เกินกี่คน
- Intent ที่คาด: `area_rules`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `ไม่เกิน 6 คน`
- Missing keywords: `ไม่เกิน 6 คน`
- Missing source: `competition_rules_cs2_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Counter-Strike 2 แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 46. [FAIL] competition_cs2_v2_046 - ผิด/ต้องแก้

- คำถาม: CS2 เอามือถือหรือ smart watch เข้าพื้นที่แข่งได้ไหม
- Intent ที่คาด: `area_rules`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_pause_policy`
- Expected keywords: `ห้าม, โทรศัพท์มือถือ, สมาร์ทวอทช์`
- Missing keywords: `ห้าม, โทรศัพท์มือถือ, สมาร์ทวอทช์`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `cs2_pause_policy` คนละ intent กับที่ถาม (`area_rules`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `cs2_pause_policy` แต่คำถามต้องการ intent `area_rules`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_pause_policy`
- คำตอบย่อจาก AI: คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 47. [FAIL] competition_cs2_v2_047 - ผิด/ต้องแก้

- คำถาม: CS2 หัวหน้าทีมนำเอกสารเข้าไปได้ไหม
- Intent ที่คาด: `area_rules`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `cs2_pause_policy`
- Expected keywords: `หัวหน้าทีม, เอกสาร, กรรมการ`
- Missing keywords: `หัวหน้าทีม, กรรมการ`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `cs2_pause_policy` คนละ intent กับที่ถาม (`area_rules`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `cs2_pause_policy` แต่คำถามต้องการ intent `area_rules`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `cs2_pause_policy`
- คำตอบย่อจาก AI: คำตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที หลักฐานจากกติกา: - เอกสารระบุ Technical Pause ได้ทีมละ 2 ครั้ง ระยะเวลารวมไม่เกิน 10...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 48. [FAIL] competition_cs2_v2_048 - ผิด/ต้องแก้

- คำถาม: CS2 อนุญาตอาหารหรือเครื่องดื่มอะไรในพื้นที่แข่ง
- Intent ที่คาด: `area_rules`
- Route/Mode: `competition_rules` / `pipeline:rag_direct_curated`
- Retrieved: `competition_rules_cs2_psu_phuket_2026_s39_c01, competition_rules_cs2_psu_phuket_2026_s40_c01, competition_rules_cs2_psu_phuket_2026_s42_c01`
- Expected keywords: `น้ำดื่ม, ปิดสนิท, หมากฝรั่ง`
- Missing keywords: `น้ำดื่ม, ปิดสนิท, หมากฝรั่ง`
- Missing source: `-`
- สาเหตุ: `rag_partial_answer` - RAG ดึง source ถูกแต่คำตอบไม่ครบ keyword สำคัญ
- ปัญหา: retrieval ดึงเอกสารถูก แต่ synthesis ยังไม่ตอบ direct answer ให้ครบ
- ลักษณะคำตอบ: ตอบจาก curated/chunk retrieval โดยตรงจาก `competition_rules_cs2_psu_phuket_2026_s39_c01, competition_rules_cs2_psu_phuket_2026_s40_c01, competition_rules_cs2_psu_phuket_2026_s42_c01` อาจตรงบางส่วนหรือดึง source ผิด
- คำตอบย่อจาก AI: คำตอบ: 6. อุปกรณ์และการตั้งค่าเกม รายละเอียดที่เกี่ยวข้อง: - 1. อุปกรณ์ที่อนุญาต - 2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament แหล...
- แนวแก้: ปรับ chunk selection/answer synthesis ให้ตอบ direct answer ก่อน แล้วค่อยรายละเอียด

## Arena of Valor (RoV)

### 49. [FAIL] competition_rov_v2_001 - ผิด/ต้องแก้

- คำถาม: Blueket Games RoV แข่งวันไหน
- Intent ที่คาด: `schedule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_rematch_first_blood`
- Expected keywords: `11 กันยายน 2568`
- Missing keywords: `11 กันยายน 2568`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `rov_rematch_first_blood` คนละ intent กับที่ถาม (`schedule`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `rov_rematch_first_blood` แต่คำถามต้องการ intent `schedule`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_rematch_first_blood`
- คำตอบย่อจาก AI: คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน หลักฐานจากกติกา: - เอกสารระบุเงื่อนไขการขอแข่งขันใหม่ก่อน Fi...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 50. [PASS] competition_rov_v2_002 - ผ่าน

- คำถาม: RoV ลงทะเบียนช่วงกี่โมง
- Intent ที่คาด: `schedule`
- Route/Mode: `general` / `pipeline:rag_direct_curated`
- Retrieved: `competition_rules_rov_blueket_2025_men_s03_c01, competition_rules_cs2_psu_phuket_2026_s12_c01, competition_rules_valorant_psu_phuket_2026_s02_c01`
- Expected keywords: `8.00, 8.30`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบจาก curated/chunk retrieval โดยตรงจาก `competition_rules_rov_blueket_2025_men_s03_c01, competition_rules_cs2_psu_phuket_2026_s12_c01, competition_rules_valorant_psu_phuket_2026_s02_c01` อาจตรงบางส่วนหรือดึง source ผิด
- คำตอบย่อจาก AI: คำตอบ: 1. กำหนดการแข่งขัน รายละเอียดที่เกี่ยวข้อง: - 1.1. แข่งขันออฟไลน์ วันที่ 11 กันยายน 2568 - เวลา 8.00-8.30 ลงทะเบียน - เวลา 8.30-8.40 แบ่งสายการแข่งขัน - เวลา 8.40-10.00 รอบ 5 ทีม แข่งแบบ Single Elimination BO3 อ้า...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 51. [FAIL] competition_rov_v2_003 - ผิด/ต้องแก้

- คำถาม: RoV แบ่งสายการแข่งขันกี่โมง
- Intent ที่คาด: `schedule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_format_bo3_all_rounds`
- Expected keywords: `8.30, 8.40`
- Missing keywords: `8.30, 8.40`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `rov_format_bo3_all_rounds` คนละ intent กับที่ถาม (`schedule`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `rov_format_bo3_all_rounds` แต่คำถามต้องการ intent `schedule`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_format_bo3_all_rounds`
- คำตอบย่อจาก AI: คำตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ หลักฐานจากกติกา: - เอกสารหัวข้อ 3. รูปแบบการแข่งขัน ระบุว่าแข่งแบบออฟไลน์ และแข่ง Best of 3 (BO3) ทุกรอบ อ้างอิงจากกติกา: Arena of Valor (RoV)...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 52. [FAIL] competition_rov_v2_004 - ผิด/ต้องแก้

- คำถาม: RoV รอบ 5 ทีมแข่งช่วงเวลาไหน
- Intent ที่คาด: `schedule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_late_start_forfeit`
- Expected keywords: `8.40, 10.00, BO3`
- Missing keywords: `8.40, 10.00, BO3`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `rov_late_start_forfeit` คนละ intent กับที่ถาม (`schedule`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `rov_late_start_forfeit` แต่คำถามต้องการ intent `schedule`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_late_start_forfeit`
- คำตอบย่อจาก AI: คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น หลักฐานจากกติกา: - เอกสารระบุว่าหากเริ่มการแข่งขันล่าช้าเกิน 15 นาที ทีมที่ทำให้เกิดความล่าช้าจะถูกปรับแพ้ อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket G...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 53. [FAIL] competition_rov_v2_005 - ผิด/ต้องแก้

- คำถาม: RoV รอบรองคู่ที่ 1 เริ่มประมาณกี่โมง
- Intent ที่คาด: `schedule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_format_bo3_all_rounds`
- Expected keywords: `10.00, 11.30`
- Missing keywords: `10.00, 11.30`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `rov_format_bo3_all_rounds` คนละ intent กับที่ถาม (`schedule`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `rov_format_bo3_all_rounds` แต่คำถามต้องการ intent `schedule`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_format_bo3_all_rounds`
- คำตอบย่อจาก AI: คำตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ หลักฐานจากกติกา: - เอกสารหัวข้อ 3. รูปแบบการแข่งขัน ระบุว่าแข่งแบบออฟไลน์ และแข่ง Best of 3 (BO3) ทุกรอบ อ้างอิงจากกติกา: Arena of Valor (RoV)...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 54. [FAIL] competition_rov_v2_006 - ผิด/ต้องแก้

- คำถาม: RoV รอบรองคู่ที่ 2 อยู่ช่วงเวลาไหน
- Intent ที่คาด: `schedule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_format_bo3_all_rounds`
- Expected keywords: `12.30, 14.00`
- Missing keywords: `12.30, 14.00`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `rov_format_bo3_all_rounds` คนละ intent กับที่ถาม (`schedule`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `rov_format_bo3_all_rounds` แต่คำถามต้องการ intent `schedule`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_format_bo3_all_rounds`
- คำตอบย่อจาก AI: คำตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ หลักฐานจากกติกา: - เอกสารหัวข้อ 3. รูปแบบการแข่งขัน ระบุว่าแข่งแบบออฟไลน์ และแข่ง Best of 3 (BO3) ทุกรอบ อ้างอิงจากกติกา: Arena of Valor (RoV)...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 55. [FAIL] competition_rov_v2_007 - ผิด/ต้องแก้

- คำถาม: RoV รอบชิงอันดับ 3 แข่งกี่โมงถึงกี่โมง
- Intent ที่คาด: `schedule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_format_bo3_all_rounds`
- Expected keywords: `14.00, 15.30`
- Missing keywords: `14.00, 15.30`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `rov_format_bo3_all_rounds` คนละ intent กับที่ถาม (`schedule`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `rov_format_bo3_all_rounds` แต่คำถามต้องการ intent `schedule`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_format_bo3_all_rounds`
- คำตอบย่อจาก AI: คำตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ หลักฐานจากกติกา: - เอกสารหัวข้อ 3. รูปแบบการแข่งขัน ระบุว่าแข่งแบบออฟไลน์ และแข่ง Best of 3 (BO3) ทุกรอบ อ้างอิงจากกติกา: Arena of Valor (RoV)...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 56. [FAIL] competition_rov_v2_008 - ผิด/ต้องแก้

- คำถาม: RoV รอบชิงชนะเลิศแข่งช่วงไหน
- Intent ที่คาด: `schedule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_format_bo3_all_rounds`
- Expected keywords: `15.30, 17.00`
- Missing keywords: `15.30, 17.00`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `rov_format_bo3_all_rounds` คนละ intent กับที่ถาม (`schedule`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `rov_format_bo3_all_rounds` แต่คำถามต้องการ intent `schedule`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_format_bo3_all_rounds`
- คำตอบย่อจาก AI: คำตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ หลักฐานจากกติกา: - เอกสารหัวข้อ 3. รูปแบบการแข่งขัน ระบุว่าแข่งแบบออฟไลน์ และแข่ง Best of 3 (BO3) ทุกรอบ อ้างอิงจากกติกา: Arena of Valor (RoV)...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 57. [FAIL] competition_rov_v2_009 - ผิด/ต้องแก้

- คำถาม: RoV แข่งที่อาคารไหนของ PSU Esports Studio Phuket
- Intent ที่คาด: `schedule_location`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_pause_disconnect`
- Expected keywords: `อาคาร 5, ชั้น 1`
- Missing keywords: `อาคาร 5, ชั้น 1`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `rov_pause_disconnect` คนละ intent กับที่ถาม (`schedule_location`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `rov_pause_disconnect` แต่คำถามต้องการ intent `schedule_location`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_pause_disconnect`
- คำตอบย่อจาก AI: คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 58. [PASS] competition_rov_v2_010 - ผ่าน

- คำถาม: RoV แข่งออนไลน์หรือออฟไลน์
- Intent ที่คาด: `format`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_format_bo3_all_rounds`
- Expected keywords: `ออฟไลน์`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_format_bo3_all_rounds`
- คำตอบย่อจาก AI: คำตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ หลักฐานจากกติกา: - เอกสารหัวข้อ 3. รูปแบบการแข่งขัน ระบุว่าแข่งแบบออฟไลน์ และแข่ง Best of 3 (BO3) ทุกรอบ อ้างอิงจากกติกา: Arena of Valor (RoV)...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 59. [PASS] competition_rov_v2_011 - ผ่าน

- คำถาม: แข่ง ROV ต้องเล่นกี่เกม
- Intent ที่คาด: `format`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_format_bo3_all_rounds`
- Expected keywords: `BO3, ทุกรอบ`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_format_bo3_all_rounds`
- คำตอบย่อจาก AI: คำตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ หลักฐานจากกติกา: - เอกสารหัวข้อ 3. รูปแบบการแข่งขัน ระบุว่าแข่งแบบออฟไลน์ และแข่ง Best of 3 (BO3) ทุกรอบ อ้างอิงจากกติกา: Arena of Valor (RoV)...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 60. [PASS] competition_rov_v2_012 - ผ่าน

- คำถาม: RoV รายการนี้เป็น Best of 3 ทุกด่านไหม
- Intent ที่คาด: `format`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_format_bo3_all_rounds`
- Expected keywords: `Best of 3, ทุกรอบ`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_format_bo3_all_rounds`
- คำตอบย่อจาก AI: คำตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ หลักฐานจากกติกา: - เอกสารหัวข้อ 3. รูปแบบการแข่งขัน ระบุว่าแข่งแบบออฟไลน์ และแข่ง Best of 3 (BO3) ทุกรอบ อ้างอิงจากกติกา: Arena of Valor (RoV)...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 61. [FAIL] competition_rov_v2_013 - ผิด/ต้องแก้

- คำถาม: RoV เกมแรกใครได้ฝั่งสีน้ำเงิน
- Intent ที่คาด: `side_selection`
- Route/Mode: `games` / `pipeline:rag_direct_curated`
- Retrieved: `curated_home_popular_games_list, curated_games_popular, curated_games_cockpit`
- Expected keywords: `ด้านบน, สายการแข่งขัน, สีน้ำเงิน`
- Missing keywords: `ด้านบน, สายการแข่งขัน, สีน้ำเงิน`
- Missing source: `competition_rules_rov_blueket_2025_men`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Arena of Valor (RoV) แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบจาก curated/chunk retrieval โดยตรงจาก `curated_home_popular_games_list, curated_games_popular, curated_games_cockpit` อาจตรงบางส่วนหรือดึง source ผิด
- คำตอบย่อจาก AI: เกมยอดนิยมที่ปรากฏบนหน้า Home ได้แก่ Gran Turismo 7, Mario Kart 8 Deluxe, Tekken 8 และ Beat Saber แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home, https://esports.computing.psu.ac.th/
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 62. [FAIL] competition_rov_v2_014 - ผิด/ต้องแก้

- คำถาม: RoV เกมถัดไปใครเลือกฝั่ง
- Intent ที่คาด: `side_selection`
- Route/Mode: `games` / `pipeline:rag_direct_curated`
- Retrieved: `curated_games_cockpit, curated_home_popular_games_list, curated_games_pc`
- Expected keywords: `ผู้ที่แพ้, เลือกฝั่ง`
- Missing keywords: `ผู้ที่แพ้, เลือกฝั่ง`
- Missing source: `competition_rules_rov_blueket_2025_men`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Arena of Valor (RoV) แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบจาก curated/chunk retrieval โดยตรงจาก `curated_games_cockpit, curated_home_popular_games_list, curated_games_pc` อาจตรงบางส่วนหรือดึง source ผิด
- คำตอบย่อจาก AI: Cockpit ใช้เล่นเกม Gran Turismo 7 (Single Player) ได้ โดยปรากฏในรายการบริการ Cockpit #1 (1 Person) 60 min ของระบบจอง แหล่งข้อมูล: https://esports.computing.psu.ac.th/, https://esports.phuket.psu.ac.th/home
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 63. [FAIL] competition_rov_v2_015 - ผิด/ต้องแก้

- คำถาม: กรรมการ RoV แจ้งอะไรให้ทีมเข้าห้องแข่ง
- Intent ที่คาด: `match_process`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_device_mobile_only`
- Expected keywords: `หมายเลขห้อง`
- Missing keywords: `หมายเลขห้อง`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `rov_device_mobile_only` คนละ intent กับที่ถาม (`match_process`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `rov_device_mobile_only` แต่คำถามต้องการ intent `match_process`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_device_mobile_only`
- คำตอบย่อจาก AI: คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad หลักฐานจากกติกา: - เอกสารระบุให้ใช้โทรศัพท์มือถือ และไม่อนุญาตให้ใช้ Tablet/iPad ในการแข่งขัน อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Game...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 64. [PASS] competition_rov_v2_016 - ผ่าน

- คำถาม: RoV มาสายเกิน 15 นาทีเป็นอะไร
- Intent ที่คาด: `late_start`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_late_start_forfeit`
- Expected keywords: `15 นาที, ปรับแพ้`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_late_start_forfeit`
- คำตอบย่อจาก AI: คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น หลักฐานจากกติกา: - เอกสารระบุว่าหากเริ่มการแข่งขันล่าช้าเกิน 15 นาที ทีมที่ทำให้เกิดความล่าช้าจะถูกปรับแพ้ อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket G...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 65. [PASS] competition_rov_v2_017 - ผ่าน

- คำถาม: กติกา RoV ถ้าเริ่มแข่งช้าเกินเวลาที่กำหนดลงโทษยังไง
- Intent ที่คาด: `late_start`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_late_start_forfeit`
- Expected keywords: `ล่าช้า, ปรับแพ้`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_late_start_forfeit`
- คำตอบย่อจาก AI: คำตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น หลักฐานจากกติกา: - เอกสารระบุว่าหากเริ่มการแข่งขันล่าช้าเกิน 15 นาที ทีมที่ทำให้เกิดความล่าช้าจะถูกปรับแพ้ อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket G...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 66. [FAIL] competition_rov_v2_018 - ผิด/ต้องแก้

- คำถาม: RoV ต้องมีฮีโร่อย่างน้อยกี่ตัว
- Intent ที่คาด: `hero_rule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_team_size_active_players`
- Expected keywords: `18 ตัว`
- Missing keywords: `18 ตัว`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `rov_team_size_active_players` คนละ intent กับที่ถาม (`hero_rule`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `rov_team_size_active_players` แต่คำถามต้องการ intent `hero_rule`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_team_size_active_players`
- คำตอบย่อจาก AI: คำตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้ หลักฐานจากกติกา: - เอกสารระบุการเข้าแข่งขันในโหมดการแข่งขัน 5v5 แต่ไม่...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 67. [FAIL] competition_rov_v2_019 - ผิด/ต้องแก้

- คำถาม: RoV ใช้ระบบแบนเลือกฮีโร่แบบไหน
- Intent ที่คาด: `hero_rule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_format_bo3_all_rounds`
- Expected keywords: `Global Ban/Pick`
- Missing keywords: `Global Ban/Pick`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `rov_format_bo3_all_rounds` คนละ intent กับที่ถาม (`hero_rule`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `rov_format_bo3_all_rounds` แต่คำถามต้องการ intent `hero_rule`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_format_bo3_all_rounds`
- คำตอบย่อจาก AI: คำตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ หลักฐานจากกติกา: - เอกสารหัวข้อ 3. รูปแบบการแข่งขัน ระบุว่าแข่งแบบออฟไลน์ และแข่ง Best of 3 (BO3) ทุกรอบ อ้างอิงจากกติกา: Arena of Valor (RoV)...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 68. [FAIL] competition_rov_v2_020 - ผิด/ต้องแก้

- คำถาม: RoV ใส่รูนและพลังเสริมได้ไหม
- Intent ที่คาด: `hero_rule`
- Route/Mode: `general` / `pipeline:rag_direct_curated`
- Retrieved: `competition_rules_rov_blueket_2025_men_s06_c02, competition_rules_rov_blueket_2025_men_s06_c01, competition_rules_rov_blueket_2025_men_s06_c03`
- Expected keywords: `รูน, พลังเสริม, ตามความต้องการ`
- Missing keywords: `รูน, พลังเสริม, ตามความต้องการ`
- Missing source: `-`
- สาเหตุ: `wrong_route` - Router ไม่มั่นใจพอและปล่อยเป็น general ทำให้ retrieval ไม่เจาะเอกสารการแข่งขัน
- ปัญหา: คำถามควรเป็น competition_rules ของ Arena of Valor (RoV) แต่ถูกส่งไป `general`
- ลักษณะคำตอบ: ตอบจาก curated/chunk retrieval โดยตรงจาก `competition_rules_rov_blueket_2025_men_s06_c02, competition_rules_rov_blueket_2025_men_s06_c01, competition_rules_rov_blueket_2025_men_s06_c03` อาจตรงบางส่วนหรือดึง source ผิด
- คำตอบย่อจาก AI: คำตอบ: 4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพ...
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 69. [FAIL] competition_rov_v2_021 - ผิด/ต้องแก้

- คำถาม: RoV เลือกฮีโร่ซ้ำได้ไหม
- Intent ที่คาด: `hero_rule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_pause_disconnect`
- Expected keywords: `ห้าม, ฮีโร่ซ้ำ`
- Missing keywords: `ห้าม, ฮีโร่ซ้ำ`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `rov_pause_disconnect` คนละ intent กับที่ถาม (`hero_rule`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `rov_pause_disconnect` แต่คำถามต้องการ intent `hero_rule`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_pause_disconnect`
- คำตอบย่อจาก AI: คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 70. [PASS] competition_rov_v2_022 - ผ่าน

- คำถาม: RoV ใช้สกินพิเศษได้หรือเปล่า
- Intent ที่คาด: `skin`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_skin_default_only`
- Expected keywords: `Default Skin`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_skin_default_only`
- คำตอบย่อจาก AI: คำตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น หลักฐานจากกติกา: - เอกสารระบุให้ใช้ Default Skin เท่านั้นสำหรับการแข่งขัน อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย แหล่งข้อมูล: local://competit...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 71. [PASS] competition_rov_v2_023 - ผ่าน

- คำถาม: RoV แต่ละทีม pause ได้กี่ครั้ง ครั้งละเท่าไหร่
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_pause_disconnect`
- Expected keywords: `5 ครั้ง, 1 นาที`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_pause_disconnect`
- คำตอบย่อจาก AI: คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 72. [FAIL] competition_rov_v2_024 - ผิด/ต้องแก้

- คำถาม: RoV ถ้า pause เกิน 1 นาทีอีกทีมทำอะไรได้
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_pause_disconnect`
- Expected keywords: `Resume`
- Missing keywords: `Resume`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_pause_disconnect`
- คำตอบย่อจาก AI: คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 73. [FAIL] competition_rov_v2_025 - ผิด/ต้องแก้

- คำถาม: RoV หลุดเพราะเน็ตล่มหรือเซิร์ฟเวอร์พังต้องทำยังไง
- Intent ที่คาด: `rematch`
- Route/Mode: `general` / `pipeline:no_answer`
- Retrieved: `Reservation`
- Expected keywords: `แจ้งทีมงาน, ดุลยพินิจ, กรรมการ`
- Missing keywords: `แจ้งทีมงาน, ดุลยพินิจ, กรรมการ`
- Missing source: `competition_rules_rov_blueket_2025_men`
- สาเหตุ: `wrong_route` - Router ไม่มั่นใจพอและปล่อยเป็น general ทำให้ retrieval ไม่เจาะเอกสารการแข่งขัน
- ปัญหา: คำถามควรเป็น competition_rules ของ Arena of Valor (RoV) แต่ถูกส่งไป `general`
- ลักษณะคำตอบ: ตอบว่าไม่พบข้อมูล ทั้งที่หลายข้อมีข้อมูลอยู่ใน competition chunks แต่ pipeline ดึงไม่ถึง
- คำตอบย่อจาก AI: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 74. [FAIL] competition_rov_v2_026 - ผิด/ต้องแก้

- คำถาม: RoV ขอเริ่มเกมใหม่ได้ตอนไหนก่อน First Blood
- Intent ที่คาด: `rematch`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_rematch_first_blood`
- Expected keywords: `First Blood, 2 นาที, เริ่มเกมใหม่`
- Missing keywords: `เริ่มเกมใหม่`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_rematch_first_blood`
- คำตอบย่อจาก AI: คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน หลักฐานจากกติกา: - เอกสารระบุเงื่อนไขการขอแข่งขันใหม่ก่อน Fi...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 75. [FAIL] competition_rov_v2_027 - ผิด/ต้องแก้

- คำถาม: RoV ถ้าเกิด First Blood แล้วขอ remake ได้ไหม
- Intent ที่คาด: `rematch`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_rematch_first_blood`
- Expected keywords: `First Blood, อนุญาต, คู่แข่ง, กรรมการ`
- Missing keywords: `อนุญาต, คู่แข่ง, กรรมการ`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_rematch_first_blood`
- คำตอบย่อจาก AI: คำตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน หลักฐานจากกติกา: - เอกสารระบุเงื่อนไขการขอแข่งขันใหม่ก่อน Fi...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 76. [FAIL] competition_rov_v2_028 - ผิด/ต้องแก้

- คำถาม: RoV เจตนากด pause ก่อกวนโดนอะไร
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_pause_disconnect`
- Expected keywords: `ปรับแพ้, ตัดสิทธิ์`
- Missing keywords: `ปรับแพ้, ตัดสิทธิ์`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_pause_disconnect`
- คำตอบย่อจาก AI: คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 77. [FAIL] competition_rov_v2_029 - ผิด/ต้องแก้

- คำถาม: RoV พักหลังจบทุกสองเกมกี่นาที
- Intent ที่คาด: `break_time`
- Route/Mode: `games` / `pipeline:rag_direct_curated`
- Retrieved: `curated_home_popular_games_list, curated_games_cockpit, curated_games_pc`
- Expected keywords: `5 นาที`
- Missing keywords: `5 นาที`
- Missing source: `competition_rules_rov_blueket_2025_men`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Arena of Valor (RoV) แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบจาก curated/chunk retrieval โดยตรงจาก `curated_home_popular_games_list, curated_games_cockpit, curated_games_pc` อาจตรงบางส่วนหรือดึง source ผิด
- คำตอบย่อจาก AI: เกมยอดนิยมที่ปรากฏบนหน้า Home ได้แก่ Gran Turismo 7, Mario Kart 8 Deluxe, Tekken 8 และ Beat Saber แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home, https://esports.computing.psu.ac.th/
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 78. [FAIL] competition_rov_v2_030 - ผิด/ต้องแก้

- คำถาม: RoV ไม่กลับมาหลังเวลาพักที่กำหนดเสี่ยงอะไร
- Intent ที่คาด: `break_time`
- Route/Mode: `schedule` / `pipeline:schedule_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `ปรับ, แพ้`
- Missing keywords: `ปรับ, แพ้`
- Missing source: `competition_rules_rov_blueket_2025_men`
- สาเหตุ: `wrong_route` - Router จัดเป็น schedule ของศูนย์ เพราะเจอคำถามเวลา/รอบ ทำให้ตอบเวลาเปิด-ปิดศูนย์แทนตารางแข่งขัน
- ปัญหา: คำถามควรเป็น competition_rules ของ Arena of Valor (RoV) แต่ถูกส่งไป `schedule`
- ลักษณะคำตอบ: ตอบเป็นเวลาเปิด-ปิด/ตารางบริการของศูนย์ ทำให้หลุดจากตารางหรือกติกาการแข่งขัน
- คำตอบย่อจาก AI: เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน รายละเอียดจากตาราง: - Morning คือ 09:00-12:00 - Afternoon คือ 13:00-16:00 - Monday ช่วง Morning 09:00-12:00 เป็น Maint...
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 79. [FAIL] competition_rov_v2_031 - ผิด/ต้องแก้

- คำถาม: RoV เกมหยุดเกิน 10 นาทีทีมงานทำอะไรได้
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_pause_disconnect`
- Expected keywords: `10 นาที, เริ่มเกมใหม่`
- Missing keywords: `10 นาที, เริ่มเกมใหม่`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_pause_disconnect`
- คำตอบย่อจาก AI: คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 80. [PASS] competition_rov_v2_032 - ผ่าน

- คำถาม: RoV เครื่องร้อนพักได้กี่นาที
- Intent ที่คาด: `pause`
- Route/Mode: `general` / `pipeline:rag_direct_curated`
- Retrieved: `competition_rules_rov_blueket_2025_men_s06_c04, competition_rules_tekken8_psu_esports_s02_c01, competition_rules_valorant_psu_phuket_2026_s02_c01`
- Expected keywords: `เครื่องร้อน, 5 นาที`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบจาก curated/chunk retrieval โดยตรงจาก `competition_rules_rov_blueket_2025_men_s06_c04, competition_rules_tekken8_psu_esports_s02_c01, competition_rules_valorant_psu_phuket_2026_s02_c01` อาจตรงบางส่วนหรือดึง source ผิด
- คำตอบย่อจาก AI: คำตอบ: 4.5.6.1.2. อุปกรณ์พกพาหรือซอฟต์แวร์ทำงานผิดปกติ รายละเอียดที่เกี่ยวข้อง: - 4.6.1.การหยุดพักเกมอันเนื่องมากจากปัญหาเครื่องร้อนของอุปกรณ์พกพา - 4.6.1.1. ทางทีมงานอาจสั่งให้หยุดพักเกมเป็นเวลาไม่เกินกว่า 5 นาที เพื่อท...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 81. [FAIL] competition_rov_v2_033 - ผิด/ต้องแก้

- คำถาม: RoV ระหว่าง pause ผู้เล่นคุยกันได้ไหม
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_pause_disconnect`
- Expected keywords: `ห้าม, สื่อสาร`
- Missing keywords: `ห้าม, สื่อสาร`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_pause_disconnect`
- คำตอบย่อจาก AI: คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 82. [FAIL] competition_rov_v2_034 - ผิด/ต้องแก้

- คำถาม: RoV บทลงโทษการ pause ผิดครั้งแรกคืออะไร
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_pause_disconnect`
- Expected keywords: `ครั้งที่ 1, ตักเตือน`
- Missing keywords: `ครั้งที่ 1, ตักเตือน`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_pause_disconnect`
- คำตอบย่อจาก AI: คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 83. [FAIL] competition_rov_v2_035 - ผิด/ต้องแก้

- คำถาม: RoV pause ผิดครั้งที่ 2 โดนอะไร
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_pause_disconnect`
- Expected keywords: `ครั้งที่ 2, เพิ่มสิทธิการแบนฮีโร่, 1 ครั้ง`
- Missing keywords: `ครั้งที่ 2, เพิ่มสิทธิการแบนฮีโร่, 1 ครั้ง`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_pause_disconnect`
- คำตอบย่อจาก AI: คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 84. [FAIL] competition_rov_v2_036 - ผิด/ต้องแก้

- คำถาม: RoV pause ผิดครั้งที่ 3 โดนอะไร
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_pause_disconnect`
- Expected keywords: `ครั้งที่ 3, เพิ่มสิทธิการแบนฮีโร่, 2 ครั้ง`
- Missing keywords: `ครั้งที่ 3, เพิ่มสิทธิการแบนฮีโร่, 2 ครั้ง`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_pause_disconnect`
- คำตอบย่อจาก AI: คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 85. [PASS] competition_rov_v2_037 - ผ่าน

- คำถาม: RoV ใช้อุปกรณ์อะไรแข่ง
- Intent ที่คาด: `equipment`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_device_mobile_only`
- Expected keywords: `โทรศัพท์มือถือ`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_device_mobile_only`
- คำตอบย่อจาก AI: คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad หลักฐานจากกติกา: - เอกสารระบุให้ใช้โทรศัพท์มือถือ และไม่อนุญาตให้ใช้ Tablet/iPad ในการแข่งขัน อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Game...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 86. [PASS] competition_rov_v2_038 - ผ่าน

- คำถาม: RoV ใช้ iPad หรือ Tablet ลงแข่งได้ไหม
- Intent ที่คาด: `equipment`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_device_mobile_only`
- Expected keywords: `ไม่อนุญาต, Tablet, iPad`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_device_mobile_only`
- คำตอบย่อจาก AI: คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad หลักฐานจากกติกา: - เอกสารระบุให้ใช้โทรศัพท์มือถือ และไม่อนุญาตให้ใช้ Tablet/iPad ในการแข่งขัน อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Game...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 87. [FAIL] competition_rov_v2_039 - ผิด/ต้องแก้

- คำถาม: RoV เอาปลั๊กพ่วงกับอุปกรณ์ชาร์จส่วนตัวได้ไหม
- Intent ที่คาด: `equipment`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_device_mobile_only`
- Expected keywords: `ปลั๊กพ่วง, อุปกรณ์ชาร์จ`
- Missing keywords: `ปลั๊กพ่วง, อุปกรณ์ชาร์จ`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `rov_device_mobile_only` คนละ intent กับที่ถาม (`equipment`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `rov_device_mobile_only` แต่คำถามต้องการ intent `equipment`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_device_mobile_only`
- คำตอบย่อจาก AI: คำตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad หลักฐานจากกติกา: - เอกสารระบุให้ใช้โทรศัพท์มือถือ และไม่อนุญาตให้ใช้ Tablet/iPad ในการแข่งขัน อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Game...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 88. [FAIL] competition_rov_v2_040 - ผิด/ต้องแก้

- คำถาม: RoV ใช้คำพูดไม่สุภาพหรือเสียดสีโดนอะไร
- Intent ที่คาด: `penalty`
- Route/Mode: `rules` / `pipeline:rules_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `ปรับแพ้, เกมที่พบ`
- Missing keywords: `ปรับแพ้, เกมที่พบ`
- Missing source: `competition_rules_rov_blueket_2025_men`
- สาเหตุ: `wrong_route` - Router จัดเป็น rules ทั่วไปของศูนย์ ไม่ใช่ competition_rules
- ปัญหา: คำถามควรเป็น competition_rules ของ Arena of Valor (RoV) แต่ถูกส่งไป `rules`
- ลักษณะคำตอบ: ตอบจาก rulebase กฎทั่วไปของศูนย์ ไม่ใช่กฎการแข่งขันของเกมนั้น
- คำตอบย่อจาก AI: กรุณางดส่งเสียงดังเกินควร และห้ามพูดจาดูหมิ่นหรือเสียดสีผู้อื่น แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 89. [FAIL] competition_rov_v2_041 - ผิด/ต้องแก้

- คำถาม: RoV ส่งผลการแข่งขันเท็จโดนลงโทษยังไง
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_format_bo3_all_rounds`
- Expected keywords: `ปรับแพ้, ตัดสิทธิ์`
- Missing keywords: `ปรับแพ้, ตัดสิทธิ์`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `rov_format_bo3_all_rounds` คนละ intent กับที่ถาม (`penalty`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `rov_format_bo3_all_rounds` แต่คำถามต้องการ intent `penalty`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_format_bo3_all_rounds`
- คำตอบย่อจาก AI: คำตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ หลักฐานจากกติกา: - เอกสารหัวข้อ 3. รูปแบบการแข่งขัน ระบุว่าแข่งแบบออฟไลน์ และแข่ง Best of 3 (BO3) ทุกรอบ อ้างอิงจากกติกา: Arena of Valor (RoV)...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 90. [FAIL] competition_rov_v2_042 - ผิด/ต้องแก้

- คำถาม: RoV ให้คนอื่นที่ไม่ได้ลงทะเบียนมาแข่งแทนได้ไหม
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:no_answer`
- Retrieved: `Reservation`
- Expected keywords: `ไม่ตรงตามที่ลงทะเบียน, ปรับแพ้, ตัดสิทธิ์`
- Missing keywords: `ไม่ตรงตามที่ลงทะเบียน, ปรับแพ้, ตัดสิทธิ์`
- Missing source: `competition_rules_rov_blueket_2025_men`
- สาเหตุ: `no_answer_despite_data` - Route เข้า competition_rules แล้ว แต่ retrieval/fact card ไม่เจอ context ที่มั่นใจพอ จึงตอบไม่พบข้อมูล
- ปัญหา: ระบบตอบไม่พบข้อมูล ทั้งที่ข้อมูลน่าจะอยู่ใน competition chunks
- ลักษณะคำตอบ: ตอบว่าไม่พบข้อมูล ทั้งที่หลายข้อมีข้อมูลอยู่ใน competition chunks แต่ pipeline ดึงไม่ถึง
- คำตอบย่อจาก AI: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด competition_rules ตอนนี้ครับ
- แนวแก้: ให้ fallback ไปค้น `competition_rule_chunks.jsonl` และใช้ RAG/LLM สรุปเมื่อ fact card ไม่ครอบคลุม

### 91. [FAIL] competition_rov_v2_043 - ผิด/ต้องแก้

- คำถาม: RoV ห้ามให้คนอื่นเล่นแทนตัวเองไหม
- Intent ที่คาด: `penalty`
- Route/Mode: `rules` / `pipeline:rag_direct_curated`
- Retrieved: `curated_rule_weapons_gambling, curated_rule_noise_language, curated_rule_power_outlet`
- Expected keywords: `เล่นแทน, ห้าม`
- Missing keywords: `เล่นแทน`
- Missing source: `competition_rules_rov_blueket_2025_men`
- สาเหตุ: `wrong_route` - Router จัดเป็น rules ทั่วไปของศูนย์ ไม่ใช่ competition_rules
- ปัญหา: คำถามควรเป็น competition_rules ของ Arena of Valor (RoV) แต่ถูกส่งไป `rules`
- ลักษณะคำตอบ: ตอบจาก curated/chunk retrieval โดยตรงจาก `curated_rule_weapons_gambling, curated_rule_noise_language, curated_rule_power_outlet` อาจตรงบางส่วนหรือดึง source ผิด
- คำตอบย่อจาก AI: ห้ามพกอาวุธหรือของมีคม ห้ามทะเลาะวิวาท และห้ามเล่นการพนัน แหล่งข้อมูล: https://esports.computing.psu.ac.th/
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 92. [FAIL] competition_rov_v2_044 - ผิด/ต้องแก้

- คำถาม: RoV ถามสรุปรูปแบบแข่งกับสถานที่แบบสั้นๆ
- Intent ที่คาด: `summary`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_format_bo3_all_rounds`
- Expected keywords: `ออฟไลน์, BO3, PSU Esports Studio`
- Missing keywords: `ออฟไลน์, PSU Esports Studio`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_format_bo3_all_rounds`
- คำตอบย่อจาก AI: คำตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 93. [FAIL] competition_rov_v2_045 - ผิด/ต้องแก้

- คำถาม: RoV ถ้าถามเรื่องเวลาแข่งทั้งวันควรตอบหัวข้ออะไรบ้าง
- Intent ที่คาด: `schedule`
- Route/Mode: `competition_rules` / `pipeline:no_answer`
- Retrieved: `Reservation`
- Expected keywords: `ลงทะเบียน, รอบรอง, รอบชิง`
- Missing keywords: `ลงทะเบียน, รอบรอง, รอบชิง`
- Missing source: `competition_rules_rov_blueket_2025_men`
- สาเหตุ: `no_answer_despite_data` - Route เข้า competition_rules แล้ว แต่ retrieval/fact card ไม่เจอ context ที่มั่นใจพอ จึงตอบไม่พบข้อมูล
- ปัญหา: ระบบตอบไม่พบข้อมูล ทั้งที่ข้อมูลน่าจะอยู่ใน competition chunks
- ลักษณะคำตอบ: ตอบว่าไม่พบข้อมูล ทั้งที่หลายข้อมีข้อมูลอยู่ใน competition chunks แต่ pipeline ดึงไม่ถึง
- คำตอบย่อจาก AI: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด competition_rules ตอนนี้ครับ
- แนวแก้: ให้ fallback ไปค้น `competition_rule_chunks.jsonl` และใช้ RAG/LLM สรุปเมื่อ fact card ไม่ครอบคลุม

### 94. [FAIL] competition_rov_v2_046 - ผิด/ต้องแก้

- คำถาม: RoV ขอกฎ disconnect แบบเข้าใจง่าย
- Intent ที่คาด: `rematch`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_pause_disconnect`
- Expected keywords: `pause, First Blood, 2 นาที`
- Missing keywords: `pause, First Blood, 2 นาที`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_pause_disconnect`
- คำตอบย่อจาก AI: คำตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมีสิทธิ์ขอหยุดเกม 5 ครั้ง ครั้งละไม่เกิน 1 นาที กรณีเกิดปัญหาเช่นหลุดเกมห...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 95. [PASS] competition_rov_v2_047 - ผ่าน

- คำถาม: RoV มีข้อมูลตัวสำรองชัดเจนไหมในไฟล์นี้
- Intent ที่คาด: `team_size`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_team_size_active_players`
- Expected keywords: `5v5`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_team_size_active_players`
- คำตอบย่อจาก AI: คำตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้ หลักฐานจากกติกา: - เอกสารระบุการเข้าแข่งขันในโหมดการแข่งขัน 5v5 แต่ไม่...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 96. [PASS] competition_rov_v2_048 - ผ่าน

- คำถาม: สมาชิกในทีม ROV ต้องเล่นพร้อมกันฝั่งละกี่คน
- Intent ที่คาด: `team_size`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `rov_team_size_active_players`
- Expected keywords: `5v5, ฝ่ายละ 5 คน`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `rov_team_size_active_players`
- คำตอบย่อจาก AI: คำตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้ หลักฐานจากกติกา: - เอกสารระบุการเข้าแข่งขันในโหมดการแข่งขัน 5v5 แต่ไม่...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

## VALORANT

### 97. [PASS] competition_valorant_v2_001 - ผ่าน

- คำถาม: VALORANT ทีมละกี่คน
- Intent ที่คาด: `team_size`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_team_size_players`
- Expected keywords: `5 คน`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_team_size_players`
- คำตอบย่อจาก AI: คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน หลักฐานจากกติกา: - เอกสารการแข่งขัน VALORANT ระบุการแข่งขันแบบทีม 5 คนต่อทีม อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament แหล่งข้อมูล: local://competition_...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 98. [PASS] competition_valorant_v2_002 - ผ่าน

- คำถาม: วาโลต้องส่งผู้เล่นตัวจริงกี่คน
- Intent ที่คาด: `team_size`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_team_size_players`
- Expected keywords: `ตัวจริง 5 คน`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_team_size_players`
- คำตอบย่อจาก AI: คำตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน หลักฐานจากกติกา: - เอกสารการแข่งขัน VALORANT ระบุการแข่งขันแบบทีม 5 คนต่อทีม อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament แหล่งข้อมูล: local://competition_...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 99. [FAIL] competition_valorant_v2_003 - ผิด/ต้องแก้

- คำถาม: VALORANT Match Prep มีคนได้ไม่เกินกี่คน
- Intent ที่คาด: `area_rules`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `ไม่เกิน 6`
- Missing keywords: `ไม่เกิน 6`
- Missing source: `competition_rules_valorant_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ VALORANT แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 100. [FAIL] competition_valorant_v2_004 - ผิด/ต้องแก้

- คำถาม: VALORANT เอามือถือเข้าพื้นที่แข่งได้ไหม
- Intent ที่คาด: `area_rules`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_agent_map_restriction`
- Expected keywords: `ห้าม, โทรศัพท์มือถือ`
- Missing keywords: `ห้าม, โทรศัพท์มือถือ`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `valorant_agent_map_restriction` คนละ intent กับที่ถาม (`area_rules`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `valorant_agent_map_restriction` แต่คำถามต้องการ intent `area_rules`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_agent_map_restriction`
- คำตอบย่อจาก AI: คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง หลักฐานจากกติกา: - เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์ อ้างอิงจาก...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 101. [FAIL] competition_valorant_v2_005 - ผิด/ต้องแก้

- คำถาม: VALORANT หัวหน้าทีมนำโน้ตเข้าได้ไหม
- Intent ที่คาด: `area_rules`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_emergency_pause`
- Expected keywords: `หัวหน้าทีม, กรรมการ`
- Missing keywords: `หัวหน้าทีม, กรรมการ`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `valorant_emergency_pause` คนละ intent กับที่ถาม (`area_rules`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `valorant_emergency_pause` แต่คำถามต้องการ intent `area_rules`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_emergency_pause`
- คำตอบย่อจาก AI: คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 102. [FAIL] competition_valorant_v2_006 - ผิด/ต้องแก้

- คำถาม: VALORANT อาหารเครื่องดื่มที่อนุญาตมีอะไร
- Intent ที่คาด: `area_rules`
- Route/Mode: `rules` / `pipeline:rules_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `น้ำดื่ม, ปิดสนิท, หมากฝรั่ง`
- Missing keywords: `น้ำดื่ม, ปิดสนิท, หมากฝรั่ง`
- Missing source: `competition_rules_valorant_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็น rules ทั่วไปของศูนย์ ไม่ใช่ competition_rules
- ปัญหา: คำถามควรเป็น competition_rules ของ VALORANT แต่ถูกส่งไป `rules`
- ลักษณะคำตอบ: ตอบจาก rulebase กฎทั่วไปของศูนย์ ไม่ใช่กฎการแข่งขันของเกมนั้น
- คำตอบย่อจาก AI: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 103. [FAIL] competition_valorant_v2_007 - ผิด/ต้องแก้

- คำถาม: VALORANT ต้องมารายงานตัวก่อนแข่งกี่นาที
- Intent ที่คาด: `checkin`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_agent_map_restriction`
- Expected keywords: `30 นาที`
- Missing keywords: `30 นาที`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `valorant_agent_map_restriction` คนละ intent กับที่ถาม (`checkin`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `valorant_agent_map_restriction` แต่คำถามต้องการ intent `checkin`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_agent_map_restriction`
- คำตอบย่อจาก AI: คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง หลักฐานจากกติกา: - เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์ อ้างอิงจาก...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 104. [PASS] competition_valorant_v2_008 - ผ่าน

- คำถาม: วาโล agent ใหม่ใช้ได้ทันทีไหม
- Intent ที่คาด: `character`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_agent_map_restriction`
- Expected keywords: `Agent, 2 สัปดาห์`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_agent_map_restriction`
- คำตอบย่อจาก AI: คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง หลักฐานจากกติกา: - เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์ อ้างอิงจาก...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 105. [PASS] competition_valorant_v2_009 - ผ่าน

- คำถาม: VALORANT แผนที่ใหม่ต้องรอกี่สัปดาห์ก่อนใช้แข่ง
- Intent ที่คาด: `map_pool`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_agent_map_restriction`
- Expected keywords: `4 สัปดาห์`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_agent_map_restriction`
- คำตอบย่อจาก AI: คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง หลักฐานจากกติกา: - เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์ อ้างอิงจาก...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 106. [FAIL] competition_valorant_v2_010 - ผิด/ต้องแก้

- คำถาม: VALORANT ต้องปิด setting อะไรก่อนแข่ง
- Intent ที่คาด: `game_setting`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_agent_map_restriction`
- Expected keywords: `เลือด, ศพ, OFF`
- Missing keywords: `เลือด, ศพ, OFF`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `valorant_agent_map_restriction` คนละ intent กับที่ถาม (`game_setting`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `valorant_agent_map_restriction` แต่คำถามต้องการ intent `game_setting`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_agent_map_restriction`
- คำตอบย่อจาก AI: คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง หลักฐานจากกติกา: - เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์ อ้างอิงจาก...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 107. [FAIL] competition_valorant_v2_011 - ผิด/ต้องแก้

- คำถาม: VALORANT เปิดกราฟ FPS หรือ latency ระหว่างแข่งได้ไหม
- Intent ที่คาด: `game_setting`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_agent_map_restriction`
- Expected keywords: `ห้าม, FPS, Latency`
- Missing keywords: `ห้าม, FPS, Latency`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `valorant_agent_map_restriction` คนละ intent กับที่ถาม (`game_setting`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `valorant_agent_map_restriction` แต่คำถามต้องการ intent `game_setting`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_agent_map_restriction`
- คำตอบย่อจาก AI: คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง หลักฐานจากกติกา: - เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์ อ้างอิงจาก...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 108. [FAIL] competition_valorant_v2_012 - ผิด/ต้องแก้

- คำถาม: VALORANT map pool มีทั้งหมดกี่ map และชื่ออะไรบ้าง
- Intent ที่คาด: `map_pool`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_map_pool`
- Expected keywords: `7, Abyss, Sunset`
- Missing keywords: `7`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_map_pool`
- คำตอบย่อจาก AI: คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset หลักฐานจากกติกา: - เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset อ้างอิงจากกติกา: VALORANT /...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 109. [PASS] competition_valorant_v2_013 - ผ่าน

- คำถาม: วาโลมี Haven Lotus Sunset ใน map pool ไหม
- Intent ที่คาด: `map_pool`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_map_pool`
- Expected keywords: `Haven, Lotus, Sunset`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_map_pool`
- คำตอบย่อจาก AI: คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset หลักฐานจากกติกา: - เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset อ้างอิงจากกติกา: VALORANT /...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 110. [FAIL] competition_valorant_v2_014 - ผิด/ต้องแก้

- คำถาม: VALORANT ban map จนเหลือกี่แผนที่
- Intent ที่คาด: `map_pool`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_map_pool`
- Expected keywords: `3 แผนที่`
- Missing keywords: `3 แผนที่`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_map_pool`
- คำตอบย่อจาก AI: คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset หลักฐานจากกติกา: - เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset อ้างอิงจากกติกา: VALORANT /...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 111. [FAIL] competition_valorant_v2_015 - ผิด/ต้องแก้

- คำถาม: VALORANT เลือกฝั่งด้วยวิธีอะไร
- Intent ที่คาด: `side_selection`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `โยนเหรียญ`
- Missing keywords: `โยนเหรียญ`
- Missing source: `competition_rules_valorant_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ VALORANT แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 112. [FAIL] competition_valorant_v2_016 - ผิด/ต้องแก้

- คำถาม: หลังจบแมตช์ VALORANT ใครยืนยันและบันทึกผล
- Intent ที่คาด: `post_match`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `เจ้าหน้าที่, บันทึกผล`
- Missing keywords: `เจ้าหน้าที่, บันทึกผล`
- Missing source: `competition_rules_valorant_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ VALORANT แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 113. [FAIL] competition_valorant_v2_017 - ผิด/ต้องแก้

- คำถาม: VALORANT ถ้า forfeit แผนที่นั้นบันทึกผลเป็นเท่าไหร่
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_map_pool`
- Expected keywords: `13-0`
- Missing keywords: `13-0`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `valorant_map_pool` คนละ intent กับที่ถาม (`penalty`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `valorant_map_pool` แต่คำถามต้องการ intent `penalty`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_map_pool`
- คำตอบย่อจาก AI: คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset หลักฐานจากกติกา: - เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset อ้างอิงจากกติกา: VALORANT /...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 114. [FAIL] competition_valorant_v2_018 - ผิด/ต้องแก้

- คำถาม: VALORANT pause มีกี่ประเภทหลัก
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_emergency_pause`
- Expected keywords: `3, Tactical, Technical, Emergency`
- Missing keywords: `3, Tactical`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_emergency_pause`
- คำตอบย่อจาก AI: คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 115. [PASS] competition_valorant_v2_019 - ผ่าน

- คำถาม: VALORANT tactical timeout ได้กี่ครั้งต่อแผนที่
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_tactical_timeout`
- Expected keywords: `2, ต่อแผนที่`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_tactical_timeout`
- คำตอบย่อจาก AI: คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง หลักฐานจากกติกา: - เอกสารระบุ Tactical Timeout ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และเมื่อเข...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 116. [PASS] competition_valorant_v2_020 - ผ่าน

- คำถาม: วาโล tactical timeout ครั้งละกี่วินาที
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_tactical_timeout`
- Expected keywords: `60 วินาที`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_tactical_timeout`
- คำตอบย่อจาก AI: คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง หลักฐานจากกติกา: - เอกสารระบุ Tactical Timeout ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และเมื่อเข...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 117. [PASS] competition_valorant_v2_021 - ผ่าน

- คำถาม: VALORANT overtime ได้ timeout เพิ่มไหม
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_tactical_timeout`
- Expected keywords: `Overtime, เพิ่ม, 1 ครั้ง`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_tactical_timeout`
- คำตอบย่อจาก AI: คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง หลักฐานจากกติกา: - เอกสารระบุ Tactical Timeout ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และเมื่อเข...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 118. [FAIL] competition_valorant_v2_022 - ผิด/ต้องแก้

- คำถาม: VALORANT Technical Pause ใช้กรณีไหน
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_emergency_pause`
- Expected keywords: `อุปกรณ์ขัดข้อง, หลุด, ซอฟต์แวร์`
- Missing keywords: `อุปกรณ์ขัดข้อง, หลุด, ซอฟต์แวร์`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_emergency_pause`
- คำตอบย่อจาก AI: คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 119. [FAIL] competition_valorant_v2_023 - ผิด/ต้องแก้

- คำถาม: ตอน Technical Pause วาโลคุยกันได้ไหม
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_emergency_pause`
- Expected keywords: `ห้าม, สื่อสาร, เว้นแต่`
- Missing keywords: `ห้าม, สื่อสาร, เว้นแต่`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_emergency_pause`
- คำตอบย่อจาก AI: คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 120. [PASS] competition_valorant_v2_024 - ผ่าน

- คำถาม: VALORANT Emergency Pause ขอได้กี่ครั้ง
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_emergency_pause`
- Expected keywords: `1 ครั้ง, ต่อแผนที่`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_emergency_pause`
- คำตอบย่อจาก AI: คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 121. [PASS] competition_valorant_v2_025 - ผ่าน

- คำถาม: VALORANT Emergency Pause รวมเวลาได้ไม่เกินกี่นาที
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_emergency_pause`
- Expected keywords: `10 นาที`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_emergency_pause`
- คำตอบย่อจาก AI: คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 122. [FAIL] competition_valorant_v2_026 - ผิด/ต้องแก้

- คำถาม: VALORANT ถ้า emergency pause เกินเวลาผู้เล่นอาจเป็นอะไร
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_emergency_pause`
- Expected keywords: `หมดสิทธิ์, ตัวสำรอง`
- Missing keywords: `หมดสิทธิ์, ตัวสำรอง`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_emergency_pause`
- คำตอบย่อจาก AI: คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 123. [FAIL] competition_valorant_v2_027 - ผิด/ต้องแก้

- คำถาม: VALORANT Play Through Bug คืออะไร
- Intent ที่คาด: `bug_rule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_emergency_pause`
- Expected keywords: `ไม่ส่งผลกระทบ, เล่นต่อ`
- Missing keywords: `ไม่ส่งผลกระทบ, เล่นต่อ`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `valorant_emergency_pause` คนละ intent กับที่ถาม (`bug_rule`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `valorant_emergency_pause` แต่คำถามต้องการ intent `bug_rule`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_emergency_pause`
- คำตอบย่อจาก AI: คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 124. [FAIL] competition_valorant_v2_028 - ผิด/ต้องแก้

- คำถาม: VALORANT Major Bug ขอ Challenge ได้ไหม
- Intent ที่คาด: `bug_rule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_emergency_pause`
- Expected keywords: `Major Bug, Challenge`
- Missing keywords: `Major Bug, Challenge`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `valorant_emergency_pause` คนละ intent กับที่ถาม (`bug_rule`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `valorant_emergency_pause` แต่คำถามต้องการ intent `bug_rule`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_emergency_pause`
- คำตอบย่อจาก AI: คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 125. [FAIL] competition_valorant_v2_029 - ผิด/ต้องแก้

- คำถาม: VALORANT Game Breaking Bug จัดการยังไง
- Intent ที่คาด: `bug_rule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_emergency_pause`
- Expected keywords: `Game-Breaking, ย้อนรอบ`
- Missing keywords: `Game-Breaking, ย้อนรอบ`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `valorant_emergency_pause` คนละ intent กับที่ถาม (`bug_rule`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `valorant_emergency_pause` แต่คำถามต้องการ intent `bug_rule`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_emergency_pause`
- คำตอบย่อจาก AI: คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 126. [FAIL] competition_valorant_v2_030 - ผิด/ต้องแก้

- คำถาม: VALORANT ถ้าบั๊กเกิดก่อนมี damage ทำอะไรได้
- Intent ที่คาด: `bug_rule`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `ก่อน, ดาเมจ, ย้อนรอบ`
- Missing keywords: `ก่อน, ดาเมจ, ย้อนรอบ`
- Missing source: `competition_rules_valorant_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ VALORANT แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 127. [FAIL] competition_valorant_v2_031 - ผิด/ต้องแก้

- คำถาม: VALORANT ถ้าทำ damage ไปแล้ว rollback ได้ไหม
- Intent ที่คาด: `bug_rule`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `damage, ไม่, Challenge`
- Missing keywords: `damage, ไม่, Challenge`
- Missing source: `competition_rules_valorant_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ VALORANT แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 128. [FAIL] competition_valorant_v2_032 - ผิด/ต้องแก้

- คำถาม: VALORANT ใช้บั๊กเพื่อได้เปรียบถือว่าผิดไหม
- Intent ที่คาด: `penalty`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `ผิด, ได้เปรียบ`
- Missing keywords: `ผิด, ได้เปรียบ`
- Missing source: `competition_rules_valorant_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ VALORANT แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 129. [FAIL] competition_valorant_v2_033 - ผิด/ต้องแก้

- คำถาม: VALORANT วางกล้อง Cypher จุดมองไม่เห็นได้ไหม
- Intent ที่คาด: `character`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `ห้าม, Cypher`
- Missing keywords: `ห้าม, Cypher`
- Missing source: `competition_rules_valorant_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ VALORANT แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 130. [FAIL] competition_valorant_v2_034 - ผิด/ต้องแก้

- คำถาม: VALORANT ใช้สกิลนอกขอบแผนที่เพื่อหาข้อมูลได้ไหม
- Intent ที่คาด: `character`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_map_pool`
- Expected keywords: `ห้าม, นอกขอบเขต`
- Missing keywords: `ห้าม, นอกขอบเขต`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `valorant_map_pool` คนละ intent กับที่ถาม (`character`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `valorant_map_pool` แต่คำถามต้องการ intent `character`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_map_pool`
- คำตอบย่อจาก AI: คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset หลักฐานจากกติกา: - เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset อ้างอิงจากกติกา: VALORANT /...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 131. [FAIL] competition_valorant_v2_035 - ผิด/ต้องแก้

- คำถาม: VALORANT ข้อยกเว้น KAY/O ZERO/POINT คืออะไร
- Intent ที่คาด: `character`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `KAY/O, ZERO/POINT, Texture`
- Missing keywords: `KAY/O, ZERO/POINT, Texture`
- Missing source: `competition_rules_valorant_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ VALORANT แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 132. [FAIL] competition_valorant_v2_036 - ผิด/ต้องแก้

- คำถาม: VALORANT ใช้เพื่อนกระโดดต่อตัวขึ้นจุดสูงได้ไหม
- Intent ที่คาด: `character`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `ห้าม, กระโดด`
- Missing keywords: `ห้าม, กระโดด`
- Missing source: `competition_rules_valorant_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ VALORANT แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 133. [FAIL] competition_valorant_v2_037 - ผิด/ต้องแก้

- คำถาม: VALORANT ความผิดครั้งแรกผลกระทบต่ำโดนอะไร
- Intent ที่คาด: `penalty`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `Warning, ตักเตือน`
- Missing keywords: `Warning, ตักเตือน`
- Missing source: `competition_rules_valorant_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ VALORANT แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 134. [FAIL] competition_valorant_v2_038 - ผิด/ต้องแก้

- คำถาม: VALORANT Round Rollback ใช้เมื่อไหร่
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_tactical_timeout`
- Expected keywords: `Round Rollback, ช่องโหว่`
- Missing keywords: `Round Rollback, ช่องโหว่`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `valorant_tactical_timeout` คนละ intent กับที่ถาม (`penalty`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `valorant_tactical_timeout` แต่คำถามต้องการ intent `penalty`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_tactical_timeout`
- คำตอบย่อจาก AI: คำตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง หลักฐานจากกติกา: - เอกสารระบุ Tactical Timeout ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และเมื่อเข...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 135. [FAIL] competition_valorant_v2_039 - ผิด/ต้องแก้

- คำถาม: VALORANT Round Loss เกิดจากอะไร
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_emergency_pause`
- Expected keywords: `Round Loss, เจตนา, ช่องโหว่`
- Missing keywords: `Round Loss, เจตนา, ช่องโหว่`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `valorant_emergency_pause` คนละ intent กับที่ถาม (`penalty`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `valorant_emergency_pause` แต่คำถามต้องการ intent `penalty`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_emergency_pause`
- คำตอบย่อจาก AI: คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 136. [FAIL] competition_valorant_v2_040 - ผิด/ต้องแก้

- คำถาม: VALORANT Map Forfeit ใช้กรณีไหน
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_map_pool`
- Expected keywords: `Map Forfeit, ร้ายแรง, ซ้ำ`
- Missing keywords: `Map Forfeit, ร้ายแรง, ซ้ำ`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_map_pool`
- คำตอบย่อจาก AI: คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset หลักฐานจากกติกา: - เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset อ้างอิงจากกติกา: VALORANT /...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 137. [FAIL] competition_valorant_v2_041 - ผิด/ต้องแก้

- คำถาม: VALORANT Match Forfeit ใช้กับความผิดแบบไหน
- Intent ที่คาด: `penalty`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `Match Forfeit, Cheating, Match fixing`
- Missing keywords: `Match Forfeit, Cheating, Match fixing`
- Missing source: `competition_rules_valorant_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ VALORANT แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 138. [FAIL] competition_valorant_v2_042 - ผิด/ต้องแก้

- คำถาม: VALORANT ใช้ keyboard Snap Tap หรือ SOCD ได้ไหม
- Intent ที่คาด: `equipment`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_emergency_pause`
- Expected keywords: `Snap Tap, SOCD, permitted`
- Missing keywords: `Snap Tap, SOCD, permitted`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `valorant_emergency_pause` คนละ intent กับที่ถาม (`equipment`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `valorant_emergency_pause` แต่คำถามต้องการ intent `equipment`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_emergency_pause`
- คำตอบย่อจาก AI: คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที หลักฐานจากกติกา: - เอกสารระบุแต่ละทีมมี Emergency Pause ได้ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที อ้างอิงจากกติกา...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 139. [FAIL] competition_valorant_v2_043 - ผิด/ต้องแก้

- คำถาม: VALORANT ใช้ macro ได้ไหม
- Intent ที่คาด: `equipment`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `ห้าม, Macros`
- Missing keywords: `ห้าม, Macros`
- Missing source: `competition_rules_valorant_psu_phuket_2026`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ VALORANT แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 140. [FAIL] competition_valorant_v2_044 - ผิด/ต้องแก้

- คำถาม: VALORANT ติดตั้งโปรแกรมเองบนคอมแข่งได้ไหม
- Intent ที่คาด: `equipment`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_agent_map_restriction`
- Expected keywords: `ห้าม, ติดตั้งโปรแกรม`
- Missing keywords: `ห้าม, ติดตั้งโปรแกรม`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `valorant_agent_map_restriction` คนละ intent กับที่ถาม (`equipment`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `valorant_agent_map_restriction` แต่คำถามต้องการ intent `equipment`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_agent_map_restriction`
- คำตอบย่อจาก AI: คำตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง หลักฐานจากกติกา: - เอกสารระบุข้อจำกัด Agent ใหม่ประมาณ 2 สัปดาห์ และแผนที่ใหม่ประมาณ 4 สัปดาห์ อ้างอิงจาก...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 141. [FAIL] competition_valorant_v2_045 - ผิด/ต้องแก้

- คำถาม: VALORANT เข้าเว็บสื่อสารหรือโซเชียลบนคอมแข่งได้ไหม
- Intent ที่คาด: `equipment`
- Route/Mode: `competition_rules` / `pipeline:no_answer`
- Retrieved: `Reservation`
- Expected keywords: `ห้าม, social media`
- Missing keywords: `ห้าม, social media`
- Missing source: `competition_rules_valorant_psu_phuket_2026`
- สาเหตุ: `no_answer_despite_data` - Route เข้า competition_rules แล้ว แต่ retrieval/fact card ไม่เจอ context ที่มั่นใจพอ จึงตอบไม่พบข้อมูล
- ปัญหา: ระบบตอบไม่พบข้อมูล ทั้งที่ข้อมูลน่าจะอยู่ใน competition chunks
- ลักษณะคำตอบ: ตอบว่าไม่พบข้อมูล ทั้งที่หลายข้อมีข้อมูลอยู่ใน competition chunks แต่ pipeline ดึงไม่ถึง
- คำตอบย่อจาก AI: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด competition_rules ตอนนี้ครับ
- แนวแก้: ให้ fallback ไปค้น `competition_rule_chunks.jsonl` และใช้ RAG/LLM สรุปเมื่อ fact card ไม่ครอบคลุม

### 142. [FAIL] competition_valorant_v2_046 - ผิด/ต้องแก้

- คำถาม: VALORANT สรุป pause แต่ละประเภทแบบสั้นๆ
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_emergency_pause`
- Expected keywords: `Tactical, Technical, Emergency`
- Missing keywords: `Tactical`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_emergency_pause`
- คำตอบย่อจาก AI: คำตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 143. [FAIL] competition_valorant_v2_047 - ผิด/ต้องแก้

- คำถาม: VALORANT สรุปกฎเนื้อหาใหม่กับ map pool
- Intent ที่คาด: `summary`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_map_pool`
- Expected keywords: `Agent, 2 สัปดาห์, แผนที่ใหม่, 4 สัปดาห์, Abyss`
- Missing keywords: `Agent, 2 สัปดาห์, แผนที่ใหม่, 4 สัปดาห์`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_map_pool`
- คำตอบย่อจาก AI: คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset หลักฐานจากกติกา: - เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset อ้างอิงจากกติกา: VALORANT /...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 144. [FAIL] competition_valorant_v2_048 - ผิด/ต้องแก้

- คำถาม: VALORANT สรุปบทลงโทษในเกมว่ามีอะไรบ้าง
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `valorant_map_pool`
- Expected keywords: `Warning, Round Rollback, Round Loss, Map Forfeit, Match Forfeit`
- Missing keywords: `Warning, Round Rollback, Round Loss, Map Forfeit, Match Forfeit`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `valorant_map_pool` คนละ intent กับที่ถาม (`penalty`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `valorant_map_pool` แต่คำถามต้องการ intent `penalty`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `valorant_map_pool`
- คำตอบย่อจาก AI: คำตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset หลักฐานจากกติกา: - เอกสารระบุ map pool ของ VALORANT ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset อ้างอิงจากกติกา: VALORANT /...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

## Tekken 8

### 145. [PASS] competition_tekken8_v2_001 - ผ่าน

- คำถาม: Tekken 8 แข่งออนไลน์หรือออฟไลน์
- Intent ที่คาด: `format`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_format_ps5_1v1`
- Expected keywords: `ออฟไลน์`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_format_ps5_1v1`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที หลักฐานจากกติกา: - เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วิน...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 146. [PASS] competition_tekken8_v2_002 - ผ่าน

- คำถาม: Tekken 8 ใช้เครื่องอะไรแข่ง
- Intent ที่คาด: `equipment`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_equipment_ps5`
- Expected keywords: `PlayStation 5`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_equipment_ps5`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5 หลักฐานจากกติกา: - เอกสารระบุ Platform การแข่งขันเป็น PlayStation 5 อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ แหล่งข้อมูล: local://competition_rules/competit...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 147. [PASS] competition_tekken8_v2_003 - ผ่าน

- คำถาม: Tekken 8 แข่งแบบกี่ต่อกี่
- Intent ที่คาด: `format`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_format_ps5_1v1`
- Expected keywords: `1v1`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_format_ps5_1v1`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที หลักฐานจากกติกา: - เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วิน...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 148. [FAIL] competition_tekken8_v2_004 - ผิด/ต้องแก้

- คำถาม: Tekken 8 FT2 คือชนะกี่เกมก่อน
- Intent ที่คาด: `format`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_format_ps5_1v1`
- Expected keywords: `ชนะครบ 2 เกม`
- Missing keywords: `ชนะครบ 2 เกม`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ; AI ใช้คำเทียบเท่า `FT2/First to 2` แต่ตัวตรวจคาดคำว่า `ชนะครบ 2 เกม`
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_format_ps5_1v1`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที หลักฐานจากกติกา: - เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วิน...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 149. [FAIL] competition_tekken8_v2_005 - ผิด/ต้องแก้

- คำถาม: Tekken 8 ถ้าเสมอกัน 1-1 ต้องทำอะไร
- Intent ที่คาด: `format`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `เกมตัดสิน`
- Missing keywords: `เกมตัดสิน`
- Missing source: `competition_rules_tekken8_psu_esports`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Tekken 8 แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 150. [FAIL] competition_tekken8_v2_006 - ผิด/ต้องแก้

- คำถาม: Tekken 8 ในแต่ละเกมแข่งกี่รอบ
- Intent ที่คาด: `game_setting`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_format_ps5_1v1`
- Expected keywords: `3 รอบ`
- Missing keywords: `3 รอบ`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `tekken8_format_ps5_1v1` คนละ intent กับที่ถาม (`game_setting`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `tekken8_format_ps5_1v1` แต่คำถามต้องการ intent `game_setting`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_format_ps5_1v1`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที หลักฐานจากกติกา: - เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วิน...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 151. [PASS] competition_tekken8_v2_007 - ผ่าน

- คำถาม: Tekken 8 จำกัดเวลาต่อรอบกี่วินาที
- Intent ที่คาด: `game_setting`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_format_ps5_1v1`
- Expected keywords: `60 วินาที`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_format_ps5_1v1`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที หลักฐานจากกติกา: - เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วิน...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 152. [FAIL] competition_tekken8_v2_008 - ผิด/ต้องแก้

- คำถาม: Tekken 8 ตั้งค่า Advantage เป็นอะไร
- Intent ที่คาด: `game_setting`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `No advantage`
- Missing keywords: `No advantage`
- Missing source: `competition_rules_tekken8_psu_esports`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Tekken 8 แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 153. [FAIL] competition_tekken8_v2_009 - ผิด/ต้องแก้

- คำถาม: Tekken 8 เลือก Stage อย่างไร
- Intent ที่คาด: `game_setting`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_character_dlc_rule`
- Expected keywords: `Random`
- Missing keywords: `Random`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `tekken8_character_dlc_rule` คนละ intent กับที่ถาม (`game_setting`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `tekken8_character_dlc_rule` แต่คำถามต้องการ intent `game_setting`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_character_dlc_rule`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน หลักฐานจากกติกา: - เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization อ้างอ...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 154. [PASS] competition_tekken8_v2_010 - ผ่าน

- คำถาม: Tekken 8 เลือกตัวละคร DLC ได้ไหม
- Intent ที่คาด: `character`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_character_dlc_rule`
- Expected keywords: `ยกเว้น, DLC`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_character_dlc_rule`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน หลักฐานจากกติกา: - เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization อ้างอ...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 155. [PASS] competition_tekken8_v2_011 - ผ่าน

- คำถาม: Tekken 8 ใช้ตัวละครตัวไหนก็ได้ไหม
- Intent ที่คาด: `character`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_character_dlc_rule`
- Expected keywords: `ทุกตัว, ยกเว้น, DLC`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_character_dlc_rule`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน หลักฐานจากกติกา: - เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization อ้างอ...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 156. [FAIL] competition_tekken8_v2_012 - ผิด/ต้องแก้

- คำถาม: Tekken 8 ปรับแต่งชุดหรือทรงผมตัวละครได้ไหม
- Intent ที่คาด: `character`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_character_dlc_rule`
- Expected keywords: `ห้าม, ปรับแต่ง`
- Missing keywords: `ปรับแต่ง`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_character_dlc_rule`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน หลักฐานจากกติกา: - เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization อ้างอ...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 157. [FAIL] competition_tekken8_v2_013 - ผิด/ต้องแก้

- คำถาม: Tekken 8 ต้องใช้สกินแบบไหน
- Intent ที่คาด: `skin`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_format_ps5_1v1`
- Expected keywords: `สกินมาตรฐาน`
- Missing keywords: `สกินมาตรฐาน`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `tekken8_format_ps5_1v1` คนละ intent กับที่ถาม (`skin`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `tekken8_format_ps5_1v1` แต่คำถามต้องการ intent `skin`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_format_ps5_1v1`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที หลักฐานจากกติกา: - เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วิน...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 158. [FAIL] competition_tekken8_v2_014 - ผิด/ต้องแก้

- คำถาม: Tekken 8 ใช้ปุ่ม Assist ได้ไหม
- Intent ที่คาด: `game_setting`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `อนุญาต, Assist`
- Missing keywords: `อนุญาต, Assist`
- Missing source: `competition_rules_tekken8_psu_esports`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Tekken 8 แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 159. [FAIL] competition_tekken8_v2_015 - ผิด/ต้องแก้

- คำถาม: Tekken 8 ใช้ bug หรือ glitch ได้ไหม
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_character_dlc_rule`
- Expected keywords: `ห้าม, Bug, Glitch`
- Missing keywords: `Bug, Glitch`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `tekken8_character_dlc_rule` คนละ intent กับที่ถาม (`penalty`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `tekken8_character_dlc_rule` แต่คำถามต้องการ intent `penalty`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_character_dlc_rule`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน หลักฐานจากกติกา: - เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization อ้างอ...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 160. [PASS] competition_tekken8_v2_016 - ผ่าน

- คำถาม: Tekken 8 เมื่อเริ่มเกมแล้ว pause ได้ไหม
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_pause_penalty`
- Expected keywords: `ห้าม, หยุดเกม`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_pause_penalty`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร หลักฐานจากกติกา: - เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 161. [FAIL] competition_tekken8_v2_017 - ผิด/ต้องแก้

- คำถาม: Tekken 8 ตั้งใจกด pause โดนอะไร
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_pause_penalty`
- Expected keywords: `ปรับแพ้ 1 รอบ`
- Missing keywords: `ปรับแพ้ 1 รอบ`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_pause_penalty`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร หลักฐานจากกติกา: - เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 162. [FAIL] competition_tekken8_v2_018 - ผิด/ต้องแก้

- คำถาม: Tekken 8 กดหยุดเกมได้ในกรณีไหน
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_pause_penalty`
- Expected keywords: `ยินยอม, อุปกรณ์ขัดข้อง, เหตุฉุกเฉิน`
- Missing keywords: `อุปกรณ์ขัดข้อง, เหตุฉุกเฉิน`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_pause_penalty`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร หลักฐานจากกติกา: - เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 163. [FAIL] competition_tekken8_v2_019 - ผิด/ต้องแก้

- คำถาม: Tekken 8 ถ้าออกจากเกมก่อนจบโดยไม่ได้รับอนุญาตโดนอะไร
- Intent ที่คาด: `penalty`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `ปรับแพ้ทันที`
- Missing keywords: `ปรับแพ้ทันที`
- Missing source: `competition_rules_tekken8_psu_esports`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Tekken 8 แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 164. [FAIL] competition_tekken8_v2_020 - ผิด/ต้องแก้

- คำถาม: Tekken 8 หยุดเกมโดยไม่จำเป็นลงโทษเหมือนอะไร
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_pause_penalty`
- Expected keywords: `ออกจากเกมก่อนจบ`
- Missing keywords: `ออกจากเกมก่อนจบ`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_pause_penalty`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร หลักฐานจากกติกา: - เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 165. [FAIL] competition_tekken8_v2_021 - ผิด/ต้องแก้

- คำถาม: Tekken 8 เยาะเย้ยหรือไม่สุภาพต่อคู่แข่งโดนอะไร
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_pause_penalty`
- Expected keywords: `ปรับแพ้ทันที`
- Missing keywords: `ปรับแพ้ทันที`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ; AI มีคำว่า `ปรับแพ้` แต่ยังไม่ชัดว่า `ทันที` ตามเกณฑ์
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_pause_penalty`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร หลักฐานจากกติกา: - เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 166. [FAIL] competition_tekken8_v2_022 - ผิด/ต้องแก้

- คำถาม: Tekken 8 ดูถูกผู้ตัดสินหรือผู้เข้าแข่งคนอื่นได้ไหม
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:no_answer`
- Retrieved: `Reservation`
- Expected keywords: `ห้าม, ปรับแพ้ทันที`
- Missing keywords: `ห้าม, ปรับแพ้ทันที`
- Missing source: `competition_rules_tekken8_psu_esports`
- สาเหตุ: `no_answer_despite_data` - Route เข้า competition_rules แล้ว แต่ retrieval/fact card ไม่เจอ context ที่มั่นใจพอ จึงตอบไม่พบข้อมูล
- ปัญหา: ระบบตอบไม่พบข้อมูล ทั้งที่ข้อมูลน่าจะอยู่ใน competition chunks
- ลักษณะคำตอบ: ตอบว่าไม่พบข้อมูล ทั้งที่หลายข้อมีข้อมูลอยู่ใน competition chunks แต่ pipeline ดึงไม่ถึง
- คำตอบย่อจาก AI: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด competition_rules ตอนนี้ครับ
- แนวแก้: ให้ fallback ไปค้น `competition_rule_chunks.jsonl` และใช้ RAG/LLM สรุปเมื่อ fact card ไม่ครอบคลุม

### 167. [FAIL] competition_tekken8_v2_023 - ผิด/ต้องแก้

- คำถาม: Tekken 8 ผู้เข้าแข่งขันต้องยอมรับอะไรเกี่ยวกับคำตัดสิน
- Intent ที่คาด: `policy`
- Route/Mode: `competition_rules` / `pipeline:no_answer`
- Retrieved: `Reservation`
- Expected keywords: `คำตัดสิน, กรรมการ`
- Missing keywords: `คำตัดสิน, กรรมการ`
- Missing source: `competition_rules_tekken8_psu_esports`
- สาเหตุ: `no_answer_despite_data` - Route เข้า competition_rules แล้ว แต่ retrieval/fact card ไม่เจอ context ที่มั่นใจพอ จึงตอบไม่พบข้อมูล
- ปัญหา: ระบบตอบไม่พบข้อมูล ทั้งที่ข้อมูลน่าจะอยู่ใน competition chunks
- ลักษณะคำตอบ: ตอบว่าไม่พบข้อมูล ทั้งที่หลายข้อมีข้อมูลอยู่ใน competition chunks แต่ pipeline ดึงไม่ถึง
- คำตอบย่อจาก AI: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด competition_rules ตอนนี้ครับ
- แนวแก้: ให้ fallback ไปค้น `competition_rule_chunks.jsonl` และใช้ RAG/LLM สรุปเมื่อ fact card ไม่ครอบคลุม

### 168. [FAIL] competition_tekken8_v2_024 - ผิด/ต้องแก้

- คำถาม: ผู้จัด Tekken 8 เปลี่ยนกฎได้ไหม
- Intent ที่คาด: `policy`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_pause_penalty`
- Expected keywords: `ปรับเปลี่ยนกฎ, ไม่ต้องแจ้ง`
- Missing keywords: `ปรับเปลี่ยนกฎ, ไม่ต้องแจ้ง`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `tekken8_pause_penalty` คนละ intent กับที่ถาม (`policy`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `tekken8_pause_penalty` แต่คำถามต้องการ intent `policy`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_pause_penalty`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร หลักฐานจากกติกา: - เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 169. [FAIL] competition_tekken8_v2_025 - ผิด/ต้องแก้

- คำถาม: Tekken 8 คำตัดสินของกรรมการถือว่าอย่างไร
- Intent ที่คาด: `policy`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `ถือเป็นที่สิ้นสุด`
- Missing keywords: `ถือเป็นที่สิ้นสุด`
- Missing source: `competition_rules_tekken8_psu_esports`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Tekken 8 แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 170. [FAIL] competition_tekken8_v2_026 - ผิด/ต้องแก้

- คำถาม: Tekken 8 ถ้าเกิดข้อโต้แย้งต้องฟังคำตัดสินใคร
- Intent ที่คาด: `dispute`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `ผู้ดูแล, กรรมการ`
- Missing keywords: `ผู้ดูแล, กรรมการ`
- Missing source: `competition_rules_tekken8_psu_esports`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Tekken 8 แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 171. [FAIL] competition_tekken8_v2_027 - ผิด/ต้องแก้

- คำถาม: Tekken 8 หากเกิดปัญหาใดๆ ต้องแจ้งใคร
- Intent ที่คาด: `dispute`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `ผู้จัดการแข่งขัน, ทันที`
- Missing keywords: `ผู้จัดการแข่งขัน, ทันที`
- Missing source: `competition_rules_tekken8_psu_esports`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Tekken 8 แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 172. [PASS] competition_tekken8_v2_028 - ผ่าน

- คำถาม: Tekken 8 สรุปรูปแบบการแข่งขันแบบสั้นๆ
- Intent ที่คาด: `summary`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_format_ps5_1v1`
- Expected keywords: `ออฟไลน์, PlayStation 5, 1v1, FT2`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_format_ps5_1v1`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 173. [FAIL] competition_tekken8_v2_029 - ผิด/ต้องแก้

- คำถาม: Tekken 8 สรุปกฎตัวละครและสกิน
- Intent ที่คาด: `summary`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_character_dlc_rule`
- Expected keywords: `DLC, ปรับแต่ง, สกินมาตรฐาน`
- Missing keywords: `ปรับแต่ง`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_character_dlc_rule`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน หลักฐานจากกติกา: - เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization อ้างอ...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 174. [PASS] competition_tekken8_v2_030 - ผ่าน

- คำถาม: Tekken 8 สรุปกฎ pause แบบเข้าใจง่าย
- Intent ที่คาด: `summary`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_pause_penalty`
- Expected keywords: `Pause, ยินยอม, ปรับแพ้`
- Missing keywords: `-`
- Missing source: `-`
- สาเหตุ: `pass` - ผ่านตามเกณฑ์: keyword/source/validation ตรง
- ปัญหา: ไม่มีปัญหาหลักในเกณฑ์อัตโนมัติ
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_pause_penalty`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร หลักฐานจากกติกา: - เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round...
- แนวแก้: ใช้เป็นตัวอย่างคำตอบที่ pipeline ทำได้ดีในหมวดนี้

### 175. [FAIL] competition_tekken8_v2_031 - ผิด/ต้องแก้

- คำถาม: Tekken 8 รอบละ 60 วิและ R3 หมายถึงอะไร
- Intent ที่คาด: `game_setting`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_character_dlc_rule`
- Expected keywords: `3 รอบ, 60 วินาที`
- Missing keywords: `3 รอบ, 60 วินาที`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `tekken8_character_dlc_rule` คนละ intent กับที่ถาม (`game_setting`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `tekken8_character_dlc_rule` แต่คำถามต้องการ intent `game_setting`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_character_dlc_rule`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน หลักฐานจากกติกา: - เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization อ้างอ...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 176. [FAIL] competition_tekken8_v2_032 - ผิด/ต้องแก้

- คำถาม: Tekken 8 ใช้ PS5 กับ Stage Random ใช่ไหม
- Intent ที่คาด: `game_setting`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_equipment_ps5`
- Expected keywords: `PlayStation 5, Random`
- Missing keywords: `Random`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `tekken8_equipment_ps5` คนละ intent กับที่ถาม (`game_setting`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `tekken8_equipment_ps5` แต่คำถามต้องการ intent `game_setting`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_equipment_ps5`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5 หลักฐานจากกติกา: - เอกสารระบุ Platform การแข่งขันเป็น PlayStation 5 อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ แหล่งข้อมูล: local://competition_rules/competit...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 177. [FAIL] competition_tekken8_v2_033 - ผิด/ต้องแก้

- คำถาม: Tekken 8 ถามว่าแข่งกี่เกมควรตอบว่าอะไร
- Intent ที่คาด: `format`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_format_ps5_1v1`
- Expected keywords: `FT2, ชนะครบ 2 เกม`
- Missing keywords: `ชนะครบ 2 เกม`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ; AI ใช้คำเทียบเท่า `FT2/First to 2` แต่ตัวตรวจคาดคำว่า `ชนะครบ 2 เกม`
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_format_ps5_1v1`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที หลักฐานจากกติกา: - เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วิน...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 178. [FAIL] competition_tekken8_v2_034 - ผิด/ต้องแก้

- คำถาม: Tekken 8 ใช้ customization เอฟเฟกต์หรือออร่าได้ไหม
- Intent ที่คาด: `character`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_character_dlc_rule`
- Expected keywords: `ห้าม, เอฟเฟกต์, ออร่า`
- Missing keywords: `เอฟเฟกต์, ออร่า`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_character_dlc_rule`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน หลักฐานจากกติกา: - เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization อ้างอ...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 179. [FAIL] competition_tekken8_v2_035 - ผิด/ต้องแก้

- คำถาม: Tekken 8 เหตุผลด้านอุปกรณ์ขัดข้องสามารถ pause ได้ไหม
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_pause_penalty`
- Expected keywords: `อุปกรณ์ขัดข้อง, ยินยอม`
- Missing keywords: `อุปกรณ์ขัดข้อง`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_pause_penalty`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร หลักฐานจากกติกา: - เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 180. [FAIL] competition_tekken8_v2_036 - ผิด/ต้องแก้

- คำถาม: Tekken 8 เหตุฉุกเฉินใช้เป็นเหตุผล pause ได้ไหม
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_pause_penalty`
- Expected keywords: `เหตุฉุกเฉิน`
- Missing keywords: `เหตุฉุกเฉิน`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_pause_penalty`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร หลักฐานจากกติกา: - เอกสารระบุห้ามหยุดเกมหลังเริ่มแข่งขัน การ Pause โดยตั้งใจทำให้แพ้ 1 Round...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 181. [FAIL] competition_tekken8_v2_037 - ผิด/ต้องแก้

- คำถาม: Tekken 8 กติกาบอกว่าผู้จัดขอสงวนสิทธิ์อะไร
- Intent ที่คาด: `policy`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_format_ps5_1v1`
- Expected keywords: `เปลี่ยนแปลง, กฎระเบียบ`
- Missing keywords: `เปลี่ยนแปลง, กฎระเบียบ`
- Missing source: `-`
- สาเหตุ: `wrong_fact_card_intent` - Fact card ที่ถูกเลือก `tekken8_format_ps5_1v1` คนละ intent กับที่ถาม (`policy`) ทำให้ตอบผิดประเด็น
- ปัญหา: ระบบตอบจาก `tekken8_format_ps5_1v1` แต่คำถามต้องการ intent `policy`
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_format_ps5_1v1`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที หลักฐานจากกติกา: - เอกสารระบุแข่งขันแบบ Offline, Platform PlayStation 5, 1v1, FT2, R3 และตั้งเวลา 60 วิน...
- แนวแก้: เพิ่ม fact card เฉพาะเรื่องนี้ และลดคะแนน fact card คนละ intent เมื่อ intent_hint ชัดเจน

### 182. [FAIL] competition_tekken8_v2_038 - ผิด/ต้องแก้

- คำถาม: Tekken 8 ถ้าฝ่าฝืนมารยาทมีข้อยกเว้นไหม
- Intent ที่คาด: `penalty`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `ไม่มีข้อยกเว้น, ปรับแพ้`
- Missing keywords: `ไม่มีข้อยกเว้น, ปรับแพ้`
- Missing source: `competition_rules_tekken8_psu_esports`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Tekken 8 แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่

### 183. [FAIL] competition_tekken8_v2_039 - ผิด/ต้องแก้

- คำถาม: Tekken 8 เลือกตัวละคร DLC ไม่ได้แต่ใช้ Assist ได้ใช่ไหม
- Intent ที่คาด: `character`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Retrieved: `tekken8_character_dlc_rule`
- Expected keywords: `DLC, Assist`
- Missing keywords: `Assist`
- Missing source: `-`
- สาเหตุ: `partial_or_strict_keyword` - Fact card ที่เลือกใกล้เคียง แต่คำตอบยังไม่ครบ keyword สำคัญ
- ปัญหา: คำตอบอยู่ในเอกสารเกมถูกแล้ว แต่ยังไม่ครบประเด็นที่ ground truth คาด หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ลักษณะคำตอบ: ตอบแบบ fact card สั้นพร้อมหลักฐาน แต่เลือก card จาก `tekken8_character_dlc_rule`
- คำตอบย่อจาก AI: คำตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน หลักฐานจากกติกา: - เอกสารระบุอนุญาตให้ใช้ตัวละครทุกตัว ยกเว้น DLC Character และไม่อนุญาตให้ใช้ Customization อ้างอ...
- แนวแก้: ขยาย answer ของ fact card ให้มีรายละเอียดครบ หรือเพิ่ม acceptable keyword/synonym group ใน evaluator

### 184. [FAIL] competition_tekken8_v2_040 - ผิด/ต้องแก้

- คำถาม: Tekken 8 ต้องเล่นบนแพลตฟอร์มอะไรและเป็นเดี่ยวไหม
- Intent ที่คาด: `format`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Retrieved: `Reservation`
- Expected keywords: `PlayStation 5, เดี่ยว, 1v1`
- Missing keywords: `เดี่ยว, 1v1`
- Missing source: `competition_rules_tekken8_psu_esports`
- สาเหตุ: `wrong_route` - Router จัดเป็นหมวด games เพราะเห็นชื่อเกม/รายการเกม แล้ว fast path ของ games ตอบแทนกติกา
- ปัญหา: คำถามควรเป็น competition_rules ของ Tekken 8 แต่ถูกส่งไป `games`
- ลักษณะคำตอบ: ตอบเป็นข้อมูล static ของหมวดเกม/รายการเกมในศูนย์ ไม่ใช่คำตอบกติกาการแข่งขันเฉพาะข้อนี้
- คำตอบย่อจาก AI: PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation
- แนวแก้: เพิ่ม priority ให้ competition_rules เมื่อมีชื่อเกม + คำเกี่ยวกับแข่ง/กติกา/โดนอะไร/ได้ไหม/รอบ/อุปกรณ์/แผนที่
