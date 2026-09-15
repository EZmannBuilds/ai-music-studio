# Research: Rhythm Systems

## Purpose

The research behind `shared/RHYTHM_SYSTEMS/`, the rhythm brief in `composer/SKILL.md`, the groove
model in `listener-model/SKILL.md` and the timing models in `performance-director/SKILL.md`.

The guiding question:

> What is there beyond 4/4, syncopation and swing, and how much of it can be stated as mechanism
> rather than as flavour?

## Evidence note

Most journal hosts were unreachable when this page was written. Entries rest on abstracts and
excerpts except where noted. Figures are ranges from particular corpora, never constants.

---

# 1. Metre has perceptual limits, and need not be isochronous

## Research

- London, *Hearing in Time* (2004; 2nd ed. 2012): metre is entrainment, constrained by what can be
  perceived as a periodicity, and **non-isochronous metres are well formed**, not deviations.
- Polak & London (2014), *MTO* 20(1), and Polak & London (2022) on Malian drumming: roughly **100 ms**
  is the rule-of-thumb floor for the fastest metrical subdivision, better treated as a range from
  about 120 ms down to about 80 ms; the fastest useful beat is around 250 ms and the slowest around
  1.5 s. In *Bire* (Khasonka dundunba) the bell's long-short subdivision averages 58.6:41.4, and in
  *Ngòn Fariman* (Segu Bambara) a long-short-short pattern averages about 41:31:28; the patterns hold
  through acceleration from about 85 to 125 BPM (2014 paper read for 2.1). 2.0 also stated here that
  ensembles **drop the fastest layer** as tempo rises; the 2014 paper does not report that, and the
  claim is unverified.
- Polak, Jacoby & London (2016), *Frontiers in Neuroscience*: non-isochronous subdivision supports
  ensemble entrainment as precisely and stably as isochronous subdivision.
- Lerdahl & Jackendoff (1983) require equal spacing at the tactus and above; London admits unequal
  beats. The two frameworks genuinely disagree, and the disagreement is worth stating.

## Skill translation

A metre in `shared/RHYTHM_SYSTEMS/METER_AND_PULSE.md` is an object:

```yaml
meter:
  cycle_length_pulses:
  beat_pattern: []          # e.g. [2, 2, 2, 3]
  subdivision_pattern: []   # isochronous or long/short
  tactus_ms:
```

The Performance Director checks the fastest layer against the tempo and warns before a layer crosses
the floor. MIDI Builder maps unequal subdivision onto a fine grid rather than forcing triplets.

---

# 2. Vocabulary for layered conflict

## Research

- Krebs (1999), *Fantasy Pieces*: **grouping dissonance** (incongruent cardinalities, such as 3
  against 2) and **displacement dissonance** (same cardinality, shifted). This gives a way to describe
  layered conflict as a relationship rather than as an error.
- Definitions in the reference literature: polyrhythm is simultaneous rhythms not heard as derived
  from one another; cross-rhythm is polyrhythm as the basis of a whole piece; hemiola and sesquialtera
  both name a 3:2 relation, with some theorists reserving hemiola for a momentary regrouping.
- Documented cases: Pieslak (2007), *Music Theory Spectrum*, on Meshuggah's odd groupings over a
  steady anchor; Reich's *Clapping Music* (a discrete shift of one eighth through twelve rotations)
  and *Piano Phase* (continuous); Ligeti's Études, which combine a Romantic hemiola practice with an
  additive-pulsation principle encountered through Arom's Central African recordings.

## Working definitions adopted

```text
polyrhythm     different subdivisions of a shared cycle; they land together each cycle
polymeter      different cycle lengths over a shared pulse; they realign at the common multiple
cross-rhythm   a polyrhythm that is the structural basis, not an ornament
hemiola        a temporary 3:2 regrouping inside one metre
displacement   the same pattern shifted against an anchor
```

Every layered passage names an **anchor layer**. Without one, a displaced pattern is simply heard in a
new metre, and the intended tension does not exist.

---

# 3. Additive metre, and a caution about the word

## Research

- Brăiloiu (1951), "Le rythme aksak": a period built from Short and Long units, nominally 2:3.
- Bartók's *Mikrokosmos* 148–153 notate groupings such as 3+2+3/8.
- Agawu (2006), *JAMS*, and *Representing African Music* (2003): the additive/divisive pair is used
  imprecisely, and an "additive" reading can smuggle in the claim that a music has no metre.
- Ferneyhough's nested tuplets: beyond about two levels of nesting, notated ratios decouple from
  anything a listener tracks.

## Skill translation

Aksak is represented as a beat-pattern string over a fast pulse plus a **performed** short-to-long
ratio range, because the nominal 2:3 is not what performance measures. One level of tuplet nesting is
allowed by default; deeper nesting requires an explicit "notational only" flag.

Never write a bare odd signature. Write the grouping: `9/8 = 2+2+2+3`.

---

# 4. Euclidean rhythms generate shapes, not names

## Research

- Toussaint (2005), "The Euclidean Algorithm Generates Traditional Musical Rhythms": E(k,n)
  distributes k onsets as evenly as possible over n pulses. Confirmed matches include E(3,8) as the
  Cuban tresillo, E(5,8) as the cinquillo and E(5,16) as a bossa nova pattern. Several matches require
  rotating the generated necklace.
- Bjorklund (2003) devised the algorithm for accelerator timing; Toussaint showed it coincides with
  Euclid's steps.

## Skill translation

`EUCLIDEAN_AND_GENERATED_RHYTHM.md` implements E(k,n) with an explicit `rotation` parameter, because
rotation is where the musical and cultural meaning lives. The studio **never labels a generated
pattern with the name of a tradition** unless the pattern, its rotation and its tempo range match a
documented case, and then it says which.

---

# 5. Metric modulation and tempo morphing

## Research

- Carter's Cello Sonata (1948) is the prominent early use; the term was coined by a reviewer, and
  Carter preferred "tempo modulation". The mechanism: a value in the old tempo is set equal to a
  different value in the new one, so new tempo = old tempo × (old value ÷ new value).
- Stravinsky's *Symphonies of Wind Instruments* holds a constant eighth across tempi in a 2:3:4
  relation.
- Nancarrow's tempo canons run voices at different, sometimes irrational, tempo ratios, with
  convergence points where they coincide.
- Digital audio workstations expose tempo as a master lane, with differing decimal precision, and none
  of the common ones give a track its own tempo.

## Skill translation

Two implementation routes, and a plan picks one rather than mixing them:

```text
tempo-map route     write a tempo event at the pivot; notation stays simple in the new tempo
implied-pulse route keep the tempo and write the new pulse as tuplets; the grid stays stable
```

The pivot value must be audible for at least a bar before the switch, or the modulation is heard as a
new piece. Tempo canons are emulated by re-quantisation or by stretching a rendered voice.

---

# 6. Cycles are not bars

## Research

- Clayton (2000), *Time in Indian Music*: tāl is externalised through clap patterns and drum thekas,
  has at least three pulse levels, and **sam** is both the end of one cycle and the beginning of the
  next, functioning as an arrival.
- Arabic iqā'āt are defined by a dum and tak skeleton with rests, in cycles from 3 to 48 or more
  pulses, ornamented freely over a fixed skeleton.
- Javanese colotomic structure marks nested intervals with specific gongs, and the largest gong falls
  at the **end** of the cycle.
- Locke (2009; 2010) describes a "metric matrix" in Ewe music: several simultaneously valid hearings,
  where Western notation forces a single one. Agawu (2006) treats the same bell pattern as a time line
  whose entry point is contested.

## Skill translation

```yaml
cycle:
  length_pulses:
  marker_pattern:
  reference_point: start | end | multiple
  hierarchy_levels: []
```

MIDI Builder never silently converts a 12-pulse timeline into 4/4 with an initial downbeat, and the
Listener Model reports alternative hearings instead of forcing one.

---

# 7. Microtiming is a template, not a randomiser

## Research

- Friberg & Sundström (2002): the swing ratio falls from about 3.5:1 at slow tempi toward 1:1 at fast
  tempi, with the short note near 100 ms across medium to fast tempi.
- Naveda, Gouyon, Guedes & Leman (2011), *JNMR*: in a samba corpus, the third and fourth sixteenths of
  each beat are systematically early relative to a quantised grid, interacting with intensity and
  metric position.
- Polak & London (2014): *Bire* bell subdivision about 59:41; *Ngòn Fariman* about 41:31:28. Two pieces, not a Malian constant.
- Danielsen (2006; ed. 2010): the **beat bin**, a span rather than a point, whose felt centre depends
  on the shape of the sound; and the scholarly account of the displaced pulse associated with
  D'Angelo and the Soulquarians.
- Against the idea that deviation itself creates groove: Butterfield (2010), Davies et al. (2013),
  Frühauf et al. (2013), Senn et al. (2016). See `research/PERFORMANCE_AND_EXPRESSION.md`.

## Skill translation

```yaml
microtiming_template:
  subdivision_level:
  offsets_percent_of_beat: []    # per position, systematic
  tempo_function:                # e.g. swing ratio as a function of BPM
  beat_bin_width_ms:
  tightness_sd_percent:          # 1-3% of beat in the studied corpora
```

Marker instruments — bell, gong, clap, clave — are never "humanised". They are the reference everything
else is heard against.

---

# 8. Displacement needs something to be displaced from

Krebs' displacement dissonance, Reich's process and the soloist lag measured by Friberg & Sundström
all require an audible reference. The operator therefore carries an anchor and a resolution point:

```yaml
displacement:
  motif:
  shift: {amount:, unit:}
  anchor_layer:
  schedule: static | stepwise | continuous
  resolve_at:
```

The Listener Model requires the undisplaced motif to be established first before it scores a
displacement as intelligible.

---

# 9. Cautions

- Every number here is a range from a particular corpus at a particular tempo, not a constant.
- "Quantised rated highest" is a result about rock and pop stimuli with mostly Western student
  listeners. It is not a verdict on jazz, samba, Malian drumming or hip-hop.
- Keil's participatory-discrepancy theory is contested, not established.
- Euclidean generation recovers a shape. It does not recover a rotation, an accent hierarchy, a dance
  or a name.
- "Additive" is a notational stance. Used loosely it denies a music its metre.
- Western theory frameworks and outsider ethnography are lenses with provenance, not neutral physics.
  Where they disagree, the skill files say so.
- To verify before quoting: London's upper limit for the measure, the full Toussaint correspondence
  table, and direct quotations from Carter.

---

# 10. Primary sources

- London, 2004/2012 — *Hearing in Time*
- Polak & London, 2014; 2022; Polak, Jacoby & London, 2016 — Malian metre and subdivision
- Lerdahl & Jackendoff, 1983; Temperley, 2001 — metrical hierarchy, preference rules
- Krebs, 1999 — metrical dissonance
- Agawu, 2003; 2006 — representing African music, the standard pattern
- Locke, 2009; 2010 — metric matrix
- Clayton, 2000 — time in Indian music
- Brăiloiu, 1951; Arom, 1991; 2004 — aksak, African polyphony and polyrhythm
- Toussaint, 2005; 2013 — Euclidean rhythms, the geometry of musical rhythm
- Pieslak, 2007 — metre in Meshuggah
- Friberg & Sundström, 2002; Naveda et al., 2011 — swing and samba microtiming
- Danielsen, 2006; 2010 — beat bin, funk and neo-soul rhythm
