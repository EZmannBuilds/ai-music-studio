# Rhythm Systems

## What this folder is for

This folder holds the *mechanisms* of rhythm: how a metre is represented, how layers are set
against each other, how a cycle differs from a bar, how a tempo pivots, and how timing is
shifted on purpose. Each file describes a mechanism as an object a specialist can build, inspect
and argue with.

The source is `research/RHYTHM.md`, with the microtiming evidence in
`research/PERFORMANCE_AND_EXPRESSION.md`. Those pages carry the citations and the cautions.
Nothing here overrides them.

## Division of labour with MUSICAL_SYSTEMS

Mechanics live here. Cultural context lives in `shared/MUSICAL_SYSTEMS/`.

```text
here                          there
the 12-pulse cycle object     what an Ewe bell pattern is, and whose it is
short:long ratio ranges       the Balkan and Turkish dances that use them
E(k,n) and rotation           the tresillo and cinquillo as named patterns
cycle reference points        tala, iqa'at and colotomic structure
```

If a question is "how do I encode this", it is answered here. If it is "what is this, where is
it from, and what does it mean to the people who play it", it is answered there. When both
matter, this folder links out rather than summarising.

## The eight mechanism files

| File | What it gives you |
|---|---|
| `METER_AND_PULSE.md` | Metre as entrainment, its limits, and the meter object |
| `ADDITIVE_AND_NONISOCHRONOUS_METER.md` | Metres from 2s and 3s, performed ratios, tuplet limits |
| `POLYMETER_POLYRHYTHM_CROSSRHYTHM.md` | Definitions, the layer record, the anchor requirement |
| `EUCLIDEAN_AND_GENERATED_RHYTHM.md` | E(k,n), rotation, and the naming rule |
| `METRIC_MODULATION_AND_TEMPO_MORPHING.md` | Pivot arithmetic, the two routes, DAW limits |
| `CYCLES_AND_TIMELINES.md` | How a cycle differs from a bar, and the cycle object |
| `MICROTIMING_AND_GROOVE.md` | Microtiming as a template, and the evidence against |
| `DISPLACEMENT_AND_METRIC_DISSONANCE.md` | Displacement as an operator with an anchor |

## Who reads them

- **Composer** chooses the system. It picks a metre, a cycle, a layer scheme or a modulation and
  writes it into the composition brief before pitches exist.
- **Performance Director** realises it. It checks layers against the perceptual limits, selects
  a microtiming template, and decides which parts are humanised and which are not.
- **Listener Model** judges intelligibility. It asks whether the reference was established
  before it was contradicted, and reports alternative hearings rather than forcing one.
- **MIDI Builder** encodes it. It maps cycles, unequal subdivisions and displacements onto a
  grid without silently normalising them, and states what it did.

Each file ends with a short section naming what these four do with it.

## Standing rules

These hold across every file in this folder.

**Write the grouping, not a bare odd signature.** `9/8` alone does not say whether it is 2+2+2+3
or 3+3+3 or 2+3+2+2. Those are different pieces of music. Always write `9/8 = 2+2+2+3`.

**Name the anchor layer for any layered conflict.** Polyrhythm, polymeter, cross-rhythm, hemiola
and displacement are all relationships against a reference. Without a named anchor a displaced
pattern is simply heard in a different metre, and the intended tension does not exist.

**Never label a generated pattern with a tradition's name** unless the pattern, its rotation and
its tempo range match a documented case, and then say which case. A Euclidean generator recovers
a shape. It does not recover a rotation, an accent hierarchy, a dance or a name.

**Marker instruments are never humanised.** Bell, gong, clap and clave state the cycle. They are
the reference everything else is heard against, so they are placed exactly. Microtiming
templates apply to the parts that play against them.

**All figures here are corpus ranges.** Every number came from a particular repertoire at a
particular tempo, measured by a named study. None of them is a constant, and none of them
transfers to a repertoire that was not measured. Where the research marked something *to
verify*, this folder keeps the mark.

## Cross-links

Cultural context, in `shared/MUSICAL_SYSTEMS/`: `ADDITIVE_METERS_BALKAN_TURKISH.md`,
`CLAVE_AND_TIMELINES.md`, `WEST_AFRICAN_POLYRHYTHM.md`, `RAGA_AND_TALA.md`, `MAQAM.md`,
`GAMELAN.md`, `BLUES_SYSTEM.md`.

Adjacent shared pages: `shared/QUALITY_GATE.md` (the groove and expectation checks),
`shared/RESEARCH_RULES.md` (why an empirical average is not a law),
`shared/TRACK_STATE_SCHEMA.md` (where `musical.meter`, `musical.rhythmic_cells` and
`musical.groove_notes` are carried between specialists).
