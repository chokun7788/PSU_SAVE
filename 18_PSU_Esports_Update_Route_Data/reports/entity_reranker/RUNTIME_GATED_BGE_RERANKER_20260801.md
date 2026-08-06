# Runtime Gated BGE Entity Reranker - 2026-08-01

## What Changed

- Added optional gated entity reranker inside `app/pipeline/entity_resolver.py`.
- Selected one model for runtime experiments: `BAAI/bge-reranker-v2-m3`.
- Default runtime remains off:
  - `PSU_ENTITY_RERANKER=0`
- Enable with:
  - `PSU_ENTITY_RERANKER=1`
  - `PSU_ENTITY_RERANKER_CACHE_DIR=D:/AIModels/huggingface`
- Added CLI flags:
  - `tools/local_ai_chat.py --entity-reranker`
  - `start_local_ai_chat.ps1 -EntityReranker`
- Added eval runner flags:
  - `app/runtime/run_question_bank_eval.py --entity-reranker`

## Gated Policy

The reranker is allowed only after the resolver has generated game candidates.

It currently runs only for:

- `controls`
- `gameplay`
- `detail`

It skips:

- price questions
- booking questions
- family/list questions
- generic broad family questions such as `Mario เล่นยังไง`
- exact alias matches such as `Gran Turismo 7` and `Overcooked 2`
- high-confidence exact resolver matches

## Why Price And Booking Are Skipped

During the first 1,600-case eval, the reranker incorrectly treated `Nintendo Switch ราคาเท่าไหร่` as the game `Nintendo Switch Sports`.

That is a service/zone target, not a game target, so price/booking are not safe reranker domains yet.

## Eval Results

Baseline no reranker:

- Run dir: `data/eval/question_bank_runs/20260802_001347_no_llm_no_reranker_1500_20260801b`
- Total: 1,600 cases
- Total wall time: 1366.01 sec
- Average wall time: 0.8538 sec

Gated BGE reranker after gate fix:

- Run dir: `data/eval/question_bank_runs/20260802_005715_no_llm_gated_bge_reranker_1600_after_gate_fix_20260801`
- Total: 1,600 cases
- Total wall time: 1040.37 sec
- Average wall time: 0.6502 sec
- Mode diff vs baseline: 0
- Route diff vs baseline: 0
- Answer diff vs baseline: 0
- Validation diff vs baseline: 0
- Reranker trace actions:
  - skipped: 525
  - kept_ambiguous: 1
  - selected_exact: 0 in this 1,600-case set

Focused runtime check:

- `Modern Warfare III ปุ่มอะไร` can be promoted from resolver `unknown` to exact `Call of Duty: Modern Warfare III`.
- `Mario เล่นยังไง` still clarifies and does not force-select one Mario game.
- `Call of Duty ปุ่มทั้งหมดมีอะไรบ้าง` still clarifies.
- `Nintendo Switch ราคาเท่าไหร่` remains service fee, not game entity.
- `Overcooked 2 ราคาเท่าไหร่` remains structured service fee by game.
- `Overcooked 2 ปุ่มทั้งหมดมีอะไรบ้าง` remains structured game controls.

## Current Conclusion

The runtime integration is safe after the gate fix, but the current gate is intentionally conservative.

It should not be enabled globally as a replacement for the resolver. It is useful only as an optional rescue path for narrow entity cases such as partial titles that the resolver detects but marks below threshold.

Next improvement should be a better service-vs-game target classifier before allowing reranker to touch price/booking questions.
