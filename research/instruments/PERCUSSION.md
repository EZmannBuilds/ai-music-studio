# Percussion (Orchestral): research records

## Scope and method

Forsyth's 1914 *Orchestration* is unusually thorough on this family and was read at section depth
across every relevant chapter (kettle-drums, side drum, bass drum, cymbals, gong, triangle,
tambourine, castanets). Rimsky-Korsakov's *Principles of Orchestration* was read for timpani range
and the register grouping of unpitched instruments; its printed range tables for glockenspiel,
celesta, and xylophone did not survive plain-text extraction from the source scan (image-only
tables) and are not used here (they belong to `MALLETS.md` regardless). Two of Sofia Dahl's studies,
already read for `DRUM_KIT.md`, are reused where their findings (rebound physics, accent timing) apply
identically to the orchestral snare, which is mechanically the same instrument. One page of Jim
Woodhouse's *Euphonics* acoustics text, also reused from `DRUM_KIT.md`, supports the timpani
strike-position claim. Two university percussion-studio pages (BYU) were read for woodblock and
temple blocks, which neither Forsyth nor Rimsky-Korsakov cover (both instruments entered standard
orchestral use later than 1914). Fletcher and Rossing was not reachable in full and is cited only as
`standard-reference`/`to-verify`. A search for a modern practitioner source giving concrete timpani
retuning times (with and without a tuning gauge) did not turn up anything read at section depth that
the page could cite with confidence, so no number is given for retuning speed.

## Records

### PERC-01 Timpani strike position and pitched-mode physics
- claim: a timpanist strikes about halfway between rim and centre; striking near the centre
  maximises unpitched, axisymmetric modes and gives little of the tuned modes, all of which have a
  nodal line through the centre.
- source: FORSYTH-1914 (section, strike position as practitioner observation); WOODHOUSE-TUNED-DRUMS
  (section, the physical mechanism)
- source_type: orchestration (Forsyth); academic acoustics (Woodhouse)
- confidence: high
- scope: timpani specifically; the mode-shape mechanism is general to any circular tuned membrane
- limitations: high for both the strike-position practice (Forsyth) and the general physics as stated
  for timpani (Woodhouse). Woodhouse's page does not discuss the exact fraction of the radius that
  best balances pitched and unpitched content, only the direction of the effect
- inference: none beyond combining a 1914 practitioner observation with a modern acoustics mechanism
  for why it works

### PERC-02 Kettle-drum historical and practical range
- claim: the historical two-drum set covered Bb2-F3 (small) and F2-C3 (large), a perfect fourth/fifth
  relationship; Rimsky-Korsakov recommends a composer rely on roughly E2-G#3 across a modern set, and
  notes a specially made very small drum reaching Db4.
- source: FORSYTH-1914 (section); RIMSKY-1913 (section)
- source_type: orchestration (both)
- confidence: high
- scope: early-20th-century orchestral practice; modern timpani sets (with pedal mechanisms and
  standardised drum sizes) may have somewhat different practical extremes, not verified here
- limitations: high as historical/pedagogical guidance from two independent orchestration texts of
  the same era; both sources predate modern pedal timpani as the default, and the ranges given are
  representative rather than a current manufacturer specification
- inference: none

### PERC-03 Orchestral snare drum: wire mechanism, pressed roll, and sticking vocabulary
- claim: (a) the snare wires buzz against the snare head and roughly double the perceived pitch
  versus the drum unsnared; (b) Forsyth describes the roll as double alternate strokes per hand
  (LL-RR, the "daddy-mammy"), not one hand holding a continuous buzz; the PAS rudiments list that
  open double-stroke roll and the multiple-bounce (closed) roll as separate rudiments, both hand to
  hand; (c) flam, drag, and paradiddle are
  named, distinct sticking techniques, with the paradiddle specifically a sticking pattern (not a
  rhythm) that secures alternating hand attack on successive strong beats.
- source: FORSYTH-1914 (section); PAS-RUDIMENTS-1984 (full)
- source_type: orchestration
- confidence: high
- scope: orchestral/military side drum technique as documented in 1914, and the rudiments as
  published by the PAS; that a smooth modern orchestral closed roll is usually multiple-bounce is
  inference, not stated by either source; the same physical instrument
  and technique are used on a drum kit, per `DRUM_KIT.md`
- limitations: all three claims are stated plainly and are internally consistent with modern drumming
  pedagogy's description of the same techniques (cross-checked informally against the drum-kit
  sources in `research/sources/INSTRUMENT_SOURCES.md`, not independently re-verified in an orchestral-snare-specific
  modern source). A single early-20th-century source; not cross-checked against a modern PAS resource
  specific to orchestral (as opposed to kit) snare technique
- inference: none for the core claims; the note that this corrects the SPEC-identified error ("pressed
  rather than alternated," implying the two are opposites) is this page's own framing

### PERC-04 Accent preparation height, velocity, and timing
- claim: accented strokes are prepared from greater height and struck at higher velocity than
  unaccented strokes, and the interval before an accent is measurably lengthened, more so at softer
  dynamics.
- source: DAHL-2004-ACCENT (section); mechanism further described in DAHL-2003-THESIS (section)
- source_type: academic acoustics/perception
- confidence: medium
- scope: general stick-percussion technique, not orchestral-snare-specific; extended to the orchestral
  snare on the reasoning that it is the same physical technique studied
- limitations: as DK-05 in `research/instruments/DRUM_KIT.md`, which this record's confidence rating follows
- inference: applying a kit/general-percussion finding to the orchestral snare specifically

### PERC-05 Bass drum: no definite pitch, illusory pitch from sympathetic reinforcement
- claim: a struck bass drum has no definite pitch of its own; an apparent pitch sometimes heard is an
  illusion caused by the drum's strongest partials coincidentally reinforcing the orchestra's
  prevailing bass note, not a real, constant pitch of the instrument.
- source: FORSYTH-1914 (section)
- source_type: orchestration
- confidence: medium
- scope: orchestral bass drum, early-20th-century instruments; the physical account (coincidental
  partial reinforcement) is general acoustics reasoning consistent with how any resonant body could
  appear to "ring along" with a strong nearby pitch, but this specific claim was not cross-checked
  against a modern acoustics source
- limitations: stated plainly by Forsyth as "matter of general observation," which is a
  practitioner's empirical account rather than a measured acoustic study; no measured data, only
  practitioner observation
- inference: none beyond Forsyth's own account

### PERC-06 Tam-tam: single-blow failure and the graduated-attack requirement
- claim: a single heavy blow on a tam-tam produces a dull, unpleasant, low-power sound; achieving the
  instrument's characteristic "strange and imposing" tone requires a continual, persistent, graduated
  attack (a sustained rolling build), and the instrument is correspondingly difficult to use for more
  than a single soft-to-moderate stroke, or a graduated crescendo roll, per work.
- source: FORSYTH-1914 (section)
- source_type: orchestration
- confidence: medium
- scope: orchestral concert tam-tam use, early 20th century; the underlying claim (that a single sharp
  impact excites the plate's modes less effectively than a sustained, building stroke) is physically
  plausible and consistent with how large, thick metal plates are generally excited, but was not
  independently verified in an acoustics source this pass
- limitations: a plainly and specifically stated practitioner claim, but no acoustic measurement
  backs it; a single practitioner-orchestrator's account
- inference: the framing of this as a direct instance of `COMMON_ERRORS.md` item 10 (a swell must not
  be a volume fade on a static sample) is this page's own extrapolation, not stated by Forsyth, who
  is describing real-instrument technique rather than virtual programming

### PERC-07 Triangle: dynamic range, odd-grouping convention, and sparing use
- claim: the triangle is effective across an unusually wide dynamic range for its size, asserting
  itself even in a full tutti fortissimo while also working at ppp against soft strings and winds;
  grouped rapid strokes are conventionally written in odd numbers so the accent lands in the same
  (right-to-left) beating direction as the group began; the most effective orchestral triangle parts
  on record are extremely short.
- source: FORSYTH-1914 (section)
- source_type: orchestration
- confidence: high
- scope: orchestral triangle practice, early 20th century through the Romantic repertoire Forsyth
  cites; likely still broadly true of modern orchestral practice but not independently confirmed in a
  modern source
- limitations: stated plainly with named examples (Meistersinger Overture, Siegfried, Liszt's Eb
  Piano Concerto); none of the modern (post-1914) repertoire is covered
- inference: none

### PERC-08 Tambourine: three (or four) distinct playing techniques
- claim: knuckle strike (detached notes), hoop shake (a jingle-dominated roll), and thumb rub across
  the head (a jingle-dominated partial tremolo) are three genuinely different techniques and sounds;
  a rarer fourth method rests the tambourine on a tuned kettle-drum and strikes it with kettle-drum
  sticks for a muffled-drum tone edged with jingles.
- source: FORSYTH-1914 (section)
- source_type: orchestration
- confidence: high
- scope: orchestral and theatre tambourine use, early 20th century
- limitations: stated plainly with named repertoire examples (Berlioz's *Carnaval Romain*, Elgar's
  *Cockaigne*, Tchaikovsky's *Nutcracker* Arab Dance); none identified beyond the source's age
- inference: none

### PERC-09 Castanets: macho/hembra hand technique versus the mounted orchestral form
- claim: traditional Spanish hand castanets use a larger, simpler-rhythm pair (macho) in the left hand
  and a smaller, full-rhythm pair (hembra) in the right; orchestral and military-band use instead
  mounts a pair at each end of a handle, which Forsyth calls a concession to ensemble practicality
  rather than a full substitute for the hand technique.
- source: FORSYTH-1914 (section)
- source_type: orchestration
- confidence: medium
- scope: early-20th-century orchestral practice; the macho/hembra description is offered as
  background on a tradition this page does not otherwise cover in depth (per this project's own
  routing rules, a living tradition's own vocabulary should ideally come from a practitioner or
  tradition-institution source, not an outside orchestration text)
- limitations: high for the mounted-orchestral-form claim and its framing as a practical substitute;
  lower (hence medium overall) for the specific macho/hembra description, which is a brief aside in a
  source about Western orchestration rather than a Spanish-tradition-specific pedagogical or
  ethnomusicological source. Forsyth is not a Spanish-percussion specialist source; the macho/hembra
  claim should be treated as background context for why the orchestral mounted form exists, not as
  authoritative description of Spanish castanet practice itself
- inference: the page frames orchestral castanets as explicitly out of scope for describing the living
  hand-castanet tradition in depth, consistent with this project's tradition-routing rules

### PERC-10 Woodblock and temple block construction and playing technique
- claim: a woodblock is a single hollowed hardwood block with a drilled resonance chamber; temple
  blocks are a set of hollow "dragon mouth" wooden blocks (also made in plastic or marine plywood),
  typically tuned as a set (commonly five blocks in a pentatonic relationship, though whole-tone,
  diatonic, and chromatic sets exist), played with soft rubber mallets at the block's edge, and have
  less cutting power than a plain woodblock.
- source: BYU-WOOD-BLOCKS (section); BYU-TEMPLE-BLOCKS (section)
- source_type: pedagogy (university percussion studio resource)
- confidence: medium
- scope: Western concert-percussion practice
- limitations: a teaching-studio reference page, not a peer-reviewed or tradition-institution source,
  though consistent in substance with general percussion-instrument knowledge; brief pages, not
  exhaustive; roll technique and idiomatic figuration on either instrument were not covered in the
  source and are left as `inference` in the page
- inference: sustain/decay behaviour, phrase limits, and virtual-programming rows are this page's own
  reasoning from the construction facts, not stated in either BYU source

## Corrections to the 2.0 page

- **"Rolls are pressed rather than alternated" (old PERCUSSION.md line 57) is corrected.** Every roll
  alternates hands. Forsyth (1914) describes the double-stroke roll; the PAS rudiments distinguish it
  from the multiple-bounce (closed) roll. The integration review also corrected this pass's first
  draft, which had presented Forsyth's double-stroke roll as the closed roll. See PERC-03.
- **Roll rates are human properties and are not deferred to calibration**, which measures a patch, not
  a player (`shared/PLUGIN_CALIBRATION_SCHEMA.md`, Rules). No source read this pass gave a
  strokes-per-second figure with enough context to state as a guide-level fact, so the page marks it
  to verify.
- **CC dynamics for rolls and swells, and release samples, were added** as explicit rows across every
  card (previously largely absent), most substantively for the tam-tam, where the graduated-swell
  requirement is a direct, sourced correction to treating the instrument as a single loud/soft sample.
- **Timpani pedal glissando, tuning time, head resonance/damping, and mallet choice** were added per
  the brief, sourced to Forsyth for the audible-pitch-bend-during-a-ringing-head observation and to
  Woodhouse for the strike-position mode physics; exact tuning-time figures were searched for and not
  found at section depth, so none is printed.

## Still to verify

- Modern timpani retuning time, with and without a tuning gauge, from a percussion-pedagogy source
  read at section depth (not found this pass).
- Cymbal, drumhead, and gong decay spectra, and why some struck metal idiophones (tam-tam, gong)
  resist a single-blow attack while others (cymbal, triangle) do not: Fletcher and Rossing, not
  opened.
- Whether the macho/hembra castanet description (PERC-09) matches current Spanish/flamenco
  practitioner terminology; this page deliberately does not attempt a fuller account, consistent with
  keeping living-tradition description out of an orchestration-text-sourced page.
- Roll rates in strokes per second, by instrument and dynamic: still absent, as in the 2.0 page.
