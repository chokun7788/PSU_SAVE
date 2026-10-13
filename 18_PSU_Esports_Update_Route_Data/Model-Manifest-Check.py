"""Check tested model identities and complete blob sizes before accepting traffic."""
import json,sys
from pathlib import Path
root=Path(__file__).resolve().parent
expected=json.loads((root/'models/expected_manifests.json').read_text(encoding='utf-8-sig'))
store=root/'models/ollama'
for name,wanted in expected.items():
 path=store/'manifests'/name
 if not path.is_file():raise SystemExit('Missing model manifest: '+name)
 actual=json.loads(path.read_text(encoding='utf-8'))
 signature={'config':actual['config']['digest'],'layers':[{'digest':x['digest'],'size':x['size']} for x in actual['layers']]}
 if signature!=wanted:raise SystemExit('Model revision differs from the tested package: '+name+'. Use the matching release or have the new revision verified before deployment.')
 for item in [actual['config'],*actual['layers']]:
  blob=store/'blobs'/item['digest'].replace(':','-')
  if not blob.is_file() or blob.stat().st_size!=item['size']:raise SystemExit('Incomplete model blob: '+item['digest'])
print('Tested model identities and blob sizes verified.')
