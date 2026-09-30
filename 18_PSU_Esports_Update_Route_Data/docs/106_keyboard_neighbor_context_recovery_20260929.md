# Thai keyboard-neighbor recovery, r13 (29 September 2026)

## Scope and evidence

This release adds a small, deterministic candidate stage before intent routing. It checks whether one Thai character in a likely intent word came from an adjacent **unshifted Kedmanee** key. The candidate is used only when a narrow sentence pattern agrees and exactly one candidate survives. The original customer message remains available as `raw_query`; resource IDs, times, and game titles are not edited by this stage.

The approach is inspired by [Thai chatbot keyboard-error research](https://digital.car.chula.ac.th/chulaetd/65753/) and by [context-aware spelling correction](https://aclanthology.org/2020.emnlp-demos.21/). It is an implementation choice for this project, not a reproduction of either paper's model or reported performance. [Thai misspelling semantics research](https://aclanthology.org/2022.lrec-1.24/) is a reason to avoid indiscriminate normalization: a misspelled form can carry meaning or be a valid word.

## Flow implemented

1. Keep the original message.
2. For the supported intent words `สวัสดี`, `จอง`, `ว่าง`, and `เกม`, locate a single-character substitution on neighboring Kedmanee keys. Reject other edit types, multiple candidate words, and messages longer than 120 characters.
3. Check the surrounding phrase: a standalone greeting, a booking how-to phrase, an availability question naming a resource, or a game-list phrase.
4. Do not rewrite a known valid observed word. `จอย` is protected because “ใช้จอยยังไง” asks about controls.
5. Route the accepted candidate through the existing answer pipeline. If no candidate is accepted, use the original input.

Examples verified in the pipeline: `สวัาดี` → greeting; `จแงยังไง` → booking instructions; `มีเดมอะไรบ้าง` → 42-game catalog. `PC1 ส่างไหม` becomes a live booking-status question; the free/occupied value still depends on the live data source. `วันนี้ 10:00 PC1 ส่างไหม` preserves the resource and time.

## Evaluation

| Check | Result |
| --- | --- |
| New focused tests | 4/4 passed |
| Existing related regression tests | 59/59 passed |
| Thai noisy-input pairs, expected intent and protected literals | 49/49 passed |
| Separate holdout | 25/25 passed |
| Scan of 10,000 bilingual ground-truth questions | 0 remaining rewrites after real-word guard |

The first scan exposed a real false positive: 38 game-control questions containing `ใช้จอยยังไง` would have become `ใช้จองยังไง`. The valid-word guard was added, and the full scan then had zero rewrites. The 10,000-question scan checks **which questions the new stage would change**; it is not a 10,000-answer accuracy score. The 49 and 25 noisy-input runs have manually specified intent expectations but do not certify the actual free/occupied state of a live booking slot.

Machine-readable results: `reports/thai_noisy_input_eval_20260929_keyboard_neighbor_r13_49.jsonl` and `reports/thai_noisy_input_eval_20260929_keyboard_neighbor_r13_holdout25.jsonl`, each with a `.summary.json` file. Existing reports and logs were retained.

The separate r13 owner package was built at `owner_local_delivery_20260929_keyboard_neighbor_r13/PSU_Esports_Chatbot_Local` and started on `http://127.0.0.1:8095/`. `/health` reported version `2026.09.29-keyboard-neighbor-r13`, successful warmup, and a ready pipeline worker. Real `/api/chat` requests returned booking instructions for `จแงยังไง`, the game catalog for `มีเดมอะไรบ้าง`, a greeting for `สวัาดี`, and game controls for the protected `Beat Saber ใช้จอยยังไง`.

The live request `PC1 ส่างไหม` reached `live_booking_status` in 0.11 seconds, but the answer was `live_booking_status_unavailable`: it did **not** confirm whether PC1 is free or occupied. This is a live data availability issue separate from typo detection. The health endpoint reports the live-booking feature enabled, which does not by itself prove that the requested slot can be answered.

## Limits and next evidence needed

- This covers one adjacent-key **substitution** in four short intent words. Missing characters, doubled characters, shifted keys, Pattachote keyboards, mobile layouts, and arbitrary Thai vocabulary need separate handling and test data. Existing recovery stages may cover some of those errors.
- Context rules are intentionally narrow. A typo outside the accepted sentence patterns may remain unresolved rather than be silently changed.
- The 10,000-question suite contains few of the exact new mistakes; the new positive cases are separately asserted in focused tests. Collecting opt-in, anonymized real examples would support a wider candidate model and a meaningful false-positive estimate. No such owner-confirmed live corpus was assumed here.
