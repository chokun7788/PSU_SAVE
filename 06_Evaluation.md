# 06 — Evaluation: วัดผล RAG ให้เป็น (เฟส 5) + โค้ดตัวอย่าง

> เป้าหมายเฟสนี้: เปลี่ยนจาก "รู้สึกว่าดีขึ้น" เป็น "มีตัวเลขยืนยันว่าดีขึ้น"
> ⚠️ เฟสที่คนข้ามมากที่สุด และเป็นสาเหตุที่ระบบ RAG หลายตัวพังเงียบๆ — **ห้ามข้าม เริ่มทำตั้งแต่ RAG ตัวแรก**

---

## ทำไม Evaluation สำคัญกว่าที่คิด
- RAG มี "ปุ่มปรับ" เยอะมาก (chunk size, k, embedding, reranker, prompt) วัดไม่เป็น = ปรับแบบสุ่ม
- คำตอบที่ "อ่านดูดี" อาจมั่ว/ยึดข้อมูลผิด — ตาเปล่ามองไม่ออกเมื่อข้อมูลเยอะ
- เปลี่ยนโมเดล/prompt ต้องรู้ "ดีขึ้นหรือแย่ลง" ก่อนปล่อยจริง
- มืออาชีพ **ตัดสินใจจากตัวเลข ไม่ใช่ความรู้สึก**

---

## 5.1 แนวคิด: แยกวัด 2 ส่วน
```
1. Retrieval ดีไหม?   (ค้น chunk ที่ถูกต้อง/ครบมาได้ไหม)
2. Generation ดีไหม?  (LLM ใช้ context ตอบถูกและไม่มั่วไหม)
```
คำตอบแย่ → ต้องรู้ว่า "ค้นมาผิด" (แก้ retrieval เฟส 4) หรือ "ค้นถูกแต่ตอบเพี้ยน" (แก้ prompt/LLM)

---

## 5.2 Metrics ที่ต้องรู้

**ฝั่ง Retrieval**
- **Context Precision**: ใน chunk ที่ค้นมา สัดส่วนที่เกี่ยวข้องจริง (ไม่มีขยะปน)
- **Context Recall**: ข้อมูลจำเป็นถูกค้นมาครบไหม (พลาดข้อมูลสำคัญไหม)
- **Hit Rate / MRR / NDCG**: ตัวชี้วัดการจัดอันดับ (chunk ถูกอยู่อันดับต้นไหม)

**ฝั่ง Generation**
- **Faithfulness / Groundedness**: คำตอบยึด context จริงไหม หรือมั่ว — **สำคัญสุด วัด hallucination โดยตรง**
- **Answer Relevance**: คำตอบตรงคำถามไหม
- **Answer Correctness**: ถูกต้องเทียบ ground truth (ถ้ามี)

**ภาพรวม**: Latency, Cost, Robustness

### โค้ดวัด Hit Rate แบบ manual (เข้าใจง่ายสุด เริ่มจากนี่ได้)
```python
# test_set: list ของ {"question", "relevant_id"}  (id ของ chunk ที่ควรค้นเจอ)
def hit_rate(test_set, k=4):
    hits = 0
    for item in test_set:
        qv = embedder.encode([item["question"]]).tolist()
        ids = col.query(query_embeddings=qv, n_results=k)["ids"][0]
        if item["relevant_id"] in ids:
            hits += 1
    return hits / len(test_set)

print(f"Hit Rate@4 = {hit_rate(test_set):.2%}")
```

---

## 5.3 เครื่องมือวัดผล

### คืออะไร
ไลบรารี/แพลตฟอร์มที่คำนวณ metric ให้ (หลายตัวใช้ "LLM-as-a-judge")

### RAGAS — เริ่มจากตัวนี้
```python
# pip install ragas datasets
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall
from datasets import Dataset

data = {
    "question":     ["ลาพักร้อนได้กี่วัน?"],
    "answer":       [rag("ลาพักร้อนได้กี่วัน?")],          # คำตอบจากระบบเรา
    "contexts":     [retrieve("ลาพักร้อนได้กี่วัน?", 4)[0]], # chunk ที่ค้นได้
    "ground_truth": ["พนักงานมีวันลาพักร้อน 10 วันต่อปี"],   # เฉลย
}
result = evaluate(
    Dataset.from_dict(data),
    metrics=[faithfulness, answer_relevancy, context_precision, context_recall],
)
print(result)   # ได้คะแนนแต่ละ metric
```

- **DeepEval / TruLens / Phoenix (Arize)**: เครื่องมือ eval อื่น มี dashboard ต่างกัน
- **LangSmith / Langfuse**: trace + eval บนข้อมูลจริง (production — ไฟล์ `07`)
- **LLM-as-a-judge**: ใช้ LLM ให้คะแนน — สเกลได้ แต่กรรมการก็ลำเอียง/พลาดได้ ควรสุ่มตรวจด้วยคนเป็นระยะ

### ศึกษายังไง / วิธี
1. ติดตั้ง **RAGAS** รันกับ RAG ที่มีอยู่ อ่าน docs (quickstart ชัด)
2. คอร์สสั้นฟรี **DeepLearning.AI**: "Building and Evaluating Advanced RAG"
3. **เน้น**: ทำให้ eval รันได้ด้วยคำสั่งเดียว เพื่อรันซ้ำทุกครั้งที่ปรับระบบ

---

## 5.4 สร้างชุดทดสอบ (Test Set / Golden Dataset)

### คืออะไร
ชุดคำถาม (+เฉลย +chunk ที่ควรค้นเจอ) ใช้เป็นมาตรฐานวัดซ้ำ — หัวใจของการวัดที่เชื่อถือได้

### ต้องรู้อะไรบ้าง + โค้ด
```python
# เริ่มเล็ก 20-50 คำถามก็ได้ ครอบคลุมหลายแบบ
test_set = [
    {"question": "ลาพักร้อนได้กี่วัน?", "ground_truth": "10 วันต่อปี", "relevant_id": "c12"},
    {"question": "เวลาทำการกี่โมง?",   "ground_truth": "9.00-18.00",  "relevant_id": "c3"},
    # คำถามนอกเอกสาร (ระบบควรตอบ "ไม่รู้")
    {"question": "ราคาหุ้นวันนี้?",     "ground_truth": "ไม่มีข้อมูลในเอกสาร", "relevant_id": None},
]

# สร้างอัตโนมัติด้วย RAGAS (แล้วให้คนตรวจ)
# from ragas.testset import TestsetGenerator
```

- **เริ่มเล็ก 20–50 คำถาม** ดีกว่าไม่มี
- ครอบคลุม: คำถามตรงๆ, ต้องรวมหลาย chunk, นอกเอกสาร (ควรตอบ "ไม่รู้"), กำกวม
- **Ground truth**: เฉลย/chunk ที่ "ควร" ถูกค้น
- **Synthetic generation**: ใช้ LLM สร้างคำถาม-คำตอบจากเอกสาร (RAGAS ทำได้) แต่ให้คนตรวจ
- **Regression test**: เพิ่มคำถามที่ระบบเคยตอบพลาดเข้าไปเรื่อยๆ

### ศึกษายังไง / วิธี
1. เขียนคำถามจริง 20–30 ข้อจากเอกสารตัวเอง + เฉลย
2. ลองให้ RAGAS generate เพิ่ม แล้วคัดกรองด้วยตา
3. **เน้น**: test set คือสินทรัพย์ ลงทุนกับมัน

---

## 5.5 Workflow การปรับปรุงด้วยข้อมูล
```
1. วัด baseline (รัน eval บน test set)
2. ตั้งสมมติฐาน ("เพิ่ม reranker น่าจะ precision ดีขึ้น")
3. เปลี่ยน "ทีละอย่าง" (หลายอย่างพร้อมกัน = ไม่รู้ว่าอะไรช่วย)
4. รัน eval ซ้ำ เทียบ baseline
5. เก็บถ้าดีขึ้น / ทิ้งถ้าแย่ลง → วนข้อ 2
```
```python
# ตัวอย่าง: หา chunk_size ที่ดีสุด
for size in [200, 400, 600, 800]:
    rebuild_index(chunk_size=size)        # สร้าง index ใหม่
    score = run_eval(test_set)            # วัดผล
    print(f"chunk_size={size}: faithfulness={score['faithfulness']:.3f}")
```
- **เปลี่ยนทีละตัวแปร** คือกฎเหล็ก
- แยกดูว่า metric retrieval หรือ generation ขยับ เพื่อรู้ว่าแก้ถูกจุด
- เก็บ log ผลการทดลองไว้เทียบย้อนหลัง

### ศึกษายังไง / วิธี
1. ทำจริง: baseline → เพิ่ม reranker → วัดใหม่ → เทียบ
2. ลองเปลี่ยน chunk size หลายค่าแล้ว plot หาจุดดีสุด

---

## ✅ เช็กลิสต์ก่อนขึ้นเฟส 6

- [ ] อธิบายความต่าง faithfulness / answer relevance / context precision / context recall
- [ ] รัน RAGAS วัด RAG ของตัวเองได้
- [ ] มี test set อย่างน้อย 20–30 คำถามพร้อมเฉลย
- [ ] เคยปรับระบบ 1 อย่าง (เช่นใส่ reranker) แล้ววัดได้ว่าดีขึ้น/แย่ลงจริง
- [ ] แยกออกว่าปัญหาอยู่ที่ retrieval หรือ generation
- [ ] รัน eval ซ้ำได้ด้วยคำสั่งเดียว

ไปต่อ `07_Production.md`

---
> หมายเหตุ: เนื้อหานี้พูดถึง evaluation ของระบบ RAG ถ้าสนใจ "ความปลอดภัย/ความเสี่ยง" ของ output ดูไฟล์ `07` หัวข้อ guardrails
