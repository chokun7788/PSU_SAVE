# English localization registry

`approved_localizations.jsonl` is the production English overlay. Each row is
keyed by `content_id + field + locale` and is usable only when:

- `status` is `approved`;
- `approved_by` and `approved_at` are present; and
- `source_text_sha256` still matches the current Thai source field.

Draft generation and approval are offline publishing operations. Runtime code
must never translate missing text or silently use a stale row.

## Review and publish workflow

Machine-generated drafts are not production content. An authorized PSU reviewer
must compare a draft with the Thai source, then create a candidate using only
explicit `content_id:field` selectors:

```powershell
py tools/manage_english_localizations.py review-queue data/locales/en/localization_review_drafts_machine_20260909_verified.jsonl --category reservation --output reports/bilingual_english/reservation_review.md
py tools/manage_english_localizations.py approve data/locales/en/localization_review_drafts_machine_20260909_verified.jsonl --output data/locales/en/reviewed_candidate.jsonl --reviewer <reviewer-id> --select curated_booking_no_edit:text
py tools/manage_english_localizations.py validate data/locales/en/reviewed_candidate.jsonl
py tools/manage_english_localizations.py publish data/locales/en/reviewed_candidate.jsonl --build-vector
```

`approve` cannot select every draft implicitly. `publish` validates source hashes,
writes a complete staged release, and switches `CURRENT` only after the release
has been created. If a Thai source changes, its English overlay becomes stale
and runtime code will not use it.
