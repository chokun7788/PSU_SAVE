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
- run local chatbot
- run notebook
- run smoke/eval
- เก็บ reports จากการทดสอบ

## Daily Logs

```text
C:\Users\Chokhun\Downloads\Learn-LLM\17_PSU_Esports_Daily_Logs
```

ใช้เก็บบันทึกรายวันว่าวันนั้นทำอะไร พบปัญหาอะไร แก้อะไร และผลทดสอบเป็นอย่างไร

## Current Handoff Folder

```text
C:\Users\Chokhun\Downloads\Learn-LLM\23_PSU_Esports_Handoff_Summary_20260723
```

ใช้เป็น handoff ล่าสุดสำหรับเปิดแชทใหม่

## Older Handoff Folders

```text
C:\Users\Chokhun\Downloads\Learn-LLM\21_PSU_Esports_Handoff_Summary_20260705
C:\Users\Chokhun\Downloads\Learn-LLM\22_PSU_Esports_Handoff_Summary_20260711
```

ใช้ดูประวัติ/แนวคิดเดิมได้ แต่สถานะล่าสุดให้ยึด folder 23 เป็นหลัก

## Local Chat Entry Points

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\start_local_ai_chat.ps1
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\tools\local_ai_chat.py
```

ใช้เปิด terminal chat แบบ local มี session id, history, trace, local LLM, intent LLM, optional composer

## Notebook สำคัญ

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\notebooks\04_local_hybrid_chat_debug.ipynb
```

ใช้ถามทดลองแบบ interactive ใน notebook:

- มี `SESSION_ID` / `SECTION_ID`
- มี `ask(...)`
- มี `ask_with_composer(...)`
- มี `chat_loop(...)`
- log ไปที่ `reports\local_hybrid_chat_debug`

Notebook อื่น:

```text
notebooks\03_user_question_bank_eval.ipynb
notebooks\02_test_final_pipeline.ipynb
```

ใช้ดู/ทดสอบชุดคำถามและ ground truth เก่า

## Core Pipeline Files

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
```

หน้าที่หลัก:

- `engine.py`: pipeline หลัก ตั้งแต่ preprocess ถึง output
- `preprocess.py`: normalize query, build variants, apply game title correction
- `router.py`: heuristic route/category/intent เดิม
- `universal_intent.py`: intent layer ใหม่ แยก domain/operation/target และใช้ Intent LLM review ได้
- `structured_tools.py`: structured answers สำหรับ members, games, controls, equipment, reservation, schedule, service fee
- `game_title_correction.py`: fuzzy title correction สำหรับชื่อเกม ภาษาอังกฤษ/ไทย/ภาษาวิบัติ
- `facts_composer.py`: optional LLM composer ที่เรียบเรียงจาก facts เท่านั้น
- `llm_tool_router.py`: optional tool router ให้ LLM ช่วยเลือก tool/capability
- `capability_registry.py`: registry ของ capability/candidate
- `decision_artifact.py`: trace เหตุผลว่ารับ/ปฏิเสธ candidate ไหน
- `tool_preconditions.py`: guard ก่อนเรียก structured tool
- `retrieval.py`: curated retrieval และ competition fact cards
- `vector_retrieval.py`: local vector/hash char n-gram retrieval และ game control retrieval
- `hybrid_retrieval.py`: guarded hybrid retrieval/rerank
- `validator.py`: validate answer
- `formatter.py`: format answer/no-answer/source

## Runtime / Rule / Normalization

```text
app\runtime\fast_answer.py
app\runtime\pipeline_answer.py
app\core\normalization.py
app\core\thai_style.py
app\rules\matcher.py
```

หน้าที่:

- `fast_answer.py`: fast/rule answer สำหรับราคา เวลา วิธีจอง เกม อุปกรณ์ กฎพื้นฐาน
- `pipeline_answer.py`: wrapper ที่ local tools/notebook ใช้เรียก pipeline
- `normalization.py`: normalize, alias, typo, keyboard-layout variants, fuzzy helper
- `thai_style.py`: post-process formatting ภาษาไทย
- `matcher.py`: rule matcher

## Session / Memory

```text
app\session\context_resolver.py
app\session\chat_logger.py
```

หน้าที่:

- `context_resolver.py`: resolve follow-up จาก history เช่น ถามเกมก่อน แล้วถามต่อว่า “มีปุ่มอะไรบ้าง”
- `chat_logger.py`: log session/local chat

## Important Data Files

Curated facts:

```text
data\curated\curated_facts.jsonl
data\curated\equipment_item_details.jsonl
data\curated\game_item_details.jsonl
data\curated\our_games_scraped_details.jsonl
data\curated\game_title_aliases.jsonl
data\curated\game_control_facts.jsonl
data\curated\member_profiles.jsonl
```

Competition:

```text
data\competition_rules\competition_rule_fact_cards.jsonl
data\curated\curated_competition_rules.jsonl
```

Game control source/split:

```text
data\control_game
data\control_game_split\ps5
data\control_game_split\nintendo
```

Vector index:

```text
data\vector\psu_hybrid_vector_index.json
```

## Important Tools

```text
tools\run_routing_eval.py
tools\run_answer_quality_eval.py
tools\run_adaptive_intent_eval.py
tools\run_game_title_fuzzy_eval.py
tools\generate_real_usage_eval_cases.py
tools\build_game_control_facts.py
tools\build_vector_index.py
tools\run_user_question_bank_eval.py
```

หน้าที่:

- `run_routing_eval.py`: วัด route/mode ของคำถามใช้งานจริง
- `run_answer_quality_eval.py`: วัด answer quality แบบ expected substrings
- `run_adaptive_intent_eval.py`: วัดว่า exact route ข้าม LLM และ ambiguous route ให้ Intent LLM review
- `run_game_title_fuzzy_eval.py`: วัด typo/fuzzy ชื่อเกมทุกเกม
- `generate_real_usage_eval_cases.py`: generate routing/answer cases
- `build_game_control_facts.py`: build control facts จาก JSON ต้นทาง
- `build_vector_index.py`: build vector index
- `run_user_question_bank_eval.py`: รัน question bank ที่สร้างไว้

