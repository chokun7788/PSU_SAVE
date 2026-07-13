# Experiment Timeline

บันทึก timeline การทดลองทำ Local RAG Chatbot สำหรับ PSU Esports Studio - Phuket

วันที่หลักของรอบนี้: 2026-06-29

---

## รอบที่ 1: วางเป้าหมายระบบ

สิ่งที่ต้องการ:

- ทำ Chatbot สำหรับตอบ FAQ ของ PSU Esports Studio - Phuket
- เน้นข้อมูลกฎ, การจอง, กฎการจอง, เกม, การแข่งขัน, contact
- ใช้งาน local เป็นหลัก
- ไม่ใช้ API เสียเงิน
- รองรับภาษาไทยและอังกฤษ
- MVP ต้องทำให้เห็นผลเร็ว
- ใช้ Docker ได้ในอนาคต
- ต่อ Facebook chatbot เป็นเป้าหมายถัดไป

ข้อจำกัดที่รู้:

- เครื่องเป้าหมายใช้ CPU Intel Core i5-14400
- RAM 32GB
- GPU NVIDIA GeForce RTX 5060 8GB VRAM
- ต้องพยายามให้ตอบเร็วและไม่ใช้ resource หนักเกินไป

ผลลัพธ์:

- ตัดสินใจใช้แนวทาง Local RAG แทน fine-tune เต็ม
- เลือกใช้ Ollama เป็นตัวรัน LLM local
- เลือกใช้ Chroma เป็น vector database
- เลือกใช้ multilingual embedding เพื่อรองรับไทย/อังกฤษ

---

## รอบที่ 2: เลือกและโหลดโมเดลแรก

สิ่งที่ทดลอง:

- เลือก `qwen3:4b` เป็นโมเดลหลักรอบแรก
- โหลดผ่าน Ollama
- ตรวจว่าโมเดลรันบน GPU ได้

เหตุผลที่เลือก:

- ขนาดไม่ใหญ่มาก
- รองรับภาษาไทยพอใช้
- เหมาะกับเครื่อง local ที่มี VRAM 8GB

ผลลัพธ์:

- โหลด `qwen3:4b` สำเร็จ
- โมเดลรันบน GPU ได้
- ใช้ VRAM ประมาณ 3-4GB ตอนโหลดโมเดล

ปัญหาที่เจอ:

- Qwen3 มี thinking behavior
- แม้สั่งไม่ให้คิด บางครั้งยังพิมพ์ reasoning เช่น `Okay, let's see...`
- เวลาตอบช้ามากในหลายคำถาม

---

## รอบที่ 3: สร้าง Local RAG Notebook

สิ่งที่ทดลอง:

- สร้างโฟลเดอร์ระบบ RAG หลัก
- สร้าง notebook `01_local_rag_qwen3_4b.ipynb`
- โหลดข้อมูลจาก webscraping
- ทำ embeddings ด้วย `intfloat/multilingual-e5-small`
- เก็บลง Chroma vector database
- ทำ retrieval + prompt + call Ollama

ผลลัพธ์:

- Notebook รัน pipeline ได้
- ดึง context จาก Chroma ได้
- เรียกโมเดล local ผ่าน Ollama ได้
- มี `logs/chat_log.jsonl` สำหรับเก็บคำถาม/คำตอบ

ปัญหาที่เจอ:

- ข้อมูลไทยบางส่วนอาจมี encoding เพี้ยนจาก webscraping
- retrieval บางคำถามยังดึง source ไม่ตรง
- LLM บางครั้งตอบว่าไม่พบข้อมูลแม้ข้อมูลมีอยู่

วิธีแก้รอบแรก:

- เพิ่ม logic ซ่อม mojibake
- เพิ่ม category routing
- เพิ่ม lexical rerank
- เพิ่ม curated facts สำหรับข้อมูลสำคัญ

---

## รอบที่ 4: Optimize Content และ Chunking

สิ่งที่ทดลอง:

- สร้าง `scripts/optimize_content.py`
- ใช้ structure-aware chunking แทนการตัดตามจำนวนคำอย่างเดียว
- รวมข้อมูลจาก webscraping และ curated facts
- เพิ่ม category, priority, tags

ผลลัพธ์:

- ได้ `data/processed/optimized_chunks.jsonl`
- จำนวน chunks ล่าสุดประมาณ 69 chunks
- มี curated facts ประมาณ 42 รายการ
- หมวดหลัก ได้แก่ overview, reservation, rules, penalty, games, contact, knowledge

ปัญหาที่แก้:

- chunk เดิมบางส่วนยาว/กระจัดกระจาย
- คำถาม FAQ ควรมี fact ที่ชัดเจน ไม่ควรหวังให้ LLM สรุปจากเว็บอย่างเดียว

ผลที่ดีขึ้น:

- Retrieval ดึง curated facts ได้ง่ายขึ้น
- ข้อมูลสำคัญ เช่น check-in, refund, penalty, games, contact ถูกจัดหมวดชัดเจนขึ้น

---

## รอบที่ 5: เพิ่ม Ground Truth

สิ่งที่ทดลอง:

- สร้าง ground truth สำหรับคำถามทดสอบ
- ครอบคลุมหลายหมวด เช่น reservation, rules, games, contact, overview, no_answer

ผลลัพธ์:

- มี `ground_truth/ground_truth_full.jsonl`
- มีคำถามประมาณ 105 ข้อ

ประโยชน์:

- ใช้วัดว่า retrieval ดึง source ถูกไหม
- ใช้วัดว่าคำตอบมี keyword สำคัญไหม
- ใช้กัน regression เวลาเปลี่ยน prompt/model/chunking

ข้อจำกัด:

- Evaluation ตอนนี้ยังเป็น keyword/source check แบบง่าย
- ยังไม่ได้ใช้ LLM-as-judge
- ยังไม่ได้วัด hallucination แบบละเอียด

---

## รอบที่ 6: พบปัญหา Latency สูง

สิ่งที่ทดลอง:

- รันคำถามจริงใน notebook
- ดู latency จาก `logs/chat_log.jsonl`

ค่าที่พบ:

```text
qwen3:4b เดิม: ประมาณ 20-40 วินาทีต่อคำถาม
บางคำถามเฉลี่ยประมาณ 33 วินาที
```

สาเหตุหลัก:

- `num_predict=1600` สูงเกินไป
- `num_ctx=8192` สูงเกินไปสำหรับ MVP
- context ยาวเกินจำเป็น
- Qwen3 ชอบ generate reasoning ก่อนคำตอบ

วิธีแก้:

- ลด `TOP_K`
- ลด `MAX_CONTEXT_CHARS`
- ลด `num_ctx`
- ลด `num_predict`
- เพิ่ม `keep_alive`
- ทดลองโมเดลที่ไม่ใช่ thinking model

---

## รอบที่ 7: โหลดและทดสอบ Fast Model

สิ่งที่ทดลอง:

- โหลด `qwen2.5:3b`
- ทดสอบกับ prompt สั้น
- เทียบกับ `qwen3:4b`

ผลลัพธ์:

```text
qwen2.5:3b รอบแรกหลังโหลด/สลับโมเดล: ช้าได้ถึง 40 วินาที
หลัง warm แล้ว: ประมาณ 3-9 วินาที
```

ข้อดี:

- ตอบตรงกว่า Qwen3
- ไม่ค่อยพิมพ์ reasoning ออกมา
- เหมาะกับ MVP ที่ต้องการตอบเร็ว

ข้อเสีย:

- อาจฉลาดน้อยกว่า Qwen3 ในคำถาม reasoning ซับซ้อน
- ควรใช้กับคำถาม FAQ/RAG ที่ context ชัดเจน

Decision:

- ตั้ง `qwen2.5:3b` เป็น fast default
- เก็บ `qwen3:4b` เป็น quality option

---

## รอบที่ 8: เพิ่ม Rule-based Fast Path

สิ่งที่ทดลอง:

- สร้าง `data/curated/rule_patterns.jsonl`
- สร้าง `scripts/rule_matcher.py`
- ให้ `answer_question()` เช็ก rule ก่อน RAG/LLM

ตัวอย่างคำถามที่เข้า rule:

```text
เช็คอินล่วงหน้าได้กี่นาที
PS5 มีเกมอะไรบ้าง
ศูนย์อยู่ที่ไหน
ยกเลิกจองได้เงินคืนไหม
```

ผลลัพธ์:

```text
rule_fast_path: ประมาณ 0.000-0.006 วินาที
```

ข้อดี:

- เร็วมาก
- ลด hallucination สำหรับกฎสำคัญ
- เหมาะกับ Facebook chatbot
- ลด load ของ LLM

ปัญหาที่เจอ:

- Rule แรก ๆ แข็งเกินไป
- ถามว่า "กี่วินาที" ยังตอบว่า "30 นาที" อย่างเดียว

วิธีแก้:

- เพิ่ม `adapt_answer_to_query()` ใน `rule_matcher.py`
- ถามวินาทีให้ตอบ 1,800 วินาที
- ถามชั่วโมงให้ตอบ 0.5 ชั่วโมง

ผลลัพธ์หลังแก้:

```text
ถาม: เช็คอินล่วงหน้าได้กี่วินาที
ตอบ: 30 นาที หรือ 1,800 วินาที

ถาม: เช็คอินล่วงหน้าได้กี่ชั่วโมง
ตอบ: 0.5 ชั่วโมง หรือ 30 นาที
```

---

## รอบที่ 9: เจอปัญหา RAG ดึงถูก แต่ LLM ตอบว่าไม่พบข้อมูล

สิ่งที่ทดลอง:

```python
answer, hits, elapsed = answer_question("ศูนย์นี้เกี่ยวกับอะไร", use_rules=False)
```

ผลที่พบ:

```text
retrieved_ids:
- curated_overview_identity
- curated_overview_mission

answer:
ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี
```

วิเคราะห์:

- Retrieval ไม่ได้ผิด เพราะดึง source ถูก
- ปัญหาอยู่ที่ LLM generation/prompt
- โมเดลตัดสินใจผิดว่า context ไม่มีคำตอบ

วิธีแก้:

- เพิ่ม `rag_direct_curated`
- ถ้า retrieval ดึง `curated_fact` ที่ชัดเจนได้ ให้ตอบจาก retrieved text โดยตรง
- ไม่ต้องเรียก LLM ในเคสที่ข้อมูลเป็น fact สั้นและชัดเจน

ผลลัพธ์หลังแก้:

```text
mode = rag_direct_curated
ตอบจาก curated_overview_identity และ curated_overview_mission ได้ทันที
ไม่ตอบว่าไม่พบข้อมูลแล้ว
```

---

## รอบที่ 10: เพิ่ม Debug Flags

สิ่งที่ทดลอง:

เพิ่ม parameter:

```python
answer_question(question, use_rules=True, use_direct=True)
```

ใช้ debug ได้ 3 แบบ:

```python
# ใช้ pipeline เต็มแบบเร็วสุด
answer_question("ศูนย์นี้เกี่ยวกับอะไร")

# ปิด rule แต่ยังให้ตอบตรงจาก curated fact ได้
answer_question("ศูนย์นี้เกี่ยวกับอะไร", use_rules=False)

# ทดสอบ RAG + LLM ล้วน
answer_question("ศูนย์นี้เกี่ยวกับอะไร", use_rules=False, use_direct=False)
```

ผลลัพธ์:

- แยกปัญหาได้ง่ายขึ้น
- ถ้า retrieved ถูกแต่ LLM ตอบผิด ให้ดู `rag_direct_curated`
- ถ้า retrieved ผิด ต้องแก้ retrieval/chunking/category

---

## สรุปสถานะล่าสุด

Pipeline ล่าสุด:

```text
Rule-based FAQ
-> RAG Direct Curated
-> RAG + LLM
-> Log
```

ผลลัพธ์หลัก:

- FAQ ซ้ำ ๆ ตอบได้ระดับ milliseconds
- คำถาม RAG ที่เจอ curated fact ชัดเจนตอบได้เร็วและเสถียรกว่า
- LLM ใช้เฉพาะกรณีที่ต้องสรุปจาก context ที่ไม่ใช่ fact ตรง ๆ
- ลด latency จาก 20-40 วินาทีลงมาได้มากในหลายกรณี

