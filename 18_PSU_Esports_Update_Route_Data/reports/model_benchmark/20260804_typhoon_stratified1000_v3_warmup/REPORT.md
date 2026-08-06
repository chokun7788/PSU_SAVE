# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-04T22:58:00
- Case bank: `data\eval\model_benchmark_1500.jsonl`
- Runs: 2

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | no_llm | No-LLM | 85.9% | 97.42 | 0.4587 | 0.8575 | 7.336 | 0 |
| 2 | llm_scb10x_typhoon2.5-qwen3-4b | scb10x/typhoon2.5-qwen3-4b | 84.2% | 94.21 | 1.0705 | 3.1813 | 30.3664 | 228 |

## Group Breakdown

### no_llm (No-LLM)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 15 | 100.0% | 100.0 | 0.6635 | 3.298 |
| ambiguous_controls | 3 | 100.0% | 100.0 | 0.1433 | 0.3123 |
| availability_game | 103 | 100.0% | 100.0 | 0.4523 | 0.7749 |
| availability_machine_split | 2 | 100.0% | 100.0 | 0.311 | 0.3265 |
| availability_service | 14 | 100.0% | 100.0 | 1.0108 | 3.8571 |
| competition_rules | 46 | 100.0% | 100.0 | 0.2896 | 0.4345 |
| compound | 55 | 100.0% | 100.0 | 0.9176 | 1.4544 |
| equipment | 36 | 100.0% | 100.0 | 0.2331 | 0.3199 |
| game_controls | 215 | 100.0% | 100.0 | 0.4183 | 0.6269 |
| game_detail | 11 | 100.0% | 100.0 | 0.4821 | 0.7978 |
| games | 98 | 100.0% | 100.0 | 0.5834 | 0.8166 |
| general_llm | 179 | 21.23% | 85.59 | 0.3886 | 0.8047 |
| members | 39 | 100.0% | 100.0 | 0.275 | 0.4088 |
| policy_schedule_rules | 5 | 100.0% | 100.0 | 0.257 | 0.3217 |
| reservation | 12 | 100.0% | 100.0 | 2.1044 | 3.2599 |
| schedule | 6 | 100.0% | 100.0 | 0.6301 | 1.6685 |
| service_fee | 161 | 100.0% | 100.0 | 0.3212 | 0.4231 |

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
| ambiguity_no_answer | 15 | 93.33% | 98.93 | 1.5798 | 5.3538 |
| ambiguous_controls | 3 | 100.0% | 100.0 | 0.5655 | 1.5574 |
| availability_game | 103 | 100.0% | 100.0 | 1.3016 | 1.5374 |
| availability_machine_split | 2 | 100.0% | 100.0 | 0.8629 | 1.4118 |
| availability_service | 14 | 100.0% | 100.0 | 1.419 | 5.0852 |
| competition_rules | 46 | 100.0% | 100.0 | 0.4102 | 1.2871 |
| compound | 55 | 94.55% | 97.38 | 5.2806 | 15.7308 |
| equipment | 36 | 100.0% | 100.0 | 0.2131 | 0.2842 |
| game_controls | 215 | 100.0% | 100.0 | 0.496 | 0.6519 |
| game_detail | 11 | 100.0% | 100.0 | 1.5507 | 2.0002 |
| games | 98 | 97.96% | 99.35 | 1.5831 | 1.7345 |
| general_llm | 179 | 15.08% | 68.89 | 1.0951 | 3.1813 |
| members | 39 | 100.0% | 100.0 | 0.2553 | 0.3518 |
| policy_schedule_rules | 5 | 100.0% | 100.0 | 0.9137 | 1.564 |
| reservation | 12 | 100.0% | 100.0 | 2.0505 | 2.762 |
| schedule | 6 | 100.0% | 100.0 | 0.497 | 1.2539 |
| service_fee | 161 | 100.0% | 100.0 | 0.3448 | 0.4269 |

Top errors:
- `llm_required_but_unavailable`: 133
- `missing_any:API|เชื่อมต่อ`: 23
- `missing_any:server|client`: 20
- `missing_any:GPU|กราฟิก`: 14
- `category_mismatch:equipment`: 13
- `missing_any:latency|หน่วง`: 13
- `missing_any:กิจกรรม`: 13
- `missing_any:คีย์บอร์ด|mechanical`: 13

## How To Read

- `No-LLM` คือ baseline ที่ปิด Local LLM เพื่อดูว่า rule/structured/RAG ตอบเองได้แค่ไหน
- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
