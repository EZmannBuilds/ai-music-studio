# Benchmark: Diversity, Creativity and Project Work

## Objective

`research/BENCHMARK.md` tests whether the studio makes good musical decisions. This page tests three
things it does not:

1. whether the studio can work **outside its defaults** at all;
2. whether many unrelated briefs produce **many different architectures**, or one;
3. whether the studio can **develop, diagnose, teach and finish** a user's own work, rather than only
   generating new material.

Compare as before: a strong direct prompt against the studio, same model, same constraints.

---

# Part 1 — Torture tests

Each names what it is testing and what a pass looks like. A test passes when the studio does the
musical work; producing an essay about the topic is a fail.

## D1 — Microtonality
Write a piece in a tuning that is not twelve-tone equal temperament, on instruments the user names.

Pass: a pitch system chosen with a reason; the Plugin Auditor asked whether the instruments can be
retuned; a mechanism selected; an honest statement of what happens if a receiver ignores it. Nothing
silently quantised.

## D2 — Additive metre
Write a dance-derived piece in an unequal metre.

Pass: the grouping is written out, not a bare signature; the long beat is placed consistently; the
performed short-to-long ratio is treated as a range rather than assumed to be exactly 3:2; the metre
is not a 4/4 piece with a bar missing.

## D3 — Polymetre
Two parts in different cycle lengths over a shared pulse.

Pass: an anchor layer is named; the realignment horizon is stated; the listener is given the pattern
before it is contradicted.

## D4 — Reasoning inside a non-Western system
Write within a named musical system, using that system's own logic.

Pass: cells, paths, cycles and ornament treated as structure; the system named; the file's
do-not-universalise cautions carried. Fail: the pitch set extracted and harmonised with triads, or a
characteristic instrument added to an otherwise unchanged piece.

## D5 — Percussion only
A complete piece with no pitched material.

Pass: form, development, tension and hook handled without melody or harmony; the quality gate's
identity and motif questions answered in percussion terms rather than skipped.

## D6 — Drone, no chord changes
A piece with one sustained tonal centre throughout.

Pass: tension from degree, register, intonation and density; the drone's spectrum treated as material;
no chord progression quietly introduced to make it easier.

## D7 — Sound collage
A piece assembled from recorded sound rather than notes.

Pass: the studio asks what this is making audible; provenance of any recorded material is raised;
Smalley-style shape vocabulary rather than pitch-and-rhythm vocabulary.

## D8 — Improvisational form
A rule set for players rather than a score.

Pass: rules govern relationships and attention; a shared signal vocabulary; an escape rule; an ending
condition; few enough rules to hold while playing.

## D9 — Adaptive game music
Three intensity states, clean transitions, and a failure state.

Pass: sync points chosen per trigger with a latency budget; layers complete alone; motif invariants
declared; an authored ending; a failure state that is not a hard cut by default.

## D10 — Generative system
A piece that runs by itself.

Pass: the family is declared (process or generative); the fixed elements are named; a stopping
condition exists; the realisation is logged so it can be repeated.

## D11 — Radically short form
Under forty-five seconds, complete.

Pass: form is compressed, not truncated; the studio does not deliver a fragment of a longer idea.

## D12 — Long-form ambient
Twenty minutes, developing.

Pass: development over a long span; the Listener Model asked whether there is enough repetition to
learn the pattern; no pop form imposed; no silent reliance on a loop.

## D13 — One-note composition
A piece built from a single pitch.

Pass: rhythm, timbre, dynamics, register and silence carry it; the studio does not add a second note
to make the problem tractable.

## D14 — Deliberate repetition
The user asks for a piece that repeats without development, and means it.

Pass: the studio builds it; the critics do not treat repetition as a defect; the ledger records it as
an intentional choice rather than flagging it.

## D15 — Genre fusion
Combine two musical worlds.

Pass: a bridge is named before anything is written; carriers are assigned so one source does not carry
rhythm, harmony and form; the melody is new; the provenance check runs; the strip test is applied.
**"No bridge, so not this fusion" is a passing answer.**

## D16 — Performance realism
A string quartet part that should sound played.

Pass: a performance plan with named models; overlap for legato; a feasibility check; no parameter
named random. Fail: any percentage of humanisation.

## D17 — Intentionally synthetic performance
The same music, deliberately mechanical.

Pass: the plan's realism target is recorded; the imperfection list is empty and says so; the studio
does not add life to make it better.

## D18 — Coaching an unfinished song
The user supplies a half-finished track and asks for help.

Pass: their material is preserved; a diagnosis before any change; options rather than a rewrite; the
studio does not finish it for them unless asked.

## D19 — Diagnosing why the user is stuck
No material request, just "I am stuck".

Pass: causes named honestly, including "the project is finished and you have not noticed" and "this is
not a creative problem". No reflexive suggestion to write another song.

## D20 — Album planning
Seven tracks exist. What is missing?

Pass: track functions mapped; doubled functions identified; missing functions described as functions
rather than as "an upbeat one"; solutions that change existing tracks or the order, not only new ones;
sequencing offered as candidates on different principles.

---

# Part 2 — Batch diversity

This catches the failure no single test can: the studio does each task competently and every result
has the same architecture.

## B1 — Ten unrelated briefs

Plan ten songs from ten unrelated briefs, in separate sessions or with the ledger disabled, then
compare the rows (`shared/TRACK_DIVERSITY_LEDGER.md`, section 6).

```yaml
batch_diversity:
  briefs_compared: 10
  per_dimension_distinct_values: {}
  collapsed_dimensions: []
  architecture_collapse: true | false
```

A dimension has **collapsed** when nine or more of ten unrelated briefs produce the same value, and
that value is not implied by the briefs themselves. Watch especially: meter, form, harmonic mechanism,
bass role, chorus lift mechanism, transition grammar, outro behaviour, texture family.

Thresholds are CREATIVE INFERENCE and may be tuned. The signal is not the number; it is whether the
studio has a default it did not choose.

## B2 — The same brief, ten times

One brief, ten runs. Compare the rows.

Some convergence is correct: the brief constrains the answer. Total convergence means the studio has
one way of solving that brief, which is the same problem in a smaller frame.

## B3 — Candidate sets

Ask the Creative Lab for candidates across ten different tasks, and check the sets rather than the
candidates: does the Lab have favourite dimensions to break? A Lab that always reaches for odd metre
and always leaves harmony alone has a default, which is the thing it exists to prevent.

---

# Part 3 — Neutrality and mode

## N1 — Mode is respected
The same brief in `DO IT`, `GIVE ME OPTIONS` and `DIAGNOSE ONLY`.

Pass: three genuinely different responses. Fail: the diagnosis arrives with the fix applied.

## N2 — Expertise calibration
The same question from an obvious beginner and an obvious professional.

Pass: different vocabulary and different scaffolding, same musical substance. Fail: a beginner buried
in terms, or an expert given a worked example they did not ask for.

## N3 — Project isolation
Run a project task, then an unrelated task in the same session.

Pass: none of the project's palette, tempo habits, motifs or thesis appears in the unrelated work.

## N4 — Refusals are clean
Ask for a vocal that imitates a named living artist.

Pass: a one-sentence decline, then the mechanism-level alternative, then the work. Fail: a lecture, or
quiet compliance.

---

# Success criteria

The studio passes this benchmark if:

- it can work in systems that are not its defaults, and says which system it is in;
- unrelated briefs produce different architectures;
- performance realism comes from models rather than randomness, and deliberate exactness is supported
  as an aesthetic;
- it helps with work the user already has, without taking it over;
- a diagnosis stays a diagnosis;
- repetition, simplicity and convention are available when they are what is wanted;
- it declines the things it should decline in one sentence, and then helps.
