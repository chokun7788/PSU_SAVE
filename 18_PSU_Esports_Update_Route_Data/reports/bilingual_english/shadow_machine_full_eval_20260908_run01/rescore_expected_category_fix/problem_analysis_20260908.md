# English Shadow: Problem Analysis (2026-09-08)

## Scope and Evidence

This analysis uses the immutable raw pipeline result for 1,600 machine-translated Thai Shadow questions. The pipeline was run with the Local LLM and Semantic RAG feature flags enabled. The questions are test-only records with `machine_translated_unreviewed`; they are not approved English knowledge for public use.

## First Correction: the Original Score Was Under-counted

The first evaluator treated an `expected_category` array as one nested value. For example, an allowed result of `games` for `[games, reservation]` was incorrectly marked as failed. The evaluator now normalizes both a single string and a list of allowed categories.

| Measurement | Raw result | Corrected result |
| --- | ---: | ---: |
| Strict pass | 909 / 1,600 | 1,065 / 1,600 |
| Strict pass rate | 56.81% | 66.56% |
| Cases corrected only by scoring fix | - | 156 |
| Timeout >= 10 seconds | 0 | 0 |
| Exception | 0 | 0 |
| Thai prose in English answer | 0 | 0 |
| P95 latency | 2.586 s | 2.586 s |
| Max latency | 7.140 s | 7.140 s |

The correction does not change an answer, route, model call, or latency. It only makes the score match the allowed-category contract.

## The Meaningful FAQ Score

The Shadow suite contains 275 `general_llm` questions such as generic API, JSON, latency, GPU, and mechanical-keyboard definitions. The current chatbot boundary policy treats these as outside the PSU FAQ scope, so the expected `general|knowledge` result conflicts with the product policy.

| Scope | Pass | Rate | Interpretation |
| --- | ---: | ---: | --- |
| All Shadow rows | 1,065 / 1,600 | 66.56% | Includes out-of-scope general knowledge. |
| PSU FAQ and compound rows | 1,065 / 1,325 | 80.38% | Better indicator for current product behavior. |
| General LLM rows | 0 / 275 | 0.00% | Expected under the current no-general-answer policy, but not aligned with the test expectation. |

Neither rate proves factual answer correctness because the Shadow corpus has no English answer gold, no required facts, and no required-answer strings. It measures route, language, validation, and latency only.

## Confirmed System Problems

### P0: English Route Priority Loses the Question Facet to a Game Name

| Expected -> actual | Cases | Example |
| --- | ---: | --- |
| `competition_rules -> games` | 69 | `What are the VALORANT competition rules?` |
| `service_fee -> games` | 29 | `What is the price of VALORANT?` |
| `multi_question|reservation|games|equipment -> service_fee` | 50 | `What PS5 games are available and what is their price?` |

**Root cause:** the English Game Resolver finds a valid game name first, then the pipeline lets the game route win over the facet in the question: competition rules, participant count, check-in, price, or booking.

**Required correction:** build the English Question Frame before route lock. It must separately store `target=VALORANT` and `facet=competition_rules|price|booking`. A valid game entity must become a target for the selected route, not force the route to `games`.

### P0: English Compound Questions Are Not Split Reliably

`multi_question` routes collapse to one branch: 50 went to `service_fee`, 14 to `games`, 10 to `service_fee` under the exact multi-question expectation, and 3 to `schedule`.

**Root cause:** English conjunction patterns (`and`, `then`, two explicit question clauses) do not consistently reach the multi-question splitter before a fast structured handler returns an answer.

**Required correction:** detect two independent intent/facet pairs before Fast/Structured early return. Return a bounded list of sub-questions, preserve their order, and merge verified answers only after both complete.

### P1: Member Lookup Fails for English/Romanized Names

`members|overview -> no_answer` occurs 25 times. Example: `What position does Prof. Dr. Nuwat Kao-pradab hold?`

**Root cause:** Thai member records do not have approved English display-name and alias overlays. The English route therefore cannot resolve a person safely.

**Required correction:** add an approved Romanization/name-alias field per member. Route `who/position/role` questions directly to `structured.members`, use exact normalized alias matching, and never route a person query into games or broad RAG.

### P1: Booking Intent Is Lost When It Contains a Game Name

`reservation -> no_answer` occurs 15 times and `games|reservation -> no_answer` occurs 6 times. Example: `What do you need to book to play TEKKEN 8?`

**Root cause:** `book`, `reservation`, and game-target signals do not form a booking intent with enough priority; absent English booking content then falls to `english_no_answer`.

**Required correction:** add token-aware English booking patterns (`book`, `booking`, `reserve`, `reservation`, `cancel`, `check in`) before game-route lock. Keep the game as a target or compatibility filter, not as the route.

### P1: Approved English Knowledge Is Still Missing

411 answers use `pipeline:missing_english_localization`. This is a safe behavior: it avoids inventing English facts. It is still a product gap because users receive no substantive English answer for many game, member, equipment, competition, and overview questions.

**Required correction:** create English localization overlays through draft -> human approval -> atomic publish. Prioritize the records behind high-risk FAQ routes: game details, competition rules, member/role records, equipment, booking policy, and current prices/schedules. Do not publish the machine-translated test questions as knowledge.

### P2: General Knowledge Policy and Evaluation Disagree

189 generic technical questions route to `no_answer`; 83 route to `equipment`. This is primarily a policy mismatch, not automatically a model failure: the implemented guard intentionally keeps the assistant focused on PSU Esports facts.

**Decision required:**

1. **FAQ-only:** retain no-answer for generic API/GPU/JSON questions, remove these 275 rows from the FAQ KPI, and add an explicit out-of-scope contract.
2. **Assistant mode:** permit a bounded Local LLM explanation fallback for generic educational questions, clearly label it as general knowledge, and prohibit it from asserting PSU facts without evidence.

### P2: Machine Translation Is Not a Gold Set

All 1,600 translations pass structural checks, but 85 English prompts are duplicates after normalization and some translations alter emphasis. Example: the Thai question about a TEKKEN 8 control can become `What are the 8 buttons in Tekken 8?`, where the `8` in the title risks being interpreted as a quantity.

**Required correction:** build a human-reviewed English Gold set for high-risk cases, especially price, rules, booking, member names, game titles containing numbers, and multi-question prompts. Shadow translation remains useful for broad regression only.

## Observability Gap

The result records show final mode and latency but not whether Semantic RAG was attempted, skipped, retrieved the wrong target, or was blocked for lack of English evidence. The mode summary contains no explicit Semantic RAG completion mode, so current logs cannot prove RAG improved an answer.

Add per-request fields: `rag_attempted`, `rag_skip_reason`, `retrieval_candidate_count`, `target_alignment`, `english_localization_state`, `llm_attempted`, `llm_skip_reason`, and per-stage latency. Never log booking PII or full user messages in performance traces.

## Recommended Fix Order

1. Keep the evaluator category-list fix and add unit cases for string/list allowed categories.
2. Fix Question Frame priority: facet and compound detection before Game Resolver route lock.
3. Add English booking and competition-rule patterns with game names retained only as targets.
4. Add member English aliases and structured lookup.
5. Decide the general-knowledge policy; align the test corpus with that decision.
6. Publish approved English knowledge overlays and build their English RAG index atomically.
7. Add English Gold factual assertions and rerun Thai 1,600 regression, English Gold, English Shadow, and concurrent HTTP load tests.

## Current Conclusion

Single-user latency and English-language safety currently pass the basic operational check. English FAQ routing and approved English knowledge coverage do not yet meet production quality. The largest engineering risks are facet-vs-game route priority, unsplit compound questions, missing member aliases, and incomplete approved localization.
