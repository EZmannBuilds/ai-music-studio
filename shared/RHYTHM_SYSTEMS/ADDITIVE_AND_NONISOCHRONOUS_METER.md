# Additive and Non-Isochronous Meter

## Building a metre from 2s and 3s

A large family of metres is built by chaining short and long units over a single fast pulse. The
units are usually two pulses and three pulses. The chain, not the total, is the metre.

```text
7/8  = 2+2+3      9/8  = 2+2+2+3      5/8  = 2+3  or  3+2
7/8  = 3+2+2      9/8  = 3+3+3        11/8 = 2+2+3+2+2
```

`2+2+3` and `3+2+2` share a total and share nothing else. They start differently, they are
danced differently, and a listener entrains to them differently. This is why the standing rule
in `INDEX.md` forbids a bare odd signature: **write the grouping**.

Brăiloiu (1951, "Le rythme aksak") described such periods as built from Short and Long units in
a nominal 2:3 relation. The nominal ratio is where the notation starts. It is not where
performance ends up.

## The performed ratio is not the notated ratio

The beat-pattern string says which pulses group together. It does not say how long the groups
are in performance. Those are two separate pieces of information and the object carries both.

```yaml
nonisochronous_meter:
  fast_pulse_ms:            # the unit the groups are counted in
  beat_pattern: []          # e.g. [2, 2, 3]
  performed_ratio:
    nominal:                # e.g. "2:3" as notated
    measured_range:         # e.g. "short 0.40-0.45 of the pair" with the corpus named
    corpus:                 # which repertoire, which study, which tempo range
```

The measured figures the studio has come from two named pieces: in *Bire*, a Khasonka dundunba piece, the bell's long-short subdivision averages **58.6:41.4** across four performances by two players (one near 60:40, the other near 57:43); in *Ngòn Fariman*, a Segu Bambara piece, a ternary long-short-short pattern averages about **41:31:28** (Polak & London 2014, *MTO* 20.1, read 2026-09-15). Those are measurements
of those pieces, played by those ensembles, at tempi that accelerate from about 85 to 125 BPM. They
are not a Malian ratio, not a general aksak ratio, and must not be copied onto a Balkan dance
because both are "uneven".

If no measurement exists for the target repertoire, the honest move is to write the nominal
ratio, mark the performed ratio as unmeasured, and say so in the plan. Do not invent a decimal.

## Why "additive" is a stance, not a fact

Agawu (2006, *JAMS*) and *Representing African Music* (2003) argue that the additive/divisive
pair is used imprecisely, and that an "additive" reading can smuggle in a claim the analyst
never defended: that the music has **no metre**, only a string of added durations.

That claim is often false. A 12-pulse timeline with a stable cycle and a stable reference point
is metrical. Calling it additive because it does not divide evenly into 4/4 describes the
notation system's discomfort, not the music.

So the word is used here with limits:

```text
additive        a description of how a metre is written down: units chained rather than divided
not additive    a claim that the music lacks a metre, a tactus, or a hierarchy
```

When the studio writes `9/8 = 2+2+2+3` it is describing a grouping inside a metre. It is not
claiming the music is a sequence of unrelated durations. If a source or a user makes the
stronger claim, the plan says the stronger claim is contested and cites Agawu.

## Tuplets and odd subdivisions

A tuplet is the other way to get an unequal-looking division: keep the beat, divide it into a
count the metre does not supply.

```text
one level        quarter = 5 equal parts                          allowed by default
one level        dotted quarter = 4 equal parts                   allowed by default
two levels       a 5-tuplet whose third element is a 7-tuplet     requires a flag
```

Ferneyhough's nested tuplets are the documented case at the far end: beyond about **two levels
of nesting**, notated ratios decouple from anything a listener tracks. The ratio still means
something to a performer reading it and to an analyst counting it. It stops meaning something to
entrainment.

The studio's rule:

- one level of tuplet nesting is allowed without comment;
- deeper nesting requires an explicit `notational_only: true` flag on the passage;
- with that flag set, the Listener Model scores the passage on its audible result, not on the
  ratio, and the plan says what the audible result is meant to be.

```yaml
tuplet:
  base_value:
  divisions:
  nesting_depth:            # 1 by default
  notational_only: false    # must be true if nesting_depth > 1
```

The flag exists so that a deep nesting is a decision someone made, rather than an accident of a
generator chaining ratios.

## Encoding

MIDI Builder does not implement non-isochronous subdivision as triplets against a straight grid.
That misrepresents the metre and it fights the DAW's quantiser. The route is a fine pulse grid:

```text
choose a pulse short enough to express every group exactly
place onsets at integer multiples of that pulse
carry beat_pattern as metadata so the grouping survives
apply performed_ratio as a microtiming template, not as random spread
```

The last line matters. An unequal subdivision is a target position, and Polak, Jacoby & London
(2016) found it is held as precisely as an equal one. Implementing it with jitter produces a
looser result than the tradition it is imitating, not a more human one. See
`MICROTIMING_AND_GROOVE.md`.

## What each specialist does with it

**Composer** writes the grouping and, where the system is a named one, links to
`shared/MUSICAL_SYSTEMS/ADDITIVE_METERS_BALKAN_TURKISH.md` rather than describing the dance
here. It decides whether the piece needs a performed ratio at all, or whether an even reading is
intended.

**Performance Director** turns `performed_ratio` into a microtiming template with a named
corpus, or declines to and says the ratio is unmeasured. It checks the fast pulse against the
perceptual floor in `METER_AND_PULSE.md`.

**Listener Model** asks whether a listener can hold the grouping. A long chain of mixed units at
a fast tempo may be heard as an irregular surface over a simpler tactus, and the model reports
that.

**MIDI Builder** uses the fine-pulse grid, carries `beat_pattern` into the export, and states
the pulse resolution it chose.

## Cross-links

- `METER_AND_PULSE.md` for the meter object and the perceptual limits
- `MICROTIMING_AND_GROOVE.md` for the measured ratio ranges and the template object
- `shared/MUSICAL_SYSTEMS/ADDITIVE_METERS_BALKAN_TURKISH.md` for the dances themselves, their
  names, their regions and their repertoire
