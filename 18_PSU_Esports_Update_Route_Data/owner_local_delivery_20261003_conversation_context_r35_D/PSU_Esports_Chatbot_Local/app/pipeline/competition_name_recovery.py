"""Recover a unique registered long name as a whole span, keeping editions.

The caller supplies the rulebook registry. This module never normalizes query
intent, short IDs, quantities, or a guessed unsupported game.
"""
from __future__ import annotations
from collections import Counter
from dataclasses import dataclass
from functools import lru_cache
import re
import unicodedata

@dataclass(frozen=True)
class NameRecovery:
    game_id: str
    start: int
    end: int
    original: str
    canonical: str
    edits: int
    edit_fraction: float
    registered_alias: str = ''

def _compact(text: str):
    chars=[];positions=[]
    for i,ch in enumerate(text):
        for c in unicodedata.normalize('NFKC',ch).casefold():
            if c.isalnum() or '\u0e00' <= c <= '\u0e7f':
                if '\u0e50' <= c <= '\u0e59':c=str(ord(c)-ord('\u0e50'))
                chars.append(c);positions.append(i)
    return ''.join(chars),positions

def _osa(a: str,b: str,budget: int) -> int:
    if abs(len(a)-len(b))>budget:return budget+1
    prev=list(range(len(b)+1));older=None
    for i,ca in enumerate(a,1):
        row=[i]
        for j,cb in enumerate(b,1):
            value=min(row[-1]+1,prev[j]+1,prev[j-1]+(ca!=cb))
            if older is not None and i>1 and j>1 and ca==b[j-2] and a[i-2]==cb:value=min(value,older[j-2]+1)
            row.append(value)
        if min(row)>budget:return budget+1
        older,prev=prev,row
    return prev[-1]

def has_recovery_context(query: str) -> bool:
    return bool(re.search(r'กฎ|กฏ|กติกา|แข่ง|เวลานอก|รายชื่อทีม|ประท้วง|(?<![a-z0-9])(?:rules?|rulebook|competition|tournament|timeouts?|pause|roster|protest)(?![a-z0-9])',query,re.I))

@lru_cache(maxsize=2048)
def recover_names(query: str,registry: tuple[tuple[str,str],...],allow_same_target_overlap: bool = False) -> tuple[str,tuple[NameRecovery,...]]:
    if not has_recovery_context(query) or len(query)>800:return query,()
    compact,positions=_compact(query);candidates=[];protected=[]
    for protected_target,alias in registry:
        name,_=_compact(alias);offset=0
        while name and (start:=compact.find(name,offset))>=0:
            a=positions[start];b=positions[start+len(name)-1]+1
            latin=alias.isascii()
            if not latin or not ((a and re.match(r'[a-z0-9]',query[a-1],re.I)) or (b<len(query) and re.match(r'[a-z0-9]',query[b],re.I))):protected.append((a,b,protected_target,name))
            offset=start+len(name)
    for game_id,alias in registry:
        name,_=_compact(alias)
        if len(name)<6:continue  # Never fuzzy-map CS2/RoV/T8/valo.
        thai=bool(re.search(r'[\u0e00-\u0e7f]',name));budget=2 if len(name)>=10 else 1
        digits=re.findall(r'\d+',name);freq=Counter(name)
        for start in range(len(compact)):
            original_start=positions[start]
            if allow_same_target_overlap and compact.startswith(name,start):continue
            if not thai and original_start and re.match(r'[a-z0-9]',query[original_start-1],re.I):continue
            for size in range(max(6,len(name)-budget),len(name)+budget+1):
                end=start+size
                if end>len(compact):continue
                original_end=positions[end-1]+1;span=query[original_start:original_end];value=compact[start:end]
                if any(original_start<b and a<original_end and (not allow_same_target_overlap or protected_target!=game_id or protected_name==name) for a,b,protected_target,protected_name in protected):continue
                if len(span)>len(alias)+2*budget+5:continue
                if not thai and original_end<len(query) and re.match(r'[a-z0-9]',query[original_end],re.I):continue
                if thai and re.search(r'[a-z]',value):continue
                if re.findall(r'\d+',value)!=digits:continue
                # An explicit different edition is evidence, not a typo.
                if re.search(r'^\s*(?:ภาค|เวอร์ชัน|version|v)\s*(?:\d+|[ivx]+\b)',query[original_end:],re.I):continue
                if digits and original_end<len(query) and query[original_end].isdigit():continue
                if sum((freq & Counter(value)).values())<max(len(name),len(value))-budget:continue
                # Facet prefixes may overlap only to repair a longer phrase.
                # Never consume a following word after an already exact alias.
                if allow_same_target_overlap and name in value:continue
                distance=_osa(value,name,budget)
                if distance==0:continue
                if distance<=budget and distance/len(name)<=.18:
                    candidates.append(NameRecovery(game_id,original_start,original_end,span,alias,distance,distance/len(name),alias))
    selected=[]
    for candidate in sorted(candidates,key=lambda c:(c.edit_fraction,c.edits,-(c.end-c.start),c.start)):
        if any(candidate.start<c.end and c.start<candidate.end for c in selected):continue
        rivals=[c for c in candidates if c.game_id!=candidate.game_id and candidate.start<c.end and c.start<candidate.end]
        if rivals and min(c.edit_fraction for c in rivals)-candidate.edit_fraction<.08:continue
        selected.append(candidate)
    result=query
    for c in sorted(selected,key=lambda c:c.start,reverse=True):result=result[:c.start]+c.canonical+result[c.end:]
    return result,tuple(sorted(selected,key=lambda c:c.start))
