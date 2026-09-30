# Current LLM Flow Evaluation Analysis

**Date:** 2026-08-31  
**Model:** `scb10x/typhoon2.5-qwen3-4b` via local Ollama  
**Embedding / Semantic RAG:** `psu-bge-m3:q8_0`  
**LLM-only scope:** This report deliberately does **not** run the `No-LLM` benchmark. Every pipeline execution used the current model-enabled Flow. Cases stopped by the keyboard-layout guard were intentionally not sent to the model.

## 1. Runs and Artifacts

| Run | Scope | Main output |
|---|---:|---|
| Current Flow benchmark | 1,600 FAQ / product cases | `model_benchmark/20260831_current_flow_full1600_llm/` |
| Keyboard Guard + Current Flow | 500 synthetic keyboard-error / normal-input cases | `keyboard_input_pipeline_eval/20260831_current_flow_guard_llm500/` |
| Previous comparable model run | 1,600 cases, model enabled | `model_benchmark/20260823_pipeline_fixes_full1600_final_v3/` |

Per-case logs are saved as `results.jsonl`, `results.csv`, `results.json`, and `summary.json`. The keyboard run also contains `analysis.json` and a resumable `partial_results.jsonl` checkpoint.

## 2. Configuration Under Test

```text
Question -> Keyboard Guard (evaluation simulation) -> Current Pipeline
  -> Fast / Structured OR Semantic RAG OR Local LLM
  -> Evidence + Draft -> optional Facts Composer
  -> Validation / Answer Contract -> Final Answer

Local LLM: Typhoon2.5 Qwen3 4B
Context: 2,048 tokens
Generation limit: 128 tokens
Global request budget: 9 seconds
Semantic RAG: enabled
Facts Composer: enabled
No-LLM baseline: not run
```

The 500-case keyboard test simulates the intended early guard. At the time of this test, the production web API has not yet called this guard before the chatbot pipeline, so the score must not be described as a live production result.

## 3. Result: 1,600 Current-Flow Cases

| Metric | Previous model-enabled run | Current Flow | Change |
|---|---:|---:|---:|
| Pass rate | 99.94% (1,599 / 1,600) | 94.31% (1,509 / 1,600) | -5.63 percentage points |
| Average score | 99.99 | 98.47 | -1.52 |
| Average latency | 0.773 s | 2.705 s | +1.932 s |
| Median latency | 0.447 s | 0.474 s | +0.027 s |
| P95 latency | 2.314 s | 4.783 s | +2.469 s |
| Maximum latency | 6.325 s | 1,820.695 s | deadline enforcement failure |
| Total elapsed time | 1,253.54 s | 4,343.67 s | +3,090.13 s |
| Logged LLM calls | 349 | 542 | +193 |

### What uses the model in this run

Actual successful model calls in the 1,600-case run:

| Model role | Calls | Purpose |
|---|---:|---|
| `general_llm` | 275 | General, non-PSU or open-ended questions |
| `facts_composer` | 126 | Compose supported evidence into Thai answer drafts |
| `universal_intent` | 84 | Intent / route review where the heuristic requests help |

There were also 57 `facts_composer` attempts skipped by the health/cooldown guard after earlier failures. This is safe behavior, but it shows the Composer is not stable enough to be treated as a required step.

### Accuracy regression

There are **90 regressions** compared with the prior model-enabled 1,600 run and **no improvements**. The largest regression groups are:

| Group | Regressed cases | Main pattern |
|---|---:|---|
| Games | 43 | Exact game facts fell into Semantic RAG or returned incomplete details |
| Competition rules | 11 | Structured fact-card answers fell into RAG |
| Members | 10 | Person/role lookups fell into RAG or timed out |
| Game availability | 9 | Exact compatibility answers fell into RAG |
| Game controls | 8 | Exact control mappings fell into RAG |

The most common route change was:

```text
Structured exact answer -> Semantic RAG dynamic answer
```

This is the main accuracy issue. `Semantic RAG` is valuable for new long-form documents, but it must not replace a verified Structured record for questions that ask for an exact game, control, service, person, price, or availability fact.

### Latency and deadline failure

Ten cases exceeded the 9-second target. Most serious examples:

| Case | Expected fast route before | Current result | Time |
|---|---|---|---:|
| `MB-1123-SF-154` | Deterministic price calculator | Timeout / no-answer | 1,820.695 s |
| `MB-0507-M-018` | Member person lookup | Timeout / no-answer | 70.134 s |
| `MB-0503-M-014` | Member role lookup | Timeout / no-answer | 61.887 s |
| `MB-0618-C-007` | Multi-question split | Timeout / no-answer | 28.549 s |

For `MB-1123-SF-154`, trace timing shows `candidate_decisions` alone took 1,820.500 seconds. The system only checked the deadline **after** that synchronous work ended. Therefore, the current Global Deadline detects an overrun but does not interrupt a blocking stage. It is not yet a true 9-second product guarantee.

## 4. Result: 500 Keyboard-Input Cases

### Guard results

| Metric | Result |
|---|---:|
| Dataset size | 500 |
| Guard action accuracy | 100.00% |
| Guard block / allow accuracy | 100.00% |
| Hard-blocked before model | 240 |
| Sent to current chatbot Flow | 260 |

The perfect guard result applies only to this synthetic, generated dataset. It verifies the defined thresholds against the test cases; it does **not** prove 100% performance on real user traffic.

High-confidence keyboard-layout mismatches such as `g]jo` are intentionally blocked and answered with a request to type again. They do not consume Model queue time. The test does **not** automatically translate or repair the user text.

### Quality of cases that entered the Flow

Only 175 of the 260 allowed cases have a mapped FAQ source contract, so these are the only ones that can be scored for answer correctness.

| Input family | Entered pipeline | Source-contract pass rate | P95 pipeline time | Notes |
|---|---:|---:|---:|---|
| Normal valid text | 50 | 98.00% (49 / 50) | 7.340 s | Reference quality |
| Thai internal repeated character | 60 | 70.00% (42 / 60) | 9.426 s | Largest typo-related quality drop |
| Thai repeated mark / vowel | 40 | 75.00% (30 / 40) | 1.565 s | Route / entity errors remain |
| Latin internal repeated character | 25 | 84.00% (21 / 25) | 2.021 s | Game/equipment names can miss aliases |

Overall for the 500 set:

| Metric | Result |
|---|---:|
| Source-contract pass rate | 81.14% (142 / 175) |
| Average time: all 500 | 1.173 s |
| P95: all 500 | 6.085 s |
| Average time: 260 pipeline cases | 2.256 s |
| P95: 260 pipeline cases | 7.673 s |
| Cases over 9 seconds | 8 |

The lower score for repeated-character inputs is expected because the current Guard **detects but does not correct** them. For example, `จอองแล้วแก้ไขได้ไหม` can lose the booking intent and route incorrectly. This confirms the user's concern: simply sending typo text into the normal pipeline still causes factual route errors.

### Models used in the 500-case run

| Model role | Actual calls |
|---|---:|
| Universal Intent review | 64 |
| Facts Composer | 21 |
| General Local LLM | 28 |
| RAG LLM fallback | 9 |
| Query Planner | 2 |

## 5. Root Causes

### A. Exact facts are being displaced by Semantic RAG

**Evidence:** most 1,600-case regressions changed from Structured / fast answer modes to `pipeline:semantic_rag_dynamic`.

**Effect:** the RAG evidence may be relevant but incomplete, so strict facts such as game genre, game availability, controls, staff role, or event rule are missed or categorized incorrectly.

**Fix:** enforce a priority order:

```text
Verified Structured / calculator result
  -> return directly after validation
Semantic RAG
  -> only if no verified Structured candidate is available,
     or the Structured source explicitly reports no data
```

### B. Global Deadline is observed, not enforced

**Evidence:** the 1,820.500-second `candidate_decisions` stage happened before the timeout response was generated.

**Effect:** a request can occupy the single local worker far beyond the 9-second product promise, which can make other users queue.

**Fix:** put hard, cancellable time limits around every potentially blocking stage, especially candidate scoring, reranking, and local-model calls. Stop the stage at the remaining budget rather than checking the clock afterwards. Return a safe clarification or the already validated Structured draft when time is nearly exhausted.

### C. Facts Composer is useful but must remain optional

**Evidence:** 126 successful Composer calls, 57 health-skipped Composer attempts, and several tail-latency failures during this run.

**Effect:** waiting for style rewriting can make an otherwise correct fact answer slow or unavailable.

**Fix:** do not call Composer for exact Fast / Structured answers. Use it only for long, multi-source RAG evidence and only when enough remaining budget exists. A deterministic Thai template should remain the fallback.

### D. Keyboard Guard is not yet connected to the website API

**Evidence:** the 500-case runner simulates the intended early guard; the current web endpoint still enters the chatbot flow directly.

**Effect:** real users can still send `g]jo` or `จออง` into routing today.

**Fix:** integrate the detector before Session Context Resolver / question understanding:

```text
Web request
  -> Keyboard Input Guard
     -> hard layout mismatch: request retype, no model call
     -> soft repeated-character signal: show a neutral retype suggestion,
        or continue only after the user confirms the text
  -> normal Flow
```

The safest first release is detection + retype only. Do not automatically mutate user text or silently translate keyboard-layout errors.

## 6. Recommended Fix Order

1. **P0: Enforce cancellable sub-stage deadlines.** Fix the blocking `candidate_decisions` path before any broader production load test.
2. **P0: Restore Structured / Fast precedence.** Prevent Semantic RAG from overriding verified exact records.
3. **P1: Integrate Keyboard Guard in Web API.** Hard-block only high-confidence layout mismatch; preserve raw input and log the decision.
4. **P1: Gate Facts Composer by answer type and remaining budget.** Exact fact answers bypass it; only RAG drafts may use it.
5. **P2: Add typo-aware retrieval aliases only after evaluation.** Normalize approved repeated-character candidates for retrieval as a *candidate*, but never silently change the original user text or use it for price/booking actions.
6. **P2: Re-run the same 1,600 + 500 suites after each P0/P1 change.** Target: return at least to the prior 99.94% 1,600 pass rate, P95 below 9 seconds, and no individual stage exceeding the request budget.

## 7. Honest Product Status After This Test

The deterministic FAQ foundation still performs strongly for normal inputs, and the local 4B model is usable for the intended assistant roles. However, the **current combined Flow is not ready to claim a strict 10-second production SLA** because the deadline cannot cancel blocking candidate scoring, and Semantic RAG currently causes measurable regressions in exact FAQ answers.

The correct next move is not to remove LLM or RAG. It is to keep them behind verified Structured facts, enforce bounded execution, and integrate the input guard before the expensive Flow.
