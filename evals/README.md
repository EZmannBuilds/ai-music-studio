# Evaluating the studio

`python3 tools/check_all.py` proves the pack is internally consistent. It cannot prove that the
studio behaves the way its pages say: that a diagnosis stays a diagnosis, that a performance comes
from models rather than randomness, that unrelated briefs get different architectures, that a
tradition is not reduced to a scale. This folder tests those things.

## Three layers, kept apart

| Layer | What it answers | Where | Runs |
|---|---|---|---|
| **Static** | Is the repository correct? Paths resolve, schemas parse, examples obey their schemas, old files still read, evidence labels match what was read. | `tools/` | on every push, in CI |
| **Behavioural** | What does the agent actually do? Routes, modes, preserved material, named models, declined requests, batch diversity. | `evals/` | on demand, against a real agent |
| **Musical and human** | Is the result musically successful? | `evals/reports/<run>/HUMAN_EVALUATION.md` | by a person, listening |

The behavioural layer checks structure and behaviour with deterministic assertions. **It computes no
score for musical quality, and must never be given one.** Human listening is the authority on
whether the music works, as `shared/RESEARCH_RULES.md` says.

## Layout

```text
evals/
├── cases/<category>/<ID>.yaml   41 cases: the D1-D20, B1-B3 and N1-N4 benchmark, plus performance,
│                                routing, cultural-system and compatibility cases new in 2.1
├── fixtures/                    the user's material a case supplies, and old files for compatibility
├── expected/<ID>/{pass,fail}/   hand-written responses that must pass and must fail each case
├── schemas/CASE_SCHEMA.md       the case format and every assertion type
├── runners/
│   ├── run_evals.py             the runner
│   ├── graders.py               the assertions
│   ├── diversity.py             batch diversity (B1, B2) and candidate-set habits (B3)
│   ├── cases.py                 loading and validation
│   ├── PROMPT_TEMPLATE.md       exactly what the agent is sent
│   ├── adapters/manual.py       grade responses already on disk
│   ├── adapters/command.py      run any command-line agent
│   └── examples/COMMAND_TEMPLATES.md
└── reports/                     run output (git-ignored) and the human evaluation template
```

## Running

```bash
python3 evals/runners/run_evals.py --list

# grade replies you collected by hand: <dir>/<CASE_ID>/<trial>.md
python3 evals/runners/run_evals.py --adapter manual --responses <dir>

# run a command-line agent; start small, a full run is expensive
python3 evals/runners/run_evals.py --adapter command --cmd "<agent command>" --only D16,D18,N1-C
```

Each case runs for several trials, because agents are nondeterministic. Every assertion is reported as
passed in k of k trials, and a case that passes in some trials and not others is **flaky**, which is
reported as such rather than averaged away. Each run writes, into its own folder under
evals/reports/runs/: results.json, REPORT.md, the replies, and a HUMAN_EVALUATION.md sheet with the
questions only a person can answer.

Routing and material preservation are read from the **session trace**, an optional block the Director
writes when asked (`shared/SPECIALIST_HANDOFF_SCHEMA.md`). The prompt asks for it; it never tells the
agent what the case is looking for.

## How the harness is itself tested

`tools/eval_selftest.py`, part of `check_all`, validates every case and grades the hand-written
expected responses: every passing response must pass, and every failing response must fail the
assertions it names. So CI catches a grader that has stopped detecting a rewritten lyric, a
percentage of humanisation or a collapsed batch, without calling any model.

## Adding a case

1. Write `evals/cases/<category>/<ID>.yaml` to `schemas/CASE_SCHEMA.md`.
2. Prefer assertions on parsed fields over patterns in prose, and always add a human question.
3. Write a passing and a failing response, as response.md in evals/expected/<ID>/pass/ and
   evals/expected/<ID>/fail/; the failing one names what it must fail in `<!-- must_fail: ... -->`.
4. `python3 tools/eval_selftest.py`.

## What these results can and cannot show

A pass shows that the studio did the structural thing the case checks, in that run. It does not show
that the music is good, that the behaviour holds for briefs the cases did not try, or that a
different model will behave the same. The cases are a floor, not a certificate.
