# Optional PyThaiNLP Normalization - 2026-07-06

## สรุป

เพิ่ม PyThaiNLP เป็น optional helper สำหรับช่วย normalization ภาษาไทยในอนาคต โดยยังคง alias dictionary/manual rules เป็นแกนหลักของระบบ

เหตุผลที่ทำเป็น optional:

- PyThaiNLP ช่วย tokenize/spell suggestion ภาษาไทยได้
- แต่การเปิด spell correction อัตโนมัติอาจแก้ชื่อเฉพาะผิด เช่น RoV, PS5, CS2, VALORANT, TEKKEN, VR, PC
- ตอนทดสอบแบบติดตั้งจริง PyThaiNLP 5.3.4 มี cold start ประมาณ 56 วินาทีในรอบแรก จึงไม่ควรเปิดเป็นค่าเริ่มต้นบน production API

ดังนั้นค่าเริ่มต้นคือปิดไว้ และเปิดได้ด้วย environment variable:

```text
PSU_ENABLE_PYTHAINLP=1
```

## ไฟล์ที่เพิ่ม/แก้

- `app/core/thai_nlp.py`
- `app/core/normalization.py`
- `20_PSU_Esports_Vercel_Deploy/requirements.txt`

## พฤติกรรม

ถ้าไม่มี PyThaiNLP หรือไม่ได้เปิด `PSU_ENABLE_PYTHAINLP=1`:

- ระบบใช้ normalization/manual alias เดิม
- ไม่มี import PyThaiNLP ระหว่าง runtime
- API ไม่เสียเวลา cold start จาก PyThaiNLP

ถ้าเปิด `PSU_ENABLE_PYTHAINLP=1` และติดตั้ง package แล้ว:

- ใช้ `pythainlp.tokenize.word_tokenize`
- ใช้ `pythainlp.spell.correct`
- รับ correction เฉพาะคำที่อยู่ใน safe target list เช่น `ไหม`, `รายการ`, `อาหาร`, `นักศึกษา`, `จอง`, `ราคา`, `กติกา`
- skip คำที่เป็นชื่อเฉพาะหรือโดเมน เช่น `RoV`, `AOV`, `VALORANT`, `CS2`, `TEKKEN`, `PS5`, `VR`, `PC`, `PSU`

## Dependency

เพิ่มในโฟลเดอร์ deploy 20:

```text
pythainlp>=4.0,<6
```

หมายเหตุ: โฟลเดอร์ 18 ไม่มี `requirements.txt` หลักอยู่เดิม จึงเพิ่ม dependency เฉพาะ deploy folder ที่ใช้ Vercel

## ผลทดสอบ

โฟลเดอร์ 18:

```powershell
python -m py_compile app\core\thai_nlp.py app\core\normalization.py app\pipeline\router.py app\runtime\fast_answer.py
python tools\validate_update.py
python tests\smoke_test_answer_pipeline.py
python tests\smoke_test_fast_runtime.py
```

ผล:

- compile: PASS
- validate_update: PASS
- smoke_test_answer_pipeline: PASS
- smoke_test_fast_runtime: PASS

ทดสอบแบบติดตั้ง PyThaiNLP ลง temporary target:

```powershell
python -m pip install --target work\pythainlp_test_deps "pythainlp>=4.0,<6"
```

ผล:

- ติดตั้งได้ PyThaiNLP 5.3.4
- เมื่อเปิด path และใช้ PyThaiNLP จริง ระบบยังตอบเคสสำคัญได้ถูก
- พบ cold start หนัก จึงตั้ง default เป็น off

โฟลเดอร์ 20:

```powershell
python -m py_compile app\core\thai_nlp.py app\core\normalization.py app\pipeline\router.py app\runtime\fast_answer.py api\chat.py api\calendar.py api\health.py
```

ผล:

- compile: PASS
- `/api/chat` smoke จากไฟล์ UTF-8: PASS
- `pythainlp_enabled_default`: `False`

## สถานะ

- โค้ดในโฟลเดอร์ 18 อัปเดตแล้ว
- ซิงก์ `app` และ `data` ไปโฟลเดอร์ deploy 20 แล้ว
- เพิ่ม dependency ใน `20_PSU_Esports_Vercel_Deploy/requirements.txt`
- ยังไม่ได้ deploy production
- ไม่ได้รัน Ground Truth ตามคำสั่งผู้ใช้

## คำแนะนำ

ตอนนี้ควรใช้ manual alias + priority router เป็นหลักต่อไป

ถ้าจะลอง PyThaiNLP บน production จริง ให้เปิด `PSU_ENABLE_PYTHAINLP=1` ชั่วคราวแล้วสังเกต latency ก่อน ถ้าช้าหรือ timeout ให้ปิดกลับทันที
