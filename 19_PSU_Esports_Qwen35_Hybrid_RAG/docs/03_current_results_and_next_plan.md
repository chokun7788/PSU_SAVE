# Current Results and Next Plan

วันที่: 2026-07-03

## ตอนนี้ทำอะไรไปแล้ว

สร้างโฟลเดอร์ใหม่:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\19_PSU_Esports_Qwen35_Hybrid_RAG
```

คัดลอก data จากโฟลเดอร์ 18 เข้ามาไว้ที่:

```text
data/source_18
```

สร้าง unified corpus:

```text
data/unified/unified_knowledge.jsonl
```

ผลลัพธ์:

- total rows: 398
- curated facts: 195
- rulebase: 77
- competition fact cards: 19
- competition chunks: 104
- calendar closures: 3

สร้าง lexical index:

```text
data/index/lexical_index.json
```

ผลลัพธ์:

- documents: 398
- vocabulary: 16,718

## ปัญหาที่เจอระหว่างทดลอง

### 1. ข้อมูลต่าง schema กัน

ข้อมูลเดิมมีหลายรูปแบบ:

- curated ใช้ `text`
- rulebase ใช้ `answer_th`, `patterns`
- competition fact card ใช้ `answer`, `evidence`, `intent`
- calendar ใช้ `date`, `status`, `note`

ถ้าเอาไปค้นรวมกันตรงๆ จะทำให้ RAG ปนหมวดง่าย จึงแก้ด้วย unified schema ที่มี:

- `source_kind`
- `category`
- `answer_type`
- `priority`
- `metadata`
- `search_text`

### 2. Competition fact card priority สูงเกินไป

ตอนแรกคำถามคนละหมวด เช่น:

```text
ต่างมหาลัยเล่น VR 30 นาทีเท่าไหร่
วันไหนหยุดบ้างในเดือนนี้
ทำเมาส์พังต้องเสียค่าปรับไหม
```

เคยดึง competition fact card ผิดขึ้นมาก่อน เพราะ fact card มี priority สูง

แก้โดยเพิ่ม:

- category-aware scoring
- service fee bonus
- deterministic service fee synthesis
- deterministic calendar synthesis
- penalty category boost

### 3. คำถาม RoV ดึงเกมถูกแต่พ่วง intent อื่น

ตัวอย่าง:

```text
สรุปกฎ RoV เรื่อง pause และมาสายให้หน่อย
```

ตอนแรกดึง RoV ถูก แต่ติดเรื่อง team size/equipment/skin มาด้วย

แก้โดยเพิ่ม intent-aware scoring:

- `pause`
- `late_start`
- `team_size`
- `map_pool`
- `format`
- `equipment`
- `skin`
- `character`

### 4. LLM บางครั้งตอบว่าไม่พบข้อมูล ทั้งที่ context มี

เจอในคำถาม RoV ตอนใช้ `qwen3:4b`

แก้โดยเพิ่ม `fact_card_synthesis` ก่อนเข้า LLM:

ถ้า context เป็น fact card ที่มีคำตอบชัด ให้ระบบสรุปเอง ไม่ต้องให้ LLM ตอบ

## ผลทดสอบล่าสุด

### RoV pause + มาสาย

คำถาม:

```text
สรุปกฎ RoV เรื่อง pause และมาสายให้หน่อย
```

ผล:

- mode: `fact_card_synthesis`
- elapsed: ประมาณ 0.06 sec
- คำตอบถูกประเด็น:
  - มาสาย/เริ่มแข่งล่าช้าเกิน 15 นาที ถูกปรับแพ้
  - pause ได้สูงสุด 5 ครั้ง ครั้งละไม่เกิน 1 นาที

### CS2 pause compare

คำถาม:

```text
CS2 technical pause กับ tactical timeout ต่างกันยังไง
```

ผล:

- mode: `fact_card_synthesis`
- elapsed: ประมาณ 0.07 sec
- ตอบเฉพาะ technical/tactical ไม่พ่วง team/format แล้ว

### Tekken 8 equipment

คำถาม:

```text
Tekken 8 ใช้เครื่องอะไรแข่ง
```

ผล:

- mode: `direct_fact`
- elapsed: ประมาณ 0.06 sec
- ตอบ PlayStation 5

### Service fee

คำถาม:

```text
ต่างมหาลัยเล่น VR 30 นาทีเท่าไหร่
```

ผล:

- mode: `service_fee_synthesis`
- elapsed: ประมาณ 0.09 sec
- ตอบ 190 บาท สำหรับกลุ่ม General Student/นักศึกษาต่างสถาบัน

### Calendar

คำถาม:

```text
วันไหนหยุดบ้างในเดือนนี้
```

ผล:

- mode: `calendar_synthesis`
- elapsed: ประมาณ 0.05 sec
- ตอบวันที่ 2026-07-28, 2026-07-29, 2026-07-30

### Penalty

คำถาม:

```text
ทำเมาส์พังต้องเสียค่าปรับไหม
```

ผล:

- mode: `direct_fact`
- elapsed: ประมาณ 0.05 sec
- ตอบค่าปรับ/ชดเชยตามระดับความเสียหาย:
  - เล็กน้อย 100-500 บาท
  - ปานกลาง 500-2,000 บาทหรือตามราคาซ่อมจริง
  - ร้ายแรงชดเชยเต็มจำนวน

## แผนถัดไป

### Phase A: ทำให้ retrieval แม่นขึ้นอีก

- เพิ่ม category/intent aliases ให้ครบขึ้น
- เพิ่ม service fee parser สำหรับ Nintendo/Switch/Cockpit/PlayStation
- เพิ่ม fallback กรณีถามราคาแต่ไม่ระบุกลุ่ม ให้แสดงราคาทุกกลุ่ม
- เพิ่ม fallback กรณีถามราคา PC ให้ตอบว่ายังไม่พบราคา PC ใน Service Fee 2026

### Phase B: Vector RAG

โหลด embedding model:

```powershell
ollama pull qwen3-embedding:0.6b
```

สร้าง vector index:

```powershell
py -3 tools\03_build_vector_index_ollama.py --model qwen3-embedding:0.6b
```

ทดสอบ:

```powershell
py -3 tools\04_ask_qwen35_hybrid.py "RoV ถ้ามาสายและหลุดเกมมีกฎยังไง" --model qwen3:4b --use-vector
```

### Phase C: Qwen3.5 Test

โหลด:

```powershell
ollama pull qwen3.5:4b
```

เทียบกับตัวเดิม:

```powershell
py -3 tools\05_compare_models.py --models qwen2.5:3b qwen3:4b qwen3.5:4b
```

### Phase D: เชื่อมกลับ Web/API

เมื่อ pipeline นี้นิ่งแล้ว ค่อยเอา logic กลับไปผูกกับ:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\app\web_api\server.py
```

แนวทางคือ:

```text
Rule/Calculator เดิม
-> Hybrid RAG ใหม่
-> Qwen3.5 เฉพาะเคสที่จำเป็น
```

## คำตอบเรื่องใช้กี่โมเดล

ใช้จริงไม่จำเป็นต้องใช้ LLM 2 ตัวพร้อมกัน

Production แนะนำ:

- LLM หลัก 1 ตัว: `qwen3.5:4b`
- Embedding model 1 ตัว: `qwen3-embedding:0.6b`

ส่วน `qwen2.5:3b`, `qwen3:4b`, `qwen3.5:4b` ตอนนี้เก็บไว้เพื่อเทียบคุณภาพ/ความเร็ว ยังไม่ต้องลบ

หลังเทียบแล้วค่อยเลือก:

- ถ้าเน้นเร็วสุด: `qwen2.5:3b`
- ถ้าเน้นสมดุลและมีอยู่แล้ว: `qwen3:4b`
- ถ้าเน้นคุณภาพ RAG+LLM: `qwen3.5:4b`
