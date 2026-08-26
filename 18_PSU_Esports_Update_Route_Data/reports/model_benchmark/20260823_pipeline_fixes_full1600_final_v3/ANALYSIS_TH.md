# วิเคราะห์ Full 1,600 Cases หลัง Pipeline Fixes

วันที่: 23/08/2026

## 1. ขอบเขตการรัน

- Case bank: `data/eval/model_benchmark_1500.jsonl` จำนวน 1,600 cases
- Model: `scb10x/typhoon2.5-qwen3-4b`
- Profile: Local LLM enabled, warmup enabled
- Backend deadline: 9 วินาที
- `num_predict` configured: 128 และ General ใช้ adaptive profile
- Tool Router LLM: ปิด
- Facts Composer: ปิด
- BGE document reranker: ไม่ได้เปิดในรอบนี้
- Health manager: เปิด
- ลักษณะการรัน: sequential single process

ไฟล์หลัก:

- `REPORT.md`
- `llm_scb10x_typhoon2.5-qwen3-4b/results.jsonl`
- `llm_scb10x_typhoon2.5-qwen3-4b/results.csv`
- `llm_scb10x_typhoon2.5-qwen3-4b/summary.json`

## 2. ผลรวม

| Metric | Result |
|---|---:|
| Total | 1,600 |
| Passed | 1,599 |
| Failed | 1 |
| Pass rate | 99.94% |
| Average score | 99.99 |
| Average latency | 0.7730s |
| Median | 0.4465s |
| P95 | 2.3135s |
| P99 | 2.9207s |
| Max | 6.3254s |
| >1s | 416 |
| >2s | 115 |
| >3s | 15 |
| >5s | 6 |
| >9s | 0 |

สรุปตรง ๆ: sequential product profile ผ่าน backend SLA 9 วินาทีครบทุก request แต่ยังไม่ใช่หลักฐานว่า 20 users พร้อมกันจะต่ำกว่า 10 วินาที เพราะรอบนี้ไม่มี queue contention

## 3. LLM Call Audit

| Metric | Result |
|---|---:|
| Requests with 0 calls | 1,251 |
| Requests with 1 call | 349 |
| Requests with 2+ calls | 0 |
| Total calls | 349 |

แยกตาม kind:

| Kind | Calls | Avg | P95 | Max | num_ctx | Errors |
|---|---:|---:|---:|---:|---:|---:|
| General LLM | 275 | 1,429.58ms | 2,209.21ms | 2,856.67ms | 3072 | 0 |
| Universal Intent | 74 | 862.23ms | 1,105.27ms | 1,305.62ms | 3072 | 0 |

ไม่พบ Query Planner, Tool Router LLM, Grounded Composer หรือ RAG LLM call ในรอบนี้

ผลสำคัญคือปัญหา double-call ของ General ถูกตัดออก: ไม่มี request ใดใช้ 2 calls แม้ global policy ยอมได้สูงสุด 2

## 4. Final-mode Share

| Bucket | Requests | Share |
|---|---:|---:|
| Structured | 873 | 54.56% |
| Fast/Rule/Calculator | 244 | 15.25% |
| Retrieval/RAG/Fact Card | 75 | 4.69% |
| General LLM | 275 | 17.19% |
| Compound parent | 88 | 5.50% |
| Guard/Clarification/No-answer | 45 | 2.81% |

ข้อควรระวัง:

- Compound parent รวมคำตอบจาก child paths จึงไม่ใช่ knowledge source ใหม่
- Retrieval bucket 75 รวม Competition Fact Card 60
- หากนับเฉพาะ `rag_direct_curated` 14 และ `guarded_vector_direct` 1 จะเป็น direct RAG/vector 15 requests หรือ 0.94%
- `experimental_rag_no_context` 5 requests จบ safe no-answer และอยู่ใน guard bucket

## 5. Group Results

ทุกกลุ่มผ่าน 100% ยกเว้น competition rules:

- General LLM: 275/275, avg 1.8534s, P95 2.6276s
- Compound: 89/89, avg 1.2148s, P95 2.6338s
- Equipment: 58/58, avg 1.0866s, P95 1.2043s
- Game controls: 345/345, avg 0.4175s, P95 0.6109s
- Service fee: 258/258, avg 0.3342s, P95 0.4354s
- Reservation: 20/20, avg 0.3504s, P95 0.5125s
- Competition rules: 74/75 ตาม heuristic judge

## 6. Stage Latency

| Stage | Count | Total | Avg | P95 | Max |
|---|---:|---:|---:|---:|---:|
| Experimental/General fallback | 276 | 393.72s | 1,426.51ms | 2,209.73ms | 2,866.59ms |
| Ambiguity Gate | 1,503 | 168.05s | 111.81ms | 227.16ms | 1,217.47ms |
| Structured execution | 1,242 | 143.98s | 115.93ms | 296.73ms | 6,087.18ms |
| Candidate decisions | 1,469 | 115.14s | 78.38ms | 133.51ms | 221.36ms |
| Compound children | 88 | 105.02s | 1,193.38ms | 2,619.82ms | 5,841.93ms |
| Question Frame | 1,469 | 101.11s | 68.83ms | 110.15ms | 215.54ms |
| Validation | 1,123 | 77.31s | 68.85ms | 115.79ms | 222.37ms |
| Universal Intent | 1,503 | 65.16s | 43.35ms | 3.53ms | 1,307.19ms |
| Preprocess | 1,512 | 30.28s | 20.02ms | 117.25ms | 1,375.02ms |

Universal Intent P95 ต่ำกว่า average เพราะส่วนใหญ่เป็น heuristic ที่เร็ว มีเพียง 74 LLM calls ซึ่งสร้าง long tail

## 7. Slowest Cases และ Root Cause

### 7.1 Structured service catalog

Slowest:

```text
MB-0816-AS-012
Nintendo Switch (1-4 Persons) มีเกมอะไรบ้าง
Wall 6.3254s
Structured execution 6.0872s
LLM calls 0
```

Root cause: service catalog ไม่มี specific game target แต่ code ยัง fuzzy scan game-title aliases ทุกตัวเพราะ domain เป็น games

อาการเดียวกันพบใน:

- Nintendo Switch 1-2 Persons: 5.9847s
- PlayStation 5 Zone list: 5.5404s
- VR Station 1 ชั่วโมง list: 5.1808s
- PS5 + Nintendo compound list: 5.8517s

### 7.2 Unknown named game

`มี GTA V ไหม` ใช้ 5.1437s:

- deterministic handlers 4.1763s
- structured tool 572.69ms
- hybrid retrieval 187.24ms
- hybrid vector 135.20ms

ระบบตอบ no-answer ถูก แต่ยังมี repeated fuzzy/fallback work ที่ควร optimize ต่อ

### 7.3 Rare vector retrieval

`TEKKEN 8 มาสายจะโดนอะไร` ใช้ 4.3385s โดย vector retrieval ใช้ 4.0706s เป็น rare retrieval outlier ถึงแม้สุดท้ายตอบได้ผ่าน

## 8. Failure Analysis

เคสเดียว:

```text
MB-0607-CR-071
ROV ถ้าใช้ bug จะโดนอะไร
Mode: pipeline:answer_contract_no_answer
Answer: ยังไม่พบข้อมูลที่ยืนยันได้...
Judge error: category_mismatch:no_answer
```

Root cause ไม่ใช่ wrong route หรือ timeout แต่เป็น evidence coverage:

- query อยู่ competition rules
- retrieval ไม่มี fact ที่รองรับบทลงโทษอย่างชัด
- Answer Contract ปฏิเสธ unsupported claim
- Final output จึง no-answer

ข้อสรุป: นี่เป็น heuristic/product-policy mismatch ที่ปลอดภัยกว่าการเดา ควรเพิ่ม authoritative fact source หรือทำ evaluator รับ safe no-answer เมื่อ coverage ไม่มี

## 9. Post-full Fix

หลังอ่าน trace ได้แก้ service-catalog fuzzy scan:

```text
should_detect_game =
  game presence/location
  OR booking selection

ไม่ใช่:
  intent.domain == games
```

Focused probe:

Artifact: `../20260823_service_catalog_fuzzy_fix_probe9/REPORT.md`

| Case type | Before | After |
|---|---:|---:|
| Cockpit list | 3.0356s | 0.3019s |
| PS5 + Switch compound list | 5.8517s | 0.5085s |
| PS5 Zone list | 5.5404s | 0.3211s |
| Nintendo 1-2 list | 5.9847s | 0.3410s |
| Nintendo 1-4 list | 6.3254s | 0.3478s |
| VR 1 hour list | 5.1808s | 0.3350s |

Named game availability/booking ยังผ่าน:

- TEKKEN availability 0.3161s
- VALORANT availability 0.4136s
- VALORANT booking selection 0.2921s

Probe ผ่าน 9/9

### 9.1 Affected 460 v1 พบ second-order timeout

เมื่อขยาย test เป็น games, availability, reservation และ compound รวม 460 cases:

- ผ่าน 457/460
- Average 1.0445s, P95 5.9929s, max 9.1671s
- 3 failures เป็น compound Cockpit ราคา+จองที่จบ `request_timeout_no_answer`
- ไม่มี LLM call

Trace/profile พบว่า booking child ที่มีข้อความยาวและ phrase `จะเล่น ... Cockpit ... เสีย จองยังไง` ใช้ structured execution 8.4-10.4 วินาที เพราะ:

1. Service availability เปิด fuzzy game scan จาก booking signal แม้ target เป็น zone ไม่ใช่ชื่อเกม
2. Reservation facts ทำ fuzzy scan ทุก fact ทั้งที่มี exact alias `จองยังไง`

Artifact failure: `../20260823_service_catalog_postfix_affected460/REPORT.md`

### 9.2 Exact-first + target-aware fuzzy gating

แก้โดย:

- booking zone ใช้ exact game lookup และไม่เปิด fuzzy หากไม่มี `เกม/game` หรือ presence/location intent
- reservation facts ทำ exact pass ก่อน
- ถ้า exact ไม่พบ จึง flatten aliases แล้ว fuzzy เพียง pass เดียว
- tie ของ exact aliases เลือก alias ที่ยาว/เฉพาะกว่า

Isolated warm reproduce:

- booking child ลดจาก 8.4-10.4s เหลือ 0.56-0.62s
- parent Cockpit ราคา+จองลดจาก timeout/7.5s เหลือประมาณ 1.21s

Affected-scope v2:

| Metric | v1 | v2 |
|---|---:|---:|
| Total | 460 | 460 |
| Passed | 457 | 460 |
| Pass rate | 99.35% | 100% |
| Average | 1.0445s | 0.6152s |
| P95 | 5.9929s | 1.0512s |
| Max | 9.1671s | 1.6804s |
| Compound pass | 86/89 | 89/89 |
| Compound average | 3.3144s | 0.8449s |
| Compound P95 | 8.8105s | 1.3794s |
| LLM calls | 0 | 0 |

Artifact ล่าสุด: `../20260823_service_catalog_postfix_affected460_v2/REPORT.md`

## 10. สิ่งที่ผลนี้พิสูจน์

1. 8 correctness/latency pipelines แก้ technical failures หลักจาก fresh run เดิม
2. General clear path ใช้หนึ่ง call และต่ำกว่า backend deadline
3. Health manager ไม่ปิด General จาก optional planner/reviewer failure ในรอบยาว
4. Context ของ Universal Intent และ General ใช้ 3072 ตรงกัน
5. Structured/Fast ยังเป็นแกนหลัก
6. ไม่มี request timeout ใน sequential 1,600 run
7. Affected scope หลัง micro-fixes ผ่าน 460/460 โดย max 1.6804 วินาที

## 11. สิ่งที่ผลนี้ยังไม่พิสูจน์

1. 20 concurrent users จะตอบภายใน 10 วินาที
2. Queue wait ภายใต้ LLM concurrency 1
3. Session isolation ระหว่าง Web/Facebook users
4. Multi-process safety เพราะ semaphore ยังเป็น in-process
5. BGE cost/benefit เพราะไม่ได้เปิด
6. Semantic RAG quality เพราะ vector backend ยังไม่ใช่ semantic embedding เต็มรูปแบบ
7. Human correctness ของ pass 1,599 cases
8. Network latency ของ Facebook/Web channel
9. Full 1,600 หลัง micro-fixes สองรายการสุดท้าย เพราะ rerun ล่าสุดครอบคลุมเฉพาะ affected scope 460 cases

## 12. งานต่อ

1. รัน multi-user load test 5, 10 และ 20 sessions
2. แยก service time กับ queue wait
3. วัด end-to-end P50/P95/P99/max และ timeout rate
4. ตรวจ session context leakage
5. ออกแบบ shared queue/worker ก่อนเปิดหลาย backend processes
6. ทำ human audit sample ของ pass cases
7. เพิ่ม source ของ ROV bug penalty หากมีเอกสารจริง
8. Optimize unknown-game deterministic chain และ rare vector cold path
