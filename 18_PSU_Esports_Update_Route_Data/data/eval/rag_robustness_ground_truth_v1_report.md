# RAG Robustness Ground Truth v1

ชุดทดสอบนี้วัด routing, target handling, source requirement และ safe outcome ก่อนวัดสำนวนคำตอบ เพื่อรองรับคำถามใหม่ คำถามกำกวม ภาษาพูด และภาษาไทย/อังกฤษที่ไม่เป็นทางการ.

- Total: 600
- Thai: 300
- English: 300
- Critical safety cases: 280

## Expected Outcome

- `answer_available`: 400
- `clarification_required`: 96
- `live_lookup_required`: 56
- `no_answer_expected`: 48

## Coverage by Group

| Group | Cases |
| --- | ---: |
| booking | 56 |
| clarification | 64 |
| competition | 80 |
| contact | 16 |
| equipment | 56 |
| games | 96 |
| general | 8 |
| input_quality | 24 |
| live_availability | 32 |
| live_schedule | 24 |
| members | 16 |
| out_of_scope | 16 |
| overview | 16 |
| rules | 16 |
| schedule | 32 |
| service_fee | 48 |

## Adversarial Coverage

- `agent`: 8
- `ambiguous_reference`: 32
- `ambiguous_time`: 8
- `broad`: 8
- `calculation`: 8
- `catalog`: 8
- `comparison`: 8
- `competition`: 96
- `compound`: 16
- `detail`: 8
- `format`: 16
- `future_time`: 8
- `game_to_zone`: 8
- `greeting`: 8
- `group_booking`: 8
- `holiday`: 8
- `how_to`: 8
- `identity`: 8
- `keyboard_layout`: 16
- `live`: 56
- `machine`: 8
- `maintenance`: 24
- `map_veto`: 8
- `missing_event`: 8
- `missing_game_event`: 8
- `mixed_known_unknown`: 8
- `mixed_language`: 16
- `needs_date`: 8
- `nonsense`: 8
- `out_of_scope`: 16
- `overtime`: 8
- `pause`: 8
- `payment`: 8
- `penalty`: 8
- `policy`: 8
- `policy_edge`: 8
- `price`: 8
- `relative_date`: 8
- `role_lookup`: 8
- `safety`: 8
- `semantic`: 8
- `short`: 16
- `skin`: 8
- `slang`: 8
- `stage`: 8
- `team_size`: 8
- `time_range`: 8
- `typo`: 16
- `underspecified`: 8
- `unknown_entity`: 16
- `unsupported_detail`: 16

## Evaluation Rules

- `answer_available`: route ต้องถูก และคำตอบต้องไม่เป็น no-answer/clarification โดยไม่มีเหตุผล.
- `live_lookup_required`: ต้องไปเส้นทางข้อมูลสด; ห้ามใช้คำตอบ snapshot เก่าเป็น Ground Truth.
- `clarification_required`: ต้องขอข้อมูลที่ขาด เช่น เกม รายการแข่ง เวลา หรือ object อ้างอิง.
- `no_answer_expected`: ต้องไม่แต่งข้อเท็จจริงหรือแสดง catalog ทั้งหมดเพื่อตอบ unknown entity.
- ใช้ชุดนี้เป็น gold candidate ก่อนใช้นับคะแนน release: ข้อที่เป็น policy/time-sensitive ต้อง owner review ก่อน promote เป็น strict gold.
