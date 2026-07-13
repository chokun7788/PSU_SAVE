# Deployment Runbook

ไฟล์นี้คือคู่มือรัน local และ deploy production

## Local Development

โฟลเดอร์หลัก:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data
```

รัน local web/API:

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data"
py -3 -m app.web_api.server --host 127.0.0.1 --port 8018
```

เปิดเว็บ:

```text
http://127.0.0.1:8018/
```

Health check:

```text
http://127.0.0.1:8018/health
```

API:

```text
POST http://127.0.0.1:8018/api/chat
```

ตัวอย่างยิง API ด้วย PowerShell:

```powershell
Invoke-RestMethod `
  -Method Post `
  -Uri "http://127.0.0.1:8018/api/chat" `
  -ContentType "application/json; charset=utf-8" `
  -Body (@{question="อุปกรณ์เล่นเกมอะไรได้บ้าง"; debug=$false} | ConvertTo-Json)
```

## Restart Local Server

ถ้ามี server เก่าค้าง:

```powershell
$root='C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data'
$serverProcs = Get-CimInstance Win32_Process | Where-Object { ($_.Name -match 'python|py') -and ($_.CommandLine -match 'app\.web_api\.server') }
foreach ($proc in $serverProcs) { Stop-Process -Id $proc.ProcessId -Force }
Start-Sleep -Milliseconds 500
Start-Process -FilePath 'py.exe' -ArgumentList @('-3','-m','app.web_api.server','--host','127.0.0.1','--port','8018') -WorkingDirectory $root -WindowStyle Hidden
```

## Vercel Deploy Folder

โฟลเดอร์:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy
```

มี:

```text
api\chat.py
api\health.py
app
data
index.html
app.js
styles.css
vercel.json
requirements.txt
.python-version
README_DEPLOY.md
```

Production:

```text
https://psu-esports-chatbot.vercel.app
```

## Sync จากโฟลเดอร์ 18 ไป 20

เมื่อแก้โค้ดใน `18` แล้วต้อง sync ไป `20` ก่อน deploy

คำสั่ง:

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

หมายเหตุ:

- `robocopy` exit code 0-7 ถือว่า OK
- `vercel.json` มี exclude สำหรับบางโฟลเดอร์ เช่น reports/logs/human_review/ground_truth
- อย่าเอา model หลาย GB ขึ้น Vercel

## Compile ฝั่ง Deploy

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy"
py -3 -m py_compile app\runtime\fast_answer.py app\pipeline\router.py app\pipeline\engine.py api\chat.py api\health.py
```

## Deploy Production

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy"
vercel deploy --prod --yes
```

deploy ล่าสุด:

```text
Production: https://psu-esports-chatbot.vercel.app
Deployment: https://psu-esports-chatbot-kku2axrsq-chokuns-projects-908117b8.vercel.app
Inspect: https://vercel.com/chokuns-projects-908117b8/psu-esports-chatbot/3iHJehurdZdYCDS7ZtTH7cBbZ1E5
```

Deploy log:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy\deploy_stdout_equipment_game_catalog_fix5_20260704.txt
```

## Test Production API

Python quick test:

```powershell
$env:PYTHONIOENCODING='utf-8'
$OutputEncoding = [System.Text.UTF8Encoding]::new($false)
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new($false)
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

## Vercel CLI Prompt ที่เคยเจอ

ถ้าใช้ `vercel` ครั้งแรกจะถาม:

```text
Which team?
Project? Create new project
Name?
Detected Flask
Customize settings? (y/N)
Customize advanced settings?
```

แนวทางตอบ:

- Team: เลือกของผู้ใช้ เช่น `chokhun's projects`
- Project: create new หรือเลือก project เดิม `psu-esports-chatbot`
- Name: `PSU_Esports` หรือ `psu-esports-chatbot`
- Customize settings: ปกติ `N`
- Customize advanced settings: ปกติ `N`

ตอนนี้ project ผูกกับ Vercel แล้ว จึงใช้:

```powershell
vercel deploy --prod --yes
```

## Git จำเป็นไหม

ถ้า deploy ผ่าน Vercel CLI จากเครื่อง:

```text
ไม่จำเป็นต้อง push Git ก่อน
```

แต่ถ้าจะ deploy ผ่าน Vercel Dashboard แบบ Import Project:

```text
ควรอัปขึ้น GitHub ก่อน
```

แนะนำระยะยาว:

- ใช้ GitHub repo
- push เฉพาะโฟลเดอร์ deploy หรือ repo ที่จัดสะอาดแล้ว
- ตั้ง Vercel auto deploy จาก main branch
- เก็บ secrets ใน Vercel Environment Variables

## ข้อจำกัดของ Vercel

Vercel serverless:

- เหมาะกับ API เบา ๆ
- ไม่เหมาะกับ local LLM หลาย GB
- ไม่เหมาะกับงาน compute นาน
- ไม่ควรเขียน log เป็นไฟล์ถาวร
- function มี timeout

ดังนั้น production ตอนนี้:

- ใช้ rulebase/RAG-lite
- ไม่ใช้ Ollama
- ไม่ใช้ Qwen local บน Vercel

ถ้าจะใช้ LLM จริง:

- ทำ backend แยกบนเครื่องศูนย์/VPS/Render/Fly/Railway
- เว็บ Vercel เรียก API backend
- backend รัน Ollama/Qwen/Vector DB ได้

