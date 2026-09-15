# Evaluation case schema

One file per case, in `evals/cases/<category>/<ID>.yaml`. `evals/runners/cases.py` loads and
validates cases, and `tools/eval_selftest.py` runs that validation in CI.

```yaml
test:
  id:                      # D18, PF1, B1 ... unique; matches the file name
  title:
  category:                # diversity | project_work | performance | routing | cultural_systems |
                           # tuning | interaction_modes | rhythm_and_form |
                           # experimental_and_adaptive | compatibility; matches the folder
  source:                  # where the case comes from: a benchmark id, or "new in 2.1"
  brief:                   # what the user says, written as a user would write it
  supplied_context: []     # files under evals/fixtures/ given to the agent as the user's material
  expected_routes:
    must_include: []       # specialist folder names that must appear in session_trace.routes
    must_not_include: []
  required_behaviors: []   # prose, for the human reader and the report
  forbidden_behaviors: []  # prose
  structural_assertions:   # deterministic checks; each has an id and exactly one type
    - id:
      why:                 # optional: what the assertion stands for
      <type>: <spec>
  human_questions: []      # what only a listener or reader can judge; at least one
  trials: 3                # how many times to run it; agents are nondeterministic
  batch:                   # only for batch cases (B1, B2, B3)
    kind: track_dna | exploration      # default track_dna
    briefs: []             # one session per brief
    threshold: 0.9         # share of rows that must agree for a dimension to collapse
    watch: []              # the dimensions whose collapse fails the case
    brief_implied: {}      # dimension -> values the briefs themselves require; never a collapse
    fail_if: any_watched_collapsed | all_watched_collapsed | any_always_changed
```

## Assertion types

All of them read the reply: its prose, and the fenced `yaml` blocks in it, whose top-level keys are
merged into one document. A path uses dots, and `[]` after a key to walk every item of a list, e.g.
`performance_state.timing_character.models[].model`.

| Type | Spec | Passes when |
|---|---|---|
| `block_present` | `key` | a yaml block has that top-level key |
| `field_equals` | `{path, value}` | every value at the path equals it (case-insensitive) |
| `field_in` | `{path, values}` | every value at the path is one of them |
| `field_nonempty` | `path` | the path exists and every value is non-empty |
| `field_empty` | `path` | the path exists and every value is empty; absent is not empty |
| `field_in_vocab` | `{path, vocab}` | every value is in that list in `tools/vocab.json` |
| `min_count` | `{path, min}` | the list or map at the path has at least `min` items |
| `regex_present` | `{pattern, in: text or prose, ignore_case}` | the pattern occurs |
| `regex_absent` | same | the pattern does not occur |
| `regex_count` | `{pattern, min}` | the pattern occurs at least `min` times |
| `no_random_humanization` | `true` | no percentage of randomness and none of the phrasing `tools/skill_lint.py` rules out |
| `routes_include` / `routes_exclude` | `[specialists]` | against `session_trace.routes` |
| `knowledge_loaded` | `[paths]` | against `session_trace.knowledge_loaded` |
| `fixture_not_rewritten` | `{fixture, max_rewritten_lines, similarity}` | no line of the reply is a near-copy of a line of the user's material |
| `appears_before` | `{first, then}` | `first` occurs before `then`, or `then` never occurs |
| `any_of` / `all_of` | `[assertions]` | combinators |
| `not` | `assertion` | inverts one |

**Prefer structure to phrases.** An assertion on a parsed field (`performance_state.realism_target`)
is harder to satisfy by accident, and harder to game, than a regular expression over prose. Use a
pattern where the behaviour lives only in words, and keep the human question beside it.

## Expected responses

Every case has `evals/expected/<ID>/pass/` and `evals/expected/<ID>/fail/`, hand-written, not model
output. A failing response starts with `<!-- must_fail: id, id -->` naming the assertions it must
fail. `tools/eval_selftest.py` grades both with the same graders a real run uses. That is how the
harness is tested without calling a model: if a grader stops catching what it claims to catch, CI
fails. Batch cases keep one folder per trial set (pass/set-1/01.md to 10.md).

## What a case must not do

- **Score music.** There is no numeric quality measure anywhere in this folder, and a case must not
  add one. Musical success is asked in `human_questions` and answered by a person.
- **Tell the agent the answer.** The brief is what a user would write; the grading criteria stay in
  the case file and are never sent.
