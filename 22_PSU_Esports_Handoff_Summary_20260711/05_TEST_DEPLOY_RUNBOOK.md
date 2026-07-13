# Test And Deploy Runbook

## ตั้ง working directory

Source:

```powershell
cd C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data
```

Deploy:

```powershell
cd C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy
```

## UTF-8 สำหรับ PowerShell

ถ้า PowerShell แสดงไทยเพี้ยน ให้ตั้ง:

```powershell
chcp 65001
$OutputEncoding = [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()
```

หมายเหตุ:

- บางครั้ง output ใน terminal อาจยังดูเพี้ยน แต่ไฟล์จริง encoding ถูกต้อง
- เช็กด้วย Python อ่านไฟล์ UTF-8 จะชัวร์กว่า

## Compile

ตัวอย่าง compile เฉพาะไฟล์ที่แก้:

```powershell
python -m py_compile app\pipeline\engine.py app\pipeline\vector_retrieval.py tools\build_game_control_facts.py
```

ถ้าแก้ `fast_answer.py`:

```powershell
python -m py_compile app\runtime\fast_answer.py
```

## Build Game Control Facts

```powershell
python tools\build_game_control_facts.py
```

ผลที่ควรเห็น:

```text
GAME CONTROL FACTS OK
- rows total: 346
- ps5: 18 games, 261 rows
- nintendo: 8 games, 85 rows
```

## Build Vector Index

```powershell
python tools\build_vector_index.py
```

ผลที่ควรเห็นหลังงานล่าสุด:

```text
VECTOR INDEX OK
- backend: local_hash_char_ngram_v1
- docs: 659
```

## Smoke Test ผ่าน Python

ตัวอย่าง:

```powershell
@'
from app.pipeline.engine import answer_question_pipeline_debug

questions = [
    "ปุ่มกระโดดใน Call of Duty กดอะไร",
    "เทคเคน 8 ปุ่มเตะขวากดอะไร",
    "ลิตเติลไนท์แม ปุ่มวิ่งกดอะไร",
    "เกมเทคอิดเอ้าปุ่มกระโดดกดอะไร",
]

for q in questions:
    result = answer_question_pipeline_debug(q)
    print("Q:", q)
    print("mode:", result.mode, "route:", result.route.category, result.route.intent, "conf:", result.confidence)
    print(result.answer[:500])
    print("---")
'@ | python -
```

mode ที่ควรเห็นสำหรับคำถามปุ่ม:

```text
pipeline:game_control_vector_first
```

## Sync 18 ไป 20 แบบจำเพาะไฟล์

ใช้เมื่อแก้เฉพาะไฟล์บางชุด:

```powershell
$src='C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data'
$dst='C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy'

Copy-Item -LiteralPath "$src\app\pipeline\engine.py" -Destination "$dst\app\pipeline\engine.py" -Force
Copy-Item -LiteralPath "$src\app\pipeline\vector_retrieval.py" -Destination "$dst\app\pipeline\vector_retrieval.py" -Force
Copy-Item -LiteralPath "$src\tools\build_game_control_facts.py" -Destination "$dst\tools\build_game_control_facts.py" -Force
Copy-Item -LiteralPath "$src\data\curated\game_control_facts.jsonl" -Destination "$dst\data\curated\game_control_facts.jsonl" -Force

if (Test-Path -LiteralPath "$dst\data\control_game_split") {
  Remove-Item -LiteralPath "$dst\data\control_game_split" -Recurse -Force
}
Copy-Item -LiteralPath "$src\data\control_game_split" -Destination "$dst\data\control_game_split" -Recurse -Force
Copy-Item -LiteralPath "$src\data\vector\psu_hybrid_vector_index.json" -Destination "$dst\data\vector\psu_hybrid_vector_index.json" -Force
```

หลัง sync ให้ไป folder 20 แล้ว compile/build:

```powershell
cd C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy
python -m py_compile app\pipeline\engine.py app\pipeline\vector_retrieval.py tools\build_game_control_facts.py
python tools\build_vector_index.py
```

## Deploy Vercel

ผู้ใช้มัก deploy เอง

ขั้นตอนปกติ:

```powershell
cd C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy
vercel
vercel --prod
```

หมายเหตุ:

- ถ้า project เชื่อมแล้ว บางครั้งใช้ `vercel --prod` ได้เลย
- ถ้าเจอ `ECONNRESET` อาจเป็น network/Vercel CLI connection หลุด ให้ลองใหม่ ไม่จำเป็นว่า deploy fail เสมอไป
- ต้องดู production URL/inspect URL ที่ CLI แสดง

## Production API Test

หลัง deploy:

```powershell
@'
import json, urllib.request

url = "https://psu-esports-chatbot.vercel.app/api/chat"
payload = {"message": "ปุ่มกระโดดใน Call of Duty กดอะไร"}
req = urllib.request.Request(
    url,
    data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
    headers={"Content-Type": "application/json; charset=utf-8"},
    method="POST",
)
with urllib.request.urlopen(req, timeout=20) as r:
    print(r.read().decode("utf-8"))
'@ | python -
```

## Ground Truth

อย่า run Ground Truth ชุดใหญ่ทุกครั้ง ยกเว้นผู้ใช้ขอ

ถ้าผู้ใช้ขอ ให้หาไฟล์/command ที่มีใน repo ก่อน ไม่ต้องสร้างตัวเช็กใหม่โดยไม่จำเป็น

