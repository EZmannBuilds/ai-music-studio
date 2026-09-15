# Displacement and Metric Dissonance

## Displacement needs something to be displaced from

Displacement is the same pattern shifted against a reference. Krebs (1999, *Fantasy Pieces*)
calls this **displacement dissonance**: same cardinality, shifted phase, as opposed to grouping
dissonance where the cardinalities differ. Both are in `POLYMETER_POLYRHYTHM_CROSSRHYTHM.md`.

The device only exists in relation to a reference. Krebs' dissonance, Reich's process and the
soloist lag measured by Friberg & Sundström all require an audible one. Without it, the listener
re-entrains to the shifted pattern, the shift becomes the metre, and nothing has been displaced.

This is why the operator carries an anchor and a resolution point rather than just an amount.

## The operator

```yaml
displacement:
  motif:                  # what is being shifted
  shift:
    amount:               # signed; negative is early
    unit:                 # pulses, subdivisions, percent of beat, or ms
  anchor_layer:           # required; what it is shifted against
  schedule: static | stepwise | continuous
  resolve_at:             # where it returns, or explicitly "never"
```

`anchor_layer` is required. A displacement with no anchor is rejected, not executed with a
default.

`resolve_at` may be "never", but that has to be written. An unresolved displacement is a
decision about the whole section, and it should be one someone made.

`unit` decides which of the two kinds of displacement this is.

## Grid level versus microtiming level

These are different devices that share a name, and confusing them produces work that is neither.

```text
grid level         shift by a whole subdivision or more: an eighth, a sixteenth, a pulse
                   the pattern lands on different grid positions
                   the listener hears a changed relationship to the metre
                   unit: pulses or subdivisions

microtiming level  shift by a fraction of a subdivision, tens of milliseconds
                   the pattern lands in the same grid positions, placed differently within them
                   the listener hears a changed feel, not a changed position
                   unit: percent of beat or ms
```

A grid-level displacement is structural and is heard as an event. A microtiming-level
displacement is a feel and is heard as a quality. Sizing one like the other fails in both
directions: a 30 ms "displacement" of a riff is not a displacement, it is a slightly late riff;
a full-sixteenth "laid-back" horn section is not laid back, it is playing a different figure.

Microtiming-level displacement uses the templates and the ceiling in
`MICROTIMING_AND_GROOVE.md`, including the beat bin: a shift small enough to stay inside the bin
may not read as a shift at all, depending on the transient.

## Establish the reference first

**The undisplaced motif must be heard before the displacement.** The working figure is roughly
**one to two cycles** of the undisplaced form, in a clearly audible part, before the shift
begins.

```text
fewer than one cycle     the shifted form is simply what the motif is; nothing was displaced
one to two cycles        the reference is established; the shift reads as a shift
more than that           safe, but the passage may become predictable before the device arrives
```

The Listener Model applies this directly: it does not score a displacement as intelligible
unless the undisplaced motif was established first. That check is on the audible arrangement,
not on the plan, so a motif stated in a part nobody can hear does not count.

## Documented cases

- **Discrete shift through all rotations.** Reich's *Clapping Music*: one voice shifts by one
  eighth per stage through twelve rotations, arriving back at unison. The opening unison is the
  reference, and the return to unison is the resolution. This is the clearest model for
  `schedule: stepwise` with an explicit `resolve_at`.
- **Continuous phase.** Reich's *Piano Phase*: one voice accelerates slightly so the shift is
  continuous rather than stepwise, passing through alignments rather than stopping at them.
- **Systematic soloist lag.** Friberg & Sundström measured a soloist placed systematically
  against the section. This is the microtiming-level case: a constant offset per part per
  section, not a wandering one, which is why `shared/HUMAN_PERFORMANCE_SCHEMA.md` models it as
  `section_offset`.
- **Ambiguity of pulse placement in neo-soul.** Danielsen (2006; ed. 2010) gives the scholarly
  account of the displaced pulse associated with D'Angelo and the Soulquarians, where the
  placement of the pulse is genuinely ambiguous rather than merely late. The beat bin is the
  tool for this: the span is wide, several placements are live at once, and the ambiguity is the
  point.
- **Odd groupings over a steady anchor.** Pieslak (2007) on Meshuggah, where the anchor cymbal
  is what keeps the groupings audible as displacement. See
  `POLYMETER_POLYRHYTHM_CROSSRHYTHM.md`.

## Interaction with listener expectation

Displacement is a tension device and it spends the same currency as every other one: an
established pattern.

```text
establish     the listener projects the motif's position
displace      the projection is contradicted; tension
sustain       the listener may re-entrain to the displaced form, and the tension decays
resolve       the projection is confirmed again; release
```

The third line is the one that gets missed. A displacement held long enough stops being a
displacement, because the listener adopts it. This is what the anchor prevents: as long as the
anchor keeps stating the original position, re-entrainment is blocked and the tension holds.
When the anchor drops out, the tension decays within a cycle or two whether or not the plan
intended it.

`shared/QUALITY_GATE.md` asks whether the track establishes patterns clearly enough for
deviations to matter. Displacement is the case that question was written for.

## Implementation

```text
static        one constant offset applied to the motif's notes for the passage
stepwise      note-list rotation: rewrite the motif's positions by the shift amount at each stage
continuous    per-track offset automated over time, or a rendered voice time-stretched
```

**Stepwise displacement is note-list rotation**, not a delay. Rotating the written positions
keeps the material editable, keeps it on a grid that can be quantised and inspected, and keeps
the notation honest about where the notes are.

**Continuous displacement** is a per-track delay automated over the passage, or a rendered part
stretched and placed. The rendered route is the same trade as in
`METRIC_MODULATION_AND_TEMPO_MORPHING.md`: audibly correct, no longer editable as MIDI.

**Never implement displacement as random jitter.** Jitter is not a small displacement. It has no
direction, no anchor relationship and no resolution, so it produces none of the effect and costs
the tightness the anchor relationship depends on. If the plan asks for a shift, apply a shift.

## What each specialist does with it

**Composer** chooses the amount and unit, names the anchor, sets the schedule and the
resolution, and makes sure the undisplaced motif is stated first in a part that will be heard.

**Performance Director** decides grid level or microtiming level, keeps microtiming-level shifts
inside the natural magnitudes in `MICROTIMING_AND_GROOVE.md`, and keeps the anchor exact.

**Listener Model** checks that the reference was established, reports whether re-entrainment is
likely by the end of the passage, and lists alternative hearings rather than forcing one.

**MIDI Builder** implements stepwise shifts as rewritten note positions, continuous shifts as an
automated track offset or a rendered stretch, records the offset and unit in a track note, and
never substitutes randomisation for a specified shift.
