# Polymeter, Polyrhythm and Cross-Rhythm

## Working definitions

These four words are used loosely in most sources. The studio adopts one set of definitions and
uses them consistently, so that a plan means the same thing to every specialist.

```text
polyrhythm     different subdivisions of a shared cycle; they land together each cycle
polymeter      different cycle lengths over a shared pulse; they realign at the common multiple
cross-rhythm   a polyrhythm that is the structural basis of the music, not an ornament
hemiola        a temporary 3:2 regrouping inside one metre
displacement   the same pattern shifted against an anchor
```

Two distinctions carry most of the weight.

**Polyrhythm versus polymeter.** In polyrhythm the cycle is shared and the subdivision differs:
3 against 2 inside one bar, coinciding at every barline. In polymeter the pulse is shared and
the cycle length differs: a 4-pulse pattern against a 3-pulse pattern, coinciding only every 12
pulses. One is a texture inside a cycle; the other is a long-range structure.

**Polyrhythm versus cross-rhythm.** Cross-rhythm is not a stronger polyrhythm. It is a
polyrhythm that the piece is built on, present from the start and not resolved away. The
reference literature defines polyrhythm as simultaneous rhythms not heard as derived from one
another, and cross-rhythm as polyrhythm functioning as the basis of a whole piece.

**Hemiola and sesquialtera** both name a 3:2 relation. Some theorists reserve hemiola for a
momentary regrouping and sesquialtera for a sustained simultaneity. The studio uses hemiola for
the temporary case and says "3:2 polyrhythm" for the sustained one, and notes that the usage is
not universal.

## Grouping dissonance and displacement dissonance

Krebs (1999, *Fantasy Pieces*) gives a vocabulary that makes these describable as
*relationships* rather than as errors.

```text
grouping dissonance       incongruent cardinalities, such as 3 against 2
displacement dissonance   the same cardinality, shifted against the reference
consonance                layers agreeing in cardinality and phase
```

The value of this vocabulary is that it names the state the music is in. A generator that
produces "3 against 2" and a quantiser that produces "3 against 2" look identical in a piano
roll. Labelling the passage as a grouping dissonance with a named anchor says it was intended,
says what it is against, and gives the Listener Model something to evaluate. See
`DISPLACEMENT_AND_METRIC_DISSONANCE.md` for the displacement case in full.

## The layer record

Every layer in a conflicted passage gets a record.

```yaml
layer:
  pulse_ref:              # the shared fast pulse, in pulses per cycle or in ms
  cycle_len:              # this layer's cycle, in shared pulses
  phase_offset:           # this layer's start, in shared pulses, against the anchor
  subdivision:            # how this layer divides its own cycle
```

`pulse_ref` must be identical across the layers of one passage. If two layers do not share a
pulse, they are not in polymeter, they are in two tempi, and that belongs in
`METRIC_MODULATION_AND_TEMPO_MORPHING.md`.

## The realignment horizon

For polymeter, compute it and state it in the plan.

```text
horizon_pulses = least common multiple of the cycle_len values
horizon_bars   = horizon_pulses / pulses_per_bar_of_the_anchor
horizon_seconds = horizon_pulses * pulse_duration_ms / 1000
```

```text
cycles 4 and 3       LCM 12 pulses
cycles 5 and 4       LCM 20 pulses
cycles 7 and 8       LCM 56 pulses
cycles 5 and 7       LCM 35 pulses
```

The horizon is a compositional fact, not a footnote. A 56-pulse realignment at a slow tempo may
outlast the section it is in, so the layers never visibly resolve and the passage reads as noise
rather than as structure. Either shorten a cycle, extend the section, or accept the
non-resolution deliberately and say so.

## The anchor layer requirement

**Every layered passage names an anchor layer.** Without one, a displaced or conflicting pattern
is not heard as conflicting. It is heard as the metre, and the intended tension does not exist.

The anchor is the layer that states the cycle plainly: the bell, the clave, the hats, the bass,
the gong. It is placed exactly, on its own documented feel where it has one, and is given no
expressive deviation (see `MICROTIMING_AND_GROOVE.md`).

```yaml
layered_passage:
  anchor_layer:           # required; names one layer
  layers: []              # each a layer record
  horizon_pulses:
  resolves_within_section: true | false
```

Without an anchor the failure is specific and predictable: the listener re-entrains to whichever
layer is loudest or lowest, the "conflict" becomes the new metre, and any later resolution
arrives as an unexplained lurch rather than as an arrival.

## Documented cases

- **Odd groupings over a steady anchor.** Pieslak (2007, *Music Theory Spectrum*) analyses
  Meshuggah, where odd-length riff groupings run against a steady anchor kept by the cymbals.
  The anchor is what makes the groupings audible as displacement rather than as a change of
  metre.
- **Phase processes.** Reich's *Clapping Music* shifts one voice by one eighth per stage through
  twelve rotations back to unison, a discrete process. *Piano Phase* shifts continuously. Both
  need the unison opening as the reference.
- **Hemiola plus additive pulsation.** Ligeti's Etudes combine a Romantic hemiola practice with
  an additive-pulsation principle he encountered through Arom's recordings of Central African
  music. This is a documented encounter with recordings and a compositional response to them, not a
  transplant of a tradition, and it should be described that way. **The pack has no file on the
  Central African traditions Arom recorded**; the Ewe and Mande files cover different peoples and
  practices and must not be used to stand in for them.

## Worked grids

```text
3:2 over a shared cycle of 6 units          polyrhythm: they land together each cycle

unit     1  2  3  4  5  6 | 1
three    x  .  x  .  x  . | x
two      x  .  .  x  .  . | x
both     *                | *


4:3 over a shared cycle of 12 units         polyrhythm: coincidence only at the cycle

unit     1  2  3  4  5  6  7  8  9 10 11 12 | 1
four     x  .  .  x  .  .  x  .  .  x  .  . | x
three    x  .  .  .  x  .  .  .  x  .  .  . | x
both     *                                  | *


polymeter, cycles 4 and 3 over a shared pulse       realignment horizon 12 pulses

pulse    1  2  3  4  5  6  7  8  9 10 11 12 | 1
cyc 4    A  .  .  .  A  .  .  .  A  .  .  . | A
cyc 3    B  .  .  B  .  .  B  .  .  B  .  . | B
both     *                                  | *
```

In the 4:3 grid, "four" and "three" divide the same 12-unit span. In the polymeter grid, both
layers step on the same pulse but their cycles differ in length, so the downbeats walk past each
other and meet again at pulse 13.

## What each specialist does with it

**Composer** chooses the relationship, names the anchor, and computes the horizon before writing
parts. It says which of the four words it means.

**Performance Director** keeps the anchor exact and applies templates only to the non-anchor
layers. It checks each layer's fastest subdivision against the limits in `METER_AND_PULSE.md`.

**Listener Model** reports whether the anchor was established before the conflict began, and
whether the horizon falls inside the section. It reports alternative hearings rather than
forcing one.

**MIDI Builder** encodes every layer against the shared pulse with `phase_offset` applied as
note positions, not as a track delay, unless the plan asks for a delay explicitly.
