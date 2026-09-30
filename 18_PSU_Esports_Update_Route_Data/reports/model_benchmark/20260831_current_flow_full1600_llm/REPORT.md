# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-31T13:51:13
- Case bank: `data\eval\model_benchmark_1500.jsonl`
- Runs: 1

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | llm_scb10x_typhoon2.5-qwen3-4b | scb10x/typhoon2.5-qwen3-4b | 94.31% | 98.47 | 2.7053 | 4.7825 | 1820.6946 | 542 |

## Group Breakdown

### llm_scb10x_typhoon2.5-qwen3-4b (scb10x/typhoon2.5-qwen3-4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 95.83% | 98.17 | 1.5143 | 7.1936 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 0.838 | 3.713 |
| availability_game | 166 | 94.58% | 98.73 | 0.4386 | 0.647 |
| availability_machine_split | 4 | 50.0% | 83.0 | 0.3684 | 0.6274 |
| availability_service | 23 | 95.65% | 98.52 | 0.2987 | 0.4541 |
| competition_rules | 75 | 84.0% | 97.12 | 0.3484 | 0.4857 |
| compound | 89 | 98.88% | 99.37 | 1.3109 | 3.2362 |
| equipment | 58 | 100.0% | 99.48 | 3.9503 | 8.9387 |
| game_controls | 345 | 97.68% | 99.21 | 0.4645 | 0.6853 |
| game_detail | 18 | 83.33% | 94.33 | 1.9648 | 4.3033 |
| games | 158 | 72.78% | 93.16 | 1.943 | 4.657 |
| general_llm | 275 | 100.0% | 100.0 | 4.2001 | 6.2912 |
| members | 63 | 84.13% | 95.24 | 3.8331 | 10.6703 |
| policy_schedule_rules | 8 | 100.0% | 100.0 | 2.3901 | 6.7691 |
| reservation | 20 | 100.0% | 100.0 | 0.2659 | 0.4242 |
| schedule | 10 | 100.0% | 100.0 | 0.4789 | 1.369 |
| service_fee | 258 | 99.61% | 99.83 | 7.3861 | 0.5018 |

Top errors:
- `category_mismatch:knowledge`: 44
- `category_mismatch:events_news`: 21
- `category_mismatch:no_answer`: 7
- `category_mismatch:about_us`: 6
- `missing_any:แนวเกม|เกม Battle Royale`: 2
- `missing_any:แนวเกม|เกม Survival Horror`: 2
- `missing_any:ไม่มี|PC #01-#02`: 2
- `missing_any:แนวเกม|เกมยิง Tactical FPS แบบทีม 5v5`: 1

## How To Read

- ค่าเริ่มต้นของ benchmark รันเฉพาะ model เพื่อไม่เสียเวลาทำ baseline ซ้ำ
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
