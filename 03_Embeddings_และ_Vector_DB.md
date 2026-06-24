# 03 — Embeddings และ Vector Database (เฟส 2) + โค้ดตัวอย่าง

> เป้าหมายเฟสนี้: เข้าใจ "หัวใจ" ที่ทำให้ RAG เป็นไปได้ — การค้นข้อมูลด้วยความหมาย (semantic search)

---

## 2.1 Embeddings

### คืออะไร
**Embedding** = แปลงข้อความเป็น **เวกเตอร์ตัวเลข** ที่จับ "ความหมาย" ไว้
กฎทอง: **ข้อความความหมายใกล้กัน → เวกเตอร์อยู่ใกล้กัน**

### ต้องรู้อะไรบ้าง + โค้ด

**สร้าง embedding ด้วย sentence-transformers (ฟรี รันบนเครื่อง — เริ่มจากตัวนี้)**
```python
# pip install sentence-transformers
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("intfloat/multilingual-e5-small")  # รองรับไทย
vecs = model.encode(["สุนัขน่ารัก", "หมาน่ารัก", "รถยนต์เร็วมาก"])
print(vecs.shape)   # (3, 384)  -> 3 ประโยค เวกเตอร์ละ 384 มิติ
```

**หรือใช้ API embedding (เมื่อต้องการคุณภาพ/ความสะดวก)**
```python
from openai import OpenAI
client = OpenAI()
r = client.embeddings.create(model="text-embedding-3-small", input=["ข้อความ A", "ข้อความ B"])
vec_a = r.data[0].embedding   # list ความยาว 1536
```

### ต้องรู้อะไรบ้าง (concept)
- **มิติ (dimensions)**: จำนวนตัวเลขในเวกเตอร์ (384/768/1024/1536) — เยอะมักละเอียดกว่าแต่กินที่มากกว่า
- **Embedding model ≠ LLM**: เป็นคนละโมเดลกับตัวที่ใช้ตอบ
- **เลือกยังไง**: (1) รองรับภาษาไหม — **ไทยต้อง multilingual/โมเดลไทย** (ไฟล์ `09`), (2) ความยาวสูงสุดที่รับได้, (3) มิติ, (4) ความเร็ว/ราคา, (5) คะแนน MTEB
- **MTEB leaderboard**: เทียบ embedding model (Hugging Face)
- **ต้องใช้ model ตัวเดียวกันทั้ง index และ query** ไม่งั้นเทียบกันไม่ได้ (ข้อผิดพลาดที่เจอบ่อย)
- **Dense vs Sparse**: dense = จับความหมาย (ที่คุยอยู่); sparse = keyword (BM25) — RAG ดีมักผสมทั้งสอง (hybrid — ไฟล์ `05`)

### ศึกษายังไง / วิธี
1. บล็อกไทยอธิบาย embedding/DPR เช่นบทความ **Orapin Anonthanasap** (Medium)
2. ลงมือ: encode 5 ประโยคแล้ว print เวกเตอร์
3. ดู MTEB เลือกโมเดลที่รองรับไทย
4. **โปรเจคจบหัวข้อ**: encode 10 ประโยค คำนวณว่าประโยคไหนใกล้คำถามสุด

---

## 2.2 Similarity — การวัดความคล้าย

### คืออะไร
วิธีคำนวณว่าเวกเตอร์สองตัว "ใกล้กัน" แค่ไหน — หัวใจของการค้น

### ต้องรู้อะไรบ้าง + โค้ด
```python
import numpy as np
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("intfloat/multilingual-e5-small")

def cos(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

docs = ["วันลาพักร้อนมี 10 วัน", "เวลาทำการ 9 โมงถึง 6 โมง", "เบิกค่าเดินทางต้องแนบใบเสร็จ"]
query = "ลาหยุดได้กี่วัน"
dv = model.encode(docs)
qv = model.encode(query)

scores = [(cos(qv, d), doc) for d, doc in zip(dv, docs)]
scores.sort(reverse=True)
for s, doc in scores:
    print(f"{s:.3f}  {doc}")
# ประโยคเรื่องวันลาจะได้คะแนนสูงสุด แม้ query ใช้คำว่า "ลาหยุด" ไม่ตรงกับ "ลาพักร้อน"
```

- **Cosine similarity**: วัดมุม — นิยมสุดในงาน text (ใกล้ 1 = คล้ายมาก)
- **Dot product**: เร็ว ใช้บ่อยเมื่อ normalize แล้ว
- **Euclidean (L2)**: ระยะตรง — ยิ่งน้อยยิ่งใกล้
- **Top-k**: ดึง k อันที่ใกล้สุด (เช่น top-5) มาเป็น context

### ศึกษายังไง / วิธี
1. ค้น "cosine similarity อธิบาย" ดูคลิป/บทความสั้น
2. คำนวณ cosine ด้วย numpy เองสัก 1 ครั้ง (เข้าใจลึกขึ้นเยอะ)
3. ทดลองเปลี่ยน metric ดูผล

---

## 2.3 Vector Database

### คืออะไร
ฐานข้อมูลที่เก็บ **เวกเตอร์** และค้น "เวกเตอร์ที่ใกล้ที่สุด" ได้เร็วแม้มีข้อมูลล้านชิ้น

### ต้องรู้อะไรบ้าง + โค้ด (Chroma — ง่ายสุดสำหรับมือใหม่)
```python
# pip install chromadb sentence-transformers
import chromadb
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("intfloat/multilingual-e5-small")

client = chromadb.PersistentClient(path="./chroma_db")   # เก็บลงดิสก์ ไม่หายเมื่อปิดโปรแกรม
col = client.get_or_create_collection("company_docs")

docs = [
    "วันลาพักร้อนมี 10 วันต่อปี",
    "เวลาทำการ จันทร์-ศุกร์ 9.00-18.00",
    "เบิกค่าเดินทางต้องแนบใบเสร็จและให้หัวหน้าอนุมัติ",
]
col.add(
    ids=["d1", "d2", "d3"],
    embeddings=model.encode(docs).tolist(),
    documents=docs,
    metadatas=[{"section": "HR"}, {"section": "HR"}, {"section": "Finance"}],  # เก็บ metadata
)

# ค้น top-2 + กรอง metadata เฉพาะแผนก HR
q = model.encode(["ลาหยุดกี่วัน"]).tolist()
res = col.query(query_embeddings=q, n_results=2, where={"section": "HR"})
print(res["documents"][0])
```

**FAISS — library ค้นเวกเตอร์ในหน่วยความจำ (เร็ว เหมาะโปรเจคเล็ก/เรียน)**
```python
# pip install faiss-cpu
import faiss, numpy as np
vecs = model.encode(docs).astype("float32")
faiss.normalize_L2(vecs)                 # normalize เพื่อใช้ dot = cosine
index = faiss.IndexFlatIP(vecs.shape[1]) # inner product
index.add(vecs)
qv = model.encode(["ลาหยุดกี่วัน"]).astype("float32"); faiss.normalize_L2(qv)
scores, ids = index.search(qv, k=2)
print([docs[i] for i in ids[0]])
```

### ต้องรู้อะไรบ้าง (concept)
- **หน้าที่**: เก็บเวกเตอร์ + metadata และทำ similarity search ดึง top-k
- **ANN (HNSW, IVF)**: อัลกอริทึมค้นเวกเตอร์ใกล้สุดแบบ "ประมาณ" เพื่อความเร็ว — รู้จักชื่อพอ
- **Metadata filtering**: กรองด้วยเงื่อนไข เช่น "เฉพาะปี 2024" — สำคัญมากในงานจริง
- **ตัวเลือก** (เริ่มจากง่าย): **FAISS/Chroma** (local, ฟรี, เรียน) → **Qdrant/Weaviate/Milvus** (production, filtering/scaling ดี) → **pgvector** (ถ้าใช้ Postgres อยู่แล้ว) → **Pinecone** (managed, จ่ายเงิน)
- **เกณฑ์เลือก**: ขนาดข้อมูล, filtering ซับซ้อนไหม, self-host vs managed, งบ, SDK ที่ถนัด
- **CRUD บนเวกเตอร์**: เพิ่ม/อัปเดต/ลบ — ในระบบจริงข้อมูลเปลี่ยนตลอด

### ศึกษายังไง / วิธี
1. บล็อกไทย **VulturePrime "RAG 101"** (เทียบ query กับข้อมูลใน vector DB)
2. เริ่มจาก **Chroma** หรือ **FAISS**
3. คอร์สสั้นฟรี **DeepLearning.AI**: "Building Applications with Vector Databases"
4. **โปรเจคจบหัวข้อ**: เก็บ 50 ประโยคลง Chroma ค้น top-3 พร้อม metadata

---

## 2.4 Semantic Search (ปะติดเป็นภาพ)

### คืออะไร
ค้นข้อมูล "ด้วยความหมาย" แทน "คำตรงเป๊ะ" — สิ่งที่ embedding + vector DB ทำงานร่วมกันแล้วได้

### ต้องรู้อะไรบ้าง
- flow เต็ม: ข้อความ → embedding → เก็บใน vector DB || คำถาม → embedding → ค้น top-k → ได้ข้อความเกี่ยวข้อง
- **ต่างจาก keyword search**: keyword หาคำตรงเป๊ะ ("รถ" ไม่เจอ "ยานพาหนะ"), semantic เข้าใจความหมายจึงเจอแม้คำต่างกัน
- **ข้อจำกัด**: คำเฉพาะ/ชื่อรุ่น/รหัสที่ต้องตรงเป๊ะ semantic อาจพลาด → ต้องมี hybrid (ไฟล์ `05`)

### ศึกษายังไง / วิธี
1. รวมโปรเจค 2.1–2.3 เป็น semantic search เล็กๆ
2. **โปรเจคจบเฟส**: semantic search บนข้อมูลจริงของตัวเอง (โน้ต/FAQ) — ค้นด้วยภาษาธรรมชาติให้แม่นก่อน **ยังไม่ต้องใส่ LLM ตอบ**

> 💡 ทำตรงนี้ได้ เหลือแค่ "เอาผลที่ค้นยัดเข้า LLM ให้สรุป" ก็เป็น RAG เต็มตัว (เฟส 3)

---

## ✅ เช็กลิสต์ก่อนขึ้นเฟส 3

- [ ] อธิบาย embedding ได้ และ "ความหมายใกล้กัน = เวกเตอร์ใกล้กัน"
- [ ] เลือก embedding model ที่รองรับไทย และรู้ว่าต้องใช้ตัวเดียวกันทั้ง index/query
- [ ] เข้าใจ cosine similarity และ top-k (เขียนเองได้)
- [ ] เก็บและค้นเวกเตอร์ใน Chroma/FAISS ได้
- [ ] ใช้ metadata filtering เป็น และรู้จักตัวเลือก vector DB หลักๆ
- [ ] สร้าง semantic search บนข้อมูลตัวเองที่ค้นได้แม่นพอควร
- [ ] อธิบายความต่าง semantic vs keyword และข้อจำกัดได้

ไปต่อ `04_RAG_พื้นฐาน_Pipeline.md`
