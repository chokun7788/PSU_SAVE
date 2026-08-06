# PSU Esports Chatbot - Current Project All-in-One Handoff

## สถานะ ณ วันที่ 06/08/2026

เอกสารนี้คือ handoff ล่าสุดสำหรับรับช่วงโปรเจกต์ PSU Esports Chatbot ต่อจาก session เดิม

ถ้าข้อมูลในไฟล์ handoff วันที่ 23/07/2026 ขัดกับไฟล์นี้ ให้ยึดไฟล์นี้และ daily log วันที่ 03-05/08/2026 เป็นหลัก เพราะมีการแก้ architecture, model, game catalog และ runtime controls หลังจาก handoff เดิม

---

## 1. โปรเจกต์นี้คืออะไร

โปรเจกต์นี้คือ chatbot สำหรับ PSU Esports Studio - Phuket โดยเน้นใช้งานแบบ local-first และตอบคำถามจากข้อมูลที่ตรวจสอบได้ เช่น:

- ราคาใช้บริการและการคำนวณราคา
- เวลาเปิด-ปิดและวันให้บริการ
- วิธีจอง เช็กอิน ชำระเงิน และ policy การจอง
- รายชื่อเกม เกมอยู่โซนไหน และเครื่องใดมีเกมอะไร
- อุปกรณ์ จำนวนเครื่อง รุ่น และวิธีใช้งาน
- วิธีเล่นและปุ่มควบคุมเกม
- สมาชิก ทีมงาน ตำแหน่ง และผู้รับผิดชอบ
- กฎของ Studio และกติกาการแข่งขัน
- คำถามหลายเรื่องในประโยคเดียว
- คำถาม follow-up ที่อ้างบริบทก่อนหน้า
- คำถามทั่วไปบางประเภทผ่าน Local LLM เมื่อผ่าน boundary policy

ระบบไม่ได้ให้ LLM ตอบทุกอย่างโดยตรง แต่ใช้ pipeline หลายชั้นเพื่อให้ข้อมูล PSU ถูกต้องและตรวจสอบแหล่งที่มาได้

---

## 2. Requirement ของผู้ใช้ที่ต้องรักษา

- ตอบผู้ใช้เป็นภาษาไทย
- ใช้ answer-first: ตอบคำตอบหลักก่อนรายละเอียด
- ไม่เวิ่นเว้อ แต่ต้องอธิบายให้ครบเมื่อผู้ใช้ขอรายละเอียด
- ถ้าไม่มีข้อมูลจริงของ PSU Esports Studio - Phuket ห้ามเดา
- ถ้าคำตอบมาจาก rule, fast path, structured tool หรือ RAG ห้ามบอกผู้ใช้ว่าเป็น LLM
- ถ้าคำถามกำกวมและไม่มี evidence พอ ให้ถามกลับหรือ no-answer
- งานที่มีสาระต้องอัปเดต daily log โดยเพิ่มสรุปล่าสุดไว้ด้านบนของไฟล์วันนั้น
- ไม่ต้องบอกผู้ใช้ทุกครั้งว่าเขียน daily log หรือรัน test อะไร เว้นแต่ผู้ใช้ถาม
- อย่าแก้ test หรือ validator ให้ผ่านง่าย ต้องแก้ logic/data ที่ root cause
- ไม่ใช้ git, commit, push, reset หรือ deploy ถ้าผู้ใช้ไม่ได้สั่ง
- ไม่ยุ่ง Vercel/deploy folder ถ้าผู้ใช้ไม่ได้สั่งใหม่
- ถ้าคำตอบผิด ให้ตรวจ mode, route, intent, target, source, trace และ validator ก่อนแก้
- หลีกเลี่ยงการเพิ่ม keyword rule เฉพาะเคสซ้ำ ๆ ถ้าปัญหาเป็น pattern ระดับระบบ

---

## 3. Path สำคัญและแต่ละ path คืออะไร

### Root รวม

```text
C:\Users\Chokhun\Downloads\Learn-LLM
```

เป็นโฟลเดอร์รวม source, daily logs, handoff และงานรุ่นก่อนหน้า

### Source หลักที่ต้องแก้และทดสอบ

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data
```

ใช้สำหรับ:

- แก้โค้ด chatbot
- แก้ curated data
- รัน local chat
- รัน smoke tests/evaluation
- ดู reports
- ดู notebook และ flow documentation

### Daily logs

```text
C:\Users\Chokhun\Downloads\Learn-LLM\17_PSU_Esports_Daily_Logs
```

ใช้เก็บบันทึกรายวันว่าวันนั้นเพิ่มอะไร แก้อะไร ใช้เทคนิคไหน ผลทดสอบเป็นอย่างไร และยังมีข้อจำกัดอะไร

ไฟล์สำคัญล่าสุด:

```text
2026-08-03.md
2026-08-04.md
2026-08-05.md
2026-08-06.md
```

### Handoff folder

```text
C:\Users\Chokhun\Downloads\Learn-LLM\23_PSU_Esports_Handoff_Summary_20260723
```

ไฟล์เก่า 00-09 อธิบายฐานระบบถึงวันที่ 23/07/2026 ส่วนสถานะล่าสุดให้ยึด:

```text
10_CURRENT_PROJECT_ALL_IN_ONE_20260806.md
11_COPY_PASTE_PROMPT_FOR_NEXT_SESSION_20260806.md
```

### Entry point สำหรับ local chat

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\start_local_ai_chat.ps1
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\tools\local_ai_chat.py
```

รันจาก PowerShell:

```powershell
cd C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data
.\start_local_ai_chat.ps1
```

### Notebook

```text
notebooks\04_local_hybrid_chat_debug.ipynb
```

ใช้ทดลองถามแบบ interactive, ดู trace และใช้ session context

### Flow documentation ล่าสุด

```text
docs\38_current_chatbot_full_process_flow_20260803.md
docs\current_chatbot_full_process_flow_th_20260803.png
docs\33_current_chatbot_full_architecture_flow_20260727.md
docs\current_chatbot_flow_th_20260727.svg
```

หมายเหตุ: Flow วันที่ 03/08 ละเอียดที่สุดก่อนเพิ่ม Compound Complexity/Concurrency วันที่ 05/08 ดังนั้นต้องอ่านไฟล์นี้ประกอบ

### Model/reranker cache

```text
D:\AIModels\huggingface
```

ใช้เป็น cache ของ optional BGE Entity Reranker ตามค่า `PSU_ENTITY_RERANKER_CACHE_DIR`

---

## 4. Core code map

### Pipeline หลัก

```text
app\pipeline\engine.py
```

ควบคุม flow ตั้งแต่ split, planner, preprocess, route, candidate execution, retrieval, validation จนสร้างคำตอบสุดท้าย

### Compound planning/execution

```text
app\pipeline\compound_execution.py
app\pipeline\query_planner.py
```

- `compound_execution.py`: ประเมิน simple/complex, dependency และ bounded parallel policy
- `query_planner.py`: Constrained Local LLM Planner ที่คืน task/domain/operation แบบ JSON แล้วตรวจด้วย schema/allowlist

### Runtime deadline และ LLM controls

```text
app\pipeline\request_deadline.py
app\pipeline\llm_health.py
```

- `request_deadline.py`: global timeout และ per-request LLM call budget
- `llm_health.py`: health state, circuit breaker และ Local LLM concurrency guard

### Preprocess/entity/route

```text
app\pipeline\preprocess.py
app\core\normalization.py
app\pipeline\game_title_correction.py
app\pipeline\entity_resolver.py
app\pipeline\router.py
app\pipeline\routing_policy.py
app\pipeline\universal_intent.py
```

- normalize ภาษาไทย/อังกฤษ
- alias/typo/query variants
- แก้ชื่อเกมและ family ambiguity
- resolve target/entity
- heuristic route
- route priority และ optional Intent LLM review

### Safety/correctness selection

```text
app\pipeline\boundary_guard.py
app\pipeline\ambiguity_gate.py
app\pipeline\question_frame.py
app\pipeline\capability_registry.py
app\pipeline\tool_preconditions.py
app\pipeline\answer_contracts.py
app\pipeline\validator.py
app\pipeline\decision_artifact.py
```

ใช้สำหรับ:

- scope/sensitive/safety guard
- ambiguity detection และ clarification
- candidate scoring + margin
- tool preconditions
- answer-type/source/route contract
- bounded repair และ hard veto
- trace ว่าทำไมเลือกหรือปฏิเสธ candidate

### Answer execution

```text
app\pipeline\structured_tools.py
app\runtime\fast_answer.py
app\rules\matcher.py
```

- Structured tools: games, controls, equipment, members, reservation, price, schedule
- Fast/rule: deterministic answers ที่ควรเร็วและแม่น

### RAG/retrieval/rerank

```text
app\pipeline\retrieval.py
app\pipeline\vector_retrieval.py
app\pipeline\hybrid_retrieval.py
app\pipeline\target_resolver.py
```

- curated retrieval และ competition fact cards
- local hashed sparse/char n-gram vector retrieval
- guarded hybrid retrieval
- optional BGE reranker เฉพาะ gated low-margin/entity ambiguity

Vector ปัจจุบันยังไม่ใช่ semantic embedding model เต็มรูปแบบ

### Optional LLM modules

```text
app\pipeline\llm_tool_router.py
app\pipeline\facts_composer.py
app\pipeline\experimental_fallback.py
app\pipeline\shadow_critic.py
```

- Tool Router: ช่วยเลือก action เฉพาะ route ที่ไม่แน่ใจ
- Facts Composer: เรียบเรียงจาก verified facts เท่านั้น
- Experimental/general fallback: general Local LLM หรือ RAG LLM ตาม policy
- Shadow Critic: ตรวจผลแบบ offline/background ไม่เพิ่ม latency ให้ผู้ใช้ปกติ

### Session/logging

```text
app\session\context_resolver.py
app\session\chat_logger.py
app\web_api\server.py
```

- resolve follow-up จาก session history
- log message/trace/session
- web API รองรับ `client_session_id`

Restart local chat จะสร้าง live session ใหม่ แม้ log ของ session เก่ายังอยู่

---

## 5. Data map

### Curated facts

```text
data\curated\curated_facts.jsonl
data\curated\equipment_item_details.jsonl
data\curated\game_item_details.jsonl
data\curated\our_games_scraped_details.jsonl
data\curated\service_game_availability.jsonl
data\curated\game_title_aliases.jsonl
data\curated\game_control_facts.jsonl
data\curated\member_profiles.jsonl
data\curated\curated_competition_rules.jsonl
```

### Game controls ต้นทาง

```text
data\control_game
data\control_game_split\ps5
data\control_game_split\nintendo
```

JSON/JSONL ในส่วนนี้เก็บปุ่ม เกม แพลตฟอร์ม และ source URL

### Competition rules

```text
data\competition_rules\competition_rule_fact_cards.jsonl
data\competition_rules\competition_rule_chunks.jsonl
```

### Vector index

```text
data\vector\psu_hybrid_vector_index.json
```

### Evaluation bank

```text
data\eval\model_benchmark_1500.jsonl
data\eval\model_benchmark_1500.json
```

ชื่อไฟล์เดิมมีคำว่า 1500 แต่ชุดปัจจุบันถูก regenerate เป็นประมาณ 1,600 cases โดยแบ่ง core PSU และ general LLM

---

## 6. Current chatbot flow ณ 06/08/2026

```text
User Input
-> Session Context Resolver
-> Global Request Deadline + per-request LLM budget
-> Boundary-aware multi-question splitter
-> Compound Complexity Gate
   -> simple independent parts: deterministic preflight + bounded parallel
   -> complex/dependent parts: constrained Query Planner + ordered execution
-> Compound Reference Resolver เช่น เกมนั้น/เครื่องนั้น/อันเดิม
-> Preprocess / normalization / typo / aliases / query variants
-> Game title correction + entity/target extraction
-> Heuristic Router + Routing Priority Policy
-> Universal Intent
   -> exact/strong route: skip Intent LLM
   -> weak/broad/ambiguous: optional Intent LLM review
-> Boundary Guard / Ambiguity Gate
-> Question Frame + Target Resolver
-> Capability Candidate Scoring + Margin Threshold
-> Policy Veto + Tool Preconditions
-> Execute selected capability
   -> Structured Tools
   -> Fast/Rule
   -> Curated RAG / Competition Fact Cards
   -> Vector / Hybrid Retrieval / gated rerank
   -> Optional Facts Composer
   -> General Local LLM fallback เฉพาะ route ที่ policy อนุญาต
-> Answer Contract + Source/Route/Target Cross-check
-> Bounded Repair สูงสุด 1 ครั้ง
-> Final Hard Veto -> clarification/no-answer หากยังไม่ผ่าน
-> Thai format + source + trace + decision artifact + log
-> Final Answer
```

### Compound flow

ตัวอย่าง simple independent:

```text
PC ราคาเท่าไหร่ แล้วจองยังไง
```

- deterministic splitter แยกได้ 2 parts
- preflight ยืนยันว่าเป็น structured/fast
- รัน child แบบ bounded parallel สูงสุด 2 workers
- child ไม่เรียก LLM/RAG fallback โดยไม่จำเป็น

ตัวอย่าง complex/dependent:

```text
อุปกรณ์ไหนเกมเยอะสุด แล้วราคาเครื่องนั้นเท่าไหร่
```

- Complexity Gate พบ ranking + reference
- Query Planner มีงบสูงสุด 4 วินาทีสำหรับ complex case
- ถ้า Planner timeout/invalid ให้ deterministic fallback และไม่เรียก child Intent LLM ซ้ำ
- ทำ child ตาม dependency
- ถ้าผลแรกเสมอกันหลายโซน จะถามให้เลือกแทนการเดา

ตัวอย่าง evidence-grounded reference:

```text
Tekken 8 เล่นที่ไหน แล้วเกมนั้นมีปุ่มอะไร
```

- child แรกคืน evidence ของ TEKKEN 8
- reference resolver เติม TEKKEN 8 ให้ child ถัดไป
- ถ้าไม่มี evidence ชื่อเดียวที่ชัด ระบบจะถามกลับ

---

## 7. Local LLM ใช้ที่ไหน

Default model ปัจจุบัน:

```text
scb10x/typhoon2.5-qwen3-4b
```

โมเดลนี้แทนค่า default เก่า `qwen2.5:3b` หลังผล benchmark ของโปรเจกต์

Local LLM ใช้เฉพาะ:

1. Query Planner สำหรับ complex compound/weak decomposition
2. Universal Intent review สำหรับ weak/broad/ambiguous route
3. Optional Tool Router
4. Optional Facts-only Composer จาก verified facts
5. General Local LLM fallback ที่ผ่าน boundary และ PSU-safety policy
6. Optional RAG LLM เมื่อมี context ที่ผ่าน retrieval guard
7. Shadow Critic/Failure Analyst ในการทดสอบ ไม่ใช่คำตอบหลักทุกครั้ง

Local LLM ไม่ควรใช้แทน structured facts สำหรับราคา เกม ปุ่ม สมาชิก ตารางเวลา หรือข้อมูล PSU ที่มี source อยู่แล้ว

### Runtime controls ปัจจุบัน

```text
Global request timeout: 20 วินาที
General LLM timeout: 20 วินาที
Per-request LLM max calls: 2
LLM max concurrency: 1
LLM slot wait: 0.20 วินาที
Compound max workers: 2
Complex Query Planner cap: 4 วินาที
Query Planner num_predict: 128
Intent num_predict: 50
Ollama think: false
```

หมายเหตุ: timeout ของ Python/network ยังไม่ใช่ hard cancellation ของงานที่ Ollama เริ่มประมวลผลไปแล้วทั้งหมด

---

## 8. ข้อมูลที่ยืนยันในระบบปัจจุบัน

### Game catalog

Canonical current catalog จาก `service_game_availability.jsonl`:

```text
42 unique games
PC Zone: 6
PlayStation 5 Zone: 17
Nintendo Switch Zone: 17
VR Zone: 4
Cockpit Zone: 1
```

ผลรวมตาม zone เป็น 45 เพราะบางเกมอยู่มากกว่าหนึ่ง zone

เลขเก่า 44/36 เกมใน report เก่าหรือ synthetic validator fixture ไม่ใช่ canonical current catalog

### Service/machine availability

- PC #01-#02 มี TEKKEN 8 แต่ไม่มี Call of Duty: Warzone
- PC #03-#10 มี Call of Duty: Warzone แต่ไม่มี TEKKEN 8
- เกม PC อื่นเหมือนกันตาม current availability
- PS5 #01-#02 ใช้รายการเกมเดียวกัน
- Nintendo Switch แยกบริการ 1-2 players และ 1-4 players แต่รายการเกมปัจจุบันเหมือนกัน
- Cockpit มี 2 เครื่องและใช้ Gran Turismo 7
- VR มีบริการ 30 นาทีและ 1 ชั่วโมง โดยรายการเกมเหมือนกัน

### ราคา PC ที่ผู้ใช้ยืนยัน

```text
PSU Student and Staff: 0 บาท/1 ชั่วโมง
PSU Alumni and General Student: 25 บาท/1 ชั่วโมง
General Adult: 70 บาท/1 ชั่วโมง
```

### ราคา service อื่นจาก Service Fee 2026

```text
PS5 1 ชั่วโมง: 0 / 50 / 150 บาท
Nintendo Switch 1-2 คน 1 ชั่วโมง: 0 / 50 / 140 บาท
Nintendo Switch 3-4 คน 1 ชั่วโมง: 0 / 100 / 280 บาท
Cockpit 1 ชั่วโมง: 0 / 65 / 200 บาท
VR 30 นาที: 0 / 190 / 525 บาท
VR 1 ชั่วโมง: 0 / 375 / 1050 บาท
```

ลำดับราคาในแต่ละบรรทัดคือ PSU Student and Staff / PSU Alumni and General Student / General Adult

### Game controls

- มีข้อมูลปุ่มสำหรับเกมใน current catalog
- ปุ่มมี source URL และ platform แยกไว้ใน control JSON/JSONL
- บางเกมใช้ secondary source และมีสถานะ `secondary_needs_manual_verify`
- เกม VR บางเกมมีเพียง partial official control information
- ถ้าไม่มี version/platform-matched controls ห้ามดึงปุ่มเกมหรือภาคอื่นมาตอบแทน

### Schedule

- โดยหลักเปิดวันจันทร์-ศุกร์
- เช้าวันจันทร์และบ่ายวันศุกร์ปิดตามข้อมูลปัจจุบัน
- วันหยุดสำคัญหรือการเปิดเพิ่มเติมต้องยึด API/ข้อมูลล่าสุด ห้ามเดา

### Booking

ตอนนี้ chatbot อธิบายขั้นตอนจองและ policy แต่ยังไม่ได้ทำ transaction จองจริงแบบ end-to-end

---

## 9. สิ่งสำคัญที่ทำแล้วช่วง 03-05/08/2026

### 03/08/2026

- เพิ่ม Question Frame, capability candidate scoring, margin และ tool preconditions
- เพิ่ม Answer Contract, bounded repair และ final hard veto
- แก้ exact game title/family/version collisions
- เพิ่ม Global Request Deadline
- ปรับ performance ของ entity/equipment resolution
- Regenerate case bank ประมาณ 1,600 cases
- Core PSU No-LLM 1,325/1,325 ผ่านในชุดที่กำหนด
- สร้างเอกสาร flow และ PNG ล่าสุด

### 04/08/2026

- เปลี่ยน default model เป็น Typhoon 2.5 Qwen3 4B
- เพิ่ม per-request LLM call budget
- เพิ่ม Query Planner, Shadow Critic และ Failure Analyst
- เพิ่ม Boundary/Abstention Guard
- แก้ greeting/identity/capability fast path
- แก้ `ใครทำแชทบอท` ให้ role lookup ชนะ member list
- ตรวจและยืนยัน current catalog 42 unique games
- Benchmark stratified 1,000 cases และวิเคราะห์ latency/circuit breaker

### 05/08/2026

- ศึกษา Adaptive-RAG, LLMCompiler, EfficientRAG, Question Decomposition, FrugalGPT และ LLMLingua-2
- เพิ่ม Compound Complexity Gate และ DAG/dependency primitives
- เพิ่ม bounded parallel สำหรับ structured/fast children
- ลด complex compound จากประมาณ 18.3 วินาทีเหลือประมาณ 4.7 วินาทีในตัวอย่างที่ทดสอบ
- เพิ่ม Planner robustness ต่อ think block/fence/array/field variants
- เพิ่ม reference resolver สำหรับ `เกมนั้น`, `เครื่องนั้น`, `อันเดิม`
- เพิ่ม Local LLM concurrency guard
- ตรวจ canonical catalog อีกครั้งว่าเป็น 42 unique games

---

## 10. ผลทดสอบและ report สำคัญ

### Core PSU verification วันที่ 03/08

```text
Report: reports\model_benchmark\20260803_213849\REPORT.md
Core PSU No-LLM: 1,325/1,325
Average: 0.5443s
P95: 1.0222s
Max: 8.2799s
Real Usage Golden: 24/24
```

คะแนนนี้หมายถึง test bank ที่กำหนด ไม่ได้แปลว่าคำถามใหม่ใน production ถูก 100%

### Stratified 1,000 benchmark วันที่ 04/08

```text
Report: reports\model_benchmark\20260804_typhoon_stratified1000_v3_warmup\REPORT.md
No-LLM: 859/1,000 = 85.9%, average 0.4587s, P95 0.8575s
Typhoon v3: 842/1,000 = 84.2%, average 1.0705s, P95 3.1813s, max 30.3664s
Typhoon LLM calls: 228
```

ผลสองชุดไม่ควรเทียบตรง ๆ เป็น regression เพราะใช้ scope/judge/sample ต่างกัน และผล Typhoon บางส่วนถูกกระทบจาก timeout/circuit-breaker propagation

### Latest smoke coverage

```text
tests\smoke_test_compound_execution.py
tests\smoke_test_query_planner.py
tests\smoke_test_llm_concurrency.py
tests\smoke_test_llm_health_circuit_breaker.py
tests\smoke_test_game_catalog.py
tests\smoke_test_game_controls.py
tests\smoke_test_structured_tools.py
tests\smoke_test_answer_validator.py
tests\smoke_test_boundary_guard.py
tests\smoke_test_pipeline_timing.py
tests\smoke_test_session_context.py
tests\smoke_test_shadow_critic.py
```

---

## 11. ปัญหาและข้อจำกัด ณ ตอนนี้

เรียงตามความสำคัญ:

1. ยังไม่ได้รัน full evaluation 1,500+/1,600 cases หลังการแก้วันที่ 05/08
2. Concurrency guard ปัจจุบันเป็น in-process semaphore ไม่ใช่ distributed queue สำหรับหลาย process/หลายเครื่อง
3. ยังต้องทำ multi-user load test และ session isolation test แบบพร้อมกันจริง
4. Python/network timeout ยังไม่สามารถ hard-cancel งาน Ollama ที่เริ่มทำไปแล้วทุกกรณี
5. Query Planner ยังอาจ timeout หรือคืน JSON ที่ไม่ผ่าน schema แต่มี safe fallback แล้ว
6. Compound reference resolver จะถามกลับเมื่อ evidence ไม่ชัด ยังไม่ได้เดาความหมายจากภาษาทุกแบบ
7. Game controls บางเกมยังต้อง manual verify จากเครื่องจริงหรือ official source
8. Vector backend ยังไม่ใช่ semantic embedding เต็มรูปแบบ
9. Facts Composer ยังไม่ควรเปิดทุกเคส ต้องใช้เฉพาะ verified multi-source facts
10. Restart local chat จะไม่ใช้ live memory จาก process เดิมอัตโนมัติ แม้มี log เก็บไว้
11. Chatbot ยังบอกวิธีจอง ไม่ได้ทำรายการจองจริง
12. ข่าว/กิจกรรมล่าสุดยังรอเพิ่มภายหลัง

---

## 12. ลำดับงานที่แนะนำต่อ

1. รัน full 1,600-case evaluation หลัง latest changes ทั้ง No-LLM และ Typhoon
2. วิเคราะห์ failure แยก route, target, missing subanswer, source mismatch, timeout และ unnecessary LLM
3. ทำ multi-user load test 5 users พร้อมกัน พร้อมวัด queue wait/P50/P95/P99
4. ถ้าจะใช้งานหลาย process ให้ย้าย concurrency จาก in-process semaphore เป็น shared queue/worker service
5. ตรวจ game control sources ที่เป็น manual verify โดยไม่เพิ่มปุ่มจากการเดา
6. เพิ่ม real-user adversarial/compound/follow-up cases จาก log ใหม่
7. ค่อยพัฒนา semantic embedding/retrieval เมื่อ correctness ของ structured paths ยังนิ่ง
8. ตัดสินใจ scope ของ booking integration ว่าจะเป็น guidance หรือ transaction จริง

---

## 13. วิธี debug เมื่อผู้ใช้รายงานว่าตอบผิด

อย่าแก้จากข้อความคำตอบอย่างเดียว ให้ตรวจตามลำดับ:

1. Original question และ resolved session question
2. Preprocess/normalized query/query variants
3. Entity/game target resolution และ margin
4. Compound split/profile/planner/dependency
5. Route category/intent/confidence
6. Universal Intent method และ LLM attempted หรือไม่
7. Candidate list, candidate score, margin และ policy veto
8. Tool precondition และ final execution step
9. Mode ของคำตอบจริง
10. Hits/source IDs/source URLs
11. Validator/Answer Contract errors และ bounded repair
12. LLM call count, timeout, queue/concurrency และ circuit breaker

หากเป็นคำถาม PSU facts ต้องยึด evidence และ source contract ไม่ใช้ General LLM เติมข้อมูลที่ไม่มี

---

## 14. คำสั่งที่ใช้บ่อย

รัน local chat:

```powershell
.\start_local_ai_chat.ps1
```

รันแบบไม่ใช้ LLM:

```powershell
.\start_local_ai_chat.ps1 -NoLlm
```

รันคำถามเดียวพร้อม debug:

```powershell
.\start_local_ai_chat.ps1 -Debug -Once "PC ราคาเท่าไหร่ แล้วจองยังไง"
```

Smoke tests สำคัญ:

```powershell
python tests\smoke_test_compound_execution.py
python tests\smoke_test_query_planner.py
python tests\smoke_test_llm_concurrency.py
python tests\smoke_test_game_catalog.py
python tests\smoke_test_game_controls.py
python tests\smoke_test_structured_tools.py
python tests\smoke_test_answer_validator.py
python tests\smoke_test_boundary_guard.py
```

---

## 15. สิ่งที่ session ใหม่ควรทำเป็นอันดับแรก

1. อ่านไฟล์นี้ทั้งหมด
2. อ่าน daily logs วันที่ 03, 04, 05 และ 06/08/2026
3. อ่าน flow detail วันที่ 03/08 หากต้องแก้ architecture
4. ตรวจ source code จริงก่อนเชื่อเอกสาร หากเอกสารกับโค้ดไม่ตรงให้ยึดโค้ดและ daily log ล่าสุด
5. สรุปให้ผู้ใช้ก่อนว่าเข้าใจ current flow, model, data status, tests และ blockers อย่างไร
6. ก่อนแก้คำตอบผิด ให้ reproduce พร้อมดู mode/route/source/trace
7. เมื่อทำงานที่มีสาระ ให้เพิ่ม daily log ของวันนั้นไว้ด้านบน

---

## 16. สรุปสั้นที่สุด

ระบบปัจจุบันเป็น local-first hybrid chatbot ที่ใช้ structured/fast path เป็นแกนหลัก ใช้ RAG/vector/rerank เฉพาะเมื่อเหมาะ และใช้ Local LLM แบบ gated สำหรับ planner, intent, composer, fallback และ offline critic

ระบบมี safety/correctness layers ได้แก่ boundary guard, ambiguity gate, candidate scoring, margin, tool preconditions, answer contract, bounded repair และ final hard veto

สถานะข้อมูลเกมปัจจุบันคือ 42 unique games พร้อมปุ่มและแหล่งอ้างอิง แต่บาง control source ยังต้อง manual verify

ปัญหาหลักต่อไปคือ full evaluation หลัง latest changes, multi-user/distributed queue, hard cancellation, manual control verification และ production observability

