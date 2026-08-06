# สรุป Eval ใหญ่หลังแก้ Regression - PSU Esports Chatbot

วันที่รัน: เริ่ม 2026-07-31, จบ 2026-08-01 00:12  
ชุดคำถาม: `data/eval/model_benchmark_1500.jsonl` จำนวน 1,600 cases  
ผลดิบ: `reports/model_benchmark/20260731_full_after_regression_cleanup`

## สรุปสั้น

ผลหลังแก้ regression ดีขึ้นชัดในส่วนข้อมูล PSU จริงครับ ถ้าไม่นับคำถาม `general_llm` ระบบตอบ PSU-domain ได้ประมาณ 98%+ แล้ว

แต่ถ้าวัดรวมทุกอย่าง คะแนนจะถูกลากลงโดยกลุ่ม general fallback และบาง keyword false positive เช่น `ประชาสัมพันธ์` ถูกมองเป็นตำแหน่งทีมแทนการเขียนประโยคประชาสัมพันธ์

ตัวที่เหมาะสุดตอนนี้ยังเป็น `scb10x/typhoon2.5-qwen3-4b` เพราะ avg score สูงสุด และ latency ดีกว่า `qwen2.5:7b` มาก แม้ pass rate ดิบจะน้อยกว่า `qwen2.5:7b` เล็กน้อย

## โมเดลที่รัน

1. No-LLM baseline
2. `qwen3:4b`
3. `qwen2.5:7b`
4. `scb10x/llama3.2-typhoon2-3b-instruct`
5. `scb10x/typhoon2.5-qwen3-4b`

หมายเหตุ: runner เลือกตามลำดับใน config เดิม จึงรัน `qwen2.5:7b` ก่อน Typhoon แม้ตอนวางแผนจะพูดถึง Typhoon ก่อน

## Ranking รวม 1,600 cases

| อันดับ | Run | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | `scb10x/typhoon2.5-qwen3-4b` | 94.75% | 98.61 | 2.3089 | 12.5265 | 262.9887 | 454 |
| 2 | `scb10x/llama3.2-typhoon2-3b-instruct` | 94.62% | 98.59 | 2.3342 | 13.0106 | 263.3470 | 454 |
| 3 | `qwen2.5:7b` | 94.94% | 98.27 | 3.3979 | 18.4911 | 232.3512 | 454 |
| 4 | No-LLM | 81.19% | 96.45 | 0.8310 | 4.1635 | 269.6652 | 215 |
| 5 | `qwen3:4b` | 82.44% | 93.27 | 1.0368 | 5.0101 | 277.6614 | 453 |

## แยกเฉพาะ PSU-domain ไม่รวม general

| Run | Cases | Pass rate | Avg score | Avg sec |
|---|---:|---:|---:|---:|
| No-LLM | 1,321 | 98.33% | 99.67 | 0.559 |
| `qwen3:4b` | 1,321 | 98.33% | 99.67 | 0.692 |
| `scb10x/typhoon2.5-qwen3-4b` | 1,321 | 98.26% | 99.65 | 1.078 |
| `qwen2.5:7b` | 1,321 | 98.11% | 99.63 | 1.325 |
| `scb10x/llama3.2-typhoon2-3b-instruct` | 1,321 | 98.03% | 99.62 | 1.094 |

สรุป: ส่วน core chatbot ของ PSU ตอนนี้ดีขึ้นจริง ส่วนใหญ่ตอบด้วย structured/fast/RAG ก่อนถึง LLM

## แยกเฉพาะ general fallback

| Run | Cases | Pass rate | Avg score | Avg sec |
|---|---:|---:|---:|---:|
| `qwen2.5:7b` | 279 | 79.93% | 91.83 | 13.212 |
| `scb10x/llama3.2-typhoon2-3b-instruct` | 279 | 78.49% | 93.71 | 8.206 |
| `scb10x/typhoon2.5-qwen3-4b` | 279 | 78.14% | 93.69 | 8.137 |
| `qwen3:4b` | 279 | 7.17% | 62.98 | 2.667 |
| No-LLM | 279 | 0.00% | 81.19 | 2.120 |

สรุป: `qwen3:4b` ในรอบนี้เจอ `general_llm_unavailable` เยอะมาก จึงไม่ควรเลือกเป็น default ตอนนี้ ถึงแม้บางรอบก่อนจะดูดี

## สิ่งที่ดีขึ้นหลังแก้ regression

1. Machine-specific availability ผ่านแล้ว
   - PC #01-#02 กับ PC #03-#10 แยก Tekken 8 / Call of Duty: Warzone ถูก
   - กลุ่ม `availability_machine_split` ได้ 100% ใน Typhoon 4B

2. เกม/ปุ่มส่วนใหญ่เสถียรมาก
   - `game_controls` 343 cases ได้ประมาณ 98.83%
   - เกมที่ไม่มีใน catalog ปัจจุบันไม่ถูกเอาปุ่มเกมอื่นมาตอบแทน

3. ราคาเสถียรที่สุด
   - `service_fee` 258 cases ได้ 100% ทุก run
   - ใช้ deterministic calculator ถูกทาง

4. กติกาแข่งขันเสถียร
   - `competition_rules` 75 cases ได้ 100% หรือเกือบ 100%

5. สมาชิกทีมเสถียร
   - `members` 63 cases ได้ 100%

## ปัญหาที่เจอจริงจาก Eval ใหญ่

### P0 - General fallback ยังถูก route แย่งเพราะ keyword

ตัวอย่าง:

- `เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค`
- ระบบตอบเป็นสมาชิกตำแหน่ง `ประชาสัมพันธ์`

สาเหตุ:

- keyword `ประชาสัมพันธ์` ถูก match เป็น role ของทีมงาน
- router ไม่แยกว่าผู้ใช้ต้องการ "เขียนข้อความประชาสัมพันธ์" ไม่ใช่ "ถามว่าใครเป็นประชาสัมพันธ์"

วิธีแก้:

- เพิ่ม intent guard สำหรับคำกริยาเชิง generation เช่น `เขียน`, `แต่ง`, `ช่วยเขียน`, `ประโยค`, `caption`
- ถ้าเจอ generation intent ให้ส่ง general LLM หรือถาม scope แทน ไม่เข้า members role lookup ทันที

### P0 - LLM health / unavailable ยังทำให้ qwen3:4b คะแนนตก

ตัวอย่าง:

- `qwen3:4b` มี `llm_required_but_unavailable` 216 เคส

สาเหตุที่เป็นไปได้:

- health manager/circuit breaker ปิด LLM หลัง timeout/empty response บางช่วง
- `qwen3:4b` อาจยังมีพฤติกรรม thinking/empty/timeout แม้ตั้ง `PSU_OLLAMA_THINK=false`
- general fallback ถูกยิงต่อเนื่องท้ายชุด ทำให้ model/server หน่วง

วิธีแก้:

- แยก benchmark สำหรับ general LLM แบบไม่ผ่าน pipeline เพื่อวัด raw model ก่อน
- log reason ของ `general_llm_unavailable` ให้ละเอียดกว่าเดิม เช่น timeout, empty, circuit-open, connection error
- เพิ่ม per-model warmup + reset health state ก่อนเข้า general batch

### P1 - Equipment บางคำถูกมองเป็น game controls

ตัวอย่าง:

- `Sony PlayStation VR2 คืออะไร`
- `Sony PlayStation VR2 ใช้ทำอะไร`

ระบบตอบถามกลับว่าไม่รู้เกมไหน แทนที่จะตอบว่าเป็นอุปกรณ์ VR

สาเหตุ:

- คำว่า `VR2` ไปกระตุ้น path ที่เกี่ยวกับเกม/ปุ่ม/VR
- equipment entity ยังไม่ชนะ game control ambiguity

วิธีแก้:

- เพิ่ม equipment aliases เช่น `PlayStation VR2`, `PS VR2`, `Sony PlayStation VR2`
- เพิ่ม operation-first สำหรับ `คืออะไร`, `ใช้ทำอะไร` + equipment entity
- negative guard: ถ้า target เป็นอุปกรณ์ชัด ห้ามเข้า control missing game

### P1 - Booking by game ของเกม VR ยังตอบกว้างเกิน

ตัวอย่าง:

- `ถ้าจะเล่น Beat Saber ต้องจองอะไร`
- `ถ้าจะเล่น Horizon Call of the Mountain ต้องจองอะไร`

ระบบตอบแค่ต้องจองล่วงหน้าผ่านระบบออนไลน์ แต่ควรตอบว่าเกี่ยวกับ `VR Station` ด้วย

วิธีแก้:

- เพิ่ม booking-by-game resolver สำหรับทุกเกม ไม่ใช่เฉพาะ Call of Duty
- ใช้ `service_game_availability.jsonl` map game -> service/machine
- ถ้าเกมอยู่หลาย service ให้ถามกลับหรือแสดงตัวเลือก

### P1 - Compound บางเคสถูกตอบแค่ครึ่งเดียว

ตัวอย่าง:

- `TEKKEN 8 เล่นที่ไหน แล้ว Resident Evil Village ปุ่มอะไร`
- ระบบตอบเฉพาะปุ่ม Resident Evil Village ไม่ตอบว่า TEKKEN 8 เล่นที่ไหน

สาเหตุ:

- splitter/structured path บางเคสเลือก game_controls ก่อน แล้วไม่แตกเป็น 2 subquestion
- คำว่า `แล้ว` กับ game title หลายตัวควรบังคับเข้า multi-question

วิธีแก้:

- เพิ่ม compound detector จากจำนวน game entities >= 2 และ operation >= 2
- ถ้ามี pattern `เกม A เล่นที่ไหน แล้ว เกม B ปุ่มอะไร` ต้อง split เสมอ

### P1 - Control phrase บางอันโดน split ผิด

ตัวอย่าง:

- `Beat Saber ถ้าจะหลบและจัดตำแหน่งร่างกายต้องกดอะไร`
- ระบบแตกเป็นหลายคำถาม เพราะเห็น `และ`

สาเหตุ:

- compound splitter ใช้คำเชื่อม `และ` กว้างเกิน
- บางคำเชื่อมเป็นส่วนหนึ่งของ action เดียว ไม่ใช่คนละคำถาม

วิธีแก้:

- เพิ่ม same-intent action phrase whitelist สำหรับ control เช่น `หลบและจัดตำแหน่งร่างกาย`, `วิ่ง กระโดด และเหยียบศัตรู`
- ถ้ามี game เดียว + operation เดียว ให้ไม่ split แม้มี `และ`

### P2 - Schedule wording ผ่าน logic แต่ไม่ผ่าน expected text บางเคส

ตัวอย่าง:

- `ช่วงเช้าวันจันทร์เปิดไหม`
- ระบบตอบว่า `เล่นไม่ได้ เพราะเป็น Maintenance`
- expected อยากเห็นคำว่า `เปิด` หรือ `ปิด`

สาเหตุ:

- คำตอบถูกเชิงข้อมูล แต่ wording ไม่ตรง answer contract

วิธีแก้:

- ปรับ schedule answer ให้ใส่คำว่า `ปิด/ไม่เปิดให้จอง` ชัดเจนเมื่อเป็น maintenance

### P2 - Eval data ยังมี stale/contract issue บางส่วน

ตัวอย่าง:

- `Mario Kart Live ถ้าจะเลี้ยวต้องกดอะไร`
- ระบบตอบว่าไม่อยู่ใน catalog ปัจจุบัน ซึ่งถูกตามข้อมูลปัจจุบัน แต่ eval ยัง expected ปุ่ม `Left Stick`

วิธีแก้:

- แยก eval case เป็น `current_catalog` กับ `legacy_control_reference`
- ถ้าเกมไม่อยู่ catalog ปัจจุบัน ห้าม expected ให้ตอบปุ่มเหมือนเกมยังให้บริการ

## สรุปเลือกโมเดล

แนะนำ default ตอนนี้:

1. `scb10x/typhoon2.5-qwen3-4b`
   - avg score รวมสูงสุด
   - latency ดีกว่า `qwen2.5:7b`
   - general fallback ใช้ได้พอสมควร

ตัวสำรอง:

2. `scb10x/llama3.2-typhoon2-3b-instruct`
   - คะแนนใกล้มาก
   - เบากว่า
   - เหมาะถ้าต้องการลดภาระเครื่อง

ยังไม่แนะนำเป็น default:

3. `qwen3:4b`
   - รอบนี้ general fallback ล้มเยอะจาก `general_llm_unavailable`
   - ต้องแก้ health/circuit-breaker หรือวิธีเรียกก่อน

4. `qwen2.5:7b`
   - pass rate ดิบสูงสุดเล็กน้อย
   - แต่ p95 18.49 วิ ใกล้ timeout 20 วิเกินไปสำหรับใช้งานจริง

## งานที่ควรทำต่อ

1. แก้ generation intent guard สำหรับคำว่า `เขียน/แต่ง/ประโยค/ประชาสัมพันธ์`
2. แก้ equipment guard สำหรับ `Sony PlayStation VR2` และคำถาม `คืออะไร/ใช้ทำอะไร`
3. เพิ่ม booking-by-game resolver จาก game -> service/machine
4. ปรับ compound detector ให้ split เมื่อมีหลาย game + หลาย operation
5. ปรับ control splitter ไม่ให้แตก action phrase ภายในเกมเดียว
6. เพิ่ม schedule wording contract ให้มี `ปิด/ไม่เปิดให้จอง` ชัดเจน
7. แยก eval stale cases ออกจาก current catalog cases
8. เพิ่ม log reason ของ LLM unavailable ให้ชัดกว่าเดิม

