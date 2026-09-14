# Research: Reference Translation and DAW-Ready MIDI

## Motivation

Two needs come up constantly:

1. users often supply a streaming song URL and expect the skill to use it as a reference;
2. users often need an actual MIDI artifact rather than textual composition advice.

This page covers both.

## 1. Evidence levels for references

A streaming URL may expose:
- identity;
- release data;
- BPM/key metadata;
- third-party descriptions;

without exposing analyzable audio.

The skill must separate:
- verified metadata;
- direct observations;
- inference;
- community description.

This prevents hallucinated claims such as "I hear a distorted bass entering at 0:17" when the
system never accessed the recording.

## 2. Reference translation

The creative objective is to convert a source into abstract dimensions:

```text
energy
density
hook salience
digital/acoustic balance
emotional contrast
form compactness
rhythmic intensity
```

Then instantiate those dimensions through new material.

## 3. Similarity distance

When one source dominates the brief, build deliberate differences:

```text
different tonal center
different melody
different harmony
different drum grammar
different section proportions
different sound-design signatures
```

This makes the reference a design coordinate rather than a tracing template.

## 4. MIDI as a production artifact

MIDI export is not only note serialization.

A DAW-ready MIDI should include:
- track names;
- tempo;
- time signature;
- key/pitch context;
- form markers;
- separate musical roles;
- velocities;
- control messages;
- pitch bend where useful;
- import notes.

## 5. Track-count validation

Requests such as "more than 10 tracks" are testable constraints.

The generator should validate:
- requested track count;
- active events on each track;
- duration;
- file readability;

programmatically before delivery.

## 6. Guide vs rendered sound

MIDI cannot fully represent:
- vocal formants;
- distortion texture;
- granular processing;
- detailed audio transitions;
- human articulation.

Use guide tracks for those intentions and state clearly that the DAW user must replace them
with audio/sampler/synth processing.

## 7. Where MIDI Builder sits

MIDI Builder turns the accepted musical plan into a DAW-ready file. The core flow:

```text
Reference Analyst
→ Music Director
→ Composer
→ Arranger
→ Producer
→ MIDI Builder
→ DAW
→ rendered-audio feedback
```


# Implementation lessons

Two failure modes are common in generated multitrack MIDI.

## 1. Pitched parts on the percussion channel

General MIDI reserves channel 10 for percussion. A bass or any pitched track placed there is
played as a drum kit by a GM-compatible receiver.

Treat channel allocation as a validated artifact constraint, not a low-level implementation
detail (`midi-builder/SKILL.md`).

## 2. MIDI balance vs real mix

A 20+ track MIDI may sound unbalanced under default General MIDI instruments even when
the musical roles are correct.

The final mix depends on the actual:
- samples;
- synth patches;
- saturation;
- effects;
- articulation;
- vocals;
- processing.

Therefore the studio separates:

```text
rough MIDI balance
from
rendered audio mix
```

Analyzer-assisted feedback (including WavRead when available) is optional and must be
reference-conditioned to avoid turning one generic tonal/loudness target into a universal
mix rule.
