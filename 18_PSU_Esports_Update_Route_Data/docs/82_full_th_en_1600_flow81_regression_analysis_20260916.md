# รายงานผล Full Regression Thai-English 1,600 ข้อ (Flow 81)

> วันที่รัน: 16 กันยายน 2026  
> Run ID: `full_th_en_1600_flow81_25690916_143338`  
> สถานะ: **เสร็จสมบูรณ์ แต่ยังไม่พร้อมประกาศผ่าน Production SLA**

## 1. ขอบเขตและข้อจำกัด

- รัน Thai benchmark 1,600 ข้อ และ English Shadow 1,600 ข้อแบบ serial in-process ด้วย pipeline ที่เปิด Local LLM และ Semantic RAG
- English Shadow เป็นคำถามที่แปลงจากชุดไทยด้วยเครื่องมือ จึงใช้ตรวจ route, contract, locale และ latency ได้ แต่ไม่ใช่ตัววัดคุณภาพภาษาอังกฤษที่ผ่านการอนุมัติจากมนุษย์
- ไม่มี browser queue, HTTP load หรือ concurrent users ในรอบนี้ จึงห้ามตีความ latency ว่าเป็นค่าการใช้งานพร้อมกันจริง
- Raw results ห้ามแก้ไข: `reports/bilingual_english/full_th_en_1600_flow81_25690916_143338/`

## 2. ผลที่ยืนยันจาก Log

| ชุดทดสอบ | Strict pass | P95 | P99 | สูงสุด | >= 10 วินาที | >= 20 วินาที | Harness timeout | Worker crash |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Thai | 1,519/1,600 (94.94%) | 2.180s | 14.421s | 19.535s | 30 | 0 | 0 | 0 |
| English | 1,425/1,600 (89.06%) | 0.892s | 4.301s | 8.678s | 0 | 0 | 0 | 0 |

### สรุปการตัดสิน

1. **Worker reliability ผ่านในรอบนี้**: ไม่มี harness timeout และไม่มี worker crash ทั้งสองภาษา
2. **English 20-second ceiling ผ่าน**: ทุกคำขอตอบก่อน 10 วินาทีด้วยซ้ำ แต่คุณภาพยังต่ำกว่าเป้าหมาย English 90%
3. **Thai accuracy ดี**: 94.94% สูงกว่าเป้าหมาย 94% แต่ latency ไม่ผ่านเป้าหมายเดิม 10 วินาที เพราะมี 30 ข้อเกินเพดาน
4. **ห้ามใช้คะแนนรวมอย่างเดียวตัดสิน**: Thai มี latency tail ที่กระทบผู้ใช้จริง ส่วน English มีคำตอบไทยปะปนและ route/contract ที่ยังไม่ครบ

## 3. Thai: ปัญหาที่ต้องแก้ก่อน

### 3.1 Long-tail จาก General LLM หลัง RAG miss

**สิ่งที่ยืนยันจาก Log**

- 25 จาก 30 slow cases ใช้ `pipeline:general_llm_after_rag_miss`
- อีก 5 ข้อเป็น `pipeline:no_answer` หลังรอเส้นทาง RAG/LLM เดิม
- ตัวอย่างช้าที่สุดคือ `MB-1360-GL-035` คำถาม “ช่วยสรุปวิธีพูดขอบคุณแบบสุภาพ 2 ประโยค ตอบเป็นภาษาไทย” ใช้ 19.535 วินาที
- คำถามกลุ่มนี้เป็น general knowledge นอกขอบเขต PSU Esports Studio จึงไม่ควร consume RAG budget แล้วรอ Local LLM เต็ม 20 วินาทีทุกครั้ง

**Root cause ที่เสนอและต้องทดสอบใน trace ละเอียด**

1. General-question gate ปล่อยให้ RAG ลองค้นก่อน แม้ไม่มี PSU entity, target หรือ knowledge-category signal
2. หลัง RAG miss ระบบเรียก Local LLM เพื่อสร้าง general answer โดยไม่มี output-token cap ที่สั้นพอสำหรับคำถามนอกโดเมน
3. บางกรณี RAG miss แล้ว fallback `no_answer` แต่เกิดหลัง budget ถูกใช้ไปแล้ว

**แนวทางแก้ตามลำดับ**

1. เพิ่ม `GeneralScopeGate` ก่อน RAG: หากไม่มี PSU scope และไม่ได้เป็นคำถามที่อนุญาตให้ตอบความรู้ทั่วไป ให้ตอบ boundary/no-answer ทันที
2. ถ้าจะรองรับ general answer ให้มี `general_llm_budget` แยก เช่น 4-6 วินาที และ `max_tokens` ต่ำสำหรับคำตอบสั้น
3. เมื่อ remaining budget ต่ำกว่า `general_llm_min_start_budget` ให้ตอบ safe no-answer ทันที ไม่เริ่ม model call
4. เก็บ log `rag_skipped_reason`, `llm_queue_sec`, `llm_generation_sec`, `fallback_reason` เพื่อยืนยันว่าปัญหาอยู่ที่ queue, model load หรือ generation

### 3.2 Game description ถูกถาม แต่ได้ clarification

**สิ่งที่ยืนยันจาก Log**

- Thai failure `games -> clarification` 34 ข้อ
- ตัวอย่าง: “VALORANT คือเกมอะไร”, “TEKKEN 8 คือเกมอะไร”, “Beat Saber คือเกมอะไร” ได้ `pipeline:ambiguity_clarification`
- แต่คำถามรูปแบบ “X คือเกมอะไร” ระบุ game entity และ facet `overview/description` ชัดเจนแล้ว จึงไม่ควรขอให้ผู้ใช้เลือก “รายชื่อเกม/ข้อมูลเกม”

**แนวทางแก้**

1. เพิ่ม Question Frame rule: `<resolved_game> + คือเกมอะไร/what is <game>` => `games/game_detail/overview`
2. ให้ `GameResolver.matched` ที่มี margin ผ่านเกณฑ์ล็อก target ก่อน Ambiguity Gate
3. Clarification ทำงานเฉพาะ `ambiguous`, `unknown`, หรือถามหลาย game โดยไม่มี target เดียวเท่านั้น
4. เพิ่ม regression cases สำหรับ 34 game-description questions ทั้งไทยและอังกฤษ

### 3.3 Competition rule ถูกดึงเข้า game/knowledge route

**สิ่งที่ยืนยันจาก Log**

- Thai failures ในกลุ่ม `competition_rules` 22 ข้อ
- route ที่ออกผิดมากสุดคือ `competition_rules -> games` 9 ข้อ และ `competition_rules -> knowledge` 6 ข้อ

**แนวทางแก้**

1. เพิ่ม competition vocabulary/facet ที่ยังขาดใน `QuestionFrame`: tournament, roster, substitute, late arrival, disconnect, restart, penalty, registration deadline
2. เมื่อมี competition operation + rule signal ให้ lock `competition_rules` ก่อน game detail และ generic RAG
3. ใช้ RAG เฉพาะ chunks ที่ filter `category=competition_rules`, `effective_from <= now`, `valid_until >= now`
4. การตอบต้องอ้าง evidence card ของกฎ ไม่ให้ LLM สรุปหรือสร้างกฎเอง

## 4. English: ปัญหาที่ต้องแก้ก่อน

### 4.1 Thai prose leak จาก Member response

**สิ่งที่ยืนยันจาก Log**

- English มี `thai_prose_leak` 55 ข้อ
- ทั้งหมดอยู่ใน `pipeline:structured_members_source_th`
- ตัวอย่าง `Who are the members?` ส่งรายชื่อและตำแหน่งภาษาไทยจำนวนมาก แม้ prefix และ source เป็นอังกฤษ

**การตัดสินใจที่ต้องล็อก**

- ชื่อบุคคลภาษาไทยสามารถแสดงตาม source record ได้
- แต่ role/title และ explanatory prose ต้องเป็น English approved localization หรือแทนด้วย English no-answer ที่ชัดเจน ไม่ใช่ส่งทั้ง block ไทยโดยอัตโนมัติ

**แนวทางแก้**

1. สร้าง `members` localization overlay: `display_name_en`, `role_en`, `group_en`, `source_url`, `source_hash`, `status=approved`
2. English member template แสดงเฉพาะ field ที่ approved; Thai original ให้เป็น source link ไม่ใช่ body หลัก
3. ถ้า person/role ยังไม่มี English localization: ตอบว่ารายละเอียดอยู่ใน official Thai source พร้อม URL แทน Thai prose block
4. เพิ่ม validator: อนุญาต Thai script ได้เฉพาะ `approved_proper_name` token list, URL และ quoted source title

### 4.2 English general knowledge และ out-of-domain ถูกนับเป็น category failure

**สิ่งที่ยืนยันจาก Log**

- English `general knowledge -> no_answer` 86 ข้อ เช่น “Can you help me with my math homework?” และ “What is the current hit song?”
- คำตอบ `pipeline:english_no_answer` เป็น behavior ที่ปลอดภัยตาม PSU-only policy เป็นส่วนใหญ่
- English Shadow มี answer contract ที่คาดหวัง general/knowledge จึงทำให้ strict score ลดลง แม้ product behavior อาจถูกต้อง

**การแก้ที่ต้องทำกับ Evaluation ก่อนแก้ runtime**

1. แยก benchmark เป็น `in_scope_factual`, `approved_general_assist`, `out_of_scope_safe_refusal`
2. กรณีที่ product policy คือ no-answer/refusal ต้องมี allowed mode/expected category เป็น `no_answer` หรือ `boundary`
3. เก็บ `policy_correct` แยกจาก `strict_contract_pass` เพื่อไม่ให้ score บอกว่าสิ่งที่ปลอดภัยเป็น bug
4. ห้ามเพิ่ม knowledge ที่ไม่เกี่ยวกับ PSU เพียงเพื่อทำคะแนน English Shadow ดีขึ้น

### 4.3 English category routing ยังหลุดในคำถามผสม

**สิ่งที่ยืนยันจาก Log**

- English category failure รวม 120 ข้อ
- ตัวอย่าง pattern ที่ยังหลุด: game+reservation, multi-question, rules/penalty, game->schedule และ game->competition_rules
- มี Thai-English route category mismatch 219 คู่ และ output bullet shape ต่างกันมาก 478 คู่

**แนวทางแก้**

1. ใช้ Universal Intent/Question Frame เดียวกันทุก locale; ภาษาเปลี่ยนได้เฉพาะ parser lexicon และ formatter
2. เพิ่ม English intent patterns แบบ token-aware สำหรับ `play`, `available`, `where`, `book`, `reservation`, `cancel`, `rule`, `penalty`, `schedule`, `price`
3. Multi-question splitter ต้องส่ง locale และ facet/target ต่อ fragment ไม่ให้ fragment หลังเสีย context ของ game จาก fragment ก่อน
4. สร้าง bilingual parity tests จาก 219 pair ที่ mismatch โดยแบ่ง “expected locale variation” กับ “runtime route defect” ก่อน

### 4.4 English output format ยังไม่เท่า Thai

**สิ่งที่ยืนยันจาก Log**

- พบ large bullet-format gap 478 คู่
- ราคาและเกมบางคำตอบอังกฤษสั้นกว่าไทยมาก เช่น Thai แสดง price breakdown ทุก tier แต่ English บาง case สรุปเพียง 1-2 บรรทัด

**แนวทางแก้**

1. สร้าง locale-neutral `AnswerViewModel` สำหรับ price, games catalog, schedule, member list, controls และ rules
2. ให้ Thai/English formatter render view model เดียวกัน; ต่างเฉพาะ label, grammar และ localized content
3. เพิ่ม `format_contract` ต่อ route: required sections, bullet count range, source placement, total/count consistency
4. ไม่ใช้ LLM เพื่อจัดรูปแบบ fact answer ที่ Structured template ทำได้

## 5. ลำดับการทำงานที่แนะนำ

| Priority | งาน | เหตุผล | เกณฑ์ผ่าน |
|---|---|---|---|
| P0 | GeneralScopeGate + bounded general LLM | ลด 30 Thai slow cases โดยตรง | Thai over-10s = 0 ใน corpus เดิม |
| P0 | Thai game-description Question Frame | แก้ 34 clear questions ที่ไม่ควร clarification | 34/34 เข้า game detail |
| P0 | Member English localization fallback | กำจัด 55 Thai prose leaks | English leak = 0 |
| P1 | Reclassify English Shadow policy cases | แยก metric ที่มีความหมายออกจาก benchmark mismatch | policy-correct report แยกชัดเจน |
| P1 | Competition route lock + filtered evidence | แก้ 22 Thai competition failures | competition strict pass ดีขึ้นโดยไม่มี source mismatch |
| P1 | Shared AnswerViewModel + formatter contract | ลด format gap 478 คู่ | format parity per route ผ่านเกณฑ์ |
| P2 | English mixed/multi-question intent expansion | ลด 120 English category errorsที่เป็น runtime defect จริง | English in-scope factual >= 94% |
| P2 | HTTP concurrent load test | Serial run ยังยืนยัน capacity ไม่ได้ | ไม่มี cross-session leak/worker crash ตาม profile ที่ตกลง |

## 6. Acceptance Criteria สำหรับรอบถัดไป

- Thai strict pass ไม่ต่ำกว่า 94.94% และ Thai in-scope factual answer ไม่ลดลง
- Thai `over_10s = 0`, P95 <= 5s, P99 <= 10s ใน full benchmark ที่เปิด model
- English Thai prose leak = 0 ยกเว้น approved proper name token ที่ตรวจได้
- English in-scope factual strict pass >= 94%; policy refusal ต้องถูกนับใน policy metric ไม่ใช่ category error
- ไม่มี worker crash, harness timeout, watchdog escape หรือ response เกิน 20s
- Thai-English parity ต้องวัด per route template; large bullet gap ลดลงจาก 478 โดยกำหนด allowed route-specific exceptions

## 7. Artefacts

- [Summary](../reports/bilingual_english/full_th_en_1600_flow81_25690916_143338/summary.json)
- [Analyzer report](../reports/bilingual_english/full_th_en_1600_flow81_25690916_143338/analysis.md)
- [Thai raw results](../reports/bilingual_english/full_th_en_1600_flow81_25690916_143338/th_results.jsonl)
- [English raw results](../reports/bilingual_english/full_th_en_1600_flow81_25690916_143338/en_results.jsonl)
- [Related remediation flow](81_game_detail_bilingual_reliability_remediation_flow_20260916.md)
