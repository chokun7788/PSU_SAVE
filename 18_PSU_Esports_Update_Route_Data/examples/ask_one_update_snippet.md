# Ask One Snippet

เอาโค้ดนี้ไปวางใน notebook เพื่อดู route และคำตอบจาก calculator/rule แบบเร็ว:

```python
import sys
from pathlib import Path

UPDATE_DIR = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
sys.path.insert(0, str(UPDATE_DIR))

from app.core.router import route_question
from app.calculator.service_fee import answer_service_fee
from app.rules.matcher import RuleMatcher

matcher = RuleMatcher.default()

def ask_update(question: str):
    decision = route_question(question, matcher=matcher)
    print("คำถาม:", question)
    print("Route:", decision.route)
    print("Confidence:", decision.confidence)
    print("Reason:", decision.reason)
    if decision.route == "deterministic_calculator":
        print(decision.metadata["answer"])
    elif decision.route == "rule_fast_path":
        print(decision.metadata["answer"])
    else:
        print("Route นี้ควรส่งต่อเข้า curated RAG / vector RAG / LLM ในระบบหลัก")
    return decision

ask_update("ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่")
```
