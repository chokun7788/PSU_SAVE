# Data Quality Audit - PSU Esports Local RAG

วันที่ตรวจสอบ: 2026-06-29  
โฟกัสรอบนี้: ตรวจว่า AI ตอบผิดเพราะ Data / Category / Chunk / Format หรือ Retrieval pipeline ตรงไหน

## สรุปสั้นที่สุด

ตอนนี้สาเหตุหลักที่ตอบผิด **ไม่ใช่เพราะ LLM อย่างเดียว** แต่เกิดจาก Data pipeline เป็นหลัก โดยเฉพาะ 3 จุดนี้:

1. **Chunk ยาวเกินมาก**  
   ตั้งใจให้ chunk ไม่เกิน `900` ตัวอักษร แต่ข้อมูลจริงมี chunk ยาวถึง `29,503`, `19,884`, `13,303` ตัวอักษร เพราะตัวแบ่ง chunk ไม่ได้แยกตามบรรทัด/หัวข้อจริง

2. **Category ผิดหรือกว้างเกิน**  
   เช่น `Home` ถูกจัดเป็น `penalty`, `Reservation` ถูกจัดเป็น `penalty`, `Services / Our Games` ถูกจัดเป็น `games`, `Events and News / News` ถูกจัดเป็น `rules` ทำให้ query filter ไปหมวดผิดหรือดึง source ผิด

3. **ข้อมูลมีอยู่ แต่ RAG มองไม่เห็นตอนตอบ**  
   Notebook ตัด source ละ `750` ตัวอักษร (`MAX_DOC_CHARS = 750`) ถ้าคำตอบอยู่หลังตัวอักษรที่ 750 LLM จะไม่เห็น แม้ retrieval จะดึง chunk ถูกมาก็ตาม

จาก Ground Truth ล่าสุด:

- Total: `105`
- PASS: `38`
- FAIL: `67`
- Pass rate: `36.19%`

Breakdown ของ 67 ข้อที่ผิด:

| Cause | Count | ความหมาย |
|---|---:|---|
| `data_present_but_long_chunk_or_retrieval_miss` | 32 | ข้อมูลมีในฐาน แต่ chunk ยาว/หมวดผิด/ดึงผิด source |
| `data_present_but_trimmed_after_750_chars` | 10 | ดึง source ได้ แต่คำตอบอยู่หลัง 750 ตัวอักษรเลยถูกตัดทิ้ง |
| `source_check_only_or_eval_strict` | 17 | คำตอบอาจถูก แต่ evaluation เช็ก source เข้มเกิน โดยเฉพาะ rule-based |
| `data_present_but_retrieval_or_category_miss` | 7 | ข้อมูลมี แต่ route/category/retrieval พาไปผิดทาง |
| `missing_or_not_explicit_in_data` | 1 | ไม่มีข้อมูลตรงคำถาม หรือ rule ตีความกว้างเกิน |

สรุปเชิง root cause: **ประมาณ 42/67 ข้อที่ fail เกี่ยวกับ chunk/retrieval/context โดยตรง** ไม่ใช่ว่าข้อมูลไม่มี

## ไฟล์ที่ตรวจ

Project:

`C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B`

ไฟล์ Data:

- `data\raw\all_sections_rag_chunks.jsonl`
- `data\raw_sections\*\section_text.txt`
- `data\curated\curated_facts.jsonl`
- `data\curated\rule_patterns.jsonl`
- `data\processed\optimized_chunks.jsonl`
- `data\processed\chunks_clean.jsonl`
- `ground_truth\ground_truth_full.jsonl`
- `data\vector_db\chroma_psu_esports\chroma.sqlite3`

ไฟล์ผลทดสอบ:

- `C:\Users\Chokhun\Downloads\Learn-LLM\16_PSU_Esports_RAG_Experiment_Timeline\ground_truth_eval_results_2026-06-29.jsonl`
- `C:\Users\Chokhun\Downloads\Learn-LLM\16_PSU_Esports_RAG_Experiment_Timeline\06_ground_truth_eval_2026-06-29.md`

## 1. JSONL / Format Check

ผลตรวจ JSONL:

| File | Rows | Bad JSON | Duplicate ID | สถานะ |
|---|---:|---:|---:|---|
| `raw/all_sections_rag_chunks.jsonl` | 191 | 15 | 0 | มีปัญหา |
| `curated/curated_facts.jsonl` | 42 | 0 | 0 | OK |
| `curated/rule_patterns.jsonl` | 27 | 0 | 0 | OK |
| `processed/optimized_chunks.jsonl` | 69 | 0 | 0 | OK |
| `processed/chunks_clean.jsonl` | 69 | 0 | 0 | OK |
| `ground_truth/ground_truth_full.jsonl` | 105 | 0 | 0 | OK |
| `ground_truth_eval_results_2026-06-29.jsonl` | 105 | 0 | 0 | OK |

### ปัญหาของ raw JSONL

ไฟล์ `all_sections_rag_chunks.jsonl` มี bad JSON 15 จุด สาเหตุที่เห็นคือมีตัวแบ่งบรรทัดพิเศษอยู่ใน string เช่นเนื้อหากลุ่ม penalty / suspension ทำให้ reader แบบ `splitlines()` มองว่า JSON หนึ่ง record แตกเป็นหลายบรรทัด

ผลกระทบ:

- ถ้าใช้ parser ปกติแบบอ่านทีละบรรทัด จะอ่าน raw data บางส่วนไม่ได้
- Notebook มี `parse_jsonl_loose()` เลยช่วยกู้ได้บางกรณี
- แต่ตอนนี้ notebook เลือกใช้ `optimized_chunks.jsonl` ก่อน raw อยู่แล้ว ดังนั้นปัญหานี้ไม่ใช่สาเหตุหลักของคำตอบล่าสุด แต่เป็น data-risk ที่ควรแก้

ข้อเสนอ:

- regenerate raw JSONL ด้วย `json.dumps(..., ensure_ascii=False)` และต้อง escape newline/line separator ให้ถูก
- หลีกเลี่ยงการเก็บ raw text ที่มี Unicode line separator แบบ literal ใน JSONL
- เพิ่ม validation step หลัง scrape ทุกครั้ง

## 2. Chunking ผิดจุดหลัก

ตั้งค่าใน `scripts\optimize_content.py`:

- `MAX_CHARS = 900`
- `OVERLAP_ITEMS = 2`

แต่ผลจริงใน `optimized_chunks.jsonl`:

| Metric | Value |
|---|---:|
| Total chunks | 69 |
| Min length | 43 |
| Median length | 170 |
| P90 length | 3986 |
| Max length | 29503 |
| Chunks > 900 chars | 23 |
| Chunks > 1500 chars | 19 |
| Chunks > 3000 chars | 14 |
| Chunks > 5000 chars | 5 |
| Chunks > 10000 chars | 3 |

Chunk ที่ยาวผิดปกติ:

| ID | Section | Category | Length | ปัญหา |
|---|---|---|---:|---|
| `events-and-news-01-001` | Events_and_News | rules | 29503 | รวมข่าวจำนวนมากไว้ใน chunk เดียว |
| `services-01-001` | Services | games | 19884 | รวมรายชื่อเกม/บริการ/แกลเลอรีไว้ยาวมาก |
| `reservation-01-001` | Reservation | penalty | 13303 | รวมกฎการจอง กฎใช้งาน penalty ราคา เกม ติดต่อ ไว้ก้อนเดียว |
| `knowledge-02-001` | Knowledge | knowledge | 5945 | บทความยาวทั้งหน้า |
| `knowledge-04-001` | Knowledge | knowledge | 5031 | บทความยาวทั้งหน้า |
| `home-01-001` | Home | penalty | 4175 | รวม overview + equipment + rules แล้วโดนติดหมวด penalty |

### สาเหตุจริงในโค้ด

ใน `optimize_content.py` ฟังก์ชัน `split_items()` แยก item ด้วย pattern:

```python
re.split(r"\s+\|\s+", text)
```

แต่ `raw_sections/*/section_text.txt` ส่วนใหญ่ไม่ได้มี ` | ` เป็นตัวแบ่ง semantic จริง ทำให้ 1 page = 1 item ขนาดใหญ่มาก

ผลตรวจ raw section:

| Section | File length | Pages | Max item length | หมายเหตุ |
|---|---:|---:|---:|---|
| About_Us | 6222 | 3 | 3986 | page ใหญ่ยังไม่ถูกแตก |
| Contact_Us | 708 | 1 | 707 | พอใช้ได้ |
| Events_and_News | 34410 | 5 | 29511 | news page ใหญ่มาก |
| Home | 4177 | 1 | 4176 | equipment อยู่ก้อนเดียว |
| Knowledge | 44099 | 14 | 5945 | บทความละก้อนใหญ่ |
| Reservation | 13304 | 1 | 13303 | ใหญ่มากและปนหลายเรื่อง |
| Services | 20401 | 2 | 19884 | ใหญ่มากและปนหลายเรื่อง |

อีกจุดคือ `chunk_items()` ไม่ hard split ถ้า item เดียวเกิน `MAX_CHARS`:

```python
if current and current_len + item_len > max_chars:
    chunks.append(...)
current.append(item)
```

ถ้า `current` ยังว่างและ `item` ยาว 10,000 ตัวอักษร มันจะ append item ทั้งก้อนทันที จึงเกิด chunk ยาวมาก

ข้อเสนอ:

- แก้ `split_items()` ให้แยกตาม newline, heading, bullet, numbered list, วันที่ข่าว, service block
- เพิ่ม hard split สำหรับ item ที่ยาวเกิน `MAX_CHARS`
- ใช้ structure-aware chunking:
  - Reservation: แยก `booking policy`, `check-in`, `cancellation`, `rules`, `penalty`, `bank account`, `game list`
  - Services: แยกตาม service เช่น `PC`, `PS5`, `Nintendo`, `Cockpit`, `VR`
  - Home: แยก `overview`, `equipment zone`, `mission`, `facility`
  - News: แยกข่าวละ 1 chunk
  - About: แยก `members`, `club committee`, `gallery`, `download`

## 3. Context ถูกตัด ทำให้ข้อมูลมีแต่ตอบไม่ได้

ใน notebook:

- `MAX_CONTEXT_CHARS = 3200`
- `MAX_DOC_CHARS = 750`
- `TOP_K = 4`

ฟังก์ชัน `trim_doc_text()` ตัด source แต่ละอันเหลือ 750 ตัวอักษรแรก:

```python
return text[:max_chars].rstrip() + "..."
```

ดังนั้นถ้าข้อมูลอยู่ท้าย chunk จะหายจาก context ที่ส่งให้ LLM

ตัวอย่างตำแหน่งข้อมูลสำคัญ:

| ข้อมูล | อยู่ใน chunk | Position | เห็นใน 750 แรกไหม |
|---|---|---:|---|
| `TV 65` | `home-01-001` | 915 | ไม่เห็น |
| `Logitech G923` | `home-01-001` | 938 | ไม่เห็น |
| `TV 86` | `home-01-001` | 1141 | ไม่เห็น |
| `Gaming Monitor` | `home-01-001` | 1267 | ไม่เห็น |
| `MSI MAG` | `home-01-001` | 1368 | ไม่เห็น |
| `PlayStation VR2` | `home-01-001` | 1582 | ไม่เห็น |
| `Service Fee` | `reservation-01-001` | 1675 | ไม่เห็น |
| `SURAT SMASH` | `events-and-news-01-001` | 1047 | ไม่เห็น |
| `Game-based Learning` | `events-and-news-01-001` | 1804 | ไม่เห็น |
| `VALORANT 2026` | `events-and-news-01-001` | 1965 | ไม่เห็น |

ผลกระทบ:

- คำถามอุปกรณ์ เช่น PC กี่เครื่อง, Nintendo TV กี่นิ้ว, VR มีอะไร ตอบผิด เพราะข้อมูลอยู่ใน `home-01-001` แต่เกิน 750 ตัวแรก
- คำถามข่าว เช่น VALORANT / SURAT SMASH อาจไม่พบข้อมูล เพราะอยู่ท้าย chunk ข่าวยาว 29k
- คำถามราคา/Service Fee อยู่หลัง 750 ใน reservation chunk จึงไม่เหมาะกับ RAG แบบ context สั้น

ข้อเสนอ:

- แก้ chunking ก่อน ไม่ควรเพิ่ม `MAX_DOC_CHARS` อย่างเดียว
- ถ้าต้องทำระยะสั้น ให้ใช้ snippet extraction หลัง retrieve: ตัด context รอบ keyword/query แทนตัดหัว chunk เสมอ
- ใช้ `parent-child retrieval`: embed child chunk สั้น แต่ตอบพร้อม parent metadata/source

## 4. Category ผิดจาก keyword rule

ใน `optimize_content.py` category ถูก infer ด้วย keyword แบบเรียงลำดับ:

```python
if "ค่าปรับ" / "ชดเชย" / "เสียหาย" / "damage":
    return "penalty"
if "กฎ" / "ห้าม" / "rules":
    return "rules"
if "ps5" / "nintendo" / "vr" / "pc #" / "เกม":
    return "games"
if "เช็คอิน" / "จอง" / "ชำระ":
    return "reservation"
```

ปัญหา:

- ถ้า chunk ปนหลายเรื่อง แล้วมีคำว่า `เสียหาย` นิดเดียว ทั้ง chunk จะกลายเป็น `penalty`
- ถ้า chunk มีคำว่า `เกม` ทั้งก้อนจะกลายเป็น `games`
- category ไม่ได้อิง section/heading ย่อย แต่ดูทั้งก้อน

ตัวอย่าง category ที่ผิดหรือทำให้ retrieval เสี่ยง:

| Chunk | Section | Category ปัจจุบัน | ควรเป็น |
|---|---|---|---|
| `home-01-001` | Home | penalty | overview / equipment / facility แยกย่อย |
| `reservation-01-001` | Reservation | penalty | reservation / rules / penalty / payment / games แยกย่อย |
| `services-01-001` | Services | games | services_games / game_list / equipment_usage |
| `events-and-news-01-001` | Events_and_News | rules | events_news |
| `knowledge-05-001` | Knowledge | rules | knowledge |

อีกปัญหาคือ `route_category()` ใน notebook มี category vocabulary ไม่ตรงกับ data:

- query ที่มี `อุปกรณ์` ถูก route ไป `games`
- query การแข่งขันถูก route ไป `competition` แต่ processed data ใช้ `events_news` ไม่ใช่ `competition`
- ไม่มี route/category สำหรับ `equipment`, `services`, `price`, `about_us`, `events_news` แบบชัดเจน

ผลกระทบ:

- ถาม `ใน PC Zone มีอุปกรณ์อะไรบ้าง` แล้ว route ไป `games`
- ดึง `curated_games_pc` มาแทนที่จะดึงข้อมูลอุปกรณ์ใน Home
- ถามข่าวหรือ member อาจไปดึง overview/games/contact เพราะ route ไม่ตรงหมวดจริง

ข้อเสนอ:

- เพิ่ม category หลักที่ตรงกับ use case:
  - `overview`
  - `equipment`
  - `reservation`
  - `booking_rules`
  - `studio_rules`
  - `penalty`
  - `games`
  - `service_fee`
  - `events_news`
  - `about_members`
  - `contact`
- เปลี่ยน infer category ให้ใช้ section + heading + local block ไม่ใช่ keyword ทั้ง page
- เพิ่ม `category_confidence` หรือ `tags` หลายค่า แทน category เดียวเมื่อจำเป็น

## 5. Curated Facts ยังไม่ครอบคลุม Data ที่ถามบ่อย

ตอนนี้ curated facts มี 42 record และช่วยให้ตอบเร็วมาก แต่ยัง bias ไปที่:

- reservation
- rules
- penalty
- games
- contact
- overview

สิ่งที่ยังขาดหรือไม่ละเอียดพอ:

- `equipment` เช่น PC กี่เครื่อง, รุ่นอะไร, zone ไหนมีอุปกรณ์อะไร
- `service_fee` เช่น ราคาแต่ละ service ตามกลุ่มผู้ใช้
- `events_news` เช่น ข่าว tournament แต่ละวัน
- `about_members` เช่น คณบดี, ผู้จัดการ, สโมสร, รายชื่อสมาชิก
- `knowledge` แบบ Q&A ย่อย เช่น esports เกิดที่ไหน, อาชีพอะไรบ้าง

ตัวอย่างที่ผิดเพราะ curated ไม่ครอบ:

- `equipment_001`: ถาม Gaming PC กี่เครื่อง แต่ดึง `curated_games_pc`
- `equipment_002`: ถามอุปกรณ์ PC Zone แต่ตอบรายชื่อเกม PC
- `equipment_007`: ถาม PlayStation 5 กี่เครื่อง แต่ตอบรายชื่อเกม PS5
- `news_001`: ถามข่าววันที่ 25 เมษายน 2569 แต่ดึง curated games

ข้อเสนอ:

- ทำ `curated_facts_equipment.jsonl` หรือเพิ่มเข้า `curated_facts.jsonl`
- ทำ `curated_facts_service_fee.jsonl`
- ทำ `curated_facts_events_news.jsonl`
- ทำ `curated_facts_about_members.jsonl`
- ทุก curated fact ควรมี field:
  - `id`
  - `category`
  - `title`
  - `question_aliases`
  - `text`
  - `source_url`
  - `source_ids`
  - `effective_date`
  - `confidence`

## 6. Rule-based มีประโยชน์ แต่ pattern บางอันกว้างเกิน

Rule-based ทำให้ตอบเร็วมาก เหมาะกับ FAQ ซ้ำ ๆ เช่น:

- เปิดกี่โมง / ปิดกี่โมง
- เช็คอินล่วงหน้าได้กี่นาที
- ยกเลิกล่วงหน้ากี่ชั่วโมง
- PS5 มีเกมอะไร
- เบอร์ติดต่อ / Facebook / Email

แต่ตอนนี้ pattern บางตัวกว้างเกิน เช่น:

| Rule | Pattern ที่เสี่ยง | ปัญหา |
|---|---|---|
| `rule_overview_identity` | `คืออะไร` | คำถาม knowledge หลายแบบมีคำว่า "คืออะไร" ได้ |
| `rule_food_drink` | `อาหาร`, `เครื่องดื่ม` | คำถาม "มีบริการจัดส่งอาหารไหม" ถูกตอบเป็นกฎอาหาร |
| `rule_service_schedule` | `เปิดกี่โมง`, `ปิดกี่โมง` | ใช้ได้ดี แต่ควรแยก intent เปิด/ปิดให้ตอบตรง |
| `rule_cancel_advance` | `ยกเลิก.*กี่ชั่วโมง` | ใช้ได้ แต่ต้องแยกกรณีถาม consequence/no-show |

เคสที่เห็นชัด:

คำถาม:

`มีบริการจัดส่งอาหารถึงโต๊ะเล่นเกมไหม`

สิ่งที่ควรตอบ:

`ไม่พบข้อมูลเรื่องบริการจัดส่งอาหารถึงโต๊ะเล่นเกมในฐานข้อมูลที่มี`

สิ่งที่ตอบ:

`อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น`

สาเหตุ:

- pattern `อาหาร` ใน `rule_food_drink` กว้างเกิน
- ไม่มี negative intent / no-answer guard

ข้อเสนอ:

- เพิ่ม intent guard เช่น ถ้าคำถามมี `จัดส่ง`, `delivery`, `ถึงโต๊ะ`, `สั่งอาหาร` และไม่มี data ให้ตอบ no-answer
- Rule ต้องมี `required_terms` และ `forbidden_terms`
- อย่าใช้ pattern เดี่ยวสั้นเกินไป เช่น `อาหาร` โดยไม่มีบริบท

ตัวอย่างโครง rule ที่ควรใช้:

```json
{
  "id": "rule_food_drink",
  "intent": "food_drink_rule",
  "required_any": ["อาหาร", "เครื่องดื่ม", "กินข้าว", "กินน้ำ"],
  "forbidden_any": ["จัดส่ง", "delivery", "ถึงโต๊ะ", "สั่งอาหาร"],
  "answer_th": "อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น"
}
```

## 7. Evaluation strict เกินสำหรับ rule-based

Ground Truth บางข้อ fail เพราะ source check ไม่รองรับ rule-based ดีพอ

ตัวอย่าง:

- `games_002`: PS5 มีเกมอะไรบ้าง
- `games_006`: PC มีเกมอะไรให้เล่นบ้าง
- `rules_001`: ศูนย์ให้รับประทานอาหารและเครื่องดื่มตรงไหน

คำตอบจริงอาจถูก แต่ evaluation ต้องการ source keyword เช่น `reservation` ใน retrieved hits ขณะที่ hit เป็น:

- `rule_ps5_games`
- `rule_pc_games`
- `rule_food_drink`

ใน `run_ground_truth_eval.py` ฟังก์ชัน `source_status()` ตรวจเฉพาะ:

- `id`
- `metadata.title`
- `metadata.category`
- `metadata.source_url`

แต่ไม่ได้ตรวจ `metadata.source_ids` ที่ rule hit เก็บไว้

ผลคือ rule-based ที่ตอบถูกอาจถูกนับ fail เพราะ source ไม่ตรง format ที่ eval คาด

ข้อเสนอ:

- แก้ `source_status()` ให้รวม `metadata.source_ids`
- หรือให้ `rule_match_to_hit()` ส่ง source id จริงเป็น retrieved hits เพิ่มอีกชั้น
- แยก score เป็น:
  - answer correctness
  - source correctness
  - citation format correctness

## 8. คำถามคำนวณราคา PC ผิดเพราะอะไร

เคส:

`ถ้าจอง 9โมงถึง11โมง แบบเล่น PC ต้องเสียกี่บาท`

ตอนนี้ calculator parse ได้ว่า:

- 09:00 ถึง 11:00 = 2 ชั่วโมง
- PC session = 60 นาที
- จำนวน session = 2

แต่ตอบราคาสุดท้ายไม่ได้ เพราะ `SERVICE_PRICING` ใน notebook ไม่มี key `pc`

ตอนนี้มี rate สำหรับ:

- PS5
- Nintendo
- Cockpit
- VR 30 นาที
- VR 1 ชั่วโมง

แต่ไม่มี:

- PC Game Station

ใน curated data ก็มีแค่:

- `curated_games_pc`: รายชื่อเกม PC

ไม่มี:

- ราคา PC ต่อ session
- ราคาแยกตามกลุ่มผู้ใช้
- เงื่อนไขฟรี/เสียเงินของ PC

สรุป: **ผิดเพราะข้อมูลราคา PC ยังไม่ครบใน structured data** ไม่ใช่เพราะสูตรคำนวณอย่างเดียว

ข้อเสนอ:

- ต้องดึง/ยืนยันราคา PC จากแหล่งจริงก่อน
- เพิ่ม `service_fee` structured data เช่น:

```json
{"service": "pc", "duration_min": 60, "rates": {"psu": 0, "alumni_student": 0, "adult": 0}, "source": "...", "verified": false}
```

ถ้ายังไม่รู้ราคา:

```json
{"service": "pc", "duration_min": 60, "rates": null, "note": "พบ duration แต่ไม่พบราคา PC ในข้อมูลที่มี"}
```

## 9. ทำไมบางคำถามขึ้น "ไม่พบข้อมูล" ทั้งที่มีข้อมูล

สาเหตุหลักมี 4 แบบ:

1. **ข้อมูลอยู่ท้าย chunk แล้วโดนตัด**  
   เช่น Home equipment, News details, Service Fee

2. **category filter พาไปผิดหมวด**  
   เช่น equipment query ไป `games` แต่ข้อมูลจริงอยู่ Home ที่ถูก label เป็น `penalty`

3. **curated direct answer หยิบ fact ใกล้เคียงผิด**  
   เช่นถามอุปกรณ์ แต่ direct curated ตอบรายชื่อเกม

4. **LLM ได้ context ไม่พอ**  
   ถ้า top source ไม่มีข้อมูลตรง หรือข้อมูลตรงถูกตัด ก็ต้องตอบ `ไม่พบข้อมูล`

## 10. Data Fix Plan ที่ควรทำต่อ

### Priority 1 - แก้ chunking ใหม่

แก้ `scripts\optimize_content.py`:

- split by heading
- split by newline
- split by numbered rules
- split by service block
- split by news date/title
- hard split item > 900 chars

เป้าหมาย:

- ไม่มี chunk > 1200 ตัวอักษร ยกเว้นจำเป็นจริง
- ค่า median ควรอยู่ประมาณ 300-700
- ข้อมูลสำคัญต้องอยู่ใน 750 ตัวแรกของ chunk หรือใช้ snippet extraction

### Priority 2 - ทำ curated facts เพิ่ม

เพิ่ม curated facts สำหรับ:

- equipment
- service_fee
- events_news
- about_members
- knowledge FAQ

โดยเฉพาะ equipment ควรเพิ่มทันที เพราะ fail 0/8 ใน category นี้

### Priority 3 - แก้ category taxonomy

เพิ่มหมวด:

- `equipment`
- `service_fee`
- `events_news`
- `about_members`
- `booking_rules`
- `studio_rules`

และแก้ `route_category()` ให้ตรงกับหมวดเหล่านี้

### Priority 4 - แก้ rule-based guard

- เพิ่ม `required_any`
- เพิ่ม `forbidden_any`
- เพิ่ม no-answer guard สำหรับคำถามที่ถามบริการที่ไม่มีข้อมูล
- ลด pattern ที่กว้างเกิน เช่น `คืออะไร`, `อาหาร`

### Priority 5 - แก้ evaluation

- ให้ `source_status()` อ่าน `metadata.source_ids`
- แยก answer score กับ source score
- เพิ่ม expected answer แบบ semantic ไม่ใช่ exact keyword อย่างเดียว

### Priority 6 - Rebuild Vector DB ให้แน่นอน

ตอนนี้ notebook rebuild index ถ้า:

```python
collection.count() == 0 or collection.count() != len(records)
```

ปัญหา:

- ถ้าแก้ text/category แต่จำนวน chunk เท่าเดิม จะไม่ rebuild

ข้อเสนอ:

- ทำ checksum ของ `optimized_chunks.jsonl`
- เก็บ checksum ใน Chroma metadata หรือ local manifest
- ถ้า checksum เปลี่ยนให้ rebuild ทันที
- หรือเพิ่มปุ่ม/flag `FORCE_REBUILD_INDEX = True`

## 11. ตอบคำถามผู้ใช้แบบตรง ๆ

### ตอนนี้ผิดเพราะ Data ไหม?

ใช่ ส่วนใหญ่ผิดเพราะ Data pipeline มากกว่า model

### Category บาง chunk ผิดไหม?

ใช่ ผิดหลายจุด โดยเฉพาะ:

- Home -> penalty
- Reservation -> penalty
- Services -> games
- Events News -> rules
- Knowledge บางบทความ -> rules

### Format ผิดไหม?

มี 2 ระดับ:

- raw JSONL มี bad JSON 15 จุด
- processed JSONL valid แล้ว แต่ chunk format ยังไม่เหมาะกับ RAG เพราะ chunk ยาวและปนหลายหัวข้อ

### ข้อมูลไม่มีจริงไหม?

มีบางส่วนที่ไม่มีจริง เช่น ราคา PC แบบ structured rate ยังไม่ครบ แต่หลายเคสข้อมูลมีอยู่แล้ว เพียงแต่ถูก chunk/category/context ทำให้หาไม่เจอ

### ต้องแก้อะไรก่อน?

ควรแก้ตามลำดับนี้:

1. chunking ใหม่
2. category ใหม่
3. curated facts สำหรับ equipment/service_fee/news/about
4. rebuild vector DB
5. rerun ground truth
6. ค่อย fine tune rule/direct answer

## 12. Expected Result หลังแก้ Data

ถ้าแก้ chunking + category + curated facts อย่างเดียว โดยยังไม่เปลี่ยน model ควรคาดหวังได้ว่า:

- equipment จาก `0/8` ควรขึ้นเป็นอย่างน้อย `6/8`
- events_news จาก `0/5` ควรขึ้นเป็นอย่างน้อย `3/5`
- about_us จาก `0/5` ควรขึ้นเป็นอย่างน้อย `3/5`
- rules จาก `1/18` ควรขึ้นมาก เพราะตอนนี้หลายข้อ fail จาก source strict/context/rule
- pass rate รวมมีโอกาสขยับจาก `36.19%` ไปแถว `60-75%` ก่อนแตะเรื่อง LLM เพิ่ม

สรุปสุดท้าย: รอบนี้ควรกลับไปเน้น **Data Optimization** ก่อน ไม่ควรรีบเปลี่ยน model เพราะ Qwen/LLM ไม่ใช่คอขวดหลักของความถูกต้องในตอนนี้
