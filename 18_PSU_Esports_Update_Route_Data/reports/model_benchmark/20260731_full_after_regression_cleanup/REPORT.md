# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-01T00:12:22
- Case bank: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\model_benchmark_1500.jsonl`
- Runs: 5

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | llm_scb10x_typhoon2.5-qwen3-4b | scb10x/typhoon2.5-qwen3-4b | 94.75% | 98.61 | 2.3089 | 12.5265 | 262.9887 | 454 |
| 2 | llm_scb10x_llama3.2-typhoon2-3b-instruct | scb10x/llama3.2-typhoon2-3b-instruct | 94.62% | 98.59 | 2.3342 | 13.0106 | 263.347 | 454 |
| 3 | llm_qwen2.5_7b | qwen2.5:7b | 94.94% | 98.27 | 3.3979 | 18.4911 | 232.3512 | 454 |
| 4 | no_llm | No-LLM | 81.19% | 96.45 | 0.831 | 4.1635 | 269.6652 | 215 |
| 5 | llm_qwen3_4b | qwen3:4b | 82.44% | 93.27 | 1.0368 | 5.0101 | 277.6614 | 453 |

## Group Breakdown

### llm_scb10x_typhoon2.5-qwen3-4b (scb10x/typhoon2.5-qwen3-4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 91.67% | 98.67 | 1.9416 | 8.0923 |
| ambiguous_controls | 6 | 100.0% | 98.33 | 3.8674 | 20.3441 |
| availability_game | 166 | 98.8% | 99.81 | 0.9568 | 1.1246 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.5157 | 1.1363 |
| availability_service | 21 | 71.43% | 94.86 | 1.0583 | 3.1919 |
| competition_rules | 75 | 100.0% | 99.87 | 0.8792 | 1.2213 |
| compound | 89 | 95.51% | 99.19 | 3.6426 | 8.2946 |
| equipment | 58 | 96.55% | 99.1 | 3.2923 | 6.1151 |
| game_controls | 343 | 98.83% | 99.76 | 0.2924 | 0.4067 |
| game_detail | 18 | 100.0% | 100.0 | 1.5639 | 3.961 |
| games | 158 | 99.37% | 99.81 | 1.003 | 1.1836 |
| general_llm | 279 | 78.14% | 93.69 | 8.1369 | 14.7141 |
| members | 63 | 100.0% | 100.0 | 3.0319 | 4.5779 |
| policy_schedule_rules | 8 | 75.0% | 96.0 | 1.1717 | 1.8883 |
| reservation | 20 | 100.0% | 100.0 | 3.1177 | 6.4134 |
| schedule | 10 | 100.0% | 100.0 | 2.0181 | 4.239 |
| service_fee | 258 | 100.0% | 100.0 | 0.0782 | 0.1763 |

Top errors:
- `missing_any:กิจกรรม`: 28
- `category_mismatch:overview`: 27
- `missing_any:ขอบคุณ`: 12
- `category_mismatch:clarification`: 10
- `missing_any:latency|หน่วง`: 10
- `category_mismatch:equipment`: 8
- `category_mismatch:games`: 7
- `category_mismatch:schedule`: 4

### llm_scb10x_llama3.2-typhoon2-3b-instruct (scb10x/llama3.2-typhoon2-3b-instruct)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 91.67% | 98.67 | 1.8975 | 6.1525 |
| ambiguous_controls | 6 | 100.0% | 98.33 | 3.9987 | 21.1735 |
| availability_game | 166 | 98.19% | 99.7 | 1.0459 | 1.2411 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.5736 | 1.2746 |
| availability_service | 21 | 61.9% | 93.14 | 1.1023 | 3.245 |
| competition_rules | 75 | 100.0% | 100.0 | 0.8002 | 1.3143 |
| compound | 89 | 95.51% | 99.19 | 3.6464 | 7.9924 |
| equipment | 58 | 96.55% | 99.1 | 3.7792 | 6.6975 |
| game_controls | 343 | 98.83% | 99.76 | 0.3051 | 0.3941 |
| game_detail | 18 | 100.0% | 100.0 | 1.508 | 3.312 |
| games | 158 | 99.37% | 99.81 | 1.0572 | 1.2431 |
| general_llm | 279 | 78.49% | 93.71 | 8.2063 | 15.0176 |
| members | 63 | 100.0% | 100.0 | 2.6851 | 4.1156 |
| policy_schedule_rules | 8 | 75.0% | 96.0 | 1.1441 | 1.791 |
| reservation | 20 | 100.0% | 100.0 | 3.0344 | 6.0124 |
| schedule | 10 | 100.0% | 100.0 | 1.4643 | 3.4228 |
| service_fee | 258 | 100.0% | 100.0 | 0.079 | 0.1742 |

Top errors:
- `missing_any:กิจกรรม`: 28
- `category_mismatch:overview`: 27
- `missing_any:latency|หน่วง`: 12
- `category_mismatch:clarification`: 10
- `category_mismatch:equipment`: 9
- `missing_any:server|client`: 8
- `category_mismatch:games`: 7
- `category_mismatch:schedule`: 6

### llm_qwen2.5_7b (qwen2.5:7b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 91.67% | 98.25 | 3.1345 | 14.921 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 3.9174 | 19.6183 |
| availability_game | 166 | 98.8% | 99.81 | 1.5274 | 1.787 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.8315 | 1.7406 |
| availability_service | 21 | 61.9% | 93.14 | 1.5721 | 3.7879 |
| competition_rules | 75 | 100.0% | 100.0 | 1.2057 | 1.82 |
| compound | 89 | 95.51% | 99.19 | 3.7744 | 8.3579 |
| equipment | 58 | 96.55% | 99.1 | 3.875 | 6.9096 |
| game_controls | 343 | 98.83% | 99.76 | 0.3137 | 0.3855 |
| game_detail | 18 | 100.0% | 100.0 | 2.169 | 4.243 |
| games | 158 | 99.37% | 99.81 | 1.5648 | 1.777 |
| general_llm | 279 | 79.93% | 91.83 | 13.212 | 24.705 |
| members | 63 | 100.0% | 100.0 | 3.0216 | 4.4666 |
| policy_schedule_rules | 8 | 75.0% | 96.0 | 1.496 | 1.8448 |
| reservation | 20 | 100.0% | 100.0 | 3.6126 | 6.8535 |
| schedule | 10 | 100.0% | 100.0 | 1.6804 | 4.3133 |
| service_fee | 258 | 100.0% | 100.0 | 0.099 | 0.1758 |

Top errors:
- `missing_any:กิจกรรม`: 28
- `category_mismatch:overview`: 27
- `missing_any:latency|หน่วง`: 16
- `category_mismatch:clarification`: 10
- `category_mismatch:games`: 8
- `category_mismatch:equipment`: 7
- `category_mismatch:schedule`: 6
- `missing_any:เฟรม|ความละเอียด`: 3

### no_llm (No-LLM)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 91.67% | 97.0 | 0.4627 | 3.4361 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 2.6575 | 15.5769 |
| availability_game | 166 | 98.8% | 99.81 | 0.1389 | 0.184 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.0166 | 0.0243 |
| availability_service | 21 | 61.9% | 93.14 | 0.4246 | 1.791 |
| competition_rules | 75 | 100.0% | 100.0 | 0.158 | 0.3058 |
| compound | 89 | 95.51% | 99.19 | 2.7668 | 6.8209 |
| equipment | 58 | 100.0% | 100.0 | 1.6217 | 3.3107 |
| game_controls | 343 | 98.83% | 99.76 | 0.2304 | 0.2884 |
| game_detail | 18 | 100.0% | 100.0 | 0.5075 | 2.3341 |
| games | 158 | 100.0% | 100.0 | 0.1518 | 0.2583 |
| general_llm | 279 | 0.0% | 81.19 | 2.1199 | 8.8233 |
| members | 63 | 100.0% | 100.0 | 2.4036 | 4.0106 |
| policy_schedule_rules | 8 | 75.0% | 96.0 | 0.7591 | 2.1411 |
| reservation | 20 | 100.0% | 100.0 | 1.7258 | 4.6059 |
| schedule | 10 | 100.0% | 100.0 | 1.0565 | 2.0906 |
| service_fee | 258 | 100.0% | 100.0 | 0.047 | 0.1631 |

Top errors:
- `missing_any:latency|หน่วง`: 28
- `missing_any:เฟรม|ความละเอียด`: 28
- `missing_any:API|เชื่อมต่อ`: 28
- `missing_any:JSON|ข้อมูล`: 28
- `missing_any:ขอบคุณ`: 28
- `missing_any:จอง`: 28
- `missing_any:กิจกรรม`: 28
- `missing_any:คีย์บอร์ด|mechanical`: 28

### llm_qwen3_4b (qwen3:4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 91.67% | 97.0 | 0.5176 | 3.859 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 3.1931 | 18.7645 |
| availability_game | 166 | 98.8% | 99.81 | 0.1774 | 0.2337 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.0208 | 0.0319 |
| availability_service | 21 | 61.9% | 93.14 | 0.5245 | 2.2726 |
| competition_rules | 75 | 100.0% | 100.0 | 0.237 | 0.3569 |
| compound | 89 | 95.51% | 99.19 | 2.7482 | 7.9277 |
| equipment | 58 | 100.0% | 100.0 | 2.2045 | 4.7129 |
| game_controls | 343 | 98.83% | 99.76 | 0.2683 | 0.3366 |
| game_detail | 18 | 100.0% | 100.0 | 2.7207 | 3.7836 |
| games | 158 | 100.0% | 100.0 | 0.3173 | 0.3995 |
| general_llm | 279 | 7.17% | 62.98 | 2.6672 | 9.34 |
| members | 63 | 100.0% | 100.0 | 2.5968 | 3.9244 |
| policy_schedule_rules | 8 | 75.0% | 96.0 | 1.8712 | 3.4146 |
| reservation | 20 | 100.0% | 100.0 | 2.1165 | 5.0774 |
| schedule | 10 | 100.0% | 100.0 | 1.2606 | 2.7201 |
| service_fee | 258 | 100.0% | 100.0 | 0.1073 | 0.19 |

Top errors:
- `llm_required_but_unavailable`: 216
- `missing_any:กิจกรรม`: 28
- `category_mismatch:overview`: 27
- `missing_any:latency|หน่วง`: 26
- `missing_any:เฟรม|ความละเอียด`: 26
- `missing_any:API|เชื่อมต่อ`: 26
- `missing_any:JSON|ข้อมูล`: 26
- `missing_any:ขอบคุณ`: 26

## How To Read

- `No-LLM` คือ baseline ที่ปิด Local LLM เพื่อดูว่า rule/structured/RAG ตอบเองได้แค่ไหน
- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
