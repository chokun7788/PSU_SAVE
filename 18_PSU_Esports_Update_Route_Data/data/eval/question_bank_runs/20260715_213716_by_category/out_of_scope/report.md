# User Question Bank Evaluation

- Generated at: 2026-07-15T21:45:58
- Total questions: 100
- Total wall time: 142.668s

## Summary By Strategy
- fastpath/rulebase: 27
- llm: 62
- rag/vector: 11

## Results

### OOS-001 out_of_scope ข้อ 1
- Question: สอนทำข้าวผัดแบบง่ายๆ
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/general_knowledge_query`
- Strategy: `llm`
- Latency: 0.4987s | Wall: 0.4988s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-002 out_of_scope ข้อ 2
- Question: วันนี้ฝนจะตกไหม
- Expected: general_llm_or_decline
- Mode: `pipeline:calendar_schedule_fast_path`
- Route: `schedule/schedule_query`
- Strategy: `fastpath/rulebase`
- Latency: 1.0229s | Wall: 1.0229s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: วันนี้ 15/07/2026 (วันพุธ): วันพุธเปิดให้เล่น 09:00-12:00 และ 13:00-16:00 วันที่อ้างอิงของระบบ: วันนี้คือ 15/07/2026 (วันพุธ) ตามเวลาไทย  ปฏิทินไทยของวันที่นี้: ไม่พบวันหยุดไทยหรือเทศกาลในปฏิทินที่บันทึกไว้สำหรับวันที่นี้  รายละเอียดจากตาราง: - วันจันทร์ช่วงเช...

### OOS-003 out_of_scope ข้อ 3
- Question: ช่วยแปลประโยคนี้เป็นอังกฤษได้ไหม
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.4602s | Wall: 0.4602s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-004 out_of_scope ข้อ 4
- Question: สูตรคำนวณพื้นที่วงกลมคืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/general_knowledge_query`
- Strategy: `llm`
- Latency: 0.4447s | Wall: 0.4448s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-005 out_of_scope ข้อ 5
- Question: ขอไอเดียตั้งชื่อร้านกาแฟ
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.2761s | Wall: 0.2761s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-006 out_of_scope ข้อ 6
- Question: ช่วยเขียนคำอวยพรวันเกิดให้เพื่อน
- Expected: general_llm_or_decline
- Mode: `pipeline:experimental_soft_related_fallback`
- Route: `general/unknown_domain_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.4402s | Wall: 0.4403s
- Sources: reservation: https://esports.computing.psu.ac.th/reservation
- Answer: โหมดทดลอง RAG: ข้อมูลที่ยืนยันได้คือศูนย์มีระบบจองเพื่อเข้าใช้บริการเป็นรอบเวลา แต่ยังไม่มีข้อมูลยืนยันว่าศูนย์รับจัดงานวันเกิด/ปาร์ตี้/อีเวนต์ส่วนตัวในฐานข้อมูลที่มีครับ แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### OOS-007 out_of_scope ข้อ 7
- Question: วิธีลดน้ำหนักที่ปลอดภัยควรเริ่มยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.5926s | Wall: 0.5926s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-008 out_of_scope ข้อ 8
- Question: อาการปวดหัวบ่อยควรทำยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.3646s | Wall: 0.3646s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-009 out_of_scope ข้อ 9
- Question: หุ้นตัวไหนดีวันนี้
- Expected: general_llm_or_decline
- Mode: `pipeline:calendar_schedule_fast_path`
- Route: `schedule/schedule_query`
- Strategy: `fastpath/rulebase`
- Latency: 1.4252s | Wall: 1.4253s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: วันนี้ 15/07/2026 (วันพุธ): วันพุธเปิดให้เล่น 09:00-12:00 และ 13:00-16:00 วันที่อ้างอิงของระบบ: วันนี้คือ 15/07/2026 (วันพุธ) ตามเวลาไทย  ปฏิทินไทยของวันที่นี้: ไม่พบวันหยุดไทยหรือเทศกาลในปฏิทินที่บันทึกไว้สำหรับวันที่นี้  รายละเอียดจากตาราง: - วันจันทร์ช่วงเช...

### OOS-010 out_of_scope ข้อ 10
- Question: ราคาทองวันนี้เท่าไหร่
- Expected: general_llm_or_decline
- Mode: `pipeline:rag_direct_curated`
- Route: `service_fee/service_fee_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.3259s | Wall: 0.3259s
- Sources: curated_service_fee_2026_full_table: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png | curated_service_fee_pc_unknown: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png | curated_user_group_alias_psu_student_staff: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
- Answer: ตารางค่าบริการ PSU Esports Studio - Phuket Service Fee 2026 ตามภาพ: PlayStation 5 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท, PSU Alumni and General Student 50 บาท, General Adult 150 บาท. Nintendo Switch 1 ชั่วโมง 1-2 คน: PSU Student and Staff ฟรี 0 บาท...

### OOS-011 out_of_scope ข้อ 11
- Question: ข่าวการเมืองล่าสุดคืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:hybrid_guarded_rerank`
- Route: `events_news/news_lookup`
- Strategy: `rag/vector`
- Latency: 0.4134s | Wall: 0.4135s
- Sources: curated_news_chinese_students_game_based_learning: https://esports.phuket.psu.ac.th/events-news/news | curated_news_cs2_2026: https://esports.phuket.psu.ac.th/events-news/news | curated_news_valorant_2026: https://esports.phuket.psu.ac.th/events-news/news | curated_news_game_on_thaimuang: https://esports.phuket.psu.ac.th/events-news/news
- Answer: เมื่อวันที่ 27 กุมภาพันธ์ 2569 นักศึกษาชาวจีนระดับปริญญาโท คณะการบริการและการท่องเที่ยว จำนวน 11 คน เข้าร่วมกิจกรรมการเรียนรู้โดยใช้เกมเป็นฐาน (Game-based Learning) ณ PSU Esports Studio - Phuket แหล่งข้อมูล: https://esports.phuket.psu.ac.th/events-news/news

### OOS-012 out_of_scope ข้อ 12
- Question: ใครเป็นนายกรัฐมนตรีตอนนี้
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.3128s | Wall: 0.3128s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-013 out_of_scope ข้อ 13
- Question: ช่วยแต่งกลอนสั้นๆ เรื่องทะเล
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.2871s | Wall: 0.2871s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-014 out_of_scope ข้อ 14
- Question: Python list comprehension คืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 20.405s | Wall: 20.405s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### OOS-015 out_of_scope ข้อ 15
- Question: JavaScript promise คืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 14.6038s | Wall: 14.6039s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### OOS-016 out_of_scope ข้อ 16
- Question: ช่วยเขียน SQL select เบื้องต้น
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.2401s | Wall: 0.2401s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-017 out_of_scope ข้อ 17
- Question: วิธีสมัคร Gmail ทำยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.2138s | Wall: 0.2139s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-018 out_of_scope ข้อ 18
- Question: แนะนำโน้ตบุ๊กเล่นเกมหน่อย
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `equipment/related_guidance`
- Strategy: `rag/vector`
- Latency: 19.4327s | Wall: 19.4328s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด equipment ตอนนี้ครับ

### OOS-019 out_of_scope ข้อ 19
- Question: iPhone รุ่นไหนคุ้มสุด
- Expected: general_llm_or_decline
- Mode: `pipeline:category_rule_fast_path`
- Route: `general/unknown_domain_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2135s | Wall: 0.2135s
- Sources: rule_contact_phone: https://esports.computing.psu.ac.th/
- Answer: เบอร์ติดต่อที่ปรากฏในระบบจองคือ +66 7627 6004 และ +66 7627 6045 แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### OOS-020 out_of_scope ข้อ 20
- Question: เที่ยวภูเก็ต 1 วันไปไหนดี
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.3203s | Wall: 0.3204s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-021 out_of_scope ข้อ 21
- Question: ร้านอาหารใกล้ฉันมีอะไรบ้าง
- Expected: general_llm_or_decline
- Mode: `pipeline:rules_fast_path`
- Route: `rules/studio_rules`
- Strategy: `fastpath/rulebase`
- Latency: 0.3801s | Wall: 0.3801s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### OOS-022 out_of_scope ข้อ 22
- Question: แผนที่ไปสนามบินภูเก็ต
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.0987s | Wall: 0.0988s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-023 out_of_scope ข้อ 23
- Question: วิธีทำพาสปอร์ต
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.1002s | Wall: 0.1002s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-024 out_of_scope ข้อ 24
- Question: ต่อภาษีรถต้องทำยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.1736s | Wall: 0.1736s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-025 out_of_scope ข้อ 25
- Question: ยื่นภาษีบุคคลธรรมดายังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.2641s | Wall: 0.2642s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-026 out_of_scope ข้อ 26
- Question: เขียน resume ภาษาอังกฤษยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.3138s | Wall: 0.3139s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-027 out_of_scope ข้อ 27
- Question: ช่วยซ้อมสัมภาษณ์งานหน่อย
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.2306s | Wall: 0.2306s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-028 out_of_scope ข้อ 28
- Question: คำว่า resilience แปลว่าอะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.219s | Wall: 0.219s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-029 out_of_scope ข้อ 29
- Question: ทำไมท้องฟ้าถึงเป็นสีฟ้า
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.2092s | Wall: 0.2093s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-030 out_of_scope ข้อ 30
- Question: โลกร้อนเกิดจากอะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.1671s | Wall: 0.1672s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-031 out_of_scope ข้อ 31
- Question: AI คืออะไรแบบง่ายๆ
- Expected: general_llm_or_decline
- Mode: `pipeline:rag_direct_curated`
- Route: `overview/overview_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.1768s | Wall: 0.1768s
- Sources: curated_overview_identity: https://esports.phuket.psu.ac.th/home
- Answer: PSU Esports Studio - Phuket คือศูนย์พัฒนาการเรียนรู้ด้านอีสปอร์ตเพื่อความเป็นเลิศและขับเคลื่อนเศรษฐกิจในพื้นที่ภาคใต้ สาขาภูเก็ต เป็นศูนย์การเรียนรู้ผ่านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์ แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### OOS-032 out_of_scope ข้อ 32
- Question: LLM ทำงานยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.0881s | Wall: 0.0881s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-033 out_of_scope ข้อ 33
- Question: RAG คืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 2.9449s | Wall: 2.945s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### OOS-034 out_of_scope ข้อ 34
- Question: Docker คืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 5.2108s | Wall: 5.2109s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### OOS-035 out_of_scope ข้อ 35
- Question: Git commit กับ push ต่างกันยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.3732s | Wall: 0.3733s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-036 out_of_scope ข้อ 36
- Question: Vercel คืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 4.7333s | Wall: 4.7334s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### OOS-037 out_of_scope ข้อ 37
- Question: Neon database คืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 9.8627s | Wall: 9.8627s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### OOS-038 out_of_scope ข้อ 38
- Question: SQLite ต่างจาก Postgres ยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.2703s | Wall: 0.2703s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-039 out_of_scope ข้อ 39
- Question: ช่วยวางแผนอ่านหนังสือสอบ
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.2942s | Wall: 0.2943s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-040 out_of_scope ข้อ 40
- Question: วิธีจัดการเวลาให้ดีขึ้น
- Expected: general_llm_or_decline
- Mode: `pipeline:schedule_fast_path`
- Route: `schedule/schedule_query`
- Strategy: `fastpath/rulebase`
- Latency: 2.7856s | Wall: 2.7856s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน  รายละเอียดจากตาราง: - Morning คือ 09:00-12:00 - Afternoon คือ 13:00-16:00 - Monday ช่วง Morning 09:00-12:00 เป็น Maintenance* - Monday ช่วง Afternoon 13:00-1...

### OOS-041 out_of_scope ข้อ 41
- Question: วิธีนอนให้หลับง่าย
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.1339s | Wall: 0.134s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-042 out_of_scope ข้อ 42
- Question: ควรดื่มน้ำวันละเท่าไหร่
- Expected: general_llm_or_decline
- Mode: `pipeline:rag_direct_curated`
- Route: `service_fee/service_fee_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.3784s | Wall: 0.3784s
- Sources: curated_service_fee_pc_unknown: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png | curated_user_group_alias_general_student: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png | curated_user_group_alias_psu_student_staff: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
- Answer: บริการ PC ในระบบจองมีระยะเวลา 60 min แต่ในข้อมูลที่ดึงมาและในรูป Service Fee 2026 ยังไม่พบราคาค่าบริการ PC ที่ยืนยันได้ จึงยังไม่ควรคำนวณยอดเงิน PC แบบฟันธง แหล่งข้อมูล: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-S...

### OOS-043 out_of_scope ข้อ 43
- Question: อาหารเช้าควรกินอะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:rules_fast_path`
- Route: `rules/studio_rules`
- Strategy: `fastpath/rulebase`
- Latency: 0.1996s | Wall: 0.1996s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### OOS-044 out_of_scope ข้อ 44
- Question: วิธีปลูกต้นไม้ในห้อง
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.1563s | Wall: 0.1563s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-045 out_of_scope ข้อ 45
- Question: วิธีดูแลกล้องถ่ายรูปเบื้องต้น
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.3228s | Wall: 0.3229s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-046 out_of_scope ข้อ 46
- Question: วิธีดูแลคอมไม่ให้ช้า
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.1328s | Wall: 0.1328s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-047 out_of_scope ข้อ 47
- Question: ทำไม Wi-Fi ช้า
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.0517s | Wall: 0.0517s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-048 out_of_scope ข้อ 48
- Question: วิธีตั้งรหัสผ่านให้ปลอดภัย
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.2816s | Wall: 0.2816s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-049 out_of_scope ข้อ 49
- Question: phishing คืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 7.092s | Wall: 7.0923s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### OOS-050 out_of_scope ข้อ 50
- Question: ช่วยคิด caption ลง Instagram
- Expected: general_llm_or_decline
- Mode: `pipeline:equipment_fast_path`
- Route: `equipment/equipment_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 4.6114s | Wall: 4.6115s
- Sources: home: https://esports.phuket.psu.ac.th/home
- Answer: อุปกรณ์บนหน้า Home:  PC Zone • Gaming PC รุ่น MSI MAG Infinite S3 14th (จำนวน 10 เครื่อง) • Gaming Monitor (จำนวน 10 จอ) • Gaming Chair (จำนวน 10 ตัว) • Gaming Gear ครบชุด ทั้ง Keyboard, Mouse และ Headset  Cockpit Zone • TV ขนาด 65 นิ้ว (จำนวน 2 เครื่อง) • Rac...

### OOS-051 out_of_scope ข้อ 51
- Question: เขียน bio โปรไฟล์ให้หน่อย
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.2666s | Wall: 0.2666s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-052 out_of_scope ข้อ 52
- Question: ช่วยสรุปนิยายที่ฉันชอบได้ไหม
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.3287s | Wall: 0.3288s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-053 out_of_scope ข้อ 53
- Question: วิธีทำบันทึกรายรับรายจ่าย
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.3021s | Wall: 0.3021s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-054 out_of_scope ข้อ 54
- Question: ขอไอเดียของขวัญรับปริญญา
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.2938s | Wall: 0.2938s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-055 out_of_scope ข้อ 55
- Question: ช่วยตั้งชื่อช่อง YouTube
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.0834s | Wall: 0.0834s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-056 out_of_scope ข้อ 56
- Question: วิธีฝึกวาดรูปเบื้องต้น
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.222s | Wall: 0.222s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-057 out_of_scope ข้อ 57
- Question: วันนี้มีบอลคู่ไหน
- Expected: general_llm_or_decline
- Mode: `pipeline:calendar_schedule_fast_path`
- Route: `schedule/schedule_query`
- Strategy: `fastpath/rulebase`
- Latency: 1.1935s | Wall: 1.1936s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: วันนี้ 15/07/2026 (วันพุธ): วันพุธเปิดให้เล่น 09:00-12:00 และ 13:00-16:00 วันที่อ้างอิงของระบบ: วันนี้คือ 15/07/2026 (วันพุธ) ตามเวลาไทย  ปฏิทินไทยของวันที่นี้: ไม่พบวันหยุดไทยหรือเทศกาลในปฏิทินที่บันทึกไว้สำหรับวันที่นี้  รายละเอียดจากตาราง: - วันจันทร์ช่วงเช...

### OOS-058 out_of_scope ข้อ 58
- Question: ตาราง NBA วันนี้
- Expected: general_llm_or_decline
- Mode: `pipeline:calendar_schedule_fast_path`
- Route: `schedule/schedule_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.7421s | Wall: 0.7421s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: วันนี้ 15/07/2026 (วันพุธ): วันพุธเปิดให้เล่น 09:00-12:00 และ 13:00-16:00 วันที่อ้างอิงของระบบ: วันนี้คือ 15/07/2026 (วันพุธ) ตามเวลาไทย  ปฏิทินไทยของวันที่นี้: ไม่พบวันหยุดไทยหรือเทศกาลในปฏิทินที่บันทึกไว้สำหรับวันที่นี้  รายละเอียดจากตาราง: - วันจันทร์ช่วงเช...

### OOS-059 out_of_scope ข้อ 59
- Question: ผลพรีเมียร์ลีกล่าสุด
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.1828s | Wall: 0.1828s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-060 out_of_scope ข้อ 60
- Question: ค่าเงิน USD เป็น THB เท่าไหร่
- Expected: general_llm_or_decline
- Mode: `pipeline:rag_direct_curated`
- Route: `service_fee/service_fee_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.4542s | Wall: 0.4543s
- Sources: curated_user_group_alias_psu_student_staff: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png | curated_service_fee_pc_unknown: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png | curated_user_group_alias_general_student: https://esports.computing.psu.ac.th/wp-content/uploads/2026/01/PSU-Esports-Studio-phuket-SERVICE-FEE-2026.png
- Answer: คำถามที่ใช้คำว่า นักศึกษา ม.อ., นักเรียน ม.อ., เด็ก ม.อ., นักศึกษา PSU, นักเรียน PSU, บุคลากร PSU, staff PSU, PSU student, PSU staff ให้ตีความเป็นกลุ่ม PSU Student and Staff ในตาราง Service Fee 2026 ซึ่งเป็นกลุ่มที่ค่าบริการในภาพระบุว่า Free หรือ 0 บาท สำหรับบ...

### OOS-061 out_of_scope ข้อ 61
- Question: Bitcoin ราคาเท่าไหร่
- Expected: general_llm_or_decline
- Mode: `pipeline:category_rule_fast_path`
- Route: `service_fee/service_fee_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.2653s | Wall: 0.2654s
- Sources: rule_no_answer_crypto_payment: https://esports.computing.psu.ac.th/
- Answer: ยังไม่พบข้อมูลว่าศูนย์รับชำระด้วยคริปโตในฐานข้อมูลที่มี ข้อมูลการชำระเงินที่ยืนยันได้คือชำระโดยโอนเข้าบัญชีธนาคารและแนบสลิปการโอนเงินในระบบจอง แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### OOS-062 out_of_scope ข้อ 62
- Question: ช่วยวางแผนเที่ยวญี่ปุ่น
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.1868s | Wall: 0.1869s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-063 out_of_scope ข้อ 63
- Question: ขอ checklist จัดกระเป๋าเดินทาง
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.3529s | Wall: 0.353s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-064 out_of_scope ข้อ 64
- Question: วิธีจองตั๋วเครื่องบินราคาถูก
- Expected: general_llm_or_decline
- Mode: `pipeline:category_rule_fast_path`
- Route: `service_fee/service_fee_query`
- Strategy: `fastpath/rulebase`
- Latency: 0.6977s | Wall: 0.6977s
- Sources: rule_booking_steps: https://esports.computing.psu.ac.th/
- Answer: ขั้นตอนจองคือ เลือกบริการ เลือกวันและเวลา กรอกข้อมูลผู้ใช้ ตรวจสอบข้อมูล ชำระเงินโดยโอนเข้าบัญชี และแนบสลิปการโอนเงิน แหล่งข้อมูล: https://esports.computing.psu.ac.th/

### OOS-065 out_of_scope ข้อ 65
- Question: ประกันสุขภาพเลือกยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.326s | Wall: 0.326s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-066 out_of_scope ข้อ 66
- Question: บัตรเครดิตใบไหนดี
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.1621s | Wall: 0.1621s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-067 out_of_scope ข้อ 67
- Question: กู้ซื้อบ้านต้องเตรียมอะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.2132s | Wall: 0.2132s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-068 out_of_scope ข้อ 68
- Question: ดอกเบี้ยทบต้นคืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:rag_direct_curated`
- Route: `overview/overview_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.1781s | Wall: 0.1781s
- Sources: curated_overview_identity: https://esports.phuket.psu.ac.th/home
- Answer: PSU Esports Studio - Phuket คือศูนย์พัฒนาการเรียนรู้ด้านอีสปอร์ตเพื่อความเป็นเลิศและขับเคลื่อนเศรษฐกิจในพื้นที่ภาคใต้ สาขาภูเก็ต เป็นศูนย์การเรียนรู้ผ่านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์ แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### OOS-069 out_of_scope ข้อ 69
- Question: วิธีเริ่มลงทุนกองทุนรวม
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.2843s | Wall: 0.2844s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-070 out_of_scope ข้อ 70
- Question: ช่วยเขียนอีเมลขอลางาน
- Expected: general_llm_or_decline
- Mode: `pipeline:category_rule_fast_path`
- Route: `contact/contact_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.2334s | Wall: 0.2335s
- Sources: rule_contact_email: https://esports.phuket.psu.ac.th/Contact-Us
- Answer: อีเมลติดต่อศูนย์คือ psuesportspkt@gmail.com แหล่งข้อมูล: https://esports.phuket.psu.ac.th/Contact-Us

### OOS-071 out_of_scope ข้อ 71
- Question: ช่วยเขียนประกาศรับสมัครงาน
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.325s | Wall: 0.3251s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-072 out_of_scope ข้อ 72
- Question: ช่วยทำสคริปต์นำเสนอ 3 นาที
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.2735s | Wall: 0.2736s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-073 out_of_scope ข้อ 73
- Question: สอนทำ PowerPoint ให้น่าสนใจ
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.2097s | Wall: 0.2097s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-074 out_of_scope ข้อ 74
- Question: วิธีอ่านงบการเงินเบื้องต้น
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.3224s | Wall: 0.3225s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-075 out_of_scope ข้อ 75
- Question: เศรษฐกิจเงินเฟ้อคืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:rag_direct_curated`
- Route: `overview/overview_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.2909s | Wall: 0.291s
- Sources: curated_overview_identity: https://esports.phuket.psu.ac.th/home
- Answer: PSU Esports Studio - Phuket คือศูนย์พัฒนาการเรียนรู้ด้านอีสปอร์ตเพื่อความเป็นเลิศและขับเคลื่อนเศรษฐกิจในพื้นที่ภาคใต้ สาขาภูเก็ต เป็นศูนย์การเรียนรู้ผ่านเกมและอีสปอร์ตของมหาวิทยาลัยสงขลานครินทร์ แหล่งข้อมูล: https://esports.phuket.psu.ac.th/home

### OOS-076 out_of_scope ข้อ 76
- Question: ประวัติศาสตร์สงครามโลกครั้งที่สอง
- Expected: general_llm_or_decline
- Mode: `pipeline:penalty_fast_path`
- Route: `knowledge/knowledge_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.5041s | Wall: 0.5041s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: หากละเมิดกฎอาจถูกระงับสิทธิ์ชั่วคราว 1-7 วันหรือถาวร มีการบันทึกประวัติ และสามารถอุทธรณ์ได้ภายใน 7 วัน แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### OOS-077 out_of_scope ข้อ 77
- Question: ดาวอังคารอยู่ไกลแค่ไหน
- Expected: general_llm_or_decline
- Mode: `pipeline:schedule_fast_path`
- Route: `schedule/schedule_query`
- Strategy: `fastpath/rulebase`
- Latency: 2.3172s | Wall: 2.3172s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: วันอังคารเล่นได้ 09:00-12:00 และ 13:00-16:00 โดยรอบสุดท้ายสิ้นสุด 16:00  รายละเอียดจากตาราง: - วันอังคาร-พฤหัสบดีเปิดตามรอบปกติ - Morning คือ 09:00-12:00 - Afternoon คือ 13:00-16:00 แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### OOS-078 out_of_scope ข้อ 78
- Question: ระบบสุริยะมีดาวอะไรบ้าง
- Expected: general_llm_or_decline
- Mode: `pipeline:rules_fast_path`
- Route: `rules/studio_rules`
- Strategy: `fastpath/rulebase`
- Latency: 0.2602s | Wall: 0.2602s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ห้ามสูบบุหรี่ เสพสารเสพติด ดื่มแอลกอฮอล์ พกอาวุธ เล่นการพนัน ใช้ปลั๊กไฟส่วนตัว หรือเคลื่อนย้ายอุปกรณ์โดยไม่ได้รับอนุญาต แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### OOS-079 out_of_scope ข้อ 79
- Question: ทำไมทะเลถึงเค็ม
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.1123s | Wall: 0.1124s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-080 out_of_scope ข้อ 80
- Question: ช่วยแก้โจทย์คณิตสมการกำลังสอง
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.1564s | Wall: 0.1565s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-081 out_of_scope ข้อ 81
- Question: วิธีจำศัพท์อังกฤษ
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.1372s | Wall: 0.1372s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-082 out_of_scope ข้อ 82
- Question: ฝึกพูดอังกฤษด้วยตัวเองยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.3425s | Wall: 0.3426s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-083 out_of_scope ข้อ 83
- Question: แปลไทยเป็นญี่ปุ่นได้ไหม
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.1848s | Wall: 0.1848s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-084 out_of_scope ข้อ 84
- Question: ช่วยตรวจแกรมมาร์ประโยคอังกฤษ
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.369s | Wall: 0.369s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-085 out_of_scope ข้อ 85
- Question: ทำไมคอมเปิดไม่ติด
- Expected: general_llm_or_decline
- Mode: `pipeline:schedule_fast_path`
- Route: `schedule/schedule_query`
- Strategy: `fastpath/rulebase`
- Latency: 1.53s | Wall: 1.53s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: เวลาที่มีในตารางคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 แต่วันจันทร์ช่วงเช้าเป็น Maintenance*  รายละเอียดจากตาราง: - Morning คือ 09:00-12:00 - Afternoon คือ 13:00-16:00 - Monday ช่วง Morning 09:00-12:00 เป็น Maintenance* - Monday ช่วง Afternoon 13:00...

### OOS-086 out_of_scope ข้อ 86
- Question: Windows update ค้างทำยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.2395s | Wall: 0.2396s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-087 out_of_scope ข้อ 87
- Question: ลืมรหัสผ่าน Facebook ทำยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:booking_howto_fast_path`
- Route: `contact/contact_lookup`
- Strategy: `fastpath/rulebase`
- Latency: 0.2778s | Wall: 0.2779s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: จองคิวเล่นเกม/ใช้อุปกรณ์ได้ผ่านระบบจองออนไลน์ครับ ขั้นตอนโดยสรุปคือ 1) เลือกบริการหรือโซนที่ต้องการใช้ 2) เลือกวันและรอบเวลา 3) กรอก Student ID/Staff ID/National ID ชื่อ นามสกุล อีเมล และเบอร์โทรศัพท์ 4) ตรวจสอบข้อมูลและชำระเงินโดยโอนเข้าบัญชีที่ระบบแจ้ง 5) แน...

### OOS-088 out_of_scope ข้อ 88
- Question: บัญชีโดนแฮกควรทำยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:schedule_fast_path`
- Route: `schedule/schedule_query`
- Strategy: `fastpath/rulebase`
- Latency: 2.398s | Wall: 2.398s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน  รายละเอียดจากตาราง: - Morning คือ 09:00-12:00 - Afternoon คือ 13:00-16:00 - Monday ช่วง Morning 09:00-12:00 เป็น Maintenance* - Monday ช่วง Afternoon 13:00-1...

### OOS-089 out_of_scope ข้อ 89
- Question: ทำ portfolio สมัครงานยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.2737s | Wall: 0.2738s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-090 out_of_scope ข้อ 90
- Question: เรียนสาย data ต้องเริ่มจากอะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.3637s | Wall: 0.3637s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-091 out_of_scope ข้อ 91
- Question: Data analyst ใช้เครื่องมืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.2851s | Wall: 0.2852s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-092 out_of_scope ข้อ 92
- Question: Machine learning ต่างจาก deep learning ยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.4753s | Wall: 0.4753s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-093 out_of_scope ข้อ 93
- Question: Prompt engineering คืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:no_answer`
- Route: `games/game_detail_lookup`
- Strategy: `rag/vector`
- Latency: 14.6098s | Wall: 14.6098s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: ยังไม่พบข้อมูลที่ยืนยันได้ในฐานข้อมูลของ PSU Esports Studio - Phuket สำหรับหมวด games ตอนนี้ครับ

### OOS-094 out_of_scope ข้อ 94
- Question: ช่วยคิด business model ร้านชา
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.2792s | Wall: 0.2792s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-095 out_of_scope ข้อ 95
- Question: วิธีทำแบบสอบถามออนไลน์
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.2519s | Wall: 0.2519s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-096 out_of_scope ข้อ 96
- Question: ทำ infographic ด้วยเครื่องมืออะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.3931s | Wall: 0.3932s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว

### OOS-097 out_of_scope ข้อ 97
- Question: เพลงฮิตตอนนี้มีอะไรบ้าง
- Expected: general_llm_or_decline
- Mode: `pipeline:experimental_rag_no_context`
- Route: `schedule/schedule_query`
- Strategy: `rag/vector`
- Latency: 0.4383s | Wall: 0.4383s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: โหมดทดลอง RAG: ยังไม่มี context ที่โยงกับคำถามนี้ได้ชัดในฐานข้อมูลหมวด schedule ถ้าต้องการให้ตอบได้ ควรเพิ่ม fact/card หรือข้อมูลจริงของเรื่องนั้นเข้า knowledge base ก่อน

### OOS-098 out_of_scope ข้อ 98
- Question: หนังน่าดูปีนี้มีเรื่องอะไร
- Expected: general_llm_or_decline
- Mode: `pipeline:schedule_fast_path`
- Route: `schedule/schedule_query`
- Strategy: `fastpath/rulebase`
- Latency: 2.9784s | Wall: 2.9785s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: เวลาบริการที่มีในข้อมูลคือ Morning 09:00-12:00 และ Afternoon 13:00-16:00 โดยมีช่วง Maintenance บางวัน  รายละเอียดจากตาราง: - Morning คือ 09:00-12:00 - Afternoon คือ 13:00-16:00 - Monday ช่วง Morning 09:00-12:00 เป็น Maintenance* - Monday ช่วง Afternoon 13:00-1...

### OOS-099 out_of_scope ข้อ 99
- Question: ช่วยคิดเมนูอาหารเย็น
- Expected: general_llm_or_decline
- Mode: `pipeline:rules_fast_path`
- Route: `rules/studio_rules`
- Strategy: `fastpath/rulebase`
- Latency: 0.2246s | Wall: 0.2246s
- Sources: Reservation: https://esports.computing.psu.ac.th/reservation
- Answer: อนุญาตให้รับประทานอาหารและเครื่องดื่มเฉพาะในพื้นที่ที่กำหนดเท่านั้น แหล่งข้อมูล: https://esports.computing.psu.ac.th/reservation

### OOS-100 out_of_scope ข้อ 100
- Question: ทำกาแฟลาเต้เองที่บ้านยังไง
- Expected: general_llm_or_decline
- Mode: `pipeline:general_llm_disabled`
- Route: `general/unknown_domain_query`
- Strategy: `llm`
- Latency: 0.3043s | Wall: 0.3044s
- Sources: -
- Answer: คำถามนี้ถูกจัดเป็นคำถามทั่วไปนอกฐานข้อมูล PSU Esports Studio - Phuket แล้วครับ ตอนนี้โหมดตอบจากความรู้ทั่วไปของ Local LLM ยังไม่ได้เปิดในสภาพแวดล้อมนี้ จึงไม่ดึงข้อมูลศูนย์มาตอบแทนเพื่อเลี่ยงคำตอบมั่ว
