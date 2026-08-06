# Entity Reranker Experiment

- created_at: 2026-08-01T23:22:21
- model: cross-encoder/mmarco-mMiniLMv2-L12-H384-v1
- case_count: 20
- baseline_accuracy: 0.9
- reranker_accuracy: 0.75
- baseline_avg_sec: 0.0587
- reranker_avg_sec: 0.1879
- reranker_p95_sec: 0.4451
- model_load_sec: 27.617

## Failures / Changes

### amb_call_of_gameplay
- question: `Call of เล่นยังไง`
- expected: ambiguous 
- baseline: ambiguous / Call of Duty: Modern Warfare III / correct=True / margin=0.0
- reranker: exact / Call of Duty: Modern Warfare III / correct=False / margin=0.3789

### amb_call_of_controls
- question: `Call of Duty ปุ่มทั้งหมดมีอะไรบ้าง`
- expected: ambiguous 
- baseline: ambiguous / Call of Duty: Modern Warfare III / correct=True / margin=0.0
- reranker: exact / Call of Duty: Modern Warfare III / correct=False / margin=1.4138

### exact_call_of_action
- question: `ปุ่มกระโดดใน Call of Duty กดอะไร`
- expected: exact Call of Duty: Modern Warfare III
- baseline: ambiguous / Call of Duty: Modern Warfare III / correct=False / margin=0.0
- reranker: exact / Call of Duty: Modern Warfare III / correct=True / margin=1.4782

### exact_mw3
- question: `Modern Warfare III ปุ่มอะไร`
- expected: exact Call of Duty: Modern Warfare III
- baseline: unknown / Call of Duty: Modern Warfare III / correct=False / margin=1.0
- reranker: exact / Call of Duty: Modern Warfare III / correct=True / margin=1.0

### amb_mario_controls
- question: `Mario ปุ่มอะไร`
- expected: ambiguous 
- baseline: ambiguous / Mario Kart 8 Deluxe / correct=True / margin=0.0
- reranker: exact / Mario Kart 8 Deluxe / correct=False / margin=0.5792

### amb_resident_gameplay
- question: `Resident เล่นยังไง`
- expected: ambiguous 
- baseline: ambiguous / Resident Evil 4 / correct=True / margin=0.0
- reranker: exact / Resident Evil Village / correct=False / margin=1.935

### amb_overcook_gameplay
- question: `Over cook เล่นยังไง`
- expected: ambiguous 
- baseline: ambiguous / Overcooked! / correct=True / margin=0.0
- reranker: exact / Overcooked! 2 / correct=False / margin=3.3193
