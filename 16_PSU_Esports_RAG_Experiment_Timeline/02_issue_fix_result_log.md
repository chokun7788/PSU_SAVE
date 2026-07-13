# Issue, Fix, Result Log

ตารางสรุปปัญหาที่เจอ วิธีแก้ และผลลัพธ์

---

| ลำดับ | ปัญหาที่เจอ | สาเหตุที่คาดว่าเกิด | วิธีแก้ | ผลลัพธ์ |
|---:|---|---|---|---|
| 1 | ข้อมูลไทยบางส่วนอาจเพี้ยน | webscraping/encoding ผิด | เพิ่ม mojibake repair | ข้อความไทยใน chunks ดีขึ้น |
| 2 | chunk ข้อมูลไม่เหมาะกับ RAG | ตัดตามโครงสร้างเว็บไม่ดีพอ | ทำ `optimize_content.py` และ structure-aware chunking | ได้ `optimized_chunks.jsonl` |
| 3 | คำถามกฎ/จองดึงข้อมูลไม่แม่น | ข้อมูลสำคัญกระจายหลายหน้า | เพิ่ม curated facts | retrieval แม่นขึ้น |
| 4 | ไม่มีชุดทดสอบคุณภาพ | ยังไม่มี ground truth | สร้าง `ground_truth_full.jsonl` | มีชุดประเมิน 100+ คำถาม |
| 5 | Qwen3 ตอบช้า 20-40 วิ | thinking behavior, context/output ยาว | ลด context/output และหาโมเดลเร็ว | latency ลดลง |
| 6 | Qwen3 พิมพ์ reasoning | โมเดลเป็นสาย thinking | เพิ่ม cleaner และทดลอง `/no_think` | ดีขึ้นบางส่วน แต่ยังไม่เสถียร |
| 7 | ต้องการตอบ FAQ เร็ว | LLM ไม่เหมาะกับคำถามซ้ำ ๆ | เพิ่ม rule-based fast path | FAQ ตอบได้ประมาณ 0.006 วิ |
| 8 | Rule แข็งเกินไป | answer fix เป็นข้อความเดียว | เพิ่ม unit adaptation | ถามวินาที/ชั่วโมงตอบตามหน่วยได้ |
| 9 | RAG ดึง source ถูก แต่ LLM ตอบไม่พบข้อมูล | generation ตัดสินใจผิด | เพิ่ม `rag_direct_curated` | ตอบจาก curated fact โดยตรง |
| 10 | Debug ยากว่าใช้ mode ไหน | ไม่มี flag แยก path | เพิ่ม `use_rules` และ `use_direct` | ทดสอบแยก rule/direct/LLM ได้ |

---

## รายละเอียดปัญหาสำคัญ

### 1. Latency สูง

อาการ:

```text
ตอบหนึ่งครั้งใช้เวลาประมาณ 20-40 วินาที
```

ค่าที่ทำให้ช้า:

```python
num_ctx = 8192
num_predict = 1600
TOP_K = 6
MAX_CONTEXT_CHARS = 7000
```

ค่าที่ปรับใหม่:

```python
LLM_MODEL = "qwen2.5:3b"
TOP_K = 4
MAX_CONTEXT_CHARS = 3200
MAX_DOC_CHARS = 750
LLM_NUM_CTX = 2048
LLM_NUM_PREDICT = 120
LLM_KEEP_ALIVE = "30m"
```

ผล:

```text
FAQ rule: ประมาณ 0.006 วิ
qwen2.5:3b หลัง warm: ประมาณ 3-9 วิ
qwen3:4b เดิม: ประมาณ 20-40 วิ
```

---

### 2. Rule-based ตอบเร็วแต่ต้องไม่แข็งเกินไป

อาการ:

```text
ถาม: เช็คอินล่วงหน้าได้กี่วินาที
ตอบ: เช็คอินได้ล่วงหน้าสูงสุด 30 นาที
```

ปัญหา:

- คำตอบถูกในเชิงข้อมูล แต่ไม่ตอบตามหน่วยที่ผู้ใช้ถาม
- ผู้ใช้ถามวินาที ก็ควรแปลงเป็นวินาทีให้

วิธีแก้:

- เพิ่ม `adapt_answer_to_query()` ใน `scripts/rule_matcher.py`

ผล:

```text
ถาม: เช็คอินล่วงหน้าได้กี่วินาที
ตอบ: เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที

ถาม: เช็คอินล่วงหน้าได้กี่ชั่วโมง
ตอบ: เช็คอินได้ล่วงหน้าสูงสุด 0.5 ชั่วโมง หรือ 30 นาที
```

---

### 3. RAG ดึงถูกแต่ LLM ตอบผิด

อาการ:

```text
question = "ศูนย์นี้เกี่ยวกับอะไร"
use_rules = False

retrieved_ids:
- curated_overview_identity
- curated_overview_mission

answer:
ไม่พบข้อมูลนี้ในฐานข้อมูลที่มี
```

วิเคราะห์:

- Retrieval ถูก
- Context มีคำตอบ
- LLM generation ผิด

วิธีแก้:

- เพิ่ม direct fallback
- ถ้า top hit เป็น `curated_fact` ในหมวดสำคัญ ให้ตอบจาก retrieved text โดยตรง

ผล:

```text
mode = rag_direct_curated
answer = สรุปจาก curated_overview_identity และ curated_overview_mission
```

---

## วิธีดูว่าแต่ละคำตอบมาจากอะไร

เปิดไฟล์:

```text
C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B\logs\chat_log.jsonl
```

ดู field:

```json
{
  "mode": "rule_fast_path",
  "question": "...",
  "retrieved_ids": ["..."],
  "model": "...",
  "latency_sec": 0.001
}
```

ความหมายของ `mode`:

| mode | ความหมาย | ควรใช้เมื่อ |
|---|---|---|
| `rule_fast_path` | ตอบจาก rule | FAQ ซ้ำ ๆ / กฎสำคัญ |
| `rag_direct_curated` | retrieve แล้วตอบจาก curated fact | ข้อมูล fact ชัดเจน |
| `rag_llm` | retrieve แล้วให้ LLM สรุป | คำถามเปิด/ต้องสรุปหลาย context |

---

## วิธีแยกปัญหา

### ถ้าคำตอบผิด

เช็กตามลำดับ:

1. `mode` คืออะไร
2. `retrieved_ids` ดึง source ถูกไหม
3. ถ้า source ผิด ให้แก้ retrieval/category/chunking
4. ถ้า source ถูกแต่ answer ผิด ให้แก้ prompt หรือใช้ direct fallback
5. ถ้าเป็น FAQ ซ้ำ ให้เพิ่ม rule

### ถ้าตอบช้า

เช็กตามลำดับ:

1. เข้า `rule_fast_path` หรือไม่
2. ถ้าเข้า `rag_llm` ให้ดู context ยาวไหม
3. ลด `TOP_K`
4. ลด `MAX_CONTEXT_CHARS`
5. ลด `LLM_NUM_PREDICT`
6. ใช้ `qwen2.5:3b` แทน `qwen3:4b`

### ถ้าถามรูปแบบใหม่แล้ว rule ไม่ match

ให้เพิ่ม pattern ใน:

```text
data/curated/rule_patterns.jsonl
```

แล้วทดสอบ:

```powershell
python scripts\rule_matcher.py "คำถามที่ต้องการทดสอบ"
```

