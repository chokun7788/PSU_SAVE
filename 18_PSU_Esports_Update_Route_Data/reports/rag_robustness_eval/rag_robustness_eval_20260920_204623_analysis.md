# RAG Robustness Evaluation Analysis

- Generated: 2026-09-20T20:46:23
- Detail input: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\rag_robustness_eval\rag_robustness_eval_20260920_204623.json`
- Evaluated: 600
- Passed: 342 (57.00%)
- Failed: 258 (43.00%)

## Locale Comparison

| Locale | Cases | Passed | Failed | Pass rate |
| --- | ---: | ---: | ---: | ---: |
| th | 300 | 183 | 117 | 61.00% |
| en | 300 | 159 | 141 | 53.00% |

## Failure Taxonomy

- `route_mismatch`: 174
- `safe_outcome_mismatch`: 147

## Results by Group

| Group | Passed | Failed | Pass rate |
| --- | ---: | ---: | ---: |
| booking | 34 | 22 | 60.71% |
| clarification | 3 | 61 | 4.69% |
| competition | 60 | 20 | 75.00% |
| contact | 12 | 4 | 75.00% |
| equipment | 28 | 28 | 50.00% |
| games | 70 | 26 | 72.92% |
| general | 5 | 3 | 62.50% |
| input_quality | 8 | 16 | 33.33% |
| live_availability | 0 | 32 | 0.00% |
| live_schedule | 19 | 5 | 79.17% |
| members | 12 | 4 | 75.00% |
| out_of_scope | 8 | 8 | 50.00% |
| overview | 8 | 8 | 50.00% |
| rules | 8 | 8 | 50.00% |
| schedule | 28 | 4 | 87.50% |
| service_fee | 39 | 9 | 81.25% |

## Most Frequent Route Mismatches

- `schedule` instead of `reservation`: 41
- `games` instead of `competition_rules`: 20
- `schedule` instead of `games`: 14
- `games` instead of `equipment | game_controls`: 8
- `no_answer` instead of `general | unknown`: 8
- `games` instead of `equipment`: 7
- `no_answer` instead of `reservation`: 5
- `clarification` instead of `service_fee | general`: 4
- `clarification` instead of `reservation`: 4
- `clarification` instead of `overview | members`: 4
- `no_answer` instead of `contact | overview`: 4
- `general` instead of `rules | overview`: 4

## Slowest Cases

| Case | Locale | Group | Elapsed | Route | Status | Question |
| --- | --- | --- | ---: | --- | --- | --- |
| RAG-ROBUST-TH-071 | th | equipment | 14.953s | games | no_answer | กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า มีเมาส์เกมมิ่งให้ไหม |
| RAG-ROBUST-TH-086 | th | service_fee | 11.631s | general | no_answer | ขอข้อมูลที่ยืนยันได้หน่อยครับ: เล่น PC 2 ชั่วโมง บุคคลทั่วไปคิดยังไง |
| RAG-ROBUST-TH-085 | th | service_fee | 10.105s | general | no_answer | เล่น PC 2 ชั่วโมง บุคคลทั่วไปคิดยังไง |
| RAG-ROBUST-TH-033 | th | games | 8.878s | games | no_answer | ที่ศูนย์มี Minecraft ไหม |
| RAG-ROBUST-TH-035 | th | games | 7.416s | games | no_answer | กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า ที่ศูนย์มี Minecraft ไหม |
| RAG-ROBUST-TH-070 | th | equipment | 7.372s | games | no_answer | ขอข้อมูลที่ยืนยันได้หน่อยครับ: มีเมาส์เกมมิ่งให้ไหม |
| RAG-ROBUST-TH-066 | th | equipment | 7.034s | equipment | answer | ขอข้อมูลที่ยืนยันได้หน่อยครับ: เอาคีย์บอร์ดตัวเองมาใช้ได้ไหม |
| RAG-ROBUST-TH-034 | th | games | 6.790s | games | no_answer | ขอข้อมูลที่ยืนยันได้หน่อยครับ: ที่ศูนย์มี Minecraft ไหม |
| RAG-ROBUST-TH-088 | th | service_fee | 6.622s | general | no_answer | เล่น PC 2 ชั่วโมง บุคคลทั่วไปคิดยังไง อะ |
| RAG-ROBUST-TH-065 | th | equipment | 5.941s | equipment | answer | เอาคีย์บอร์ดตัวเองมาใช้ได้ไหม |
| RAG-ROBUST-TH-290 | th | out_of_scope | 4.969s | general | no_answer | ขอข้อมูลที่ยืนยันได้หน่อยครับ: พรุ่งนี้ฝนตกไหม |
| RAG-ROBUST-TH-289 | th | out_of_scope | 4.487s | general | no_answer | พรุ่งนี้ฝนตกไหม |
| RAG-ROBUST-TH-125 | th | live_availability | 2.106s | schedule | answer | PC เครื่อง 2 ว่างไหมตอนนี้ |
| RAG-ROBUST-EN-001 | en | games | 2.098s | schedule | answer | What games are currently available? |
| RAG-ROBUST-TH-285 | th | booking | 2.091s | schedule | answer | pc2 available ตอน 3pm ไหม |

## Representative Failures

### RAG-ROBUST-TH-005 (th, games)
- Question: PC Zone มีเกมอะไรให้เล่น
- Expected: route `games`; outcome `answer_available`
- Actual: route `games`; outcome `clarification`; mode `pipeline:game_target_ambiguous`; 0.084s
- Failure: outcome expected answer_available, got clarification
- Answer excerpt: ยังไม่แน่ใจว่าหมายถึงเกมใดครับ จึงไม่ขอดึงข้อมูลของเกมอื่นมาตอบแทน กรุณาระบุชื่อเกมให้ชัดเจนอีกครั้ง

### RAG-ROBUST-TH-006 (th, games)
- Question: ขอข้อมูลที่ยืนยันได้หน่อยครับ: PC Zone มีเกมอะไรให้เล่น
- Expected: route `games`; outcome `answer_available`
- Actual: route `games`; outcome `clarification`; mode `pipeline:game_target_ambiguous`; 0.093s
- Failure: outcome expected answer_available, got clarification
- Answer excerpt: ยังไม่แน่ใจว่าหมายถึงเกมใดครับ จึงไม่ขอดึงข้อมูลของเกมอื่นมาตอบแทน กรุณาระบุชื่อเกมให้ชัดเจนอีกครั้ง

### RAG-ROBUST-TH-007 (th, games)
- Question: กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า PC Zone มีเกมอะไรให้เล่น
- Expected: route `games`; outcome `answer_available`
- Actual: route `games`; outcome `clarification`; mode `pipeline:game_target_ambiguous`; 0.105s
- Failure: outcome expected answer_available, got clarification
- Answer excerpt: ยังไม่แน่ใจว่าหมายถึงเกมใดครับ จึงไม่ขอดึงข้อมูลของเกมอื่นมาตอบแทน กรุณาระบุชื่อเกมให้ชัดเจนอีกครั้ง

### RAG-ROBUST-TH-008 (th, games)
- Question: PC Zone มีเกมอะไรให้เล่น อะ
- Expected: route `games`; outcome `answer_available`
- Actual: route `games`; outcome `clarification`; mode `pipeline:game_target_ambiguous`; 0.078s
- Failure: outcome expected answer_available, got clarification
- Answer excerpt: ยังไม่แน่ใจว่าหมายถึงเกมใดครับ จึงไม่ขอดึงข้อมูลของเกมอื่นมาตอบแทน กรุณาระบุชื่อเกมให้ชัดเจนอีกครั้ง

### RAG-ROBUST-TH-041 (th, clarification)
- Question: เกมนี้เล่นที่ไหน
- Expected: route `games, general`; outcome `clarification_required`
- Actual: route `games`; outcome `answer`; mode `pipeline:structured_games_catalog`; 0.392s
- Failure: outcome expected clarification_required, got answer
- Answer excerpt: ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 42 เกมครับ PC Zone (6 เกม) • Call of Duty: Warzone • Counter-Strike 2 • League of Legends • PUBG: BATTLEGROUNDS • TEKKEN 8 • VALORANT PlayStation 5 Zone (17 เกม) • Call of Duty: Modern Warfare III • Delta Force • EA Sports FC 24 • eFootball • FINAL FANTASY XVI • Fortnite • God of War Ragnarok • Hogwarts Legacy • Marvel's Spi...

### RAG-ROBUST-TH-042 (th, clarification)
- Question: ขอข้อมูลที่ยืนยันได้หน่อยครับ: เกมนี้เล่นที่ไหน
- Expected: route `games, general`; outcome `clarification_required`
- Actual: route `games`; outcome `answer`; mode `pipeline:structured_games_catalog`; 0.758s
- Failure: outcome expected clarification_required, got answer
- Answer excerpt: ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 42 เกมครับ PC Zone (6 เกม) • Call of Duty: Warzone • Counter-Strike 2 • League of Legends • PUBG: BATTLEGROUNDS • TEKKEN 8 • VALORANT PlayStation 5 Zone (17 เกม) • Call of Duty: Modern Warfare III • Delta Force • EA Sports FC 24 • eFootball • FINAL FANTASY XVI • Fortnite • God of War Ragnarok • Hogwarts Legacy • Marvel's Spi...

### RAG-ROBUST-TH-043 (th, clarification)
- Question: กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า เกมนี้เล่นที่ไหน
- Expected: route `games, general`; outcome `clarification_required`
- Actual: route `games`; outcome `answer`; mode `pipeline:structured_service_game_availability`; 0.491s
- Failure: outcome expected clarification_required, got answer
- Answer excerpt: บริการที่ถาม มีเกมที่ยืนยันได้ดังนี้ PC #01-#02 (60 นาที, 1 คน) • TEKKEN 8 • Counter-Strike 2 • League of Legends • PUBG: BATTLEGROUNDS • VALORANT หมายเหตุ: PC #01-#02 มี TEKKEN 8 แต่ไม่มี Call of Duty: Warzone หมายเหตุ: PC #01-#02 และ PC #03-#10 มี Counter-Strike 2, League of Legends, PUBG: BATTLEGROUNDS, VALORANT เหมือนกัน PC #03-#10 (60 นาที, 1 คน) • C...

### RAG-ROBUST-TH-044 (th, clarification)
- Question: เกมนี้เล่นที่ไหน อะ
- Expected: route `games, general`; outcome `clarification_required`
- Actual: route `games`; outcome `answer`; mode `pipeline:structured_games_catalog`; 0.243s
- Failure: outcome expected clarification_required, got answer
- Answer excerpt: ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 42 เกมครับ PC Zone (6 เกม) • Call of Duty: Warzone • Counter-Strike 2 • League of Legends • PUBG: BATTLEGROUNDS • TEKKEN 8 • VALORANT PlayStation 5 Zone (17 เกม) • Call of Duty: Modern Warfare III • Delta Force • EA Sports FC 24 • eFootball • FINAL FANTASY XVI • Fortnite • God of War Ragnarok • Hogwarts Legacy • Marvel's Spi...

### RAG-ROBUST-TH-057 (th, equipment)
- Question: PS5 ใช้จอยแบบไหน
- Expected: route `equipment, game_controls`; outcome `answer_available`
- Actual: route `games`; outcome `clarification`; mode `pipeline:game_control_missing_game_context`; 0.057s
- Failure: route expected one of ['equipment', 'game_controls'], got games; outcome expected answer_available, got clarification
- Answer excerpt: ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

### RAG-ROBUST-TH-058 (th, equipment)
- Question: ขอข้อมูลที่ยืนยันได้หน่อยครับ: PS5 ใช้จอยแบบไหน
- Expected: route `equipment, game_controls`; outcome `answer_available`
- Actual: route `games`; outcome `clarification`; mode `pipeline:game_control_missing_game_context`; 0.161s
- Failure: route expected one of ['equipment', 'game_controls'], got games; outcome expected answer_available, got clarification
- Answer excerpt: ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

### RAG-ROBUST-TH-059 (th, equipment)
- Question: กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า PS5 ใช้จอยแบบไหน
- Expected: route `equipment, game_controls`; outcome `answer_available`
- Actual: route `games`; outcome `clarification`; mode `pipeline:game_control_missing_game_context`; 0.165s
- Failure: route expected one of ['equipment', 'game_controls'], got games; outcome expected answer_available, got clarification
- Answer excerpt: ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

### RAG-ROBUST-TH-060 (th, equipment)
- Question: PS5 ใช้จอยแบบไหน อะ
- Expected: route `equipment, game_controls`; outcome `answer_available`
- Actual: route `games`; outcome `clarification`; mode `pipeline:game_control_missing_game_context`; 0.040s
- Failure: route expected one of ['equipment', 'game_controls'], got games; outcome expected answer_available, got clarification
- Answer excerpt: ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

### RAG-ROBUST-TH-069 (th, equipment)
- Question: มีเมาส์เกมมิ่งให้ไหม
- Expected: route `equipment`; outcome `answer_available`
- Actual: route `games`; outcome `no_answer`; mode `pipeline:no_answer`; 1.771s
- Failure: route expected one of ['equipment'], got games; outcome expected answer_available, got no_answer
- Answer excerpt: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### RAG-ROBUST-TH-070 (th, equipment)
- Question: ขอข้อมูลที่ยืนยันได้หน่อยครับ: มีเมาส์เกมมิ่งให้ไหม
- Expected: route `equipment`; outcome `answer_available`
- Actual: route `games`; outcome `no_answer`; mode `pipeline:no_answer`; 7.372s
- Failure: route expected one of ['equipment'], got games; outcome expected answer_available, got no_answer
- Answer excerpt: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### RAG-ROBUST-TH-071 (th, equipment)
- Question: กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า มีเมาส์เกมมิ่งให้ไหม
- Expected: route `equipment`; outcome `answer_available`
- Actual: route `games`; outcome `no_answer`; mode `pipeline:no_answer`; 14.953s
- Failure: route expected one of ['equipment'], got games; outcome expected answer_available, got no_answer
- Answer excerpt: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### RAG-ROBUST-TH-072 (th, equipment)
- Question: มีเมาส์เกมมิ่งให้มั้ย
- Expected: route `equipment`; outcome `answer_available`
- Actual: route `games`; outcome `no_answer`; mode `pipeline:no_answer`; 1.926s
- Failure: route expected one of ['equipment'], got games; outcome expected answer_available, got no_answer
- Answer excerpt: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### RAG-ROBUST-TH-073 (th, equipment)
- Question: เครื่อง PC ใช้การ์ดจอรุ่นอะไร
- Expected: route `equipment`; outcome `no_answer_expected`
- Actual: route `equipment`; outcome `answer`; mode `pipeline:structured_equipment_item`; 0.185s
- Failure: outcome expected no_answer_expected, got answer
- Answer excerpt: Gaming Monitor: จอภาพสำหรับใช้คู่กับ Gaming PC ใน PC Zone จำนวน: 10 Units อยู่ที่: PC Zone ใช้สำหรับ: • แสดงผลเกมและโปรแกรมบน PC Zone แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### RAG-ROBUST-TH-074 (th, equipment)
- Question: ขอข้อมูลที่ยืนยันได้หน่อยครับ: เครื่อง PC ใช้การ์ดจอรุ่นอะไร
- Expected: route `equipment`; outcome `no_answer_expected`
- Actual: route `equipment`; outcome `answer`; mode `pipeline:structured_equipment_item`; 0.275s
- Failure: outcome expected no_answer_expected, got answer
- Answer excerpt: Gaming Monitor: จอภาพสำหรับใช้คู่กับ Gaming PC ใน PC Zone จำนวน: 10 Units อยู่ที่: PC Zone ใช้สำหรับ: • แสดงผลเกมและโปรแกรมบน PC Zone แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### RAG-ROBUST-TH-075 (th, equipment)
- Question: กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า เครื่อง PC ใช้การ์ดจอรุ่นอะไร
- Expected: route `equipment`; outcome `no_answer_expected`
- Actual: route `equipment`; outcome `answer`; mode `pipeline:structured_equipment_item`; 0.299s
- Failure: outcome expected no_answer_expected, got answer
- Answer excerpt: Gaming Monitor: จอภาพสำหรับใช้คู่กับ Gaming PC ใน PC Zone จำนวน: 10 Units อยู่ที่: PC Zone ใช้สำหรับ: • แสดงผลเกมและโปรแกรมบน PC Zone แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### RAG-ROBUST-TH-076 (th, equipment)
- Question: เครื่อง PC ใช้การ์ดจอรุ่นอะไร อะ
- Expected: route `equipment`; outcome `no_answer_expected`
- Actual: route `equipment`; outcome `answer`; mode `pipeline:structured_equipment_item`; 0.181s
- Failure: outcome expected no_answer_expected, got answer
- Answer excerpt: Gaming Monitor: จอภาพสำหรับใช้คู่กับ Gaming PC ใน PC Zone จำนวน: 10 Units อยู่ที่: PC Zone ใช้สำหรับ: • แสดงผลเกมและโปรแกรมบน PC Zone แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

## Interpretation

- This report scores routing, safe outcome, validation and latency. It does not claim that passing prose is fully owner-approved factual content.
- `live_lookup_required` verifies that the pipeline provides a safe non-stale response path; availability accuracy additionally requires a reachable live booking source.
- Use failures with their trace in the detail JSON to prioritize fixes. Do not weaken expected routes merely to raise the score unless the runtime route contract has deliberately changed.
