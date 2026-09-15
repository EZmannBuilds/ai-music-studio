#!/usr/bin/env python3
"""Release check: the manifest describes the folder, and the versions agree.

usage: python3 tools/manifest_check.py [--root .]

Fails (exit 1) when:
  - a path listed in manifest.json does not exist;
  - a SKILL.md, shared/ page, research/ page, adapter or tool is not listed in the manifest;
  - the manifest version is not a version string (a plain one such as 2.1, or a pre-release such
    as 2.1-dev, 2.1-beta.1 or 2.1-rc.1);
  - README.md, CHANGELOG.md, manifest.json and any SKILL.md front matter disagree about the version;
  - a pre-release version has no CHANGELOG heading that says it is unreleased;
  - README.md's specialist count does not match the manifest.
Nothing is changed.
"""
import argparse, json, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
# folders whose .md files must all be listed in manifest["shared"] / ["research"]
TRACKED = {
    'shared': 'shared',
    'research': 'research',
    'daw-adapters': 'adapters',
    'profiles': 'profiles',
    'tools': 'tools',
}
SKIP = {'.git', 'local', '__pycache__'}
# A plain version, or a pre-release one. Keep in step with skill_lint.py.
VERSION_RE = r'\d+(?:\.\d+)*(?:-(?:dev|beta\.\d+|rc\.\d+))?'

WORDS = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
         9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
         15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
         20: 'twenty'}


def walk(root, sub):
    out = []
    base = os.path.join(root, sub)
    if not os.path.isdir(base):
        return out
    for dp, dn, fn in os.walk(base):
        dn[:] = [d for d in dn if d not in SKIP]
        for f in sorted(fn):
            if f.startswith('.'):
                continue
            out.append(os.path.relpath(os.path.join(dp, f), root).replace(os.sep, '/'))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=ROOT)
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    problems = []

    mpath = os.path.join(root, 'manifest.json')
    try:
        m = json.load(open(mpath, encoding='utf-8'))
    except Exception as e:
        print(f'manifest.json: cannot parse: {e}')
        sys.exit(2)

    listed = set()
    for key, val in m.items():
        if isinstance(val, list):
            for p in val:
                if isinstance(p, str) and ('/' in p or p.endswith(('.md', '.json', '.py', '.yaml'))):
                    listed.add(p)
        elif isinstance(val, str) and val.endswith(('.md', '.json', '.py')):
            listed.add(val)

    # 1. every listed path exists
    for p in sorted(listed):
        if not os.path.exists(os.path.join(root, p)):
            problems.append(f'manifest.json lists a path that does not exist: {p}')

    # 2. every skill is listed
    skills_on_disk = []
    for d in sorted(os.listdir(root)):
        full = os.path.join(root, d)
        if os.path.isdir(full) and d not in SKIP and os.path.exists(os.path.join(full, 'SKILL.md')):
            skills_on_disk.append(f'{d}/SKILL.md')
    for s in skills_on_disk:
        if s not in listed:
            problems.append(f'SKILL.md not listed in manifest.json: {s}')

    # 3. every tracked file is listed
    for sub in TRACKED:
        for p in walk(root, sub):
            if p.endswith(('.md', '.json', '.py', '.yaml')) and p not in listed:
                problems.append(f'file not listed in manifest.json: {p}')

    # 4. version sanity and agreement
    version = str(m.get('version', ''))
    if not re.fullmatch(VERSION_RE, version):
        problems.append(f'manifest.json version is not a version string: {version!r}')
    prerelease = '-' in version

    ch = os.path.join(root, 'CHANGELOG.md')
    if os.path.exists(ch):
        head = open(ch, encoding='utf-8').read()
        mm = re.search(r'^##\s*(' + VERSION_RE + r')(.*)$', head, re.M)
        if not mm:
            problems.append('CHANGELOG.md: no version heading found')
        else:
            if mm.group(1) != version:
                problems.append(f'CHANGELOG.md newest version {mm.group(1)} != manifest {version}')
            if prerelease and 'unreleased' not in mm.group(2).lower():
                problems.append(f'CHANGELOG.md: {version} is a pre-release, so its heading must say '
                                f'"unreleased"')

    for s in skills_on_disk:
        text = open(os.path.join(root, s), encoding='utf-8').read()
        fm = re.match(r'---\n(.*?)\n---\n', text, re.S)
        sv = re.search(r'^version:\s*(\S+)', fm.group(1), re.M) if fm else None
        if sv and sv.group(1) != version:
            problems.append(f'{s}: front matter version {sv.group(1)} != manifest {version}')

    # 5. README specialist count
    rd = os.path.join(root, 'README.md')
    if os.path.exists(rd):
        txt = open(rd, encoding='utf-8').read()
        n_specialists = len([s for s in skills_on_disk if not s.startswith('music-director/')])
        word = WORDS.get(n_specialists, str(n_specialists))
        pat = re.compile(r'\b(' + '|'.join(WORDS.values()) + r'|\d+)\s+specialists?\b', re.I)
        found = pat.findall(txt)
        wrong = [f for f in found if f.lower() not in (word, str(n_specialists))]
        if wrong:
            problems.append(
                f'README.md says {sorted(set(wrong))} specialists; the folder has {n_specialists} '
                f'({word})')
        if not found:
            problems.append('README.md: no specialist count found to check')
        rv = re.search(r'^Version\s+(' + VERSION_RE + r')\b', txt, re.M)
        if not rv:
            problems.append('README.md: no "Version x.y" line found to check')
        elif rv.group(1) != version:
            problems.append(f'README.md says version {rv.group(1)}; manifest says {version}')

    for p in problems:
        print(p)
    print(f'{len(problems)} finding(s)')
    sys.exit(1 if problems else 0)


if __name__ == '__main__':
    main()
