# Competition English Draft Translation Audit

**Date:** 2026-09-21  
**Scope:** English localization overlay for the four active competition rulebooks: Counter-Strike 2, Arena of Valor (RoV), Tekken 8, and VALORANT.  
**Release status:** `draft_preview_only` - not approved or published.

## What Was Checked

- 615 English localization records were loaded into a review-only overlay.
- 312 records belong to competition rules: 104 `text`, 104 `section_title`, and 104 `title` fields.
- Registry validation passed with zero schema/hash errors.
- Mechanical localization audit found zero remaining Thai-script, hash, URL, or registry-format issues.
- A Local LLM semantic audit compared all 104 Thai rule text fields with their English drafts.

## Corrections Applied

The following errors were confirmed by direct Thai-to-English review and repaired in the preview overlay:

| Rulebook | Issue in original machine draft | Corrected meaning |
| --- | --- | --- |
| CS2 venue | Prince of Songkla University was rendered as Chulalongkorn University | `Prince of Songkla University, Phuket Campus` |
| CS2 overtime | Overtime was rendered as a prize pool / unlimited matches | 3 rounds per side, first to 4 rounds, starting money `$10,000`, overtime without limit |
| CS2 software | The Thai wording "install your own software" was changed to "without permission" | Do not install your own software on the provided computers |
| CS2 refreshments | `หมากฝรั่ง` was rendered as `checkers` | Chewing gum |
| RoV venue | `อาคาร 5 ชั้น 1` was rendered as Building Level 5, Floor 1 | Building 5, Floor 1 |
| RoV disconnect | `ผู้เข้าแข่งขันหลุด` was rendered as disqualified | Competitor disconnects |
| VALORANT refreshments | `หมากฝรั่ง` was rendered as `checkers` | Chewing gum |
| VALORANT bug rules | The Exploit Adjudication heading was omitted | Heading retained in English draft |

The corrected review overlay is:

`data/locales/en/localization_review_drafts_competition_20260921_repaired.jsonl`

## Semantic Audit Result

- **83/104** text fields received a `pass` verdict from the Local LLM semantic audit.
- **21/104** remain in the manual-review queue.
- Several flags are not translation errors: e.g. omitted section numbering, a heading rendered as a natural English heading, or an English clock format such as `08:30` instead of Thai `08.30`.
- The Local LLM audit is a triage tool, not approval evidence. Each remaining warning needs a bilingual reviewer to compare against the Thai source.

Audit artifacts:

- `reports/competition_rules_rag_eval/english_semantic_audit_20260921_repaired_r2/semantic_audit.json`
- `reports/competition_rules_rag_eval/english_semantic_audit_20260921_repaired_r2/semantic_audit.md`

## Runtime Evaluation

The English competition corpus was run with the corrected draft overlay enabled.

| Run | Passed | Total | Pass rate | Notes |
| --- | ---: | ---: | ---: | --- |
| Before translation-aware selection | 156 | 264 | 59.1% | Thai lexical retrieval often hid a valid English localized section. |
| Current corrected preview | 198 | 264 | 75.0% | Explicit game target and hash-verified English rule text are now ranked by the English rule facet. |

Latest report:

- `reports/competition_rules_rag_eval/competition_rules_rag_eval_20260921_225158.json`
- `reports/competition_rules_rag_eval/competition_rules_rag_eval_20260921_225158_summary.json`
- `reports/competition_rules_rag_eval/analysis_20260921_225158/competition_rules_rag_triage_20260921_225224.md`

Latency stayed within the current 20-second ceiling. Most requests completed below one second; the slowest observed cases in this run were under seven seconds.

## Remaining Gaps

There are **66 failed Gold checks** in the latest English corpus:

- **62 `gold_or_section_contract_gap`:** an answer came from the correct game rulebook but cited a different section than the current expected evidence ID. Main affected facets are penalties, dispute resolution, RoV disconnect/reconnect, and VALORANT in-match procedure.
- **4 `routing_or_target_failure`:** an English phrasing still did not retain the expected game/target contract.

These are now primarily retrieval-ranking and Gold-contract issues, not missing English translation records. They must be addressed before treating the corpus score as release-ready.

## Runtime Safeguards Added

- A named competition-game plus English rule facet such as `overtime`, `Game Breaking Bug`, `competition venue`, or `install software` retains the competition-rule route instead of falling into ordinary game details.
- English candidate ranking separates the game name from the requested rule facet, preventing a generic game section from winning merely because it contains `CS2` or `VALORANT`.
- The Thai source remains the immutable source of truth: an English overlay must have the same `content_id`, field, and source-text SHA-256.
- A known source gap produces a safe no-answer rather than a claim that a missing translation is the cause.
- Static inventory wording such as `What equipment is available in VR Zone?` no longer calls the live booking adapter.

## Approval Gate

This work deliberately does **not** mark translations as `approved`. Before the overlay can be published, an authorized reviewer must:

1. Review the 21 semantic-audit queue items against the Thai source.
2. Confirm official spellings for organizations, people, places, and event names.
3. Update `status`, `approved_by`, and `approved_at` through the localization publishing workflow.
4. Re-run the English corpus with draft preview disabled against the new approved release.

Until then, the corrected file is safe for internal draft preview only.
