# 06 — Evaluation Pipeline: วัดผลบอท

Evaluation คือขั้นตอนที่ทำให้รู้ว่าบอทดีจริง ไม่ใช่แค่รู้สึกว่าดี

---

## 1. สิ่งที่ต้องวัด

### Retrieval Quality

คำถามหนึ่งข้อ ระบบค้นเจอข้อมูลถูกไหม

ดูจาก:

- category ที่เจอ
- chunk title
- text มีคำตอบจริงไหม
- source URL ถูกไหม

### Answer Quality

LLM ตอบถูกไหม

ดูจาก:

- ตอบตรงคำถาม
- ครบประเด็น
- ไม่ hallucinate
- มี citation
- ภาษาชัดเจน

### Safety

บอทไม่ทำสิ่งที่ห้ามทำไหม

เช่น:

- ไม่บอกข้อมูลส่วนตัว
- ไม่เดา real-time booking
- ไม่ตอบนอกเว็บ

---

## 2. Test Set

ใช้ไฟล์จาก starter kit:

```text
11_PSU_Esports_AI_ChatBot/eval/testset.jsonl
```

ควรเพิ่มเองเรื่อย ๆ

โครง record:

```json
{
  "id": "q001",
  "question": "จองต้องล่วงหน้ากี่ชั่วโมง",
  "expected_category": "reservation",
  "expected_behavior": "answer_from_context",
  "must_contain": ["1 ชั่วโมง"]
}
```

---

## 3. Evaluation Flow

```text
for each question:
  retrieve
  check category
  build prompt
  generate answer
  check must_contain
  check citation
  save result
```

---

## 4. Metrics ง่าย ๆ สำหรับ MVP

| metric | ความหมาย |
|---|---|
| category_accuracy | retrieve ได้หมวดถูกไหม |
| must_contain_pass | คำตอบมีคำสำคัญไหม |
| citation_rate | มี citation ไหม |
| refusal_pass | คำถามนอกขอบเขตตอบไม่พบไหม |
| realtime_guardrail_pass | ไม่เดาสถานะจอง real-time ไหม |

---

## 5. เกณฑ์ผ่าน

MVP:

- category accuracy >= 80%
- must contain pass >= 80%
- citation rate >= 90%
- out-of-scope refusal >= 95%
- real-time guardrail >= 95%

Production:

- category accuracy >= 90%
- must contain pass >= 90%
- citation rate >= 95%
- safety guardrail >= 99%

---

## 6. Error Analysis

ถ้าผิด ให้จัดประเภท:

| error | สาเหตุ | วิธีแก้ |
|---|---|---|
| retrieve ผิดหมวด | routing ไม่ดี | เพิ่ม keyword routing |
| retrieve เจอข้อมูลกว้างเกิน | chunk noisy | curated facts / rerank |
| LLM ตอบเกิน context | prompt อ่อน | เพิ่ม guardrail |
| ไม่มี citation | prompt ไม่บังคับ | ปรับ answer format |
| ถาม real-time แล้วเดา | safety ไม่พอ | เพิ่ม rule |

---

## 7. Human Review

ช่วงแรกควรให้คนตรวจคำตอบอย่างน้อย:

- 20 คำถามแรก
- ทุกครั้งที่เปลี่ยน prompt
- ทุกครั้งที่เปลี่ยน embedding model
- ทุกครั้งที่เพิ่มหมวด news

