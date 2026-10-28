"""Metadata-based English typo candidates; never edits names or facts.

Runs only on the name-stripped query for a semantic review. Each edit must have
one unique one-edit candidate in the schema lexicon. Negation/short words stay raw.
"""
import re,json
from pathlib import Path
from functools import lru_cache
from app.core.typo_similarity import osa_distance
from app.core.intent_cue_recovery import _VALID_ENGLISH_WORDS
from .registry import CATALOG
from .query_contract import CUES,scope_kinds

PROTECTED={'not','never','no','now','pay','play','book','look','score','scores','more','core','free','price','cost','host','post','cast','coat','last','list','close','closed','first','floor','for','four','our','hour','hours','where','there','here','form','from','role','rule','rules','name','names'}|_VALID_ENGLISH_WORDS
GRAMMAR={'what','which','where','when','why','whose','would','should','could','does','have','with','from','this','that','then','please','beginner','complete','actual','compare','present','verify','proof','qualify','smallest','largest','entire','information','installed','version','return','read','write','their','there','receive','response','reply','device','blocked','reserved'}
@lru_cache(maxsize=128)
def lexicon(kinds):
    descriptions=json.loads(Path(__file__).with_name('schema_descriptions.json').read_text(encoding='utf-8'))['fields']
    words=set(GRAMMAR)|PROTECTED
    for kind in scope_kinds(kinds):
        for f in CATALOG[kind]['fields']:
            words.update(re.findall('[a-z]{4,}',descriptions.get(f['key'],{}).get('description_en','').lower()))
            for cue in CUES.get(f['key'],[]):words.update(re.findall('[a-z]{4,}',cue.lower()))
    return frozenset(words)
def recover_schema_language(question,kinds):
    if not kinds:return question,[]
    words=lexicon(tuple(sorted(kinds)));edits=[]
    def replace(m):
        token=m.group().casefold()
        if token in words or len(token)<4 or len(edits)>=4:return m.group()
        candidates=[w for w in words if len(w)>=4 and abs(len(w)-len(token))<=1 and osa_distance(token,w)==1]
        # Apply the permitted error channel before the uniqueness test. An
        # unsafe same-length substitute must not mask a unique duplicate/deletion.
        def safe_channel(target):
            if len(target)!=len(token):return True
            different=[i for i,(a,b) in enumerate(zip(token,target)) if a!=b]
            return len(different)==2 and different[1]==different[0]+1 and token[different[0]]==target[different[1]] and token[different[1]]==target[different[0]]
        candidates=[w for w in candidates if safe_channel(w)]
        # A substitute/transposition is riskier than a missing/repeated letter.
        # Never infer a different valid word or remove a negation.
        if len(candidates)!=1:return m.group()
        target=candidates[0]
        if len(target)==len(token):
            # A single adjacent transposition is a concrete channel; arbitrary
            # substitutions remain suggestions requiring a separate review.
            different=[i for i,(a,b) in enumerate(zip(token,target)) if a!=b]
            if len(different)!=2 or different[1]!=different[0]+1 or token[different[0]]!=target[different[1]] or token[different[1]]!=target[different[0]]:return m.group()
        if target in {'not','never','now','none'}:return m.group()
        edits.append({'observed':m.group(),'intended':target,'start':m.start(),'distance':1,'source':'schema_description_lexicon'})
        return target
    recovered=re.sub(r'[A-Za-z]+',replace,question)
    return recovered,edits
