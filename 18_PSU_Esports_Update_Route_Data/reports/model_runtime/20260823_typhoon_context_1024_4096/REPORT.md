# Ollama Context Benchmark

- Generated: 2026-08-23T23:40:20+07:00
- Model: `scb10x/typhoon2.5-qwen3-4b`
- Contexts: 1024, 2048, 3072, 4096
- Repeats per workload: 2

| num_ctx | Warm avg sec | P95 sec | Max sec | tok/s | Ollama size MiB | VRAM size MiB |
|---:|---:|---:|---:|---:|---:|---:|
| 1024 | 1.4507 | 1.8385 | 1.8385 | 54.44 | 2595.9 | 2595.9 |
| 2048 | 1.4974 | 1.9385 | 1.9385 | 54.04 | 2740.9 | 2740.9 |
| 3072 | 1.4857 | 1.8503 | 1.8503 | 54.16 | 2885.9 | 2885.9 |
| 4096 | 1.4551 | 1.8348 | 1.8348 | 54.6 | 3030.9 | 3030.9 |

หมายเหตุ: context length คือเพดาน token ต่อ request และมีผลต่อ KV cache; ไม่ได้หมายความว่า prompt ทุกข้อใช้ token เต็มเพดาน
