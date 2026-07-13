# PSU Esports Chatbot Handoff Summary

สร้างเมื่อ: 2026-07-05  
โฟลเดอร์นี้ทำไว้สำหรับเปิดในแชทใหม่ เพื่อลด token และให้ AI ตัวต่อไปเข้าใจโปรเจกต์ PSU Esports Chatbot ได้เร็วที่สุด

## อ่านไฟล์ไหนก่อน

แนะนำลำดับอ่าน:

1. `00_README_START_HERE.md` ไฟล์นี้ สรุปเร็วที่สุด
2. `01_HANDOFF_CONTEXT_FOR_NEXT_CHAT.md` บริบทเต็มแบบเล่าให้ AI ตัวใหม่เข้าใจ
3. `03_FILE_AND_FOLDER_MAP.md` แผนที่โฟลเดอร์และไฟล์สำคัญ
4. `05_PIPELINE_RULE_RAG_LLM_DESIGN.md` อธิบายระบบตอบคำถามทำงานยังไง
5. `08_KNOWN_ISSUES_NEXT_STEPS.md` สิ่งที่ยังควรทำต่อ
6. `09_COPY_PASTE_PROMPT_FOR_NEW_CHAT.md` prompt สำเร็จรูปสำหรับโยนให้อีกแชท
7. `11_AGENT_STATE_TRANSFER_FULL.md` ความต้องการ/ข้อห้าม/วิธีคิดแบบละเอียดที่สุดสำหรับ agent ใหม่
8. `17_IF_NEXT_AGENT_ONLY_READS_ONE_FILE.md` ไฟล์เดียวแบบสั้นที่สุดถ้า agent ใหม่อ่านได้แค่ไฟล์เดียว

ถ้ารีบมาก ให้อ่านแค่:

- `01_HANDOFF_CONTEXT_FOR_NEXT_CHAT.md`
- `09_COPY_PASTE_PROMPT_FOR_NEW_CHAT.md`
- `17_IF_NEXT_AGENT_ONLY_READS_ONE_FILE.md`

ถ้าต้องการให้ AI ตัวใหม่ “รับช่วงเหมือนอยู่แชทนี้” ให้อ่าน:

- `11_AGENT_STATE_TRANSFER_FULL.md`
- `12_CHANGED_FILES_AND_CODE_INDEX.md`
- `13_COMMAND_CHEATSHEET.md`
- `14_SMOKE_TEST_QUESTIONS.md`
- `15_REQUIREMENTS_AND_ACCEPTANCE_CRITERIA.md`
- `16_DO_NOT_DO_AND_RISK_REGISTER.md`

## สถานะล่าสุดของโปรเจกต์

โปรเจกต์หลักตอนนี้อยู่ที่:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data
```

โฟลเดอร์ deploy Vercel อยู่ที่:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy
```

เว็บ production:

```text
https://psu-esports-chatbot.vercel.app
```

local web/API:

```text
http://127.0.0.1:8018/
POST http://127.0.0.1:8018/api/chat
GET  http://127.0.0.1:8018/health
```

โน้ตบุ๊กทดสอบหลัก:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\notebooks\02_test_final_pipeline.ipynb
```

## สิ่งที่ระบบทำได้ตอนนี้

ระบบเป็น Chatbot สำหรับ PSU Esports Studio - Phuket โดยเน้นตอบ FAQ และข้อมูลจากเว็บ/ไฟล์ที่มีในฐานข้อมูล

ตอบได้ดีในหมวด:

- เวลาเปิดปิดและตารางบริการ
- วันปิดพิเศษ/วันหยุดที่ config ไว้ เช่น 28-30 กรกฎาคม 2026
- กฎการจองและการเช็คอิน
- กฎทั่วไปของศูนย์
- ราคาค่าบริการ Service Fee 2026 พร้อมคำนวณบางกรณี
- รายการเกมที่เล่นได้ตามโซน
- รายละเอียดอุปกรณ์ เช่น PC Zone, VR Zone, Cockpit Zone, PS5, Nintendo Switch
- เกมรายตัว เช่น Beat Saber, Gran Turismo 7, TEKKEN 8, VALORANT
- กติกาการแข่งขัน CS2, VALORANT, RoV, Tekken 8
- คำถามที่ไม่พบข้อมูลจริง จะตอบแบบไม่มั่วและแนะนำให้ถามเจ้าหน้าที่

## สถาปัตยกรรมล่าสุดแบบสั้น

ตอนนี้ระบบ production ไม่ได้ใช้ LLM local หรือ API LLM เป็นหลัก

เหตุผล:

- ต้องการฟรี
- ต้องตอบเร็ว
- Vercel serverless ไม่เหมาะกับการรันโมเดล local หลาย GB
- คำถามส่วนใหญ่เป็น FAQ/ข้อมูลตายตัว จึงควรใช้ rulebase, calculator, fact card และ RAG-lite ก่อน

ระบบตอบผ่าน pipeline:

```text
User question
-> preprocess/normalize
-> entity extraction
-> guard/no-answer
-> intent router
-> deterministic fast path/rulebase/calculator
-> competition fact cards
-> curated RAG-lite fallback
-> formatter
-> validator
-> answer + route + mode + sources
```

## ผลทดสอบล่าสุด

หลังแก้ปัญหาคำถามอุปกรณ์/เกมล่าสุด:

- GT360: 360/360 PASS
- Competition challenger v2: 369/369 PASS
- รวม regression หลัก: 729/729 PASS
- Production API ทดสอบแล้วผ่าน

ไฟล์ report ล่าสุด:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_report_gt360_equipment_game_catalog_fix5_source_20260704.md
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_report_competition_challenger_v2_equipment_game_catalog_fix5_source_20260704.md
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\ad_hoc_pipeline_results_equipment_game_catalog_fix5_source_20260704.md
```

## ปัญหาล่าสุดที่เพิ่งแก้

ปัญหา:

ผู้ใช้ถามว่า:

```text
อุปกรณ์เล่นเกมอะไรได้บ้าง
Cockpit มีเกมอะไรบ้าง
VR มีเกมอะไรบ้าง
Roblox เล่นได้ไหม
Minecraft เล่นได้ไหม
ตอนนี้มีเกมแข่งอะไรบ้าง
```

ระบบเดิมบางครั้งตอบผิด เช่น:

- `ยังไม่พบ เกมนี้ ในรายการเกมที่ยืนยันได้`
- ดึง schedule มาตอบ Roblox
- ดึงกติกา CS2 มาตอบ Minecraft
- ดึงข่าว Tekken มาตอบคำถามเกมแข่งทั้งหมด

สิ่งที่แก้:

- เพิ่ม route `equipment_game_catalog`
- เพิ่ม mode `pipeline:equipment_game_catalog_fast_path`
- แยก intent ระหว่าง “อุปกรณ์มีเกมอะไรบ้าง” กับ “เกมนี้เล่นได้ไหม”
- unknown game เช่น Minecraft/Roblox จะตอบว่าไม่พบในรายการเกมที่ยืนยันได้ และแสดงรายการเกมที่มีจริงแทน
- คำถามกติกา Tekken เช่น `round`, `decider`, `1v1`, `R3` จะเข้า competition rule ไม่หลุดไป game availability
- แหล่งข้อมูลเกมปรับให้อ้างหน้า `Our Games`

## สิ่งที่ยังต้องทำต่อ

เรื่องสำคัญที่ยังควรพัฒนา:

- รองรับหลายคำถามในข้อความเดียว
- ทำ memory สนทนายาวแบบ session จริง
- เชื่อม Facebook Messenger
- ทำ admin/update data flow ที่ใช้งานง่าย
- เพิ่มข้อมูลจากเจ้าหน้าที่ เช่น กฎค่าปรับจริง, booking API, ข้อมูลปิดทำการจริง, รายการเกม/อุปกรณ์ล่าสุด
- ทำ RAG/LLM fallback ที่ฉลาดขึ้นสำหรับคำถามนอก rulebase แต่ยังต้องไม่มั่ว
- ทำ evaluation ที่มี human review เพิ่มสำหรับคำตอบเชิงภาษา ไม่ใช่แค่ keyword

## คำสั่งพื้นฐาน

รัน local web/API:

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data"
py -3 -m app.web_api.server --host 127.0.0.1 --port 8018
```

ตรวจ sanity:

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data"
py -3 tools\validate_update.py
py -3 -m py_compile app\runtime\fast_answer.py app\pipeline\router.py app\pipeline\engine.py
```

รัน GT360:

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data"
py -3 tools\run_ground_truth_pipeline_eval.py --label manual_check_YYYYMMDD
```

deploy Vercel:

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy"
vercel deploy --prod --yes
```

## ไฟล์เสริมสำหรับ agent ใหม่

เพิ่มไฟล์ชุด state transfer รอบละเอียด:

- `11_AGENT_STATE_TRANSFER_FULL.md` สรุปความต้องการผู้ใช้, product policy, answer policy, no-answer policy, สิ่งที่ต้องรักษา
- `12_CHANGED_FILES_AND_CODE_INDEX.md` ชี้ตำแหน่งโค้ด/ฟังก์ชันจริงที่เกี่ยวข้อง
- `13_COMMAND_CHEATSHEET.md` รวมคำสั่ง compile/test/run/deploy
- `14_SMOKE_TEST_QUESTIONS.md` ชุดคำถาม smoke test หลังแก้ทุกครั้ง
- `15_REQUIREMENTS_AND_ACCEPTANCE_CRITERIA.md` requirement และเกณฑ์ว่าเสร็จจริงคืออะไร
- `16_DO_NOT_DO_AND_RISK_REGISTER.md` ข้อห้ามและความเสี่ยง
- `17_IF_NEXT_AGENT_ONLY_READS_ONE_FILE.md` สรุปฉุกเฉินสำหรับอ่านไฟล์เดียว
