"""Prefer a named physical control to generic action-description overlap."""
import re
from dataclasses import dataclass
from app.core.typo_similarity import osa_distance

def _key(value):return re.sub(r'[^a-z0-9\u0e00-\u0e7f]','',str(value).casefold())

@dataclass(frozen=True)
class ButtonSelection:
    observed: str
    rows: tuple[dict,...]
    status: str

def explicit_button_selection(query,rows):
    patterns=(r'ปุ่ม\s*(.+?)(?=\s*(?:ใช้|ทำ|คือ|บน|ของ|ใน|อะไร|[?]|$))',
              r'\b(?:does|do|is|are)\s+(?:the\s+)?(.+?)\s+(?:button|key)\b',
              r'\b(?:press|use|using)\s+(?:the\s+)?(.+?)\s+(?:button|key)\b')
    match=next((m for pattern in patterns if (m:=re.search(pattern,query,re.I))),None)
    if match is None:return None
    observed=match.group(1).strip();target=_key(observed)
    if not target or len(target)>65:return None
    exact=[];short=[];near=[]
    for row in rows:
        labels=[str(row.get('button') or ''),*[str(v) for v in row.get('buttons',[])]]
        aliases=[]
        for label in labels:
            aliases += [label,re.sub(r'\([^)]*\)','',label).strip()]
            aliases += re.split(r'\s*/\s*',re.sub(r'\([^)]*\)','',label).strip())
        keys={_key(alias) for alias in aliases if alias}
        if target==_key(labels[0]):exact.append(row)
        elif target in keys:short.append(row)
        elif not re.search(r'\d',target) and len(target)>=4 and any(not re.search(r'\d',key) and osa_distance(target,key)==1 for key in keys if len(key)>=4):near.append(row)
    if exact:return ButtonSelection(observed,tuple(exact),'exact')
    if short:return ButtonSelection(observed,tuple(short),'source_alias')
    if len(near)==1:return ButtonSelection(observed,tuple(near),'unique_one_edit')
    if re.fullmatch(r'[a-z]+\d+|dpad(?:up|down|left|right)?',target):return ButtonSelection(observed,(),'unknown_physical_identifier')
    return None
