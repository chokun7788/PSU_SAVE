# Entity Reranker Experiment

- created_at: 2026-08-01T23:09:11
- model: None
- case_count: 20
- baseline_accuracy: 0.9
- reranker_accuracy: None
- baseline_avg_sec: 0.0654
- reranker_avg_sec: 0.0
- reranker_p95_sec: 0.0
- model_load_sec: 0.0

## Failures / Changes

### amb_call_of_gameplay
- question: `Call of เล่นยังไง`
- expected: ambiguous 
- baseline: ambiguous / Call of Duty: Modern Warfare III / correct=True / margin=0.0
- reranker: not_run /  / correct=False / margin=0.0

### amb_call_of_controls
- question: `Call of Duty ปุ่มทั้งหมดมีอะไรบ้าง`
- expected: ambiguous 
- baseline: ambiguous / Call of Duty: Modern Warfare III / correct=True / margin=0.0
- reranker: not_run /  / correct=False / margin=0.0

### exact_call_of_action
- question: `ปุ่มกระโดดใน Call of Duty กดอะไร`
- expected: exact Call of Duty: Modern Warfare III
- baseline: ambiguous / Call of Duty: Modern Warfare III / correct=False / margin=0.0
- reranker: not_run /  / correct=False / margin=0.0

### exact_warzone
- question: `Call of Duty Warzone ปุ่มอะไร`
- expected: exact Call of Duty: Warzone
- baseline: exact / Call of Duty: Warzone / correct=True / margin=0.26
- reranker: not_run /  / correct=False / margin=0.0

### exact_mw3
- question: `Modern Warfare III ปุ่มอะไร`
- expected: exact Call of Duty: Modern Warfare III
- baseline: unknown / Call of Duty: Modern Warfare III / correct=False / margin=1.0
- reranker: not_run /  / correct=False / margin=0.0

### amb_mario_controls
- question: `Mario ปุ่มอะไร`
- expected: ambiguous 
- baseline: ambiguous / Mario Kart 8 Deluxe / correct=True / margin=0.0
- reranker: not_run /  / correct=False / margin=0.0

### amb_mario_gameplay
- question: `Mario เล่นยังไง`
- expected: ambiguous 
- baseline: ambiguous / Mario Kart 8 Deluxe / correct=True / margin=0.0
- reranker: not_run /  / correct=False / margin=0.0

### exact_mario_kart
- question: `Mario Kart 8 Deluxe ปุ่มอะไร`
- expected: exact Mario Kart 8 Deluxe
- baseline: exact / Mario Kart 8 Deluxe / correct=True / margin=0.14
- reranker: not_run /  / correct=False / margin=0.0

### exact_mario_party
- question: `Mario Party Superstars เล่นยังไง`
- expected: exact Mario Party Superstars
- baseline: exact / Mario Party Superstars / correct=True / margin=0.14
- reranker: not_run /  / correct=False / margin=0.0

### exact_mario_odyssey
- question: `Super Mario Odyssey ปุ่มอะไร`
- expected: exact Super Mario Odyssey
- baseline: exact / Super Mario Odyssey / correct=True / margin=0.14
- reranker: not_run /  / correct=False / margin=0.0

### amb_resident_gameplay
- question: `Resident เล่นยังไง`
- expected: ambiguous 
- baseline: ambiguous / Resident Evil 4 / correct=True / margin=0.0
- reranker: not_run /  / correct=False / margin=0.0

### exact_re4
- question: `Resident Evil 4 ปุ่มอะไร`
- expected: exact Resident Evil 4
- baseline: exact / Resident Evil 4 / correct=True / margin=0.14
- reranker: not_run /  / correct=False / margin=0.0

### exact_revillage
- question: `Resident Evil Village เล่นยังไง`
- expected: exact Resident Evil Village
- baseline: exact / Resident Evil Village / correct=True / margin=0.14
- reranker: not_run /  / correct=False / margin=0.0

### amb_overcook_gameplay
- question: `Over cook เล่นยังไง`
- expected: ambiguous 
- baseline: ambiguous / Overcooked! / correct=True / margin=0.0
- reranker: not_run /  / correct=False / margin=0.0

### exact_overcooked2
- question: `Overcooked 2 มีปุ่มอะไรบ้าง`
- expected: exact Overcooked! 2
- baseline: exact / Overcooked! 2 / correct=True / margin=0.09
- reranker: not_run /  / correct=False / margin=0.0

### exact_gran_turismo
- question: `Gran Turismo 7 ปุ่ม`
- expected: exact Gran Turismo 7
- baseline: exact / Gran Turismo 7 / correct=True / margin=1.0
- reranker: not_run /  / correct=False / margin=0.0

### exact_gt7_thai_typo
- question: `แกรนทูริสโม่ 7 ปุ่ม`
- expected: exact Gran Turismo 7
- baseline: exact / Gran Turismo 7 / correct=True / margin=1.0
- reranker: not_run /  / correct=False / margin=0.0

### exact_tekken
- question: `เทคเคน 8 ปุ่มเตะขวากดอะไร`
- expected: exact TEKKEN 8
- baseline: exact / TEKKEN 8 / correct=True / margin=1.0
- reranker: not_run /  / correct=False / margin=0.0

### exact_valorant
- question: `วาโล ปุ่มอะไร`
- expected: exact VALORANT
- baseline: exact / VALORANT / correct=True / margin=1.0
- reranker: not_run /  / correct=False / margin=0.0

### exact_little_nightmares
- question: `ลิตเติลไนท์แม ปุ่มวิ่งกดอะไร`
- expected: exact Little Nightmares II
- baseline: exact / Little Nightmares II / correct=True / margin=1.0
- reranker: not_run /  / correct=False / margin=0.0
