# File and Folder Map

ไฟล์นี้คือแผนที่โฟลเดอร์ทั้งหมดที่เกี่ยวกับโปรเจกต์ เพื่อให้แชทใหม่รู้ว่าควรเปิดอะไร

## Root

```text
C:\Users\Chokhun\Downloads\Learn-LLM
```

ไฟล์เรียนรู้พื้นฐาน:

```text
00_เริ่มต้นที่นี่_Roadmap.md
01_พื้นฐานก่อนเริ่ม.md
02_LLM_พื้นฐาน.md
03_Embeddings_และ_Vector_DB.md
04_RAG_พื้นฐาน_Pipeline.md
05_Advanced_RAG.md
06_Evaluation.md
07_Production.md
08_ต่อยอด_Agentic_FineTune_GraphRAG.md
09_ภาษาไทยโดยเฉพาะ.md
10_แหล่งเรียนและโปรเจค.md
```

โฟลเดอร์โปรเจกต์:

```text
11_PSU_Esports_AI_ChatBot
12_PSU_Esports_AI_ChatBot_Full_Pipeline
13_PSU_Esports_AI_ChatBot_Local_vs_API
14_Chatbot_Stakeholder_Questions
15_PSU_Esports_Local_RAG_Qwen3_4B
16_PSU_Esports_RAG_Experiment_Timeline
17_PSU_Esports_Daily_Logs
18_PSU_Esports_Update_Route_Data
19_PSU_Esports_Qwen35_Hybrid_RAG
20_PSU_Esports_Vercel_Deploy
21_PSU_Esports_Handoff_Summary_20260705
```

## โฟลเดอร์ 15

```text
C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B
```

ใช้สำหรับ RAG local รุ่นแรกและ Ground Truth 360

ไฟล์สำคัญ:

```text
ground_truth\ground_truth_v2_360.jsonl
```

ใช้กับ:

```powershell
py -3 tools\run_ground_truth_pipeline_eval.py
```

จากโฟลเดอร์ `18` โดย default tool จะชี้ไปที่ GT360 ในโฟลเดอร์ `15`

## โฟลเดอร์ 17

```text
C:\Users\Chokhun\Downloads\Learn-LLM\17_PSU_Esports_Daily_Logs
```

ใช้บันทึกสิ่งที่ทำแต่ละวัน

ไฟล์สำคัญ:

```text
2026-06-29.md
2026-06-30.md
2026-07-01.md
2026-07-02.md
2026-07-03.md
2026-07-04.md
README.md
```

ไฟล์ `2026-07-04.md` มีรายละเอียดล่าสุดมากที่สุด รวมถึง:

- Web chat
- Vercel deploy
- game/equipment details
- competition rules
- equipment game catalog fix
- production test

## โฟลเดอร์ 18: โฟลเดอร์หลัก

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data
```

โครงสร้าง:

```text
app
assets
data
docs
examples
notebooks
reports
review_ui
tests
tools
web_chat
README.md
NEXT_STEPS.md
```

### app

โค้ดหลักของระบบตอบคำถาม

```text
app\calculator
app\calendar
app\core
app\data_admin
app\pipeline
app\rag
app\review
app\rules
app\runtime
app\web_api
```

ไฟล์สำคัญ:

```text
app\runtime\fast_answer.py
```

มี deterministic answer/fast path จำนวนมาก เช่น:

- schedule
- service fee
- reservation
- games
- equipment
- competition list
- unknown game

```text
app\pipeline\router.py
```

กำหนดว่าจะ route คำถามไปหมวดไหน

```text
app\pipeline\engine.py
```

ควบคุม pipeline หลัก

```text
app\pipeline\retrieval.py
```

curated RAG-lite retrieval

```text
app\pipeline\validator.py
```

ตรวจคำตอบไม่ให้เสี่ยง เช่น ตอบ 24 ชั่วโมงโดยไม่ได้ถาม 24 ชั่วโมง

```text
app\calculator\service_fee.py
```

คำนวณราคาค่าบริการ

```text
app\calendar\service_calendar.py
```

จัดการวันที่ปัจจุบัน วันหยุด วันปิดพิเศษ

```text
app\web_api\server.py
```

local web/API server ที่เปิด `http://127.0.0.1:8018/`

### data

ฐานข้อมูล JSONL และ data ที่ pipeline ใช้

```text
data\calendar
data\competition_rules
data\curated
data\ground_truth
data\human_review
data\logs
data\manifests
data\rules
```

จำนวนไฟล์โดยกลุ่มล่าสุด:

- `calendar`: 1
- `competition_rules`: 8
- `curated`: 7
- `ground_truth`: หลายชุด
- `human_review`: 16
- `logs`: 5
- `rules`: 8

### docs

เอกสาร design และ audit จำนวนมาก

ไฟล์สำคัญ:

```text
docs\09_answer_quality_pipeline.md
docs\10_pipeline_implementation_result.md
docs\11_web_chat_session_memory_pipeline.md
docs\12_web_chat_api_flow.md
docs\13_calendar_holiday_pipeline.md
docs\14_competition_rules_ingestion.md
docs\15_competition_rules_quality_pipeline.md
docs\18_ground_truth_false_pass_and_strict_audit.md
docs\25_competition_pipeline_round7_best_20260703.md
docs\28_competition_challenger_v2_eval_audit_20260704.md
```

หมายเหตุ:

- `docs\23...` และ `docs\24...` ใหญ่มาก เป็น audit item/answer style ของ competition GT
- ถ้าอีกแชทต้องทำงานเร็ว ไม่ต้องอ่านทั้งหมดก่อน ให้เปิดเมื่อเจอปัญหา competition answer

### notebooks

```text
notebooks\02_test_final_pipeline.ipynb
```

โน้ตบุ๊กหลักสำหรับทดสอบถามเองและดู output เช่น:

- คำถาม
- คำตอบจาก AI
- route
- mode
- source
- latency

### reports

เก็บผลรัน ground truth, ad-hoc test, stdout log

ไฟล์ล่าสุดที่สำคัญ:

```text
reports\ad_hoc_pipeline_results_equipment_game_catalog_fix5_source_20260704.md
reports\pipeline_ground_truth_report_gt360_equipment_game_catalog_fix5_source_20260704.md
reports\pipeline_ground_truth_report_competition_challenger_v2_equipment_game_catalog_fix5_source_20260704.md
```

### tools

สคริปต์ช่วย build/test/audit

ไฟล์สำคัญ:

```text
tools\validate_update.py
tools\run_ground_truth_pipeline_eval.py
tools\run_ad_hoc_pipeline_log.py
tools\convert_competition_rules.py
tools\build_competition_ground_truth.py
tools\build_competition_ground_truth_by_game_v2.py
tools\build_competition_challenger_v2.py
tools\audit_competition_v2_item_causes.py
tools\audit_competition_v2_answer_style.py
tools\update_02_test_mixed_modes_notebook.py
```

### web_chat

หน้าเว็บ local MVP

```text
web_chat\index.html
web_chat\app.js
web_chat\styles.css
```

ใช้กับ:

```powershell
py -3 -m app.web_api.server --host 127.0.0.1 --port 8018
```

## โฟลเดอร์ 19

```text
C:\Users\Chokhun\Downloads\Learn-LLM\19_PSU_Esports_Qwen35_Hybrid_RAG
```

สำหรับทดลอง hybrid RAG + Qwen

ไฟล์สำคัญ:

```text
README.md
docs\01_pipeline_design.md
docs\02_model_usage_policy.md
docs\03_current_results_and_next_plan.md
data\unified\unified_knowledge.jsonl
data\index\lexical_index.json
notebooks\02_test_qwen35_hybrid_rag.ipynb
tools\01_build_unified_corpus.py
tools\02_build_lexical_index.py
tools\03_build_vector_index_ollama.py
tools\04_ask_qwen35_hybrid.py
tools\05_compare_models.py
```

สถานะ:

- ใช้ทดลอง ไม่ใช่ production หลัก
- มี lexical index แล้ว
- vector index ผ่าน Ollama เตรียมไว้เป็นแนวทาง

## โฟลเดอร์ 20

```text
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy
```

ไฟล์ deploy:

```text
api\chat.py
api\health.py
index.html
app.js
styles.css
vercel.json
requirements.txt
.python-version
README_DEPLOY.md
```

ไฟล์ code/data ที่ copy มาจาก `18`:

```text
app
data\calendar
data\competition_rules
data\curated
data\rules
```

Production:

```text
https://psu-esports-chatbot.vercel.app
```

## โฟลเดอร์ 21

```text
C:\Users\Chokhun\Downloads\Learn-LLM\21_PSU_Esports_Handoff_Summary_20260705
```

คือ summary handoff นี้

ใช้เมื่อ:

- เปิดแชทใหม่
- ให้ AI ตัวใหม่เข้าใจโปรเจกต์
- ลด token จาก conversation เดิม
- เอาไปทำรายงานฝึกงาน

