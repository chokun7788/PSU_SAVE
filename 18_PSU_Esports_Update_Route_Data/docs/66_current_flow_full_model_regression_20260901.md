# ผลทดสอบ Current Flow: FAQ 1,600 + Keyboard 500 + Canonical Pilot 16

วันที่ทดสอบ: 1 กันยายน 2026, Asia/Bangkok

## สรุปตรง ๆ

**รันครบแล้ว แต่ยังไม่ควรเปิด Guard แบบ enforce และ Canonical Pilot ชุดนี้กับผู้ใช้จริงทันที**

- FAQ ผ่านเงื่อนไขเดิม **1,456/1,600 = 91.00%** ลดจาก **1,509/1,600 = 94.31%** ในรอบ 31 สิงหาคม
- มีข้อที่เคยผ่านแล้วตก 56 ข้อ และเคยตกแล้วผ่าน 3 ข้อ จึงลดสุทธิ 53 ข้อ หรือ 3.31 จุดเปอร์เซ็นต์
- ผลกระทบใหม่ส่วนใหญ่มาจาก Guard สกัดคำถามปกติ และ Pilot รับคำถามรายชื่อเกมทั้งที่ข้อมูลทดลองไม่ครบ
- เส้นทาง `semantic_rag_dynamic` เดิมยังเลือกหลักฐานผิด target/facet ได้ มีแหล่งอ้างอิงไม่ได้แปลว่าตอบตรงคำถาม
- Keyboard 500 ตรวจผิดแป้นพิมพ์ได้ครบ 240 กรณีที่มีผลตรวจ แต่ตัวอักษรซ้ำหลุด 27 กรณี และมี false positive 2 กรณี
- Pilot ผ่าน **15/16** ข้อ ข้อที่ตกถูก Guard สกัดก่อนถึง Pilot ส่วนการเรียก LLM จัดลำดับหลักฐานสองครั้ง timeout ทั้งคู่ คำตอบเอกสารจึงใช้ verified draft fallback
- ยังไม่ผ่านเป้าหมายทุกคำถามต้องตอบภายใน 10 วินาที และยังไม่ได้ทดสอบผู้ใช้พร้อมกัน

นี่เป็น **การทดลองเปิด Guard + Pilot** ไม่ใช่ controlled A/B ที่เปลี่ยนเพียงตัวแปรเดียว และไม่ได้เปลี่ยนค่า Production

## เปิดอ่านไฟล์

- [คำถามและคำตอบทุกข้อ](../reports/current_flow_regression/20260901_full_model_enabled/questions_answers.md)
- [วิเคราะห์ข้อที่ต้องตรวจต่อ พร้อมคำถาม คำตอบ และ contract](../reports/current_flow_regression/20260901_full_model_enabled/analysis/cases_requiring_review.md)
- [วิเคราะห์รายข้อครบ 2,116 รายการ JSONL](../reports/current_flow_regression/20260901_full_model_enabled/analysis/per_case_analysis.jsonl)
- [Raw outputs และ Trace เต็ม](../reports/current_flow_regression/20260901_full_model_enabled/results.jsonl)
- [คะแนนและเวลาแยกส่วน](../reports/current_flow_regression/20260901_full_model_enabled/analysis/metrics.json)
- [วิธีทดสอบและข้อจำกัด](../reports/current_flow_regression/20260901_full_model_enabled/evaluation_protocol.md)
- [รายละเอียดภายในตัวตรวจพิมพ์ผิด](../reports/current_flow_regression/20260901_full_model_enabled/analysis/guard_span_diagnostics.jsonl)

คำถาม-คำตอบแบ่งไฟล์ละไม่เกิน 100 ข้อ รวม 22 ไฟล์ เพื่อเปิดอ่านได้ง่าย Raw output ไม่ถูกแก้เพื่อให้ผ่าน ส่วนการจัดกลุ่มสาเหตุอยู่ในไฟล์ analysis แยกต่างหาก

## 1. รอบนี้รันอะไร

| รายการ | ค่าที่ใช้ |
|---|---|
| FAQ | 1,600 ข้อจาก `model_benchmark_1500.jsonl` |
| Keyboard | 500 ข้อจากชุดวันที่ 2026-08-30 |
| Canonical | 16 acceptance cases จากเกม/กฎสมมติสอง records |
| LLM | `scb10x/typhoon2.5-qwen3-4b` บน Ollama localhost |
| Embedding | `psu-bge-m3:q8_0`, 1,024 dimensions |
| Input Guard | Runtime ตัวจริง, `enforce`, `ask_retype`; thresholds 0.39/0.55 |
| Canonical storage | SQLite ทดลองแยกจากข้อมูลจริง |
| Global budget | 9 วินาที; เกณฑ์ส่งคำตอบไม่เกิน 10 วินาที |
| Watchdog ของตัวทดสอบ | 30 วินาที แล้วหยุดเฉพาะ worker ที่ค้าง |
| การรัน | Serial, ไม่มีประวัติ session, เปิด model-enabled ทุกชุด |
| Hardware จริง | RTX 4050 Laptop GPU, VRAM 6,141 MiB |

ไม่มีการรัน No-LLM baseline และไม่มีการใช้ Cloud Chatbot API อย่างไรก็ตาม Flow ยังข้ามโมเดลได้ตาม gate สำหรับ Fast/Structured/Guard ตามการออกแบบเดิม

Hardware นี้ไม่ใช่ RTX 5060 8GB ของเครื่องเป้าหมาย ผลจึงไม่ใช่คำรับรองความเร็วบน Server เป้าหมาย

## 2. FAQ 1,600

| ตัวชี้วัด | รอบก่อน | รอบนี้ |
|---|---:|---:|
| ผ่าน contract เดิม | 1,509 | 1,456 |
| อัตราผ่าน | 94.31% | 91.00% |
| ไม่ผ่าน | 91 | 144 |
| ผ่านพร้อม validation และ <=10 วินาที | ไม่ได้ใช้เป็นคะแนนหลักเดิม | 1,456 |
| Median | 0.474 วินาที | 0.583 วินาที |
| P95 nearest-rank | 4.783 วินาที | 3.570 วินาที |
| Mean ที่สังเกต | 2.705 วินาที | 1.140 วินาที |
| เกิน 10 วินาที | 9 | 10 |

**ห้ามสรุปจาก Mean ว่าแก้ความช้าแล้ว:** รอบนี้ตัดงานค้างที่ 30 วินาที และบางข้อถูก Guard สกัดอย่างรวดเร็ว ขณะที่รอบเดิมปล่อยข้อหนึ่งถึง 1,820.69 วินาที ค่าเฉลี่ยจึงเทียบตรง ๆ ไม่ได้ อีกทั้ง Median รอบนี้สูงขึ้น

ข้อ `MB-1123-SF-154` ที่เคยใช้ 1,820.69 วินาที รอบนี้ใช้ 0.431 วินาที จึงไม่เกิด outlier เดิมซ้ำ แต่ยังมีข้ออื่นค้าง ไม่ใช่หลักฐานว่าต้นเหตุถูกแก้แล้ว

### 144 ข้อที่ไม่ผ่าน แยกตามผลลัพธ์ปลายทาง

| กลุ่ม | จำนวน | ความหมาย |
|---|---:|---|
| `semantic_rag_dynamic` | 66 | ไม่ผ่าน contract ทั้ง 66 ข้อ บางข้อผิดเรื่องจริง บางข้อตกจาก label หมวด |
| Pilot ขอ clarification เรื่อง catalog | 28 | ฐานทดลองไม่ครบ จึงไม่ตอบรายชื่อ/จำนวนเกมเดิม |
| Input Guard ขอพิมพ์ใหม่ | 26 | มีคำถามปกติถูกสกัด เช่น จอง PS5, วันนี้เปิดไหม |
| Structured game detail ไม่ตรงข้อความที่คาด | 12 | ต้องแยกการ paraphrase ที่ถูกความหมายจากการตกหล่นของข้อมูล |
| Timeout/worker failure | 10 | Watchdog 7, worker crash 1, pipeline ตอบ timeout ช้า 2 |
| อื่น ๆ | 2 | multi-name fast path 1 และ Answer Contract no-answer 1 |
| รวม | **144** | ตารางนี้นับแต่ละข้อครั้งเดียว |

ไม่ควรแปลว่า RAG ทั้ง 66 ข้อให้ข้อเท็จจริงเท็จทั้งหมด เพราะตัวตรวจรวม category/mode ด้วย แต่มีหลักฐานชัดว่าบางข้อผิดเกมหรือผิดประเด็นจริง

### 56 ข้อที่เคยผ่านแล้วตก

- 26 ข้อ: Pilot เปลี่ยน catalog answer เป็น clarification
- 24 ข้อ: Guard เปลี่ยนคำตอบเดิมเป็นขอพิมพ์ใหม่
- 2 ข้อ: semantic RAG
- 2 ข้อ: structured game detail
- 2 ข้อ: ไม่มีคำตอบเพราะ watchdog

อีก 88 ข้อตกทั้งสองรอบ และมี 3 ข้อดีขึ้น รายการ ID อยู่ใน `metrics.json -> faq.change_ids`

## 3. Keyboard 500

มีผล Guard บันทึกจริง 499 ข้อ อีก 1 ข้อคือ `KIA-0487` ไม่มีผลก่อน worker ปิด จึงไม่ถูกนับเป็น true negative

| สิ่งที่ตรวจ | TP | FP | FN | TN | ยังไม่มีผล |
|---|---:|---:|---:|---:|---:|
| ผิดแป้นพิมพ์ | 240 | 0 | 0 | 259 | 1 |
| ตัวอักษรซ้ำ | 173 | 2 | 27 | 297 | 1 |

- Layout precision/recall = 100% เฉพาะผลที่สังเกตในชุดนี้ ไม่ใช่ความแม่นยำบนการใช้งานจริงทั้งหมด
- Repeat precision = 98.86%, recall = 86.50%
- Repeat ที่หลุด 27 ข้อ: แบบผสมผิดแป้นพิมพ์+ตัวซ้ำ 13, ซ้ำภายในภาษาไทย 7, สระ/เครื่องหมายไทยซ้ำ 5, token สั้น 2
- 13 ข้อในกลุ่มผสมยังถูกสกัดจากสัญญาณผิดแป้นพิมพ์ อีก 14 ข้อที่ซ้ำหลุดเข้าเส้นทางตอบ
- False positive สองข้อมีหนึ่งข้อเป็นคำถามปกติ `KIA-0470`: "วันนี้เปิดไหม???" ซึ่งถูกมองว่า `นน` ใน "วันนี้" เป็น typo

### การตอบหลังผ่าน Guard

| ผลการเดินทาง | จำนวน |
|---|---:|
| ขอพิมพ์ใหม่ | 367 |
| ผ่านเข้า Pipeline | 132 |
| ยังไม่ทราบผล Guard เพราะ worker ปิด | 1 |
| รวม | 500 |

จาก 132 ข้อที่เข้า Pipeline มี source FAQ contract 62 ข้อ ผ่าน 56/62 = **90.32%** อีก 70 ข้อไม่มี answer gold จึงยังไม่ให้คะแนนความถูกต้องของเนื้อหา

เมื่อเทียบ **62 ID เดียวกัน** รอบก่อนผ่าน 58/62 = 93.55% รอบนี้ผ่าน 56/62 = 90.32% จึงไม่ได้ดีขึ้น ส่วนคะแนนเก่า 142/175 = 81.14% ใช้คนละ denominator ห้ามเอามาเทียบแล้วกล่าวว่าแม่นขึ้นเพราะ 90.32 สูงกว่า 81.14

Label เดิมของการพิมพ์ซ้ำบางกลุ่มต้องการ warn/continue แต่ policy รอบนี้เป็น ask_retype จึงเกิด block-policy disagreement 127 ข้อ ซึ่งไม่ได้หมายถึงตรวจ anomaly ผิดทั้งหมด ห้ามเปลี่ยน label เงียบ ๆ เพื่อทำคะแนนให้ดีขึ้น

### ทำไมชุด 500 ดูดี แต่ FAQ ถูกสกัด

ชุด 500 มีขอบเขตคำศัพท์และรูปประโยคจำกัด จึงยังไม่ครอบคลุม negative examples เช่น "จอง PS5 ต้องทำยังไง", "วันนี้เปิดไหม" และ "ช่วยยกตัวอย่าง" เพียงพอ รอบ FAQ พบ layout block 9 ข้อ และ repeat block 17 ข้อ ต้องนำกรณีปกติเหล่านี้ไปตรวจแยกจากชุดที่ตั้งใจทำให้ผิด

### Output เมื่อถูกสกัด

กรณี `g]jo` ระบบตอบจริงว่า:

> เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน กรุณาตรวจสอบภาษาแป้นพิมพ์แล้วพิมพ์คำถามใหม่อีกครั้งครับ

กรณีตัวอักษรซ้ำ:

> ข้อความนี้อาจมีตัวอักษรซ้ำโดยไม่ตั้งใจ กรุณาตรวจสอบและพิมพ์คำถามใหม่อีกครั้งครับ

ไม่มีการแปลหรือแก้ข้อความแล้วส่งเข้าระบบตอบแทนผู้ใช้ การ mapping ที่เห็นใน diagnostic เป็นเพียง feature ภายใน detector

## 4. Canonical Pilot

ผ่าน 15/16 ข้อ, Mean 0.430 วินาที, สูงสุด 3.124 วินาที

ข้อที่ตกคือ `CP-14`: "จอง Nebula Fields" ควรเข้า `canonical_clarification` เพราะ Pilot ไม่ทำ booking แต่ถูก Guard ตัดเป็น `input_guard_layout_retype` ก่อน

ผลที่เข้าถึง Canonical จริง 15 ข้อ: answer 7, no-answer 2, partial 1, clarification 5

**ยังอ้างว่า LLM ของ Pilot ทำงานสำเร็จในรอบนี้ไม่ได้:**

- `CP-04`, `CP-05`: เรียก LLM จัดลำดับหลักฐานสองครั้งและ Timeout ที่ประมาณ 3 วินาทีทั้งคู่
- `CP-08`, `CP-09`, `CP-10`: ข้ามเพราะ health cooldown แล้วใช้ checked draft
- Accepted LLM ordering = **0 ครั้ง**
- คำตอบที่ยังผ่านมาจากหลักฐาน/ข้อความที่อนุมัติไว้และ fallback ที่รักษาข้อยกเว้น ไม่ใช่คำตอบที่โมเดลเรียบเรียงสำเร็จ

นี่พิสูจน์ว่าการ fallback ในกรอบข้อมูลสมมติช่วยรักษาคำตอบได้ แต่ไม่ได้พิสูจน์คุณภาพ LLM ordering หรือความสามารถรองรับข้อมูลใหม่ทุกประเภท ไม่ควรบังคับเพิ่มน้ำหนัก RAG เพียงเพื่อให้เส้นทางนี้ชนะ

## 5. สาเหตุที่ตรวจได้จาก Log และ Code

### A. RAG ล็อก route ก่อนยืนยัน target และ facet

ตัวอย่าง `MB-0093-G-005`: "Counter-Strike 2 คือเกมอะไร" กลับตอบบทความทักษะจาก Overcooked! 2

Trace แสดงว่า:

1. Router เริ่มที่ `games`
2. Semantic refiner เลือก `curated_knowledge_overcooked2_skills`, score 0.500492
3. เหลือ hit เดียว จึงคำนวณ second score เป็น 0 และ margin เป็น 0.500492
4. ล็อก route เป็น `knowledge` และ veto การแก้ route กลับ
5. Entity resolver กลับรู้ชื่อ `Counter-Strike 2` ถูกต้องอยู่แล้ว แต่ constraint นี้ไม่ปิดกั้นเอกสารผิดเกม
6. Semantic branch ตอบก่อนขั้น Question Frame ปกติ และ validation ให้ผ่าน

จุดตรวจ code: [semantic_vector_retrieval.py](../app/pipeline/semantic_vector_retrieval.py), [engine.py](../app/pipeline/engine.py)

`retrieve_semantic_guarded` ตรวจ category/time/trust แต่ไม่ได้ใช้ requested entity/facet เป็นข้อบังคับใน loop นี้ ส่วนการใช้ margin หลังกรองแล้วเหลือ hit เดียวทำให้ความมั่นใจดูสูงเกินหลักฐาน

**ควรแก้:** สร้าง Question Frame ที่เก็บ target/facet ต้นฉบับก่อน route refinement; filter/reject ตาม entity และ facet; เก็บสถานะ "ไม่มีคู่แข่งให้เทียบ" แทนการตีความ second=0 ว่าเป็นหลักฐานหนักแน่น; ให้ทุกทางใช้ Answer Contract เดียวกันก่อนส่ง

### B. Validation ตรวจหลักฐานได้ แต่ยังปล่อยคำตอบผิดคำถาม

ตัวอย่าง `MB-0089-G-001`: ถาม VALORANT คือเกมอะไร แต่ตอบข่าวการแข่งขัน VALORANT จึงตรงชื่อเกมแต่ผิด facet

ใน `_build_result` มีการตรวจรอบท้ายด้วย query ว่าง และ route อาจถูก semantic override ไปแล้ว การตรวจรูปแบบ/source จึงไม่ทดแทนการเทียบกับ target/facet เดิม

**ควรแก้:** เก็บ immutable answer obligations ตั้งแต่ input; ตรวจก่อนส่งว่า "อธิบายเกม" ไม่ถูกแทนด้วย "ข่าวเกม" และ "มีให้เล่นไหม" ไม่ถูกแทนด้วย "ประโยชน์ของเกม" การมี citation ต้องเป็นเงื่อนไขหนึ่ง ไม่ใช่เงื่อนไขเดียว

### C. Guard ใช้คะแนนรูปคำปลายทางมากเกินไป

Diagnostic ของ "จอง" ภายใน `MB-0462-R-003`:

- คำเดิมมี quality 0.939254
- ข้อความสมมติเมื่อสลับแป้น `0v'` มี quality 0.925573 ซึ่งต่ำกว่าคำเดิม
- gain = 0, target ไม่ใช่คำที่รู้จัก แต่ span score ยังได้ 0.527577 สูงกว่า threshold 0.39

จุดตรวจ: `_score_th_to_en_span` ใน [keyboard_input_anomaly.py](../app/core/keyboard_input_anomaly.py)

**ควรแก้:** ใช้หลักฐานเชิงเปรียบเทียบกับความสมเหตุสมผลของข้อความเดิม ไม่ใช้ absolute target score อย่างเดียว; แยกการ calibrate ตามทิศภาษา/ความยาว/คำที่รู้จัก; อย่าให้คำไทยปกติถูก block เพียงเพราะ mapping เป็น ASCII ที่ character profile ให้คะแนนสูง

### D. ตัวซ้ำข้ามรอยต่อคำถูกเข้าใจผิด

- `MB-0482-S-003`: "วันนี้เปิดไหม" มี `นน` ตามรูปคำที่ถูกต้อง แต่การลบหนึ่งตัวเป็น "วันี้เปิดไหม" กลับได้คะแนน profile สูงกว่า
- `MB-1464-GL-139`: `ยย` ระหว่าง "ช่วย" กับ "ยก" ถูกลดเหลือ "ช่วยก" แล้วได้คะแนนสูงกว่า

จุดตรวจ: `_score_repeat` และ `_form_evidence` ใน [keyboard_input_anomaly.py](../app/core/keyboard_input_anomaly.py)

**ควรแก้:** แยก duplicated combining marks ที่ชัดเจนจากพยัญชนะซ้ำที่อาจเป็นรอยต่อคำ; ใช้ word/grapheme context และ contrastive evidence; ประเมิน valid-negative ที่หลากหลาย ไม่ใช่เพิ่ม Alias ของทั้งประโยคทีละอัน หรือปรับ threshold จากชุด test นี้โดยตรง

### E. Catalog ownership กว้างกว่าข้อมูลที่ Pilot มี

คำถาม "มีเกมทั้งหมดกี่เกม" และ "PS5 มีเกมอะไรบ้าง" ถูก Canonical รับก่อนระบบเก่า เพราะ `broad_catalog` ตรวจเพียงว่ามี ownership และเข้า pattern

จุดตรวจ: [answer.py](../app/knowledge/answer.py) บริเวณ `broad_catalog`

การไม่อ้างจำนวนจากข้อมูลไม่ครบเป็นสิ่งถูก แต่การเปิด Pilot แล้วทำให้คำถามเดิมตอบไม่ได้คือ compatibility gap

**ควรแก้:** สร้าง catalog projection ที่รวมข้อมูลเดิมและใหม่ พร้อม coverage/version/scope; แยก "ข้อมูลเกี่ยวกับเกม" จาก "เกมที่ยืนยันว่ามีให้บริการ"; อย่าเพิ่มเกม availability=unknown ลงยอดบริการ และอย่าให้ rule-only/demo records รับ ownership ของ catalog จริงทั้งหมด

### F. งาน fuzzy matching บน CPU ไม่มีขอบเขตที่เพียงพอ

Stack จากหลายข้อ เช่น `MB-0499-M-010`, `MB-0503-M-014`, `MB-1232-M-052` อยู่ใน:

```text
normalization._best_compact_window_ratio
  -> difflib.SequenceMatcher
  -> fast_answer._match_game_detail / _match_supported_game
  -> answer_games / answer_equipment
```

คำถามบุคลากรบางข้อไปวนเทียบ game aliases ใน fallback การตรวจ deadline หลังจบขั้นตอนไม่สามารถหยุด loop นี้กลางทาง

จุดตรวจ: [normalization.py](../app/core/normalization.py) บริเวณ `_best_compact_window_ratio`/`contains_alias`, [fast_answer.py](../app/runtime/fast_answer.py)

**ควรแก้:** pre-normalize/index aliases; shortlist candidates ก่อน fuzzy matching; จำกัดจำนวน candidate/window/ความยาว; ตรวจเวลาคงเหลือภายใน loop; ไม่เรียก game/equipment fallback เมื่อ task เป็น members และไม่มี game target; ออก safe response ด้วยเวลาสำรอง

Watchdog รอบนี้ช่วยให้ทดสอบต่อได้เท่านั้น ไม่ใช่ production deadline implementation

### G. Model-enabled ไม่เท่ากับทุก model call สำเร็จ

มี facts-composer decision ที่ข้ามเพราะ health 96 รายการ และ Canonical ordering timeout สองครั้ง จึงต้องแยก timeout/skip/response/accepted output

สำหรับ Canonical ยังไม่ยืนยันว่า timeout เกิดจาก model load, context change, queue หรือ inference ส่วนใด เพราะ call ที่ timeout ไม่มี breakdown จาก Ollama ครบถ้วน ต้องเก็บ role-specific warmup, queue wait, load, prompt evaluation และ generation แยกก่อนปรับ budget

### H. Worker crash ยังไม่ทราบต้นเหตุแน่ชัด

พบ Windows access violation ใน `worker_002.log` และ `worker_009.log` ไม่ใช่ Python exception ที่แอปจัดการตามปกติ

`KIA-0487` ไม่มีแม้แต่ guard event และ log สุดท้ายของ worker ยังกล่าวถึงข้อก่อนหน้า จึงห้ามสรุปว่าข้อความ Hollow Knight เป็นสาเหตุของ crash ต้องแยกทดสอบ Python runtime, native dependencies และตัวเก็บ stack ด้วย workload เดิมต่อไป

## 6. ตัวอย่างที่ควรตอบต่างจากผลจริง

| ID | ปัญหาที่เห็น | สิ่งที่คำตอบควรทำ |
|---|---|---|
| MB-0093-G-005 | ถาม CS2 แต่ตอบ Overcooked! 2 | อธิบาย CS2 จากข้อมูลของ CS2 หรือบอกว่าไม่มีหลักฐาน ห้ามเปลี่ยนเกม |
| MB-0089-G-001 | ถามตัวเกม VALORANT แต่ตอบข่าวแข่ง | ตอบ overview ของเกม ไม่ใช่ข่าว |
| MB-0797-AG-136 | ถามมี Overcooked! 2 ไหม แต่ตอบประโยชน์เกม | ตอบ availability ตามแหล่งบริการ หรือระบุว่ายังยืนยันไม่ได้ |
| MB-0462-R-003 | คำถามจอง PS5 ปกติถูกขอพิมพ์ใหม่ | ให้ขั้นตอนจองตาม FAQ ที่ตรวจสอบแล้ว |
| MB-0482-S-003 | "วันนี้" ถูกมองว่าพิมพ์ซ้ำ | ตรวจตารางและข้อยกเว้นวันเปิดปิดตามวันที่จริง |
| MB-0499-M-010 | ถามบุคลากรแล้วค้างใน game fuzzy lookup | ค้น member/role พร้อมข้อมูลช่วงเวลาที่มีผล ไม่วนค้นชื่อเกม |
| CP-14 | จองเกมสมมติถูกตีความว่าผิดภาษา | Clarify ว่า Pilot ไม่ทำ booking โดยไม่เพิ่มข้อเท็จจริงบริการ |
| KIA-0470 | "วันนี้เปิดไหม???" ถูก block | ไม่ตีความเครื่องหมายเน้นหรือรูปคำปกติเป็น typo |

### ตัวอย่างที่ไม่ควรนับเป็นเนื้อหาผิดทันที

- `MB-0092-G-004`: คำตอบมี "เกมยิงเชิงกลยุทธ์แนว Tactical FPS" แต่ judge ต้องการ substring อีกแบบ จึงตก แม้ส่วนอธิบายแนวเกมจะตรงความหมาย
- `MB-1228-M-048`: ชื่อ/ตำแหน่งในคำตอบสอดคล้องกับ contract ของ dataset แต่ตกเพราะ category เป็น `about_us` แทน `members` ต้องแยก label mismatch จากเนื้อหาผิด และยังต้องตรวจวันที่มีผลของข้อมูลบุคลากรก่อนใช้จริง

สองตัวอย่างนี้ไม่ได้รับรองข้อเท็จจริงอื่นทุกประโยคหรือสถานะบุคลากรปัจจุบัน เป็นการตรวจความสอดคล้องกับข้อมูลประเมินใน repository เท่านั้น

## 7. เวลาแต่ละส่วน

ค่าต่อไปนี้เป็นเวลาเฉลี่ยของ request ที่มี stage นั้นบันทึก รวมกรณี skip ของบาง stage ไม่ใช่เวลาเฉพาะ successful LLM call

| Stage | เฉลี่ย | P95 | หมายเหตุ |
|---|---:|---:|---|
| Input Quality Guard | 1.40 ms | 2.90 ms | เร็ว แต่ false positive กระทบคุณภาพ |
| Semantic route refiner | 36.51 ms | 139.75 ms | ต้องแก้ความถูกต้องของ scope มากกว่าความเร็ว |
| Question Frame | 74.14 ms | 132.68 ms | บาง RAG path ตอบก่อนขั้นนี้ |
| Candidate decisions | 83.94 ms | 150.20 ms | ข้อมูล timer ที่จบแล้ว ไม่รวมส่วนที่ค้างก่อนส่งผล |
| Ambiguity gate | 122.43 ms | 238.69 ms | มี repeated entity-resolution work |
| Facts composer | 364.25 ms | 2,937.56 ms | เฉลี่ยรวม skip; สูงสุดประมาณ 6.75 วินาที |
| General/experimental fallback | 1,227.26 ms | 2,136.84 ms | ขั้นที่ใช้เวลารวมมากในผลที่บันทึกสำเร็จ |
| Deterministic fallback | 236.04 ms | 112.51 ms | Mean ถูกดันจาก outlier; มี stage ที่จบช้าถึง 23.87 วินาที |
| Semantic RAG composer | 2,267.88 ms | 5,017.27 ms | มีเพียง 8 request ที่บันทึก stage นี้ |
| Canonical ranking หลัง embedding | 2.75 ms | 6.52 ms | ไม่รวม BGE query embedding; fixture มี candidate น้อย |

Stage อาจซ้อนกัน จึงห้ามบวกทุกค่าเป็นเวลาทั้ง request งานที่ watchdog ตัดไม่มี timer ปลายทางครบ การใช้ Stack เป็นหลักฐานจึงสำคัญกว่าดูตารางเวลาสำเร็จเพียงอย่างเดียว

Keyboard ที่เข้า Pipeline 132 ข้อมี P95 8.056 วินาทีและสูงสุด 28.102 วินาที ส่วนค่าเฉลี่ย 500 ข้อที่เพียง 0.540 วินาทีรวมข้อความที่ถูก Guard สกัด 367 ข้อ ไม่ใช่ความเร็วตอบคำถามทุกข้อ

### Model logs รวม FAQ และ Keyboard

| Role | Log entries รวม skip | ได้ข้อความกลับ |
|---|---:|---:|
| Facts composer | 207 | 100 |
| Universal intent | 116 | 106 |
| General LLM | 278 | 277 |
| RAG LLM | 8 | 7 |

Facts composer มีข้อความกลับ 100 รายการ แต่ยอมรับใช้ 79 และ reject 21 รายการ จำนวนข้อความกลับไม่ใช่จำนวนคำตอบที่ถูกต้อง ส่วน Canonical ordering นับแยกไว้ในหัวข้อ 4

## 8. ลำดับที่ควรแก้ต่อ

1. **อย่าเปิด rollout config นี้กับผู้ใช้จริงทันที:** เก็บ Guard เป็น shadow ระหว่างแก้ false positive และจำกัด Canonical rollout ให้ตรง coverage; รอบนี้ยังไม่ได้เปลี่ยนค่าของเว็บ
2. **แก้ entity/facet contract ก่อนเพิ่ม RAG priority:** สร้าง frame ก่อน retrieval, รักษา target เดิม, ตรวจ scope ก่อน route lock และตรวจคำตอบกับ frame เดิมทุก path
3. **แก้ Guard แบบ contrastive และ context-aware:** ยืนยันว่าคำเดิมไม่น่าใช่ภาษาที่ตั้งใจจริงก่อน block; รองรับรอยต่อคำไทยและรูปคำซ้ำที่ถูกต้อง โดยไม่มี auto-correction
4. **จำกัด CPU fuzzy work และ fallback routing:** budget ต่อ stage/candidate, cached normalization แบบมีขนาดจำกัด, gate เฉพาะ domain และ fallback ที่ส่งออกทันเวลา
5. **ทำ union catalog ที่มี completeness metadata:** รวม source เดิมกับ canonical อย่างถูก scope ก่อนรับคำถาม list/count ของระบบทั้งหมด
6. **แยกความเสถียรของโมเดลออกจาก draft fallback:** วัด warm/context/queue/inference ต่อ role; ทดสอบ Canonical ordering ให้มี accepted output จริงก่อนกล่าวว่าความสามารถ LLM ส่วนนี้ผ่าน
7. **ปรับ evaluator โดยไม่แก้ gold ให้เข้าข้างระบบ:** แยก route-label, required facts, target/facet, source support, coverage และ SLA พร้อม human review ของ paraphrases
8. **รันทวนทั้ง 1,600/500 และ held-out ใหม่:** แยก source question ก่อนสร้าง typo เพื่อไม่ให้ train/test แชร์ประโยคต้นฉบับ เพิ่ม clean negatives และทดสอบ HTTP/concurrency/session isolation บนเครื่องเป้าหมาย

ไม่จำเป็นต้องรื้อ Backbone ทั้งหมดทันที แต่ต้องแก้ขอบเขตความรับผิดชอบระหว่าง Guard, Question Frame, Retrieval, Catalog และ Final Contract ให้ครบก่อน การบังคับให้ RAG ชนะโดยไม่แก้ส่วนเหล่านี้จะทำให้คำตอบที่มี citation แต่ผิดเรื่องเพิ่มขึ้น

## 9. การตรวจสอบและข้อจำกัด

- รันครบ 2,116 ID และเก็บ output record ครบ แม้บาง record ระบุว่าไม่มีคำตอบจาก worker
- Source/data fingerprints ก่อนและหลังรันตรงกัน (`source_unchanged=true`)
- Unit tests ของ runner/analysis ผ่าน 12 ข้อ และ Canonical unit tests ผ่าน 48 ข้อ แยกจากคะแนน Model-enabled
- Guard diagnostic replay ใช้ profile เดิม; mapping ใช้วิเคราะห์ภายใน ไม่ใช้แทนคำถามของผู้ใช้
- Counter เบื้องต้นที่นับกรณีไม่มี guard event เป็น TN ถูกตรวจแก้ใน summary แล้ว เก็บต้นฉบับไว้ที่ `summary_initial.json` โดยไม่แก้ raw answers
- ทุกโจทย์ FAQ มี positive keyword assertions แต่ assertions ไม่ได้ตรวจความหมายและข้อเท็จจริงครบทุกประโยค
- วิเคราะห์อัตโนมัติครบทุกข้อ และอ่าน Trace/คำตอบของกรณีตัวแทนเชิงลึก ไม่ได้อ้างว่าตรวจความจริงทุกประโยคของ 2,116 คำตอบด้วยมนุษย์ครบแล้ว
- ยังไม่ได้วัด load ของ 20-30 ผู้ใช้, HTTP queue, client latency, peak RAM/VRAM ต่อ stage หรือ production uptime
- ไม่มีการแก้โค้ดตอบคำถามหรือเผยแพร่ฐานทดลองในรอบนี้ สิ่งที่เพิ่มคือ runner, analysis, tests และเอกสารผลทดลอง

ข้อสรุป: **ระบบมีส่วนที่ตอบได้และมี fallback ที่ช่วยได้ แต่ยังไม่พร้อมให้เปิด RAG-first/Guard enforce อย่างมั่นใจจากผลรอบนี้** ประเด็นเร่งด่วนคือไม่ตอบผิด target, ไม่สกัดภาษาไทยที่ถูกต้อง, และไม่ปล่อย CPU fallback เกินเวลา
