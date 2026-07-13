# Experimental RAG Fallback Ad Hoc Fix1

| Question | Strict | Experimental |
|---|---|---|
| มีให้เช่าจอไปบ้านไหม | `pipeline:guard_no_answer`: ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ | `pipeline:experimental_soft_related_fallback`: โหมดทดลอง RAG: ข้อมูลที่ยืนยันได้ตอนนี้คือศูนย์มี Gaming Monitor 10 Units สำหรับใช้งานใน PC Zone ภายในศูนย์ |
| รับซ่อมคอมส่วนตัวไหม | `pipeline:guard_no_answer`: ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ | `pipeline:experimental_soft_related_fallback`: โหมดทดลอง RAG: ข้อมูลที่ยืนยันได้คือศูนย์มี Gaming PC สำหรับให้ใช้งานใน PC Zone และมีอุปกรณ์ของศูนย์เอง |
| อยากจัดวันเกิดที่ศูนย์ได้ไหม | `pipeline:rag_direct_curated`: PSU Phuket VALORANT 2026 Tournament จัดขึ้นเมื่อวันที่ 21 กุมภาพันธ์ 2569 โดยเป็นการแข่งขันเกม VALORANT ณ PSU Esports Studio - Phuket | `pipeline:rag_direct_curated`: PSU Phuket VALORANT 2026 Tournament จัดขึ้นเมื่อวันที่ 21 กุมภาพันธ์ 2569 โดยเป็นการแข่งขันเกม VALORANT ณ PSU Esports Studio - Phuket |
| มีคอร์สสอนเล่น Valorant ไหม | `pipeline:guard_no_answer`: ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ | `pipeline:experimental_soft_related_fallback`: โหมดทดลอง RAG: ข้อมูลที่ยืนยันได้คือ VALORANT มีให้เล่นใน PC Zone และเป็นเกม Tactical FPS แบบทีม 5v5 |
| ถ้าอยากพาเพื่อนไปเล่นเกมสนุก ๆ ควรเลือกอะไร | `pipeline:related_guidance_fast_path`: ถ้าไปกับเพื่อน แนะนำให้เลือกตามสไตล์การเล่น: | `pipeline:experimental_rag_direct_fallback`: โหมดทดลอง RAG: ข้อมูลที่ใกล้กับคำถามที่สุดคือ Arena of Valor (RoV): 4. ระเบียบและกติกาการแข่งขัน |
| เกมแนวฝึกทีมเวิร์คมีอะไรบ้าง | `pipeline:related_guidance_fast_path`: สรุปแนวเกมที่มีข้อมูลยืนยันได้: | `pipeline:related_guidance_fast_path`: สรุปแนวเกมที่มีข้อมูลยืนยันได้: |
| อยากเล่น Pokemon | `pipeline:games_unknown_fast_path`: ยังไม่พบ Pokemon ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ | `pipeline:rag_direct_curated`: Animal Crossing: New Horizons: Animal Crossing: New Horizons คือเกมใช้ชีวิตบนเกาะ ผู้เล่นตกแต่งบ้าน เก็บของ สร้างพื้นที่ และพูดคุยกับชาวเกาะ ??????: เกม Life Simulation ???????????????: เล่นแบบสบาย ๆ โดยเก็บทรัพยากร ตกปลา จับแมลง ตกแต่งเกาะ และทำกิจกรรมประจำวัน ??????????: Nintendo Switch Zone |
| อยากซื้อคีย์บอร์ดจากศูนย์ | `pipeline:category_rule_fast_path`: ยังไม่พบข้อมูลว่าศูนย์มีบริการขายคีย์บอร์ดเกมมิ่งในฐานข้อมูลที่มี ข้อมูลอุปกรณ์ที่มีเป็นรายการอุปกรณ์สำหรับใช้งานภายในศูนย์ เช่น Gaming Keyboard, Gaming Mouse, Gaming Headset และ Gaming PC | `pipeline:experimental_rag_direct_fallback`: โหมดทดลอง RAG: ข้อมูลที่ใกล้กับคำถามที่สุดคือ VALORANT: ภาพรวมเอกสาร |

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

- strict: `pipeline:rag_direct_curated` / events_news/news_lookup
- experimental: `pipeline:rag_direct_curated` / events_news/news_lookup

PSU Phuket VALORANT 2026 Tournament จัดขึ้นเมื่อวันที่ 21 กุมภาพันธ์ 2569 โดยเป็นการแข่งขันเกม VALORANT ณ PSU Esports Studio - Phuket
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

### มีคอร์สสอนเล่น Valorant ไหม

- strict: `pipeline:guard_no_answer` / no_answer/guard_no_answer
- experimental: `pipeline:experimental_soft_related_fallback` / no_answer/guard_no_answer

โหมดทดลอง RAG: ข้อมูลที่ยืนยันได้คือ VALORANT มีให้เล่นใน PC Zone และเป็นเกม Tactical FPS แบบทีม 5v5
แต่ยังไม่มีข้อมูลยืนยันว่าศูนย์มีคอร์สสอนเล่น VALORANT หรือคอร์สฝึกเฉพาะเกมในฐานข้อมูลที่มีครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### ถ้าอยากพาเพื่อนไปเล่นเกมสนุก ๆ ควรเลือกอะไร

- strict: `pipeline:related_guidance_fast_path` / equipment/related_guidance
- experimental: `pipeline:experimental_rag_direct_fallback` / equipment/related_guidance

โหมดทดลอง RAG: ข้อมูลที่ใกล้กับคำถามที่สุดคือ Arena of Valor (RoV): 4. ระเบียบและกติกาการแข่งขัน
4. ระเบียบและกติกาการแข่งขัน 4.1. กติกาพื้นฐาน 4.1.1.ห้ามใช้ชื่อตัวละครหรือคําพูดที่เป็นการหยาบคายหรือเสียดสีผู้อื่น 4.1.2.ในเกมแรก ทีมที่อยู่ทางด้านบนของสายการแข่งขันจะได้อยู่ฝ่ายสีน้ำเงิน และในเกมถัดไป ผู้ที่แพ้ในเกมก่อนหน้าจะได้สิทธิ์ในการเลือกฝั่ง 4.1.3.กรรมการจะเป็นผู้แจ้งหมายเลขห้อง เพื่อให้ผู้เข้าแข่งขันทั้งสองทีมเข้าห้องตามหมายเลขที่กำหนดไว้ * ฝ่ายทีมสีฟ้าอยู่ด้านบน * ฝ่ายทีมสีเเดงอยู่ข้างล่าง 4.1.4.หากเริ่มการแข่งขันช้าเกินกว่าเวลาที่กำหนดไว้ 15 นาที ฝ่ายที่ล่าช้าจะถูกปรับแพ้จากการแข่งขันทันที 4.2. กติกาการแข่งขัน 4.2.1.ผู้เข้าแข่งขันทุกคนต้องมีฮีโร่อย่างน้อย 18 ตัว สำหรับการเข้าแข่งขันในโหมด “การแข่งขัน 5v5” (ชื่อเดิม Tournament Mod...

หมายเหตุ: คำตอบนี้เป็นการดึงข้อมูลใกล้เคียงแทน no-answer จึงควรตรวจแหล่งข้อมูลประกอบก่อนใช้เป็นคำตอบยืนยัน
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men, https://esports.phuket.psu.ac.th/Services/our-games

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
- experimental: `pipeline:rag_direct_curated` / games/game_availability_lookup

Animal Crossing: New Horizons: Animal Crossing: New Horizons คือเกมใช้ชีวิตบนเกาะ ผู้เล่นตกแต่งบ้าน เก็บของ สร้างพื้นที่ และพูดคุยกับชาวเกาะ ??????: เกม Life Simulation ???????????????: เล่นแบบสบาย ๆ โดยเก็บทรัพยากร ตกปลา จับแมลง ตกแต่งเกาะ และทำกิจกรรมประจำวัน ??????????: Nintendo Switch Zone
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games, https://esports.computing.psu.ac.th/reservation

### อยากซื้อคีย์บอร์ดจากศูนย์

- strict: `pipeline:category_rule_fast_path` / general/unknown_domain_query
- experimental: `pipeline:experimental_rag_direct_fallback` / general/unknown_domain_query

โหมดทดลอง RAG: ข้อมูลที่ใกล้กับคำถามที่สุดคือ VALORANT: ภาพรวมเอกสาร
กฎระเบียบและรูปแบบการแข่งขัน VALORANT รายการ PSU Phuket VALORANT 2026 Tournament Update: 17/02/2026 English below อุปกรณ์และอุปกรณ์ต่อพ่วง ในการแข่งขันแบบ LAN ผู้เล่นต้องปฏิบัติตามข้อกำหนดเรื่องอุปกรณ์อย่างเคร่งครัดเพื่อความเท่าเทียม * อุปกรณ์ที่นำมาเองได้ คีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) * อุปกรณ์ที่ผู้จัดจัดเตรียมให้ ผู้จัดจะจัดเตรียม PC, จอภาพ, หูฟังพร้อมไมโครโฟน, โต๊ะ และเก้าอี้ให้ * เทคโนโลยีคีย์บอร์ด อนุญาตให้ใช้ Snap Tap, SOCD หรือเทคโนโลยีที่เทียบเท่าได้ เว้นแต่เจ้าหน้าที่จะสั่งเป็นอย่างอื่น * ข้อห้ามสำคัญ * ห้ามใช้มาโคร (Macros) ทั้งที่...

หมายเหตุ: คำตอบนี้เป็นการดึงข้อมูลใกล้เคียงแทน no-answer จึงควรตรวจแหล่งข้อมูลประกอบก่อนใช้เป็นคำตอบยืนยัน
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026, local://competition_rules/competition_rules_cs2_psu_phuket_2026
