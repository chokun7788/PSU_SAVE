# Smoke Test Results - PSU Esports Local RAG

วันที่ทดสอบ: 2026-06-29

ทดสอบ pipeline ล่าสุดหลังปรับ rule-based fast path, RAG direct curated fallback, และ fast model

## Environment

- Project: `C:\Users\Chokhun\Downloads\Learn-LLM\15_PSU_Esports_Local_RAG_Qwen3_4B`
- LLM model: `qwen2.5:3b`
- Embedding model: `intfloat/multilingual-e5-small`
- TOP_K: `4`
- MAX_CONTEXT_CHARS: `3200`
- LLM_NUM_CTX: `2048`
- LLM_NUM_PREDICT: `120`
- Warmup latency: `8.71` sec

## Summary

- Total tests: `17`
- PASS: `17`
- CHECK: `0`
- Average recorded latency: `1.283` sec

## Result Table

| Group | Question | Mode | Expected | Latency | Verdict | Retrieved IDs | Short Answer |
|---|---|---|---|---:|---|---|---|
| rule | เช็คอินล่วงหน้าได้กี่นาที | `rule_fast_path` | `rule_fast_path` | 0.009s | PASS | rule_checkin_advance | คำตอบ: เช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_checkin_advance / curated_checkin_30_mi... |
| rule | เช็คอินล่วงหน้าได้กี่วินาที | `rule_fast_path` | `rule_fast_path` | 0.000s | PASS | rule_checkin_advance | คำตอบ: เช็คอินได้ล่วงหน้าสูงสุด 30 นาที หรือ 1,800 วินาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_checkin_advance / cur... |
| rule | เช็คอินล่วงหน้าได้กี่ชั่วโมง | `rule_fast_path` | `rule_fast_path` | 0.000s | PASS | rule_checkin_advance | คำตอบ: เช็คอินได้ล่วงหน้าสูงสุด 0.5 ชั่วโมง หรือ 30 นาที และต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_checkin_advance / cura... |
| rule | PS5 มีเกมอะไรบ้าง | `rule_fast_path` | `rule_fast_path` | 0.001s | PASS | rule_ps5_games | คำตอบ: เกม PlayStation 5 ที่มีในรายการ ได้แก่ Call of Duty: Modern Warfare III, Delta Force, EA Sports FC 24, eFootball, FINAL FANTASY XVI, Fortnite, God of War Ragnarok, Hogwarts... |
| rule | ศูนย์นี้เกี่ยวกับอะไร | `rule_fast_path` | `rule_fast_path` | 0.000s | PASS | rule_overview_identity | คำตอบ: PSU Esports Studio - Phuket คือศูนย์พัฒนาการเรียนรู้ด้านอีสปอร์ตเพื่อความเป็นเลิศและขับเคลื่อนเศรษฐกิจในพื้นที่ภาคใต้ สาขาภูเก็ต ของมหาวิทยาลัยสงขลานครินทร์ แหล่งข้อมูล: - h... |
| rule | ยกเลิกจองได้เงินคืนไหม | `rule_fast_path` | `rule_fast_path` | 0.000s | PASS | rule_refund_policy | คำตอบ: โดยทั่วไปไม่มีการคืนเงิน ยกเว้นกรณีที่ศูนย์เป็นฝ่ายผิดพลาด เช่น อุปกรณ์ขัดข้อง หรือมีเหตุสุดวิสัยที่ทำให้ศูนย์ต้องปิดให้บริการ แหล่งข้อมูล: - https://esports.computing.psu.a... |
| rule | สูบบุหรี่ได้ไหม | `rule_fast_path` | `rule_fast_path` | 0.000s | PASS | rule_smoking_alcohol | คำตอบ: ศูนย์ห้ามสูบบุหรี่ เสพสารเสพติด หรือดื่มเครื่องดื่มแอลกอฮอล์ภายในศูนย์ แหล่งข้อมูล: - https://esports.computing.psu.ac.th/ (rule_smoking_alcohol / curated_rule_smoking_alcoh... |
| rule | ศูนย์เปิดถึงกี่โมง | `rule_fast_path` | `rule_fast_path` | 0.000s | PASS | rule_service_schedule | คำตอบ: ข้อมูลที่มีในระบบเป็นตารางรอบบริการอุปกรณ์: Morning 09:00–12:00 และ Afternoon 13:00–16:00 โดยยังไม่พบข้อมูลเวลาเปิด-ปิดศูนย์อย่างเป็นทางการแยกต่างหาก แหล่งข้อมูล: - https://... |
| rag_direct | ศูนย์นี้เกี่ยวกับอะไร | `rag_direct_curated` | `rag_direct_curated` | 0.037s | PASS | curated_overview_identity, curated_overview_mission | คำตอบ: - PSU Esports Studio - Phuket คือศูนย์พัฒนาการเรียนรู้ด้านอีสปอร์ตเพื่อความเป็นเลิศและขับเคลื่อนเศรษฐกิจในพื้นที่ภาคใต้ สาขาภูเก็ต เป็นศูนย์การเรียนรู้ผ่านเกมและอีสปอร์ตของม... |
| rag_direct | ติดต่อศูนย์ได้ทางไหน | `rag_direct_curated` | `rag_direct_curated` | 0.037s | PASS | curated_contact_facebook, curated_contact_email, curated_contact_location, curated_contact_phone | คำตอบ: - Facebook ของศูนย์คือ https://www.facebook.com/psuesportsphuket - อีเมลติดต่อศูนย์คือ psuesportspkt@gmail.com - PSU Esports Studio - Phuket ตั้งอยู่ที่มหาวิทยาลัยสงขลานคริน... |
| rag_direct | PS5 มีเกมอะไรบ้าง | `rag_direct_curated` | `rag_direct_curated` | 0.033s | PASS | curated_games_ps5, curated_games_pc, curated_games_switch, curated_games_popular | คำตอบ: - เกมที่ปรากฏในรายการ PlayStation 5 ได้แก่ Call of Duty: Modern Warfare III, Delta Force, EA Sports FC 24, eFootball, FINAL FANTASY XVI, Fortnite, God of War Ragnarok, Hogwa... |
| rag_direct | เช็คอินล่วงหน้าได้กี่วินาที | `rag_direct_curated` | `rag_direct_curated` | 0.034s | PASS | curated_checkin_30_minutes, curated_time_change_policy, curated_reservation_advance_time, curated_checkin_late_cancel | คำตอบ: - ผู้ใช้งานต้องเช็คอินก่อนเวลาเริ่มต้นของรอบที่จอง โดยสามารถเช็คอินได้ล่วงหน้าสูงสุด 30 นาที และต้องเช็คอินก่อนถึงเวลาเริ่มต้นของรอบ แหล่งข้อมูล: - https://esports.computing... |
| rag_direct | ศูนย์เปิดถึงกี่โมง | `rag_direct_curated` | `rag_direct_curated` | 0.031s | PASS | curated_schedule_morning, curated_schedule_afternoon, curated_time_change_policy, curated_reservation_advance_time | คำตอบ: - ตารางบริการช่วง Morning คือ 09:00 – 12:00 - ตารางบริการช่วง Afternoon คือ 13:00 – 16:00 - ยังไม่พบข้อมูลเวลาเปิด-ปิดศูนย์อย่างเป็นทางการแยกต่างหากในฐานข้อมูลปัจจุบัน แหล่ง... |
| rag_llm | ศูนย์นี้เกี่ยวกับอะไร | `rag_llm` | `rag_llm` | 10.165s | PASS | curated_overview_identity, curated_overview_mission | คำตอบ: ศูนย์ PSU Esports Studio - Phuket เกี่ยวข้องกับการพัฒนาและส่งเสริมความเป็นเลิศด้านอีสปอร์ต โดยผ่านการใช้ประโยชน์จากเกมและอีสปอร์ตเพื่อการเรียนรู้และการศึกษา ศูนย์นี้ได้รับกา... |
| rag_llm | ติดต่อศูนย์ได้ทางไหน | `rag_llm` | `rag_llm` | 4.802s | PASS | curated_contact_facebook, curated_contact_email, curated_contact_location, curated_contact_phone | คำตอบ: สามารถติดต่อกับ PSU Esports Studio - Phuket ได้หลายช่องทางดังนี้: - Facebook: https://www.facebook.com/psuesportsphuket - อีเมล: psuesportspkt@gmail.com - ที่ตั้ง: มหาวิทยาล... |
| rag_llm | กฎการใช้บริการมีอะไรบ้าง | `rag_llm` | `rag_llm` | 3.622s | PASS | curated_rule_weapons_gambling, curated_rule_move_equipment, curated_rule_lost_items, curated_rule_smoking_alcohol_drugs | คำตอบ: 1. ห้ามพกอาวุธหรือของมีคม 2. ห้ามทะเลาะวิวาท 3. ห้ามเล่นการพนัน |
| rag_llm | ศูนย์เปิดถึงกี่โมง | `rag_llm` | `rag_llm` | 3.035s | PASS | curated_schedule_morning, curated_schedule_afternoon, curated_time_change_policy, curated_reservation_advance_time | คำตอบ: 09:00 - 16:00 |

## Cases To Check

ไม่มี case ที่ต้องเช็กเพิ่มจากเกณฑ์เบื้องต้น

## Notes

- `rule_fast_path` เร็วที่สุดและเหมาะกับ FAQ ซ้ำ ๆ
- `rag_direct_curated` ใช้เมื่อ retrieval เจอ curated fact ชัดเจน จึงไม่ต้องเรียก LLM
- `rag_llm` ใช้เมื่อคำถามต้องสรุปจาก context หรือไม่มี rule/direct answer
- ถ้า retrieved IDs ถูกแต่คำตอบผิด ให้ปรับ prompt หรือเพิ่ม direct/curated rule
- ถ้า retrieved IDs ผิด ให้ปรับ route category, chunk, tags, หรือ curated facts
