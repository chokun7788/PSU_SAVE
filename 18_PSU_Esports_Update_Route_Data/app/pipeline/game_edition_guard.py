"""Protect explicit numbered editions using aliases of the recorded catalog.

Only numbers immediately attached to a known game stem are checked. Durations,
event years, station numbers and the rest of the user's sentence are untouched.
"""
from functools import lru_cache
import re
from app.core.normalization import normalize_text
from app.pipeline.entity_resolver import _game_resolver_index

def _roman_number(token):
    token = token.upper()
    if not token or not re.fullmatch(r'M{0,3}(?:CM|CD|D?C{0,3})(?:XC|XL|L?X{0,3})(?:IX|IV|V?I{0,3})', token):
        return None
    values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total = 0
    for i, char in enumerate(token):
        value = values[char]
        total += -value if i+1<len(token) and value<values[token[i+1]] else value
    return str(total)

@lru_cache(maxsize=2)
def _numbered_stems(catalog_version):
    groups={}
    for row in _game_resolver_index().rows_by_id.values():
        for alias in [row['title'],*row.get('aliases',())]:
            text=normalize_text(alias)
            match=re.match(r'^([^\d]+?)(\d+)(?:\D.*)?$',text)
            if not match:
                roman = re.fullmatch(r'(.+?)\s+([ivxlcdm]+)', text)
                number = _roman_number(roman[2]) if roman else None
                if not number:
                    continue
                stem, edition = roman[1].rstrip(), number
            else:
                stem, edition = match[1].rstrip(), match[2]
            if len(re.sub(r'\W','',stem))<2:
                continue
            groups.setdefault(stem,set()).add(edition)
    return tuple((stem,frozenset(versions)) for stem,versions in sorted(groups.items(),key=lambda p:len(p[0]),reverse=True))

def unsupported_numbered_game(query):
    if not re.search(r'\d|\b[ivxlcdm]+\b', query, re.I):
        return None
    q=normalize_text(query)
    index=_game_resolver_index()
    confirmed_spans=[]
    for stem,versions in _numbered_stems(index.catalog_version):
        pattern=r'(?<![a-z0-9])'+re.escape(stem).replace(r'\ ',r'\s+')+r'\s*(\d+|[ivxlcdm]+)(?![a-z0-9])'
        for match in re.finditer(pattern,q):
            if any(start <= match.start() and match.end() <= end for start,end in confirmed_spans):
                continue
            version = match[1] if match[1].isdigit() else _roman_number(match[1])
            if version is None:
                continue
            # "Tekken I want to play" contains the English pronoun, not an edition.
            if match[1] == 'i' and re.match(r'\s+(?:want|need|would|can|have|am|like)\b', q[match.end():]):
                continue
            if version not in versions:
                return {'requested_title':match[0].strip(),'requested_version':match[1],
                        'normalized_version':version,'known_stem':stem,'recorded_versions':sorted(versions),'catalog_version':index.catalog_version}
            confirmed_spans.append(match.span())
    return None
