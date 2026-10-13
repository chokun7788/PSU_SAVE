"""Bridge published common ownership into legacy retrieval without guessed IDs."""
import os,sqlite3
from pathlib import Path
from .store import CommonStore
from .authority import filter_legacy_hits,scoped_names
def snapshot():
    path=Path(os.getenv('PSU_KNOWLEDGE_DB') or Path(__file__).resolve().parents[3]/'data/knowledge/approved.sqlite')
    if not path.is_file():return None
    try:
        store=CommonStore(path)
        with store.connect() as c:
            if not c.execute("SELECT 1 FROM sqlite_master WHERE name='cc_meta'").fetchone():return None
        s=store.snapshot()
        if s['allow_demo'] and os.getenv('PSU_COMMON_ALLOW_DEMO')!='1':return None
        return s if s.get('release') else None
    except (sqlite3.Error,ValueError,OSError):return None
def guard_hits(hits):
    s=snapshot()
    if not s:return hits,0
    kept,blocked=filter_legacy_hits(s,hits)
    return kept,len(blocked)
def legacy_game_titles(common_snapshot,*,locale='th'):
    """Only titles from the existing published curated store; no new facts."""
    if common_snapshot.get('allow_demo'):return [] # Keep synthetic catalogs isolated.
    from app.runtime.fast_answer import _verified_game_catalog
    game_ids={rid for rid,r in common_snapshot['release']['records'].items() if r['kind']=='game'}
    game_ids.update(rid for rid,kind in common_snapshot.get('historical_kinds',{}).items() if kind=='game')
    name_map=scoped_names(common_snapshot)
    blocked_names={name.casefold() for rid,aliases in name_map.items() if rid in game_ids for name in aliases}
    blocked_names.update(name.casefold() for rid,aliases in common_snapshot.get('historical_names',{}).items() if rid in game_ids for name in aliases)
    titles=[]
    for row in _verified_game_catalog():
        name=str(row.get('name') or '').strip()
        if not name or name.casefold() in blocked_names:continue
        if any(alias.casefold() in blocked_names for alias in row.get('aliases',[])):continue
        if name not in titles:titles.append(name)
    return sorted(titles)
