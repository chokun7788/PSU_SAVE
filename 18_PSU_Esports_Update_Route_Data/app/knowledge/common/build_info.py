"""Fingerprint captured at module import; excludes databases, logs and tokens."""
from pathlib import Path
import hashlib
def _capture():
 root=Path(__file__).resolve().parents[3];digest=hashlib.sha256()
 files=[]
 for folder in ('app','web_chat'):
  files.extend(p for p in (root/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix in {'.py','.json','.js','.html','.css'})
 files.extend(root.glob('*.ps1'))
 for p in sorted(files):
  digest.update(p.relative_to(root).as_posix().encode());digest.update(p.read_bytes())
 return {'build_id':'common-r62','loaded_source_sha256':digest.hexdigest(),'fingerprint_scope':'application, web UI and launchers at module import'}
LOADED_BUILD=_capture()
