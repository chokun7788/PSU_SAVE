# Paper Technique Review - Entity Disambiguation / Abstention

วันที่: 2026-08-01

## ข้อสรุปแบบตัดสินใจ

วิธีที่เหมาะกับโปรเจกต์นี้ที่สุดคือทำ `Entity Resolver v2` แบบ data-driven ก่อนเข้า structured/fast/RAG:

1. สร้าง candidate จาก data จริงทั้งหมด ไม่ hardcode ทีละ family
2. ให้คะแนน candidate ด้วย exact alias, fuzzy/token match, operation compatibility, source priority และ session context แบบมี guard
3. ใช้ margin threshold / reject option เพื่อตัดสินว่า `ตอบได้`, `ต้องถามกลับ`, `unknown/no-answer`
4. ใช้ LLM เฉพาะเคสที่ scorer ยังไม่มั่นใจ และบังคับให้เลือกจาก candidate list เท่านั้น
5. ห้ามปล่อย ambiguous entity เข้า RAG ตรง ๆ ต้องผ่าน answerability check ก่อน

ผลที่ควรได้:

- `Call of เล่นยังไง` ไม่ควรเลือก Modern Warfare III เอง ต้องถามกลับระหว่าง `Call of Duty: Modern Warfare III` กับ `Call of Duty: Warzone`
- `Mario เล่นยังไง` ไม่ควรเลือก Mario Party เอง ต้องถามกลับหรือ list candidate ตามเจตนา
- `Mario มีเกมอะไรบ้าง` ตอบ list ได้ เพราะ operation คือถามรายการ ไม่ใช่ถามปุ่ม/วิธีเล่นของเกมเดียว
- `ปุ่ม` หลังจากถาม Gran Turismo ใน session เดิม ใช้ context ได้ แต่ต้องไม่ใช้ context ถ้า user เปลี่ยน target ใหม่ชัดกว่า

## เป้าหมาย

หาวิธีแก้ปัญหา chatbot ที่ต้องคอยเพิ่ม rule/fast/family guard ไปเรื่อย ๆ เมื่อเจอ query ใหม่ เช่น `Mario`, `Call of`, `Resident`, `เกมนี้`, `ปุ่ม`

สรุปสั้น:

- ปัญหานี้ควรแก้ด้วย `Entity Linking / Entity Disambiguation + Reject Option`
- ไม่ควร hardcode family เพิ่มทีละเคส
- ให้ระบบสร้าง candidate จาก data เอง แล้วใช้ scoring/margin/abstention ตัดสินว่าจะตอบหรือถามกลับ

## Paper / Source ที่อ่านประกอบ

### 1. Neural Entity Linking Survey

Source:

- `Neural Entity Linking: A Survey of Models Based on Deep Learning`
- https://www.semantic-web-journal.net/system/files/swj2986.pdf

ใจความที่เอามาใช้:

- entity linking architecture มักแยกเป็น:
  - candidate generation
  - mention/context encoding
  - entity ranking
- ตรงกับปัญหาเรา เพราะ query ต้อง map ไปยัง game/entity ใน KB ก่อนตอบ

เอามาใช้กับเรา:

- สร้าง `Game Entity Resolver v2`
- ไม่ให้ router เลือกเกมเอง
- resolver คืน candidate list + score + match type

### 2. Entity Disambiguation for Knowledge Base Population

Source:

- `Entity Disambiguation for Knowledge Base Population`
- https://www.cs.jhu.edu/~mdredze/publications/entity_linking_coling.pdf

ใจความที่เอามาใช้:

- ใช้ candidate selection เพื่อหา name variants
- ใช้ ranker ให้คะแนน candidate
- มีแนวคิด NIL prediction เพื่อไม่ link เมื่อไม่มี target ที่เหมาะ

เอามาใช้กับเรา:

- `Call of` ถ้า candidate ไม่มั่นใจหรือ incomplete ให้เป็น NIL/ambiguous ไม่ใช่เลือก Modern Warfare III
- `Mario` ถ้า candidate หลายตัวสูสี ให้ถามกลับ

### 3. Learn to Not Link / NIL Prediction

Source:

- `Learn to Not Link: Exploring NIL Prediction in Entity Linking`
- https://aclanthology.org/2023.findings-acl.690.pdf

ใจความที่เอามาใช้:

- NIL prediction คือการเรียนรู้/ตัดสินว่า mention ไม่ควร link ไป entity ใด
- ใช้ similarity threshold และ candidate signals

เอามาใช้กับเรา:

- ถ้า top score ต่ำ หรือ margin ระหว่างอันดับ 1 กับ 2 ต่ำ ให้ `abstain`
- ถ้า query เป็น non-entity phrase เช่น `ปุ่ม`, `เล่นยังไง`, `เกมนี้` ให้ไม่ link

### 4. Machine Learning with a Reject Option

Source:

- `Machine Learning with a Reject Option: A Survey`
- https://arxiv.org/html/2107.11277v3

ใจความที่เอามาใช้:

- โมเดล/ระบบควร abstain เมื่อเสี่ยงตอบผิด
- แยก rejection ได้เป็น ambiguity rejection และ novelty rejection
- มี trade-off ระหว่าง coverage กับ risk

เอามาใช้กับเรา:

- ถ้าไม่มั่นใจ ให้ถามกลับแทนตอบผิด
- วัดผลแยก:
  - accuracy on answered questions
  - coverage
  - abstention rate
  - false-answer rate

### 5. Selective Classification / Risk-Coverage

Source:

- `Selective Classification for Deep Neural Networks`
- https://papers.nips.cc/paper/7073-selective-classification-for-deep-neural-networks

ใจความที่เอามาใช้:

- selective classifier เลือกตอบเฉพาะเคสที่มั่นใจ
- ผู้ใช้สามารถกำหนด risk level ที่ยอมรับได้

เอามาใช้กับเรา:

- PSU fact chatbot ควรเลือก risk ต่ำมาก
- ยอมถามกลับมากขึ้น ดีกว่าตอบผิดเรื่องราคา/เกม/ปุ่ม

### 6. Disambiguation in Conversational QA

Source:

- `Disambiguation in Conversational Question Answering in the Era of LLMs and Agents: A Survey`
- https://aclanthology.org/2025.emnlp-main.482.pdf

ใจความที่เอามาใช้:

- ambiguity เป็นปัญหาหลักของ conversational QA
- มีหลายแนวทาง เช่น detect ambiguity, ask clarification, use context, compare interpretations

เอามาใช้กับเรา:

- session context ช่วยได้ แต่ต้องมี topic-shift guard
- ถ้า query ใหม่มี target ใหม่ ต้องไม่ยึด context เก่า
- clarification ควรมี choices จากข้อมูลจริง

### 7. Ambiguous Query Disambiguation in RAG / VerDICT

Source:

- `Agentic Verification for Ambiguous Query Disambiguation`
- https://aclanthology.org/2026.findings-acl.1932/

ใจความที่เอามาใช้:

- ใน RAG ถ้า generate interpretations ก่อน retrieve อาจเกิด ungrounded queries และ cascading errors
- VerDICT รวม diversification กับ verification โดยใช้ retriever relevance และ answerability feedback เร็วขึ้น

เอามาใช้กับเรา:

- อย่าปล่อย ambiguous query เข้า RAG ตรง ๆ
- ให้สร้าง interpretations/candidates จาก catalog ก่อน
- เช็คว่าแต่ละ candidate answerable จาก source จริงไหม
- ถ้าไม่มี candidate ที่ answerable ชัด ให้ถามกลับ

### 8. RAG with Conflicting Evidence

Source:

- `Retrieval-Augmented Generation with Conflicting Evidence`
- https://arxiv.org/html/2504.13079v2

ใจความที่เอามาใช้:

- RAG ยังมีปัญหาเมื่อ retrieved documents ขัดแย้งหรือรองรับหลายคำตอบ

เอามาใช้กับเรา:

- ถ้า `Resident` ดึงได้ทั้ง Resident Evil 4 และ Resident Evil Village ต้องไม่เลือกเอง
- ถ้า evidence มีหลาย valid answers ให้ถามกลับหรือ list candidates

## เทคนิคที่เหมาะกับโปรเจกต์เรา

### A. Data-Driven Entity Resolver

ควรทำเป็น module กลาง เช่น:

- `app/pipeline/entity_resolver.py`

Input:

- normalized query
- operation hint เช่น controls/detail/booking/price
- session context optional

Output:

```json
{
  "status": "exact|ambiguous|incomplete|unknown|nil",
  "top_candidate": "...",
  "candidates": [
    {"id": "...", "title": "...", "score": 0.91, "sources": ["service_game_availability"]}
  ],
  "top_score": 0.91,
  "margin": 0.34,
  "reason": "exact alias match"
}
```

### B. Candidate Generation จาก data ไม่ใช่ hardcode

แหล่ง candidate:

- `service_game_availability.jsonl`
- `game_title_aliases.jsonl`
- `game_control_facts.jsonl`
- `game rows / current catalog`

สร้าง candidate จาก:

- exact alias
- normalized alias
- compact alias
- token overlap
- fuzzy match
- family grouping จาก shared tokens / alias parent
- current catalog availability

### C. Candidate Ranking

Feature ที่เหมาะ:

- exact alias match
- substring/compact match
- token overlap
- action compatibility เช่น ถามปุ่ม ต้องมี control facts
- operation compatibility เช่น ถามจอง ต้องมี service availability
- source priority เช่น current catalog > old control reference
- session context boost แบบมี TTL
- negative signals เช่น partial mention `call of`

### D. Margin Threshold + Reject Option

ตัวอย่าง policy:

- `top_score >= 0.90` และ `margin >= 0.20` -> ตอบได้
- `top_score >= 0.80` แต่ `margin < 0.15` -> ถามกลับ
- `top_score < 0.70` -> unknown/no-answer
- family/incomplete mention -> ถามกลับ ยกเว้น operation เป็น list เช่น `Mario มีเกมอะไรบ้าง`

### E. Operation-Specific Disambiguation

คำถามคนละ operation ต้องใช้เกณฑ์ต่างกัน:

- `Mario มีเกมอะไรบ้าง` -> ตอบ list ได้
- `Mario ปุ่มอะไร` -> ambiguous ต้องถามกลับ
- `Call of Duty จองอะไร` -> family clarification
- `Call of Duty Warzone จองอะไร` -> exact answer
- `Resident เล่นยังไง` -> ambiguous
- `Resident Evil Village เล่นยังไง` -> exact answer

### F. Constrained LLM Resolver เฉพาะเคสยาก

ใช้ LLM ได้ แต่ห้ามให้เดานอก candidate list

Prompt style:

```text
Given user query and candidate entities, choose:
- exact candidate id
- ambiguous
- unknown

You must not invent entities.
Return JSON only.
```

ใช้เฉพาะเมื่อ:

- rule scorer ยัง uncertain
- query เป็นภาษาอ้อม เช่น `เกมรถมาริโอ`, `cod ภาค battle royale`, `เกมผีหมู่บ้าน`

### G. Answerability Check Before RAG

ก่อนเข้า RAG/hybrid:

- candidate ต้องชัด
- retrieved evidence ต้อง match candidate
- answer type ต้องตรง operation

ถ้าไม่ครบ:

- clarification
- no-answer
- ไม่เข้า RAG แบบเปิดกว้าง

## อะไรไม่ควรทำ

- ไม่ควรเพิ่ม `if mario`, `if call of`, `if resident` ไปเรื่อย ๆ
- ไม่ควรให้ RAG เป็นตัวแก้ ambiguity ตั้งแต่แรก
- ไม่ควรให้ LLM เลือกเกมโดยไม่มี candidate list
- ไม่ควรตอบเกมหนึ่งเมื่อ query เป็น family และมีหลายเกมใน current catalog
- ไม่ควรใช้ session context เดิมถ้า query ใหม่มี target ใหม่ที่ชัดกว่า

## Recommendation สำหรับโปรเจกต์นี้

ควรทำลำดับนี้:

1. ทำ `Entity Resolver v2`
2. สร้าง candidate จาก data ทั้งหมด
3. เพิ่ม score + margin + reject option
4. ผูก resolver เข้า router / ambiguity gate / structured tools
5. ทำ clarification preview จาก candidates
6. กัน RAG/hybrid ไม่ให้ทำงานถ้า entity status ไม่ใช่ exact
7. เพิ่ม eval set สำหรับ entity ambiguity โดยเฉพาะ

## ตัวอย่างผลลัพธ์ที่ควรได้

### Query: `Call of เล่นยังไง`

```json
{
  "status": "incomplete",
  "candidates": [
    "Call of Duty: Modern Warfare III",
    "Call of Duty: Warzone"
  ]
}
```

Answer:

```text
คำว่า Call of ยังไม่ชัดครับ หมายถึงเกมไหน?
• Call of Duty: Modern Warfare III
• Call of Duty: Warzone
พิมพ์ชื่อเกมต่อได้เลย เช่น `Warzone เล่นยังไง`
```

### Query: `Mario เล่นยังไง`

Answer:

```text
Mario มีหลายเกมในรายการครับ หมายถึงเกมไหน?
• Mario Kart 8 Deluxe
• Mario Party Superstars
• New Super Mario Bros. U Deluxe
• Super Mario Odyssey
```

### Query: `Mario มีเกมอะไรบ้าง`

Answer:

```text
เกมตระกูล Mario ที่มีในรายการปัจจุบัน:
• Mario Kart 8 Deluxe
• Mario Party Superstars
• New Super Mario Bros. U Deluxe
• Super Mario Odyssey
```

## สรุปสุดท้าย

เทคนิคที่เหมาะที่สุดคือ:

`Data-driven Entity Linking + Candidate Ranking + Reject Option + Clarification`

ไม่ใช่เพิ่ม family guard ไปเรื่อย ๆ
