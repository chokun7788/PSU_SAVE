# 11 — PSU Esports AI ChatBot

โฟลเดอร์นี้คือแนวทางและ starter kit สำหรับทำ AI Chatbot ของเว็บไซต์ PSU Esports Studio - Phuket โดยเฉพาะ

เป้าหมายของบอท:

- ตอบคำถามเกี่ยวกับระบบจอง
- ตอบกฎการจอง / กฎการเช็คอิน / การยกเลิก / ค่าปรับ
- ตอบว่าอุปกรณ์ของศูนย์มีอะไรบ้าง เช่น PC, PS5, Nintendo Switch, VR, Cockpit
- ตอบว่าแต่ละอุปกรณ์มีเกมอะไร
- ตอบข้อมูลการแข่งขันและกิจกรรมจากเว็บ
- ตอบความรู้เกี่ยวกับ Esports จากบทความในเว็บ
- อ้างอิงแหล่งที่มาจาก URL หรือหมวดข้อมูล
- ถ้าไม่มีข้อมูลในเว็บ ต้องตอบว่าไม่พบข้อมูล ไม่เดาเอง

---

## โครงสร้างโฟลเดอร์

```text
11_PSU_Esports_AI_ChatBot/
  README.md
  01_ภาพรวมโปรเจกต์และขอบเขตบอท.md
  02_ข้อมูลและหมวดหมู่ที่ใช้ทำบอท.md
  03_RAG_Architecture_สำหรับเว็บนี้.md
  04_ขั้นตอนทำจริงแบบ_MVP.md
  05_ออกแบบ Prompt และนโยบายคำตอบ.md
  06_Evaluation_ชุดคำถามทดสอบ.md
  07_Production_Deploy_Maintenance.md
  requirements.txt
  data/
    curated/
      faq_facts.jsonl
    raw/
      psu_esports_ai_extracted/
    processed/
      all_chunks.jsonl
      all_pages.jsonl
  prompts/
    system_prompt_th.md
    answer_format.md
  src/
    simple_retriever_demo.py
    rag_app_skeleton.py
  eval/
    testset.jsonl
  examples/
    example_questions.md
```

---

## อ่านไฟล์ไหนก่อน

1. `01_ภาพรวมโปรเจกต์และขอบเขตบอท.md`
2. `02_ข้อมูลและหมวดหมู่ที่ใช้ทำบอท.md`
3. `03_RAG_Architecture_สำหรับเว็บนี้.md`
4. `04_ขั้นตอนทำจริงแบบ_MVP.md`
5. `05_ออกแบบ Prompt และนโยบายคำตอบ.md`
6. `06_Evaluation_ชุดคำถามทดสอบ.md`
7. `07_Production_Deploy_Maintenance.md`

ถ้าจะทดลองค้นข้อมูลจากไฟล์ที่เตรียมไว้:

```bash
python src/simple_retriever_demo.py "จองได้สูงสุดกี่ session"
python src/simple_retriever_demo.py "PS5 มีเกมอะไรบ้าง"
python src/simple_retriever_demo.py "กฎการเช็คอินคืออะไร"
```

---

## แนวทางสั้นที่สุด

ระบบนี้ควรทำเป็น RAG ไม่ใช่ fine-tune ตั้งแต่แรก

เหตุผล:

- ข้อมูลอยู่ในเว็บไซต์และเปลี่ยนได้
- ต้องอ้างอิงกฎ/ข้อมูลล่าสุดจากเว็บ
- ถ้า fine-tune แล้วข้อมูลเปลี่ยน ต้องเทรนใหม่
- RAG แค่ scrape ใหม่ -> build index ใหม่ -> chatbot ใช้ข้อมูลใหม่ได้

Flow ที่แนะนำ:

```text
ข้อมูลจากเว็บ (.jsonl)
-> ทำ chunk และ metadata
-> embed
-> เก็บลง vector database
-> ผู้ใช้ถาม
-> retrieve ข้อมูลที่เกี่ยวข้อง
-> LLM ตอบจาก context พร้อม citation
```

---

## ข้อมูลที่เตรียมไว้แล้ว

ไฟล์ข้อมูลหลัก:

- `data/curated/faq_facts.jsonl` — ข้อมูล fact ที่จัดรูปแบบเอง เช่น กฎจอง รายชื่อเกม ช่องทางติดต่อ เหมาะใส่เข้า index เป็นอันดับแรก
- `data/processed/all_chunks.jsonl`
- `data/processed/all_pages.jsonl`

ข้อมูลแยกหมวด:

- `data/raw/psu_esports_ai_extracted/reservation`
- `data/raw/psu_esports_ai_extracted/services`
- `data/raw/psu_esports_ai_extracted/competition`
- `data/raw/psu_esports_ai_extracted/news`
- `data/raw/psu_esports_ai_extracted/knowledge`
- `data/raw/psu_esports_ai_extracted/contact`

สำหรับทำบอทจริง แนะนำเริ่มจาก:

0. `data/curated/faq_facts.jsonl`
1. `reservation/chunks.jsonl`
2. `services/chunks.jsonl`
3. `competition/chunks.jsonl`
4. `knowledge/chunks.jsonl`

แล้วค่อยเพิ่ม `news/chunks.jsonl` เพราะข่าวมีเยอะและอาจทำให้ retrieval มี noise
