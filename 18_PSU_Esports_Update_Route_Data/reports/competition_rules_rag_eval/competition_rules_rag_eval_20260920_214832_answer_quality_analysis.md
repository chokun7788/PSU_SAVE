# Competition Rules RAG: Answer Quality Analysis

## Run Scope

- Corpus: `competition_rules_rag_ground_truth_v1`
- Cases: 528 (Thai 264, English 264)
- Runtime: RAG fallback and Local LLM enabled, trace retained for every case.
- Evaluation: route, safe outcome, game/rulebook target alignment, evidence ID alignment, validation, and a 20-second ceiling.

## Result

| Measure | Result |
| --- | ---: |
| Strict pass | 17 / 528 (3.22%) |
| Route correct | 380 / 528 (71.97%) |
| Safe outcome correct | 485 / 528 (91.86%) |
| Rulebook target correct | 181 / 528 (34.28%) |
| Evidence ID aligned | 17 / 528 (3.22%) |
| Thai strict pass | 17 / 264 (6.44%) |
| English strict pass | 0 / 264 (0.00%) |
| P50 latency | 0.191s |
| P95 latency | 2.197s |
| P99 latency | 9.504s |
| Maximum latency | 25.417s |

## What Is Working

- A direct Thai query with an exact CS2 target can return the correct fact card, answer, rulebook source, and evidence ID. Example: `กติกา CS2 เรื่องรูปแบบการแข่งขัน ว่าอย่างไร` returns `cs2_format_single_elim_bo3`.
- The broad competition-domain route is selected for most cases. The issue is primarily target/evidence control after routing, rather than total absence of a competition route.
- Safe no-answer and clarification behavior is usually non-hallucinatory at the wording level, but still needs better domain specificity.

## Critical Answer Failures

### 1. Correct route, wrong game and wrong evidence

Question: `Arena of Valor แข่งจริง กฎเกี่ยวกับรูปแบบการแข่งขัน เป็นแบบไหน`

- Expected: RoV / `competition_rules_rov_blueket_2025_men` / `competition_format`
- Actual: VALORANT sections and a VALORANT answer
- Mode: `pipeline:hybrid_guarded_rerank`

This is the highest-risk RAG error: a plausible answer is produced with a cited source, but the source belongs to another game. Any final response must reject evidence whose game/rulebook does not match the resolved target.

### 2. Competition wording leaks into the general game path

Question: `Counter-Strike 2 มีข้อกำหนดเรื่องมารยาทและพฤติกรรมผู้เล่น ไหม`

- Expected: CS2 competition rules
- Actual: `games` then no-answer for the games category

The competition intent is lost when a question is phrased as a policy rather than using an explicit term such as `กติกา` or `แข่งขัน`.

### 3. English is blocked before evidence retrieval

Question: `What do the CS2 tournament rules say about the competition format?`

- Route: `competition_rules`
- Actual response: missing approved English localization
- Returned evidence: generic `competition_rules`, not a fact/rule ID

All 264 English cases fail strict evidence alignment. The current localization gate prevents useful retrieval and makes English RAG unavailable even when Thai source evidence exists.

### 4. Two-game comparisons silently answer only one game

Question: `CS2 กับ VALORANT เรื่อง technical pause ต่างกันยังไง`

- Expected: evidence from CS2 and VALORANT
- Actual: CS2 only

The final answer must carry a required-target set. It may only compare after each target has at least one aligned evidence item; otherwise it must state which side is unavailable.

### 5. Unsupported games are substituted with unrelated information

Question: `กติกา Free Fire ของรายการนี้เรื่องโกงว่าไง`

- Expected: safe no-answer for an unsupported game
- Actual: CS2 pause policy

Unknown-game detection must run before competition fact retrieval. `unknown game` must veto all existing rulebooks instead of using the nearest rule-related card.

### 6. Reservation route can win over competition intent and break SLA

Question: `ตาม rulebook อารีน่าออฟเวเลอร์ การหลุดจากเกมหรือการเชื่อมต่อ ต้องทำยังไง`

- Expected: RoV disconnect rules
- Actual: reservation booking steps
- Latency: 25.417 seconds

This combines a routing failure with a deadline failure. Competition-rule signal and resolved game target must veto reservation candidates before they can start an expensive branch.

## Priority Fix Order

1. Enforce `QuestionFrame.game_id` and `rulebook_id` as retrieval filters before similarity/reranking. Reject cross-game evidence at validation.
2. Add an explicit `competition_rule_target` resolver for CS2, RoV/Arena of Valor/AOV, TEKKEN 8/T8, and VALORANT/Valo. It must run before generic GameResolver and reservation routing.
3. For multiple games, retrieve each target independently and require one evidence set per target before composing a comparison.
4. For unknown games, return safe no-answer and never fall back to an existing game rulebook.
5. Make English retrieval read Thai source evidence first. The absence of English localization should control output wording, not prevent target/evidence retrieval.
6. Add a hard 20-second request deadline and a competition-rule-to-reservation veto. The 25.417-second case is a production blocker.

## Release Note

The canonical rule records used by this corpus are still `pending_owner_review`. This evaluation does not activate them. It exposes the exact work needed before activating Canonical RAG safely.
