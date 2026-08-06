# Cross-Domain Target Gate + Game Reranker - 2026-08-02

## Why This Was Added

The first runtime reranker was too narrow because it only reranked game candidates.

That protected safety, but it also meant the system could not safely use reranking in cases where terms overlap across domains:

- `Nintendo Switch` can be a service/zone.
- `Nintendo Switch Sports` is a game.
- `Nintendo Switch OLED` is equipment.

If the reranker only sees game candidates, it may incorrectly force a service question into a game target.

## Current Design

New flow:

```text
query
-> rule/intent/operation hint
-> cross-domain target candidates
   - service_fee targets
   - game targets
   - equipment targets
-> rule-first target scoring
-> optional target reranker only if PSU_TARGET_RERANKER=1
-> allow game reranker only if target is exact games
-> otherwise skip/clarify/use normal structured path
```

## Files Changed

- Added `app/pipeline/target_resolver.py`
- Updated `app/pipeline/entity_resolver.py`
- Added `tests/smoke_test_target_resolver.py`
- Updated `tests/smoke_test_entity_reranker_gate.py`

## Important Policy

`PSU_ENTITY_RERANKER=1` enables the game reranker path.

`PSU_TARGET_RERANKER=1` is separate and remains off by default.

Reason: target reranking with BGE can be expensive, and the heuristic cross-domain target gate is enough for the current safety problem.

## Focused Behavior

- `Nintendo Switch ราคาเท่าไหร่`
  - target = `service_fee`
  - game reranker skipped
  - final answer remains service fee

- `Nintendo Switch Sports ปุ่มอะไร`
  - target = `games`
  - exact game alias protected
  - final answer remains game controls

- `Modern Warfare III ราคาเท่าไหร่`
  - target = `games`
  - allowed to use game reranker
  - final answer maps game to PlayStation 5 service fee

- `Call of Duty ราคาเท่าไหร่`
  - target = ambiguous games
  - game reranker skipped
  - final answer clarifies which Call of Duty game

- `Mario เล่นยังไง`
  - generic family query
  - game reranker skipped
  - final answer clarifies which Mario game

## Eval Result

Baseline no reranker:

- Run dir: `data/eval/question_bank_runs/20260802_001347_no_llm_no_reranker_1500_20260801b`
- Total: 1,600 cases
- Total wall time: 1366.01 sec
- Average wall time: 0.8538 sec

Cross-domain target gate + gated BGE game reranker:

- Run dir: `data/eval/question_bank_runs/20260802_161507_no_llm_cross_domain_target_gate_bge_game_reranker_1600_20260802`
- Total: 1,600 cases
- Total wall time: 1227.201 sec
- Average wall time: 0.767 sec
- Mode diff vs baseline: 0
- Route diff vs baseline: 0
- Answer diff vs baseline: 0
- Validation diff vs baseline: 0

Reranker/gate actions:

- `cross_domain_target_not_game`: 229
- `operation_not_supported`: 264
- `cross_domain_target_unknown`: 18
- `no_candidates`: 11
- `generic_family_query`: 3
- `kept_ambiguous`: 1

The important result is that 229 service targets were blocked from entering the game reranker, with no answer regressions in the 1,600-case eval.

## Current Conclusion

This is better than the previous game-only gated reranker because it no longer relies on a hard block like "price cannot rerank".

Instead, it asks:

```text
Is the target actually a game?
```

If yes, game reranker may run.

If no, the structured service/equipment path continues normally.

The next step is to extend the same target candidate idea into capability selection, so tool/capability candidates can also be reranked safely after rule-first scoring.
