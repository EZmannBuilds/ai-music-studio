# Cuban Hand Percussion

Traditions: Cuban son, rumba (guaguanco, yambu, columbia) and salsa/timba hand-drum practice.
Context: `shared/MUSICAL_SYSTEMS/CLAVE_AND_TIMELINES.md`.

This page covers the tumbadora (conga: quinto, conga/tres dos, tumba/salidor) and the bongo,
including the bongocero's switch to the handheld cencerro in son montuno and salsa performance. It
does not cover batá drums, which are covered under "Restricted and ceremonial repertoire" below and
not otherwise. It does not cover the clave instrument or timeline logic itself, which
`shared/MUSICAL_SYSTEMS/CLAVE_AND_TIMELINES.md` covers; this page links to that file rather than
repeating it. `shared/VIRTUAL_INSTRUMENT_GUIDE/HAND_PERCUSSION.md` covers only the physics shared
across hand-struck membranes in general and explicitly routes the Cuban-specific vocabulary here;
this page is that routing's destination, not a restatement of that frame page.

> Evidence: read at full depth: Alex Pertout's practitioner account of conga technique, excerpted
> from his own MPhil thesis [PERTOUT-CONGA-II], and three pedagogy articles by a named
> Latin-percussion teacher [ZAHNER-CONGA-TECHNIQUE; ZAHNER-BONGO-TECHNIQUE; ZAHNER-CONGA-TUNING].
> Read at section depth: a salsa-drumming pedagogy article by a named teacher, covering clave
> orientation, martillo and the bongo-to-cencerro switch [LIBERTYPARK-BACHE-SALSA]. A Percussive Arts
> Society article was reached but is paywalled and was not read [PAS-CONGA-MARCHA]. Source IDs
> resolve in `research/sources/INSTRUMENT_SOURCES.md`; the claims and their limits are recorded in
> `research/instruments/CUBAN_HAND_PERCUSSION.md`.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## Behaviour cards

### Tumbadora (Conga: quinto, conga/tres dos, tumba/salidor)

A set of three sizes plays folkloric rumba: quinto (the smallest and highest, the lead/solo drum),
conga (also called tres dos or segunda, the middle drum) and tumba (also called salidor, the largest
and lowest). One or two drums (commonly called conga and tumba) are the norm in son, mambo, cha-cha
and salsa contexts. The three-drum naming (tres dos, salidor) comes from the task brief and general
usage in the field; it was not independently confirmed by a source read this pass, so it is marked
accordingly below.

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A single head (skin or synthetic) mounted on a staved wooden or fibreglass shell, open at the bottom, struck with the bare hand; the smallest (quinto), middle (conga) and largest (tumba) drums differ mainly in shell diameter and head size, giving progressively lower fundamental pitch as the drum gets larger. | sourced: PERTOUT-CONGA-II + inference |
| attack_behavior | Where and how the hand strikes changes which sound results, not only its loudness: striking and retracting the palm from the drum's centre gives the low bass tone; striking the head's edge with the ridge of the palm (fingers elevated) gives the open tone; the same edge strike with relaxed, cupped fingers that whip forward and grab the head gives the slap. | sourced: PERTOUT-CONGA-II; ZAHNER-CONGA-TECHNIQUE |
| sustain_behavior | An open tone or open slap is allowed to ring after the hand lifts away; a muffled (muted/closed) tone or slap is damped by fingers left resting on, or pressed into, the head after the strike. | sourced: PERTOUT-CONGA-II |
| release_behavior | As sustain_behavior: an open stroke's ring decays naturally; a muffled stroke's decay is cut short by the hand remaining on the head, both being deliberate, named techniques rather than one correct default. | sourced: PERTOUT-CONGA-II |
| dynamic_timbre_change | Not addressed directly by a source read this pass beyond the general point that a slap is a distinct technique (relaxed, cupped fingers whipping the head) rather than simply a harder-struck tone. | sourced: ZAHNER-CONGA-TECHNIQUE + to-verify: not opened this pass |
| register_character | Quinto is highest and is the lead/solo voice; conga (tres dos/segunda) sits in the middle and typically states the main tumbao pattern; tumba (salidor) is lowest and, in Havana-style guaguanco, lands its phrases on beat four on both sides of the clave. | sourced: PERTOUT-CONGA-II + inference |
| practical_range | Not given as pitch classes by any source read this pass; drums are tuned relative to each other (see virtual_programming/velocity and the tuning discussion below) rather than to fixed absolute pitches. | to-verify: typical fundamental-frequency ranges per drum size, not opened this pass |
| tessitura | Follows from register_character: quinto carries fast, high, improvised material; tumba/salidor carries the lowest, most repetitive structural phrases; the middle drum(s) carry the main repeating pattern. | inference |
| articulation_logic | Eight named strokes make up a developed technique: palm (also called heel), fingers (also called toe, tip or touch), bass, open tone, muffled tone, slap, open slap and muffled slap. The naming is genuinely unsettled across the pedagogical literature, and Spanish terms are also in use; this page does not pick one standard, because its own best source states none exists. | sourced: PERTOUT-CONGA-II |
| phrase_limits | Two hands alternating sets the basic speed limit, as on any hand drum; tumbao and guaguanco patterns are built from named, repeating cyclical figures rather than free-length phrases outside of the quinto's lead role. | inference |
| transitions | No legato; every stroke is a discrete hand contact, though a marcha-style pattern alternates the heel and toe strokes continuously enough to read as a rolling texture under the louder tone/slap accents. | sourced: ZAHNER-CONGA-TECHNIQUE |
| repeated_note_behavior | Two-hand alternation (heel/toe, or fingers/palm) is the mechanism for fast repeated figures, developed through dedicated alternation and "chop" exercises. | sourced: ZAHNER-CONGA-TECHNIQUE |
| vibrato | Not applicable in the sustained-pitch sense. | inference |
| pitch_instability | Not addressed by a source read this pass; conga heads are not typically bent in pitch during play the way some other hand drums are. | to-verify: whether any Cuban tumbadora technique uses in-stroke pitch bending, not opened this pass |
| resonance | The open-bottomed shell couples the struck head to the enclosed air column; specific resonance behaviour (how the open bottom shapes the tone versus a closed-bottom drum) was not addressed by a source read this pass. | to-verify: shell/bottom resonance behaviour specific to the tumbadora, not opened this pass |
| physical_noise | Hand-on-skin contact noise is audible on every stroke and is part of the instrument's identity, consistent with `shared/VIRTUAL_INSTRUMENT_GUIDE/HAND_PERCUSSION.md`'s general claim for hand-struck membranes. | inference |
| feasibility | Two hands, one drum each in a two-or-three-drum set (a folkloric guaguanco ensemble uses three separate players, one per drum, not one player playing three drums); a pattern needing more than two simultaneous strikes, or a hand re-striking faster than a real player can, is not playable. | sourced: ZAHNER-CONGA-TECHNIQUE + inference |
| ensemble_behavior | In Havana-style guaguanco, three named roles interlock: tumba (beat four, both sides of clave), segunda/conga (at least beat one on the "two" side of clave) and quinto (solo, conversational, playing off the dancers and the other drums). The Matanzas style is named by the source as differing, but its specifics were not read this pass. In son, mambo and salsa contexts, one or two conga players state the tumbao pattern within a larger percussion section (bongo, timbales, clave). | sourced: ZAHNER-CONGA-TECHNIQUE + to-verify: not opened this pass |
| recording_behavior | Not addressed by a source read this pass. | to-verify: conventional close-mic or room approach for congas, not opened this pass |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | A struck drum: note length does not extend the natural decay, which is set by stroke type (open versus muffled) and hand position at release, not by how long a MIDI note is held. | inference |
| overlap | Not a legato instrument; every stroke is a separate sample trigger. | inference |
| velocity | Should select among the genuinely different recorded strokes (the eight named in articulation_logic) where the instrument's vocabulary has them, not act only as level within one stroke sample; collapsing "open tone" and "slap" onto one velocity curve loses the instrument's real vocabulary, consistent with `HAND_PERCUSSION.md`'s general warning. | sourced: PERTOUT-CONGA-II + inference |
| continuous_dynamics | Not applicable to single discrete strokes. | inference |
| expression | Not the primary control for a single stroke. | inference |
| articulation_switching | Each of the eight named strokes is its own recorded sample set, not an EQ or gain variant of another stroke; a patch with only "open tone" and "slap" at different velocities is missing most of the real vocabulary. | sourced: PERTOUT-CONGA-II |
| round_robins | Essential: tumbao, guaguanco and marcha patterns repeat short figures rapidly, and identical repeated strokes are highly exposed. | inference |
| release_samples | The difference between an open stroke's natural ring and a muffled stroke's immediate stop is a real, named technique distinction (sustain_behavior/release_behavior above); collapsing both into one undamped sample loses the muffled/muted technique entirely. | sourced: PERTOUT-CONGA-II |
| pedal_or_breath_behavior | Not applicable to the tumbadora itself. | inference |
| transition_samples | Not applicable between discrete strokes. | inference |
| mic_or_room_behavior | Not addressed by a source read this pass. | to-verify: recording convention, not opened this pass |
| likely_fake_sounding_errors | Collapsing the eight-stroke vocabulary into "open tone" and "slap" at varying velocity; a muffled stroke played as an open stroke turned down rather than a genuinely damped recording; a guaguanco part with all three drum roles quantised identically instead of each landing at its own named position relative to clave; treating conga tuning as fixed absolute pitches rather than a relative, by-ear interval between drums. | sourced: PERTOUT-CONGA-II; ZAHNER-CONGA-TECHNIQUE; ZAHNER-CONGA-TUNING |
| organic_programming_methods | Use the tradition's own eight-stroke vocabulary rather than a generic bass/open/slap model; alternate hands (heel/toe or palm/fingers) for repeated figures, per repeated_note_behavior; place each guaguanco drum role (tumba, segunda, quinto) at its own named position relative to the clave's orientation (`shared/MUSICAL_SYSTEMS/CLAVE_AND_TIMELINES.md`), never quantised as a generic loop; vary quinto's material as genuine, non-repeating solo improvisation rather than a looped figure. | sourced: PERTOUT-CONGA-II; ZAHNER-CONGA-TECHNIQUE |

### Bongo

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A pair of small, single-headed, open-bottomed drums joined together: the smaller, higher-pitched macho and the larger, lower-pitched hembra, traditionally held between the seated player's knees. | sourced: ZAHNER-BONGO-TECHNIQUE |
| attack_behavior | Struck primarily with the finger pads rather than the whole hand; striking with one finger pad produces a higher-pitched, more pointed accent than striking with two or more pads together. | sourced: ZAHNER-BONGO-TECHNIQUE |
| sustain_behavior | An unmuted stroke rings; leaving a finger resting on the head after the strike produces a muted tone, used deliberately to thicken a pattern (the "heel and toe" technique within martillo). | sourced: ZAHNER-BONGO-TECHNIQUE |
| release_behavior | As sustain_behavior: open strokes decay naturally; muted strokes are cut short by finger contact remaining on the head. | sourced: ZAHNER-BONGO-TECHNIQUE |
| dynamic_timbre_change | Not addressed by a source read this pass beyond the one- versus two-finger-pad distinction under attack_behavior. | to-verify: how tone changes with force within one stroke type, not opened this pass |
| register_character | Macho (smaller) is higher and carries more of the melodic/pattern material; hembra (larger) is lower. | sourced: ZAHNER-BONGO-TECHNIQUE |
| practical_range | Not given as pitch classes; bongo pairs are commonly tuned to an interval (an octave or a fifth is named as usual) between macho and hembra, by ear, rather than to fixed pitches. | sourced: ZAHNER-BONGO-TECHNIQUE |
| tessitura | Follows register_character: most of the martillo pattern's melodic movement sits on the macho, with the hembra used more sparingly. | inference |
| articulation_logic | The core pattern is martillo ("hammer"), a continuous, largely quarter-note-driven pattern; within it, a heel-and-toe muted-stroke technique on the macho (commonly the non-dominant hand muting with the thumb while the playing hand's finger pads state the pattern) sits under the louder open strokes. In son and salsa performance, the bongocero (bongo player) switches, for the more intense montuno or coro section of a tune, from the drums to a handheld cowbell (cencerro, called campana de bongo); once that switch is made it is unlikely, in practice, that the player returns to the drums for the rest of the performance. In a salsa ensemble with a timbalero, the timbales player's cowbell or cascara part may cover this role instead, reducing the need for the bongocero to switch. | sourced: ZAHNER-BONGO-TECHNIQUE; LIBERTYPARK-BACHE-SALSA |
| phrase_limits | Two hands, martillo as a continuous pattern rather than a phrase-bounded figure; the switch to cencerro (articulation_logic above) is a section-level, not phrase-level, change. | sourced: LIBERTYPARK-BACHE-SALSA + inference |
| transitions | No legato; discrete finger-pad strokes, as with the tumbadora. | inference |
| repeated_note_behavior | Two-hand (finger-pad) alternation drives martillo's continuous repeated pattern. | sourced: ZAHNER-BONGO-TECHNIQUE |
| vibrato | Not applicable. | inference |
| pitch_instability | Not addressed by a source read this pass. | to-verify: whether bongo technique includes in-stroke pitch bending, not opened this pass |
| resonance | Open-bottomed shell as with the tumbadora; not addressed in more detail by a source read this pass. | to-verify: bongo-specific shell resonance behaviour, not opened this pass |
| physical_noise | Finger-on-skin contact noise is audible on every stroke, consistent with `shared/VIRTUAL_INSTRUMENT_GUIDE/HAND_PERCUSSION.md`'s general claim for hand-struck membranes. | inference |
| feasibility | Two hands on the drum pair; the bongocero's switch to a handheld cencerro is a switch of instrument, not an added limb, so a part that asks for simultaneous bongo martillo and cencerro from one player is not playable. | sourced: LIBERTYPARK-BACHE-SALSA + inference |
| ensemble_behavior | The bongocero sits within the wider percussion section (alongside clave, tumbadora and, in salsa, timbales); the decision of who plays the cowbell during a montuno/coro section (bongocero versus timbalero) is a real, named ensemble-arranging choice, not a fixed rule. | sourced: LIBERTYPARK-BACHE-SALSA |
| recording_behavior | Not addressed by a source read this pass. | to-verify: conventional close-mic or room approach for bongo, not opened this pass |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Struck drum; note length does not extend natural decay, which is set by open versus muted technique. | inference |
| overlap | Not a legato instrument. | inference |
| velocity | Should select genuinely different recorded strokes (open versus muted, one-pad versus two-pad) where the instrument's vocabulary has them, not act only as level within one sample. | sourced: ZAHNER-BONGO-TECHNIQUE + inference |
| continuous_dynamics | Not applicable to discrete strokes. | inference |
| expression | Not the primary control for a single stroke. | inference |
| articulation_switching | Bongo drum strokes and the cencerro (bongo bell) are different instruments entirely, not articulations of one patch; a part that needs both requires either two separate instrument tracks or an explicit, notated instrument-change point matching the tradition's own section-level switch, not a keyswitch mid-pattern. | sourced: LIBERTYPARK-BACHE-SALSA |
| round_robins | Essential: martillo is a continuous, rapidly repeating pattern, and identical repeated strokes are highly exposed. | inference |
| release_samples | The difference between an open and a muted stroke (heel-and-toe technique) is a real, named release-behaviour distinction that a single undamped sample loses. | sourced: ZAHNER-BONGO-TECHNIQUE |
| pedal_or_breath_behavior | Not applicable. | inference |
| transition_samples | Not applicable between discrete strokes; the bongo-to-cencerro section change is an instrument change, not a note-to-note transition. | sourced: LIBERTYPARK-BACHE-SALSA + inference |
| mic_or_room_behavior | Not addressed by a source read this pass. | to-verify: recording convention, not opened this pass |
| likely_fake_sounding_errors | Playing martillo with no heel-and-toe muted layer under the open strokes, which flattens the pattern's real texture; never switching to cencerro for a montuno/coro section (or switching and then switching back, which the source states real bongoceros in practice do not do); treating the bongo bell as a bongo articulation rather than a separate instrument. | sourced: ZAHNER-BONGO-TECHNIQUE; LIBERTYPARK-BACHE-SALSA |
| organic_programming_methods | Alternate hands/fingers for martillo's repeated pattern, per repeated_note_behavior; include the heel-and-toe muted layer under the open strokes rather than only the accented strokes; write the bongo-to-cencerro switch as a real, section-level instrument change timed to the tune's structure (typically at the montuno/coro), not as a random or decorative addition. | sourced: ZAHNER-BONGO-TECHNIQUE; LIBERTYPARK-BACHE-SALSA |

---

## Tradition and context

### Construction

The tumbadora is a single-headed, open-bottomed drum built in three traditional sizes -- quinto
(smallest, highest), conga (middle) and tumba (largest, lowest) -- with a staved wooden or fibreglass
shell. The bongo pairs two small, single-headed, open-bottomed drums of different sizes (macho,
hembra) joined together, traditionally played seated with the drum pair held between the knees.
[sourced: PERTOUT-CONGA-II; ZAHNER-BONGO-TECHNIQUE]

### Tuning

Neither instrument is tuned to a fixed absolute pitch in the sources read this pass; both are tuned
relatively, by ear. Conga players commonly tune multiple drums to a perfect fourth or perfect fifth
interval apart (a minor third or major second are also named as workable), adjusting tension until
the open tone, slap and bass strokes all sound clear rather than targeting specific pitches. Bongo
pairs are commonly tuned with macho and hembra an octave or a fifth apart. [sourced: ZAHNER-CONGA-TUNING; ZAHNER-BONGO-TECHNIQUE]

### Note production and technique

The tumbadora's eight-stroke vocabulary (palm/heel, fingers/toe, bass, open tone, muffled tone, slap,
open slap, muffled slap) is produced entirely by where and how the bare hand contacts the head: near
the centre for the low bass tone, at the edge with the palm ridge and fingers elevated for the open
tone, and at the edge with relaxed, cupped fingers that whip forward for the slap. The bongo's
vocabulary is narrower and finger-pad-based: one- versus two-pad strikes at the edge, with a muted
tone produced by leaving a finger on the head. Both instruments rely on two-hand alternation for fast
repeated figures. [sourced: PERTOUT-CONGA-II; ZAHNER-CONGA-TECHNIQUE; ZAHNER-BONGO-TECHNIQUE]

### Idiomatic phrasing and ornamentation

The tumbadora's tumbao and the bongo's martillo are both continuous, cyclically repeating patterns
rather than phrase-bounded melodic material; within martillo, the heel-and-toe muted-stroke layer
functions as a constant textural bed under the louder accented strokes, similar in function (though
not in name or mechanism) to a marcha's heel/toe alternation on conga. Ornamentation in the sense used
for melodic instruments does not apply; variation happens through stroke choice, dynamic accent and,
for the quinto in rumba, genuine improvised soloing. [sourced: ZAHNER-CONGA-TECHNIQUE; ZAHNER-BONGO-TECHNIQUE]

### Performer interaction and ensemble role

In Havana-style guaguanco, three named drum roles interlock against the clave: tumba landing on beat
four on both sides, segunda/conga on at least beat one of the "two" side, and quinto soloing in
conversation with the other drums and the dancers -- everyone hearing their part against the clave's
timeline logic, per `shared/MUSICAL_SYSTEMS/CLAVE_AND_TIMELINES.md`. In son and salsa contexts, the
bongocero's decision to switch from bongo to handheld cencerro at the montuno or coro section is a
named, real-time ensemble decision, and in a salsa ensemble with a timbalero, either player may end
up covering the cowbell role depending on the arrangement. [sourced: ZAHNER-CONGA-TECHNIQUE; LIBERTYPARK-BACHE-SALSA]

### Repertoire contexts

Son and son montuno (bongo as the primary hand drum, tumbadora added later in the ensemble's
development), rumba in its guaguanco, yambu and columbia forms (tumbadora-family drums, one player
per drum in a folkloric ensemble), and salsa/timba (tumbadora and bongo both present, alongside
timbales). This page's sources reached guaguanco's roles specifically (Havana style); yambu and
columbia were not addressed by a source read this pass. [sourced: ZAHNER-CONGA-TECHNIQUE; LIBERTYPARK-BACHE-SALSA + to-verify: not opened this pass]

### Improvisation

The quinto is the named improvising/soloing voice in guaguanco, playing in conversation with the
other two drums and with the dancers. Improvisation elsewhere (within martillo, or within a
tumbao-based groove) was not addressed in detail by a source read this pass beyond the general
observation that a lead drum's role is conversational rather than fixed. [sourced: ZAHNER-CONGA-TECHNIQUE]

---

## What the instrument is

Two related but distinct Afro-Cuban hand-drum families: the tumbadora (conga), a single-headed,
open-bottomed drum built in three sizes with an eight-stroke hand technique, and the bongo, a paired
small-drum instrument played with the finger pads whose player also, at specific points in a tune,
switches to a handheld cowbell. [sourced: PERTOUT-CONGA-II; ZAHNER-BONGO-TECHNIQUE]

## Range and register

Not given as fixed pitch classes by any source read this pass; both instruments are tuned relatively,
by ear, to intervals between drums rather than to absolute pitches (see "Tuning" above). [sourced: ZAHNER-CONGA-TUNING; ZAHNER-BONGO-TECHNIQUE]

## Articulation and note transitions

See articulation_logic in both cards above: an eight-stroke vocabulary for the tumbadora, a narrower
finger-pad vocabulary plus the martillo pattern's heel-and-toe muted layer for the bongo, and, for the
bongo specifically, the section-level switch to cencerro. [sourced: PERTOUT-CONGA-II; ZAHNER-BONGO-TECHNIQUE; LIBERTYPARK-BACHE-SALSA]

## Physical constraints

Two hands per player, one drum (or drum pair) per player; a folkloric three-drum guaguanco ensemble
uses three separate players, not one player covering all three drums. [sourced: ZAHNER-CONGA-TECHNIQUE]

## Phrase behaviour

Both instruments are built from continuously repeating cyclical patterns (tumbao, martillo) rather
than phrase-bounded melodic material, with the quinto's improvised soloing in guaguanco as the main
exception. [sourced: ZAHNER-CONGA-TECHNIQUE]

## Ensemble behaviour

See "Performer interaction and ensemble role" above: named, interlocking roles in guaguanco;
real-time arranging decisions (the cencerro switch, and who covers the cowbell role) in son and
salsa. [sourced: ZAHNER-CONGA-TECHNIQUE; LIBERTYPARK-BACHE-SALSA]

## Recording behaviour

Not addressed by a source read this pass. [to-verify: conventional close-mic or room approach for
either instrument, not opened this pass]

## Programming it: the control model

```text
stroke_vocabulary: eight named tumbadora strokes, a narrower bongo vocabulary; each is a separate
  recorded sample set, not a velocity layer of another stroke
tuning: relative, by ear, to a named interval between drums (commonly a fourth or fifth for conga,
  an octave or fifth for bongo); never a fixed absolute pitch
clave_orientation: every guaguanco, son or salsa part is written relative to a stated clave
  orientation (2:3 or 3:2), per shared/MUSICAL_SYSTEMS/CLAVE_AND_TIMELINES.md, never quantised
  without one
bongo_to_cencerro: a real instrument change at a named section boundary (typically the montuno or
  coro), not an articulation switch within one patch
```
[sourced: PERTOUT-CONGA-II; ZAHNER-CONGA-TUNING; LIBERTYPARK-BACHE-SALSA]

## Programming it: what makes it sound real

- Use the full eight-stroke tumbadora vocabulary and the bongo's open/muted, one-pad/two-pad
  vocabulary as separate recorded strokes, not as velocity layers of one sample. [sourced: PERTOUT-CONGA-II; ZAHNER-BONGO-TECHNIQUE]
- State a clave orientation (2:3 or 3:2) for the section before writing any part against it, per
  `shared/MUSICAL_SYSTEMS/CLAVE_AND_TIMELINES.md`. [sourced: LIBERTYPARK-BACHE-SALSA]
- Place each guaguanco drum role (tumba, segunda, quinto) at its own named position relative to
  clave, not quantised identically. [sourced: ZAHNER-CONGA-TECHNIQUE]
- Write the bongo-to-cencerro switch as a real section-level instrument change timed to the tune's
  structure, and do not switch back to bongo once the bell is established, matching the source's own
  account of real performance practice. [sourced: LIBERTYPARK-BACHE-SALSA]
- Tune multiple drums to a stated relative interval (fourth or fifth for conga; octave or fifth for
  bongo), never to fixed absolute pitches presented as "the" tuning. [sourced: ZAHNER-CONGA-TUNING; ZAHNER-BONGO-TECHNIQUE]

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Family- and tradition-specific tells:

- collapsing the tumbadora's eight-stroke vocabulary into "open tone" and "slap" at varying velocity;
  [sourced: PERTOUT-CONGA-II]
- a muffled/muted stroke played as an open stroke turned down, on either instrument, rather than a
  genuinely damped recording; [sourced: PERTOUT-CONGA-II; ZAHNER-BONGO-TECHNIQUE]
- a guaguanco part with all three drum roles quantised to the same grid position instead of each
  landing at its own named point relative to clave; [sourced: ZAHNER-CONGA-TECHNIQUE]
- a crossed clave orientation, or no stated orientation at all, per
  `shared/MUSICAL_SYSTEMS/CLAVE_AND_TIMELINES.md`; [sourced: LIBERTYPARK-BACHE-SALSA]
- a bongo part that never switches to cencerro for a montuno/coro section, or that switches back to
  bongo mid-section, when the source read this pass states real bongoceros in practice do not do
  that; [sourced: LIBERTYPARK-BACHE-SALSA]
- treating conga or bongo tuning as fixed absolute pitches rather than a relative, by-ear interval.
  [sourced: ZAHNER-CONGA-TUNING; ZAHNER-BONGO-TECHNIQUE]

## What virtual implementations commonly get wrong

The task brief's own framing names the core failure directly: a conga patch built around one stroke
type. Where a patch offers only "open tone" and "slap" (or worse, one generic hit) at different
velocities, the tumbadora's real eight-stroke, hand-position-dependent vocabulary is lost entirely,
and no amount of velocity-curve shaping recovers the missing strokes, because velocity is meant to
select among genuinely different recordings here, not to fake a stroke change through level alone.
[sourced: PERTOUT-CONGA-II]

A second common failure is treating the bongo bell (cencerro) as an articulation of a bongo patch --
a keyswitch or a round-robin variant -- rather than as a wholly separate instrument that the
bongocero physically changes to at a specific point in the tune's structure. A patch that offers
"bongo" and "bongo bell" as switchable articulations on one track invites exactly the kind of
mid-pattern switching real bongoceros do not do, per the source read this pass. [sourced: LIBERTYPARK-BACHE-SALSA]

A third is rhythmic: writing guaguanco, son or salsa parts with no stated clave orientation, or with
each drum's role quantised to the same grid position rather than each landing at its own named point
relative to the clave. See `shared/MUSICAL_SYSTEMS/CLAVE_AND_TIMELINES.md` for the orientation logic
this page depends on rather than repeats. [sourced: ZAHNER-CONGA-TECHNIQUE; LIBERTYPARK-BACHE-SALSA]

## What must not be generalised outside the tradition

- **The guaguanco drum roles recorded here (CU-03 in the research file) are named specifically for
  the Havana style.** The source itself states the Matanzas style differs; this page does not state
  what that difference is, because it was not read this pass. Do not apply Havana-style role
  assignments to a Matanzas-style arrangement. [sourced: ZAHNER-CONGA-TECHNIQUE]
- **The eight-stroke tumbadora vocabulary's naming is genuinely unsettled**, per Pertout's own text;
  do not present any one naming scheme (including this page's) as the single correct standard.
  [sourced: PERTOUT-CONGA-II]
- **"Tres dos" and "salidor" as names for the middle and low drums are not confirmed by a source read
  this pass** and are marked as inference on this page; do not present them as verified terminology
  without checking a dedicated source. [inference]
- **Son and salsa practice are not folkloric rumba practice.** The bongo-to-cencerro switch and the
  timbalero's possible role in covering it are specific to son montuno and salsa ensemble contexts,
  not to guaguanco, yambu or columbia, which do not feature a timbalero. [sourced: LIBERTYPARK-BACHE-SALSA]
- **Do not extend clave/timeline claims beyond what
  `shared/MUSICAL_SYSTEMS/CLAVE_AND_TIMELINES.md` itself supports**: that file's own confidence note
  states it has not read Penalosa's *The Clave Matrix* in full, and this page has not read it either.
  [standard-reference: PENALOSA-2009]

## Restricted and ceremonial repertoire

Batá drums (the consecrated fundamento set and the unconsecrated aberikulá set, in Lucumi/Santeria
practice) are a separate instrument from the tumbadora and bongo this page covers, and their
technique and repertoire are deliberately not researched or described here, per rule 5 of
`shared/MUSICAL_SYSTEMS/INDEX.md`: batá fundamento drums are consecrated instruments played in
religious ritual contexts within Lucumi/Santeria practice, and this pack declines to imitate or
sample that repertoire. No source read this pass addresses batá construction, technique or repertoire
in any depth, so this page states plainly that it has nothing further to say about them beyond naming
the fundamento/aberikulá distinction and declining to go further -- this is a boundary, not a summary.
For a secular or concert-context Cuban hand-percussion request, the tumbadora and bongo material on
this page, and the folkloric rumba forms it covers (guaguanco, yambu, columbia), are the adjacent,
non-restricted repertoire. Whether any part of the tumbadora or bongo repertoire itself (as distinct
from batá) carries restrictions was not addressed by any source read this pass; this page treats that
as an open question, not a confirmed absence of restriction. [inference]

## What the Performance Director needs from this file

- `articulation_unavailable` is the expected outcome when a general-purpose hand-percussion library
  is asked for the full eight-stroke tumbadora vocabulary, or for a genuine bongo-to-cencerro
  instrument change; report it rather than approximating with velocity layers or a keyswitch.
- Do not proceed on an unstated clave orientation: per
  `shared/MUSICAL_SYSTEMS/CLAVE_AND_TIMELINES.md`, name the orientation (2:3 or 3:2) before writing
  any guaguanco, son or salsa percussion part, and treat an unstated orientation as an unanswered
  check, not a default to assume silently.
- `limb_or_finger_conflicts`: two hands per player; a folkloric three-drum guaguanco part needs three
  players' worth of material, not one part covering all three drum roles simultaneously.
- Batá repertoire is declined per "Restricted and ceremonial repertoire" above; a request for it
  routes back to the user as a named, explained decline, not a substitution with tumbadora or bongo
  material presented as equivalent.

## Sources and what to verify

Full citations and read depth are in `research/sources/INSTRUMENT_SOURCES.md`; claim-by-claim
evidence and limits are in `research/instruments/CUBAN_HAND_PERCUSSION.md`. Left open by this pass:
bongo and conga fundamental-pitch ranges as such; recording convention for either instrument; yambu
and columbia drum roles specifically (only guaguanco, and only its Havana style, was reached);
Matanzas-style guaguanco; the "tres dos"/"salidor" naming question; and a direct reading of Penalosa's
*The Clave Matrix*, which `shared/MUSICAL_SYSTEMS/CLAVE_AND_TIMELINES.md` cites but has not itself
read in full.
