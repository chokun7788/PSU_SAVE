# Runtime Input Quality Guard

**Latest update:** 2026-08-31  
**Status:** Implemented in Web API. Default is `shadow`; enable `enforce` only after reviewing live logs.

## Problem Found

The earlier 500-case detector run was a prototype: it could score keyboard-layout mismatch and repeated characters, but the Web API did not call it before `Session Context Resolver` and the chatbot pipeline.

This allowed inputs such as these to reach routing:

```text
g]jo                    -> user intended Thai but keyboard was English
จอองแล้วแก้ไขได้ไหม     -> duplicate character hides the booking term
VALORANT เล่นได้ที่เครรื่องไหน -> duplicate character hides an intent term
```

The 500-case model-flow run confirmed the impact. Repeated-character cases that entered the pipeline had lower source-contract pass rates than normal input, because route selection could no longer recognize the intended term reliably.

## Root Cause

The standalone detector was initially fitted with the evaluation question corpus. Runtime cannot depend on that test corpus, so the integrated guard was changed to learn only from published chatbot knowledge.

That revealed two defects:

1. **Threshold transfer failure:** the old repeat threshold (`0.718849`) was too high for the published-content corpus. `จออง` scored about `0.56`, so it was missed.
2. **Thai boundary false positives:** Thai words often touch without spaces. The old scorer awarded an internal-repeat bonus even when deleting the character made the text worse, which could incorrectly flag normal text such as `ระบบ` or `กรรมการ`.

## Implemented Solution

```text
Web API request
  -> Runtime Input Quality Guard
     -> keyboard layout mismatch
        -> request retype, stop before session / router / RAG / LLM
     -> high-confidence repeated character
        -> request retype, stop before session / router / RAG / LLM
     -> no signal or shadow mode
        -> original input proceeds unchanged
```

### 1. Published-data runtime corpus

`app/core/runtime_input_quality_guard.py` builds a character-profile corpus from published FAQ knowledge only:

- game titles, aliases, game details and controls
- service/game availability and equipment labels
- member names and roles
- rules, reservation patterns and fact cards

It does not load the 500-case typo test set at runtime and does not silently replace a user's question with a guessed correction.

### 2. Evidence-based duplicate scoring

The repeated-character scorer now adds its inside-Thai-span confidence bonus only when deleting the repeated character improves the linguistic form or creates corpus evidence.

```text
Old behavior:
  internal duplicate -> bonus, even if deleting it made the phrase worse

New behavior:
  internal duplicate + deletion improves form -> bonus
  internal duplicate + deletion worsens form -> no bonus
```

This is a general signal, not a hand-made alias list for each typo.

### 3. Runtime thresholds

The runtime profile was re-evaluated against the 500-case dataset. Selected values:

| Signal | Runtime threshold | Product policy |
|---|---:|---|
| Keyboard-layout mismatch | `0.39` | Ask user to retype and stop pipeline in enforce mode |
| Repeated-character typo | `0.55` | Ask user to retype and stop pipeline in enforce mode |

At these thresholds on the 400-case test split:

| Metric | Keyboard layout | Repeated character |
|---|---:|---:|
| Precision | 100.00% | 99.29% |
| Recall | 100.00% | 87.50% |
| F1 | 100.00% | 93.02% |

The one repeat false positive occurred inside an input already detected as keyboard-layout mismatch, so the visible product action is still the same safe retype request. Some low-confidence duplicate errors are intentionally allowed through; this is safer than blocking ordinary Thai words incorrectly.

## Runtime Policy

The guard supports two modes:

| Environment setting | Behavior |
|---|---|
| `PSU_INPUT_QUALITY_GUARD_MODE=shadow` | Detect and log; do not alter the chatbot response. This is the default. |
| `PSU_INPUT_QUALITY_GUARD_MODE=enforce` | Stop high-confidence layout/repeat input before expensive chatbot stages and ask the user to type again. |

Other controls:

```text
PSU_INPUT_QUALITY_GUARD_ENABLED=true
PSU_INPUT_QUALITY_LAYOUT_THRESHOLD=0.39
PSU_INPUT_QUALITY_REPEAT_THRESHOLD=0.55
PSU_INPUT_QUALITY_REPEAT_POLICY=ask_retype
```

`PSU_INPUT_QUALITY_REPEAT_POLICY=warn_and_continue` is available for a softer rollout, but it does not prevent a typo from reaching the answer router. For accuracy-first FAQ usage, `ask_retype` is the recommended enforce policy.

## API Result

When enforce mode detects a problem, it returns a normal JSON response without invoking the chatbot pipeline:

```json
{
  "ok": true,
  "mode": "input_guard_layout_retype",
  "route_category": "input_guard",
  "answer": "เหมือนข้อความอาจพิมพ์โดยใช้ภาษาแป้นพิมพ์ไม่ตรงกัน ...",
  "input_quality": {
    "action": "request_retype",
    "should_retype": true,
    "flags": ["keyboard_layout_mismatch"]
  }
}
```

The API intentionally does not send a translated or deleted-character candidate to the chatbot. The original text is preserved in the normal chat log; the guard log stores only action, scores and detector reason.

## Verification

Completed:

```text
tests/smoke_test_keyboard_input_anomaly.py
tests/smoke_test_runtime_input_quality_guard.py
tools/run_runtime_input_quality_guard_eval.py
```

API smoke test with `PSU_INPUT_QUALITY_GUARD_MODE=enforce`:

| Input | Returned mode | Model called? |
|---|---|---|
| `g]jo` | `input_guard_layout_retype` | No |
| `จอองแล้วแก้ไขได้ไหม` | `input_guard_repeat_retype` | No |

Artifacts:

- `reports/keyboard_input_anomaly_eval/20260831_runtime_guard_final/summary.json`
- `reports/keyboard_input_anomaly_eval/20260831_runtime_guard_final/results.jsonl`
- `reports/keyboard_input_anomaly_eval/20260831_runtime_guard_final/api_smoke2.stdout.log`

## Remaining Limits

- This covers Thai Kedmanee and English keyboard mismatch. It does not cover Pattachote, mobile swipe, voice transcription, missing characters, swapped characters, or Romanized Thai.
- The 500-case suite is synthetic and has been inspected during development. It is regression evidence, not a final real-user accuracy claim.
- Start in `shadow` mode and label anonymized near-threshold real inputs before making enforce the production default.
