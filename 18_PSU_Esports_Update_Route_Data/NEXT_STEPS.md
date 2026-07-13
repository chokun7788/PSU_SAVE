# Next Steps

## งานที่ควรทำต่อทันที

1. เชื่อม router ใน `app/core/router.py` กลับเข้า notebook หรือ backend หลัก
2. ให้ notebook เรียก `deterministic_calculator` ก่อนเข้า RAG/LLM สำหรับคำถามราคา
3. เอา `data/rules/*.jsonl` ไปใช้แทน rule file เดี่ยว หรือทำ loader ให้รองรับทั้งสองแบบ
4. เปิด `data/human_review/human_review_from_eval_sample.jsonl` แล้วให้คนตรวจ 100-120 ข้อแรก
5. สรุป error tags ที่เจอบ่อย แล้วค่อยแก้เป็นรอบ

## งาน Phase ถัดไป

- เพิ่มข้อมูลกฎเกม/การแข่งขันจริงเมื่อได้เอกสารจากศูนย์
- เพิ่ม route สำหรับ Facebook FAQ ถ้าเริ่มดึงข้อมูลจากเพจ
- เพิ่ม admin UI เล็ก ๆ สำหรับเพิ่ม curated fact/rule โดยไม่ต้องแก้ JSONL เอง
- เพิ่ม test ชุด edge case เรื่องวันศุกร์, maintenance, ราคาไม่ระบุกลุ่ม, PC ไม่มีราคา
- ทำ Docker สำหรับ backend หลัง route stable

## สิ่งที่ยังไม่ควรทำตอนนี้

- Fine-tune model ทันที เพราะปัญหาหลักยังเป็น data/routing มากกว่า model
- ใช้ fuzzy/cosine กว้างกับ rulebase ทั้งหมด เพราะจะเพิ่ม false positive
- ให้ LLM คำนวณราคาเอง เพราะเสี่ยงตอบผิดและช้ากว่า deterministic calculator
