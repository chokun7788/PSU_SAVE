# PSU Esports Local RAG Chatbot - Full System Summary

วันที่สรุป: 2026-06-29  
โปรเจกต์หลัก: `C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B`  
โฟลเดอร์รายงาน/Timeline: `C:\Users\Chokhun\Downloads\Learn-LLM\16_PSU_Esports_RAG_Experiment_Timeline`

## 1. เป้าหมายของระบบ

ทำ Local AI Chatbot แบบ RAG สำหรับเว็บ PSU Esports Studio - Phuket โดยเน้นตอบคำถาม FAQ ให้คนทั่วไป/ลูกค้า เช่น:

- กฎการใช้บริการ
- กฎการจอง
- การเช็คอิน/ยกเลิก/คืนเงิน
- รายการเกมและอุปกรณ์
- ช่องทางติดต่อ
- เวลาเปิด-ปิด/รอบบริการ
- คำนวณราคาจองจากเวลาและประเภทบริการ ในระดับ MVP

แนวทางหลักคือรัน Local เป็นหลัก ไม่ใช้ API เสียเงิน และต้องสามารถพัฒนาไป deploy ผ่าน Docker ได้ในอนาคต

## 2. Stack ที่ใช้

### LLM

- `qwen2.5:3b` ผ่าน Ollama ใช้เป็นค่า default ตอนนี้ เพราะตอบเร็วกว่า เหมาะกับ MVP บนเครื่องที่ RAM ไม่เยอะ
- `qwen3:4b` โหลดไว้แล้ว ใช้เป็น quality model ได้ แต่ช้ากว่า

เหตุผลที่ default เป็น `qwen2.5:3b`:

- เครื่องเป้าหมาย RAM ประมาณ 8GB-32GB แล้วแต่เครื่อง demo/ศูนย์
- ต้องการ latency ต่ำกว่า 10 วินาที
- RAG + rule/direct answer ช่วยลดงานของ LLM ได้มาก จึงไม่จำเป็นต้องใช้โมเดลใหญ่ตลอด

### Embedding

- `intfloat/multilingual-e5-small`
- เหมาะกับไทย/อังกฤษ และเบาพอสำหรับเครื่อง local
- ใช้ prefix แบบ `query: ...` ตอน embed query

### Vector Database

- ChromaDB
- Collection: `psu_esports_local_rag_optimized`
- Path: `data/vector_db/chroma_psu_esports`

### Main Notebook

- `notebooks/01_local_rag_qwen3_4b.ipynb`

### Core Config ปัจจุบัน

```python
FAST_LOCAL_MODEL = "qwen2.5:3b"
QUALITY_LOCAL_MODEL = "qwen3:4b"
LLM_MODEL = FAST_LOCAL_MODEL
EMBEDDING_MODEL = "intfloat/multilingual-e5-small"

TOP_K = 4
MAX_CONTEXT_CHARS = 3200
MAX_DOC_CHARS = 750
LLM_KEEP_ALIVE = "30m"
LLM_NUM_CTX = 2048
LLM_NUM_PREDICT = 120
LLM_TEMPERATURE = 0.0
```

## 3. โครงสร้างไฟล์สำคัญ

```text
15_PSU_Esports_Local_RAG_Qwen3_4B/
  data/
    raw/
      all_sections_rag_chunks.jsonl
      SERVICE-FEE-2026.png
    raw_sections/
      Home/section_text.txt
      Reservation/section_text.txt
      Services/section_text.txt
      Contact_Us/section_text.txt
      Knowledge/section_text.txt
      Events_and_News/section_text.txt
      About_Us/section_text.txt
    curated/
      curated_facts.jsonl
      rule_patterns.jsonl
    processed/
      chunks_clean.jsonl
      optimized_chunks.jsonl
      optimization_manifest.json
    vector_db/
      chroma_psu_esports/
  ground_truth/
    ground_truth_seed.jsonl
    ground_truth_full.jsonl
    README.md
  notebooks/
    01_local_rag_qwen3_4b.ipynb
  scripts/
    optimize_content.py
    rule_matcher.py
    run_smoke_tests.py
    run_ground_truth_eval.py
    run_ollama_fast.ps1
    run_ollama_qwen3_4b.ps1
  optimization/
    README.md
    latency_optimization.md
    rule_based_fast_path.md
    content_optimization_checklist.md
  prompts/
    system_prompt_th_en.md
```

## 4. Pipeline ปัจจุบัน

### Step 1: Load Data

โหลดข้อมูลจาก:

- `data/processed/optimized_chunks.jsonl` ถ้ามี
- fallback ไป `data/raw/all_sections_rag_chunks.jsonl`

มีขั้นตอนซ่อมภาษาไทยที่ mojibake เช่น `à¸...` ด้วย `repair_mojibake()`

### Step 2: Clean + Category + Metadata

แต่ละ chunk จะมี field เช่น:

- `id`
- `title`
- `category`
- `source_url`
- `source_type`
- `priority`
- `text`

ตอนนี้ยังมีปัญหา category บาง chunk ผิด เช่น:

- `home-01-001` ถูกจัดเป็น `penalty` ทั้งที่ควรเป็น `overview/equipment/rules`
- `reservation-01-001` ถูกจัดเป็น `penalty` ทั้งที่มีหลายหมวดรวมกัน เช่น schedule, reservation, rules, services
- `events-and-news-01-001` ถูกจัดเป็น `rules` ทั้งที่ควรเป็น `events_news`

นี่เป็นหนึ่งในสาเหตุใหญ่ที่ retrieval ดึงผิด

### Step 3: Build Chroma Index

ถ้า collection ว่างหรือจำนวน chunk ไม่ตรงกับ records จะ rebuild index

### Step 4: Question Routing

มี `route_category(query)` เพื่อ filter หมวดก่อนค้น เช่น:

- penalty
- overview
- reservation
- rules
- games
- contact
- competition

มีการเพิ่ม route สำหรับ service schedule: 

- `เปิดถึง`
- `เปิดกี่โมง`
- `ปิดถึงกี่โมง`
- `ปิดกี่โมง`
- `เปิดปิดกี่โมง`
- `เวลาเปิด`
- `เวลาปิด`
- `เวลาทำการ`
- `ตารางบริการ`

### Step 5: Retrieval

คะแนน retrieval ใช้:

```text
score = -distance + lexical_score + priority_boost + curated_boost + schedule_boost
```

เพิ่ม `schedule_boost` เพื่อดัน `curated_schedule_morning` และ `curated_schedule_afternoon` เมื่อถามเวลาเปิด-ปิด

### Step 6: Answer Modes

ตอนนี้ `answer_question()` มี 4 โหมดหลัก:

1. `deterministic_calculator`
2. `rule_fast_path`
3. `rag_direct_curated`
4. `rag_llm`

ลำดับการทำงาน:

```text
question
  -> calculator ถ้าเป็นคำถามคำนวณราคา/เวลา
  -> rule-based ถ้า match FAQ rule
  -> retrieve top_k
  -> direct curated answer ถ้าเจอ curated fact ชัด
  -> LLM ตอบจาก context
```

## 5. สิ่งที่ปรับไปแล้ว

### 5.1 เปลี่ยนโมเดล default เพื่อความเร็ว

จากเดิมอยากใช้ `qwen3:4b` เป็นหลัก แต่ตอบช้ากว่า จึงตั้ง:

```python
LLM_MODEL = "qwen2.5:3b"
```

ผล:

- rule/direct answer เร็วมาก ระดับ 0.001-0.05 วินาที
- LLM-only ส่วนใหญ่ประมาณ 3-5 วินาทีใน targeted test

### 5.2 เพิ่ม Rule-Based Fast Path

ไฟล์:

```text
data/curated/rule_patterns.jsonl
scripts/rule_matcher.py
```

เป้าหมาย:

- คำถามซ้ำ/FAQ ไม่ต้องเข้า LLM
- ตอบเร็ว
- ลด hallucination
- ใช้แหล่งอ้างอิงชัดเจน

### 5.3 เพิ่มการแปลงหน่วยใน rule

เช่นคำถาม:

```text
เช็คอินล่วงหน้าได้กี่วินาที
```

จากเดิม rule ตอบแค่ 30 นาที ทำให้ดูไม่ตรงคำถาม  
ตอนนี้ `rule_matcher.py` มี `adapt_answer_to_query()`:

- ถ้าถามวินาที ตอบ `30 นาที หรือ 1,800 วินาที`
- ถ้าถามชั่วโมง ตอบ `0.5 ชั่วโมง หรือ 30 นาที`

### 5.4 เพิ่ม Direct RAG Answer

ปัญหาเดิม:

- retrieval ดึงเอกสารถูก แต่ LLM ตอบว่าไม่พบ
- หรือ LLM สรุปหลุดจาก context

จึงเพิ่ม `rag_direct_curated`:

- ถ้า retrieved hit เป็น `curated_fact`
- category ตรงกับ route
- คำถามเป็น fact/list ที่ชัด
- ตอบจาก text ใน curated fact โดยตรง ไม่เรียก LLM

### 5.5 แก้คำถาม "ศูนย์เปิดถึงกี่โมง / ปิดถึงกี่โมง"

ปัญหาเดิม:

- ข้อมูลมีแค่ schedule: Morning 09:00-12:00, Afternoon 13:00-16:00
- retrieval ดึง `curated_time_change_policy` ขึ้นก่อน ทำให้ตอบเรื่องเปลี่ยนเวลาแทน
- ถ้าปิด rule จะตอบไม่พบ

สิ่งที่แก้:

- เพิ่ม `rule_service_schedule`
- เพิ่ม route keyword
- เพิ่ม `schedule_boost`
- เพิ่ม direct fallback ให้หยิบ `curated_schedule_morning/afternoon`
- ปรับคำตอบให้ตรงตามที่ต้องการ:

```text
เปิด 09:00 น. และปิด 16:00 น.
โดยแบ่งรอบบริการเป็น Morning 09:00-12:00 และ Afternoon 13:00-16:00
```

ผล targeted test:

```text
answer_question("ปิดถึงกี่โมง")
mode: rule_fast_path
latency: 0.008s
```

### 5.6 กันโมเดลตอบปนภาษาจีน

เคยเจอ LLM-only ตอบไทยแต่มีท้ายภาษาจีน เช่น:

```text
根据提供的资料
```

สิ่งที่แก้:

- เพิ่ม system prompt: ห้ามปนภาษาที่สาม
- เพิ่ม `sanitize_model_answer()` เพื่อตัดอักษรจีนในคำตอบภาษาไทย

ผล Ground Truth:

```text
Chinese character leakage: 0
```

### 5.7 เพิ่ม Deterministic Calculator

คำถามตัวอย่าง:

```text
ถ้าจอง 9โมงถึง11โมง แบบเล่น PC ต้องเสียกี่บาท
```

ปัญหาเดิม:

- ระบบ RAG ไปดึงกฎจอง/ยกเลิกแทน
- ไม่มี calculator
- ไม่มีราคา PC ในฐานข้อมูล text
- LLM ตอบ `ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี`

สิ่งที่เช็ค:

- หน้าเว็บมี service list ผ่าน `https://esports.computing.psu.ac.th/wp-json/wbk/v2/get-preset`
- พบว่า PC มี duration `60 min`
- หน้าเว็บมีรูป `SERVICE-FEE-2026.png`
- รูป Service Fee มีราคา PlayStation/Nintendo/Cockpit/VR
- แต่ **ไม่มีราคา PC ในรูป**
- API service list บอก `PC payable=true` แต่ไม่ส่งราคา PC

สิ่งที่เพิ่ม:

- `SERVICE_PRICING`
- `parse_time_range_minutes()`
- `detect_pricing_service()`
- `detect_customer_group()`
- `calculate_service_price_answer()`
- mode ใหม่ `deterministic_calculator`

ผล targeted test:

```text
ถ้าจอง 9โมงถึง11โมง แบบเล่น PC ต้องเสียกี่บาท
-> 09:00-11:00 = 2 ชั่วโมง
-> PC รอบละ 60 นาที = 2 sessions
-> ยังไม่สามารถคำนวณยอดเงินบาทได้ เพราะยังไม่พบราคา PC
```

ตัวอย่างที่คำนวณได้:

```text
ถ้าจอง 9โมงถึง11โมง เล่น PlayStation บุคคลทั่วไปต้องเสียกี่บาท
-> 150 บาท/session x 2 = 300 บาท
```

```text
ถ้าจอง 9โมงถึง11โมง เล่น cockpit ศิษย์เก่าต้องเสียกี่บาท
-> 65 บาท/session x 2 = 130 บาท
```

## 6. Rule-Based มีอะไรบ้าง

ตอนนี้มี 27 rules

| ID | Category | Intent | ใช้ตอบเรื่อง |
|---|---|---|---|
| `rule_checkin_advance` | reservation | checkin_advance_time | เช็คอินล่วงหน้าได้กี่นาที/ชั่วโมง/วินาที |
| `rule_checkin_late` | reservation | late_checkin_cancel | ไม่เช็คอิน/เช็คอินไม่ทัน |
| `rule_booking_advance` | reservation | booking_advance_time | ต้องจองล่วงหน้าอย่างน้อยกี่ชั่วโมง |
| `rule_booking_max_sessions` | reservation | booking_max_sessions | จองได้สูงสุดกี่ sessions |
| `rule_payment_10_minutes` | reservation | payment_timeout | ไม่ชำระเงินใน 10 นาที |
| `rule_cancel_advance` | reservation | cancel_advance_time | ยกเลิกล่วงหน้ากี่ชั่วโมง |
| `rule_refund_policy` | reservation | refund_policy | คืนเงินไหม |
| `rule_edit_booking` | reservation | edit_booking | แก้ไขข้อมูลจองได้ไหม |
| `rule_payment_bank` | reservation | bank_account | เลขบัญชี/ธนาคาร |
| `rule_booking_steps` | reservation | booking_steps | ขั้นตอนการจอง |
| `rule_minor_damage` | penalty | minor_damage_fine | เสียหายเล็กน้อย/ค่าปรับ 100-500 บาท |
| `rule_moderate_damage` | penalty | moderate_damage_fine | เสียหายปานกลาง/500-2,000 บาท |
| `rule_severe_damage` | penalty | severe_damage_compensation | จอแตก/คอมพัง/ชดเชยเต็มจำนวน |
| `rule_smoking_alcohol` | rules | smoking_alcohol_rule | สูบบุหรี่/แอลกอฮอล์/สารเสพติด |
| `rule_food_drink` | rules | food_drink_rule | อาหาร/เครื่องดื่ม |
| `rule_weapons_gambling` | rules | weapons_gambling_rule | อาวุธ/ของมีคม/ทะเลาะ/การพนัน |
| `rule_ps5_games` | games | ps5_games | เกม PlayStation 5 |
| `rule_switch_games` | games | switch_games | เกม Nintendo Switch |
| `rule_pc_games` | games | pc_games | เกม PC |
| `rule_vr_games` | games | vr_games | เกม VR |
| `rule_contact_email` | contact | contact_email | อีเมลติดต่อ |
| `rule_contact_facebook` | contact | contact_facebook | Facebook |
| `rule_contact_location` | contact | contact_location | ที่ตั้ง |
| `rule_contact_phone` | contact | contact_phone | เบอร์โทร |
| `rule_service_schedule` | reservation | service_schedule | เปิด/ปิดกี่โมง/ตารางบริการ |
| `rule_overview_identity` | overview | studio_identity | PSU Esports Studio Phuket คืออะไร |
| `rule_overview_mission` | overview | studio_mission | Mission/พันธกิจ |

## 7. จุดที่ Rule-Based ทำให้ตอบมั่ว

Rule-based เร็ว แต่ถ้า pattern กว้างเกินจะจับผิด intent

### ตัวอย่าง 1: Knowledge โดน Overview Rule

คำถาม:

```text
Esports คืออะไร
```

หรือ:

```text
NARUTO X BORUTO ... ในบทความเกี่ยวกับอะไร
```

ปัญหา:

- มีคำว่า `คืออะไร` หรือ `เกี่ยวกับอะไร`
- ไป match `rule_overview_identity`
- ตอบว่า PSU Esports Studio คืออะไร แทนที่จะตอบความรู้/บทความ

ควรแก้:

- ทำ rule priority/context guard
- `คืออะไร` ไม่ควร match overview ถ้าคำถามมีคำว่า `Esports`, ชื่อเกม, `บทความ`, `Knowledge`
- เพิ่ม route category `knowledge`

### ตัวอย่าง 2: No Answer โดน Food Rule

คำถาม:

```text
มีบริการจัดส่งอาหารถึงโต๊ะเล่นเกมไหม
```

ปัญหา:

- มีคำว่า `อาหาร`
- ไป match `rule_food_drink`
- ตอบเรื่องกินอาหารในพื้นที่ที่กำหนด
- แต่คำถามจริงถามบริการจัดส่งอาหาร ซึ่งไม่มีข้อมูล

ควรแก้:

- เพิ่ม negative intent guard เช่น `จัดส่ง`, `delivery`, `ถึงโต๊ะ`
- ถ้าพบคำเหล่านี้ให้ตอบ no_answer หรือส่งเข้า RAG ก่อน rule

### ตัวอย่าง 3: Reservation ยกเลิกโดนผิด rule

คำถาม:

```text
การจองอาจถูกยกเลิกโดยไม่แจ้งล่วงหน้าในกรณีใด
```

ปัญหา:

- ไป match `rule_cancel_advance`
- ตอบแค่ยกเลิกล่วงหน้า 1 ชั่วโมง
- แต่ expected คือข้อมูลไม่ถูกต้อง/ไม่ปฏิบัติตามกฎ

ควรแก้:

- เพิ่ม rule เฉพาะ `booking_cancel_without_notice`
- pattern เช่น `ยกเลิกโดยไม่แจ้ง`, `without prior notice`

## 8. Ground Truth ล่าสุด

รันด้วย:

```powershell
py scripts\run_ground_truth_eval.py
```

ผลรวม:

```text
Total: 105
PASS: 38
FAIL: 67
ERROR: 0
Pass rate: 36.19%
Average latency: 0.871s
Keyword fail: 50
Source fail: 43
Answers containing "ไม่พบข้อมูล": 16
Chinese character leakage: 0
```

ไฟล์รายงาน:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\16_PSU_Esports_RAG_Experiment_Timeline\06_ground_truth_eval_2026-06-29.md
```

ไฟล์ผลลัพธ์ JSONL:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\16_PSU_Esports_RAG_Experiment_Timeline\ground_truth_eval_results_2026-06-29.jsonl
```

## 9. Ground Truth แยกตามหมวด

| Category | PASS | Total | Pass Rate |
|---|---:|---:|---:|
| reservation | 22 | 29 | 75.86% |
| contact | 4 | 5 | 80.00% |
| no_answer | 5 | 6 | 83.33% |
| overview | 3 | 5 | 60.00% |
| knowledge | 2 | 8 | 25.00% |
| games | 1 | 8 | 12.50% |
| rules | 1 | 18 | 5.56% |
| equipment | 0 | 8 | 0.00% |
| services | 0 | 3 | 0.00% |
| penalty | 0 | 5 | 0.00% |
| events_news | 0 | 5 | 0.00% |
| about_us | 0 | 5 | 0.00% |

สรุป:

- หมวดจอง/contact/no_answer เริ่มใช้ได้
- หมวด equipment/services/rules/penalty/news/about_us ยังต้องแก้ใหญ่

## 10. Ground Truth แยกตามโหมดคำตอบ

| Mode | PASS | Total | Pass Rate |
|---|---:|---:|---:|
| `rule_fast_path` | 19 | 43 | 44.19% |
| `rag_llm` | 10 | 27 | 37.04% |
| `rag_direct_curated` | 9 | 35 | 25.71% |

ตีความ:

- `rule_fast_path` เร็วที่สุด แต่ยังมี false positive เพราะ pattern กว้าง
- `rag_direct_curated` เร็วมาก แต่ถ้า retrieval ดึง curated fact ผิด ก็จะตอบผิดทันที
- `rag_llm` ช้ากว่า แต่บางครั้งช่วยสรุปจาก context ได้ดี ถ้า retrieval ถูก

## 11. ปัญหาตอบมั่วที่เจอจริง

### 11.1 ถามอุปกรณ์ แต่ตอบเกม

ตัวอย่าง:

```text
ศูนย์มี Gaming PC กี่เครื่อง
```

ได้ retrieval:

```text
curated_games_pc
curated_games_ps5
curated_games_popular
curated_games_switch
```

แล้วตอบรายการเกม PC แทนจำนวนเครื่อง

สาเหตุ:

- คำว่า `PC` ไปใกล้กับ curated games มากกว่า equipment
- ยังไม่มี curated fact แยก equipment ชัดพอ
- `home-01-001` ที่มีข้อมูล equipment ถูก category ผิด/ใหญ่เกิน

ควรแก้:

- เพิ่ม curated facts หมวด equipment เช่น:
  - `curated_equipment_pc_count`
  - `curated_equipment_pc_zone`
  - `curated_equipment_cockpit`
  - `curated_equipment_ps5`
  - `curated_equipment_vr`
- เพิ่ม route `equipment`
- เพิ่ม rule เฉพาะคำว่า `กี่เครื่อง`, `อุปกรณ์`, `zone`

### 11.2 ถาม services แต่ตอบเกม

ตัวอย่าง:

```text
PC แต่ละเครื่องให้บริการกี่นาที
```

ตอบรายการเกม PC แทน `60 min`

สาเหตุ:

- route `games` ชนกับคำว่า PC
- service duration อยู่ใน `reservation-01-015` แต่ retrieval ดึง `curated_games_pc`

ควรแก้:

- แยก curated service facts:
  - PC 60 min
  - Cockpit 60 min
  - Nintendo 60 min
  - PlayStation 60 min
  - VR 60 min / 30 min

### 11.3 ถาม rules แต่ตอบเกมหรือ rule อื่น

ตัวอย่าง:

```text
ยืมอุปกรณ์หรือแผ่นเกมแล้วต้องทำอะไรหลังใช้งาน
```

ดึง:

```text
curated_games_ps5
curated_games_pc
curated_games_switch
curated_games_vr
```

ตอบรายการเกม แทน `นำอุปกรณ์และแผ่นเกมมาคืน`

สาเหตุ:

- มีคำว่า `เกม`
- route/retrieval ไป games
- rules fact ยังไม่ชัดหรือไม่ได้ boost

ควรแก้:

- ถ้าคำถามมี `ยืม`, `คืน`, `แผ่นเกม`, `หลังใช้งาน` ให้ route ไป rules
- เพิ่ม rule `return_borrowed_equipment`

### 11.4 ถาม penalty แต่ตอบ rules ทั่วไป

ตัวอย่าง:

```text
ถ้าละเมิดกฎจะโดนอะไรบ้าง
```

ตอบ:

```text
ห้ามพกอาวุธ ห้ามทะเลาะ ห้ามเล่นการพนัน
```

แทนที่จะตอบ:

```text
คำเตือน, ระงับสิทธิ์ชั่วคราว, ระงับสิทธิ์ถาวร, ชดเชยค่าเสียหาย, บันทึกประวัติ
```

สาเหตุ:

- คำว่า `กฎ` ไปดึง rules มากกว่า penalty
- direct curated เลือก top hit เร็วเกิน

ควรแก้:

- route ถ้ามี `ละเมิด`, `โดนอะไร`, `ลงโทษ`, `ระงับสิทธิ์`, `อุทธรณ์` ให้ไป `penalty`
- เพิ่ม penalty rules เฉพาะ

### 11.5 ถาม News/About Us แล้วตอบไม่พบ

ตัวอย่าง:

```text
ใครเป็นอธิการบดีที่ปรากฏในหน้าสมาชิก
```

ตอบไม่พบ

สาเหตุ:

- about/members data ยังไม่ได้ทำ curated facts
- category routing ยังไม่รู้จัก `สมาชิก`, `อธิการบดี`, `คณบดี`, `ประธาน`
- source อาจอยู่ใน About Us แต่ retrieval ไป home/contact/news

ควรแก้:

- เพิ่ม curated facts หมวด about_us/members
- route category `about_us`

## 12. ปัญหาที่เป็น False Fail จาก Evaluation

บางข้อใน Ground Truth fail เพราะ source keyword strict ไม่ตรง แต่คำตอบจริงถูก

ตัวอย่าง:

- `games_002` ตอบ PS5 games ถูก แต่ source keyword expected คือ `Reservation`
- rule source เป็น `rule_ps5_games` จึงไม่เจอคำว่า Reservation

แนวทางแก้:

- ใน eval ให้ source check ดู `source_ids` ด้วย
- หรือ map rule id ไป source id เช่น `rule_ps5_games -> curated_games_ps5 -> Reservation`
- หรือแยกคะแนนเป็น:
  - `answer_keyword_ok`
  - `source_ok`
  - `semantic_ok/manual_review`

## 13. ราคาและ Calculator

### แหล่งราคาที่พบ

ไฟล์รูป:

```text
data/raw/SERVICE-FEE-2026.png
```

URL:

```text
https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
```

ราคาที่อ่านจากรูป:

| Service | PSU Student/Staff | PSU Alumni/General Student | General Adult |
|---|---:|---:|---:|
| PlayStation 5 - 1 HR (1-2 persons) | Free | 50 THB | 150 THB |
| Nintendo Switch - 1 HR (1-2 persons) | Free | 50 THB | 140 THB |
| Nintendo Switch - 1 HR (3-4 persons) | Free | 100 THB | 280 THB |
| Cockpit - 1 HR (1 person) | Free | 65 THB | 200 THB |
| VR - 30 MINS (1-5 persons) | Free | 190 THB | 525 THB |
| VR - 1 HR (1-5 persons) | Free | 375 THB | 1050 THB |
| PC | ยังไม่พบ | ยังไม่พบ | ยังไม่พบ |

### ปัญหาราคา PC

เว็บมี service:

```text
PC #01 - PC #10
duration: 60 min
payable: true
```

แต่:

- รูป Service Fee 2026 ไม่มีราคา PC
- endpoint `get-preset` ไม่มี price
- endpoint ลึกกว่านี้บางอัน 401/500
- จึงยังไม่ควรให้ AI เดาราคา PC

### Behavior ปัจจุบัน

ถ้าถาม PC:

```text
ถ้าจอง 9โมงถึง11โมง แบบเล่น PC ต้องเสียกี่บาท
```

ตอบ:

```text
09:00-11:00 = 2 ชั่วโมง
PC รอบละ 60 นาที = 2 sessions
ยังคำนวณยอดเงินบาทไม่ได้ เพราะยังไม่พบราคา PC
```

ถ้าถาม PlayStation/Cockpit/VR/Nintendo:

```text
ถ้าจอง 9โมงถึง11โมง เล่น PlayStation บุคคลทั่วไปต้องเสียกี่บาท
```

ตอบ:

```text
150 บาท/session x 2 = 300 บาท
```

## 14. จุดแข็งตอนนี้

- ตอบ FAQ จอง/เช็คอิน/คืนเงิน/เวลาเปิดปิด ได้เร็วมาก
- มี log ทุกคำถามใน `logs/chat_log.jsonl`
- มี ground truth 105 ข้อ
- มี evaluation script แล้ว
- มี rule-based + direct RAG + LLM fallback
- มี deterministic calculator สำหรับราคาที่รู้จริง
- ลดปัญหา LLM ตอบจีนปนแล้ว
- มีไฟล์รายงาน timeline แยกเป็นลำดับการทดลอง

## 15. จุดอ่อนตอนนี้

- Pass rate รวมยังต่ำ: 36.19%
- Category ของ chunk หลายตัวผิด ทำให้ retrieval ผิด
- Direct curated answer เร็วแต่เสี่ยงตอบผิดถ้า top hit ผิด
- Rule patterns บางอันกว้างเกิน เช่น `คืออะไร`, `อาหาร`, `กฎ`
- Equipment/services ยังไม่มี curated facts ที่ดีพอ
- About Us/News ยังไม่ได้ curate เป็น facts
- ราคา PC ยังไม่มีข้อมูลตัวเลข
- Evaluation เป็น keyword strict ทำให้บางคำตอบที่ถูกความหมาย fail ได้

## 16. สิ่งที่ควรแก้ต่อ ตามลำดับความคุ้ม

### Priority 1: แก้ Equipment + Services

เหตุผล:

- ตอนนี้ 0/8 และ 0/3
- เป็นข้อมูล fact ชัด แก้ง่ายและเพิ่ม pass rate ได้เร็ว

ต้องเพิ่ม curated facts:

- จำนวน Gaming PC: MSI MAG Infinite S3 14th 10 Units
- PC Zone มี Gaming Monitor/Chair/Keyboard/Headset/Mouse/PC
- Cockpit Zone มี Logitech G923, Driving Force Shifter, Racezone Full Cockpit
- TV 65 2 Units
- TV 86 1 Unit
- Nintendo Switch OLED model Neon Red Neon Blue set 1 Unit
- PlayStation 5 Slim 2 Units
- VR: PlayStation 5 Slim 1 Unit, Sony PlayStation VR2 1 Unit
- service duration: PC 60 min, VR 60/30 min, etc.

### Priority 2: แก้ Rules + Penalty

เพิ่ม rules เฉพาะ:

- return borrowed equipment/game discs
- trash rule
- noise/offensive language
- move equipment without permission
- personal electronics without permission
- lost item responsibility
- report issue to staff
- violation penalties summary
- temporary suspension 1-7 days
- permanent suspension conditions
- appeal within 7 days
- violation record

### Priority 3: ลด False Positive ของ Rule-Based

เพิ่ม guard:

- ถ้าคำถามมี `บทความ`, `Knowledge`, ชื่อเกม ให้ไม่ใช้ overview rule
- ถ้ามี `จัดส่งอาหาร`, `delivery`, `ถึงโต๊ะ` ให้ไม่ใช้ food rule
- ถ้ามี `ยกเลิกโดยไม่แจ้ง` ให้ใช้ rule เฉพาะ ไม่ใช้ cancel advance

### Priority 4: แก้ Category Inference/Optimized Chunks

ต้องปรับ `scripts/optimize_content.py` หรือ curated metadata ให้:

- Home -> overview/equipment/rules แยก chunk ย่อย
- Reservation -> schedule/reservation/rules/penalty/services แยก chunk ย่อย
- Events and News -> events_news
- Knowledge -> knowledge
- About Us -> about_us

### Priority 5: ปรับ Evaluation

แยกคะแนน:

- `keyword_ok`
- `source_ok`
- `mode_ok`
- `manual_semantic_ok`

และ source check ควรเข้าใจ rule source:

```text
rule_ps5_games -> curated_games_ps5 -> Reservation
```

### Priority 6: ราคา PC

ต้องถามพี่/ศูนย์:

- PC ราคาเท่าไหร่ต่อ 60 นาที สำหรับแต่ละกลุ่มผู้ใช้
- PSU Student/Staff ฟรีไหม
- ศิษย์เก่า/General Student กี่บาท
- General Adult กี่บาท

เมื่อได้แล้วเพิ่มใน notebook:

```python
SERVICE_PRICING["pc"]["rates"] = {
    "psu": ...,
    "alumni_student": ...,
    "adult": ...,
}
```

## 17. คำสั่งที่ใช้บ่อย

เปิด Ollama:

```powershell
& "C:\Users\Chokhun\AppData\Local\Programs\Ollama\ollama.exe" serve
```

เช็ค model:

```powershell
ollama list
```

รัน smoke test:

```powershell
cd C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B
py scripts\run_smoke_tests.py
```

รัน ground truth:

```powershell
cd C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B
py scripts\run_ground_truth_eval.py
```

เช็ค rule:

```powershell
$env:PYTHONIOENCODING="utf-8"
py scripts\rule_matcher.py "ปิดถึงกี่โมง"
```

## 18. วิธีทดสอบใน Notebook

หลัง Restart Kernel ให้ Run All หรือรัน cell ที่โหลด config/records/index/rules/functions ใหม่

เช็ค rule count:

```python
print(len(RULES))
```

ควรได้:

```text
27
```

ทดสอบเวลาเปิด-ปิด:

```python
answer, hits, elapsed = answer_question("ปิดถึงกี่โมง")
print(elapsed)
print([h["id"] for h in hits])
print(answer)
```

ทดสอบ calculator:

```python
answer, hits, elapsed = answer_question("ถ้าจอง 9โมงถึง11โมง เล่น PlayStation บุคคลทั่วไปต้องเสียกี่บาท")
print(elapsed)
print([h["id"] for h in hits])
print(answer)
```

ทดสอบ RAG โดยไม่ใช้ rule:

```python
answer, hits, elapsed = answer_question("ศูนย์นี้เกี่ยวกับอะไร", use_rules=False)
print(elapsed)
print([h["id"] for h in hits])
print(answer)
```

ทดสอบ LLM-only:

```python
answer, hits, elapsed = answer_question("ศูนย์นี้เกี่ยวกับอะไร", use_rules=False, use_direct=False)
print(elapsed)
print([h["id"] for h in hits])
print(answer)
```

## 19. สรุปสถานะ MVP

ตอนนี้ระบบอยู่ในสถานะ:

```text
MVP functional prototype
```

แปลว่า:

- รัน local ได้
- ถามตอบ RAG ได้
- FAQ หลักบางส่วนตอบเร็วมาก
- มี ground truth/eval แล้ว
- เห็นปัญหาชัดว่าต้องแก้ข้อมูลและ routing ต่อ

ยังไม่ควรมองว่า production-ready เพราะ:

- pass rate ยังต่ำ
- หมวดอุปกรณ์/กฎ/โทษ/news/about ยังผิดเยอะ
- PC price ยังไม่ครบ
- ยังไม่มี UI/FB integration จริง
- ยังไม่มี Docker app ที่ end-to-end พร้อม deploy

## 20. ข้อเสนอสำหรับ Phase ถัดไป

### Phase 1.1 - เพิ่ม Accuracy เร็วที่สุด

เป้าหมาย: ดัน pass rate จาก 36% ไป 60-70%

ทำ:

- เพิ่ม curated facts equipment/services/rules/penalty
- เพิ่ม route guards
- ปรับ rule false positives
- rerun ground truth

### Phase 1.2 - Pricing Calculator

เป้าหมาย: ตอบคำถามราคาได้ถูก

ทำ:

- ขอราคา PC official
- เพิ่ม service fee facts เป็น JSON
- แยก customer group ให้ชัด
- รองรับคำถามเวลา เช่น 9-11, 09:30-11:00, 1 ชั่วโมงครึ่ง
- เช็ค maximum 3 sessions
- เช็คเวลานอกช่วงเปิดบริการ

### Phase 1.3 - Chatbot API

เป้าหมาย: พร้อมต่อ Facebook

ทำ:

- แยก notebook logic เป็น Python module
- ทำ FastAPI endpoint `/chat`
- เก็บ log
- ทำ Dockerfile/docker-compose
- ต่อ webhook Facebook Messenger

### Phase 2 - Production Readiness

ทำ:

- Auth/admin สำหรับเพิ่มกฎใหม่
- Upload PDF/Image แล้ว OCR/parse เข้า knowledge base
- Evaluation dashboard
- Monitor hallucination/no-answer
- Manual review feedback loop

## 21. บทเรียนหลักจากการทดลอง

1. RAG ไม่ได้แปลว่าจะคำนวณได้ ต้องมี calculator/tool แยก
2. Rule-based เร็วมาก แต่ถ้า pattern กว้างจะตอบมั่วเร็วมากเหมือนกัน
3. Direct curated answer ดีมากสำหรับ FAQ/fact แต่ต้องมั่นใจว่า retrieval ถูก
4. Chunk/category สำคัญมาก ถ้า category ผิด retrieval จะพังต่อเนื่อง
5. Ground truth ทำให้เห็นปัญหาจริง ไม่ใช่แค่ลองถาม 2-3 ข้อแล้วคิดว่าดี
6. ข้อมูลที่เป็นรูปภาพ เช่น Service Fee ถ้าไม่ OCR/curate จะไม่มีใน RAG
7. ไม่ควรให้ LLM เดาราคา กฎ หรือเงื่อนไขการจอง ควรตอบว่าไม่พบหรือใช้ structured data เท่านั้น

