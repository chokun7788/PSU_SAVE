# วิเคราะห์สาเหตุ r28 จากคำถามจริงในชุดทดสอบ

## การอ่านผล

Baseline r27 เมื่อใช้เกณฑ์ v3 เดียวกัน: 63/280; หลังแก้ Candidate B: 280/280. เกณฑ์ 3 ข้อถูกแก้เพราะเดิมเรียก clause Cypher ที่คำถามไม่ได้ถาม ไม่ใช่แก้เกณฑ์ตามคำตอบผิด; ดู oracle_revision_audit.json. การทดสอบเป็นคำถามที่สร้างเพื่อพัฒนา ไม่ใช่คำถามผู้ใช้จริงหรือ owner signoff.

## สาเหตุและลำดับแก้

1. เลือกหัวข้อหรือ clause ผิด: ค่าสมัครถูกตีเป็น late_registration, final decision ถูกตีเป็น final match; เสี่ยงตอบข้อมูลผิดแม้มีแหล่งอ้างอิงของเกมถูกต้อง.
2. ตอบขัดกันหรือยืมข้ออื่น: Tekken pause เริ่มด้วยอนุญาตก่อนเห็นข้อห้าม, RoV ข้อที่ขาดใช้บทลงโทษข้างเคียง; เพิ่มสถานะ conflict และจับเลขข้อแบบ exact.
3. คำถามหลายเรื่องตกหล่น: exclude ตรวจทั้งประโยคแล้วตัดหัวข้อ normal money/overtime, language/protest, map pool/mapban; แยกเงื่อนไขตามประเด็นที่ถาม.
4. ประเด็นเฉพาะไม่มีตัวเลือก clause: เพิ่มแนวคิดทั่วไปสองภาษา เช่น bug, stream, install, macro, prep, drinks, custom settings จาก source เดิม ไม่ใช้ alias ทั้งประโยค.
5. คำอังกฤษของ source แตกต่างกับ pattern: clause macro/customization มีข้อความอังกฤษที่ถูกต้องแต่ไม่ผ่าน pattern จึงตกไปหัวข้อกว้าง; ขยายตามข้อความที่อนุมัติและ hash ตรง.
6. การตรวจคำตอบ: ประโยค no-answer ใหม่ต้องเข้า contract; คำตอบ partial ยังต้องตรวจ source ของเกม ไม่ให้ข้อความ “ไม่พบ” ทำให้ข้าม evidence gate.
7. เกณฑ์ตรวจละเอียด: source presence หรือ route ถูกไม่ได้ยืนยันเงื่อนไขครบ; ใช้ complete clauses + first line + game evidence และบันทึก raw/source-grade แยก.

## คะแนนและเหตุผลที่เลือก

เส้นทางรายละเอียดใช้เงื่อนไขจับแนวคิดและรูปประโยค ไม่ได้ให้ LLM สุ่มเลือก clause. ค่า confidence 0.97 ใน trace เป็นค่าที่ตั้งให้เส้นทางนี้เมื่อผ่านเงื่อนไข ไม่ใช่ความน่าจะเป็นที่สอบเทียบแล้ว. การเลือก row ใช้จำนวน clause ที่ตรงแนวคิดและลำดับ source; เมื่อไม่มีรายละเอียดครอบคลุมจะตกไปเส้นทาง facet/retrieval ซึ่งอาจได้หัวข้อกว้าง. การเปลี่ยนค่า confidence อย่างเดียวจึงแก้ความผิดของการตีประเด็นไม่ได้. ด้านล่างเก็บ trace ที่นำไปสู่คำตอบจริงพร้อมคำที่ควรปรากฏ.

## แยกทุก anchor ที่ผิดใน baseline

### cs2-mode (en)

คำถาม: Which competitive mode is used under CS2 tournament rules?

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:Competitive mode (5v5), first_line_off_topic

คำตอบก่อนแก้:

```text
Selected Counter-Strike 2 competition rules from the recorded rulebook:
Tournament: Counter-Strike 2 / 2026


**Competition format**
•    Tournament format: Single Elimination

**Players and team composition**
•    Team composition Each team consists of 5 players

**Eligibility and registration**
•    Registration of players is not permitted after the registration period has closed.

**Competition equipment**
•    Players may bring their own keyboard (wired or wireless), mouse (wired or wireless), mouse cord holder (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.

**Match settings**
•    The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited.

**Before the match**
•    Mobile phones, tablets, or smartwatches are prohibited in the competition area until the match concludes.

**Pauses and timeouts**
•    Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.
•    Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

This is a summary of selected clauses. Ask about a specific topic for details.
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

เนื้อหาที่ควรปรากฏครบจาก source:

- Competitive mode (5v5)

Source IDs: competition_rules_cs2_psu_phuket_2026_s23_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "competition_overview",
    "decision": "accepted",
    "confidence": 0.98,
    "detail": "source clauses across sections; headings alone are insufficient",
    "metadata": {
      "section_ids": [
        "competition_rules_cs2_psu_phuket_2026_s20_c01",
        "competition_rules_cs2_psu_phuket_2026_s18_c01",
        "competition_rules_cs2_psu_phuket_2026_s12_c01",
        "competition_rules_cs2_psu_phuket_2026_s41_c01",
        "competition_rules_cs2_psu_phuket_2026_s05_c01",
        "competition_rules_cs2_psu_phuket_2026_s51_c01",
        "competition_rules_cs2_psu_phuket_2026_s33_c01",
        "competition_rules_cs2_psu_phuket_2026_s34_c01"
      ],
      "game_ids": [
        "cs2"
      ],
      "validation_errors": []
    }
  }
]
```

คำตอบหลังแก้:

```text
Answer: Competitive mode (5v5)

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### cs2-bracket (th)

คำถาม: กติกา CS2 ประกาศสายล่วงหน้ากี่วันและมาสายเป็นยังไง

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: wrong_outcome, missing_complete_clause:7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์, first_line_off_topic, wrong_game_source

คำตอบก่อนแก้:

```text
ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
```

เนื้อหาที่ควรปรากฏครบจาก source:

- 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์

Source IDs: competition_rules_cs2_psu_phuket_2026_s15_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.9,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "cs2",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "Counter-Strike 2",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "cs2"
      ],
      "competition_game_labels": [
        "Counter-Strike 2"
      ],
      "competition_rulebook_ids": [
        "competition_rules_cs2_psu_phuket_2026"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "cs2"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=Counter-Strike 2 intent=schedule_location",
    "metadata": {
      "category": "competition_rules",
      "game": "Counter-Strike 2",
      "intent": "schedule_location"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "facet_not_covered_safe_no_answer",
    "confidence": 0.92,
    "detail": "retrieved_source_does_not_prove_requested_facet",
    "metadata": {
      "hit_count": 8,
      "covered": false,
      "facet": "unspecified",
      "target_game_ids": [
        "cs2"
      ],
      "matched_chunk_ids": [
        "competition_rules_cs2_psu_phuket_2026_s15_c01",
        "competition_rules_cs2_psu_phuket_2026_s04_c01",
        "competition_rules_cs2_psu_phuket_2026_s06_c01",
        "competition_rules_cs2_psu_phuket_2026_s08_c01",
        "competition_rules_cs2_psu_phuket_2026_s45_c01",
        "competition_rules_cs2_psu_phuket_2026_s36_c01",
        "competition_rules_cs2_psu_phuket_2026_s49_c01",
        "competition_rules_cs2_psu_phuket_2026_s54_c01"
      ],
      "reason": "retrieved_source_does_not_prove_requested_facet"
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### cs2-bugs (en)

คำถาม: Under CS2 tournament rules, may players use map or engine bugs?

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:Exploiting map or game-engine bugs is strictly prohibited. Violations result in forfeiture of that round/map or disqualification., first_line_off_topic

คำตอบก่อนแก้:

```text
Selected Counter-Strike 2 competition rules from the recorded rulebook:
Tournament: Counter-Strike 2 / 2026


**Competition format**
•    Tournament format: Single Elimination

**Players and team composition**
•    Team composition Each team consists of 5 players

**Eligibility and registration**
•    Registration of players is not permitted after the registration period has closed.

**Competition equipment**
•    Players may bring their own keyboard (wired or wireless), mouse (wired or wireless), mouse cord holder (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.

**Match settings**
•    The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited.

**Before the match**
•    Mobile phones, tablets, or smartwatches are prohibited in the competition area until the match concludes.

**Pauses and timeouts**
•    Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.
•    Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

This is a summary of selected clauses. Ask about a specific topic for details.
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

เนื้อหาที่ควรปรากฏครบจาก source:

- Exploiting map or game-engine bugs is strictly prohibited. Violations result in forfeiture of that round/map or disqualification.

Source IDs: competition_rules_cs2_psu_phuket_2026_s37_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "competition_overview",
    "decision": "accepted",
    "confidence": 0.98,
    "detail": "source clauses across sections; headings alone are insufficient",
    "metadata": {
      "section_ids": [
        "competition_rules_cs2_psu_phuket_2026_s20_c01",
        "competition_rules_cs2_psu_phuket_2026_s18_c01",
        "competition_rules_cs2_psu_phuket_2026_s12_c01",
        "competition_rules_cs2_psu_phuket_2026_s41_c01",
        "competition_rules_cs2_psu_phuket_2026_s05_c01",
        "competition_rules_cs2_psu_phuket_2026_s51_c01",
        "competition_rules_cs2_psu_phuket_2026_s33_c01",
        "competition_rules_cs2_psu_phuket_2026_s34_c01"
      ],
      "game_ids": [
        "cs2"
      ],
      "validation_errors": []
    }
  }
]
```

คำตอบหลังแก้:

```text
Answer: Exploiting map or game-engine bugs is strictly prohibited. Violations result in forfeiture of that round/map or disqualification.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### cs2-streams (en)

คำถาม: Under CS2 tournament rules, may players watch live streams during the match?

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:Watching streams: Players are prohibited from watching live streams during competition., first_line_off_topic

คำตอบก่อนแก้:

```text
Selected Counter-Strike 2 competition rules from the recorded rulebook:
Tournament: Counter-Strike 2 / 2026


**Competition format**
•    Tournament format: Single Elimination

**Players and team composition**
•    Team composition Each team consists of 5 players

**Eligibility and registration**
•    Registration of players is not permitted after the registration period has closed.

**Competition equipment**
•    Players may bring their own keyboard (wired or wireless), mouse (wired or wireless), mouse cord holder (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.

**Match settings**
•    The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited.

**Before the match**
•    Mobile phones, tablets, or smartwatches are prohibited in the competition area until the match concludes.

**Pauses and timeouts**
•    Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.
•    Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

This is a summary of selected clauses. Ask about a specific topic for details.
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

เนื้อหาที่ควรปรากฏครบจาก source:

- Watching streams: Players are prohibited from watching live streams during competition.

Source IDs: competition_rules_cs2_psu_phuket_2026_s38_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "competition_overview",
    "decision": "accepted",
    "confidence": 0.98,
    "detail": "source clauses across sections; headings alone are insufficient",
    "metadata": {
      "section_ids": [
        "competition_rules_cs2_psu_phuket_2026_s20_c01",
        "competition_rules_cs2_psu_phuket_2026_s18_c01",
        "competition_rules_cs2_psu_phuket_2026_s12_c01",
        "competition_rules_cs2_psu_phuket_2026_s41_c01",
        "competition_rules_cs2_psu_phuket_2026_s05_c01",
        "competition_rules_cs2_psu_phuket_2026_s51_c01",
        "competition_rules_cs2_psu_phuket_2026_s33_c01",
        "competition_rules_cs2_psu_phuket_2026_s34_c01"
      ],
      "game_ids": [
        "cs2"
      ],
      "validation_errors": []
    }
  }
]
```

คำตอบหลังแก้:

```text
Answer: Watching streams: Players are prohibited from watching live streams during competition.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### cs2-gear-quality (en)

คำถาม: Under CS2 tournament rules, who is responsible for the quality and readiness of personal equipment?

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:Players are responsible for the quality and readiness of their own equipment., first_line_off_topic

คำตอบก่อนแก้:

```text
Answer: Players may bring their own keyboard (wired or wireless), mouse (wired or wireless), mouse cord holder (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

เนื้อหาที่ควรปรากฏครบจาก source:

- Players are responsible for the quality and readiness of their own equipment.

Source IDs: competition_rules_cs2_psu_phuket_2026_s42_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "competition_detail",
    "decision": "accepted",
    "confidence": 0.97,
    "detail": "one rulebook, literal complete clauses, no inferred policies",
    "metadata": {
      "concepts": [
        "own_equipment"
      ],
      "source_ids": [
        "competition_rules_cs2_psu_phuket_2026_s41_c01"
      ],
      "validation_errors": []
    }
  },
  {
    "stage": "semantic_route",
    "decision": "skipped_exact_competition_facet",
    "confidence": 0.97,
    "detail": "explicit detail propositions already bound to source clauses",
    "metadata": {}
  },
  {
    "stage": "competition_source_grounding",
    "decision": "detail_clauses_covered",
    "confidence": 0.97,
    "detail": "all requested detail concepts have source clauses",
    "metadata": {
      "concepts": [
        "own_equipment"
      ],
      "source_ids": [
        "competition_rules_cs2_psu_phuket_2026_s41_c01"
      ]
    }
  }
]
```

คำตอบหลังแก้:

```text
Answer: Players are responsible for the quality and readiness of their own equipment.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### cs2-custom-settings (th)

คำถาม: กติกา CS2 ปรับ Brightness Resolution Crosshair ได้ไหมและปรับที่ไหน

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น, first_line_off_topic

คำตอบก่อนแก้:

```text
คำตอบ: 1. อุปกรณ์ที่อนุญาต

รายละเอียดที่เกี่ยวข้อง:
•    2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

เนื้อหาที่ควรปรากฏครบจาก source:

- 1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น

Source IDs: competition_rules_cs2_psu_phuket_2026_s45_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.9,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "cs2",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "Counter-Strike 2",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "cs2"
      ],
      "competition_game_labels": [
        "Counter-Strike 2"
      ],
      "competition_rulebook_ids": [
        "competition_rules_cs2_psu_phuket_2026"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "cs2"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=Counter-Strike 2 intent=equipment",
    "metadata": {
      "category": "competition_rules",
      "game": "Counter-Strike 2",
      "intent": "equipment"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "accepted",
    "confidence": 0.84,
    "detail": "target-filtered source chunks are preferred over summary fact cards",
    "metadata": {
      "hit_count": 8,
      "validation_errors": [],
      "pause_detail_missing": false
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: 1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### cs2-macros (en)

คำถาม: Under CS2 tournament rules, are scripts or macros allowed?

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:No scripts or macros are allowed at all., first_line_off_topic

คำตอบก่อนแก้:

```text
Selected Counter-Strike 2 competition rules from the recorded rulebook:
Tournament: Counter-Strike 2 / 2026


**Competition format**
•    Tournament format: Single Elimination

**Players and team composition**
•    Team composition Each team consists of 5 players

**Eligibility and registration**
•    Registration of players is not permitted after the registration period has closed.

**Competition equipment**
•    Players may bring their own keyboard (wired or wireless), mouse (wired or wireless), mouse cord holder (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.

**Match settings**
•    The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited.

**Before the match**
•    Mobile phones, tablets, or smartwatches are prohibited in the competition area until the match concludes.

**Pauses and timeouts**
•    Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.
•    Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

This is a summary of selected clauses. Ask about a specific topic for details.
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

เนื้อหาที่ควรปรากฏครบจาก source:

- No scripts or macros are allowed at all.

Source IDs: competition_rules_cs2_psu_phuket_2026_s46_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "competition_overview",
    "decision": "accepted",
    "confidence": 0.98,
    "detail": "source clauses across sections; headings alone are insufficient",
    "metadata": {
      "section_ids": [
        "competition_rules_cs2_psu_phuket_2026_s20_c01",
        "competition_rules_cs2_psu_phuket_2026_s18_c01",
        "competition_rules_cs2_psu_phuket_2026_s12_c01",
        "competition_rules_cs2_psu_phuket_2026_s41_c01",
        "competition_rules_cs2_psu_phuket_2026_s05_c01",
        "competition_rules_cs2_psu_phuket_2026_s51_c01",
        "competition_rules_cs2_psu_phuket_2026_s33_c01",
        "competition_rules_cs2_psu_phuket_2026_s34_c01"
      ],
      "game_ids": [
        "cs2"
      ],
      "validation_errors": []
    }
  }
]
```

คำตอบหลังแก้:

```text
Answer: No scripts or macros are allowed at all.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### cs2-install (th)

คำถาม: กติกา CS2 ติดตั้งโปรแกรมเองได้ไหม

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้, first_line_off_topic

คำตอบก่อนแก้:

```text
คำตอบ: 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้

รายละเอียดที่เกี่ยวข้อง:
•    2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

เนื้อหาที่ควรปรากฏครบจาก source:

- 4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้

Source IDs: competition_rules_cs2_psu_phuket_2026_s47_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.9,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "cs2",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "Counter-Strike 2",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "cs2"
      ],
      "competition_game_labels": [
        "Counter-Strike 2"
      ],
      "competition_rulebook_ids": [
        "competition_rules_cs2_psu_phuket_2026"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "cs2"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=Counter-Strike 2 intent=equipment",
    "metadata": {
      "category": "competition_rules",
      "game": "Counter-Strike 2",
      "intent": "equipment"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "accepted",
    "confidence": 0.84,
    "detail": "target-filtered source chunks are preferred over summary fact cards",
    "metadata": {
      "hit_count": 8,
      "validation_errors": [],
      "pause_detail_missing": false
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: 4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### cs2-prep (th)

คำถาม: กติกา CS2 ในช่วงเตรียมตัวมีผู้เล่นได้กี่คน

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: wrong_outcome, missing_complete_clause:1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน, first_line_off_topic, wrong_game_source

คำตอบก่อนแก้:

```text
ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
```

เนื้อหาที่ควรปรากฏครบจาก source:

- 1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน

Source IDs: competition_rules_cs2_psu_phuket_2026_s50_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.9,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "cs2",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "Counter-Strike 2",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "cs2"
      ],
      "competition_game_labels": [
        "Counter-Strike 2"
      ],
      "competition_rulebook_ids": [
        "competition_rules_cs2_psu_phuket_2026"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "cs2"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=Counter-Strike 2 intent=area_rules",
    "metadata": {
      "category": "competition_rules",
      "game": "Counter-Strike 2",
      "intent": "area_rules"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "facet_not_covered_safe_no_answer",
    "confidence": 0.92,
    "detail": "retrieved_source_does_not_prove_requested_facet",
    "metadata": {
      "hit_count": 8,
      "covered": false,
      "facet": "unspecified",
      "target_game_ids": [
        "cs2"
      ],
      "matched_chunk_ids": [
        "competition_rules_cs2_psu_phuket_2026_s50_c01",
        "competition_rules_cs2_psu_phuket_2026_s18_c01",
        "competition_rules_cs2_psu_phuket_2026_s41_c01",
        "competition_rules_cs2_psu_phuket_2026_s04_c01",
        "competition_rules_cs2_psu_phuket_2026_s36_c01",
        "competition_rules_cs2_psu_phuket_2026_s38_c01",
        "competition_rules_cs2_psu_phuket_2026_s45_c01",
        "competition_rules_cs2_psu_phuket_2026_s52_c01"
      ],
      "reason": "retrieved_source_does_not_prove_requested_facet"
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: 1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### cs2-drinks (th)

คำถาม: กติกา CS2 ในพื้นที่แข่งอนุญาตอาหารเครื่องดื่มอะไรบ้าง

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: wrong_outcome, missing_complete_clause:4. อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น, first_line_off_topic, wrong_game_source

คำตอบก่อนแก้:

```text
ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
```

เนื้อหาที่ควรปรากฏครบจาก source:

- 4. อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น

Source IDs: competition_rules_cs2_psu_phuket_2026_s53_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.9,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "cs2",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "Counter-Strike 2",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "cs2"
      ],
      "competition_game_labels": [
        "Counter-Strike 2"
      ],
      "competition_rulebook_ids": [
        "competition_rules_cs2_psu_phuket_2026"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "cs2"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=Counter-Strike 2 intent=area_rules",
    "metadata": {
      "category": "competition_rules",
      "game": "Counter-Strike 2",
      "intent": "area_rules"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "facet_not_covered_safe_no_answer",
    "confidence": 0.92,
    "detail": "retrieved_source_does_not_prove_requested_facet",
    "metadata": {
      "hit_count": 8,
      "covered": false,
      "facet": "unspecified",
      "target_game_ids": [
        "cs2"
      ],
      "matched_chunk_ids": [
        "competition_rules_cs2_psu_phuket_2026_s53_c01",
        "competition_rules_cs2_psu_phuket_2026_s43_c01",
        "competition_rules_cs2_psu_phuket_2026_s50_c01",
        "competition_rules_cs2_psu_phuket_2026_s08_c01",
        "competition_rules_cs2_psu_phuket_2026_s38_c01",
        "competition_rules_cs2_psu_phuket_2026_s49_c01",
        "competition_rules_cs2_psu_phuket_2026_s51_c01",
        "competition_rules_cs2_psu_phuket_2026_s56_c01"
      ],
      "reason": "retrieved_source_does_not_prove_requested_facet"
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: 4. อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### cs2-authority (th)

คำถาม: กติกา CS2 คำตัดสินใครถือเป็นที่สุดและผู้จัดเปลี่ยนกฎได้ไหม

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: wrong_outcome, missing_complete_clause:1. อำนาจตัดสิน คำตัดสินของกรรมการ และผู้จัดถือเป็นที่สิ้นสุด ฝ่ายจัดมีสิทธิ์แก้ไขกฎตามความเหมาะสมเพื่อความยุติธรรม, first_line_off_topic, wrong_game_source

คำตอบก่อนแก้:

```text
ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
```

เนื้อหาที่ควรปรากฏครบจาก source:

- 1. อำนาจตัดสิน คำตัดสินของกรรมการ และผู้จัดถือเป็นที่สิ้นสุด ฝ่ายจัดมีสิทธิ์แก้ไขกฎตามความเหมาะสมเพื่อความยุติธรรม

Source IDs: competition_rules_cs2_psu_phuket_2026_s57_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.9,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "cs2",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "Counter-Strike 2",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "cs2"
      ],
      "competition_game_labels": [
        "Counter-Strike 2"
      ],
      "competition_rulebook_ids": [
        "competition_rules_cs2_psu_phuket_2026"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "cs2"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=Counter-Strike 2 intent=policy",
    "metadata": {
      "category": "competition_rules",
      "game": "Counter-Strike 2",
      "intent": "policy"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "facet_not_covered_safe_no_answer",
    "confidence": 0.92,
    "detail": "retrieved_source_does_not_prove_requested_facet",
    "metadata": {
      "hit_count": 8,
      "covered": false,
      "facet": "unspecified",
      "target_game_ids": [
        "cs2"
      ],
      "matched_chunk_ids": [
        "competition_rules_cs2_psu_phuket_2026_s43_c01",
        "competition_rules_cs2_psu_phuket_2026_s48_c01",
        "competition_rules_cs2_psu_phuket_2026_s57_c01",
        "competition_rules_cs2_psu_phuket_2026_s08_c01",
        "competition_rules_cs2_psu_phuket_2026_s38_c01",
        "competition_rules_cs2_psu_phuket_2026_s49_c01",
        "competition_rules_cs2_psu_phuket_2026_s56_c01",
        "competition_rules_cs2_psu_phuket_2026_s36_c01"
      ],
      "reason": "retrieved_source_does_not_prove_requested_facet"
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: 1. อำนาจตัดสิน คำตัดสินของกรรมการ และผู้จัดถือเป็นที่สิ้นสุด ฝ่ายจัดมีสิทธิ์แก้ไขกฎตามความเหมาะสมเพื่อความยุติธรรม

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### valorant-macros (th)

คำถาม: กติกา VALORANT มาโครทั้งซอฟต์แวร์และฮาร์ดแวร์ใช้ได้ไหม

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:ห้ามใช้มาโคร (Macros) ทั้งที่ตั้งค่าผ่านซอฟต์แวร์หรือฮาร์ดแวร์, first_line_off_topic

คำตอบก่อนแก้:

```text
คำตอบ: 2. การหยุดเกมทางเทคนิค (Technical Pause)

รายละเอียดที่เกี่ยวข้อง:
•    ใช้เมื่อมีปัญหาอุปกรณ์ขัดข้อง, หลุดจากการเชื่อมต่อ หรือปัญหาซอฟต์แวร์
•    ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที
•    เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

เนื้อหาที่ควรปรากฏครบจาก source:

- ห้ามใช้มาโคร (Macros) ทั้งที่ตั้งค่าผ่านซอฟต์แวร์หรือฮาร์ดแวร์

Source IDs: competition_rules_valorant_psu_phuket_2026_s01_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.9,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "valorant",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "VALORANT",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "valorant"
      ],
      "competition_game_labels": [
        "VALORANT"
      ],
      "competition_rulebook_ids": [
        "competition_rules_valorant_psu_phuket_2026"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "valorant"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=VALORANT intent=pause",
    "metadata": {
      "category": "competition_rules",
      "game": "VALORANT",
      "intent": "pause"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "accepted",
    "confidence": 0.84,
    "detail": "target-filtered source chunks are preferred over summary fact cards",
    "metadata": {
      "hit_count": 8,
      "validation_errors": [],
      "pause_detail_missing": false
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: ห้ามใช้มาโคร (Macros) ทั้งที่ตั้งค่าผ่านซอฟต์แวร์หรือฮาร์ดแวร์

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### valorant-prep (th)

คำถาม: กติกา VALORANT ช่วง Match Prep มีผู้เล่นได้กี่คน

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: wrong_outcome, missing_complete_clause:จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน, first_line_off_topic, wrong_game_source

คำตอบก่อนแก้:

```text
ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
```

เนื้อหาที่ควรปรากฏครบจาก source:

- จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน

Source IDs: competition_rules_valorant_psu_phuket_2026_s02_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.9,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "valorant",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "VALORANT",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "valorant"
      ],
      "competition_game_labels": [
        "VALORANT"
      ],
      "competition_rulebook_ids": [
        "competition_rules_valorant_psu_phuket_2026"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "valorant"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=VALORANT intent=area_rules",
    "metadata": {
      "category": "competition_rules",
      "game": "VALORANT",
      "intent": "area_rules"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "facet_not_covered_safe_no_answer",
    "confidence": 0.92,
    "detail": "retrieved_source_does_not_prove_requested_facet",
    "metadata": {
      "hit_count": 8,
      "covered": false,
      "facet": "unspecified",
      "target_game_ids": [
        "valorant"
      ],
      "matched_chunk_ids": [
        "competition_rules_valorant_psu_phuket_2026_s02_c01",
        "competition_rules_valorant_psu_phuket_2026_s08_c01",
        "competition_rules_valorant_psu_phuket_2026_s07_c01",
        "competition_rules_valorant_psu_phuket_2026_s01_c01",
        "competition_rules_valorant_psu_phuket_2026_s06_c01",
        "competition_rules_valorant_psu_phuket_2026_s03_c01",
        "competition_rules_valorant_psu_phuket_2026_s11_c01",
        "competition_rules_valorant_psu_phuket_2026_s17_c01"
      ],
      "reason": "retrieved_source_does_not_prove_requested_facet"
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### valorant-drinks (th)

คำถาม: กติกา VALORANT กินดื่มอะไรได้ในพื้นที่แข่ง

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: wrong_outcome, missing_complete_clause:อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น, first_line_off_topic, wrong_game_source

คำตอบก่อนแก้:

```text
ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
```

เนื้อหาที่ควรปรากฏครบจาก source:

- อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น

Source IDs: competition_rules_valorant_psu_phuket_2026_s02_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.9,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "valorant",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "VALORANT",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "valorant"
      ],
      "competition_game_labels": [
        "VALORANT"
      ],
      "competition_rulebook_ids": [
        "competition_rules_valorant_psu_phuket_2026"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "valorant"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=VALORANT intent=area_rules",
    "metadata": {
      "category": "competition_rules",
      "game": "VALORANT",
      "intent": "area_rules"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "facet_not_covered_safe_no_answer",
    "confidence": 0.92,
    "detail": "retrieved_source_does_not_prove_requested_facet",
    "metadata": {
      "hit_count": 8,
      "covered": false,
      "facet": "unspecified",
      "target_game_ids": [
        "valorant"
      ],
      "matched_chunk_ids": [
        "competition_rules_valorant_psu_phuket_2026_s02_c01",
        "competition_rules_valorant_psu_phuket_2026_s08_c01",
        "competition_rules_valorant_psu_phuket_2026_s09_c01",
        "competition_rules_valorant_psu_phuket_2026_s01_c01",
        "competition_rules_valorant_psu_phuket_2026_s06_c01",
        "competition_rules_valorant_psu_phuket_2026_s05_c01",
        "competition_rules_valorant_psu_phuket_2026_s03_c01",
        "competition_rules_valorant_psu_phuket_2026_s04_c01"
      ],
      "reason": "retrieved_source_does_not_prove_requested_facet"
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### valorant-regular-timeout (en)

คำถาม: Under VALORANT tournament rules, how many Tactical Timeouts are allowed in regulation and how long is each?

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:2 requests per map during regulation (first 24 rounds), 60 seconds each., first_line_off_topic

คำตอบก่อนแก้:

```text
Answer: Each team may request up to 2 timeouts per map during regulation (first 24 rounds), each lasting 60 seconds.

Details:
• During Overtime, each team receives 1 additional timeout. Timeouts from regulation do not carry over.

Rulebook: VALORANT
Source: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

เนื้อหาที่ควรปรากฏครบจาก source:

- 2 requests per map during regulation (first 24 rounds), 60 seconds each.

Source IDs: competition_rules_valorant_psu_phuket_2026_s06_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "bilingual_route",
    "decision": "pipeline:structured_competition_rules_en",
    "confidence": 0.94,
    "detail": "English competition localization overlay matched current Thai source hashes",
    "metadata": {
      "effective_locale": "en",
      "route_category": "competition_rules",
      "route_intent": "competition_rule_lookup",
      "runtime_translation": false
    }
  }
]
```

คำตอบหลังแก้:

```text
Answer: 2 requests per map during regulation (first 24 rounds), 60 seconds each.

Rulebook: VALORANT
Source: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### valorant-outside (th)

คำถาม: กติกา VALORANT ใช้สกิลนอกขอบแผนที่เพื่อหาข้อมูลได้ไหม

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: first_line_off_topic

คำตอบก่อนแก้:

```text
คำตอบ: การเลือกแผนที่ (Map Pool): ประกอบด้วย 7 แผนที่ตามที่กำหนด ได้แก่

รายละเอียดที่เกี่ยวข้อง:
•    แผนที่ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 4 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive
•    ห้ามวางกล้อง Cypher ในจุดที่มองไม่เห็นหรือทำลายไม่ได้ผ่านการทะลุ Texture ของแผนที่
•    ห้ามใช้สกิลในพื้นที่นอกขอบเขตแผนที่ (Out of boundaries) เพื่อหาข้อมูลหรือสร้างความได้เปรียบ
•    ข้อยกเว้นพิเศษ สกิล ZERO/POINT ของ KAY/O สามารถใช้ภายนอกแผนที่หรือจุดที่ทำลายไม่ได้ได้ แต่ตัวมีดห้ามพุ่งทะลุ Texture ที่ควรจะเป็นของแข็ง
•    แบนจนเหลือ 3 แผนที่

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

เนื้อหาที่ควรปรากฏครบจาก source:

- ห้ามใช้สกิลในพื้นที่นอกขอบเขตแผนที่ (Out of boundaries) เพื่อหาข้อมูลหรือสร้างความได้เปรียบ
- ข้อยกเว้นพิเศษ สกิล ZERO/POINT ของ KAY/O สามารถใช้ภายนอกแผนที่หรือจุดที่ทำลายไม่ได้ได้ แต่ตัวมีดห้ามพุ่งทะลุ Texture ที่ควรจะเป็นของแข็ง

Source IDs: competition_rules_valorant_psu_phuket_2026_s09_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.9,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "valorant",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "VALORANT",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "valorant"
      ],
      "competition_game_labels": [
        "VALORANT"
      ],
      "competition_rulebook_ids": [
        "competition_rules_valorant_psu_phuket_2026"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "valorant"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=VALORANT intent=map_pool",
    "metadata": {
      "category": "competition_rules",
      "game": "VALORANT",
      "intent": "map_pool"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "accepted",
    "confidence": 0.84,
    "detail": "target-filtered source chunks are preferred over summary fact cards",
    "metadata": {
      "hit_count": 8,
      "validation_errors": [],
      "pause_detail_missing": false
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: ห้ามใช้สกิลในพื้นที่นอกขอบเขตแผนที่ (Out of boundaries) เพื่อหาข้อมูลหรือสร้างความได้เปรียบ

รายละเอียดที่เกี่ยวข้อง:
•    ข้อยกเว้นพิเศษ สกิล ZERO/POINT ของ KAY/O สามารถใช้ภายนอกแผนที่หรือจุดที่ทำลายไม่ได้ได้ แต่ตัวมีดห้ามพุ่งทะลุ Texture ที่ควรจะเป็นของแข็ง

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### valorant-cypher (en)

คำถาม: Under VALORANT tournament rules, may Cypher cameras be invisible or indestructible through map textures?

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:Agent abilities: Cypher cameras must not be placed where they are invisible or indestructible through map-texture clipping., first_line_off_topic

คำตอบก่อนแก้:

```text
Selected VALORANT competition rules from the recorded rulebook:
Tournament: VALORANT / 2026


**Competition equipment**
•    Allowed keyboard technology: Snap Tap, SOCD, or equivalent technologies, unless otherwise instructed by officials.

**Before the match**
•    Personnel: During Match Prep, no more than 6 players may be present.
•    Electronic devices: Mobile phones, tablets, and smartwatches may not be brought into the competition area until the match ends.

**Pauses and timeouts**

**1. Tactical Timeout**
•    2 requests per map during regulation (first 24 rounds), 60 seconds each.
•    In Overtime, each team receives 1 additional timeout. Regulation quotas do not carry over.

**2. Technical Pause**
•    Used when there are device malfunctions, disconnections, or software issues
•    Players must not communicate with each other (either verbally or in text) unless authorized

**3. Player Emergency Pause**
•    One request per map is allowed.
•    Total emergency-pause time may not exceed 10 minutes per match. If that limit is exceeded, the affected player may be unable to continue and must be replaced by a substitute.

**Penalties**
•    Map Forfeit for serious violations or repeated infractions that negatively impact the outcome of a map

This is a summary of selected clauses. Ask about a specific topic for details.
Source: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

เนื้อหาที่ควรปรากฏครบจาก source:

- Agent abilities: Cypher cameras must not be placed where they are invisible or indestructible through map-texture clipping.

Source IDs: competition_rules_valorant_psu_phuket_2026_s09_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "competition_overview",
    "decision": "accepted",
    "confidence": 0.98,
    "detail": "source clauses across sections; headings alone are insufficient",
    "metadata": {
      "section_ids": [
        "competition_rules_valorant_psu_phuket_2026_s01_c01",
        "competition_rules_valorant_psu_phuket_2026_s02_c01",
        "competition_rules_valorant_psu_phuket_2026_s06_c01",
        "competition_rules_valorant_psu_phuket_2026_s07_c01",
        "competition_rules_valorant_psu_phuket_2026_s08_c01",
        "competition_rules_valorant_psu_phuket_2026_s14_c01"
      ],
      "game_ids": [
        "valorant"
      ],
      "validation_errors": []
    }
  }
]
```

คำตอบหลังแก้:

```text
Answer: Agent abilities: Cypher cameras must not be placed where they are invisible or indestructible through map-texture clipping.

Rulebook: VALORANT
Source: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### valorant-boost (th)

คำถาม: กติกา VALORANT ต่อตัวเพื่อนให้กระโดดสูงกว่าปกติได้ไหม

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:การกระโดดต่อตัว ห้ามใช้ตัวละครเพื่อนร่วมทีมเพื่อกระโดดไปยังจุดที่สูงเกินกว่าระยะกระโดดปกติ, first_line_off_topic

คำตอบก่อนแก้:

```text
คำตอบ: การใช้บั๊กที่เกิดจากตัวผู้เล่นเองเพื่อสร้างความได้เปรียบที่ไม่ได้ตั้งใจถือเป็นความผิด

รายละเอียดที่เกี่ยวข้อง:
•    ห้ามวางกล้อง Cypher ในจุดที่มองไม่เห็นหรือทำลายไม่ได้ผ่านการทะลุ Texture ของแผนที่
•    ห้ามใช้สกิลในพื้นที่นอกขอบเขตแผนที่ (Out of boundaries) เพื่อหาข้อมูลหรือสร้างความได้เปรียบ
•    ข้อยกเว้นพิเศษ สกิล ZERO/POINT ของ KAY/O สามารถใช้ภายนอกแผนที่หรือจุดที่ทำลายไม่ได้ได้ แต่ตัวมีดห้ามพุ่งทะลุ Texture ที่ควรจะเป็นของแข็ง

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

เนื้อหาที่ควรปรากฏครบจาก source:

- การกระโดดต่อตัว ห้ามใช้ตัวละครเพื่อนร่วมทีมเพื่อกระโดดไปยังจุดที่สูงเกินกว่าระยะกระโดดปกติ

Source IDs: competition_rules_valorant_psu_phuket_2026_s09_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.9,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "valorant",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "VALORANT",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "valorant"
      ],
      "competition_game_labels": [
        "VALORANT"
      ],
      "competition_rulebook_ids": [
        "competition_rules_valorant_psu_phuket_2026"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "valorant"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=VALORANT intent=-",
    "metadata": {
      "category": "competition_rules",
      "game": "VALORANT",
      "intent": null
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "accepted",
    "confidence": 0.84,
    "detail": "target-filtered source chunks are preferred over summary fact cards",
    "metadata": {
      "hit_count": 8,
      "validation_errors": [],
      "pause_detail_missing": false
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: การกระโดดต่อตัว ห้ามใช้ตัวละครเพื่อนร่วมทีมเพื่อกระโดดไปยังจุดที่สูงเกินกว่าระยะกระโดดปกติ

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### tekken-custom (th)

คำถาม: กติกา Tekken 8 ปรับชุดทรงผมเอฟเฟกต์ตัวละครได้ไหม

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: first_line_off_topic

คำตอบก่อนแก้:

```text
คำตอบ: สามารถเลือก ตัวละครใดก็ได้ (ยกเว้น ตัวละคร DLC)

รายละเอียดที่เกี่ยวข้อง:
•    ห้าม ปรับแต่งตัวละคร ทุกกรณี (เช่น ชุด, ทรงผม, เอฟเฟกต์การต่อสู้, ออร่า ฯลฯ)
•    ห้ามใช้ Bug หรือ Glitch ที่ส่งผลให้เกิดความได้เปรียบ
•    เมื่อเริ่มเกมแล้ว ห้ามหยุดเกม ด้วยเหตุผลใด ๆ
•    อนุญาตให้ใช้ ปุ่ม Assist หรือระบบช่วยเหลือพิเศษ

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports
```

เนื้อหาที่ควรปรากฏครบจาก source:

- ห้าม ปรับแต่งตัวละคร ทุกกรณี (เช่น ชุด, ทรงผม, เอฟเฟกต์การต่อสู้, ออร่า ฯลฯ)

Source IDs: competition_rules_tekken8_psu_esports_s03_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.9,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "tekken8",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "Tekken 8",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "tekken8"
      ],
      "competition_game_labels": [
        "Tekken 8"
      ],
      "competition_rulebook_ids": [
        "competition_rules_tekken8_psu_esports"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "tekken 8"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=Tekken 8 intent=character",
    "metadata": {
      "category": "competition_rules",
      "game": "Tekken 8",
      "intent": "character"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "accepted",
    "confidence": 0.84,
    "detail": "target-filtered source chunks are preferred over summary fact cards",
    "metadata": {
      "hit_count": 8,
      "validation_errors": [],
      "pause_detail_missing": false
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: ห้าม ปรับแต่งตัวละคร ทุกกรณี (เช่น ชุด, ทรงผม, เอฟเฟกต์การต่อสู้, ออร่า ฯลฯ)

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports
```

ผลหลังแก้: ผ่าน

### tekken-glitch (th)

คำถาม: กติกา Tekken 8 ใช้ Bug หรือ Glitch สร้างความได้เปรียบได้ไหม

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: wrong_outcome, missing_complete_clause:ห้ามใช้ Bug หรือ Glitch ที่ส่งผลให้เกิดความได้เปรียบ, first_line_off_topic, wrong_game_source

คำตอบก่อนแก้:

```text
ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
```

เนื้อหาที่ควรปรากฏครบจาก source:

- ห้ามใช้ Bug หรือ Glitch ที่ส่งผลให้เกิดความได้เปรียบ

Source IDs: competition_rules_tekken8_psu_esports_s03_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.9,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "tekken8",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "Tekken 8",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "tekken8"
      ],
      "competition_game_labels": [
        "Tekken 8"
      ],
      "competition_rulebook_ids": [
        "competition_rules_tekken8_psu_esports"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "tekken 8"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=Tekken 8 intent=bug_rule",
    "metadata": {
      "category": "competition_rules",
      "game": "Tekken 8",
      "intent": "bug_rule"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "facet_not_covered_safe_no_answer",
    "confidence": 0.92,
    "detail": "retrieved_source_does_not_prove_requested_facet",
    "metadata": {
      "hit_count": 8,
      "covered": false,
      "facet": "unspecified",
      "target_game_ids": [
        "tekken8"
      ],
      "matched_chunk_ids": [
        "competition_rules_tekken8_psu_esports_s03_c01",
        "competition_rules_tekken8_psu_esports_s02_c01",
        "competition_rules_tekken8_psu_esports_s06_c01",
        "competition_rules_tekken8_psu_esports_s07_c01",
        "competition_rules_tekken8_psu_esports_s08_c01",
        "competition_rules_tekken8_psu_esports_s01_c01",
        "competition_rules_tekken8_psu_esports_s04_c01",
        "competition_rules_tekken8_psu_esports_s05_c01"
      ],
      "reason": "retrieved_source_does_not_prove_requested_facet"
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: ห้ามใช้ Bug หรือ Glitch ที่ส่งผลให้เกิดความได้เปรียบ

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports
```

ผลหลังแก้: ผ่าน

### rov-side (en)

คำถาม: Under RoV tournament rules, which team is blue in game one and who chooses the side in later games?

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:4.1.2. In the first match, the team on the upper side of the bracket will play as the blue team; in the next match, the team that lost the previous match will have the right to choose their side., first_line_off_topic

คำตอบก่อนแก้:

```text
Selected Arena of Valor (RoV) competition rules from the recorded rulebook:
Tournament: Arena of Valor (RoV) / 2025


**Competition format**
•    08:40-10:00: round of 5 teams, Single Elimination BO3
•    10:00-11:30: semifinal match 1, Single Elimination BO3

**Competition equipment**
•    5.3. Tablets, iPads and any devices other than mobile phones may not be used in competition. If detected, staff will immediately impose disqualification.

**Pauses and timeouts**
•    4.3.1. If a participant disconnects during the match, the game will be paused temporarily. Each team may pause the game up to five times, each pause not exceeding one minute. If the time limit is exceeded, the other team may immediately resume the game and continue playing normally.
•    4.5.1.1. If a competitor intentionally disconnects from the game without informing the referee, the referee may deny the pause request.
•    4.5.1.2 In cases where the game is paused due to technical issues, not caused by player actions, the event staff may order a pause and require players to rejoin the game after all disconnected players have reconnected.
•    4.5.2 If the game is paused for more than 10 minutes, the event staff may order a restart of the game, unless one team has a significantly larger score than the other; in such cases, the event staff may use their discretion to declare the higher-scoring team as the winner of the interrupted game.

**Penalties**
•    6.2.4.1. Penalty: If staff verify such violations or receive complaints from others, staff will impose penalties on offending competitors by disqualifying them from the competition.

This is a summary of selected clauses. Ask about a specific topic for details.
Source: local://competition_rules/competition_rules_rov_blueket_2025_men
```

เนื้อหาที่ควรปรากฏครบจาก source:

- 4.1.2. In the first match, the team on the upper side of the bracket will play as the blue team; in the next match, the team that lost the previous match will have the right to choose their side.

Source IDs: competition_rules_rov_blueket_2025_men_s06_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "competition_overview",
    "decision": "accepted",
    "confidence": 0.98,
    "detail": "source clauses across sections; headings alone are insufficient",
    "metadata": {
      "section_ids": [
        "competition_rules_rov_blueket_2025_men_s03_c01",
        "competition_rules_rov_blueket_2025_men_s07_c01",
        "competition_rules_rov_blueket_2025_men_s06_c01",
        "competition_rules_rov_blueket_2025_men_s06_c02",
        "competition_rules_rov_blueket_2025_men_s06_c03",
        "competition_rules_rov_blueket_2025_men_s08_c02"
      ],
      "game_ids": [
        "rov"
      ],
      "validation_errors": []
    }
  }
]
```

คำตอบหลังแก้:

```text
Answer: 4.1.2. In the first match, the team on the upper side of the bracket will play as the blue team; in the next match, the team that lost the previous match will have the right to choose their side.

Rulebook: Arena of Valor (RoV)
Source: local://competition_rules/competition_rules_rov_blueket_2025_men
```

ผลหลังแก้: ผ่าน

### rov-late (th)

คำถาม: กติกา RoV เริ่มแข่งช้าเกิน 15 นาทีเป็นยังไง

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: wrong_outcome, missing_complete_clause:4.1.4.หากเริ่มการแข่งขันช้าเกินกว่าเวลาที่กำหนดไว้ 15 นาที ฝ่ายที่ล่าช้าจะถูกปรับแพ้จากการแข่งขันทันที, first_line_off_topic, wrong_game_source

คำตอบก่อนแก้:

```text
ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
```

เนื้อหาที่ควรปรากฏครบจาก source:

- 4.1.4.หากเริ่มการแข่งขันช้าเกินกว่าเวลาที่กำหนดไว้ 15 นาที ฝ่ายที่ล่าช้าจะถูกปรับแพ้จากการแข่งขันทันที

Source IDs: competition_rules_rov_blueket_2025_men_s06_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.9,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "rov",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "Arena of Valor (RoV)",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "rov"
      ],
      "competition_game_labels": [
        "Arena of Valor (RoV)"
      ],
      "competition_rulebook_ids": [
        "competition_rules_rov_blueket_2025_men"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "rov"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=Arena of Valor (RoV) intent=late_start",
    "metadata": {
      "category": "competition_rules",
      "game": "Arena of Valor (RoV)",
      "intent": "late_start"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "facet_not_covered_safe_no_answer",
    "confidence": 0.92,
    "detail": "retrieved_source_does_not_prove_requested_facet",
    "metadata": {
      "hit_count": 8,
      "covered": false,
      "facet": "unspecified",
      "target_game_ids": [
        "rov"
      ],
      "matched_chunk_ids": [
        "competition_rules_rov_blueket_2025_men_s06_c01",
        "competition_rules_rov_blueket_2025_men_s06_c02",
        "competition_rules_rov_blueket_2025_men_s06_c03",
        "competition_rules_rov_blueket_2025_men_s06_c04",
        "competition_rules_rov_blueket_2025_men_s08_c01",
        "competition_rules_rov_blueket_2025_men_s01_c01",
        "competition_rules_rov_blueket_2025_men_s08_c02",
        "competition_rules_rov_blueket_2025_men_s03_c01"
      ],
      "reason": "retrieved_source_does_not_prove_requested_facet"
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: 4.1.4.หากเริ่มการแข่งขันช้าเกินกว่าเวลาที่กำหนดไว้ 15 นาที ฝ่ายที่ล่าช้าจะถูกปรับแพ้จากการแข่งขันทันที

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men
```

ผลหลังแก้: ผ่าน

### rov-runes (en)

คำถาม: Under RoV tournament rules, are runes and enhancement systems allowed?

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:4.2.3. Runes and enhancement systems may be used as desired., first_line_off_topic

คำตอบก่อนแก้:

```text
Selected Arena of Valor (RoV) competition rules from the recorded rulebook:
Tournament: Arena of Valor (RoV) / 2025


**Competition format**
•    08:40-10:00: round of 5 teams, Single Elimination BO3
•    10:00-11:30: semifinal match 1, Single Elimination BO3

**Competition equipment**
•    5.3. Tablets, iPads and any devices other than mobile phones may not be used in competition. If detected, staff will immediately impose disqualification.

**Pauses and timeouts**
•    4.3.1. If a participant disconnects during the match, the game will be paused temporarily. Each team may pause the game up to five times, each pause not exceeding one minute. If the time limit is exceeded, the other team may immediately resume the game and continue playing normally.
•    4.5.1.1. If a competitor intentionally disconnects from the game without informing the referee, the referee may deny the pause request.
•    4.5.1.2 In cases where the game is paused due to technical issues, not caused by player actions, the event staff may order a pause and require players to rejoin the game after all disconnected players have reconnected.
•    4.5.2 If the game is paused for more than 10 minutes, the event staff may order a restart of the game, unless one team has a significantly larger score than the other; in such cases, the event staff may use their discretion to declare the higher-scoring team as the winner of the interrupted game.

**Penalties**
•    6.2.4.1. Penalty: If staff verify such violations or receive complaints from others, staff will impose penalties on offending competitors by disqualifying them from the competition.

This is a summary of selected clauses. Ask about a specific topic for details.
Source: local://competition_rules/competition_rules_rov_blueket_2025_men
```

เนื้อหาที่ควรปรากฏครบจาก source:

- 4.2.3. Runes and enhancement systems may be used as desired.

Source IDs: competition_rules_rov_blueket_2025_men_s06_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "competition_overview",
    "decision": "accepted",
    "confidence": 0.98,
    "detail": "source clauses across sections; headings alone are insufficient",
    "metadata": {
      "section_ids": [
        "competition_rules_rov_blueket_2025_men_s03_c01",
        "competition_rules_rov_blueket_2025_men_s07_c01",
        "competition_rules_rov_blueket_2025_men_s06_c01",
        "competition_rules_rov_blueket_2025_men_s06_c02",
        "competition_rules_rov_blueket_2025_men_s06_c03",
        "competition_rules_rov_blueket_2025_men_s08_c02"
      ],
      "game_ids": [
        "rov"
      ],
      "validation_errors": []
    }
  }
]
```

คำตอบหลังแก้:

```text
Answer: 4.2.3. Runes and enhancement systems may be used as desired.

Rulebook: Arena of Valor (RoV)
Source: local://competition_rules/competition_rules_rov_blueket_2025_men
```

ผลหลังแก้: ผ่าน

### rov-global (en)

คำถาม: Under RoV tournament rules, what hero ban and pick system is used?

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:4.2.2. Use Global Ban/Pick hero selection., first_line_off_topic

คำตอบก่อนแก้:

```text
Selected Arena of Valor (RoV) competition rules from the recorded rulebook:
Tournament: Arena of Valor (RoV) / 2025


**Competition format**
•    08:40-10:00: round of 5 teams, Single Elimination BO3
•    10:00-11:30: semifinal match 1, Single Elimination BO3

**Competition equipment**
•    5.3. Tablets, iPads and any devices other than mobile phones may not be used in competition. If detected, staff will immediately impose disqualification.

**Pauses and timeouts**
•    4.3.1. If a participant disconnects during the match, the game will be paused temporarily. Each team may pause the game up to five times, each pause not exceeding one minute. If the time limit is exceeded, the other team may immediately resume the game and continue playing normally.
•    4.5.1.1. If a competitor intentionally disconnects from the game without informing the referee, the referee may deny the pause request.
•    4.5.1.2 In cases where the game is paused due to technical issues, not caused by player actions, the event staff may order a pause and require players to rejoin the game after all disconnected players have reconnected.
•    4.5.2 If the game is paused for more than 10 minutes, the event staff may order a restart of the game, unless one team has a significantly larger score than the other; in such cases, the event staff may use their discretion to declare the higher-scoring team as the winner of the interrupted game.

**Penalties**
•    6.2.4.1. Penalty: If staff verify such violations or receive complaints from others, staff will impose penalties on offending competitors by disqualifying them from the competition.

This is a summary of selected clauses. Ask about a specific topic for details.
Source: local://competition_rules/competition_rules_rov_blueket_2025_men
```

เนื้อหาที่ควรปรากฏครบจาก source:

- 4.2.2. Use Global Ban/Pick hero selection.

Source IDs: competition_rules_rov_blueket_2025_men_s06_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "competition_overview",
    "decision": "accepted",
    "confidence": 0.98,
    "detail": "source clauses across sections; headings alone are insufficient",
    "metadata": {
      "section_ids": [
        "competition_rules_rov_blueket_2025_men_s03_c01",
        "competition_rules_rov_blueket_2025_men_s07_c01",
        "competition_rules_rov_blueket_2025_men_s06_c01",
        "competition_rules_rov_blueket_2025_men_s06_c02",
        "competition_rules_rov_blueket_2025_men_s06_c03",
        "competition_rules_rov_blueket_2025_men_s08_c02"
      ],
      "game_ids": [
        "rov"
      ],
      "validation_errors": []
    }
  }
]
```

คำตอบหลังแก้:

```text
Answer: 4.2.2. Use Global Ban/Pick hero selection.

Rulebook: Arena of Valor (RoV)
Source: local://competition_rules/competition_rules_rov_blueket_2025_men
```

ผลหลังแก้: ผ่าน

### rov-force-majeure (en)

คำถาม: Under RoV tournament rules, who decides on a rematch after an area-wide ISP or game server failure?

ชนิด: single / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:4.3.2. If a competitor disconnects because of force majeure (such as an internet-service outage across the area or a game-server error), the affected team must notify the staff. Whether to allow a replay is at the referees' discretion., first_line_off_topic

คำตอบก่อนแก้:

```text
Answer: 4.3.3. If no First Blood has occurred and in-game time has not exceeded 2 minutes, the team whose competitor disconnected may notify the other team and request an immediate restart. Before a restart is requested, every competitor must select the same hero and playing position as in the first game.

Details:
• 4.3.4. Once First Blood has occurred or the game has exceeded 2 minutes, neither team may request a restart unless the opponent permits it and/or the referees consider it appropriate.

Rulebook: Arena of Valor (RoV)
Source: local://competition_rules/competition_rules_rov_blueket_2025_men
```

เนื้อหาที่ควรปรากฏครบจาก source:

- 4.3.2. If a competitor disconnects because of force majeure (such as an internet-service outage across the area or a game-server error), the affected team must notify the staff. Whether to allow a replay is at the referees' discretion.

Source IDs: competition_rules_rov_blueket_2025_men_s06_c02

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "competition_detail",
    "decision": "accepted",
    "confidence": 0.97,
    "detail": "one rulebook, literal complete clauses, no inferred policies",
    "metadata": {
      "concepts": [
        "rematch"
      ],
      "source_ids": [
        "competition_rules_rov_blueket_2025_men_s06_c02"
      ],
      "validation_errors": []
    }
  },
  {
    "stage": "semantic_route",
    "decision": "skipped_exact_competition_facet",
    "confidence": 0.97,
    "detail": "explicit detail propositions already bound to source clauses",
    "metadata": {}
  },
  {
    "stage": "competition_source_grounding",
    "decision": "detail_clauses_covered",
    "confidence": 0.97,
    "detail": "all requested detail concepts have source clauses",
    "metadata": {
      "concepts": [
        "rematch"
      ],
      "source_ids": [
        "competition_rules_rov_blueket_2025_men_s06_c02"
      ]
    }
  }
]
```

คำตอบหลังแก้:

```text
Answer: 4.3.2. If a competitor disconnects because of force majeure (such as an internet-service outage across the area or a game-server error), the affected team must notify the staff. Whether to allow a replay is at the referees' discretion.

Rulebook: Arena of Valor (RoV)
Source: local://competition_rules/competition_rules_rov_blueket_2025_men
```

ผลหลังแก้: ผ่าน

### cs2-macro-install (th)

คำถาม: กติกา CS2 ใช้มาโครได้ไหม แล้วติดตั้งโปรแกรมเองได้ไหม

ชนิด: composite / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด, missing_complete_clause:4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้, first_line_off_topic

คำตอบก่อนแก้:

```text
คำตอบ: 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์

รายละเอียดที่เกี่ยวข้อง:
•    1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้
•    2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

เนื้อหาที่ควรปรากฏครบจาก source:

- 3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด
- 4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้

Source IDs: competition_rules_cs2_psu_phuket_2026_s46_c01, competition_rules_cs2_psu_phuket_2026_s47_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.9,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "cs2",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "Counter-Strike 2",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "cs2"
      ],
      "competition_game_labels": [
        "Counter-Strike 2"
      ],
      "competition_rulebook_ids": [
        "competition_rules_cs2_psu_phuket_2026"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "cs2"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=Counter-Strike 2 intent=equipment",
    "metadata": {
      "category": "competition_rules",
      "game": "Counter-Strike 2",
      "intent": "equipment"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "accepted",
    "confidence": 0.84,
    "detail": "target-filtered source chunks are preferred over summary fact cards",
    "metadata": {
      "hit_count": 8,
      "validation_errors": [],
      "pause_detail_missing": false
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: 3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด

รายละเอียดที่เกี่ยวข้อง:
•    4. ห้ามติดตั้งโปรแกรมเองบนคอมพิวเตอร์ที่จัดไว้ให้

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### cs2-custom-macro (th)

คำถาม: กติกา CS2 ปรับ Brightness Resolution Crosshair ที่ไหน แล้วใช้สคริปต์หรือมาโครได้ไหม

ชนิด: composite / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น, missing_complete_clause:3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด, first_line_off_topic

คำตอบก่อนแก้:

```text
คำตอบ: 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์

รายละเอียดที่เกี่ยวข้อง:
•    1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้
•    2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

เนื้อหาที่ควรปรากฏครบจาก source:

- 1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น
- 3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด

Source IDs: competition_rules_cs2_psu_phuket_2026_s45_c01, competition_rules_cs2_psu_phuket_2026_s46_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.9,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "cs2",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "Counter-Strike 2",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "cs2"
      ],
      "competition_game_labels": [
        "Counter-Strike 2"
      ],
      "competition_rulebook_ids": [
        "competition_rules_cs2_psu_phuket_2026"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "cs2"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=Counter-Strike 2 intent=equipment",
    "metadata": {
      "category": "competition_rules",
      "game": "Counter-Strike 2",
      "intent": "equipment"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "accepted",
    "confidence": 0.84,
    "detail": "target-filtered source chunks are preferred over summary fact cards",
    "metadata": {
      "hit_count": 8,
      "validation_errors": [],
      "pause_detail_missing": false
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: 1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น

รายละเอียดที่เกี่ยวข้อง:
•    3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### cs2-prep-drinks (th)

คำถาม: กติกา CS2 ช่วงเตรียมตัวมีผู้เล่นได้กี่คนและในพื้นที่แข่งกินดื่มอะไรได้บ้าง

ชนิด: composite / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: wrong_outcome, missing_complete_clause:1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน, missing_complete_clause:4. อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น, first_line_off_topic, wrong_game_source

คำตอบก่อนแก้:

```text
ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
```

เนื้อหาที่ควรปรากฏครบจาก source:

- 1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน
- 4. อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น

Source IDs: competition_rules_cs2_psu_phuket_2026_s50_c01, competition_rules_cs2_psu_phuket_2026_s53_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.9,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "cs2",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "Counter-Strike 2",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "cs2"
      ],
      "competition_game_labels": [
        "Counter-Strike 2"
      ],
      "competition_rulebook_ids": [
        "competition_rules_cs2_psu_phuket_2026"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "cs2"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=Counter-Strike 2 intent=area_rules",
    "metadata": {
      "category": "competition_rules",
      "game": "Counter-Strike 2",
      "intent": "area_rules"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "facet_not_covered_safe_no_answer",
    "confidence": 0.92,
    "detail": "retrieved_source_does_not_prove_requested_facet",
    "metadata": {
      "hit_count": 8,
      "covered": false,
      "facet": "unspecified",
      "target_game_ids": [
        "cs2"
      ],
      "matched_chunk_ids": [
        "competition_rules_cs2_psu_phuket_2026_s50_c01",
        "competition_rules_cs2_psu_phuket_2026_s18_c01",
        "competition_rules_cs2_psu_phuket_2026_s23_c01",
        "competition_rules_cs2_psu_phuket_2026_s53_c01",
        "competition_rules_cs2_psu_phuket_2026_s08_c01",
        "competition_rules_cs2_psu_phuket_2026_s38_c01",
        "competition_rules_cs2_psu_phuket_2026_s49_c01",
        "competition_rules_cs2_psu_phuket_2026_s56_c01"
      ],
      "reason": "retrieved_source_does_not_prove_requested_facet"
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: 1. จำนวนบุคลากรในช่วงเตรียมตัว มีผู้เล่นได้ไม่เกิน 6 คน

รายละเอียดที่เกี่ยวข้อง:
•    4. อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### cs2-bug-stream (th)

คำถาม: กติกา CS2 ใช้บัคแผนที่ได้ไหม แล้วดูสตรีมสดระหว่างแข่งได้ไหม

ชนิด: composite / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์, missing_complete_clause:3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง, first_line_off_topic

คำตอบก่อนแก้:

```text
คำตอบ: ดูสตรีมระหว่างแข่ง

รายละเอียดที่เกี่ยวข้อง:
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที
•    หยุดเกมโดยไม่ได้รับอนุญาต
•    ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

เนื้อหาที่ควรปรากฏครบจาก source:

- 2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์
- 3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง

Source IDs: competition_rules_cs2_psu_phuket_2026_s37_c01, competition_rules_cs2_psu_phuket_2026_s38_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.9,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "cs2",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "Counter-Strike 2",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "cs2"
      ],
      "competition_game_labels": [
        "Counter-Strike 2"
      ],
      "competition_rulebook_ids": [
        "competition_rules_cs2_psu_phuket_2026"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "cs2"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=Counter-Strike 2 intent=in_match_operations",
    "metadata": {
      "category": "competition_rules",
      "game": "Counter-Strike 2",
      "intent": "in_match_operations"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "accepted",
    "confidence": 0.84,
    "detail": "target-filtered source chunks are preferred over summary fact cards",
    "metadata": {
      "hit_count": 8,
      "validation_errors": [],
      "pause_detail_missing": false
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: 2. การใช้บัค ห้ามใช้บัคของแผนที่หรือ Engine เกมเด็ดขาด หากฝ่าฝืนจะถูกปรับแพ้ในรอบ/แผนที่นั้น หรือตัดสิทธิ์

รายละเอียดที่เกี่ยวข้อง:
•    3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### cs2-format-mode (th)

คำถาม: กติกา CS2 ใช้รูปแบบคัดออกอะไรและโหมดการแข่งขันอะไร

ชนิด: composite / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:1. รูปแบบทัวร์นาเมนต์ Single Elimination

คำตอบก่อนแก้:

```text
คำตอบ: 1. โหมด Competitive (5v5)

รายละเอียดที่เกี่ยวข้อง:
•    4. การขอเวลานอก ทีมละ 4 ครั้ง ครั้งละ 30 วินาที ใช้ได้ในช่วง Freeze time
•    2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

เนื้อหาที่ควรปรากฏครบจาก source:

- 1. รูปแบบทัวร์นาเมนต์ Single Elimination
- 1. โหมด Competitive (5v5)

Source IDs: competition_rules_cs2_psu_phuket_2026_s20_c01, competition_rules_cs2_psu_phuket_2026_s23_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.9,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "cs2",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "Counter-Strike 2",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "cs2"
      ],
      "competition_game_labels": [
        "Counter-Strike 2"
      ],
      "competition_rulebook_ids": [
        "competition_rules_cs2_psu_phuket_2026"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "cs2"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=Counter-Strike 2 intent=game_setting",
    "metadata": {
      "category": "competition_rules",
      "game": "Counter-Strike 2",
      "intent": "game_setting"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "accepted",
    "confidence": 0.84,
    "detail": "target-filtered source chunks are preferred over summary fact cards",
    "metadata": {
      "hit_count": 8,
      "validation_errors": [],
      "pause_detail_missing": false
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: 1. รูปแบบทัวร์นาเมนต์ Single Elimination

รายละเอียดที่เกี่ยวข้อง:
•    1. โหมด Competitive (5v5)

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### cs2-bracket-authority (th)

คำถาม: กติกา CS2 สายประกาศเมื่อไหร่ มาสายเป็นยังไง และคำตัดสินใครเป็นที่สุด

ชนิด: composite / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:1. อำนาจตัดสิน คำตัดสินของกรรมการ และผู้จัดถือเป็นที่สิ้นสุด ฝ่ายจัดมีสิทธิ์แก้ไขกฎตามความเหมาะสมเพื่อความยุติธรรม

คำตอบก่อนแก้:

```text
คำตอบ: 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์

รายละเอียดที่เกี่ยวข้อง:
•    ตักเตือน → ปรับแพ้ในรอบนั้น → ตัดสิทธิ์
•    ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน
•    ปรับแพ้ในรอบนั้น → ตัดสิทธิ์

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

เนื้อหาที่ควรปรากฏครบจาก source:

- 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์
- 1. อำนาจตัดสิน คำตัดสินของกรรมการ และผู้จัดถือเป็นที่สิ้นสุด ฝ่ายจัดมีสิทธิ์แก้ไขกฎตามความเหมาะสมเพื่อความยุติธรรม

Source IDs: competition_rules_cs2_psu_phuket_2026_s15_c01, competition_rules_cs2_psu_phuket_2026_s57_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.92,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "cs2",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "Counter-Strike 2",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "cs2"
      ],
      "competition_game_labels": [
        "Counter-Strike 2"
      ],
      "competition_rulebook_ids": [
        "competition_rules_cs2_psu_phuket_2026"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "cs2"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=Counter-Strike 2 intent=late_start",
    "metadata": {
      "category": "competition_rules",
      "game": "Counter-Strike 2",
      "intent": "late_start"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "accepted",
    "confidence": 0.84,
    "detail": "target-filtered source chunks are preferred over summary fact cards",
    "metadata": {
      "hit_count": 8,
      "validation_errors": [],
      "pause_detail_missing": false
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: 7. เวลาการแข่งขัน สายการแข่งขันจะประกาศล่วงหน้าอย่างน้อย 1 วัน ต้องยืนยันการเข้าแข่งขันก่อนเริ่มแมตช์ การมาสายอาจถูกตัดสิทธิ์

รายละเอียดที่เกี่ยวข้อง:
•    1. อำนาจตัดสิน คำตัดสินของกรรมการ และผู้จัดถือเป็นที่สิ้นสุด ฝ่ายจัดมีสิทธิ์แก้ไขกฎตามความเหมาะสมเพื่อความยุติธรรม

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### valorant-macro-drinks (th)

คำถาม: กติกา VALORANT ใช้มาโครได้ไหมและกินดื่มอะไรได้ในพื้นที่แข่ง

ชนิด: composite / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: wrong_outcome, missing_complete_clause:ห้ามใช้มาโคร (Macros) ทั้งที่ตั้งค่าผ่านซอฟต์แวร์หรือฮาร์ดแวร์, missing_complete_clause:อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น, first_line_off_topic, wrong_game_source

คำตอบก่อนแก้:

```text
ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
```

เนื้อหาที่ควรปรากฏครบจาก source:

- ห้ามใช้มาโคร (Macros) ทั้งที่ตั้งค่าผ่านซอฟต์แวร์หรือฮาร์ดแวร์
- อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น

Source IDs: competition_rules_valorant_psu_phuket_2026_s01_c01, competition_rules_valorant_psu_phuket_2026_s02_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.9,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "valorant",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "VALORANT",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "valorant"
      ],
      "competition_game_labels": [
        "VALORANT"
      ],
      "competition_rulebook_ids": [
        "competition_rules_valorant_psu_phuket_2026"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "valorant"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.54,
    "detail": "hits=8 game=VALORANT intent=area_rules",
    "metadata": {
      "category": "competition_rules",
      "game": "VALORANT",
      "intent": "area_rules"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "facet_not_covered_safe_no_answer",
    "confidence": 0.92,
    "detail": "retrieved_source_does_not_prove_requested_facet",
    "metadata": {
      "hit_count": 8,
      "covered": false,
      "facet": "unspecified",
      "target_game_ids": [
        "valorant"
      ],
      "matched_chunk_ids": [
        "competition_rules_valorant_psu_phuket_2026_s11_c01",
        "competition_rules_valorant_psu_phuket_2026_s12_c01",
        "competition_rules_valorant_psu_phuket_2026_s02_c01",
        "competition_rules_valorant_psu_phuket_2026_s24_c02",
        "competition_rules_valorant_psu_phuket_2026_s06_c01",
        "competition_rules_valorant_psu_phuket_2026_s01_c01",
        "competition_rules_valorant_psu_phuket_2026_s05_c01",
        "competition_rules_valorant_psu_phuket_2026_s08_c01"
      ],
      "reason": "retrieved_source_does_not_prove_requested_facet"
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: ห้ามใช้มาโคร (Macros) ทั้งที่ตั้งค่าผ่านซอฟต์แวร์หรือฮาร์ดแวร์

รายละเอียดที่เกี่ยวข้อง:
•    อาหารและเครื่องดื่ม อนุญาตเฉพาะน้ำดื่มในภาชนะที่ปิดสนิทและหมากฝรั่งเท่านั้น

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### valorant-cypher-outside (en)

คำถาม: Under VALORANT tournament rules, may Cypher cameras clip through map textures and may abilities be used outside map boundaries?

ชนิด: composite / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:Agent abilities: Cypher cameras must not be placed where they are invisible or indestructible through map-texture clipping., missing_complete_clause:Abilities must not be used outside map boundaries to obtain information or an advantage., missing_complete_clause:Special exception: KAY/O's ZERO/POINT may be used outside the map or in indestructible locations, but the knife must not pass through textures that should be solid., first_line_off_topic

คำตอบก่อนแก้:

```text
Selected VALORANT competition rules from the recorded rulebook:
Tournament: VALORANT / 2026


**Competition equipment**
•    Allowed keyboard technology: Snap Tap, SOCD, or equivalent technologies, unless otherwise instructed by officials.

**Before the match**
•    Personnel: During Match Prep, no more than 6 players may be present.
•    Electronic devices: Mobile phones, tablets, and smartwatches may not be brought into the competition area until the match ends.

**Pauses and timeouts**

**1. Tactical Timeout**
•    2 requests per map during regulation (first 24 rounds), 60 seconds each.
•    In Overtime, each team receives 1 additional timeout. Regulation quotas do not carry over.

**2. Technical Pause**
•    Used when there are device malfunctions, disconnections, or software issues
•    Players must not communicate with each other (either verbally or in text) unless authorized

**3. Player Emergency Pause**
•    One request per map is allowed.
•    Total emergency-pause time may not exceed 10 minutes per match. If that limit is exceeded, the affected player may be unable to continue and must be replaced by a substitute.

**Penalties**
•    Map Forfeit for serious violations or repeated infractions that negatively impact the outcome of a map

This is a summary of selected clauses. Ask about a specific topic for details.
Source: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

เนื้อหาที่ควรปรากฏครบจาก source:

- Agent abilities: Cypher cameras must not be placed where they are invisible or indestructible through map-texture clipping.
- Abilities must not be used outside map boundaries to obtain information or an advantage.
- Special exception: KAY/O's ZERO/POINT may be used outside the map or in indestructible locations, but the knife must not pass through textures that should be solid.

Source IDs: competition_rules_valorant_psu_phuket_2026_s09_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "competition_overview",
    "decision": "accepted",
    "confidence": 0.98,
    "detail": "source clauses across sections; headings alone are insufficient",
    "metadata": {
      "section_ids": [
        "competition_rules_valorant_psu_phuket_2026_s01_c01",
        "competition_rules_valorant_psu_phuket_2026_s02_c01",
        "competition_rules_valorant_psu_phuket_2026_s06_c01",
        "competition_rules_valorant_psu_phuket_2026_s07_c01",
        "competition_rules_valorant_psu_phuket_2026_s08_c01",
        "competition_rules_valorant_psu_phuket_2026_s14_c01"
      ],
      "game_ids": [
        "valorant"
      ],
      "validation_errors": []
    }
  }
]
```

คำตอบหลังแก้:

```text
Answer: Abilities must not be used outside map boundaries to obtain information or an advantage.

Details:
• Special exception: KAY/O's ZERO/POINT may be used outside the map or in indestructible locations, but the knife must not pass through textures that should be solid.
• Agent abilities: Cypher cameras must not be placed where they are invisible or indestructible through map-texture clipping.

Rulebook: VALORANT
Source: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### valorant-prep-timeout (th)

คำถาม: กติกา VALORANT Match Prep มีได้กี่คน และ Tactical Timeout รอบปกติได้กี่ครั้งกี่วินาที

ชนิด: composite / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน

คำตอบก่อนแก้:

```text
คำตอบ: ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที

รายละเอียดที่เกี่ยวข้อง:
•    เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

เนื้อหาที่ควรปรากฏครบจาก source:

- จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน
- ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที

Source IDs: competition_rules_valorant_psu_phuket_2026_s02_c01, competition_rules_valorant_psu_phuket_2026_s06_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped_exact_competition_facet",
    "confidence": 0.97,
    "detail": "one registered game and an explicit rule facet; source coverage remains required",
    "metadata": {
      "game_id": "valorant",
      "competition_facet": "pause_timeout",
      "competition_rulebook_id": "competition_rules_valorant_psu_phuket_2026",
      "answer_coverage_deferred": true
    }
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.97,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "valorant",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "VALORANT",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "valorant"
      ],
      "competition_game_labels": [
        "VALORANT"
      ],
      "competition_rulebook_ids": [
        "competition_rules_valorant_psu_phuket_2026"
      ],
      "competition_facet": "pause_timeout",
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "valorant"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=VALORANT intent=pause",
    "metadata": {
      "category": "competition_rules",
      "game": "VALORANT",
      "intent": "pause"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "target_facet_source_index",
    "confidence": 0.98,
    "detail": "hits=8 facet=pause_timeout",
    "metadata": {
      "facet": "pause_timeout",
      "target_game_ids": [
        "valorant"
      ],
      "rulebook_ids": [
        "competition_rules_valorant_psu_phuket_2026"
      ],
      "hit_ids": [
        "competition_rules_valorant_psu_phuket_2026_s06_c01",
        "competition_rules_valorant_psu_phuket_2026_s08_c01",
        "competition_rules_valorant_psu_phuket_2026_s07_c01",
        "competition_rules_valorant_psu_phuket_2026_s05_c01",
        "competition_rules_valorant_psu_phuket_2026_s21_c01",
        "competition_rules_valorant_psu_phuket_2026_s23_c01",
        "competition_rules_valorant_psu_phuket_2026_s20_c01",
        "competition_rules_valorant_psu_phuket_2026_s22_c01"
      ]
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "accepted",
    "confidence": 0.84,
    "detail": "target-filtered source chunks are preferred over summary fact cards",
    "metadata": {
      "hit_count": 2,
      "validation_errors": [],
      "pause_detail_missing": false
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: จำนวนบุคลากร ในช่วงเตรียมตัว (Match Prep) มีผู้เล่นได้ไม่เกิน 6 คน

รายละเอียดที่เกี่ยวข้อง:
•    ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### tekken-custom-glitch (th)

คำถาม: กติกา Tekken 8 ปรับชุดทรงผมตัวละครได้ไหม แล้วใช้ Bug Glitch ได้ไหม

ชนิด: composite / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: wrong_outcome, missing_complete_clause:ห้าม ปรับแต่งตัวละคร ทุกกรณี (เช่น ชุด, ทรงผม, เอฟเฟกต์การต่อสู้, ออร่า ฯลฯ), missing_complete_clause:ห้ามใช้ Bug หรือ Glitch ที่ส่งผลให้เกิดความได้เปรียบ, first_line_off_topic, wrong_game_source

คำตอบก่อนแก้:

```text
ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
```

เนื้อหาที่ควรปรากฏครบจาก source:

- ห้าม ปรับแต่งตัวละคร ทุกกรณี (เช่น ชุด, ทรงผม, เอฟเฟกต์การต่อสู้, ออร่า ฯลฯ)
- ห้ามใช้ Bug หรือ Glitch ที่ส่งผลให้เกิดความได้เปรียบ

Source IDs: competition_rules_tekken8_psu_esports_s03_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.9,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "tekken8",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "Tekken 8",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "tekken8"
      ],
      "competition_game_labels": [
        "Tekken 8"
      ],
      "competition_rulebook_ids": [
        "competition_rules_tekken8_psu_esports"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "tekken 8"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=Tekken 8 intent=bug_rule",
    "metadata": {
      "category": "competition_rules",
      "game": "Tekken 8",
      "intent": "bug_rule"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "facet_not_covered_safe_no_answer",
    "confidence": 0.92,
    "detail": "retrieved_source_does_not_prove_requested_facet",
    "metadata": {
      "hit_count": 8,
      "covered": false,
      "facet": "unspecified",
      "target_game_ids": [
        "tekken8"
      ],
      "matched_chunk_ids": [
        "competition_rules_tekken8_psu_esports_s03_c01",
        "competition_rules_tekken8_psu_esports_s02_c01",
        "competition_rules_tekken8_psu_esports_s06_c01",
        "competition_rules_tekken8_psu_esports_s07_c01",
        "competition_rules_tekken8_psu_esports_s08_c01",
        "competition_rules_tekken8_psu_esports_s01_c01",
        "competition_rules_tekken8_psu_esports_s04_c01",
        "competition_rules_tekken8_psu_esports_s05_c01"
      ],
      "reason": "retrieved_source_does_not_prove_requested_facet"
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: ห้ามใช้ Bug หรือ Glitch ที่ส่งผลให้เกิดความได้เปรียบ

รายละเอียดที่เกี่ยวข้อง:
•    ห้าม ปรับแต่งตัวละคร ทุกกรณี (เช่น ชุด, ทรงผม, เอฟเฟกต์การต่อสู้, ออร่า ฯลฯ)

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports
```

ผลหลังแก้: ผ่าน

### rov-side-global (th)

คำถาม: กติกา RoV เกมแรกใครอยู่สีฟ้าและเกมต่อไปใครเลือกฝั่ง แล้วแบนเลือกฮีโร่แบบไหน

ชนิด: composite / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:4.2.2.ใช้การแบนและเลือกฮีโร่แบบ Global Ban/Pick

คำตอบก่อนแก้:

```text
คำตอบ: 4.1.2.ในเกมแรก ทีมที่อยู่ทางด้านบนของสายการแข่งขันจะได้อยู่ฝ่ายสีน้ำเงิน และในเกมถัดไป ผู้ที่แพ้ในเกมก่อนหน้าจะได้สิทธิ์ในการเลือกฝั่ง

รายละเอียดที่เกี่ยวข้อง:
•    4.2.1.ผู้เข้าแข่งขันทุกคนต้องมีฮีโร่อย่างน้อย 18 ตัว สำหรับการเข้าแข่งขันในโหมด “การแข่งขัน 5v5” (ชื่อเดิม Tournament Mode)

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men
```

เนื้อหาที่ควรปรากฏครบจาก source:

- 4.1.2.ในเกมแรก ทีมที่อยู่ทางด้านบนของสายการแข่งขันจะได้อยู่ฝ่ายสีน้ำเงิน และในเกมถัดไป ผู้ที่แพ้ในเกมก่อนหน้าจะได้สิทธิ์ในการเลือกฝั่ง
- 4.2.2.ใช้การแบนและเลือกฮีโร่แบบ Global Ban/Pick

Source IDs: competition_rules_rov_blueket_2025_men_s06_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.9,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "rov",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "Arena of Valor (RoV)",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "rov"
      ],
      "competition_game_labels": [
        "Arena of Valor (RoV)"
      ],
      "competition_rulebook_ids": [
        "competition_rules_rov_blueket_2025_men"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "rov"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=Arena of Valor (RoV) intent=side_selection",
    "metadata": {
      "category": "competition_rules",
      "game": "Arena of Valor (RoV)",
      "intent": "side_selection"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "accepted",
    "confidence": 0.84,
    "detail": "target-filtered source chunks are preferred over summary fact cards",
    "metadata": {
      "hit_count": 8,
      "validation_errors": [],
      "pause_detail_missing": false
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: 4.1.2.ในเกมแรก ทีมที่อยู่ทางด้านบนของสายการแข่งขันจะได้อยู่ฝ่ายสีน้ำเงิน และในเกมถัดไป ผู้ที่แพ้ในเกมก่อนหน้าจะได้สิทธิ์ในการเลือกฝั่ง

รายละเอียดที่เกี่ยวข้อง:
•    4.2.2.ใช้การแบนและเลือกฮีโร่แบบ Global Ban/Pick

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men
```

ผลหลังแก้: ผ่าน

### rov-runes-late (th)

คำถาม: กติกา RoV ใช้รูนได้ไหม แล้วเริ่มช้าเกิน 15 นาทีเป็นยังไง

ชนิด: composite / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: wrong_outcome, missing_complete_clause:4.2.3.สามารถใส่รูนและระบบพลังเสริมได้ตามความต้องการ, missing_complete_clause:4.1.4.หากเริ่มการแข่งขันช้าเกินกว่าเวลาที่กำหนดไว้ 15 นาที ฝ่ายที่ล่าช้าจะถูกปรับแพ้จากการแข่งขันทันที, first_line_off_topic, wrong_game_source

คำตอบก่อนแก้:

```text
ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
```

เนื้อหาที่ควรปรากฏครบจาก source:

- 4.2.3.สามารถใส่รูนและระบบพลังเสริมได้ตามความต้องการ
- 4.1.4.หากเริ่มการแข่งขันช้าเกินกว่าเวลาที่กำหนดไว้ 15 นาที ฝ่ายที่ล่าช้าจะถูกปรับแพ้จากการแข่งขันทันที

Source IDs: competition_rules_rov_blueket_2025_men_s06_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.9,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "rov",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "Arena of Valor (RoV)",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "rov"
      ],
      "competition_game_labels": [
        "Arena of Valor (RoV)"
      ],
      "competition_rulebook_ids": [
        "competition_rules_rov_blueket_2025_men"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "rov"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=Arena of Valor (RoV) intent=late_start",
    "metadata": {
      "category": "competition_rules",
      "game": "Arena of Valor (RoV)",
      "intent": "late_start"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "facet_not_covered_safe_no_answer",
    "confidence": 0.92,
    "detail": "retrieved_source_does_not_prove_requested_facet",
    "metadata": {
      "hit_count": 8,
      "covered": false,
      "facet": "unspecified",
      "target_game_ids": [
        "rov"
      ],
      "matched_chunk_ids": [
        "competition_rules_rov_blueket_2025_men_s06_c02",
        "competition_rules_rov_blueket_2025_men_s06_c03",
        "competition_rules_rov_blueket_2025_men_s06_c01",
        "competition_rules_rov_blueket_2025_men_s06_c04",
        "competition_rules_rov_blueket_2025_men_s08_c01",
        "competition_rules_rov_blueket_2025_men_s08_c02",
        "competition_rules_rov_blueket_2025_men_s01_c01",
        "competition_rules_rov_blueket_2025_men_s04_c01"
      ],
      "reason": "retrieved_source_does_not_prove_requested_facet"
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: 4.1.4.หากเริ่มการแข่งขันช้าเกินกว่าเวลาที่กำหนดไว้ 15 นาที ฝ่ายที่ล่าช้าจะถูกปรับแพ้จากการแข่งขันทันที

รายละเอียดที่เกี่ยวข้อง:
•    4.2.3.สามารถใส่รูนและระบบพลังเสริมได้ตามความต้องการ

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men
```

ผลหลังแก้: ผ่าน

### fee (th)

คำถาม: กติกา CS2 ค่าสมัครกี่บาท

ชนิด: control / ผลที่ควรเป็น: no_answer

เกณฑ์ที่ขาด: wrong_outcome:answer

คำตอบก่อนแก้:

```text
คำตอบ: 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร

รายละเอียดที่เกี่ยวข้อง:
•    1. มารยาทผู้เล่น ห้ามพฤติกรรมก้าวร้าว วาจาสร้างความเกลียดชัง (เหยียดเชื้อชาติ/ศาสนา) และการกระทำที่ไม่มีน้ำใจนักกีฬา
•    3. การดูสตรีม ห้ามผู้เล่นดูสตรีมสดระหว่างแข่ง

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.93,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "cs2",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "Counter-Strike 2",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "cs2"
      ],
      "competition_game_labels": [
        "Counter-Strike 2"
      ],
      "competition_rulebook_ids": [
        "competition_rules_cs2_psu_phuket_2026"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "cs2"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=Counter-Strike 2 intent=registration",
    "metadata": {
      "category": "competition_rules",
      "game": "Counter-Strike 2",
      "intent": "registration"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "accepted",
    "confidence": 0.84,
    "detail": "target-filtered source chunks are preferred over summary fact cards",
    "metadata": {
      "hit_count": 8,
      "validation_errors": [],
      "pause_detail_missing": false
    }
  }
]
```

คำตอบหลังแก้:

```text
ยังไม่พบข้อมูลค่าสมัครการแข่งขันในเอกสารของเกมนี้ครับ
```

ผลหลังแก้: ผ่าน

### fee-multi (th)

คำถาม: กติกา CS2 ใช้สคริปต์ได้ไหมและค่าสมัครกี่บาท

ชนิด: control / ผลที่ควรเป็น: safe_unknown_fee

เกณฑ์ที่ขาด: silently_omitted_unknown_fee

คำตอบก่อนแก้:

```text
คำตอบ: 2. ไม่อนุญาตให้ลงทะเบียนผู้เล่น หลังจากปิดรับสมัคร

รายละเอียดที่เกี่ยวข้อง:
•    1. มารยาทผู้เล่น ห้ามพฤติกรรมก้าวร้าว วาจาสร้างความเกลียดชัง (เหยียดเชื้อชาติ/ศาสนา) และการกระทำที่ไม่มีน้ำใจนักกีฬา
•    3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped",
    "confidence": 0.0,
    "detail": "semantic retrieval disabled",
    "metadata": {}
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.93,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "cs2",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "Counter-Strike 2",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "cs2"
      ],
      "competition_game_labels": [
        "Counter-Strike 2"
      ],
      "competition_rulebook_ids": [
        "competition_rules_cs2_psu_phuket_2026"
      ],
      "competition_facet": null,
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "cs2"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=Counter-Strike 2 intent=registration",
    "metadata": {
      "category": "competition_rules",
      "game": "Counter-Strike 2",
      "intent": "registration"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "skipped",
    "confidence": 1.0,
    "detail": "target or canonical facet is unresolved",
    "metadata": {
      "facet": null,
      "target_status": "exact"
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "accepted",
    "confidence": 0.84,
    "detail": "target-filtered source chunks are preferred over summary fact cards",
    "metadata": {
      "hit_count": 8,
      "validation_errors": [],
      "pause_detail_missing": false
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: 3. ห้ามใช้สคริปต์ หรือมาโคร โดยเด็ดขาด

ประเด็นที่ยังไม่พบข้อมูล: ยังไม่พบข้อมูลค่าสมัครการแข่งขันในเอกสารของเกมนี้ครับ
อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### pause-conflict (en)

คำถาม: May I pause under Tekken 8 tournament rules?

ชนิด: control / ผลที่ควรเป็น: conflict

เกณฑ์ที่ขาด: missing_conflict_notice

คำตอบก่อนแก้:

```text
Answer: The game may be paused only when all players agree and there is a valid reason, such as equipment malfunction or an emergency.

Details:
• Pausing the game without necessity will result in the same penalty as leaving the game prematurely.
• Once the game starts, no game pausing for any reason is permitted
• Any intentional game pause will result in a penalty of losing one round immediately

Rulebook: Tekken 8
Source: local://competition_rules/competition_rules_tekken8_psu_esports
```

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "bilingual_route",
    "decision": "pipeline:structured_competition_rules_en",
    "confidence": 0.94,
    "detail": "English competition localization overlay matched current Thai source hashes",
    "metadata": {
      "effective_locale": "en",
      "route_category": "competition_rules",
      "route_intent": "competition_rule_lookup",
      "runtime_translation": false
    }
  }
]
```

คำตอบหลังแก้:

```text
Answer: The recorded pause clauses conflict. The organizer must confirm the exception conditions and penalty level before a definite ruling can be given.

Details:
• Once the game starts, no game pausing for any reason is permitted
• The game may be paused only when all players agree and there is a valid reason, such as equipment malfunction or an emergency.
• Any intentional game pause will result in a penalty of losing one round immediately
• Pausing the game without necessity will result in the same penalty as leaving the game prematurely.

Rulebook: Tekken 8
Source: local://competition_rules/competition_rules_tekken8_psu_esports
```

ผลหลังแก้: ผ่าน

### clipped-rov (th)

คำถาม: กติกา RoV ข้อ 6.1.5.1 บทลงโทษเต็มว่าอะไร

ชนิด: control / ผลที่ควรเป็น: no_answer

เกณฑ์ที่ขาด: wrong_outcome:answer

คำตอบก่อนแก้:

```text
คำตอบ: 6.1.2.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันทีและตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที

รายละเอียดที่เกี่ยวข้อง:
•    6.1.3.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันทีและตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที
•    6.1.4.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันทีและตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที
•    6.1.5.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันทีและตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจาก
•    6.1.1.1. บทลงโทษ: ปรับแพ้ในเกมที่พบการกระทำผิดในทันที

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men
```

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "semantic_route_refiner",
    "decision": "skipped_exact_competition_facet",
    "confidence": 0.97,
    "detail": "one registered game and an explicit rule facet; source coverage remains required",
    "metadata": {
      "game_id": "rov",
      "competition_facet": "penalty",
      "competition_rulebook_id": "competition_rules_rov_blueket_2025_men",
      "answer_coverage_deferred": true
    }
  },
  {
    "stage": "router",
    "decision": "competition_rules",
    "confidence": 0.97,
    "detail": "competition rule terms found before reservation/check-in",
    "metadata": {
      "intent": "competition_rules_lookup",
      "answer_type": "fact"
    }
  },
  {
    "stage": "tool_router",
    "decision": "heuristic:retrieval",
    "confidence": 0.97,
    "detail": "experimental_allow_llm is false",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false
    }
  },
  {
    "stage": "operation_route_refine",
    "decision": "competition_rules/competition_rules_lookup -> competition_rules/competition_rules_lookup",
    "confidence": 0.97,
    "detail": "question frame supplied a clear PSU operation domain",
    "metadata": {
      "operation": "competition_rule_lookup",
      "domain": "competition_rules",
      "expected_answer_types": [
        "competition_rule"
      ],
      "targets": [
        {
          "target_id": "rov",
          "target_type": "competition_game",
          "domain": "competition_rules",
          "label": "Arena of Valor (RoV)",
          "score": 1.0
        }
      ],
      "target_status": "exact",
      "target_margin": 1.0,
      "target_required": true,
      "allows_multiple_targets": false,
      "needs_clarification": false,
      "confidence": 0.97,
      "method": "competition_target_first",
      "route_category": "competition_rules",
      "route_intent": "competition_rules_lookup",
      "intent_operation": "rule_lookup",
      "competition_game_ids": [
        "rov"
      ],
      "competition_game_labels": [
        "Arena of Valor (RoV)"
      ],
      "competition_rulebook_ids": [
        "competition_rules_rov_blueket_2025_men"
      ],
      "competition_facet": "penalty",
      "competition_target_reason": "registered_competition_alias",
      "competition_explicit_mentions": [
        "rov"
      ],
      "target_reason": "registered_competition_alias",
      "target_candidate_count": 1,
      "game_family": ""
    }
  },
  {
    "stage": "rag_retrieval",
    "decision": "curated_lexical",
    "confidence": 0.84,
    "detail": "hits=8 game=Arena of Valor (RoV) intent=penalty",
    "metadata": {
      "category": "competition_rules",
      "game": "Arena of Valor (RoV)",
      "intent": "penalty"
    }
  },
  {
    "stage": "competition_contract_retrieval",
    "decision": "target_facet_source_index",
    "confidence": 0.98,
    "detail": "hits=2 facet=penalty",
    "metadata": {
      "facet": "penalty",
      "target_game_ids": [
        "rov"
      ],
      "rulebook_ids": [
        "competition_rules_rov_blueket_2025_men"
      ],
      "hit_ids": [
        "competition_rules_rov_blueket_2025_men_s08_c01",
        "competition_rules_rov_blueket_2025_men_s08_c02"
      ]
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "accepted",
    "confidence": 0.84,
    "detail": "target-filtered source chunks are preferred over summary fact cards",
    "metadata": {
      "hit_count": 2,
      "validation_errors": [],
      "pause_detail_missing": false
    }
  }
]
```

คำตอบหลังแก้:

```text
ยังไม่พบข้อความฉบับเต็มที่ยืนยันได้สำหรับข้อ 6.1.5.1 เพราะต้นฉบับจบไม่ครบ ต้องขอเอกสารฉบับเต็มจากผู้จัดครับ
```

ผลหลังแก้: ผ่าน

### money-regular-overtime (th)

คำถาม: กติกา CS2 เงินเริ่มต้นและเวลาระเบิดรอบปกติเท่าไร แล้วต่อเวลามีกี่รอบและเงินเริ่มต้นเท่าไร

ชนิด: composite / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:3. เงินเริ่มต้น $800 | เวลาของระเบิด: 40 วินาที

คำตอบก่อนแก้:

```text
คำตอบ: 5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

เนื้อหาที่ควรปรากฏครบจาก source:

- 3. เงินเริ่มต้น $800 | เวลาของระเบิด: 40 วินาที
- 5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง

Source IDs: competition_rules_cs2_psu_phuket_2026_s25_c01, competition_rules_cs2_psu_phuket_2026_s27_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "competition_detail",
    "decision": "accepted",
    "confidence": 0.97,
    "detail": "one rulebook, literal complete clauses, no inferred policies",
    "metadata": {
      "concepts": [
        "overtime"
      ],
      "source_ids": [
        "competition_rules_cs2_psu_phuket_2026_s27_c01"
      ],
      "validation_errors": []
    }
  },
  {
    "stage": "semantic_route",
    "decision": "skipped_exact_competition_facet",
    "confidence": 0.97,
    "detail": "explicit detail propositions already bound to source clauses",
    "metadata": {}
  },
  {
    "stage": "competition_source_grounding",
    "decision": "detail_clauses_covered",
    "confidence": 0.97,
    "detail": "all requested detail concepts have source clauses",
    "metadata": {
      "concepts": [
        "overtime"
      ],
      "source_ids": [
        "competition_rules_cs2_psu_phuket_2026_s27_c01"
      ]
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: 3. เงินเริ่มต้น $800 | เวลาของระเบิด: 40 วินาที

รายละเอียดที่เกี่ยวข้อง:
•    5. การต่อเวลา ฝั่งละ 3 รอบ (รวม 6) ใครได้ 4 ใน 6 รอบก่อนชนะ เงินเริ่มต้น $10,000 ต่อเวลาไม่จำกัดจำนวนครั้ง

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### language-protest (th)

คำถาม: กติกา CS2 ประท้วงใช้ภาษาอะไร ใครยื่นและภายในกี่นาที

ชนิด: composite / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น

คำตอบก่อนแก้:

```text
คำตอบ: 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

เนื้อหาที่ควรปรากฏครบจาก source:

- 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น
- 2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น

Source IDs: competition_rules_cs2_psu_phuket_2026_s06_c01, competition_rules_cs2_psu_phuket_2026_s58_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "competition_detail",
    "decision": "accepted",
    "confidence": 0.97,
    "detail": "one rulebook, literal complete clauses, no inferred policies",
    "metadata": {
      "concepts": [
        "language"
      ],
      "source_ids": [
        "competition_rules_cs2_psu_phuket_2026_s06_c01"
      ],
      "validation_errors": []
    }
  },
  {
    "stage": "semantic_route",
    "decision": "skipped_exact_competition_facet",
    "confidence": 0.97,
    "detail": "explicit detail propositions already bound to source clauses",
    "metadata": {}
  },
  {
    "stage": "competition_source_grounding",
    "decision": "detail_clauses_covered",
    "confidence": 0.97,
    "detail": "all requested detail concepts have source clauses",
    "metadata": {
      "concepts": [
        "language"
      ],
      "source_ids": [
        "competition_rules_cs2_psu_phuket_2026_s06_c01"
      ]
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: 3. ภาษา ภาษาทางการของการแข่งขันคือ ภาษาไทย การสื่อสาร การประท้วง และการรายงานผลทั้งหมดต้องใช้ภาษาไทย เว้นแต่จะระบุไว้เป็นอย่างอื่น

รายละเอียดที่เกี่ยวข้อง:
•    2. การประท้วง ต้องยื่นเรื่องภายใน 15 นาทีหลังจากจบแมตช์ โดยกัปตันทีมหรือโค้ชเท่านั้น

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### gear-bring-quality (th)

คำถาม: กติกา CS2 นำอุปกรณ์ของตัวเองอะไรมาได้ แล้วใครรับผิดชอบคุณภาพและความพร้อมของอุปกรณ์

ชนิด: composite / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง

คำตอบก่อนแก้:

```text
คำตอบ: 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

เนื้อหาที่ควรปรากฏครบจาก source:

- 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้
- 2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง

Source IDs: competition_rules_cs2_psu_phuket_2026_s41_c01, competition_rules_cs2_psu_phuket_2026_s42_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "competition_detail",
    "decision": "accepted",
    "confidence": 0.97,
    "detail": "one rulebook, literal complete clauses, no inferred policies",
    "metadata": {
      "concepts": [
        "own_equipment"
      ],
      "source_ids": [
        "competition_rules_cs2_psu_phuket_2026_s41_c01"
      ],
      "validation_errors": []
    }
  },
  {
    "stage": "semantic_route",
    "decision": "skipped_exact_competition_facet",
    "confidence": 0.97,
    "detail": "explicit detail propositions already bound to source clauses",
    "metadata": {}
  },
  {
    "stage": "competition_source_grounding",
    "decision": "detail_clauses_covered",
    "confidence": 0.97,
    "detail": "all requested detail concepts have source clauses",
    "metadata": {
      "concepts": [
        "own_equipment"
      ],
      "source_ids": [
        "competition_rules_cs2_psu_phuket_2026_s41_c01"
      ]
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้

รายละเอียดที่เกี่ยวข้อง:
•    2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

### maps-pool-tool (th)

คำถาม: กติกา CS2 ใช้แผนที่อะไรบ้าง แล้วเลือกแผนที่ผ่านเว็บอะไร

ชนิด: composite / ผลที่ควรเป็น: answer

เกณฑ์ที่ขาด: missing_complete_clause:1. ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN

คำตอบก่อนแก้:

```text
คำตอบ: 1. การเลือกแผนที่ ใช้ MAPBAN.GG

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

เนื้อหาที่ควรปรากฏครบจาก source:

- 1. ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN
- 1. การเลือกแผนที่ ใช้ MAPBAN.GG

Source IDs: competition_rules_cs2_psu_phuket_2026_s29_c01, competition_rules_cs2_psu_phuket_2026_s31_c01

Trace ที่เกี่ยวข้อง:

```json
[
  {
    "stage": "competition_detail",
    "decision": "accepted",
    "confidence": 0.97,
    "detail": "one rulebook, literal complete clauses, no inferred policies",
    "metadata": {
      "concepts": [
        "map_tool"
      ],
      "source_ids": [
        "competition_rules_cs2_psu_phuket_2026_s31_c01"
      ],
      "validation_errors": []
    }
  },
  {
    "stage": "semantic_route",
    "decision": "skipped_exact_competition_facet",
    "confidence": 0.97,
    "detail": "explicit detail propositions already bound to source clauses",
    "metadata": {}
  },
  {
    "stage": "competition_source_grounding",
    "decision": "detail_clauses_covered",
    "confidence": 0.97,
    "detail": "all requested detail concepts have source clauses",
    "metadata": {
      "concepts": [
        "map_tool"
      ],
      "source_ids": [
        "competition_rules_cs2_psu_phuket_2026_s31_c01"
      ]
    }
  }
]
```

คำตอบหลังแก้:

```text
คำตอบ: 1. ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN

รายละเอียดที่เกี่ยวข้อง:
•    1. การเลือกแผนที่ ใช้ MAPBAN.GG

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

ผลหลังแก้: ผ่าน

## ขอบเขตและสิ่งที่ยังไม่ยืนยัน

- 280 ข้อนี้ตรวจ 28 ประเด็นเดี่ยว, 16 คู่ประเด็น, 8 controls ต่อภาษา. ไทย/อังกฤษมี clean, คำสุภาพ และ task typo; ไม่ได้พิสูจน์ typo ทุกคำหรือทุกคำถามหลายเรื่อง.
- คำถามหลายเกม,หลายข้อที่ระบุเลข,เงื่อนไขมากกว่าสองส่วน และรายละเอียดที่ยังไม่มีตัวจับ ต้องทดสอบเพิ่มจาก log ผู้ใช้จริง. กรณี missing age ปัจจุบันยังตอบ no-answer ตาม guard เดิมเมื่อคำถามมี age ร่วมกับ eligibility.
- การอ่านเลข/ราคาในอนาคตมีขอบเขต: parser ยังต้องมีตัวเลขชัดเจน ไม่ได้ยืนยันเงื่อนไขทุกแบบของค่าธรรมเนียม waived/free. source ปัจจุบันไม่มีราคาเหล่านี้.
- ค่า 0.97 ไม่ใช่คะแนนความถูกต้องจริง; complete-clause pass ก็ไม่ใช่ owner approval ของนโยบายหรือผลเทียบผู้ตัดสิน.
- Tekken pause, RoV 6.1.5–6.1.5.1 และ V2 104 ต้องให้ผู้จัดส่งข้อมูล/ยืนยัน. รูปแบบจอย, นโยบายภาพ, ชื่ออังกฤษทางการยังเป็น owner pending; booking oracle เก็บภายหลังตามคำสั่งผู้ใช้.
- ชุด Gold 2,000 มีเกณฑ์ legacy และ source-grade ที่ต้องอ่านแยก ไม่ใช้ source-grade เป็น semantic correctness ทั้งชุด.
