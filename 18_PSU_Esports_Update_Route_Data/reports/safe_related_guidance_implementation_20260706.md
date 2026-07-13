# Safe Related Guidance Implementation

วันที่: 2026-07-06

## สรุปสั้น

เพิ่มชั้นตอบคำถามเชิงแนะนำ/เปรียบเทียบแบบปลอดภัย เพื่อให้ chatbot ตอบคำถามที่เกี่ยวข้องกันได้กว้างขึ้น โดยยังยึดข้อมูลจริงจากฐานข้อมูลเดิม

สิ่งนี้เป็น `safe related guidance` หรือ RAG-style answer จากข้อมูล curated/structured ที่มีอยู่ ไม่ใช่ LLM อิสระ และไม่เดาข้อมูลนอกฐาน

ยังไม่ได้ deploy และยังไม่ได้ sync ไปโฟลเดอร์ deploy

## ไฟล์ที่แก้

```text
app/pipeline/router.py
app/runtime/fast_answer.py
```

## สิ่งที่เพิ่ม

### 1. Route ใหม่

เพิ่ม helper:

```text
_looks_like_related_guidance_query()
```

route:

```text
equipment / related_guidance
```

ใช้กับคำถามแนว:

```text
แนะนำ...
ควรเลือก...
เหมาะกับ...
ต่างกันยังไง...
ไปกับเพื่อน...
อยากเล่นเกมแนว...
```

### 2. Guard กันชนกับกติกาการแข่งขัน

ตอนแรก regression fail 3 เคส เพราะคำถามกติกาเช่น `มาสาย`, `แบ่งสายการแข่งขัน`, `เข้าแข่งก่อนแมตช์` ถูกดึงเข้า related guidance

จึงเพิ่ม guard ให้ related guidance ไม่รับคำถามที่มีสัญญาณกติกา/การแข่งขัน เช่น:

```text
กติกา
เข้าแข่ง
แมตช์
มาสาย
แบ่งสาย
ตัดสิทธิ์
ปรับแพ้
โทษ
ทีม
สมาชิก
เช็คอิน
```

ผลคือคำถามกติกากลับไปเข้า:

```text
competition_rules / competition_rules_lookup
```

### 3. Fast path ใหม่

เพิ่ม:

```text
_related_guidance_answer()
```

mode:

```text
pipeline:related_guidance_fast_path
```

คำตอบดึงจากข้อมูลจริงใน:

```text
ZONE_DETAILS
SUPPORTED_GAME_CATALOG / game catalog
SERVICE_FEE_SUMMARY เฉพาะเมื่อจำเป็นต้องเตือนเรื่องราคา
```

เพิ่ม source metadata:

```text
home_our_games
```

เพื่อให้ sources object ตรงกับคำตอบ:

```text
https://esports.phuket.psu.ac.th/home
https://esports.phuket.psu.ac.th/Services/our-games
```

## ตัวอย่างที่รองรับแล้ว

```text
ถ้าอยากเล่นเกมขยับตัวควรเล่นโซนไหน
VR กับ Cockpit ต่างกันยังไง
อยากไปกับเพื่อน 4 คนควรเลือกอะไร
มีเกมแนวจังหวะไหม
ศูนย์นี้เหมาะกับนักเรียนไหม
อยากเล่นเกมขับรถควรเลือกอะไร
มีเกมแนว FPS หรือ MOBA ไหม
```

ตัวอย่างคำตอบ:

- เกมขยับตัว/จังหวะ: แนะนำ VR Zone เพราะมี Beat Saber และบอกทางเลือก Nintendo Switch Sports / Ring Fit Adventure จาก catalog
- VR vs Cockpit: เปรียบเทียบจากโซน อุปกรณ์ และเกมที่ยืนยันได้
- ไปกับเพื่อน 4 คน: แนะนำ Nintendo Switch / VR / PC ตามสไตล์ พร้อมไม่คำนวณราคา PC เพราะยังไม่มีราคา PC ที่ยืนยันได้
- เกมขับรถ: แนะนำ Cockpit Zone และ Gran Turismo 7

## Ad-hoc test

Questions:

```text
reports/ad_hoc_questions_safe_related_guidance_20260706.txt
```

Latest report:

```text
reports/ad_hoc_pipeline_results_safe_related_guidance_fix3_20260706.md
reports/ad_hoc_pipeline_results_safe_related_guidance_fix3_20260706.jsonl
```

ผล:

```text
questions=10
routes:
- competition_rules/competition_rules_lookup: 1
- equipment/related_guidance: 7
- games/game_availability_lookup: 1
- service_fee/service_fee_query: 1
```

Regression guard ที่ตรวจ:

- `VR ราคาเท่าไหร่` ยังเข้า service fee calculator
- `Minecraft เล่นได้ไหม` ยัง no-answer แบบ unknown game
- `Tekken 8 เกมนึงมี 3 rounds ใช่ไหม` ยังเข้า competition rules

## Regression

Compile:

```text
py_compile OK
```

Validate:

```text
VALIDATION OK
- rule files: 8
- rules: 77
- curated rows: 324
- service fee sanity: OK
```

GT360:

```text
Total: 360
PASS: 360
FAIL: 0
Pass rate: 100.00%
```

Report:

```text
reports/pipeline_ground_truth_report_safe_related_guidance_fix3_gt360_20260706.md
reports/pipeline_ground_truth_results_safe_related_guidance_fix3_gt360_20260706.jsonl
```

Competition challenger v2:

```text
Total: 369
PASS: 369
FAIL: 0
Pass rate: 100.00%
```

Report:

```text
reports/pipeline_ground_truth_report_safe_related_guidance_fix3_comp_v2_20260706.md
reports/pipeline_ground_truth_results_safe_related_guidance_fix3_comp_v2_20260706.jsonl
```

## ข้อจำกัด

- ยังไม่ใช่ LLM fallback จริง
- ยังไม่ตอบเรื่องนอกฐานข้อมูล
- ยังไม่สร้างคำตอบใหม่จากเอกสารอิสระ
- ยังไม่ทำ vector search
- ถ้าคำถามเชิงแนะนำอยู่นอกข้อมูลศูนย์ ควร no-answer หรือถามกลับ

## ขั้นต่อไป

1. ถ้าจะให้กว้างขึ้นอีก ให้เพิ่ม curated facts สำหรับ scenario แนะนำ เช่น กลุ่มผู้เล่น/แนวเกม/จำนวนคน/งบประมาณ
2. ถ้าจะใช้ LLM จริง ให้ทำเป็น optional local backend หรือ external backend ไม่ควรรันบน Vercel โดยตรง
3. LLM prompt ต้องบังคับตอบจาก retrieved context เท่านั้น และ no-answer ถ้า context ไม่พอ
4. ก่อน deploy ให้ sync ไปโฟลเดอร์ `20` แล้วผู้ใช้กด deploy เองตามข้อตกลงล่าสุด

