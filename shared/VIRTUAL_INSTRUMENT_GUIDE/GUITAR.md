# Guitar

Six-string steel-string acoustic, nylon-string classical, and electric guitar, standard and common
alternate tunings. Twelve-string, resonator and pedal-steel variants are not covered. Bass guitar and
double bass are in `BASS.md`.

> Evidence: thirteen sources read at section depth for this pass: six academic acoustics/music-
> computing papers (strum microtiming, tremolo regularity, plucking-point physics, pickup acoustics,
> fret-pressure intonation, distortion intermodulation), one academic dissertation on distorted-chord
> acoustics, two public-domain orchestration treatises, one public-domain classical method, two
> university acoustics-group pages, and two performer-pedagogy pages. **A measured strum spread was
> found and is used below** [academic: FREIRE-STRUM-2018], replacing the 2.0 page's "no source
> available" note. Source IDs resolve in `research/sources/INSTRUMENT_SOURCES.md`; the claims and
> their limits are recorded in `research/instruments/GUITAR.md`.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## Behaviour cards

### Steel-String Acoustic

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Steel strings driven by a plectrum or fingers, coupled through the bridge to a spruce or cedar top plate that radiates the sound; the body does not add energy, it converts string vibration into a larger, more efficient radiating surface | academic: UNSW-GUITAR-INTRO |
| attack_behavior | A sharp transient set by plucking speed, plectrum hardness or fingernail versus flesh, and plucking point; the string's higher harmonics are suppressed near their own nodes, so where the string is plucked shapes the attack's brightness as much as how hard it is plucked | academic: TRAUBE-2000 |
| sustain_behavior | Decays from the moment of pluck; there is no true sustain without re-attack, tremolo picking or a resonance trick (open strings, harmonics). Decay rate is fastest in the highest register and on the wound bass strings' higher harmonics | inference |
| release_behavior | The fretting hand controls the ending: releasing pressure on a fretted string (without leaving it) stops the note; lightening pressure without releasing produces a damped "buffed" tone that still speaks briefly. Right-hand palm muting near the bridge is a separate, steel-string/electric picking-hand technique that shortens and thickens the note instead of silencing it | sourced: SOR-METHOD |
| dynamic_timbre_change | Louder is not simply "more of the same" sound: plucking harder increases high-harmonic content as well as level, and moving the plucking point toward the bridge (sul ponticello) brightens and thins the tone while moving it toward the fingerboard (sul tasto) mellows and rounds it, independent of loudness | academic: TRAUBE-2000 |
| register_character | Below the fifth fret, thick and resonant, and open-position voicings exploit ringing open strings; above the twelfth fret, thin, quiet and short-sustaining, used melodically rather than harmonically | inference |
| practical_range | written and sounding are the same letter names but the guitar sounds one octave below what is written; standard tuning's open strings are E2 A2 D3 G3 B3 E4, and a modern 19-24 fret fingerboard reaches into the B5-D6 region above the twelfth-fret octave | sourced: BERLIOZ-1855 + inference |
| tessitura | Most idiomatic and resonant between the open strings and about the ninth fret; the top three or four frets on the highest string are reachable but thin and rarely load-bearing | inference |
| articulation_logic | Picked (plectrum or fingerstyle), hammer-on, pull-off, slide, natural and artificial harmonics, palm mute, dead/muted stroke, and the strum as a distinct multi-string gesture rather than a single articulation | inference |
| phrase_limits | Bounded by hand position on the neck; a position shift is audible as a slide or a small gap. No breath limit, but a note or chord decays, so a "held" phrase longer than the natural decay needs re-attack or a different device | inference |
| transitions | Hammer-ons and pull-offs are the instrument's real legato: the string is not re-struck, so the resulting note is quieter than a picked note before it. Slides carry pitch continuously between two fretted notes on one string | inference |
| repeated_note_behavior | A picked repeated note decays and re-attacks each time; tremolo picking (rapid alternation, single string) is regular in overall timing among skilled players but the individual note durations and loudness are not perfectly uniform even then | academic: FREIRE-TREMOLO-2013 |
| vibrato | Produced by the fretting hand rocking or bending the string after the attack, not from the pluck itself; absent on open strings unless the hand rocks the whole neck (rare) or a vibrato arm is used (electric only) | inference |
| pitch_instability | Fretting pressure stretches the string and sharpens its pitch above the theoretical fretted value; standard saddle compensation corrects most of this, but a hard press (heavy barre, held bend) sharpens further, unevenly across strings | academic: VARIESCHI-2009 |
| resonance | Open strings vibrate sympathetically with a played string's matching harmonics, coupled through the bridge and body rather than the air; most steel-string bodies show three strong resonances clustered near 100-200 Hz from top/back coupling and the soundhole's Helmholtz mode, plus weaker higher top-plate modes that colour but do not dominate | academic: UNSW-GUITAR-INTRO; UNSW-GUITAR-MODES |
| physical_noise | Fret buzz and squeak on position shifts, pick or nail attack noise, string-on-fret noise during bends and slides; captured up close and normally left audible | inference |
| feasibility | Six notes maximum (one per string, no unisons on one string); movable barre shapes reproduce open-position six- and five-note voicings at any fret, so dense movable voicings are not restricted to four notes the way a non-barred movable shape is | sourced: FORSYTH-1914 + inference |
| ensemble_behavior | Two guitars in the same register and voicing mask each other; the usual fix is different neck positions for the same chord, giving different string assignment and timbre, or a register split with the bass | inference |
| recording_behavior | Microphone position along the body changes the balance; near the soundhole is boomy, further out and toward the twelfth fret is more even. This is a property of the recording, not the instrument | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Notes decay naturally; holding a MIDI note past its natural decay does not sustain it on a sample-based patch unless the patch loops, which reads as fake for a plucked instrument | inference |
| overlap | Legato transitions (hammer-on/pull-off/slide patches) are usually monophonic per string and need note overlap to trigger; picked notes do not need overlap and should not be glued | inference |
| velocity | Selects level and, in most libraries, pick/finger strength and sample choice; it is not a stand-in for plucking-point brightness, which some libraries expose as a separate control or articulation | inference |
| continuous_dynamics | Guitar has no true held-note crossfade the way a bowed or blown instrument does, because notes decay; "dynamics" mostly means per-note velocity plus plucking-position/articulation choice, not a CC swell on a long note | inference |
| expression | Where a library exposes a separate expression/trim lane, it is a level trim, not a timbre control; timbre changes come from articulation and, where modelled, plucking-position choice | inference |
| articulation_switching | Usually keyswitches; keyswitch notes are non-sounding and must not be audible in the render | inference |
| round_robins | Needed for any repeated note or tremolo passage; see `COMMON_ERRORS.md` item 1 | inference |
| release_samples | Fret-release and string-damping noise; lost when notes are glued end to end, which removes the fretting-hand release character described above | inference |
| pedal_or_breath_behavior | Not applicable: the acoustic guitar has no pedal or breath control | inference |
| transition_samples | Recorded slides, hammer-ons and pull-offs in some libraries, versus pitch-bend simulation in others; a whole-step fretted bend is not the same gesture as a smooth pitch-bend glide and should not be substituted silently | inference |
| mic_or_room_behavior | Mic position along the body is a recorded or modelled choice; a position near the soundhole is boomy by construction, not because the guitar is boomy | inference |
| likely_fake_sounding_errors | Uniform strum spread and direction every time; picked-note velocity applied to hammer-ons/pull-offs; sustained block chords with no decay; six-note voicings the fretting hand cannot reach; no fret or pick noise anywhere | inference |
| organic_programming_methods | Spread every strum by direction (low-to-high on a downstroke) using the measured ranges in GTR-01, quieten hammer-ons and pull-offs below the picked note before them, vary plucking-position brightness across a phrase rather than only velocity, and let fretting-hand release stop or damp notes instead of gluing note-off to the next note-on | sourced: SOR-METHOD + academic: FREIRE-STRUM-2018 |

### Nylon-String Classical

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Nylon (historically gut) strings, plucked by the fingertips and nails, over a wider, flatter fretboard than steel-string designs; body construction is broadly similar in principle to the steel-string (top plate as radiator) but lighter-built for the lower string tension | inference |
| attack_behavior | Two structurally different strokes: rest stroke (apoyando), where the finger follows through to rest on the next string, giving a louder, clearer, more projecting attack; and free stroke (tirando), where the finger clears the strings, giving a tone shaped by the player's chosen hand and wrist angle rather than by follow-through | sourced: RESTSTROKE-PEDAGOGY |
| sustain_behavior | As steel-string: decays from the pluck; nylon's lower tension and different core material give a longer, softer decay in the mid-to-low register than a comparable steel string | inference |
| release_behavior | Same fretting-hand mechanism as steel-string: release pressure (without leaving the string) to stop cleanly, or lighten pressure to damp while it briefly continues; picking-hand palm muting is not part of standard classical technique | sourced: SOR-METHOD |
| dynamic_timbre_change | Rest stroke versus free stroke is itself a dynamic-and-timbre choice, not only a loudness one; nail versus flesh contact and plucking distance from the bridge (ponticello/tasto) both shift brightness independent of loudness, as on steel-string | sourced: RESTSTROKE-PEDAGOGY + academic: TRAUBE-2000 |
| register_character | As steel-string: thick and resonant below the fifth fret, thin and quiet above the twelfth; nylon's lower string tension makes the open strings ring longer and louder relative to fretted notes than on steel-string | inference |
| practical_range | Same open tuning and written-octave convention as steel-string (E2 A2 D3 G3 B3 E4, written up an octave); classical instruments typically have 19 frets, so the practical ceiling sits lower than an extended steel-string or electric fingerboard, closer to the historical three-octaves-and-a-fifth figure | sourced: BERLIOZ-1855 |
| tessitura | Most resonant and idiomatic in open position and up to about the seventh fret, where open strings can ring under fretted notes; classical repertoire uses higher positions for colour and melody, not as the main register | inference |
| articulation_logic | Rest stroke, free stroke, hammer-on, pull-off, slide, natural and artificial harmonics, damped ("buffed"/etouffe) notes, rasgueado (percussive multi-finger strum), and tremolo (rapid repeated note, typically thumb plus three fingers in rotation) | sourced: RESTSTROKE-PEDAGOGY; NIEDT-RASGUEADO + academic: FREIRE-TREMOLO-2013 |
| phrase_limits | As steel-string, bounded by hand position; classical phrasing additionally treats rest-stroke melody lines and free-stroke arpeggio accompaniment as separate textural layers that can phrase independently within one hand | inference |
| transitions | Hammer-ons and pull-offs as steel-string (quieter than a plucked note); slides (glissando) audible between fretted positions; rest-to-free-stroke changes are a technique choice within a phrase, not usually audible as a "transition" event | inference |
| repeated_note_behavior | Tremolo (thumb plus ring-middle-index, or similar rotation, repeating one note rapidly) is regular in overall timing among skilled players, but note duration and loudness are not perfectly uniform even for trained players; this is the technique's natural character, not a defect to smooth away | academic: FREIRE-TREMOLO-2013 |
| vibrato | Fretting-hand vibrato as steel-string; classical technique also uses a lateral (side-to-side) vibrato distinct from the bend-style vibrato common on steel-string and electric | inference |
| pitch_instability | Same fret-pressure sharpening mechanism as steel-string; nylon-specific magnitude was not measured in any source opened | academic: VARIESCHI-2009 + to-verify: what would settle this is not recorded |
| resonance | As steel-string, sympathetic vibration of open strings; nylon's lower tension and longer sustain make this more audible in normal play, which is part of why classical writing leaves open strings ringing under fretted lines deliberately | academic: UNSW-GUITAR-INTRO + inference |
| physical_noise | Nail noise on attack (more prominent than steel-string pick attack), fret buzz on position shifts, and the mechanical click/scrape of rasgueado's fingernail-back contact | sourced: NIEDT-RASGUEADO |
| feasibility | Same six-note/one-per-string ceiling as steel-string; classical voicings favour open strings more heavily, so movable barre chords are comparatively less central to the repertoire than on steel-string rhythm guitar | inference |
| ensemble_behavior | As steel-string: two classical guitars in the same register and voicing mask each other and are usually separated by neck position or register split | inference |
| recording_behavior | Recorded at a greater distance than typical steel-string close-miking, to let the (typically quieter, more delicately voiced) instrument's body and room blend rather than emphasising nail/finger noise | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | As steel-string: notes decay naturally; sustaining past natural decay without a loop reads as fake | inference |
| overlap | As steel-string: legato transition patches need overlap; picked/plucked notes should not be glued | inference |
| velocity | Selects level and, in libraries that model it, rest-stroke-versus-free-stroke or nail-versus-flesh sample selection; treating velocity as a pure loudness knob loses the technique distinction | inference |
| continuous_dynamics | As steel-string: no true held-note swell; per-note articulation and plucking choice carry expression instead of a CC lane | inference |
| expression | As steel-string: a level trim where present, not a timbre control | inference |
| articulation_switching | Keyswitches for rest/free stroke, rasgueado, tremolo, and harmonics where modelled separately; non-sounding keyswitch notes must stay inaudible | inference |
| round_robins | Especially important for tremolo and rasgueado, where the same pitch repeats rapidly and machine-gunning is most audible | academic: FREIRE-TREMOLO-2013 + inference |
| release_samples | Fret-release and damping noise; rasgueado's percussive attack also has a distinct decay character that a glued-note patch loses | inference |
| pedal_or_breath_behavior | Not applicable: the classical guitar has no pedal or breath control | inference |
| transition_samples | Recorded slides and hammer-on/pull-off transitions where modelled; rasgueado is normally a distinct recorded articulation, not a fast strum patch | sourced: NIEDT-RASGUEADO |
| mic_or_room_behavior | Classical libraries are typically captured at a more reverberant distance than steel-string libraries by convention; this is a product fact for the calibration profile, not a guide fact | inference |
| likely_fake_sounding_errors | Rest-stroke and free-stroke used interchangeably with no tonal difference programmed; rasgueado played as a fast simple strum; tremolo at one uniform velocity and duration; sustained chords with no natural decay | inference |
| organic_programming_methods | Alternate rest and free stroke by the same logic a player would (melody notes rest-stroke, arpeggio notes free-stroke); give tremolo passages small, named timing and dynamic variation per GTR-02 rather than a flat randomisation; build rasgueado as a fast finger sequence with separated onsets, not a single spread strum | sourced: NIEDT-RASGUEADO + academic: FREIRE-TREMOLO-2013 |

### Electric Guitar

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Steel strings sensed by one or more fixed-position magnetic pickups, which measure string velocity near that point rather than the whole string; the amplifier and speaker are part of the sound-producing chain, not an add-on effect | academic: PAIVA-PICKUPS-2012 |
| attack_behavior | As steel-string acoustic for the string mechanics, but the pickup's fixed sensing point and any downstream gain stage reshape the attack transient; a hard-clipped/distorted signal compresses and lengthens the perceived attack and decay compared to a clean signal | academic: LILJA-2009 |
| sustain_behavior | Materially longer than an unamplified guitar: high gain and proximity to the amplifier/speaker can create sustained or infinite sustain through acoustic feedback, a genuinely different sustain mechanism from the string's natural decay | inference |
| release_behavior | Same fretting-hand release/damping mechanism as acoustic guitar; palm muting (picking-hand edge damping near the bridge) is characteristic electric/steel-string technique and, combined with gain, produces the short, percussive "chugging" articulation common in distorted rhythm playing | sourced: SOR-METHOD + inference |
| dynamic_timbre_change | Distortion/gain is itself a dynamic-to-timbre control: increasing gain (or increasing pick attack into a fixed gain stage) increases harmonic and intermodulation content non-linearly, not just loudness; this makes "how hard the amp is driven" as much a phrasing decision as velocity is on an acoustic instrument | academic: LILJA-2009 |
| register_character | As acoustic guitar for fretboard geography; pickup selection changes which register/timbre is emphasised independent of fret position | academic: PAIVA-PICKUPS-2012 |
| practical_range | Same tuning and octave-transposition convention as acoustic guitar; most electrics have 21-24 frets, reaching further above the twelfth-fret octave than a classical instrument, into roughly the B5-D6 region | sourced: BERLIOZ-1855 + inference |
| tessitura | Most idiomatic register depends heavily on pickup and gain choice: bridge pickup and higher gain favour upper-register lead lines that cut through a mix; neck pickup and lower gain favour full, round rhythm and low-register work | academic: PAIVA-PICKUPS-2012 |
| articulation_logic | All acoustic articulations (picked, hammer-on, pull-off, slide, harmonics, palm mute, dead note) plus vibrato-arm pitch effects and controlled feedback, which have no unplugged equivalent | inference |
| phrase_limits | As acoustic for hand position; gain and sustain can extend an apparent "held" phrase well past the string's natural decay, so the acoustic decay limit does not apply the same way under high gain | inference |
| transitions | Hammer-ons and pull-offs as acoustic (quieter than picked); the vibrato arm additionally allows a smooth, continuous pitch glide with no discrete fret events, mechanically unlike a fretted bend | inference |
| repeated_note_behavior | Picked repeated notes and tremolo picking as acoustic; under distortion, a rapid repeated note also re-triggers the transient compression/sustain behaviour of the gain stage each time, which is audibly different from a clean repeated note | inference |
| vibrato | Fretting-hand vibrato as acoustic, plus vibrato-arm (whammy bar) vibrato, which varies string tension/length mechanically and also shifts the string's position relative to the pickup's magnetic field, adding a secondary timbral flutter beyond pitch | inference |
| pitch_instability | Fret-pressure sharpening as acoustic; a vibrato arm or a bend adds large, deliberate pitch instability as an expressive device rather than an error; bend intonation depends on ear and finger strength, and an underbent target is a common and audible fault | academic: VARIESCHI-2009 + inference |
| resonance | Body resonance is less perceptually central than on an acoustic (the amplified/pickup signal dominates), but sympathetic string vibration still occurs and can be audible, especially at high gain and sustain | academic: UNSW-GUITAR-INTRO + inference |
| physical_noise | Fret buzz, pick attack, string noise on bends/slides as acoustic; additionally, pickup and cable noise, and controlled feedback, which is not noise in the pejorative sense but a usable, deliberately courted sound | inference |
| feasibility | Same six-note/one-per-string and barre-shape rules as acoustic; heavily distorted rich voicings (thirds and beyond) are not physically infeasible but read as arranged for a clean instrument, because the combination-tone complexity they generate under gain is not what the style expects | academic: LILJA-2009 + inference |
| ensemble_behavior | Two electrics sharing register and voicing mask each other as acoustic; pickup and gain choice give an additional separation tool beyond neck position, since two guitars can occupy different spectral "lanes" via tone alone | inference |
| recording_behavior | Pickup position and selection (neck: dark/full; bridge: bright/thin, via the comb-filter mechanism below) function as part of the instrument, not a mix decision; a raw, unamplified direct signal from a magnetic pickup sounds thin and unlike the instrument as heard in practice, because the amplifier/speaker stage is expected | academic: PAIVA-PICKUPS-2012 |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | As acoustic, except high-gain/high-sustain patches can legitimately hold well past a clean instrument's natural decay; this should be a deliberate sustain/feedback choice, not silent over-holding | inference |
| overlap | As acoustic: legato patches need overlap; a vibrato-arm glide patch, where present, behaves more like a continuous pitch-bend device than a discrete transition sample | inference |
| velocity | Selects level, pick attack character, and on some patches interacts with a separate gain/distortion stage rather than being the sole determinant of "how distorted" a note sounds | inference |
| continuous_dynamics | Gain/distortion amount is a legitimate continuous-dynamics control here, distinct from velocity, because it changes timbre (harmonic/intermodulation content) the way a crossfaded dynamic layer does on a bowed or blown instrument; treating gain as fixed and velocity as the only dynamic control loses this | academic: LILJA-2009 |
| expression | Where exposed, a separate trim from level; on some patches a vibrato-arm or feedback-sustain lane is carried as an expression-like continuous control and should be planned for, not left to chance | inference |
| articulation_switching | Keyswitches as acoustic, plus dedicated feedback/sustain and vibrato-arm articulations in some libraries; non-sounding keyswitches must stay inaudible | inference |
| round_robins | As acoustic: needed for any repeated note, most audible on clean tremolo picking and on repeated palm-muted notes | inference |
| release_samples | Fret-release/damping as acoustic; a high-sustain patch's release character (how it decays out of feedback) is a distinct, product-specific behaviour worth checking rather than assuming | inference |
| pedal_or_breath_behavior | Not applicable in the acoustic sense; some libraries expose a sustain/feedback control on a pedal-like continuous lane, which is functionally closer to continuous_dynamics above than to a true sustain pedal | to-verify: whether a specific library's sustain/feedback lane should be treated as continuous_dynamics or as its own control |
| transition_samples | Recorded slides/hammer-pull as acoustic; a genuine vibrato-arm dip or dive should use a pitch-bend/MPE-style continuous control, not be approximated with a fretted-bend articulation sample, and vice versa | inference |
| mic_or_room_behavior | For a modelled amplifier/cabinet, "mic position" describes a simulated speaker-cabinet microphone choice, not the guitar body; this is a distinct control from the acoustic guitar's room-mic behaviour | inference |
| likely_fake_sounding_errors | Rich, undistorted-style chord voicings played through heavy distortion; sustained block chords with no decay or feedback logic; vibrato-arm effects substituted with plain pitch bend or vice versa; uniform gain with no dynamic relationship between pick attack and distortion character | inference |
| organic_programming_methods | Treat gain/distortion level as a phrase-level dynamic decision tied to pick attack, not a fixed amp setting; reserve rich (three-plus-note) voicings for clean or low-gain passages and thin them toward root-fifth as gain increases, following the consonance mechanism in GTR-06; use a genuine pitch-bend/MPE lane for vibrato-arm gestures | academic: LILJA-2009 |

---

## What the instrument is

A six-string fretted instrument played with two hands doing different jobs: the fretting hand chooses
which pitches are available and, on nylon and steel-string acoustics, also ends most notes; the
picking or plucking hand decides when and how notes start, and on electric guitar shares "how the
note sounds" with a gain stage that behaves non-linearly [inference]. Most of what makes a part
idiomatic follows from the fretting hand's physical limits, one consequence of which is string-stretch
sharpening under fret pressure, rather than from harmony alone [academic: VARIESCHI-2009].

## Range and register

Standard tuning's open strings, low to high, are E2 A2 D3 G3 B3 E4, and the instrument sounds an
octave below what is written in the treble clef [sourced: BERLIOZ-1855]. Berlioz describes a
practical compass of three octaves and a fifth above the low E, which corresponds to a shorter,
19th-century fingerboard; a modern instrument with 19-24 frets reaches further, into roughly the
B5-D6 region above the twelfth-fret octave [sourced: BERLIOZ-1855 + inference]. **The old page's "E2
to roughly E5" understated this**; the correction is the fret count, not a new range claim from a new
source [inference]. Below the fifth fret the instrument is thick and resonant and open strings do
real harmonic work; above the twelfth fret it thins out and is used melodically rather than as
harmonic foundation [inference].

## Articulation and note transitions

```text
palm mute (steel-string/electric)   picking-hand edge damping near the bridge; short, thick, percussive
rest stroke / apoyando (nylon)      finger follows through to rest on next string; louder, clearer
free stroke / tirando (nylon)       finger clears the strings; required for arpeggios, tone shaped by hand angle
rasgueado (nylon/flamenco)          sequenced finger flicks striking with the back of the nail; percussive, not a strum
harmonics, natural and artificial   natural at nodal frets; artificial fretted+touched+plucked; bell-like, quiet, an octave up
bends (steel-string/electric)       a fretted note pushed sideways; intonation is by ear and finger strength
slides                              one finger moving along a string; intervening pitches are audible
hammer-on / pull-off                the instrument's real legato; quieter than the picked note before it
vibrato                             fretting-hand finger or hand motion after the attack; electric also has vibrato-arm vibrato
dead note                           a muted click at a rhythmic position, with no clear pitch
vibrato arm (electric only)         mechanically varies string tension/length and position relative to the pickup; no unfretted equivalent
feedback (electric only)            sustained or growing note from acoustic coupling between speaker output and string; a usable device, not only noise
```

Rest stroke and free stroke are read from performer pedagogy [sourced: RESTSTROKE-PEDAGOGY].
Rasgueado is read from performer pedagogy [sourced: NIEDT-RASGUEADO]. The fretting-hand mechanics of
ending a note are read from a classical method [sourced: SOR-METHOD]. Bends, slides, dead notes,
harmonics, the vibrato arm and feedback are stated as general fretted-instrument and
electric-instrument reasoning [inference].

Hammer-ons and pull-offs are quieter than the picked note before them because no new pluck excites
the string; a legato line played at uniform velocity has been written as if every note were picked
[inference]. Rest stroke and free stroke are a genuinely separate mechanical choice on nylon guitar,
not a volume knob on one stroke [sourced: RESTSTROKE-PEDAGOGY]; treating them as interchangeable
loses both the tonal difference and the arpeggio-vs-melody logic that decides which one a real player
would use [inference].

## Physical constraints

This section is the source of most feasibility failures in this family [inference].

```text
one note per string, six strings, so six notes maximum and no unisons on one string
the fretting hand spans about four frets in low positions, more higher up where frets are closer
open strings extend what is reachable, which is why open-position chords are shaped as they are
a barre uses one finger across some or all six strings, and REPRODUCES the open-position shape movably
movable barre shapes are therefore full five- and six-note voicings, not reduced to four notes
```
[inference]

**The 2.0 page's claim that six-note voicings exist mainly in open position was wrong.** An E-shape
barre chord (root on the low E string) and an A-shape barre chord (root on the A string) are both
movable six- and five-note shapes respectively, built by laying the first finger across the strings
as a temporary fret and fingering the rest of the open-position shape on top of it, which Forsyth
describes as the barre acting "as a temporary fret" [sourced: FORSYTH-1914]. Generalising this
mechanism to the specific E- and A-shape barre system is this pack's own fretboard-geometry reasoning
[inference]. A dense jazz voicing that omits tones is a chosen thinning, not evidence that six-note
movable shapes are impossible [inference].

Fretting pressure stretches the string and sharpens its pitch above the theoretical fretted value; a
hard barre or a held bend sharpens further and unevenly across strings [academic: VARIESCHI-2009].
Standard saddle compensation corrects most of this for normal fretting pressure but does not chase a
harder-than-normal press [inference].

## Phrase behaviour

Phrases are bounded by neck position; a shift is audible as a slide or a small gap, and a line that
never shifts across two octaves reads as written for a keyboard [inference]. A note decays from the
moment it sounds, so sustained writing on acoustic guitars needs re-attack, tremolo picking, or a
different instrument; on electric guitar, gain and feedback genuinely extend sustain past the
string's natural decay and this is a legitimate, deliberate device rather than an error [inference].

**A strum is a spread, not a chord, and the spread is now measured rather than guessed.** A
downstroke runs low string to high, an upstroke high to low, and alternating strokes give alternating
directions; the order decides which note the ear hears as the top of the attack [inference]. A study
of guitar strumming measured intertone spread (between adjacent strings) and global spread (first to
last string) across block, strummed and arpeggiated chords on one nylon guitar, three players
[academic: FREIRE-STRUM-2018]:

```text
chord type (notes)         tempo             intertone spread     global spread
4-note block                very fast          0-6 ms                5-18 ms
3-note block                 very slow          0-5.5 ms              5-11 ms
6-note strummed              adagio             8-11 ms               37-46 ms
6-note strummed              moderate           5-12.5 ms             26-62 ms
6-note arpeggio               moderate           16-40 ms              64-202 ms
```
[academic: FREIRE-STRUM-2018]

**These are means from a small study (three players, three excerpts) and are labelled by the paper
itself as preliminary empirical limits, not a general law of guitar strumming.** They are a real,
sourced starting point in place of an invented "a few milliseconds" default, and should be treated as
a range to vary within by chord density and tempo, not a constant to apply everywhere
[academic: FREIRE-STRUM-2018].

Tremolo and other repeated-note passages are, among skilled players, regular in overall rhythmic
timing, but the individual note durations and dynamics are not perfectly uniform even then; this
irregularity is the technique's real character, not a flaw to remove with a flat randomisation
[academic: FREIRE-TREMOLO-2013].

Open strings vibrate sympathetically with a played string's matching harmonics, coupled through the
bridge and body; plucking the low E string anywhere except near its own one-third point can set the B
string ringing through a shared harmonic [academic: UNSW-GUITAR-INTRO]. Most acoustic guitar bodies
show three strong resonances clustered near 100-200 Hz, from top/back-plate coupling and the
soundhole's Helmholtz (air-cavity) mode, with weaker higher-frequency top-plate modes adding colour
rather than loudness [academic: UNSW-GUITAR-MODES]. The body is a radiator, not an amplifier: all of
the acoustic energy comes from the string, and the body's job is to convert it into a larger, more
efficient radiating surface [academic: UNSW-GUITAR-INTRO]. A part with every string damped at all
times denies this resonance entirely, which is audibly different from a part that lets it happen
[inference].

## Ensemble behaviour

Two guitars playing the same voicing in the same register fight; the usual solution is different neck
positions, so the same chord has different string assignments and different timbre [inference].
Rhythm guitar and bass share a low register and are separated by the guitar staying above the bass, or
by playing only the upper part of its voicing [inference]. On electric guitar, pickup and gain
selection add a spectral-separation tool beyond neck position [inference].

## Recording behaviour

On an electric instrument the pickup position, and the amplifier and speaker, are part of the
instrument, not effects layered afterward [inference]. A magnetic pickup senses string velocity at a
fixed point; because the string vibrates in standing-wave modes, this produces a comb-filter response
that removes the harmonics with a node near the pickup [academic: PAIVA-PICKUPS-2012]. This is *why* a
bridge pickup sounds bright and thin and a neck pickup sounds dark and full, not merely a matter of
"output level" [academic: PAIVA-PICKUPS-2012]. A raw, unamplified direct signal from a magnetic
pickup sounds thin and unlike the instrument as normally heard, because the amplifier and speaker
stage is part of what listeners expect [academic: PAIVA-PICKUPS-2012].

**Distortion generates both harmonic and intermodulation (combination-tone) products, and a
root-and-fifth power chord's combination tones reinforce the root's own harmonic series, which is why
it reads as consolidated rather than muddy under heavy gain.** A third's combination tones do not
reinforce as cleanly, which is part of why rich, thirds-containing voicings read as arranged for a
clean instrument when played through heavy distortion [academic: LILJA-2009]. **The 2.0 page's claim
that a root and fifth "do not" produce intermodulation was wrong**: intermodulation exists for any
simultaneous interval under non-linear gain; the fifth's products are simply well-behaved relative to
the root, not absent [academic: LILJA-2009].

Acoustic instruments are captured by microphone position along the body; a position near the
soundhole is boomy in a way that belongs to the recording, not the instrument [inference].

## Programming it: the control model

Product specifics (controller numbers, exact velocity curves) belong in the calibration profile, not
here [inference].

```yaml
velocity: level and, in most libraries, pick/finger strength and sample selection; not a substitute for plucking-position brightness
articulation_switching: usually keyswitches; keyswitch notes are non-sounding and must not be audible
legato_patches: often monophonic per string or per patch, and need overlap
string_assignment: some libraries infer it; where they do, voicing decides the timbre
fret_noise: a separate layer or an articulation, and it is part of the instrument
strum_handling: either recorded strum patterns, or single notes spread manually using the FREIRE-STRUM-2018 ranges above
bends_and_slides: recorded articulations in some libraries, pitch bend in others; not the same gesture
gain_or_distortion: on electric, a continuous timbral control tied to pick attack, not a fixed amp setting
vibrato_arm: a genuine pitch-bend/MPE-style continuous control where available; not the same device as a fretted bend
```

Most of this control model is general sample-library convention [inference]. The `strum_handling` row
carries forward the measured strumming ranges [academic: FREIRE-STRUM-2018], and the
`gain_or_distortion` row carries forward the distortion-acoustics mechanism [academic: LILJA-2009].

## Programming it: what makes it sound real

- Solve the fretboard before writing the MIDI: decide which string each note is on, check the fret
  span, and remove anything needing two notes on one string. [inference]
- Spread every strum with a direction, varying the spread by chord density and tempo using the
  measured ranges above rather than one constant. [academic: FREIRE-STRUM-2018]
- Make hammer-ons and pull-offs quieter than the picked notes before them. [inference]
- On nylon guitar, choose rest stroke or free stroke per note the way a player would (melody and
  accented notes rest-stroke; arpeggio notes free-stroke), because the two produce genuinely
  different tone. [sourced: RESTSTROKE-PEDAGOGY]
- Build rasgueado as a fast sequence of separately-onset finger strikes, not a fast strum.
  [sourced: NIEDT-RASGUEADO]
- Give tremolo and other repeated-note passages small, named timing/dynamic variation rather than a
  flat randomisation. [academic: FREIRE-TREMOLO-2013]
- Use fretting-hand release, not silence or a glued note-off, to end or damp a note.
  [sourced: SOR-METHOD]
- Let notes decay rather than holding them on acoustic guitar; on electric, treat sustain/feedback as
  a deliberate device, not an accident. [inference]
- On electric, tie gain/distortion level to pick-attack dynamics and thin voicings toward root-fifth
  as gain rises. [academic: LILJA-2009]
- Capo: raises all open strings together, so a capoed part keeps open-string shapes in a higher key;
  writing in the sounding key with movable shapes gives a different, thicker instrument. [inference]
- Alternate tunings (drop D, open tunings, DADGAD and similar) change which shapes are movable and
  which chords fall under open strings; this reshapes voicing logic rather than only lowering a note.
  [to-verify: a dedicated alternate-tuning pedagogy source, read at section depth]

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Guitar-specific tells:

- uniform strum spread and direction every time, which removes the measured variation and error 3
  (quantised chord attacks); [academic: FREIRE-STRUM-2018]
- legato passages with picked-note velocity on every hammer-on and pull-off; [inference]
- rest stroke and free stroke used interchangeably with no tonal difference, or rasgueado played as a
  simple fast strum; [sourced: RESTSTROKE-PEDAGOGY; NIEDT-RASGUEADO]
- sustained block chords with no decay on acoustic guitar, or with no feedback/sustain logic on
  electric; [inference]
- rich, thirds-containing voicings played through heavy distortion, which reads as arranged for a
  clean instrument; [academic: LILJA-2009]
- a part that never shifts position and never makes a noise doing it; [inference]
- no fretting-hand release anywhere, so nothing ever damps or stops except by note-off; [inference]
- pitch bend used as a smooth glide where the instrument would bend a whole step from a fretted note,
  or a vibrato-arm gesture faked with plain pitch bend. [inference]

## What the Performance Director needs from this file

- `impossible_voicings`: more than six notes, two notes on one string, spans beyond roughly four
  frets in low positions, and unisons that need one string twice.
- `simultaneity_exceeded`: six voices maximum; movable barre shapes can legitimately reach five or
  six, so this is not automatically four for a movable chord (correcting the 2.0 page).
- `out_of_range`: below E2 in standard tuning, unless an alternate tuning or capo is declared; above
  roughly B5-D6 depending on the declared fret count.
- `articulation_unavailable`: bends, slides, rasgueado, rest/free stroke and vibrato-arm effects
  recorded as separate articulations cannot be silently substituted with pitch bend or a generic
  strum.
- `fret_noise`, `pick_noise` and nail noise (nylon) are recognised imperfection causes and should be
  requested here.
- Strum spread should cite the FREIRE-STRUM-2018 ranges by chord type and tempo, not a single
  practitioner constant.
- Distortion/gain level, where used, should be logged as a phrase-level dynamic decision (see
  `continuous_dynamics`), not left implicit in a fixed amp patch.

## Sources and what to verify

Full citations are in `research/sources/INSTRUMENT_SOURCES.md`; claim-level detail and limitations
are in `research/instruments/GUITAR.md`.

- **Available and used**: a measured strum spread (FREIRE-STRUM-2018), tremolo timing regularity
  (FREIRE-TREMOLO-2013), plucking-point acoustics (TRAUBE-2000), pickup-position acoustics
  (PAIVA-PICKUPS-2012), fret-pressure intonation (VARIESCHI-2009), distortion intermodulation
  (LILJA-2009), fretting-hand release and nail technique (SOR-METHOD), body resonance and sympathetic
  vibration (UNSW-GUITAR-INTRO, UNSW-GUITAR-MODES), rasgueado mechanics (NIEDT-RASGUEADO), rest/free
  stroke mechanics (RESTSTROKE-PEDAGOGY), and guitar range/voicing basics from a public-domain
  orchestration treatise (BERLIOZ-1855, FORSYTH-1914).
- **To verify**: exact sounding-range and register description in Adler, *The Study of
  Orchestration* (ADLER-ORCH, not-read). This page's range figure is an inference from fret-count
  arithmetic, not an Adler citation.
- **To verify**: the acoustic-feedback phase mechanism between speaker output and string, and the
  general physics of dynamic-dependent spectral brightening, in Fletcher and Rossing, *The Physics of
  Musical Instruments* (FLETCHER-ROSSING-1998, not-read).
- **To verify**: alternate-tuning voicing logic beyond drop-D and open tunings, in a dedicated
  fingerstyle/alternate-tuning pedagogy source; not opened at section depth for this pass.
- **Not available**: nylon-specific fret-pressure sharpening magnitude (the measured figures in
  VARIESCHI-2009 are from a steel-strung laboratory instrument); a controlled study of palm-mute
  damping time or fret-hand release timing in milliseconds.
