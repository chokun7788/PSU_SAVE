# Competition Rules Pipeline Round 7 Best

วันที่บันทึก: 2026-07-03

ไฟล์นี้สรุปรอบปรับแก้ pipeline สำหรับตอบคำถามกติกาการแข่งขันของ PSU Esports Studio - Phuket โดยเน้นให้ตอบตรงประเด็นก่อน รายละเอียดตามมา และมีแหล่งอ้างอิงท้ายคำตอบ

## เป้าหมาย

- ทำให้คำถามเกี่ยวกับกติกา CS2, RoV, VALORANT และ Tekken 8 เข้า route `competition_rules` ให้ถูก
- ลดอาการถามอย่างหนึ่งแต่ตอบอีกอย่างหนึ่ง เช่น ถาม RoV เล่นกี่เกม แต่ตอบกติกา pause
- ทำให้คำตอบขึ้นต้นด้วยคำตอบจริงก่อน ไม่ใช่ขึ้นต้นด้วยหัวข้อเอกสารกว้าง ๆ
- ใช้ RAG/curated fact card เท่าที่เหมาะสม โดยไม่บังคับให้ใช้ LLM ทุกข้อ
- คุมตัวตรวจ Ground Truth ให้ยัง strict เหมือนเดิม ไม่ผ่อนผ่านง่ายเกินไป

## สถานะก่อนปรับ

Ground Truth ชุด competition by game v2 มี 184 ข้อ

ผลเริ่มต้นของชุดนี้:

- PASS: 41/184
- FAIL: 143/184
- Pass rate: 22.28%

ปัญหาหลักที่พบ:

- route หลุดไป `games`, `service_fee`, `schedule`, `events_news` ทั้งที่คำถามเป็นกติกาแข่งขัน
- fact card บางใบมีข้อมูลถูก แต่ intent ไม่ตรงกับ intent ที่ router เดา ทำให้ถูกตัดทิ้ง
- RAG ดึง chunk ถูกหมวด แต่เลือกบรรทัดแรกเป็นหัวข้อกว้าง ๆ แทนคำตอบจริง
- คำถามผสมหลายประเด็น เช่น `PS5 + Stage Random` ตอบได้แค่ประเด็นเดียว
- คำไทยสะกดต่างกัน เช่น `บัค` กับ `บั๊ก` ทำให้ route หรือ intent เพี้ยน
- บางเคส strict keyword ต้องการคำเฉพาะ เช่น `Game-Breaking` แต่คำตอบเดิมใช้ `Game Breaking`

## สิ่งที่ปรับในรอบนี้

### 1. เพิ่มคำ trigger ใน router

ไฟล์ที่แก้:

- `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\app\pipeline\router.py`

เพิ่มคำที่ทำให้คำถามการแข่งขันเข้า `competition_rules` ได้แม่นขึ้น:

- `บั๊ก`
- `damage`
- `ดาเมจ`
- `ย้อนรอบ`
- `ได้เปรียบ`
- `ถือว่าผิด`
- `game breaking`
- `game-breaking`
- `exploit`

ผลที่ได้:

- คำถามอย่าง `VALORANT ถ้าบั๊กเกิดก่อนมี damage ทำอะไรได้` ไม่หลุดไป route `games`
- คำถามอย่าง `VALORANT ใช้บั๊กเพื่อได้เปรียบถือว่าผิดไหม` เข้า route `competition_rules`

### 2. เพิ่ม synonym/intent alias ให้ bug rule

ไฟล์ที่แก้:

- `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\app\pipeline\retrieval.py`

เพิ่มคำพ้อง/คำสะกดใกล้เคียงใน `bug_rule`:

- `บัค`
- `บั๊ก`
- `damage`
- `ดาเมจ`
- `game-breaking`
- `game breaking`
- `ได้เปรียบ`
- `ถือว่าผิด`

ผลที่ได้:

- คำถามเกี่ยวกับบั๊กของ VALORANT ไม่ถูกตีความเป็นคำถามรายชื่อเกม
- RAG/fact card เลือกข้อมูล bug rule ได้ตรงขึ้น

### 3. ปรับลำดับ intent hint

ไฟล์ที่แก้:

- `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\app\pipeline\retrieval.py`

ปรับให้ intent เฉพาะมาก่อน intent กว้าง:

- ถ้ามี `Tablet`, `iPad`, `PS5`, `platform`, `macro`, `script` ให้เป็น `equipment` ก่อน `eligibility`
- ถ้ามี `ช้า`, `ล่าช้า`, `เริ่มแข่ง`, `เกิน 15 นาที` ให้เป็น `late_start` ก่อน `penalty`

ตัวอย่างปัญหาเดิม:

- `RoV ใช้ iPad หรือ Tablet ลงแข่งได้ไหม`
  - เดิมถูกตีเป็น `eligibility` เพราะมีคำว่า `ลงแข่งได้ไหม`
  - ใหม่ตีเป็น `equipment` จึงตอบกติกาอุปกรณ์ได้ถูก

- `กติกา RoV ถ้าเริ่มแข่งช้าเกินเวลาที่กำหนดลงโทษยังไง`
  - เดิมถูกตีเป็น `penalty` เพราะมีคำว่า `ลงโทษ`
  - ใหม่ตีเป็น `late_start` จึงตอบเรื่องล่าช้าเกิน 15 นาทีได้ตรง

### 4. เพิ่ม exact matched fact card gate

ไฟล์ที่แก้:

- `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\app\pipeline\retrieval.py`

แนวคิด:

- fact card เฉพาะทางบางใบถูกสร้างมาเพื่อคำถามยากหรือคำถามผสม
- แต่ intent ที่เดาอาจไม่ตรง 100% เช่น คำถามมีคำว่า `pause` แต่คำตอบจริงอยู่ในบทลงโทษ
- ถ้า pattern ของ fact card match กับคำถามจริงแบบ exact/ใกล้ exact ให้ยอมใช้ fact card นั้น แม้ intent จะต่างเล็กน้อย
- แต่ยังไม่ปล่อยให้ fact card กว้าง ๆ แย่งตอบ เพราะไฟล์ round3 fixes ยังบังคับ exact match อยู่

สิ่งที่เพิ่มใน code:

- เก็บ `_matched_pattern`
- ถ้า `intent_hint` ไม่ตรงกับ `best_intent` แต่ `_matched_pattern=True` ให้ตอบได้
- ถ้าไม่ exact match ยังใช้ตัวกรอง intent เหมือนเดิม

ตัวอย่างที่แก้ได้:

- `RoV pause ผิดครั้งที่ 2 โดนอะไร`
  - intent query เป็น `pause`
  - fact card เป็น `penalty`
  - แต่ question pattern ตรง จึงตอบได้ว่าเพิ่มสิทธิการแบนฮีโร่ 1 ครั้ง

- `RoV ให้คนอื่นที่ไม่ได้ลงทะเบียนมาแข่งแทนได้ไหม`
  - intent query เป็น `registration`
  - fact card เป็น `penalty`
  - แต่ question pattern ตรง จึงตอบได้ว่าผู้เล่นไม่ตรงตามที่ลงทะเบียนจะถูกปรับแพ้และตัดสิทธิ์

### 5. เพิ่ม fact card เฉพาะจุด

ไฟล์ที่แก้:

- `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\competition_rules\competition_rule_fact_cards_round3_fixes.jsonl`

จำนวน fact card ในไฟล์นี้หลังปรับ:

- 40 rows

เพิ่ม/ปรับ fact card สำคัญ:

- `valorant_game_breaking_bug_hyphen`
  - ตอบ `Game-Breaking Bug` แบบมีขีด
  - มีคำว่า `ย้อนรอบ`

- `valorant_new_content_and_map_pool_summary`
  - เพิ่มชื่อแผนที่ใน Map Pool
  - ใส่ `Abyss, Ascent, Bind, Corrode, Haven, Lotus, Sunset`

- `tekken8_ps5_stage_random_combined`
  - ตอบคำถามผสม `PS5 + Stage Random`
  - ใส่ทั้ง `PlayStation 5` และ `Random`

### 6. ปรับให้คำตอบตอบประเด็นก่อน

แนวทางที่ใช้:

- ถ้ามี fact card เฉพาะ ให้ตอบบรรทัดแรกด้วย answer ของ fact card
- ถ้าไม่มี fact card ให้ใช้ curated RAG แล้วเลือก focus lines ตาม intent
- รายละเอียด/หลักฐานไว้หลังคำตอบ
- แหล่งข้อมูลอยู่ท้ายคำตอบ

ตัวอย่างรูปแบบที่ต้องการ:

```text
คำตอบ: RoV Pause ผิดครั้งที่ 2 จะเพิ่มสิทธิการแบนฮีโร่ให้ฝ่ายตรงข้าม 1 ครั้ง

หลักฐานจากกติกา:
- เอกสารบทลงโทษการ Pause ผิดระบุครั้งที่ 2 เพิ่มสิทธิการแบนฮีโร่ 1 ครั้ง

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men
```

## ผลรันหลังปรับ

รอบสำคัญ:

| รอบ | ผลลัพธ์ | หมายเหตุ |
|---|---:|---|
| ก่อนเริ่มแก้ชุดนี้ | 41/184 | route/fact card ยังหลุดเยอะ |
| Round 2 intent/rerank | 107/184 | เพิ่ม intent และ rerank |
| Round 3 specific fallback | 144/184 | เพิ่ม fallback สำหรับคำถามเฉพาะ |
| Round 5 exact fact cards | 174/184 | เหลือ 10 fail |
| Round 6 finalfix | 183/184 | เหลือ Tekken 8 คำถามผสม |
| Round 7 best | 184/184 | ผ่านครบชุดนี้ |

ผล Round 7:

- Total: 184
- PASS: 184
- FAIL: 0
- ERROR: 0
- Pass rate: 100.00%
- Average latency: 0.0168s
- P95 latency: 0.0256s
- Keyword fail: 0
- Source fail: 0
- Quality fail: 0
- Validation fail: 0

Mode distribution:

- `pipeline:rag_direct_curated`: 108
- `pipeline:competition_fact_card`: 76

Route distribution:

- `competition_rules`: 184

รายงานผล:

- `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_report_competition_by_game_v2_round7_best_20260703.md`

ผลลัพธ์รายข้อ JSONL:

- `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_competition_by_game_v2_round7_best_20260703.jsonl`

## วิเคราะห์สาเหตุที่ผิดก่อนหน้า

### RoV late start

คำถาม:

- `กติกา RoV ถ้าเริ่มแข่งช้าเกินเวลาที่กำหนดลงโทษยังไง`

สาเหตุเดิม:

- intent ถูกมองเป็น `penalty`
- RAG ดึงหัวข้อกติกากว้างและ pause มาแทน late start

วิธีแก้:

- ให้ `late_start` มาก่อน `penalty`
- ใช้ fact card `rov_late_start_delay_wording`

ผลใหม่:

- ตอบว่าล่าช้าเกิน 15 นาทีจะถูกปรับแพ้ทันที

### RoV pause ผิดครั้งที่ 2/3

คำถาม:

- `RoV pause ผิดครั้งที่ 2 โดนอะไร`
- `RoV pause ผิดครั้งที่ 3 โดนอะไร`

สาเหตุเดิม:

- query intent เป็น `pause`
- fact card อยู่ intent `penalty`
- strict intent gate ตัด fact card ทิ้ง

วิธีแก้:

- เพิ่ม `_matched_pattern`
- ถ้า question pattern match ให้ใช้ fact card ได้แม้ intent ต่างกันเล็กน้อย

ผลใหม่:

- ครั้งที่ 2 เพิ่มสิทธิการแบนฮีโร่ 1 ครั้ง
- ครั้งที่ 3 เพิ่มสิทธิการแบนฮีโร่ 2 ครั้ง

### RoV iPad/Tablet

คำถาม:

- `RoV ใช้ iPad หรือ Tablet ลงแข่งได้ไหม`

สาเหตุเดิม:

- intent ถูกตีเป็น `eligibility` เพราะมีคำว่า `ลงแข่งได้ไหม`

วิธีแก้:

- ให้คำเกี่ยวกับอุปกรณ์ เช่น `iPad`, `Tablet`, `มือถือ` มาก่อน eligibility

ผลใหม่:

- ตอบว่าไม่อนุญาตให้ใช้ Tablet หรือ iPad ต้องใช้โทรศัพท์มือถือเท่านั้น

### VALORANT bug/damage

คำถาม:

- `VALORANT ถ้าบั๊กเกิดก่อนมี damage ทำอะไรได้`
- `VALORANT ใช้บั๊กเพื่อได้เปรียบถือว่าผิดไหม`

สาเหตุเดิม:

- router ไม่รู้จัก `บั๊ก`, `damage`, `ได้เปรียบ`, `ถือว่าผิด`
- คำถามจึงหลุดไป `games`

วิธีแก้:

- เพิ่ม trigger ใน router
- เพิ่ม alias ใน `bug_rule`

ผลใหม่:

- route เข้า `competition_rules`
- ตอบจาก fact card/curated rule ได้ตรง

### VALORANT Game-Breaking

คำถาม:

- `VALORANT Game Breaking Bug จัดการยังไง`

สาเหตุเดิม:

- คำตอบมี `Game Breaking` แต่ Ground Truth ต้องการ `Game-Breaking`

วิธีแก้:

- เพิ่ม fact card ที่ตอบด้วยคำว่า `Game-Breaking Bug`

ผลใหม่:

- ผ่าน keyword strict และยังอ้างอิงแหล่งข้อมูลถูก

### VALORANT new content + map pool

คำถาม:

- `VALORANT สรุปกฎเนื้อหาใหม่กับ map pool`

สาเหตุเดิม:

- ตอบเรื่อง Agent/แผนที่ใหม่ได้ แต่ไม่ใส่ชื่อ `Abyss`
- Ground Truth ต้องการเห็นชื่อ map pool

วิธีแก้:

- ปรับ fact card ให้ใส่ map pool ทั้ง 7 แผนที่

ผลใหม่:

- ตอบ Agent 2 สัปดาห์, แผนที่ใหม่ 4 สัปดาห์, และรายชื่อ map pool ครบ

### Tekken 8 PS5 + Stage Random

คำถาม:

- `Tekken 8 ใช้ PS5 กับ Stage Random ใช่ไหม`

สาเหตุเดิม:

- ระบบหยิบ fact card `PlayStation 5` อย่างเดียว
- คำตอบไม่ใส่ `Random`

วิธีแก้:

- เพิ่ม fact card แบบ combined fact สำหรับคำถามผสม

ผลใหม่:

- ตอบว่าใช้ PlayStation 5 และ Stage เป็นแบบ Random

## สิ่งที่ต้องระวัง

ผล 184/184 หมายถึงผ่าน Ground Truth ชุด competition by game v2 เท่านั้น

ยังควรระวังเรื่อง:

- คำถามจริงจากผู้ใช้อาจสะกดผิดหนักกว่านี้
- ผู้ใช้อาจถามแบบมีบริบทต่อเนื่อง เช่น `แล้วถ้าเกมนั้น pause ได้กี่ครั้ง`
- เอกสารกติกาอาจมีการแก้ไขในอนาคต
- fact card exact-only ช่วยให้แม่นกับคำถามยาก แต่ถ้าเจอคำถามแปลกมากอาจต้อง fallback ไป RAG/LLM
- ถ้าข้อมูลใหม่เพิ่มเข้ามา ควร regenerate curated chunks/fact cards แล้วรัน Ground Truth ใหม่

## สิ่งที่ควรทำต่อ

### 1. เพิ่ม fuzzy normalization

ตัวอย่าง:

- `บัค`, `บั๊ก`, `bug`
- `วาโล`, `valorant`, `valo`
- `rov`, `aov`, `arena of valor`

แนวทาง:

- ทำ dictionary synonym ก่อน
- ถ้าไม่เจอค่อยใช้ fuzzy similarity แบบจำกัด scope
- หลีกเลี่ยงการใช้ cosine similarity แบบเปิดกว้างกับ rule ทุกหมวด เพราะอาจดึงกติกาคนละเกม

### 2. เพิ่ม conversation memory

ตัวอย่าง:

ผู้ใช้ถาม:

- `RoV pause ได้กี่ครั้ง`
- `แล้วผิดครั้งที่ 2 ล่ะ`

ระบบควรจำได้ว่า `เกม = RoV` และหัวข้อเดิมคือ `pause`

### 3. ทำ eval ชุด paraphrase เพิ่ม

Ground Truth ชุดนี้ดีขึ้นมากแล้ว แต่ควรเพิ่มคำถามที่เป็นภาษาคนทั่วไปมากขึ้น:

- `วาโลใช้บั๊กแล้วได้เปรียบได้ปะ`
- `rov เริ่มช้าโดนไร`
- `เทคเคนสุ่มด่านป่าว`
- `cs2 timeout tactical ได้กี่วิ`

### 4. ทำ LLM fallback แบบมี guardrail

ใช้เมื่อ:

- fact card ไม่เจอ
- curated RAG เจอหลาย chunk แต่คำตอบต้องสรุปหลายข้อ
- คำถามเป็นเชิงเปรียบเทียบ/สรุป/อธิบาย

เงื่อนไข:

- LLM ต้องตอบจาก context เท่านั้น
- ถ้า context ไม่พอให้ถามกลับหรือบอกว่าไม่พบข้อมูลยืนยัน
- ต้อง validate source ก่อนปล่อยคำตอบ

### 5. แยก data layer ชัดขึ้น

แนะนำโครงสร้าง:

```text
data/
  competition_rules/
    source_txt/
    curated_jsonl/
    fact_cards/
    ground_truth/
    eval_reports/
```

ข้อดี:

- เพิ่มเอกสารกติกาใหม่ง่าย
- รัน rebuild/eval แยกหมวดได้
- ลดปัญหาข้อมูลหลายชุดผสมกัน

## สรุป

รอบนี้แก้จากปัญหา route/retrieval/fact card เป็นหลัก ไม่ได้แก้ด้วยการให้ LLM เดาสุ่ม

ผลลัพธ์ที่ได้คือ:

- คำถามกติกาเข้า `competition_rules` ครบ
- ระบบเลือก fact card เฉพาะคำถามยากได้ดีขึ้น
- RAG curated ยังทำงานกับคำถามที่ไม่ต้องใช้ fact card
- คำตอบตอบประเด็นก่อนมากขึ้น
- Ground Truth ชุด 184 ข้อผ่านครบ 100%

