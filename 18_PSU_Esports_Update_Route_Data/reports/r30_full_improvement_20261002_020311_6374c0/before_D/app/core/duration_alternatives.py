"""Read explicitly connected duration choices without changing other numbers."""
from dataclasses import dataclass
import re

_WORDS={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'หนึ่ง':1,'สอง':2,'สาม':3,'สี่':4,'ห้า':5,'ครึ่ง':.5,'half':.5}
_NUM=r'(?:\d+(?:\.\d+)?|'+ '|'.join(_WORDS)+r')'
_UNIT=r'(?:ชั่วโมง|ชม\.?|hours?|hrs?|นาที|minutes?|mins?)'
_JOIN=r'(?:หรือ|และ|กับ|or|and|versus|vs\.?)'
_DURATION=re.compile(r'(?<![0-9A-Za-z:.])(?P<n>'+_NUM+r')\s*(?P<u>'+_UNIT+r')',re.I)
_SHARED=re.compile(r'(?<![0-9A-Za-z:.])(?P<a>'+_NUM+r')\s*(?:'+_JOIN+r')\s*(?P<b>'+_NUM+r')\s*(?P<u>'+_UNIT+r')',re.I)

def _minutes(number,unit):
    value=_WORDS.get(number.casefold())
    value=float(number) if value is None else value
    return int(value*60) if re.match(r'ชั่วโมง|ชม|hour|hr',unit,re.I) else int(value)

@dataclass(frozen=True)
class DurationAlternatives:
    minutes: tuple[int,...]
    start: int
    end: int

    def for_minutes(self,query: str,value: int)->str:
        return query[:self.start]+f'{value} minutes'+query[self.end:]

def parse_duration_alternatives(query: str)->DurationAlternatives|None:
    shared=_SHARED.search(query)
    if shared:
        values=tuple(dict.fromkeys(_minutes(shared[g],shared['u']) for g in ('a','b')))
        if len(values)>1 and min(values)>0:
            return DurationAlternatives(values,shared.start(),shared.end())
    matches=list(_DURATION.finditer(query))
    for index,left in enumerate(matches[:-1]):
        group=[left]
        for right in matches[index+1:]:
            connector=query[group[-1].end():right.start()].strip(' ,')
            if not re.fullmatch(_JOIN,connector,re.I):break
            group.append(right)
        if len(group)>1:
            values=tuple(dict.fromkeys(_minutes(m['n'],m['u']) for m in group))
            if len(values)>1 and min(values)>0:
                return DurationAlternatives(values,group[0].start(),group[-1].end())
    return None
