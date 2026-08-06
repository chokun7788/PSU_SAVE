# สรุป Model Benchmark สำหรับ PSU Esports Chatbot ณ 2026-07-31

## สถานะที่ทำแล้ว

1. สร้างรายการ model ต่ำกว่า 10B สำหรับทดสอบไว้ที่ `data/eval/model_benchmark_models_under_10b.json`
2. โหลด model ทั้ง 10 ตัวลง Drive D: ที่ `D:\OllamaModels`
3. เปิด Ollama แยกสำหรับ benchmark ที่ `http://127.0.0.1:11435`
4. สร้าง question bank แบบ deterministic จำนวน 1,600 คำถามไว้ที่ `data/eval/model_benchmark_1500.jsonl`
5. สร้าง runner ที่รันซ้ำได้ ไม่ต้อง generate คำถามใหม่ทุกครั้ง:
   - `tools/generate_model_benchmark_cases.py`
   - `tools/run_model_benchmark_eval.py`
   - `tools/setup_ollama_models_on_d.ps1`
6. รัน pilot benchmark แบบกระจายทุกหมวด `sample-per-group=2` รวม 34 คำถามต่อ run:
   - No-LLM 1 รอบ
   - LLM 10 model
   - report หลักอยู่ที่ `reports/model_benchmark/20260731_pilot_all_models_sample2/REPORT.md`

## Model ที่โหลดไว้แล้ว

| Model | ขนาดบน Ollama | หมายเหตุ |
|---|---:|---|
| `qwen3:4b` | 2.5 GB | Qwen3 รุ่นเล็ก ใช้กับภาษาไทยได้และเร็วพอควร |
| `qwen2.5:3b` | 1.9 GB | baseline เดิมของโปรเจกต์ |
| `qwen2.5:7b` | 4.7 GB | ใหญ่กว่า 3B คุณภาพควรดีขึ้น แต่ช้าขึ้น |
| `qwen3:8b` | 5.2 GB | คุณภาพดี แต่ latency สูงขึ้นชัด |
| `scb10x/llama3.2-typhoon2-3b-instruct` | 2.0 GB | Typhoon 2 3B เน้นไทย/อังกฤษ |
| `scb10x/llama3.1-typhoon2-8b-instruct` | 4.9 GB | Typhoon 2 8B เน้นไทย/อังกฤษ |
| `scb10x/typhoon2.5-qwen3-4b` | 2.5 GB | Typhoon 2.5 บน Qwen3 4B |
| `scb10x/typhoon2.1-gemma3-4b` | 2.6 GB | Typhoon 2.1 บน Gemma3 4B |
| `llama3.1:8b` | 4.9 GB | multilingual baseline |
| `sailor2:8b` | 5.2 GB | multilingual model สำหรับ South-East Asia |

## ผล Pilot Ranking

> หมายเหตุ: นี่เป็น pilot sample 34 คำถามต่อ run ยังไม่ใช่ full 1,600 case

| อันดับ | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec |
|---:|---|---:|---:|---:|---:|---:|
| 1 | `scb10x/typhoon2.5-qwen3-4b` | 91.18% | 98.06 | 1.6154 | 8.2408 | 12.9238 |
| 2 | `scb10x/llama3.2-typhoon2-3b-instruct` | 88.24% | 97.59 | 1.6568 | 7.6505 | 13.7547 |
| 3 | `qwen3:8b` | 91.18% | 97.47 | 3.9234 | 17.4288 | 31.0378 |
| 4 | `qwen2.5:7b` | 88.24% | 97.29 | 2.7487 | 12.4723 | 26.3079 |
| 5 | `qwen3:4b` | 88.24% | 97.29 | 3.0074 | 10.9457 | 20.3503 |
| 6 | `scb10x/llama3.1-typhoon2-8b-instruct` | 88.24% | 97.24 | 3.6175 | 15.5210 | 32.3055 |
| 7 | No-LLM | 85.29% | 97.12 | 0.2071 | 0.7069 | 1.9267 |
| 8 | `llama3.1:8b` | 85.29% | 96.76 | 3.5423 | 14.6532 | 30.0440 |
| 9 | `qwen2.5:3b` | 82.35% | 96.47 | 1.8532 | 8.3492 | 12.4075 |
| 10 | `sailor2:8b` | 88.24% | 96.26 | 4.2739 | 16.0565 | 35.3175 |
| 11 | `scb10x/typhoon2.1-gemma3-4b` | 85.29% | 90.06 | 12.5767 | 21.5377 | 40.1729 |

## ข้อสรุปจาก Pilot

1. ตัวที่น่าใช้ก่อนตอนนี้คือ `scb10x/typhoon2.5-qwen3-4b`
   - คะแนนรวมดีที่สุดใน pilot
   - latency เฉลี่ยต่ำสุดในกลุ่ม LLM
   - general LLM ผ่าน 2/2 ใน pilot

2. ตัวสำรองที่น่าลองคือ `scb10x/llama3.2-typhoon2-3b-instruct`
   - เร็วใกล้เคียงอันดับ 1
   - เป็นรุ่น 3B เน้นไทย
   - แต่มี 1 general case ที่ heuristic judge มองว่า keyword ไม่ครบ

3. `qwen3:8b` คุณภาพดีแต่ latency สูงกว่า
   - Avg sec สูงกว่า Typhoon 4B/3B ชัด
   - max เกิน 30 วินาทีใน pilot ทั้งที่ตั้ง timeout 20 วิ เพราะเวลารวมของ pipeline มี overhead หลายจุด ไม่ใช่เฉพาะ generate call

4. `qwen2.5:3b` ไม่ใช่ตัวที่ดีที่สุดใน pilot นี้
   - เร็วพอใช้ แต่ pass rate ต่ำกว่า Typhoon 4B/3B และ Qwen3 4B/8B
   - เหมาะเป็น fallback เบา ๆ มากกว่าเป็น model หลัก

5. `scb10x/typhoon2.1-gemma3-4b` ยังไม่น่าใช้เป็นตัวหลัก
   - ช้ามากเมื่อเทียบตัวอื่น
   - เจอ `general_llm_unavailable` ใน pilot

## ปัญหาที่เจอจาก Pilot

1. คำถาม `PC #01 มี Call of Duty: Warzone ไหม` และ `PC #02 มี Call of Duty: Warzone ไหม` ยังตอบไม่ตรง machine split
   - expected ควรสื่อว่า PC #01-#02 ไม่มี Warzone และ Warzone อยู่ PC #03-#10
   - ระบบปัจจุบันยังไป `structured_game_detail` และตอบระดับเกม/โซน ไม่ได้ตอบระดับเครื่อง

2. คำถาม `PC #01-#02 เล่นได้กี่คน` ถูก route ไป equipment
   - expected ควรตอบ capacity 1 คน
   - ปัจจุบัน route เป็น `structured_equipment_item`

3. เมื่อเปิด LLM บางคำถามที่ควรเป็น clarification/routing check ใช้เวลาสูงขึ้นมาก
   - เพราะ universal intent / tool router อาจเรียก LLM ในคำถามที่กำกวม
   - แม้สุดท้ายไม่ได้ให้ LLM ตอบ final answer

4. timeout 20 วิไม่ได้แปลว่า wall time จะไม่เกิน 20 วิเสมอ
   - เพราะหนึ่งคำถามอาจผ่านหลาย stage
   - มี overhead จาก preprocess, structured, deterministic, retrieval, validation และ LLM routing
   - ถ้า LLM call timeout 20 วิ บวก stage อื่น ๆ จะเห็น max เกิน 20 วิได้

5. No-LLM ยังเร็วมาก และตอบ factual ส่วนใหญ่ได้ดี
   - แต่ general question จะ decline ตามที่ตั้งใจ
   - ดังนั้น production ควรใช้ No-LLM/structured เป็นหลัก และเรียก LLM เฉพาะจุดที่จำเป็นจริง ๆ

## คำแนะนำ Model ตอนนี้

1. ใช้ `scb10x/typhoon2.5-qwen3-4b` เป็น candidate หลักสำหรับทดสอบต่อ
2. ใช้ `scb10x/llama3.2-typhoon2-3b-instruct` เป็น candidate สำรองถ้าต้องการลด latency
3. เก็บ `qwen3:4b` เป็น baseline เทียบกับ Typhoon Qwen3
4. ยังไม่ควรใช้ `scb10x/typhoon2.1-gemma3-4b` เป็น production default
5. `qwen3:8b`, `llama3.1:8b`, `sailor2:8b` ควรเก็บไว้เทียบคุณภาพ แต่ยังไม่น่าเป็น default ถ้า requirement ต้องเร็ว

## คำสั่งรัน

ตั้ง Ollama บน D: และตรวจ model:

```powershell
powershell -ExecutionPolicy Bypass -File tools\setup_ollama_models_on_d.ps1 -SkipPull
```

รัน pilot แบบที่ทำรอบนี้:

```powershell
python tools\run_model_benchmark_eval.py --sample-per-group 2 --output-dir reports\model_benchmark\pilot_all_models --ollama-host 127.0.0.1:11435 --ollama-url http://127.0.0.1:11435 --timeout-sec 20 --num-predict 128 --progress 16 --disable-health-manager
```

รันเต็ม 1,600 case ทุก model:

```powershell
python tools\run_model_benchmark_eval.py --output-dir reports\model_benchmark\full_all_models_1600 --ollama-host 127.0.0.1:11435 --ollama-url http://127.0.0.1:11435 --timeout-sec 20 --num-predict 256 --progress 100 --disable-health-manager
```

ถ้ารันเต็มแล้วหลุดกลางทาง ให้รันต่อ:

```powershell
python tools\run_model_benchmark_eval.py --resume --output-dir reports\model_benchmark\full_all_models_1600 --ollama-host 127.0.0.1:11435 --ollama-url http://127.0.0.1:11435 --timeout-sec 20 --num-predict 256 --progress 100 --disable-health-manager
```

## หมายเหตุสำคัญ

- full run ทุก model กับ 1,600 case อาจใช้เวลาหลายชั่วโมงหรือข้ามคืน
- runner มี checkpoint ที่ `partial_results.jsonl` ทุก 25 case
- report สุดท้ายจะสร้างเป็น `REPORT.md` ใน output folder
- heuristic judge ใช้คัดปัญหาเร็ว ไม่ใช่ human approval สุดท้าย
- ปัญหาหลักที่ควรแก้ก่อน full benchmark คือ machine-level availability ของ PC #01-#02 / PC #03-#10 และ capacity query

## แหล่งอ้างอิง Model

- Qwen3 บน Ollama: https://ollama.com/library/qwen3
- SCB10X/Typhoon บน Ollama: https://ollama.com/scb10x
- Llama 3.1 บน Ollama: https://ollama.com/library/llama3.1
- Sailor2 บน Ollama: https://ollama.com/library/sailor2
- Typhoon local Ollama tutorial: https://opentyphoon.ai/blog/en/typhoon-local-ollama-tutorial
- Typhoon 2 Thai LLM blog: https://www.scb10x.com/en/blog/introducing-typhoon-2-thai-llm
