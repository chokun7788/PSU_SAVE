# Current Test Results and Reports

ไฟล์นี้สรุปผลทดสอบล่าสุดและ report ที่ควรเปิดดู

## สรุปผลล่าสุด

หลังแก้ equipment game catalog/source ล่าสุด:

```text
GT360: 360/360 PASS
Competition challenger v2: 369/369 PASS
รวม: 729/729 PASS
```

ผล local API และ production API ผ่านคำถาม smoke test แล้ว

## GT360 ล่าสุด

Report:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_report_gt360_equipment_game_catalog_fix5_source_20260704.md
```

JSONL result:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_gt360_equipment_game_catalog_fix5_source_20260704.jsonl
```

stdout log:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\run_stdout_gt360_equipment_game_catalog_fix5_source_20260704.txt
```

Summary:

```text
Total: 360
PASS: 360
FAIL: 0
ERROR: 0
Pass rate: 100.00%
Average latency: 0.0144s
P95 latency: 0.0371s
Keyword fail: 0
Source fail: 0
Quality fail: 0
Validation fail: 0
```

Mode distribution สำคัญ:

```text
pipeline:deterministic_calculator_fast: 139
pipeline:schedule_fast_path: 46
pipeline:guard_no_answer: 25
pipeline:rules_fast_path: 21
pipeline:booking_fast_path: 20
pipeline:games_availability_fast_path: 19
pipeline:equipment_game_catalog_fast_path: 5
```

## Competition Challenger v2 ล่าสุด

Report:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_report_competition_challenger_v2_equipment_game_catalog_fix5_source_20260704.md
```

JSONL result:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_results_competition_challenger_v2_equipment_game_catalog_fix5_source_20260704.jsonl
```

stdout log:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\run_stdout_competition_challenger_v2_equipment_game_catalog_fix5_source_20260704.txt
```

Summary:

```text
Total: 369
PASS: 369
FAIL: 0
ERROR: 0
Pass rate: 100.00%
Average latency: 0.0305s
P95 latency: 0.0479s
Keyword fail: 0
Source fail: 0
Quality fail: 0
Validation fail: 0
```

Mode distribution:

```text
pipeline:competition_fact_card: 237
pipeline:rag_direct_curated: 132
```

## Ad-hoc Test ล่าสุด

คำถามเฉพาะจุด:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\ad_hoc_questions_equipment_game_catalog_fix4_20260704.txt
```

Report:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\ad_hoc_pipeline_results_equipment_game_catalog_fix5_source_20260704.md
```

JSONL:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\ad_hoc_pipeline_results_equipment_game_catalog_fix5_source_20260704.jsonl
```

ชุดคำถาม:

```text
อุปกรณ์เล่นเกมอะไรได้บ้าง
อุปกรณ์มีเกมอะไรบ้าง
เครื่องเล่นอะไรได้บ้าง
เครื่องเล่นเกมอะไรได้บ้าง
อุปกรณ์นี้เล่นไรได้บ้าง
PC Zone เล่นเกมอะไรได้บ้าง
PC Zone มีอุปกรณ์อะไรบ้าง
Cockpit มีเกมอะไรบ้าง
VR มีเกมอะไรบ้าง
PS5 มีเกมอะไรบ้าง
Nintendo Switch มีเกมอะไรบ้าง
คอมมีวาโลไหม
เพลย์ห้ามี tekken 8 หรือเปล่า
Warzone อยู่เครื่อง PC ไหน
Tekken 8 เกมนึงมี 3 rounds ใช่ไหม
tekken 1 ต่อ 1 ในเกมรวมต้องมี decider หรือเปล่า
เล่น Minecraft ได้ไหม
Roblox เล่นได้ไหม
Beat Saber เล่นยังไง
อะไรคือ Cockpit
ตอนนี้มีเกมแข่งอะไรบ้าง
```

Route distribution:

```text
competition_rules/competition_rules_lookup: 2
equipment/equipment_game_catalog: 10
equipment/zone_equipment_lookup: 2
games/competition_game_list: 1
games/game_availability_lookup: 5
games/game_detail_lookup: 1
```

ตัวอย่างที่ผ่าน:

```text
อุปกรณ์เล่นเกมอะไรได้บ้าง
-> equipment/equipment_game_catalog
-> pipeline:equipment_game_catalog_fast_path
```

```text
Cockpit มีเกมอะไรบ้าง
-> equipment/equipment_game_catalog
-> pipeline:equipment_game_catalog_fast_path
```

```text
เล่น Minecraft ได้ไหม
-> games/game_availability_lookup
-> pipeline:games_unknown_fast_path
```

```text
Tekken 8 เกมนึงมี 3 rounds ใช่ไหม
-> competition_rules/competition_rules_lookup
-> pipeline:competition_fact_card
```

## คำสั่งรัน test

ตั้ง encoding PowerShell ก่อนรันภาษาไทย:

```powershell
$env:PYTHONIOENCODING='utf-8'
$OutputEncoding = [System.Text.UTF8Encoding]::new($false)
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
```

Validate data:

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data"
py -3 tools\validate_update.py
```

Compile:

```powershell
py -3 -m py_compile app\runtime\fast_answer.py app\pipeline\router.py app\pipeline\engine.py
```

Run GT360:

```powershell
py -3 tools\run_ground_truth_pipeline_eval.py --label my_gt360_check
```

Run competition challenger v2:

```powershell
py -3 tools\run_ground_truth_pipeline_eval.py --ground-truth data\ground_truth\competition_challenger_v2\ground_truth_competition_challenger_v2_real_competitor_questions.jsonl --label my_comp_challenger_check
```

Run ad-hoc:

```powershell
py -3 tools\run_ad_hoc_pipeline_log.py --label my_adhoc_check --questions-file reports\ad_hoc_questions_equipment_game_catalog_fix4_20260704.txt
```

ถ้าต้องการเก็บ stdout ลงไฟล์เพื่อลด token:

```powershell
py -3 tools\run_ground_truth_pipeline_eval.py --label my_gt360_check *> reports\run_stdout_my_gt360_check.txt
```

## วิธีอ่าน JSONL result

ใน result JSONL แต่ละบรรทัดจะมี:

```text
id
category
question
answer
mode
route_category
route_intent
confidence
verdict
keyword_ok
source_ok
quality_ok
validation_errors
retrieved_ids
trace
```

ใช้ดู:

- route ที่ใช้
- mode ที่ตอบ
- คำตอบจริง
- source ที่ดึงมา
- trace ว่าผ่านขั้นตอนไหน
- ถ้าผิด ดู missing_keywords/source/quality_problems

## ข้อควรระวังเรื่อง PASS

PASS ไม่ได้แปลว่าสมบูรณ์ 100% สำหรับผู้ใช้จริง

เหตุผล:

- Ground Truth ยังตรวจจาก keyword/source/quality rule
- คำตอบอาจถูกแต่สำนวนยังไม่สวย
- บางคำถามจริงนอก pattern อาจยังไม่ครอบคลุม
- ข้อมูลในเว็บอาจเปลี่ยนแล้ว แต่ data local ยังเก่า

ควรทำเพิ่ม:

- human review รอบสุ่ม
- ad-hoc test จากคำถามจริง
- เก็บ log production แล้วเอามาทำ Ground Truth ใหม่

## Production test ล่าสุด

ทดสอบ:

```text
https://psu-esports-chatbot.vercel.app/api/chat
```

คำถามที่ผ่าน:

```text
อุปกรณ์เล่นเกมอะไรได้บ้าง
Cockpit มีเกมอะไรบ้าง
เล่น Minecraft ได้ไหม
Roblox เล่นได้ไหม
ตอนนี้มีเกมแข่งอะไรบ้าง
```

ผล:

- production ใช้โค้ดล่าสุด
- route ตรง
- source เป็น Our Games ในคำถามเกม
- unknown game ไม่มั่ว

