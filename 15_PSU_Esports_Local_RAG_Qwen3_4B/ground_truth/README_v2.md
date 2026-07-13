# Ground Truth v2

- File: `ground_truth_v2_360.jsonl`
- Total: 360 cases
- Focus: typo, casual Thai, Thai/English mixed, synonyms, multi-intent questions, price/service fee, schedule edge cases, and no-answer safety.
- Evaluation note: this set is harder than `ground_truth_full.jsonl`; some cases intentionally test future improvements.

Run example:

```powershell
py -3 scripts\run_ground_truth_eval.py --ground-truth ground_truth\ground_truth_v2_360.jsonl --label v2 --limit 40
```
