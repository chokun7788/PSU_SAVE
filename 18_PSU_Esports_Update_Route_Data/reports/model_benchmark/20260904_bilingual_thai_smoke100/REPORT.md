# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-09-04T10:09:49
- Case bank: `data\eval\model_benchmark_1500.jsonl`
- Runs: 1

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | llm_scb10x_typhoon2.5-qwen3-4b | scb10x/typhoon2.5-qwen3-4b | 98.0% | 99.41 | 1.6652 | 4.4444 | 8.0179 | 31 |

## Group Breakdown

### llm_scb10x_typhoon2.5-qwen3-4b (scb10x/typhoon2.5-qwen3-4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 1 | 100.0% | 100.0 | 0.0401 | 0.0401 |
| ambiguous_controls | 1 | 100.0% | 100.0 | 2.545 | 2.545 |
| availability_game | 10 | 100.0% | 100.0 | 0.7944 | 2.7952 |
| availability_machine_split | 1 | 100.0% | 100.0 | 2.6613 | 2.6613 |
| availability_service | 1 | 100.0% | 100.0 | 0.1426 | 0.1426 |
| competition_rules | 4 | 100.0% | 100.0 | 1.2166 | 2.9867 |
| compound | 5 | 100.0% | 100.0 | 0.4389 | 0.6797 |
| equipment | 3 | 100.0% | 100.0 | 0.2665 | 0.3562 |
| game_controls | 21 | 95.24% | 99.14 | 1.4065 | 2.8741 |
| game_detail | 1 | 100.0% | 100.0 | 2.8612 | 2.8612 |
| games | 9 | 100.0% | 100.0 | 3.6111 | 7.5193 |
| general_llm | 17 | 94.12% | 97.59 | 4.3627 | 6.3423 |
| members | 7 | 100.0% | 100.0 | 0.0918 | 0.1746 |
| policy_schedule_rules | 1 | 100.0% | 100.0 | 0.1255 | 0.1255 |
| reservation | 1 | 100.0% | 100.0 | 0.1431 | 0.1431 |
| schedule | 1 | 100.0% | 100.0 | 0.1631 | 0.1631 |
| service_fee | 16 | 100.0% | 100.0 | 0.3243 | 0.4125 |

Top errors:
- `category_mismatch:clarification`: 1
- `missing_any:latency|หน่วง`: 1
- `llm_required_but_unavailable`: 1

## How To Read

- ค่าเริ่มต้นของ benchmark รันเฉพาะ model เพื่อไม่เสียเวลาทำ baseline ซ้ำ
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
