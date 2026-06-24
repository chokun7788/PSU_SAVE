# 04 — RAG พื้นฐาน: สร้าง Pipeline ให้ครบ (เฟส 3) + โค้ดตัวอย่าง

> เป้าหมายเฟสนี้: สร้าง RAG ตัวแรกที่รันได้จริง ครบทั้ง pipeline และเข้าใจทุกขั้น
> นี่คือเฟสที่ "ลงมือทำ" — อ่านแล้วต้อง code ตามทุกขั้น

---

## โครงรวม RAG Pipeline (7 ขั้น)

```
[เฟส Indexing — ทำล่วงหน้า]
1. Document Loading   โหลดเอกสารดิบเข้ามา
2. Chunking           แบ่งเอกสารเป็นชิ้นเล็ก         ◄◄ สำคัญสุดอันดับ 1
3. Embedding          แปลงแต่ละชิ้นเป็นเวกเตอร์
4. Indexing/Storing   เก็บลง Vector DB

[เฟส Query — ทุกครั้งที่ถาม]
5. Retrieval          ค้นชิ้นที่เกี่ยวข้องกับคำถาม    ◄◄ สำคัญสุดอันดับ 2
6. Augmentation       ยัด context เข้า prompt
7. Generation         LLM สร้างคำตอบจาก context
```

---

## 3.1 ขั้น 1 — Document Loading

### คืออะไร
นำเอกสารจากแหล่งต่างๆ (ไฟล์ เว็บ DB) เข้ามาเป็นข้อความที่จัดการได้

### ต้องรู้อะไรบ้าง + โค้ด

**โหลด PDF (PDF เป็นตัวร้าย — มีตาราง คอลัมน์ หัว/ท้ายกระดาษ)**
```python
# pip install pypdf
from pypdf import PdfReader

reader = PdfReader("handbook.pdf")
pages = []
for i, page in enumerate(reader.pages):
    text = page.extract_text() or ""
    pages.append({"text": text, "metadata": {"source": "handbook.pdf", "page": i + 1}})
print(pages[0]["text"][:300])   # ตรวจด้วยตา: "อ่านรู้เรื่องไหม?"
```

**ทำความสะอาดข้อความ (ลบช่องว่างเกิน/อักขระขยะ)**
```python
import re
def clean(text: str) -> str:
    text = re.sub(r"\s+", " ", text)      # ยุบช่องว่าง/บรรทัดซ้ำ
    text = text.replace("\x00", "")
    return text.strip()
```

- ชนิดไฟล์ที่ต้องโหลดได้: PDF, docx, TXT, Markdown, HTML, CSV, JSON, ดึงจากเว็บ
- เครื่องมือ: `pypdf`/`PyMuPDF`, **unstructured** (หลายแบบ + แยกโครงสร้าง), **LlamaParse**/**Docling** (เอกสารซับซ้อน), **BeautifulSoup** (เว็บ)
- **OCR** (เอกสารสแกน): Tesseract
- **Metadata**: เก็บ ชื่อไฟล์/เลขหน้า/วันที่ ไว้เสมอ — ใช้ทำ citation + filtering
- **Cleaning**: ลบ header/footer ซ้ำ, ช่องว่างเกิน

### ศึกษายังไง / วิธี
1. เริ่มจากไฟล์ง่าย (TXT/MD) ให้ pipeline เดินได้ก่อน แล้วค่อยไป PDF
2. ลอง document loaders ของ LangChain/LlamaIndex (มี loader เกือบทุกชนิดไฟล์)
3. ทดสอบกับ PDF จริง ดูว่าข้อความ "อ่านรู้เรื่อง" ไหม

> ⚠️ "garbage in, garbage out" เริ่มที่นี่ ถ้าโหลดออกมาเพี้ยน แก้ตรงนี้ก่อนไปต่อ

---

## 3.2 ขั้น 2 — Chunking (สำคัญที่สุด ลงแรงให้เยอะ)

### คืออะไร
แบ่งเอกสารยาวเป็น "ชิ้น" (chunk) เพราะ embedding รับข้อความได้จำกัด และชิ้นที่เล็ก/ตรงประเด็นทำให้ค้นแม่นและประหยัด context

### ต้องรู้อะไรบ้าง + โค้ด

**Recursive splitter (default ที่ดีสำหรับเริ่มต้น — พยายามตัดตามขอบเขตธรรมชาติ)**
```python
# pip install langchain-text-splitters
from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,        # ~500 ตัวอักษร/ชิ้น (ลองปรับ 200-800)
    chunk_overlap=50,      # ซ้อนทับ 50 กันประโยคถูกตัดขาดกลางคัน
    separators=["\n\n", "\n", " ", ""],   # ลองตัดตามย่อหน้า -> บรรทัด -> คำ
)
chunks = splitter.split_text(long_text)
print(f"ได้ {len(chunks)} ชิ้น, ชิ้นแรก: {chunks[0][:100]}")
```

**Markdown — ตัดตามหัวข้อ (รักษาบริบท ได้ผลดี)**
```python
from langchain_text_splitters import MarkdownHeaderTextSplitter
md_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=[("#", "h1"), ("##", "h2"), ("###", "h3")]
)
docs = md_splitter.split_text(markdown_text)   # แต่ละ chunk รู้ว่าอยู่ใต้หัวข้อไหน
```

### ต้องรู้อะไรบ้าง (concept)
- **ทำไม chunk สำคัญสุด**: ใหญ่ไป = ข้อมูลปนเปื้อน/ค้นไม่ตรง; เล็กไป = ขาดบริบท การ chunk ตัดสินว่า retrieval ดึงข้อมูลถูกได้ไหม
- **Chunk size**: เริ่ม ~200–500 token
- **Chunk overlap**: ~10–20% กันประโยคขาด
- **กลยุทธ์ (ง่าย→ดี)**: fixed-size → recursive (default ดี) → sentence-based → document-structure → semantic (ฉลาดสุดแต่แพง — ไฟล์ `05`)
- **ภาษาไทย**: ไม่มีเว้นวรรคระหว่างคำ การตัดตามตัวอักษรดิบอาจตัดกลางคำ ใช้ตัวตัดคำไทย (ไฟล์ `09`)
- **ไม่มีขนาดตายตัวที่ถูกเสมอ** — ต้องทดลอง+วัดผล (เฟส 5)

### ศึกษายังไง / วิธี
1. เริ่ม recursive splitter แล้วทดลองเปลี่ยน size/overlap
2. ดูผลการค้นด้วยตาก่อน แล้ววัดด้วย metric (เฟส 5)
3. **เน้น**: ทดลองหลายขนาด อย่าใช้ default แล้วจบ — ปรับแล้วเห็นผลชัดสุด

> 💡 ระบบตอบไม่ดี 80% อยู่ที่ chunking + retrieval ก่อนโทษ LLM ให้กลับมาดู 2 ขั้นนี้

---

## 3.3 ขั้น 3 — Embedding (ทบทวนจากเฟส 2)
```python
from sentence_transformers import SentenceTransformer
embedder = SentenceTransformer("intfloat/multilingual-e5-small")
vectors = embedder.encode(chunks, batch_size=32)   # batch เพื่อความเร็ว
```
ต้องใช้ embedding model **ตัวเดียวกับตอน query** และจับคู่เวกเตอร์กับ chunk + metadata ให้ครบ

---

## 3.4 ขั้น 4 — Indexing / Storing
```python
import chromadb
client = chromadb.PersistentClient(path="./db")
col = client.get_or_create_collection("kb")
col.add(
    ids=[f"c{i}" for i in range(len(chunks))],
    embeddings=embedder.encode(chunks).tolist(),
    documents=chunks,
    metadatas=[{"source": "handbook.pdf"} for _ in chunks],
)
```
- โครงสร้าง: `{vector, text ต้นฉบับ, metadata}`
- เลือก distance metric (cosine มัก default ดี)
- **Persistence**: เก็บลงดิสก์/server ไม่ให้หาย
- **อัปเดต index**: วางแผนตั้งแต่ต้น (ทั้งก้อน vs เฉพาะที่เปลี่ยน)

---

## 3.5 ขั้น 5 — Retrieval (สำคัญอันดับ 2)

### คืออะไร
รับคำถาม → embed → ค้น top-k chunk ที่ใกล้สุด มาเป็น context

### ต้องรู้อะไรบ้าง + โค้ด
```python
def retrieve(question: str, k: int = 4):
    qv = embedder.encode([question]).tolist()
    res = col.query(query_embeddings=qv, n_results=k)
    chunks_found = res["documents"][0]
    metas = res["metadatas"][0]
    dists = res["distances"][0]
    # ตรวจด้วยตาเสมอ: chunk ที่ได้ "เกี่ยวกับคำถามจริงไหม?"
    for c, d in zip(chunks_found, dists):
        print(f"[dist={d:.3f}] {c[:80]}")
    return chunks_found, metas
```
- embed คำถามด้วย model **ตัวเดียวกับตอน index**
- **เลือก k**: น้อยไป=ข้อมูลไม่พอ, มากไป=ยาว/เปลือง/มี noise — เริ่ม k=3–5
- **Similarity threshold**: ถ้าไม่มี chunk ใกล้พอ → ตอบ "ไม่มีข้อมูล" (กันมั่ว)
- **Metadata filtering ตอนค้น**: เช่นเฉพาะแผนก/ปีนั้น
- ปัญหาที่พบบ่อย: ค้นได้ chunk "คล้ายผิวเผิน" แต่ไม่ตอบโจทย์ → แก้ด้วยเทคนิคเฟส 4 (hybrid/rerank)

### ศึกษายังไง / วิธี
1. ค้น top-k แล้ว **print chunk ออกมาดูด้วยตาทุกครั้ง**
2. ทดลองปรับ k และ threshold
3. **เน้น**: ก่อนใส่ LLM ตอบ ต้องมั่นใจว่า retrieval ดึงข้อมูลถูกมาได้ก่อน

---

## 3.6 ขั้น 6 — Augmentation (ประกอบ Prompt)

### คืออะไร
เอา chunk ที่ค้นได้มา "ยัด" เข้า prompt พร้อมคำถาม — ตัว "A" ใน RAG

### ต้องรู้อะไรบ้าง + โค้ด
```python
def build_prompt(question, chunks, metas):
    context = "\n\n".join(
        f"[{i+1}] (ที่มา: {m.get('source')}) {c}"
        for i, (c, m) in enumerate(zip(chunks, metas))
    )
    system = (
        "ตอบจาก <context> เท่านั้น ห้ามใช้ความรู้ภายนอก "
        "ถ้าไม่มีข้อมูลให้ตอบว่า 'ไม่พบข้อมูลนี้ในเอกสาร' "
        "และอ้างอิงหมายเลขแหล่ง [n] ท้ายประโยค"
    )
    user = f"<context>\n{context}\n</context>\n\nคำถาม: {question}"
    return system, user
```
- โครงสร้าง prompt RAG: system (บทบาท+กติกา) / context (chunk คั่นด้วยแท็ก) / user (คำถาม)
- **กัน hallucination**: สั่งชัดให้ตอบเฉพาะจาก context และยอมรับเมื่อไม่รู้
- **Citation**: ใส่หมายเลข/ชื่อแหล่งใน context ให้ LLM อ้างอิง
- **ระวัง context window**: chunk + คำถาม + คำสั่ง ต้องไม่เกิน
- **"lost in the middle"**: LLM สนใจต้น/ท้าย context มากกว่ากลาง — จัดอันเกี่ยวสุดไว้ตำแหน่งเด่น

### ศึกษายังไง / วิธี
1. ทดลองปรับถ้อยคำกติกาใน system prompt
2. ทดสอบ "ถามเรื่องที่ไม่มีในเอกสาร" — ระบบควรตอบว่าไม่รู้ ไม่ใช่มั่ว

---

## 3.7 ขั้น 7 — Generation
```python
from openai import OpenAI
llm = OpenAI()
def generate(system, user):
    r = llm.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": system},
                  {"role": "user", "content": user}],
        temperature=0,    # ต่ำ เพื่อยึดข้อมูล ไม่แต่งเติม
    )
    return r.choices[0].message.content
```

### 🎯 รวมเป็น RAG เต็มฟังก์ชัน
```python
def rag(question: str) -> str:
    chunks, metas = retrieve(question, k=4)
    system, user = build_prompt(question, chunks, metas)
    return generate(system, user)

print(rag("ลาพักร้อนได้กี่วัน?"))   # ตอบพร้อมอ้างอิง [n]
```

ต้องรู้: เลือก LLM ให้เหมาะ (งานตอบจากเอกสารมักไม่ต้องโมเดลแพงสุด), temperature ต่ำ, streaming เพื่อ UX, **แสดง citation**, ตรวจว่าคำตอบยึด context จริง (faithfulness — เฟส 5)

---

## 3.8 Framework: LangChain vs LlamaIndex

### คืออะไร
เครื่องมือที่ห่อทุกขั้นข้างบนไว้ให้

**LlamaIndex — RAG ครบใน ~10 บรรทัด (เน้นงานเอกสาร)**
```python
# pip install llama-index llama-index-embeddings-huggingface
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

Settings.embed_model = HuggingFaceEmbedding("intfloat/multilingual-e5-small")
docs = SimpleDirectoryReader("./data").load_data()      # โหลดทุกไฟล์ในโฟลเดอร์
index = VectorStoreIndex.from_documents(docs)            # chunk+embed+index ให้หมด
engine = index.as_query_engine(similarity_top_k=4)
print(engine.query("ลาพักร้อนได้กี่วัน?"))
```

**LangChain — ยืดหยุ่น สร้าง app/agent กว้างกว่า**
```python
# pip install langchain langchain-openai langchain-community langchain-chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

docs = PyPDFLoader("handbook.pdf").load()
splits = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50).split_documents(docs)
emb = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-small")
vs = Chroma.from_documents(splits, emb)
retriever = vs.as_retriever(search_kwargs={"k": 4})

prompt = ChatPromptTemplate.from_template(
    "ตอบจาก context เท่านั้น ถ้าไม่มีให้บอกว่าไม่ทราบ\n\ncontext:\n{context}\n\nคำถาม: {question}"
)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

def rag_lc(q):
    ctx = "\n\n".join(d.page_content for d in retriever.invoke(q))
    return llm.invoke(prompt.format(context=ctx, question=q)).content
```

### ต้องรู้อะไรบ้าง
- **LangChain**: ครอบจักรวาล (app/agent) ชุมชนใหญ่สุด มี Python + JS — core: chat models, prompt templates, retrievers, chains, memory, tool calling
- **LlamaIndex**: เน้น RAG/data framework โดยเฉพาะ สะดวกสำหรับงานเอกสาร
- **เลือกตัวไหน**: concept เหมือนกัน 90% — RAG ล้วน → LlamaIndex สะดวก; agent/ระบบกว้าง → LangChain
- **ควรลองเขียน RAG แบบ "ไม่ใช้ framework" สัก 1 ครั้ง** (เหมือน 3.1–3.7) เพื่อเข้าใจข้างใน แล้วค่อยใช้ framework

### ศึกษายังไง / วิธี
1. ทำ RAG ครั้งแรกแบบ **manual** (3.1–3.7) → แล้วทำซ้ำด้วย **framework**
2. แหล่งไทย: **Appsynth** (Llama3.1+LangChain+RAG+FAISS), **codingthailand** (LangChain.js+RAG+Next.js), **SkillLane** (LLM+Python LangChain)
3. ทำ official RAG tutorial ของ framework ที่เลือก

---

## ✅ เช็กลิสต์ก่อนขึ้นเฟส 4

- [ ] โหลดเอกสาร (รวม PDF) เป็นข้อความที่อ่านรู้เรื่อง + เก็บ metadata
- [ ] chunk ด้วย recursive splitter และเข้าใจผลของ size/overlap
- [ ] embed + เก็บลง vector DB
- [ ] retrieve top-k แล้วตรวจด้วยตาว่า chunk เกี่ยวข้องจริง
- [ ] เขียน prompt RAG ที่ยึด context และยอมรับเมื่อไม่รู้
- [ ] ได้คำตอบพร้อม citation จากเอกสารจริง
- [ ] เคยเขียน RAG แบบ manual 1 ครั้ง และแบบ framework 1 ครั้ง
- [ ] **มีบอทตอบคำถามจากเอกสารของตัวเองที่รันได้จริง** ← ผลงานสำคัญของเฟสนี้

ไปต่อ `05_Advanced_RAG.md`
