# Drum Kit

The played kit: kick, snare, toms, hi-hat, and ride and crash cymbals, operated by two hands and two
feet. Orchestral percussion has its own page, `PERCUSSION.md`. Tuned mallet percussion has its own
page, `MALLETS.md`. Hand-struck drums have their own frame page, `HAND_PERCUSSION.md`, which routes
each tradition (conga, jembe, tabla, and so on) to its own page.

> Evidence: read at section depth this pass: two of Sofia Dahl's studies of drumstick movement and
> striking velocity (source IDs DAHL-2003-THESIS, DAHL-2004-ACCENT), Cecil Forsyth's 1914
> orchestration text on snare and cymbal technique (FORSYTH-1914; the physical mechanisms transfer to
> the kit even though his examples are orchestral), the Percussive Arts Society's 40 International
> Drum Rudiments (PAS-RUDIMENTS-1984), one peer-reviewed study of a drummer's hi-hat microtiming
> (RASANEN-2015), and one acoustics textbook's pages on drum-head vibration modes
> (WOODHOUSE-TUNED-DRUMS; general physics, not kit-specific). Cymbal and drum-head decay spectra, and
> a general acoustics account of why a struck membrane's overtones are inharmonic, are attributed to
> Fletcher and Rossing, *The Physics of Musical Instruments*, but not opened this pass. Read depths
> and full citations are in `research/sources/INSTRUMENT_SOURCES.md`; the claims and their limits are in
> `research/instruments/DRUM_KIT.md`.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## Behaviour cards

### Kick

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A single large drum: a batter head struck by a foot-operated beater, usually with a second, resonant head on the far side carrying a port. Shell, both heads and the enclosed air together set the tone. | inference |
| attack_behavior | Beater material (felt, hard felt, plastic, wood) and strike force set the attack transient; a harder or more central strike drives more high-frequency click relative to the low thump. | inference |
| sustain_behavior | Very short natural sustain. The resonant head, the port size, and any internal muffling set how long and how pitched the decay is. | inference |
| release_behavior | The decay tail continues briefly after the beater leaves the head unless damped; an internal pillow, foam block, or external gate shortens it. | inference |
| dynamic_timbre_change | A harder strike is not only louder: it drives the head and the beater's own compression further into their non-linear range, adding click energy disproportionate to the added loudness. | inference + to-verify: what would settle this is not recorded |
| register_character | Sits at the bottom of the mix. Head tension and muffling decide whether it reads as a short, dry thump or a longer, more pitched boom. | inference |
| practical_range | Not pitched in the melodic sense. Tuning sets a fundamental the ear reads as "kick" rather than "tom," typically somewhere in the bottom two octaves of the piano; the exact frequency is a mixing and calibration fact, not a guide fact. | inference |
| tessitura | One surface, so no tessitura in the wind or string sense. The practical equivalent is the tuning window that still reads as a kick rather than a low tom. | inference |
| articulation_logic | One primary stroke. Some setups add a second technique: heel-down versus heel-up beater control, or a "buried beater" technique that presses the beater into the head after the stroke for a drier, shorter sound, functionally a self-administered mute. | inference |
| phrase_limits | Bound by one foot (or two with a double pedal or two kick drums). Repeated-kick speed is limited by ankle and leg speed and by the pedal spring's return time, the one-limb analogue of the hand's stick-alternation limit. | inference |
| transitions | No legato; every kick is a discrete strike. | inference |
| repeated_note_behavior | The same physical strike repeated. A real player's strike force and the pedal's return timing vary slightly stroke to stroke, and a long fast passage tires the leg. | inference |
| vibrato | None. | inference |
| pitch_instability | Head tension can drift over a set from heat, humidity, and play, but this is not something a player bends in real time. | inference |
| resonance | The shell's enclosed air and the port colour the tone; a heavily muffled kick loses most of this and becomes close to a dry click. | inference |
| physical_noise | Beater impact click; pedal spring and hinge noise, audible as a squeak on some hardware; the player's heel or footboard contact. | inference |
| feasibility | One foot, one strike at a time, unless a double pedal or a second kick drum is in use. Conflicts arise only if the same physical foot is asked to do something else at the same instant. | inference |
| ensemble_behavior | Anchors the arrangement with the bass. The kick-bass relationship is an arrangement decision; see `BASS.md`. | inference |
| recording_behavior | Typically close-miked inside or just outside the port, often blended with a second, more distant mic; mic placement relative to the beater changes the click-to-body balance heard. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short notes trigger the sample; a held note beyond the sample's natural decay adds nothing, because a real kick does not sustain under sustained pressure. | inference |
| overlap | Not a legato instrument; no overlap requirement. | inference |
| velocity | Selects among recorded dynamic layers where the instrument has more than one (a real soft, medium, and hard beater strike are different recordings), then level within a layer. | inference |
| continuous_dynamics | Not a sustaining instrument; each hit is its own event, so there is no drawn shape within a note. | inference |
| expression | Not applicable in the sustained-instrument sense. | inference |
| articulation_switching | Where a patch offers an alternate beater type or an open/muffled kick, that is a separate recorded sample set, chosen before writing, not faked with EQ. | inference |
| round_robins | Essential. The kick repeats often and identically in most styles, which makes it one of the most exposed instruments for the machine-gun error. | inference |
| release_samples | The decay tail and any port "whoosh" after the beater leaves the head is part of the character; a very fast, glued pattern can lose it on some patches. | inference |
| pedal_or_breath_behavior | Not applicable here; the physical kick pedal is covered under `physical_noise` and `feasibility`, not a sustain-pedal behaviour. | inference |
| transition_samples | Not applicable; there is no note-to-note transition on a kick. | inference |
| mic_or_room_behavior | As for the rest of the kit: blending close, overhead, and room capture changes how much shell and room, versus beater click, is heard. | inference |
| likely_fake_sounding_errors | Identical kicks with no round robin; a kick pattern faster than the head's natural decay can actually clear, which no real muffling setting produces live; a kick mixed with no low-frequency body under a driving part. | inference |
| organic_programming_methods | Bias velocity slightly by metrical position (`metrical_accent`, small magnitude, `shared/HUMAN_PERFORMANCE_SCHEMA.md`); let fast, dense patterns show `performer_fatigue`; leave the kick untouched by timing deviation only where it is genuinely the arrangement's marker (see Ensemble behaviour below), not by default. | inference |

### Snare

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A shell with a batter head on top and a snare head underneath, the latter crossed by a set of wire or gut snares held against it. Striking the batter head sets up air-borne and shell-borne vibration that reaches the snares, which then buzz against the snare head. | sourced: FORSYTH-1914 |
| attack_behavior | Stick tip, shoulder, or rimshot (stick and rim together) each strike a different area with a different implement contact, producing genuinely different attack spectra, not the same attack at different volumes. A drumhead is elastic and returns the stick's energy; a stroke can be thought of, and taught, as a controlled bounce off the head rather than a dead blow. | sourced: DAHL-2003-THESIS |
| sustain_behavior | No sustain in the wind or string sense; the head and snares ring briefly after the strike and are then either left to decay or damped by hand or by the next stroke landing. | inference |
| release_behavior | The snare-wire buzz continues for a short, audible tail after the stick leaves the head; how long depends on wire tension and head tuning. | inference |
| dynamic_timbre_change | Louder strokes are prepared from a measurably greater height and struck at higher velocity; the same study found the interval before an accented stroke was lengthened, more so at softer dynamics, so the accent is not only a louder hit but a timed one. | academic: DAHL-2004-ACCENT |
| register_character | The wires give the snare its bright, dry, cutting identity; disengaging them removes that identity and leaves a small, unsnared drum, closer in character to a tom. | inference |
| practical_range | Not pitched; register is set by head tuning (tighter is brighter and drier, looser is fatter and lower) and by wire tension, both persistent states rather than per-note choices. | inference |
| tessitura | Not applicable in the pitched sense; the practical equivalent is the tuning/wire-tension window a part is written to sit in. | inference |
| articulation_logic | Distinct strokes, each its own sound: full stroke, tap, rimshot, cross-stick (stick laid across the head and struck against the rim), buzz/press roll, flam, drag, and the alternate-implement families (brushes, hot rods) that change the attack profile of every stroke, not just its level. | sourced: FORSYTH-1914; PAS-RUDIMENTS-1984 |
| phrase_limits | Bound by two hands. A closed or "buzz" roll is a pressed, bounced stroke, not a single continuous scrape, and it still alternates hands: each hand delivers a multi-bounce press before handing off, historically drilled as the "long-roll" or "Daddy-Mammy" (LL-RR-LL-RR), described as the stick's rebound becoming, with practice, a controlled bounce rather than a fresh stroke. Treating a closed roll as one hand holding a buzz indefinitely, or as hand-to-hand with no press at all, both misdescribe it. | sourced: FORSYTH-1914 |
| transitions | No legato; consecutive notes are discrete strokes, though a roll blurs them into a continuous texture by design. | inference |
| repeated_note_behavior | Real repeated strokes alternate hands by default, and the two hands do not strike with identical force; the Percussive Arts Society's standard rudiment set exists specifically to name and drill the resulting sticking and accent patterns (single strokes, doubles, paradiddles, flams, drags, ratamacues), which is why a programmed part built from named rudiments reads as played rather than sequenced. | sourced: PAS-RUDIMENTS-1984 |
| vibrato | None. | inference |
| pitch_instability | Minor drift from head tension changing with heat and humidity over a set; not a real-time control. | inference |
| resonance | The snare wires buzz sympathetically when nearby drums or loud instruments excite a matching frequency, not only when the snare itself is struck; a patch with no sympathetic buzz is missing a real part of the instrument's presence in a mix. | inference |
| physical_noise | Wire buzz itself is a noise component as much as a pitch; stick-on-rim contact noise on a rimshot or cross-stick; the mechanical click of stick-to-stick or stick-to-hardware contact during fast sticking. | inference |
| feasibility | Two hands, one stroke each at a time; a rimshot or cross-stick uses one hand for the whole gesture, so it cannot combine with a second simultaneous stroke from the same hand. | inference |
| ensemble_behavior | Carries backbeat and groove definition in most popular styles; where the kit (and the snare within it) is the timekeeping reference, see the marker-part discussion below, which this file's evidence narrows rather than assumes. | academic: RASANEN-2015 |
| recording_behavior | Usually close-miked top and bottom (to capture the wire buzz separately), plus present in the overhead and room mics; a kit recorded with only a close top mic is missing the wire detail and the room's contribution to the crack of the sound. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short notes trigger the sample; length beyond the sample's own decay does nothing extra except on a roll articulation, which is its own sustained sample or repeated-note construction. | inference |
| overlap | Not a legato instrument in the melodic sense; no overlap requirement between discrete strokes. | inference |
| velocity | In a well-built multi-layer instrument, velocity crossfades or switches between several independently recorded dynamic layers (tap or ghost, normal, accent, rimshot); a low-velocity ghost note reaching a genuinely recorded soft layer is the system working as designed, not an error. The failure is a library that lacks enough recorded layers and instead scales the gain of one louder sample down to fake a soft stroke, or a programmer who manually lowers a normal stroke's velocity instead of triggering the instrument's actual ghost layer. | inference |
| continuous_dynamics | Not a sustaining instrument for single strokes; a roll's dynamic shape is built from the individual stroke velocities within it (or a dedicated roll articulation's own dynamic control), not a single continuous-controller sweep standing in for the strokes. | inference |
| expression | Not the primary control for a single stroke; on a roll articulation, an expression or CC lane may shape the crescendo the recorded roll allows. | inference |
| articulation_switching | Rimshot, cross-stick, brushes, and hot rods are separate recorded sample sets. A patch that fakes cross-stick with EQ on a normal stroke, or brushes with a filtered stick sample, is audible as the substitution it is. | inference |
| round_robins | Essential, and the clearest case in the kit for the machine-gun error, because the snare repeats more than any other drum in most grooves. | inference |
| release_samples | The wire-buzz tail after the stroke is a release behaviour; gluing snare notes end to end in a fast pattern can truncate it on patches that model it as a release sample. | inference |
| pedal_or_breath_behavior | Not applicable. | inference |
| transition_samples | Not applicable between discrete strokes; a roll articulation may itself be a single sustained or repeated-trigger construction rather than a transition between two notes. | inference |
| mic_or_room_behavior | Close top/bottom plus overhead and room, as above; the wire detail lives mostly in the close mics, the crack and body in the overheads. | inference |
| likely_fake_sounding_errors | A ghost note made by turning down a normal stroke's velocity on a patch with a real ghost layer available; identical repeated snare hits with no round robin; a closed roll played as one continuous unbroken buzz with no hand alternation audible in the accent pattern; a rimshot faked by boosting a normal stroke's high end. | inference |
| organic_programming_methods | Build repeated-note and fill passages from named rudiments (single strokes, doubles, paradiddles, flams, drags) so the sticking is real rather than arbitrary; use `flam` (two limbs arriving fractionally apart) and `velocity_asymmetry` (a hand does not strike evenly) for two-hand passages; use `metrical_accent` for backbeat and fill emphasis; use the accent's own timing lengthening documented above, rather than only its velocity, when programming a strong accent. | sourced: PAS-RUDIMENTS-1984 + academic: DAHL-2004-ACCENT |

### Toms

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Single- or double-headed tuned drums, typically two to five in a kit, each shell size and head tension setting a different fundamental. | inference |
| attack_behavior | Stick tip strikes near the centre give the fullest fundamental; off-centre strikes bring in more of the head's higher, inharmonic modes, the same physics that governs where a timpanist strikes (see `PERCUSSION.md`). | academic: WOODHOUSE-TUNED-DRUMS |
| sustain_behavior | Decay is longer and more pitched than the snare's, shorter than a resonant, unmuffled kick's; an unmuffled tom rings audibly after the stroke. | inference |
| release_behavior | Ring continues until it decays naturally or is damped by hand, a gel/tape dampener, or internal muffling. | inference |
| dynamic_timbre_change | As with the snare, a harder stroke is prepared from greater height and struck at higher velocity, and the ratio of attack transient to ringing body shifts with force. | academic: DAHL-2004-ACCENT |
| register_character | Toms are pitched relative to each other and are usually voiced high to low across a fill; each drum's usable dynamic range narrows toward its tuning extremes. | inference |
| practical_range | Not fixed; set by shell size and head tension per kit, typically spanning a little over an octave across a four- or five-piece set. A specific tuning is a calibration fact. | inference |
| tessitura | The comfortable tuning window for each shell size; pushed far outside it, a head either goes slack and dead or chokes tight and thin. | inference |
| articulation_logic | Full stroke, rimshot (less common than on snare but used), and the same alternate-implement families (brushes, hot rods) as the snare. | inference |
| phrase_limits | Two hands; moving between toms takes physical travel time across the kit, which is why fast tom fills follow the drums' physical layout rather than an arbitrary pitch order. | inference |
| transitions | No legato; a fill crossing several toms is a sequence of discrete strokes whose order is constrained by hand-to-drum travel. | inference |
| repeated_note_behavior | As the snare: alternating hands by default, with the same rudiment vocabulary available for tom-to-tom sticking patterns. | sourced: PAS-RUDIMENTS-1984 |
| vibrato | None. | inference |
| pitch_instability | Head tension drifts with heat, humidity, and heavy play over a set. | inference |
| resonance | Unmuffled toms ring and can excite sympathetic response in nearby drums (including the snare's wires). | inference |
| physical_noise | Stick-on-shell rim clicks when a fill grazes the rim; hardware and mounting-system resonance on some kits. | inference |
| feasibility | Two hands, one stroke each; a fill that asks for more simultaneous strokes than two hands, or a hand-crossing pattern no player's reach allows, is not playable. | inference |
| ensemble_behavior | Mostly a fill and accent voice rather than a continuous pulse; less often the arrangement's marker than the hi-hat or ride. | inference |
| recording_behavior | Close-miked per drum, plus present in overheads and room; close mics emphasise attack and can make the toms sound smaller and drier than they are live. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short notes trigger the sample; sustain is carried by the sample's own decay, not by holding the note. | inference |
| overlap | No legato requirement. | inference |
| velocity | Selects among recorded dynamic layers, as the snare; a fill's dynamic shape should come from real per-stroke velocity variation, not a uniform value repeated across the pattern. | inference |
| continuous_dynamics | Not applicable to single strokes; each hit is its own event. | inference |
| expression | Not applicable in the sustained-instrument sense. | inference |
| articulation_switching | Rimshot and alternate-implement (brush, hot rod) sounds are separate sample sets. | inference |
| round_robins | Essential wherever a fill repeats a pitch quickly, which is common in tom-based fills. | inference |
| release_samples | The ring after the stroke is part of the character; truncating tom notes in a fast fill can cut it audibly on patches that carry a real decay tail. | inference |
| pedal_or_breath_behavior | Not applicable. | inference |
| transition_samples | Not applicable between discrete strokes. | inference |
| mic_or_room_behavior | As the rest of the kit; close mics alone lose the room's contribution to how a tom fill "opens up" live. | inference |
| likely_fake_sounding_errors | A fill using more than two simultaneous voices; identical repeated single-tom hits with no round robin; a fill order that ignores physical kit layout (jumping between non-adjacent drums faster than a hand could travel); toms with no ring, sounding gated even when nothing calls for that. | inference |
| organic_programming_methods | Use the same rudiment-based sticking as the snare for tom-to-tom patterns; respect hand-to-drum travel time between non-adjacent toms; vary velocity per stroke with `velocity_asymmetry`; let a fast fill show `performer_fatigue` only where the brief wants a driving, effortful feel. | sourced: PAS-RUDIMENTS-1984 |

### Hi-Hat

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Two cymbals mounted face to face on a stand, the lower fixed and the upper moved by a foot pedal; closed, they clap together and choke each other's ring, and open, they ring more like a pair of small crash cymbals. | inference |
| attack_behavior | Stick strikes on the bow, edge, or bell of the top cymbal each give a different attack colour; a foot-only "chick" (closing the pedal to strike the cymbals together) is a separate sound from any stick strike. | inference |
| sustain_behavior | Sustain is continuously variable with the pedal position: fully closed gives almost none, fully open lets the cymbals ring like a crash. | inference |
| release_behavior | Closing the pedal after an open stroke chokes the ring audibly; how fast depends on how quickly the foot closes. | inference |
| dynamic_timbre_change | Louder strikes bring in more of the cymbals' upper partials, as with any struck cymbal; openness itself is a second, independent dynamic-like control over brightness and decay. | inference |
| register_character | Bright, metallic, and higher in perceived pitch than the ride in most kits, though neither is tuned to a musical pitch. | inference |
| practical_range | Not pitched; "range" here is the continuum from closed to fully open. | inference |
| tessitura | Not applicable. | inference |
| articulation_logic | Closed, half-open (a specific, named state, not just "partway"), open, foot chick, foot splash (a fast open-close with no stick), and bell/edge/bow stick placement are each distinct sounds. | inference |
| phrase_limits | One hand for stick strokes, one foot for openness; a pattern that needs the hi-hat foot to do something else at the same instant (for example, operate a second kick pedal) is not playable by one player. | inference |
| transitions | Openness is continuous, so a "transition" here is a pedal move between two openness states while the hand continues striking, not a note-to-note slur. | inference |
| repeated_note_behavior | Sixteenth-note hi-hat patterns are a classic case where a single player's own microtiming, not a metronomic grid, has been shown to carry the groove (see Ensemble behaviour). | academic: RASANEN-2015 |
| vibrato | None. | inference |
| pitch_instability | Not applicable in the pitched sense; the openness state is the analogous variable. | inference |
| resonance | Closed cymbals damp each other; open, they resonate together more than a single suspended cymbal because of the close second surface. | inference |
| physical_noise | Pedal spring and clutch-mechanism noise, audible as a squeak or click on some hardware, independent of any cymbal strike. | inference |
| feasibility | One hand and one foot; conflicts arise if the foot is needed elsewhere at the same instant. | inference |
| ensemble_behavior | The hi-hat is the part of the kit most often treated as the pulse-carrying marker, and the part a live-feel groove is most likely to actually live in: a peer-reviewed analysis of a well-known drummer's one-handed hi-hat part found long-range correlated timing and amplitude fluctuations and a two-bar periodic pattern, not a rigid grid, and concluded the part's "subtle modulation" was intentional musicality rather than mechanical precision. Treating the hi-hat as an untouched marker by default, in styles where this is how the groove actually works, removes exactly what makes the part sound played; a genuinely mechanical or grid-built style is a different, legitimate case, and the decision belongs in `performance_state.realism_target`, not a blanket rule. | academic: RASANEN-2015 |
| recording_behavior | Usually close-miked on its own, and prominent in the snare and overhead mics too because of its physical proximity to both. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short notes trigger a strike sample; a held note does not itself control openness. | inference |
| overlap | Not applicable; hi-hat openness, not note overlap, carries the continuous behaviour here. | inference |
| velocity | Selects among stroke dynamic layers as with any struck cymbal. | inference |
| continuous_dynamics | Not the primary continuous control on this instrument; openness is. | inference |
| expression | Not the primary control; see pedal/openness below. | inference |
| articulation_switching | Closed, half-open, open, foot chick, and foot splash are separate recordings or a modelled continuum; bell/edge/bow placement is a further separate set on some libraries. | inference |
| round_robins | Essential; repeated identical hi-hat strokes are extremely exposed because the pattern repeats so often. | inference |
| release_samples | Choking an open hi-hat by closing the pedal needs its own recorded or modelled transition, distinct from letting an open stroke ring out. | inference |
| pedal_or_breath_behavior | Openness is a continuous state set by the foot, persisting until the foot moves again, not a set of unrelated discrete notes; this is the instrument's defining programming fact. | inference |
| transition_samples | A pedal move between openness states while notes continue needs either a modelled continuum or enough discrete openness stages that the steps are not audible as steps. | inference |
| mic_or_room_behavior | Close mic dominant, with real bleed into the snare and overhead mics on a recorded kit. | inference |
| likely_fake_sounding_errors | Open and closed hits programmed as unrelated one-shot samples with no continuous state and no audible foot closing them; a sixteenth-note hi-hat pattern quantised with no microtiming at all in a style where that pattern is normally the most expressive part of the groove; identical repeated strokes with no round robin. | inference |
| organic_programming_methods | Model openness as a continuous, persistent state driven by a foot, not discrete notes; where the style calls for it, apply a named microtiming model (see `shared/RHYTHM_SYSTEMS/MICROTIMING_AND_GROOVE.md`) to the hi-hat pattern specifically, on the evidence above, rather than leaving it untouched by default; reserve the untouched, marker treatment for a part the brief wants mechanically exact. | academic: RASANEN-2015 |

### Cymbals (Ride and Crash)

Struck cymbals other than the hi-hat pair. The ride is played continuously as a timekeeping and
colour voice; crashes are struck occasionally as an accent and decay for seconds. Both are the same
kind of object (a shaped bronze-alloy disc) played differently; differences are named in the rows
below rather than split into two cards, because almost every row besides articulation and phrase role
is shared.

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A cast or sheet bronze-alloy disc, tapered so it contacts a striking implement first at the edge rather than flat across its face; size, weight, and alloy set its pitch content and decay. | sourced: FORSYTH-1914 |
| attack_behavior | Where the stick lands changes the sound: the bow (the flat main body) gives a defined "ping" with stick definition audible over the wash, the edge gives a fuller, washier attack, and the bell (the raised centre dome) gives a sharp, high, cutting attack used for accents. | inference |
| sustain_behavior | Rings for a long time once struck; the ring is the note, and a cymbal cut off early by a short note length is audibly wrong rather than merely stylised. | inference |
| release_behavior | Decays on its own unless choked: physically grabbing the cymbal immediately after the strike stops the ring, implemented on a kit by hand or by a felt/mute; the same "choke" idea is documented for orchestral cymbals as a note-off or aftertouch message when modelled virtually. | sourced: FORSYTH-1914 |
| dynamic_timbre_change | Harder strikes bring proportionally more high-partial energy; a crash struck softly is a different, darker sound, not a quiet version of a hard crash. | inference + to-verify: what would settle this is not recorded |
| register_character | Rides sit as a continuous, articulate pulse; crashes sit as a wash that briefly covers everything around it before decaying clear again. | inference |
| practical_range | Not pitched to a specific note; "range" is size and weight, which set brightness and decay length rather than a musical pitch. | inference |
| tessitura | Not applicable. | inference |
| articulation_logic | Ride: bow tip taps for the ticking pulse, bell hits for accents, occasional crash-ride (struck harder, washier) at high dynamic. Crash: edge strikes, sometimes choked immediately, sometimes let ring. | inference |
| phrase_limits | One hand per cymbal strike; a ride pattern with simultaneous bell accents from the other hand elsewhere on the kit is two separate limb events, not one. | inference |
| transitions | No legato; a roll (rapid alternation, or a rolled mallet tremolo in concert settings) is the closest thing to a sustained gesture and is a distinct technique, not a fast repeated single stroke at the kit. | sourced: FORSYTH-1914 |
| repeated_note_behavior | A ride pattern repeats the same physical gesture at high frequency; real playing varies stick contact point and force slightly stroke to stroke, which is most of what keeps a fast ride pattern from sounding looped. | inference |
| vibrato | None. | inference |
| pitch_instability | Not applicable in the pitched sense. | inference |
| resonance | Cymbals ring for seconds and overlap whatever follows; a crash under a quiet passage is audible for longer than a programmer expects if the previous bar was loud. | inference |
| physical_noise | Stick-on-bell click is part of a bell accent's character, not an unwanted artifact. | inference |
| feasibility | One hand per strike; a choke needs a hand (or a foot-operated mute on some setups) free at the moment of the choke. | inference |
| ensemble_behavior | The ride, like the hi-hat, frequently carries the pulse and is a candidate marker part; crashes are accent events tied to structural moments (section changes, downbeats) rather than a continuous pulse. | inference |
| recording_behavior | Heard mostly through the overhead and room mics on a recorded kit, with a close mic (if used at all) adding definition rather than replacing the overheads; an all-close-mic cymbal sound is thin compared with a real kit in a room. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Notes shorter than the cymbal's natural decay do not shorten a real cymbal; a patch that truncates on note-off rather than letting the sample ring is misrepresenting the instrument unless deliberately choked. | inference |
| overlap | Not a legato instrument in the melodic sense. | inference |
| velocity | Selects among recorded dynamic layers, which for a good crash patch are genuinely different recordings (a soft crash is not a hard crash turned down), the same principle as the snare's ghost-note layers above. | inference |
| continuous_dynamics | Not applicable to a single struck note; a rolled cymbal's crescendo comes from the roll's own recorded or modelled dynamic shape. | inference |
| expression | Not the primary control for a single strike. | inference |
| articulation_switching | Bow, edge, and bell strikes, and choked versus rung notes, are separate recordings or explicitly modelled states. | inference |
| round_robins | Essential for the ride pattern especially, since it is struck at high repetition; less critical, but still relevant, for crashes if a part crashes more than once in a passage. | inference |
| release_samples | A real release-samples case: a cymbal glued end to end with the next hit, or with no note-off event at all, cannot show its natural decay or a deliberate choke. | inference |
| pedal_or_breath_behavior | Not applicable, except where a choke is implemented through a pedal or continuous controller rather than a discrete note-off. | inference |
| transition_samples | Not applicable between discrete strikes. | inference |
| mic_or_room_behavior | Overhead- and room-dominant, as above; this is where a kit's cymbals most need the room to sound real. | inference |
| likely_fake_sounding_errors | Cymbals cut off by short note lengths (a direct instance of `COMMON_ERRORS.md` item 12); a ride pattern with identical stick contact and velocity on every stroke; a crash choked on every hit regardless of musical context; a soft crash that is audibly a loud sample turned down rather than a different recording. | inference |
| organic_programming_methods | Vary ride stroke velocity and, where the library supports it, contact point, per beat rather than uniformly; let crashes ring their full length unless the passage specifically calls for a choke, and record the choke as a deliberate event rather than a default; use `velocity_asymmetry` for hand-to-hand variation in fast ride patterns. | inference |

---

## What the instrument is

Several unrelated percussion instruments arranged so that one person can play them with two hands
and two feet, and the arrangement is the instrument: what a kit can play is decided by where the
drums and cymbals are and how many limbs are free, not by what a score's notes say in isolation.
[inference]

## Range and register

Not pitched in the melodic sense, so "range" means the kit's vocabulary of surfaces and the zones on
each, laid out in the cards above. Two facts cut across every drum on the kit: **tuning and muffling
are persistent states, not per-note choices** (a head is tightened, loosened, or muffled between
passages, not note by note), and **the striking implement changes the sound as much as the surface
does**: sticks, brushes, and hot rods (bundled dowels that split the difference between the two) are
each a separate recorded sample set, because the attack transient they produce is physically
different, not an EQ variant of the same recording. [inference]

## Articulation and note transitions

Velocity's job on a well-built kit patch is to select among genuinely different recordings first and
set level within that recording second. Where the prior version of this file said a ghost note "is a
different sample, not a quieter one," that overstates the case: **in most multi-layer kits, a ghost
note *is* the low-velocity layer**, reached by velocity exactly as the schema intends, because a real
soft stroke was recorded at that dynamic and mapped to that velocity range. The actual failure mode,
and the one worth naming, is narrower: a library without enough recorded layers filling the gap by
scaling a louder sample's gain down, or a programmer manually lowering a normal stroke's velocity
instead of finding the instrument's real ghost layer. Both produce the same audible tell, a stroke
that gets quieter without changing colour, but the cause is a missing or misused layer, not velocity
itself doing the wrong job. [inference]

The specific MIDI velocity band a ghost note or an accent lands in is a property of one installed
instrument, not a fact about drumming, and belongs in a calibration profile rather than here.

Rudiment-based sticking is the named cause behind most of the dynamic and timing texture in a real
drum part. The Percussive Arts Society's standard 40 International Drum Rudiments, organised into
roll, diddle, flam, and drag families, are not decoration: they are how a player is taught to
distribute strokes between two hands so that repeated notes, accents, and rolls come out with a
particular, reproducible feel rather than an arbitrary one. A paradiddle (RLRR LRLL) played on a
kit's toms produces a specific accent pattern purely from which hand lands where; programming the
same rhythm with uniform alternation, or with accents placed anywhere convenient, produces a
different, less idiomatic result even at identical note values. [sourced: PAS-RUDIMENTS-1984]

Rebound is physical, not incidental. A drumhead is elastic and returns the stick's energy; players are
taught named stroke types, tap, upstroke (or pull-out), downstroke (or control stroke), and full (or
free) stroke, that plan how much of that rebound is used or caught before the next stroke. A loud
passage of repeated strokes typically rides the rebound to full height between hits; a passage
alternating loud and soft strokes actively catches or releases the stick at different heights to set
up the next dynamic. Measured preparatory stick height and striking velocity both rise with intended
dynamic level and, further, rise specifically before an accented stroke, which is also timed slightly
later than a strictly even grid would place it, more so at softer dynamics. This is a physical account
of why accents in real playing carry both a velocity and a small timing signature together, and it is
the basis for treating accent as a `metrical_accent` timing effect as well as a velocity one, not
velocity alone. [sourced: DAHL-2003-THESIS + academic: DAHL-2004-ACCENT]

The closed, "buzz" orchestral-style roll sometimes borrowed into kit playing (and the kit's own
multi-bounce rolls, taught the same way) is a pressed stroke that still alternates hands: LL-RR-LL-RR,
the second stroke in each pair becoming, with practice, a controlled bounce rather than a fresh
attack. A programmed roll built as one hand holding a buzz with no hand-to-hand structure at all
misrepresents the technique; so does a roll built as plain alternating single strokes with no bounce
character. [sourced: FORSYTH-1914]

## Physical constraints

```text
FOUR LIMBS.
Two hands and two feet, and each can do one thing at a time.
```

A right hand on the hi-hat cannot simultaneously hit a tom across the kit. A left foot holding the
hi-hat closed cannot also play a second kick pedal. The hands cross and uncross, which takes time.
This is the hard validator rule that catches the most programmed-drum errors. [inference]

**Hi-hat openness is a continuous state set by a foot**, not a set of separate instruments, and it
persists until the foot moves. Programming open and closed hats as unrelated notes with no continuous
state produces a hat part with no foot in it. [inference]

## Phrase behaviour

A groove is a repeating pattern with variation inside it, and the variation is sticking and ghost
notes rather than new notes. **Fills must be playable unless the brief wants them not to be**: a fill
is a hand-to-hand, hand-to-drum sequence across the kit, and one requiring three hands, an impossible
crossing, or travel between non-adjacent drums faster than a hand can move reads as a machine even
when every individual hit sounds real. [inference]

Cymbals ring. A crash decays for seconds and overlaps whatever follows it; cutting it off with a note
length shorter than the sample is audible and is `COMMON_ERRORS.md` item 12 in its clearest kit-level
form. [inference]

## Ensemble behaviour

The prior version of this file treated the kit as "usually a marker part," on the reasoning that it
is the arrangement's timekeeper and so any deviation applied to it moves the reference everything
else is heard against. **That is too broad a rule for most live-feel genres.** A peer-reviewed
analysis of a well-known drummer's hi-hat part, recorded without a metronome, found long-range
correlated fluctuations in both timing and dynamics, short-range anticorrelation (a longer interval
tending to be followed by a shorter one), and a two-bar periodic pattern in the amplitude of the
sixteenth notes; the authors describe this "subtle modulation" as the source of the part's musicality,
not noise around a grid the part is otherwise obeying. In funk, soul, classic rock, R&B, and any
style built on a felt pocket, the kit's own microtiming, above all in the hi-hat or ride, **is** the
groove, and stripping it out to protect a reference removes the thing the reference was supposed to
serve. [academic: RASANEN-2015]

This does not overturn the marker-part idea; it narrows it. A grid-built or deliberately mechanical
style (much EDM, some pop, a kit programmed to lock to a click a vocal was already tracked against) is
a real and legitimate case where the kit, or a specific element of it, should stay untouched. The
decision belongs in `performance_state.realism_target` and `timing_character.marker_parts_excluded`,
made per track rather than assumed by default, and the plan should say which part, if any, is being
held as the reference and why. Where a kit does carry deviation, the timekeeping element (commonly
the hat or ride) is still usually left tighter than the rest of the kit, because *something* has to
anchor the ensemble even in a loose performance. [inference]

The kick and bass relationship is an arrangement decision. See `BASS.md`.

## Recording behaviour

**Room sound and microphone bleed are part of a recorded kit.** The snare is in the overheads, the
hat is in the snare mic, and the kit is heard as one instrument in one room. Sampled kits offering
close, overhead, and room microphone positions are offering the same kit at different distances, and
using only close mics produces a kit that is detailed and dead. [inference]

Bleed also means the room is triggered by every hit. A kit with a large room sound on the snare and
none on anything else is not a kit in a room, it is a snare in a room next to a dry kit. [inference]

## Programming it: the control model

Product-specific facts (which controller carries dynamics, exact velocity zone boundaries, how a
choke is implemented, which mic positions exist) belong in a calibration profile, not here. What
carries across any well-built kit instrument:

```text
velocity:
  selects: a recorded dynamic layer first, level within it second
  a ghost note reached by low velocity into a real soft layer is correct, not a failure
hi_hat:
  openness: a continuous, persistent state set by a foot
  extras: foot chick, foot splash, and the closing sound itself
cymbals:
  bow, edge, bell: separate attack colours, not EQ variants
  choke: a deliberate event with its own implementation, not a default
snare:
  ghost, rimshot, cross-stick, brushes, hot rods: separate recorded sample sets
  closed roll: a pressed, alternating-hand stroke, not one held buzz
round_robins:
  essential everywhere on the kit; the snare and hi-hat are the most exposed
microphones:
  close, overhead, room; bleed is modelled or recorded, not skipped
```

[inference]

## Programming it: what makes it sound real

- Validate four limbs before anything else.
- Build repeated notes and fills from named rudiments (single strokes, doubles, paradiddles, flams,
  drags), not arbitrary alternation. [sourced: PAS-RUDIMENTS-1984]
- Let accents carry a small timing lengthening as well as extra velocity, on the evidence that real
  players prepare and place accented strokes slightly differently in time, not only louder.
  [academic: DAHL-2004-ACCENT]
- Program hi-hat openness as a continuous state, and give the sixteenth-note hat (or ride) pattern its
  own microtiming where the style is a live-feel one, rather than holding it as an untouched marker by
  default. [academic: RASANEN-2015]
- Reach ghost notes through the instrument's real soft-velocity layer; treat a gain-scaled substitute
  as the error, not low velocity itself.
- Let cymbals ring for their full sample unless deliberately choked, and treat a choke as an event with
  a cause, not a habit.
- Play a closed roll as a pressed, hand-alternating stroke, not a single held buzz.
- Keep fills inside four limbs and real hand-to-drum travel time, or record the exception.
- Where the kit does carry timing deviation, still leave the chosen timekeeping element tighter than
  the rest, and name marker parts explicitly rather than assuming the whole kit is one.

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Kit-specific tells:

- the same snare or hi-hat sample repeated at one velocity, error 1 in its most exposed kit form;
  [inference]
- a ghost note made by turning down a normal stroke instead of reaching the instrument's real soft
  layer; [inference]
- open and closed hats with no continuous state and no foot; [inference]
- a closed roll played as one continuous unbroken buzz with no hand-alternation structure;
  [sourced: FORSYTH-1914]
- fills that need more than four limbs, or that jump between non-adjacent drums faster than a hand
  can travel, error 6 in kit form; [inference]
- cymbals truncated by short note lengths, error 12; [inference]
- close microphones only, with no room and no bleed; [inference]
- a sixteenth-note hi-hat or ride pattern quantised dead flat in a style where that pattern is
  normally the part carrying the most feel; [academic: RASANEN-2015]
- humanised timekeeping where a part was deliberately declared a marker, error 13, and the reverse
  failure this file corrects: a marker declared by default with no evidence it should be one.
  [inference]

## What the Performance Director needs from this file

- `limb_or_finger_conflicts`: the four-limb rule, applied per tick, including the hi-hat foot.
- `simultaneity_exceeded`: more than four simultaneous hits, or more than two hand strikes at once.
- `articulation_unavailable`: ghost, rimshot, cross-stick, brushes, hot rods, and choke are separate
  recordings; a request for one the instrument lacks is reported, not silently substituted with a
  gain-scaled stand-in.
- `flam` and `velocity_asymmetry` are the recognised imperfection causes for hand-to-hand strokes;
  `performer_fatigue` applies to long, fast, repeated passages on one limb (notably the kick foot).
- Marker part declaration is a per-track decision, not a default: the plan should name which element,
  if any, is held untouched as the reference, on the evidence in Ensemble behaviour above.

## Sources and what to verify

- [inference] and [inference] claims above rest on: Cecil Forsyth's 1914 orchestration text (snare and
  cymbal construction and technique, read at section depth, examples orchestral but the physical
  mechanisms are the instrument's, not the ensemble's); the Percussive Arts Society's 40 International
  Drum Rudiments (read in full); two studies by Sofia Dahl on drumstick movement, rebound, and accent
  timing and velocity (read at section depth); one peer-reviewed study of a drummer's hi-hat
  microtiming (read at section depth); and one page of an acoustics textbook on tuned-drum vibration
  modes (read at section depth, general physics, not kit-specific). Full citations in
  `research/sources/INSTRUMENT_SOURCES.md`.
- **To verify**: cymbal and drumhead decay spectra, and the general physics of why a struck membrane's
  overtones are inharmonic, in Fletcher and Rossing, *The Physics of Musical Instruments*.
  [inference], not opened this pass.
- **To verify**: the specific attack-colour differences between bow, edge, and bell cymbal strikes are
  widely taught (present in most kit-percussion methods) but were not opened at section depth in a
  named pedagogical source this pass; kept as [inference] rather than [inference] for that reason.
- **Not available, and correctly absent from this file**: any MIDI velocity number, controller
  assignment, or millisecond latency for a specific product. Those are calibration-profile facts.
