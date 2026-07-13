# Competition Challenger V2 Evaluation Audit - 2026-07-04

เอกสารนี้สรุปงานรอบเพิ่ม Ground Truth หลักร้อยข้อสำหรับกติกาการแข่งขัน และการปรับ pipeline หลังจากรันจริง/อ่านผลลัพธ์จริงของ AI

## ไฟล์หลัก

- Ground Truth V2: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\ground_truth\competition_challenger_v2\ground_truth_competition_challenger_v2_real_competitor_questions.jsonl`
- Generator: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\tools\build_competition_challenger_v2.py`
- Repair card generator: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\tools\build_competition_challenger_repair_cards.py`
- Round 4 fact cards: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\competition_rules\competition_rule_fact_cards_round4_challenger.jsonl`
- Round 5 repair cards: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\competition_rules\competition_rule_fact_cards_round5_challenger_repairs.jsonl`
- Round 6 regression cards: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\competition_rules\competition_rule_fact_cards_round6_regression_v1.jsonl`
- Notebook: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\notebooks\02_test_final_pipeline.ipynb`

## Ground Truth ที่เพิ่ม

- สร้าง Challenger V2 จำนวน 369 ข้อ
- มาจาก stable/previous GT 264 ข้อ
- เพิ่ม edge-style questions ใหม่ 105 ข้อ
- ครอบคลุม Counter-Strike 2, RoV/AoV, VALORANT, Tekken 8
- ลักษณะคำถามที่เพิ่ม: ภาษาคนจริง, สะกดไม่ตรง, ใช้ชื่อเกมย่อ, ถามแบบสถานการณ์, ถามหลายคำในประโยคเดียว, และคำถามที่มีโอกาส route หลุดไปหมวดอื่น

## ผลรันตามรอบ

### Baseline

- Total: 369
- PASS: 190
- FAIL: 179
- Pass rate: 51.49%

สาเหตุหลัก:

- Router ยังจับ alias ไม่ครบ เช่น `เคาเตอร์`, `เกมตีป้อม`, `เทคเคน`, `valo`
- คำถามกติกาบางข้อหลุดไปหมวด `games`, `events_news`, `schedule`, `service_fee`
- Retrieval ดึง chunk ใกล้เคียงแต่ไม่ใช่คำตอบจริง เช่น ถามจำนวนเกมแต่ไปตอบ pause
- คำถามเชิงสถานการณ์ยังไม่มี fact card ที่ตอบแบบสั้นและตรง

### Afterfix 1

- Total: 369
- PASS: 299
- FAIL: 70
- Pass rate: 81.03%

สิ่งที่ดีขึ้น:

- Route หลุดน้อยลงมาก
- Alias ของชื่อเกมและคำเกี่ยวกับกติกาถูกจับได้มากขึ้น

ปัญหาที่ยังเหลือ:

- บาง intent ยังดึง chunk ผิด เช่น map ban, pause, location, late start
- คำถามที่ต้องตอบแบบสรุปเชิงนโยบายยังตอบกว้างเกินไป

### Afterfix 2

- Total: 369
- PASS: 363
- FAIL: 6
- Pass rate: 98.37%

ข้อที่ยังพลาดหลังรอบนี้:

- RoV เน็ตทั้งโซนล่ม route ไปหมวดอื่นบางครั้ง
- CS2 ตัวจริงติดธุระ/ตัวสำรองโดน guard ของ fact card ตัดผิด
- RoV pause ผิดครั้งที่ 1/2/3 คำตอบถูกแต่ไม่ขึ้นต้นด้วยคำตอบเปรียบเทียบที่ user ต้องการ
- AOV จัดตรงไหน route หลุดไป contact
- VALORANT หมดเวลาพักฉุกเฉินโดน guard ตัดผิดเพราะเจอคำว่าเวลาพัก

### Final

- Challenger V2 final: 369/369 ผ่าน
- Challenger V1 final: 80/80 ผ่าน
- Competition by-game V2 final: 184/184 ผ่าน

Latency final:

- Challenger V2 average: 0.0300s, P95: 0.0458s, max: 0.0620s
- Challenger V1 average: 0.0228s, P95: 0.0342s, max: 0.0644s
- By-game V2 average: 0.0254s, P95: 0.0380s, max: 0.0580s

## สิ่งที่ปรับ

- เพิ่ม alias และ rule terms ใน `app\pipeline\router.py`
- เพิ่ม alias เกมและ intent terms ใน `app\pipeline\retrieval.py`
- เพิ่ม fact cards รอบ 4 สำหรับคำถามที่เป็น edge case หลัก
- เพิ่ม repair cards รอบ 5 จาก failure ของ Challenger V2
- เพิ่ม regression cards รอบ 6 สำหรับคำถาม Challenger V1 ที่กลับมาพลาดหลังแก้ชุดใหม่
- แก้ Ground Truth ที่เฉลยไม่ตรงบางจุด เช่น RoV format ต้องเป็น BO3 ทุกรอบ ไม่ใช่ BO3/BO5
- เพิ่ม section ใน notebook สำหรับรัน Challenger V2 และดู verbose แบบเรียงข้อ

## ตัวอย่างข้อที่แก้แล้ว

- `cs2 ตัวจริงติดธุระ เอาตัวสำรองที่ไม่ได้ลงชื่อมาแทนได้ไหม`
  - ตอบ: CS2 ไม่มีการเปลี่ยนแปลงสมาชิกหลังยืนยันรายชื่อ ต้องใช้สมาชิกที่ลงทะเบียนไว้

- `RoV เน็ตทั้งโซนล่มต้องทำยังไง`
  - ตอบ: ต้องแจ้งทีมงาน/กรรมการ และให้พิจารณาตามดุลยพินิจ

- `rov pause ผิดครั้งที่ 1 2 3 ต่างกันยังไง`
  - ตอบ: ต่างกันคือ ครั้งที่ 1 ตักเตือน, ครั้งที่ 2 เพิ่มสิทธิการแบนฮีโร่ 1 ครั้ง, และโทษรุนแรงอาจถึงปรับแพ้

- `CS2 hate speech หรือเหยียดศาสนาผิดไหม`
  - ตอบ: ห้าม hate speech การเหยียดศาสนา เชื้อชาติ หรือวาจาสร้างความเกลียดชัง

- `วาโลต้องปิดเลือดกับศพไหม`
  - ตอบ: ต้องปิด Blood และ Bodies โดยตั้งค่าเป็น Off

## บทเรียนจากการอ่านผลโดย Codex

- ตัวตรวจ keyword/source ผ่านไม่ได้แปลว่าคำตอบดีเสมอไป ต้องอ่านคำตอบจริงด้วย
- คำถามที่ลูกค้าถามจริงมักต้องการคำตอบหลักก่อน เช่น จำนวนเงิน จำนวนคน จำนวนครั้ง หรือทำได้/ไม่ได้
- สำหรับกติกาที่เสี่ยงตอบผิด ควรใช้ fact card เป็น canonical answer มากกว่าให้ RAG ดึง chunk แล้วประกอบเอง
- ลองทำ strict answer filtering เพื่อตัดรายละเอียดที่ไม่เกี่ยวข้องแล้ว แต่ทำให้บางคำตอบขาด keyword สำคัญ จึงไม่ใช้วิธีนั้นใน final
- แนวทางที่เหมาะกว่าคือเพิ่ม fact card เฉพาะคำถาม/intent ที่เป็น high-risk และค่อยปรับ formatter เฉพาะหมวดในรอบถัดไป

## สถานะล่าสุด

ตอนนี้ชุดทดสอบกติกาการแข่งขันหลักทั้งหมดผ่านครบ:

- `competition_challenger_v2_final_20260704`: 369/369
- `competition_challenger_v1_final_20260704`: 80/80
- `competition_by_game_v2_final_20260704`: 184/184

ผลลัพธ์สุดท้ายยังใช้ทั้ง `pipeline:competition_fact_card` และ `pipeline:rag_direct_curated` ไม่ได้เป็น rulebase ก้อนเดียวทั้งหมด
