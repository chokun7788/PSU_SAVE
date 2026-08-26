# Semantic Embedding Model Benchmark

- Generated: 2026-08-23T23:23:19+07:00
- Cases: 11

| Model | Quantization | Size MiB | Build sec | Top-1 | Top-3 | Avg query sec | P95 sec | Max sec |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| `bge-m3` | F16 | 603.2 | 13.0138 | 100.00% | 100.00% | 2.822 | 5.2742 | 5.2742 |
| `psu-bge-m3:q8_0` | Q8_0 | 333.2 | 21.5811 | 100.00% | 100.00% | 0.4594 | 0.4927 | 0.4927 |
| `psu-bge-m3:q4_k_m` | Q4_K_M | 204.7 | 11.409 | 100.00% | 100.00% | 0.5625 | 0.6172 | 0.6172 |

## Quantization Drift

- `psu-bge-m3:q8_0` เทียบ `bge-m3`: average same-document cosine=0.999327, minimum=0.998712, top-1 agreement=100.00%
- `psu-bge-m3:q4_k_m` เทียบ `bge-m3`: average same-document cosine=0.970213, minimum=0.957227, top-1 agreement=100.00%

หมายเหตุ: ชุดนี้วัด retrieval บนข้อมูลจริงที่มีในหมวด knowledge/events_news ยังไม่ใช่ human relevance benchmark ขนาดใหญ่
