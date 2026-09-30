# English Shadow 1,600: Detailed Analysis

Run: `20260909T113600+0700`  
Corpus: `data/eval/english_shadow_1600_machine_20260908.jsonl`  
Execution: Local `Typhoon2.5-Qwen3-4B` enabled, Canonical RAG enabled, no cloud API.

## 1. What the run proves

| Metric | Result |
|---|---:|
| Source questions | 1,600 |
| Evaluator strict pass | 1,069 (66.81%) |
| Timeout at 10 seconds | 0 |
| Thai prose leaked into English | 0 |
| Answer-contract validation failed | 0 |
| Mean / P95 / P99 latency | 0.30s / 0.57s / 0.83s |
| Maximum latency | 6.42s |

The English routing path is stable and fast in this serial local evaluation. It is not yet a production-quality English knowledge experience.

## 2. Important scoring caveat

All 1,600 English questions are machine-translated Shadow data, not human-reviewed English Gold data. This is acceptable for finding route regressions, but it cannot certify English wording quality.

More importantly, `411` requests returned `pipeline:missing_english_localization`. Of those, `366` were counted as strict passes because the evaluator checked route/language/latency but did not require an answer to be available. They are safe outcomes, but not usable English answers.

Therefore:

- **66.81%** means the current evaluator contract passed.
- A conservative user-usable estimate is at most **703 / 1,600 = 43.94%** after removing the 366 route-correct-but-unavailable English answers.
- This estimate is deliberately conservative; it does not claim that all remaining 703 answers are semantically complete.

## 3. Failure Families

### A. Missing approved English knowledge: 411 requests

The canonical English projection intentionally contains zero approved records. The system correctly refuses to translate Thai source content at runtime and returns an English safety message instead.

This explains missing answers for game descriptions, game how-to-play content, competition documents, member/overview content, rules, and booking details. It is a **content-release gap**, not an embedding or vector-search failure.

Example:

> `What is the price of VALORANT?` returns a missing-localization message rather than inventing an English answer.

The safety behaviour is correct. The user experience is incomplete until a reviewer approves the English overlays and rebuilds `rag_en_approved_projection.jsonl`.

### B. English price intent loses to a named game: at least 28 direct cases

Questions such as these should request the service fee for the machine/zone that hosts the game:

- `How much does PUBG: BATTLEGROUNDS cost?`
- `What is the price of Counter-Strike 2?`
- `Horizon Call of the Mountain price`

The current pipeline resolves a known game entity first, then selects `games` and returns availability or a localization-blocked game detail. The word `price`, `cost`, or `how much` must instead create a high-priority **price operation** while retaining the game as a constraint used to infer the compatible zone. It must never treat the game title itself as a priced item unless a verified game-specific price exists.

### C. Out-of-scope technical terms leak into equipment: 85 cases

Examples:

- `What is a GPU in simple terms?`
- `What is a mechanical keyboard like?`
- `How do frame rate and resolution differ?`

The system sees `GPU`, `keyboard`, or related hardware terms and returns the entire studio equipment list. These questions ask for general technical knowledge, not for PSU equipment inventory. Since general technical explanations are outside the declared scope, the safe result should be a concise English no-answer or clarification, not an irrelevant catalogue.

Required guard: equipment routing must require a PSU/inventory signal such as `at the studio`, a zone name, `do you have`, `available`, `specification`, or a recognized catalog item plus an inventory operation.

### D. Booking English routes are incomplete: at least 15 direct cases

Examples:

- `Summarize the booking steps for me`
- `How do I book a PS5?`
- `How do I book a Nintendo Switch?`

The route reaches reservation/no-answer but there is no approved English booking-policy evidence. The system should use a structured English booking template for stable booking steps once its source fields are reviewed. Until then, the English localization message is safer than generic no-answer because it tells the user why the response is unavailable.

### E. Multi-question decomposition is not applied consistently: at least 60 cases

Examples:

- `What PS5 games are available and what is their price?`
- `What is the VR price, and how do I book it?`
- `Is it open today? How do I book a PS5?`
- `What buttons does Tekken 8 and Mario Kart 8 Deluxe have?`

The router selects only one dominant route, such as service fee, schedule, or one game's controls. It drops the remaining clause. This is a query-planning defect: English conjunction patterns (`and`, `also`, paired `what ... and what ...`) must be split before deterministic routing, then combine verified sub-answers in their original order.

### F. Control-data coverage is incomplete: 9 known control questions

The test expects controls for `It Takes Two`, but the current structured control set cannot provide verified mappings. The answer contract correctly blocks unsupported output. This is a data-coverage gap, not a reason to allow the LLM to invent controls.

### G. English price comparison and duration comparison are unsupported

Examples:

- `Which is more expensive, PS5 or Nintendo?`
- `How are VR 30-minute sessions different from VR one-hour sessions?`

The underlying service-fee data is structured enough to support both. The missing component is an English comparative-price operation that computes two verified packages and presents the difference. This should be deterministic calculation, not RAG or LLM generation.

## 4. Latency Findings

There were no requests over 10 seconds. The maximum, `6.42s`, was `Which is more expensive, PS5 or Nintendo?`; the next was `5.45s` for a VR duration comparison. These are early, complex no-answer/misroute cases and remain below SLA, but they are inefficient because the route explores unnecessary fallback work before stopping.

The ordinary path is healthy: P95 is `0.57s`. Do not raise global LLM budgets to solve the failures above. They are mostly missing English data, operation precedence, scope guarding, and multi-question planning problems. More LLM time would make the same wrong route slower.

## 5. Priority Remediation Order

1. Add English operation precedence: `price/cost/how much` beats a matched game name and maps the game to a compatible priced resource.
2. Add comparative price/duration calculator for two verified packages.
3. Require inventory intent before an English technical word can enter the equipment catalogue route.
4. Split English compound questions before route selection; execute and merge bounded sub-answers.
5. Build a reviewer workflow to approve English Canonical overlays, then rebuild the English RAG projection. Do not approve machine drafts automatically.
6. Add verified control data only for games for which an authoritative control source exists.
7. Create a human-reviewed English Gold corpus. Shadow translations should remain a regression detector only.

## 6. Acceptance Tests for the Fixes

| Case | Expected behaviour |
|---|---|
| `How much does VALORANT cost?` | Service-fee route; explain the relevant playable resource/package, no game-price invention. |
| `Which is more expensive, PS5 or Nintendo?` | Deterministic comparison of verified packages. |
| `What is a GPU?` | Out-of-scope English no-answer; never inventory dump. |
| `How do I book a PS5?` | Approved English booking steps or explicit localization-pending message. |
| `What PS5 games are available and what is their price?` | Two verified sections: game list + fee. |
| `What controls does It Takes Two use?` | No-answer unless verified control data is added. |
| New approved game/rule record | Appears in English RAG only after reviewer approval and rebuild. |

## 7. Files

- `summary.json`: machine-readable run summary.
- `results.jsonl`: each question, answer, route, mode, timing, and evaluator failure.
- This file: interpretation and implementation priorities.
