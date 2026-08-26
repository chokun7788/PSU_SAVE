# คู่มืออธิบายเทคนิค Full Process Flow ของ PSU Esports Chatbot

สถานะเอกสาร: 2026-08-07  
ขอบเขต: Local-first chatbot สำหรับ PSU Esports Studio - Phuket  
เอกสารหลักที่คู่มือนี้ใช้อธิบาย: [`40_current_chatbot_full_process_flow_20260807.md`](./40_current_chatbot_full_process_flow_20260807.md)  
ภาพประกอบ Flow: [`psu_esports_chatbot_full_process_flow_20260807.png`](./psu_esports_chatbot_full_process_flow_20260807.png)

เอกสารนี้ไม่ได้เสนอ Flow ชุดใหม่ แต่ขยายความ Flow เดิมทีละ process โดยอธิบายว่า:

1. process นั้นมีหน้าที่อะไร
2. รับข้อมูลอะไรและส่งอะไรต่อ
3. ใช้เทคนิคอะไร และศัพท์นั้นหมายถึงอะไร
4. ตัดสินใจอย่างไรใน implementation ปัจจุบัน
5. ถ้าผ่านหรือไม่ผ่านแล้วไปทางไหน 
6. มีตัวอย่างให้เห็นภาพอย่างไร
7. มีข้อจำกัดหรือจุดที่ไม่ควรเข้าใจเกินจริงตรงไหน

> ตัวอย่างคำถามและ JSON ในเอกสารนี้ใช้เพื่ออธิบายกลไก ไม่ใช่การยืนยันว่าศูนย์มีราคา เวลา เกม หรือกฎตามข้อความตัวอย่าง หากต้องตอบข้อมูลจริง ระบบยังต้องอ่านจาก source ที่ยืนยันแล้วเสมอ

---

## 1. ภาพรวมแบบภาษาคนก่อนอ่านรายละเอียด

ให้มอง chatbot ตัวนี้เป็น “ผู้ประสานงานหลายเครื่องมือ” ไม่ใช่ LLM ตัวเดียวที่อ่านข้อความแล้วตอบทันที

```text
เปิดระบบ
  -> เตรียมข้อมูล ดัชนี cache และ model ที่จำเป็น

ผู้ใช้ส่งคำถาม
  -> เว็บแปลงคำถามเป็น API request แบบ JSON
  -> server ตรวจ request และควบคุมจำนวนงานพร้อมกัน
  -> กำหนดเส้นตายของ request
  -> อ่านบริบท session เพื่อแก้คำว่า เกมนั้น/เครื่องนั้น/อันเดิม
  -> ตรวจว่าเป็นคำถามเดียวหรือหลายคำถาม
  -> ถ้าหลายคำถาม ตรวจว่าส่วนต่าง ๆ ทำพร้อมกันได้หรือจำเป็นต้องทำตามลำดับ
  -> ทำความเข้าใจคำถาม: normalize, route, intent, target, ambiguity
  -> เลือกความสามารถที่เหมาะที่สุด
       Fast / Rule / Calculator
       Structured Tool
       Fact Card / RAG / Vector / Reranker
       Local LLM เฉพาะจุดที่อนุญาต
  -> ตรวจรูปแบบคำตอบ หลักฐาน ตัวเลข target และความสอดคล้อง
  -> ถ้ายังเสี่ยง ให้ถามกลับหรือ no-answer
  -> ส่ง JSON กลับเว็บ
  -> เว็บแสดงคำตอบและแหล่งข้อมูล
  -> เขียน log/metrics ภายหลังแบบ asynchronous
```

แก่นของระบบคือ **evidence-first**: หาหรืออ่านข้อมูลจริงก่อน แล้วจึงตอบหรือให้ LLM ช่วยเรียบเรียง ไม่ใช่ให้ LLM จำข้อมูล PSU เอง

---

## 2. ศัพท์พื้นฐานที่ต้องรู้

### 2.1 Process, stage และ path

- **Process/Stage** คือขั้นตอนหนึ่ง เช่น `Boundary Guard` หรือ `Entity Extraction`
- **Path** คือเส้นทางที่ request เลือกเดิน เช่น Structured path หรือ RAG path
- request หนึ่งรายการไม่ได้ใช้ทุก path แต่จะผ่านขั้นตอนทำความเข้าใจร่วมกัน แล้วเลือก execution path ที่เหมาะ

### 2.2 Deterministic

หมายถึง เมื่อ input และข้อมูลเหมือนเดิม กฎจะให้ผลเดิมตามโค้ด ไม่ได้สุ่มสร้างข้อความแบบ generative model ตัวอย่างเช่น:

- ถ้าพบคำว่า `ราคา` และรู้ service/user group/duration ครบ ให้เครื่องคำนวณราคา
- ถ้าถามรายชื่อเกมในโซน ให้กรองแถวข้อมูลตาม `zone_id`

Fast, Rule และ Structured ส่วนใหญ่เป็น deterministic

### 2.3 Heuristic

คือกฎประมาณการที่ออกแบบจากสัญญาณหลายอย่าง ไม่ใช่สูตรความจริงสากลและไม่จำเป็นต้องเป็น AI model เช่น:

- พบคำว่า `ปุ่ม`, `จอย`, `กดอะไร` เพิ่มคะแนน intent ด้าน controls
- พบชื่อเกมแบบ exact alias เพิ่มความมั่นใจ target มากกว่าการสะกดคล้าย

### 2.4 Gate และ Guard

- **Gate** คือประตูตัดสินใจว่าจะให้ไปต่อทางใด เช่น Complexity Gate, Ambiguity Gate
- **Guard** คือด่านป้องกันความผิดหรือความเสี่ยง เช่น Boundary Guard, Source Guard
- ทั้งสองอาจใช้ rules, scores, threshold หรือ model แต่ชื่อ `Gate/Guard` ไม่ได้แปลว่าใช้ LLM เสมอ

### 2.5 Confidence และ margin

- **Confidence** คือคะแนนความมั่นใจที่ process นั้นรายงาน ช่วงประมาณ `0.0-1.0`
- ในระบบนี้คะแนนหลายจุดเป็น **policy score ที่กำหนดจากกฎ** ไม่ใช่ความน่าจะเป็นที่ผ่านการ calibrate ทางสถิติ
- **Margin** คือส่วนต่างระหว่างคะแนนอันดับหนึ่งกับอันดับสอง

ตัวอย่าง:

```text
structured.games = 0.86
retrieval.hybrid = 0.80
margin = 0.86 - 0.80 = 0.06
```

margin สูงแปลว่าผู้ชนะห่างจากตัวเลือกถัดไปมากกว่า แต่ไม่ได้รับประกันว่าคำตอบถูก จึงยังต้องผ่าน precondition และ validator

### 2.6 Evidence, source และ grounding

- **Evidence** คือข้อมูลที่ใช้รองรับคำตอบ เช่น row ของเกม, ตารางราคา, fact card หรือข้อความจากเอกสาร
- **Source** คือที่มาของ evidence เช่น source ID, ไฟล์, URL, หมวด และ trust level
- **Grounding** คือการบังคับให้คำตอบอยู่บน evidence ไม่เพิ่มข้อเท็จจริงเอง

### 2.7 Fallback และ abstain

- **Fallback** คือทางสำรองเมื่อทางหลักใช้ไม่ได้
- **Abstain** คือระบบตั้งใจไม่ตอบข้อเท็จจริง เพราะความมั่นใจหรือหลักฐานไม่พอ
- ผลของ abstain อาจเป็นคำถามขอรายละเอียดเพิ่ม หรือ no-answer

---

## 3. Startup / Setup / Warmup

### 3.1 Startup คืออะไร

Startup คือช่วงหลังเปิด Python server แต่ก่อนหรือระหว่างที่ระบบเริ่มพร้อมรับคำถาม ช่วงนี้เหมาะกับงานที่มีต้นทุนครั้งแรกสูง เพราะไม่ควรให้ผู้ใช้คนแรกเป็นคนรอค่าใช้จ่ายนั้น

`app/pipeline/warmup.py` เป็นตัวประสาน warmup หลัก ส่วน `app/web_api/server.py` เรียก warmup และ LLM preflight ตอนเริ่ม server

### 3.2 Warmup คืออะไร

Warmup คือการเรียกโหลดหรือทดลองใช้ทรัพยากรล่วงหน้า เพื่อให้ข้อมูล ดัชนี หรือ model อยู่ใน memory/cache แล้ว เมื่อ request จริงเข้ามาจึงไม่ต้องเริ่มจากศูนย์

เปรียบเทียบ:

```text
Cold request:
อ่านไฟล์ -> สร้าง index -> โหลด model -> คำนวณ -> ตอบ

Warm request:
ใช้ index/model ใน memory -> คำนวณ -> ตอบ
```

### 3.3 Warmup โหลดอะไรบ้าง

#### A. Game alias และ typo/correction cache

**โหลดอะไร**

- ชื่อเกมมาตรฐาน
- alias เช่นชื่อย่อ ชื่อภาษาไทย หรือรูปแบบสะกดอื่นที่ข้อมูลกำหนดไว้
- compact form ที่ตัดช่องว่าง/สัญลักษณ์เพื่อใช้เทียบชื่อ
- helper สำหรับแก้ชื่อเกมที่สะกดคลาดเคลื่อน

**เอาไปใช้ทำอะไร**

- ตรวจว่าคำว่า `TEKKEN 8`, รูปแบบตัวพิมพ์ต่างกัน หรือ alias ที่ลงทะเบียนไว้หมายถึงเกมเดียวกันหรือไม่
- ช่วย `Session Context Resolver`, `Entity Resolver`, Structured Games และ game-control retrieval ใช้ target ID เดียวกัน

**เทคนิค**

- อ่านข้อมูลครั้งแรกแล้วเก็บใน cache
- สร้าง lookup map ลักษณะ `alias -> canonical game`
- บางฟังก์ชันใช้ `lru_cache` ซึ่งเก็บผลไว้ใน process ปัจจุบัน

#### B. Structured data cache

**โหลดอะไร**

- สมาชิกและกลุ่มสมาชิก
- เกม แพลตฟอร์ม และโซน
- ข้อมูล controls ที่มีการยืนยัน
- อุปกรณ์
- การจอง ตารางเวลา และค่าบริการ

**เอาไปใช้ทำอะไร**

ทำให้ Structured Tool สามารถกรอง นับ จัดกลุ่ม และคำนวณจาก field ได้ทันที เช่นเลือกแถวที่ `zone=PS5` แทนการอ่านข้อความยาวทุกครั้ง

**เทคนิค**

- parse JSON/JSONL/CSV ให้เป็น row หรือ object
- cache ผลการ parse
- lookup ด้วย key/field ที่กำหนดไว้

#### C. Routing matrix และ semantic-intent catalog

**โหลดอะไร**

- คำและวลีที่สัมพันธ์กับ route/intent
- ตัวอย่างประโยคของแต่ละ intent
- threshold และ policy ที่ใช้แยกหมวด

**เอาไปใช้ทำอะไร**

ช่วย Heuristic Router และ Semantic Intent Fallback ตัดสินว่า `ราคาเท่าไหร่` ควรไป price path หรือ `ปุ่มอะไร` ควรไป game controls

#### D. Curated retrieval rows

**โหลดอะไร**

- ข้อความความรู้ FAQ ข่าว/กิจกรรม หรือข้อมูลอธิบายที่ไม่ได้อยู่ในตาราง field ตายตัว
- metadata เช่น category, source ID, URL, trust level และ updated time ถ้ามี

**เอาไปใช้ทำอะไร**

เป็น candidate ฝั่งเอกสารของ Hybrid RAG

#### E. Competition fact cards

**โหลดอะไร**

ข้อเท็จจริงกติกาที่แปลงเป็น record สั้นและมีหัวข้อ เช่น team size, map pool, pause หรือ penalty

**เอาไปใช้ทำอะไร**

ค้นกติกาแบบเจาะจงโดยไม่ต้องส่งเอกสารการแข่งขันทั้งหมดให้ LLM

#### F. Local vector index

**โหลดอะไร**

- feature ของข้อความในคลัง retrieval
- mapping ระหว่าง vector/feature กับเอกสารและ metadata

**เทคนิคจริงในปัจจุบัน**

backend คือ `local_hash_char_ngram_v1` ใช้ character n-gram และ word feature แบบ sparse แล้วเทียบ cosine similarity ไม่ใช่ neural semantic embedding เต็มรูปแบบ

ตัวอย่าง character n-gram ของคำว่า `ราคา` เมื่อใช้ชิ้นยาว 2-3 ตัวอักษร อาจมองเป็นส่วนย่อยเช่น `รา`, `าค`, `คา`, `ราค`, `าคา` การเทียบชิ้นย่อยช่วยรับมือข้อความที่สะกดหรือเว้นวรรคต่างกันได้บางส่วน

#### G. Probe queries

**คืออะไร**

ระบบส่งคำถามตัวอย่างภายในไปยัง pipeline เพื่อบังคับให้โค้ดส่วนที่ใช้บ่อยสร้าง cache ล่วงหน้า

**ครอบคลุมอะไร**

- Fast path
- Structured path
- Knowledge/RAG path
- News path

**จุดสำคัญ**

probe ตั้งใจปิด experimental LLM เพื่อไม่ให้ startup ใช้ model call เกินจำเป็นหรือสร้างคำตอบ model ที่ไม่เกี่ยวกับการ warm cache

#### H. Optional BGE reranker warmup

**โหลดอะไร**

โมเดล `BAAI/bge-reranker-v2-m3` พร้อม tokenizer/weights และ runtime ที่เกี่ยวข้องเข้า RAM หรือ VRAM ตาม environment

**เอาไปใช้ทำอะไร**

รับคู่ `(คำถาม, เอกสาร candidate)` แล้วให้คะแนนความเกี่ยวข้องใหม่แบบ CrossEncoder หลัง retrieval รอบแรก

**สถานะปัจจุบัน**

- ปิดเป็นค่าเริ่มต้นของ pipeline warmup
- เปิดได้ด้วย `PSU_PIPELINE_WARMUP_RERANKER=1`
- ถ้าไม่ warm และเวลา request เหลือน้อยกว่าเกณฑ์ ระบบจะข้าม BGE แล้วใช้ hybrid score

#### I. Ollama LLM preflight

**ทำอะไร**

- ส่ง prompt สั้นมาก เช่นให้ตอบ `OK`
- ตรวจว่า Ollama endpoint ติดต่อได้
- ตรวจว่า model ชื่อที่กำหนดโหลดและสร้าง token ได้
- บันทึก success/failure เข้า LLM Health Manager
- ใช้ `keep_alive` เพื่อให้ model ค้างใน memory ช่วงหนึ่ง

**ไม่ใช่อะไร**

preflight ไม่ได้ตอบคำถามผู้ใช้ และไม่ได้รับประกันว่าคำตอบจริงทุกคำถามจะเสร็จทันเวลา มันยืนยันเพียง health/readiness เบื้องต้น

### 3.4 Warmup ทำงานตามลำดับอย่างไร

```text
เริ่ม Python process
  -> สร้าง singleton pipeline
  -> warm alias/correction indexes
  -> warm structured rows
  -> warm routing/intent catalogs
  -> warm curated/fact-card/vector data
  -> รัน probe queries
  -> optional: โหลด BGE
  -> LLM preflight ไปยัง Ollama
  -> server พร้อมรับ request
```

Warmup จับ exception ของแต่ละงานและรายงานผลได้ เพื่อไม่ให้ความผิดพลาดของส่วน optional ทำ server ล้มทั้งหมด แต่ผลเช่น `server เปิดได้` ไม่ได้แปลว่า optional model ทุกตัวพร้อม ต้องดู warmup/preflight result เพิ่ม

### 3.5 Cold-start cost คืออะไร

Cold-start cost คือต้นทุนเวลาและทรัพยากรครั้งแรกที่เกิดเมื่อสิ่งนั้นยังไม่อยู่ใน memory/cache เช่น:

- เปิดและ parse ไฟล์ครั้งแรก
- สร้าง alias/index ครั้งแรก
- import framework/model runtime
- โหลด weights ของ BGE
- ให้ Ollama โหลด Typhoon จาก disk เข้า RAM/VRAM
- compile/initialize kernel บางชนิดใน model runtime

ตัวเลข BGE ประมาณ `93.46 วินาที` ที่เคยวัดคือ cold load ใน environment ที่ทดสอบ ไม่ใช่เวลาที่ BGE ใช้ rerank ทุกครั้ง เมื่อ model อยู่ใน memory การ rerank ครั้งถัดไปเร็วกว่าอย่างมาก

อย่างไรก็ตาม คำว่า “เกิดครั้งเดียว” มีเงื่อนไข:

- เกิดอย่างน้อยหนึ่งครั้ง **ต่อ process**
- ถ้า restart server/process ต้องโหลดใหม่
- ถ้ามีหลาย worker process แต่ละ process อาจโหลด model ของตัวเอง
- ถ้า memory pressure ทำให้ model ถูก unload ต้องโหลดใหม่
- Typhoon ผ่าน Ollama มี `keep_alive=10m` เป็นค่าเริ่มต้น จึงอาจถูก unload หลังไม่มีการใช้ตามนโยบายของ Ollama
- BGE ใช้ Python cache และมักอยู่จน process ปิด แต่ยังขึ้นกับ runtime และทรัพยากร

### 3.6 Warmup กินทรัพยากรอย่างไร

- aliases, rows และดัชนีข้อความกิน RAM แต่โดยทั่วไปเบากว่า model weights
- BGE กิน RAM/VRAM มากกว่าดัชนี และถ้ามีหลาย process จะมีโอกาสทำสำเนาหลายชุด
- Typhoon 4B กิน RAM/VRAM ของ Ollama ขณะ resident
- การเปิดทิ้งไว้ช่วย latency แต่แลกกับ memory ที่ถูกถือไว้
- warm ไม่ได้แก้คอขวด multi-user: ถ้า LLM concurrency ยังเท่ากับ 1 ผู้ใช้หลายคนยังต้องแย่ง slot เดียวกัน

---

## 4. User Input, Web และ API

### 4.1 ผู้ใช้กรอกอะไร

หน้าเว็บรับข้อความธรรมชาติ เช่น:

```text
PS5 มีเกมอะไรบ้าง
```

ฝั่ง browser ยังอาจมีข้อมูลประกอบที่ผู้ใช้ไม่ต้องพิมพ์เอง เช่น:

- `client_session_id` เพื่อแยกการสนทนา
- `recent_history` เพื่อให้ resolve คำอ้างอิง
- debug/experimental flags เฉพาะเมื่อเปิดใช้

### 4.2 Web คืออะไร

Web คือส่วนหน้าที่ผู้ใช้เห็น ได้แก่ช่องพิมพ์ ปุ่มส่ง ประวัติแชต loading state และพื้นที่แสดงคำตอบ/แหล่งข้อมูล JavaScript ใน browser จะรับข้อความแล้วเรียก backend

### 4.3 API คืออะไร

API คือข้อตกลงการสื่อสารระหว่างหน้าเว็บกับ backend ในระบบนี้ entry point หลักคือ:

```text
POST /api/chat
```

`POST` หมายถึงส่งข้อมูลเข้า server ส่วน `/api/chat` คือ path ของฟังก์ชันแชต

### 4.4 ทำไมต้องมี JSON

JSON เป็นรูปแบบข้อมูลมีโครงสร้างที่ทั้ง browser และ Python อ่านได้ง่าย จึงส่งได้มากกว่าข้อความคำถามเพียงค่าเดียว

ตัวอย่าง request เชิงโครงสร้าง:

```json
{
  "question": "PS5 มีเกมอะไรบ้าง",
  "client_session_id": "session-example-001",
  "recent_history": [],
  "debug": false
}
```

ตัวอย่าง response แบบย่อ:

```json
{
  "answer": "ข้อความคำตอบที่ผ่านการตรวจแล้ว",
  "mode": "pipeline:structured_games_catalog",
  "route": {
    "category": "games",
    "intent": "games_lookup"
  },
  "confidence": 0.9,
  "elapsed": 0.42,
  "sources": []
}
```

JSON มีประโยชน์เพราะ:

- web แสดงเฉพาะ `answer` ได้
- debug panel อ่าน `trace` ได้เมื่อเปิด debug
- metrics อ่าน `elapsed`, `mode`, `confidence` ได้
- client อื่น เช่น mobile app สามารถใช้ API เดียวกันได้

JSON ไม่ใช่ฐานข้อมูล และไม่ได้เป็น AI เป็นเพียงรูปแบบบรรจุข้อมูลระหว่างระบบ

### 4.5 ความสัมพันธ์ของ Web กับ API

```text
ผู้ใช้ -> หน้าเว็บ -> HTTP/JSON -> API server -> chatbot pipeline
ผู้ใช้ <- หน้าเว็บ <- HTTP/JSON <- API server <- pipeline result
```

หน้าเว็บไม่ควรมี logic ความจริงของ PSU เอง หน้าที่หลักคือรับ input และแสดง output ส่วนการ route, retrieve, validate และตอบอยู่ที่ backend

### 4.6 Request validation

ก่อนเข้า pipeline server ตรวจอย่างน้อย:

- `Content-Length` สูงสุดประมาณ 128 KB
- body ต้อง decode เป็น UTF-8 JSON ได้
- ต้องมี question ที่ไม่ว่าง
- question ยาวไม่เกิน 4,000 ตัวอักษร
- field ที่ส่งเข้ามาต้องอยู่ในรูปแบบที่รองรับ

การตรวจตรงนี้ป้องกัน request เสีย ขนาดใหญ่ผิดปกติ และงานที่ไม่มีคำถามจริง ไม่ใช่การตรวจความหมายของคำถาม

---

## 5. Admission Control และ Multi-user Guard

### 5.1 Admission Control คืออะไร

Admission Control คือด่านหน้าที่ตัดสินว่า server มีความสามารถรับงานใหม่ตอนนี้หรือไม่ เป้าหมายคือไม่ปล่อยให้ทุก request วิ่งเข้า CPU/GPU พร้อมกันจนทั้งหมดช้าและ timeout

เปรียบเทียบกับร้านที่มีโต๊ะจำกัด: การรับลูกค้าเกินความจุไม่ได้ทำให้บริการมากขึ้นเสมอ แต่ทำให้ทุกโต๊ะรอนานขึ้น

### 5.2 Active request semaphore

**Semaphore** คือตัวนับ slot งานพร้อมกัน

ค่าเริ่มต้นปัจจุบัน:

```text
MAX_ACTIVE_REQUESTS = 16
```

กลไก:

1. request มาถึง
2. ลองขอ active slot
3. ถ้าได้ slot จึงไปต่อ
4. เมื่อจบหรือ error ต้องคืน slot
5. ถ้าไม่มี slot ตอบ HTTP `503 server_busy`

นี่คือการ fail fast เพื่อให้ client รู้ว่า server ยุ่ง แทนการปล่อยให้ request แขวนจนหมดเวลา

### 5.3 Per-session lock

session เดียวกันมี lock แยก เพื่อป้องกันข้อความสองข้อความจากผู้ใช้เดียวกันประมวลผลสลับลำดับ

ตัวอย่างปัญหาถ้าไม่มี lock:

```text
ข้อความ 1: TEKKEN 8 มีที่โซนไหน
ข้อความ 2: แล้วปุ่มอะไร
```

ถ้าข้อความ 2 ประมวลผลก่อนข้อความ 1 เขียน context เสร็จ คำว่า `แล้ว` อาจไม่มี target ที่ยืนยันได้

ค่า wait ปัจจุบันประมาณ `0.10 วินาที` หาก session เดิมยังยุ่งจะตอบ HTTP `409 session_busy` แทนการรอนาน

### 5.4 LLM concurrency guard

แม้ server รับ request ได้หลายรายการ แต่ Local LLM เป็นงานหนัก จึงมี semaphore อีกชั้น ค่าเริ่มต้นให้ LLM ทำพร้อมกัน `1 call`

- ถ้า slot ว่าง: call ไปยัง Ollama
- ถ้า slot ไม่ว่าง: รอแบบจำกัด โดย default ประมาณ `0.20 วินาที` และถูกบีบตาม deadline ที่เหลือ
- ถ้ายังไม่ได้ slot: ข้าม/fallback ไม่รอแบบไม่มีกำหนด

### 5.5 Per-request LLM call budget

request หนึ่งรายการมีสิทธิ์ใช้ LLM สูงสุด `2 calls` รวมทุกบทบาท เช่น planner, intent review, tool router, composer หรือ general fallback

เหตุผลคือ หากแต่ละ stage เรียก model ได้เองโดยไม่แชร์ budget request เดียวอาจเรียก 4-5 ครั้งและเกิน 10 วินาทีง่ายมาก

### 5.6 Compound worker limit

คำถามหลายส่วนที่เป็นอิสระอาจทำ child พร้อมกัน แต่จำกัด worker เริ่มต้นที่ `2` และบีบในช่วง `1-3` เพื่อไม่ให้ parallelism ขยายงานจนแย่งทรัพยากร

### 5.7 ข้อจำกัดของ guard ปัจจุบัน

semaphore, session lock, LLM state และ cache เป็น **in-process** หมายความว่า process A ไม่เห็นคิวของ process B หากเปิดหลาย Python processes จึงยังไม่ใช่ distributed queue และไม่สามารถรับประกัน global concurrency ของเครื่องทั้งเครื่องได้

---

## 6. Global Deadline และ Time Budget

### 6.1 Deadline ต่างจาก timeout รายขั้นอย่างไร

- **Global deadline** คือเวลาสิ้นสุดร่วมของ request ทั้งก้อน
- **Stage timeout** คือเวลาสูงสุดของขั้นเดียว เช่น Query Planner สูงสุด 4 วินาที

ถ้าไม่มี global deadline แต่ละขั้นอาจใช้ timeout เต็มของตัวเองต่อกัน:

```text
planner 4s + retrieval 2s + composer 8s + validation 1s = 15s
```

global deadline บังคับให้ทุกขั้นแบ่งเวลาจากนาฬิกาเรือนเดียว

### 6.2 Product backend budget คืออะไร

สำหรับ Web/API ปัจจุบัน backend สร้าง request deadline ประมาณ `9 วินาที` หมายถึง pipeline และงาน backend ต้องพยายามจบภายในช่วงนี้

### 6.3 User-visible cap คืออะไร

คือเวลาที่ผู้ใช้รู้สึกจริงตั้งแต่กดส่งจนเห็นคำตอบ ซึ่งรวมมากกว่า pipeline:

```text
browser ส่ง request
+ network/localhost overhead
+ backend queue/admission
+ pipeline
+ serialize JSON
+ browser render
= user-visible latency
```

จึงตั้ง backend budget ต่ำกว่าเป้าหมายผู้ใช้เล็กน้อย เป้าหมายประมาณ 10 วินาที แต่ backend ใช้ประมาณ 9 วินาที

### 6.4 Finalizer reserve คืออะไร

ระบบกันเวลาประมาณ `1 วินาที` ไว้สำหรับงานท้าย เช่น:

- formatter
- validator และ answer contract
- สร้าง safe fallback ถ้าจำเป็น
- สร้าง result/decision artifact
- encode และส่ง HTTP response

ถ้าเวลาคงเหลือเท่ากับ reserve ระบบไม่ควรเริ่ม LLM call ใหม่ เพราะอาจได้ข้อความ model มาแต่ไม่มีเวลาตรวจ

### 6.5 Deadline-aware timeout ทำงานอย่างไร

แนวคิดของ `timeout_for_call(configured_timeout)` คือ:

```text
เวลาที่ให้ call = min(timeout ของ stage, เวลาที่เหลือ - finalizer reserve)
```

ตัวอย่าง:

- composer ตั้งไว้สูงสุด 8 วินาที
- request เหลือ 5 วินาที
- reserve 1 วินาที
- composer จะได้ไม่เกินประมาณ 4 วินาที ไม่ใช่ 8 วินาที

ถ้าเวลาใช้การได้เหลือ `<= 0` stage จะถูก skip และไป fallback

### 6.6 Product budget, legacy cap และ direct pipeline call

ค่าต้องแยกเป็นคนละชั้น:

- Web product path กำหนด deadline ประมาณ 9 วินาทีจาก `server.py`
- `request_deadline.py` รองรับค่า global timeout จาก environment
- การเรียก pipeline โดยตรงจาก test/script อาจไม่มี outer deadline หากไม่ได้ส่ง context หรือ config เข้าไป
- ตัวเลข 20 วินาทีเป็นเพดานเดิม/ค่า global ที่เคยใช้ใน flow ก่อนหน้า ไม่ได้ถูกบวกต่อจาก 9 วินาที ใน Web product path เส้นตายที่ครอบจริงคือประมาณ 9 วินาที

ดังนั้นไม่ควรอ่านว่า `9 + 20 = 29 วินาที`

### 6.7 ตัวอย่าง timeline

```text
0.00s  รับ request และสร้าง deadline
0.05s  validation/admission/session context
0.20s  preprocess/routing/target/candidate decision
0.35s  retrieval เริ่ม
0.70s  ได้ evidence
0.75s  ตรวจ model gateway
0.75s  ถ้าเหลือเวลาไม่ถึง minimum ของ composer -> ใช้ deterministic draft
8.00s  ควรหยุดเริ่มงานหนักใหม่
8-9s   validation/finalizer/HTTP response
ประมาณ 10s ผู้ใช้เห็นผลรวมหน้าเว็บ
```

### 6.8 ทำไมยัง timeout ได้แม้มี deadline

- library หรือ Ollama บางช่วงอาจไม่ตอบสนองต่อการยกเลิกทันที
- การปิด streaming socket เป็น best effort ไม่ใช่ process-level hard cancel
- thread ที่กำลังติด native/model operation อาจคืน control ช้า
- ถ้ารอ queue ก่อน stage เริ่ม เวลาคงเหลืออาจน้อยลงมาก
- cold load อาจกินเวลายาวกว่างบก่อน logic จะรู้ว่าควร skip

deadline ทำให้ระบบมีนโยบายหยุดและ fallback แต่ไม่สามารถรับประกัน interrupt ทุกคำสั่งระดับ OS/GPU ได้

---

## 7. Session Context Resolver

ไฟล์หลัก: `app/session/context_resolver.py`

### 7.1 ปัญหาที่แก้

มนุษย์มักถามต่อแบบละประธาน:

```text
User: TEKKEN 8 เล่นที่ไหน
User: แล้วปุ่มอะไร
```

ข้อความที่สองไม่มีชื่อเกม แต่คนเข้าใจจากบริบท ระบบจึงต้อง resolve ว่า `ปุ่มอะไร` หมายถึงปุ่มของ target ใด

### 7.2 ใช้ LLM หรือไม่

ปัจจุบันเป็น deterministic resolver ไม่ใช้ LLM หลัก ๆ ใช้:

- normalization
- alias lookup
- pattern/keyword recognition
- การเลือกข้อความล่าสุดที่เกี่ยวข้อง
- กฎ topic shift
- pending clarification state

### 7.3 ข้อมูลที่อ่านจาก history

ระบบจำกัด history เพื่อไม่ให้ context โตไม่สิ้นสุด โดยใช้ช่วงล่าสุดประมาณ:

- 12 รายการสำหรับ history แบบข้อความ
- 16 รายการสำหรับ history แบบ object/dict

จากนั้นหา evidence เช่น:

- เกมล่าสุดที่กล่าวถึงอย่างชัดเจน
- โซน/เครื่อง/service ล่าสุด
- intent/domain ล่าสุด
- คำถาม clarification ที่ระบบเพิ่งถาม

### 7.4 เทคนิค normalization

Normalization ทำให้รูปแบบที่เขียนต่างกันเทียบกันง่ายขึ้น เช่น:

- ตัวพิมพ์ใหญ่/เล็ก
- ช่องว่างเกิน
- Unicode form
- alias ที่ข้อมูลกำหนดไว้

ไม่ได้แปลว่าสามารถแก้ typo ทุกชนิดได้ แต่ลดความต่างที่ไม่เปลี่ยนความหมาย

### 7.5 Explicit target wins

ถ้าคำถามปัจจุบันระบุ target ชัด ให้ใช้ target ปัจจุบันก่อน history เสมอ

```text
History: คุยเรื่อง TEKKEN 8
Current: แล้ว EA SPORTS FC 25 ปุ่มอะไร
ผล: ใช้ EA SPORTS FC 25 ไม่ดึง TEKKEN 8 จาก history
```

กฎนี้ป้องกัน context เก่าทับสิ่งที่ผู้ใช้พิมพ์ใหม่

### 7.6 Follow-up detection

ระบบมองหาสัญญาณคำถามต่อ เช่น:

- `แล้ว...`
- `อันนั้น`
- `เกมนั้น`
- `เครื่องนั้น`
- ประโยคสั้นที่เป็น operation เช่น `ปุ่มอะไร`, `ราคาเท่าไหร่`

ถ้าพบ target ล่าสุดเพียงหนึ่งรายการที่สอดคล้องกับ domain จึงเติม context ให้ active query

ตัวอย่างแนวคิด:

```text
history_target = TEKKEN 8
current = ปุ่มอะไร
resolved_query = TEKKEN 8 ปุ่มอะไร
```

### 7.7 Topic-shift detection

ระบบตรวจว่าผู้ใช้เปลี่ยนหัวข้อหรือยัง เพื่อไม่ลาก target เก่ามาใช้ผิด

```text
History: คุยเรื่องเกม TEKKEN 8
Current: วันจันทร์เปิดกี่โมง
```

คำถามปัจจุบันมี schedule signal ชัด จึงไม่ควรเติมชื่อเกม

### 7.8 Pending clarification

หาก bot ถามกลับว่าให้เลือกเกมหรือ service ใด แล้วผู้ใช้ตอบเพียงตัวเลือกสั้น ๆ resolver พยายามเชื่อมคำตอบนั้นกับคำถามที่ค้างอยู่

ตัวอย่าง:

```text
Bot: ต้องการถามราคา PC Zone หรือ PS5 Zone ครับ
User: PC
```

`PC` จะถูกตีความร่วมกับ pending question ไม่ใช่คำถามทั่วไปคำใหม่

### 7.9 เมื่อไม่ควร resolve

```text
History: กล่าวถึง TEKKEN 8 และ EA SPORTS FC 25 ใกล้กัน
Current: เกมนั้นปุ่มอะไร
```

ถ้าไม่มีหลักฐานว่าหมายถึงเกมใด resolver ต้องไม่สุ่มเลือกชื่อที่ใกล้ที่สุด ผลควรคงคำถามไว้ให้ Ambiguity Gate ถามกลับ

### 7.10 Output ของ resolver

ข้อมูลสำคัญที่ส่งต่อคือ:

- active/resolved question
- สถานะ resolved หรือ unchanged
- target/context ที่พบ
- เหตุผลหรือ trace เพื่อ debug

resolver ไม่ได้ตอบคำถาม หน้าที่ของมันคือทำให้คำถามที่ส่งเข้า pipeline มี context ที่ตรวจสอบย้อนกลับได้

---

## 8. Split Multi-question

### 8.1 ปัญหาที่แก้

ผู้ใช้หนึ่งข้อความอาจมีหลาย operation:

```text
PS5 มีเกมอะไรบ้าง และ PC ราคาเท่าไหร่
```

ถ้าส่งทั้งหมดให้ route เดียว route อาจเลือกเพียง games หรือ price แล้วทำอีกส่วนหาย จึงต้องแยกเป็น child questions ก่อน

### 8.2 เทคนิคที่ใช้จริง

ฟังก์ชัน `_split_multi_question()` ใน `engine.py` ใช้ deterministic pattern/regex ไม่ได้ให้ LLM แยกทุกข้อความ

สัญญาณแบ่งมีลักษณะเช่น:

- เครื่องหมาย `?`
- `แล้ว`
- `และ`
- `ส่วน`
- `อีกอย่าง`
- รูปแบบ shared-tail หรือ shared-subject ที่รองรับ

แต่ไม่ได้ตัดทุกครั้งที่เจอคำว่า `และ` เพราะคำว่าเดียวกันอาจเชื่อม field ของเรื่องเดียว

### 8.3 Inseparable clause preservation

ระบบมี safeguard รักษาวลีการจองหรือข้อมูลที่ต้องอยู่ด้วยกัน ไม่ให้แยกจนความหมายพัง

แนวคิด:

```text
จอง PC วันจันทร์ช่วงบ่ายและเล่น 2 ชั่วโมง
```

คำว่า `และ` เชื่อมเงื่อนไขของการจองเดียว ไม่ควรกลายเป็นสองคำถามอิสระ

### 8.4 Standalone-question signal

หลังแบ่ง candidate แล้ว แต่ละส่วนต้องดูเหมือนคำถามที่ตอบได้เอง เช่นมี operation/target ที่สมเหตุสมผล ระบบไม่สร้าง child จากเศษคำสั้น ๆ โดยไม่มีความหมาย

### 8.5 Shared subject

บางประโยคระบุ subject ครั้งเดียวแล้วมีหลาย operation:

```text
TEKKEN 8 อยู่โซนไหนและปุ่มอะไร
```

splitter ต้อง carry subject `TEKKEN 8` ไปยัง child ที่สอง เพื่อไม่ให้กลายเป็น `ปุ่มอะไร` แบบไร้ target

### 8.6 Shared tail / multi-entity

บางประโยคมีหลาย target แต่ operation อยู่ท้าย:

```text
PC กับ PS5 ราคาเท่าไหร่
```

ระบบพยายามรักษาหรือกระจาย operation `ราคาเท่าไหร่` ให้แต่ละ target ตาม pattern ที่รองรับ

### 8.7 Boundary tail split

ถ้าข้อความมีส่วนที่ระบบตอบได้และส่วนที่อยู่นอกขอบเขต splitter สามารถแยกให้แต่ละ child ผ่าน Boundary Guard ของตัวเอง แทนการปล่อยส่วนหนึ่งกลบอีกส่วน

### 8.8 จำนวน child

implementation จำกัดผล split แบบ bounded โดยทั่วไป `1-3 parts` แม้ planner schema รองรับได้ถึง 4 tasks การจำกัดนี้ลด fan-out, latency และโอกาสที่ context จะผิด

### 8.9 ผลลัพธ์ตัวอย่าง

```text
Input:
PS5 มีเกมอะไรบ้าง และ PC ราคาเท่าไหร่

Parts:
1. PS5 มีเกมอะไรบ้าง
2. PC ราคาเท่าไหร่
```

```text
Input:
TEKKEN 8 อยู่โซนไหนและปุ่มอะไร

Conceptual parts:
1. TEKKEN 8 อยู่โซนไหน
2. TEKKEN 8 ปุ่มอะไร
```

### 8.10 ข้อจำกัด

regex เข้าใจรูปแบบที่เขียนไว้ในกฎ ไม่ได้เข้าใจภาษาทุกแบบเหมือนมนุษย์ ประโยคยาวที่ละประธานหลายชั้น ประชด หรือใช้เครื่องหมายผิดปกติอาจ split ไม่ครบ จึงมี Complexity Gate และ optional Query Planner เป็นชั้นถัดไป

---

## 9. Complexity Gate และ Compound Execution

ไฟล์หลัก: `app/pipeline/compound_execution.py`

### 9.1 Complexity Gate คืออะไร

เป็นตัวจำแนกว่า child questions ที่ split แล้ว:

- เป็นคำถามเดียว
- เป็นหลายคำถามที่เป็นอิสระและทำพร้อมกันได้
- เป็นคำถามซับซ้อน/มี dependency ที่ต้องทำตามลำดับ

Gate นี้ไม่ได้ตอบคำถามและไม่ได้เลือก data source หน้าที่คือออก execution profile

### 9.2 สัญญาณที่ตรวจ

ปัจจุบันเป็น deterministic keyword policy และจำนวน parts:

1. **Dependency/reference** เช่น `แล้วค่อย`, `จากนั้น`, `ผลลัพธ์`, `เกมนั้น`, `เครื่องนั้น`
2. **Broad/open-ended** เช่น `อธิบาย`, `แนะนำ`, `ภาพรวม`, `ทั้งหมด`
3. **Calculation/comparison** เช่น `เยอะสุด`, `อันดับ`, `รวม`, `เฉลี่ย`, `ต่างกัน`, `เปรียบเทียบ`
4. **Three or more parts** เมื่อมีอย่างน้อย 3 child questions

### 9.3 คะแนน complexity

สูตรปัจจุบันคือ:

```text
score = min(1.0, 0.18 x จำนวน parts + 0.30 x จำนวนสัญญาณ)
```

ตัวอย่าง:

```text
2 parts และไม่มีสัญญาณซับซ้อน
score = 0.18 x 2 = 0.36
ผล: simple independent
```

```text
2 parts + dependency + comparison
score = 0.18 x 2 + 0.30 x 2 = 0.96
ผล: complex/ordered
```

คะแนนนี้เป็น policy score เพื่ออธิบายระดับงาน ไม่ใช่ probability ว่า query “ซับซ้อนจริง” กี่เปอร์เซ็นต์

### 9.4 Simple independent

ตัวอย่าง:

```text
PS5 มีเกมอะไรบ้าง และวันจันทร์เปิดกี่โมง
```

ถ้าไม่มี reference ระหว่าง child ทั้งสอง แต่ละ child สามารถเข้า single pipeline ของตัวเอง ระบบอนุญาต bounded parallel ได้เมื่อ child เป็น deterministic

```text
child 1 -> Structured Games
child 2 -> Structured/Fast Schedule
          ทำพร้อมกันได้สูงสุด 2 workers
```

เพื่อควบคุมความเสี่ยง child ที่ทำ parallel จะไม่เปิด LLM อย่างอิสระ เพราะ model concurrency และ call budget อาจชนกัน

### 9.5 Ordered dependent

ตัวอย่าง:

```text
โซนไหนมีเกมเยอะสุด แล้วเครื่องนั้นราคาเท่าไหร่
```

child 2 ต้องรู้ผลจาก child 1 จึงทำพร้อมกันไม่ได้:

```text
child 1: หาโซนที่มีเกมมากที่สุด
  -> ได้ target ที่มี evidence
child 2: resolve "เครื่องนั้น" จากผล child 1
  -> ถ้า target ชัดจึงถามราคา
  -> ถ้าไม่ชัดให้ clarification
```

เมื่อ query มี signal ซับซ้อน โค้ดสร้าง dependency chain แบบอนุรักษนิยม คือ task ที่ 2 ขึ้นกับ task ที่ 1, task ที่ 3 ขึ้นกับ task ที่ 2 แทนการเดา Directed Acyclic Graph ที่ละเอียดแต่เสี่ยงผิด

### 9.6 Partial grounded answer

compound บางส่วนอาจตอบได้และบางส่วนไม่มีข้อมูล ระบบควรรวมเฉพาะ subanswer ที่ยืนยันได้ พร้อมแจ้งส่วนที่ต้องถามเพิ่มหรือยังไม่มี evidence ไม่ควรให้ child ที่ผิดทำลายคำตอบถูกทั้งหมด และไม่ควรแต่งส่วนที่หายให้ครบ

---

## 10. Query Planner

ไฟล์หลัก: `app/pipeline/query_planner.py`

### 10.1 Query Planner คืออะไร

Query Planner คือ Local LLM ที่ถูกจำกัดบทบาทให้ “แปลงคำถามซับซ้อนเป็นแผนงานมีโครงสร้าง” ไม่ใช่ผู้ตอบข้อเท็จจริง

เปรียบเทียบ:

- Answer model: พยายามตอบว่าอะไรคือคำตอบ
- Query Planner: บอกว่าต้องทำ task ใดก่อนหลัง ใช้ domain/operation อะไร และตรงไหนต้องถามกลับ

### 10.2 ทำไมต้องมี planner ทั้งที่มี splitter

splitter เก่งกับรูปแบบภาษาที่มีกฎชัด แต่ query บางชนิดมี dependency เชิงความหมาย เช่น:

```text
ช่วยหาโซนที่มีเกมมากที่สุด แล้วบอกค่าบริการของโซนนั้นสำหรับเงื่อนไขที่ฉันระบุ
```

คำว่า `โซนนั้น` พึ่งผลของ task แรก planner ช่วยเสนอ task semantics ให้ executor แต่ executor ยังตรวจ schema, route และ target อีกครั้ง

### 10.3 Planner ถูกเรียกเมื่อใด

หลัก ๆ เมื่อ:

- compound profile มี dependency/broad/calculation/comparison
- มีหลายส่วนที่ต้องจัดลำดับ
- single query บางชนิดมี route อ่อนและข้อความยาวพอ

คำถามง่ายที่ split ชัดและทำ deterministic ได้จะข้าม planner เพื่อประหยัดเวลาและ LLM budget

### 10.4 Input ของ planner

planner ได้รับข้อความคำถาม/parts และคำสั่งเข้มงวดว่า:

- ห้ามตอบ fact
- ห้ามเพิ่ม task ที่ไม่มีในคำถาม
- ใช้ domain/operation จาก allowlist เท่านั้น
- สร้างไม่เกิน 4 tasks
- ตอบ JSON เท่านั้น

### 10.5 Output schema

ตัวอย่างเชิงโครงสร้าง:

```json
{
  "is_compound": true,
  "confidence": 0.82,
  "reason": "ส่วนที่สองอ้างถึงผลจากส่วนแรก",
  "clarification": "",
  "tasks": [
    {
      "task_id": "t1",
      "question": "โซนไหนมีเกมมากที่สุด",
      "domain": "games",
      "operation": "compare",
      "target": "",
      "target_type": "zone",
      "filters": {},
      "needs_clarification": false,
      "confidence": 0.84,
      "reason": "ต้องจัดอันดับจำนวนเกมตามโซน"
    },
    {
      "task_id": "t2",
      "question": "ค่าบริการของโซนนั้นเท่าไหร่",
      "domain": "service_fee",
      "operation": "price_calculate",
      "target": "โซนจากผล task แรก",
      "target_type": "service",
      "filters": {},
      "needs_clarification": false,
      "confidence": 0.75,
      "reason": "ต้องใช้ target จาก task ก่อนหน้า"
    }
  ]
}
```

ตัวอย่างนี้อธิบายรูปแบบ ไม่ใช่ JSON ที่ยืนยันว่าจะออกเหมือนกันทุกตัวอักษร

### 10.6 Constrained planning คืออะไร

คำว่า constrained หมายถึง output ไม่ได้เชื่อทันที แต่ต้องผ่านเงื่อนไข:

- JSON parse ได้
- มี `tasks` เป็น list
- 1-4 tasks เท่านั้น
- domain อยู่ใน `PLANNER_DOMAINS`
- operation อยู่ใน `PLANNER_OPERATIONS`
- task ไม่ซ้ำ
- confidence รวมอย่างน้อยประมาณ `0.45`
- compound flag สอดคล้องกับจำนวน task

หาก model ครอบคำตอบด้วย code fence หรือ `<think>...</think>` parser จะลอก wrapper ที่รู้จักออก แต่ยังต้อง validate schema เดิม การลอก wrapper ไม่ได้ลดมาตรฐานด้านเนื้อหา

### 10.7 Allowlist คืออะไร

Allowlist คือรายการค่าที่อนุญาตล่วงหน้า ตัวอย่าง domain ที่รองรับ ได้แก่ games, game_controls, equipment, reservation, service_fee, schedule, rules, competition_rules และ general

หาก model สร้าง domain แปลกใหม่ เช่น `financial_advice` จะไม่ยอมรับ เพราะ executor ไม่มี contract รองรับ

### 10.8 Planner timeout และ budget

- planner cap สำหรับ complex query ไม่เกินประมาณ `4 วินาที`
- timeout ยังถูกบีบด้วย global deadline
- ใช้ LLM call budget ร่วมกับ stage อื่น
- ต้องผ่าน LLM Health Manager และ concurrency slot

ถ้า planner ใช้หนึ่ง call request จะเหลือ call budget น้อยลงสำหรับ composer จึงไม่เรียก planner ในคำถามง่าย

### 10.9 เมื่อ planner ล้มเหลว

กรณี timeout, Ollama ไม่พร้อม, JSON ผิด, schema ผิด หรือ confidence ต่ำ:

```text
reject plan
  -> ใช้ deterministic split/profile/ordered chain เดิม
  -> หาก target ยังไม่ชัด ให้ถามกลับ
  -> ไม่ใช้ข้อความ planner เป็นคำตอบผู้ใช้
```

planner จึงเป็นตัวช่วย ไม่ใช่ single point of failure

### 10.10 Planner ไม่ทำอะไร

- ไม่อ่านฐานข้อมูลราคาแทน Structured Tool
- ไม่ค้นเอกสารแทน RAG
- ไม่ยืนยันว่า target ที่ model พิมพ์มีอยู่จริง
- ไม่ข้าม Boundary/Ambiguity/Precondition/Validator
- ไม่ควรสร้างคำตอบสุดท้าย

---

## 11. Single-question Understanding Pipeline

ส่วนนี้คือแกนทำความเข้าใจของทุก child question ก่อนเลือก execution path

```text
Preprocess
  -> Active Query
  -> Entity/Reference/Target
  -> Boundary + Scope
  -> Route
  -> Model Gateway
  -> Universal Intent
  -> Route Refinement
  -> Optional Tool Router
  -> Ambiguity Gate
  -> Question Frame
  -> Candidate Scoring + Margin
  -> Tool Preconditions
  -> Execution
```

### 11.1 Preprocess

ไฟล์หลัก: `app/pipeline/preprocess.py`

#### หน้าที่

ทำข้อความให้อยู่ในรูปที่ process ถัดไปอ่านได้สม่ำเสมอ และดึง entity เบื้องต้น

#### ขั้นตอน

1. ตัดช่องว่างหัวท้ายและรวม whitespace ที่เกิน
2. normalize ตัวอักษร/ข้อความเพื่อใช้เทียบ
3. สร้าง query variants สูงสุดประมาณ 8 แบบจาก typo/รูปแบบคำที่รู้จัก
4. ประเมิน language hint จากจำนวนอักษรไทยและ Latin
5. ดึง entities และ flags

#### Entity ที่ดึง

- วัน เช่น Monday/วันจันทร์
- time slot เช่น morning/afternoon
- service/zone
- customer group เช่นนักศึกษา/บุคลากร/บุคคลทั่วไปเมื่อมีคำชัด
- duration
- price intent
- comparison intent
- short-answer request

#### ตัวอย่าง

```text
Input: "  PC วันจันทร์ ช่วงบ่าย 2 ชั่วโมง ราคาเท่าไหร่  "

Conceptual output:
clean_query = "PC วันจันทร์ ช่วงบ่าย 2 ชั่วโมง ราคาเท่าไหร่"
entities.service = "PC"
entities.day = "monday"
entities.time_slots = ["afternoon"]
entities.duration = 2
entities.price_intent = true
language_hint = "th"
```

Preprocess ยังไม่คำนวณราคาและยังไม่ยืนยันว่าข้อมูลครบ

### 11.2 Query variants และ Active Query Selection

#### Query variant คืออะไร

คือข้อความทางเลือกที่สื่อคำถามเดิม แต่ normalize/แก้รูปแบบที่รู้จัก เพื่อเพิ่มโอกาส route หรือ alias match

ตัวอย่างแนวคิด:

```text
original: "เพลห้า มีเกมไร"
variant:  "PS5 มีเกมอะไร"
```

ระบบจะไม่ควรสร้างความหมายใหม่จากคำที่ไม่รู้จัก

#### Active Query Selection

ระบบลองดู original และ variants แล้วเลือกข้อความที่ route/entity ชัดกว่าเป็น active query โดยยังเก็บ trace ว่ามาจาก variant ใด

เหตุผลที่ไม่แทน original แบบตาบอด: การแก้ typo ผิดอาจเปลี่ยนชื่อเกมหรือ target ดังนั้น exact/known mapping ต้องมีน้ำหนักสูงกว่า guess

### 11.3 Entity Extraction

#### Entity คืออะไร

Entity คือค่าที่อ้างถึงสิ่งเฉพาะในคำถาม เช่นชื่อเกม โซน วัน ระยะเวลา หรือกลุ่มผู้ใช้

#### เทคนิค

- keyword/phrase mapping
- regex สำหรับรูปแบบตัวเลขและเวลา
- alias lookup สำหรับ service/game
- flags สำหรับ operation เช่นราคา/เปรียบเทียบ/ตอบสั้น

#### Entity กับ intent ต่างกันอย่างไร

```text
คำถาม: PS5 ราคา 2 ชั่วโมงสำหรับนักศึกษาเท่าไหร่

intent/operation = price_calculate
entities = service: PS5, duration: 2, user_group: student
```

intent บอกว่าจะทำอะไร ส่วน entity บอกทำกับอะไร/เงื่อนไขใด

### 11.4 Reference และ Target Resolution

หลัง session resolver ให้ context แล้ว pipeline ยังต้องยืนยัน target จาก catalog

#### วิธีจับคู่ target ปัจจุบัน

เรียงจากหลักฐานแข็งไปอ่อนโดยประมาณ:

1. exact normalized alias: score ใกล้ `1.00`
2. compact alias match: score ใกล้ `0.96`
3. token overlap: สูงสุดประมาณ `0.86`
4. fuzzy string similarity: ใช้เมื่อ similarity ถึงเกณฑ์ประมาณ `0.84` แล้วมี penalty
5. optional entity reranker สำหรับกรณี candidate หลายตัวและ feature gate อนุญาต

#### Fuzzy matching คืออะไร

คือวัดความคล้ายของข้อความ แม้ไม่ตรงทุกตัวอักษร เช่นลำดับอักขระใกล้กัน แต่ fuzzy มีความเสี่ยงเลือกเกมผิด จึงไม่ควรเอาชนะ exact alias และต้องดู margin

#### Target resolver

รวม candidate จาก game, service และ equipment แล้วใช้ domain bias ช่วย เช่น intent เป็น game_controls ก็ควรให้น้ำหนัก target type `game` มากกว่า equipment แต่ bias ไม่ควรสร้าง target ที่ไม่มีใน catalog

### 11.5 Boundary Guard

ไฟล์หลัก: `app/pipeline/boundary_guard.py`

#### หน้าที่

หยุดคำถามที่มีนโยบายชัดก่อนใช้ retrieval/LLM เพื่อลดทั้งความเสี่ยงและเวลา

#### ตรวจอะไร

- ข้อมูลส่วนตัวหรือข้อมูลอ่อนไหว
- คำขอช่วยโกง/หลีกเลี่ยงกฎในบริบทที่ระบุ
- คำถามนอกขอบเขตที่ชัดเจน
- เหตุฉุกเฉินที่ควรส่งต่อช่องทางเหมาะสม
- facility/service ที่ระบบไม่มีข้อมูลรองรับ

#### เทคนิคจริง

ใช้รายการคำ/วลีและลำดับกฎ deterministic ไม่ได้ใช้ classifier neural และไม่ได้คำนวณ embedding

ตัวอย่างเชิงกลไก:

```text
normalized question
  -> match sensitive phrase?
       yes -> fixed privacy-safe action
  -> match unsafe cheating phrase?
       yes -> refuse/safe guidance
  -> match clear out-of-scope phrase?
       yes -> boundary response
  -> otherwise allow
```

#### Confidence วัดอย่างไร

ค่าประมาณ `0.90`, `0.96` ใน guard เป็นคะแนนที่ผู้พัฒนากำหนดตามความชัดของ rule ไม่ใช่ผลวัดว่ามีโอกาสถูก 90% จาก dataset ดังนั้นต้องประเมินด้วย test cases แยกต่างหาก

#### ตัวอย่าง

- คำถาม PSU ที่มี operation รองรับ: `allow`
- คำขอข้อมูลส่วนตัวที่ไม่มีสิทธิ์: ตอบ safe boundary response
- คำถามที่ไม่มี PSU/domain hint เลย: Boundary Guard อาจยัง allow ให้ Scope Guard/General policy ตัดสิน ไม่ได้ no-answer ทุกกรณีทันที

### 11.6 Scope Guard

ไฟล์หลัก: `app/pipeline/guard.py`

Boundary เน้นประเภทความเสี่ยง ส่วน Scope Guard ตรวจว่าคำถามอยู่ในขอบเขตข้อมูลที่ระบบรองรับหรือไม่

พฤติกรรมสำคัญ:

- พบ known unsupported term ชัด: no-answer ด้วย policy confidence สูงประมาณ `0.96`
- พบ domain hint: allow ด้วยคะแนนประมาณ `0.90`
- ไม่พบ domain hint: ให้สัญญาณอ่อนประมาณ `0.35` แต่ไม่ได้หยุดเสมอ อาจไป General policy

### 11.7 Heuristic Router

ไฟล์หลัก: `app/pipeline/router.py`

#### Route คืออะไร

Route เป็นป้ายกำกับระดับระบบ เช่น:

```text
category = service_fee
intent = service_fee_query
answer_type = calculation
risk = medium
confidence = ...
```

#### วิธีทำงาน

router ใช้ ordered priority chain: ตรวจ recognizer ที่เฉพาะหรือเสี่ยงสูงก่อนคำกว้าง ตัวอย่างเช่นคำถาม booking, cancellation หรือ controls ควรจับก่อนคำทั่วไปเกี่ยวกับเกม

เหตุผล: keyword เดียวอาจอยู่หลายหมวด เช่นคำว่า `เล่น` ปรากฏทั้งเกม วิธีจอง และวิธีควบคุม การเรียง priority จึงเป็นส่วนหนึ่งของ logic

#### Semantic Intent Fallback

เมื่อ exact rules ยังไม่ชัด ระบบมี catalog ตัวอย่างและเทียบ character n-gram ขนาด 2, 3, 4 ตัวอักษร

ขั้นตอน:

1. แปลง query และตัวอย่าง intent เป็น Counter ของ n-grams
2. คำนวณ cosine similarity
3. หา best score และ runner-up
4. blend คะแนนตาม policy
5. ตรวจ minimum confidence และ minimum margin ของ row

สูตร cosine โดยแนวคิด:

```text
cosine = dot(query_features, example_features)
         / (length(query_features) x length(example_features))
```

ค่ามากหมายถึง pattern ตัวอักษรทับซ้อนกันมากกว่า

> ชื่อโมดูลมีคำว่า semantic แต่ implementation นี้ยังไม่ใช่ sentence embedding neural จึงเข้าใจความหมายได้จำกัดกว่าระบบ embedding เต็มรูปแบบ

### 11.8 Model Gateway Preflight

ไฟล์หลัก: `app/pipeline/model_gateway.py`

#### หน้าที่

ตัดสินว่าจะเปิดสิทธิ์ให้ optional model stage ใด และควรสงวนเวลา/LLM call ให้ส่วนไหน

#### หลักการ

- strong deterministic route: มักข้าม model review
- ambiguous/weak route: อาจอนุญาต intent review หรือ tool router
- knowledge/news ที่ต้อง RAG: สงวน budget ให้ grounded composer มากกว่านำไปใช้กับ preflight stage
- source conflict หรือ exact facts: ไม่ควรให้ composer เพิ่มความเสี่ยง
- RAG composer ต้องมีเวลาคงเหลือขั้นต่ำประมาณ 8 วินาทีตาม policy ปัจจุบัน

#### ทำไมต้องมี gateway

หาก planner, intent reviewer, tool router และ composer ต่างเรียก LLM โดยไม่ประสานกัน คำถามเดียวอาจหมดทั้ง call budget และเวลา ก่อนถึงขั้นที่มีประโยชน์ที่สุด

### 11.9 Universal Intent

ไฟล์หลัก: `app/pipeline/universal_intent.py`

#### Universal Intent คืออะไร

เป็น representation กลางที่ละเอียดกว่า route:

```text
domain      = games
operation   = control_lookup
target      = TEKKEN 8
filters     = {...}
needs       = [verified_control_data]
answer_style= direct
confidence  = ...
method      = heuristic หรือ llm_review
```

ทุก execution capability สามารถอ่านโครงเดียวกัน จึงลดการผูกกับคำศัพท์ของ router ตัวใดตัวหนึ่ง

#### Heuristic intent scoring

ระบบเพิ่มคะแนน domain และ operation จาก:

- คำ/วลีใน query
- route prior
- entity/target ที่พบ
- signal เฉพาะ operation

แล้วเลือกอันดับหนึ่งพร้อม runner-up/margin

#### Optional LLM intent review

ใช้เมื่อ intent อ่อน กว้าง หรือมีหลายสัญญาณแข่งขันกัน และ feature flag/budget/health อนุญาต

ผล LLM ไม่ได้รับสิทธิ์ทับ strong deterministic route ง่าย ๆ ต้องผ่าน schema/confidence และ policy โดย intent ที่ยอมรับเพื่อ refine route ต้องมี confidence เพียงพอ เช่นประมาณ `0.78` ในจุดสำคัญ

### 11.10 Route Refinement

Universal Intent อาจทำให้ route เบื้องต้นละเอียดขึ้น เช่น router มองเป็น `games` กว้าง ๆ แต่ intent พบ operation `control_lookup` และ target game ชัด จึง refine intent ของ route ไปทาง controls

Refinement ต้องรักษา high-risk route ไม่ให้ model เปลี่ยนหมวดสำคัญด้วยความมั่นใจต่ำ และต้องบันทึก old/new route ใน trace

### 11.11 Optional Tool Router

ไฟล์หลัก: `app/pipeline/llm_tool_router.py`

#### หน้าที่

ให้ Local LLM เสนอว่า query ควรใช้ `fast`, `structured`, `retrieval`, `clarification` หรือ path ที่ allowlist รองรับ โดยตอบ candidate JSON

#### สถานะอำนาจ

Tool Router เป็นคำแนะนำ ไม่ใช่คำสั่งสุดท้าย ข้อเสนอของมันยังต้องเทียบกับ:

- deterministic route
- universal intent
- target
- capability registry
- tool preconditions
- policy veto

#### เมื่อไม่ควรเรียก

- route/target ชัดและ structured ตอบได้
- LLM budget ควรสงวนให้ RAG composer
- deadline เหลือน้อย
- health circuit cooldown

### 11.12 Ambiguity Gate

ไฟล์หลัก: `app/pipeline/ambiguity_gate.py`

#### Ambiguity คืออะไร

คือสถานการณ์ที่คำถามตีความได้มากกว่าหนึ่งทาง หรือ operation ต้องใช้ข้อมูลที่ยังไม่มี ถ้าระบบเลือกเองมีโอกาสตอบคนละเรื่องกับที่ผู้ใช้ต้องการ

#### สิ่งที่ตรวจ

1. มีหลาย game candidates ที่ใกล้กัน
2. price query ไม่มี service/target
3. broad query เช่น `มีอะไรบ้าง`
4. follow-up สั้นแต่ไม่มี context target
5. controls query ไม่มีชื่อเกม
6. bare play/how-to ที่ไม่รู้เกม
7. service target กว้างเกินไป
8. intent อันดับหนึ่งและสองคะแนนใกล้กัน
9. reference ที่ session resolver ยืนยันไม่ได้

#### Candidate scoring ใน gate

gate รวม evidence signal และ prior แบบ deterministic แล้วเทียบ top/runner-up ตัวอย่างเงื่อนไข intent ambiguity ปัจจุบันโดยประมาณ:

```text
top score >= 0.50
runner-up >= 0.42
margin < 0.14
```

เมื่อเข้าเงื่อนไขและไม่มี exception ที่ทำให้ operation ชัด ระบบเลือก clarify

คะแนนดังกล่าวเป็น policy score ไม่ใช่ calibrated probability

#### ตัวอย่าง 1: ราคาไม่มี target

```text
User: ราคาเท่าไหร่
```

สิ่งที่รู้: operation = price lookup  
สิ่งที่ขาด: service/zone, และอาจขาด user group/durationสำหรับ calculation  
ผล: ถามกลับว่าหมายถึงบริการใด แทนการเลือกราคาใดราคาหนึ่ง

#### ตัวอย่าง 2: controls ไม่มีเกม

```text
User: ปุ่มอะไร
History: ไม่มีชื่อเกมที่ยืนยันได้
```

ผล: ถามชื่อเกมก่อน เพราะ controls เป็น operation ที่ต้องมี target

#### ตัวอย่าง 3: intent แข่งขันกัน

```text
User: เล่นยังไง
```

อาจหมายถึงวิธีเล่นเกม วิธีใช้เครื่อง หรือขั้นตอนเข้ารับบริการ ถ้าสัญญาณและ margin ไม่พอ ระบบถามกลับ

#### Output

- `allow`: ความหมายพอชัด ไป Question Frame
- `clarification`: สร้างคำถามขอข้อมูลเฉพาะที่ขาด
- บางกรณี policy อาจลง no-answer หากสิ่งที่ขอไม่มีข้อมูลรองรับ ไม่ใช่ ambiguity อย่างเดียว

### 11.13 Question Frame

ไฟล์หลัก: `app/pipeline/question_frame.py`

#### หน้าที่

สร้าง “สัญญาคำตอบที่คาดหวัง” จาก operation ก่อนเลือก tool

ตัวอย่าง:

```text
operation = control_lookup
expected_answer_types = controls, list, how_to
target_required = true
target_type = game
```

operation ที่ตรวจมีทั้ง control, price, booking, schedule, ranking, studio rules, competition, members, game detail/catalog, equipment และ how-to

#### ทำไม operation-first

category เดียวอาจตอบได้หลายรูปแบบ เช่น games มีทั้งรายชื่อเกม รายละเอียดเกม อันดับโซน และปุ่ม หากรู้เพียง category แต่ไม่รู้ operation มีโอกาสเลือก tool หรือรูปคำตอบผิด

### 11.14 Capability Candidate Scoring

ไฟล์หลัก: `app/pipeline/capability_registry.py`

#### Capability คืออะไร

คือความสามารถที่ execute ได้จริง เช่น:

- `fast.price_calculator`
- `structured.games`
- `structured.game_controls`
- `retrieval.competition_fact_cards`
- `retrieval.hybrid_guarded`
- `llm.general_answer`
- `clarification.ask_user`
- `fallback.no_answer`

#### วิธีให้คะแนน

แต่ละ capability มี base score แล้วรับ boost/penalty จาก:

- domain
- operation
- answer type
- route
- target status
- tool router proposal
- question frame
- policy risk

คะแนนรวมถูก normalize ตามสูตรภายใน ไม่ใช่ probability

#### Selection threshold

- คะแนนผู้ชนะต่ำกว่า `0.45`: abstain
- ถ้า top กับ second ต่าง action กัน, operation ยัง unknown และ margin ต่ำกว่า `0.035`: review/clarify
- หากชัดกว่านั้น: เลือก candidate แต่ยังต้องผ่าน precondition

#### Policy veto

แม้ LLM ได้คะแนนสูง policy ยังห้าม general LLM ตอบข้อมูล PSU ที่ไม่มี evidence และห้าม model-only path ในคำถาม high-risk

### 11.15 Tool Preconditions

ไฟล์หลัก: `app/pipeline/tool_preconditions.py`

#### Precondition คืออะไร

เงื่อนไขขั้นต่ำก่อนเรียกเครื่องมือ เปรียบเสมือนตรวจว่าฟังก์ชันมี input ครบและชนิดถูกหรือไม่

ตัวอย่าง policy:

- booking tool ต้องเป็น booking ไม่ใช่เพียงเห็นคำว่าเกม/อุปกรณ์
- price tool ต้องเป็นราคา ไม่ใช่คำถามขั้นตอนจอง
- competition fact tool ไม่ควรรับ equipment query
- people/member query ไม่ควรวิ่งไป game catalog
- game controls ต้องมี control signal และ target ที่ใช้ได้
- general LLM รับเฉพาะ general domain

#### ทำไม candidate score อย่างเดียวไม่พอ

score อาจสูงจาก keyword ซ้ำ แต่ precondition ตรวจ requirement แบบแข็ง ตัวอย่าง `PS5 มีเกมอะไรและจองยังไง` อาจมี games signal สูง แต่ booking child ต้องไม่ถูกตอบด้วย catalog เพียงเพราะคำว่า PS5

#### เมื่อไม่ผ่าน

candidate ถูก reject พร้อมเหตุผลใน trace แล้วระบบลอง candidate ถัดไปแบบ bounded หรือถามกลับ/no-answer ไม่ควรฝืน execute tool ที่ input ไม่ครบ

---

## 12. สรุปความต่างของ Route, Intent, Target, Frame และ Capability

คำเหล่านี้ดูคล้ายกัน แต่ตอบคนละคำถาม:

| สิ่ง | ตอบคำถามว่า | ตัวอย่าง |
|---|---|---|
| Route | อยู่หมวดระบบใด | `games` |
| Intent/Operation | ผู้ใช้ต้องการทำอะไร | `control_lookup` |
| Target | ทำกับสิ่งใด | เกมที่ resolve ได้หนึ่งรายการ |
| Entities/Filters | มีเงื่อนไขอะไร | วัน, เวลา, ระยะเวลา, user group |
| Question Frame | คำตอบที่ถูกต้องควรมีชนิดใด | controls + how-to และต้องมี game target |
| Capability | จะใช้เครื่องมือใดทำงาน | `structured.game_controls` |
| Mode | สุดท้าย execute ทางใดจริง | `pipeline:structured_game_controls` |

ตัวอย่างทั้งสาย:

```text
คำถาม: "TEKKEN 8 ปุ่มอะไร"

route       = games / game_control_lookup
intent      = game_controls / control_lookup
target      = canonical game record ของ TEKKEN 8
frame       = ต้องตอบ controls และกล่าวถึง target
candidate   = structured.game_controls
precondition= ต้องมี control signal + resolved game
mode        = structured_game_controls หากมีข้อมูลยืนยัน
fallback    = no verified control data หรือ clarification ตามสาเหตุ
```

---

## 13. Decision Trace ที่ใช้ดูว่า Flow เดินอย่างไร

แต่ละ stage บันทึก `PipelineTrace` โดยทั่วไปมี:

```text
stage       ชื่อขั้นตอน
decision    ผลตัดสิน
confidence  คะแนนของ stage
detail      เหตุผลย่อ
metadata    รายละเอียด เช่นคะแนน candidate, timing, model call
```

ตัวอย่าง trace เชิงแนวคิด:

```json
{
  "stage": "ambiguity_gate",
  "decision": "allow",
  "confidence": 0.88,
  "detail": "explicit game target and control operation",
  "metadata": {
    "target": "resolved-game-id",
    "top_intent": "control_lookup",
    "margin": 0.31
  }
}
```

Trace มีไว้ตอบคำถามเชิง debug ว่า:

- เลือก route เพราะอะไร
- target มาจาก input หรือ session
- candidate ใดชนะและ margin เท่าไร
- LLM ถูกเรียกหรือถูก skip เพราะอะไร
- stage ใดใช้เวลามาก
- validator ปฏิเสธ draft ด้วย error ใด

Trace ไม่ควรถูกแสดงเป็นคำตอบหลักให้ผู้ใช้ทั่วไป แต่มีประโยชน์มากในการวิเคราะห์ failure โดยเรียง `mode -> route -> intent -> target -> source -> trace`

---

## 14. Execution Paths: ระบบลงมือหาคำตอบอย่างไร

หลัง candidate selection และ precondition ระบบไม่ได้เรียกทุกเครื่องมือพร้อมกัน แต่เลือกเส้นที่เหมาะ แล้วอาจลองทางสำรองแบบจำกัดเมื่อ draft ไม่ผ่าน validator

### 14.1 Fast Path

#### Fast คืออะไร

Fast path คือฟังก์ชันตอบคำถามที่ออกแบบเฉพาะ pattern ที่พบบ่อยและมี logic ชัด จุดเด่นคือไม่ต้องวางแผนค้นข้อมูลกว้างหรือเรียก model

ตัวอย่างงาน:

- ตรวจคำถามค่าบริการที่ entity ครบแล้วส่งเข้า calculator
- ตอบ schedule/calendar pattern ที่รองรับ
- ตอบ penalty/check-in/reservation facts ที่เป็นรูปแบบตายตัว
- format คำตอบโดเมนที่รู้ route แน่

#### วิธีทำงาน

```text
query + route + entities
  -> ตรวจ pattern เฉพาะ
  -> อ่านค่าที่จำเป็นจากข้อมูล/constant ที่ยืนยันแล้ว
  -> คำนวณหรือประกอบ template
  -> คืน answer + hits + mode + confidence
```

#### ทำไมเรียก Fast

เพราะข้ามขั้น retrieval ranking และ generation ที่ไม่จำเป็น ไม่ได้หมายความว่า logic ง่ายทุกตัว แต่หมายถึงมีทางตรงสำหรับ use case นั้น

### 14.2 Rule Path

Rule path ใช้กฎ `if/then`, phrase matching และ policy response เช่น:

```text
ถ้าคำถามถามนโยบาย X และมี source fact Y
  -> ตอบ template ตาม Y
```

Rule เหมาะกับข้อกำหนดที่คำตอบต้องคงที่และตรวจง่าย ข้อเสียคือ coverage จำกัดตามกฎที่เขียน และต้องแก้ rule/data เมื่อภาษาใหม่เข้ามา

### 14.3 Calculator

Calculator เป็น deterministic function สำหรับโจทย์ตัวเลข เช่นราคาที่ขึ้นกับ service, user group และ duration

```text
input fields ที่ผ่าน validation
  -> lookup rate/rule
  -> คำนวณ
  -> แสดงหน่วยและเงื่อนไข
```

ข้อสำคัญคือ calculator ต้องไม่เดา field ที่หาย หากราคาต่างตามกลุ่มผู้ใช้แต่ผู้ใช้ไม่ระบุ กลไกควรถามกลับหรือแสดงเฉพาะตารางที่ source รองรับตาม question frame

### 14.4 Fast, Rule และ Structured ต่างกันอย่างไร

| แนวทาง | จุดตั้งต้น | วิธีหลัก | เหมาะกับ |
|---|---|---|---|
| Fast | pattern ของคำถาม | เรียก handler ทางตรง | คำถามพบบ่อยและ route ชัด |
| Rule | เงื่อนไขนโยบาย | if/then + fixed/template response | กฎที่ต้องคงเส้นคงวา |
| Calculator | entity ตัวเลข | lookup + arithmetic | ราคา จำนวน ผลต่าง |
| Structured | schema/rows | filter, join, count, group, project | รายการและ fact ที่มี field ชัด |

Fast อาจเรียกข้อมูล structured ภายในได้ และ Structured อาจตอบเร็วมากเช่นกัน คำต่างกันที่ “รูปแบบ ownership ของ logic” ไม่ใช่เส้นแบ่งความเร็วแบบเด็ดขาด

---

## 15. Structured Tools

ไฟล์หลัก: `app/pipeline/structured_tools.py`

### 15.1 Structured data คืออะไร

ข้อมูลที่แต่ละ record มี field ชัดเจน เช่น:

```json
{
  "game_id": "canonical-id",
  "title": "ชื่อเกมจากข้อมูลจริง",
  "zone": "zone-id",
  "platform": "platform-id",
  "genre": ["..."],
  "source_ids": ["..."]
}
```

ระบบสามารถถาม field โดยตรง เช่น `zone == requested_zone` หรือ `game_id == resolved_target`

### 15.2 Structured Tool ทำงานทีละขั้นอย่างไร

```text
1. รับ route + universal intent + resolved target + filters
2. ตรวจว่า domain/operation อยู่ใน handler ที่รองรับ
3. เลือก dataset/schema
4. filter rows ตาม target/zone/platform/วัน/กลุ่มผู้ใช้
5. ทำ operation เช่น count/list/group/rank/calculation
6. format deterministic draft
7. แนบ evidence/hits/source IDs
8. optional: ส่ง draft ให้ facts-only composer
9. validate
```

### 15.3 ตัวอย่าง Structured Games

```text
คำถาม: PS5 มีเกมอะไรบ้าง

intent = games/game_catalog
filter = platform หรือ zone ที่ resolve เป็น PS5
operation = list
ผล = รายชื่อเฉพาะ rows ที่ตรง filter
```

ระบบไม่ต้องใช้ similarity search เพื่อค้นชื่อเกมทั้งหมด เพราะ field บอกอยู่แล้วว่าแต่ละเกมอยู่โซนใด

### 15.4 ตัวอย่าง Structured Members

```text
คำถาม: สมาชิกกลุ่ม X มีกี่คน

filter rows by group_id
count rows
format count + source
```

### 15.5 ตัวอย่าง Structured Controls

```text
คำถาม: [ชื่อเกมที่ resolve แล้ว] ปุ่มอะไร

target_id -> control records ของเกมนั้น
ถ้ามี verified rows -> list controls
ถ้าไม่มี -> no verified control data
```

การไม่มี control row ไม่ได้แปลว่าให้ RAG หรือ LLM เดาปุ่มจากความรู้ทั่วไป เพราะ requirement คือข้อมูลที่ยืนยันสำหรับระบบนี้

### 15.6 Structured Service Fee

อ่าน rate/rule ตาม service, group และ duration ที่มี field ชัด จากนั้น lookup หรือคำนวณ คำตอบต้องมี source ที่เหมาะ โดย PC price ยังมี source-specific contract เพิ่ม

### 15.7 Structured Reservation

ตอบข้อมูลหรือวิธีจองที่ยืนยันแล้ว เช่นขั้นตอนและเงื่อนไข แต่ยังไม่สร้าง booking transaction จริง ไม่มีการล็อกเวลา ชำระเงิน หรือยืนยันการจองแทนผู้ใช้

### 15.8 ทำไม Structured มักเป็นเส้นหลัก

- exact และตรวจสอบได้
- เร็ว
- list/count/filter แม่นกว่า retrieval
- update field เดียวได้โดยไม่ต้องพึ่งการตีความของ model
- validator รู้ expected source category ได้ง่าย

### 15.9 Structured draft กับ LLM composer

Structured Tool สร้างคำตอบที่ใช้ได้เองก่อน หากเปิด `PSU_FACTS_LLM_COMPOSER` และ request อนุญาต LLM จึงอาจให้ Typhoon เรียบเรียง draft โดย prompt ห้ามเพิ่ม fact

```text
structured facts -> deterministic draft -> optional rewrite -> grounding/contract
```

ถ้า composer ปิด, timeout, health fail, source line เปลี่ยน หรือเพิ่มตัวเลขที่ไม่มีใน evidence ระบบใช้ draft เดิม ไม่ทำให้ structured path พึ่ง LLM

### 15.10 ถ้าเก็บทุกอย่างเป็น Structured จะไม่ต้องใช้ RAG หรือไม่

ตอบตรง ๆ: **ถ้าข้อมูลทั้งหมดแปลงเป็น schema ได้ครบ ถูกต้อง อัปเดตทัน และคำถามต้องการเฉพาะ field/operation ที่ schema รองรับ ก็ไม่จำเป็นต้องใช้ RAG สำหรับข้อมูลส่วนนั้น**

แต่ต้นทุนจะย้ายไปอยู่ที่:

- ออกแบบ schema
- แปลงเอกสารทุกฉบับเป็น row
- รักษาความสอดคล้องเมื่อกฎ/ข่าวเปลี่ยน
- รองรับคำถามอธิบายยาวหรือรายละเอียดที่ schema ไม่ได้เก็บ

ดังนั้น Structured เหมาะกับ stable atomic facts ส่วน RAG มีประโยชน์กับข้อความอธิบาย กฎฉบับเต็ม ข่าว/กิจกรรม และเอกสารที่โครงสร้างเปลี่ยนบ่อย

---

## 16. Competition Fact Cards

### 16.1 Fact card คืออะไร

เป็นทางกลางระหว่าง Structured row กับเอกสารเต็ม โดยแตกเอกสารกติกาเป็นข้อเท็จจริงย่อยที่มี metadata ชัด

```text
competition/game/topic -> fact text -> source ID -> trust/update metadata
```

ตัวอย่าง topic เชิงประเภท:

- จำนวนผู้เล่น
- รูปแบบ BO1/BO3
- map pool
- pause/timeout
- อุปกรณ์
- penalty

### 16.2 ทำไมไม่ใช้ RAG จาก PDF ทั้งก้อน

- ลดโอกาสดึงย่อหน้าผิดหัวข้อ
- แยกกฎคนละเกม/ทัวร์นาเมนต์
- validator ตรวจ source/category ได้ง่าย
- คำตอบสั้นและรักษาตัวเลขได้ดีขึ้น

### 16.3 Guard ที่ต้องมี

- game/competition target match
- topic match
- source ID ที่ยืนยัน
- ไม่รวม fact cards คนละกฎโดยไม่มี claim relation

หาก target หรือการแข่งขันไม่ชัดควรถามกลับ ไม่ควรเลือกกติกาที่ชื่อคล้าย

---

## 17. Game-control Vector-first

### 17.1 ทำไม controls มี path เฉพาะ

ข้อมูล controls มีชื่อปุ่มและคำอธิบายจำนวนมาก การค้นด้วย title/target แล้วจัดอันดับข้อความอาจยืดหยุ่นกว่าการ hard-code ทุกคำถาม แต่ความผิดพลาดมีผลชัด เพราะปุ่มของเกมหนึ่งใช้แทนอีกเกมไม่ได้

### 17.2 Flow

```text
control operation + resolved game target
  -> retrieve เฉพาะ category game_controls
  -> บังคับ entity/game match
  -> rank candidate documents
  -> optional rerank เมื่อเงื่อนไขพร้อม
  -> สร้าง answer จาก verified hit
  -> answer contract ตรวจ target + answer type controls
```

### 17.3 เหตุผลที่เรียก vector-first แต่ยัง guarded

vector ช่วยหาเอกสารที่ถ้อยคำคล้าย query แต่ไม่รู้โดยอัตโนมัติว่าเอกสารเป็นของเกมเดียวกัน จึงต้องมี metadata/category/entity guard ครอบ similarity

### 17.4 เมื่อไม่มี target

`ปุ่มอะไร` โดยไม่มี game context จะไม่ควร search ทุก control document แล้วเลือกอันดับหนึ่ง เพราะอันดับหนึ่งอาจเป็นเพียงเอกสารที่มีคำว่า `ปุ่ม` มากที่สุด ผลที่ปลอดภัยคือถามชื่อเกม

---

## 18. RAG แบบละเอียด

### 18.1 RAG คืออะไร

RAG ย่อจาก Retrieval-Augmented Generation ในความหมายกว้างคือ:

```text
ค้นข้อมูลที่เกี่ยวข้องก่อน (Retrieval)
  -> ใช้ข้อมูลนั้นสร้าง/เรียบเรียงคำตอบ (Augmented Answer/Generation)
```

RAG ไม่จำเป็นต้องมี LLM เสมอ ในระบบนี้สามารถ:

- retrieve แล้วประกอบ deterministic answer
- retrieve แล้วให้ Local LLM composer เรียบเรียงเมื่อ gate อนุญาต

ทั้งสองแบบยังเป็น retrieval-grounded path

### 18.2 เมื่อใด RAG มีประโยชน์

- ข้อมูลเป็นข้อความยาวและไม่ได้แตก field ครบ
- ผู้ใช้ใช้ถ้อยคำหลากหลายกว่าคีย์ schema
- ต้องหา passage จาก FAQ/knowledge/news/rules
- ต้องแสดงหลักฐานต้นฉบับหรือ URL
- มีเอกสารใหม่เข้าบ่อยและยังไม่คุ้มแปลงทุกประโยคเป็น structured rows

### 18.3 เมื่อใดไม่ควรใช้ RAG

- รายชื่อเกมทั้งหมดที่มี field zone ชัด
- การนับ/จัดอันดับจาก rows
- ราคาและการคำนวณที่มี rate schema
- exact member/equipment lookup
- operation ที่ target ขาด เพราะ retrieval อันดับหนึ่งไม่ใช่การ resolve ambiguity

### 18.4 Guarded Hybrid RAG Flow

ไฟล์หลัก: `app/pipeline/hybrid_retrieval.py`, `retrieval.py`, `vector_retrieval.py`

```text
query + category + target
  -> กำหนด retrieval budget
  -> Curated Retrieval
  -> Local Vector Retrieval
  -> category/entity/competition guards
  -> merge + deduplicate
  -> hybrid score
  -> optional BGE rerank
  -> source assessment
  -> evidence packing
  -> deterministic draft หรือ grounded composer
```

### 18.5 Retrieval budget

Budget ตรงนี้หมายถึงจำนวน candidate ไม่ใช่เวลา:

- query ปกติ: candidate ราว 8, final ราว 4
- broad/complex: candidate ราว 12, final ราว 5

การจำกัดจำนวนช่วยลดเวลารerank และขนาด prompt

### 18.6 Curated Retrieval

#### Curated คืออะไร

ข้อมูลที่คัดและจัด metadata ไว้แล้ว เช่น knowledge/news/FAQ/fact rows

#### เทคนิคจริง

ใช้ weighted lexical/token/entity/priority scoring จากคำที่ปรากฏและ metadata ไม่ได้ใช้ BM25 library เต็มรูปแบบใน implementation ปัจจุบัน

สัญญาณเช่น:

- token overlap ระหว่าง query กับ title/text
- exact phrase
- entity match
- category match
- source priority

ข้อดีคืออธิบายคะแนนได้และทำงานเร็ว ข้อจำกัดคือคำพ้องที่ไม่มีตัวอักษรร่วมกันอาจค้นไม่เจอ

### 18.7 Local Vector Retrieval

#### Vector คืออะไร

vector คือชุดตัวเลข/น้ำหนักที่แทน feature ของข้อความ แล้ววัดว่าข้อความสองชุดอยู่ใกล้กันเพียงใด

#### Implementation ปัจจุบัน

`local_hash_char_ngram_v1` สร้าง sparse features จาก character n-gram และคำ แล้วใช้ cosine similarity ร่วมกับ lexical/entity/priority score

```text
score โดยแนวคิด
= vector similarity x weight
+ lexical overlap x weight
+ entity match x weight
+ source priority
```

นี่ช่วยเรื่องรูปคำที่คล้ายและ typo บางส่วน แต่ยังไม่เข้าใจ semantic ลึกแบบ embedding model เช่นคำพ้องที่เขียนต่างกันทั้งหมด

### 18.8 Category Guard

ถ้าถามข่าว ไม่ควรให้ game catalog document ชนะเพียงเพราะมีชื่อเกมเดียวกัน ระบบจึงกรอง/ลงโทษ candidate ที่ category ไม่สอดคล้องกับ route/intent

### 18.9 Entity Guard

ถ้ามี resolved target เอกสารต้องกล่าวถึงหรือผูก metadata กับ target นั้น โดยเฉพาะ controls และ competition rules

### 18.10 Competition Guard

ป้องกันการนำกติกาคนละเกมหรือคนละ event มารวมกัน ต้อง match competition/game/topic ตามข้อมูลที่มี

### 18.11 Merge และ Deduplicate

เอกสารเดียวกันอาจถูกเจอจาก curated และ vector จึงรวมโดย key เช่น source ID/file/URL และตัด duplicate เพื่อไม่ให้ passage เดียวครองหลาย slot

candidate ที่มาจากสองวิธีอาจได้ dual-origin bonus เพราะมีสัญญาณสนับสนุนสองทาง แต่ยังไม่แทน source authority

### 18.12 Hybrid score

implementation ผสมคะแนนฐานกับองค์ประกอบโดยประมาณ:

```text
hybrid score
= base score
+ vector score x 6
+ lexical score x 3
+ entity score x 5
+ priority
+ dual-origin bonus เมื่อเข้าเงื่อนไข
```

น้ำหนักเหล่านี้เป็น ranking policy ต้องประเมินจาก retrieval test ไม่ใช่ probability ของความถูกต้อง

### 18.13 ทำไม Hybrid ดีกว่าใช้วิธีเดียว

- lexical เก่งกับชื่อเฉพาะ ตัวเลข และคำตรง
- char vector รับความต่างรูปคำได้บางส่วน
- entity/category guard บังคับ domain correctness
- source priority ช่วยให้ข้อมูลทางการอยู่เหนือข้อมูลรอง

การรวมหลายสัญญาณลดจุดอ่อนของแต่ละวิธี แต่ไม่ได้ทำให้ retrieval ถูกเสมอ จึงยังมี rerank/source guard/validator

---

## 19. BGE Document Reranker

ไฟล์หลัก: `app/pipeline/document_reranker.py`

### 19.1 Rerank คืออะไร

Retrieval รอบแรกเน้นเร็วและกว้าง ได้ candidate list จากนั้น reranker ใช้วิธีที่หนักกว่าอ่านคำถามกับแต่ละ candidate ร่วมกัน แล้วจัดลำดับใหม่

```text
retrieve: 100% ของคลัง -> candidate เล็ก ๆ
rerank: candidate เล็ก ๆ -> final top documents
```

### 19.2 CrossEncoder คืออะไร

BGE reranker เป็น CrossEncoder: นำข้อความคำถามและเอกสารเข้า model พร้อมกัน ทำให้ model เห็นความสัมพันธ์ระหว่าง token ของทั้งคู่โดยตรง

ต่างจาก embedding retrieval:

- Bi-encoder/embedding: encode query และ docs แยกกัน เร็วและทำ index ได้
- CrossEncoder: encode เป็นคู่ทุก candidate ช้ากว่า แต่โดยทั่วไปแยกความเกี่ยวข้องละเอียดกว่า

### 19.3 เงื่อนไขเรียกปัจจุบัน

- feature เปิด
- มีอย่างน้อย 2 hits จึงมีสิ่งให้จัดอันดับ
- deadline เหลืออย่างน้อยประมาณ 3 วินาที
- ถ้า model ยัง cold ต้องมีเวลาคงเหลือประมาณ 30 วินาที มิฉะนั้น skip เพื่อไม่ให้ cold load อยู่ใน request
- rerank candidate ไม่เกินประมาณ 8 รายการ

### 19.4 BGE cold load 93.46 วินาทีหมายถึงอะไร

เป็นเวลาที่เคยวัดในการโหลด model/runtime ครั้งแรก ไม่ใช่ inference warm ทุก request สาเหตุอาจรวมอ่าน weights จาก disk, initialize PyTorch/transformers, allocate RAM/VRAM และสร้าง kernels/runtime state

หลัง model ถูก cache ต่อ process การ rerank จะใช้เวลาน้อยลง แต่หาก process ใหม่ก็ cold ใหม่

### 19.5 ถ้า BGE ใช้ไม่ได้

จับ exception หรือ skip แล้วคืนลำดับจาก hybrid score ระบบ retrieval ยังทำงาน ไม่ควรให้ optional reranker ทำ request ทั้งก้อน fail

### 19.6 Reranker ไม่รับรอง source correctness

BGE ตอบเพียงว่า passage ใดสัมพันธ์กับคำถามมากกว่า มันไม่ได้ยืนยันว่า source เป็นทางการ ล่าสุด หรือไม่มีตัวเลขขัดกัน จึงต้องผ่าน Source Guard หลังจากนั้น

---

## 20. Evidence Packer

ไฟล์หลัก: `app/pipeline/evidence_packer.py`

### 20.1 ทำไมต้อง pack evidence

การส่งเอกสารเต็มทุกชิ้นให้ LLM ทำให้ prompt ใหญ่ ช้า และมีข้อมูลรบกวน Evidence Packer จึงสร้างชุดหลักฐานขนาดจำกัดและติดป้าย source ชัด

### 20.2 ขั้นตอน

1. รับ final hits หลัง ranking
2. deduplicate ตาม source และ normalized text
3. ตัด passage ตามความยาวสูงสุด
4. จำกัดจำนวน items
5. รวม metadata ที่จำเป็น
6. สร้างข้อความ/JSON compact สำหรับ composer และ validator

### 20.3 ขนาดปัจจุบัน

ค่าเริ่มต้นประมาณ:

```text
สูงสุด 4 items
รวมไม่เกิน 4,200 characters
```

### 20.4 Field ที่แพ็ก

- source ID
- title
- text/passages
- category
- URL
- trust level
- updated time
- retrieval/rerank score

### 20.5 ข้อแลกเปลี่ยน

- pack ใหญ่: coverage ดีขึ้นแต่ prompt ช้าและ distract model
- pack เล็ก: เร็วแต่เสี่ยงตัด subanswer ที่อยู่ใน passage อันดับรอง

จึงต้องติดตาม missing subanswer และ retrieval recall จาก benchmark ไม่ใช่ปรับขนาดจากความรู้สึกอย่างเดียว

---

## 21. Source Guard

ไฟล์หลัก: `app/pipeline/source_guard.py`

### 21.1 หน้าที่

ประเมินคุณภาพที่มาของ hits ก่อนให้ composer หรือ final answer ใช้

### 21.2 Authority rank

ลำดับปัจจุบัน:

| Trust level | Rank |
|---|---:|
| `official` | 4 |
| `user_confirmed` | 3 |
| `internal_verified` | 2 |
| `secondary` | 1 |
| ไม่ระบุ | 0 |

rank ใช้เป็น metadata/policy signal ไม่ได้พิสูจน์ว่าเนื้อหาใน source ถูกทุกบรรทัด

### 21.3 Source ID

ระบบรวบรวม source IDs ที่ไม่ซ้ำ หากไม่มี source ID จะเพิ่ม warning `missing_source_id` เพราะตรวจ provenance ย้อนกลับได้ยาก

### 21.4 Claim key และ numeric conflict

หาก hit มี `claim_key` หรือ `fact_key` ระบบใช้ key นั้นจัดกลุ่มตัวเลขที่อ้าง claim เดียวกัน หากไม่มี key จะใช้ ID/source/title แยกเอกสาร เพื่อไม่ให้วันที่หรือจำนวนในข่าวคนละชิ้นถูกมองว่า conflict กันทันที

implementation ปัจจุบันตั้ง `conflict=true` เมื่อกลุ่ม `(category, claim_key)` เดียวมีค่าตัวเลขต่างกันมากกว่า 3 ค่า

นี่เป็น heuristic ง่าย ๆ ไม่ใช่ semantic contradiction detector จึงอาจ:

- ไม่จับ conflict ที่มีเพียง 2 ค่าขัดกัน
- มอง list ตัวเลขหลายค่าที่ถูกต้องเป็นเรื่องต้อง review หากใช้ claim key กว้างเกิน

การออกแบบ `claim_key` จึงสำคัญ และควรเพิ่ม test ก่อนพึ่ง guard นี้ในกฎซับซ้อน

### 21.5 Staleness: ข้อเท็จจริงของ implementation ปัจจุบัน

เอกสาร Flow หลักกล่าวถึงการตรวจ stale metadata แต่ `assess_sources()` ปัจจุบันคืน `stale=False` เสมอ ยังไม่ได้เปรียบเทียบ `updated_at`, expiry หรือ effective date จริง

ดังนั้นตอนนี้:

- metadata เวลาอาจถูกแพ็กและบันทึก
- แต่ Source Guard ยัง **ไม่ได้ enforce freshness**
- ข่าว ตาราง หรือกฎที่มีอายุควรมี freshness policy เพิ่มก่อนถือว่าตรวจ stale แล้ว

นี่เป็นข้อจำกัดสำคัญ ไม่ควรอธิบายว่าระบบป้องกันข้อมูลเก่าครบแล้ว

### 21.6 เมื่อมี conflict

Model Gateway ไม่ควรส่ง evidence ที่ conflict ไปให้ composer เพื่อให้ LLM “เลือกเอง” เพราะ LLM อาจเขียนคำตอบลื่นแต่ปกปิดความขัดแย้ง ทางที่ปลอดภัยคือใช้ deterministic review, เลือก source ตาม policy ที่ชัด หรือ no-answer/ถามเจ้าหน้าที่

---

## 22. Draft Answer จาก RAG

หลังได้ hits ระบบมีสองทาง:

### 22.1 Deterministic RAG answer

เลือก/สรุป passage ด้วย template และ formatter โดยไม่เรียก LLM เหมาะเมื่อ hit เดียวหรือ fact card ตอบตรงคำถามอยู่แล้ว

ข้อดี:

- เร็ว
- ไม่เกิด hallucination จาก generation
- รักษาตัวเลข/source ง่าย

ข้อจำกัด:

- ภาษาอาจแข็ง
- รวมหลาย passage หรือหลาย subanswer ได้ไม่เป็นธรรมชาติเท่า composer

### 22.2 Grounded LLM composer

ส่ง evidence pack และ deterministic draft ให้ Typhoon เรียบเรียง โดยมี prompt ห้ามเพิ่ม fact รายละเอียดอยู่ในหัวข้อถัดไป

---

## 23. ข่าวและกฎควรเป็น Structured หรือ RAG

คำตอบตรงไปตรงมา:

### ข่าว/กิจกรรม

ให้ใช้ RAG เป็นหลักเมื่อเนื้อหามาเป็นบทความ มีวัน ชื่อกิจกรรม รายละเอียด และอัปเดตบ่อย แต่ควร extract field สำคัญเป็น structured metadata ด้วย เช่น:

- event ID
- title
- start/end date
- status
- source URL
- published/updated time

วิธีที่เหมาะคือ **structured metadata + RAG body** ไม่ใช่เลือกอย่างใดอย่างหนึ่งทั้งหมด

### กฎ

- กฎที่ใช้ตัดสินคำตอบบ่อยและเป็น atomic fact ควรทำ Structured/Fact Card เช่นจำนวนผู้เล่นหรือรูปแบบการแข่งขัน
- ข้อยกเว้น รายละเอียด และข้อความต้นฉบับควรเก็บใน RAG พร้อม source
- กฎที่มีผลตามวันที่ต้องมี version/effective date/freshness policy

### ทำไมไม่ใช้ RAG เฉพาะข่าวอย่างเดียว

RAG ยังมีประโยชน์กับ FAQ อธิบายยาว คู่มือ เอกสารกฎต้นฉบับ และ knowledge ที่ไม่คุ้มแตก schema ทุกประโยค แต่หากข้อมูลปัจจุบันส่วนใหญ่ structured จริง สัดส่วน RAG ใน production ต่ำก็เป็นเรื่องปกติ ไม่ควรบังคับใช้ RAG เพื่อให้ตัวเลข usage สูง

---

## 24. Local LLM ทำงานตรงไหนบ้าง

Model หลักปัจจุบัน: `scb10x/typhoon2.5-qwen3-4b` ผ่าน Ollama ในเครื่อง

### 24.1 Local LLM หมายถึงอะไร

model inference รันบนเครื่อง/เซิร์ฟเวอร์ของระบบผ่าน local HTTP API ของ Ollama ไม่ได้ส่ง prompt ไป cloud model โดย design ปัจจุบัน

Local ไม่ได้แปลว่าไม่มีต้นทุน:

- ใช้ RAM/VRAM
- ใช้ CPU/GPU compute
- มี queue และ concurrency limit
- มี cold load
- token generation ยังใช้เวลาหลายวินาที

### 24.2 บทบาทของ LLM แต่ละตัว

| บทบาท | Input | Output | อยู่ในคำตอบจริงหรือไม่ |
|---|---|---|---|
| Query Planner | query ซับซ้อน | JSON tasks | ช่วยวางแผน ไม่ใช่คำตอบ |
| Intent Review | route/สัญญาณที่ยังอ่อน | domain/operation JSON | ช่วย refine |
| Tool Router | intent/target/candidates | tool proposal JSON | เป็นข้อเสนอ |
| Facts Composer | evidence + deterministic draft | คำตอบเรียบเรียงใหม่ | อาจเป็น final หากผ่าน guard |
| General Fallback | คำถามทั่วไปที่ policy อนุญาต | general answer | ใช้เฉพาะ non-PSU/general |
| Experimental Fallback | context ที่ feature gate อนุญาต | ทดลอง RAG/answer | ไม่ใช่แกนหลัก |
| Shadow Critic | result + expected contract | verdict/labels | ใช้ตรวจงาน/evaluation ไม่ควรอยู่ใน synchronous user path ปกติ |

### 24.3 Gated LLM คืออะไร

LLM ไม่ได้ถูกเรียกเพียงเพราะเปิด model แต่ต้องผ่านหลายเงื่อนไข:

```text
feature enabled?
  -> request allows LLM?
  -> role เหมาะกับ route นี้?
  -> deadline เหลือพอ?
  -> ยังมี call budget?
  -> health circuit เปิด?
  -> concurrency slot ว่าง?
  -> evidence/source พร้อมถ้าเป็น PSU facts?
  -> call model
```

ถ้าข้อใดไม่ผ่าน ระบบ skip/fallback และบันทึกเหตุผล

### 24.4 Model-first หมายถึงอะไร

`PSU_MODEL_FIRST_FLOW` เป็น feature flag ที่เพิ่มบทบาท model-assisted flow แต่ไม่ได้แปลว่าให้ LLM ข้าม structured/RAG evidence โดยค่าเริ่มต้น model-first ปิด และแม้เปิดก็ยังมี precondition, source guard และ final contract

### 24.5 Facts-only Composer

ไฟล์หลัก: `app/pipeline/facts_composer.py`

Composer ได้รับ:

- `QUESTION`
- `ROUTE`
- `INTENT`
- `FACTS_JSON`
- `DRAFT_ANSWER`

prompt กำหนดว่า:

- ใช้เฉพาะ facts และ draft
- ห้ามเพิ่มชื่อเกม ราคา เวลา จำนวนคน จำนวนเครื่อง หรือกฎ
- รักษาตัวเลขและ source line
- ตอบ answer-first
- ห้ามบอกว่ากำลัง compose หรือเป็น AI

### 24.6 Composer modes

Composer รับเฉพาะ allowlisted modes เช่น structured member/game/equipment/schedule/reservation/fee และ RAG modes ที่กำหนด ไม่ได้ rewrite ทุกคำตอบ

- Structured composer เปิดด้วย `PSU_FACTS_LLM_COMPOSER`
- RAG composer ใช้ `PSU_RAG_LLM_COMPOSER` หรือสืบจาก model-first policy
- request ยังต้องเปิด `experimental_allow_llm`

### 24.7 Runtime config ของ composer

ค่าหลักปัจจุบัน:

```text
timeout configured = 8s แต่ถูกบีบด้วย global deadline
num_predict        = 64
num_ctx            = 3072
temperature        = 0.05
top_p              = 0.75
stream             = true
keep_alive         = 10m
think              = false โดย default
```

#### num_predict

จำนวน token สูงสุดที่อนุญาตให้ model สร้าง ค่าน้อยช่วยเวลาแต่คำตอบยาวอาจถูกตัด

#### num_ctx

ขนาด context window ที่จัดให้ request รวม prompt/evidence/output ยิ่งใหญ่ยิ่งใช้ memory/compute มาก จึงใช้ Evidence Packer จำกัด prompt ด้วย

#### temperature

ควบคุมความสุ่ม ค่า `0.05` ต่ำเพื่อให้เรียบเรียงข้อเท็จจริงคงที่ขึ้น แต่ temperature ต่ำไม่ได้ป้องกัน hallucination จึงยังต้อง validate

#### streaming

Ollama ส่งข้อความเป็นหลาย JSON lines ทีละช่วง ระบบสะสม field `response` จน `done=true` ข้อดีคือสามารถปิด response socket เมื่อหมดเวลาได้เร็วกว่ารอ body ก้อนเดียว

### 24.8 LLM Health Manager

ไฟล์หลัก: `app/pipeline/llm_health.py`

#### Circuit breaker คืออะไร

เมื่อ model ล้มเหลวซ้ำ การลองต่อทุก request จะทำให้ทุกคนรอ timeout Circuit breaker จึงปิดการเรียกชั่วคราว

ค่าเริ่มต้น:

- failure threshold: 2
- cooldown: 90 วินาที
- เก็บ state ทั้งระดับ kind/model และภาพรวม model

```text
success -> reset failures
failure ครั้งที่ 1 -> degraded
failureถึง threshold -> circuit cooldown
request ระหว่าง cooldown -> skip model ทันที
ครบ cooldown -> อนุญาตลองใหม่
```

### 24.9 Preflight กับ Health ต่างกันอย่างไร

- Preflight คือการทดลอง call สั้นตอน startup
- Health Manager คือ state ที่ใช้ทุก call เพื่ออนุญาต/ระงับ model
- preflight fail สามารถเปิด circuit ตั้งแต่ก่อน user request

### 24.10 LLM concurrency slot

Health Manager ยังเป็นจุดขอ semaphore ของ model ค่า default 1 เพื่อป้องกัน inference หลาย call แย่งเครื่องจน latency ทุก call พุ่ง

slot ที่ได้อาจถูก reuse ภายใน context เดียวตาม implementation แต่ทุก call ยังต้องผ่าน per-request call budget

### 24.11 Hard cancellation ทำได้แค่ไหน

เมื่อ timeout ระบบปิด streaming HTTP response ซึ่งเป็นวิธี cancel ที่แรงที่สุดที่ integration ปัจจุบันทำผ่าน Ollama endpoint แต่เป็น best effort:

- client หยุดอ่าน/ปิด socketได้
- backend model อาจใช้เวลาหยุดจริง
- ไม่มี process-level kill ต่อ request

จึงยังต้องวัด GPU/CPU หลัง client timeout ว่างานเก่ายังค้างหรือไม่

### 24.12 General Local LLM

ใช้กับความรู้ทั่วไปที่ policy อนุญาตและไม่มี PSU-specific fact ที่ต้องมี source หากคำถามมีสัญญาณ PSU แต่ฐานข้อมูลไม่มีคำตอบ ระบบต้อง no-answer ไม่ส่งให้ general model เดา

### 24.13 Shadow Critic

Shadow Critic ตรวจคำตอบภายหลังโดยใช้ deterministic labels ก่อน แล้ว LLM เป็น second opinion เช่น:

- wrong route
- wrong intent/target
- missing subanswer
- unsupported claim
- source mismatch
- unnecessary LLM call
- timeout

มันไม่ควรแก้คำตอบสดให้ผู้ใช้และไม่ควรนับเป็น latency ปกติของ production request เว้นแต่มีการนำไปผูก synchronous flow ในอนาคต

### 24.14 ห้ามรายงานแหล่งคำตอบผิด

ถ้าคำตอบสุดท้ายมาจาก Fast, Rule, Structured หรือ RAG deterministic ระบบไม่ควรบอกผู้ใช้ว่า LLM เป็นผู้ตอบ แม้ LLM อาจเคยช่วย planner/intent ภายใน เพราะข้อเท็จจริงมาจาก tool/evidence path

---

## 25. Formatter, Validation, Repair และ Final Hard Veto

### 25.1 ทำไมต้องตรวจหลังได้ draft

route อาจถูกแต่คำตอบผิดชนิด target หาย source ผิด หรือ composer เพิ่มตัวเลขได้ การมี answer string ไม่ได้แปลว่าพร้อมส่งผู้ใช้

### 25.2 Formatter

ไฟล์หลัก: `app/pipeline/formatter.py`

หน้าที่:

- trim คำตอบว่าง/ช่องว่าง
- ถ้าไม่มีคำตอบ สร้างข้อความ no-answer ตาม category
- รองรับ short-answer mode
- เติม source URL จาก hits หากยังไม่มีและประเภทคำตอบอนุญาต
- ไม่เติม source line บางชนิดใน safe no-answer

Formatter จัดรูป ไม่ใช่ตัวพิสูจน์ fact

### 25.3 Thai response style

ก่อนคืนผล `_build_result()` เรียก style formatter เพื่อรักษารูปแบบภาษาไทย answer-first และ presentation consistency โดยไม่ควรเปลี่ยนข้อเท็จจริง

### 25.4 Base Validator

ไฟล์หลัก: `app/pipeline/validator.py`

ตรวจ regression/pattern ที่เคยเสี่ยง เช่น:

- schedule ตอบ `24 ชั่วโมง` ทั้งที่ผู้ใช้ไม่ได้ถาม
- price query ถูกตอบเป็น game catalog
- booking ถูกตอบเป็น equipment/game list
- controls ถูกตอบเป็น catalog หรือ game detail ที่ไม่มีปุ่ม
- specific game detail ถูกตอบเป็นรายชื่อเกมทั้งหมด
- competition/member query ถูกส่งไป game catalog
- broad bare query ควรถามกลับ
- PC price ต้องมี source update ที่กำหนด

บางรายการเป็น error ที่ทำให้ draft fail บางรายการเป็น warning สำหรับ observability

### 25.5 Answer Contract

ไฟล์หลัก: `app/pipeline/answer_contracts.py`

Contract เปรียบเทียบ expected answer จาก Question Frame กับสิ่งที่ draft มีจริง

#### ตรวจชนิดคำตอบ

```text
expected = controls/list/how_to
actual   = game_catalog/list
ผล       = type mismatch
```

#### ตรวจ target coverage

ถ้า operation เป็น control/game detail/how-to/booking ที่เจาะเกม คำตอบต้องมี target ที่ resolve แล้ว ไม่ใช่พูดถึงเกมอื่นหรือคำตอบทั่วไป

#### ตรวจ evidence

route ที่ไม่ใช่ general/unknown ต้องมี hits เมื่อ contract กำหนด และ source category ต้องไม่ขัดกับ operation เช่น controls ควรมาจาก `game_controls`

#### ตรวจ ambiguity

ถ้า frame ระบุ `needs_clarification=true` คำตอบต้องเป็น clarification/no-answer ไม่ใช่ตอบ fact เลย

### 25.6 Grounding Claim Validator

ไฟล์หลัก: `app/pipeline/claim_validator.py`

ใช้กับ RAG composer เพื่อเทียบคำตอบกับ evidence pack

#### ตรวจตัวเลข

1. ดึงตัวเลขจาก answer
2. ดึงตัวเลขจาก evidence text/title
3. หา `answer_numbers - evidence_numbers`
4. ถ้ามีตัวเลขใหม่ ให้ `ok=false`

ตัวอย่าง:

```text
evidence numbers = {2, 60}
answer numbers   = {2, 60, 100}
unsupported      = {100}
```

#### ตรวจ token overlap ของ claims

แบ่งคำตอบเป็นประโยค/บรรทัดที่ยาวพอ แล้ววัดสัดส่วน token ที่พบใน evidence หาก overlap ต่ำกว่า `0.08` และประโยคไม่มีตัวเลข จะบันทึก `unsupported_claims`/warning

#### ข้อจำกัดสำคัญ

ปัจจุบัน `GroundingValidation.ok` ตัดสิน fail จาก unsupported numbers เป็นหลัก ส่วน low-overlap text claim ถูกบันทึกเป็น warning แต่ไม่ได้ทำ `ok=false` เอง ดังนั้นยังไม่ใช่ semantic entailment validator และอาจพลาด claim ที่เขียนใหม่โดยไม่มีตัวเลข

### 25.7 Composer-specific safety checks

ก่อนรับข้อความ LLM ตรวจเพิ่มว่า:

- คำตอบไม่ว่าง
- ไม่มี `FINAL_ANSWER` หรือ `FACTS_JSON` หลุดออกมา
- source line จาก draft ไม่หาย
- source line ไม่ถูกแก้
- RAG answer ไม่มี unsupported numeric claim ตาม grounding validator

ถ้าไม่ผ่าน composer คืน deterministic draft เดิมและระบุ `used_llm=false`

### 25.8 Bounded Repair

คำว่า bounded หมายถึงจำกัดจำนวนและชนิดการซ่อม ไม่วนจนกว่าจะได้คำตอบ

พฤติกรรมสำคัญใน `engine.py`:

- หาก early fast candidate ถูก validator ปฏิเสธ ให้ลอง candidate deterministic ถัดไป
- หาก structured draft ถูกปฏิเสธ ให้ mark candidate หมดสิทธิ์และลองทางถัดไป
- trace ระบุ `attempt=1`, `max_attempts=1` ใน branch หลัก
- หาก LLM composer ไม่ปลอดภัย ให้กลับ draft ไม่เรียก model ซ้ำไม่จำกัด

การจำกัดหนึ่ง retry ช่วยป้องกัน latency spiral และ loop ที่แต่ละ path ตอบผิดคนละแบบ

### 25.9 Final Validation

ใน `_build_result()` ระบบรวมผล validation เดิมกับการตรวจแหล่งข้อมูลรอบท้าย หากมี error ใหม่หรือ error เดิมคงอยู่ จะไม่ส่ง draft เสี่ยงออก

### 25.10 Final Hard Veto

หาก final validation ไม่ผ่าน:

```text
เก็บ rejected mode/route/errors ใน trace
  -> เปลี่ยน answer เป็น format_no_answer(...)
  -> ล้าง hits ที่ไม่ควรแสดงกับคำตอบถูก veto
  -> mode = pipeline:answer_contract_no_answer
  -> route = no_answer/answer_contract_rejected
  -> ลด confidence ไม่เกินประมาณ 0.45
  -> บันทึก warning ว่า draft ถูก reject
```

Hard Veto คือด่านสุดท้ายที่ยอมตอบน้อยลงเพื่อไม่ส่งคำตอบผิด

### 25.11 Clarification กับ No-answer ต่างกันอย่างไร

- **Clarification**: ข้อมูลอาจมี แต่คำถามขาด target/เงื่อนไข เช่น `ราคาเท่าไหร่`
- **No-answer**: คำถามชัดแล้ว แต่ไม่มีข้อมูลที่ยืนยันได้ เช่น target ชัดแต่ไม่มี control source ที่ผ่านเกณฑ์

ไม่ควรถามกลับเมื่อรู้ว่าฐานข้อมูลไม่มี fact อยู่แล้ว และไม่ควร no-answer เมื่อเพียงขาด field ที่ผู้ใช้สามารถระบุเพิ่มได้

---

## 26. Fallback Matrix แบบอธิบายเหตุผล

| เหตุการณ์ | เหตุผลที่ไม่ไปต่อ | ผลที่ควรได้ |
|---|---|---|
| reference มีหลาย target | เดาแล้วเสี่ยงตอบผิดเกม/เครื่อง | clarification |
| operation ต้องมี target แต่ไม่มี | tool precondition ไม่ครบ | clarification |
| PSU fact ไม่มี evidence | general model อาจแต่ง | no-answer |
| planner timeout/JSON fail | plan เชื่อถือไม่ได้ | deterministic plan |
| LLM health cooldown | การ call ซ้ำมีแนวโน้ม timeout | structured/RAG draft หรือ no-answer |
| LLM slot ไม่ว่าง | รออาจเกิน deadline | skip/fallback |
| composer เพิ่มตัวเลข | ไม่ grounded | ใช้ draft เดิม |
| BGE cold และเวลาไม่พอ | cold load เกิน product budget | ใช้ hybrid score |
| source conflict | ไม่รู้ค่าใดถูก | deterministic review/no-answer |
| candidate margin ต่ำ | tool choice ยังไม่ชัด | abstain/clarification |
| validator fail | draft ผิด contract | bounded retry แล้ว hard veto |
| global deadline หมด | ไม่มีเวลาตรวจงานหนักต่อ | timeout-safe no-answer |

---

## 27. Build Result, Decision Artifact และ Output

### 27.1 PipelineAnswer

ผลภายในมีข้อมูลหลัก:

- `answer`: ข้อความสุดท้าย
- `mode`: path ที่ execute จริง
- `route`: category/intent/answer type/risk
- `universal_intent`
- `confidence`
- `entities`
- `hits`
- `validation`
- `trace`
- `decision_artifact`
- `elapsed`

### 27.2 Mode สำคัญอย่างไร

`mode` บอกสิ่งที่เกิดจริง จึงใช้วิเคราะห์ก่อนคำอธิบายเชิงคาดเดา ตัวอย่าง prefix:

- `pipeline:structured_...`
- `pipeline:...fast...`
- `pipeline:...hybrid...`
- `pipeline:...vector...`
- `pipeline:...clarification...`
- `pipeline:answer_contract_no_answer`

หากคำตอบผิด ควรเริ่มจาก mode แล้วไล่ route/intent/target/source/trace

### 27.3 Decision Artifact

ไฟล์หลัก: `app/pipeline/decision_artifact.py`

เป็นสรุป machine-readable ของการตัดสินใจ เช่น:

- intent และ route
- tool router proposal
- selected/rejected candidates
- policy และ margin
- execution plan
- capability ที่ execute จริง
- selected capability ตรงกับ execution หรือไม่
- validation/evidence/source IDs
- LLM call count
- repair attempted/recovered
- outcome และ quality gate status

มีประโยชน์ต่อ eval และ failure taxonomy มากกว่าอ่านข้อความ trace ทุกบรรทัดด้วยมือ

### 27.4 API response

`app/web_api/server.py` แปลง PipelineAnswer เป็น JSON ที่ browser ใช้ เช่น answer, mode, route, confidence, latency, sources และ deadline metadata ส่วน trace/decision artifact เปิดเมื่อ debug policy อนุญาต

### 27.5 Web output

browser รับ JSON แล้ว:

1. ปิด loading state
2. แสดง `answer`
3. แสดง source links/metadata ตาม UI
4. เก็บ recent history/session ID สำหรับข้อความถัดไป
5. แสดง error ที่เหมาะกับ 409/503/timeout โดยไม่เปิดเผย internal stack trace

### 27.6 Async logging

หลังเตรียม response แล้ว server เขียน chat log ผ่าน background thread เพื่อไม่ให้ disk logging เพิ่ม user-visible latency โดยตรง

ข้อมูล log อาจรวม:

- request/session ID
- question/answer
- mode/route/intent
- source IDs
- elapsed/wall time
- validation
- decision artifact
- trace/LLM metadataตาม config

Asynchronous ไม่ได้แปลว่า log รับประกันเขียนสำเร็จก่อน process ถูกปิดทันที จึงต้องออกแบบ shutdown/flush เพิ่มหากต้องการ durability ระดับ production

### 27.7 Timing trace

stage ที่บันทึกเวลาได้ช่วยแยกว่าช้าตรงไหน เช่น:

- warmup/cold load
- session resolver
- preprocess/router/intent
- curated/vector retrieval
- merge/reranker/evidence packer
- LLM queue และ generation
- validation/build result

ควรดู `average`, `P50`, `P95`, `P99`, `max` และ timeout rate ไม่ใช่ดู run เดียว

---

## 28. End-to-end Examples

ตัวอย่างทั้งหมดแสดงเส้นทาง ไม่ยืนยันเนื้อหาคำตอบจริง

### 28.1 คำถาม Structured ชัดเจน

```text
User: PS5 มีเกมอะไรบ้าง
```

```text
API validation
-> session unchanged
-> single question
-> preprocess: service/zone signal = PS5
-> route = games catalog
-> intent = games/game_catalog
-> target resolver = PS5 zone/platform
-> ambiguity allow
-> frame expects game_catalog/list
-> candidate structured.games ชนะ
-> precondition ผ่าน
-> filter structured game rows
-> deterministic draft
-> optional composer เฉพาะเมื่อเปิดและเวลาเหลือ
-> answer contract: list + games source
-> output
```

RAG ไม่จำเป็น เพราะ list จาก field ให้ผล exact กว่า

### 28.2 Follow-up ที่ resolve ได้

```text
History: ผู้ใช้ระบุเกมหนึ่งอย่างชัดและระบบตอบจาก source แล้ว
User: แล้วปุ่มอะไร
```

```text
session resolver หา latest unique game target
-> เติม target ให้ active query
-> intent = control_lookup
-> ambiguity allow
-> frame requires game target + controls
-> structured controls หรือ guarded vector-control path
-> ถ้ามี verified controls: ตอบและ validate target
-> ถ้าไม่มี: no verified control data
```

### 28.3 Follow-up ที่กำกวม

```text
History: มีเกม A และเกม B
User: เกมนั้นปุ่มอะไร
```

```text
session resolver ไม่พบ unique referent
-> ไม่เดา
-> ambiguity gate ตรวจ missing/ambiguous target
-> ถามกลับให้ระบุชื่อเกม
```

### 28.4 Simple independent compound

```text
User: PS5 มีเกมอะไรบ้าง และวันจันทร์เปิดกี่โมง
```

```text
split -> 2 parts
complexity: ไม่มี dependency -> simple independent
bounded parallel max 2
  child 1 -> structured games
  child 2 -> structured/fast schedule
validate children
merge grounded subanswers
final validation/output
```

### 28.5 Dependent compound

```text
User: โซนไหนมีเกมมากที่สุด แล้วเครื่องนั้นราคาเท่าไหร่
```

```text
split -> 2 parts
complexity detects ranking + reference
-> complex/ordered
-> optional planner
-> child 1 counts/ranks structured rows
-> capture supported target
-> child 2 resolves "เครื่องนั้น"
-> ถ้า mapping ไป service ยังไม่ชัด: clarification
-> ถ้าชัดและ price entities ครบ: calculator/structured fee
-> merge only supported parts
```

### 28.6 RAG + optional rerank/composer

```text
User: ถามรายละเอียดจากข่าวหรือเอกสารความรู้ที่มีในคลัง
```

```text
route/intent = events_news หรือ knowledge
-> retrieval budget
-> curated + local vector
-> category/entity guard
-> merge/deduplicate/hybrid score
-> optional BGE ถ้า warm + time พอ
-> source guard
-> pack top evidence
-> deterministic answer หรือ Typhoon composer
-> claim/source/contract validation
-> output พร้อม source
```

หากคลังไม่มีข่าวนั้น ระบบต้อง no-answer ไม่ใช้ LLM สร้างข่าว

### 28.7 ราคาไม่ครบเงื่อนไข

```text
User: ราคาเท่าไหร่
```

```text
intent price ชัด
target/service ขาด
-> ambiguity/precondition fail
-> clarification ระบุ field ที่ต้องการ
```

### 28.8 LLM ช้า/ล้มเหลว

```text
structured/RAG draft มีอยู่แล้ว
-> composer call timeout หรือ circuit cooldown
-> composer used_llm=false
-> ใช้ draft ที่ผ่าน contract
-> ผู้ใช้ยังได้คำตอบ evidence-first
```

หากไม่มี draft/evidence จึง no-answer ไม่ส่ง partial token ของ model

---

## 29. Time และทรัพยากรของแต่ละกลุ่ม

| กลุ่ม | เวลาโดยทั่วไปหลัง warm | ทรัพยากรหลัก | จุดเสี่ยง |
|---|---|---|---|
| Normalize/Rules | ต่ำมาก | CPU | rule coverage |
| Structured | ต่ำ | CPU + RAM data cache | schema/data quality |
| Curated/Hash Vector | ต่ำถึงปานกลาง | CPU + RAM index | retrieval recall/precision |
| BGE warm rerank | ปานกลาง | CPU/GPU + RAM/VRAM | queue/model residency |
| BGE cold load | สูงมาก | disk + RAM/VRAM + runtime init | เกิน product deadline |
| Typhoon generation | หลายวินาทีได้ | CPU/GPU + RAM/VRAM | concurrency/timeout |
| Validation | ต่ำ | CPU | heuristic blind spots |

ค่าที่เคยวัดใน environment ล่าสุดจาก Flow หลัก:

- Fast price warm ราว `0.16-0.18s`
- Structured probes ราว `0.3-0.7s`
- Hybrid/vector retrieval หลัง warm ราว `0.14s` เฉพาะ retrieval
- Product-like warm RAG + LLM ราว `7.75s`; composer ราว `7.27s`
- BGE cold load เคยราว `93.46s`

ตัวเลขเหล่านี้เป็น measurements ของเครื่อง/config ช่วงหนึ่ง ไม่ใช่ SLA จนกว่าจะทดสอบหลายรอบและหลายผู้ใช้

---

## 30. สิ่งที่ชื่ออาจทำให้เข้าใจผิด

| ชื่อ | สิ่งที่ทำจริงปัจจุบัน | สิ่งที่ยังไม่ใช่ |
|---|---|---|
| Semantic Intent | char n-gram cosine กับ catalog examples | neural semantic understanding เต็มรูปแบบ |
| Local Vector | hashed char/word sparse features | sentence embedding model |
| Confidence | heuristic/policy scoreในหลาย stage | calibrated probability เสมอ |
| Source Conflict | นับ distinct numeric values ต่อ claim key | logical contradiction detector |
| Staleness Guard | field มีใน result แต่คืน false | freshness enforcement ตามวันหมดอายุ |
| RAG | retrieval + deterministicหรือ LLM composition | จำเป็นต้องเรียก LLMทุกครั้ง |
| Query Planner | constrained JSON task planner | answer generator |
| Warmup | preload/cache/probe | รับประกันทุก model พร้อมทุก process ตลอดเวลา |
| Timeout | deadline + socket close/fallback | hard kill inference ทุกกรณี |
| Booking | ให้ข้อมูลวิธีจอง | transaction/slot reservation จริง |

---

## 31. Safety Invariants ที่ทุกเส้นต้องรักษา

1. ไม่มีข้อมูลจริงของ PSU Esports Studio - Phuket ห้ามเดา
2. Reference ต้องมี evidence จาก input/history/result ก่อนหน้า ไม่เช่นนั้นถามกลับ
3. Exact structured fact ต้องไม่ถูก model เปลี่ยนตัวเลข ชื่อ เวลา หรือ source
4. RAG hit ต้องผ่าน category/entity/source policy ไม่ใช่เลือกเพราะ similarity อย่างเดียว
5. General LLM ห้ามตอบ PSU-specific fact ที่ไม่มี evidence
6. Source conflict ห้ามถูกซ่อนด้วยภาษาที่ฟังมั่นใจ
7. Partial/timeout model output ห้ามส่งก่อน validation
8. Candidate ที่ precondition ไม่ผ่านห้าม execute
9. Final contract fail ต้อง hard veto
10. คำตอบ Fast/Rule/Structured/RAG ต้องรายงานที่มาตรง path ไม่อ้างว่าเป็น LLM

---

## 32. ข้อจำกัดและงานที่ควรทำต่อ

### 32.1 Correctness evaluation

ยังต้องรัน full 1,500+/1,600 cases หลัง changes ล่าสุด แยก No-LLM และ Typhoon แล้วจำแนก:

- wrong route
- wrong intent
- wrong target
- missing subanswer
- unsupported claim
- source mismatch
- timeout
- unnecessary LLM call

### 32.2 Multi-user load

ต้องทดสอบอย่างน้อย 5 sessions พร้อมกัน วัด:

- admission rejection
- session isolation
- LLM slot wait
- average/P50/P95/P99/max
- timeout rate
- CPU/GPU/RAM/VRAM
- model ยังทำงานต่อหลัง client timeoutหรือไม่

### 32.3 Distributed control

ถ้ามีหลาย processes ควรมี shared queue/worker หรือ global inference service เพราะ in-process semaphore ไม่ควบคุม GPU รวม

### 32.4 Retrieval backend

หลัง structured correctness นิ่ง จึงเปรียบเทียบ semantic embedding กับ hash char n-gram โดยใช้ retrieval benchmark เดียวกัน อย่าเปลี่ยนเพียงเพราะชื่อเทคนิคดูใหม่กว่า

### 32.5 Freshness

ควรเพิ่ม:

- `published_at`, `updated_at`, `effective_from`, `expires_at`
- policy ต่อ category
- stale rejection/penalty
- source precedence เมื่อกฎหลาย version

### 32.6 Control sources

ต้อง manual verify source ที่ยังเป็น secondary และบันทึก canonical game/control IDs ก่อนเพิ่ม coverage

### 32.7 Booking

หากจะทำ transaction จริง ต้องเพิ่ม authentication, availability check, idempotency, lock, payment state, confirmation และ audit log แยกจาก chatbot answer flow

---

## 33. File-to-Process Map ที่ตรงกับ implementation ปัจจุบัน

| Process | Source หลัก |
|---|---|
| Web/API, active semaphore, session lock | `app/web_api/server.py` |
| Session context | `app/session/context_resolver.py` |
| Global deadline/LLM call budget | `app/pipeline/request_deadline.py` |
| Startup warmup | `app/pipeline/warmup.py` |
| Main orchestration/split/compound execution | `app/pipeline/engine.py` |
| Compound complexity/profile | `app/pipeline/compound_execution.py` |
| Query Planner | `app/pipeline/query_planner.py` |
| Preprocess/entities | `app/pipeline/preprocess.py` |
| Boundary Guard | `app/pipeline/boundary_guard.py` |
| Scope Guard | `app/pipeline/guard.py` |
| Heuristic route | `app/pipeline/router.py` |
| Char n-gram intent fallback | `app/pipeline/semantic_intent.py` |
| Universal Intent | `app/pipeline/universal_intent.py` |
| Model allocation policy | `app/pipeline/model_gateway.py` |
| Optional Tool Router | `app/pipeline/llm_tool_router.py` |
| Ambiguity Gate | `app/pipeline/ambiguity_gate.py` |
| Question Frame | `app/pipeline/question_frame.py` |
| Target/entity resolution | `app/pipeline/target_resolver.py`, `entity_resolver.py`, `game_title_correction.py` |
| Capability candidates/margin | `app/pipeline/capability_registry.py` |
| Tool Preconditions | `app/pipeline/tool_preconditions.py` |
| Structured execution | `app/pipeline/structured_tools.py` |
| Fast/rule handlers | `app/runtime/fast_answer.py` และ handler ที่ `engine.py` เรียก |
| Curated retrieval | `app/pipeline/retrieval.py` |
| Local hash vector | `app/pipeline/vector_retrieval.py` |
| Hybrid merge/guards | `app/pipeline/hybrid_retrieval.py` |
| BGE reranker | `app/pipeline/document_reranker.py` |
| Evidence Packer | `app/pipeline/evidence_packer.py` |
| Source Guard | `app/pipeline/source_guard.py` |
| Facts Composer | `app/pipeline/facts_composer.py` |
| Grounding claims | `app/pipeline/claim_validator.py` |
| General/experimental fallback | `app/pipeline/experimental_fallback.py` |
| LLM health/concurrency/preflight | `app/pipeline/llm_health.py` |
| Formatter | `app/pipeline/formatter.py` |
| Base Validator | `app/pipeline/validator.py` |
| Answer Contract | `app/pipeline/answer_contracts.py` |
| Decision Artifact | `app/pipeline/decision_artifact.py` |
| Shadow Critic/eval support | `app/pipeline/shadow_critic.py` |
| Chat logging | `app/session/chat_logger.py` |

หมายเหตุ: เอกสาร Flow หลักใช้ชื่อเชิงแนวคิดบางรายการ เช่น `complexity_gate.py`, `routing.py`, `fast_paths.py` แต่ไฟล์จริงปัจจุบันอยู่ใน `compound_execution.py`, `router.py`, `engine.py` และ `app/runtime/fast_answer.py` ตามตารางนี้

---

## 34. Glossary ภาษาไทย

| ศัพท์ | ความหมายแบบสั้น |
|---|---|
| Alias | ชื่ออื่นที่ชี้ไป canonical item เดียวกัน |
| API | ช่องทาง/สัญญาการสื่อสารระหว่าง client กับ server |
| Answer Contract | ข้อกำหนดว่าคำตอบต้องมีชนิด target และ source แบบใด |
| Cache | เก็บข้อมูล/ผลที่ใช้แล้วใน memory เพื่อลดงานซ้ำ |
| Candidate | ตัวเลือก route/target/tool/document ก่อนเลือกผู้ชนะ |
| Canonical | ชื่อหรือ ID มาตรฐานเพียงหนึ่งเดียว |
| Circuit Breaker | หยุดเรียก service ชั่วคราวหลังล้มเหลวซ้ำ |
| Cold Start | ต้นทุนครั้งแรกก่อน resource อยู่ใน memory |
| Compound Query | ข้อความเดียวที่มีหลายคำถาม/operation |
| Concurrency | จำนวนงานที่ทำพร้อมกัน |
| Context | ข้อมูลรอบคำถาม เช่นประวัติ session |
| Cosine Similarity | การวัดทิศทางความคล้ายของ feature vectors |
| CrossEncoder | model ที่อ่าน query กับ document เป็นคู่เพื่อให้คะแนน |
| Deadline | เวลาสิ้นสุดรวมของ request |
| Deduplicate | รวม/ตัดข้อมูลซ้ำ |
| Deterministic | input/data เดิมให้ผลตามกฎเดิม |
| Embedding | vector ที่ model เรียนรู้เพื่อแทนความหมายของข้อมูล |
| Entity | สิ่งเฉพาะ เช่นเกม โซน วัน หรือกลุ่มผู้ใช้ |
| Evidence | ข้อมูลรองรับคำตอบ |
| Fallback | ทางสำรองเมื่อทางหลักใช้ไม่ได้ |
| Fact Card | record ข้อเท็จจริงย่อยจากเอกสาร |
| Feature Flag | ตัวเปิด/ปิดความสามารถโดยไม่แก้ flow หลัก |
| Fuzzy Match | จับข้อความที่คล้ายแต่ไม่ตรงทุกตัวอักษร |
| Gate | ขั้นตัดสินว่าจะให้ไปต่อทางใด |
| Grounding | ผูกคำตอบกับ evidence ที่ให้ไว้ |
| Guard | ขั้นป้องกันความเสี่ยงหรือข้อมูลผิด |
| Hallucination | model สร้างข้อมูลที่ไม่มีหลักฐาน |
| Heuristic | กฎประมาณการจากสัญญาณที่ออกแบบไว้ |
| Hit | เอกสาร/record ที่ retrieval คืนมา |
| Intent | สิ่งที่ผู้ใช้ต้องการทำ |
| JSON | รูปแบบข้อมูลมี key/value สำหรับส่งระหว่างระบบ |
| Latency | เวลาตั้งแต่เริ่มจนได้ผล |
| LLM | โมเดลภาษาขนาดใหญ่ที่สร้างหรือวิเคราะห์ข้อความ |
| Margin | คะแนนอันดับหนึ่งลบอันดับสอง |
| Metadata | ข้อมูลอธิบายข้อมูล เช่น source/category/date |
| Mode | path ที่ระบบ execute จริง |
| n-gram | ชิ้นข้อความต่อเนื่องยาว n ตัวอักษร/คำ |
| No-answer | แจ้งว่าไม่มีข้อมูลที่ยืนยันได้ |
| Normalize | ทำข้อความต่างรูปให้อยู่รูปเทียบกันได้ |
| Ollama | runtime/API สำหรับรัน Local LLM |
| Operation | การกระทำ เช่น list, count, price, control lookup |
| P95 | 95% ของ request เร็วกว่าหรือเท่าค่านี้ อีก 5% ช้ากว่า |
| Planner | ตัวแปลง query เป็นแผนงาน |
| Precondition | เงื่อนไขขั้นต่ำก่อน execute tool |
| Prompt | ข้อความคำสั่งและ context ที่ส่งให้ LLM |
| Provenance | เส้นทางว่าข้อมูลมาจาก source ใด |
| RAG | ค้น evidence ก่อนนำมาสร้างคำตอบ |
| Rerank | จัดลำดับ candidates ใหม่ด้วยวิธีละเอียดกว่า |
| Resolver | ตัวเปลี่ยนชื่อ/คำอ้างอิงเป็น target ที่ยืนยันได้ |
| Route | หมวดและเส้นทางระดับระบบ |
| Schema | โครง field และชนิดข้อมูลที่กำหนดไว้ |
| Semaphore | ตัวจำกัดจำนวนงานพร้อมกัน |
| Session | บริบทการสนทนาของผู้ใช้หนึ่งชุด |
| Source Guard | ตรวจ source IDs, trust และ conflict heuristic |
| Sparse Vector | vector ที่ตำแหน่งส่วนใหญ่เป็นศูนย์ |
| Structured Tool | เครื่องมือที่ query ข้อมูลตาม field/schema |
| Target | สิ่งที่ operation กระทำกับมัน |
| Threshold | ค่าตัดสินผ่าน/ไม่ผ่าน |
| Timeout | เวลาสูงสุดของงานหรือขั้นหนึ่ง |
| Token | หน่วยข้อความที่ model ประมวลผล/สร้าง |
| Trace | บันทึกลำดับการตัดสินใจและเวลา |
| Validator | ตัวตรวจว่าคำตอบผ่านเงื่อนไขหรือไม่ |
| Vector Retrieval | ค้น candidate จากความคล้ายของ feature vectors |
| Warmup | โหลด/เรียก resource ล่วงหน้าให้พร้อม |

---

## 35. วิธีอ่านปัญหาจาก Flow เมื่อคำตอบผิดหรือช้า

### คำตอบผิด

ตรวจตามลำดับนี้:

```text
mode
-> route
-> universal intent/operation
-> target และ reference source
-> selected candidate + margin
-> tool precondition
-> evidence/source IDs
-> validator/contract
-> trace ของการ repair/fallback
```

### คำตอบช้า

ตรวจ:

```text
cold หรือ warm?
-> admission/session/LLM queue wait
-> planner call?
-> retrieval timing แยก curated/vector
-> BGE load/rerank
-> composer generation
-> deadline remaining ก่อนแต่ละ call
-> cancellation หลัง timeout
-> validation/finalizer
```

### คำตอบขาดบางส่วน

ตรวจ:

- splitter สร้าง child ครบหรือไม่
- complexity/dependency ถูกหรือไม่
- child ใด no-answer หรือถูก veto
- evidence pack ตัด passage ที่จำเป็นหรือไม่
- composer `num_predict=64` ตัด output หรือไม่
- merge compound รักษาทุก grounded subanswer หรือไม่

---

## 36. บทสรุป

Flow นี้แบ่งงานเป็นสามชั้นใหญ่:

1. **ควบคุม request และเวลา**: Web/API, admission, session lock, deadline, call/concurrency budget
2. **ทำความเข้าใจและตัดสินใจ**: context, split, complexity, planner, route, intent, target, ambiguity, frame, candidates, preconditions
3. **หาคำตอบและพิสูจน์ก่อนส่ง**: Fast/Rule/Structured/RAG/BGE/LLM, source/grounding, validation, repair, hard veto, output/logging

Structured และ Fast เป็นแกนหลักเพราะข้อมูล PSU จำนวนมากเป็น fact ที่มี schema และต้องแม่น RAG เพิ่ม coverage ให้เอกสาร ข่าว กฎ และข้อความอธิบาย ส่วน Local LLM ช่วยวางแผน ตีความ และเรียบเรียงเฉพาะเมื่อมีเวลา สิทธิ์ และหลักฐานเพียงพอ

เป้าหมายที่ถูกต้องจึงไม่ใช่ “ทำให้ทุกคำถามใช้ LLM/RAG” แต่คือ “ให้ทุกคำถามใช้ path ที่แม่นและเร็วที่สุดสำหรับชนิดข้อมูลนั้น พร้อมถามกลับหรือหยุดเมื่อหลักฐานไม่พอ”
