# 02 — LLM พื้นฐาน (เฟส 1) + โค้ดตัวอย่าง

> เป้าหมายเฟสนี้: เรียกใช้ LLM เป็น, เขียน prompt เป็น, และ **เข้าใจขีดจำกัดของมัน** (ซึ่งเป็นเหตุผลที่ RAG มีอยู่)

---

## 1.1 LLM คืออะไร และทำงานยังไง (ระดับ concept)

### คืออะไร
**LLM (Large Language Model)** คือโมเดล AI ที่เทรนด้วยข้อความมหาศาล จนทำนาย "คำถัดไป" ได้เก่งมาก ตัวอย่าง: Claude, GPT, Gemini, Llama, Typhoon (ไทย)

### ต้องรู้อะไรบ้าง
- **Token**: หน่วยย่อยที่ LLM มองข้อความ ไม่ใช่ "คำ" เป๊ะ — ภาษาไทยมักโดนตัด token เยอะกว่าอังกฤษ (กระทบ cost/context — ไฟล์ `09`)
- **Next-token prediction**: เลือกคำถัดไปจาก "ความน่าจะเป็น" ของคำที่เป็นไปได้
- **Context window**: token สูงสุดที่ LLM "เห็น" ได้ในครั้งเดียว (เช่น 8K, 128K, 200K) — ทุกอย่างที่ใส่เข้าไป (prompt + context + ประวัติ) ต้องไม่เกินนี้ → เหตุผลที่ต้อง "เลือกข้อมูลที่เกี่ยวข้อง" (งานของ RAG)
- **Hallucination**: ตอบผิดด้วยความมั่นใจ เพราะทำนายคำที่ "ฟังดูถูก" ไม่ใช่ค้นความจริง → เหตุผลหลักของ RAG
- **Knowledge cutoff**: รู้แค่ข้อมูลถึงวันที่เทรน ไม่รู้เรื่องใหม่/ข้อมูลเฉพาะองค์กรเรา → อีกเหตุผลของ RAG
- **Transformer / Attention** (intuition พอ): กลไกที่ทำให้โมเดลรู้ว่าคำไหนเกี่ยวกับคำไหน — ยังไม่ต้องเข้าใจคณิต
- **Pre-training / Fine-tuning / In-context learning**: RAG คือรูปแบบหนึ่งของ in-context learning

### เห็นภาพ token ด้วยโค้ด
```python
# pip install tiktoken
import tiktoken
enc = tiktoken.get_encoding("cl100k_base")

th = "สวัสดีครับ ผมกำลังเรียน RAG"
en = "Hello, I am learning RAG"
print(len(enc.encode(th)))   # ไทยมักได้ token เยอะกว่า
print(len(enc.encode(en)))   # อังกฤษน้อยกว่าทั้งที่ความหมายพอกัน
```

### ศึกษายังไง / วิธี
1. บล็อกไทย: **SCB10X** "เบื้องหลังการทำงานของ LLM", **TNIC**, **Disrupt**
2. เห็นภาพ: YouTube "How LLMs work", ช่อง **3Blue1Brown** ซีรีส์ Transformer/Attention
3. เล่นจริง: เว็บ **tiktokenizer** พิมพ์ไทย/อังกฤษ ดูการตัด token

> 💡 key takeaway: **LLM ไม่ได้ "รู้" มันแค่ "เดาคำเก่ง"** เข้าใจตรงนี้แล้วจะเข้าใจว่าทำไม RAG จำเป็น

---

## 1.2 การเรียกใช้ LLM ผ่าน API

### คืออะไร
เขียนโปรแกรมส่ง prompt ไป LLM แล้วรับคำตอบ — ทักษะที่ใช้ตลอด RAG pipeline

### ต้องรู้อะไรบ้าง + โค้ด

**โครงสร้าง message: role system / user / assistant**
```python
# pip install openai python-dotenv
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system",    "content": "คุณเป็นผู้ช่วยที่ตอบเป็นภาษาไทยสั้นกระชับ"},
        {"role": "user",      "content": "RAG คืออะไรใน 1 ประโยค"},
    ],
    temperature=0.2,
)
print(resp.choices[0].message.content)
```

**เทียบกับ Anthropic SDK (รูปแบบคล้ายกัน เรียนตัวเดียวโยกง่าย)**
```python
# pip install anthropic
from anthropic import Anthropic
client = Anthropic()
resp = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=200,
    system="คุณเป็นผู้ช่วยภาษาไทย",
    messages=[{"role": "user", "content": "RAG คืออะไร"}],
)
print(resp.content[0].text)
```

**จำประวัติแชต (LLM ไม่มีความจำข้ามครั้ง ต้องส่งประวัติไปทุกครั้ง)**
```python
history = [{"role": "system", "content": "คุณเป็นผู้ช่วยภาษาไทย"}]
def chat(user_msg):
    history.append({"role": "user", "content": user_msg})
    r = client.chat.completions.create(model="gpt-4o-mini", messages=history)
    answer = r.choices[0].message.content
    history.append({"role": "assistant", "content": answer})   # เก็บคำตอบกลับเข้าประวัติ
    return answer
```

**Streaming (รับทีละ token ทำ UX ดีขึ้น)**
```python
stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "เล่าเรื่องสั้นเกี่ยวกับ AI"}],
    stream=True,
)
for chunk in stream:
    delta = chunk.choices[0].delta.content or ""
    print(delta, end="", flush=True)
```

**Structured output — บังคับให้ตอบเป็น JSON (มีประโยชน์มากในระบบจริง)**
```python
resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "สกัดชื่อและอายุจาก: สมชาย อายุ 30 ปี"}],
    response_format={"type": "json_object"},   # บังคับ JSON
)
import json
data = json.loads(resp.choices[0].message.content)   # {"name": "สมชาย", "age": 30}
```

**Tool calling (พื้นฐานของ Agent — ลงลึกไฟล์ `08`)**
```python
tools = [{
    "type": "function",
    "function": {
        "name": "search_docs",
        "description": "ค้นเอกสารภายในบริษัท",
        "parameters": {"type": "object", "properties": {"query": {"type": "string"}}},
    },
}]
resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "นโยบายลาป่วยเป็นยังไง"}],
    tools=tools,   # LLM จะ "ขอ" เรียก search_docs เอง ถ้าเห็นว่าควรค้น
)
```

### ศึกษายังไง / วิธี
1. เลือกผู้ให้บริการ 1 เจ้า อ่าน **Quickstart** ใน docs ทางการ (docs.anthropic.com / platform.openai.com)
2. ทำตาม quickstart: ส่ง "Hello" รับคำตอบให้ได้ก่อน
3. ลอง system prompt, streaming, structured output, tool calling ทีละอย่าง
4. **โปรเจคจบหัวข้อ**: CLI ถาม-ตอบที่จำประวัติได้

---

## 1.3 พารามิเตอร์และการควบคุมโมเดล

### คืออะไร
ค่าต่างๆ ที่ปรับพฤติกรรม LLM ตอนเรียกใช้

### ต้องรู้อะไรบ้าง
- **Temperature**: ความสุ่ม — ต่ำ (0–0.3) ตอบนิ่งแม่น เหมาะ RAG/ข้อเท็จจริง; สูง (0.7–1) สร้างสรรค์ เหมาะงานเขียน
- **Max tokens**: จำกัดความยาวคำตอบ (คุม cost)
- **Top-p / Top-k**: คุมการสุ่มอีกแบบ — รู้ว่ามีพอ
- **Stop sequences**: หยุดตอบเมื่อเจอข้อความที่กำหนด
- **Cost**: คิดตาม token (input/output แยกราคา) — ประมาณค่าใช้จ่ายและตั้ง budget limit
- **Latency**: โมเดลใหญ่ฉลาดกว่าแต่ช้า/แพงกว่า

**ประมาณ cost คร่าวๆ ก่อนยิงจริง**
```python
import tiktoken
enc = tiktoken.get_encoding("cl100k_base")
prompt = "..." * 100
in_tokens = len(enc.encode(prompt))
# สมมติราคา input $0.15 / 1M tokens (ตรวจราคาจริง ณ วันใช้งานเสมอ)
print(f"~${in_tokens/1_000_000 * 0.15:.6f} ต่อ 1 คำขอ")
```

### ศึกษายังไง / วิธี
1. อ่านหน้า pricing/models ของผู้ให้บริการ (ราคา/ความสามารถเปลี่ยนบ่อย เช็ก ณ วันใช้งาน)
2. ทดลอง: ถามคำถามเดิม temperature 0 vs 1 เทียบคำตอบ

> 💡 สำหรับ RAG ส่วนใหญ่ตั้ง **temperature ต่ำ (0–0.2)** เพราะอยากให้ตอบตามข้อมูลจริง

---

## 1.4 Prompt Engineering

### คืออะไร
ศิลปะ+วิทยาศาสตร์ของการเขียนคำสั่งให้ LLM ทำงานดีที่สุด — คุ้มค่าเรียนสุดเพราะใช้ได้ทุกที่

### ต้องรู้อะไรบ้าง + โค้ด

**Few-shot (ให้ตัวอย่าง input→output โมเดลจะเลียนแบบ)**
```python
prompt = """จำแนกอารมณ์ของรีวิว (บวก/ลบ/กลาง)

รีวิว: อาหารอร่อยมาก -> บวก
รีวิว: รอนานเกินไป -> ลบ
รีวิว: ก็โอเคนะ -> กลาง
รีวิว: พนักงานบริการดีเยี่ยม ->"""
```

**Chain-of-Thought (สั่งให้ "คิดทีละขั้น" เพิ่มความแม่นกับโจทย์ที่ต้องใช้เหตุผล)**
```python
prompt = "ร้านมีแอปเปิล 23 ลูก ขายไป 8 ขายต่ออีก 5 เหลือกี่ลูก? คิดทีละขั้นก่อนตอบ"
```

**Prompt สำหรับ RAG โดยเฉพาะ — ใช้ delimiter/แท็กแยก context จากคำสั่ง + กัน hallucination**
```python
RAG_PROMPT = """คุณเป็นผู้ช่วยตอบคำถามจากเอกสารบริษัท
กติกา:
- ตอบจาก <context> เท่านั้น ห้ามใช้ความรู้ภายนอก
- ถ้าใน context ไม่มีคำตอบ ให้ตอบว่า "ไม่พบข้อมูลนี้ในเอกสาร"
- ระบุแหล่งอ้างอิง (เลขข้อ) ท้ายคำตอบ

<context>
{context}
</context>

คำถาม: {question}"""
```

### ศึกษายังไง / วิธี
1. อ่าน **prompt engineering guide** ของ Anthropic/OpenAI และ **promptingguide.ai**
2. คอร์สสั้นฟรี **DeepLearning.AI**: "ChatGPT Prompt Engineering for Developers"
3. ฝึก: โจทย์เดียวเขียน prompt 3 แบบ เทียบผล
4. **โปรเจคจบหัวข้อ**: prompt ที่ดึงข้อมูลเป็น JSON ตาม schema ได้ทุกครั้ง

> 💡 prompt ที่ดีมักประหยัดกว่า fine-tune ลองปรับ prompt ให้สุดก่อนคิดทำอย่างอื่น
> ⚠️ ระวัง **prompt injection** (ผู้ใช้แอบใส่คำสั่งมาแย่งคุม) — ลงลึกไฟล์ `07`

---

## 1.5 การรัน LLM บนเครื่องตัวเอง (Local LLM)

### คืออะไร
รันโมเดล open-source บนเครื่องเรา ไม่ต้องจ่ายค่า API และข้อมูลไม่ออกนอกเครื่อง

### ต้องรู้อะไรบ้าง + โค้ด

**Ollama — ง่ายสุด**
```bash
# ติดตั้ง Ollama จาก ollama.com แล้ว
ollama pull llama3.1        # ดาวน์โหลดโมเดล
ollama run llama3.1         # คุยใน terminal ได้เลย
```
```python
# เรียก Ollama ผ่าน API ที่ "เข้ากันได้กับ OpenAI" — โค้ดแทบเหมือนใช้ cloud
from openai import OpenAI
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
resp = client.chat.completions.create(
    model="llama3.1",
    messages=[{"role": "user", "content": "อธิบาย RAG สั้นๆ"}],
)
print(resp.choices[0].message.content)
```

- **โมเดล open-source**: Llama, Mistral, Qwen, Gemma, **Typhoon** (ไทย)
- **ขนาด (parameters)**: 1B/7B/70B — ใหญ่ = ฉลาดกว่าแต่กินแรม/VRAM มากกว่า เครื่องทั่วไปรันได้ ~7B–8B
- **Quantization**: บีบโมเดลให้เล็กลงรันบนเครื่องเล็กได้ (แลกความแม่นนิดหน่อย)
- **Hugging Face**: แหล่งรวมโมเดล open-source ใหญ่สุด
- **ข้อจำกัด local**: ช้า/ฉลาดน้อยกว่า cloud ตัวท็อป — เหมาะฝึก/งาน privacy

### ศึกษายังไง / วิธี
1. บล็อกไทย **Mikelopster** "LLM Local and API"
2. ติดตั้ง Ollama รันโมเดลแรกให้ได้
3. **โปรเจคจบหัวข้อ**: CLI จากหัวข้อ 1.2 ให้สลับใช้ได้ทั้ง cloud และ Ollama

---

## ✅ เช็กลิสต์ก่อนขึ้นเฟส 2

- [ ] อธิบาย token, context window, hallucination, knowledge cutoff ได้
- [ ] เรียก LLM API เขียนโปรแกรมถาม-ตอบที่จำประวัติได้
- [ ] ใช้ role system/user/assistant และ system prompt เป็น
- [ ] ทำ streaming + structured output (JSON) ได้
- [ ] ปรับ temperature/max tokens และประมาณ cost ได้
- [ ] เขียน prompt few-shot และ chain-of-thought เป็น
- [ ] รัน LLM local ด้วย Ollama ได้
- [ ] **เข้าใจชัดว่า "ทำไมต้องมี RAG"** (LLM มั่ว + ไม่รู้ข้อมูลเรา + knowledge cutoff)

ไปต่อ `03_Embeddings_และ_Vector_DB.md`
