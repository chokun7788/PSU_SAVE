"""Typed catalog discovery; numeric selectors are not room seating or live stock."""
import re
from .registry import value
from .query_contract import normalize,live_request
def discover_games(question,records):
    q=normalize(question)
    if live_request(q) or not re.search(r'เกม|\bgames?\b',q):return None
    count=re.search(r'(\d+)\s*(?:คน|players?|people)|(?:four|สี่)\s*(?:คน|players?|people)',q)
    if not count:return None
    people=int(count.group(1)) if count.group(1) else 4
    if not 1<=people<=100:return None
    # Do not reinterpret installation, prices or tournament rules as discovery.
    if re.search(r'ติดตั้ง|ลงเกม|แข่ง|ราคา|บาท|\b(?:install|price|cost|tournament|rules)\b',q):return None
    platform=next((p for p in ('Nintendo Switch','PS5','PC','VR','Cockpit') if re.search(r'(?<![a-z0-9])'+re.escape(p.lower())+r'(?![a-z0-9])',q)),None)
    modes=[]
    for r in records.values():
        if r['kind']!='game_mode':continue
        lo,hi=value(r,'players_min'),value(r,'players_max')
        if type(lo) is int and type(hi) is int and lo<=people<=hi and value(r,'studio_supported') is True and (not platform or value(r,'platform')==platform):modes.append(r['record_id'])
    return {'record_ids':modes,'people':people,'platform':platform,'method':'typed_game_player_filter'}
