# Focused Model Eval - Top 4 Models ณ 2026-07-31

## รอบนี้รันอะไร

- ใช้ question bank เดิม `data/eval/model_benchmark_1500.jsonl`
- เลือก sample แบบกระจายทุกหมวด `sample-per-group=25`
- ได้ทั้งหมด 336 คำถามต่อ run
- รันทั้งหมด 5 run:
  - No-LLM
  - `scb10x/typhoon2.5-qwen3-4b`
  - `scb10x/llama3.2-typhoon2-3b-instruct`
  - `qwen3:4b`
  - `qwen2.5:7b`
- ใช้ timeout 20 วินาที และ `num_predict=128`
- raw report อยู่ที่ `reports/model_benchmark/20260731_focused_top4_sample25/REPORT.md`

## ผล ranking รอบ focused

| อันดับ | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec |
|---:|---|---:|---:|---:|---:|---:|
| 1 | `scb10x/typhoon2.5-qwen3-4b` | 93.15% | 98.43 | 1.3615 | 5.7947 | 15.9192 |
| 2 | `qwen3:4b` | 92.86% | 98.33 | 2.6119 | 8.0819 | 17.8010 |
| 3 | `scb10x/llama3.2-typhoon2-3b-instruct` | 91.96% | 98.09 | 1.3364 | 6.0723 | 15.3076 |
| 4 | `qwen2.5:7b` | 92.26% | 97.99 | 2.0514 | 9.4357 | 24.4974 |
| 5 | No-LLM | 86.01% | 97.10 | 0.2875 | 1.2332 | 14.3892 |

## สรุปแบบไม่อวย

1. `scb10x/typhoon2.5-qwen3-4b` ยังเป็นตัวที่น่าใช้สุดตอนนี้
   - ชนะทั้ง pilot และ focused eval
   - avg latency ต่ำมากเมื่อเทียบคุณภาพ
   - p95 ยังอยู่ประมาณ 5.8 วิใน sample นี้

2. `qwen3:4b` คุณภาพใกล้มาก
   - pass rate และ avg score ใกล้อันดับ 1
   - แต่ช้ากว่าเกือบ 2 เท่าในค่าเฉลี่ย

3. `scb10x/llama3.2-typhoon2-3b-instruct` เร็วมากและเหมาะเป็นตัวสำรอง
   - avg sec ดีสุดเล็กน้อย
   - แต่ general LLM pass rate ต่ำกว่าอันดับ 1/2

4. `qwen2.5:7b` ยังโอเค แต่ latency tail แย่กว่า
   - max ไปถึง 24.5 วิ
   - ถ้า requirement ต้องไม่เกิน 20 วิจริง ๆ ยังต้องระวัง

5. No-LLM ยังเร็วที่สุด แต่ตอบ general knowledge ไม่ได้ตามที่ตั้งใจ
   - เหมาะเป็น backbone หลักของ factual PSU
   - ไม่พอถ้าผู้ใช้ถามคำถามทั่วไปแล้วอยากให้ตอบได้

## หมวดที่ผ่านดี

หมวดเหล่านี้ผ่านแทบ 100% ใน top models:

- `competition_rules`
- `compound`
- `equipment`
- `game_controls`
- `game_detail`
- `games`
- `members`
- `reservation`
- `schedule`
- `service_fee`

แปลว่าปัญหาหลักตอนนี้ไม่ได้อยู่ที่ “model ตอบมั่วทุกหมวด” แต่เป็น logic routing/structured บางกลุ่ม

## หมวดที่ยังมีปัญหาจริง

1. `availability_machine_split`
   - pass rate 0% ทุก model
   - เพราะเป็น bug logic ไม่ใช่ปัญหา model
   - ตัวอย่าง:
     - `PC #01 มี Call of Duty: Warzone ไหม`
     - `PC #03 มี TEKKEN 8 ไหม`
   - ควรตอบระดับเครื่องว่า PC #01-#02 ไม่มี Warzone / PC #03-#10 ไม่มี TEKKEN 8

2. `availability_service`
   - pass rate ประมาณ 38-48%
   - เคสที่พังคือคำถาม capacity / รายการเกมระดับ zone
   - ตัวอย่าง:
     - `PC #01-#02 เล่นได้กี่คน`
     - `PlayStation 5 #01-#02 เล่นได้กี่คน`
     - `PC Zone รายการเกมมีอะไรบ้าง`
   - บางคำถามถูก route ไป equipment / schedule / clarification ผิด

3. `policy_schedule_rules`
   - pass rate 75%
   - บางคำถาม policy/rule/schedule ยังโดน route ไม่ตรง

4. `general_llm`
   - top models ผ่าน 84-88%
   - ยังไม่เต็ม 100 เพราะบางคำตอบไม่ติด keyword ที่ judge คาดไว้ หรือ model ตอบไม่ตรงพอ
   - ต้องใช้ human review เพิ่มก่อนเลือก default production

## ข้อสรุปเรื่อง “ดีเฉพาะบางเคสไหม”

ตอนนี้ตอบได้ว่า:

- ใช่ มีบางหมวดที่ผลดีมากจนเกือบนิ่งแล้ว
- แต่มีบางหมวดที่พังซ้ำทุก model ซึ่งแปลว่าเป็นปัญหา logic ไม่ใช่เลือก model ผิด
- ผล focused eval ทำให้มั่นใจกว่า pilot มาก เพราะรัน 336 เคสต่อ run แทน 34 เคส
- แต่ยังไม่ใช่ full proof 100% เพราะยังเป็น sample ไม่ใช่ 1,600 ทั้งหมด

## Recommendation หลัง focused eval

1. แก้ logic ก่อน ไม่ควรรีบ full benchmark ทันที
   - machine-level availability
   - capacity query
   - zone game list query
   - policy/schedule/rule conflict

2. หลังแก้ logic แล้วค่อยรัน focused eval ซ้ำกับ top 3:
   - `scb10x/typhoon2.5-qwen3-4b`
   - `qwen3:4b`
   - `scb10x/llama3.2-typhoon2-3b-instruct`

3. ถ้าผ่านดี ค่อยรัน full 1,600 case กับ 2 model สุดท้าย

## หมายเหตุเรื่อง LLM Call

ใน raw report ช่อง `LLM calls` เป็นการนับ metadata event จาก trace บางส่วน ไม่ควรตีความว่า No-LLM ยิง model จริงทุกครั้ง  
No-LLM ยังคือรอบที่ปิด `experimental_allow_llm` และคำตอบทั่วไปจบด้วย disabled/fallback ตามที่ออกแบบไว้
