#!/usr/bin/env python3
"""Offline, rebuildable heading-level search index for local Markdown research."""
import argparse,json,pathlib,re,sys
def build(root):
    rows=[]
    for path in sorted(root.rglob('*.md')):
        if '.git' in path.parts:continue
        text=path.read_text(encoding='utf-8',errors='replace');title=path.stem;body=[]
        for line in text.splitlines():
            if line.startswith('# '):
                if body:rows.append({'path':str(path.relative_to(root)),'heading':title,'preview':' '.join(body)[:350]})
                title=line.lstrip('# ').strip();body=[]
            elif line.startswith('## '):
                if body:rows.append({'path':str(path.relative_to(root)),'heading':title,'preview':' '.join(body)[:350]})
                title=line.lstrip('# ').strip();body=[]
            elif line.strip() and not line.startswith('```'):body.append(line.strip())
        if body:rows.append({'path':str(path.relative_to(root)),'heading':title,'preview':' '.join(body)[:350]})
    return rows
def search(rows,q):
    terms=set(re.findall(r'[a-z0-9]+',q.lower()))
    if not terms:return []
    def score(r):
        head=r['heading'].lower();alltext=(head+' '+r['preview']).lower()
        return sum((3 if t in head else 1) for t in terms if t in alltext)
    return [dict(score=score(r),**r) for r in sorted(rows,key=lambda r:-score(r)) if score(r)>0][:15]
def main():
    p=argparse.ArgumentParser();s=p.add_subparsers(dest='action',required=True)
    b=s.add_parser('build');b.add_argument('--root',required=True);b.add_argument('--output',required=True)
    q=s.add_parser('search');q.add_argument('--index',required=True);q.add_argument('--query',required=True)
    a=p.parse_args()
    if a.action=='build':
        root=pathlib.Path(a.root).resolve();out=pathlib.Path(a.output).resolve()
        if not root.is_dir():p.error('root is not a directory')
        if out.is_relative_to(root):p.error('output must be outside indexed root')
        rows=build(root);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps({'root':str(root),'entries':rows},indent=2));print(len(rows),'entries')
    else:
        data=json.loads(pathlib.Path(a.index).read_text());print(json.dumps(search(data['entries'],a.query),indent=2))
if __name__=='__main__':main()
