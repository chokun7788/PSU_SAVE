# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-23T16:06:15
- Case bank: `data\eval\model_benchmark_1500.jsonl`
- Runs: 2

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | llm_scb10x_typhoon2.5-qwen3-4b | scb10x/typhoon2.5-qwen3-4b | 96.25% | 98.88 | 1.4635 | 4.1762 | 20.4899 | 278 |
| 2 | no_llm | No-LLM | 86.12% | 97.39 | 0.5235 | 1.2627 | 9.3943 | 0 |

## Group Breakdown

### llm_scb10x_typhoon2.5-qwen3-4b (scb10x/typhoon2.5-qwen3-4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 87.5% | 94.5 | 2.1999 | 13.901 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 0.7206 | 1.4961 |
| availability_game | 166 | 100.0% | 100.0 | 1.2678 | 1.5839 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.7974 | 1.3957 |
| availability_service | 23 | 100.0% | 100.0 | 1.6968 | 5.2137 |
| competition_rules | 75 | 98.67% | 98.67 | 0.8017 | 1.5076 |
| compound | 89 | 100.0% | 100.0 | 1.0933 | 4.2876 |
| equipment | 58 | 100.0% | 100.0 | 0.2394 | 0.3216 |
| game_controls | 345 | 100.0% | 100.0 | 0.4534 | 0.6386 |
| game_detail | 18 | 100.0% | 100.0 | 1.37 | 1.6639 |
| games | 158 | 98.73% | 99.53 | 1.8049 | 2.105 |
| general_llm | 275 | 80.36% | 94.57 | 4.3495 | 14.6939 |
| members | 63 | 100.0% | 100.0 | 0.4184 | 1.3274 |
| policy_schedule_rules | 8 | 100.0% | 100.0 | 0.8501 | 1.2913 |
| reservation | 20 | 100.0% | 100.0 | 2.9853 | 8.3466 |
| schedule | 10 | 100.0% | 100.0 | 0.7525 | 1.5711 |
| service_fee | 258 | 100.0% | 100.0 | 0.3787 | 0.5908 |

Top errors:
- `category_mismatch:equipment`: 27
- `missing_any:คีย์บอร์ด|mechanical`: 27
- `missing_any:ขอบคุณ`: 12
- `category_mismatch:clarification`: 10
- `missing_any:latency|หน่วง`: 7
- `exception:UnboundLocalError`: 2
- `missing_any:ยังไม่พบ|ไม่มี|ไม่ได้อยู่|ตอบจากข้อมูล`: 2
- `missing_any:กิจกรรม`: 2

### no_llm (No-LLM)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 24 | 100.0% | 100.0 | 0.4393 | 0.9671 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 0.2186 | 0.5258 |
| availability_game | 166 | 100.0% | 100.0 | 0.4551 | 0.7064 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.2919 | 0.3152 |
| availability_service | 23 | 100.0% | 100.0 | 1.0911 | 4.0415 |
| competition_rules | 75 | 100.0% | 100.0 | 0.3711 | 0.5197 |
| compound | 89 | 100.0% | 100.0 | 1.3162 | 2.4641 |
| equipment | 58 | 100.0% | 100.0 | 0.2983 | 0.4001 |
| game_controls | 345 | 100.0% | 100.0 | 0.3718 | 0.6186 |
| game_detail | 18 | 100.0% | 100.0 | 0.4676 | 0.6736 |
| games | 158 | 100.0% | 100.0 | 0.5488 | 0.8857 |
| general_llm | 275 | 19.27% | 84.79 | 0.556 | 1.3563 |
| members | 63 | 100.0% | 100.0 | 0.3711 | 0.591 |
| policy_schedule_rules | 8 | 100.0% | 100.0 | 0.4518 | 1.5793 |
| reservation | 20 | 100.0% | 100.0 | 3.1136 | 9.1871 |
| schedule | 10 | 100.0% | 100.0 | 0.6945 | 1.837 |
| service_fee | 258 | 100.0% | 100.0 | 0.3454 | 0.4376 |

Top errors:
- `missing_any:latency|หน่วง`: 28
- `missing_any:เฟรม|ความละเอียด`: 28
- `missing_any:API|เชื่อมต่อ`: 28
- `missing_any:ขอบคุณ`: 28
- `missing_any:กิจกรรม`: 27
- `missing_any:คีย์บอร์ด|mechanical`: 27
- `missing_any:GPU|กราฟิก`: 27
- `missing_any:server|client`: 27

## How To Read

- `No-LLM` คือ baseline ที่ปิด Local LLM เพื่อดูว่า rule/structured/RAG ตอบเองได้แค่ไหน
- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
