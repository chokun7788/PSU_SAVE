# Benchmark Markdown Export

สร้างเมื่อ: `2026-08-23T16:16:54+07:00`

- Evaluation cases: `1600`
- Run modes: `2` (no_llm, llm_scb10x_typhoon2.5-qwen3-4b)
- Detail Markdown: `3200` ไฟล์
- Paired Markdown: `1600` ไฟล์
- Case Markdown รวม: `4800` ไฟล์
- Case bank SHA256: `C6BCB5AEF610705F70E0BC762CF6D761313897B39FDFEDD3A165A70EE1D92B76`

## ทางเข้าหลัก

- [Index ทุกโจทย์และทุกโหมด](INDEX.md)
- `paired/`: หนึ่งไฟล์ต่อโจทย์ มีคำตอบทุกโหมดในหน้าเดียว
- `details/<run>/`: หนึ่งไฟล์ต่อโจทย์ต่อโหมด มี raw record และ trace ทุก entry ที่ benchmark output เก็บไว้
- ข้อจำกัด: pipeline output ปัจจุบันจำกัด trace ไว้สูงสุด 12 entries ต่อเคส จึงไม่ใช่ event ledger ครบทุก process ภายใน request
- [Manifest JSON](MANIFEST.json)

## สรุปแต่ละโหมด

| Run | Total | Passed | Pass rate | Avg s | P95 s | Max s | LLM calls |
|---|---:|---:|---:|---:|---:|---:|---:|
| [no_llm](details/no_llm/INDEX.md) | 1600 | 1378 | 86.12% | 0.5235 | 1.2627 | 9.3943 | 0 |
| [llm_scb10x_typhoon2.5-qwen3-4b](details/llm_scb10x_typhoon2.5-qwen3-4b/INDEX.md) | 1600 | 1540 | 96.25% | 1.4635 | 4.1762 | 20.4899 | 278 |
