# Analysis: Full 1,600 FAQ Rerun After Timeout Fixes

วันที่รัน: 2026-09-02  
ชุดทดสอบ: `data/eval/model_benchmark_1500.jsonl` จำนวน 1,600 ข้อ  
โมเดล: `scb10x/typhoon2.5-qwen3-4b`  
Embedding/RAG: `psu-bge-m3:q8_0`  
Output directory: `reports/model_benchmark/20260902_full1600_rerun_after_timeout_fixes`

## 1. สรุปผลรอบใหม่

รอบใหม่ผ่าน 1,506/1,600 ข้อ หรือ 94.12%

Latency ดีขึ้นชัดเจน:

- Average latency: 0.8106 วินาที
- Median latency: 0.3347 วินาที
- P95 latency: 3.0857 วินาที
- Max latency: 8.0421 วินาที
- จำนวนข้อที่เกิน 10 วินาที: 0
- Validation failed: 0
- LLM calls: 470 ครั้ง

ดังนั้นรอบนี้ไม่มี timeout ในชุด 1,600 FAQ และไม่มี validation fail ที่ทำให้คะแนนตกเพิ่ม

## 2. ทำไมเคยเห็นจาก 94% เหลือ 91%

ตัวเลข 94.31% และ 91.00% มาจากคนละ runner และคนละเกณฑ์วัด

รอบ 94.31% มาจาก `run_model_benchmark_eval.py`

- โฟกัสการให้คะแนนคำตอบด้วย heuristic judge
- ไม่รวม Input Quality Guard แบบ production เต็มรูปแบบ
- ไม่รวม keyboard/canonical harness behavior
- ไม่นับ worker/harness timeout แบบเดียวกับ current-flow runner

รอบ 91.00% มาจาก `run_current_flow_regression.py`

- ใช้ flow ที่ใกล้ production มากกว่า
- นับ `strict_passed = legacy judge + validation + within 10s + worker status`
- เปิด Input Quality Guard แบบ enforce
- รวมผลกระทบจาก worker crash และ harness timeout
- มี canonical pilot/context behavior ที่ทำให้บางคำถาม route เปลี่ยน

สรุปสั้นๆ: คะแนนไม่ได้ลดเพราะคำตอบทั้งหมดแย่ลง แต่เพราะ runner 91% ใช้เกณฑ์เข้มกว่าและมี component เพิ่มขึ้น ทำให้เคสบางข้อถูกดักเป็น `input_guard_*`, `canonical_clarification`, `request_timeout_no_answer`, `harness_timeout` หรือ `worker_crash`

## 3. หลักฐานจากรอบ 91%

ผล `reports/current_flow_regression/20260901_full_model_enabled`:

- FAQ: 1,456/1,600 = 91.00%
- Fail รวม: 144 ข้อ
- Completed แต่ไม่ผ่าน: 136 ข้อ
- Harness timeout: 7 ข้อ
- Worker crash: 1 ข้อ
- เกิน 10 วินาที: 10 ข้อ

กลุ่มที่ตกมากที่สุด:

| Group | Fail |
|---|---:|
| games | 50 |
| members | 15 |
| competition_rules | 15 |
| game_controls | 12 |
| general_llm | 11 |
| compound | 10 |
| availability_service | 9 |
| availability_game | 9 |
| reservation | 5 |

Mode ที่ตกมากที่สุด:

| Mode | Fail |
|---|---:|
| `pipeline:semantic_rag_dynamic` | 66 |
| `canonical_clarification` | 28 |
| `input_guard_repeat_retype` | 17 |
| `pipeline:structured_game_detail` | 12 |
| `input_guard_layout_retype` | 9 |
| `harness_timeout` | 7 |
| `pipeline:request_timeout_no_answer` | 2 |
| `worker_crash` | 1 |

## 4. Root Cause หลักของ 94% -> 91%

### 4.1 Input Quality Guard ถูกเปิดแบบ enforce

มี 26 เคสใน FAQ ปกติที่ถูกตีว่าเป็น input ผิดภาษา/พิมพ์เบิ้ล แล้วบังคับให้พิมพ์ใหม่:

- `input_guard_repeat_retype`: 17
- `input_guard_layout_retype`: 9

ผลคือคำถามที่จริงควรไป Structured/Fast กลับถูกตอบเป็นข้อความให้พิมพ์ใหม่ จึง fail ตาม expected answer ของ FAQ

ตัวอย่างกลุ่มที่ได้รับผล:

- game controls
- reservation
- schedule
- members

### 4.2 Canonical pilot/context แทรก route ของ FAQ จริง

มี 28 เคสที่กลายเป็น `canonical_clarification` ทั้งที่ model benchmark เดิมตอบด้วย structured route ได้

สาเหตุเชิง flow:

- current-flow runner เปิด canonical knowledge pilot
- บางคำถามเกม/รายการถูกตีว่าเป็นข้อมูล canonical ที่ยังไม่ชัด
- ระบบจึงถาม clarification แทนที่จะตอบจาก structured catalog

ผลคือ category/mode ไม่ตรง expected contract

### 4.3 Member route เคยหลุดไป Game Resolver และเกิด timeout

ในรอบ 91% มีเคสสมาชิก timeout/crash ชัดเจน:

- `MB-0499-M-010`: harness timeout 30.000s
- `MB-0500-M-011`: worker crash 29.842s
- `MB-0503-M-014`: harness timeout 30.000s
- `MB-0507-M-018`: harness timeout 30.014s
- `MB-0518-M-029`: harness timeout 30.016s
- `MB-0519-M-030`: request timeout no answer 24.628s
- `MB-1229-M-049`: harness timeout 30.007s
- `MB-1232-M-052`: harness timeout 30.006s

ในรอบใหม่หลังแก้ focused slow cases กลุ่ม member ดีขึ้นมาก เช่น checkpoint รอบ 1,600 ใหม่:

- `MB-0500-M-011`: `structured_members_person_lookup` ประมาณ 0.087s
- `MB-0525-M-036`: `structured_members_role_lookup` ประมาณ 0.037s

### 4.4 RAG เลือก evidence ผิด category/target

รอบใหม่ยังเหลือ failure หลักที่ `semantic_rag_dynamic`:

- `category_mismatch:knowledge`: 39
- `category_mismatch:events_news`: 21
- `category_mismatch:clarification`: 13

แปลว่า RAG ยังมีปัญหาเลือกเอกสารคนละหมวดหรือคนละ target ในบางคำถาม โดยเฉพาะกลุ่ม `games`, `competition_rules`, `availability_game`

### 4.5 Structured game detail ขาด keyword ตาม strict judge

บางข้อได้ route ถูก แต่คำตอบขาดคำที่ตัวตรวจคาดไว้ เช่น:

- `missing_any:แนวเกม|เกม Battle Royale`
- `missing_any:แนวเกม|เกม Survival Horror`
- `missing_any:แนวเกม|เกม Action RPG`

กรณีนี้อาจเป็นได้ทั้งคำตอบไม่ครบจริง หรือ strict keyword คาดคำเฉพาะเกินไป ต้องแยก human review

## 5. สิ่งที่รอบใหม่ดีขึ้น

รอบใหม่ `20260902_full1600_rerun_after_timeout_fixes`:

- ไม่มีข้อเกิน 10 วินาที
- ไม่มี worker crash
- ไม่มี validation failed
- สมาชิกและ multi-question ที่เคย timeout กลับมาเร็ว
- Pass rate อยู่ 94.12% ใกล้กับรอบ 94.31%

เทียบกับรอบ 91%:

- Timeout/harness/worker problem หายไปใน runner นี้
- คะแนนกลับขึ้นจาก 91.00% เป็น 94.12%
- ยังต่ำกว่า 94.31% อยู่ 3 ข้อ และยังมี failure รวม 94 ข้อที่ต้องแก้เชิง correctness

## 6. จุดที่ยังต้องแก้ต่อ

ลำดับแนะนำ:

1. แก้ RAG target/category grounding
   - ให้ Question Frame lock `category`, `target`, `facet`
   - filter category ก่อน similarity scoring
   - ห้าม evidence คนละ target ชนะเพราะ vector score สูงอย่างเดียว

2. แยก Input Quality Guard สำหรับ production กับ eval
   - FAQ ปกติไม่ควรถูกดักเป็นพิมพ์ผิดง่ายเกินไป
   - เพิ่ม threshold หรือ allowlist pattern สำหรับคำถามสั้นที่เป็นคำถามจริง

3. ปรับ canonical pilot scope
   - canonical demo data ไม่ควร override structured catalog ของข้อมูลจริง
   - ใช้เฉพาะ record ที่ target ตรงและ source/version ชัด

4. ปรับ structured game detail answer template
   - บังคับ field สำคัญ เช่น แนวเกม, วิธีเล่น, เล่นได้ที่
   - ลด failure จาก missing keyword

5. รัน current-flow full 2,116 ซ้ำหลังแก้
   - ต้องยืนยันด้วย runner strict ตัวเดิม ไม่ใช่ดูเฉพาะ model benchmark
   - เป้าหมายคือ FAQ strict >= 94%, keyboard precision/recall ไม่ตก, canonical >= 15/16

## 7. ข้อสรุป

รอบใหม่ 1,600 FAQ ไม่ได้เหลือ 91% แล้ว แต่กลับมาเป็น 94.12% และไม่มี timeout เกิน 10 วินาที

สาเหตุที่เคยเห็น 91% คือใช้ runner ที่เข้มกว่าและเปิด component เพิ่ม ได้แก่ Input Quality Guard, canonical pilot, watchdog timeout และ worker crash handling ทำให้หลายเคสที่ model benchmark ผ่านถูกนับตก

ปัญหาหลักหลังจากนี้ไม่ใช่ timeout แล้ว แต่เป็น correctness ของ RAG และ routing โดยเฉพาะการเลือก evidence ให้ตรง category/target/facet
