# Ask Fast Runtime Snippet

ใช้ถามทีละข้อโดยไม่โหลด LLM:

```python
import sys
from pathlib import Path

UPDATE_DIR = Path(r"C:\Users\Chokhun\Downloads\Learn-LLM\18_PSU_Esports_Update_Route_Data")
sys.path.insert(0, str(UPDATE_DIR))

from app.runtime.fast_answer import answer_question_fast

def ask_fast(question: str):
    answer, hits, elapsed, mode = answer_question_fast(question)
    print("คำถาม:", question)
    print("Route:", mode)
    print("Elapsed:", elapsed, "sec")
    print()
    print(answer)
    print()
    print("Sources:", [hit.get("id") for hit in hits])
    return answer, hits, elapsed, mode

ask_fast("ต่างมหาลัย เล่น vr ครึ่ง ชม เท่าไหร่")
ask_fast("วันจันทร์เปิดให้เล่นกี่โมง")
ask_fast("คอมมีวาโลไหม")
```
