# Ground Truth Evaluation - PSU Esports Local RAG

วันที่: 2026-06-30

## Summary

- Total: 60
- PASS: 60
- FAIL: 0
- ERROR: 0
- Pass rate: 100.00%
- Average latency: 0.087s
- Keyword fail: 0
- Source fail: 0
- Answers containing `ไม่พบข้อมูล`: 0
- Chinese character leakage: 0

## Mode Distribution

- `rule_fast_path`: 38
- `deterministic_calculator`: 20
- `rag_llm`: 1
- `rag_direct_curated`: 1

## Answer Type Distribution

- `fact`: 40
- `calculation`: 20

## By Category

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| reservation | 40 | 40 | 100.00% |
| service_fee | 20 | 20 | 100.00% |

## By Answer Type

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| calculation | 20 | 20 | 100.00% |
| fact | 40 | 40 | 100.00% |

## By Difficulty

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| medium | 60 | 60 | 100.00% |

## By Mode

| Group | PASS | Total | Pass rate |
|---|---:|---:|---:|
| deterministic_calculator | 20 | 20 | 100.00% |
| rag_direct_curated | 1 | 1 | 100.00% |
| rag_llm | 1 | 1 | 100.00% |
| rule_fast_path | 38 | 38 | 100.00% |

## Failed Cases

No failed cases.

## Answer Characteristics

- `rule_fast_path` คือคำตอบ FAQ ที่เร็วและนิ่งที่สุด
- `rag_direct_curated` คือคำตอบจาก curated facts ที่ไม่ต้องเรียก LLM จึงเร็วและลด hallucination
- `rag_llm` คือคำตอบที่ต้องให้โมเดลสรุปจาก context จึงช้ากว่าและเสี่ยง keyword หายมากกว่า
- การวัดนี้เป็น keyword/source match แบบเข้ม ถ้าคำตอบถูกความหมายแต่ใช้คำคนละรูป อาจถูกนับเป็น FAIL ได้

## Files

- Results JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\16_PSU_Esports_RAG_Experiment_Timeline\ground_truth_eval_results_v2_after_data_fix_sample60.jsonl`
- Chat log JSONL: `C:\Users\Chokhun\Downloads\Learn-LLM\16_PSU_Esports_RAG_Experiment_Timeline\ground_truth_chat_log_v2_after_data_fix_sample60.jsonl`
