# Metric Modulation and Tempo Morphing

## The pivot mechanism

A metric modulation sets a value in the old tempo equal to a different value in the new one. The
shared value is the pivot: it sounds the same across the change, and the grid around it moves.

Carter's Cello Sonata (1948) is the prominent early use. The term "metric modulation" was coined
by a reviewer; Carter preferred "tempo modulation". Direct quotations from Carter are marked
**to verify** in `research/RHYTHM.md` and are not reproduced here.

```text
new tempo = old tempo x (old value / new value)
```

Read the ratio as a count of units across one pivot span: if 2 units of the old pulse are
respelled as 3 units of the new pulse, the new units are shorter and the tempo rises by 3/2.

## Pivot table

Worked from an old tempo of **120 BPM**. Multiply the factor by any other starting tempo to get
that case. These are arithmetic, not measurements.

```text
ratio (old:new)   factor     new tempo from 120     character
2:3               1.500      180.000                a clear lift, easily heard
3:4               1.333      160.000                moderate lift
4:5               1.250      150.000                subtle lift
5:6               1.200      144.000                very subtle; needs a clean pivot
3:5               1.667      200.000                large lift, close to a cut

and in the slowing direction

3:2               0.667       80.000
4:3               0.750       90.000
5:4               0.800       96.000
6:5               0.833      100.000
5:3               0.600       72.000
```

A small ratio such as 5:6 is not a small event. It is harder to hear, so it needs a longer and
plainer pivot, or the listener registers a slightly wrong tempo rather than a modulation.

## The pivot must be audible first

**The pivot value must be sounding for at least a bar before the switch.** If it is not, the
modulation is not heard as a modulation. It is heard as a new piece starting.

```text
before   sound the pivot value in the old tempo, at least one bar, in a part that is clearly heard
at      the switch happens on the pivot
after   the pivot value continues, now meaning something different in the new grid
```

The pivot should be in a part with a clean transient and a stable role. A pivot buried in an
inner voice, or carried by a pad with a slow attack, does not do the job. See the beat bin
discussion in `MICROTIMING_AND_GROOVE.md`: the shape of the sound determines where its beat is
felt, and a pivot whose felt centre is vague makes the whole modulation vague.

## Two implementation routes, and pick one

```text
tempo-map route       write a tempo event at the pivot; notation stays simple in the new tempo
implied-pulse route   keep the tempo and write the new pulse as tuplets; the grid stays stable
```

**Pick one route per modulation. Never both.** Mixing them produces a project where the written
durations and the tempo lane both encode the same change, so the change happens twice and
nothing lines up. This is the most common way a metric modulation fails in a DAW.

Choose the tempo-map route when the new tempo is the destination and the music stays there:
later editing, later parts and later quantisation all want the grid to mean the new tempo.

Choose the implied-pulse route when the change is brief, when the old grid must stay available
for other layers, or when the target is a notation export that should show the tuplets.

```yaml
modulation:
  at:                    # position of the pivot
  pivot_value:           # the value held constant
  ratio:                 # old:new counts across the pivot span
  old_tempo:
  new_tempo:             # computed, not guessed
  route: tempo_map | implied_pulse
  pivot_established_bars: # must be at least 1
```

## Constant pulse across changing tempi

A related but distinct practice: hold one value constant while the notated tempo and metre
change around it. Stravinsky's *Symphonies of Wind Instruments* holds a constant eighth across
tempi in a 2:3:4 relation.

This is not the same as a pivot modulation. In a pivot modulation the shared value changes
meaning and the surface tempo changes. In constant-pulse practice the pulse never changes at
all, and what changes is how it is grouped and counted. The listener's entrainment can be left
entirely intact while the notation is transformed.

The studio records which of the two is intended, because the ear-level result is different and
the Listener Model scores them differently.

## Tempo canons and convergence points

Nancarrow's tempo canons run voices at different, sometimes irrational, tempo ratios, with
**convergence points** where the voices coincide. The convergence point is the structural event;
the ratio is the means.

The obstacle is practical: **no common DAW gives a track its own tempo.** Tempo is a master
lane. So a tempo canon is emulated, and the two emulations have different costs:

```text
re-quantisation      write each voice's material at positions derived from its own tempo ratio,
                     placed on the master grid; exact, editable, but the notation is meaningless
rendered stretch     render a voice, then time-stretch it to its ratio and place it; audibly
                     correct, but the voice is now audio and the stretch has artefacts
```

For an irrational ratio, re-quantisation is an approximation by definition, and the plan should
say what resolution was used and where the error accumulates. Compute the convergence point from
the ratio and check that the emulation still lands on it after rounding.

## DAW practicalities

- Tempo is a master lane. Per-track tempo does not exist in the common hosts.
- Decimal precision of the tempo field **differs between hosts**. A tempo of 133.333... is
  stored as a rounded value, and the rounding differs, so a modulation that is exact in one
  project is a few milliseconds off per bar in another. State the intended exact ratio alongside
  the rounded tempo.
- Anything already committed to audio does not follow a tempo change unless it is stretched.
- Quantising after a modulation quantises to the new grid, which will drag pre-modulation
  material if the selection crosses the pivot.

## What each specialist does with it

**Composer** chooses the ratio for a musical reason, computes the new tempo rather than guessing
it, and names the pivot value and the part that carries it.

**Performance Director** ensures the pivot is established for at least a bar in an audible part
with a clean transient, and checks that the post-modulation subdivisions stay inside the
perceptual limits in `METER_AND_PULSE.md`.

**Listener Model** asks whether the pivot was heard before the switch, and reports the likely
hearing if it was not: a new section, a mistake, or a tempo drift.

**MIDI Builder** implements exactly one route, states which, writes the exact ratio into a track
note next to the rounded tempo value, and never leaves both a tempo event and compensating
tuplets in place.
