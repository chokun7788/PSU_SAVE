# Normalization / Alias Intent Routing - 2026-07-06

## สรุป

เพิ่มชุด Normalization / Alias Dictionary และ route priority เพื่อให้คำถามภาษาพูด/พิมพ์ผิดเข้า intent ที่ถูกก่อนถึง RAG โดยเฉพาะเคสที่ผู้ใช้ลองถามแล้วคำตอบหลุดไป context ผิด

รอบนี้ไม่ได้รัน Ground Truth ตามคำสั่งผู้ใช้ ใช้เฉพาะ compile, validate, smoke และ ad hoc จากคำถามจริงที่ผู้ใช้ส่งมา

## ปัญหาที่แก้

คำถามจริงที่พบปัญหา:

- `ถ้าใช้บัตรนักศึกษาจะเล่นฟรีใช่ไหม`
- `ไม่มีบัตรนักศึกษาทำยังไง สำหรับตอนจอง`
- `รายกรแข่งมีอะไรบ้าง`
- `จองขั้นที่2ทำยังไง`
- `สอนเล่น RoV หน่อย`
- `ROV แข่งชนะได้เงินเท่าไหร่`
- `รายการแข่งมีอะไรบ้าง`
- `มีคอมให้เล่นไหม`
- `เอาของกินเข้าไปกินได้ไมห`

ปัญหาเดิม:

- คำถามนักศึกษา/ฟรีถูกตีเป็น game availability
- `รายกรแข่ง` และ `รายการแข่งมีอะไรบ้าง` ถูกตีเป็นข่าว Tekken
- `จองขั้นที่2` ตอบขั้นตอนจองทั้งหมด ไม่ตอบเฉพาะขั้นที่ 2
- `ROV แข่งชนะได้เงินเท่าไหร่` ดึงกติกา pause มาตอบ ทั้งที่ถามเงินรางวัล
- `มีคอมให้เล่นไหม` และ `เอาของกินเข้าไปกินได้ไมห` ตกไป experimental RAG แล้วดึงกติกา VALORANT

## สิ่งที่เพิ่ม

### 1. Normalization / Alias

เพิ่มคำแทนและคำพิมพ์ผิด เช่น:

- `รายกร` -> `รายการ`
- `ไมห` / `ใหม` -> `ไหม`
- `ของกิน` / `ข้าว` -> `อาหาร`
- `บัตรนศ` / `นศ.` -> `บัตรนักศึกษา` / `นักศึกษา`
- `วันจัน` -> `วันจันทร์`
- `สเตป` / `step` -> `ขั้น`
- `พีซี` -> `pc`
- `คอมฯ` / `เครื่องคอม` -> `คอม`
- `ชนะได้เงิน` -> `ชนะได้เงินรางวัล`

ไฟล์:

- `app/core/normalization.py`

### 2. Intent Routing

เพิ่ม route เฉพาะ:

- student/free service fee -> `service_fee/service_fee_query`
- PC availability -> `equipment/pc_availability`
- competition prize unknown -> `no_answer/competition_prize_unknown`
- competition game list phrase แบบไม่มีคำว่า `เกม` เช่น `รายการแข่งมีอะไรบ้าง`
- food/rules alias จาก `ของกิน`

ไฟล์:

- `app/pipeline/router.py`

### 3. Fast Path / Rule Answers

เพิ่มหรือปรับคำตอบ:

- คำถามบัตรนักศึกษา/เล่นฟรี ตอบว่าไม่ใช่ทุกบัตรนักศึกษาจะฟรี และแยกกลุ่ม PSU Student and Staff, General Student, General Adult
- ไม่มีบัตรนักศึกษาตอนจอง ตอบว่าใช้ Student ID/Staff ID/National ID ตามระบบรองรับ
- จองขั้นที่ 1-5 ตอบเฉพาะขั้นที่ถาม
- PC availability ตอบว่ามี PC Zone พร้อมอุปกรณ์และเกมที่ยืนยันได้
- เงินรางวัลการแข่งขัน ถ้าไม่มีข้อมูลจริงให้ตอบ no-answer เฉพาะเรื่องเงินรางวัล
- คอร์สสอนเล่นเกม ปรับ wording ให้นุ่มขึ้นและโยงเกมเฉพาะ เช่น RoV / VALORANT

ไฟล์:

- `app/runtime/fast_answer.py`
- `data/rules/no_answer_rules.jsonl`

## ผล ad hoc หลังแก้

| Question | Mode | First line |
|---|---|---|
| ถ้าใช้บัตรนักศึกษาจะเล่นฟรีใช่ไหม | `pipeline:deterministic_calculator_fast` | ไม่ใช่ทุกบัตรนักศึกษาจะเล่นฟรีครับ ต้องดูว่าเป็นกลุ่มผู้ใช้แบบไหน |
| ไม่มีบัตรนักศึกษาทำยังไง สำหรับตอนจอง | `pipeline:booking_identity_fast_path` | ตอนจองไม่จำเป็นต้องมีเฉพาะบัตรนักศึกษาอย่างเดียวครับ |
| รายกรแข่งมีอะไรบ้าง | `pipeline:competition_game_list_fast_path` | เกม/รายการแข่งขันที่มีข้อมูลกติกาในฐานข้อมูลตอนนี้: |
| จองขั้นที่2ทำยังไง | `pipeline:booking_step_fast_path` | ขั้นที่ 2 คือเลือกวันและรอบเวลาที่ต้องการเข้าใช้บริการจากรอบที่ระบบเปิดให้จอง |
| สอนเล่น RoV หน่อย | `pipeline:category_rule_fast_path` | ยังไม่พบข้อมูลยืนยันว่าศูนย์มีคอร์สสอนเล่นเกมหรือบริการโค้ชส่วนตัวครับ |
| ROV แข่งชนะได้เงินเท่าไหร่ | `pipeline:category_rule_fast_path` | ยังไม่พบข้อมูลเงินรางวัลหรือจำนวนเงินที่ผู้ชนะจะได้รับในฐานข้อมูลที่ยืนยันได้ |
| รายการแข่งมีอะไรบ้าง | `pipeline:competition_game_list_fast_path` | เกม/รายการแข่งขันที่มีข้อมูลกติกาในฐานข้อมูลตอนนี้: |
| มีคอมให้เล่นไหม | `pipeline:pc_availability_fast_path` | มีครับ ศูนย์มี PC Zone สำหรับเล่นเกมบนคอมพิวเตอร์ |
| เอาของกินเข้าไปกินได้ไมห | `pipeline:rules_fast_path` | อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น |

## ผลทดสอบ

โฟลเดอร์ 18:

```powershell
python -m py_compile app\core\normalization.py app\pipeline\router.py app\runtime\fast_answer.py
python tools\validate_update.py
python tests\smoke_test_answer_pipeline.py
python tests\smoke_test_fast_runtime.py
```

ผล:

- compile: PASS
- validate_update: PASS
- smoke_test_answer_pipeline: PASS
- smoke_test_fast_runtime: PASS

หมายเหตุ:

- รอบแรก smoke พบ regression ที่ `คอมมีวาโลไหม` ถูก route ไป equipment เพราะ helper `pc_availability` กว้างเกินไป
- แก้โดยไม่ให้ `pc_availability` แย่ง route เมื่อมีชื่อเกมชัดเจน เช่น `วาโล`, `VALORANT`, `CS2`, `PUBG`, `Warzone`, `LoL`, `TEKKEN`
- หลังแก้ smoke ผ่าน

โฟลเดอร์ 20:

```powershell
python -m py_compile app\core\normalization.py app\pipeline\router.py app\runtime\fast_answer.py api\chat.py api\calendar.py api\health.py
```

ผล:

- compile: PASS
- `/api/chat` smoke เฉพาะคำถามสำคัญ 5 ข้อ: PASS

## สถานะหลังจบงาน

- โค้ดในโฟลเดอร์ 18 อัปเดตแล้ว
- ซิงก์ `app` และ `data` ไปโฟลเดอร์ deploy 20 แล้ว
- ยังไม่ได้ deploy production ตามคำสั่งผู้ใช้
- ไม่ได้รัน Ground Truth ตามคำสั่งผู้ใช้
