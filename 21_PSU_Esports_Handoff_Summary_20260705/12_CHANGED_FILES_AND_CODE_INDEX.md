# Changed Files and Code Index

ไฟล์นี้สรุปว่าโค้ด/data สำคัญอยู่ตรงไหน และล่าสุดแก้ส่วนไหนไป เพื่อให้ agent ใหม่รู้ตำแหน่งทันที

## โฟลเดอร์หลัก

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data
```

## ไฟล์ที่แก้ล่าสุดและสำคัญมาก

### `app\runtime\fast_answer.py`

บทบาท:

- deterministic fast path
- answer functions
- hardcoded service/game/equipment/schedule knowledge บางส่วน
- HITS/source metadata
- no-answer/unknown game
- equipment game catalog

จุดสำคัญล่าสุด:

```text
OUR_GAMES_URL = "https://esports.phuket.psu.ac.th/Services/our-games"
HITS["our_games"] includes:
  - our_games
  - Reservation fallback
```

function สำคัญ:

```text
_looks_like_game_availability(q)
_looks_like_equipment_game_catalog(q)
_equipment_game_catalog_answer(q, start)
answer_games(query, start)
answer_equipment(query, start)
```

ตำแหน่งโดยประมาณล่าสุด:

```text
OUR_GAMES_URL: line ~30
HITS: line ~45
_looks_like_game_availability: line ~1258
_looks_like_equipment_game_catalog: line ~1284
_equipment_game_catalog_answer: line ~1357
answer_games: line ~1456
answer_equipment: line ~1510
```

สิ่งที่แก้ล่าสุด:

- เพิ่ม source `our_games`
- เพิ่ม equipment game catalog answer
- ให้ `answer_games()` ตรวจ equipment catalog ก่อน availability
- ให้ `answer_equipment()` ตรวจ equipment catalog ก่อน zone/item fallback
- unknown game ใช้ Our Games source
- known game availability ใช้ Our Games source
- เพิ่ม guard ไม่ให้ competition rule terms ไป game availability

ต้องระวัง:

- ถ้าแก้ `_looks_like_game_availability` กว้างเกิน จะดึงคำถามกติกามาตอบแบบเกมมีไหม
- ถ้าแก้ `_looks_like_equipment_game_catalog` กว้างเกิน จะดึงคำถามอุปกรณ์ไปตอบรายชื่อเกมผิด
- ถ้าแก้ HITS source อาจทำให้ ground truth source check fail

### `app\pipeline\router.py`

บทบาท:

- เลือก route/category/intent
- จัด priority ของ intent
- กัน broad keyword ชนกัน

function สำคัญ:

```text
_looks_like_equipment_game_catalog_query(q)
_looks_like_game_availability_query(q)
route_intent(pre, entities)
```

ตำแหน่งโดยประมาณ:

```text
_looks_like_equipment_game_catalog_query: line ~90
_looks_like_game_availability_query: line ~143
equipment_game_catalog route: line ~178
game_availability route: line ~184
```

route order ล่าสุดช่วงต้น:

```text
equipment item
equipment game catalog
specific news date
competition game list
game availability
zone equipment
competition rule
game detail
...
```

เหตุผล:

- equipment game catalog ต้องมาก่อน game availability
- competition game list ต้องมาก่อน general games
- competition rule guard ต้องกัน round/decider/map/team

### `app\pipeline\engine.py`

บทบาท:

- orchestrates answer pipeline
- preprocess -> route -> deterministic -> competition -> RAG -> no answer

มักไม่ต้องแก้บ่อย ยกเว้นจะเพิ่มขั้น pipeline ใหม่

### `app\pipeline\retrieval.py`

บทบาท:

- curated RAG-lite retrieval
- ใช้เมื่อตัว fast path/fact card ไม่ตอบ

ถ้า RAG หาไม่เจอทั้งที่ data มี ให้ดูไฟล์นี้

### `app\pipeline\validator.py`

บทบาท:

- ตรวจคำตอบหลัง format
- ดักคำตอบยาว/เสี่ยงผิด

ควรเพิ่ม validator ถ้าเจอ false pass หรือคำตอบเสี่ยง

### `app\calculator\service_fee.py`

บทบาท:

- คำนวณราคา
- map user group/service/session

ถ้าคำถามราคาเสีย ให้ดูไฟล์นี้ร่วมกับ `fast_answer.py`

### `app\calendar\service_calendar.py`

บทบาท:

- วันนี้/พรุ่งนี้/เดือนนี้
- holiday/closure
- Bangkok timezone

ถ้าถามวันหยุดแล้วผิด ให้ดูไฟล์นี้กับ `data\calendar\service_closures.jsonl`

## Data files ที่มักต้องแก้

### Rules

```text
data\rules\reservation_rules.jsonl
data\rules\games_rules.jsonl
data\rules\equipment_rules.jsonl
data\rules\penalty_rules.jsonl
data\rules\no_answer_rules.jsonl
```

ใช้เมื่อ:

- เพิ่ม FAQ pattern
- เพิ่มคำตอบตายตัว
- เพิ่ม no-answer guard

### Curated facts

```text
data\curated\curated_facts.jsonl
data\curated\curated_competition_rules.jsonl
data\curated\equipment_item_details.jsonl
data\curated\game_item_details.jsonl
```

ใช้เมื่อ:

- เพิ่มข้อมูลอธิบาย
- เพิ่ม game detail
- เพิ่ม equipment detail
- เพิ่ม evidence สำหรับ RAG-lite

### Competition rules

```text
data\competition_rules\competition_rule_documents.jsonl
data\competition_rules\competition_rule_chunks.jsonl
data\competition_rules\competition_rule_fact_cards.jsonl
```

ใช้เมื่อ:

- เพิ่มเอกสารกติกา
- เพิ่ม fact card
- แก้คำตอบกติกา

### Calendar

```text
data\calendar\service_closures.jsonl
```

ใช้เมื่อ:

- เพิ่มวันปิดพิเศษ
- เพิ่มวันหยุดราชการ
- แก้ closure reason

## Test/report files ล่าสุด

```text
reports\ad_hoc_pipeline_results_equipment_game_catalog_fix5_source_20260704.md
reports\pipeline_ground_truth_report_gt360_equipment_game_catalog_fix5_source_20260704.md
reports\pipeline_ground_truth_report_competition_challenger_v2_equipment_game_catalog_fix5_source_20260704.md
```

## Deploy folder files

หลังแก้ใน `18` ต้อง sync ไป `20`

ไฟล์ deploy:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy\api\chat.py
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy\api\health.py
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy\app
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy\data
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy\index.html
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy\app.js
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy\styles.css
```

## วิธีค้นหาเร็ว

หา route:

```powershell
rg -n "equipment_game_catalog|game_availability|competition_rules_lookup" app
```

หา answer function:

```powershell
rg -n "def answer_games|def answer_equipment|def answer_schedule|def answer_service_fee" app\runtime\fast_answer.py
```

หา source URL:

```powershell
rg -n "OUR_GAMES_URL|RESERVATION_URL|SERVICE_FEE" app data
```

หา ground truth case:

```powershell
rg -n "Minecraft|Roblox|Cockpit มีเกม|เด็ก มอ|decider|rounds" data ..\15_PSU_Esports_Local_RAG_Qwen3_4B\ground_truth
```

## ถ้าจะแก้คำตอบผิด ควรเริ่มที่ไหน

กรณีราคา:

```text
app\calculator\service_fee.py
app\runtime\fast_answer.py
data\curated\curated_facts_service_fee_2026_aliases.jsonl
ground truth GT360
```

กรณี schedule:

```text
app\calendar\service_calendar.py
app\runtime\fast_answer.py
data\calendar\service_closures.jsonl
app\pipeline\router.py
```

กรณี game/equipment:

```text
app\runtime\fast_answer.py
app\pipeline\router.py
data\curated\game_item_details.jsonl
data\curated\equipment_item_details.jsonl
```

กรณี competition rules:

```text
data\competition_rules\competition_rule_fact_cards.jsonl
data\curated\curated_competition_rules.jsonl
app\runtime\fast_answer.py
app\pipeline\retrieval.py
data\ground_truth\competition_challenger_v2
```

กรณี no-answer:

```text
data\rules\no_answer_rules.jsonl
app\pipeline\guard.py
app\runtime\fast_answer.py
```

