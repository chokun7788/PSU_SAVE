# Experimental RAG Fallback Ad Hoc Fix2

| Question | Strict | Experimental |
|---|---|---|
| มีให้เช่าจอไปบ้านไหม | `pipeline:guard_no_answer`: ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ | `pipeline:experimental_soft_related_fallback`: โหมดทดลอง RAG: ข้อมูลที่ยืนยันได้ตอนนี้คือศูนย์มี Gaming Monitor 10 Units สำหรับใช้งานใน PC Zone ภายในศูนย์ |
| รับซ่อมคอมส่วนตัวไหม | `pipeline:guard_no_answer`: ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ | `pipeline:experimental_soft_related_fallback`: โหมดทดลอง RAG: ข้อมูลที่ยืนยันได้คือศูนย์มี Gaming PC สำหรับให้ใช้งานใน PC Zone และมีอุปกรณ์ของศูนย์เอง |
| อยากจัดวันเกิดที่ศูนย์ได้ไหม | `pipeline:no_answer`: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ | `pipeline:experimental_soft_related_fallback`: โหมดทดลอง RAG: ข้อมูลที่ยืนยันได้คือศูนย์มีระบบจองเพื่อเข้าใช้บริการเป็นรอบเวลา |
| มีคอร์สสอนเล่น Valorant ไหม | `pipeline:guard_no_answer`: ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ | `pipeline:experimental_soft_related_fallback`: โหมดทดลอง RAG: ข้อมูลที่ยืนยันได้คือ VALORANT มีให้เล่นใน PC Zone และเป็นเกม Tactical FPS แบบทีม 5v5 |
| ถ้าอยากพาเพื่อนไปเล่นเกมสนุก ๆ ควรเลือกอะไร | `pipeline:related_guidance_fast_path`: ถ้าไปกับเพื่อน แนะนำให้เลือกตามสไตล์การเล่น: | `pipeline:related_guidance_fast_path`: ถ้าไปกับเพื่อน แนะนำให้เลือกตามสไตล์การเล่น: |
| เกมแนวฝึกทีมเวิร์คมีอะไรบ้าง | `pipeline:related_guidance_fast_path`: สรุปแนวเกมที่มีข้อมูลยืนยันได้: | `pipeline:related_guidance_fast_path`: สรุปแนวเกมที่มีข้อมูลยืนยันได้: |
| อยากเล่น Pokemon | `pipeline:games_unknown_fast_path`: ยังไม่พบ Pokemon ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ | `pipeline:games_unknown_fast_path`: ยังไม่พบ Pokemon ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ |
| อยากซื้อคีย์บอร์ดจากศูนย์ | `pipeline:category_rule_fast_path`: ยังไม่พบข้อมูลว่าศูนย์มีบริการขายคีย์บอร์ดเกมมิ่งในฐานข้อมูลที่มี ข้อมูลอุปกรณ์ที่มีเป็นรายการอุปกรณ์สำหรับใช้งานภายในศูนย์ เช่น Gaming Keyboard, Gaming Mouse, Gaming Headset และ Gaming PC | `pipeline:category_rule_fast_path`: ยังไม่พบข้อมูลว่าศูนย์มีบริการขายคีย์บอร์ดเกมมิ่งในฐานข้อมูลที่มี ข้อมูลอุปกรณ์ที่มีเป็นรายการอุปกรณ์สำหรับใช้งานภายในศูนย์ เช่น Gaming Keyboard, Gaming Mouse, Gaming Headset และ Gaming PC |

## Details

### มีให้เช่าจอไปบ้านไหม

- strict: `pipeline:guard_no_answer` / no_answer/guard_no_answer
- experimental: `pipeline:experimental_soft_related_fallback` / no_answer/guard_no_answer

โหมดทดลอง RAG: ข้อมูลที่ยืนยันได้ตอนนี้คือศูนย์มี Gaming Monitor 10 Units สำหรับใช้งานใน PC Zone ภายในศูนย์
ยังไม่มีข้อมูลยืนยันเรื่องบริการเช่าจอ/ยืมจอออกไปใช้นอกสถานที่ในฐานข้อมูลที่มีครับ
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### รับซ่อมคอมส่วนตัวไหม

- strict: `pipeline:guard_no_answer` / no_answer/guard_no_answer
- experimental: `pipeline:experimental_soft_related_fallback` / no_answer/guard_no_answer

โหมดทดลอง RAG: ข้อมูลที่ยืนยันได้คือศูนย์มี Gaming PC สำหรับให้ใช้งานใน PC Zone และมีอุปกรณ์ของศูนย์เอง
ยังไม่มีข้อมูลยืนยันว่าศูนย์รับซ่อมคอมพิวเตอร์ส่วนตัวหรืออุปกรณ์ส่วนตัวของผู้ใช้ครับ
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### อยากจัดวันเกิดที่ศูนย์ได้ไหม

- strict: `pipeline:no_answer` / general/unknown_domain_query
- experimental: `pipeline:experimental_soft_related_fallback` / general/unknown_domain_query

โหมดทดลอง RAG: ข้อมูลที่ยืนยันได้คือศูนย์มีระบบจองเพื่อเข้าใช้บริการเป็นรอบเวลา
แต่ยังไม่มีข้อมูลยืนยันว่าศูนย์รับจัดงานวันเกิด/ปาร์ตี้/อีเวนต์ส่วนตัวในฐานข้อมูลที่มีครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### มีคอร์สสอนเล่น Valorant ไหม

- strict: `pipeline:guard_no_answer` / no_answer/guard_no_answer
- experimental: `pipeline:experimental_soft_related_fallback` / no_answer/guard_no_answer

โหมดทดลอง RAG: ข้อมูลที่ยืนยันได้คือ VALORANT มีให้เล่นใน PC Zone และเป็นเกม Tactical FPS แบบทีม 5v5
แต่ยังไม่มีข้อมูลยืนยันว่าศูนย์มีคอร์สสอนเล่น VALORANT หรือคอร์สฝึกเฉพาะเกมในฐานข้อมูลที่มีครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### ถ้าอยากพาเพื่อนไปเล่นเกมสนุก ๆ ควรเลือกอะไร

- strict: `pipeline:related_guidance_fast_path` / equipment/related_guidance
- experimental: `pipeline:related_guidance_fast_path` / equipment/related_guidance

ถ้าไปกับเพื่อน แนะนำให้เลือกตามสไตล์การเล่น:
- เล่นเป็นกลุ่ม/ครอบครัวหน้าจอเดียว: Nintendo Switch Zone เพราะมีเกม Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกม Nintendo Switch อื่น ๆ ในรายการ
- อยากลอง VR เป็นกลุ่มเล็ก: VR Zone มีเกม Beat Saber และ Horizon Call of the Mountain และตารางค่าบริการระบุ VR 1-5 คนต่อรอบ
- อยากเล่นเกม PC/FPS/MOBA แยกเครื่อง: PC Zone มี Gaming PC 10 เครื่อง และเกม VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, TEKKEN 8 และ League of Legends
หมายเหตุ: ในข้อมูล Service Fee 2026 ที่มีตอนนี้ยังไม่พบราคา PC ที่ยืนยันได้ จึงไม่คำนวณราคา PC ให้เอง
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home และ https://esports.phuket.psu.ac.th/Services/our-games

### เกมแนวฝึกทีมเวิร์คมีอะไรบ้าง

- strict: `pipeline:related_guidance_fast_path` / games/games_lookup
- experimental: `pipeline:related_guidance_fast_path` / games/games_lookup

สรุปแนวเกมที่มีข้อมูลยืนยันได้:
- FPS/Tactical/PC: VALORANT, Counter-Strike 2, Call of Duty: Warzone
- MOBA: League of Legends
- Fighting: TEKKEN 8
- Racing/ขับรถ: Gran Turismo 7 ใน Cockpit Zone
- VR/Rhythm: Beat Saber ใน VR Zone
- Party/เล่นกับเพื่อน: Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home และ https://esports.phuket.psu.ac.th/Services/our-games

### อยากเล่น Pokemon

- strict: `pipeline:games_unknown_fast_path` / games/game_availability_lookup
- experimental: `pipeline:games_unknown_fast_path` / games/game_availability_lookup

ยังไม่พบ Pokemon ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ
ถ้าต้องการเล่นเกมนอกเหนือจากรายการนี้ ควรสอบถามเจ้าหน้าที่ก่อนจองหรือก่อนเข้าใช้บริการ

เกมที่มีข้อมูลยืนยันตอนนี้:
- PC Zone: VALORANT, Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, TEKKEN 8 และ League of Legends
- PlayStation 5 Zone: Marvel's Spider-Man 2, TEKKEN 8, Fortnite, God of War Ragnarok และเกม PS5 อื่น ๆ ในรายการ
- Nintendo Switch Zone: Mario Kart 8 Deluxe, Overcooked 2, Super Smash Bros Ultimate, Nintendo Switch Sports และเกม Switch อื่น ๆ ในรายการ
- Cockpit Zone: Gran Turismo 7
- VR Zone: Beat Saber และ Horizon Call of the Mountain
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### อยากซื้อคีย์บอร์ดจากศูนย์

- strict: `pipeline:category_rule_fast_path` / general/unknown_domain_query
- experimental: `pipeline:category_rule_fast_path` / general/unknown_domain_query

ยังไม่พบข้อมูลว่าศูนย์มีบริการขายคีย์บอร์ดเกมมิ่งในฐานข้อมูลที่มี ข้อมูลอุปกรณ์ที่มีเป็นรายการอุปกรณ์สำหรับใช้งานภายในศูนย์ เช่น Gaming Keyboard, Gaming Mouse, Gaming Headset และ Gaming PC
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
