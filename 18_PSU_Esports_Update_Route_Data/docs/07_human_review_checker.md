# Human Review Checker

ไฟล์ Ground Truth แบบ auto ใช้เช็คว่า AI มี keyword/source สำคัญครบไหม แต่ยังจับปัญหาเรื่อง “ตอบตรงเจตนาคำถามไหม” ได้ไม่พอ เช่น คำถามถามว่า “ต่างกันเท่าไหร่” แต่ AI ตอบเป็นราคาอย่างเดียว แบบนี้ keyword อาจ PASS แต่ประสบการณ์ใช้งานจริงยังควรแก้

## ไฟล์ที่ควรเปิดตรวจ

- Markdown สำหรับอ่านและให้คะแนน: `data/human_review/human_review_fast_qualityfix_full_360.md`
- JSONL สำหรับเอาไปประมวลผลต่อ: `data/human_review/human_review_fast_qualityfix_full_360.jsonl`
- หน้าเว็บแบบกดคลิก: `review_ui/index.html`

## วิธีสร้างไฟล์ใหม่

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data"
py -3 tools\run_ground_truth_fast_eval.py --label v2_fast_update_human_review_20260701
py -3 tools\create_human_review_markdown.py
py -3 tools\create_review_ui_data.py
```

## วิธีให้คะแนนเร็ว

ให้ดูทีละข้อแล้วกรอกใน Markdown ได้เลย

- `ตรงเจตนาคำถาม 0-4`: ประโยคแรกตอบโจทย์ไหม
- `ความถูกต้อง 0-4`: ตัวเลข เวลา กฎ กลุ่มผู้ใช้ถูกไหม
- `ความครบถ้วน 0-4`: ตอบครบพอไหม
- `น้ำเสียง/อ่านง่าย 0-4`: ลูกค้าทั่วไปอ่านแล้วเข้าใจไหม
- `Route เหมาะไหม 0-4`: ใช้ rule/calculator/RAG/no-answer ถูกไหม

## Decision

- `pass`: ใช้ได้
- `minor_fix`: ถูกแต่ควรเรียงคำตอบ/เพิ่มคำอธิบาย
- `major_fix`: ตอบผิดเจตนา ผิดตัวเลข หรือทำให้เข้าใจผิด
- `needs_data`: ไม่มีข้อมูลจริง
- `needs_policy`: ต้องให้ศูนย์ยืนยัน

## ตัวอย่างการตัดสิน

คำถาม: `ต่างมหาลัยเล่น VR 30 นาที กับ VR 1 ชั่วโมงต่างกันเท่าไหร่`

คำตอบที่ดีควรขึ้นต้นประมาณ:

```text
ต่างกัน 185 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน
- VR 30 นาที ราคา 190 บาท
- VR 1 ชั่วโมง ราคา 375 บาท
```

ถ้าคำตอบบอกแค่ `ราคา 190 บาท` หรือบอกเฉพาะแถวราคาโดยไม่สรุปส่วนต่าง ให้ให้ `minor_fix` หรือ `major_fix` ตามความเสี่ยงของข้อ
