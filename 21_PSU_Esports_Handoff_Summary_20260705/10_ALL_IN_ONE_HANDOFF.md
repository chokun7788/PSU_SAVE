# All-in-one Handoff: PSU Esports Chatbot

ไฟล์นี้คือสรุปรวมแบบไฟล์เดียว เหมาะสำหรับส่งให้อีกแชทอ่าน ถ้าไม่อยากเปิดหลายไฟล์

## 1. โปรเจกต์นี้คืออะไร

เป็นโปรเจกต์ AI Chatbot สำหรับ PSU Esports Studio - Phuket เพื่อให้ผู้ใช้ถามข้อมูลของศูนย์ได้ เช่น:

- เวลาเปิดปิด
- วันนี้เปิดไหม
- วันหยุด/วันปิดพิเศษ
- วิธีจอง
- กฎการจอง
- การเช็คอิน
- ค่าบริการ
- เกมที่มีให้เล่น
- อุปกรณ์และโซนต่าง ๆ
- กติกาการแข่งขัน
- ข้อมูลติดต่อ

เว็บต้นทาง:

```text
https://esports.phuket.psu.ac.th/
https://esports.phuket.psu.ac.th/home
https://esports.phuket.psu.ac.th/Services/our-games
https://esports.computing.psu.ac.th/reservation
```

## 2. ข้อกำหนดหลักจากผู้ใช้

- เน้น local/free
- ไม่อยากใช้ API เสียเงิน
- ต้องทำ MVP ให้ใช้งานได้เร็ว
- ต้องทำ log รายวัน
- รองรับภาษาไทย/อังกฤษ
- เริ่มจาก text ก่อน
- เน้น FAQ ก่อน
- Action เช่น จอง/ยกเลิก/เช็คสถานะ เอาไว้ phase 2
- ตอน demo รัน local ได้
- Deploy เว็บ demo ได้
- ถ้า production จริงอาจไป Facebook Messenger
- ต้องไม่ตอบมั่วถ้าไม่มีข้อมูลจริง

## 3. สถานะล่าสุด

โฟลเดอร์หลัก:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data
```

โฟลเดอร์ deploy:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy
```

Production:

```text
https://psu-esports-chatbot.vercel.app
```

Local:

```text
http://127.0.0.1:8018/
```

Notebook test:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\notebooks\02_test_final_pipeline.ipynb
```

ผล test ล่าสุด:

```text
GT360: 360/360 PASS
Competition challenger v2: 369/369 PASS
รวม regression หลัก: 729/729 PASS
```

## 4. ระบบตอบด้วยอะไร

Production ตอนนี้ไม่ได้ใช้ LLM เป็นหลัก

ใช้:

- rulebase
- deterministic calculator
- fast path
- competition fact cards
- curated RAG-lite
- guard/no-answer

เหตุผล:

- เร็วกว่า
- ฟรีกว่า
- คุมคำตอบได้ดีกว่า
- Vercel ไม่เหมาะกับ local LLM

LLM/Qwen ยังอยู่ใน phase ทดลองที่:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\19_PSU_Esports_Qwen35_Hybrid_RAG
```

## 5. Pipeline

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

ไฟล์สำคัญ:

```text
app\runtime\fast_answer.py
app\pipeline\router.py
app\pipeline\engine.py
app\pipeline\retrieval.py
app\pipeline\formatter.py
app\pipeline\validator.py
app\calculator\service_fee.py
app\calendar\service_calendar.py
```

## 6. ข้อมูลในระบบ

Curated facts:

```text
data\curated\curated_facts.jsonl
42 rows
```

Competition rules:

```text
data\competition_rules\competition_rule_documents.jsonl
4 documents

data\competition_rules\competition_rule_chunks.jsonl
104 chunks

data\curated\curated_competition_rules.jsonl
104 rows
```

Equipment details:

```text
data\curated\equipment_item_details.jsonl
16 rows
```

Game details:

```text
data\curated\game_item_details.jsonl
36 rows
```

Rules:

```text
data\rules\*.jsonl
8 files
```

Calendar:

```text
data\calendar\service_closures.jsonl
```

Ground Truth:

```text
15_PSU_Esports_Local_RAG_Qwen3_4B\ground_truth\ground_truth_v2_360.jsonl
18_PSU_Esports_Update_Route_Data\data\ground_truth\ground_truth_competition_rules_v1_228.jsonl
18_PSU_Esports_Update_Route_Data\data\ground_truth\competition_challenger_v2\ground_truth_competition_challenger_v2_real_competitor_questions.jsonl
```

## 7. หมวดคำถามที่ตอบได้

### เวลาเปิดปิด

ตอบ:

- Monday morning maintenance
- Monday afternoon open
- Tuesday-Thursday เปิดตามรอบ
- Friday morning open
- Friday afternoon maintenance
- Morning 09:00-12:00
- Afternoon 13:00-16:00
- ไม่เปิด 24 ชั่วโมง

### วันปิดพิเศษ

ใช้ `service_closures.jsonl`

เคยเพิ่ม 28-30 กรกฎาคม 2026 เป็นวันปิด

### ราคา

จาก Service Fee 2026:

- PS5
- Nintendo Switch
- Cockpit
- VR

กลุ่ม:

- PSU Student and Staff
- PSU Alumni and General Student
- General Adult

หลักตอบ:

- ตอบราคาไว้บรรทัดแรก
- ถ้าไม่รู้กลุ่ม แสดงทุกกลุ่ม
- ต่างมหาวิทยาลัย = General Student
- เด็ก/นักศึกษา มอ = PSU Student and Staff

### เกมและอุปกรณ์

ตอบได้:

- PC Zone
- PS5 Zone
- Nintendo Switch Zone
- Cockpit Zone
- VR Zone
- เกมที่เล่นได้ในแต่ละโซน
- เกมนี้มีไหม
- เกมนี้คืออะไร
- เล่นยังไง
- อุปกรณ์นี้คืออะไร

### กติกาการแข่งขัน

ตอบได้จาก 4 เกม:

- CS2
- VALORANT
- RoV
- Tekken 8

ใช้ fact cards และ curated RAG-lite

## 8. ปัญหาล่าสุดและการแก้

ปัญหา:

ถาม:

```text
อุปกรณ์เล่นเกมอะไรได้บ้าง
```

เคยตอบ:

```text
ยังไม่พบ เกมนี้ ในรายการเกมที่ยืนยันได้
```

สาเหตุ:

- route เดิมจับเป็น game availability
- ไม่มีชื่อเกมเฉพาะ จึง fallback เป็น `เกมนี้`
- คำถาม unknown game บางทีหลุดไป schedule/competition

แก้แล้ว:

- เพิ่ม route `equipment_game_catalog`
- เพิ่ม mode `pipeline:equipment_game_catalog_fast_path`
- แยก equipment game catalog กับ game availability
- unknown game เช่น Minecraft/Roblox ตอบว่าไม่พบเกมนั้นในรายการที่ยืนยันได้
- คำถามกติกา Tekken ที่มี `round/decider` ไม่หลุดไป route เกมแล้ว

ผล production:

```text
อุปกรณ์เล่นเกมอะไรได้บ้าง -> ตอบเกมทุกโซน
Cockpit มีเกมอะไรบ้าง -> Gran Turismo 7
VR มีเกมอะไรบ้าง -> Beat Saber, Horizon Call of the Mountain
เล่น Minecraft ได้ไหม -> ไม่พบ Minecraft ในรายการเกมที่ยืนยันได้
Roblox เล่นได้ไหม -> ไม่พบ Roblox ในรายการเกมที่ยืนยันได้
ตอนนี้มีเกมแข่งอะไรบ้าง -> รายการ CS2, VALORANT, RoV, Tekken 8
```

## 9. Report ล่าสุด

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\ad_hoc_pipeline_results_equipment_game_catalog_fix5_source_20260704.md

C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_report_gt360_equipment_game_catalog_fix5_source_20260704.md

C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\pipeline_ground_truth_report_competition_challenger_v2_equipment_game_catalog_fix5_source_20260704.md
```

## 10. คำสั่งสำคัญ

รัน local:

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data"
py -3 -m app.web_api.server --host 127.0.0.1 --port 8018
```

Validate:

```powershell
py -3 tools\validate_update.py
```

Compile:

```powershell
py -3 -m py_compile app\runtime\fast_answer.py app\pipeline\router.py app\pipeline\engine.py
```

Run GT360:

```powershell
py -3 tools\run_ground_truth_pipeline_eval.py --label manual_check
```

Run competition challenger:

```powershell
py -3 tools\run_ground_truth_pipeline_eval.py --ground-truth data\ground_truth\competition_challenger_v2\ground_truth_competition_challenger_v2_real_competitor_questions.jsonl --label manual_comp_check
```

Deploy:

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy"
vercel deploy --prod --yes
```

## 11. สิ่งที่ยังต้องทำต่อ

ลำดับแนะนำ:

1. เก็บคำถามจริงจาก log แล้วเพิ่ม ad-hoc/ground truth
2. ทำหลายคำถามในข้อความเดียว
3. ทำ session memory
4. ทำ Facebook Messenger webhook
5. ขอข้อมูลจริงจากศูนย์เพิ่ม เช่น penalty/booking API/day off/latest games
6. ทำ admin page สำหรับเพิ่มข้อมูล
7. ทดลอง RAG/LLM fallback ในโฟลเดอร์ 19
8. ทำ Dockerfile สำหรับ backend local
9. ทำ GitHub repo และ Vercel auto deploy
10. ทำ dashboard unanswered questions

## 12. ข้อควรระวัง

- อย่าให้ LLM เดาข้อมูลที่ไม่มี
- อย่าเชื่อ Ground Truth 100% โดยไม่อ่านคำตอบจริง
- ถ้าแก้ route ต้อง run regression
- ถ้าแก้ data ต้องเพิ่ม test
- ถ้า deploy ต้อง sync จาก 18 ไป 20 ก่อน
- ถ้าใช้ภาษาไทยใน PowerShell ให้ตั้ง UTF-8 ก่อนรัน

## 13. Prompt สำหรับแชทใหม่

ใช้ได้เลย:

```text
อ่าน handoff นี้ก่อน:
C:\Users\Chokhun\Downloads\Learn-LLM\21_PSU_Esports_Handoff_Summary_20260705

โฟลเดอร์หลัก:
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data

Deploy folder:
C:\Users\Chokhun\Downloads\Learn-LLM\20_PSU_Esports_Vercel_Deploy

Production:
https://psu-esports-chatbot.vercel.app

ช่วยทำโปรเจกต์ PSU Esports Chatbot ต่อจากสถานะล่าสุด โดยตอบภาษาไทย แก้จากไฟล์จริง รันทดสอบก่อนสรุป และอย่าให้ระบบตอบมั่วถ้าไม่มีข้อมูลจริง
```

