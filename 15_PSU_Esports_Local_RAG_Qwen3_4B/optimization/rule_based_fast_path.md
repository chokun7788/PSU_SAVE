# Rule-based FAQ Fast Path

Rule-based fast path คือการตอบคำถาม FAQ ที่ pattern ชัดเจนด้วย rule ก่อนเข้า RAG/LLM

ตัวอย่าง:

```text
ผู้ใช้ถาม: เช็คอินล่วงหน้าได้กี่นาที
-> match rule_checkin_advance
-> ตอบทันทีจาก curated fact
-> ไม่ต้องเรียก Qwen3
```

---

## ทำไมควรใช้

- เร็วกว่า RAG + LLM มาก
- ลด latency จากหลายสิบวินาทีเหลือระดับ milliseconds
- ลดโอกาส hallucination สำหรับกฎสำคัญ
- เหมาะกับ FAQ ซ้ำ ๆ
- เหมาะกับ Facebook chatbot ที่ต้องตอบไว

---

## ไฟล์ที่ใช้

```text
data/curated/rule_patterns.jsonl
scripts/rule_matcher.py
notebooks/01_local_rag_qwen3_4b.ipynb
```

---

## วิธีทดสอบ

```powershell
cd C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B
python scripts\rule_matcher.py "เช็คอินล่วงหน้าได้กี่นาที"
python scripts\rule_matcher.py "PS5 มีเกมอะไรบ้าง"
python scripts\rule_matcher.py "ศูนย์อยู่ที่ไหน"
```

---

## วิธีใช้ใน Notebook

ฟังก์ชัน `answer_question()` จะเช็ก rule ก่อนอัตโนมัติ:

```python
answer, hits, elapsed = answer_question("เช็คอินล่วงหน้าได้กี่นาที")
print(elapsed)
print(answer)
```

ถ้าต้องการปิด rule เพื่อเทียบกับ RAG + Qwen3 เต็ม ๆ:

```python
answer, hits, elapsed = answer_question("เช็คอินล่วงหน้าได้กี่นาที", use_rules=False)
```

ใน log จะมี `mode`:

```text
rule_fast_path = ตอบจาก rule
rag_llm = เข้า retrieval + Qwen3
```

---

## วิธีเพิ่ม Rule ใหม่

เพิ่ม 1 บรรทัดในไฟล์ `data/curated/rule_patterns.jsonl`

ตัวอย่าง:

```json
{"id":"rule_example","category":"reservation","intent":"example_intent","patterns":["ตัวอย่างคำถาม","example question"],"answer_th":"คำตอบภาษาไทย","answer_en":"English answer.","source_ids":["curated_example"],"source_url":"https://esports.phuket.psu.ac.th/","priority":100}
```

คำอธิบาย field:

- `id`: ชื่อ rule ห้ามซ้ำ
- `category`: หมวด เช่น `reservation`, `rules`, `games`, `contact`, `overview`
- `intent`: เจตนาของคำถาม
- `patterns`: regex หรือคำที่ใช้จับคำถาม
- `answer_th`: คำตอบภาษาไทย
- `answer_en`: คำตอบภาษาอังกฤษ
- `source_ids`: id ของ curated fact หรือ source ที่อ้างอิง
- `source_url`: URL แหล่งข้อมูล
- `priority`: เลขยิ่งสูงยิ่งถูกเลือกก่อน

หลังเพิ่ม rule ให้ทดสอบทันที:

```powershell
python scripts\rule_matcher.py "คำถามที่อยากทดสอบ"
```

---

## Flow ที่แนะนำ

```text
User question
-> Rule matcher
   -> ถ้า match ชัด: ตอบทันที
   -> ถ้าไม่ match: ใช้ RAG
      -> ถ้า retrieve ได้ curated fact ชัดเจน: ตอบจากข้อความที่ดึงมาโดยตรง
      -> ถ้ายังไม่ชัด: ใช้ RAG + LLM
```

---

## ควรใช้กับคำถามแบบไหน

- เช็คอินกี่นาที
- จองล่วงหน้ากี่ชั่วโมง
- จ่ายเงินภายในกี่นาที
- เลขบัญชี
- ค่าปรับ
- กฎห้ามสูบบุหรี่/แอลกอฮอล์/การพนัน
- PS5/Switch/PC/VR มีเกมอะไร
- email/Facebook/ที่ตั้ง/เบอร์โทร
- คำถามหน่วยเวลาง่าย ๆ เช่น นาที/วินาที/ชั่วโมง

---

## Rule ไม่ควรแข็งเกินไป

Rule ที่ดีควรตอบตามเจตนาและรูปแบบคำถาม เช่น ถ้าข้อมูลจริงคือ 30 นาที:

```text
ถาม: เช็คอินล่วงหน้าได้กี่นาที
ตอบ: 30 นาที

ถาม: เช็คอินล่วงหน้าได้กี่วินาที
ตอบ: 30 นาที หรือ 1,800 วินาที

ถาม: เช็คอินล่วงหน้าได้กี่ชั่วโมง
ตอบ: 0.5 ชั่วโมง หรือ 30 นาที
```

ถ้าคำถามต้องตีความซับซ้อนหรือไม่มี rule ชัดเจน ให้ปล่อยไป RAG แทน

---

## ไม่ควรใช้กับคำถามแบบไหน

- คำถามปลายเปิด
- คำถามที่ต้องสรุปหลายหน้า
- คำถามเปรียบเทียบ
- คำถามที่ phrasing หลากหลายมาก
- คำถามที่ต้อง reasoning

กรณีเหล่านี้ให้ใช้ RAG + Qwen3
