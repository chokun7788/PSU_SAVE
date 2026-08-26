# PSU Esports Chatbot: Pipeline 1-8 Implementation Detail

วันที่จัดทำ: 23/08/2026

เอกสารนี้อธิบายการแก้ Pipeline 8 เรื่องจากผลวิเคราะห์ benchmark 1,600 ข้อ โดยเน้นว่าแต่ละส่วนรับอะไร ตัดสินอย่างไร ส่งต่อไปไหน ใช้หรือไม่ใช้ Local LLM/RAG อย่างไร ตรวจคำตอบอย่างไร และมีหลักฐานทดสอบอะไร

เอกสาร Flow รวมที่ใช้เป็นฐานอ้างอิงคือ `docs/40_current_chatbot_full_process_flow_20260807.md` ส่วนเอกสารนี้เจาะเฉพาะ behavior ที่แก้และยืนยันในวันที่ 23/08/2026

## 1. เป้าหมายและขอบเขต

เป้าหมายหลักมี 4 ข้อ:

1. ถาม A ต้องตอบ A โดยลด wrong route, wrong intent และ wrong target
2. ข้อมูล PSU ต้องมาจาก evidence ที่ยืนยันได้ ห้ามให้ LLM เดา
3. คำถามทั่วไปที่เหมาะกับ LLM ต้องไม่เสีย call ไปกับ intent review ที่ไม่จำเป็น
4. Backend ต้องพยายามจบภายใน 9 วินาที เพื่อเหลือประมาณ 1 วินาทีสำหรับ network/API และรักษา user-visible target ไม่เกิน 10 วินาที

สิ่งที่ Pipeline 1-8 ชุดนี้ยังไม่แก้:

- ยังไม่ทำ distributed queue สำหรับหลาย process
- ยังไม่ทำ booking transaction
- ยังไม่เพิ่ม live news provider
- ยังไม่เปลี่ยน local hash vector เป็น semantic embedding เต็มรูปแบบ
- ยังไม่ทำ multi-user load test 20 users พร้อมกัน

## 2. ภาพรวม Flow หลังแก้

```text
User Input
  -> Request Deadline + LLM Call Budget
  -> Split Multi-question + Complexity Gate
  -> Preprocess / Normalize / Query Variants
  -> Route + Entity + Target Resolution
  -> Freshness / Boundary / Scope Guards
  -> Model Gateway Preflight
  -> Universal Intent
  -> Ambiguity Gate + Question Frame
  -> Candidate Scoring + Tool Preconditions
  -> Execution
       Fast / Rule / Calculator
       Structured Tool
       Fact Card / Guarded Retrieval / Optional RAG
       General Local LLM
  -> Format + Validate + Answer Contract
  -> Bounded Repair
  -> Final Hard Veto
  -> Final Answer + Trace + Timing + LLM Call Ledger
```

ตำแหน่งของ Pipeline 1-8:

| หมายเลข | เรื่องที่แก้ | ตำแหน่งหลักใน Flow |
|---:|---|---|
| 1 | Request state initialization | ก่อนเริ่ม single-question execution |
| 2 | Context-aware lexical signals | Preprocess, entity, route, ambiguity, validation |
| 3 | General definition vs PSU inventory | Router, Universal Intent, Question Frame, Tool Preconditions |
| 4 | ASCII token boundary | Routing policy, control/entity matching |
| 5 | Deterministic game-zone ranking | Router ถึง Structured Games |
| 6 | Dynamic freshness guard | หลัง route/entity และก่อน optional LLM/RAG |
| 7 | Clear-general one-call path | Model Gateway, Universal Intent, General fallback |
| 8 | Adaptive generation/output budget | General Local LLM และ output contract |

## 3. Pipeline 1: Request State Initialization

### 3.1 ปัญหาเดิม

บาง early-return หรือ fallback branch อ่านค่า `rag_llm_attempted` และ `rag_source_conflict` ก่อนมีการกำหนดค่า ทำให้เกิด `UnboundLocalError` สองเคสใน benchmark เดิม คำถามจึงไม่ได้คำตอบ แม้ source และ route ส่วนอื่นจะทำงานได้

นี่เป็น control-flow bug ไม่ใช่ปัญหาของ model และไม่ควรแก้ด้วยการเปลี่ยน expected result

### 3.2 Input contract

ทุก single question ต้องเริ่มด้วย state ที่แน่นอน:

- `started`: เวลาเริ่ม request/child
- `trace`: trace ที่รับต่อจาก parent compound หรือ list ว่าง
- `rag_llm_attempted = False`
- `rag_source_conflict = False`
- deadline context และ LLM budget จาก parent request

### 3.3 ขั้นตอนทำงาน

1. `_answer_single()` สร้าง state ก่อน preprocess
2. ถ้าเป็น child ของ compound ให้ reuse `pipeline_started` และ `initial_trace` ตาม contract
3. ทุก branch อ่าน state ชุดเดียวกัน
4. เมื่อ RAG composer ถูกลอง จึงเปลี่ยน `rag_llm_attempted` เป็นจริง
5. เมื่อ Source Guard พบ conflict จึงเปลี่ยน `rag_source_conflict` เป็นจริง
6. Experimental fallback ตรวจสองค่านี้ก่อนอนุญาต LLM เพื่อป้องกัน duplicate call

### 3.4 เหตุผลที่ต้อง initialize ก่อน preprocess

Preprocess, route, boundary, freshness และ ambiguity สามารถ early return ได้ทั้งหมด หาก state ถูกสร้างกลางฟังก์ชัน branch ที่ข้ามจุดนั้นอาจอ่านตัวแปรที่ไม่มีค่า การกำหนด state ที่ entry point ทำให้ทุก path มี invariant เดียวกัน

### 3.5 ตัวอย่าง

Input:

```text
คำถามที่ route ไม่ชัดและ structured tool ไม่ได้ผล
```

Behavior:

```text
state=False/False
  -> preprocess
  -> route
  -> structured miss
  -> retrieval/fallback decision
  -> อ่าน state ได้เสมอ
  -> no exception
```

### 3.6 Fallback และ safety

- ถ้า RAG LLM ถูกลองแล้ว Experimental fallback ต้องไม่เรียก LLM ซ้ำ
- ถ้ามี source conflict ต้องไม่ให้ LLM เรียบเรียงเพื่อกลบ conflict
- ถ้า state ไม่เปลี่ยน แปลว่ายังไม่มี expensive/grounded LLM attempt

### 3.7 Trace ที่เกี่ยวข้อง

- `preprocess`
- `model_gateway`
- `rag_model_plan`
- `facts_composer`
- `experimental_rag_fallback`
- `build_result`

### 3.8 ไฟล์และ test

- `app/pipeline/engine.py`
- `tests/smoke_test_pipeline_fixes_20260823.py::test_request_state_is_initialized_on_all_single_paths`

ผล: test ผ่าน และ full 1,600 รอบล่าสุดไม่มี `UnboundLocalError` หรือคำตอบว่างจาก exception

## 4. Pipeline 2: Context-aware Lexical Signals

### 4.1 ปัญหาเดิม

ระบบเดิมใช้ substring กว้างเกินไป เช่นคำว่า `เสีย` เป็น price signal ทำให้:

- `ข้อเสียของ API` ถูกตีความเป็นคำถามราคา
- `ข้อดีข้อเสีย` วิ่งไป Service Fee
- route, entity.price_intent, ambiguity candidate และ validator ผิดพร้อมกัน

การแก้เฉพาะ Router ไม่พอ เพราะ signal เดียวกันถูกใช้หลาย stage

### 4.2 หลักการใหม่

สร้าง shared query signals ใน `query_signals.py` แล้วให้ทุก stage ใช้ความหมายเดียวกัน

Price amount ต้องมี phrase ที่สื่อถึงจำนวนเงินจริง เช่น:

- ราคา
- ค่าบริการ
- ค่าใช้จ่าย
- กี่บาท
- เท่าไหร่
- เสียเงิน
- เสียกี่บาท
- ต้องจ่าย
- service fee / price / cost

คำว่า `เสีย` เดี่ยว ๆ ไม่ใช่ price signal

### 4.3 ขั้นตอนทำงาน

1. Normalize query
2. ตรวจ signal ด้วย `looks_like_price_amount_query()`
3. Entity resolver ตั้ง `price_intent` เฉพาะเมื่อ phrase contract ผ่าน
4. Router ใช้ผลเดียวกันก่อนเลือก Service Fee
5. Ambiguity Gate ไม่เพิ่ม price candidate จากคำว่า `ข้อเสีย`
6. Tool Preconditions ไม่เปิด calculator หากไม่มี amount/fee intent
7. Validator ไม่บังคับ price answer contract กับคำถามทั่วไป

### 4.4 ตัวอย่างเปรียบเทียบ

| Input | Price signal | Route ที่ต้องการ |
|---|---:|---|
| `PS5 ราคาเท่าไหร่` | จริง | service_fee |
| `เล่น VR เสียกี่บาท` | จริง | service_fee |
| `API มีข้อเสียอะไร` | เท็จ | general |
| `ข้อดีข้อเสียของ JSON` | เท็จ | general |
| `ทำเมาส์เสียต้องทำยังไง` | เท็จ | penalty/rules |

### 4.5 ทำไมไม่ใช้ regex คำเดียว

ภาษาไทยไม่มี word boundary แบบช่องว่างที่เสถียรทุกกรณี และคำสั้นสามารถอยู่ในคำยาว การใช้ allowlist ของ phrase ที่มีความหมายครบลด false positive โดยไม่ต้องเดาความหมายจาก substring

### 4.6 Failure behavior

หาก query ไม่มี price phrase:

- calculator candidate ถูก reject
- structured service-fee tool ไม่ควรถูก execute
- คำถามยังเดินต่อไป General, Rules หรือ domain ที่มี evidence

### 4.7 Trace ที่ควรตรวจเมื่อผิด

- `entities.price_intent`
- `router category/intent`
- `decision_candidates`
- `tool_precondition`
- `validation`

### 4.8 ไฟล์และ test

- `app/pipeline/query_signals.py`
- `app/pipeline/entity_resolver.py`
- `app/pipeline/router.py`
- `app/pipeline/ambiguity_gate.py`
- `app/pipeline/tool_preconditions.py`
- `app/pipeline/validator.py`
- `tests/smoke_test_pipeline_fixes_20260823.py::test_price_signal_uses_phrase_context`

## 5. Pipeline 3: General Definition vs PSU Inventory

### 5.1 ปัญหาเดิม

คำถามเชิงแนวคิด เช่น:

```text
mechanical keyboard คืออะไร
คีย์บอร์ด mechanical มีข้อดีข้อเสียอะไร
```

มีคำว่า `keyboard/คีย์บอร์ด` ซึ่งชน equipment inventory ทำให้ระบบตอบรุ่นคีย์บอร์ดที่ศูนย์แทนคำจำกัดความ

### 5.2 การแยก intent

General concept definition ต้องมีครบ:

1. concept term ที่รองรับ
2. definition/comparison term เช่น `คืออะไร`, `อธิบาย`, `ต่างกันยังไง`
3. ไม่มี PSU inventory signal

Inventory signal เช่น:

- PSU / ศูนย์ / ร้าน / ที่นี่
- มีรุ่นอะไร
- ใช้รุ่นอะไร
- มีกี่เครื่อง
- อยู่โซนไหน
- อุปกรณ์ในศูนย์

### 5.3 Operation-first routing

ระบบให้ operation สำคัญกว่าคำนามกว้าง:

```text
คำนาม: keyboard
operation: definition
PSU scope: ไม่มี
=> general/detail
```

แต่:

```text
คำนาม: keyboard
operation: inventory lookup
PSU scope: มี "ที่ศูนย์"
=> equipment/equipment_item_lookup
```

### 5.4 Defense in depth

ไม่ได้พึ่ง Router จุดเดียว:

1. Router เลือก general ก่อน known equipment
2. Universal Intent lock เป็น `general/detail`
3. Question Frame สร้าง expected answer type เป็น general definition
4. Ambiguity Gate ไม่เพิ่ม equipment candidate
5. Tool Preconditions veto `structured.equipment`
6. Candidate Scoring จึงไม่สามารถเลือก inventory tool ได้

### 5.5 ตัวอย่าง

| Input | Route | Tool |
|---|---|---|
| `mechanical keyboard คืออะไร` | general/detail | General LLM |
| `คีย์บอร์ด mechanical ต่างจาก membrane ยังไง` | general/detail | General LLM |
| `คีย์บอร์ดที่ศูนย์ใช้รุ่นอะไร` | equipment/item | Structured Equipment |
| `PC Zone มีคีย์บอร์ดกี่ชุด` | equipment/list/count | Structured Equipment |

### 5.6 LLM policy

General definition ใช้ Local LLM ได้ เพราะไม่ใช่ข้อเท็จจริงเฉพาะ PSU แต่คำถาม inventory ต้องใช้ structured evidence และห้ามให้ General LLM เดารุ่น/จำนวน

### 5.7 Trace ที่ควรได้

General:

- route `general/general_knowledge_query`
- universal intent `general/detail`
- preflight intent LLM ถูก skip
- final `pipeline:general_llm_fallback`

Inventory:

- route `equipment/...`
- target เป็น equipment ที่ยืนยันได้
- selected capability `structured.equipment`
- final `pipeline:structured_equipment_item` หรือ catalog

### 5.8 ไฟล์และ test

- `app/pipeline/query_signals.py`
- `app/pipeline/router.py`
- `app/pipeline/universal_intent.py`
- `app/pipeline/question_frame.py`
- `app/pipeline/ambiguity_gate.py`
- `app/pipeline/tool_preconditions.py`
- `tests/smoke_test_pipeline_fixes_20260823.py::test_general_definition_does_not_use_psu_equipment_inventory`

## 6. Pipeline 4: ASCII Token Boundary for Entity and Controls

### 6.1 ปัญหาเดิม

คำว่า `cross` เป็นชื่อปุ่ม/ทิศทางในบาง control aliases แต่เป็น substring ภายในชื่อ `Animal Crossing` ระบบจึงอาจคิดว่าผู้ใช้ถามปุ่ม Cross ทั้งที่กำลังถามชื่อเกม

### 6.2 วิธีแก้

ใช้ `contains_ascii_bounded()`:

```text
(?<![a-z0-9])TERM(?![a-z0-9])
```

ASCII term ต้องอยู่เป็น token ที่มีขอบเขต ไม่ใช่อยู่กลางคำภาษาอังกฤษ

ภาษาไทยยังใช้ substring matching เพราะการเว้นวรรคไม่สม่ำเสมอ แต่คำเสี่ยงต้องมี signal/phrase เฉพาะตาม Pipeline 2

### 6.3 ตัวอย่าง

| Query | term=`cross` | ผล |
|---|---:|---|
| `Animal Crossing มีใน Switch ไหม` | ไม่ match | game availability |
| `กด cross เพื่อยืนยันใช่ไหม` | match | control lookup |
| `ปุ่ม X / Cross ทำอะไร` | match | control lookup |

### 6.4 จุดที่ใช้

- Routing priority matrix
- game/control intent detection
- target/entity cross-check
- operation signals ที่เป็น English token

### 6.5 ทำไม boundary ต้องอยู่ shared helper

ถ้า Router ใช้ boundary แต่ Ambiguity Gate ยังใช้ substring ผลอาจขัดกัน เช่น Router บอก game availability แต่ candidate scorer เพิ่ม control candidate การใช้ helper เดียวกันลด route-intent conflict

### 6.6 Failure behavior

เมื่อไม่มี control token จริง:

- control tool precondition ต้องไม่ผ่านเพียงเพราะชื่อเกม
- game title resolver ยัง resolve `Animal Crossing` ได้
- คำถามไป availability/detail ตาม operation

### 6.7 ไฟล์และ test

- `app/pipeline/query_signals.py`
- `app/pipeline/routing_policy.py`
- `app/pipeline/entity_resolver.py`
- `tests/smoke_test_pipeline_fixes_20260823.py::test_ascii_control_token_does_not_match_inside_game_title`

## 7. Pipeline 5: Deterministic Game-zone Ranking

### 7.1 ปัญหาเดิม

คำถาม:

```text
โซนไหนมีเกมเยอะที่สุด
จัดอันดับจำนวนเกมตามโซน
```

มีคำว่า `โซน/เครื่อง` จึงอาจถูก route เป็น equipment หรือให้ LLM ตีความกว้าง ทั้งที่ข้อมูลจำนวนเกมคำนวณตรงจาก catalog ได้

### 7.2 Signal contract

ต้องมีอย่างใดอย่างหนึ่ง:

- phrase ตรง เช่น `เกมเยอะสุด`, `จำนวนเกมตามโซน`
- หรือมีครบ game term + ranking operation + zone/equipment target term

### 7.3 ขั้นตอนทำงาน

1. Router ตรวจ ranking ก่อน equipment
2. Route เป็น `games/game_zone_rank` confidence 0.99
3. Universal Intent เป็น `games/list` target `game_zone_counts`
4. Model Gateway/Intent Review veto optional intent LLM
5. Question Frame เป็น `game_zone_rank`
6. Candidate Scoring ให้ `structured.games` เป็น candidate หลัก
7. Tool Preconditions อนุญาต games และ veto equipment
8. Structured tool สร้าง mapping `zone -> unique game count`
9. Sort ตามมากสุด/น้อยสุด
10. ถ้าเสมอกัน รายงานทุก zone ที่เสมอ
11. แนบ source ของ current game catalog

### 7.4 Pseudocode

```text
grouped = games_by_zone(current_catalog)
counts = {zone: len(unique_games)}
ascending = query asks "น้อยสุด"
ordered = sort(counts, count then zone)
best = all zones whose count equals top count
render answer + per-zone counts + source
```

### 7.5 เหตุผลที่ไม่ใช้ LLM

- เป็นการนับและ sort ที่ deterministic
- LLM อาจนับผิด เพิ่ม/ลบเกม หรือเลือก zone ผิด
- Structured output ตรวจซ้ำและ reproduce ได้
- ลด latency และ LLM call

### 7.6 Output contract

ต้องมี:

- zone ที่มากสุด/น้อยสุด
- จำนวนเกม
- ตาราง/รายการจำนวนตามโซน
- source

ห้ามมี:

- เกมที่ไม่มีใน current catalog
- ตัวเลขจากความจำของ model

### 7.7 ไฟล์และ test

- `app/pipeline/query_signals.py`
- `app/pipeline/router.py`
- `app/pipeline/universal_intent.py`
- `app/pipeline/question_frame.py`
- `app/pipeline/tool_preconditions.py`
- `app/pipeline/structured_tools.py::_game_zone_ranking_answer`
- `tests/smoke_test_pipeline_fixes_20260823.py::test_game_zone_ranking_is_deterministic_structured_path`

## 8. Pipeline 6: Dynamic Freshness Guard

### 8.1 ปัญหาเดิม

คำถามอย่าง:

```text
วันนี้เพลงอะไรฮิตล่าสุด
ข่าว esports ล่าสุดคืออะไร
ราคาทองตอนนี้เท่าไหร่
```

อาจเข้า General LLM แล้วตอบจาก model memory ซึ่งไม่ใช่ live evidence และอาจเก่า

### 8.2 เงื่อนไขสองแกน

Freshness Guard ต้องพบทั้ง:

1. เวลาแบบ dynamic เช่น ล่าสุด, ตอนนี้, วันนี้, current, latest
2. topic ที่เปลี่ยนตามเวลา เช่น ข่าว, เพลงฮิต, คะแนน, ผลแข่ง, หุ้น, ทอง, อากาศ, ผู้ดำรงตำแหน่ง

การใช้ conjunction ป้องกัน false positive:

- `วันนี้ศูนย์เปิดไหม` เป็น calendar/schedule ของ PSU ไม่ใช่ generic live news
- `อธิบายคำว่า current` ไม่ใช่ freshness query

### 8.3 ขั้นตอนทำงาน

1. Preprocess และ route/entity ทำงานก่อนเพื่อรู้ domain
2. `evaluate_freshness_requirement()` ตรวจ dynamic time + dynamic topic
3. หากต้องใช้ live evidence แต่ยังไม่มี provider ที่มี `live_evidence=true` และ `retrieved_at`:
   - หยุดก่อน Universal Intent LLM
   - ไม่ใช้ General LLM
   - ไม่ใช้ stale RAG document เป็นคำตอบปัจจุบัน
   - คืน no-answer ที่อธิบายว่าไม่มีแหล่งสด
4. เมื่ออนาคตมี live provider Source Guard ต้องตรวจ timestamp ก่อนอนุญาต answer

### 8.4 ทำไมต้องอยู่ก่อน LLM/RAG

การ validate หลัง model ตอบไม่สามารถพิสูจน์ได้ว่าข่าว/ราคาเป็นปัจจุบัน หากไม่มี timestamp การหยุดก่อน expensive call ทั้งเร็วกว่าและปลอดภัยกว่า

### 8.5 Output

ตัวอย่าง:

```text
ตอนนี้ยังไม่มีแหล่งข้อมูลสดที่ใช้ยืนยันคำตอบปัจจุบันสำหรับเรื่องนี้ครับ
จึงไม่ควรระบุชื่อหรือข้อมูลล่าสุดจากความรู้เดิม เพราะอาจไม่ตรงกับสถานการณ์ตอนนี้
```

### 8.6 Trace

- `freshness_guard.requires_live_evidence`
- route `no_answer/freshness_live_source_required`
- warning `live_freshness_evidence_unavailable`
- LLM calls = 0

### 8.7 ไฟล์และ test

- `app/pipeline/query_signals.py`
- `app/pipeline/engine.py`
- `app/pipeline/validator.py`
- `tests/smoke_test_pipeline_fixes_20260823.py::test_dynamic_freshness_requires_live_evidence`

## 9. Pipeline 7: Clear-general One-call LLM Path

### 9.1 ปัญหาเดิม

General questions 41 slow cases ใช้สอง LLM calls ต่อเนื่อง:

1. Intent review
2. Final General answer

เวลารวมเฉลี่ยของกลุ่มนี้เดิมประมาณ 14.75 วินาที จึงเกิน product target แม้ final answer call เพียงตัวเดียวจะตอบได้

### 9.2 แนวคิด

คำถาม general ที่ operation ชัดไม่ต้องใช้ LLM เพื่อบอกว่าเป็น general อีกครั้ง ให้ heuristic lock intent แล้วสงวน call เดียวไว้สร้างคำตอบ

Clear-general examples:

- definition
- translation
- short writing
- comparison/tradeoffs
- explanation request ที่ไม่ใช่ PSU-specific

### 9.3 ขั้นตอนทำงาน

1. Router ตรวจ `looks_like_clear_general_request()`
2. Route เป็น `general/general_knowledge_query`
3. `preflight_llm_allowed()` คืน false สำหรับ optional preflight LLM
4. Universal Intent สร้าง heuristic `general/detail`
5. Optional Tool Router ไม่ได้รับอนุญาตให้ใช้ LLM
6. Candidate Scoring เลือก `llm.general_answer`
7. Guard ตรวจซ้ำว่าไม่มี PSU-specific signal
8. General Local LLM ถูกเรียกหนึ่งครั้ง
9. Output contract ตรวจรูปแบบและความครบ
10. เติมหมายเหตุว่าเป็นความรู้ทั่วไปของ model ไม่ใช่ฐาน PSU

### 9.4 ทำไมไม่ใช้ RAG กับ General ทุกข้อ

ฐานเอกสาร PSU อาจดึง context ที่ไม่เกี่ยวข้องกับคำถามทั่วไป เช่น API/JSON/latency ทำให้คำตอบ drift เข้า PSU และเพิ่มเวลา หากไม่มี corpus ทั่วไปที่เชื่อถือได้ General path จึงใช้ model โดยระบุขอบเขตชัด

### 9.5 Gate สำคัญ

General LLM ห้ามใช้เมื่อ:

- query มี PSU/service signal
- ต้องการ live current data
- คำถามขาด input ที่จำเป็น
- deadline เหลือไม่พอ
- LLM health circuit ปิด
- LLM budget หมด
- concurrency slot ไม่พร้อมตาม policy

### 9.6 Missing-input clarification

คำขอ `ช่วยทำการบ้านคณิตให้หน่อย` แต่ไม่มีโจทย์ไม่ควรใช้ LLM สร้างโจทย์เอง ระบบจึงตอบขอสมการ/ตัวเลข/รูปโจทย์ด้วย deterministic clarification และใช้ 0 LLM calls

### 9.7 Health isolation

Failure ของ optional `query_planner`, `universal_intent` หรือ `tool_router` ถูกจำกัดเป็น kind-only circuit ไม่ให้ปิด General answer ทั้ง model

เฉพาะ `preflight` และ `general_llm` เปลี่ยน model-wide health ได้ และ failure จะนับเป็น consecutive เฉพาะภายใน window 30 วินาที ค่าเก่ากว่านั้นไม่ถูกสะสมไปเปิด circuit ในอีกหลายนาทีต่อมา

### 9.8 Context alignment

เส้น Local LLM ใช้:

- model: `scb10x/typhoon2.5-qwen3-4b`
- `num_ctx=3072`
- `keep_alive=10m`

Universal Intent, Query Planner, Tool Router และ General ใช้ context baseline เดียวกัน เพื่อลดการสลับ context configuration ที่อาจทำให้ Ollama setup ใหม่

### 9.9 ผลวัด

Full v3:

- General 275/275 ผ่าน
- Average 1.8534 วินาที
- P95 2.6276 วินาที
- General LLM call average 1,429.58 ms
- General LLM call P95 2,209.21 ms
- General LLM call max 2,856.67 ms
- 275 requests ใช้ General LLM อย่างละ 1 call
- LLM errors 0

### 9.10 ไฟล์และ test

- `app/pipeline/query_signals.py`
- `app/pipeline/model_gateway.py`
- `app/pipeline/universal_intent.py`
- `app/pipeline/experimental_fallback.py`
- `app/pipeline/llm_health.py`
- `tests/smoke_test_pipeline_fixes_20260823.py::test_clear_general_reserves_one_llm_call_for_final_answer`
- `tests/smoke_test_llm_health_circuit_breaker.py`

## 10. Pipeline 8: Adaptive Generation and Output Budget

### 10.1 ปัญหาเดิม

ใช้ `num_predict` เท่ากันทุกคำถามทำให้:

- คำแปลสั้นเสียเวลาเกินจำเป็น
- คำตอบ 1 ประโยคอาจยาว
- tradeoff อาจถูกตัดก่อนมีข้อเสีย
- token-limit output บางครั้งจบกลางประโยคแต่ถูกส่งให้ผู้ใช้

### 10.2 Generation profiles

| Profile | Trigger | Cap | Output contract |
|---|---|---:|---|
| short_creation | ช่วยเขียน/แต่ง/ร่าง | 96 | 1 ประโยค ไม่เกิน 25 คำ |
| definition_with_tradeoffs | ข้อดีข้อเสีย/เปรียบเทียบ | 112 | 3 บรรทัด: คำตอบ/ข้อดี/ข้อเสีย |
| translation | แปลคำว่า/translate | 48 | 1 วลี ไม่เกิน 8 คำ |
| single_sentence | ประโยคเดียว | 64 | 1 ประโยค ไม่เกิน 25 คำ |
| short_bullets | 2 ข้อ/bullet | 96 | 2 bullets เท่านั้น |
| two_sentences | 2 ประโยค | 96 | 2 ประโยคเท่านั้น |
| concise_definition | แบบสั้น/คำจำกัดความ | 96 | ไม่เกิน 2 ประโยค 45 คำ |
| general_concise | ค่าเริ่มต้น | 128 | 1-2 ประโยค ไม่เกิน 35 คำ |

Cap จริงคือ `min(configured_num_predict, profile_cap)` จึงไม่ขยายเกินค่าที่ operator กำหนด

### 10.3 Priority ของ profile

Priority สำคัญเพื่อไม่ให้ trigger สั้นกลบ requirement:

1. งานสร้างข้อความ
2. tradeoff/comparison
3. translation
4. explicit sentence/bullet count
5. concise definition
6. general concise

ตัวอย่าง `แปลคำว่า reservation และอธิบายข้อดีข้อเสีย` ต้องเลือก tradeoff profile เพื่อให้ตอบครบ ไม่ใช่ translation cap 48

### 10.4 Prompt contract

Prompt กำหนด:

- ตอบภาษาไทย answer-first
- ไม่แสดง chain of thought
- คง keyword หลักจากคำถาม
- ห้ามโยงเข้า PSU หากไม่ได้ถาม
- ถ้าขาด fact ที่จำเป็นให้ถามกลับ
- งานสร้างข้อความทั่วไปทำได้โดยไม่แต่งวัน เวลา สถานที่

### 10.5 Ollama call

Payload หลัก:

- streaming = true
- think = false
- temperature = 0.15
- top_p = 0.8
- adaptive `num_predict`
- `num_ctx=3072`
- `keep_alive=10m`
- timeout ถูกบีบด้วย global deadline

### 10.6 Output shaping

หลังรับ stream:

1. รวม response chunks
2. อ่าน provider metadata เช่น `done_reason` และ token counts
3. ตัดส่วนเกินตามจำนวนประโยค/bullet ที่ user ขอ
4. รักษา bounded complete prefix เมื่อ model ถูกตัดด้วย token limit แต่มีส่วนตอบที่สมบูรณ์
5. ตรวจ keyword retention
6. ตรวจ tradeoff coverage
7. ตรวจ sentence/bullet count
8. ปฏิเสธคำตอบที่จบกลางเนื้อหาและไม่มี complete prefix

### 10.7 Bounded repair

Repair ทำได้เฉพาะ:

- เลือก prefix ที่สมบูรณ์
- ตัดประโยค/bullet ส่วนเกิน
- กลับ deterministic/structured draft

Repair ห้าม:

- เพิ่มข้อเท็จจริงใหม่
- เติมราคา เวลา ชื่อเกม หรือกฎ
- เดาคำที่ model ตัดกลาง

### 10.8 Telemetry

ต่อ call เก็บ:

- `llm_kind`
- `llm_model`
- `llm_timeout_sec`
- `llm_num_predict`
- `llm_num_ctx`
- `llm_keep_alive`
- `llm_prompt_chars`
- `llm_elapsed_ms`
- `ollama_load_duration`
- `ollama_eval_duration`
- generation profile
- output contract result
- health, budget, concurrency และ deadline metadata

### 10.9 ไฟล์และ test

- `app/pipeline/experimental_fallback.py`
- `tests/smoke_test_pipeline_fixes_20260823.py::test_general_generation_budget_is_adaptive`
- `tests/smoke_test_llm_timing_and_general_guard.py`

## 11. การทำงานร่วมกับ Fast, Structured, RAG, Rerank และ LLM

### 11.1 Fast/Rule

ใช้เมื่อ operation ชัดและมีสูตร/กฎแน่นอน เช่น:

- คำนวณราคา
- check-in
- booking how-to แบบชัด
- calendar/schedule บางรูปแบบ
- penalty/rules overview

LLM calls = 0

### 11.2 Structured

อ่าน schema โดย target ตรง:

- games
- equipment
- members
- reservation
- schedule
- service fee
- controls

Structured เป็น final-mode หลัก 873/1,600 หรือ 54.56% ใน full v3

### 11.3 Retrieval/RAG

แบ่งเป็น:

- Competition fact card 60 requests
- Curated RAG direct 14 requests
- Guarded vector direct 1 request
- RAG no-context 5 requestsที่จบ safe no-answer

คำว่า retrieval/RAG ในสัดส่วน final mode 75 requests หรือ 4.69% รวม fact card ด้วย หากนับเฉพาะ curated/vector direct ที่เป็น RAG search มี 15 requests หรือ 0.94%

### 11.4 BGE reranker

BGE เป็น optional reranker หลัง retrieval มีหลาย candidates ไม่ได้ถูกเปิดใน full v3 นี้ จึงห้ามนำ pass rate รอบนี้ไปอ้างว่า BGE ช่วยให้ดีขึ้น

### 11.5 Local LLM

Full v3 มี 349 calls:

- General answer 275
- Universal Intent 74
- Query Planner 0
- Tool Router LLM 0
- Grounded Composer 0

ไม่มี request ใดใช้เกิน 1 call แม้ policy cap สูงสุด 2 calls

## 12. Full 1,600 Result

Artifact:

- `reports/model_benchmark/20260823_pipeline_fixes_full1600_final_v3/REPORT.md`
- `reports/model_benchmark/20260823_pipeline_fixes_full1600_final_v3/llm_scb10x_typhoon2.5-qwen3-4b/results.jsonl`
- `reports/model_benchmark/20260823_pipeline_fixes_full1600_final_v3/llm_scb10x_typhoon2.5-qwen3-4b/summary.json`

### 12.1 Overall

| Metric | Result |
|---|---:|
| Total | 1,600 |
| Passed by heuristic judge | 1,599 |
| Pass rate | 99.94% |
| Average | 0.7730s |
| Median | 0.4465s |
| P95 | 2.3135s |
| P99 | 2.9207s |
| Max | 6.3254s |
| Over 9s | 0 |
| LLM calls | 349 |
| Requests with 0 calls | 1,251 |
| Requests with 1 call | 349 |
| Requests with 2+ calls | 0 |

### 12.2 Final-mode share

| Bucket | Requests | Share |
|---|---:|---:|
| Structured | 873 | 54.56% |
| Fast/Rule/Calculator | 244 | 15.25% |
| Retrieval/RAG/Fact Card | 75 | 4.69% |
| General LLM | 275 | 17.19% |
| Compound orchestration | 88 | 5.50% |
| Guard/Clarification/No-answer | 45 | 2.81% |

หมายเหตุ: Compound เป็น parent mode และข้างในอาจใช้ Structured/Fast หลาย child จึงไม่ควรตีความเป็น knowledge source แยกจาก path อื่น

### 12.3 Latency threshold

| Threshold | Requests |
|---|---:|
| มากกว่า 1s | 416 |
| มากกว่า 2s | 115 |
| มากกว่า 3s | 15 |
| มากกว่า 5s | 6 |
| มากกว่า 9s | 0 |

### 12.4 Stage ที่ใช้เวลารวมสูง

| Stage | Count | Total | Avg | P95 | Max |
|---|---:|---:|---:|---:|---:|
| Experimental/General fallback | 276 | 393.72s | 1,426.51ms | 2,209.73ms | 2,866.59ms |
| Ambiguity Gate | 1,503 | 168.05s | 111.81ms | 227.16ms | 1,217.47ms |
| Structured execution | 1,242 | 143.98s | 115.93ms | 296.73ms | 6,087.18ms |
| Candidate decisions | 1,469 | 115.14s | 78.38ms | 133.51ms | 221.36ms |
| Compound children | 88 | 105.02s | 1,193.38ms | 2,619.82ms | 5,841.93ms |
| Question Frame | 1,469 | 101.11s | 68.83ms | 110.15ms | 215.54ms |
| Validation | 1,123 | 77.31s | 68.85ms | 115.79ms | 222.37ms |

## 13. Failure ที่เหลือ

เคสเดียวที่ heuristic judge ไม่ผ่าน:

```text
ID: MB-0607-CR-071
คำถาม: ROV ถ้าใช้ bug จะโดนอะไร
คำตอบ: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูล...
Mode: pipeline:answer_contract_no_answer
Error: category_mismatch:no_answer
```

การประเมิน:

- ระบบไม่มี fact ที่ยืนยันบทลงโทษของ claim นี้
- การตอบโทษแบบเจาะจงจะเป็น unsupported claim
- no-answer จึงถูกต้องตาม product safety แม้ heuristic judge คาด competition_rules
- ไม่ควรแก้ด้วยการเดากฎหรือเปลี่ยน no-answer ให้เป็นข้อความที่ดูเหมือนตอบ
- งานต่อคือเพิ่ม source/fact card ที่ยืนยันได้ หรือปรับ evaluator ให้ยอมรับ safe no-answer เมื่อ fact coverage ไม่มี

## 14. Post-full Hardening

หลัง full v3 พบ slow structured catalog ไม่ใช่ LLM:

- `Nintendo Switch (1-4 Persons) มีเกมอะไรบ้าง` ใช้ 6.3254s
- Structured execution ใช้ 6.0872s
- Root cause คือ fuzzy game-title scan ทุก alias แม้ query ขอ catalog และไม่มี game target

แก้โดย:

- เรียก `_detect_game()` เฉพาะ game presence/location หรือ booking selection
- catalog list ของ service/zone ข้าม fuzzy target scan
- คำถามที่มีชื่อเกมจริงยังคง exact/fuzzy resolution

Post-fix probe 9 cases:

| Metric | ก่อนแก้ใน full v3 | หลังแก้ probe |
|---|---:|---:|
| Slow catalog range | 3.0356-6.3254s | 0.3019-0.3478s |
| Compound PS5 + Switch list | 5.8517s | 0.5085s |
| Named game availability | ผ่าน | ผ่าน 0.3161-0.4136s |
| Booking named game | ผ่าน | ผ่าน 0.2921s |
| Probe pass | n/a | 9/9 |

Artifact:

- `reports/model_benchmark/20260823_service_catalog_fuzzy_fix_probe9/REPORT.md`

ผล probe เป็น focused evidence หลัง patch ไม่ใช่การแทนค่าผล full 1,600 อย่างเงียบ ๆ

### 14.1 Sustained affected-scope regression

เมื่อขยายเป็น affected scope 460 cases รอบ v1 พบปัญหาเพิ่มที่ compound ราคา+จอง:

- v1 ผ่าน 457/460, P95 5.9929s และ max 9.1671s
- 3 failures เป็น `request_timeout_no_answer`
- booking child ใช้ structured execution 8.4-10.4 วินาทีโดยไม่มี LLM
- Root cause คือ `_service_game_availability_answer()` เปิด fuzzy game scan จากสัญญาณ `จะเล่น/จอง` แม้ target เป็น `Cockpit Zone` และ `_reservation_answer()` fuzzy scan fact aliases ทุกชุดแม้มี phrase exact `จองยังไง`

แก้เพิ่มด้วย:

1. Zone/service booking ทำ exact game lookup ได้ แต่ fuzzy game lookup เปิดเมื่อเป็น game presence/location หรือมีคำว่า `เกม/game` ใน booking query
2. Reservation facts ใช้ exact-first และเลือก alias ที่เฉพาะกว่าด้วยความยาวเมื่อ score เท่ากัน
3. เมื่อไม่มี exact fact จึง flatten aliases และทำ fuzzy pass ครั้งเดียว
4. เก็บ `match_method` และ `matched_alias` ใน structured evidence

ผล affected-scope v2:

| Metric | v1 ก่อน exact/fuzzy gating | v2 หลังแก้ |
|---|---:|---:|
| Total | 460 | 460 |
| Passed | 457 | 460 |
| Pass rate | 99.35% | 100% |
| Average | 1.0445s | 0.6152s |
| P95 | 5.9929s | 1.0512s |
| Max | 9.1671s | 1.6804s |
| LLM calls | 0 | 0 |
| Compound pass | 86/89 | 89/89 |
| Compound average | 3.3144s | 0.8449s |
| Compound P95 | 8.8105s | 1.3794s |

Artifact ล่าสุด:

- `reports/model_benchmark/20260823_service_catalog_postfix_affected460_v2/REPORT.md`

Artifact v1 ถูกเก็บไว้เพื่อเป็นหลักฐาน failure/root cause:

- `reports/model_benchmark/20260823_service_catalog_postfix_affected460/REPORT.md`

## 15. Hardening เพิ่มเติมที่ทำร่วมกัน

แม้ไม่ใช่ชื่อ Pipeline 1-8 โดยตรง แต่จำเป็นต่อผลสุดท้าย:

1. Query Planner ใช้เฉพาะ true dependency/broad complex ไม่ใช้เพราะมี comparison อย่างเดียว
2. Shared-tail compound ไม่เอาคำว่า `จองยังไง` ไปต่อท้ายทุก operand
3. Generic booking ไม่ fuzzy scan ทุกชื่อเกม
4. Bare `เกม` ตอบ catalog deterministic
5. Bare `จอง` ถาม clarification
6. `ร่างกาย` ไม่ชน text-generation keyword `ร่าง`
7. Missing homework content ถามขอ input โดยไม่ใช้ LLM
8. Optional LLM circuit แยกจาก model-wide General health
9. LLM context/keep-alive aligned
10. Service catalog ข้าม fuzzy game scan เมื่อไม่มี target
11. Reservation fact exact-first และ fuzzy pass เดียวเมื่อจำเป็น
12. Zone booking ไม่เปิด fuzzy game scan เพียงเพราะมีคำว่า `จะเล่น/จอง`

## 16. Test Matrix

ชุดที่ผ่านหลังแก้:

- `tests/smoke_test_pipeline_fixes_20260823.py`
- `tests/smoke_test_universal_intent.py`
- `tests/smoke_test_llm_tool_router.py`
- `tests/smoke_test_query_planner.py`
- `tests/smoke_test_llm_health_circuit_breaker.py`
- `tests/smoke_test_product_sla_guards.py`
- `tests/smoke_test_llm_timing_and_general_guard.py`
- `tests/smoke_test_structured_tools.py`
- `tests/smoke_test_answer_pipeline.py`

Benchmark/probe:

- context alignment 4/4
- general contract 21/21
- general group adjusted 275/275
- full v3 1,599/1,600 by heuristic judge
- post-fix service catalog 9/9
- post-fix affected scope v2 460/460, P95 1.0512s, max 1.6804s

## 17. Configuration ที่เกี่ยวข้อง

| Variable/Policy | ค่า |
|---|---:|
| Backend global timeout | 9s ใน product benchmark |
| User-visible target | <=10s |
| Finalizer reserve | 1s |
| Max LLM calls/request | 2 |
| LLM concurrency | 1 |
| Query Planner cap | 4s |
| General num_ctx | 3072 |
| Ollama keep_alive | 10m |
| General num_predict | adaptive, สูงสุด 128 ใน profile ปัจจุบัน |
| Health failure window | 30s |
| Model | scb10x/typhoon2.5-qwen3-4b |

## 18. Acceptance Criteria ของ Pipeline 1-8

ถือว่าผ่าน functional acceptance ในขอบเขต single-process sequential เมื่อ:

1. ไม่มี uninitialized request-state exception
2. `ข้อเสีย` ไม่กลายเป็นราคา
3. general definition ไม่ตอบ inventory
4. ASCII alias ไม่ match กลางชื่อเกม
5. game-zone ranking ใช้ structured deterministic
6. dynamic latest query ไม่มี live evidenceแล้วไม่เดา
7. clear-general ใช้ LLM ไม่เกิน 1 call
8. output profile ตรงรูปแบบและ reject truncated answer
9. Full benchmark ไม่มี request เกิน 9 วินาที
10. ไม่มี request ใช้ 2 LLM calls ใน full v3

## 19. ข้อจำกัดที่ต้องพูดตรง ๆ

- 99.94% เป็น heuristic judge ไม่ใช่ human verification ทุกคำตอบ
- Full 1,600 v3 อยู่ก่อน micro-fixes สองรายการสุดท้าย; latest affected scope 460 cases ผ่าน 100% แต่ยังไม่ได้รัน full 1,600 ซ้ำหลัง micro-fixes
- รอบ full เป็น sequential จึงยังไม่พิสูจน์ queue wait ของ 20 concurrent users
- Backend 9 วินาทีไม่รวม queue/network ของ Facebook/Web ในสภาพ production จริง
- BGE ไม่ได้เปิดใน full v3
- Grounded LLM Composer ไม่ได้ถูกใช้ใน full v3
- RAG coverage ยังน้อยเพราะ PSU facts ส่วนใหญ่มี structured schema
- Vector retrieval มี cold/rare outlier และ backend ยังเป็น hash char n-gram
- In-process semaphore ไม่ป้องกันหลาย Python processes แย่ง Ollama พร้อมกัน
- Ollama socket close เป็น best effort ไม่ใช่ hard process cancellation
- ข้อมูล controls บางรายการยังต้อง manual source verification
- การจองยังเป็นคำแนะนำ ไม่ใช่ transaction

## 20. งานถัดไป

1. ทำ load test อย่างน้อย 5 sessions และ target peak 20 sessions
2. วัด queue wait, end-to-end P95/P99, session isolation และ timeout rate
3. ออกแบบ shared queue/worker สำหรับหลาย process
4. เพิ่ม live provider สำหรับข่าว/กิจกรรม/วันเปิดปิดพิเศษ พร้อม timestamp
5. เพิ่ม human review sample ของ 1,599 pass cases
6. แก้/ทำ contract สำหรับ ROV bug เมื่อมี authoritative source
7. ทำ semantic embedding experimentหลัง structured correctness นิ่ง
8. ตรวจ secondary/manual control sources

## 21. สรุป

Pipeline 1-8 เปลี่ยนระบบจากการแก้คำผิดรายเคสเป็น shared contracts ที่ครอบคลุมหลาย stage: request state ต้องมีเสมอ, lexical signals ต้องมีบริบท, operation ต้องมาก่อนคำนามกว้าง, ASCII ต้องมี boundary, calculation/ranking ต้อง deterministic, live fact ต้องมี timestamp, clear-general ต้องสงวน call ให้คำตอบ และ generation ต้องมี bounded output contract

ผล full v3 ยืนยันว่าเป้าหมาย sequential single-request ต่ำกว่า 9 วินาทีทำได้โดยไม่มี timeout ส่วน post-fix affected-scope v2 ผ่าน 460/460 และลด P95 เหลือ 1.0512 วินาทีโดยไม่มี LLM call อย่างไรก็ตาม readiness สำหรับ 20 concurrent users ยังต้องพิสูจน์ด้วย load test และ shared queue ต่อไป
