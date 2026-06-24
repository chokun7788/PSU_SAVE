# 05 — Advanced RAG (เฟส 4) + โค้ดตัวอย่าง

> เป้าหมายเฟสนี้: ยกระดับจาก RAG "พอใช้" เป็น RAG "ใช้งานจริงได้ดี" — จุดที่แยกมือใหม่จากมืออาชีพ
> หลักการ: ปัญหา RAG เกือบทั้งหมดอยู่ที่ **retrieval ดึงข้อมูลมาผิด/ไม่ครบ** ไม่ใช่ที่ LLM

---

## ภาพรวมจุดที่ปรับได้ (เรียงตามคุ้มค่า)

```
ก่อนค้น (Pre-retrieval):   ปรับ chunking, ปรับคำถาม (query transformation)
ตอนค้น (Retrieval):        hybrid search, metadata filtering, ปรับ k
หลังค้น (Post-retrieval):  reranking, compression, จัดลำดับ context
```
ลำดับที่แนะนำให้ลองก่อน (ได้ผลชัด): **Reranking → Hybrid search → Query transformation → Chunking ขั้นสูง**

---

## 4.1 Chunking ขั้นสูง

### คืออะไร
กลยุทธ์แบ่งเอกสารที่ฉลาดกว่าตัดตายตัว เพื่อ chunk มีบริบทครบและค้นแม่นขึ้น

### ต้องรู้อะไรบ้าง / มีวิธีอะไร + โค้ด

**Parent-child / Small-to-big (ค้นด้วยชิ้นเล็ก ส่งชิ้นใหญ่ให้ LLM — ยอดนิยม ได้ผลดี)**
```python
# LangChain ParentDocumentRetriever
from langchain.retrievers import ParentDocumentRetriever
from langchain.storage import InMemoryStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

child_splitter  = RecursiveCharacterTextSplitter(chunk_size=200)   # เล็ก = match แม่น
parent_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)  # ใหญ่ = บริบทครบ
retriever = ParentDocumentRetriever(
    vectorstore=Chroma(embedding_function=emb),
    docstore=InMemoryStore(),
    child_splitter=child_splitter,
    parent_splitter=parent_splitter,
)
retriever.add_documents(docs)   # ค้นเจอชิ้นเล็ก แต่คืนชิ้นใหญ่ที่มีบริบท
```

**Semantic chunking (ตัดตรงจุดที่ความหมายเปลี่ยน)**
```python
# pip install langchain-experimental
from langchain_experimental.text_splitter import SemanticChunker
splitter = SemanticChunker(emb, breakpoint_threshold_type="percentile")
chunks = splitter.split_text(long_text)
```

- **Sentence-window**: index ทีละประโยค แต่ตอนส่งขยายเอาประโยคข้างเคียง
- **Hierarchical / Auto-merging**: เก็บหลายระดับ รวมอัตโนมัติเมื่อหลายชิ้นย่อยถูกค้นพร้อมกัน
- **Document-specific**: โค้ดตัดตามฟังก์ชัน, ตารางเก็บทั้งตาราง, Markdown ตามหัวข้อ
- **Metadata enrichment**: เติมสรุป/keyword ให้ chunk ช่วยค้น

### ศึกษายังไง / วิธี
1. ลอง parent-child / sentence-window ใน LlamaIndex/LangChain (มี retriever สำเร็จ)
2. เทียบผลแต่ละแบบด้วย metric เฟส 5 — อย่าเดา ให้วัด
3. **เน้น**: parent-child / small-to-big คุ้มลองมากกับเอกสารยาว

---

## 4.2 Hybrid Search

### คืออะไร
ผสม **semantic** (เวกเตอร์ จับความหมาย) + **keyword** (BM25 จับคำตรงเป๊ะ) แล้วรวมผล

### ต้องรู้อะไรบ้าง + โค้ด
```python
# pip install rank-bm25 langchain-community
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever

bm25 = BM25Retriever.from_documents(splits); bm25.k = 5
vector = vs.as_retriever(search_kwargs={"k": 5})
hybrid = EnsembleRetriever(retrievers=[bm25, vector], weights=[0.4, 0.6])  # ปรับน้ำหนักได้
results = hybrid.invoke("รหัสสินค้า SKU-2024 ราคาเท่าไร")  # คำเฉพาะ -> BM25 ช่วยจับ
```

- **ทำไมต้อง hybrid**: semantic อาจพลาดคำเฉพาะ/ชื่อรุ่น/รหัส/ศัพท์เทคนิคที่ต้องตรงเป๊ะ; keyword ไม่เข้าใจความหมาย — รวมกันได้จุดแข็งทั้งคู่
- **BM25 / sparse retrieval**: อัลกอริทึมค้นคีย์เวิร์ดมาตรฐาน
- **การรวมผล**: Reciprocal Rank Fusion (RRF) หรือถ่วงน้ำหนัก
- vector DB หลายตัว (Qdrant, Weaviate) รองรับ hybrid ในตัว

### ศึกษายังไง / วิธี
1. เพิ่ม BM25 คู่ vector แล้วรวมผล (EnsembleRetriever / QueryFusionRetriever)
2. ทดสอบกับคำถามที่มีคำเฉพาะ/ชื่อรุ่น
3. **เน้น**: ภาษาไทย + งานที่มีศัพท์เฉพาะ/รหัส มักได้ประโยชน์จาก hybrid มาก (ไฟล์ `09`)

---

## 4.3 Reranking

### คืออะไร
ขั้นหลังค้น: ดึงเกินจำเป็น (เช่น top-20) แล้วใช้โมเดลแม่นกว่า (cross-encoder/reranker) จัดอันดับใหม่ เลือก top-3–5 ที่ดีจริงส่ง LLM

### ต้องรู้อะไรบ้าง + โค้ด
```python
# pip install sentence-transformers
from sentence_transformers import CrossEncoder
reranker = CrossEncoder("BAAI/bge-reranker-v2-m3")   # รองรับ multilingual/ไทย

def retrieve_rerank(question, k_first=20, k_final=4):
    qv = embedder.encode([question]).tolist()
    cand = col.query(query_embeddings=qv, n_results=k_first)["documents"][0]  # ค้นกว้าง
    pairs = [[question, c] for c in cand]
    scores = reranker.predict(pairs)                                          # ให้คะแนนใหม่
    ranked = [c for _, c in sorted(zip(scores, cand), reverse=True)]
    return ranked[:k_final]                                                   # เอาที่ดีจริง
```

- **Bi-encoder vs Cross-encoder**: embedding (bi) เร็วแต่หยาบ เหมาะค้นกว้าง; cross-encoder ดูคำถาม+เอกสารพร้อมกัน แม่นกว่ามากแต่ช้า เหมาะ rerank จำนวนน้อย
- **โมเดล**: Cohere Rerank (API), **BGE-reranker**, **Jina reranker** (open-source) — เลือกที่รองรับไทย
- **two-stage retrieval**: ค้นกว้างด้วย vector → กรองแคบด้วย reranker = แม่นขึ้นชัด

### ศึกษายังไง / วิธี
1. เพิ่ม reranker หลัง retrieval (top-20 → rerank → top-5)
2. วัด context precision ก่อน/หลัง (เฟส 5)
3. **เน้น**: ถ้าปรับได้แค่อย่างเดียว เริ่มที่ reranking (คุ้มสุด)

---

## 4.4 Query Transformation / Expansion

### คืออะไร
ปรับ "คำถาม" ก่อนค้น เพราะคำถามดิบมักสั้น กำกวม หรือใช้คำไม่ตรงกับในเอกสาร

### ต้องรู้อะไรบ้าง / มีวิธีอะไร + โค้ด

**Multi-query (สร้างหลายเวอร์ชันแล้วค้นทุกอันรวมผล)**
```python
def multi_query(question, n=3):
    prompt = f"เขียนคำถามนี้ใหม่ {n} แบบที่ความหมายเดียวกันแต่ใช้คำต่างกัน อย่างละบรรทัด:\n{question}"
    variants = llm.chat.completions.create(
        model="gpt-4o-mini", messages=[{"role":"user","content":prompt}]
    ).choices[0].message.content.splitlines()
    seen = {}
    for q in [question] + variants:
        for c in retrieve(q, k=4)[0]:
            seen[c] = True          # รวมผล + ตัดซ้ำ
    return list(seen)
```

**HyDE (แต่งคำตอบสมมติก่อนแล้วเอาไปค้น — คำตอบมักใกล้เอกสารกว่าคำถาม)**
```python
def hyde(question):
    hypo = llm.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":f"เขียนย่อหน้าคำตอบสมมติของ: {question}"}]
    ).choices[0].message.content
    return retrieve(hypo, k=4)[0]   # ค้นด้วย "คำตอบสมมติ" แทนคำถาม
```

- **Query rewriting**: LLM เขียนคำถามใหม่ให้ชัด/ตรงคำในเอกสาร
- **Step-back prompting**: ถอยถามกว้างกว่าเพื่อดึงบริบทพื้นฐาน
- **Query decomposition**: แตกคำถามซับซ้อนเป็นย่อยหลายอัน (สำคัญกับ "เปรียบเทียบ A กับ B")
- **Routing**: เลือกแหล่ง/index ที่เหมาะกับคำถาม

### ศึกษายังไง / วิธี
1. เริ่ม multi-query (ง่าย เห็นผล) แล้วลอง HyDE
2. ลอง decomposition กับคำถามที่ระบบเดิมตอบไม่ได้
3. **เน้น**: decomposition สำคัญมากกับ "เปรียบเทียบ" หรือ "สรุปหลายแง่มุม"

---

## 4.5 Context Post-processing

### คืออะไร
จัดการ context ที่ค้นได้ก่อนส่ง LLM ให้กระชับและเรียงดี

### ต้องรู้อะไรบ้าง + โค้ด
```python
# จัดลำดับแก้ "lost in the middle": เอาชิ้นเกี่ยวสุดไว้หัวและท้าย
def reorder(chunks):
    reordered = []
    for i, c in enumerate(chunks):
        reordered.insert(0, c) if i % 2 == 0 else reordered.append(c)
    return reordered
```
- **Contextual compression**: ตัดส่วนไม่เกี่ยวออกจาก chunk ก่อนส่ง (ประหยัด token ลด noise)
- **Deduplication**: ลบ chunk ซ้ำ/คล้ายมาก
- **Reordering ("lost in the middle")**: เอาชิ้นสำคัญไว้หัว/ท้าย
- **Context window budget**: คุมจำนวน chunk ไม่ให้ยาวเกินจน LLM งง/แพง

### ศึกษายังไง / วิธี
1. ลอง contextual compression retriever
2. ทดลองสลับลำดับ chunk ดูผล

---

## 4.6 รูปแบบ RAG ขั้นสูง (รู้จักไว้)

### ต้องรู้อะไรบ้าง
- **Multi-hop / Iterative retrieval**: ค้นหลายรอบ ใช้ผลรอบแรกตั้งคำถามรอบต่อไป
- **Self-RAG / Corrective RAG (CRAG)**: ระบบ "ประเมินตัวเอง" ว่า context พอ/ถูกไหม ถ้าไม่พอค้นใหม่/ไปหาเว็บ
- **Agentic RAG**: LLM ตัดสินใจเองว่าจะค้นไหม จากไหน กี่รอบ (ไฟล์ `08`)
- **Multimodal RAG**: ค้น/ตอบจากรูป ตาราง เสียง
- **GraphRAG**: ใช้ knowledge graph เสริม (ไฟล์ `08`)

### ศึกษายังไง / วิธี
1. รู้จัก concept ก่อน ยังไม่ต้องทำทุกอัน
2. ทำเฉพาะแบบที่ตรงกับโจทย์จริง
3. อ่าน survey "Advanced RAG techniques" เพื่อเห็นภาพรวม

---

## ✅ เช็กลิสต์ก่อนขึ้นเฟส 5

- [ ] เพิ่ม reranking และวัดได้ว่าคุณภาพดีขึ้น
- [ ] ทำ hybrid search (semantic + BM25) เป็น
- [ ] ลอง query transformation อย่างน้อย 2 แบบ (multi-query, HyDE)
- [ ] ลอง chunking ขั้นสูง (parent-child หรือ sentence-window)
- [ ] เข้าใจ "lost in the middle" และจัดลำดับ context เป็น
- [ ] รู้จักรูปแบบ RAG ขั้นสูง (multi-hop, CRAG, agentic, graph) ระดับ concept

> ⚠️ ทุกการปรับในเฟสนี้ **ต้องวัดผล** ไม่งั้นไม่รู้ว่าดีขึ้นจริงหรือแค่รู้สึก → `06_Evaluation.md`
