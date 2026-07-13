# Content Optimization Layer

โฟลเดอร์นี้อธิบายชั้น optimize เนื้อหาก่อนทำ embedding/RAG

เป้าหมาย:

- ซ่อมภาษาไทยที่เพี้ยนจาก encoding
- ลบ boilerplate ที่ไม่ช่วยตอบคำถาม
- แยกหมวด เช่น reservation, rules, games, contact
- แตก chunk ตามโครงสร้างเนื้อหา ไม่ใช่นับจำนวนคำอย่างเดียว
- เพิ่ม curated facts สำหรับข้อมูลสำคัญที่ห้ามตอบพลาด
- เพิ่ม priority ให้ข้อมูลกฎ/จองสำคัญขึ้น
- เตรียมข้อมูลให้เหมาะกับ local embedding และ Qwen3 4B

---

## ไฟล์หลัก

```text
scripts/optimize_content.py
```

อ่านข้อมูลจาก:

```text
data/raw_sections/*/section_text.txt
data/curated/curated_facts.jsonl
```

เขียนออก:

```text
data/processed/optimized_chunks.jsonl
data/processed/optimization_manifest.json
```

---

## เทคนิคที่ใช้

### 1. Encoding Repair

แก้ข้อความไทยที่กลายเป็น `à¸...` โดยพยายามแปลงกลับจาก latin1 -> utf-8

### 2. Structure-Aware Chunking

ใช้ตัวคั่นจาก scraper เช่น `|` และ `---` เพื่อแบ่งตามหัวข้อ/บรรทัดข้อมูล แทนการตัดตามจำนวนคำล้วน ๆ

### 3. Category Inference

แยกหมวดจากเนื้อหา เช่น:

- reservation
- rules
- penalty
- games
- services_games
- contact
- knowledge
- events_news

### 4. Curated Facts

ข้อมูลสำคัญ เช่น เช็คอิน 30 นาที, จองล่วงหน้า 1 ชั่วโมง, ค่าปรับ, เกม, contact จะถูกเก็บเป็น chunk สั้น ๆ priority สูง

### 5. Deduplication

ลบ chunk ที่ซ้ำกันแบบง่าย เพื่อไม่ให้ vector search เจอข้อความซ้ำเยอะเกิน

---

## วิธีรัน

```powershell
cd C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B
python scripts\optimize_content.py
```

ถ้า `python` ใช้ไม่ได้ ให้ใช้ Python ที่มากับ Codex runtime หรือ interpreter ที่ใช้เปิด notebook

---

## หลัง optimize

Notebook จะใช้ไฟล์นี้เป็นหลัก:

```text
data/processed/optimized_chunks.jsonl
```

ถ้าไฟล์นี้ยังไม่มี ให้รัน `scripts/optimize_content.py` ก่อน

