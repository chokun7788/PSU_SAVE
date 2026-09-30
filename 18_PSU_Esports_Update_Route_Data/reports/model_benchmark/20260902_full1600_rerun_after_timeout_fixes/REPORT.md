# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-09-02T18:55:42
- Case bank: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\model_benchmark_1500.jsonl`
- Runs: 1

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | llm_scb10x_typhoon2.5-qwen3-4b | scb10x/typhoon2.5-qwen3-4b | 94.12% | 98.55 | 0.8106 | 3.0857 | 8.0421 | 470 |

## Group Breakdown

### llm_scb10x_typhoon2.5-qwen3-4b (scb10x/typhoon2.5-qwen3-4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 95.83% | 98.58 | 0.9032 | 4.1558 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 0.7548 | 3.462 |
| availability_game | 166 | 93.37% | 98.54 | 0.3336 | 0.4477 |
| availability_machine_split | 4 | 50.0% | 83.0 | 0.2722 | 0.3567 |
| availability_service | 23 | 95.65% | 98.52 | 0.2363 | 0.4149 |
| competition_rules | 75 | 84.0% | 97.12 | 0.3744 | 0.4988 |
| compound | 89 | 100.0% | 100.0 | 0.4139 | 0.5184 |
| equipment | 58 | 98.28% | 99.72 | 1.8236 | 3.8562 |
| game_controls | 345 | 95.65% | 98.67 | 0.3528 | 0.5715 |
| game_detail | 18 | 83.33% | 94.33 | 1.747 | 4.1615 |
| games | 158 | 71.52% | 93.06 | 1.8086 | 4.42 |
| general_llm | 275 | 99.64% | 99.94 | 1.6826 | 3.1726 |
| members | 63 | 100.0% | 100.0 | 0.2562 | 1.4511 |
| policy_schedule_rules | 8 | 100.0% | 100.0 | 2.2964 | 7.4095 |
| reservation | 20 | 95.0% | 99.2 | 1.5124 | 3.8818 |
| schedule | 10 | 100.0% | 100.0 | 1.5146 | 4.0244 |
| service_fee | 258 | 99.61% | 99.88 | 0.2196 | 0.3645 |

Top errors:
- `category_mismatch:knowledge`: 39
- `category_mismatch:events_news`: 21
- `category_mismatch:clarification`: 13
- `mode_mismatch:pipeline:ambiguity_clarification`: 5
- `missing:Overcooked 2`: 2
- `missing_any:แนวเกม|เกม Battle Royale`: 2
- `missing_any:แนวเกม|เกม Survival Horror`: 2
- `missing_any:ไม่มี|PC #01-#02`: 2

## How To Read

- ค่าเริ่มต้นของ benchmark รันเฉพาะ model เพื่อไม่เสียเวลาทำ baseline ซ้ำ
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
