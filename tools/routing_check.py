#!/usr/bin/env python3
"""Release check: the Director's hierarchy, the routing rules and the folder agree.

usage: python3 tools/routing_check.py [--root .]

Fails (exit 1) when:
  - a specialist folder exists that the Director's hierarchy does not list;
  - the hierarchy lists a specialist that does not exist;
  - a listed specialist has no routing rule saying when to use it;
  - a specialist is referenced by another skill but is not in the manifest;
  - two skills claim the same responsibility with no stated reason for the overlap.
Nothing is changed.
"""
import argparse, json, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
SKIP_DIRS = {'.git', 'local', '__pycache__'}
DIRECTOR = 'music-director/SKILL.md'

# Responsibilities that must have exactly one owner. Each maps to the folder that owns it and the
# phrases that mean a skill is claiming it.
SOLE_OWNERSHIP = {
    'performance planning': ('performance-director',
                             [r'\bowns?\b[^.]*\bmicrotiming\b', r'\bwe decide\b[^.]*articulation']),
    'vocal architecture': ('vocal-director',
                           [r'\bowns?\b[^.]*\bvocal (?:architecture|hierarchy)\b']),
    'project state': ('project-guide', [r'\bowns?\b[^.]*\bproject (?:state|thesis)\b']),
    'candidate generation': ('creative-lab', [r'\bowns?\b[^.]*\bexploration candidates?\b']),
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=ROOT)
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    problems = []

    on_disk = sorted(
        d for d in os.listdir(root)
        if os.path.isdir(os.path.join(root, d)) and d not in SKIP_DIRS
        and os.path.exists(os.path.join(root, d, 'SKILL.md')))
    specialists = [d for d in on_disk if d != 'music-director']

    dpath = os.path.join(root, DIRECTOR)
    if not os.path.exists(dpath):
        print(f'{DIRECTOR}: missing')
        sys.exit(2)
    dtext = open(dpath, encoding='utf-8').read()

    # the hierarchy block
    hm = re.search(r'```text\s*\nMusic Director\n(.*?)```', dtext, re.S)
    if not hm:
        problems.append(f'{DIRECTOR}: no hierarchy block found')
        listed = []
    else:
        listed = []
        for line in hm.group(1).split('\n'):
            m = re.match(r'^[├└]──\s+([A-Za-z][A-Za-z ]+?)(?:\s{2,}|$)', line.strip())
            if m:
                listed.append(m.group(1).strip().lower().replace(' ', '-'))

    for s in specialists:
        if s not in listed:
            problems.append(
                f'{DIRECTOR}: specialist folder {s}/ is not in the hierarchy')
    for s in listed:
        if s not in specialists:
            problems.append(
                f'{DIRECTOR}: hierarchy lists "{s}" but there is no {s}/SKILL.md')

    # a routing rule per specialist
    for s in specialists:
        pretty = s.replace('-', ' ')
        pat = re.compile(rf'###\s*Use\s+{pretty}\b', re.I)
        alt = re.compile(rf'\|\s*{pretty}\s*\|', re.I)
        if not (pat.search(dtext) or alt.search(dtext)):
            problems.append(f'{DIRECTOR}: no routing rule for {s}')

    # README's routing table names every specialist, and names nothing that is not one
    rpath = os.path.join(root, 'README.md')
    if os.path.exists(rpath):
        rtext = open(rpath, encoding='utf-8').read()
        sec = re.search(r'^## Routing\n(.*?)(?=^## )', rtext, re.S | re.M)
        if not sec:
            problems.append('README.md: no "## Routing" section')
        else:
            routes = set()
            for line in sec.group(1).split('\n'):
                cells = [c.strip() for c in line.strip().strip('|').split('|')]
                if len(cells) >= 2 and not set(cells[-1]) <= set('-: '):
                    routes.add(cells[-1])
            routes.discard('Route')
            names = {s: s.replace('-', ' ').lower() for s in specialists}
            for s, name in names.items():
                if not any(r.lower() == name for r in routes):
                    problems.append(f'README.md: the routing table has no row for {s}')
            for r in routes:
                if r.lower() not in names.values() and not r.startswith('Music Director'):
                    problems.append(f'README.md: the routing table routes to "{r}", which is not a '
                                    f'specialist')

    # manifest coverage of anything a skill points at
    mpath = os.path.join(root, 'manifest.json')
    if os.path.exists(mpath):
        m = json.load(open(mpath, encoding='utf-8'))
        listed_paths = set()
        for v in m.values():
            if isinstance(v, list):
                listed_paths.update(x for x in v if isinstance(x, str))
            elif isinstance(v, str):
                listed_paths.add(v)
        for s in specialists + ['music-director']:
            if f'{s}/SKILL.md' not in listed_paths:
                problems.append(f'manifest.json: {s}/SKILL.md is not listed')

    # Sole ownership. A sentence that names the owner is deferring to it, not claiming it, which is
    # exactly what a well-behaved skill does, so those sentences are not findings.
    for label, (owner, patterns) in SOLE_OWNERSHIP.items():
        owner_name = owner.replace('-', ' ')
        claimants = []
        for s in on_disk:
            text = open(os.path.join(root, s, 'SKILL.md'), encoding='utf-8').read()
            for p in patterns:
                hit = False
                for m in re.finditer(p, text, re.I):
                    start = text.rfind('.', 0, m.start()) + 1
                    end = text.find('.', m.end())
                    sentence = text[start:end if end != -1 else len(text)]
                    if not re.search(owner_name, sentence, re.I):
                        hit = True
                        break
                if hit:
                    claimants.append(s)
                    break
        extra = [c for c in claimants if c != owner]
        for c in extra:
            snippet = open(os.path.join(root, c, 'SKILL.md'), encoding='utf-8').read()
            if not re.search(r'overlap_reason|shared with|jointly owned', snippet, re.I):
                problems.append(
                    f'{c}/SKILL.md claims "{label}", which {owner} owns, with no stated reason')

    for p in problems:
        print(p)
    print(f'{len(problems)} finding(s) across {len(specialists)} specialist(s)')
    sys.exit(1 if problems else 0)


if __name__ == '__main__':
    main()
