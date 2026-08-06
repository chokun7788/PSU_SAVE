# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-04T22:28:41
- Case bank: `data\eval\model_benchmark_1500.jsonl`
- Runs: 2

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | no_llm | No-LLM | 85.9% | 97.42 | 0.4679 | 0.8809 | 7.8146 | 0 |
| 2 | llm_scb10x_typhoon2.5-qwen3-4b | scb10x/typhoon2.5-qwen3-4b | 85.6% | 94.79 | 1.1124 | 4.3961 | 29.6274 | 228 |

## Group Breakdown

### no_llm (No-LLM)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 15 | 100.0% | 100.0 | 0.7825 | 3.8593 |
| ambiguous_controls | 3 | 100.0% | 100.0 | 0.1414 | 0.3098 |
| availability_game | 103 | 100.0% | 100.0 | 0.4686 | 0.7224 |
| availability_machine_split | 2 | 100.0% | 100.0 | 0.315 | 0.3518 |
| availability_service | 14 | 100.0% | 100.0 | 1.0712 | 4.1854 |
| competition_rules | 46 | 100.0% | 100.0 | 0.3112 | 0.5172 |
| compound | 55 | 100.0% | 100.0 | 0.917 | 1.4244 |
| equipment | 36 | 100.0% | 100.0 | 0.2367 | 0.3147 |
| game_controls | 215 | 100.0% | 100.0 | 0.4031 | 0.6053 |
| game_detail | 11 | 100.0% | 100.0 | 0.4994 | 0.7568 |
| games | 98 | 100.0% | 100.0 | 0.6379 | 0.9054 |
| general_llm | 179 | 21.23% | 85.59 | 0.3815 | 0.8188 |
| members | 39 | 100.0% | 100.0 | 0.2667 | 0.3719 |
| policy_schedule_rules | 5 | 100.0% | 100.0 | 0.1988 | 0.2438 |
| reservation | 12 | 100.0% | 100.0 | 2.224 | 3.0412 |
| schedule | 6 | 100.0% | 100.0 | 0.5881 | 1.517 |
| service_fee | 161 | 100.0% | 100.0 | 0.3356 | 0.4672 |

Top errors:
- `missing_any:API|เชื่อมต่อ`: 28
- `missing_any:server|client`: 24
- `missing_any:กิจกรรม`: 17
- `missing_any:GPU|กราฟิก`: 17
- `missing_any:latency|หน่วง`: 14
- `missing_any:เฟรม|ความละเอียด`: 14
- `missing_any:ขอบคุณ`: 14
- `missing_any:คีย์บอร์ด|mechanical`: 13

### llm_scb10x_typhoon2.5-qwen3-4b (scb10x/typhoon2.5-qwen3-4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 15 | 93.33% | 98.93 | 1.5233 | 5.2572 |
| ambiguous_controls | 3 | 100.0% | 100.0 | 0.5458 | 1.5197 |
| availability_game | 103 | 100.0% | 100.0 | 1.2835 | 1.646 |
| availability_machine_split | 2 | 100.0% | 100.0 | 0.9254 | 1.4604 |
| availability_service | 14 | 100.0% | 100.0 | 1.3182 | 4.7744 |
| competition_rules | 46 | 100.0% | 100.0 | 0.3298 | 0.7719 |
| compound | 55 | 96.36% | 98.4 | 5.1528 | 15.4278 |
| equipment | 36 | 100.0% | 100.0 | 0.2287 | 0.2954 |
| game_controls | 215 | 100.0% | 100.0 | 0.4748 | 0.6198 |
| game_detail | 11 | 100.0% | 100.0 | 1.2522 | 1.69 |
| games | 98 | 97.96% | 99.35 | 1.546 | 1.6593 |
| general_llm | 179 | 22.35% | 71.83 | 1.5034 | 10.6952 |
| members | 39 | 100.0% | 100.0 | 0.2485 | 0.3461 |
| policy_schedule_rules | 5 | 100.0% | 100.0 | 0.8089 | 1.3209 |
| reservation | 12 | 100.0% | 100.0 | 2.102 | 3.2123 |
| schedule | 6 | 100.0% | 100.0 | 0.496 | 1.2407 |
| service_fee | 161 | 100.0% | 100.0 | 0.3116 | 0.3826 |

Top errors:
- `llm_required_but_unavailable`: 119
- `missing_any:API|เชื่อมต่อ`: 21
- `missing_any:server|client`: 17
- `category_mismatch:equipment`: 13
- `missing_any:GPU|กราฟิก`: 13
- `missing_any:คีย์บอร์ด|mechanical`: 13
- `missing_any:กิจกรรม`: 12
- `missing_any:latency|หน่วง`: 11

## How To Read

- `No-LLM` คือ baseline ที่ปิด Local LLM เพื่อดูว่า rule/structured/RAG ตอบเองได้แค่ไหน
- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
