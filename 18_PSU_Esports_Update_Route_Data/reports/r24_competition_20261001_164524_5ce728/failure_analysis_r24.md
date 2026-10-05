# รายละเอียดเคสที่ตกในการทดสอบ r24

เก็บคำตอบจริงจากการรันไว้ครบใน JSONL เดิม เอกสารนี้เพิ่มคำอธิบายโดยไม่แก้ผลเก่า

## รอบ B: 37 เคสที่ตกและทดสอบซ้ำ C ผ่าน

### R24-TH-rov-173

- คำถาม: สอบถามหน่อยครับ กติกา RoV เรื่องการหลุดจากเกมหรือการเชื่อมต่อ ว่าอย่างไร ครับ
- คาดหวัง: answer / rov / disconnect
- ตอบจริงรอบ B: `pipeline:game_meta_clarification` — ถามเรื่องเกมได้ครับ แต่คำถามนี้ยังกว้างเกินไป เลยไม่ขอดึงเกมใดเกมหนึ่งมาตอบแทน  ตัวอย่างที่ถามได้: •    `มีเกมอะไรบ้าง` •    `PS5 มีเกมอะไรบ้าง` •    `TEKKEN 8 คือเกมอะไร` •    `TEKKEN 8 มีปุ่มอะไรบ้าง` •    `Nintendo Switch มีเกมแนวปาร์ตี้ไหม`
- เงื่อนไขที่ตก: outcome_mismatch, route_mismatch, missing_target_evidence, wrong_facet_evidence, answer_without_substantive_source_content
- วิเคราะห์: ตัวกรองคำถามเกมทั่วไปทำงานก่อนกติกา แม้มีชื่อเกมและหัวข้อการแข่งขันครบ; เพิ่มเงื่อนไข competition signal ก่อนตัวกรอง
- ทดสอบซ้ำ C: ผ่าน / `pipeline:competition_source_rag`
- คำตอบหลังแก้: คำตอบ: 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ  รายละเอียดที่เกี่ยวข้อง: •    4.3.4.หากเกิดการ First Blood ขึ้นแล้ว หรือเริ่มเกมไปแล้วเกินกว่า 2 นาทีในเกม ห้ามไม่ให้ผู้เข้าแข่งขันทั้งสองฝ่ายขอเริ่มเกมใหม่ เว้นแต่ได้รับการอนุญาตจากคู่แข่ง และ/หรือตามเห็นสมควรจากกรรมการ •    4.3.5.หากพบหลักฐานว่าผู้เข้าแข่งขันคนใดเจตนากดหยุดเกม ไม่ว่าจะในจังหวะสำคัญ หรือเพื่อการก่อกวน ปรับแพ้ในเกมที่พบการกระทำผิดในทันที และตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที •    4.4.3.พัก 5 นาที หลังจากจบทุกสองเกม •    4.5.1.1. หากผู้เข้าแข่งขันคนใดจงใจไม่เชื่อมต่อเกม โดยไม่แจ้งให้ผู้ตัดสินทราบ ผู้ตัดสินมีสิทธิไม่อนุมัติคำขอหยุดเกมนั้น ๆ •    4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพินิจของกรรมการ ว่าจะเห็นสมควรให้แข่งขันใหม่หรือไม่  อ้างอิงจากกติกา: Arena of 

### R24-TH-rov-175

- คำถาม: สอบถามหน่อยครับ ขออ้างอิงกติกา อารีน่าออฟเวเลอร์ ในหัวข้อการหลุดจากเกมหรือการเชื่อมต่อ หน่อย ครับ
- คาดหวัง: answer / rov / disconnect
- ตอบจริงรอบ B: `pipeline:game_meta_clarification` — ถามเรื่องเกมได้ครับ แต่คำถามนี้ยังกว้างเกินไป เลยไม่ขอดึงเกมใดเกมหนึ่งมาตอบแทน  ตัวอย่างที่ถามได้: •    `มีเกมอะไรบ้าง` •    `PS5 มีเกมอะไรบ้าง` •    `TEKKEN 8 คือเกมอะไร` •    `TEKKEN 8 มีปุ่มอะไรบ้าง` •    `Nintendo Switch มีเกมแนวปาร์ตี้ไหม`
- เงื่อนไขที่ตก: outcome_mismatch, route_mismatch, missing_target_evidence, wrong_facet_evidence, answer_without_substantive_source_content
- วิเคราะห์: ตัวกรองคำถามเกมทั่วไปทำงานก่อนกติกา แม้มีชื่อเกมและหัวข้อการแข่งขันครบ; เพิ่มเงื่อนไข competition signal ก่อนตัวกรอง
- ทดสอบซ้ำ C: ผ่าน / `pipeline:competition_source_rag`
- คำตอบหลังแก้: คำตอบ: 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ  รายละเอียดที่เกี่ยวข้อง: •    4.3.4.หากเกิดการ First Blood ขึ้นแล้ว หรือเริ่มเกมไปแล้วเกินกว่า 2 นาทีในเกม ห้ามไม่ให้ผู้เข้าแข่งขันทั้งสองฝ่ายขอเริ่มเกมใหม่ เว้นแต่ได้รับการอนุญาตจากคู่แข่ง และ/หรือตามเห็นสมควรจากกรรมการ •    4.3.5.หากพบหลักฐานว่าผู้เข้าแข่งขันคนใดเจตนากดหยุดเกม ไม่ว่าจะในจังหวะสำคัญ หรือเพื่อการก่อกวน ปรับแพ้ในเกมที่พบการกระทำผิดในทันที และตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที •    4.4.3.พัก 5 นาที หลังจากจบทุกสองเกม •    4.5.1.1. หากผู้เข้าแข่งขันคนใดจงใจไม่เชื่อมต่อเกม โดยไม่แจ้งให้ผู้ตัดสินทราบ ผู้ตัดสินมีสิทธิไม่อนุมัติคำขอหยุดเกมนั้น ๆ •    4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพินิจของกรรมการ ว่าจะเห็นสมควรให้แข่งขันใหม่หรือไม่  อ้างอิงจากกติกา: Arena of 

### R24-TH-rov-176

- คำถาม: สอบถามหน่อยครับ กำลังจะลงแข่ง RoV อยากรู้เรื่องการหลุดจากเกมหรือการเชื่อมต่อ ครับ
- คาดหวัง: answer / rov / disconnect
- ตอบจริงรอบ B: `pipeline:game_meta_clarification` — ถามเรื่องเกมได้ครับ แต่คำถามนี้ยังกว้างเกินไป เลยไม่ขอดึงเกมใดเกมหนึ่งมาตอบแทน  ตัวอย่างที่ถามได้: •    `มีเกมอะไรบ้าง` •    `PS5 มีเกมอะไรบ้าง` •    `TEKKEN 8 คือเกมอะไร` •    `TEKKEN 8 มีปุ่มอะไรบ้าง` •    `Nintendo Switch มีเกมแนวปาร์ตี้ไหม`
- เงื่อนไขที่ตก: outcome_mismatch, route_mismatch, missing_target_evidence, wrong_facet_evidence, answer_without_substantive_source_content
- วิเคราะห์: ตัวกรองคำถามเกมทั่วไปทำงานก่อนกติกา แม้มีชื่อเกมและหัวข้อการแข่งขันครบ; เพิ่มเงื่อนไข competition signal ก่อนตัวกรอง
- ทดสอบซ้ำ C: ผ่าน / `pipeline:competition_source_rag`
- คำตอบหลังแก้: คำตอบ: 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ  รายละเอียดที่เกี่ยวข้อง: •    4.3.4.หากเกิดการ First Blood ขึ้นแล้ว หรือเริ่มเกมไปแล้วเกินกว่า 2 นาทีในเกม ห้ามไม่ให้ผู้เข้าแข่งขันทั้งสองฝ่ายขอเริ่มเกมใหม่ เว้นแต่ได้รับการอนุญาตจากคู่แข่ง และ/หรือตามเห็นสมควรจากกรรมการ •    4.4.3.พัก 5 นาที หลังจากจบทุกสองเกม •    4.5.1.1. หากผู้เข้าแข่งขันคนใดจงใจไม่เชื่อมต่อเกม โดยไม่แจ้งให้ผู้ตัดสินทราบ ผู้ตัดสินมีสิทธิไม่อนุมัติคำขอหยุดเกมนั้น ๆ •    4.3.2.หากผู้เข้าแข่งขันหลุดด้วยเหตุผลอื่น ๆ ที่เป็นเหตุสุดวิสัย (เช่นเครือข่ายผู้ให้บริการอินเตอร์เน็ตล่มทั้งบริเวณ หรือเกิดข้อผิดพลาดจากเซิร์ฟเวอร์ของเกม) ทางทีมที่มีส่วนเสียหาย ต้องแจ้งทีมงาน และขึ้นอยู่กับดุลยพินิจของกรรมการ ว่าจะเห็นสมควรให้แข่งขันใหม่หรือไม่ •    4.2.1.ผู้เข้าแข่งขันทุกคนต้องมีฮีโร่อย่างน้อย 18 ตัว สำหรับการเข้าแข่งขันในโหมด “การแข่งขัน 5v5” (ชื่อเดิม Tournament Mode)  อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ประเภททีมชาย แหล่งข้อมูล: local:/

### R24-TH-rov-178

- คำถาม: สอบถามหน่อยครับ ตาม rulebook อารีน่าออฟเวเลอร์ การหลุดจากเกมหรือการเชื่อมต่อ ต้องทำยังไง ครับ
- คาดหวัง: answer / rov / disconnect
- ตอบจริงรอบ B: `pipeline:game_meta_clarification` — ถามเรื่องเกมได้ครับ แต่คำถามนี้ยังกว้างเกินไป เลยไม่ขอดึงเกมใดเกมหนึ่งมาตอบแทน  ตัวอย่างที่ถามได้: •    `มีเกมอะไรบ้าง` •    `PS5 มีเกมอะไรบ้าง` •    `TEKKEN 8 คือเกมอะไร` •    `TEKKEN 8 มีปุ่มอะไรบ้าง` •    `Nintendo Switch มีเกมแนวปาร์ตี้ไหม`
- เงื่อนไขที่ตก: outcome_mismatch, route_mismatch, missing_target_evidence, wrong_facet_evidence, answer_without_substantive_source_content
- วิเคราะห์: ตัวกรองคำถามเกมทั่วไปทำงานก่อนกติกา แม้มีชื่อเกมและหัวข้อการแข่งขันครบ; เพิ่มเงื่อนไข competition signal ก่อนตัวกรอง
- ทดสอบซ้ำ C: ผ่าน / `pipeline:competition_source_rag`
- คำตอบหลังแก้: คำตอบ: 4.3.1.ในกรณีที่มีผู้เข้าแข่งขันหลุดออกจากเกม ให้ทำการหยุดเกมชั่วคราว โดยแต่ละทีมสามารถกดหยุดเกมได้ทีมละ 5 ครั้ง ครั้งละไม่เกิน 1 นาที ถ้าหากเกินเวลาดังกล่าว อีกทีมสามารถกด Resume ได้ทันทีและทำการแข่งขันต่อตามปกติ  รายละเอียดที่เกี่ยวข้อง: •    4.3.3.ในกรณีที่ยังไม่มี First Blood และเวลาในเกมยังไม่เกิน 2 นาที ทีมที่ผู้เข้าแข่งขันหลุดสามารถแจ้งอีกทีมหนึ่งเพื่อขอเริ่มเกมใหม่ได้ทันที โดยผู้เข้าแข่งขันทุกคนจะต้องเลือกฮีโร่และตำแหน่งการเล่นเหมือนเกมแรกก่อนมีการขอเริ่มเกมใหม่ •    4.3.4.หากเกิดการ First Blood ขึ้นแล้ว หรือเริ่มเกมไปแล้วเกินกว่า 2 นาทีในเกม ห้ามไม่ให้ผู้เข้าแข่งขันทั้งสองฝ่ายขอเริ่มเกมใหม่ เว้นแต่ได้รับการอนุญาตจากคู่แข่ง และ/หรือตามเห็นสมควรจากกรรมการ •    4.3.5.หากพบหลักฐานว่าผู้เข้าแข่งขันคนใดเจตนากดหยุดเกม ไม่ว่าจะในจังหวะสำคัญ หรือเพื่อการก่อกวน ปรับแพ้ในเกมที่พบการกระทำผิดในทันที และตัดสิทธิ์ทีมผู้เข้าแข่งขันดังกล่าวออกจากการแข่งขันทันที •    4.4.3.พัก 5 นาที หลังจากจบทุกสองเกม •    4.5.1.1. หากผู้เข้าแข่งขันคนใดจงใจไม่เชื่อมต่อเกม โดยไม่แจ้งให้ผู้ตัดสินทราบ ผู้ตัดสินมีสิทธิไม่อนุมัติคำขอหยุดเกมนั้น ๆ  อ้างอิงจากกติกา: Arena of Valor (RoV) / Blueket Games 2025 ป

### R24-TH-tekken8-169

- คำถาม: สอบถามหน่อยครับ ขออ้างอิงกติกา เทคเค่น 8 ในหัวข้อการตั้งค่าในเกม หน่อย ครับ
- คาดหวัง: answer / tekken8 / match_settings
- ตอบจริงรอบ B: `pipeline:game_meta_clarification` — ถามเรื่องเกมได้ครับ แต่คำถามนี้ยังกว้างเกินไป เลยไม่ขอดึงเกมใดเกมหนึ่งมาตอบแทน  ตัวอย่างที่ถามได้: •    `มีเกมอะไรบ้าง` •    `PS5 มีเกมอะไรบ้าง` •    `TEKKEN 8 คือเกมอะไร` •    `TEKKEN 8 มีปุ่มอะไรบ้าง` •    `Nintendo Switch มีเกมแนวปาร์ตี้ไหม`
- เงื่อนไขที่ตก: outcome_mismatch, route_mismatch, missing_target_evidence, wrong_facet_evidence, answer_without_substantive_source_content
- วิเคราะห์: ตัวกรองคำถามเกมทั่วไปทำงานก่อนกติกา แม้มีชื่อเกมและหัวข้อการแข่งขันครบ; เพิ่มเงื่อนไข competition signal ก่อนตัวกรอง
- ทดสอบซ้ำ C: ผ่าน / `pipeline:competition_source_rag`
- คำตอบหลังแก้: คำตอบ: * จำนวนรอบต่อเกม (Round): 3  รายละเอียดที่เกี่ยวข้อง: •    เวลาแข่งขันต่อรอบ (Timer): 60 วินาที •    การตั้งค่าเกม  อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-TH-tekken8-172

- คำถาม: สอบถามหน่อยครับ ตาม rulebook เทคเค่น 8 การตั้งค่าในเกม ต้องทำยังไง ครับ
- คาดหวัง: answer / tekken8 / match_settings
- ตอบจริงรอบ B: `pipeline:game_meta_clarification` — ถามเรื่องเกมได้ครับ แต่คำถามนี้ยังกว้างเกินไป เลยไม่ขอดึงเกมใดเกมหนึ่งมาตอบแทน  ตัวอย่างที่ถามได้: •    `มีเกมอะไรบ้าง` •    `PS5 มีเกมอะไรบ้าง` •    `TEKKEN 8 คือเกมอะไร` •    `TEKKEN 8 มีปุ่มอะไรบ้าง` •    `Nintendo Switch มีเกมแนวปาร์ตี้ไหม`
- เงื่อนไขที่ตก: outcome_mismatch, route_mismatch, missing_target_evidence, wrong_facet_evidence, answer_without_substantive_source_content
- วิเคราะห์: ตัวกรองคำถามเกมทั่วไปทำงานก่อนกติกา แม้มีชื่อเกมและหัวข้อการแข่งขันครบ; เพิ่มเงื่อนไข competition signal ก่อนตัวกรอง
- ทดสอบซ้ำ C: ผ่าน / `pipeline:competition_source_rag`
- คำตอบหลังแก้: คำตอบ: * จำนวนรอบต่อเกม (Round): 3  รายละเอียดที่เกี่ยวข้อง: •    เวลาแข่งขันต่อรอบ (Timer): 60 วินาที •    การตั้งค่าเกม  อ้างอิงจากกติกา: Tekken 8 / PSU Esports ปะทะมันส์ สนั่นจอ แหล่งข้อมูล: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-TH-SAFE-013

- คำถาม: อยากทราบว่า กติกกา timeout เป็นยังไง ครับ
- คาดหวัง: clarification /  / ต้องระบุเกม
- ตอบจริงรอบ B: `pipeline:experimental_rag_no_context` — ยังไม่พบข้อมูลที่ยืนยันคำตอบเรื่องนี้ได้ชัดในหมวด ภาพรวม/ข้อมูลทั่วไป ครับ กรุณาระบุคำถามให้เจาะจงขึ้น หรือตรวจสอบกับศูนย์โดยตรงครับ
- เงื่อนไขที่ตก: outcome_mismatch, route_mismatch
- วิเคราะห์: คำว่า กติกกา ไม่ฟื้นเป็น กติกา เมื่อไม่มีชื่อเกม; ฟื้น cue เฉพาะเมื่อมี timeout/การแข่งขัน แล้วถามให้ระบุเกม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:competition_target_clarification`
- คำตอบหลังแก้: ต้องการดูกติกาของเกมใดครับ เช่น Counter-Strike 2, RoV, Tekken 8 หรือ VALORANT

### R24-EN-tekken8-041

- คำถาม: What do the TEKKEN 8 tournament rules say about the rulebook scope and tournament identity?
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:competition_source_localization_pending_en` — Verified Tekken 8 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition_rules_tekken8_psu_esports
- เงื่อนไขที่ตก: outcome_mismatch
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-042

- คำถาม: For Tekken 8, can you verify the rule on the rulebook scope and tournament identity?
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:competition_source_localization_pending_en` — Verified Tekken 8 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition_rules_tekken8_psu_esports
- เงื่อนไขที่ตก: outcome_mismatch
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-043

- คำถาม: I am preparing for a T8 match. What is the policy for the rulebook scope and tournament identity?
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:missing_english_localization` — This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation. Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- เงื่อนไขที่ตก: outcome_mismatch, missing_target_evidence, wrong_facet_evidence
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-044

- คำถาม: Please retrieve the official TEKKEN 8 rulebook evidence for the rulebook scope and tournament identity.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:competition_source_localization_pending_en` — Verified Tekken 8 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition_rules_tekken8_psu_esports
- เงื่อนไขที่ตก: outcome_mismatch
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-045

- คำถาม: How is the rulebook scope and tournament identity handled in the Tekken 8 tournament rules?
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:competition_source_localization_pending_en` — Verified Tekken 8 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition_rules_tekken8_psu_esports
- เงื่อนไขที่ตก: outcome_mismatch
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-046

- คำถาม: Could you cite the T8 rule concerning the rulebook scope and tournament identity?
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:missing_english_localization` — This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation. Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- เงื่อนไขที่ตก: outcome_mismatch, missing_target_evidence, wrong_facet_evidence
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-087

- คำถาม: Please check: What do the TEKKEN 8 tournament ruls say about the rulebook scope and tournament identity? please.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:competition_source_localization_pending_en` — Verified Tekken 8 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition_rules_tekken8_psu_esports
- เงื่อนไขที่ตก: outcome_mismatch
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-088

- คำถาม: Please check: For Tekken 8, can you verify the rule on the rulebook scope and tournament identity? please.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:competition_source_localization_pending_en` — Verified Tekken 8 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition_rules_tekken8_psu_esports
- เงื่อนไขที่ตก: outcome_mismatch
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-089

- คำถาม: Please check: I am preparing for a T8 match. What is the policy for the rulebook scope and tournament identity? please.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:missing_english_localization` — This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation. Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- เงื่อนไขที่ตก: outcome_mismatch, missing_target_evidence, wrong_facet_evidence
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-090

- คำถาม: Please check: Please retrieve the official TEKKEN 8 rulebook evidence for the rulebook scope and tournament identity. please.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:competition_source_localization_pending_en` — Verified Tekken 8 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition_rules_tekken8_psu_esports
- เงื่อนไขที่ตก: outcome_mismatch
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-091

- คำถาม: Please check: How is the rulebook scope and tournament identity handled in the Tekken 8 tournament ruls? please.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:competition_source_localization_pending_en` — Verified Tekken 8 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition_rules_tekken8_psu_esports
- เงื่อนไขที่ตก: outcome_mismatch
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-092

- คำถาม: Please check: Could you cite the T8 rule concerning the rulebook scope and tournament identity? please.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:missing_english_localization` — This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation. Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- เงื่อนไขที่ตก: outcome_mismatch, missing_target_evidence, wrong_facet_evidence
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-133

- คำถาม: Could you explain: What do the TEKKEN 8 tournament rules say about the rulebook scope and tournament identity? please.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:competition_source_localization_pending_en` — Verified Tekken 8 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition_rules_tekken8_psu_esports
- เงื่อนไขที่ตก: outcome_mismatch
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-134

- คำถาม: Could you explain: For Tekken 8, can you verify the rule on the rulebook scope and tournament identity? please.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:competition_source_localization_pending_en` — Verified Tekken 8 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition_rules_tekken8_psu_esports
- เงื่อนไขที่ตก: outcome_mismatch
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-135

- คำถาม: Could you explain: I am preparing for a T8 match. What is the policy for the rulebook scope and tournament identity? please.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:missing_english_localization` — This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation. Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- เงื่อนไขที่ตก: outcome_mismatch, missing_target_evidence, wrong_facet_evidence
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-136

- คำถาม: Could you explain: Please retrieve the official TEKKEN 8 rulebook evidence for the rulebook scope and tournament identity. please.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:competition_source_localization_pending_en` — Verified Tekken 8 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition_rules_tekken8_psu_esports
- เงื่อนไขที่ตก: outcome_mismatch
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-137

- คำถาม: Could you explain: How is the rulebook scope and tournament identity handled in the Tekken 8 tournament rules? please.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:competition_source_localization_pending_en` — Verified Tekken 8 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition_rules_tekken8_psu_esports
- เงื่อนไขที่ตก: outcome_mismatch
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-138

- คำถาม: Could you explain: Could you cite the T8 rule concerning the rulebook scope and tournament identity? please.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:missing_english_localization` — This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation. Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- เงื่อนไขที่ตก: outcome_mismatch, missing_target_evidence, wrong_facet_evidence
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-179

- คำถาม: I would like to know: What do the TEKKEN 8 tournamet rules say about the rulebook scope and tournament identity? please.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:competition_source_localization_pending_en` — Verified Tekken 8 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition_rules_tekken8_psu_esports
- เงื่อนไขที่ตก: outcome_mismatch
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-180

- คำถาม: I would like to know: For Tekken 8, can you verify the rule on the rulebook scope and tournamet identity? please.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:competition_source_localization_pending_en` — Verified Tekken 8 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition_rules_tekken8_psu_esports
- เงื่อนไขที่ตก: outcome_mismatch
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-181

- คำถาม: I would like to know: I am preparing for a T8 match. What is the policy for the rulebook scope and tournamet identity? please.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:missing_english_localization` — This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation. Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- เงื่อนไขที่ตก: outcome_mismatch, missing_target_evidence, wrong_facet_evidence
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-182

- คำถาม: I would like to know: Please retrieve the official TEKKEN 8 rulebook evidence for the rulebook scope and tournamet identity. please.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:competition_source_localization_pending_en` — Verified Tekken 8 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition_rules_tekken8_psu_esports
- เงื่อนไขที่ตก: outcome_mismatch
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-183

- คำถาม: I would like to know: How is the rulebook scope and tournamet identity handled in the Tekken 8 tournament rules? please.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:competition_source_localization_pending_en` — Verified Tekken 8 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition_rules_tekken8_psu_esports
- เงื่อนไขที่ตก: outcome_mismatch
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-184

- คำถาม: I would like to know: Could you cite the T8 rule concerning the rulebook scope and tournamet identity? please.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:missing_english_localization` — This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation. Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- เงื่อนไขที่ตก: outcome_mismatch, missing_target_evidence, wrong_facet_evidence
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-225

- คำถาม: Please tell me: What do the TEKKEN 8 tournament ruules say about the rulebook scope and tournament identity? please.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:competition_source_localization_pending_en` — Verified Tekken 8 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition_rules_tekken8_psu_esports
- เงื่อนไขที่ตก: outcome_mismatch
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-226

- คำถาม: Please tell me: For Tekken 8, can you verify the rule on the rulebook scope and tournament identity? please.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:competition_source_localization_pending_en` — Verified Tekken 8 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition_rules_tekken8_psu_esports
- เงื่อนไขที่ตก: outcome_mismatch
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-227

- คำถาม: Please tell me: I am preparing for a T8 match. What is the policy for the rulebook scope and tournament identity? please.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:missing_english_localization` — This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation. Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- เงื่อนไขที่ตก: outcome_mismatch, missing_target_evidence, wrong_facet_evidence
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-228

- คำถาม: Please tell me: Please retrieve the official TEKKEN 8 rulebook evidence for the rulebook scope and tournament identity. please.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:competition_source_localization_pending_en` — Verified Tekken 8 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition_rules_tekken8_psu_esports
- เงื่อนไขที่ตก: outcome_mismatch
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-229

- คำถาม: Please tell me: How is the rulebook scope and tournament identity handled in the Tekken 8 tournament ruules? please.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:competition_source_localization_pending_en` — Verified Tekken 8 competition-rule evidence was found in the original Thai source for this topic. An approved English wording is not available yet, so I will not translate the rule live. Original source in Thai: local://competition_rules/competition_rules_tekken8_psu_esports
- เงื่อนไขที่ตก: outcome_mismatch
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

### R24-EN-tekken8-230

- คำถาม: Please tell me: Could you cite the T8 rule concerning the rulebook scope and tournament identity? please.
- คาดหวัง: answer / tekken8 / rulebook_identity
- ตอบจริงรอบ B: `pipeline:missing_english_localization` — This information does not yet have an approved English localization. Please open the cited original source or ask a staff member for confirmation. Source: https://esports.computing.psu.ac.th/ (original source in Thai)
- เงื่อนไขที่ตก: outcome_mismatch, missing_target_evidence, wrong_facet_evidence
- วิเคราะห์: ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม
- ทดสอบซ้ำ C: ผ่าน / `pipeline:structured_competition_rules_en`
- คำตอบหลังแก้: Verified Tekken 8 competition rules: - Document overview: Competition rules and format for Tekken 8. Event: PSU Esports 'Thrilling Showdown on Screen' (an English rendering of the Thai event title). Source: local://competition_rules/competition_rules_tekken8_psu_esports

## รอบ A: เคสที่ตกตาม rubric เดิม 180 เคส

หลายสาเหตุอาจเกิดร่วมกันในเคสเดียว; คอลัมน์วิเคราะห์เป็นการจัดกลุ่มเบื้องต้น ต้องอ่าน trace เพื่อยืนยันข้อสรุปรายเคส

| ID | คำถาม | Mode | เหตุที่ตก | วิเคราะห์ |
|---|---|---|---|---|
| R24-TH-cs2-082 | ตาม rulebook เคาน์เตอร์สไตรก์ 2 ตารางบทลงโทษ ต้องทำยังไง | pipeline:protected_booking_window | route_mismatch, missing_target_evidence, wrong_facet_evidence, answer_without_substantive_source_content | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-TH-cs2-112 | ตาม rulebook เคาน์เตอร์สไตรก์ 2 ตารางและเวลาแข่งขัน ต้องทำยังไง | pipeline:protected_booking_window | route_mismatch, missing_target_evidence, wrong_facet_evidence, answer_without_substantive_source_content | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-TH-cs2-200 | ช่วยดูหน่อย ตาม rulebook เคาน์เตอร์สไตรก์ 2 ตารางบทลงโทษ ต้องทำยังไง ครับ | pipeline:protected_booking_window | route_mismatch, missing_target_evidence, wrong_facet_evidence, answer_without_substantive_source_content | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-TH-cs2-230 | ช่วยดูหน่อย ตาม rulebook เคาน์เตอร์สไตรก์ 2 ตารางและเวลาแข่งขัน ต้องทำยังไง ครับ | pipeline:protected_booking_window | route_mismatch, missing_target_evidence, wrong_facet_evidence, answer_without_substantive_source_content | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-TH-cs2-238 | อยากทราบว่า กติกกา cs2 มีอะไรบ้าง ครับ | pipeline:structured_games_catalog | route_mismatch, missing_target_evidence, overview_without_multiple_rule_clauses | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-TH-cs2-239 | อยากทราบว่า สรุปกฎการแข่งขัน cs2 ทั้งหมด ครับ | pipeline:competition_fact_card_comparison | foreign_game_evidence, overview_without_multiple_rule_clauses | พบหลักฐานเกมอื่น; trace แสดงการขยายชื่อเกม/การเปรียบเทียบ ต้องยึด explicit target เดิมและใช้ query แยกแต่ละเกม |
| R24-TH-rov-054 | ไปถึงหน้างานแข่ง RoV แล้วต้องเช็กอินหรือรายงานตัวตามขั้นตอนอะไรบ้าง | pipeline:protected_checkin_required | outcome_mismatch, route_mismatch | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-TH-rov-108 | ช่วยดูหน่อย ไปถึงหน้างานแข่ง RoV แล้วต้องเช็กอินหรือรายงานตัวตามขั้นตอนอะไรบ้าง ครับ | pipeline:protected_checkin_required | outcome_mismatch, route_mismatch | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-TH-rov-110 | อยากทราบว่า กติกกา rov มีอะไรบ้าง ครับ | pipeline:structured_games_catalog | route_mismatch, missing_target_evidence, overview_without_multiple_rule_clauses | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-TH-rov-111 | อยากทราบว่า สรุปกฎการแข่งขัน rov ทั้งหมด ครับ | pipeline:competition_fact_card_comparison | foreign_game_evidence, overview_without_multiple_rule_clauses | พบหลักฐานเกมอื่น; trace แสดงการขยายชื่อเกม/การเปรียบเทียบ ต้องยึด explicit target เดิมและใช้ query แยกแต่ละเกม |
| R24-TH-rov-162 | อยากทราบว่า ไปถึงหน้างานแข่ง RoV แล้วต้องเช็กอินหรือรายงานตัวตามขั้นตอนอะไรบ้าง ครับ | pipeline:protected_checkin_required | outcome_mismatch, route_mismatch | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-TH-rov-173 | สอบถามหน่อยครับ กติกา RoV เรื่องการหลุดจากเกมหรือการเชื่อมต่อ ว่าอย่างไร ครับ | pipeline:game_meta_clarification | outcome_mismatch, route_mismatch, missing_target_evidence, wrong_facet_evidence, answer_without_substantive_source_content | ตัวกรองคำถามเกมทั่วไปทำงานก่อนกติกา แม้มีชื่อเกมและหัวข้อการแข่งขันครบ; เพิ่มเงื่อนไข competition signal ก่อนตัวกรอง |
| R24-TH-rov-175 | สอบถามหน่อยครับ ขออ้างอิงกติกา อารีน่าออฟเวเลอร์ ในหัวข้อการหลุดจากเกมหรือการเชื่อมต่อ หน่อย ครับ | pipeline:game_meta_clarification | outcome_mismatch, route_mismatch, missing_target_evidence, wrong_facet_evidence, answer_without_substantive_source_content | ตัวกรองคำถามเกมทั่วไปทำงานก่อนกติกา แม้มีชื่อเกมและหัวข้อการแข่งขันครบ; เพิ่มเงื่อนไข competition signal ก่อนตัวกรอง |
| R24-TH-rov-176 | สอบถามหน่อยครับ กำลังจะลงแข่ง RoV อยากรู้เรื่องการหลุดจากเกมหรือการเชื่อมต่อ ครับ | pipeline:game_meta_clarification | outcome_mismatch, route_mismatch, missing_target_evidence, wrong_facet_evidence, answer_without_substantive_source_content | ตัวกรองคำถามเกมทั่วไปทำงานก่อนกติกา แม้มีชื่อเกมและหัวข้อการแข่งขันครบ; เพิ่มเงื่อนไข competition signal ก่อนตัวกรอง |
| R24-TH-rov-178 | สอบถามหน่อยครับ ตาม rulebook อารีน่าออฟเวเลอร์ การหลุดจากเกมหรือการเชื่อมต่อ ต้องทำยังไง ครับ | pipeline:game_meta_clarification | outcome_mismatch, route_mismatch, missing_target_evidence, wrong_facet_evidence, answer_without_substantive_source_content | ตัวกรองคำถามเกมทั่วไปทำงานก่อนกติกา แม้มีชื่อเกมและหัวข้อการแข่งขันครบ; เพิ่มเงื่อนไข competition signal ก่อนตัวกรอง |
| R24-TH-rov-216 | สอบถามหน่อยครับ ไปถึงหน้างานแข่ง RoV แล้วต้องเช็กอินหรือรายงานตัวตามขั้นตอนอะไรบ้าง ครับ | pipeline:protected_checkin_required | outcome_mismatch, route_mismatch | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-TH-tekken8-094 | อยากทราบว่า กติกกา tekken 8 มีอะไรบ้าง ครับ | pipeline:structured_games_catalog | route_mismatch, missing_target_evidence, overview_without_multiple_rule_clauses | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-TH-tekken8-095 | อยากทราบว่า สรุปกฎการแข่งขัน tekken 8 ทั้งหมด ครับ | pipeline:competition_fact_card_comparison | foreign_game_evidence, overview_without_multiple_rule_clauses | พบหลักฐานเกมอื่น; trace แสดงการขยายชื่อเกม/การเปรียบเทียบ ต้องยึด explicit target เดิมและใช้ query แยกแต่ละเกม |
| R24-TH-tekken8-169 | สอบถามหน่อยครับ ขออ้างอิงกติกา เทคเค่น 8 ในหัวข้อการตั้งค่าในเกม หน่อย ครับ | pipeline:game_meta_clarification | outcome_mismatch, route_mismatch, missing_target_evidence, wrong_facet_evidence, answer_without_substantive_source_content | ตัวกรองคำถามเกมทั่วไปทำงานก่อนกติกา แม้มีชื่อเกมและหัวข้อการแข่งขันครบ; เพิ่มเงื่อนไข competition signal ก่อนตัวกรอง |
| R24-TH-tekken8-172 | สอบถามหน่อยครับ ตาม rulebook เทคเค่น 8 การตั้งค่าในเกม ต้องทำยังไง ครับ | pipeline:game_meta_clarification | outcome_mismatch, route_mismatch, missing_target_evidence, wrong_facet_evidence, answer_without_substantive_source_content | ตัวกรองคำถามเกมทั่วไปทำงานก่อนกติกา แม้มีชื่อเกมและหัวข้อการแข่งขันครบ; เพิ่มเงื่อนไข competition signal ก่อนตัวกรอง |
| R24-TH-valorant-134 | อยากทราบว่า กติกกา วาโล มีอะไรบ้าง ครับ | pipeline:structured_games_catalog | route_mismatch, missing_target_evidence, overview_without_multiple_rule_clauses | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-TH-SAFE-005 | CS2 กับ VALORANT เรื่อง technical pause ต่างกันยังไง | pipeline:competition_fact_card_comparison | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-TH-SAFE-006 | RoV กับ Tekken 8 ถ้ากด pause ผิดมีผลยังไง | pipeline:competition_fact_card_comparison | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-TH-SAFE-011 | ช่วยดูหน่อย CS2 กับ VALORANT เรื่อง technical pause ต่างกันยังไง ครับ | pipeline:competition_fact_card_comparison | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-TH-SAFE-012 | ช่วยดูหน่อย RoV กับ Tekken 8 ถ้ากด pause ผิดมีผลยังไง ครับ | pipeline:competition_fact_card_comparison | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-TH-SAFE-013 | อยากทราบว่า กติกกา timeout เป็นยังไง ครับ | pipeline:experimental_rag_no_context | outcome_mismatch, route_mismatch | คำว่า กติกกา ไม่ฟื้นเป็น กติกา เมื่อไม่มีชื่อเกม; ฟื้น cue เฉพาะเมื่อมี timeout/การแข่งขัน แล้วถามให้ระบุเกม |
| R24-TH-SAFE-017 | อยากทราบว่า CS2 กับ VALORANT เรื่อง technical pause ต่างกันยังไง ครับ | pipeline:competition_fact_card_comparison | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-TH-SAFE-018 | อยากทราบว่า RoV กับ Tekken 8 ถ้ากด pause ผิดมีผลยังไง ครับ | pipeline:competition_fact_card_comparison | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-TH-SAFE-023 | สอบถามหน่อยครับ CS2 กับ VALORANT เรื่อง technical pause ต่างกันยังไง ครับ | pipeline:competition_fact_card_comparison | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-TH-SAFE-024 | สอบถามหน่อยครับ RoV กับ Tekken 8 ถ้ากด pause ผิดมีผลยังไง ครับ | pipeline:competition_fact_card_comparison | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-TH-SAFE-029 | ขอข้อมูล CS2 กับ VALORANT เรื่อง technical pause ต่างกันยังไง ครับ | pipeline:competition_fact_card_comparison | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-TH-SAFE-030 | ขอข้อมูล RoV กับ Tekken 8 ถ้ากด pause ผิดมีผลยังไง ครับ | pipeline:competition_fact_card_comparison | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-TH-SAFE-035 | ช่วยอธิบาย CS2 กับ VALORANT เรื่อง technical pause ต่างกันยังไง ครับ | pipeline:competition_fact_card_comparison | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-TH-SAFE-036 | ช่วยอธิบาย RoV กับ Tekken 8 ถ้ากด pause ผิดมีผลยังไง ครับ | pipeline:competition_fact_card_comparison | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-047 | What do the CS2 tournament rules say about maps, vetoes, and map selection? | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-048 | For Counter-Strike 2, can you verify the rule on maps, vetoes, and map selection? | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-049 | I am preparing for a Counter Strike 2 match. What is the policy for maps, vetoes, and map selection? | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-050 | Please retrieve the official CS2 rulebook evidence for maps, vetoes, and map selection. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-051 | How is maps, vetoes, and map selection handled in the Counter-Strike 2 tournament rules? | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-052 | Could you cite the Counter Strike 2 rule concerning maps, vetoes, and map selection? | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-059 | What do the CS2 tournament rules say about in-game settings? | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-060 | For Counter-Strike 2, can you verify the rule on in-game settings? | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-061 | I am preparing for a Counter Strike 2 match. What is the policy for in-game settings? | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-062 | Please retrieve the official CS2 rulebook evidence for in-game settings. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-063 | How is in-game settings handled in the Counter-Strike 2 tournament rules? | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-064 | Could you cite the Counter Strike 2 rule concerning in-game settings? | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-101 | What do the CS2 tournament rules say about the rulebook scope and tournament identity? | pipeline:competition_rule_overview_source | wrong_facet_evidence | เลือกหัวข้อไม่ตรงคำถามหรือไม่มี English เนื้อหาในแถวที่ตรง; จัด substantive candidates ก่อน headings |
| R24-EN-cs2-105 | How is the rulebook scope and tournament identity handled in the Counter-Strike 2 tournament rules? | pipeline:competition_rule_overview_source | wrong_facet_evidence | เลือกหัวข้อไม่ตรงคำถามหรือไม่มี English เนื้อหาในแถวที่ตรง; จัด substantive candidates ก่อน headings |
| R24-EN-cs2-110 | Please retrieve the official CS2 rulebook evidence for the tournament schedule. | pipeline:protected_booking_window | route_mismatch, missing_target_evidence, wrong_facet_evidence, answer_without_substantive_source_content | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-EN-cs2-119 | Please check: What are the cs2 tournament ruls? please. | pipeline:structured_competition_rules_en | overview_without_multiple_rule_clauses | คำถามรวมได้หลักฐานหลายหัวข้อแต่ไม่มีข้อความกติกาจริงครบ; ใช้ selected substantive overview ของเกมที่ระบุ |
| R24-EN-cs2-120 | Please check: What ruls apply to the cs2 competition? please. | pipeline:structured_competition_rules_en | overview_without_multiple_rule_clauses | คำถามรวมได้หลักฐานหลายหัวข้อแต่ไม่มีข้อความกติกาจริงครบ; ใช้ selected substantive overview ของเกมที่ระบุ |
| R24-EN-cs2-121 | Please check: Summarize the cs2 competition ruls. please. | pipeline:structured_competition_rules_en | overview_without_multiple_rule_clauses | คำถามรวมได้หลักฐานหลายหัวข้อแต่ไม่มีข้อความกติกาจริงครบ; ใช้ selected substantive overview ของเกมที่ระบุ |
| R24-EN-cs2-122 | Please check: cs2 ruls overview please. please. | pipeline:structured_game_availability_en | route_mismatch, missing_target_evidence, overview_without_multiple_rule_clauses | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-EN-cs2-165 | Please check: What do the CS2 tournament ruls say about maps, vetoes, and map selection? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-166 | Please check: For Counter-Strike 2, can you verify the rule on maps, vetoes, and map selection? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-167 | Please check: I am preparing for a Counter Strike 2 match. What is the policy for maps, vetoes, and map selection? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-168 | Please check: Please retrieve the official CS2 rulebook evidence for maps, vetoes, and map selection. please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-169 | Please check: How is maps, vetoes, and map selection handled in the Counter-Strike 2 tournament ruls? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-170 | Please check: Could you cite the Counter Strike 2 rule concerning maps, vetoes, and map selection? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-177 | Please check: What do the CS2 tournament ruls say about in-game settings? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-178 | Please check: For Counter-Strike 2, can you verify the rule on in-game settings? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-179 | Please check: I am preparing for a Counter Strike 2 match. What is the policy for in-game settings? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-180 | Please check: Please retrieve the official CS2 rulebook evidence for in-game settings. please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-181 | Please check: How is in-game settings handled in the Counter-Strike 2 tournament ruls? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-182 | Please check: Could you cite the Counter Strike 2 rule concerning in-game settings? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-cs2-228 | Please check: Please retrieve the official CS2 rulebook evidence for the tournament schedule. please. | pipeline:protected_booking_window | route_mismatch, missing_target_evidence, wrong_facet_evidence, answer_without_substantive_source_content | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-EN-rov-041 | What do the RoV tournament rules say about the rulebook scope and tournament identity? | pipeline:competition_rule_overview_source | wrong_facet_evidence | เลือกหัวข้อไม่ตรงคำถามหรือไม่มี English เนื้อหาในแถวที่ตรง; จัด substantive candidates ก่อน headings |
| R24-EN-rov-042 | For Arena of Valor, can you verify the rule on the rulebook scope and tournament identity? | pipeline:structured_competition_rules_en | foreign_game_evidence | พบหลักฐานเกมอื่น; trace แสดงการขยายชื่อเกม/การเปรียบเทียบ ต้องยึด explicit target เดิมและใช้ query แยกแต่ละเกม |
| R24-EN-rov-045 | How is the rulebook scope and tournament identity handled in the Arena of Valor tournament rules? | pipeline:competition_rule_overview_source | wrong_facet_evidence | เลือกหัวข้อไม่ตรงคำถามหรือไม่มี English เนื้อหาในแถวที่ตรง; จัด substantive candidates ก่อน headings |
| R24-EN-rov-055 | Please check: What are the rov tournament ruls? please. | pipeline:structured_competition_rules_en | overview_without_multiple_rule_clauses | คำถามรวมได้หลักฐานหลายหัวข้อแต่ไม่มีข้อความกติกาจริงครบ; ใช้ selected substantive overview ของเกมที่ระบุ |
| R24-EN-rov-056 | Please check: What ruls apply to the rov competition? please. | pipeline:structured_competition_rules_en | overview_without_multiple_rule_clauses | คำถามรวมได้หลักฐานหลายหัวข้อแต่ไม่มีข้อความกติกาจริงครบ; ใช้ selected substantive overview ของเกมที่ระบุ |
| R24-EN-rov-057 | Please check: Summarize the rov competition ruls. please. | pipeline:structured_competition_rules_en | overview_without_multiple_rule_clauses | คำถามรวมได้หลักฐานหลายหัวข้อแต่ไม่มีข้อความกติกาจริงครบ; ใช้ selected substantive overview ของเกมที่ระบุ |
| R24-EN-rov-058 | Please check: rov ruls overview please. please. | pipeline:structured_games_catalog_en | route_mismatch, missing_target_evidence, overview_without_multiple_rule_clauses | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-EN-rov-096 | Please check: For Arena of Valor, can you verify the rule on the rulebook scope and tournament identity? please. | pipeline:structured_competition_rules_en | foreign_game_evidence | พบหลักฐานเกมอื่น; trace แสดงการขยายชื่อเกม/การเปรียบเทียบ ต้องยึด explicit target เดิมและใช้ query แยกแต่ละเกม |
| R24-EN-rov-149 | Could you explain: What do the RoV tournament rules say about the rulebook scope and tournament identity? please. | pipeline:competition_rule_overview_source | wrong_facet_evidence | เลือกหัวข้อไม่ตรงคำถามหรือไม่มี English เนื้อหาในแถวที่ตรง; จัด substantive candidates ก่อน headings |
| R24-EN-rov-150 | Could you explain: For Arena of Valor, can you verify the rule on the rulebook scope and tournament identity? please. | pipeline:structured_competition_rules_en | foreign_game_evidence | พบหลักฐานเกมอื่น; trace แสดงการขยายชื่อเกม/การเปรียบเทียบ ต้องยึด explicit target เดิมและใช้ query แยกแต่ละเกม |
| R24-EN-rov-153 | Could you explain: How is the rulebook scope and tournament identity handled in the Arena of Valor tournament rules? please. | pipeline:competition_rule_overview_source | wrong_facet_evidence | เลือกหัวข้อไม่ตรงคำถามหรือไม่มี English เนื้อหาในแถวที่ตรง; จัด substantive candidates ก่อน headings |
| R24-EN-rov-203 | I would like to know: What do the RoV tournamet rules say about the rulebook scope and tournament identity? please. | pipeline:competition_rule_overview_source | wrong_facet_evidence | เลือกหัวข้อไม่ตรงคำถามหรือไม่มี English เนื้อหาในแถวที่ตรง; จัด substantive candidates ก่อน headings |
| R24-EN-rov-204 | I would like to know: For Arena of Valor, can you verify the rule on the rulebook scope and tournamet identity? please. | pipeline:structured_competition_rules_en | foreign_game_evidence | พบหลักฐานเกมอื่น; trace แสดงการขยายชื่อเกม/การเปรียบเทียบ ต้องยึด explicit target เดิมและใช้ query แยกแต่ละเกม |
| R24-EN-rov-207 | I would like to know: How is the rulebook scope and tournamet identity handled in the Arena of Valor tournament rules? please. | pipeline:competition_rule_overview_source | wrong_facet_evidence | เลือกหัวข้อไม่ตรงคำถามหรือไม่มี English เนื้อหาในแถวที่ตรง; จัด substantive candidates ก่อน headings |
| R24-EN-rov-217 | Please tell me: What are the rov tournament ruules? please. | pipeline:structured_competition_rules_en | overview_without_multiple_rule_clauses | คำถามรวมได้หลักฐานหลายหัวข้อแต่ไม่มีข้อความกติกาจริงครบ; ใช้ selected substantive overview ของเกมที่ระบุ |
| R24-EN-rov-218 | Please tell me: What ruules apply to the rov competition? please. | pipeline:structured_competition_rules_en | overview_without_multiple_rule_clauses | คำถามรวมได้หลักฐานหลายหัวข้อแต่ไม่มีข้อความกติกาจริงครบ; ใช้ selected substantive overview ของเกมที่ระบุ |
| R24-EN-rov-219 | Please tell me: Summarize the rov competition ruules. please. | pipeline:structured_competition_rules_en | overview_without_multiple_rule_clauses | คำถามรวมได้หลักฐานหลายหัวข้อแต่ไม่มีข้อความกติกาจริงครบ; ใช้ selected substantive overview ของเกมที่ระบุ |
| R24-EN-rov-220 | Please tell me: rov ruules overview please. please. | pipeline:structured_games_catalog_en | route_mismatch, missing_target_evidence, overview_without_multiple_rule_clauses | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-EN-tekken8-029 | What do the TEKKEN 8 tournament rules say about in-game settings? | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-030 | For Tekken 8, can you verify the rule on in-game settings? | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-031 | I am preparing for a T8 match. What is the policy for in-game settings? | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-032 | Please retrieve the official TEKKEN 8 rulebook evidence for in-game settings. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-033 | How is in-game settings handled in the Tekken 8 tournament rules? | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-034 | Could you cite the T8 rule concerning in-game settings? | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-041 | What do the TEKKEN 8 tournament rules say about the rulebook scope and tournament identity? | pipeline:competition_rule_overview_source | wrong_facet_evidence | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-042 | For Tekken 8, can you verify the rule on the rulebook scope and tournament identity? | pipeline:competition_source_localization_pending_en | outcome_mismatch | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-043 | I am preparing for a T8 match. What is the policy for the rulebook scope and tournament identity? | pipeline:missing_english_localization | outcome_mismatch, missing_target_evidence, wrong_facet_evidence | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-044 | Please retrieve the official TEKKEN 8 rulebook evidence for the rulebook scope and tournament identity. | pipeline:competition_source_localization_pending_en | outcome_mismatch | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-045 | How is the rulebook scope and tournament identity handled in the Tekken 8 tournament rules? | pipeline:competition_rule_overview_source | wrong_facet_evidence | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-046 | Could you cite the T8 rule concerning the rulebook scope and tournament identity? | pipeline:missing_english_localization | outcome_mismatch, missing_target_evidence, wrong_facet_evidence | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-047 | Please check: What are the tekken 8 tournament ruls? please. | pipeline:structured_competition_rules_en | overview_without_multiple_rule_clauses | คำถามรวมได้หลักฐานหลายหัวข้อแต่ไม่มีข้อความกติกาจริงครบ; ใช้ selected substantive overview ของเกมที่ระบุ |
| R24-EN-tekken8-048 | Please check: What ruls apply to the tekken 8 competition? please. | pipeline:structured_competition_rules_en | overview_without_multiple_rule_clauses | คำถามรวมได้หลักฐานหลายหัวข้อแต่ไม่มีข้อความกติกาจริงครบ; ใช้ selected substantive overview ของเกมที่ระบุ |
| R24-EN-tekken8-049 | Please check: Summarize the tekken 8 competition ruls. please. | pipeline:structured_competition_rules_en | overview_without_multiple_rule_clauses | คำถามรวมได้หลักฐานหลายหัวข้อแต่ไม่มีข้อความกติกาจริงครบ; ใช้ selected substantive overview ของเกมที่ระบุ |
| R24-EN-tekken8-050 | Please check: tekken 8 ruls overview please. please. | pipeline:structured_game_detail_en | route_mismatch, missing_target_evidence, overview_without_multiple_rule_clauses | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-EN-tekken8-075 | Please check: What do the TEKKEN 8 tournament ruls say about in-game settings? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-076 | Please check: For Tekken 8, can you verify the rule on in-game settings? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-077 | Please check: I am preparing for a T8 match. What is the policy for in-game settings? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-078 | Please check: Please retrieve the official TEKKEN 8 rulebook evidence for in-game settings. please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-079 | Please check: How is in-game settings handled in the Tekken 8 tournament ruls? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-080 | Please check: Could you cite the T8 rule concerning in-game settings? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-087 | Please check: What do the TEKKEN 8 tournament ruls say about the rulebook scope and tournament identity? please. | pipeline:competition_source_localization_pending_en | outcome_mismatch | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-088 | Please check: For Tekken 8, can you verify the rule on the rulebook scope and tournament identity? please. | pipeline:competition_source_localization_pending_en | outcome_mismatch | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-089 | Please check: I am preparing for a T8 match. What is the policy for the rulebook scope and tournament identity? please. | pipeline:missing_english_localization | outcome_mismatch, missing_target_evidence, wrong_facet_evidence | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-090 | Please check: Please retrieve the official TEKKEN 8 rulebook evidence for the rulebook scope and tournament identity. please. | pipeline:competition_source_localization_pending_en | outcome_mismatch | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-091 | Please check: How is the rulebook scope and tournament identity handled in the Tekken 8 tournament ruls? please. | pipeline:competition_source_localization_pending_en | outcome_mismatch | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-092 | Please check: Could you cite the T8 rule concerning the rulebook scope and tournament identity? please. | pipeline:missing_english_localization | outcome_mismatch, missing_target_evidence, wrong_facet_evidence | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-121 | Could you explain: What do the TEKKEN 8 tournament rules say about in-game settings? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-122 | Could you explain: For Tekken 8, can you verify the rule on in-game settings? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-123 | Could you explain: I am preparing for a T8 match. What is the policy for in-game settings? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-124 | Could you explain: Please retrieve the official TEKKEN 8 rulebook evidence for in-game settings. please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-125 | Could you explain: How is in-game settings handled in the Tekken 8 tournament rules? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-126 | Could you explain: Could you cite the T8 rule concerning in-game settings? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-133 | Could you explain: What do the TEKKEN 8 tournament rules say about the rulebook scope and tournament identity? please. | pipeline:competition_rule_overview_source | wrong_facet_evidence | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-134 | Could you explain: For Tekken 8, can you verify the rule on the rulebook scope and tournament identity? please. | pipeline:competition_source_localization_pending_en | outcome_mismatch | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-135 | Could you explain: I am preparing for a T8 match. What is the policy for the rulebook scope and tournament identity? please. | pipeline:missing_english_localization | outcome_mismatch, missing_target_evidence, wrong_facet_evidence | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-136 | Could you explain: Please retrieve the official TEKKEN 8 rulebook evidence for the rulebook scope and tournament identity. please. | pipeline:competition_source_localization_pending_en | outcome_mismatch | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-137 | Could you explain: How is the rulebook scope and tournament identity handled in the Tekken 8 tournament rules? please. | pipeline:competition_rule_overview_source | wrong_facet_evidence | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-138 | Could you explain: Could you cite the T8 rule concerning the rulebook scope and tournament identity? please. | pipeline:missing_english_localization | outcome_mismatch, missing_target_evidence, wrong_facet_evidence | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-167 | I would like to know: What do the TEKKEN 8 tournamet rules say about in-game settings? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-168 | I would like to know: For Tekken 8, can you verify the rule on in-game settings? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-169 | I would like to know: I am preparing for a T8 match. What is the policy for in-game settings? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-170 | I would like to know: Please retrieve the official TEKKEN 8 rulebook evidence for in-game settings. please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-171 | I would like to know: How is in-game settings handled in the Tekken 8 tournamet rules? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-172 | I would like to know: Could you cite the T8 rule concerning in-game settings? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-179 | I would like to know: What do the TEKKEN 8 tournamet rules say about the rulebook scope and tournament identity? please. | pipeline:competition_rule_overview_source | wrong_facet_evidence | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-180 | I would like to know: For Tekken 8, can you verify the rule on the rulebook scope and tournamet identity? please. | pipeline:competition_source_localization_pending_en | outcome_mismatch | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-181 | I would like to know: I am preparing for a T8 match. What is the policy for the rulebook scope and tournamet identity? please. | pipeline:missing_english_localization | outcome_mismatch, missing_target_evidence, wrong_facet_evidence | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-182 | I would like to know: Please retrieve the official TEKKEN 8 rulebook evidence for the rulebook scope and tournamet identity. please. | pipeline:competition_source_localization_pending_en | outcome_mismatch | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-183 | I would like to know: How is the rulebook scope and tournamet identity handled in the Tekken 8 tournament rules? please. | pipeline:competition_rule_overview_source | wrong_facet_evidence | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-184 | I would like to know: Could you cite the T8 rule concerning the rulebook scope and tournamet identity? please. | pipeline:missing_english_localization | outcome_mismatch, missing_target_evidence, wrong_facet_evidence | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-185 | Please tell me: What are the tekken 8 tournament ruules? please. | pipeline:structured_competition_rules_en | overview_without_multiple_rule_clauses | คำถามรวมได้หลักฐานหลายหัวข้อแต่ไม่มีข้อความกติกาจริงครบ; ใช้ selected substantive overview ของเกมที่ระบุ |
| R24-EN-tekken8-186 | Please tell me: What ruules apply to the tekken 8 competition? please. | pipeline:structured_competition_rules_en | overview_without_multiple_rule_clauses | คำถามรวมได้หลักฐานหลายหัวข้อแต่ไม่มีข้อความกติกาจริงครบ; ใช้ selected substantive overview ของเกมที่ระบุ |
| R24-EN-tekken8-187 | Please tell me: Summarize the tekken 8 competition ruules. please. | pipeline:structured_competition_rules_en | overview_without_multiple_rule_clauses | คำถามรวมได้หลักฐานหลายหัวข้อแต่ไม่มีข้อความกติกาจริงครบ; ใช้ selected substantive overview ของเกมที่ระบุ |
| R24-EN-tekken8-188 | Please tell me: tekken 8 ruules overview please. please. | pipeline:structured_game_detail_en | route_mismatch, missing_target_evidence, overview_without_multiple_rule_clauses | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-EN-tekken8-213 | Please tell me: What do the TEKKEN 8 tournament ruules say about in-game settings? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-214 | Please tell me: For Tekken 8, can you verify the rule on in-game settings? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-215 | Please tell me: I am preparing for a T8 match. What is the policy for in-game settings? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-216 | Please tell me: Please retrieve the official TEKKEN 8 rulebook evidence for in-game settings. please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-217 | Please tell me: How is in-game settings handled in the Tekken 8 tournament ruules? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-218 | Please tell me: Could you cite the T8 rule concerning in-game settings? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-tekken8-225 | Please tell me: What do the TEKKEN 8 tournament ruules say about the rulebook scope and tournament identity? please. | pipeline:competition_source_localization_pending_en | outcome_mismatch | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-226 | Please tell me: For Tekken 8, can you verify the rule on the rulebook scope and tournament identity? please. | pipeline:competition_source_localization_pending_en | outcome_mismatch | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-227 | Please tell me: I am preparing for a T8 match. What is the policy for the rulebook scope and tournament identity? please. | pipeline:missing_english_localization | outcome_mismatch, missing_target_evidence, wrong_facet_evidence | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-228 | Please tell me: Please retrieve the official TEKKEN 8 rulebook evidence for the rulebook scope and tournament identity. please. | pipeline:competition_source_localization_pending_en | outcome_mismatch | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-229 | Please tell me: How is the rulebook scope and tournament identity handled in the Tekken 8 tournament ruules? please. | pipeline:competition_source_localization_pending_en | outcome_mismatch | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-tekken8-230 | Please tell me: Could you cite the T8 rule concerning the rulebook scope and tournament identity? please. | pipeline:missing_english_localization | outcome_mismatch, missing_target_evidence, wrong_facet_evidence | ข้อความชื่อเอกสาร Tekken แถว s01_c01 ขาด English text; เพิ่มคำแปลหนึ่งรายการด้วย source hash โดยคง 590 รายการเดิม |
| R24-EN-valorant-041 | What do the VALORANT tournament rules say about penalties? | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-valorant-042 | For Valorant, can you verify the rule on penalties? | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-valorant-044 | Please retrieve the official VALORANT rulebook evidence for penalties. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-valorant-045 | How is penalties handled in the Valorant tournament rules? | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-valorant-046 | Could you cite the Valo rule concerning penalties? | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-valorant-070 | Please check: VALORANT ruls overview please. please. | pipeline:structured_game_detail_en | route_mismatch, missing_target_evidence, overview_without_multiple_rule_clauses | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-EN-valorant-107 | Please check: What do the VALORANT tournament ruls say about penalties? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-valorant-108 | Please check: For Valorant, can you verify the rule on penalties? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-valorant-110 | Please check: Please retrieve the official VALORANT rulebook evidence for penalties. please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-valorant-111 | Please check: How is penalties handled in the Valorant tournament ruls? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-valorant-112 | Please check: Could you cite the Valo rule concerning penalties? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-valorant-173 | Could you explain: What do the VALORANT tournament rules say about penalties? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-valorant-174 | Could you explain: For Valorant, can you verify the rule on penalties? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-valorant-176 | Could you explain: Please retrieve the official VALORANT rulebook evidence for penalties. please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-valorant-177 | Could you explain: How is penalties handled in the Valorant tournament rules? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-valorant-178 | Could you explain: Could you cite the Valo rule concerning penalties? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-valorant-239 | I would like to know: What do the VALORANT tournamet rules say about penalties? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-valorant-240 | I would like to know: For Valorant, can you verify the rule on penalties? please. | pipeline:structured_competition_rules_en | answer_without_substantive_source_content | ต้องอ่านคำตอบเทียบ source: บางข้อเป็นหัวข้อจริง บางข้อเป็นค่าตัวเลขสั้นที่ rubric A ให้ตกผิด; ดูผล regrade แยก |
| R24-EN-SAFE-002 | How many players can a team have? | pipeline:structured_service_capacity_en | outcome_mismatch, route_mismatch | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-EN-SAFE-007 | Please check: What are the timeout ruls? please. | pipeline:english_no_answer | outcome_mismatch, route_mismatch | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-EN-SAFE-008 | Please check: How many players can a team have? please. | pipeline:structured_service_capacity_en | outcome_mismatch, route_mismatch | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-EN-SAFE-014 | Could you explain: How many players can a team have? please. | pipeline:structured_service_capacity_en | outcome_mismatch, route_mismatch | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-EN-SAFE-020 | I would like to know: How many players can a team have? please. | pipeline:structured_service_capacity_en | outcome_mismatch, route_mismatch | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-EN-SAFE-025 | Please tell me: What are the timeout ruules? please. | pipeline:english_no_answer | outcome_mismatch, route_mismatch | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-EN-SAFE-026 | Please tell me: How many players can a team have? please. | pipeline:structured_service_capacity_en | outcome_mismatch, route_mismatch | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-EN-SAFE-032 | Quick question: How many players can a team have? please. | pipeline:structured_service_capacity_en | outcome_mismatch, route_mismatch | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-EN-SAFE-037 | What are the timeout rulse? please. | pipeline:english_no_answer | outcome_mismatch, route_mismatch | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
| R24-EN-SAFE-038 | How many players can a team have? please. | pipeline:structured_service_capacity_en | outcome_mismatch, route_mismatch | เข้าหมวดอื่นก่อนการแข่งขัน; ตรวจ cue และ protected responder ที่แย่งตอบ เช่น rulebook มี book |
