#!/usr/bin/env python3
"""Release check: every SKILL.md is shaped like a skill, and stays neutral.

usage: python3 tools/skill_lint.py [--root .]

Fails (exit 1) when a SKILL.md:
  - has no front matter, or its name does not match its folder;
  - has no version or description;
  - has no mission;
  - never says what it does not own;
  - uses a phrase the pack has ruled out, such as randomising timing;
  - names a commercial product outside the files where product names belong.

The ruled-out phrases are checked as instructions, not as mentions. The pages that forbid
randomising timing have to be able to say so, and a diagnosis that names the mistake is doing its
job, so a line carrying a prohibition or a quotation is not a finding. Nothing is changed.
"""
import argparse, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
SKIP_DIRS = {'.git', 'local', '__pycache__'}

# Product names belong in the adapters, the free-instruments reference, the auditor's worked
# example and the research pages that cite manufacturer documentation. Not in a neutral skill.
# Some shared pages name products because naming them is the point: the adapter contract exists to
# say that DAWs have different object models, file naming shows what a session file is called, and
# render verification gives a concrete export example.
PRODUCT_OK_PREFIXES = (
    'daw-adapters/', 'shared/FREE_INSTRUMENTS.md', 'shared/PLUGIN_CALIBRATION_SCHEMA.md',
    'shared/DAW_ADAPTER_CONTRACT.md', 'shared/FILE_NAMING.md', 'shared/RENDER_VERIFICATION.md',
    'plugin-auditor/SKILL.md', 'research/', 'README.md', 'CHANGELOG.md',
)
PRODUCTS = re.compile(
    r'\b(ableton|live\s+1[12]|fl\s+studio|pro\s+tools|logic\s+pro|cubase|reaper|studio\s+one|'
    r'bitwig|spitfire|kontakt|native\s+instruments|orchestral\s+tools|vienna\s+symphonic|'
    r'cinematic\s+studio|serum|vital|omnisphere|superior\s+drummer|ezdrummer|addictive\s+drums|'
    r'pianoteq|hammond|leslie|wwise|fmod|izotope|melda|soundflow|abletonosc)\b', re.I)

# Phrases the pack has ruled out, written as instructions. The second element is why.
FORBIDDEN = [
    (re.compile(r'\b(?:apply|add|use|set)\s+(?:a\s+)?random(?:ly)?\s*'
                r'(?:humani[sz]\w*|timing|velocity|jitter|offsets?)', re.I),
     'name a model instead, per shared/HUMAN_PERFORMANCE_SCHEMA.md section 3'),
    (re.compile(r'\bhumani[sz]e\s+(?:by\s+)?\d+\s*%', re.I),
     'a percentage of humanisation is what shared/HUMAN_PERFORMANCE_SCHEMA.md rules out'),
    (re.compile(r'\brandom(?:ly)?\s+(?:move|shift|offset|nudge)\s+'
                r'(?:the\s+)?(?:midi\s+)?notes?', re.I),
     'moving notes at random is contradicted by the microtiming research'),
    (re.compile(r'\brandomi[sz]e\s+(?:the\s+)?(?:timing|velocit|note)', re.I),
     'name a model instead, per shared/HUMAN_PERFORMANCE_SCHEMA.md section 3'),
]

# A line that forbids, diagnoses or quotes the mistake is not committing it.
PROHIBITION = re.compile(
    r'\b(?:not|never|no|rather than|instead|stop|forbid\w*|avoid|avoids|rules? out|'
    r'do not|does not|is not|are not|cannot|without|usually|which is|the thing|'
    r'contradict\w*|fail\w*|wrong|error|mistake|remove)\b|"', re.I)


def front_matter(text):
    if not text.startswith('---\n'):
        return None
    end = text.find('\n---\n', 4)
    if end == -1:
        return None
    fm = {}
    for line in text[4:end].split('\n'):
        if ':' in line:
            k, v = line.split(':', 1)
            fm[k.strip()] = v.strip()
    return fm


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=ROOT)
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    problems, n = [], 0

    # 1. every SKILL.md
    for d in sorted(os.listdir(root)):
        full = os.path.join(root, d)
        skill = os.path.join(full, 'SKILL.md')
        if not (os.path.isdir(full) and d not in SKIP_DIRS and os.path.exists(skill)):
            continue
        n += 1
        rel = f'{d}/SKILL.md'
        text = open(skill, encoding='utf-8').read()

        fm = front_matter(text)
        if fm is None:
            problems.append(f'{rel}: no front matter')
        else:
            if fm.get('name') != d:
                problems.append(f'{rel}: front matter name {fm.get("name")!r} != folder {d!r}')
            if not re.fullmatch(r'\d+(\.\d+)*', fm.get('version', '')):
                problems.append(f'{rel}: version {fm.get("version")!r} is not a version string')
            if len(fm.get('description', '')) < 40:
                problems.append(f'{rel}: description is missing or too short to route on')

        if not re.search(r'^##\s*(?:Mission|Purpose)\b', text, re.M):
            problems.append(f'{rel}: no "## Mission" or "## Purpose" section')

        # every skill has to draw a boundary somewhere
        boundary = re.search(
            r'does\s+not\s+own|##\s*Does not own|must\s+NOT|it\s+does\s+not:|'
            r'is\s+not\s+(?:building|mixing|the)|does\s+not\s+(?:decide|replace|include|'
            r'choose|change|set)\b|not\s+a\s+\w+\s+specialist|Never\s+instruct',
            text, re.I)
        if not boundary:
            problems.append(f'{rel}: never says what it does not own')

    # 2. forbidden phrases and product names, across every page
    for dp, dn, fn in os.walk(root):
        dn[:] = [x for x in dn if x not in SKIP_DIRS]
        for f in sorted(fn):
            if not f.endswith('.md'):
                continue
            path = os.path.join(dp, f)
            rel = os.path.relpath(path, root).replace(os.sep, '/')
            for i, line in enumerate(open(path, encoding='utf-8', errors='replace'), 1):
                for pat, why in FORBIDDEN:
                    if pat.search(line) and not PROHIBITION.search(line):
                        problems.append(f'{rel}:{i}: ruled-out phrasing: {why}')
                if not rel.startswith(PRODUCT_OK_PREFIXES):
                    m = PRODUCTS.search(line)
                    if m:
                        problems.append(
                            f'{rel}:{i}: product name "{m.group(0)}" in a tool-neutral page')

    for p in problems:
        print(p)
    print(f'{len(problems)} finding(s) across {n} skill(s)')
    sys.exit(1 if problems else 0)


if __name__ == '__main__':
    main()
