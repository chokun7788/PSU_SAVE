# Per-Case Audit Log: 162 Flagged Cases

วันที่วิเคราะห์: 2026-08-23

## ขอบเขต

ตรวจ 162 เคสไม่ซ้ำกันจาก union ของ 54 heuristic failures, 44 เคสเกิน 10 วินาที และ 85 เคสที่ output lint พบความเสี่ยงด้านภาษา/รูปแบบ หลายเคสมีมากกว่าหนึ่งอาการ

คำตอบในช่อง `ตัวอย่างคำตอบที่ควรได้` เป็น counterfactual example สำหรับออกแบบ behavior และ regression contract ไม่ใช่การแก้ expected result ให้ผ่านโดยอัตโนมัติ

## เทคนิคที่ใช้ตรวจ

1. Expected Contract Check: อ่าน expected category, required/forbidden terms, risk และ LLM requirement จาก case bank
2. Actual Output Review: อ่านคำตอบจริง ไม่สรุปจาก pass/fail label อย่างเดียว
3. Route/Intent/Mode Trace: หา process แรกที่เปลี่ยน domain, operation หรือ target ผิด
4. No-LLM Counterfactual: เทียบ case ID เดียวกันเพื่อดูว่า LLM ช่วยหรือทำ route ถอยหลัง
5. Source Grounding Audit: ตรวจว่า PSU/current fact มี source ตรง category, game และ target หรือไม่
6. Latency Decomposition: เทียบ wall time, visible LLM time, timing stages และ overhead signature
7. Answer Shape Lint: ตรวจจำนวนข้อ/ประโยค ความยาว คำลงท้าย emoji ความซ้ำและการตัดกลางประโยค
8. Subanswer Coverage: สำหรับ compound ตรวจว่าตอบครบทุก operation ไม่ใช่แค่มี keyword ใด keyword หนึ่ง

## สรุปสถานะ

| สถานะ | จำนวน |
|---|---:|
| `passed_but_quality_risk` | 66 |
| `confirmed_sla_failure` | 41 |
| `confirmed_failure` | 40 |
| `evaluator_false_negative` | 13 |
| `policy_failure` | 1 |
| `confirmed_failure_hidden_by_judge` | 1 |

| Priority | จำนวน |
|---|---:|
| `P0` | 13 |
| `P1` | 70 |
| `P2` | 79 |

## Root-Cause Counts

| Cluster | จำนวน |
|---|---:|
| `general_output_contract_risk` | 66 |
| `clear_general_double_llm_latency` | 40 |
| `general_concept_misrouted_to_equipment` | 26 |
| `heuristic_judge_false_negative` | 13 |
| `substring_price_collision` | 9 |
| `runtime_exception_uninitialized_state` | 2 |
| `animal_crossing_control_collision_and_false_ambiguity` | 1 |
| `llm_route_regression_and_expensive_fallback` | 1 |
| `unsupported_freshness_claim` | 1 |
| `product_scope_and_missing_clarification` | 1 |
| `compound_split_missing_subanswer` | 1 |
| `single_llm_generation_latency` | 1 |

## รายข้อ

### 001. MB-0189-G-101 - animal_crossing_control_collision_and_false_ambiguity

- **คำถาม:** Animal Crossing: New Horizons คือเกมอะไร
- **สถานะ/Priority:** `confirmed_failure` / `P0`
- **อาการทั้งหมด:** `animal_crossing_control_collision_and_false_ambiguity, heuristic_judge_failed`
- **Expected contract:** category=`games`, must contain=`['Animal Crossing']`
- **Actual path:** `clarification/ambiguity_gate_clarification` / `pipeline:ambiguity_clarification` / wall `0.7906s` / visible LLM `700.30ms`
- **จุดแรกที่พลาด:** routing policy แล้วตามด้วย Ambiguity Gate
- **สิ่งที่พบ:** Typhoon mode=pipeline:ambiguity_clarification route=clarification/ambiguity_gate_clarification; wall=0.7906s visible_llm=700.30ms; judge_passed=False judge_errors=['category_mismatch:clarification', 'missing:Animal Crossing']; answer_body_chars=93; quality_flags=[]; No-LLM mode=pipeline:structured_game_detail passed=True wall=0.8667s
- **ลำดับเหตุ:** ชื่อเกม exact -> cross substring บังคับ controls -> LLM ซ่อม detail -> candidate list/detail margin ต่ำ -> clarification ทั้งที่ target ชัด
- **Root cause:** Crossing มี substring cross จึงถูกบังคับเป็น game control; LLM Intent ซ่อมเป็น games/detail แล้ว แต่ list/detail candidates ยังมี margin ต่ำจนถามกลับทั้งที่ resolve ชื่อเกมได้ exact
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, source_grounding_and_conflict_check`
- **เส้นทางที่ควรเป็น:** `games/game_detail_lookup` ด้วย `structured_game_detail from verified game catalog`
- **Source requirement:** Verified PSU game catalog: https://esports.phuket.psu.ac.th/Services/our-games
- **คำตอบจริง:**
> คำถามนี้มีได้หลายความหมายครับ ขอระบุเพิ่มนิดหนึ่งว่าต้องการถามเรื่องไหน: รายชื่อเกม/ข้อมูลเกม
- **ตัวอย่างคำตอบที่ควรได้:**
> Animal Crossing: New Horizons เป็นเกมแนว Life Simulation ที่ให้ผู้เล่นใช้ชีวิตบนเกาะ เก็บทรัพยากร ตกปลา จับแมลง ตกแต่งบ้านและเกาะ โดยที่ศูนย์มีให้เล่นใน Nintendo Switch Zone ครับ
> แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games
- **วิธีแก้:** ใช้ English word boundary สำหรับ control terms, เพิ่ม cue คือเกมอะไร เป็น detail และให้ exact entity + detail intent veto low-margin clarification
- **จุดโค้ด:** `data/routing/route_priority_matrix.json; app/pipeline/ambiguity_gate.py; game entity resolver`
- **Regression assertion:** Animal Crossing ต้องไม่ hit cross control rule และต้องตอบ structured detail โดยไม่ clarification
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 002. MB-0607-CR-071 - runtime_exception_uninitialized_state

- **คำถาม:** ROV ถ้าใช้ bug จะโดนอะไร
- **สถานะ/Priority:** `confirmed_failure` / `P0`
- **อาการทั้งหมด:** `runtime_exception_uninitialized_state, heuristic_judge_failed`
- **Expected contract:** category=`competition_rules`, must contain=`['ROV', 'กติกา', 'แข่งขัน', 'ยังไม่พบ']`
- **Actual path:** `/` / `exception` / wall `0.2438s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** single-question fallback request state
- **สิ่งที่พบ:** Typhoon mode=exception route=/; wall=0.2438s visible_llm=0.00ms; judge_passed=False judge_errors=['exception:UnboundLocalError']; answer_body_chars=0; quality_flags=[]; No-LLM mode=pipeline:experimental_rag_direct_fallback passed=True wall=0.7083s
- **ลำดับเหตุ:** คำถามเข้า single path -> fallback ตรวจ RAG/LLM state -> อ่าน local variable ที่ยังไม่มีค่า -> exception -> ไม่มี final answer
- **Root cause:** _answer_single ใช้ rag_llm_attempted/rag_source_conflict โดยไม่ได้ initialize เหมือน _answer_multi จึงเกิด UnboundLocalError เมื่อเข้า fallback บางเส้นทาง
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, source_grounding_and_conflict_check`
- **เส้นทางที่ควรเป็น:** `route เดิมตามคำถาม แล้วจบที่ verified retrieval/clarification/no-answer โดยไม่ exception` ด้วย `shared RequestState defaults + guarded retrieval/source veto`
- **Source requirement:** ต้องมี ROV bug-rule evidence โดยตรง; ปัจจุบันไม่พบ จึงต้อง no-answer
- **คำตอบจริง:**

- **ตัวอย่างคำตอบที่ควรได้:**
> ยังไม่พบกติกา ROV ที่ยืนยันบทลงโทษกรณีใช้ bug ในข้อมูลปัจจุบัน จึงไม่ควรนำกติกาของเกมอื่นหรือบทลงโทษเรื่องอื่นมาตอบแทนครับ
- **วิธีแก้:** สร้าง request-local state object ที่ initialize ค่า RAG/LLM flags ครั้งเดียวก่อนแยก single/compound และเพิ่ม direct exception regression
- **จุดโค้ด:** `app/pipeline/engine.py:_answer_single,_answer_multi; request-state helper ใหม่หรือ schema เดิม`
- **Regression assertion:** คำถามเดิมต้องไม่ exception, validation ต้องทำงาน และ unsupported source ต้องไม่ถูกนำมาตอบแทน
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 003. MB-0636-ANA-010 - runtime_exception_uninitialized_state

- **คำถาม:** จอง
- **สถานะ/Priority:** `confirmed_failure` / `P0`
- **อาการทั้งหมด:** `runtime_exception_uninitialized_state, heuristic_judge_failed`
- **Expected contract:** category=`['clarification', 'games', 'equipment', 'service_fee', 'reservation', 'no_answer']`, must contain=`['หมายถึง', 'พิมพ์', 'ยังไม่', 'เกม', 'อุปกรณ์', 'ราคา', 'จอง']`
- **Actual path:** `/` / `exception` / wall `1.3628s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** single-question fallback request state
- **สิ่งที่พบ:** Typhoon mode=exception route=/; wall=1.3628s visible_llm=0.00ms; judge_passed=False judge_errors=['exception:UnboundLocalError']; answer_body_chars=0; quality_flags=[]; No-LLM mode=pipeline:answer_contract_no_answer passed=True wall=0.5758s
- **ลำดับเหตุ:** คำถามเข้า single path -> fallback ตรวจ RAG/LLM state -> อ่าน local variable ที่ยังไม่มีค่า -> exception -> ไม่มี final answer
- **Root cause:** _answer_single ใช้ rag_llm_attempted/rag_source_conflict โดยไม่ได้ initialize เหมือน _answer_multi จึงเกิด UnboundLocalError เมื่อเข้า fallback บางเส้นทาง
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, source_grounding_and_conflict_check`
- **เส้นทางที่ควรเป็น:** `route เดิมตามคำถาม แล้วจบที่ verified retrieval/clarification/no-answer โดยไม่ exception` ด้วย `shared RequestState defaults + guarded retrieval/source veto`
- **Source requirement:** ยังไม่ต้องดึง source จนกว่าผู้ใช้ระบุบริการ/วันเวลา
- **คำตอบจริง:**

- **ตัวอย่างคำตอบที่ควรได้:**
> ต้องการจองบริการไหนครับ เช่น PC, PS5, Nintendo Switch, VR หรือ Cockpit และต้องการใช้วันกับเวลาใด
- **วิธีแก้:** สร้าง request-local state object ที่ initialize ค่า RAG/LLM flags ครั้งเดียวก่อนแยก single/compound และเพิ่ม direct exception regression
- **จุดโค้ด:** `app/pipeline/engine.py:_answer_single,_answer_multi; request-state helper ใหม่หรือ schema เดิม`
- **Regression assertion:** คำถามเดิมต้องไม่ exception, validation ต้องทำงาน และ unsupported source ต้องไม่ถูกนำมาตอบแทน
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 004. MB-1557-GL-232 - substring_price_collision

- **คำถาม:** เฟรมเรตกับความละเอียดต่างกันยังไง อธิบายข้อดีข้อเสียสั้น ๆ
- **สถานะ/Priority:** `confirmed_failure` / `P0`
- **อาการทั้งหมด:** `substring_price_collision, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['เฟรม', 'ความละเอียด']`
- **Actual path:** `clarification/ambiguity_gate_clarification` / `pipeline:ambiguity_clarification` / wall `0.2543s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** price lexical detection -> Ambiguity Gate
- **สิ่งที่พบ:** Typhoon mode=pipeline:ambiguity_clarification route=clarification/ambiguity_gate_clarification; wall=0.2543s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:clarification', 'missing_any:เฟรม|ความละเอียด']; answer_body_chars=149; quality_flags=[]; No-LLM mode=pipeline:ambiguity_clarification passed=False wall=0.2269s
- **ลำดับเหตุ:** general query -> router/intent ยังเป็น general -> substring เสีย ถูกตั้งเป็น price signal -> Ambiguity Gate ขอ service target -> ตอบถามกลับผิดเรื่อง
- **Root cause:** raw substring เห็นคำว่า เสีย ภายในคำว่า ข้อเสีย จึงตั้ง price_intent และถามกลับเรื่องบริการ/ราคา ทั้งที่ router กับ Universal Intent เป็น general
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM with answer-shape contract`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง
> เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`
- **ตัวอย่างคำตอบที่ควรได้:**
> เฟรมเรตบอกความลื่นของภาพ ส่วนความละเอียดบอกความคมชัดครับ ค่าสูงให้ภาพดีขึ้น แต่ทั้งสองอย่างใช้พลังประมวลผลมากขึ้น จึงต้องปรับให้สมดุลกับเครื่อง
- **วิธีแก้:** แทน term-in-text ด้วย lexical matcher กลางที่รองรับ exact phrase/context และ negative phrase เช่น ข้อเสีย ไม่ใช่ price intent
- **จุดโค้ด:** `app/pipeline/ambiguity_gate.py; app/pipeline/tool_preconditions.py; app/runtime/fast_answer.py; shared lexical matcher`
- **Regression assertion:** ทุกคำถามที่มี ข้อดีข้อเสีย ต้องไม่เกิด price_missing_service_or_game_target หากไม่มีบริการ ราคา หรือจำนวนเงิน
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 005. MB-1558-GL-233 - substring_price_collision

- **คำถาม:** API คืออะไร อธิบายข้อดีข้อเสียสั้น ๆ
- **สถานะ/Priority:** `confirmed_failure` / `P0`
- **อาการทั้งหมด:** `substring_price_collision, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['API', 'เชื่อมต่อ']`
- **Actual path:** `clarification/ambiguity_gate_clarification` / `pipeline:ambiguity_clarification` / wall `0.2202s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** price lexical detection -> Ambiguity Gate
- **สิ่งที่พบ:** Typhoon mode=pipeline:ambiguity_clarification route=clarification/ambiguity_gate_clarification; wall=0.2202s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:clarification', 'missing_any:API|เชื่อมต่อ']; answer_body_chars=149; quality_flags=[]; No-LLM mode=pipeline:ambiguity_clarification passed=False wall=0.2279s
- **ลำดับเหตุ:** general query -> router/intent ยังเป็น general -> substring เสีย ถูกตั้งเป็น price signal -> Ambiguity Gate ขอ service target -> ตอบถามกลับผิดเรื่อง
- **Root cause:** raw substring เห็นคำว่า เสีย ภายในคำว่า ข้อเสีย จึงตั้ง price_intent และถามกลับเรื่องบริการ/ราคา ทั้งที่ router กับ Universal Intent เป็น general
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM with answer-shape contract`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง
> เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`
- **ตัวอย่างคำตอบที่ควรได้:**
> API คือช่องทางที่โปรแกรมใช้สื่อสารและแลกข้อมูลกันครับ ข้อดีคือเชื่อมระบบได้เป็นมาตรฐาน ส่วนข้อจำกัดคือต้องดูแลสิทธิ์ ความปลอดภัย และความพร้อมใช้งานของบริการ
- **วิธีแก้:** แทน term-in-text ด้วย lexical matcher กลางที่รองรับ exact phrase/context และ negative phrase เช่น ข้อเสีย ไม่ใช่ price intent
- **จุดโค้ด:** `app/pipeline/ambiguity_gate.py; app/pipeline/tool_preconditions.py; app/runtime/fast_answer.py; shared lexical matcher`
- **Regression assertion:** ทุกคำถามที่มี ข้อดีข้อเสีย ต้องไม่เกิด price_missing_service_or_game_target หากไม่มีบริการ ราคา หรือจำนวนเงิน
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 006. MB-1559-GL-234 - substring_price_collision

- **คำถาม:** JSON คืออะไร อธิบายข้อดีข้อเสียสั้น ๆ
- **สถานะ/Priority:** `confirmed_failure` / `P0`
- **อาการทั้งหมด:** `substring_price_collision, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['JSON', 'ข้อมูล']`
- **Actual path:** `clarification/ambiguity_gate_clarification` / `pipeline:ambiguity_clarification` / wall `0.2079s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** price lexical detection -> Ambiguity Gate
- **สิ่งที่พบ:** Typhoon mode=pipeline:ambiguity_clarification route=clarification/ambiguity_gate_clarification; wall=0.2079s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:clarification', 'missing_any:JSON|ข้อมูล']; answer_body_chars=149; quality_flags=[]; No-LLM mode=pipeline:ambiguity_clarification passed=False wall=0.2200s
- **ลำดับเหตุ:** general query -> router/intent ยังเป็น general -> substring เสีย ถูกตั้งเป็น price signal -> Ambiguity Gate ขอ service target -> ตอบถามกลับผิดเรื่อง
- **Root cause:** raw substring เห็นคำว่า เสีย ภายในคำว่า ข้อเสีย จึงตั้ง price_intent และถามกลับเรื่องบริการ/ราคา ทั้งที่ router กับ Universal Intent เป็น general
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM with answer-shape contract`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง
> เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`
- **ตัวอย่างคำตอบที่ควรได้:**
> JSON คือรูปแบบข้อความสำหรับเก็บและส่งข้อมูลเป็นคู่ key-value ครับ ข้อดีคืออ่านง่ายและใช้ร่วมกันได้หลายภาษา ส่วนข้อจำกัดคือ syntax ต้องถูกต้องและไม่เหมาะกับข้อมูลไบนารีขนาดใหญ่
- **วิธีแก้:** แทน term-in-text ด้วย lexical matcher กลางที่รองรับ exact phrase/context และ negative phrase เช่น ข้อเสีย ไม่ใช่ price intent
- **จุดโค้ด:** `app/pipeline/ambiguity_gate.py; app/pipeline/tool_preconditions.py; app/runtime/fast_answer.py; shared lexical matcher`
- **Regression assertion:** ทุกคำถามที่มี ข้อดีข้อเสีย ต้องไม่เกิด price_missing_service_or_game_target หากไม่มีบริการ ราคา หรือจำนวนเงิน
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 007. MB-1560-GL-235 - substring_price_collision

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค อธิบายข้อดีข้อเสียสั้น ๆ
- **สถานะ/Priority:** `confirmed_failure` / `P0`
- **อาการทั้งหมด:** `substring_price_collision, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `clarification/ambiguity_gate_clarification` / `pipeline:ambiguity_clarification` / wall `0.2321s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** price lexical detection -> Ambiguity Gate
- **สิ่งที่พบ:** Typhoon mode=pipeline:ambiguity_clarification route=clarification/ambiguity_gate_clarification; wall=0.2321s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:clarification', 'missing_any:ขอบคุณ']; answer_body_chars=149; quality_flags=[]; No-LLM mode=pipeline:ambiguity_clarification passed=False wall=0.2260s
- **ลำดับเหตุ:** general query -> router/intent ยังเป็น general -> substring เสีย ถูกตั้งเป็น price signal -> Ambiguity Gate ขอ service target -> ตอบถามกลับผิดเรื่อง
- **Root cause:** raw substring เห็นคำว่า เสีย ภายในคำว่า ข้อเสีย จึงตั้ง price_intent และถามกลับเรื่องบริการ/ราคา ทั้งที่ router กับ Universal Intent เป็น general
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM with answer-shape contract`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง
> เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอบคุณมากครับสำหรับความช่วยเหลือ ข้อดีของคำพูดสุภาพคือแสดงความเคารพ ส่วนข้อควรระวังคือไม่ควรใช้ถ้อยคำเป็นทางการเกินบริบทครับ
- **วิธีแก้:** แทน term-in-text ด้วย lexical matcher กลางที่รองรับ exact phrase/context และ negative phrase เช่น ข้อเสีย ไม่ใช่ price intent
- **จุดโค้ด:** `app/pipeline/ambiguity_gate.py; app/pipeline/tool_preconditions.py; app/runtime/fast_answer.py; shared lexical matcher`
- **Regression assertion:** ทุกคำถามที่มี ข้อดีข้อเสีย ต้องไม่เกิด price_missing_service_or_game_target หากไม่มีบริการ ราคา หรือจำนวนเงิน
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 008. MB-1561-GL-236 - substring_price_collision

- **คำถาม:** แปลคำว่า reservation เป็นภาษาไทย อธิบายข้อดีข้อเสียสั้น ๆ
- **สถานะ/Priority:** `confirmed_failure` / `P0`
- **อาการทั้งหมด:** `substring_price_collision, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['จอง']`
- **Actual path:** `clarification/ambiguity_gate_clarification` / `pipeline:ambiguity_clarification` / wall `0.3239s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** price lexical detection -> Ambiguity Gate
- **สิ่งที่พบ:** Typhoon mode=pipeline:ambiguity_clarification route=clarification/ambiguity_gate_clarification; wall=0.3239s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:clarification', 'missing_any:จอง']; answer_body_chars=149; quality_flags=[]; No-LLM mode=pipeline:ambiguity_clarification passed=False wall=0.3612s
- **ลำดับเหตุ:** general query -> router/intent ยังเป็น general -> substring เสีย ถูกตั้งเป็น price signal -> Ambiguity Gate ขอ service target -> ตอบถามกลับผิดเรื่อง
- **Root cause:** raw substring เห็นคำว่า เสีย ภายในคำว่า ข้อเสีย จึงตั้ง price_intent และถามกลับเรื่องบริการ/ราคา ทั้งที่ router กับ Universal Intent เป็น general
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM with answer-shape contract`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง
> เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`
- **ตัวอย่างคำตอบที่ควรได้:**
> `reservation` แปลว่า “การจอง” หรือ “การสำรองล่วงหน้า” ครับ ข้อดีคือช่วยรับประกันสิทธิ์ใช้งาน ส่วนข้อจำกัดคืออาจมีเงื่อนไขการยกเลิกหรือชำระเงิน
- **วิธีแก้:** แทน term-in-text ด้วย lexical matcher กลางที่รองรับ exact phrase/context และ negative phrase เช่น ข้อเสีย ไม่ใช่ price intent
- **จุดโค้ด:** `app/pipeline/ambiguity_gate.py; app/pipeline/tool_preconditions.py; app/runtime/fast_answer.py; shared lexical matcher`
- **Regression assertion:** ทุกคำถามที่มี ข้อดีข้อเสีย ต้องไม่เกิด price_missing_service_or_game_target หากไม่มีบริการ ราคา หรือจำนวนเงิน
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 009. MB-1562-GL-237 - substring_price_collision

- **คำถาม:** เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค อธิบายข้อดีข้อเสียสั้น ๆ
- **สถานะ/Priority:** `confirmed_failure` / `P0`
- **อาการทั้งหมด:** `substring_price_collision, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['กิจกรรม']`
- **Actual path:** `clarification/ambiguity_gate_clarification` / `pipeline:ambiguity_clarification` / wall `0.2794s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** price lexical detection -> Ambiguity Gate
- **สิ่งที่พบ:** Typhoon mode=pipeline:ambiguity_clarification route=clarification/ambiguity_gate_clarification; wall=0.2794s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:clarification', 'missing_any:กิจกรรม']; answer_body_chars=149; quality_flags=[]; No-LLM mode=pipeline:ambiguity_clarification passed=False wall=0.2763s
- **ลำดับเหตุ:** general query -> router/intent ยังเป็น general -> substring เสีย ถูกตั้งเป็น price signal -> Ambiguity Gate ขอ service target -> ตอบถามกลับผิดเรื่อง
- **Root cause:** raw substring เห็นคำว่า เสีย ภายในคำว่า ข้อเสีย จึงตั้ง price_intent และถามกลับเรื่องบริการ/ราคา ทั้งที่ router กับ Universal Intent เป็น general
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM with answer-shape contract`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง
> เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอเชิญทุกท่านเข้าร่วมกิจกรรมเพื่อสร้างการมีส่วนร่วมที่ดี โดยควรระบุวัน เวลา และสถานที่ให้ชัดเจนครับ
- **วิธีแก้:** แทน term-in-text ด้วย lexical matcher กลางที่รองรับ exact phrase/context และ negative phrase เช่น ข้อเสีย ไม่ใช่ price intent
- **จุดโค้ด:** `app/pipeline/ambiguity_gate.py; app/pipeline/tool_preconditions.py; app/runtime/fast_answer.py; shared lexical matcher`
- **Regression assertion:** ทุกคำถามที่มี ข้อดีข้อเสีย ต้องไม่เกิด price_missing_service_or_game_target หากไม่มีบริการ ราคา หรือจำนวนเงิน
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 010. MB-1563-GL-238 - substring_price_collision

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น อธิบายข้อดีข้อเสียสั้น ๆ
- **สถานะ/Priority:** `confirmed_failure` / `P0`
- **อาการทั้งหมด:** `substring_price_collision, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `clarification/ambiguity_gate_clarification` / `pipeline:ambiguity_clarification` / wall `0.3617s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** price lexical detection -> Ambiguity Gate
- **สิ่งที่พบ:** Typhoon mode=pipeline:ambiguity_clarification route=clarification/ambiguity_gate_clarification; wall=0.3617s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:clarification', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=149; quality_flags=[]; No-LLM mode=pipeline:ambiguity_clarification passed=False wall=0.3764s
- **ลำดับเหตุ:** general query -> router/intent ยังเป็น general -> substring เสีย ถูกตั้งเป็น price signal -> Ambiguity Gate ขอ service target -> ตอบถามกลับผิดเรื่อง
- **Root cause:** raw substring เห็นคำว่า เสีย ภายในคำว่า ข้อเสีย จึงตั้ง price_intent และถามกลับเรื่องบริการ/ราคา ทั้งที่ router กับ Universal Intent เป็น general
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM with answer-shape contract`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง
> เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical ใช้สวิตช์แยกใต้แต่ละปุ่มครับ ข้อดีคือกดแม่น ทน และเลือกสัมผัสได้ ส่วนข้อเสียคือมักแพง หนัก และเสียงดังกว่าคีย์บอร์ด membrane
- **วิธีแก้:** แทน term-in-text ด้วย lexical matcher กลางที่รองรับ exact phrase/context และ negative phrase เช่น ข้อเสีย ไม่ใช่ price intent
- **จุดโค้ด:** `app/pipeline/ambiguity_gate.py; app/pipeline/tool_preconditions.py; app/runtime/fast_answer.py; shared lexical matcher`
- **Regression assertion:** ทุกคำถามที่มี ข้อดีข้อเสีย ต้องไม่เกิด price_missing_service_or_game_target หากไม่มีบริการ ราคา หรือจำนวนเงิน
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 011. MB-1564-GL-239 - substring_price_collision

- **คำถาม:** GPU คืออะไรแบบเข้าใจง่าย อธิบายข้อดีข้อเสียสั้น ๆ
- **สถานะ/Priority:** `confirmed_failure` / `P0`
- **อาการทั้งหมด:** `substring_price_collision, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['GPU', 'กราฟิก']`
- **Actual path:** `clarification/ambiguity_gate_clarification` / `pipeline:ambiguity_clarification` / wall `0.2816s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** price lexical detection -> Ambiguity Gate
- **สิ่งที่พบ:** Typhoon mode=pipeline:ambiguity_clarification route=clarification/ambiguity_gate_clarification; wall=0.2816s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:clarification', 'missing_any:GPU|กราฟิก']; answer_body_chars=149; quality_flags=[]; No-LLM mode=pipeline:ambiguity_clarification passed=False wall=0.2930s
- **ลำดับเหตุ:** general query -> router/intent ยังเป็น general -> substring เสีย ถูกตั้งเป็น price signal -> Ambiguity Gate ขอ service target -> ตอบถามกลับผิดเรื่อง
- **Root cause:** raw substring เห็นคำว่า เสีย ภายในคำว่า ข้อเสีย จึงตั้ง price_intent และถามกลับเรื่องบริการ/ราคา ทั้งที่ router กับ Universal Intent เป็น general
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM with answer-shape contract`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง
> เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`
- **ตัวอย่างคำตอบที่ควรได้:**
> GPU คือหน่วยประมวลผลที่ถนัดงานภาพและการคำนวณพร้อมกันจำนวนมากครับ ข้อดีคือช่วยให้เกมและงานกราฟิกลื่นขึ้น ส่วนข้อเสียคือเพิ่มราคา การใช้ไฟ และความร้อน
- **วิธีแก้:** แทน term-in-text ด้วย lexical matcher กลางที่รองรับ exact phrase/context และ negative phrase เช่น ข้อเสีย ไม่ใช่ price intent
- **จุดโค้ด:** `app/pipeline/ambiguity_gate.py; app/pipeline/tool_preconditions.py; app/runtime/fast_answer.py; shared lexical matcher`
- **Regression assertion:** ทุกคำถามที่มี ข้อดีข้อเสีย ต้องไม่เกิด price_missing_service_or_game_target หากไม่มีบริการ ราคา หรือจำนวนเงิน
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 012. MB-1565-GL-240 - substring_price_collision

- **คำถาม:** server กับ client ต่างกันยังไง อธิบายข้อดีข้อเสียสั้น ๆ
- **สถานะ/Priority:** `confirmed_failure` / `P0`
- **อาการทั้งหมด:** `substring_price_collision, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['server', 'client']`
- **Actual path:** `clarification/ambiguity_gate_clarification` / `pipeline:ambiguity_clarification` / wall `0.2877s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** price lexical detection -> Ambiguity Gate
- **สิ่งที่พบ:** Typhoon mode=pipeline:ambiguity_clarification route=clarification/ambiguity_gate_clarification; wall=0.2877s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:clarification', 'missing_any:server|client']; answer_body_chars=149; quality_flags=[]; No-LLM mode=pipeline:ambiguity_clarification passed=False wall=0.3089s
- **ลำดับเหตุ:** general query -> router/intent ยังเป็น general -> substring เสีย ถูกตั้งเป็น price signal -> Ambiguity Gate ขอ service target -> ตอบถามกลับผิดเรื่อง
- **Root cause:** raw substring เห็นคำว่า เสีย ภายในคำว่า ข้อเสีย จึงตั้ง price_intent และถามกลับเรื่องบริการ/ราคา ทั้งที่ router กับ Universal Intent เป็น general
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM with answer-shape contract`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอรู้บริการหรือโซนก่อนครับ จะได้ตอบราคาให้ตรง
> เช่น `PS5 ราคาเท่าไหร่`, `Nintendo 3-4 คนกี่บาท`, `VR 30 นาทีราคาเท่าไหร่` หรือ `Tekken 8 ราคาเท่าไหร่`
- **ตัวอย่างคำตอบที่ควรได้:**
> Server เป็นฝ่ายให้บริการ ส่วน client เป็นฝ่ายส่งคำขอและแสดงผลครับ การรวมข้อมูลที่ server จัดการง่าย แต่ server ล่มจะกระทบหลาย client ขณะที่ client ทำงานบางอย่างเองได้แต่ต้องดูแลหลายอุปกรณ์
- **วิธีแก้:** แทน term-in-text ด้วย lexical matcher กลางที่รองรับ exact phrase/context และ negative phrase เช่น ข้อเสีย ไม่ใช่ price intent
- **จุดโค้ด:** `app/pipeline/ambiguity_gate.py; app/pipeline/tool_preconditions.py; app/runtime/fast_answer.py; shared lexical matcher`
- **Regression assertion:** ทุกคำถามที่มี ข้อดีข้อเสีย ต้องไม่เกิด price_missing_service_or_game_target หากไม่มีบริการ ราคา หรือจำนวนเงิน
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 013. MB-0649-ANA-023 - unsupported_freshness_claim

- **คำถาม:** เพลงฮิตตอนนี้คืออะไร
- **สถานะ/Priority:** `confirmed_failure` / `P0`
- **อาการทั้งหมด:** `unsupported_freshness_claim, heuristic_judge_failed, latency_over_10s`
- **Expected contract:** category=`['no_answer', 'games', 'general']`, must contain=`['ยังไม่พบ', 'ไม่มี', 'ไม่ได้อยู่', 'ตอบจากข้อมูล']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `11.2947s` / visible LLM `11090.39ms`
- **จุดแรกที่พลาด:** freshness/source guard before General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=11.2947s visible_llm=11090.39ms; judge_passed=False judge_errors=['missing_any:ยังไม่พบ|ไม่มี|ไม่ได้อยู่|ตอบจากข้อมูล']; answer_body_chars=232; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.1853s
- **ลำดับเหตุ:** current query -> ไม่มี live retrieval precondition -> General LLM ใช้ model memory -> สร้างชื่อเพลงที่ยืนยันเวลาไม่ได้
- **Root cause:** คำว่า ตอนนี้ ต้องการข้อมูลสด แต่ระบบไม่มี live source แล้วยังปล่อย model memory สร้างชื่อเพลง ทำให้ claim ไม่ยืนยันและล้าสมัยได้
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, source_grounding_and_conflict_check`
- **เส้นทางที่ควรเป็น:** `general/current_information requiring live evidence` ด้วย `live Web/API retrieval or safe no-answer/clarification`
- **Source requirement:** Live chart Web/API พร้อม retrieval timestamp; ไม่มี source ให้ no-answer
- **คำตอบจริง:**
> เพลงฮิตตอนนี้อาจแตกต่างกันไปตามประเทศและช่วงเวลา เช่น เพลง "Flowers" โดย Miley Cyrus หรือเพลงแนว Pop/R&B จากศิลปินต่างชาติที่กำลังมาแรงในขณะนี้ แต่ข้อมูลอาจเปลี่ยนแปลงได้ตลอดเวลา กรุณาตรวจสอบแหล่งข้อมูลอื่นเพื่อความถูกต้องที่สุดครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ตอนนี้ระบบไม่มีข้อมูลชาร์ตเพลงสดที่ยืนยันได้ครับ ต้องการดูเพลงฮิตจากประเทศไทยบน Spotify, YouTube หรือแพลตฟอร์มใดเป็นพิเศษ
- **วิธีแก้:** เพิ่ม freshness classifier และ source precondition; current/latest claim ต้องมี URL กับ retrieval timestamp มิฉะนั้น hard veto
- **จุดโค้ด:** `Boundary/Source Guard; candidate preconditions; General LLM fallback policy`
- **Regression assertion:** ไม่มี live sourceต้องไม่ปรากฏชื่อเพลง ข่าว ราคา หรือสถานะปัจจุบันที่ model เดาเอง
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 014. MB-1331-GL-006 - clear_general_double_llm_latency

- **คำถาม:** แปลคำว่า reservation เป็นภาษาไทย
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['จอง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `13.5623s` / visible LLM `6400.71ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=13.5623s visible_llm=6400.71ms; judge_passed=True judge_errors=[]; answer_body_chars=10; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.2829s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> การจองครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> `reservation` แปลว่า “การจอง” หรือ “การสำรอง” ขึ้นอยู่กับบริบทครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 015. MB-1332-GL-007 - clear_general_double_llm_latency

- **คำถาม:** เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['กิจกรรม']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `14.7671s` / visible LLM `7693.13ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=14.7671s visible_llm=7693.13ms; judge_passed=True judge_errors=[]; answer_body_chars=111; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2896s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอเชิญทุกท่านร่วมเป็นส่วนหนึ่งในกิจกรรมพิเศษนี้เพื่อสร้างความสนุกสนานและความทรงจำร่วมกันอย่างอบอุ่นและสุภาพนะคะ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอเชิญทุกท่านเข้าร่วมกิจกรรมและมาร่วมสร้างประสบการณ์ดี ๆ ไปด้วยกันครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 016. MB-1341-GL-016 - clear_general_double_llm_latency

- **คำถาม:** แปลคำว่า reservation เป็นภาษาไทย ตอบสั้น ๆ
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['จอง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `13.3109s` / visible LLM `6209.02ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=13.3109s visible_llm=6209.02ms; judge_passed=True judge_errors=[]; answer_body_chars=10; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.2544s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> การจองครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> `reservation` แปลว่า “การจอง” หรือ “การสำรอง” ขึ้นอยู่กับบริบทครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 017. MB-1342-GL-017 - clear_general_double_llm_latency

- **คำถาม:** เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ตอบสั้น ๆ
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['กิจกรรม']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `14.7101s` / visible LLM `7791.57ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=14.7101s visible_llm=7791.57ms; judge_passed=True judge_errors=[]; answer_body_chars=126; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2377s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอเชิญทุกท่านร่วมเป็นส่วนหนึ่งในกิจกรรมพิเศษนี้นะคะ เพื่อสร้างความสนุกสนานและเพิ่มพลังบวกให้กับชีวิตประจำวันของเราได้อีกครั้ง!
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอเชิญทุกท่านเข้าร่วมกิจกรรมและมาร่วมสร้างประสบการณ์ดี ๆ ไปด้วยกันครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 018. MB-1351-GL-026 - clear_general_double_llm_latency

- **คำถาม:** แปลคำว่า reservation เป็นภาษาไทย ขอแบบเข้าใจง่าย
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s, mixed_gender_particles`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['จอง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `13.4945s` / visible LLM `6353.44ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=13.4945s visible_llm=6353.44ms; judge_passed=True judge_errors=[]; answer_body_chars=14; quality_flags=['mixed_gender_particles']; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.2168s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น; output flags=mixed_gender_particles
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> การจองครับ/ค่ะ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> `reservation` แปลว่า “การจอง” หรือ “การสำรอง” ขึ้นอยู่กับบริบทครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 019. MB-1352-GL-027 - clear_general_double_llm_latency

- **คำถาม:** เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ขอแบบเข้าใจง่าย
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['กิจกรรม']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `14.0005s` / visible LLM `6790.75ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=14.0005s visible_llm=6790.75ms; judge_passed=True judge_errors=[]; answer_body_chars=61; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2230s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> เรามีกิจกรรมสนุก ๆ เตรียมไว้แล้ว ร่วมมาลุยกับเราได้เลยนะครับ!
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอเชิญทุกท่านเข้าร่วมกิจกรรมและมาร่วมสร้างประสบการณ์ดี ๆ ไปด้วยกันครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 020. MB-1361-GL-036 - clear_general_double_llm_latency

- **คำถาม:** แปลคำว่า reservation เป็นภาษาไทย ตอบเป็นภาษาไทย
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['จอง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `13.0868s` / visible LLM `6121.98ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=13.0868s visible_llm=6121.98ms; judge_passed=True judge_errors=[]; answer_body_chars=10; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.2157s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> การจองครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> `reservation` แปลว่า “การจอง” หรือ “การสำรอง” ขึ้นอยู่กับบริบทครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 021. MB-1362-GL-037 - clear_general_double_llm_latency

- **คำถาม:** เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ตอบเป็นภาษาไทย
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s, awkward_thai_phrase`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['กิจกรรม']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `14.6473s` / visible LLM `7523.67ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=14.6473s visible_llm=7523.67ms; judge_passed=True judge_errors=[]; answer_body_chars=81; quality_flags=['awkward_thai_phrase']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2455s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น; output flags=awkward_thai_phrase
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอเชิญทุกท่านร่วมตื่นเต้นร่วมสนุกกับกิจกรรมพิเศษที่กำลังจะมาถึงอย่างไม่ต้องรอช้า!
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอเชิญทุกท่านเข้าร่วมกิจกรรมและมาร่วมสร้างประสบการณ์ดี ๆ ไปด้วยกันครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 022. MB-1371-GL-046 - clear_general_double_llm_latency

- **คำถาม:** แปลคำว่า reservation เป็นภาษาไทย ไม่ต้องยาว
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['จอง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `13.1599s` / visible LLM `6285.84ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=13.1599s visible_llm=6285.84ms; judge_passed=True judge_errors=[]; answer_body_chars=10; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.2595s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> การจองครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> `reservation` แปลว่า “การจอง” หรือ “การสำรอง” ขึ้นอยู่กับบริบทครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 023. MB-1372-GL-047 - clear_general_double_llm_latency

- **คำถาม:** เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ไม่ต้องยาว
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s, emoji_present`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['กิจกรรม']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `13.8322s` / visible LLM `6900.91ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=13.8322s visible_llm=6900.91ms; judge_passed=True judge_errors=[]; answer_body_chars=66; quality_flags=['emoji_present']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2737s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น; output flags=emoji_present
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอเชิญทุกท่านร่วมเป็นส่วนหนึ่งในกิจกรรมพิเศษนี้อย่างอบอุ่นใจนะคะ 😊
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอเชิญทุกท่านเข้าร่วมกิจกรรมและมาร่วมสร้างประสบการณ์ดี ๆ ไปด้วยกันครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 024. MB-1381-GL-056 - clear_general_double_llm_latency

- **คำถาม:** แปลคำว่า reservation เป็นภาษาไทย ขอ 1 ย่อหน้า
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['จอง']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `15.8927s` / visible LLM `8801.10ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=15.8927s visible_llm=8801.10ms; judge_passed=True judge_errors=[]; answer_body_chars=289; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.2173s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> คำว่า "reservation" เมื่อแปลเป็นภาษาไทย หมายถึง การจองล่วงหน้า หรือการจัดสรรที่นั่ง เวลา พื้นที่ หรือสิ่งของใด ๆ เพื่อใช้งานในอนาคต โดยมักใช้ในบริบทต่าง ๆ เช่น การจองห้องพัก การจองโต๊ะอาหาร หรือการจองเวลาให้บริการต่าง ๆ เนื่องจากคำนี้มีความหมายหลากหลายขึ้นอยู่กับบริบทที่ใช้งานอยู่เสมอครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> `reservation` แปลว่า “การจอง” หรือ “การสำรอง” ขึ้นอยู่กับบริบทครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 025. MB-1382-GL-057 - clear_general_double_llm_latency

- **คำถาม:** เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ขอ 1 ย่อหน้า
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['กิจกรรม']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `14.1058s` / visible LLM `7096.87ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=14.1058s visible_llm=7096.87ms; judge_passed=True judge_errors=[]; answer_body_chars=79; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1948s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอเชิญชวนทุกท่านร่วมเป็นส่วนหนึ่งในกิจกรรมสนุกสนานและสร้างสรรค์ร่วมกันได้ทันที!
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอเชิญทุกท่านเข้าร่วมกิจกรรมและมาร่วมสร้างประสบการณ์ดี ๆ ไปด้วยกันครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 026. MB-1401-GL-076 - clear_general_double_llm_latency

- **คำถาม:** แปลคำว่า reservation เป็นภาษาไทย ตอบแบบเด็กปีหนึ่งเข้าใจได้
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['จอง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `13.2412s` / visible LLM `6165.53ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=13.2412s visible_llm=6165.53ms; judge_passed=True judge_errors=[]; answer_body_chars=10; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.2754s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> การจองครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> `reservation` แปลว่า “การจอง” หรือ “การสำรอง” ขึ้นอยู่กับบริบทครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 027. MB-1402-GL-077 - clear_general_double_llm_latency

- **คำถาม:** เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ตอบแบบเด็กปีหนึ่งเข้าใจได้
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s, emoji_present`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['กิจกรรม']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `13.7362s` / visible LLM `6686.54ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=13.7362s visible_llm=6686.54ms; judge_passed=True judge_errors=[]; answer_body_chars=35; quality_flags=['emoji_present']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2286s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น; output flags=emoji_present
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> มาสนุกกับกิจกรรมน่ารัก ๆ กันเถอะ! 😊
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอเชิญทุกท่านเข้าร่วมกิจกรรมและมาร่วมสร้างประสบการณ์ดี ๆ ไปด้วยกันครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 028. MB-1411-GL-086 - clear_general_double_llm_latency

- **คำถาม:** แปลคำว่า reservation เป็นภาษาไทย ขอแบบไม่ใช้ศัพท์ยาก
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['จอง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `13.3484s` / visible LLM `6383.40ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=13.3484s visible_llm=6383.40ms; judge_passed=True judge_errors=[]; answer_body_chars=10; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.2302s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> การจองครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> `reservation` แปลว่า “การจอง” หรือ “การสำรอง” ขึ้นอยู่กับบริบทครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 029. MB-1412-GL-087 - clear_general_double_llm_latency

- **คำถาม:** เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ขอแบบไม่ใช้ศัพท์ยาก
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s, emoji_present, awkward_thai_phrase`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['กิจกรรม']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `13.7373s` / visible LLM `6731.30ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=13.7373s visible_llm=6731.30ms; judge_passed=True judge_errors=[]; answer_body_chars=62; quality_flags=['emoji_present', 'awkward_thai_phrase']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2057s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น; output flags=emoji_present, awkward_thai_phrase
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> เรียนชวนทุกคนมาร่วมสนุกกับกิจกรรมน่ารัก ๆ เหล่านี้ได้เลยนะคะ 😊
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอเชิญทุกท่านเข้าร่วมกิจกรรมและมาร่วมสร้างประสบการณ์ดี ๆ ไปด้วยกันครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 030. MB-1421-GL-096 - clear_general_double_llm_latency

- **คำถาม:** แปลคำว่า reservation เป็นภาษาไทย ขอสรุปเป็น 2 ข้อ
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['จอง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `13.6918s` / visible LLM `6722.79ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=13.6918s visible_llm=6722.79ms; judge_passed=True judge_errors=[]; answer_body_chars=37; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.2392s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> •    การจอง
> •    การจัดเตรียมล่วงหน้า
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> • การจอง
> • การสำรองล่วงหน้า
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 031. MB-1422-GL-097 - clear_general_double_llm_latency

- **คำถาม:** เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ขอสรุปเป็น 2 ข้อ
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['กิจกรรม']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `15.8931s` / visible LLM `8893.18ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=15.8931s visible_llm=8893.18ms; judge_passed=True judge_errors=[]; answer_body_chars=249; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2302s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอเชิญร่วมกิจกรรมสนุกสนานภายใต้บรรยากาศอบอุ่นใจ เพื่อสร้างความสัมพันธ์ที่ดีและเพิ่มพลังบวกให้กับทุกคนในชุมชนครับ
> •    กิจกรรมนี้เปิดโอกาสให้ทุกคนได้มีส่วนร่วมอย่างสนุกสนานและปลอดภัย
> •    ส่งเสริมความร่วมมือและการแบ่งปันพลังบวกในชุมชนอย่างยั่งยืนครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอเชิญทุกท่านเข้าร่วมกิจกรรมเพื่อ 1) ร่วมสนุก และ 2) สร้างประสบการณ์ดี ๆ ไปด้วยกันครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 032. MB-1431-GL-106 - clear_general_double_llm_latency

- **คำถาม:** แปลคำว่า reservation เป็นภาษาไทย ขอคำตอบไม่เกิน 3 บรรทัด
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['จอง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `15.2029s` / visible LLM `8011.73ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=15.2029s visible_llm=8011.73ms; judge_passed=True judge_errors=[]; answer_body_chars=199; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.2798s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> การจอง การจัดสรรไว้ล่วงหน้า โดยเฉพาะสำหรับบริการหรือสถานที่ใช้งานต่อไปในอนาคต โดยมีข้อตกลงหรือเงื่อนไขแน่นอนแล้วก่อนใช้งานจริง ซึ่งช่วยให้มั่นใจว่าจะได้รับบริการตามที่ต้องการโดยไม่ต้องรอคอยนานเกินไป.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> `reservation` แปลว่า “การจอง” หรือ “การสำรอง” ขึ้นอยู่กับบริบทครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 033. MB-1432-GL-107 - clear_general_double_llm_latency

- **คำถาม:** เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ขอคำตอบไม่เกิน 3 บรรทัด
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['กิจกรรม']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `14.6651s` / visible LLM `7602.48ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=14.6651s visible_llm=7602.48ms; judge_passed=True judge_errors=[]; answer_body_chars=162; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2530s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> เรียนผู้สนใจทุกท่าน ขอเชิญร่วมตื่นเต้นเข้าร่วมงานกิจกรรมพิเศษในวันนี้ได้เลยนะคะ! เสริมพลังความสนุกสนานและสร้างสรรค์ด้วยกิจกรรมที่น่าตื่นเต้นรออยู่ข้างหน้าแล้วล่ะ!
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอเชิญทุกท่านเข้าร่วมกิจกรรมและมาร่วมสร้างประสบการณ์ดี ๆ ไปด้วยกันครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 034. MB-1461-GL-136 - clear_general_double_llm_latency

- **คำถาม:** แปลคำว่า reservation เป็นภาษาไทย ช่วยยกตัวอย่างสั้น ๆ
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['จอง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `14.7691s` / visible LLM `7676.24ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=14.7691s visible_llm=7676.24ms; judge_passed=True judge_errors=[]; answer_body_chars=155; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.3090s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> การจอง
> ตัวอย่าง: การจองที่พักสำหรับวันพรุ่งนี้คือการเลือกสถานที่พักล่วงหน้าเพื่อใช้บริการในอนาคตได้ล่วงหน้าโดยไม่ต้องรอให้เกิดความต้องการขึ้นมาเองอีกครั้ง.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> `reservation` แปลว่า “การจอง” เช่น `room reservation` หมายถึงการจองห้องครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 035. MB-1462-GL-137 - clear_general_double_llm_latency

- **คำถาม:** เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ช่วยยกตัวอย่างสั้น ๆ
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['กิจกรรม']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `13.9892s` / visible LLM `6993.17ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=13.9892s visible_llm=6993.17ms; judge_passed=True judge_errors=[]; answer_body_chars=81; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2401s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอเชิญชวนทุกท่านร่วมเป็นส่วนหนึ่งในกิจกรรมสนุกสนานและสร้างสรรค์ร่วมกันได้เลยนะคะ!
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอเชิญทุกท่านเข้าร่วมกิจกรรมและมาร่วมสร้างประสบการณ์ดี ๆ ไปด้วยกันครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 036. MB-1481-GL-156 - clear_general_double_llm_latency

- **คำถาม:** แปลคำว่า reservation เป็นภาษาไทย ตอบแบบสุภาพ
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s, mixed_gender_particles`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['จอง']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `13.4238s` / visible LLM `6522.23ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=13.4238s visible_llm=6522.23ms; judge_passed=True judge_errors=[]; answer_body_chars=14; quality_flags=['mixed_gender_particles']; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.1978s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น; output flags=mixed_gender_particles
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> การจองครับ/ค่ะ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> `reservation` แปลว่า “การจอง” หรือ “การสำรอง” ขึ้นอยู่กับบริบทครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 037. MB-1482-GL-157 - clear_general_double_llm_latency

- **คำถาม:** เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ตอบแบบสุภาพ
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s, awkward_thai_phrase`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['กิจกรรม']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `14.7619s` / visible LLM `7379.08ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=14.7619s visible_llm=7379.08ms; judge_passed=True judge_errors=[]; answer_body_chars=82; quality_flags=['awkward_thai_phrase']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1826s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น; output flags=awkward_thai_phrase
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอเชิญชวนทุกท่านร่วมตื่นเต้นรับชมกิจกรรมพิเศษที่กำลังจะมาถึงอย่างไม่ต้องรอช้าครับ!
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอเชิญทุกท่านเข้าร่วมกิจกรรมและมาร่วมสร้างประสบการณ์ดี ๆ ไปด้วยกันครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 038. MB-1501-GL-176 - clear_general_double_llm_latency

- **คำถาม:** แปลคำว่า reservation เป็นภาษาไทย เขียนเป็นภาษาไทยธรรมชาติ
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s, mixed_gender_particles`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['จอง']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `13.5997s` / visible LLM `6390.91ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=13.5997s visible_llm=6390.91ms; judge_passed=True judge_errors=[]; answer_body_chars=14; quality_flags=['mixed_gender_particles']; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.2393s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น; output flags=mixed_gender_particles
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> การจองครับ/ค่ะ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> `reservation` แปลว่า “การจอง” หรือ “การสำรอง” ขึ้นอยู่กับบริบทครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 039. MB-1502-GL-177 - clear_general_double_llm_latency

- **คำถาม:** เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค เขียนเป็นภาษาไทยธรรมชาติ
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s, emoji_present`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['กิจกรรม']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `14.1319s` / visible LLM `7085.03ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=14.1319s visible_llm=7085.03ms; judge_passed=True judge_errors=[]; answer_body_chars=79; quality_flags=['emoji_present']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2316s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น; output flags=emoji_present
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> เรียนท่านผู้สนใจ! มีกิจกรรมสนุก ๆ กำลังจะมาถึงแล้ว อย่ารอช้ามาพบกันได้เลยครับ 😊
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอเชิญทุกท่านเข้าร่วมกิจกรรมและมาร่วมสร้างประสบการณ์ดี ๆ ไปด้วยกันครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 040. MB-1511-GL-186 - clear_general_double_llm_latency

- **คำถาม:** แปลคำว่า reservation เป็นภาษาไทย ขอแบบไม่เป็นทางการมาก
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s, mixed_gender_particles`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['จอง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `13.7609s` / visible LLM `6660.71ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=13.7609s visible_llm=6660.71ms; judge_passed=True judge_errors=[]; answer_body_chars=14; quality_flags=['mixed_gender_particles']; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.2351s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น; output flags=mixed_gender_particles
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> การจองครับ/ค่ะ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> `reservation` แปลว่า “การสำรอง” หรือ “การจองล่วงหน้า” ตามบริบทครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 041. MB-1512-GL-187 - clear_general_double_llm_latency

- **คำถาม:** เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ขอแบบไม่เป็นทางการมาก
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s, emoji_present`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['กิจกรรม']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `13.6645s` / visible LLM `6679.94ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=13.6645s visible_llm=6679.94ms; judge_passed=True judge_errors=[]; answer_body_chars=45; quality_flags=['emoji_present']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2300s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น; output flags=emoji_present
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ชวนเพื่อนมาลุยกิจกรรมสนุก ๆ กับเราได้เลยนะ! 😊
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอเรียนเชิญทุกท่านเข้าร่วมกิจกรรมและร่วมสร้างประสบการณ์อันดีไปด้วยกันครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 042. MB-1521-GL-196 - clear_general_double_llm_latency

- **คำถาม:** แปลคำว่า reservation เป็นภาษาไทย ขอแบบเป็นทางการ
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['จอง']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `13.0208s` / visible LLM `6212.74ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=13.0208s visible_llm=6212.74ms; judge_passed=True judge_errors=[]; answer_body_chars=10; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.5012s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> การจองครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> `reservation` แปลว่า “การสำรอง” หรือ “การจองล่วงหน้า” ตามบริบทครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 043. MB-1522-GL-197 - clear_general_double_llm_latency

- **คำถาม:** เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ขอแบบเป็นทางการ
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['กิจกรรม']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `15.4191s` / visible LLM `7939.98ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=15.4191s visible_llm=7939.98ms; judge_passed=True judge_errors=[]; answer_body_chars=142; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.5357s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอเชิญชวนทุกท่านร่วมเข้าร่วมงานกิจกรรมอย่างอบอุ่นใจและเป็นมิตรในวันนี้ครับ เพื่อสร้างความสัมพันธ์ที่ดีขึ้นและแบ่งปันความสนุกสนานไปพร้อมกันครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอเรียนเชิญทุกท่านเข้าร่วมกิจกรรมและร่วมสร้างประสบการณ์อันดีไปด้วยกันครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 044. MB-1531-GL-206 - clear_general_double_llm_latency

- **คำถาม:** แปลคำว่า reservation เป็นภาษาไทย ช่วยสรุปใจความสำคัญ
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['จอง']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `13.2780s` / visible LLM `6249.34ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=13.2780s visible_llm=6249.34ms; judge_passed=True judge_errors=[]; answer_body_chars=10; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.4902s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> การจองครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> `reservation` แปลว่า “การจอง” หรือ “การสำรอง” ขึ้นอยู่กับบริบทครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 045. MB-1532-GL-207 - clear_general_double_llm_latency

- **คำถาม:** เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ช่วยสรุปใจความสำคัญ
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['กิจกรรม']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `14.0921s` / visible LLM `6852.49ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=14.0921s visible_llm=6852.49ms; judge_passed=True judge_errors=[]; answer_body_chars=62; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.4593s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอเชิญทุกท่านร่วมตื่นเต้นเข้าร่วมกิจกรรมพิเศษที่จะมาแรงแน่นอน!
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอเชิญทุกท่านเข้าร่วมกิจกรรมและมาร่วมสร้างประสบการณ์ดี ๆ ไปด้วยกันครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 046. MB-1541-GL-216 - clear_general_double_llm_latency

- **คำถาม:** แปลคำว่า reservation เป็นภาษาไทย ตอบแบบ bullet สั้น ๆ
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['จอง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `14.2934s` / visible LLM `6825.52ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=14.2934s visible_llm=6825.52ms; judge_passed=True judge_errors=[]; answer_body_chars=51; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.4732s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> •    การจอง
> •    การขอรับรอง
> •    การจัดสรรล่วงหน้า
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> • การจอง
> • การสำรองล่วงหน้า
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 047. MB-1542-GL-217 - clear_general_double_llm_latency

- **คำถาม:** เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ตอบแบบ bullet สั้น ๆ
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['กิจกรรม']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `13.7792s` / visible LLM `6702.20ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=13.7792s visible_llm=6702.20ms; judge_passed=True judge_errors=[]; answer_body_chars=53; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.5631s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> •    เตรียมตัวสนุกกับกิจกรรมพิเศษนี้ได้แล้ววันนี้เลย!
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> • ขอเชิญทุกท่านเข้าร่วมกิจกรรมและมาร่วมสร้างประสบการณ์ดี ๆ ไปด้วยกันครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 048. MB-1551-GL-226 - clear_general_double_llm_latency

- **คำถาม:** แปลคำว่า reservation เป็นภาษาไทย ตอบแบบประโยคเดียว
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['จอง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `14.1468s` / visible LLM `6952.36ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=14.1468s visible_llm=6952.36ms; judge_passed=True judge_errors=[]; answer_body_chars=99; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.4475s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> การจองคือการขอรับสิทธิ์หรือสถานที่ใช้งานล่วงหน้าเพื่อความสะดวกในการดำเนินงานตามกำหนดเวลาที่ต้องการ.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> `reservation` แปลว่า “การจอง” หรือ “การสำรอง” ขึ้นอยู่กับบริบทครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 049. MB-1552-GL-227 - clear_general_double_llm_latency

- **คำถาม:** เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ตอบแบบประโยคเดียว
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s, emoji_present`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['กิจกรรม']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `14.3140s` / visible LLM `7264.05ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=14.3140s visible_llm=7264.05ms; judge_passed=True judge_errors=[]; answer_body_chars=77; quality_flags=['emoji_present']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.4205s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น; output flags=emoji_present
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอเชิญทุกท่านร่วมเป็นส่วนหนึ่งในกิจกรรมพิเศษนี้อย่างอบอุ่นใจและสนุกสนานนะคะ 😊
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอเชิญทุกท่านเข้าร่วมกิจกรรมและมาร่วมสร้างประสบการณ์ดี ๆ ไปด้วยกันครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 050. MB-1571-GL-246 - clear_general_double_llm_latency

- **คำถาม:** แปลคำว่า reservation เป็นภาษาไทย ให้คำจำกัดความแบบสั้น
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s, short_request_over_250_chars, body_over_300_chars, obvious_repetition_or_truncation`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['จอง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `18.2820s` / visible LLM `11207.99ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=18.2820s visible_llm=11207.99ms; judge_passed=True judge_errors=[]; answer_body_chars=511; quality_flags=['short_request_over_250_chars', 'body_over_300_chars', 'obvious_repetition_or_truncation']; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.5334s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น; output flags=short_request_over_250_chars, body_over_300_chars, obvious_repetition_or_truncation
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> การจองคิวหรือการขอรับบริการล่วงหน้า โดยมักหมายถึงการจัดสรรทรัพยากรไว้ล่วงหน้าเพื่อใช้งานในอนาคต เช่น การจองห้องพัก โต๊ะอาหาร หรือบริการเฉพาะทางต่าง ๆ เนื่องจากคำว่า reservation มีความหมายหลากหลายขึ้นอยู่กับบริบทที่ใช้ แต่โดยทั่วไปแล้วหมายถึงการยืนยันการใช้งานล่วงหน้าของทรัพยากรใด ๆ โดยไม่ต้องรอให้เกิดเหตุการณ์จริง ๆ เกิดขึ้นก่อน ซึ่งช่วยให้ผู้ใช้งานสามารถวางแผนได้อย่างมีประสิทธิภาพมากยิ่งขึ้น และลดความไม่แน่นอนในการใช้งานทรัพยากรต่าง ๆ ได้อย่างมีระบบและเป็นระเบียบ โดยเฉพาะในสถานการณ์ที่มีความต้องการสูงหรือ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของ...
- **ตัวอย่างคำตอบที่ควรได้:**
> `reservation` แปลว่า “การจอง” หรือ “การสำรอง” ขึ้นอยู่กับบริบทครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 051. MB-1572-GL-247 - clear_general_double_llm_latency

- **คำถาม:** เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ให้คำจำกัดความแบบสั้น
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['กิจกรรม']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `14.5081s` / visible LLM `7225.51ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=14.5081s visible_llm=7225.51ms; judge_passed=True judge_errors=[]; answer_body_chars=78; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.4566s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอเชิญทุกท่านร่วมเป็นส่วนหนึ่งในกิจกรรมสนุกสนานและสร้างสรรค์ร่วมกันได้เลยนะคะ!
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอเชิญทุกท่านเข้าร่วมกิจกรรมและมาร่วมสร้างประสบการณ์ดี ๆ ไปด้วยกันครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 052. MB-1591-GL-266 - clear_general_double_llm_latency

- **คำถาม:** แปลคำว่า reservation เป็นภาษาไทย ตอบแบบไม่ต้องมีตัวอย่างยาว
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['จอง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `13.6080s` / visible LLM `6246.28ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=13.6080s visible_llm=6246.28ms; judge_passed=True judge_errors=[]; answer_body_chars=10; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.4921s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> การจองครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> `reservation` แปลว่า “การจอง” หรือ “การสำรอง” ขึ้นอยู่กับบริบทครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 053. MB-1592-GL-267 - clear_general_double_llm_latency

- **คำถาม:** เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ตอบแบบไม่ต้องมีตัวอย่างยาว
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `clear_general_double_llm_latency, latency_over_10s`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['กิจกรรม']`
- **Actual path:** `general/detail` / `pipeline:general_llm_fallback` / wall `14.6223s` / visible LLM `7584.56ms`
- **จุดแรกที่พลาด:** Universal Intent LLM followed by General LLM
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/detail; wall=14.6223s visible_llm=7584.56ms; judge_passed=True judge_errors=[]; answer_body_chars=111; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.4662s
- **ลำดับเหตุ:** clear translation/generation -> Intent LLM review -> General LLM generation -> เวลาสอง call รวมเกิน SLA แม้คำตอบสั้น
- **Root cause:** translation/promo เป็น clear-general task แต่ operation confidence ต่ำทำให้เรียก Intent LLM ก่อน General LLM; compact trace ซ่อน call แรกในหลายเคส โดย focused trace และ overhead signature ยืนยัน pattern
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general with explicit translation or text_generation operation` ด้วย `one General LLM call with shape-based token budget`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอเชิญทุกท่านร่วมเป็นส่วนหนึ่งในกิจกรรมพิเศษนี้เพื่อสร้างความสนุกสนานและความทรงจำร่วมกันอย่างอบอุ่นและสุภาพนะคะ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอเชิญทุกท่านเข้าร่วมกิจกรรมและมาร่วมสร้างประสบการณ์ดี ๆ ไปด้วยกันครับ
- **วิธีแก้:** เพิ่ม deterministic operation detector สำหรับ translation/generation, skip Intent LLM, max 1 call, token budget 64-96 และ backend deadline 8.5-9 วินาที
- **จุดโค้ด:** `Universal Intent gate; General LLM fallback; request deadline/token budget policy`
- **Regression assertion:** แต่ละ clear-general request ต้องมี actual LLM call <=1, คำตอบตรงรูปแบบ และ wall time <10s
- **ความมั่นใจ/Caveat:** `high_inference_from_focused_trace_and_signature`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 054. MB-1320-C-084 - compound_split_missing_subanswer

- **คำถาม:** VR 30 นาทีกับ VR 1 ชั่วโมงต่างกันยังไง แล้วจองยังไง
- **สถานะ/Priority:** `confirmed_failure_hidden_by_judge` / `P1`
- **อาการทั้งหมด:** `compound_split_missing_subanswer, compound_split_missing_comparison_subanswer`
- **Expected contract:** category=`['multi_question', 'reservation', 'games', 'equipment']`, must contain=`['จอง', 'เลือก', 'บริการ']`
- **Actual path:** `multi_question/multi_question_split` / `pipeline:multi_question_splitter` / wall `4.9485s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** multi-question splitter / dependency planning
- **สิ่งที่พบ:** Typhoon mode=pipeline:multi_question_splitter route=multi_question/multi_question_split; wall=4.9485s visible_llm=0.00ms; judge_passed=True judge_errors=[]; answer_body_chars=852; quality_flags=['compound_split_missing_comparison_subanswer']; No-LLM mode=pipeline:multi_question_splitter passed=True wall=2.6176s
- **ลำดับเหตุ:** comparison+booking -> splitter ทำ compared pair แตกผิด -> child แรกกลายเป็น booking no-answer -> composer รวมคำตอบที่ขาด comparison -> keyword judge ยังผ่าน; output flags=compound_split_missing_comparison_subanswer
- **Root cause:** splitter แบ่งเป็น VR 30 นาทีจองยังไง และ VR 1 ชั่วโมงต่างกันยังไงแล้วจองยังไง ทำให้ comparison 30 vs 60 นาทีหายและคำตอบแรก no-answer แต่ keyword judge ยังผ่าน
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, source_grounding_and_conflict_check, answer_shape_and_language_lint, subquestion_coverage_check`
- **เส้นทางที่ควรเป็น:** `compound: service_fee comparison -> reservation how-to` ด้วย `semantic dependency plan + two structured children + subanswer coverage validation`
- **Source requirement:** app/calculator/service_fee.py verified rates + curated_booking_steps
- **คำตอบจริง:**
> คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:
>
> คำถามที่ 1: VR 30 นาที จองยังไง
> ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ
>
> คำถามที่ 2: VR 1 ชั่วโมงต่างกันยังไง แล้ว จองยังไง
> ระยะเวลาที่ถามคือ 1 ชั่วโมง ใช้ 1 session ตามแพ็กเกจ VR 1 ชั่วโมง
> ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน:
> •    PSU Student and Staff: 0 บาท/session x 1 = 0 บาท
> •    PSU Alumni and General Student / นักศึกษาหรือนักเรียนต่างสถาบัน: 375 บาท/session x 1 = 375 บาท
> •    General Adult / บุคคลทั่วไป: 1050 บาท/sess...
- **ตัวอย่างคำตอบที่ควรได้:**
> VR 30 นาทีและ 1 ชั่วโมงรองรับ 1-5 คนเหมือนกัน ต่างกันที่เวลาและราคา: นักศึกษา/บุคลากร PSU 0 บาททั้งสองแบบ, นักศึกษาต่างสถาบัน 190/375 บาท และบุคคลทั่วไป 525/1,050 บาทตามลำดับครับ
> วิธีจอง: เลือกบริการ VR และแพ็กเกจ เลือกวันเวลา กรอกข้อมูล ตรวจสอบข้อมูล ชำระเงิน และแนบสลิป
> แหล่งข้อมูล: https://esports.computing.psu.ac.th/
- **วิธีแก้:** รักษา compared entities ไว้ใน comparison task, deduplicate booking task และตรวจ expected subanswer slots ก่อน final answer
- **จุดโค้ด:** `split_multi_question; Query Planner schema; compound composer; answer contract coverage`
- **Regression assertion:** คำตอบต้องมีทั้งความต่าง/ราคาของ 30 และ 60 นาที และขั้นตอนจอง โดยไม่มี child no-answer
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 055. MB-1333-GL-008 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `0.8201s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=0.8201s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=825; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=0.6635s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> PC Zone
> •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
> •    Gaming Monitor (จำนวน 10 จอ)
> •    Gaming Chair (จำนวน 10 ตัว)
> •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset
>
> Cockpit Zone
> •    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
> •    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
> •    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
> •    Pulse Elite Wireless Headset (จำนวน 2 อัน)
>
> Nintendo Switch Zone
> •    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
> •    Nintendo Switch OLED (จำนวน 1 เครื่อง)...
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical คือคีย์บอร์ดที่มีสวิตช์แยกใต้แต่ละปุ่ม ทำให้กดแม่น ทน และเลือกสัมผัสหรือเสียงได้หลายแบบครับ
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 056. MB-1343-GL-018 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น ตอบสั้น ๆ
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `0.7393s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=0.7393s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=70; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=0.4844s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical คือคีย์บอร์ดที่มีสวิตช์แยกใต้แต่ละปุ่ม ทำให้กดแม่น ทน และเลือกสัมผัสหรือเสียงได้หลายแบบครับ
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 057. MB-1353-GL-028 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น ขอแบบเข้าใจง่าย
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `0.9568s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=0.9568s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=825; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=0.5399s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> PC Zone
> •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
> •    Gaming Monitor (จำนวน 10 จอ)
> •    Gaming Chair (จำนวน 10 ตัว)
> •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset
>
> Cockpit Zone
> •    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
> •    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
> •    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
> •    Pulse Elite Wireless Headset (จำนวน 2 อัน)
>
> Nintendo Switch Zone
> •    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
> •    Nintendo Switch OLED (จำนวน 1 เครื่อง)...
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical คือคีย์บอร์ดที่มีสวิตช์แยกใต้แต่ละปุ่ม ทำให้กดแม่น ทน และเลือกสัมผัสหรือเสียงได้หลายแบบครับ
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 058. MB-1363-GL-038 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น ตอบเป็นภาษาไทย
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `0.9467s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=0.9467s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=825; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=0.5015s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> PC Zone
> •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
> •    Gaming Monitor (จำนวน 10 จอ)
> •    Gaming Chair (จำนวน 10 ตัว)
> •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset
>
> Cockpit Zone
> •    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
> •    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
> •    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
> •    Pulse Elite Wireless Headset (จำนวน 2 อัน)
>
> Nintendo Switch Zone
> •    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
> •    Nintendo Switch OLED (จำนวน 1 เครื่อง)...
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical คือคีย์บอร์ดที่มีสวิตช์แยกใต้แต่ละปุ่ม ทำให้กดแม่น ทน และเลือกสัมผัสหรือเสียงได้หลายแบบครับ
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 059. MB-1373-GL-048 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น ไม่ต้องยาว
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `0.7867s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=0.7867s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=825; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=0.4313s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> PC Zone
> •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
> •    Gaming Monitor (จำนวน 10 จอ)
> •    Gaming Chair (จำนวน 10 ตัว)
> •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset
>
> Cockpit Zone
> •    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
> •    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
> •    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
> •    Pulse Elite Wireless Headset (จำนวน 2 อัน)
>
> Nintendo Switch Zone
> •    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
> •    Nintendo Switch OLED (จำนวน 1 เครื่อง)...
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical คือคีย์บอร์ดที่มีสวิตช์แยกใต้แต่ละปุ่ม ทำให้กดแม่น ทน และเลือกสัมผัสหรือเสียงได้หลายแบบครับ
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 060. MB-1383-GL-058 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น ขอ 1 ย่อหน้า
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `0.7567s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=0.7567s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=825; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=0.4536s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> PC Zone
> •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
> •    Gaming Monitor (จำนวน 10 จอ)
> •    Gaming Chair (จำนวน 10 ตัว)
> •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset
>
> Cockpit Zone
> •    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
> •    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
> •    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
> •    Pulse Elite Wireless Headset (จำนวน 2 อัน)
>
> Nintendo Switch Zone
> •    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
> •    Nintendo Switch OLED (จำนวน 1 เครื่อง)...
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical คือคีย์บอร์ดที่มีสวิตช์แยกใต้แต่ละปุ่ม ทำให้กดแม่น ทน และเลือกสัมผัสหรือเสียงได้หลายแบบครับ
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 061. MB-1393-GL-068 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น อธิบายให้มือใหม่เข้าใจ
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `1.3139s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=1.3139s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=825; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=0.6937s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> PC Zone
> •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
> •    Gaming Monitor (จำนวน 10 จอ)
> •    Gaming Chair (จำนวน 10 ตัว)
> •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset
>
> Cockpit Zone
> •    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
> •    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
> •    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
> •    Pulse Elite Wireless Headset (จำนวน 2 อัน)
>
> Nintendo Switch Zone
> •    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
> •    Nintendo Switch OLED (จำนวน 1 เครื่อง)...
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical คือคีย์บอร์ดที่มีสวิตช์แยกใต้แต่ละปุ่ม ทำให้กดแม่น ทน และเลือกสัมผัสหรือเสียงได้หลายแบบครับ
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 062. MB-1403-GL-078 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น ตอบแบบเด็กปีหนึ่งเข้าใจได้
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `1.3614s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=1.3614s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=825; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=0.7155s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> PC Zone
> •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
> •    Gaming Monitor (จำนวน 10 จอ)
> •    Gaming Chair (จำนวน 10 ตัว)
> •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset
>
> Cockpit Zone
> •    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
> •    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
> •    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
> •    Pulse Elite Wireless Headset (จำนวน 2 อัน)
>
> Nintendo Switch Zone
> •    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
> •    Nintendo Switch OLED (จำนวน 1 เครื่อง)...
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical คือคีย์บอร์ดที่มีสวิตช์แยกใต้แต่ละปุ่ม ทำให้กดแม่น ทน และเลือกสัมผัสหรือเสียงได้หลายแบบครับ
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 063. MB-1413-GL-088 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น ขอแบบไม่ใช้ศัพท์ยาก
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `1.0396s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=1.0396s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=825; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=0.5674s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> PC Zone
> •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
> •    Gaming Monitor (จำนวน 10 จอ)
> •    Gaming Chair (จำนวน 10 ตัว)
> •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset
>
> Cockpit Zone
> •    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
> •    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
> •    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
> •    Pulse Elite Wireless Headset (จำนวน 2 อัน)
>
> Nintendo Switch Zone
> •    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
> •    Nintendo Switch OLED (จำนวน 1 เครื่อง)...
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical คือคีย์บอร์ดที่มีสวิตช์แยกใต้แต่ละปุ่ม ทำให้กดแม่น ทน และเลือกสัมผัสหรือเสียงได้หลายแบบครับ
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 064. MB-1423-GL-098 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น ขอสรุปเป็น 2 ข้อ
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `0.9791s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=0.9791s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=825; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=0.5217s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> PC Zone
> •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
> •    Gaming Monitor (จำนวน 10 จอ)
> •    Gaming Chair (จำนวน 10 ตัว)
> •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset
>
> Cockpit Zone
> •    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
> •    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
> •    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
> •    Pulse Elite Wireless Headset (จำนวน 2 อัน)
>
> Nintendo Switch Zone
> •    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
> •    Nintendo Switch OLED (จำนวน 1 เครื่อง)...
- **ตัวอย่างคำตอบที่ควรได้:**
> • ใช้สวิตช์แยกใต้แต่ละปุ่ม จึงให้สัมผัสการกดชัดและตอบสนองสม่ำเสมอ
> • มักทนและปรับแต่งได้ แต่ราคาและเสียงอาจสูงกว่าคีย์บอร์ดทั่วไป
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 065. MB-1433-GL-108 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น ขอคำตอบไม่เกิน 3 บรรทัด
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `1.4511s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=1.4511s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=825; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=0.6866s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> PC Zone
> •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
> •    Gaming Monitor (จำนวน 10 จอ)
> •    Gaming Chair (จำนวน 10 ตัว)
> •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset
>
> Cockpit Zone
> •    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
> •    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
> •    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
> •    Pulse Elite Wireless Headset (จำนวน 2 อัน)
>
> Nintendo Switch Zone
> •    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
> •    Nintendo Switch OLED (จำนวน 1 เครื่อง)...
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical คือคีย์บอร์ดที่มีสวิตช์แยกใต้แต่ละปุ่ม ทำให้กดแม่น ทน และเลือกสัมผัสหรือเสียงได้หลายแบบครับ
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 066. MB-1443-GL-118 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น อธิบายแบบใช้ในงาน chatbot
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `1.5369s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=1.5369s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=825; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=0.6641s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> PC Zone
> •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
> •    Gaming Monitor (จำนวน 10 จอ)
> •    Gaming Chair (จำนวน 10 ตัว)
> •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset
>
> Cockpit Zone
> •    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
> •    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
> •    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
> •    Pulse Elite Wireless Headset (จำนวน 2 อัน)
>
> Nintendo Switch Zone
> •    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
> •    Nintendo Switch OLED (จำนวน 1 เครื่อง)...
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical คือคีย์บอร์ดที่มีสวิตช์แยกใต้แต่ละปุ่ม ทำให้กดแม่น ทน และเลือกสัมผัสหรือเสียงได้หลายแบบครับ
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 067. MB-1453-GL-128 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น อธิบายแบบใช้กับวงการเกม
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `1.2596s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=1.2596s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=825; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=0.7898s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> PC Zone
> •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
> •    Gaming Monitor (จำนวน 10 จอ)
> •    Gaming Chair (จำนวน 10 ตัว)
> •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset
>
> Cockpit Zone
> •    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
> •    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
> •    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
> •    Pulse Elite Wireless Headset (จำนวน 2 อัน)
>
> Nintendo Switch Zone
> •    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
> •    Nintendo Switch OLED (จำนวน 1 เครื่อง)...
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical ใช้สวิตช์แยกแต่ละปุ่ม ทำให้กดแม่นและเลือกสัมผัสที่เหมาะกับเกมได้ครับ
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 068. MB-1463-GL-138 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น ช่วยยกตัวอย่างสั้น ๆ
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `1.2114s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=1.2114s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=70; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=0.5569s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical คือคีย์บอร์ดที่มีสวิตช์แยกใต้แต่ละปุ่ม เช่นสวิตช์แบบ linear ที่กดลื่นและเหมาะกับการเล่นเกมครับ
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 069. MB-1473-GL-148 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น เปรียบเทียบแบบสั้น
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `1.1064s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=1.1064s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=825; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=0.5411s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> PC Zone
> •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
> •    Gaming Monitor (จำนวน 10 จอ)
> •    Gaming Chair (จำนวน 10 ตัว)
> •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset
>
> Cockpit Zone
> •    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
> •    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
> •    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
> •    Pulse Elite Wireless Headset (จำนวน 2 อัน)
>
> Nintendo Switch Zone
> •    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
> •    Nintendo Switch OLED (จำนวน 1 เครื่อง)...
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical ใช้สวิตช์แยกทุกปุ่ม จึงกดชัดและทนกว่าแบบ membrane แต่มักแพง หนัก และเสียงดังกว่าครับ
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 070. MB-1483-GL-158 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น ตอบแบบสุภาพ
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `0.8630s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=0.8630s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=825; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=0.4163s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> PC Zone
> •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
> •    Gaming Monitor (จำนวน 10 จอ)
> •    Gaming Chair (จำนวน 10 ตัว)
> •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset
>
> Cockpit Zone
> •    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
> •    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
> •    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
> •    Pulse Elite Wireless Headset (จำนวน 2 อัน)
>
> Nintendo Switch Zone
> •    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
> •    Nintendo Switch OLED (จำนวน 1 เครื่อง)...
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical คือคีย์บอร์ดที่มีสวิตช์แยกใต้แต่ละปุ่ม ทำให้กดแม่น ทน และเลือกสัมผัสหรือเสียงได้หลายแบบครับ
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 071. MB-1493-GL-168 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น ตอบให้เหมาะกับนักศึกษา
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `1.2682s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=1.2682s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=825; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=0.6105s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> PC Zone
> •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
> •    Gaming Monitor (จำนวน 10 จอ)
> •    Gaming Chair (จำนวน 10 ตัว)
> •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset
>
> Cockpit Zone
> •    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
> •    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
> •    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
> •    Pulse Elite Wireless Headset (จำนวน 2 อัน)
>
> Nintendo Switch Zone
> •    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
> •    Nintendo Switch OLED (จำนวน 1 เครื่อง)...
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical คือคีย์บอร์ดที่มีสวิตช์แยกใต้แต่ละปุ่ม ทำให้กดแม่น ทน และเลือกสัมผัสหรือเสียงได้หลายแบบครับ
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 072. MB-1503-GL-178 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น เขียนเป็นภาษาไทยธรรมชาติ
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `1.3403s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=1.3403s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=825; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=0.7144s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> PC Zone
> •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
> •    Gaming Monitor (จำนวน 10 จอ)
> •    Gaming Chair (จำนวน 10 ตัว)
> •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset
>
> Cockpit Zone
> •    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
> •    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
> •    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
> •    Pulse Elite Wireless Headset (จำนวน 2 อัน)
>
> Nintendo Switch Zone
> •    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
> •    Nintendo Switch OLED (จำนวน 1 เครื่อง)...
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical คือคีย์บอร์ดที่มีสวิตช์แยกใต้แต่ละปุ่ม ทำให้กดแม่น ทน และเลือกสัมผัสหรือเสียงได้หลายแบบครับ
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 073. MB-1513-GL-188 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น ขอแบบไม่เป็นทางการมาก
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `1.2804s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=1.2804s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=825; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=0.6427s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> PC Zone
> •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
> •    Gaming Monitor (จำนวน 10 จอ)
> •    Gaming Chair (จำนวน 10 ตัว)
> •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset
>
> Cockpit Zone
> •    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
> •    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
> •    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
> •    Pulse Elite Wireless Headset (จำนวน 2 อัน)
>
> Nintendo Switch Zone
> •    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
> •    Nintendo Switch OLED (จำนวน 1 เครื่อง)...
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical คือคีย์บอร์ดที่มีสวิตช์แยกใต้แต่ละปุ่ม ทำให้กดแม่น ทน และเลือกสัมผัสหรือเสียงได้หลายแบบครับ
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 074. MB-1523-GL-198 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น ขอแบบเป็นทางการ
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `1.0013s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=1.0013s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=825; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=1.1783s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> PC Zone
> •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
> •    Gaming Monitor (จำนวน 10 จอ)
> •    Gaming Chair (จำนวน 10 ตัว)
> •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset
>
> Cockpit Zone
> •    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
> •    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
> •    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
> •    Pulse Elite Wireless Headset (จำนวน 2 อัน)
>
> Nintendo Switch Zone
> •    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
> •    Nintendo Switch OLED (จำนวน 1 เครื่อง)...
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical คือคีย์บอร์ดที่มีสวิตช์แยกใต้แต่ละปุ่ม ทำให้กดแม่น ทน และเลือกสัมผัสหรือเสียงได้หลายแบบครับ
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 075. MB-1533-GL-208 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น ช่วยสรุปใจความสำคัญ
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `1.1354s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=1.1354s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=825; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=1.0592s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> PC Zone
> •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
> •    Gaming Monitor (จำนวน 10 จอ)
> •    Gaming Chair (จำนวน 10 ตัว)
> •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset
>
> Cockpit Zone
> •    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
> •    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
> •    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
> •    Pulse Elite Wireless Headset (จำนวน 2 อัน)
>
> Nintendo Switch Zone
> •    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
> •    Nintendo Switch OLED (จำนวน 1 เครื่อง)...
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical คือคีย์บอร์ดที่มีสวิตช์แยกใต้แต่ละปุ่ม ทำให้กดแม่น ทน และเลือกสัมผัสหรือเสียงได้หลายแบบครับ
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 076. MB-1543-GL-218 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น ตอบแบบ bullet สั้น ๆ
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `1.2312s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=1.2312s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=70; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=1.0444s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home
- **ตัวอย่างคำตอบที่ควรได้:**
> • ใช้สวิตช์แยกใต้แต่ละปุ่ม จึงให้สัมผัสการกดชัดและตอบสนองสม่ำเสมอ
> • มักทนและปรับแต่งได้ แต่ราคาและเสียงอาจสูงกว่าคีย์บอร์ดทั่วไป
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 077. MB-1553-GL-228 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น ตอบแบบประโยคเดียว
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `1.0801s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=1.0801s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=825; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=1.0100s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> PC Zone
> •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
> •    Gaming Monitor (จำนวน 10 จอ)
> •    Gaming Chair (จำนวน 10 ตัว)
> •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset
>
> Cockpit Zone
> •    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
> •    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
> •    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
> •    Pulse Elite Wireless Headset (จำนวน 2 อัน)
>
> Nintendo Switch Zone
> •    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
> •    Nintendo Switch OLED (จำนวน 1 เครื่อง)...
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical คือคีย์บอร์ดที่มีสวิตช์แยกใต้แต่ละปุ่ม ทำให้กดแม่น ทน และเลือกสัมผัสหรือเสียงได้หลายแบบครับ
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 078. MB-1573-GL-248 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น ให้คำจำกัดความแบบสั้น
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `1.1227s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=1.1227s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=825; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=1.1830s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> PC Zone
> •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
> •    Gaming Monitor (จำนวน 10 จอ)
> •    Gaming Chair (จำนวน 10 ตัว)
> •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset
>
> Cockpit Zone
> •    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
> •    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
> •    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
> •    Pulse Elite Wireless Headset (จำนวน 2 อัน)
>
> Nintendo Switch Zone
> •    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
> •    Nintendo Switch OLED (จำนวน 1 เครื่อง)...
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical คือคีย์บอร์ดที่มีสวิตช์แยกใต้แต่ละปุ่ม ทำให้กดแม่น ทน และเลือกสัมผัสหรือเสียงได้หลายแบบครับ
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 079. MB-1583-GL-258 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น อธิบายด้วยคำง่าย ๆ
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `1.0229s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=1.0229s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=825; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=1.0495s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> PC Zone
> •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
> •    Gaming Monitor (จำนวน 10 จอ)
> •    Gaming Chair (จำนวน 10 ตัว)
> •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset
>
> Cockpit Zone
> •    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
> •    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
> •    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
> •    Pulse Elite Wireless Headset (จำนวน 2 อัน)
>
> Nintendo Switch Zone
> •    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
> •    Nintendo Switch OLED (จำนวน 1 เครื่อง)...
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical คือคีย์บอร์ดที่มีสวิตช์แยกใต้แต่ละปุ่ม ทำให้กดแม่น ทน และเลือกสัมผัสหรือเสียงได้หลายแบบครับ
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 080. MB-1593-GL-268 - general_concept_misrouted_to_equipment

- **คำถาม:** คีย์บอร์ด mechanical คืออะไรแบบสั้น ตอบแบบไม่ต้องมีตัวอย่างยาว
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `general_concept_misrouted_to_equipment, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['คีย์บอร์ด', 'mechanical']`
- **Actual path:** `equipment/list` / `pipeline:structured_equipment_catalog` / wall `1.3502s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Question Frame -> equipment precondition
- **สิ่งที่พบ:** Typhoon mode=pipeline:structured_equipment_catalog route=equipment/list; wall=1.3502s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:คีย์บอร์ด|mechanical']; answer_body_chars=825; quality_flags=[]; No-LLM mode=pipeline:structured_equipment_catalog passed=False wall=1.3170s
- **ลำดับเหตุ:** general definition -> Question Frame เห็นคำว่า คีย์บอร์ด -> equipment_lookup -> structured equipment catalog -> ตอบรายการอุปกรณ์ของศูนย์แทนคำจำกัดความ
- **Root cause:** คำว่า คีย์บอร์ด เพียงคำเดียวทำให้ looks_like_equipment_query เป็นจริง แม้คำถามเป็น definition และไม่มี PSU/ศูนย์/รุ่น/จำนวน/โซน context
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query` ด้วย `single-call General LLM; no RAG required`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> อุปกรณ์บนหน้า Home:
> PC Zone
> •    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
> •    Gaming Monitor (จำนวน 10 จอ)
> •    Gaming Chair (จำนวน 10 ตัว)
> •    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset
>
> Cockpit Zone
> •    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
> •    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
> •    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
> •    Pulse Elite Wireless Headset (จำนวน 2 อัน)
>
> Nintendo Switch Zone
> •    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
> •    Nintendo Switch OLED (จำนวน 1 เครื่อง)...
- **ตัวอย่างคำตอบที่ควรได้:**
> คีย์บอร์ด mechanical คือคีย์บอร์ดที่มีสวิตช์แยกใต้แต่ละปุ่ม ทำให้กดแม่น ทน และเลือกสัมผัสหรือเสียงได้หลายแบบครับ
- **วิธีแก้:** ให้ definition/comparison cue ชนะ equipment inventory cue และบังคับ structured equipment ต้องมี PSU/inventory context หรือ inventory operation
- **จุดโค้ด:** `app/pipeline/question_frame.py:_operation_from_question; app/pipeline/tool_preconditions.py:looks_like_equipment_query; app/pipeline/engine.py:operation_route_refine`
- **Regression assertion:** 26 variants ต้องอยู่ general route และคำถาม ศูนย์มีคีย์บอร์ดอะไร ยังต้องเข้า structured equipment
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 081. MB-0240-G-152 - llm_route_regression_and_expensive_fallback

- **คำถาม:** อุปกรณ์ไหนเกมเยอะสุด
- **สถานะ/Priority:** `confirmed_failure` / `P1`
- **อาการทั้งหมด:** `llm_route_regression_and_expensive_fallback, heuristic_judge_failed, latency_over_10s`
- **Expected contract:** category=`games`, must contain=`['เกม', 'Zone', 'TEKKEN', 'Mario', 'Gran Turismo']`
- **Actual path:** `equipment/list` / `pipeline:no_answer` / wall `10.8023s` / visible LLM `0.00ms`
- **จุดแรกที่พลาด:** Universal Intent route override -> operation route repair blocked
- **สิ่งที่พบ:** Typhoon mode=pipeline:no_answer route=equipment/list; wall=10.8023s visible_llm=0.00ms; judge_passed=False judge_errors=['category_mismatch:equipment', 'missing_any:เกม|Zone|TEKKEN|Mario|Gran Turismo']; answer_body_chars=100; quality_flags=[]; No-LLM mode=pipeline:structured_game_zone_ranking passed=True wall=0.3211s
- **ลำดับเหตุ:** deterministic games/rank -> LLM เปลี่ยน equipment/list -> frame ซ่อมกลับไม่ได้ -> structured contract reject -> repeated fuzzy retrieval -> no-answer และเกิน 10s
- **Root cause:** LLM เปลี่ยน games/list ที่ deterministic วิเคราะห์ถูกเป็น equipment/list; Question Frame พบ game_zone_rank แต่ engine ซ่อมเฉพาะ general/unknown/no_answer จากนั้น fallback เรียก fuzzy game matching ซ้ำหลายรอบ
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, source_grounding_and_conflict_check`
- **เส้นทางที่ควรเป็น:** `games/list with operation=game_zone_rank` ด้วย `structured_game_zone_ranking`
- **Source requirement:** Verified PSU game catalog: https://esports.phuket.psu.ac.th/Services/our-games
- **คำตอบจริง:**
> ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด equipment ตอนนี้ครับ
- **ตัวอย่างคำตอบที่ควรได้:**
> ถ้านับจากรายชื่อเกมที่ยืนยันได้ PlayStation 5 Zone และ Nintendo Switch Zone มีเกมมากที่สุดเท่ากันที่ 17 เกมครับ
> • PlayStation 5 Zone: 17 เกม
> • Nintendo Switch Zone: 17 เกม
> • PC Zone: 6 เกม
> • VR Zone: 4 เกม
> • Cockpit Zone: 1 เกม
> แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games
- **วิธีแก้:** ให้ high-confidence operation frame override incompatible route, ให้ deterministic exact operation veto LLM review และ cache game match ต่อ request
- **จุดโค้ด:** `app/pipeline/engine.py:operation_route_refine; Universal Intent arbitration; app/runtime/fast_answer.py:_match_supported_game,answer_equipment`
- **Regression assertion:** LLM-on และ No-LLM ต้องเลือก structured_game_zone_ranking เหมือนกันและจบต่ำกว่า 1 วินาทีหลัง warm state
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 082. MB-0650-ANA-024 - product_scope_and_missing_clarification

- **คำถาม:** ช่วยทำการบ้านคณิตให้หน่อย
- **สถานะ/Priority:** `policy_failure` / `P1`
- **อาการทั้งหมด:** `product_scope_and_missing_clarification, heuristic_judge_failed, latency_over_10s`
- **Expected contract:** category=`['no_answer', 'games', 'general']`, must contain=`['ยังไม่พบ', 'ไม่มี', 'ไม่ได้อยู่', 'ตอบจากข้อมูล']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `11.0166s` / visible LLM `5752.66ms`
- **จุดแรกที่พลาด:** product scope policy and General LLM prompt
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=11.0166s visible_llm=5752.66ms; judge_passed=False judge_errors=['missing_any:ยังไม่พบ|ไม่มี|ไม่ได้อยู่|ตอบจากข้อมูล']; answer_body_chars=155; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.2070s
- **ลำดับเหตุ:** คำขอไม่มีโจทย์ -> ควรถามขอข้อมูล -> PSU-only prompt ครอบการตัดสิน -> model ปฏิเสธทั้งงานแทน clarification
- **Root cause:** ผู้ใช้ยังไม่ได้ส่งโจทย์จริง จึงควรถามกลับ แต่ model ปฏิเสธเพราะ PSU-only ซึ่งขัดกับเป้าหมาย broad assistant ที่ผู้ใช้ระบุล่าสุด
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, source_grounding_and_conflict_check`
- **เส้นทางที่ควรเป็น:** `general/clarification` ด้วย `deterministic clarification; call LLM after receiving the actual problem`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขออภัยครับ แต่ผมไม่สามารถช่วยทำการบ้านคณิตได้ครับ เนื่องจากคำถามนี้ไม่เกี่ยวข้องกับ PSU Esports Studio - Phuket และผมต้องปฏิบัติตามคำสั่งที่ระบุไว้ด้วยครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ได้ครับ ส่งโจทย์คณิตพร้อมสิ่งที่ลองทำมาได้เลย ผมจะช่วยอธิบายวิธีคิดทีละขั้นครับ
- **วิธีแก้:** กำหนด product scope เป็น policy ชัดเจนและแยก missing-input clarification ออกจาก out-of-domain refusal
- **จุดโค้ด:** `Boundary Guard policy; General LLM system prompt; clarification templates`
- **Regression assertion:** ข้อความขอช่วยแต่ไม่มีโจทย์ต้องถามให้ส่งโจทย์ ไม่ปฏิเสธแบบ PSU-only และไม่เริ่มคำนวณจากข้อมูลที่ไม่มี
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 083. MB-1326-GL-001 - single_llm_generation_latency

- **คำถาม:** อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ
- **สถานะ/Priority:** `confirmed_sla_failure` / `P1`
- **อาการทั้งหมด:** `single_llm_generation_latency, latency_over_10s, short_request_over_250_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['latency', 'หน่วง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `13.1525s` / visible LLM `12830.76ms`
- **จุดแรกที่พลาด:** General LLM inference budget
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=13.1525s visible_llm=12830.76ms; judge_passed=True judge_errors=[]; answer_body_chars=277; quality_flags=['short_request_over_250_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2933s
- **ลำดับเหตุ:** general definition -> General LLM call เดียวใช้ generation budgetนาน -> final answer มาหลัง 10s; output flags=short_request_over_250_chars
- **Root cause:** visible General LLM call เดียวใช้เวลาเกือบทั้ง request เช่น latency case ใช้ 12.831 วินาที แสดงว่า generation timeout/output budget ยังสูงกว่า product SLA
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, latency_decomposition_and_overhead_signature, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/detail` ด้วย `one bounded General LLM call or deterministic micro-answer for common definitions`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> Latency คือเวลาที่ใช้ในการตอบสนองหรือประมวลผลข้อมูลจากอุปกรณ์หนึ่งไปยังอีกอุปกรณ์หนึ่ง เช่น เวลาที่ระบบคอมพิวเตอร์ตอบกลับคำสั่งของผู้ใช้หลังจากกดปุ่มใด ๆ โดยมักวัดเป็นไมลลิวินาที (ms) และมีผลต่อประสิทธิภาพการทำงานโดยตรง เช่น เวลาตอบสนองในเกมออนไลน์หรือการเชื่อมต่ออินเทอร์เน็ต.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> Latency คือเวลาหน่วงตั้งแต่ส่งคำสั่งจนระบบตอบสนอง ยิ่งต่ำยิ่งรู้สึกลื่น โดยมักวัดเป็นมิลลิวินาที (ms) ครับ
- **วิธีแก้:** ใช้ shape-based max tokens, stop conditions, 5-7 วินาที model budget และ deterministic fallback ก่อน visible cap
- **จุดโค้ด:** `General LLM client config; output budget selector; request deadline/finalizer`
- **Regression assertion:** คำจำกัดความสั้นต้องจบ <10s และไม่ถูกตัดกลางประโยคเมื่อ model budgetหมด
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 084. MB-1329-GL-004 - general_output_contract_risk

- **คำถาม:** JSON คืออะไร
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['JSON', 'ข้อมูล']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `3.8638s` / visible LLM `3710.89ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=3.8638s visible_llm=3710.89ms; judge_passed=True judge_errors=[]; answer_body_chars=417; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.1518s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> JSON คือ JavaScript Object Notation เป็นรูปแบบข้อมูลที่ใช้ในการแลกเปลี่ยนข้อมูลระหว่างระบบต่าง ๆ โดยเขียนในรูปแบบโครงสร้างข้อมูลที่อ่านง่ายและเขียนง่าย เช่น คู่ค่า (key-value) และ array หรือ object มักใช้ใน API และการจัดเก็บข้อมูลในโปรแกรมต่าง ๆ เพื่อให้สามารถส่งผ่านข้อมูลระหว่างระบบได้อย่างมีประสิทธิภาพและรวดเร็ว โดยไม่ต้องพึ่งพาภาษาโปรแกรมเฉพาะเจาะจง เช่น JavaScript เองก็สามารถอ่านและเขียน JSON ได้โดยตรงแล้วครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> JSON คือรูปแบบข้อความสำหรับเก็บและส่งข้อมูลเป็นคู่ key-value ครับ ข้อดีคืออ่านง่ายและใช้ร่วมกันได้หลายภาษา ส่วนข้อจำกัดคือ syntax ต้องถูกต้องและไม่เหมาะกับข้อมูลไบนารีขนาดใหญ่
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 085. MB-1335-GL-010 - general_output_contract_risk

- **คำถาม:** server กับ client ต่างกันยังไง
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['server', 'client']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `3.5856s` / visible LLM `3318.09ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=3.5856s visible_llm=3318.09ms; judge_passed=True judge_errors=[]; answer_body_chars=323; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1648s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> Server และ Client มีหน้าที่ต่างกันในการสื่อสารระบบเครือข่าย โดย Server เป็นอุปกรณ์ที่ให้บริการหรือจัดเก็บข้อมูลให้ Client ใช้งาน เช่น การให้บริการเว็บไซต์หรือเกมออนไลน์ ในขณะที่ Client เป็นอุปกรณ์ที่เชื่อมต่อกับ Server เพื่อรับข้อมูลหรือใช้งานบริการ เช่น เครื่องคอมพิวเตอร์หรือมือถือที่ผู้ใช้งานเข้าใช้งานระบบต่าง ๆ โดยตรง.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> Server เป็นระบบที่ให้บริการหรือข้อมูล ส่วน client เป็นระบบที่ส่งคำขอและนำผลลัพธ์มาแสดงให้ผู้ใช้ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 086. MB-1339-GL-014 - general_output_contract_risk

- **คำถาม:** JSON คืออะไร ตอบสั้น ๆ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, short_request_over_250_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['JSON', 'ข้อมูล']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `3.1158s` / visible LLM `2865.75ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=3.1158s visible_llm=2865.75ms; judge_passed=True judge_errors=[]; answer_body_chars=252; quality_flags=['short_request_over_250_chars']; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.1376s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=short_request_over_250_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> JSON คือภาษาความรู้ (หรือรูปแบบข้อมูล) ที่ใช้จัดเก็บและแลกเปลี่ยนข้อมูลในรูปแบบโครงสร้างตัวอย่างเช่น ตารางหรือพจนานุกรม โดยใช้เครื่องหมายวงเล็บและเครื่องหมายคำพูด เช่น {} และ [] เพื่อแสดงโครงสร้างข้อมูลได้อย่างชัดเจนและเข้าใจง่ายในระบบคอมพิวเตอร์ต่าง ๆ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> JSON คือรูปแบบข้อความสำหรับเก็บและส่งข้อมูลเป็นคู่ key-value ครับ ข้อดีคืออ่านง่ายและใช้ร่วมกันได้หลายภาษา ส่วนข้อจำกัดคือ syntax ต้องถูกต้องและไม่เหมาะกับข้อมูลไบนารีขนาดใหญ่
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 087. MB-1340-GL-015 - general_output_contract_risk

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ตอบสั้น ๆ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, mixed_gender_particles`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `1.5813s` / visible LLM `1282.87ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=1.5813s visible_llm=1282.87ms; judge_passed=True judge_errors=[]; answer_body_chars=83; quality_flags=['mixed_gender_particles']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1950s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=mixed_gender_particles
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอบคุณสำหรับความช่วยเหลืออย่างยิ่งครับ/ค่ะ
> ขอแสดงความชื่นชมและขอบพระคุณอีกครั้งนะคะ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอบคุณมากครับสำหรับความช่วยเหลือและเวลาที่สละให้ ผมซาบซึ้งและจะนำคำแนะนำไปใช้ให้เกิดประโยชน์ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 088. MB-1350-GL-025 - general_output_contract_risk

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ขอแบบเข้าใจง่าย
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, mixed_gender_particles`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `1.6951s` / visible LLM `1353.89ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=1.6951s visible_llm=1353.89ms; judge_passed=True judge_errors=[]; answer_body_chars=81; quality_flags=['mixed_gender_particles']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1752s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=mixed_gender_particles
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอบคุณมากสำหรับความช่วยเหลือครับ/ค่ะ
> ยินดีเป็นอย่างยิ่งที่ได้ช่วยเหลือคุณครับ/ค่ะ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอบคุณมากครับสำหรับความช่วยเหลือและเวลาที่สละให้ ผมซาบซึ้งและจะนำคำแนะนำไปใช้ให้เกิดประโยชน์ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 089. MB-1365-GL-040 - general_output_contract_risk

- **คำถาม:** server กับ client ต่างกันยังไง ตอบเป็นภาษาไทย
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['server', 'client']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `3.7602s` / visible LLM `3362.76ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=3.7602s visible_llm=3362.76ms; judge_passed=True judge_errors=[]; answer_body_chars=333; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2465s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> Server และ Client เป็นส่วนประกอบของระบบเครือข่ายที่ทำงานร่วมกัน โดย Server เป็นอุปกรณ์ที่ให้บริการหรือจัดเก็บข้อมูลให้ Client ใช้งาน เช่น การให้บริการเว็บไซต์หรือเกมออนไลน์ ในขณะที่ Client เป็นอุปกรณ์ที่ใช้งานบริการจาก Server เช่น เครื่องคอมพิวเตอร์หรือมือถือที่ผู้ใช้งานเชื่อมต่อเข้ามาใช้งานบริการต่าง ๆ โดยตรงกับ Server นั่นเองครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> Server เป็นระบบที่ให้บริการหรือข้อมูล ส่วน client เป็นระบบที่ส่งคำขอและนำผลลัพธ์มาแสดงให้ผู้ใช้ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 090. MB-1370-GL-045 - general_output_contract_risk

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ไม่ต้องยาว
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, mixed_gender_particles`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `1.3605s` / visible LLM `1078.53ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=1.3605s visible_llm=1078.53ms; judge_passed=True judge_errors=[]; answer_body_chars=63; quality_flags=['mixed_gender_particles']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1722s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=mixed_gender_particles
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอบคุณสำหรับความช่วยเหลืออย่างยิ่ง
> ขอแสดงความนับถือเสมอครับ/ค่ะ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอบคุณมากครับสำหรับความช่วยเหลือและเวลาที่สละให้ ผมซาบซึ้งและจะนำคำแนะนำไปใช้ให้เกิดประโยชน์ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 091. MB-1376-GL-051 - general_output_contract_risk

- **คำถาม:** อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ ขอ 1 ย่อหน้า
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, short_request_over_250_chars, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['latency', 'หน่วง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `4.2865s` / visible LLM `3907.68ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=4.2865s visible_llm=3907.68ms; judge_passed=True judge_errors=[]; answer_body_chars=336; quality_flags=['short_request_over_250_chars', 'body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1948s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=short_request_over_250_chars, body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> Latency คือเวลาที่ใช้ในการตอบสนองหรือประมวลผลข้อมูลจากอุปกรณ์หนึ่งไปยังอีกอุปกรณ์หนึ่ง เช่น เวลาที่เกิดขึ้นระหว่างการส่งคำสั่งจากผู้ใช้งานไปยังระบบคอมพิวเตอร์แล้วได้รับผลลัพธ์กลับมา โดยมักวัดเป็นไมลลิวินาที (ms) และมีผลต่อประสิทธิภาพการทำงานของระบบโดยเฉพาะในงานที่ต้องการความเร็วสูง เช่น เกมออนไลน์หรือการเชื่อมต่อเครือข่ายอินเทอร์เน็ต.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> Latency คือเวลาหน่วงตั้งแต่ส่งคำสั่งจนระบบตอบสนอง ยิ่งต่ำยิ่งรู้สึกลื่น โดยมักวัดเป็นมิลลิวินาที (ms) ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 092. MB-1377-GL-052 - general_output_contract_risk

- **คำถาม:** เฟรมเรตกับความละเอียดต่างกันยังไง ขอ 1 ย่อหน้า
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['เฟรม', 'ความละเอียด']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `4.4127s` / visible LLM `4038.68ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=4.4127s visible_llm=4038.68ms; judge_passed=True judge_errors=[]; answer_body_chars=360; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1543s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> เฟรมเรต (Frame Rate) และความละเอียด (Resolution) เป็นคุณสมบัติที่แตกต่างกันโดยเฟรมเรตหมายถึงจำนวนเฟรมที่แสดงผลต่อวินาที เช่น 60 FPS จะแสดงภาพได้ 60 เฟรมต่อวินาที ส่งผลให้การเคลื่อนไหวดูลื่นไหล ในขณะที่ความละเอียดคือขนาดของหน้าจอที่แสดงผล เช่น 1080p, 4K ซึ่งกำหนดขนาดของพิกเซลในภาพ โดยทั้งสองอย่างมีบทบาทสำคัญต่อประสบการณ์การชมหรือเล่นเกมแต่ละอย่างแตกต่างกันไป.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> เฟรมเรตบอกความลื่นของภาพ ส่วนความละเอียดบอกความคมชัดครับ ค่าสูงให้ภาพดีขึ้น แต่ทั้งสองอย่างใช้พลังประมวลผลมากขึ้น จึงต้องปรับให้สมดุลกับเครื่อง
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 093. MB-1378-GL-053 - general_output_contract_risk

- **คำถาม:** API คืออะไร ขอ 1 ย่อหน้า
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['API', 'เชื่อมต่อ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `4.4417s` / visible LLM `4190.15ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=4.4417s visible_llm=4190.15ms; judge_passed=True judge_errors=[]; answer_body_chars=426; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1111s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> API หรือ Application Programming Interface เป็นชุดคำสั่งที่ช่วยให้โปรแกรมต่าง ๆ สามารถสื่อสารและทำงานร่วมกันได้อย่างมีประสิทธิภาพ โดยผู้พัฒนาสามารถใช้ API เพื่อดึงข้อมูลหรือเรียกใช้งานฟังก์ชันจากบริการอื่น ๆ โดยไม่ต้องเข้าใจรายละเอียดภายในการทำงานของบริการนั้น ๆ ได้โดยตรง เช่น การเชื่อมต่อระบบชำระเงินออนไลน์หรือการเข้าถึงข้อมูลจากเว็บไซต์ต่าง ๆ เพื่อนำมาใช้งานในแอปพลิเคชันของตนเองได้อย่างรวดเร็วและมีประสิทธิภาพมากยิ่งขึ้น.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> API คือช่องทางที่โปรแกรมใช้สื่อสารและแลกข้อมูลกันครับ ข้อดีคือเชื่อมระบบได้เป็นมาตรฐาน ส่วนข้อจำกัดคือต้องดูแลสิทธิ์ ความปลอดภัย และความพร้อมใช้งานของบริการ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 094. MB-1379-GL-054 - general_output_contract_risk

- **คำถาม:** JSON คืออะไร ขอ 1 ย่อหน้า
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['JSON', 'ข้อมูล']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `3.4255s` / visible LLM `3200.80ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=3.4255s visible_llm=3200.80ms; judge_passed=True judge_errors=[]; answer_body_chars=315; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.1303s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> JSON หรือ JavaScript Object Notation เป็นรูปแบบข้อมูลที่ใช้ในการแลกเปลี่ยนข้อมูลระหว่างระบบต่าง ๆ โดยเขียนในรูปแบบโครงสร้างข้อมูลที่อ่านง่ายและเข้าใจได้ง่าย เช่น คู่ค่า (key-value) และโครงสร้างลิสต์หรือแผนภาพต้นไม้ ซึ่งสามารถใช้งานได้ทั้งในโปรแกรมคอมพิวเตอร์และเว็บไซต์ต่าง ๆ โดยไม่ต้องพึ่งพาภาษาโปรแกรมเฉพาะเจาะจง.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> JSON คือรูปแบบข้อความสำหรับเก็บและส่งข้อมูลเป็นคู่ key-value ครับ ข้อดีคืออ่านง่ายและใช้ร่วมกันได้หลายภาษา ส่วนข้อจำกัดคือ syntax ต้องถูกต้องและไม่เหมาะกับข้อมูลไบนารีขนาดใหญ่
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 095. MB-1380-GL-055 - general_output_contract_risk

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ขอ 1 ย่อหน้า
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, mixed_gender_particles`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `2.2019s` / visible LLM `1908.62ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=2.2019s visible_llm=1908.62ms; judge_passed=True judge_errors=[]; answer_body_chars=141; quality_flags=['mixed_gender_particles']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1693s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=mixed_gender_particles
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอขอบพระคุณอย่างสุดหัวใจสำหรับความช่วยเหลือและความใส่ใจที่มีต่อผม/ฉันนะคะ
> ขอบคุณอีกครั้งสำหรับโอกาสและเวลาที่ท่านได้ให้มาอย่างแท้จริงครับ/ค่ะ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอบคุณมากครับสำหรับความช่วยเหลือและเวลาที่สละให้ ผมซาบซึ้งและจะนำคำแนะนำไปใช้ให้เกิดประโยชน์ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 096. MB-1384-GL-059 - general_output_contract_risk

- **คำถาม:** GPU คืออะไรแบบเข้าใจง่าย ขอ 1 ย่อหน้า
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['GPU', 'กราฟิก']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `4.6713s` / visible LLM `4323.15ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=4.6713s visible_llm=4323.15ms; judge_passed=True judge_errors=[]; answer_body_chars=437; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1728s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> GPU หรือ Graphics Processing Unit คือ ชิปประมวลผลกราฟิกที่ทำหน้าที่ประมวลผลภาพและข้อมูลกราฟิกต่าง ๆ เช่น การเล่นเกม เล่นวิดีโอออนไลน์ หรือการแสดงผลบนหน้าจอ โดย GPU จะทำงานร่วมกับ CPU เพื่อให้ภาพออกมาได้อย่างราบรื่นและรวดเร็วมากขึ้น โดยเฉพาะในงานที่ต้องใช้กราฟิกซับซ้อน เช่น เล่นเกม 3D หรือสร้างภาพยนตร์ดิจิทัล GPU มีความสามารถในการประมวลผลหลายงานพร้อมกันได้มากกว่า CPU ทำให้มันเหมาะกับงานกราฟิกและเรนเดอร์ภาพสูง ๆ เยอะ ๆ อย่างยิ่งเลยครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> GPU คือหน่วยประมวลผลที่ถนัดงานภาพ วิดีโอ เกม และการคำนวณหลายชุดพร้อมกัน ช่วยให้การแสดงผลกราฟิกลื่นขึ้นครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 097. MB-1385-GL-060 - general_output_contract_risk

- **คำถาม:** server กับ client ต่างกันยังไง ขอ 1 ย่อหน้า
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['server', 'client']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `3.5347s` / visible LLM `3182.92ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=3.5347s visible_llm=3182.92ms; judge_passed=True judge_errors=[]; answer_body_chars=310; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1855s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> Server และ Client เป็นองค์ประกอบหลักของระบบเครือข่าย โดย Server เป็นอุปกรณ์ที่ให้บริการหรือจัดเก็บข้อมูล เช่น เว็บไซต์หรือเกมออนไลน์ ขณะที่ Client เป็นอุปกรณ์ที่เชื่อมต่อเข้ามาใช้งานบริการจาก Server เช่น เครื่องคอมพิวเตอร์หรือมือถือ โดย Client จะส่งคำขอให้ Server และรับข้อมูลหรือผลลัพธ์กลับมาเพื่อใช้งานต่อไป.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> Server เป็นระบบที่ให้บริการหรือข้อมูล ส่วน client เป็นระบบที่ส่งคำขอและนำผลลัพธ์มาแสดงให้ผู้ใช้ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 098. MB-1389-GL-064 - general_output_contract_risk

- **คำถาม:** JSON คืออะไร อธิบายให้มือใหม่เข้าใจ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['JSON', 'ข้อมูล']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `5.0151s` / visible LLM `4579.28ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=5.0151s visible_llm=4579.28ms; judge_passed=True judge_errors=[]; answer_body_chars=453; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.1743s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> JSON คือภาษาเขียนข้อมูลแบบโครงสร้าง (data format) ที่ใช้จัดเก็บและส่งข้อมูลระหว่างโปรแกรมต่าง ๆ โดยเขียนเป็นรูปแบบที่อ่านง่าย เช่น ใช้เครื่องหมายวงเล็บ จุดคอมม่า และคู่วงเล็บเพื่อแสดงค่าต่าง ๆ เช่น ชื่อ-อายุ-ที่อยู่ เป็นต้น โดยมือใหม่สามารถเข้าใจได้ง่าย เพราะคล้ายกับการเขียนข้อมูลในรูปแบบตารางหรือรายการที่เรียบง่ายและเป็นมาตรฐานทั่วไปในโลกไซเบอร์ เช่น เว็บไซต์หรือแอปพลิเคชันต่าง ๆ มักใช้ JSON เพื่อแลกเปลี่ยนข้อมูลระหว่างระบบได้อย่างรวดเร็วและแม่นยำ.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuke...
- **ตัวอย่างคำตอบที่ควรได้:**
> JSON คือรูปแบบข้อความสำหรับเก็บและส่งข้อมูลเป็นคู่ key-value ครับ ข้อดีคืออ่านง่ายและใช้ร่วมกันได้หลายภาษา ส่วนข้อจำกัดคือ syntax ต้องถูกต้องและไม่เหมาะกับข้อมูลไบนารีขนาดใหญ่
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 099. MB-1397-GL-072 - general_output_contract_risk

- **คำถาม:** เฟรมเรตกับความละเอียดต่างกันยังไง ตอบแบบเด็กปีหนึ่งเข้าใจได้
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['เฟรม', 'ความละเอียด']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `4.7314s` / visible LLM `4345.52ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=4.7314s visible_llm=4345.52ms; judge_passed=True judge_errors=[]; answer_body_chars=364; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2317s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> เฟรมเรตคือจำนวนภาพที่จอแสดงผลเปลี่ยนไปทุก ๆ วินาที เช่น 60 เฟรมต่อวินาที ก็แปลว่าเห็นภาพเปลี่ยนไปทุก ๆ หนึ่งในหกสิบวินาที
> ความละเอียดคือขนาดของภาพ เช่น 1080p หมายถึงภาพแบ่งเป็นช่องเล็ก ๆ 1080 แถวแนวนอน และ 1920 แถวแนวตั้ง
>
> สรุปสั้น ๆ เฟรมเรตคือความเร็วของภาพ เปลี่ยนเร็วหรือช้า
> ความละเอียดคือขนาดของภาพใหญ่หรือเล็ก เหมือนเปรียบเทียบกับขนาดของกระดาษที่วาดภาพไว้ครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> เฟรมเรตบอกความลื่นของภาพ ส่วนความละเอียดบอกความคมชัดครับ ค่าสูงให้ภาพดีขึ้น แต่ทั้งสองอย่างใช้พลังประมวลผลมากขึ้น จึงต้องปรับให้สมดุลกับเครื่อง
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 100. MB-1400-GL-075 - general_output_contract_risk

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ตอบแบบเด็กปีหนึ่งเข้าใจได้
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, mixed_gender_particles, emoji_present`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `1.3572s` / visible LLM `962.60ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=1.3572s visible_llm=962.60ms; judge_passed=True judge_errors=[]; answer_body_chars=45; quality_flags=['mixed_gender_particles', 'emoji_present']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1886s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=mixed_gender_particles, emoji_present
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอบคุณมากเลยครับ/ค่ะ
> น่ารักจังเลยนะครับ/ค่ะ 😊
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอบคุณมากครับสำหรับความช่วยเหลือและเวลาที่สละให้ ผมซาบซึ้งและจะนำคำแนะนำไปใช้ให้เกิดประโยชน์ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 101. MB-1420-GL-095 - general_output_contract_risk

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ขอสรุปเป็น 2 ข้อ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, mixed_gender_particles`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `1.7981s` / visible LLM `1442.48ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=1.7981s visible_llm=1442.48ms; judge_passed=True judge_errors=[]; answer_body_chars=98; quality_flags=['mixed_gender_particles']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1617s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=mixed_gender_particles
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> •    ขอบคุณสำหรับความช่วยเหลือและความใส่ใจเสมอ
> •    มีความยินดีที่ได้ร่วมงานกับคุณอย่างมากครับ/ค่ะ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอบคุณมากครับสำหรับความช่วยเหลือและเวลาที่สละให้ ผมซาบซึ้งและจะนำคำแนะนำไปใช้ให้เกิดประโยชน์ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 102. MB-1424-GL-099 - general_output_contract_risk

- **คำถาม:** GPU คืออะไรแบบเข้าใจง่าย ขอสรุปเป็น 2 ข้อ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars, obvious_repetition_or_truncation`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['GPU', 'กราฟิก']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `5.7765s` / visible LLM `5418.84ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=5.7765s visible_llm=5418.84ms; judge_passed=True judge_errors=[]; answer_body_chars=549; quality_flags=['body_over_300_chars', 'obvious_repetition_or_truncation']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1879s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars, obvious_repetition_or_truncation
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> GPU คือ ชิปประมวลผลกราฟิก ใช้แสดงภาพเคลื่อนไหวบนหน้าจอ เช่น เล่นเกมหรือดูวิดีโอได้ดีกว่า CPU โดยมีความเร็วในการประมวลผลภาพสูงกว่า CPU มากในงานกราฟิกเฉพาะทาง เช่น เล่นเกมหรือสร้างภาพเคลื่อนไหวต่าง ๆ ได้ดีกว่า CPU โดยมีความเร็วในการประมวลผลภาพสูงกว่า CPU มากในงานกราฟิกเฉพาะทาง เช่น เล่นเกมหรือสร้างภาพเคลื่อนไหวต่าง ๆ ได้ดีกว่า CPU โดยมีความเร็วในการประมวลผลภาพสูงกว่า CPU มากในงานกราฟกิเฉพาะทาง เช่น เล่นเกมหรือสร้างภาพเคลื่อนไหวต่าง ๆ ได้ดีกว่า CPU โดยมีความเร็วในการประมวลผลภาพสูงกว่า CPU มากในงานกราฟิกเฉพาะทาง เช่น เล่นเกมหรือสร้างภาพเคลื่อนไหวต...
- **ตัวอย่างคำตอบที่ควรได้:**
> • GPU ประมวลผลภาพ วิดีโอ เกม และงานคำนวณหลายชุดพร้อมกัน
> • GPU ที่แรงช่วยให้งานลื่นขึ้น แต่ใช้ไฟ สร้างความร้อน และมีราคาสูงขึ้น
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 103. MB-1426-GL-101 - general_output_contract_risk

- **คำถาม:** อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ ขอคำตอบไม่เกิน 3 บรรทัด
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, short_request_over_250_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['latency', 'หน่วง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `3.3754s` / visible LLM `2944.20ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=3.3754s visible_llm=2944.20ms; judge_passed=True judge_errors=[]; answer_body_chars=251; quality_flags=['short_request_over_250_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2312s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=short_request_over_250_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> Latency คือเวลาที่ใช้ในการตอบสนองระหว่างการส่งคำสั่งและได้รับผลลัพธ์จากระบบคอมพิวเตอร์ โดยมักวัดเป็นช่วงเวลาสั้น ๆ เช่น มิลลิวินาที (ms) ซึ่งส่งผลต่อประสิทธิภาพการทำงานโดยตรงโดยเฉพาะในงานที่ต้องการความเร็วสูง เช่น เกมออนไลน์หรือระบบควบคุมแบบเรียลไทม์.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> Latency คือเวลาหน่วงตั้งแต่ส่งคำสั่งจนระบบตอบสนอง ยิ่งต่ำยิ่งรู้สึกลื่น โดยมักวัดเป็นมิลลิวินาที (ms) ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 104. MB-1430-GL-105 - general_output_contract_risk

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ขอคำตอบไม่เกิน 3 บรรทัด
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, mixed_gender_particles`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `2.0232s` / visible LLM `1574.73ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=2.0232s visible_llm=1574.73ms; judge_passed=True judge_errors=[]; answer_body_chars=121; quality_flags=['mixed_gender_particles']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2143s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=mixed_gender_particles
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอขอบพระคุณอย่างยิ่งสำหรับความช่วยเหลือและความใส่ใจเสมอมา
> ขอบคุณเป็นอย่างยิ่งสำหรับคำแนะนำและโอกาสในการพัฒนาตนเองครับ/ค่ะ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอบคุณมากครับสำหรับความช่วยเหลือและเวลาที่สละให้ ผมซาบซึ้งและจะนำคำแนะนำไปใช้ให้เกิดประโยชน์ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 105. MB-1437-GL-112 - general_output_contract_risk

- **คำถาม:** เฟรมเรตกับความละเอียดต่างกันยังไง อธิบายแบบใช้ในงาน chatbot
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['เฟรม', 'ความละเอียด']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `5.0116s` / visible LLM `4491.34ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=5.0116s visible_llm=4491.34ms; judge_passed=True judge_errors=[]; answer_body_chars=437; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2699s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> เฟรมเรต (Frame Rate) และความละเอียด (Resolution) เป็นคุณสมบัติที่แตกต่างกัน โดยเฟรมเรตหมายถึงจำนวนเฟรมต่อวินาทีที่แสดงผล เช่น 30 FPS หรือ 60 FPS ส่วนความละเอียดคือขนาดของภาพ เช่น 1080p, 4K ซึ่งกำหนดโดยจำนวนพิกเซลในแต่ละมิติ โดยเฟรมเรตส่งผลต่อความลื่นไหลของภาพ ในขณะที่ความละเอียดส่งผลต่อความชัดเจนของภาพ โดยทั้งสองคุณสมบัตินี้มีผลต่อประสบการณ์ผู้ใช้งานในงานแสดงผล เช่น เกมหรือวิดีโอ โดยไม่เกี่ยวข้องโดยตรงกับ PSU Esports Studio - Phuket.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> เฟรมเรตบอกความลื่นของภาพ ส่วนความละเอียดบอกความคมชัดครับ ค่าสูงให้ภาพดีขึ้น แต่ทั้งสองอย่างใช้พลังประมวลผลมากขึ้น จึงต้องปรับให้สมดุลกับเครื่อง
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 106. MB-1438-GL-113 - general_output_contract_risk

- **คำถาม:** API คืออะไร อธิบายแบบใช้ในงาน chatbot
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['API', 'เชื่อมต่อ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `4.7879s` / visible LLM `4448.13ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=4.7879s visible_llm=4448.13ms; judge_passed=True judge_errors=[]; answer_body_chars=470; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1869s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> API คือ Application Programming Interface หรืออินเตอร์เฟซการเขียนโปรแกรมสำหรับแอปพลิเคชัน โดยในงาน chatbot จะใช้ API เพื่อเชื่อมต่อกับระบบภายนอก เช่น ฐานข้อมูล เครื่องมือวิเคราะห์ข้อความ หรือบริการอื่น ๆ เพื่อให้ chatbot สามารถตอบคำถามหรือให้ข้อมูลได้อย่างแม่นยำและทันสมัย โดย API จะส่งคำขอ (request) และรับคำตอบกลับ (response) ในรูปแบบข้อมูลที่เข้าใจง่าย เช่น JSON เพื่อให้ระบบต่าง ๆ สื่อสารกันได้อย่างมีประสิทธิภาพและรวดเร็ว โดยไม่จำเป็นต้องเขียนโค้ดซับซ้อนเองทั้งหมด.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Espor...
- **ตัวอย่างคำตอบที่ควรได้:**
> API คือช่องทางที่โปรแกรมใช้สื่อสารและแลกข้อมูลกันครับ ข้อดีคือเชื่อมระบบได้เป็นมาตรฐาน ส่วนข้อจำกัดคือต้องดูแลสิทธิ์ ความปลอดภัย และความพร้อมใช้งานของบริการ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 107. MB-1439-GL-114 - general_output_contract_risk

- **คำถาม:** JSON คืออะไร อธิบายแบบใช้ในงาน chatbot
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['JSON', 'ข้อมูล']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `3.5734s` / visible LLM `3239.81ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=3.5734s visible_llm=3239.81ms; judge_passed=True judge_errors=[]; answer_body_chars=355; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.1841s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> JSON (JavaScript Object Notation) เป็นรูปแบบข้อมูลที่ใช้ในการส่งข้อมูลระหว่างระบบต่าง ๆ โดยเขียนในรูปแบบโครงสร้างข้อมูล เช่น คู่ค่า (key-value) และสามารถอ่านเข้าใจง่าย โดยในงาน chatbot จะใช้ JSON เพื่อส่งข้อความคำขอและคำตอบระหว่างผู้ใช้กับระบบ เช่น ส่งคำถามไปยัง backend และรับคำตอบกลับมาในรูปแบบ JSON เพื่อประมวลผลต่อไปได้อย่างรวดเร็วและมีประสิทธิภาพครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> JSON คือรูปแบบข้อความสำหรับเก็บและส่งข้อมูลเป็นคู่ key-value ครับ ข้อดีคืออ่านง่ายและใช้ร่วมกันได้หลายภาษา ส่วนข้อจำกัดคือ syntax ต้องถูกต้องและไม่เหมาะกับข้อมูลไบนารีขนาดใหญ่
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 108. MB-1442-GL-117 - general_output_contract_risk

- **คำถาม:** เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค อธิบายแบบใช้ในงาน chatbot
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, emoji_present`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['กิจกรรม']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `2.6450s` / visible LLM `1915.98ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=2.6450s visible_llm=1915.98ms; judge_passed=True judge_errors=[]; answer_body_chars=117; quality_flags=['emoji_present']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.3437s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=emoji_present
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอเชิญทุกท่านร่วมเป็นส่วนหนึ่งในกิจกรรมพิเศษนี้นะคะ เพื่อสร้างความสนุกสนานและเพิ่มพูนประสบการณ์ร่วมกันอย่างอบอุ่นใจ 🌟
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอเชิญทุกท่านเข้าร่วมกิจกรรมและมาร่วมสร้างประสบการณ์ดี ๆ ไปด้วยกันครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 109. MB-1444-GL-119 - general_output_contract_risk

- **คำถาม:** GPU คืออะไรแบบเข้าใจง่าย อธิบายแบบใช้ในงาน chatbot
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['GPU', 'กราฟิก']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `4.2412s` / visible LLM `3723.90ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=4.2412s visible_llm=3723.90ms; judge_passed=True judge_errors=[]; answer_body_chars=331; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2449s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> GPU คือชิปประมวลผลกราฟิกที่ใช้ในการประมวลผลข้อมูลอย่างรวดเร็ว โดยเฉพาะงานที่ต้องการคำนวณจำนวนมาก เช่น การเล่นเกม เล่นวิดีโอ หรือฝึกสอนเครื่องจักรเรียนรู้ใน chatbot เพื่อให้ตอบสนองได้เร็วและแม่นยำขึ้น โดยเฉพาะเมื่อใช้ร่วมกับ CPU เพื่อทำงานร่วมกันได้อย่างมีประสิทธิภาพในงานต่าง ๆ เช่น การสร้างคำตอบในแชทบอทให้รวดเร็วและแม่นยำมากขึ้น.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> GPU คือหน่วยประมวลผลที่ถนัดงานภาพ วิดีโอ เกม และการคำนวณหลายชุดพร้อมกัน ช่วยให้การแสดงผลกราฟิกลื่นขึ้นครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 110. MB-1445-GL-120 - general_output_contract_risk

- **คำถาม:** server กับ client ต่างกันยังไง อธิบายแบบใช้ในงาน chatbot
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['server', 'client']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `4.4940s` / visible LLM `4016.48ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=4.4940s visible_llm=4016.48ms; judge_passed=True judge_errors=[]; answer_body_chars=381; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2472s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> Server และ Client ในระบบแชทบอท มีหน้าที่ต่างกันดังนี้:
> •    Server เป็นเซิร์ฟเวอร์ที่จัดการข้อมูลและประมวลผลคำขอ เช่น ตอบคำถามหรือเก็บข้อมูลผู้ใช้
> •    Client เป็นอุปกรณ์หรือแอปพลิเคชันที่ผู้ใช้งานใช้งานโดยตรง เช่น เครื่องคอมพิวเตอร์หรือมือถือที่ส่งคำขอไปยังเซิร์ฟเวอร์เพื่อรับคำตอบกลับมา
>
> ในแชทบอท Server จะรับคำสั่งจาก Client แล้วประมวลผลและส่งคำตอบกลับไปยัง Client โดยอัตโนมัติ.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> Server เป็นระบบที่ให้บริการหรือข้อมูล ส่วน client เป็นระบบที่ส่งคำขอและนำผลลัพธ์มาแสดงให้ผู้ใช้ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 111. MB-1446-GL-121 - general_output_contract_risk

- **คำถาม:** อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ อธิบายแบบใช้กับวงการเกม
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, short_request_over_250_chars, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['latency', 'หน่วง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `4.4853s` / visible LLM `4030.69ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=4.4853s visible_llm=4030.69ms; judge_passed=True judge_errors=[]; answer_body_chars=378; quality_flags=['short_request_over_250_chars', 'body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2175s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=short_request_over_250_chars, body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> Latency คือเวลาที่ใช้ในการตอบสนองระหว่างการกระทำในเกมกับผลลัพธ์ที่เห็นบนหน้าจอ โดยมักหมายถึงความช้าของระบบ เช่น การกดปุ่มแล้วไม่ได้เห็นการเคลื่อนไหวทันที ส่งผลให้ผู้เล่นรู้สึกว่าเกมตอบสนองช้า ซึ่งสำคัญมากในเกมที่ต้องการความแม่นยำ เช่น FPS เกมแนวการยิงหรือการต่อสู้แบบเรียลไทม์ โดย latency สูงอาจทำให้เกิดความล่าช้าในการเล่น และส่งผลเสียต่อประสิทธิภาพในการแข่งขันได้มากขึ้นไปอีก.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> Latency คือเวลาหน่วงระหว่างกดคำสั่งกับผลที่เกิดในเกม เช่น กดยิงแล้วภาพตอบสนองช้า โดยค่ายิ่งต่ำยิ่งเล่นได้ลื่นครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 112. MB-1447-GL-122 - general_output_contract_risk

- **คำถาม:** เฟรมเรตกับความละเอียดต่างกันยังไง อธิบายแบบใช้กับวงการเกม
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['เฟรม', 'ความละเอียด']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `4.0290s` / visible LLM `3632.73ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=4.0290s visible_llm=3632.73ms; judge_passed=True judge_errors=[]; answer_body_chars=315; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1943s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> เฟรมเรตคือจำนวนเฟรมที่แสดงขึ้นต่อวินาที ส่วนความละเอียดคือขนาดของภาพ เช่น 1080p, 4K โดยเฟรมเรตส่งผลต่อความลื่นไหลในการเล่นเกม ส่วนความละเอียดส่งผลต่อคุณภาพภาพโดยรวม เช่น เล่นเกมที่ต้องการความแม่นยำและลื่นไหลควรเลือกเฟรมเรตสูง เช่น 144fps และความละเอียดเหมาะสม เช่น 1080p เพื่อประสิทธิภาพเครื่องคอมพิวเตอร์ที่ดีขึ้น.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> เฟรมเรตบอกความลื่นของภาพ ส่วนความละเอียดบอกความคมชัดครับ ค่าสูงให้ภาพดีขึ้น แต่ทั้งสองอย่างใช้พลังประมวลผลมากขึ้น จึงต้องปรับให้สมดุลกับเครื่อง
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 113. MB-1448-GL-123 - general_output_contract_risk

- **คำถาม:** API คืออะไร อธิบายแบบใช้กับวงการเกม
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['API', 'เชื่อมต่อ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `4.6037s` / visible LLM `4277.65ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=4.6037s visible_llm=4277.65ms; judge_passed=True judge_errors=[]; answer_body_chars=421; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1792s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> API คือ Application Programming Interface หรืออินเตอร์เฟซการเขียนโปรแกรมแอปพลิเคชัน เป็นช่องทางที่อนุญาตให้แอปพลิเคชันหนึ่งสามารถสื่อสารหรือใช้งานฟีเจอร์จากแอปหรือบริการอื่นได้ โดยในวงการเกม API มักถูกใช้เพื่อเชื่อมโยงระบบต่าง ๆ เช่น การเชื่อมต่อระหว่างเกมกับระบบจัดการผู้เล่น หรือให้ผู้พัฒนาเกมสามารถเข้าถึงข้อมูล เช่น คะแนน เครื่องมือช่วยเหลือ หรือระบบรางวัลได้อย่างรวดเร็วและปลอดภัย โดยไม่ต้องเขียนโค้ดซ้ำ ๆ เองทั้งหมด
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> API คือช่องทางที่โปรแกรมใช้สื่อสารและแลกข้อมูลกันครับ ข้อดีคือเชื่อมระบบได้เป็นมาตรฐาน ส่วนข้อจำกัดคือต้องดูแลสิทธิ์ ความปลอดภัย และความพร้อมใช้งานของบริการ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 114. MB-1454-GL-129 - general_output_contract_risk

- **คำถาม:** GPU คืออะไรแบบเข้าใจง่าย อธิบายแบบใช้กับวงการเกม
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['GPU', 'กราฟิก']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `3.9935s` / visible LLM `3580.02ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=3.9935s visible_llm=3580.02ms; judge_passed=True judge_errors=[]; answer_body_chars=330; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2547s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> GPU คือ “จอภาพ” หรือ “หน่วยประมวลผลกราฟิก” ที่ทำหน้าที่วาดภาพเกมให้เร็วและคมชัด เหมือนเป็นหัวใจสำคัญของเครื่องเล่นเกม เพราะเกมส่วนใหญ่ต้องใช้ภาพเคลื่อนไหวเยอะ ๆ ดังนั้น GPU จะช่วยให้ภาพเกมไหลลื่น ไม่กระเด้งหรือช้าเวลาเล่น โดยเฉพาะเกมแนวแอ็กชันหรือ RPG ที่ต้องการภาพสวย ๆ และตอบสนองเร็วสุด ๆ เหมือนเป็น “หัวใจ” ของเครื่องเล่นเกมค่ะ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> GPU คือส่วนที่ประมวลผลภาพของเกม ยิ่งเหมาะกับงานมากก็ยิ่งช่วยให้ภาพลื่นและตั้งค่ากราฟิกได้สูงขึ้นครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 115. MB-1455-GL-130 - general_output_contract_risk

- **คำถาม:** server กับ client ต่างกันยังไง อธิบายแบบใช้กับวงการเกม
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['server', 'client']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `4.3365s` / visible LLM `3897.42ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=4.3365s visible_llm=3897.42ms; judge_passed=True judge_errors=[]; answer_body_chars=382; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2806s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ในวงการเกม Server และ Client มีหน้าที่ต่างกัน โดย Server เป็นศูนย์กลางที่จัดการข้อมูลและสถานะของเกม เช่น การเคลื่อนไหวของผู้เล่น หรือผลลัพธ์ของเกม ในขณะที่ Client เป็นอุปกรณ์ที่ผู้เล่นใช้เล่นเกม โดยรับข้อมูลจาก Server และแสดงผลลัพธ์ให้เห็น เช่น การเคลื่อนไหวของตัวละครบนหน้าจอ ซึ่งทั้งสองทำงานร่วมกันเพื่อให้เกมดำเนินไปอย่างราบรื่นและสมดุลระหว่างผู้เล่นทุกคนในระบบเกมนั้น ๆ เสมอครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ในเกมออนไลน์ server ดูแลสถานะการแข่งขัน ส่วน client บนเครื่องผู้เล่นส่งคำสั่งและแสดงผลครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 116. MB-1458-GL-133 - general_output_contract_risk

- **คำถาม:** API คืออะไร ช่วยยกตัวอย่างสั้น ๆ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, short_request_over_250_chars, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['API', 'เชื่อมต่อ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `4.1369s` / visible LLM `3825.64ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=4.1369s visible_llm=3825.64ms; judge_passed=True judge_errors=[]; answer_body_chars=384; quality_flags=['short_request_over_250_chars', 'body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2187s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=short_request_over_250_chars, body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> API คือ Application Programming Interface หรืออินเตอร์เฟซการเขียนโปรแกรมแอปพลิเคชัน เป็นช่องทางที่ให้โปรแกรมหนึ่งสามารถสื่อสารหรือแลกเปลี่ยนข้อมูลกับโปรแกรมอีกตัวหนึ่งได้ เช่น การใช้ API จาก Google Maps เพื่อแสดงแผนที่ในแอปพลิเคชันของคุณ โดยตัวอย่างเช่น เมื่อคุณเปิดแอปจองตั๋วเครื่องบิน ระบบอาจใช้ API จากบริษัทผู้ให้บริการตั๋วเพื่อดึงข้อมูลราคาและเวลาเที่ยวบินมาแสดงบนหน้าจอได้ทันที.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> API คือช่องทางที่โปรแกรมใช้สื่อสารและแลกข้อมูลกันครับ ข้อดีคือเชื่อมระบบได้เป็นมาตรฐาน ส่วนข้อจำกัดคือต้องดูแลสิทธิ์ ความปลอดภัย และความพร้อมใช้งานของบริการ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 117. MB-1460-GL-135 - general_output_contract_risk

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ช่วยยกตัวอย่างสั้น ๆ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, mixed_gender_particles`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `1.6868s` / visible LLM `1350.51ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=1.6868s visible_llm=1350.51ms; judge_passed=True judge_errors=[]; answer_body_chars=94; quality_flags=['mixed_gender_particles']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2364s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=mixed_gender_particles
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอบคุณสำหรับความช่วยเหลือและความใส่ใจเสมอครับ/ค่ะ
> ทำให้รู้สึกอบอุ่นใจและประทับใจมากเลยค่ะ/ครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอบคุณมากครับสำหรับความช่วยเหลือและเวลาที่สละให้ ผมซาบซึ้งและจะนำคำแนะนำไปใช้ให้เกิดประโยชน์ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 118. MB-1465-GL-140 - general_output_contract_risk

- **คำถาม:** server กับ client ต่างกันยังไง ช่วยยกตัวอย่างสั้น ๆ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, short_request_over_250_chars, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['server', 'client']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `4.6039s` / visible LLM `4204.60ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=4.6039s visible_llm=4204.60ms; judge_passed=True judge_errors=[]; answer_body_chars=391; quality_flags=['short_request_over_250_chars', 'body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2301s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=short_request_over_250_chars, body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> Server และ Client เปรียบเสมือนผู้ให้บริการและผู้ใช้งานในระบบเครือข่าย
> Server เป็นอุปกรณ์ที่จัดเก็บข้อมูลและให้บริการ เช่น เว็บไซต์หรือเกมออนไลน์
> Client เป็นอุปกรณ์ที่ใช้งานบริการ เช่น เครื่องคอมพิวเตอร์หรือมือถือที่เข้าไปดูเว็บหรือเล่นเกม
>
> ตัวอย่าง: เมื่อคุณเข้าไปดูหน้าเว็บไซต์ หน้าเว็บนั้นอยู่บน Server ส่วนคอมพิวเตอร์ของคุณคือ Client ที่รับข้อมูลจาก Server มาแสดงให้เห็นบนหน้าจอคุณได้ครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> Server เป็นระบบที่ให้บริการหรือข้อมูล ส่วน client เป็นระบบที่ส่งคำขอและนำผลลัพธ์มาแสดงให้ผู้ใช้ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 119. MB-1466-GL-141 - general_output_contract_risk

- **คำถาม:** อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ เปรียบเทียบแบบสั้น
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, short_request_over_250_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['latency', 'หน่วง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `3.5055s` / visible LLM `3037.09ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=3.5055s visible_llm=3037.09ms; judge_passed=True judge_errors=[]; answer_body_chars=273; quality_flags=['short_request_over_250_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2106s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=short_request_over_250_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> Latency คือเวลาที่ใช้ระหว่างการเริ่มต้นและได้รับผลลัพธ์ เช่น เครื่องเริ่มทำงานแล้วรอผลตอบกลับมา ถ้า latency ต่ำ ก็เหมือนกับเดินทางจากบ้านไปทำงานโดยไม่ต้องรอคอยนานเลย ส่วน latency สูง ก็เหมือนต้องรอคอยนานมากกว่าปกติ เช่น เดินทางต้องนั่งรถติดยาวนาน ๆ จนถึงจุดหมายช้ากว่าเดิม.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> Latency คือเวลาหน่วงตั้งแต่ส่งคำสั่งจนระบบตอบสนอง ยิ่งต่ำยิ่งรู้สึกลื่น โดยมักวัดเป็นมิลลิวินาที (ms) ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 120. MB-1467-GL-142 - general_output_contract_risk

- **คำถาม:** เฟรมเรตกับความละเอียดต่างกันยังไง เปรียบเทียบแบบสั้น
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, short_request_over_250_chars, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['เฟรม', 'ความละเอียด']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `3.8203s` / visible LLM `3480.66ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=3.8203s visible_llm=3480.66ms; judge_passed=True judge_errors=[]; answer_body_chars=330; quality_flags=['short_request_over_250_chars', 'body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1690s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=short_request_over_250_chars, body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> เฟรมเรตคือจำนวนเฟรมต่อวินาทีที่แสดงผลบนหน้าจอ ส่วนความละเอียดคือขนาดของภาพ เช่น พิกเซลในแนวนอนและแนวตั้ง โดยความละเอียดส่งผลต่อความชัดเจนของภาพ ในขณะที่เฟรมเรตส่งผลต่อความลื่นไหลของการเคลื่อนไหว เช่น เฟรมเรต 60 FPS จะลื่นกว่า 30 FPS หากความละเอียดเท่ากัน โดยทั้งสองอย่างมีบทบาทร่วมกันในการสร้างภาพที่ดูสมจริงและลื่นไหลบนหน้าจอครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> เฟรมเรตบอกความลื่นของภาพ ส่วนความละเอียดบอกความคมชัดครับ ค่าสูงให้ภาพดีขึ้น แต่ทั้งสองอย่างใช้พลังประมวลผลมากขึ้น จึงต้องปรับให้สมดุลกับเครื่อง
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 121. MB-1469-GL-144 - general_output_contract_risk

- **คำถาม:** JSON คืออะไร เปรียบเทียบแบบสั้น
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, short_request_over_250_chars, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['JSON', 'ข้อมูล']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `3.9575s` / visible LLM `3634.45ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=3.9575s visible_llm=3634.45ms; judge_passed=True judge_errors=[]; answer_body_chars=358; quality_flags=['short_request_over_250_chars', 'body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.1503s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=short_request_over_250_chars, body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> JSON คือภาษาเขียนข้อมูลแบบโครงสร้าง (data format) เหมือนตาราง ใช้แทนข้อมูลในโปรแกรม เช่น เปรียบเทียบกับฟอร์แมตข้อความที่เข้าใจง่าย เช่น ข้อความธรรมดา แต่จัดเรียงเป็นคู่ค่าได้ชัดเจน เช่น ชื่อ-อายุ หรือ รายการสินค้า-ราคา โดยไม่ต้องใช้โค้ดซับซ้อนเหมือนภาษาโปรแกรมเต็มรูปแบบ เช่น Python หรือ Java เหมือนกับการเขียนแบบกระดาษส่งข้อมูลให้คนอื่นอ่านง่าย ๆ โดยตรงครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> JSON คือรูปแบบข้อความสำหรับเก็บและส่งข้อมูลเป็นคู่ key-value ครับ ข้อดีคืออ่านง่ายและใช้ร่วมกันได้หลายภาษา ส่วนข้อจำกัดคือ syntax ต้องถูกต้องและไม่เหมาะกับข้อมูลไบนารีขนาดใหญ่
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 122. MB-1474-GL-149 - general_output_contract_risk

- **คำถาม:** GPU คืออะไรแบบเข้าใจง่าย เปรียบเทียบแบบสั้น
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, short_request_over_250_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['GPU', 'กราฟิก']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `3.3931s` / visible LLM `3019.41ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=3.3931s visible_llm=3019.41ms; judge_passed=True judge_errors=[]; answer_body_chars=269; quality_flags=['short_request_over_250_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1931s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=short_request_over_250_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> GPU คือ “จอภาพ” หรือ “หน่วยประมวลผลกราฟิก” ที่ทำหน้าที่วาดภาพและเคลื่อนไหวให้เร็วขึ้น เช่น เล่นเกมหรือดูวิดีโอได้ไหลลื่น ส่วน CPU (หน่วยประมวลผลกลาง) จะเป็น “สมอง” ควบคุมการทำงานทั้งระบบโดยรวม โดย GPU เหมือนช่างภาพวาดภาพให้เร็ว ส่วน CPU เหมือนผู้จัดการวางแผนทั้งหมดครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> GPU คือหน่วยประมวลผลที่ถนัดงานภาพ วิดีโอ เกม และการคำนวณหลายชุดพร้อมกัน ช่วยให้การแสดงผลกราฟิกลื่นขึ้นครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 123. MB-1476-GL-151 - general_output_contract_risk

- **คำถาม:** อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ ตอบแบบสุภาพ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, short_request_over_250_chars, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['latency', 'หน่วง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `4.4926s` / visible LLM `4131.84ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=4.4926s visible_llm=4131.84ms; judge_passed=True judge_errors=[]; answer_body_chars=374; quality_flags=['short_request_over_250_chars', 'body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2233s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=short_request_over_250_chars, body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> Latency คือเวลาที่ใช้ในการตอบสนองหรือประมวลผลข้อมูลจากเหตุการณ์หนึ่งไปยังอีกเหตุการณ์หนึ่งในระบบคอมพิวเตอร์ เช่น เวลาที่จอภาพตอบสนองหลังจากกดปุ่มใด ๆ หรือเวลาที่ข้อมูลถูกส่งผ่านเครือข่ายแล้วได้รับคำตอบกลับมาต่อจากเซิร์ฟเวอร์ โดยมักวัดเป็นไมลลิวินาที (ms) และมีผลต่อประสิทธิภาพการทำงานโดยตรง เช่น ในเกมออนไลน์ latency สูงอาจทำให้การเคลื่อนไหวดูช้าหรือล่าช้าจากความจริงได้ครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> Latency คือเวลาหน่วงตั้งแต่ส่งคำสั่งจนระบบตอบสนอง ยิ่งต่ำยิ่งรู้สึกลื่น โดยมักวัดเป็นมิลลิวินาที (ms) ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 124. MB-1485-GL-160 - general_output_contract_risk

- **คำถาม:** server กับ client ต่างกันยังไง ตอบแบบสุภาพ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['server', 'client']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `5.4348s` / visible LLM `5081.02ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=5.4348s visible_llm=5081.02ms; judge_passed=True judge_errors=[]; answer_body_chars=534; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1850s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> Server และ Client เป็นองค์ประกอบหลักของระบบเครือข่าย โดย Server เป็นอุปกรณ์ที่ให้บริการหรือจัดเก็บข้อมูลให้แก่ Client ซึ่งเป็นอุปกรณ์ที่เชื่อมต่อเข้ามาใช้งานบริการนั้น ๆ เช่น การเข้าถึงเว็บไซต์ การเล่นเกมออนไลน์ เป็นต้น โดย Server จะรับคำขอจาก Client และตอบกลับข้อมูลหรือบริการตามที่ต้องการไปยัง Client อย่างไรก็ตาม ความแตกต่างนี้อาจเปลี่ยนแปลงไปตามบริบทของระบบ เช่น ในระบบเกมออนไลน์ Server มักทำหน้าที่ควบคุมสถานะเกมและส่งข้อมูลให้ผู้เล่นทุกคนในเวลาจริง ส่วน Client จะแสดงผลลัพธ์และรับคำสั่งจากผู้ใช้งานเพื่อส่งไปยัง Server ต่อไปครับ
> หมายเหตุ: คำตอบ...
- **ตัวอย่างคำตอบที่ควรได้:**
> Server เป็นระบบที่ให้บริการหรือข้อมูล ส่วน client เป็นระบบที่ส่งคำขอและนำผลลัพธ์มาแสดงให้ผู้ใช้ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 125. MB-1488-GL-163 - general_output_contract_risk

- **คำถาม:** API คืออะไร ตอบให้เหมาะกับนักศึกษา
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['API', 'เชื่อมต่อ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `3.6122s` / visible LLM `3288.33ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=3.6122s visible_llm=3288.33ms; judge_passed=True judge_errors=[]; answer_body_chars=340; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1624s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> API คือ Application Programming Interface หรืออินเตอร์เฟซการเขียนโปรแกรมแอปพลิเคชัน เป็นช่องทางที่ช่วยให้โปรแกรมต่าง ๆ สื่อสารและทำงานร่วมกันได้อย่างราบรื่น โดยนักศึกษาสามารถใช้ API เพื่อดึงข้อมูลหรือส่งคำขอไปยังระบบอื่น ๆ เช่น เว็บไซต์หรือแอปพลิเคชันต่าง ๆ ได้ง่ายขึ้น เช่น การเชื่อมต่อกับ Google Maps เพื่อแสดงแผนที่ในโปรเจกต์ของตนเองครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> API คือช่องทางที่โปรแกรมใช้สื่อสารและแลกข้อมูลกันครับ ข้อดีคือเชื่อมระบบได้เป็นมาตรฐาน ส่วนข้อจำกัดคือต้องดูแลสิทธิ์ ความปลอดภัย และความพร้อมใช้งานของบริการ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 126. MB-1489-GL-164 - general_output_contract_risk

- **คำถาม:** JSON คืออะไร ตอบให้เหมาะกับนักศึกษา
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['JSON', 'ข้อมูล']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `3.6776s` / visible LLM `3366.58ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=3.6776s visible_llm=3366.58ms; judge_passed=True judge_errors=[]; answer_body_chars=318; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.1589s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> JSON คือภาษาเขียนข้อมูลแบบโครงสร้าง (data format) ที่ใช้จัดเก็บและส่งข้อมูลระหว่างโปรแกรมต่าง ๆ เช่น เขียนข้อมูลในรูปแบบชื่อ-ค่า เช่น {"ชื่อ":"นักศึกษา","อายุ":20} เพื่อให้ง่ายต่อการอ่านและประมวลผล โดยนักศึกษาสามารถใช้ JSON ได้ในวิชาคอมพิวเตอร์หรือโปรเจกต์ต่าง ๆ เช่น เขียนโปรแกรมเว็บไซต์หรือแอปพลิเคชันได้ง่ายขึ้นครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> JSON คือรูปแบบข้อความสำหรับเก็บและส่งข้อมูลเป็นคู่ key-value ครับ ข้อดีคืออ่านง่ายและใช้ร่วมกันได้หลายภาษา ส่วนข้อจำกัดคือ syntax ต้องถูกต้องและไม่เหมาะกับข้อมูลไบนารีขนาดใหญ่
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 127. MB-1491-GL-166 - general_output_contract_risk

- **คำถาม:** แปลคำว่า reservation เป็นภาษาไทย ตอบให้เหมาะกับนักศึกษา
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, mixed_gender_particles`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['จอง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `1.0316s` / visible LLM `568.39ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=1.0316s visible_llm=568.39ms; judge_passed=True judge_errors=[]; answer_body_chars=14; quality_flags=['mixed_gender_particles']; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.2345s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=mixed_gender_particles
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> การจองครับ/ค่ะ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> `reservation` แปลว่า “การจอง” หรือ “การสำรอง” ขึ้นอยู่กับบริบทครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 128. MB-1494-GL-169 - general_output_contract_risk

- **คำถาม:** GPU คืออะไรแบบเข้าใจง่าย ตอบให้เหมาะกับนักศึกษา
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, emoji_present`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['GPU', 'กราฟิก']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `3.1773s` / visible LLM `2767.37ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=3.1773s visible_llm=2767.37ms; judge_passed=True judge_errors=[]; answer_body_chars=224; quality_flags=['emoji_present']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2047s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=emoji_present
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> GPU คือ “จอภาพ” หรือ “หน่วยประมวลผลกราฟิก” ที่ช่วยให้คอมพิวเตอร์วาดภาพสวย ๆ เช่น เล่นเกม ดูวิดีโอ หรือใช้งานโปรแกรมกราฟิกได้ไหลลื่น โดยเฉพาะเกมที่ต้องการภาพคมชัดและเคลื่อนไหวเร็วมาก ๆ ก็จะต้องใช้ GPU มาช่วยให้แรงขึ้นนะครับ 😊
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> GPU คือหน่วยประมวลผลที่ถนัดงานภาพ วิดีโอ เกม และการคำนวณหลายชุดพร้อมกัน ช่วยให้การแสดงผลกราฟิกลื่นขึ้นครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 129. MB-1496-GL-171 - general_output_contract_risk

- **คำถาม:** อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ เขียนเป็นภาษาไทยธรรมชาติ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, short_request_over_250_chars, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['latency', 'หน่วง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `4.2240s` / visible LLM `3692.37ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=4.2240s visible_llm=3692.37ms; judge_passed=True judge_errors=[]; answer_body_chars=312; quality_flags=['short_request_over_250_chars', 'body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2200s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=short_request_over_250_chars, body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ความล่าช้า (latency) คือเวลาที่ใช้ในการตอบสนองระหว่างการส่งคำสั่งจากเครื่องคอมพิวเตอร์ไปยังระบบหรืออุปกรณ์ปลายทาง และรอผลตอบกลับมาอีกครั้ง เช่น เครื่องมือเล่นเกมหรือการเชื่อมต่ออินเทอร์เน็ต โดยมักวัดเป็นไมลิวินาที (ms) ยิ่งต่ำยิ่งดี เพราะแสดงถึงความเร็วในการทำงานของระบบคอมพิวเตอร์และเครือข่ายได้ดีขึ้นเท่าไรครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> Latency คือเวลาหน่วงตั้งแต่ส่งคำสั่งจนระบบตอบสนอง ยิ่งต่ำยิ่งรู้สึกลื่น โดยมักวัดเป็นมิลลิวินาที (ms) ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 130. MB-1500-GL-175 - general_output_contract_risk

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค เขียนเป็นภาษาไทยธรรมชาติ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, mixed_gender_particles`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `1.7905s` / visible LLM `1381.32ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=1.7905s visible_llm=1381.32ms; judge_passed=True judge_errors=[]; answer_body_chars=79; quality_flags=['mixed_gender_particles']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2035s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=mixed_gender_particles
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอบคุณมากที่ช่วยเหลือเสมอครับ/ค่ะ
> ยินดีเป็นอย่างยิ่งที่ได้ร่วมงานกับคุณครับ/ค่ะ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอบคุณมากครับสำหรับความช่วยเหลือและเวลาที่สละให้ ผมซาบซึ้งและจะนำคำแนะนำไปใช้ให้เกิดประโยชน์ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 131. MB-1510-GL-185 - general_output_contract_risk

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ขอแบบไม่เป็นทางการมาก
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, emoji_present`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `1.7267s` / visible LLM `1323.71ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=1.7267s visible_llm=1323.71ms; judge_passed=True judge_errors=[]; answer_body_chars=74; quality_flags=['emoji_present']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1938s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=emoji_present
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอบคุณมากเลยนะคะ ที่ช่วยเหลือให้หน่อยนะ
> รู้สึกดีใจที่ได้พูดคุยกับคุณนะคะ 😊
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอขอบพระคุณสำหรับความช่วยเหลือและเวลาที่กรุณาสละให้ครับ ผมซาบซึ้งและจะนำคำแนะนำไปใช้ให้เกิดประโยชน์ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 132. MB-1517-GL-192 - general_output_contract_risk

- **คำถาม:** เฟรมเรตกับความละเอียดต่างกันยังไง ขอแบบเป็นทางการ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['เฟรม', 'ความละเอียด']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `4.5462s` / visible LLM `4151.94ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=4.5462s visible_llm=4151.94ms; judge_passed=True judge_errors=[]; answer_body_chars=370; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1847s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> เฟรมเรต (Frame Rate) และความละเอียด (Resolution) เป็นคุณสมบัติที่แตกต่างกันในการแสดงผลภาพ โดยเฟรมเรตหมายถึงจำนวนเฟรมที่แสดงออกมาในหนึ่งวินาที ซึ่งส่งผลต่อความลื่นไหลของภาพ เช่น 60 FPS หมายถึงแสดงภาพได้ 60 เฟรมต่อวินาที ในขณะที่ความละเอียดหมายถึงจำนวนพิกเซลในแต่ละจอ เช่น 1920x1080 (Full HD) หรือ 4K โดยทั้งสองคุณสมบัตินี้มีผลต่อประสบการณ์การใช้งานภาพอย่างอิสระกันได้ครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> เฟรมเรตบอกความลื่นของภาพ ส่วนความละเอียดบอกความคมชัดครับ ค่าสูงให้ภาพดีขึ้น แต่ทั้งสองอย่างใช้พลังประมวลผลมากขึ้น จึงต้องปรับให้สมดุลกับเครื่อง
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 133. MB-1518-GL-193 - general_output_contract_risk

- **คำถาม:** API คืออะไร ขอแบบเป็นทางการ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['API', 'เชื่อมต่อ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `5.6064s` / visible LLM `5335.58ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=5.6064s visible_llm=5335.58ms; judge_passed=True judge_errors=[]; answer_body_chars=527; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2030s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> API หรือ Application Programming Interface เป็นชุดของกฎเกณฑ์และมาตรฐานที่กำหนดวิธีการให้โปรแกรมต่าง ๆ สื่อสารกันอย่างมีระบบ โดยอนุญาตให้แอปพลิเคชันหนึ่งสามารถใช้งานฟังก์ชันหรือข้อมูลจากแอปพลิเคชันอื่นได้อย่างปลอดภัยและมีประสิทธิภาพ โดยทั่วไปแล้ว API จะช่วยให้การพัฒนาซอฟต์แวร์ทำได้ง่ายขึ้นและรวดเร็วขึ้น รวมถึงสามารถเชื่อมโยงระบบต่าง ๆ เข้าด้วยกันได้อย่างมีประสิทธิภาพ เช่น การเชื่อมต่อระหว่างเว็บไซต์กับฐานข้อมูลหรือบริการภายนอกต่าง ๆ เพื่อให้สามารถใช้งานข้อมูลและฟังก์ชันต่าง ๆ ได้อย่างราบรื่นและรวดเร็ว โดยไม่จำเป็นต้องพัฒนา
> หมายเหตุ: คำตอบนี้เป็น...
- **ตัวอย่างคำตอบที่ควรได้:**
> API คือช่องทางที่โปรแกรมใช้สื่อสารและแลกข้อมูลกันครับ ข้อดีคือเชื่อมระบบได้เป็นมาตรฐาน ส่วนข้อจำกัดคือต้องดูแลสิทธิ์ ความปลอดภัย และความพร้อมใช้งานของบริการ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 134. MB-1519-GL-194 - general_output_contract_risk

- **คำถาม:** JSON คืออะไร ขอแบบเป็นทางการ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['JSON', 'ข้อมูล']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `4.2778s` / visible LLM `4002.71ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=4.2778s visible_llm=4002.71ms; judge_passed=True judge_errors=[]; answer_body_chars=387; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.3149s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> JSON (JavaScript Object Notation) เป็นรูปแบบข้อมูลที่ใช้ในการแลกเปลี่ยนข้อมูลระหว่างระบบต่าง ๆ โดยเขียนในรูปแบบโครงสร้างข้อมูลที่อ่านง่ายและสามารถประมวลผลได้ง่าย เช่น คู่วงเล็บ หรือสตริงที่มีค่าตัวแปรประกอบอยู่ภายใน โดยมักใช้ในงานพัฒนาเว็บไซต์หรือแอปพลิเคชันต่าง ๆ เพื่อส่งและรับข้อมูลระหว่างเซิร์ฟเวอร์กับไคลเอนต์ได้อย่างมีประสิทธิภาพ และเป็นมาตรฐานที่ยอมรับกันอย่างกว้างขวางในปัจจุบัน.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> JSON คือรูปแบบข้อความสำหรับเก็บและส่งข้อมูลเป็นคู่ key-value ครับ ข้อดีคืออ่านง่ายและใช้ร่วมกันได้หลายภาษา ส่วนข้อจำกัดคือ syntax ต้องถูกต้องและไม่เหมาะกับข้อมูลไบนารีขนาดใหญ่
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 135. MB-1520-GL-195 - general_output_contract_risk

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ขอแบบเป็นทางการ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, mixed_gender_particles`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `2.1796s` / visible LLM `1826.30ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=2.1796s visible_llm=1826.30ms; judge_passed=True judge_errors=[]; answer_body_chars=147; quality_flags=['mixed_gender_particles']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.3980s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=mixed_gender_particles
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอแสดงความชื่นชมและขอบพระคุณอย่างยิ่งสำหรับความร่วมมือและความใส่ใจในการสนับสนุน
> กราบขอบคุณอย่างสุดหัวใจสำหรับโอกาสและโอกาสในการทำงานร่วมกันครับ/ค่ะ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอขอบพระคุณสำหรับความช่วยเหลือและเวลาที่กรุณาสละให้ครับ ผมซาบซึ้งและจะนำคำแนะนำไปใช้ให้เกิดประโยชน์ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 136. MB-1524-GL-199 - general_output_contract_risk

- **คำถาม:** GPU คืออะไรแบบเข้าใจง่าย ขอแบบเป็นทางการ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['GPU', 'กราฟิก']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `4.6148s` / visible LLM `4218.11ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=4.6148s visible_llm=4218.11ms; judge_passed=True judge_errors=[]; answer_body_chars=425; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.3845s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> GPU หรือ Graphics Processing Unit เป็นชิปประมวลผลกราฟิกที่ใช้จัดการงานแสดงผลภาพ เช่น การวาดภาพบนหน้าจอคอมพิวเตอร์หรือสมาร์ตโฟน โดยสามารถประมวลผลข้อมูลจำนวนมากพร้อมกันได้อย่างมีประสิทธิภาพ ทำให้เหมาะสำหรับงานที่ต้องใช้กราฟิกสูง เช่น เล่นเกม สร้างภาพยนตร์ หรือเรียนรู้ปัญญาประดิษฐ์ (AI) โดยเฉพาะอย่างยิ่งในงานด้านวิศวกรรมคอมพิวเตอร์และเทคโนโลยีสารสนเทศที่เกี่ยวข้องกับการประมวลผลภาพและข้อมูลขนาดใหญ่ได้อย่างมีประสิทธิภาพสูงสุด.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> GPU คือหน่วยประมวลผลที่ถนัดงานภาพ วิดีโอ เกม และการคำนวณหลายชุดพร้อมกัน ช่วยให้การแสดงผลกราฟิกลื่นขึ้นครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 137. MB-1525-GL-200 - general_output_contract_risk

- **คำถาม:** server กับ client ต่างกันยังไง ขอแบบเป็นทางการ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['server', 'client']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `5.7829s` / visible LLM `5378.28ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=5.7829s visible_llm=5378.28ms; judge_passed=True judge_errors=[]; answer_body_chars=557; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.3794s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> Server และ Client เป็นองค์ประกอบหลักในระบบเครือข่ายที่ทำงานร่วมกัน โดย Server เป็นอุปกรณ์ที่ให้บริการหรือจัดเก็บข้อมูลให้แก่ Client ซึ่งเป็นอุปกรณ์ที่เชื่อมต่อเข้ามาใช้งานบริการจาก Server เช่น การเข้าถึงเว็บไซต์ การเล่นเกมออนไลน์ หรือการส่งรับข้อมูลต่าง ๆ โดย Server จะรับคำขอจาก Client และตอบสนองกลับไปอย่างเหมาะสมตามนโยบายการทำงานของระบบ เทียบเท่ากับศูนย์กลางบริการในเครือข่ายที่จัดการและควบคุมทรัพยากรให้แก่ผู้ใช้งานต่าง ๆ ขณะที่ Client เป็นผู้ใช้งานปลายทางที่เชื่อมต่อเข้ามาเพื่อขอข้อมูลหรือบริการจาก Server โดยมีหน้าที่รับคำสั่งและแสดงผลลัพธ์ให้...
- **ตัวอย่างคำตอบที่ควรได้:**
> Server เป็นระบบที่ให้บริการหรือข้อมูล ส่วน client เป็นระบบที่ส่งคำขอและนำผลลัพธ์มาแสดงให้ผู้ใช้ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 138. MB-1528-GL-203 - general_output_contract_risk

- **คำถาม:** API คืออะไร ช่วยสรุปใจความสำคัญ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['API', 'เชื่อมต่อ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `3.6777s` / visible LLM `3371.25ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=3.6777s visible_llm=3371.25ms; judge_passed=True judge_errors=[]; answer_body_chars=347; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.3079s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> API คือ Application Programming Interface หรืออินเตอร์เฟซการเขียนโปรแกรมแอปพลิเคชัน เป็นช่องทางที่อนุญาตให้โปรแกรมหนึ่งสามารถสื่อสารและแลกเปลี่ยนข้อมูลกับโปรแกรมอีกโปรแกรมหนึ่งได้อย่างมีประสิทธิภาพ โดยไม่ต้องเข้าใจรายละเอียดการทำงานภายในของแต่ละโปรแกรม เช่น การใช้ API เพื่อดึงข้อมูลจากเว็บไซต์มาแสดงผลในแอปพลิเคชันต่าง ๆ ได้อย่างรวดเร็วและแม่นยำ.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> API คือช่องทางที่โปรแกรมใช้สื่อสารและแลกข้อมูลกันครับ ข้อดีคือเชื่อมระบบได้เป็นมาตรฐาน ส่วนข้อจำกัดคือต้องดูแลสิทธิ์ ความปลอดภัย และความพร้อมใช้งานของบริการ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 139. MB-1529-GL-204 - general_output_contract_risk

- **คำถาม:** JSON คืออะไร ช่วยสรุปใจความสำคัญ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['JSON', 'ข้อมูล']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `4.0340s` / visible LLM `3732.87ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=4.0340s visible_llm=3732.87ms; judge_passed=True judge_errors=[]; answer_body_chars=404; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.2938s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> JSON หรือ JavaScript Object Notation เป็นรูปแบบข้อมูลที่ใช้ในการแลกเปลี่ยนข้อมูลระหว่างระบบต่าง ๆ โดยเขียนในรูปแบบโครงสร้างข้อมูลที่อ่านง่ายและเข้าใจได้ง่าย เช่น คู่ค่า (key-value) และสามารถใช้งานร่วมกับภาษาโปรแกรมหลายภาษาได้ โดยเน้นความเรียบง่าย มีโครงสร้างชัดเจน และรองรับการอ่านเขียนข้อมูลได้อย่างรวดเร็ว โดยใจความสำคัญคือ เป็นมาตรฐานสำหรับแลกเปลี่ยนข้อมูลในระบบต่าง ๆ อย่างมีประสิทธิภาพและเข้าใจง่าย.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> JSON คือรูปแบบข้อความสำหรับเก็บและส่งข้อมูลเป็นคู่ key-value ครับ ข้อดีคืออ่านง่ายและใช้ร่วมกันได้หลายภาษา ส่วนข้อจำกัดคือ syntax ต้องถูกต้องและไม่เหมาะกับข้อมูลไบนารีขนาดใหญ่
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 140. MB-1530-GL-205 - general_output_contract_risk

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ช่วยสรุปใจความสำคัญ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, mixed_gender_particles`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `1.9173s` / visible LLM `1553.71ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=1.9173s visible_llm=1553.71ms; judge_passed=True judge_errors=[]; answer_body_chars=114; quality_flags=['mixed_gender_particles']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.3332s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=mixed_gender_particles
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอขอบพระคุณอย่างสุดหัวใจสำหรับความช่วยเหลือและโอกาสที่ได้รับ
> ขอบคุณจริง ๆ สำหรับความใส่ใจและความเข้าใจเสมอครับ/ค่ะ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอบคุณมากครับสำหรับความช่วยเหลือและเวลาที่สละให้ ผมซาบซึ้งและจะนำคำแนะนำไปใช้ให้เกิดประโยชน์ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 141. MB-1535-GL-210 - general_output_contract_risk

- **คำถาม:** server กับ client ต่างกันยังไง ช่วยสรุปใจความสำคัญ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['server', 'client']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `3.7152s` / visible LLM `3224.01ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=3.7152s visible_llm=3224.01ms; judge_passed=True judge_errors=[]; answer_body_chars=304; quality_flags=['body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.4476s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> Server และ Client แตกต่างกันในระบบเครือข่าย โดย Server เป็นอุปกรณ์ที่ให้บริการหรือจัดเก็บข้อมูล เช่น เว็บไซต์หรือเกมออนไลน์ ในขณะที่ Client เป็นอุปกรณ์ที่ใช้งานบริการจาก Server เช่น เครื่องคอมพิวเตอร์หรือมือถือที่ผู้ใช้เข้ามาใช้งาน โดย Server รับคำขอจาก Client และตอบสนองกลับไปให้ได้ผลลัพธ์ตามที่ต้องการ.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> Server เป็นระบบที่ให้บริการหรือข้อมูล ส่วน client เป็นระบบที่ส่งคำขอและนำผลลัพธ์มาแสดงให้ผู้ใช้ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 142. MB-1538-GL-213 - general_output_contract_risk

- **คำถาม:** API คืออะไร ตอบแบบ bullet สั้น ๆ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, short_request_over_250_chars, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['API', 'เชื่อมต่อ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `3.5253s` / visible LLM `3244.49ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=3.5253s visible_llm=3244.49ms; judge_passed=True judge_errors=[]; answer_body_chars=319; quality_flags=['short_request_over_250_chars', 'body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.3071s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=short_request_over_250_chars, body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> •    API คือ Application Programming Interface
> •    เป็นช่องทางที่โปรแกรมต่าง ๆ สามารถสื่อสารและแลกเปลี่ยนข้อมูลได้
> •    เหมือน "ตัวกลาง" ที่ช่วยให้ซอฟต์แวร์ต่าง ๆ ทำงานร่วมกันได้โดยไม่ต้องเขียนโค้ดซ้ำ ๆ
> •    มักใช้ในการเชื่อมต่อระบบต่าง ๆ เช่น เว็บไซต์กับฐานข้อมูล หรือแอปพลิเคชันต่าง ๆ ได้อย่างรวดเร็วและมีประสิทธิภาพ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> • API คือช่องทางที่ให้โปรแกรมสองระบบส่งคำขอและแลกข้อมูลกัน
> • ข้อดีคือเชื่อมระบบได้เป็นมาตรฐาน ส่วนข้อจำกัดคือต้องจัดการสิทธิ์ ความปลอดภัย และกรณี API ล่ม
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 143. MB-1539-GL-214 - general_output_contract_risk

- **คำถาม:** JSON คืออะไร ตอบแบบ bullet สั้น ๆ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, short_request_over_250_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['JSON', 'ข้อมูล']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `2.6824s` / visible LLM `2421.84ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=2.6824s visible_llm=2421.84ms; judge_passed=True judge_errors=[]; answer_body_chars=254; quality_flags=['short_request_over_250_chars']; No-LLM mode=pipeline:general_llm_disabled passed=True wall=0.2912s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=short_request_over_250_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> •    JSON = JavaScript Object Notation
> •    เป็นรูปแบบข้อมูลที่ใช้จัดเก็บและแลกเปลี่ยนข้อมูลระหว่างระบบต่าง ๆ
> •    เขียนง่าย อ่านง่าย และเข้าใจง่าย
> •    ใช้ในเว็บไซต์และแอปพลิเคชันหลายประเภท
> •    ประกอบด้วย key-value และ array แบบโครงสร้างข้อมูลที่ชัดเจน
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> • JSON คือรูปแบบข้อความสำหรับเก็บและส่งข้อมูลเป็นคู่ key-value
> • ข้อดีคืออ่านง่ายและใช้ได้หลายภาษา ส่วนข้อจำกัดคือ syntax ต้องถูกต้องและไม่เหมาะกับข้อมูลไบนารีขนาดใหญ่
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 144. MB-1540-GL-215 - general_output_contract_risk

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ตอบแบบ bullet สั้น ๆ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, mixed_gender_particles`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `2.1147s` / visible LLM `1546.57ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=2.1147s visible_llm=1546.57ms; judge_passed=True judge_errors=[]; answer_body_chars=90; quality_flags=['mixed_gender_particles']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.4750s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=mixed_gender_particles
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> •    ขอบคุณสำหรับความช่วยเหลืออย่างยิ่ง
> •    ยินดีเป็นอย่างยิ่งที่ได้ร่วมงานกับคุณครับ/ค่ะ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอบคุณมากครับสำหรับความช่วยเหลือและเวลาที่สละให้ ผมซาบซึ้งและจะนำคำแนะนำไปใช้ให้เกิดประโยชน์ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 145. MB-1556-GL-231 - general_output_contract_risk

- **คำถาม:** อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ อธิบายข้อดีข้อเสียสั้น ๆ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, short_request_over_250_chars, body_over_300_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['latency', 'หน่วง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `4.3840s` / visible LLM `3917.14ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=4.3840s visible_llm=3917.14ms; judge_passed=True judge_errors=[]; answer_body_chars=341; quality_flags=['short_request_over_250_chars', 'body_over_300_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.4252s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=short_request_over_250_chars, body_over_300_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> Latency คือเวลาที่ใช้ในการตอบสนองต่อคำขอหรือสัญญาณจากอุปกรณ์หนึ่งไปยังอีกอุปกรณ์หนึ่งในระบบคอมพิวเตอร์ เช่น เวลาที่จอภาพแสดงผลหลังจากกดปุ่ม
>
> ข้อดี: เพิ่มความเร็วในการตอบสนอง เช่น การเล่นเกมหรือใช้งานอินเทอร์เน็ตแบบเรียลไทม์
> ข้อเสีย: latency สูงอาจทำให้เกิดความล่าช้า หรือข้อมูลผิดพลาดในระบบสำคัญ เช่น การสื่อสารออนไลน์หรือระบบควบคุมอัตโนมัติ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> Latency คือเวลาหน่วงของระบบครับ ข้อดีของ latency ต่ำคือการตอบสนองไว ส่วน latency สูงทำให้รู้สึกหน่วงและควบคุมได้ช้าลง
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 146. MB-1567-GL-242 - general_output_contract_risk

- **คำถาม:** เฟรมเรตกับความละเอียดต่างกันยังไง ให้คำจำกัดความแบบสั้น
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, short_request_over_250_chars`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['เฟรม', 'ความละเอียด']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `3.4268s` / visible LLM `2987.73ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=3.4268s visible_llm=2987.73ms; judge_passed=True judge_errors=[]; answer_body_chars=258; quality_flags=['short_request_over_250_chars']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.3700s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=short_request_over_250_chars
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> เฟรมเรตคือจำนวนเฟรมต่อวินาทีที่แสดงผลบนหน้าจอ ส่วนความละเอียดคือขนาดของภาพในหน่วยพิกเซล (เช่น 1920x1080) โดยทั้งสองอย่างมีบทบาทในการกำหนดคุณภาพการแสดงผลเกมหรือวิดีโอต่าง ๆ เฟรมเรตส่งผลต่อความลื่นไหลของภาพ ในขณะที่ความละเอียดส่งผลต่อความชัดเจนของภาพโดยรวมครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> เฟรมเรตบอกความลื่นของภาพ ส่วนความละเอียดบอกความคมชัดครับ ค่าสูงให้ภาพดีขึ้น แต่ทั้งสองอย่างใช้พลังประมวลผลมากขึ้น จึงต้องปรับให้สมดุลกับเครื่อง
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 147. MB-1570-GL-245 - general_output_contract_risk

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ให้คำจำกัดความแบบสั้น
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, mixed_gender_particles`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `1.5085s` / visible LLM `1171.11ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=1.5085s visible_llm=1171.11ms; judge_passed=True judge_errors=[]; answer_body_chars=70; quality_flags=['mixed_gender_particles']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.3408s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=mixed_gender_particles
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอบคุณสำหรับความช่วยเหลืออย่างยิ่ง
> ขอแสดงความนับถืออย่างสูงสุดครับ/ค่ะ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอบคุณมากครับสำหรับความช่วยเหลือและเวลาที่สละให้ ผมซาบซึ้งและจะนำคำแนะนำไปใช้ให้เกิดประโยชน์ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 148. MB-1590-GL-265 - general_output_contract_risk

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ตอบแบบไม่ต้องมีตัวอย่างยาว
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, mixed_gender_particles`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `1.9238s` / visible LLM `1519.83ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=1.9238s visible_llm=1519.83ms; judge_passed=True judge_errors=[]; answer_body_chars=107; quality_flags=['mixed_gender_particles']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.3842s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=mixed_gender_particles
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอขอบพระคุณเป็นอย่างยิ่งสำหรับความช่วยเหลือและความใส่ใจ
> ขอบคุณครับ/ค่ะ ที่ให้โอกาสและสนับสนุนเสมอมาครับ/ค่ะ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอบคุณมากครับสำหรับความช่วยเหลือและเวลาที่สละให้ ผมซาบซึ้งและจะนำคำแนะนำไปใช้ให้เกิดประโยชน์ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 149. MB-1600-GL-275 - general_output_contract_risk

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ขอแบบใช้พูดกับผู้ใช้บริการ
- **สถานะ/Priority:** `passed_but_quality_risk` / `P2`
- **อาการทั้งหมด:** `general_output_contract_risk, mixed_gender_particles`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `2.2919s` / visible LLM `1905.57ms`
- **จุดแรกที่พลาด:** General LLM generation -> answer contract/validation
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=2.2919s visible_llm=1905.57ms; judge_passed=True judge_errors=[]; answer_body_chars=130; quality_flags=['mixed_gender_particles']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.3813s
- **ลำดับเหตุ:** general route ถูก -> model สร้างคำตอบ -> validator ตรวจเนื้อหาหลักแต่ shape/style constraints ไม่ครบ -> judge ผ่านแม้ output ไม่เหมาะ; output flags=mixed_gender_particles
- **Root cause:** คำตอบผ่าน keyword judge แต่ไม่รักษารูปแบบที่ผู้ใช้ขอ เช่นยาวเกินไป คำลงท้ายผสม emoji วลีไม่ธรรมชาติ การซ้ำ หรือตัดกลางประโยค
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general route เดิม` ด้วย `one General LLM call + explicit output-shape contract + deterministic post-validation`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอบคุณที่ให้ความร่วมมือและสนับสนุนอย่างเต็มที่นะคะ
> ยินดีช่วยเหลือเสมอครับ/ค่ะ หากมีอะไรเพิ่มเติมต้องการสอบถามก็แจ้งได้นะคะครับ/ค่ะ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอบคุณมากครับสำหรับความช่วยเหลือและเวลาที่สละให้ ผมซาบซึ้งและจะนำคำแนะนำไปใช้ให้เกิดประโยชน์ครับ
- **วิธีแก้:** parse requested shape, จำกัด sentence/bullet/length, เลือกคำลงท้ายเดียว, ปิด emoji, ตรวจ repetition/truncation และ bounded repair ไม่เกินหนึ่งครั้ง
- **จุดโค้ด:** `General LLM prompt; Answer Contract; validator; bounded repair/final hard veto`
- **Regression assertion:** ตรวจจำนวนข้อ/ประโยค/ความยาว, ไม่มีครับ/ค่ะ, ไม่มี emoji โดย default และคำตอบต้องจบสมบูรณ์
- **ความมั่นใจ/Caveat:** `medium_to_high_based_on_output_lint`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 150. MB-1330-GL-005 - heuristic_judge_false_negative

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค
- **สถานะ/Priority:** `evaluator_false_negative` / `P2`
- **อาการทั้งหมด:** `heuristic_judge_false_negative, heuristic_judge_failed, awkward_thai_phrase`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `1.6625s` / visible LLM `1420.03ms`
- **จุดแรกที่พลาด:** benchmark heuristic judge
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=1.6625s visible_llm=1420.03ms; judge_passed=False judge_errors=['missing_any:ขอบคุณ']; answer_body_chars=100; quality_flags=['awkward_thai_phrase']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2378s
- **ลำดับเหตุ:** คำตอบมีความหมายถูก -> ใช้รูปคำ/คำพ้องต่างจาก must_contain_any -> exact substring judge ตัดไม่ผ่าน; output flags=awkward_thai_phrase
- **Root cause:** judge ใช้ exact substring จึงไม่ยอมรับรูปคำหรือคำพ้อง เช่น ขอขอบพระคุณ/ขอบใจ แทน ขอบคุณ และ ความล่าช้า/เวลาตอบสนอง แทน latency/หน่วง
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query (current route mostly correct)` ด้วย `single-call General LLM + semantic evaluator`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอขอบพระคุณเป็นอย่างยิ่งสำหรับความใส่ใจและความช่วยเหลือเสมอครับ
> ยังไงก็รู้สึกขอบใจและประทับใจมากครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอบคุณมากครับสำหรับความช่วยเหลือและเวลาที่สละให้ ผมซาบซึ้งและจะนำคำแนะนำไปใช้ให้เกิดประโยชน์ครับ
- **วิธีแก้:** normalize Thai morphology, เพิ่ม synonym sets และตรวจ semantic operation/answer shape แยกจาก exact keyword
- **จุดโค้ด:** `tools/run_model_benchmark_eval.py judge; eval case contracts; semantic audit layer`
- **Regression assertion:** คำพ้องที่ความหมายถูกต้องต้องผ่าน แต่คำตอบคนละเรื่องที่มี keyword กว้างต้องไม่ผ่าน
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 151. MB-1336-GL-011 - heuristic_judge_false_negative

- **คำถาม:** อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ ตอบสั้น ๆ
- **สถานะ/Priority:** `evaluator_false_negative` / `P2`
- **อาการทั้งหมด:** `heuristic_judge_false_negative, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['latency', 'หน่วง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `2.1049s` / visible LLM `1731.56ms`
- **จุดแรกที่พลาด:** benchmark heuristic judge
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=2.1049s visible_llm=1731.56ms; judge_passed=False judge_errors=['missing_any:latency|หน่วง']; answer_body_chars=138; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2263s
- **ลำดับเหตุ:** คำตอบมีความหมายถูก -> ใช้รูปคำ/คำพ้องต่างจาก must_contain_any -> exact substring judge ตัดไม่ผ่าน
- **Root cause:** judge ใช้ exact substring จึงไม่ยอมรับรูปคำหรือคำพ้อง เช่น ขอขอบพระคุณ/ขอบใจ แทน ขอบคุณ และ ความล่าช้า/เวลาตอบสนอง แทน latency/หน่วง
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query (current route mostly correct)` ด้วย `single-call General LLM + semantic evaluator`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ความล่าช้าในการตอบสนองของระบบคอมพิวเตอร์ระหว่างการส่งข้อมูลจากผู้ใช้ไปยังอุปกรณ์หรือโปรแกรมปลายทาง โดยมักวัดเป็นเวลา เช่น มิลลิวินาที (ms)
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> Latency คือเวลาหน่วงตั้งแต่ส่งคำสั่งจนระบบตอบสนอง ยิ่งต่ำยิ่งรู้สึกลื่น โดยมักวัดเป็นมิลลิวินาที (ms) ครับ
- **วิธีแก้:** normalize Thai morphology, เพิ่ม synonym sets และตรวจ semantic operation/answer shape แยกจาก exact keyword
- **จุดโค้ด:** `tools/run_model_benchmark_eval.py judge; eval case contracts; semantic audit layer`
- **Regression assertion:** คำพ้องที่ความหมายถูกต้องต้องผ่าน แต่คำตอบคนละเรื่องที่มี keyword กว้างต้องไม่ผ่าน
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 152. MB-1360-GL-035 - heuristic_judge_false_negative

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ตอบเป็นภาษาไทย
- **สถานะ/Priority:** `evaluator_false_negative` / `P2`
- **อาการทั้งหมด:** `heuristic_judge_false_negative, heuristic_judge_failed, mixed_gender_particles`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `1.8521s` / visible LLM `1514.45ms`
- **จุดแรกที่พลาด:** benchmark heuristic judge
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=1.8521s visible_llm=1514.45ms; judge_passed=False judge_errors=['missing_any:ขอบคุณ']; answer_body_chars=108; quality_flags=['mixed_gender_particles']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1634s
- **ลำดับเหตุ:** คำตอบมีความหมายถูก -> ใช้รูปคำ/คำพ้องต่างจาก must_contain_any -> exact substring judge ตัดไม่ผ่าน; output flags=mixed_gender_particles
- **Root cause:** judge ใช้ exact substring จึงไม่ยอมรับรูปคำหรือคำพ้อง เช่น ขอขอบพระคุณ/ขอบใจ แทน ขอบคุณ และ ความล่าช้า/เวลาตอบสนอง แทน latency/หน่วง
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query (current route mostly correct)` ด้วย `single-call General LLM + semantic evaluator`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอขอบพระคุณอย่างสุดหัวใจสำหรับความช่วยเหลือและความใส่ใจเสมอมา
> ยังคงรู้สึกซาบซึ้งและประทับใจอย่างยิ่งครับ/ค่ะ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอบคุณมากครับสำหรับความช่วยเหลือและเวลาที่สละให้ ผมซาบซึ้งและจะนำคำแนะนำไปใช้ให้เกิดประโยชน์ครับ
- **วิธีแก้:** normalize Thai morphology, เพิ่ม synonym sets และตรวจ semantic operation/answer shape แยกจาก exact keyword
- **จุดโค้ด:** `tools/run_model_benchmark_eval.py judge; eval case contracts; semantic audit layer`
- **Regression assertion:** คำพ้องที่ความหมายถูกต้องต้องผ่าน แต่คำตอบคนละเรื่องที่มี keyword กว้างต้องไม่ผ่าน
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 153. MB-1390-GL-065 - heuristic_judge_false_negative

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค อธิบายให้มือใหม่เข้าใจ
- **สถานะ/Priority:** `evaluator_false_negative` / `P2`
- **อาการทั้งหมด:** `heuristic_judge_false_negative, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `2.1198s` / visible LLM `1747.00ms`
- **จุดแรกที่พลาด:** benchmark heuristic judge
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=2.1198s visible_llm=1747.00ms; judge_passed=False judge_errors=['missing_any:ขอบคุณ']; answer_body_chars=123; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1806s
- **ลำดับเหตุ:** คำตอบมีความหมายถูก -> ใช้รูปคำ/คำพ้องต่างจาก must_contain_any -> exact substring judge ตัดไม่ผ่าน
- **Root cause:** judge ใช้ exact substring จึงไม่ยอมรับรูปคำหรือคำพ้อง เช่น ขอขอบพระคุณ/ขอบใจ แทน ขอบคุณ และ ความล่าช้า/เวลาตอบสนอง แทน latency/หน่วง
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query (current route mostly correct)` ด้วย `single-call General LLM + semantic evaluator`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอขอบพระคุณเป็นอย่างยิ่งสำหรับความช่วยเหลือและคำแนะนำที่ให้มาครับ
> ขอบใจที่ได้แบ่งปันความรู้ดี ๆ ไว้ให้คนอื่นได้เรียนรู้ครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอบคุณมากครับสำหรับความช่วยเหลือและเวลาที่สละให้ ผมซาบซึ้งและจะนำคำแนะนำไปใช้ให้เกิดประโยชน์ครับ
- **วิธีแก้:** normalize Thai morphology, เพิ่ม synonym sets และตรวจ semantic operation/answer shape แยกจาก exact keyword
- **จุดโค้ด:** `tools/run_model_benchmark_eval.py judge; eval case contracts; semantic audit layer`
- **Regression assertion:** คำพ้องที่ความหมายถูกต้องต้องผ่าน แต่คำตอบคนละเรื่องที่มี keyword กว้างต้องไม่ผ่าน
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 154. MB-1406-GL-081 - heuristic_judge_false_negative

- **คำถาม:** อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ ขอแบบไม่ใช้ศัพท์ยาก
- **สถานะ/Priority:** `evaluator_false_negative` / `P2`
- **อาการทั้งหมด:** `heuristic_judge_false_negative, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['latency', 'หน่วง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `2.5556s` / visible LLM `2152.97ms`
- **จุดแรกที่พลาด:** benchmark heuristic judge
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=2.5556s visible_llm=2152.97ms; judge_passed=False judge_errors=['missing_any:latency|หน่วง']; answer_body_chars=168; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2395s
- **ลำดับเหตุ:** คำตอบมีความหมายถูก -> ใช้รูปคำ/คำพ้องต่างจาก must_contain_any -> exact substring judge ตัดไม่ผ่าน
- **Root cause:** judge ใช้ exact substring จึงไม่ยอมรับรูปคำหรือคำพ้อง เช่น ขอขอบพระคุณ/ขอบใจ แทน ขอบคุณ และ ความล่าช้า/เวลาตอบสนอง แทน latency/หน่วง
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query (current route mostly correct)` ด้วย `single-call General LLM + semantic evaluator`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ความล่าช้าในการตอบสนองของระบบ เช่น เครื่องคอมพิวเตอร์หรืออินเทอร์เน็ต เมื่อเราส่งคำสั่งออกไปแล้วรอผลตอบกลับมาเป็นเวลาหนึ่งช่วงเวลาสั้น ๆ ก่อนจะได้เห็นผลลัพธ์ที่ต้องการ.
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> Latency คือเวลาหน่วงตั้งแต่ส่งคำสั่งจนระบบตอบสนอง ยิ่งต่ำยิ่งรู้สึกลื่น โดยมักวัดเป็นมิลลิวินาที (ms) ครับ
- **วิธีแก้:** normalize Thai morphology, เพิ่ม synonym sets และตรวจ semantic operation/answer shape แยกจาก exact keyword
- **จุดโค้ด:** `tools/run_model_benchmark_eval.py judge; eval case contracts; semantic audit layer`
- **Regression assertion:** คำพ้องที่ความหมายถูกต้องต้องผ่าน แต่คำตอบคนละเรื่องที่มี keyword กว้างต้องไม่ผ่าน
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 155. MB-1440-GL-115 - heuristic_judge_false_negative

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค อธิบายแบบใช้ในงาน chatbot
- **สถานะ/Priority:** `evaluator_false_negative` / `P2`
- **อาการทั้งหมด:** `heuristic_judge_false_negative, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `2.1460s` / visible LLM `1613.74ms`
- **จุดแรกที่พลาด:** benchmark heuristic judge
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=2.1460s visible_llm=1613.74ms; judge_passed=False judge_errors=['missing_any:ขอบคุณ']; answer_body_chars=112; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2784s
- **ลำดับเหตุ:** คำตอบมีความหมายถูก -> ใช้รูปคำ/คำพ้องต่างจาก must_contain_any -> exact substring judge ตัดไม่ผ่าน
- **Root cause:** judge ใช้ exact substring จึงไม่ยอมรับรูปคำหรือคำพ้อง เช่น ขอขอบพระคุณ/ขอบใจ แทน ขอบคุณ และ ความล่าช้า/เวลาตอบสนอง แทน latency/หน่วง
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query (current route mostly correct)` ด้วย `single-call General LLM + semantic evaluator`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอขอบพระคุณเป็นอย่างยิ่งสำหรับความใส่ใจและคำแนะนำที่ให้มาครับ
> ยินดีช่วยเหลือเสมอ หากมีอะไรเพิ่มเติมแจ้งได้นะครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอบคุณที่ติดต่อเราครับ เรายินดีช่วยเหลือและพร้อมตอบคำถามเพิ่มเติมเสมอครับ
- **วิธีแก้:** normalize Thai morphology, เพิ่ม synonym sets และตรวจ semantic operation/answer shape แยกจาก exact keyword
- **จุดโค้ด:** `tools/run_model_benchmark_eval.py judge; eval case contracts; semantic audit layer`
- **Regression assertion:** คำพ้องที่ความหมายถูกต้องต้องผ่าน แต่คำตอบคนละเรื่องที่มี keyword กว้างต้องไม่ผ่าน
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 156. MB-1450-GL-125 - heuristic_judge_false_negative

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค อธิบายแบบใช้กับวงการเกม
- **สถานะ/Priority:** `evaluator_false_negative` / `P2`
- **อาการทั้งหมด:** `heuristic_judge_false_negative, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `1.8408s` / visible LLM `1476.99ms`
- **จุดแรกที่พลาด:** benchmark heuristic judge
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=1.8408s visible_llm=1476.99ms; judge_passed=False judge_errors=['missing_any:ขอบคุณ']; answer_body_chars=107; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1953s
- **ลำดับเหตุ:** คำตอบมีความหมายถูก -> ใช้รูปคำ/คำพ้องต่างจาก must_contain_any -> exact substring judge ตัดไม่ผ่าน
- **Root cause:** judge ใช้ exact substring จึงไม่ยอมรับรูปคำหรือคำพ้อง เช่น ขอขอบพระคุณ/ขอบใจ แทน ขอบคุณ และ ความล่าช้า/เวลาตอบสนอง แทน latency/หน่วง
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query (current route mostly correct)` ด้วย `single-call General LLM + semantic evaluator`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอขอบพระคุณสำหรับโอกาสในการแข่งขันครับ
> ขอบใจที่ให้เกียรติแสดงความคิดเห็นและสนับสนุนผลงานของเราอย่างยิ่งครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอบคุณทุกคนสำหรับการแข่งขันและการสนับสนุนครับ หวังว่าจะได้พบกันในกิจกรรมครั้งต่อไปครับ
- **วิธีแก้:** normalize Thai morphology, เพิ่ม synonym sets และตรวจ semantic operation/answer shape แยกจาก exact keyword
- **จุดโค้ด:** `tools/run_model_benchmark_eval.py judge; eval case contracts; semantic audit layer`
- **Regression assertion:** คำพ้องที่ความหมายถูกต้องต้องผ่าน แต่คำตอบคนละเรื่องที่มี keyword กว้างต้องไม่ผ่าน
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 157. MB-1480-GL-155 - heuristic_judge_false_negative

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ตอบแบบสุภาพ
- **สถานะ/Priority:** `evaluator_false_negative` / `P2`
- **อาการทั้งหมด:** `heuristic_judge_false_negative, heuristic_judge_failed, mixed_gender_particles`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `1.9382s` / visible LLM `1619.11ms`
- **จุดแรกที่พลาด:** benchmark heuristic judge
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=1.9382s visible_llm=1619.11ms; judge_passed=False judge_errors=['missing_any:ขอบคุณ']; answer_body_chars=120; quality_flags=['mixed_gender_particles']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1597s
- **ลำดับเหตุ:** คำตอบมีความหมายถูก -> ใช้รูปคำ/คำพ้องต่างจาก must_contain_any -> exact substring judge ตัดไม่ผ่าน; output flags=mixed_gender_particles
- **Root cause:** judge ใช้ exact substring จึงไม่ยอมรับรูปคำหรือคำพ้อง เช่น ขอขอบพระคุณ/ขอบใจ แทน ขอบคุณ และ ความล่าช้า/เวลาตอบสนอง แทน latency/หน่วง
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query (current route mostly correct)` ด้วย `single-call General LLM + semantic evaluator`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอขอบพระคุณเป็นอย่างยิ่งสำหรับความช่วยเหลือและคำแนะนำที่ให้มา
> มีความประทับใจและซาบซึ้งจริง ๆ กับความใส่ใจของท่านครับ/ค่ะ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอบคุณมากครับสำหรับความช่วยเหลือและเวลาที่สละให้ ผมซาบซึ้งและจะนำคำแนะนำไปใช้ให้เกิดประโยชน์ครับ
- **วิธีแก้:** normalize Thai morphology, เพิ่ม synonym sets และตรวจ semantic operation/answer shape แยกจาก exact keyword
- **จุดโค้ด:** `tools/run_model_benchmark_eval.py judge; eval case contracts; semantic audit layer`
- **Regression assertion:** คำพ้องที่ความหมายถูกต้องต้องผ่าน แต่คำตอบคนละเรื่องที่มี keyword กว้างต้องไม่ผ่าน
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 158. MB-1490-GL-165 - heuristic_judge_false_negative

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ตอบให้เหมาะกับนักศึกษา
- **สถานะ/Priority:** `evaluator_false_negative` / `P2`
- **อาการทั้งหมด:** `heuristic_judge_false_negative, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `2.0869s` / visible LLM `1725.92ms`
- **จุดแรกที่พลาด:** benchmark heuristic judge
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=2.0869s visible_llm=1725.92ms; judge_passed=False judge_errors=['missing_any:ขอบคุณ']; answer_body_chars=130; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.1857s
- **ลำดับเหตุ:** คำตอบมีความหมายถูก -> ใช้รูปคำ/คำพ้องต่างจาก must_contain_any -> exact substring judge ตัดไม่ผ่าน
- **Root cause:** judge ใช้ exact substring จึงไม่ยอมรับรูปคำหรือคำพ้อง เช่น ขอขอบพระคุณ/ขอบใจ แทน ขอบคุณ และ ความล่าช้า/เวลาตอบสนอง แทน latency/หน่วง
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query (current route mostly correct)` ด้วย `single-call General LLM + semantic evaluator`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอขอบพระคุณที่ให้โอกาสและสนับสนุนนักศึกษาอย่างยิ่งครับ
> ความช่วยเหลือเหล่านี้เป็นแรงบันดาลใจให้นักศึกษาพัฒนาตนเองอย่างต่อเนื่องครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอบคุณอาจารย์และทุกคนที่ให้คำแนะนำครับ ผมจะนำคำแนะนำไปปรับใช้และพัฒนางานให้ดีขึ้นครับ
- **วิธีแก้:** normalize Thai morphology, เพิ่ม synonym sets และตรวจ semantic operation/answer shape แยกจาก exact keyword
- **จุดโค้ด:** `tools/run_model_benchmark_eval.py judge; eval case contracts; semantic audit layer`
- **Regression assertion:** คำพ้องที่ความหมายถูกต้องต้องผ่าน แต่คำตอบคนละเรื่องที่มี keyword กว้างต้องไม่ผ่าน
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 159. MB-1506-GL-181 - heuristic_judge_false_negative

- **คำถาม:** อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ ขอแบบไม่เป็นทางการมาก
- **สถานะ/Priority:** `evaluator_false_negative` / `P2`
- **อาการทั้งหมด:** `heuristic_judge_false_negative, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['latency', 'หน่วง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `1.9233s` / visible LLM `1463.70ms`
- **จุดแรกที่พลาด:** benchmark heuristic judge
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=1.9233s visible_llm=1463.70ms; judge_passed=False judge_errors=['missing_any:latency|หน่วง']; answer_body_chars=95; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.2652s
- **ลำดับเหตุ:** คำตอบมีความหมายถูก -> ใช้รูปคำ/คำพ้องต่างจาก must_contain_any -> exact substring judge ตัดไม่ผ่าน
- **Root cause:** judge ใช้ exact substring จึงไม่ยอมรับรูปคำหรือคำพ้อง เช่น ขอขอบพระคุณ/ขอบใจ แทน ขอบคุณ และ ความล่าช้า/เวลาตอบสนอง แทน latency/หน่วง
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query (current route mostly correct)` ด้วย `single-call General LLM + semantic evaluator`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ความล่าช้าระหว่างการกระทำกับผลลัพธ์ในเครื่องคอมฯ เลยนะครับ เช่น กดปุ่มแล้วจอโต้ตอบช้า ๆ เลยครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> Latency คือเวลาหน่วงตั้งแต่ส่งคำสั่งจนระบบตอบสนอง ยิ่งต่ำยิ่งรู้สึกลื่น โดยมักวัดเป็นมิลลิวินาที (ms) ครับ
- **วิธีแก้:** normalize Thai morphology, เพิ่ม synonym sets และตรวจ semantic operation/answer shape แยกจาก exact keyword
- **จุดโค้ด:** `tools/run_model_benchmark_eval.py judge; eval case contracts; semantic audit layer`
- **Regression assertion:** คำพ้องที่ความหมายถูกต้องต้องผ่าน แต่คำตอบคนละเรื่องที่มี keyword กว้างต้องไม่ผ่าน
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 160. MB-1536-GL-211 - heuristic_judge_false_negative

- **คำถาม:** อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ ตอบแบบ bullet สั้น ๆ
- **สถานะ/Priority:** `evaluator_false_negative` / `P2`
- **อาการทั้งหมด:** `heuristic_judge_false_negative, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['latency', 'หน่วง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `2.2613s` / visible LLM `1876.31ms`
- **จุดแรกที่พลาด:** benchmark heuristic judge
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=2.2613s visible_llm=1876.31ms; judge_passed=False judge_errors=['missing_any:latency|หน่วง']; answer_body_chars=145; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.3864s
- **ลำดับเหตุ:** คำตอบมีความหมายถูก -> ใช้รูปคำ/คำพ้องต่างจาก must_contain_any -> exact substring judge ตัดไม่ผ่าน
- **Root cause:** judge ใช้ exact substring จึงไม่ยอมรับรูปคำหรือคำพ้อง เช่น ขอขอบพระคุณ/ขอบใจ แทน ขอบคุณ และ ความล่าช้า/เวลาตอบสนอง แทน latency/หน่วง
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query (current route mostly correct)` ด้วย `single-call General LLM + semantic evaluator`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> •    เวลาตอบสนองระหว่างอุปกรณ์กับระบบ
> •    เวลาที่ใช้ในการส่งข้อมูลจากหนึ่งจุดไปยังอีกจุดหนึ่ง
> •    ส่งผลต่อความลื่นไหลของเกมและแอปพลิเคชันโดยตรง
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> • ความหมาย: Latency คือเวลาหน่วงตั้งแต่ส่งคำสั่งจนระบบตอบสนอง
> • ผลกระทบ: ค่ายิ่งต่ำ ระบบหรือเกมยิ่งตอบสนองไว โดยมักวัดเป็นมิลลิวินาที (ms)
- **วิธีแก้:** normalize Thai morphology, เพิ่ม synonym sets และตรวจ semantic operation/answer shape แยกจาก exact keyword
- **จุดโค้ด:** `tools/run_model_benchmark_eval.py judge; eval case contracts; semantic audit layer`
- **Regression assertion:** คำพ้องที่ความหมายถูกต้องต้องผ่าน แต่คำตอบคนละเรื่องที่มี keyword กว้างต้องไม่ผ่าน
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 161. MB-1550-GL-225 - heuristic_judge_false_negative

- **คำถาม:** ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ตอบแบบประโยคเดียว
- **สถานะ/Priority:** `evaluator_false_negative` / `P2`
- **อาการทั้งหมด:** `heuristic_judge_false_negative, heuristic_judge_failed, mixed_gender_particles, awkward_thai_phrase`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['ขอบคุณ']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `1.8106s` / visible LLM `1443.70ms`
- **จุดแรกที่พลาด:** benchmark heuristic judge
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=1.8106s visible_llm=1443.70ms; judge_passed=False judge_errors=['missing_any:ขอบคุณ']; answer_body_chars=101; quality_flags=['mixed_gender_particles', 'awkward_thai_phrase']; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.3673s
- **ลำดับเหตุ:** คำตอบมีความหมายถูก -> ใช้รูปคำ/คำพ้องต่างจาก must_contain_any -> exact substring judge ตัดไม่ผ่าน; output flags=mixed_gender_particles, awkward_thai_phrase
- **Root cause:** judge ใช้ exact substring จึงไม่ยอมรับรูปคำหรือคำพ้อง เช่น ขอขอบพระคุณ/ขอบใจ แทน ขอบคุณ และ ความล่าช้า/เวลาตอบสนอง แทน latency/หน่วง
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query (current route mostly correct)` ด้วย `single-call General LLM + semantic evaluator`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ขอขอบพระคุณเป็นอย่างยิ่งสำหรับความช่วยเหลือและโอกาสที่ได้รับ กรุณาต้อนรับและสนับสนุนต่อไปนะคะครับ/ค่ะ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> ขอบคุณมากครับสำหรับความช่วยเหลือและเวลาที่สละให้ ผมซาบซึ้งจริง ๆ ครับ
- **วิธีแก้:** normalize Thai morphology, เพิ่ม synonym sets และตรวจ semantic operation/answer shape แยกจาก exact keyword
- **จุดโค้ด:** `tools/run_model_benchmark_eval.py judge; eval case contracts; semantic audit layer`
- **Regression assertion:** คำพ้องที่ความหมายถูกต้องต้องผ่าน แต่คำตอบคนละเรื่องที่มี keyword กว้างต้องไม่ผ่าน
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction

### 162. MB-1586-GL-261 - heuristic_judge_false_negative

- **คำถาม:** อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ ตอบแบบไม่ต้องมีตัวอย่างยาว
- **สถานะ/Priority:** `evaluator_false_negative` / `P2`
- **อาการทั้งหมด:** `heuristic_judge_false_negative, heuristic_judge_failed`
- **Expected contract:** category=`['general', 'knowledge']`, must contain=`['latency', 'หน่วง']`
- **Actual path:** `general/general_knowledge_query` / `pipeline:general_llm_fallback` / wall `2.3955s` / visible LLM `1968.26ms`
- **จุดแรกที่พลาด:** benchmark heuristic judge
- **สิ่งที่พบ:** Typhoon mode=pipeline:general_llm_fallback route=general/general_knowledge_query; wall=2.3955s visible_llm=1968.26ms; judge_passed=False judge_errors=['missing_any:latency|หน่วง']; answer_body_chars=155; quality_flags=[]; No-LLM mode=pipeline:general_llm_disabled passed=False wall=0.4500s
- **ลำดับเหตุ:** คำตอบมีความหมายถูก -> ใช้รูปคำ/คำพ้องต่างจาก must_contain_any -> exact substring judge ตัดไม่ผ่าน
- **Root cause:** judge ใช้ exact substring จึงไม่ยอมรับรูปคำหรือคำพ้อง เช่น ขอขอบพระคุณ/ขอบใจ แทน ขอบคุณ และ ความล่าช้า/เวลาตอบสนอง แทน latency/หน่วง
- **เทคนิคที่ใช้วินิจฉัย:** `expected_contract_check, actual_answer_review, route_intent_mode_trace, no_llm_counterfactual_comparison, answer_shape_and_language_lint`
- **เส้นทางที่ควรเป็น:** `general/general_knowledge_query (current route mostly correct)` ด้วย `single-call General LLM + semantic evaluator`
- **Source requirement:** ไม่ต้องใช้ PSU RAG; ห้ามเพิ่ม current/PSU claims
- **คำตอบจริง:**
> ความล่าช้าในการตอบสนองระหว่างอุปกรณ์หรือระบบคอมพิวเตอร์ เช่น เวลาที่ข้อมูลเดินทางจากเครื่องหนึ่งไปยังอีกเครื่องหนึ่งจนได้รับการประมวลผลและตอบกลับมาแล้วครับ
> หมายเหตุ: คำตอบนี้เป็นความรู้ทั่วไปของโมเดล ไม่ได้อ้างอิงจากฐานข้อมูล PSU Esports Studio - Phuket
- **ตัวอย่างคำตอบที่ควรได้:**
> Latency คือเวลาหน่วงตั้งแต่ส่งคำสั่งจนระบบตอบสนอง ยิ่งต่ำยิ่งรู้สึกลื่น โดยมักวัดเป็นมิลลิวินาที (ms) ครับ
- **วิธีแก้:** normalize Thai morphology, เพิ่ม synonym sets และตรวจ semantic operation/answer shape แยกจาก exact keyword
- **จุดโค้ด:** `tools/run_model_benchmark_eval.py judge; eval case contracts; semantic audit layer`
- **Regression assertion:** คำพ้องที่ความหมายถูกต้องต้องผ่าน แต่คำตอบคนละเรื่องที่มี keyword กว้างต้องไม่ผ่าน
- **ความมั่นใจ/Caveat:** `high`; ผล benchmark เก็บเพียง 12 trace entries สุดท้าย; first wrong stage บางเคสมาจาก focused reproduction และ source-code reconstruction
