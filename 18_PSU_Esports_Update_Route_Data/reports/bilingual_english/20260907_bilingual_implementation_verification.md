# Bilingual English Support - Implementation Verification

Date: 2026-09-07 (Asia/Bangkok)

## Result

The bilingual FAQ implementation is complete for the approved deterministic English routes. The service has an `Auto | Thai | English` selector, request-local language resolution, bilingual session metadata, English-safe fallback messages, and English structured/rule answers that use the same source facts as Thai.

## Verified Results

| Verification | Result |
| --- | --- |
| English Gold corpus | 400/400 strict pass (100%) |
| English critical facts | 218/218 pass (100%) |
| English P95 latency | 0.1011 seconds |
| English maximum latency | 1.1021 seconds |
| English requests over 10 seconds | 0 |
| Thai model-enabled regression | 1,568/1,600 pass (98.00%) |
| Thai comparison with previous 94.12% baseline | +62 fixed cases, 0 new regressions |
| Concurrent web API language isolation | 10/10 sessions passed with no locale leakage |
| Desktop and mobile web UI | Verified with English switch, Thai switch, English request, translated controls, and responsive layout |

## Important Safety Outcome

The English Gold corpus includes 86 cases that correctly return a localized `missing_english_localization` no-answer. This is intentional: unapproved Thai detail, document, member, or RAG content is never translated at runtime and never allowed to become a new English PSU fact.

## Pending Human Work

1. Approve or reject the generated localization drafts in `data/locales/en/localization_review_drafts.jsonl`.
2. Create and review English questions for all 1,600 Thai Shadow cases. The Shadow run is correctly blocked until that review exists, rather than producing untrusted automated translations.
3. Publish approved overlays through `data/locales/en/approved_localizations.jsonl`. A source-hash mismatch automatically makes an older translation stale.

## Evidence Artifacts

- English release candidate: `reports/bilingual_english/20260907_full400_release_candidate/summary.json`
- English per-case results: `reports/bilingual_english/20260907_full400_release_candidate/results.jsonl`
- Shadow review gate: `reports/bilingual_english/20260907_shadow1600_review_gate/summary.json`
- Thai model-enabled regression: `reports/model_benchmark/20260904_bilingual_thai_full1600/llm_scb10x_typhoon2.5-qwen3-4b/summary.json`
- English corpus generator: `tools/generate_bilingual_eval_corpora.py`
- English evaluator: `tools/run_bilingual_english_eval.py`

## Demo Configuration

The bilingual feature defaults to disabled in code for controlled rollout. The local demonstration server was started with `PSU_BILINGUAL_EN_ENABLED=1`. Production rollout should keep the feature flag off until the owner approves the required localizations and Shadow corpus.
