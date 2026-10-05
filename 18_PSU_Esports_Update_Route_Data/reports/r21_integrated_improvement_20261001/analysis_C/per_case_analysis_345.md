# วิเคราะห์รายข้อ: r20 failures → r21

ครอบคลุม noisy failures เดิม 345 ข้อ โดยแยก trace-confirmed cause ออกจากสมมติฐานที่ยังต้องตรวจ source เพิ่ม คำตอบ clean เป็น reference output ของระบบเดิม ไม่ใช่ human gold โดยอัตโนมัติ

คะแนน shortcut เป็นค่าของ branch; candidate score เป็นคะแนนจัดอันดับ ไม่ใช่ความน่าจะเป็นว่าคำตอบถูก เกณฑ์ legacy/v2 และ source semantics แยกกัน

## MASTER-GT-TH-03957 — studio_rules_penalties

- Priority: P2 source/ambiguity/label review
- Evidence: trace_code_source_inspected
- คำถาม: ถามแบบตรง ๆ นะ กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า ออัดวิดีโอในศูนย์ได้ไหม
- Legacy expected: ['no_answer', 'overview', 'rules']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: Standard safe no_answer satisfies status but general route is absent from expected route set. Route-label failure needs review, not forcing unsupported recording policy.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-02083 — games_catalog_availability

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: ขอสอบถามหน่อยครับ มั Counter-Strike 2 ไหม
- Legacy expected: ['games']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.56; source IDs=['Reservation']
- Top candidate: structured.games; score=0.999; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=games; structured_operation_priority; question_frame_domain_match; question_frame_operation=game_detail; precondition=game_domain_or_catalog_query
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ได้ครับ Counter-Strike 2 เล่นได้ที่ PC Zone - PC #01-#02, PC Zone - PC #03-#10
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "Counter-Strike 2",
    "PC #01-#02",
    "PC"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-04785 — compound_context_boundary

- Priority: P0 wrong task/target or omitted facet
- Evidence: trace_code_source_inspected
- คำถาม: อันนี้จอได้มั้ย
- Legacy expected: ['clarification', 'general', 'reservation']; clarification_required
- ก่อนแก้: pipeline:structured_equipment_catalog; confidence=0.96; source IDs=['home_equipment']
- Top candidate: structured.equipment; score=0.856; reason=base=0.88; domain_match; answer_type_match; question_frame_domain_match; question_frame_operation=equipment_lookup; precondition=equipment_preconditions_passed
- สาเหตุ/ขอบเขตการยืนยัน: Ambiguous anaphora อันนี้ persists; จอง becomes จอ and broad equipment handler returns all inventory. Clean also answers booking without identifying referent.
- หลังแก้: pipeline:structured_equipment_catalog; frozen pass=False

### คำตอบก่อนแก้

อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ขั้นตอนจองโดยสรุป:
•    เลือกบริการหรือโซนที่ต้องการใช้
•    เลือกวันและรอบเวลาที่ต้องการ
•    กรอก Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล และเบอร์โทรศัพท์
•    ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง
•    หลังจองต้องชำระเงินภายใน 10 นาที
•    แนบสลิปและยืนยันการจอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04959 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: อธิบายคำว่า latency ในรพบบคอมพิวเตอร์แบบสั้น ๆ อแบบเข้าใจง่าย
- Legacy expected: ['general', 'knowledge']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.763; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "latency",
    "หน่วง"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04758 — compound_context_boundary

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: ขอข้อมูลเรื่องส่งเครื่องงเกมไปบ้าน
- Legacy expected: ['no_answer']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.56; source IDs=['Reservation']
- Top candidate: structured.equipment; score=0.836; reason=base=0.88; answer_type_match; tool_router_action=structured; question_frame_domain_match; question_frame_operation=equipment_lookup; precondition=equipment_preconditions_passed
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-01285 — schedule_calendar

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า ตอนนี้ศูนย์ปเิดไหม
- Legacy expected: ['reservation', 'schedule']; live_lookup_required
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ศูนย์ปิดให้บริการตามวันหยุดราชการ/วันปิดพิเศษที่ระบุไว้ในระบบ

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04611 — members_overview_contact

- Priority: P1 task/qualifier or English evidence
- Evidence: trace_code_source_inspected
- คำถาม: นางาาวกมลวรรณ นวลสาย ทำำแหน่งอะไร
- Legacy expected: ['members', 'overview']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: Damaged person prefix and operation remain unchanged; operation=unknown; hybrid candidate 0.433 below 0.45; member capability rejected by general-route veto. Generic clarification omits known person topic.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

นางสาวกมลวรรณ นวลสาย: กรรมการ
หมวด: PSU Phuket Esports Club - PSU Phuket
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "กรรมการ",
    "นางสาวกมลวรรณ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-03292 — game_controls

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ROV มีปุ่มให้เล่นในศูยน์ไหม
- Legacy expected: ['clarification', 'games', 'no_answer']; answer_available
- ก่อนแก้: pipeline:game_control_missing_game_context; confidence=0.84; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:game_control_missing_game_context; frozen pass=False

### คำตอบก่อนแก้

ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน
ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III
เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน
ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III
เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

### คำตอบหลังแก้

ขอชื่อเกมก่อนครับ ยังไม่แน่ใจว่าหมายถึงเกมไหน จึงไม่ขอดึงปุ่มหรือวิธีเล่นของเกมอื่นมาตอบแทน
ตัวอย่างเกมที่มีข้อมูลปุ่มแล้ว: TEKKEN 8, Mario Kart 8 Deluxe, Call of Duty: Modern Warfare III
เช่น `TEKKEN 8 มีปุ่มอะไรบ้าง` หรือ `Mario Kart 8 Deluxe กดอะไร`

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "ยังไม่แน่ใจ",
    "ยังไม่พบ",
    "ขอ",
    "ไม่มี"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-04564 — members_overview_contact

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ใคีดูแลศูนย อะ
- Legacy expected: ['members', 'overview']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ผมอาจอ่านคำนี้ได้ไม่ครบครับ ต้องการถามเรื่องไหน: เกมหรืออุปกรณ์, ราคา, การจอง, เวลาเปิด-ปิด, กฎ หรือถามเกี่ยวกับแชทบอทนี้ครับ?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### คำตอบหลังแก้

ผมอาจอ่านคำนี้ได้ไม่ครบครับ ต้องการถามเรื่องไหน: เกมหรืออุปกรณ์, ราคา, การจอง, เวลาเปิด-ปิด, กฎ หรือถามเกี่ยวกับแชทบอทนี้ครับ?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-02611 — game_detail

- Priority: P2 source/ambiguity/label review
- Evidence: trace_code_source_inspected
- คำถาม: กำลงวางแผนไปใช้บริการ เลยอยากทราบว่า Counter-Strike 2 เล่นได้ที่โซนไหน
- Legacy expected: ['games']; answer_available
- ก่อนแก้: pipeline:structured_service_game_availability_no_match; confidence=0.91; source IDs=['availability_ps5_01_02', 'availability_pc_01_02', 'availability_pc_03_10']
- Top candidate: structured.games; score=0.999; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=games; question_frame_domain_match; question_frame_operation=game_detail; precondition=game_domain_or_catalog_query
- สาเหตุ/ขอบเขตการยืนยัน: Clean also fails: helper source probe maps polite เลย to เพลย์0.857>0.84; local zone resolver inserts PS5 although central game target and sources point PC.
- หลังแก้: pipeline:structured_service_game_availability; frozen pass=True

### คำตอบก่อนแก้

PlayStation 5 #01-#02 ไม่มี Counter-Strike 2 ครับ
Counter-Strike 2 เล่นได้ที่ PC #01-#02, PC #03-#10

เกมที่มีใน PlayStation 5 #01-#02:
•    Call of Duty: Modern Warfare III
•    Delta Force
•    EA Sports FC 24
•    eFootball
•    FINAL FANTASY XVI
•    Fortnite
•    God of War Ragnarok
•    Hogwarts Legacy
•    Marvel's Spider-Man 2
•    NARUTO X BORUTO Ultimate Ninja Storm Connections
•    Resident Evil 4
•    Resident Evil Village
•    TEKKEN 8
•    THE FINALS
•    The Last of Us Part I
•    The Last of Us Part II (Remastered)
•    Uncharted: Legacy of Thieves Collection
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

PlayStation 5 #01-#02 ไม่มี Counter-Strike 2 ครับ
Counter-Strike 2 เล่นได้ที่ PC #01-#02, PC #03-#10

เกมที่มีใน PlayStation 5 #01-#02:
•    Call of Duty: Modern Warfare III
•    Delta Force
•    EA Sports FC 24
•    eFootball
•    FINAL FANTASY XVI
•    Fortnite
•    God of War Ragnarok
•    Hogwarts Legacy
•    Marvel's Spider-Man 2
•    NARUTO X BORUTO Ultimate Ninja Storm Connections
•    Resident Evil 4
•    Resident Evil Village
•    TEKKEN 8
•    THE FINALS
•    The Last of Us Part I
•    The Last of Us Part II (Remastered)
•    Uncharted: Legacy of Thieves Collection
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ได้ครับ Counter-Strike 2 เล่นได้ที่ PC Zone - PC #01-#02, PC Zone - PC #03-#10
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "PC Zone"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-01773 — games_catalog_availability

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ถ้าจะเล่น Call of Duty ต้องจองอไร
- Legacy expected: ['games', 'reservation']; answer_available
- ก่อนแก้: pipeline:structured_booking_game_family_clarification; confidence=0.94; source IDs=['availability_pc_01_02', 'availability_pc_03_10', 'availability_ps5_01_02', 'availability_nintendo_1_2', 'availability_nintendo_1_4', 'availability_cockpit_01_02', 'availability_vr_30', 'availability_vr_60']
- Top candidate: structured.reservation; score=0.999; reason=base=0.86; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=reservation; question_frame_domain_match; question_frame_operation=booking_lookup; precondition=reservation_or_booking_query
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:structured_booking_game_family_clarification; frozen pass=False

### คำตอบก่อนแก้

Call of Duty ในข้อมูลตอนนี้มีมากกว่า 1 เกมครับ ต้องเลือกให้ตรงกับเกมที่จะเล่น
•    ถ้าหมายถึง Call of Duty: Modern Warfare III ให้จอง PlayStation 5 #01-#02
•    ถ้าหมายถึง Call of Duty: Warzone ให้จอง PC #03-#10
พิมพ์ต่อได้เลยว่า Warzone หรือ Modern Warfare III ถ้าต้องการให้ช่วยเจาะจง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Call of Duty ในข้อมูลตอนนี้มีมากกว่า 1 เกมครับ ต้องเลือกให้ตรงกับเกมที่จะเล่น
•    ถ้าหมายถึง Call of Duty: Modern Warfare III ให้จอง PlayStation 5 #01-#02
•    ถ้าหมายถึง Call of Duty: Warzone ให้จอง PC #03-#10
พิมพ์ต่อได้เลยว่า Warzone หรือ Modern Warfare III ถ้าต้องการให้ช่วยเจาะจง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

Call of Duty ในข้อมูลตอนนี้มีมากกว่า 1 เกมครับ ต้องเลือกให้ตรงกับเกมที่จะเล่น
•    ถ้าหมายถึง Call of Duty: Modern Warfare III ให้จอง PlayStation 5 #01-#02
•    ถ้าหมายถึง Call of Duty: Warzone ให้จอง PC #03-#10
พิมพ์ต่อได้เลยว่า Warzone หรือ Modern Warfare III ถ้าต้องการให้ช่วยเจาะจง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "PC #03-#10",
    "PC",
    "Call of Duty"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-04984 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: แปลคำวา่ reservation เป็นภาษาไทย ไม่ต้องยาว
- Legacy expected: ['general', 'knowledge', 'no_answer']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.759; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "จอง"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03994 — studio_rules_penalties

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ช่วยอธิบายให้เข้าใจงา่ยหน่อยว่า ขอข้อมูลเรื่องเล่นพนัน
- Legacy expected: ['rules']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.763; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04776 — compound_context_boundary

- Priority: P0 wrong task/target or omitted facet
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: กำลังวางแผนจะไปใช้บริกร พอดีอยากรู้ว่า อันนั้นใช้อะไรเล่ย
- Legacy expected: ['clarification', 'equipment', 'games', 'general']; clarification_required
- ก่อนแก้: pipeline:structured_equipment_catalog; confidence=0.95; source IDs=['home_equipment']
- Top candidate: structured.equipment; score=0.856; reason=base=0.88; domain_match; tool_router_domain=equipment; question_frame_domain_match; question_frame_operation=equipment_lookup; precondition=equipment_preconditions_passed
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:structured_equipment_catalog; frozen pass=False

### คำตอบก่อนแก้

อุปกรณ์ใน PlayStation 5 Zone:
PlayStation 5 Zone / VR Zone
•    PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive (2 Units in PlayStation 5 Zone and 1 Unit in VR Zone)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### คำตอบหลังแก้

อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-01160 — live_booking

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: สอบถามครับ PC #02 มี Call of Duty: Warzone หไม
- Legacy expected: ['games', 'reservation', 'schedule']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.56; source IDs=['Reservation']
- Top candidate: structured.games; score=0.999; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=games; question_frame_domain_match; question_frame_operation=game_detail; precondition=game_domain_or_catalog_query
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

PC #01-#02 ไม่มี Call of Duty: Warzone ครับ
Call of Duty: Warzone เล่นได้ที่ PC #03-#10

เกมที่มีใน PC #01-#02:
•    TEKKEN 8
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    VALORANT
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "ไม่มี",
    "PC #03-#10"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-04958 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: server กับ client ต่างกนยัวไง ตอบสั้น ๆ
- Legacy expected: ['general', 'knowledge', 'no_answer']; no_answer_expected
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "server",
    "client"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-00024 — service_fee

- Priority: P1 task/qualifier or English evidence
- Evidence: trace_code_source_inspected
- คำถาม: PC กับ VR อันไหนแพงกว่่า อะ
- Legacy expected: ['service_fee']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.456; reason=base=0.72; multi_domain; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: Comparison qualifier duplication removes comparison_intent; clean calculator0.999, noisy hybrid0.456; no anchored factual answer.
- หลังแก้: pipeline:deterministic_calculator_fast; frozen pass=True

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

PC 1 ชั่วโมง (1 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 25 บาท
•    General Adult: 70 บาท
หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27

VR 30 นาที (1-5 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 190 บาท
•    General Adult: 525 บาท

VR 1 ชั่วโมง (60 นาที, 1-5 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 375 บาท
•    General Adult: 1,050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### คำตอบหลังแก้

PC 1 ชั่วโมง (1 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 25 บาท
•    General Adult: 70 บาท
หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27

VR 30 นาที (1-5 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 190 บาท
•    General Adult: 525 บาท

VR 1 ชั่วโมง (60 นาที, 1-5 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 375 บาท
•    General Adult: 1,050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04569 — members_overview_contact

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ศูนย์์อยู่ที่ไหน
- Legacy expected: ['contact', 'overview']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=['Reservation']
- Top candidate: structured.equipment; score=0.789; reason=base=0.88; answer_type_match; question_frame_domain_match; question_frame_operation=equipment_lookup; precondition=equipment_preconditions_passed
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด contact ตอนนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด contact ตอนนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด contact ตอนนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04858 — compound_context_boundary

- Priority: P0 wrong task/target or omitted facet
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: Roblox เล่นได้ไม
- Legacy expected: ['games', 'general', 'no_answer']; no_answer_expected
- ก่อนแก้: pipeline:schedule_fast_path; confidence=0.96; source IDs=['Reservation']
- Top candidate: structured.schedule; score=0.926; reason=base=0.86; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=schedule; question_frame_domain_match; question_frame_operation=schedule_lookup; precondition=schedule_query_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:schedule_fast_path; frozen pass=False

### คำตอบก่อนแก้

เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน

รายละเอียดจากตาราง:
•    Morning คือ 09:00-12:00
•    Afternoon คือ 13:00-16:00
•    Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
•    Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
•    Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
•    Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบ Roblox ในรายการเกมที่ยืนยันได้ของ PSU Esports Studio - Phuket ครับ
ถ้าต้องการเล่นเกมนี้ ควรสอบถามเจ้าหน้าที่ก่อนจองหรือก่อนเข้าใช้บริการ

ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 42 เกมครับ

PC Zone (6 เกม)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 เกม)
•    Call of Duty: Modern Warfare III
•    Delta Force
•    EA Sports FC 24
•    eFootball
•    FINAL FANTASY XVI
•    Fortnite
•    God of War Ragnarok
•    Hogwarts Legacy
•    Marvel's Spider-Man 2
•    NARUTO X BORUTO Ultimate Ninja Storm Connections
•    Resident Evil 4
•    Resident Evil Village
•    TEKKEN 8
•    THE FINALS
•    The Last of Us Part I
•    The Last of Us Part II (Remastered)
•    Uncharted: Legacy of Thieves Collection

Nintendo Switch Zone (17 เกม)
•    Animal Crossing: New Horizons
•    It Takes Two
•    Little Nightmares II
•    Luigi's Mansion 3
•    Mario Kart 8 Deluxe
•    Mario Party Superstars
•    Monster Hunter Rise
•    Moving Out 2
•    New Super Mario Bros. U Deluxe
•    Nintendo Switch Sports
•    Overcooked!
•    Overcooked! 2
•    Pokémon Champions
•    Ring Fit Adventure
•    Super Mario Odyssey
•    Super Smash Bros Ultimate
•    The Legend of Zelda: Breath of The Wild

Cockpit Zone (1 เกม)
•    Gran Turismo 7

VR Zone (4 เกม)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### คำตอบหลังแก้

เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน

รายละเอียดจากตาราง:
•    Morning คือ 09:00-12:00
•    Afternoon คือ 13:00-16:00
•    Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
•    Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
•    Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
•    Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "ยังไม่พบ",
    "ไม่มี",
    "ไม่ได้อยู่",
    "ตอบจากข้อมูล"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-04989 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: อธิบายคำส่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ ขอ 1 ย่อหน้า
- Legacy expected: ['general', 'knowledge']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.763; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "latency",
    "หน่วง"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04761 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ขอขอมูลเรื้องเช่า notebook กลับบ้าน
- Legacy expected: ['no_answer']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=['Reservation']
- Top candidate: structured.reservation; score=0.999; reason=base=0.86; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=reservation; question_frame_domain_match; question_frame_operation=booking_lookup; precondition=reservation_or_booking_query
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ตอนจองต้องกรอก Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล, เบอร์โทรศัพท์ และคอมเมนต์ถ้ามี จากนั้นชำระเงินโดยโอนเข้าบัญชีธนาคารและแนบสลิปการโอนเงิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04795 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ขอข้อมูลที่ยืนยันได้หน่อยครับ: กติกา Valorant งานล่าสุดดใช้อะไร
- Legacy expected: ['clarification', 'competition_rules', 'general']; clarification_required
- ก่อนแก้: pipeline:competition_facet_not_covered_no_answer; confidence=0.92; source IDs=[]
- Top candidate: retrieval.competition_fact_cards; score=0.939; reason=base=0.82; domain_match; answer_type_match; tool_router_action=retrieval; tool_router_domain=competition_rules; competition_fact_card_priority; question_frame_domain_match; precondition=competition_rule_retrieval_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:competition_facet_not_covered_no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### คำตอบหลังแก้

ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-01159 — live_booking

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: สอบถมครับ PC #01 มี Call of Duty: Warzone ไหท
- Legacy expected: ['games', 'reservation', 'schedule']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.56; source IDs=['Reservation']
- Top candidate: structured.games; score=0.999; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=games; question_frame_domain_match; question_frame_operation=game_detail; precondition=game_domain_or_catalog_query
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

PC #01-#02 ไม่มี Call of Duty: Warzone ครับ
Call of Duty: Warzone เล่นได้ที่ PC #03-#10

เกมที่มีใน PC #01-#02:
•    TEKKEN 8
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    VALORANT
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "ไม่มี",
    "PC #03-#10"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-01257 — schedule_calendar

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: สัปดาห์นี้มีวันปิิดพิเศษไหม
- Legacy expected: ['reservation', 'schedule']; live_lookup_required
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00

รายละเอียดจากตาราง:
•    วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open
•    วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันพุธ: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันพฤหัสบดี: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันศุกร์: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = maintenance
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03602 — equipment

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: ช่วยตอบจากข้อมูลที่ยืนยันได้หน่อย: เอาคีย์บอร์ตดัวเองมาใช้ได้ไหม
- Legacy expected: ['equipment', 'rules']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.759; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-01876 — games_catalog_availability

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: New Super Mario Bros. U Deluxe เล่นได้ที่เครื่องไห
- Legacy expected: ['games']; answer_available
- ก่อนแก้: pipeline:ambiguity_clarification; confidence=0.74; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:ambiguity_clarification; frozen pass=False

### คำตอบก่อนแก้

คำถามนี้มีได้หลายความหมายครับ ขอระบุเพิ่มนิดหนึ่งว่าต้องการถามเรื่องไหน: อุปกรณ์, รายชื่อเกม/ข้อมูลเกม

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ได้ครับ New Super Mario Bros. U Deluxe เล่นได้ที่ Nintendo Switch Zone - Nintendo Switch (1-2 Persons), Nintendo Switch Zone - Nintendo Switch (1-4 Persons)
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

คำถามนี้มีได้หลายความหมายครับ ขอระบุเพิ่มนิดหนึ่งว่าต้องการถามเรื่องไหน: อุปกรณ์, รายชื่อเกม/ข้อมูลเกม

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "Nintendo Switch (1-2 Persons)",
    "Nintendo Switch",
    "New Super Mario Bros. U Deluxe"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-03502 — equipment

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ขอสบถาทหน่อยครับ VR Zone มีอะไรให้ใช้บ้าง
- Legacy expected: ['clarification', 'equipment']; answer_available
- ก่อนแก้: pipeline:ambiguity_clarification; confidence=0.78; source IDs=['our_games', 'home_equipment', 'service_fee_image_2026', 'reservation']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:ambiguity_clarification; frozen pass=False

### คำตอบก่อนแก้

คำถามนี้ยังตีได้หลายทางครับ หมายถึงเรื่องไหนของ VR Zone?

ข้อมูลย่อที่ยืนยันได้ตอนนี้:
•    เกม: มี 2 เกม เช่น Beat Saber, Horizon Call of the Mountain | พิมพ์ `VR มีเกมอะไรบ้าง`
•    อุปกรณ์: มี 1 รายการ เช่น Sony PlayStation VR2 | พิมพ์ `VR มีอุปกรณ์อะไรบ้าง`
•    ราคา: มีหลายแพ็กเกจตามเวลา/จำนวนผู้เล่น: VR 30 นาที (1-5 คน), VR 1 ชั่วโมง (1-5 คน) | พิมพ์ `VR ราคาเท่าไหร่`
•    จอง: ต้องจองผ่านระบบก่อนเข้าใช้ | พิมพ์ `VR จองยังไง`

พิมพ์ต่อสั้น ๆ ได้ เช่น `เกม`, `อุปกรณ์`, `ราคา` หรือ `จอง`

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

คำถามนี้ยังตีได้หลายทางครับ หมายถึงเรื่องไหนของ VR Zone?

ข้อมูลย่อที่ยืนยันได้ตอนนี้:
•    เกม: มี 2 เกม เช่น Beat Saber, Horizon Call of the Mountain | พิมพ์ `VR มีเกมอะไรบ้าง`
•    อุปกรณ์: มี 1 รายการ เช่น Sony PlayStation VR2 | พิมพ์ `VR มีอุปกรณ์อะไรบ้าง`
•    ราคา: มีหลายแพ็กเกจตามเวลา/จำนวนผู้เล่น: VR 30 นาที (1-5 คน), VR 1 ชั่วโมง (1-5 คน) | พิมพ์ `VR ราคาเท่าไหร่`
•    จอง: ต้องจองผ่านระบบก่อนเข้าใช้ | พิมพ์ `VR จองยังไง`

พิมพ์ต่อสั้น ๆ ได้ เช่น `เกม`, `อุปกรณ์`, `ราคา` หรือ `จอง`

### คำตอบหลังแก้

คำถามนี้ยังตีได้หลายทางครับ หมายถึงเรื่องไหนของ VR Zone?

ข้อมูลย่อที่ยืนยันได้ตอนนี้:
•    เกม: มี 2 เกม เช่น Beat Saber, Horizon Call of the Mountain | พิมพ์ `VR มีเกมอะไรบ้าง`
•    อุปกรณ์: มี 1 รายการ เช่น Sony PlayStation VR2 | พิมพ์ `VR มีอุปกรณ์อะไรบ้าง`
•    ราคา: มีหลายแพ็กเกจตามเวลา/จำนวนผู้เล่น: VR 30 นาที (1-5 คน), VR 1 ชั่วโมง (1-5 คน) | พิมพ์ `VR ราคาเท่าไหร่`
•    จอง: ต้องจองผ่านระบบก่อนเข้าใช้ | พิมพ์ `VR จองยังไง`

พิมพ์ต่อสั้น ๆ ได้ เช่น `เกม`, `อุปกรณ์`, `ราคา` หรือ `จอง`

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "อุปกรณ์",
    "หมายถึงเรื่องไหน",
    "Zone"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-03829 — studio_rules_penalties

- Priority: P1 task/qualifier or English evidence
- Evidence: trace_code_source_inspected
- คำถาม: อยากรู้ว่า ขอข้อมูลเรื่องทรัพย์สสินส่วนตัว สูญหาย
- Legacy expected: ['rules']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: Damaged policy noun misses direct protected policy; unknown operation, hybrid0.433 below0.45; no execution. Clean gives source-supported property-loss policy.
- หลังแก้: pipeline:protected_studio_rule_direct; frozen pass=True

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

กรุณาตรวจสอบทรัพย์สินของท่านทุกครั้งระหว่างการใช้บริการ หากมีการสูญหาย ศูนย์ขอสงวนสิทธิ์ไม่รับผิดชอบในทุกกรณี
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

กรุณาตรวจสอบทรัพย์สินของท่านทุกครั้งระหว่างการใช้บริการ หากมีการสูญหาย ศูนย์ขอสงวนสิทธิ์ไม่รับผิดชอบในทุกกรณี
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03808 — studio_rules_penalties

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: สอบถามครับ ขอข้อมูลเรื่องเสียหานเล็กน้อย
- Legacy expected: ['penalty']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ความเสียหายเล็กน้อย เช่น รอยเปื้อน คราบน้ำ รอยขีดข่วน ฝาปิดหลุด หรือปุ่มหลวม มีค่าปรับ 100–500 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04998 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: server กับ client ต่างกันยัไงง ขอ 1 ย่อหน้า
- Legacy expected: ['general', 'knowledge', 'no_answer']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.759; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "server",
    "client"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03868 — studio_rules_penalties

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ขอช้อมูลที่ยืนยันได้หน่อยครับ: อัดวิดีโอในศูนย์ได้ไหม ครับ
- Legacy expected: ['no_answer', 'overview', 'rules']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-00831 — reservation_policy

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: อง PS5 ต้องทำบังไง ช่วยแนบแหล่งข้อมูลด้วย
- Legacy expected: ['reservation']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

จอง PlayStation 5 ต้องเลือกบริการ PlayStation 5 และเลือกรอบเวลาที่ต้องการครับ
•    ข้อมูลค่าบริการที่มีระบุ PlayStation 5 ต่อ 60 นาที สำหรับ 1-2 คน
•    จากนั้นกรอกข้อมูลผู้ใช้บริการ ชำระเงิน และแนบสลิปเพื่อยืนยันการจอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "จอง",
    "เช็คอิน",
    "ชำระ",
    "session",
    "ยกเลิก"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-04963 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ช่วยสรุปวิธีพูดขอบคุณแบบสุภา 2 ผระโยค ขอแบบเข้าใจง่าย
- Legacy expected: ['general', 'knowledge', 'no_answer']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.759; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "ขอบคุณ"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04944 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: trace_code_source_inspected
- คำถาม: แปลคำวาา reservation เป็นภาษาไทย
- Legacy expected: ['general', 'knowledge', 'no_answer']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.759; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Expected no_answer plus required จอง does not match generic refusal. Needs scope/contract review; clean also fails, not caused solely by typo.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "จอง"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04949 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: อธิบายคำว่า latency ในระบบคอมพิวเตอร์แบบวั้น ๆ ตอบสั้น ๆ
- Legacy expected: ['general', 'knowledge']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.763; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "latency",
    "หน่วง"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-01517 — schedule_calendar

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: รบกวนเช็กข้อมูลของศูนย์ให้หนอยครับ สัปดาห์นี้มีวันปิกพิเศษไหม
- Legacy expected: ['reservation', 'schedule']; live_lookup_required
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00

รายละเอียดจากตาราง:
•    วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open
•    วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันพุธ: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันพฤหัสบดี: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันศุกร์: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = maintenance
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03826 — studio_rules_penalties

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: สอบถามครับ อัดวิีโอในศูนย์ได้มั้ย
- Legacy expected: ['no_answer', 'overview', 'rules']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-00110 — service_fee

- Priority: P0 wrong task/target or omitted facet
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Mario Party Superstars รคาเท่าๆหร่
- Legacy expected: ['service_fee']; answer_available
- ก่อนแก้: pipeline:structured_games_genre_list; confidence=0.95; source IDs=['our_games_genre']
- Top candidate: structured.games; score=0.999; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=games; question_frame_domain_match; question_frame_operation=game_detail; precondition=game_domain_or_catalog_query
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:structured_games_genre_list; frozen pass=False

### คำตอบก่อนแก้

เกมแนว Party / Co-op ที่พบในรายการเกมที่ยืนยันได้:

It Takes Two
•    แนวเกม: เกม Co-op Adventure
•    เล่นได้ที่: Nintendo Switch Zone

Mario Kart 8 Deluxe
•    แนวเกม: เกมแข่งรถ Party Racing
•    เล่นได้ที่: Nintendo Switch Zone

Mario Party Superstars
•    แนวเกม: เกม Party / Mini-games
•    เล่นได้ที่: Nintendo Switch Zone

Moving Out 2
•    แนวเกม: เกม Co-op Puzzle / Party
•    เล่นได้ที่: Nintendo Switch Zone

Overcooked! 2
•    แนวเกม: เกม Co-op ทำอาหาร
•    เล่นได้ที่: Nintendo Switch Zone
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Mario Party Superstars ไม่มีราคาแยกตามชื่อเกมครับ ต้องดูราคาตามโซน/บริการที่ใช้เล่นเกมนี้

Nintendo Switch Zone
ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคา Nintendo Switch ทุกกลุ่มให้เทียบก่อน

Nintendo Switch 1 ชั่วโมง (1-2 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU: 0 บาท
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท
•    บุคคลทั่วไป (General Adult): 140 บาท

Nintendo Switch 1 ชั่วโมง (3-4 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU: 0 บาท
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 100 บาท
•    บุคคลทั่วไป (General Adult): 280 บาท
หมายเหตุ: คำถามยังไม่ระบุจำนวนผู้เล่น จึงแสดงทั้งราคา 1-2 คนและ 3-4 คน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### คำตอบหลังแก้

เกมแนว Party / Co-op ที่พบในรายการเกมที่ยืนยันได้:

It Takes Two
•    แนวเกม: เกม Co-op Adventure
•    เล่นได้ที่: Nintendo Switch Zone

Mario Kart 8 Deluxe
•    แนวเกม: เกมแข่งรถ Party Racing
•    เล่นได้ที่: Nintendo Switch Zone

Mario Party Superstars
•    แนวเกม: เกม Party / Mini-games
•    เล่นได้ที่: Nintendo Switch Zone

Moving Out 2
•    แนวเกม: เกม Co-op Puzzle / Party
•    เล่นได้ที่: Nintendo Switch Zone

Overcooked! 2
•    แนวเกม: เกม Co-op ทำอาหาร
•    เล่นได้ที่: Nintendo Switch Zone
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [
    "Mario Party Superstars"
  ],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-00542 — reservation_policy

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ข่วยตอบจากข้อมูลที่ยืนยันได้หน่อย: ขอข้อมูลเรื่องได้เงินคืน
- Legacy expected: ['reservation']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04796 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: กำลังวางแผนจะไปมช้บริการ พอดอยากรู้ว่า กติกา Valorant งานล่าสุดใช้อะไร
- Legacy expected: ['clarification', 'competition_rules', 'general']; clarification_required
- ก่อนแก้: pipeline:competition_facet_not_covered_no_answer; confidence=0.92; source IDs=[]
- Top candidate: retrieval.competition_fact_cards; score=0.939; reason=base=0.82; domain_match; answer_type_match; tool_router_action=retrieval; tool_router_domain=competition_rules; competition_fact_card_priority; question_frame_domain_match; precondition=competition_rule_retrieval_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:competition_facet_not_covered_no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### คำตอบหลังแก้

ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04546 — members_overview_contact

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ขอข้อมูลเรื่องหน่วยวาน ดำเนนการ
- Legacy expected: ['overview']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

สมาชิกจากหน้า Members แยกตามหมวด รวม 25 คน:
Members (7 คน):
•    ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี
•    รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี
•    รศ.ดร.อซีส นันทอมรพงศ์: คณบดี
•    ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ
•    นายพฤทธิ์ เกษตรสมบูรณ์: นักวิชาการคอมพิวเตอร์
•    นายณัฐวัฒน์ นิธิคุณานนต์: นักวิชาการคอมพิวเตอร์
•    นายชนะชัย สิริพันธ์วราภรณ์: ผู้จัดการ

cooperative education and Internship student (5 คน):
•    นายณภัทร เชื้อเหล่าวานิช: นักศึกษาสหกิจ Game and 3D Developer
•    Mr. Amine Abidellaoui: Internship Student
•    นายสุพศิน อะนะฝรั่ง: นักศึกษาสหกิจ Web & AI Developer
•    Mr. Yanis Igoudjil: Internship Student
•    นายภาสวุฒิ ชูติประชากิจ: นักศึกษาฝึกงานโครงการ Super AI SS6 ตำแหน่ง AI Chat Bot Developer

PSU Phuket Esports Club - PSU Phuket (13 คน):
•    นายษุภากรณ์ จิราจินดากุล: ประธาน
•    นายนพัทธ์ ฝอยทอง: รองประธาน
•    นายปัณณวิชญ์ หนูเรือง: เลขานุการ
•    นายภูจิตร จิรวิริยาภรณ์: เหรัญญิก
•    นายธนชาติ เอ่งฉ้วน: ประชาสัมพันธ์
•    นางสาวกมลวรรณ นวลสาย: กรรมการ
•    นางสาวชญาภา จันทร์เอิบ: กรรมการ
•    นางสาวณัฐธิดา คำทะเนตร์: กรรมการ
•    นางสาวสุภาสินี ธนภพ: กรรมการ
•    นางสาวอาทิตยา แดงประดับ: กรรมการ
•    นายณัฐพนธ์ อินทรสังขนาวิน: กรรมการ
•    นายอภิวิชญ์ เลิศกมลรักษ์: กรรมการ
•    นายอรรถนนท์ สุขแก้ว: กรรมการ
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-02213 — game_detail

- Priority: P0 wrong task/target or omitted facet
- Evidence: trace_code_source_inspected
- คำถาม: EA Sports FC 24 คือเดมอะร
- Legacy expected: ['games']; answer_available
- ก่อนแก้: pipeline:structured_games_genre_list; confidence=0.95; source IDs=['our_games_genre']
- Top candidate: structured.games; score=0.999; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=games; question_frame_domain_match; question_frame_operation=game_detail; precondition=game_domain_or_catalog_query
- สาเหตุ/ขอบเขตการยืนยัน: Title exact but detail cue corrupted; substring Sports in title drives genre list; source-backed facts do not answer requested game detail.
- หลังแก้: pipeline:structured_game_detail; frozen pass=True

### คำตอบก่อนแก้

เกมแนว Sports / เกมกีฬา ที่พบในรายการเกมที่ยืนยันได้:

EA Sports FC 24
•    แนวเกม: เกมฟุตบอล
•    เล่นได้ที่: PlayStation 5 Zone

Nintendo Switch Sports
•    แนวเกม: เกมกีฬา Motion Control
•    เล่นได้ที่: Nintendo Switch Zone
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

EA Sports FC 24: EA Sports FC 24 คือเกมฟุตบอลที่ให้ผู้เล่นควบคุมทีม แข่งขัน ยิงประตู และวางแผนเกมเหมือนการแข่งขันฟุตบอล
แนวเกม: เกมฟุตบอล
วิธีเล่นโดยสรุป: เลือกทีม จัดตัว ควบคุมการส่งบอล เลี้ยง ยิง และตั้งรับเพื่อทำประตูให้มากกว่าคู่แข่ง
เล่นได้ที่: PlayStation 5 Zone
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### คำตอบหลังแก้

EA Sports FC 24: EA Sports FC 24 คือเกมฟุตบอลที่ให้ผู้เล่นควบคุมทีม แข่งขัน ยิงประตู และวางแผนเกมเหมือนการแข่งขันฟุตบอล
แนวเกม: เกมฟุตบอล
วิธีเล่นโดยสรุป: เลือกทีม จัดตัว ควบคุมการส่งบอล เลี้ยง ยิง และตั้งรับเพื่อทำประตูให้มากกว่าคู่แข่ง
เล่นได้ที่: PlayStation 5 Zone
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "EA Sports FC 24 คือเกมฟุตบอลที่ให้ผู้เล่นควบคุมทีม แข่งขัน ยิงประตู และวางแผนเกมเหมือนการแข่งขันฟุตบอล"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-01617 — games_catalog_availability

- Priority: P0 wrong task/target or omitted facet
- Evidence: paired_regression_primary_cause_pending
- คำถาม: PC Zone รอบละกี่าที
- Legacy expected: ['games', 'reservation']; answer_available
- ก่อนแก้: pipeline:structured_equipment_item; confidence=0.95; source IDs=['equipment_gaming_pc']
- Top candidate: structured.equipment; score=0.836; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=equipment; structured_operation_priority; question_frame_domain_match; precondition=equipment_preconditions_passed
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:structured_service_duration; frozen pass=True

### คำตอบก่อนแก้

Gaming PC รุ่น MSI MAG Infinite S3 14th: เครื่องคอมพิวเตอร์เกมมิ่งของ PC Zone สำหรับเล่นเกมบนคอมและฝึกซ้อมอีสปอร์ต
จำนวน: 10 Units
อยู่ที่: PC Zone
ใช้สำหรับ:
•    เล่น VALORANT
•    เล่น Counter-Strike 2
•    เล่น PUBG: BATTLEGROUNDS
•    เล่น Call of Duty: Warzone
•    เล่น TEKKEN 8
•    เล่น League of Legends
หมายเหตุ: สเปกที่บันทึกไว้ในโปรเจกต์: Intel Core i5-14400, RAM DDR5 32GB, NVIDIA GeForce RTX 5060 8GB
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

PC Zone มีรอบ 60 นาทีในระบบจองครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

PC Zone มีรอบ 60 นาทีในระบบจองครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "TEKKEN 8",
    "Counter-Strike 2",
    "League of Legends",
    "60"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04674 — members_overview_contact

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ขอสอบถามหน่อยครับ นายณัฐพนธ์ อินทรสังขนาวิน มีตำแหน้งอะไร
- Legacy expected: ['members', 'overview']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

นายณัฐพนธ์ อินทรสังขนาวิน: กรรมการ
หมวด: PSU Phuket Esports Club - PSU Phuket
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "นายณัฐพนธ์ อินทรสังขนาวิน",
    "กรรมการ"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04571 — members_overview_contact

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: กำลังวางแผนจะไปใช้บริการ พอดีอยากร้ว่า ศูนย์อยู่ทร่ไหน
- Legacy expected: ['contact', 'overview']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด contact ตอนนี้ครับ

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-00558 — reservation_policy

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ช่วยตอบจากข้อมูลที่ยืนยันได้หน่อย: ขอข้อมูลที่ยืนยันได้หน่อยครับ: ไปถึงแล้วต้องเ็ชกอินไหม
- Legacy expected: ['reservation']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ต้องเช็กอินครับ ให้เช็กอินก่อนเวลาเริ่มรอบที่จอง โดยเช็กอินล่วงหน้าได้สูงสุด 30 นาที และแสดงบัตรนักศึกษา บัตรบุคลากร หรือบัตรประชาชน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-01666 — games_catalog_availability

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Counter-Strike 2 เป็นเกมแนไวหน
- Legacy expected: ['games']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.56; source IDs=['Reservation']
- Top candidate: structured.games; score=0.999; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=games; structured_operation_priority; question_frame_domain_match; question_frame_operation=game_detail; precondition=game_domain_or_catalog_query
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Counter-Strike 2: Counter-Strike 2 คือเกมยิงแข่งขันแบบทีมที่แบ่งเป็นฝ่ายบุกและฝ่ายรับ โดยมีเป้าหมายหลักเกี่ยวกับการวาง/กู้ระเบิดหรือจัดการฝ่ายตรงข้าม
แนวเกม: เกมยิง Tactical FPS
วิธีเล่นโดยสรุป: เล่นเป็นรอบ ๆ ต้องซื้ออาวุธ วางแผนกับทีม คุมพื้นที่ และใช้การเล็งกับการสื่อสารเพื่อชนะรอบ
เล่นได้ที่: PC Zone
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "แนวเกม",
    "เกมยิง Tactical FPS"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-04967 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: GPU คืออะไรแบบเข้าใจง่าย ขอแบบเขข้าใจง่าย
- Legacy expected: ['general', 'knowledge']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.763; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "GPU",
    "กราฟิก"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04647 — members_overview_contact

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ขอสอบถามหน่อยครับ นายชนะชัย สิริพันธ์วราภรณ์ มีตแหน่งอะไร
- Legacy expected: ['members', 'overview']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

นายชนะชัย สิริพันธ์วราภรณ์: ผู้จัดการ
หมวด: Members
สังกัด/รายละเอียด: PSU Esports Studio - Phuket วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "นายชนะชัย สิริพันธ์วราภรณ์",
    "ผู้จัดการ"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03773 — studio_rules_penalties

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ขอขอมูลเรื่องสูบบุหรีา ขอรายละเอียดแบบสั้น ๆ
- Legacy expected: ['rules']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03758 — studio_rules_penalties

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: รบกวนเช็กข้อมูลของศูนย์ให้หน่อยครับ ขอข้อมูลที่ยืนนยันได้หน่อยครับ: อัดวิดีโอในศูนย์ได้ไหม
- Legacy expected: ['no_answer', 'overview', 'rules']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03935 — studio_rules_penalties

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ขอข้อมูลล่าสุดที่ระบบยืนยันได้: กำลังวางแผนจะไปใช้บริการ พออดีอยากรู้ว่า อัดวิดีโอในศูนย์ได้ไหม
- Legacy expected: ['no_answer', 'overview', 'rules']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-00815 — reservation_policy

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: กำลังวางแผนจะไปใช้บริการ พดีอยากรู้ว่า ไปถึงแล้วต้องเข็กอินไหม ช่วยแนบแหล่งข้อมูลด้วย
- Legacy expected: ['reservation']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ต้องเช็กอินครับ ให้เช็กอินก่อนเวลาเริ่มรอบที่จอง โดยเช็กอินล่วงหน้าได้สูงสุด 30 นาที และแสดงบัตรนักศึกษา บัตรบุคลากร หรือบัตรประชาชน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03869 — studio_rules_penalties

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: กำลังวางแผนจะไปใช้บริการ พอดีอยากรูว่า อัดวิดีโอในศูนย์ได้ไหม ครับ
- Legacy expected: ['no_answer', 'overview', 'rules']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-00032 — service_fee

- Priority: P0 wrong task/target or omitted facet
- Evidence: trace_code_source_inspected
- คำถาม: บุคคลทั่วไป เล่น PC 30 นาที เสียกี่บบาท
- Legacy expected: ['service_fee']; answer_available
- ก่อนแก้: pipeline:protected_public_access; confidence=0.98; source IDs=['reservation_public_access_reviewed_20260924']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: entities.price_intent=True but protected exact price cue misses กี่บบาท; public-access returns before central scoring. Confirmed conflicting cue definitions and early return.
- หลังแก้: pipeline:deterministic_calculator_fast; frozen pass=True

### คำตอบก่อนแก้

ได้ครับ บุคคลทั่วไปสามารถจองใช้บริการ PC Zone ได้ ค่าบริการขึ้นกับประเภทบริการและกลุ่มผู้ใช้ ต้องจองผ่านระบบและแสดงบัตรประชาชนเมื่อเช็กอิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ระยะเวลาที่ถามคือ 30 นาที ใช้ 1 session ตามแพ็กเกจ PC 1 ชั่วโมง
คำตอบราคา: 70 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
•    คำนวณจาก 70 บาท/session x 1 session = 70 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
PC 1 ชั่วโมง (1 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 25 บาท
•    General Adult: 70 บาท
หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### คำตอบหลังแก้

ระยะเวลาที่ถามคือ 30 นาที ใช้ 1 session ตามแพ็กเกจ PC 1 ชั่วโมง
คำตอบราคา: 70 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
•    คำนวณจาก 70 บาท/session x 1 session = 70 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
PC 1 ชั่วโมง (1 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 25 บาท
•    General Adult: 70 บาท
หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "General Adult",
    "0 บาท"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-04986 — compound_context_boundary

- Priority: P0 wrong task/target or omitted facet
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: คีย์บอร์ด mechanical คทออะไรแบบสั้น ไม่ต้องยาว
- Legacy expected: ['general', 'knowledge', 'no_answer']; no_answer_expected
- ก่อนแก้: pipeline:structured_equipment_catalog; confidence=0.96; source IDs=['home_equipment']
- Top candidate: structured.equipment; score=0.856; reason=base=0.88; domain_match; answer_type_match; question_frame_domain_match; question_frame_operation=equipment_lookup; precondition=equipment_preconditions_passed
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:structured_equipment_catalog; frozen pass=False

### คำตอบก่อนแก้

อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "คีย์บอร์ด",
    "mechanical"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04966 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: คีย์บอร์ด mechanical คืออะไรแบบบสั้น ขอแบบเข้าใจง่าย
- Legacy expected: ['general', 'knowledge', 'no_answer']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.763; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "คีย์บอร์ด",
    "mechanical"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-02613 — game_detail

- Priority: P0 wrong task/target or omitted facet
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า EA Sports FC 24 เล่นยังไงง
- Legacy expected: ['games']; answer_available
- ก่อนแก้: pipeline:structured_game_controls; confidence=0.96; source IDs=['game_controls_easportsfc24']
- Top candidate: structured.games; score=0.999; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=games; question_frame_domain_match; question_frame_operation=game_detail; precondition=game_domain_or_catalog_query
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:structured_game_controls; frozen pass=False

### คำตอบก่อนแก้

EA Sports FC 24 ปุ่มที่ตรงกับคำถาม:
PlayStation / PS5
•    L1: เปลี่ยนตัวผู้เล่น - สลับการควบคุมไปยังนักเตะคนอื่นที่อยู่ใกล้บอล
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://fifauteam.com/fc-24-controls/

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

EA Sports FC 24 ปุ่มที่ตรงกับคำถาม:
PlayStation / PS5
•    L1: เปลี่ยนตัวผู้เล่น - สลับการควบคุมไปยังนักเตะคนอื่นที่อยู่ใกล้บอล
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://fifauteam.com/fc-24-controls/

### คำตอบหลังแก้

EA Sports FC 24 ปุ่มที่ตรงกับคำถาม:
PlayStation / PS5
•    L1: เปลี่ยนตัวผู้เล่น - สลับการควบคุมไปยังนักเตะคนอื่นที่อยู่ใกล้บอล
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://fifauteam.com/fc-24-controls/

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "เลือกทีม จัดตัว ควบคุมการส่งบอล เลี้ยง ยิง และตั้งรับเพื่อทำประตูให้มากกว่าคู่แข่ง"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04556 — members_overview_contact

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: นาย้ปนไค อ
- Legacy expected: ['general', 'knowledge', 'overview']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ผมอาจอ่านคำนี้ได้ไม่ครบครับ ต้องการถามเรื่องไหน: เกมหรืออุปกรณ์, ราคา, การจอง, เวลาเปิด-ปิด, กฎ หรือถามเกี่ยวกับแชทบอทนี้ครับ?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ผมคือ PSU Esports Assistant แชทบอทผู้ช่วยของ PSU Esports Studio - Phuket ครับ

ผมช่วยตอบคำถามเกี่ยวกับ:
•    เกมที่มีให้เล่นและเกมที่เกี่ยวข้องกับการแข่งขัน
•    ปุ่มควบคุมและวิธีเล่นของเกมที่มีข้อมูลยืนยัน
•    อุปกรณ์และโซนบริการ เช่น PC, PS5, Nintendo Switch, VR และ Cockpit
•    วิธีจอง เช็คอิน ค่าบริการ เวลาเปิด-ปิด และกฎการใช้งาน
•    สมาชิกทีม ตำแหน่ง และหมวดสมาชิกของ PSU Esports Studio - Phuket

ถ้าเป็นข้อมูลของศูนย์ ผมจะตอบจากฐานข้อมูลที่ยืนยันได้ก่อนเสมอ ถ้ายังไม่มีข้อมูลยืนยัน ผมจะบอกตรง ๆ ครับ

### คำตอบหลังแก้

ผมอาจอ่านคำนี้ได้ไม่ครบครับ ต้องการถามเรื่องไหน: เกมหรืออุปกรณ์, ราคา, การจอง, เวลาเปิด-ปิด, กฎ หรือถามเกี่ยวกับแชทบอทนี้ครับ?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-00589 — reservation_policy

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ช่วยตอบจากข้อมูลที่ยืนยันได้หน่อย: ต้องแนบสลปิไหม
- Legacy expected: ['reservation']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ตอนจองต้องกรอก Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล เบอร์โทรศัพท์ และชำระโดยโอนเงินพร้อมแนบสลิป
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "จอง",
    "เช็คอิน",
    "ชำระ",
    "session",
    "ยกเลิก"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-04971 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: API คออะไร ตอบเป็นภาษาำทย
- Legacy expected: ['general', 'knowledge']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "API",
    "เชื่อมต่อ"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-01667 — games_catalog_availability

- Priority: P0 wrong task/target or omitted facet
- Evidence: trace_code_source_inspected
- คำถาม: PUBG: BATTLEGROUNDS เล่นได้ทที่ไหน
- Legacy expected: ['games']; answer_available
- ก่อนแก้: pipeline:schedule_fast_path; confidence=0.96; source IDs=['Reservation']
- Top candidate: structured.schedule; score=0.926; reason=base=0.86; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=schedule; question_frame_domain_match; question_frame_operation=schedule_lookup; precondition=schedule_query_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Broken เล่นได้ที่ไหน misses game availability operation; broad เล่นได้ hits schedule; score boosts repeat mistaken route/frame; schedule wins0.926.
- หลังแก้: pipeline:structured_service_game_availability; frozen pass=True

### คำตอบก่อนแก้

เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน

รายละเอียดจากตาราง:
•    Morning คือ 09:00-12:00
•    Afternoon คือ 13:00-16:00
•    Monday ช่วง Morning 09:00-12:00 เป็น Maintenance*
•    Monday ช่วง Afternoon 13:00-16:00 เป็น Open for Service
•    Tuesday-Thursday เปิดตามรอบปกติ 09:00-12:00 และ 13:00-16:00
•    Friday ช่วง Afternoon 13:00-16:00 เป็น Maintenance สำหรับ Weekly hardware inspection and cleaning
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ได้ครับ PUBG: BATTLEGROUNDS เล่นได้ที่ PC Zone - PC #01-#02, PC Zone - PC #03-#10
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ได้ครับ PUBG: BATTLEGROUNDS เล่นได้ที่ PC Zone - PC #01-#02, PC Zone - PC #03-#10
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "PC",
    "เล่นได้ที่"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-04968 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: server กับ client ต่างกัยยังไง ขอแบบเข้ใจง่าย
- Legacy expected: ['general', 'knowledge', 'no_answer']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "server",
    "client"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04946 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: คีย์บอ์ด mechanical คืออะไรแบบสั้น
- Legacy expected: ['general', 'knowledge', 'no_answer']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.759; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "คีย์บอร์ด",
    "mechanical"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04376 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: ขอสอบถามหน่อยครับ ตาม rulebook เคานน์เตอร์สไตรก์ 2 ขอบเขตและข้อมูลของรายการ ต้องทำยังไง
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:competition_target_clarification; confidence=0.97; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:competition_target_clarification; frozen pass=False

### คำตอบก่อนแก้

ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

คำตอบ: รายการ PSU Phuket CS2 2026 Tournament

รายละเอียดที่เกี่ยวข้อง:
•    1. ขอบเขตการบังคับใช้ กฎระเบียบนี้ใช้กับผู้เล่น ทีม และเจ้าหน้าที่ทุกคนที่เข้าร่วมการแข่งขัน CS2 อย่างเป็นทางการที่จัดโดย PSU Esports Studio - Phuket
•    1. ข้อมูลทั่วไป (General Information)

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### คำตอบหลังแก้

ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-00493 — reservation_policy

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ขอสอบถามหน่อยครับ ไปถึงแล้วต้องช็กอินไหม
- Legacy expected: ['reservation']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ต้องเช็กอินครับ ให้เช็กอินก่อนเวลาเริ่มรอบที่จอง โดยเช็กอินล่วงหน้าได้สูงสุด 30 นาที และแสดงบัตรนักศึกษา บัตรบุคลากร หรือบัตรประชาชน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04463 — competition_rules

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ขอสอบถามหน่อยครรับ ขออ้างอิงกติกา เทคเค่น 8 ในหัวข้อการตั้งค่าในเกม หน่อย
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:game_meta_clarification; confidence=0.74; source IDs=['our_games', 'Reservation']
- Top candidate: retrieval.competition_fact_cards; score=0.789; reason=base=0.82; answer_type_match; competition_fact_card_priority; question_frame_domain_match; precondition=competition_rule_retrieval_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:game_meta_clarification; frozen pass=False

### คำตอบก่อนแก้

ถามเรื่องเกมได้ครับ แต่คำถามนี้ยังกว้างเกินไป เลยไม่ขอดึงเกมใดเกมหนึ่งมาตอบแทน

ตัวอย่างที่ถามได้:
•    `มีเกมอะไรบ้าง`
•    `PS5 มีเกมอะไรบ้าง`
•    `TEKKEN 8 คือเกมอะไร`
•    `TEKKEN 8 มีปุ่มอะไรบ้าง`
•    `Nintendo Switch มีเกมแนวปาร์ตี้ไหม`

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ถามเรื่องเกมได้ครับ แต่คำถามนี้ยังกว้างเกินไป เลยไม่ขอดึงเกมใดเกมหนึ่งมาตอบแทน

ตัวอย่างที่ถามได้:
•    `มีเกมอะไรบ้าง`
•    `PS5 มีเกมอะไรบ้าง`
•    `TEKKEN 8 คือเกมอะไร`
•    `TEKKEN 8 มีปุ่มอะไรบ้าง`
•    `Nintendo Switch มีเกมแนวปาร์ตี้ไหม`

### คำตอบหลังแก้

ถามเรื่องเกมได้ครับ แต่คำถามนี้ยังกว้างเกินไป เลยไม่ขอดึงเกมใดเกมหนึ่งมาตอบแทน

ตัวอย่างที่ถามได้:
•    `มีเกมอะไรบ้าง`
•    `PS5 มีเกมอะไรบ้าง`
•    `TEKKEN 8 คือเกมอะไร`
•    `TEKKEN 8 มีปุ่มอะไรบ้าง`
•    `Nintendo Switch มีเกมแนวปาร์ตี้ไหม`

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-02316 — game_detail

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: PUBG เป็นเกมนแวไหน
- Legacy expected: ['games']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.56; source IDs=['Reservation']
- Top candidate: structured.games; score=0.978; reason=base=0.88; domain_match; answer_type_match; tool_router_domain=games; question_frame_domain_match; question_frame_operation=game_detail; precondition=game_domain_or_catalog_query
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

PUBG: BATTLEGROUNDS: PUBG: BATTLEGROUNDS คือเกมเอาชีวิตรอดที่ผู้เล่นลงสนาม ค้นหาอาวุธและอุปกรณ์ แล้วพยายามอยู่รอดเป็นคนหรือทีมสุดท้าย
แนวเกม: เกม Battle Royale
วิธีเล่นโดยสรุป: เลือกจุดลง หาอาวุธ เข้าโซนปลอดภัย วางตำแหน่ง และต่อสู้กับทีมอื่นจนเหลือผู้ชนะท้ายเกม
เล่นได้ที่: PC Zone
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "เกม Battle Royale",
    "PUBG",
    "แนว"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-04673 — members_overview_contact

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ขอสอบถามหน่อยครับ นางสาวอาทิตยา แดงประดับ มีำตแหน่งอะไร
- Legacy expected: ['members', 'overview']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

นางสาวอาทิตยา แดงประดับ: กรรมการ
หมวด: PSU Phuket Esports Club - PSU Phuket
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "นางสาวอาทิตยา แดงประดับ",
    "กรรมการ"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-01299 — schedule_calendar

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: เปืดกี่โง
- Legacy expected: ['reservation', 'schedule']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00

รายละเอียดจากตาราง:
•    วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open
•    วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันพุธ: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันพฤหัสบดี: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันศุกร์: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = maintenance
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "เปิด",
    "ปิด",
    "เวลา",
    "วัน",
    "ไม่เปิด"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-01260 — schedule_calendar

- Priority: P0 wrong task/target or omitted facet
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ตอนนี้ศูนย์์เปิดอยู่ไหม
- Legacy expected: ['reservation', 'schedule']; live_lookup_required
- ก่อนแก้: pipeline:rag_direct_curated; confidence=0.84; source IDs=['schedule.closure.2026-07-28::th::note', 'schedule.closure.2026-07-29::th::note', 'schedule.closure.2026-07-30::th::note']
- Top candidate: structured.schedule; score=0.928; reason=base=0.86; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=schedule; question_frame_domain_match; question_frame_operation=schedule_lookup; precondition=schedule_query_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:rag_direct_curated; frozen pass=False

### คำตอบก่อนแก้

ศูนย์ปิดให้บริการตามวันหยุดราชการ/วันปิดพิเศษที่ระบุไว้ในระบบ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ศูนย์ปิดให้บริการตามวันหยุดราชการ/วันปิดพิเศษที่ระบุไว้ในระบบ

### คำตอบหลังแก้

ศูนย์ปิดให้บริการตามวันหยุดราชการ/วันปิดพิเศษที่ระบุไว้ในระบบ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03676 — studio_rules_penalties

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ขอสอบถามหน่อยครับ ขอข้อมูลเรื่องเสียหาบเล็กน้อย
- Legacy expected: ['penalty']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ความเสียหายเล็กน้อย เช่น รอยเปื้อน คราบน้ำ รอยขีดข่วน ฝาปิดหลุด หรือปุ่มหลวม มีค่าปรับ 100–500 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-00766 — reservation_policy

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: สรุปขั้นตอนจองให้หน่ยอ ขอรายละเอียดแบบสั้น ๆ
- Legacy expected: ['reservation']; answer_available
- ก่อนแก้: pipeline:ambiguity_clarification; confidence=0.8; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:ambiguity_clarification; frozen pass=False

### คำตอบก่อนแก้

คำถามนี้ยังกว้างเกินไปครับ ยังไม่แน่ใจว่าต้องการถามเรื่องไหนของ PSU Esports Studio - Phuket
ถามให้เจาะจงได้ เช่น `มีเกมอะไรบ้าง`, `มีอุปกรณ์อะไรบ้าง`, `จองยังไง`, `ราคา PS5 เท่าไหร่` หรือ `TEKKEN 8 มีปุ่มอะไรบ้าง`

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

คำถามนี้ยังกว้างเกินไปครับ ยังไม่แน่ใจว่าต้องการถามเรื่องไหนของ PSU Esports Studio - Phuket
ถามให้เจาะจงได้ เช่น `มีเกมอะไรบ้าง`, `มีอุปกรณ์อะไรบ้าง`, `จองยังไง`, `ราคา PS5 เท่าไหร่` หรือ `TEKKEN 8 มีปุ่มอะไรบ้าง`

### คำตอบหลังแก้

คำถามนี้ยังกว้างเกินไปครับ ยังไม่แน่ใจว่าต้องการถามเรื่องไหนของ PSU Esports Studio - Phuket
ถามให้เจาะจงได้ เช่น `มีเกมอะไรบ้าง`, `มีอุปกรณ์อะไรบ้าง`, `จองยังไง`, `ราคา PS5 เท่าไหร่` หรือ `TEKKEN 8 มีปุ่มอะไรบ้าง`

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "จอง",
    "เช็คอิน",
    "ชำระ",
    "session",
    "ยกเลิก"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-03375 — equipment

- Priority: P0 wrong task/target or omitted facet
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ขิข้อมูลที่ยืนยันได้หน่อยรับ: เครื่อง PC ใช้การ์ดจอรุ่นอะไร
- Legacy expected: ['equipment', 'no_answer']; no_answer_expected
- ก่อนแก้: pipeline:structured_equipment_item; confidence=0.95; source IDs=['equipment_gaming_pc']
- Top candidate: structured.equipment; score=0.99; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=equipment; structured_operation_priority; question_frame_domain_match; question_frame_operation=equipment_lookup; precondition=equipment_preconditions_passed
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:structured_equipment_item; frozen pass=False

### คำตอบก่อนแก้

Gaming PC รุ่น MSI MAG Infinite S3 14th: เครื่องคอมพิวเตอร์เกมมิ่งของ PC Zone สำหรับเล่นเกมบนคอมและฝึกซ้อมอีสปอร์ต
จำนวน: 10 Units
อยู่ที่: PC Zone
ใช้สำหรับ:
•    เล่น VALORANT
•    เล่น Counter-Strike 2
•    เล่น PUBG: BATTLEGROUNDS
•    เล่น Call of Duty: Warzone
•    เล่น TEKKEN 8
•    เล่น League of Legends
หมายเหตุ: สเปกที่บันทึกไว้ในโปรเจกต์: Intel Core i5-14400, RAM DDR5 32GB, NVIDIA GeForce RTX 5060 8GB
สเปกนี้เป็นข้อมูลที่บันทึกไว้ในโปรเจกต์ ยังไม่พบหลักฐานในชุดข้อมูลนี้ว่ายืนยันตรงกับเครื่อง PC ที่ใช้งานจริงทุกเครื่อง
เว็บไซต์รายการอุปกรณ์ของศูนย์: https://esports.phuket.psu.ac.th/home
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Gaming PC รุ่น MSI MAG Infinite S3 14th: เครื่องคอมพิวเตอร์เกมมิ่งของ PC Zone สำหรับเล่นเกมบนคอมและฝึกซ้อมอีสปอร์ต
จำนวน: 10 Units
อยู่ที่: PC Zone
ใช้สำหรับ:
•    เล่น VALORANT
•    เล่น Counter-Strike 2
•    เล่น PUBG: BATTLEGROUNDS
•    เล่น Call of Duty: Warzone
•    เล่น TEKKEN 8
•    เล่น League of Legends
หมายเหตุ: สเปกที่บันทึกไว้ในโปรเจกต์: Intel Core i5-14400, RAM DDR5 32GB, NVIDIA GeForce RTX 5060 8GB
สเปกนี้เป็นข้อมูลที่บันทึกไว้ในโปรเจกต์ ยังไม่พบหลักฐานในชุดข้อมูลนี้ว่ายืนยันตรงกับเครื่อง PC ที่ใช้งานจริงทุกเครื่อง
เว็บไซต์รายการอุปกรณ์ของศูนย์: https://esports.phuket.psu.ac.th/home
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### คำตอบหลังแก้

Gaming PC รุ่น MSI MAG Infinite S3 14th: เครื่องคอมพิวเตอร์เกมมิ่งของ PC Zone สำหรับเล่นเกมบนคอมและฝึกซ้อมอีสปอร์ต
จำนวน: 10 Units
อยู่ที่: PC Zone
ใช้สำหรับ:
•    เล่น VALORANT
•    เล่น Counter-Strike 2
•    เล่น PUBG: BATTLEGROUNDS
•    เล่น Call of Duty: Warzone
•    เล่น TEKKEN 8
•    เล่น League of Legends
หมายเหตุ: สเปกที่บันทึกไว้ในโปรเจกต์: Intel Core i5-14400, RAM DDR5 32GB, NVIDIA GeForce RTX 5060 8GB
สเปกนี้เป็นข้อมูลที่บันทึกไว้ในโปรเจกต์ ยังไม่พบหลักฐานในชุดข้อมูลนี้ว่ายืนยันตรงกับเครื่อง PC ที่ใช้งานจริงทุกเครื่อง
เว็บไซต์รายการอุปกรณ์ของศูนย์: https://esports.phuket.psu.ac.th/home
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04678 — members_overview_contact

- Priority: P0 wrong task/target or omitted facet
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ขอสอบถามหน่อยครับ ขอข้อมูลเรื่งcontact facebook
- Legacy expected: ['contact']; answer_available
- ก่อนแก้: pipeline:rag_direct_curated; confidence=0.84; source IDs=['rule_booking_steps::th::answer', 'rule_edit_booking::th::answer', 'rule_en_booking_steps_natural::th::answer']
- Top candidate: structured.reservation; score=0.933; reason=base=0.86; domain_match; answer_type_match; question_frame_domain_match; question_frame_operation=booking_lookup; precondition=reservation_or_booking_query
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:rag_direct_curated; frozen pass=False

### คำตอบก่อนแก้

ขั้นตอนจองคือ เลือกบริการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชี และแนบสลิปการโอนเงิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปเดิม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ขั้นตอนจองคือ เลือกบริการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชี และแนบสลิปการโอนเงิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04683 — members_overview_contact

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ขอสอบถามหน่อยครั ขอข้อมูลเรื่องเป้าหมายศูนย์
- Legacy expected: ['overview']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-01622 — games_catalog_availability

- Priority: P0 wrong task/target or omitted facet
- Evidence: trace_code_source_inspected
- คำถาม: VR Zone รอบละกีน่าที
- Legacy expected: ['games', 'reservation']; answer_available
- ก่อนแก้: pipeline:structured_equipment_catalog; confidence=0.95; source IDs=['home_equipment']
- Top candidate: structured.equipment; score=0.99; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=equipment; structured_operation_priority; question_frame_domain_match; question_frame_operation=equipment_lookup; precondition=equipment_preconditions_passed
- สาเหตุ/ขอบเขตการยืนยัน: Broken duration qualifier leaves VR target but unknown requested fact; equipment wins0.990; catalog instead of session duration.
- หลังแก้: pipeline:structured_service_duration; frozen pass=True

### คำตอบก่อนแก้

อุปกรณ์ใน VR Zone:
PlayStation 5 Zone / VR Zone
•    PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive (2 Units in PlayStation 5 Zone and 1 Unit in VR Zone)
VR Zone
•    Sony PlayStation VR2 (1 Unit)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

VR Zone มีรอบ 30 และ 60 นาทีในระบบจองครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

VR Zone มีรอบ 30 และ 60 นาทีในระบบจองครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "Beat Saber",
    "Horizon Call of the Mountain",
    "Resident Evil 4",
    "30"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03611 — equipment

- Priority: P0 wrong task/target or omitted facet
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ช่วยตอบจากข้อมูลที่ยืนยันได้หน่อย: ขอข้อมูลที่ยืนยันได้หน่อยครับ: เครื่อง PC ใช้การ์ดจอรุน่อะไร
- Legacy expected: ['equipment', 'no_answer']; no_answer_expected
- ก่อนแก้: pipeline:structured_equipment_item; confidence=0.95; source IDs=['equipment_gaming_pc']
- Top candidate: structured.equipment; score=0.99; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=equipment; structured_operation_priority; question_frame_domain_match; question_frame_operation=equipment_lookup; precondition=equipment_preconditions_passed
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:structured_equipment_item; frozen pass=False

### คำตอบก่อนแก้

Gaming PC รุ่น MSI MAG Infinite S3 14th: เครื่องคอมพิวเตอร์เกมมิ่งของ PC Zone สำหรับเล่นเกมบนคอมและฝึกซ้อมอีสปอร์ต
จำนวน: 10 Units
อยู่ที่: PC Zone
ใช้สำหรับ:
•    เล่น VALORANT
•    เล่น Counter-Strike 2
•    เล่น PUBG: BATTLEGROUNDS
•    เล่น Call of Duty: Warzone
•    เล่น TEKKEN 8
•    เล่น League of Legends
หมายเหตุ: สเปกที่บันทึกไว้ในโปรเจกต์: Intel Core i5-14400, RAM DDR5 32GB, NVIDIA GeForce RTX 5060 8GB
สเปกนี้เป็นข้อมูลที่บันทึกไว้ในโปรเจกต์ ยังไม่พบหลักฐานในชุดข้อมูลนี้ว่ายืนยันตรงกับเครื่อง PC ที่ใช้งานจริงทุกเครื่อง
เว็บไซต์รายการอุปกรณ์ของศูนย์: https://esports.phuket.psu.ac.th/home
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Gaming PC รุ่น MSI MAG Infinite S3 14th: เครื่องคอมพิวเตอร์เกมมิ่งของ PC Zone สำหรับเล่นเกมบนคอมและฝึกซ้อมอีสปอร์ต
จำนวน: 10 Units
อยู่ที่: PC Zone
ใช้สำหรับ:
•    เล่น VALORANT
•    เล่น Counter-Strike 2
•    เล่น PUBG: BATTLEGROUNDS
•    เล่น Call of Duty: Warzone
•    เล่น TEKKEN 8
•    เล่น League of Legends
หมายเหตุ: สเปกที่บันทึกไว้ในโปรเจกต์: Intel Core i5-14400, RAM DDR5 32GB, NVIDIA GeForce RTX 5060 8GB
สเปกนี้เป็นข้อมูลที่บันทึกไว้ในโปรเจกต์ ยังไม่พบหลักฐานในชุดข้อมูลนี้ว่ายืนยันตรงกับเครื่อง PC ที่ใช้งานจริงทุกเครื่อง
เว็บไซต์รายการอุปกรณ์ของศูนย์: https://esports.phuket.psu.ac.th/home
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### คำตอบหลังแก้

Gaming PC รุ่น MSI MAG Infinite S3 14th: เครื่องคอมพิวเตอร์เกมมิ่งของ PC Zone สำหรับเล่นเกมบนคอมและฝึกซ้อมอีสปอร์ต
จำนวน: 10 Units
อยู่ที่: PC Zone
ใช้สำหรับ:
•    เล่น VALORANT
•    เล่น Counter-Strike 2
•    เล่น PUBG: BATTLEGROUNDS
•    เล่น Call of Duty: Warzone
•    เล่น TEKKEN 8
•    เล่น League of Legends
หมายเหตุ: สเปกที่บันทึกไว้ในโปรเจกต์: Intel Core i5-14400, RAM DDR5 32GB, NVIDIA GeForce RTX 5060 8GB
สเปกนี้เป็นข้อมูลที่บันทึกไว้ในโปรเจกต์ ยังไม่พบหลักฐานในชุดข้อมูลนี้ว่ายืนยันตรงกับเครื่อง PC ที่ใช้งานจริงทุกเครื่อง
เว็บไซต์รายการอุปกรณ์ของศูนย์: https://esports.phuket.psu.ac.th/home
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-02516 — game_detail

- Priority: P0 wrong task/target or omitted facet
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ช่วยคอบจากข้อมูลที่ยืนยันได้หน่อย: Mario Party Superstars เล่นยังไง
- Legacy expected: ['games']; answer_available
- ก่อนแก้: pipeline:structured_game_controls; confidence=0.96; source IDs=['game_controls_mariopartysuperstars']
- Top candidate: structured.games; score=0.999; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=games; question_frame_domain_match; question_frame_operation=game_detail; precondition=game_domain_or_catalog_query
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:structured_game_controls; frozen pass=False

### คำตอบก่อนแก้

Mario Party Superstars มีข้อมูลปุ่มควบคุมดังนี้:
Nintendo Switch
•    Button controls: เล่นบอร์ดและมินิเกมด้วยปุ่ม - แหล่งทางการยืนยันว่า 100 มินิเกมรองรับ button controls และเล่นได้ด้วย Joy-Con หรือ Nintendo Switch Pro Controller
•    Single Joy-Con / Joy-Con grip / Pro Controller: รูปแบบคอนโทรลเลอร์ที่รองรับ - สามารถเล่นด้วย Joy-Con เดี่ยว, Joy-Con grip, Nintendo Switch Pro Controller หรือ Nintendo Switch Lite ตามข้อมูล Play Nintendo
แหล่งข้อมูล: https://play.nintendo.com/news-tips/game-releases/mario-party-superstars-game-announcement/

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Mario Party Superstars มีข้อมูลปุ่มควบคุมดังนี้:
Nintendo Switch
•    Button controls: เล่นบอร์ดและมินิเกมด้วยปุ่ม - แหล่งทางการยืนยันว่า 100 มินิเกมรองรับ button controls และเล่นได้ด้วย Joy-Con หรือ Nintendo Switch Pro Controller
•    Single Joy-Con / Joy-Con grip / Pro Controller: รูปแบบคอนโทรลเลอร์ที่รองรับ - สามารถเล่นด้วย Joy-Con เดี่ยว, Joy-Con grip, Nintendo Switch Pro Controller หรือ Nintendo Switch Lite ตามข้อมูล Play Nintendo
แหล่งข้อมูล: https://play.nintendo.com/news-tips/game-releases/mario-party-superstars-game-announcement/

### คำตอบหลังแก้

Mario Party Superstars มีข้อมูลปุ่มควบคุมดังนี้:
Nintendo Switch
•    Button controls: เล่นบอร์ดและมินิเกมด้วยปุ่ม - แหล่งทางการยืนยันว่า 100 มินิเกมรองรับ button controls และเล่นได้ด้วย Joy-Con หรือ Nintendo Switch Pro Controller
•    Single Joy-Con / Joy-Con grip / Pro Controller: รูปแบบคอนโทรลเลอร์ที่รองรับ - สามารถเล่นด้วย Joy-Con เดี่ยว, Joy-Con grip, Nintendo Switch Pro Controller หรือ Nintendo Switch Lite ตามข้อมูล Play Nintendo
แหล่งข้อมูล: https://play.nintendo.com/news-tips/game-releases/mario-party-superstars-game-announcement/

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "ทอยลูกเต๋าเดินบนกระดาน เก็บดาว และเล่นมินิเกมเพื่อทำคะแนน"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-00402 — reservation_policy

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: อขข้อมูลเรื่องการจอง ยกเลิก ไม่แจ้ง
- Legacy expected: ['reservation']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=['Reservation']
- Top candidate: structured.reservation; score=0.999; reason=base=0.86; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=reservation; question_frame_domain_match; question_frame_operation=booking_lookup; precondition=reservation_or_booking_query
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04840 — compound_context_boundary

- Priority: P0 wrong task/target or omitted facet
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Tekken 8 ราคาเท่าไหร่ แล้วมีป่มอะไรบ้าง
- Legacy expected: ['multi_question']; answer_available
- ก่อนแก้: pipeline:structured_service_fee_by_game; confidence=0.9; source IDs=['TEKKEN 8', 'service_fee_image_2026', 'pc_service_fee_local_update_20260727']
- Top candidate: structured.service_fee; score=0.985; reason=base=0.86; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=service_fee; question_frame_domain_match; game_price_requires_service_mapping; precondition=known_game_price_query_needs_zone_service_mapping
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:structured_service_fee_by_game; frozen pass=False

### คำตอบก่อนแก้

TEKKEN 8 ไม่มีราคาแยกตามชื่อเกมครับ ต้องดูราคาตามโซน/บริการที่ใช้เล่นเกมนี้

PC Zone
ราคา PC 1 ชั่วโมง (1 คน) สำหรับ นักศึกษา/นักเรียน/บุคลากร PSU
•    0 บาท
หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

PlayStation 5 Zone
ราคา PlayStation 5 1 ชั่วโมง (1-2 คน) สำหรับ นักศึกษา/นักเรียน/บุคลากร PSU
•    0 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: Tekken 8 ราคาเท่าไหร่
TEKKEN 8 ไม่มีราคาแยกตามชื่อเกมครับ ต้องดูราคาตามโซน/บริการที่ใช้เล่นเกมนี้

PC Zone
ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน
PC 1 ชั่วโมง (1 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU: 0 บาท/1 ชั่วโมง
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 25 บาท/1 ชั่วโมง
•    บุคคลทั่วไป (General Adult): 70 บาท/1 ชั่วโมง
หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

PlayStation 5 Zone
ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน
PlayStation 5 1 ชั่วโมง (1-2 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU: 0 บาท/1 ชั่วโมง
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท/1 ชั่วโมง
•    บุคคลทั่วไป (General Adult): 150 บาท/1 ชั่วโมง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

คำถามที่ 2: Tekken 8 มีปุ่มอะไรบ้าง
TEKKEN 8 มีข้อมูลปุ่มควบคุมดังนี้:
PlayStation / PS5
•    Square: หมัดซ้าย / ต่อยซ้าย - ออกหมัดแย็บหรือโจมตีด้วยมือซ้าย เป็นปุ่มหลักในการเริ่มต้นเฟรมคอมโบที่รวดเร็ว
•    Triangle: หมัดขวา / ต่อยขวา - ออกหมัดหนักหรือโจมตีด้วยมือขวา มักใช้ทำดาเมจแรงหรือสวนกลับ (Counter)
•    Cross: ลูกเตะซ้าย - ใช้ขาซ้ายเตะสกัดหรือโจมตีเพื่อเปิดช่องว่างของศัตรู
•    Circle: ลูกเตะขวา - ใช้ขาขวาหวดเตะอย่างรุนแรง มักเป็นท่าเคลียร์ระยะหรือตัดขาที่ทำดาเมจสูง
•    D-Pad Up: กระโดด - ควบคุมให้ตัวละครกระโดดขึ้นด้านบนเพื่อหลบการโจมตีล่าง หรือใช้กดร่วมกับปุ่มโจมตีกลางอากาศ
•    D-Pad Left: ถอยหลัง / บล็อก - บังคับตัวละครให้เดินถอยหลังเพื่อรักษาระยะ หรือใช้กดค้างเพื่อ "บล็อก (Guard)" การโจมตีระดับสูงและระดับกลางของศัตรู
•    D-Pad Down: ย่อตัว / ก้มหลบ - สั่งให้ตัวละครย่อตัวต่ำ ใช้ก้มหลบหมัดหรือการโจมตีระดับสูง (High) และใช้บล็อกการโจมตีระดับต่ำ (Low)
•    L (Left Stick): เคลื่อนที่ - ขยับทิศทางของตัวละคร بشكلทั่วไป หรือใช้โยกทิศทางในการเคลื่อนที่และเดินหน้าถอยหลัง
•    L1: สเปเชียลสไตล์ - กดเพื่อเปิด/ปิดโหมดช่วยเหลืออัจฉริยะ ช่วยให้กดคอมโบและท่าไม้ตายของตัวละครนั้น ๆ ได้ง่ายด้วยปุ่มเดียว
•    R1: เปิดใช้งาน Heat - ระเบิดพลัง Heat System เข้าสู่สถานะโอเวอร์ไดรฟ์เพื่อบัฟการโจมตีและเพิ่มคุณสมบัติพิเศษให้ตัวละคร
•    R1 (While in Heat): ฮีทสแมช - ปลดปล่อยท่าโจมตีเผด็จศึกอันทรงพลังปิดฉากคอมโบ โดยจะใช้เกจ Heat ที่เหลืออยู่ทั้งหมดทิ้งทันที
•    Options: หยุดเกม - หยุดเกมชั่วคราวเพื่อเข้าสู่หน้าต่างเมนู เช่น การเช็ก Move List (รายการท่า) หรือการตั้งค่าอื่น ๆ
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://gameinputdatabase.com/game/83

### คำตอบหลังแก้

TEKKEN 8 ไม่มีราคาแยกตามชื่อเกมครับ ต้องดูราคาตามโซน/บริการที่ใช้เล่นเกมนี้

PC Zone
ราคา PC 1 ชั่วโมง (1 คน) สำหรับ นักศึกษา/นักเรียน/บุคลากร PSU
•    0 บาท
หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

PlayStation 5 Zone
ราคา PlayStation 5 1 ชั่วโมง (1-2 คน) สำหรับ นักศึกษา/นักเรียน/บุคลากร PSU
•    0 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "คำถามที่",
    "ราคา",
    "ปุ่ม",
    "Zone",
    "จอง"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-04765 — compound_context_boundary

- Priority: P0 wrong task/target or omitted facet
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ขอข้อมูลเรท่องโปรไฟล์เกมเมอร
- Legacy expected: ['no_answer']; no_answer_expected
- ก่อนแก้: pipeline:structured_games_catalog; confidence=0.95; source IDs=['our_games']
- Top candidate: structured.games; score=0.999; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=games; structured_operation_priority; question_frame_domain_match; question_frame_operation=game_catalog; precondition=game_domain_or_catalog_query
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:structured_games_catalog; frozen pass=False

### คำตอบก่อนแก้

ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 42 เกมครับ

PC Zone (6 เกม)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 เกม)
•    Call of Duty: Modern Warfare III
•    Delta Force
•    EA Sports FC 24
•    eFootball
•    FINAL FANTASY XVI
•    Fortnite
•    God of War Ragnarok
•    Hogwarts Legacy
•    Marvel's Spider-Man 2
•    NARUTO X BORUTO Ultimate Ninja Storm Connections
•    Resident Evil 4
•    Resident Evil Village
•    TEKKEN 8
•    THE FINALS
•    The Last of Us Part I
•    The Last of Us Part II (Remastered)
•    Uncharted: Legacy of Thieves Collection

Nintendo Switch Zone (17 เกม)
•    Animal Crossing: New Horizons
•    It Takes Two
•    Little Nightmares II
•    Luigi's Mansion 3
•    Mario Kart 8 Deluxe
•    Mario Party Superstars
•    Monster Hunter Rise
•    Moving Out 2
•    New Super Mario Bros. U Deluxe
•    Nintendo Switch Sports
•    Overcooked!
•    Overcooked! 2
•    Pokémon Champions
•    Ring Fit Adventure
•    Super Mario Odyssey
•    Super Smash Bros Ultimate
•    The Legend of Zelda: Breath of The Wild

Cockpit Zone (1 เกม)
•    Gran Turismo 7

VR Zone (4 เกม)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 42 เกมครับ

PC Zone (6 เกม)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 เกม)
•    Call of Duty: Modern Warfare III
•    Delta Force
•    EA Sports FC 24
•    eFootball
•    FINAL FANTASY XVI
•    Fortnite
•    God of War Ragnarok
•    Hogwarts Legacy
•    Marvel's Spider-Man 2
•    NARUTO X BORUTO Ultimate Ninja Storm Connections
•    Resident Evil 4
•    Resident Evil Village
•    TEKKEN 8
•    THE FINALS
•    The Last of Us Part I
•    The Last of Us Part II (Remastered)
•    Uncharted: Legacy of Thieves Collection

Nintendo Switch Zone (17 เกม)
•    Animal Crossing: New Horizons
•    It Takes Two
•    Little Nightmares II
•    Luigi's Mansion 3
•    Mario Kart 8 Deluxe
•    Mario Party Superstars
•    Monster Hunter Rise
•    Moving Out 2
•    New Super Mario Bros. U Deluxe
•    Nintendo Switch Sports
•    Overcooked!
•    Overcooked! 2
•    Pokémon Champions
•    Ring Fit Adventure
•    Super Mario Odyssey
•    Super Smash Bros Ultimate
•    The Legend of Zelda: Breath of The Wild

Cockpit Zone (1 เกม)
•    Gran Turismo 7

VR Zone (4 เกม)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### คำตอบหลังแก้

ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 42 เกมครับ

PC Zone (6 เกม)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 เกม)
•    Call of Duty: Modern Warfare III
•    Delta Force
•    EA Sports FC 24
•    eFootball
•    FINAL FANTASY XVI
•    Fortnite
•    God of War Ragnarok
•    Hogwarts Legacy
•    Marvel's Spider-Man 2
•    NARUTO X BORUTO Ultimate Ninja Storm Connections
•    Resident Evil 4
•    Resident Evil Village
•    TEKKEN 8
•    THE FINALS
•    The Last of Us Part I
•    The Last of Us Part II (Remastered)
•    Uncharted: Legacy of Thieves Collection

Nintendo Switch Zone (17 เกม)
•    Animal Crossing: New Horizons
•    It Takes Two
•    Little Nightmares II
•    Luigi's Mansion 3
•    Mario Kart 8 Deluxe
•    Mario Party Superstars
•    Monster Hunter Rise
•    Moving Out 2
•    New Super Mario Bros. U Deluxe
•    Nintendo Switch Sports
•    Overcooked!
•    Overcooked! 2
•    Pokémon Champions
•    Ring Fit Adventure
•    Super Mario Odyssey
•    Super Smash Bros Ultimate
•    The Legend of Zelda: Breath of The Wild

Cockpit Zone (1 เกม)
•    Gran Turismo 7

VR Zone (4 เกม)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-00676 — reservation_policy

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: รบกวนเช็กข้อมูลของศนย์ให้หน่อยครับ จ่ายเงินยังไงตอนของ อะ
- Legacy expected: ['reservation', 'service_fee']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

การยกเลิกหรือแก้ไขการจองควรทำล่วงหน้าอย่างน้อย 1 ชั่วโมง หากกดจองแล้วจะแก้ข้อมูลเดิมไม่ได้ ต้องยกเลิกแล้วจองใหม่ตามเงื่อนไข
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03380 — equipment

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: PlayStation 5 Zone มีอะไรใหห้ใช้บ้าง
- Legacy expected: ['clarification', 'equipment']; answer_available
- ก่อนแก้: pipeline:ambiguity_clarification; confidence=0.78; source IDs=['our_games', 'home_equipment', 'service_fee_image_2026', 'reservation']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:ambiguity_clarification; frozen pass=False

### คำตอบก่อนแก้

คำถามนี้ยังตีได้หลายทางครับ หมายถึงเรื่องไหนของ PlayStation 5 Zone?

ข้อมูลย่อที่ยืนยันได้ตอนนี้:
•    เกม: มี 26 เกม เช่น Beat Saber, Call of Duty: Modern Warfare III, Call of Duty: Warzone, Delta Force และอื่น ๆ | พิมพ์ `PS5 มีเกมอะไรบ้าง`
•    อุปกรณ์: มี 1 รายการ เช่น PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive | พิมพ์ `PS5 มีอุปกรณ์อะไรบ้าง`
•    ราคา: PlayStation 5 1 ชั่วโมง (1-2 คน): PSU 0 บาท, General Student 50 บาท, General Adult 150 บาท | พิมพ์ `PS5 ราคาเท่าไหร่`
•    จอง: ต้องจองผ่านระบบก่อนเข้าใช้ | พิมพ์ `PS5 จองยังไง`

พิมพ์ต่อสั้น ๆ ได้ เช่น `เกม`, `อุปกรณ์`, `ราคา` หรือ `จอง`

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

คำถามนี้ยังตีได้หลายทางครับ หมายถึงเรื่องไหนของ PlayStation 5 Zone?

ข้อมูลย่อที่ยืนยันได้ตอนนี้:
•    เกม: มี 26 เกม เช่น Beat Saber, Call of Duty: Modern Warfare III, Call of Duty: Warzone, Delta Force และอื่น ๆ | พิมพ์ `PS5 มีเกมอะไรบ้าง`
•    อุปกรณ์: มี 1 รายการ เช่น PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive | พิมพ์ `PS5 มีอุปกรณ์อะไรบ้าง`
•    ราคา: PlayStation 5 1 ชั่วโมง (1-2 คน): PSU 0 บาท, General Student 50 บาท, General Adult 150 บาท | พิมพ์ `PS5 ราคาเท่าไหร่`
•    จอง: ต้องจองผ่านระบบก่อนเข้าใช้ | พิมพ์ `PS5 จองยังไง`

พิมพ์ต่อสั้น ๆ ได้ เช่น `เกม`, `อุปกรณ์`, `ราคา` หรือ `จอง`

### คำตอบหลังแก้

คำถามนี้ยังตีได้หลายทางครับ หมายถึงเรื่องไหนของ PlayStation 5 Zone?

ข้อมูลย่อที่ยืนยันได้ตอนนี้:
•    เกม: มี 26 เกม เช่น Beat Saber, Call of Duty: Modern Warfare III, Call of Duty: Warzone, Delta Force และอื่น ๆ | พิมพ์ `PS5 มีเกมอะไรบ้าง`
•    อุปกรณ์: มี 1 รายการ เช่น PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive | พิมพ์ `PS5 มีอุปกรณ์อะไรบ้าง`
•    ราคา: PlayStation 5 1 ชั่วโมง (1-2 คน): PSU 0 บาท, General Student 50 บาท, General Adult 150 บาท | พิมพ์ `PS5 ราคาเท่าไหร่`
•    จอง: ต้องจองผ่านระบบก่อนเข้าใช้ | พิมพ์ `PS5 จองยังไง`

พิมพ์ต่อสั้น ๆ ได้ เช่น `เกม`, `อุปกรณ์`, `ราคา` หรือ `จอง`

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "อุปกรณ์",
    "หมายถึงเรื่องไหน",
    "Zone"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-04754 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ขอข้อมูลเรื่องคริปโ
- Legacy expected: ['no_answer']; no_answer_expected
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04527 — members_overview_contact

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: นายปัณณวิชญ์ หนูเรือง มีตไแหน่งอไร
- Legacy expected: ['members', 'overview']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

นายปัณณวิชญ์ หนูเรือง: เลขานุการ
หมวด: PSU Phuket Esports Club - PSU Phuket
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "นายปัณณวิชญ์ หนูเรือง",
    "เลขานุการ"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04992 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: JSON คืออะไรร ขอ 1 ย่อหน้า
- Legacy expected: ['general', 'knowledge']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.763; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "JSON",
    "ข้อมูล"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03877 — studio_rules_penalties

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ถ้าจะไปใช้บริการจริง ขอข้อมูลเรื่องเสียหาปยานกลาง
- Legacy expected: ['penalty']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ความเสียหายปานกลาง เช่น เบาะขาด รอยขีดข่วนลึก โครงเฟอร์นิเจอร์เสียหาย คอนโทรลเลอร์ปุ่มค้าง หรือหูฟังสายขาด ต้องชำระค่าซ่อมตามราคาจริง หรือ 500–2,000 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-00082 — service_fee

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: PSU Staff เล่น PC ต้องเวียเงินไหม
- Legacy expected: ['service_fee']; answer_available
- ก่อนแก้: pipeline:structured_members_game_relation_no_data; confidence=0.94; source IDs=['Members']
- Top candidate: structured.members; score=0.923; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=members; structured_operation_priority; question_frame_domain_mismatch; question_frame_operation=member_lookup; member_closed_route_priority; precondition=member_query_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:structured_members_game_relation_no_data; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ว่าสมาชิกหรือสตาฟแต่ละคนเล่นเกม/ดูแลเกมหรือโซนไหนครับ
ข้อมูลที่มีตอนนี้ยืนยันได้เฉพาะรายชื่อสมาชิก หมวด และตำแหน่งในหน้า Members
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ราคา PC 1 ชั่วโมง สำหรับ PSU Student and Staff: 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff
หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ว่าสมาชิกหรือสตาฟแต่ละคนเล่นเกม/ดูแลเกมหรือโซนไหนครับ
ข้อมูลที่มีตอนนี้ยืนยันได้เฉพาะรายชื่อสมาชิก หมวด และตำแหน่งในหน้า Members
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "บาท",
    "ต่างกัน",
    "ฟรี",
    "0 บาท"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-00370 — service_fee

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: ขอสอบถามหน่อยครับ Fortnite าคาเท่าไหร่
- Legacy expected: ['service_fee']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.56; source IDs=['Reservation']
- Top candidate: fast.price_calculator; score=0.806; reason=base=0.93; domain_match; tool_router_domain=service_fee; price_calculation_priority; precondition=price_calculator_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Fortnite ไม่มีราคาแยกตามชื่อเกมครับ ต้องดูราคาตามโซน/บริการที่ใช้เล่นเกมนี้

PlayStation 5 Zone
ยังไม่ทราบกลุ่มผู้ใช้ จึงแสดงราคาทุกกลุ่มให้เทียบก่อน
PlayStation 5 1 ชั่วโมง (1-2 คน)
•    นักศึกษา/นักเรียน/บุคลากร PSU: 0 บาท/1 ชั่วโมง
•    ศิษย์เก่า PSU / นักศึกษา-นักเรียนต่างสถาบัน (General Student): 50 บาท/1 ชั่วโมง
•    บุคคลทั่วไป (General Adult): 150 บาท/1 ชั่วโมง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [
    "Fortnite"
  ],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-03757 — studio_rules_penalties

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: รบกวนเช็กข้อมูลของศูนย์ให้หน่ิยครับ อัดวิดีโอในศูนย์ได้ไหม
- Legacy expected: ['no_answer', 'overview', 'rules']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04544 — members_overview_contact

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ขอข้อมูลเรื่องอยู่ที่หน
- Legacy expected: ['contact']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด contact ตอนนี้ครับ

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04159 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: ขออ้างอิงกติกา อารีน่สออฟเวเลอร์ ในหัวข้อจำนวผู้เล่นต่อทีม หน่อย
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:ambiguity_clarification; confidence=0.74; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:ambiguity_clarification; frozen pass=False

### คำตอบก่อนแก้

คำถามนี้มีได้หลายความหมายครับ ขอระบุเพิ่มนิดหนึ่งว่าต้องการถามเรื่องไหน: กติกาการแข่งขัน, สมาชิกทีม

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

คำตอบ: 4. ระเบียบและกติกาการแข่งขัน

รายละเอียดที่เกี่ยวข้อง:
•    4.1. กติกาพื้นฐาน
•    4.1.1.ห้ามใช้ชื่อตัวละครหรือคําพูดที่เป็นการหยาบคายหรือเสียดสีผู้อื่น
•    4.1.2.ในเกมแรก ทีมที่อยู่ทางด้านบนของสายการแข่งขันจะได้อยู่ฝ่ายสีน้ำเงิน และในเกมถัดไป ผู้ที่แพ้ในเกมก่อนหน้าจะได้สิทธิ์ในการเลือกฝั่ง
•    4.1.3.กรรมการจะเป็นผู้แจ้งหมายเลขห้อง เพื่อให้ผู้เข้าแข่งขันทั้งสองทีมเข้าห้องตามหมายเลขที่กำหนดไว้

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

### คำตอบหลังแก้

คำถามนี้มีได้หลายความหมายครับ ขอระบุเพิ่มนิดหนึ่งว่าต้องการถามเรื่องไหน: กติกาการแข่งขัน, สมาชิกทีม

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03467 — equipment

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ขอสบอถามหน่อยครับ ขอข้อมูลเรื่องเก้าอี้เกมมิ่ง pc
- Legacy expected: ['equipment']; answer_available
- ก่อนแก้: pipeline:game_meta_clarification; confidence=0.74; source IDs=['our_games', 'Reservation']
- Top candidate: structured.equipment; score=0.836; reason=base=0.88; answer_type_match; tool_router_action=structured; question_frame_domain_match; question_frame_operation=equipment_lookup; precondition=equipment_preconditions_passed
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:game_meta_clarification; frozen pass=False

### คำตอบก่อนแก้

ถามเรื่องเกมได้ครับ แต่คำถามนี้ยังกว้างเกินไป เลยไม่ขอดึงเกมใดเกมหนึ่งมาตอบแทน

ตัวอย่างที่ถามได้:
•    `มีเกมอะไรบ้าง`
•    `PS5 มีเกมอะไรบ้าง`
•    `TEKKEN 8 คือเกมอะไร`
•    `TEKKEN 8 มีปุ่มอะไรบ้าง`
•    `Nintendo Switch มีเกมแนวปาร์ตี้ไหม`

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ถามเรื่องเกมได้ครับ แต่คำถามนี้ยังกว้างเกินไป เลยไม่ขอดึงเกมใดเกมหนึ่งมาตอบแทน

ตัวอย่างที่ถามได้:
•    `มีเกมอะไรบ้าง`
•    `PS5 มีเกมอะไรบ้าง`
•    `TEKKEN 8 คือเกมอะไร`
•    `TEKKEN 8 มีปุ่มอะไรบ้าง`
•    `Nintendo Switch มีเกมแนวปาร์ตี้ไหม`

### คำตอบหลังแก้

ถามเรื่องเกมได้ครับ แต่คำถามนี้ยังกว้างเกินไป เลยไม่ขอดึงเกมใดเกมหนึ่งมาตอบแทน

ตัวอย่างที่ถามได้:
•    `มีเกมอะไรบ้าง`
•    `PS5 มีเกมอะไรบ้าง`
•    `TEKKEN 8 คือเกมอะไร`
•    `TEKKEN 8 มีปุ่มอะไรบ้าง`
•    `Nintendo Switch มีเกมแนวปาร์ตี้ไหม`

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03891 — studio_rules_penalties

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ถ้าจะไปใช้บริการจริง กำลังวางแผนจะปใช้บริการ พอดีอยากรู้ว่า อักวิดีโอในศูนย์ได้ไหม
- Legacy expected: ['no_answer', 'overview', 'rules']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-01419 — schedule_calendar

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ช่วยตอบจากข้อมูลที่ยืนยันได้น่อย: กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า พรุ่งนี้เปิดไหม
- Legacy expected: ['reservation', 'schedule']; live_lookup_required
- ก่อนแก้: pipeline:no_answer; confidence=0.56; source IDs=['Reservation']
- Top candidate: structured.games; score=0.999; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=games; question_frame_domain_match; question_frame_operation=game_detail; precondition=game_domain_or_catalog_query
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03669 — studio_rules_penalties

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: อัดวิดีโอในศููนย์ได้ไหม
- Legacy expected: ['no_answer', 'overview', 'rules']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.759; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03243 — game_controls

- Priority: P0 wrong task/target or omitted facet
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: Resident Evil 4 (Remake) ปุ่มท้งหมดมีอะไรบ้าง
- Legacy expected: ['games']; answer_available
- ก่อนแก้: pipeline:structured_game_controls; confidence=0.96; source IDs=['game_controls_residentevil4']
- Top candidate: structured.game_controls; score=0.999; reason=base=0.90; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=game_controls; game_control_priority; question_frame_domain_match; question_frame_operation=control_lookup; precondition=game_control_query_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:structured_game_controls; frozen pass=False

### คำตอบก่อนแก้

Resident Evil 4 มีข้อมูลปุ่มควบคุมดังนี้:
PlayStation / PS5
•    L (Left Stick): เคลื่อนที่
•    L3: วิ่งสปรินต์
•    R (Right Stick): มุมกล้อง
•    L2 (Hold): เล็ง
•    L1: ปัดป้อง
•    R1: วิ่ง / กลับหลังหัน
•    R2: ยิง / โจมตีด้วยมีด
•    Triangle: คลังไอเทม
•    Circle: ย่อตัว
•    Square: รีโหลด
•    Cross: โต้ตอบ
•    D-Pad: เปลี่ยนอาวุธ
•    Options: หยุดเกม
•    Touch Pad: แผนที่
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://gameinputdatabase.com/game/45

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Resident Evil 4 มีข้อมูลปุ่มควบคุมดังนี้:
PlayStation / PS5
•    L (Left Stick): เคลื่อนที่
•    L3: วิ่งสปรินต์
•    R (Right Stick): มุมกล้อง
•    L2 (Hold): เล็ง
•    L1: ปัดป้อง
•    R1: วิ่ง / กลับหลังหัน
•    R2: ยิง / โจมตีด้วยมีด
•    Triangle: คลังไอเทม
•    Circle: ย่อตัว
•    Square: รีโหลด
•    Cross: โต้ตอบ
•    D-Pad: เปลี่ยนอาวุธ
•    Options: หยุดเกม
•    Touch Pad: แผนที่
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://gameinputdatabase.com/game/45

### คำตอบหลังแก้

Resident Evil 4 มีข้อมูลปุ่มควบคุมดังนี้:
PlayStation / PS5
•    L (Left Stick): เคลื่อนที่
•    L3: วิ่งสปรินต์
•    R (Right Stick): มุมกล้อง
•    L2 (Hold): เล็ง
•    L1: ปัดป้อง
•    R1: วิ่ง / กลับหลังหัน
•    R2: ยิง / โจมตีด้วยมีด
•    Triangle: คลังไอเทม
•    Circle: ย่อตัว
•    Square: รีโหลด
•    Cross: โต้ตอบ
•    D-Pad: เปลี่ยนอาวุธ
•    Options: หยุดเกม
•    Touch Pad: แผนที่
หมายเหตุ: ข้อมูลปุ่มจากแหล่งรองนี้ยังไม่ได้ตรวจยืนยันกับเกมและเครื่องที่ศูนย์ใช้อยู่จริง การตั้งค่าปุ่มอาจต่างจากรายการนี้
แหล่งข้อมูล: https://gameinputdatabase.com/game/45

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [
    "Resident Evil 4 (Remake)",
    "ปุ่ม"
  ],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-02110 — games_catalog_availability

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: ขอสอบถามหน่อยครับ ถ้าจะเล่น Delta Force ต้องจอองะไร
- Legacy expected: ['games', 'reservation']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=['Reservation']
- Top candidate: structured.equipment; score=0.834; reason=base=0.88; answer_type_match; tool_router_action=structured; question_frame_domain_match; question_frame_operation=equipment_lookup; precondition=equipment_preconditions_passed
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ถ้าจะเล่น Delta Force ให้จอง PlayStation 5 Zone - PlayStation 5 #01-#02 ครับ
•    PlayStation 5 Zone - PlayStation 5 #01-#02 (60 นาที, 1-2 คน)
จากนั้นเลือกวัน รอบเวลา กรอกข้อมูลผู้ใช้บริการ ชำระเงิน และแนบสลิปเพื่อยืนยันการจอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "PlayStation 5 #01-#02",
    "PlayStation 5",
    "Delta Force"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-03977 — studio_rules_penalties

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: พอดีไม่แน่ใจว่า อัดวิีโอฝนศูนย์ได้ไหม
- Legacy expected: ['no_answer', 'overview', 'rules']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04767 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ขอข้อมูลเรื่องซ่อมคอมพิวเตอร์ส่วนนตัว
- Legacy expected: ['no_answer']; no_answer_expected
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03824 — studio_rules_penalties

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: สอบถามครับ ขอข้อมูลที่ืนยันได้หน่อยครับ: อัดวิดีโอในศูนย์ได้ไหม
- Legacy expected: ['no_answer', 'overview', 'rules']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-00313 — service_fee

- Priority: P0 wrong task/target or omitted facet
- Evidence: paired_regression_primary_cause_pending
- คำถาม: ขอาอบถามหน่อยครับ บุคคลทั่วไป เล่น PC 30 นาที เสียี่บาท
- Legacy expected: ['service_fee']; answer_available
- ก่อนแก้: pipeline:protected_public_access; confidence=0.98; source IDs=['reservation_public_access_reviewed_20260924']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:deterministic_calculator_fast; frozen pass=True

### คำตอบก่อนแก้

ได้ครับ บุคคลทั่วไปสามารถจองใช้บริการ PC Zone ได้ ค่าบริการขึ้นกับประเภทบริการและกลุ่มผู้ใช้ ต้องจองผ่านระบบและแสดงบัตรประชาชนเมื่อเช็กอิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ระยะเวลาที่ถามคือ 30 นาที ใช้ 1 session ตามแพ็กเกจ PC 1 ชั่วโมง
คำตอบราคา: 70 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
•    คำนวณจาก 70 บาท/session x 1 session = 70 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
PC 1 ชั่วโมง (1 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 25 บาท
•    General Adult: 70 บาท
หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### คำตอบหลังแก้

ระยะเวลาที่ถามคือ 30 นาที ใช้ 1 session ตามแพ็กเกจ PC 1 ชั่วโมง
คำตอบราคา: 70 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
•    คำนวณจาก 70 บาท/session x 1 session = 70 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
PC 1 ชั่วโมง (1 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 25 บาท
•    General Adult: 70 บาท
หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "General Adult",
    "0 บาท"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-04352 — competition_rules

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ขอสอบถามหน่อยครับ ตาม rulebook เค่น์เตอร์สไตรก์ 2 ตารงบทลงโทษ ต้องทำยังไง
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:competition_target_clarification; confidence=0.97; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:competition_target_clarification; frozen pass=False

### คำตอบก่อนแก้

ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

วันและช่วงเวลาให้บริการตามตารางปกติ (ไม่ใช่สถานะเครื่องว่างแบบสด):
•    วันจันทร์: เปิด 13:00-16:00; Maintenance 09:00-12:00
•    วันอังคาร-พฤหัสบดี: เปิด 09:00-12:00, 13:00-16:00
•    วันศุกร์: เปิด 09:00-12:00; Maintenance 13:00-16:00
•    วันเสาร์-อาทิตย์: ไม่มีรอบให้บริการหรือจองตามตารางปกติ
วันปิดพิเศษมีผลก่อนตารางปกติ และช่วงที่เปิดไม่ได้ยืนยันว่าเครื่องยังว่างครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### คำตอบหลังแก้

ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03901 — studio_rules_penalties

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: ช่วยยืนยันใ้ทีว่า ขอข้อมูลเรื่องระงับสิทธิ์ชี่วคราว
- Legacy expected: ['penalty']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=['Reservation']
- Top candidate: fast.domain_handlers; score=0.539; reason=base=0.78; multi_domain; answer_type_match; tool_router_action=fast_path; precondition=domain_fast_handler_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด penalty ตอนนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

หากผู้ใช้งานละเมิดกฎซ้ำหรือกระทำการรุนแรง อาจถูกระงับสิทธิ์การใช้งานชั่วคราวเป็นระยะเวลา 1-7 วัน ขึ้นอยู่กับลักษณะของการละเมิด
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด penalty ตอนนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03832 — studio_rules_penalties

- Priority: P0 wrong task/target or omitted facet
- Evidence: paired_regression_primary_cause_pending
- คำถาม: อยากรู้ว่า ขอข้อมูลเรื่ององหาย อุปกรณ์ เปียด
- Legacy expected: ['rules']; answer_available
- ก่อนแก้: pipeline:structured_equipment_catalog; confidence=0.96; source IDs=['home_equipment']
- Top candidate: structured.equipment; score=0.99; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=equipment; structured_operation_priority; question_frame_domain_match; question_frame_operation=equipment_lookup; precondition=equipment_preconditions_passed
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:structured_equipment_catalog; frozen pass=False

### คำตอบก่อนแก้

อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

กรุณาตรวจสอบทรัพย์สินของท่านทุกครั้งระหว่างการใช้บริการ หากมีการสูญหาย ศูนย์ขอสงวนสิทธิ์ไม่รับผิดชอบในทุกกรณี
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03988 — studio_rules_penalties

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: ช่วยอธิบายให้เข้าใจง่ายหน่อยว่า ขอข้อมูลเรื่องคำพูไดม่เหมาะสม
- Legacy expected: ['rules']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.763; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

กรุณางดส่งเสียงดังเกินควร และห้ามพูดจาดูหมิ่นหรือเสียดสีผู้อื่น
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03739 — studio_rules_penalties

- Priority: P0 wrong task/target or omitted facet
- Evidence: paired_regression_primary_cause_pending
- คำถาม: รบกวนเช็กข้อมูลของศูนย์ให้หน่อยครับ ขอข้อมูลเรื่องทำอุปกรณ์เสยหาย รับผิดชอบ
- Legacy expected: ['penalty']; answer_available
- ก่อนแก้: pipeline:structured_equipment_catalog; confidence=0.96; source IDs=['home_equipment']
- Top candidate: structured.equipment; score=0.934; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=equipment; question_frame_domain_match; question_frame_operation=equipment_lookup; precondition=equipment_preconditions_passed
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:structured_equipment_catalog; frozen pass=False

### คำตอบก่อนแก้

อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ถ้าทำอุปกรณ์เสียหาย ผู้ใช้งานต้องรับผิดชอบค่าปรับหรือค่าชดเชยตามระดับความเสียหาย ตั้งแต่ความเสียหายเล็กน้อย 100–500 บาท ความเสียหายปานกลางตามราคาจริงหรือ 500–2,000 บาท ไปจนถึงความเสียหายร้ายแรงที่ต้องชดเชยราคาทรัพย์สินเต็มจำนวน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04789 — compound_context_boundary

- Priority: P0 wrong task/target or omitted facet
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: เปิดปะ อ
- Legacy expected: ['clarification', 'general', 'schedule']; clarification_required
- ก่อนแก้: pipeline:structured_schedule; confidence=0.96; source IDs=['reservation_schedule']
- Top candidate: structured.schedule; score=0.928; reason=base=0.86; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=schedule; question_frame_domain_match; question_frame_operation=schedule_lookup; precondition=schedule_query_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:structured_schedule; frozen pass=False

### คำตอบก่อนแก้

เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00

รายละเอียดจากตาราง:
•    วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open
•    วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันพุธ: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันพฤหัสบดี: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันศุกร์: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = maintenance
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00

รายละเอียดจากตาราง:
•    วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open
•    วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันพุธ: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันพฤหัสบดี: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันศุกร์: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = maintenance
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00

รายละเอียดจากตาราง:
•    วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open
•    วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันพุธ: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันพฤหัสบดี: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันศุกร์: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = maintenance
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-02476 — game_detail

- Priority: P1 task/qualifier or English evidence
- Evidence: trace_code_source_inspected
- คำถาม: ช่วยตอบจาข้อมูลที่ยืนยันได้หน่อย: Counter-Strike 2 คือเกมอะไน
- Legacy expected: ['games']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.56; source IDs=['Reservation']
- Top candidate: structured.games; score=0.999; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=games; structured_operation_priority; question_frame_domain_match; question_frame_operation=game_detail; precondition=game_domain_or_catalog_query
- สาเหตุ/ขอบเขตการยืนยัน: Exact game retained and structured.games0.999 wins; local detail predicate misses เกมอะไน, returns catalog; validator rejects type, then slow deterministic/fallback also rejected. Profile proves repeated normalization/fuzzy comparison CPU work.
- หลังแก้: pipeline:structured_game_detail; frozen pass=True

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Counter-Strike 2: Counter-Strike 2 คือเกมยิงแข่งขันแบบทีมที่แบ่งเป็นฝ่ายบุกและฝ่ายรับ โดยมีเป้าหมายหลักเกี่ยวกับการวาง/กู้ระเบิดหรือจัดการฝ่ายตรงข้าม
แนวเกม: เกมยิง Tactical FPS
วิธีเล่นโดยสรุป: เล่นเป็นรอบ ๆ ต้องซื้ออาวุธ วางแผนกับทีม คุมพื้นที่ และใช้การเล็งกับการสื่อสารเพื่อชนะรอบ
เล่นได้ที่: PC Zone
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### คำตอบหลังแก้

Counter-Strike 2: Counter-Strike 2 คือเกมยิงแข่งขันแบบทีมที่แบ่งเป็นฝ่ายบุกและฝ่ายรับ โดยมีเป้าหมายหลักเกี่ยวกับการวาง/กู้ระเบิดหรือจัดการฝ่ายตรงข้าม
แนวเกม: เกมยิง Tactical FPS
วิธีเล่นโดยสรุป: เล่นเป็นรอบ ๆ ต้องซื้ออาวุธ วางแผนกับทีม คุมพื้นที่ และใช้การเล็งกับการสื่อสารเพื่อชนะรอบ
เล่นได้ที่: PC Zone
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "Counter-Strike 2 คือเกมยิงแข่งขันแบบทีมที่แบ่งเป็นฝ่ายบุกและฝ่ายรับ โดยมีเป้าหมายหลักเกี่ยวกับการวาง/กู้ระเบิดหรือจัดการฝ่ายตรงข้าม"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03978 — studio_rules_penalties

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: พอดีไม่แน่ใจว่า ขอข้อมูลที่ยืนยันไดเหน่อยครับ: อัดวิดีโอในศูนย์ได้ไหม
- Legacy expected: ['no_answer', 'overview', 'rules']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-01488 — schedule_calendar

- Priority: P0 wrong task/target or omitted facet
- Evidence: paired_regression_primary_cause_pending
- คำถาม: กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า วันหยดราชการเปิดไหม
- Legacy expected: ['clarification', 'schedule']; clarification_required
- ก่อนแก้: pipeline:structured_schedule; confidence=0.96; source IDs=['reservation_schedule']
- Top candidate: structured.schedule; score=0.928; reason=base=0.86; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=schedule; question_frame_domain_match; question_frame_operation=schedule_lookup; precondition=schedule_query_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:structured_schedule; frozen pass=False

### คำตอบก่อนแก้

เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00

รายละเอียดจากตาราง:
•    วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open
•    วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันพุธ: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันพฤหัสบดี: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันศุกร์: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = maintenance
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

หมายถึงวันหยุดวันที่เท่าไรครับ? วันหยุดราชการไม่ได้ทำให้ศูนย์ปิดโดยอัตโนมัติ ต้องตรวจวันปิดพิเศษที่บันทึกไว้และตารางบริการของวันที่นั้นก่อน
แหล่งข้อมูลตารางบริการ: https://esports.computing.psu.ac.th/reservation

### คำตอบหลังแก้

เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00

รายละเอียดจากตาราง:
•    วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open
•    วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันพุธ: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันพฤหัสบดี: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันศุกร์: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = maintenance
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04543 — members_overview_contact

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ขอข่อมูลเรืองcontact facebook
- Legacy expected: ['contact']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=['Reservation']
- Top candidate: structured.reservation; score=0.933; reason=base=0.86; domain_match; answer_type_match; question_frame_domain_match; question_frame_operation=booking_lookup; precondition=reservation_or_booking_query
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

เมื่อกดจองแล้วจะไม่สามารถแก้ไขข้อมูลได้ หากต้องการแก้ไขต้องยกเลิกการจองผ่านทางอีเมลก่อนเวลาใช้งานอย่างน้อย 1 ชั่วโมง แล้วจองใหม่ พร้อมแนบสลิปเดิม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-00781 — reservation_policy

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ต้องแนบสลิไปหม ขอรายละเอียดแบบสั้น ๆ
- Legacy expected: ['reservation']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ตอนจองต้องกรอก Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล เบอร์โทรศัพท์ และชำระโดยโอนเงินพร้อมแนบสลิป
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "จอง",
    "เช็คอิน",
    "ชำระ",
    "session",
    "ยกเลิก"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-00347 — service_fee

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ขอสอบถามหน่อยครับ นักศึกษา PSU เฃ่น VR 30 นาที เสียกี่บท
- Legacy expected: ['service_fee']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:deterministic_calculator_fast; frozen pass=True

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ระยะเวลาที่ถามคือ 30 นาที ใช้ 1 session ตามแพ็กเกจ VR 30 นาที
คำตอบราคา: 0 บาท สำหรับกลุ่ม PSU Student and Staff
•    คำนวณจาก 0 บาท/session x 1 session = 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 190 บาท
•    General Adult: 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### คำตอบหลังแก้

ระยะเวลาที่ถามคือ 30 นาที ใช้ 1 session ตามแพ็กเกจ VR 30 นาที
คำตอบราคา: 0 บาท สำหรับกลุ่ม PSU Student and Staff
•    คำนวณจาก 0 บาท/session x 1 session = 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
VR 30 นาที (1-5 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 190 บาท
•    General Adult: 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "0 บาท",
    "0 บาท"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-03801 — studio_rules_penalties

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: อัดวิดีโอในศูนย์ได้ไหม ช่วยแนบแหล่งข้อมูลด้ย
- Legacy expected: ['no_answer', 'overview', 'rules']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-01111 — live_booking

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: PC3 ตอนบ่ายโมงว่ามงั้ย ช่วยแนบแหล่งข้อมูลด้วย
- Legacy expected: ['reservation', 'schedule']; live_lookup_required
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

วันที่ 2026-10-01 (เวลาไทย) ยังยืนยันสถานะเปิด-ปิดและ Slot แบบสดไม่ได้ เพราะ Booking Dashboard ไม่พร้อมใช้งานครับ
ผมจะไม่เอาตารางเก่ามาแสดงว่าเป็นข้อมูลจองแบบสด กรุณาลองใหม่อีกครั้งหรือดูหน้าจองโดยตรง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04950 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: เฟรมเรตกับความละ้อียดต่างกนยังไง ตอบสั้น ๆ
- Legacy expected: ['general', 'knowledge', 'no_answer']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "เฟรม",
    "ความละเอียด"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-01842 — games_catalog_availability

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Pokémon Champions อยู่โซซนไหน
- Legacy expected: ['games']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.56; source IDs=['Reservation']
- Top candidate: structured.games; score=0.978; reason=base=0.88; domain_match; answer_type_match; tool_router_domain=games; question_frame_domain_match; question_frame_operation=game_detail; precondition=game_domain_or_catalog_query
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ได้ครับ Pokémon Champions เล่นได้ที่ Nintendo Switch Zone - Nintendo Switch (1-2 Persons), Nintendo Switch Zone - Nintendo Switch (1-4 Persons)
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "Nintendo Switch",
    "Nintendo Switch (1-2 Persons)"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-04990 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: เฟรมเรตกับความละเอียดต่างกันยังไง ขอ 1 ย่อหน้
- Legacy expected: ['general', 'knowledge', 'no_answer']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.763; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "เฟรม",
    "ความละเอียด"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-00187 — service_fee

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: คนทั่วไป เล่น Nintendo Switch 3 ชั่วโมง เสียกี่บาม
- Legacy expected: ['service_fee']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.56; source IDs=['Reservation']
- Top candidate: structured.games; score=0.999; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=games; structured_operation_priority; question_frame_domain_match; question_frame_operation=game_detail; precondition=game_domain_or_catalog_query
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:deterministic_calculator_fast; frozen pass=True

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ราคา Nintendo Switch สำหรับกลุ่ม General Adult / บุคคลทั่วไป
•    Nintendo Switch 1-2 คน: 140 บาท
•    Nintendo Switch 3-4 คน: 280 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป
หมายเหตุ: คำถามยังไม่ระบุจำนวนผู้เล่น จึงแสดงทั้งราคา 1-2 คนและ 3-4 คน

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 50 บาท
•    General Adult: 140 บาท

Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 100 บาท
•    General Adult: 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### คำตอบหลังแก้

ราคา Nintendo Switch สำหรับกลุ่ม General Adult / บุคคลทั่วไป
•    Nintendo Switch 1-2 คน: 140 บาท
•    Nintendo Switch 3-4 คน: 280 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป
หมายเหตุ: คำถามยังไม่ระบุจำนวนผู้เล่น จึงแสดงทั้งราคา 1-2 คนและ 3-4 คน

รายละเอียดจากตาราง:
Nintendo Switch 1-2 คน 60 นาที (1 ชั่วโมง)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 50 บาท
•    General Adult: 140 บาท

Nintendo Switch 3-4 คน 60 นาที (1 ชั่วโมง)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 100 บาท
•    General Adult: 280 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "บาท",
    "บาท",
    "ฟรี"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-03384 — equipment

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: VR Zone มีอะไรให้ใช้บบ้าง
- Legacy expected: ['clarification', 'equipment']; answer_available
- ก่อนแก้: pipeline:ambiguity_clarification; confidence=0.78; source IDs=['our_games', 'home_equipment', 'service_fee_image_2026', 'reservation']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:ambiguity_clarification; frozen pass=False

### คำตอบก่อนแก้

คำถามนี้ยังตีได้หลายทางครับ หมายถึงเรื่องไหนของ VR Zone?

ข้อมูลย่อที่ยืนยันได้ตอนนี้:
•    เกม: มี 2 เกม เช่น Beat Saber, Horizon Call of the Mountain | พิมพ์ `VR มีเกมอะไรบ้าง`
•    อุปกรณ์: มี 1 รายการ เช่น Sony PlayStation VR2 | พิมพ์ `VR มีอุปกรณ์อะไรบ้าง`
•    ราคา: มีหลายแพ็กเกจตามเวลา/จำนวนผู้เล่น: VR 30 นาที (1-5 คน), VR 1 ชั่วโมง (1-5 คน) | พิมพ์ `VR ราคาเท่าไหร่`
•    จอง: ต้องจองผ่านระบบก่อนเข้าใช้ | พิมพ์ `VR จองยังไง`

พิมพ์ต่อสั้น ๆ ได้ เช่น `เกม`, `อุปกรณ์`, `ราคา` หรือ `จอง`

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

คำถามนี้ยังตีได้หลายทางครับ หมายถึงเรื่องไหนของ VR Zone?

ข้อมูลย่อที่ยืนยันได้ตอนนี้:
•    เกม: มี 2 เกม เช่น Beat Saber, Horizon Call of the Mountain | พิมพ์ `VR มีเกมอะไรบ้าง`
•    อุปกรณ์: มี 1 รายการ เช่น Sony PlayStation VR2 | พิมพ์ `VR มีอุปกรณ์อะไรบ้าง`
•    ราคา: มีหลายแพ็กเกจตามเวลา/จำนวนผู้เล่น: VR 30 นาที (1-5 คน), VR 1 ชั่วโมง (1-5 คน) | พิมพ์ `VR ราคาเท่าไหร่`
•    จอง: ต้องจองผ่านระบบก่อนเข้าใช้ | พิมพ์ `VR จองยังไง`

พิมพ์ต่อสั้น ๆ ได้ เช่น `เกม`, `อุปกรณ์`, `ราคา` หรือ `จอง`

### คำตอบหลังแก้

คำถามนี้ยังตีได้หลายทางครับ หมายถึงเรื่องไหนของ VR Zone?

ข้อมูลย่อที่ยืนยันได้ตอนนี้:
•    เกม: มี 2 เกม เช่น Beat Saber, Horizon Call of the Mountain | พิมพ์ `VR มีเกมอะไรบ้าง`
•    อุปกรณ์: มี 1 รายการ เช่น Sony PlayStation VR2 | พิมพ์ `VR มีอุปกรณ์อะไรบ้าง`
•    ราคา: มีหลายแพ็กเกจตามเวลา/จำนวนผู้เล่น: VR 30 นาที (1-5 คน), VR 1 ชั่วโมง (1-5 คน) | พิมพ์ `VR ราคาเท่าไหร่`
•    จอง: ต้องจองผ่านระบบก่อนเข้าใช้ | พิมพ์ `VR จองยังไง`

พิมพ์ต่อสั้น ๆ ได้ เช่น `เกม`, `อุปกรณ์`, `ราคา` หรือ `จอง`

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "อุปกรณ์",
    "หมายถึงเรื่องไหน",
    "Zone"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-04433 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ขอสอบถามหน่อยครับ ขออ้างอิงติกา อารีน่าออฟเวเลอร์ ในหัวข้อจำนวยผู้เล่นต่อทีม หน่อย
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

คำตอบ: 4. ระเบียบและกติกาการแข่งขัน

รายละเอียดที่เกี่ยวข้อง:
•    4.1. กติกาพื้นฐาน
•    4.1.1.ห้ามใช้ชื่อตัวละครหรือคําพูดที่เป็นการหยาบคายหรือเสียดสีผู้อื่น
•    4.1.2.ในเกมแรก ทีมที่อยู่ทางด้านบนของสายการแข่งขันจะได้อยู่ฝ่ายสีน้ำเงิน และในเกมถัดไป ผู้ที่แพ้ในเกมก่อนหน้าจะได้สิทธิ์ในการเลือกฝั่ง
•    4.1.3.กรรมการจะเป็นผู้แจ้งหมายเลขห้อง เพื่อให้ผู้เข้าแข่งขันทั้งสองทีมเข้าห้องตามหมายเลขที่กำหนดไว้

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04965 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: เขียนประโยคประชาสัมพันธ์กิจกรรมแบบสุภพหนึ่งประโยค ขอแบบเข้าใจง่าบ
- Legacy expected: ['general', 'knowledge', 'no_answer']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.763; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "กิจกรรม"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03934 — studio_rules_penalties

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ขอข้อมูลล่าสุดที่ระบบยืนยันได้: ขอข้อมูลที่ยืนยันได้หน่อยคับ: อัดวิดีโอในศูนบ์ได้ไหม
- Legacy expected: ['no_answer', 'overview', 'rules']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.759; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04540 — members_overview_contact

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: นายอภิวิชญ์ เลิศกมลรักษ์ มีตแำหน่งอะไร
- Legacy expected: ['members', 'overview']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

นายอภิวิชญ์ เลิศกมลรักษ์: กรรมการ
หมวด: PSU Phuket Esports Club - PSU Phuket
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "นายอภิวิชญ์ เลิศกมลรักษ์",
    "กรรมการ"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-02422 — game_detail

- Priority: P0 wrong task/target or omitted facet
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ขอสอบถามหน่อยคครับ Nintendo Switch Sports เล่นยังไง
- Legacy expected: ['games']; answer_available
- ก่อนแก้: pipeline:structured_game_controls; confidence=0.96; source IDs=['game_controls_nintendoswitchsports']
- Top candidate: structured.games; score=0.999; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=games; question_frame_domain_match; question_frame_operation=game_detail; precondition=game_domain_or_catalog_query
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:structured_game_controls; frozen pass=False

### คำตอบก่อนแก้

Nintendo Switch Sports ปุ่มที่ตรงกับคำถาม:
Nintendo Switch
•    Joy-Con motion: เล่นท่ากีฬาด้วยการขยับ Joy-Con - เกมใช้ Joy-Con หรือ Joy-Con 2 ตามชนิดกีฬาที่เลือก โดยการออกท่าจะขึ้นกับกีฬานั้น ๆ
•    + Button on controller-holding screen: เลือกโหมดสายรัดขาใน Soccer ตอนเล่น Local/Friends - ในหน้าวิธีถือ Joy-Con ให้กด + เพื่อเปลี่ยนเป็น Leg-Strap Mode
แหล่งข้อมูล: https://en-americas-support.nintendo.com/app/answers/detail/a_id/58596/~/nintendo-switch-sports-faq

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Nintendo Switch Sports ปุ่มที่ตรงกับคำถาม:
Nintendo Switch
•    Joy-Con motion: เล่นท่ากีฬาด้วยการขยับ Joy-Con - เกมใช้ Joy-Con หรือ Joy-Con 2 ตามชนิดกีฬาที่เลือก โดยการออกท่าจะขึ้นกับกีฬานั้น ๆ
•    + Button on controller-holding screen: เลือกโหมดสายรัดขาใน Soccer ตอนเล่น Local/Friends - ในหน้าวิธีถือ Joy-Con ให้กด + เพื่อเปลี่ยนเป็น Leg-Strap Mode
แหล่งข้อมูล: https://en-americas-support.nintendo.com/app/answers/detail/a_id/58596/~/nintendo-switch-sports-faq

### คำตอบหลังแก้

Nintendo Switch Sports ปุ่มที่ตรงกับคำถาม:
Nintendo Switch
•    Joy-Con motion: เล่นท่ากีฬาด้วยการขยับ Joy-Con - เกมใช้ Joy-Con หรือ Joy-Con 2 ตามชนิดกีฬาที่เลือก โดยการออกท่าจะขึ้นกับกีฬานั้น ๆ
•    + Button on controller-holding screen: เลือกโหมดสายรัดขาใน Soccer ตอนเล่น Local/Friends - ในหน้าวิธีถือ Joy-Con ให้กด + เพื่อเปลี่ยนเป็น Leg-Strap Mode
แหล่งข้อมูล: https://en-americas-support.nintendo.com/app/answers/detail/a_id/58596/~/nintendo-switch-sports-faq

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "ถือ Joy-Con แล้วขยับตามกีฬาที่เลือก เช่น ตี โยน หรือแกว่งตามท่าทางในเกม"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04799 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ขอข้อมูลที่ยืนยันได้หน่อยครับ: ขอทเำรื่องพิเศษได้ไหม
- Legacy expected: ['clarification', 'general', 'reservation']; clarification_required
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.759; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-00300 — service_fee

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ขอสอถามหน่อยคระบ กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า Tekken 8 ราคาเท่าไหร่
- Legacy expected: ['games', 'service_fee']; answer_available
- ก่อนแก้: pipeline:protected_price_missing_service; confidence=0.98; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:protected_price_missing_service; frozen pass=False

### คำตอบก่อนแก้

ต้องการทราบค่าบริการของ PC, PlayStation 5, Nintendo Switch, Cockpit หรือ VR ครับ? ราคาแตกต่างตามบริการและกลุ่มผู้ใช้ จึงยังระบุราคาเดียวไม่ได้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ต้องการทราบค่าบริการของ PC, PlayStation 5, Nintendo Switch, Cockpit หรือ VR ครับ? ราคาแตกต่างตามบริการและกลุ่มผู้ใช้ จึงยังระบุราคาเดียวไม่ได้ครับ

### คำตอบหลังแก้

ต้องการทราบค่าบริการของ PC, PlayStation 5, Nintendo Switch, Cockpit หรือ VR ครับ? ราคาแตกต่างตามบริการและกลุ่มผู้ใช้ จึงยังระบุราคาเดียวไม่ได้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04632 — members_overview_contact

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ำแหน่ง เลข่นุการ คือใคร
- Legacy expected: ['overview']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ตำแหน่ง เลขานุการ มี 1 คนครับ
•    นายปัณณวิชญ์ หนูเรือง: เลขานุการ
  ◦    หมวด: PSU Phuket Esports Club - PSU Phuket
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "นายปัณณวิชญ์ หนูเรือง",
    "เลขานุการ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-04382 — competition_rules

- Priority: P0 wrong task/target or omitted facet
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ขอสอบถามหน่อยครับ คาม rulebook เคาน์เตอร์สไตรก์ 2 ตารางและเวลาแข่งขัน ต้องทำยังไง
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:protected_booking_window; confidence=0.98; source IDs=['service_schedule']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:protected_booking_window; frozen pass=False

### คำตอบก่อนแก้

วันและช่วงเวลาให้บริการตามตารางปกติ (ไม่ใช่สถานะเครื่องว่างแบบสด):
•    วันจันทร์: เปิด 13:00-16:00; Maintenance 09:00-12:00
•    วันอังคาร-พฤหัสบดี: เปิด 09:00-12:00, 13:00-16:00
•    วันศุกร์: เปิด 09:00-12:00; Maintenance 13:00-16:00
•    วันเสาร์-อาทิตย์: ไม่มีรอบให้บริการหรือจองตามตารางปกติ
วันปิดพิเศษมีผลก่อนตารางปกติ และช่วงที่เปิดไม่ได้ยืนยันว่าเครื่องยังว่างครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

วันและช่วงเวลาให้บริการตามตารางปกติ (ไม่ใช่สถานะเครื่องว่างแบบสด):
•    วันจันทร์: เปิด 13:00-16:00; Maintenance 09:00-12:00
•    วันอังคาร-พฤหัสบดี: เปิด 09:00-12:00, 13:00-16:00
•    วันศุกร์: เปิด 09:00-12:00; Maintenance 13:00-16:00
•    วันเสาร์-อาทิตย์: ไม่มีรอบให้บริการหรือจองตามตารางปกติ
วันปิดพิเศษมีผลก่อนตารางปกติ และช่วงที่เปิดไม่ได้ยืนยันว่าเครื่องยังว่างครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### คำตอบหลังแก้

วันและช่วงเวลาให้บริการตามตารางปกติ (ไม่ใช่สถานะเครื่องว่างแบบสด):
•    วันจันทร์: เปิด 13:00-16:00; Maintenance 09:00-12:00
•    วันอังคาร-พฤหัสบดี: เปิด 09:00-12:00, 13:00-16:00
•    วันศุกร์: เปิด 09:00-12:00; Maintenance 13:00-16:00
•    วันเสาร์-อาทิตย์: ไม่มีรอบให้บริการหรือจองตามตารางปกติ
วันปิดพิเศษมีผลก่อนตารางปกติ และช่วงที่เปิดไม่ได้ยืนยันว่าเครื่องยังว่างครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04975 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: เขียนประโยคปรชาสัมพันธ์กิจกรรมแบบสุภาพหนึ่งประโยค ตอบเป็นภาษาไทย
- Legacy expected: ['general', 'knowledge', 'no_answer']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.763; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "กิจกรรม"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-00010 — service_fee

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ขอข้อมูลที่ยินยันได้หน่อยครับ: VR ครึ่งชั่วโมงกี่บา
- Legacy expected: ['service_fee']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

VR 30 นาที (1-5 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 190 บาท
•    General Adult: 525 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03848 — studio_rules_penalties

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: อยากรู้ว่า อัดดวิดีโอในศูนย์ได้มั้ย
- Legacy expected: ['no_answer', 'overview', 'rules']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-02204 — game_detail

- Priority: P0 wrong task/target or omitted facet
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Beat Saber คือเกมออะไร
- Legacy expected: ['games']; answer_available
- ก่อนแก้: pipeline:structured_games_catalog; confidence=0.95; source IDs=['our_games']
- Top candidate: structured.games; score=0.999; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=games; structured_operation_priority; question_frame_domain_match; question_frame_operation=game_detail; precondition=game_domain_or_catalog_query
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:structured_game_detail; frozen pass=True

### คำตอบก่อนแก้

ตอนนี้มีเกมที่ยืนยันได้ทั้งหมด 42 เกมครับ

PC Zone (6 เกม)
•    Call of Duty: Warzone
•    Counter-Strike 2
•    League of Legends
•    PUBG: BATTLEGROUNDS
•    TEKKEN 8
•    VALORANT

PlayStation 5 Zone (17 เกม)
•    Call of Duty: Modern Warfare III
•    Delta Force
•    EA Sports FC 24
•    eFootball
•    FINAL FANTASY XVI
•    Fortnite
•    God of War Ragnarok
•    Hogwarts Legacy
•    Marvel's Spider-Man 2
•    NARUTO X BORUTO Ultimate Ninja Storm Connections
•    Resident Evil 4
•    Resident Evil Village
•    TEKKEN 8
•    THE FINALS
•    The Last of Us Part I
•    The Last of Us Part II (Remastered)
•    Uncharted: Legacy of Thieves Collection

Nintendo Switch Zone (17 เกม)
•    Animal Crossing: New Horizons
•    It Takes Two
•    Little Nightmares II
•    Luigi's Mansion 3
•    Mario Kart 8 Deluxe
•    Mario Party Superstars
•    Monster Hunter Rise
•    Moving Out 2
•    New Super Mario Bros. U Deluxe
•    Nintendo Switch Sports
•    Overcooked!
•    Overcooked! 2
•    Pokémon Champions
•    Ring Fit Adventure
•    Super Mario Odyssey
•    Super Smash Bros Ultimate
•    The Legend of Zelda: Breath of The Wild

Cockpit Zone (1 เกม)
•    Gran Turismo 7

VR Zone (4 เกม)
•    Beat Saber
•    Horizon Call of the Mountain
•    Resident Evil 4
•    Resident Evil Village
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Beat Saber: Beat Saber คือเกม VR จังหวะดนตรีที่ผู้เล่นใช้ดาบแสงฟันบล็อกตามจังหวะเพลง
แนวเกม: เกม VR Rhythm
วิธีเล่นโดยสรุป: สวมแว่น VR ถือคอนโทรลเลอร์ แล้วฟันบล็อกตามทิศทาง หลบสิ่งกีดขวาง และพยายามทำคะแนนตามจังหวะเพลง
เล่นได้ที่: VR Zone
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### คำตอบหลังแก้

Beat Saber: Beat Saber คือเกม VR จังหวะดนตรีที่ผู้เล่นใช้ดาบแสงฟันบล็อกตามจังหวะเพลง
แนวเกม: เกม VR Rhythm
วิธีเล่นโดยสรุป: สวมแว่น VR ถือคอนโทรลเลอร์ แล้วฟันบล็อกตามทิศทาง หลบสิ่งกีดขวาง และพยายามทำคะแนนตามจังหวะเพลง
เล่นได้ที่: VR Zone
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "Beat Saber คือเกม VR จังหวะดนตรีที่ผู้เล่นใช้ดาบแสงฟันบล็อกตามจังหวะเพลง"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04548 — members_overview_contact

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ขอข้อมูลเรื่องเป้าหทายศูนย์
- Legacy expected: ['overview']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04964 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: แปลคำว่า reservation ดป็นภาษาไทย ขอแบเข้าใจง่าย
- Legacy expected: ['general', 'knowledge', 'no_answer']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.763; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "จอง"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04977 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: GPU คทออะไรแบบเข้าใจง่าย ตอบเป็นภาษาไทย
- Legacy expected: ['general', 'knowledge']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.759; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "GPU",
    "กราฟิก"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-00304 — service_fee

- Priority: P0 wrong task/target or omitted facet
- Evidence: paired_regression_primary_cause_pending
- คำถาม: จอสอบถามหน่อยครับ กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า PC กับ VR อันไหนพงกว่า
- Legacy expected: ['service_fee']; answer_available
- ก่อนแก้: pipeline:structured_equipment_catalog; confidence=0.95; source IDs=['home_equipment']
- Top candidate: structured.equipment; score=0.99; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=equipment; structured_operation_priority; question_frame_domain_match; question_frame_operation=equipment_lookup; precondition=equipment_preconditions_passed
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:structured_equipment_catalog; frozen pass=False

### คำตอบก่อนแก้

อุปกรณ์ใน PC Zone:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (10 Units)
•    Gaming Monitor (10 Units)
•    Gaming Keyboard
•    Gaming Mouse
•    Gaming Headset
•    Gaming Chair (10 Units)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

PC 1 ชั่วโมง (1 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 25 บาท
•    General Adult: 70 บาท
หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27

VR 30 นาที (1-5 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 190 บาท
•    General Adult: 525 บาท

VR 1 ชั่วโมง (60 นาที, 1-5 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 375 บาท
•    General Adult: 1,050 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### คำตอบหลังแก้

อุปกรณ์ใน PC Zone:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (10 Units)
•    Gaming Monitor (10 Units)
•    Gaming Keyboard
•    Gaming Mouse
•    Gaming Headset
•    Gaming Chair (10 Units)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-00670 — reservation_policy

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: รบกวนเช็กข้อูมลของศูนย์ให้หน่อยครับ ขอข้อมูลเรื่องได้เงินคืน
- Legacy expected: ['reservation']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04707 — members_overview_contact

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ขอสอบถมหนาอยครับ ศูนย์อยู่ที่ไหน อะ
- Legacy expected: ['contact', 'overview']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=['Reservation']
- Top candidate: structured.equipment; score=0.789; reason=base=0.88; answer_type_match; question_frame_domain_match; question_frame_operation=equipment_lookup; precondition=equipment_preconditions_passed
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด contact ตอนนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด contact ตอนนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด contact ตอนนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-01817 — games_catalog_availability

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: ถ้าจะเล่น Resident Evil 4 ต้องจอวอะไร
- Legacy expected: ['games', 'reservation']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=['Reservation']
- Top candidate: structured.equipment; score=0.834; reason=base=0.88; answer_type_match; tool_router_action=structured; question_frame_domain_match; question_frame_operation=equipment_lookup; precondition=equipment_preconditions_passed
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ถ้าจะเล่น Resident Evil 4 ให้จอง PlayStation 5 Zone - PlayStation 5 #01-#02 หรือ VR Zone - VR Station 30 นาที หรือ VR Zone - VR Station 1 ชั่วโมง ครับ
•    PlayStation 5 Zone - PlayStation 5 #01-#02 (60 นาที, 1-2 คน)
•    VR Zone - VR Station 30 นาที (30 นาที, 1-5 คน)
•    VR Zone - VR Station 1 ชั่วโมง (60 นาที, 1-5 คน)
จากนั้นเลือกวัน รอบเวลา กรอกข้อมูลผู้ใช้บริการ ชำระเงิน และแนบสลิปเพื่อยืนยันการจอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "PlayStation 5 #01-#02",
    "PlayStation 5",
    "Resident Evil 4"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-02069 — games_catalog_availability

- Priority: P0 wrong task/target or omitted facet
- Evidence: paired_regression_primary_cause_pending
- คำถาม: ขอสอบถามหน่อยครับ อุปกร์ไหนเกม้ยอะสุด
- Legacy expected: ['games']; answer_available
- ก่อนแก้: pipeline:structured_equipment_catalog; confidence=0.96; source IDs=['home_equipment']
- Top candidate: structured.equipment; score=0.99; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=equipment; structured_operation_priority; question_frame_domain_match; question_frame_operation=equipment_lookup; precondition=equipment_preconditions_passed
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:structured_equipment_catalog; frozen pass=False

### คำตอบก่อนแก้

อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ถ้านับตามโซน/บริการที่มีรายชื่อเกมยืนยันได้ PlayStation 5 Zone และ Nintendo Switch Zone มีเกมเยอะสุดครับ (17 เกม)

จำนวนเกมตามโซน:
•    PlayStation 5 Zone: 17 เกม
•    Nintendo Switch Zone: 17 เกม
•    PC Zone: 6 เกม
•    VR Zone: 4 เกม
•    Cockpit Zone: 1 เกม
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### คำตอบหลังแก้

อุปกรณ์บนหน้า Home:
PC Zone
•    Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง)
•    Gaming Monitor (จำนวน 10 จอ)
•    Gaming Chair (จำนวน 10 ตัว)
•    Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset

Cockpit Zone
•    TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง)
•    Racezone Full Cockpit V3 (จำนวน 2 ชุด)
•    Logitech G923 TRUEFORCE Racing wheel พร้อม Driving Force Shifter (จำนวน 2 ชุด)
•    Pulse Elite Wireless Headset (จำนวน 2 อัน)

Nintendo Switch Zone
•    TV ขนาด 86 นิ้ว (จำนวน 1 เครื่อง)
•    Nintendo Switch OLED (จำนวน 1 เครื่อง)
•    Sofa ขนาด 2 ที่นั่ง (จำนวน 2 ตัว)

PlayStation 5 Zone
•    PlayStation 5 Slim รุ่น Ultra HD Blu-Ray Disc Drive (จำนวน 2 เครื่อง)

VR Zone
•    PlayStation 5 Slim (จำนวน 1 เครื่อง)
•    Sony PlayStation VR2 (จำนวน 1 ชุด)
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "เกม",
    "Zone",
    "TEKKEN",
    "Mario",
    "Gran Turismo"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-04027 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: ขออ้างอิงกติกา เคาน์เตอร์สไรก์ 2 ในหัวข้ออุปกรณ์ที่ใช้แข่งขัน หน่อย
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:competition_target_clarification; confidence=0.97; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:competition_target_clarification; frozen pass=False

### คำตอบก่อนแก้

ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

คำตอบ: 1. อุปกรณ์ที่อนุญาต

รายละเอียดที่เกี่ยวข้อง:
•    2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง
•    6. อุปกรณ์และการตั้งค่าเกม

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

### คำตอบหลังแก้

ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03703 — studio_rules_penalties

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ช่วยตอบจากข้อมูลที่ยืนยันได้หน่อย: ขอข้อมูลเรื่องระงับสิมธิ์ชั่วคราว
- Legacy expected: ['penalty']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

หากผู้ใช้งานละเมิดกฎซ้ำหรือกระทำการรุนแรง อาจถูกระงับสิทธิ์การใช้งานชั่วคราวเป็นระยะเวลา 1-7 วัน ขึ้นอยู่กับลักษณะของการละเมิด
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-00042 — service_fee

- Priority: P0 wrong task/target or omitted facet
- Evidence: paired_regression_primary_cause_pending
- คำถาม: บุคคลทั่วไป เล่น PS5 30 นาที เสียกี่บาื
- Legacy expected: ['service_fee']; answer_available
- ก่อนแก้: pipeline:protected_public_access; confidence=0.98; source IDs=['reservation_public_access_reviewed_20260924']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:deterministic_calculator_fast; frozen pass=True

### คำตอบก่อนแก้

ได้ครับ บุคคลทั่วไปสามารถจองใช้บริการ PlayStation 5 ได้ ค่าบริการขึ้นกับประเภทบริการและกลุ่มผู้ใช้ ต้องจองผ่านระบบและแสดงบัตรประชาชนเมื่อเช็กอิน
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ระยะเวลาที่ถามคือ 30 นาที ใช้ 1 session ตามแพ็กเกจ PlayStation 5 60 นาที
คำตอบราคา: 150 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
•    คำนวณจาก 150 บาท/session x 1 session = 150 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 50 บาท
•    General Adult: 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### คำตอบหลังแก้

ระยะเวลาที่ถามคือ 30 นาที ใช้ 1 session ตามแพ็กเกจ PlayStation 5 60 นาที
คำตอบราคา: 150 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
•    คำนวณจาก 150 บาท/session x 1 session = 150 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 50 บาท
•    General Adult: 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "General Adult",
    "0 บาท"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-04898 — compound_context_boundary

- Priority: P0 wrong task/target or omitted facet
- Evidence: paired_regression_primary_cause_pending
- คำถาม: นักศึกษา PSU เล่น PS5 1 ชั่วโมง เสียกี่าบท แล้วจองยังไง
- Legacy expected: ['equipment', 'games', 'multi_question', 'reservation']; answer_available
- ก่อนแก้: pipeline:multi_question_splitter; confidence=0.55; source IDs=['booking_steps']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:multi_question_splitter; frozen pass=True

### คำตอบก่อนแก้

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: นักศึกษา PSU เล่น PS5 1 ชั่วโมง เสียกี่าบท
ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

คำถามที่ 2: จองยังไง
ขั้นตอนจองโดยสรุป:
•    เลือกบริการหรือโซนที่ต้องการใช้
•    เลือกวันและรอบเวลาที่ต้องการ
•    กรอก Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล และเบอร์โทรศัพท์
•    ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง
•    หลังจองต้องชำระเงินภายใน 10 นาที
•    แนบสลิปและยืนยันการจอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: นักศึกษา PSU เล่น PS5 1 ชั่วโมง เสีย กี่บาท
ระยะเวลาที่ถามคือ 1 ชั่วโมง ใช้ 1 session ตามแพ็กเกจ PlayStation 5 60 นาที
คำตอบราคา: 0 บาท สำหรับกลุ่ม PSU Student and Staff
•    คำนวณจาก 0 บาท/session x 1 session = 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 50 บาท
•    General Adult: 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

คำถามที่ 2: จะเล่น นักศึกษา PSU เล่น PS5 1 ชั่วโมง เสีย จองยังไง
ขั้นตอนจองโดยสรุป:
•    เลือกบริการหรือโซนที่ต้องการใช้
•    เลือกวันและรอบเวลาที่ต้องการ
•    กรอก Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล และเบอร์โทรศัพท์
•    ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง
•    หลังจองต้องชำระเงินภายใน 10 นาที
•    แนบสลิปและยืนยันการจอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: นักศึกษา PSU เล่น PS5 1 ชั่วโมง เสีย กี่บาท
ระยะเวลาที่ถามคือ 1 ชั่วโมง ใช้ 1 session ตามแพ็กเกจ PlayStation 5 60 นาที
คำตอบราคา: 0 บาท สำหรับกลุ่ม PSU Student and Staff
•    คำนวณจาก 0 บาท/session x 1 session = 0 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: PSU Student and Staff

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 50 บาท
•    General Adult: 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

คำถามที่ 2: จะเล่น นักศึกษา PSU เล่น PS5 1 ชั่วโมง เสีย จองยังไง
ขั้นตอนจองโดยสรุป:
•    เลือกบริการหรือโซนที่ต้องการใช้
•    เลือกวันและรอบเวลาที่ต้องการ
•    กรอก Student ID/Staff ID/National ID, ชื่อ, นามสกุล, อีเมล และเบอร์โทรศัพท์
•    ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง
•    หลังจองต้องชำระเงินภายใน 10 นาที
•    แนบสลิปและยืนยันการจอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "จอง",
    "เลือก",
    "บริการ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-04969 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: อธิบายคำว่า latency ในระบบคอพมิวเตอร์แบบสั้น ๆ ตอบเป็นภาษาไทย
- Legacy expected: ['general', 'knowledge']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.763; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "latency",
    "หน่วง"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04948 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: server กับ client ต่าางกันยังไง
- Legacy expected: ['general', 'knowledge', 'no_answer']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "server",
    "client"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04518 — members_overview_contact

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: นายสุพศิน อะนะฝรั่ง มีตำแห่งอะไร
- Legacy expected: ['members', 'overview']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

นายสุพศิน อะนะฝรั่ง: นักศึกษาสหกิจ Web & AI Developer
หมวด: cooperative education and Internship student
สังกัด/รายละเอียด: วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
ระยะเวลา: 12/1/2026 - 8/5/2026
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "นายสุพศิน อะนะฝรั่ง",
    "นักศึกษาสหกิจ Web & AI Developer"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-00956 — live_booking

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: ช่วยตอบจากข้อมูลที่ยืนยันได้หน่อย: PC กับ VR ตอนสามโมงว่าไหม
- Legacy expected: ['reservation', 'schedule']; live_lookup_required
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.456; reason=base=0.72; multi_domain; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

วันที่ 2026-10-01 (เวลาไทย) ยังยืนยันสถานะเปิด-ปิดและ Slot แบบสดไม่ได้ เพราะ Booking Dashboard ไม่พร้อมใช้งานครับ
ผมจะไม่เอาตารางเก่ามาแสดงว่าเป็นข้อมูลจองแบบสด กรุณาลองใหม่อีกครั้งหรือดูหน้าจองโดยตรง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-01507 — schedule_calendar

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: กำลังวางแผนไปใช้บริการ เลยอยากทราบว่า เอาอสหารเข้าไดไหม
- Legacy expected: ['penalty', 'rules']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

นำอาหารหรือเครื่องดื่มเข้ามาได้ครับ แต่รับประทานหรือดื่มได้เฉพาะพื้นที่ที่ศูนย์กำหนด ไม่ใช่ทุกจุดในห้องเล่นเกม
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "เปิด",
    "ปิด",
    "จอง",
    "ยกเลิก",
    "นาที",
    "อาหาร",
    "ปรับ",
    "กติกา"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-01283 — schedule_calendar

- Priority: P0 wrong task/target or omitted facet
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ตอนนี้ศูนย์เปิดไหหม
- Legacy expected: ['reservation', 'schedule']; live_lookup_required
- ก่อนแก้: pipeline:rag_direct_curated; confidence=0.84; source IDs=['schedule.closure.2026-07-28::th::note', 'schedule.closure.2026-07-29::th::note', 'schedule.closure.2026-07-30::th::note']
- Top candidate: structured.schedule; score=0.928; reason=base=0.86; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=schedule; question_frame_domain_match; question_frame_operation=schedule_lookup; precondition=schedule_query_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:rag_direct_curated; frozen pass=False

### คำตอบก่อนแก้

ศูนย์ปิดให้บริการตามวันหยุดราชการ/วันปิดพิเศษที่ระบุไว้ในระบบ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ศูนย์ปิดให้บริการตามวันหยุดราชการ/วันปิดพิเศษที่ระบุไว้ในระบบ

### คำตอบหลังแก้

ศูนย์ปิดให้บริการตามวันหยุดราชการ/วันปิดพิเศษที่ระบุไว้ในระบบ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-01371 — schedule_calendar

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ขอสอบถามหย่อยครับ วันหยุดเปิดไหม
- Legacy expected: ['reservation', 'schedule']; answer_available
- ก่อนแก้: pipeline:calendar_date_clarification_fast_path; confidence=0.96; source IDs=['Reservation']
- Top candidate: structured.schedule; score=0.928; reason=base=0.86; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=schedule; question_frame_domain_match; question_frame_operation=schedule_lookup; precondition=schedule_query_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:calendar_date_clarification_fast_path; frozen pass=False

### คำตอบก่อนแก้

หมายถึงวันหยุดวันที่เท่าไรครับ? วันหยุดราชการไม่ได้ทำให้ศูนย์ปิดโดยอัตโนมัติ ต้องตรวจวันปิดพิเศษที่บันทึกไว้และตารางบริการของวันที่นั้นก่อน
แหล่งข้อมูลตารางบริการ: https://esports.computing.psu.ac.th/reservation

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

หมายถึงวันหยุดวันที่เท่าไรครับ? วันหยุดราชการไม่ได้ทำให้ศูนย์ปิดโดยอัตโนมัติ ต้องตรวจวันปิดพิเศษที่บันทึกไว้และตารางบริการของวันที่นั้นก่อน
แหล่งข้อมูลตารางบริการ: https://esports.computing.psu.ac.th/reservation

### คำตอบหลังแก้

หมายถึงวันหยุดวันที่เท่าไรครับ? วันหยุดราชการไม่ได้ทำให้ศูนย์ปิดโดยอัตโนมัติ ต้องตรวจวันปิดพิเศษที่บันทึกไว้และตารางบริการของวันที่นั้นก่อน
แหล่งข้อมูลตารางบริการ: https://esports.computing.psu.ac.th/reservation

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "เปิด",
    "ปิด",
    "เวลา",
    "วัน",
    "ไม่เปิด"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-03879 — studio_rules_penalties

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: ถ้าจะไปใช้บริการจริง ขอข้อมูลเรื่องระงับสิทธิ์ชั่วึราว
- Legacy expected: ['penalty']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=['Reservation']
- Top candidate: fast.domain_handlers; score=0.539; reason=base=0.78; multi_domain; answer_type_match; tool_router_action=fast_path; precondition=domain_fast_handler_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด penalty ตอนนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

หากผู้ใช้งานละเมิดกฎซ้ำหรือกระทำการรุนแรง อาจถูกระงับสิทธิ์การใช้งานชั่วคราวเป็นระยะเวลา 1-7 วัน ขึ้นอยู่กับลักษณะของการละเมิด
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด penalty ตอนนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04547 — members_overview_contact

- Priority: P0 wrong task/target or omitted facet
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ขอข้อมูลเร่องpsu esports คืออะไร
- Legacy expected: ['overview']; answer_available
- ก่อนแก้: pipeline:category_rule_fast_path; confidence=0.9; source IDs=['rule_overview_identity']
- Top candidate: structured.games; score=0.522; reason=base=0.88; question_frame_domain_mismatch; precondition=specific_game_detail_allowed
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:category_rule_fast_path; frozen pass=False

### คำตอบก่อนแก้

PSU Esports Studio - Phuket คือศูนย์พัฒนาการเรียนรู้ด้านอีสปอร์ตเพื่อความเป็นเลิศและขับเคลื่อนเศรษฐกิจในพื้นที่ภาคใต้ สาขาภูเก็ต ของมหาวิทยาลัยสงขลานครินทร์ และดำเนินการโดยวิทยาลัยการคอมพิวเตอร์
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

PSU Esports Studio - Phuket คือศูนย์พัฒนาการเรียนรู้ด้านอีสปอร์ตเพื่อความเป็นเลิศและขับเคลื่อนเศรษฐกิจในพื้นที่ภาคใต้ สาขาภูเก็ต ของมหาวิทยาลัยสงขลานครินทร์ และดำเนินการโดยวิทยาลัยการคอมพิวเตอร์
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### คำตอบหลังแก้

PSU Esports Studio - Phuket คือศูนย์พัฒนาการเรียนรู้ด้านอีสปอร์ตเพื่อความเป็นเลิศและขับเคลื่อนเศรษฐกิจในพื้นที่ภาคใต้ สาขาภูเก็ต ของมหาวิทยาลัยสงขลานครินทร์ และดำเนินการโดยวิทยาลัยการคอมพิวเตอร์
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04873 — compound_context_boundary

- Priority: P0 wrong task/target or omitted facet
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Cockpit จองนังไง แล้วเปิวันไหนบ้าง
- Legacy expected: ['multi_question']; answer_available
- ก่อนแก้: pipeline:structured_booking_selection; confidence=0.96; source IDs=['booking_selection_cockpit']
- Top candidate: structured.reservation; score=0.999; reason=base=0.86; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=reservation; question_frame_domain_match; question_frame_operation=booking_lookup; precondition=reservation_or_booking_query
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:structured_booking_selection; frozen pass=False

### คำตอบก่อนแก้

ถ้าอยากเล่นเกมขับรถหรือใช้พวงมาลัย ให้จอง Cockpit Zone / Cockpit ครับ
•    โซนนี้ใช้กับชุด Racezone Full Cockpit V3 และ Logitech G923 TRUEFORCE Racing Wheel
•    เกมที่ยืนยันได้คือ Gran Turismo 7
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: Cockpit จองยังไง
ถ้าอยากเล่นเกมขับรถหรือใช้พวงมาลัย ให้จอง Cockpit Zone / Cockpit ครับ
•    โซนนี้ใช้กับชุด Racezone Full Cockpit V3 และ Logitech G923 TRUEFORCE Racing Wheel
•    เกมที่ยืนยันได้คือ Gran Turismo 7
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

คำถามที่ 2: เปิดวันไหนบ้าง
เวลาบริการตามตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00

รายละเอียดจากตาราง:
•    วันจันทร์: Morning 09:00-12:00 = maintenance, Afternoon 13:00-16:00 = open
•    วันอังคาร: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันพุธ: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันพฤหัสบดี: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = open
•    วันศุกร์: Morning 09:00-12:00 = open, Afternoon 13:00-16:00 = maintenance
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ถ้าอยากเล่นเกมขับรถหรือใช้พวงมาลัย ให้จอง Cockpit Zone / Cockpit ครับ
•    โซนนี้ใช้กับชุด Racezone Full Cockpit V3 และ Logitech G923 TRUEFORCE Racing Wheel
•    เกมที่ยืนยันได้คือ Gran Turismo 7
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "Cockpit",
    "จอง",
    "เปิด"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-04756 — compound_context_boundary

- Priority: P0 wrong task/target or omitted facet
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ขอช้อมูลเรื่องอาหาร ถึงโต๊ะ
- Legacy expected: ['no_answer']; no_answer_expected
- ก่อนแก้: pipeline:protected_food_consumption; confidence=0.98; source IDs=['rule_food_drink']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:protected_food_consumption; frozen pass=False

### คำตอบก่อนแก้

อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04994 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: แปลคำ่า reservation เป็ยภาษาไทย ขอ 1 ย่อหน้า
- Legacy expected: ['general', 'knowledge', 'no_answer']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.759; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "จอง"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03905 — studio_rules_penalties

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ช่วยยืนยันให้ทีว่า ขอข้อมูลเรื่องสูบยุหรี่
- Legacy expected: ['rules']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04999 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: อธิบายคำว่่า latency ในระบบคอมพิวเตอร์แบบสั้น ๆ อธิบายให้มือใหม่เข้าใจ
- Legacy expected: ['general', 'knowledge']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.763; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "latency",
    "หน่วง"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-02641 — game_detail

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: กำลังวางแผนไปใใช้บริการ เลยอยากทราบว่า Little Nightmares II เล่นได้ที่โซนไหน
- Legacy expected: ['games']; answer_available
- ก่อนแก้: pipeline:structured_service_game_availability_no_match; confidence=0.91; source IDs=['availability_ps5_01_02', 'availability_nintendo_1_2', 'availability_nintendo_1_4']
- Top candidate: structured.games; score=0.999; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=games; question_frame_domain_match; question_frame_operation=game_detail; precondition=game_domain_or_catalog_query
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:structured_service_game_availability; frozen pass=True

### คำตอบก่อนแก้

PlayStation 5 #01-#02 ไม่มี Little Nightmares II ครับ
Little Nightmares II เล่นได้ที่ Nintendo Switch (1-2 Persons), Nintendo Switch (1-4 Persons)

เกมที่มีใน PlayStation 5 #01-#02:
•    Call of Duty: Modern Warfare III
•    Delta Force
•    EA Sports FC 24
•    eFootball
•    FINAL FANTASY XVI
•    Fortnite
•    God of War Ragnarok
•    Hogwarts Legacy
•    Marvel's Spider-Man 2
•    NARUTO X BORUTO Ultimate Ninja Storm Connections
•    Resident Evil 4
•    Resident Evil Village
•    TEKKEN 8
•    THE FINALS
•    The Last of Us Part I
•    The Last of Us Part II (Remastered)
•    Uncharted: Legacy of Thieves Collection
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

PlayStation 5 #01-#02 ไม่มี Little Nightmares II ครับ
Little Nightmares II เล่นได้ที่ Nintendo Switch (1-2 Persons), Nintendo Switch (1-4 Persons)

เกมที่มีใน PlayStation 5 #01-#02:
•    Call of Duty: Modern Warfare III
•    Delta Force
•    EA Sports FC 24
•    eFootball
•    FINAL FANTASY XVI
•    Fortnite
•    God of War Ragnarok
•    Hogwarts Legacy
•    Marvel's Spider-Man 2
•    NARUTO X BORUTO Ultimate Ninja Storm Connections
•    Resident Evil 4
•    Resident Evil Village
•    TEKKEN 8
•    THE FINALS
•    The Last of Us Part I
•    The Last of Us Part II (Remastered)
•    Uncharted: Legacy of Thieves Collection
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ได้ครับ Little Nightmares II เล่นได้ที่ Nintendo Switch Zone - Nintendo Switch (1-2 Persons), Nintendo Switch Zone - Nintendo Switch (1-4 Persons)
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "Nintendo Switch Zone"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04563 — members_overview_contact

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: กำลังวสงแผนจะไปใช้บริการ พดีอยากรู้ว่า ใครดูแลศูนย์
- Legacy expected: ['members', 'overview']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04957 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: GPU คืออะไรแบบเข้าใจง่าย ตอบสัน ๆ
- Legacy expected: ['general', 'knowledge']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: llm.general_answer; score=0.763; reason=base=0.66; domain_match; answer_type_match; tool_router_action=general_llm; tool_router_domain=general; general_route_priority; question_frame_domain_match; precondition=general_llm_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "GPU",
    "กราฟิก"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03693 — studio_rules_penalties

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ขอสอบถามหน่อยครับ กำลังวางแผนนจะไปใช้บริการ พอดีอยากรู้ว่า อัดวิดีโอในศูนย์ได้ไหม
- Legacy expected: ['no_answer', 'overview', 'rules']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04698 — members_overview_contact

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ขอสอบถามหน่อยครับ กำลังวางแผนจะไปใช้บริการ พอดีอยากรู้ว่า ใครดูแลศนูย์
- Legacy expected: ['members', 'overview']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-03702 — studio_rules_penalties

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ช่วยตอบจากข้อมูลที่ยืนยันได้หน่อย: ขอข้อมูลเรื่องคำพูดไม่หมาัสม
- Legacy expected: ['rules']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

กรุณางดส่งเสียงดังเกินควร และห้ามพูดจาดูหมิ่นหรือเสียดสีผู้อื่น
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04896 — compound_context_boundary

- Priority: P0 wrong task/target or omitted facet
- Evidence: trace_code_source_inspected
- คำถาม: บุคคลทั่วไป เล่น PC 2 ชั่วโมง เสียกี่บาท แล้วของยังไง
- Legacy expected: ['equipment', 'games', 'multi_question', 'reservation']; answer_available
- ก่อนแก้: pipeline:deterministic_calculator_fast; confidence=0.97; source IDs=['service_fee_image_2026', 'pc_service_fee_local_update_20260727']
- Top candidate: fast.price_calculator; score=0.999; reason=base=0.93; domain_match; answer_type_match; tool_router_domain=service_fee; price_calculation_priority; question_frame_domain_match; question_frame_operation=price_lookup; precondition=price_calculator_applicable
- สาเหตุ/ขอบเขตการยืนยัน: ของยังไง is real-word-looking corruption of จองยังไง; preflight/split remain one part, price answer excludes booking task. Contract needs each task plus correct price, not OR of booking words.
- หลังแก้: pipeline:deterministic_calculator_fast; frozen pass=False

### คำตอบก่อนแก้

ระยะเวลาที่ถามคือ 2 ชั่วโมง ใช้ 2 session ตามแพ็กเกจ PC 1 ชั่วโมง
คำตอบราคา: 140 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
•    คำนวณจาก 70 บาท/session x 2 session = 140 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
PC 1 ชั่วโมง (1 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 25 บาท
•    General Adult: 70 บาท
หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: บุคคลทั่วไป เล่น PC 2 ชั่วโมง เสีย กี่บาท
ระยะเวลาที่ถามคือ 2 ชั่วโมง ใช้ 2 session ตามแพ็กเกจ PC 1 ชั่วโมง
คำตอบราคา: 140 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
•    คำนวณจาก 70 บาท/session x 2 session = 140 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
PC 1 ชั่วโมง (1 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 25 บาท
•    General Adult: 70 บาท
หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

คำถามที่ 2: จะเล่น บุคคลทั่วไป เล่น PC 2 ชั่วโมง เสีย จองยังไง
จองคิวเล่นเกม/ใช้อุปกรณ์ได้ผ่านระบบจองออนไลน์ครับ
ถ้าต้องการจอง PC ให้เลือกเครื่อง PC/บริการ PC ที่ต้องการและเลือกรอบเวลา
ขั้นตอนโดยสรุปคือ 1) เลือกบริการหรือโซนที่ต้องการใช้ 2) เลือกวันและรอบเวลา 3) กรอก Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล และเบอร์โทรศัพท์ 4) ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง 5) แนบสลิปและยืนยันการจอง
ต้องจองล่วงหน้าอย่างน้อย 1 ชั่วโมง และหลังจองต้องชำระเงินภายใน 10 นาทีครับ
แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### คำตอบหลังแก้

ระยะเวลาที่ถามคือ 2 ชั่วโมง ใช้ 2 session ตามแพ็กเกจ PC 1 ชั่วโมง
คำตอบราคา: 140 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
•    คำนวณจาก 70 บาท/session x 2 session = 140 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
PC 1 ชั่วโมง (1 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 25 บาท
•    General Adult: 70 บาท
หมายเหตุข้อมูล PC: ราคา PC เพิ่มจาก local service fee update 2026-07-27
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "จอง",
    "เลือก",
    "บริการ"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-01286 — schedule_calendar

- Priority: P0 wrong task/target or omitted facet
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: ตอนนี้ศูนย์เปืดมั้ย
- Legacy expected: ['reservation', 'schedule']; live_lookup_required
- ก่อนแก้: pipeline:rag_direct_curated; confidence=0.84; source IDs=['schedule.closure.2026-07-28::th::note', 'schedule.closure.2026-07-29::th::note', 'schedule.closure.2026-07-30::th::note']
- Top candidate: structured.schedule; score=0.928; reason=base=0.86; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=schedule; question_frame_domain_match; question_frame_operation=schedule_lookup; precondition=schedule_query_applicable
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:rag_direct_curated; frozen pass=False

### คำตอบก่อนแก้

ศูนย์ปิดให้บริการตามวันหยุดราชการ/วันปิดพิเศษที่ระบุไว้ในระบบ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ศูนย์ปิดให้บริการตามวันหยุดราชการ/วันปิดพิเศษที่ระบุไว้ในระบบ

### คำตอบหลังแก้

ศูนย์ปิดให้บริการตามวันหยุดราชการ/วันปิดพิเศษที่ระบุไว้ในระบบ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04768 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ขอข้อมูลเรื่่องsteam ผ่านศูนย์
- Legacy expected: ['no_answer']; no_answer_expected
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-04716 — members_overview_contact

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ขอสอบถามหน่อยครับ รศ.ดร.พันธ์ ทองชุมนุม ทำตำแหน่องะไร
- Legacy expected: ['members', 'overview']; answer_available
- ก่อนแก้: pipeline:candidate_margin_clarification; confidence=0.62; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:candidate_margin_clarification; frozen pass=False

### คำตอบก่อนแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี
หมวด: Members
สังกัด/รายละเอียด: มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/about-us/Members

### คำตอบหลังแก้

ขอรายละเอียดเพิ่มนิดนึงครับ ต้องการถามเรื่องเกม ปุ่ม ราคา การจอง อุปกรณ์ หรือตารางเวลา?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "รองอธิการบดี",
    "รศ.ดร.พันธ์"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-03911 — studio_rules_penalties

- Priority: P2 source/ambiguity/label review
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: ช่วยยทนยันให้ทีว่า อัดวิดีโอในศูนย์ได้ไหม
- Legacy expected: ['no_answer', 'overview', 'rules']; no_answer_expected
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-TH-01867 — games_catalog_availability

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: ถ้าจะเล่น Mario Party Superstars ต้องจงออะไร
- Legacy expected: ['games', 'reservation']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=['Reservation']
- Top candidate: structured.reservation; score=0.999; reason=base=0.86; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=reservation; question_frame_domain_match; question_frame_operation=booking_lookup; precondition=reservation_or_booking_query
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ถ้าจะเล่น Mario Party Superstars ให้จอง Nintendo Switch Zone - Nintendo Switch (1-2 Persons) หรือ Nintendo Switch Zone - Nintendo Switch (1-4 Persons) ครับ
•    Nintendo Switch Zone - Nintendo Switch (1-2 Persons) (60 นาที, 1-2 คน)
•    Nintendo Switch Zone - Nintendo Switch (1-4 Persons) (60 นาที, 1-4 คน)
จากนั้นเลือกวัน รอบเวลา กรอกข้อมูลผู้ใช้บริการ ชำระเงิน และแนบสลิปเพื่อยืนยันการจอง
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด reservation ตอนนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "Nintendo Switch (1-2 Persons)",
    "Nintendo Switch",
    "Mario Party Superstars"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-03382 — equipment

- Priority: P0 wrong task/target or omitted facet
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: Nintendo Switch Zone มีอะไรให้ใข้บ้าง
- Legacy expected: ['clarification', 'equipment']; answer_available
- ก่อนแก้: pipeline:structured_games_genre_list; confidence=0.95; source IDs=['our_games_genre']
- Top candidate: structured.games; score=0.999; reason=base=0.88; domain_match; answer_type_match; tool_router_action=structured; tool_router_domain=games; question_frame_domain_match; question_frame_operation=game_detail; precondition=game_domain_or_catalog_query
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:structured_games_genre_list; frozen pass=False

### คำตอบก่อนแก้

เกมแนว Sports / เกมกีฬา ที่พบในรายการเกมที่ยืนยันได้:

Nintendo Switch Sports
•    แนวเกม: เกมกีฬา Motion Control
•    เล่นได้ที่: Nintendo Switch Zone
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

เกมแนว Sports / เกมกีฬา ที่พบในรายการเกมที่ยืนยันได้:

Nintendo Switch Sports
•    แนวเกม: เกมกีฬา Motion Control
•    เล่นได้ที่: Nintendo Switch Zone
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### คำตอบหลังแก้

เกมแนว Sports / เกมกีฬา ที่พบในรายการเกมที่ยืนยันได้:

Nintendo Switch Sports
•    แนวเกม: เกมกีฬา Motion Control
•    เล่นได้ที่: Nintendo Switch Zone
แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Services/our-games

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "อุปกรณ์",
    "หมายถึงเรื่องไหน",
    "Zone"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-TH-00161 — service_fee

- Priority: P1 task/qualifier or English evidence
- Evidence: selection_reason_confirmed_primary_cause_pending
- คำถาม: คนทั่วไป เล่น PS5 3 ชั่วโมง เสีบกี่าท
- Legacy expected: ['service_fee']; answer_available
- ก่อนแก้: pipeline:no_answer; confidence=0.55; source IDs=[]
- Top candidate: retrieval.hybrid_guarded; score=0.433; reason=base=0.72; answer_type_match; precondition=no_specific_precondition
- สาเหตุ/ขอบเขตการยืนยัน: The top capability is below its execution threshold; low score reflects missing operation/verified target signals. The trace does not prove that every input should be auto-corrected.
- หลังแก้: pipeline:no_answer; frozen pass=False

### คำตอบก่อนแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

ระยะเวลาที่ถามคือ 3 ชั่วโมง ใช้ 3 session ตามแพ็กเกจ PlayStation 5 60 นาที
คำตอบราคา: 450 บาท สำหรับกลุ่ม General Adult / บุคคลทั่วไป
•    คำนวณจาก 150 บาท/session x 3 session = 450 บาท
กลุ่มผู้ใช้ที่ตรวจเจอ: General Adult / บุคคลทั่วไป

รายละเอียดจากตาราง:
PlayStation 5 60 นาที (1 ชั่วโมง, 1-2 คน)
•    PSU Student and Staff: 0 บาท
•    PSU Alumni and General Student: 50 บาท
•    General Adult: 150 บาท
แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png

### คำตอบหลังแก้

ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับคำถามนี้ครับ

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "บาท",
    "บาท",
    "ฟรี"
  ],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-00143 — service_fee

- Priority: P1 task/qualifier or English evidence
- Evidence: trace_code_source_inspected
- คำถาม: NARUTO X BORUTO Ultimate Ninja Storm Connections rice
- Legacy expected: ['service_fee']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.99; source IDs=['game_detail_naruto_x_boruto']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: rice removes price task and sends exact game toward detail localization. Missing localization is downstream symptom; primary intent ambiguity is pay/play-like collision.
- หลังแก้: pipeline:structured_game_detail_en; frozen pass=False

### คำตอบก่อนแก้

NARUTO X BORUTO Ultimate Ninja Storm Connections: This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Which service, duration, and user group should I price: PC, PlayStation 5, Nintendo Switch, Cockpit, or VR?

### คำตอบหลังแก้

Verified English information:
NARUTO X BORUTO Ultimate Ninja Storm Connections
Genre: Fighting game from anime
Overview: NARUTO X BORUTO Ultimate Ninja Storm Connections is a fighting game featuring characters from the Naruto/Boruto universe.
How to play: Select a character, use combos, ninja skills, and timing for dodging and countering to defeat your opponent
Available at: PlayStation 5 Zone
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04469 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: trace_code_source_inspected
- คำถาม: Could you please hwlp me with this: I am prparing for a T8 match. What is the policy for dispute resolution
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_tekken8_psu_esports_s08_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean and noisy both localization_pending. Selected Tekken8 dispute card exists in Thai; text/section_title missing in active approved registry. No LLM rewrite/translation preview.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Tekken 8 competition rules:
- Dispute Resolution * Any issues must be reported to the competition organizer immediately. * In cases of disputes or protests, the decision of the supervisors or referees shall be final. Note: The competition organizer reserves the right to amend or modify these regulations without prior notice.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04236 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: For Valorant, can you verify the rule on pausees and timeouts
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_valorant_psu_phuket_2026_s20_c01', 'competition_rules_valorant_psu_phuket_2026_s21_c01', 'competition_rules_valorant_psu_phuket_2026_s23_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified VALORANT competition rules:
- 1. Tactical Timeout * Each team may request up to 2 timeouts per map during regulation (first 24 rounds), each lasting 60 seconds. * During Overtime, each team receives 1 additional timeout. Timeouts from regulation do not carry over.
- There are three main types of pauses, each for different purposes
- 3. Player Emergency Pause * Each team may request 1 pause per map. * Total emergency pause time may not exceed 10 minutes per match. If the time limit is exceeded, the affected player may be disqualified from continuing and must be replaced by a substitute Bug Regulations
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04011 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: How is player conduct and sportsmanship handled in the Counter-Strike 2 tournmaent rules
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s35_c01', 'competition_rules_cs2_psu_phuket_2026_s36_c01', 'competition_rules_cs2_psu_phuket_2026_s54_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Player conduct: aggressive behavior, hate speech (racial/religious), and unsportsmanlike actions are prohibited.
- Behavior and Penalties
- 8. Penalty Table (Penalties) Violation Penalty Insulting / using verbal aggression Warning → Loss in that round → Disqualification Cheating in any form Loss in that round / Disqualification from competition Watching streams during gameplay Loss in that match Stopping the game without permission Loss in that round Using bugs Loss in that round or match...
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04038 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: For Counter-Strike 2, can you verify the rule on in-match proceure
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s30_c01', 'competition_rules_cs2_psu_phuket_2026_s33_c01', 'competition_rules_cs2_psu_phuket_2026_s08_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Step-by-step competition procedure
- Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.
- The competition will be held for one day at PSU Esports Studio - Phuket, Prince of Songkla University, Phuket Campus.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04309 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could yyou please help me with this: How is fair play and prohibited conduct handled in the Counter-Strike 2 tournament rules
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s35_c01', 'competition_rules_cs2_psu_phuket_2026_s36_c01', 'competition_rules_cs2_psu_phuket_2026_s54_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Player conduct: aggressive behavior, hate speech (racial/religious), and unsportsmanlike actions are prohibited.
- Behavior and Penalties
- 8. Penalty Table (Penalties) Violation Penalty Insulting / using verbal aggression Warning → Loss in that round → Disqualification Cheating in any form Loss in that round / Disqualification from competition Watching streams during gameplay Loss in that match Stopping the game without permission Loss in that round Using bugs Loss in that round or match...
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-03598 — equipment

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: Could you please help me with this: What is a gaming mmouse used for
- Legacy expected: ['equipment']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-02255 — game_detail

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: How do you pay Moving Out 2
- Legacy expected: ['games']; localization_pending
- ก่อนแก้: pipeline:game_pay_or_play_clarification; confidence=0.8; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:game_pay_or_play_clarification; frozen pass=False

### คำตอบก่อนแก้

Do you mean how to play Moving Out 2, or the service fee for the zone where it is available?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Moving Out 2: This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### คำตอบหลังแก้

Do you mean how to play Moving Out 2, or the service fee for the zone where it is available?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "Moving Out 2"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04743 — members_overview_contact

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Could you please help me with this: Who are the embers
- Legacy expected: ['members', 'overview']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Official Thai source member record(s):
Names and role titles below are shown exactly as published by PSU.
- ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี - มหาวิทยาลัยสงขลานครินทร์
- รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี - มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- รศ.ดร.อซีส นันทอมรพงศ์: คณบดี - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ - มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- นายพฤทธิ์ เกษตรสมบูรณ์: นักวิชาการคอมพิวเตอร์ - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- นายณัฐวัฒน์ นิธิคุณานนต์: นักวิชาการคอมพิวเตอร์ - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- นายชนะชัย สิริพันธ์วราภรณ์: ผู้จัดการ - PSU Esports Studio - Phuket วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- นายณภัทร เชื้อเหล่าวานิช: นักศึกษาสหกิจ Game and 3D Developer - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- Mr. Amine Abidellaoui: Internship Student - High School Bristol Cannes, France
- นายสุพศิน อะนะฝรั่ง: นักศึกษาสหกิจ Web & AI Developer - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- Mr. Yanis Igoudjil: Internship Student - Industrial Engineering and Information Systems, EPF Graduate School of Engineering, Cachan Val-De-Marne, France
- นายภาสวุฒิ ชูติประชากิจ: นักศึกษาฝึกงานโครงการ Super AI SS6 ตำแหน่ง AI Chat Bot Developer - วิศวกรรมระบบไอโอทีและสารสนเทศ สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง
- นายษุภากรณ์ จิราจินดากุล: ประธาน
- นายนพัทธ์ ฝอยทอง: รองประธาน
- นายปัณณวิชญ์ หนูเรือง: เลขานุการ
- นายภูจิตร จิรวิริยาภรณ์: เหรัญญิก
- นายธนชาติ เอ่งฉ้วน: ประชาสัมพันธ์
- นางสาวกมลวรรณ นวลสาย: กรรมการ
- นางสาวชญาภา จันทร์เอิบ: กรรมการ
- นางสาวณัฐธิดา คำทะเนตร์: กรรมการ
- นางสาวสุภาสินี ธนภพ: กรรมการ
- นางสาวอาทิตยา แดงประดับ: กรรมการ
- นายณัฐพนธ์ อินทรสังขนาวิน: กรรมการ
- นายอภิวิชญ์ เลิศกมลรักษ์: กรรมการ
- นายอรรถนนท์ สุขแก้ว: กรรมการ
Source: https://esports.phuket.psu.ac.th/about-us/Members (official Thai source)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04823 — compound_context_boundary

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: I am planning a visit and nerd to know: Where an I play this game
- Legacy expected: ['clarification', 'games', 'general']; clarification_required
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Which game do you mean? Please provide the game title so I can check its verified studio zone.

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-03462 — equipment

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: What cn a 86-inch TV be used for
- Legacy expected: ['equipment']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.99; source IDs=['equipment_tv_86']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_equipment_item_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### คำตอบหลังแก้

Verified equipment record: TV 86-inch is listed in Nintendo Switch Zone.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04409 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: I am prepparing for a AOV match. What is the policy for pauses and timeouts
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_rov_blueket_2025_men_s06_c02', 'competition_rules_rov_blueket_2025_men_s06_c03', 'competition_rules_rov_blueket_2025_men_s06_c04']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Arena of Valor (RoV) competition rules:
- 4. Competition regulations and rules: 4.3.2. If a competitor disconnects because of force majeure (such as an internet-service outage across the area or a game-server error), the affected team must notify the staff. Whether to allow a replay is at the referees' discretion.
- 4. Competition regulations and rules: 4.5.1.2 In cases where the game is paused due to technical issues, not caused by player actions, the event staff may order a pause and require players to rejoin the game after all disconnected players have reconnected.
- 4. Competition regulations and rules: 4.5.6.1.1 Physical disturbances between competitors, such as causing chaos, noise, and loud sounds that interfere with gameplay. 4.5.6.1.2 Portable devices or software malfunctioning. 4.5.6.1.3 Frame drops or increased ping outside of player control. 4.5.6.1.4 When the opposing team engages in severe cheating or disrespect.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-03900 — studio_rules_penalties

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Could you check the studio information for me? What is the studio policy for sharp objeect
- Legacy expected: ['rules']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Weapons or sharp objects are prohibited, and fighting or gambling is not allowed.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-03596 — equipment

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Could you please help me with this: What is a gamimg moue
- Legacy expected: ['equipment']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Verified equipment record: Gaming Mouse is listed in PC Zone.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04460 — competition_rules

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: Could you please help me with this: Could you cite the T8 rule concerning competiion equopment and devices
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:multi_question_splitter; confidence=0.52; source IDs=['equipment_gaming_pc', 'equipment_gaming_monitor', 'equipment_gaming_keyboard', 'equipment_gaming_mouse', 'equipment_gaming_headset', 'equipment_gaming_chair', 'equipment_logitech_g923', 'equipment_driving_force_shifter', 'equipment_racezone_cockpit_v3', 'equipment_pulse_elite_headset', 'equipment_nintendo_switch_oled', 'equipment_playstation_5_slim', 'equipment_sony_playstation_vr2', 'equipment_tv_65', 'equipment_tv_86', 'equipment_sofa_2_seats']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This question contains several topics. Here are the answers separately:

Question 1: Could you please help me with this: Could you cite the T8 rule concerning competiion equopment
I could not find verified PSU Esports Studio - Phuket information for this question.

Question 2: devices
Verified equipment:
- Gaming PC model MSI MAG Infinite S3 14th (PC Zone) - 10 Units
- Gaming Monitor (PC Zone) - 10 Units
- Gaming Keyboard (PC Zone)
- Gaming Mouse (PC Zone)
- Gaming Headset (PC Zone)
- Gaming Chair (PC Zone) - 10 Units
- Logitech G923 TRUEFORCE Racing Wheel (Cockpit Zone) - 2 Units with Driving Force Shifter
- Driving Force Shifter (Cockpit Zone) - 2 Units with Logitech G923
- Racezone Full Cockpit V3 (Cockpit Zone) - 2 Units
- Pulse Elite Wireless Headset (Cockpit Zone) - 2 Units
- Nintendo Switch OLED (Nintendo Switch Zone) - 1 Unit
- PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive (PlayStation 5 Zone / VR Zone) - 2 Units in PlayStation 5 Zone and 1 Unit in VR Zone
- Sony PlayStation VR2 (VR Zone) - 1 Unit
- TV 65 inch (Cockpit Zone) - 2 Units
- TV 86 inch (Nintendo Switch Zone) - 1 Unit
- Sofa 2 seats (Nintendo Switch Zone) - 2 Sets
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Tekken 8 competition rules:
- Competition Rules * Offline mode * PlayStation 5 console used * Singles (1v1) format * Match format: * FT2: Winner is the first to win two games * Each game uses R3 rules (3 rounds per game) and 60S rule (60 seconds per round) * If tied at 1-1, a deciding game will be played
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04388 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: Could you cite the Counter Strike 2 rule concerning teaam size
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.99; source IDs=['game_detail_cs2']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_game_detail_en; frozen pass=False

### คำตอบก่อนแก้

Counter-Strike 2: This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified English information:
Counter-Strike 2
Genre: Tactical FPS
Overview: Counter-Strike 2 is a competitive team shooter with attackers and defenders. The main objectives involve planting/defusing a bomb or eliminating opponents.
How to play: Play in rounds, must buy weapons, plan with your team, control territory, and use aiming along with communication to win the round
Available at: PC Zone
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04891 — compound_context_boundary

- Priority: P1 task/qualifier or English evidence
- Evidence: trace_code_source_inspected
- คำถาม: rice
- Legacy expected: ['clarification', 'equipment', 'games', 'no_answer', 'reservation', 'service_fee']; clarification_required
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: rice is a valid word; non-correction is intentional. Better clarification needs context; cannot certify user meant Price from synthetic edit alone.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Which service, duration, and user group should I price: PC, PlayStation 5, Nintendo Switch, Cockpit, or VR?

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04372 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me ith this: For Counter-Strike 2, can you verify the rule on the rulebook scope and tournament identity
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s01_c01', 'competition_rules_cs2_psu_phuket_2026_s02_c01', 'competition_rules_cs2_psu_phuket_2026_s03_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Scope of Application This regulation applies to all players, teams, and staff members participating officially in any CS2 competition organized by PSU Esports Studio - Phuket.
- Document overview: Competition Rules and Format for Counter-Strike 2
- PSU Phuket CS2 2026 Tournament
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-03846 — studio_rules_penalties

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: I am planning a visit and would like to know: What are the daage penalties
- Legacy expected: ['penalty']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Damage penalties depend on severity: minor damage is 100-500 THB, moderate damage is the actual cost or 500-2,000 THB, and severe damage requires full compensation for the property.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [
    "full compensation"
  ],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04570 — members_overview_contact

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Where is the studi? Could you check this fot me
- Legacy expected: ['contact']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [
    "Phuket Campus"
  ],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04435 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: How is team size hanndled in the Arena of Valor tournament rules
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_rov_blueket_2025_men_s06_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Arena of Valor (RoV) competition rules:
- 4. Competition regulations and rules: Competition Rules 4. Regulations and Competition Rules 4.1. Basic Rules 4.1.1. Prohibited to use character names or phrases that are offensive or disrespectful toward others.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-01260 — schedule_calendar

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Is the studio ope right now
- Legacy expected: ['reservation', 'schedule']; live_lookup_required
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

For 2026-10-01 (Asia/Bangkok), I cannot confirm the live opening or booking status because the Booking Dashboard is unavailable. I will not present a saved schedule as live availability. Please check the reservation page or try again shortly.
Source: https://esports.computing.psu.ac.th/reservation

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04381 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with tihs: How is the tournament schedule handled in the Counter-Strike 2 tournament rules
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s07_c01', 'competition_rules_cs2_psu_phuket_2026_s15_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Drawing of lots and schedule
- Match schedule: The tournament bracket will be announced at least 1 day in advance. Entry must be confirmed before the match starts. Late arrivals may be disqualified.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-03621 — equipment

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me wth rhis: What is the Sony PlayStation VR2 used for
- Legacy expected: ['equipment']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.99; source IDs=['equipment_sony_playstation_vr2']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_equipment_item_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### คำตอบหลังแก้

Verified equipment record: Sony PlayStation VR2 is listed in VR Zone.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04453 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: How is protests and disptes handled in the Tekken 8 tournament rules
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_tekken8_psu_esports_s08_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Tekken 8 competition rules:
- Dispute Resolution * Any issues must be reported to the competition organizer immediately. * In cases of disputes or protests, the decision of the supervisors or referees shall be final. Note: The competition organizer reserves the right to amend or modify these regulations without prior notice.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-01451 — schedule_calendar

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: Could you please help me with thhis: What should I do if I lose something
- Legacy expected: ['penalty', 'rules']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

I could not find verified PSU Esports Studio - Phuket information for this question.

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04102 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you cite the Counter Strike 2 rule concerning the rulebook scope and tournamennt identity
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s01_c01', 'competition_rules_cs2_psu_phuket_2026_s02_c01', 'competition_rules_cs2_psu_phuket_2026_s03_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Scope of Application This regulation applies to all players, teams, and staff members participating officially in any CS2 competition organized by PSU Esports Studio - Phuket.
- Document overview: Competition Rules and Format for Counter-Strike 2
- PSU Phuket CS2 2026 Tournament
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04017 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: How is protests and disputes handled in the Counter-Strike 2 tournament rulrs
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s06_c01', 'competition_rules_cs2_psu_phuket_2026_s58_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Language: The official language of the competition is Thai. All communication, protests, and reporting must be conducted in Thai, unless otherwise specified.
- Protests must be submitted within 15 minutes after the match ends, by the team captain or coach only.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04463 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: I am preparing for a T8 match. What is the policy for in-gaame settings
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_tekken8_psu_esports_s04_c01', 'competition_rules_tekken8_psu_esports_s03_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Tekken 8 competition rules:
- Game settings * Rounds per game (Round): 3 * Time per round (Timer): 60 seconds * Advantage: No advantage * Stage: Random
- Characters and settings: Characters and Setup * Any character can be selected (except DLC characters) * No character customization allowed in any case (such as clothing, hairstyle, combat effects, aura, etc.) * Only standard skins are permitted * Assist buttons or special assist systems are allowed * No use of bugs or glitches that provide an advantage * Once the game starts, no...
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-03673 — studio_rules_penalties

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Can I smke inside the studio? Please answer briefly
- Legacy expected: ['rules']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Smoking and alcoholic drinks are prohibited inside the studio.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [
    "prohibited"
  ],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-03891 — studio_rules_penalties

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Could you check the studio information for me? What is the studio polcy for dood noise damage
- Legacy expected: ['rules']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

- Food and drinks are allowed only in designated areas.
- Users should avoid excessive noise and must not insult or mock others.
- If equipment is damaged through improper or negligent use, users are responsible according to severity: minor damage carries a 100-500 THB fine; moderate damage costs the actual repair amount or 500-2,000 THB; severe damage requires full compensation based on the property's market value.
Source: https://esports.computing.psu.ac.th/reservation

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04402 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: For Arena of Valor, can you verify the rule on competition equipemnt and devices
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_rov_blueket_2025_men_s01_c01', 'competition_rules_rov_blueket_2025_men_s02_c01', 'competition_rules_rov_blueket_2025_men_s03_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Arena of Valor (RoV) competition rules:
- 5. Competition attire and equipment 5.1. Personal mobile phones and personal internet and/or university internet. 5.2. Personal power strips and battery-charging equipment. 5.3. Tablets, iPads and any devices other than mobile phones may not be used in competition. If detected, staff will immediately impose disqualification.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04297 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: How is eligibility, rostr, and rrgistration handled in the Counter-Strike 2 tournament rules
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s02_c01', 'competition_rules_cs2_psu_phuket_2026_s04_c01', 'competition_rules_cs2_psu_phuket_2026_s11_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Scope of Application This regulation applies to all players, teams, and staff members participating officially in any CS2 competition organized by PSU Esports Studio - Phuket.
- No team member changes are allowed during the competition period
- Registration of players is not permitted after the registration period has closed.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04057 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: I am preparing for a Counter Strike 2 match. What is the policy for in-game settngs
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s01_c01', 'competition_rules_cs2_psu_phuket_2026_s02_c01', 'competition_rules_cs2_psu_phuket_2026_s03_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited.
- Game Settings
- Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-03865 — studio_rules_penalties

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: I am planning a visit and would like to know: What are the studio rule? I need the official answer
- Legacy expected: ['rules']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Key studio rules:
• Leave belongings before using the service; the studio is not responsible for lost property.
• Food and drinks are allowed only in designated areas.
• Return equipment and game discs after use.
• Avoid excessive noise and insulting or sarcastic language.
• Do not move equipment or other items without permission, and do not use personal power plugs without permission.
• Smoking, drugs, alcohol, weapons, fighting, and gambling are prohibited.
• Damage to equipment may result in a repair fee or compensation based on the extent of damage.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [
    "Key studio rules"
  ],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04805 — compound_context_boundary

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Please tell me: Explain the laetst verified studio announcement. Please answer briefly
- Legacy expected: ['events_news', 'knowledge', 'no_answer']; no_answer_expected
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.95; source IDs=['english_rag_projection']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:missing_english_localization; frozen pass=False

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

I do not have a verified live news feed for that request. Please check the official PSU Esports Studio - Phuket channels.

### คำตอบหลังแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-03614 — equipment

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me wth this: What is the Pulse Elite Wireless Headset used for
- Legacy expected: ['equipment']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.99; source IDs=['equipment_pulse_elite_headset']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_equipment_item_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### คำตอบหลังแก้

Verified equipment record: Pulse Elite Wireless Headset is listed in Cockpit Zone.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-00412 — reservation_policy

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: What is the studio policy for not pay late hceck
- Legacy expected: ['reservation']; answer_available
- ก่อนแก้: pipeline:protected_price_missing_service; confidence=0.98; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:protected_price_missing_service; frozen pass=False

### คำตอบก่อนแก้

Which service would you like the fee for: PC, PlayStation 5, Nintendo Switch, Cockpit, or VR? The rate depends on the service and user group.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Which service would you like the fee for: PC, PlayStation 5, Nintendo Switch, Cockpit, or VR? The rate depends on the service and user group.

### คำตอบหลังแก้

Which service would you like the fee for: PC, PlayStation 5, Nintendo Switch, Cockpit, or VR? The rate depends on the service and user group.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04629 — members_overview_contact

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: Who is the ambasaador
- Legacy expected: ['members', 'overview']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

I could not find a verified PSU Esports Studio - Phuket member record for that requested role.

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04067 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: What do the CS2 tournamentt rules say about penalties
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s54_c01', 'competition_rules_cs2_psu_phuket_2026_s13_c01', 'competition_rules_cs2_psu_phuket_2026_s15_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- 8. Penalty Table (Penalties) Violation Penalty Insulting / using verbal aggression Warning → Loss in that round → Disqualification Cheating in any form Loss in that round / Disqualification from competition Watching streams during gameplay Loss in that match Stopping the game without permission Loss in that round Using bugs Loss in that round or match...
- Behavior and Penalties
- If any member withdraws, the team may be disqualified.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-03612 — equipment

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me wwith this: What is the Racezone Full Cockpit V3 used for
- Legacy expected: ['equipment']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.99; source IDs=['equipment_racezone_cockpit_v3']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_equipment_item_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### คำตอบหลังแก้

Verified equipment record: Racezone Full Cockpit V3 is listed in Cockpit Zone.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-00120 — service_fee

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: How are VR 30-minute sessions dfiferent from VR one-hour sessions
- Legacy expected: ['service_fee']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

The question does not specify the duration, so both verified packages are shown.
VR - 30 minutes (1-5 people)
- PSU students and staff: 0 THB
- PSU alumni and students from other institutions: 190 THB
- General adults: 525 THB
VR - 1 hour (1-5 people)
- PSU students and staff: 0 THB
- PSU alumni and students from other institutions: 375 THB
- General adults: 1,050 THB
Prices are calculated deterministically from the Service Fee 2026 table.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04829 — compound_context_boundary

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: I am planning a visit and need to know: How muh is it
- Legacy expected: ['clarification', 'general', 'service_fee']; clarification_required
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Which service would you like the fee for: PC, PlayStation 5, Nintendo Switch, Cockpit, or VR? The rate depends on the service and user group.

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04075 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: I am preparing for a Counter Strike 2 match. What is the policy for the penalty mtarix
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s13_c01', 'competition_rules_cs2_psu_phuket_2026_s15_c01', 'competition_rules_cs2_psu_phuket_2026_s35_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- If any member withdraws, the team may be disqualified.
- Match schedule: The tournament bracket will be announced at least 1 day in advance. Entry must be confirmed before the match starts. Late arrivals may be disqualified.
- Behavior and Penalties
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04083 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: How is pe-match and on-site rewuirements handled in the Counter-Strike 2 tournament rules
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s51_c01', 'competition_rules_cs2_psu_phuket_2026_s52_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Mobile phones, tablets, or smartwatches are prohibited in the competition area until the match concludes.
- Players are not allowed to bring notes or documents into the arena, but team leaders may bring them in and must hand them to the referees before every match.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04697 — members_overview_contact

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: Could you please help me with this: What is the studio policy for studio foundeer operator
- Legacy expected: ['overview']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

I could not find verified PSU Esports Studio - Phuket information for this question.

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04981 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: Explain the term latency in a computer system btiefly
- Legacy expected: ['general', 'knowledge']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

I could not find verified PSU Esports Studio - Phuket information for this question.

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-01351 — schedule_calendar

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: What are the rules in the cenetr
- Legacy expected: ['penalty', 'rules']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

I could not find verified PSU Esports Studio - Phuket information for this question.

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04830 — compound_context_boundary

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Can I biok his
- Legacy expected: ['clarification', 'general', 'reservation']; clarification_required
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Which service or zone do you want to book, and for what date and time?

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-02690 — game_controls

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: What does thr Y button do in Mario Kart Live: Home Circuit on Nintendo Switch
- Legacy expected: ['games']; answer_available
- ก่อนแก้: pipeline:game_controls_no_current_game_en; confidence=0.98; source IDs=['service_game_availability']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:game_controls_no_current_game_en; frozen pass=False

### คำตอบก่อนแก้

Mario Kart Live: Home Circuit is not listed in the current verified PSU Esports Studio - Phuket game catalog. I cannot confirm its controls for studio use or substitute Mario Kart 8 Deluxe.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Mario Kart Live: Home Circuit is not listed in the current verified PSU Esports Studio - Phuket game catalog. I cannot confirm its controls for studio use or substitute Mario Kart 8 Deluxe.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Mario Kart Live: Home Circuit is not listed in the current verified PSU Esports Studio - Phuket game catalog. I cannot confirm its controls for studio use or substitute Mario Kart 8 Deluxe.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "Y",
    "Assist"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04033 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: I am preparing for a Counter Strike 2 mach. What is the policy for fair play and prohibited conduct
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s35_c01', 'competition_rules_cs2_psu_phuket_2026_s36_c01', 'competition_rules_cs2_psu_phuket_2026_s54_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Player conduct: aggressive behavior, hate speech (racial/religious), and unsportsmanlike actions are prohibited.
- Behavior and Penalties
- 8. Penalty Table (Penalties) Violation Penalty Insulting / using verbal aggression Warning → Loss in that round → Disqualification Cheating in any form Loss in that round / Disqualification from competition Watching streams during gameplay Loss in that match Stopping the game without permission Loss in that round Using bugs Loss in that round or match...
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-01735 — games_catalog_availability

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Wheere can you play Uncharted: Legacy of Thieves Collection
- Legacy expected: ['games']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.99; source IDs=['game_detail_uncharted']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_game_detail_en; frozen pass=True

### คำตอบก่อนแก้

Uncharted: Legacy of Thieves Collection: This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Uncharted: Legacy of Thieves Collection is available on: PlayStation 5 #01-#02. Studio zone(s): PlayStation 5 Zone.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified English information:
Uncharted: Legacy of Thieves Collection
Genre: Action-Adventure
Overview: Uncharted is a treasure-hunting adventure game focused on climbing, exploration, puzzle solving and action scenes.
How to play: Explore locations, climb, solve puzzles, fight with firearms and progress through missions.
Available at: PlayStation 5 Zone
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04440 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you lease help me with this: Please retrieve the official TEKKEN 8 rulebook evidence for the competition format
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_tekken8_psu_esports_s02_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Tekken 8 competition rules:
- Competition Rules * Offline mode * PlayStation 5 console used * Singles (1v1) format * Match format: * FT2: Winner is the first to win two games * Each game uses R3 rules (3 rounds per game) and 60S rule (60 seconds per round) * If tied at 1-1, a deciding game will be played
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04894 — compound_context_boundary

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Ewuipent
- Legacy expected: ['clarification', 'equipment', 'games', 'no_answer', 'reservation', 'service_fee']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Verified equipment:
- Gaming PC model MSI MAG Infinite S3 14th (PC Zone) - 10 Units
- Gaming Monitor (PC Zone) - 10 Units
- Gaming Keyboard (PC Zone)
- Gaming Mouse (PC Zone)
- Gaming Headset (PC Zone)
- Gaming Chair (PC Zone) - 10 Units
- Logitech G923 TRUEFORCE Racing Wheel (Cockpit Zone) - 2 Units with Driving Force Shifter
- Driving Force Shifter (Cockpit Zone) - 2 Units with Logitech G923
- Racezone Full Cockpit V3 (Cockpit Zone) - 2 Units
- Pulse Elite Wireless Headset (Cockpit Zone) - 2 Units
- Nintendo Switch OLED (Nintendo Switch Zone) - 1 Unit
- PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive (PlayStation 5 Zone / VR Zone) - 2 Units in PlayStation 5 Zone and 1 Unit in VR Zone
- Sony PlayStation VR2 (VR Zone) - 1 Unit
- TV 65 inch (Cockpit Zone) - 2 Units
- TV 86 inch (Nintendo Switch Zone) - 1 Unit
- Sofa 2 seats (Nintendo Switch Zone) - 2 Sets
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04464 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: Please retrieve th official TEKKEN 8 rulebook evidence for in-game settings
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_tekken8_psu_esports_s04_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Tekken 8 competition rules:
- Game settings * Rounds per game (Round): 3 * Time per round (Timer): 60 seconds * Advantage: No advantage * Stage: Random
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04588 — members_overview_contact

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: I am planning a visit and need to know: How can I cotnact the studio
- Legacy expected: ['contact', 'overview']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Contact PSU Esports Studio - Phuket by email at psuesportspkt@gmail.com, by phone at +66 7627 6004 or +66 7627 6045, or through https://www.facebook.com/psuesportsphuket.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-01778 — games_catalog_availability

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Whete can VALORANT be plaed
- Legacy expected: ['games']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.99; source IDs=['game_detail_valorant']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_game_detail_en; frozen pass=True

### คำตอบก่อนแก้

VALORANT: This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

VALORANT is available on: PC #01-#02, PC #03-#10. Studio zone(s): PC Zone.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified English information:
VALORANT
Genre: Tactical 5v5 team-based FPS
Overview: VALORANT is a tactical shooter game where players select agents with unique skills and play as either attackers or defenders in each round.
How to play: Attackers must plant the Spike; defenders must defend the area or defuse the Spike. Play emphasizes aiming, communication, ability use and teamwork.
Available at: PC Zone
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04007 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: What do the CS2 tournaent rules say about player conduct and sportsmanship
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s35_c01', 'competition_rules_cs2_psu_phuket_2026_s36_c01', 'competition_rules_cs2_psu_phuket_2026_s54_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Player conduct: aggressive behavior, hate speech (racial/religious), and unsportsmanlike actions are prohibited.
- Behavior and Penalties
- 8. Penalty Table (Penalties) Violation Penalty Insulting / using verbal aggression Warning → Loss in that round → Disqualification Cheating in any form Loss in that round / Disqualification from competition Watching streams during gameplay Loss in that match Stopping the game without permission Loss in that round Using bugs Loss in that round or match...
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-03714 — studio_rules_penalties

- Priority: P0 wrong task/target or omitted facet
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Could you please help me with this: What is the studio policy for dood noise damag
- Legacy expected: ['rules']; answer_available
- ก่อนแก้: pipeline:protected_damage_responsibility; confidence=0.98; source IDs=['rule_damage_responsibility']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:protected_damage_responsibility; frozen pass=False

### คำตอบก่อนแก้

If equipment is damaged through improper or negligent use, users are responsible according to severity: minor damage carries a 100-500 THB fine; moderate damage costs the actual repair amount or 500-2,000 THB; severe damage requires full compensation based on the property's market value.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

- Food and drinks are allowed only in designated areas.
- Users should avoid excessive noise and must not insult or mock others.
- If equipment is damaged through improper or negligent use, users are responsible according to severity: minor damage carries a 100-500 THB fine; moderate damage costs the actual repair amount or 500-2,000 THB; severe damage requires full compensation based on the property's market value.
Source: https://esports.computing.psu.ac.th/reservation

### คำตอบหลังแก้

If equipment is damaged through improper or negligent use, users are responsible according to severity: minor damage carries a 100-500 THB fine; moderate damage costs the actual repair amount or 500-2,000 THB; severe damage requires full compensation based on the property's market value.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04611 — members_overview_contact

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: What possition does Mr. Naphat Chuea Lekwanich hold
- Legacy expected: ['members', 'overview']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Official Thai source member record(s):
Names and role titles below are shown exactly as published by PSU.
- ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี - มหาวิทยาลัยสงขลานครินทร์
- รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี - มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- รศ.ดร.อซีส นันทอมรพงศ์: คณบดี - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ - มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- นายพฤทธิ์ เกษตรสมบูรณ์: นักวิชาการคอมพิวเตอร์ - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- นายณัฐวัฒน์ นิธิคุณานนต์: นักวิชาการคอมพิวเตอร์ - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- นายชนะชัย สิริพันธ์วราภรณ์: ผู้จัดการ - PSU Esports Studio - Phuket วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- นายณภัทร เชื้อเหล่าวานิช: นักศึกษาสหกิจ Game and 3D Developer - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- Mr. Amine Abidellaoui: Internship Student - High School Bristol Cannes, France
- นายสุพศิน อะนะฝรั่ง: นักศึกษาสหกิจ Web & AI Developer - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- Mr. Yanis Igoudjil: Internship Student - Industrial Engineering and Information Systems, EPF Graduate School of Engineering, Cachan Val-De-Marne, France
- นายภาสวุฒิ ชูติประชากิจ: นักศึกษาฝึกงานโครงการ Super AI SS6 ตำแหน่ง AI Chat Bot Developer - วิศวกรรมระบบไอโอทีและสารสนเทศ สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง
- นายษุภากรณ์ จิราจินดากุล: ประธาน
- นายนพัทธ์ ฝอยทอง: รองประธาน
- นายปัณณวิชญ์ หนูเรือง: เลขานุการ
- นายภูจิตร จิรวิริยาภรณ์: เหรัญญิก
- นายธนชาติ เอ่งฉ้วน: ประชาสัมพันธ์
- นางสาวกมลวรรณ นวลสาย: กรรมการ
- นางสาวชญาภา จันทร์เอิบ: กรรมการ
- นางสาวณัฐธิดา คำทะเนตร์: กรรมการ
- นางสาวสุภาสินี ธนภพ: กรรมการ
- นางสาวอาทิตยา แดงประดับ: กรรมการ
- นายณัฐพนธ์ อินทรสังขนาวิน: กรรมการ
- นายอภิวิชญ์ เลิศกมลรักษ์: กรรมการ
- นายอรรถนนท์ สุขแก้ว: กรรมการ
Source: https://esports.phuket.psu.ac.th/about-us/Members (official Thai source)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04127 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: What do the RoV tournament rules say about competition quipment and devices
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_rov_blueket_2025_men_s06_c01', 'competition_rules_rov_blueket_2025_men_s01_c01', 'competition_rules_rov_blueket_2025_men_s02_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Arena of Valor (RoV) competition rules:
- 5. Competition attire and equipment 5.1. Personal mobile phones and personal internet and/or university internet. 5.2. Personal power strips and battery-charging equipment. 5.3. Tablets, iPads and any devices other than mobile phones may not be used in competition. If detected, staff will immediately impose disqualification.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-03828 — studio_rules_penalties

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: I am planning a visit and would like to know: What is the tudio policy foe damage responsibility
- Legacy expected: ['penalty']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

If equipment is damaged through improper or negligent use, users are responsible according to severity: minor damage carries a 100-500 THB fine; moderate damage costs the actual repair amount or 500-2,000 THB; severe damage requires full compensation based on the property's market value.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04432 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: For Arena of Valor, can you verify tge rule on team size
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_rov_blueket_2025_men_s06_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Arena of Valor (RoV) competition rules:
- 4. Competition regulations and rules: Competition Rules 4. Regulations and Competition Rules 4.1. Basic Rules 4.1.1. Prohibited to use character names or phrases that are offensive or disrespectful toward others.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-01933 — games_catalog_availability

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: What do you need to ook to play Beat Saber
- Legacy expected: ['games', 'reservation']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.99; source IDs=['game_detail_beat_saber']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_game_detail_en; frozen pass=True

### คำตอบก่อนแก้

Beat Saber: This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Booking steps:
• Select a service.
• Choose a date and time.
• Fill in your user information.
• Review the details.
• Pay by bank transfer.
• Upload the payment slip.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

### คำตอบหลังแก้

Verified English information:
Beat Saber
Genre: VR Rhythm Game
Overview: Beat Saber is a VR rhythm game in which players use light swords to slash blocks in time with the music.
How to play: Put on VR glasses, hold the controller, and smash blocks in the direction indicated. Dodge obstacles and try to score points according to the rhythm of the music.
Available at: VR Zone
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-00039 — service_fee

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Please tell me: How muuch is VR for 30 minutes
- Legacy expected: ['service_fee']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

VR - 30 minutes (1-5 people)
- PSU students and staff: 0 THB
- PSU alumni and students from other institutions: 190 THB
- General adults: 525 THB
- Requested duration: 30 minutes, charged as 1 session(s).
Prices are calculated deterministically from the Service Fee 2026 table.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [
    "30 minutes",
    "THB"
  ],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04154 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Please retriebe the official RoV rulebook evidence for the rulebook scope and tournament identity
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_rov_blueket_2025_men_s01_c01', 'competition_rules_rov_blueket_2025_men_s02_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Arena of Valor (RoV) competition rules:
- Document overview: Competition Rules for Blueket Games 2025 Esports Event Game: Arena of Valor (RoV)
- Male Team Category
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04133 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: What do the RoV tournament rules say about pauses and timeout
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_rov_blueket_2025_men_s06_c02', 'competition_rules_rov_blueket_2025_men_s06_c03', 'competition_rules_rov_blueket_2025_men_s06_c04']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Arena of Valor (RoV) competition rules:
- 4. Competition regulations and rules: 4.3.2. If a competitor disconnects because of force majeure (such as an internet-service outage across the area or a game-server error), the affected team must notify the staff. Whether to allow a replay is at the referees' discretion.
- 4. Competition regulations and rules: 4.5.1.2 In cases where the game is paused due to technical issues, not caused by player actions, the event staff may order a pause and require players to rejoin the game after all disconnected players have reconnected.
- 4. Competition regulations and rules: 4.5.6.1.1 Physical disturbances between competitors, such as causing chaos, noise, and loud sounds that interfere with gameplay. 4.5.6.1.2 Portable devices or software malfunctioning. 4.5.6.1.3 Frame drops or increased ping outside of player control. 4.5.6.1.4 When the opposing team engages in severe cheating or disrespect.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-01199 — live_booking

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Doed PC #03 hae TEKKEN 8 Thanks
- Legacy expected: ['games', 'reservation', 'schedule']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.99; source IDs=['game_detail_tekken_8']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_game_detail_en; frozen pass=True

### คำตอบก่อนแก้

TEKKEN 8: This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

TEKKEN 8 is not listed for PC #03 (PC #03-#10) in the verified game catalog. Catalog last verified: 2026-07-30. This is catalog availability, not a live installation check.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified English information:
TEKKEN 8
Genre: Fighting game 1v1
Overview: TEKKEN 8 is a one-on-one fighting game where players select characters and win by using combos, blocking, and counterattacks against their opponent.
How to play: Play in rounds. Choose a character. Practice basic moves/combo sequences. Read your opponent's timing and reduce their health to zero before them.
Available at: PC Zone, PlayStation 5 Zone
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04585 — members_overview_contact

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: I am planning a visit and need to know: Who manages the studuo
- Legacy expected: ['members', 'overview']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

The studio was established by Prince of Songkla University and is operated by the College of Computing.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-03799 — studio_rules_penalties

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Please answer from verified studio information: What are the sstudio rules? Please use verified information
- Legacy expected: ['rules']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Key studio rules:
• Leave belongings before using the service; the studio is not responsible for lost property.
• Food and drinks are allowed only in designated areas.
• Return equipment and game discs after use.
• Avoid excessive noise and insulting or sarcastic language.
• Do not move equipment or other items without permission, and do not use personal power plugs without permission.
• Smoking, drugs, alcohol, weapons, fighting, and gambling are prohibited.
• Damage to equipment may result in a repair fee or compensation based on the extent of damage.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [
    "Key studio rules"
  ],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04027 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: I am prpearing for a Counter Strike 2 match. What is the policy for competition equipment and devices
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s39_c01', 'competition_rules_cs2_psu_phuket_2026_s40_c01', 'competition_rules_cs2_psu_phuket_2026_s41_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Equipment and Game Settings
- Permitted Equipment
- Players may bring their own keyboard (wired or wireless), mouse (wired or wireless), mouse cord holder (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04988 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: What is a mechanical keyboard liek
- Legacy expected: ['general', 'knowledge']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

I could not find verified PSU Esports Studio - Phuket information for this question.

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04296 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: Please retrieve the official CS2 rulebook eviddence for eligibility, roster, and registration
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s12_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Registration of players is not permitted after the registration period has closed.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04627 — members_overview_contact

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: Who is the captainn
- Legacy expected: ['members', 'overview']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

I could not find a verified PSU Esports Studio - Phuket member record for that requested role.

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04347 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Coud you please help me with this: What do the CS2 tournament rules say about the penaltu matrix
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s02_c01', 'competition_rules_cs2_psu_phuket_2026_s01_c01', 'competition_rules_cs2_psu_phuket_2026_s03_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Scope of Application This regulation applies to all players, teams, and staff members participating officially in any CS2 competition organized by PSU Esports Studio - Phuket.
- PSU Phuket CS2 2026 Tournament
- Document overview: Competition Rules and Format for Counter-Strike 2
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-00407 — reservation_policy

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: What is the studio policy for canceellation advance
- Legacy expected: ['reservation']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Cancellations must be made at least 1 hour in advance.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04420 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me ith this: For Arena of Valor, csn you verify the rule on registration
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_rov_blueket_2025_men_s03_c01', 'competition_rules_rov_blueket_2025_men_s08_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Arena of Valor (RoV) competition rules:
- 1. Competition schedule 1.1. Offline competition on 11 September 2025 (B.E. 2568).
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-03401 — equipment

- Priority: P2 source/ambiguity/label review
- Evidence: trace_code_source_inspected
- คำถาม: Could you check this using verifide information: What controller is used for PS5
- Legacy expected: ['equipment', 'game_controls']; answer_available
- ก่อนแก้: pipeline:equipment_spec_unverified_en; confidence=0.98; source IDs=['equipment_playstation_5_slim']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: PS5 controller model absent in selected equipment source. Safe unverified result conflicts with answer_available candidate label; do not infer DualSense from generic product knowledge.
- หลังแก้: pipeline:equipment_spec_unverified_en; frozen pass=False

### คำตอบก่อนแก้

The published equipment record does not specify the PS5 controller model.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

The published equipment record does not specify the PS5 controller model.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### คำตอบหลังแก้

The published equipment record does not specify the PS5 controller model.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-01715 — games_catalog_availability

- Priority: P0 wrong task/target or omitted facet
- Evidence: trace_code_source_inspected
- คำถาม: Wherw can you pay VALORANT
- Legacy expected: ['games']; answer_available
- ก่อนแก้: pipeline:structured_service_fee_en; confidence=0.9; source IDs=['service_fee_image_2026', 'pc_service_fee_local_update_20260727']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: play->pay becomes another valid word; price handler returns service fee. User meaning ambiguous; source-grounded price cannot certify intended game location.
- หลังแก้: pipeline:structured_service_fee_en; frozen pass=False

### คำตอบก่อนแก้

PC - 1 hour (1 people)
- PSU students and staff: 0 THB
- PSU alumni and students from other institutions: 25 THB
- General adults: 70 THB
Prices are calculated deterministically from the Service Fee 2026 table.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

VALORANT is available on: PC #01-#02, PC #03-#10. Studio zone(s): PC Zone.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

PC - 1 hour (1 people)
- PSU students and staff: 0 THB
- PSU alumni and students from other institutions: 25 THB
- General adults: 70 THB
Prices are calculated deterministically from the Service Fee 2026 table.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-02394 — game_detail

- Priority: P0 wrong task/target or omitted facet
- Evidence: trace_code_source_inspected
- คำถาม: How to pay Ring Fit Adventure
- Legacy expected: ['games']; localization_pending
- ก่อนแก้: pipeline:structured_service_fee_en; confidence=0.9; source IDs=['service_fee_image_2026']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: play->pay real-word collision similarly returns Nintendo fee instead of game how-to; label requires review and scoped ambiguity guard.
- หลังแก้: pipeline:structured_service_fee_en; frozen pass=False

### คำตอบก่อนแก้

The question does not specify the number of players, so both verified packages are shown.
Nintendo Switch - 1 hour (1-2 people)
- PSU students and staff: 0 THB
- PSU alumni and students from other institutions: 50 THB
- General adults: 140 THB
Nintendo Switch - 1 hour (3-4 people)
- PSU students and staff: 0 THB
- PSU alumni and students from other institutions: 100 THB
- General adults: 280 THB
Prices are calculated deterministically from the Service Fee 2026 table.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Ring Fit Adventure: This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### คำตอบหลังแก้

The question does not specify the number of players, so both verified packages are shown.
Nintendo Switch - 1 hour (1-2 people)
- PSU students and staff: 0 THB
- PSU alumni and students from other institutions: 50 THB
- General adults: 140 THB
Nintendo Switch - 1 hour (3-4 people)
- PSU students and staff: 0 THB
- PSU alumni and students from other institutions: 100 THB
- General adults: 280 THB
Prices are calculated deterministically from the Service Fee 2026 table.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04047 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: How is maps, vetoes, and map delection handled in the Counter-Strike 2 tournament rules
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s28_c01', 'competition_rules_cs2_psu_phuket_2026_s31_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Competition maps
- Map selection uses MAPBAN.GG
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-00110 — service_fee

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: How muc does it xost for a PSU student to play VR for 1 hour
- Legacy expected: ['service_fee']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

VR - 1 hour (1-5 people)
- PSU students and staff: 0 THB
- Requested duration: 60 minutes, charged as 1 session(s).
Prices are calculated deterministically from the Service Fee 2026 table.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04982 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: How do frame rtae and resolution differ
- Legacy expected: ['general', 'knowledge']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Which service would you like the fee for: PC, PlayStation 5, Nintendo Switch, Cockpit, or VR? The rate depends on the service and user group.

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04303 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: How is comppetition equipment and devices handled in the Counter-Strike 2 tournament rules
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s39_c01', 'competition_rules_cs2_psu_phuket_2026_s40_c01', 'competition_rules_cs2_psu_phuket_2026_s41_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Equipment and Game Settings
- Permitted Equipment
- Players may bring their own keyboard (wired or wireless), mouse (wired or wireless), mouse cord holder (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04820 — compound_context_boundary

- Priority: P0 wrong task/target or omitted facet
- Evidence: trace_code_source_inspected
- คำถาม: Do you offer vernight accommodation? Please use verified information
- Legacy expected: ['no_answer']; safe_no_answer
- ก่อนแก้: pipeline:structured_equipment_catalog_en; confidence=0.97; source IDs=['equipment_gaming_pc', 'equipment_gaming_monitor', 'equipment_gaming_keyboard', 'equipment_gaming_mouse', 'equipment_gaming_headset', 'equipment_gaming_chair', 'equipment_logitech_g923', 'equipment_driving_force_shifter', 'equipment_racezone_cockpit_v3', 'equipment_pulse_elite_headset', 'equipment_nintendo_switch_oled', 'equipment_playstation_5_slim', 'equipment_sony_playstation_vr2', 'equipment_tv_65', 'equipment_tv_86', 'equipment_sofa_2_seats']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Wrong accommodation noun cue bypasses exact rule; offer alone triggers inventory, bilingual early return0.97 before central selection; source facts unrelated to requested service.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

Verified equipment:
- Gaming PC model MSI MAG Infinite S3 14th (PC Zone) - 10 Units
- Gaming Monitor (PC Zone) - 10 Units
- Gaming Keyboard (PC Zone)
- Gaming Mouse (PC Zone)
- Gaming Headset (PC Zone)
- Gaming Chair (PC Zone) - 10 Units
- Logitech G923 TRUEFORCE Racing Wheel (Cockpit Zone) - 2 Units with Driving Force Shifter
- Driving Force Shifter (Cockpit Zone) - 2 Units with Logitech G923
- Racezone Full Cockpit V3 (Cockpit Zone) - 2 Units
- Pulse Elite Wireless Headset (Cockpit Zone) - 2 Units
- Nintendo Switch OLED (Nintendo Switch Zone) - 1 Unit
- PlayStation 5 Slim With Ultra HD Blu-Ray Disc Drive (PlayStation 5 Zone / VR Zone) - 2 Units in PlayStation 5 Zone and 1 Unit in VR Zone
- Sony PlayStation VR2 (VR Zone) - 1 Unit
- TV 65 inch (Cockpit Zone) - 2 Units
- TV 86 inch (Nintendo Switch Zone) - 1 Unit
- Sofa 2 seats (Nintendo Switch Zone) - 2 Sets
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

No information about sleeping rooms or overnight stays was found in the available knowledge base. The available schedule describes time-slot usage between 09:00-16:00 with maintenance periods, so overnight service should not be assumed.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [
    "No information"
  ],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04155 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: How is the rulebook scop anf tournament identity handled in the Arena of Valor tournament rules
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_rov_blueket_2025_men_s01_c01', 'competition_rules_rov_blueket_2025_men_s02_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Arena of Valor (RoV) competition rules:
- Document overview: Competition Rules for Blueket Games 2025 Esports Event Game: Arena of Valor (RoV)
- Male Team Category
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04468 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: For Tekken 8, can you verify the ryle on dispute resolution
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_tekken8_psu_esports_s08_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Tekken 8 competition rules:
- Dispute Resolution * Any issues must be reported to the competition organizer immediately. * In cases of disputes or protests, the decision of the supervisors or referees shall be final. Note: The competition organizer reserves the right to amend or modify these regulations without prior notice.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-03567 — equipment

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: Could you please help me with this: I am plannign a visit and need to know: What controller is used for PS5
- Legacy expected: ['equipment', 'game_controls']; answer_available
- ก่อนแก้: pipeline:equipment_spec_unverified_en; confidence=0.98; source IDs=['equipment_playstation_5_slim']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:equipment_spec_unverified_en; frozen pass=False

### คำตอบก่อนแก้

The published equipment record does not specify the PS5 controller model.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

The published equipment record does not specify the PS5 controller model.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### คำตอบหลังแก้

The published equipment record does not specify the PS5 controller model.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04429 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: How is the rulebpok scope and tournament identity handled in the Arena of Valor tournament rules
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_rov_blueket_2025_men_s01_c01', 'competition_rules_rov_blueket_2025_men_s02_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Arena of Valor (RoV) competition rules:
- Document overview: Competition Rules for Blueket Games 2025 Esports Event Game: Arena of Valor (RoV)
- Male Team Category
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04874 — compound_context_boundary

- Priority: P0 wrong task/target or omitted facet
- Evidence: trace_code_source_inspected
- คำถาม: How many memberss are there, and who is the president
- Legacy expected: ['multi_question']; answer_available
- ก่อนแก้: pipeline:structured_members_source_th; confidence=0.98; source IDs=['Members']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Exact members? regex fails memberss; no split; president always maps อธิการบดี. Missing numeric count handler/contract even on clean; ambiguous institutional versus club scope.
- หลังแก้: pipeline:multi_question_splitter; frozen pass=True

### คำตอบก่อนแก้

Official Thai source member record(s):
Names and role titles below are shown exactly as published by PSU.
- ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี - มหาวิทยาลัยสงขลานครินทร์
Source: https://esports.phuket.psu.ac.th/about-us/Members (official Thai source)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This question contains several topics. Here are the answers separately:

Question 1: How many members are there?
Official Thai source member record(s):
Names and role titles below are shown exactly as published by PSU.
- ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี - มหาวิทยาลัยสงขลานครินทร์
- รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี - มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- รศ.ดร.อซีส นันทอมรพงศ์: คณบดี - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ - มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- นายพฤทธิ์ เกษตรสมบูรณ์: นักวิชาการคอมพิวเตอร์ - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- นายณัฐวัฒน์ นิธิคุณานนต์: นักวิชาการคอมพิวเตอร์ - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- นายชนะชัย สิริพันธ์วราภรณ์: ผู้จัดการ - PSU Esports Studio - Phuket วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- นายณภัทร เชื้อเหล่าวานิช: นักศึกษาสหกิจ Game and 3D Developer - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- Mr. Amine Abidellaoui: Internship Student - High School Bristol Cannes, France
- นายสุพศิน อะนะฝรั่ง: นักศึกษาสหกิจ Web & AI Developer - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- Mr. Yanis Igoudjil: Internship Student - Industrial Engineering and Information Systems, EPF Graduate School of Engineering, Cachan Val-De-Marne, France
- นายภาสวุฒิ ชูติประชากิจ: นักศึกษาฝึกงานโครงการ Super AI SS6 ตำแหน่ง AI Chat Bot Developer - วิศวกรรมระบบไอโอทีและสารสนเทศ สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง
- นายษุภากรณ์ จิราจินดากุล: ประธาน
- นายนพัทธ์ ฝอยทอง: รองประธาน
- นายปัณณวิชญ์ หนูเรือง: เลขานุการ
- นายภูจิตร จิรวิริยาภรณ์: เหรัญญิก
- นายธนชาติ เอ่งฉ้วน: ประชาสัมพันธ์
- นางสาวกมลวรรณ นวลสาย: กรรมการ
- นางสาวชญาภา จันทร์เอิบ: กรรมการ
- นางสาวณัฐธิดา คำทะเนตร์: กรรมการ
- นางสาวสุภาสินี ธนภพ: กรรมการ
- นางสาวอาทิตยา แดงประดับ: กรรมการ
- นายณัฐพนธ์ อินทรสังขนาวิน: กรรมการ
- นายอภิวิชญ์ เลิศกมลรักษ์: กรรมการ
- นายอรรถนนท์ สุขแก้ว: กรรมการ
Source: https://esports.phuket.psu.ac.th/about-us/Members (official Thai source)

Question 2: who is the president?
Official Thai source member record(s):
Names and role titles below are shown exactly as published by PSU.
- ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี - มหาวิทยาลัยสงขลานครินทร์
Source: https://esports.phuket.psu.ac.th/about-us/Members (official Thai source)

### คำตอบหลังแก้

This question contains several topics. Here are the answers separately:

Question 1: How many members are there?
The stored source directory contains 25 member records:
- Members: 7
- cooperative education and Internship student: 5
- PSU Phuket Esports Club - PSU Phuket: 13
These are counts in the recorded directory, not a live headcount.
Source: https://esports.phuket.psu.ac.th/about-us/Members (original source in Thai)

Question 2: who is the president?
Do you mean the university president or the esports club chairperson?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04070 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Please retrieve the official CS2 rukebook evidence for penalties
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s54_c01', 'competition_rules_cs2_psu_phuket_2026_s13_c01', 'competition_rules_cs2_psu_phuket_2026_s15_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- 8. Penalty Table (Penalties) Violation Penalty Insulting / using verbal aggression Warning → Loss in that round → Disqualification Cheating in any form Loss in that round / Disqualification from competition Watching streams during gameplay Loss in that match Stopping the game without permission Loss in that round Using bugs Loss in that round or match...
- Behavior and Penalties
- If any member withdraws, the team may be disqualified.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-00725 — reservation_policy

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: I am planning a visit and would like to know: What is the studio policy for transfre booking
- Legacy expected: ['reservation']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for reservation.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Payment is made by bank transfer via Siam Commercial Bank, account name PSU Esports Studio - Phuket, account number 795-276244-1, with the payment slip uploaded.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for reservation.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04362 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: Please retrieve he official CS2 rulebook evidence for dispyte resolution
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s39_c01', 'competition_rules_cs2_psu_phuket_2026_s40_c01', 'competition_rules_cs2_psu_phuket_2026_s41_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Players may customize brightness, resolution, and crosshair settings only within the game and computer monitor.
- Scope of Application This regulation applies to all players, teams, and staff members participating officially in any CS2 competition organized by PSU Esports Studio - Phuket.
- Equipment and Game Settings
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04279 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: How is the competition format handled in the Counter-Strike 2 tourament rules
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s19_c01', 'competition_rules_cs2_psu_phuket_2026_s20_c01', 'competition_rules_cs2_psu_phuket_2026_s21_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Competition Format
- Tournament format: Single Elimination
- Semifinals and finals: Best of 3 (BO3)
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-01887 — games_catalog_availability

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: On which amchine can you play New Super Mario Bros. U Deluxe
- Legacy expected: ['games']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.99; source IDs=['game_detail_new_super_mario_bros']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_game_detail_en; frozen pass=True

### คำตอบก่อนแก้

New Super Mario Bros. U Deluxe: This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

New Super Mario Bros. U Deluxe is available on: Nintendo Switch (1-2 Persons), Nintendo Switch (1-4 Persons). Studio zone(s): Nintendo Switch Zone.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified English information:
New Super Mario Bros. U Deluxe
Genre: Genre: Platformer 2D
Overview: New Super Mario Bros. U Deluxe is a Mario-style platformer game featuring jumping, enemy evasion, and coin collection.
How to play: Run, jump, use power-ups to progress through levels and play with multiple teammates
Available at: Nintendo Switch Zone
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04702 — members_overview_contact

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Could you please help me wit this: Where is the stidio
- Legacy expected: ['contact']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

PSU Esports Studio - Phuket is located at Prince of Songkla University, Phuket Campus, 80 Moo 1 Vichitsongkram Road, Kathu, Phuket 83120.
Source: https://esports.phuket.psu.ac.th/Contact-Us (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [
    "Phuket Campus"
  ],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04340 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could yoi please help me with this: Could you cite the Counter Strike 2 rule concerning pauses and timeouts
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s33_c01', 'competition_rules_cs2_psu_phuket_2026_s34_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.
- Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-01935 — games_catalog_availability

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Were is Horizon Call of the Mountain locates
- Legacy expected: ['games']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.99; source IDs=['game_detail_horizon_call_of_the_mountain']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_game_detail_en; frozen pass=True

### คำตอบก่อนแก้

Horizon Call of the Mountain: This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Horizon Call of the Mountain is available on: VR Station 30 minutes, VR Station 1 hour. Studio zone(s): VR Zone.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified English information:
Horizon Call of the Mountain
Genre: VR Action-Adventure
Overview: Horizon Call of the Mountain is a VR adventure game set in the Horizon world, emphasizing climbing, exploration, and combat with machinery.
How to play: Put on VR glasses, use the controller to climb, move around, aim your bow, and complete scene-specific quests
Available at: VR Zone
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-03969 — studio_rules_penalties

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: What are the studio ryles? Please answer briefly Please keep the answer concise
- Legacy expected: ['rules']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Key studio rules:
• Leave belongings before using the service; the studio is not responsible for lost property.
• Food and drinks are allowed only in designated areas.
• Return equipment and game discs after use.
• Avoid excessive noise and insulting or sarcastic language.
• Do not move equipment or other items without permission, and do not use personal power plugs without permission.
• Smoking, drugs, alcohol, weapons, fighting, and gambling are prohibited.
• Damage to equipment may result in a repair fee or compensation based on the extent of damage.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [
    "Key studio rules"
  ],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04079 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: What do the CS2 tournament rules say about pre-match and on-site requuirements
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s51_c01', 'competition_rules_cs2_psu_phuket_2026_s52_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Mobile phones, tablets, or smartwatches are prohibited in the competition area until the match concludes.
- Players are not allowed to bring notes or documents into the arena, but team leaders may bring them in and must hand them to the referees before every match.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04200 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: For Tekken 8, can you verify the rule on the rulebook sope and tournament identity
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_tekken8_psu_esports_s01_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:competition_source_localization_pending_en; frozen pass=False

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Tekken 8 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live.
Original source in Thai: local://competition_rules/competition_rules_tekken8_psu_esports

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04447 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: How is player conduct and sportsmanship handled in the Tekken 8 tournament ruels
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_tekken8_psu_esports_s05_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Tekken 8 competition rules:
- Competition etiquette * Unsportsmanlike behavior, such as mocking, taunting, or rude words or actions towards others, is prohibited. Violations result in an immediate forfeit without exception. * Competitors must respect referees and other competitors. Insulting or disrespectful behavior is prohibited in all cases.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-03674 — studio_rules_penalties

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: What are the stduio rules? Please answer briefly
- Legacy expected: ['rules']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Key studio rules:
• Leave belongings before using the service; the studio is not responsible for lost property.
• Food and drinks are allowed only in designated areas.
• Return equipment and game discs after use.
• Avoid excessive noise and insulting or sarcastic language.
• Do not move equipment or other items without permission, and do not use personal power plugs without permission.
• Smoking, drugs, alcohol, weapons, fighting, and gambling are prohibited.
• Damage to equipment may result in a repair fee or compensation based on the extent of damage.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [
    "Key studio rules"
  ],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04888 — compound_context_boundary

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Which drvice is bes
- Legacy expected: ['clarification', 'equipment', 'games', 'no_answer', 'reservation', 'service_fee']; clarification_required
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Please tell me the zone, game type, or specific request you are interested in so I can answer from the verified catalog.

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04573 — members_overview_contact

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Who sre you
- Legacy expected: ['general', 'knowledge', 'overview']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

I am PSU Esports Assistant, the chatbot for PSU Esports Studio - Phuket. I can help with verified information about games, equipment, booking, opening hours, service fees, rules, competitions, and studio contacts.

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-03603 — equipment

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Could you please help me with this: Where is he gaming chaur located
- Legacy expected: ['equipment', 'games']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Verified equipment record: Gaming Chair is listed in PC Zone.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-01338 — schedule_calendar

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Is it opn on Sundays
- Legacy expected: ['reservation', 'schedule']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Regular service hours are Monday-Friday. Monday morning and Friday afternoon are maintenance periods. Please specify a day for the exact play window.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04884 — compound_context_boundary

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: What does PS5 hsve
- Legacy expected: ['clarification', 'equipment', 'games', 'no_answer', 'reservation', 'service_fee']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

There are currently 17 verified games in PlayStation 5 Zone.

PlayStation 5 Zone (17 games)
•    Call of Duty: Modern Warfare III
•    Delta Force
•    EA Sports FC 24
•    eFootball
•    FINAL FANTASY XVI
•    Fortnite
•    God of War Ragnarok
•    Hogwarts Legacy
•    Marvel's Spider-Man 2
•    NARUTO X BORUTO Ultimate Ninja Storm Connections
•    Resident Evil 4
•    Resident Evil Village
•    TEKKEN 8
•    THE FINALS
•    The Last of Us Part I
•    The Last of Us Part II (Remastered)
•    Uncharted: Legacy of Thieves Collection
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-02171 — games_catalog_availability

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could yo please help me with this: Is Resident Evil Village availanle
- Legacy expected: ['games']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.99; source IDs=['game_detail_resident_evil_village']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_game_detail_en; frozen pass=True

### คำตอบก่อนแก้

Resident Evil Village: This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Resident Evil Village is available on: PlayStation 5 #01-#02, VR Station 30 minutes, VR Station 1 hour. Studio zone(s): PlayStation 5 Zone, VR Zone.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified English information:
Resident Evil Village
Genre: Survival Horror
Overview: Resident Evil Village is a survival horror game emphasizing atmosphere, exploration, and combat against diverse enemies.
How to play: Explore scenes, collect items, manage resources, fight and solve puzzles to progress the story
Available at: PlayStation 5 Zone
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-01849 — games_catalog_availability

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: What do you need to bok to play Uncharted
- Legacy expected: ['games', 'reservation']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.99; source IDs=['game_detail_uncharted']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_game_detail_en; frozen pass=True

### คำตอบก่อนแก้

Uncharted: Legacy of Thieves Collection: This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Booking steps:
• Select a service.
• Choose a date and time.
• Fill in your user information.
• Review the details.
• Pay by bank transfer.
• Upload the payment slip.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

### คำตอบหลังแก้

Verified English information:
Uncharted: Legacy of Thieves Collection
Genre: Action-Adventure
Overview: Uncharted is a treasure-hunting adventure game focused on climbing, exploration, puzzle solving and action scenes.
How to play: Explore locations, climb, solve puzzles, fight with firearms and progress through missions.
Available at: PlayStation 5 Zone
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04006 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you cite the Counter Strike 2 rule concerning the competition formta
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s01_c01', 'competition_rules_cs2_psu_phuket_2026_s02_c01', 'competition_rules_cs2_psu_phuket_2026_s03_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Document overview: Competition Rules and Format for Counter-Strike 2
- PSU Phuket CS2 2026 Tournament
- 1. General Information
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-03667 — studio_rules_penalties

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: What are the studio ules
- Legacy expected: ['rules']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Key studio rules:
• Leave belongings before using the service; the studio is not responsible for lost property.
• Food and drinks are allowed only in designated areas.
• Return equipment and game discs after use.
• Avoid excessive noise and insulting or sarcastic language.
• Do not move equipment or other items without permission, and do not use personal power plugs without permission.
• Smoking, drugs, alcohol, weapons, fighting, and gambling are prohibited.
• Damage to equipment may result in a repair fee or compensation based on the extent of damage.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [
    "Key studio rules"
  ],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04005 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: How is the competition format handdled in the Counter-Strike 2 tournament rules
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s19_c01', 'competition_rules_cs2_psu_phuket_2026_s20_c01', 'competition_rules_cs2_psu_phuket_2026_s21_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Competition Format
- Tournament format: Single Elimination
- Semifinals and finals: Best of 3 (BO3)
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04320 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: Please retrieve the official CS2 rulebook evidence for maps, vetose, and map selection
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s28_c01', 'competition_rules_cs2_psu_phuket_2026_s31_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Competition maps
- Map selection uses MAPBAN.GG
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-01405 — schedule_calendar

- Priority: P0 wrong task/target or omitted facet
- Evidence: trace_code_source_inspected
- คำถาม: Could you please help me with this: What time is the afteronon session? Could you check this for me
- Legacy expected: ['reservation', 'schedule']; answer_available
- ก่อนแก้: pipeline:structured_schedule_en; confidence=0.98; source IDs=['service_schedule']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: afteronon loses time_slots/afternoon qualifier; schedule family recognized but generic weekly hours instead of13:00-16:00. Same confidence0.98 in both branches.
- หลังแก้: pipeline:structured_schedule_en; frozen pass=True

### คำตอบก่อนแก้

Regular service hours are Monday-Friday. Monday morning and Friday afternoon are maintenance periods. Please specify a day for the exact play window.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

The afternoon service period is 13:00-16:00. Friday afternoon is reserved for maintenance.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

The afternoon service period is 13:00-16:00. Friday afternoon is reserved for maintenance.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [
    "13:00-16:00"
  ],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-00065 — service_fee

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Whih is more expensivw, PC or VR
- Legacy expected: ['service_fee']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

The question does not specify the duration, so both verified packages are shown.
VR - 30 minutes (1-5 people)
- PSU students and staff: 0 THB
- PSU alumni and students from other institutions: 190 THB
- General adults: 525 THB
VR - 1 hour (1-5 people)
- PSU students and staff: 0 THB
- PSU alumni and students from other institutions: 375 THB
- General adults: 1,050 THB
Prices are calculated deterministically from the Service Fee 2026 table.
Source: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04651 — members_overview_contact

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: Who is te referee pisition
- Legacy expected: ['overview']; answer_available
- ก่อนแก้: pipeline:member_role_not_found_en; confidence=0.96; source IDs=['Members']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:member_role_not_found_en; frozen pass=False

### คำตอบก่อนแก้

I could not find a verified PSU Esports Studio - Phuket member record for that requested role.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

I could not find a verified PSU Esports Studio - Phuket member record for that requested role.

### คำตอบหลังแก้

I could not find a verified PSU Esports Studio - Phuket member record for that requested role.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-01343 — schedule_calendar

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: What is the operating scheudle
- Legacy expected: ['reservation', 'schedule']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Regular service hours are Monday-Friday. Monday morning and Friday afternoon are maintenance periods. Please specify a day for the exact play window.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04475 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: I am preparing for a T8 match. What is the oolicy for the rulebook scope and tournament identity
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_tekken8_psu_esports_s01_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:missing_english_localization; frozen pass=False

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-00141 — service_fee

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: Residentt Evil 4 price
- Legacy expected: ['service_fee']; answer_available
- ก่อนแก้: pipeline:english_clarification; confidence=0.96; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:english_clarification; frozen pass=False

### คำตอบก่อนแก้

Which service, duration, and user group should I price: PC, PlayStation 5, Nintendo Switch, Cockpit, or VR?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Which service, duration, and user group should I price: PC, PlayStation 5, Nintendo Switch, Cockpit, or VR?

### คำตอบหลังแก้

Which service, duration, and user group should I price: PC, PlayStation 5, Nintendo Switch, Cockpit, or VR?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04245 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: How is penalties handled in the Valorant touenament rules
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_valorant_psu_phuket_2026_s25_c01', 'competition_rules_valorant_psu_phuket_2026_s10_c01', 'competition_rules_valorant_psu_phuket_2026_s13_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified VALORANT competition rules:
- In-Game Penalty Types * Warning - For first offenses with low impact. * Round Rollback - When an exploit clearly affects a round but intent cannot be determined. * Round Loss - When a player or team is found to have intentionally used an exploit for advantage. * Map Forfeit - For severe offenses or repeated violations that affect the map result.
- Penalty types in the game
- Adjustment for Round Loss when it is found that a player or team intentionally exploits a vulnerability to gain an advantage
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04162 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Coud you cite the AOV rule concerning team size
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_rov_blueket_2025_men_s06_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Arena of Valor (RoV) competition rules:
- 4. Competition regulations and rules: Competition Rules 4. Regulations and Competition Rules 4.1. Basic Rules 4.1.1. Prohibited to use character names or phrases that are offensive or disrespectful toward others.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-00406 — reservation_policy

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: What is the studio policy for how reservstion
- Legacy expected: ['reservation']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Booking steps:
• Select a service.
• Choose a date and time.
• Fill in your user information.
• Review the details.
• Pay by bank transfer.
• Upload the payment slip.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-00062 — service_fee

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: How mich does TEKKEN 8 cos
- Legacy expected: ['games', 'service_fee']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.99; source IDs=['game_detail_tekken_8']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_game_detail_en; frozen pass=True

### คำตอบก่อนแก้

TEKKEN 8: This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

TEKKEN 8 is available on more than one service (PC, PlayStation 5). Which service and duration should I price?
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified English information:
TEKKEN 8
Genre: Fighting game 1v1
Overview: TEKKEN 8 is a one-on-one fighting game where players select characters and win by using combos, blocking, and counterattacks against their opponent.
How to play: Play in rounds. Choose a character. Practice basic moves/combo sequences. Read your opponent's timing and reduce their health to zero before them.
Available at: PC Zone, PlayStation 5 Zone
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04090 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you cite the Counter Strike 2 rul concerning dispute resolution
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s06_c01', 'competition_rules_cs2_psu_phuket_2026_s58_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Language: The official language of the competition is Thai. All communication, protests, and reporting must be conducted in Thai, unless otherwise specified.
- Protests must be submitted within 15 minutes after the match ends, by the team captain or coach only.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04837 — compound_context_boundary

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Could you check this using verified information: What are the competiion rules
- Legacy expected: ['clarification', 'competition_rules', 'general']; clarification_required
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:competition_target_clarification_en; frozen pass=True

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Which game's competition rules would you like to check: Counter-Strike 2, RoV, Tekken 8, or VALORANT?

### คำตอบหลังแก้

Which game's competition rules would you like to check: Counter-Strike 2, RoV, Tekken 8, or VALORANT?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04913 — compound_context_boundary

- Priority: P0 wrong task/target or omitted facet
- Evidence: paired_regression_primary_cause_pending
- คำถาม: How to book VR and what days are availablee
- Legacy expected: ['multi_question']; answer_available
- ก่อนแก้: pipeline:protected_booking_window; confidence=0.98; source IDs=['service_schedule']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:protected_booking_window; frozen pass=False

### คำตอบก่อนแก้

Regular booking/service periods (not live station availability):
- Monday: open 13:00-16:00; maintenance 09:00-12:00
- Tuesday-Thursday: open 09:00-12:00, 13:00-16:00
- Friday: open 09:00-12:00; maintenance 13:00-16:00
- Weekend (Saturday-Sunday): no regular service or booking period is listed.
Special closures override this weekly schedule. A bookable period does not confirm that a station is free.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This question contains several topics. Here are the answers separately:

Question 1: How to book VR
Booking steps:
• Select a service.
• Choose a date and time.
• Fill in your user information.
• Review the details.
• Pay by bank transfer.
• Upload the payment slip.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

Question 2: what days are available
Regular service hours are Monday-Friday. Monday morning and Friday afternoon are maintenance periods. Please specify a day for the exact play window.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Regular booking/service periods (not live station availability):
- Monday: open 13:00-16:00; maintenance 09:00-12:00
- Tuesday-Thursday: open 09:00-12:00, 13:00-16:00
- Friday: open 09:00-12:00; maintenance 13:00-16:00
- Weekend (Saturday-Sunday): no regular service or booking period is listed.
Special closures override this weekly schedule. A bookable period does not confirm that a station is free.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04812 — compound_context_boundary

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Wheere can I play it? Please answer briefly
- Legacy expected: ['clarification', 'games', 'no_answer']; safe_clarification
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Which game do you mean? Please provide the game title so I can check its verified studio zone.

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04389 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me wit this: What do the RoV tournament rules say about the competition format
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_rov_blueket_2025_men_s06_c01', 'competition_rules_rov_blueket_2025_men_s03_c01', 'competition_rules_rov_blueket_2025_men_s05_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Arena of Valor (RoV) competition rules:
- 4. Competition regulations and rules: Competition Rules 4. Regulations and Competition Rules 4.1. Basic Rules 4.1.1. Prohibited to use character names or phrases that are offensive or disrespectful toward others.
- 1. Competition schedule 1.1. Offline competition on 11 September 2025 (B.E. 2568).
- Competition Format 3.1. Offline Mode 3.2. Each round played as Best of 3 (BO3)
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-03459 — equipment

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: What caan a 65-inch TV be used for
- Legacy expected: ['equipment']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.99; source IDs=['equipment_tv_65']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_equipment_item_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### คำตอบหลังแก้

Verified equipment record: TV 65-inch is listed in Cockpit Zone.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04478 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: Could you cite the T8 rule concerning the rulebok scope and tournament identiyy
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:missing_english_localization; frozen pass=False

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-00145 — service_fee

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: Whaat is the price of Uncharted: Legacy of Thieves Collection
- Legacy expected: ['service_fee']; answer_available
- ก่อนแก้: pipeline:english_clarification; confidence=0.96; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:english_clarification; frozen pass=False

### คำตอบก่อนแก้

Which service, duration, and user group should I price: PC, PlayStation 5, Nintendo Switch, Cockpit, or VR?

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Which service, duration, and user group should I price: PC, PlayStation 5, Nintendo Switch, Cockpit, or VR?

### คำตอบหลังแก้

Which service, duration, and user group should I price: PC, PlayStation 5, Nintendo Switch, Cockpit, or VR?

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04403 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: I am preoaring for a AOV match. What is the policy for competition equipment and devices
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_rov_blueket_2025_men_s07_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Arena of Valor (RoV) competition rules:
- 5. Competition attire and equipment 5.1. Personal mobile phones and personal internet and/or university internet. 5.2. Personal power strips and battery-charging equipment. 5.3. Tablets, iPads and any devices other than mobile phones may not be used in competition. If detected, staff will immediately impose disqualification.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04394 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: Could you ciite the AOV rule concerning the competition format
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_rov_blueket_2025_men_s03_c01', 'competition_rules_rov_blueket_2025_men_s05_c01', 'competition_rules_rov_blueket_2025_men_s06_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Arena of Valor (RoV) competition rules:
- 1. Competition schedule 1.1. Offline competition on 11 September 2025 (B.E. 2568).
- Competition Format 3.1. Offline Mode 3.2. Each round played as Best of 3 (BO3)
- 4. Competition regulations and rules: Competition Rules 4. Regulations and Competition Rules 4.1. Basic Rules 4.1.1. Prohibited to use character names or phrases that are offensive or disrespectful toward others.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-03589 — equipment

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you plase help me with this: What is the MSI MAG Infinite S3 14th generation gaming PC used for
- Legacy expected: ['equipment']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.99; source IDs=['equipment_gaming_pc']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_equipment_item_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### คำตอบหลังแก้

Verified equipment record: Gaming PC model MSI MAG Infinite S3 14th is listed in PC Zone.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04476 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: Please retrieve the pfficial TEKKEN 8 rulebok evidence for the rulebook scope and tournament identity
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_tekken8_psu_esports_s01_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:competition_source_localization_pending_en; frozen pass=False

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Tekken 8 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live.
Original source in Thai: local://competition_rules/competition_rules_tekken8_psu_esports

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04326 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: Please retrieve the official CS2 rulebook evidence for game vetsion and match configurtion
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s01_c01', 'competition_rules_cs2_psu_phuket_2026_s02_c01', 'competition_rules_cs2_psu_phuket_2026_s03_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Scope of Application This regulation applies to all players, teams, and staff members participating officially in any CS2 competition organized by PSU Esports Studio - Phuket.
- The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited.
- Game Settings
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04889 — compound_context_boundary

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: What shuld I plat
- Legacy expected: ['clarification', 'equipment', 'games', 'no_answer', 'reservation', 'service_fee']; clarification_required
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Please tell me the zone, game type, or specific request you are interested in so I can answer from the verified catalog.

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04151 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: What do hte RoV tournament rules say about the rulebook scope and tournament identity
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_rov_blueket_2025_men_s01_c01', 'competition_rules_rov_blueket_2025_men_s02_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Arena of Valor (RoV) competition rules:
- Document overview: Competition Rules for Blueket Games 2025 Esports Event Game: Arena of Valor (RoV)
- Male Team Category
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-00147 — service_fee

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: What is the pricr of Overcooked 2
- Legacy expected: ['service_fee']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.99; source IDs=['game_detail_overcooked_2']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_game_detail_en; frozen pass=False

### คำตอบก่อนแก้

Overcooked 2: This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Which service, duration, and user group should I price: PC, PlayStation 5, Nintendo Switch, Cockpit, or VR?

### คำตอบหลังแก้

Verified English information:
Overcooked 2
Genre: Co-op cooking game
Overview: Overcooked 2 is a cooperative cooking game where players must divide tasks, prepare food, serve dishes, and manage a chaotic kitchen.
How to play: Work together to chop ingredients, cook, serve, clean up, and communicate with the team on time
Available at: Nintendo Switch Zone
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04126 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you cite the AOV rue concerning disconnections and reconnects
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_rov_blueket_2025_men_s06_c01', 'competition_rules_rov_blueket_2025_men_s06_c02']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Arena of Valor (RoV) competition rules:
- 4. Competition regulations and rules: Competition Rules 4. Regulations and Competition Rules 4.1. Basic Rules 4.1.1. Prohibited to use character names or phrases that are offensive or disrespectful toward others.
- 4. Competition regulations and rules: 4.3.2. If a competitor disconnects because of force majeure (such as an internet-service outage across the area or a game-server error), the affected team must notify the staff. Whether to allow a replay is at the referees' discretion.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-03439 — equipment

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: What is a ganing chair used for
- Legacy expected: ['equipment']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04847 — compound_context_boundary

- Priority: P2 source/ambiguity/label review
- Evidence: mixed_baseline_failure_primary_cause_pending
- คำถาม: Coukd you check this using verified informaion: helllo
- Legacy expected: ['general', 'knowledge', 'overview']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Both variants fail or clean is not certified. Investigate source gap, task/qualifier, localization and label contract before treating this as a spelling defect.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

I could not find verified PSU Esports Studio - Phuket information for this question.

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-01570 — schedule_calendar

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: I am planning a visit and would like to know: What is the studio policy for mondya play
- Legacy expected: ['reservation', 'schedule']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for schedule.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Monday: 09:00-12:00 is maintenance; the studio is open for play from 13:00-16:00.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for schedule.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04811 — compound_context_boundary

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: How mch does it cost? Please answer briefly
- Legacy expected: ['clarification', 'no_answer', 'service_fee']; safe_clarification
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for service_fee.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Which service, duration, and user group should I price: PC, PlayStation 5, Nintendo Switch, Cockpit, or VR?

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for service_fee.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-01339 — schedule_calendar

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Can I play in the mornimg
- Legacy expected: ['reservation', 'schedule']; answer_available
- ก่อนแก้: pipeline:games_unknown_target_en; confidence=0.99; source IDs=['service_game_availability']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:games_unknown_target_en; frozen pass=False

### คำตอบก่อนแก้

I could not find in the mornimg in the verified PSU game records. I will not substitute another game.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

The morning service period is 09:00-12:00. Monday morning is reserved for maintenance.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

I could not find in the mornimg in the verified PSU game records. I will not substitute another game.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04060 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could yyou cite the Counter Strike 2 rule concerning in-game settings
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s05_c01', 'competition_rules_cs2_psu_phuket_2026_s22_c01', 'competition_rules_cs2_psu_phuket_2026_s23_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Game Settings
- Equipment and Game Settings
- Game Setup
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-01758 — games_catalog_availability

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Which game can be played across multtiple zones
- Legacy expected: ['games']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for equipment.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Verified games available in multiple zones:
- Resident Evil 4: PlayStation 5 Zone, VR Zone
- Resident Evil Village: PlayStation 5 Zone, VR Zone
- TEKKEN 8: PC Zone, PlayStation 5 Zone
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for equipment.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04819 — compound_context_boundary

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Can I use an unknown gsme called Example Quest? Please use verified information
- Legacy expected: ['games', 'no_answer']; safe_no_answer
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

I could not find Example Quest in the verified PSU game records. I will not substitute another game.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [
    "Example Quest"
  ],
  "must_contain_any": [],
  "must_not_contain": [
    "Verified game catalog"
  ]
}
```

## MASTER-GT-EN-03616 — equipment

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me wiith this: What is the Nintendo Switch OLED used for
- Legacy expected: ['equipment']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.99; source IDs=['equipment_nintendo_switch_oled']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_equipment_item_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### คำตอบหลังแก้

Verified equipment record: Nintendo Switch OLED is listed in Nintendo Switch Zone.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04065 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: How is pauses and timeouts handled in the Counter-Strike 2 turnament rules
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s33_c01', 'competition_rules_cs2_psu_phuket_2026_s34_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.
- Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04055 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Wht do the CS2 tournament rules say about in-game settings
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s05_c01', 'competition_rules_cs2_psu_phuket_2026_s22_c01', 'competition_rules_cs2_psu_phuket_2026_s23_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Game Settings
- Equipment and Game Settings
- Game Setup
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-01593 — schedule_calendar

- Priority: P0 wrong task/target or omitted facet
- Evidence: paired_regression_primary_cause_pending
- คำถาม: I am planning a visit and would like to know: What time is the aftrrnoon session? Please use verified nformation
- Legacy expected: ['reservation', 'schedule']; answer_available
- ก่อนแก้: pipeline:structured_schedule_en; confidence=0.98; source IDs=['service_schedule']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:structured_schedule_en; frozen pass=True

### คำตอบก่อนแก้

Regular service hours are Monday-Friday. Monday morning and Friday afternoon are maintenance periods. Please specify a day for the exact play window.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

The afternoon service period is 13:00-16:00. Friday afternoon is reserved for maintenance.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

The afternoon service period is 13:00-16:00. Friday afternoon is reserved for maintenance.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [
    "13:00-16:00"
  ],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04809 — compound_context_boundary

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Can I use an unknown gamr called Example Quest
- Legacy expected: ['games', 'no_answer']; safe_no_answer
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

I could not find Example Quest in the verified PSU game records. I will not substitute another game.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [
    "Example Quest"
  ],
  "must_contain_any": [],
  "must_not_contain": [
    "Verified game catalog"
  ]
}
```

## MASTER-GT-EN-04037 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: What do the CS2 tornament rules say about in-march procedure
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.99; source IDs=['game_detail_cs2']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_game_detail_en; frozen pass=False

### คำตอบก่อนแก้

Counter-Strike 2: This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified English information:
Counter-Strike 2
Genre: Tactical FPS
Overview: Counter-Strike 2 is a competitive team shooter with attackers and defenders. The main objectives involve planting/defusing a bomb or eliminating opponents.
How to play: Play in rounds, must buy weapons, plan with your team, control territory, and use aiming along with communication to win the round
Available at: PC Zone
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04121 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: What do the RoV tourament rules say about disconnections and reconnects
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_rov_blueket_2025_men_s06_c01', 'competition_rules_rov_blueket_2025_men_s06_c02']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Arena of Valor (RoV) competition rules:
- 4. Competition regulations and rules: Competition Rules 4. Regulations and Competition Rules 4.1. Basic Rules 4.1.1. Prohibited to use character names or phrases that are offensive or disrespectful toward others.
- 4. Competition regulations and rules: 4.3.2. If a competitor disconnects because of force majeure (such as an internet-service outage across the area or a game-server error), the affected team must notify the staff. Whether to allow a replay is at the referees' discretion.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-00531 — reservation_policy

- Priority: P0 wrong task/target or omitted facet
- Evidence: trace_code_source_inspected
- คำถาม: Could you please help me with this: How many sessioons can one booking include
- Legacy expected: ['reservation']; answer_available
- ก่อนแก้: pipeline:rule_en; confidence=0.99; source IDs=['rule_en_booking_steps_natural']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: sessioons bypasses exact session limit rule and returns generic booking steps; route remains reservation and fixed rule confidence0.99 but numeric limit absent.
- หลังแก้: pipeline:rule_en; frozen pass=True

### คำตอบก่อนแก้

Booking steps:
• Select a service.
• Choose a date and time.
• Fill in your user information.
• Review the details.
• Pay by bank transfer.
• Upload the payment slip.
Source: https://esports.computing.psu.ac.th/reservation (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

One booking can include a maximum of 3 sessions.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

One booking can include a maximum of 3 sessions.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [
    "3 sessions"
  ],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04285 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: How is player conduct and sportsmanship handled in the Counter-Strike 2 touranment rules
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s35_c01', 'competition_rules_cs2_psu_phuket_2026_s36_c01', 'competition_rules_cs2_psu_phuket_2026_s54_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Player conduct: aggressive behavior, hate speech (racial/religious), and unsportsmanlike actions are prohibited.
- Behavior and Penalties
- 8. Penalty Table (Penalties) Violation Penalty Insulting / using verbal aggression Warning → Loss in that round → Disqualification Cheating in any form Loss in that round / Disqualification from competition Watching streams during gameplay Loss in that match Stopping the game without permission Loss in that round Using bugs Loss in that round or match...
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04269 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: What is the minimum sge requrement to enter this VALORANT tournament
- Legacy expected: ['competition_rules', 'no_answer']; no_answer_expected
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_valorant_psu_phuket_2026_s25_c01', 'competition_rules_valorant_psu_phuket_2026_s01_c01', 'competition_rules_valorant_psu_phuket_2026_s16_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=False

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.

### คำตอบหลังแก้

Verified VALORANT competition rules:
- In-Game Penalty Types * Warning - For first offenses with low impact. * Round Rollback - When an exploit clearly affects a round but intent cannot be determined. * Round Loss - When a player or team is found to have intentionally used an exploit for advantage. * Map Forfeit - For severe offenses or repeated violations that affect the map result.
- Document overview: Competition rules and format for VALORANT PSU Phuket VALORANT 2026 Tournament Update: 17/02/2026 English below Equipment and peripherals In LAN competitions, players must strictly adhere to equipment requirements for fairness.
- The organizer reserves the right to amend the regulations without prior notice. Equipment and Peripherals In LAN competitions, players must strictly comply with equipment regulations to ensure fair play.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-02647 — game_detail

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Please answer from verified studio infirmation: Which studio zne has Animal Crossing: New Horizons
- Legacy expected: ['games']; localization_pending
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.99; source IDs=['game_detail_animal_crossing']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_game_detail_en; frozen pass=True

### คำตอบก่อนแก้

Animal Crossing: New Horizons: This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Animal Crossing: New Horizons is available on: Nintendo Switch (1-2 Persons), Nintendo Switch (1-4 Persons). Studio zone(s): Nintendo Switch Zone.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified English information:
Animal Crossing: New Horizons
Genre: Life Simulation
Overview: Animal Crossing: New Horizons is a life simulation game where players decorate homes, collect items, create spaces, and chat with island residents.
How to play: Play casually by gathering resources, fishing, catching insects, decorating the island, and completing daily activities
Available at: Nintendo Switch Zone
Source: https://esports.phuket.psu.ac.th/Services/our-games (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "Nintendo Switch Zone"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04434 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Could you please help me with this: Please retrieve the official RoV rulebbook evidence for team size
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_rov_blueket_2025_men_s06_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Arena of Valor (RoV) competition rules:
- 4. Competition regulations and rules: Competition Rules 4. Regulations and Competition Rules 4.1. Basic Rules 4.1.1. Prohibited to use character names or phrases that are offensive or disrespectful toward others.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04089 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: How is dispute resolution handled in the Counter-Strike 2 yournament rules
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s06_c01', 'competition_rules_cs2_psu_phuket_2026_s58_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Language: The official language of the competition is Thai. All communication, protests, and reporting must be conducted in Thai, unless otherwise specified.
- Protests must be submitted within 15 minutes after the match ends, by the team captain or coach only.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04062 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: For Counter-Strike 2, can you verify the rule on pause and timeouts
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s33_c01', 'competition_rules_cs2_psu_phuket_2026_s34_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.
- Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04437 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: Coould you please help me with this: What do the TEKKEN 8 tournament rules say about the competition format
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_tekken8_psu_esports_s02_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Tekken 8 competition rules:
- Competition Rules * Offline mode * PlayStation 5 console used * Singles (1v1) format * Match format: * FT2: Winner is the first to win two games * Each game uses R3 rules (3 rounds per game) and 60S rule (60 seconds per round) * If tied at 1-1, a deciding game will be played
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-03428 — equipment

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: What is a gamimg keyboard
- Legacy expected: ['equipment']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Verified equipment record: Gaming Keyboard is listed in PC Zone.
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04181 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: What do the TEKKEN 8 tournament rules say about competitio equipment and devices
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_tekken8_psu_esports_s02_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Tekken 8 competition rules:
- Competition Rules * Offline mode * PlayStation 5 console used * Singles (1v1) format * Match format: * FT2: Winner is the first to win two games * Each game uses R3 rules (3 rounds per game) and 60S rule (60 seconds per round) * If tied at 1-1, a deciding game will be played
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04609 — members_overview_contact

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: What oosition does Mr. Kanokchai Siripanthisaraworn old
- Legacy expected: ['members', 'overview']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Official Thai source member record(s):
Names and role titles below are shown exactly as published by PSU.
- ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี - มหาวิทยาลัยสงขลานครินทร์
- รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี - มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- รศ.ดร.อซีส นันทอมรพงศ์: คณบดี - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ - มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- นายพฤทธิ์ เกษตรสมบูรณ์: นักวิชาการคอมพิวเตอร์ - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- นายณัฐวัฒน์ นิธิคุณานนต์: นักวิชาการคอมพิวเตอร์ - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- นายชนะชัย สิริพันธ์วราภรณ์: ผู้จัดการ - PSU Esports Studio - Phuket วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- นายณภัทร เชื้อเหล่าวานิช: นักศึกษาสหกิจ Game and 3D Developer - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- Mr. Amine Abidellaoui: Internship Student - High School Bristol Cannes, France
- นายสุพศิน อะนะฝรั่ง: นักศึกษาสหกิจ Web & AI Developer - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- Mr. Yanis Igoudjil: Internship Student - Industrial Engineering and Information Systems, EPF Graduate School of Engineering, Cachan Val-De-Marne, France
- นายภาสวุฒิ ชูติประชากิจ: นักศึกษาฝึกงานโครงการ Super AI SS6 ตำแหน่ง AI Chat Bot Developer - วิศวกรรมระบบไอโอทีและสารสนเทศ สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง
- นายษุภากรณ์ จิราจินดากุล: ประธาน
- นายนพัทธ์ ฝอยทอง: รองประธาน
- นายปัณณวิชญ์ หนูเรือง: เลขานุการ
- นายภูจิตร จิรวิริยาภรณ์: เหรัญญิก
- นายธนชาติ เอ่งฉ้วน: ประชาสัมพันธ์
- นางสาวกมลวรรณ นวลสาย: กรรมการ
- นางสาวชญาภา จันทร์เอิบ: กรรมการ
- นางสาวณัฐธิดา คำทะเนตร์: กรรมการ
- นางสาวสุภาสินี ธนภพ: กรรมการ
- นางสาวอาทิตยา แดงประดับ: กรรมการ
- นายณัฐพนธ์ อินทรสังขนาวิน: กรรมการ
- นายอภิวิชญ์ เลิศกมลรักษ์: กรรมการ
- นายอรรถนนท์ สุขแก้ว: กรรมการ
Source: https://esports.phuket.psu.ac.th/about-us/Members (official Thai source)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-04594 — members_overview_contact

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: How many categories are memmbers divided into
- Legacy expected: ['members', 'overview']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Official Thai source member record(s):
Names and role titles below are shown exactly as published by PSU.
- ผศ.ดร.นิวัติ แก้วประดับ: อธิการบดี - มหาวิทยาลัยสงขลานครินทร์
- รศ.ดร.พันธ์ ทองชุมนุม: รองอธิการบดี - มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- รศ.ดร.อซีส นันทอมรพงศ์: คณบดี - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- ผศ.ดร.ณัฐพงศ์ ทองเทพ: ผู้ช่วยอธิการบดีฝ่ายวิชาการ - มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- นายพฤทธิ์ เกษตรสมบูรณ์: นักวิชาการคอมพิวเตอร์ - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- นายณัฐวัฒน์ นิธิคุณานนต์: นักวิชาการคอมพิวเตอร์ - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- นายชนะชัย สิริพันธ์วราภรณ์: ผู้จัดการ - PSU Esports Studio - Phuket วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- นายณภัทร เชื้อเหล่าวานิช: นักศึกษาสหกิจ Game and 3D Developer - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- Mr. Amine Abidellaoui: Internship Student - High School Bristol Cannes, France
- นายสุพศิน อะนะฝรั่ง: นักศึกษาสหกิจ Web & AI Developer - วิทยาลัยการคอมพิวเตอร์ มหาวิทยาลัยสงขลานครินทร์ วิทยาเขตภูเก็ต
- Mr. Yanis Igoudjil: Internship Student - Industrial Engineering and Information Systems, EPF Graduate School of Engineering, Cachan Val-De-Marne, France
- นายภาสวุฒิ ชูติประชากิจ: นักศึกษาฝึกงานโครงการ Super AI SS6 ตำแหน่ง AI Chat Bot Developer - วิศวกรรมระบบไอโอทีและสารสนเทศ สถาบันเทคโนโลยีพระจอมเกล้าเจ้าคุณทหารลาดกระบัง
- นายษุภากรณ์ จิราจินดากุล: ประธาน
- นายนพัทธ์ ฝอยทอง: รองประธาน
- นายปัณณวิชญ์ หนูเรือง: เลขานุการ
- นายภูจิตร จิรวิริยาภรณ์: เหรัญญิก
- นายธนชาติ เอ่งฉ้วน: ประชาสัมพันธ์
- นางสาวกมลวรรณ นวลสาย: กรรมการ
- นางสาวชญาภา จันทร์เอิบ: กรรมการ
- นางสาวณัฐธิดา คำทะเนตร์: กรรมการ
- นางสาวสุภาสินี ธนภพ: กรรมการ
- นางสาวอาทิตยา แดงประดับ: กรรมการ
- นายณัฐพนธ์ อินทรสังขนาวิน: กรรมการ
- นายอภิวิชญ์ เลิศกมลรักษ์: กรรมการ
- นายอรรถนนท์ สุขแก้ว: กรรมการ
Source: https://esports.phuket.psu.ac.th/about-us/Members (official Thai source)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for this question.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": [
    "Local LLM"
  ]
}
```

## MASTER-GT-EN-03527 — equipment

- Priority: P1 task/qualifier or English evidence
- Evidence: paired_regression_primary_cause_pending
- คำถาม: Could you please help me with this: Does the PC Zone have hamin monitors? Please use verified information
- Legacy expected: ['equipment']; answer_available
- ก่อนแก้: pipeline:english_no_answer; confidence=0.52; source IDs=[]
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: Clean passes and noisy fails under the same contract. Trace records the changed route/facet, but exact damaged span and source applicability still require semantic review.
- หลังแก้: pipeline:english_no_answer; frozen pass=False

### คำตอบก่อนแก้

I could not find verified PSU Esports Studio - Phuket information for schedule.

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

Verified equipment in PC Zone:
- Gaming PC model MSI MAG Infinite S3 14th (PC Zone) - 10 Units
- Gaming Monitor (PC Zone) - 10 Units
- Gaming Keyboard (PC Zone)
- Gaming Mouse (PC Zone)
- Gaming Headset (PC Zone)
- Gaming Chair (PC Zone) - 10 Units
Source: https://esports.phuket.psu.ac.th/home (original source in Thai)

### คำตอบหลังแก้

I could not find verified PSU Esports Studio - Phuket information for schedule.

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [
    "Gaming Monitor",
    "Gaming Monitors"
  ],
  "must_not_contain": []
}
```

## MASTER-GT-EN-04100 — competition_rules

- Priority: P1 task/qualifier or English evidence
- Evidence: branch_reason_confirmed_primary_cause_pending
- คำถาม: lPease retrieve the official CS2 rulebook evidence for the rulebook scope and tournament identity
- Legacy expected: ['competition_rules']; answer_available
- ก่อนแก้: pipeline:missing_english_localization; confidence=0.96; source IDs=['competition_rules_cs2_psu_phuket_2026_s02_c01', 'competition_rules_cs2_psu_phuket_2026_s04_c01', 'competition_rules_cs2_psu_phuket_2026_s01_c01']
- Top candidate: ไม่มี central ranking ใน trace ของผลนี้; score=N/A; reason=ใช้ branch reason ใน JSON audit
- สาเหตุ/ขอบเขตการยืนยัน: English branch reports missing source-hash-matched localization. Inspect task/target first: a pending translation can also be downstream of the wrong operation.
- หลังแก้: pipeline:structured_competition_rules_en; frozen pass=True

### คำตอบก่อนแก้

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### Reference แบบสะอาด (ต้องตรวจ source ก่อนเรียกว่า correct gold)

This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation.
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### คำตอบหลังแก้

Verified Counter-Strike 2 competition rules:
- Scope of Application This regulation applies to all players, teams, and staff members participating officially in any CS2 competition organized by PSU Esports Studio - Phuket.
- PSU Phuket CS2 2026 Tournament
- Document overview: Competition Rules and Format for Counter-Strike 2
Source: https://esports.computing.psu.ac.th/ (original source in Thai)

### เงื่อนไขเนื้อหาของ GT เดิม

```json
{
  "must_contain": [],
  "must_contain_any": [],
  "must_not_contain": []
}
```
