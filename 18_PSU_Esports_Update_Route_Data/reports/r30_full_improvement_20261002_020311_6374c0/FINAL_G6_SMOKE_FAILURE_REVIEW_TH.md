# Smoke ที่ไม่ผ่าน G6 — หลักฐานรายไฟล์

71/85 ไฟล์ผ่าน อีก 14 ไฟล์มี log ครบ แต่ไฟล์ที่หยุด assertion แรกไม่ได้แปลว่าคำถามถัดไปในไฟล์ถูกทั้งหมด

## smoke_test_answer_pipeline.py

```text
AssertionError: CS2 แข่งทีมละกี่คน: expected mode prefix pipeline:competition_fact_card, got pipeline:competition_source_rag
```

Expecting a historical mode prefix does not establish incorrect CS2 roster content; retain the old grade and compare source/content separately.

Full log: C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\r30_full_improvement_20261002_020311_6374c0\final_G6_smokes\smoke_test_answer_pipeline.log

## smoke_test_availability_policy_regressions.py

```text
AssertionError: ถ้าจะเล่น Call of Duty ต้องจองอะไร: category clarification != reservation
```

Family-title ambiguity is now clarification instead of guessing a reservation service.

Full log: C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\r30_full_improvement_20261002_020311_6374c0\final_G6_smokes\smoke_test_availability_policy_regressions.log

## smoke_test_bilingual_web_api.py

```text
urllib.error.HTTPError: HTTP Error 503: Service Unavailable
```

503 under concurrent requests while machine loaded. Idle final check recorded separately; no evidence here identifies WordPress as cause.

Full log: C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\r30_full_improvement_20261002_020311_6374c0\final_G6_smokes\smoke_test_bilingual_web_api.log

## smoke_test_bilingual_pipeline.py

```text
AssertionError
```

Baseline replay reproduces the failing file; exact content/control assumptions still require item-level source review. Do not label all assertions obsolete.

Full log: C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\r30_full_improvement_20261002_020311_6374c0\final_G6_smokes\smoke_test_bilingual_pipeline.log

## smoke_test_boundary_guard.py

```text
AssertionError: pipeline:freshness_live_source_required
```

Current freshness_live_source_required behavior differs from assertion. Requires source/freshness policy review, not a declaration that stale live status is valid.

Full log: C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\r30_full_improvement_20261002_020311_6374c0\final_G6_smokes\smoke_test_boundary_guard.log

## smoke_test_correctness_control_flow_v1.py

```text
AssertionError
```

Baseline replay reproduces the failing file; exact content/control assumptions still require item-level source review. Do not label all assertions obsolete.

Full log: C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\r30_full_improvement_20261002_020311_6374c0\final_G6_smokes\smoke_test_correctness_control_flow_v1.log

## smoke_test_english_draft_preview.py

```text
AssertionError: PipelineAnswer(answer='Selected Arena of Valor (RoV) competition rules from the recorded rulebook:\nTournament: Arena of Valor (RoV) / 2025\n\n\n**Competition format**\n•    1.1. Offline event on September 11, 2025 · Registration: 8:00–8:30 AM · Draw of brackets: 8:30–8:40 AM · Round … (full PipelineAnswer/trace retained in log)
```

Approved source-bound competition overview now returned; historical draft/mode assertion differs. Does not prove every translated clause correct.

Full log: C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\r30_full_improvement_20261002_020311_6374c0\final_G6_smokes\smoke_test_english_draft_preview.log

## smoke_test_english_format_parity_fixes.py

```text
AssertionError
```

Baseline replay reproduces the failing file; exact content/control assumptions still require item-level source review. Do not label all assertions obsolete.

Full log: C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\r30_full_improvement_20261002_020311_6374c0\final_G6_smokes\smoke_test_english_format_parity_fixes.log

## smoke_test_game_catalog.py

```text
AssertionError: surface variant should receive bounded Local LLM intent review
```

Expectation of bounded Local LLM review differs from deterministic catalog processing; examine actual source/answer independently.

Full log: C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\r30_full_improvement_20261002_020311_6374c0\final_G6_smokes\smoke_test_game_catalog.log

## smoke_test_genre_alias_formatting.py

```text
AssertionError: moba popular games formatting: missing ['MOBA', '• League of Legends', '• Dota 2', '• Mobile Legends: Bang Bang']
```

Expected genre/title/bullet content is absent. Could be alias/normalization or presentation mismatch; not confirmed purely formatting.

Full log: C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\r30_full_improvement_20261002_020311_6374c0\final_G6_smokes\smoke_test_genre_alias_formatting.log

## smoke_test_llm_health_circuit_breaker.py

```text
AssertionError
```

Baseline replay reproduces the failing file; exact content/control assumptions still require item-level source review. Do not label all assertions obsolete.

Full log: C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\r30_full_improvement_20261002_020311_6374c0\final_G6_smokes\smoke_test_llm_health_circuit_breaker.log

## smoke_test_pipeline_fixes_20260823.py

```text
AssertionError: []
```

Baseline replay reproduces the failing file; exact content/control assumptions still require item-level source review. Do not label all assertions obsolete.

Full log: C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\r30_full_improvement_20261002_020311_6374c0\final_G6_smokes\smoke_test_pipeline_fixes_20260823.log

## smoke_test_real_usage_golden.py

```text
AssertionError: REAL USAGE GOLDEN FAILURES:
```

Baseline replay reproduces the failing file; exact content/control assumptions still require item-level source review. Do not label all assertions obsolete.

Full log: C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\r30_full_improvement_20261002_020311_6374c0\final_G6_smokes\smoke_test_real_usage_golden.log

## smoke_test_update.py

```text
AssertionError: เด็กจุฬา เล่น PC กี่บาท: expected 'มหาลัยอื่น' in 'ราคา PC 1 ชั่วโมง (1 คน) สำหรับ ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student)\n•    25 บาท\nหมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27\nแหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png'
```

Exact Thai phrase มหาลัยอื่น differs from full group label นักศึกษา-นักเรียนต่างสถาบัน; retained 25-baht PC source and grade. Verify group/amount/source rather than phrase only.

Full log: C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\r30_full_improvement_20261002_020311_6374c0\final_G6_smokes\smoke_test_update.log

