# Agent State Transfer Full

ไฟล์นี้ตั้งใจให้ AI/Codex ตัวใหม่อ่านแล้วเหมือนอยู่ในแชทเดิมมากที่สุด ไม่ใช่แค่รู้ path แต่รู้เจตนา วิธีคิด ข้อห้าม สิ่งที่ผู้ใช้ชอบ/ไม่ชอบ และสถานะเทคนิคปัจจุบัน

## 1. ผู้ใช้ต้องการอะไรจริง ๆ

ผู้ใช้กำลังทำโปรเจกต์ฝึกงาน/โปรเจกต์จริงเกี่ยวกับ AI Chatbot สำหรับ PSU Esports Studio - Phuket

สิ่งที่ผู้ใช้ต้องการ:

- อยากได้ระบบที่ใช้จริงได้ ไม่ใช่แค่ demo สวย ๆ
- อยากเข้าใจว่า AI/RAG/LLM ทำงานยังไง
- อยากทำแบบ local/free เป็นหลัก
- อยากให้คำตอบเร็ว ไม่เกินประมาณ 10 วินาที ถ้าต้องใช้ RAG/LLM แต่ถ้า rulebase ทำได้หลัก ms ยิ่งดี
- อยากให้ตอบถูก ตรงคำถาม ไม่เวิ่นเว้อ
- อยากให้มีหลักฐาน/แหล่งข้อมูล
- อยากให้มี log/report เพื่อใช้ทำรายงานฝึกงาน
- อยากให้เอาไป deploy ได้
- อยากให้แยกข้อมูล/โค้ด/ทดสอบเป็นระเบียบ
- อยากให้แชทใหม่ทำต่อได้โดยไม่ต้องไล่อ่าน conversation เก่า

สิ่งที่ผู้ใช้ไม่ชอบ:

- คำตอบที่ดูมั่วหรือดึงข้อมูลคนละเรื่องมาตอบ
- คำตอบที่ตอบรายละเอียดก่อนประเด็นหลัก
- rulebase ที่ fix เกินไปจนถามคนละคำแล้วตอบไม่ได้
- test ที่บอก PASS ทั้งที่คำตอบจริงผิด
- คำตอบที่อ้างว่าไม่มีข้อมูล ทั้งที่ข้อมูลมีแต่ระบบหาไม่เจอ
- การบอกว่าใช้ LLM/RAG ทั้งที่จริงใช้ rulebase โดยไม่อธิบาย
- การทำ human review UI ที่ repetitive มากเกินและไม่ช่วยงานตอนนั้น

## 2. บุคลิกการทำงานที่ควรใช้กับผู้ใช้

ควรตอบเป็นภาษาไทยแบบตรงไปตรงมาและช่วยลงมือทำจริง

ควร:

- อธิบายให้เห็นภาพ
- สรุปเป็น bullet/หัวข้อเมื่อข้อมูลเยอะ
- ถ้าแก้โค้ด ให้แก้จริงและรันทดสอบ
- ถ้ารันนาน ให้เก็บ stdout ลงไฟล์เพื่อลด token
- บอก path ไฟล์ชัดเจน
- แยกสิ่งที่ทำแล้ว/ยังไม่ได้ทำ/ควรทำต่อ
- ถ้าคำถามเกี่ยวกับคุณภาพคำตอบ ให้ดูจาก output จริง ไม่ใช่แค่ตัวตรวจ

ไม่ควร:

- ตอบแค่ทฤษฎีโดยไม่ทำไฟล์เมื่อผู้ใช้ขอให้ทำ
- บอกว่า “น่าจะ” มากเกินโดยไม่ตรวจไฟล์
- แก้แบบกว้างจนพัง regression
- ปรับให้ตัวตรวจผ่านแบบผ่อนผัน
- ให้ LLM เดาข้อมูลที่ไม่มี

## 3. สถานะโปรเจกต์ล่าสุดแบบ snapshot

เวลาสรุป: 2026-07-05

Root:

```text
C:\Users\Chokhun\Downloads\Learn-LLM
```

Main source:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data
```

Deploy source:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy
```

Handoff:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\21_PSU_Esports_Handoff_Summary_20260705
```

Production:

```text
https://psu-esports-chatbot.vercel.app
```

Latest confirmed regression:

```text
GT360 = 360/360 PASS
Competition challenger v2 = 369/369 PASS
Total major regression = 729/729 PASS
```

Latest important fix:

```text
equipment_game_catalog route
```

## 4. ความจริงเรื่อง AI/LLM ในระบบนี้

ตอนนี้ production ไม่ใช่ LLM chatbot เต็มรูปแบบ

มันคือ:

```text
rulebase + deterministic calculator + fact cards + curated RAG-lite + guard/no-answer
```

ผู้ใช้เคยถามหลายครั้งว่า “อันนี้ใช้ RAG ใช่ไหม / LLM ใช่ไหม / ทำไมเร็วมาก”

คำตอบที่ควรยืนยัน:

- ถ้า mode เป็น `pipeline:*_fast_path` ส่วนใหญ่ไม่ใช้ LLM
- ถ้า mode เป็น `pipeline:deterministic_calculator_fast` คือ calculator
- ถ้า mode เป็น `pipeline:competition_fact_card` คือ fact card
- ถ้า mode เป็น `pipeline:rag_direct_curated` คือ curated RAG-lite/lexical retrieval ไม่ใช่ LLM local
- Production บน Vercel ไม่ได้รัน Qwen/Ollama
- Qwen อยู่ในโฟลเดอร์ทดลอง `19`

เหตุผล:

- ฟรี
- เร็ว
- คุมคำตอบได้
- deploy บน Vercel ได้

## 5. User-facing answer policy ที่สำคัญที่สุด

ผู้ใช้ย้ำหลายครั้งว่า:

```text
ตอบสิ่งที่ถามก่อน แล้วค่อยรายละเอียด/แหล่งข้อมูล
```

ตัวอย่างผิด:

```text
ถาม: วันจันทร์ morning เล่นได้ไหม afternoon เปิดไหม
ตอบ: ไม่ได้เปิด 24 ชั่วโมง...
```

เพราะผู้ใช้ไม่ได้ถาม 24 ชั่วโมง

ตัวอย่างถูก:

```text
วันจันทร์ช่วงเช้า 09:00-12:00 เล่นไม่ได้ เพราะเป็น Maintenance
ช่วงบ่าย 13:00-16:00 เปิดให้บริการ
```

แล้วค่อยเสริมรายละเอียด

## 6. Price answer policy

ราคาต้องตอบราคาเด่นก่อน

ตัวอย่าง:

```text
เด็ก สจล เล่น VR 30 นาทีเท่าไหร่
```

ควรตอบ:

```text
ราคา: 190 บาทต่อ 30 นาที สำหรับนักศึกษาหรือนักเรียนต่างสถาบัน / General Student
```

แล้วค่อยรายละเอียด:

- PSU Student and Staff: 0 บาท
- PSU Alumni and General Student: 190 บาท
- General Adult: 525 บาท

ถ้าผู้ใช้ไม่ระบุกลุ่ม:

```text
ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน
```

แต่ต้องไม่ใช้ประโยคนี้เมื่อคำถามระบุกลุ่มชัดแล้ว เช่น `เด็ก สจล`, `เด็กจุฬา`, `ต่างมหาลัย`

## 7. Schedule answer policy

ต้องแยกวันและช่วงเวลาให้ชัด:

- Monday morning: Maintenance, เล่นไม่ได้
- Monday afternoon: Open, 13:00-16:00
- Tuesday-Thursday: เปิด morning/afternoon ปกติ
- Friday morning: เปิด
- Friday afternoon: Maintenance สำหรับ weekly hardware inspection and cleaning

ถ้าถาม generic เช่น:

```text
รอบเช้า 09 ถึง 12 ใช่ไหม
```

ควรตอบรวม:

- Morning 09:00-12:00
- Afternoon 13:00-16:00
- วันจันทร์เช้า maintenance
- วันศุกร์บ่าย maintenance
- ถ้ามีวันปิดพิเศษให้ดู closure ด้วย

## 8. Game/equipment policy

ถ้าถาม:

```text
อุปกรณ์เล่นเกมอะไรได้บ้าง
```

ต้องตอบรายการเกมตามโซน ไม่ใช่บอกไม่พบ `เกมนี้`

ถ้าถาม:

```text
PC Zone มีอุปกรณ์อะไรบ้าง
```

ต้องตอบอุปกรณ์ ไม่ใช่รายการเกมอย่างเดียว

ถ้าถาม:

```text
เล่น Minecraft ได้ไหม
```

เพราะ Minecraft ไม่อยู่ใน list ที่ยืนยันได้ ต้องตอบ:

```text
ยังไม่พบ Minecraft ในรายการเกมที่ยืนยันได้...
```

แล้วแสดง list เกมที่มีจริง

## 9. Competition rule policy

ถ้าถามกติกา:

```text
Tekken 8 เกมนึงมี 3 rounds ใช่ไหม
```

ต้องเข้า `competition_rules`, ไม่ใช่ `games/game_availability_lookup`

คำที่ต้องระวัง:

- round
- rounds
- รอบ
- decider
- เกมตัดสิน
- FT2
- R3
- 1v1
- 1 ต่อ 1
- pause
- timeout
- map
- ทีม
- สมาชิก
- ตัวจริง
- ตัวสำรอง

คำถามกติกาควรตอบ:

```text
คำตอบ: ...

หลักฐานจากกติกา:
- ...

อ้างอิงจากกติกา: ...
แหล่งข้อมูล: ...
```

## 10. No-answer policy

ถ้าไม่มีข้อมูลจริง:

```text
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ
```

ถ้ารู้หมวด:

```text
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด penalty ตอนนี้ครับ
```

อย่าตอบเหมือนมีข้อมูลถ้าไม่มี

## 11. วิธีทำงานเมื่อผู้ใช้บอก “มันตอบผิด”

ให้ทำตามนี้:

1. เอาคำถามจริงไปถาม pipeline
2. ดู route/mode/source
3. ดูว่า data มีไหม
4. ดูว่าผิดเพราะ:
   - route ผิด
   - data ไม่มี
   - data มีแต่ retrieval ไม่เจอ
   - fact card ผิด
   - formatter ตอบไม่ดี
   - validator ไม่จับ
   - ground truth ผ่อนเกิน
5. แก้เฉพาะจุด
6. เพิ่ม ad-hoc question
7. รัน regression
8. บันทึก report/log
9. ถ้า production ต้อง sync ไป deploy folder และ deploy ใหม่

## 12. Golden path หลังแก้ code

ทุกครั้งที่แก้ `app/runtime/fast_answer.py`, `app/pipeline/router.py`, `app/pipeline/engine.py`:

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data"
py -3 -m py_compile app\runtime\fast_answer.py app\pipeline\router.py app\pipeline\engine.py
py -3 tools\validate_update.py
py -3 tools\run_ad_hoc_pipeline_log.py --label <label> --questions-file <file>
py -3 tools\run_ground_truth_pipeline_eval.py --label <label_gt360> *> reports\run_stdout_<label_gt360>.txt
py -3 tools\run_ground_truth_pipeline_eval.py --ground-truth data\ground_truth\competition_challenger_v2\ground_truth_competition_challenger_v2_real_competitor_questions.jsonl --label <label_comp> *> reports\run_stdout_<label_comp>.txt
```

ถ้า deploy:

```powershell
sync 18 -> 20
compile deploy folder
vercel deploy --prod --yes
test production /api/chat
```

## 13. Current main limitations

ยังไม่รองรับดี:

- หลายคำถามใน input เดียว
- conversation memory จริง
- Facebook Messenger integration
- booking action จริง
- API booking/payment/check slot
- admin UI สำหรับ update data
- LLM fallback production
- vector DB production
- automatic Thai holiday API

## 14. What the next agent should do if asked to continue

ถ้าผู้ใช้บอกให้ “ทำต่อ” โดยไม่ระบุ:

แนะนำถามหรือเสนอ:

1. ทำ multi-question splitter
2. ทำ session memory
3. เพิ่ม unanswered log analyzer
4. ทำ admin update flow
5. เชื่อม Facebook webhook
6. ทำ Dockerfile
7. ทดลอง RAG/LLM fallback จากโฟลเดอร์ 19

แต่ถ้าผู้ใช้ให้ปัญหาคำตอบเฉพาะ ให้แก้ปัญหานั้นก่อน

## 15. Absolute must-not-break behavior

ห้ามทำให้สิ่งเหล่านี้พัง:

- GT360 ต้องยังผ่าน
- Competition challenger v2 ต้องยังผ่าน หรือถ้า fail ต้องอธิบายว่าทำไม
- ราคาเด็ก มอ/นักศึกษา PSU ต้องฟรีตาม service fee
- นักศึกษาต่างมหาวิทยาลัยต้องเป็น General Student ไม่ใช่บุคคลทั่วไป
- unknown game ต้องไม่ดึง schedule/competition มั่ว
- คำถาม equipment game catalog ต้องไม่ตอบ `เกมนี้`
- คำถามกติกา Tekken round/decider ต้องเข้า competition rules
- คำถามวันศุกร์ต้องแยกเช้า/บ่าย ไม่ตอบรวมจนเข้าใจผิด
- ถ้าไม่มีข้อมูล penalty จริง ต้องตอบไม่พบข้อมูล ไม่แต่งค่าปรับเอง

