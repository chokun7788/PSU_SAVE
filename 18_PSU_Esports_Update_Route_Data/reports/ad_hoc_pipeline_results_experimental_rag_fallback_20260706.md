# Experimental RAG Fallback Ad Hoc

| Question | Strict | Experimental |
|---|---|---|
| มีให้เช่าจอไปบ้านไหม | `pipeline:guard_no_answer`: ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ | `pipeline:experimental_rag_direct_fallback`: โหมดทดลอง RAG: ข้อมูลที่ใกล้กับคำถามที่สุดคือ Arena of Valor (RoV): 4. ระเบียบและกติกาการแข่งขัน |
| รับซ่อมคอมส่วนตัวไหม | `pipeline:guard_no_answer`: ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ | `pipeline:experimental_rag_direct_fallback`: โหมดทดลอง RAG: ข้อมูลที่ใกล้กับคำถามที่สุดคือ Arena of Valor (RoV): 4. ระเบียบและกติกาการแข่งขัน |
| อยากจัดวันเกิดที่ศูนย์ได้ไหม | `pipeline:rag_direct_curated`: PSU Phuket VALORANT 2026 Tournament จัดขึ้นเมื่อวันที่ 21 กุมภาพันธ์ 2569 โดยเป็นการแข่งขันเกม VALORANT ณ PSU Esports Studio - Phuket | `pipeline:rag_direct_curated`: PSU Phuket VALORANT 2026 Tournament จัดขึ้นเมื่อวันที่ 21 กุมภาพันธ์ 2569 โดยเป็นการแข่งขันเกม VALORANT ณ PSU Esports Studio - Phuket |
| มีคอร์สสอนเล่น Valorant ไหม | `pipeline:guard_no_answer`: ไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ | `pipeline:experimental_rag_direct_fallback`: โหมดทดลอง RAG: ข้อมูลที่ใกล้กับคำถามที่สุดคือ Counter-Strike 2 |
| ถ้าอยากพาเพื่อนไปเล่นเกมสนุก ๆ ควรเลือกอะไร | `pipeline:related_guidance_fast_path`: ถ้าไปกับเพื่อน แนะนำให้เลือกตามสไตล์การเล่น: | `pipeline:related_guidance_fast_path`: ถ้าไปกับเพื่อน แนะนำให้เลือกตามสไตล์การเล่น: |
| เกมแนวฝึกทีมเวิร์คมีอะไรบ้าง | `pipeline:related_guidance_fast_path`: สรุปแนวเกมที่มีข้อมูลยืนยันได้: | `pipeline:related_guidance_fast_path`: สรุปแนวเกมที่มีข้อมูลยืนยันได้: |
| อยากเล่น Pokemon | `pipeline:games_unknown_fast_path`: ยังไม่พบ Pokemon ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ | `pipeline:games_unknown_fast_path`: ยังไม่พบ Pokemon ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ |
| อยากซื้อคีย์บอร์ดจากศูนย์ | `pipeline:category_rule_fast_path`: ยังไม่พบข้อมูลว่าศูนย์มีบริการขายคีย์บอร์ดเกมมิ่งในฐานข้อมูลที่มี ข้อมูลอุปกรณ์ที่มีเป็นรายการอุปกรณ์สำหรับใช้งานภายในศูนย์ เช่น Gaming Keyboard, Gaming Mouse, Gaming Headset และ Gaming PC | `pipeline:category_rule_fast_path`: ยังไม่พบข้อมูลว่าศูนย์มีบริการขายคีย์บอร์ดเกมมิ่งในฐานข้อมูลที่มี ข้อมูลอุปกรณ์ที่มีเป็นรายการอุปกรณ์สำหรับใช้งานภายในศูนย์ เช่น Gaming Keyboard, Gaming Mouse, Gaming Headset และ Gaming PC |

## Details

### มีให้เช่าจอไปบ้านไหม

- strict: `pipeline:guard_no_answer` / no_answer/guard_no_answer
- experimental: `pipeline:experimental_rag_direct_fallback` / no_answer/guard_no_answer

โหมดทดลอง RAG: ข้อมูลที่ใกล้กับคำถามที่สุดคือ Arena of Valor (RoV): 4. ระเบียบและกติกาการแข่งขัน
4.5.1.2. ในกรณีที่เกมหยุดลงอันเนื่องมาจากปัญหาทางเทคนิค โดยมิได้เกิดจากการกระทำของผู้เข้าร่วมการแข่งขัน ทางทีมงานมีสิทธิสั่งให้หยุดพักเกมดังกล่าว และให้ผู้เข้าแข่งขันกลับเข้าสู่การแข่งขันใหม่อีกครั้งภายหลังจากผู้เข้าแข่งขันที่ไม่ได้เชื่อมต่อได้กลับเข้ามาในเกมแล้ว 4.5.2.หากเกมหยุดลงเป็นเวลาเกินกว่า 10 นาที ทางทีมงานมีสิทธิสั่งให้เริ่มเกมใหม่ เว้นแต่ทีมผู้เข้าร่วมแข่งขันทีมใดทีมหนึ่งมีคะแนนมากกว่าอีกทีมเป็นจำนวนมาก ทางทีมงานอาจใช้ดุลยพินิจในการสั่งให้ทีมที่มีคะแนนมากกว่าดังกล่าวเป็นผู้ชนะในเกมที่หยุดลงนั้นตามที่เห็นควร 4.5.3.ภายหลังจากที่เกมเชื่อมต่อแล้ว ทางทีมงานอาจสั่งให้ทีมผู้เข้าแข่งขันทั้งสองทีมเริ่มเกมใหม่โดยเร็ว และ/หรือดำเนินเกมใหม่ต่อไ...

หมายเหตุ: คำตอบนี้เป็นการดึงข้อมูลใกล้เคียงแทน no-answer จึงควรตรวจแหล่งข้อมูลประกอบก่อนใช้เป็นคำตอบยืนยัน
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

### รับซ่อมคอมส่วนตัวไหม

- strict: `pipeline:guard_no_answer` / no_answer/guard_no_answer
- experimental: `pipeline:experimental_rag_direct_fallback` / no_answer/guard_no_answer

โหมดทดลอง RAG: ข้อมูลที่ใกล้กับคำถามที่สุดคือ Arena of Valor (RoV): 4. ระเบียบและกติกาการแข่งขัน
4. ระเบียบและกติกาการแข่งขัน 4.1. กติกาพื้นฐาน 4.1.1.ห้ามใช้ชื่อตัวละครหรือคําพูดที่เป็นการหยาบคายหรือเสียดสีผู้อื่น 4.1.2.ในเกมแรก ทีมที่อยู่ทางด้านบนของสายการแข่งขันจะได้อยู่ฝ่ายสีน้ำเงิน และในเกมถัดไป ผู้ที่แพ้ในเกมก่อนหน้าจะได้สิทธิ์ในการเลือกฝั่ง 4.1.3.กรรมการจะเป็นผู้แจ้งหมายเลขห้อง เพื่อให้ผู้เข้าแข่งขันทั้งสองทีมเข้าห้องตามหมายเลขที่กำหนดไว้ * ฝ่ายทีมสีฟ้าอยู่ด้านบน * ฝ่ายทีมสีเเดงอยู่ข้างล่าง 4.1.4.หากเริ่มการแข่งขันช้าเกินกว่าเวลาที่กำหนดไว้ 15 นาที ฝ่ายที่ล่าช้าจะถูกปรับแพ้จากการแข่งขันทันที 4.2. กติกาการแข่งขัน 4.2.1.ผู้เข้าแข่งขันทุกคนต้องมีฮีโร่อย่างน้อย 18 ตัว สำหรับการเข้าแข่งขันในโหมด “การแข่งขัน 5v5” (ชื่อเดิม Tournament Mod...

หมายเหตุ: คำตอบนี้เป็นการดึงข้อมูลใกล้เคียงแทน no-answer จึงควรตรวจแหล่งข้อมูลประกอบก่อนใช้เป็นคำตอบยืนยัน
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

### อยากจัดวันเกิดที่ศูนย์ได้ไหม

- strict: `pipeline:rag_direct_curated` / events_news/news_lookup
- experimental: `pipeline:rag_direct_curated` / events_news/news_lookup

PSU Phuket VALORANT 2026 Tournament จัดขึ้นเมื่อวันที่ 21 กุมภาพันธ์ 2569 โดยเป็นการแข่งขันเกม VALORANT ณ PSU Esports Studio - Phuket
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

### มีคอร์สสอนเล่น Valorant ไหม

- strict: `pipeline:guard_no_answer` / no_answer/guard_no_answer
- experimental: `pipeline:experimental_rag_direct_fallback` / no_answer/guard_no_answer

โหมดทดลอง RAG: ข้อมูลที่ใกล้กับคำถามที่สุดคือ Counter-Strike 2
Counter-Strike 2: Counter-Strike 2 คือเกมยิงแข่งขันแบบทีมที่แบ่งเป็นฝ่ายบุกและฝ่ายรับ โดยมีเป้าหมายหลักเกี่ยวกับการวาง/กู้ระเบิดหรือจัดการฝ่ายตรงข้าม ??????: เกมยิง Tactical FPS ???????????????: เล่นเป็นรอบ ๆ ต้องซื้ออาวุธ วางแผนกับทีม คุมพื้นที่ และใช้การเล็งกับการสื่อสารเพื่อชนะรอบ ??????????: PC Zone

หมายเหตุ: คำตอบนี้เป็นการดึงข้อมูลใกล้เคียงแทน no-answer จึงควรตรวจแหล่งข้อมูลประกอบก่อนใช้เป็นคำตอบยืนยัน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation, https://esports.phuket.psu.ac.th/Services/our-games

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
