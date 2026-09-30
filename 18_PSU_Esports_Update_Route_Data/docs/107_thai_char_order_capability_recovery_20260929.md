# Thai character-order recovery for capability questions, r14

## Reported failure

On the running r13 package, `สามารถถามอะไรดไ้บ้าง` returned the generic clarification “ขอรายละเอียดเพิ่มนิดนึงครับ...”, while the correctly ordered `สามารถถามอะไรได้บ้าง` returned the chatbot capability answer. The typo swaps the adjacent code points `ไ` and `ด` in `ได้`; it is not an adjacent-key substitution, so r13's keyboard-neighbor stage did not apply.

## Change

Added `app/core/thai_transposition_recovery.py` before routing. It generates a candidate only for one adjacent character-order swap in `ได้`, inside a short chatbot capability question such as `ถามอะไร...บ้าง`, `ทำอะไร...บ้าง`, `ช่วยอะไร...บ้าง`, or `ตอบอะไร...บ้าง`. It rejects domain targets and people such as PC1, PS5, games, the studio, and the manager. It retains the original message as `raw_query`. This is a narrow repair of a verified failure, not a general Thai spell checker.

## Verification

| Check | Result |
| --- | --- |
| Focused and related unit tests | 50/50 passed |
| Previously established noisy-input set | 49/49 correct intents and protected literals |
| Separate holdout | 25/25 correct intents and protected literals |
| Scan of 10,000 bilingual ground-truth questions | 0 questions rewritten by the new stage |
| Running r14 `/api/chat`: `สามารถถามอะไรดไ้บ้าง` | `chatbot_identity`; capability answer, 1.40 s |
| Running r14 `/api/chat`: `ผู้จัดการทำอะไรดไ้บ้าง` | `members_lookup`; manager answer retained |

The 10,000-question scan checks for unintended rewrites; it is not a 10,000-answer accuracy score. The two noisy-input suites assert expected intents, not live booking occupancy.

The owner package is `owner_local_delivery_20260929_thai_char_order_r14/PSU_Esports_Chatbot_Local`. It is running at `http://127.0.0.1:8095/`. `/health` reported `2026.09.29-thai-char-order-r14` with a ready worker. The r13 package and its logs were retained. New evaluation results were saved under `reports/thai_noisy_input_eval_20260929_char_order_r14_49.jsonl` and `reports/thai_noisy_input_eval_20260929_char_order_r14_holdout25.jsonl` with corresponding summaries.

## Limit

The new stage only handles this high-confidence character-order pattern in capability questions. Other transpositions and mobile-keyboard typos need their own labeled examples and false-positive checks before widening the rule.
