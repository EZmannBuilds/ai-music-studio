#!/usr/bin/env python3
"""Release check: what users already have on disk still reads.

usage: python3 tools/compat_check.py [--root .]

The CHANGELOG promises that 1.0 and 1.1 profiles, 1.0 track states, calibration profiles and paths
that user files point to keep working. This check holds those promises against real old files in
evals/fixtures/compatibility/, and fails (exit 1) when:
  - a fixture uses a key that the current schema no longer has, unless tools/vocab.json lists it
    as a field alias AND the schema itself still documents the old name (a reader has to be told);
  - a value governed by a vocabulary (tools/vocab.json key_vocabularies) is no longer accepted,
    allowing the documented aliases;
  - a profile's profile_version is not one the profile schema accepts;
  - a path that existed at the 2.0 milestone (paths_2.0.txt) no longer exists. Removing a file is
    allowed only by leaving a pointer page at its old path.

Keys are compared, not values: a fixture's content is illustrative. Where a schema leaves a field
open ([] or {} with no structure), anything below it is accepted. PyYAML is needed; without it the
check says so and passes, like schema_check.py. Nothing is changed.
"""
import argparse, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from schema_check import blocks, placeholder_free  # noqa: E402

try:
    import yaml
    HAVE_YAML = True
except ImportError:
    HAVE_YAML = False

ROOT = os.path.join(HERE, '..')
FIXTURES = os.path.join('evals', 'fixtures', 'compatibility')
# fixture file prefix -> the schema that defines it
SCHEMAS = {
    'profile_': 'shared/USER_PROFILE_SCHEMA.md',
    'track_state_': 'shared/TRACK_STATE_SCHEMA.md',
    'calibration_profile_': 'shared/PLUGIN_CALIBRATION_SCHEMA.md',
}
ACCEPTED_PROFILE_VERSIONS = {'1.0', '1.1'}
IGNORED_KEYS = {'_fixture'}


def schema_paths(path):
    """Every key path the schema's yaml blocks define, and the set of paths left open."""
    known, open_ = set(), set()

    def walk(node, prefix):
        if isinstance(node, dict):
            if not node:
                open_.add(prefix)
            for k, v in node.items():
                p = f'{prefix}.{k}' if prefix else str(k)
                known.add(p)
                if v is None or v == '' or v == [] or v == {}:
                    open_.add(p)
                walk(v, p)
        elif isinstance(node, list):
            if not node or not any(isinstance(x, (dict, list)) for x in node):
                open_.add(prefix)
            for item in node:
                walk(item, prefix + '[]')

    for lang, _, text in blocks(path):
        if lang != 'yaml':
            continue
        try:
            doc = yaml.safe_load(placeholder_free(text))
        except Exception:
            continue
        walk(doc, '')
    return known, open_


def fixture_paths(node, prefix=''):
    if isinstance(node, dict):
        for k, v in node.items():
            if k in IGNORED_KEYS:
                continue
            p = f'{prefix}.{k}' if prefix else str(k)
            yield p, k, v
            yield from fixture_paths(v, p)
    elif isinstance(node, list):
        for item in node:
            yield from fixture_paths(item, prefix + '[]')


def under_open(p, open_):
    return any(p == o or p.startswith(o + '.') or p.startswith(o + '[]') for o in open_ if o)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default=ROOT)
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    problems, n = [], 0
    fdir = os.path.join(root, FIXTURES)
    if not os.path.isdir(fdir):
        print(f'{FIXTURES}: missing')
        sys.exit(1)

    vocab = json.load(open(os.path.join(root, 'tools', 'vocab.json'), encoding='utf-8'))
    vocabs, aliases = vocab.get('vocabularies', {}), vocab.get('aliases', {})
    key_vocabs, field_aliases = vocab.get('key_vocabularies', {}), vocab.get('field_aliases', {})

    # 1. paths that existed at 2.0 still resolve
    listing = os.path.join(fdir, 'paths_2.0.txt')
    if os.path.exists(listing):
        for line in open(listing, encoding='utf-8'):
            p = line.strip()
            if p and not p.startswith('#') and not os.path.exists(os.path.join(root, p)):
                problems.append(f'{p}: existed at 2.0 and is gone; leave a pointer page at the old path')

    if not HAVE_YAML:
        for p in problems:
            print(p)
        print(f'{len(problems)} finding(s); fixture keys not checked (PyYAML not installed)')
        sys.exit(1 if problems else 0)

    # 2. every fixture's keys still exist, or are documented aliases
    for f in sorted(os.listdir(fdir)):
        schema_rel = next((s for pre, s in SCHEMAS.items() if f.startswith(pre)), None)
        if not schema_rel or not f.endswith(('.yaml', '.yml', '.json')):
            continue
        n += 1
        rel = f'{FIXTURES}/{f}'.replace(os.sep, '/')
        text = open(os.path.join(fdir, f), encoding='utf-8').read()
        try:
            doc = json.loads(text) if f.endswith('.json') else yaml.safe_load(text)
        except Exception as e:
            problems.append(f'{rel}: does not parse: {str(e).splitlines()[0]}')
            continue
        schema_path = os.path.join(root, schema_rel)
        known, open_ = schema_paths(schema_path)
        schema_text = open(schema_path, encoding='utf-8').read()
        for p, key, val in fixture_paths(doc):
            # read an old field name as its current one, everywhere in the path
            segs = p.replace('[]', '.[]').split('.')
            mapped = '.'.join(field_aliases.get(s_, s_) for s_ in segs).replace('.[]', '[]')
            parent = mapped.rsplit('.', 1)[0] if '.' in mapped else ''
            if not (mapped in known or under_open(parent, open_)):
                problems.append(f'{rel}: {p} is not in {schema_rel} and is not a documented alias')
            for old_name in (s_ for s_ in segs if s_ in field_aliases):
                if old_name not in schema_text:
                    problems.append(f'{rel}: {p} is read as {field_aliases[old_name]}, but '
                                    f'{schema_rel} no longer mentions {old_name!r}, so no reader '
                                    f'is told')
            if key in key_vocabs and val not in (None, '') and not isinstance(val, (dict, list)):
                vname = key_vocabs[key]
                allowed = set(vocabs.get(vname, []))
                if allowed and str(val) not in allowed and str(val) not in aliases.get(vname, {}):
                    problems.append(f'{rel}: {p}: {val!r} is no longer accepted by {vname}')
        if f.startswith('profile_') and isinstance(doc, dict):
            v = str(doc.get('profile_version'))
            if v not in ACCEPTED_PROFILE_VERSIONS:
                problems.append(f'{rel}: profile_version {v!r} is not one of '
                                f'{sorted(ACCEPTED_PROFILE_VERSIONS)}')

    for p in problems:
        print(p)
    print(f'{len(problems)} finding(s) in {n} fixture(s)')
    sys.exit(1 if problems else 0)


if __name__ == '__main__':
    main()
