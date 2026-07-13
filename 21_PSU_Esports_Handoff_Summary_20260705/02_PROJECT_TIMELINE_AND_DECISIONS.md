# Timeline และ Decision Log

ไฟล์นี้สรุปลำดับเหตุการณ์สำคัญและการตัดสินใจด้านเทคนิคของโปรเจกต์

## ช่วงเริ่มต้น

เริ่มจากผู้ใช้มีโฟลเดอร์เรียน LLM/RAG:

```text
C:\Users\Chokhun\Downloads\Learn-LLM
```

มีการทำเอกสารพื้นฐานหลายไฟล์:

- `00_เริ่มต้นที่นี่_Roadmap.md`
- `01_พื้นฐานก่อนเริ่ม.md`
- `02_LLM_พื้นฐาน.md`
- `03_Embeddings_และ_Vector_DB.md`
- `04_RAG_พื้นฐาน_Pipeline.md`
- `05_Advanced_RAG.md`
- `06_Evaluation.md`
- `07_Production.md`
- `08_ต่อยอด_Agentic_FineTune_GraphRAG.md`
- `09_ภาษาไทยโดยเฉพาะ.md`
- `10_แหล่งเรียนและโปรเจค.md`

เป้าหมายตอนนั้นคือเรียนรู้ LLM/RAG แบบกว้าง ๆ ก่อน

## 11-14: วางแผน Chatbot

สร้างโฟลเดอร์แนวทาง:

```text
11_PSU_Esports_AI_ChatBot
12_PSU_Esports_AI_ChatBot_Full_Pipeline
13_PSU_Esports_AI_ChatBot_Local_vs_API
14_Chatbot_Stakeholder_Questions
```

เนื้อหาหลัก:

- สรุปว่าจะทำ Chatbot ของ PSU Esports ยังไง
- เปรียบเทียบ Local vs API
- วาง pipeline ตั้งแต่ data -> retrieval -> LLM -> deploy
- ทำ list คำถามที่ควรถาม stakeholder เช่น งบ, cloud, API, local, input format, booking action, login, data format

Decision:

- ถ้าเป็น MVP ให้เน้น FAQ ก่อน
- Action เช่น จอง/ยกเลิก/เช็คสถานะ ให้เก็บไว้ phase หลัง
- ควรแยกคำถามที่ตอบได้จากข้อมูลจริงกับคำถามที่ต้องถามเจ้าหน้าที่

## 15: Local RAG Qwen3 4B

โฟลเดอร์:

```text
15_PSU_Esports_Local_RAG_Qwen3_4B
```

สิ่งที่ทำ:

- วาง notebook สำหรับ RAG local
- เตรียม data และ ground truth
- ทดลองโมเดล local/Qwen
- คุยเรื่องว่า RAG ไม่ใช่การ train โมเดลถาวร
- สรุปว่าโมเดลจะไม่ “จำ” ข้อมูลใหม่เอง แต่ pipeline จะโหลด data/index มาใช้

Ground Truth สำคัญ:

```text
15_PSU_Esports_Local_RAG_Qwen3_4B\ground_truth\ground_truth_v2_360.jsonl
```

มี 360 ข้อ ใช้ทดสอบ FAQ หลัก เช่น:

- ราคา
- ตารางเวลา
- การจอง
- กฎ
- เกม
- อุปกรณ์
- contact
- no-answer

Decision:

- ใช้ Ground Truth เป็นตัวจับ regression
- ต้องระวัง false pass เพราะ keyword check อาจบอกถูกทั้งที่คำตอบผิด เช่น ตอบราคาผิดแต่มี keyword บางตัวครบ

## 16-17: Timeline และ Daily Logs

โฟลเดอร์:

```text
16_PSU_Esports_RAG_Experiment_Timeline
17_PSU_Esports_Daily_Logs
```

จุดประสงค์:

- บันทึกว่าแต่ละวันทำอะไร
- เจอปัญหาอะไร
- แก้อะไรไป
- ผลลัพธ์เป็นอย่างไร

ไฟล์ daily log:

- `2026-06-29.md`
- `2026-06-30.md`
- `2026-07-01.md`
- `2026-07-02.md`
- `2026-07-03.md`
- `2026-07-04.md`

Decision:

- ทุกครั้งที่แก้ใหญ่ควร update daily log
- ใช้ daily log เป็นเอกสารฝึกงานและเป็น project memory

## 18: Update Route + Data Layer

โฟลเดอร์หลักปัจจุบัน:

```text
18_PSU_Esports_Update_Route_Data
```

เป้าหมาย:

- แยก rulebase, calculator, RAG-lite, LLM, validator ให้ชัดขึ้น
- ลด hallucination
- ตอบเร็วขึ้น
- เพิ่ม data ใหม่ได้ง่าย
- มีระบบ evaluation ที่รัดกุมขึ้น

สิ่งที่เกิดขึ้นในโฟลเดอร์นี้:

- เพิ่ม answer pipeline ใหม่
- เพิ่ม fast runtime
- เพิ่ม rulebase แยกหมวด
- เพิ่ม service fee calculator
- เพิ่ม calendar/holiday layer
- เพิ่ม competition rules ingestion
- เพิ่ม game/equipment details
- เพิ่ม web chat local
- เพิ่ม tools สำหรับ ground truth และ ad-hoc test

Decision สำคัญ:

- คำถามตายตัวใช้ rulebase/calculator ก่อน
- คำถามราคาใช้ deterministic calculator
- คำถามกติกาแข่งขันใช้ fact cards และ curated RAG-lite
- คำถามไม่มีข้อมูลให้ตอบ no-answer สุภาพ
- LLM ไม่ควรถูกใช้ให้เดาข้อมูลสำคัญ

## กฎราคาและ Service Fee

เพิ่มข้อมูลราคา Service Fee 2026 จากภาพ:

- PlayStation 5 1 ชั่วโมง
- Nintendo Switch 1 ชั่วโมง 1-2 persons
- Nintendo Switch 1 ชั่วโมง 3-4 persons
- Cockpit 1 ชั่วโมง 1 person
- VR 30 นาที 1-5 persons
- VR 1 ชั่วโมง 1-5 persons

กลุ่มผู้ใช้:

- PSU Student and Staff: ฟรี
- PSU Alumni and General Student: ราคากลาง
- General Adult: ราคาสูงสุด

Decision:

- ถ้าผู้ใช้บอกว่าเป็นนักศึกษา PSU/เด็ก มอ/นักเรียน มอ ให้คิดเป็น PSU Student and Staff
- ถ้าเป็นต่างมหาวิทยาลัย เช่น สจล/จุฬา ให้คิดเป็น General Student
- ถ้าไม่ระบุกลุ่มและถามราคา ให้แสดงทุกกลุ่มแทนที่จะเดา
- ราคาต้องตอบไว้บรรทัดแรก แล้วค่อยรายละเอียด

## ปัญหา false pass ของ Ground Truth

เคยพบเคสเช่น:

```text
เด็ก มอ เล่นเพลย์ห้าเสียกี่บาท
```

เฉลยควรเป็น 0 บาท แต่ AI ตอบ 150 บาทและตัวตรวจยังบอก PASS เพราะ keyword/source check ไม่เข้มพอ

Decision:

- เพิ่ม strict audit
- ตรวจคำตอบด้วย logic เพิ่ม ไม่ใช่ keyword อย่างเดียว
- ต้องอ่าน human review บางช่วงด้วย
- คำตอบราคาให้บังคับ direct answer missing check

## Competition Rules

เพิ่มกติกาการแข่งขันจากไฟล์ `.txt` 4 รายการ:

- Counter-Strike 2 รายการ PSU Phuket CS2 2026 Tournament
- VALORANT รายการ PSU Phuket VALORANT 2026 Tournament
- Arena of Valor (RoV) รายการ Blueket Games 2025 ประเภททีมชาย
- Tekken 8 รายการ PSU Esports ปะทะมันส์ สนั่นจอ

แปลงเป็น JSONL:

- documents
- chunks
- curated_competition_rules
- fact cards
- ground truth

Decision:

- คำถามกติกาควรตอบแบบ answer-first
- ต้องบอกคำตอบก่อน แล้วค่อยหลักฐาน/อ้างอิง
- ถ้าไม่พบข้อมูลในกติกา อย่าดึงข้อมูลเกมอื่นมาตอบ
- ต้องระวังคำถามสั้น ๆ เช่น `สมาชิกทีม ROV ต้องมีกี่คน` เพราะ keyword ใกล้กับหลาย section

## 19: Qwen35 Hybrid RAG

โฟลเดอร์:

```text
19_PSU_Esports_Qwen35_Hybrid_RAG
```

จุดประสงค์:

- ทดลองเอาข้อมูลจาก `18` มารวมเป็น corpus เดียว
- ทำ lexical index
- เตรียม vector index ผ่าน Ollama
- ทดลองถามด้วย Qwen 3.5/4B หรือโมเดลใกล้เคียง
- ใช้เทียบว่า rulebase/RAG-lite/LLM แบบไหนเหมาะกว่า

Decision:

- ยังไม่ใช่ production หลัก
- เหมาะเป็น research/phase 2
- ถ้าจะใช้จริง ควรจำกัด LLM ให้ตอบจาก context เท่านั้น และมี guard/no-answer

## 20: Vercel Deploy

โฟลเดอร์:

```text
20_PSU_Esports_Vercel_Deploy
```

จุดประสงค์:

- ทำ package สำหรับ Vercel
- มีหน้าเว็บ demo
- มี `/api/chat` และ `/api/health`
- Bundle เฉพาะ data/code ที่จำเป็น

Production:

```text
https://psu-esports-chatbot.vercel.app
```

Decision:

- Vercel ใช้ Python serverless function
- ไม่รัน local LLM
- ใช้ rulebase/RAG-lite/fact-card ที่ bundle ไปกับ function
- ถ้าจะใช้ LLM จริงในอนาคต ให้แยก backend

## ปัญหาล่าสุดที่แก้ก่อนสร้าง handoff

ผู้ใช้พบว่า:

```text
อุปกรณ์เล่นเกมอะไรได้บ้าง
```

ระบบตอบผิดว่า:

```text
ยังไม่พบ เกมนี้ ในรายการเกมที่ยืนยันได้
```

สาเหตุ:

- router เดิมมองคำถาม generic game catalog เป็น game availability
- ไม่มีชื่อเกมเฉพาะ จึง fallback เป็น `เกมนี้`
- บางคำถาม unknown game ดึง schedule หรือกติกามาตอบผิด

แก้โดย:

- เพิ่ม `equipment_game_catalog`
- เพิ่ม `_looks_like_equipment_game_catalog`
- เพิ่ม `_equipment_game_catalog_answer`
- ปรับ source เป็น `our_games`
- เพิ่ม guard ของ game availability เพื่อไม่ชน competition rule

ผล:

- GT360 ผ่าน 360/360
- Competition challenger v2 ผ่าน 369/369
- Local API ผ่าน
- Production API ผ่าน

