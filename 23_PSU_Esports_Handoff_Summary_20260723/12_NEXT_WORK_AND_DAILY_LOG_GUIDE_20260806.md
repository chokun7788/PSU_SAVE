# PSU Esports Chatbot - Next Work and Daily Log Guide

## สถานะ ณ วันที่ 06/08/2026

ไฟล์นี้บอก session ใหม่ว่า หลังอ่าน handoff แล้วควรทำอะไรต่อ และ Daily Log ต้องเขียนอย่างไร

---

## 1. ก่อนเริ่มทำงานทุกครั้ง

1. อ่าน `10_CURRENT_PROJECT_ALL_IN_ONE_20260806.md`
2. อ่าน daily log วันที่ล่าสุด
3. ถ้างานเกี่ยวกับ flow/architecture ให้อ่าน `docs\38_current_chatbot_full_process_flow_20260803.md`
4. ตรวจ source code จริง เพราะเอกสารอาจล้าหลังโค้ด
5. ถ้าเป็น bug ให้ reproduce พร้อมดู mode/route/intent/target/source/trace
6. สรุป root cause ก่อนเลือกวิธีแก้
7. ห้ามแก้ test ให้ผ่านโดยลดมาตรฐานคำตอบ

---

## 2. งานที่ควรทำต่อ เรียงตามลำดับ

### Priority 1 - Full evaluation หลัง latest changes

เป้าหมาย:

- รัน case bank ประมาณ 1,600 cases หลังการแก้ Compound/Planner/Concurrency วันที่ 05/08
- รันอย่างน้อย 2 แบบ:
  - No-LLM
  - `scb10x/typhoon2.5-qwen3-4b`
- ใช้ config เดียวกันเรื่อง timeout, sample, judge และ endpoint
- เก็บ pass rate, average, median, P95, P99, max, timeout และ LLM call count
- อย่าสรุปจาก pass rate อย่างเดียว ต้องดูคำตอบจริงและ failure propagation

ผลลัพธ์ที่ควรสร้าง:

```text
results.jsonl
summary.json
REPORT.md
```

### Priority 2 - Failure analysis และ correctness repair

จัดกลุ่ม failure อย่างน้อย:

- `wrong_route`
- `wrong_intent`
- `wrong_target`
- `missing_subanswer`
- `unsupported_claim`
- `source_mismatch`
- `should_clarify`
- `timeout`
- `unnecessary_llm_call`
- `candidate_execution_mismatch`

วิธีทำ:

1. เปิดดูคำตอบจริง ไม่ดูเฉพาะ heuristic score
2. ตรวจ trace ว่าผิดที่ preprocess, target, route, candidate, retrieval, validation หรือ formatting
3. แก้ pattern ระดับระบบก่อนเพิ่ม keyword rule
4. เพิ่ม regression test จากเคสจริงทุกครั้งที่แก้ปัญหาสำคัญ
5. รัน focused tests ก่อน แล้วค่อยรันชุดใหญ่

### Priority 3 - Multi-user/load test

ทดสอบอย่างน้อย 5 sessions พร้อมกัน:

- คำถาม structured/fast
- คำถาม Intent LLM
- complex compound
- general LLM
- follow-up ที่ใช้ session context

ต้องวัด:

- request latency
- queue/slot wait
- P50/P95/P99/max
- timeout rate
- LLM busy fallback
- session context ปนกันหรือไม่
- Ollama CPU/GPU/RAM utilization ถ้าวัดได้

ข้อควรจำ:

- `PSU_LLM_MAX_CONCURRENCY=1` เป็น in-process guard
- ยังไม่ใช่ distributed queue
- ถ้าจะใช้หลาย process ต้องออกแบบ shared queue/worker หรือ inference service กลาง

### Priority 4 - Game control source verification

- ตรวจรายการที่มี `secondary_needs_manual_verify`
- ตรวจ VR ที่เป็น partial official controls
- เปรียบเทียบกับ control layout บนเครื่องจริงของ Studio หากทำได้
- ห้ามเปลี่ยนปุ่มโดยไม่มี source หรือหลักฐานจากเครื่องจริง
- เก็บ source URL, platform, version และวันที่ตรวจ

### Priority 5 - Retrieval improvement

ทำเมื่อ structured correctness และ load control เริ่มนิ่ง:

- semantic embedding model แบบ local
- hybrid BM25/vector
- gated reranker
- query rewriting/decomposition
- grounded multi-source composer

อย่าเปิด retrieval/LLM ทุกคำถาม เพราะจะเพิ่ม latency และอาจลดความแม่นของ structured facts

### Priority 6 - Feature scope ที่ต้องถามผู้ใช้ก่อน

- Booking จะเป็นเพียงคำแนะนำ หรือทำ transaction จริง
- ข่าว/กิจกรรมจะอัปเดตจาก source ใดและบ่อยแค่ไหน
- จะใช้ web API จริงหรือ terminal/local demo เป็นหลัก
- ต้องรองรับผู้ใช้พร้อมกันกี่คนใน production

---

## 3. Definition of Done ของงานแก้ระบบ

งานหนึ่งถือว่าเสร็จเมื่อ:

- reproduce ปัญหาเดิมได้
- ระบุ root cause ได้
- แก้ logic/data ที่ต้นเหตุ
- คำตอบใหม่ตรง operation, target และ source
- validator/answer contract ผ่านโดยไม่ลดมาตรฐาน
- regression test ของเคสเดิมผ่าน
- smoke tests ที่เกี่ยวข้องผ่าน
- ตรวจว่าไม่ทำให้หมวดใกล้เคียงพัง
- มี latency/LLM call comparison ถ้างานกระทบ performance
- อัปเดต Daily Log แล้ว

---

## 4. Daily Log อยู่ที่ไหน

```text
C:\Users\Chokhun\Downloads\Learn-LLM\17_PSU_Esports_Daily_Logs
```

ชื่อไฟล์ใช้วันที่ปัจจุบัน:

```text
YYYY-MM-DD.md
```

ถ้ามีไฟล์ของวันนั้นแล้ว ให้เพิ่มหัวข้อ `Latest Update` ใหม่ไว้ด้านบนใต้ H1 ห้ามสร้างไฟล์ซ้ำหลายชื่อสำหรับวันเดียว

---

## 5. เมื่อไหร่ต้องเขียน Daily Log

ต้องเขียนเมื่อ:

- แก้ logic หรือ architecture
- เพิ่ม/แก้ data
- เพิ่ม/แก้ test หรือ evaluation
- เปลี่ยน routing, retrieval, LLM หรือ runtime controls
- สร้าง handoff/report/tool
- พบ root cause หรือ blocker สำคัญ
- รัน benchmark/load test ที่มีผลต้องส่งต่อ session อื่น

ไม่จำเป็นต้องเขียนเมื่อ:

- ตอบคำถามสั้น ๆ โดยไม่แก้ไฟล์
- อธิบายแนวคิดทั่วไป
- ผู้ใช้ถามสถานะโดยไม่มีงานใหม่

---

## 6. Daily Log Template ที่ควรใช้

```md
# PSU Esports Daily Log - YYYY-MM-DD

## Latest Update - ชื่อหัวข้องาน

### สรุป

- วันนี้ทำอะไรและผลหลักคืออะไร

### ปัญหา / Root Cause

- อาการที่พบ
- สาเหตุจริงที่ตรวจพบ
- จุดใน flow ที่ทำให้เกิดปัญหา

### เพิ่มหรือแก้อะไรไปบ้าง

- Logic/data/config ที่เปลี่ยน
- Behavior ก่อนและหลังแก้

### เทคนิค/วิธีที่ใช้

- Candidate scoring / margin / guard / RAG / LLM / concurrency หรือเทคนิคที่เกี่ยวข้อง
- เหตุผลที่เลือกวิธีนี้

### ไฟล์หรือข้อมูลสำคัญ

- `path\to\important_file.py`
- `path\to\data.jsonl`

### ผลทดสอบ / ผลวัด

- Tests ที่เกี่ยวข้อง
- จำนวนผ่าน/ไม่ผ่าน
- Average/P95/Max latency ถ้าเกี่ยวข้อง
- LLM calls/timeout ถ้าเกี่ยวข้อง

### ข้อจำกัด / สิ่งที่ยังเหลือ

- สิ่งที่ยังไม่ได้ทำ
- ความเสี่ยงหรือเคสที่ยังไม่ครอบคลุม

### งานที่ควรทำต่อ

1. งานถัดไปที่สำคัญที่สุด
2. งานรองลงมา
```

---

## 7. หลักการเขียน Daily Log

- เขียนภาษาไทยให้เข้าใจง่าย
- สรุปล่าสุดต้องอยู่บนสุด
- บันทึกตัวเลขจริง ไม่เขียนว่าเร็วขึ้นโดยไม่มีผลวัดถ้ามีวิธีวัดได้
- แยกสิ่งที่ทำแล้วกับข้อเสนอที่ยังไม่ได้ทำ
- ระบุว่า test bank ใดถูกใช้ เพื่อไม่ให้เอาคะแนนคนละชุดมาเทียบตรง ๆ
- ถ้าไม่ได้รัน test หรือ full eval ให้เขียนตรง ๆ
- ถ้าใช้ข้อมูลจากผู้ใช้ ให้ระบุว่าเป็น user-confirmed data
- ถ้า source ยังไม่ยืนยัน ให้เขียนว่า pending/manual verify
- ไม่ใส่รหัสผ่าน token หรือข้อมูลส่วนตัวลง log
- ไม่ต้องบอกผู้ใช้ทุกครั้งว่าเขียน log แล้ว เว้นแต่ผู้ใช้ถาม

---

## 8. สิ่งที่ session ใหม่ต้องตอบหลังอ่านเอกสาร

ก่อนลงมือแก้ ให้สรุปกลับผู้ใช้แบบกระชับว่า:

1. เข้าใจระบบและ current flow อย่างไร
2. ข้อมูล/model/runtime controls ปัจจุบันคืออะไร
3. ปัญหาที่ยังเหลือคืออะไร
4. งานใดควรทำต่อเป็นอันดับแรก
5. จะตรวจความถูกต้องและผลกระทบอย่างไร

หลังจากผู้ใช้อนุมัติหรือสั่งให้ทำ ให้ลงมือจนจบ implementation, verification และ Daily Log ของงานนั้น

