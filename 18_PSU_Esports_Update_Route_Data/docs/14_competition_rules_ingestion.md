# Competition Rules Ingestion

เอกสารนี้สรุปการนำไฟล์กติกาการแข่งขัน `.txt` มาแปลงเป็น JSONL เพื่อใช้กับ RAG/curated retrieval ของ chatbot

## Source Files

ไฟล์ต้นทางอยู่ใน `C:\Users\Chokhun\Downloads`

```text
กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2 รายการ PSU Phuket CS2 2026 Tournament.txt
กติกาการแข่งขัน Arena of Valor (RoV) รายการ Blueket Games 2025 ประเภททีมชาย.txt
กฎระเบียบและรูปแบบการแข่งขัน Tekken 8 รายการ PSU Esports ปะทะมันส์ สนั่นจอ.txt
กฎระเบียบและรูปแบบการแข่งขัน VALORANT รายการ PSU Phuket VALORANT 2026 Tournament.txt
```

## Converter

ไฟล์ script:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\tools\convert_competition_rules.py
```

วิธีรัน:

```powershell
cd "C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data"
py -3 tools\convert_competition_rules.py
```

## Output Files

```text
data/competition_rules/competition_rule_documents.jsonl
data/competition_rules/competition_rule_chunks.jsonl
data/curated/curated_competition_rules.jsonl
```

อัปเดตเพิ่มเติม 2026-07-02:

```text
data/competition_rules/competition_rule_fact_cards.jsonl
```

ไฟล์นี้ไม่ได้เป็น output ตรงจาก web scraping หรือ chunking แต่เป็น curated structured facts สำหรับคำถามกติกาที่ต้องแม่น เช่น ทีมละกี่คน, timeout, map pool, skin, อุปกรณ์, DLC character และ penalty บางกรณี

ตอน runtime ระบบจะลองใช้ fact card ก่อน ถ้าไม่มั่นใจค่อย fallback ไป `curated_competition_rules.jsonl`

ผลล่าสุด:

```text
documents: 4
chunks: 104
curated_rows: 104
```

## JSONL Schema

### Document Row

```json
{
  "id": "competition_rules_cs2_psu_phuket_2026",
  "category": "competition_rules_document",
  "title": "กฎระเบียบและรูปแบบการแข่งขัน Counter-Strike 2",
  "game": "Counter-Strike 2",
  "tournament": "PSU Phuket CS2 2026 Tournament",
  "source_file": "...txt",
  "source_path": "C:\\Users\\Chokhun\\Downloads\\...",
  "source_url": "local://competition_rules/competition_rules_cs2_psu_phuket_2026",
  "language": "th/mixed",
  "char_count": 4330,
  "line_count": 77,
  "tags": ["competition_rules", "document", "cs2"]
}
```

### Chunk Row

```json
{
  "id": "competition_rules_valorant_psu_phuket_2026_s06_c01",
  "document_id": "competition_rules_valorant_psu_phuket_2026",
  "category": "competition_rules",
  "title": "VALORANT: 1. เวลานอกทางยุทธวิธี (Tactical Timeout)",
  "game": "VALORANT",
  "tournament": "PSU Phuket VALORANT 2026 Tournament",
  "section_title": "1. เวลานอกทางยุทธวิธี (Tactical Timeout)",
  "text": "1. เวลานอกทางยุทธวิธี...",
  "source_url": "local://competition_rules/competition_rules_valorant_psu_phuket_2026",
  "tags": ["competition_rules", "valorant", "pause"],
  "priority": 90
}
```

### Curated Row

`data/curated/curated_competition_rules.jsonl` ใช้ schema เดียวกับ curated facts เดิม:

```json
{
  "id": "competition_rules_valorant_psu_phuket_2026_s06_c01",
  "category": "competition_rules",
  "title": "VALORANT: 1. เวลานอกทางยุทธวิธี (Tactical Timeout)",
  "text": "...",
  "source_url": "local://competition_rules/competition_rules_valorant_psu_phuket_2026",
  "source_ids": ["competition_rules_valorant_psu_phuket_2026", "competition_rules_valorant_psu_phuket_2026_s06_c01"],
  "tags": ["competition_rules", "valorant", "pause"],
  "priority": 90
}
```

## Pipeline Changes

เพิ่ม route ใหม่:

```text
competition_rules
```

คำถามที่เข้า route นี้จะไม่ใช้ rulebase จอง/ราคา/FAQ เพื่อกันชนผิดหมวด แต่จะใช้ curated retrieval จาก `curated_competition_rules.jsonl`

แก้ไฟล์:

```text
app/pipeline/router.py
app/pipeline/engine.py
app/pipeline/retrieval.py
```

## Retrieval Improvement

เพิ่ม Thai n-gram tokenizer เพื่อช่วยกรณีคำไทยติดกัน เช่น:

```text
ทีมละกี่คน
ใช้สกินได้ไหม
ขอ timeout ได้กี่ครั้ง
```

เพิ่ม game filter สำหรับ competition rules:

```text
CS2 -> ดึงเฉพาะ Counter-Strike 2
VALORANT / วาโล -> ดึงเฉพาะ VALORANT
RoV / Arena of Valor / Blueket -> ดึงเฉพาะ RoV
Tekken -> ดึงเฉพาะ Tekken 8
```

## Answer Policy

เพิ่มการจัดคำตอบเฉพาะหมวด `competition_rules` เพื่อไม่ให้ตอบเป็น chunk ดิบยาวๆ

รูปแบบคำตอบ:

```text
คำตอบ: ...

รายละเอียดที่เกี่ยวข้อง:
- ...

อ้างอิงจากกติกา: เกม / รายการ
แหล่งข้อมูล: local://competition_rules/...
```

Intent ที่รองรับเพิ่ม:

```text
จำนวนผู้เล่น/ทีมละกี่คน
timeout / pause / หยุดเกม / เวลานอก
สกิน / Default skin
อุปกรณ์ / ใช้เครื่องอะไรแข่ง
แผนที่ / map pool
บทลงโทษ / ปรับแพ้ / ตัดสิทธิ์
รูปแบบการแข่งขัน / BO3 / FT2
รายงานตัว / เช็คอินก่อนแข่ง
เริ่มแข่งช้า / มาสาย / เกิน 15 นาที
```

ตัวอย่าง:

```text
CS2 แข่งทีมละกี่คน
-> คำตอบ: แต่ละทีมประกอบด้วยผู้เล่น 5 คน
```

```text
VALORANT แผนที่ที่ใช้แข่งมีอะไรบ้าง
-> คำตอบ: แผนที่ที่ใช้แข่งมี 7 แผนที่ ได้แก่ Abyss, Ascent, Bind, Corrode, Haven, Lotus, Sunset
```

## Tested Questions

เพิ่มใน `tests/smoke_test_answer_pipeline.py`

```text
CS2 แข่งทีมละกี่คน
VALORANT Tactical Timeout ขอได้กี่ครั้ง
RoV ใช้สกินได้ไหม
Tekken 8 ใช้เครื่องอะไรแข่ง
VALORANT แผนที่ที่ใช้แข่งมีอะไรบ้าง
RoV ถ้าเริ่มแข่งช้าเกิน 15 นาทีโดนอะไร
```

ผล:

```text
OK pipeline:rag_direct_curated competition_rules | CS2 แข่งทีมละกี่คน
OK pipeline:rag_direct_curated competition_rules | VALORANT Tactical Timeout ขอได้กี่ครั้ง
OK pipeline:rag_direct_curated competition_rules | RoV ใช้สกินได้ไหม
OK pipeline:rag_direct_curated competition_rules | Tekken 8 ใช้เครื่องอะไรแข่ง
```

## Notes

- ข้อมูลยังเป็น local source เพราะมาจากไฟล์ `.txt` ที่ผู้ใช้ให้มา
- ถ้ามีไฟล์ใหม่ ให้เพิ่ม pattern/metadata ใน `tools/convert_competition_rules.py` แล้วรัน script ซ้ำ
- ถ้าต้องการตอบสวยขึ้น อาจเพิ่ม answer formatter เฉพาะ `competition_rules` ให้สรุปสั้นกว่านี้
