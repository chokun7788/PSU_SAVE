# 13 - PSU Esports AI ChatBot: Local vs API

โฟลเดอร์นี้ทำขึ้นเพื่อเปรียบเทียบการทำ AI Chatbot สำหรับเว็บ PSU Esports Studio - Phuket แบบละเอียด 2 แนวทาง:

1. ใช้ LLM ผ่าน API
2. ใช้ LLM แบบ Local / Self-hosted

พร้อมไฟล์เปรียบเทียบ วิธี deploy เครื่องมือที่ควรใช้ เทคนิคที่ต้องรู้ และ checklist สำหรับทำงานจริงภายในเวลา 2 เดือน

---

## ควรอ่านตามลำดับนี้

### 0. ภาพรวมร่วมกัน

1. `00_overview/01_โจทย์และเป้าหมาย.md`
2. `00_overview/02_Architecture_ร่วมกันของทั้งสองแบบ.md`

### 1. แบบใช้ API

3. `01_API_Approach/README_API.md`
4. `01_API_Approach/01_Model_Selection_API.md`
5. `01_API_Approach/02_Tools_Stack_API.md`
6. `01_API_Approach/03_Deployment_API.md`
7. `01_API_Approach/04_Cost_Optimization_API.md`

### 2. แบบ Local / Self-hosted

8. `02_Local_Approach/README_LOCAL.md`
9. `02_Local_Approach/01_Model_Selection_Local.md`
10. `02_Local_Approach/02_Tools_Stack_Local.md`
11. `02_Local_Approach/03_Deployment_Local.md`
12. `02_Local_Approach/04_GPU_Server_Sizing.md`
13. `02_Local_Approach/05_Optimization_Techniques_Local.md`

### 3. เปรียบเทียบและตัดสินใจ

14. `03_Comparison/01_API_vs_Local_Comparison.md`
15. `03_Comparison/02_Decision_Matrix.md`
16. `03_Comparison/03_Two_Month_Roadmap_Both_Paths.md`
17. `03_Comparison/04_Final_Recommendation_For_This_Project.md`

### 4. Deploy และ Production

18. `04_Deployment/01_Docker_Compose_Examples.md`
19. `04_Deployment/02_Cloud_Options.md`
20. `04_Deployment/03_Production_Checklist.md`

### 5. Tools, Checklist, Templates

21. `05_Tools_Checklists/Tool_List_By_Purpose.md`
22. `05_Tools_Checklists/Evaluation_Monitoring_Checklist.md`
23. `06_Templates/env_templates.md`
24. `06_Templates/system_prompts.md`
25. `06_Templates/cost_calculation_template.md`
26. `diagrams/local_vs_api_mermaid.md`
27. `99_sources.md`

---

## สรุปคำแนะนำหลัก

ถ้ามีเวลา 2 เดือนและต้อง deploy จริง:

```text
เส้นทางที่ปลอดภัยสุด:
API-based RAG ก่อน
แล้วทำ Local model เป็น benchmark และ cost-saving path
```

ถ้าอยากลด cost ระยะยาว:

```text
ทำ Hybrid
คำถามง่าย -> curated facts/cache
คำถามทั่วไป -> local model ถ้าคุณภาพผ่าน
คำถามยาก -> API fallback
```

---

## นิยามสั้น ๆ

### API-based AI

ใช้โมเดลจากผู้ให้บริการ เช่น OpenAI, Google Gemini, Anthropic Claude หรือ Typhoon API โดยเราไม่ต้องรันโมเดลเอง

เหมาะกับ:

- ต้อง deploy ให้ทัน
- ยังไม่มี GPU
- ต้องการคุณภาพดีตั้งแต่แรก
- ทีมยังไม่เชี่ยวชาญ LLM serving

### Local / Self-hosted AI

ดาวน์โหลด open-weight model มารันเอง เช่นผ่าน Ollama, vLLM, llama.cpp หรือ Hugging Face TGI

เหมาะกับ:

- มี GPU หรือเช่า GPU ได้
- ต้องการควบคุมข้อมูล/ระบบมากขึ้น
- traffic สูงจนค่า API เริ่มแพง
- มีเวลาทำ benchmark และดูแล infrastructure

---

## โครงระบบที่ควรใช้ร่วมกัน

ไม่ว่าจะเลือก API หรือ Local แกนระบบควรเหมือนกัน:

```text
Website data
-> scrape/clean
-> chunk
-> embedding
-> vector database
-> retrieve
-> rerank/filter
-> build context
-> LLM answer
-> citation
-> log/evaluate
```

ความต่างหลักคือ "LLM answer" ใช้ API หรือ local model
