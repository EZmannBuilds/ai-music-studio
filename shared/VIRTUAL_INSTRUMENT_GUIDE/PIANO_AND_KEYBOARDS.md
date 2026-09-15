# Piano and Keyboards

Grand and upright acoustic piano (as one card, with upright differences stated in the affected rows);
harpsichord; celesta; accordion and harmonium/reed organ (one card, differences stated in-row); tine
electric piano and reed electric piano (two cards, since their sound-production physics differ even
though both are struck, damped, keyboard instruments); and clavinet. The hand-pumped Indian harmonium
tradition is out of scope here; it is a distinct tradition with its own technique and belongs under
`CULTURALLY_SPECIFIC_INSTRUMENTS.md` if written up with tradition-specific sources.

> Evidence: fourteen sources read at section or excerpt depth: a piano-technician action walkthrough,
> one academic acoustics paper (read via a university lecture summary), one perception study on
> harpsichord touch, orchestration and performer pedagogy for celesta and accordion, a hand-span
> advocacy page citing measured data, mechanism sources for the reed organ and clavinet, one official
> manufacturer manual (the Rhodes service manual), and one peer-reviewed conference paper covering both
> electric pianos together. Fletcher and Rossing (hammer-felt physics) and Adler (register-writing
> convention) were named as targets and not opened; claims resting on them stay `to-verify`. Source IDs
> resolve in `research/sources/INSTRUMENT_SOURCES.md`; the claims and their limits are recorded in
> `research/instruments/PIANO_AND_KEYBOARDS.md`.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## Behaviour cards

### Grand and Upright Piano

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Felt-covered hammers thrown at steel (wound copper-steel in the bass) strings by a mechanical action; two or three strings per note above the low bass, dynamically coupled through a shared bridge; the player has no contact with the string after the hammer leaves the action | sourced: SMIT-PIANOACTION + academic: WEINREICH-1977 |
| attack_behavior | Decided entirely at the moment of the hammer strike: harder strikes drive the hammer into the string with greater force and a shorter, stiffer contact time, producing a louder **and** brighter attack. Grand and upright actions both work this way; they differ in how quickly the action resets (see repeated_note_behavior) | to-verify: hammer felt as a nonlinear spring and the exact velocity-to-spectrum relationship, in Fletcher and Rossing, not opened for this work |
| sustain_behavior | Strings decay from the moment of the strike; multi-string unisons produce a two-stage decay, a fast symmetric-mode decay followed by a slower "aftersound" from the antisymmetric mode, whose forces largely cancel at the bridge. Deliberate mistuning of the unison strings and the una corda pedal both act on this coupling | academic: WEINREICH-1977 |
| release_behavior | A felt damper drops onto the string(s) when the key is released and the sustain pedal is up, stopping the sound within a fraction of a second; with the sustain pedal down, dampers are lifted and strings ring and resonate sympathetically until they decay naturally | sourced: SMIT-PIANOACTION |
| dynamic_timbre_change | Louder is brighter, not only bigger, because of the hammer-felt attack mechanism; the soft (una corda) pedal shifts the hammer to strike fewer strings or a different part of the felt, changing colour as much as loudness | to-verify: exact spectral mechanism, in Fletcher and Rossing, not opened + sourced: SMIT-PIANOACTION |
| register_character | The bottom octave is inharmonic and thick, muddying quickly under pedal; the top octave has almost no sustain and functions mainly as attack and sparkle; the singing register sits roughly two octaves below middle C to two octaves above it, where close voicings work best | inference |
| practical_range | A full modern instrument covers A0 to C8, written and sounding the same (non-transposing) | inference |
| tessitura | Most controllable and resonant roughly two octaves either side of middle C; below that, close chord voicings turn to mud and the usual remedy is to open the spacing as the register descends | inference |
| articulation_logic | No true legato exists: one note decays while the next begins, and the illusion of connection is made by overlapping fingers and the sustain pedal. Articulation is therefore a matter of note length, attack strength and pedal use, not of separate mechanical techniques the way a bowed or blown instrument has them | inference |
| phrase_limits | Bounded by the hand and by the pedal, not by breath. Every note begins decaying immediately, so a sustained line is built from re-strikes, rhythmic figuration, or pedal holding the harmony while the hand moves | inference |
| transitions | No sustained legato transition exists between two struck notes; the closest equivalent is finger overlap plus pedal, which blends decay tails rather than producing a bowed- or blown-instrument-style glide | inference |
| repeated_note_behavior | On a grand action, double escapement resets the jack under the hammer as the key rises only partway, allowing repetition before the key fully returns; a well-regulated grand action can repeat a note up to roughly eight times per second. Upright actions use single escapement without a repetition lever and reset only on a fuller key return, so they cannot repeat as fast; a repetition faster than the action allows produces a weak or missing note, one of the few places a written keyboard part can be physically impossible | sourced: SMIT-PIANOACTION |
| vibrato | None; pitch is fixed once the string is struck and there is no mechanism to modulate it during the note | inference |
| pitch_instability | Strings are stretch-tuned: because a real string's stiffness sharpens its upper partials relative to an ideal harmonic series, tuning pure 2:1 octaves against that inharmonicity would sound dissonant, so octaves are tuned bass-flat, treble-sharp of 12-tone equal temperament to match perceived consonance to the strings' actual partials (the Railsback stretch) | standard-reference: RAILSBACK-STRETCH-2015 |
| resonance | Undamped strings (sustain pedal down) resonate sympathetically with whatever is played, including strings not struck; the soundboard and case add their own resonant colour; the una corda pedal changes which part of the coupled-string system is engaged | sourced: SMIT-PIANOACTION + academic: WEINREICH-1977 |
| physical_noise | Audible hammer thump, damper contact and pedal mechanism noise are part of the instrument's normal close-mic'd sound | inference |
| feasibility | Two hands, ten fingers, two or three pedals (see below); a hand spans roughly a ninth to a tenth comfortably depending on the player, not "a ninth comfortably" as a safe default: about 8.5 inches (21.6 cm) is the threshold below which a tenth is not comfortable, adult male spans average about an inch more than adult female spans, and by cited figures a majority of women cannot comfortably play a tenth on a standard keyboard. A chord wider than the player's hand is not impossible, it is rolled, a different, deliberate sound. One finger per key; the thumb can occupy two adjacent keys in some voicings, which is why a strict "more than five notes in one hand is impossible" rule is too strict | sourced: PASK-HANDSPAN + inference |
| ensemble_behavior | The piano covers its own bass, harmony and melody, so in an ensemble it is usually either the whole accompaniment or a deliberately restricted layer; doubling a bass part in the left hand at the same octave as a bass instrument thickens the low end quickly | inference |
| recording_behavior | Recorded close, the instrument is percussive and detailed with audible hammer and damper noise; recorded further back it becomes rounder as the room takes over. Lid position and microphone distance and perspective are part of the instrument's sound, not an effect added afterward | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Not a rectangular block; a real note-off lets the damper and release be heard, and gluing notes end to end removes that | inference |
| overlap | No monophonic legato transition exists on piano; overlap is a performance illusion (finger and pedal), not a sample-triggering requirement the way it is on a bowed or sampled-legato instrument | inference |
| velocity | Selects level and timbre together on a well-built patch, mirroring the acoustic hammer-felt mechanism; a patch that only scales level with velocity is discarding the instrument's central behaviour | sourced: SMIT-PIANOACTION + inference |
| continuous_dynamics | Not applicable in the way a bowed or blown instrument uses a continuous crossfade on a held note, because a piano note has no sustained excitation to crossfade; dynamic shape across a passage is made note by note through velocity and voicing, not by a within-note continuous controller | inference |
| expression | A patch-level trim, not a substitute for per-note velocity or voicing decisions | inference |
| articulation_switching | Not needed for the core instrument; pedal state (sustain, sostenuto, soft) is the closest equivalent to an articulation switch and should be automated as its own continuous or stepped control, not folded into velocity | inference |
| round_robins | Needed for any repeated pitch, since no two real strikes are identical even at matched intent | inference |
| release_samples | Damper and mechanism noise on note-off; lost if notes are glued end to end | inference |
| pedal_or_breath_behavior | Sustain pedal is not a switch: half-pedalling (partial damper contact) and flutter/surface pedalling (very quick, shallow movements to control accumulating blur) are real, continuous techniques, and pedal changes are timed to harmony changes, not bar lines. A sostenuto pedal (holds only the dampers already lifted at the moment it is pressed) exists on many grands; its mechanism is `unresolved` here | sourced: SPANSWICK-PEDAL + to-verify: not covered by any source read in this pass |
| transition_samples | Not applicable: there is no recorded legato transition analogous to a bowed instrument's, since the piano has no sustained excitation to glide between notes on | inference |
| mic_or_room_behavior | Lid position, mic distance and player-vs-audience perspective materially change the recorded character; treated as part of the instrument, not a mix decision layered on afterward | inference |
| likely_fake_sounding_errors | Uniform-velocity chords (COMMON_ERRORS.md error 3), which is the specific reason a sampled piano reads as organ-like; a pedal lane that changes exactly on bar lines; chords wider than the patch's rolled-voicing behaviour played as instantaneous blocks; repeated notes faster than a real action's repetition rate at identical velocity; dynamics made by a volume fader rather than by velocity, so loud passages are loud but not brighter; release and pedal noise muted for tidiness | inference |
| organic_programming_methods | Voice every chord (melody note highest in velocity, bass next, inner voices lowest) — named cause: `velocity_asymmetry`, a hand does not strike evenly and voicing is intentional. Roll anything wider than the player's declared hand span, by default upward. Spread chord attacks slightly rather than placing every note on one tick — named cause: `chord_asynchrony`. Pedal on harmony changes, not bar lines, using half-pedalling and flutter pedalling in the low register and under descending lines. Give notes real note-offs. Vary velocity between repeated notes for a reason tied to the passage (dynamic shape, accent pattern), not a flat percentage — see `shared/HUMAN_PERFORMANCE_SCHEMA.md` section 4 | sourced: SPANSWICK-PEDAL; PASK-HANDSPAN |

### Harpsichord

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A jack, one per string per register, rises when the key is pressed; a small plectrum (historically a bird-quill, now often synthetic) mounted in the jack plucks the string as the jack rises | sourced: ORGANOLOGY-HARPSICHORD |
| attack_behavior | Essentially one plucking strength regardless of how hard or soft the key is struck, because the plectrum's engagement with the string is set by the jack's geometry, not by key velocity; a controlled study nonetheless measured a real (if modest) loudness difference of up to about 11 dB between a "loud/struck" and a "soft/pressed" touch on some registers of one historical instrument, with listeners able to tell the two touches apart above chance | academic: HARPSICHORD-TOUCH-STUDY-1 |
| sustain_behavior | The string rings after the pluck with no further input from the player; sustain is a matter of the string's own decay, not held player energy the way a bowed or blown note is | inference |
| release_behavior | On key release the jack falls and a damper mounted on the jack silences the string quickly; overholding (leaving keys down beyond the written length) is a real articulation technique used to enrich the sound by letting strings ring together | sourced: ORGANOLOGY-HARPSICHORD + standard-reference: HARPSICHORD-TOUCH-STUDY-1 |
| dynamic_timbre_change | Large-scale dynamic and timbral contrast is made by registration (which string choirs sound, whether manuals are coupled), not by touch; touch contributes a secondary, real but modest loudness/colour difference layered on top of registration | sourced: ORGANOLOGY-HARPSICHORD + academic: HARPSICHORD-TOUCH-STUDY-1 |
| register_character | An 8-foot register sounds at written pitch; a 4-foot register sounds an octave higher; instruments with two manuals typically offer at least one 8-foot choir per manual plus a 4-foot, selectable and combinable via stops, with coupling between manuals adding further combinations | sourced: ORGANOLOGY-HARPSICHORD |
| practical_range | Typically about five octaves on a standard two-manual instrument (specific compass varies by instrument and period); written and sounding pitch match except on a coupled or transposed register, which sounds at its own labelled footage | inference |
| tessitura | No register is dynamically "hard to control" the way a wind instrument's extremes are, since touch does not change loudness much; tessitura concerns are about which registers and stops carry which musical role, not about player effort | inference |
| articulation_logic | Articulation is made by note length, overholding, and registration choice, not by touch dynamics; a detached, clearly released note reads very differently from an overheld, ringing one even at identical pitch and duration otherwise | sourced: ORGANOLOGY-HARPSICHORD |
| phrase_limits | Bounded by hand position and by registration/stop changes, which (like an organ's) are not instantaneous within a phrase; not bounded by breath | inference |
| transitions | No legato transition mechanism exists between plucked notes; phrasing is made through overlap, overholding and touch nuance rather than a connecting technique | inference |
| repeated_note_behavior | A repeated pitch on the same register plucks with essentially the same strength each time; the plectrum's engagement does vary slightly with re-set speed and wear, a real but small source of note-to-note difference | inference |
| vibrato | None available from the mechanism itself | inference |
| pitch_instability | Standard tuning stability of a plucked string instrument; no per-note pitch control exists | inference |
| resonance | Multiple string choirs and, where present, a soundboard rose contribute sympathetic resonance and case colour; specific magnitude not measured by any source read here | to-verify: an acoustics source measuring harpsichord soundboard/rose resonance specifically |
| physical_noise | Audible jack and plectrum mechanism noise (a characteristic "chiff"-like pluck transient and a soft mechanical clack on release) is part of the instrument's identity, not a flaw to remove | inference |
| feasibility | Two hands, one note per finger per string choir; chords beyond what the hand spans are rolled, as on piano, though the harpsichord's lighter action changes the feel, not the physical limit | inference |
| ensemble_behavior | Frequently a continuo/accompaniment role, realizing harmony under a melodic line; registration changes are often used between sections to mark structure | inference |
| recording_behavior | A comparatively quiet, transient-heavy instrument; close miking foregrounds the plectrum attack and mechanism noise, while distant miking favours the string's ring and the room | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Real note-offs matter, since overholding and clean release are both deliberate, audible choices, not incidental | inference |
| overlap | No monophonic legato transition to trigger; overlap here is closer to overholding, an intentional ringing-together of notes, not a sample-triggering requirement | inference |
| velocity | Should not be mapped to loudness the way a piano's is; if a patch offers any velocity-driven layer, treat it as the secondary touch-dynamics effect described above, not the primary dynamic control | academic: HARPSICHORD-TOUCH-STUDY-1 + inference |
| continuous_dynamics | Not applicable within a single sustained note (there is none to crossfade); dynamic shape across a passage is made by registration/stop changes, which are discrete events, not a continuous line | inference |
| expression | Not a meaningful control on this instrument unless a patch maps it to a registration crossfade, in which case it should be documented as such | inference |
| articulation_switching | The primary switch this instrument needs is registration (choir/stop selection) and manual coupling, which functions like an articulation switch even though it is really a timbre/loudness selector | sourced: ORGANOLOGY-HARPSICHORD |
| round_robins | Needed for repeated pitches, as on any plucked instrument, though the variation is smaller than on piano since the plucking strength barely changes | inference |
| release_samples | The jack-fall and damper "clack" on release is a real, audible, and identity-carrying sound; losing it to glued notes is a tell | inference |
| pedal_or_breath_behavior | Not applicable: no pedal or breath control on the historical instrument itself (some 19th/20th-century revival instruments added pedals for registration, which is `unresolved` here) | to-verify: pedal-equipped revival harpsichords, not covered by any source read in this pass |
| transition_samples | Not applicable; no recorded legato transition exists to trigger | inference |
| mic_or_room_behavior | Close mic favours pluck-transient detail; distant mic favours string ring and room, similar in principle to piano but with a quieter, more transient-dominated source | inference |
| likely_fake_sounding_errors | Velocity mapped to a wide loudness range, which the instrument cannot produce; registration changes happening mid-phrase with no structural reason; missing jack/damper mechanism noise; a held chord with no ring-through variation at all | inference |
| organic_programming_methods | Use registration changes at structural points (section boundaries, repeats), not mid-phrase — named cause: this mirrors the organ's `registration_changes` behaviour and should be planned as an event, not a continuous curve. Use overholding deliberately where the music benefits from ring-through, distinct from simply lengthening note values. Keep any velocity-driven touch effect subtle, consistent with the measured magnitude above, not a full dynamic range | sourced: ORGANOLOGY-HARPSICHORD + academic: HARPSICHORD-TOUCH-STUDY-1 |

### Celesta

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Felt-wrapped hammers, operated from a piano-style keyboard and action, strike tuned steel bars; each bar sits over an individual wood resonator box that shapes and reinforces its tone | sourced: HUGILL-CELESTA |
| attack_behavior | A soft, bell-like mallet-style attack; the instrument has only one practical dynamic level, and it is quiet | sourced: HUGILL-CELESTA |
| sustain_behavior | The struck bar rings on its own once struck; sustain is the bar-and-resonator's natural decay, not a held excitation | inference |
| release_behavior | A damper pedal lets the struck bars ring on when depressed and cuts them short when released, comparable in function (not mechanism) to a piano's sustain pedal | sourced: HUGILL-CELESTA |
| dynamic_timbre_change | Very little dynamic range is available; the instrument does not brighten meaningfully with harder playing the way a piano does, and is not written for contrast within a phrase so much as chosen for its single characteristic colour | sourced: HUGILL-CELESTA |
| register_character | Even in colour across its range; the whole instrument functions as a "sparkle" register rather than having strong and weak registers the way a wind or string instrument does | inference |
| practical_range | Written on a piano-style grand staff; the instrument sounds one octave higher than written, so the part is written one octave below the desired sounding pitch | sourced: HUGILL-CELESTA |
| tessitura | The instrument is used throughout its range for the same colouristic purpose; there is no register it avoids for tone-quality reasons the way a wind instrument has weak registers | inference |
| articulation_logic | Articulation is note length and pedal only, as with piano, but with a narrower expressive range since velocity barely changes the sound | inference |
| phrase_limits | Bounded by the hand and the pedal, as with piano; the instrument's low sustain in isolated notes and near-uniform colour make it suited to short figures and sparkle rather than sustained melodic lines | inference |
| transitions | No true legato exists, as with piano; the pedal is the only way to blend successive notes | inference |
| repeated_note_behavior | Governed by the same action-reset logic as a piano action, though celesta parts rarely demand the repetition speeds a virtuosic piano part does | inference |
| vibrato | None; the bar's pitch is fixed once struck | inference |
| pitch_instability | Standard tuning stability of a struck idiophone with fixed, tuned bars; no per-note pitch control | inference |
| resonance | The wood resonator under each bar is central to the tone, not an incidental cabinet effect; with the damper pedal down, struck bars ring together | sourced: HUGILL-CELESTA |
| physical_noise | Hammer-on-bar attack noise is audible at close range and is part of the character, similar in kind to piano hammer noise but brighter and more metallic | inference |
| feasibility | Same hand/finger constraints as piano, played on essentially a piano action and keyboard; usually performed by a keyboardist rather than a percussionist even though the instrument is classified as a percussion idiophone | sourced: HUGILL-CELESTA |
| ensemble_behavior | Used as a colour, not a foundation; pairs recognisably with glockenspiel and with harp in scored combinations, and needs a quiet texture to be heard at all given its narrow dynamic range | sourced: HUGILL-CELESTA |
| recording_behavior | A quiet instrument that needs closer miking or a quieter mix context than most of the ensemble around it to register at all | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Real note-offs let the pedal-controlled ring or the natural decay register properly; not much is lost by gluing notes, since the instrument's decay is fairly short without the pedal, but pedal-held passages need real length | inference |
| overlap | No monophonic legato transition exists; nothing to overlap for triggering purposes | inference |
| velocity | Should select only a narrow loudness range, consistent with the instrument's real dynamic ceiling; a patch with a wide velocity-to-loudness curve overstates the instrument | sourced: HUGILL-CELESTA + inference |
| continuous_dynamics | Not applicable to a single struck note; there is no sustained excitation to crossfade | inference |
| expression | Not a meaningful control unless mapped to overall mix level | inference |
| articulation_switching | Not generally needed; the instrument has essentially one articulation, a soft mallet attack | inference |
| round_robins | Needed for repeated pitches, as with any struck idiophone | inference |
| release_samples | Pedal-release and natural decay tails carry real character; losing them to glued notes removes the "ring" the pedal is for | sourced: HUGILL-CELESTA + inference |
| pedal_or_breath_behavior | The damper pedal is a real, continuous-feeling control (down = ring, up = short) and should be automated as such rather than ignored | sourced: HUGILL-CELESTA |
| transition_samples | Not applicable; no legato transition to trigger | inference |
| mic_or_room_behavior | Given the narrow dynamic range, mic/room choice materially affects whether the part is audible in context at all | inference |
| likely_fake_sounding_errors | A wide velocity-driven dynamic range that the real instrument cannot produce; pedal ignored so notes cut off with no ring; treating it as a lead instrument in a dense mix rather than the quiet-context colour it is | inference |
| organic_programming_methods | Keep the velocity range narrow and consistent with the instrument's real dynamic ceiling — named cause: the instrument genuinely has almost no dynamic range, so "organic" here means restraint, not variation. Use the pedal as a real continuous control at phrase points. Write it into a texture quiet enough for it to be heard, per its known ensemble behaviour | sourced: HUGILL-CELESTA |

### Accordion and Harmonium / Reed Organ

Two related free-reed keyboard instruments; differences are stated in-row. "Harmonium" here means the
Western hand- or foot-pumped free-reed keyboard instrument (reed organ, parlour organ, melodeon), not
the hand-pumped Indian harmonium tradition, which has its own technique and belongs under
`CULTURALLY_SPECIFIC_INSTRUMENTS.md` if written up with tradition sources.

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A free reed, fixed at one end in a close-fitting frame, vibrates back and forth through the frame opening as air is forced past it, interrupting the airflow periodically to produce sound; the accordion supplies air with hand-operated bellows strapped between two keyboards/button boards, the harmonium/reed organ with foot- (or sometimes hand-) operated bellows feeding an internal wind chest | sourced: NEWWORLD-REEDORGAN; WACHTER-ACCORDION |
| attack_behavior | Onset is shaped by how quickly bellows pressure rises at the start of a note, which the player controls directly; there is no separate "strike" the way a struck or plucked instrument has one | sourced: WACHTER-ACCORDION |
| sustain_behavior | Sustains indefinitely as long as bellows motion (accordion) or pumping (harmonium) continues; unlike a struck or plucked instrument, the note does not decay on its own | sourced: NEWWORLD-REEDORGAN |
| release_behavior | Ends when the key is released (stopping air to that reed) or when bellows motion stops; no separate damper mechanism is needed since the driving air is what sustains the reed | inference |
| dynamic_timbre_change | A free reed's pitch is set mainly by its own physical properties (mass, length, stiffness), not by driving pressure, so changing bellows speed mainly changes loudness rather than pitch — unlike a pipe organ's beating reed pipes. Loudness is therefore the bellows' primary output, and is a continuous, played-in-real-time control, not a fixed level per note | sourced: NEWWORLD-REEDORGAN |
| register_character | Consistent character across the practical range on both instruments, since the free-reed principle is uniform; low reeds are physically larger and slower to speak | inference |
| practical_range | Accordion: typically several octaves on the treble side (instrument-dependent) plus a bass/chord side using pre-set buttons on a standard bass system; harmonium/reed organ: typically about five octaves, instrument-dependent | inference |
| tessitura | Both instruments are usable evenly across their range; there is no register the free-reed principle makes especially weak the way a wind instrument's extremes are | inference |
| articulation_logic | Articulation is made primarily by bellows shaping (how a note begins and ends) and by key length, not by a separate technique vocabulary; a bellows "shake" is a rapid in-and-out bellows movement used on accordion as an ornament or accent, found in jazz, zydeco and cabaret styles among others | sourced: WACHTER-ACCORDION + inference |
| phrase_limits | Bounded by available bellows travel (accordion) or by the player's pumping stamina and the reservoir's air supply (harmonium), analogous to a wind player's breath but mechanically mediated | sourced: WACHTER-ACCORDION |
| transitions | No legato transition mechanism exists between notes beyond continuous bellows/air pressure; phrasing across notes is a matter of unbroken air, not a triggered technique | inference |
| repeated_note_behavior | A repeated pitch reflects small, real variations in bellows/pumping consistency and reed settling, not identical repetition | inference |
| vibrato | Not a standard mechanism on either instrument in this scope (distinct from the bellows shake, which is a rhythmic ornament, not a pitch vibrato) | inference |
| pitch_instability | Free reeds are comparatively pitch-stable under changing drive pressure, by design, unlike beating reed pipes | sourced: NEWWORLD-REEDORGAN |
| resonance | Reed organs may couple registers (doubling reeds an octave apart) for a fuller sound at increased air demand; accordions have registers (reed-bank combinations) selected by switches, changing timbre rather than pitch | sourced: NEWWORLD-REEDORGAN |
| physical_noise | Bellows and mechanism noise (key/pallet action, bellows creak) is audible at close range and is part of the instrument's character | inference |
| feasibility | Accordion: two hands, one on buttons/keys for melody, one largely on preset bass/chord buttons, plus continuous bellows management, which is effectively a third independent control the player must coordinate with the fingers; harmonium: two hands on the keyboard plus the feet pumping (or, on some models, a hand-operated bellows lever), which constrains how much can be played with the hands alone during heavy pumping | sourced: WACHTER-ACCORDION; NEWWORLD-REEDORGAN |
| ensemble_behavior | Both function as self-sufficient melody-plus-harmony instruments, similar in ensemble role to piano; the accordion's bellows dynamics give it an expressive, breath-like quality piano lacks | inference |
| recording_behavior | Bellows and mechanism noise are audible at close range on both instruments; harmonium pumping noise (foot or hand) can be audible and is a period-appropriate texture rather than a flaw | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Length is a real, audible parameter since both instruments sustain as long as driven; a glued or arbitrarily long note misrepresents intentional phrasing | inference |
| overlap | No monophonic legato-transition patch requirement in the sampled-strings sense; smooth phrasing is a matter of continuous dynamics, not note overlap | inference |
| velocity | Should not be the primary dynamic control on either instrument; where a patch offers velocity, it is a poor substitute for the bellows/pumping-driven continuous dynamic described below | sourced: NEWWORLD-REEDORGAN + inference |
| continuous_dynamics | The primary and correct dynamic control on both instruments: a continuous bellows/air line should carry the dynamic shape of a held note or phrase, not a fixed velocity value | sourced: WACHTER-ACCORDION; NEWWORLD-REEDORGAN |
| expression | On accordion, register/reed-bank switching is closer to an "expression" control in the sense of a timbre selector than a loudness trim | sourced: NEWWORLD-REEDORGAN |
| articulation_switching | Register (reed-bank) switching on accordion, and coupler engagement on harmonium, function as switches selecting timbre, not articulation in the struck- or bowed-instrument sense | sourced: NEWWORLD-REEDORGAN |
| round_robins | Needed for repeated notes, though the effect is smaller than on a struck or plucked instrument since the reed itself does not physically reset between notes as dramatically | inference |
| release_samples | Release noise (bellows/key mechanism) is audible and should not be glued away | inference |
| pedal_or_breath_behavior | This is the central control for both instruments: bellows motion (accordion, hand-driven) or pumping (harmonium, foot- or hand-driven) should be modelled as a continuous curve carrying dynamics directly, analogous to a wind player's breath but under more direct, sustained mechanical control | sourced: WACHTER-ACCORDION; NEWWORLD-REEDORGAN |
| transition_samples | Not applicable in the sampled-legato sense; continuous air, not a triggered transition sample, carries phrasing | inference |
| mic_or_room_behavior | Bellows and pumping noise are picked up more at close range; distance affects how much mechanism noise is audible relative to reed tone | inference |
| likely_fake_sounding_errors | A held note or chord with a static, unmoving dynamic level, since real bellows/pumping air is never perfectly constant; bellows reversals placed with no regard to phrase structure; velocity used as the primary dynamic control instead of the continuous air line; accordion register switches changing mid-note rather than between phrases | inference |
| organic_programming_methods | Draw the continuous air/bellows control as a phrase-shaped curve, not a flat line — named cause: this is literally what the player's arm or foot is doing throughout the note, the direct analogue of `phrase_arch`. Place bellows reversals at points the articulation allows, timed with the finger action, per accordion pedagogy. Use the bellows shake deliberately as a named ornament, not as random modulation, where the style calls for it | sourced: WACHTER-ACCORDION |

### Tine Electric Piano (Rhodes-type)

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A key-operated hammer with a neoprene tip strikes a thin spring-steel rod (a tine) cantilevered from a larger tuning-fork-shaped tone bar; the vibrating ferromagnetic tine's motion is sensed by an electromagnetic pickup (a wound permanent magnet) positioned near its tip, inducing an alternating voltage. The key action is comparable to a Viennese-style piano action, with the hammer in direct contact with the key rather than an escapement-and-repetition mechanism | academic: PFEIFLE-2017 |
| attack_behavior | A struck attack, as on piano; higher-velocity strikes produce a richer harmonic sound than softer playing, so velocity changes timbre as well as level | academic: PFEIFLE-2017 |
| sustain_behavior | The tine rings after the strike, decaying on its own; an individual felt damper contacts each tine from below at rest, damping it when the key is not held and the sustain pedal is up | academic: PFEIFLE-2017 + manual-derived: TINE-EPIANO-MANUAL-1 |
| release_behavior | The felt damper drops back onto the tine when the key is released (and the pedal is up), stopping the sound; with the pedal down, all dampers are lifted at once via a damper release bar and tines ring until they decay naturally | manual-derived: TINE-EPIANO-MANUAL-1 |
| dynamic_timbre_change | Harder strikes yield a brighter, more harmonically rich tone; the position of the tine relative to the pickup magnet also shapes timbre and is a fixed setup adjustment, not a per-note control | academic: PFEIFLE-2017 |
| register_character | Even in general playability across the keyboard; very low notes rely more on fundamental-adjacent partials than on a rich harmonic spread, as with any struck metal bar/rod source | inference |
| practical_range | Standard 73- or 88-key layouts existed depending on model; written and sounding pitch match (non-transposing) | inference |
| tessitura | Usable evenly across the range; no register is avoided for tone-quality reasons the way a wind instrument's extremes are | inference |
| articulation_logic | Articulation is note length, attack strength and pedal, as with acoustic piano, since the key action and damper model closely parallel a piano's | academic: PFEIFLE-2017 |
| phrase_limits | Bounded by the hand and the pedal, exactly as with acoustic piano, since the action and damper mechanism are directly comparable | manual-derived: TINE-EPIANO-MANUAL-1 |
| transitions | No true legato transition exists, as with piano; connection between notes is made by finger overlap and pedal | inference |
| repeated_note_behavior | Governed by the felt-tipped hammer key action's reset speed, comparable in kind (though not necessarily in maximum rate) to a piano action | academic: PFEIFLE-2017 |
| vibrato | None from the mechanism itself; some instruments offer a built-in tremolo/vibrato circuit, which is an amplitude or pitch effect applied electronically, not a played technique | inference |
| pitch_instability | Standard tuning stability; the tine's fundamental is set by its length and by added/removed solder mass at the tip, a setup adjustment, not a performance variable | inference |
| resonance | No significant sympathetic string resonance the way a piano has, since each note has its own isolated tine; tone bar and pickup interaction is the closest analogue | inference |
| physical_noise | Key and damper mechanism noise, and an audible mechanical "clunk" from some units, are part of the instrument's identity | inference |
| feasibility | Same hand/finger constraints as piano, played on a piano-style keyboard | inference |
| ensemble_behavior | Functions as a comping/lead keyboard voice, frequently in jazz, soul and funk contexts; blends differently from acoustic piano because of its narrower, more focused electromagnetic-pickup timbre | inference |
| recording_behavior | Typically recorded direct or through an amplifier; distortion and vibrato/tremolo circuit character (where present) are part of the recorded sound, not effects added afterward | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Real note-offs matter for the damper and release character to register, as with piano | manual-derived: TINE-EPIANO-MANUAL-1 |
| overlap | No monophonic legato-transition requirement; connection between notes is a performance illusion via pedal, as with piano | inference |
| velocity | Should select level and timbre together, mirroring the real strike-to-harmonic-richness relationship | academic: PFEIFLE-2017 |
| continuous_dynamics | Not applicable within a single held note in the bowed/blown sense, since there is no sustained excitation to crossfade; dynamic shape is built note by note through velocity | inference |
| expression | A patch-level trim, not a substitute for velocity | inference |
| articulation_switching | Not generally needed for the core instrument; pedal state is the closest equivalent | inference |
| round_robins | Needed for repeated pitches, as with any struck instrument | inference |
| release_samples | Damper-drop and mechanism noise on release; lost if notes are glued end to end | manual-derived: TINE-EPIANO-MANUAL-1 |
| pedal_or_breath_behavior | A real sustain pedal, pedalled much like an acoustic piano's: half-pedalling and pedal timed to harmony are applicable in principle, since the mechanism (a damper release bar lifting all dampers together) is directly analogous | manual-derived: TINE-EPIANO-MANUAL-1 |
| transition_samples | Not applicable; no recorded legato transition to trigger | inference |
| mic_or_room_behavior | Direct/DI and amplifier/room capture are genuinely different sources on this instrument, as with electric guitar; treat them as distinct signal paths, not one "mic position" choice | inference |
| likely_fake_sounding_errors | Uniform velocity (loses the timbre-brightening effect, which is central to the instrument's identity); glued notes losing damper release character; sustain pedal treated as a binary switch instead of pedalled like a piano's; no round robins on repeated chords | inference |
| organic_programming_methods | Map velocity to timbral brightness, not only level — named cause: `velocity_asymmetry`/attack-hardness, directly evidenced for this instrument. Pedal the sustain like a piano's, including partial and re-pedalling gestures where the target can carry them. Give notes real note-offs so damper character registers | academic: PFEIFLE-2017 + manual-derived: TINE-EPIANO-MANUAL-1 |

### Reed Electric Piano (Wurlitzer-type)

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A key-operated action, regulated comparably to a scaled-down grand piano action, drives a felt-tipped hammer against a metal reed; the reed's vibration is sensed by an electrostatic pickup, a time-varying capacitor formed between the grounded, vibrating reed and a fixed, charged plate | academic: PFEIFLE-2017 |
| attack_behavior | A struck attack, as on piano; higher-velocity strikes produce a richer harmonic sound than soft playing, so velocity changes timbre, not only level | academic: PFEIFLE-2017 |
| sustain_behavior | The reed rings after the strike and decays on its own; an individual felt damper rests on each reed at rest, damping it when the key is not held and the pedal is up | sourced: REED-EPIANO-SERVICE-1 + academic: PFEIFLE-2017 |
| release_behavior | The damper felt returns to the reed when the key is released (pedal up), stopping the sound; the sustain pedal lifts all damper felts at once via a cable-and-rod mechanism, comparable in function to a piano's damper pedal | sourced: REED-EPIANO-SERVICE-1 |
| dynamic_timbre_change | Harder strikes yield a richer, more harmonically complex tone, directly analogous to the tine piano and to acoustic piano's velocity-to-timbre relationship | academic: PFEIFLE-2017 |
| register_character | Even in general playability across the keyboard; reed length and mass are set per note in manufacture, not adjustable in performance | inference |
| practical_range | Standard piano-style keyboard layouts (models varied, commonly 64 to 73 keys); written and sounding pitch match (non-transposing) | inference |
| tessitura | Usable evenly across the range | inference |
| articulation_logic | Articulation is note length, attack strength and pedal, as with acoustic piano, since the key action is explicitly regulated like a (miniaturized) grand piano action | academic: PFEIFLE-2017 |
| phrase_limits | Bounded by the hand and pedal, exactly as with acoustic piano | sourced: REED-EPIANO-SERVICE-1 |
| transitions | No true legato transition exists, as with piano | inference |
| repeated_note_behavior | Governed by the felt-tipped hammer action's reset speed, structurally comparable to a (miniaturized) piano action | academic: PFEIFLE-2017 |
| vibrato | None from the mechanism itself | inference |
| pitch_instability | Standard tuning stability; reed fundamental is set by manufacture (length, mass, tip solder), not a performance variable | inference |
| resonance | No significant sympathetic resonance between reeds the way a piano's strings couple; each note's reed is its own isolated resonator | inference |
| physical_noise | Key action and damper mechanism noise are part of the instrument's identity | inference |
| feasibility | Same hand/finger constraints as piano, played on a piano-style keyboard and (per this pass's correction) a comparably regulated action | academic: PFEIFLE-2017 |
| ensemble_behavior | Comping/lead keyboard voice in jazz, soul, and pop contexts; its electrostatic-pickup timbre and characteristic "bark" under hard playing distinguish it from the tine piano's electromagnetic-pickup character | academic: PFEIFLE-2017 |
| recording_behavior | Typically recorded direct or through an amplifier; hard playing introduces an audible overdrive-like "bark," which is part of the instrument's normal dynamic range, not a fault | academic: PFEIFLE-2017 |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Real note-offs matter for damper and release character, as with piano | sourced: REED-EPIANO-SERVICE-1 |
| overlap | No monophonic legato-transition requirement; connection between notes is a performance illusion, as with piano | inference |
| velocity | Should select level and timbre together, mirroring the real strike-to-harmonic-richness relationship | academic: PFEIFLE-2017 |
| continuous_dynamics | Not applicable within a single held note in the bowed/blown sense; dynamic shape is built note by note through velocity | inference |
| expression | A patch-level trim, not a substitute for velocity | inference |
| articulation_switching | Not generally needed for the core instrument; pedal state is the closest equivalent | inference |
| round_robins | Needed for repeated pitches, as with any struck instrument | inference |
| release_samples | Damper-drop and mechanism noise on release; lost if notes are glued end to end | sourced: REED-EPIANO-SERVICE-1 |
| pedal_or_breath_behavior | A real sustain pedal, pedalled much like an acoustic piano's, since the mechanism (a cable-and-rod assembly lifting all damper felts together) is directly analogous | sourced: REED-EPIANO-SERVICE-1 |
| transition_samples | Not applicable; no recorded legato transition to trigger | inference |
| mic_or_room_behavior | Direct/DI and amplifier/room capture are genuinely different sources, as with the tine piano and electric guitar | inference |
| likely_fake_sounding_errors | Uniform velocity, which loses the timbre-brightening (and characteristic "bark" at high velocity) that is central to the instrument's identity; glued notes losing damper release character; sustain pedal treated as a binary switch instead of pedalled like a piano's; treating this instrument as if it sustains substantially longer than an acoustic piano, a claim no source read here supports | academic: PFEIFLE-2017 + to-verify: not measured by any source read in this pass |
| organic_programming_methods | Map velocity to timbral brightness and "bark," not only level — named cause: directly evidenced for this instrument. Pedal the sustain like a piano's. Give notes real note-offs so damper character registers | sourced: REED-EPIANO-SERVICE-1 + academic: PFEIFLE-2017 |

### Clavinet

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A rubber-tipped tangent, mounted under each key, is driven down onto the string and traps it against a fixed metal anvil for the duration of the note, both exciting the string and dividing it into a speaking and non-speaking length; pickups (commonly two, at different positions) sense the speaking length's vibration. This is a struck-and-stopped mechanism, not a plucked one | sourced: CLAVINET-FAQ-1 |
| attack_behavior | A sharp, percussive attack from the tangent striking the string against the anvil, closer in character to a fretted string instrument's fret-and-pluck attack than to a piano hammer's | sourced: CLAVINET-FAQ-1 |
| sustain_behavior | Short: the struck-and-stopped string decays quickly compared to a piano string, and the instrument is not used for long sustained notes idiomatically | inference |
| release_behavior | Release is immediate and percussive; a damper (yarn on a mute bar) rests against the strings and mutes them when the tangent releases, and its position/adjustment materially affects whether notes ring on or cut cleanly | sourced: CLAVINET-FAQ-1 |
| dynamic_timbre_change | Harder key strikes drive the tangent against the anvil more forcefully, affecting attack character and level; the instrument has no pedal and no sustain-pedal-style resonance behaviour | sourced: CLAVINET-FAQ-1 |
| register_character | Even in playability across its range; the instrument's identity is rhythmic and percussive throughout rather than register-dependent | inference |
| practical_range | Standard piano-style keyboard layout on the common models (roughly five octaves); written and sounding pitch match (non-transposing) | inference |
| tessitura | Used across its range for its percussive, rhythmic character rather than avoided in any register | inference |
| articulation_logic | Articulation is almost entirely note length and rhythmic placement, since the instrument has no pedal and minimal sustain to manage otherwise | inference |
| phrase_limits | Bounded by the hand, as with piano, but the instrument's short natural decay means phrasing is built from rhythm and repetition rather than sustained lines | inference |
| transitions | No legato transition mechanism; the instrument's idiom is built on discrete, separated attacks | inference |
| repeated_note_behavior | Governed by how quickly the tangent-and-key mechanism resets; muted release (the damper yarn engaging quickly) is central to the instrument's rhythmic feel and is itself a big part of "the groove," not an incidental byproduct | sourced: CLAVINET-FAQ-1 |
| vibrato | None from the mechanism itself | inference |
| pitch_instability | Standard tuning stability; strings are tuned like guitar strings and are subject to the same oxidation-related tonal dulling over time as any wound string, a maintenance fact rather than a performance one | sourced: CLAVINET-FAQ-1 |
| resonance | No significant sympathetic resonance between strings the way a piano's coupled unisons resonate, since each string is individually struck and stopped | inference |
| physical_noise | Tangent-strike and mechanism noise (including audible "click"/"thunk" artifacts from worn hammer tips on real instruments, a maintenance issue rather than a performance feature) are part of the instrument's percussive identity | sourced: CLAVINET-FAQ-1 |
| feasibility | Same hand/finger constraints as piano, played on a piano-style keyboard | inference |
| ensemble_behavior | A rhythmic/comping voice, prominently associated with funk and soul contexts; typically sits in a percussive role alongside or instead of guitar, not as a harmonic pad | inference |
| recording_behavior | Typically recorded direct through pickups (often through effects such as wah or an envelope filter, which are commonly used with this instrument and shape its recorded identity as much as the raw pickup signal does) | sourced: CLAVINET-FAQ-1 |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | A central, constantly-used control, since the instrument's idiom is built on note length and muted release rather than sustain | inference |
| overlap | No monophonic legato-transition requirement; the idiom is discrete, separated attacks | inference |
| velocity | Selects attack strength/level; not a timbre-brightening mechanism to the degree the tine and reed pianos have, since the struck-and-stopped mechanism behaves differently from a free-ringing struck string | sourced: CLAVINET-FAQ-1 + inference |
| continuous_dynamics | Not applicable; no sustained excitation to crossfade within a note | inference |
| expression | Not a meaningful control on the core instrument | inference |
| articulation_switching | Not generally needed; pickup-configuration character (where modelled) is closer to a patch-level tone choice than a per-note articulation switch | inference |
| round_robins | Needed for repeated notes, since the instrument's idiom relies heavily on fast repetition | inference |
| release_samples | The muted, damped release is central to the instrument's rhythmic identity, not an optional detail; losing it to glued notes removes the groove | sourced: CLAVINET-FAQ-1 |
| pedal_or_breath_behavior | Not applicable: the instrument has no pedal | sourced: CLAVINET-FAQ-1 |
| transition_samples | Not applicable; no legato transition to trigger | inference |
| mic_or_room_behavior | Not meaningfully applicable; the instrument is a direct-pickup, not an acoustically miked, source, and its recorded identity is shaped as much by outboard effects (wah, envelope filter) as by pickup position | sourced: CLAVINET-FAQ-1 |
| likely_fake_sounding_errors | Notes glued end to end, which removes the muted-release groove that is the instrument's central expressive device; uniform velocity with no attack variation; sustained pad-like writing, which fights the instrument's short-decay idiom; no round robins on repeated funk patterns | sourced: CLAVINET-FAQ-1 + inference |
| organic_programming_methods | Write note length and muted release deliberately as the primary rhythmic device — named cause: `note_length_variation`, directly evidenced as central to this instrument's idiom. Vary attack velocity across a repeated pattern for a named reason (accent pattern, metrical position), not a flat percentage. Keep phrasing short and rhythmic rather than sustained, consistent with the instrument's real decay behaviour | sourced: CLAVINET-FAQ-1 |

---

## What the instrument is

A piano is a struck-string keyboard instrument: felt hammers thrown at strings by a mechanical action,
with dampers that stop the strings and pedals that lift or soften them. The player has no contact with
the string after the hammer leaves the action, so everything about a single note is decided at the
moment of the strike, and everything after it is decay, pedalling and release [sourced: SMIT-PIANOACTION]. Multi-string unisons are dynamically coupled through the bridge, producing a
two-stage decay whose slow second phase ("aftersound") is a real acoustic phenomenon, not an artifact
[academic: WEINREICH-1977].

The rest of the keyboard family shares "a keyboard operating a sound-producing mechanism" and little
else. A harpsichord plucks; a celesta strikes tuned steel bars; an accordion or harmonium drives free
reeds with player-controlled air; a clavinet strikes a string against a fixed anvil rather than a
piano's free string; and the tine and reed electric pianos strike a metal resonator (a tine or a reed)
and sense it electromagnetically or electrostatically rather than acoustically. Programming any of
these as "quiet piano" is the single most common category error this file exists to prevent.

## Range and register

Grand piano covers A0 to C8, seven and a bit octaves, non-transposing; the celesta is written one
octave below where it sounds [sourced: HUGILL-CELESTA], which is the one genuinely transposing
instrument in this family. Harpsichord compass varies by instrument and period, commonly around five
octaves. Accordion and harmonium ranges are instrument-dependent; both are usable evenly across their
practical compass because the free-reed mechanism does not have the register-dependent weak spots a
wind instrument has [sourced: NEWWORLD-REEDORGAN]. The two electric pianos and the clavinet follow
their era's common keyboard layouts (typically five to just over six octaves) and are non-transposing.

## Articulation and note transitions

None of these instruments has a true legato transition in the sampled-strings sense: there is no
mechanism that glides pitch or blends timbre continuously from one note into the next. What reads as
"legato" on piano, electric piano or clavinet is finger overlap plus release timing; on harpsichord it
is overholding; on accordion or harmonium it is unbroken air across a phrase; on organ-adjacent
celesta it is the damper pedal. Programming any of them with a monophonic legato-transition patch model
borrowed from `STRINGS.md` or `WOODWINDS.md` is a category error [inference].

## Physical constraints

```text
piano, celesta, tine e-piano, reed e-piano, clavinet: two hands, ten fingers, keyboard-standard reach
harpsichord: as above, lighter action, same hand-span physics
accordion: two hands (one largely on preset bass/chord buttons) plus continuous bellows management
harmonium: two hands on keys plus feet (or a hand lever) pumping continuously
```

Hand span is not a fixed constant. About 8.5 inches (21.6 cm) is the threshold below which a tenth is
not comfortably reachable, adult male hand spans average roughly an inch more than adult female hand
spans, and by cited figures a majority of adult women cannot comfortably play a tenth on a standard
keyboard [sourced: PASK-HANDSPAN]. "A ninth comfortably" is not a safe universal default; a chord wider
than the declared hand span is rolled, which is a deliberate, different sound, not an error.

## Phrase behaviour

Piano, electric piano and clavinet phrases are bounded by the hand and by pedal or note-length choices,
not by breath: every struck note begins decaying immediately, so a sustained line is built from
re-strikes, figuration, or pedal holding harmony while the hand moves [inference]. Harpsichord phrasing
adds registration changes as structural, between-phrase events [sourced: ORGANOLOGY-HARPSICHORD].
Accordion and harmonium phrasing is genuinely breath-like: bounded by bellows travel or pumping stamina,
and carried by a continuous air control the way a wind player's breath carries a phrase [sourced: WACHTER-ACCORDION; NEWWORLD-REEDORGAN].

## Ensemble behaviour

Piano, electric piano, harpsichord (as continuo) and accordion/harmonium typically cover their own
bass, harmony and melody, so in an ensemble each is usually either the whole accompaniment or a
deliberately restricted layer [inference]. The clavinet instead usually takes a rhythmic, comping role
alongside or instead of guitar [inference]. Celesta is a colour instrument, not a foundation, and needs
a quiet texture to register given its narrow dynamic range [sourced: HUGILL-CELESTA].

## Recording behaviour

Piano, celesta and harpsichord are acoustic sources whose recorded character depends heavily on mic
distance and room; the electric pianos and clavinet are pickup-based sources where direct signal and
amplifier/room capture are genuinely separate signal paths, not one "mic position" choice, and the
clavinet's recorded identity is shaped as much by outboard effects (wah, envelope filter) as by the
pickup itself [sourced: CLAVINET-FAQ-1]. Accordion and harmonium recordings carry audible bellows or
pumping mechanism noise at close range, which is period-appropriate texture, not a flaw [inference].

## Programming it: the control model

```yaml
piano_and_celesta_and_ep_and_clav:
  velocity: selects level and timbre together on piano, tine e-piano and reed e-piano (struck
    mechanism, evidenced); level and attack character on clavinet (struck-and-stopped mechanism);
    a narrow loudness range only on celesta
  continuous_dynamics: not applicable within a single note on any of these; dynamic shape is built
    note by note through velocity and voicing
  pedal: a real, continuous-feeling sustain control on piano, tine e-piano and reed e-piano, pedalled
    comparably across all three because the damper mechanisms are directly analogous; a damper pedal
    on celesta with the same down=ring, up=short logic; no pedal on clavinet
harpsichord:
  velocity: should not drive a wide loudness range; registration is the primary dynamic and timbral
    control, touch a secondary, measured-but-modest effect on top of it
accordion_and_harmonium:
  continuous_dynamics: the primary and correct control, via a bellows/air line, not velocity
  articulation_switching: register/reed-bank or coupler selection, a timbre choice, not an
    articulation in the struck- or bowed-instrument sense
```

Controller numbers, exact layer counts and specific latencies are product facts and belong in the
calibration profile, not here [inference].

## Programming it: what makes it sound real

- Voice every piano, e-piano or celesta chord: melody highest in velocity, bass next, inner voices
  lowest [sourced: SMIT-PIANOACTION].
- Roll anything wider than the declared hand span, by default upward [sourced: PASK-HANDSPAN].
- Pedal follows harmony on piano and both electric pianos, not bar lines; use half-pedalling and
  flutter pedalling where the register is low enough to muddy [sourced: SPANSWICK-PEDAL].
- On the electric pianos, map velocity to brightness and (on the reed piano) the characteristic "bark,"
  not only to level [academic: PFEIFLE-2017].
- On the clavinet, treat note length and muted release as the primary expressive device, since the
  instrument's groove lives there, not in sustain [sourced: CLAVINET-FAQ-1].
- On harpsichord, change registration between phrases or sections, not mid-line, and use overholding
  deliberately where ring-through is wanted [sourced: ORGANOLOGY-HARPSICHORD].
- On accordion and harmonium, draw the bellows/air line as a phrase-shaped curve, and place bellows
  reversals where the articulation allows them [sourced: WACHTER-ACCORDION].
- On celesta, keep the dynamic range narrow and use the pedal as a real, phrase-level control [sourced: HUGILL-CELESTA].
- Give notes real note-offs on every instrument in this family so damper, release and mechanism noise
  is heard.

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Family-specific tells:

- uniform-velocity piano or electric-piano chords, which is error 3, and the reason a sampled piano or
  electric piano reads as organ-like;
- a piano or electric-piano pedal lane that changes exactly on bar lines;
- harpsichord velocity mapped to a wide loudness range the real mechanism cannot produce;
- harpsichord registration changing mid-phrase rather than at structural points;
- accordion or harmonium held notes with a static, unmoving dynamic level;
- accordion bellows reversals placed with no regard to phrase structure;
- clavinet notes glued end to end, losing the muted-release groove that is the instrument's central
  device;
- celesta given a piano-scale dynamic range it does not have;
- reed electric piano assumed to sustain longer than an acoustic piano, a claim no source read for this
  pass supports [to-verify: comparative sustain length versus acoustic piano, in Fletcher and Rossing or a manufacturer source].

## What the Performance Director needs from this file

- `impossible_voicings`: any simultaneous span wider than the declared (not assumed) hand span on
  piano, celesta, tine e-piano, reed e-piano or clavinet. Wider spans are rolled, a performance
  decision, not an error. Harpsichord follows the same hand-span physics with a lighter action.
- `limb_or_finger_conflicts`: two hands on all seven cards; accordion adds continuous bellows
  management as an effectively independent control the player must coordinate with the fingers;
  harmonium adds foot pumping.
- `velocity_asymmetry` is the correct imperfection cause for chord voicing on piano, celesta and both
  electric pianos, expected on every chord, not occasional.
- `melody_lead` applies wherever chords are voiced by hand on a struck keyboard instrument.
- Repeated-note rate is a real feasibility check on piano (grand vs. upright differ), both electric
  pianos, and clavinet; less so on harpsichord, celesta, accordion or harmonium.
- `dynamic_arc.control` must be the bellows/air line, not velocity, for accordion and harmonium; must
  be registration events, not a continuous curve, for harpsichord.
- Pedal state (piano, both electric pianos, celesta) is a continuous or event-based automation target
  that MIDI Builder and the DAW adapter need explicitly, not an assumed default.

## Sources and what to verify

- **To verify**: hammer felt as a nonlinear spring and the exact velocity-to-spectrum relationship, in
  Fletcher and Rossing, *The Physics of Musical Instruments*. Not opened for this work.
- **To verify**: register descriptions and practical writing ranges in Adler, *The Study of
  Orchestration*. Not opened.
- **To verify**: the Railsback stretch's magnitude by register; `RAILSBACK-STRETCH-2015` was read only
  at excerpt (search-summary) depth, not opened directly.
- **To verify**: whether reed or tine electric pianos genuinely sustain longer, shorter or comparably
  to an acoustic piano at a matched dynamic; no source read here measures this comparison.
- **To verify**: the sostenuto pedal's mechanism; no source read in this pass describes it specifically.
- **Not available**: any measured figure for typical chord-roll spread or bellows-reversal timing.
  Both are practitioner values until calibrated.
- The Indian hand-pumped harmonium tradition is deliberately out of scope for the accordion/harmonium
  card here; it would need its own tradition-institution sources under
  `CULTURALLY_SPECIFIC_INSTRUMENTS.md`.
