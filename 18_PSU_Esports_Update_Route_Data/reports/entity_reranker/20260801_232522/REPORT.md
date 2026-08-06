# Entity Reranker Experiment

- created_at: 2026-08-01T23:25:22
- model: BAAI/bge-reranker-v2-m3
- case_count: 20
- baseline_accuracy: 0.9
- reranker_accuracy: 0.95
- baseline_avg_sec: 0.0646
- reranker_avg_sec: 0.6229
- reranker_p95_sec: 0.9924
- model_load_sec: 27.231
- include_control_snippets: False

## Failures / Changes

### exact_call_of_action
- question: `ปุ่มกระโดดใน Call of Duty กดอะไร`
- expected: exact Call of Duty: Modern Warfare III
- baseline: ambiguous / Call of Duty: Modern Warfare III / correct=False / margin=0.0
- reranker: ambiguous / Call of Duty: Modern Warfare III / correct=False / margin=0.0

### exact_mw3
- question: `Modern Warfare III ปุ่มอะไร`
- expected: exact Call of Duty: Modern Warfare III
- baseline: unknown / Call of Duty: Modern Warfare III / correct=False / margin=1.0
- reranker: exact / Call of Duty: Modern Warfare III / correct=True / margin=1.0
