# Meter and Pulse

## Metre is entrainment, not notation

London (*Hearing in Time*, 2004; 2nd ed. 2012) treats metre as an entrainment behaviour: a
listener projects a periodicity and hears events against it. A time signature is a notation of
that behaviour, not the behaviour itself. Two consequences follow, and both matter for how the
studio builds rhythm.

First, metre is constrained by perception. A periodicity that is too fast or too slow cannot be
entrained to, so it cannot be a metrical level, however cleanly it divides on paper.

Second, metre does not require equal spacing. London holds that **non-isochronous metres are
well formed**, not deviations from an isochronous ideal.

## Perceptual limits

These are rules of thumb from Polak & London (2014, *MTO* 20(1)) and Polak & London (2022) on
Malian drumming. They are ranges from studied repertoires, not constants.

```text
fastest metrical subdivision   around 100 ms, better held as roughly 80-120 ms
fastest useful beat            around 250 ms
slowest useful beat            around 1.5 s
whole-measure upper limit      to verify (London's figure was not confirmed at source)
```

The whole-measure limit is left marked. Do not quote a number for it. If a plan needs one, say
that the limit is unverified and make the decision by ear.

### What happens at the fast limit

The documented behaviour is important and counterintuitive: as tempo rises, an ensemble **drops
the fastest layer rather than compressing it**. The subdivision does not get squeezed below the
floor. It stops being played, and the layer above it carries the metre.

A generator that keeps sixteenths present as tempo climbs is doing something players do not do.
The Performance Director checks the fastest active layer against the tempo and warns before the
layer crosses the floor, then thins that layer rather than scaling it.

```text
tempo 100 BPM   sixteenth = 150 ms    inside the range
tempo 160 BPM   sixteenth =  94 ms    at the floor, thinning warranted
tempo 200 BPM   sixteenth =  75 ms    below the floor, drop the layer
```

Those milliseconds are arithmetic from the BPM, not measurements. The floor they are compared
against is the corpus range above.

## The meter object

```yaml
meter:
  cycle_length_pulses:      # total fast pulses in one measure or cycle
  beat_pattern: []          # e.g. [2, 2, 2, 3] for 9/8 as 2+2+2+3
  subdivision_pattern: []   # isochronous, or a long/short pattern
  tactus_ms:                # the beat the listener is expected to entrain to
```

`beat_pattern` is required even when the metre is even. `[2,2,2,2]` and `[4,4]` describe
different hearings of eight pulses, and writing one of them down forces the choice to be made
deliberately.

`tactus_ms` is the level a listener taps. It should sit inside the 250 ms to 1.5 s range. If it
does not, the metre as written is not the metre that will be heard, and the plan should say
which level is actually the tactus.

`subdivision_pattern` carries unequal subdivision directly rather than through triplet notation.
See `ADDITIVE_AND_NONISOCHRONOUS_METER.md` for how the ratios are written and
`MICROTIMING_AND_GROOVE.md` for the measured ratio ranges.

## Non-isochronous metre is not looser

Polak, Jacoby & London (2016, *Frontiers in Neuroscience*) found that non-isochronous
subdivision supports ensemble entrainment **as precisely and stably as** isochronous
subdivision. Unequal is not approximate. A 60:40 subdivision held across an ensemble is a tight,
learned, reproducible target, and the tightness measures like any other well-drilled part.

This forbids a common shortcut: treating unequal subdivision as "feel" and implementing it with
random spread. Unequal subdivision is a position in the grid, not a deviation from one.

## A genuine disagreement, stated as one

Lerdahl & Jackendoff (1983) require equal spacing at the tactus and above. Metrical levels in
their framework are isochronous by definition, and unequal beat spacing is handled as something
other than metre. London admits unequal beats as metre.

These frameworks **disagree**. This is not a case where one is a refinement of the other, and
the studio does not quietly pick a winner.

```text
if the repertoire is one Lerdahl & Jackendoff's rules were built on
    their hierarchy is the better tool; unequal spacing will be rare and marked
if the repertoire has documented non-isochronous beats
    London's framework is the better tool; forcing equal spacing misdescribes it
in either case
    say which framework is being used, and that the other exists
```

Both are lenses with provenance, not neutral physics. `shared/RESEARCH_RULES.md` covers the
general form of this caution.

## What each specialist does with it

**Composer** fills the meter object before writing pitches. It states `beat_pattern` explicitly,
never a bare signature, and it names the intended tactus. If the metre is non-isochronous it
says so and cites the system it comes from, linking to the relevant page in
`shared/MUSICAL_SYSTEMS/`.

**Performance Director** checks every active layer against the perceptual limits at the planned
tempo. It warns before the fastest layer crosses the floor and thins rather than compresses. It
also checks that `tactus_ms` is inside the entrainable range.

**Listener Model** asks what a listener will entrain to, which is not always what is notated. A
notated 7/8 at a fast tempo may be heard as an uneven pulse of three beats rather than as seven.
The model reports the likely hearing and any alternatives, and does not assume the notation
wins.

**MIDI Builder** maps unequal subdivision onto a fine grid rather than forcing triplets. It
records `beat_pattern` in the exported metre where the format allows and in a track note where
it does not, so the grouping survives the export.

## Cross-links

- `ADDITIVE_AND_NONISOCHRONOUS_METER.md` for building metres from 2s and 3s
- `CYCLES_AND_TIMELINES.md` for when the measure is a cycle with an external marker
- `MICROTIMING_AND_GROOVE.md` for what happens inside the beat
- `shared/MUSICAL_SYSTEMS/ADDITIVE_METERS_BALKAN_TURKISH.md` and
  `shared/MUSICAL_SYSTEMS/RAGA_AND_TALA.md` for the traditions these objects describe
