# Extended Paper Technique Scan - PSU Esports Chatbot / RAG / Entity Resolver

วันที่: 2026-08-01

## สรุปสั้นที่สุด

หลังอ่านเพิ่มหลายสาย แนวทางที่เหมาะกับโปรเจกต์นี้ไม่ใช่เพิ่ม rule ไปเรื่อย ๆ แต่ควรเปลี่ยนเป็น architecture แบบนี้:

`Data-driven Entity Resolver -> Abstain/Clarify Policy -> Structured/Fast/RAG -> Retrieval Evaluator -> Answer Validator`

เทคนิคที่ควรเอามาใช้จริงก่อน:

1. `Entity Resolver v2` สร้าง candidate จาก data จริง
2. `Cross-Encoder Reranker` ขนาดเล็กสำหรับ rerank candidate / retrieved facts
3. `Reject Option / Selective Prediction` เพื่อถามกลับเมื่อเสี่ยงตอบผิด
4. `Operation-aware Clarification` ถามกลับตามเจตนา เช่น ปุ่ม/จอง/ราคา/รายการเกม
5. `Answerability Gate` ก่อนเข้า RAG และหลัง retrieve
6. `Failure-driven Eval / Active Learning Loop` เอา log ที่พลาดไปสร้าง eval/data ไม่ใช่เพิ่ม if เฉพาะหน้า

เทคนิคที่น่าลองทีหลัง:

- Query rewrite / decomposition สำหรับคำถามยาวหรือหลาย intent
- CRAG-style retrieval evaluator
- Self-RAG-style reflection แบบไม่ train model ใหม่
- Conformal calibration สำหรับ threshold

เทคนิคที่ไม่ควรเป็นแกนหลักตอนนี้:

- HyDE / RAG-Fusion แบบเปิดกว้าง เพราะอาจเพิ่ม latency และทำให้ ambiguous query ขยายมั่ว
- LLM เป็น router หลักทุกคำถาม เพราะช้าและเสี่ยงมั่ว entity
- Multi-agent RAG เต็มรูปแบบ เพราะหนักเกิน use case/local machine

## Paper / Source ที่อ่านเพิ่ม

### 1. RQ-RAG - Query Refinement for RAG

Source:

- `RQ-RAG: Learning to Refine Queries for Retrieval Augmented Generation`
- https://arxiv.org/html/2404.00610v1

ใจความ:

- RAG ทั่วไปมักใช้ query แรกตรง ๆ ทั้งที่ query อาจกำกวม/ซับซ้อน
- RQ-RAG ฝึกให้ model rewrite, decompose, disambiguate query ก่อน retrieve

เอามาใช้กับเรา:

- ใช้ query rewriting เฉพาะตอน entity ชัดแล้ว แต่คำถามยาวหรือมีหลายส่วน
- เช่น `Tekken 8 กับ Mario มีปุ่มอะไรบ้าง` ต้อง decompose เป็น 2 subquestions ก่อน
- ห้ามใช้ rewrite เพื่อเดา entity ที่ยังไม่ชัด เช่น `Mario เล่นยังไง`

ความเหมาะสม: สูง แต่ทำหลัง Entity Resolver v2

### 2. Conversational Search Survey

Source:

- `A Survey of Conversational Search`
- https://arxiv.org/html/2410.15576v1

ใจความ:

- conversational search มี module สำคัญคือ query reformulation, search clarification, conversational retrieval, response generation

เอามาใช้กับเรา:

- แยก `context resolver` ออกจาก `entity resolver`
- context ใช้เฉพาะ follow-up ที่ปลอดภัย เช่น `ปุ่ม` หลังเพิ่งคุย Gran Turismo
- ถ้า user พิมพ์ target ใหม่ ต้องให้ target ใหม่ชนะ context เก่า

ความเหมาะสม: สูง

### 3. ICR - Iterative Clarification and Rewriting

Source:

- `ICR: Iterative Clarification and Rewriting for Conversational Search`
- https://aclanthology.org/2025.emnlp-main.496.pdf

ใจความ:

- ระบบสลับระหว่างถาม clarification กับ rewrite query เพื่อเพิ่ม retrieval performance

เอามาใช้กับเรา:

- ไม่ต้องทำ iterative หลายรอบเต็มรูปแบบ
- ใช้แบบเบา: ถามกลับ 1 รอบพร้อม choices จาก candidate จริง แล้ว rewrite query หลัง user เลือก
- เช่น user: `Mario ปุ่มอะไร` -> bot: `หมายถึงเกมไหน? ...` -> user: `Kart` -> rewrite เป็น `Mario Kart 8 Deluxe ปุ่มอะไร`

ความเหมาะสม: สูงมากสำหรับ follow-up

### 4. Generating Clarifying Questions for IR

Source:

- `Generating Clarifying Questions for Information Retrieval`
- https://www.microsoft.com/en-us/research/wp-content/uploads/2020/01/webconf-2020-camera-zamani-et-al.pdf

ใจความ:

- clarification ที่ดีควรรู้ aspect ของ query และช่วยให้ retrieval ตรงขึ้น

เอามาใช้กับเรา:

- clarification ควรมาจาก candidate/aspect จริง ไม่ใช่ประโยคกว้าง ๆ
- ตัวเลือกควรสั้นและกด/พิมพ์ตามได้ง่าย เช่น `Warzone`, `Modern Warfare III`

ความเหมาะสม: สูง

### 5. Diversify-Verify-Adapt / Ambiguous RAG

Source:

- `Diversify-Verify-Adapt: Efficient and Robust Retrieval-Augmented Ambiguous Question Answering`
- https://aclanthology.org/2025.naacl-long.56.pdf

ใจความ:

- RAG มีปัญหากับ ambiguous query
- ใช้ retrieval diversification และ retrieval verification เพื่อลด retrieval คุณภาพต่ำ

เอามาใช้กับเรา:

- สร้าง interpretations จาก catalog ก่อน ไม่ใช่ให้ LLM แต่งเอง
- verify ว่าแต่ละ interpretation มี source จริงและ answerable
- ถ้า valid หลายตัว ให้ถามกลับ/list ไม่ใช่เลือกเอง

ความเหมาะสม: สูง

### 6. VerDICT - Agentic Verification for Ambiguous Query Disambiguation

Source:

- `Agentic Verification for Ambiguous Query Disambiguation`
- https://aclanthology.org/2026.findings-acl.1932/

ใจความ:

- pipeline แบบ generate interpretations ก่อนแล้วค่อย verify ทีหลังเสี่ยงสร้าง ungrounded queries
- VerDICT ผูก retriever relevance และ generator answerability feedback ตั้งแต่ต้น

เอามาใช้กับเรา:

- candidate ต้องมาจาก data/catalog ก่อน
- ก่อน RAG ต้องเช็ค `candidate answerable ไหม`
- ถ้า query ambiguous แล้ว retrieved facts หลายชุดถูกทั้งคู่ ต้องถามกลับ

ความเหมาะสม: สูงมาก

### 7. RAG with Conflicting Evidence

Source:

- `Retrieval-Augmented Generation with Conflicting Evidence`
- https://arxiv.org/abs/2504.13079

ใจความ:

- RAG ต้องรับมือ query กำกวม, evidence ขัดแย้ง, misinformation/noise พร้อมกัน
- ถ้ามีหลาย valid answers ต้องไม่บังคับเหลือคำตอบเดียว

เอามาใช้กับเรา:

- `Resident` อาจตรง Resident Evil 4 และ Resident Evil Village
- ถ้า evidence หลายเกมถูกพร้อมกัน ให้ตอบแบบ `มีหลายเกมที่ตรง` หรือถามกลับ
- Answer Validator ต้องเช็คว่า answer ไม่แอบเลือกหนึ่ง entity ทั้งที่ resolver บอก ambiguous

ความเหมาะสม: สูง

### 8. CRAG - Corrective Retrieval Augmented Generation

Source:

- `Corrective Retrieval Augmented Generation`
- https://arxiv.org/abs/2401.15884

ใจความ:

- เพิ่ม lightweight retrieval evaluator เพื่อประเมินคุณภาพ retrieved docs
- ถ้า retrieve แย่ ให้ trigger action อื่นแทนใช้ผล retrieval ดิบ

เอามาใช้กับเรา:

- ทำ `Retrieval Quality Gate` แบบง่าย:
  - retrieved hit ต้อง match entity
  - source_type ต้องตรง operation
  - top score ต้องเกิน threshold
  - ถ้า top-k ขัดกัน ให้ถามกลับ/no-answer
- ไม่ต้องใช้ web search fallback ใน local PSU facts

ความเหมาะสม: สูง แต่ทำแบบเบา

### 9. Self-RAG

Source:

- `Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection`
- https://arxiv.org/abs/2310.11511

ใจความ:

- model เรียนรู้ว่าจะ retrieve เมื่อไหร่ และ critique output/retrieved passages ด้วย reflection tokens

เอามาใช้กับเรา:

- ไม่ควร train Self-RAG ใหม่
- เอาแนวคิดมาทำ rule/validator:
  - need_retrieval?
  - evidence_relevant?
  - answer_supported?
  - answer_type_correct?
- ใช้ LLM judge เฉพาะ offline eval หรือเคสยาก ไม่ใช้ทุก request

ความเหมาะสม: กลาง-สูง ถ้าใช้เป็นแนวคิด ไม่ใช่ full model

### 10. HyDE

Source:

- `Precise Zero-Shot Dense Retrieval without Relevance Labels`
- https://aclanthology.org/2023.acl-long.99/

ใจความ:

- ให้ LLM สร้าง hypothetical document แล้ว embed เพื่อช่วย dense retrieval

เอามาใช้กับเรา:

- เหมาะกับคำถาม general knowledge หรือเอกสารยาวที่ไม่มี keyword ตรง
- ไม่เหมาะกับ PSU facts ที่ต้องไม่เดา เพราะ hypothetical doc อาจแต่ง fact เอง
- ถ้าจะใช้ ให้ใช้เฉพาะหลัง answerability gate และห้ามใช้กับราคา/เกม/ปุ่มที่ต้องตรง source

ความเหมาะสม: ต่ำ-กลาง

### 11. RAG-Fusion / Reciprocal Rank Fusion

Source:

- `Scaling Retrieval Augmented Generation with RAG Fusion: Lessons from an Industry Deployment`
- https://arxiv.org/abs/2603.02153

ใจความ:

- fusion เพิ่ม recall ได้ แต่ใน production-style constraints อาจไม่เพิ่ม end-to-end accuracy และเพิ่ม latency

เอามาใช้กับเรา:

- ใช้ RRF เฉพาะรวม BM25 + vector + alias retrieval
- ไม่ควร generate multi-query หลายชุดด้วย LLM ทุกคำถาม

ความเหมาะสม: กลาง

### 12. Selective Prediction / Abstention in NLP

Source:

- `The Art of Abstention: Selective Prediction and Error Regularization for Natural Language Processing`
- https://aclanthology.org/2021.acl-long.84/

ใจความ:

- classifier ควร abstain ใน low-confidence examples
- confidence estimator มีผลมาก และต้องวัด coverage/accuracy พร้อมกัน

เอามาใช้กับเรา:

- วัดผลแยก:
  - answered accuracy
  - false-answer rate
  - clarification rate
  - no-answer rate
  - coverage
- PSU chatbot ควรยอม clarification มากขึ้นเพื่อ false-answer ต่ำลง

ความเหมาะสม: สูงมาก

### 13. Conformal Prediction for NLP

Source:

- `Conformal Prediction for Natural Language Processing: A Survey`
- https://arxiv.org/abs/2405.01976

ใจความ:

- conformal prediction ช่วยทำ uncertainty set/coverage guarantee แบบ model-agnostic

เอามาใช้กับเรา:

- ใช้ภายหลังเพื่อ calibrate threshold จาก eval set จริง
- เช่น ตั้ง threshold ให้ false-answer rate ไม่เกิน target ที่กำหนด
- ตอนนี้ยังไม่จำเป็นต้องทำเต็มรูปแบบ แต่ควรออกแบบ log ให้เก็บ score/margin ไว้

ความเหมาะสม: กลาง-สูง สำหรับ production tuning

### 14. BGE-M3 Embedding

Source:

- `BGE M3-Embedding: Multi-Lingual, Multi-Functionality, Multi-Granularity Text Embeddings`
- https://aclanthology.org/2024.findings-acl.137/
- https://bge-model.com/bge/bge_m3.html

ใจความ:

- รองรับ multilingual มากกว่า 100 ภาษา
- รองรับ dense, sparse, multi-vector retrieval
- รองรับ input ยาวถึง 8192 tokens

เอามาใช้กับเรา:

- เหมาะกับ Thai/English mixed query
- ใช้ทำ candidate semantic retrieval และ RAG retrieval ได้
- ควรใช้เป็น embedding/rerieval layer มากกว่าให้ LLM generate

ความเหมาะสม: สูงมาก

### 15. BGE Reranker v2 M3

Source:

- https://bge-model.com/tutorial/5_Reranking/5.2.html
- https://huggingface.co/BAAI/bge-reranker-v2-m3

ใจความ:

- multilingual cross-encoder reranker
- ขนาดประมาณ 568M
- เหมาะกับ rerank เอกสาร/candidate จำนวนน้อยหลัง retrieval

เอามาใช้กับเรา:

- rerank top candidates เช่น Mario family, Call of Duty family, Resident family
- rerank retrieved facts ก่อนส่ง answer composer
- ใช้เฉพาะ top-k เล็ก ๆ เพื่อไม่ให้ latency สูง

ความเหมาะสม: สูงมาก

### 16. Qwen3 Embedding / Reranker

Source:

- `Qwen3 Embedding: Advancing Text Embedding and Reranking Through Foundation Models`
- https://arxiv.org/abs/2506.05176
- https://qwenlm.github.io/blog/qwen3-embedding/
- https://huggingface.co/Qwen/Qwen3-Reranker-0.6B

ใจความ:

- มี embedding/reranker size 0.6B, 4B, 8B
- เน้น multilingual retrieval/reranking

เอามาใช้กับเรา:

- ลอง `Qwen3-Reranker-0.6B` เป็น candidate reranker ได้
- เหมาะกับการเทียบกับ BGE reranker เพราะเล็กกว่า 1B และ multilingual
- ต้อง benchmark latency local ก่อน

ความเหมาะสม: สูงสำหรับ experiment

### 17. CONQRR / Conversational Query Rewriting

Source:

- `CONQRR: Conversational Query Rewriting for Retrieval with Reinforcement Learning`
- https://research.google/pubs/conqrr-conversational-query-rewriting-for-retrieval-with-reinforcement-learning/

ใจความ:

- rewrite คำถามหลาย turn ให้เป็น standalone question เพื่อ retrieval ดีขึ้น

เอามาใช้กับเรา:

- ใช้แนวคิดกับ follow-up:
  - user: `Gran Turismo เล่นยังไง`
  - user: `ปุ่ม`
  - rewrite เป็น `Gran Turismo 7 ปุ่มอะไร`
- ต้องมี context safety ไม่ให้ target ใหม่โดน context เก่าทับ

ความเหมาะสม: สูง

### 18. GuideCQR

Source:

- `Conversational Query Reformulation with the Guidance of Retrieved Documents`
- https://arxiv.org/html/2407.12363v2

ใจความ:

- ใช้ข้อมูลจาก retrieval รอบแรกมาช่วย rewrite query

เอามาใช้กับเรา:

- ทำได้ใน RAG layer:
  - retrieve เบื้องต้น
  - extract candidate keywords/entities
  - rewrite เฉพาะถ้าไม่ conflict
- ไม่ควรใช้กับ structured facts ที่มี data ตรงอยู่แล้ว

ความเหมาะสม: กลาง

## เทคนิคที่ควรนำไปทำจริง เรียงลำดับ

### Priority 1 - Entity Resolver v2

เป้าหมาย:

- แก้ปัญหา hardcode family ที่เพิ่มไม่จบ
- ทำให้ router/structured/RAG ใช้ entity decision เดียวกัน

ควรมี output:

```json
{
  "status": "exact|ambiguous|incomplete|unknown|nil",
  "operation": "controls|availability|price|booking|detail|list",
  "top_candidate": "...",
  "candidates": [],
  "top_score": 0.0,
  "margin": 0.0,
  "requires_clarification": true,
  "reason": "family_name_has_multiple_valid_candidates"
}
```

### Priority 2 - Reranker สำหรับ candidate

เริ่มจาก rule score ก่อน แล้วค่อย rerank top-k ด้วย model เล็ก:

- `BAAI/bge-reranker-v2-m3` ประมาณ 568M
- `Qwen/Qwen3-Reranker-0.6B`

ใช้เมื่อ:

- candidate 2-8 ตัว
- route score สูสี
- query เป็น Thai/English mixed

ไม่ใช้เมื่อ:

- exact alias ชัดมาก
- คำถามราคา/เวลา/กติกาที่ structured answer ได้เลย

### Priority 3 - Clarification Policy

ชนิด clarification:

- `entity clarification`: หมายถึงเกมไหน
- `operation clarification`: หมายถึงเกมใน PC / ราคา PC / จอง PC / ปุ่มเกม
- `context clarification`: จากคำว่า `ปุ่ม`, `เกมนี้`, `อันนี้`

หลัก:

- ถามครั้งเดียวให้เลือกง่าย
- choice มาจาก source จริง
- ถ้า user ตอบสั้น ให้ resolver รับต่อได้

### Priority 4 - Retrieval Quality Gate

ก่อน answer จาก RAG:

- entity status ต้อง exact หรือ operation ต้องเป็น list
- top hit ต้อง match entity/operation
- ถ้ามีหลาย entity ใน hits ต้องถามกลับ
- ถ้า evidence ไม่พอ ต้อง no-answer

### Priority 5 - Eval/Logging สำหรับ calibration

ทุกคำตอบควรเก็บ:

- resolver status
- candidates
- score/margin
- route
- retrieval score
- answer source
- validator result
- clarification/no-answer flag

ใช้ log เพื่อสร้าง active learning loop:

1. เก็บ failed/clarified/slow cases
2. group เป็น ambiguity family อัตโนมัติ
3. เติม alias/source/eval ไม่ใช่เติม if ทีละเคส
4. rerun targeted eval

## เทคนิคที่ยังไม่ควรทำเป็นแกนหลัก

### HyDE

เหตุผล:

- ใช้ LLM สร้าง hypothetical content เสี่ยงแต่ง PSU facts
- latency เพิ่ม
- เหมาะกับ open-domain มากกว่า structured local facts

ใช้ได้เฉพาะ:

- general question
- competition rules long documents
- เคสที่ไม่ใช่ราคา/เกม/ปุ่ม/จอง

### Full Self-RAG

เหตุผล:

- ต้อง train/ใช้ model เฉพาะ
- หนักเกิน local chatbot ตอนนี้

ใช้แนวคิดได้:

- ทำ reflection checklist ใน validator แทน

### Multi-agent debate / MADAM-RAG

เหตุผล:

- เหมาะกับ evidence ขัดแย้งหนัก
- latency สูงมาก

ใช้ได้ใน offline analysis เท่านั้น

## Proposed Flow ใหม่ที่ควรไปทางนี้

```text
User Input
  -> Normalize / Typo / Alias
  -> Operation Detector
  -> Entity Resolver v2
      -> candidate generation จาก data จริง
      -> rule score
      -> optional local reranker เฉพาะ top-k uncertain
      -> status exact / ambiguous / incomplete / nil
  -> Decision Policy
      -> exact + structured answerable: Structured/Fast
      -> exact + needs docs: RAG with retrieval gate
      -> ambiguous + list intent: list candidates
      -> ambiguous + specific intent: clarification
      -> nil/unknown: no-answer หรือ general fallback ตาม scope
  -> Answer Composer
  -> Answer Validator
  -> Final Answer + trace/log
```

## Local Model / Tool ที่น่าลอง

ยังไม่ควรโหลดทันทีจนกว่าจะทำ resolver shell พร้อม benchmark แต่ candidate ที่เหมาะ:

1. `BAAI/bge-reranker-v2-m3`
   - multilingual
   - ประมาณ 568M
   - เหมาะ rerank top-k candidate/facts

2. `Qwen/Qwen3-Reranker-0.6B`
   - multilingual
   - 0.6B
   - เหมาะเทียบกับ BGE reranker

3. `BAAI/bge-m3`
   - embedding multilingual
   - เหมาะทำ vector retrieval Thai/English mixed

4. `Qwen/Qwen3-Embedding-0.6B`
   - embedding multilingual
   - เหมาะลองเทียบกับ BGE-M3

ไม่แนะนำเป็นอันดับแรก:

- `mxbai-embed-large-v1` เพราะเด่น English มากกว่า Thai/multilingual mixed ใน use case นี้

## สรุปคำตอบสำหรับโปรเจกต์

ถ้าจะหยุดปัญหา “เจอเคสใหม่แล้วต้องเพิ่ม rule ตลอด” ต้องทำระบบให้เป็น:

`data -> candidate -> score -> margin -> abstain/clarify -> answer`

ไม่ใช่:

`if query contains X -> answer Y`

งานถัดไปที่ควรทำ:

1. implement `Entity Resolver v2`
2. ต่อเข้ากับ ambiguity gate / structured tools / RAG
3. เพิ่ม targeted eval สำหรับ ambiguity โดยเฉพาะ
4. benchmark แบบ no-reranker ก่อน
5. ค่อยลอง BGE/Qwen reranker local กับเฉพาะเคส uncertain

