#!/usr/bin/env python3
"""Validate the local memory tree, not truth of documentary statements."""
from __future__ import annotations
import collections, hashlib,json,re,sys
from datetime import datetime
from pathlib import Path
try:
    import yaml,jsonschema
except ImportError:
    print('ERROR: install dependencies: python -m pip install pyyaml jsonschema',file=sys.stderr);sys.exit(2)
ROOT=Path(__file__).resolve().parent.parent
issues=[];warn=[];counts=collections.Counter()
def bad(msg):issues.append(msg)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rootpath(path):
    p=(ROOT/path).resolve()
    if not p.is_relative_to(ROOT):raise ValueError('Path escapes repo: '+str(path))
    return p
def obj_file(path):
    t=path.read_text(encoding='utf8')
    m=re.match(r'\A---\n(.*?)\n---\n',t,re.S)
    if not m:raise ValueError('No front matter: '+str(path))
    return yaml.safe_load(m.group(1))
def check_link(path,href):
    h=href.split('#',1)[0].split('?',1)[0]
    if not h or re.match(r'^(https?://|mailto:|data:)',h):return
    from urllib.parse import unquote
    if h.startswith('/'):
        warn.append(f'Absolute link (not validated): {path} {h}');return
    dest=(path.parent/unquote(h)).resolve()
    if not dest.is_relative_to(ROOT) or not dest.exists():bad(f'Broken relative link: {path.relative_to(ROOT)} -> {h}')
def main():
    must=['README.md','START_HERE.md','MEMORY_MANIFEST.yaml','CHANGELOG.md','.gitignore','.gitattributes','.github/CODEOWNERS','.github/pull_request_template.md','.github/workflows/validate-memory.yml','identity/communication-preferences.md','indexes/projects.md','indexes/topics.md','indexes/sessions.jsonl','indexes/search-catalog.jsonl','backups/README.md']
    for d in ['memory-policy','security-policy','retention-policy','citation-policy','naming-conventions','recovery-runbook']:must.append('governance/'+d+'.md')
    for d in ['session','event','decision','task']:must.append('schemas/'+d+'.schema.json')
    for d in ['session-open','session-close','conflict-resolution','maintenance']:must.append('procedures/'+d+'.md')
    for d in ['handoff','session','decision','task']:must.append('templates/'+d+'.template.md')
    for d in ['build_context','validate_memory','rebuild_indexes']:must.append('tools/'+d+'.py')
    for p in must:
        if not (ROOT/p).is_file():bad('Missing structural file: '+p)
    try:
        manifest=yaml.safe_load((ROOT/'MEMORY_MANIFEST.yaml').read_text(encoding='utf8'))
        assert isinstance(manifest,dict) and manifest['schema_version']=='1.0'
    except Exception as e:bad('Invalid manifest: '+str(e));return 1
    for p in must+manifest['policies']+list(manifest['schemas'].values())+list(manifest['indexes'].values())+manifest['events']:
        try:
            if not rootpath(p).is_file():bad('Invalid manifest reference: '+p)
        except Exception as e:bad(str(e))
    schemas={}
    for name,rel in manifest['schemas'].items():
        try:
            sch=json.loads((ROOT/rel).read_text(encoding='utf8'));jsonschema.Draft202012Validator.check_schema(sch);schemas[name]=sch;counts['schemas_valid']+=1
        except Exception as e:bad(f'Invalid {name} schema: {e}')
    def js_valid(name,data,p):
        if name not in schemas:return
        try:jsonschema.Draft202012Validator(schemas[name],format_checker=jsonschema.FormatChecker()).validate(data);counts[name+'_records']+=1
        except Exception as e:bad(f'Schema validation {p}: {e}')
    all_ids=set()
    projects=manifest.get('projects',[])
    if len(projects)!=1:bad('Expected exactly one project in this documentary package')
    for p in projects:
        base=p['path'];
        if p['id'] in all_ids:bad('Duplicate project ID')
        all_ids.add(p['id'])
        for rel in [p['state'],p['handoff']]+p['sessions']+p['decisions']+p['raw_messages']:
            if not rootpath(rel).is_file():bad('Missing project path: '+rel)
        for sf in p['sessions']:
            try:
                v=obj_file(rootpath(sf));js_valid('session',v,sf)
                if v['id']!=Path(sf).stem or v['id']!=p['latest_verified_session']:bad('Session ID mismatch')
                if v['project_id']!=p['id']:bad('Session project mismatch')
                for ref in v['raw_refs']:
                    if not rootpath(ref).exists():bad('Missing session raw: '+ref)
                for ref in v['decisions']:
                    if not (ROOT/base/'decisions'/f'{ref}.md').exists():bad('Decision reference missing: '+ref)
                all_ids.add(v['id'])
            except Exception as e:bad(f'Parse session {sf}: {e}')
        for df in p['decisions']:
            try:
                v=obj_file(rootpath(df));js_valid('decision',v,df)
                if v['id']!=Path(df).stem or v['project_id']!=p['id']:bad('Decision mismatch')
                if v['id'] in all_ids:bad('Duplicate ID '+v['id'])
                all_ids.add(v['id'])
                for source in v['source_refs']:
                    if not rootpath(source).is_file():bad('Missing decision source '+source)
            except Exception as e:bad(f'Parse decision {df}: {e}')
        tasks=list((ROOT/base/'tasks').glob('TASK-*.md'))
        if len(tasks)!=len(p['tasks']):bad('Task manifest disagrees with task files')
        for f in tasks:
            v=obj_file(f);js_valid('task',v,str(f));
            if v['id'] in all_ids:bad('Duplicate task ID')
            all_ids.add(v['id'])
    # raw integrity against sha256 lines + manifest records
    raw_manifest=rootpath(manifest['source_integrity']['manifest']);lines=raw_manifest.read_text(encoding='utf8').splitlines(); recorded={}
    for line in lines:
        m=re.fullmatch(r'([0-9a-f]{64})  ([^\n]+)',line)
        if not m:bad('Bad sha256sum manifest line: '+line);continue
        digest,rr=m.groups(); path=(raw_manifest.parent/rr).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file():bad('Missing raw checksum target: '+rr);continue
        if sha(path)!=digest:bad('SHA mismatch: '+str(path.relative_to(ROOT)))
        recorded[path.relative_to(ROOT).as_posix()]=digest;counts['raw_checks']+=1
    for x in manifest['source_integrity']['files']:
        if recorded.get(x['path'])!=x['sha256']:bad('Manifest raw SHA mismatch: '+x['path'])
    if set(recorded)!=set(p for x in projects for p in x['raw_messages']):bad('Raw SHA set != declared source set')
    # parse JSONL, date/ID and source references
    event_ids=set()
    for ep in manifest['events']:
        for i,line in enumerate(rootpath(ep).read_text(encoding='utf8').splitlines(),1):
            try:
                v=json.loads(line);js_valid('event',v,f'{ep}:{i}')
                if v['event_id'] in event_ids:bad('Duplicate event ID '+v['event_id'])
                event_ids.add(v['event_id']);
                if not rootpath(v['source_ref']).is_file():bad('Event source missing '+v['source_ref'])
                if v['project_id'] not in [p['id'] for p in projects]:bad('Event project mismatched')
            except Exception as e:bad(f'Bad event JSONL {ep}:{i}: {e}')
    for ip in ('indexes/sessions.jsonl','indexes/search-catalog.jsonl'):
        ids=set()
        for i,line in enumerate(rootpath(ip).read_text(encoding='utf8').splitlines(),1):
            try:
                v=json.loads(line)
                path=rootpath(v['path'])
                if not path.is_file():bad(f'Stale index path {ip}:{i}')
                id=v.get('document_id',v.get('session_id'))
                if id in ids:bad(f'Duplicate index ID {ip}:{id}')
                ids.add(id)
                if v.get('sha256',v.get('source_sha256')) != sha(path):bad(f'Stale index hash {ip}:{i}')
                counts['index_records']+=1
            except Exception as e:bad(f'Bad index JSONL {ip}:{i}: {e}')
    # verify Markdown links in authored docs only (not the raw originals, and not placeholders in templates)
    for file in ROOT.rglob('*.md'):
        rel=file.relative_to(ROOT).as_posix()
        if rel.startswith('raw/') or rel.startswith('templates/'):continue
        txt=file.read_text(encoding='utf8')
        # skip image links and inline fenced code where a fake URL might appear
        txt=re.sub(r'(?ms)^```.*?^```','',txt)
        for m in re.finditer(r'(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)',txt):check_link(file,m.group(1))
    # reject fixture extra instances
    if list((ROOT/'raw').rglob('chat-2')):bad('chat-2 unexpectedly instantiated')
    if len(list((ROOT/'projects').glob('*/sessions/S-*.md')))!=1:bad('More than one session instance')
    if len(list((ROOT/'projects').glob('*/decisions/DEC-*.md')))!=1:bad('More than one decision instance')
    if len(list((ROOT/'projects').glob('*/tasks/TASK-*.md')))!=0:bad('Unexpected task instances')
    # parse GitHub workflow YAML (PyYAML treats 'on' as boolean in 1.1; merely syntactic validation)
    for file in ['.github/workflows/validate-memory.yml','MEMORY_MANIFEST.yaml']:
        try: yaml.safe_load((ROOT/file).read_text(encoding='utf8'));counts['yaml_files']+=1
        except Exception as e:bad(f'Invalid YAML {file}: {e}')
    print('Counts: '+json.dumps(counts,sort_keys=True))
    if warn:
        for x in warn:print('WARN:',x)
    if issues:
        for x in issues:print('FAIL:',x,file=sys.stderr)
        print(f'FAIL: {len(issues)} technical issue(s). Not a semantic truth check.',file=sys.stderr)
        return 1
    print('PASS: manifest, files, raw SHA-256, JSON Schema, JSONL, IDs, links, indexes structurally valid.')
    print('LIMIT: no claim of a full historical chat export, third-party approval, comprehensive external URL verification, a remote CI run, secrets clearance, or production system testing. Documentary owner approval is self-declared for this personal edition.')
    return 0
if __name__=='__main__':sys.exit(main())
