# Canonical Competition Rule Format

โฟลเดอร์นี้เป็น **canonical layer** ของกติกาการแข่งขัน: เก็บกติกาเดิมในรูปแบบกลางที่อ่านได้เหมือนกันทุกเกม โดยไม่แทนที่ source chunks หรือ fact cards ที่ runtime ปัจจุบันใช้.

## ไฟล์

- `rulebook_registry.jsonl` - metadata ระดับเอกสาร/รายการแข่งขัน
- `competition_rule_releases.jsonl` - release lifecycle, approval และ eligibility ของแต่ละ rulebook
- `competition_rule_records.jsonl` - กติกาแต่ละส่วนจาก RAG chunks พร้อม conditions, rule type และ source locator
- `competition_rule_fact_projections.jsonl` - คำตอบ structured พร้อม evidence links และสถานะการตรวจหลักฐาน
- `competition_rule_rag_projections.jsonl` - text สำหรับ RAG ที่เติมชื่อเกม รายการ และบริบทให้ครบ
- `en_localization_review_queue.jsonl` - รายการข้อความที่ยังต้องมี English localization ที่อนุมัติแล้ว
- `active_release_manifest.json` - release ที่ Runtime อนุญาตให้อ่านได้
- `release_overrides.jsonl` และ `release_override_template.json` - owner-controlled approval/effective date overlay
- `competition_rule_coverage.json` และ `competition_rule_coverage_report.md` - ความครอบคลุมและรายการที่ต้องตรวจ
- `competition_rule_submission_template.json` - แบบฟอร์มเพิ่ม rulebook ใหม่ พร้อม common sections และ optional modules

## Schema กลาง

ทุก Rule Record มี `rulebook_id`, `game_id`, `scope`, `canonical_section`, `module`, `facet`, `rule_type`, `conditions`, `content_th`, source locator และ hash ของข้อความต้นทาง. หัวข้อกลางมี 10 ส่วน: `rulebook_identity`, `eligibility_registration`, `competition_format`, `match_configuration`, `pre_match_on_site`, `in_match_operations`, `fair_play_conduct`, `penalty_matrix`, `protest_dispute`, และ `references_change_history`.

`module=common` ใช้ซ้ำได้ทุกเกม ส่วน module อื่นเป็น optional game-specific module เช่น map veto ของ CS2 หรือ Hero/Skin ของ RoV. ห้ามสร้าง runtime route ตามชื่อเกม; route ควรเลือก `competition_rules` แล้ว filter จาก `game_id`, `canonical_section`, `module`, `facet`, conditions, วันที่มีผล และ source trust.

## สถานะและการ publish

ข้อมูลที่ย้ายจาก runtime เดิมถูกติดสถานะ `migrated_from_existing_content` และ `pending_owner_review` เพื่อไม่อ้างว่าได้รับ human approval ใหม่. Release จะเป็น `runtime_eligible` ได้ก็ต่อเมื่อ owner approval มี source hash ที่ตรงกัน, มี `effective_from` และตั้ง `activation_status=active` ใน `release_overrides.jsonl`. ถ้า source เปลี่ยน hash จะไม่สามารถ publish ต่อได้จนกว่าจะ review ใหม่. Structured facts และ RAG chunks ต้องใช้ active release/version เดียวกันและสลับพร้อมกัน.

Fact card ที่ไม่ได้มีข้อความตรงกับ source chunk จะถูกติด `candidate_review_required` หรือ `document_level_only`; ห้ามตีความว่าเป็นหลักฐานยืนยันจนกว่าจะ review.

## สร้าง/ตรวจ

```powershell
py -3 tools/build_competition_rule_canonical.py --write
py -3 tools/build_competition_rule_canonical.py --check
```
