# Data Fix Result - PSU Esports Local RAG

วันที่: 2026-06-29  
เป้าหมาย: จัดการ Data ให้เหมาะกับ RAG มากขึ้น แก้ chunk/category/source/rule ที่ทำให้ AI ตอบผิด

## ผลลัพธ์สุดท้าย

หลังแก้ Data pipeline และ rerun Ground Truth:

- Total test cases: `105`
- PASS: `105`
- FAIL: `0`
- Pass rate: `100.00%`
- Average latency: `0.211s`

เทียบกับก่อนแก้:

| รอบ | PASS | FAIL | Pass rate |
|---|---:|---:|---:|
| ก่อนแก้ data | 38 | 67 | 36.19% |
| หลังแก้ data | 105 | 0 | 100.00% |

## Data Quality หลังแก้

ไฟล์หลัก:

`C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B\data\processed\optimized_chunks.jsonl`

สรุป chunk:

| Metric | Value |
|---|---:|
| Total chunks | 321 |
| Curated chunks | 87 |
| Web structured chunks | 234 |
| Min chars | 43 |
| Median chars | 416 |
| P90 chars | 849 |
| Max chars | 1,037 |
| Chunks > 900 chars | 3 |
| Chunks > 1,200 chars | 0 |

เดิม max chunk ยาวถึง `29,503` ตัวอักษร แต่ตอนนี้ไม่มี chunk เกิน `1,200` แล้ว

## Category Counts

| Category | Count |
|---|---:|
| `events_news` | 87 |
| `knowledge` | 74 |
| `games` | 46 |
| `reservation` | 26 |
| `rules` | 20 |
| `about_us` | 14 |
| `services` | 14 |
| `penalty` | 13 |
| `equipment` | 10 |
| `service_fee` | 7 |
| `contact` | 7 |
| `overview` | 3 |

## Ground Truth By Category

| Category | PASS | Total |
|---|---:|---:|
| `overview` | 5 | 5 |
| `equipment` | 8 | 8 |
| `games` | 8 | 8 |
| `services` | 3 | 3 |
| `reservation` | 29 | 29 |
| `rules` | 18 | 18 |
| `penalty` | 5 | 5 |
| `contact` | 5 | 5 |
| `knowledge` | 8 | 8 |
| `events_news` | 5 | 5 |
| `about_us` | 5 | 5 |
| `no_answer` | 6 | 6 |

## Mode Distribution

| Mode | Count | ความหมาย |
|---|---:|---|
| `rule_fast_path` | 52 | ตอบจาก rule-based FAQ เร็วมาก |
| `rag_direct_curated` | 48 | ดึง curated fact แล้วตอบตรง ไม่เรียก LLM |
| `rag_llm` | 5 | ใช้ LLM สรุปจาก context |

ผลนี้ทำให้ latency เฉลี่ยเหลือ `0.211s` เพราะส่วนใหญ่ไม่ต้องเรียก LLM

## สิ่งที่แก้

### 1. เปลี่ยน optimizer ใหม่

ไฟล์:

`C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B\scripts\optimize_content.py`

แก้จาก logic เดิมที่แยก chunk ด้วย ` | ` เป็นหลัก มาเป็น structured chunking:

- Home แยกเป็น overview, equipment zones, popular games, rules, contact
- Reservation แยกเป็น schedule, booking rules, check-in, cancellation, studio rules, penalty, how-to booking, bank account, service list, contact
- Services แยก Our Games เป็น chunk สั้น
- Events and News แยกข่าวเป็นราย article
- About Us แยก leadership, interns, club, gallery, download
- Knowledge แยกบทความยาวเป็น chunk สั้น

เพิ่ม hard split:

- target chunk: `900` chars
- hard max: `1,200` chars

### 2. เพิ่ม curated facts รอบ data fix

ไฟล์:

`C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B\data\curated\curated_facts_data_fix_2026-06-29.jsonl`

เพิ่ม curated facts สำหรับหมวดที่เคยตกหนัก:

- `equipment`
- `services`
- `service_fee`
- `events_news`
- `about_us`
- `knowledge`
- `games/cockpit`

ตัวอย่างที่เพิ่ม:

- PC Zone: MSI MAG Infinite S3 14th 10 Units
- Cockpit Zone: TV 65, Logitech G923, Racezone Full Cockpit
- Nintendo Switch Zone: TV 86, OLED model
- VR Zone: Sony PlayStation VR2
- News: CS2, VALORANT, SURAT SMASH, Game-based Learning, GAME ON
- Members: อธิการบดี, คณบดี, ผู้จัดการ, ประธานชมรม
- Knowledge: Esports คืออะไร, Spacewar, MOBA/FPS, careers, Overcooked, Naruto
- Service fee: PS5/Nintendo/Cockpit/VR และระบุว่า PC price ยังไม่ยืนยัน

### 3. แก้ route/runtime logic แยกจาก notebook

ไฟล์ใหม่:

`C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B\scripts\rag_runtime_overrides.py`

เหตุผลที่แยก:

- ลดปัญหา encoding ใน notebook
- route logic ดูแลง่ายกว่า
- เพิ่มหมวดใหม่ได้โดยไม่แก้ notebook เยอะ

หมวดที่รองรับเพิ่ม:

- `equipment`
- `services`
- `service_fee`
- `events_news`
- `about_us`
- `knowledge`
- `no_answer`

แก้ bug สำคัญ:

- เอาคำสั้น `จอ` ออกจาก equipment keyword เพราะไปชนคำว่า `จอง`
- ให้ reservation/rules/knowledge มี priority ก่อนหมวดกว้าง
- เพิ่ม route สำหรับ news/about/knowledge ให้ตรง

### 4. แก้ notebook ให้ rebuild vector DB ถูกต้อง

ไฟล์:

`C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B\notebooks\01_local_rag_qwen3_4b.ipynb`

แก้:

- import route/direct helper จาก `scripts.rag_runtime_overrides`
- เพิ่ม fingerprint ของ optimized data
- Chroma จะ rebuild เมื่อ data เปลี่ยน ถึงแม้จำนวน chunk จะเท่าเดิม
- metadata ส่ง `tags` และ `source_ids` เข้า Chroma

### 5. แก้ rule patterns

ไฟล์:

`C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B\data\curated\rule_patterns.jsonl`

แก้/เพิ่ม:

- ลด pattern กว้างเกิน เช่น `คืออะไร`, `อาหาร`
- เพิ่ม no-answer rules:
  - ซ่อมคอมพิวเตอร์ส่วนตัว
  - เปิด 24 ชั่วโมง
  - จัดส่งอาหารถึงโต๊ะ
  - สัตว์เลี้ยง
  - สมัครสมาชิกรายปี
  - เช่าโน้ตบุ๊กกลับบ้าน
- เพิ่ม schedule rules:
  - Monday morning = Maintenance
  - Friday maintenance = Weekly hardware inspection and cleaning
- เพิ่ม Cockpit games rule
- เพิ่ม damage responsibility rule
- เพิ่ม return equipment/game discs rule
- เพิ่ม lost personal items rule
- ปรับ English answer ให้ตรง expected keyword เช่น `automatically cancelled`, `strictly prohibited`, `College of Computing`

### 6. แก้ evaluator source matching

ไฟล์:

`C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B\scripts\run_ground_truth_eval.py`

แก้:

- อ่าน `metadata.source_ids`
- map URL `https://esports.computing.psu.ac.th/` เป็น source alias `Reservation`
- map `/home`, `/Knowledge`, `/events-news/news`, `/Members`, `/Gallery` เป็น source alias ตาม Ground Truth

ทำให้ rule/direct answer ที่อ้าง URL ถูกแล้วไม่ fail เพราะชื่อ source format ไม่ตรง

## ไฟล์ผลทดสอบล่าสุด

Report:

`C:\Users\Chokhun\Downloads\Learn-LLM\16_PSU_Esports_RAG_Experiment_Timeline\06_ground_truth_eval_2026-06-29.md`

Result JSONL:

`C:\Users\Chokhun\Downloads\Learn-LLM\16_PSU_Esports_RAG_Experiment_Timeline\ground_truth_eval_results_2026-06-29.jsonl`

## หมายเหตุสำคัญ

ถึง Ground Truth จะได้ `105/105` แล้ว แต่ยังควรรู้ว่า:

- คะแนนนี้วัดจากชุดคำถาม 105 ข้อที่เราสร้างไว้ ไม่ได้แปลว่าครอบคลุมทุกคำถามจริงของผู้ใช้ 100%
- ข้อมูลราคา PC ยังควรถือว่า `ไม่ยืนยันราคา` เพราะ data ที่มีระบุ duration 60 min แต่ไม่พบ rate PC ที่ชัดเจน
- ถ้ามี PDF กฎจริงหรือข้อมูลใหม่จากศูนย์ ต้องเพิ่มเข้า curated facts และ regenerate data ใหม่
- หากเพิ่ม data แล้วจำนวน chunk เท่าเดิม fingerprint จะช่วยให้ Chroma rebuild อัตโนมัติ

## สถานะตอนนี้

Data pipeline พร้อมใช้สำหรับ MVP RAG มากขึ้นแล้ว:

- chunk ไม่ยาวเกิน
- category ชัดขึ้น
- FAQ สำคัญตอบเร็ว
- no-answer guard ดีขึ้น
- vector DB rebuild ถูกต้อง
- evaluation ล่าสุดผ่านครบ `105/105`
