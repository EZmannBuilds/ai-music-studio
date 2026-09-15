# Cycles and Timelines

## A cycle is not a bar

Much of the world's rhythm is organised in cycles. A cycle and a bar both repeat, both have a
length, and both group events. Treating them as the same thing loses three properties, and each
loss changes the music.

### 1. The reference point may be cycle-final, not cycle-initial

A bar begins at its strongest point. A cycle need not.

Clayton (2000, *Time in Indian Music*) describes **sam** as both the end of one cycle and the
beginning of the next, functioning as an **arrival**. Javanese colotomic structure places the
largest gong at the **end** of the cycle. In both cases the strongest event is what the cycle
moves toward, not what it departs from.

```text
bar      |> . . .  |> . . .        strong first, then decay
cycle    . . . <|  . . . <|        motion toward the marker
```

### 2. The cycle is marked externally, not inferred

A bar line is inferred by the listener from accents. A cycle is usually stated by an explicit
pattern that is present as sound.

- Indian tala is externalised through clap patterns and drum thekas, with at least three pulse
  levels.
- Arabic iqa'at are defined by a dum and tak skeleton with rests, in cycles from 3 to 48 or more
  pulses, ornamented freely over a fixed skeleton.
- Javanese colotomic structure marks nested intervals with specific gongs.
- West African ensembles state the cycle with a bell pattern.

This has a direct consequence for arrangement: **the marker is a part**, not a metrical
abstraction. If it is removed, thinned or humanised, the cycle it states weakens. See the marker
rule in `MICROTIMING_AND_GROOVE.md`.

### 3. Several valid "ones" may coexist

Locke (2009; 2010) describes a **metric matrix** in Ewe music: several simultaneously valid
hearings of the same sounding pattern, where Western notation forces a single one. Agawu (2006)
treats the same bell pattern as a time line whose entry point is contested.

The disagreement is not about who is right. It is evidence that the pattern supports more than
one valid orientation, and that different participants hold different ones at the same time. A
notation that picks one and suppresses the rest has made an analytical choice and should say so.

## The cycle object

```yaml
cycle:
  length_pulses:                     # total pulses in the cycle
  marker_pattern:                    # the sounding pattern that states the cycle
  reference_point: start | end | multiple
  hierarchy_levels: []               # nested levels, largest first
```

`reference_point: multiple` is the metric-matrix case. It is a legitimate value, not a failure
to decide, and it is written when the source system genuinely supports more than one
orientation.

`hierarchy_levels` carries the nesting: for a colotomic structure, which marker falls at which
interval; for a tala, the vibhag divisions; for a timeline, the levels the ensemble references.
At least three pulse levels is the documented case for tala.

```yaml
cycle:
  length_pulses: 16
  marker_pattern: "stated by the marker part, not inferred"
  reference_point: end
  hierarchy_levels: [16, 8, 4]
```

## Phrases resolve to, or depart from

This is the compositional consequence of the reference point, and it is where most generated
cycle music goes wrong.

```text
departing-from     material is strongest at the reference and relaxes away from it
resolving-to       material builds across the cycle and lands on the reference
```

A phrase written to depart from an initial downbeat, then dropped into a cycle whose reference
point is final, arrives with its weight in the wrong place. The cycle still repeats, so nothing
sounds broken, but the music pushes away from the moment the system points toward. The result is
flat in a way that is hard to diagnose from a piano roll.

So the cycle object's `reference_point` is consulted **before** phrases are written, not after.
Composer states which way phrases run, and says so in the plan.

## Hard rules

**MIDI Builder never silently converts a cycle to 4/4 with an initial downbeat.** A 12-pulse
timeline written as three bars of 4/4 starting on a downbeat is a different piece of music from
the timeline. If the export format cannot carry the cycle, the builder:

- chooses a metre that preserves the cycle length and grouping where one exists;
- writes `length_pulses`, `reference_point` and `marker_pattern` into a track note;
- states in its report what was lost and what was chosen;
- never renames the material after the metre it was forced into.

**The Listener Model reports alternative hearings rather than forcing one.** When a pattern
supports more than one orientation, the model lists them, says which the arrangement currently
favours and why (usually the marker part, the bass, or the loudest layer), and does not treat
the notated downbeat as the answer.

## What each specialist does with it

**Composer** fills the cycle object before writing phrases, decides resolving-to or
departing-from, and links to the relevant page in `shared/MUSICAL_SYSTEMS/` rather than
describing the tradition here.

**Performance Director** keeps the marker part exact and unhumanised, and keeps it audible. It
checks that the cycle length at the planned tempo is trackable, using the limits in
`METER_AND_PULSE.md`.

**Listener Model** reports which orientation the arrangement produces, lists the alternatives,
and flags a mismatch between the stated `reference_point` and the phrase shapes actually
written.

**MIDI Builder** preserves the cycle, carries the metadata, and reports the conversion honestly.

## Cross-links

- `shared/MUSICAL_SYSTEMS/RAGA_AND_TALA.md` for tala, sam, theka and the clap patterns
- `shared/MUSICAL_SYSTEMS/MAQAM.md` for the iqa'at and their dum and tak skeletons
- `shared/MUSICAL_SYSTEMS/GAMELAN.md` for colotomic structure and the gongs that mark it
- `shared/MUSICAL_SYSTEMS/CLAVE_AND_TIMELINES.md` for clave, bell patterns and entry points
- `POLYMETER_POLYRHYTHM_CROSSRHYTHM.md` for what happens when layers run against the cycle
- `MICROTIMING_AND_GROOVE.md` for why the marker is never humanised
