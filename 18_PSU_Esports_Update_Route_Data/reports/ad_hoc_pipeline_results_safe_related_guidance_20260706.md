# Ad Hoc Pipeline Test Log

- Generated: 2026-07-06T03:58:41
- JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\ad_hoc_pipeline_results_safe_related_guidance_20260706.jsonl`
- Total questions: 10

## Summary

- competition_rules/competition_rules_lookup: 1
- equipment/related_guidance: 7
- games/game_availability_lookup: 1
- service_fee/service_fee_query: 1

## Results

### 1. ถ้าอยากเล่นเกมขยับตัวควรเล่นโซนไหน

- mode: `pipeline:related_guidance_fast_path`
- route: `equipment/related_guidance`
- confidence: `0.92`
- elapsed: `0.0037` sec

คำตอบ:

ถ้าอยากเล่นเกมที่ได้ขยับตัวหรือเล่นตามจังหวะ แนะนำเริ่มจาก VR Zone
- เกมที่ยืนยันได้: Beat Saber เป็นเกม VR Rhythm ใช้ดาบแสงฟันบล็อกตามจังหวะเพลง
- อีกทางเลือกในรายการเกมคือ Nintendo Switch Zone ที่มี Nintendo Switch Sports และ Ring Fit Adventure ใน catalog เกม
ควรเลือกตามความถนัดและสอบถามเจ้าหน้าที่ก่อนเล่นถ้าไม่คุ้นกับอุปกรณ์ VR
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home และ https://esports.phuket.psu.ac.th/Services/our-games

แหล่งข้อมูล:
- our_games | https://esports.phuket.psu.ac.th/Services/our-games
- Reservation | https://esports.computing.psu.ac.th/reservation

### 2. VR กับ Cockpit ต่างกันยังไง

- mode: `pipeline:related_guidance_fast_path`
- route: `equipment/related_guidance`
- confidence: `0.92`
- elapsed: `0.0079` sec

คำตอบ:

ถ้าเทียบ VR กับ Cockpit:
- VR Zone: VR Zone คือโซนเล่นเกม VR โดยใช้ PlayStation VR2 เหมาะกับประสบการณ์เกมเสมือนจริง เกมที่ยืนยันได้คือ Beat Saber และ Horizon Call of the Mountain
- Cockpit Zone: Cockpit Zone คือโซนจำลองการขับรถ/เกมแข่งรถ ใช้เล่น Gran Turismo 7 ด้วยชุดพวงมาลัยและเบาะขับ เกมที่ยืนยันได้คือ Gran Turismo 7 (Single Player)
เลือก VR ถ้าอยากได้ประสบการณ์เสมือนจริง/เกม VR; เลือก Cockpit ถ้าอยากเล่นเกมขับรถด้วยพวงมาลัยและเบาะจำลอง
หมายเหตุ: ถ้าถามเรื่องราคา ต้องดูตาม Service Fee แยกตามกลุ่มผู้ใช้และระยะเวลา
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home และ https://esports.phuket.psu.ac.th/Services/our-games

แหล่งข้อมูล:
- our_games | https://esports.phuket.psu.ac.th/Services/our-games
- Reservation | https://esports.computing.psu.ac.th/reservation

### 3. อยากไปกับเพื่อน 4 คนควรเลือกอะไร

- mode: `pipeline:related_guidance_fast_path`
- route: `equipment/related_guidance`
- confidence: `0.92`
- elapsed: `0.0095` sec

คำตอบ:

ถ้าไปกับเพื่อน แนะนำให้เลือกตามสไตล์การเล่น:
- เล่นเป็นกลุ่ม/ครอบครัวหน้าจอเดียว: Nintendo Switch Zone เพราะมีเกม Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกม Nintendo Switch อื่น ๆ ในรายการ
- อยากลอง VR เป็นกลุ่มเล็ก: VR Zone มีเกม Beat Saber และ Horizon Call of the Mountain และตารางค่าบริการระบุ VR 1-5 คนต่อรอบ
- อยากเล่นเกม PC/FPS/MOBA แยกเครื่อง: PC Zone มี Gaming PC 10 เครื่อง และเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, TEKKEN 8 และ League of Legends
หมายเหตุ: ในข้อมูล Service Fee 2026 ที่มีตอนนี้ยังไม่พบราคา PC ที่ยืนยันได้ จึงไม่คำนวณราคา PC ให้เอง
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home และ https://esports.phuket.psu.ac.th/Services/our-games

แหล่งข้อมูล:
- our_games | https://esports.phuket.psu.ac.th/Services/our-games
- Reservation | https://esports.computing.psu.ac.th/reservation

### 4. มีเกมแนวจังหวะไหม

- mode: `pipeline:related_guidance_fast_path`
- route: `equipment/related_guidance`
- confidence: `0.92`
- elapsed: `0.0043` sec

คำตอบ:

ถ้าอยากเล่นเกมที่ได้ขยับตัวหรือเล่นตามจังหวะ แนะนำเริ่มจาก VR Zone
- เกมที่ยืนยันได้: Beat Saber เป็นเกม VR Rhythm ใช้ดาบแสงฟันบล็อกตามจังหวะเพลง
- อีกทางเลือกในรายการเกมคือ Nintendo Switch Zone ที่มี Nintendo Switch Sports และ Ring Fit Adventure ใน catalog เกม
ควรเลือกตามความถนัดและสอบถามเจ้าหน้าที่ก่อนเล่นถ้าไม่คุ้นกับอุปกรณ์ VR
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home และ https://esports.phuket.psu.ac.th/Services/our-games

แหล่งข้อมูล:
- our_games | https://esports.phuket.psu.ac.th/Services/our-games
- Reservation | https://esports.computing.psu.ac.th/reservation

### 5. ศูนย์นี้เหมาะกับนักเรียนไหม

- mode: `pipeline:related_guidance_fast_path`
- route: `equipment/related_guidance`
- confidence: `0.91`
- elapsed: `0.0037` sec

คำตอบ:

ถ้าเป็นนักเรียน/นักศึกษาหรือมือใหม่ แนะนำเลือกจากความอยากลองก่อน:
- อยากเล่นง่ายกับเพื่อน: Nintendo Switch Zone
- อยากลอง VR: VR Zone มี Beat Saber และ Horizon Call of the Mountain
- อยากเล่นเกมคอนโซล 1-2 คน: PlayStation 5 Zone
- อยากฝึกเกม PC/eSports: PC Zone
ข้อมูลค่าบริการมีแยกกลุ่ม PSU Student and Staff, PSU Alumni and General Student และ General Adult; ถ้าระบุกลุ่มผู้ใช้กับโซน ผมจะคำนวณราคาให้ได้
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home และ https://esports.phuket.psu.ac.th/Services/our-games

แหล่งข้อมูล:
- our_games | https://esports.phuket.psu.ac.th/Services/our-games
- Reservation | https://esports.computing.psu.ac.th/reservation

### 6. อยากเล่นเกมขับรถควรเลือกอะไร

- mode: `pipeline:related_guidance_fast_path`
- route: `equipment/related_guidance`
- confidence: `0.92`
- elapsed: `0.0015` sec

คำตอบ:

ถ้าอยากเล่นเกมขับรถ แนะนำ Cockpit Zone
- เหตุผล: Cockpit Zone คือโซนจำลองการขับรถ/เกมแข่งรถ ใช้เล่น Gran Turismo 7 ด้วยชุดพวงมาลัยและเบาะขับ
- อุปกรณ์หลัก: TV 65 นิ้ว 2 เครื่อง (2 Units), Logitech G923 TRUEFORCE Racing wheel + Driving Force Shifter 2 ชุด (2 Units), Racezone Full Cockpit V3 2 ชุด (2 Units) และ Pulse Elite Wireless Headset 2 ชุด (2 Units)
- เกมที่ยืนยันได้: Gran Turismo 7 (Single Player)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home และ https://esports.phuket.psu.ac.th/Services/our-games

แหล่งข้อมูล:
- home | https://esports.phuket.psu.ac.th/home

### 7. มีเกมแนว FPS หรือ MOBA ไหม

- mode: `pipeline:related_guidance_fast_path`
- route: `equipment/related_guidance`
- confidence: `0.91`
- elapsed: `0.0149` sec

คำตอบ:

สรุปแนวเกมที่มีข้อมูลยืนยันได้:
- FPS/Tactical/PC: VALORANT, Counter-Strike 2, Call of Duty: Warzone
- MOBA: League of Legends
- Fighting: TEKKEN 8
- Racing/ขับรถ: Gran Turismo 7 ใน Cockpit Zone
- VR/Rhythm: Beat Saber ใน VR Zone
- Party/เล่นกับเพื่อน: Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home และ https://esports.phuket.psu.ac.th/Services/our-games

แหล่งข้อมูล:
- our_games | https://esports.phuket.psu.ac.th/Services/our-games
- Reservation | https://esports.computing.psu.ac.th/reservation

### 8. VR ราคาเท่าไหร่

- mode: `pipeline:deterministic_calculator_fast`
- route: `service_fee/service_fee_query`
- confidence: `0.97`
- elapsed: `0.0168` sec

คำตอบ:

VR 30 นาที (1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 190 บาท, General Adult 525 บาท
VR 1 ชั่วโมง (60 นาที, 1-5 คน): PSU Student and Staff 0 บาท, PSU Alumni and General Student 375 บาท, General Adult 1050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

แหล่งข้อมูล:
- service_fee_image_2026 | https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### 9. Minecraft เล่นได้ไหม

- mode: `pipeline:games_unknown_fast_path`
- route: `games/game_availability_lookup`
- confidence: `0.94`
- elapsed: `0.0056` sec

คำตอบ:

ยังไม่พบ Minecraft ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ
ถ้าต้องการเล่นเกมนอกเหนือจากรายการนี้ ควรสอบถามเจ้าหน้าที่ก่อนจองหรือก่อนเข้าใช้บริการ

เกมที่มีข้อมูลยืนยันตอนนี้:
- PC Zone: VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, TEKKEN 8 และ League of Legends
- PlayStation 5 Zone: Marvel's Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกม PS5 อื่น ๆ ในรายการ
- Nintendo Switch Zone: Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกม Switch อื่น ๆ ในรายการ
- Cockpit Zone: Gran Turismo 7
- VR Zone: Beat Saber และ Horizon Call of the Mountain
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

แหล่งข้อมูล:
- our_games | https://esports.phuket.psu.ac.th/Services/our-games
- Reservation | https://esports.computing.psu.ac.th/reservation

### 10. Tekken 8 เกมนึงมี 3 rounds ใช่ไหม

- mode: `pipeline:competition_fact_card`
- route: `competition_rules/competition_rules_lookup`
- confidence: `0.96`
- elapsed: `0.0307` sec

คำตอบ:

คำตอบ: Tekken 8 แต่ละเกมตั้งค่าเป็น 3 รอบ (R3)

หลักฐานจากกติกา:
- เอกสารการตั้งค่าเกมระบุ Round 3 / R3

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

แหล่งข้อมูล:
- tekken8_rounds3_challenger | local://competition_rules/competition_rules_tekken8_psu_esports
