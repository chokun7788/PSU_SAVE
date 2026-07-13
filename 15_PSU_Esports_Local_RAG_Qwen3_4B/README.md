# 15 - PSU Esports Local RAG with Fast Local LLM

โฟลเดอร์นี้คือ starter project สำหรับทำ Local RAG Chatbot ของ PSU Esports โดยใช้:

- LLM fast default: `qwen2.5:3b` ผ่าน Ollama
- LLM quality option: `qwen3:4b` ผ่าน Ollama
- Embedding: `intfloat/multilingual-e5-small`
- Vector DB: Chroma
- Data: chunks จาก `PSU Esports/Webscraping/sections/all_sections_rag_chunks.jsonl`
- Input phase แรก: Text
- Output: ตอบไทย/อังกฤษ พร้อม source/citation

---

## สถานะตอนนี้

ทำแล้ว:

- ติดตั้ง Ollama แล้ว
- โหลด `qwen3:4b` แล้ว
- โหลด `qwen2.5:3b` แล้ว สำหรับโหมดตอบเร็ว
- สร้างโฟลเดอร์โปรเจกต์แล้ว
- copy data chunks มาไว้ใน `data/raw/`
- เพิ่ม Content Optimization Layer แล้ว
- สร้าง `data/processed/optimized_chunks.jsonl` แล้ว
- เพิ่ม curated facts สำหรับกฎ/จอง/เกม/contact แล้ว
- เพิ่ม Rule-based FAQ Fast Path สำหรับคำถามซ้ำ ๆ แล้ว
- เพิ่ม Latency Optimization ให้ตอบได้ใกล้/ต่ำกว่า 10 วินาทีในโหมดเร็วแล้ว
- เตรียม notebook pipeline แล้ว
- เตรียม ground truth seed/template แล้ว

---

## โครงโฟลเดอร์

```text
15_PSU_Esports_Local_RAG_Qwen3_4B/
  README.md
  requirements.txt
  notebooks/
    01_local_rag_qwen3_4b.ipynb
  data/
    raw/
      all_sections_rag_chunks.jsonl
      manifest.json
    raw_sections/
    curated/
      curated_facts.jsonl
      rule_patterns.jsonl
    processed/
      optimized_chunks.jsonl
      optimization_manifest.json
    vector_db/
  ground_truth/
    README.md
    ground_truth_seed.jsonl
  prompts/
    system_prompt_th_en.md
  scripts/
    optimize_content.py
    rule_matcher.py
    run_ollama_fast.ps1
    run_ollama_qwen3_4b.ps1
  optimization/
    README.md
    content_optimization_checklist.md
    rule_based_fast_path.md
    latency_optimization.md
  docker/
    README.md
```

---

## วิธีเริ่มใช้งาน

### 1. เปิด Ollama

ถ้า `ollama` ยังไม่อยู่ใน PATH ให้ใช้ full path:

```powershell
& "C:\Users\Chokhun\AppData\Local\Programs\Ollama\ollama.exe" list
```

ตรวจว่าเห็น:

```text
qwen2.5:3b
qwen3:4b
```

หมายเหตุ: จากการทดสอบบนเครื่องนี้ `qwen3:4b` รันบน GPU ได้ แต่มี thinking mode ค่อนข้างยาวและมักใช้เวลาประมาณ 20-40 วินาทีต่อคำถาม ใน notebook จึงตั้งค่า default เป็น `qwen2.5:3b` สำหรับโหมดเร็ว ส่วน `qwen3:4b` เก็บไว้เป็นตัวเลือกกรณีต้องการคุณภาพหรือ reasoning มากขึ้น

### 2. ทดสอบโมเดล

โหมดเร็ว:

```powershell
& "C:\Users\Chokhun\AppData\Local\Programs\Ollama\ollama.exe" run qwen2.5:3b "ตอบเป็นภาษาไทยสั้น ๆ ว่า Local RAG คืออะไร"
```

โหมดคุณภาพ:

```powershell
& "C:\Users\Chokhun\AppData\Local\Programs\Ollama\ollama.exe" run qwen3:4b "ตอบเป็นภาษาไทยสั้น ๆ ว่า Local RAG คืออะไร"
```

### 3. เปิด Notebook

ก่อนเปิด notebook ถ้าข้อมูล raw เปลี่ยน ให้รัน optimize ใหม่:

```powershell
cd C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B
python scripts\optimize_content.py
```

ไฟล์หลักที่ notebook ใช้คือ:

```text
data/processed/optimized_chunks.jsonl
```

เปิดไฟล์นี้:

```text
notebooks/01_local_rag_qwen3_4b.ipynb
```

แล้วรัน cell ตามลำดับ

---

## Rule-based FAQ Fast Path

คำถามที่เป็น FAQ ชัด ๆ เช่น เช็คอินกี่นาที, จ่ายเงินภายในกี่นาที, PS5 มีเกมอะไร, ศูนย์อยู่ที่ไหน จะถูกจับด้วย rule ก่อนเข้า RAG/LLM

ข้อดี:

- เร็วมาก เพราะไม่ต้องเรียก LLM
- ลดโอกาส hallucination สำหรับกฎสำคัญ
- เหมาะกับ Facebook chatbot ที่มีคำถามซ้ำ ๆ

ไฟล์หลัก:

```text
data/curated/rule_patterns.jsonl
scripts/rule_matcher.py
optimization/rule_based_fast_path.md
```

ทดสอบ rule อย่างเดียว:

```powershell
cd C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B
python scripts\rule_matcher.py "เช็คอินล่วงหน้าได้กี่นาที"
python scripts\rule_matcher.py "PS5 มีเกมอะไรบ้าง"
```

ใน notebook ฟังก์ชัน `answer_question()` จะใช้ rule อัตโนมัติ:

```python
answer, hits, elapsed = answer_question("PS5 มีเกมอะไรบ้าง")
```

ถ้าอยากปิด rule เพื่อทดสอบ RAG + LLM แบบเต็ม:

```python
answer, hits, elapsed = answer_question("PS5 มีเกมอะไรบ้าง", use_rules=False)
```

หมายเหตุ: ถ้า `use_rules=False` จะไม่ใช้ rule แต่ยังใช้ RAG อยู่ โดย notebook มีชั้น `rag_direct_curated` เพิ่มเข้ามาแล้ว ถ้า retrieval ดึง `curated_fact` ที่ชัดเจนได้ จะตอบจากข้อความที่ดึงมาโดยตรงก่อนเรียก LLM เพื่อกันกรณี LLM ตอบว่าไม่พบข้อมูลทั้งที่ retrieve ถูกแล้ว

ถ้าต้องการทดสอบ RAG + LLM ล้วน ๆ โดยปิดทั้ง rule และ direct curated fallback:

```python
answer, hits, elapsed = answer_question("ศูนย์นี้เกี่ยวกับอะไร", use_rules=False, use_direct=False)
```

---

## Latency Optimization

ค่า default ใน notebook ถูกปรับเป็นโหมดเร็ว:

```python
LLM_MODEL = "qwen2.5:3b"
TOP_K = 4
MAX_CONTEXT_CHARS = 3200
MAX_DOC_CHARS = 750
LLM_NUM_CTX = 2048
LLM_NUM_PREDICT = 120
LLM_KEEP_ALIVE = "30m"
```

ผลทดสอบบนเครื่องนี้หลังโมเดล warm แล้ว:

```text
Rule-based FAQ: ประมาณ 0.006 วินาที
qwen2.5:3b + short context: ประมาณ 3-9 วินาที
qwen3:4b แบบเดิม: มักอยู่ประมาณ 20-40 วินาที
```

รายละเอียดอยู่ที่:

```text
optimization/latency_optimization.md
```

---

## ต้องทำ Ground Truth ไหม

ควรทำครับ

Ground Truth ไม่จำเป็นต้องใหญ่ตั้งแต่วันแรก แต่ควรมีอย่างน้อย:

```text
MVP: 30-50 คำถาม
ดีขึ้น: 100 คำถาม
production: 200+ คำถาม
```

เหตุผล:

- ใช้เทียบว่าโมเดลตอบดีจริงไหม
- ใช้วัดว่า retrieval ดึง source ถูกไหม
- ใช้กัน regressions เวลาเปลี่ยน chunking/model/prompt
- ใช้อธิบายตอน demo ว่าประเมินคุณภาพอย่างไร

เริ่มจากไฟล์:

```text
ground_truth/ground_truth_seed.jsonl
```

---

## สิ่งที่ยังขาด

ข้อมูลที่ควรเติมเพิ่ม:

1. ไฟล์กฎฉบับจริงจากพี่/ศูนย์
2. PDF หรือเอกสารที่เป็น official source
3. คำถาม FAQ จริงจากผู้ใช้/แอดมิน
4. กฎกรณีข้อมูลเว็บกับ PDF ขัดกัน ให้เชื่ออันไหน
5. รายละเอียด Facebook Page / Meta App / Page Access Token
6. ขอบเขต MVP วันอาทิตย์ว่าต้องโชว์อะไรบ้าง
7. จะให้บอทตอบเฉพาะ FAQ หรือเริ่มคำนวณเวลา/slot ด้วยไหม

---

## คำแนะนำสำหรับ MVP

ทำให้เสร็จตามลำดับนี้:

```text
1. Notebook RAG ตอบได้
2. Encoding ภาษาไทยไม่เพี้ยน
3. Retrieval source ถูก
4. โมเดลตอบจาก context ไม่เดา
5. มี ground truth 30-50 ข้อ
6. มี log คำถาม/คำตอบ
7. ค่อยทำ FastAPI/Streamlit
8. ค่อยต่อ Facebook
```
