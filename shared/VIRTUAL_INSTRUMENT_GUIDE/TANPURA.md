# Tanpura / Tambura

Traditions: Hindustani (North Indian) and Carnatic (South Indian) classical music, where the
instrument is called tanpura and tambura respectively. Context: `shared/MUSICAL_SYSTEMS/RAGA_AND_TALA.md`
 and `shared/MUSICAL_SYSTEMS/DRONE_TRADITIONS.md`.

The tanpura/tambura is the drone instrument of both systems: an unfretted, long-necked plucked
lute whose four (occasionally five) strings are sounded one after another in a continuous cycle
throughout a performance, never playing melody. The bridge physics that makes its sound
distinctive is shared across the family of Indian "flat"-bridge instruments (tanpura, sitar,
veena) and is covered here from acoustics literature. Construction, tuning order and plucking
practice are documented here specifically for Hindustani practice, from a practitioner and a
performer's manual; Carnatic tambura practice was not reached by a comparable source in this pass
and is named, not described, below.

> Evidence: two acoustics lines were read in full or at section depth (C. V. Raman's 1921 founding
> account of the bridge mechanism; a 2018 high-speed-video study from IIT Kanpur; two 2016-2017
> physical-modelling papers from Queen's University Belfast) alongside one ethnomusicology paper
> with named fieldwork (Weisser, Demoucron and Leman, 2012, ITC Sangeet Research Academy) and two
> Hindustani practitioner sources (Ravi Shankar's sitar manual, which gives one page to the
> tamboura; Martin Spaink, a professional tanpura player and jivari-maker, writing on tuning
> practice). Source IDs resolve in `research/sources/INSTRUMENT_SOURCES.md`; claims and their
> limits are recorded in `research/instruments/TANPURA.md`.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## Behaviour cards

### Tanpura / tambura

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Four (sometimes five) metal strings over a large resonant gourd body, excited by plucking; the strings pass over a curved wooden bridge, with a cotton or silk thread (jiva/jivari) inserted between each string and the bridge to set a precise grazing contact. | sourced: RAMAN-1921; PISHARODY-GUPTA-2018 |
| attack_behavior | The pluck itself is soft and produces little immediate transient; the sound instead builds in overtone richness over roughly the first half-second, a "precursor" effect whose spectral centre glides downward as it decays. This only occurs within a narrow range of pluck amplitude: too hard a pluck collapses the effect. | sourced: PISHARODY-GUPTA-2018; VANWALSTIJN-2016 + inference |
| sustain_behavior | Each plucked string rings on its own into the next string's pluck; the instrument produces no continuous excitation (no bow, no breath), so what reads as a sustained drone is the overlapping decay of four strings struck in rotation, each individually decaying while renewed by the next stroke. | sourced: RAMAN-1921; SPAINK-2012 |
| release_behavior | A single string's decay is prolonged and irregular rather than a simple exponential fade: energy visibly migrates between the fundamental and higher overtones during the decay (the jiva's "cascading" effect), with the overtones, not the fundamental, often dominating for a stretch of the decay. | sourced: PISHARODY-GUPTA-2018 |
| dynamic_timbre_change | The instrument is played at one dynamic level, set by touch and by the jiva's adjustment, not by a range of plucking dynamics; a harder pluck does not produce a "louder" version of the same timbre, it destroys the intended jivari effect. | sourced: PISHARODY-GUPTA-2018 + inference |
| register_character | unresolved: no source read in this pass reports how the jivari effect or the instrument's character changes across the range of tunings actually used (the tonic can sit anywhere a player chooses within the singer's or soloist's comfortable range). | to-verify: a practitioner or acoustics source reporting jivari behaviour across a range of tunings/string gauges |
| practical_range | The four strings are tuned to a small set of scale degrees around one octave (see tuning below), not a melodic range; the tonic pitch itself is chosen per performer/singer and is not fixed. | sourced: SPAINK-2012 |
| tessitura | Not applicable in the melodic-instrument sense: the instrument sounds a fixed set of pitches throughout, chosen once per performance. | inference |
| articulation_logic | One articulation only: an open-string pluck with the right-hand index (and sometimes middle) finger, played with a "delicate, and almost un-heard" touch aimed at bringing the string into full, sustained vibration rather than a percussive attack. | sourced: SPAINK-2012 |
| phrase_limits | Not applicable: the tanpura does not phrase melodically. Its "phrase" is the repeating pluck cycle itself, which the player sustains without interruption for the length of the performance. | inference |
| transitions | Not applicable: strings are open (unfretted) and each pluck is a discrete, unpitch-shifted event. | inference |
| repeated_note_behavior | Central to the instrument: the same four pitches repeat in a fixed rotation for the entire performance, each pluck timed by ear against the decay of the previous strings so the four blend into one continuous "harmonic halo" rather than reading as separate attacks. | sourced: SPAINK-2012 |
| vibrato | None; the strings are open and unfretted, so there is no mechanism for pitch vibrato. | inference |
| pitch_instability | unresolved: no source read in this pass measured pitch drift from string tension relaxation, temperature or humidity on the tanpura specifically, though string instruments generally are affected by these. | to-verify: a maker's or acoustics source on tanpura string tuning stability over a performance |
| resonance | The large gourd (or, on some builds, wood) body and doubly-curved bridge are central to the sound; the sympathetic-style, self-resonant behaviour comes from the jiva/bridge interaction on the played strings themselves (the tanpura has no separate sympathetic string set), unlike the sitar's dedicated taraf strings. | sourced: RAMAN-1921; PISHARODY-GUPTA-2018 |
| physical_noise | The buzzing, overtone-rich quality produced by the jiva-bridge contact is the desired tone, not noise to be minimised; distinguishing "the jivari sound" from an incorrectly set, merely rattling contact is a large part of what tuning the instrument by ear means. | sourced: SPAINK-2012 + inference |
| feasibility | Normally played by one dedicated player (sometimes the vocalist or a student) whose sole task for the performance is maintaining the drone; the technique (steady, evenly timed plucking, precise finger placement, and by-ear jiva adjustment) is described by a practitioner as demanding in its own right, not a background task. | sourced: SPAINK-2012 |
| ensemble_behavior | Sounds continuously and unchangingly throughout a performance, underneath the soloist/vocalist, the accompanying melody line (if any) and the percussion; it does not participate in the metric or melodic development, and is the fixed reference the raga's intervals are heard against. | sourced: SPAINK-2012 |
| recording_behavior | unresolved: no source read in this pass discusses how the tanpura is normally close- or room-miked, or how its buzz spectrum interacts with typical recording setups. | to-verify: a recording-engineering source on Hindustani/Carnatic classical sessions |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Each of the four (or five) pitches is a discrete pluck event with a long, irregular, non-exponential decay (see release_behavior); a sampled or modelled patch needs full-length samples or a modelled decay for each string, not a looped sustain. | sourced: PISHARODY-GUPTA-2018 + inference |
| overlap | Not a legato instrument; there is no note-to-note transition to trigger. What must overlap is the four strings' individual decays with each other, in the fixed, by-ear-timed rotation a player uses, so that the ear hears one continuous halo rather than four separate plucks. | sourced: SPAINK-2012 + inference |
| velocity | Velocity/dynamic layering in the sampler sense is largely inappropriate: the instrument is played at essentially one touch, calibrated to the jiva setting: harder is not louder-and-otherwise-the-same, it is a different (wrong) sound. A patch offering only one or two "correct" dynamic layers, rather than a wide velocity-to-loudness curve, is closer to the instrument's real behaviour. | sourced: PISHARODY-GUPTA-2018 + inference |
| continuous_dynamics | unresolved: no source describes a continuous, within-note dynamic control appropriate to the tanpura; the instrument has no such gesture (see dynamic_timbre_change). | to-verify: whether any documented library models the precursor/jivari build-up as a continuous control at all |
| expression | Not applicable in the usual crossfade-trim sense; the "expression" available to a player is entirely in the timing of the pluck cycle and the jiva setting, both of which are set-up decisions, not per-note performance controls. | inference |
| articulation_switching | Not applicable: one articulation only (see articulation_logic). | inference |
| round_robins | Because the same four pitches repeat throughout an entire performance, a sampled patch without round robins (or without a synthesis model reproducing the precursor's amplitude-dependence) will be especially exposed here: COMMON_ERRORS.md item 1 applies with unusual force to an instrument whose entire part is repetition. | inference |
| release_samples | Because the decay itself carries the instrument's identifying spectral evolution (the precursor and cascading overtones), a patch that truncates or loops the sustain rather than playing a full natural decay for each pluck loses the part of the sound that identifies the instrument. | sourced: PISHARODY-GUPTA-2018 + inference |
| pedal_or_breath_behavior | Not applicable: no pedal, no breath mechanism. | inference |
| transition_samples | Not applicable: no fretted or bent transitions between the four pitches. | inference |
| mic_or_room_behavior | unresolved: see recording_behavior. | to-verify: a recording-engineering source on Hindustani/Carnatic classical sessions |
| likely_fake_sounding_errors | A quantised, evenly-spaced, identical-velocity repeating pluck pattern is the single most exposing error here, because the real instrument's whole part is that repetition, made to sound continuous only by the player's by-ear micro-timing between the four strings and the precursor decay of each. A drone rendered as a static pad or a looped sample similarly loses the precursor build and the cascading overtone behaviour that is the instrument's identity. | sourced: SPAINK-2012; PISHARODY-GUPTA-2018 + inference |
| organic_programming_methods | Vary the inter-pluck timing by the same logic a player uses: the cycle is not metronomic, but timed against the decay of the previously plucked strings, longer where a low string (karaj/pancham) needs to "come to full bloom" before the next stroke (a named, source-attested cause, not a random offset); this is closest to the `phrase_arch`/`ensemble_spread`-style reasoning in `shared/HUMAN_PERFORMANCE_SCHEMA.md` section 3, applied to a single instrument's internal cycle rather than to multiple players, and should be logged as a deliberate model, not left as an unexplained humanisation percentage. | sourced: SPAINK-2012 |

---

## Tradition and context

### Construction

The tanpura/tambura is an unfretted long-necked plucked lute with a large resonating body
(traditionally a gourd, tumba, though wood-bodied builds exist) [sourced: RAMAN-1921]. It
commonly carries four playing strings, though five-string instruments exist and give more tuning
options [sourced: SPAINK-2012; SHANKAR-1968]. Tuning uses large pegs at the pegbox for coarse
adjustment and sliding beads below the bridge for fine adjustment [sourced: SPAINK-2012]. The
defining feature is the bridge: a doubly curved surface over which each string passes, with a thin
cotton or silk thread (called jiva, "the soul," or jivari) placed between string and bridge and
positioned by trial so the string just grazes the bridge surface [sourced: RAMAN-1921]. String
gauge, material (steel, brass or phosphor-bronze in different positions) and length are chosen to
balance tension roughly equally across the four strings, according to one practitioner's stated
practice [sourced: SPAINK-2012].

### Tuning

There is no single "tanpura tuning": the tonic (Sa) is chosen per performer or singer, and the
remaining strings are chosen relative to it by raga and by convention, not fixed in absolute pitch
[sourced: SPAINK-2012]. One
practitioner (a professional Hindustani tanpura player and jivari-maker) documents, from his own
practice, a four-string order in playing sequence: the pancham (fifth, or another svara chosen for
the raga) as the first string, a pair of strings ("jora") tuned to the upper-octave Sa, and the
low-octave Sa ("karaj" or "mandra") as the last [sourced: SPAINK-2012]. He explicitly discourages
tuning any string to the third (gandhar, Ga), because the harmonics of the three Sa-strings already
sound that pitch in several octaves, and he notes that a common commercial string set (equal steel
on three strings, one brass) is better suited to an occasional "Ni Sa Sa Sa" tuning than to his
preferred balanced-tension set [sourced: SPAINK-2012]. Beyond this general order and its stated
exception, raga-specific variants exist but were not enumerated by a source read in this pass:
[to-verify: a fuller table of which svara replaces the pancham string by raga, from a second
Hindustani or a Carnatic practitioner source]. Fine tuning of the jiva/jivari thread position is a
separate, continuous adjustment, made by ear while plucking, distinct from pitch tuning
[sourced: SPAINK-2012; BRIDGES-2017; VANWALSTIJN-2016].

### Note production and technique

Each string is plucked with the right-hand index finger (sometimes with the middle finger too),
near the middle of its open length, with a light, almost imperceptible touch aimed at setting the
string into full, even vibration rather than striking it percussively [sourced: SPAINK-2012]. The
four strings are plucked one after another in a fixed, continuously repeating cycle, the timing of
each stroke judged by ear against the decay of the strings already sounding, so that the four blend
into one continuous texture rather than four separate attacks [sourced: SPAINK-2012]. A pause is
conventionally left after the pancham and, longer still, after the karaj, to let those thicker,
lower strings "come to full bloom" before the cycle continues [sourced: SPAINK-2012].

### Idiomatic phrasing and ornamentation

The tanpura does not itself ornament or phrase melodically; its "phrasing" is entirely the pluck
cycle described above. What the instrument contributes to the music's ornamental identity is
indirect: because the jawari-family bridge keeps generating overtones through a note's decay
[sourced: RAMAN-1921; PISHARODY-GUPTA-2018], and because Hindustani aesthetics value continuity and
textural richness over the melodic line [sourced: WEISSER-DEMOUCRON-2012], the tanpura's role is to
supply that continuity and richness as a constant condition the soloist plays against, not as an
event of its own. See `shared/MUSICAL_SYSTEMS/DRONE_TRADITIONS.md` for how a drone shapes tension
and release generally.

### Performer interaction and ensemble role

The tanpura player (who may be the vocalist, a student, or a dedicated accompanist) has one task:
maintain the drone steadily for the length of the performance, adjusting nothing about it once it
is correctly tuned and jiva-set except, occasionally, re-settling a thread that has drifted
[sourced: SPAINK-2012]. It sits under the soloist, the accompanying melody line where one exists,
and the percussion, and does not interact rhythmically or melodically with any of them; it is the
fixed reference the other parts, and the listener, judge every interval against
[cross-reference `shared/MUSICAL_SYSTEMS/DRONE_TRADITIONS.md`].

### Repertoire contexts

The tanpura accompanies Hindustani and Carnatic classical vocal and instrumental performance
generally; it is not associated with one genre or repertoire more than another within either
system [cross-reference `shared/MUSICAL_SYSTEMS/RAGA_AND_TALA.md`].

### Improvisation

Not applicable: the tanpura's part does not vary within a performance beyond the by-ear timing
described above. It is never improvised in the sense the melodic line or the tabla's development
is [inference].

---

## Physical constraints

Four (or five) strings, one player, one continuous cyclic pluck pattern for the duration of a
performance; no polyphony, no chordal capability, no melodic range beyond the tuned pitches
[sourced: RAMAN-1921; SPAINK-2012].

## Phrase behaviour

Not applicable in the melodic sense; see repeated_note_behavior and the tradition sections above.
[inference]

## Ensemble behaviour

See "Performer interaction and ensemble role" above and `shared/MUSICAL_SYSTEMS/DRONE_TRADITIONS.md`.
[sourced: SPAINK-2012]

## Recording behaviour

[to-verify: a recording-engineering source on Hindustani/Carnatic classical sessions; see the
recording_behavior and mic_or_room_behavior rows in the behaviour cards above]

## Programming it: the control model

A tanpura part is not a melodic MIDI part in any ordinary sense. What needs representing is: (1)
the four fixed pitches (chosen per project, per `DRONE_TRADITIONS.md`'s tension-plan guidance,
never re-quantised to 12-tone equal temperament without saying so, per `shared/TUNING_AND_MPE.md`),
(2) a continuously repeating, by-ear-timed pluck cycle rather than a metronomic loop, and (3) full,
uncut decay samples or a modelled decay for each string that preserves the precursor/cascading-
overtone behaviour, not a sustained loop. Because the whole part is repetition of four pitches for
the length of a piece, `COMMON_ERRORS.md` item 1 (machine-gun repeated samples) and item 11 (round
robins reset every bar) apply with more force here than almost anywhere else in the guide
[sourced: PISHARODY-GUPTA-2018; SPAINK-2012 + inference].

## Programming it: what makes it sound real

Time the four strings' entries against each other's decay rather than on a fixed subdivision,
lengthening the gap after the lower strings specifically (a named cause: the lower strings take
longer to "come to full bloom"), and preserve each string's full natural decay including its
overtone build-up, rather than gating or looping it
[sourced: SPAINK-2012; PISHARODY-GUPTA-2018].

## What sounds fake here

A tanpura on a metronomic grid, or one built from a short looped sample, loses both of the things
that make the real instrument work: the by-ear micro-timing between strings, and the precursor
build-up in each string's decay. A tanpura with velocity mapped to a wide loudness range (rather
than treated as essentially one calibrated touch) misrepresents an instrument where harder plucking
degrades, rather than amplifies, the intended sound [sourced: SPAINK-2012; PISHARODY-GUPTA-2018].
See also `COMMON_ERRORS.md`.

## What the Performance Director needs from this file

- `performance_state.performance_reference` should record which of the tuning conventions in
  "Tuning" above is being followed, and by whom (a named practitioner's account, in this pass,
  is the only source available); do not present a single tuning order as universal.
- The pluck cycle's timing is a `timing_character` model in its own right (closest to
  `phrase_arch`/`ensemble_spread` reasoning applied within one instrument), not a candidate for
  `drift_1f` or any unnamed randomisation; log it as a deliberate, sourced model per
  `shared/HUMAN_PERFORMANCE_SCHEMA.md` section 1.
- `feasibility_report` for a tanpura part should flag, and never silently substitute for, an
  `articulation_unavailable` case where the available patch cannot represent the precursor decay or
  the by-ear inter-string timing at all: report it as a limitation of the instrument used, not
  smooth it over.
- Treat the tanpura as a required, continuously sounding part per `shared/MUSICAL_SYSTEMS/
  DRONE_TRADITIONS.md`, not an optional pad; removing it or letting it drop out changes the harmonic
  system the raga is heard against.

## What virtual implementations commonly get wrong

Most sampled or modelled tanpura patches are built as a short looped drone sample or a synthesized
pad tuned to two or three pitches, triggered as a sustained chord. This loses: the four-string
rotation and its by-ear timing (see repeated_note_behavior); the precursor build-up and cascading
overtone behaviour that is acoustically documented as central to the instrument's identity
[sourced: PISHARODY-GUPTA-2018; VANWALSTIJN-2016]; and the sensitivity of the jivari effect to
exactly how hard the string is excited, which a static sample or a velocity-to-volume mapping
cannot represent at all [sourced: PISHARODY-GUPTA-2018]. A patch built from one recorded pluck per
string, looped or crossfaded into a "drone," should be understood as an approximation with a named,
specific loss, not treated as equivalent to a real instrument or to the physical models described
in the acoustics literature read here [inference].

## What must not be generalised outside the tradition

The tanpura's role as a fixed, unchanging harmonic reference that the entire raga is heard against
is specific to Hindustani and Carnatic practice and to the broader family of drone traditions
described in `shared/MUSICAL_SYSTEMS/DRONE_TRADITIONS.md`; it is not a "world music drone pad" and
should not be used as generic exotic texture under unrelated harmonic material, per
`shared/MUSICAL_SYSTEMS/INDEX.md` rule 6. The tuning order and terminology recorded here (pancham,
jora, karaj) is specifically Hindustani, from one named practitioner's account; it is not
established here as Carnatic tambura practice, which was not reached by a comparable source in this
pass [sourced: SPAINK-2012 + inference].

## Restricted and ceremonial repertoire

No source read in this pass identified any restricted, ceremonial or lineage-held repertoire
specific to the tanpura/tambura itself (as distinct from vocal or instrumental repertoire it might
accompany). The tanpura's role is accompanimental and drone-providing across concert Hindustani and
Carnatic performance generally, which is secular concert repertoire. This question is open for
repertoire the tanpura might accompany in a devotional or ritual context specifically; none was
identified either way in this research pass [to-verify: whether any devotional or ritual
Hindustani/Carnatic repertoire the tanpura accompanies carries restrictions of its own, from a
practitioner or institutional source].

## Sources and what to verify

Full source rows are in `research/sources/INSTRUMENT_SOURCES.md`; claim-by-claim records, with
scope and limitations, are in `research/instruments/TANPURA.md`. In summary: the bridge/jivari
mechanism rests on academic acoustics read in full or at section depth (Raman 1921; Pisharody and
Gupta 2018; van Walstijn, Bridges and Mehes 2016; Bridges and van Walstijn 2017); the aesthetic and
ensemble-role claims rest on ethnomusicology with named fieldwork (Weisser, Demoucron and Leman
2012); construction, tuning order and plucking practice rest on two Hindustani practitioner sources
(Ravi Shankar; Martin Spaink). Carnatic-specific practice, recording practice, pitch-stability over
a performance, and the internal design of the electronic tanpura/sruti box substitute are all
to-verify, listed in full in the research file.
