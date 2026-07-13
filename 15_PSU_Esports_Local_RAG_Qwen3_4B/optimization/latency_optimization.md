# Latency Optimization

เป้าหมาย MVP คือให้คำถามทั่วไปตอบได้ใกล้หรือต่ำกว่า 10 วินาที และคำถาม FAQ ซ้ำ ๆ ตอบได้ต่ำกว่า 1 วินาที

---

## ค่า Fast Mode ใน Notebook

ไฟล์หลัก:

```text
notebooks/01_local_rag_qwen3_4b.ipynb
```

ค่าที่ปรับแล้ว:

```python
FAST_LOCAL_MODEL = "qwen2.5:3b"
QUALITY_LOCAL_MODEL = "qwen3:4b"
LLM_MODEL = FAST_LOCAL_MODEL

TOP_K = 4
MAX_CONTEXT_CHARS = 3200
MAX_DOC_CHARS = 750
LLM_KEEP_ALIVE = "30m"
LLM_NUM_CTX = 2048
LLM_NUM_PREDICT = 120
LLM_TEMPERATURE = 0.0
```

---

## ทำไมเร็วขึ้น

- `qwen2.5:3b` ตอบตรงกว่าและไม่คิดออกเสียงแบบ Qwen3
- `num_predict=120` จำกัดความยาวคำตอบ
- `num_ctx=2048` ลด context window ที่โมเดลต้องประมวลผล
- `TOP_K=4` ลดจำนวน source ที่ส่งเข้า prompt
- `MAX_DOC_CHARS=750` ตัด chunk ที่ยาวเกินไป
- `keep_alive=30m` กันไม่ให้โมเดล unload บ่อย
- Rule-based fast path ตอบ FAQ ซ้ำ ๆ โดยไม่เรียก LLM

---

## ผลทดสอบบนเครื่องนี้

หลังโมเดล warm แล้ว:

```text
Rule-based FAQ: ประมาณ 0.006 วินาที
qwen2.5:3b + short context: ประมาณ 3-9 วินาที
qwen3:4b แบบเดิม: มักอยู่ประมาณ 20-40 วินาที
```

หมายเหตุ: รอบแรกหลังสลับโมเดลอาจช้ากว่าปกติ เพราะ Ollama ต้องโหลดโมเดลเข้า GPU ก่อน

---

## วิธีสลับโมเดล

เร็วกว่า:

```python
LLM_MODEL = FAST_LOCAL_MODEL
```

คุณภาพ/เหตุผลดีกว่า แต่ช้ากว่า:

```python
LLM_MODEL = QUALITY_LOCAL_MODEL
```

---

## วิธีทดสอบเวลา

```python
answer, hits, elapsed = answer_question("PS5 มีเกมอะไรบ้าง")
print(elapsed)
print(answer)
```

ถ้าต้องการวัดเฉพาะ RAG + LLM ไม่ผ่าน rule:

```python
answer, hits, elapsed = answer_question("PS5 มีเกมอะไรบ้าง", use_rules=False)
```

---

## ถ้ายังเกิน 10 วินาที

ให้ลองลดค่าตามลำดับนี้:

```python
LLM_NUM_PREDICT = 80
MAX_CONTEXT_CHARS = 2400
MAX_DOC_CHARS = 500
TOP_K = 3
```

ข้อแลกเปลี่ยนคือคำตอบจะสั้นลง และอาจมี source น้อยลง
