# Ground Truth Evaluation - PSU Esports Local RAG

วันที่: 2026-06-30

## Summary

- Total: 360
- PASS: 360
- FAIL: 0
- ERROR: 0
- Pass rate: 100.00%
- Average latency: 0.234s
- Keyword fail: 0
- Source fail: 0
- Answers containing `ไม่พบข้อมูล`: 26
- Chinese character leakage: 0

## Mode Distribution

- `rule_fast_path`: 158
- `deterministic_calculator`: 130
- `rag_direct_curated`: 49
- `rag_llm`: 23

## Answer Type Distribution

- `fact`: 172
- `calculation`: 113
- `no_answer`: 34
- `list`: 19
- `summary`: 12
- `multi_fact`: 10

## By Category

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| about_us | 5 | 5 | 100.00% |
| contact | 10 | 10 | 100.00% |
| equipment | 10 | 10 | 100.00% |
| events_news | 5 | 5 | 100.00% |
| games | 26 | 26 | 100.00% |
| knowledge | 7 | 7 | 100.00% |
| no_answer | 26 | 26 | 100.00% |
| overview | 5 | 5 | 100.00% |
| penalty | 11 | 11 | 100.00% |
| reservation | 93 | 93 | 100.00% |
| rules | 23 | 23 | 100.00% |
| service_fee | 139 | 139 | 100.00% |

## By Answer Type

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| calculation | 113 | 113 | 100.00% |
| fact | 172 | 172 | 100.00% |
| list | 19 | 19 | 100.00% |
| multi_fact | 10 | 10 | 100.00% |
| no_answer | 34 | 34 | 100.00% |
| summary | 12 | 12 | 100.00% |

## By Difficulty

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| hard | 90 | 90 | 100.00% |
| medium | 270 | 270 | 100.00% |

## By Mode

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| deterministic_calculator | 130 | 130 | 100.00% |
| rag_direct_curated | 49 | 49 | 100.00% |
| rag_llm | 23 | 23 | 100.00% |
| rule_fast_path | 158 | 158 | 100.00% |

## Failed Cases

No failed cases.

## Answer Characteristics

- `rule_fast_path` คือคำตอบ FAQ ที่เร็วและนิ่งที่สุด
- `rag_direct_curated` คือคำตอบจาก curated facts ที่ไม่ต้องเรียก LLM จึงเร็วและลด hallucination
- `rag_llm` คือคำตอบที่ต้องให้โมเดลสรุปจาก context จึงช้ากว่าและเสี่ยง keyword หายมากกว่า
- การวัดนี้เป็น keyword/source match แบบเข้ม ถ้าคำตอบถูกความหมายแต่ใช้คำคนละรูป อาจถูกนับเป็น FAIL ได้

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\16_PSU_Esports_RAG_Experiment_Timeline\ground_truth_eval_results_v2_data_fix_100pct.jsonl`
- Chat log JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\16_PSU_Esports_RAG_Experiment_Timeline\ground_truth_chat_log_v2_data_fix_100pct.jsonl`
