# Competition Rules RAG: Trace Root-Cause Analysis

**Run:** `competition_rules_rag_eval_20260920_214832`  
**Scope:** 528 competition-rule questions, Thai 264 and English 264  
**Mode:** `--rag-fallback --allow-llm --include-trace`  
**Purpose:** Explain *why* the current pipeline produced each representative wrong outcome. This is a diagnostic report, not a claim that the canonical rulebooks are already active in production.

## How to read this report

- **Confirmed from trace** means the event appears in the per-case runtime trace.
- **Confirmed from evaluation** means the answer/evidence/latency field in the saved result proves it.
- **Inference to verify** is a likely internal cause that needs a focused unit test or code inspection before changing behavior.

## Overall signal

| Measure | Result | Meaning |
|---|---:|---|
| Strict pass | 17 / 528 (3.22%) | Route, outcome, target and evidence all correct at once |
| Route correct | 380 / 528 (71.97%) | The category often looks right, but that alone does not ensure the right rulebook |
| Outcome correct | 485 / 528 (91.86%) | Many wrong answers still look like valid answers rather than a safe no-answer |
| Target correct | 181 / 528 (34.28%) | Target identity is lost or not enforced often |
| Evidence correct | 17 / 528 (3.22%) | Main failure: returned evidence rarely matches the requested game/facet |
| Thai strict pass | 17 / 264 (6.44%) | Some legacy Thai fact cards match exactly |
| English strict pass | 0 / 264 (0.00%) | English localization guard returns before target-grounded retrieval |
| P95 / maximum latency | 2.197 s / 25.417 s | One wrong structured branch alone violated the 20-second run ceiling |

The important conclusion is that a response may be fluent, have a source, and even have category `competition_rules`, while still being unsafe. The missing invariant is: **every competition answer must prove that its evidence belongs to every game and rulebook named in the question.**

---

## 0. Baseline: the path that works

### Case `COMP-RAG-TH-001`

**Question:** `กติกา CS2 เรื่องรูปแบบการแข่งขัน ว่าอย่างไร`  
**Expected:** CS2 / `competition_format` / `competition_rules_cs2_psu_phuket_2026`  
**Actual:** Correct `pipeline:competition_fact_card`, 2.457 s, evidence `cs2_format_single_elim_bo3`.

### Trace sequence

1. Active route selection identifies `competition_rules / competition_rules_lookup`.
2. Universal intent remains `competition_rules / rule_lookup`.
3. `question_frame` resolves the game to exact `Counter-Strike 2`, confidence 0.96.
4. Capability selection chooses `retrieval.competition_fact_cards`.
5. Fact-card retrieval records `game=Counter-Strike 2; intent=format` and returns the CS2 format card.
6. Validator returns `ok`.

### Why this one succeeds

**Confirmed from trace:** the intent is stable from routing through retrieval, the game alias resolves exactly, and the fact-card search is called with the same game and facet. This is the target behavior the failing examples below do not preserve.

---

## 1. Competition wording is overwritten by a generic game lock

### Case `COMP-RAG-TH-011`

**Question:** `Counter-Strike 2 มีข้อกำหนดเรื่องมารยาทและพฤติกรรมผู้เล่น ไหม`  
**Expected:** CS2 / `conduct` / answer from CS2 rulebook  
**Actual:** `games`, `pipeline:no_answer`, 1.484 s.

### What happened, step by step

1. **Correct first classification.** `active_route_selection` initially returns `competition_rules / competition_rules_lookup`.
2. **Route gets overwritten.** `semantic_route_refiner` emits `skipped_exact_target_lock`, but the metadata locks the request to `games / game_detail_lookup` with reason `exact_known_game_target`.
3. **Intent now follows the wrong domain.** `universal_intent` becomes `games/count`, although the wording asks about player conduct and not game availability or a count.
4. **Question frame inherits the error.** It is built as `operation=game_detail; domain=games` instead of `competition_rule_lookup`.
5. **Wrong capability is allowed.** Candidate selection picks `structured.reservation`; its precondition allows it because the request is now treated as reservation-like.
6. **Fallback cannot repair the target.** Structured validation fails, then hybrid retrieval runs, but validation again fails and the pipeline falls through to `pipeline:no_answer`.

### Root cause

**Confirmed from trace:** `exact_known_game_target` has higher priority than the rule-policy signals. Recognizing a game name should identify the target, not replace the domain from `competition_rules` with `games`.

**Inference to verify:** the English/Thai keyword classifier may be treating a broad word such as `มี` or the request form as a game-count signal. Regardless, that later classifier must be unable to override a rulebook-intent lock.

### Why the answer becomes a no-answer

Once the question frame says `games/game_detail`, no eligible structured game fact exists for “conduct”. The subsequent retrieval results also fail validation, so the safe outcome is no-answer. The safe outcome is preferable to inventing a rule, but it occurs for the wrong reason.

### Required invariant

If a question includes a competition-policy signal such as `กติกา`, `ข้อกำหนด`, `มารยาท`, `พฤติกรรม`, `rule`, `roster`, `pause`, `forfeit`, or `anti-cheat`, an exact game resolution must be attached as the **competition target**. It must not force the `games` route.

---

## 2. RoV target is resolved correctly, then retrieval answers with VALORANT evidence

### Case `COMP-RAG-TH-116`

**Question:** `Arena of Valor แข่งจริง กฎเกี่ยวกับรูปแบบการแข่งขัน เป็นแบบไหน`  
**Expected:** RoV / `competition_format` / `competition_rules_rov_blueket_2025_men`  
**Actual:** `competition_rules`, `pipeline:hybrid_guarded_rerank`, 1.344 s; evidence references VALORANT rulebook sections 1 and 8.

### What happened, step by step

1. Route and universal intent are both correctly classified as `competition_rules / rule_lookup`.
2. `question_frame` resolves the target as exact `Arena of Valor (RoV)`.
3. `target_context` explicitly carries `target_id=competition_game_arenaofvalorrov`, score 1.0.
4. Capability selection correctly chooses `retrieval.competition_fact_cards`.
5. **The target is lost at retrieval.** `fact_card_retrieval` records `game=VALORANT; intent=format`, not RoV.
6. No acceptable fact-card answer is found (`raw_hit_count=0`), so hybrid retrieval starts.
7. Hybrid retrieval returns four items whose evidence IDs and rulebook references are all VALORANT.
8. The validator returns `ok`, because it validates response structure/evidence presence but does not enforce that evidence game and rulebook equal the resolved target.

### Root cause

**Confirmed from trace:** this is not a failed alias lookup. RoV was resolved correctly before capability selection. The fault is between `QuestionFrame/target_context` and fact-card/hybrid retrieval filtering.

**Inference to verify:** the fact-card retriever likely falls back to a global facet match when it does not find an exact RoV fact; `format` then ranks a VALORANT card. The hybrid index is also searched globally, so its denser VALORANT sections can win similarity scoring.

### Why this is more serious than a no-answer

The answer is fluent, categorized as a competition answer, and cites a real local rulebook. Yet it asserts VALORANT rules as RoV rules. This is a false, apparently well-supported answer, and should be blocked by the final answer contract.

### Required invariant

For a single-game rule question, retrieve only documents where:

```text
evidence.game_id == QuestionFrame.game_id
AND evidence.rulebook_id is active for that game
AND evidence.facet matches the requested facet
```

If no item remains, return a target-specific no-answer. Never widen to another game merely to provide an answer.

---

## 3. English stops before the system even tries to retrieve the Thai source

### Case `COMP-RAG-EN-001`

**Question:** `What do the CS2 tournament rules say about the competition format?`  
**Expected:** CS2 / `competition_format` / English source-grounded answer  
**Actual:** `competition_rules`, `pipeline:missing_english_localization`, 0.278 s.

### What happened, step by step

1. Locale resolution correctly chooses English: `requested=en; effective=en`.
2. Active route selection correctly identifies `competition_rules / competition_rules_lookup`.
3. Immediately after entity extraction, `bilingual_route` produces `pipeline:missing_english_localization`.
4. The pipeline builds the response without `question_frame`, target resolution, fact-card retrieval, canonical RAG retrieval, or evidence validation.
5. It returns a generic English message saying the localization is not approved, with the broad site source.

### Root cause

**Confirmed from trace:** the localization gate runs before retrieval. Therefore, the system cannot determine whether the Thai source has the requested CS2 rule even though that source exists and Thai can answer it.

**Confirmed from evaluation:** all 264 English cases have no strict pass under this run. This is primarily a control-flow/data-publication issue, not evidence that every English query fails language understanding.

### Why the answer is short and generic

The current design intentionally forbids runtime translation. That safety rule is valid. However, it was implemented as an early exit, so it also suppresses target identification and source-grounded evidence discovery.

### Required invariant

Language controls wording, not evidence selection:

```text
Resolve target and retrieve approved Thai source evidence first.
Then select an approved English localization overlay for the same content_id + field.
If the overlay is absent or stale, respond in English with a target-specific
"English wording not approved yet" outcome and the exact original Thai source.
```

This preserves the no-runtime-translation rule without hiding the requested source target.

---

## 4. Comparison questions are treated as a single-target question

### Case `COMP-RAG-TH-263`

**Question:** `CS2 กับ VALORANT เรื่อง technical pause ต่างกันยังไง`  
**Expected:** CS2 and VALORANT / `pause_timeout`, evidence from both rulebooks  
**Actual:** only CS2 fact `cs2_pause_policy`, 0.307 s.

### What happened, step by step

1. The category and universal intent are correct: `competition_rules / rule_lookup`.
2. `question_frame` reports `allows_multiple_targets=False` even though two game names and a comparison form (`ต่างกันยังไง`) are present.
3. `target_context` contains only `VALORANT` at this point.
4. Fact-card retrieval subsequently uses `game=Counter-Strike 2; intent=pause` and returns only `cs2_pause_policy`.
5. The validator returns `ok`, because one valid fact exists. The evaluator rejects it because both expected rulebook targets are missing.

### Root cause

**Confirmed from trace:** the pipeline has no preserved target set. It reduces a two-game question to one target, then retrieval can independently drift to another game. There is no “retrieve one evidence set per named target” requirement.

**Inference to verify:** target extraction may store one winner in a scalar field, causing later aliases to overwrite or be ignored. Either way, a comparison cannot use a single `target_id` representation.

### Why the final answer looks plausible but is incomplete

CS2 pause policy is a real, supported fact. The failure is omission: it does not answer the comparison and says nothing verified about VALORANT. The validator currently checks “has evidence”, not “has evidence for every requested target”.

### Required invariant

When comparison or conjunction signals are present, produce a target plan:

```text
targets = [CS2, VALORANT]
for each target:
    retrieve within that target's rulebook filter
require one verified evidence set per target
only then compose a comparison
```

If either game lacks evidence, state which side is unavailable and do not infer the difference.

---

## 5. An unsupported game is allowed to borrow a CS2 rule

### Case `COMP-RAG-TH-262`

**Question:** `กติกา Free Fire ของรายการนี้เรื่องโกงว่าไง`  
**Expected:** no-answer because Free Fire is outside the four supplied rulebooks  
**Actual:** `competition_rules`, `pipeline:competition_fact_card`, CS2 evidence `cs2_pause_policy`, 0.385 s.

### What happened, step by step

1. Initial route selection returns `general / unknown_domain_query`, which is reasonable because Free Fire has no supported rulebook alias.
2. The model-first intent review is attempted because the route is weak, but the trace records `llm unavailable or invalid json`.
3. The fallback heuristic labels it `general / rule_lookup`.
4. `question_frame` changes the domain to `competition_rules` with `target_status=unknown`.
5. Despite that unknown target status, capability selection allows `retrieval.competition_fact_cards`.
6. Fact-card retrieval records no game and no intent filter, then returns a generic top candidate: `cs2_pause_policy`.
7. Validator returns `ok`; it does not require an explicit supported-game match when the user named a game.

### Root cause

**Confirmed from trace:** the target is explicitly `unknown`, yet global competition fact retrieval remains enabled.

**Confirmed from trace:** an unavailable/invalid LLM review falls back to heuristic behavior, but there is no deterministic unknown-game safety gate after that fallback.

### Why this answer is unsafe

The user did not ask for an unscoped anti-cheat policy. They named Free Fire. Returning any other game's rule changes the meaning of the request.

### Required invariant

If the text explicitly names a game-like entity and the competition target resolver returns `unknown_explicit`, stop before global fact-card/RAG retrieval:

```text
status = no_answer
reason = unsupported_competition_rulebook
```

The system may list the supported rulebooks only if that list is explicitly requested; it must not substitute one.

---

## 6. A competition disconnect rule is routed to reservation, then the slow branch exceeds the SLA

### Case `COMP-RAG-TH-126`

**Question:** `ตาม rulebook อารีน่าออฟเวเลอร์ การหลุดจากเกมหรือการเชื่อมต่อ ต้องทำยังไง`  
**Expected:** RoV / `disconnect` / competition rule answer  
**Actual:** `reservation`, `pipeline:structured_reservation_fact`, booking steps, 25.417 s.

### What happened, step by step

1. Preprocessing completes in 0.123 s.
2. `active_route_selection` immediately chooses `reservation / booking_policy`.
3. Semantic route refinement is skipped, so no later stage reconsiders the explicit `rulebook` signal.
4. Universal intent confirms `reservation / how_to`, with the metadata reason that reservation route overrides entity/game domain.
5. The question frame becomes `operation=booking_lookup; domain=reservation`, with no game target.
6. Candidate selection chooses `structured.reservation`; its precondition allows the tool.
7. `structured_tool_execution` consumes **24.845 s** and returns booking steps.
8. The response validates structurally and is returned at 25.417 s, exceeding the 20-second ceiling.

### Root cause

**Confirmed from trace:** `reservation route overrides entity/game domain` is the explicit decision that turns a rulebook question into booking help.

**Confirmed from trace:** the expensive structured reservation call is allowed to run for 24.845 s even though the trace starts with a 20-second global timeout.

**Inference to verify:** the phrase `ต้องทำยังไง` and words around connection loss are triggering booking/how-to features strongly enough to overpower `ตาม rulebook`. The RoV Thai alias spelling may also be weaker than the reservation keyword signals.

### Why it times out even though a 20-second budget is logged

The trace proves the deadline is recorded (`global_timeout_sec=20`) but not enforced as a hard interrupt inside `structured_tool_execution`. The budget is observability here, not cancellation.

### Required invariant

1. An explicit rulebook signal must veto `structured.reservation` unless the user is actually asking about booking/cancellation/payment.
2. Every external/structured stage must receive remaining budget and must be terminated or skipped before it can overrun the response ceiling.
3. A controlled timeout must return a safe outcome, not an answer after the deadline.

---

## 7. The current validator accepts evidence that is merely present, not evidence that answers this request

### Cross-case pattern

The following cases all end with `validation: ok` while failing the evaluation's target/evidence contract:

| Case | Request target | Evidence actually accepted | Why it should have been rejected |
|---|---|---|---|
| `TH-116` | RoV format | VALORANT rulebook sections | wrong game and wrong rulebook |
| `TH-263` | CS2 + VALORANT pause comparison | CS2 only | target coverage incomplete |
| `TH-262` | Free Fire anti-cheat | CS2 pause card | unsupported named target replaced |
| `TH-126` | RoV disconnect | booking steps | wrong domain, target and source |

### Root cause

**Confirmed from trace:** validation is `ok` after the wrong retrieved/structured evidence is already selected in these cases.

**Confirmed from evaluation:** `outcome_ok` is 91.86% but `evidence_ok` is only 3.22%. This large gap is the numerical signature of an answer-shape validator instead of a target-grounding validator.

### Required answer contract

Before a competition answer is published, validate all of the following against the original `QuestionFrame`:

```text
1. route/category == competition_rules
2. every named game has a resolved, supported target
3. every evidence item has a permitted game_id + rulebook_id
4. evidence facet is compatible with the requested facet
5. comparison asks require coverage for every target
6. unknown explicit game -> no-answer, never cross-game substitution
7. evidence language/localization status is acceptable for output language
```

Failing any of these must bypass repair-by-guessing and return clarification or no-answer.

---

## 8. Canonical rulebooks are available as evaluation data but are not yet a universally active runtime source

### What the run shows

**Confirmed from trace:** successful Thai cases use legacy `competition_fact_cards`, for example `cs2_format_single_elim_bo3`. The trace reports `skipped_for_active_canonical=0`; it does not prove a canonical release was used for every query.

**Confirmed from registry state (earlier audit):** the four canonical rulebook records are `pending_owner_review`.

### Consequence

Even after routing is corrected, not every new standardized facet may have an active approved runtime projection. That can correctly lead to a target-specific no-answer, but it must never lead to global fallback into another game's fact card.

### Required publication rule

Only an approved release/version becomes searchable. When an owner publishes a new or revised rulebook, build the structured projection and RAG chunks atomically for the same release. Preserve the old approved version until the new one passes validation.

---

## Fix order derived from the traces

### P0: Stop false facts immediately

1. Enforce `game_id + rulebook_id + facet` evidence validation before final answer publication.
2. Block global competition retrieval for `unknown_explicit` named games.
3. Add a competition-rule veto before reservation/game structured capabilities.
4. Enforce a hard deadline in `structured_tool_execution`.

### P1: Preserve the target throughout the pipeline

5. Add `CompetitionTargetResolver` before generic game routing. It must return single, multiple, ambiguous, or explicit-unknown targets.
6. Keep `QuestionFrame.targets` as a list; never reduce a comparison to a scalar target.
7. Filter fact cards and RAG chunks by target before similarity/reranking.

### P2: Make English source-grounded rather than an early generic exit

8. Retrieve the same approved Thai evidence first.
9. Match an approved English localization overlay by `content_id + field + source hash`.
10. If absent, return a target-specific English localization-pending response with the exact Thai rulebook source, not a generic site source.

### P3: Improve recall after correctness is protected

11. Add aliases for the four rulebooks to the dedicated competition target resolver, including Thai spellings and common English short forms.
12. Add focused regression tests for the seven cases in this report before expanding wording variants.

## Regression cases that must pass before a rerun

| Case | Required result |
|---|---|
| `COMP-RAG-TH-011` | CS2 conduct answer from CS2-only evidence |
| `COMP-RAG-TH-116` | RoV-only format evidence, or target-specific no-answer if unavailable |
| `COMP-RAG-EN-001` | CS2 evidence retrieval before English localization decision |
| `COMP-RAG-TH-263` | comparison with both CS2 and VALORANT evidence, or explicit partial-data outcome |
| `COMP-RAG-TH-262` | Free Fire unsupported-rulebook no-answer; no CS2 evidence |
| `COMP-RAG-TH-126` | RoV disconnect answer or safe deadline outcome; never booking steps |
| `COMP-RAG-TH-001` | remains a passing CS2 format baseline |

## Links

- [Raw evaluation result](competition_rules_rag_eval_20260920_214832.json)
- [Run summary](competition_rules_rag_eval_20260920_214832_summary.json)
- [Earlier answer-quality analysis](competition_rules_rag_eval_20260920_214832_answer_quality_analysis.md)
- [Competition RAG ground truth](../../data/eval/competition_rules_rag_ground_truth_v1.jsonl)
