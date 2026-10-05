"""Explicit source task signals shared by answers and their validators."""
import re
from app.core.normalization import SERVICE_ALIASES, contains_alias

def fee_comparison_query(query: str) -> bool:
    services = [key for key, aliases in SERVICE_ALIASES.items()
                if contains_alias(query, aliases, fuzzy=False)[0]]
    comparison = re.search(r'แพงกว่า|ถูกกว่า|(?:เทียบ|ต่างกัน).*ราคา|ราคา.*(?:เทียบ|ต่างกัน)|\b(?:more expensive|cheaper)\b|\bcompare\b.*\b(?:prices?|fees?)\b|\b(?:prices?|fees?)\b.*\bcompare\b', query, re.I)
    return len(services) >= 2 and bool(comparison)

def payment_method_query(query: str) -> bool:
    return bool(re.search(r'(?:จ่าย|ชำระ)(?:เงิน)?(?:ยังไง|อย่างไร)|วิธี(?:จ่าย|ชำระ)|โอนเงิน|เลขบัญชี|\b(?:how\s+(?:do|can)\s+(?:i|we)\s+pay|payment\s+method|bank\s+account|(?:pay\s+by|make\s+a?)\s+bank\s+transfer)\b', query, re.I))

def speech_rule_query(query: str) -> bool:
    thai = re.search(r'คำพูด(?:ไม่)?เหมาะสม|ดูหมิ่น|เสียดสี|เสียงดังเกิน', query)
    english = re.search(r'\b(?:offensive\s+language|inappropriate\s+speech|insult(?:s|ing)?|mock(?:ing)?\s+(?:other\s+)?people)\b', query, re.I)
    context = re.search(r'ศูนย์|คำพูด|กฎ|ข้อห้าม|\b(?:studio|rules?|allowed|may|can\s+i)\b', query, re.I)
    return bool((thai or english) and context)
