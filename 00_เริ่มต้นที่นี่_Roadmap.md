# 📍 เริ่มต้นที่นี่ — Roadmap การเรียน RAG / LLM ตั้งแต่ศูนย์ (ฉบับละเอียด + โค้ดตัวอย่าง)

> ไฟล์นี้คือ "แผนที่" ของทั้งชุด อ่านไฟล์นี้ให้จบก่อน แล้วค่อยไล่อ่านไฟล์ที่ 01–10 ตามลำดับ
> ทุกไฟล์ในชุดนี้มี **โค้ดตัวอย่างจริงที่รันได้** ประกอบทุกหัวข้อ

---

## ชุดไฟล์ทั้งหมดในคู่มือนี้

   | ไฟล์ | หัวข้อ | เฟส | ใช้เวลาโดยประมาณ |
   |------|--------|-----|------------------|
   | `00` | เริ่มต้นที่นี่ + Roadmap + วิธีเรียน (ไฟล์นี้) | — | อ่าน 30 นาที |
   | `01` | พื้นฐานที่ต้องมีก่อน (Python, API, เครื่องมือ, คณิต) | เฟส 0 | 2–6 สัปดาห์ |
   | `02` | LLM พื้นฐาน (token, prompt, เรียก API, local model) | เฟส 1 | 1–2 สัปดาห์ |
   | `03` | Embeddings และ Vector Database | เฟส 2 | 1–2 สัปดาห์ |
   | `04` | RAG พื้นฐาน — สร้าง pipeline ให้ครบ | เฟส 3 | 2–3 สัปดาห์ |
   | `05` | Advanced RAG (chunking, hybrid, rerank, query transform) | เฟส 4 | 3–4 สัปดาห์ |
   | `06` | Evaluation — วัดผลให้เป็น | เฟส 5 | 1–2 สัปดาห์ |
   | `07` | Production — นำขึ้นใช้งานจริง | เฟส 6 | 2–4 สัปดาห์ |
   | `08` | ต่อยอด — Agentic RAG, Fine-tuning, GraphRAG | เฟส 7 | ตามงาน |
   | `09` | RAG ภาษาไทยโดยเฉพาะ (จุดที่ต้องระวังเป็นพิเศษ) | เสริม | 1 สัปดาห์ |
   | `10` | รวมแหล่งเรียน + โปรเจคแต่ละเฟส + คำศัพท์ | อ้างอิง | ใช้ตลอดทาง |

ตัวเลขเวลาเป็นแค่ประมาณการถ้าเรียนแบบมีงานประจำ (วันละ 1–2 ชม.) ถ้าเรียนเต็มเวลาจะเร็วกว่านี้มาก

---

## ภาพรวม RAG pipeline (สิ่งที่คุณจะสร้างได้)

RAG (Retrieval-Augmented Generation) คือเทคนิคให้ LLM ตอบคำถามโดยอ้างอิง "ข้อมูลของเราเอง" แทนที่จะตอบจากความจำที่อาจเก่าหรือมั่ว มันมี **2 เฟส**

```
เฟส 1: Indexing (เตรียมข้อมูลล่วงหน้า — ทำครั้งเดียว/อัปเดตเป็นรอบ)
  เอกสาร ──► แบ่งเป็นชิ้น (Chunking) ──► แปลงเป็นเวกเตอร์ (Embedding) ──► เก็บลง Vector DB

เฟส 2: Retrieval + Generation (ทำทุกครั้งที่มีคำถาม)
  คำถาม ──► ค้นชิ้นที่เกี่ยวข้อง (Retrieval) ──► ยัด context เข้า Prompt ──► LLM สร้างคำตอบ ──► คำตอบที่อ้างอิงข้อมูลจริง
```

**จุดที่สำคัญที่สุด** (ลงแรงที่นี่ก่อนเสมอ): `Chunking` และ `Retrieval` — สองอันนี้ตัดสิน ~80% ของคุณภาพคำตอบ ถ้าค้นข้อมูลผิด ต่อให้ LLM เก่งแค่ไหนก็ตอบมั่ว หลักการคือ **garbage in, garbage out**

---

## 🚀 ดูปลายทางก่อน: RAG ขั้นต่ำที่รันได้จริง (~40 บรรทัด)

โค้ดนี้คือ "RAG ทั้งระบบแบบย่อสุด" — ตอนนี้ยังไม่ต้องเข้าใจทุกบรรทัด แค่ดูภาพรวมว่าปลายทางหน้าตาเป็นยังไง พอจบเฟส 3 คุณจะเขียนแบบนี้ได้เองและเข้าใจทุกบรรทัด

```python
# pip install chromadb sentence-transformers openai
import chromadb
from sentence_transformers import SentenceTransformer
from openai import OpenAI

# ---------- เฟส Indexing (ทำครั้งเดียว) ----------
embedder = SentenceTransformer("intfloat/multilingual-e5-small")  # รองรับไทย
client = chromadb.Client()
col = client.create_collection("docs")

documents = [
    "บริษัทเปิดทำการ จันทร์-ศุกร์ เวลา 9.00-18.00 น.",
    "วันลาพักร้อนพนักงานมี 10 วันต่อปี สะสมข้ามปีได้ไม่เกิน 5 วัน",
    "การเบิกค่าเดินทางต้องแนบใบเสร็จและอนุมัติจากหัวหน้าก่อน",
]
# 1) chunk (ที่นี่สั้นอยู่แล้ว) 2) embed 3) เก็บลง vector DB
col.add(
    ids=[f"doc{i}" for i in range(len(documents))],
    embeddings=embedder.encode(documents).tolist(),
    documents=documents,
)

# ---------- เฟส Query (ทุกครั้งที่ถาม) ----------
def ask(question: str) -> str:
    # 4) retrieve: ค้น chunk ที่เกี่ยวข้องที่สุด
    q_vec = embedder.encode([question]).tolist()
    hits = col.query(query_embeddings=q_vec, n_results=2)
    context = "\n".join(hits["documents"][0])

    # 5) augment: ยัด context เข้า prompt + สั่งให้ตอบจาก context เท่านั้น
    prompt = f"ตอบจากข้อมูลที่ให้เท่านั้น ถ้าไม่มีให้บอกว่าไม่ทราบ\n\nข้อมูล:\n{context}\n\nคำถาม: {question}"

    # 6) generate: ให้ LLM สร้างคำตอบ
    llm = OpenAI()
    resp = llm.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )
    return resp.choices[0].message.content

print(ask("ลาพักร้อนได้กี่วัน?"))
# -> ตอบโดยอ้างอิงเอกสารข้อ 2 ไม่ใช่เดาเอง
```

ทั้งหมดนี้คือ RAG: **embed → เก็บ → ค้น → ยัด context → ตอบ** ที่เหลือในคู่มือคือการทำแต่ละขั้นให้ดีและเชื่อถือได้จริง

---

## 🧰 Tech Stack ที่จะได้ใช้ (cheat sheet)

| งาน | ตัวเลือกเริ่มต้น (ง่าย) | ตัวเลือก production |
|-----|----------------------|---------------------|
| ภาษา | Python 3.10+ | เดิม |
| เรียก LLM | `openai` / `anthropic` / Ollama (ฟรี) | เดิม + model routing |
| Embedding | `sentence-transformers` (ฟรี, local) | API embedding / โมเดล fine-tuned |
| Vector DB | **Chroma** / FAISS (local) | Qdrant / Weaviate / pgvector / Pinecone |
| Framework | LlamaIndex หรือ LangChain | เดิม / LangGraph (agent) |
| Reranker | BGE-reranker (local) | Cohere Rerank API |
| Evaluation | **RAGAS** | RAGAS + Langfuse/LangSmith |
| ภาษาไทย | **PyThaiNLP** + multilingual-e5 / BGE-M3 | + Typhoon |
| Backend | FastAPI | FastAPI + Docker + cloud |
| UI ทดลอง | Streamlit / Gradio | Next.js / React |
| Observability | — | Langfuse / LangSmith |

---

## เส้นทางการเรียน 7 เฟส (สรุปย่อ)

```
เฟส 0  พื้นฐาน           Python + API + คณิตเบาๆ          ◄── ห้ามข้าม แต่ไม่ต้องเพอร์เฟกต์
   │
เฟส 1  LLM               เรียก API เป็น + prompt + เข้าใจขีดจำกัด
   │
เฟส 2  Embeddings        เข้าใจ semantic search + vector DB   ◄── หัวใจที่ทำให้ RAG เป็นไปได้
   │
เฟส 3  RAG พื้นฐาน        สร้าง pipeline ครบทั้ง 7 ขั้น        ◄── ลงมือทำตัวแรก
   │
เฟส 4  Advanced RAG      chunking ขั้นสูง, hybrid, rerank     ◄── แยกมือใหม่จากมืออาชีพ
   │
เฟส 5  Evaluation        RAGAS + metrics                     ◄── คนข้ามมากสุด พังเพราะมันมากสุด
   │
เฟส 6  Production        deploy, monitor, cost, security
   │
เฟส 7  ต่อยอด            Agentic RAG, fine-tune, GraphRAG     ◄── เลือกตามงาน
```

---

## วิธีเรียนให้ได้ผลจริง (อ่านส่วนนี้ให้ดี สำคัญพอๆ กับเนื้อหา)

### หลัก 5 ข้อ

1. **เรียนแบบทำโปรเจค ไม่ใช่แบบดูคลิปรวด**
   ทุกเฟสต้องจบด้วย "ของที่รันได้จริง" เช่น จบเฟส 3 ต้องมีบอทตอบคำถามจาก PDF ของตัวเองได้ ความรู้ที่ไม่ได้ลงมือทำจะหายภายใน 1 สัปดาห์

2. **อย่าติดกับดักทฤษฎี (Tutorial Hell)**
   อาการคือดูคอร์สแล้วคอร์สเล่า แต่ไม่เคยสร้างอะไรเอง วิธีแก้: ดูแค่พอเข้าใจ concept แล้วรีบลงมือ พอติดค่อยกลับไปดูเฉพาะจุดที่ติด

3. **ไม่ต้องเข้าใจทุกอย่างก่อนเริ่ม**
   คุณไม่จำเป็นต้องเข้าใจคณิตของ transformer ก่อนสร้าง RAG เหมือนขับรถเป็นได้โดยไม่ต้องรู้กลไกเครื่องยนต์ ปูพอใช้งานก่อน เจาะลึกทีหลังเฉพาะส่วนที่จำเป็น

4. **เรียน "พอ" แล้วไปต่อ — กลับมาวนซ้ำได้**
   การเรียนแบบนี้เป็น **วงกลม ไม่ใช่เส้นตรง** รอบแรกอ่านเอา concept พอทำโปรเจคจริงจะเจอคำถาม แล้วค่อยกลับมาอ่านซ้ำให้ลึกขึ้น ปกติมาก

5. **เก็บโน้ตของตัวเอง**
   เขียนสรุปด้วยภาษาตัวเองหลังเรียนแต่ละหัวข้อ ถ้าอธิบายให้คนอื่นเข้าใจไม่ได้ = ยังไม่เข้าใจจริง (Feynman Technique)

### เทคนิคการศึกษาแต่ละแบบ (ใช้ผสมกัน)

- **อ่าน/ดู เพื่อเอา concept** — บล็อกไทย, YouTube, คอร์ส (ดูไฟล์ `10`)
- **อ่าน docs อย่างเป็นทางการ** — LangChain / LlamaIndex / OpenAI / Anthropic docs คือแหล่งที่แม่นและอัปเดตที่สุด ฝึกอ่าน docs ให้คล่องตั้งแต่เนิ่นๆ
- **ลงมือ code ตาม (follow-along)** — พิมพ์เองทุกตัว อย่า copy-paste ล้วน
- **ดัดแปลง (modify)** — เอาตัวอย่างมาเปลี่ยนให้เป็นข้อมูล/โจทย์ของตัวเอง นี่คือจุดที่เรียนรู้จริง
- **สร้างจากศูนย์ (build from scratch)** — ปิด tutorial แล้วสร้างเองให้ได้ ถ้าทำได้ = ผ่านหัวข้อนั้น
- **ถาม AI เป็นติวเตอร์** — ใช้ Claude/ChatGPT อธิบาย concept ที่งง, review code, หรือถาม "ทำไมโค้ดนี้ error" แต่อย่าให้มันเขียนให้ทั้งหมดตั้งแต่ยังไม่เข้าใจ

### สัญญาณว่า "ผ่าน" แต่ละเฟสแล้ว

- เฟส 1: เรียก LLM API เขียนโปรแกรมสั้นๆ ได้เองโดยไม่ต้องลอกตัวอย่าง
- เฟส 2: อธิบายให้เพื่อนฟังได้ว่า "semantic search ต่างจากค้นคีย์เวิร์ดยังไง"
- เฟส 3: มีบอทตอบคำถามจากเอกสารตัวเองที่รันได้
- เฟส 4: ปรับ retrieval แล้ววัดได้ว่าดีขึ้นจริง
- เฟส 5: มีตัวเลข metric บอกได้ว่าระบบดีแค่ไหน ไม่ใช่แค่ "รู้สึกว่าดี"
- เฟส 6: deploy ให้คนอื่นใช้ได้จริง

---

## ก่อนเริ่ม: เตรียมเครื่องมือพื้นฐาน

```bash
# 1) ติดตั้ง Python 3.10+ แล้วสร้าง virtual environment ต่อโปรเจค
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2) เก็บ API key ใน .env (อย่า hardcode ใน code, อย่า push ขึ้น git)
echo "OPENAI_API_KEY=sk-xxxx" >> .env
echo ".env" >> .gitignore        # สำคัญมาก!

# 3) ติดตั้ง package พื้นฐานที่จะใช้
pip install python-dotenv openai chromadb sentence-transformers
```

```python
# โหลด .env ใน Python
from dotenv import load_dotenv
load_dotenv()   # ดึงค่าจาก .env เข้า environment variable อัตโนมัติ
```

- **บัญชี + API key**: เริ่มจากอันใดอันหนึ่งก็ได้ (Anthropic Claude / OpenAI / Google Gemini) หรือใช้ฟรีด้วย Ollama รันบนเครื่องตัวเอง (รายละเอียดในไฟล์ `02`)
- **Google Colab** (ฟรี) ถ้าเครื่องไม่แรงพอ — รัน Python บน cloud ได้เลย

> ⚠️ เรื่อง cost: การเรียก LLM API มีค่าใช้จ่ายตาม token ตอนเรียนให้ตั้ง budget limit ไว้กันพลาด หรือใช้ Ollama (ฟรี) ฝึกก่อน

---

ไปต่อที่ไฟล์ `01_พื้นฐานก่อนเริ่ม.md`
