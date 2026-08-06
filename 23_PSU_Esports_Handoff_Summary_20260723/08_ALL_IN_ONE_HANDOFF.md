# PSU Esports Chatbot - All In One Handoff 2026-07-23

ไฟล์นี้เป็นสรุปแบบไฟล์เดียวสำหรับแชทใหม่ ถ้าอ่านได้ไฟล์เดียวให้อ่านไฟล์นี้ก่อน

## Project

โปรเจกต์นี้คือ PSU Esports Chatbot สำหรับตอบคำถามเกี่ยวกับ PSU Esports Studio - Phuket เช่น:

- ราคาใช้บริการ
- เวลาเปิด-ปิด
- วิธีจอง
- รายชื่อเกม
- เกมอยู่โซนไหน
- อุปกรณ์มีอะไร
- วิธีใช้อุปกรณ์
- ปุ่มควบคุมเกม
- สมาชิกทีมและตำแหน่ง
- กติกาการแข่งขัน
- คำถาม follow-up ใน session
- คำถามทั่วไปนอกโดเมนผ่าน Local LLM fallback

ตอนนี้ทิศทางคือ local-first:

- ไม่ต้องยุ่ง git
- ไม่ต้องยุ่ง Vercel/deploy folder ถ้าผู้ใช้ไม่ได้สั่งใหม่
- โฟกัส local chatbot/local LLM/local eval

## Main Paths

Root:

```text
C:\Users\Chokhun\Downloads\Learn-LLM
```

Source หลัก:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data
```

Daily logs:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\17_PSU_Esports_Daily_Logs
```

Handoff ล่าสุด:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\23_PSU_Esports_Handoff_Summary_20260723
```

## User Requirements

ต้องยึดสิ่งนี้ทุกครั้ง:

- ตอบเป็นภาษาไทย
- answer-first
- ไม่เวิ่นเว้อ
- ถ้าไม่มีข้อมูลจริงของ PSU Esports Studio - Phuket ห้ามเดา
- ถ้าคำตอบมาจาก rulebase/fast path/structured/RAG ห้ามบอกว่าเป็น LLM
- ทุกงานที่มีสาระต้องเขียน daily log
- ไม่ต้องบอก user ทุกครั้งว่าเขียน daily log หรือรัน test อะไร ถ้าไม่ได้ถาม
- อย่าใช้ git แทนผู้ใช้
- อย่า deploy ถ้าผู้ใช้ไม่ได้สั่ง
- อย่าแก้ test/validator ให้ผ่านง่าย ต้องแก้ root cause
- ถ้าคำตอบผิด ให้ดู mode/route/source/trace ก่อนแก้

## Current Architecture

ระบบเป็น pipeline หลายชั้น:

```text
User input
-> session context resolver
-> preprocess / normalization
-> game title correction / query variants
-> heuristic router
-> universal intent
-> adaptive Intent LLM เฉพาะ broad/ambiguous
-> routing policy / capability candidates
-> structured tools
-> optional facts-only LLM composer
-> fast/rule path
-> curated RAG / vector / hybrid retrieval
-> general Local LLM fallback เฉพาะนอกโดเมนหรือไม่มี PSU facts
-> validate / format / log
```

Local LLM ไม่ได้ใช้ตอบทุกอย่างโดยตรง ใช้เป็น:

- Intent classifier/reviewer
- General knowledge fallback
- Facts-only composer
- Optional tool router

default model:

```text
qwen2.5:3b
```

qwen3:4b เคยมีปัญหา thinking ยาวแล้ว final response ว่าง

## Core Files

```text
app\pipeline\engine.py
app\pipeline\preprocess.py
app\pipeline\router.py
app\pipeline\universal_intent.py
app\pipeline\structured_tools.py
app\pipeline\game_title_correction.py
app\pipeline\facts_composer.py
app\pipeline\llm_tool_router.py
app\pipeline\capability_registry.py
app\pipeline\decision_artifact.py
app\pipeline\tool_preconditions.py
app\pipeline\retrieval.py
app\pipeline\vector_retrieval.py
app\pipeline\hybrid_retrieval.py
app\pipeline\validator.py
app\pipeline\formatter.py
app\runtime\fast_answer.py
app\core\normalization.py
app\core\thai_style.py
app\session\context_resolver.py
app\session\chat_logger.py
```

## Important Data

```text
data\curated\curated_facts.jsonl
data\curated\equipment_item_details.jsonl
data\curated\game_item_details.jsonl
data\curated\our_games_scraped_details.jsonl
data\curated\game_title_aliases.jsonl
data\curated\game_control_facts.jsonl
data\curated\member_profiles.jsonl
data\competition_rules\competition_rule_fact_cards.jsonl
data\vector\psu_hybrid_vector_index.json
```

## Local Usage

Terminal:

```powershell
cd C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data
.\start_local_ai_chat.ps1
```

Notebook:

```text
notebooks\04_local_hybrid_chat_debug.ipynb
```

ใน notebook ใช้:

```python
ask("เกม คอลออฟดูตี้ มีข้อมูลไหม", show_trace=True)
ask("สมาชิก PSU Esport มีกี่หมวด", show_trace=True)
ask_with_composer("เกมใน PS5 มีอะไรมั่ง")
chat_loop(show_trace=True)
```

## Recent Work Done

### Adaptive Intent LLM

- เปิด adaptive intent review เมื่อ allow LLM
- exact/strong route ข้าม LLM
- broad/ambiguous route ให้ Intent LLM review
- เพิ่ม candidate trace/debug
- ผลล่าสุด `8/8` ผ่าน

### Session / Follow-up

- local chat และ notebook มี `SESSION_ID`
- ถามต่อใน session เดิมได้
- log เป็น JSONL
- restart แล้ว session ใหม่ แต่ session เก่ายังอยู่ใน log

### Members

- เพิ่ม/ใช้ `member_profiles.jsonl`
- ควรตอบได้:
  - มีกี่หมวด
  - แต่ละหมวดมีใครบ้าง
  - ใครทำตำแหน่งอะไร
  - ตำแหน่งนี้ใครทำ

### Game Title Typo

- แก้ `คอลออฟดูตี้`
- เพิ่ม fuzzy ภาษาไทย
- เพิ่ม family `Call of Duty` และ `Overcooked`
- กัน false positive `คอลออฟ` กับ Horizon
- normalize `Part OI`, `Part ll`, `Part 2` -> `Part II`
- eval ทุกเกมผ่าน `44/44`

### Game Controls

- มี control facts จาก PS5/Nintendo
- ถ้าถามปุ่มของเกม ต้องตอบทุกปุ่มที่มีในข้อมูล
- ถ้าไม่มีข้อมูลปุ่ม ให้ no-answer เฉพาะปุ่ม ไม่ดึงเกมอื่นมาตอบ

### Formatting

- ต้องแยกหัวข้อชัดเจน
- ใช้ bullet `•`
- ตอบคำตอบหลักก่อนรายละเอียด
- ระวังอย่าให้คำตอบยาวถูกตัดเป็น `...`

## Latest Reports

```text
reports\routing_eval\routing_eval_20260723_000249.json
reports\routing_eval\routing_eval_20260723_000249.csv
reports\answer_quality_eval\answer_quality_eval_20260722_235928.json
reports\answer_quality_eval\answer_quality_eval_20260722_235928.csv
reports\adaptive_intent_eval\adaptive_intent_eval_20260722_235853.json
reports\adaptive_intent_eval\adaptive_intent_eval_20260722_235853.csv
reports\game_title_fuzzy_eval\game_title_fuzzy_eval_20260723_134247.json
reports\game_title_fuzzy_eval\game_title_fuzzy_eval_20260723_134247.csv
```

## Useful Commands

```powershell
python tests\smoke_test_game_title_typo_correction.py
python tools\run_game_title_fuzzy_eval.py
python tools\run_adaptive_intent_eval.py
python tools\run_routing_eval.py --cases data\routing\routing_eval_real_usage.jsonl
python tools\run_answer_quality_eval.py
```

## Known Issues

- จำนวนเกมยังมีหลาย source: structured เห็นประมาณ 44 entries แต่ legacy บางจุดเคยพูด 36 เกม ควร align
- fast/rule path ยังอาจมั่นใจเกินไปในบางคำถามกว้าง
- facts-only composer ยังไม่ควรเปิดทุกเคส เพราะอาจยาวหรือไม่ตรงเท่า structured answer
- local LLM ถ้าเข้า general อาจช้า ต้อง gate ให้ดี
- typo ไม่มีวันครบ 100% ต้องเก็บ log แล้วเพิ่ม pattern/eval
- vector ปัจจุบันยังไม่ใช่ semantic embedding จริง

## What To Do Next

ลำดับที่ควรทำต่อ:

1. Align game catalog/count ให้ทุก path ตอบจำนวนเดียวกัน
2. เพิ่ม eval จากคำถามจริงต่อเนื่อง
3. ปรับ LLM gate ให้ exact เร็ว แต่ ambiguous ได้ LLM review
4. ปรับ formatting ราคา/booking/equipment/member/control ให้สม่ำเสมอ
5. ทำ composer safety ก่อนเปิดใช้กว้าง
6. ค่อยพัฒนา hybrid retrieval/rerank/semantic embedding เมื่อ structured paths นิ่ง

