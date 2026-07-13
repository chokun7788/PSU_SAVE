# Admin Update Flow

เอกสารนี้เป็นขั้นตอนสำหรับเพิ่มข้อมูลใหม่ เช่น กฎใหม่, ราคาใหม่, ข่าวกิจกรรม, กติกาเกม, หรือข้อมูลการแข่งขัน

## เพิ่มข้อมูลแบบ Curated Fact

ใช้เมื่อเป็นข้อความความรู้หรือข้อมูลประกาศที่ควรให้ RAG ค้นได้

1. เพิ่ม row ใน `data/curated/curated_facts.jsonl` หรือสร้างไฟล์ curated ใหม่
2. ใส่ `id`, `category`, `title`, `text`, `source_url`, `tags`
3. รัน `py -3 tools\validate_update.py`
4. ถ้าใช้ vector DB จริง ให้ rebuild index
5. เพิ่ม ground truth อย่างน้อย 3-5 คำถามต่อ fact ใหม่

## เพิ่ม Rule Base

ใช้เมื่อคำตอบเป็น FAQ ตายตัวและต้องการตอบเร็ว

1. เลือกไฟล์ใน `data/rules/` ตามหมวด
2. เพิ่ม rule พร้อม `patterns`, `answer_th`, `source_ids`, `priority`
3. อย่าใส่ pattern กว้างเกินไป เช่น `จอง` คำเดียว เพราะจะชนหลาย intent
4. รัน smoke test และ ground truth
5. ถ้ามีคำสะกดผิดหรือคำเหมือน ให้เพิ่มใน `app/core/normalization.py` ก่อนเพิ่ม rule ใหม่

## เพิ่มราคา/บริการ

ถ้าเป็นราคาที่ต้องคำนวณ ให้แก้ที่ `app/calculator/service_fee.py` มากกว่าฝังเป็น rulebase เพราะ:

- คำนวณจำนวน session ได้
- แสดงราคาทุกกลุ่มได้เมื่อผู้ใช้ไม่ระบุกลุ่ม
- ตรวจกลุ่มผู้ใช้ได้ชัดกว่า
- ลดโอกาส LLM ตอบราคาผิด

## เพิ่มคำเหมือน

ให้เพิ่มเป็นลำดับ:

1. Exact alias ก่อน เช่น `นักเรียน มอ.` = `psu_student_staff`
2. Normalization เช่น `ม.อ.` -> `มอ`
3. Fuzzy เฉพาะกลุ่ม entity เช่น service/group/day
4. ถ้า ambiguity สูง ให้ใช้ clarify ไม่ใช่บังคับตอบทันที

## ก่อน Deploy ทุกครั้ง

ต้องผ่านขั้นต่ำ:

- `tools/validate_update.py`
- smoke test
- ground truth ล่าสุด
- human review เฉพาะข้อที่เคย fail หรือเสี่ยงสูง
- ตรวจว่า source URL และวันหมดอายุของข้อมูลราคายังถูกต้อง
