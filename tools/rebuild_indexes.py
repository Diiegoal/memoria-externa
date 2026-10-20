#!/usr/bin/env python3
"""Rebuild four derived English indexes locally. PyYAML; no network or Git writes."""
from __future__ import annotations
import argparse, hashlib, json, os, re, sys, tempfile
from pathlib import Path
try:
    import yaml
except ImportError:
    print('ERROR: install PyYAML with python -m pip install pyyaml',file=sys.stderr)
    sys.exit(2)
ROOT=Path(__file__).resolve().parent.parent

def rel(path):return path.relative_to(ROOT).as_posix()
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def parse(path):
    content=path.read_text(encoding='utf-8')
    match=re.match(r'\A---\n(.*?)\n---\n',content,re.S)
    if not match:raise ValueError('Missing YAML front matter: '+rel(path))
    data=yaml.safe_load(match.group(1))
    if not isinstance(data,dict):raise ValueError('Invalid YAML front matter: '+rel(path))
    return data,content[match.end():]
def jsonlines(rows):
    return ''.join(json.dumps(item,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n' for item in rows)

def indices():
    manifest=yaml.safe_load((ROOT/'MEMORY_MANIFEST.yaml').read_text(encoding='utf-8'))
    projects=[];sessions=[];search=[];topics=[]
    for project in sorted(manifest['projects'],key=lambda p:p['id']):
        pid=project['id'];base=ROOT/project['path']
        session_files=sorted((base/'sessions').glob('S-*.md'))
        latest=None
        for file in session_files:
            front,_=parse(file);latest=front['id']
            sessions.append({'session_id':front['id'],'project_id':pid,'chat_id':front['chat_id'],'path':rel(file),'status':front['status'],'started_at':front.get('started_at'),'ended_at':front.get('ended_at'),'topics':['Agent SDLC','Claude Code','professional module order'],'sha256':sha(file)})
        projects.append((pid,project['path'],latest or 'NOT_RECORDED'))
        for file in sorted((base/'knowledge').glob('*.md')):
            topics.append((pid,rel(file),latest or 'NOT_RECORDED'))
        authored=[base/'README.md',base/'current-state.md',base/'handoff.md',base/'timeline.md',base/'constraints.md',base/'questions.md',base/'evidence/sources.md']
        authored+=sorted((base/'decisions').glob('*.md'))+sorted((base/'knowledge').glob('*.md'))+session_files
        for file in authored:
            if not file.is_file():continue
            lines=file.read_text(encoding='utf8').splitlines()
            headings=[(i+1,line.lstrip('# ').strip()) for i,line in enumerate(lines) if re.match(r'^#{1,3} ',line)]
            category=('decision' if '/decisions/' in rel(file) else 'session' if '/sessions/' in rel(file) else 'knowledge' if '/knowledge/' in rel(file) else 'project')
            terms=[]
            for term in re.findall(r'[\w-]{3,}',' '.join(h for _,h in headings).lower()):
                if term not in terms:terms.append(term)
            search.append({'document_id':f'DOC-{len(search)+1:04d}','path':rel(file),'section':headings[0][1] if headings else file.stem,'line_start':headings[0][0] if headings else 1,'headings':[{'line':i,'text':h} for i,h in headings[:50]],'terms':terms[:120],'category':category,'source_sha256':sha(file),'generation':'derived-local-v1'})
    ptext='# Project Index\n\n## Control\n- **Regeneration:** deterministic from manifest and sessions; historical generation time NOT_RECORDED.\n- **Own Git commit:** NOT_RECORDED; this index is not an independent source of truth.\n\n## Catalog\n| ID (organizational convention) | Path | State | Documentary session | Access |\n|---|---|---|---|---|\n'
    for pid,path,latest in projects:
        ptext+=f'| `{pid}` | [{path}](../{path}/README.md) | personally adopted order; application not built | `{latest}` | restricted access recommended |\n'
    ptext+='\n## Caveats\nThis index does not prove a GitHub fetch or historical chat closure; check originals.\n'
    ttext='# Topic Index\n\n## Control\n- **Method:** lexical indexing of existing notes, fully rebuildable.\n- **Research cut-off:** 2026-10-19; **personal adoption:** 2026-10-20; technical regeneration on demand, without invented event times.\n\n## Topics\n| Topic | Project | Note | Session | Evidence |\n|---|---|---|---|---|\n'
    for pid,path,latest in topics:
        ttext+=f'| Architecture / Agent SDLC | `{pid}` | [{Path(path).name}](../{path}) | `{latest}` | [Sources](../projects/{pid}/evidence/sources.md) |\n'
    ttext+='\n## Indexing scope\nTerms: Agent SDLC, Claude Code, SDD, full-stack, architecture, privacy, evaluation. No embeddings or external services; use `--check` to detect staleness.\n'
    return {'indexes/projects.md':ptext,'indexes/topics.md':ttext,'indexes/sessions.jsonl':jsonlines(sorted(sessions,key=lambda x:x['session_id'])),'indexes/search-catalog.jsonl':jsonlines(sorted(search,key=lambda x:x['path']))}

def run(check):
    derived=indices();stale=[];changed=[]
    for name,content in derived.items():
        file=ROOT/name;existing=file.read_text(encoding='utf8') if file.is_file() else None
        if existing!=content:
            if check:stale.append(name)
            else:
                file.parent.mkdir(parents=True,exist_ok=True)
                fd,temp=tempfile.mkstemp(prefix='.index_',dir=file.parent,text=True)
                try:
                    with os.fdopen(fd,'w',encoding='utf8',newline='\n') as output:output.write(content)
                    os.replace(temp,file)
                finally:
                    if os.path.exists(temp):os.unlink(temp)
                changed.append(name)
    if check and stale:
        print('FAIL: stale or missing derived indexes:',', '.join(stale),file=sys.stderr)
        return 1
    print('PASS: four derived indexes match sources' if check else 'Indexes rebuilt; changed: '+(', '.join(changed) if changed else 'none'))
    return 0
if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true',help='check whether index regeneration would change anything')
    args=parser.parse_args()
    sys.exit(run(args.check))
