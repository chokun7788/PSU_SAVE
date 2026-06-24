# 08 — ต่อยอด: Agentic RAG, Fine-tuning, GraphRAG (เฟส 7) + โค้ดตัวอย่าง

> เป้าหมายเฟสนี้: หัวข้อขั้นสูงที่ **เลือกทำตามโจทย์จริง ไม่ต้องทำทุกอัน**
> เงื่อนไขก่อนเข้า: RAG พื้นฐาน + advanced + eval ต้องนิ่งแล้ว อย่ากระโดดมาเร็วเกินไป

---

## 8.1 Agentic RAG / AI Agents

### คืออะไร
ยกระดับจาก RAG ที่ "ค้น 1 รอบแล้วตอบ" เป็นระบบที่ LLM **ตัดสินใจเอง** ว่าจะค้นไหม จากแหล่งไหน กี่รอบ ใช้เครื่องมืออะไร

### ต้องรู้อะไรบ้าง + โค้ด

**Tool calling = พื้นฐานของ agent (ให้ LLM เลือกเรียกเครื่องมือเอง)**
```python
tools = [{
    "type": "function",
    "function": {
        "name": "search_kb",
        "description": "ค้นฐานความรู้ภายในบริษัท",
        "parameters": {"type": "object",
                       "properties": {"query": {"type": "string"}},
                       "required": ["query"]},
    },
}]

def agent(question):
    msgs = [{"role": "user", "content": question}]
    r = llm.chat.completions.create(model="gpt-4o-mini", messages=msgs, tools=tools)
    msg = r.choices[0].message
    if msg.tool_calls:                                    # LLM ตัดสินใจว่าจะค้น
        import json
        args = json.loads(msg.tool_calls[0].function.arguments)
        found = retrieve(args["query"], k=4)[0]           # เรียก tool จริง
        msgs += [msg, {"role": "tool",
                       "tool_call_id": msg.tool_calls[0].id,
                       "content": "\n".join(found)}]
        r = llm.chat.completions.create(model="gpt-4o-mini", messages=msgs)  # ตอบจากผล
    return r.choices[0].message.content
```

**LangGraph — agent แบบ graph/stateful (ควบคุม flow ได้)**
```python
# pip install langgraph
# โครงสร้าง: node (ขั้นตอน) + edge (เงื่อนไขไปต่อ) + state (ความจำระหว่างขั้น)
# เหมาะกับ flow ที่มีหลายขั้นและต้องตัดสินใจวนซ้ำ เช่น CRAG (ประเมิน context แล้วค้นใหม่ถ้าไม่พอ)
```

- **ReAct pattern**: วน "คิด → ทำ (เรียก tool) → สังเกตผล → คิดต่อ"
- **Multi-step reasoning & planning**: แตกงานซับซ้อนเป็นขั้น
- **Memory**: ระยะสั้น (ในบทสนทนา) + ระยะยาว (ข้ามครั้ง)
- **Multi-agent**: หลาย agent ทำงานร่วมกัน
- **Framework**: **LangGraph**, LlamaIndex agents, หรือ tool use ของ OpenAI/Anthropic ตรงๆ
- **ความเสี่ยงเพิ่ม**: หลายขั้น = แพง/ช้า/debug ยากขึ้น → observability ยิ่งสำคัญ

### ศึกษายังไง / วิธี
1. เริ่ม tool calling พื้นฐาน (ให้ LLM เรียกฟังก์ชันค้น) ก่อนทำ agent เต็ม
2. ลอง ReAct agent ที่เลือกได้ว่าจะค้น vector DB หรือค้นเว็บ
3. ศึกษา **LangGraph** ถ้าต้องการ flow ควบคุมได้/มี state
4. แหล่งไทย: **codingthailand**, **SkillLane** (AI Agent / tool calling)

---

## 8.2 Fine-tuning

### คืออะไร
"ปรับจูน" โมเดลด้วยข้อมูลเฉพาะทางของเรา ให้เก่งงานเฉพาะหรือรู้สไตล์/รูปแบบที่ต้องการ

> ⚠️ ทำเป็นอันท้ายๆ — **ส่วนใหญ่ RAG + prompt ดีๆ พอแล้ว** fine-tune เหมาะเมื่อต้องการ "สไตล์/รูปแบบเฉพาะ" หรือ "ลด cost ระยะยาว" **ไม่ใช่เพื่อเพิ่มความรู้** (เพิ่มความรู้ใช้ RAG ดีกว่า)

### ต้องรู้อะไรบ้าง
- **เมื่อไรควรอะไร**: ต้องการ "ความรู้ใหม่" → **RAG**; ปรับ "พฤติกรรม/สไตล์/รูปแบบ output" ที่ prompt ไม่พอ → **fine-tune**; ลองสุดทาง → **prompt** ก่อนเสมอ
- **ประเภท**: full fine-tuning (แพง), **LoRA / QLoRA** (ปรับบางส่วน ประหยัด นิยมสุด), instruction tuning
- **Fine-tune embedding model**: ปรับ embedding ให้เข้า domain — มักคุ้มกว่า fine-tune LLM สำหรับงาน RAG (retrieval แม่นขึ้น)
- **ข้อมูลเทรน**: ต้องเตรียม dataset คุณภาพดี (คู่ input-output) — งานหนักอยู่ที่นี่
- **เครื่องมือ**: Hugging Face (transformers, PEFT, TRL), **Unsloth** (เทรน LoRA เร็ว/ประหยัด), บริการ fine-tune ของผู้ให้บริการ API
- **ต้องการ GPU**: รู้เรื่อง VRAM และ quantization

**โครงร่าง fine-tune embedding (ผลตรงกับงาน RAG ที่สุด)**
```python
# pip install sentence-transformers
from sentence_transformers import SentenceTransformer, InputExample, losses
from torch.utils.data import DataLoader

model = SentenceTransformer("intfloat/multilingual-e5-small")
# คู่ (คำถาม, chunk ที่ตอบได้) จากข้อมูล domain ของเรา
examples = [InputExample(texts=["ลาพักร้อนกี่วัน", "พนักงานมีวันลาพักร้อน 10 วัน"])]
loader = DataLoader(examples, batch_size=16, shuffle=True)
loss = losses.MultipleNegativesRankingLoss(model)
model.fit(train_objectives=[(loader, loss)], epochs=1, warmup_steps=10)
```

### ศึกษายังไง / วิธี
1. **อย่าเพิ่งรีบ** — ดันด้วย RAG + prompt + reranker ให้สุดก่อน
2. ถ้าจะทำ เริ่มจาก **fine-tune embedding** (ผลตรงงาน RAG)
3. ศึกษา **LoRA/QLoRA** ผ่าน Hugging Face / Unsloth (มี notebook พร้อมใช้)
4. ปูพื้น DL ก่อน (Andrew Ng / Skooldio) ถ้ายังไม่แน่น

---

## 8.3 GraphRAG / Knowledge Graph

### คืออะไร
RAG ที่ใช้ **knowledge graph** (ข้อมูลเชื่อมโยงเป็นเครือข่าย เช่น "บริษัท A → มี CEO → คน B") เสริม vector search — เก่งคำถามที่ต้อง "เชื่อมโยงหลายจุด" หรือ "เห็นภาพรวมทั้งชุดเอกสาร"

### ต้องรู้อะไรบ้าง
- **ปัญหาที่แก้**: vector RAG ตอบคำถาม "global" ไม่เก่งพอ เช่น "ธีมหลักของเอกสารทั้งชุดคืออะไร" หรือคำถามที่ต้องลากความสัมพันธ์หลายต่อ
- **Entity & Relationship extraction**: ดึง "สิ่งของ" และ "ความสัมพันธ์" มาสร้างกราฟ (มักใช้ LLM ช่วย)
- **Graph database**: Neo4j ฯลฯ
- **Microsoft GraphRAG**: เฟรมเวิร์ก/แนวทางที่รู้จักกว้าง — จุดตั้งต้นที่ดี
- **Hybrid (graph + vector)**: ใช้ร่วมกันมักได้ผลดีสุด
- **ต้นทุน**: สร้างกราฟแพง (ใช้ LLM เยอะตอน index) — คุ้มเฉพาะบางโจทย์

### ศึกษายังไง / วิธี
1. รู้จัก concept และดูว่าโจทย์ "ต้องการการเชื่อมโยง" จริงไหมก่อนลงทุน
2. ศึกษา Microsoft GraphRAG หรือ knowledge graph features ของ LlamaIndex/Neo4j
3. ทำเฉพาะเมื่อ vector RAG + advanced ยังตอบคำถามเชิงเชื่อมโยงไม่ได้

---

## 8.4 Multimodal RAG

### คืออะไร
RAG ที่ค้น/ตอบจากสื่อหลายแบบ — รูป ตาราง ไดอะแกรม เสียง ไม่ใช่แค่ข้อความ

### ต้องรู้อะไรบ้าง
- **Multimodal embedding**: embed รูป+ข้อความในปริภูมิเดียวกัน (เช่น CLIP)
- **Vision LLM**: LLM ที่ "ดูรูปได้" ตอบจากภาพ/ตาราง/แผนภูมิ
- **เอกสารที่มีตาราง/รูปเยอะ**: parse ตารางให้ดี, ทำ caption รูป

### ศึกษายังไง / วิธี
1. ทำเฉพาะถ้าเอกสารมีรูป/ตารางสำคัญต่อคำตอบ
2. เริ่มจาก parse ตารางใน PDF ให้ดีก่อน แล้วค่อยขยับไปภาพ

---

## 8.5 ติดตามความเปลี่ยนแปลงของวงการ

### ต้องรู้/ทำยังไง
- ติดตาม blog ทางการ: Anthropic, OpenAI, Google, Hugging Face, LangChain, LlamaIndex
- ติดตามชุมชนไทย: เพจ/กลุ่ม AI Builders, AI Thailand, ML/Data ชิลชิล ฯลฯ (ไฟล์ `10`)
- อ่าน paper สำคัญผ่าน survey/สรุป (ไม่ต้องอ่าน raw ทุกอัน)
- **อย่าวิ่งตามทุกของใหม่** — เลือกที่ตรงงานจริง ของเก่าที่นิ่งแล้ว (RAG, eval) ยังเป็นพื้นฐานสำคัญเสมอ

---

## ✅ เช็กลิสต์เฟส 7 (เลือกทำตามงาน)

- [ ] ทำ tool calling และ agentic RAG ง่ายๆ ได้ (ถ้างานต้องการตัดสินใจหลายขั้น)
- [ ] เข้าใจว่าเมื่อไรควร RAG / prompt / fine-tune (และทำไม fine-tune มักไม่ใช่คำตอบแรก)
- [ ] รู้จัก GraphRAG/multimodal RAG ระดับ concept และรู้ว่าโจทย์แบบไหนต้องใช้
- [ ] มีนิสัยติดตามวงการอย่างมีวิจารณญาณ

ดูเรื่องเฉพาะภาษาไทยที่ `09_ภาษาไทยโดยเฉพาะ.md` และรวมแหล่งเรียน/โปรเจคที่ `10_แหล่งเรียนและโปรเจค.md`
