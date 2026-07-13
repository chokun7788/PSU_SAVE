# Answer Quality Pipeline

เอกสารนี้เป็น pipeline สำหรับทำให้ Chatbot ของ PSU Esports ตอบได้ถูกต้องขึ้น ไม่มั่ว ตรงคำถาม และไม่เวิ่นเว้อเกินไป

หลักสำคัญคือไม่ให้ระบบเลือกแค่ระหว่าง `Rule base` กับ `LLM` แบบตรง ๆ แต่ต้องมีหลายชั้นที่ช่วยคัดกรอง เจาะหมวด ตรวจความมั่นใจ และจัดรูปคำตอบ

## เป้าหมาย

Chatbot ที่ดีสำหรับศูนย์ควรมีคุณสมบัติ 5 อย่าง:

1. ตอบข้อเท็จจริงถูก เช่น ราคา เวลา กฎ จำนวน session
2. ตอบตรงเจตนาคำถาม เช่น ถ้าถาม “ต่างกันเท่าไหร่” ต้องตอบส่วนต่างก่อน
3. ไม่มั่วเมื่อไม่มีข้อมูล
4. ตอบเร็วพอสำหรับ Facebook/Chatbot จริง
5. เพิ่มข้อมูลใหม่ได้โดยไม่ต้องแก้ code ยุ่งยากทุกครั้ง

## Pipeline ภาพรวม

```text
User input
↓
1. Input preprocessing
↓
2. Normalization + alias mapping
↓
3. Safety / scope / no-answer guard
↓
4. Intent + entity router
↓
5. Deterministic handlers
   - calculator
   - structured lookup
   - category rule base
↓
6. Confidence gate
↓
7. RAG retrieval
↓
8. Grounded LLM rewrite
↓
9. Answer quality formatter
↓
10. Final validation + source
↓
Answer
```

## Stage 1: Input Preprocessing

หน้าที่:

- รับข้อความจากผู้ใช้
- ตัดช่องว่างเกิน
- เก็บต้นฉบับไว้สำหรับ log
- แยกภาษาไทย/อังกฤษแบบคร่าว ๆ
- แยกประโยคที่มีหลายคำถาม

ตัวอย่าง:

```text
วันจันทร์ morning เล่นได้ไหม afternoon เปิดไหม
```

ควรเก็บเป็น:

```json
{
  "raw_query": "วันจันทร์ morning เล่นได้ไหม afternoon เปิดไหม",
  "clean_query": "วันจันทร์ morning เล่นได้ไหม afternoon เปิดไหม",
  "language_hint": "mixed_th_en"
}
```

สิ่งที่ไม่ควรทำ:

- อย่าแปลภาษาอัตโนมัติเร็วเกินไป เพราะคำเฉพาะ เช่น `Morning`, `Afternoon`, `PSU`, `VR` อาจมีความหมายตามระบบจอง

## Stage 2: Normalization + Alias Mapping

หน้าที่:

- แปลงคำพิมพ์หลายแบบให้เป็น canonical term
- ลดปัญหาคำสะกดผิดเล็กน้อย
- ทำให้ router จับหมวดง่ายขึ้น

ตัวอย่าง alias:

```text
มอ. -> PSU
นักเรียน มอ. -> PSU student/staff candidate
เด็ก มอ -> PSU student/staff candidate
ต่างมหาลัย -> general_student
ต่างสถาบัน -> general_student
คนนอก -> general_adult หรือ unknown_group ขึ้นกับบริบท
วีอาร์ / แว่น / vr -> VR
เพลย์ / playstation / ps5 -> PlayStation 5
นินเทนโด / switch -> Nintendo Switch
พวงมาลัย / ขับรถ -> Cockpit
```

ผลลัพธ์ที่ควรได้:

```json
{
  "normalized_query": "วันจันทร์ morning เล่นได้ไหม afternoon เปิดไหม",
  "entities": {
    "day": "monday",
    "time_slots": ["morning", "afternoon"]
  }
}
```

ข้อควรระวัง:

- ใช้ fuzzy เฉพาะ entity ที่ควบคุมได้ เช่น ชื่อเครื่อง/กลุ่มผู้ใช้
- ไม่ควรใช้ cosine similarity ทั้ง rule base โดยตรง เพราะอาจ match ผิดหมวด

## Stage 3: Safety / Scope / No-answer Guard

หน้าที่:

- กันคำถามที่ไม่มีข้อมูลจริง
- กันคำถามนอกบริการ
- กัน AI ตอบมั่วเพราะอยากช่วยเกินไป

ตัวอย่างคำถามที่ควรเข้า no-answer:

```text
มีบริการซ่อมคอมส่วนตัวไหม
เช่าจอไปบ้านได้ไหม
มีที่นอนค้างคืนไหม
จ่ายด้วยคริปโตได้ไหม
```

คำตอบที่ดี:

```text
ยังไม่พบข้อมูลที่ยืนยันได้ว่าศูนย์มีบริการซ่อมคอมส่วนตัวในฐานข้อมูลตอนนี้ครับ
```

ไม่ควรตอบ:

```text
สามารถติดต่อเจ้าหน้าที่เพื่อสอบถามราคาได้
```

ถ้าไม่มีข้อมูลยืนยัน การโยนให้ติดต่อเจ้าหน้าที่ควรใช้เป็นประโยคเสริมอย่างระมัดระวัง ไม่ใช่ตอบเหมือนบริการนั้นมีจริง

## Stage 4: Intent + Entity Router

หน้าที่:

- แยกว่าคำถามอยู่หมวดไหน
- แยก entity ที่ต้องใช้ตอบ เช่น วัน, เวลา, เครื่อง, กลุ่มผู้ใช้, จำนวนชั่วโมง
- ไม่ตอบในขั้นนี้ แค่ตัดสินใจว่าจะส่งไป route ไหน

หมวดหลักที่ควรมี:

```text
service_fee
schedule
reservation
checkin
payment
cancel
rules
penalty
games
equipment
contact
overview
events_news
knowledge
no_answer
unknown
```

ตัวอย่าง:

```text
ต่างมหาลัย เล่น VR ครึ่งชม เท่าไหร่
```

ควร route เป็น:

```json
{
  "intent": "service_fee",
  "entities": {
    "user_group": "general_student",
    "service": "vr_30",
    "duration": "30_minutes"
  },
  "confidence": 0.95
}
```

```text
วันจันทร์ morning เล่นได้ไหม afternoon เปิดไหม
```

ควร route เป็น:

```json
{
  "intent": "schedule",
  "entities": {
    "day": "monday",
    "time_slots": ["morning", "afternoon"]
  },
  "confidence": 0.95
}
```

## Stage 5: Deterministic Handlers

Deterministic handler คือส่วนที่ตอบได้โดยไม่ต้องใช้ LLM เพราะข้อมูลแน่นอน

### 5.1 Calculator

ใช้กับ:

- ราคา
- ส่วนต่างราคา
- จำนวน session
- ค่าปรับที่เป็นช่วง
- เวลา/slot ถ้ามีสูตรชัด

ตัวอย่าง:

```text
ต่างมหาลัยเล่น VR 30 นาที กับ VR 1 ชั่วโมงต่างกันเท่าไหร่
```

คำตอบที่ควรได้:

```text
ต่างกัน 185 บาท สำหรับกลุ่ม PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน

- VR 30 นาที ราคา 190 บาท
- VR 1 ชั่วโมง ราคา 375 บาท

แหล่งข้อมูล: ...
```

### 5.2 Structured Lookup

ใช้กับ:

- ตารางเวลา
- รายการเกม
- รายการอุปกรณ์
- ช่องทางติดต่อ
- สมาชิก/ภาพรวมศูนย์

ตัวอย่าง:

```text
คอมมีวาโลไหม
```

คำตอบ:

```text
มีครับ PC มีเกม VALORANT

เกม PC ที่มีในรายการยังรวมถึง Counter-Strike 2, PUBG: BATTLEGROUNDS, Call of Duty: Warzone, Tekken 8 และ League of Legends
```

### 5.3 Category Rule Base

ใช้กับ:

- กฎการจอง
- กฎการเช็คอิน
- กฎอาหาร/เสียงดัง/อุปกรณ์
- เงื่อนไขยกเลิก/ชำระเงิน

Rule base ไม่ควรเก็บคำตอบยาวเป็นก้อนเดียว ควรเก็บแบบ structured:

```json
{
  "id": "rule_checkin_advance",
  "category": "reservation",
  "intent": "checkin_advance_time",
  "answer_first": "เช็คอินได้ล่วงหน้าสูงสุด 30 นาที",
  "details": [
    "ต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง"
  ],
  "source_url": "https://esports.computing.psu.ac.th/reservation"
}
```

## Stage 6: Confidence Gate

หลัง deterministic handler ได้คำตอบ ต้องตรวจ confidence ก่อนตอบจริง

เกณฑ์แนะนำ:

```text
>= 0.90 ตอบได้เลย
0.75-0.89 ตอบได้ถ้าคำถามไม่เสี่ยง และควรใส่เงื่อนไข/ขอ clarification เล็กน้อย
0.50-0.74 ส่งต่อ RAG หรือถามกลับ
< 0.50 ไม่ตอบมั่ว ให้ no-answer หรือ clarify
```

ตัวอย่าง ambiguity:

```text
นักเรียนเล่น VR ราคาเท่าไหร่
```

คำว่า `นักเรียน` ไม่ชัดว่าเป็น PSU หรือโรงเรียน/ต่างสถาบัน

คำตอบที่ดี:

```text
ขอแยกกลุ่มก่อนนะครับ ถ้าหมายถึงนักศึกษา/บุคลากร PSU ราคา 0 บาท แต่ถ้าเป็นนักเรียนหรือนักศึกษาต่างสถาบันให้ดูราคา General Student

สำหรับ VR 30 นาที:
- PSU Student and Staff: 0 บาท
- PSU Alumni and General Student: 190 บาท
- General Adult: 525 บาท
```

## Stage 7: RAG Retrieval

ใช้เมื่อ:

- deterministic route ไม่มีคำตอบ
- คำถามเป็นข้อมูลยาว เช่น ข่าว กิจกรรม ประวัติ รายละเอียดจากเว็บ/PDF/Facebook
- ผู้ใช้ถามแบบสรุป/เปรียบเทียบจากหลายแหล่ง

RAG ควรค้นแบบมี category filter:

```text
ถ้า intent = events_news -> ค้นเฉพาะ events/news/facebook chunks ก่อน
ถ้า intent = rules -> ค้น rules/policy chunks ก่อน
ถ้า intent = games -> ค้น games catalog ก่อน
```

ไม่ควรค้นทั้งฐานแบบกว้างทุกครั้ง เพราะ:

- ช้า
- ดึง context ผิดง่าย
- ทำให้ LLM ตอบหลุดเรื่อง

## Stage 8: Grounded LLM Rewrite

LLM ควรทำหน้าที่:

- เรียบเรียงคำตอบให้อ่านเป็นธรรมชาติ
- รวมข้อมูลจากหลาย chunk
- ตอบภาษาไทย/อังกฤษให้เหมาะกับผู้ใช้

LLM ไม่ควรทำหน้าที่:

- คิดราคาเอง
- เดากฎเอง
- เดาเวลาเปิดปิดเอง
- เติมข้อมูลที่ไม่มีใน context

Prompt ควรบังคับ:

```text
ให้ตอบจากข้อมูลที่ให้เท่านั้น
ถ้าข้อมูลไม่พอ ให้บอกว่ายังไม่พบข้อมูลที่ยืนยันได้
ให้ตอบสิ่งที่ผู้ใช้ถามก่อน แล้วค่อยใส่รายละเอียด
ห้ามเริ่มจากตารางรวม ถ้าผู้ใช้ถามค่าเฉพาะ
```

## Stage 9: Answer Quality Formatter

ทุก route ควรผ่าน formatter กลางก่อนตอบ

รูปแบบคำตอบที่แนะนำ:

```text
[คำตอบตรงคำถาม 1-2 บรรทัด]

รายละเอียด:
- ...
- ...

แหล่งข้อมูล:
- ...
```

กฎของ formatter:

- ถ้าถามราคา ให้ตัวเลขมาก่อน
- ถ้าถามเวลา ให้ช่วงเวลามาก่อน
- ถ้าถามได้/ไม่ได้ ให้ตอบได้/ไม่ได้ก่อน
- ถ้าถามต่างกันเท่าไหร่ ให้ตอบส่วนต่างก่อน
- ถ้าถามรายการ ให้สรุปรายการแบบ bullet
- ถ้าข้อมูลไม่พอ ห้ามใส่รายละเอียดที่ไม่ได้ยืนยัน

ตัวอย่างที่ไม่ดี:

```text
ตารางบริการที่มีในข้อมูล:
- Morning คือ ...
- Afternoon คือ ...
ดังนั้น ...
```

ตัวอย่างที่ดี:

```text
วันจันทร์ Morning เล่นไม่ได้ เพราะ 09:00-12:00 เป็น Maintenance* ส่วน Afternoon เปิดให้เล่น 13:00-16:00

รายละเอียด:
- Morning คือ 09:00-12:00
- Afternoon คือ 13:00-16:00
```

## Stage 10: Final Validation + Source

ก่อนส่งคำตอบควรตรวจ:

- มีคำตอบตรง question intent หรือยัง
- มี source หรือยังเมื่อเป็นข้อมูลจากเว็บ/เอกสาร
- มีคำต้องห้ามแบบ “เดาเอง” หรือไม่
- ถ้า confidence ต่ำ มีคำว่า “ยืนยันได้” หรือ “ยังไม่พบข้อมูล” ตามเหมาะสมหรือไม่
- คำตอบยาวเกินไปไหม

Rule ง่าย ๆ:

```text
ถ้าคำถามเป็น fact เฉพาะ คำตอบไม่ควรเกิน 3-6 บรรทัด
ถ้าคำถามเป็น list คำตอบไม่ควรเกิน 8-12 bullet
ถ้าคำถามเป็น summary ค่อยยาวได้
```

## Pipeline แบบ Pseudocode

```python
def answer(user_input: str) -> Answer:
    raw = user_input
    clean = preprocess(raw)
    normalized, entities = normalize_and_extract(clean)

    no_answer = no_answer_guard(normalized, entities)
    if no_answer.confidence >= 0.90:
        return format_no_answer(no_answer)

    route = route_intent(normalized, entities)

    deterministic = try_deterministic(route, normalized, entities)
    if deterministic.confidence >= 0.90:
        return answer_quality_formatter(deterministic)

    if deterministic.confidence >= 0.75 and deterministic.risk == "low":
        return answer_quality_formatter(deterministic)

    if should_clarify(route, entities):
        return clarify_with_options(route, entities)

    docs = rag_retrieve(normalized, category=route.category)
    if docs.best_score < RAG_THRESHOLD:
        return format_no_answer_for_missing_context(route)

    llm_answer = grounded_llm_rewrite(
        question=raw,
        context=docs,
        rules=[
            "answer_first",
            "no_unverified_claims",
            "cite_sources",
        ],
    )

    checked = final_validate(llm_answer, route, docs)
    if not checked.ok:
        return format_no_answer_for_low_confidence(route)

    return checked.answer
```

## การแบ่งงานพัฒนา

### Phase 1: MVP ที่ควรทำก่อน

- ทำ normalize/alias ให้แน่น
- แยก router หมวดหลัก
- ทำ deterministic handlers:
  - schedule
  - service_fee
  - reservation/checkin/payment/cancel
  - games
  - equipment
  - contact
- ทำ answer-first formatter
- ทำ no-answer guard
- เพิ่ม test สำหรับ first sentence

### Phase 2: RAG ที่ดีขึ้น

- แยก chunk ตาม category
- เพิ่ม metadata:
  - `category`
  - `source_url`
  - `source_type`
  - `updated_at`
  - `confidence`
- retrieval แบบ filter ตาม intent
- reranker หรือ lightweight scoring
- threshold ถ้าไม่เจอข้อมูลให้ no-answer

### Phase 3: LLM Rewrite

- ให้ LLM เรียบเรียงจาก structured facts/context เท่านั้น
- ทำ prompt แบบ answer-first
- จำกัดความยาวคำตอบตาม answer type
- เพิ่ม bilingual response policy ไทย/อังกฤษ

### Phase 4: Monitoring

- เก็บคำถามจริงจากผู้ใช้
- เก็บ route ที่ใช้
- เก็บ confidence
- เก็บ fallback/no-answer
- เอาคำถามซ้ำกลับมาเพิ่ม rule หรือ ground truth

## Evaluation ที่ควรเพิ่ม

Ground Truth เดิมเช็ค keyword/source อย่างเดียวไม่พอ ควรเพิ่ม metric:

- `intent_match`: ตอบตรงสิ่งที่ถามไหม
- `first_sentence_quality`: ประโยคแรกตอบคำถามไหม
- `fact_correctness`: ตัวเลข/เวลา/กฎถูกไหม
- `no_unverified_claim`: มีการเดาหรือแต่งเองไหม
- `verbosity`: ยาวเกินจำเป็นไหม
- `source_ok`: source ถูกหมวดไหม

ตัวอย่าง test:

```json
{
  "question": "วันจันทร์ morning เล่นได้ไหม afternoon เปิดไหม",
  "must_start_with_any": [
    "วันจันทร์ Morning เล่นไม่ได้",
    "Morning เล่นไม่ได้"
  ],
  "must_contain": ["13:00", "16:00", "Maintenance"],
  "must_not_contain": ["24 ชั่วโมง", "24 hours"],
  "category": "schedule"
}
```

## สรุป

แนวทางที่ควรใช้คือ:

```text
Normalize -> Guard -> Router -> Deterministic -> Confidence Gate -> RAG -> Grounded LLM -> Formatter -> Validation
```

ถ้าทำครบ pipeline นี้ ระบบจะ:

- เร็ว เพราะคำถามซ้ำ/ข้อเท็จจริงไม่ต้องเข้า LLM
- แม่น เพราะราคา เวลา และกฎมาจาก structured facts
- ไม่มั่ว เพราะมี guard และ confidence gate
- ตรงคำถามขึ้น เพราะมี answer-first formatter
- ขยายต่อได้ เพราะ RAG และ LLM อยู่เป็น fallback ไม่ใช่แกนหลักของทุกคำตอบ
