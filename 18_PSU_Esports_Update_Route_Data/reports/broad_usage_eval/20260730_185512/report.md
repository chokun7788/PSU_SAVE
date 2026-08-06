# Broad Usage Eval v1

- Generated at: 2026-07-30T18:56:55
- Cases: 667
- Turn checks: 679
- Passed: 674
- Failed: 5
- Pass rate: 0.9926
- Total wall sec: 102.896
- Allow LLM: False
- RAG fallback: False

## By Group
- ambiguity_no_answer: 25/25 pass, 0 fail
- competition_rules: 75/75 pass, 0 fail
- compound: 15/15 pass, 0 fail
- equipment: 58/58 pass, 0 fail
- game_controls: 156/159 pass, 3 fail
- games: 158/158 pass, 0 fail
- members: 47/47 pass, 0 fail
- reservation: 20/20 pass, 0 fail
- schedule: 10/10 pass, 0 fail
- service_fee: 87/88 pass, 1 fail
- session_followup: 23/24 pass, 1 fail

## By Strategy
- clarification: 15
- compound: 15
- fast/rule: 126
- no_answer: 7
- pipeline: 9
- rag/retrieval: 20
- structured: 487

## Common Problems
- missing 'Mario Kart Live': 2
- missing 'Overcooked 2': 1
- missing any of ['L (Left Stick)', 'เคลื่อนที่']: 1
- missing any of ['L3 (Click Left Stick)', 'หันมองจุดสนใจ']: 1

## Top Failures

### SF-081 service_fee
- Question: Overcooked 2 ราคาเท่าไหร่
- Resolved: -
- Mode: `pipeline:structured_service_fee_by_game`
- Route: `service_fee/service_fee_query`
- Problems: missing 'Overcooked 2'
- Answer: Overcooked! 2 ไม่มีราคาแยกตามชื่อเกมครับ ต้องดูราคาตามโซน/บริการที่ใช้เล่นเกมนี้  Nintendo Switch Zone ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคา Nintendo Switch ทุกกลุ่มให้เทียบก่อน  Nintendo Switch 1 ชั่วโมง (1-2 คน) •    นักศึกษา/นักเรียน/บุคลากร PSU: 0 บาท •    ศิษ...

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
