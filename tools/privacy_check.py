#!/usr/bin/env python3
"""Release check: no user-specific content in the skill files.

usage: python3 tools/privacy_check.py [--profile path/to/profile.yaml] [--root .]

Fails (exit 1) when a skill file contains:
  - an absolute home or user path (/Users/..., /home/..., C:\\Users\\...), or a ~/ path;
  - any term from the profile's privacy.private_terms list (names, titles, paths).
The profile itself, profiles/local/ and this tool are skipped. Nothing is changed.
"""
import argparse, os, re, sys

PATH_RE = re.compile(r"(/Users/[^\s`'\"]+|/home/[^\s`'\"]+|[A-Za-z]:\\\\Users\\\\[^\s`'\"]+|~/[^\s`'\"]+)")
SKIP_DIRS = {'.git', 'local'}
# generic locations that are the same on every machine of that OS
GENERIC = ('~/Library/Audio/Plug-Ins', '~/Music/Ableton/User Library', 'C:\\Users\\<')
SKIP_FILES = {'privacy_check.py', 'user-profile.example.yaml'}

def private_terms(profile):
    """Read privacy.private_terms from a simple YAML profile without needing a YAML library."""
    terms, inside = [], False
    for line in open(profile, encoding='utf-8'):
        if re.match(r'^\s*private_terms:\s*\[(.*)\]\s*$', line):
            return [t.strip().strip('"\'') for t in re.match(r'^\s*private_terms:\s*\[(.*)\]', line).group(1).split(',') if t.strip()]
        if re.match(r'^\s*private_terms:\s*$', line):
            inside = True; continue
        if inside:
            m = re.match(r'^\s*-\s*(.+?)\s*$', line)
            if m: terms.append(m.group(1).strip('"\''))
            elif line.strip() and not line.startswith(' ' * 4): break
    return terms

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--profile'); ap.add_argument('--root', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
    a = ap.parse_args()
    terms = private_terms(a.profile) if a.profile else []
    hits = []
    for dp, dn, fn in os.walk(a.root):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in fn:
            if f in SKIP_FILES or not f.endswith(('.md', '.json', '.yaml', '.yml', '.txt', '.py')):
                continue
            p = os.path.join(dp, f)
            for i, line in enumerate(open(p, encoding='utf-8', errors='replace'), 1):
                for m in PATH_RE.finditer(line):
                    if not m.group(0).startswith(GENERIC):
                        hits.append((p, i, 'path', m.group(0)))
                low = line.lower()
                for t in terms:
                    if t and t.lower() in low:
                        hits.append((p, i, 'private term', t))
    for p, i, kind, what in hits:
        print(f'{os.path.relpath(p, a.root)}:{i}: {kind}: {what}')
    print(f'{len(hits)} finding(s)' + ('' if a.profile else ' (no profile given: paths only)'))
    sys.exit(1 if hits else 0)

if __name__ == '__main__':
    main()
