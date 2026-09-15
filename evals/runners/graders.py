"""Deterministic assertions over an agent's response.

A response is Markdown text. Its structured parts are the fenced ```yaml blocks it contains; their
top-level keys are merged into one document (a later block's key replaces an earlier one's), so an
assertion can ask for `performance_state.timing_character.models[].model` or `session_trace.routes`
wherever in the reply the block appeared.

Every assertion returns (passed: bool, detail: str). None of them scores music. They check structure
and behaviour: that a plan names its models, that a diagnosis did not rewrite the user's song, that a
tradition was not reduced to a scale. Whether the music is good is a human question, asked in the
report's evaluation sheet.

Standard library plus PyYAML.
"""
import difflib, os, re, sys

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.join(HERE, '..', '..', 'tools')
sys.path.insert(0, TOOLS)
from skill_lint import FORBIDDEN, PROHIBITION  # noqa: E402  the pack's own ruled-out phrasing

FENCE = re.compile(r'^```(?:yaml|yml)\s*\n(.*?)^```', re.S | re.M)


class Response:
    def __init__(self, text, fixtures_dir=None):
        # HTML comments are notes to a reader (the expected responses carry their must_fail list in
        # one), not part of what the agent said.
        text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
        self.text = text
        self.fixtures_dir = fixtures_dir
        self.doc, self.parse_errors = {}, []
        for block in FENCE.findall(text):
            try:
                data = yaml.safe_load(block)
            except Exception as e:
                self.parse_errors.append(str(e).splitlines()[0])
                continue
            if isinstance(data, dict):
                self.doc.update(data)
        self.prose = FENCE.sub('', text)


def values(doc, path):
    """All values at a dotted path. `[]` after a key walks every item of a list."""
    cur = [doc]
    for part in path.split('.'):
        nxt = []
        many = part.endswith('[]')
        key = part[:-2] if many else part
        for node in cur:
            if isinstance(node, dict) and key in node:
                v = node[key]
                if many:
                    nxt.extend(v if isinstance(v, list) else [])
                else:
                    nxt.append(v)
        cur = nxt
    return cur


def _empty(v):
    return v is None or v == '' or v == [] or v == {}


def a_block_present(r, spec, ctx):
    ok = spec in r.doc
    return ok, f'block {spec!r} {"present" if ok else "missing"}'


def a_field_equals(r, spec, ctx):
    vs = values(r.doc, spec['path'])
    want = spec['value']
    ok = bool(vs) and all(str(v).lower() == str(want).lower() for v in vs)
    return ok, f'{spec["path"]} = {vs!r}, want {want!r}'


def a_field_in(r, spec, ctx):
    vs = values(r.doc, spec['path'])
    allowed = [str(x).lower() for x in spec['values']]
    ok = bool(vs) and all(str(v).lower() in allowed for v in vs)
    return ok, f'{spec["path"]} = {vs!r}, want one of {spec["values"]}'


def a_field_nonempty(r, spec, ctx):
    vs = values(r.doc, spec)
    ok = bool(vs) and all(not _empty(v) for v in vs)
    return ok, f'{spec} = {vs!r}'


def a_field_empty(r, spec, ctx):
    vs = values(r.doc, spec)
    ok = bool(vs) and all(_empty(v) for v in vs)
    return ok, f'{spec} = {vs!r}, want present and empty'


def a_field_in_vocab(r, spec, ctx):
    vocab = ctx['vocab']
    allowed = vocab.get('vocabularies', {}).get(spec['vocab'], vocab.get(spec['vocab'], []))
    vs = values(r.doc, spec['path'])
    bad = [v for v in vs if str(v) not in allowed]
    ok = bool(vs) and not bad
    return ok, f'{spec["path"]} = {vs!r}; outside {spec["vocab"]}: {bad!r}'


def a_min_count(r, spec, ctx):
    vs = values(r.doc, spec['path'])
    n = sum(len(v) if isinstance(v, (list, dict)) else 1 for v in vs if not _empty(v))
    return n >= spec['min'], f'{spec["path"]} has {n}, want at least {spec["min"]}'


def a_regex_present(r, spec, ctx):
    where = r.prose if spec.get('in') == 'prose' else r.text
    flags = re.I if spec.get('ignore_case', True) else 0
    m = re.search(spec['pattern'], where, flags | re.M)
    return bool(m), f'/{spec["pattern"]}/ {"found" if m else "not found"}'


def a_regex_absent(r, spec, ctx):
    where = r.prose if spec.get('in') == 'prose' else r.text
    flags = re.I if spec.get('ignore_case', True) else 0
    m = re.search(spec['pattern'], where, flags | re.M)
    return not m, f'/{spec["pattern"]}/ ' + (f'found: {m.group(0)!r}' if m else 'absent')


def a_regex_count(r, spec, ctx):
    where = r.prose if spec.get('in') == 'prose' else r.text
    n = len(re.findall(spec['pattern'], where, re.I | re.M))
    return n >= spec['min'], f'/{spec["pattern"]}/ found {n} times, want at least {spec["min"]}'


def a_no_random_humanization(r, spec, ctx):
    """The pack's own ruled-out phrasing (tools/skill_lint.py), applied to the reply, plus any
    percentage of randomness or humanisation."""
    pct = re.compile(r'\b(?:humani[sz]\w*|random\w*|jitter)\b[^.\n]{0,40}?\d+\s*%|'
                     r'\d+\s*%\s*(?:of\s+)?(?:humani[sz]\w*|random\w*|jitter)', re.I)
    for line in r.text.split('\n'):
        if pct.search(line) and not PROHIBITION.search(line):
            return False, f'percentage of randomness: {line.strip()[:100]!r}'
        for pat, why in FORBIDDEN:
            if pat.search(line) and not PROHIBITION.search(line):
                return False, f'{why}: {line.strip()[:100]!r}'
    for path in ('performance_state', 'performance_plan'):
        for v in values(r.doc, path):
            if isinstance(v, dict) and re.search(r'random|humani[sz]ation_amount', str(list(v.keys())), re.I):
                return False, f'{path} has a random/humanization-amount field'
    return True, 'no random humanisation'


def a_routes_include(r, spec, ctx):
    routes = [str(x) for v in values(r.doc, 'session_trace.routes') for x in (v or [])]
    missing = [x for x in spec if x not in routes]
    return not missing, f'routes {routes}; missing {missing}'


def a_routes_exclude(r, spec, ctx):
    routes = [str(x) for v in values(r.doc, 'session_trace.routes') for x in (v or [])]
    extra = [x for x in spec if x in routes]
    return not extra, f'routes {routes}; forbidden present {extra}'


def a_knowledge_loaded(r, spec, ctx):
    loaded = [str(x) for v in values(r.doc, 'session_trace.knowledge_loaded') for x in (v or [])]
    missing = [x for x in spec if not any(x in l for l in loaded)]
    return not missing, f'knowledge_loaded {loaded}; missing {missing}'


def a_fixture_not_rewritten(r, spec, ctx):
    """The user's own lines may be quoted exactly, or discussed, but not replaced by near-copies.
    A response line that is similar to a fixture line without being that line is a rewrite."""
    path = os.path.join(r.fixtures_dir or '', spec['fixture'])
    src = [l.strip() for l in open(path, encoding='utf-8') if l.strip() and not l.startswith('#')]
    lo, hi = spec.get('similarity', [0.6, 0.97])
    allowed = spec.get('max_rewritten_lines', 0)
    rewritten = []
    for line in r.text.split('\n'):
        s = line.strip().strip('>*-"` ')
        if len(s) < 12 or s in src:
            continue
        for orig in src:
            ratio = difflib.SequenceMatcher(None, s.lower(), orig.lower()).ratio()
            if lo <= ratio < hi:
                rewritten.append((orig, s))
                break
    ok = len(rewritten) <= allowed
    detail = f'{len(rewritten)} rewritten line(s), allowed {allowed}'
    if rewritten:
        detail += f'; e.g. {rewritten[0][0]!r} -> {rewritten[0][1]!r}'
    return ok, detail


def a_appears_before(r, spec, ctx):
    """`first` must occur before `then`; if `then` never occurs the assertion passes."""
    a = re.search(spec['first'], r.text, re.I | re.M)
    b = re.search(spec['then'], r.text, re.I | re.M)
    if not b:
        return True, f'/{spec["then"]}/ absent'
    ok = bool(a) and a.start() < b.start()
    return ok, f'/{spec["first"]}/ at {a.start() if a else None}, /{spec["then"]}/ at {b.start()}'


def a_any_of(r, spec, ctx):
    results = [grade_one(r, s, ctx) for s in spec]
    ok = any(p for p, _ in results)
    return ok, 'any of: ' + ' | '.join(d for _, d in results)


def a_all_of(r, spec, ctx):
    results = [grade_one(r, s, ctx) for s in spec]
    ok = all(p for p, _ in results)
    return ok, 'all of: ' + ' | '.join(d for _, d in results)


def a_not(r, spec, ctx):
    p, d = grade_one(r, spec, ctx)
    return not p, f'not ({d})'


ASSERTIONS = {
    'block_present': a_block_present,
    'field_equals': a_field_equals,
    'field_in': a_field_in,
    'field_nonempty': a_field_nonempty,
    'field_empty': a_field_empty,
    'field_in_vocab': a_field_in_vocab,
    'min_count': a_min_count,
    'regex_present': a_regex_present,
    'regex_absent': a_regex_absent,
    'regex_count': a_regex_count,
    'no_random_humanization': a_no_random_humanization,
    'routes_include': a_routes_include,
    'routes_exclude': a_routes_exclude,
    'knowledge_loaded': a_knowledge_loaded,
    'fixture_not_rewritten': a_fixture_not_rewritten,
    'appears_before': a_appears_before,
    'any_of': a_any_of,
    'all_of': a_all_of,
    'not': a_not,
}


def grade_one(r, assertion, ctx):
    """assertion is {type: spec} with exactly one key, plus optional id and why."""
    kinds = [k for k in assertion if k in ASSERTIONS]
    if len(kinds) != 1:
        return False, f'malformed assertion {assertion!r}'
    kind = kinds[0]
    return ASSERTIONS[kind](r, assertion[kind], ctx)


def grade(text, assertions, ctx, fixtures_dir=None):
    """Grade one response. Returns a list of {id, passed, detail}."""
    r = Response(text, fixtures_dir)
    out = []
    if r.parse_errors:
        out.append({'id': 'yaml_parses', 'passed': False,
                    'detail': 'a yaml block does not parse: ' + r.parse_errors[0]})
    for i, a in enumerate(assertions):
        aid = a.get('id', f'a{i + 1}')
        try:
            passed, detail = grade_one(r, a, ctx)
        except Exception as e:  # a broken assertion is a failure, never a pass
            passed, detail = False, f'assertion error: {e}'
        out.append({'id': aid, 'passed': bool(passed), 'detail': detail})
    return out
