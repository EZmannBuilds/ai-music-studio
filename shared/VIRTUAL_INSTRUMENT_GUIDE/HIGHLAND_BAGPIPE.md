# Highland Bagpipe

Traditions: Scottish Great Highland bagpipe (a' phìob mhòr) solo and pipe band practice. Context:
`shared/MUSICAL_SYSTEMS/DRONE_TRADITIONS.md`.

This page covers the Great Highland bagpipe: chanter, drones, tuning and the gracenote-embellishment
system that substitutes for breath articulation on a continuously sounding reed instrument. It does
not cover other bagpipes (uilleann pipes, Scottish smallpipes, Northumbrian pipes, gaida and others),
which are separate instruments with their own construction and repertoire.
`shared/MUSICAL_SYSTEMS/DRONE_TRADITIONS.md` already covers this instrument's place among drone
traditions generally, including the just-intonation chanter model and the pitch-history figures this
page also cites directly from the same primary source; this page adds embellishment technique,
construction detail and programming guidance that file does not cover, and links to it rather than
repeating its drone-theory content.

> Evidence: read at full depth: a piping-magazine article giving measured chanter and drone pitch
> figures across a century and naming competing tuning schools [MACPHERSON-1998], and a piping-press
> article built from named teachers' and judges' own testimony about embellishment technique
> [PIPINGPRESS-FINGERING-2020]. Read at section depth: a trade-publication article on drone and
> chanter acoustics, whose acoustic content is cited and whose uncited speculative prehistory is not
> [BAGPIPENEWS-TUNING-2020], and a self-published tutor's embellishment chapters
> [HEINEMAN-TUTOR]. Source IDs resolve in `research/sources/INSTRUMENT_SOURCES.md`; the claims and
> their limits are recorded in `research/instruments/HIGHLAND_BAGPIPE.md`.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## Behaviour cards

### Great Highland Bagpipe (chanter and drones)

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A double-reed conical-bore chanter plus three single-reed cylindrical drones (one bass, two tenor), all fed continuously from a bag the player keeps pressurised by arm pressure between breaths blown in through a blowpipe; the chanter's conical bore is acoustically why it produces both odd and even harmonics, while each drone, closed at the reed end and open at the other, behaves as a stopped pipe whose harmonic content is dominated by odd harmonics. | sourced: BAGPIPENEWS-TUNING-2020 |
| attack_behavior | The chanter has no true silent attack in the sense a stopped wind instrument has: because the reed sounds continuously as long as the bag is pressurised, a note "starts" only by fingering a new pitch while the air column keeps sounding, so a clean attack on a repeated note is produced by a gracenote figure (see articulation_logic), not by breath or tonguing. | sourced: HEINEMAN-TUTOR + inference |
| sustain_behavior | Continuous for as long as fingering is held and the bag stays pressurised; the drones sustain constantly through an entire performance once started, providing the fixed reference the chanter is tuned against. | sourced: MACPHERSON-1998 |
| release_behavior | A note "ends" only when the fingering changes to the next note or a gracenote figure intervenes; there is no independent note-off the way a struck or bowed instrument has one, since the reed keeps sounding. | inference |
| dynamic_timbre_change | Not addressed in detail by a source read this pass; blowing pressure is understood to affect chanter reed response and overall volume, but no source read this pass measures or describes a specific timbral change with dynamic level on this instrument. | to-verify: how chanter or drone timbre changes with blowing pressure, not opened this pass |
| register_character | The chanter's fixed nine-note compass (low G up to high A) has no dynamically weak notes in the sense a wind instrument's upper or lower extreme might; MacPherson's tuning discussion instead treats individual notes (D, high G, high A) as harder or easier to tune cleanly against the drones, which is a tuning-difficulty distinction, not a loudness or register-strength one. | sourced: MACPHERSON-1998 |
| practical_range | Nine notes on the chanter: low G, low A, B, C, D, E, F, high G, high A, sounding (not written separately from sounding pitch, since pipe music is notated at the instrument's own sharp pitch rather than transposed); the drones sound continuously at low A and the two octaves' relationship to it, well below and around the chanter's own low A. | sourced: MACPHERSON-1998 |
| tessitura | Not meaningfully distinct from practical_range on a nine-note fixed-compass instrument with no dynamic range by register; not addressed further by a source read this pass. | inference |
| articulation_logic | Because the chanter cannot be silenced note to note, gracenote figures are the instrument's articulation system, not ornamentation added to an otherwise separately-articulated line. Named figures include doublings (a family of short gracenote figures, one per melody note), the birl (a Low A-Low G-Low A figure, playable by more than one physical technique -- tap, down-up, tap-and-pull, tap-and-push -- per player preference), the great birl (a birl with an added high-G gracenote), the leumluath or grip (Low G, D gracenote, Low G, then the melody note), the taorluath (a leumluath/grip plus an E gracenote on Low A) and the D throw (Low A, Low G, then a D-C-D figure). Real, named disagreement exists among prominent teachers over some figures' exact execution (for example, whether a D taorluath or D throw takes a D or a B gracenote), which this page states as documented variation, not as one settled standard. | sourced: HEINEMAN-TUTOR; PIPINGPRESS-FINGERING-2020 |
| phrase_limits | Bounded by the player's ability to keep the bag pressurised via arm pressure between breaths, not by breath directly, since the reservoir of air in the bag decouples phrase length from breath length far more than on a free-reed or open-reed wind instrument; not quantified by a source read this pass. | to-verify: typical sustainable phrase length or breathing-cycle interval, not opened this pass |
| transitions | No legato in the sense of a bowed or blown instrument's slur; the chanter's continuous sound means every note change is itself a kind of transition, and gracenote figures both articulate repeated notes and smooth or mark transitions between different notes. | inference |
| repeated_note_behavior | A repeated melody note is separated by a gracenote figure (most simply a doubling), since there is no breath or tonguing mechanism to re-articulate it; the specific figure used depends on the note and the surrounding phrase. | sourced: HEINEMAN-TUTOR |
| vibrato | Not applicable; the chanter has no vibrato mechanism, and traditional pipe music does not use one. | inference |
| pitch_instability | Not applicable in the sense of a bowed or blown instrument's pitch bending; the chanter's nine notes are fixed by fingering and reed, with tuning adjustment (see the "Tuning" section below) a separate, pre-performance matter rather than an in-note technique. | inference |
| resonance | The bass and two tenor drones sound continuously throughout performance and are the instrument's defining resonant reference: chanter notes are tuned to form recognisable harmonic relationships (small-whole-number ratios) against the drones' own harmonic content, and a piper tunes by listening for beating between chanter and drone harmonics. | sourced: MACPHERSON-1998; BAGPIPENEWS-TUNING-2020 |
| physical_noise | Not addressed in detail by a source read this pass beyond the general mechanism of reed and bag; no source read this pass describes specific incidental noises (bag creak, blowpipe valve click) as part of the instrument's audible identity. | to-verify: whether incidental mechanical noise is considered part of the instrument's normal sound, not opened this pass |
| feasibility | Two hands finger the chanter (no separate valve or key mechanism beyond the finger holes in the traditional instrument); the player simultaneously maintains bag pressure by arm and blowing; a chanter figure requiring fingers faster than a real player's hands can move, or continuing to play through a bag-pressure failure, is not playable. | inference |
| ensemble_behavior | Solo piobaireachd (ceòl mòr) is unaccompanied; pipe bands play chanters in unison with massed drones, which the sources read this pass do not describe the tuning or ensemble mechanics of in detail. | sourced: BAGPIPENEWS-TUNING-2020 + to-verify: not opened this pass |
| recording_behavior | Not addressed by a source read this pass. | to-verify: conventional close-mic or room approach for solo or pipe-band recording, not opened this pass |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | The chanter has no independent note-off the way a struck or bowed instrument does (release_behavior above); a virtual chanter's "note length" is really about when the next fingering or gracenote figure begins, not about a decay the sample needs room for. | inference |
| overlap | Continuously sounding in the sense that there is no rest between notes in normal playing (the reed never stops); a virtual patch that inserts silence between notes misrepresents the instrument's basic acoustic behaviour, per the task's own framing of this exact failure. | sourced: MACPHERSON-1998 + inference |
| velocity | Not the instrument's real expressive control in the sense it is for a struck or plucked instrument; the chanter has essentially one dynamic level in practice (bag pressure is kept steady to hold pitch, since pitch and pressure are linked on a reed instrument), so velocity's main use on a virtual instrument is likely to be gracenote or articulation selection rather than loudness. | to-verify: whether any real dynamic range exists in practice and how it is controlled, not opened this pass |
| continuous_dynamics | Not addressed by a source read this pass; given the pitch/pressure link noted under velocity, a continuous dynamics control that changes chanter pitch as a side effect would misrepresent the instrument, but this page has not verified the extent of that link with a source this pass. | to-verify: the practical relationship between blowing pressure, dynamics and pitch stability, not opened this pass |
| expression | Not addressed by a source read this pass. | to-verify: not opened this pass |
| articulation_switching | Each named gracenote figure (doubling, birl, great birl, leumluath/grip, taorluath, D throw, and others) needs its own distinct, correctly fingered figure, not a generic "grace note" or trill effect; a patch or notation approach that reduces all of these to one ornament type loses the instrument's real articulation system. | sourced: HEINEMAN-TUTOR |
| round_robins | Not addressed directly by a source read this pass; general reasoning (repeated gracenote figures in a fast tune are exposed to identical-sample fatigue the way any repeated short figure is) plausibly applies but is not independently sourced for this instrument. | inference |
| release_samples | Given there is no true note release on this instrument (release_behavior above), a "release sample" in the sampler sense is likely inapplicable, but this was not directly addressed by a source read this pass. | to-verify: not opened this pass |
| pedal_or_breath_behavior | The bag, not the player's breath directly, is what sustains sound between breaths; a virtual instrument's breath or sustain control should model bag pressure (decaying slowly between breaths, refilled on each breath) rather than a wind instrument's direct breath-to-sound mapping. | sourced: MACPHERSON-1998 + inference |
| transition_samples | Gracenote figures are the tradition's real "transition" vocabulary between notes (see articulation_logic and articulation_switching); a generic legato or portamento transition sample, of the kind built for a bowed or blown melodic instrument, does not represent how this instrument moves between notes. | sourced: HEINEMAN-TUTOR + inference |
| mic_or_room_behavior | Not addressed by a source read this pass. | to-verify: not opened this pass |
| likely_fake_sounding_errors | Gaps or silence between notes, which the real instrument's continuously sounding reed does not produce; a single generic "grace note" or trill effect standing in for the specific named gracenote figures (doubling, birl, taorluath, and the rest), which collapses a real, named articulation system into decoration; tuning the chanter to 12-tone-equal A440 rather than to its own sharp pitch and internal scale relationships; velocity-driven dynamics that imply a wind-instrument-style loudness range the real chanter does not straightforwardly have. | sourced: MACPHERSON-1998; HEINEMAN-TUTOR |
| organic_programming_methods | Model the chanter as continuously sounding with no rests except where a gracenote figure or phrase boundary calls for one, per `shared/HUMAN_PERFORMANCE_SCHEMA.md`'s general note-overlap guidance applied to a drone-and-chanter instrument; use the specific named gracenote figure a passage calls for, not a generic ornament; tune chanter and drones to the instrument's own sharp reference pitch and internal interval relationships (see "Tuning" below), routed through `shared/TUNING_AND_MPE.md`, not to 12-tone-equal A440. | sourced: MACPHERSON-1998; HEINEMAN-TUTOR |

---

## Tradition and context

### Construction

A double-reed, conical-bore chanter plus three single-reed, cylindrical-bore drones (one bass, two
tenor), all supplied with continuous air from a bag the player keeps pressurised by arm pressure
between breaths blown in through a blowpipe (the traditional instrument's mouth-blown form; bellows-
blown variants exist in other bagpipe traditions but were not addressed by a source read this pass
for the Highland pipe specifically). The chanter's conical bore is the acoustic reason it produces
both odd and even harmonics; each drone's cylindrical, one-end-closed geometry is why it behaves as a
stopped pipe dominated by odd harmonics. [sourced: BAGPIPENEWS-TUNING-2020]

### Tuning

The instrument's reference pitch, conventionally called "A," is substantially sharper than concert
A440 and has risen over roughly the past century: about 441 Hz measured on one chanter in 1885, an
average of about 459 Hz across several chanters in the mid-1950s, and 470 to 480 Hz for low A on
1990s chanters, per named measurement studies MacPherson cites. **Treat any single figure as the
measurement of a date, not as a fixed fact about the instrument**; a 2020 trade-publication source
read this pass independently states "about 459 cps" as its own "current" figure, lower than
MacPherson's 1990s figure, which itself illustrates the point. Against that reference, the chanter's
nine notes form a scale close to a major scale with a flattened seventh (Mixolydian, starting from
low A), except that the notes conventionally written as "C" and "F" actually sound closer to C-sharp
and F-sharp. Two of the nine notes, D and high G, are tuned by more than one named scheme rather than
one settled standard: a simple whole-number-ratio ("just") tuning puts D at a 4:3 ratio above low A
and high G at 16:9; a 1954 study of eighteen chanters found a sharper D (27:20) and high G (9:5) in
use; and more recent recordings, per MacPherson's own analysis, show a shift back toward the simple
just D and toward a flatter high G (around 7:4, which MacPherson calls "Harmonic" because its
harmonics coincide with the bass drone's seventh harmonic). High A is conventionally tuned 10 to 30
cents flat of a true octave above the drones, by convention or taste rather than acoustic necessity.
**Never tune this instrument to 12-tone-equal A440**, and never present one of these named schools as
the only correct tuning. See `shared/MUSICAL_SYSTEMS/DRONE_TRADITIONS.md` for the just-intonation
framing in more theoretical depth. [sourced: MACPHERSON-1998]

### Note production and technique

The chanter and drones sound continuously once the bag is pressurised; there is no breath-driven
attack or release the way a flute or clarinet has one. Because of this, the instrument's real
articulation system is a set of named gracenote figures, fingered at speed, rather than tonguing or
breath control: doublings (one short figure per melody note), the birl, the great birl, the leumluath
(grip), the taorluath and the D throw are the core named figures, each with its own specific
fingering. [sourced: HEINEMAN-TUTOR]

### Idiomatic phrasing and ornamentation

Ornament here is not decorative in the usual sense: because the chanter cannot be silenced note to
note, a gracenote figure is frequently the only way to separate two statements of the same pitch or
to mark a clean attack, which is exactly the structural role
`shared/VIRTUAL_INSTRUMENT_GUIDE/CULTURALLY_SPECIFIC_INSTRUMENTS.md` step 2.3 describes for
ornament-as-articulation traditions generally. Real disagreement exists among prominent named
teachers about some figures' exact execution: whether a D taorluath or D throw takes an additional D
gracenote or a B gracenote is a documented point of dispute among named twentieth-century teachers
and competition judges, not a settled universal rule, and this page does not resolve it in either
direction. [sourced: HEINEMAN-TUTOR; PIPINGPRESS-FINGERING-2020]

### Performer interaction and ensemble role

Solo piobaireachd (ceòl mòr) is performed unaccompanied. Pipe bands play multiple chanters in unison
against massed drones; the mechanics of tuning and ensemble blend specific to pipe-band practice were
not addressed in detail by a source read this pass. [sourced: BAGPIPENEWS-TUNING-2020 + to-verify: not opened this pass]

### Repertoire contexts

Two broad repertoire categories are named in piping generally: ceòl mòr ("great music," piobaireachd),
the instrument's extended formal solo repertoire, historically taught and memorised through
canntaireachd, a system of sung vocables representing the tune and its gracenotes in the absence of a
dedicated written notation for the style; and ceòl beag ("small music": marches, strathspeys, reels,
jigs and related dance and march forms). This page's sources confirm the ceòl mòr/canntaireachd
naming at only low confidence (one trade-publication source, with no citation for the historical
claims it makes around that naming); the ceòl beag/ceòl mòr distinction itself was not independently
confirmed by a source read at section depth this pass, despite being well-established general piping
knowledge, and is accordingly marked to-verify rather than sourced. [standard-reference: BAGPIPENEWS-TUNING-2020 + to-verify: not
confirmed at section depth by a source read this pass]

### Improvisation

Not addressed by any source read this pass. [to-verify: whether and how improvisation figures in
either ceòl mòr or ceòl beag performance, not opened this pass]

---

## What the instrument is

A double-reed, conical-bore chanter plus three continuously sounding single-reed drones (one bass,
two tenor), all fed from a bag the player keeps pressurised between breaths; a fixed nine-note
chanter compass tuned to its own sharp reference pitch rather than to concert pitch, articulated
entirely through named gracenote figures because the reed itself never stops sounding. [sourced: MACPHERSON-1998; BAGPIPENEWS-TUNING-2020]

## Range and register

Nine chanter notes (low G to high A), sounding at the instrument's own sharp reference pitch; see
"Tuning" above for the specific interval relationships and how far that reference pitch has moved
over the past century. [sourced: MACPHERSON-1998]

## Articulation and note transitions

See articulation_logic above: gracenote figures (doublings, birl, great birl, leumluath/grip,
taorluath, D throw) are the instrument's real articulation system, with documented, named variation
in exact execution among prominent teachers. [sourced: HEINEMAN-TUTOR; PIPINGPRESS-FINGERING-2020]

## Physical constraints

Two hands on the chanter; simultaneous arm pressure on the bag and breath through the blowpipe to
maintain sound; a gracenote figure faster than a real player's fingers can execute, or continuing
sound through a bag-pressure failure, is not playable. [inference]

## Phrase behaviour

Bounded by the player's ability to keep the bag pressurised between breaths, which decouples phrase
length from breath length more than on an open-reed wind instrument; not quantified by a source read
this pass. [to-verify: typical sustainable phrase or breathing-cycle length, not opened this pass]

## Ensemble behaviour

Solo (unaccompanied piobaireachd) versus pipe-band (unison chanters over massed drones) are the two
named contexts; pipe-band-specific ensemble mechanics were not addressed in detail by a source read
this pass. [sourced: BAGPIPENEWS-TUNING-2020]

## Recording behaviour

Not addressed by a source read this pass. [to-verify: not opened this pass]

## Programming it: the control model

```text
tuning: the instrument's own sharp reference pitch (historically documented between roughly 440 and
  480 Hz for low A, rising over a century) and its internal Mixolydian-like interval relationships,
  never 12-tone-equal A440; route through shared/TUNING_AND_MPE.md
continuous_sound: no rests between notes in normal chanter playing; the reed does not stop
articulation: named gracenote figures select articulation, not a generic ornament or grace-note
  effect; each figure (doubling, birl, great birl, leumluath/grip, taorluath, D throw, and others)
  is its own distinct fingering
drones: three continuously sounding reference pitches (one bass, two tenor, all at the chanter's "A")
  that the chanter is tuned against; not a static pad, but the tuning reference itself
```
[sourced: MACPHERSON-1998; HEINEMAN-TUTOR]

## Programming it: what makes it sound real

- Tune the chanter and drones to the instrument's own sharp reference pitch and internal interval
  relationships, not to 12-tone-equal A440, and state which of the named tuning schools (simple just,
  the 1954-survey sharper scheme, or the more recent "Harmonic" high-G practice) a given rendering
  follows, per `shared/TUNING_AND_MPE.md`. [sourced: MACPHERSON-1998]
- Write continuous sound with no rests between notes in normal playing; a gap between notes
  misrepresents the reed's actual behaviour. [sourced: MACPHERSON-1998 + inference]
- Use the specific named gracenote figure a passage calls for (doubling, birl, great birl,
  leumluath/grip, taorluath, D throw), not a generic grace-note or trill effect standing in for all of
  them. [sourced: HEINEMAN-TUTOR]
- Where more than one named execution of a figure exists (for example, a D or B gracenote in a D
  taorluath), state which school or teacher's practice is being followed rather than presenting one
  silently as the only correct version. [sourced: PIPINGPRESS-FINGERING-2020]

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Family- and tradition-specific tells, and the task brief's
own framing names the central one directly: a bagpipe patch played with velocity dynamics and gaps
between notes.

- **Gaps between notes**, the exact failure the task brief names: the real chanter's reed never stops
  sounding in normal playing, so any silence between melody notes misrepresents the instrument at a
  basic acoustic level, not merely a stylistic one. [sourced: MACPHERSON-1998]
- **Velocity-driven dynamics** standing in for the instrument's real expressive control: bag pressure
  is kept steady to hold pitch on a reed instrument, so a virtual chanter with a wide, freely swept
  dynamic range driven by note velocity likely misrepresents how the real instrument's loudness
  actually works, though this page has not independently verified the extent of that link this pass.
  [to-verify: the practical dynamic range and its control mechanism, not opened this pass]
- A single generic grace-note or trill effect standing in for the named gracenote figures (doubling,
  birl, great birl, leumluath/grip, taorluath, D throw), which collapses a real, named articulation
  system used as this instrument's substitute for breath articulation. [sourced: HEINEMAN-TUTOR]
- Tuning to 12-tone-equal A440 rather than to the instrument's own sharp reference pitch and internal
  interval relationships. [sourced: MACPHERSON-1998]

## What virtual implementations commonly get wrong

Two failures compound each other, and the task brief names both directly. First, **gaps between
notes**: a sampled or modelled chanter patch built like a generic wind instrument, with a note-on and
a note-off and a small silence between successive melody notes, misrepresents the physical mechanism
of a bag-driven, continuously sounding reed. The correct model is closer to a legato string or organ
patch (continuous sound, articulated by transitions) than to a tongued wind instrument, though even
that comparison is imperfect since the real articulation mechanism (gracenote figures) is unique to
this instrument's tradition. Second, **velocity as the dynamics control**: giving a virtual chanter a
wide, freely swept dynamic range keyed to note velocity, the way an orchestral wind or brass patch
commonly works, likely misrepresents an instrument whose pitch and blowing pressure are linked closely
enough that pipers keep pressure steady specifically to hold pitch; this page has not independently
verified the size of that effect this pass, but the mechanism itself (pitch instability under pressure
change, which is why steady bag pressure matters) is basic reed-instrument acoustics. [sourced: MACPHERSON-1998 + to-verify: not opened this
pass]

A third, related failure is collapsing the named gracenote system into one generic ornament. Because
these figures are this instrument's actual articulation system, not decoration layered onto an
otherwise separately-articulated line, substituting a single grace-note or trill effect for all of
them removes the mechanism that makes a bagpipe part sound played rather than sequenced. [sourced: HEINEMAN-TUTOR]

## What must not be generalised outside the tradition

- **This page's pitch figures are each one dated measurement or survey, not "the" pitch of the
  instrument.** MacPherson's own century-spanning figures, and the disagreement between his 1990s
  figure and a separately read 2020 source's "current" figure, both illustrate that pipe pitch has
  kept moving and any single number should be treated as dated. [sourced: MACPHERSON-1998]
- **The D-and-high-G tuning schools named here (simple just, the 1954-survey scheme, "Harmonic") are
  named schools of practice, not a progression from wrong to right.** MacPherson frames the more
  recent shift as an observed trend in recordings, not as a correction of earlier practice. [sourced: MACPHERSON-1998]
- **The gracenote-execution disagreements documented in Piping Press are named, individually
  attributed teachers' and judges' practice** (Robert Brown and Robert Nicol as Patrick Molard's own
  teachers; RG Hardie's own naming convention; Seumas MacNeill's correspondence as then-editor of
  Piping Times and former Principal of the College of Piping; the Donald MacPherson competition
  anecdote), not evidence that piping as a whole has settled on one answer. Do not present either side
  of a named disagreement as the single correct standard. [sourced: PIPINGPRESS-FINGERING-2020]
- **Do not extend this page's claims to other bagpipes** (uilleann pipes, Scottish smallpipes,
  Northumbrian pipes, launeddas, gaida and others), which `shared/MUSICAL_SYSTEMS/DRONE_TRADITIONS.md`
  itself lists as separate instruments and repertoires with their own construction. [inference]
- **The ceòl mòr/ceòl beag distinction and canntaireachd's history are stated here at low confidence
  and from one uncited trade-publication source**; do not treat this page's account of their history
  as settled without a stronger source. [standard-reference: BAGPIPENEWS-TUNING-2020]

## Restricted and ceremonial repertoire

No source read this pass identifies any part of the Great Highland bagpipe repertoire as sacred,
ceremonial in the sense of being restricted to particular lineages or communities, or otherwise closed
to outsiders in the way `shared/MUSICAL_SYSTEMS/INDEX.md` rule 5 addresses. Piobaireachd (ceòl mòr) is
described by the sources read this pass as a formal, extended competitive and concert repertoire, not
as a restricted or lineage-held one, and pipe music generally is widely taught, competed and performed
publicly. This page states plainly, however, that it did not specifically seek out a tradition-bearer
source addressing this question directly, so this is an absence of a finding within this pass's
sources, not a confirmed absence of any restriction; the question is treated as open rather than
resolved. [to-verify: whether any specific tune, context (for example, certain funerary or memorial
piobaireachd) or teaching relationship carries restrictions beyond ordinary copyright and competition
convention, per a tradition-bearer or institutional source, not opened this pass]

## What the Performance Director needs from this file

- `articulation_unavailable` is the expected outcome when a general-purpose wind or organ library is
  asked for this instrument's specific named gracenote figures; report it rather than substituting a
  generic grace-note or trill effect.
- Treat "gaps between notes" and "velocity-driven dynamics" as flags on any bagpipe patch or
  performance plan, per "What sounds fake here" above, since both misrepresent the instrument's basic
  acoustic mechanism rather than being a stylistic choice.
- Do not proceed on an unstated tuning-school choice for D and high G, or on an unstated reference
  pitch: per `shared/VIRTUAL_INSTRUMENT_GUIDE/CULTURALLY_SPECIFIC_INSTRUMENTS.md` step 0/2.1, name
  which named school and which reference pitch (with its date, since pipe pitch is a moving target)
  before writing anything, rather than defaulting silently to A440 or to one tuning school.
- Where a gracenote figure's exact execution is contested among named teachers (per "What must not be
  generalised outside the tradition"), record which school or teacher's practice the plan follows,
  per `shared/HUMAN_PERFORMANCE_SCHEMA.md`'s `performance_reference` field.

## Sources and what to verify

Full citations and read depth are in `research/sources/INSTRUMENT_SOURCES.md`; claim-by-claim
evidence and limits are in `research/instruments/HIGHLAND_BAGPIPE.md`. Left open by this pass, in
order of what would most improve the page: pipe-band-specific ensemble and massed-drone-tuning
convention; the practical dynamic range and how it is actually controlled; the ceòl beag/ceòl mòr
distinction and canntaireachd's history, confirmed at section depth against a piping-institution
source rather than one uncited trade-publication article; phrase length and breathing-cycle timing;
recording convention; and whether any part of the repertoire carries restrictions this pass's sources
did not surface.
