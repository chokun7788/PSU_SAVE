# Competition Rules RAG: Remediation Iteration 2026-09-21

## Scope

This iteration changed retrieval safety and English localization provenance for
the four supported competition rulebooks. It did not add, infer, or publish a
new tournament rule.

## Implemented Changes

1. **Direct-source facet detection**
   - `_competition_row_intents()` now derives a section facet from its title,
     source text, answer, and evidence fields only.
   - Import tags are no longer treated as proof. A legacy row tagged
     `penalty_matrix` but containing a match-schedule statement is therefore
     classified as `schedule`, not a penalty table.

2. **Narrow evidence guards**
   - A check-in/on-site question requires an arrival, check-in, or explicit
     participation-confirmation instruction.
   - A generic in-match-process question requires an operational instruction
     such as reporting a result, room assignment, or notifying an official.
   - Questions about named starters and substitutes still require both pieces
     of evidence in the same retrieved material.

3. **English/Thai evidence parity**
   - English competition responses run `competition_hits_cover_intent()`
     before localization.
   - English can no longer report a translation gap merely because it found
     an unrelated section from the correct game.
   - English overlays now retain the underlying canonical rule identifier in
     their response hits.

4. **Additive draft-preview registry**
   - `PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW` now overlays draft records onto
     the published registry instead of replacing it.
   - A narrow eight-record review batch was generated for directly supported
     CS2 conduct, CS2 penalty table, CS2 schedule, and RoV disconnect text.
   - The batch remains draft-only and is not visible to normal chatbot users.

## Verification

### Automated tests

- `20` focused unit/release-safety tests passed.
- Localization registry smoke test passed, including source-hash invalidation
  and the additive-preview regression test.

### Latest full Ground Truth, normal runtime configuration

| Locale | Passed | Total | Result | Observation |
| --- | ---: | ---: | ---: | --- |
| Thai | 113 | 141 | 80.1% | Fewer cross-facet answers; expected-answer rows with no direct source now safely decline. |
| English | 108 | 141 | 76.6% | Same strict source guard plus unresolved approved-localization coverage. |

Raw reports:

- `competition_rules_rag_eval_20260921_201631.json` (Thai)
- `competition_rules_rag_eval_20260921_201611.json` (English)

Both runs completed under the 20-second per-case ceiling. The slowest observed
Thai case was about 2.26 seconds; English cases stayed below one second.

## What the Score Means

The pre-change raw score was higher in several cases because the pipeline
answered with a nearby section from the correct game, or because an English
"translation not available" message was treated as an answer-shaped outcome.
That is not acceptable evidence grounding. This iteration intentionally
chooses `no_answer` for these cases:

- VALORANT conduct and fair-play rules: no direct rule text in the imported
  source establishes the requested conduct policy.
- VALORANT in-match contact/procedure: the source has settings and pause
  material, but no instruction saying who to notify for a general issue.
- CS2/RoV check-in: the current imported excerpts do not establish a specific
  check-in or on-site arrival procedure.
- CS2/RoV/VALORANT starter-and-substitute questions: the exact roster split
  is not established by the retrieved evidence.

These are **source coverage gaps**, not a reason to make up a rule.

## Gold Contract Issues Confirmed

Some expected evidence selectors point at a heading or a different section
than the text that contains the answer. Examples requiring source-reviewed
Gold reconciliation:

- CS2 penalty table: current Gold allows `s55_c01` ("permanent ban"), while
  the actual table is `s54_c01`.
- RoV disconnect: current Gold points to `s08_c02`; the directly retrieved
  disconnect procedure is in `s06_c01` through `s06_c03`.
- CS2 schedule: the current answer comes from `s15_c01`; Gold permits the
  broad schedule heading `s07_c01` only.

Do not edit raw Ground Truth merely to raise a score. Create a versioned
source-reviewed evidence-alias manifest only after comparing every changed
selector to the rulebook source.

## Next Safe Implementation Order

1. Obtain or ingest source text for missing VALORANT conduct, match-contact,
   and roster rules; otherwise formally classify those topics as unsupported.
2. Review the eight English draft records, then approve and publish them with
   the standard atomic localization workflow.
3. Build a versioned evidence-alias manifest for the three confirmed
   Gold/source mismatches above and rerun both locales.
4. Add an explicit multi-rulebook comparison renderer so CS2-versus-VALORANT
   pause questions return one verified block per game rather than the first
   game only.
5. Expand the approved English overlay only for source-backed sections, then
   run the full corpus again.
