# Entity Reranker Experiment

- created_at: 2026-08-01T23:18:25
- model: BAAI/bge-reranker-v2-m3
- case_count: 20
- baseline_accuracy: 0.9
- reranker_accuracy: 0.95
- baseline_avg_sec: 0.061
- reranker_avg_sec: 0.5633
- reranker_p95_sec: 0.8798
- model_load_sec: 161.198

## Failures / Changes

### exact_call_of_action
- question: `ปุ่มกระโดดใน Call of Duty กดอะไร`
- expected: exact Call of Duty: Modern Warfare III
- baseline: ambiguous / Call of Duty: Modern Warfare III / correct=False / margin=0.0
- reranker: ambiguous / Call of Duty: Warzone / correct=False / margin=0.0003

### exact_mw3
- question: `Modern Warfare III ปุ่มอะไร`
- expected: exact Call of Duty: Modern Warfare III
- baseline: unknown / Call of Duty: Modern Warfare III / correct=False / margin=1.0
- reranker: exact / Call of Duty: Modern Warfare III / correct=True / margin=1.0
