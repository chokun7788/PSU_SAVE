# Competition Rules RAG: V2 Natural-language Ground Truth Analysis

## Scope

- Corpus: `data/eval/competition_rules_rag_ground_truth_v2_expanded.jsonl`
- 282 source-preserving paraphrase cases: 141 Thai and 141 English.
- Each case retains the route, safe-outcome contract, rulebook target, and
  evidence contract of a reviewed v1 parent case.  The wording is new and is
  intended to resemble participant questions instead of internal test labels.
- Runtime setting: RAG fallback enabled, Local LLM disabled.  This measures
  routing and evidence selection without model-generated wording changing the
  factual result.

## Latest Result

| Locale | Passed | Total | Evidence-aligned | Note |
| --- | ---: | ---: | ---: | --- |
| Thai | 117 | 141 | 117 | 83.0%; all but one failure retained the correct competition route and answer status. |
| English | 113 | 141 | 113 | 80.1%; English now uses the same target-first source ranking as Thai. |

There were no latency failures.  The slowest first request in each isolated
batch included cold-start work; ordinary targeted source retrieval completed
well below the 20-second request ceiling.

## Confirmed Findings

### 1. Natural wording previously bypassed competition routing

**Confirmed from trace:** questions such as “ผู้เล่น VALORANT มีข้อควรระวัง
เรื่องการวางตัวอะไร” previously entered `games/game_detail_lookup` and then
spent about seven seconds in unrelated hybrid game retrieval.

**Fix implemented:** `looks_like_competition_rule_query()` now accepts a
registered competition-game target plus bounded participant context, including
conduct, eligibility, roster, registration, equipment, map pool, check-in,
match configuration, penalty, protest, and their English equivalents.

**Verification:** all answerable v2 cases are now recognized as competition
queries before target locking.  The unintended seven-second game RAG detour no
longer occurs for the tested wording.

### 2. Route and target can be correct while source section is wrong

**Confirmed from reports:** 23 of 24 remaining Thai failures and 40 of 42
remaining English failures still return `competition_rules` with an answer.
They fail because the evidence ID is from the correct rulebook but not the
Gold-allowed section.

**Cause:** imported chunks have inconsistent legacy tags.  For example,
player-etiquette chunks can be tagged `eligibility`, while generic Thai
character n-grams such as `ผู้เล่น` or `การแข่งขัน` can outrank a more specific
section title.

**Fix implemented:** retrieval now derives canonical facets from source title,
text, and tags at query time.  A matching facet receives a strong bounded
ranking boost; a concrete non-matching facet is penalized.  The source evidence
window increased from four to six sections so a heading and its detail chunk
can remain together.  This raised Thai from 108/141 to 117/141 and English
from 99/141 to 113/141 in the same v2 corpus.

### 3. English and Thai formerly selected source sections independently

**Confirmed from code:** English competition responses first ranked English
localization rows by raw English token overlap, while Thai used curated
target-first RAG.  The two paths could cite different sections for the same
intent.

**Fix implemented:** English now receives the same target-filtered source
ranking as Thai.  Localization is only a display overlay.  When the ranked
Thai source has no approved English localization, the system returns the
existing source-grounded English localization-pending response instead of
borrowing a lower-ranked translated chunk.

### 4. Exact game target lock could undo a competition route later in pipeline

**Confirmed from trace:** `Tekken 8 มี setting ที่ผู้เล่นต้องใช้เหมือนกันไหม`
could be initially recognized as a rule question and then restored to the
ordinary game-detail route by the later exact-game lock.

**Fix implemented:** the later restoration now respects an already-confirmed
competition signal, matching the earlier target-lock veto.

## Remaining Failures: Data Contract, Not a Safe Candidate for Alias Patches

The remaining clusters need a content and Gold review rather than more query
aliases:

1. **VALORANT conduct/fair-play/in-match/team-size (12 Thai, 9 English):**
   natural questions ask for generic behaviour or roster guidance, while v1
   Gold often permits only chunks about bug exploits, technical pauses, or
   competition-area rules.  The topic labels and permitted source sections do
   not express the same proposition.
2. **CS2 fair-play, penalty matrix, pre-match, match settings (13 Thai,
   12 English):** the requested semantic facet is often present, but its
   allowed Gold chunk ranks after a closely related section.  A reviewed
   section-to-facet registry is needed to distinguish a heading from the
   actual rule detail.
3. **RoV disconnect (three cases in each locale):** current source text may
   contain the connection policy across adjacent chunks.  The Gold accepts one
   narrow chunk while the answer has another correct chunk from the same
   rulebook.  Review the allowed evidence set as a rule-section bundle.
4. **Safe outcome variants (four English cases):** a few inherited v1 safe
   cases share the same `safe` group but do not have an identical expected
   outcome after paraphrase.  They should be split into explicit
   `clarification_required` and `no_answer` v3 cases.

## Next Data Fixes (Do Not Infer New Facts)

1. Create `competition_rule_section_registry.jsonl` from the source rulebooks.
   Each entry must contain `rulebook_id`, `source_chunk_id`, one or more
   reviewed `facets`, `section_role` (`heading`, `rule_detail`, or `table`),
   `approved_by`, and source text hash.
2. Rebuild the canonical RAG projection from this registry.  A source hash
   change must invalidate its facet approval.
3. Review the v1 Gold rows whose `expected_facet` and source chunk disagree.
   Preserve them as historical baseline; create v3 Gold only after approval.
4. Split compound requests such as “fair play and prohibited actions” into
   either a multi-facet contract or a target-specific clarification contract.
5. Re-run v2, then run the original v1 regression.  Do not claim a strict
   retrieval improvement merely by broadening allowed IDs without reviewer
   confirmation.

## Files and Reports

- Corpus: `data/eval/competition_rules_rag_ground_truth_v2_expanded.jsonl`
- Manifest: `data/eval/competition_rules_rag_ground_truth_v2_expanded_manifest.json`
- Builder: `tools/build_competition_rules_rag_ground_truth_v2.py`
- Latest Thai batch reports: `competition_rules_rag_eval_20260921_131946.json`
  through `competition_rules_rag_eval_20260921_132032.json`
- Latest English batch reports: `competition_rules_rag_eval_20260921_132048.json`
  through `competition_rules_rag_eval_20260921_132119.json`
