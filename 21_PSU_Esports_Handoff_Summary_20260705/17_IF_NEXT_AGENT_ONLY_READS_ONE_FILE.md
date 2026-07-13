# If Next Agent Only Reads One File

ถ้า AI/Codex ตัวใหม่มีเวลาอ่านแค่ไฟล์เดียว ให้อ่านไฟล์นี้

## Current Mission

ทำ PSU Esports Chatbot ให้ตอบคำถามลูกค้าเกี่ยวกับศูนย์ได้ถูกต้อง เร็ว และไม่มั่ว โดยใช้ข้อมูลจริงจากเว็บ/ไฟล์ของ PSU Esports Studio - Phuket

## Main Paths

```text
Root:
C:\Users\Chokhun\Downloads\Learn-LLM

Main project:
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data

Deploy folder:
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy

Handoff folder:
C:\Users\Chokhun\Downloads\Learn-LLM\21_PSU_Esports_Handoff_Summary_20260705

Production:
https://psu-esports-chatbot.vercel.app
```

## Current System

Production is not LLM-first.

It uses:

```text
rulebase + deterministic calculator + fact cards + curated RAG-lite + guard/no-answer
```

Main files:

```text
app\runtime\fast_answer.py
app\pipeline\router.py
app\pipeline\engine.py
app\pipeline\retrieval.py
app\pipeline\validator.py
app\calculator\service_fee.py
app\calendar\service_calendar.py
```

## Latest Confirmed Tests

```text
GT360: 360/360 PASS
Competition challenger v2: 369/369 PASS
Total: 729/729 PASS
```

Reports:

```text
reports\pipeline_ground_truth_report_gt360_equipment_game_catalog_fix5_source_20260704.md
reports\pipeline_ground_truth_report_competition_challenger_v2_equipment_game_catalog_fix5_source_20260704.md
reports\ad_hoc_pipeline_results_equipment_game_catalog_fix5_source_20260704.md
```

## Latest Important Fix

Problem:

```text
ถาม: อุปกรณ์เล่นเกมอะไรได้บ้าง
ตอบผิด: ยังไม่พบ เกมนี้...
```

Fix:

- Added `equipment_game_catalog`
- Added `pipeline:equipment_game_catalog_fast_path`
- Split equipment game catalog from game availability
- Unknown games like Minecraft/Roblox now no-answer properly
- Competition terms like round/decider guarded from game availability
- Our Games source used for game-related answers

## User Preferences

User wants:

- Thai explanations
- real file edits
- detailed but practical docs
- test reports
- no hallucination
- answer-first style
- fast responses
- local/free-first
- deployable MVP

User dislikes:

- vague theory
- pretending LLM is used when it is rulebase
- answers that pull unrelated data
- PASS tests that hide wrong answers
- overly fixed rulebase that cannot handle natural wording

## Must Preserve Behavior

- เด็ก/นักศึกษา มอ = PSU Student and Staff = 0 บาท when service fee says free
- ต่างมหาลัย/สจล/จุฬา = General Student
- Unknown games must not pull schedule/rules
- Equipment game catalog must not answer `เกมนี้`
- Tekken `round/decider/1v1` must route competition_rules
- Friday answer must separate morning/afternoon
- Penalty questions with no data must no-answer

## Run Commands

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data"
$env:PYTHONIOENCODING='utf-8'
$OutputEncoding = [System.Text.UTF8Encoding]::new($false)
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)

py -3 -m py_compile app\runtime\fast_answer.py app\pipeline\router.py app\pipeline\engine.py
py -3 tools\validate_update.py
py -3 tools\run_ground_truth_pipeline_eval.py --label check_gt360
py -3 tools\run_ground_truth_pipeline_eval.py --ground-truth data\ground_truth\competition_challenger_v2\ground_truth_competition_challenger_v2_real_competitor_questions.jsonl --label check_comp_v2
```

Run local:

```powershell
py -3 -m app.web_api.server --host 127.0.0.1 --port 8018
```

Deploy:

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy"
vercel deploy --prod --yes
```

## If Asked To Fix A Bad Answer

Do this:

1. Reproduce with exact question.
2. Inspect route/mode/source.
3. Decide if issue is route, data, retrieval, formatter, validator, or GT.
4. Patch the smallest responsible file.
5. Add ad-hoc question.
6. Run relevant regression.
7. If deploy needed, sync 18 -> 20, deploy, test production.
8. Update daily log/report.

## Read More If Needed

Read:

```text
00_README_START_HERE.md
11_AGENT_STATE_TRANSFER_FULL.md
12_CHANGED_FILES_AND_CODE_INDEX.md
13_COMMAND_CHEATSHEET.md
14_SMOKE_TEST_QUESTIONS.md
15_REQUIREMENTS_AND_ACCEPTANCE_CRITERIA.md
16_DO_NOT_DO_AND_RISK_REGISTER.md
```

