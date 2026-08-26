# วิเคราะห์ Failure และเวลา - Fresh Typhoon 1,600 Cases

## คำตอบตรงประเด็น

ข้อที่ไม่ผ่านส่วนใหญ่ไม่ได้เกิดจาก timeout เพราะ failure 60 ข้อกับ slow over 10s 44 ข้อซ้อนกันเพียง 3 ข้อ

- ทั้งหมด: `1600`
- ผ่าน: `1540`
- ไม่ผ่าน: `60`
- เกิน 10 วินาที: `44`
- ไม่ผ่านและเกิน 10 วินาที: `3`
- ไม่ผ่านแต่ไม่เกิน 10 วินาที: `57`
- เกิน 10 วินาทีแต่ยังผ่าน: `41`
- Explicit TimeoutError/deadline exception: `0`
- เกิน configured 20 วินาที: `1`

ดังนั้นต้องแยกคำว่า `ไม่ผ่าน`, `ช้ากว่าเป้า 10 วินาที` และ `timeout exception` ออกจากกัน

## Failure 60 ข้อ

| Assessment | จำนวน | ความหมาย |
|---|---:|---|
| Chatbot ผิดจริง | 40 | route, exception, unsupported claim หรือคำตอบคนละเรื่อง |
| Judge ตรวจพลาด | 19 | คำตอบสื่อความหมายถูกแต่ไม่ตรง exact keyword |
| ต้องตัดสิน Product Policy | 1 | contract เดิมขัดกับเป้าหมาย broad assistant |

| Root cause | จำนวน |
|---|---:|
| `general_concept_misrouted_equipment` | 26 |
| `judge_false_negative_thanks_synonym` | 11 |
| `substring_collision_price_in_kho_sia` | 9 |
| `judge_false_negative_latency_synonym` | 7 |
| `system_exception` | 2 |
| `substring_collision_animal_crossing` | 1 |
| `wrong_route_game_ranking` | 1 |
| `unsupported_freshness_hallucination` | 1 |
| `product_scope_policy_mismatch` | 1 |
| `judge_false_negative_activity_synonym` | 1 |

### Root cause หลัก

1. `general_concept_misrouted_equipment` 26 ข้อ: คำว่า keyboard ชนะ operation `คืออะไร` ทำให้ตอบรายการอุปกรณ์ PSU แทนคำจำกัดความ
2. `substring_collision_price_in_kho_sia` 9 ข้อ: `ข้อเสีย` มี substring `เสีย` จึงถูกตีเป็น price query และถามกลับเรื่องบริการ/โซน
3. `judge_false_negative_*` 19 ข้อ: `ความล่าช้า`, `ขอบพระคุณ`, `งานแข่งขันเกม` ถูกความหมายแต่ exact-keyword judge ไม่ยอมรับ
4. `system_exception` 2 ข้อ: UnboundLocalError ทำให้ answer ว่าง
5. อีก 4 ข้อ: Animal Crossing substring collision, game-zone ranking ผิด route, freshness hallucination และ product-scope policy mismatch

## Slow 44 ข้อ

| Latency cause | จำนวน | อธิบาย |
|---|---:|---|
| Two sequential LLM calls | 41 | Intent/review call แล้วตามด้วย answer call |
| Single slow generation | 2 | call เดียวแต่ generation เกิน 10 วินาที |
| Wrong-route expensive retrieval | 1 | route ผิดและ retrieval/entity work แพง |

41 double-call cases มี wall เฉลี่ย `14.7497s`, visible final LLM เฉลี่ย `7.5321s` และเวลาที่ไม่อยู่ใน visible final call เฉลี่ย `7.2176s`

`results.llm_call_count` บันทึก 1 call แต่ final metadata ระบุ `llm_budget_used_calls=2` จึงเป็น telemetry gap ด้วย ไม่ใช่หลักฐานว่าใช้ LLM แค่ครั้งเดียว

## ลำดับแก้ที่แนะนำ

1. P0: แก้ UnboundLocalError และเพิ่ม state initialization test
2. P0: เปลี่ยน raw substring matcher เป็น boundary/context-aware matcher สำหรับ `ข้อเสีย`, `cross` และ price/control terms
3. P0: ให้ deterministic game ranking และ exact entity veto route/ambiguity ที่ผิด
4. P1: ทำ operation-first distinction ระหว่าง general definition กับ PSU inventory lookup
5. P1: ทำ clear-general one-call path และ shape-based token budget เพื่อตัด double LLM
6. P1: เพิ่ม freshness guard ที่ต้องมี live source/timestamp หรือ no-answer
7. P2: แยก semantic correctness evaluator ออกจาก style/keyword lint โดยไม่แก้ expected ให้ตามคำตอบผิด
8. เพิ่ม append-only timing/call ledger เพราะ trace cap 12 และ `llm_call_count` ปัจจุบันอธิบาย hidden call ไม่ครบ

## ข้อจำกัด

- Judge ปัจจุบันเป็น heuristic จึงมีทั้ง false negative และอาจมี false positive; ตัวเลขที่ปรับ false negative แล้วไม่ใช่ human-approved accuracy
- Trace output จำกัด 12 entries ในเกือบทุกเคส จึงต้อง focused reproduction เมื่อต้องหา first wrong stage ที่เกิดก่อน retained trace
- รอบนี้ใช้ global profile 20 วินาที ไม่ใช่ product profile 10 วินาที
