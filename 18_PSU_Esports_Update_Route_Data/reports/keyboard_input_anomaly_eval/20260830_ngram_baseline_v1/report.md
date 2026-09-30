# Keyboard Input Anomaly Detector Evaluation

Generated: 2026-08-30T21:10:54+07:00
Detector: `char_ngram_hidden_layout_hypothesis_v1`
Evaluation status: **regression benchmark; not an untouched independent holdout**

## Locked Thresholds

| Detector | Threshold | Calibration policy |
|---|---:|---|
| Keyboard layout | 0.418411 | maximum calibration recall with precision >= 0.97 |
| Repeated character | 0.718849 | maximum calibration recall with precision >= 0.95 |

## Test Split (400 cases)

| Metric | Layout | Repeat |
|---|---:|---:|
| Precision | 100.00% | 100.00% |
| Recall | 100.00% | 100.00% |
| F1 | 100.00% | 100.00% |
| False-positive rate | 0.00% | 0.00% |

- Exact flag accuracy: 100.00%
- Action accuracy: 100.00%
- No-flag control false-positive rate: 0.00%
- Mean detector latency: 0.804 ms per case
- Layout score separation margin: 0.150962
- Repeat score separation margin: 0.360887
- Hidden layout preview exactly matched canonical text in 59.90% of layout-positive test cases.

## Error Concentration

No evaluation errors were found.

## Interpretation Guardrail

Mapped candidates in the result files are hidden diagnostic hypotheses only. They must not replace user input or be sent to Fast/Structured, RAG, or LLM answer routes automatically.

The dataset is mostly synthetic. These scores are baseline engineering evidence, not a production accuracy claim. Real anonymized user typo logs still require human labeling and a separate holdout evaluation.

Feature rules were revised after earlier test errors were inspected during this implementation run. The final 400-case result is therefore a regression result, not an untouched independent holdout.
