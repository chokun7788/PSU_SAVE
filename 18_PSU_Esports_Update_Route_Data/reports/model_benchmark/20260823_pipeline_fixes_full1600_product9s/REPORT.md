# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-23T18:52:15
- Case bank: `data\eval\model_benchmark_1500.jsonl`
- Runs: 2

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | no_llm | No-LLM | 86.19% | 97.79 | 0.5111 | 0.9932 | 8.0346 | 0 |
| 2 | llm_scb10x_typhoon2.5-qwen3-4b | scb10x/typhoon2.5-qwen3-4b | 81.56% | 92.98 | 0.7198 | 1.6465 | 13.9026 | 411 |

## Group Breakdown

### no_llm (No-LLM)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 100.0% | 100.0 | 0.4682 | 0.9826 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 0.1832 | 0.4561 |
| availability_game | 166 | 100.0% | 100.0 | 0.4503 | 0.7326 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.3394 | 0.3989 |
| availability_service | 23 | 100.0% | 100.0 | 1.0147 | 4.4074 |
| competition_rules | 75 | 98.67% | 99.76 | 0.4045 | 0.6358 |
| compound | 89 | 100.0% | 100.0 | 2.0262 | 4.996 |
| equipment | 58 | 100.0% | 100.0 | 0.2584 | 0.3338 |
| game_controls | 345 | 100.0% | 100.0 | 0.4388 | 0.6306 |
| game_detail | 18 | 100.0% | 100.0 | 0.5227 | 0.7649 |
| games | 158 | 100.0% | 100.0 | 0.6584 | 0.9533 |
| general_llm | 275 | 20.0% | 87.2 | 0.2056 | 0.2724 |
| members | 63 | 100.0% | 100.0 | 0.2935 | 0.4357 |
| policy_schedule_rules | 8 | 100.0% | 100.0 | 0.1736 | 0.5987 |
| reservation | 20 | 100.0% | 100.0 | 2.7624 | 7.87 |
| schedule | 10 | 100.0% | 100.0 | 0.5901 | 1.6179 |
| service_fee | 258 | 100.0% | 100.0 | 0.302 | 0.4516 |

Top errors:
- `missing_any:latency|หน่วง`: 28
- `missing_any:เฟรม|ความละเอียด`: 28
- `missing_any:API|เชื่อมต่อ`: 28
- `missing_any:ขอบคุณ`: 28
- `missing_any:กิจกรรม`: 27
- `missing_any:คีย์บอร์ด|mechanical`: 27
- `missing_any:GPU|กราฟิก`: 27
- `missing_any:server|client`: 27

### llm_scb10x_typhoon2.5-qwen3-4b (scb10x/typhoon2.5-qwen3-4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 95.83% | 98.92 | 1.7519 | 8.0461 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 0.4359 | 1.4254 |
| availability_game | 166 | 100.0% | 100.0 | 0.4977 | 0.7613 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.3351 | 0.3647 |
| availability_service | 23 | 100.0% | 100.0 | 1.2542 | 4.8167 |
| competition_rules | 75 | 98.67% | 99.76 | 0.3917 | 0.605 |
| compound | 89 | 79.78% | 91.1 | 4.401 | 11.8388 |
| equipment | 58 | 100.0% | 100.0 | 0.2575 | 0.3376 |
| game_controls | 345 | 100.0% | 100.0 | 0.5331 | 0.6432 |
| game_detail | 18 | 100.0% | 100.0 | 0.5391 | 0.8471 |
| games | 158 | 100.0% | 100.0 | 0.4598 | 0.8293 |
| general_llm | 275 | 0.0% | 62.2 | 0.4493 | 0.6104 |
| members | 63 | 100.0% | 100.0 | 0.3496 | 0.4513 |
| policy_schedule_rules | 8 | 100.0% | 100.0 | 0.8689 | 1.4057 |
| reservation | 20 | 100.0% | 100.0 | 2.8019 | 8.0838 |
| schedule | 10 | 100.0% | 100.0 | 0.5883 | 1.613 |
| service_fee | 258 | 100.0% | 100.0 | 0.3006 | 0.4097 |

Top errors:
- `llm_required_but_unavailable`: 275
- `missing_any:latency|หน่วง`: 28
- `missing_any:เฟรม|ความละเอียด`: 28
- `missing_any:API|เชื่อมต่อ`: 28
- `missing_any:ขอบคุณ`: 28
- `missing_any:กิจกรรม`: 27
- `missing_any:คีย์บอร์ด|mechanical`: 27
- `missing_any:GPU|กราฟิก`: 27

## How To Read

- `No-LLM` คือ baseline ที่ปิด Local LLM เพื่อดูว่า rule/structured/RAG ตอบเองได้แค่ไหน
- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
