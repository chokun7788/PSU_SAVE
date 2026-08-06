# Known Issues And Next Steps

ไฟล์นี้สรุปปัญหาที่รู้แล้วและสิ่งที่ควรทำต่อ

## ปัญหาหลักที่ยังต้องระวัง

### 1. Fast/rule path ยังอาจมั่นใจเกินไป

อาการ:

- คำถามกำกวมบางอย่างอาจถูก route เข้า fast path ผิด
- ถาม staff แล้วเคยตอบเกม
- ถามเกมทั้งหมดแล้วเคยตอบเฉพาะ PS5

แนวแก้:

- ใช้ adaptive Intent LLM review สำหรับ broad/ambiguous มากขึ้น
- เพิ่ม precondition ก่อน structured/fast path
- เพิ่ม eval cases จากคำถามจริงที่หลุด

### 2. จำนวนเกมมีหลายแหล่ง

อาการ:

- structured `_game_rows()` เห็นประมาณ 44 entries
- legacy fast path บางคำตอบยังเคยพูด 36 เกม
- บาง entry เป็นภาค/รีมาสเตอร์/กลุ่ม เช่น `The Last of Us Part I / Part II`

แนวแก้:

- ตัดสินใจ canonical catalog policy:
  - นับแบบ unique playable titles
  - หรือนับแบบ entries จาก source
- รวม logic count/list ให้ใช้ source เดียวกัน
- เพิ่ม eval สำหรับ `เกมทั้งหมดมีกี่เกม`, `เกมใน PS5`, `เกมใน Nintendo`, `เกมใน PC`, `เกมใน VR`

### 3. Facts-only composer ยังไม่ควรเปิดทุกเคส

อาการ:

- `ask_with_composer(...)` บางครั้งเรียบเรียงยาว หรือดึง draft เดิมที่ไม่เหมาะ
- structured answer ตรง ๆ บางเคสดีกว่า composer

แนวแก้:

- เปิด composer เฉพาะ answer ที่เป็นหลาย facts และ structured evidence แน่น
- reject composer ถ้าคำตอบยาวเกิน, มี `...`, source หาย, จำนวน/ชื่อไม่ครบ
- ทำ answer-quality eval แยก `composer on/off`

### 4. Local LLM latency

อาการ:

- คำถามง่ายอย่าง `สวัสดี` ถ้าเข้า LLM อาจใช้เวลานาน
- qwen3:4b เคย thinking ยาวจน final response ว่าง

แนวแก้:

- ใช้ `qwen2.5:3b` เป็น default
- greeting/identity/capability ควรตอบด้วย role/structured ไม่ต้องเข้า general LLM
- จำกัด Intent LLM ด้วย `num_predict` ต่ำ เช่น 50
- cache intent result
- exact/strong intent ข้าม LLM

### 5. Typo/ภาษาวิบัติไม่มีวันครบ 100%

อาการ:

- พิมพ์ผิดเล็กน้อยแก้ได้มากขึ้น
- แต่ถ้าผิดหนักหรือเป็นคำเรียกใหม่ที่ไม่มี alias อาจยังไม่เจอ

แนวแก้:

- เก็บ log ของ miss
- เพิ่ม alias เฉพาะคำที่เจอบ่อย
- ใช้ fuzzy eval ทุกเกมหลังแก้ title correction
- ในอนาคตพิจารณา semantic embedding หรือ phonetic matching สำหรับไทย

### 6. RAG/vector ยังไม่ใช่ semantic เต็ม

อาการ:

- local hash char n-gram ช่วย typo แต่ไม่เข้าใจความหมายลึกเท่า embedding model
- คำถามข้ามหมวด/ซับซ้อนยังต้องพึ่ง routing/structured tools

แนวแก้:

- ทำ hybrid retrieval ที่มี BM25/vector/rerank ชัดขึ้น
- เพิ่ม query decomposition สำหรับคำถามหลายส่วน
- เพิ่ม reranker แบบ local ถ้ามี model ที่เร็วพอ
- ทำ source-grounded answer composer

## สิ่งที่ควรทำต่อเป็นลำดับ

### Step 1: Align game catalog/count

เป้าหมาย:

- `เกมทั้งหมดมีกี่เกม`
- `เกมตอนนี้มีอะไรบ้าง`
- `PS5 มีเกมอะไรบ้าง`
- `Nintendo มีเกมอะไรบ้าง`
- `PC มีเกมอะไรบ้าง`
- `VR มีเกมอะไรบ้าง`

ต้องตอบจาก source เดียวกันและจำนวนไม่ขัดกัน

### Step 2: เพิ่ม eval จากคำถามจริงต่อเนื่อง

ควรเพิ่ม cases จากคำถามที่ผู้ใช้ลองจริง:

- staff/member
- game list/count
- typo game title
- price calculation
- follow-up
- off-domain general LLM

### Step 3: ปรับ LLM gate ให้สมดุล

เป้าหมาย:

- คำถามชัด -> deterministic/structured เร็ว
- คำถามกำกวม -> Intent LLM review
- คำถามนอกโดเมน -> general LLM
- คำถาม PSU facts -> ห้าม general LLM เดา

### Step 4: ปรับ answer formatting ให้สม่ำเสมอ

โดยเฉพาะ:

- service fee
- booking price calculation
- equipment list
- member list
- game controls

### Step 5: Composer safety

ทำให้ facts-only composer ใช้ได้จริงมากขึ้น:

- ต้องไม่ตัดข้อมูลเป็น `...`
- ต้องไม่เปลี่ยนจำนวน/ชื่อ/ราคา
- ต้องไม่ลบ source
- ต้องไม่ตอบผิดจาก draft

### Step 6: Better retrieval

เมื่อ structured/fast เริ่มนิ่งแล้ว ค่อยทำ:

- Query rewriting
- Hybrid Search
- Reranking
- Agentic/Graph RAG แบบคุม scope

## หลักคิดสำคัญ

อย่าแก้ด้วยการเพิ่ม rule เฉพาะเคสทุกครั้งถ้าปัญหาเป็น pattern กว้าง

ให้ถามตัวเองก่อน:

- คำถามนี้ผิดเพราะ normalization หรือไม่
- entity/title correction เจอไหม
- intent ผิดไหม
- structured tool ถูก reject ไหม
- fast path แย่งตอบไหม
- retrieval ดึงผิด source ไหม
- formatter/validator ตัดคำตอบไหม
- LLM ควรช่วยตรง intent, composer หรือ general fallback

