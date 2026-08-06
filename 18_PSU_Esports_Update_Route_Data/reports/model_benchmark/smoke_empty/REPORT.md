# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-07-31T15:48:42
- Case bank: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\model_benchmark_1500.jsonl`
- Runs: 10

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | llm_qwen2.5_7b | qwen2.5:7b | 100.0% | 100.0 | 0.0631 | 0.0415 | 1.0083 | 20 |
| 2 | llm_scb10x_typhoon2.5-qwen3-4b | scb10x/typhoon2.5-qwen3-4b | 100.0% | 100.0 | 0.0642 | 0.0456 | 1.0015 | 20 |
| 3 | llm_scb10x_llama3.1-typhoon2-8b-instruct | scb10x/llama3.1-typhoon2-8b-instruct | 100.0% | 100.0 | 0.0647 | 0.0438 | 1.0365 | 20 |
| 4 | llm_qwen2.5_3b | qwen2.5:3b | 100.0% | 100.0 | 0.0654 | 0.0451 | 1.0408 | 20 |
| 5 | llm_sailor2_8b | sailor2:8b | 100.0% | 100.0 | 0.0656 | 0.0412 | 1.0559 | 20 |
| 6 | llm_scb10x_llama3.2-typhoon2-3b-instruct | scb10x/llama3.2-typhoon2-3b-instruct | 100.0% | 100.0 | 0.0657 | 0.0375 | 1.0171 | 20 |
| 7 | llm_llama3.1_8b | llama3.1:8b | 100.0% | 100.0 | 0.0662 | 0.0413 | 1.0284 | 20 |
| 8 | llm_qwen3_8b | qwen3:8b | 100.0% | 100.0 | 0.0666 | 0.0436 | 1.0449 | 20 |
| 9 | llm_qwen3_4b | qwen3:4b | 100.0% | 100.0 | 0.0698 | 0.0399 | 1.1148 | 20 |
| 10 | llm_scb10x_typhoon2.1-gemma3-4b | scb10x/typhoon2.1-gemma3-4b | 100.0% | 100.0 | 0.0744 | 0.049 | 1.173 | 20 |

## Group Breakdown

### llm_qwen2.5_7b (qwen2.5:7b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| service_fee | 20 | 100.0% | 100.0 | 0.0631 | 0.0415 |

### llm_scb10x_typhoon2.5-qwen3-4b (scb10x/typhoon2.5-qwen3-4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| service_fee | 20 | 100.0% | 100.0 | 0.0642 | 0.0456 |

### llm_scb10x_llama3.1-typhoon2-8b-instruct (scb10x/llama3.1-typhoon2-8b-instruct)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| service_fee | 20 | 100.0% | 100.0 | 0.0647 | 0.0438 |

### llm_qwen2.5_3b (qwen2.5:3b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| service_fee | 20 | 100.0% | 100.0 | 0.0654 | 0.0451 |

### llm_sailor2_8b (sailor2:8b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| service_fee | 20 | 100.0% | 100.0 | 0.0656 | 0.0412 |

### llm_scb10x_llama3.2-typhoon2-3b-instruct (scb10x/llama3.2-typhoon2-3b-instruct)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| service_fee | 20 | 100.0% | 100.0 | 0.0657 | 0.0375 |

### llm_llama3.1_8b (llama3.1:8b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| service_fee | 20 | 100.0% | 100.0 | 0.0662 | 0.0413 |

### llm_qwen3_8b (qwen3:8b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| service_fee | 20 | 100.0% | 100.0 | 0.0666 | 0.0436 |

### llm_qwen3_4b (qwen3:4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| service_fee | 20 | 100.0% | 100.0 | 0.0698 | 0.0399 |

### llm_scb10x_typhoon2.1-gemma3-4b (scb10x/typhoon2.1-gemma3-4b)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| service_fee | 20 | 100.0% | 100.0 | 0.0744 | 0.049 |

## How To Read

- `No-LLM` คือ baseline ที่ปิด Local LLM เพื่อดูว่า rule/structured/RAG ตอบเองได้แค่ไหน
- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
