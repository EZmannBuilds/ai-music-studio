# Research: Generalization, User Neutrality and Transfer Across Workflows

## Purpose

A reusable music skill should not become optimized around the preferences, tools, genres and
workflow of any one user.

The studio is a general-purpose music intelligence architecture that adapts to each user. What
belongs to one user lives in that user's profile (`shared/USER_PROFILE_SCHEMA.md`), not in the
skills.

---

# 1. Personalization vs Generalization

Personalization is valuable when the current user explicitly wants it.

It becomes a problem when a reusable skill silently assumes:

- a favorite genre;
- a favorite DAW;
- a favorite synth;
- a preferred production style;
- preferred song length;
- preferred loudness;
- preferred harmony;
- preferred amount of experimentation.

The studio separates:

```text
CORE MUSICAL REASONING
from
SESSION-SPECIFIC PREFERENCES
```

The core should remain reusable.

---

# 2. Tool Independence

Specific tools, such as an analyzer, a synth or a DAW, can be supported, but the skills must not
depend on any one of them.

The architecture is:

```text
musical intention
→ generic musical/production representation
→ optional tool adapter
```

Example:

```text
Composer:
write a counterline.

Producer:
define the sound behavior.

DAW adapter:
enter MIDI / configure device / automate parameters.
```

The creative reasoning remains portable.

---

# 3. Analyzer Independence

An analyzer is optional. WavRead is the recommended one, and any structured source can feed the
Reference Analyst:

- WavRead;
- stems;
- DAW analysis;
- spectrum/loudness tools;
- manual notes;
- another MIR tool.

The core skill records:

```text
measurement
source
confidence
limitation
```

and translates findings into music decisions.

---

# 4. Genre Neutrality

The form and production logic are explicitly open.

The skill should be able to reason about:

- song-based popular music;
- instrumental composition;
- electronic music;
- orchestral/cinematic work;
- game music;
- ambient;
- jazz;
- rock/metal;
- acoustic music;
- experimental work;
- loop-based production.

Genre-specific modules can be added.

They should not become global defaults.

---

# 5. Theory Neutrality

The Composer does not assume one harmonic language unless the current task implies it.

Possible composition frameworks include:

- functional harmony;
- modal harmony;
- riff-centered writing;
- nonfunctional harmony;
- pedal/drone organization;
- chromatic writing;
- atonal organization;
- loop-based pitch systems;
- other systems.

The architecture asks:

```text
What musical system is useful for this piece?
```

rather than:

```text
How do I force this piece into my default theory system?
```

---

# 6. Mix Neutrality

A general mix skill should not assume every record wants:

- maximal clarity;
- modern brightness;
- maximum width;
- commercial loudness;
- vocal-forward hierarchy;
- pristine dynamics.

Mix evaluation is conditioned on:

```text
style
playback context
aesthetic
reference
foreground priority
dynamic-range target
```

This protects intentional roughness and unusual balance.

---

# 7. Listener Neutrality

The Listener Model uses the research on:

- expectation;
- uncertainty;
- surprise;
- groove;
- memorability;
- salience;
- auditory scene analysis.

It does not assume a particular user's desired outcome.

The listener model must first determine:

```text
Who is the target listener?
What is the use case?
What is the genre context?
```

When unknown, it reports possibilities rather than certainty.

---

# 8. Critic Neutrality

A critic must distinguish:

```text
DEFECT
Something conflicts with the stated objective.

TRADEOFF
Improving one property may reduce another.

PREFERENCE
A taste judgment.

INTENTIONAL CHOICE
A deliberate irregularity.

UNCERTAIN
Not enough evidence.
```

This prevents a reusable skill from silently turning one person's taste into universal rules.

---

# 9. Benchmark Neutrality

The studio's benchmark (`research/BENCHMARK.md`) is general-purpose. It tests:

- melody;
- harmony;
- rhythm;
- groove;
- form;
- orchestration;
- production;
- mixing;
- sound design;
- game/cinematic use;
- acoustic use;
- electronic use;
- reference transfer;
- user-specific goal adaptation.

The purpose is to test adaptability, not conformity to one style.

---

# 10. Architecture

```text
Music Director
│
├── Composer
├── Arranger
├── Producer
├── Lyric Generator
├── Mix Engineer
├── Reference Analyst
├── Music Critics
├── Listener Model
├── MIDI Builder
├── Plugin Auditor
└── Music Research

OPTIONAL ADAPTERS
├── DAW adapters
├── synth/plugin adapters
└── analysis-tool adapters
```

The creative layer is generic.
Adapters handle software-specific execution.

---

# 11. Core Rule

> Never confuse "this worked for the last project" with "this is how music should work."

Every important recommendation must be grounded in the current brief, current evidence,
current reference material, or a clearly stated general principle.
