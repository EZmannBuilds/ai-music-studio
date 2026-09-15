# Percussion (Orchestral)

Orchestral percussion: timpani, the orchestral snare drum, bass drum, suspended and clash cymbals,
tam-tam, triangle, tambourine, woodblock and temple blocks, and castanets in their orchestral (not
flamenco hand) form. The drum kit has its own page, `DRUM_KIT.md`. Tuned mallet percussion has its
own page, `MALLETS.md`. Hand-struck drums have their own frame page, `HAND_PERCUSSION.md`, which
routes each tradition to its own page; **tabla, and any other drum belonging to a specific living
tradition, are not on this page** for the same reason.

> Evidence: read at section depth this pass: Cecil Forsyth's 1914 *Orchestration* (timpani, side
> drum, bass drum, cymbals, gong, triangle, tambourine, and castanets chapters; source ID
> FORSYTH-1914), Rimsky-Korsakov's *Principles of Orchestration* (timpani range and the register
> grouping of unpitched percussion; RIMSKY-1913), the Percussive Arts Society's 40 rudiments
> (PAS-RUDIMENTS-1984, reused from `DRUM_KIT.md` for the orchestral snare's sticking), one acoustics
> textbook page on tuned-drum membrane modes (WOODHOUSE-TUNED-DRUMS), and two university
> percussion-studio pages on temple blocks and wood blocks (BYU-TEMPLE-BLOCKS, BYU-WOOD-BLOCKS). Roll
> rates, exact retuning times, and cymbal/drumhead decay spectra were not opened at section depth and
> are left to-verify rather than invented. Read depths and full citations are in
> `research/sources/INSTRUMENT_SOURCES.md`; the claims and their limits are in `research/instruments/PERCUSSION.md`.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## Behaviour cards

### Timpani

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A basin-shaped copper or alloy shell with a calfskin or synthetic head stretched across it; tension, adjusted by pedal, tunes it to a definite pitch, unusually for a drum. | sourced: FORSYTH-1914 |
| attack_behavior | Struck about halfway between rim and centre; striking near the centre maximises unpitched, axisymmetric modes and gives little of the tuned modes, which all have a nodal line through the centre, so players avoid the centre to get a clear pitch. | sourced: FORSYTH-1914 + academic: WOODHOUSE-TUNED-DRUMS |
| sustain_behavior | Rings after the stroke; a tremolo (roll) sustains the note and can carry the most gradual crescendo or diminuendo in the percussion section. | sourced: RIMSKY-1913 |
| release_behavior | The drum must be damped by hand to stop ringing; a note with no damping instruction rings until it decays on its own. | inference |
| dynamic_timbre_change | Capable of every dynamic shade from thundering fortissimo to a barely perceptible pianissimo; mallet hardness, not dynamic level alone, sets how much attack transient rides on top of the pitched body. | sourced: RIMSKY-1913; FORSYTH-1914 |
| register_character | A modern set of two to four drums covers roughly the bottom two octaves of the piano's range between them; the set's historical core (Beethoven's era) covered a perfect fifth on the small drum and a perfect fourth on the large, tonic and dominant. | sourced: FORSYTH-1914; RIMSKY-1913 |
| practical_range | Historically, small drum Bb2-F3, large drum F2-C3, chromatically, with a third (and now often fourth) intermediate drum added since; Rimsky-Korsakov's own recommendation for a composer to rely on is roughly E2-G#3 across a set, noting a very small drum he had made could reach as high as Db4. | sourced: FORSYTH-1914; RIMSKY-1913 |
| tessitura | Each drum has a comfortable pedal range of roughly a fifth to a sixth; pushed to its extremes the head either goes slack (dull, unfocused) or overtight (choked, thin). | inference |
| articulation_logic | Single stroke, roll (sustained tremolo), and muffled/covered strokes (a cloth laid on the head, marked timpani coperti) are each a distinct technique. | sourced: RIMSKY-1913 |
| phrase_limits | A pedal change takes real time and, if made while the head is still ringing, is audible as a pitch bend (a glissando); a good timpanist with three or four drums can retune one during a sufficiently long rest, but a part that retunes a single drum instantly between adjacent bars is not playable. | sourced: FORSYTH-1914 |
| transitions | A pedal glissando between two pitches on one drum is a real, audible technique, distinct from silently retuning during a rest. | inference |
| repeated_note_behavior | A roll is single-stroke alternation at speed, sustaining rather than articulating each repetition separately. | inference |
| vibrato | None in the pitched-instrument sense; a struck head does not sustain a controllable pitch vibrato. | inference |
| pitch_instability | Head tension, and so pitch, drifts with temperature and humidity over a concert; this is why a timpanist checks and re-verifies tuning by ear against a reference pitch, listening for the beating between the struck note and the reference to slow and vanish as the pitch converges. | inference + to-verify: what would settle this is not recorded |
| resonance | The drum's ring after a stroke is the definitive pitched percussion sound in the orchestra; kettle-drums have a "ringing, resounding quality" that lets them prevail over other instrument groups even at moderate dynamics. | sourced: RIMSKY-1913 |
| physical_noise | Pedal mechanism noise (clicks, creaks) during a tuning change; mallet-on-head attack noise varies with mallet hardness. | inference |
| feasibility | One player generally plays one set of drums with two hands; a part asking for a pedal change and a simultaneous stroke on the same drum, or more simultaneous notes than the set has drums for, is not playable. | inference |
| ensemble_behavior | Ringing and resounding, timpani cut through orchestral texture more than their dynamic marking alone suggests, and pair naturally with pizzicato strings, harp, and other instruments of limited sustaining power. | sourced: RIMSKY-1913 |
| recording_behavior | Recorded at orchestral distance in a concert setting; close-miking isolates the attack from the shell's resonance in a way a hall recording does not. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short notes trigger a struck sample; sustain within a note is a roll articulation or a held tremolo construction, not a long single sample stretched by note length. | inference |
| overlap | Not a legato instrument. | inference |
| velocity | Selects among recorded dynamic layers and, where a library offers it, mallet-hardness layers; a swell (roll crescendo) needs the roll's own recorded or modelled dynamic shape, not a single note's velocity turned into a fade. | inference |
| continuous_dynamics | A roll's crescendo or diminuendo needs a drawn shape on whatever control the instrument reads for rolls, not a static velocity. | inference |
| expression | Where offered, a trim on top of the dynamic layer crossfade, not a substitute for it. | inference |
| articulation_switching | Open stroke, roll, and muffled (coperti) strokes are separate recordings; mallet hardness sets are a further separate set, not an EQ variant. | sourced: RIMSKY-1913; FORSYTH-1914 |
| round_robins | Important on repeated single strokes; less exposed than the snare because timpani parts repeat a single stroke less densely in most repertoire. | inference |
| release_samples | The head's ring after a stroke, and the sound of a hand damping it, are both real release behaviours a glued or ungapped part would lose. | inference |
| pedal_or_breath_behavior | The tuning pedal is a real, continuous control with audible transition time; treating a pitch change as instantaneous misrepresents the instrument, and a pedal glissando needs pitch-bend or per-note retuning, not a hard cut. | sourced: FORSYTH-1914 |
| transition_samples | A recorded or modelled glissando between two pitches on one drum, where available, is distinct from a cut between two separately tuned notes. | inference |
| mic_or_room_behavior | As with the rest of orchestral percussion, distance and hall reverberation are part of the sound; close-miked timpani in an otherwise distant orchestral mix reads as out of place. | inference |
| likely_fake_sounding_errors | Instant retuning between adjacent bars with no rest; a muffled note with no muffling programmed (full ring where the part calls for coperti); a roll built from identical single-velocity repeated strokes with no crescendo shape. | inference |
| organic_programming_methods | Give every pedal change the time a real transition needs, checked as a feasibility item; shape roll dynamics with a drawn curve rather than a flat velocity; use ensemble_spread or section_offset only where more than one timpanist is genuinely implied. | sourced: FORSYTH-1914 |

### Orchestral Snare Drum

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A shell with a batter head and, underneath a second snare head, a set of wires held against it; striking the batter head sets up vibration that reaches the wires, which buzz against the snare head and roughly double the perceived pitch of the tone compared with the drum unsnared. | sourced: FORSYTH-1914 |
| attack_behavior | The stick is thrown back by the head's elasticity after a stroke; skilled playing uses this rebound rather than fighting it. | sourced: DAHL-2003-THESIS |
| sustain_behavior | No true sustain; a roll is how the instrument sustains a sound at all. | inference |
| release_behavior | The wire buzz continues briefly after the stroke; a practically universal convention is to end a roll with a written, detached finishing stroke rather than an unmarked stop, because an unmarked stop "sounds untidy" except at the faintest pianissimo. | sourced: FORSYTH-1914 |
| dynamic_timbre_change | Accented strokes are prepared from greater height and struck at higher velocity than unaccented ones, and the interval before an accent is measurably lengthened, more so at softer dynamics: an accent is a small timing event as well as a loud one. | academic: DAHL-2004-ACCENT |
| register_character | Bright, dry, and cutting because of the wires; disengaging them (a lever most snares carry) turns the instrument into a small, dull tom. | sourced: FORSYTH-1914 |
| practical_range | Not pitched; register is set by head tuning and wire tension as persistent states. | inference |
| tessitura | Not applicable in the pitched sense. | inference |
| articulation_logic | A roll always alternates hands. Two rolls are distinct: the double-stroke open roll (LL-RR, the "daddy-mammy" Forsyth describes as the basis of rolling in 1914) and the multiple-bounce or closed roll, several bounces per stroke, hands still alternating; the rudiments list them separately, and a closed orchestral roll today is usually the second. Flam (two notes close together, the grace note quiet), drag (two to six grace strokes fused before an accented note), and the paradiddle (a sticking pattern, not a rhythm, that secures alternating left/right attack on successive strong beats) are named, separate techniques. | sourced: FORSYTH-1914; PAS-RUDIMENTS-1984 + inference |
| phrase_limits | Two hands; a persistent eight-note pattern is typically played as a paradiddle sticking to keep the hands alternating with a stronger rhythmic impulse, rather than strict L-R-L-R. | sourced: FORSYTH-1914 |
| transitions | No legato; a roll is the sustained case, notated as a slurred, trill-lined passage ending, in almost all cases, on a written detached stroke. | sourced: FORSYTH-1914 |
| repeated_note_behavior | Real repeated strokes alternate hands, drilled through the standard rudiment set (rolls, diddles, flams, drags). | sourced: PAS-RUDIMENTS-1984 |
| vibrato | None. | inference |
| pitch_instability | Minor drift with temperature and humidity over a performance. | inference |
| resonance | The wires buzz sympathetically when other loud instruments excite a matching frequency, not only when the drum itself is struck; this is a real, audible part of a good snare's presence in the orchestra, and a patch without it is missing something. | inference |
| physical_noise | The wire buzz is itself part-noise, part-pitch; snare-off (wires disengaged) removes it entirely. | inference |
| feasibility | Two hands, one stroke each; damping (for a short, stopped note) takes a hand that is then unavailable to strike. | inference |
| ensemble_behavior | Functions as a colour and rhythmic-emphasis voice rather than a continuous pulse in most orchestral writing, unlike its role on a kit. | inference |
| recording_behavior | Recorded at orchestral distance by default; the wire detail is more audible close than far, so close and hall balance is a real choice. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short notes trigger the sample; a roll is its own articulation, not a long note extended by length. | inference |
| overlap | Not a legato instrument. | inference |
| velocity | Selects among recorded dynamic layers, including a genuine soft/ghost layer where the library has one, the same principle documented for the kit snare in `DRUM_KIT.md`. | inference |
| continuous_dynamics | A roll's dynamic shape is built from the roll's own construction (recorded crescendo, or per-stroke velocities), not a single sustained control standing in for it. | inference |
| expression | Not the primary control on a single stroke. | inference |
| articulation_switching | Open stroke, flam, drag, rimshot (where used), and snares-off are separate recordings. | sourced: FORSYTH-1914 |
| round_robins | Important; repeated strokes are common in orchestral snare writing (marches, military topics). | inference |
| release_samples | The wire tail after a stroke, and the detached finishing note most rolls need, are both release behaviours a glued part would lose. | sourced: FORSYTH-1914 |
| pedal_or_breath_behavior | Not applicable. | inference |
| transition_samples | Not applicable between discrete strokes. | inference |
| mic_or_room_behavior | Distance-appropriate for an orchestral section; an isolated, close-miked snare in an otherwise distant mix is a mismatch. | inference |
| likely_fake_sounding_errors | A closed roll played as one unbroken buzz with no hand-alternation structure; a roll with no written finishing stroke, ending abruptly; snares audibly present when the part calls for them disengaged. | sourced: FORSYTH-1914 |
| organic_programming_methods | Build rolls as pressed, hand-alternating strokes, not a single sustained buzz sample; give accents a small timing lengthening as well as extra velocity; use named rudiment stickings for repeated-note passages. | sourced: FORSYTH-1914; PAS-RUDIMENTS-1984 + academic: DAHL-2004-ACCENT |

### Bass Drum

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A large, shallow cylindrical shell with a parchment or synthetic head at each end, tightened or loosened by leather tags or braces; no snares. | sourced: FORSYTH-1914 |
| attack_behavior | A heavy, felt-padded stick is standard; a birch-broom-like bundle (the Ruthe) gives a very different, scattered attack, historically used for a distinct written part alongside the ordinary stick within the same passage. | sourced: FORSYTH-1914 |
| sustain_behavior | A struck bass drum sets up slow, irregular vibrations, described as resembling the deepest organ pipes; an unmuffled drum booms and sustains audibly. | sourced: FORSYTH-1914 |
| release_behavior | Rings until damped or until it decays; a partially slack, unmuffled head left idle in a concert hall can be excited into audible sympathetic vibration by other loud instruments in the room, an unwanted effect a player prevents by hanging a cloth over the head when the drum is not in use. | sourced: FORSYTH-1914 |
| dynamic_timbre_change | At very soft dynamics the drum's low, indefinite rumble is close enough to distant artillery or thunder that it has been used to represent exactly that. | sourced: FORSYTH-1914 |
| register_character | The lowest-pitched member of the unpitched percussion group; grouped by Rimsky-Korsakov, with cymbals and gong, as the "deep" register among unpitched instruments (triangle, castanets, and small bells being "high"; tambourine, side drum, cymbals, and bass drum "medium" to "deep"). | sourced: RIMSKY-1913 |
| practical_range | No definite pitch; the instrument has no fixed fundamental to give as a range. Orchestral players and the surrounding ensemble sometimes perceive an illusory definite pitch, explained as coincidental reinforcement between the drum's strongest partials and the orchestra's prevailing bass note, not a real pitch of the drum's own. | sourced: FORSYTH-1914 |
| tessitura | Not applicable. | inference |
| articulation_logic | Ordinary stroke, Ruthe (switch) strokes, and the long roll (played with two soft kettle-drum-type sticks) are named, separate techniques. | sourced: FORSYTH-1914 |
| phrase_limits | A large, heavy instrument: quick rhythmic figures are technically playable but impractical, because each fast successive stroke damps out the ring of the one before it, defeating the instrument's character. | sourced: FORSYTH-1914 |
| transitions | No legato; a roll is the sustained case and, unlike timpani, its crescendo cannot be spread across as many bars as a kettle-drum roll's can. | sourced: FORSYTH-1914 |
| repeated_note_behavior | A quick repeated series is possible but works against the instrument's character, per phrase_limits above. | sourced: FORSYTH-1914 |
| vibrato | None. | inference |
| pitch_instability | Not applicable; no controlled pitch to begin with. | inference |
| resonance | Large, and prone to audible sympathetic response to other loud instruments when left unmuffled and idle (see release_behavior). | sourced: FORSYTH-1914 |
| physical_noise | The felt beater's own contact noise is minor compared with the drum's own low-frequency output; the Ruthe's scattering attack is itself closer to noise than to a defined pitch attack. | inference |
| feasibility | One player, one stroke at a time (occasionally two players on two drums in works calling for it, e.g. multiple bass drums in a battle scene). | inference |
| ensemble_behavior | Conventionally paired with cymbals in march and light-orchestral writing; Forsyth calls the pairing a habit without a clear musical reason, and cautions that overused together they can bury harmony and melody in noise. | sourced: FORSYTH-1914 |
| recording_behavior | Its impact is felt as much as heard in a hall; a very close mic captures beater attack a listener in the room would not perceive as separated from the drum's low body. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short notes trigger the sample; the drum's own long, slow decay is carried by the sample, not by note length. | inference |
| overlap | Not a legato instrument. | inference |
| velocity | Selects among recorded dynamic layers; a soft stroke's near-thunder colour is a different recording from a loud stroke turned down. | inference |
| continuous_dynamics | A roll's shape comes from the roll construction itself; the instrument's very slow natural decay means back-to-back single strokes at speed will audibly damp each other even at a fixed high velocity, which is authentic rather than a bug. | sourced: FORSYTH-1914 |
| expression | Not the primary control for a single stroke. | inference |
| articulation_switching | Ordinary stick, Ruthe, and roll (soft kettle-drum-stick technique) are separate recordings. | sourced: FORSYTH-1914 |
| round_robins | Useful but less exposed than the snare, since the bass drum's character resists fast repeated writing in the first place. | inference |
| release_samples | The long decay tail, and any audible damping, are real release behaviours; a note glued to the next loses them. | inference |
| pedal_or_breath_behavior | Not applicable. | inference |
| transition_samples | Not applicable. | inference |
| mic_or_room_behavior | Orchestral distance is part of the character; the drum's low body is a room phenomenon as much as a source phenomenon. | inference |
| likely_fake_sounding_errors | A fast repeated pattern with no audible damping between strokes, where a real instrument would blur; cymbal-and-bass-drum pairing used so continuously it buries the rest of the texture; an idle bass drum audibly "singing" along with unrelated material because muffling was never modelled. | sourced: FORSYTH-1914 |
| organic_programming_methods | Respect the instrument's slow natural decay in fast passages rather than treating it as an instant, gateable hit; use the Ruthe as a genuinely different sound, not a filtered stick sample; keep the cymbal pairing a deliberate choice, not a reflex. | sourced: FORSYTH-1914 |

### Suspended and Clash Cymbals

Orchestral cymbals appear two ways: a clashed pair (two plates struck edge to edge) and a single
suspended plate struck with a stick or rolled with soft mallets. Both are the same tapered
bronze-alloy disc; differences are named in the rows.

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Two circular brass (bronze-alloy) plates, tapered (not flat) so that, held together, they touch only at the edges; tone varies with size, weight, and alloy. | sourced: FORSYTH-1914 |
| attack_behavior | Four distinct playing methods: (1) clashing the pair edge-to-edge with a sideways brushing motion, the ordinary single-note technique; (2) striking a single suspended plate with a hard stick (usable only at loud dynamics) or a soft stick (usable at any dynamic, with a deep, gong-like quality); (3) a two-plate roll, agitating the plates' edges against each other; (4) a two-stick roll on a single hung plate. | sourced: FORSYTH-1914 |
| sustain_behavior | Rings for a long time; the ring is the note. | inference |
| release_behavior | A choke is a physical grab that stops the ring immediately; without one, the cymbal decays on its own. | sourced: FORSYTH-1914 |
| dynamic_timbre_change | A hard-stick single-plate stroke is usable only in loud, excited passages; the same stroke with a soft stick works at any dynamic and reads as darker and rounder. | sourced: FORSYTH-1914 |
| register_character | Bright and metallic in the clashed pair; darker and more gong-like when a single plate is struck with a soft stick. | sourced: FORSYTH-1914 |
| practical_range | Not pitched to a written note in normal orchestral use, though small, specifically tuned ancient-style cymbals (revived by Berlioz, tuned in pairs to specific pitches such as Bb and F) exist as a distinct historical/special effect. | sourced: FORSYTH-1914 |
| tessitura | Not applicable to the ordinary instrument. | inference |
| articulation_logic | Clash (paired), single-plate hard stick, single-plate soft stick, two-plate roll, two-stick roll, and choke are each separate techniques with separate notation conventions ("with hard stick" / "with soft stick" marked above the part). | sourced: FORSYTH-1914 |
| phrase_limits | A two-stick roll needs both hands (one often just holding the suspended plate by its strap, though a skilled player can roll with sticks on both sides while the plate hangs from a fixed arm to avoid oscillation). | sourced: FORSYTH-1914 |
| transitions | No legato; a roll is the sustained gesture. | inference |
| repeated_note_behavior | Not idiomatic at speed; the ring of one stroke persists into and colours the next. | inference |
| vibrato | None. | inference |
| pitch_instability | Not applicable. | inference |
| resonance | Persistent vibration is the defining behaviour: notes must be written with accurate length because the instrument keeps sounding after the notated attack. | sourced: FORSYTH-1914 |
| physical_noise | The two-stick roll is prone to an "aggravating oscillation" if the hung plate is allowed to swing; mounting it fixed to a solid arm and striking both sides prevents this. | sourced: FORSYTH-1914 |
| feasibility | Two hands for a two-stick roll; one hand plus a stand for a struck suspended plate; two hands (or one player managing both plates) for a clash. | sourced: FORSYTH-1914 |
| ensemble_behavior | Conventionally, though not necessarily musically, paired with the bass drum; used alone, a soft stroke blends well with light strings and winds, while a hard clash asserts itself even in a full tutti fortissimo. | sourced: FORSYTH-1914 |
| recording_behavior | Heard through orchestral distance and hall reverberation by default; a crash captured too close loses the sense of the room the ring is decaying into. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | A struck cymbal rings past its notated length by design; cutting it short with note length misrepresents the instrument unless a choke is wanted. | sourced: FORSYTH-1914 |
| overlap | Not a legato instrument. | inference |
| velocity | Selects among recorded dynamic layers and, ideally, hard-stick versus soft-stick recordings, which are genuinely different sounds, not the same sample at different gain. | sourced: FORSYTH-1914 |
| continuous_dynamics | A roll's crescendo needs the roll's own recorded or modelled shape; a single struck note has no internal dynamic shape to draw. | inference |
| expression | Not the primary control on a single strike. | inference |
| articulation_switching | Clash, hard-stick single-plate, soft-stick single-plate, two-plate roll, two-stick roll, and choke are separate recordings or explicitly modelled states. | sourced: FORSYTH-1914 |
| round_robins | Useful for repeated crashes or rolls within one passage. | inference |
| release_samples | The ring after the strike, and a choke's abrupt stop, are both real release behaviours a glued or note-length-truncated part would lose. | sourced: FORSYTH-1914 |
| pedal_or_breath_behavior | Not applicable, except where a choke is implemented on a continuous controller. | inference |
| transition_samples | Not applicable between discrete strikes. | inference |
| mic_or_room_behavior | Orchestral distance and hall tail are part of the character; an all-close-mic cymbal in an otherwise distant mix reads as pasted in. | inference |
| likely_fake_sounding_errors | Cymbals cut off by short note lengths, `COMMON_ERRORS.md` item 12; a hard-stick attack used at a dynamic where the source names it as inappropriate; a bass-drum-and-cymbal pairing so constant it drowns the rest of the texture. | sourced: FORSYTH-1914 |
| organic_programming_methods | Let cymbals ring their full sample unless a choke is a deliberate, notated event; choose hard- or soft-stick colour by the passage's dynamic and character, not by habit; treat the bass-drum pairing as a decision, not a default. | sourced: FORSYTH-1914 |

### Tam-tam

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A broad circular plate of thick hammered metal, its edge turned over all round so the instrument is shaped like a shallow sieve; Chinese, Japanese, and Burmese instruments are noted as superior in size and tone to European-made ones. | sourced: FORSYTH-1914 |
| attack_behavior | A single heavy blow produces a dull, unpleasant, low-power sound; the instrument's real tone needs a continual, persistent, graduated attack (a sustained rolling stroke building the plate up to full vibration), which is why a proper tam-tam sound cannot be produced as a single instantaneous hit at performance dynamic. | sourced: FORSYTH-1914 |
| sustain_behavior | Once properly excited, the tone is described as strange and imposing and persists at length. | sourced: FORSYTH-1914 |
| release_behavior | Difficult to damp once set in vibration; a large tam-tam does not stop cleanly on command the way a smaller struck instrument does. | sourced: FORSYTH-1914 |
| dynamic_timbre_change | The instrument's usable dynamic in a single stroke is essentially p to mp; louder single strokes do not produce a proportionally better tone, only a louder bad one, so real dynamic range is achieved through the graduated roll/swell technique rather than through single-stroke force. | sourced: FORSYTH-1914 |
| register_character | Grouped among the "deep" unpitched percussion, alongside bass drum and cymbals. | sourced: RIMSKY-1913 |
| practical_range | No definite pitch. | sourced: FORSYTH-1914 |
| tessitura | Not applicable. | inference |
| articulation_logic | A single soft-mallet stroke (rare, and effectively usable only once in a work because of its dramatic weight) and a graduated crescendo roll (pp to ff) are the two named techniques; a single heavy blow is explicitly not a correct technique. | sourced: FORSYTH-1914 |
| phrase_limits | Because a single strong stroke cannot be repeated for effect within one work without losing impact, and because damping is difficult, tam-tam events are sparse, structural moments rather than a repeating pattern. | sourced: FORSYTH-1914 |
| transitions | No legato; the roll/swell is the sustained gesture and its own distinct technique. | inference |
| repeated_note_behavior | Not idiomatic; the instrument's character resists repetition (see phrase_limits). | sourced: FORSYTH-1914 |
| vibrato | None. | inference |
| pitch_instability | Not applicable. | inference |
| resonance | Large surface area, long persistence, and (per Forsyth) a genuinely strange, imposing tone quality when properly excited. | sourced: FORSYTH-1914 |
| physical_noise | A soft bass-drum-type stick is the usual beater; harder implements were not documented as standard in this source. | sourced: FORSYTH-1914 |
| feasibility | One player, one beater; a graduated roll needs sustained, continuous motion over a real span of time, which is a feasibility fact (it cannot be instantaneous) as much as a stylistic one. | sourced: FORSYTH-1914 |
| ensemble_behavior | Used in the theatre continuously since the nineteenth century for solemn, mysterious, or terrifying effect; its dramatic weight is part of why it is used sparingly. | sourced: FORSYTH-1914 |
| recording_behavior | A room's full reverberant tail is arguably more of this instrument's character than for any other in the section, given how long and how strangely it rings. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | A single hit sample does not capture the instrument correctly if the real technique for a full-dynamic event is a graduated build, not an instantaneous strike; a swell needs to be modelled as a swell. | sourced: FORSYTH-1914 |
| overlap | Not applicable in the melodic sense. | inference |
| velocity | A single soft-dynamic stroke and a full graduated swell are different events, not the same sample at different velocities; a "hard hit" sample used alone misrepresents how the instrument actually reaches full volume. | sourced: FORSYTH-1914 |
| continuous_dynamics | The swell is the instrument's primary expressive device and needs a real drawn dynamic shape over real time, the clearest orchestral-percussion case of `COMMON_ERRORS.md` item 10 (a swell is not a volume fade on a static sample; here it may need a genuinely different, longer-evolving recorded or modelled event). | sourced: FORSYTH-1914 |
| expression | Where available, a shaping control on top of the swell's own recorded dynamic evolution. | inference |
| articulation_switching | Single soft stroke and graduated roll/swell are separate recordings or a modelled continuum, not the same event at different lengths. | sourced: FORSYTH-1914 |
| round_robins | Low priority; the instrument is used sparingly by its own nature. | sourced: FORSYTH-1914 |
| release_samples | The long, hard-to-damp tail is a defining release behaviour; a gated or truncated tam-tam is audibly wrong. | sourced: FORSYTH-1914 |
| pedal_or_breath_behavior | Not applicable. | inference |
| transition_samples | Not applicable. | inference |
| mic_or_room_behavior | Room reverberation is close to inseparable from this instrument's character. | inference |
| likely_fake_sounding_errors | A tam-tam swell built as a static hit with a volume automation fade rather than a real graduated-attack recording or model; a tam-tam used repeatedly in a way that dulls its dramatic weight; a tail cut short by a gate. | sourced: FORSYTH-1914 |
| organic_programming_methods | Model the full-dynamic event as a genuine swell with its own time-evolving attack, not a fader move on a struck sample; use the instrument sparingly, matching its documented dramatic function; let the tail ring long and reverberant. | sourced: FORSYTH-1914 |

### Triangle

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A small steel bar bent into a triangle, open at one corner, struck with a beater of the same metal. | sourced: FORSYTH-1914 |
| attack_behavior | A moderate size is wanted: too small sounds "tinkly," too large acquires an unwanted distinct musical note; the tone should be clear rather than pitched. | sourced: FORSYTH-1914 |
| sustain_behavior | Rings after a single stroke; a roll (rapid beating to and fro between two sides) sustains a shimmering texture. | sourced: FORSYTH-1914 |
| release_behavior | Decays on its own; not normally damped by hand in orchestral use. | inference |
| dynamic_timbre_change | Effective across an unusually wide dynamic range for such a small instrument: it asserts itself even in a full tutti fortissimo, and is equally charming played ppp against soft strings and winds. | sourced: FORSYTH-1914 |
| register_character | Grouped among the "high" unpitched percussion. | sourced: RIMSKY-1913 |
| practical_range | No definite pitch by design (a well-made instrument avoids acquiring one). | sourced: FORSYTH-1914 |
| tessitura | Not applicable. | inference |
| articulation_logic | Single strokes, small grouped figures, and the roll (tremolo) are the vocabulary; grouped strokes are conventionally written in odd numbers so the same-direction (right-to-left) motion starts and ends the group. | sourced: FORSYTH-1914 |
| phrase_limits | Best used sparingly: the most effective orchestral triangle parts on record are extremely short, sometimes a single note. | sourced: FORSYTH-1914 |
| transitions | No legato; the roll is the sustained gesture. | inference |
| repeated_note_behavior | An even number of grouped strokes forces the player to reverse beating direction to land an accent correctly; an odd number avoids this. | sourced: FORSYTH-1914 |
| vibrato | None. | inference |
| pitch_instability | Not applicable. | inference |
| resonance | Rings clearly after a stroke; the instrument's whole identity is its ring. | inference |
| physical_noise | The beater striking a specific point on the bar is the whole sound; no separate mechanism noise. | inference |
| feasibility | One hand holds the instrument (often by a cord), the other strikes it; a roll needs the striking hand free to move rapidly between two sides. | inference |
| ensemble_behavior | Effective at converting a climactic tutti crescendo into a still brighter texture; equally effective as a single bright event that "sets free" a new phrase at a change of harmony or colour, used once, not repeated at every similar structural moment. | sourced: FORSYTH-1914 |
| recording_behavior | High-frequency content translates well at orchestral distance; it is not an instrument that benefits from close-miking in a section recording. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short notes trigger the strike sample; the ring is carried by the sample's own decay. | inference |
| overlap | Not applicable. | inference |
| velocity | Selects among dynamic layers across an unusually wide usable range for the instrument's size. | sourced: FORSYTH-1914 |
| continuous_dynamics | A roll's dynamic shape needs a drawn curve on whatever the roll articulation reads. | inference |
| expression | Not the primary control for a single stroke. | inference |
| articulation_switching | Single stroke and roll are separate recordings. | inference |
| round_robins | Useful for grouped-stroke figures; low priority for the sparse single events the instrument favours. | inference |
| release_samples | The ring after the stroke is essential to the character and should not be truncated. | inference |
| pedal_or_breath_behavior | Not applicable. | inference |
| transition_samples | Not applicable. | inference |
| mic_or_room_behavior | Orchestral distance is appropriate; the instrument is not meant to read as close and forward. | inference |
| likely_fake_sounding_errors | A grouped-stroke figure written with an even count and no direction change accounted for; a triangle used at every similar structural moment rather than sparingly, undercutting the "sets a new phrase free" effect the source names; a truncated ring. | sourced: FORSYTH-1914 |
| organic_programming_methods | Use odd-numbered groupings where the pattern calls for an accent at the end; reserve the instrument for genuinely climactic or phrase-opening moments rather than habitual use. | sourced: FORSYTH-1914 |

### Tambourine

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A small wooden hoop with a parchment head on one side, tunable by rods and nuts, and pairs of small metal jingles set into cutouts around the hoop. | sourced: FORSYTH-1914 |
| attack_behavior | Three recognised playing methods, each a genuinely different sound, not a dynamic variant of one: (1) striking the head with the knuckles, giving detached notes; (2) shaking the hoop, giving a roll made of the jingles alone; (3) rubbing the thumb across the head, giving a partial tremolo dominated by the jingles. A rarer fourth method rests the tambourine on a tuned kettle-drum and strikes it with kettle-drum sticks, giving a muffled-drum tone edged with faint jingles. | sourced: FORSYTH-1914 |
| sustain_behavior | The shaken roll and the thumb-rubbed tremolo are the instrument's two sustained techniques; a knuckle strike is a discrete, decaying event. | sourced: FORSYTH-1914 |
| release_behavior | Jingles continue to sound briefly after the head is struck or the shake stops. | inference |
| dynamic_timbre_change | An unexpected sudden fortissimo roll is a specific, named effect, most striking when the orchestra is in its upper register; its charm fades with repetition, and its natural home is the theatre more than the concert hall. | sourced: FORSYTH-1914 |
| register_character | Grouped among the "medium" unpitched percussion. | sourced: RIMSKY-1913 |
| practical_range | No definite pitch. | sourced: FORSYTH-1914 |
| tessitura | Not applicable. | inference |
| articulation_logic | Knuckle strike, hoop shake, thumb rub, and (rarely) drum-mounted kettle-stick playing are each distinct; batutto colla mano (struck with the flat of the hand) is a further named variant seen in scores. | sourced: FORSYTH-1914 |
| phrase_limits | The pp dynamic is less generally useful and works best tied directly to the music's rhythmic pattern; used loosely, quiet tambourine notes risk sounding like a copyist's error rather than a musical gesture. | sourced: FORSYTH-1914 |
| transitions | No legato; roll and tremolo are the two sustained states, discrete strikes the articulated one. | inference |
| repeated_note_behavior | Rhythmic dance-style patterns (of the kind documented in French orchestral repertoire) repeat a short figure steadily rather than varying it. | sourced: FORSYTH-1914 |
| vibrato | None, beyond the jingles' own natural buzz. | inference |
| pitch_instability | Not applicable. | inference |
| resonance | The jingles are a secondary, always-present resonant layer riding on top of whichever primary technique is used. | inference |
| physical_noise | The jingles are, functionally, a controlled noise component; they are the instrument's identity, not an unwanted artifact. | inference |
| feasibility | One or two hands depending on technique (shaking needs one or both hands on the hoop; the drum-mounted method needs both hands holding sticks). | inference |
| ensemble_behavior | Historically associated with dance rhythms and with the bass drum, pizzicato low strings, and a sustained horn note in at least one documented orchestral example; overused, its tone becomes tiresome. | sourced: FORSYTH-1914 |
| recording_behavior | The jingles carry significant high-frequency content that reads clearly even at orchestral distance. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short notes trigger a strike sample; roll and tremolo are separate, sustained articulations. | inference |
| overlap | Not applicable. | inference |
| velocity | Selects among dynamic layers within one technique; it does not select between the three techniques, which are separate patches or keyswitches by nature. | sourced: FORSYTH-1914 |
| continuous_dynamics | A shaken roll's or thumb tremolo's dynamic shape needs a drawn curve, not a static velocity. | inference |
| expression | Not the primary control for a discrete knuckle strike. | inference |
| articulation_switching | Knuckle strike, shake/roll, and thumb tremolo are separate recordings; they are not velocity layers of one recording. | sourced: FORSYTH-1914 |
| round_robins | Important for repeated knuckle-strike dance patterns. | inference |
| release_samples | The jingles' decay after a strike or after a shake stops is a real release behaviour. | inference |
| pedal_or_breath_behavior | Not applicable. | inference |
| transition_samples | Not applicable. | inference |
| mic_or_room_behavior | High-frequency jingle content survives orchestral distance well; a close-only capture can overstate it relative to a real hall balance. | inference |
| likely_fake_sounding_errors | A shaken roll faked by rapid identical knuckle strikes rather than the instrument's actual jingle-dominated shake sound; quiet tambourine notes scattered with no rhythmic relationship to the surrounding music; the sudden ff roll effect used so often it loses its impact. | sourced: FORSYTH-1914 |
| organic_programming_methods | Treat the three (or four) playing methods as genuinely separate instruments within one part, chosen for their sound rather than convenience; tie quiet notes to the rhythmic pattern rather than scattering them; keep the surprise fortissimo roll rare. | sourced: FORSYTH-1914 |

### Woodblock and Temple Blocks

Two related struck wooden idiophones. The (single) woodblock is a hollowed hardwood block struck for
a sharp, cutting, unpitched crack. Temple blocks are usually a tuned set of several hollow wooden
blocks (traditionally carved, "dragon mouth" instruments), giving a darker, more hollow timbre than
a plain woodblock and a small, relative-pitch melodic vocabulary.

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Woodblock: a single piece of hollowed hardwood (maple, mahogany, or oak), with a drilled-out section through roughly the top third for resonance. Temple blocks: a set of hollow wooden "dragon mouth" blocks, also made in plastic or marine plywood by some manufacturers. | sourced: BYU-WOOD-BLOCKS; BYU-TEMPLE-BLOCKS |
| attack_behavior | A sharp, percussive strike; temple blocks are played with soft rubber mallets at the block's edge or mouth and have less cutting power than a traditional woodblock. | sourced: BYU-TEMPLE-BLOCKS |
| sustain_behavior | Very short; a hard, dry, immediate decay typical of a struck wooden idiophone. | inference |
| release_behavior | Decays on its own almost immediately; not normally damped further by hand. | inference |
| dynamic_timbre_change | Harder strikes bring more crack and less body; woodblocks are chosen specifically for cutting through texture, which favours a harder, more percussive stroke than temple blocks typically use. | inference |
| register_character | A woodblock reads as a single, unpitched crack; a temple-block set reads as a small family of relative pitches (commonly a set of five tuned to a pentatonic pattern, though sets are also built to whole-tone, diatonic, or chromatic patterns), used melodically or coloristically rather than to a fixed absolute pitch. | sourced: BYU-TEMPLE-BLOCKS |
| practical_range | No standard absolute pitch for either instrument; a temple-block set's relative tuning is a per-set fact, not a fixed orchestral range. | inference |
| tessitura | Not applicable. | inference |
| articulation_logic | Single strikes are the primary vocabulary for both; rolls (rapid alternation) are possible on either but are less idiomatic than on a resonant metal or skin instrument, given the very fast decay. | inference |
| phrase_limits | Bound by two hands and, for a temple-block set, by travel time between blocks, the same physical constraint as moving between kit toms. | inference |
| transitions | No legato; every note is a discrete strike. | inference |
| repeated_note_behavior | Real repeated strokes alternate hands or mallets by default, with the same rudiment vocabulary applicable as on any struck instrument. | inference |
| vibrato | None. | inference |
| pitch_instability | Not applicable. | inference |
| resonance | Minimal; the whole character is the attack, not a ringing body. | inference |
| physical_noise | Mallet or stick contact noise is close to the entire sound; there is little decay to separate it from. | inference |
| feasibility | Two hands (or two mallets); more simultaneous notes than the player has mallets for, or a leap between distant blocks faster than a hand can travel, is not playable. | inference |
| ensemble_behavior | A colour and punctuation voice; not a sustaining or blending instrument in an ensemble texture. | inference |
| recording_behavior | A close, dry capture suits the instrument's character better than a distant, reverberant one, unlike most of the rest of this page. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short notes trigger the sample; the natural decay is already very short, so note length rarely matters beyond triggering. | inference |
| overlap | Not applicable. | inference |
| velocity | Selects among dynamic layers; a genuinely soft strike is a different recording from a hard strike turned down. | inference |
| continuous_dynamics | Not applicable to single strikes. | inference |
| expression | Not applicable. | inference |
| articulation_switching | Where a temple-block set offers alternate mallet types, that is a separate sample set. | inference |
| round_robins | Essential; a repeated woodblock or temple-block pattern is one of the more exposed cases for the machine-gun error, given how dry and identical an unvaried sample sounds. | inference |
| release_samples | Minimal; the instrument's natural decay is already close to its release. | inference |
| pedal_or_breath_behavior | Not applicable. | inference |
| transition_samples | Not applicable. | inference |
| mic_or_room_behavior | A closer, drier capture than most of the rest of the section suits the instrument. | inference |
| likely_fake_sounding_errors | Identical repeated strikes with no round robin, especially audible given how little natural variation the instrument's short decay leaves to hide it; a temple-block melodic figure played with no hand-to-hand variation in force. | inference |
| organic_programming_methods | Vary strike velocity and, where available, mallet contact point per note; respect travel time between blocks in a temple-block set; alternate hands on repeated figures. | inference |

### Castanets (Orchestral)

Orchestral castanets, unlike the hand-clicked pairs of flamenco and Spanish folk practice, are
normally mounted, a pair at each end of a handle, for practical reasons of ensemble playing; this
page covers that orchestral form. Hand castanets as a living Spanish practice are outside this page's
scope.

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A pair of hollow hardwood shells (traditionally chestnut), clicked together; the traditional hand form uses a larger pair (macho, "male") in the left hand for a simplified rhythm and a smaller pair (hembra, "female") in the right hand for the full dance rhythm. Orchestral use mounts a pair at each end of a handle instead. | sourced: FORSYTH-1914 |
| attack_behavior | A sharp, dry click; the mounted orchestral version is a concession to ensemble practicality and, by Forsyth's account, a somewhat blunter substitute for the hand-held technique. | sourced: FORSYTH-1914 |
| sustain_behavior | None; each click is a discrete, immediately decaying event. | inference |
| release_behavior | No sustain to release; the click is the entire event. | inference |
| dynamic_timbre_change | Harder clicks are simply louder and sharper; there is little separate timbral shift with dynamic. | inference |
| register_character | Grouped among the "high" unpitched percussion. | sourced: RIMSKY-1913 |
| practical_range | No definite pitch, though some scores (Saint-Saëns, *Samson et Dalila*) call for both wood and iron castanets as distinct timbres. | sourced: FORSYTH-1914 |
| tessitura | Not applicable. | inference |
| articulation_logic | The characteristic figure is a simple triple-time quaver rhythm with the central quaver subdivided into semiquavers, a semiquaver triplet, or demisemiquavers; several such named variants exist in the traditional (Spanish dance) vocabulary. | sourced: FORSYTH-1914 |
| phrase_limits | In dance practice the rhythm typically runs continuously through a whole dance; in song it is used as a periodic interpolation (commonly alternating four bars of song with four bars of castanets). | sourced: FORSYTH-1914 |
| transitions | No legato; every click is discrete. | inference |
| repeated_note_behavior | The macho/hembra division lets the two hands carry different rhythmic roles simultaneously in hand-held practice; the mounted orchestral version collapses this into one player's single implement. | sourced: FORSYTH-1914 |
| vibrato | None. | inference |
| pitch_instability | Not applicable. | inference |
| resonance | Minimal; a dry, hollow-wood click with almost no ring. | inference |
| physical_noise | The click itself is the entire sound. | inference |
| feasibility | Traditional practice uses two hands, one pair of castanets each; the mounted orchestral form is typically played by one hand shaking or striking a single handle. | sourced: FORSYTH-1914 |
| ensemble_behavior | A colour instrument tied to Spanish dance idiom; used outside that idiom it reads as an explicit topical reference rather than a neutral texture. | inference |
| recording_behavior | A close, dry capture suits the instrument; it carries little that benefits from distant hall capture. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short notes trigger the sample; there is no decay to extend. | inference |
| overlap | Not applicable. | inference |
| velocity | Selects among dynamic layers; the timbral change with dynamic is small compared with most other instruments on this page. | inference |
| continuous_dynamics | Not applicable to a single click. | inference |
| expression | Not applicable. | inference |
| articulation_switching | Wood and iron castanets (where a score calls for both) are separate sample sets, not a filtered variant of one recording. | sourced: FORSYTH-1914 |
| round_robins | Essential; the characteristic rhythm repeats a short figure rapidly and identically clicked samples are highly exposed. | inference |
| release_samples | Not applicable; there is no meaningful release phase to lose. | inference |
| pedal_or_breath_behavior | Not applicable. | inference |
| transition_samples | Not applicable. | inference |
| mic_or_room_behavior | Close, dry capture is appropriate. | inference |
| likely_fake_sounding_errors | Identical repeated clicks with no round robin, especially exposed given the instrument's fast, repetitive idiom; the traditional macho/hembra two-hand rhythmic independence collapsed into one flat pattern where the brief wants the fuller hand-held texture. | sourced: FORSYTH-1914 |
| organic_programming_methods | Vary click velocity slightly across the repeated figure; where the brief wants the traditional hand-held texture rather than the orchestral mounted form, model two independent rhythmic layers (macho and hembra), not one. | sourced: FORSYTH-1914 |

---

## What the instrument is

A family united only by being struck, scraped, or shaken, so this page is a set of behaviours rather
than one model. Two generalisations hold across nearly all of it: **the striking implement is half
the sound** (mallet hardness, stick versus Ruthe, hard versus soft cymbal stick are all separate
sample sets, not EQ variants), and **what happens after the strike is the other half**, because most
of this family rings, sometimes for a long time, and the ring is frequently the note rather than a
decay to be tolerated. [inference]

## Range and register

Almost nothing here is pitched in the melodic sense; timpani are the clear exception, and their
range is a set of pedal-adjustable drums rather than a fixed compass. Rimsky-Korsakov's rough
register grouping of the unpitched instruments (triangle, castanets, and small bells as "high";
tambourine, side drum, cymbals, and bass drum "medium" to "deep"; gong among the deepest) is a useful
first approximation for balancing an unpitched-percussion texture against pitched instruments in a
corresponding register, though it is a nineteenth-century rule of thumb, not a measured fact.
[sourced: RIMSKY-1913]

## Articulation and note transitions

Almost every instrument on this page has **more than one genuinely distinct playing technique**,
each its own recorded sound rather than a dynamic layer of the others: a tambourine's knuckle strike,
shake, and thumb rub; a cymbal's clash, hard-stick, soft-stick, and two roll methods; a tam-tam's
single stroke versus its graduated swell; a bass drum's ordinary stick versus the Ruthe. Programming
that collapses these into one sample with a dynamic layer, rather than separate articulations chosen
by the passage, is a recurring and specific way this family sounds fake, distinct from the general
velocity-layer question that applies more cleanly to a single-technique instrument like the triangle.
[sourced: FORSYTH-1914]

The orchestral snare's closed roll deserves its own note because a prior version of this page said it
was "pressed rather than alternated". **Every roll alternates hands.** The rudiments name two distinct
rolls: the double-stroke open roll, two strokes per hand (LL-RR), and the multiple-bounce roll, each
stroke pressed into several bounces [sourced: PAS-RUDIMENTS-1984]. Forsyth, writing in 1914, describes
the double-stroke "daddy-mammy" as the foundation of the roll, with the second stroke of each pair
becoming a controlled rebound [sourced: FORSYTH-1914]. The smooth closed roll of current orchestral
writing is usually the multiple-bounce kind, still hand to hand [inference]. Neither is one hand
holding a buzz.

Roll rates in strokes per second, by instrument and dynamic, are human properties this page does not
give a number for: no source read for 2.1 gave one with enough context. They are a fact about players,
not about a patch, so a calibration render cannot supply them either; until a source is read, set
the rate per style in the performance plan and label it as set, not measured
[to-verify: a pedagogy or measurement source for roll rates by dynamic and instrument].

## Physical constraints

Two hands (occasionally two hands plus a foot-worked damper on some setups, and one hand plus a
pedal for timpani). **Damping takes a hand**, so an instruction to stop a ring competes directly with
an instruction to keep playing; a part that asks for both from the same player at the same instant is
not playable. [inference]

**Timpani pedal changes take real time and are audible if made while the head still rings.** A part
that retunes a drum silently between two adjacent, unrested bars is not playable; a part that retunes
during a written rest of sufficient length is. [sourced: FORSYTH-1914]

## Phrase behaviour

Ring is the default and silence is the effort: a part that wants a short, stopped note has to say who
is damping it and when. [inference]

Several instruments here (tam-tam above all, triangle close behind it) are documented as most
effective used sparingly, tied to a specific structural or dramatic moment rather than repeated at
every similar point in a score; overuse is named explicitly in the sources as a way these instruments
lose their effect. [sourced: FORSYTH-1914]

## Ensemble behaviour

Orchestral percussion is usually a colour and accent layer rather than a continuous pulse, which
makes the marker-part question less pressing here than for the drum kit's hi-hat (see `DRUM_KIT.md`
for that correction). Where a percussion part is genuinely the pulse (a march's side drum, for
instance), name it in `marker_parts_excluded` rather than assuming the whole section behaves the same
way. [inference]

## Recording behaviour

Orchestral percussion is recorded at the back of the hall by design, distant and reverberant, and
close-miking most of it produces an instrument that is not in the same room as the rest of the
orchestra. Woodblock, temple blocks, and castanets are a partial exception: their character is
short and dry enough that a closer, drier capture suits them better than the section's usual distant
placement. [inference]

## Programming it: the control model

Product specifics belong in the calibration profile.

```text
velocity: selects the technique's dynamic layer first, level second
articulations: each named technique (clash vs. single-plate, knuckle vs. shake vs. thumb,
  ordinary stick vs. Ruthe, single stroke vs. graduated swell) is a separate recording
timpani_tuning: a pedal state with a real transition time; check pedal changes as feasibility
tam_tam_swell: a time-evolving event, not a static sample with a volume fade
damping: an explicit event; ring is the default
choke: note-off or aftertouch depending on the product; the physical grab is the guide-level fact
round_robins: essential; this family is the most exposed for repeated identical samples
```

[inference]

## Programming it: what makes it sound real

- Choose the technique first (clash vs. suspended stroke, knuckle vs. shake, stick vs. Ruthe), then
  write the part; these are separate instruments in practice, not one instrument at different
  velocities. [inference]
- Build the orchestral snare's closed roll as a pressed, hand-alternating stroke. [sourced: FORSYTH-1914]
- Give timpani pedal changes the time they need, and let a glissando bend pitch audibly rather than
  cutting between two static pitches. [sourced: FORSYTH-1914]
- Model a tam-tam swell as a genuine, time-evolving event, not a fader move on a static hit. [sourced: FORSYTH-1914]
- Let things ring, and write the damping where it is wanted. [inference]
- Use instruments documented as sparing effects (tam-tam, triangle) sparingly, not habitually.
  [sourced: FORSYTH-1914]

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Family-specific tells:

- one sample repeated identically, error 1, most exposed on tambourine, castanets, and woodblock;
  [inference]
- distinct playing techniques collapsed into one sample's velocity layers; [sourced: FORSYTH-1914]
- cymbal and gong notes truncated instead of damped or allowed to ring, error 12; [inference]
- a tam-tam swell built as a volume fade on a static sample rather than a real graduated event, a
  clear case of error 10; [sourced: FORSYTH-1914]
- timpani retuning instantly with no pedal transition; [sourced: FORSYTH-1914]
- an orchestral snare's closed roll played as one continuous unbroken buzz with no hand-alternation;
  [sourced: FORSYTH-1914]
- a sparing-use instrument (triangle, tam-tam) used at every structurally similar moment. [sourced: FORSYTH-1914]

## What the Performance Director needs from this file

- `limb_or_finger_conflicts`: two hands per player, and damping takes one of them.
- `out_of_range`: timpani pitch per drum, and the pedal transition time between settings.
- `articulation_unavailable`: each named technique per instrument (clash vs. suspended, knuckle vs.
  shake vs. thumb, stick vs. Ruthe, single stroke vs. swell) is a separate recording; a request for
  one the instrument lacks is reported, not silently substituted.
- `simultaneity_exceeded`: two hands (or two mallets) per player, one player per instrument unless
  the part says otherwise.
- Marker part declaration where a percussion part genuinely carries the pulse.

## Sources and what to verify

- [inference] claims above rest mainly on Cecil Forsyth's 1914 *Orchestration* (read at section depth
  across the timpani, side drum, bass drum, cymbal, gong, triangle, tambourine, and castanets
  chapters) and Rimsky-Korsakov's *Principles of Orchestration* (timpani range and register grouping,
  read at section depth); full citations in `research/sources/INSTRUMENT_SOURCES.md`.
- **To verify**: roll rates in strokes per second, by instrument and dynamic; these are human
  properties, deferred to calibration rather than invented here, per the brief.
- **To verify**: modern timpani retuning times with and without a tuning gauge; a practitioner source
  giving concrete figures was searched for but not opened at section depth this pass, and no number
  is printed in this file as a result.
- **To verify**: cymbal, drumhead, and gong decay spectra, and the acoustic basis for why some struck
  metal instruments (tam-tam, gong) resist a single-blow attack while others (triangle, cymbal clash)
  do not, in Fletcher and Rossing, *The Physics of Musical Instruments*. Not opened this pass.
- **Not available**: measured stroke-force or roll-rate figures for any instrument on this page. Where
  the old page gave a number without a source, this page removes it rather than repeating it.
