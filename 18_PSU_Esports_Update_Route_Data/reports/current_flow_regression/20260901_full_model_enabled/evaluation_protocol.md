# วิธีทดสอบและอ่านผลรอบ 2026-09-01

## ขอบเขต

- FAQ เดิม 1,600 ข้อจาก `model_benchmark_1500.jsonl` ชื่อไฟล์มี 1500 แต่ข้อมูลจริงมี 1,600 ข้อ
- Keyboard anomaly 500 ข้อจาก `keyboard_input_anomaly_ground_truth_500_20260830.jsonl`
- Canonical Pilot อีก 16 ข้อเพื่อยืนยันการเรียกข้อมูลใหม่โดยตรง ไม่รวมกับคะแนน 1,600/500
- เปิดใช้ Local Model ใน Flow ทุกชุด ไม่มีการรัน No-LLM baseline
- การเปิด Model ไม่ได้หมายถึงบังคับสร้างคำตอบด้วย LLM ทุกข้อ: Fast/Structured และ Guard ยังข้ามโมเดลได้ตามนโยบาย
- FAQ/keyboard ส่วนใหญ่ตรวจเส้นทางเดิม ส่วน Pilot มีเกมและกฎสมมติรวมสอง records ไม่ใช่ฐานข้อมูล PSU ที่ครบถ้วน

## การตั้งค่าทดลอง

| ส่วน | ค่า |
|---|---|
| Local LLM | `scb10x/typhoon2.5-qwen3-4b` ผ่าน Ollama ที่ localhost |
| Embedding | `psu-bge-m3:q8_0`, 1,024 dimensions |
| Generative context | 2,048 tokens สำหรับ general/intent; 3,072 สำหรับ facts/canonical |
| LLM calls | จำกัด 2 ครั้งต่อ request |
| Model-first / RAG | เปิด |
| Facts/RAG composer | เปิด แต่ผ่าน gate ก่อนใช้ |
| LLM tool router | ปิดตามค่าทดสอบเดิม |
| Request budget | 9 วินาที; ประเมินเป้าหมายผู้ใช้ที่ไม่เกิน 10 วินาที |
| Guard | RuntimeInputQualityGuard จริง, `enforce`, repeat policy `ask_retype` |
| Guard thresholds | layout 0.39; repeat 0.55 |
| Canonical | เปิดเฉพาะฐาน SQLite สมมติในโฟลเดอร์ผลทดสอบ |
| Hardware ที่รันจริง | RTX 4050 Laptop GPU, 6,141 MiB VRAM |

นี่คือ **การทดลองเปิด Guard + Canonical Pilot** ไม่ใช่ค่าตั้งต้นของเว็บจริง ซึ่ง Guard ยังเป็น `shadow` และ Canonical เป็น feature flag ที่ไม่ได้เปิดให้อัตโนมัติ การรันนี้ไม่แก้ไฟล์ตั้งค่าเว็บ ไม่เผยแพร่ข้อมูลทดลอง และไม่เปลี่ยนฐานข้อมูลจริง

เครื่องที่ทดสอบไม่ใช่เครื่อง RTX 5060 8GB ที่เคยกำหนดไว้สำหรับ Production จึงไม่ควรนำความเร็วไปคาดการณ์เครื่องเป้าหมายโดยตรง

## ขั้นตอนต่อข้อ

```text
เริ่ม request_deadline(9)
  -> RuntimeInputQualityGuard.inspect(original input)
  -> ถ้าต้องพิมพ์ใหม่: คืนข้อความจริงจาก Guard และหยุดเส้นทางตอบ
  -> ถ้าอนุญาต: resolve_question_with_context(input, history=[])
  -> answer_question_pipeline_debug(..., allow_llm=True, rag_fallback=True)
  -> เก็บผลเต็ม + validation + evidence/hits + trace + decision artifact
  -> ประเมิน contract เดิม, เวลา, และผลของ Guard แยกกัน
```

ทำทีละข้อใน worker เพื่อไม่ให้สองชุดแย่ง GPU กัน ไม่ได้ทดสอบ HTTP admission queue, concurrent users, session history, browser rendering หรือ network latency ข้อมูลเวลาที่แสดงคือ backend call ในเครื่องนี้เท่านั้น

## Warmup และ Watchdog

ก่อนเริ่มวัดข้อแรก โหลดข้อมูลและอุ่นโมเดล โดยแยกเวลานี้ใน `startup_XXX.json` หลัง worker ถูกตัดจะ warmup worker ใหม่และแยกเวลาเช่นเดียวกัน

Parent process รอคำตอบไม่เกิน 30 วินาทีต่อข้อ ถ้าค้าง:

1. เก็บ diagnostic stack เมื่อทำได้ใน `worker_XXX.log`
2. บันทึก `status=harness_timeout`, `answer=""`, `right_censored=true`
3. หยุดเฉพาะ worker ของการทดลอง แล้วสร้าง worker ใหม่
4. รันข้อต่อไป ไม่มีการลบหรือเปลี่ยนผลที่ล้มเหลว

`harness_timeout` **ไม่ใช่ข้อความที่ Chatbot ส่งกลับผู้ใช้** และไม่ได้พิสูจน์ว่า Production มี hard deadline ที่ทำงานได้ การหยุด worker ก็ไม่รับรองว่า Ollama ยกเลิกงาน GPU ไปแล้ว

เวลา 30 วินาทีของข้อดังกล่าวเป็นเวลาเมื่อหยุดสังเกต ไม่ใช่เวลาที่ระบบตอบเสร็จ ค่าเฉลี่ย/P95 ที่รวมข้อถูกตัดจึงห้ามนำไปเทียบกับการรันเดิมที่ปล่อยให้จบเองแล้วสรุปว่าเร็วขึ้น

`worker_crash` หมายถึง worker ปิดก่อนส่งผล ต้องตรวจ log เพิ่ม โดยยังไม่สรุปว่าเกิดจาก application, Python runtime หรือ diagnostic instrumentation

## วิธีให้คะแนน

### FAQ

- `legacy_judge`: ใช้ตัวตรวจเดียวกับการทดสอบเดิม เช่น category, mode และคำที่ต้องมี/ห้ามมี
- `strict_passed`: legacy ผ่าน, validation ผ่าน และตอบเสร็จไม่เกิน 10 วินาที
- `text_contract_passed`: ตรวจข้อกำหนดข้อความบางส่วนแยกจาก route ไม่ใช่คะแนนความหมายหรือข้อเท็จจริง
- ข้อที่ runtime ให้ `validation.ok=true` ยังอาจตอบผิดเรื่องได้ เพราะตัวตรวจภายในมีขอบเขตจำกัด
- การไม่พบคำตาม substring อาจเกิดจากการเรียบเรียงใหม่ที่มีความหมายถูกต้อง หรืออาจเกิดจากการตอบผิดจริง ต้องแยกด้วยการอ่านคำตอบและหลักฐาน

### Keyboard 500

- วัด detection ของ keyboard layout และ repeated character แยกเป็น TP/FP/FN/TN
- เทียบ block/action กับ label เดิมโดยไม่แก้ label
- label เดิมของตัวอักษรซ้ำส่วนหนึ่งเป็น warn/continue แต่ค่าทดลองปัจจุบันขอให้พิมพ์ใหม่ จึงมี policy disagreement ที่ไม่ใช่ detector error เสมอไป
- คำตอบหลังผ่าน Guard วัดกับ source FAQ contract เฉพาะข้อที่มี `source_case_id`
- ข้อที่ไม่มี source gold หรือถูก Guard สกัด ไม่ถูกนับว่าตอบ FAQ ถูกจากการไม่มีข้อผิดพลาดของข้อความ
- การขอพิมพ์ใหม่ตามนโยบาย กับการตอบเนื้อหาถูก เป็นคนละตัวชี้วัด

### Canonical 16

ตรวจ mode, ข้อความที่ต้องมี/ห้ามมี, validation และเวลา จากข้อมูลสมมติที่รู้ contract เป็น development acceptance tests ไม่ใช่ความแม่นยำบนข้อมูลใหม่ที่ไม่เคยเห็นจำนวนมาก

## การเทียบผลเก่า

Baseline คือรอบวันที่ 2026-08-31:

- FAQ เดิมไม่ผ่าน RuntimeInputQualityGuard ก่อนเข้า Pipeline
- Keyboard เดิมใช้ detector prototype ที่ฝึก profile จากคำถาม FAQ ในชุดประเมิน จึงไม่ใช่ detector/runtime profile เดียวกับรอบนี้
- วันที่รัน, cache, model context, health state และการ restart worker ต่างกัน
- Canonical Pilot เพิ่มการรับผิดชอบคำถามรายชื่อ/จำนวนเกม แต่ฐานทดลองยังไม่ครอบคลุมรายชื่อทั้งหมด

รายงานจะแสดงคำถามเดิมตาม ID ที่เคยผ่านแล้วตก และเคยตกแล้วผ่าน แต่ไม่อ้างว่าเป็น controlled A/B ที่เปลี่ยนตัวแปรเดียว

## ไฟล์ที่เก็บ

| ไฟล์ | เนื้อหา |
|---|---|
| `manifest.json` | การตั้งค่า, รายชื่อโมเดล, hardware, ข้อจำกัด |
| `cases_manifest.json` | โจทย์และ label ที่ใช้ รวม Pilot |
| สำเนา dataset `.jsonl` | ข้อมูลก่อนรันที่ไม่แก้ label |
| `results.jsonl` | หนึ่งข้อหนึ่งบรรทัด: คำถาม คำตอบ เวลา Guard Trace hits และผล judge |
| `worker_XXX.log` | console และ stack ตอนค้าง/ล่ม |
| `startup_XXX.json` | เวลาโหลด cache/model และ profile Guard |
| `progress.json` | checkpoint ระหว่างรัน ไม่ใช่รายงานสุดท้าย |
| `summary.json` | ผลรวมเมื่อจบ พร้อมจำนวนครบ/ไม่ครบ |
| `fingerprints_before.json`, `fingerprints_after.json` | SHA-256 ของ source/data ที่ตรวจเพื่อจับการเปลี่ยนระหว่างรัน |
| `questions_answers.md` | ดัชนีไปยังคำถาม-คำตอบทุกข้อ แบ่งไฟล์ละไม่เกิน 100 ข้อ |
| `analysis/metrics.json` | เปรียบเทียบ baseline, กลุ่มปัญหา, เวลาแต่ละ stage |
| `analysis/per_case_analysis.jsonl` | ข้อสังเกตและข้อเสนอสำหรับทุกข้อ แยกจาก raw output |
| `analysis/cases_requiring_review.md` | ข้อที่ต้องตรวจ พร้อมโจทย์ คำตอบ ข้อกำหนด และแนวทางตรวจต่อ |
| `analysis/guard_span_diagnostics.jsonl` | diagnostic replay ของ Guard ภายหลังรัน ไม่มีการสร้างคำตอบใหม่ |

Stage timing บางส่วนซ้อนกัน และบางขั้นไม่มี timer จึงใช้หาจุดช้าได้แต่ห้ามบวกทุก stage แล้วถือเป็นเวลา request อย่างแม่นยำ ส่วน `llm_calls` มีทั้งการเรียกและการข้ามเพราะ health/budget ต้องอ่าน decision ก่อนนับเป็น successful model call

ผลจากสคริปต์จัดกลุ่มสาเหตุเป็นการวิเคราะห์เบื้องต้นจาก Trace ไม่ใช่หลักประกันว่าอ่านความหมายและตรวจความจริงครบทุกประโยค
