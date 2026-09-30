# Thai multi-error sentence recovery, r15 (29 September 2026)

## User report and baseline

The correct `นายเป็นใครแล้วทำอะไรได้บ้าง` routed to `chatbot_identity`. The reported multi-error form `นานเปนไคแเสทำอะไรไดเทั่ง` instead returned a clarification. The prior keyboard-neighbor and character-order stages each handled a narrow single-word error; neither established the intent of both damaged clauses together.

## Implementation

- `chatbot_identity.py`: compare the whole short sentence **and both clauses** against chatbot identity/capability request forms. Require a recognizable chatbot subject and action; reject named people, resources, fees, booking slots, competition topics, and other targets. A short single-clause identity question can also survive multiple edits when its subject and “who” ending remain recognizable.
- `typo_similarity.py`: a deterministic edit distance that counts adjacent character transpositions as one edit. No external model is trained on customer chat.
- `chatbot_identity.py` and `social_dialogue.py`: bounded two-error recovery for standalone greetings and social replies. Social candidates require the same opening character and a clear winning intent; a greeting cannot consume a following task.
- `multi_error_phrase_recovery.py`: whole-phrase candidates for common price, opening/closing time, game list, equipment, and contact requests. Use edit distance plus sentence context and reject close competing meanings. Resource names and duration literals are preserved, including `VR 30 นาที`.
- `router.py`: a semantic prototype alone cannot force `chatbot_identity` when the safer chatbot-identity detector rejects the target. This prevents resource and staff questions from being answered as if they asked about the bot.

The original message remains available as `raw_query`; the accepted corrected phrase is used for routing. Only bounded, high-confidence patterns are corrected. Uncertain text still receives clarification.

## Ground-truth procedure and results

`tools/generate_thai_multi_error_eval_20260929.py` adds a second deterministic character error to each of the **49 already labeled Thai noisy-input questions**, then adds six separately specified multi-error identity questions. The generator writes a new fixture and does not change the source fixture. It also generated a separate **25-question holdout** from the prior holdout source, without the six manually specified identity examples. These are synthetic text errors with inherited expected intents, not human-verified live conversation outcomes.

| Evaluation | Initial | Final |
| --- | ---: | ---: |
| 55 multi-error questions | 37/55 | **55/55** expected intents |
| 25 multi-error holdout questions | 18/25 | **25/25** expected intents |
| Original 49 noisy questions | 49/49 before | **49/49** after |
| Original 25 holdout questions | 25/25 before | **25/25** after |
| Related unit and regression tests | — | **55 + 51 passed** |

Each evaluation also preserved all case-level protected literals. The final machine-readable results are `reports/thai_multi_error_eval_20260929_r15_verified55.jsonl`, `reports/thai_multi_error_eval_20260929_r15_verified_holdout25.jsonl`, `reports/thai_noisy_input_eval_20260929_r15_regression49.jsonl`, and `reports/thai_noisy_input_eval_20260929_r15_regression_holdout25.jsonl`, each with a `.summary.json`. Earlier reports and logs remain in place.

A read-only scan of 10,000 bilingual ground-truth questions found **zero rewrites** by the new phrase stage. The chatbot-identity detector matched **zero questions outside the chatbot identity source contract** after correcting earlier false positives involving `คุณสมบัติ`, `รายชื่อผู้เล่น`, and `ผู้ช่วยอธิการบดี`. This scan checks these specific risks; it is not a 10,000-answer correctness result.

## Live package check

The separate owner package is `owner_local_delivery_20260929_multi_error_r15/PSU_Esports_Chatbot_Local`, running at `http://127.0.0.1:8095/`. `/health` reported `2026.09.29-multi-error-recovery-r15` and a ready worker. Real `/api/chat` requests gave:

| Question | Route | Observed latency |
| --- | --- | ---: |
| `นานเปนไคแเสทำอะไรไดเทั่ง` | `chatbot_identity` | 1.49 s |
| `นานเปนไคแเสทำอะไรไดเทั่งครับ` | `chatbot_identity` | 2.56 s |
| `มีเกมแข่งนดมั้ยย` | game list / racing catalog | 2.30 s |
| `VR 30 นาที คิดตัวเท่าไหรอ่า` | verified service fee | 0.95 s |
| `ปิดกี่โมง` | schedule | 0.33 s |
| `PC1 เป็นอะไรแล้วทำอะไรได้บ้าง` | clarification, not chatbot identity | 8.45 s |

## Remaining limits

- Passing synthetic perturbations proves behavior on those generated examples. It does not establish a general Thai spell-correction accuracy rate for arbitrary customer messages, mobile keyboards, names, or long multi-topic requests.
- The game, fee, schedule, equipment, and contact answers still depend on their existing verified data paths. The intent tests do not certify a live booking slot's free/occupied value or owner policy.
- A false correction could still occur on a novel real-world word. The runtime abstains on close candidates; a future, separately reviewed real typo sample set would allow measurement before widening coverage.
