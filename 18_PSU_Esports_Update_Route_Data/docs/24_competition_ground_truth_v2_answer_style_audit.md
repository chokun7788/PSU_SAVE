# Competition Ground Truth V2 - Answer Style Audit

วันที่: 2026-07-03

รายงานนี้เน้นวิเคราะห์รูปแบบคำตอบ โดยเฉพาะหลักที่ต้องการคือ `ตอบคำตอบจริงก่อน -> รายละเอียด -> หลักฐาน/อ้างอิงท้ายสุด`

## Desired Answer Format

รูปแบบที่ควรใช้:

```text
คำตอบ: <ตอบตรงคำถามในบรรทัดแรก เช่น จำนวน/ราคา/ได้หรือไม่ได้/บทลงโทษ/เวลา>

รายละเอียด:
- <ขยายเงื่อนไขที่เกี่ยวข้อง>
- <ข้อควรระวังหรือข้อยกเว้น>

อ้างอิงจากกติกา: <ชื่อเกม / ชื่อรายการ>
แหล่งข้อมูล: <source>
```

หลักการ:

- บรรทัดแรกต้องตอบสิ่งที่ผู้ใช้ถามก่อน ห้ามเริ่มด้วยประวัติ/รายละเอียด/แหล่งข้อมูล
- ถ้าคำถามถาม `ได้ไหม` ต้องตอบ `ได้/ไม่ได้/ห้าม/อนุญาต` ก่อน
- ถ้าคำถามถาม `กี่` ต้องตอบตัวเลขก่อน
- ถ้าคำถามถาม `โดนอะไร` ต้องตอบบทลงโทษก่อน
- รายละเอียดและหลักฐานควรอยู่ข้างล่าง ไม่ควรกลบคำตอบหลัก

## Summary

- Total: 184
- PASS: 41
- FAIL: 143

## Style Counts

- `direct_but_wrong_fact`: 53
- `wrong_domain_first_line`: 48
- `good_direct_first`: 37
- `missing_expected_content`: 37
- `no_answer`: 7
- `details_have_answer_but_first_line_missing`: 2

## Cause Counts

- `wrong_fact_card_intent`: 53
- `wrong_route`: 47
- `pass`: 41
- `partial_or_strict_keyword`: 36
- `no_answer_despite_data`: 6
- `rag_partial_answer`: 1

## Style By Game

### Counter-Strike 2
- `wrong_domain_first_line`: 17
- `direct_but_wrong_fact`: 16
- `good_direct_first`: 9
- `missing_expected_content`: 5
- `no_answer`: 1

### Arena of Valor (RoV)
- `direct_but_wrong_fact`: 14
- `missing_expected_content`: 11
- `good_direct_first`: 10
- `wrong_domain_first_line`: 9
- `no_answer`: 3
- `details_have_answer_but_first_line_missing`: 1

### VALORANT
- `direct_but_wrong_fact`: 15
- `wrong_domain_first_line`: 13
- `good_direct_first`: 10
- `missing_expected_content`: 9
- `no_answer`: 1

### Tekken 8
- `missing_expected_content`: 12
- `wrong_domain_first_line`: 9
- `good_direct_first`: 8
- `direct_but_wrong_fact`: 8
- `no_answer`: 2
- `details_have_answer_but_first_line_missing`: 1

## Main Findings

### 1. หลายคำตอบมี direct-first แต่เป็นคำตอบผิดเรื่อง

เช่นถามคุณสมบัติผู้เข้าแข่ง แต่ first line ตอบเรื่อง pause หรือ map pool ปัญหาไม่ใช่ formatter แต่เป็น retrieval/fact card intent ผิด

### 2. หลายคำถามหลุด route ก่อนจะถึง competition rules

เมื่อหลุดไป `games_fast_path`, `events_news`, `schedule_fast_path` คำตอบแรกจึงกลายเป็นข้อมูลทั่วไปของศูนย์หรือข่าว ไม่ใช่กติกาการแข่งขัน

### 3. บางข้อมีข้อมูลในคำตอบรวม แต่ first line ยังไม่ตอบจุดที่ถาม

กรณีนี้ต้องปรับ answer synthesis ให้ดึงประเด็นที่ผู้ใช้ถามมาไว้บรรทัดแรก

### 4. บางข้อเป็นปัญหาตัวตรวจ strict keyword

เช่น AI ตอบ `FT2/First to 2` แต่เฉลยคาด `ชนะครบ 2 เกม` แบบนี้ความหมายถูกใกล้เคียง แต่ evaluator ยังไม่มี synonym group

## Item Style Audit

## Counter-Strike 2

### 1. [FAIL] competition_cs2_v2_001

- คำถาม: PSU Phuket CS2 2026 รับเฉพาะนักศึกษาแบบไหน
- Intent ที่คาด: `eligibility`
- Route/Mode: `events_news` / `pipeline:rag_direct_curated`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: เมื่อวันที่ 27 กุมภาพันธ์ 2569 นักศึกษาชาวจีนระดับปริญญาโท คณะการบริการและการท่องเที่ยว จำนวน 11 คน เข้าร่วมกิจกรรมการเรียนรู้โดยใช้เกมเป็นฐาน (Game-based Learning) ณ PSU Esports Studio - Phuket
- Keyword ที่ขาดใน first line: `มหาวิทยาลัยสงขลานครินทร์, ภูเก็ต`
- Keyword ที่ขาดในคำตอบรวม: `มหาวิทยาลัยสงขลานครินทร์, ภูเก็ต`
- Retrieved: `curated_news_chinese_students_game_based_learning, curated_news_game_on_thaimuang, curated_news_cs2_2026`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `events_news` จึงตอบ `เมื่อวันที่ 27 กุมภาพันธ์ 2569 นักศึกษาชาวจีนระดับปริญญาโท คณะการบริการและการท่องเที่ยว จำนวน 11 คน เข้าร่วมกิจกรรมการเรียนรู้โดยใช้เกมเป็นฐาน (Game-based Learning) ณ PSU Esports Studio - Phuket` ซึ่งไม่ใช่คำตอบของคำถาม `PSU Phuket CS2 2026 รับเฉพาะนักศึกษาแบบไหน`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: นักศึกษา, มหาวิทยาลัยสงขลานครินทร์, ภูเก็ต

### 2. [FAIL] competition_cs2_v2_002

- คำถาม: คนนอก PSU Phuket ลงแข่ง CS2 รายการนี้ได้ไหม
- Intent ที่คาด: `eligibility`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
- Keyword ที่ขาดใน first line: `เฉพาะ, นักศึกษา, ภูเก็ต`
- Keyword ที่ขาดในคำตอบรวม: `เฉพาะ, นักศึกษา, ภูเก็ต`
- Retrieved: `cs2_pause_policy`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `cs2_pause_policy` ทำให้คำตอบแรกเป็น `ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที` แต่คำถามต้องการ intent `eligibility` และยังขาด `เฉพาะ, นักศึกษา, ภูเก็ต`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: เฉพาะ, นักศึกษา, ภูเก็ต

### 3. [PASS] competition_cs2_v2_003

- คำถาม: CS2 แข่งทีมละกี่คน
- Intent ที่คาด: `team_size`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `cs2_team_size_players`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยจำนวนผู้เล่น/ทีมของ Counter-Strike 2 ให้ชัด เช่นมีคำว่า CS2, ผู้เล่น 5 คน

### 4. [PASS] competition_cs2_v2_004

- คำถาม: Counter-Strike 2 ต้องส่งผู้เล่นหลักกี่คน
- Intent ที่คาด: `team_size`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `cs2_team_size_players`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยจำนวนผู้เล่น/ทีมของ Counter-Strike 2 ให้ชัด เช่นมีคำว่า 5 คน

### 5. [FAIL] competition_cs2_v2_005

- คำถาม: CS2 ใช้แพลตฟอร์มอะไรและห้ามดัดแปลงตัวเกมไหม
- Intent ที่คาด: `game_version`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
- Keyword ที่ขาดใน first line: `Steam, ห้าม, ดัดแปลง`
- Keyword ที่ขาดในคำตอบรวม: `Steam, ห้าม, ดัดแปลง`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends` ซึ่งไม่ใช่คำตอบของคำถาม `CS2 ใช้แพลตฟอร์มอะไรและห้ามดัดแปลงตัวเกมไหม`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: Steam, ห้าม, ดัดแปลง

### 6. [FAIL] competition_cs2_v2_006

- คำถาม: รายการ CS2 ใช้เวอร์ชันเกมแบบไหน
- Intent ที่คาด: `game_version`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
- Keyword ที่ขาดใน first line: `ล่าสุด, CS2, Steam`
- Keyword ที่ขาดในคำตอบรวม: `ล่าสุด, CS2, Steam`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends` ซึ่งไม่ใช่คำตอบของคำถาม `รายการ CS2 ใช้เวอร์ชันเกมแบบไหน`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: ล่าสุด, CS2, Steam

### 7. [FAIL] competition_cs2_v2_007

- คำถาม: ภาษาทางการของการแข่งขัน CS2 คือภาษาอะไร
- Intent ที่คาด: `language`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
- Keyword ที่ขาดใน first line: `ภาษาไทย`
- Keyword ที่ขาดในคำตอบรวม: `ภาษาไทย`
- Retrieved: `cs2_map_pool`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `cs2_map_pool` ทำให้คำตอบแรกเป็น `CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train` แต่คำถามต้องการ intent `language` และยังขาด `ภาษาไทย`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: ภาษาไทย

### 8. [FAIL] competition_cs2_v2_008

- คำถาม: ถ้าจะประท้วงผล CS2 ต้องใช้ภาษาอะไรในเอกสาร
- Intent ที่คาด: `language`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
- Keyword ที่ขาดใน first line: `ภาษาไทย`
- Keyword ที่ขาดในคำตอบรวม: `ภาษาไทย`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends` ซึ่งไม่ใช่คำตอบของคำถาม `ถ้าจะประท้วงผล CS2 ต้องใช้ภาษาอะไรในเอกสาร`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: ภาษาไทย

### 9. [FAIL] competition_cs2_v2_009

- คำถาม: CS2 แข่งกี่วันและแข่งที่ไหน
- Intent ที่คาด: `schedule_location`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
- Keyword ที่ขาดใน first line: `1 วัน, PSU Esports Studio, Phuket`
- Keyword ที่ขาดในคำตอบรวม: `1 วัน, PSU Esports Studio`
- Retrieved: `cs2_team_size_players`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `cs2_team_size_players` ทำให้คำตอบแรกเป็น `CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน` แต่คำถามต้องการ intent `schedule_location` และยังขาด `1 วัน, PSU Esports Studio`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยวัน เวลา หรือสถานที่ที่ถามก่อน เช่น 1 วัน, PSU Esports Studio, Phuket

### 10. [FAIL] competition_cs2_v2_010

- คำถาม: สถานที่จัด PSU Phuket CS2 2026 คือที่ไหน
- Intent ที่คาด: `schedule_location`
- Route/Mode: `events_news` / `pipeline:category_rule_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PSU Esports Studio - Phuket ตั้งอยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `rule_contact_location`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `events_news` จึงตอบ `PSU Esports Studio - Phuket ตั้งอยู่ที่มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต 80 หมู่ 1 ถ.วิชิตสงคราม อ.กะทู้ จ.ภูเก็ต 83120` ซึ่งไม่ใช่คำตอบของคำถาม `สถานที่จัด PSU Phuket CS2 2026 คือที่ไหน`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยวัน เวลา หรือสถานที่ที่ถามก่อน เช่น PSU Esports Studio, Phuket

### 11. [FAIL] competition_cs2_v2_011

- คำถาม: CS2 ใช้ช่องทางสื่อสารหลักอะไร
- Intent ที่คาด: `communication`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
- Keyword ที่ขาดใน first line: `Discord`
- Keyword ที่ขาดในคำตอบรวม: `Discord`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends` ซึ่งไม่ใช่คำตอบของคำถาม `CS2 ใช้ช่องทางสื่อสารหลักอะไร`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: Discord

### 12. [FAIL] competition_cs2_v2_012

- คำถาม: ผู้เข้าแข่ง CS2 ต้องใช้เซิร์ฟเวอร์ไหนในการสื่อสาร
- Intent ที่คาด: `communication`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
- Keyword ที่ขาดใน first line: `Discord, ศูนย์`
- Keyword ที่ขาดในคำตอบรวม: `Discord, ศูนย์`
- Retrieved: `cs2_team_size_players`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `cs2_team_size_players` ทำให้คำตอบแรกเป็น `CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน` แต่คำถามต้องการ intent `communication` และยังขาด `Discord, ศูนย์`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: Discord, ศูนย์

### 13. [FAIL] competition_cs2_v2_013

- คำถาม: CS2 เปลี่ยนสมาชิกทีมระหว่างทัวร์นาเมนต์ได้ไหม
- Intent ที่คาด: `roster_change`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
- Keyword ที่ขาดใน first line: `ไม่มีการเปลี่ยนแปลง, สมาชิก`
- Keyword ที่ขาดในคำตอบรวม: `ไม่มีการเปลี่ยนแปลง, สมาชิก`
- Retrieved: `cs2_team_size_players`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `cs2_team_size_players` ทำให้คำตอบแรกเป็น `CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน` แต่คำถามต้องการ intent `roster_change` และยังขาด `ไม่มีการเปลี่ยนแปลง, สมาชิก`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: ไม่มีการเปลี่ยนแปลง, สมาชิก

### 14. [FAIL] competition_cs2_v2_014

- คำถาม: หลังปิดรับสมัคร CS2 ลงทะเบียนผู้เล่นเพิ่มได้ไหม
- Intent ที่คาด: `registration`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
- Keyword ที่ขาดใน first line: `ไม่อนุญาต, ปิดรับสมัคร`
- Keyword ที่ขาดในคำตอบรวม: `ไม่อนุญาต, ปิดรับสมัคร`
- Retrieved: `cs2_pause_policy`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `cs2_pause_policy` ทำให้คำตอบแรกเป็น `ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที` แต่คำถามต้องการ intent `registration` และยังขาด `ไม่อนุญาต, ปิดรับสมัคร`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: ไม่อนุญาต, ปิดรับสมัคร

### 15. [FAIL] competition_cs2_v2_015

- คำถาม: ถ้าผู้เล่น CS2 ถอนตัวทีมจะเป็นยังไง
- Intent ที่คาด: `eligibility`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
- Keyword ที่ขาดใน first line: `ถอนตัว, ตัดสิทธิ์`
- Keyword ที่ขาดในคำตอบรวม: `ถอนตัว, ตัดสิทธิ์`
- Retrieved: `cs2_team_size_players`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `cs2_team_size_players` ทำให้คำตอบแรกเป็น `CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน` แต่คำถามต้องการ intent `eligibility` และยังขาด `ถอนตัว, ตัดสิทธิ์`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: ถอนตัว, ตัดสิทธิ์

### 16. [FAIL] competition_cs2_v2_016

- คำถาม: ผู้เล่น CS2 เล่นให้สองทีมได้ไหม
- Intent ที่คาด: `eligibility`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน
- Keyword ที่ขาดใน first line: `ทีมเดียว`
- Keyword ที่ขาดในคำตอบรวม: `ทีมเดียว`
- Retrieved: `cs2_team_size_players`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `CS2 แต่ละทีมประกอบด้วยผู้เล่น 5 คน` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `ทีมเดียว` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: ทีมเดียว

### 17. [FAIL] competition_cs2_v2_017

- คำถาม: สายการแข่งขัน CS2 จะประกาศก่อนแข่งนานแค่ไหน
- Intent ที่คาด: `schedule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
- Keyword ที่ขาดใน first line: `ล่วงหน้า, 1 วัน`
- Keyword ที่ขาดในคำตอบรวม: `ล่วงหน้า, 1 วัน`
- Retrieved: `cs2_map_pool`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `cs2_map_pool` ทำให้คำตอบแรกเป็น `CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train` แต่คำถามต้องการ intent `schedule` และยังขาด `ล่วงหน้า, 1 วัน`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยวัน เวลา หรือสถานที่ที่ถามก่อน เช่น ล่วงหน้า, 1 วัน

### 18. [PASS] competition_cs2_v2_018

- คำถาม: CS2 มาสายหรือไม่ยืนยันเข้าแข่งก่อนแมตช์เสี่ยงอะไร
- Intent ที่คาด: `late_start`
- Route/Mode: `competition_rules` / `pipeline:rag_direct_curated`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `competition_rules_cs2_psu_phuket_2026_s15_c01, competition_rules_cs2_psu_phuket_2026_s37_c01, competition_rules_cs2_psu_phuket_2026_s54_c01`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น มาสาย, ตัดสิทธิ์

### 19. [PASS] competition_cs2_v2_019

- คำถาม: รูปแบบทัวร์นาเมนต์ CS2 เป็นแบบไหน
- Intent ที่คาด: `format`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `cs2_format_single_elim_bo3`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น Single Elimination

### 20. [PASS] competition_cs2_v2_020

- คำถาม: CS2 รอบรองกับรอบชิงแข่ง BO อะไร
- Intent ที่คาด: `format`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: CS2 เป็น Single Elimination และรอบรองชนะเลิศ/รอบชิงชนะเลิศเป็น Best of 3 (BO3)
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `cs2_format_single_elim_bo3`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น รอบรอง, รอบชิง, BO3

### 21. [FAIL] competition_cs2_v2_021

- คำถาม: โหมดในเกม CS2 ใช้โหมดอะไร
- Intent ที่คาด: `game_setting`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
- Keyword ที่ขาดใน first line: `Competitive, 5v5`
- Keyword ที่ขาดในคำตอบรวม: `Competitive, 5v5`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends` ซึ่งไม่ใช่คำตอบของคำถาม `โหมดในเกม CS2 ใช้โหมดอะไร`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น Competitive, 5v5

### 22. [FAIL] competition_cs2_v2_022

- คำถาม: CS2 เวลาต่อรอบกับ Freeze time เท่าไหร่
- Intent ที่คาด: `game_setting`
- Route/Mode: `service_fee` / `pipeline:rag_direct_curated`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: บริการ PC ในระบบจองมีระยะเวลา 60 min แต่ในข้อมูลที่ดึงมาและในรูป Service Fee 2026 ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ จึงยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง
- Keyword ที่ขาดใน first line: `1:55, 15 วินาที`
- Keyword ที่ขาดในคำตอบรวม: `1:55, 15 วินาที`
- Retrieved: `curated_service_fee_pc_unknown, curated_service_fee_ps5_rates, curated_service_fee_nintendo_1_2_rates`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `service_fee` จึงตอบ `บริการ PC ในระบบจองมีระยะเวลา 60 min แต่ในข้อมูลที่ดึงมาและในรูป Service Fee 2026 ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ จึงยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง` ซึ่งไม่ใช่คำตอบของคำถาม `CS2 เวลาต่อรอบกับ Freeze time เท่าไหร่`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น 1:55, 15 วินาที

### 23. [FAIL] competition_cs2_v2_023

- คำถาม: CS2 เงินเริ่มต้นกับเวลาระเบิดตั้งไว้เท่าไหร่
- Intent ที่คาด: `game_setting`
- Route/Mode: `service_fee` / `pipeline:rag_direct_curated`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: บริการ PC ในระบบจองมีระยะเวลา 60 min แต่ในข้อมูลที่ดึงมาและในรูป Service Fee 2026 ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ จึงยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง
- Keyword ที่ขาดใน first line: `$800, 40 วินาที`
- Keyword ที่ขาดในคำตอบรวม: `$800, 40 วินาที`
- Retrieved: `curated_service_fee_pc_unknown, curated_service_fee_2026_full_table, curated_user_group_alias_psu_student_staff`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `service_fee` จึงตอบ `บริการ PC ในระบบจองมีระยะเวลา 60 min แต่ในข้อมูลที่ดึงมาและในรูป Service Fee 2026 ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ จึงยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง` ซึ่งไม่ใช่คำตอบของคำถาม `CS2 เงินเริ่มต้นกับเวลาระเบิดตั้งไว้เท่าไหร่`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น $800, 40 วินาที

### 24. [FAIL] competition_cs2_v2_024

- คำถาม: CS2 ชนะกี่รอบก่อนถึงชนะในแผนที่
- Intent ที่คาด: `game_setting`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
- Keyword ที่ขาดใน first line: `13 รอบ`
- Keyword ที่ขาดในคำตอบรวม: `13 รอบ`
- Retrieved: `cs2_map_pool`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `cs2_map_pool` ทำให้คำตอบแรกเป็น `CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train` แต่คำถามต้องการ intent `game_setting` และยังขาด `13 รอบ`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น 13 รอบ

### 25. [FAIL] competition_cs2_v2_025

- คำถาม: CS2 เล่นสูงสุดกี่รอบก่อน overtime
- Intent ที่คาด: `game_setting`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
- Keyword ที่ขาดใน first line: `24 รอบ, 12 รอบ`
- Keyword ที่ขาดในคำตอบรวม: `24 รอบ, 12 รอบ`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends` ซึ่งไม่ใช่คำตอบของคำถาม `CS2 เล่นสูงสุดกี่รอบก่อน overtime`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น 24 รอบ, 12 รอบ

### 26. [FAIL] competition_cs2_v2_026

- คำถาม: CS2 overtime เล่นยังไง
- Intent ที่คาด: `game_setting`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
- Keyword ที่ขาดใน first line: `ฝั่งละ 3 รอบ, 4 ใน 6, $10,000`
- Keyword ที่ขาดในคำตอบรวม: `ฝั่งละ 3 รอบ, 4 ใน 6, $10,000`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends` ซึ่งไม่ใช่คำตอบของคำถาม `CS2 overtime เล่นยังไง`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น ฝั่งละ 3 รอบ, 4 ใน 6, $10,000

### 27. [FAIL] competition_cs2_v2_027

- คำถาม: CS2 ต่อเวลาได้จำกัดกี่ครั้ง
- Intent ที่คาด: `game_setting`
- Route/Mode: `schedule` / `pipeline:schedule_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน
- Keyword ที่ขาดใน first line: `ไม่จำกัด`
- Keyword ที่ขาดในคำตอบรวม: `ไม่จำกัด`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `schedule` จึงตอบ `เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน` ซึ่งไม่ใช่คำตอบของคำถาม `CS2 ต่อเวลาได้จำกัดกี่ครั้ง`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น ไม่จำกัด

### 28. [PASS] competition_cs2_v2_028

- คำถาม: CS2 map pool มีอะไรบ้าง
- Intent ที่คาด: `map_pool`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `cs2_map_pool`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: Ancient, Anubis, Dust 2, Train

### 29. [PASS] competition_cs2_v2_029

- คำถาม: CS2 มี Mirage กับ Nuke ในแผนที่แข่งไหม
- Intent ที่คาด: `map_pool`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `cs2_map_pool`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: Mirage, Nuke

### 30. [FAIL] competition_cs2_v2_030

- คำถาม: CS2 เลือกแผนที่ผ่านอะไร
- Intent ที่คาด: `map_pool`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
- Keyword ที่ขาดใน first line: `MAPBAN.GG`
- Keyword ที่ขาดในคำตอบรวม: `MAPBAN.GG`
- Retrieved: `cs2_map_pool`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `MAPBAN.GG` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: MAPBAN.GG

### 31. [FAIL] competition_cs2_v2_031

- คำถาม: CS2 เลือกฝั่งด้วยวิธีไหน
- Intent ที่คาด: `side_selection`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
- Keyword ที่ขาดใน first line: `ดวลมีด, เลือกฝั่ง`
- Keyword ที่ขาดในคำตอบรวม: `ดวลมีด, เลือกฝั่ง`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends` ซึ่งไม่ใช่คำตอบของคำถาม `CS2 เลือกฝั่งด้วยวิธีไหน`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: ดวลมีด, เลือกฝั่ง

### 32. [PASS] competition_cs2_v2_032

- คำถาม: CS2 technical pause ขอได้กี่ครั้งและนานเท่าไหร่
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `cs2_pause_policy`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น 2 ครั้ง, 10 นาที

### 33. [FAIL] competition_cs2_v2_033

- คำถาม: CS2 เครื่องมีปัญหาต้องแจ้งใครตอน technical pause
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
- Keyword ที่ขาดใน first line: `กรรมการ, ทันที`
- Keyword ที่ขาดในคำตอบรวม: `กรรมการ, ทันที`
- Retrieved: `cs2_pause_policy`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `กรรมการ, ทันที` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น กรรมการ, ทันที

### 34. [PASS] competition_cs2_v2_034

- คำถาม: CS2 tactical timeout ได้กี่ครั้ง ครั้งละกี่วินาที
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `cs2_pause_policy`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น 4 ครั้ง, 30 วินาที

### 35. [FAIL] competition_cs2_v2_035

- คำถาม: CS2 ขอเวลานอกใช้ได้ช่วงไหน
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
- Keyword ที่ขาดใน first line: `Freeze time`
- Keyword ที่ขาดในคำตอบรวม: `Freeze time`
- Retrieved: `cs2_pause_policy`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `Freeze time` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น Freeze time

### 36. [FAIL] competition_cs2_v2_036

- คำถาม: CS2 ใช้บัคแผนที่หรือ Engine ได้ไหม
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
- Keyword ที่ขาดใน first line: `ห้าม, บัค, ปรับแพ้`
- Keyword ที่ขาดในคำตอบรวม: `ห้าม, บัค, ปรับแพ้`
- Retrieved: `cs2_map_pool`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `cs2_map_pool` ทำให้คำตอบแรกเป็น `CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train` แต่คำถามต้องการ intent `penalty` และยังขาด `ห้าม, บัค, ปรับแพ้`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น ห้าม, บัค, ปรับแพ้

### 37. [FAIL] competition_cs2_v2_037

- คำถาม: CS2 ดูสตรีมสดระหว่างแข่งได้ไหม
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
- Keyword ที่ขาดใน first line: `ห้าม, สตรีม`
- Keyword ที่ขาดในคำตอบรวม: `ห้าม, สตรีม`
- Retrieved: `cs2_pause_policy`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `cs2_pause_policy` ทำให้คำตอบแรกเป็น `ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที` แต่คำถามต้องการ intent `penalty` และยังขาด `ห้าม, สตรีม`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น ห้าม, สตรีม

### 38. [FAIL] competition_cs2_v2_038

- คำถาม: CS2 พฤติกรรมเหยียดหรือวาจาสร้างความเกลียดชังผิดกติกาไหม
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:no_answer`
- Cause: `no_answer_despite_data`
- Style: `no_answer` - รูปแบบสุภาพ แต่ไม่ควรตอบไม่พบข้อมูลถ้าข้อมูลมีอยู่ใน competition chunks
- First line ที่ AI ตอบ: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด competition_rules ตอนนี้ครับ
- Keyword ที่ขาดใน first line: `ห้าม, เกลียดชัง`
- Keyword ที่ขาดในคำตอบรวม: `ห้าม, เกลียดชัง`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: ระบบตอบไม่พบข้อมูล ทั้งที่ Ground Truth สร้างจากข้อมูลใน competition chunks จึงควร fallback ไปค้น chunk/LLM ต่อ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น ห้าม, เกลียดชัง

### 39. [FAIL] competition_cs2_v2_039

- คำถาม: CS2 นำคีย์บอร์ดเมาส์ส่วนตัวไปเองได้ไหม
- Intent ที่คาด: `equipment`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
- Keyword ที่ขาดใน first line: `คีย์บอร์ด, เมาส์, มาเองได้`
- Keyword ที่ขาดในคำตอบรวม: `คีย์บอร์ด, เมาส์, มาเองได้`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends` ซึ่งไม่ใช่คำตอบของคำถาม `CS2 นำคีย์บอร์ดเมาส์ส่วนตัวไปเองได้ไหม`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น คีย์บอร์ด, เมาส์, มาเองได้

### 40. [FAIL] competition_cs2_v2_040

- คำถาม: CS2 ผู้จัดเตรียมอุปกรณ์อะไรให้บ้าง
- Intent ที่คาด: `equipment`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train
- Keyword ที่ขาดใน first line: `PC, จอภาพ, โต๊ะ, เก้าอี้`
- Keyword ที่ขาดในคำตอบรวม: `PC, จอภาพ, โต๊ะ, เก้าอี้`
- Retrieved: `cs2_map_pool`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `cs2_map_pool` ทำให้คำตอบแรกเป็น `CS2 ใช้แผนที่ Ancient, Anubis, Dust 2, Inferno, Mirage, Nuke และ Train` แต่คำถามต้องการ intent `equipment` และยังขาด `PC, จอภาพ, โต๊ะ, เก้าอี้`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น PC, จอภาพ, โต๊ะ, เก้าอี้

### 41. [FAIL] competition_cs2_v2_041

- คำถาม: CS2 ปรับ crosshair หรือ resolution ได้ไหม
- Intent ที่คาด: `game_setting`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
- Keyword ที่ขาดใน first line: `Crosshair, Resolution, Brightness`
- Keyword ที่ขาดในคำตอบรวม: `Crosshair, Resolution, Brightness`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends` ซึ่งไม่ใช่คำตอบของคำถาม `CS2 ปรับ crosshair หรือ resolution ได้ไหม`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น Crosshair, Resolution, Brightness

### 42. [FAIL] competition_cs2_v2_042

- คำถาม: CS2 ใช้ macro หรือ script ได้หรือเปล่า
- Intent ที่คาด: `equipment`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
- Keyword ที่ขาดใน first line: `ห้าม, สคริปต์, มาโคร`
- Keyword ที่ขาดในคำตอบรวม: `ห้าม, สคริปต์, มาโคร`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends` ซึ่งไม่ใช่คำตอบของคำถาม `CS2 ใช้ macro หรือ script ได้หรือเปล่า`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น ห้าม, สคริปต์, มาโคร

### 43. [FAIL] competition_cs2_v2_043

- คำถาม: CS2 ติดตั้งโปรแกรมเองบนคอมแข่งได้ไหม
- Intent ที่คาด: `equipment`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
- Keyword ที่ขาดใน first line: `ห้าม, ติดตั้งโปรแกรม`
- Keyword ที่ขาดในคำตอบรวม: `ห้าม, ติดตั้งโปรแกรม`
- Retrieved: `cs2_pause_policy`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `cs2_pause_policy` ทำให้คำตอบแรกเป็น `ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที` แต่คำถามต้องการ intent `equipment` และยังขาด `ห้าม, ติดตั้งโปรแกรม`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น ห้าม, ติดตั้งโปรแกรม

### 44. [FAIL] competition_cs2_v2_044

- คำถาม: CS2 เข้าโซเชียลบนคอมแข่งได้ไหม
- Intent ที่คาด: `equipment`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
- Keyword ที่ขาดใน first line: `ห้าม, โซเชียลมีเดีย`
- Keyword ที่ขาดในคำตอบรวม: `ห้าม, โซเชียลมีเดีย`
- Retrieved: `cs2_pause_policy`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `cs2_pause_policy` ทำให้คำตอบแรกเป็น `ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที` แต่คำถามต้องการ intent `equipment` และยังขาด `ห้าม, โซเชียลมีเดีย`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น ห้าม, โซเชียลมีเดีย

### 45. [FAIL] competition_cs2_v2_045

- คำถาม: CS2 ช่วงเตรียมตัวมีคนในพื้นที่ได้ไม่เกินกี่คน
- Intent ที่คาด: `area_rules`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
- Keyword ที่ขาดใน first line: `ไม่เกิน 6 คน`
- Keyword ที่ขาดในคำตอบรวม: `ไม่เกิน 6 คน`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends` ซึ่งไม่ใช่คำตอบของคำถาม `CS2 ช่วงเตรียมตัวมีคนในพื้นที่ได้ไม่เกินกี่คน`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น ไม่เกิน 6 คน

### 46. [FAIL] competition_cs2_v2_046

- คำถาม: CS2 เอามือถือหรือ smart watch เข้าพื้นที่แข่งได้ไหม
- Intent ที่คาด: `area_rules`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
- Keyword ที่ขาดใน first line: `ห้าม, โทรศัพท์มือถือ, สมาร์ทวอทช์`
- Keyword ที่ขาดในคำตอบรวม: `ห้าม, โทรศัพท์มือถือ, สมาร์ทวอทช์`
- Retrieved: `cs2_pause_policy`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `cs2_pause_policy` ทำให้คำตอบแรกเป็น `ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที` แต่คำถามต้องการ intent `area_rules` และยังขาด `ห้าม, โทรศัพท์มือถือ, สมาร์ทวอทช์`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น ห้าม, โทรศัพท์มือถือ, สมาร์ทวอทช์

### 47. [FAIL] competition_cs2_v2_047

- คำถาม: CS2 หัวหน้าทีมนำเอกสารเข้าไปได้ไหม
- Intent ที่คาด: `area_rules`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที
- Keyword ที่ขาดใน first line: `หัวหน้าทีม, เอกสาร, กรรมการ`
- Keyword ที่ขาดในคำตอบรวม: `หัวหน้าทีม, กรรมการ`
- Retrieved: `cs2_pause_policy`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `cs2_pause_policy` ทำให้คำตอบแรกเป็น `ต่างกันคือ CS2 Technical Pause ขอได้ทีมละ 2 ครั้ง รวมไม่เกิน 10 นาที ส่วน Tactical Timeout ขอได้ทีมละ 4 ครั้ง ครั้งละ 30 วินาที` แต่คำถามต้องการ intent `area_rules` และยังขาด `หัวหน้าทีม, กรรมการ`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น หัวหน้าทีม, เอกสาร, กรรมการ

### 48. [FAIL] competition_cs2_v2_048

- คำถาม: CS2 อนุญาตอาหารหรือเครื่องดื่มอะไรในพื้นที่แข่ง
- Intent ที่คาด: `area_rules`
- Route/Mode: `competition_rules` / `pipeline:rag_direct_curated`
- Cause: `rag_partial_answer`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: 6. อุปกรณ์และการตั้งค่าเกม
- Keyword ที่ขาดใน first line: `น้ำดื่ม, ปิดสนิท, หมากฝรั่ง`
- Keyword ที่ขาดในคำตอบรวม: `น้ำดื่ม, ปิดสนิท, หมากฝรั่ง`
- Retrieved: `competition_rules_cs2_psu_phuket_2026_s39_c01, competition_rules_cs2_psu_phuket_2026_s40_c01, competition_rules_cs2_psu_phuket_2026_s42_c01`
- ทำไมผิด/ปัญหาคืออะไร: RAG ดึงบริบทได้บางส่วน แต่คำตอบแรก `6. อุปกรณ์และการตั้งค่าเกม` ยังไม่ใช่ประเด็นที่ถามและขาด `น้ำดื่ม, ปิดสนิท, หมากฝรั่ง`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น น้ำดื่ม, ปิดสนิท, หมากฝรั่ง

## Arena of Valor (RoV)

### 49. [FAIL] competition_rov_v2_001

- คำถาม: Blueket Games RoV แข่งวันไหน
- Intent ที่คาด: `schedule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
- Keyword ที่ขาดใน first line: `11 กันยายน 2568`
- Keyword ที่ขาดในคำตอบรวม: `11 กันยายน 2568`
- Retrieved: `rov_rematch_first_blood`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `rov_rematch_first_blood` ทำให้คำตอบแรกเป็น `RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน` แต่คำถามต้องการ intent `schedule` และยังขาด `11 กันยายน 2568`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยวัน เวลา หรือสถานที่ที่ถามก่อน เช่น 11 กันยายน 2568

### 50. [PASS] competition_rov_v2_002

- คำถาม: RoV ลงทะเบียนช่วงกี่โมง
- Intent ที่คาด: `schedule`
- Route/Mode: `general` / `pipeline:rag_direct_curated`
- Cause: `pass`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: 1. กำหนดการแข่งขัน
- Keyword ที่ขาดใน first line: `8.00, 8.30`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `competition_rules_rov_blueket_2025_men_s03_c01, competition_rules_cs2_psu_phuket_2026_s12_c01, competition_rules_valorant_psu_phuket_2026_s02_c01`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยวัน เวลา หรือสถานที่ที่ถามก่อน เช่น 8.00, 8.30

### 51. [FAIL] competition_rov_v2_003

- คำถาม: RoV แบ่งสายการแข่งขันกี่โมง
- Intent ที่คาด: `schedule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ
- Keyword ที่ขาดใน first line: `8.30, 8.40`
- Keyword ที่ขาดในคำตอบรวม: `8.30, 8.40`
- Retrieved: `rov_format_bo3_all_rounds`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `rov_format_bo3_all_rounds` ทำให้คำตอบแรกเป็น `RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ` แต่คำถามต้องการ intent `schedule` และยังขาด `8.30, 8.40`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยวัน เวลา หรือสถานที่ที่ถามก่อน เช่น 8.30, 8.40

### 52. [FAIL] competition_rov_v2_004

- คำถาม: RoV รอบ 5 ทีมแข่งช่วงเวลาไหน
- Intent ที่คาด: `schedule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น
- Keyword ที่ขาดใน first line: `8.40, 10.00, BO3`
- Keyword ที่ขาดในคำตอบรวม: `8.40, 10.00, BO3`
- Retrieved: `rov_late_start_forfeit`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `rov_late_start_forfeit` ทำให้คำตอบแรกเป็น `RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น` แต่คำถามต้องการ intent `schedule` และยังขาด `8.40, 10.00, BO3`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยวัน เวลา หรือสถานที่ที่ถามก่อน เช่น 8.40, 10.00, BO3

### 53. [FAIL] competition_rov_v2_005

- คำถาม: RoV รอบรองคู่ที่ 1 เริ่มประมาณกี่โมง
- Intent ที่คาด: `schedule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ
- Keyword ที่ขาดใน first line: `10.00, 11.30`
- Keyword ที่ขาดในคำตอบรวม: `10.00, 11.30`
- Retrieved: `rov_format_bo3_all_rounds`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `rov_format_bo3_all_rounds` ทำให้คำตอบแรกเป็น `RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ` แต่คำถามต้องการ intent `schedule` และยังขาด `10.00, 11.30`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยวัน เวลา หรือสถานที่ที่ถามก่อน เช่น 10.00, 11.30

### 54. [FAIL] competition_rov_v2_006

- คำถาม: RoV รอบรองคู่ที่ 2 อยู่ช่วงเวลาไหน
- Intent ที่คาด: `schedule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ
- Keyword ที่ขาดใน first line: `12.30, 14.00`
- Keyword ที่ขาดในคำตอบรวม: `12.30, 14.00`
- Retrieved: `rov_format_bo3_all_rounds`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `rov_format_bo3_all_rounds` ทำให้คำตอบแรกเป็น `RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ` แต่คำถามต้องการ intent `schedule` และยังขาด `12.30, 14.00`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยวัน เวลา หรือสถานที่ที่ถามก่อน เช่น 12.30, 14.00

### 55. [FAIL] competition_rov_v2_007

- คำถาม: RoV รอบชิงอันดับ 3 แข่งกี่โมงถึงกี่โมง
- Intent ที่คาด: `schedule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ
- Keyword ที่ขาดใน first line: `14.00, 15.30`
- Keyword ที่ขาดในคำตอบรวม: `14.00, 15.30`
- Retrieved: `rov_format_bo3_all_rounds`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `rov_format_bo3_all_rounds` ทำให้คำตอบแรกเป็น `RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ` แต่คำถามต้องการ intent `schedule` และยังขาด `14.00, 15.30`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยวัน เวลา หรือสถานที่ที่ถามก่อน เช่น 14.00, 15.30

### 56. [FAIL] competition_rov_v2_008

- คำถาม: RoV รอบชิงชนะเลิศแข่งช่วงไหน
- Intent ที่คาด: `schedule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ
- Keyword ที่ขาดใน first line: `15.30, 17.00`
- Keyword ที่ขาดในคำตอบรวม: `15.30, 17.00`
- Retrieved: `rov_format_bo3_all_rounds`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `rov_format_bo3_all_rounds` ทำให้คำตอบแรกเป็น `RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ` แต่คำถามต้องการ intent `schedule` และยังขาด `15.30, 17.00`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยวัน เวลา หรือสถานที่ที่ถามก่อน เช่น 15.30, 17.00

### 57. [FAIL] competition_rov_v2_009

- คำถาม: RoV แข่งที่อาคารไหนของ PSU Esports Studio Phuket
- Intent ที่คาด: `schedule_location`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
- Keyword ที่ขาดใน first line: `อาคาร 5, ชั้น 1`
- Keyword ที่ขาดในคำตอบรวม: `อาคาร 5, ชั้น 1`
- Retrieved: `rov_pause_disconnect`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `rov_pause_disconnect` ทำให้คำตอบแรกเป็น `RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ` แต่คำถามต้องการ intent `schedule_location` และยังขาด `อาคาร 5, ชั้น 1`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยวัน เวลา หรือสถานที่ที่ถามก่อน เช่น อาคาร 5, ชั้น 1

### 58. [PASS] competition_rov_v2_010

- คำถาม: RoV แข่งออนไลน์หรือออฟไลน์
- Intent ที่คาด: `format`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `details_have_answer_but_first_line_missing` - ข้อมูลที่ต้องการอาจอยู่ในรายละเอียด/หลักฐาน แต่บรรทัดแรกยังไม่ตอบสิ่งที่ถามโดยตรง
- First line ที่ AI ตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ
- Keyword ที่ขาดใน first line: `ออฟไลน์`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `rov_format_bo3_all_rounds`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น ออฟไลน์

### 59. [PASS] competition_rov_v2_011

- คำถาม: แข่ง ROV ต้องเล่นกี่เกม
- Intent ที่คาด: `format`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `rov_format_bo3_all_rounds`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น BO3, ทุกรอบ

### 60. [PASS] competition_rov_v2_012

- คำถาม: RoV รายการนี้เป็น Best of 3 ทุกด่านไหม
- Intent ที่คาด: `format`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `rov_format_bo3_all_rounds`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น Best of 3, ทุกรอบ

### 61. [FAIL] competition_rov_v2_013

- คำถาม: RoV เกมแรกใครได้ฝั่งสีน้ำเงิน
- Intent ที่คาด: `side_selection`
- Route/Mode: `games` / `pipeline:rag_direct_curated`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: เกมยอดนิยมที่ปรากฏบนหน้า Home ได้แก่ Gran Turismo 7, Mario Kart 8 Deluxe, Tekken 8 และ Beat Saber
- Keyword ที่ขาดใน first line: `ด้านบน, สายการแข่งขัน, สีน้ำเงิน`
- Keyword ที่ขาดในคำตอบรวม: `ด้านบน, สายการแข่งขัน, สีน้ำเงิน`
- Retrieved: `curated_home_popular_games_list, curated_games_popular, curated_games_cockpit`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `เกมยอดนิยมที่ปรากฏบนหน้า Home ได้แก่ Gran Turismo 7, Mario Kart 8 Deluxe, Tekken 8 และ Beat Saber` ซึ่งไม่ใช่คำตอบของคำถาม `RoV เกมแรกใครได้ฝั่งสีน้ำเงิน`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: ด้านบน, สายการแข่งขัน, สีน้ำเงิน

### 62. [FAIL] competition_rov_v2_014

- คำถาม: RoV เกมถัดไปใครเลือกฝั่ง
- Intent ที่คาด: `side_selection`
- Route/Mode: `games` / `pipeline:rag_direct_curated`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: Cockpit ใช้เล่นเกม Gran Turismo 7 (Single Player) ได้ โดยปรากฏในรายการบริการ Cockpit #1 (1 Person) 60 min ของระบบจอง
- Keyword ที่ขาดใน first line: `ผู้ที่แพ้, เลือกฝั่ง`
- Keyword ที่ขาดในคำตอบรวม: `ผู้ที่แพ้, เลือกฝั่ง`
- Retrieved: `curated_games_cockpit, curated_home_popular_games_list, curated_games_pc`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `Cockpit ใช้เล่นเกม Gran Turismo 7 (Single Player) ได้ โดยปรากฏในรายการบริการ Cockpit #1 (1 Person) 60 min ของระบบจอง` ซึ่งไม่ใช่คำตอบของคำถาม `RoV เกมถัดไปใครเลือกฝั่ง`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: ผู้ที่แพ้, เลือกฝั่ง

### 63. [FAIL] competition_rov_v2_015

- คำถาม: กรรมการ RoV แจ้งอะไรให้ทีมเข้าห้องแข่ง
- Intent ที่คาด: `match_process`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
- Keyword ที่ขาดใน first line: `หมายเลขห้อง`
- Keyword ที่ขาดในคำตอบรวม: `หมายเลขห้อง`
- Retrieved: `rov_device_mobile_only`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `rov_device_mobile_only` ทำให้คำตอบแรกเป็น `RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad` แต่คำถามต้องการ intent `match_process` และยังขาด `หมายเลขห้อง`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: หมายเลขห้อง

### 64. [PASS] competition_rov_v2_016

- คำถาม: RoV มาสายเกิน 15 นาทีเป็นอะไร
- Intent ที่คาด: `late_start`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `rov_late_start_forfeit`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น 15 นาที, ปรับแพ้

### 65. [PASS] competition_rov_v2_017

- คำถาม: กติกา RoV ถ้าเริ่มแข่งช้าเกินเวลาที่กำหนดลงโทษยังไง
- Intent ที่คาด: `late_start`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: RoV ถ้าเริ่มแข่งล่าช้าเกิน 15 นาที จะถูกปรับแพ้ในรอบนั้น
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `rov_late_start_forfeit`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น ล่าช้า, ปรับแพ้

### 66. [FAIL] competition_rov_v2_018

- คำถาม: RoV ต้องมีฮีโร่อย่างน้อยกี่ตัว
- Intent ที่คาด: `hero_rule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
- Keyword ที่ขาดใน first line: `18 ตัว`
- Keyword ที่ขาดในคำตอบรวม: `18 ตัว`
- Retrieved: `rov_team_size_active_players`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `rov_team_size_active_players` ทำให้คำตอบแรกเป็น `ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้` แต่คำถามต้องการ intent `hero_rule` และยังขาด `18 ตัว`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น 18 ตัว

### 67. [FAIL] competition_rov_v2_019

- คำถาม: RoV ใช้ระบบแบนเลือกฮีโร่แบบไหน
- Intent ที่คาด: `hero_rule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ
- Keyword ที่ขาดใน first line: `Global Ban/Pick`
- Keyword ที่ขาดในคำตอบรวม: `Global Ban/Pick`
- Retrieved: `rov_format_bo3_all_rounds`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `rov_format_bo3_all_rounds` ทำให้คำตอบแรกเป็น `RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ` แต่คำถามต้องการ intent `hero_rule` และยังขาด `Global Ban/Pick`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น Global Ban/Pick

### 68. [FAIL] competition_rov_v2_020

- คำถาม: RoV ใส่รูนและพลังเสริมได้ไหม
- Intent ที่คาด: `hero_rule`
- Route/Mode: `general` / `pipeline:rag_direct_curated`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: 4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพินิจของกรรมการ ว่าจะเห็นสมควรให้แข่งขันใหม่หรือไม่
- Keyword ที่ขาดใน first line: `รูน, พลังเสริม, ตามความต้องการ`
- Keyword ที่ขาดในคำตอบรวม: `รูน, พลังเสริม, ตามความต้องการ`
- Retrieved: `competition_rules_rov_blueket_2025_men_s06_c02, competition_rules_rov_blueket_2025_men_s06_c01, competition_rules_rov_blueket_2025_men_s06_c03`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `general` จึงตอบ `4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพินิจของกรรมการ ว่าจะเห็นสมควรให้แข่งขันใหม่หรือไม่` ซึ่งไม่ใช่คำตอบของคำถาม `RoV ใส่รูนและพลังเสริมได้ไหม`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น รูน, พลังเสริม, ตามความต้องการ

### 69. [FAIL] competition_rov_v2_021

- คำถาม: RoV เลือกฮีโร่ซ้ำได้ไหม
- Intent ที่คาด: `hero_rule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
- Keyword ที่ขาดใน first line: `ห้าม, ฮีโร่ซ้ำ`
- Keyword ที่ขาดในคำตอบรวม: `ห้าม, ฮีโร่ซ้ำ`
- Retrieved: `rov_pause_disconnect`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `rov_pause_disconnect` ทำให้คำตอบแรกเป็น `RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ` แต่คำถามต้องการ intent `hero_rule` และยังขาด `ห้าม, ฮีโร่ซ้ำ`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น ห้าม, ฮีโร่ซ้ำ

### 70. [PASS] competition_rov_v2_022

- คำถาม: RoV ใช้สกินพิเศษได้หรือเปล่า
- Intent ที่คาด: `skin`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: RoV ให้ใช้เฉพาะ Default Skin เท่านั้น
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `rov_skin_default_only`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น Default Skin

### 71. [PASS] competition_rov_v2_023

- คำถาม: RoV แต่ละทีม pause ได้กี่ครั้ง ครั้งละเท่าไหร่
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `rov_pause_disconnect`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น 5 ครั้ง, 1 นาที

### 72. [FAIL] competition_rov_v2_024

- คำถาม: RoV ถ้า pause เกิน 1 นาทีอีกทีมทำอะไรได้
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
- Keyword ที่ขาดใน first line: `Resume`
- Keyword ที่ขาดในคำตอบรวม: `Resume`
- Retrieved: `rov_pause_disconnect`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `Resume` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น Resume

### 73. [FAIL] competition_rov_v2_025

- คำถาม: RoV หลุดเพราะเน็ตล่มหรือเซิร์ฟเวอร์พังต้องทำยังไง
- Intent ที่คาด: `rematch`
- Route/Mode: `general` / `pipeline:no_answer`
- Cause: `wrong_route`
- Style: `no_answer` - รูปแบบสุภาพ แต่ไม่ควรตอบไม่พบข้อมูลถ้าข้อมูลมีอยู่ใน competition chunks
- First line ที่ AI ตอบ: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
- Keyword ที่ขาดใน first line: `แจ้งทีมงาน, ดุลยพินิจ, กรรมการ`
- Keyword ที่ขาดในคำตอบรวม: `แจ้งทีมงาน, ดุลยพินิจ, กรรมการ`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `general` จึงตอบ `ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ` ซึ่งไม่ใช่คำตอบของคำถาม `RoV หลุดเพราะเน็ตล่มหรือเซิร์ฟเวอร์พังต้องทำยังไง`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น แจ้งทีมงาน, ดุลยพินิจ, กรรมการ

### 74. [FAIL] competition_rov_v2_026

- คำถาม: RoV ขอเริ่มเกมใหม่ได้ตอนไหนก่อน First Blood
- Intent ที่คาด: `rematch`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
- Keyword ที่ขาดใน first line: `เริ่มเกมใหม่`
- Keyword ที่ขาดในคำตอบรวม: `เริ่มเกมใหม่`
- Retrieved: `rov_rematch_first_blood`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `เริ่มเกมใหม่` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น First Blood, 2 นาที, เริ่มเกมใหม่

### 75. [FAIL] competition_rov_v2_027

- คำถาม: RoV ถ้าเกิด First Blood แล้วขอ remake ได้ไหม
- Intent ที่คาด: `rematch`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน
- Keyword ที่ขาดใน first line: `อนุญาต, คู่แข่ง, กรรมการ`
- Keyword ที่ขาดในคำตอบรวม: `อนุญาต, คู่แข่ง, กรรมการ`
- Retrieved: `rov_rematch_first_blood`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `RoV ขอแข่งใหม่ได้เฉพาะก่อนเกิด First Blood และก่อนเวลาเกม 2 นาที หากเกิด First Blood แล้วหรือเกิน 2 นาที ต้องได้รับความยินยอมจากฝ่ายตรงข้ามหรือผู้ตัดสิน` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `อนุญาต, คู่แข่ง, กรรมการ` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น First Blood, อนุญาต, คู่แข่ง, กรรมการ

### 76. [FAIL] competition_rov_v2_028

- คำถาม: RoV เจตนากด pause ก่อกวนโดนอะไร
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
- Keyword ที่ขาดใน first line: `ปรับแพ้, ตัดสิทธิ์`
- Keyword ที่ขาดในคำตอบรวม: `ปรับแพ้, ตัดสิทธิ์`
- Retrieved: `rov_pause_disconnect`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `ปรับแพ้, ตัดสิทธิ์` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น ปรับแพ้, ตัดสิทธิ์

### 77. [FAIL] competition_rov_v2_029

- คำถาม: RoV พักหลังจบทุกสองเกมกี่นาที
- Intent ที่คาด: `break_time`
- Route/Mode: `games` / `pipeline:rag_direct_curated`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: เกมยอดนิยมที่ปรากฏบนหน้า Home ได้แก่ Gran Turismo 7, Mario Kart 8 Deluxe, Tekken 8 และ Beat Saber
- Keyword ที่ขาดใน first line: `5 นาที`
- Keyword ที่ขาดในคำตอบรวม: `5 นาที`
- Retrieved: `curated_home_popular_games_list, curated_games_cockpit, curated_games_pc`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `เกมยอดนิยมที่ปรากฏบนหน้า Home ได้แก่ Gran Turismo 7, Mario Kart 8 Deluxe, Tekken 8 และ Beat Saber` ซึ่งไม่ใช่คำตอบของคำถาม `RoV พักหลังจบทุกสองเกมกี่นาที`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: 5 นาที

### 78. [FAIL] competition_rov_v2_030

- คำถาม: RoV ไม่กลับมาหลังเวลาพักที่กำหนดเสี่ยงอะไร
- Intent ที่คาด: `break_time`
- Route/Mode: `schedule` / `pipeline:schedule_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน
- Keyword ที่ขาดใน first line: `ปรับ, แพ้`
- Keyword ที่ขาดในคำตอบรวม: `ปรับ, แพ้`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `schedule` จึงตอบ `เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน` ซึ่งไม่ใช่คำตอบของคำถาม `RoV ไม่กลับมาหลังเวลาพักที่กำหนดเสี่ยงอะไร`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: ปรับ, แพ้

### 79. [FAIL] competition_rov_v2_031

- คำถาม: RoV เกมหยุดเกิน 10 นาทีทีมงานทำอะไรได้
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
- Keyword ที่ขาดใน first line: `10 นาที, เริ่มเกมใหม่`
- Keyword ที่ขาดในคำตอบรวม: `10 นาที, เริ่มเกมใหม่`
- Retrieved: `rov_pause_disconnect`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `10 นาที, เริ่มเกมใหม่` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น 10 นาที, เริ่มเกมใหม่

### 80. [PASS] competition_rov_v2_032

- คำถาม: RoV เครื่องร้อนพักได้กี่นาที
- Intent ที่คาด: `pause`
- Route/Mode: `general` / `pipeline:rag_direct_curated`
- Cause: `pass`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: 4.5.6.1.2. อุปกรณ์พกพาหรือซอฟต์แวร์ทำงานผิดปกติ
- Keyword ที่ขาดใน first line: `เครื่องร้อน, 5 นาที`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `competition_rules_rov_blueket_2025_men_s06_c04, competition_rules_tekken8_psu_esports_s02_c01, competition_rules_valorant_psu_phuket_2026_s02_c01`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น เครื่องร้อน, 5 นาที

### 81. [FAIL] competition_rov_v2_033

- คำถาม: RoV ระหว่าง pause ผู้เล่นคุยกันได้ไหม
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
- Keyword ที่ขาดใน first line: `ห้าม, สื่อสาร`
- Keyword ที่ขาดในคำตอบรวม: `ห้าม, สื่อสาร`
- Retrieved: `rov_pause_disconnect`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `ห้าม, สื่อสาร` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น ห้าม, สื่อสาร

### 82. [FAIL] competition_rov_v2_034

- คำถาม: RoV บทลงโทษการ pause ผิดครั้งแรกคืออะไร
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
- Keyword ที่ขาดใน first line: `ครั้งที่ 1, ตักเตือน`
- Keyword ที่ขาดในคำตอบรวม: `ครั้งที่ 1, ตักเตือน`
- Retrieved: `rov_pause_disconnect`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `ครั้งที่ 1, ตักเตือน` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น ครั้งที่ 1, ตักเตือน

### 83. [FAIL] competition_rov_v2_035

- คำถาม: RoV pause ผิดครั้งที่ 2 โดนอะไร
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
- Keyword ที่ขาดใน first line: `ครั้งที่ 2, เพิ่มสิทธิการแบนฮีโร่, 1 ครั้ง`
- Keyword ที่ขาดในคำตอบรวม: `ครั้งที่ 2, เพิ่มสิทธิการแบนฮีโร่, 1 ครั้ง`
- Retrieved: `rov_pause_disconnect`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `ครั้งที่ 2, เพิ่มสิทธิการแบนฮีโร่, 1 ครั้ง` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น ครั้งที่ 2, เพิ่มสิทธิการแบนฮีโร่, 1 ครั้ง

### 84. [FAIL] competition_rov_v2_036

- คำถาม: RoV pause ผิดครั้งที่ 3 โดนอะไร
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
- Keyword ที่ขาดใน first line: `ครั้งที่ 3, เพิ่มสิทธิการแบนฮีโร่, 2 ครั้ง`
- Keyword ที่ขาดในคำตอบรวม: `ครั้งที่ 3, เพิ่มสิทธิการแบนฮีโร่, 2 ครั้ง`
- Retrieved: `rov_pause_disconnect`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `ครั้งที่ 3, เพิ่มสิทธิการแบนฮีโร่, 2 ครั้ง` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น ครั้งที่ 3, เพิ่มสิทธิการแบนฮีโร่, 2 ครั้ง

### 85. [PASS] competition_rov_v2_037

- คำถาม: RoV ใช้อุปกรณ์อะไรแข่ง
- Intent ที่คาด: `equipment`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `rov_device_mobile_only`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น โทรศัพท์มือถือ

### 86. [PASS] competition_rov_v2_038

- คำถาม: RoV ใช้ iPad หรือ Tablet ลงแข่งได้ไหม
- Intent ที่คาด: `equipment`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `rov_device_mobile_only`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น ไม่อนุญาต, Tablet, iPad

### 87. [FAIL] competition_rov_v2_039

- คำถาม: RoV เอาปลั๊กพ่วงกับอุปกรณ์ชาร์จส่วนตัวได้ไหม
- Intent ที่คาด: `equipment`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad
- Keyword ที่ขาดใน first line: `ปลั๊กพ่วง, อุปกรณ์ชาร์จ`
- Keyword ที่ขาดในคำตอบรวม: `ปลั๊กพ่วง, อุปกรณ์ชาร์จ`
- Retrieved: `rov_device_mobile_only`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `rov_device_mobile_only` ทำให้คำตอบแรกเป็น `RoV ใช้โทรศัพท์มือถือในการแข่งขัน ไม่อนุญาตให้ใช้ Tablet หรือ iPad` แต่คำถามต้องการ intent `equipment` และยังขาด `ปลั๊กพ่วง, อุปกรณ์ชาร์จ`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น ปลั๊กพ่วง, อุปกรณ์ชาร์จ

### 88. [FAIL] competition_rov_v2_040

- คำถาม: RoV ใช้คำพูดไม่สุภาพหรือเสียดสีโดนอะไร
- Intent ที่คาด: `penalty`
- Route/Mode: `rules` / `pipeline:rules_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: กรุณางดส่งเสียงดังเกินควร และห้ามพูดจาดูหมิ่นหรือเสียดสีผู้อื่น
- Keyword ที่ขาดใน first line: `ปรับแพ้, เกมที่พบ`
- Keyword ที่ขาดในคำตอบรวม: `ปรับแพ้, เกมที่พบ`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `rules` จึงตอบ `กรุณางดส่งเสียงดังเกินควร และห้ามพูดจาดูหมิ่นหรือเสียดสีผู้อื่น` ซึ่งไม่ใช่คำตอบของคำถาม `RoV ใช้คำพูดไม่สุภาพหรือเสียดสีโดนอะไร`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น ปรับแพ้, เกมที่พบ

### 89. [FAIL] competition_rov_v2_041

- คำถาม: RoV ส่งผลการแข่งขันเท็จโดนลงโทษยังไง
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ
- Keyword ที่ขาดใน first line: `ปรับแพ้, ตัดสิทธิ์`
- Keyword ที่ขาดในคำตอบรวม: `ปรับแพ้, ตัดสิทธิ์`
- Retrieved: `rov_format_bo3_all_rounds`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `rov_format_bo3_all_rounds` ทำให้คำตอบแรกเป็น `RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ` แต่คำถามต้องการ intent `penalty` และยังขาด `ปรับแพ้, ตัดสิทธิ์`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น ปรับแพ้, ตัดสิทธิ์

### 90. [FAIL] competition_rov_v2_042

- คำถาม: RoV ให้คนอื่นที่ไม่ได้ลงทะเบียนมาแข่งแทนได้ไหม
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:no_answer`
- Cause: `no_answer_despite_data`
- Style: `no_answer` - รูปแบบสุภาพ แต่ไม่ควรตอบไม่พบข้อมูลถ้าข้อมูลมีอยู่ใน competition chunks
- First line ที่ AI ตอบ: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด competition_rules ตอนนี้ครับ
- Keyword ที่ขาดใน first line: `ไม่ตรงตามที่ลงทะเบียน, ปรับแพ้, ตัดสิทธิ์`
- Keyword ที่ขาดในคำตอบรวม: `ไม่ตรงตามที่ลงทะเบียน, ปรับแพ้, ตัดสิทธิ์`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: ระบบตอบไม่พบข้อมูล ทั้งที่ Ground Truth สร้างจากข้อมูลใน competition chunks จึงควร fallback ไปค้น chunk/LLM ต่อ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น ไม่ตรงตามที่ลงทะเบียน, ปรับแพ้, ตัดสิทธิ์

### 91. [FAIL] competition_rov_v2_043

- คำถาม: RoV ห้ามให้คนอื่นเล่นแทนตัวเองไหม
- Intent ที่คาด: `penalty`
- Route/Mode: `rules` / `pipeline:rag_direct_curated`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: ห้ามพกอาวุธหรือของมีคม ห้ามทะเลาะวิวาท และห้ามเล่นการพนัน
- Keyword ที่ขาดใน first line: `เล่นแทน`
- Keyword ที่ขาดในคำตอบรวม: `เล่นแทน`
- Retrieved: `curated_rule_weapons_gambling, curated_rule_noise_language, curated_rule_power_outlet`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `rules` จึงตอบ `ห้ามพกอาวุธหรือของมีคม ห้ามทะเลาะวิวาท และห้ามเล่นการพนัน` ซึ่งไม่ใช่คำตอบของคำถาม `RoV ห้ามให้คนอื่นเล่นแทนตัวเองไหม`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น เล่นแทน, ห้าม

### 92. [FAIL] competition_rov_v2_044

- คำถาม: RoV ถามสรุปรูปแบบแข่งกับสถานที่แบบสั้นๆ
- Intent ที่คาด: `summary`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ
- Keyword ที่ขาดใน first line: `ออฟไลน์, PSU Esports Studio`
- Keyword ที่ขาดในคำตอบรวม: `ออฟไลน์, PSU Esports Studio`
- Retrieved: `rov_format_bo3_all_rounds`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `RoV รายการ Blueket Games 2025 ประเภททีมชาย แข่ง Best of 3 (BO3) ทุกรอบ` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `ออฟไลน์, PSU Esports Studio` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: ออฟไลน์, BO3, PSU Esports Studio

### 93. [FAIL] competition_rov_v2_045

- คำถาม: RoV ถ้าถามเรื่องเวลาแข่งทั้งวันควรตอบหัวข้ออะไรบ้าง
- Intent ที่คาด: `schedule`
- Route/Mode: `competition_rules` / `pipeline:no_answer`
- Cause: `no_answer_despite_data`
- Style: `no_answer` - รูปแบบสุภาพ แต่ไม่ควรตอบไม่พบข้อมูลถ้าข้อมูลมีอยู่ใน competition chunks
- First line ที่ AI ตอบ: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด competition_rules ตอนนี้ครับ
- Keyword ที่ขาดใน first line: `ลงทะเบียน, รอบรอง, รอบชิง`
- Keyword ที่ขาดในคำตอบรวม: `ลงทะเบียน, รอบรอง, รอบชิง`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: ระบบตอบไม่พบข้อมูล ทั้งที่ Ground Truth สร้างจากข้อมูลใน competition chunks จึงควร fallback ไปค้น chunk/LLM ต่อ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยวัน เวลา หรือสถานที่ที่ถามก่อน เช่น ลงทะเบียน, รอบรอง, รอบชิง

### 94. [FAIL] competition_rov_v2_046

- คำถาม: RoV ขอกฎ disconnect แบบเข้าใจง่าย
- Intent ที่คาด: `rematch`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ
- Keyword ที่ขาดใน first line: `pause, First Blood, 2 นาที`
- Keyword ที่ขาดในคำตอบรวม: `pause, First Blood, 2 นาที`
- Retrieved: `rov_pause_disconnect`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `RoV แต่ละทีมสามารถหยุดเกมได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที และเมื่อครบเวลาต้องกลับเข้าแข่งขันต่อ` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `pause, First Blood, 2 นาที` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น pause, First Blood, 2 นาที

### 95. [PASS] competition_rov_v2_047

- คำถาม: RoV มีข้อมูลตัวสำรองชัดเจนไหมในไฟล์นี้
- Intent ที่คาด: `team_size`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `rov_team_size_active_players`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยจำนวนผู้เล่น/ทีมของ Arena of Valor (RoV) ให้ชัด เช่นมีคำว่า 5v5

### 96. [PASS] competition_rov_v2_048

- คำถาม: สมาชิกในทีม ROV ต้องเล่นพร้อมกันฝั่งละกี่คน
- Intent ที่คาด: `team_size`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: ไฟล์กติกา RoV ระบุว่าแข่งขันในโหมด 5v5 จึงยืนยันได้ว่าลงแข่งพร้อมกันฝ่ายละ 5 คน แต่ยังไม่พบจำนวนสมาชิกทีมรวมหรือตัวสำรองที่ระบุชัดเจนในไฟล์นี้
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `rov_team_size_active_players`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยจำนวนผู้เล่น/ทีมของ Arena of Valor (RoV) ให้ชัด เช่นมีคำว่า 5v5, ฝ่ายละ 5 คน

## VALORANT

### 97. [PASS] competition_valorant_v2_001

- คำถาม: VALORANT ทีมละกี่คน
- Intent ที่คาด: `team_size`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `valorant_team_size_players`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยจำนวนผู้เล่น/ทีมของ VALORANT ให้ชัด เช่นมีคำว่า 5 คน

### 98. [PASS] competition_valorant_v2_002

- คำถาม: วาโลต้องส่งผู้เล่นตัวจริงกี่คน
- Intent ที่คาด: `team_size`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: VALORANT แต่ละทีมมีผู้เล่นตัวจริง 5 คน
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `valorant_team_size_players`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยจำนวนผู้เล่น/ทีมของ VALORANT ให้ชัด เช่นมีคำว่า ตัวจริง 5 คน

### 99. [FAIL] competition_valorant_v2_003

- คำถาม: VALORANT Match Prep มีคนได้ไม่เกินกี่คน
- Intent ที่คาด: `area_rules`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
- Keyword ที่ขาดใน first line: `ไม่เกิน 6`
- Keyword ที่ขาดในคำตอบรวม: `ไม่เกิน 6`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends` ซึ่งไม่ใช่คำตอบของคำถาม `VALORANT Match Prep มีคนได้ไม่เกินกี่คน`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น ไม่เกิน 6

### 100. [FAIL] competition_valorant_v2_004

- คำถาม: VALORANT เอามือถือเข้าพื้นที่แข่งได้ไหม
- Intent ที่คาด: `area_rules`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
- Keyword ที่ขาดใน first line: `ห้าม, โทรศัพท์มือถือ`
- Keyword ที่ขาดในคำตอบรวม: `ห้าม, โทรศัพท์มือถือ`
- Retrieved: `valorant_agent_map_restriction`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `valorant_agent_map_restriction` ทำให้คำตอบแรกเป็น `VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง` แต่คำถามต้องการ intent `area_rules` และยังขาด `ห้าม, โทรศัพท์มือถือ`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น ห้าม, โทรศัพท์มือถือ

### 101. [FAIL] competition_valorant_v2_005

- คำถาม: VALORANT หัวหน้าทีมนำโน้ตเข้าได้ไหม
- Intent ที่คาด: `area_rules`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Keyword ที่ขาดใน first line: `หัวหน้าทีม, กรรมการ`
- Keyword ที่ขาดในคำตอบรวม: `หัวหน้าทีม, กรรมการ`
- Retrieved: `valorant_emergency_pause`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `valorant_emergency_pause` ทำให้คำตอบแรกเป็น `VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที` แต่คำถามต้องการ intent `area_rules` และยังขาด `หัวหน้าทีม, กรรมการ`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น หัวหน้าทีม, กรรมการ

### 102. [FAIL] competition_valorant_v2_006

- คำถาม: VALORANT อาหารเครื่องดื่มที่อนุญาตมีอะไร
- Intent ที่คาด: `area_rules`
- Route/Mode: `rules` / `pipeline:rules_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น
- Keyword ที่ขาดใน first line: `น้ำดื่ม, ปิดสนิท, หมากฝรั่ง`
- Keyword ที่ขาดในคำตอบรวม: `น้ำดื่ม, ปิดสนิท, หมากฝรั่ง`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `rules` จึงตอบ `อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น` ซึ่งไม่ใช่คำตอบของคำถาม `VALORANT อาหารเครื่องดื่มที่อนุญาตมีอะไร`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น น้ำดื่ม, ปิดสนิท, หมากฝรั่ง

### 103. [FAIL] competition_valorant_v2_007

- คำถาม: VALORANT ต้องมารายงานตัวก่อนแข่งกี่นาที
- Intent ที่คาด: `checkin`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
- Keyword ที่ขาดใน first line: `30 นาที`
- Keyword ที่ขาดในคำตอบรวม: `30 นาที`
- Retrieved: `valorant_agent_map_restriction`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `valorant_agent_map_restriction` ทำให้คำตอบแรกเป็น `VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง` แต่คำถามต้องการ intent `checkin` และยังขาด `30 นาที`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยวัน เวลา หรือสถานที่ที่ถามก่อน เช่น 30 นาที

### 104. [PASS] competition_valorant_v2_008

- คำถาม: วาโล agent ใหม่ใช้ได้ทันทีไหม
- Intent ที่คาด: `character`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `valorant_agent_map_restriction`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น Agent, 2 สัปดาห์

### 105. [PASS] competition_valorant_v2_009

- คำถาม: VALORANT แผนที่ใหม่ต้องรอกี่สัปดาห์ก่อนใช้แข่ง
- Intent ที่คาด: `map_pool`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `valorant_agent_map_restriction`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: 4 สัปดาห์

### 106. [FAIL] competition_valorant_v2_010

- คำถาม: VALORANT ต้องปิด setting อะไรก่อนแข่ง
- Intent ที่คาด: `game_setting`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
- Keyword ที่ขาดใน first line: `เลือด, ศพ, OFF`
- Keyword ที่ขาดในคำตอบรวม: `เลือด, ศพ, OFF`
- Retrieved: `valorant_agent_map_restriction`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `valorant_agent_map_restriction` ทำให้คำตอบแรกเป็น `VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง` แต่คำถามต้องการ intent `game_setting` และยังขาด `เลือด, ศพ, OFF`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น เลือด, ศพ, OFF

### 107. [FAIL] competition_valorant_v2_011

- คำถาม: VALORANT เปิดกราฟ FPS หรือ latency ระหว่างแข่งได้ไหม
- Intent ที่คาด: `game_setting`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
- Keyword ที่ขาดใน first line: `ห้าม, FPS, Latency`
- Keyword ที่ขาดในคำตอบรวม: `ห้าม, FPS, Latency`
- Retrieved: `valorant_agent_map_restriction`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `valorant_agent_map_restriction` ทำให้คำตอบแรกเป็น `VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง` แต่คำถามต้องการ intent `game_setting` และยังขาด `ห้าม, FPS, Latency`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น ห้าม, FPS, Latency

### 108. [FAIL] competition_valorant_v2_012

- คำถาม: VALORANT map pool มีทั้งหมดกี่ map และชื่ออะไรบ้าง
- Intent ที่คาด: `map_pool`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
- Keyword ที่ขาดใน first line: `7`
- Keyword ที่ขาดในคำตอบรวม: `7`
- Retrieved: `valorant_map_pool`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `7` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: 7, Abyss, Sunset

### 109. [PASS] competition_valorant_v2_013

- คำถาม: วาโลมี Haven Lotus Sunset ใน map pool ไหม
- Intent ที่คาด: `map_pool`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `valorant_map_pool`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: Haven, Lotus, Sunset

### 110. [FAIL] competition_valorant_v2_014

- คำถาม: VALORANT ban map จนเหลือกี่แผนที่
- Intent ที่คาด: `map_pool`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
- Keyword ที่ขาดใน first line: `3 แผนที่`
- Keyword ที่ขาดในคำตอบรวม: `3 แผนที่`
- Retrieved: `valorant_map_pool`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `3 แผนที่` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: 3 แผนที่

### 111. [FAIL] competition_valorant_v2_015

- คำถาม: VALORANT เลือกฝั่งด้วยวิธีอะไร
- Intent ที่คาด: `side_selection`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
- Keyword ที่ขาดใน first line: `โยนเหรียญ`
- Keyword ที่ขาดในคำตอบรวม: `โยนเหรียญ`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends` ซึ่งไม่ใช่คำตอบของคำถาม `VALORANT เลือกฝั่งด้วยวิธีอะไร`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: โยนเหรียญ

### 112. [FAIL] competition_valorant_v2_016

- คำถาม: หลังจบแมตช์ VALORANT ใครยืนยันและบันทึกผล
- Intent ที่คาด: `post_match`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
- Keyword ที่ขาดใน first line: `เจ้าหน้าที่, บันทึกผล`
- Keyword ที่ขาดในคำตอบรวม: `เจ้าหน้าที่, บันทึกผล`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends` ซึ่งไม่ใช่คำตอบของคำถาม `หลังจบแมตช์ VALORANT ใครยืนยันและบันทึกผล`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: เจ้าหน้าที่, บันทึกผล

### 113. [FAIL] competition_valorant_v2_017

- คำถาม: VALORANT ถ้า forfeit แผนที่นั้นบันทึกผลเป็นเท่าไหร่
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
- Keyword ที่ขาดใน first line: `13-0`
- Keyword ที่ขาดในคำตอบรวม: `13-0`
- Retrieved: `valorant_map_pool`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `valorant_map_pool` ทำให้คำตอบแรกเป็น `VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset` แต่คำถามต้องการ intent `penalty` และยังขาด `13-0`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น 13-0

### 114. [FAIL] competition_valorant_v2_018

- คำถาม: VALORANT pause มีกี่ประเภทหลัก
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Keyword ที่ขาดใน first line: `3, Tactical`
- Keyword ที่ขาดในคำตอบรวม: `3, Tactical`
- Retrieved: `valorant_emergency_pause`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `3, Tactical` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น 3, Tactical, Technical, Emergency

### 115. [PASS] competition_valorant_v2_019

- คำถาม: VALORANT tactical timeout ได้กี่ครั้งต่อแผนที่
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `valorant_tactical_timeout`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น 2, ต่อแผนที่

### 116. [PASS] competition_valorant_v2_020

- คำถาม: วาโล tactical timeout ครั้งละกี่วินาที
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `valorant_tactical_timeout`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น 60 วินาที

### 117. [PASS] competition_valorant_v2_021

- คำถาม: VALORANT overtime ได้ timeout เพิ่มไหม
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `valorant_tactical_timeout`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น Overtime, เพิ่ม, 1 ครั้ง

### 118. [FAIL] competition_valorant_v2_022

- คำถาม: VALORANT Technical Pause ใช้กรณีไหน
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Keyword ที่ขาดใน first line: `อุปกรณ์ขัดข้อง, หลุด, ซอฟต์แวร์`
- Keyword ที่ขาดในคำตอบรวม: `อุปกรณ์ขัดข้อง, หลุด, ซอฟต์แวร์`
- Retrieved: `valorant_emergency_pause`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `อุปกรณ์ขัดข้อง, หลุด, ซอฟต์แวร์` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น อุปกรณ์ขัดข้อง, หลุด, ซอฟต์แวร์

### 119. [FAIL] competition_valorant_v2_023

- คำถาม: ตอน Technical Pause วาโลคุยกันได้ไหม
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Keyword ที่ขาดใน first line: `ห้าม, สื่อสาร, เว้นแต่`
- Keyword ที่ขาดในคำตอบรวม: `ห้าม, สื่อสาร, เว้นแต่`
- Retrieved: `valorant_emergency_pause`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `ห้าม, สื่อสาร, เว้นแต่` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น ห้าม, สื่อสาร, เว้นแต่

### 120. [PASS] competition_valorant_v2_024

- คำถาม: VALORANT Emergency Pause ขอได้กี่ครั้ง
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `valorant_emergency_pause`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น 1 ครั้ง, ต่อแผนที่

### 121. [PASS] competition_valorant_v2_025

- คำถาม: VALORANT Emergency Pause รวมเวลาได้ไม่เกินกี่นาที
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `valorant_emergency_pause`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น 10 นาที

### 122. [FAIL] competition_valorant_v2_026

- คำถาม: VALORANT ถ้า emergency pause เกินเวลาผู้เล่นอาจเป็นอะไร
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Keyword ที่ขาดใน first line: `หมดสิทธิ์, ตัวสำรอง`
- Keyword ที่ขาดในคำตอบรวม: `หมดสิทธิ์, ตัวสำรอง`
- Retrieved: `valorant_emergency_pause`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `หมดสิทธิ์, ตัวสำรอง` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น หมดสิทธิ์, ตัวสำรอง

### 123. [FAIL] competition_valorant_v2_027

- คำถาม: VALORANT Play Through Bug คืออะไร
- Intent ที่คาด: `bug_rule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Keyword ที่ขาดใน first line: `ไม่ส่งผลกระทบ, เล่นต่อ`
- Keyword ที่ขาดในคำตอบรวม: `ไม่ส่งผลกระทบ, เล่นต่อ`
- Retrieved: `valorant_emergency_pause`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `valorant_emergency_pause` ทำให้คำตอบแรกเป็น `VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที` แต่คำถามต้องการ intent `bug_rule` และยังขาด `ไม่ส่งผลกระทบ, เล่นต่อ`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น ไม่ส่งผลกระทบ, เล่นต่อ

### 124. [FAIL] competition_valorant_v2_028

- คำถาม: VALORANT Major Bug ขอ Challenge ได้ไหม
- Intent ที่คาด: `bug_rule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Keyword ที่ขาดใน first line: `Major Bug, Challenge`
- Keyword ที่ขาดในคำตอบรวม: `Major Bug, Challenge`
- Retrieved: `valorant_emergency_pause`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `valorant_emergency_pause` ทำให้คำตอบแรกเป็น `VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที` แต่คำถามต้องการ intent `bug_rule` และยังขาด `Major Bug, Challenge`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น Major Bug, Challenge

### 125. [FAIL] competition_valorant_v2_029

- คำถาม: VALORANT Game Breaking Bug จัดการยังไง
- Intent ที่คาด: `bug_rule`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Keyword ที่ขาดใน first line: `Game-Breaking, ย้อนรอบ`
- Keyword ที่ขาดในคำตอบรวม: `Game-Breaking, ย้อนรอบ`
- Retrieved: `valorant_emergency_pause`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `valorant_emergency_pause` ทำให้คำตอบแรกเป็น `VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที` แต่คำถามต้องการ intent `bug_rule` และยังขาด `Game-Breaking, ย้อนรอบ`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น Game-Breaking, ย้อนรอบ

### 126. [FAIL] competition_valorant_v2_030

- คำถาม: VALORANT ถ้าบั๊กเกิดก่อนมี damage ทำอะไรได้
- Intent ที่คาด: `bug_rule`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
- Keyword ที่ขาดใน first line: `ก่อน, ดาเมจ, ย้อนรอบ`
- Keyword ที่ขาดในคำตอบรวม: `ก่อน, ดาเมจ, ย้อนรอบ`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends` ซึ่งไม่ใช่คำตอบของคำถาม `VALORANT ถ้าบั๊กเกิดก่อนมี damage ทำอะไรได้`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น ก่อน, ดาเมจ, ย้อนรอบ

### 127. [FAIL] competition_valorant_v2_031

- คำถาม: VALORANT ถ้าทำ damage ไปแล้ว rollback ได้ไหม
- Intent ที่คาด: `bug_rule`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
- Keyword ที่ขาดใน first line: `damage, ไม่, Challenge`
- Keyword ที่ขาดในคำตอบรวม: `damage, ไม่, Challenge`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends` ซึ่งไม่ใช่คำตอบของคำถาม `VALORANT ถ้าทำ damage ไปแล้ว rollback ได้ไหม`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น damage, ไม่, Challenge

### 128. [FAIL] competition_valorant_v2_032

- คำถาม: VALORANT ใช้บั๊กเพื่อได้เปรียบถือว่าผิดไหม
- Intent ที่คาด: `penalty`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
- Keyword ที่ขาดใน first line: `ผิด, ได้เปรียบ`
- Keyword ที่ขาดในคำตอบรวม: `ผิด, ได้เปรียบ`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends` ซึ่งไม่ใช่คำตอบของคำถาม `VALORANT ใช้บั๊กเพื่อได้เปรียบถือว่าผิดไหม`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น ผิด, ได้เปรียบ

### 129. [FAIL] competition_valorant_v2_033

- คำถาม: VALORANT วางกล้อง Cypher จุดมองไม่เห็นได้ไหม
- Intent ที่คาด: `character`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
- Keyword ที่ขาดใน first line: `ห้าม, Cypher`
- Keyword ที่ขาดในคำตอบรวม: `ห้าม, Cypher`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends` ซึ่งไม่ใช่คำตอบของคำถาม `VALORANT วางกล้อง Cypher จุดมองไม่เห็นได้ไหม`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น ห้าม, Cypher

### 130. [FAIL] competition_valorant_v2_034

- คำถาม: VALORANT ใช้สกิลนอกขอบแผนที่เพื่อหาข้อมูลได้ไหม
- Intent ที่คาด: `character`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
- Keyword ที่ขาดใน first line: `ห้าม, นอกขอบเขต`
- Keyword ที่ขาดในคำตอบรวม: `ห้าม, นอกขอบเขต`
- Retrieved: `valorant_map_pool`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `valorant_map_pool` ทำให้คำตอบแรกเป็น `VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset` แต่คำถามต้องการ intent `character` และยังขาด `ห้าม, นอกขอบเขต`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น ห้าม, นอกขอบเขต

### 131. [FAIL] competition_valorant_v2_035

- คำถาม: VALORANT ข้อยกเว้น KAY/O ZERO/POINT คืออะไร
- Intent ที่คาด: `character`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
- Keyword ที่ขาดใน first line: `KAY/O, ZERO/POINT, Texture`
- Keyword ที่ขาดในคำตอบรวม: `KAY/O, ZERO/POINT, Texture`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends` ซึ่งไม่ใช่คำตอบของคำถาม `VALORANT ข้อยกเว้น KAY/O ZERO/POINT คืออะไร`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น KAY/O, ZERO/POINT, Texture

### 132. [FAIL] competition_valorant_v2_036

- คำถาม: VALORANT ใช้เพื่อนกระโดดต่อตัวขึ้นจุดสูงได้ไหม
- Intent ที่คาด: `character`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
- Keyword ที่ขาดใน first line: `ห้าม, กระโดด`
- Keyword ที่ขาดในคำตอบรวม: `ห้าม, กระโดด`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends` ซึ่งไม่ใช่คำตอบของคำถาม `VALORANT ใช้เพื่อนกระโดดต่อตัวขึ้นจุดสูงได้ไหม`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น ห้าม, กระโดด

### 133. [FAIL] competition_valorant_v2_037

- คำถาม: VALORANT ความผิดครั้งแรกผลกระทบต่ำโดนอะไร
- Intent ที่คาด: `penalty`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
- Keyword ที่ขาดใน first line: `Warning, ตักเตือน`
- Keyword ที่ขาดในคำตอบรวม: `Warning, ตักเตือน`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends` ซึ่งไม่ใช่คำตอบของคำถาม `VALORANT ความผิดครั้งแรกผลกระทบต่ำโดนอะไร`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น Warning, ตักเตือน

### 134. [FAIL] competition_valorant_v2_038

- คำถาม: VALORANT Round Rollback ใช้เมื่อไหร่
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง
- Keyword ที่ขาดใน first line: `Round Rollback, ช่องโหว่`
- Keyword ที่ขาดในคำตอบรวม: `Round Rollback, ช่องโหว่`
- Retrieved: `valorant_tactical_timeout`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `valorant_tactical_timeout` ทำให้คำตอบแรกเป็น `VALORANT ขอ Tactical Timeout ได้ทีมละ 2 ครั้งต่อแผนที่ ครั้งละ 60 วินาที และถ้าเข้า Overtime จะได้เพิ่มอีก 1 ครั้ง` แต่คำถามต้องการ intent `penalty` และยังขาด `Round Rollback, ช่องโหว่`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น Round Rollback, ช่องโหว่

### 135. [FAIL] competition_valorant_v2_039

- คำถาม: VALORANT Round Loss เกิดจากอะไร
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Keyword ที่ขาดใน first line: `Round Loss, เจตนา, ช่องโหว่`
- Keyword ที่ขาดในคำตอบรวม: `Round Loss, เจตนา, ช่องโหว่`
- Retrieved: `valorant_emergency_pause`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `valorant_emergency_pause` ทำให้คำตอบแรกเป็น `VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที` แต่คำถามต้องการ intent `penalty` และยังขาด `Round Loss, เจตนา, ช่องโหว่`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น Round Loss, เจตนา, ช่องโหว่

### 136. [FAIL] competition_valorant_v2_040

- คำถาม: VALORANT Map Forfeit ใช้กรณีไหน
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
- Keyword ที่ขาดใน first line: `Map Forfeit, ร้ายแรง, ซ้ำ`
- Keyword ที่ขาดในคำตอบรวม: `Map Forfeit, ร้ายแรง, ซ้ำ`
- Retrieved: `valorant_map_pool`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `Map Forfeit, ร้ายแรง, ซ้ำ` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น Map Forfeit, ร้ายแรง, ซ้ำ

### 137. [FAIL] competition_valorant_v2_041

- คำถาม: VALORANT Match Forfeit ใช้กับความผิดแบบไหน
- Intent ที่คาด: `penalty`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
- Keyword ที่ขาดใน first line: `Match Forfeit, Cheating, Match fixing`
- Keyword ที่ขาดในคำตอบรวม: `Match Forfeit, Cheating, Match fixing`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends` ซึ่งไม่ใช่คำตอบของคำถาม `VALORANT Match Forfeit ใช้กับความผิดแบบไหน`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น Match Forfeit, Cheating, Match fixing

### 138. [FAIL] competition_valorant_v2_042

- คำถาม: VALORANT ใช้ keyboard Snap Tap หรือ SOCD ได้ไหม
- Intent ที่คาด: `equipment`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Keyword ที่ขาดใน first line: `Snap Tap, SOCD, permitted`
- Keyword ที่ขาดในคำตอบรวม: `Snap Tap, SOCD, permitted`
- Retrieved: `valorant_emergency_pause`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `valorant_emergency_pause` ทำให้คำตอบแรกเป็น `VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที` แต่คำถามต้องการ intent `equipment` และยังขาด `Snap Tap, SOCD, permitted`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น Snap Tap, SOCD, permitted

### 139. [FAIL] competition_valorant_v2_043

- คำถาม: VALORANT ใช้ macro ได้ไหม
- Intent ที่คาด: `equipment`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
- Keyword ที่ขาดใน first line: `ห้าม, Macros`
- Keyword ที่ขาดในคำตอบรวม: `ห้าม, Macros`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PC มีเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends` ซึ่งไม่ใช่คำตอบของคำถาม `VALORANT ใช้ macro ได้ไหม`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น ห้าม, Macros

### 140. [FAIL] competition_valorant_v2_044

- คำถาม: VALORANT ติดตั้งโปรแกรมเองบนคอมแข่งได้ไหม
- Intent ที่คาด: `equipment`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง
- Keyword ที่ขาดใน first line: `ห้าม, ติดตั้งโปรแกรม`
- Keyword ที่ขาดในคำตอบรวม: `ห้าม, ติดตั้งโปรแกรม`
- Retrieved: `valorant_agent_map_restriction`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `valorant_agent_map_restriction` ทำให้คำตอบแรกเป็น `VALORANT จำกัดคอนเทนต์ใหม่: Agent ใหม่ต้องรอประมาณ 2 สัปดาห์ และแผนที่ใหม่ต้องรอประมาณ 4 สัปดาห์ก่อนใช้แข่ง` แต่คำถามต้องการ intent `equipment` และยังขาด `ห้าม, ติดตั้งโปรแกรม`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น ห้าม, ติดตั้งโปรแกรม

### 141. [FAIL] competition_valorant_v2_045

- คำถาม: VALORANT เข้าเว็บสื่อสารหรือโซเชียลบนคอมแข่งได้ไหม
- Intent ที่คาด: `equipment`
- Route/Mode: `competition_rules` / `pipeline:no_answer`
- Cause: `no_answer_despite_data`
- Style: `no_answer` - รูปแบบสุภาพ แต่ไม่ควรตอบไม่พบข้อมูลถ้าข้อมูลมีอยู่ใน competition chunks
- First line ที่ AI ตอบ: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด competition_rules ตอนนี้ครับ
- Keyword ที่ขาดใน first line: `ห้าม, social media`
- Keyword ที่ขาดในคำตอบรวม: `ห้าม, social media`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: ระบบตอบไม่พบข้อมูล ทั้งที่ Ground Truth สร้างจากข้อมูลใน competition chunks จึงควร fallback ไปค้น chunk/LLM ต่อ
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น ห้าม, social media

### 142. [FAIL] competition_valorant_v2_046

- คำถาม: VALORANT สรุป pause แต่ละประเภทแบบสั้นๆ
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที
- Keyword ที่ขาดใน first line: `Tactical`
- Keyword ที่ขาดในคำตอบรวม: `Tactical`
- Retrieved: `valorant_emergency_pause`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `VALORANT Emergency/Technical Pause ขอได้ทีมละ 1 ครั้งต่อแผนที่ และเวลาหยุดรวมสูงสุด 10 นาที` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `Tactical` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น Tactical, Technical, Emergency

### 143. [FAIL] competition_valorant_v2_047

- คำถาม: VALORANT สรุปกฎเนื้อหาใหม่กับ map pool
- Intent ที่คาด: `summary`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
- Keyword ที่ขาดใน first line: `Agent, 2 สัปดาห์, แผนที่ใหม่, 4 สัปดาห์`
- Keyword ที่ขาดในคำตอบรวม: `Agent, 2 สัปดาห์, แผนที่ใหม่, 4 สัปดาห์`
- Retrieved: `valorant_map_pool`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `Agent, 2 สัปดาห์, แผนที่ใหม่, 4 สัปดาห์` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: Agent, 2 สัปดาห์, แผนที่ใหม่, 4 สัปดาห์, Abyss

### 144. [FAIL] competition_valorant_v2_048

- คำถาม: VALORANT สรุปบทลงโทษในเกมว่ามีอะไรบ้าง
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset
- Keyword ที่ขาดใน first line: `Warning, Round Rollback, Round Loss, Map Forfeit, Match Forfeit`
- Keyword ที่ขาดในคำตอบรวม: `Warning, Round Rollback, Round Loss, Map Forfeit, Match Forfeit`
- Retrieved: `valorant_map_pool`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `valorant_map_pool` ทำให้คำตอบแรกเป็น `VALORANT ใช้แผนที่ Abyss, Ascent, Bind, Corrode, Haven, Lotus และ Sunset` แต่คำถามต้องการ intent `penalty` และยังขาด `Warning, Round Rollback, Round Loss, Map Forfeit, Match Forfeit`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น Warning, Round Rollback, Round Loss, Map Forfeit, Match Forfeit

## Tekken 8

### 145. [PASS] competition_tekken8_v2_001

- คำถาม: Tekken 8 แข่งออนไลน์หรือออฟไลน์
- Intent ที่คาด: `format`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `tekken8_format_ps5_1v1`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น ออฟไลน์

### 146. [PASS] competition_tekken8_v2_002

- คำถาม: Tekken 8 ใช้เครื่องอะไรแข่ง
- Intent ที่คาด: `equipment`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `tekken8_equipment_ps5`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น PlayStation 5

### 147. [PASS] competition_tekken8_v2_003

- คำถาม: Tekken 8 แข่งแบบกี่ต่อกี่
- Intent ที่คาด: `format`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `tekken8_format_ps5_1v1`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น 1v1

### 148. [FAIL] competition_tekken8_v2_004

- คำถาม: Tekken 8 FT2 คือชนะกี่เกมก่อน
- Intent ที่คาด: `format`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
- Keyword ที่ขาดใน first line: `ชนะครบ 2 เกม`
- Keyword ที่ขาดในคำตอบรวม: `ชนะครบ 2 เกม`
- Retrieved: `tekken8_format_ps5_1v1`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `ชนะครบ 2 เกม` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น ชนะครบ 2 เกม

### 149. [FAIL] competition_tekken8_v2_005

- คำถาม: Tekken 8 ถ้าเสมอกัน 1-1 ต้องทำอะไร
- Intent ที่คาด: `format`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
- Keyword ที่ขาดใน first line: `เกมตัดสิน`
- Keyword ที่ขาดในคำตอบรวม: `เกมตัดสิน`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5` ซึ่งไม่ใช่คำตอบของคำถาม `Tekken 8 ถ้าเสมอกัน 1-1 ต้องทำอะไร`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น เกมตัดสิน

### 150. [FAIL] competition_tekken8_v2_006

- คำถาม: Tekken 8 ในแต่ละเกมแข่งกี่รอบ
- Intent ที่คาด: `game_setting`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
- Keyword ที่ขาดใน first line: `3 รอบ`
- Keyword ที่ขาดในคำตอบรวม: `3 รอบ`
- Retrieved: `tekken8_format_ps5_1v1`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `tekken8_format_ps5_1v1` ทำให้คำตอบแรกเป็น `Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที` แต่คำถามต้องการ intent `game_setting` และยังขาด `3 รอบ`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น 3 รอบ

### 151. [PASS] competition_tekken8_v2_007

- คำถาม: Tekken 8 จำกัดเวลาต่อรอบกี่วินาที
- Intent ที่คาด: `game_setting`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `tekken8_format_ps5_1v1`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น 60 วินาที

### 152. [FAIL] competition_tekken8_v2_008

- คำถาม: Tekken 8 ตั้งค่า Advantage เป็นอะไร
- Intent ที่คาด: `game_setting`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
- Keyword ที่ขาดใน first line: `No advantage`
- Keyword ที่ขาดในคำตอบรวม: `No advantage`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5` ซึ่งไม่ใช่คำตอบของคำถาม `Tekken 8 ตั้งค่า Advantage เป็นอะไร`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น No advantage

### 153. [FAIL] competition_tekken8_v2_009

- คำถาม: Tekken 8 เลือก Stage อย่างไร
- Intent ที่คาด: `game_setting`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
- Keyword ที่ขาดใน first line: `Random`
- Keyword ที่ขาดในคำตอบรวม: `Random`
- Retrieved: `tekken8_character_dlc_rule`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `tekken8_character_dlc_rule` ทำให้คำตอบแรกเป็น `Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน` แต่คำถามต้องการ intent `game_setting` และยังขาด `Random`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น Random

### 154. [PASS] competition_tekken8_v2_010

- คำถาม: Tekken 8 เลือกตัวละคร DLC ได้ไหม
- Intent ที่คาด: `character`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `tekken8_character_dlc_rule`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น ยกเว้น, DLC

### 155. [PASS] competition_tekken8_v2_011

- คำถาม: Tekken 8 ใช้ตัวละครตัวไหนก็ได้ไหม
- Intent ที่คาด: `character`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `tekken8_character_dlc_rule`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น ทุกตัว, ยกเว้น, DLC

### 156. [FAIL] competition_tekken8_v2_012

- คำถาม: Tekken 8 ปรับแต่งชุดหรือทรงผมตัวละครได้ไหม
- Intent ที่คาด: `character`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
- Keyword ที่ขาดใน first line: `ปรับแต่ง`
- Keyword ที่ขาดในคำตอบรวม: `ปรับแต่ง`
- Retrieved: `tekken8_character_dlc_rule`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `ปรับแต่ง` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น ห้าม, ปรับแต่ง

### 157. [FAIL] competition_tekken8_v2_013

- คำถาม: Tekken 8 ต้องใช้สกินแบบไหน
- Intent ที่คาด: `skin`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
- Keyword ที่ขาดใน first line: `สกินมาตรฐาน`
- Keyword ที่ขาดในคำตอบรวม: `สกินมาตรฐาน`
- Retrieved: `tekken8_format_ps5_1v1`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `tekken8_format_ps5_1v1` ทำให้คำตอบแรกเป็น `Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที` แต่คำถามต้องการ intent `skin` และยังขาด `สกินมาตรฐาน`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น สกินมาตรฐาน

### 158. [FAIL] competition_tekken8_v2_014

- คำถาม: Tekken 8 ใช้ปุ่ม Assist ได้ไหม
- Intent ที่คาด: `game_setting`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
- Keyword ที่ขาดใน first line: `อนุญาต, Assist`
- Keyword ที่ขาดในคำตอบรวม: `อนุญาต, Assist`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5` ซึ่งไม่ใช่คำตอบของคำถาม `Tekken 8 ใช้ปุ่ม Assist ได้ไหม`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น อนุญาต, Assist

### 159. [FAIL] competition_tekken8_v2_015

- คำถาม: Tekken 8 ใช้ bug หรือ glitch ได้ไหม
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
- Keyword ที่ขาดใน first line: `Bug, Glitch`
- Keyword ที่ขาดในคำตอบรวม: `Bug, Glitch`
- Retrieved: `tekken8_character_dlc_rule`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `tekken8_character_dlc_rule` ทำให้คำตอบแรกเป็น `Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน` แต่คำถามต้องการ intent `penalty` และยังขาด `Bug, Glitch`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น ห้าม, Bug, Glitch

### 160. [PASS] competition_tekken8_v2_016

- คำถาม: Tekken 8 เมื่อเริ่มเกมแล้ว pause ได้ไหม
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `details_have_answer_but_first_line_missing` - ข้อมูลที่ต้องการอาจอยู่ในรายละเอียด/หลักฐาน แต่บรรทัดแรกยังไม่ตอบสิ่งที่ถามโดยตรง
- First line ที่ AI ตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
- Keyword ที่ขาดใน first line: `ห้าม`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `tekken8_pause_penalty`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น ห้าม, หยุดเกม

### 161. [FAIL] competition_tekken8_v2_017

- คำถาม: Tekken 8 ตั้งใจกด pause โดนอะไร
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
- Keyword ที่ขาดใน first line: `ปรับแพ้ 1 รอบ`
- Keyword ที่ขาดในคำตอบรวม: `ปรับแพ้ 1 รอบ`
- Retrieved: `tekken8_pause_penalty`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `ปรับแพ้ 1 รอบ` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น ปรับแพ้ 1 รอบ

### 162. [FAIL] competition_tekken8_v2_018

- คำถาม: Tekken 8 กดหยุดเกมได้ในกรณีไหน
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
- Keyword ที่ขาดใน first line: `อุปกรณ์ขัดข้อง, เหตุฉุกเฉิน`
- Keyword ที่ขาดในคำตอบรวม: `อุปกรณ์ขัดข้อง, เหตุฉุกเฉิน`
- Retrieved: `tekken8_pause_penalty`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `อุปกรณ์ขัดข้อง, เหตุฉุกเฉิน` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น ยินยอม, อุปกรณ์ขัดข้อง, เหตุฉุกเฉิน

### 163. [FAIL] competition_tekken8_v2_019

- คำถาม: Tekken 8 ถ้าออกจากเกมก่อนจบโดยไม่ได้รับอนุญาตโดนอะไร
- Intent ที่คาด: `penalty`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
- Keyword ที่ขาดใน first line: `ปรับแพ้ทันที`
- Keyword ที่ขาดในคำตอบรวม: `ปรับแพ้ทันที`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5` ซึ่งไม่ใช่คำตอบของคำถาม `Tekken 8 ถ้าออกจากเกมก่อนจบโดยไม่ได้รับอนุญาตโดนอะไร`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น ปรับแพ้ทันที

### 164. [FAIL] competition_tekken8_v2_020

- คำถาม: Tekken 8 หยุดเกมโดยไม่จำเป็นลงโทษเหมือนอะไร
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
- Keyword ที่ขาดใน first line: `ออกจากเกมก่อนจบ`
- Keyword ที่ขาดในคำตอบรวม: `ออกจากเกมก่อนจบ`
- Retrieved: `tekken8_pause_penalty`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `ออกจากเกมก่อนจบ` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น ออกจากเกมก่อนจบ

### 165. [FAIL] competition_tekken8_v2_021

- คำถาม: Tekken 8 เยาะเย้ยหรือไม่สุภาพต่อคู่แข่งโดนอะไร
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
- Keyword ที่ขาดใน first line: `ปรับแพ้ทันที`
- Keyword ที่ขาดในคำตอบรวม: `ปรับแพ้ทันที`
- Retrieved: `tekken8_pause_penalty`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `ปรับแพ้ทันที` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น ปรับแพ้ทันที

### 166. [FAIL] competition_tekken8_v2_022

- คำถาม: Tekken 8 ดูถูกผู้ตัดสินหรือผู้เข้าแข่งคนอื่นได้ไหม
- Intent ที่คาด: `penalty`
- Route/Mode: `competition_rules` / `pipeline:no_answer`
- Cause: `no_answer_despite_data`
- Style: `no_answer` - รูปแบบสุภาพ แต่ไม่ควรตอบไม่พบข้อมูลถ้าข้อมูลมีอยู่ใน competition chunks
- First line ที่ AI ตอบ: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด competition_rules ตอนนี้ครับ
- Keyword ที่ขาดใน first line: `ห้าม, ปรับแพ้ทันที`
- Keyword ที่ขาดในคำตอบรวม: `ห้าม, ปรับแพ้ทันที`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: ระบบตอบไม่พบข้อมูล ทั้งที่ Ground Truth สร้างจากข้อมูลใน competition chunks จึงควร fallback ไปค้น chunk/LLM ต่อ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น ห้าม, ปรับแพ้ทันที

### 167. [FAIL] competition_tekken8_v2_023

- คำถาม: Tekken 8 ผู้เข้าแข่งขันต้องยอมรับอะไรเกี่ยวกับคำตัดสิน
- Intent ที่คาด: `policy`
- Route/Mode: `competition_rules` / `pipeline:no_answer`
- Cause: `no_answer_despite_data`
- Style: `no_answer` - รูปแบบสุภาพ แต่ไม่ควรตอบไม่พบข้อมูลถ้าข้อมูลมีอยู่ใน competition chunks
- First line ที่ AI ตอบ: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด competition_rules ตอนนี้ครับ
- Keyword ที่ขาดใน first line: `คำตัดสิน, กรรมการ`
- Keyword ที่ขาดในคำตอบรวม: `คำตัดสิน, กรรมการ`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: ระบบตอบไม่พบข้อมูล ทั้งที่ Ground Truth สร้างจากข้อมูลใน competition chunks จึงควร fallback ไปค้น chunk/LLM ต่อ
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น คำตัดสิน, กรรมการ

### 168. [FAIL] competition_tekken8_v2_024

- คำถาม: ผู้จัด Tekken 8 เปลี่ยนกฎได้ไหม
- Intent ที่คาด: `policy`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
- Keyword ที่ขาดใน first line: `ปรับเปลี่ยนกฎ, ไม่ต้องแจ้ง`
- Keyword ที่ขาดในคำตอบรวม: `ปรับเปลี่ยนกฎ, ไม่ต้องแจ้ง`
- Retrieved: `tekken8_pause_penalty`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `tekken8_pause_penalty` ทำให้คำตอบแรกเป็น `Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร` แต่คำถามต้องการ intent `policy` และยังขาด `ปรับเปลี่ยนกฎ, ไม่ต้องแจ้ง`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น ปรับเปลี่ยนกฎ, ไม่ต้องแจ้ง

### 169. [FAIL] competition_tekken8_v2_025

- คำถาม: Tekken 8 คำตัดสินของกรรมการถือว่าอย่างไร
- Intent ที่คาด: `policy`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
- Keyword ที่ขาดใน first line: `ถือเป็นที่สิ้นสุด`
- Keyword ที่ขาดในคำตอบรวม: `ถือเป็นที่สิ้นสุด`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5` ซึ่งไม่ใช่คำตอบของคำถาม `Tekken 8 คำตัดสินของกรรมการถือว่าอย่างไร`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น ถือเป็นที่สิ้นสุด

### 170. [FAIL] competition_tekken8_v2_026

- คำถาม: Tekken 8 ถ้าเกิดข้อโต้แย้งต้องฟังคำตัดสินใคร
- Intent ที่คาด: `dispute`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
- Keyword ที่ขาดใน first line: `ผู้ดูแล, กรรมการ`
- Keyword ที่ขาดในคำตอบรวม: `ผู้ดูแล, กรรมการ`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5` ซึ่งไม่ใช่คำตอบของคำถาม `Tekken 8 ถ้าเกิดข้อโต้แย้งต้องฟังคำตัดสินใคร`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: ผู้ดูแล, กรรมการ

### 171. [FAIL] competition_tekken8_v2_027

- คำถาม: Tekken 8 หากเกิดปัญหาใดๆ ต้องแจ้งใคร
- Intent ที่คาด: `dispute`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
- Keyword ที่ขาดใน first line: `ผู้จัดการแข่งขัน, ทันที`
- Keyword ที่ขาดในคำตอบรวม: `ผู้จัดการแข่งขัน, ทันที`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5` ซึ่งไม่ใช่คำตอบของคำถาม `Tekken 8 หากเกิดปัญหาใดๆ ต้องแจ้งใคร`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: ผู้จัดการแข่งขัน, ทันที

### 172. [PASS] competition_tekken8_v2_028

- คำถาม: Tekken 8 สรุปรูปแบบการแข่งขันแบบสั้นๆ
- Intent ที่คาด: `summary`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `tekken8_format_ps5_1v1`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: ออฟไลน์, PlayStation 5, 1v1, FT2

### 173. [FAIL] competition_tekken8_v2_029

- คำถาม: Tekken 8 สรุปกฎตัวละครและสกิน
- Intent ที่คาด: `summary`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
- Keyword ที่ขาดใน first line: `ปรับแต่ง`
- Keyword ที่ขาดในคำตอบรวม: `ปรับแต่ง`
- Retrieved: `tekken8_character_dlc_rule`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `ปรับแต่ง` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: DLC, ปรับแต่ง, สกินมาตรฐาน

### 174. [PASS] competition_tekken8_v2_030

- คำถาม: Tekken 8 สรุปกฎ pause แบบเข้าใจง่าย
- Intent ที่คาด: `summary`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `pass`
- Style: `good_direct_first` - ตอบสิ่งที่ถามในบรรทัดแรกแล้วค่อยตามด้วยหลักฐาน/อ้างอิง
- First line ที่ AI ตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
- Keyword ที่ขาดใน first line: `-`
- Keyword ที่ขาดในคำตอบรวม: `-`
- Retrieved: `tekken8_pause_penalty`
- ทำไมผิด/ปัญหาคืออะไร: ไม่ผิดตามเกณฑ์อัตโนมัติ
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยคำตอบตรงประเด็นที่มี keyword หลัก: Pause, ยินยอม, ปรับแพ้

### 175. [FAIL] competition_tekken8_v2_031

- คำถาม: Tekken 8 รอบละ 60 วิและ R3 หมายถึงอะไร
- Intent ที่คาด: `game_setting`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
- Keyword ที่ขาดใน first line: `3 รอบ, 60 วินาที`
- Keyword ที่ขาดในคำตอบรวม: `3 รอบ, 60 วินาที`
- Retrieved: `tekken8_character_dlc_rule`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `tekken8_character_dlc_rule` ทำให้คำตอบแรกเป็น `Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน` แต่คำถามต้องการ intent `game_setting` และยังขาด `3 รอบ, 60 วินาที`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น 3 รอบ, 60 วินาที

### 176. [FAIL] competition_tekken8_v2_032

- คำถาม: Tekken 8 ใช้ PS5 กับ Stage Random ใช่ไหม
- Intent ที่คาด: `game_setting`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: Tekken 8 แข่งขันบนเครื่อง PlayStation 5
- Keyword ที่ขาดใน first line: `Random`
- Keyword ที่ขาดในคำตอบรวม: `Random`
- Retrieved: `tekken8_equipment_ps5`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `tekken8_equipment_ps5` ทำให้คำตอบแรกเป็น `Tekken 8 แข่งขันบนเครื่อง PlayStation 5` แต่คำถามต้องการ intent `game_setting` และยังขาด `Random`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น PlayStation 5, Random

### 177. [FAIL] competition_tekken8_v2_033

- คำถาม: Tekken 8 ถามว่าแข่งกี่เกมควรตอบว่าอะไร
- Intent ที่คาด: `format`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
- Keyword ที่ขาดใน first line: `ชนะครบ 2 เกม`
- Keyword ที่ขาดในคำตอบรวม: `ชนะครบ 2 เกม`
- Retrieved: `tekken8_format_ps5_1v1`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `ชนะครบ 2 เกม` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น FT2, ชนะครบ 2 เกม

### 178. [FAIL] competition_tekken8_v2_034

- คำถาม: Tekken 8 ใช้ customization เอฟเฟกต์หรือออร่าได้ไหม
- Intent ที่คาด: `character`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
- Keyword ที่ขาดใน first line: `เอฟเฟกต์, ออร่า`
- Keyword ที่ขาดในคำตอบรวม: `เอฟเฟกต์, ออร่า`
- Retrieved: `tekken8_character_dlc_rule`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `เอฟเฟกต์, ออร่า` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น ห้าม, เอฟเฟกต์, ออร่า

### 179. [FAIL] competition_tekken8_v2_035

- คำถาม: Tekken 8 เหตุผลด้านอุปกรณ์ขัดข้องสามารถ pause ได้ไหม
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
- Keyword ที่ขาดใน first line: `อุปกรณ์ขัดข้อง`
- Keyword ที่ขาดในคำตอบรวม: `อุปกรณ์ขัดข้อง`
- Retrieved: `tekken8_pause_penalty`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `อุปกรณ์ขัดข้อง` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น อุปกรณ์ขัดข้อง, ยินยอม

### 180. [FAIL] competition_tekken8_v2_036

- คำถาม: Tekken 8 เหตุฉุกเฉินใช้เป็นเหตุผล pause ได้ไหม
- Intent ที่คาด: `pause`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร
- Keyword ที่ขาดใน first line: `เหตุฉุกเฉิน`
- Keyword ที่ขาดในคำตอบรวม: `เหตุฉุกเฉิน`
- Retrieved: `tekken8_pause_penalty`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `Tekken 8 ไม่อนุญาตให้ Pause หลังเริ่มเกม หากตั้งใจกดหยุดเกมจะถูกปรับแพ้ 1 Round เว้นแต่ทั้งสองฝ่ายยินยอมและมีเหตุผลสมควร` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `เหตุฉุกเฉิน` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น เหตุฉุกเฉิน

### 181. [FAIL] competition_tekken8_v2_037

- คำถาม: Tekken 8 กติกาบอกว่าผู้จัดขอสงวนสิทธิ์อะไร
- Intent ที่คาด: `policy`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `wrong_fact_card_intent`
- Style: `direct_but_wrong_fact` - มีคำตอบนำหน้าก่อนรายละเอียด แต่คำตอบแรกเป็น fact คนละเรื่องกับคำถาม
- First line ที่ AI ตอบ: Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที
- Keyword ที่ขาดใน first line: `เปลี่ยนแปลง, กฎระเบียบ`
- Keyword ที่ขาดในคำตอบรวม: `เปลี่ยนแปลง, กฎระเบียบ`
- Retrieved: `tekken8_format_ps5_1v1`
- ทำไมผิด/ปัญหาคืออะไร: ระบบเลือก `tekken8_format_ps5_1v1` ทำให้คำตอบแรกเป็น `Tekken 8 เป็นการแข่งขันออฟไลน์แบบ 1v1 บน PlayStation 5 ใช้รูปแบบ First to 2 (FT2), Round 3 และเวลา 60 วินาที` แต่คำถามต้องการ intent `policy` และยังขาด `เปลี่ยนแปลง, กฎระเบียบ`
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น เปลี่ยนแปลง, กฎระเบียบ

### 182. [FAIL] competition_tekken8_v2_038

- คำถาม: Tekken 8 ถ้าฝ่าฝืนมารยาทมีข้อยกเว้นไหม
- Intent ที่คาด: `penalty`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
- Keyword ที่ขาดใน first line: `ไม่มีข้อยกเว้น, ปรับแพ้`
- Keyword ที่ขาดในคำตอบรวม: `ไม่มีข้อยกเว้น, ปรับแพ้`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5` ซึ่งไม่ใช่คำตอบของคำถาม `Tekken 8 ถ้าฝ่าฝืนมารยาทมีข้อยกเว้นไหม`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยผล/บทลงโทษ/จำนวนครั้งตามที่ถาม เช่น ไม่มีข้อยกเว้น, ปรับแพ้

### 183. [FAIL] competition_tekken8_v2_039

- คำถาม: Tekken 8 เลือกตัวละคร DLC ไม่ได้แต่ใช้ Assist ได้ใช่ไหม
- Intent ที่คาด: `character`
- Route/Mode: `competition_rules` / `pipeline:competition_fact_card`
- Cause: `partial_or_strict_keyword`
- Style: `missing_expected_content` - ทั้งบรรทัดแรกและคำตอบรวมยังขาด keyword สำคัญ
- First line ที่ AI ตอบ: Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน
- Keyword ที่ขาดใน first line: `Assist`
- Keyword ที่ขาดในคำตอบรวม: `Assist`
- Retrieved: `tekken8_character_dlc_rule`
- ทำไมผิด/ปัญหาคืออะไร: คำตอบแรกคือ `Tekken 8 เลือกตัวละครได้ทุกตัว ยกเว้นตัวละคร DLC และห้ามใช้ customization โดยให้ใช้ชุด/สกินมาตรฐาน` แต่ยังไม่ครบ keyword ที่ต้องมีคือ `Assist` หรือใช้คำเทียบเท่าที่ตัวตรวจยังไม่รู้จัก
- ควรตอบขึ้นต้นประมาณไหน: ควรตอบก่อนว่าได้/ไม่ได้/ห้าม/อนุญาต พร้อม keyword หลัก เช่น DLC, Assist

### 184. [FAIL] competition_tekken8_v2_040

- คำถาม: Tekken 8 ต้องเล่นบนแพลตฟอร์มอะไรและเป็นเดี่ยวไหม
- Intent ที่คาด: `format`
- Route/Mode: `games` / `pipeline:games_fast_path`
- Cause: `wrong_route`
- Style: `wrong_domain_first_line` - บรรทัดแรกตอบคนละ domain ตั้งแต่ต้น จึงผิดทั้งเนื้อหาและรูปแบบ
- First line ที่ AI ตอบ: PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5
- Keyword ที่ขาดใน first line: `เดี่ยว, 1v1`
- Keyword ที่ขาดในคำตอบรวม: `เดี่ยว, 1v1`
- Retrieved: `Reservation`
- ทำไมผิด/ปัญหาคืออะไร: คำถามถามกติกาการแข่งขัน แต่ router ส่งไป `games` จึงตอบ `PlayStation 5 มีเกม Marvel’s Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกมอื่น ๆ ในรายการ PlayStation 5` ซึ่งไม่ใช่คำตอบของคำถาม `Tekken 8 ต้องเล่นบนแพลตฟอร์มอะไรและเป็นเดี่ยวไหม`
- ควรตอบขึ้นต้นประมาณไหน: ควรขึ้นต้นด้วยรูปแบบหรือค่าการตั้งค่าที่ถามก่อน เช่น PlayStation 5, เดี่ยว, 1v1
