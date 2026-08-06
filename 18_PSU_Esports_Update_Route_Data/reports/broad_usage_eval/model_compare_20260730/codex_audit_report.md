# Broad Usage Eval v1 - Codex Audit Report

วันที่รัน: 2026-07-30

## สรุปสั้น

- `tools/run_broad_usage_eval_v1.py` คือโค้ดตัวรัน eval
- `data/eval/broad_usage_eval_v1.jsonl` และ `data/eval/broad_usage_eval_v1.json` คือ bank 667 cases ที่สร้างและเก็บไว้แล้ว
- bank นี้เป็น broad behavior eval / regression bank ยังไม่ใช่ human-verified golden truth 100%
- รันครบ 4 รอบแล้ว: no-LLM, Qwen2.5, Qwen3, Typhoon
- ผลที่ดีที่สุดตอนนี้คือ no-LLM / deterministic core เพราะผ่าน 92.05% และเร็วสุด
- Qwen2.5 มีผลต่อ route จริง แต่ทำให้คะแนนรวมแย่ลงและช้าขึ้นมาก
- Qwen3 และ Typhoon ผลเหมือน no-LLM เพราะ LLM ไม่ได้เข้ามาเปลี่ยน final route จริงใน run นี้

## Run Matrix

| Run | Model | LLM enabled | Passed / Turns | Pass rate | Total wall time | Median turn | P95 turn | Max turn |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| 01 | none / deterministic | no | 625 / 679 | 92.05% | 108.150s | 0.0875s | 0.5641s | 5.4938s |
| 02 | qwen2.5:3b | yes | 613 / 679 | 90.28% | 422.456s | 0.1449s | 1.6133s | 19.8705s |
| 03 | qwen3:4b | yes | 625 / 679 | 92.05% | 121.022s | 0.0774s | 0.5583s | 11.0117s |
| 04 | supachai/llama-3-typhoon-v1.5:8b-instruct | yes | 625 / 679 | 92.05% | 121.213s | 0.0779s | 0.5566s | 10.8910s |

หมายเหตุ: ผู้ใช้เรียก Qwen3.5 แต่ในเครื่องมี `qwen3:4b` ไม่พบ tag Qwen3.5 ตรง ๆ จึงใช้ `qwen3:4b` แทนรอบ Qwen3

## LLM Impact

### No-LLM

- เสถียรสุดในรอบนี้
- ไม่มี LLM intent เข้ามาเปลี่ยน route
- ปัญหาที่เหลือเป็นปัญหา deterministic/router/structured tool จริง จึงเหมาะใช้เป็น baseline หลัก

### Qwen2.5:3b

- `universal_intent.method=llm` เกิด 301 turns จาก 679 turns
- route/mode เปลี่ยนจาก no-LLM 50 turns
- ช่วยแก้ fail ได้ 6 turns
- ทำให้เคสที่เดิมผ่านกลายเป็น fail 18 turns
- เวลารวมช้ากว่า no-LLM ประมาณ 3.9 เท่า
- สรุป: ยังไม่ควรเปิด intent LLM-first แบบกว้างใน production

ตัวอย่างที่ Qwen2.5 ช่วย:

- `PSU Staff เล่น PC ต้องเสียเงินไหม` จาก members/no-data กลับเป็น price ได้
- `เกมยิงมีอะไรบ้าง` จาก equipment กลับเป็น games catalog ได้
- `Nintendo Switch OLED คืออะไร` จากเกมผิด กลับเป็น equipment ได้
- `Nintendo Switch OLED อยู่โซนไหน` จากเกมผิด กลับเป็น equipment ได้

ตัวอย่างที่ Qwen2.5 ทำให้แย่ลง:

- `PUBG: BATTLEGROUNDS คือเกมอะไร` จาก game detail กลายเป็น clarification
- `Nintendo Switch Sports คือเกมอะไร` จาก game detail กลายเป็น equipment
- `Animal Crossing: New Horizons คือเกมอะไร` จาก game detail กลายเป็น clarification
- `Logitech G923 TRUEFORCE Racing Wheel คืออะไร` จาก equipment กลายเป็น no-answer
- `Sony PlayStation VR2 คืออะไร` จาก equipment กลายเป็น game control missing context
- `จองยังไง` จาก reservation กลายเป็น equipment/how_to route

### Qwen3:4b

- ผล pass/fail/mode/route เหมือน no-LLM แบบ 0 diff
- หลังรัน ตรวจ preflight แล้ว timeout ที่ 8 วินาที
- สรุป: ใน config นี้ไม่ได้ช่วย routing จริง และยังมีความเสี่ยงเรื่อง timeout

### Typhoon 1.5 8B

- ผล pass/fail/mode/route เหมือน no-LLM แบบ 0 diff
- หลังรัน ตรวจ preflight แล้ว timeout ที่ 8 วินาที
- สรุป: ยังไม่เหมาะเปิดเป็น intent/fallback หลักบนเครื่องนี้ ถ้าไม่เพิ่ม timeout หรือทำ queue/circuit breaker ให้ดี

## Codex Answer-Quality Audit

### 1. Wrong Route จาก keyword ชนกัน

พบหลายเคสที่คำถามมี keyword ที่ router ตีผิดหมวด:

- `PUBG: BATTLEGROUNDS เล่นได้ที่ไหน` ไป schedule เพราะคำว่า `ที่ไหน/เล่นได้` ถูกดึงไปเวลาเปิด-ปิด
- `เกมไหนเล่นได้หลายโซน` ไป schedule ทั้งที่ควรเป็น games aggregation
- `เกมยิงมีอะไรบ้าง` ไป equipment เพราะคำว่า `มีอะไรบ้าง` กว้างเกิน
- `Nintendo Switch Sports คือเกมอะไร` บางรอบไป equipment เพราะชนกับคำว่า Nintendo Switch

แนวแก้:

- เพิ่ม game-title-first guard ให้ชื่อเกมชนะ service/equipment/schedule เมื่อถาม `คืออะไร`, `เล่นได้ที่ไหน`, `แนวไหน`
- เพิ่ม genre query detector สำหรับ `เกมยิง`, `เกมแข่งรถ`, `เกมปาร์ตี้`
- ลดน้ำหนัก schedule เมื่อคำถามมีคำว่า `เกมไหน`, `เล่นได้หลายโซน`, หรือมี explicit game title

### 2. Equipment detail ยังไม่แน่น

หลายคำถามมีข้อมูลจริงใน `equipment_item_details.jsonl` แต่ตอบ no-answer หรือ greeting:

- `Gaming PC รุ่น MSI MAG Infinite S3 14th คืออะไร`
- `Gaming Monitor คืออะไร`
- `Gaming Keyboard คืออะไร`
- `Driving Force Shifter คืออะไร`
- `TV 65 นิ้ว คืออะไร`
- `Sofa 2 seats คืออะไร`

แนวแก้:

- ทำ equipment item alias index ให้เทียบ exact/fuzzy ก่อน general/no-answer
- เพิ่ม operation `equipment_detail_lookup` สำหรับคำถาม `คืออะไร`, `ใช้ทำอะไร`, `อยู่โซนไหน`
- กันคำว่า `hi` ใน `Shifter` ไม่ให้เข้า greeting path

### 3. Reservation policy บางคำถามโดน price/equipment/clarification แย่ง

ตัวอย่าง:

- `หลังจองต้องจ่ายภายในกี่นาที` ไป clarification ราคา
- `จ่ายเงินผ่านช่องทางไหน` ไป clarification ราคา
- `จองแล้วแก้ไขได้ไหม` บางรอบกลายเป็น equipment/how_to no-answer
- `walk in ได้ไหม` ยัง no-answer ซึ่งอาจถูกต้องถ้าไม่มีข้อมูลจริง แต่ควรตอบให้ชัดว่าไม่มีข้อมูล walk-in

แนวแก้:

- เพิ่ม reservation-policy priority ให้คำว่า `หลังจอง`, `จ่ายภายใน`, `ชำระ`, `แก้ไข`, `โอนสิทธิ์`, `walk in`
- แยก `ถามราคา` ออกจาก `ถามขั้นตอน/นโยบายการชำระเงิน`
- ถ้าไม่มีข้อมูล walk-in ให้ตอบ no-answer แบบเจาะจง ไม่ใช่ generic no-answer

### 4. Game controls edge cases

ตัวอย่าง:

- `Uncharted: Legacy of Thieves Collection ปุ่มมาร์กตำแหน่งศัตรูกดอะไร` ไป members เพราะคำว่า `ตำแหน่ง`
- คำถามปุ่มที่มีหลาย action ในประโยคเดียว เช่น `วิ่ง กระโดด และเหยียบศัตรู` ถูก split เป็น multi-question ทั้งที่ structured controls ตอบได้
- ชื่อ canonical บางอันทำให้ evaluator fail เช่น `Ragnarök` vs `Ragnarok`, `Super Smash Bros. Ultimate` vs `Super Smash Bros Ultimate`

แนวแก้:

- ถ้ามี explicit game title + `ปุ่ม/กดอะไร/control` ให้ game_controls ชนะ members
- เพิ่ม action phrase parser สำหรับหลาย action ในเกมเดียว
- ปรับ eval alias/canonical matching ไม่ให้ fail จาก punctuation/diacritics ที่ความหมายเดียวกัน

### 5. Members ยังมี edge case ชื่อคน/คำกว้าง

ตัวอย่าง:

- `แต่ละหมวดมีใครบ้าง` แบบไม่มีคำว่า สมาชิก ยัง no-answer
- `นางสาวชญาภา จันทร์เอิบ ทำตำแหน่งอะไร` กลายเป็น clarification เพราะชนกับคำว่าเวลา/ตำแหน่ง

แนวแก้:

- ถ้าคำถามมี `แต่ละหมวด/แต่ละกลุ่ม` และไม่มี domain อื่น ให้ลอง members group list
- ถ้ามีชื่อคนจาก member alias index ให้ members ชนะ ambiguity gate

### 6. LLM ไม่ควรถูกเปิดกว้างตอนนี้

Qwen2.5 ช่วยบางเคส แต่ทำให้ route regression มากกว่า โดยเฉพาะ:

- เกมชื่อชัด -> clarification
- เกม Nintendo -> equipment
- reservation -> equipment/how_to
- equipment -> controls/no-answer

แนวที่ควรใช้:

- LLM ใช้เฉพาะ margin ต่ำหรือ route สูสีจริง
- ห้าม LLM override explicit entity ที่ deterministic เจอแล้ว เช่น game title, equipment item, service name
- ถ้า LLM intent confidence ไม่สูงพอ ต้อง keep heuristic route
- เพิ่ม cross-check: LLM route ต้องผ่าน answer-type contract ก่อนเปลี่ยน route

## Recommendation

ลำดับแก้ที่ควรทำต่อ:

1. แก้ wrong route ที่ไม่ต้องใช้ LLM ก่อน: game title first, equipment item detail, reservation policy
2. ปรับ broad eval expected/canonical บางจุดที่เป็น false fail จากชื่อสะกดต่างกัน
3. ทำ LLM gate ให้แคบลง ไม่ให้ Qwen2.5 override route ที่ deterministic มี entity ชัด
4. ค่อยรัน model compare ใหม่
5. ยังไม่ควรใช้ Qwen3/Typhoon เป็น production fallback บนเครื่องนี้จนกว่าจะแก้ timeout/queue/preflight

## Files

- Bank JSONL: `data/eval/broad_usage_eval_v1.jsonl`
- Bank JSON: `data/eval/broad_usage_eval_v1.json`
- No LLM: `reports/broad_usage_eval/model_compare_20260730/01_no_llm`
- Qwen2.5: `reports/broad_usage_eval/model_compare_20260730/02_qwen25_3b`
- Qwen3: `reports/broad_usage_eval/model_compare_20260730/03_qwen3_4b`
- Typhoon: `reports/broad_usage_eval/model_compare_20260730/04_typhoon15_8b`
