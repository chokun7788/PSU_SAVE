# PSU Esports Chatbot - All In One Handoff 2026-07-11

ไฟล์นี้เป็นสรุปแบบไฟล์เดียวสำหรับแชทใหม่ ถ้าอ่านได้ไฟล์เดียวให้อ่านไฟล์นี้ก่อน

## Project

โปรเจกต์นี้คือ PSU Esports Chatbot สำหรับตอบคำถามเกี่ยวกับ PSU Esports Studio - Phuket เช่น:

- ราคาใช้บริการ
- เวลาเปิดปิด
- วิธีจอง
- รายชื่อเกม
- เกมอยู่โซนไหน
- อุปกรณ์มีอะไร
- วิธีใช้งานอุปกรณ์
- ปุ่มควบคุมเกม
- กติกาการแข่งขัน
- ข่าว/กิจกรรมบางส่วน
- วันหยุด/ปฏิทินบางส่วน

Production URL:

```text
https://psu-esports-chatbot.vercel.app
```

## Main Paths

Root:

```text
C:\Users\Chokhun\Downloads\Learn-LLM
```

Source หลัก:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data
```

Deploy:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy
```

Daily logs:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\17_PSU_Esports_Daily_Logs
```

Handoff ล่าสุด:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\22_PSU_Esports_Handoff_Summary_20260711
```

## User Requirements

ต้องยึดสิ่งนี้ทุกครั้ง:

- ตอบเป็นภาษาไทย
- อ่าน handoff ก่อนเริ่มงาน
- ถ้าแก้โค้ด ให้แก้ไฟล์จริงใน folder 18
- ถ้าพร้อม deploy ให้ sync ไป folder 20
- ถ้าไม่มีข้อมูลจริง ห้ามเดา ให้ตอบ no-answer แบบสุภาพ
- รักษา answer-first style
- อย่าบอกว่าใช้ LLM ถ้าคำตอบมาจาก rulebase/fast path
- อย่าแก้ตัวตรวจให้ผ่อนลงเพื่อให้ PASS ง่าย
- อย่า run Ground Truth ชุดใหญ่ทุกครั้ง ยกเว้นผู้ใช้ขอ
- ถ้าแก้ logic สำคัญ ให้ compile และ smoke test ตามความเหมาะสม
- ถ้า deploy ต้อง test production API หลัง deploy
- ต้องเขียน daily log ใน `17_PSU_Esports_Daily_Logs`
- ผู้ใช้ต้องการประหยัด token ให้ทำเท่าที่จำเป็นและสรุปชัดเจน

## Current Architecture

ระบบ production ไม่ได้ปล่อย LLM ตอบอิสระเป็นหลัก แต่ใช้:

```text
rulebase + deterministic fast path + curated RAG-lite + guarded vector retrieval + validator + no-answer guard
```

Flow หลัก:

```text
User question
-> preprocess / normalize
-> extract entities
-> guard scope
-> route intent
-> game control vector first เฉพาะคำถามปุ่ม/จอย
-> deterministic fast path
-> competition fact card ถ้าเป็นกติกาแข่ง
-> hybrid/curated retrieval
-> guarded vector retrieval
-> validate
-> format answer
-> polite no-answer ถ้าไม่มี verified context
```

## Core Files

```text
app\pipeline\engine.py
app\pipeline\router.py
app\pipeline\retrieval.py
app\pipeline\vector_retrieval.py
app\pipeline\hybrid_retrieval.py
app\pipeline\validator.py
app\pipeline\formatter.py
app\runtime\fast_answer.py
app\core\normalization.py
app\core\thai_style.py
```

หน้าที่:

- `engine.py`: flow หลักของ pipeline
- `router.py`: route/category/intent
- `fast_answer.py`: rulebase/fast path
- `retrieval.py`: curated retrieval
- `vector_retrieval.py`: vector index และ guarded vector retrieval
- `hybrid_retrieval.py`: retrieval/rerank แบบ guard เพิ่ม
- `validator.py`: ตรวจคำตอบก่อนปล่อย
- `thai_style.py`: post-process ภาษาไทย

## Important Data

```text
data\curated\game_title_aliases.jsonl
data\curated\game_item_details.jsonl
data\curated\our_games_scraped_details.jsonl
data\curated\equipment_item_details.jsonl
data\curated\game_control_facts.jsonl
data\competition_rules\competition_rule_fact_cards.jsonl
data\vector\psu_hybrid_vector_index.json
```

## Latest Major Change: Game Controls

ผู้ใช้ต้องการให้ข้อมูลวิธีควบคุมเกมแยกระหว่าง PS5 และ Nintendo และนำเข้า vector DB

Source เดิม:

```text
data\control_game\nintendo
```

หมายเหตุ: folder นี้ชื่อ nintendo แต่มีทั้ง PS5 และ Nintendo Switch

Script ใหม่:

```text
tools\build_game_control_facts.py
```

Output ใหม่:

```text
data\control_game_split\ps5
data\control_game_split\nintendo
data\curated\game_control_facts.jsonl
```

ผลลัพธ์ล่าสุด:

```text
control facts: 346 rows
PS5: 18 games, 261 rows
Nintendo Switch: 8 games, 85 rows
vector docs total: 659
game_controls docs in vector: 346
vector backend: local_hash_char_ngram_v1
```

Logic ใหม่:

- `app/pipeline/vector_retrieval.py`
  - มี `looks_like_game_control_query()`
  - เปิด category `game_controls` ให้ route `games/equipment`
  - มี guard บังคับว่าต้องเป็นคำถามปุ่ม/จอย/ควบคุม
  - format answer เป็นรายการปุ่ม

- `app/pipeline/engine.py`
  - มี mode `pipeline:game_control_vector_first`
  - คำถามปุ่มจะลอง vector control ก่อน fast path เกมทั่วไป

Smoke test ที่ผ่าน:

```text
ปุ่มกระโดดใน Call of Duty กดอะไร
เทคเคน 8 ปุ่มเตะขวากดอะไร
ลิตเติลไนท์แม ปุ่มวิ่งกดอะไร
เกมเทคอิดเอ้าปุ่มกระโดดกดอะไร
```

## Other Recent Fixes

Booking:

- คำถามแนว `จองคิวเล่นเกมต้องทำยังไง`, `จองอุปกรณ์ต้องทำยังไง`, `สอนจอง VR`
- ตอนนี้เข้า `pipeline:booking_howto_fast_path`
- ไม่ควรตอบนโยบายยกเลิก/คืนเงินผิด

Game catalog count:

- `มีเกมทั้งหมดกี่เกม`
- ควรตอบจำนวนเกมทั้งหมดและรายการแยก zone
- mode: `pipeline:games_full_catalog_count_fast_path`

Game alias:

- มี `data\curated\game_title_aliases.jsonl`
- ใช้รองรับชื่อไทย ชื่อย่อ และสะกดเพี้ยน
- ยังจำเป็นแม้มี vector เพราะช่วยล็อก entity ลดการตอบมั่ว

## Common Debug Strategy

ถ้าคำตอบผิด:

1. ดู `mode`
2. ดู `route.category` และ `route.intent`
3. ดู source/hits ว่ามาจากไฟล์ไหน
4. ถ้า fast path ตอบผิด ให้แก้ `fast_answer.py`
5. ถ้า route ผิด ให้แก้ `router.py`
6. ถ้า data มีแต่ retrieval ไม่เจอ ให้เช็ก:
   - data อยู่ใน curated หรือยัง
   - build vector แล้วหรือยัง
   - category allowed หรือยัง
   - guard threshold block หรือไม่
   - formatter รองรับ category นั้นไหม
7. ถ้า answer ถูกแต่ format แปลก ให้ดู `formatter.py` หรือ answer function

## Testing

Compile:

```powershell
python -m py_compile app\pipeline\engine.py app\pipeline\vector_retrieval.py tools\build_game_control_facts.py
```

Build game controls:

```powershell
python tools\build_game_control_facts.py
```

Build vector:

```powershell
python tools\build_vector_index.py
```

Smoke test:

```powershell
@'
from app.pipeline.engine import answer_question_pipeline_debug
for q in ["ปุ่มกระโดดใน Call of Duty กดอะไร", "ลิตเติลไนท์แม ปุ่มวิ่งกดอะไร"]:
    r = answer_question_pipeline_debug(q)
    print(q)
    print(r.mode, r.route.category, r.route.intent, r.confidence)
    print(r.answer[:500])
    print("---")
'@ | python -
```

อย่า run Ground Truth ใหญ่ทุกครั้ง ยกเว้นผู้ใช้ขอ

## Deploy

ผู้ใช้มัก deploy เอง

ถ้าต้องเตรียม deploy:

1. sync 18 ไป 20
2. compile/test ใน 20
3. build vector ใน 20
4. ให้ผู้ใช้ run:

```powershell
cd C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy
vercel --prod
```

หลัง deploy ต้อง test production API

## Known Risks / Do Not Do

- อย่า deploy เองถ้าผู้ใช้ไม่ได้สั่ง
- อย่าแก้ test ให้ผ่านง่าย
- อย่าเดาคำตอบจากความรู้ทั่วไปถ้าเป็นข้อมูลศูนย์
- อย่าเปิด vector guard กว้างเกินไป เพราะจะดึงเอกสารผิด
- อย่าปล่อย competition rules มาตอบคำถามเกมทั่วไป
- อย่าเอา model embedding/LLM ใหญ่ขึ้น Vercel โดยไม่คิดเรื่องขนาด/เวลา/ค่าใช้จ่าย
- อย่าลืม daily log

## What To Read Next

ถ้าจะทำงานเฉพาะด้าน:

- requirement ผู้ใช้: `01_PERSONAL_REQUIREMENTS_AND_WORK_STYLE.md`
- path/file map: `02_PROJECT_PATHS_AND_FILE_MAP.md`
- flow ระบบ: `03_CURRENT_SYSTEM_FLOW.md`
- งานล่าสุด: `04_RECENT_WORK_AND_CURRENT_STATE.md`
- command/deploy: `05_TEST_DEPLOY_RUNBOOK.md`

