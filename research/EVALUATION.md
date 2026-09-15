# Evaluation: how the studio's behaviour is tested

The evidence behind `evals/`. The harness's design rests on a few claims about how prompt and agent
systems are regression-tested; each is recorded here with what was read and where it stops. Record
format: `shared/RESEARCH_RULES.md`, "Research records".

## Scope and method

Three sources were opened on 2026-09-15: the abstract of a benchmark paper on agent reliability over
repeated trials, the abstract of a study of language models used as judges, and the assertion
documentation of an open-source prompt-testing tool. None of the papers was read beyond its abstract,
so their claims are recorded as `standard-reference`. The rest of the design is inference, labelled as
such.

## Sources

| id | citation | type | read | url | accessed |
|---|---|---|---|---|---|
| YAO-2024-TAU-BENCH | Shunyu Yao, Noah Shinn, Pedram Razavi and Karthik Narasimhan, "τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains", arXiv:2406.12045, 2024 | academic (computer science) | abstract | https://arxiv.org/abs/2406.12045 | 2026-09-15 |
| ZHENG-2023-LLM-JUDGE | Lianmin Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena", arXiv:2306.05685, 2023 | academic (computer science) | abstract | https://arxiv.org/abs/2306.05685 | 2026-09-15 |
| PROMPTFOO-ASSERTIONS | promptfoo documentation, "Assertions and metrics" (expected outputs) | specification | section | https://www.promptfoo.dev/docs/configuration/expected-outputs/ | 2026-09-15 |

## Records

### EVAL-01 One run is not a result
- claim: an agent that passes a task once may fail it on the next attempt, so a behavioural case is run several times and reported as passed in k of k trials, with a case that sometimes passes marked flaky.
- source: YAO-2024-TAU-BENCH (abstract)
- source_type: standard reference
- confidence: medium
- scope: tool-using conversational agents in the benchmark's retail and airline domains
- limitations: the abstract reports reliability collapsing across eight trials for the models it tested; it says nothing about music tasks, and the right number of trials here is not established
- inference: the default of three trials is a cost compromise chosen for this pack, not a figure from the source

### EVAL-02 Deterministic assertions are the base layer
- claim: prompt test suites commonly define cases with assertions of two kinds, programmatic checks (equality, containment, pattern, structure, code) that need no model, and model-graded checks; the base harness uses only the first kind.
- source: PROMPTFOO-ASSERTIONS (section)
- source_type: specification
- confidence: high
- scope: one widely used open-source tool's case format
- limitations: one tool's documentation shows a practice, not that it is universal
- inference: keeping the base harness deterministic is this pack's choice, so that CI needs no model and no account

### EVAL-03 A model as judge is not used for musical quality
- claim: strong language models used as judges agree with human preference at about the rate humans agree with each other in the studied settings, but show position, verbosity and self-enhancement biases; the harness therefore does not use a model to judge musical quality, and keeps listening human.
- source: ZHENG-2023-LLM-JUDGE (abstract)
- source_type: standard reference
- confidence: medium
- scope: open-ended chat answers in the paper's benchmarks, not music
- limitations: the agreement figure is for chat responses; nothing in the abstract addresses judging audio, composition or performance
- inference: extending the caution to music is inference, and is also what shared/RESEARCH_RULES.md already requires ("human preference remains authoritative")

### EVAL-04 The graders are tested before they are trusted
- claim: every case carries a hand-written response that must pass and one that must fail, and CI grades both, so a grader that stops catching its failure is caught without calling a model.
- source: none
- source_type: none; this record is inference
- confidence: medium
- scope: this harness
- limitations: the expected responses are written by the same hand as the graders, so they test that each grader detects the failure imagined for it, not failures nobody imagined
- inference: this is ordinary software practice (a test for the test), applied here; no source was read for it

### EVAL-05 Behaviour is read from structure, not phrasing
- claim: assertions prefer parsed fields in the reply's yaml records (performance_state, feasibility_report, session_trace) over patterns in prose, because a field is harder to satisfy by accident and harder to game with keywords.
- source: none
- source_type: none; this record is inference
- confidence: medium
- scope: this harness
- limitations: an agent can still write a well-formed record that misdescribes what it did; the session trace asks for what happened, and a human reading the reply is the check on it
- inference: all of it
