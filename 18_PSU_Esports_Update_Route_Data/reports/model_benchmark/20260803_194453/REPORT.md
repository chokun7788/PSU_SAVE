# PSU Esports Chatbot Model Benchmark Report

- Generated at: 2026-08-03T19:50:24
- Case bank: `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\data\eval\model_benchmark_1500.jsonl`
- Runs: 1

## Overall Ranking

| Rank | Run | Model | Pass rate | Avg score | Avg sec | P95 sec | Max sec | LLM calls |
|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | no_llm | No-LLM | 93.01% | 98.88 | 1.1508 | 3.6913 | 7.326 | 0 |

## Group Breakdown

### no_llm (No-LLM)

| Group | Total | Pass rate | Avg score | Avg sec | P95 sec |
|---|---:|---:|---:|---:|---:|
| ambiguity_no_answer | 20 | 100.0% | 100.0 | 0.6747 | 3.8752 |
| ambiguous_controls | 6 | 100.0% | 100.0 | 0.147 | 0.4166 |
| availability_game | 20 | 100.0% | 100.0 | 0.3487 | 0.5004 |
| availability_machine_split | 4 | 100.0% | 100.0 | 0.2333 | 0.2506 |
| availability_service | 20 | 100.0% | 100.0 | 0.8877 | 3.5511 |
| competition_rules | 20 | 100.0% | 100.0 | 0.3169 | 0.4845 |
| compound | 20 | 100.0% | 100.0 | 1.285 | 2.383 |
| equipment | 20 | 100.0% | 100.0 | 2.8093 | 6.6469 |
| game_controls | 20 | 100.0% | 100.0 | 0.4143 | 0.4919 |
| game_detail | 18 | 100.0% | 100.0 | 0.4313 | 0.6393 |
| games | 20 | 100.0% | 100.0 | 0.5179 | 0.8025 |
| general_llm | 20 | 0.0% | 84.0 | 0.2804 | 0.3901 |
| members | 20 | 100.0% | 100.0 | 2.1393 | 3.347 |
| policy_schedule_rules | 8 | 100.0% | 100.0 | 0.7112 | 1.6526 |
| reservation | 20 | 100.0% | 100.0 | 2.4799 | 6.8567 |
| schedule | 10 | 100.0% | 100.0 | 1.1857 | 2.2794 |
| service_fee | 20 | 100.0% | 100.0 | 2.9468 | 4.0186 |

Top errors:
- `missing_any:latency|หน่วง`: 2
- `missing_any:เฟรม|ความละเอียด`: 2
- `missing_any:API|เชื่อมต่อ`: 2
- `missing_any:JSON|ข้อมูล`: 2
- `missing_any:ขอบคุณ`: 2
- `missing_any:จอง`: 2
- `missing_any:กิจกรรม`: 2
- `missing_any:คีย์บอร์ด|mechanical`: 2

## How To Read

- `No-LLM` คือ baseline ที่ปิด Local LLM เพื่อดูว่า rule/structured/RAG ตอบเองได้แค่ไหน
- case ที่เป็น `general_llm` ตั้งใจให้ No-LLM decline ได้ แต่ model run ควรตอบได้
- คะแนนเป็น heuristic judge สำหรับคัดปัญหาเร็ว ยังไม่ใช่ human approval สุดท้าย
- ดูตัวอย่างคำตอบละเอียดได้ใน `results.csv` และ `results.jsonl` ของแต่ละ run
