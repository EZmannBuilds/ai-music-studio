# Benchmark: General-Purpose Evaluation

## Objective

Test whether the AI Music Studio improves musical reasoning across varied users and tasks
without depending on one person's favorite genres, tools, references, or workflow.

Compare:

```text
A. strong direct prompt
B. the AI Music Studio
```

Keep the same model and constraints.

---

# Human Questions

1. Which version better satisfies the stated brief?
2. Which has the stronger musical identity?
3. Which makes better musical decisions?
4. Which is more coherent?
5. Which is less generic?
6. Which uses repetition/development better?
7. Which handles tension/release better?
8. Which preserves the requested aesthetic better?
9. Which would you choose to continue developing?
10. Which is better overall?

---

# Test 1 — Simple Melody

Create an 8-bar melody over a static harmony. The melody should be memorable without relying
on production effects.

Tests:
- motif;
- contour;
- repetition;
- development.

---

# Test 2 — Functional Harmony

Write an 8-bar functional progression that creates a clear departure and satisfying return.

Tests:
- harmonic direction;
- voice leading;
- tension/release.

---

# Test 3 — Nonfunctional Harmony

Create an 8-bar progression where color and voice leading matter more than dominant-tonic
function.

Tests:
- whether the system can avoid forcing functional analysis;
- coherence without conventional cadence.

---

# Test 4 — Groove

Design three groove options with different rhythmic complexity for the same tempo.

Tests:
- pulse clarity;
- syncopation;
- kick/bass relationship;
- tradeoff explanation.

---

# Test 5 — Acoustic Arrangement

Arrange a small acoustic ensemble using limited instrumentation.

Tests:
- register;
- role assignment;
- restraint;
- dynamic contrast.

---

# Test 6 — Electronic Arrangement

Build a section plan for an electronic track whose energy should increase without simply
adding more layers.

Tests:
- contrast;
- automation;
- register;
- rhythmic change;
- timbre change.

---

# Test 7 — Orchestral / Cinematic Cue

Create a 90-second cue plan for a dramatic scene with a clear emotional arc.

Tests:
- motif;
- orchestration;
- long-range tension;
- pacing.

---

# Test 8 — Game Music

Create a loopable cue with three intensity states that can transition cleanly.

Tests:
- modularity;
- motif preservation;
- transition design.

---

# Test 9 — Ambient

Create a five-minute ambient structure that develops slowly without relying on verse/chorus
form.

Tests:
- form flexibility;
- density;
- timbral development;
- avoidance of pop defaults.

---

# Test 10 — Rock / Band Arrangement

Given guitar, bass, drums, and lead vocal, create a section plan that avoids all instruments
occupying the same role.

Tests:
- role allocation;
- register;
- energy;
- dynamics.

---

# Test 11 — Jazz-Oriented Harmony

Design harmonic movement where extensions and voice leading are important, but do not make
complexity the objective by itself.

Tests:
- theory quality;
- voicing logic;
- musical usefulness.

---

# Test 12 — Minimal Music

Create a compelling idea using very little harmonic change.

Tests:
- whether the skill can preserve simplicity;
- development through rhythm/timbre/register.

---

# Test 13 — Raw Production Aesthetic

Produce a concept that intentionally sounds rough and imperfect.

Tests:
- whether Producer/Mix Engineer preserve the aesthetic rather than polishing it away.

---

# Test 14 — Clean Production Aesthetic

Create a precise, controlled production concept.

Tests:
- whether the same skill can move in the opposite direction when asked.

---

# Test 15 — Reference Transfer

Analyze two supplied references and extract transferable principles without copying identifiable
melody, lyrics, progression, or signature sound.

Tests:
- abstraction;
- originality;
- reference locality.

---

# Test 16 — Analyzer Input

Given a structured audio-analysis report from any tool, diagnose composition, arrangement,
production, and mix implications.

Tests:
- analyzer independence;
- evidence handling;
- correct specialist routing.

---

# Test 17 — DAW Independence

Ask for the same production plan without naming a DAW.

Success:
Generic production instructions.

Then name a DAW.

Success:
Translate the same intent into tool-specific steps without changing the music concept.

---

# Test 18 — Preference Change

Prompt A:
"Make this restrained and minimal."

Prompt B:
"Make this maximal and chaotic."

Success:
The skill adapts completely rather than preserving one preferred aesthetic.

---

# Test 19 — Structure Change

Prompt A:
"Use a conventional verse/chorus song form."

Prompt B:
"Avoid verse/chorus and make it through-composed."

Success:
The skill handles both without treating either as inherently superior.

---

# Test 20 — Critic Neutrality

Give a deliberately repetitive piece.

Ask:
"Is the repetition a problem?"

Success:
The critic evaluates repetition relative to the stated goal instead of automatically condemning it.

---

# Success Criteria

The studio succeeds if:

- it adapts strongly to contradictory briefs;
- it does not carry preferences between unrelated tasks;
- tool choice does not alter core musical reasoning;
- critics distinguish taste from defects;
- references remain local to the current project;
- it beats a strong direct prompt across several very different musical tasks.
