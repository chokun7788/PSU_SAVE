# Command Cheatsheet

คำสั่งที่ใช้บ่อยสำหรับทำงานต่อ โปรดใช้ PowerShell

## Encoding สำหรับภาษาไทย

รันก่อนคำสั่งที่อ่าน/เขียนภาษาไทย:

```powershell
$env:PYTHONIOENCODING='utf-8'
$OutputEncoding = [System.Text.UTF8Encoding]::new($false)
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
```

## เข้าโฟลเดอร์หลัก

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data"
```

## Compile

```powershell
py -3 -m py_compile app\runtime\fast_answer.py app\pipeline\router.py app\pipeline\engine.py
```

## Validate data

```powershell
py -3 tools\validate_update.py
```

ผลที่คาดหวัง:

```text
VALIDATION OK
- rule files: 8
- rules: 77
- curated rows: 324
- service fee sanity: OK
```

## Run local server

```powershell
py -3 -m app.web_api.server --host 127.0.0.1 --port 8018
```

เปิด:

```text
http://127.0.0.1:8018/
```

## Restart local server แบบ background

```powershell
$root='C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data'
$serverProcs = Get-CimInstance Win32_Process | Where-Object { ($_.Name -match 'python|py') -and ($_.CommandLine -match 'app\.web_api\.server') }
foreach ($proc in $serverProcs) { Stop-Process -Id $proc.ProcessId -Force }
Start-Sleep -Milliseconds 500
Start-Process -FilePath 'py.exe' -ArgumentList @('-3','-m','app.web_api.server','--host','127.0.0.1','--port','8018') -WorkingDirectory $root -WindowStyle Hidden
```

## Test local health

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8018/health" -Method Get
```

## Test local API คำถามเดียว

```powershell
Invoke-RestMethod `
  -Method Post `
  -Uri "http://127.0.0.1:8018/api/chat" `
  -ContentType "application/json; charset=utf-8" `
  -Body (@{question="อุปกรณ์เล่นเกมอะไรได้บ้าง"; debug=$false} | ConvertTo-Json)
```

## Test local API หลายคำถามด้วย Python

```powershell
@'
import json
import urllib.request

questions = [
    "อุปกรณ์เล่นเกมอะไรได้บ้าง",
    "Cockpit มีเกมอะไรบ้าง",
    "เล่น Minecraft ได้ไหม",
    "Roblox เล่นได้ไหม",
    "ตอนนี้มีเกมแข่งอะไรบ้าง",
    "Tekken 8 เกมนึงมี 3 rounds ใช่ไหม",
]

for question in questions:
    body = json.dumps({"question": question, "debug": False}, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request("http://127.0.0.1:8018/api/chat", data=body, headers={"Content-Type": "application/json; charset=utf-8"}, method="POST")
    with urllib.request.urlopen(req, timeout=20) as res:
        data = json.loads(res.read().decode("utf-8"))
    print("=" * 80)
    print("Q:", question)
    print("route:", data.get("route_category"), "/", data.get("route_intent"), "mode:", data.get("mode"), "latency:", data.get("latency_sec"))
    print(data.get("answer"))
'@ | py -3 -
```

## Run ad-hoc test

```powershell
py -3 tools\run_ad_hoc_pipeline_log.py --label my_adhoc --questions-file reports\ad_hoc_questions_equipment_game_catalog_fix4_20260704.txt
```

## Run GT360

```powershell
py -3 tools\run_ground_truth_pipeline_eval.py --label my_gt360
```

ลด token โดย redirect:

```powershell
py -3 tools\run_ground_truth_pipeline_eval.py --label my_gt360 *> reports\run_stdout_my_gt360.txt
```

## Run competition challenger v2

```powershell
py -3 tools\run_ground_truth_pipeline_eval.py --ground-truth data\ground_truth\competition_challenger_v2\ground_truth_competition_challenger_v2_real_competitor_questions.jsonl --label my_comp_v2
```

redirect:

```powershell
py -3 tools\run_ground_truth_pipeline_eval.py --ground-truth data\ground_truth\competition_challenger_v2\ground_truth_competition_challenger_v2_real_competitor_questions.jsonl --label my_comp_v2 *> reports\run_stdout_my_comp_v2.txt
```

## Read latest reports

```powershell
Get-Content -Encoding UTF8 -Path reports\pipeline_ground_truth_report_gt360_equipment_game_catalog_fix5_source_20260704.md
Get-Content -Encoding UTF8 -Path reports\pipeline_ground_truth_report_competition_challenger_v2_equipment_game_catalog_fix5_source_20260704.md
Get-Content -Encoding UTF8 -Path reports\ad_hoc_pipeline_results_equipment_game_catalog_fix5_source_20260704.md
```

## Sync 18 -> 20 สำหรับ deploy

```powershell
$src='C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data'
$dst='C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy'
robocopy "$src\app" "$dst\app" /E /XD __pycache__ /XF *.pyc
if ($LASTEXITCODE -le 7) { $global:LASTEXITCODE = 0 }
robocopy "$src\data" "$dst\data" /E /XD __pycache__ /XF *.pyc
if ($LASTEXITCODE -le 7) { $global:LASTEXITCODE = 0 }
Copy-Item -LiteralPath "$src\web_chat\index.html" -Destination "$dst\index.html" -Force
Copy-Item -LiteralPath "$src\web_chat\app.js" -Destination "$dst\app.js" -Force
Copy-Item -LiteralPath "$src\web_chat\styles.css" -Destination "$dst\styles.css" -Force
```

## Compile deploy folder

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy"
py -3 -m py_compile app\runtime\fast_answer.py app\pipeline\router.py app\pipeline\engine.py api\chat.py api\health.py
```

## Deploy Vercel

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy"
vercel deploy --prod --yes
```

เก็บ output:

```powershell
vercel deploy --prod --yes *> deploy_stdout_<label>.txt
```

## Test production API

```powershell
@'
import json
import urllib.request

base = "https://psu-esports-chatbot.vercel.app/api/chat"
questions = [
    "อุปกรณ์เล่นเกมอะไรได้บ้าง",
    "Cockpit มีเกมอะไรบ้าง",
    "เล่น Minecraft ได้ไหม",
    "Roblox เล่นได้ไหม",
    "ตอนนี้มีเกมแข่งอะไรบ้าง",
]
for question in questions:
    body = json.dumps({"question": question, "debug": False}, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(base, data=body, headers={"Content-Type": "application/json; charset=utf-8"}, method="POST")
    with urllib.request.urlopen(req, timeout=40) as res:
        data = json.loads(res.read().decode("utf-8"))
    print("=" * 80)
    print("Q:", question)
    print("route:", data.get("route_category"), "/", data.get("route_intent"), "mode:", data.get("mode"), "latency:", data.get("latency_sec"))
    print(data.get("answer"))
'@ | py -3 -
```

## Search commands

```powershell
rg -n "equipment_game_catalog|game_availability|competition_rules_lookup" app
rg -n "Minecraft|Roblox|Cockpit มีเกม|เด็ก มอ|decider|rounds" data ..\15_PSU_Esports_Local_RAG_Qwen3_4B\ground_truth
rg -n "def answer_games|def answer_equipment|def answer_schedule|def answer_service_fee" app\runtime\fast_answer.py
```

## Git status

```powershell
git status --short
```

หมายเหตุ:

- repo มี untracked หลายโฟลเดอร์จากงานที่สร้าง
- อย่า revert ไฟล์ของผู้ใช้

