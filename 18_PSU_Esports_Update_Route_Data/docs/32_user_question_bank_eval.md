# User Question Bank Eval

ไฟล์นี้คือชุดทดสอบคำถามจำลองจากผู้ใช้ทั่วไป 400 ข้อ และตัว runner สำหรับยิงคำถามเข้า pipeline ของ chatbot เพื่อดูว่าแต่ละข้อระบบตอบจากอะไร ใช้เวลาเท่าไหร่ และคำตอบออกมาเป็นแบบไหน

## มีคำถามอะไรบ้าง

- `game_rules` 100 ข้อ: เกมและกติกา เช่น ROV, VALORANT, CS2, TEKKEN 8
- `play_booking_controls` 100 ข้อ: วิธีเล่น วิธีจอง ปุ่ม controller และคำถาม follow-up
- `equipment_game_inside` 100 ข้อ: อุปกรณ์ โซนต่างๆ รายชื่อเกม หมวดเกม และข้อมูลข้างในเกม
- `out_of_scope` 100 ข้อ: คำถามนอกโดเมน เพื่อดูว่าระบบจะปฏิเสธ ใช้ LLM หรือหลุดไป RAG ผิดทางไหม

## คำสั่งพื้นฐาน

ถ้าอยากดูแบบรายข้อใน Jupyter ให้เปิด:

```text
notebooks\03_user_question_bank_eval.ipynb
```

ใน notebook สามารถ filter/search คำถาม, run ทีละหมวด, ดูตารางผลลัพธ์ และเปิดคำตอบเต็มด้วย `show_answer("GR-001")`

```powershell
cd C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data

# สร้างไฟล์ bank 400 ข้ออย่างเดียว
python tools\run_user_question_bank_eval.py --export-bank-only

# รันตัวอย่าง 20 ข้อแรก
python tools\run_user_question_bank_eval.py --limit 20

# รันเฉพาะคำถามนอกเรื่อง 20 ข้อ
python tools\run_user_question_bank_eval.py --category out_of_scope --limit 20

# รันคำถามนอกเรื่องโดยเปิด Local LLM fallback
python tools\run_user_question_bank_eval.py --category out_of_scope --limit 20 --allow-llm

# รันครบ 400 ข้อ และแยกโฟลเดอร์ตามหมวด
python tools\run_user_question_bank_eval.py --split-category-dirs --quiet
```

## ไฟล์ผลลัพธ์

หลังรัน ระบบจะสร้างโฟลเดอร์ใน:

```text
data\eval\question_bank_runs\<timestamp>\
```

ถ้าใช้ `--split-category-dirs` จะได้โฟลเดอร์ย่อยตามหมวด:

```text
data\eval\question_bank_runs\<timestamp>_by_category\game_rules\
data\eval\question_bank_runs\<timestamp>_by_category\play_booking_controls\
data\eval\question_bank_runs\<timestamp>_by_category\equipment_game_inside\
data\eval\question_bank_runs\<timestamp>_by_category\out_of_scope\
```

ไฟล์สำคัญ:

- `results.json`: อ่านง่ายที่สุด เป็น JSON list แบบ pretty print สำหรับดูรายข้อ
- `results_by_category.json`: อ่านง่ายแบบแยกหมวดในไฟล์เดียว
- `results.jsonl`: เก็บละเอียดที่สุด เหมาะสำหรับเอาไปวิเคราะห์ต่อ
- `results.csv`: เปิดด้วย Excel ได้
- `report.md`: อ่านง่าย มีคำถาม คำตอบ route strategy source และ latency
- `summary.json`: สรุปจำนวนข้อและจำนวนของแต่ละ strategy

ไฟล์คำถาม 400 ข้อจะอยู่ที่:

```text
data\eval\user_question_bank_400.jsonl
data\eval\user_question_bank_400.json
```

## ความหมาย field สำคัญ

- `mode`: mode ที่ pipeline ตอบกลับ เช่น fast path, vector, hybrid, no answer
- `route`: หมวด/เจตนาที่ router ตีความ
- `strategy`: สรุปแบบอ่านง่ายว่าเป็น `fastpath/rulebase`, `rag/vector`, `rag/hybrid`, `llm`, `no_answer` หรือ `pipeline`
- `sources`: แหล่งข้อมูลหรือ chunk ที่ถูกดึงมาใช้
- `latency_sec`: เวลาที่ pipeline รายงาน
- `wall_sec`: เวลาจริงที่ runner วัดจากเครื่อง
- `answer`: คำตอบที่ระบบตอบจริง

## วิธีไล่ดูปัญหา

เริ่มจากรันทีละหมวดแบบ `--limit 20` ก่อน ถ้าเจอคำตอบผิด ให้เปิด `report.md` แล้วดู 3 อย่างนี้:

1. `route` ตีความถูกหมวดไหม
2. `strategy` ใช้ทางที่ควรใช้ไหม เช่น ปุ่มเกมควรไป RAG/control ไม่ใช่ random game
3. `sources` ดึงข้อมูลตรงกับคำถามไหม

ถ้า route ผิด ให้แก้ router/alias ก่อน ถ้า route ถูกแต่ source ผิด ให้แก้ retrieval หรือข้อมูล split ถ้า source ถูกแต่คำตอบสรุปไม่ดี ให้แก้ prompt/formatter
