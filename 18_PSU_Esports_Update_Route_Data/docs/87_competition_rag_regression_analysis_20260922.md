# Competition Rules RAG Regression Analysis - 2026-09-22

## Scope

This report evaluates the four current competition rulebooks with the full 264-case corpus per locale. English uses the repaired, hash-matched draft-localization preview only for evaluation. It does not publish English translations or activate an owner-approved competition release.

## Changes Evaluated

1. English competition ranking removes generic request scaffolding such as `tournament rules`, `verify`, `policy`, and `cite` before scoring a rule facet.
2. Exact Thai source retrieval remains a tie-breaker only. It does not override an answerable English clause merely because a broad document heading ranks highly.
3. English excerpt trimming no longer treats an outline number such as `8.` as a complete sentence. This preserves the visible start of a penalty table.
4. The shared Thai/English target guard was left unchanged after an experiment showed that unreviewed canonical metadata can mislabel a clause. Only reviewed V2 metadata may later influence runtime ranking.

## Full Regression Results

| Locale | Passed | Total | Pass Rate | Evidence Aligned | P95 | Max | Timeout over 20s |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Thai | 209 | 264 | 79.2% | 209 | 0.726s | 2.795s | 0 |
| English | 203 | 264 | 76.9% | 206 | 0.314s | 6.508s | 0 |

The previous English run on 2026-09-21 passed 198/264 (75.0%). The evaluated change improves it by 5 cases while keeping the latency budget intact.

## What Is Still Wrong

### 1. English: 55 evidence-contract gaps

The dominant English failure is not a wrong game target. The system usually answers from the correct rulebook but the returned source chunk does not appear in the current Gold row's allowed-evidence IDs.

Most affected facets:

| Facet | Failed cases | Typical behavior |
| --- | ---: | --- |
| `protest_dispute` | 12 | Returns a nearby CS2/Tekken rule instead of the exact dispute clause expected by Gold. |
| `penalty` | 10 | Returns the verified CS2 penalty table, while the Gold contract expects a different allowed rule ID. |
| `penalty_matrix` | 6 | Same source-content issue: the table is useful but its ID mapping is not in the Gold set. |
| `disconnect` | 6 | RoV answers a genuine reconnect clause, but it differs from the one currently allow-listed. |
| `fair_play_conduct` | 6 | Correct-game conduct clauses are broader/narrower than the current Gold section contract. |
| `in_match_operations` | 6 | VALORANT source chunks are too broad and mix preparation with in-match procedure. |
| `team_size` | 6 | Source content/Gold mapping has not yet isolated roster composition claims. |

There are also 2 missing-English-localization cases, 3 target failures, 2 outcome failures, and 1 route failure. English still relies on draft translation during this evaluation; production must continue to return the safe missing-localization outcome until each overlay is approved.

### 2. Thai: 36 real source-coverage gaps

Thai has 38 outcome failures. Of these, 36 are safe `competition_facet_not_covered_no_answer` responses. The source coverage manifest reports that the currently imported rulebook does not provide a direct clause for the requested proposition.

The largest gaps are:

| Facet | Failed cases | Meaning |
| --- | ---: | --- |
| `pre_match_on_site` | 17 | Several rulebooks lack a direct check-in/on-site arrival procedure. The system correctly refuses to borrow another game's procedure. |
| `match_configuration` | 6 | The available CS2 chunks do not isolate a direct match-configuration claim under the present evidence guard. |
| `conduct` | 6 | The corpus asks for a broad conduct policy while source clauses are more specific. |
| `fair_play_conduct` | 6 | Some expected propositions are not atomically represented in source data. |
| `in_match_operations` | 6 | In-match instructions are mixed into broader paragraphs, so the guard cannot prove the requested procedure. |

The remaining 17 Thai failures have target-correct answers but do not satisfy the current allowed evidence ID set, especially for the CS2 penalty matrix.

### 3. Imported Metadata Cannot Yet Rank Runtime Answers

The existing canonical metadata is migration data, not reviewed truth. A check during this run found examples where a penalty-table source chunk carries an unrelated `pause_timeout` facet. Ranking with that field degraded English from 198/264 to 178/264, so the experiment was removed.

This confirms why the V2 review queue is required: game, facet, exact clause, and evidence ID must be reviewed together before metadata participates in runtime retrieval.

## Recommended Next Steps

1. Review and split the 65 V2 rows where headings and clauses are conflated. Prioritize VALORANT, CS2 penalties, RoV reconnects, and dispute clauses.
2. Update the Gold corpus only after confirming that an alternate source chunk truly answers the same proposition. Do not widen allowed IDs merely to increase a score.
3. Add direct source clauses or mark explicit `unsupported_in_active_source` gaps for check-in, team composition, and in-match procedure. This converts ambiguous failure into an intentional safe outcome.
4. Approve English overlays claim-by-claim after Thai source review. Draft preview is evaluation-only.
5. Build a V2 runtime projection from approved atomic claims, then run this exact corpus in shadow mode before enabling the feature flag.

## Evidence Files

- English full result: `reports/competition_rules_rag_eval/competition_rules_rag_eval_20260922_110549.json`
- Thai full result: `reports/competition_rules_rag_eval/competition_rules_rag_eval_20260922_110749.json`
- English triage: `reports/competition_rules_rag_eval/analysis_20260922_002121/competition_rules_rag_triage_20260922_110319.md`
- Thai triage: `reports/competition_rules_rag_eval/analysis_20260922_002341/competition_rules_rag_triage_20260922_110319.md`
