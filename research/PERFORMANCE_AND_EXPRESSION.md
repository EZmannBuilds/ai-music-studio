# Research: Human Performance, Expression and MIDI Realisation

## Purpose

The research behind `performance-director/SKILL.md`, `shared/HUMAN_PERFORMANCE_SCHEMA.md` and the
expression rules in `midi-builder/SKILL.md`.

The guiding question:

> What do performers actually do to a score, and which of it can be modelled rather than randomised?

## Evidence note

Several journal pages and manufacturer PDFs could not be opened when this page was written; those
entries rest on abstracts, search excerpts and one manual read in full. Each claim below says which.
Items marked **to verify** should be confirmed against the primary text before anyone quotes a page
number or a exact figure from them.

---

# 1. The central finding: organic is not random

## Research

- Frühauf, Kopiez & Platz (2013), "Music on the timing grid", *Musicae Scientiae* 17(2): systematic
  microtiming shifts applied to a rock drum pattern **decreased** groove, liking and naturalness
  compared with the quantised version. The authors propose an "aesthetics of exactitude" for some
  groove styles.
- Davies, Madison, Silva & Gouyon (2013), *Music Perception* 30(5): microtiming was varied from none
  to about twice its natural magnitude. Quantised and natural versions were rated **equally**;
  exaggerated versions were rated lower.
- Senn, Kilchenmann, von Georgi & Bullerjahn (2016), *Frontiers in Psychology* 7:1487: microtiming
  taken from a competent performance did **not** increase groove relative to quantised; doubling its
  magnitude decreased groove, most strongly for expert listeners.
- Hennig et al. (2011), *PLOS One* 6(10): human timing fluctuations are long-range (1/f) correlated,
  and listeners preferred 1/f-humanised sequences over white-noise-humanised ones.
- Räsänen et al. (2015), *PLOS One* 10(6): a virtuoso drummer's hi-hat track showed long-range
  correlations, short-range anticorrelations and two-bar periodic patterns in both timing and
  amplitude.
- Butterfield (2010), *Music Perception* 27(3): little support for bass/drum asynchrony as the source
  of swing; the effects found were local and explained by metric entrainment.

## Skill translation

`shared/HUMAN_PERFORMANCE_SCHEMA.md` carries **no parameter named random**. Timing and dynamic
deviations are produced by named models, each of which can be inspected and argued with:

```text
phrase_arch              tempo and dynamics shaped over a phrase
metrical_accent          accent by position in the bar or cycle
chord_asynchrony         derived from voicing and velocity, not scattered
section_offset           one constant per part per section (laid-back horns, driving hats)
swing_ratio(tempo)       a ratio that changes with tempo
drift_1f                 a small long-range-correlated wander, applied last and least
```

Natural magnitude is the ceiling. A "more human" control that scales past what players do is scaling
into the region listeners liked least.

## Caution

These results come from short loops, mostly rock and funk stimuli, and mostly Western listeners.
"Quantised rates highest" is a finding about those stimuli, not a law. Jazz, samba, Malian drumming
and hip-hop have documented systematic feels (see `research/RHYTHM.md`), and a style built on exact
placement is a style, not a default.

---

# 2. What expert performers actually vary

## Research

- Palmer (1997), "Music Performance", *Annual Review of Psychology* 48: melody events are played
  louder than other chord tones and precede them by roughly 20–50 ms; asynchronies are larger on
  strong metrical beats; deviations are systematic and reproducible across performances.
- Repp (1992), *JASA* 92, on 28 performances of one Schumann piece: ritardandi occur at the ends of
  major structural sections, and within-gesture ritardandi follow a parabolic timing function.
- Repp (1996), *JASA* 100: melody lead of about 30 ms; the highest notes lead and inner voices lag.
- Goebl (2001), *JASA* 110(1): the ~30 ms melody lead measured at hammer–string contact nearly
  disappears at finger–key contact. **The louder note simply arrives first**, so melody lead is
  largely a consequence of dynamic differentiation in the piano action.
- Todd (1992), *JASA* 91(6): a coupled tempo and dynamics arch, "the faster the louder, the slower
  the softer", described for some classical and romantic styles.
- Friberg, Bresin & Sundberg (2006), "Overview of the KTH rule system for musical performance",
  *Advances in Cognitive Psychology* 2(2): performance rules grouped as phrasing, micro-level timing,
  metrical patterns and grooves, articulation, tonal tension, intonation, ensemble timing, and
  **performance noise as the last and smallest element**. Rule quantities select expressive character.
  (Individual rule names are **to verify**.)
- Bresin & Friberg (2000), *Computer Music Journal* 24(4): emotion-specific rule settings (anger,
  fear, happiness, sadness, tenderness, solemnity) alter tempo, sound level, articulation and onset
  timing.

## Skill translation

The Performance Director builds a plan in this order, which mirrors the KTH grouping: phrase shape
first, metre and articulation next, ensemble relationships after that, and a small noise layer last
if at all.

Goebl's finding is why the schema derives chord asynchrony from velocity rather than storing a fixed
millisecond value, and why the guide warns against copying a piano figure to strings, synths or voices.

---

# 3. Groove and swing are tempo-dependent

## Research

- Friberg & Sundström (2002), *Music Perception* 19(3): the ride-cymbal swing ratio falls from about
  3.5:1 at slow tempi toward 1:1 at fast tempi; the short note stays near 100 ms across medium to
  fast tempi. A 2:1 ratio occurs at one tempo, not as a general rule.
- Danielsen (ed., 2010), *Musical Rhythm in the Age of Digital Reproduction*: the **beat bin** — the
  beat is a span rather than a point, and the shape of the sound determines where the beat is felt.
  Onset-only measurement cannot see this.

## Skill translation

`shared/RHYTHM_SYSTEMS/MICROTIMING_AND_GROOVE.md` holds a swing table by tempo. The Producer and Mix
Engineer are told that envelope shape moves felt placement, so a timing problem is sometimes a
transient problem.

---

# 4. MIDI expression: three tiers

## Research

- MIDI Polyphonic Expression 1.0 (MIDI Manufacturers Association, March 2018): a Lower Zone with
  master channel 1 and an Upper Zone with master channel 16; per-note pitch bend, channel pressure
  and CC74 on member channels; default per-note bend range **±48 semitones**, master ±2, configurable
  through RPN 0; zones declared by an MPE Configuration Message; at most 15 simultaneously expressive
  notes in a single zone. At 14-bit resolution, ±48 gives roughly 0.586 cents per unit.
- MIDI 2.0: 16-bit velocity, 32-bit controllers, native per-note pitch bend, registered and assignable
  per-note controllers, note-on attributes.
- MIDI Tuning Standard: bulk tuning dump and request, single-note tuning change in real time, and
  scale/octave tuning in 1-byte and 2-byte forms; frequency data as a semitone byte plus a 14-bit
  fraction, an effective resolution near 0.0061 cents.
- A Standard MIDI File carries MPE only implicitly, through preserved channel numbers, and cannot
  carry MIDI 2.0 per-note controllers or 16-bit velocity.

## Skill translation

```text
tier 1   MIDI 2.0 per-note controllers      when the target supports them
tier 2   MPE zone, per-note bend and CC74   when the target is an MPE instrument
tier 3   MIDI 1.0 channel CC and bend       the portable fallback
```

`shared/TUNING_AND_MPE.md` defines the downgrade path, and MIDI Builder states which tier it used.
Pitch intent is stored in cents so that it survives the choice of tier. Bend range is always declared
alongside bend data, because a receiver that assumes ±2 will play a ±48 gesture as noise.

---

# 5. Sample-library grammar

## Research

Read in full: the Spitfire Symphonic Strings user manual. Read as excerpts: Spitfire BBC Symphony
Orchestra manuals, Orchestral Tools SINE help pages, Native Instruments Kontakt documentation,
Vienna Symphonic Library Academy articles, Cinematic Studio Series manual.

The shared grammar across these products:

- long notes take dynamics from a continuous controller (commonly CC1) which **crossfades recorded
  dynamic layers**; a fader that only changes volume is not the same thing;
- CC11 is an expression trim, distinct from dynamics;
- short notes take dynamics from velocity, and often select the articulation as well;
- legato patches are monophonic and require **overlapping notes** to trigger a recorded transition;
  in one documented library the velocity of the arriving note selects the transition type;
- transitions have latency, documented in one library as roughly 50–300 ms, compensated with a
  negative track delay;
- round robins exist to prevent the machine-gun effect and must not be reset at every bar;
- release samples need real note-offs, so a part written with notes glued end to end loses them.

## Skill translation

This grammar is general and lives in `shared/VIRTUAL_INSTRUMENT_GUIDE/`. The exact controller numbers,
velocity ranges and latencies are **per product**, so they live in calibration profiles
(`shared/PLUGIN_CALIBRATION_SCHEMA.md`) and never in a skill file.

---

# 6. Physical feasibility

## Research and craft

- Drums: two hands and two feet. Documented programming guidance places ghost notes around velocity
  40–70 with a different sample rather than a quieter one, treats hi-hat openness as a continuous
  controller, and implements chokes through note-off or aftertouch depending on the product.
- Guitar: one note per string, a comfortable span of about four frets in low positions; strums have a
  direction and a temporal spread; the spread in milliseconds is a practitioner default, **not a
  measured figure**, because no source giving one could be opened.
- Winds and brass: a phrase is a breath; embouchure fatigue accumulates; attack character changes with
  dynamic and register; a swell is a timbre change, not a volume fade, because brass spectra brighten
  with dynamic (physics reference **to verify**).
- Voice: consonants are placed before the beat so the vowel lands on it; vowel intelligibility falls
  as the fundamental rises past the first formant (Sundberg, **to verify**).

## Skill translation

The Performance Director returns a `feasibility_report` before anything is written: impossible
voicings, limb collisions, breath overruns, out-of-range notes. A part can still be written when the
brief wants the impossible; the report says so rather than silently allowing it.

---

# 7. Deliberate imperfection with a reason

Every imperfection in the schema names its cause:

| Entry | Cause |
|---|---|
| `melody_lead` | louder note reaches the string first (Goebl 2001) |
| `phrase_arch` | tempo and dynamics coupled over a phrase (Todd 1992) |
| `final_ritard` | parabolic slowing at structural ends (Repp 1992) |
| `swing_ratio` | ratio set by tempo (Friberg & Sundström 2002) |
| `drift_1f` | long-range-correlated human fluctuation (Hennig 2011) |
| `double_spread` | two takes are never identical |
| `ensemble_spread` | many players do not attack at one instant |
| `tape_wow`, `tape_flutter` | transport speed variation, slow and fast |
| `flam` | two limbs arriving fractionally apart; magnitude is a practitioner default |

An imperfection with no cause is a bug, not a feature.

---

# 8. Primary sources

- Palmer, 1997 — music performance review
- Repp, 1992; 1996 — expressive timing, onset asynchrony
- Goebl, 2001 — melody lead as a consequence of dynamics
- Todd, 1992 — tempo and dynamics arch
- Friberg, Bresin & Sundberg, 2006 — KTH performance rule system
- Bresin & Friberg, 2000 — emotional colouring of rule settings
- Friberg & Sundström, 2002 — swing ratio against tempo
- Frühauf, Kopiez & Platz, 2013; Davies et al., 2013; Senn et al., 2016 — microtiming and groove
- Hennig et al., 2011; Räsänen et al., 2015 — 1/f structure in human timing
- Butterfield, 2010 — participatory discrepancies questioned
- Danielsen, 2006; 2010 — beat bin, funk microrhythm
- MIDI Manufacturers Association — MPE 1.0 (2018), MIDI Tuning Standard, MIDI 2.0
- Spitfire Audio, Orchestral Tools, Native Instruments, Vienna Symphonic Library, Cinematic Studio —
  product manuals and public academies
