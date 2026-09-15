# Research: Musical Systems and Tuning

## Purpose

The research behind `shared/MUSICAL_SYSTEMS/`, `shared/TUNING_AND_MPE.md`, the pitch-system step in
`composer/SKILL.md` and the tuning capability fields in `plugin-auditor/SKILL.md`.

The guiding question:

> What do musicians inside these traditions say their systems are, and what can be taught as musical
> logic without flattening a living practice into a scale?

## Evidence note

Nearly every primary host was unreachable when this page was written. Entries rest on search excerpts
of the named sources and are marked **to verify** where even that was thin. No citation here should be
quoted with a page number until the text has been read. This is a limitation of the research pass, not
a claim about the sources.

---

# 1. The finding that shapes every file

Independent sources in unrelated traditions say the same thing in different words:

| Source | What it says |
|---|---|
| Abu Shumays (2013) | ajnas, not octave scales, are the operative units of maqam |
| Bor; Clayton (2000) | a raga is behaviour and a tala is a cycle |
| Sumarsam; Tenzer (2000) | gamelan tuning is per ensemble, form is colotomic |
| Titon (1977); Evans (1982); Cutting (2018) | blue notes are pitch *areas* |
| Marcus (1993); Akkoç | 24-EDO and 53-comma theory are notations, not measured practice |
| Breathnach (1971); Bronson | gapped scales are the point, not an absence |

A file that emits "Maqam Bayati equals these seven notes" or "slendro equals five-tone equal
temperament" has already failed. `shared/MUSICAL_SYSTEMS/INDEX.md` makes this the first rule: encode
phrase grammar, pivots, cycle markers, ornament as pitch contour, and intonation as context-dependent
ranges, and mark any table of cents as one measured instance of one ensemble or performer.

---

# 2. What each system contributes as transferable logic

### Arabic maqam
Melodic identity lives in three- to five-note cells (ajnas) with a tonic and a pivot from which the
next cell hangs. A maqam is a **path** with places to dwell, ascend, modulate and cadence. Intonation
belongs to the cell in context, not to an abstract scale degree: the same written note is tuned
differently in Egyptian, Levantine and Turkish practice, and the equal 24-division was contested at
the 1932 Cairo Congress rather than agreed. Improvisation (taqsīm) establishes the maqam low, may
travel, and returns, with cadential formulas closing sections.

### Hindustani and Carnatic raga and tala
A raga is a grammar: ascending and descending forms, a principal and secondary note, an identifying
phrase, characteristic crooked motion and characteristic ornament. Two ragas can share all seven
notes and be entirely different. Form is a density gradient over fixed pitch material. The tala cycle
has an arrival point that is simultaneously the end and the beginning, and an "empty" region that
creates orientation by absence. In Carnatic practice the oscillation is not decoration of the note;
it is the note.

### Clave, timelines and West African polyrhythm
A timeline is a reference ostinato, asymmetric inside a symmetric cycle, that everything else is heard
against. It is neither the metre nor the melody. Twelve- and sixteen-pulse cycles support
simultaneous four- and six-beat hearings, and the music uses that ambiguity deliberately. The 3-2 and
2-3 orientations are a decision about which half of the pattern aligns with the harmonic or lyrical
start, not two different rhythms.

### Gamelan
There is no canonical slendro or pelog in cents: each ensemble has its own interval profile, and two
respected sets can differ while both sound right. Form is nested cycles marked by punctuating
instruments, with the largest gong at the **end**. A skeletal melody is elaborated at fixed density
ratios, so changing tempo level means changing density, not only speed. Paired instruments are tuned
slightly apart on purpose, making the ensemble's shimmer a tuning parameter.

### Aksak and usul
Unequal beats are the primary metrical level, not a subdivision trick. The same total divides
differently for different dances, and those are different pieces. In Turkish art music the cycle binds
melodic phrase length. Theory in 53 commas is deviated from systematically in performance.

### Blues as a system
The third, fifth and seventh are microtonal areas rather than flattened degrees; measurement of
recorded performances finds the major third common enough to belong in the system. Melody is built on
a frame of stacked thirds that is independent of the chords underneath, which is why a melody note can
sit against the harmony without being an error. Twelve bars is one form among eight-bar, sixteen-bar
and irregular ones.

### Drone traditions
With a fixed reference sounding continuously, every melodic note is heard as an interval against it,
so intonation becomes audible as beating and tension comes from degree and register rather than chord
change. The drone's own overtone structure supplies partials the melody locks to, which is why drone
traditions tend toward just intervals.

### Modal folk systems
Melody carries the mode; harmony is optional and modal when present. Gapped scales let a tune be heard
in two modes at once, which is a feature. Sympathetic strings and open-string tonal centres pull
intonation toward resonance rather than toward equal temperament.

---

# 3. Tuning theory

- Every tuning trades pure intervals against note count against transposability. Meantone buys thirds
  and loses keys; well temperaments buy all keys and vary key colour; twelve-tone equal temperament
  buys uniformity and loses a little of everything.
- A **limit** names which primes the harmony admits. Partch's system is built from an eleven-limit
  diamond, with otonality and utonality as the two directions.
- Equal divisions are best understood by which just intervals they approximate and which commas they
  temper out: 19 and 31 in the meantone family, 22 with a sharp fifth and a nearly just septimal
  third, 53 with near-pure fifths and a role in Turkish theory.
- Sethares (1998; 2005): consonance depends on the relation between a timbre's partials and the scale.
  For inharmonic timbres — bells, many gamelan instruments, stretched partials — the "right" scale
  changes. **Design timbre and tuning together.**
- Notation systems for extended just intonation exist and differ; Johnston's accidentals and the
  Helmholtz-Ellis system are two, and they are not interchangeable.
- Non-octave scales exist; the Bohlen-Pierce scale repeats at 3:1 rather than 2:1.

---

# 4. Implementation

| Mechanism | What it is | Practical note |
|---|---|---|
| `.scl` | plain-text scale: description, note count, then cents or ratios; last line is the period | says nothing about which key it starts on |
| `.kbm` | keyboard mapping: size, range, middle note, reference note and frequency, period degree | not supported everywhere |
| MIDI Tuning Standard | bulk dump, real-time single-note retune, scale/octave forms | resolution near 0.0061 cents; adoption is uneven |
| MTS-ESP | a master plugin retunes client plugins in a session, in real time, even on held notes | falls back to a local table, 12-tone equal by default |
| MPE | per-note pitch bend, default range ±48 semitones, at most 15 notes per zone | about 0.586 cents per unit at 14-bit |
| per-channel bend | one voice per channel with the range set by RPN | costs polyphony; last resort |

The hierarchy adopted in `shared/TUNING_AND_MPE.md`:

```text
1. an MTS-ESP-style master, when every instrument is a client
2. per-instrument scale files, remembering each product maps 1/1 differently
3. MPE per-note bend with the range declared
4. one voice per channel with an explicit bend range
```

A Standard MIDI File can carry tuning sysex and per-channel bends, but the receiver has to honour
them, so the export states which mechanism it used and what happens if the receiver ignores it.
**Silent re-quantisation to twelve-tone equal temperament is never acceptable**: if the instrument
cannot be retuned, the studio says so and offers a substitution or a bend-based fallback.

---

# 5. Cautions

**On appropriation.** Several of these systems are living, taught orally, and embedded in ritual or
community practice. Some ensembles and repertoires are consecrated. The skill files name the tradition
and its people precisely instead of using umbrella terms, separate *learning the logic* from
*presenting output as that tradition*, recommend crediting and where possible collaborating with
tradition bearers, and decline sacred or community-restricted repertoire.

**On reduction.** See section 1. The most common failure is to keep the scale and throw away the
grammar, then add a characteristic instrument sample and call the result the tradition.

**Where sources disagree.** Whether West African timeline music has metre in the Western sense; whether
an equal quarter-tone exists in Arabic practice; how the blues third should be modelled; whether a
timeline is best described geometrically or as a named dance. The skill files present these as open
questions, because they are.

---

# 6. Primary sources

- Farraj & Abu Shumays, *Inside Arabic Music*, 2019; Abu Shumays, "Maqam Analysis: A Primer", 2013;
  Marcus, 1993, on intonation in Arab music
- Bor (ed.), *The Raga Guide*, 1999; Clayton, *Time in Indian Music*, 2000; Schachter on gamaka, 2015
- Agawu, 2003; 2006; Locke, 2010; Kubik, 1994; Toussaint, 2013; Peñalosa, 2009 — timelines and clave
- Sumarsam; Tenzer, 2000; Sorrell, 1990 — Javanese and Balinese gamelan
- Brăiloiu, 1951; Arom, 2004 — aksak typology
- Titon, 1977; Evans, 1982; Kubik, 1999; Van der Merwe, 1989; Cutting, 2018 — blues tonality
- Partch, *Genesis of a Music*, 1949/1974; Sethares, *Tuning, Timbre, Spectrum, Scale*, 1998/2005
- Fonville on Johnston notation, 1991
- MIDI Manufacturers Association — MIDI Tuning Standard, MPE 1.0
- Scala scale file format documentation; ODDSound MTS-ESP documentation
