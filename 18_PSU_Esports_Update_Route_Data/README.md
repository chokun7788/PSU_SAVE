# PSU Esports Update: Route + Data Layer

โฟลเดอร์นี้เป็นชุด Update สำหรับจัดระเบียบระบบ Chatbot RAG ของ PSU Esports ให้แยกชัดขึ้นระหว่าง `Rule base`, `Calculator`, `RAG`, `LLM`, และ `Human Review`

จุดประสงค์หลักคือทำให้ระบบตอบได้แม่นขึ้นโดยไม่พึ่ง LLM ทุกคำถาม โดยเฉพาะคำถามที่เป็นข้อเท็จจริงตายตัว เช่น เวลาเปิดปิด, กฎการจอง, การเช็คอิน, ค่าบริการ และคำถามที่พิมพ์คนละรูปแบบแต่ความหมายเดียวกัน

## สิ่งที่อยู่ในโฟลเดอร์นี้

- `docs/01_route_pipeline.md` อธิบาย route ว่าคำถามแบบไหนควรเข้า Rule base, Calculator, RAG, LLM หรือ No-answer
- `docs/02_data_architecture.md` อธิบายโครงสร้างข้อมูลและ format JSONL
- `docs/03_human_review_guide.md` แบบให้คนตรวจคำตอบและให้คะแนน
- `docs/04_admin_update_flow.md` วิธีเพิ่มกฎ/ข้อมูลใหม่แบบเป็นขั้นตอน
- `docs/05_question_answer_policy.md` แนวทางตอบคำถามให้สุภาพ ชัด และไม่ตอบมั่ว
- `docs/07_human_review_checker.md` วิธีใช้ไฟล์ตรวจคุณภาพคำตอบด้วยคน หลังจาก auto Ground Truth ผ่านแล้ว
- `docs/08_rulebase_rag_future_design.md` แนวทางแยก Rule base, Calculator, RAG และ LLM สำหรับใช้งานระยะยาว
- `docs/09_answer_quality_pipeline.md` pipeline ละเอียดเพื่อให้ตอบถูก ไม่มั่ว ตรงคำถาม และไม่เวิ่นเว้อ
- `docs/10_pipeline_implementation_result.md` สรุป implementation ล่าสุดของ Answer Quality Pipeline และผล Ground Truth 360/360
- `docs/11_web_chat_session_memory_pipeline.md` pipeline สำหรับเว็บแชท, session memory และ log
- `docs/12_web_chat_api_flow.md` diagram และวิธีรันเว็บแชท MVP ที่เรียก `/api/chat`
- `docs/13_calendar_holiday_pipeline.md` pipeline สำหรับวันที่ปัจจุบัน, วันหยุดราชการ และวันปิดพิเศษ
- `docs/14_competition_rules_ingestion.md` วิธีแปลงไฟล์กติกาการแข่งขันเป็น JSONL และผูกเข้า RAG
- `docs/15_competition_rules_quality_pipeline.md` pipeline แก้คุณภาพคำตอบหมวดกติกาการแข่งขัน
- `docs/17_competition_rules_ground_truth.md` Ground Truth ชุดแยกสำหรับกติกาการแข่งขัน 228 ข้อ
- `app/core/normalization.py` ตัว normalize คำไทย/อังกฤษ, alias, fuzzy เฉพาะ entity
- `app/core/router.py` ตัวอย่าง router สำหรับเลือกว่าจะตอบด้วยทางไหน
- `app/rules/loader.py` และ `app/rules/matcher.py` โหลดและ match rulebase จากหลายไฟล์
- `app/calculator/service_fee.py` ตัวคำนวณ/ตอบราคาค่าบริการจากภาพ Service Fee 2026
- `app/web_api/server.py` local web/API server สำหรับทดสอบ chatbot บนเว็บ
- `web_chat/index.html` หน้าเว็บแชท MVP
- `data/calendar/service_closures.jsonl` ไฟล์วันปิดพิเศษ/วันหยุดที่ใช้ override ตารางปกติ
- `data/competition_rules/*.jsonl` ข้อมูลกติกาการแข่งขันที่แปลงจากไฟล์ `.txt`
- `data/ground_truth/ground_truth_competition_rules_v1_228.jsonl` ชุดคำถาม Ground Truth เฉพาะกติกาการแข่งขัน/รายการแข่ง
- `data/rules/*.jsonl` rulebase ที่ถูกแยกเป็นหมวด
- `data/curated/*.jsonl` curated facts ที่ copy จากโปรเจกต์หลัก
- `data/human_review/*.jsonl` template สำหรับให้คนตรวจ
- `review_ui/index.html` หน้าเว็บสำหรับให้คนกดรีวิวคำตอบ 360 ข้อและ export ผลออกมา
- `tools/validate_update.py` ตรวจ format และ sanity check
- `tests/smoke_test_update.py` ทดสอบพื้นฐานว่า route/calculator ใช้งานได้

## วิธีใช้งานเร็ว

เปิด PowerShell แล้วรัน:

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data"
py -3 tools\validate_update.py
py -3 tests\smoke_test_update.py
py -3 tools\create_human_review_batch.py --limit 120
```

โฟลเดอร์นี้ยังเป็น Update scaffold สำหรับเอาไปผูกกับ notebook/ระบบจริงต่อ ไม่ได้ทับตัว notebook เดิมใน `15_PSU_Esports_Local_RAG_Qwen3_4B`

## Fast Runtime ล่าสุด

เพิ่ม runtime ที่ตอบ FAQ/ราคา/เวลา/กฎ/เกม/อุปกรณ์แบบไม่เรียก LLM:

```powershell
py -3 tests\smoke_test_fast_runtime.py
py -3 tools\run_ground_truth_fast_eval.py --label v2_fast_update_round4_20260701
py -3 tools\create_human_review_markdown.py
py -3 tools\create_review_ui_data.py
```

ผลล่าสุดผ่าน Ground Truth 360/360, average latency ประมาณ 0.0001s

อ่านรายละเอียดที่ `docs/06_fast_runtime_update.md`

ถ้าต้องการเช็คว่าคำตอบ “ตรงเจตนา” และอ่านเป็นธรรมชาติไหม ให้เปิด `data/human_review/human_review_fast_qualityfix_full_360.md` แล้วให้คะแนนทีละข้อ

ถ้าต้องการแบบกดคลิก ให้เปิด `review_ui/index.html`

## Answer Quality Pipeline ล่าสุด

เพิ่ม runtime ใหม่ที่แยกขั้นตอนชัดเจนกว่า fast runtime เดิม:

- preprocess/normalize
- entity extraction
- guard/no-answer
- intent router
- deterministic fast path
- category rule base
- curated RAG fallback
- answer-first formatter
- validator

คำสั่งรัน:

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data"
py -3 tests\smoke_test_answer_pipeline.py
py -3 tools\run_ground_truth_pipeline_eval.py --label quality_pipeline_round4_group_fix_20260701
```

ผลล่าสุด:

- Ground Truth v2: 360/360
- Average latency: ประมาณ 0.0002s
- P95 latency: ประมาณ 0.0004s

รายงานล่าสุด:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_report_quality_pipeline_round4_group_fix_20260701.md
```

อ่านรายละเอียดที่ `docs/10_pipeline_implementation_result.md`

## Web Chat API MVP

เพิ่มหน้าเว็บแชทที่เรียก API เข้า answer pipeline เดิมได้แล้ว โดยใช้ Python standard library ไม่ต้องติดตั้ง FastAPI/Flask เพิ่ม

รัน server:

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data"
py -3 -m app.web_api.server --host 127.0.0.1 --port 8018
```

เปิดเว็บ:

```text
http://127.0.0.1:8018/
```

API:

```text
POST http://127.0.0.1:8018/api/chat
GET  http://127.0.0.1:8018/health
```

ประวัติแชทบนหน้าเว็บเก็บไว้ใน JavaScript memory เท่านั้น ดังนั้นถ้า refresh หรือปิดหน้าเว็บ ประวัติที่แสดงบนหน้าเว็บจะหายและเริ่มใหม่ แต่ backend จะเขียน log แยกไว้ใน `data/logs/` เพื่อ debug และวิเคราะห์คุณภาพคำตอบ

อ่าน flow และ diagram ที่ `docs/12_web_chat_api_flow.md`

## Calendar + Holiday Schedule

เพิ่ม calendar layer สำหรับคำถามเช่น:

```text
วันนี้เปิดไหม
พรุ่งนี้เปิดไหม
28 กรกฎา เปิดไหม
30/7/2026 ศูนย์เปิดรึเปล่า
```

ระบบใช้ timezone `Asia/Bangkok` และอ่านวันปิดพิเศษจาก:

```text
data/calendar/service_closures.jsonl
```

ตอนนี้เพิ่มวันที่ 28-30 กรกฎาคม 2026 เป็นวันปิดให้บริการตาม manual config แล้ว ถ้าตรงกับวันปิดพิเศษ ระบบจะตอบว่าปิดก่อน แม้วันนั้นตามตารางปกติจะเปิด

อ่าน flow และ diagram ที่ `docs/13_calendar_holiday_pipeline.md`

## Competition Rules JSONL

เพิ่มตัวแปลงไฟล์กติกาการแข่งขัน `.txt` เป็น JSONL:

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data"
py -3 tools\convert_competition_rules.py
```

Output:

```text
data/competition_rules/competition_rule_documents.jsonl
data/competition_rules/competition_rule_chunks.jsonl
data/curated/curated_competition_rules.jsonl
```

ตอนนี้มีข้อมูลจาก CS2, RoV, Tekken 8 และ VALORANT รวม 4 เอกสาร 104 chunks และผูกเข้า route `competition_rules` แล้ว

อ่านรายละเอียดที่ `docs/14_competition_rules_ingestion.md`
