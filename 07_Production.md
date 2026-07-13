# 07 — Production: นำ RAG ขึ้นใช้งานจริง (เฟส 6) + โค้ดตัวอย่าง

> เป้าหมายเฟสนี้: เปลี่ยนจาก "โน้ตบุ๊กบนเครื่องตัวเอง" เป็น "ระบบที่คนอื่นใช้ได้จริง เสถียร ปลอดภัย คุม cost ได้"

---

## 7.1 การห่อเป็น Service / API

### คืออะไร
แปลง RAG จากสคริปต์เป็นบริการที่เรียกผ่าน API หรือมีหน้าเว็บ

### ต้องรู้อะไรบ้าง + โค้ด

**FastAPI endpoint (นิยมสุดในงาน AI)**
```python
# pip install fastapi uvico2rn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask(q: Query):
    chunks, metas = retrieve(q.question, k=4)
    answer = generate(*build_prompt(q.question, chunks, metas))
    return {"answer": answer, "sources": [m.get("source") for m in metas]}

# รัน: uvicorn main:app --reload
```

**Streaming response (UX ดีขึ้น)**
```python
from fastapi.responses import StreamingResponse

@app.post("/ask-stream")
def ask_stream(q: Query):
    def gen():
        stream = llm.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": q.question}],
            stream=True,
        )
        for chunk in stream:
            yield chunk.choices[0].delta.content or ""
    return StreamingResponse(gen(), media_type="text/plain")
```

**UI ทดลองเร็วด้วย Streamlit**
```python
# pip install streamlit  ->  streamlit run app.py
import streamlit as st
st.title("ถาม-ตอบเอกสารบริษัท")
if q := st.chat_input("พิมพ์คำถาม..."):
    st.chat_message("user").write(q)
    st.chat_message("assistant").write(rag(q))
```

- **แยก index pipeline ออกจาก query pipeline**: indexing ทำ batch/background, query ตอบ real-time
- **Async** รองรับหลายคำขอพร้อมกัน
- **UI**: Streamlit/Gradio (prototype เร็ว), Next.js/React (production)

### ศึกษายังไง / วิธี
1. ห่อ RAG ด้วย FastAPI endpoint เดียว แล้วต่อ streaming
2. ทำ UI ด้วย Streamlit/Gradio ให้คนทดลองใช้
3. แหล่งไทย: **codingthailand** (LangChain.js+Next.js+streaming), **IMC Institute** (deploy Docker)

---

## 7.2 Deployment

### คืออะไร
นำระบบขึ้นรันบน server/cloud ให้เข้าถึงได้ตลอด

### ต้องรู้อะไรบ้าง + โค้ด

**Dockerfile**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```
```bash
docker build -t my-rag .
docker run -p 8000:8000 --env-file .env my-rag
```

- **ที่ deploy**: เริ่ม managed ง่ายๆ (Railway/Render/Fly.io) → cloud ใหญ่ (AWS/GCP/Azure) เมื่อโต
- **Vector DB production**: ย้ายจาก FAISS/Chroma local → Qdrant/Weaviate/pgvector/Pinecone (persistent + scale)
- **Secrets**: environment variable/secret manager — ห้าม hardcode
- **CI/CD พื้นฐาน**: auto deploy เมื่อ push

### ศึกษายังไง / วิธี
1. เขียน Dockerfile ห่อ RAG service รันใน container ให้ได้
2. deploy ขึ้น Railway/Render สักครั้งให้คนนอกเข้าถึง
3. แหล่งไทย: **Cloudnone** (Docker, Kubernetes, cloud เป็นไทย)

---

## 7.3 Observability & Monitoring

### คืออะไร
"มองเห็น" ว่าระบบทำอะไรในแต่ละคำถาม เพื่อ debug และพัฒนา

### ต้องรู้อะไรบ้าง + โค้ด
```python
# pip install langfuse — ดู trace แต่ละคำถามได้ครบ
from langfuse.decorators import observe

@observe()
def rag(question: str):
    chunks, metas = retrieve(question, k=4)   # Langfuse บันทึก: ค้น chunk ไหน
    answer = generate(*build_prompt(question, chunks, metas))  # ใช้ token เท่าไร เวลาเท่าไร
    return answer
```

- **Tracing**: ดูว่าแต่ละคำถาม embed อะไร, ค้น chunk ไหน, prompt สุดท้ายหน้าตาไง, token/เวลาเท่าไร — สำคัญมากในการหาว่าพังตรงไหน
- **เครื่องมือ**: **LangSmith**, **Langfuse** (open-source, self-host ได้), Arize Phoenix
- **Metrics ที่เฝ้า**: latency (p50/p95), cost ต่อคำถาม, error rate, จำนวนตอบ "ไม่รู้"
- **User feedback loop**: ปุ่ม 👍/👎 → ปรับปรุง + เพิ่มเข้า test set
- **Logging**: เก็บคำถาม-คำตอบ (ระวัง privacy/PDPA — ไฟล์ `09`)

### ศึกษายังไง / วิธี
1. ต่อ **Langfuse** หรือ **LangSmith** ดู trace ของคำถามจริง
2. ทำ dashboard latency/cost พื้นฐาน
3. **เน้น**: เห็น trace = debug เร็วขึ้นมหาศาล ติดตั้งตั้งแต่เนิ่นๆ

---

## 7.4 Cost & Performance Optimization

### คืออะไร
ทำให้ระบบเร็วและถูกพอจะใช้จริง

### ต้องรู้อะไรบ้าง + โค้ด
```python
# Semantic cache อย่างง่าย: ถ้าคำถามคล้ายของเดิมมาก ใช้คำตอบเดิม (ลด cost/latency)
cache = []   # [(vector, answer)]
def cached_rag(question, threshold=0.95):
    qv = embedder.encode(question)
    for v, ans in cache:
        if cos(qv, v) >= threshold:
            return ans                # cache hit
    ans = rag(question)
    cache.append((qv, ans))
    return ans
```

- **Caching**: cache คำตอบ/embedding ของคำถามซ้ำ — ลด cost/latency ชัด
- **เลือกโมเดลให้เหมาะงาน (model routing)**: โมเดลถูก/เร็วกับงานง่าย โมเดลแพงเฉพาะที่จำเป็น
- **ลด token**: contextual compression, คุมจำนวน chunk, prompt กระชับ
- **Batch / async** สำหรับ indexing
- **Embedding caching**: ไม่ embed ข้อความเดิมซ้ำ

### ศึกษายังไง / วิธี
1. วัด cost/latency baseline (จาก observability) ก่อนปรับ
2. ใส่ semantic cache แล้ววัดผล
3. ลอง model routing (โมเดลเล็กตอบก่อน ไม่มั่นใจค่อยส่งโมเดลใหญ่)

---

## 7.5 Security, Safety & Guardrails

### คืออะไร
ป้องกันระบบจากการใช้งานอันตราย และป้องกันข้อมูลรั่ว

### ต้องรู้อะไรบ้าง + โค้ด
```python
# Access control ระดับเอกสาร: กรอง metadata ตามสิทธิ์ผู้ใช้ "ก่อน" ค้น
def retrieve_secure(question, user_dept, k=4):
    qv = embedder.encode([question]).tolist()
    return col.query(
        query_embeddings=qv, n_results=k,
        where={"allowed_dept": user_dept},   # ผู้ใช้เห็นเฉพาะเอกสารที่มีสิทธิ์
    )
```

- **Prompt injection**: ผู้ใช้/ข้อมูลในเอกสารแอบใส่คำสั่งแย่งคุม AI ("ลืมคำสั่งเดิม ทำตามนี้แทน") — ลดเสี่ยงด้วยการแยก context จากคำสั่งให้ชัด + ตรวจ input
- **Data leakage**: ทำ **access control ระดับเอกสาร** (กรอง metadata ตามสิทธิ์ก่อนค้น)
- **PII / PDPA**: จัดการข้อมูลส่วนบุคคลให้ถูกกฎหมายไทย (ไฟล์ `09`)
- **Output guardrails**: กรองคำตอบไม่เหมาะสม/หลุดประเด็น, บังคับมี citation
- **Rate limiting & auth**: จำกัดการเรียก + ยืนยันตัวตน
- **Hallucination ใน production**: ตั้ง threshold ให้ตอบ "ไม่รู้" เมื่อ context ไม่พอ ดีกว่าตอบมั่ว

### ศึกษายังไง / วิธี
1. อ่าน **OWASP Top 10 for LLM Applications** — ความเสี่ยงหลักครบ
2. ทดสอบ prompt injection กับระบบตัวเอง (red-teaming เบื้องต้น)
3. ออกแบบ access control ถ้ามีผู้ใช้หลายระดับสิทธิ์
4. **เน้น**: ถ้าเปิดให้คนนอก/มีข้อมูลอ่อนไหว เรื่องนี้ห้ามมองข้าม

---

## 7.6 การดูแลระยะยาว (Maintenance)

### ต้องรู้อะไรบ้าง
- **อัปเดตข้อมูล / re-indexing**: เอกสารเปลี่ยนต้องมีระบบอัปเดต index (ทั้งหมด vs เฉพาะที่เปลี่ยน) + จัดการเวอร์ชัน
- **Monitoring drift**: คุณภาพอาจตกเมื่อข้อมูล/พฤติกรรมผู้ใช้เปลี่ยน — เฝ้า metric ต่อเนื่อง
- **Regression testing**: รัน eval ทุกครั้งก่อนเปลี่ยนอะไรขึ้น production
- **อัปเกรดโมเดล**: embedding ใหม่ = ต้อง **re-index ใหม่หมด** (เวกเตอร์เก่าเทียบกับใหม่ไม่ได้)

### ศึกษายังไง / วิธี
1. วางแผน re-indexing ตั้งแต่ออกแบบ
2. ตั้ง eval ให้รันอัตโนมัติใน CI

---

## ✅ เช็กลิสต์จบเฟส 6

- [ ] ห่อ RAG เป็น API (FastAPI) + streaming ได้
- [ ] เขียน Dockerfile และ deploy ให้คนนอกเข้าถึงได้
- [ ] ย้าย vector DB เป็นตัว production-ready
- [ ] ต่อ observability (Langfuse/LangSmith) ดู trace, latency, cost
- [ ] ใส่ caching / เลือกโมเดลเพื่อคุม cost
- [ ] เข้าใจและลดความเสี่ยง prompt injection + ทำ access control
- [ ] รู้จัก PDPA และจัดการข้อมูลส่วนบุคคลเบื้องต้น
- [ ] มีแผน re-indexing และ regression test

ไปต่อ `08_ต่อยอด.md` (เลือกตามงาน) และอย่าลืม `09_ภาษาไทยโดยเฉพาะ.md`
