# Microtiming and Groove

## Microtiming is a template, never a randomiser

Microtiming is the systematic placement of events away from an even grid. The word "systematic"
is doing all the work. Measured microtiming in the studied repertoires is **reproducible**: the
same player puts the same subdivision in the same place, take after take, and an ensemble agrees
on it.

A random offset is not a weak version of that. It is a different thing, and it does not produce
the same result. This folder therefore carries **no parameter named random**, matching
`shared/HUMAN_PERFORMANCE_SCHEMA.md`, and every timing deviation comes from a named template
with a named corpus behind it.

Polak, Jacoby & London (2016) found that non-isochronous subdivision supports ensemble
entrainment as precisely and stably as isochronous subdivision. Unequal is not loose. It is a
different target, held tightly.

## The template object

```yaml
microtiming_template:
  subdivision_level:            # which level the offsets apply to, e.g. eighths, sixteenths
  offsets_percent_of_beat: []   # one systematic offset per position in the beat
  tempo_function:               # how the offsets change with tempo, e.g. swing ratio by BPM
  beat_bin_width_ms:            # the span within which an onset reads as on the beat
  tightness_sd_percent:         # spread around the target position
  corpus:                       # which repertoire, which study, which tempo range
  applies_to: []                # parts; never the marker parts
```

`offsets_percent_of_beat` is per position, not per note. Position 1 of the beat and position 3
of the beat get different offsets, and every note in that position gets the same one.

`corpus` is required. A template without a named corpus is a guess, and the plan must say it is
one.

`tightness_sd_percent` is the spread, and it is the only place any randomness enters. The schema
allows roughly **1 to 5 percent of the beat**; the studied corpora cluster nearer **1 to 3
percent**. Use the low end unless a measurement of the target repertoire says otherwise. This is
a spread around a systematic target, not a substitute for one.

## Documented templates

Each of these came from a particular corpus at particular tempi. None is a constant, and none
transfers to a repertoire that was not measured.

### Swing, from ride-cymbal measurement

Friberg & Sundström (2002, *Music Perception* 19(3)): the swing ratio **falls from about 3.5:1
at slow tempi toward 1:1 at fast tempi**, and the short note stays **near 100 ms** across medium
to fast tempi.

```text
slow tempi        ratio near 3.5:1        strongly uneven
medium tempi      ratio falling           the short note holds near 100 ms
fast tempi        ratio approaching 1:1   effectively even
```

Two things follow. A fixed 2:1 swing is a single point on this curve, not a general rule; it
occurs at one tempo. And the constant that survives across medium to fast tempi is the
**duration of the short note**, not the ratio, so a swing implementation should be parameterised
by tempo rather than by a percentage slider left at one setting.

### Samba sixteenths

Naveda, Gouyon, Guedes & Leman (2011, *JNMR*): in a samba corpus, the **third and fourth
sixteenths of each beat are systematically early** relative to a quantised grid. The deviation
interacts with intensity and with metric position, so it is not one number applied uniformly.

```text
sixteenth 1    at or near the grid
sixteenth 2    at or near the grid
sixteenth 3    early
sixteenth 4    early
```

The magnitudes belong to that corpus at those tempi. Carry the shape, state the corpus, and do
not present a figure that was not measured.

### Two measured Mande pieces

Polak & London (2014): in *Bire*, a Khasonka dundunba piece, the bell's long-short subdivision averages **58.6:41.4** across four performances by two players (one near 60:40, the other near 57:43); in *Ngòn Fariman*, a Segu Bambara piece, a ternary long-short-short pattern averages about **41:31:28** (Polak & London 2014, *MTO* 20.1, read 2026-09-15). See `ADDITIVE_AND_NONISOCHRONOUS_METER.md` for how this is encoded as a
metre rather than as a deviation, and `shared/MUSICAL_SYSTEMS/MANDE_JEMBE_MUSIC.md` for
the music itself.

### Within-part tightness

Standard deviations of within-part timing in the studied corpora sit in the low single digits as
a percentage of the beat. This is the ceiling for `tightness_sd_percent`, not a target to
exceed.

## The beat bin

Danielsen (2006; ed. 2010) describes the **beat bin**: the beat is a **span**, not a point, and
the felt centre of an event inside that span depends on the **shape of the sound**, not only on
its onset.

A slow-attack pad placed exactly on the grid is felt late. A sharp transient placed slightly
late is felt on time. Onset-only measurement cannot see any of this, which means a measured
timing chart can say a part is perfectly placed while the part sounds wrong, and can say a part
is late while it sounds correct.

The practical consequence, which the Producer and Mix Engineer also act on:

> **A timing problem is sometimes a transient problem.**

Before moving a part in time, check whether the attack, the sample choice, the envelope or the
compression changed the felt centre. Shifting a note to compensate for a soft attack fixes one
tempo and one arrangement and breaks the rest.

`beat_bin_width_ms` in the template records how wide the usable span is for that style. A wide
bin is permission for placement variety; a narrow bin is a style built on exact placement.

## The evidence against deviation-as-groove

This must be stated fairly, because the popular belief runs the other way.

- **Frühauf, Kopiez & Platz (2013)**: systematic microtiming shifts applied to a rock drum
  pattern **decreased** groove, liking and naturalness compared with the quantised version. The
  authors propose an "aesthetics of exactitude" for some groove styles.
- **Davies, Madison, Silva & Gouyon (2013)**: microtiming varied from none to about twice its
  natural magnitude. Quantised and natural versions were rated **equally**; exaggerated versions
  were rated lower.
- **Senn, Kilchenmann, von Georgi & Bullerjahn (2016)**: microtiming taken from a competent
  performance did **not** increase groove relative to quantised; doubling its magnitude
  decreased groove, **most strongly for expert listeners**.
- **Butterfield (2010)**: little support for bass/drum asynchrony as the source of swing; the
  effects found were local and explained by metric entrainment.

Two conclusions, and no more than two.

**Natural magnitude is a ceiling.** A "more human" control that scales past what players do
scales into the region listeners liked least, and the dislike was strongest among the listeners
with the most training.

**Exactitude is a style, not a default failure.** Some repertoires are built on precise
placement, and quantising them is correct.

And the caution that belongs with the conclusions: these results come from short loops, mostly
rock and pop stimuli, with mostly Western student listeners. **They are not a verdict on jazz,
samba, Malian drumming or hip-hop**, all of which have documented systematic feels measured in
their own repertoires. Keil's participatory-discrepancy theory is contested, not established,
and is not treated here as settled either way.

## Marker instruments keep their own feel, and get no other

**Bell, gong, clap and clave are the reference everything else is heard against.** Applying another
part's template to the marker, or a random offset, moves the reference, which does not make the
groove deeper; it makes the groove undefined, because there is nothing left for the other parts to be
early or late against.

**The exception is a marker whose own feel is part of the music.** In *Bire*, a Khasonka dundunba
piece, the bell itself plays the non-isochronous long-short subdivision the ensemble follows
(Polak & London 2014; see "Two measured Mande pieces" above). There the marker is placed exactly on
that piece's named template, which is a position in the cycle, not a deviation from it. And a drum
kit in live-feel music is not a marker part by default: its microtiming is the groove.

This is the same requirement as the anchor layer in `POLYMETER_POLYRHYTHM_CROSSRHYTHM.md` and
the marker part in `CYCLES_AND_TIMELINES.md`, stated for timing.

`applies_to` in the template object lists the parts a template touches. A marker part appears in
that list only when the template is the marker's own documented feel, with its corpus named; a plan
that applies another part's template, or an unnamed one, to the marker is rejected rather than
executed.

## What each specialist does with it

**Composer** decides whether the music has a feel at all, names the style, and says whether
exact placement is part of the identity. It does not specify millisecond offsets.

**Performance Director** selects the template, names its corpus, sets `tightness_sd_percent` at
the low end by default, keeps within natural magnitude, applies the tempo function rather than a
fixed ratio, and excludes the marker parts. Any deviation layer is applied last and least, after
phrase shape, metrical accent and ensemble relationships.

**Listener Model** judges the groove result, not the deviation amount. It reports when a
template has been exaggerated past its corpus, and it does not award credit for deviation as
such. It applies the audience calibration in `shared/RESEARCH_RULES.md`, because expectation is
listener-dependent.

**MIDI Builder** writes the offsets as note positions on a fine grid, records which template and
which corpus were used, keeps the marker parts on the grid, and states in its report whether the
export preserved the offsets or the destination re-quantised them.

## Cross-links

- `research/PERFORMANCE_AND_EXPRESSION.md` for the full performance evidence and the named
  models
- `ADDITIVE_AND_NONISOCHRONOUS_METER.md` for unequal subdivision as metre rather than deviation
- `DISPLACEMENT_AND_METRIC_DISSONANCE.md` for deliberate shifts against an anchor
- `shared/QUALITY_GATE.md` for the groove and expectation checks
