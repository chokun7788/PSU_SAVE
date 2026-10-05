# วิเคราะห์ r27: สาเหตุ คำตอบที่ควรได้ และการแก้

หลักฐานอยู่ใน `C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data\reports\r27_competition_contract_20261001_211252_b0bf95`

## ระดับของผล

- 2,000 ข้อ: route/status/evidence/source presence; ไม่ใช่ตรวจทุก proposition ทุกคำตอบ
- 320 ข้อ: 104 ประเด็นไทย/อังกฤษ ×3 รูปคำถาม +8 controls; literal clause completeness และ first line
- 128 ข้อ: 16 ประเด็น ×2 ภาษา ×4 รูปแบบใหม่/พิมพ์เบิ้ล/ผิดหลายส่วน/พิมพ์ขาด เป็น development cases หลังตรวจแล้ว ไม่ใช่ blind field data
- ข้อกำหนดที่ผู้จัดไม่ได้รับรองแยกจากผลอัตโนมัติ

## ลำดับแก้ตามความรุนแรง

| ระดับ | ปัญหา | ตัวอย่าง | สาเหตุ | วิธีแก้ |
| --- | --- | --- | --- | --- |
| P0 | เลือกข้อกฎย่อยไม่ตรงคำถาม | devices, notes, own/provided equipment, hero/skin, roster change | facet กว้างกับคำว่า game/team/equipment มีคะแนน แต่ไม่ได้แยก proposition; guard จึงอาจยอมรับเรื่องข้างเคียงหรือปฏิเสธว่าไม่มีข้อมูล | เลือก clause จาก rulebook เดียวตามแนวคิดย่อย และตรวจ source hash สำหรับอังกฤษ |
| P0 | ตัดเงื่อนไขและรายการไม่ครบ | RoV rematch/overheating/long pause, VALORANT rollback, Tekken settings | window และจำนวน clause ที่แสดงมีขีดจำกัด; ข้อห้าม/เว้นแต่/Stage/Advantage ถูกตัดจากท้ายแม้เอกสารมี | รักษา clause เต็มและรับทุก clause ที่ผูกกับ proposition; test ต้องตรวจทุกเงื่อนไขและหน่วย |
| P0 | การแก้คำเปลี่ยนคำที่ถูกเป็นความหมายอื่น | score → scope | บริบท tournament ทำให้ scope เป็นผู้สมัครของ edit distance แต่ score ไม่อยู่ในรายการคำจริงที่ป้องกันไว้ | ป้องกัน score/scores และทดสอบคำจริง scope, ชื่อเกม ตัวเลข และ negation |
| P1 | ประโยคแรกไม่ตรง แม้รายละเอียดมีคำตอบ | overtime timeout, source scope, notes, heroes | เรียงจาก chunk/heading หรือค่าแรกของ subtype ไม่ได้เรียงจาก proposition ที่ถาม | first-line contract แยกจากการมีเนื้อหาที่ส่วน Details |
| P1 | คำสำคัญพิมพ์ขาดแล้วไม่ได้เข้า facet | ประท้วง/โน้ต/โซเชียล/ฮีโร่, protest/notes/heroes/settings/score | ตัวกู้คำเดิมเน้น task vocabulary จึงกู้ tournament ได้แต่ไม่กู้ proposition word; fallback กลายเป็น overview หรือข้ออื่น | OSA edit distance 1 พร้อม registered game และ independent syntax/context anchor; จำกัด span/edit budget เดิม ไม่มี whole-question alias |
| P1 | worker เปลี่ยนทุก 250 คำถามทำให้ 503 | HTTP candidate และ sequential จบไม่ครบ | Start-PSU-Esports-Chatbot.ps1 ตั้ง recycle=250, queue wait=3s; supervisor ฆ่าตัวเดิมและเริ่มตัวใหม่ทันที ก่อน ready จึงไม่มี worker รับงาน ไม่ใช่ข้อกฎผิด | เตรียม replacement ขณะตัวเดิมยังทำงาน สลับหลัง ready; cleanup spare เมื่อ failure/shutdown และไม่รับ stale slot |
| P2 | Grader เก่าปฏิเสธ clause อังกฤษสั้น | 30 Tekken equipment +17 VALORANT penalty | กรองเฉพาะ modal/ตัวเลขและ window 7 tokens; 5-token PS5 clause กับ penalty definitions บางข้อไม่ผ่าน | atomic complete-clause presence; คงคะแนนดิบและ gates อื่น; completeness แยกใช้ fixture |
| P2 | คำถามไม่ระบุเกมเสียเวลาผ่านโมเดลก่อนถามกลับ | TH/EN tournament rules without target | การตรวจ target เดิมอยู่หลัง semantic/intent route; การถามกลับไม่ต้องเรียกโมเดลเหล่านี้ | ย้าย guard มาไว้หลัง preprocess/explicit competition signal ก่อนโมเดล; ไม่เรียก RAG หรือ booking เพื่อเดาเกม |

## คะแนนและเหตุที่เลือกคำตอบ

- ค่า confidence 0.97 ของเส้นทางใหม่หมายถึงการตัดสินเส้นทางแบบขอบเขตจำกัด ไม่ใช่โอกาส 97% ที่ทุกข้อกฎถูก
- เส้นทางใหม่ต้องเป็นเกมเดียวที่ลงทะเบียนและมี competition signal; คำถามไม่รู้จักยังผ่าน pipeline เดิม
- แนวคิดย่อยใช้คำทั่วไปของหัวข้อ (ไม่ใช้ ID คำถามหรือข้อความ Gold) จับ clause เต็มใน source; ถ้าหลาย chunk มีข้อความตรง เลือก chunk ที่รองรับ clause ในแนวคิดนั้นมากกว่า
- เนื้อหาคำตอบไม่ได้สร้างจากคะแนนหรือจาก LLM: ใช้ต้นฉบับหรือ English overlay ที่ hash ผ่าน พร้อม source ID ใน trace
- รูปแบบเดิมมี retrieval/facet score แต่ source heading และหัวข้อกว้างไม่ได้พิสูจน์ proposition เช่น time allowance กับ pause reason
- การรวม eligibility/roster/registration ต้องรวมทุกเรื่องที่ถาม; full run A จับ regression นี้และแก้ก่อน run B

## Oracle ที่ตรวจแก้เอง

- เก็บ fixture v1 กับผลดิบไว้; v2 แยก numbered clause ที่ไม่มีจุดท้ายออกจาก heading ให้ถูก
- EN check-in/new content/emergency มีคำแปลหลาย chunk ที่มีความหมายเทียบกันได้; การไม่ตรง literal ใน v1 ไม่ใช่หลักฐาน semantic wrong ทุกเคส
- ไม่แก้ Gold เดิมเพื่อเพิ่มคะแนน: กรณี 47 fails ใช้ source-presence grade อีกช่อง

## หลักฐานต่อประเด็นที่ baseline ไม่ผ่าน

### cs2-scope-en

**คำถาม:** Who does the CS2 rulebook apply to?

**คำตอบเดิม:**
```text
Answer: PSU Phuket CS2 2026 Tournament

Details:
• Scope of Application This regulation applies to all players, teams, and staff members participating officially in any CS2 competition organized by PSU Esports Studio - Phuket.
• The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- Scope of Application This regulation applies to all players, teams, and staff members participating officially in any CS2 competition organized by PSU Esports Studio - Phuket.

อ้างอิง `competition_rules_cs2_psu_phuket_2026_s04_c01`; source hash `80114f6fde3b5244569ffb7850f8f177337a9a318ed44914186af5c718fc6c6d`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### cs2-version-en

**คำถาม:** Which game version do the CS2 tournament rules use?

**คำตอบเดิม:**
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

**ข้อที่ตัวตรวจรายงาน:** first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- The competition will use the latest version of CS2 on the Steam platform. Unauthorized modifications to the game are strictly prohibited.

อ้างอิง `competition_rules_cs2_psu_phuket_2026_s05_c01`; source hash `ba967cd89a88ae836d050f8abbe816aa69c3d04c09bfdcc02cc1433a9ba54210`

**เหตุการณ์จาก trace:**
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

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### cs2-roster-change-th

**คำถาม:** กติกา CS2 เปลี่ยนสมาชิกทีมระหว่างแข่งได้ไหม

**คำตอบเดิม:**
```text
คำตอบ: ดูสตรีมระหว่างแข่ง

รายละเอียดที่เกี่ยวข้อง:
•    3. การหยุดเกมทางเทคนิค ทีมละ 2 ครั้ง ครั้งละไม่เกิน 10 นาที หากพบปัญหาต้องรีบแจ้งกรรมการทันที
•    หยุดเกมโดยไม่ได้รับอนุญาต
•    ปรับแพ้ในรอบนั้น / ตัดสิทธิ์จากการแข่งขัน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- 1. ต้องไม่มีการเปลี่ยนแปลงสมาชิกในทีมตลอดระยะเวลาการแข่งขัน

อ้างอิง `competition_rules_cs2_psu_phuket_2026_s11_c01`; source hash `8c80933db5870bb4ec86b703a8b8321cca6f7cd692820433bacf32ab0b811a2f`

**เหตุการณ์จาก trace:**
```json
[
  {
    "stage": "universal_intent",
    "decision": "competition_rules/rule_lookup",
    "confidence": 0.9,
    "detail": "domain_terms=3; competition route overrides game/count ambiguity; rule terms found; competition route forces rule lookup",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false,
      "llm_first": false,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {},
      "intent_risk_flags": [
        "competing_domain_signals",
        "people_or_role_signal_conflicts_with_domain"
      ],
      "input_recovery": {
        "score": 0.1115,
        "language": "mixed",
        "language_quality": 0.8885,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.889",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "competition_rules",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        },
        {
          "id": "c3",
          "domain": "members",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        },
        {
          "id": "c4",
          "domain": "games",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [
        "lookup_competition_rule"
      ],
      "answer_style": "direct",
      "heuristic": {
        "domain": "competition_rules",
        "operation": "rule_lookup",
        "confidence": 0.9,
        "reason": "domain_terms=3; competition route overrides game/count ambiguity; rule terms found; competition route forces rule lookup"
      }
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

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### cs2-roster-change-en

**คำถาม:** Can CS2 tournament teams change members during the event?

**คำตอบเดิม:**
```text
Answer: Scope of Application This regulation applies to all players, teams, and staff members participating officially in any CS2 competition organized by PSU Esports Studio - Phuket.

Details:
• No team member changes are allowed during the competition period
• Technical game pauses allowed per team: two times, each not exceeding 10 minutes. If issues arise, teams must immediately notify the referees.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- No team member changes are allowed during the competition period

อ้างอิง `competition_rules_cs2_psu_phuket_2026_s11_c01`; source hash `8c80933db5870bb4ec86b703a8b8321cca6f7cd692820433bacf32ab0b811a2f`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### cs2-one-team-th

**คำถาม:** กติกา CS2 ผู้เล่นลงได้กี่ทีม

**คำตอบเดิม:**
```text
คำตอบ: 2. องค์ประกอบทีม แต่ละทีมประกอบด้วยผู้เล่น 5 คน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- 4. ผู้เล่นสามารถลงแข่งในนามของทีมได้ทีมเดียวเท่านั้น

อ้างอิง `competition_rules_cs2_psu_phuket_2026_s14_c01`; source hash `70397e8766f670250215c8ecd5e313130b39aeda90d082e5c18c61c45fabd667`

**เหตุการณ์จาก trace:**
```json
[
  {
    "stage": "universal_intent",
    "decision": "competition_rules/rule_lookup",
    "confidence": 0.9,
    "detail": "domain_terms=3; competition route overrides game/count ambiguity; rule terms found; competition route forces rule lookup",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false,
      "llm_first": false,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {},
      "intent_risk_flags": [
        "competing_domain_signals"
      ],
      "input_recovery": {
        "score": 0.1626,
        "language": "mixed",
        "language_quality": 0.8374,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.837",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "competition_rules",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "competition_rules",
          "operation": "count",
          "target": "",
          "confidence": 0.97,
          "reason": "router category candidate"
        },
        {
          "id": "c3",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        },
        {
          "id": "c4",
          "domain": "games",
          "operation": "count",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [
        "lookup_competition_rule"
      ],
      "answer_style": "direct",
      "heuristic": {
        "domain": "competition_rules",
        "operation": "rule_lookup",
        "confidence": 0.9,
        "reason": "domain_terms=3; competition route overrides game/count ambiguity; rule terms found; competition route forces rule lookup"
      }
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

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### cs2-eligibility-en

**คำถาม:** Who is eligible to register for the CS2 tournament?

**คำตอบเดิม:**
```text
Answer: Registration of players is not permitted after the registration period has closed.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- General eligibility: Open only to students currently enrolled at Prince of Songkla University, Phuket Campus.

อ้างอิง `competition_rules_cs2_psu_phuket_2026_s17_c01`; source hash `f4e9682157dee0ebab12248f2c3523189e2aaf9e51e1be010b1e795ab100cf1d`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### cs2-money-bomb-en

**คำถาม:** What are starting money and bomb time in the CS2 tournament?

**คำตอบเดิม:**
```text
I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
```

**ข้อที่ตัวตรวจรายงาน:** outcome_mismatch, missing_complete_clause, first_line_off_topic, wrong_game_evidence

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- Initial money: $800 | Bomb time: 40 seconds

อ้างอิง `competition_rules_cs2_psu_phuket_2026_s25_c01`; source hash `a067fdf5bfb6523fe9f699bba90b621043a0ff3b1d3684c40c5a104175ec46c8`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### cs2-maps-th

**คำถาม:** กติกา CS2 ใช้แผนที่อะไรบ้าง

**คำตอบเดิม:**
```text
คำตอบ: 1. การเลือกแผนที่ ใช้ MAPBAN.GG

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- 1. ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN

อ้างอิง `competition_rules_cs2_psu_phuket_2026_s29_c01`; source hash `ccc38b2b2e1565a6c6b166892f74b035bf75c1968fad122bd170e0f74f95da2d`

**เหตุการณ์จาก trace:**
```json
[
  {
    "stage": "universal_intent",
    "decision": "competition_rules/rule_lookup",
    "confidence": 0.97,
    "detail": "one registered game and an explicit rule facet; source coverage remains required",
    "metadata": {
      "method": "competition_target_first",
      "llm_attempted": false,
      "target": "cs2",
      "filters": {
        "competition_facet": "map_pool",
        "competition_rulebook_id": "competition_rules_cs2_psu_phuket_2026"
      },
      "answer_coverage_deferred": true
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

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### cs2-maps-en

**คำถาม:** Which maps are in the CS2 tournament map pool?

**คำตอบเดิม:**
```text
Answer: Map selection uses MAPBAN.GG

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- 1. ANCIENT, ANUBIS, DUST 2, INFERNO, MIRAGE, NUKE, TRAIN

อ้างอิง `competition_rules_cs2_psu_phuket_2026_s29_c01`; source hash `ccc38b2b2e1565a6c6b166892f74b035bf75c1968fad122bd170e0f74f95da2d`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### cs2-tactical-en

**คำถาม:** How many tactical timeouts are allowed and when can they be used in the CS2 tournament?

**คำตอบเดิม:**
```text
Verified Counter-Strike 2 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live.
Original source in Thai: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** outcome_mismatch, missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- Tactical timeouts: 4 per team, 30 seconds each, available during Freeze time.

อ้างอิง `competition_rules_cs2_psu_phuket_2026_s34_c01`; source hash `3e86c57a164675158ddcf0d58b78e6a108bd74abedd97a4bb03a7757a849f8e1`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### cs2-own-gear-th

**คำถาม:** กติกา CS2 นำอุปกรณ์ของตัวเองอะไรมาได้บ้าง

**คำตอบเดิม:**
```text
คำตอบ: 2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- 1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้

อ้างอิง `competition_rules_cs2_psu_phuket_2026_s41_c01`; source hash `60f584178fc7e234dfa11ede15e4ddc0ad9c8dda7509d3619ad7fb521c8d97ae`

**เหตุการณ์จาก trace:**
```json
[
  {
    "stage": "universal_intent",
    "decision": "competition_rules/rule_lookup",
    "confidence": 0.97,
    "detail": "one registered game and an explicit rule facet; source coverage remains required",
    "metadata": {
      "method": "competition_target_first",
      "llm_attempted": false,
      "target": "cs2",
      "filters": {
        "competition_facet": "equipment",
        "competition_rulebook_id": "competition_rules_cs2_psu_phuket_2026"
      },
      "answer_coverage_deferred": true
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "accepted",
    "confidence": 0.84,
    "detail": "target-filtered source chunks are preferred over summary fact cards",
    "metadata": {
      "hit_count": 5,
      "validation_errors": [],
      "pause_detail_missing": false
    }
  }
]
```

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### cs2-provided-th

**คำถาม:** กติกา CS2 ผู้จัดเตรียมอุปกรณ์อะไรให้

**คำตอบเดิม:**
```text
คำตอบ: 2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- 3. ผู้จัดจะจัดเตรียม PC, จอภาพ, หูฟังพร้อมไมโครโฟน, โต๊ะ และเก้าอี้ให้

อ้างอิง `competition_rules_cs2_psu_phuket_2026_s43_c01`; source hash `75d79cae19236490edfb47bb5ab9f59b2a447bf31a9060e3ca085ae481ad2974`

**เหตุการณ์จาก trace:**
```json
[
  {
    "stage": "universal_intent",
    "decision": "competition_rules/rule_lookup",
    "confidence": 0.97,
    "detail": "one registered game and an explicit rule facet; source coverage remains required",
    "metadata": {
      "method": "competition_target_first",
      "llm_attempted": false,
      "target": "cs2",
      "filters": {
        "competition_facet": "equipment",
        "competition_rulebook_id": "competition_rules_cs2_psu_phuket_2026"
      },
      "answer_coverage_deferred": true
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "accepted",
    "confidence": 0.84,
    "detail": "target-filtered source chunks are preferred over summary fact cards",
    "metadata": {
      "hit_count": 5,
      "validation_errors": [],
      "pause_detail_missing": false
    }
  }
]
```

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### cs2-provided-en

**คำถาม:** What equipment do CS2 tournament organizers provide?

**คำตอบเดิม:**
```text
Answer: Permitted Equipment

Details:
• Players may bring their own keyboard (wired or wireless), mouse (wired or wireless), mouse cord holder (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.
• Mobile phones, tablets, or smartwatches are prohibited in the competition area until the match concludes.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- The organizers will prepare PCs, monitors, headphones with microphones, tables, and chairs.

อ้างอิง `competition_rules_cs2_psu_phuket_2026_s43_c01`; source hash `75d79cae19236490edfb47bb5ab9f59b2a447bf31a9060e3ca085ae481ad2974`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### cs2-social-exception-th

**คำถาม:** กติกา CS2 เข้าโซเชียลบนเครื่องแข่งได้ไหม

**คำตอบเดิม:**
```text
คำตอบ: 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์

รายละเอียดที่เกี่ยวข้อง:
•    1. ผู้เล่นสามารถนำคีย์บอร์ด (มีสาย/ไร้สาย), เมาส์(มีสาย/ไร้สาย), ตัวยึดสายเมาส์ (mouse bungee), แผ่นรองเมาส์ หูฟังแบบ In-ear (มีสาย), Headset (มีสาย) มาเองได้
•    2. ผู้เล่นต้องรับผิดชอบต่อคุณภาพ และความพร้อมใช้งานของอุปกรณ์ตนเอง

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- 5. ห้ามเข้าโซเชียลมีเดียหรือเว็บไซต์สื่อสารใด ๆ บนคอมพิวเตอร์แข่งขันนอกจากโปรแกรมที่ทางผู้จัดจัดเตรียมไว้ให้

อ้างอิง `competition_rules_cs2_psu_phuket_2026_s48_c01`; source hash `f5456082703d2b72c1aeadfff149c1a32e3b5b9bafc4bfa74f1e749b7779fa70`

**เหตุการณ์จาก trace:**
```json
[
  {
    "stage": "universal_intent",
    "decision": "competition_rules/rule_lookup",
    "confidence": 0.9,
    "detail": "domain_terms=3; competition route overrides game/count ambiguity; rule terms found; competition route forces rule lookup",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false,
      "llm_first": false,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {},
      "intent_risk_flags": [
        "competing_domain_signals"
      ],
      "input_recovery": {
        "score": 0.1487,
        "language": "mixed",
        "language_quality": 0.8513,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.851",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "competition_rules",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        },
        {
          "id": "c3",
          "domain": "games",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        },
        {
          "id": "c4",
          "domain": "equipment",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [
        "lookup_competition_rule"
      ],
      "answer_style": "direct",
      "heuristic": {
        "domain": "competition_rules",
        "operation": "rule_lookup",
        "confidence": 0.9,
        "reason": "domain_terms=3; competition route overrides game/count ambiguity; rule terms found; competition route forces rule lookup"
      }
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

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### cs2-devices-th

**คำถาม:** กติกา CS2 นำโทรศัพท์เข้าเขตแข่งได้ไหม

**คำตอบเดิม:**
```text
ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
```

**ข้อที่ตัวตรวจรายงาน:** outcome_mismatch, missing_complete_clause, first_line_off_topic, wrong_game_evidence

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- 2. ห้ามนำโทรศัพท์มือถือ แท็บเล็ต หรือสมาร์ทวอทช์ เข้าไปในพื้นที่แข่ง จนกว่าจะจบแมตช์

อ้างอิง `competition_rules_cs2_psu_phuket_2026_s51_c01`; source hash `c63a83dc1dc90386ce5524180c505e363e7e170dbac25bb5b7120c3b3a6510f0`

**เหตุการณ์จาก trace:**
```json
[
  {
    "stage": "universal_intent",
    "decision": "competition_rules/rule_lookup",
    "confidence": 0.9,
    "detail": "domain_terms=3; competition route overrides game/count ambiguity; rule terms found; competition route forces rule lookup",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false,
      "llm_first": false,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {},
      "intent_risk_flags": [
        "competing_domain_signals"
      ],
      "input_recovery": {
        "score": 0.1861,
        "language": "mixed",
        "language_quality": 0.8139,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.814",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "competition_rules",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        },
        {
          "id": "c3",
          "domain": "games",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        },
        {
          "id": "c4",
          "domain": "contact",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [
        "lookup_competition_rule"
      ],
      "answer_style": "direct",
      "heuristic": {
        "domain": "competition_rules",
        "operation": "rule_lookup",
        "confidence": 0.9,
        "reason": "domain_terms=3; competition route overrides game/count ambiguity; rule terms found; competition route forces rule lookup"
      }
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
        "competition_rules_cs2_psu_phuket_2026_s51_c01",
        "competition_rules_cs2_psu_phuket_2026_s08_c01",
        "competition_rules_cs2_psu_phuket_2026_s04_c01",
        "competition_rules_cs2_psu_phuket_2026_s52_c01",
        "competition_rules_cs2_psu_phuket_2026_s38_c01",
        "competition_rules_cs2_psu_phuket_2026_s50_c01",
        "competition_rules_cs2_psu_phuket_2026_s49_c01",
        "competition_rules_cs2_psu_phuket_2026_s01_c01"
      ],
      "reason": "retrieved_source_does_not_prove_requested_facet"
    }
  }
]
```

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### cs2-devices-en

**คำถาม:** Can players bring phones into the CS2 tournament area?

**คำตอบเดิม:**
```text
Answer: Players are not allowed to bring notes or documents into the arena, but team leaders may bring them in and must hand them to the referees before every match.

Details:
• Players may bring their own keyboard (wired or wireless), mouse (wired or wireless), mouse cord holder (mouse bungee), mouse pad, wired in-ear headphones, and wired headset.
• Mobile phones, tablets, or smartwatches are prohibited in the competition area until the match concludes.

Rulebook: Counter-Strike 2
Source: local://competition_rules/competition_rules_cs2_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- Mobile phones, tablets, or smartwatches are prohibited in the competition area until the match concludes.

อ้างอิง `competition_rules_cs2_psu_phuket_2026_s51_c01`; source hash `c63a83dc1dc90386ce5524180c505e363e7e170dbac25bb5b7120c3b3a6510f0`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### cs2-notes-th

**คำถาม:** กติกา CS2 ใครนำโน้ตเข้าแข่งได้และต้องส่งให้ใคร

**คำตอบเดิม:**
```text
ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
```

**ข้อที่ตัวตรวจรายงาน:** outcome_mismatch, missing_complete_clause, first_line_off_topic, wrong_game_evidence

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- 3. ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง

อ้างอิง `competition_rules_cs2_psu_phuket_2026_s52_c01`; source hash `5b56fcd859dee25143fe2219804ba2d24f7d0ea4a41174e1f848edfe8892dd01`

**เหตุการณ์จาก trace:**
```json
[
  {
    "stage": "universal_intent",
    "decision": "competition_rules/rule_lookup",
    "confidence": 0.9,
    "detail": "domain_terms=3; competition route overrides game/count ambiguity; rule terms found; competition route forces rule lookup",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false,
      "llm_first": false,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {},
      "intent_risk_flags": [
        "competing_domain_signals",
        "people_or_role_signal_conflicts_with_domain"
      ],
      "input_recovery": {
        "score": 0.2305,
        "language": "mixed",
        "language_quality": 0.7695,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.769",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "competition_rules",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        },
        {
          "id": "c3",
          "domain": "games",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [
        "lookup_competition_rule"
      ],
      "answer_style": "direct",
      "heuristic": {
        "domain": "competition_rules",
        "operation": "rule_lookup",
        "confidence": 0.9,
        "reason": "domain_terms=3; competition route overrides game/count ambiguity; rule terms found; competition route forces rule lookup"
      }
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
        "competition_rules_cs2_psu_phuket_2026_s52_c01",
        "competition_rules_cs2_psu_phuket_2026_s15_c01",
        "competition_rules_cs2_psu_phuket_2026_s04_c01",
        "competition_rules_cs2_psu_phuket_2026_s51_c01",
        "competition_rules_cs2_psu_phuket_2026_s06_c01",
        "competition_rules_cs2_psu_phuket_2026_s09_c01",
        "competition_rules_cs2_psu_phuket_2026_s43_c01",
        "competition_rules_cs2_psu_phuket_2026_s49_c01"
      ],
      "reason": "retrieved_source_does_not_prove_requested_facet"
    }
  }
]
```

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### rov-format-th

**คำถาม:** กติกา RoV รูปแบบการแข่งขันเป็นอย่างไร

**คำตอบเดิม:**
```text
คำตอบ: 3.2. แข่ง Best of 3 (BO3) ทุกรอบ

รายละเอียดที่เกี่ยวข้อง:
•    เวลา 8.40-10.00 รอบ 5 ทีม แข่งแบบ Single Elimination BO3
•    เวลา 10.00-11.30 รอบรองชนะเลิศ คู่ที่ 1 แข่งแบบ Single Elimination BO3
•    เวลา 12.30-14.00 รอบรองชนะเลิศ คู่ที่ 2 แข่งแบบ Single Elimination BO3
•    เวลา 14.00-15.30 รอบชิงอันดับที่ 3 แข่งแบบ Single Elimination BO3
•    เวลา 15.30-17.00 รอบชิงชนะเลิศ แข่งแบบ Single Elimination BO3

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- 3.1. แข่งแบบออฟไลน์
- 3.2. แข่ง Best of 3 (BO3) ทุกรอบ

อ้างอิง `competition_rules_rov_blueket_2025_men_s05_c01`; source hash `dc3f6e3f0d769b3951f496c7064772367bc3d3144bb9a0f8f0813a6e59c12248`

**เหตุการณ์จาก trace:**
```json
[
  {
    "stage": "universal_intent",
    "decision": "competition_rules/rule_lookup",
    "confidence": 0.97,
    "detail": "one registered game and an explicit rule facet; source coverage remains required",
    "metadata": {
      "method": "competition_target_first",
      "llm_attempted": false,
      "target": "rov",
      "filters": {
        "competition_facet": "competition_format",
        "competition_rulebook_id": "competition_rules_rov_blueket_2025_men"
      },
      "answer_coverage_deferred": true
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "accepted",
    "confidence": 0.84,
    "detail": "target-filtered source chunks are preferred over summary fact cards",
    "metadata": {
      "hit_count": 6,
      "validation_errors": [],
      "pause_detail_missing": false
    }
  }
]
```

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### rov-format-en

**คำถาม:** What is the RoV tournament format?

**คำตอบเดิม:**
```text
Answer: Competition Rules 4. Regulations and Competition Rules

Details:
• 4.1.1. Prohibited to use character names or phrases that are offensive or disrespectful toward others.
• 4.1.3. The referees will announce the room number so both teams can enter the designated room.
• 08:40-10:00: round of 5 teams, Single Elimination BO3
• 10:00-11:30: semifinal match 1, Single Elimination BO3
• 12:30-14:00: semifinal match 2, Single Elimination BO3
• 3.2. Each round played as Best of 3 (BO3)

Rulebook: Arena of Valor (RoV)
Source: local://competition_rules/competition_rules_rov_blueket_2025_men
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- 3.1. Offline Mode
- 3.2. Each round played as Best of 3 (BO3)

อ้างอิง `competition_rules_rov_blueket_2025_men_s05_c01`; source hash `dc3f6e3f0d769b3951f496c7064772367bc3d3144bb9a0f8f0813a6e59c12248`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### rov-heroes-th

**คำถาม:** กติกา RoV ต้องมีฮีโร่อย่างน้อยกี่ตัว

**คำตอบเดิม:**
```text
ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
```

**ข้อที่ตัวตรวจรายงาน:** outcome_mismatch, missing_complete_clause, first_line_off_topic, wrong_game_evidence

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- 4.2.1.ผู้เข้าแข่งขันทุกคนต้องมีฮีโร่อย่างน้อย 18 ตัว สำหรับการเข้าแข่งขันในโหมด “การแข่งขัน 5v5” (ชื่อเดิม Tournament Mode)

อ้างอิง `competition_rules_rov_blueket_2025_men_s06_c01`; source hash `13680e662a0fff83acfe8826d260397d13a87b82d772b861b2b58de7f1fc5a92`

**เหตุการณ์จาก trace:**
```json
[
  {
    "stage": "universal_intent",
    "decision": "competition_rules/rule_lookup",
    "confidence": 0.9,
    "detail": "domain_terms=3; competition route overrides game/count ambiguity; rule terms found; competition route forces rule lookup",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false,
      "llm_first": false,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {},
      "intent_risk_flags": [
        "competing_domain_signals"
      ],
      "input_recovery": {
        "score": 0.1483,
        "language": "mixed",
        "language_quality": 0.8517,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.852",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "competition_rules",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "competition_rules",
          "operation": "count",
          "target": "",
          "confidence": 0.97,
          "reason": "router category candidate"
        },
        {
          "id": "c3",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        },
        {
          "id": "c4",
          "domain": "games",
          "operation": "count",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [
        "lookup_competition_rule"
      ],
      "answer_style": "direct",
      "heuristic": {
        "domain": "competition_rules",
        "operation": "rule_lookup",
        "confidence": 0.9,
        "reason": "domain_terms=3; competition route overrides game/count ambiguity; rule terms found; competition route forces rule lookup"
      }
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
        "competition_rules_rov_blueket_2025_men_s06_c03",
        "competition_rules_rov_blueket_2025_men_s06_c02",
        "competition_rules_rov_blueket_2025_men_s06_c04",
        "competition_rules_rov_blueket_2025_men_s01_c01",
        "competition_rules_rov_blueket_2025_men_s08_c01",
        "competition_rules_rov_blueket_2025_men_s04_c01",
        "competition_rules_rov_blueket_2025_men_s03_c01"
      ],
      "reason": "retrieved_source_does_not_prove_requested_facet"
    }
  }
]
```

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### rov-heroes-en

**คำถาม:** How many heroes must a RoV tournament participant own?

**คำตอบเดิม:**
```text
Answer: Competition Rules 4. Regulations and Competition Rules

Details:
• 4.1.1. Prohibited to use character names or phrases that are offensive or disrespectful toward others.
• 4.1.3. The referees will announce the room number so both teams can enter the designated room.
• 4.3.2. If a competitor disconnects because of force majeure (such as an internet-service outage across the area or a game-server error), the affected team must notify the staff. Whether to allow a replay is at the referees' discretion.
• 4.3.3. If no First Blood has occurred and in-game time has not exceeded 2 minutes, the team whose competitor disconnected may notify the other team and request an immediate restart. Before a restart is requested, every competitor must select the same hero and playing position as in the first game.
• 4.3.4. Once First Blood has occurred or the game has exceeded 2 minutes, neither team may request a restart unless the opponent permits it and/or the referees consider it appropriate.
• 4.5.1.2 In cases where the game is paused due to technical issues, not caused by player actions, the event staff may order a pause and require players to rejoin the game after all disconnected players have reconnected.
• 4.5.2 If the game is paused for more than 10 minutes, the event staff may order a restart of the game, unless one team has a significantly larger score than the other; in such cases, the event staff may use their discretion to declare the higher-scoring team as the winner of the interrupted game.
• 4.5.3 After reconnection, the event staff may order both competing teams to immediately restart the game and/or continue playing anew, as they deem appropriate.

Rulebook: Arena of Valor (RoV)
Source: local://competition_rules/competition_rules_rov_blueket_2025_men
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- 4.2.1. All participants must have at least 18 heroes for the "5v5" mode (formerly known as Tournament Mode).

อ้างอิง `competition_rules_rov_blueket_2025_men_s06_c01`; source hash `13680e662a0fff83acfe8826d260397d13a87b82d772b861b2b58de7f1fc5a92`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### rov-skin-th

**คำถาม:** กติกา RoV ใช้สกินอะไรได้บ้าง

**คำตอบเดิม:**
```text
ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
```

**ข้อที่ตัวตรวจรายงาน:** outcome_mismatch, missing_complete_clause, first_line_off_topic, wrong_game_evidence

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- 4.2.5.ในส่วนของสกิน ห้ามใช้สกินนอกจากสกิน Default เท่านั้น

อ้างอิง `competition_rules_rov_blueket_2025_men_s06_c01`; source hash `13680e662a0fff83acfe8826d260397d13a87b82d772b861b2b58de7f1fc5a92`

**เหตุการณ์จาก trace:**
```json
[
  {
    "stage": "universal_intent",
    "decision": "competition_rules/rule_lookup",
    "confidence": 0.9,
    "detail": "domain_terms=3; competition route overrides game/count ambiguity; rule terms found; competition route forces rule lookup",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false,
      "llm_first": false,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {},
      "intent_risk_flags": [
        "competing_domain_signals"
      ],
      "input_recovery": {
        "score": 0.1257,
        "language": "mixed",
        "language_quality": 0.8743,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.874",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "competition_rules",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "competition_rules",
          "operation": "list",
          "target": "",
          "confidence": 0.97,
          "reason": "router category candidate"
        },
        {
          "id": "c3",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [
        "lookup_competition_rule"
      ],
      "answer_style": "direct",
      "heuristic": {
        "domain": "competition_rules",
        "operation": "rule_lookup",
        "confidence": 0.9,
        "reason": "domain_terms=3; competition route overrides game/count ambiguity; rule terms found; competition route forces rule lookup"
      }
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
        "competition_rules_rov_blueket_2025_men_s06_c03",
        "competition_rules_rov_blueket_2025_men_s06_c02",
        "competition_rules_rov_blueket_2025_men_s01_c01",
        "competition_rules_rov_blueket_2025_men_s06_c04",
        "competition_rules_rov_blueket_2025_men_s04_c01",
        "competition_rules_rov_blueket_2025_men_s08_c01",
        "competition_rules_rov_blueket_2025_men_s08_c02"
      ],
      "reason": "retrieved_source_does_not_prove_requested_facet"
    }
  }
]
```

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### rov-skin-en

**คำถาม:** Which skins may be used in the RoV tournament?

**คำตอบเดิม:**
```text
I could not find a verified rule section for that specific topic in this game's rulebook, so I will not substitute a different rule.
```

**ข้อที่ตัวตรวจรายงาน:** outcome_mismatch, missing_complete_clause, first_line_off_topic, wrong_game_evidence

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- 4.2.5. Regarding skins, only Default skins may be used.

อ้างอิง `competition_rules_rov_blueket_2025_men_s06_c01`; source hash `13680e662a0fff83acfe8826d260397d13a87b82d772b861b2b58de7f1fc5a92`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### rov-disconnect-quota-en

**คำถาม:** How many pauses and minutes are allowed for a disconnect in the RoV tournament?

**คำตอบเดิม:**
```text
Answer: 4.5.1.1. If a competitor intentionally disconnects from the game without informing the referee, the referee may deny the pause request.

Details:
• 4.5.1.2 In cases where the game is paused due to technical issues, not caused by player actions, the event staff may order a pause and require players to rejoin the game after all disconnected players have reconnected.
• 4.5.2 If the game is paused for more than 10 minutes, the event staff may order a restart of the game, unless one team has a significantly larger score than the other; in such cases, the event staff may use their discretion to declare the higher-scoring team as the winner of the interrupted game.
• 4.5.4 The referee may pause the game for any reason.
• 4.6. Player injuries, illnesses, or physical issues are not acceptable grounds for a competitor to pause gameplay.
• 4.6.1.1 The staff may order a game pause of no more than 5 minutes to cool down the device if they determine that the device's temperature will cause frame drops or increased ping during gameplay.
• 4.6.2.2 Competitors must not communicate, discuss, or take any action during game pauses that constitutes communication.

Rulebook: Arena of Valor (RoV)
Source: local://competition_rules/competition_rules_rov_blueket_2025_men
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- 4.3.1. If a participant disconnects during the match, the game will be paused temporarily. Each team may pause the game up to five times, each pause not exceeding one minute. If the time limit is exceeded, the other team may immediately resume the game and continue playing normally.

อ้างอิง `competition_rules_rov_blueket_2025_men_s06_c01`; source hash `13680e662a0fff83acfe8826d260397d13a87b82d772b861b2b58de7f1fc5a92`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### rov-rematch-th

**คำถาม:** กติกา RoV ขอเริ่มเกมใหม่ก่อนและหลัง First Blood ได้ไหม

**คำตอบเดิม:**
```text
ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
```

**ข้อที่ตัวตรวจรายงาน:** outcome_mismatch, missing_complete_clause, missing_complete_clause, first_line_off_topic, wrong_game_evidence

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- 4.3.3.ในกรณีที่ยังไม่มี First Blood และเวลาในเกมยังไม่เกิน 2 นาที ทีมที่ผู้เข้าแข่งขันหลุดสามารถแจ้งอีกทีมหนึ่งเพื่อขอเริ่มเกมใหม่ได้ทันที โดยผู้เข้าแข่งขันทุกคนจะต้องเลือกฮีโร่และตำแหน่งการเล่นเหมือนเกมแรกก่อนมีการขอเริ่มเกมใหม่
- 4.3.4.หากเกิดการ First Blood ขึ้นแล้ว หรือเริ่มเกมไปแล้วเกินกว่า 2 นาทีในเกม ห้ามไม่ให้ผู้เข้าแข่งขันทั้งสองฝ่ายขอเริ่มเกมใหม่ เว้นแต่ได้รับการอนุญาตจากคู่แข่ง และ/หรือตามเห็นสมควรจากกรรมการ

อ้างอิง `competition_rules_rov_blueket_2025_men_s06_c02`; source hash `f36218979545a6145121aa48bd869186a2aa7168c47ee92bb813ab4b33ae6ad1`

**เหตุการณ์จาก trace:**
```json
[
  {
    "stage": "universal_intent",
    "decision": "competition_rules/rule_lookup",
    "confidence": 0.9,
    "detail": "domain_terms=3; competition route overrides game/count ambiguity; named game availability terms found; competition route forces rule lookup",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false,
      "llm_first": false,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {},
      "intent_risk_flags": [
        "competing_domain_signals"
      ],
      "input_recovery": {
        "score": 0.1495,
        "language": "mixed",
        "language_quality": 0.8505,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.851",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "competition_rules",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        },
        {
          "id": "c3",
          "domain": "games",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.74,
          "reason": "domain keyword score=2"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [
        "lookup_competition_rule"
      ],
      "answer_style": "direct",
      "heuristic": {
        "domain": "competition_rules",
        "operation": "rule_lookup",
        "confidence": 0.9,
        "reason": "domain_terms=3; competition route overrides game/count ambiguity; named game availability terms found; competition route forces rule lookup"
      }
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
        "competition_rules_rov_blueket_2025_men_s01_c01",
        "competition_rules_rov_blueket_2025_men_s07_c01",
        "competition_rules_rov_blueket_2025_men_s08_c01",
        "competition_rules_rov_blueket_2025_men_s04_c01"
      ],
      "reason": "retrieved_source_does_not_prove_requested_facet"
    }
  }
]
```

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### rov-rematch-en

**คำถาม:** Can RoV tournament players request a restart before or after First Blood?

**คำตอบเดิม:**
```text
Answer: 4.5.1.1. If a competitor intentionally disconnects from the game without informing the referee, the referee may deny the pause request.

Details:
• 4.3.1. If a participant disconnects during the match, the game will be paused temporarily. Each team may pause the game up to five times, each pause not exceeding one minute. If the time limit is exceeded, the other team may immediately resume the game and continue playing normally.

Rulebook: Arena of Valor (RoV)
Source: local://competition_rules/competition_rules_rov_blueket_2025_men
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- 4.3.3. If no First Blood has occurred and in-game time has not exceeded 2 minutes, the team whose competitor disconnected may notify the other team and request an immediate restart. Before a restart is requested, every competitor must select the same hero and playing position as in the first game.
- 4.3.4. Once First Blood has occurred or the game has exceeded 2 minutes, neither team may request a restart unless the opponent permits it and/or the referees consider it appropriate.

อ้างอิง `competition_rules_rov_blueket_2025_men_s06_c02`; source hash `f36218979545a6145121aa48bd869186a2aa7168c47ee92bb813ab4b33ae6ad1`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### rov-break-en

**คำถาม:** How long is the break between games in the RoV tournament?

**คำตอบเดิม:**
```text
Answer: 4.3.2. If a competitor disconnects because of force majeure (such as an internet-service outage across the area or a game-server error), the affected team must notify the staff. Whether to allow a replay is at the referees' discretion.

Details:
• 4.3.3. If no First Blood has occurred and in-game time has not exceeded 2 minutes, the team whose competitor disconnected may notify the other team and request an immediate restart. Before a restart is requested, every competitor must select the same hero and playing position as in the first game.
• 4.3.4. Once First Blood has occurred or the game has exceeded 2 minutes, neither team may request a restart unless the opponent permits it and/or the referees consider it appropriate.
• 4.6. Player injuries, illnesses, or physical issues are not acceptable grounds for a competitor to pause gameplay.
• 4.6.1.1 The staff may order a game pause of no more than 5 minutes to cool down the device if they determine that the device's temperature will cause frame drops or increased ping during gameplay.
• 4.6.2.2 Competitors must not communicate, discuss, or take any action during game pauses that constitutes communication.
• Competition Rules 4. Regulations and Competition Rules
• 4.1.1. Prohibited to use character names or phrases that are offensive or disrespectful toward others.
• 4.1.3. The referees will announce the room number so both teams can enter the designated room.

Rulebook: Arena of Valor (RoV)
Source: local://competition_rules/competition_rules_rov_blueket_2025_men
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- 4.4.3. A 5-minute break follows every two games.

อ้างอิง `competition_rules_rov_blueket_2025_men_s06_c02`; source hash `f36218979545a6145121aa48bd869186a2aa7168c47ee92bb813ab4b33ae6ad1`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### rov-long-pause-th

**คำถาม:** กติกา RoV หยุดเกิน 10 นาทีกรรมการทำอย่างไร

**คำตอบเดิม:**
```text
ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
```

**ข้อที่ตัวตรวจรายงาน:** outcome_mismatch, missing_complete_clause, first_line_off_topic, wrong_game_evidence

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- 4.5.2.หากเกมหยุดลงเป็นเวลาเกินกว่า 10 นาที ทางทีมงานมีสิทธิสั่งให้เริ่มเกมใหม่ เว้นแต่ทีมผู้เข้าร่วมแข่งขันทีมใดทีมหนึ่งมีคะแนนมากกว่าอีกทีมเป็นจำนวนมาก ทางทีมงานอาจใช้ดุลยพินิจในการสั่งให้ทีมที่มีคะแนนมากกว่าดังกล่าวเป็นผู้ชนะในเกมที่หยุดลงนั้นตามที่เห็นควร

อ้างอิง `competition_rules_rov_blueket_2025_men_s06_c03`; source hash `01acace8187569211ae28e863776dc4decf7c5f8d29d289c89ae7bc16dc4b0d2`

**เหตุการณ์จาก trace:**
```json
[
  {
    "stage": "universal_intent",
    "decision": "competition_rules/rule_lookup",
    "confidence": 0.9,
    "detail": "domain_terms=3; competition route overrides game/count ambiguity; rule terms found; competition route forces rule lookup",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false,
      "llm_first": false,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {},
      "intent_risk_flags": [
        "competing_domain_signals"
      ],
      "input_recovery": {
        "score": 0.181,
        "language": "mixed",
        "language_quality": 0.819,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.819",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "competition_rules",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        },
        {
          "id": "c3",
          "domain": "members",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        },
        {
          "id": "c4",
          "domain": "games",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        },
        {
          "id": "c5",
          "domain": "competition_rules",
          "operation": "how_to",
          "target": "",
          "confidence": 0.66,
          "reason": "operation keyword score=1"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [
        "lookup_competition_rule"
      ],
      "answer_style": "direct",
      "heuristic": {
        "domain": "competition_rules",
        "operation": "rule_lookup",
        "confidence": 0.9,
        "reason": "domain_terms=3; competition route overrides game/count ambiguity; rule terms found; competition route forces rule lookup"
      }
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
        "competition_rules_rov_blueket_2025_men_s01_c01",
        "competition_rules_rov_blueket_2025_men_s08_c01",
        "competition_rules_rov_blueket_2025_men_s04_c01",
        "competition_rules_rov_blueket_2025_men_s03_c01"
      ],
      "reason": "retrieved_source_does_not_prove_requested_facet"
    }
  }
]
```

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### rov-long-pause-en

**คำถาม:** What may staff do if a RoV tournament pause exceeds 10 minutes?

**คำตอบเดิม:**
```text
Answer: 4.5.1.2 In cases where the game is paused due to technical issues, not caused by player actions, the event staff may order a pause and require players to rejoin the game after all disconnected players have reconnected.

Details:
• 4.5.2 If the game is paused for more than 10 minutes, the event staff may order a restart of the game, unless one team has a significantly larger score than the other; in such cases, the event staff may use their discretion to declare the higher-scoring team as the winner of the interrupted game.
• 4.5.4 The referee may pause the game for any reason.
• 4.5.1.1. If a competitor intentionally disconnects from the game without informing the referee, the referee may deny the pause request.
• 4.6. Player injuries, illnesses, or physical issues are not acceptable grounds for a competitor to pause gameplay.
• 4.6.1.1 The staff may order a game pause of no more than 5 minutes to cool down the device if they determine that the device's temperature will cause frame drops or increased ping during gameplay.
• 4.6.2.2 Competitors must not communicate, discuss, or take any action during game pauses that constitutes communication.

Rulebook: Arena of Valor (RoV)
Source: local://competition_rules/competition_rules_rov_blueket_2025_men
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- 4.5.2 If the game is paused for more than 10 minutes, the event staff may order a restart of the game, unless one team has a significantly larger score than the other; in such cases, the event staff may use their discretion to declare the higher-scoring team as the winner of the interrupted game.

อ้างอิง `competition_rules_rov_blueket_2025_men_s06_c03`; source hash `01acace8187569211ae28e863776dc4decf7c5f8d29d289c89ae7bc16dc4b0d2`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### rov-overheat-th

**คำถาม:** สอบถามหน่อยครับ กติกา RoV เครื่องร้อนหยุดได้กี่นาทีและเงื่อนไขอะไร หน่อย

**คำตอบเดิม:**
```text
คำตอบ: 4.4.3.พัก 5 นาที หลังจากจบทุกสองเกม

รายละเอียดที่เกี่ยวข้อง:
•    4.6.1.1. ทางทีมงานอาจสั่งให้หยุดพักเกมเป็นเวลาไม่เกินกว่า 5 นาที เพื่อทำให้อุปกรณ์พกพาดังกล่าวเย็นลง หากทีมงานเห็นว่าความร้อนของอุปกรณ์พกพาดังกล่าวจะทำให้เฟรมลดลงหรือ Ping เพิ่มขึ้นในเกม
•    4.6.2.2. ห้ามมิให้ผู้เข้าร่วมการแข่งขันพูดคุย ติดต่อสื่อสาร หรือดำเนินการใด ๆ อันเป็นการสื่อสารในระหว่างการหยุดพักเกม

อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย
แหล่งข้อมูล: local://competition_rules/competition_rules_rov_blueket_2025_men
```

**ข้อที่ตัวตรวจรายงาน:** first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- 4.6.1.1. ทางทีมงานอาจสั่งให้หยุดพักเกมเป็นเวลาไม่เกินกว่า 5 นาที เพื่อทำให้อุปกรณ์พกพาดังกล่าวเย็นลง หากทีมงานเห็นว่าความร้อนของอุปกรณ์พกพาดังกล่าวจะทำให้เฟรมลดลงหรือ Ping เพิ่มขึ้นในเกม

อ้างอิง `competition_rules_rov_blueket_2025_men_s06_c04`; source hash `bea166fb055836153ebc30df1f0005e562b8d54d2bf9e24c12982a9b28b16e0d`

**เหตุการณ์จาก trace:**
```json
[
  {
    "stage": "universal_intent",
    "decision": "competition_rules/rule_lookup",
    "confidence": 0.9,
    "detail": "domain_terms=3; competition route overrides game/count ambiguity; rule terms found; competition route forces rule lookup",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false,
      "llm_first": false,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {},
      "intent_risk_flags": [
        "competing_domain_signals"
      ],
      "input_recovery": {
        "score": 0.2724,
        "language": "mixed",
        "language_quality": 0.7276,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.728",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "competition_rules",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "competition_rules",
          "operation": "count",
          "target": "",
          "confidence": 0.97,
          "reason": "router category candidate"
        },
        {
          "id": "c3",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        },
        {
          "id": "c4",
          "domain": "games",
          "operation": "count",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        },
        {
          "id": "c5",
          "domain": "equipment",
          "operation": "count",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [
        "lookup_competition_rule"
      ],
      "answer_style": "direct",
      "heuristic": {
        "domain": "competition_rules",
        "operation": "rule_lookup",
        "confidence": 0.9,
        "reason": "domain_terms=3; competition route overrides game/count ambiguity; rule terms found; competition route forces rule lookup"
      }
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

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### rov-overheat-en

**คำถาม:** How long may staff pause for device overheating in the RoV tournament and under what condition?

**คำตอบเดิม:**
```text
Answer: 4.6. Player injuries, illnesses, or physical issues are not acceptable grounds for a competitor to pause gameplay.

Details:
• 4.6.1.1 The staff may order a game pause of no more than 5 minutes to cool down the device if they determine that the device's temperature will cause frame drops or increased ping during gameplay.
• 4.6.2.2 Competitors must not communicate, discuss, or take any action during game pauses that constitutes communication.
• 4.5.1.1. If a competitor intentionally disconnects from the game without informing the referee, the referee may deny the pause request.
• 4.5.1.2 In cases where the game is paused due to technical issues, not caused by player actions, the event staff may order a pause and require players to rejoin the game after all disconnected players have reconnected.
• 4.5.2 If the game is paused for more than 10 minutes, the event staff may order a restart of the game, unless one team has a significantly larger score than the other; in such cases, the event staff may use their discretion to declare the higher-scoring team as the winner of the interrupted game.
• 4.5.4 The referee may pause the game for any reason.

Rulebook: Arena of Valor (RoV)
Source: local://competition_rules/competition_rules_rov_blueket_2025_men
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- 4.6.1.1 The staff may order a game pause of no more than 5 minutes to cool down the device if they determine that the device's temperature will cause frame drops or increased ping during gameplay.

อ้างอิง `competition_rules_rov_blueket_2025_men_s06_c04`; source hash `bea166fb055836153ebc30df1f0005e562b8d54d2bf9e24c12982a9b28b16e0d`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### tekken8-decider-en

**คำถาม:** What happens at a 1-1 tie in the Tekken 8 tournament?

**คำตอบเดิม:**
```text
Answer: PlayStation 5 console used

Details:
• Singles (1v1) format
• FT2: Winner is the first to win two games
• Rounds per game (Round): 3
• Time per round (Timer): 60 seconds
• Advantage: No advantage
• Competitors must accept and follow the rules, regulations, and referees' decisions unconditionally.
• Organizers may change competition rules at any time without prior notice.
• Referees may reconsider decisions as appropriate to ensure fairness.

Rulebook: Tekken 8
Source: local://competition_rules/competition_rules_tekken8_psu_esports
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- If tied at 1-1, a deciding game will be played

อ้างอิง `competition_rules_tekken8_psu_esports_s02_c01`; source hash `edc60f7da178b29666c874f1ae9471889b4f874bc64a4e49624c1df11bfa4aad`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### tekken8-assist-th

**คำถาม:** กติกา Tekken 8 ใช้ปุ่ม Assist ได้ไหม

**คำตอบเดิม:**
```text
คำตอบ: ในแต่ละเกมใช้กติกา R3 (แข่ง 3 รอบต่อเกม) และ 60S (จำกัดเวลา 60 วินาทีต่อรอบ)

รายละเอียดที่เกี่ยวข้อง:
•    ผู้เข้าแข่งขันต้องยอมรับและปฏิบัติตามกฎ กติกา และคำตัดสินของกรรมการโดยไม่มีเงื่อนไข
•    ผู้จัดมีสิทธิ์ปรับเปลี่ยนกฎการแข่งขันได้ตลอดเวลาโดยไม่ต้องแจ้งให้ทราบล่วงหน้า
•    เวลาแข่งขันต่อรอบ (Timer): 60 วินาที
•    ใช้เครื่องเกม PlayStation 5
•    FT2: ผู้ชนะคือผู้ที่ชนะครบ 2 เกมก่อน

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- อนุญาตให้ใช้ ปุ่ม Assist หรือระบบช่วยเหลือพิเศษ

อ้างอิง `competition_rules_tekken8_psu_esports_s03_c01`; source hash `8bd844d467a1b0ff7b47b68610e5a8dc605d07fc097e9113b9daa01c0a949f57`

**เหตุการณ์จาก trace:**
```json
[
  {
    "stage": "universal_intent",
    "decision": "games/availability",
    "confidence": 0.88,
    "detail": "known game alias found; named game availability terms found",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false,
      "llm_first": false,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {},
      "intent_risk_flags": [
        "competing_domain_signals",
        "competition_signal_conflicts_with_domain",
        "low_candidate_margin"
      ],
      "input_recovery": {
        "score": 0.1655,
        "language": "mixed",
        "language_quality": 0.8345,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.834",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "games",
          "operation": "availability",
          "target": "",
          "confidence": 0.88,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "unknown",
          "target": "",
          "confidence": 0.97,
          "reason": "router category candidate"
        },
        {
          "id": "c3",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        },
        {
          "id": "c4",
          "domain": "game_controls",
          "operation": "control",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        },
        {
          "id": "c5",
          "domain": "competition_rules",
          "operation": "unknown",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        },
        {
          "id": "c6",
          "domain": "games",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.66,
          "reason": "operation keyword score=1"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [
        "check_availability"
      ],
      "answer_style": "direct",
      "heuristic": {
        "domain": "games",
        "operation": "availability",
        "confidence": 0.88,
        "reason": "known game alias found; named game availability terms found"
      }
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

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### tekken8-assist-en

**คำถาม:** Are Assist buttons permitted in the Tekken 8 tournament?

**คำตอบเดิม:**
```text
Answer: Any character can be selected (except DLC characters)

Details:
• No character customization allowed in any case (such as clothing, hairstyle, combat effects, aura, etc.)
• Only standard skins are permitted
• Rounds per game (Round): 3
• Time per round (Timer): 60 seconds
• Advantage: No advantage
• PlayStation 5 console used
• Singles (1v1) format
• FT2: Winner is the first to win two games

Rulebook: Tekken 8
Source: local://competition_rules/competition_rules_tekken8_psu_esports
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- Assist buttons or special assist systems are allowed

อ้างอิง `competition_rules_tekken8_psu_esports_s03_c01`; source hash `8bd844d467a1b0ff7b47b68610e5a8dc605d07fc097e9113b9daa01c0a949f57`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### tekken8-settings-th

**คำถาม:** กติกา Tekken 8 การตั้งค่าเกมเป็นอย่างไร

**คำตอบเดิม:**
```text
คำตอบ: จำนวนรอบต่อเกม (Round): 3

รายละเอียดที่เกี่ยวข้อง:
•    เวลาแข่งขันต่อรอบ (Timer): 60 วินาที

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, missing_complete_clause

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- จำนวนรอบต่อเกม (Round): 3
- เวลาแข่งขันต่อรอบ (Timer): 60 วินาที
- Advantage: No advantage
- Stage: Random

อ้างอิง `competition_rules_tekken8_psu_esports_s04_c01`; source hash `757924c102ab2e9450d63834286ebe88d01ffa05d697c3fd1d0e9544d07cc18c`

**เหตุการณ์จาก trace:**
```json
[
  {
    "stage": "universal_intent",
    "decision": "competition_rules/rule_lookup",
    "confidence": 0.97,
    "detail": "one registered game and an explicit rule facet; source coverage remains required",
    "metadata": {
      "method": "competition_target_first",
      "llm_attempted": false,
      "target": "tekken8",
      "filters": {
        "competition_facet": "match_settings",
        "competition_rulebook_id": "competition_rules_tekken8_psu_esports"
      },
      "answer_coverage_deferred": true
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "accepted",
    "confidence": 0.84,
    "detail": "target-filtered source chunks are preferred over summary fact cards",
    "metadata": {
      "hit_count": 1,
      "validation_errors": [],
      "pause_detail_missing": false
    }
  }
]
```

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### tekken8-settings-en

**คำถาม:** What are the Tekken 8 tournament in-game settings?

**คำตอบเดิม:**
```text
Answer: Rounds per game (Round): 3

Details:
• Time per round (Timer): 60 seconds
• Advantage: No advantage

Rulebook: Tekken 8
Source: local://competition_rules/competition_rules_tekken8_psu_esports
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- Rounds per game (Round): 3
- Time per round (Timer): 60 seconds
- Advantage: No advantage
- Stage: Random

อ้างอิง `competition_rules_tekken8_psu_esports_s04_c01`; source hash `757924c102ab2e9450d63834286ebe88d01ffa05d697c3fd1d0e9544d07cc18c`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### tekken8-officials-th

**คำถาม:** กติกา Tekken 8 กรรมการเปลี่ยนคำตัดสินได้ไหม

**คำตอบเดิม:**
```text
ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
```

**ข้อที่ตัวตรวจรายงาน:** outcome_mismatch, missing_complete_clause, first_line_off_topic, wrong_game_evidence

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- กรรมการสามารถพิจารณาเปลี่ยนแปลงคำตัดสินเพื่อให้เกิดความยุติธรรมตามความเหมาะสม

อ้างอิง `competition_rules_tekken8_psu_esports_s06_c01`; source hash `41cc3adfea22bd6f466cfa4f7c773000db213c18f1fda6065af55bba2f7c6209`

**เหตุการณ์จาก trace:**
```json
[
  {
    "stage": "universal_intent",
    "decision": "competition_rules/rule_lookup",
    "confidence": 0.9,
    "detail": "known game alias found; competition route overrides game/count ambiguity; named game availability terms found; competition route forces rule lookup",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false,
      "llm_first": false,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {},
      "intent_risk_flags": [
        "competing_domain_signals"
      ],
      "input_recovery": {
        "score": 0.1127,
        "language": "mixed",
        "language_quality": 0.8873,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.887",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "competition_rules",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        },
        {
          "id": "c3",
          "domain": "members",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        },
        {
          "id": "c4",
          "domain": "games",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [
        "lookup_competition_rule"
      ],
      "answer_style": "direct",
      "heuristic": {
        "domain": "competition_rules",
        "operation": "rule_lookup",
        "confidence": 0.9,
        "reason": "known game alias found; competition route overrides game/count ambiguity; named game availability terms found; competition route forces rule lookup"
      }
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
        "competition_rules_tekken8_psu_esports_s06_c01",
        "competition_rules_tekken8_psu_esports_s02_c01",
        "competition_rules_tekken8_psu_esports_s07_c01",
        "competition_rules_tekken8_psu_esports_s08_c01",
        "competition_rules_tekken8_psu_esports_s05_c01",
        "competition_rules_tekken8_psu_esports_s04_c01",
        "competition_rules_tekken8_psu_esports_s03_c01",
        "competition_rules_tekken8_psu_esports_s01_c01"
      ],
      "reason": "retrieved_source_does_not_prove_requested_facet"
    }
  }
]
```

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### tekken8-officials-en

**คำถาม:** Can Tekken 8 tournament referees reconsider their decisions?

**คำตอบเดิม:**
```text
Answer: Competitors must accept and follow the rules, regulations, and referees' decisions unconditionally.

Details:
• Organizers may change competition rules at any time without prior notice.
• Referees may reconsider decisions as appropriate to ensure fairness.
• Unsportsmanlike behavior, such as mocking, taunting, or rude words or actions towards others, is prohibited. Violations result in an immediate forfeit without exception.
• Competitors must respect referees and other competitors. Insulting or disrespectful behavior is prohibited in all cases. Violations result in an immediate forfeit without exception.
• Players must not leave the game before the competition ends unless authorized by the referees.
• The game may be paused only when all players agree and there is a valid reason, such as equipment malfunction or an emergency.
• Pausing the game without necessity will result in the same penalty as leaving the game prematurely.

Rulebook: Tekken 8
Source: local://competition_rules/competition_rules_tekken8_psu_esports
```

**ข้อที่ตัวตรวจรายงาน:** first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- Referees may reconsider decisions as appropriate to ensure fairness.

อ้างอิง `competition_rules_tekken8_psu_esports_s06_c01`; source hash `41cc3adfea22bd6f466cfa4f7c773000db213c18f1fda6065af55bba2f7c6209`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### valorant-notes-th

**คำถาม:** กติกา VALORANT ใครนำโน้ตเข้าแข่งได้

**คำตอบเดิม:**
```text
ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน
```

**ข้อที่ตัวตรวจรายงาน:** outcome_mismatch, missing_complete_clause, first_line_off_topic, wrong_game_evidence

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- เอกสารและโน้ต ผู้เล่นห้ามนำโน้ตหรือเอกสารเข้าไป แต่ หัวหน้าทีม สามารถนำเข้าไปได้ และต้องให้เอกสารแก่กรรมการก่อนการแข่งขันทุกครั้ง

อ้างอิง `competition_rules_valorant_psu_phuket_2026_s02_c01`; source hash `5057afc56c92f944deea6b41c4b7ccb4a2a82970a05146896b3d8cb6ef2a7282`

**เหตุการณ์จาก trace:**
```json
[
  {
    "stage": "universal_intent",
    "decision": "competition_rules/rule_lookup",
    "confidence": 0.9,
    "detail": "known game alias found; competition route overrides game/count ambiguity; rule terms found; competition route forces rule lookup",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false,
      "llm_first": false,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {},
      "intent_risk_flags": [
        "competing_domain_signals",
        "people_or_role_signal_conflicts_with_domain"
      ],
      "input_recovery": {
        "score": 0.2595,
        "language": "mixed",
        "language_quality": 0.7405,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.741",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "competition_rules",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        },
        {
          "id": "c3",
          "domain": "games",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [
        "lookup_competition_rule"
      ],
      "answer_style": "direct",
      "heuristic": {
        "domain": "competition_rules",
        "operation": "rule_lookup",
        "confidence": 0.9,
        "reason": "known game alias found; competition route overrides game/count ambiguity; rule terms found; competition route forces rule lookup"
      }
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
        "competition_rules_valorant_psu_phuket_2026_s01_c01",
        "competition_rules_valorant_psu_phuket_2026_s06_c01",
        "competition_rules_valorant_psu_phuket_2026_s03_c01",
        "competition_rules_valorant_psu_phuket_2026_s08_c01",
        "competition_rules_valorant_psu_phuket_2026_s07_c01",
        "competition_rules_valorant_psu_phuket_2026_s11_c01",
        "competition_rules_valorant_psu_phuket_2026_s04_c01"
      ],
      "reason": "retrieved_source_does_not_prove_requested_facet"
    }
  }
]
```

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### valorant-notes-en

**คำถาม:** Who may bring notes into the VALORANT tournament area?

**คำตอบเดิม:**
```text
Answer: No more than 6 players are allowed in the match preparation area.

Details:
• Mobile phones, tablets, and smartwatches are strictly prohibited in the competition area until the match has concluded.
• Players may not bring notes or documents into the competition area.
• Personnel: During Match Prep, no more than 6 players may be present.
• Electronic devices: Mobile phones, tablets, and smartwatches may not be brought into the competition area until the match ends.
• Documents and notes: Players may not bring notes or documents into the area. Team captains may bring them in, but must give the documents to the referees before every match.
• In LAN competitions, players must strictly comply with equipment regulations to ensure fair play.
• Allowed personal equipment
• Players may bring and use their own keyboard (wired/wireless), mouse (wired/wireless), mouse bungee, mouse pad, In-ear earphones (wired), headset (wired).

Rulebook: VALORANT
Source: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- Documents and notes: Players may not bring notes or documents into the area. Team captains may bring them in, but must give the documents to the referees before every match.

อ้างอิง `competition_rules_valorant_psu_phuket_2026_s02_c01`; source hash `5057afc56c92f944deea6b41c4b7ccb4a2a82970a05146896b3d8cb6ef2a7282`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### valorant-checkin-en

**คำถาม:** How early must VALORANT tournament teams arrive at the venue?

**คำตอบเดิม:**
```text
Answer: Teams must arrive at the venue at least 30 minutes before the scheduled match time.

Details:
• No more than 6 players are allowed in the match preparation area.
• The team captain is allowed to bring documents, which must be submitted to the referee before the match.
• Personnel: During Match Prep, no more than 6 players may be present.
• Electronic devices: Mobile phones, tablets, and smartwatches may not be brought into the competition area until the match ends.
• Documents and notes: Players may not bring notes or documents into the area. Team captains may bring them in, but must give the documents to the referees before every match.

Rulebook: VALORANT
Source: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- Check-in: arrive at least 30 minutes before the scheduled match time.

อ้างอิง `competition_rules_valorant_psu_phuket_2026_s03_c01`; source hash `cbe6576e922fbf445aebde18945b6dcffe4265a988342cb8df7bd14fa7d4e19a`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### valorant-new-content-en

**คำถาม:** How long are new agents and new maps restricted in the VALORANT tournament?

**คำตอบเดิม:**
```text
Answer: Teams must arrive at the venue at least 30 minutes before the scheduled match time.

Details:
• New agents are restricted for approximately 2 weeks after being released in Competitive mode.
• New maps are restricted for approximately 4 weeks after being released in Competitive mode.
• Bugs that do not significantly affect competitive integrity. Play must continue, and no challenge may be requested.
• Bugs that significantly affect gameplay or core mechanics and cannot be immediately resolved. Teams may request a challenge for review.
• Round Rollback
• Using teammates to boost to locations higher than normal jump height is prohibited.

Rulebook: VALORANT
Source: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- New agents may not be used for approximately 2 weeks after release in Competitive mode.
- New maps may not be used for approximately 4 weeks after release in Competitive mode.

อ้างอิง `competition_rules_valorant_psu_phuket_2026_s03_c01`; source hash `cbe6576e922fbf445aebde18945b6dcffe4265a988342cb8df7bd14fa7d4e19a`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### valorant-settings-th

**คำถาม:** สอบถามหน่อยครับ กติกา VALORANT การตั้งค่าเลือด ศพ FPS และ Latency เป็นอย่างไร หน่อย

**คำตอบเดิม:**
```text
คำตอบ: ผู้เล่นต้อง ปิด (OFF) การแสดงผลเลือด (Blood) และศพ (Bodies)

รายละเอียดที่เกี่ยวข้อง:
•    เอเจนท์ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 2 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive
•    แผนที่ใหม่ จะถูกจำกัดห้ามใช้ประมาณ 4 สัปดาห์ หลังเปิดให้เล่นในโหมด Competitive
•    เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ
•    ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที
•    เวลาการรายงานตัว ต้องมาถึงสนามแข่งไม่น้อยกว่า 30 นาที ก่อนเวลาแข่ง

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- ผู้เล่นต้อง ปิด (OFF) การแสดงผลเลือด (Blood) และศพ (Bodies)
- ห้ามแสดงกราฟ FPS หรือ Latency ระหว่างการแข่งขัน

อ้างอิง `competition_rules_valorant_psu_phuket_2026_s03_c01`; source hash `cbe6576e922fbf445aebde18945b6dcffe4265a988342cb8df7bd14fa7d4e19a`

**เหตุการณ์จาก trace:**
```json
[
  {
    "stage": "universal_intent",
    "decision": "competition_rules/rule_lookup",
    "confidence": 0.9,
    "detail": "known game alias found; competition route overrides game/count ambiguity; rule terms found; competition route forces rule lookup",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false,
      "llm_first": false,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {},
      "intent_risk_flags": [
        "competing_domain_signals"
      ],
      "input_recovery": {
        "score": 0.2705,
        "language": "mixed",
        "language_quality": 0.7295,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.729",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "competition_rules",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        },
        {
          "id": "c3",
          "domain": "games",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        },
        {
          "id": "c4",
          "domain": "competition_rules",
          "operation": "how_to",
          "target": "",
          "confidence": 0.66,
          "reason": "operation keyword score=1"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [
        "lookup_competition_rule"
      ],
      "answer_style": "direct",
      "heuristic": {
        "domain": "competition_rules",
        "operation": "rule_lookup",
        "confidence": 0.9,
        "reason": "known game alias found; competition route overrides game/count ambiguity; rule terms found; competition route forces rule lookup"
      }
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

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### valorant-settings-en

**คำถาม:** What do VALORANT tournament rules require for Blood, Bodies, FPS and Latency displays?

**คำตอบเดิม:**
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

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- Turn OFF Blood and Bodies displays. Displaying FPS or Latency graphs during competition is prohibited.

อ้างอิง `competition_rules_valorant_psu_phuket_2026_s03_c01`; source hash `cbe6576e922fbf445aebde18945b6dcffe4265a988342cb8df7bd14fa7d4e19a`

**เหตุการณ์จาก trace:**
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

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### valorant-forfeit-score-th

**คำถาม:** กติกา VALORANT ปรับแพ้บันทึกคะแนนเท่าไร

**คำตอบเดิม:**
```text
คำตอบ: 5. การปรับแพ้ในแมตช์ (Match Forfeit) กรณีทุจริต (Cheating) หรือล็อกผล (Match fixing)

รายละเอียดที่เกี่ยวข้อง:
•    4. การปรับแพ้ในแผนที่ (Map Forfeit) สำหรับความผิดร้ายแรงหรือความผิดซ้ำที่ส่งผลกระทบต่อผลการแข่งในแผนที่นั้น
•    3. การปรับแพ้ในรอบ (Round Loss) เมื่อพบว่าผู้เล่นหรือทีมมีเจตนาใช้ช่องโหว่เพื่อสร้างความได้เปรียบ

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- การปรับแพ้ (Forfeiture) หากมีการปรับแพ้ ผลการแข่งในแผนที่นั้นจะถูกบันทึกเป็น 13-0

อ้างอิง `competition_rules_valorant_psu_phuket_2026_s04_c01`; source hash `4b950c859236fc859ab97f761864fda9b9f698bf26c341a9694ef52a35c036a0`

**เหตุการณ์จาก trace:**
```json
[
  {
    "stage": "universal_intent",
    "decision": "competition_rules/rule_lookup",
    "confidence": 0.97,
    "detail": "one registered game and an explicit rule facet; source coverage remains required",
    "metadata": {
      "method": "competition_target_first",
      "llm_attempted": false,
      "target": "valorant",
      "filters": {
        "competition_facet": "penalty",
        "competition_rulebook_id": "competition_rules_valorant_psu_phuket_2026"
      },
      "answer_coverage_deferred": true
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "accepted",
    "confidence": 0.84,
    "detail": "target-filtered source chunks are preferred over summary fact cards",
    "metadata": {
      "hit_count": 5,
      "validation_errors": [],
      "pause_detail_missing": false
    }
  }
]
```

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### valorant-forfeit-score-en

**คำถาม:** What score is recorded for a forfeited map in the VALORANT tournament?

**คำตอบเดิม:**
```text
Answer: Warning - For first offenses with low impact.

Details:
• Round Rollback - When an exploit clearly affects a round but intent cannot be determined.
• Round Loss - When a player or team is found to have intentionally used an exploit for advantage.
• Map Forfeit - For severe offenses or repeated violations that affect the map result.
• Match Forfeit - In cases of cheating or match fixing.

Rulebook: VALORANT
Source: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- If a forfeit is imposed, the result for that map is recorded as 13-0.

อ้างอิง `competition_rules_valorant_psu_phuket_2026_s04_c01`; source hash `4b950c859236fc859ab97f761864fda9b9f698bf26c341a9694ef52a35c036a0`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### valorant-overtime-timeout-th

**คำถาม:** กติกา VALORANT Tactical Timeout ช่วงต่อเวลาทบโควตาไหม

**คำตอบเดิม:**
```text
คำตอบ: ขอได้ 2 ครั้งต่อแผนที่ ในรอบปกติ (24 รอบแรก) ครั้งละ 60 วินาที

รายละเอียดที่เกี่ยวข้อง:
•    เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- เมื่อเข้าสู่ช่วงต่อเวลา (Overtime) จะได้เพิ่มอีกทีมละ 1 ครั้ง โดยที่โควตาจากรอบปกติจะไม่ถูกนำมาทบ

อ้างอิง `competition_rules_valorant_psu_phuket_2026_s06_c01`; source hash `0077e93003a4ce3d7c7f8d6bf3cc422adf1132ddb5bb957f7648d97268828087`

**เหตุการณ์จาก trace:**
```json
[
  {
    "stage": "universal_intent",
    "decision": "competition_rules/rule_lookup",
    "confidence": 0.97,
    "detail": "one registered game and an explicit rule facet; source coverage remains required",
    "metadata": {
      "method": "competition_target_first",
      "llm_attempted": false,
      "target": "valorant",
      "filters": {
        "competition_facet": "pause_timeout",
        "competition_rulebook_id": "competition_rules_valorant_psu_phuket_2026"
      },
      "answer_coverage_deferred": true
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

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### valorant-overtime-timeout-en

**คำถาม:** Do regulation Tactical Timeout quotas carry into VALORANT tournament overtime?

**คำตอบเดิม:**
```text
Answer: 2 requests per map during regulation (first 24 rounds), 60 seconds each.

Details:
• In Overtime, each team receives 1 additional timeout. Regulation quotas do not carry over.

Rulebook: VALORANT
Source: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- In Overtime, each team receives 1 additional timeout. Regulation quotas do not carry over.

อ้างอิง `competition_rules_valorant_psu_phuket_2026_s06_c01`; source hash `0077e93003a4ce3d7c7f8d6bf3cc422adf1132ddb5bb957f7648d97268828087`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### valorant-emergency-en

**คำถาม:** What are the request and time limits for a VALORANT emergency pause?

**คำตอบเดิม:**
```text
Answer: Each team may request 1 pause per map.

Details:
• Total emergency pause time may not exceed 10 minutes per match. If the time limit is exceeded, the affected player may be disqualified from continuing and must be replaced by a substitute

Rulebook: VALORANT
Source: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- One request per map is allowed.
- Total emergency-pause time may not exceed 10 minutes per match. If that limit is exceeded, the affected player may be unable to continue and must be replaced by a substitute.

อ้างอิง `competition_rules_valorant_psu_phuket_2026_s08_c01`; source hash `cce855d13600dc1c7b7526393ed2bb5e19ef57e637ae4282eff86b1da617c80f`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### valorant-rollback-th

**คำถาม:** กติกา VALORANT ย้อนรอบก่อนและหลังทำดาเมจได้ไหม

**คำตอบเดิม:**
```text
คำตอบ: หากเกิดบั๊กก่อนที่จะมีการทำดาเมจใส่กัน เจ้าหน้าที่อาจย้อนรอบให้ได้

รายละเอียดที่เกี่ยวข้อง:
•    Play Through Bug บั๊กที่ไม่ส่งผลกระทบต่อความยุติธรรมอย่างมีนัยสำคัญ ผู้เล่นต้องเล่นต่อไปและไม่สามารถขอ Challenge ได้
•    Major Bug บั๊กที่ส่งผลกระทบต่อการเล่นหรือกลไกเกมอย่างมากและไม่มีทางแก้ไขเฉพาะหน้า ทีมสามารถขอ Challenge เพื่อตรวจสอบได้
•    ห้ามใช้สกิลในพื้นที่นอกขอบเขตแผนที่ (Out of boundaries) เพื่อหาข้อมูลหรือสร้างความได้เปรียบ
•    Game Breaking Bug บั๊กที่ทำลายความยุติธรรมของรอบนั้นจนไม่สามารถตัดสินผลแพ้ชนะได้

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- หากเกิดบั๊กก่อนที่จะมีการทำดาเมจใส่กัน เจ้าหน้าที่อาจย้อนรอบให้ได้
- หากมีการทำดาเมจไปแล้ว จะไม่มีการย้อนรอบยกเว้นผ่านกระบวนการ Challenge

อ้างอิง `competition_rules_valorant_psu_phuket_2026_s08_c01`; source hash `cce855d13600dc1c7b7526393ed2bb5e19ef57e637ae4282eff86b1da617c80f`

**เหตุการณ์จาก trace:**
```json
[
  {
    "stage": "universal_intent",
    "decision": "competition_rules/rule_lookup",
    "confidence": 0.9,
    "detail": "known game alias found; competition route overrides game/count ambiguity; named game availability terms found; competition route forces rule lookup",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false,
      "llm_first": false,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {},
      "intent_risk_flags": [
        "competing_domain_signals"
      ],
      "input_recovery": {
        "score": 0.194,
        "language": "mixed",
        "language_quality": 0.806,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.806",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "competition_rules",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        },
        {
          "id": "c3",
          "domain": "games",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        },
        {
          "id": "c4",
          "domain": "reservation",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [
        "lookup_competition_rule"
      ],
      "answer_style": "direct",
      "heuristic": {
        "domain": "competition_rules",
        "operation": "rule_lookup",
        "confidence": 0.9,
        "reason": "known game alias found; competition route overrides game/count ambiguity; named game availability terms found; competition route forces rule lookup"
      }
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

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### valorant-rollback-en

**คำถาม:** Can officials roll back a VALORANT tournament round before or after damage is dealt?

**คำตอบเดิม:**
```text
Answer: Bugs that do not significantly affect competitive integrity. Play must continue, and no challenge may be requested.

Details:
• Bugs that significantly affect gameplay or core mechanics and cannot be immediately resolved. Teams may request a challenge for review.
• Round Rollback
• One request per map is allowed.
• Total emergency-pause time may not exceed 10 minutes per match. If that limit is exceeded, the affected player may be unable to continue and must be replaced by a substitute.
• Play Through Bug: does not significantly affect fairness. The player must continue and may not request a Challenge.
• Check-in: arrive at least 30 minutes before the scheduled match time.
• New agents may not be used for approximately 2 weeks after release in Competitive mode.
• New maps may not be used for approximately 4 weeks after release in Competitive mode.

Rulebook: VALORANT
Source: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- If a bug occurs before either side deals damage, officials may roll back the round.
- If damage has already been dealt, no rollback is allowed unless through the Challenge process.

อ้างอิง `competition_rules_valorant_psu_phuket_2026_s08_c01`; source hash `cce855d13600dc1c7b7526393ed2bb5e19ef57e637ae4282eff86b1da617c80f`

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### valorant-kayo-th

**คำถาม:** กติกา VALORANT ZERO/POINT ของ KAY/O มีข้อยกเว้นอะไร

**คำตอบเดิม:**
```text
คำตอบ: หากมีการทำดาเมจไปแล้ว จะไม่มีการย้อนรอบยกเว้นผ่านกระบวนการ Challenge

รายละเอียดที่เกี่ยวข้อง:
•    Play Through Bug บั๊กที่ไม่ส่งผลกระทบต่อความยุติธรรมอย่างมีนัยสำคัญ ผู้เล่นต้องเล่นต่อไปและไม่สามารถขอ Challenge ได้
•    ข้อยกเว้นพิเศษ สกิล ZERO/POINT ของ KAY/O สามารถใช้ภายนอกแผนที่หรือจุดที่ทำลายไม่ได้ได้ แต่ตัวมีดห้ามพุ่งทะลุ Texture ที่ควรจะเป็นของแข็ง
•    ห้ามใช้สกิลในพื้นที่นอกขอบเขตแผนที่ (Out of boundaries) เพื่อหาข้อมูลหรือสร้างความได้เปรียบ
•    ห้ามวางกล้อง Cypher ในจุดที่มองไม่เห็นหรือทำลายไม่ได้ผ่านการทะลุ Texture ของแผนที่

อ้างอิงจากกติกา: VALORANT / PSU Phuket VALORANT 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_valorant_psu_phuket_2026
```

**ข้อที่ตัวตรวจรายงาน:** first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- ข้อยกเว้นพิเศษ สกิล ZERO/POINT ของ KAY/O สามารถใช้ภายนอกแผนที่หรือจุดที่ทำลายไม่ได้ได้ แต่ตัวมีดห้ามพุ่งทะลุ Texture ที่ควรจะเป็นของแข็ง

อ้างอิง `competition_rules_valorant_psu_phuket_2026_s09_c01`; source hash `67c9eaa2e70e0c7f1d94ef479709d68909d76215a32046bfd4c7d03437d90eee`

**เหตุการณ์จาก trace:**
```json
[
  {
    "stage": "universal_intent",
    "decision": "competition_rules/rule_lookup",
    "confidence": 0.9,
    "detail": "known game alias found; competition route overrides game/count ambiguity; rule terms found; competition route forces rule lookup",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false,
      "llm_first": false,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {},
      "intent_risk_flags": [
        "competing_domain_signals"
      ],
      "input_recovery": {
        "score": 0.1685,
        "language": "mixed",
        "language_quality": 0.8315,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.832",
        "action": "continue"
      },
      "llm_rejected_reason": "",
      "intent_candidates": [
        {
          "id": "c1",
          "domain": "competition_rules",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.9,
          "reason": "heuristic fallback"
        },
        {
          "id": "c2",
          "domain": "games",
          "operation": "list",
          "target": "",
          "confidence": 0.66,
          "reason": "game-domain catalog alternative"
        },
        {
          "id": "c3",
          "domain": "games",
          "operation": "rule_lookup",
          "target": "",
          "confidence": 0.66,
          "reason": "domain keyword score=1"
        }
      ],
      "target": "",
      "filters": {},
      "needs": [
        "lookup_competition_rule"
      ],
      "answer_style": "direct",
      "heuristic": {
        "domain": "competition_rules",
        "operation": "rule_lookup",
        "confidence": 0.9,
        "reason": "known game alias found; competition route overrides game/count ambiguity; rule terms found; competition route forces rule lookup"
      }
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

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

### valorant-kayo-en

**คำถาม:** What exception applies to KAY/O ZERO/POINT under VALORANT tournament rules?

**คำตอบเดิม:**
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

**ข้อที่ตัวตรวจรายงาน:** missing_complete_clause, first_line_off_topic

**ข้อกำหนดที่ใช้ตรวจฉบับ v2:**
- Special exception: KAY/O's ZERO/POINT may be used outside the map or in indestructible locations, but the knife must not pass through textures that should be solid.

อ้างอิง `competition_rules_valorant_psu_phuket_2026_s09_c01`; source hash `67c9eaa2e70e0c7f1d94ef479709d68909d76215a32046bfd4c7d03437d90eee`

**เหตุการณ์จาก trace:**
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

**หลังแก้:** ผ่าน contract; mode pipeline:competition_rule_detail_source

## ขอบเขตที่ยังรอ / ไม่อ้างว่าปิดปัญหาแล้ว

- Tekken s03 กับ s07 ขัดเรื่อง pause: ให้ผู้จัดยืนยันว่า s07 เป็นข้อยกเว้นหรือไม่ ต้องขอกรรมการก่อนอย่างไร และโทษเป็น Round/Game/FT2 Match
- V2 104 รายการยัง pending review; ไม่ publish และไม่เปลี่ยน owner schedule
- EN overlay ตรวจ source ได้ ไม่ใช่การรับรองอย่างเป็นทางการของผู้จัด
- คำถามรูปแบบใหม่และคำพิมพ์ผิดนอก vocab/budget ยังอาจต้อง clarification; ไม่มีผล field traffic ที่ยืนยันความครอบคลุม
- one local worker ยังมี bounded admission queue; การแก้ planned recycle ไม่ได้ยืนยัน SLA หลายผู้ใช้/งาน LLM พร้อมกัน
- r26 timeout 719s ไม่เกิดใน full r27 B; timing ใหม่วัด locale/cue/canonical/entry-to-split ได้ แต่ยังไม่ได้พิสูจน์ว่า timeout เก่าเกิดจาก worker recycle


## ผลปิดรอบบนแพ็กเกจจริง และความผิดที่เพิ่มระหว่างแก้

HTTP final แรกได้ 318/320 เพราะส่วน planned recycle logging ที่เพิ่มไว้ขาด keyword-only request_id ของ ParentPerformanceLogger.emit_parent. ทั้ง warming/spawn_failed/promoted/warmup_failed ต้องส่ง request_id. Mock เปล่าใน unit tests ไม่บังคับ signature จึงไม่จับข้อผิดพลาดนี้; verified เปลี่ยนเป็น create_autospec เพิ่ม spawn-failure assertion และส่ง request_id ทุก branch.

แพ็กเกจ verified ทดสอบ 320/320 +128/128 +36/36 +80/80 +8/8 ต่อเนื่อง รวม 572 และอีก 1 probe (573 HTTP200) event ยืนยัน promoted ready workers 2 ครั้ง. ทดสอบโปรเซสแยก 24 คำถามและ crash recovery พร้อม timeout recovery เดิมผ่าน. หลังเปลี่ยนเว็บ 8090 ตรวจ 36/36 +8/8 และ health/runtime ถูก. ดู FINAL_RESULTS_TH.md และ FINAL_VERIFICATION.json สำหรับขอบเขตของคะแนน.
