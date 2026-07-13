# 04 — RAG Pipeline: ค้นข้อมูลและให้ LLM ตอบ

RAG pipeline คือหัวใจของ chatbot

---

## 1. Input

ผู้ใช้ถาม เช่น:

```text
PS5 มีเกมอะไรบ้าง
```

---

## 2. Query Understanding

ตรวจว่าคำถามเกี่ยวกับอะไร:

| คำถาม | หมวดที่ควรค้น |
|---|---|
| จอง, session, เช็คอิน | reservation |
| PC, PS5, Switch, VR, เกม | services |
| แข่งขัน, tournament, RoV | competition |
| Esports คืออะไร, อาชีพ | knowledge |
| เบอร์, อีเมล, Facebook | contact |

---

## 3. Retrieval

ขั้นตอน:

1. embed คำถาม
2. ค้นใน vector DB
3. filter category ถ้ามี routing
4. ดึง top-k เช่น 5-8 chunks

ควรให้ curated facts มีน้ำหนักสูงกว่า chunk ดิบ

---

## 4. Rerank

หลัง retrieve อาจใช้ reranker จัดอันดับใหม่

เหมาะกับเว็บนี้เพราะ:

- มีชื่อเกมเยอะ
- ชื่อเกมบางชื่อซ้ำในหลายหน้า
- เมนูเว็บทำให้ keyword ปน
- คำถามภาษาไทยปนอังกฤษ

MVP ยังไม่ต้องมี reranker แต่ production ควรมี

---

## 5. Build Context

ตัวอย่าง context:

```text
[1]
title: เกมบน PlayStation 5
category: services
url: https://esports.computing.psu.ac.th/
text: PlayStation 5 มี PS5 #1 และ PS5 #2 ...

[2]
title: Our Games
category: services
url: ...
text: ...
```

---

## 6. Prompt

Prompt ต้องมี:

- system instruction
- context
- question
- answer format

ตัวอย่าง:

```text
ตอบจาก <context> เท่านั้น
ถ้าไม่มีข้อมูล ให้ตอบว่าไม่พบข้อมูล
ต้องอ้างอิงแหล่งที่มา

<context>
...
</context>

คำถาม: ...
```

---

## 7. Generation

ใช้ LLM temperature ต่ำ:

```text
temperature = 0 หรือ 0.2
```

เพราะต้องการคำตอบแม่น ไม่สร้างสรรค์เกินจริง

---

## 8. Output

รูปแบบคำตอบ:

```text
คำตอบ:
...

รายละเอียด:
- ...
- ...

อ้างอิง:
- ...
```

---

## 9. Guardrail

ถ้า context ไม่มีคำตอบ:

```text
ไม่พบข้อมูลนี้ในเว็บไซต์หรือเอกสารที่ดึงมา
```

ถ้าถาม real-time:

```text
ฉันยังไม่สามารถตรวจสอบสถานะว่างแบบ real-time ได้ กรุณาเปิดระบบจองโดยตรง
```

ถ้าถามข้อมูลส่วนตัว:

```text
ไม่สามารถให้ข้อมูลส่วนบุคคลของผู้จองหรือผู้ใช้บริการได้
```

---

## 10. Debug Retrieval

ทุกครั้งที่บอทตอบผิด ให้ดู:

- top-k chunks คืออะไร
- category ตรงไหม
- context มีคำตอบจริงไหม
- LLM ใช้ context หรือเดา

กฎ:

```text
ถ้า retrieve ผิด อย่าแก้ prompt ก่อน ให้แก้ retrieval
```

