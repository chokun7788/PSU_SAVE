# Competition RAG Phase 1 Implementation Report

## Outcome

Phase 1 implements the safety and data-governance foundation from the end-to-end remediation flow without enabling unapproved V2 content in production.

## Implemented

1. Shared competition taxonomy with locked game IDs, facets, review modules and a version identifier.
2. Non-destructive competition search variants, including the confirmed `เทคเล่น 8` → TEKKEN 8 resolution case without rewriting the user's displayed question.
3. Request-local competition target caching. Repeated resolver calls for the same query compute once and reuse one result.
4. Dedicated strict schemas for draft review records and approved runtime V2.1 records.
5. Automated review validation, owner-gated conversion and release manifest generation.
6. Exact release/game/facet/locale/effective-date gates before claim ranking.
7. Rejection codes for cross-game, wrong-facet, stale evidence, missing localization, expired and conflicting claims.
8. Bounded claim ranking limited to eight eligible candidates.
9. Sentence-to-claim attribution and complete-list validation contracts.
10. Prompt hardening that treats user, web, document and evidence payloads as untrusted data.
11. Taxonomy/schema drift tests and bilingual numeric-parity checks.

## Verification

| Check | Result |
| --- | --- |
| Focused unit/contract tests | 40 passed |
| Existing competition routing smoke tests | Passed |
| Existing bilingual pipeline smoke test | Passed |
| Intent/tool-router/facts-composer smoke tests | Passed |
| Review queue schema validation | 104/104 valid draft records |
| Thai competition regression | 211/264, evidence 211/264 |
| Previous Thai baseline | 209/264 |
| English draft-preview regression | 203/264, evidence 206/264 |
| Previous English draft-preview baseline | 203/264 |
| Timeout observed in these runs | None reported |

The production-safe English run intentionally does not expose draft translations. Its low answer score is not treated as a routing regression; English V2 answers remain blocked until human approval.

## Publication Gate Result

The shadow release builder correctly produced zero runtime claims. All 104 records are blocked for the following reasons:

- 104 are not owner-approved.
- 104 have not passed atomicity review.
- 104 do not have an approved Thai answer.
- 104 do not have owner identity/timestamp approval.
- 65 still conflate or ambiguously separate heading and clause.
- 104 English translations remain drafts.

No runtime JSONL was generated. An audit manifest was written so the blocked build is reproducible.

## Remaining Work Requiring Content Review

1. Split and review the 65 heading/clause-conflicted records.
2. Approve atomic Thai claims with exact source clauses.
3. Add structured values for counts, times, penalties and complete tables.
4. Approve English per claim after Thai approval and numeric parity checks.
5. Publish the first immutable V2.1 shadow release.
6. Integrate that release with the runtime retrieval path under a feature flag.
7. Run shadow comparison, hidden/adversarial tests, 1,600+ bilingual regression and concurrency/session-isolation tests.

## Evidence

- `reports/competition_rules_rag_eval/competition-v2-shadow-20260922.manifest.json`
- `reports/competition_rules_rag_eval/rule_v2_format_audit_20260922/rule_v2_format_audit.json`
- `reports/competition_rules_rag_eval/competition_rules_rag_eval_20260922_133558.json`
- `reports/competition_rules_rag_eval/competition_rules_rag_eval_20260922_134131.json`
