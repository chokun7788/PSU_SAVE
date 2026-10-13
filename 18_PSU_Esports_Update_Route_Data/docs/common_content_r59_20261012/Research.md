# งานวิจัย → สาเหตุ → วิธีใช้ในระบบ r59

วันที่ค้น 2026-10-12; เป็น engineering literature search ระดับ Standard เพื่อแก้ระบบ ไม่ใช่ systematic review หรือหลักฐานรับรอง production accuracy

## วิธีค้นและข้อจำกัดที่เกิดขึ้นจริง

อ่าน paper-search-pro SKILL, agent_mode, tier_decision, setup และ RCS rubric ใช้เส้นทาง headless สำหรับนำงานวิจัยมาประกอบการพัฒนา ไม่ผลิต HTML/PRISMA ซึ่งไม่ใช่สิ่งที่ผู้ใช้ขอ ตัวค้น agent_search ไม่สามารถใช้งานได้ เพราะ config ไม่มี OpenAlex/Semantic Scholar API key; ไม่แก้ config หรือสร้าง credential เอง ใช้ web search + เปิดต้นฉบับ ACL Anthology/AAAI/arXiv/วารสารไทย/คลังผู้วิจัยทดแทน

ผลเสีย: ไม่มี federated dedup, quota/saturation metrics และ citation graph อัตโนมัติของ skill จึงไม่อ้างว่า literature ครบถ้วนหรือ saturated วิธีเติม: ตั้งค่า skill ตาม references/setup.md แล้วรันชุดคำค้นด้านล่างต่อ พร้อม backward/forward citations คัดซ้ำตาม title/DOI ด้วยตนเองในรายการที่ใช้ ไม่ใช้ citation count เป็นคะแนนความเหมาะสม

หัวข้อค้น 3 กลุ่ม: (schema-guided OR description-driven OR dialogue state) AND (robustness OR paraphrase); (constrained decoding OR structured generation) AND (JSON schema OR semantic correctness); (behavioral testing OR spelling correction OR calibration) AND (NLP OR question answering OR Thai). เสริมคำค้นชื่อ D3ST/SGD-X/PICARD/CheckList และงานอ้างอิง D3ST ที่ Grounding และ SDT เชื่อมถึง ไม่มีจำกัดปีชั้น foundational; เพิ่มชั้นปี 2025–2026 ของ structured decoding/uncertainty/Thai

อ่านหลักฐานระดับ abstract/หน้าต้นฉบับและส่วนวิธีที่เข้าถึงได้ ไม่อ้างว่า reproduce training ของบทความ ไม่ใช้ผลตัวเลขใน paper เป็นผลของ PSU ไม่ใช้เว็บสรุป paper แทนแหล่งหลัก

## รายการคัดใช้ (RCS ประเมินเองตาม rubric)

### P01 SGD — RCS 7

Rastogi et al. (2020), *Towards Scalable Multi-Domain Conversational Agents: The Schema-Guided Dialogue Dataset*. AAAI. DOI 10.1609/aaai.v34i05.6394. [ต้นฉบับ](https://ojs.aaai.org/index.php/AAAI/article/view/6394)

บทความเสนอ prediction เหนือ intents/slots ที่เปลี่ยนตาม service โดยส่งคำอธิบายภาษาธรรมชาติของ schema ให้โมเดล เหมาะกับ common format ที่เพิ่มรายการใหม่และมีหมวดสัมพันธ์กัน

**การประยุกต์ของเรา:** allowed fields ต้องสร้างจาก CATALOG และ selected kinds ไม่รวมทุกหัวข้อโดยไม่ดูชนิด record ใช้ source typed fields เป็น facts ไม่ให้ LLM เขียนข้อเท็จจริง ไม่ได้ติดตั้งหรือฝึกโมเดล SGD จึงไม่เรียกผลนี้ว่า zero-shot guarantee

### P02 D3ST — RCS 7

Zhao et al. (2022), *Description-Driven Task-Oriented Dialog Modeling*. [ต้นฉบับ arXiv 2201.08904](https://arxiv.org/abs/2201.08904)

ใช้ schema descriptions และ index picking สำหรับ dialogue state tracking แทนการผูกกับชื่อ slot ที่เป็นรหัสลอย ความหมายของช่องและบทสนทนาเป็น input สำคัญ

**การประยุกต์:** prompt ส่ง Thai description, canonical English phrase, selected kinds และ enum ของ fields; ไม่ส่ง technical record ID เป็น platform choice fast path ใช้ความหมาย attribute ที่ใช้ซ้ำ across records ไม่ใช้ชื่อ fixture เป็นเงื่อนไข โมเดลที่เรามีเป็น Typhoon 4B ไม่ใช่ T5 ที่ฝึกตามบทความ จึงยังต้องวัด semantic correctness เอง

### P03 SGD-X — RCS 7

Lee et al. (2022), *SGD-X: A Benchmark for Robust Generalization in Schema-Guided Dialogue Systems*. AAAI. DOI 10.1609/aaai.v36i10.21341. [ต้นฉบับ](https://ojs.aaai.org/index.php/AAAI/article/view/21341)

พบว่าระบบ state tracking ยังไวต่อรูปแบบชื่อและคำอธิบาย schema แม้ความหมายใกล้กัน และเสนอ augmentation เพื่อเพิ่ม robustness

**การประยุกต์:** canonical/description query ที่ผ่านแล้วไม่เพียงพอ ต้องแยก natural/paraphrase/followup/multi-field/typo ไทยและอังกฤษ และบันทึก pass→fail ทุกครั้ง การเพิ่ม description เพียงอย่างเดียวไม่แก้คำถามทั้งหมด

### P04 Show, Don’t Tell — RCS 7

Gupta et al. (2022), *Show, Don’t Tell: Demonstrations Outperform Descriptions for Schema-Guided Task-Oriented Dialogue*. NAACL. [ต้นฉบับ](https://aclanthology.org/2022.naacl-main.336/)

การใช้ตัวอย่างบทสนทนาที่มี label แสดงความหมาย schema ทำได้ดีกว่าคำอธิบายเพียงอย่างเดียวในชุดประเมินของบทความ

**การประยุกต์:** ถ้า field ยังสับสน ให้เพิ่ม developer-maintained semantic examples ของ field ไม่เก็บทุก paraphrase ของผู้ใช้ และแยกตัวอย่างสำหรับ planner จาก holdout ที่ใช้ตัดสินผล **รอบนี้ยังไม่ได้ใช้ in-context demonstration bank หรือ fine-tune** เพื่อไม่ทำให้ผลเกินหลักฐาน

### P05 Grounding D3ST — RCS 6

Coca et al. (2023), *Grounding Description-Driven Dialogue State Trackers with Knowledge-Seeking Turns*. SIGDIAL. [ต้นฉบับ](https://aclanthology.org/2023.sigdial-1.42/)

ใช้ knowledge-seeking turns ที่สัมพันธ์กับ schema ใน prompts ของการ fine-tune/inference เพิ่มความทนต่อความต่างของ schema descriptions

**การประยุกต์:** เก็บคำถามจริงและ slot ที่ควรตอบเป็น evidence bank สำหรับปรับ parser ในอนาคต ไม่ป้อน gold expected_fields ของ regression เข้า planner การแก้ r59 เป็น bounded interpretation + deterministic reader ไม่ใช่การฝึก model ตามงานนี้

### P06 PICARD — RCS 6

Scholak et al. (2021), *PICARD: Parsing Incrementally for Constrained Auto-Regressive Decoding from Language Models*. EMNLP. [ต้นฉบับ](https://aclanthology.org/2021.emnlp-main.779/)

คัด token ที่ใช้ไม่ได้ระหว่าง decoding เพื่อให้ output อยู่ใน formal language ที่ต้องการ งานทดลองหลักเป็น text-to-SQL

**การประยุกต์:** ใช้ Ollama JSON Schema enum เป็นข้อจำกัด field/platform แล้วมี validator ซ้ำ ไม่ใช้ PICARD parser โดยตรง และไม่ให้ chatbot สร้าง SQL จากคำถาม การประยุกต์ข้าม task ต้องวัดผลเอง

### P07 JSONSchemaBench — RCS 7

Geng et al. (2025), arXiv 2501.10868; หน้าต้นฉบับปัจจุบันใช้ชื่อ *JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models*. [ต้นฉบับ](https://arxiv.org/abs/2501.10868)

ประเมิน constrained generation แยก efficiency, constraint coverage และ output quality ไม่ควรตีความ schema validity ว่าเท่ากับความถูกต้องของงาน

**การประยุกต์:** log แยก HTTP/Ollama success, decoded JSON, schema accepted, requested-field correctness, final coverage; enum จำกัดค่าที่ใช้ได้แต่เลือก field ผิดที่ยังอยู่ใน enum ได้ จึงต้องตรวจ expected fields อิสระ

### P08 CheckList — RCS 7

Ribeiro et al. (2020), *Beyond Accuracy: Behavioral Testing of NLP Models with CheckList*. ACL. [ต้นฉบับ](https://aclanthology.org/2020.acl-main.442/)

เสนอการทดสอบความสามารถและชนิด behavior หลายแบบ ผล accuracy รวมอาจปิดบังปัญหาที่ใช้งานจริง

**การประยุกต์:** กลุ่มทดสอบ quantity, negation, noisy name, context switch, compound request, unrelated request และ unknown/false/zero; gold ของ reference ต้องไม่เรียก title() ตัวเดียวกับ implementation เพื่อหลีกเลี่ยงผ่านพร้อมกันทั้งที่แสดง ID ผิด

### P09 Correctness & Faithfulness — RCS 7

Adlakha et al. (2024), *Evaluating Correctness and Faithfulness of Instruction-Following Models for Question Answering*. TACL. [ต้นฉบับ](https://aclanthology.org/2024.tacl-1.38/)

แยกการตอบความต้องการข้อมูลของผู้ใช้จากการยึดหลักฐานต้นทาง และชี้ปัญหาของ EM/F1 เมื่อคำตอบยาวพร้อมข้อมูลเสริม

**การประยุกต์:** แยก requested fields recall, unrequested fields, source/status correctness และ answer length; runtime coverage ใช้ plan ที่เลือกแล้วจึงตรวจ semantic intent ไม่ได้ทั้งหมด ไม่ให้หน้าเว็บเขียน validated=true โดยไม่มี coverage check จริง

### P10 Noisy-channel spelling — RCS 6

Brill & Moore (2000), *An Improved Error Model for Noisy Channel Spelling Correction*. ACL. DOI 10.3115/1075218.1075255. [ต้นฉบับ](https://aclanthology.org/P00-1037/)

ปรับ channel model ด้วย string edits เพื่อเลือกคำต้นทางที่อธิบาย typo ได้ งานไม่ได้เป็นระบบภาษาไทยของ PSU

**การประยุกต์:** character repetition เป็น error channel ที่ระบุได้ จึงรับชื่อหลังแก้เบิ้ลหนึ่งตัวเมื่อมี candidate เดียว exact name ชนะ correction และปกป้องตัวเลข ไม่ใช่ probabilistic noisy-channel เต็มรูปแบบ ไม่ลด fuzzy margin ทั้งระบบเพื่อให้ผ่าน 11 เคส

### P11 Thai soft keyboard — RCS 4

Suwansophon & Siriborvornratanakul (2023), *Combining Key-target Resizing and LSTM Language Model to Reduce Typos in Thai Soft Keyboard*. [วารสารต้นฉบับ](https://ph01.tci-thaijo.org/index.php/kmutnb-journal/article/view/252143)

ศึกษาการรวม language model กับ key-target resizing ของแป้นไทยมือถือ การป้องกัน typo ที่ keyboard ไม่ใช่การอ่าน intent ฝั่ง chatbot โดยตรง จึงคะแนนเกี่ยวข้องต่ำกว่า schema parsing

**การประยุกต์:** keyboard neighbors อาจเป็น candidate features ในอนาคต แต่ไม่บังคับแทนคำทุกครั้ง การมีหลาย layouts และสระ/วรรณยุกต์ต้องทดสอบแยก ไม่อ้างว่าภาษาไทยผิดมากกว่าอังกฤษเพราะ keyboard อย่างเดียว

### P12 Natural/synthetic noise — RCS 5

Belinkov & Bisk (2018), *Synthetic and Natural Noise Both Break Neural Machine Translation*. ICLR. [ผู้วิจัยเผยแพร่ฉบับเต็ม](https://belinkov.com/assets/pdf/iclr2018.pdf)

แสดงผลของ noise ทั้งสร้างขึ้นและตามธรรมชาติใน NMT และศึกษาวิธีฝึกให้ robust เป็นคนละ task กับ chatbot

**การประยุกต์:** repeat-only synthetic cases ยังไม่แทนข้อความจริงที่ผิดหลายตำแหน่ง ต้องเก็บ natural noise และ holdout ก่อนประเมินความทนจริง ไม่สรุปว่าผลรอบนี้เท่ากับแก้ทุกภาษาแล้ว

## งานใหม่ที่ตรวจเจอแต่ไม่ใช้เป็นฐานตัดสินการแก้

- [SConU (ACL 2025)](https://aclanthology.org/2025.acl-long.934/) — RCS 4; conformal calibration ต้องมีชุด calibration และ assumptions เหมาะสม ยังไม่มีข้อมูลพอจะอ้าง guarantee สำหรับ PSU
- [Chavan arXiv 2609.23742](https://arxiv.org/abs/2609.23742) — RCS 5, recent preprint; รายการผลและ README repo ปัจจุบันไม่ตรงรายละเอียดบางจุด จึงใช้เพียงชี้ประเด็น semantic gap ไม่คัดตัวเลขมาเป็นเหตุผลเปลี่ยนโมเดล
- P.L.I.C.K. (คลังผู้วิจัย Mahidol 2026) — RCS 3; เน้น keyboard switching ไม่แก้ source/slot intent ของระบบนี้
- Schema Reinforcement Learning (arXiv 2502.18878) — RCS 4; ต้อง training pipeline/compute/data เพิ่ม ไม่จำเป็นต่อ bug fixes ที่ระบุได้ตอนนี้

## สรุปเหตุและวิธีที่เหมาะกับระบบนี้ (ข้อวิเคราะห์ของเรา)

1. ข้อมูลครบแต่ผิด เพราะ query→field mapper เล็กกว่า catalog และเลือก intent ก่อนตัดชื่อ; การเพิ่มข้อมูลจึงไม่ได้เพิ่มความสามารถอ่านคำถามโดยอัตโนมัติ
2. คำถามหลายส่วนใช้ union ของ slots ที่ตรงกับ scope และตรวจทุก clause; ไม่เลือก keyword แรกแล้วจบ
3. รูปแบบใหม่ใช้ schema-aware bounded planner เป็น fallback ไม่ให้โมเดลเดาข้อเท็จจริง; จะเร็วและเสถียรกว่าบังคับ LLM อ่าน facts ทั้งฐานสำหรับคำถามง่าย แต่ไม่มี benchmark latency ในรอบนี้
4. ต่อเนื่องต้องรักษา entity และ pending need จากประวัติอย่างมีขอบเขต; ไม่แก้ทุกกรณีด้วย embedding คำถามเดี่ยว
5. Unknown คือสถานะ fact ที่เจ้าของไม่ได้ยืนยัน; parse ไม่ได้/unsupported/ambiguous เป็นคนละสถานะ ห้ามรวมเป็น “ไม่มีข้อมูล”
6. Coverage gate ป้องกัน reader/render ตก field ได้ แต่ไม่ได้พิสูจน์ plan ตรง intent จึงต้องมีทั้ง tests และ real feedback
7. รอบนี้ใช้ deterministic semantics + bounded LLM + typed reader; ยังไม่ได้ใช้ vector embeddings, train DST, confidence calibration หรือ noisy-channel trained model จึงไม่อ้างชื่อเหล่านั้นเป็นเทคโนโลยีที่ติดตั้งแล้ว
