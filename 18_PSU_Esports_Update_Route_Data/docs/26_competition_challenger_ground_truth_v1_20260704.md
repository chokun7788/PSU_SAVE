# Competition Challenger Ground Truth V1

วันที่สร้าง: 2026-07-04

ไฟล์นี้สรุป Ground Truth ชุดใหม่สำหรับทดสอบคำถามกติกาการแข่งขันแบบภาษาคนแข่งจริง หรือคำถามที่ไม่ได้อยู่ใน pattern เดิมโดยตรง

## เป้าหมาย

- ทดสอบคำถามที่คนแข่งเกมอาจถามจริง
- ไม่เน้นคำถามเรียบร้อยแบบเอกสารเท่านั้น
- มีคำถามสั้น คำถามผสม คำอังกฤษปนไทย และคำถามสถานการณ์เฉพาะหน้า
- ใช้เป็นชุดหาแผลของระบบ ไม่ใช่ชุดที่ต้องผ่าน 100% ทันที

## ไฟล์ Ground Truth

- `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\ground_truth\competition_challenger_v1\ground_truth_competition_challenger_v1_weird_user_questions.jsonl`

จำนวนข้อทั้งหมด:

- 80 ข้อ

แบ่งตามเกม:

- CS2: 20 ข้อ
- RoV / Arena of Valor: 20 ข้อ
- VALORANT: 25 ข้อ
- Tekken 8: 15 ข้อ

## ลักษณะคำถาม

ตัวอย่าง style:

- `CS2 ปิดรับสมัครแล้วเพิ่มเพื่อนเข้า roster ได้ปะ`
- `rov เลทเกินสิบห้านาทีแพ้เลยไหม`
- `วาโลเปิด Facebook หรือเว็บสื่อสารในคอมแข่งได้ไหม`
- `เทคเคน stage สุ่มหรือเลือกเอง`
- `Tekken ถ้าเสมอ 1-1 ต้องทำไงต่อ`

เหตุผลที่เลือกคำถามแนวนี้:

- ผู้ใช้จริงมักไม่ถามตรงตามหัวข้อเอกสาร
- หลายคำถามใช้คำย่อ เช่น `วาโล`, `rov`, `cs2`
- หลายคำถามใช้คำอังกฤษปนไทย เช่น `timeout`, `stage`, `macro`, `forfeit`, `match fixing`
- บางคำถามถามแบบผสมหลาย fact ในข้อเดียว
- บางคำถามใช้ภาษาไม่เป็นทางการ เช่น `ได้ปะ`, `โดนไร`, `ใช่มั้ย`

## ผลรันครั้งแรก

สคริปต์ที่ใช้:

- `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\tools\run_ground_truth_pipeline_eval.py`

คำสั่งที่ใช้:

```powershell
py -3 tools\run_ground_truth_pipeline_eval.py --ground-truth data\ground_truth\competition_challenger_v1\ground_truth_competition_challenger_v1_weird_user_questions.jsonl --label competition_challenger_v1_weird_user_questions_20260704
```

ผลลัพธ์:

- Total: 80
- PASS: 49
- FAIL: 31
- Pass rate: 61.25%
- Average latency: 0.0180s
- P95 latency: 0.0308s
- Keyword fail: 30
- Source fail: 9
- Quality fail: 0
- Validation fail: 0

ไฟล์รายงาน:

- `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_report_competition_challenger_v1_weird_user_questions_20260704.md`

ไฟล์ผลรายข้อ:

- `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_competition_challenger_v1_weird_user_questions_20260704.jsonl`

## สิ่งที่ผลรันบอกเรา

Route distribution:

- `competition_rules`: 69
- `games`: 4
- `general`: 4
- `events_news`: 2
- `schedule`: 1

แปลว่า:

- ส่วนใหญ่เข้า `competition_rules` ได้แล้ว
- แต่คำถามภาษาคนจริงบางแบบยังหลุดไป route อื่น
- Tekken 8 ภาษาไทย เช่น `เทคเคน` ยังทำให้ route เพี้ยนหลายข้อ
- คำถาม VALORANT บางคำมีคำทั่วไป เช่น `ปิด` ทำให้หลุดไป `schedule`
- บางข้อเข้า route ถูกแล้ว แต่ RAG/fact card เลือกบรรทัดไม่ตรงพอ

## Fail ที่น่าสนใจ

### 1. Route หลุดเพราะคำไทย/คำย่อ

ตัวอย่าง:

- `เทคเคนแข่ง 1v1 หรือเป็นทีม`
- `เทคเคนแต่ละเกมแข่งกี่รอบ`
- `เทคเคนเล่นบน PS5 ใช่ไหม`

ปัญหา:

- route บางข้อหลุดไป `events_news`, `general`, หรือ `games`
- แปลว่า router ยังรู้จัก `Tekken 8` ดี แต่คำว่า `เทคเคน` แบบไทยยังไม่แข็งพอ

แนวทางแก้:

- เพิ่ม alias `เทคเคน`, `เทคเคน 8`, `เทกเคน`
- ให้คำว่า `1v1`, `กี่รอบ`, `stage`, `pause`, `เสมอ 1-1` พาเข้า `competition_rules` เมื่อมีชื่อเกม

### 2. คำถามผสมหลาย fact

ตัวอย่าง:

- `CS2 technical timeout กับ tactical timeout ต่างกันไงแบบสั้นๆ`
- `Tekken สรุปรูปแบบแข่งให้คนไม่เคยแข่งหน่อย`

ปัญหา:

- ระบบอาจตอบ fact เดียว แต่ expected ต้องการหลาย keyword

แนวทางแก้:

- เพิ่ม fact card แบบ combined summary
- หรือให้ RAG รวมหลาย chunk แล้วสรุปด้วย LLM แบบ guardrail

### 3. Fact card กว้างเกิน/เลือก card ผิด

ตัวอย่าง:

- `CS2 toxic ด่าในแชทหรือพูดแรง ๆ โดนอะไร`
  - ไปตอบ format แทน penalty
- `RoV กดหยุดแกล้งคู่แข่งโดนอะไร`
  - ไปตอบ pause policy ปกติ แทน penalty

แนวทางแก้:

- เพิ่ม intent hint สำหรับคำว่า `toxic`, `ด่า`, `พูดแรง`, `แกล้ง`, `ก่อกวน`
- เพิ่ม rerank penalty ให้ดึง penalty chunk ก่อน pause chunk เมื่อคำถามมี `โดนอะไร`

### 4. คำถามที่ใช้คำทั่วไปชนกับ schedule

ตัวอย่าง:

- `วาโลต้องปิดเลือดกับศพไหม`

ปัญหา:

- คำว่า `ปิด` ทำให้หลุดไป schedule/open-close

แนวทางแก้:

- ถ้ามีชื่อเกม + `เลือด`, `ศพ`, `Blood`, `Bodies` ให้เข้า `competition_rules/game_setting` ก่อน schedule

### 5. คำถามที่ถามสถานที่/อาคาร

ตัวอย่าง:

- `RoV แข่งที่อาคารไหนของศูนย์`

ปัญหา:

- มีคำว่า `ศูนย์` แล้ว fact card เลือก pause card แทน location

แนวทางแก้:

- เพิ่ม intent `schedule_location` สำหรับคำว่า `อาคาร`, `ที่ไหน`, `สถานที่`, `แข่งที่`
- เพิ่ม fact card location สำหรับ RoV

## เพิ่มใน Notebook แล้ว

Notebook:

- `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\notebooks\02_test_final_pipeline.ipynb`

เพิ่ม section:

- `15. Ground Truth Challenger V1 - Weird Competitor Questions (80)`
- `16. Challenger V1 - Verbose Item-by-Item`

วิธีใช้:

- Section 15 ใช้รันสรุป PASS/FAIL ทั้งชุด
- Section 16 ใช้ดูเรียงข้อแบบ verbose
- ถ้าต้องการดูครบ 80 ข้อใน verbose ให้ตั้ง:

```python
RUN_LIMIT = None
```

ถ้าต้องการดูเร็ว ๆ ก่อน:

```python
RUN_LIMIT = 20
```

## ควรทำอะไรต่อ

1. ปรับ router ให้รองรับคำไทย/คำสะกดแปลก เช่น `เทคเคน`, `บัค`, `เลท`, `ได้ปะ`
2. เพิ่ม synonym map ก่อนเข้า router/retrieval
3. เพิ่ม fact card สำหรับคำถามผสมที่คนถามบ่อย
4. เพิ่ม rerank rule สำหรับ penalty/location/game_setting
5. รัน Challenger V1 ซ้ำหลังแก้ แล้วเทียบผลกับ baseline 49/80

