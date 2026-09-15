#!/usr/bin/env python3
"""Release check: every path a page names can be found.

usage: python3 tools/link_check.py [--root .]

The pack links by naming a path in backticks, e.g. `shared/QUALITY_GATE.md`. A name is resolved
against, in order:

  1. the repository root;
  2. the folder of the page that names it;
  3. a unique basename anywhere in the pack, which is how a sentence that has already named a
     folder refers to its other files;
  4. an allowlist of files that live on the user's machine rather than in the pack.

Fails (exit 1) when a name resolves nowhere, or when a bare basename is ambiguous because two
files in the pack share it. Nothing is changed.
"""
import argparse, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
SKIP_DIRS = {'.git', 'local', '__pycache__'}

# files that belong to the user's own setup, not to the pack
USER_SIDE = {
    'CLAUDE.md', 'AGENTS.md', 'SOURCE_INDEX.md', 'README.md', 'manifest.json',
    'DATABASE_INTEGRATION.md', 'RESEARCH_BENCHMARK.md',
}
# extensions worth checking
EXTS = ('.md', '.json', '.yaml', '.yml', '.py', '.mid', '.txt')
PATH_RE = re.compile(r'`([A-Za-z0-9_][A-Za-z0-9_./<>-]*\.(?:md|json|yaml|yml|py|mid|txt))`')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=ROOT)
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    problems, checked = [], 0

    # index every file in the pack by basename, for rule 3
    by_base = {}
    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in fn:
            by_base.setdefault(f, []).append(
                os.path.relpath(os.path.join(dp, f), root).replace(os.sep, '/'))

    for dp, dn, fn in os.walk(root):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in fn:
            if not f.endswith('.md'):
                continue
            page = os.path.join(dp, f)
            rel_page = os.path.relpath(page, root).replace(os.sep, '/')
            for i, line in enumerate(open(page, encoding='utf-8', errors='replace'), 1):
                for target in PATH_RE.findall(line):
                    if '<' in target or '>' in target:
                        continue          # a pattern, not a path
                    checked += 1
                    base = os.path.basename(target)
                    if base in USER_SIDE and '/' not in target:
                        continue
                    if os.path.exists(os.path.join(root, target)):
                        continue
                    if os.path.exists(os.path.normpath(os.path.join(dp, target))):
                        continue
                    if '/' not in target and base in by_base:
                        hits = by_base[base]
                        if len(hits) > 1:
                            problems.append(
                                f'{rel_page}:{i}: ambiguous name {target}: {", ".join(hits)}. '
                                f'Use an explicit path.')
                        continue
                    problems.append(f'{rel_page}:{i}: unresolved path: {target}')

    for p in problems:
        print(p)
    print(f'{len(problems)} finding(s) in {checked} path reference(s)')
    sys.exit(1 if problems else 0)


if __name__ == '__main__':
    main()
