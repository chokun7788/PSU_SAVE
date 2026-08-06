# Entity Reranker Experiment

- created_at: 2026-08-01T23:23:24
- model: BAAI/bge-reranker-v2-m3
- case_count: 20
- baseline_accuracy: 0.9
- reranker_accuracy: 0.85
- baseline_avg_sec: 0.0622
- reranker_avg_sec: 1.1975
- reranker_p95_sec: 2.1895
- model_load_sec: 25.638

## Failures / Changes

### exact_call_of_action
- question: `ปุ่มกระโดดใน Call of Duty กดอะไร`
- expected: exact Call of Duty: Modern Warfare III
- baseline: ambiguous / Call of Duty: Modern Warfare III / correct=False / margin=0.0
- reranker: ambiguous / Call of Duty: Modern Warfare III / correct=False / margin=0.0227

### exact_mw3
- question: `Modern Warfare III ปุ่มอะไร`
- expected: exact Call of Duty: Modern Warfare III
- baseline: unknown / Call of Duty: Modern Warfare III / correct=False / margin=1.0
- reranker: exact / Call of Duty: Modern Warfare III / correct=True / margin=1.0

### amb_mario_gameplay
- question: `Mario เล่นยังไง`
- expected: ambiguous 
- baseline: ambiguous / Mario Kart 8 Deluxe / correct=True / margin=0.0
- reranker: exact / New Super Mario Bros. U Deluxe / correct=False / margin=0.3274

### amb_overcook_gameplay
- question: `Over cook เล่นยังไง`
- expected: ambiguous 
- baseline: ambiguous / Overcooked! / correct=True / margin=0.0
- reranker: exact / Overcooked! 2 / correct=False / margin=0.6124
