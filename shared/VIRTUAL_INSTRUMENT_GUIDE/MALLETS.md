# Mallets

Tuned percussion struck with mallets: marimba, vibraphone, xylophone, glockenspiel, and, more
briefly, tubular bells and crotales. Orchestral (non-mallet-keyboard) percussion has its own page,
`PERCUSSION.md`, and the drum kit has its own, `DRUM_KIT.md`.

> Evidence: read at section depth this pass: an acoustics textbook's pages on marimba and xylophone
> bar tuning (source ID WOODHOUSE-MARIMBA), four university percussion-studio pages and one
> percussion pitch-and-notation reference for written/sounding ranges (BYU-MARIMBA, BYU-VIBRAPHONE,
> BYU-XYLOPHONE, BYU-GLOCKENSPIEL, RONNEFARTH-PITCH-RANGE), one university four-mallet grip page for
> interval span (UH-FOUR-MALLET), and Rimsky-Korsakov's *Principles of Orchestration* for register
> colour and use (RIMSKY-1913). Bar-decay times by material and register, resonator-tube tuning
> detail beyond the fundamental, and measured roll rates were not opened at section depth and are
> left to-verify. Read depths and full citations are in `research/sources/INSTRUMENT_SOURCES.md`; the claims and their
> limits are in `research/instruments/MALLETS.md`.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## Behaviour cards

### Marimba

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Wooden bars (rosewood or a synthetic substitute) over tuned resonator tubes; each tube is tuned to reinforce its bar's fundamental. | sourced: BYU-MARIMBA + academic: WOODHOUSE-MARIMBA |
| attack_behavior | A mallet strike excites the bar's fundamental and a series of higher partials; makers undercut the underside of each bar to bring the second partial close to a small-integer ratio of the fundamental (see Range and register), which is what gives a struck bar a clear, focused pitch rather than a clangorous one. | academic: WOODHOUSE-MARIMBA |
| sustain_behavior | Short: a wooden bar's decay is measured in roughly a second or two, not held indefinitely; a marimba does not sustain a note the way a bowed or blown instrument does. | sourced: BYU-MARIMBA |
| release_behavior | The bar's natural decay is the release; hand-dampening (a finger pressed to a ringing bar) stops it early and deliberately. | inference |
| dynamic_timbre_change | Soft (yarn) mallets favour the fundamental and give a warm, rounded tone; hard (rubber, brass) mallets bring out more of the higher partials for a bright, articulate attack; this is a mallet choice, not a velocity curve. | sourced: BYU-MARIMBA |
| register_character | Rich fundamental and full tone through the low and middle register, thinner and more attack-dominated at the top, where the bars are short and stiff. | inference |
| practical_range | Non-transposing (sounds as written); a large concert instrument spans roughly C2 to C7, five octaves; smaller student instruments cover three to four. | sourced: BYU-MARIMBA |
| tessitura | Fullest and most controllable in the low-to-middle register; the extreme top octave is thin and short-decaying and is used for colour and articulation rather than sustained melody. | inference |
| articulation_logic | Single strokes and rolls (rapid alternation, single-bar or between chord tones) are the two fundamental techniques; dead strokes (mallet held against the bar after impact, more a vibraphone technique but usable here) give a dry, damped thud. | sourced: BYU-MARIMBA + inference |
| phrase_limits | Bounded by decay (a marimba cannot hold a note, only roll it) and by reach; a leap across the instrument, or a change of four-mallet interval, takes real travel time. | inference |
| transitions | No true legato; every note is a fresh strike. A sustained line is written as a roll, not as a long note. | inference |
| repeated_note_behavior | Real repeated single-bar notes vary mallet contact and force slightly stroke to stroke; a roll at one unchanging velocity is a specific, audible tell of a programmed part. | inference |
| vibrato | None mechanically; some players use a very fast, close roll to approximate a shimmer, which is a roll-rate choice, not a separate control. | inference |
| pitch_instability | Essentially none once built and tuned; unlike a membrane, a wooden bar's pitch does not drift with a player's touch. | inference |
| resonance | The tuned tube under each bar is a Helmholtz-type resonator reinforcing that bar's fundamental; without it a bar sounds thinner and more percussive. | academic: WOODHOUSE-MARIMBA |
| physical_noise | Mallet click on impact, proportionally more audible with harder mallets or at the instrument's thin top register. | inference |
| feasibility | Two hands, two or four mallets. Two mallets give two simultaneous notes; four give up to four, but a four-mallet chord is bounded by the two mallets in one hand, which typically span from a 2nd up to an octave comfortably, with a 9th or 10th reachable by an experienced player using a wide-spread grip (most commonly the Stevens grip) but genuinely difficult, not a routine interval. | sourced: UH-FOUR-MALLET |
| ensemble_behavior | Cuts through by attack rather than by sustained level, so it doubles melodic or bass lines effectively even at moderate dynamic; doubling a bass line adds attack and definition without adding weight the way a sustained bass instrument would. | inference |
| recording_behavior | A large instrument that needs distance for the resonator tubes to speak fully; close-miking emphasises mallet click at the expense of tube resonance. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | A held MIDI note does not sustain a real marimba note past its natural decay; sustain has to come from a roll construction (a real roll articulation or genuinely repeated notes), not a long note on a one-shot sample. | inference |
| overlap | Not a legato instrument; no overlap requirement between discrete strikes. | inference |
| velocity | Selects among recorded dynamic layers, and, where the library offers separate mallet-hardness recordings, those are a separate axis from velocity, not reachable by velocity alone. | inference |
| continuous_dynamics | A roll's crescendo or diminuendo needs a drawn shape, built from the roll's own construction (recorded roll dynamics, or per-note velocity across repeated triggers), not a static value. | inference |
| expression | Not the primary control for a single struck note. | inference |
| articulation_switching | Mallet hardness (soft yarn through hard rubber/brass) and dead stroke are separate recorded sample sets, not EQ variants of one recording. | sourced: BYU-MARIMBA |
| round_robins | Essential; repeated single-bar notes, common in mallet writing, are exposed to the machine-gun error quickly. | inference |
| release_samples | A hand-damped note's stop is audible and distinct from the bar's own natural decay; a patch with no damped-release sample cannot represent a deliberately stopped note. | inference |
| pedal_or_breath_behavior | Not applicable; the marimba has no sustain pedal. | inference |
| transition_samples | Not applicable between discrete strikes. | inference |
| mic_or_room_behavior | Distance matters for resonator tube sound, as in Recording behaviour above; an all-close mix loses it. | inference |
| likely_fake_sounding_errors | A long held note where a real marimba would already have decayed to silence; a roll built from identical repeated samples at one velocity; four-mallet chords wider than a real player's reach; mallet hardness faked with a filter instead of a separate recording. | inference |
| organic_programming_methods | Sustain with rolls, never with long notes; choose the mallet set before writing, since it changes the instrument's character more than velocity does; keep four-mallet voicings inside the documented reach, treating a 9th or 10th as a deliberate, occasional stretch rather than a routine one; vary velocity between roll strokes and between the two hands (`velocity_asymmetry`). | sourced: UH-FOUR-MALLET |

### Vibraphone

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Metal (aluminium alloy) bars over resonator tubes, each tube fitted with a motor-driven rotating disc (a "fan") that opens and closes it. | sourced: BYU-VIBRAPHONE |
| attack_behavior | A mallet strike excites the bar; soft, yarn-wrapped mallets are close to the only acceptable choice for a good tone, unlike the marimba's wider range of mallet hardness. | sourced: BYU-VIBRAPHONE |
| sustain_behavior | Metal bars ring far longer than marimba's wooden bars; sustain is real and extended, not simulated by a roll the way the marimba's is. | inference |
| release_behavior | Damped by hand (a "dead stroke," mallet held against the bar) or, more commonly, by the pedal's damper bar; releasing the pedal drops the damper and cuts everything currently ringing. | sourced: BYU-VIBRAPHONE |
| dynamic_timbre_change | As with any struck bar, harder strikes bring more high-partial energy; the motor's tremolo (see below) is a separate, independent control from strike dynamics. | inference |
| register_character | The warmest part of the instrument is its low register; unlike the marimba, the vibraphone sustains there rather than decaying quickly, which is part of why it reads as a different instrument rather than a metal marimba. | inference |
| practical_range | Non-transposing (sounds as written); typically three octaves on a common instrument, with some four-octave instruments extending the range further. | sourced: BYU-VIBRAPHONE; RONNEFARTH-PITCH-RANGE |
| tessitura | Even and controllable across its range; the extended low octave on a four-octave instrument is a real addition rather than a weak extension, given the metal bars' sustain. | inference |
| articulation_logic | Struck note (pedal up or down), dead stroke (damped immediately), and pedalled sustain are the core techniques; the motor is a further, independent on/off/speed choice layered on top of any of them. | sourced: BYU-VIBRAPHONE |
| phrase_limits | Phrasing is bounded by the pedal: notes accumulate under a raised damper and must be cleared, so pedalling and dampening are the phrasing, closely analogous to a piano's sustain pedal but with a much longer natural decay and an audible motor if engaged. | inference |
| transitions | No true legato; the pedal creates the impression of connection by letting notes ring into one another, which is a different mechanism from a bowed or blown legato. | inference |
| repeated_note_behavior | As marimba: real repeated notes vary mallet contact and force; a roll at one velocity is an audible tell. | inference |
| vibrato | Not a finger or breath vibrato; the motor produces an amplitude tremolo (see below), which is the instrument's only built-in periodic modulation and is not pitch vibrato. | sourced: BYU-VIBRAPHONE |
| pitch_instability | Essentially none; metal bars do not drift with touch. | inference |
| resonance | Resonator tubes reinforce each bar's fundamental, as on the marimba; the motor-driven fans inside the tubes are what make the vibraphone's resonance periodically modulated rather than constant. | sourced: BYU-VIBRAPHONE |
| physical_noise | Mallet click on impact; motor mechanism noise (a soft whirring) audible on some instruments when the motor is engaged. | inference |
| feasibility | Two hands, two or four mallets, with the same reach limits (roughly a 2nd to an octave per hand comfortably, up to a 9th or 10th with difficulty) documented for marimba, though the Stevens grip most associated with wide marimba spreads is rarely used on vibraphone, whose most common grip (Burton) was developed for this instrument specifically. | sourced: UH-FOUR-MALLET; BYU-VIBRAPHONE |
| ensemble_behavior | Sustains and blends more like a keyboard pad than the marimba's percussive doubling role; its long metal ring lets it sit under other instruments as a held colour, not only articulate a line. | inference |
| recording_behavior | As other mallet instruments, benefits from real distance for the resonators; the motor's mechanical noise, if present, is also part of a close recording that a distant one may mask. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | A held note can more legitimately extend toward a metal bar's real, longer decay than on marimba, but still should not exceed what the instrument's decay and the pedal state actually allow. | inference |
| overlap | Not a legato instrument in the melodic sense; the pedal, not note overlap, produces the impression of connection. | inference |
| velocity | Selects among recorded dynamic layers. | inference |
| continuous_dynamics | Where a sustained passage needs a shape, it comes from the pedal state and individual note velocities rather than a single continuous control standing in for a bowed-instrument-style swell. | inference |
| expression | Not the primary control for a single struck note. | inference |
| articulation_switching | Struck (pedal up), struck (pedal down, sustained), and dead stroke are separate recordings; motor on/off and speed is a further, separate axis. | sourced: BYU-VIBRAPHONE |
| round_robins | Essential for repeated notes, as with marimba. | inference |
| release_samples | The pedal's damper drop, and a hand-damped dead stroke, are both real, distinct release events a glued or pedal-ignorant part would lose. | inference |
| pedal_or_breath_behavior | The sustain pedal is a real, continuous damper control, not a binary switch in the way it is sometimes modelled; it should be represented as a curve (as the piano's is), with harmony cleared by lifting it, not left down indefinitely. | inference |
| transition_samples | Not applicable between discrete strikes; the pedal, not a transition sample, connects notes. | inference |
| mic_or_room_behavior | As other mallet instruments; distance serves the resonators. | inference |
| likely_fake_sounding_errors | The pedal held down implicitly forever with nothing ever dampened, producing a harmonic blur no player would allow; motor left on at one constant speed as a default sound rather than a chosen character; a roll at one unvarying velocity. | inference |
| organic_programming_methods | Model the pedal as a real, harmony-driven curve, cleared between chords; treat the motor's speed as a per-passage character choice, including off as the modern default; vary velocity across rolls and between hands. | inference |

### Xylophone

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Wooden (or synthetic) bars, narrower and denser than a marimba's, over resonator tubes on most orchestral-size instruments; undercut so that the bar's second partial sits close to three times the fundamental, roughly a twelfth above it, which is what gives the instrument its hard, clattering, powerfully piercing character rather than a rounder marimba-like tone. | sourced: RIMSKY-1913 + academic: WOODHOUSE-MARIMBA |
| attack_behavior | A hard mallet (rubber, nylon, or plastic) strike gives a sharp, bright attack that dominates the sound more than on a marimba. | sourced: BYU-XYLOPHONE |
| sustain_behavior | Very short; shorter than marimba because the bars are smaller and stiffer, and the attack transient is a larger fraction of what is heard. | inference |
| release_behavior | Decays almost immediately on its own; there is little to release. | inference |
| dynamic_timbre_change | Harder strikes bring proportionally more of the bright, high-partial "clatter" that defines the instrument. | inference |
| register_character | Hard, bright, and cutting; used for powerful, piercing effects rather than warmth. | sourced: RIMSKY-1913 |
| practical_range | **Written** roughly F3 to C7 across a standard 3.5-octave instrument; it **sounds one octave higher than written** (so a real sounding range of roughly F4 to C8). A prior version of this file gave the sounding range as the written range; the two must be stated separately. | sourced: BYU-XYLOPHONE; RONNEFARTH-PITCH-RANGE |
| tessitura | Most effective, and most idiomatic, across its full written range for cutting, percussive effects; it is not an instrument used for warm, sustained melody at any register. | inference |
| articulation_logic | Single strokes dominate; rolls exist but decay so fast that a slow roll is audible as separate strokes rather than a sustained tone. | inference |
| phrase_limits | As marimba: bounded by decay (there is effectively no sustain to extend) and by reach across the instrument. | inference |
| transitions | No legato; every note is a fresh, sharp strike. | inference |
| repeated_note_behavior | Real repeated notes vary contact and force; the instrument's exposed, clattering attack makes an identically repeated sample especially obvious. | inference |
| vibrato | None. | inference |
| pitch_instability | Essentially none. | inference |
| resonance | Resonator tubes, where fitted, reinforce the fundamental under the otherwise attack-dominated tone. | academic: WOODHOUSE-MARIMBA |
| physical_noise | Mallet click is a large fraction of the perceived sound at every dynamic. | inference |
| feasibility | Two hands, two (occasionally four) mallets, with the same general reach constraints as marimba, though four-mallet xylophone writing is less common in standard repertoire. | inference |
| ensemble_behavior | Used for brilliance, punctuation, and powerful doubling of a melodic line; its hard attack cuts through a full ensemble at any dynamic that reaches the bars at all. | sourced: RIMSKY-1913 |
| recording_behavior | As other mallet instruments, real distance lets the resonators (where fitted) speak; the attack, being so dominant, survives close-miking better than the marimba's rounder tone does. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Notes trigger a one-shot sample whose own very short decay carries the sound; held notes beyond that decay add nothing. | inference |
| overlap | Not applicable. | inference |
| velocity | Selects among recorded dynamic layers. | inference |
| continuous_dynamics | Not applicable to single struck notes given the near-absence of sustain. | inference |
| expression | Not applicable. | inference |
| articulation_switching | Mallet hardness variants, where offered, are separate recordings. | inference |
| round_robins | Essential and especially exposed, given how identical and attack-dominated repeated xylophone strikes sound without variation. | inference |
| release_samples | Minimal; the natural decay is already close to the release. | inference |
| pedal_or_breath_behavior | Not applicable. | inference |
| transition_samples | Not applicable. | inference |
| mic_or_room_behavior | Survives closer capture better than marimba or vibraphone, given the attack-dominant tone; still benefits from real distance where resonators are fitted. | inference |
| likely_fake_sounding_errors | The written/sounding octave confused, so a part reads or sounds an octave away from intended; identical repeated strikes with no round robin; a slow "roll" that is audibly just separated single strokes on an instrument whose actual roll needs real speed to fuse at all. | inference |
| organic_programming_methods | State written and sounding range separately when writing or checking a part; vary strike velocity and contact per note, especially in fast repeated passages where the attack-dominant tone exposes any repetition quickly. | sourced: BYU-XYLOPHONE; RONNEFARTH-PITCH-RANGE |

### Glockenspiel

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Small steel bars, usually without resonator tubes, giving a bright, penetrating, bell-like tone. | sourced: RIMSKY-1913; BYU-GLOCKENSPIEL |
| attack_behavior | Struck with hard mallets (very hard rubber, plastic, or brass), which give a wide range of timbre and articulation from bright to extremely cutting. | sourced: BYU-GLOCKENSPIEL |
| sustain_behavior | Rings after the strike, more than a xylophone's wooden bar but still relatively briefly compared with vibraphone's metal-over-resonator ring. | inference |
| release_behavior | Decays on its own; not typically damped by hand in normal use. | inference |
| dynamic_timbre_change | Harder mallets and harder strikes both push toward a more piercing, cutting sound; the instrument's whole identity leans bright rather than warm at any dynamic. | sourced: BYU-GLOCKENSPIEL |
| register_character | Functions as brilliance and punctuation at the very top of the orchestral range rather than as a melodic voice in its own comfortable register, precisely because it sounds so much higher than it is written. | inference |
| practical_range | **Written** roughly in a comfortable treble-staff register, commonly cited as about F3 to F6 on a 2.5-to-3-octave instrument; it **sounds two octaves higher than written** (so a real sounding range of roughly F5 to F8). A prior version of this file gave the sounding range as the written range, with an additional error of one octave beyond that. | sourced: BYU-GLOCKENSPIEL; RONNEFARTH-PITCH-RANGE |
| tessitura | The whole instrument functions as an extreme-register colour; there is no "comfortable middle" the way a marimba has one, because every written note already sounds near the top of the audible musical range. | inference |
| articulation_logic | Single strokes are the primary vocabulary; rolls exist but, as with xylophone, need real speed to read as sustained rather than as separated strokes. | inference |
| phrase_limits | As xylophone: bounded by decay and by reach; the instrument is small enough that reach is rarely a practical limit. | inference |
| transitions | No legato. | inference |
| repeated_note_behavior | Real repeated notes vary contact and force. | inference |
| vibrato | None. | inference |
| pitch_instability | Essentially none. | inference |
| resonance | Minimal beyond the bar's own ring; most glockenspiels have no resonator tubes. | sourced: BYU-GLOCKENSPIEL |
| physical_noise | Mallet click, proportionally significant given the instrument's small size and bright tone. | inference |
| feasibility | Two hands, two mallets typically (four-mallet glockenspiel writing is rare). | inference |
| ensemble_behavior | Doubles a melody two octaves above its written pitch as a brilliance effect; the celesta is the substitute Rimsky-Korsakov names when a glockenspiel is unavailable and a keyboard-percussion colour is wanted, not the reverse. | sourced: RIMSKY-1913 |
| recording_behavior | Small and bright; survives closer capture reasonably well, though hall placement still matters in a full orchestral recording for blend. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | One-shot samples with a short natural decay; held notes add nothing beyond it. | inference |
| overlap | Not applicable. | inference |
| velocity | Selects among recorded dynamic layers. | inference |
| continuous_dynamics | Not applicable to single struck notes. | inference |
| expression | Not applicable. | inference |
| articulation_switching | Mallet-hardness variants (rubber, plastic, brass), where offered, are separate recordings. | sourced: BYU-GLOCKENSPIEL |
| round_robins | Essential and exposed, as with xylophone. | inference |
| release_samples | Minimal. | inference |
| pedal_or_breath_behavior | Not applicable. | inference |
| transition_samples | Not applicable. | inference |
| mic_or_room_behavior | Survives closer capture; still benefits from ensemble blend distance in a full mix. | inference |
| likely_fake_sounding_errors | **The two-octave transposition ignored**, so a written part is checked or played back as if it sounded where it looks on the staff, landing the instrument an octave (or, if the xylophone's single-octave rule is mistakenly applied instead, still an octave) away from its real, very high sounding register; identical repeated strikes with no round robin. | sourced: BYU-GLOCKENSPIEL; RONNEFARTH-PITCH-RANGE |
| organic_programming_methods | Always state and check written versus sounding range explicitly before voicing a passage against other instruments; vary strike velocity and mallet contact per note. | sourced: BYU-GLOCKENSPIEL; RONNEFARTH-PITCH-RANGE |

### Tubular Bells and Crotales

Two further tuned mallet instruments, covered more briefly. Tubular bells (chimes) are a set of
vertically hung metal tubes struck near the top with a mallet or a rawhide-faced hammer. Crotales are
small, thick bronze discs, tuned precisely and played in chromatic sets, closer in construction to a
miniature clash cymbal than to a bar instrument.

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Tubular bells: vertically suspended metal tubes, struck near the top. Crotales: small, thick, precisely tuned bronze discs, played singly with a hard mallet or, historically, clashed in pairs like tiny cymbals. | inference |
| attack_behavior | Tubular bells: a firm mallet or hammer strike near the top of the tube; the exact strike point affects the balance of overtones. Crotales: a precise, bright, immediate metallic attack. | inference |
| sustain_behavior | Both ring considerably longer than a wooden bar; tubular bells especially are associated with long, cathedral-bell-like decay. | inference |
| release_behavior | Decays on its own unless damped by hand. | inference |
| dynamic_timbre_change | Harder strikes bring more high-partial "clang" content on both instruments, proportionally more on crotales given their smaller mass. | inference |
| register_character | Tubular bells: a solemn, bell-like colour, historically used to imitate church or clock bells. Crotales: a very bright, bell-like shimmer at the top of the audible range. | inference |
| practical_range | Tubular bells: sounding roughly C5 to F6 on a common 1.5-octave instrument, up to about F4 to G6 on a larger set; treated as non-transposing (sounds where written) in the source consulted, though this was not stated with full confidence. Crotales: sounding roughly C6 to F8; **written two octaves lower than sounding**, in the treble clef, the same direction of transposition as the glockenspiel. | sourced: RONNEFARTH-PITCH-RANGE |
| tessitura | Tubular bells sit in a comfortable mid-to-upper register that reads as genuinely bell-like; crotales function entirely as an extreme-top-register shimmer, similarly to glockenspiel. | inference |
| articulation_logic | Single strokes dominate both; a roll (tremolo, alternating mallets or discs) is possible on either but is a secondary technique. | inference |
| phrase_limits | Bounded by decay (long on both, so notes overlap and ring together more readily than on wooden-bar instruments) and by reach. | inference |
| transitions | No legato. | inference |
| repeated_note_behavior | Real repeated notes vary contact and force. | inference |
| vibrato | None. | inference |
| pitch_instability | Essentially none on either. | inference |
| resonance | Both ring long enough that overlapping harmony (several tubes or discs sounding together) is a real, audible effect, not a flaw. | inference |
| physical_noise | Mallet or hammer contact noise, proportionally minor given the long ring on both instruments. | inference |
| feasibility | Two hands, one mallet each typically; a fast passage across widely spaced tubular bells is limited by reach and travel time, as with any spread bar or tube instrument. | inference |
| ensemble_behavior | Tubular bells are used for solemn or ceremonial colour, sparingly, similarly to how the tam-tam is used in `PERCUSSION.md`; crotales double or extend a melodic line at the very top of the texture, similarly to glockenspiel. | inference |
| recording_behavior | Both benefit from real distance and hall tail, given how long they ring; close-miking foreshortens the decay a listener would otherwise hear resolve naturally. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Long natural decay on both; a held note is closer to legitimate here than on the wooden-bar instruments, but should still not exceed the real decay. | inference |
| overlap | Not a legato instrument in the melodic sense, though overlapping ring between notes is real and desirable. | inference |
| velocity | Selects among recorded dynamic layers. | inference |
| continuous_dynamics | Not applicable to single struck notes. | inference |
| expression | Not applicable. | inference |
| articulation_switching | Where alternate mallets/hammers are offered, they are separate recordings. | inference |
| round_robins | Useful; less critical than on the driest instruments on this page given the long ring, which itself varies each performance. | inference |
| release_samples | The long decay tail is close to the entire character; truncating it is a clear error on either instrument. | inference |
| pedal_or_breath_behavior | Some tubular-bell sets include a damper pedal; where modelled, it should behave as a real damper state, not a reverb send. | inference |
| transition_samples | Not applicable between discrete strikes. | inference |
| mic_or_room_behavior | Distance and hall tail matter more here than for almost any other instrument on this page. | inference |
| likely_fake_sounding_errors | Crotales' two-octave transposition ignored, the same error as the glockenspiel's; tubular bells cut off before their long natural decay resolves; either instrument used so frequently that its (intentionally sparing, ceremonial) effect is dulled. | sourced: RONNEFARTH-PITCH-RANGE |
| organic_programming_methods | Check crotales' written-versus-sounding range explicitly, as with glockenspiel; let both instruments ring their full natural decay; use tubular bells sparingly for its ceremonial effect, consistent with how the tam-tam is treated in `PERCUSSION.md`. | sourced: RONNEFARTH-PITCH-RANGE |

---

## What the instrument is

A row of tuned bars, tubes, or discs struck with mallets, most with tuned resonator tubes
underneath where the physical size allows one. Wooden bars (marimba, xylophone) give a warm-to-hard
tone that decays quickly; metal bars, tubes, and discs (vibraphone, glockenspiel, tubular bells,
crotales) ring for much longer. That one material difference decides how each instrument is written
far more than any other single fact on this page. [inference]

## Range and register

```text
Marimba          C2-C7 (large instrument), sounds as written                    sourced: BYU-MARIMBA
Vibraphone        typically 3 octaves (commonly ~F3-F6), sounds as written,      sourced: BYU-VIBRAPHONE;
                  up to 4 octaves (~C3-C7) on larger instruments                  RONNEFARTH-PITCH-RANGE
Xylophone         written ~F3-C7, sounds one octave higher (~F4-C8)             sourced: BYU-XYLOPHONE;
                                                                                   RONNEFARTH-PITCH-RANGE
Glockenspiel      written ~F3-F6, sounds two octaves higher (~F5-F8)            sourced: BYU-GLOCKENSPIEL;
                                                                                   RONNEFARTH-PITCH-RANGE
Tubular bells     ~C5-F6 (common), up to ~F4-G6 (larger sets)                    sourced: RONNEFARTH-PITCH-RANGE
Crotales          written two octaves below sounding; sounds ~C6-F8             sourced: RONNEFARTH-PITCH-RANGE
```

**A prior version of this file gave the xylophone's and glockenspiel's *sounding* ranges labelled as
their *written* ranges.** The correction above states both explicitly and in the direction the
sources give them: the xylophone is written a single octave below where it sounds, and the
glockenspiel is written two octaves below where it sounds. Exact octave boundaries vary a little by
instrument size across the sources consulted (a 2.5-octave glockenspiel and a 3-octave one do not
start and end on quite the same notes), so the figures above are typical ranges, not a fixed
specification.

The glockenspiel's transposition matters in practice: written in a comfortable staff register, it
sounds at the very top of the audible orchestral range, where it functions as brilliance and
punctuation rather than melody. Crotales work the same way, two octaves rather than one.
[sourced: BYU-GLOCKENSPIEL; RONNEFARTH-PITCH-RANGE]

**Marimba** has a rich fundamental and a short sustain, strongest in its low and middle register and
thinner at the top. **Vibraphone** rings long, and its low register is the warmest part of it.
[inference]

## Articulation and note transitions

There is no true legato: each note is a strike and a decay. Connection is produced two ways:

```text
rolls          rapid alternation on one bar, or between the notes of a chord, to sustain a pitch
pedal          on the vibraphone only; a damper bar lifted so the bars ring freely
```

**Marimba rolls are how the instrument sustains.** A held marimba note written as a long note is a
strike followed by silence, because the bar decays in roughly a second or two. A sustained marimba
line is written as a roll, and in a sampled instrument that means either a roll articulation or
genuinely repeated notes at a plausible rate. [inference]

Bar tuning is the physical reason a struck bar reads as a clear pitch rather than a clang, and it is
also what separates the marimba's and xylophone's characters from each other. An ideal uniform beam's
first two natural frequencies fall in a ratio of about 2.76 to 1, which sounds unmusical; instrument
makers undercut the underside of each bar (removing wood to vary its thickness along its length)
specifically to pull that ratio toward a small integer. Measured xylophone bars land close to a ratio
of 3 (the second partial near a twelfth above the fundamental), and marimba bars are tuned further,
closer to a ratio of 4 (the second partial near two octaves above the fundamental) — **not the other
way around, and not "an octave" for either as a flat description.** A resonator tube is then tuned
under each bar to reinforce the fundamental specifically, which is part of why the higher partials
recede into a characteristic timbre rather than being amplified along with the fundamental.
[academic: WOODHOUSE-MARIMBA]

Other articulations:

```text
mallet hardness   soft yarn, medium, hard rubber, brass; a separate sample set, not an EQ
dead stroke       the mallet held against the bar after striking; a dry pitched thud, vibraphone above all
hand dampening    a finger pressed on a ringing bar to stop it, while the mallets continue elsewhere
```

[sourced: BYU-MARIMBA; BYU-VIBRAPHONE]

## Physical constraints

- Two hands, and two or four mallets. **Two mallets means two notes; four mallets means up to four.**
  Four-mallet chords are limited by arm and hand reach: the two mallets held in one hand typically
  span anywhere from a 2nd up to an octave comfortably, with some players able to reach a 9th or a
  10th using a wide-spread grip (most often the Stevens grip on marimba), but this is a genuinely
  difficult, not a routine, interval — **not "an octave and a half," which a prior version of this
  file gave as the comfortable maximum.** [sourced: UH-FOUR-MALLET]
- A leap across the instrument takes time, and so does a change of mallet interval.
- Hand dampening uses a hand, so it cannot happen while both hands are playing elsewhere.
- Mallet changes take time and are made between phrases. [inference]

## Phrase behaviour

A phrase is bounded by decay and by reach. On marimba (and xylophone, glockenspiel) the natural
gesture is continuous motion, because stopping means silence. On vibraphone the natural gesture is
the opposite: notes accumulate under the pedal and have to be cleared, so **pedalling and dampening
are the phrasing**, exactly as on a piano but with a longer decay and an audible motor. [inference]

## The vibraphone motor

Discs inside the resonator tubes rotate, opening and closing them, which produces a **tremolo, an
amplitude modulation, at a selectable speed**. It is not vibrato and it does not change pitch. The
motor can be off, and it usually is in modern playing; when it is on, the speed is a character choice
set for a passage rather than per note. A vibraphone patch with the motor always on at one speed is a
sound, not an instrument. [sourced: BYU-VIBRAPHONE]

## Ensemble behaviour

Mallet instruments cut through by attack rather than by level, so they double melodic lines
effectively at low dynamic. The glockenspiel doubles a melody two octaves up as brilliance; crotales
do the same at their own registered transposition. Marimba doubling a bass line adds attack without
adding weight. Tubular bells, like the tam-tam in `PERCUSSION.md`, are a sparing, ceremonial effect
rather than a continuous texture instrument. [sourced: RIMSKY-1913 + inference]

## Recording behaviour

These are large instruments (marimba and vibraphone above all) recorded from a distance that lets the
resonators speak. Close-miking a marimba emphasises the mallet click and loses the tube resonance.
Orchestral libraries place them at the back of the hall, distant and reverberant. Glockenspiel and
crotales, being small and bright, survive closer capture better than the resonator-dependent
instruments do. [inference]

## Programming it: the control model

Product specifics belong in the calibration profile.

```yaml
velocity: level and mallet attack hardness within one sample set; often selects the sample
mallet_sets: separate patches or keyswitches; chosen before writing
round_robins: essential, because repeated single-bar notes are exposed
rolls: either a recorded roll articulation, or written repeated notes at a plausible rate
pedal: vibraphone only; a damper state, not a reverb
motor: a speed parameter, and off is a valid setting
dead_stroke: a separate recording
release_samples: the bar or tube stopping is audible on a damped note
written_vs_sounding: xylophone one octave, glockenspiel and crotales two octaves; state which a
  range is whenever it is given
```

[inference]

## Programming it: what makes it sound real

- Choose the mallet set first. It changes the instrument more than the velocity does. [sourced: BYU-MARIMBA]
- Sustain marimba with rolls, not with long notes. [inference]
- Pedal the vibraphone by harmony, and clear it. Dampen notes that should stop. [inference]
- Keep four-mallet chords inside documented reach (a 2nd to an octave comfortably, a 9th or 10th as a
  genuine stretch), and voice them so the outer mallets carry the outer notes. [sourced: UH-FOUR-MALLET]
- Vary velocity between the two hands, and between roll strokes. A roll at one velocity is error 1.
  [inference]
- State written and sounding range explicitly for xylophone, glockenspiel, and crotales before
  voicing against other instruments. [sourced: BYU-XYLOPHONE; BYU-GLOCKENSPIEL; RONNEFARTH-PITCH-RANGE]
- Decide the vibraphone's motor speed per passage, or leave it off. [sourced: BYU-VIBRAPHONE]
- Use tubular bells sparingly, for their ceremonial effect, not as a continuous texture. [inference]

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Mallet-specific tells:

- long held marimba (or xylophone) notes, which the instrument cannot produce; [inference]
- rolls written as identical repeated samples at one velocity; [inference]
- four-mallet chords spanning more than a genuine reach, error 6, and specifically more than the
  documented 2nd-to-tenth range rather than the wider span a prior version of this page implied;
  [sourced: UH-FOUR-MALLET]
- vibraphone written with the pedal implicitly down forever and nothing dampened; [inference]
- motor always on, at one speed, as a substitute for expression; [sourced: BYU-VIBRAPHONE]
- xylophone or glockenspiel parts voiced as if written pitch were sounding pitch, landing them an
  octave, or two octaves, away from where they actually sit, error 4; [sourced: BYU-XYLOPHONE; BYU-GLOCKENSPIEL; RONNEFARTH-PITCH-RANGE]
- mallet hardness faked with a filter. [inference]

## What the Performance Director needs from this file

- `impossible_voicings`: more than four simultaneous notes, or a four-mallet chord beyond a genuine
  reach (a 2nd to an octave comfortably; a 9th or 10th only as a deliberate stretch).
- `simultaneity_exceeded`: two mallets means two notes; state which setup the part assumes.
- `limb_or_finger_conflicts`: hand dampening competes with playing.
- `articulation_unavailable`: roll, dead stroke, and mallet hardness are separate recordings.
- Sustain feasibility on marimba (and xylophone): a long note is a flag, and the fix is a roll, not a
  longer sample.
- Vibraphone pedal state should be in the plan, as the piano's is.
- `out_of_range`: check every xylophone, glockenspiel, and crotales note against its *sounding*
  range, not its written range, when voicing against other instruments.

## Sources and what to verify

- [inference] and [inference] claims above rest on: one acoustics textbook's pages on marimba and
  xylophone bar tuning (read at section depth), four university percussion-studio pages (marimba,
  vibraphone, xylophone, glockenspiel, read at section depth), one pitch-and-notation reference page
  (read at section depth, giving written/sounding ranges for xylophone, glockenspiel, vibraphone,
  marimba, crotales, and tubular bells), one university four-mallet-grip page (read at section
  depth), and Rimsky-Korsakov's *Principles of Orchestration* (read at section depth for register
  colour and ensemble use). Full citations in `research/sources/INSTRUMENT_SOURCES.md`.
- **To verify**: bar decay times by material and register, in Fletcher and Rossing, *The Physics of
  Musical Instruments*. [inference], not opened this pass.
- **To verify**: exact resonator-tube tuning beyond "reinforces the fundamental" (for instance, how
  far a tube's own resonance can be detuned from the bar before the effect weakens). Not opened this
  pass.
- **Not available**: typical roll rates in strokes per second by instrument and dynamic. These remain
  practitioner judgements until calibrated, as in the prior version of this file.
- **Not available**: a dedicated, section-depth-read source for tubular bells' and crotales'
  attack/sustain/release behaviour beyond their pitch ranges; those cards are the thinnest sourced on
  this page and are labelled [inference] accordingly rather than upgraded.
