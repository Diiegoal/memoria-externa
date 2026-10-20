#!/usr/bin/env python3
"""Build a limited local context handoff packet with explicit omissions. No network."""
from __future__ import annotations
import argparse, hashlib, sys
from pathlib import Path
try:
    import yaml
except ImportError:
    print('ERROR: install PyYAML using python -m pip install pyyaml',file=sys.stderr)
    sys.exit(2)
ROOT=Path(__file__).resolve().parent.parent

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--project',required=True)
    ap.add_argument('--budget-chars',type=int,default=30000)
    ap.add_argument('--output',required=True,help='Destination OUTSIDE the repository; no automatic chat upload.')
    args=ap.parse_args()
    if args.budget_chars<400:ap.error('--budget-chars must be at least 400')
    manifest=yaml.safe_load((ROOT/'MEMORY_MANIFEST.yaml').read_text(encoding='utf8'))
    project=next((p for p in manifest['projects'] if p['id']==args.project),None)
    if project is None:ap.error('unknown project; inspect indexes/projects.md')
    output=Path(args.output).expanduser().resolve()
    if output.is_relative_to(ROOT):ap.error('--output must be outside the repository to avoid leaking private context into tracked files')
    paths=['START_HERE.md','governance/memory-policy.md','governance/citation-policy.md',project['path']+'/README.md',project['state'],project['handoff']]
    paths+=project['decisions']+[project['path']+'/constraints.md',project['path']+'/questions.md']+project['tasks']+project['sessions']
    included=[];excluded=[];blocks=[];used=0
    for rel in paths:
        file=(ROOT/rel).resolve()
        if not file.is_relative_to(ROOT) or not file.is_file():
            excluded.append((rel,'file is unavailable'))
            continue
        value=file.read_text(encoding='utf8')
        segment='\n\n---\n\n## SOURCE '+rel+' — SHA256 '+hashlib.sha256(file.read_bytes()).hexdigest()+'\n\n'+value
        if used+len(segment)>args.budget_chars:
            excluded.append((rel,f'character budget exceeded: needs {len(segment)} characters; never truncate sources'))
            continue
        included.append(rel);blocks.append(segment);used+=len(segment)
    header='# Local Continuity Packet — NOT the Complete Original Documents\n\n'
    header+=f'- Project: {project["id"]}\n- Approximate limit: {args.budget_chars} characters (not tokens).\n'
    header+='- Only locally opened files were included; external documents were not fetched.\n'
    header+='- Full Spanish originals are excluded by default: open raw files for exact wording.\n'
    header+='- A personally adopted decision is not an independent certification of external facts.\n\n'
    header+='## Included files\n'+(''.join('- '+x+'\n' for x in included) or '- none\n')
    header+='\n## Excluded files\n'+(''.join('- '+x+': '+reason+'\n' for x,reason in excluded) or '- none\n')
    header+='\n## Available original files NOT included\n'+''.join('- '+x+'\n' for x in project['raw_messages'])
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(header+''.join(blocks),encoding='utf8')
    print(f'WROTE: {output}, {len(included)} included, {len(excluded)} excluded; manual sharing required.')
    return 0
if __name__=='__main__':sys.exit(main())
