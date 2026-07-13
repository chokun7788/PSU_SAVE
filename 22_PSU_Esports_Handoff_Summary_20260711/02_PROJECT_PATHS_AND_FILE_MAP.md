# Project Paths And File Map

## Root

```text
C:\Users\Chokhun\Downloads\Learn-LLM
```

## Main Source Folder

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data
```

ใช้สำหรับ:

- แก้โค้ดหลัก
- เพิ่ม curated data
- build vector index
- run local smoke test
- run compile/validate

## Deploy Folder

```text
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy
```

ใช้สำหรับ:

- deploy ขึ้น Vercel
- เป็น copy ที่ต้อง sync จาก folder 18
- ก่อน deploy ต้องแน่ใจว่าไฟล์ใหม่จาก 18 ถูกคัดลอกมาครบ

Production URL:

```text
https://psu-esports-chatbot.vercel.app
```

## Daily Logs

```text
C:\Users\Chokhun\Downloads\Learn-LLM\17_PSU_Esports_Daily_Logs
```

ใช้เก็บบันทึกรายวันว่าวันนั้นทำอะไร แก้ไฟล์ไหน ทดสอบอะไร และยังไม่ได้ทำอะไร

## Handoff Folders

Handoff เดิม:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\21_PSU_Esports_Handoff_Summary_20260705
```

Handoff ล่าสุด:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\22_PSU_Esports_Handoff_Summary_20260711
```

ให้ใช้ folder 22 เป็นหลัก เพราะรวมสถานะล่าสุดหลังเพิ่ม game control JSONL/vector แล้ว

## Core Code Files

ใน folder 18:

```text
app\pipeline\engine.py
app\pipeline\router.py
app\pipeline\retrieval.py
app\pipeline\vector_retrieval.py
app\pipeline\hybrid_retrieval.py
app\pipeline\validator.py
app\pipeline\formatter.py
app\pipeline\preprocess.py
app\runtime\fast_answer.py
app\core\normalization.py
app\core\thai_style.py
```

หน้าที่โดยย่อ:

- `engine.py`: flow หลักของ pipeline ตั้งแต่ preprocess, route, fast path, retrieval, vector, validation, fallback
- `router.py`: จัด route/category/intent ของคำถาม
- `retrieval.py`: curated retrieval และ competition fact card retrieval
- `vector_retrieval.py`: guarded vector retrieval, local hash char ngram backend, game control vector logic
- `hybrid_retrieval.py`: hybrid retrieval/rerank สำหรับข้อมูลที่เสี่ยงตอบมั่ว
- `validator.py`: validate คำตอบก่อนปล่อย
- `formatter.py`: format answer/no-answer/source
- `fast_answer.py`: rulebase/fast path หลัก เช่น ราคา เวลาเปิด เกม อุปกรณ์ booking
- `normalization.py`: normalize ข้อความ, fuzzy/alias helper
- `thai_style.py`: post-process ภาษาไทย

## Important Data Files

Curated data:

```text
data\curated\curated_facts.jsonl
data\curated\equipment_item_details.jsonl
data\curated\game_item_details.jsonl
data\curated\our_games_scraped_details.jsonl
data\curated\game_title_aliases.jsonl
data\curated\game_control_facts.jsonl
```

Competition rules:

```text
data\competition_rules\competition_rule_fact_cards.jsonl
data\curated\curated_competition_rules.jsonl
```

Game control source:

```text
data\control_game\nintendo
```

หมายเหตุ: ชื่อ folder เดิมคือ `nintendo` แต่ข้างในมีข้อมูลทั้ง Nintendo Switch และ PS5

Game control split ล่าสุด:

```text
data\control_game_split\ps5
data\control_game_split\nintendo
```

Vector index:

```text
data\vector\psu_hybrid_vector_index.json
```

## Build Scripts

```text
tools\build_vector_index.py
tools\build_game_control_facts.py
```

หน้าที่:

- `build_vector_index.py`: สร้าง `data/vector/psu_hybrid_vector_index.json` จาก curated JSONL
- `build_game_control_facts.py`: อ่าน JSON ต้นทางของปุ่มควบคุมเกม แล้วสร้าง JSONL แยก PS5/Nintendo และ curated รวม

## Test/Notebook

Notebook หลักที่เคยใช้:

```text
notebooks\02_test_final_pipeline.ipynb
```

ผู้ใช้บอกว่าเวลาจะ run Ground Truth มีไฟล์สำหรับเช็คอยู่แล้ว ให้ run จากไฟล์นั้น ไม่ต้องอ่านผลยาว ๆ เองทุกครั้งถ้าไม่จำเป็น

