# English Shadow Evaluation Analysis

> Scope: machine-translated, unreviewed test questions. This is a routing and safety regression result, not approved English knowledge quality.

## Translation Audit
- Corpus: 1600 rows; duplicate IDs: 0
- Translation status: `{"machine_translated_unreviewed": 1600}`
- Missing English questions: 0; Thai script leakage: 0; duplicate English prompts: 85

## Pipeline Result
- Strict pass: 909/1600 (56.81%)
- Localization-pending blockers: 0; timeouts: 0; exceptions: 0; Thai-answer leakage: 0
- Latency: mean 0.368s, P50 0.015s, P95 2.586s, P99 3.038s, max 7.140s

## Leading Failure Types
- `category`: 691

## Interpretation
- Do not promote these translations into the public localization registry without human review.
