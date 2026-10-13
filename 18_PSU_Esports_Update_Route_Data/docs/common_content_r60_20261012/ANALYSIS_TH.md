# วิเคราะห์สาเหตุ r60 แบบแยกชั้น พร้อมหลักฐานก่อน/หลัง

## 1. ทำไมข้อมูลมีครบแล้วยังตอบผิด

การมีข้อเท็จจริงกับการเลือกข้อเท็จจริงเป็นคนละขั้น: resolve record → interpret needs → select related records → render values → validate coverage. เมื่อรายการถูกแต่เลือก `eligibility` แทน `required_proofs` ระบบอ่านข้อความที่มีอยู่จริงได้อย่างซื่อสัตย์ แต่ไม่ตอบสิ่งที่ user ต้องการ ยิ่ง validator ตรวจเฉพาะ field ที่ระบบเลือกเอง มันอาจผ่านทั้งที่ need ที่ตกหล่นไม่เคยกลายเป็น obligation เลย

รอบนี้ gold แยกจาก runtime: ตัวประเมินกำหนด expected fields เองก่อนวัด ไม่ส่งให้ LLM/parser และใช้ raw fixture values/evidence locator ตรวจคำตอบ อย่างไรก็ดี gold ที่ agent แต่งเองยังมีข้อจำกัดด้าน human agreement ไม่ใช่ “คำตอบจริงทุกสถานการณ์”

## 2. จัดลำดับสาเหตุและวิธีแก้

### P0A — Planner ไม่ถูกเรียก ทั้งที่ต้องตีความเพิ่ม

**หลักฐาน:** คำถาม `รหัสสถานะถูกแปลว่าอะไร แล้วข้อมูลหมดอายุเมื่อไหร่` ก่อนแก้ selected=[] และ clarification; reserved contact/schedule ไทย/อังกฤษมี audits=[] ทั้งที่มี need ที่สองตกหล่น. owner_server `/api/preview` ส่ง CommonAnswerer โดยไม่มี planner; engine common route ใช้ bool(None)=False ก่อนอ่าน environment default

**สาเหตุ:** broad information gate กว้างเกิน, resolver เจอหนึ่ง field จึงคิดว่าครบ, entry point มี setting ไม่ตรงกัน. นี่ไม่ใช่โมเดลสร้างคำตอบผิด เพราะหลายเคสไม่ได้ส่งคำถามไปหาโมเดลเลย

**แก้:** overview_request ต้องเป็นภาพรวมจริง; resolution_uncertain ตรวจการเปรียบเทียบ/คำถามหลายส่วน/weak nouns; owner preview ใช้ setting เดียวกับเว็บแชท + audit; engine ใช้ default เมื่อ None. explicit disable คงอยู่. เปิด LLM ไม่รับรองว่าเลือก field ถูก ต้องมีชั้นถัดไป

### P0B — Semantic collision: คำตรง แต่หมายถึงคนละ attribute

**หลักฐาน:** verify eligibility→eligibility (ต้อง proof); provider status codes→provider (ต้อง mapping+freshness); rule edition→text (ต้อง rulebook_release); FAQ response→question (ต้อง answer)

**สาเหตุ:** topic word กับ requested property ใช้คำร่วมกัน; description อังกฤษเดิมมาจาก key ที่แยก underscore จึงไม่อธิบายความต่าง; constraint ให้ field อยู่ใน schema ไม่บังคับความหมาย. ไม่ได้มี retrieval fact ผิดในเคสเหล่านี้

**แก้:** descriptions ความหมาย/ขอบเขตชัดเจน, review weak interpretations, strong needs ไม่ใช่ทุก lexical match, intent terms/concept conjunctions ใน metadata เฉพาะ kind. reserved ยังพลาด FAQ response เพราะ modelเลือก question แม้ JSONถูก ต่อมาจึงเติมความหมาย response/reply→answer ใน schema metadata. เป็นการแก้ attribute reuse ไม่เพิ่ม fixture-name branch

### P0C — ตอบส่วนเดียวในคำถามหลายส่วน

**หลักฐาน:** session_minutesไม่มี occupancy_minutes; facility accessibilityไม่มีlocation; live mappingไม่มีfreshness; closure reasonไม่มีstate. ข้อมูลทุกส่วนอยู่ใน release เดียวกัน

**สาเหตุ:** flattened field array ไม่บอกความรับผิดชอบต่อคำถามแต่ละส่วน; detector เดิมไม่ split แล้ว; selection ที่มีแค่หนึ่งข้อถูกมองว่าพอ

**แก้:** semantic_clauses + JSON per clause IDs enum + ต้องมีครบทุก ID + union fields และ obligations. เพิ่ม แล้ว/then และ modifier ellipsis. ยังไม่ใช่ syntactic parser: conjunction ในชื่อ/วลีอาจ split เกิน, >6 clause เป็น documented limit; [] ต้องแจ้ง partial ถ้าตีความไม่ได้

### P1A — False partial แม้รวม facts ครบ

**หลักฐาน:** dev_final closure EN noisy เลือกstate,reasonครบ แต่ why clause=[] เนื้อหาคำตอบมีทั้งสอง จึง response_partial_answer และ fail

**สาเหตุ:** modelใส่reasonในclause0 แล้วปล่อยclause1ว่าง; coverage guard ที่มอง allocationอย่างเดียวจึงสร้าง false alarm

**แก้:** typed clause need ที่ชัดเจน ถ้า fieldนั้นเลือกอยู่แล้วในunion ให้ repair coverage พร้อม trace clause_coverage_repairs ไม่ลบ unknown clause ทิ้งทุกกรณี. กฎนี้ไม่สามารถพิสูจน์ความหมาย clause ที่ไม่รู้ได้

### P1B — ไม่รู้ task ที่ถูกปฏิเสธ / ต่อบทสนทนาผิด

**หลักฐาน:** “ไม่เอาราคา ขอเวลาเล่นอย่างเดียว” selected session+amount; “So what should I bring to prove I qualify?” หลังข้อมูล audience คืนno_common_answer

**สาเหตุ:** bag-of-cues เก็บคำราคาโดยไม่สนใจ negation; followup trigger จำกัด; inheritfieldsจากคำถามภาพรวมเดิมอาจพาทั้งหมดกลับมา

**แก้:** focus_request เฉพาะ rejected named task + affirmative alternative ไม่ rewrite “ไม่ได้เป็นนักศึกษา/not a student”; inherited record context กับ inherited requested fields แยกกัน; bare selectorจึงสืบทอดfields คำถามใหม่เลือกneedsใหม่. ใส่ test explicit new entity priority ของr59ร่วมด้วย

### P1C — พิมพ์ผิดหลายส่วนและภาษาอังกฤษไม่ใช่ key

**หลักฐาน:** whic edition/rullebook, อย่างน้อ, ลงให้เลล่น/รอบี้ ทำให้lexicalfieldsตก; descriptionเพียงอย่างเดียวจากรอบแรกยังfail13

**แก้:** คง original input + suggested_spelling จาก lexicon schema เฉพาะ one-edit insertion/deletion candidateเดียว; private valid-English dictionary / protected words / digitsคงไว้; THnoiseอาศัยdescriptions+clauseLLM ไม่มีการอ้างว่าทำ Thai spellchecker สมบูรณ์

**ขอบเขต:** ไม่แก้same-length substitution/transpositionในhelperนี้ ป้องกันเปลี่ยนคำจริงโดยเดา; ไม่มีkeyboard-weighted probability, embedding rerankingหรือtrainednoisy-channel. งานก่อนหน้ารองรับบางแนวแยกอยู่แล้ว ไม่รวมคะแนนร60เพื่ออ้างว่าไทยทุกtypoผ่าน

### P1D — ความสัมพันธ์ระหว่างหมวดยังไม่มี projection

**หลักฐาน:** game parentถามoffered/version/installed_resource_ids/บัญชี/ข้อจำกัดของservice; เดิม readerรู้เฉพาะfieldลูกบางกลุ่ม

**แก้:** catalog-driven unique childfield projection + game_id joins; ทวน16/16พร้อมevidence. ไม่เปลี่ยนdata/FKsหรือให้LLMสร้างjoinอิสระ. fieldร่วมเช่นgame_versionยังใช้scopeheuristic; policy_idแสดงชื่อpolicy ไม่ขยายทุกเนื้อหากฎ เป็นงานต่อ

### P2 — การวัดและเครื่องมือทำให้เข้าใจผลผิด

**หลักฐาน:** unitคำสั่งหนึ่งใช้ชื่อmoduleผิด จึงFAILED(errors=1) แม้r60ทั้ง13methodผ่าน; เก็บlogนั้นไว้ แล้วแก้ชื่อเป็นtest_common_query_contract_r59รัน21ผ่าน. relatedregressionก่อนแก้เกิด20failgame_modeจากphraseเดียว across20profiles แม้harnessรายงานregressions=0เพราะมันเทียบbaselineรุ่นเก่ากว่าr59

**แก้:** รายงาน5056 actualpass/failตรงๆ เทียบr59ที่เคยผ่านครบ; repairmodifierellipsisแล้ว5056/5056. ไม่ลบfailedrun/เรียกทุกผลว่า100%. schema rejectionแยกtransportfailure และสุขภาพโมเดล

## 3. ความหมายคะแนนและ confidence

confidenceในanswerเป็นheuristic ไม่ได้calibrateกับhumanlabels; confidence_calibrated=Falseในartifact. semantic_status=typed_clause_scope คือknown typed cuesครบในช่วงนั้น; schema_only_unverified_intentแปลว่าenumถูกแต่ยังไม่มีหลักฐานรับรองintent. transport_ok=Trueหมายถึงได้HTTPresponse ไม่ได้แปลว่าเลือกfield/ตอบถูก. schema_accepted=Trueไม่รับรองsource/evidence/needทั้งหมด

ผลdevelopmentผ่านต้องครบexpectedfields/status/content/evidenceและไม่ตอบforbiddenfields แต่fieldextrasไม่ได้ทำให้failทุกกรณี จึงรายงานprecisionแยก. คำถามreservedrental “What kit is covered by the rental price?” goldกำหนดทั้งincludedkitและamount ทั้งที่priceอาจไม่ใช่สิ่งที่ขอชัดเจน เป็นgoldambiguityที่ต้องทวนในรอบhumanblind ห้ามบังคับproductionให้นำราคาออกทุกครั้งเพียงเพื่อคะแนน

## 4. ใช้งานจริงและรายการยังต้องทำ

1. **สูงสุด:** semantic validation ยังไม่รู้needที่โมเดลตีความผิดแต่ไม่เว้นclause. แก้ต่อด้วยschema meaning/exclusion/examplesแยกkindและgoldใหม่ก่อนทดสอบ; เปรียบเทียบexactfieldprecision ไม่ใช้ข้อเท็จจริงเป็นaliases. ไม่เพิ่มjudgeLLMอัตโนมัติจนกว่าจะวัดquality/latency/budget
2. ชื่อไม่ครบ/ไม่ระบุrecordหลายเป้าหมาย: รอบนี้ยังnamedrecord; ต้องมีentityretrievalrankingและclarificationbeforefactsพร้อมfuzzyadversarialcases ไม่เหมาว่าเพิ่มdescriptionแล้วจบ
3. กระบวนการpublish/withdrawกับlegacyfallback: ต้องทดสอบว่าcommonmissของrecordที่เคยpublishไม่กลับไปตอบfactsเก่าในlegacyindex อันนี้ยังไม่ได้พิสูจน์ในr60
4. graphdetails: expandpolicycontentwhenasked, resource→service→rateที่unique, multi-platformscope, sharedgame_versionsemantics; มีFKguardsแล้วแต่readprojectionยังไม่ครบทุกเส้น
5. renderer: humanlabels/enums/scopesและemptyzone_idsที่อาจหมายถึงallzones; อย่าแสดงblankจนผู้ใช้ตีความว่าไม่มี; ต้องอิงcatalogก่อนแก้
6. LLMoff/unavailable/busy: dev18/100ในสำนวนนี้; ต้องแจ้งunknownneeds/clarifyอย่างเฉพาะเมื่อfactsไม่ครบ หรือยืนยันfieldผ่านUI ไม่fallbackตอบที่ผิดเพียงเพื่อให้มีคำตอบ. plannerdeadline4sec/admission/circuitยังคงอยู่ ไม่ได้ทำconcurrencybenchmarkใหม่
7. modelsemanticmeaningมี122keysรวม155catalogslots คำที่ใช้ซ้ำแต่meaningต่างkindอาจต้องkind-specificoverride. metadataไม่ใช่เจ้าของfacttranslation; nativeTH/ENhumanreviewยังคนละงาน
8. actualownerrecordsยังdraft/ยังไม่publish — ต้องยืนยันข้อเท็จจริงโดยเจ้าของก่อนpublish; รอบนี้แก้logic/ทดสอบsynthetic ไม่อนุมัติหรือกรอกนโยบายแทน

## 5. งานวิจัยที่ใช้ประกอบจากr59

ดู [Research.md ของ r59](RESEARCH_R59.md) พร้อมวิธีค้น/ข้อจำกัด ไม่มีการค้นเพิ่มหรืออ้างว่าฝึกโมเดลในร60

- [D3ST](https://arxiv.org/abs/2201.08904): ประยุกต์schema descriptionsและfieldselection; ไม่ได้reproduce model/training
- [SGD-X](https://ojs.aaai.org/index.php/AAAI/article/view/21341): เป็นเหตุผลให้แยกสำนวนใหม่กับcanonicalและfreeze reserved
- [PICARD](https://aclanthology.org/2021.emnlp-main.779/): แนวทางtypedconstraint; ระบบนี้ใช้JSONschema+postvalidator ไม่ใช่PICARDdecoder
- [CheckList](https://aclanthology.org/2020.acl-main.442/): behavioraltests/negation/invarianceและgroupfailure; ไม่เอาaggregateเดียวปิดปัญหา
- noisy-channel/Thai keyboard papersในresearchเดิม: ชี้ว่าความน่าจะเป็นcandidate+contextสำคัญ; r60ใช้เพียงconservativecandidateproposal ไม่อ้างimplementationprobabilisticทั้งชุด

## 6. หลักฐานรายเคส

ด้านล่างแสดงinputจริง/gold/selected/response/error/auditจากlog ไม่แปลว่าgoldทุกข้อผ่านhumanreview การเลือกผิดเป็นการอ่านlogร่วมกับcode ไม่ได้อ้างว่ามีhiddenchain-of-thoughtของโมเดล

### ชุด baseline_llm

#### service-th-clean_new

คำถาม: รอบทดลอง ละอองฝน เวลาเล่นจริงกับเวลาที่ล็อกเครื่องเอาไว้เท่ากันไหม กี่นาที

ต้องมี: `['session_minutes', 'occupancy_minutes']`

เลือกก่อน: `['session_minutes']`; ผล: `['missing_field:occupancy_minutes']`

คำตอบก่อน:

```text
**รอบทดลอง ละอองฝน**
• ระยะเวลาเล่นของบริการ: 30 [S1]
```

คำตอบหลัง:

```text
**รอบทดลอง ละอองฝน**
• ระยะเวลาเล่นของบริการ: 30 [S1]
• เวลาที่กันทรัพยากร เช่น VR 30 นาทีอาจกัน 60: 60 [S2]
```

เลือกหลัง: `['session_minutes', 'occupancy_minutes']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_service_03"
    ],
    "requested_fields": [
      "session_minutes"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "เวลาเล่นจริงกับเวลาที่ล็อกเครื่องเอาไว้เท่ากันไหม กี่นาที",
    "field_selection": [
      {
        "field": "session_minutes",
        "cue": "เวลาเล่น",
        "method": "schema_attribute"
      }
    ],
    "confidence_calibrated": false,
    "unresolved_clauses": []
  },
  "planner_audits": []
}
```

#### service-th-sentence_noise

คำถาม: รอบทดลอง ละอองฝน เวลาเล่นจริงกกับเวลาที่ล็อเครื่องเอาไว้เทท่ากันไหม กี่นาที

ต้องมี: `['session_minutes', 'occupancy_minutes']`

เลือกก่อน: `['session_minutes']`; ผล: `['missing_field:occupancy_minutes']`

คำตอบก่อน:

```text
**รอบทดลอง ละอองฝน**
• ระยะเวลาเล่นของบริการ: 30 [S1]
```

คำตอบหลัง:

```text
**รอบทดลอง ละอองฝน**
• ระยะเวลาเล่นของบริการ: 30 [S1]
• เวลาที่กันทรัพยากร เช่น VR 30 นาทีอาจกัน 60: 60 [S2]
```

เลือกหลัง: `['session_minutes', 'occupancy_minutes']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_service_03"
    ],
    "requested_fields": [
      "session_minutes"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "เวลาเล่นจริงกกับเวลาที่ล็อเครื่องเอาไว้เทท่ากันไหม กี่นาที",
    "field_selection": [
      {
        "field": "session_minutes",
        "cue": "เวลาเล่น",
        "method": "schema_attribute"
      }
    ],
    "confidence_calibrated": false,
    "unresolved_clauses": []
  },
  "planner_audits": []
}
```

#### game-th-clean_new

คำถาม: เกมสมมุติ ละอองฝน เริ่มเล่นแล้วต้องทำอะไรให้ผ่านเกมนี้

ต้องมี: `['how_to_play']`

เลือกก่อน: `[]`; ผล: `['response_clarification', 'missing_field:how_to_play']`

คำตอบก่อน:

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

คำตอบหลัง:

```text
**เกมสมมุติ ประภาคารเสมือน**
• เป้าหมาย/วงจรการเล่นโดยสรุป: ใช้มือเสมือนจัดแสงนำทางเรือ; ใช้คำสั่งตามชุดควบคุมทดลอง [S1]
```

เลือกหลัง: `['how_to_play']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_game_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "เริ่มเล่นแล้วต้องทำอะไรให้ผ่านเกมนี้",
    "field_selection": [],
    "confidence_calibrated": false,
    "unresolved_clauses": [
      "เริ่มเล่นแล้วต้องทำอะไรให้ผ่านเกมนี้"
    ]
  },
  "planner_audits": [
    {
      "attempted": true,
      "transport_ok": true,
      "schema_accepted": false,
      "final_plan_accepted": false,
      "rejection_reason": "abstained",
      "proposal": {
        "requested_fields": [],
        "all_fields": false,
        "platform": null
      },
      "accepted_plan": null,
      "semantic": {
        "semantic_status": "no_schema_plan"
      },
      "elapsed_ms": 855.9857001528144
    }
  ]
}
```

#### game-th-sentence_noise

คำถาม: เกมสมมุติ ละอองฝน เริ่มเล่นแลล้วต้องำอะไรให้ผผ่านเกมนี้

ต้องมี: `['how_to_play']`

เลือกก่อน: `[]`; ผล: `['response_clarification', 'missing_field:how_to_play']`

คำตอบก่อน:

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

คำตอบหลัง:

```text
**เกมสมมุติ ประภาคารเสมือน**
• เป้าหมาย/วงจรการเล่นโดยสรุป: ใช้มือเสมือนจัดแสงนำทางเรือ; ใช้คำสั่งตามชุดควบคุมทดลอง [S1]
```

เลือกหลัง: `['how_to_play']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_game_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "เริ่มเล่นแลล้วต้องำอะไรให้ผผ่านเกมนี้",
    "field_selection": [],
    "confidence_calibrated": false,
    "unresolved_clauses": [
      "เริ่มเล่นแลล้วต้องำอะไรให้ผผ่านเกมนี้"
    ]
  },
  "planner_audits": [
    {
      "attempted": true,
      "transport_ok": true,
      "schema_accepted": false,
      "final_plan_accepted": false,
      "rejection_reason": "abstained",
      "proposal": {
        "requested_fields": [],
        "all_fields": false,
        "platform": null
      },
      "accepted_plan": null,
      "semantic": {
        "semantic_status": "no_schema_plan"
      },
      "elapsed_ms": 1039.23249989748
    }
  ]
}
```

#### game-en-clean_new

คำถาม: Fictional game Drizzle What should a beginner do to complete this game?

ต้องมี: `['how_to_play']`

เลือกก่อน: `[]`; ผล: `['response_clarification', 'missing_field:how_to_play']`

คำตอบก่อน:

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

คำตอบหลัง:

```text
**Fictional Virtual Beacon**
• how to play: Use motion inputs to arrange lights guiding ships; follow the demonstration controls [S1]

English translation is machine generated and has not been reviewed by the owner.
```

เลือกหลัง: `['how_to_play']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_game_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "what should a beginner do to complete this game?",
    "field_selection": [],
    "confidence_calibrated": false,
    "unresolved_clauses": [
      "what should a beginner do to complete this game"
    ]
  },
  "planner_audits": [
    {
      "attempted": true,
      "transport_ok": true,
      "schema_accepted": false,
      "final_plan_accepted": false,
      "rejection_reason": "abstained",
      "proposal": {
        "requested_fields": [],
        "all_fields": false,
        "platform": null
      },
      "accepted_plan": null,
      "semantic": {
        "semantic_status": "no_schema_plan"
      },
      "elapsed_ms": 978.3710001502186
    }
  ]
}
```

#### game-en-sentence_noise

คำถาม: Fictional game Drizzle What shouldd a beginner o to complette this game?

ต้องมี: `['how_to_play']`

เลือกก่อน: `[]`; ผล: `['response_clarification', 'missing_field:how_to_play']`

คำตอบก่อน:

```text
Which part of this record do you need: instructions, controls, devices, or prices?
```

คำตอบหลัง:

```text
**Fictional Virtual Beacon**
• how to play: Use motion inputs to arrange lights guiding ships; follow the demonstration controls [S1]

English translation is machine generated and has not been reviewed by the owner.
```

เลือกหลัง: `['how_to_play']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_game_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "what shouldd a beginner o to complette this game?",
    "field_selection": [],
    "confidence_calibrated": false,
    "unresolved_clauses": [
      "what shouldd a beginner o to complette this game"
    ]
  },
  "planner_audits": [
    {
      "attempted": true,
      "transport_ok": true,
      "schema_accepted": false,
      "final_plan_accepted": false,
      "rejection_reason": "abstained",
      "proposal": {
        "requested_fields": [],
        "all_fields": false,
        "platform": null
      },
      "accepted_plan": null,
      "semantic": {
        "semantic_status": "no_schema_plan"
      },
      "elapsed_ms": 1024.1004000417888
    }
  ]
}
```

#### audience-en-clean_new

คำถาม: Demo visitors Drizzle What should I present to verify my eligibility?

ต้องมี: `['required_proofs']`

เลือกก่อน: `['eligibility']`; ผล: `['missing_field:required_proofs']`

คำตอบก่อน:

```text
**Demo visitors Drizzle**
• eligibility: Fictional group 3: demo sessions only [S1]

English translation is machine generated and has not been reviewed by the owner.
```

คำตอบหลัง:

```text
**Demo visitors Drizzle**
• required proofs: • DEMO pass Drizzle [S1]

English translation is machine generated and has not been reviewed by the owner.
```

เลือกหลัง: `['required_proofs']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_audience_03"
    ],
    "requested_fields": [
      "eligibility"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "what should i present to verify my eligibility?",
    "field_selection": [
      {
        "field": "eligibility",
        "cue": "eligibility",
        "method": "schema_attribute"
      }
    ],
    "confidence_calibrated": false,
    "unresolved_clauses": []
  },
  "planner_audits": []
}
```

#### facility-th-clean_new

คำถาม: พื้นที่พัก ละอองฝน จุดนี้อยู่แถวไหน รถเข็นเข้าได้ยังไง

ต้องมี: `['location', 'accessibility']`

เลือกก่อน: `['accessibility']`; ผล: `['missing_field:location']`

คำตอบก่อน:

```text
**พื้นที่พัก ละอองฝน**
• การเข้าถึง/รถเข็น หากยังไม่มีข้อมูลให้ unknown: ข้อมูลสมมุติ: เข้าถึงได้ไม่มีขั้น [S1]
```

คำตอบหลัง:

```text
**พื้นที่พัก ละอองฝน**
• อยู่บริเวณไหน: เก้าอี้พัก VR อยู่ห้องทดสอบ 103 [S1]
• การเข้าถึง/รถเข็น หากยังไม่มีข้อมูลให้ unknown: ข้อมูลสมมุติ: เข้าถึงได้ไม่มีขั้น [S2]
```

เลือกหลัง: `['location', 'accessibility']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_facility_03"
    ],
    "requested_fields": [
      "accessibility"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "จุดนี้อยู่แถวไหน รถเข็นเข้าได้ยังไง",
    "field_selection": [
      {
        "field": "accessibility",
        "cue": "รถเข็น",
        "method": "schema_attribute"
      }
    ],
    "confidence_calibrated": false,
    "unresolved_clauses": []
  },
  "planner_audits": []
}
```

#### game_service-th-sentence_noise

คำถาม: การติดตั้งทดลอง ละอองฝน เกมนี้ลงให้เลล่นในรอบี้หรือยัง เปป็นรุ่นอะไร

ต้องมี: `['offered', 'game_version']`

เลือกก่อน: `['game_version']`; ผล: `['missing_field:offered']`

คำตอบก่อน:

```text
**การติดตั้งทดลอง ละอองฝน**
• เวอร์ชันเกมที่ติดตั้ง ถ้าไม่ทราบให้ unknown: DEMO BUILD 3 [S1]
```

คำตอบหลัง:

```text
**การติดตั้งทดลอง ละอองฝน**
• ศูนย์ยืนยันมี/ไม่มีเกมนี้ในบริการนี้: มี/ใช่ [S1]
• เวอร์ชันเกมที่ติดตั้ง ถ้าไม่ทราบให้ unknown: DEMO BUILD 3 [S2]
```

เลือกหลัง: `['offered', 'game_version']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_game_service_03"
    ],
    "requested_fields": [
      "game_version"
    ],
    "all_fields": false,
    "method": "bounded_llm_schema_fields",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "เกมนี้ลงให้เลล่นในรอบี้หรือยัง เปป็นรุ่นอะไร",
    "field_selection": [],
    "confidence_calibrated": false,
    "unresolved_clauses": []
  },
  "planner_audits": [
    {
      "attempted": true,
      "transport_ok": true,
      "schema_accepted": true,
      "final_plan_accepted": true,
      "rejection_reason": null,
      "proposal": {
        "requested_fields": [
          "game_version"
        ],
        "all_fields": false,
        "platform": null
      },
      "accepted_plan": {
        "requested_fields": [
          "game_version"
        ],
        "all_fields": false,
        "platform": null,
        "method": "bounded_llm_schema_fields"
      },
      "semantic": {
        "semantic_status": "schema_only_unverified_intent",
        "unresolved_clauses": [
          "เกมนี้ลงให้เลล่นในรอบี้หรือยัง เปป็นรุ่นอะไร"
        ]
      },
      "elapsed_ms": 573.5883999150246
    }
  ]
}
```

#### game_mode-th-sentence_noise

คำถาม: โหมดทดลอง ละอองฝน ต้องรวมคคนอย่างน้อกี่คน แล้วมมากสุดกี่คน

ต้องมี: `['players_min', 'players_max']`

เลือกก่อน: `['players_max']`; ผล: `['missing_field:players_min']`

คำตอบก่อน:

```text
**โหมดทดลอง ละอองฝน**
• สูงสุดของโหมดเกม ไม่ใช่ความจุบริการ: 1 [S1]
```

คำตอบหลัง:

```text
**โหมดทดลอง ละอองฝน**
• จำนวนผู้เล่นขั้นต่ำของโหมด: 1 [S1]
• สูงสุดของโหมดเกม ไม่ใช่ความจุบริการ: 1 [S2]
```

เลือกหลัง: `['players_min', 'players_max']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_game_mode_03"
    ],
    "requested_fields": [
      "players_max"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "ต้องรวมคคนอย่างน้อกี่คน แล้วมมากสุดกี่คน",
    "field_selection": [
      {
        "field": "players_max",
        "cue": "participant/seating count",
        "method": "schema_attribute"
      }
    ],
    "confidence_calibrated": false,
    "unresolved_clauses": []
  },
  "planner_audits": []
}
```

#### closure-th-clean_new

คำถาม: ประกาศวันทดลอง ละอองฝน ประกาศนี้ให้เปิดหรือหยุดบริการ เพราะอะไร

ต้องมี: `['state', 'reason']`

เลือกก่อน: `['reason']`; ผล: `['missing_field:state']`

คำตอบก่อน:

```text
**ประกาศวันทดลอง ละอองฝน**
• เหตุผลปิด/เปิดพิเศษ: ประกาศสมมุติ ละอองฝน: closed [S1]
```

คำตอบหลัง:

```text
**ประกาศวันทดลอง ละอองฝน**
• เหตุผลปิด/เปิดพิเศษ: ประกาศสมมุติ ละอองฝน: closed [S1]
• ประเภทข้อยกเว้น: closed [S2]
```

เลือกหลัง: `['reason', 'state']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_closure_03"
    ],
    "requested_fields": [
      "reason"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "ประกาศนี้ให้เปิดหรือหยุดบริการ เพราะอะไร",
    "field_selection": [
      {
        "field": "reason",
        "cue": "เพราะอะไร",
        "method": "schema_attribute"
      }
    ],
    "confidence_calibrated": false,
    "unresolved_clauses": []
  },
  "planner_audits": []
}
```

#### closure-th-sentence_noise

คำถาม: ประกาศวันทดลอง ละอองฝน ประกาศนี้ใหห้เปิดหรือยุดบริกการ เพราะอะไร

ต้องมี: `['state', 'reason']`

เลือกก่อน: `['reason']`; ผล: `['missing_field:state']`

คำตอบก่อน:

```text
**ประกาศวันทดลอง ละอองฝน**
• เหตุผลปิด/เปิดพิเศษ: ประกาศสมมุติ ละอองฝน: closed [S1]
```

คำตอบหลัง:

```text
**ประกาศวันทดลอง ละอองฝน**
• เหตุผลปิด/เปิดพิเศษ: ประกาศสมมุติ ละอองฝน: closed [S1]
• ประเภทข้อยกเว้น: closed [S2]
```

เลือกหลัง: `['reason', 'state']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_closure_03"
    ],
    "requested_fields": [
      "reason"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "ประกาศนี้ใหห้เปิดหรือยุดบริกการ เพราะอะไร",
    "field_selection": [
      {
        "field": "reason",
        "cue": "เพราะอะไร",
        "method": "schema_attribute"
      }
    ],
    "confidence_calibrated": false,
    "unresolved_clauses": []
  },
  "planner_audits": []
}
```

#### competition-th-clean_new

คำถาม: รายการฝึก ละอองฝน แข่งกันวันไหนและยึดกฎฉบับใด

ต้องมี: `['rulebook_release', 'competition_dates']`

เลือกก่อน: `['text']`; ผล: `['missing_field:rulebook_release', 'missing_field:competition_dates']`

คำตอบก่อน:

```text
**ข้อการแข่งขันทดลอง ละอองฝน**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ละอองฝน [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: competition_format [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ละอองฝน [S5]
• เลขข้อเดิม เช่น 6.1.5: 4.3 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 3: พักเมื่อเวียนหัว ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

คำตอบหลัง:

```text
**รายการฝึก ละอองฝน**
• วันที่การแข่งขันจากต้นทาง: • 2026-12-03 [S1]
• ฉบับและเวอร์ชันกติกา: DEMO20_REV_3 [S2]
```

เลือกหลัง: `['competition_dates', 'rulebook_release']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_competition_03"
    ],
    "requested_fields": [
      "text"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "แข่งกันวันไหนและยึดกฎฉบับใด",
    "field_selection": [
      {
        "field": "text",
        "cue": "competition rule text",
        "method": "schema_attribute"
      }
    ],
    "confidence_calibrated": false,
    "unresolved_clauses": [
      "แข่งกันวันไหน"
    ]
  },
  "planner_audits": [
    {
      "attempted": true,
      "transport_ok": true,
      "schema_accepted": true,
      "final_plan_accepted": true,
      "rejection_reason": null,
      "proposal": {
        "requested_fields": [
          "competition_dates",
          "rulebook_release"
        ],
        "all_fields": false,
        "platform": null
      },
      "accepted_plan": {
        "requested_fields": [
          "competition_dates",
          "rulebook_release"
        ],
        "all_fields": false,
        "platform": null,
        "method": "bounded_llm_schema_fields"
      },
      "semantic": {
        "semantic_status": "schema_only_unverified_intent",
        "unresolved_clauses": [
          "แข่งกันวันไหน"
        ]
      },
      "elapsed_ms": 781.7915000487119
    }
  ]
}
```

#### competition-th-sentence_noise

คำถาม: รายการฝึก ละอองฝน แข่งกันววันไหนแะยึดกฎฎฉบับใด

ต้องมี: `['rulebook_release', 'competition_dates']`

เลือกก่อน: `['text']`; ผล: `['missing_field:rulebook_release', 'missing_field:competition_dates']`

คำตอบก่อน:

```text
**ข้อการแข่งขันทดลอง ละอองฝน**
• ฉบับรายการที่กฎเป็นของมัน: รายการฝึก ละอองฝน [S1]
• สถานะความสมบูรณ์ของข้อนี้: complete [S2]
• ข้อก่อนหน้า/ข้อยกเว้นที่ต้องดึงร่วม:  [S3]
• หมวดกฎ: competition_format [S4]
• หัวข้อข้อกติกา: ข้อการแข่งขันทดลอง ละอองฝน [S5]
• เลขข้อเดิม เช่น 6.1.5: 4.3 [S6]
• ข้อความข้อกติกาเต็ม ห้ามตัดเงื่อนไขท้ายข้อ: ข้อสมมุติ 3: พักเมื่อเวียนหัว ให้ปฏิบัติตามคำตัดสิน required; ยกเว้นกรณีผู้ดูแลอนุมัติเป็นลายลักษณ์อักษร; ไม่ใช่กติกาจริง [S7]
```

คำตอบหลัง:

```text
**รายการฝึก ละอองฝน**
• วันที่การแข่งขันจากต้นทาง: • 2026-12-03 [S1]
• ฉบับและเวอร์ชันกติกา: DEMO20_REV_3 [S2]
```

เลือกหลัง: `['competition_dates', 'rulebook_release']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_competition_03"
    ],
    "requested_fields": [
      "text"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "แข่งกันววันไหนแะยึดกฎฎฉบับใด",
    "field_selection": [
      {
        "field": "text",
        "cue": "competition rule text",
        "method": "schema_attribute"
      }
    ],
    "confidence_calibrated": false,
    "unresolved_clauses": []
  },
  "planner_audits": []
}
```

#### person-th-clean_new

คำถาม: ผู้ดูแลสมมุติ ละอองฝน คนนี้ดูแลเรื่องไหน ติดต่อเรื่องงานทางไหน

ต้องมี: `['role', 'public_contact_id']`

เลือกก่อน: `['public_contact_id']`; ผล: `['missing_field:role']`

คำตอบก่อน:

```text
**ผู้ดูแลสมมุติ ละอองฝน**
• ช่องทางงานที่อนุญาตเผยแพร่: https://example.invalid/demo20/contact/3 [S1]
```

คำตอบหลัง:

```text
**ผู้ดูแลสมมุติ ละอองฝน**
• ตำแหน่ง/หน้าที่: ผู้ดูแลสมมุติเรื่อง พักเมื่อเวียนหัว [S1]
• ช่องทางงานที่อนุญาตเผยแพร่: https://example.invalid/demo20/contact/3 [S2]
```

เลือกหลัง: `['role', 'public_contact_id']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_person_03"
    ],
    "requested_fields": [
      "public_contact_id"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "คนนี้ดูแลเรื่องไหน ติดต่อเรื่องงานทางไหน",
    "field_selection": [
      {
        "field": "public_contact_id",
        "cue": "ติดต่อ",
        "method": "schema_attribute"
      }
    ],
    "confidence_calibrated": false,
    "unresolved_clauses": []
  },
  "planner_audits": []
}
```

#### live_binding-th-clean_new

คำถาม: ตัวเชื่อมทดลอง ละอองฝน รหัสสถานะถูกแปลว่าอะไร แล้วข้อมูลหมดอายุเมื่อไหร่

ต้องมี: `['status_mapping', 'freshness_policy']`

เลือกก่อน: `[]`; ผล: `['response_clarification', 'missing_field:status_mapping', 'missing_field:freshness_policy']`

คำตอบก่อน:

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

คำตอบหลัง:

```text
**ตัวเชื่อมทดลอง ละอองฝน**
• ความหมายสถานะจาก API ต้องมี fixture ที่รู้ผล: • normalized: free; raw: DEMO_EMPTY_3
• normalized: occupied; raw: DEMO_BUSY_3
• normalized: unknown; raw: DEMO_UNKNOWN_3 [S1]
• นโยบาย cache/TTL ที่อนุมัติ: ค่าจำลอง TTL 30 วินาที; ไม่เรียก API และไม่ยืนยันสถานะสด [S2]
```

เลือกหลัง: `['status_mapping', 'freshness_policy']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_live_binding_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "รหัสสถานะถูกแปลว่าอะไร แล้วข้อมูลหมดอายุเมื่อไหร่",
    "field_selection": [],
    "confidence_calibrated": false,
    "unresolved_clauses": [
      "รหัสสถานะถูกแปลว่าอะไร แล้วข้อมูลหมดอายุเมื่อไหร่"
    ]
  },
  "planner_audits": []
}
```

#### live_binding-th-sentence_noise

คำถาม: ตัวเชื่อมทดลอง ละอองฝน รหัสสถานะถูกกแปลว่าอะไร แล้ข้อมูลหมดดอายุเมื่อไหร่

ต้องมี: `['status_mapping', 'freshness_policy']`

เลือกก่อน: `[]`; ผล: `['response_clarification', 'missing_field:status_mapping', 'missing_field:freshness_policy']`

คำตอบก่อน:

```text
ต้องการทราบส่วนใดของรายการนี้ เช่น วิธีเล่น ปุ่ม อุปกรณ์ หรือราคา?
```

คำตอบหลัง:

```text
**ตัวเชื่อมทดลอง ละอองฝน**
• ความหมายสถานะจาก API ต้องมี fixture ที่รู้ผล: • normalized: free; raw: DEMO_EMPTY_3
• normalized: occupied; raw: DEMO_BUSY_3
• normalized: unknown; raw: DEMO_UNKNOWN_3 [S1]
• นโยบาย cache/TTL ที่อนุมัติ: ค่าจำลอง TTL 30 วินาที; ไม่เรียก API และไม่ยืนยันสถานะสด [S2]
```

เลือกหลัง: `['status_mapping', 'freshness_policy']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_live_binding_03"
    ],
    "requested_fields": [],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "รหัสสถานะถูกกแปลว่าอะไร แล้ข้อมูลหมดดอายุเมื่อไหร่",
    "field_selection": [],
    "confidence_calibrated": false,
    "unresolved_clauses": [
      "รหัสสถานะถูกกแปลว่าอะไร แล้ข้อมูลหมดดอายุเมื่อไหร่"
    ]
  },
  "planner_audits": []
}
```

#### live_binding-en-clean_new

คำถาม: Demo binding Drizzle What do provider status codes mean, and when does the data expire?

ต้องมี: `['status_mapping', 'freshness_policy']`

เลือกก่อน: `['provider']`; ผล: `['missing_field:status_mapping', 'missing_field:freshness_policy']`

คำตอบก่อน:

```text
**Demo binding Drizzle**
• provider: wordpress_booking [S1]

English translation is machine generated and has not been reviewed by the owner.
```

คำตอบหลัง:

```text
**Demo binding Drizzle**
• status mapping: • normalized: free; raw: DEMO_EMPTY_3
• normalized: occupied; raw: DEMO_BUSY_3
• normalized: unknown; raw: DEMO_UNKNOWN_3 [S1]
• freshness policy: Synthetic TTL 30 seconds; no API call or live status claim [S2]

English translation is machine generated and has not been reviewed by the owner.
```

เลือกหลัง: `['status_mapping', 'freshness_policy']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_live_binding_03"
    ],
    "requested_fields": [
      "provider"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "what do provider status codes mean, and when does the data expire?",
    "field_selection": [
      {
        "field": "provider",
        "cue": "provider",
        "method": "schema_attribute"
      }
    ],
    "confidence_calibrated": false,
    "unresolved_clauses": [
      "when does the data expire"
    ]
  },
  "planner_audits": [
    {
      "attempted": true,
      "transport_ok": true,
      "schema_accepted": true,
      "final_plan_accepted": true,
      "rejection_reason": null,
      "proposal": {
        "requested_fields": [
          "status_mapping",
          "freshness_policy"
        ],
        "all_fields": false,
        "platform": null
      },
      "accepted_plan": {
        "requested_fields": [
          "status_mapping",
          "freshness_policy"
        ],
        "all_fields": false,
        "platform": null,
        "method": "bounded_llm_schema_fields"
      },
      "semantic": {
        "semantic_status": "schema_only_unverified_intent",
        "unresolved_clauses": [
          "when does the data expire"
        ]
      },
      "elapsed_ms": 741.5644000284374
    }
  ]
}
```

#### negative-service-th

คำถาม: รอบทดลอง ละอองฝน ไม่เอาราคา ขอเวลาเล่นอย่างเดียว

ต้องมี: `['session_minutes']`

เลือกก่อน: `['session_minutes', 'amount_minor']`; ผล: `['rejected_need_answered:amount_minor']`

คำตอบก่อน:

```text
**รอบทดลอง ละอองฝน**
• ระยะเวลาเล่นของบริการ: 30 [S1]

**อัตราทดลอง ละอองฝน**
• จำนวนสตางค์: 70 บาท = 7000; 0 คือฟรีเมื่อยืนยันจริง: 75.00 THB [S2]
• กลุ่มผู้ใช้: กลุ่มผู้ใช้ ละอองฝน [S3]
• อนุญาตคูณเวลาได้หรือคิดตายตัว ต้องมีหลักฐาน: no_extrapolation [S4]
• สกุลเงิน: THB [S5]
• ช่วงเวลาที่ราคานี้ครอบคลุม: 30 [S6]
• ช่วงผู้ใช้สูงสุด: 1 [S7]
• ช่วงผู้ใช้ขั้นต่ำ: 1 [S8]
• บริการตามระบบจอง: รอบทดลอง ละอองฝน [S9]
• ภาษี/เงื่อนไข ถ้ายังไม่ระบุห้ามคิดรวมเอง: ราคาสมมุติ ไม่ใช้เรียกเก็บเงินจริง [S10]
• คิดต่ออะไร: per_group [S11]
```

คำตอบหลัง:

```text
**รอบทดลอง ละอองฝน**
• ระยะเวลาเล่นของบริการ: 30 [S1]
```

เลือกหลัง: `['session_minutes']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_service_03"
    ],
    "requested_fields": [
      "session_minutes",
      "amount_minor"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "ไม่เอาราคา ขอเวลาเล่นอย่างเดียว",
    "field_selection": [
      {
        "field": "session_minutes",
        "cue": "เวลาเล่น",
        "method": "schema_attribute"
      },
      {
        "field": "amount_minor",
        "cue": "ราคา",
        "method": "schema_attribute"
      }
    ],
    "confidence_calibrated": false,
    "unresolved_clauses": []
  },
  "planner_audits": []
}
```

#### negative-service-en

คำถาม: Demo session Drizzle I do not want the price; just tell me the play duration

ต้องมี: `['session_minutes']`

เลือกก่อน: `['session_minutes', 'amount_minor']`; ผล: `['rejected_need_answered:amount_minor']`

คำตอบก่อน:

```text
**Demo session Drizzle**
• session minutes: 30 [S1]

**Demo tariff Drizzle**
• amount minor: 75.00 THB [S2]
• audience id: Demo visitors Drizzle [S3]
• calculation rule: no_extrapolation [S4]
• currency: THB [S5]
• duration minutes: 30 [S6]
• persons max: 1 [S7]
• persons min: 1 [S8]
• service id: Demo session Drizzle [S9]
• tax note: Synthetic price; never collect actual payment [S10]
• unit: per_group [S11]

English translation is machine generated and has not been reviewed by the owner.
```

คำตอบหลัง:

```text
**Demo session Drizzle**
• session minutes: 30 [S1]

English translation is machine generated and has not been reviewed by the owner.
```

เลือกหลัง: `['session_minutes']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_service_03"
    ],
    "requested_fields": [
      "session_minutes",
      "amount_minor"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "i do not want the price; just tell me the play duration",
    "field_selection": [
      {
        "field": "session_minutes",
        "cue": "play duration",
        "method": "schema_attribute"
      },
      {
        "field": "amount_minor",
        "cue": "price",
        "method": "schema_attribute"
      }
    ],
    "confidence_calibrated": false,
    "unresolved_clauses": []
  },
  "planner_audits": []
}
```

#### context-audience-en

คำถาม: So what should I bring to prove I qualify?

ต้องมี: `['required_proofs']`

เลือกก่อน: `[]`; ผล: `['no_common_answer']`

คำตอบก่อน:

```text
None
```

คำตอบหลัง:

```text
**Demo visitors Drizzle**
• required proofs: • DEMO pass Drizzle [S1]

English translation is machine generated and has not been reviewed by the owner.
```

เลือกหลัง: `['required_proofs']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {},
  "planner_audits": []
}
```

### ชุด reserved_first

#### contact-th-reserved_new

คำถาม: ช่องทางช่วยเหลือ ตะวันอ่อน ขอช่องทางช่วยเหลือพร้อมช่วงเวลาที่ติดต่อได้

ต้องมี: `['value', 'office_hours']`

เลือกก่อน: `['value']`; ผล: `['missing_field:office_hours']`

คำตอบก่อน:

```text
**https://example.invalid/demo20/social/7**
• URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย: https://example.invalid/demo20/social/7 [S1]
```

คำตอบหลัง:

```text
**https://example.invalid/demo20/social/7**
• URL/อีเมล/เบอร์โทร แยกเป็นช่อง ไม่อยู่ในข้อความลอย: https://example.invalid/demo20/social/7 [S1]
• เวลาตอบของช่องทางนี้: ช่วงทดลอง 11:00–20:00 [S2]
```

เลือกหลัง: `['value', 'office_hours']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_contact_07"
    ],
    "requested_fields": [
      "value"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "ขอช่องทางช่วยเหลือพร้อมช่วงเวลาที่ติดต่อได้",
    "field_selection": [
      {
        "field": "value",
        "cue": "ติดต่อ",
        "method": "schema_attribute"
      }
    ],
    "confidence_calibrated": false,
    "request_focus": null,
    "unresolved_clauses": [],
    "semantic_review_needed": false,
    "semantic_plan_accepted": false
  },
  "planner_audits": []
}
```

#### schedule-en-reserved_new

คำถาม: Demo timetable Gentle Sun Are opening hours different from the periods available for reservations?

ต้องมี: `['open_periods', 'bookable_periods']`

เลือกก่อน: `['open_periods']`; ผล: `['missing_field:bookable_periods']`

คำตอบก่อน:

```text
**Demo timetable Gentle Sun**
• open periods: • end: 20:00; start: 11:00 [S1]

English translation is machine generated and has not been reviewed by the owner.
```

คำตอบหลัง:

```text
**Demo timetable Gentle Sun**
• open periods: • end: 20:00; start: 11:00 [S1]
• bookable periods: • end: 12:00; start: 11:00
• end: 20:00; start: 13:00 [S2]

English translation is machine generated and has not been reviewed by the owner.
```

เลือกหลัง: `['open_periods', 'bookable_periods']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_schedule_07"
    ],
    "requested_fields": [
      "open_periods"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "are opening hours different from the periods available for reservations?",
    "field_selection": [
      {
        "field": "open_periods",
        "cue": "opening hours",
        "method": "schema_attribute"
      }
    ],
    "confidence_calibrated": false,
    "request_focus": null,
    "unresolved_clauses": [],
    "semantic_review_needed": false,
    "semantic_plan_accepted": false
  },
  "planner_audits": []
}
```

#### closure-th-reserved_new

คำถาม: ประกาศวันทดลอง ตะวันอ่อน วันตามประกาศเปิดไหม เพราะเหตุใด

ต้องมี: `['state', 'reason']`

เลือกก่อน: `['state']`; ผล: `['missing_field:reason']`

คำตอบก่อน:

```text
**ประกาศวันทดลอง ตะวันอ่อน**
• ประเภทข้อยกเว้น: modified_hours [S1]
```

คำตอบหลัง:

```text
**ประกาศวันทดลอง ตะวันอ่อน**
• ประเภทข้อยกเว้น: modified_hours [S1]
• เหตุผลปิด/เปิดพิเศษ: ประกาศสมมุติ ตะวันอ่อน: modified_hours [S2]
```

เลือกหลัง: `['state', 'reason']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_closure_07"
    ],
    "requested_fields": [
      "state"
    ],
    "all_fields": false,
    "method": "exact",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "วันตามประกาศเปิดไหม เพราะเหตุใด",
    "field_selection": [
      {
        "field": "state",
        "cue": "ปิดไหม",
        "method": "schema_attribute"
      }
    ],
    "confidence_calibrated": false,
    "request_focus": null,
    "unresolved_clauses": [],
    "semantic_review_needed": false,
    "semantic_plan_accepted": false
  },
  "planner_audits": []
}
```

#### closure-en-reserved_new

คำถาม: Demo date notice Gentle Sun What does this notice say about closure, and what is the reason?

ต้องมี: `['state', 'reason']`

เลือกก่อน: `['reason']`; ผล: `['missing_field:state']`

คำตอบก่อน:

```text
**Demo date notice Gentle Sun**
• reason: Synthetic Gentle Sun date notice: modified_hours [S1]

English translation is machine generated and has not been reviewed by the owner.
```

คำตอบหลัง:

```text
**Demo date notice Gentle Sun**
• reason: Synthetic Gentle Sun date notice: modified_hours [S1]
• state: modified_hours [S2]

English translation is machine generated and has not been reviewed by the owner.
```

เลือกหลัง: `['reason', 'state']`; ผ่าน=True; fieldเสริม=`[]`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_closure_07"
    ],
    "requested_fields": [
      "reason"
    ],
    "all_fields": false,
    "method": "bounded_llm_schema_fields",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "what does this notice say about closure, and what is the reason?",
    "field_selection": [
      {
        "field": "reason",
        "cue": "reason",
        "method": "schema_attribute"
      }
    ],
    "confidence_calibrated": false,
    "request_focus": null,
    "unresolved_clauses": [],
    "semantic_review_needed": true,
    "semantic_plan_accepted": true,
    "planner_semantic_audit": {
      "semantic_status": "schema_only_unverified_intent",
      "unresolved_clauses": [
        "what does this notice say about closure"
      ],
      "preserved_strong_needs": [
        "reason"
      ],
      "unclear_clauses": [],
      "clause_coverage_repairs": []
    }
  },
  "planner_audits": [
    {
      "attempted": true,
      "transport_ok": true,
      "schema_accepted": true,
      "final_plan_accepted": true,
      "rejection_reason": null,
      "proposal": {
        "requested_fields": [
          "reason"
        ],
        "all_fields": false,
        "platform": null
      },
      "clause_plan": {
        "clause_fields": [
          {
            "id": 0,
            "requested_fields": [
              "reason"
            ]
          },
          {
            "id": 1,
            "requested_fields": [
              "reason"
            ]
          }
        ],
        "all_fields": false,
        "platform": null
      },
      "accepted_plan": {
        "requested_fields": [
          "reason"
        ],
        "all_fields": false,
        "platform": null,
        "method": "bounded_llm_schema_fields"
      },
      "semantic": {
        "semantic_status": "schema_only_unverified_intent",
        "unresolved_clauses": [
          "what does this notice say about closure"
        ],
        "preserved_strong_needs": [
          "reason"
        ],
        "unclear_clauses": [],
        "clause_coverage_repairs": []
      },
      "query_recoveries": [],
      "original_question": "what does this notice say about closure, and what is the reason?",
      "prompt_eval_count": 430,
      "elapsed_ms": 2116.9966999441385
    }
  ]
}
```

#### faq-en-reserved_new

คำถาม: Demo enquiry Gentle Sun What is the response to this FAQ, and when does it apply?

ต้องมี: `['answer', 'scope_note']`

เลือกก่อน: `['question', 'scope_note']`; ผล: `['missing_field:answer']`

คำตอบก่อน:

```text
**Demo enquiry Gentle Sun**
• question: Demo enquiry Gentle Sun [S1]
• scope note: Only applies to fictional Gentle Sun scenario [S2]

English translation is machine generated and has not been reviewed by the owner.
```

คำตอบหลัง:

```text
**Demo enquiry Gentle Sun**
• question: Demo enquiry Gentle Sun [S1]
• scope note: Only applies to fictional Gentle Sun scenario [S2]
• answer: Example answer: Fictional rule for Team roster: required; contact the demo operator if requirements are not met. Not PSU policy. [S3]

English translation is machine generated and has not been reviewed by the owner.
```

เลือกหลัง: `['question', 'scope_note', 'answer']`; ผ่าน=True; fieldเสริม=`['question']`

Traceก่อน:

```json
{
  "plan": {
    "record_ids": [
      "demo20_faq_07"
    ],
    "requested_fields": [
      "question",
      "scope_note"
    ],
    "all_fields": false,
    "method": "bounded_llm_schema_fields",
    "scope": "common_published",
    "platform": null,
    "query_without_entity": "what is the response to this faq, and when does it apply?",
    "field_selection": [],
    "confidence_calibrated": false,
    "request_focus": null,
    "unresolved_clauses": [],
    "semantic_review_needed": true,
    "semantic_plan_accepted": true,
    "planner_semantic_audit": {
      "semantic_status": "schema_only_unverified_intent",
      "unresolved_clauses": [
        "what is the response to this faq",
        "when does it apply"
      ],
      "preserved_strong_needs": [],
      "unclear_clauses": [],
      "clause_coverage_repairs": []
    }
  },
  "planner_audits": [
    {
      "attempted": true,
      "transport_ok": true,
      "schema_accepted": true,
      "final_plan_accepted": true,
      "rejection_reason": null,
      "proposal": {
        "requested_fields": [
          "question",
          "scope_note"
        ],
        "all_fields": false,
        "platform": null
      },
      "clause_plan": {
        "clause_fields": [
          {
            "id": 0,
            "requested_fields": [
              "question"
            ]
          },
          {
            "id": 1,
            "requested_fields": [
              "scope_note"
            ]
          }
        ],
        "all_fields": false,
        "platform": null
      },
      "accepted_plan": {
        "requested_fields": [
          "question",
          "scope_note"
        ],
        "all_fields": false,
        "platform": null,
        "method": "bounded_llm_schema_fields"
      },
      "semantic": {
        "semantic_status": "schema_only_unverified_intent",
        "unresolved_clauses": [
          "what is the response to this faq",
          "when does it apply"
        ],
        "preserved_strong_needs": [],
        "unclear_clauses": [],
        "clause_coverage_repairs": []
      },
      "query_recoveries": [],
      "original_question": "what is the response to this faq, and when does it apply?",
      "prompt_eval_count": 374,
      "elapsed_ms": 1179.408400086686
    }
  ]
}
```

## 7. ตาราง development ทั้ง100 — ความครบกับความเกิน

| ID | ผ่าน | ต้องมี | เลือกจริง | fieldเสริม |
|---|---|---|---|---|
| center-th-clean_new | True | building, floor | floor, building |  |
| center-th-sentence_noise | True | building, floor | floor, building |  |
| center-en-clean_new | True | building, floor | building, floor |  |
| center-en-sentence_noise | True | building, floor | building, floor |  |
| zone-th-clean_new | True | room_seats | room_seats |  |
| zone-th-sentence_noise | True | room_seats | room_seats |  |
| zone-en-clean_new | True | room_seats | room_seats |  |
| zone-en-sentence_noise | True | room_seats | room_seats |  |
| equipment_model-th-clean_new | True | specifications | name, device_type, specifications, usage | device_type, name, usage |
| equipment_model-th-sentence_noise | True | specifications | name, device_type, specifications, usage | device_type, name, usage |
| equipment_model-en-clean_new | True | specifications | specifications |  |
| equipment_model-en-sentence_noise | True | specifications | specifications |  |
| resource-th-clean_new | True | capacity_persons | capacity_persons |  |
| resource-th-sentence_noise | True | capacity_persons | capacity_persons |  |
| resource-en-clean_new | True | capacity_persons | capacity_persons |  |
| resource-en-sentence_noise | True | capacity_persons | capacity_persons |  |
| service-th-clean_new | True | session_minutes, occupancy_minutes | session_minutes, occupancy_minutes |  |
| service-th-sentence_noise | True | session_minutes, occupancy_minutes | session_minutes, occupancy_minutes |  |
| service-en-clean_new | True | session_minutes, occupancy_minutes | session_minutes, occupancy_minutes |  |
| service-en-sentence_noise | True | session_minutes, occupancy_minutes | session_minutes, occupancy_minutes |  |
| game-th-clean_new | True | how_to_play | how_to_play |  |
| game-th-sentence_noise | True | how_to_play | how_to_play |  |
| game-en-clean_new | True | how_to_play | how_to_play |  |
| game-en-sentence_noise | True | how_to_play | how_to_play |  |
| audience-th-clean_new | True | required_proofs | required_proofs |  |
| audience-th-sentence_noise | True | required_proofs | required_proofs |  |
| audience-en-clean_new | True | required_proofs | required_proofs |  |
| audience-en-sentence_noise | True | required_proofs | required_proofs |  |
| contact-th-clean_new | True | value, office_hours | channel, value, office_hours | channel |
| contact-th-sentence_noise | True | value, office_hours | channel, value, purpose, office_hours | channel, purpose |
| contact-en-clean_new | True | value, office_hours | channel, value, office_hours | channel |
| contact-en-sentence_noise | True | value, office_hours | channel, value, purpose, office_hours | channel, purpose |
| procedure-th-clean_new | True | steps, required_documents | topic, preconditions, steps, outcome, required_documents | outcome, preconditions, topic |
| procedure-th-sentence_noise | True | steps, required_documents | topic, preconditions, steps, required_documents, deadline_minutes, outcome | deadline_minutes, outcome, preconditions, topic |
| procedure-en-clean_new | True | steps, required_documents | topic, steps, required_documents | topic |
| procedure-en-sentence_noise | True | steps, required_documents | steps, required_documents |  |
| policy-th-clean_new | True | decision, exceptions | decision, conditions_all, exceptions | conditions_all, consequence, details |
| policy-th-sentence_noise | True | decision, exceptions | decision, conditions_all, exceptions | conditions_all, consequence, details |
| policy-en-clean_new | True | decision, exceptions | exceptions, decision | conditions_all, consequence, details |
| policy-en-sentence_noise | True | decision, exceptions | decision, subject, exceptions | conditions_all, consequence, details, subject |
| facility-th-clean_new | True | location, accessibility | location, accessibility |  |
| facility-th-sentence_noise | True | location, accessibility | location, accessibility |  |
| facility-en-clean_new | True | location, accessibility | accessibility, location |  |
| facility-en-sentence_noise | True | location, accessibility | accessibility, location |  |
| game_service-th-clean_new | True | offered, game_version | offered, game_version |  |
| game_service-th-sentence_noise | True | offered, game_version | offered, game_version |  |
| game_service-en-clean_new | True | offered, game_version | offered, game_version |  |
| game_service-en-sentence_noise | True | offered, game_version | offered, game_version |  |
| game_mode-th-clean_new | True | players_min, players_max | players_min, players_max |  |
| game_mode-th-sentence_noise | True | players_min, players_max | players_min, players_max |  |
| game_mode-en-clean_new | True | players_min, players_max | players_min, players_max |  |
| game_mode-en-sentence_noise | True | players_min, players_max | players_min, players_max |  |
| control_set-th-clean_new | True | bindings | bindings |  |
| control_set-th-sentence_noise | True | bindings | bindings |  |
| control_set-en-clean_new | True | bindings | bindings |  |
| control_set-en-sentence_noise | True | bindings | bindings |  |
| rate-th-clean_new | True | amount_minor, unit | unit, amount_minor | audience_id, calculation_rule, currency, duration_minutes, persons_max, persons_min, service_id, tax_note |
| rate-th-sentence_noise | True | amount_minor, unit | amount_minor | audience_id, calculation_rule, currency, duration_minutes, persons_max, persons_min, service_id, tax_note |
| rate-en-clean_new | True | amount_minor, unit | amount_minor, currency, unit | audience_id, calculation_rule, currency, duration_minutes, persons_max, persons_min, service_id, tax_note |
| rate-en-sentence_noise | True | amount_minor, unit | amount_minor, currency, unit | audience_id, calculation_rule, currency, duration_minutes, persons_max, persons_min, service_id, tax_note |
| rental_package-th-clean_new | True | equipment_included, amount_minor | equipment_included, amount_minor, currency | audience_id, currency, duration_minutes, name, period_label, room_seats, terms, zone_ids |
| rental_package-th-sentence_noise | True | equipment_included, amount_minor | equipment_included, amount_minor, currency | audience_id, currency, duration_minutes, name, period_label, room_seats, terms, zone_ids |
| rental_package-en-clean_new | True | equipment_included, amount_minor | equipment_included, amount_minor, currency | audience_id, currency, duration_minutes, name, period_label, room_seats, terms, zone_ids |
| rental_package-en-sentence_noise | True | equipment_included, amount_minor | equipment_included, amount_minor | audience_id, currency, duration_minutes, name, period_label, room_seats, terms, zone_ids |
| schedule-th-clean_new | True | open_periods, bookable_periods | open_periods, bookable_periods |  |
| schedule-th-sentence_noise | True | open_periods, bookable_periods | open_periods, bookable_periods |  |
| schedule-en-clean_new | True | open_periods, bookable_periods | open_periods, bookable_periods |  |
| schedule-en-sentence_noise | True | open_periods, bookable_periods | open_periods, bookable_periods |  |
| closure-th-clean_new | True | state, reason | reason, state |  |
| closure-th-sentence_noise | True | state, reason | reason, state |  |
| closure-en-clean_new | True | state, reason | state, reason |  |
| closure-en-sentence_noise | True | state, reason | state, reason |  |
| competition-th-clean_new | True | rulebook_release, competition_dates | competition_dates, rulebook_release |  |
| competition-th-sentence_noise | True | rulebook_release, competition_dates | competition_dates, rulebook_release |  |
| competition-en-clean_new | True | rulebook_release, competition_dates | competition_dates, rulebook_release |  |
| competition-en-sentence_noise | True | rulebook_release, competition_dates | competition_dates, rulebook_release |  |
| competition_rule-th-clean_new | True | text, completeness | text, completeness |  |
| competition_rule-th-sentence_noise | True | text, completeness | text, completeness |  |
| competition_rule-en-clean_new | True | text, completeness | text, completeness |  |
| competition_rule-en-sentence_noise | True | text, completeness | text, completeness |  |
| news-th-clean_new | True | body, event_start, event_end | title, body, event_start, event_end | title |
| news-th-sentence_noise | True | body, event_start, event_end | title, body, event_start, event_end | title |
| news-en-clean_new | True | body, event_start, event_end | body, event_start, event_end |  |
| news-en-sentence_noise | True | body, event_start, event_end | body, event_start, event_end |  |
| person-th-clean_new | True | role, public_contact_id | role, public_contact_id |  |
| person-th-sentence_noise | True | role, public_contact_id | role, team, public_contact_id, public_scope | public_scope, team |
| person-en-clean_new | True | role, public_contact_id | role, public_contact_id |  |
| person-en-sentence_noise | True | role, public_contact_id | role, public_contact_id |  |
| faq-th-clean_new | True | answer, scope_note | question, scope_note, answer | question |
| faq-th-sentence_noise | True | answer, scope_note | question, topic, scope_note, answer | question, topic |
| faq-en-clean_new | True | answer, scope_note | question, scope_note, answer | question |
| faq-en-sentence_noise | True | answer, scope_note | question, scope_note, answer | question |
| live_binding-th-clean_new | True | status_mapping, freshness_policy | status_mapping, freshness_policy |  |
| live_binding-th-sentence_noise | True | status_mapping, freshness_policy | status_mapping, freshness_policy |  |
| live_binding-en-clean_new | True | status_mapping, freshness_policy | status_mapping, freshness_policy |  |
| live_binding-en-sentence_noise | True | status_mapping, freshness_policy | status_mapping, freshness_policy |  |
| negative-service-th | True | session_minutes | session_minutes |  |
| negative-service-en | True | session_minutes | session_minutes |  |
| context-audience-th | True | required_proofs | required_proofs |  |
| context-audience-en | True | required_proofs | required_proofs |  |
