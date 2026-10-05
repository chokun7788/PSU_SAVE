# ข้อผิดจริงที่ยังต้องแก้หลัง r30-G2

ตรวจจากคำตอบ/trace และข้อความ source ที่มี ใช้เป็นงานรอบถัดไป ไม่เปลี่ยน expected เดิมเพื่อทำให้ผ่าน และไม่เหมารวมทุก fail เป็นสาเหตุเดียว

## CS2 ใช้แพลตฟอร์มอะไรและห้ามดัดแปลงตัวเกมไหม

ประเภท: target และ context หายหลัง splitter

คำตอบจริง:

คำถามนี้มีหลายเรื่อง ขอแยกตอบเป็นข้อ ๆ:

คำถามที่ 1: CS2 ใช้แพลตฟอร์มอะไร
คำตอบ: 2. เวอร์ชันของเกม การแข่งขันทั้งหมดจะใช้เวอร์ชันล่าสุดของ CS2 บนแพลตฟอร์ม Steam ห้ามใช้การดัดแปลงตัวเกมที่ไม่ได้รับอนุญาตโดยเด็ดขาด

รายละเอียดที่เกี่ยวข้อง:
•    1. ผู้เล่นสามารถปรับแต่งความสว่าง (Brightness), ความละเอียดหน้าจอ (Resolution) และเป้าเล็ง (Crosshair) เฉพาะในเกม และหน้าจอคอมพิวเตอร์เท่านั้น

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

คำถามที่ 2: ห้ามดัดแปลงตัวเกมไหม
กรุณางดส่งเสียงดังเกินควร และห้ามพูดจาดูหมิ่นหรือเสียดสีผู้อื่น
แหล่งข้อมูล: https://esports.computing.psu.ac.th/

ควรตอบ: ควรตอบเวอร์ชันล่าสุดบน Steam และข้อห้ามดัดแปลงตัวเกมจาก rulebook CS2 โดยรักษา target ของทุก proposition ข้อเสียงดังไม่ตอบการดัดแปลงเกม

สาเหตุและคะแนน: shared competition signal ยังไม่ครอบคลุม proposition เวอร์ชัน/ดัดแปลงตัวเกมในประโยค implicit จึงแยกคำถามก่อน target-bound detail ส่วนหลังไม่มีเกม; route/source validator ผ่านคำตอบกฎทั่วไปโดยไม่ได้ตรวจ proposition ของส่วนหลัง

Mode: `pipeline:multi_question_splitter`; confidence: `0.84`; route: `{"category": "multi_question", "intent": "multi_question_split", "confidence": 0.92, "answer_type": "summary", "risk": "medium", "reason": "split clear multi-intent question"}`

Trace ที่เกี่ยวข้อง:

```json
[]
```

Expected/trace/hits ทั้งหมดเก็บใน CONFIRMED_REMAINING_CASES.json

## RoV ใช้สกินพิเศษได้หรือเปล่า

ประเภท: implicit facet ไม่เข้าสู่ detail source

คำตอบจริง:

ยังไม่พบหัวข้อกติกาที่ยืนยันได้ตรงกับประเด็นที่ถามในเอกสารของเกมนี้ครับ จึงจะไม่ใช้หัวข้ออื่นมาตอบแทน

ควรตอบ: ควรอ้างข้อ 4.2.5 ห้ามใช้สกินนอกจาก Default โดยบอก rulebook RoV/Blueket 2025 ชาย

สาเหตุและคะแนน: source-detail มี concept skins แต่ gate ต้อง looks_like_competition_rule_query ก่อน; คำถาม permission สกินที่ไม่กล่าว แข่ง/กฎ ยังไม่ครอบคลุม แล้ว fallback ไม่ยืนยัน facet นี้ จึง no_answer แม้มี source

Mode: `pipeline:competition_facet_not_covered_no_answer`; confidence: `0.92`; route: `{"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "competition rule terms found before reservation/check-in; operation_first=competition_rule_lookup"}`

Trace ที่เกี่ยวข้อง:

```json
[
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
    "stage": "universal_intent",
    "decision": "competition_rules/rule_lookup",
    "confidence": 0.9,
    "detail": "domain_terms=2; competition route overrides game/count ambiguity; no clear operation terms; competition route forces rule lookup",
    "metadata": {
      "method": "heuristic",
      "llm_attempted": false,
      "llm_first": false,
      "llm_first_skip_reason": "",
      "llm_first_review_reason": "",
      "llm_call": {},
      "intent_risk_flags": [],
      "input_recovery": {
        "score": 0.0828,
        "language": "mixed",
        "language_quality": 0.9172,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.917",
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
        "reason": "domain_terms=2; competition route overrides game/count ambiguity; no clear operation terms; competition route forces rule lookup"
      }
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
        "competition_rules_rov_blueket_2025_men_s06_c03",
        "competition_rules_rov_blueket_2025_men_s06_c02",
        "competition_rules_rov_blueket_2025_men_s06_c04",
        "competition_rules_rov_blueket_2025_men_s08_c02",
        "competition_rules_rov_blueket_2025_men_s08_c01",
        "competition_rules_rov_blueket_2025_men_s04_c01",
        "competition_rules_rov_blueket_2025_men_s07_c01"
      ],
      "reason": "retrieved_source_does_not_prove_requested_facet"
    }
  }
]
```

Expected/trace/hits ทั้งหมดเก็บใน CONFIRMED_REMAINING_CASES.json

## CS2 ปิดรับสมัครแล้วเพิ่มเพื่อนเข้า roster ได้ปะ

ประเภท: qualifier เวลาและ action ถูกกลบด้วย noun roster

คำตอบจริง:

คำตอบ: 2. องค์ประกอบทีม แต่ละทีมประกอบด้วยผู้เล่น 5 คน

อ้างอิงจากกติกา: Counter-Strike 2 / PSU Phuket CS2 2026 Tournament
แหล่งข้อมูล: local://competition_rules/competition_rules_cs2_psu_phuket_2026

ควรตอบ: ควรดึงข้อไม่อนุญาตลงทะเบียนหลังปิดรับสมัคร ไม่ใช้จำนวน 5 คนตอบการเพิ่มรายชื่อ

สาเหตุและคะแนน: late_registration รองรับลำดับ หลัง...ปิดรับสมัคร แต่ไม่รองรับ ปิดรับสมัครแล้ว...; roster concept จับ noun roster และเลือกองค์ประกอบทีมได้ literal จริง แต่ไม่มีข้อห้ามตาม action; confidence .97 เป็นค่าจับเส้นทางตามโค้ด ไม่พิสูจน์ว่าตอบ action ครบ

Mode: `pipeline:competition_rule_detail_source`; confidence: `0.97`; route: `{"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "complete source clauses for explicit requested propositions"}`

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
        "roster"
      ],
      "source_ids": [
        "competition_rules_cs2_psu_phuket_2026_s18_c01"
      ],
      "validation_errors": [],
      "outcome": "answer",
      "reasons": []
    }
  },
  {
    "stage": "competition_source_grounding",
    "decision": "detail_clauses_covered",
    "confidence": 0.97,
    "detail": "supported clauses retained; source gaps/conflicts explicitly reported",
    "metadata": {
      "concepts": [
        "roster"
      ],
      "source_ids": [
        "competition_rules_cs2_psu_phuket_2026_s18_c01"
      ],
      "outcome": "answer",
      "reasons": []
    }
  }
]
```

Expected/trace/hits ทั้งหมดเก็บใน CONFIRMED_REMAINING_CASES.json

## เทคเคนแต่ละเกมแข่งกี่รอบ

ประเภท: ชื่อเกมย่อและ facet จำนวนรอบยังไม่ผูก literal settings

คำตอบจริง:

คำตอบ: กติกาการแข่งขัน

รายละเอียดที่เกี่ยวข้อง:
•    ใช้เครื่องเกม PlayStation 5
•    แข่งขันแบบ เดี่ยว (1v1)

อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ
แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

ควรตอบ: ควรยืนยันว่าเป็น Tekken 8 แล้วอ้าง settings จำนวนรอบต่อเกม 3 รอบ หากเป้าหมายยังไม่ชัดให้ถาม ไม่ส่งหัวข้อกติกา/แพลตฟอร์มแทน

สาเหตุและคะแนน: target resolver ยึดชื่อ registered edition; fallback ยังเลือก source กว้างและใช้หัวข้อ/รูปแบบนำหน้า ไม่มี proposition count ที่บังคับ source clause 3 รอบ ทุกกรณี

Mode: `pipeline:competition_source_rag`; confidence: `0.84`; route: `{"category": "competition_rules", "intent": "competition_rules_lookup", "confidence": 0.97, "answer_type": "fact", "risk": "medium", "reason": "competition rule terms found before reservation/check-in; operation_first=competition_rule_lookup"}`

Trace ที่เกี่ยวข้อง:

```json
[
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
    "stage": "universal_intent",
    "decision": "competition_rules/rule_lookup",
    "confidence": 0.9,
    "detail": "known game alias found; competition route overrides game/count ambiguity; count terms found; competition route forces rule lookup",
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
        "score": 0.0779,
        "language": "mixed",
        "language_quality": 0.9221,
        "should_review_intent": false,
        "reason": "Thai character n-gram quality=0.922",
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
          "confidence": 0.74,
          "reason": "domain keyword score=2"
        },
        {
          "id": "c5",
          "domain": "reservation",
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
        "reason": "known game alias found; competition route overrides game/count ambiguity; count terms found; competition route forces rule lookup"
      }
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

Expected/trace/hits ทั้งหมดเก็บใน CONFIRMED_REMAINING_CASES.json

## Flow แก้ร่วม

1. ให้ parser ส่ง target/edition/scope ไปทุก proposition ก่อน split และล็อกข้อที่ยังอ้างถึงเกมเดียวกัน
2. ใช้ action + qualifier เวลา + negation เป็นตัวเลือก concept ก่อน noun ทั่วไป/สถานที่
3. เพิ่ม target-bound implicit permission signals และ negative controls เรื่อง gameplay/catalog/ราคา/จอง
4. Validator ต้องตรวจว่าคำตอบแรกและข้อเสริมครอบคลุมทุก proposition ไม่ใช้ source ID/count เป็นตัวแทน
5. Oracle ใหม่อ้าง clause/source hash แบบ overlay แยกจาก frozen Gold; ไทย/อังกฤษใช้ semantic contract เดียวกัน
6. ตรวจชุดยากเก่าทั้ง 861 grades, strong content/composition 728 และทุก corpus; diff ก่อน/หลังและเก็บข้อผิดแยก

รายละเอียดลำดับรวมและ owner questions อยู่ใน docs/130_full_improvement_r30_flow_20261002.md
