# Next Checklist

รายการสิ่งที่ควรเช็ก/ทดลองต่อหลังจากรอบล่าสุด

---

## 1. ทดสอบคำถาม Paraphrase

เพิ่มคำถามที่ความหมายเหมือนกันแต่รูปแบบต่างกัน เช่น:

```text
เช็คอินได้เร็วสุดกี่นาที
เข้าเช็คอินก่อนเวลาได้ไหม
เช็คอินก่อนกี่วินาที
เช็คอินได้ก่อนกี่ชั่วโมง
ถ้าไปช้าจะเป็นอะไรไหม
PS5 มีเกมไร
เกมเพลย์ห้ามอะไรบ้าง
ศูนย์นี้ทำอะไร
ศูนย์นี้เกี่ยวกับอะไร
ที่นี่คืออะไร
```

เป้าหมาย:

- ดูว่าเข้า rule หรือ RAG
- ดูว่า retrieved_ids ถูกไหม
- เพิ่ม pattern เฉพาะที่จำเป็น

---

## 2. เพิ่ม Ground Truth สำหรับ Rule

ควรเพิ่มชุด test สำหรับ rule โดยเฉพาะ:

```json
{"question":"เช็คอินล่วงหน้าได้กี่วินาที","expected_rule_id":"rule_checkin_advance","expected_keywords":["1,800","วินาที"]}
{"question":"ศูนย์นี้เกี่ยวกับอะไร","expected_rule_id":"rule_overview_identity","expected_keywords":["ศูนย์พัฒนาการเรียนรู้","อีสปอร์ต"]}
```

เหตุผล:

- กัน rule พังตอนเพิ่ม pattern ใหม่
- เช็กว่า unit adaptation ยังทำงาน
- ใช้ demo ได้ว่าระบบไม่ได้ลองมั่ว

---

## 3. เพิ่ม Rule เฉพาะ FAQ ที่เจอบ่อย

ควรเพิ่มเฉพาะคำถามที่:

- ผู้ใช้ถามซ้ำบ่อย
- คำตอบเป็น fact ชัดเจน
- ผิดแล้วมีความเสี่ยง เช่น กฎ, ค่าปรับ, การจอง, คืนเงิน

ไม่ควรเพิ่ม rule กับ:

- คำถามปลายเปิดมาก
- คำถามต้องสรุปหลายหน้า
- คำถามที่มีเงื่อนไขซับซ้อน

---

## 4. เช็ก RAG Retrieval

สำหรับคำถามที่ไม่เข้า rule ให้เช็ก:

```python
answer, hits, elapsed = answer_question("คำถาม", use_rules=False)
[(h["id"], h["metadata"].get("category"), h["metadata"].get("title")) for h in hits]
```

ถ้า `hits` ไม่ตรง:

- เพิ่ม keyword ใน `route_category()`
- เพิ่ม curated fact
- ปรับ title/tags ใน chunk
- rebuild Chroma index

---

## 5. เช็ก LLM Generation

ใช้คำสั่งนี้เพื่อบังคับ RAG + LLM ล้วน:

```python
answer, hits, elapsed = answer_question(
    "ศูนย์นี้เกี่ยวกับอะไร",
    use_rules=False,
    use_direct=False
)
```

ถ้า LLM ตอบผิดทั้งที่ retrieved ถูก:

- ปรับ prompt
- ลด context ที่ไม่เกี่ยวข้อง
- ใช้ direct curated fallback
- เพิ่ม curated answer สำหรับคำถามนั้น

---

## 6. เก็บ Latency Benchmark

ควรทำตารางวัดเวลา:

| คำถาม | mode | model | latency | ถูกไหม |
|---|---|---|---:|---|
| เช็คอินล่วงหน้าได้กี่นาที | rule_fast_path | rule | 0.006 | yes |
| ศูนย์นี้เกี่ยวกับอะไร | rule_fast_path | rule | 0.001 | yes |
| ติดต่อศูนย์ได้ทางไหน | rag_direct_curated หรือ rag_llm | qwen2.5:3b | 3-5 | yes |

เป้าหมาย:

```text
FAQ: < 1 วิ
RAG direct: < 1 วิ
RAG + LLM: < 10 วิ เมื่อโมเดล warm แล้ว
```

---

## 7. เตรียมต่อ FastAPI / Facebook

ก่อนต่อ Facebook ควรมี API แบบ local ก่อน:

```text
POST /chat
request: { "message": "..." }
response: {
  "answer": "...",
  "mode": "rule_fast_path",
  "sources": [...],
  "latency_sec": 0.006
}
```

สิ่งที่ควร log:

- user message
- answer
- mode
- retrieved_ids
- latency
- error
- timestamp

---

## 8. สิ่งที่ควรถาม/ขอข้อมูลเพิ่มจากศูนย์

- กฎ official ฉบับล่าสุด
- PDF หรือเอกสารการจองล่าสุด
- FAQ จากแอดมิน/เพจ Facebook
- ข้อมูลราคาและค่าปรับที่ยืนยันแล้ว
- ข้อมูลเกม/อุปกรณ์ล่าสุด
- ข้อความ disclaimer ที่อยากให้บอทตอบเมื่อไม่มั่นใจ
- ขอบเขตว่าบอทตอบได้แค่ FAQ หรือให้ทำ action เช่น จอง/ยกเลิกด้วย

