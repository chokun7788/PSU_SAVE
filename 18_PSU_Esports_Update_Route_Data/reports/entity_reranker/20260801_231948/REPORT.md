# Entity Reranker Experiment

- created_at: 2026-08-01T23:19:48
- model: cross-encoder/mmarco-mMiniLMv2-L12-H384-v1
- case_count: 20
- baseline_accuracy: 0.9
- reranker_accuracy: 0.9
- baseline_avg_sec: 0.0624
- reranker_avg_sec: 0.0609
- reranker_p95_sec: 0.1029
- model_load_sec: 68.844

## Failures / Changes

### amb_call_of_controls
- question: `Call of Duty ปุ่มทั้งหมดมีอะไรบ้าง`
- expected: ambiguous 
- baseline: ambiguous / Call of Duty: Modern Warfare III / correct=True / margin=0.0
- reranker: exact / Call of Duty: Modern Warfare III / correct=False / margin=0.8081

### exact_call_of_action
- question: `ปุ่มกระโดดใน Call of Duty กดอะไร`
- expected: exact Call of Duty: Modern Warfare III
- baseline: ambiguous / Call of Duty: Modern Warfare III / correct=False / margin=0.0
- reranker: exact / Call of Duty: Modern Warfare III / correct=True / margin=0.5117

### exact_mw3
- question: `Modern Warfare III ปุ่มอะไร`
- expected: exact Call of Duty: Modern Warfare III
- baseline: unknown / Call of Duty: Modern Warfare III / correct=False / margin=1.0
- reranker: exact / Call of Duty: Modern Warfare III / correct=True / margin=1.0

### amb_mario_gameplay
- question: `Mario เล่นยังไง`
- expected: ambiguous 
- baseline: ambiguous / Mario Kart 8 Deluxe / correct=True / margin=0.0
- reranker: exact / Mario Party Superstars / correct=False / margin=0.5798
