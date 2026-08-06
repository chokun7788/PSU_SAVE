# PSU Esports Chatbot: Full Process Flow ณ วันที่ 2026-08-03

เอกสารนี้อธิบาย Flow และ Architecture ปัจจุบันของ Local Chatbot สำหรับ **PSU Esports Studio - Phuket** โดยอ้างอิงจากโค้ดที่ใช้งานจริง ณ วันที่ **3 สิงหาคม 2026** ไม่ใช่เพียงแบบร่างเชิงแนวคิด

Source หลักของระบบ:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data
```

ภาพประกอบของเอกสารนี้:

```text
docs\current_chatbot_full_process_flow_th_20260803.png
```

เวอร์ชันนโยบายควบคุมคุณภาพที่บันทึกใน Decision Artifact:

```text
correctness_control_flow_v2
```

---

## 1. หลักการสำคัญที่สุดของระบบ

ระบบนี้ไม่ใช่ Chatbot ที่ส่งทุกคำถามเข้า LLM แล้วให้ LLM ตอบเอง แต่เป็น **Hybrid Orchestration Pipeline** ที่เลือกวิธีตอบตามชนิดคำถาม ความชัดเจน ความเสี่ยง และหลักฐานที่มี

หลักการหลักมีดังนี้:

1. คำถามเกี่ยวกับ PSU Esports Studio ต้องตอบจากข้อมูลที่ยืนยันได้เท่านั้น
2. คำถามราคา ตาราง จอง สมาชิก อุปกรณ์ รายการเกม และปุ่มเกม ควรใช้ Structured Tool หรือ Deterministic Path ก่อน
3. RAG ใช้เมื่อคำตอบต้องค้นจากชุดข้อมูลที่คัดสรร และต้องผ่าน category/entity/source guard
4. LLM ใช้เฉพาะจุดที่ช่วยแยกเจตนา จัด route เรียบเรียง facts หรือคำถามความรู้ทั่วไปนอก PSU
5. ถ้า target หรือ operation ไม่ชัด ระบบต้องถามกลับหรือ abstain แทนการเดา
6. คำตอบทุกเส้นทางต้องผ่าน Answer Validator และ Answer-Type Contract ก่อนส่งออก
7. ถ้าคำตอบไม่ผ่าน ระบบมีการซ่อมแบบจำกัดจำนวน ไม่วนเรียกจนกว่าจะถูกแบบไม่สิ้นสุด
8. ถ้ายังไม่พบข้อมูลจริง ระบบจบด้วย Safe No-answer ไม่ใช้ LLM แต่งข้อมูล PSU

สรุปแนวคิด:

```text
เข้าใจคำถาม
-> ประเมินความเสี่ยงและความกำกวม
-> สร้าง candidate หลายเส้นทาง
-> ตรวจ precondition
-> เลือกเครื่องมือตอบ
-> ตรวจหลักฐานและชนิดคำตอบ
-> ส่งคำตอบ หรือถามกลับ หรือ no-answer อย่างปลอดภัย
```

---

## 2. Flow รวมแบบ Answer-first

```text
User Input
-> Interface / Session
-> Session Context Resolver
-> Global Request Deadline
-> Compound Question Planner
-> Preprocess / Normalize / Alias / Typo / Query Variants
-> Active Query Variant Selection
-> Entity Extraction
-> Scope Guard
-> Heuristic Router + Routing Priority + Semantic Intent
-> Adaptive Universal Intent
-> Optional LLM Tool Router
-> Ambiguity Gate v2 + Candidate Margin
-> Question Frame + Answer-Type Contract Plan
-> Target Resolver + Optional Gated Entity Reranker
-> Capability Candidate Scoring
-> Policy Veto + Tool Preconditions
-> Execute Selected Capability
   -> Early Price Calculator
   -> Structured Tools
   -> Game-control Vector-first
   -> Fast / Rule
   -> Competition Fact Cards
   -> Hybrid Retrieval
   -> Curated Retrieval
   -> Guarded Vector Retrieval
   -> Optional RAG / General Local LLM
   -> Safe No-answer
-> Format
-> Validate + Answer Contract + Source Contract
-> Bounded Repair หรือ Hard Veto
-> Thai Response Style
-> Decision Artifact + Trace + Metrics + Chat Log
-> Final Answer
```

จุดสำคัญคือ เส้นทางข้างบนไม่จำเป็นต้องผ่านทุกกล่อง ระบบสามารถจบเร็วได้ทันทีเมื่อได้คำตอบที่มั่นใจ มีหลักฐาน และผ่าน validation แล้ว

---

## 3. Backbone 0: Interface และ Runtime Entry Point

ไฟล์หลัก:

```text
tools\local_ai_chat.py
start_local_ai_chat.ps1
app\web_api\server.py
app\runtime\pipeline_answer.py
app\pipeline\engine.py
```

หน้าที่:

- รับข้อความจาก Local CLI, Web API หรือ Notebook
- กำหนด session id และ recent history
- ตั้งค่าเปิดหรือปิด Local LLM, Tool Router, Facts Composer, RAG fallback และ Entity Reranker
- ตั้ง global request timeout
- เรียก `resolve_question_with_context()` ก่อนเข้า pipeline หลัก
- เรียก `answer_question_pipeline_debug()` เพื่อรับ answer, route, mode, trace, validation และ decision artifact
- เขียน chat log หลังตอบเสร็จ โดย log ล้มเหลวต้องไม่ทำให้คำตอบล้ม

ค่าปริยายจาก `start_local_ai_chat.ps1` ณ วันที่เอกสารนี้:

| ค่า | Default | ความหมาย |
|---|---:|---|
| Main Ollama model | `scb10x/typhoon2.5-qwen3-4b` | รุ่นปริยายในสคริปต์เริ่มระบบ แต่เปลี่ยนได้ |
| General LLM timeout | 20 วินาที | timeout ของคำตอบ general |
| Global pipeline timeout | 20 วินาที | เพดานเวลารวมหนึ่งคำถาม |
| General `num_predict` | 128 | token output โดยประมาณของ general LLM |
| Intent timeout | 8 วินาที | timeout ของ Adaptive Intent LLM |
| Intent `num_predict` | 50 | บังคับให้ intent ตอบ JSON สั้น |
| LLM Tool Router | เปิดเมื่อไม่ใช้ `-NoLlm`/`-NoToolRouter` | แต่เรียกเฉพาะเคสที่ gate อนุญาต |
| Facts Composer | ปิดโดยปริยาย | เปิดด้วย `-Composer` |
| Intent-first | เปิด แต่ weak-route only | route ชัดไม่ต้องเสียเวลาเรียก LLM |
| Entity Reranker | ปิดโดยปริยาย | เปิดด้วย `-EntityReranker` |
| RAG fallback | เปิด ถ้าไม่ระบุ `-NoRagFallback` | ยังต้องผ่าน policy/guard |

หมายเหตุ: คำว่า "เปิด LLM" ไม่ได้แปลว่าทุกคำถามเรียก LLM เพราะแต่ละ LLM path มี gate, health check, deadline และ policy veto ของตัวเอง

---

## 4. Backbone 1: Session Context Resolver

ไฟล์หลัก:

```text
app\session\context_resolver.py
```

Input:

```text
question + recent_history สูงสุดช่วงล่าสุดของ session
```

Output:

```text
ResolvedQuestion(
  original_question,
  resolved_question,
  used_context,
  context_game,
  context_domain,
  context_operation,
  context_topic,
  reason
)
```

หน้าที่:

- เติมชื่อเกมจากบริบท เช่น ก่อนหน้าถาม `Gran Turismo 7` แล้วถามต่อ `ปุ่ม`
- เติม operation จากคำตอบก่อนหน้า เช่น หลังถามวิธีจองแล้วพิมพ์ `สรุปทำไง`
- รองรับคำตอบสั้นหลัง Clarification Preview เช่น `เกม`, `อุปกรณ์`, `ราคา`, `จอง`
- ดึง universal intent, route, game และ zone จากประวัติช่วงล่าสุด
- ป้องกัน target ใหม่ถูก context เก่าทับ

เทคนิคที่ใช้:

1. **Latest-context priority** ใช้ข้อมูลล่าสุดก่อน
2. **Explicit target override** ถ้าข้อความใหม่มีชื่อเกมหรือโซนชัด ให้ข้อความใหม่ชนะ
3. **Topic-shift guard** ถ้าเปลี่ยนไปถามราคา จอง เวลา กฎ หรือการแข่งขัน ไม่สืบทอด operation เดิมแบบสุ่ม
4. **Clarification TTL** pending clarification ใช้ได้เฉพาะ assistant turn ล่าสุด ไม่ติดค้างหลาย turn
5. **Allowed-choice contract** ข้อความตอบสั้นหลัง clarification ต้องตรง choice ที่ระบบเสนอ
6. **No blind inheritance** คำสั้นอย่าง `เครื่อง` หรือ `ปุ่ม` จะไม่ถูกยืม target ถ้า context ไม่พอ

IF/ELSE สำคัญ:

```text
IF คำถามใหม่มี target ชัด
  -> ใช้ target ใหม่
ELSE IF เป็น follow-up และ session มี context ที่เข้ากัน
  -> เติม target/domain/operation จาก context
ELSE IF เป็น choice ที่ตรง pending clarification ล่าสุด
  -> แปลงเป็นคำถามเต็มของ choice นั้น
ELSE
  -> ส่งคำถามเดิมเข้า pipeline
```

ข้อจำกัด:

- Local CLI เก็บ history ในหน่วยความจำของ process ปัจจุบัน
- เมื่อปิดแล้วเปิด process ใหม่ session memory ใน RAM เริ่มใหม่ แม้ chat log เดิมยังอยู่ใน JSONL/SQLite
- Web/API ต้องส่งหรือโหลด history ตาม `client_session_id` จึงจะต่อบริบทได้ถูกต้อง

---

## 5. Backbone 2: Global Request Deadline

ไฟล์หลัก:

```text
app\pipeline\request_deadline.py
app\pipeline\engine.py
```

หน้าที่:

- ครอบหนึ่งคำถามด้วย deadline เดียว
- จำกัดเวลารวมของ preprocess, routing, retrieval, reranker และ LLM
- ส่ง remaining time ให้ LLM call แต่ละตัวผ่าน `timeout_for_call()`
- ตรวจ deadline ตาม checkpoint สำคัญ
- ให้ compound child questions ใช้ budget เดียวกับ parent

เทคนิค:

- ใช้ `ContextVar` เพื่อแชร์ deadline ใน call chain เดียวโดยไม่ส่ง parameter ทุกฟังก์ชัน
- LLM timeout จริงเท่ากับ `min(configured_timeout, remaining_global_time)`
- ถ้าเหลือเวลาน้อยกว่า minimum call budget จะไม่เริ่ม LLM call

Checkpoint หลัก:

```text
after_split
after_route_selection
before_universal_intent
after_universal_intent
after_tool_router
after_ambiguity_gate
after_candidate_decisions
before/after multi child
before_general_fallback
before_experimental_fallback
```

เมื่อหมดเวลา:

```text
IF deadline_exceeded
  -> ไม่เริ่มงานหนักเพิ่ม
  -> คืน timeout-safe result
  -> บันทึก stage ที่หมดเวลาใน trace
```

---

## 6. Backbone 3: Compound Question Planner

ตำแหน่งหลัก:

```text
app\pipeline\engine.py
```

หน้าที่:

- แยกคำถามหลายส่วนในข้อความเดียว
- รองรับหลาย operation กับ target เดียว
- รองรับหลาย target กับ operation เดียว
- รองรับสองหมวดคนละเรื่องในประโยคเดียว
- รวมคำตอบ child เป็นข้อ ๆ โดยรักษา source และ validation ของแต่ละ child

ตัวอย่าง:

```text
ถาม: TEKKEN 8 กับ Mario Kart 8 Deluxe มีปุ่มอะไรบ้าง
ผล: แยกเป็น child ของ TEKKEN 8 และ child ของ Mario Kart 8 Deluxe
```

```text
ถาม: PC ราคาเท่าไหร่ แล้วมีเกมอะไรบ้าง
ผล: แยก price child และ game catalog child
```

```text
ถาม: VR มีเกมอะไรและจองยังไง
ผล: แยก game catalog child และ booking child โดยส่ง subject ที่ใช้ร่วมกัน
```

IF/ELSE:

```text
parts = split_multi_question(question)

IF parts > 1
  FOR each part
    -> ส่งเข้า Single Question Pipeline
    -> หยุดถ้า global deadline หมด
  -> รวม answer/hits/errors/warnings/trace
ELSE
  -> เข้า Single Question Pipeline โดยตรง
```

เทคนิค:

- Shared-subject propagation
- Shared-tail propagation
- Explicit-subject detection
- Subjectless follow-up operation detection
- Source deduplication
- Parent/child timing trace

---

## 7. Backbone 4: Preprocess, Normalize และ Query Variants

ไฟล์หลัก:

```text
app\pipeline\preprocess.py
app\core\normalization.py
app\pipeline\game_title_correction.py
```

Input:

```text
resolved_question
```

Output:

```text
PreprocessedInput(
  raw_query,
  clean_query,
  normalized_query,
  language_hint,
  query_variants
)
```

ขั้นตอน:

1. รวม whitespace และตัดช่องว่างหัวท้าย
2. ตรวจภาษา `th`, `en`, `mixed_th_en`, `unknown`
3. normalize ตัวพิมพ์ รูปคำ และ alias
4. สร้าง typo/game-title variants เมื่อมีเหตุผลพอ
5. สร้าง query variants สูงสุดจำนวนจำกัด
6. ไม่แก้ชื่อเกมในคำถามที่จริงเป็นราคา อุปกรณ์ หรือ catalog ของ zone เพื่อป้องกัน over-correction

เทคนิค:

- Alias normalization
- Typo correction แบบ domain-aware
- Protected equipment/service phrases
- Game title exact/compact/fuzzy candidates
- Bounded query variants เพื่อลด latency
- Cache alias indexes

ตัวอย่างความเสี่ยงที่ป้องกัน:

```text
Over cook
-> ควรสร้าง candidate ไปยังตระกูล Overcooked
-> แต่ยังต้องให้ Entity Resolver ตัดสินว่าเป็น Overcooked!, Overcooked! 2 หรือรายการใน family
```

```text
PlayStation VR2
-> ต้องไม่อ่าน `R2` เป็นคำถามปุ่ม R2
-> short control token ใช้ขอบเขต token ไม่ใช้ substring ตรง ๆ
```

---

## 8. Backbone 5: Active Query Variant Selection และ Entity Extraction

ไฟล์หลัก:

```text
app\pipeline\engine.py
app\pipeline\preprocess.py
```

### 8.1 Active Query Variant Selection

แต่ละ query variant ถูกทดลองด้วย:

```text
extract_entities(variant)
route_intent(variant, entities)
```

จากนั้นเลือกรูปคำที่ให้ route ดีกว่า โดยไม่ยอมให้ variant ที่กว้างหรืออ่อนกว่าแย่ง route ที่ชัดกว่า

หลักพิจารณา:

- route category ที่ไม่ใช่ `general/unknown` ดีกว่า weak category
- category เดียวกันแต่ intent เฉพาะกว่ามีโอกาสชนะ
- games availability/detail ที่ชัดไม่ควรถูก knowledge route ทับ
- confidence และลักษณะ operation ต้องสอดคล้องกัน

### 8.2 Entity Extraction

Entity ที่ดึงในชั้นแรก:

| Entity | ตัวอย่าง |
|---|---|
| `day` | monday, friday |
| `time_slots` | morning, afternoon |
| `service` | PC, PS5, Nintendo Switch, Cockpit, VR |
| `user_group` | PSU, general student/alumni, adult |
| `duration` | 30 นาที, 60 นาที |
| `price_intent` | ราคา, กี่บาท, ฟรีไหม |
| `comparison_intent` | ต่างกัน, เทียบ, แพงกว่า |
| `short_answer` | ตอบสั้น |

เทคนิค:

- Conditional entity detection ไม่สแกน alias ทุกชุดเมื่อไม่จำเป็น
- Customer group precedence แยก PSU student/staff ออกจาก general student/adult
- Duration normalization
- Style phrase stripping ก่อนจำแนกกลุ่มผู้ใช้
- Route-aware query variant selection

---

## 9. Backbone 6: Scope Guard

ไฟล์หลัก:

```text
app\pipeline\guard.py
```

หน้าที่:

- ตรวจคำถามว่างหรือสัญญาณนอกขอบเขต
- ตรวจคำถามที่ควรปฏิเสธหรือถามกลับก่อนเข้าชั้นลึก
- กันข้อมูลศูนย์ถูกนำไปตอบคำถาม general ที่ไม่มีความเกี่ยวข้อง

IF/ELSE:

```text
guard_answer, guard_confidence = guard_scope(...)

IF guard มีคำตอบและ confidence >= 0.90
  IF experimental fallback เปิด
    -> fallback ยังต้องอยู่ภายใต้นโยบายไม่เดา PSU facts
  ELSE
    -> จบด้วย guard no-answer
ELSE
  -> ไป Router Stack
```

Scope Guard เป็นด่านหยาบ ไม่ใช่ตัวตัดสิน intent สุดท้าย จึงยังมี Ambiguity Gate, Preconditions และ Answer Contract คอยตรวจซ้ำในคนละมุม

---

## 10. Backbone 7: Router Stack

Router Stack มีหลายชั้นเพราะ route เดียวที่ตัดสินเร็วเกินไปเคยทำให้คำถามปุ่มไปตอบวิธีเล่น หรือถามเกมหนึ่งแต่ไปตอบอีกเกม

### 10.1 Heuristic Router

ไฟล์:

```text
app\pipeline\router.py
app\pipeline\routing_policy.py
data\routing\route_priority_matrix.json
data\intent\semantic_intents.jsonl
app\pipeline\semantic_intent.py
```

หน้าที่:

- จับ operation/domain ที่มี keyword ชัด
- ใช้ priority matrix แก้กรณีคำหลายหมวดชนกัน
- ใช้ local semantic intent แบบ character n-gram สำหรับรูปประโยคที่ไม่ได้ตรง keyword ทุกตัว
- ป้องกัน route ที่มี negative conditions

ตัวอย่าง priority:

```text
ปุ่ม/control
-> game_controls มี priority เหนือ game detail

ราคา/กี่บาท
-> service_fee มี priority เหนือ equipment/game

จอง/เข้าใช้บริการ
-> reservation มี priority เหนือ game how-to

กติกาแข่งขัน/BO3
-> competition_rules มี priority เหนือ game controls
```

เทคนิค:

- Operation-first routing
- Negative keyword guard
- Route priority matrix
- Semantic intent using local char n-gram cosine
- Minimum confidence + minimum margin
- Route-specific overrides

หมายเหตุ: Semantic Intent ชั้นนี้ไม่ใช่ LLM และ vector ของมันเป็น character n-gram ภายในเครื่อง

### 10.2 Adaptive Universal Intent

ไฟล์:

```text
app\pipeline\universal_intent.py
```

ผลลัพธ์:

```text
UniversalIntent(
  domain,
  operation,
  target,
  filters,
  needs,
  answer_style,
  confidence,
  method,
  reason
)
```

ขั้นแรกใช้ heuristic สร้าง intent เสมอ จากนั้นประเมิน risk flags ว่าควรเรียก Intent LLM หรือไม่

IF/ELSE:

```text
heuristic_intent = build_from_route_and_query()

IF LLM ปิด
  -> ใช้ heuristic
ELSE IF route ชัดและไม่มี ambiguity risk
  -> ใช้ heuristic
ELSE IF intent-first เปิดและ weak-route policy อนุญาต
  -> สร้าง candidate intent ไม่เกินจำนวนกำหนด
  -> ให้ Local LLM เลือก candidate_id เท่านั้น
  -> parse JSON และ validate ค่า domain/operation
  -> ถ้า timeout/parse fail ใช้ heuristic เดิม
```

Intent LLM ไม่ได้มีสิทธิ์สร้าง capability ใหม่เอง แต่เลือกจาก candidate ที่ระบบเตรียมไว้ เพื่อลด open-ended hallucination

### 10.3 Optional LLM Tool Router

ไฟล์:

```text
app\pipeline\llm_tool_router.py
```

หน้าที่:

- เสนอ action เช่น structured, fast, retrieval, vector, RAG/LLM, clarification
- ช่วยเฉพาะเคสที่ heuristic route ยังไม่ชัด
- refine route จาก `general/unknown/no_answer` ไป domain ที่มี evidence target เมื่อ confidence ผ่านเกณฑ์

IF/ELSE:

```text
heuristic_tool_decision = build_heuristic_decision()

IF allow_llm = false
  -> ใช้ heuristic decision
ELSE IF PSU_LLM_TOOL_ROUTER ปิด
  -> ใช้ heuristic decision
ELSE IF route ชัดพอ
  -> ไม่เรียก LLM
ELSE IF circuit breaker ไม่อนุญาต หรือ deadline ไม่พอ
  -> ใช้ heuristic decision
ELSE
  -> เรียก Local LLM และ parse JSON
  -> ถ้า parse/timeout fail ใช้ heuristic decision
```

Tool Router เป็นคำแนะนำหนึ่งคะแนนใน Candidate Scoring ไม่ใช่ผู้ตัดสินสุดท้ายเพียงตัวเดียว

---

## 11. Backbone 8: Ambiguity Gate v2

ไฟล์หลัก:

```text
app\pipeline\ambiguity_gate.py
app\pipeline\entity_resolver.py
```

หน้าที่:

- หยุดคำถามกว้างก่อนเข้าตอบ
- ตรวจ target ขาดหาย
- ตรวจชื่อเกมเป็น family หรือมีหลาย candidate
- เปรียบเทียบคะแนน intent candidate หลาย domain
- ถามกลับเฉพาะกรณีข้อมูลไม่พอจริง
- แสดง preview สั้นจากข้อมูลที่มี source จริงได้

Candidate Intent Scoring ประเมินอย่างน้อย:

- route category/intent
- universal intent domain/operation
- tool router action/domain
- keyword operation
- entity/service/game signal
- negative conditions
- target presence

Margin rule สำคัญ:

```text
margin = top_candidate.score - second_candidate.score

IF top < 0.50
  -> ความมั่นใจต่ำ
ELSE IF second < 0.42
  -> คู่แข่งอ่อนเกินไป ไม่จำเป็นต้องถามกลับ
ELSE IF margin >= 0.14
  -> top ชัดพอ
ELSE
  -> มีโอกาสถาม clarification ตามเงื่อนไข domain/target
```

กรณีที่ Gate ถามกลับ:

1. `ปุ่ม` แต่ไม่มีชื่อเกมและ context เกมไม่พอ
2. `เล่นยังไง` แต่ไม่รู้ว่าหมายถึงวิธีเข้าใช้บริการหรือวิธีเล่นเกม
3. `PC มีอะไรบ้าง` เพราะอาจหมายถึงเกม อุปกรณ์ ราคา หรือการจอง
4. ชื่อเกมเป็น family ที่มีหลายเวอร์ชันและ operation ต้องการเกมเดียว
5. top intent และ second intent ใกล้กันเกินไปโดยไม่มี signal ชี้ขาด

Hybrid Clarification Preview:

```text
PC มีอะไรบ้าง
-> ถามว่า หมายถึงเกม อุปกรณ์ ราคา หรือจอง
-> สามารถใส่ preview สั้นที่ดึงจาก fact จริง
-> บันทึก pending choices ให้ session resolver ใช้ใน turn ถัดไป
```

ผลลัพธ์:

```text
AmbiguityGateResult(
  action = allow | clarify,
  confidence,
  reason,
  flags,
  answer,
  metadata,
  hits
)
```

---

## 12. Backbone 9: Question Frame และ Answer-Type Plan

ไฟล์หลัก:

```text
app\pipeline\question_frame.py
```

Question Frame เป็นโครงข้อกำหนดที่ระบบสร้างก่อนตอบ เพื่อบอกว่า "คำถามนี้ต้องการคำตอบชนิดไหน เกี่ยวกับ target ใด และอนุญาตหลาย target หรือไม่"

โครงสร้าง:

```text
QuestionFrame(
  operation,
  domain,
  expected_answer_types,
  targets,
  target_status,
  target_margin,
  target_required,
  allows_multiple_targets,
  needs_clarification,
  confidence,
  method
)
```

Operation-first mapping:

| สัญญาณคำถาม | Operation | Expected Answer Type |
|---|---|---|
| ปุ่ม, จอย, controls | `control_lookup` | controls |
| ราคา, กี่บาท | `price_lookup`/`price_calculate` | price/calculation |
| จอง, เข้าใช้บริการ | `booking_lookup` | booking/how_to |
| เปิดกี่โมง, วันไหน | `schedule_lookup` | schedule |
| เกมเยอะสุด | `game_zone_rank` | ranking/list/calculation |
| รายชื่อเกม | `game_catalog` | game_catalog/list |
| เกมแนวไหน | `game_detail` | game_detail |
| เล่นยังไง | `game_how_to` | game_detail/controls/how_to |
| อุปกรณ์ | `equipment_lookup` | equipment/list |
| ทีมงาน/ตำแหน่ง | `member_lookup` | member/list |
| กติกาสตูดิโอ | `studio_rule_lookup` | fact/rule |
| กติกาแข่งขัน | `competition_rule_lookup` | competition_rule |
| ค่าปรับ/เสียหาย | `penalty_lookup` | penalty/rule |

เหตุผลที่ Question Frame สำคัญ:

- Router บอกว่าจะไปหมวดไหน แต่ Frame บอกว่าคำตอบต้องมีรูปร่างอย่างไร
- Validator ใช้ Frame ตรวจคำตอบข้ามหมวด
- Capability Scoring ใช้ Frame เพิ่มคะแนนเครื่องมือที่ตรง operation
- Target Resolver ใช้ Frame ตัดสินว่าต้องมี target เดียว หลาย target หรือไม่ต้องมี target

---

## 13. Backbone 10: Target Resolver และ Gated Entity Reranker

ไฟล์หลัก:

```text
app\pipeline\target_resolver.py
app\pipeline\entity_resolver.py
app\pipeline\game_title_correction.py
```

Target ที่รองรับ:

- game
- game family/version
- service/zone
- equipment
- member/role
- price service target

Candidate matching ลำดับหลัก:

```text
exact canonical title
-> exact alias
-> compact alias
-> token match
-> fuzzy match
-> family candidate
-> unknown
```

หลักสำคัญ:

- Canonical title ที่ตรงชัดต้องชนะ alias tie
- คะแนน match ต่างชนิดมี ceiling ต่างกัน เพื่อไม่ให้ fuzzy ดูมั่นใจเท่า exact
- Family query เช่น `Overcooked` อาจมีหลายเกม ต้องใช้ operation ตัดสินว่าจะ list family หรือถามเลือกเวอร์ชัน
- Target ใหม่ชนะ session context เดิม
- หลาย target อนุญาตเฉพาะ operation ที่ประกาศ `allows_multiple_targets`

### Optional Gated Entity Reranker

Model ปริยาย:

```text
BAAI/bge-reranker-v2-m3
```

ตำแหน่ง cache ปริยาย:

```text
D:\AIModels\huggingface
```

Reranker นี้เป็น CrossEncoder สำหรับจัดอันดับ game/entity candidate ไม่ใช่ตัวตอบคำถาม

IF/ELSE:

```text
IF PSU_ENTITY_RERANKER ปิด
  -> ใช้ lexical/entity resolver ปกติ
ELSE IF candidate ชัดอยู่แล้ว
  -> ไม่ rerank
ELSE IF candidate มากเกิน top_k หรือเป็น generic family ที่ควรถามกลับ
  -> ไม่ rerank
ELSE IF operation/target domain ไม่อยู่ใน gated scope
  -> ไม่ rerank
ELSE
  -> CrossEncoder ให้คะแนน query-candidate pairs
  -> ตรวจ minimum score และ rerank margin
  -> margin ผ่าน: เลือก exact candidate
  -> margin ไม่ผ่าน: คงสถานะ ambiguous
```

เหตุผลที่ใช้เฉพาะ gated path:

- ลด latency ของคำถามชัด
- ไม่ให้ semantic model ขยายขอบเขตจนเลือกเกมมั่ว
- ใช้เมื่อ lexical candidate หลายตัวสูสีกันจริง
- ยังรักษา abstain เมื่อ reranker เองไม่ชัด

---

## 14. Backbone 11: Capability Registry และ Candidate Scoring

ไฟล์หลัก:

```text
app\pipeline\capability_registry.py
app\pipeline\tool_preconditions.py
```

ระบบไม่เลือก route เดียวแล้วเชื่อทันที แต่สร้าง candidate จาก capability ที่ระบบมีทั้งหมด

Capability ปัจจุบัน:

| Capability ID | Action | ใช้ตอบอะไร |
|---|---|---|
| `structured.members` | structured | สมาชิก กลุ่ม ตำแหน่ง โปรไฟล์ |
| `structured.games` | structured | catalog, detail, availability, count, ranking |
| `structured.game_controls` | structured | ปุ่ม/controls ที่ยืนยันได้ |
| `structured.equipment` | structured | อุปกรณ์ รุ่น จำนวน โซน |
| `structured.reservation` | structured | วิธีจอง policy และ session limit |
| `structured.schedule` | structured | วันและเวลาเปิดปิด |
| `structured.service_fee` | structured | ตารางราคาและ mapping จากเกมไปบริการ |
| `fast.price_calculator` | fast_path | คำนวณราคาแบบ deterministic |
| `fast.domain_handlers` | fast_path | คำตอบ deterministic รายหมวด |
| `rulebase.category_rules` | rulebase | pattern rules จาก data/rules |
| `retrieval.competition_fact_cards` | retrieval | ข้อเท็จจริงกติกาแข่งขัน |
| `retrieval.hybrid_guarded` | retrieval | lexical + vector + entity rerank แบบมี guard |
| `retrieval.vector_guarded` | vector | vector retrieval แบบมี category/entity threshold |
| `llm.facts_composer` | rag_llm | เรียบเรียง verified facts เท่านั้น |
| `llm.general_answer` | general_llm | ความรู้ทั่วไปที่ไม่ใช่ข้อมูล PSU |
| `clarification.ask_user` | clarification | ถาม target/operation เพิ่ม |
| `fallback.no_answer` | no_answer | ไม่มีข้อมูลยืนยัน |

คะแนน capability ประกอบจาก:

1. base score
2. domain match
3. route answer type match
4. tool router action/domain match
5. operation priority
6. Question Frame domain match
7. Question Frame operation-specific boost
8. mismatch penalty
9. policy veto
10. tool precondition

ตัวอย่าง operation priority:

```text
control_lookup -> structured.game_controls
price_lookup -> fast.price_calculator
booking_lookup -> structured.reservation
game_zone_rank -> structured.games
game_catalog -> structured.games
equipment_lookup -> structured.equipment
member_lookup -> structured.members
studio_rule_lookup -> fast.domain_handlers
```

Candidate Margin:

```text
margin = selected.score - second.score

IF ไม่มี candidate
  -> no_candidate, execution_allowed=false
ELSE IF selected.score < 0.45
  -> abstain_low_score
ELSE IF margin < 0.035 และ action ต่างกัน และ operation ยัง unknown
  -> review_required, execution_allowed=false
ELSE IF margin < 0.035
  -> selected_low_margin แต่ยัง execute ได้เมื่อ operation ชัด
ELSE
  -> selected
```

Policy Veto สำคัญ:

- `llm.general_answer` ถูกปฏิเสธสำหรับ PSU-specific หรือ medium/high-risk route
- capability ที่ต้องมี evidence ไม่ใช้กับ general route แบบไม่มี PSU target
- high-risk route ห้ามใช้ model-only `general_llm` หรือ `rag_llm`

Tool Preconditions ทำหน้าที่ตรวจว่า candidate ที่คะแนนดีมีข้อมูลขั้นต่ำจริงหรือไม่ เช่น:

- ปุ่มต้องมี control signal และ target เกมที่ใช้ได้
- ราคา calculator ต้องมี service/group/duration ตามชนิดคำถาม
- catalog เกมต้องเป็นคำถาม catalog ไม่ใช่รายละเอียดอุปกรณ์
- reservation ต้องมี booking/access signal
- competition fact card ต้องเป็นคำถามกติกาแข่งขัน

---

## 15. Backbone 12: Execution Controller

ไฟล์หลัก:

```text
app\pipeline\engine.py
```

Execution ไม่ใช่การลองทุกวิธีพร้อมกัน แต่ใช้ selected action และ precondition คุมว่าเส้นทางใดมีสิทธิ์รัน

### 15.1 Early Price Deterministic Path

ใช้เมื่อ:

```text
route = service_fee
AND มี service entity
AND operation = price_lookup/price_calculate
AND ไม่มี explicit game hint
AND selected capability = fast.price_calculator
```

Flow:

```text
calculate -> format -> validate
IF valid -> return
ELSE -> mark one bounded repair andลอง structured candidate
```

### 15.2 Structured Tool Path

ไฟล์:

```text
app\pipeline\structured_tools.py
```

Flow:

```text
evaluate_structured_tool_precondition
AND selected_action == structured หรือ early price ถูก reject
-> answer_with_structured_tool
-> optional facts composer
-> format
-> validate
-> valid: return
-> invalid: reject draft และให้ next deterministic candidate 1 ครั้ง
```

Structured domain handlers:

#### Members

- group count
- group list
- member profile
- role/position lookup
- person count
- no-data policy สำหรับ relation ที่ไม่มีหลักฐาน

#### Games

- catalog ทั้งหมดและแยก zone
- catalog ตาม machine group
- game detail/genre/how-to summary
- game availability และ zone mapping
- family/version listing
- game count/ranking per zone
- PC machine split เช่นเครื่อง 1-2 กับ 3-10

#### Game Controls

- canonical game resolution
- platform/version-aware controls
- full control list หรือ selected button
- verified source only
- no verified control data response

#### Equipment

- equipment catalog
- equipment item detail
- count และ zone
- machine grouping

#### Reservation

- วิธีจอง
- check-in/payment/cancellation policy
- session limit
- service-related booking facts

#### Schedule

- regular opening schedule
- morning/afternoon slots
- date/holiday/closure data เมื่อมี source

#### Service Fee

- ตารางราคาตาม service, duration, user group
- PC local confirmed price update
- official image prices ของ PS5, Switch, Cockpit, VR
- comparison 30 นาที/1 ชั่วโมง
- game-to-service mapping ก่อนตอบราคาเกม

### 15.3 Optional Facts-only LLM Composer

ไฟล์:

```text
app\pipeline\facts_composer.py
```

Composer รับเฉพาะ:

```text
QUESTION + ROUTE + INTENT + FACTS_JSON + DRAFT_ANSWER
```

กฎ:

- ห้ามเพิ่ม facts นอก evidence
- ต้องรักษาตัวเลข ราคา เวลา ชื่อ และ source
- ถ้า LLM ไม่พร้อม ใช้ structured draft เดิม
- ถ้า response ว่าง, prompt leak หรือ source line เปลี่ยน ให้ reject LLM output แล้วใช้ draft เดิม
- ใช้เฉพาะ mode ที่อยู่ใน `COMPOSABLE_MODES`

Composer ปิดโดยปริยาย จึงไม่ใช่คอขวดของคำถาม structured ทั่วไป

### 15.4 Game-control Vector-first

ใช้เมื่อคำถามมี control/button signal และไม่ได้เป็น rules/penalty

Flow:

```text
target/context check
-> guarded vector retrieval limit 8
-> เลือกเฉพาะ category=game_controls
-> answer_from_vector_hits
-> confidence >= 0.68
-> format + validate
-> valid: return
```

เหตุผลที่ vector-first ในหมวดนี้:

- ปุ่มเกมมีรายละเอียดหลายบรรทัดและชื่อปุ่มคล้ายกัน
- ต้องค้นเอกสารของเกม/แพลตฟอร์มที่ตรงก่อน
- ป้องกัน fast game summary ตอบแทนคำถามปุ่ม

### 15.5 Deterministic Fast / Rule Path

ไฟล์:

```text
app\runtime\fast_answer.py
app\rules\matcher.py
data\rules\*.jsonl
```

ใช้สำหรับ:

- calculator
- domain-specific deterministic answers
- exact category rules
- known policy responses
- catalog/count/comparison ที่คำนวณได้จาก structured data

ถ้า deterministic mode เป็น no-answer ที่ confidence ต่ำและ experimental RAG เปิด ระบบสามารถข้าม draft นั้นเพื่อไปค้น context เพิ่มได้

### 15.6 Competition Fact Cards

ไฟล์:

```text
app\pipeline\retrieval.py
data\competition_rules\...
data\curated\curated_competition_rules.jsonl
```

ใช้เมื่อ route เป็น `competition_rules`

Flow:

```text
retrieve_competition_fact_cards
-> score by game + intent + terms + row-specific boosts
-> answer_from_competition_fact_hits
-> confidence >= 0.72
-> format + validate
```

### 15.7 Guarded Hybrid Retrieval

ไฟล์:

```text
app\pipeline\hybrid_retrieval.py
```

องค์ประกอบคะแนน:

- lexical/BM25-like overlap
- vector score
- entity match
- route/domain compatibility
- source priority
- candidate rerank rules

ใช้เฉพาะ route ที่ `should_use_hybrid_retrieval(route)` อนุญาต

ถ้าเป็นหมวดเสี่ยงและ hybrid guard ไม่พบ verified context ระบบสามารถข้าม legacy curated direct answer แล้ว no-answer ทันที

### 15.8 Curated Direct Retrieval

Flow:

```text
retrieve_curated(query, route.category)
-> answer_from_curated_hits
-> confidence >= 0.65
-> format + validate
```

ใช้เมื่อ structured/fast/fact card/hybrid ยังไม่จบและ route ไม่ใช่ general

### 15.9 Guarded Vector Retrieval

ไฟล์:

```text
app\pipeline\vector_retrieval.py
data\vector\psu_hybrid_vector_index.json
```

Backend ปัจจุบันเป็น local hashed sparse vector ไม่ใช่ neural embedding model:

```text
word hashing + Thai/Latin tokenization + character 3/4/5-grams + cosine sparse
```

คะแนนเอกสาร:

```text
score = vector_score * 10
      + lexical_score * 3
      + entity_score * 5
      + source_priority
```

Guard:

- route category ต้องตรงกับ document category
- competition document ห้ามเข้าหมวดทั่วไป
- game_controls ต้องมี control terms
- game detail ต้องมี game entity ที่แรงพอ
- similarity ต่ำกว่า threshold ถูก block
- general/unknown/no_answer ไม่ใช้ guarded vector ของ PSU โดยตรง

### 15.10 Experimental RAG / General Local LLM

ไฟล์:

```text
app\pipeline\experimental_fallback.py
```

สองกรณีหลัก:

1. **RAG fallback**: มี curated rows ที่เกี่ยวข้องและ policy อนุญาต
2. **General Local LLM**: คำถามเป็น general non-PSU จริง และเปิด LLM

ข้อห้าม:

- General LLM ห้ามใช้ตอบ facts ของ PSU
- Medium/high-risk PSU route ห้ามส่งเข้า model-only answer
- ถ้าไม่มี verified context ให้ no-answer แทนการยืมข้อมูลใกล้เคียง

### 15.11 Safe No-answer

ใช้เมื่อ:

- ไม่มี candidate ที่ปลอดภัย
- target ขาดและไม่ควรเดา
- retrieval ไม่ผ่าน threshold
- source/evidence ไม่พอ
- LLM ปิด ล้ม timeout หรือ circuit breaker เปิด
- Answer Contract hard veto คำตอบสุดท้าย

---

## 16. Backbone 13: Retrieval และ Data Backbones

### 16.1 Structured/Curated Data

โฟลเดอร์หลัก:

```text
data\curated
data\control_game
data\competition_rules
data\calendar
data\sources
data\rules
data\routing
data\intent
data\vector
```

ไฟล์สำคัญ:

| ไฟล์ | หน้าที่ |
|---|---|
| `curated\game_item_details.jsonl` | รายละเอียดเกม |
| `curated\service_game_availability.jsonl` | เกมอยู่ service/zone/machine ใด |
| `curated\game_control_facts.jsonl` | ปุ่มที่ normalize แล้ว |
| `curated\game_title_aliases.jsonl` | alias และชื่อ canonical |
| `curated\equipment_item_details.jsonl` | อุปกรณ์และรายละเอียด |
| `curated\member_profiles.jsonl` | สมาชิก/ทีมงาน/ตำแหน่ง |
| `curated\curated_competition_rules.jsonl` | fact card การแข่งขัน |
| `routing\route_priority_matrix.json` | operation/domain priority |
| `intent\semantic_intents.jsonl` | semantic intent examples |
| `calendar\service_closures.jsonl` | วันปิดพิเศษ |
| `calendar\thai_holidays_*.jsonl` | ปฏิทินวันหยุด |
| `vector\psu_hybrid_vector_index.json` | vector index ปัจจุบัน |

### 16.2 Source Registry / Source Contract

ไฟล์:

```text
app\core\source_registry.py
```

Source Registry เก็บ:

```text
source_id
category
title
source_url
source_type
trust_level
updated_at
origin
description
```

ตัวอย่าง source ที่ register โดยตรง:

- official service fee image 2026
- user-confirmed PC service fee update 2026-07-27

Source Contract ช่วยให้คำตอบราคาและ facts สำคัญไม่เป็นเพียงข้อความที่ไม่มีที่มา

---

## 17. Backbone 14: Formatter, Answer Validator และ Answer Contract

ไฟล์หลัก:

```text
app\pipeline\formatter.py
app\pipeline\validator.py
app\pipeline\answer_contracts.py
app\pipeline\style.py
```

### 17.1 Formatter

- trim คำตอบ
- ใช้ no-answer template เมื่อข้อความว่าง
- รองรับ short answer
- append source URL เมื่อเหมาะสม
- ไม่ append source ให้ no-answer บางชนิด

### 17.2 Base Answer Validator

ตรวจความผิดข้ามหมวด เช่น:

- ถามราคาแต่ตอบ catalog เกม
- ถามปุ่มแต่ตอบรายละเอียดเกมทั่วไป
- ถามจองแต่ตอบนโยบายยกเลิกคนละประเด็น
- ถามคน/ตำแหน่งแต่ตอบอุปกรณ์
- broad query ควรถามกลับแต่ระบบกลับตอบ fact เฉพาะ
- source id/category ไม่สอดคล้องกับคำตอบ

### 17.3 Answer-Type Contract

Input:

```text
question
answer
route
hits
mode
universal_intent
question_frame
```

ตรวจ:

1. actual answer type ต้อง intersect กับ expected answer types
2. ถ้า Frame บอก `needs_clarification` คำตอบต้องเป็น clarification/no-answer
3. ถ้ามี exact target คำตอบต้องกล่าวถึง target ที่ถูกต้อง
4. PSU answer ที่ไม่ใช่ safe type ต้องมี evidence
5. source category ต้องตรง operation
6. game ranking ต้องมี ranked result
7. structured game control mode ต้องมี controls จริง

ตัวอย่าง source category contract:

```text
control_lookup -> game_controls
price_lookup -> service_fee / official_image / local_fact_update
booking_lookup -> reservation / games
schedule_lookup -> schedule / reservation
game_catalog -> games
equipment_lookup -> equipment
member_lookup -> members / overview
competition_rule_lookup -> competition_rules / rules
penalty_lookup -> penalty / rules
```

---

## 18. Backbone 15: Bounded Repair และ Final Hard Veto

ระบบไม่วนทำจนกว่าจะผ่านแบบไม่มีขีดจำกัด

### 18.1 Bounded Repair ระหว่าง Execution

กรณี early price หรือ structured draft ไม่ผ่าน validator:

```text
attempt = 1
max_attempts = 1
-> mark rejected capability
-> เปิดให้ next deterministic candidate รัน
```

จุดประสงค์:

- ป้องกัน infinite loop
- จำกัด latency
- ไม่เรียก LLM ซ้ำไปเรื่อย ๆ
- ให้มีโอกาสกู้คำตอบจาก candidate ที่ปลอดภัยกว่าเพียงหนึ่งครั้ง

### 18.2 Final Validation ใน `_build_result()`

ก่อนสร้าง `PipelineAnswer` ระบบตรวจ source/answer อีกครั้ง

```text
IF final validation ผ่าน
  -> สร้าง decision artifact
  -> ทำ Thai style formatting
  -> return
ELSE
  -> hard_veto_to_no_answer
  -> ล้าง hits
  -> เปลี่ยน mode เป็น pipeline:answer_contract_no_answer
  -> ลด confidence
  -> บันทึก draft_rejected_by_answer_contract
```

ดังนั้นคำตอบผิดซ้ำไม่ได้ทำให้ pipeline วนจนหมดเวลา แต่จะจบด้วย no-answer ที่ตรวจสอบได้

---

## 19. Backbone 16: LLM Health Manager และ Circuit Breaker

ไฟล์หลัก:

```text
app\pipeline\llm_health.py
app\pipeline\warmup.py
```

LLM kind ที่ติดตามแยกกัน:

- preflight
- intent
- tool_router
- facts_composer
- rag_llm
- general_llm

กลไก:

1. บันทึก success/failure ต่อ kind และต่อ model
2. ถ้าล้มเหลวถึง threshold เปิด cooldown
3. ระหว่าง cooldown `llm_call_allowed()` คืน false
4. pipeline ใช้ heuristic/draft/no-answer ต่อโดยไม่รอ model
5. success รีเซ็ต failure counter
6. ทุก call บันทึก model, timeout, prompt chars, elapsed, response chars และ error type

ค่า default สำคัญ:

```text
failure threshold = 2
cooldown = 90 วินาที
preflight timeout = 5 วินาทีใน Local CLI
```

Preflight เกิดตอนเริ่ม process ไม่ได้เกิดทุกคำถามใน process เดิม ส่วน warmup โหลด cache/index ที่ใช้บ่อยเพื่อไม่ให้คำถามแรกจ่าย cold-start cost เต็ม

---

## 20. Backbone 17: Decision Artifact, Trace, Metrics และ Logging

ไฟล์หลัก:

```text
app\pipeline\decision_artifact.py
app\session\chat_logger.py
tools\report_chat_quality_metrics.py
```

Decision Artifact เก็บ:

```text
intent
route
tool_router
selected_candidate
candidates
rejected
policy
execution_plan
final mode/capability
validation
evidence/source ids
entities
tool preconditions
candidate execution
LLM calls
production metrics
```

Production metrics ปัจจุบัน:

- outcome: answered / clarification / no_answer / timeout
- quality_gate_status: pass / safe_abstain / reject
- candidate_margin
- selection_status
- ambiguity_decision
- repair_attempted
- repair_recovered
- llm_call_count
- requires_shadow_review
- shadow_review_reasons

Timing Trace แยกเวลาอย่างน้อย:

- split
- preprocess
- active route selection
- guard
- universal intent
- tool router
- ambiguity gate
- question frame
- candidate decisions
- precondition
- structured execution
- facts composer
- deterministic
- retrieval/answer
- format
- validation
- build result

Chat Log sinks:

| Sink | Default/เงื่อนไข |
|---|---|
| Local JSONL | เปิดโดยปริยาย |
| SQLite | เปิดโดยปริยาย |
| Postgres | เปิดเมื่อมี URL และ flag |
| stdout | ปิดโดยปริยาย |
| webhook | เปิดเมื่อมี URL |

Logging failure ถูกจับเป็น metadata และต้องไม่ทำให้ผู้ใช้ไม่ได้คำตอบ

---

## 21. จุดที่ LLM และ Model ถูกใช้จริง

| จุด | ใช้ทำอะไร | เรียกเมื่อใด | มีสิทธิ์สร้าง PSU facts หรือไม่ |
|---|---|---|---|
| Adaptive Intent LLM | เลือก intent candidate | weak/mixed/ambiguous route เท่านั้น | ไม่มี |
| LLM Tool Router | เสนอ action/domain | heuristic ยังไม่ชัดและ gate เปิด | ไม่มี |
| Facts Composer | เรียบเรียง structured draft | เปิด composer, mode รองรับ, มี facts | ไม่มี เพิ่ม facts ไม่ได้ |
| Entity CrossEncoder | rerank target candidate | entity ambiguous และ gated scope | ไม่ใช่ตัวตอบ |
| RAG LLM fallback | ตอบจาก retrieved context | experimental path และ policy อนุญาต | ใช้ได้เฉพาะ context |
| General Local LLM | ความรู้ทั่วไป | route=general non-PSU | ห้ามตอบ PSU facts |

คำถาม structured ทั่วไปจึงอาจมี `llm_call_count = 0` แม้ระบบเปิด LLM อยู่ และนี่เป็นพฤติกรรมที่ตั้งใจเพื่อความเร็วและความถูกต้อง

ตำแหน่งที่ **ไม่ใช่ LLM**:

- normalization/alias/typo
- heuristic router
- semantic char n-gram intent
- ambiguity candidate scoring
- Question Frame
- tool preconditions
- structured tools
- calculator
- rule matcher
- hashed sparse vector retrieval
- Answer Validator/Contract
- formatter/logging

---

## 22. เส้นทาง IF/ELSE ฉบับละเอียด

```text
FUNCTION CHAT(question, session_history):

  resolved = SESSION_CONTEXT_RESOLVER(question, session_history)
  START global_deadline

  parts = SPLIT_COMPOUND(resolved.question)

  IF parts.count > 1:
      FOR part IN parts:
          IF deadline exhausted:
              RETURN timeout-safe-answer
          child_result = SINGLE_PIPELINE(part)
      RETURN merge_children_as_numbered_answer()

  RETURN SINGLE_PIPELINE(resolved.question)


FUNCTION SINGLE_PIPELINE(question):

  original_pre = PREPROCESS(question)
  pre, entities, route = SELECT_BEST_QUERY_VARIANT(original_pre)

  IF deadline exhausted:
      RETURN timeout-safe-answer

  guard = SCOPE_GUARD(pre, entities)
  IF guard.confidence >= 0.90 AND guard.has_answer:
      RETURN guard-answer OR policy-safe experimental fallback

  intent = UNIVERSAL_INTENT_HEURISTIC(pre, route)
  IF weak_or_ambiguous AND intent_llm_enabled AND llm_healthy AND deadline_available:
      llm_intent = LLM_SELECT_FROM_CANDIDATES()
      IF llm_intent parsed and valid:
          intent = llm_intent

  route = REFINE_ROUTE(route, intent)

  tool = HEURISTIC_TOOL_ROUTER(route, intent)
  IF tool_router_llm_gate allows:
      llm_tool = OPTIONAL_LLM_TOOL_ROUTER()
      IF parsed and valid:
          tool = llm_tool

  IF tool requests clarification with sufficient confidence:
      RETURN clarification

  ambiguity = AMBIGUITY_GATE(route, intent, entities, tool)
  IF ambiguity.action == clarify:
      RETURN clarification + optional verified preview

  frame = BUILD_QUESTION_FRAME(question, route, intent)
  target = RESOLVE_TARGET(question, frame.operation)

  IF target ambiguous AND gated_entity_reranker_enabled:
      target = CROSS_ENCODER_RERANK(target_candidates)

  IF frame exact target AND intent target empty:
      ENRICH intent with resolved target

  IF route weak AND frame confidence >= 0.85:
      REFINE route by operation-first frame

  candidates = SCORE_ALL_CAPABILITIES(route, intent, tool, frame)
  candidates = APPLY_POLICY_VETO(candidates)
  candidates = APPLY_TOOL_PRECONDITIONS(candidates)
  selected, second, margin = RANK(candidates)

  IF selected low score:
      RETURN clarification/no-answer

  IF margin too low AND action differs AND frame.operation unknown:
      RETURN clarification

  IF selected == fast.price_calculator AND early_price_conditions:
      draft = PRICE_CALCULATOR()
      formatted = FORMAT(draft)
      IF VALIDATE(formatted):
          RETURN BUILD_RESULT(formatted)
      ELSE:
          MARK one bounded repair

  IF selected.action == structured OR early_price_rejected:
      IF STRUCTURED_PRECONDITION passes:
          draft = STRUCTURED_TOOL()
          IF facts_composer_enabled AND LLM allowed:
              candidate_text = FACTS_ONLY_COMPOSER(draft, evidence)
              IF composer output unsafe:
                  candidate_text = draft
          formatted = FORMAT(candidate_text)
          IF VALIDATE(formatted):
              RETURN BUILD_RESULT(formatted)
          ELSE:
              MARK one bounded repair
              TRY next deterministic candidate only

  IF broad_game_meta_without_target:
      RETURN clarification

  IF control question missing game target:
      RETURN game-target clarification or verified no-data

  IF control question:
      hits = GUARDED_VECTOR_RETRIEVAL(game_controls)
      answer = BUILD_FROM_VECTOR(hits)
      IF confidence >= threshold AND VALIDATE(answer):
          RETURN BUILD_RESULT(answer)

  IF selected action permits fast/rule OR structured repair:
      answer = DETERMINISTIC_FAST_RULE()
      IF unknown-game draft:
          TRY guarded-vector override
      IF valid answer:
          RETURN BUILD_RESULT(answer)

  IF route == competition_rules:
      answer = COMPETITION_FACT_CARDS()
      IF confidence >= threshold AND VALIDATE(answer):
          RETURN BUILD_RESULT(answer)

  IF hybrid route allowed:
      answer = GUARDED_HYBRID_RETRIEVAL()
      IF confidence >= threshold AND VALIDATE(answer):
          RETURN BUILD_RESULT(answer)
      IF high-risk hybrid failed:
          RETURN safe-no-answer

  IF route == general:
      IF experimental fallback AND LLM policy allows:
          RETURN GENERAL_LOCAL_LLM_OR_GENERAL_SAFE_FALLBACK
      RETURN general-no-answer

  answer = CURATED_DIRECT_RETRIEVAL()
  IF confidence >= threshold AND VALIDATE(answer):
      RETURN BUILD_RESULT(answer)

  answer = GUARDED_VECTOR_DIRECT()
  IF confidence >= threshold AND VALIDATE(answer):
      RETURN BUILD_RESULT(answer)

  IF experimental fallback enabled:
      answer = EXPERIMENTAL_RAG_FALLBACK()
      RETURN BUILD_RESULT(answer)

  RETURN safe-no-answer


FUNCTION BUILD_RESULT(answer, hits, route, mode):

  final_validation = VALIDATE_SOURCE_AND_ANSWER_AGAIN()

  IF final_validation failed:
      answer = safe-no-answer
      hits = []
      mode = answer_contract_no_answer
      route = no_answer

  artifact = BUILD_DECISION_ARTIFACT()
  answer = FORMAT_THAI_RESPONSE_STYLE(answer)
  trace total timing
  RETURN PipelineAnswer
```

---

## 23. ตัวอย่าง Trace ตามชนิดคำถาม

### 23.1 `PC นักศึกษา PSU ราคาเท่าไหร่`

```text
session
-> preprocess
-> entities: service=PC, group=PSU, price=true
-> route=service_fee
-> intent=service_fee/price_calculate
-> ambiguity allow
-> frame=price_lookup
-> selected=fast.price_calculator
-> PC price source contract
-> format
-> validate
-> final answer
```

LLM ไม่จำเป็น

### 23.2 `Gran Turismo 7 ปุ่มอะไรบ้าง`

```text
preprocess
-> game target exact
-> operation=control_lookup
-> selected=structured.game_controls หรือ game-control vector-first
-> retrieve only Gran Turismo 7 control rows
-> target/source/type validation
-> final answer
```

ห้ามตอบปุ่มเกมอื่น ถ้าไม่พบข้อมูลต้อง no-answer ของ Gran Turismo 7

### 23.3 ถาม `Gran Turismo 7 เล่นยังไง` แล้วถามต่อ `ปุ่ม`

```text
turn 1: game detail/how-to -> answer and save context
turn 2: session resolver detects short control follow-up
-> resolved question = Gran Turismo 7 ปุ่มอะไรบ้าง
-> normal single pipeline
```

### 23.4 `PC มีอะไรบ้าง`

```text
service target=PC
operation broad
-> Ambiguity Gate detects missing operation
-> clarification preview: เกม/อุปกรณ์/ราคา/จอง
-> save pending clarification latest-turn only
```

### 23.5 `อุปกรณ์ไหนเกมเยอะสุด`

```text
operation-first = game_zone_rank
-> domain=games ไม่ใช่ equipment catalog
-> structured.games
-> count unique games per zone/machine group
-> answer type must include ranking/list/calculation
```

### 23.6 `TEKKEN 8 ปุ่มอะไร และ VR ราคา 1 ชั่วโมงเท่าไหร่`

```text
compound splitter -> 2 child questions
child 1 -> controls path
child 2 -> service fee path
merge answer + dedupe sources
```

### 23.7 `อธิบาย quantum computing`

```text
route=general
-> PSU retrieval blocked
-> optional General Local LLM
-> ถ้า LLM unavailable: general-safe unavailable/no-answer
```

---

## 24. Safety Invariants ที่ห้ามเปลี่ยนโดยไม่ตั้งใจ

1. PSU-specific facts ต้องมี evidence หรือ source contract
2. General LLM ห้ามตอบแทนข้อมูล PSU
3. คำถามปุ่มต้องมี target เกมที่ชัดหรือถามกลับ
4. ชื่อเกมที่ไม่มี control data ห้ามยืมปุ่มจากเกมใกล้เคียง
5. ราคาเกมต้อง map ไป service/zone ก่อน ไม่ถือว่าเกมมีราคาโดยตรง
6. Operation ชัดต้องมี priority เหนือ noun ที่กว้าง เช่น `ปุ่ม Naruto` ต้องเป็น controls ไม่ใช่ game detail
7. Exact canonical title ต้องชนะ fuzzy/family candidate
8. Low margin ที่ operation unknown ต้อง abstain
9. Validator fail ต้องไม่วนไม่สิ้นสุด
10. Final Answer Contract fail ต้อง hard veto เป็น no-answer
11. Deadline หมดต้องไม่เริ่ม LLM/retrieval หนักเพิ่ม
12. คำตอบจาก rule/fast/structured/RAG ห้ามอ้างว่าเป็นคำตอบจาก LLM

---

## 25. สถานะระบบล่าสุดที่เกี่ยวข้องกับ Flow นี้

ผล verification ล่าสุดที่มีในโปรเจกต์ ณ วันที่ 2026-08-03:

```text
Model benchmark/core PSU dataset: 1325/1325 ผ่าน
Full generated dataset: 1600 cases
Real Usage Golden Eval: 24/24 ผ่าน
Core PSU benchmark LLM calls: 0
Average latency: ประมาณ 0.5443 วินาที
P95 latency: ประมาณ 1.0222 วินาที
Maximum observed: ประมาณ 8.2799 วินาที
```

ความหมายของผลนี้:

- ชุดทดสอบ core ที่มีอยู่ผ่านทั้งหมดใน run นั้น
- ไม่ได้แปลว่าคำถาม production ที่ไม่เคยเห็นจะถูก 100%
- การที่ LLM calls เป็น 0 แสดงว่า core PSU facts ถูกตอบด้วย deterministic/structured/retrieval path
- ยังต้องเก็บ unknown real-user traffic, shadow review และ failure clusters ต่อเนื่องก่อน production เต็มรูปแบบ

Report อ้างอิง:

```text
reports\model_benchmark\20260803_213849\REPORT.md
```

---

## 26. File-to-Process Map

| Process | ไฟล์หลัก |
|---|---|
| CLI entry | `tools/local_ai_chat.py` |
| Startup config | `start_local_ai_chat.ps1` |
| Web entry | `app/web_api/server.py` |
| Session context | `app/session/context_resolver.py` |
| Chat logging | `app/session/chat_logger.py` |
| Pipeline orchestrator | `app/pipeline/engine.py` |
| Deadline | `app/pipeline/request_deadline.py` |
| Preprocess/entity basics | `app/pipeline/preprocess.py` |
| Heuristic router | `app/pipeline/router.py` |
| Routing priority | `app/pipeline/routing_policy.py` |
| Semantic intent | `app/pipeline/semantic_intent.py` |
| Universal intent/Intent LLM | `app/pipeline/universal_intent.py` |
| Tool Router | `app/pipeline/llm_tool_router.py` |
| Ambiguity Gate | `app/pipeline/ambiguity_gate.py` |
| Question Frame | `app/pipeline/question_frame.py` |
| Target Resolver | `app/pipeline/target_resolver.py` |
| Entity Resolver/Reranker | `app/pipeline/entity_resolver.py` |
| Capability scoring | `app/pipeline/capability_registry.py` |
| Tool preconditions | `app/pipeline/tool_preconditions.py` |
| Structured tools | `app/pipeline/structured_tools.py` |
| Fast answers | `app/runtime/fast_answer.py` |
| Rules | `app/rules/matcher.py` |
| Curated/fact retrieval | `app/pipeline/retrieval.py` |
| Hybrid retrieval | `app/pipeline/hybrid_retrieval.py` |
| Vector retrieval | `app/pipeline/vector_retrieval.py` |
| Facts composer | `app/pipeline/facts_composer.py` |
| General/RAG fallback | `app/pipeline/experimental_fallback.py` |
| LLM health | `app/pipeline/llm_health.py` |
| Formatter | `app/pipeline/formatter.py` |
| Validator | `app/pipeline/validator.py` |
| Answer Contract | `app/pipeline/answer_contracts.py` |
| Decision Artifact | `app/pipeline/decision_artifact.py` |

---

## 27. สรุปสุดท้าย

Flow ปัจจุบันเป็นระบบ **rule/scoring-first, evidence-grounded, LLM-optional และ abstain-capable**

Backbone สำคัญไม่ได้อยู่ที่ LLM เพียงตัวเดียว แต่อยู่ที่การประกอบกันของ:

```text
Session Context
+ Compound Planning
+ Normalization/Entity Resolution
+ Multi-stage Routing
+ Ambiguity and Margin Control
+ Question/Answer Contract
+ Capability Ranking and Preconditions
+ Structured/Fast/RAG Execution
+ Bounded Repair
+ Source-aware Validation
+ Observability
```

LLM ช่วยตรงจุดที่ความยืดหยุ่นมีประโยชน์ แต่ข้อมูล PSU ที่ยืนยันได้ยังถูกควบคุมด้วย structured data, retrieval guards, source contract และ final hard veto เป็นหลัก
