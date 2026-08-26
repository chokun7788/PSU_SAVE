# วิเคราะห์ Full Benchmark 1,600 เคส: Correctness, Route, Output และเวลา

วันที่วิเคราะห์: 2026-08-23  
ชุดผล: `reports/model_benchmark/20260823_full_latest_1600_product`

## สรุปตรง ๆ ก่อน

- Typhoon ผ่าน heuristic judge `1,546/1,600` หรือ `96.62%` ดีกว่า No-LLM ที่ `1,378/1,600` หรือ `86.12%`
- ตัวเลข `96.62%` ยังไม่ใช่ความแม่นจริงสำหรับปล่อย Product เพราะ evaluator พบทั้ง false negative และ false positive
- มี `44/1,600` เคส หรือ `2.75%` ที่ใช้เวลาเกิน 10 วินาที จึงยังไม่ผ่านเงื่อนไขผู้ใช้ที่ต้องเห็นคำตอบภายใน 10 วินาทีทุกครั้ง
- 54 เคสที่ judge ตัดว่าไม่ผ่าน แบ่งเป็น 40 confirmed failures, 13 keyword-judge false negatives และ 1 เคสที่ต้องตัดสิน product scope
- ปัญหา correctness ส่วนใหญ่ไม่ได้เกิดจาก RAG หาเอกสารไม่เจอ แต่เกิดก่อน execution ได้แก่ raw substring matching, route/intent conflict, Question Frame ตีขอบเขตกว้างเกินไป และ LLM Intent เขียนทับ route ที่ถูก
- ปัญหาเวลาส่วนใหญ่เกิดใน general LLM โดยเฉพาะการเรียก Intent LLM แล้วเรียก General LLM ซ้ำ รวมถึง route ผิดหนึ่งเคสที่พาไปสแกน fuzzy game aliases ซ้ำหลายรอบ
- Query Planner ใช้งานจริงเพียง 1 ครั้งแล้วได้ JSON ไม่ผ่าน schema จากนั้นอีก 16 เคสถูก circuit breaker ข้าม จึงยังไม่ถือว่า planner path ทำงานได้ตามเป้าหมาย
- รอบนี้ยังไม่แก้ source code, data หรือ expected result รายงานนี้เป็น diagnosis เพื่อกำหนดลำดับแก้ root cause

## เงื่อนไขของรอบทดสอบ

| รายการ | ค่า |
|---|---:|
| จำนวนเคส | 1,600 ต่อโหมด |
| โหมด | No-LLM และ `scb10x/typhoon2.5-qwen3-4b` |
| Global timeout ที่ใช้ตอน benchmark | 20 วินาที |
| General LLM `num_predict` | 256 |
| Query Planner `num_predict` | 128 |
| LLM max calls ต่อ request | 2 |
| Typhoon warmup | 75.9465 วินาที นอก request time |
| ลักษณะการรัน | Sequential ไม่ใช่ concurrent load test |

ข้อสำคัญ: รอบนี้ยังไม่ใช่ product latency profile 10 วินาที เพราะใช้ global timeout 20 วินาทีและ output budget 256 tokens ดังนั้นใช้รอบนี้หา root cause ได้ แต่ยังใช้ยืนยัน SLA 10 วินาทีไม่ได้

## ผลรวม

| Metric | No-LLM | Typhoon 4B |
|---|---:|---:|
| ผ่าน | 1,378 | 1,546 |
| Pass rate | 86.12% | 96.62% |
| Average | 0.4719s | 1.3425s |
| Median | 0.3800s | 0.5743s |
| P95 | 0.8623s | 4.1369s |
| Max | 7.8775s | 18.2820s |
| มากกว่า 10 วินาที | 0 | 44 |

Latency distribution ของ Typhoon:

| ช่วงเวลา | จำนวน | สัดส่วน |
|---|---:|---:|
| ไม่เกิน 1s | 1,021 | 63.81% |
| มากกว่า 1-3s | 443 | 27.69% |
| มากกว่า 3-5s | 81 | 5.06% |
| มากกว่า 5-9s | 11 | 0.69% |
| มากกว่า 9-10s | 0 | 0.00% |
| มากกว่า 10-15s | 39 | 2.44% |
| มากกว่า 15s | 5 | 0.31% |

ภาพรวมจึงมีสองกลุ่มชัดเจน: เคสส่วนใหญ่จบเร็วไม่เกิน 3 วินาที แต่เมื่อเข้ากลุ่ม LLM ช้าจะกระโดดไปช่วง 13-15 วินาที ไม่ได้ค่อย ๆ เพิ่มผ่านช่วง 9-10 วินาที

## สัดส่วนวิธีที่ใช้จริง

นับจาก final top-level mode ของแต่ละเคส โดย compound ซ่อนวิธีของ child tasks ไว้ภายใน:

| Method family | จำนวน | สัดส่วน | Judge pass | Avg | P95 | Max |
|---|---:|---:|---:|---:|---:|---:|
| Structured | 898 | 56.12% | 97.10% | 0.764s | 1.734s | 6.079s |
| Fast/Rule | 243 | 15.19% | 100.00% | 0.402s | 0.773s | 1.973s |
| General LLM | 242 | 15.12% | 93.80% | 4.864s | 14.498s | 18.282s |
| Compound | 88 | 5.50% | 100.00% | 1.185s | 3.774s | 5.596s |
| Retrieval/Fact Card | 75 | 4.69% | 100.00% | 0.613s | 1.340s | 4.190s |
| Clarification | 43 | 2.69% | 76.74% | 0.377s | 1.059s | 1.600s |
| Other fallback | 6 | 0.38% | 100.00% | 0.255s | 0.542s | 0.646s |
| No-answer | 3 | 0.19% | 66.67% | 5.740s | 10.363s | 10.802s |
| Exception | 2 | 0.12% | 0.00% | 0.803s | 1.307s | 1.363s |

ข้อสรุปจากตาราง:

- Structured และ Fast/Rule เป็นแกนหลักรวม `71.31%` และเร็วกว่า LLM ชัดเจน
- Retrieval/Fact Card ถูกใช้ `4.69%` และรอบนี้ผ่าน judge ทั้งหมด ไม่ใช่คอขวดหลัก
- General LLM มีเพียง `15.12%` ของเคส แต่ถือครองเคสช้าเกือบทั้งหมด
- Structured ที่ไม่ผ่าน 26 เคสไม่ได้เกิดจากข้อมูล structured ผิด แต่คำถามความรู้ทั่วไปเรื่อง mechanical keyboard ถูกส่งเข้า structured equipment ผิดขอบเขต

## เวลาแยกตาม Process

ตารางนี้ aggregate จาก timing trace ที่ยังถูกเก็บไว้:

| Process | Trace ที่พบ | Avg | P95 | Max | ความหมาย |
|---|---:|---:|---:|---:|---|
| Experimental/General LLM fallback | 242 | 3.353s | 7.517s | 12.831s | เวลาของ General LLM ที่เห็นใน compact trace |
| Hybrid vector retrieval | 2 | 1.393s | 2.479s | 2.599s | ค้น lexical/vector ร่วมกันใน fallback บางเคส |
| Vector retrieval | 1 | 2.339s | 2.339s | 2.339s | vector path ที่เห็นใน trace |
| Compound children total | 88 | 1.115s | 1.777s | 5.566s | เวลารวม child tasks ของ multi-question |
| Universal Intent | 43 | 0.253s | 1.000s | 1.512s | ค่านี้ต่ำกว่าจริง เพราะ trace ต้น request ถูกตัดออกหลายเคส |
| Query Planner | 17 | 0.203s | 0.688s | 3.442s | 1 actual call และ 16 health skips |
| Structured tool execution | 1,224 | 0.103s | 0.348s | 4.323s | ดึง/คำนวณข้อมูล structured |
| Ambiguity Gate | 389 | 0.136s | 0.274s | 0.619s | ตรวจ target/operation ที่ยังไม่ชัด |
| Candidate decisions | 1,436 | 0.074s | 0.136s | 0.213s | ให้คะแนนและเลือก execution capability |
| Validation | 1,147 | 0.063s | 0.112s | 0.153s | ตรวจ answer contract/source/style |
| Question Frame | 575 | 0.065s | 0.096s | 0.166s | สรุป operation/domain/target ของคำถาม |
| Competition fact retrieval | 74 | 0.013s | 0.044s | 0.276s | ดึง fact card กฎการแข่งขัน |

ข้อจำกัดสำคัญของตาราง:

- `tools/run_model_benchmark_eval.py::_trace_compact()` เก็บเพียง `trace[-12:]`
- process ที่เกิดช่วงต้น request เช่น router, Intent LLM และ planner อาจหายจากผล final
- จำนวนและเวลาราย process จึงเป็น partial aggregate และห้ามนำมาบวกรวมเป็น total request time
- ไฟล์ `PROCESS_TIMING_COMPACT.csv` เก็บค่าทั้งหมดที่ยังมองเห็นได้พร้อม caveat นี้

## จำนวน LLM Call ที่แท้จริง

Summary แสดง `278` calls แต่ความหมายต้องแยกดังนี้:

- 278 คือ logical call records ที่ compact trace ยังมองเห็น
- 24 records มี elapsed เป็น 0 เพราะถูก health manager/circuit breaker ข้าม ไม่ได้ยิง request ไป Ollama
- actual executions ที่มองเห็นใน compact trace เท่ากับ 254
- focused full-trace reproduction ประกอบกับ overhead signature ของ 41 slow cases ชี้ว่ามี early Intent LLM ที่ถูกตัดออกจากผล final อย่างน้อย 41 calls
- จากหลักฐานชุดนี้ actual executions ของรอบเต็มจึงมี lower bound `254 + 41 = 295` ครั้ง แต่หาค่าจริงแบบ exact ย้อนหลังไม่ได้จาก artifact นี้
- logical call entries มีอย่างน้อย 319 entries เมื่อรวม 41 early calls ที่หายไป

ต้องแก้ benchmark instrumentation ให้เก็บ call ledger แยกจาก compact presentation trace เพื่อให้วัด LLM calls, queue wait และ stage time ได้ตรงในรอบถัดไป

## วิเคราะห์ 54 เคสที่ Judge ไม่ผ่าน

| Root-cause cluster | จำนวน | สถานะ |
|---|---:|---|
| คำถาม mechanical keyboard ถูกส่งไป PSU equipment | 26 | Confirmed failure |
| `ข้อดีข้อเสีย` ถูกคำว่า `เสีย` กระตุ้น price intent | 9 | Confirmed failure |
| คำตอบขอบคุณใช้ `ขอขอบพระคุณ/ขอบใจ` แต่ judge หา exact `ขอบคุณ` | 8 | Judge false negative |
| คำตอบ latency ใช้ `ความล่าช้า/เวลาตอบสนอง` แต่ judge หา `latency/หน่วง` | 5 | Judge false negative |
| `rag_llm_attempted` ไม่ถูก initialize ใน single-question path | 2 | Confirmed exception |
| Animal Crossing ถูก `cross` กระตุ้น control route และ clarification | 1 | Confirmed failure |
| คำถามโซนที่มีเกมมากสุดถูก LLM เปลี่ยนเป็น equipment | 1 | Confirmed failure |
| เพลงฮิตตอนนี้ตอบชื่อเพลงโดยไม่มี live evidence | 1 | Confirmed unsupported claim |
| ขอช่วยการบ้านคณิต แต่ model ปฏิเสธเพราะ PSU-only | 1 | ต้องตัดสิน product scope |

ถ้านับเฉพาะ 13 keyword-judge false negatives เป็น semantic pass แบบจำกัด จะได้อย่างน้อย `1,559/1,600 = 97.44%` แต่ตัวเลขนี้ยังไม่ใช่ semantic release score เพราะยังพบคำตอบที่ judge ให้ผ่านทั้งที่ซ้ำ ตัดกลางประโยค ผิดรูปแบบ หรือขาด subanswer

## Root Cause เชิงระบบ

### 1. Raw substring matching ทำให้คำหนึ่งชนกับอีกคำ

หลายโมดูล normalize แล้วใช้ `term in text` โดยตรง เช่น:

- `app/pipeline/ambiguity_gate.py:101-103`
- `app/pipeline/tool_preconditions.py:25-27`
- `app/runtime/fast_answer.py:1047-1048`

ผลที่พบจริง:

- `ข้อเสีย` มี substring `เสีย` จึงถูกตีเป็นการถามราคา 9 เคส
- `Animal Crossing` มีคำว่า `cross` จึงถูก policy บังคับไป game controls
- `กากบาท` มี substring `บาท` ทำให้ validator บางครั้งเข้าใจว่าคำตอบปุ่มเกมเป็นคำตอบราคา และแจ้งเตือน source ผิดประเภท

แนวแก้ที่ต้นเหตุ:

- สร้าง lexical matcher กลางที่รองรับ English token boundary, exact phrase, Thai context และ negative phrase
- ห้ามแก้เป็น exception กระจายรายคำ เพราะจะเพิ่ม collision ใหม่เมื่อข้อมูลโต
- เพิ่ม regression matrix สำหรับ `ข้อเสีย/เสีย`, `กากบาท/บาท`, `Crossing/cross` และคำชนอื่นที่เกี่ยวกับราคา/ปุ่ม/ชื่อเกม

### 2. General concept ถูกตีว่าเป็นข้อมูลอุปกรณ์ของ PSU

คำถาม 26 รูปแบบของ `คีย์บอร์ด mechanical คืออะไร` เริ่มจาก router และ Intent เป็น `general/detail` ถูกแล้ว แต่ `Question Frame` เรียก `looks_like_equipment_query()` และเห็นคำว่า `คีย์บอร์ด` จึงเปลี่ยนเป็น `equipment/equipment_lookup` confidence 0.92

จุดที่เกี่ยวข้อง:

- `app/pipeline/question_frame.py:150-151` ตรวจ equipment ก่อนใช้ intent operation
- `app/pipeline/tool_preconditions.py:209` เป็นต้นไป ถือคำว่า `คีย์บอร์ด` เพียงคำเดียวว่าเป็น equipment query
- `app/pipeline/engine.py:1435-1454` ยอม operation-first refine เมื่อ route เดิมเป็น general

แนวแก้:

- แยก `general equipment concept` ออกจาก `PSU inventory lookup`
- structured equipment ต้องมี PSU/studio/zone/inventory context หรือ inventory operation เช่น `ศูนย์มีไหม`, `มีกี่ตัว`, `รุ่นอะไร`, `อยู่โซนไหน`
- definition/comparison เช่น `คืออะไร`, `ต่างกันยังไง`, `ข้อดีข้อเสีย` ต้องคง general route เมื่อไม่มี PSU context

### 3. LLM Intent สามารถเขียนทับ route ที่ deterministic วิเคราะห์ถูก

เคส `อุปกรณ์ไหนเกมเยอะสุด`:

- No-LLM เลือก `structured_game_zone_ranking` ถูกและตอบภายใน 0.3211 วินาที
- LLM Intent เปลี่ยนเป็น `equipment/list`
- Question Frame ยังตรวจพบ `games/game_zone_rank` confidence สูง แต่ engine refine เฉพาะเมื่อ route เป็น `general/unknown/no_answer`
- เพราะ route กลายเป็น equipment แล้ว Question Frame จึงซ่อม route กลับไม่ได้
- structured equipment ถูก Answer Contract ปฏิเสธ จากนั้นเข้าสู่ fallback ที่แพงและสุดท้าย no-answer

แนวแก้:

- ให้ high-confidence operation-first frame override route ที่ขัด domain อย่างชัดเจน ไม่จำกัดเฉพาะ general/unknown
- deterministic exact operation/target ต้องมีสิทธิ์ veto LLM review ที่อ่อนกว่า
- LLM Intent ควรทำหน้าที่ reviewer เมื่อ rule confidence ต่ำ ไม่ใช่ replace route ที่มี exact operation evidence

### 4. Fuzzy game matching ถูกเรียกซ้ำโดยไม่จำเป็น

Focused microprofile ของเคส ranking ที่ route ผิดพบว่า `answer_equipment()` เรียก flow ที่วน `_match_supported_game()` ซ้ำ:

- รอบหนึ่ง: service game availability 7.193s, game match เพิ่ม 3.795s และ 3.338s, รวม 14.327s
- อีกรอบ: 6.616s + 3.389s + 3.212s, รวม 13.217s

จุดที่เกี่ยวข้อง:

- `app/runtime/fast_answer.py:2313` `_match_supported_game()` วน game catalog และ aliases
- `app/runtime/fast_answer.py:4325-4328` `answer_equipment()` เรียก service availability ก่อน

นี่เป็น pure-Python fuzzy alias scan ไม่ใช่ BGE inference

แนวแก้:

- ตรวจ named-game likelihood ก่อนทำ fuzzy scan
- resolve game match ครั้งเดียวต่อ normalized query แล้ว cache ใน request context
- ส่ง resolved match เข้า handlers แทนให้แต่ละ handlerค้นใหม่
- route game-zone ranking ให้ถูกก่อน จึงไม่ควรเข้า equipment fallback ตั้งแต่แรก

### 5. General prompt ถูกเรียก LLM สองรอบ

คำถามแปลคำและเขียนประโยคประชาสัมพันธ์มี heuristic operation เป็น unknown จึงเรียก Universal Intent LLM ก่อน แล้วจึงเรียก General LLM อีกครั้ง แม้ intent call ไม่ได้เพิ่มคุณค่าให้คำถามที่ชัดอยู่แล้ว

Focused full-trace examples:

- แปล `reservation`: wall 9.137s = Intent LLM 0.831s + General LLM 6.281s + pipeline overhead
- เขียนประโยคประชาสัมพันธ์: wall 14.875s = Intent LLM 6.741s + General LLM 7.775s
- อธิบาย latency: wall 10.082s โดย General LLM ใช้ 9.753s

แนวแก้:

- ถ้า router เป็น general และพบ operation ชัด เช่น translation, definition, rewrite หรือ text generation ให้เข้า General LLM ครั้งเดียว
- จำกัด clear-general request เป็น max 1 LLM call
- กำหนด output token budget ตามรูปแบบที่ผู้ใช้ขอ เช่น one sentence/short definition ใช้ 64-96 tokens
- reserve เวลา finalization และคืน bounded fallback ก่อน user-visible cap

### 6. Query Planner ยังไม่ทำงานจริงตามเป้า

จาก 95 planner trace entries:

- 78 เคส deterministic splitter แยกได้ จึงข้าม planner ตาม design
- 1 เคสเรียก planner จริง ใช้ 3.4416s แต่ output ไม่ผ่าน allowlist/schema (`InvalidPlannerJSON`)
- 16 เคสถัดมาถูก health manager ข้ามเพราะ circuit breaker cooldown

แปลว่า planner ไม่ได้เป็นคอขวดใหญ่ของรอบนี้ แต่ functionality ของ complex compound ยังพึ่ง deterministic fallback เกือบทั้งหมด

แนวแก้:

- ทำ parser/JSON repair แบบ bounded สำหรับ schema ที่ใกล้เคียง
- ลด prompt/schema ให้ง่ายสำหรับ 4B model
- แยก health key ของ planner และเก็บ invalid output แบบ redacted เพื่อวิเคราะห์
- ทดสอบว่าหลัง planner fail แล้ว deterministic plan ยังตอบครบทุก subanswer ไม่ใช่แค่ judge ผ่าน

### 7. Per-request state ไม่ครบ ทำให้เกิด exception

เคส:

- `MB-0607-CR-071`: `ROV ถ้าใช้ bug จะโดนอะไร`
- `MB-0636-ANA-010`: `จอง`

เกิด `UnboundLocalError: rag_llm_attempted`

จุดที่เกี่ยวข้อง:

- `_answer_multi()` initialize `rag_llm_attempted` ที่ `app/pipeline/engine.py:721`
- `_answer_single()` เริ่มที่ `app/pipeline/engine.py:1008` แต่ไม่ได้ initialize ตัวแปรเดียวกัน
- single path ใช้ตัวแปรที่ `app/pipeline/engine.py:2273`

แนวแก้:

- initialize request-local RAG state ทุก execution path จาก object/default เดียวกัน
- เพิ่ม direct unit test ทั้ง single, compound, no-context และ ambiguity fallback

### 8. Freshness query ไม่มี source requirement

`เพลงฮิตตอนนี้คืออะไร` ตอบ `Flowers` เป็นตัวอย่างเพลงปัจจุบันโดยไม่มี Web/API evidence ถือเป็น unsupported freshness claim แม้มีข้อความเตือนว่าข้อมูลเปลี่ยนได้

แนวแก้:

- detect `ตอนนี้/ล่าสุด/วันนี้/ข่าว/เพลงฮิต` เป็น freshness requirement
- ถ้ามี live Web/API ให้ตอบจาก source พร้อม timestamp
- ถ้าไม่มี live source ให้บอกตรง ๆ ว่าไม่มีข้อมูลปัจจุบัน ห้ามใช้ model memory เดาชื่อ

### 9. Product scope ของ General Assistant ยังไม่ลงตัว

`ช่วยทำการบ้านคณิตให้หน่อย` ถูก model ปฏิเสธเพราะไม่เกี่ยวกับ PSU แต่เป้าหมายล่าสุดของ Product คือผู้ช่วยสำหรับทุกคนและอยากตอบคำถามทั่วไปด้วย

ต้องตัดสิน policy ก่อนแก้:

- PSU-only assistant: ปฏิเสธได้ แต่ข้อความต้องเป็นธรรมชาติและ test ต้องสะท้อน policy
- Broad safe assistant: ช่วยโจทย์ทั่วไปได้ แต่ต้องมี safety, latency และ resource budget แยกจาก PSU fact path

ห้ามแก้ expected result เพียงเพื่อให้ผ่านก่อนตัดสินขอบเขตจริง

## คำตอบแปลกที่ Judge ยังให้ผ่าน

ตรวจ output ของ General LLM 242 เคสพบ quality signals ต่อไปนี้:

| Signal | จำนวน |
|---|---:|
| เนื้อหาหลักยาวเกิน 300 ตัวอักษร | 42 |
| ใช้คำลงท้ายผสม เช่น `ครับ/ค่ะ` หรือทั้งครับและค่ะ | 23 |
| ขอคำตอบสั้นแต่ body เกิน 250 ตัวอักษร | 18 |
| มี emoji | 10 |
| มีวลีไทยแปลกที่ตรวจพบอัตโนมัติ | 5 |
| ซ้ำหรือตัดกลางประโยคชัดเจน | 2 |
| Compound ขาด comparison subanswer ที่ตรวจพบชัด | 1 |

ตัวอย่างสำคัญ:

- `MB-1424-GL-099` ขอ GPU สองข้อ แต่ model ย้ำประโยคเดิมหลายครั้งและถูกตัดกลางคำ ทั้งที่ judge ให้ 100
- `MB-1571-GL-246` ขอคำจำกัดความสั้น แต่ตอบยาวและจบที่คำว่า `หรือ` ก่อนหมายเหตุ ทั้งที่ judge ให้ 100
- `MB-1320-C-084` ถามความต่าง VR 30 นาที/1 ชั่วโมงและวิธีจอง แต่ splitter ทำคำถามแรกเป็น `VR 30 นาที จองยังไง` จนไม่ได้ตอบ comparison ครบ ทั้งที่ judge ให้ 100
- มี output เช่น `ครับ/ค่ะ`, `นะคะครับ/ค่ะ`, `เรียนชวน`, `ไม่ต้องรอช้า` และ emoji ซึ่งไม่เหมาะกับ voice ของ production bot

ดังนั้น keyword judge ใช้เป็น smoke test ได้ แต่ห้ามใช้เป็น release gate เพียงตัวเดียว

## Validation ที่ต้องตีความอย่างระวัง

Validation warnings ที่พบบ่อย:

| Warning | จำนวน |
|---|---:|
| `fact_answer_may_be_too_verbose` | 182 |
| `price_question_should_start_with_price_or_number` | 75 |
| `service_fee_answer_missing_service_fee_source` | 68 |
| `high_confidence_route_returned_no_answer` | 22 |
| `draft_rejected_by_answer_contract` | 5 |

ข้อสังเกต:

- warning ราคา/source บางส่วนเป็น false positive จาก `กากบาท` ชน `บาท`
- `validation_ok=false` มีเพียง 2 เคสและทั้งสองไม่ผ่าน judge แสดงว่า validator ส่วนใหญ่เตือนแต่ไม่ได้ veto
- warning ต้อง triage ใหม่หลังแก้ lexical matcher ไม่เช่นนั้น metric จะปนกันระหว่างปัญหาจริงและคำชน

## LLM ช่วยและทำให้ถอยหลังตรงไหน

เทียบ case ID เดียวกันระหว่าง No-LLM กับ Typhoon:

| Transition | จำนวน |
|---|---:|
| ทั้งคู่ผ่าน | 1,372 |
| No-LLM ไม่ผ่าน แต่ LLM ผ่าน | 174 |
| ทั้งคู่ไม่ผ่าน | 48 |
| No-LLM ผ่าน แต่ LLM ไม่ผ่าน | 6 |

6 regression เมื่อเปิด LLM:

1. Animal Crossing: route/ambiguity ผิด
2. Game-zone ranking: LLM เปลี่ยน route ถูกเป็น equipment
3. ROV bug: exception ใน RAG fallback state
4. `จอง`: exception ใน RAG fallback state
5. เพลงฮิตตอนนี้: model ตอบ claim ที่ไม่สดและไม่มี source
6. การบ้านคณิต: policy ของ model ไม่ตรง product goal ที่ยังไม่ตัดสิน

หมายเหตุ: baseline `ROV bug` ที่ judge ให้ผ่านจริง ๆ ตอบเรื่องเริ่มแข่งขันช้า จึงเป็น evaluator false positive อีกตัวอย่างหนึ่ง

## ทำไมเรื่องเวลายังเป็นปัญหา

1. รอบ benchmark เปิด deadline 20 วินาที จึงยอมให้ request อยู่เกิน product cap 10 วินาที
2. clear-general prompts บางชนิดใช้ LLM สอง call โดย call แรกเป็น intent review ที่ไม่จำเป็น
3. `num_predict=256` สูงเกินความต้องการของคำตอบหนึ่งประโยคหรือคำแปลหนึ่งคำ
4. Ollama/local generation time ผันผวน แม้ prompt คล้ายกัน บาง call ใช้ประมาณ 1 วินาทีแต่บาง call 6-12 วินาที
5. route ผิดทำให้ fallback chain ทำงานหลายชั้น และบาง handler มี repeated fuzzy scans หลายวินาที
6. compact trace ซ่อน early stages ทำให้ summary ต่ำกว่าค่า LLM workload จริง
7. ยังไม่ได้ทดสอบ queue wait จากหลายผู้ใช้; sequential P95 4.14 วินาทีไม่ได้รับประกัน P95 เมื่อมี 5-20 sessions
8. LLM concurrency เป็น 1 ดังนั้นเมื่อ 20 คนเข้าพร้อมกัน queue time อาจมากกว่า generation time หลายเท่า แม้แต่ละ call เดี่ยวไม่เกิน 10 วินาที

## ลำดับแก้ที่แนะนำ

### P0: แก้ correctness crash และ lexical collision

1. Initialize `rag_llm_attempted`/RAG request state ใน `_answer_single()` จาก shared request-state object
2. สร้าง boundary/context-aware matcher กลาง แล้วแทน raw substring ใน price, controls, ambiguity, preconditions และ validator
3. เพิ่ม regression tests สำหรับ 2 exceptions, 9 `ข้อดีข้อเสีย`, Animal Crossing และ `กากบาท`

### P1: ปิด wrong-route cluster

1. แยก general equipment concept ออกจาก PSU inventory query
2. ให้ exact/high-confidence Question Frame ซ่อม incompatible route ที่ LLM เขียนทับ
3. ให้ deterministic evidence veto LLM Intent เมื่อ operation/target ชัด
4. เพิ่ม regression tests ครบ 26 mechanical keyboard variants และ game-zone ranking

### P1: ทำ product latency path

1. clear-general translation/definition/rewrite/generation ใช้ LLM สูงสุด 1 call
2. ใช้ backend work budget ประมาณ 8.5-9 วินาที และ user-visible cap 10 วินาที
3. กำหนด token budget ตาม requested shape เช่น 64/96/128 แทน 256 ทุกเคส
4. มี deterministic bounded fallback เมื่อ LLM เหลือเวลาไม่พอ
5. เก็บ queue wait, model load, prompt eval, generation และ finalization แยกกัน

### P2: ลด fallback cost และทำ planner ให้เชื่อถือได้

1. cache game match ต่อ request และห้าม fuzzy scan เมื่อไม่มี named-game signal
2. ทำ Query Planner schema ให้ง่ายขึ้น พร้อม bounded JSON repair
3. แยก planner failure/cooldown metrics จาก general LLM health
4. ตรวจ compound answers ตาม subquestion coverage ไม่ใช่ keyword รวมทั้งคำตอบ

### P2: ทำ Answer Contract สำหรับภาษา

1. จำกัดจำนวนประโยค/ข้อ/บรรทัดตามที่ผู้ใช้ร้องขอ
2. เลือกคำลงท้ายไทยรูปแบบเดียว ห้าม `ครับ/ค่ะ`
3. ปิด emoji เป็นค่าเริ่มต้น
4. ตรวจ repetition, truncation และ incomplete final clause
5. ถ้า contract ไม่ผ่าน ให้ bounded repair เพียงครั้งเดียวหรือใช้ safe deterministic cleanup

### P2: ทำ Freshness Guard

1. current/latest query ต้องมี live source และ timestamp
2. ไม่มี source ให้ no-answer แบบตรงไปตรงมา
3. ห้าม General LLM เติมชื่อ ข่าว ราคา เวลา หรือสถานะปัจจุบันจาก model memory

### P3: ปรับ Evaluation และ Observability

1. เปลี่ยน exact keyword judge ให้รองรับ Thai morphology/synonym และตรวจ domain-operation-target-evidence
2. เพิ่ม semantic/human/Codex audit สำหรับ failed cases และ sample ของ passed cases
3. เก็บ full timing/call ledger แยกจาก compact trace
4. เก็บ expected subanswers สำหรับ compound เพื่อจับ missing subanswer
5. แยก correctness score, style score, source-grounding score และ latency SLA

## แผนทดสอบหลังแก้

1. รัน focused regression ของแต่ละ cluster ก่อน ไม่ต้องเริ่มด้วย 1,600 ทุกครั้ง
2. รัน full No-LLM และ Typhoon ด้วย product profile จริง: backend deadline 8.5-9s, visible cap 10s และ token budget ใหม่
3. เก็บ pass rate, semantic audit rate, average, P50, P95, P99, max, จำนวนเกิน 10s, actual LLM calls และ queue wait
4. เป้าขั้นต้นควรเป็น exception 0, confirmed wrong-route cluster 0 และ request เกิน 10s เท่ากับ 0 ใน sequential run
5. หลัง sequential ผ่าน จึงทำ concurrent load test 5 sessions แล้วขยายเป็น 20 sessions เพื่อวัด queue wait และ session isolation

## Artifacts

- `ANALYSIS_TH.md` รายงานนี้
- `CASE_DIAGNOSIS_1600.csv` diagnosis, route, mode, timing, answer และ No-LLM comparison ครบ 1,600 เคส
- `FAILURE_DIAGNOSIS_54.csv` เฉพาะ 54 เคสที่ heuristic judge ไม่ผ่าน
- `SLOW_CASES_OVER_10S.csv` เฉพาะ 44 เคสเกิน 10 วินาที
- `PROCESS_TIMING_COMPACT.csv` timing aggregate ของ process ที่ยังอยู่ใน compact trace
- `METHOD_AND_MODE_SUMMARY.csv` สัดส่วน, pass rate และ latency แยก method family/mode

## ข้อจำกัดที่ยังไม่ได้พิสูจน์

- ยังไม่ได้แก้ source code และยังไม่ได้รัน regression หลังแก้
- ยังไม่ได้รัน full benchmark ด้วย 10-second product profile
- ยังไม่ได้ทำ multi-user load test, queue saturation และ session isolation
- full exact LLM call count กู้ย้อนหลังไม่ได้เพราะ artifact เก็บเพียง 12 trace entries สุดท้าย
- 13 false negatives ผ่านการจัดกลุ่มเชิงความหมายแบบจำกัด ไม่ใช่ human review ครบทุกคำตอบ
- pass cases ยังต้องสุ่มตรวจเพิ่ม เพราะพบ evaluator false positives หลายลักษณะ

## Follow-up Per-Case Audit

มีการตรวจต่อระดับรายข้อสำหรับ 162 เคสไม่ซ้ำกัน ซึ่งเป็น union ของ 54 failures, 44 เคสเกิน 10 วินาที และ 85 output-quality signals โดยแต่ละ record ระบุ first wrong stage, causal chain, ideal route/method, source requirement, ตัวอย่างคำตอบ, fix strategy และ regression assertion

- `PER_CASE_AUDIT_LOG_162.md`: human-readable log ครบทุกข้อ
- `PER_CASE_AUDIT_LOG_162.csv`: ตารางสำหรับ filter/sort
- `PER_CASE_AUDIT_LOG_162.jsonl`: structured audit record สำหรับนำไปทำ tooling ต่อ
- `PER_CASE_AUDIT_ACTION_PLAN.md`: แปลงผลรายข้อเป็น implementation units และลำดับแก้
