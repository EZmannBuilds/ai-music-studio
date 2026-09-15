#!/usr/bin/env python3
"""Release check: no user-specific content in the skill files.

usage: python3 tools/privacy_check.py [--profile path/to/profile.yaml] [--root .]

Fails (exit 1) when a file in the pack contains:
  - an absolute home or user path: /Users/..., /home/..., /Volumes/..., /mnt/<drive>/Users/...,
    C:\\Users\\... (one backslash or two, as in JSON) or C:/Users/..., a ~/ path, $HOME/...,
    ${HOME}/... or %USERPROFILE%;
  - any term from the profile's privacy.private_terms list (names, titles, paths), matched as a
    whole word, case-insensitively, so that a surname does not match inside another one
    ("Lee" is found in "Ann Lee" but not in "Ashlee").

Text files are read line by line. MIDI files are read as bytes, because track names, markers and
lyric events can carry a name. A path whose user segment is a placeholder in angle brackets
(/Users/<you>/...) is generic, and so are the few locations listed in GENERIC, which are the same on
every machine of that OS. The profile itself and any local/ folder are skipped; this tool and the
profile template are checked for private terms but not for paths, since they describe path patterns.
Nothing is changed.
"""
import argparse, os, re, sys

PATH_RE = re.compile(
    r"(/Users/[^\s`'\"]+|/home/[^\s`'\"]+|/Volumes/[^\s`'\"]+|/mnt/[a-z]/Users/[^\s`'\"]+"
    r"|[A-Za-z]:(?:\\{1,2}|/)Users(?:\\{1,2}|/)[^\s`'\"]*"
    r"|~/[^\s`'\"]+|\$\{?HOME\}?/[^\s`'\"]+|%USERPROFILE%[^\s`'\"]*)")
# a user segment written as a placeholder: /Users/<you>, C:\Users\<name>, /home/<user>
PLACEHOLDER = re.compile(r"(?:Users|home)(?:\\{1,2}|/)<")
SKIP_DIRS = {'.git', 'local', '__pycache__'}
# generic locations that are the same on every machine of that OS
GENERIC = ('~/Library/Audio/Plug-Ins', '~/Music/Ableton/User Library', '~/Library/Application Support')
# These two describe path patterns as examples, so only the path check skips them. They are still
# scanned for private terms: a name left in the tool or the template would be published.
NO_PATH_CHECK = {'privacy_check.py', 'user-profile.example.yaml'}
TEXT_EXT = ('.md', '.json', '.yaml', '.yml', '.txt', '.py', '.csv', '.toml', '.cfg', '.ini', '.html')
BINARY_EXT = ('.mid', '.midi')


def private_terms(profile):
    """Read privacy.private_terms from a simple YAML profile without needing a YAML library."""
    terms, inside = [], False
    for line in open(profile, encoding='utf-8'):
        m = re.match(r'^\s*private_terms:\s*\[(.*)\]\s*$', line)
        if m:
            return [t.strip().strip('"\'') for t in m.group(1).split(',') if t.strip()]
        if re.match(r'^\s*private_terms:\s*$', line):
            inside = True
            continue
        if inside:
            m = re.match(r'^\s*-\s*(.+?)\s*$', line)
            if m:
                terms.append(m.group(1).strip('"\''))
            elif line.strip() and not line.startswith(' ' * 4):
                break
    return terms


def term_patterns(terms):
    out = []
    for t in terms:
        left = r'(?<!\w)' if t[0].isalnum() or t[0] == '_' else ''
        right = r'(?!\w)' if t[-1].isalnum() or t[-1] == '_' else ''
        out.append((t, re.compile(left + re.escape(t) + right, re.I)))
    return out


def path_hits(text):
    for m in PATH_RE.finditer(text):
        found = m.group(0)
        if PLACEHOLDER.search(found):
            continue
        if any(text[m.start():].startswith(g) for g in GENERIC):
            continue
        yield found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--profile')
    ap.add_argument('--root', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
    a = ap.parse_args()
    terms = term_patterns([t for t in (private_terms(a.profile) if a.profile else []) if t])
    skip_abs = {os.path.abspath(a.profile)} if a.profile else set()
    hits, n_files = [], 0
    for dp, dn, fn in os.walk(a.root):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in sorted(fn):
            p = os.path.join(dp, f)
            if os.path.abspath(p) in skip_abs:
                continue
            check_paths = f not in NO_PATH_CHECK
            if f.endswith(TEXT_EXT):
                n_files += 1
                for i, line in enumerate(open(p, encoding='utf-8', errors='replace'), 1):
                    for found in (path_hits(line) if check_paths else ()):
                        hits.append((p, i, 'path', found))
                    for t, pat in terms:
                        if pat.search(line):
                            hits.append((p, i, 'private term', t))
            elif f.endswith(BINARY_EXT):
                n_files += 1
                text = open(p, 'rb').read().decode('latin-1')
                for found in path_hits(text):
                    hits.append((p, 0, 'path in MIDI data', found))
                for t, pat in terms:
                    if pat.search(text):
                        hits.append((p, 0, 'private term in MIDI data', t))
    for p, i, kind, what in hits:
        where = f':{i}' if i else ''
        print(f'{os.path.relpath(p, a.root)}{where}: {kind}: {what}')
    print(f'{len(hits)} finding(s) in {n_files} file(s)' +
          ('' if a.profile else ' (no profile given: paths only)'))
    sys.exit(1 if hits else 0)


if __name__ == '__main__':
    main()
