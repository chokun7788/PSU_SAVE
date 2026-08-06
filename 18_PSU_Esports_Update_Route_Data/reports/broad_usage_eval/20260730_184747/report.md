# Broad Usage Eval v1

- Generated at: 2026-07-30T18:49:34
- Cases: 667
- Turn checks: 679
- Passed: 666
- Failed: 13
- Pass rate: 0.9809
- Total wall sec: 106.62
- Allow LLM: False
- RAG fallback: False

## By Group
- ambiguity_no_answer: 25/25 pass, 0 fail
- competition_rules: 75/75 pass, 0 fail
- compound: 15/15 pass, 0 fail
- equipment: 58/58 pass, 0 fail
- game_controls: 154/159 pass, 5 fail
- games: 152/158 pass, 6 fail
- members: 47/47 pass, 0 fail
- reservation: 20/20 pass, 0 fail
- schedule: 10/10 pass, 0 fail
- service_fee: 87/88 pass, 1 fail
- session_followup: 23/24 pass, 1 fail

## By Strategy
- clarification: 15
- compound: 15
- fast/rule: 163
- no_answer: 7
- pipeline: 9
- rag/retrieval: 20
- structured: 450

## Common Problems
- missing 'Mario Kart Live': 2
- missing any of ['L (Left Stick)', 'เคลื่อนที่']: 2
- answer_validator_not_ok: 1
- missing 'EA Sports FC 24': 1
- missing 'Overcooked 2': 1
- missing any of ['L3 (Click Left Stick)', 'หันมองจุดสนใจ']: 1
- missing any of ['R (Right Stick)', 'มุมกล้อง']: 1
- missing any of ['The Last of Us Part I / Part II', 'วิธีเล่น', 'เล่นได้ที่']: 1
- missing any of ['แนวเกม', 'เกม Action-Adventure']: 1
- missing any of ['แนวเกม', 'เกม Life Simulation']: 1
- missing any of ['แนวเกม', 'เกมยิง Tactical FPS']: 1

## Top Failures

### SF-081 service_fee
- Question: Overcooked 2 ราคาเท่าไหร่
- Resolved: -
- Mode: `pipeline:structured_service_fee_by_game`
- Route: `service_fee/service_fee_query`
- Problems: missing 'Overcooked 2'
- Answer: Overcooked! 2 ไม่มีราคาแยกตามชื่อเกมครับ ต้องดูราคาตามโซน/บริการที่ใช้เล่นเกมนี้  Nintendo Switch Zone ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคา Nintendo Switch ทุกกลุ่มให้เทียบก่อน  Nintendo Switch 1 ชั่วโมง (1-2 คน) •    นักศึกษา/นักเรียน/บุคลากร PSU: 0 บาท •    ศิษ...

### G-008 games
- Question: Counter-Strike 2 เป็นเกมแนวไหน
- Resolved: -
- Mode: `pipeline:structured_service_game_availability`
- Route: `games/count`
- Problems: missing any of ['แนวเกม', 'เกมยิง Tactical FPS']
- Answer: บริการที่ถาม มีเกมที่ยืนยันได้ 42 เกมครับ  PC #01-#02 (60 นาที, 1 คน) •    TEKKEN 8 •    Counter-Strike 2 •    League of Legends •    PUBG: BATTLEGROUNDS •    VALORANT หมายเหตุ: PC #01-#02 มี TEKKEN 8 แต่ไม่มี Call of Duty: Warzone หมายเหตุ: PC #01-#02 และ PC...

### G-053 games
- Question: EA Sports FC 24 คือเกมอะไร
- Resolved: -
- Mode: `pipeline:games_genre_list_fast_path`
- Route: `games/game_availability_lookup`
- Problems: missing 'EA Sports FC 24'
- Answer: เกมแนว Sports ที่พบในรายการเกมที่ยืนยันได้:  Nintendo Switch Sports •    แนวเกม: เกมกีฬา Motion Control •    เล่นได้ที่: Nintendo Switch Zone แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### G-061 games
- Question: Hogwarts Legacy คือเกมอะไร
- Resolved: -
- Mode: `pipeline:games_genre_no_answer_fast_path`
- Route: `games/game_availability_lookup`
- Problems: answer_validator_not_ok
- Answer: ยังไม่พบเกมแนว Real-Time Strategy (RTS) ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ เกมที่มีข้อมูลยืนยันตอนนี้ทั้งหมด 42 เกม:  PC Zone (6 เกม) •    Call of Duty: Warzone •    Counter-Strike 2 •    League of Legends •    PUBG: BATTLEGROUNDS •...

### G-079 games
- Question: The Last of Us Part I / Part II เล่นยังไง
- Resolved: -
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Problems: missing any of ['The Last of Us Part I / Part II', 'วิธีเล่น', 'เล่นได้ที่']
- Answer: The Last of Us Part I มีข้อมูลปุ่มควบคุมดังนี้: PlayStation / PS5 •    L (Left Stick): เคลื่อนที่ - บังคับทิศทางการเดินและการย่องเคลื่อนที่ของตัวละคร •    L3 (Click Left Stick): หันมองจุดสนใจ - กดเพื่อหันมุมกล้องไปยังวัตถุ เหตุการณ์ หรือจุดสำคัญในฉากที่เกมแนะน...

### G-080 games
- Question: The Last of Us Part I / Part II เป็นเกมแนวไหน
- Resolved: -
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_detail_lookup`
- Problems: missing any of ['แนวเกม', 'เกม Action-Adventure']
- Answer: The Last of Us Part I: สัมผัสการเล่าเรื่องสุดซึ้งและตัวละครที่ลืมไม่ลงใน The Last of Us ที่ชนะรางวัล Game of the Year กว่า 200 รางวัล ในอารยธรรมที่ล่มสลาย ที่ที่ผู้ติดเชื้อและผู้รอดชีวิตไร้ซึ่งความเมตตามีอยู่เต็มไปหมด โจเอล ตัวเอกผู้รู้สึกเหน็ดหน่ายได้รับจ้างใ...

### G-104 games
- Question: Animal Crossing: New Horizons เป็นเกมแนวไหน
- Resolved: -
- Mode: `pipeline:structured_game_detail`
- Route: `games/game_detail_lookup`
- Problems: missing any of ['แนวเกม', 'เกม Life Simulation']
- Answer: Animal Crossing: New Horizon: มีข้อมูลเกมนี้ในฐานข้อมูลของศูนย์ เล่นได้ที่: Nintendo Switch Zone แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### GC-003 game_controls
- Question: Animal Crossing: New Horizons ปุ่มเคลื่อนที่กดอะไร
- Resolved: -
- Mode: `pipeline:structured_game_controls_no_data`
- Route: `games/game_control_lookup`
- Problems: missing any of ['L (Left Stick)', 'เคลื่อนที่']
- Answer: Animal Crossing: New Horizon มีอยู่ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ เล่นได้ที่: Nintendo Switch Zone ยังไม่พบข้อมูลปุ่มควบคุมของ Animal Crossing: New Horizon ที่ยืนยันได้ในฐานข้อมูลตอนนี้ครับ แหล่งข้อมูล: https://esports.phuket.psu.a...

### GC-004 game_controls
- Question: Animal Crossing: New Horizons ปุ่มมุมกล้องกดอะไร
- Resolved: -
- Mode: `pipeline:structured_game_controls_no_data`
- Route: `games/game_control_lookup`
- Problems: missing any of ['R (Right Stick)', 'มุมกล้อง']
- Answer: Animal Crossing: New Horizon มีอยู่ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ เล่นได้ที่: Nintendo Switch Zone ยังไม่พบข้อมูลปุ่มควบคุมของ Animal Crossing: New Horizon ที่ยืนยันได้ในฐานข้อมูลตอนนี้ครับ แหล่งข้อมูล: https://esports.phuket.psu.a...

### GC-069 game_controls
- Question: Mario Kart Live: Home Circuit ปุ่มทั้งหมดมีอะไรบ้าง
- Resolved: -
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Problems: missing 'Mario Kart Live'
- Answer: Mario Kart 8 Deluxe มีข้อมูลปุ่มควบคุมดังนี้: Nintendo Switch •    L (Left Stick): เลี้ยว / ควบคุมทิศทาง - บังคับพวงมาลัยรถให้เลี้ยวไปทางซ้ายหรือขวา •    A: เร่งเครื่อง - กดค้างไว้ตลอดเพื่อเร่งเครื่องยนต์ให้รถวิ่งไปข้างหน้า •    B: เบรก / ถอยหลัง - แตะเพื่อเบร...

### GC-139 game_controls
- Question: The Last of Us Part II ปุ่มเคลื่อนที่กดอะไร
- Resolved: -
- Mode: `pipeline:structured_game_controls_no_data`
- Route: `games/game_control_lookup`
- Problems: missing any of ['L (Left Stick)', 'เคลื่อนที่']
- Answer: The Last of Us Part II (Remastered) มีอยู่ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ เล่นเกมที่ชนะรางวัล Game of the Year กว่า 300 รางวัล ในรูปแบบรีมาสเตอร์สำหรับคอนโซล PlayStation®5 สัมผัสเรื่องราวของเอลลี่และแอ็บบี้อีกครั้ง หรือเล่นเป็นครั้ง...

### GC-140 game_controls
- Question: The Last of Us Part II ปุ่มหันมองจุดสนใจกดอะไร
- Resolved: -
- Mode: `pipeline:structured_game_controls_no_data`
- Route: `games/game_control_lookup`
- Problems: missing any of ['L3 (Click Left Stick)', 'หันมองจุดสนใจ']
- Answer: The Last of Us Part II (Remastered) มีอยู่ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ เล่นเกมที่ชนะรางวัล Game of the Year กว่า 300 รางวัล ในรูปแบบรีมาสเตอร์สำหรับคอนโซล PlayStation®5 สัมผัสเรื่องราวของเอลลี่และแอ็บบี้อีกครั้ง หรือเล่นเป็นครั้ง...

### SF-002 session_followup
- Question: ปุ่มเร่งเครื่องกดอะไร
- Resolved: Mario Kart 8 Deluxe ปุ่มเร่งเครื่องกดอะไร
- Mode: `pipeline:structured_game_controls`
- Route: `games/game_control_lookup`
- Problems: missing 'Mario Kart Live'
- Answer: Mario Kart 8 Deluxe ปุ่มที่ตรงกับคำถาม: Nintendo Switch •    A: เร่งเครื่อง - กดค้างไว้ตลอดเพื่อเร่งเครื่องยนต์ให้รถวิ่งไปข้างหน้า แหล่งข้อมูล: https://gameinputdatabase.com/game/57
