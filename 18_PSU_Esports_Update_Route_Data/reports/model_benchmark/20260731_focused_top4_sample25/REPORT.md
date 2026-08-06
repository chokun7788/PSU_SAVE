# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-07-31T18:17:07
- Case bank: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\model_benchmark_1500.jsonl`
- Runs: 5

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | llm_scb10x_typhoon2.5-qwen3-4b | scb10x/typhoon2.5-qwen3-4b | 93.15% | 98.43 | 1.3615 | 5.7947 | 15.9192 | 66 |
| 2 | llm_qwen3_4b | qwen3:4b | 92.86% | 98.33 | 2.6119 | 8.0819 | 17.801 | 66 |
| 3 | llm_scb10x_llama3.2-typhoon2-3b-instruct | scb10x/llama3.2-typhoon2-3b-instruct | 91.96% | 98.09 | 1.3364 | 6.0723 | 15.3076 | 66 |
| 4 | llm_qwen2.5_7b | qwen2.5:7b | 92.26% | 97.99 | 2.0514 | 9.4357 | 24.4974 | 66 |
| 5 | no_llm | No-LLM | 86.01% | 97.1 | 0.2875 | 1.2332 | 14.3892 | 41 |

## Group Breakdown

### llm_scb10x_typhoon2.5-qwen3-4b (scb10x/typhoon2.5-qwen3-4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 91.67% | 98.67 | 2.378 | 8.5895 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 3.8496 | 15.9192 |
| availability_game | 25 | 96.0% | 99.36 | 0.9802 | 2.1807 |
| availability_machine_split | 4 | 0.0% | 84.0 | 0.435 | 0.9172 |
| availability_service | 21 | 47.62% | 86.0 | 1.0042 | 5.3179 |
| competition_rules | 25 | 100.0% | 100.0 | 0.5714 | 1.2096 |
| compound | 25 | 100.0% | 100.0 | 0.7991 | 2.1988 |
| equipment | 25 | 100.0% | 100.0 | 0.8939 | 0.9886 |
| game_controls | 25 | 100.0% | 100.0 | 0.0937 | 0.1236 |
| game_detail | 18 | 100.0% | 100.0 | 1.2179 | 2.4099 |
| games | 25 | 100.0% | 100.0 | 0.9911 | 1.3831 |
| general_llm | 25 | 88.0% | 96.64 | 6.7942 | 13.4766 |
| members | 25 | 100.0% | 100.0 | 0.4265 | 1.0518 |
| policy_schedule_rules | 8 | 75.0% | 95.5 | 0.5698 | 1.3322 |
| reservation | 20 | 100.0% | 100.0 | 1.6195 | 3.2501 |
| schedule | 10 | 100.0% | 100.0 | 0.6465 | 1.607 |
| service_fee | 25 | 100.0% | 100.0 | 0.0151 | 0.0176 |

Top errors:
- `category_mismatch:clarification`: 6
- `category_mismatch:equipment`: 3
- `missing_any:1 คน|คน`: 3
- `category_mismatch:schedule`: 3
- `missing_any:ยังไม่พบ|ไม่มี|ไม่ได้อยู่|ตอบจากข้อมูล`: 2
- `missing_any:ไม่มี|PC #03-#10`: 2
- `missing_any:ไม่มี|PC #01-#02`: 2
- `missing_any:1-5 คน|คน`: 2

### llm_qwen3_4b (qwen3:4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 95.83% | 99.33 | 3.643 | 8.8262 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 4.8429 | 17.7398 |
| availability_game | 25 | 96.0% | 99.36 | 2.6909 | 4.1141 |
| availability_machine_split | 4 | 0.0% | 84.0 | 1.4995 | 3.0352 |
| availability_service | 21 | 38.1% | 84.29 | 1.9669 | 7.2841 |
| competition_rules | 25 | 100.0% | 100.0 | 1.6959 | 3.5176 |
| compound | 25 | 100.0% | 100.0 | 2.089 | 4.8149 |
| equipment | 25 | 100.0% | 100.0 | 3.0187 | 3.196 |
| game_controls | 25 | 100.0% | 100.0 | 0.1014 | 0.1458 |
| game_detail | 18 | 100.0% | 100.0 | 3.2292 | 4.7046 |
| games | 25 | 100.0% | 100.0 | 3.1208 | 3.2442 |
| general_llm | 25 | 88.0% | 96.64 | 8.7749 | 17.1814 |
| members | 25 | 100.0% | 100.0 | 0.8867 | 3.3076 |
| policy_schedule_rules | 8 | 75.0% | 93.5 | 1.6442 | 3.6148 |
| reservation | 20 | 100.0% | 100.0 | 3.6241 | 5.2994 |
| schedule | 10 | 100.0% | 100.0 | 1.0246 | 3.4988 |
| service_fee | 25 | 100.0% | 100.0 | 0.013 | 0.018 |

Top errors:
- `category_mismatch:clarification`: 6
- `category_mismatch:schedule`: 6
- `missing_any:1 คน|คน`: 3
- `missing_any:ไม่มี|PC #03-#10`: 2
- `missing_any:ไม่มี|PC #01-#02`: 2
- `category_mismatch:equipment`: 2
- `missing_any:1-5 คน|คน`: 2
- `category_mismatch:overview`: 2

### llm_scb10x_llama3.2-typhoon2-3b-instruct (scb10x/llama3.2-typhoon2-3b-instruct)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 95.83% | 99.33 | 2.2198 | 8.4067 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 3.8166 | 15.3076 |
| availability_game | 25 | 96.0% | 99.36 | 0.955 | 1.9195 |
| availability_machine_split | 4 | 0.0% | 84.0 | 0.4528 | 0.8997 |
| availability_service | 21 | 38.1% | 82.76 | 1.0607 | 5.0166 |
| competition_rules | 25 | 100.0% | 100.0 | 0.5457 | 1.1435 |
| compound | 25 | 100.0% | 100.0 | 0.779 | 2.1726 |
| equipment | 25 | 100.0% | 100.0 | 0.9197 | 0.9914 |
| game_controls | 25 | 100.0% | 100.0 | 0.095 | 0.132 |
| game_detail | 18 | 100.0% | 100.0 | 1.1385 | 1.8853 |
| games | 25 | 100.0% | 100.0 | 1.0081 | 1.0802 |
| general_llm | 25 | 76.0% | 94.72 | 6.5941 | 13.9351 |
| members | 25 | 100.0% | 100.0 | 0.4593 | 1.1404 |
| policy_schedule_rules | 8 | 75.0% | 93.5 | 0.5095 | 1.1279 |
| reservation | 20 | 100.0% | 100.0 | 1.69 | 3.3631 |
| schedule | 10 | 100.0% | 100.0 | 0.6212 | 1.3629 |
| service_fee | 25 | 100.0% | 100.0 | 0.012 | 0.0172 |

Top errors:
- `category_mismatch:clarification`: 6
- `category_mismatch:schedule`: 6
- `missing_any:1 คน|คน`: 3
- `missing_any:ไม่มี|PC #03-#10`: 2
- `missing_any:ไม่มี|PC #01-#02`: 2
- `category_mismatch:equipment`: 2
- `missing_any:1-2 คน|คน`: 2
- `missing_any:1-5 คน|คน`: 2

### llm_qwen2.5_7b (qwen2.5:7b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 91.67% | 98.67 | 3.4229 | 13.517 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 4.7276 | 17.0116 |
| availability_game | 25 | 96.0% | 99.36 | 1.4686 | 2.4977 |
| availability_machine_split | 4 | 0.0% | 84.0 | 0.7437 | 1.4987 |
| availability_service | 21 | 38.1% | 82.76 | 1.3687 | 5.8906 |
| competition_rules | 25 | 100.0% | 100.0 | 0.8956 | 1.8687 |
| compound | 25 | 100.0% | 100.0 | 1.106 | 2.9332 |
| equipment | 25 | 100.0% | 100.0 | 1.5268 | 1.7216 |
| game_controls | 25 | 100.0% | 100.0 | 0.0998 | 0.1392 |
| game_detail | 18 | 100.0% | 100.0 | 1.7059 | 2.6333 |
| games | 25 | 100.0% | 100.0 | 1.6135 | 1.774 |
| general_llm | 25 | 84.0% | 94.0 | 10.8485 | 23.846 |
| members | 25 | 100.0% | 100.0 | 0.6724 | 1.6985 |
| policy_schedule_rules | 8 | 75.0% | 93.5 | 0.9123 | 1.7672 |
| reservation | 20 | 100.0% | 100.0 | 2.2404 | 3.9763 |
| schedule | 10 | 100.0% | 100.0 | 0.8096 | 1.892 |
| service_fee | 25 | 100.0% | 100.0 | 0.0142 | 0.0176 |

Top errors:
- `category_mismatch:clarification`: 6
- `category_mismatch:schedule`: 6
- `missing_any:1 คน|คน`: 3
- `missing_any:ยังไม่พบ|ไม่มี|ไม่ได้อยู่|ตอบจากข้อมูล`: 2
- `missing_any:ไม่มี|PC #03-#10`: 2
- `missing_any:ไม่มี|PC #01-#02`: 2
- `category_mismatch:equipment`: 2
- `missing_any:1-2 คน|คน`: 2

### no_llm (No-LLM)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 91.67% | 97.0 | 0.5998 | 3.8527 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 2.4457 | 14.3892 |
| availability_game | 25 | 96.0% | 99.36 | 0.2086 | 1.0207 |
| availability_machine_split | 4 | 0.0% | 84.0 | 0.0162 | 0.0226 |
| availability_service | 21 | 38.1% | 84.29 | 0.7491 | 3.9682 |
| competition_rules | 25 | 100.0% | 100.0 | 0.0739 | 0.2184 |
| compound | 25 | 100.0% | 100.0 | 0.3057 | 1.3541 |
| equipment | 25 | 100.0% | 100.0 | 0.0686 | 0.1266 |
| game_controls | 25 | 100.0% | 100.0 | 0.0948 | 0.1339 |
| game_detail | 18 | 100.0% | 100.0 | 0.3116 | 1.2332 |
| games | 25 | 100.0% | 100.0 | 0.1165 | 0.154 |
| general_llm | 25 | 0.0% | 82.56 | 0.1142 | 0.1825 |
| members | 25 | 100.0% | 100.0 | 0.0723 | 0.1224 |
| policy_schedule_rules | 8 | 75.0% | 93.0 | 0.0555 | 0.1087 |
| reservation | 20 | 100.0% | 100.0 | 0.7736 | 2.2844 |
| schedule | 10 | 100.0% | 100.0 | 0.3592 | 1.196 |
| service_fee | 25 | 100.0% | 100.0 | 0.0101 | 0.0131 |

Top errors:
- `category_mismatch:clarification`: 6
- `category_mismatch:schedule`: 6
- `forbidden:Local LLM`: 3
- `missing_any:1 คน|คน`: 3
- `missing_any:latency|หน่วง`: 3
- `missing_any:เฟรม|ความละเอียด`: 3
- `missing_any:API|เชื่อมต่อ`: 3
- `missing_any:JSON|ข้อมูล`: 3

## How To Read

- `No-LLM` คือ baseline ที่ปิด Local LLM เพื่อดูว่า rule/structured/RAG ตอบเองได้แค่ไหน
- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
