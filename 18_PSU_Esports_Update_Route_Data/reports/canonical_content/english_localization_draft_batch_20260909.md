# English Localization Draft Batch - 2026-09-09

## Result

- Source registry records: `615`
- Completed English drafts: `615`
- Schema and source-hash validation errors: `0`
- Empty English fields: `0`
- Thai-script leakage: `0`
- Placeholder outputs: `0`
- Changed number tokens: `0`
- Changed URL tokens: `0`

## Files

- Source review registry: `data/locales/en/localization_review_drafts.jsonl`
- Completed draft batch: `data/locales/en/localization_review_drafts_machine_20260909_verified.jsonl`
- Generation event log: `reports/canonical_content/english_draft_generation_20260909.jsonl`

## Runtime Policy

The draft batch is not published to the production English registry.

For local-only testing, set both environment variables before starting the web server:

```text
PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW=1
PSU_ENGLISH_LOCALIZATION_DRAFT_PREVIEW_PATH=data/locales/en/localization_review_drafts_machine_20260909_verified.jsonl
```

Draft Preview never activates by default. It is disabled without the explicit flag and path.

## Preview Verification

| Question | Result |
| --- | --- |
| `How do I play VALORANT?` | English game detail rendered from the draft overlay. |
| `What equipment is available in VR Zone?` | English equipment catalog rendered. |
| `What are the CS2 competition rules?` | Routed to `competition_rules`, not game detail. |
| `Who are the studio members?` | Deliberately remains unavailable until human approval. |

## Mandatory Human Review

Member name, role, and affiliation fields are excluded from Draft Preview. The local model produced at least one unsafe institution-name substitution during verification. Names and affiliations require official Romanization or direct reviewer correction before they may be approved.

The same review policy applies before any draft can be published to `approved_localizations.jsonl`. To publish a reviewed candidate, use `tools/manage_english_localizations.py publish` only after every approved row has a reviewer identifier and timestamp.
