"""Bounded keyboard-aware candidates for owner names, with numeric protection."""
import re,unicodedata
from .query_contract import normalize
from app.core.intent_cue_recovery import _VALID_ENGLISH_WORDS
ROWS=[('qwertyuiop',0),('asdfghjkl',.25),('zxcvbnm',.75),('ๆไำพะัีรนยบล',0),('ฟหกดเ้่าสวง',.25),('ผปแอิืทมใฝ',.75)]
POSITIONS={ch:(i+offset,row//3,row%3) for row,(letters,offset) in enumerate(ROWS) for i,ch in enumerate(letters)}
def clusters(text):
 out=[]
 for ch in text:
  if out and unicodedata.category(ch).startswith('M'):out[-1]+=ch
  else:out.append(ch)
 return out
def adjacent(a,b):
 p,q=POSITIONS.get(a),POSITIONS.get(b)
 return bool(p and q and p[1]==q[1] and abs(p[0]-q[0])<=1.3 and abs(p[2]-q[2])<=1)
def distance(a,b):
 a,b=clusters(a),clusters(b);dp=[[0.]*(len(b)+1) for _ in range(len(a)+1)]
 for i in range(len(a)+1):dp[i][0]=i
 for j in range(len(b)+1):dp[0][j]=j
 for i in range(1,len(a)+1):
  for j in range(1,len(b)+1):
   cost=0 if a[i-1]==b[j-1] else .65 if adjacent(a[i-1],b[j-1]) else 1
   dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+cost)
   if i>1 and j>1 and a[i-1]==b[j-2] and a[i-2]==b[j-1]:dp[i][j]=min(dp[i][j],dp[i-2][j-2]+1)
 return dp[-1][-1]
def candidates(question,names,max_work=18000):
 q=normalize(question);scores={};work=0
 for rid,aliases in names.items():
  for alias in aliases:
   a=normalize(alias)
   if not 5<=len(a)<=100:continue
   for size in (len(a)-2,len(a)-1,len(a),len(a)+1,len(a)+2):
    if size<=0:continue
    for start in range(max(0,len(q)-size+1)):
     work+=1
     if work>max_work:return [] # Never claim uniqueness after a truncated search.
     span=q[start:start+size]
     if re.findall(r'\d+',span)!=re.findall(r'\d+',a):continue
     if re.search('[a-z0-9]',a):
      if start and q[start-1].isalnum() and q[start-1].isascii():continue
      if start+size<len(q) and q[start+size].isalnum() and q[start+size].isascii():continue
     if re.fullmatch('[a-z]+',span) and span in _VALID_ENGLISH_WORDS and span!=a:continue
     words=re.findall('[a-z]+',span)
     if words and re.fullmatch(r'[a-z\s]+',span) and all(w in _VALID_ENGLISH_WORDS for w in words) and span!=a:continue
     if span and a and span[0] not in a[:3] and not adjacent(span[0],a[0]):continue
     if not span or abs(len(clusters(span))-len(clusters(a)))>2:continue
     # A cheap edit bound avoids a dynamic-programming pass for unrelated spans.
     if len(set(span)&set(a))<max(2,len(set(a))-3):continue
     d=distance(span,a);score=1-d/max(len(clusters(a)),1)
     if d<=2 and score>=.82 and (rid not in scores or score>scores[rid]['score']):scores[rid]={'record_id':rid,'alias':alias,'observed':span,'start':start,'end':start+size,'score':score,'edit_cost':d}
 return sorted(scores.values(),key=lambda x:-x['score'])[:3]
def recover(question,names):
 proposed=candidates(question,names)
 if not proposed:return None
 best=proposed[0]
 if len(proposed)>1 and best['score']-proposed[1]['score']<.08:return {'ambiguous':proposed}
 q=normalize(question)
 return {'record_ids':[best['record_id']],'corrected':q[:best['start']]+normalize(best['alias'])+q[best['end']:],'edits':[best],'method':'keyboard_context_candidate'}
