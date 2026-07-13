# Next Chat Reading Instructions

ไฟล์นี้ทำไว้ให้เอาไปใส่ในแชทใหม่เพียงไฟล์เดียวก่อน เพื่อบอก AI/Codex ตัวใหม่ว่าควรอ่านอะไรต่อจาก path ไหน โดยไม่ต้องอ่าน handoff ทั้งโฟลเดอร์ตั้งแต่แรก

## คำสั่งสำหรับ AI/Codex ตัวใหม่

คุณกำลังรับช่วงโปรเจกต์ PSU Esports Chatbot ต่อจากแชทเดิม

โปรเจกต์นี้อยู่บนเครื่อง Windows ของผู้ใช้ และไฟล์ทั้งหมดอยู่ใน:

```text
C:\Users\Chokhun\Downloads\Learn-LLM
```

กรุณาอ่านไฟล์ตามลำดับด้านล่างก่อนเริ่มทำงาน ถ้าคุณเข้าถึงไฟล์ในเครื่องได้ ให้เปิดอ่านจาก path โดยตรง ถ้าเข้าถึงไม่ได้ ให้ขอให้ผู้ใช้ paste ไฟล์ที่จำเป็นทีละไฟล์

## อ่านขั้นต่ำสุดก่อนตอบ

อ่านไฟล์นี้ก่อน:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\21_PSU_Esports_Handoff_Summary_20260705\17_IF_NEXT_AGENT_ONLY_READS_ONE_FILE.md
```

ไฟล์นี้คือสรุปฉุกเฉินแบบสั้นที่สุด มีข้อมูล:

- โปรเจกต์คืออะไร
- path หลัก
- production URL
- ระบบตอบด้วยอะไร
- test ล่าสุด
- สิ่งที่ห้ามทำให้พัง
- command หลัก

ถ้าอ่านได้แค่ไฟล์เดียว ให้อ่านไฟล์นี้พอ แล้วค่อยถามผู้ใช้ต่อเมื่อจำเป็น

## อ่านเพิ่มเพื่อรับช่วงให้เหมือนอยู่แชทเดิม

หลังอ่านไฟล์ขั้นต่ำแล้ว ให้อ่านไฟล์นี้:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\21_PSU_Esports_Handoff_Summary_20260705\11_AGENT_STATE_TRANSFER_FULL.md
```

ไฟล์นี้สำคัญที่สุดสำหรับการรับช่วง เพราะมี:

- ความต้องการจริงของผู้ใช้
- สิ่งที่ผู้ใช้ชอบ/ไม่ชอบ
- answer policy
- price policy
- schedule policy
- game/equipment policy
- competition rule policy
- no-answer policy
- golden path หลังแก้โค้ด
- สิ่งที่ต้องรักษาไม่ให้พัง

## ถ้าจะทำงานกับโค้ด

อ่านไฟล์นี้:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\21_PSU_Esports_Handoff_Summary_20260705\12_CHANGED_FILES_AND_CODE_INDEX.md
```

ไฟล์นี้บอกว่าโค้ดสำคัญอยู่ตรงไหน เช่น:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\app\runtime\fast_answer.py
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\app\pipeline\router.py
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\app\pipeline\engine.py
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\app\pipeline\retrieval.py
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\app\pipeline\validator.py
```

ใช้ไฟล์นี้เมื่อผู้ใช้ขอ:

- แก้คำตอบผิด
- แก้ route
- เพิ่ม rulebase
- เพิ่มข้อมูลเกม/อุปกรณ์
- แก้ราคา
- แก้ schedule
- แก้ competition rules

## ถ้าจะรันคำสั่ง ทดสอบ หรือ Deploy

อ่านไฟล์นี้:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\21_PSU_Esports_Handoff_Summary_20260705\13_COMMAND_CHEATSHEET.md
```

ไฟล์นี้มีคำสั่ง:

- ตั้ง UTF-8 สำหรับภาษาไทย
- compile
- validate
- run local server
- test local API
- run ad-hoc
- run GT360
- run competition challenger
- sync folder 18 ไป 20
- deploy Vercel
- test production API

## ถ้าจะแก้คำตอบหรือเช็คคุณภาพ

อ่านไฟล์นี้:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\21_PSU_Esports_Handoff_Summary_20260705\14_SMOKE_TEST_QUESTIONS.md
```

ไฟล์นี้มีชุดคำถามที่ควรลองหลังแก้ระบบ เช่น:

- schedule
- service fee
- booking
- rules/penalty
- equipment
- equipment game catalog
- game availability
- competition list
- competition rules
- no-answer

## ถ้าต้องเข้าใจว่า “งานเสร็จจริง” ต้องผ่านอะไร

อ่านไฟล์นี้:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\21_PSU_Esports_Handoff_Summary_20260705\15_REQUIREMENTS_AND_ACCEPTANCE_CRITERIA.md
```

ไฟล์นี้มี:

- functional requirements
- non-functional requirements
- definition of done
- quality gates
- failure severity
- review rubric

## ถ้าจะทำอะไรที่เสี่ยง หรือแก้ logic ใหญ่

อ่านไฟล์นี้ก่อน:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\21_PSU_Esports_Handoff_Summary_20260705\16_DO_NOT_DO_AND_RISK_REGISTER.md
```

ไฟล์นี้มีข้อห้าม เช่น:

- อย่าให้ LLM เดาข้อมูลสำคัญ
- อย่าแก้ตัวตรวจให้ผ่านง่ายขึ้น
- อย่า deploy ก่อน test
- อย่าเอา model ใหญ่ขึ้น Vercel
- อย่า revert งานเดิมของผู้ใช้
- อย่าเชื่อ keyword PASS อย่างเดียว

## ถ้าต้องการภาพรวมแบบละเอียดทั้งหมด

อ่านไฟล์รวม:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\21_PSU_Esports_Handoff_Summary_20260705\10_ALL_IN_ONE_HANDOFF.md
```

หรืออ่านไฟล์หลักทั้งหมดในโฟลเดอร์:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\21_PSU_Esports_Handoff_Summary_20260705
```

## Path โปรเจกต์หลัก

โฟลเดอร์ source หลัก:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data
```

โฟลเดอร์ deploy Vercel:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy
```

โฟลเดอร์ daily logs:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\17_PSU_Esports_Daily_Logs
```

โฟลเดอร์ทดลอง Qwen/Hybrid RAG:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\19_PSU_Esports_Qwen35_Hybrid_RAG
```

## สถานะล่าสุดที่ต้องรู้

Production URL:

```text
https://psu-esports-chatbot.vercel.app
```

Local web/API:

```text
http://127.0.0.1:8018/
POST http://127.0.0.1:8018/api/chat
GET  http://127.0.0.1:8018/health
```

Notebook test หลัก:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\notebooks\02_test_final_pipeline.ipynb
```

ระบบ production ตอนนี้ไม่ได้ใช้ LLM เป็นหลัก แต่ใช้:

```text
rulebase + deterministic calculator + competition fact cards + curated RAG-lite + guard/no-answer
```

ผล test ล่าสุด:

```text
GT360: 360/360 PASS
Competition challenger v2: 369/369 PASS
รวม regression หลัก: 729/729 PASS
```

## สิ่งที่เพิ่งแก้ล่าสุด

ปัญหาล่าสุดคือคำถามแนว:

```text
อุปกรณ์เล่นเกมอะไรได้บ้าง
Cockpit มีเกมอะไรบ้าง
VR มีเกมอะไรบ้าง
เล่น Minecraft ได้ไหม
Roblox เล่นได้ไหม
ตอนนี้มีเกมแข่งอะไรบ้าง
```

เคยตอบผิด เช่น:

```text
ยังไม่พบ เกมนี้ ในรายการเกมที่ยืนยันได้
```

หรือดึง schedule/competition rule คนละเรื่องมาตอบ

แก้แล้วโดยเพิ่ม route:

```text
equipment_game_catalog
pipeline:equipment_game_catalog_fast_path
```

และ production API ทดสอบแล้วตอบถูก

## วิธีทำงานเมื่อผู้ใช้บอกว่าคำตอบผิด

ให้ทำตามนี้:

1. เอาคำถามจริงไปรันกับ pipeline
2. ดู `route`, `mode`, `source`, `latency`
3. วิเคราะห์ว่าผิดเพราะ route, data, retrieval, formatter, validator หรือ ground truth
4. แก้เฉพาะจุด
5. เพิ่ม ad-hoc test หรือ ground truth
6. run compile/validate/regression
7. ถ้าต้อง deploy ให้ sync จาก folder 18 ไป 20 แล้ว deploy Vercel
8. test production API
9. update daily log/report ถ้าเป็นงานใหญ่

## กฎสำคัญที่ห้ามลืม

- ตอบภาษาไทย
- ตอบสิ่งที่ผู้ใช้ถามก่อน แล้วค่อยรายละเอียด/แหล่งข้อมูล
- อย่าให้ AI เดาข้อมูลที่ไม่มี
- อย่าบอกว่าใช้ LLM ถ้าคำตอบมาจาก rulebase/fast path
- อย่าแก้ตัวตรวจให้ผ่อนลงเพื่อให้ PASS ง่าย
- ถ้าไม่มีข้อมูลจริง ให้ no-answer แบบสุภาพ
- ถ้าแก้ core route ต้องรัน regression
- ถ้า deploy ต้อง test production

## สรุปว่าควรอ่านอะไรตามสถานการณ์

ถ้าแค่เริ่มแชทใหม่:

```text
17_IF_NEXT_AGENT_ONLY_READS_ONE_FILE.md
11_AGENT_STATE_TRANSFER_FULL.md
```

ถ้าจะแก้โค้ด:

```text
12_CHANGED_FILES_AND_CODE_INDEX.md
13_COMMAND_CHEATSHEET.md
14_SMOKE_TEST_QUESTIONS.md
```

ถ้าจะ deploy:

```text
07_DEPLOYMENT_RUNBOOK.md
13_COMMAND_CHEATSHEET.md
```

ถ้าจะเพิ่มข้อมูล/ground truth:

```text
04_DATA_KNOWLEDGE_BASE_AND_GROUND_TRUTH.md
14_SMOKE_TEST_QUESTIONS.md
15_REQUIREMENTS_AND_ACCEPTANCE_CRITERIA.md
```

ถ้าจะทำแผนต่อ:

```text
08_KNOWN_ISSUES_NEXT_STEPS.md
15_REQUIREMENTS_AND_ACCEPTANCE_CRITERIA.md
16_DO_NOT_DO_AND_RISK_REGISTER.md
```

