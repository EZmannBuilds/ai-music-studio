# Generalization Rules

This skill family is intended for any user, genre, workflow, DAW, instrument set, or artistic
goal.

It must not silently inherit preferences from a previous user, project, genre, reference set,
or production workflow.

## Core rule

Every session begins from the current user's request and available evidence.

Do not assume:
- preferred genre;
- preferred DAW;
- preferred synth;
- preferred loudness;
- preferred arrangement style;
- preferred theory system;
- preferred amount of experimentation;
- preferred song length;
- preferred vocal style;
- preferred production aesthetic;
- preferred reference artists;
- preferred audience.

If a preference is not provided, keep the recommendation flexible or present reasonable
options.

## Separate universal mechanism from user-specific preference

Example:

```text
Universal mechanism:
A chorus often benefits from contrast with the preceding section.

User-specific implementation:
Make it wider, louder, darker, more acoustic, more distorted, more minimal, etc.
```

Do not turn one user's favorite implementation into the default.

## Tool neutrality

The musical reasoning layer should not depend on one DAW, analyzer, synth, or plugin.

Use generic descriptions first:

```text
wavetable synth
subtractive synth
sampler
audio analyzer
DAW
compressor
dynamic EQ
transient shaper
```

Then translate to a named tool only when:
- the user specifies it;
- the tool is available;
- a dedicated adapter is active.

## Genre neutrality

Do not assume commercial pop form or production unless requested.

Support:
- pop;
- rock;
- hip-hop;
- R&B;
- soul;
- jazz;
- classical;
- electronic;
- ambient;
- metal;
- folk;
- game music;
- film scoring;
- experimental music;
- and other styles.

When genre conventions matter, infer them from the user's request or references rather than
from stored personal preferences.

## Reference neutrality

References are local to the current task.

Do not carry traits from a previous reference into a new project unless the user asks to. After a
task ends, its reference's tempo, genre, production density, harmonic style and sound palette are not
defaults for anything else.

## Evaluation neutrality

Evaluate against:

```text
the current artistic goal
+
the current genre/context
+
the current listener/use case
```

not against a fixed personal aesthetic.


## System neutrality

No musical system is the default.

Twelve-tone equal temperament, functional harmony, the bar line and verse/chorus form are one set of
choices among many, and they are the set most likely to be assumed. When the brief does not name a
system, say which one you are working in rather than leaving it unstated
(`shared/MUSICAL_SYSTEMS/INDEX.md`).

This cuts both ways. A user who wants a pop song in C major is not to be talked into a maqam, and a
tradition is not a flavour to be added to an otherwise unchanged piece.

## Realism neutrality

Organic performance is not always the goal.

A grid-exact part can be the point of the music. Do not treat exactness as a defect to repair, and do
not treat looseness as quality. The brief sets the realism target and the studio records which it was
(`shared/HUMAN_PERFORMANCE_SCHEMA.md`).

## Project neutrality

An album is one kind of project. So are a single song, an EP, a score, a cue list, a live set, a
generative system and an unfinished folder of ideas.

Do not assume a body of work wants an arc, a disruption, an opener and a closer. Ask what the project
is (`shared/PROJECT_STATE_SCHEMA.md`).
