# Canonical Content Repository

This directory is the human-readable source of truth for PSU Esports chatbot content. Each JSON record owns one stable `content_id`, its Thai source fields, exact facts, aliases, source evidence, and English review state.

## Categories

- `services`: prices and service conditions
- `resources`: equipment, zones, and service availability
- `games`: game profiles and supported zones
- `game_controls`: control maps grouped by game and platform
- `competition`: one record per competition document with nested sections
- `members`: people, roles, and approved name aliases
- `booking`: booking policies and reservation rules
- `schedule`: closures and operating status
- `rules`: studio, equipment, penalty, and contact policies
- `knowledge`: curated FAQ facts

## Language Contract

`locales.th.fields` is the Thai source. `locales.en` is an overlay tied to a SHA-256 hash of that source. English is usable only when its status is `approved`, the reviewer and approval timestamp are present, and its source hash still matches.

The generated `review/en_localization_drafts.jsonl` is a review queue. Local LLM output belongs there as a draft only; it must never be copied directly into a public chatbot release.

## Build

Run `python tools/build_canonical_content.py --check` to validate the migration inputs. Run `python tools/build_canonical_content.py` once in an empty `data/content` directory to build the repository.
## Runtime RAG rebuild

After a Canonical Content record is approved or changed, rebuild the runtime
artifacts from this one source of truth:

```powershell
python tools/rebuild_canonical_rag.py
```

This validates every record, writes the Thai source projection, writes only
approved English projection rows, and rebuilds both local lexical and BGE
semantic indexes. Machine English drafts remain in `review/` and are never
served to the chatbot.
