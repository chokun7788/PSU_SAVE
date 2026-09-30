# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-09-04T10:34:17
- Case bank: `data\eval\model_benchmark_1500.jsonl`
- Runs: 1

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | llm_scb10x_typhoon2.5-qwen3-4b | scb10x/typhoon2.5-qwen3-4b | 98.0% | 99.45 | 0.8816 | 2.988 | 8.3231 | 488 |

## Group Breakdown

### llm_scb10x_typhoon2.5-qwen3-4b (scb10x/typhoon2.5-qwen3-4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 100.0% | 100.0 | 2.0325 | 6.647 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 1.3704 | 7.0486 |
| availability_game | 166 | 95.78% | 99.07 | 0.431 | 0.6509 |
| availability_machine_split | 4 | 50.0% | 83.0 | 0.2893 | 0.3395 |
| availability_service | 23 | 100.0% | 100.0 | 0.3648 | 0.4089 |
| competition_rules | 75 | 98.67% | 99.76 | 1.9187 | 2.9246 |
| compound | 89 | 100.0% | 100.0 | 0.675 | 0.9546 |
| equipment | 58 | 100.0% | 100.0 | 0.3681 | 0.3269 |
| game_controls | 345 | 95.65% | 98.67 | 0.4077 | 0.6224 |
| game_detail | 18 | 83.33% | 95.22 | 1.3271 | 3.065 |
| games | 158 | 98.73% | 99.67 | 2.459 | 3.5006 |
| general_llm | 275 | 99.64% | 99.94 | 1.3775 | 2.0992 |
| members | 63 | 100.0% | 100.0 | 0.2285 | 0.2818 |
| policy_schedule_rules | 8 | 100.0% | 100.0 | 3.6343 | 8.3231 |
| reservation | 20 | 100.0% | 100.0 | 0.3098 | 0.496 |
| schedule | 10 | 100.0% | 100.0 | 0.184 | 0.2439 |
| service_fee | 258 | 99.61% | 99.88 | 0.2473 | 0.3464 |

Top errors:
- `category_mismatch:clarification`: 14
- `category_mismatch:knowledge`: 12
- `mode_mismatch:pipeline:ambiguity_clarification`: 5
- `category_mismatch:events_news`: 2
- `missing_any:ไม่มี|PC #01-#02`: 2
- `missing:Overcooked 2`: 1
- `missing_any:แนวเกม|เกม Co-op ทำอาหาร`: 1
- `category_mismatch:no_answer`: 1

## How To Read

- ค่าเริ่มต้นของ benchmark รันเฉพาะ model เพื่อไม่เสียเวลาทำ baseline ซ้ำ
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
