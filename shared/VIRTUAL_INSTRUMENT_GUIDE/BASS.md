# Bass

Electric bass (four- and five-string), fretless electric bass, and double bass played pizzicato in
jazz and popular-music contexts. **Bowed double bass stays out of scope here and is covered in
`STRINGS.md`**; where a technique (e.g. pizzicato inside an otherwise bowed part) crosses the line,
this file is the one to use.

> Evidence: seven sources read at section depth. Two are academic acoustics papers shared with
> `GUITAR.md` because the underlying physics (magnetic pickup response; fret-pressure intonation) is
> the same mechanism applied to a different instrument. Five are performer-pedagogy pages covering
> double bass pizzicato technique, fretless intonation and vibrato, and ghost-note mechanics. **No
> bass-specific manufacturer manual or acoustics paper was found and opened**, so several rows below
> apply a general mechanism to bass by extension and are labelled `inference` for that extension, not
> for the underlying physics. Source IDs resolve in `research/sources/INSTRUMENT_SOURCES.md`; the
> claims and their limits are recorded in `research/instruments/BASS.md`.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## Behaviour cards

### Electric Bass (Four- and Five-String)

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Long-scale fretted strings, plucked or struck, sensed by one or more fixed-position magnetic pickups; the pickup senses string velocity at one point, not the whole string | academic: PAIVA-PICKUPS-2012 |
| attack_behavior | A transient set by plucking-finger alternation (index/middle or similar), pick attack, or slap/pop technique; near-bridge plucking gives a tighter, more articulate attack, plucking over the neck gives a rounder, softer one | inference |
| sustain_behavior | Long and uneven: a strong initial transient, a bloom, then a slow tail with slightly moving pitch as the string settles; does not behave like a rectangular block | inference |
| release_behavior | The fretting hand ends or dampens a note by releasing or laying across the string; the picking hand can also mute by resting against the strings near the bridge. Note length on bass is an articulation choice, not a default | inference |
| dynamic_timbre_change | Plucking harder changes attack hardness and brightness, not only level; plucking position (near bridge = thin, articulate; over the neck = round, full) is a continuous timbral control a player moves through within a phrase, independent of loudness | academic: PAIVA-PICKUPS-2012 + inference |
| register_character | Below the twelfth fret is the primary working register, carrying harmonic floor and groove; above the twelfth fret is thin and used melodically. The lowest notes' fundamentals are often below what small playback systems reproduce, so audibility depends on the harmonics above the fundamental | inference |
| practical_range | four-string, standard tuning: written and sounding are the same octave family but written an octave above sounding pitch, open strings E1 A1 D2 G2, 20-24 frets; five-string adds a low B0. **Range floor depends on declared tuning**: drop-D and similar four-string drop tunings put the lowest string below standard E1 | inference |
| tessitura | Most resonant and controllable in the open-to-twelfth-fret range; the low B on a five-string is felt more than clearly heard on small speakers because its fundamental sits below common playback reproduction | inference |
| articulation_logic | Fingerstyle, pick, slap and pop, ghost note, dead note, slide, hammer-on and pull-off, harmonics | sourced: GHOSTNOTE-PEDAGOGY + inference |
| phrase_limits | Bounded by hand position and by the natural decay of a plucked low note; a "held" phrase past that decay needs re-attack or a different device | inference |
| transitions | Hammer-ons and pull-offs quieter than a plucked note, as on guitar; slides are a standard way to approach a note and carry audible intervening pitch | inference |
| repeated_note_behavior | A repeated pitch is not identical note to note even at a fixed dynamic marking: plucking-finger alternation changes attack character, the same pitch is sometimes available on two strings with different timbre, and metrical position changes accent. None of these is randomness; each is a named, controllable choice | inference |
| vibrato | On a fretted bass, a small rocking motion of the fretting finger, similar in kind to guitar vibrato but usually narrower given the thicker strings; absent on open strings | inference |
| pitch_instability | Fret-pressure stretches the string and sharpens pitch above the fretted target, by the same mechanism measured on a fretted-instrument monochord; bass-specific magnitude is unverified | academic: VARIESCHI-2009 + to-verify: what would settle this is not recorded |
| resonance | Open strings can ring sympathetically with a played string's matching harmonics through the bridge and body/neck, though this is less prominent than on an acoustic guitar because most electric basses have little resonant body cavity; pickup position affects which harmonics are emphasised via the same comb-filter mechanism as guitar | academic: PAIVA-PICKUPS-2012 + inference |
| physical_noise | Fret noise on position shifts and slides, pick or finger attack noise, and the audible "thump" of a hard pluck against the fingerboard, which is a deliberate part of some styles rather than a flaw | inference |
| feasibility | One note per string; double stops (two notes) are idiomatic and common, three-note-plus chords exist only in open, widely-spaced voicings | inference |
| ensemble_behavior | Bass and kick drum share register and rhythmic territory; the relationship (locked, answering, or deliberately ahead/behind) is an arrangement decision. Doubling bass with a low synth layer usually forces one of the two to give up its fundamental | inference |
| recording_behavior | Direct signal carries low fundamental and finger noise; amplifier carries midrange and character; pickup position matters by the same comb-filter mechanism as guitar. Compression norms are genre-bound: jazz and acoustic-leaning production often preserves wide dynamic range deliberately, while pop/rock/hip-hop convention compresses heavily; an uncompressed bass is not "unfinished" outside that convention | academic: PAIVA-PICKUPS-2012 + inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Not a rectangular block; note length and the silence after it are articulation choices, and gluing notes end to end removes the groove the silences carry | inference |
| overlap | Legato/slide/hammer-on patches are monophonic and need overlap to produce a real transition rather than two separate attacks | inference |
| velocity | Level, attack hardness, and in most libraries the choice between soft and hard pluck samples; not a stand-in for plucking-position brightness | inference |
| continuous_dynamics | No true held-note crossfade the way a bowed instrument has, because a plucked note decays; per-note velocity, plucking-position choice (where modelled), and articulation carry expression instead | inference |
| expression | A level trim where exposed, not a timbre control by itself | inference |
| articulation_switching | Keyswitches for slides, ghost notes, harmonics, slap and pop; keyswitch notes are non-sounding | inference |
| round_robins | Needed for any repeated note, especially groove patterns with a repeated root or ghost-note pattern | inference |
| release_samples | String release and finger noise; lost when notes are glued end to end, removing the release character that carries much of bass's realism | inference |
| pedal_or_breath_behavior | Not applicable: the electric bass has no pedal or breath control | inference |
| transition_samples | Recorded slides and hammer-on/pull-off transitions in some libraries, pitch bend in others; not the same gesture | inference |
| mic_or_room_behavior | Amplifier/cabinet mic position (real or modelled) shapes midrange character; the direct-signal path is a separate, usually blended source | inference |
| likely_fake_sounding_errors | Rectangular note blocks glued end to end; every note at one velocity; no ghost notes or slides anywhere; the same repeated root at identical velocity with no named variation; close-voiced chords in the bottom octave; notes below the declared tuning's lowest string | inference |
| organic_programming_methods | Write ghost notes explicitly, with left-hand deadening as the mechanism, not a velocity-zone substitute; vary a repeated figure by naming the cause (plucking-finger alternation, string choice, metrical accent), not by flat randomisation; vary note length and leave silence deliberately; use slides into notes at phrase starts and octave jumps; decide the kick relationship before writing | sourced: GHOSTNOTE-PEDAGOGY + inference |

### Fretless Electric Bass

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Same long-scale, magnetic-pickup-sensed string as fretted electric bass, but with no frets: the string is stopped directly against the fingerboard at a player-judged point rather than a fixed fret position | inference |
| attack_behavior | Softer and rounder than a fretted attack because there is no fret-edge click; otherwise as fretted electric bass (finger alternation, position, pick vs. finger) | inference |
| sustain_behavior | As fretted electric bass: long, uneven decay with a settling tail; the tail's pitch settling is more audible on fretless because there is no fret to fix the endpoint | inference |
| release_behavior | As fretted bass, the fretting hand lifts or dampens to end a note; because there is no fret, releasing pressure produces a more continuous pitch glide into silence rather than a clean cutoff | inference |
| dynamic_timbre_change | As fretted bass for plucking dynamics; finger angle at a fixed apparent position measurably shifts pitch, which is a fretless-specific coupling between "how" a note is played and its intonation that a fretted instrument does not have | sourced: FRETLESS-INTONATION-PEDAGOGY |
| register_character | As fretted bass; the absence of frets makes the upper register (where fret spacing would be narrowest) comparatively harder to place accurately | inference |
| practical_range | As fretted electric bass (same tuning, same open strings); an unlined fretless fingerboard removes even the visual position reference, which is a technique fact, not a range fact | sourced: FRETLESS-VIBRATO-PEDAGOGY |
| tessitura | As fretted bass; intonation risk rises with register because the same absolute finger-placement error is a larger fraction of a semitone in higher positions (shorter string segments) | inference |
| articulation_logic | As fretted bass, plus fretless-specific portamento/glide, since there is no fret to make a "slide" discrete | inference |
| phrase_limits | As fretted bass | inference |
| transitions | Slides and glides are continuous rather than fret-to-fret, and hammer-ons/pull-offs still work but land on a felt rather than fretted position | inference |
| repeated_note_behavior | As fretted bass (named causes, not randomness), with the added fact that no two placements of the "same" finger position are pitch-identical unless deliberately practised to be, per fretless intonation training | sourced: FRETLESS-INTONATION-PEDAGOGY |
| vibrato | A broader, more continuous rolling motion of the fingertip than fretted vibrato, closer to a string player's vibrato than a guitarist's; must not be used to cover an out-of-tune note, which is a stated pedagogical rule, not house style | sourced: FRETLESS-VIBRATO-PEDAGOGY; FRETLESS-INTONATION-PEDAGOGY |
| pitch_instability | The central technical fact of the instrument: intonation depends on developed muscle memory for interval spacing, verified by ear (and, in practice, by interference beating on double stops), not by a fret or a fixed visual reference | sourced: FRETLESS-INTONATION-PEDAGOGY |
| resonance | As fretted electric bass | inference |
| physical_noise | Less fret noise than fretted bass (no fret edges), but finger-on-fingerboard noise (a soft thump or slide noise) remains audible and is part of the instrument's character | inference |
| feasibility | As fretted bass for note count; feasibility here is primarily an intonation risk, not a physical-voicing one | inference |
| ensemble_behavior | As fretted bass | inference |
| recording_behavior | As fretted bass; intonation drift under a section or with other instruments is a real risk unique to this instrument and worth flagging for a mix/arrangement check | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | As fretted electric bass | inference |
| overlap | As fretted electric bass; slide/glide patches especially need overlap to trigger a continuous transition rather than two discrete notes | inference |
| velocity | As fretted electric bass | inference |
| continuous_dynamics | As fretted electric bass | inference |
| expression | Where a library exposes continuous pitch control (MPE or per-note pitch), this is the natural home for fretless-style glides and micro-intonation, distinct from a discrete pitch-bend articulation | inference |
| articulation_switching | As fretted electric bass, with glide/portamento as an additional common articulation | inference |
| round_robins | As fretted electric bass | inference |
| release_samples | As fretted electric bass | inference |
| pedal_or_breath_behavior | Not applicable: the fretless electric bass has no pedal or breath control | inference |
| transition_samples | A recorded fretless slide/glide articulation, where available, is not equivalent to a generic pitch-bend curve; the real instrument's glide is continuous and player-timed, not a fixed-rate ramp | inference |
| mic_or_room_behavior | As fretted electric bass | inference |
| likely_fake_sounding_errors | Perfectly in-tune notes with no natural micro-drift; vibrato used uniformly on every note regardless of phrase position; glides quantised to fret-like discrete steps, which defeats the point of the instrument | inference |
| organic_programming_methods | Model small, controlled pitch variation rather than perfect tuning, since even trained players do not land identically twice; reserve vibrato for phrase-level expressive moments rather than applying it constantly, per the explicit pedagogical warning against using it to mask intonation | sourced: FRETLESS-INTONATION-PEDAGOGY; FRETLESS-VIBRATO-PEDAGOGY |

### Double Bass (Pizzicato, Jazz/Pop Context)

Bowed double bass technique is covered in `STRINGS.md`. This card is pizzicato only.

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Four thick strings over a large body, plucked by the right hand; the left hand's stopping and the string's tension and gauge do most of the tone-shaping work before the pluck happens | sourced: FOX-DOUBLEBASS-PLUCK |
| attack_behavior | Jazz pizzicato: fingers parallel to the string, plucking with the pad/first joint, pulling through into the next string, producing a louder attack where the finger's impact against the fingerboard is audible and wanted. Orchestral pizzicato: fingers roughly perpendicular to the string, a smaller point of contact near the fingertip, a drier, more precise, faster-decaying attack that deliberately avoids fingerboard buzz | sourced: PIZZICATO-STYLE-PEDAGOGY; FOX-DOUBLEBASS-PLUCK |
| sustain_behavior | A resonant, woody decay in jazz pizzicato; a shorter, more "timpani-like" decay with a hint of resonance in orchestral pizzicato. Sound quality is a function of the balance among the overtone series set up by the pluck | sourced: PIZZICATO-STYLE-PEDAGOGY |
| release_behavior | The left hand does most of the articulation work: damping for clarity between notes is an explicit technique, not an afterthought, especially in walking-bass and swing contexts | inference |
| dynamic_timbre_change | How much of the finger (tip vs. pad/first joint), how fast the finger moves through the string, and where along the string it plucks together set both loudness and tone; playing harder with the right hand can choke the sound rather than simply making it louder, so dynamics are not a single linear knob | sourced: FOX-DOUBLEBASS-PLUCK |
| register_character | Lower register is the instrument's primary working range for walking lines and time-keeping; higher positions (thumb position and above) are used melodically and require more left-hand precision | inference |
| practical_range | Roughly E1 to the upper register reached in thumb position; written at pitch or an octave above sounding pitch depending on convention. Sounding an octave below the written bass clef in standard orchestral notation | inference |
| tessitura | Most resonant and idiomatic below the octave harmonic; walking bass lines in jazz work primarily in this lower-middle register | inference |
| articulation_logic | Jazz and orchestral pizzicato as two distinct techniques (see attack_behavior), plus left-hand damping, slides, and ghost/dead notes analogous to electric bass technique | sourced: PIZZICATO-STYLE-PEDAGOGY |
| phrase_limits | Bounded by hand position and, in a walking-bass context, by the harmonic/rhythmic demands of keeping time across a chorus; a physical decay limit as on electric bass, longer given the larger string mass and body | inference |
| transitions | Slides between positions are audible and idiomatic; hammer-on/pull-off equivalents exist but are less central to jazz pizzicato vocabulary than on electric bass | inference |
| repeated_note_behavior | As electric bass: named causes (plucking-finger choice, position, metrical accent) rather than randomness account for note-to-note variation in a repeated figure | inference |
| vibrato | Produced by the left hand on a stopped note; less central to pizzicato playing than to bowed playing, used selectively for expressive emphasis | inference |
| pitch_instability | Left-hand placement accuracy is the primary intonation factor, as on fretless electric bass, since double bass has no frets | inference |
| resonance | The large body and thick strings give substantial sympathetic resonance and a long, warm decay; this is part of why jazz pizzicato's "thumpy, resonant, woody" character is achievable at moderate dynamics | sourced: PIZZICATO-STYLE-PEDAGOGY |
| physical_noise | Fingerboard buzz from the finger's impact is a wanted, deliberate part of jazz pizzicato tone; orchestral technique generally avoids it | sourced: PIZZICATO-STYLE-PEDAGOGY |
| feasibility | One note per string typically; double stops are used but less central than on electric bass; four strings, standard tuning | inference |
| ensemble_behavior | Anchors harmony and time in a jazz rhythm section through walking bass lines, two-feel patterns, and stylistic articulation tied to swing, bop or Latin grooves | sourced: PIZZICATO-STYLE-PEDAGOGY |
| recording_behavior | Often close-miked and/or pickup-amplified in jazz contexts to bring out the attack; orchestral pizzicato is more often captured at ensemble distance, prioritising blend over individual attack | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | As electric bass: not a rectangular block; the natural decay and left-hand damping decisions carry real musical meaning | inference |
| overlap | Slide patches need overlap as on electric bass; otherwise mostly monophonic discrete attacks | inference |
| velocity | Level and, where a library distinguishes them, jazz-style versus orchestral-style pluck sample selection; these are different articulations, not points on one velocity curve | inference |
| continuous_dynamics | No true held-note crossfade for pizzicato (notes decay); per-note velocity and articulation choice carry expression | inference |
| expression | A level trim where exposed | inference |
| articulation_switching | Keyswitches for jazz vs. orchestral pizzicato, slides, ghost/dead notes, and (if the patch also covers bowed playing) arco articulations, which belong to `STRINGS.md`'s scope, not this card | inference |
| round_robins | Needed for any repeated note, especially a walking bass line's repeated roots | inference |
| release_samples | Finger and string-release noise; a large part of what makes jazz pizzicato read as played rather than triggered | inference |
| pedal_or_breath_behavior | Not applicable: double bass pizzicato has no pedal or breath control | inference |
| transition_samples | Recorded slide articulations where available; a jazz walking-bass slide into a downbeat is a distinct gesture from a generic pitch bend | inference |
| mic_or_room_behavior | Close-miked/amplified jazz pizzicato versus ensemble-distance orchestral pizzicato are different recorded characters, not the same patch at different volumes | inference |
| likely_fake_sounding_errors | Jazz and orchestral pizzicato treated as the same articulation at different velocities; no fingerboard buzz ever on a part that wants a jazz character, or buzz present on a part that wants an orchestral one; uniform walking-bass note lengths with no left-hand damping variation | inference |
| organic_programming_methods | Choose jazz or orchestral pizzicato as a distinct articulation decision, not a velocity zone, per the mechanical differences above; vary walking-bass note length and damping deliberately rather than gluing notes; let attack character follow the plucking-finger and position logic named above | sourced: PIZZICATO-STYLE-PEDAGOGY; FOX-DOUBLEBASS-PLUCK |

---

## What the instrument is

A long-scale (electric) or large-bodied (double bass) instrument whose job in most music is two
things at once: the harmonic floor, and half of the rhythmic engine [inference]. Which of those a
part is serving decides most programming choices in this file [inference]. The family spans three
meaningfully different physical instruments (fretted electric, fretless electric, double bass), which
is why this page carries three cards rather than one shared card: their release mechanisms,
intonation risk, and tone-production logic differ enough that collapsing them would lose the
distinctions the audit asked for [inference].

## Range and register

Four-string electric bass in standard tuning: E1 A1 D2 G2, written an octave above sounding pitch,
20-24 frets [inference]. Five-string adds a low B0 [inference]. **The 2.0 page's floor of "below E1
on a four-string" assumed standard tuning**; drop-D and similar four-string drop tunings put the
lowest string below standard E1 (a drop-D bass tunes its lowest string to D1), so `out_of_range` must
be checked against the declared tuning, not a fixed constant, correcting the 2.0 claim [inference].
Fretless electric bass shares the same open-string range; double bass sits in a comparable low
register with its own tuning and notation convention [inference]. The register above the twelfth
fret on electric bass is thin and melodic rather than a harmonic floor [inference].

## Articulation and note transitions

```text
fingerstyle              alternating fingers (commonly index/middle); round, soft attack; the default for most music
pick                      harder, brighter, more consistent attack; cuts through dense arrangements
slap and pop              thumb struck against low strings, fingers pulled off high ones; percussive
ghost note                a muted, pitchless click produced by left-hand deadening plus a normal pluck
dead note                  the same idea used as an articulation inside a line
slide                      audible movement between positions; a standard way to approach a note
hammer-on and pull-off     softer than a plucked note, as on guitar
fretless glide/portamento  continuous pitch movement with no discrete fret events
jazz pizzicato (double bass)      parallel-finger attack, audible fingerboard contact, resonant/woody
orchestral pizzicato (double bass) perpendicular-finger attack, dry, precise, buzz avoided
```

The ghost-note row is read from bass pedagogy [sourced: GHOSTNOTE-PEDAGOGY]. The two double bass
pizzicato rows are read from double bass pedagogy [sourced: PIZZICATO-STYLE-PEDAGOGY; FOX-DOUBLEBASS-PLUCK].
The rest is general fretted-instrument reasoning [inference].

**Ghost notes and slides carry the groove; they are not decoration.** A bass line written as pitches
on the beat with nothing between them is a harmonic part, not a bass part [inference]. The left hand
deadens the string for a ghost note while the right hand plucks normally; playing closer to the
bridge, where effective string tension is greater for a given pluck, makes ghost notes louder and
easier to control [sourced: GHOSTNOTE-PEDAGOGY].

## Physical constraints

One note per string on electric and double bass; double stops are idiomatic, chords above two notes
are rare and voiced open [inference]. Fretless removes the fret as a position reference entirely,
which is a technique and intonation constraint rather than a range or voicing one
[sourced: FRETLESS-INTONATION-PEDAGOGY]. Fret-pressure sharpens pitch on fretted bass by the same
mechanism measured on a guitar/mandolin-geometry instrument; the bass-specific magnitude is
unverified [academic: VARIESCHI-2009 + to-verify: what would settle this is not recorded].

## Phrase behaviour

A plucked low note has a long, uneven decay: a strong initial transient, a bloom, and a slow tail
with slightly moving pitch as the string settles [inference]. Note length on bass is an articulation
choice; a line with every note ending exactly at the next has no groove, because the silences between
notes are where the groove lives [inference].

On fretless bass, the settling tail's pitch drift is more audible than on fretted bass because
nothing fixes the endpoint [inference]. On double bass, phrase length in a walking-bass context is
also shaped by the harmonic and rhythmic demands of keeping time across a chorus, not only by
physical decay or breath [inference].

## Ensemble behaviour

The bass and kick drum occupy the same frequency range and rhythmic territory; the relationship
between them (locked, answering, or deliberately ahead/behind) is an arrangement decision, not a mix
problem to fix afterward [inference]. In a jazz rhythm section, double bass pizzicato anchors harmony
and time through walking bass lines, two-feel patterns, and stylistic articulation tied to swing, bop
or Latin grooves [sourced: PIZZICATO-STYLE-PEDAGOGY]. Doubling bass with a low synth layer thickens
the register quickly and usually forces one of the two to give up its low fundamental [inference].

## Recording behaviour

Direct signal carries the low fundamental and finger noise; the amplifier carries midrange and
character [inference]. Pickup position matters by the same comb-filter mechanism established for
guitar: a fixed-point magnetic pickup produces a position-dependent comb-filter response, so a
bridge-position pickup is measurably brighter than a neck-position pickup, extending the same physics
to bass [academic: PAIVA-PICKUPS-2012 + inference].

**Compression is genre-bound, not universal.** The 2.0 page's claim that "an uncompressed bass reads
as unfinished" reflects pop/rock/hip-hop production convention, where heavy compression is standard
[inference]. Jazz and acoustic-leaning production commonly preserves wide dynamic range on bass
deliberately, including on double bass pizzicato, where the point is often to hear the difference
between the quietest and loudest notes [inference].

Double bass pizzicato recording differs by context: jazz playing is often close-miked or pickup-
amplified to bring out the attack; orchestral pizzicato is more often captured at ensemble distance,
prioritising blend over individual attack, drawn from the technique differences above
[sourced: PIZZICATO-STYLE-PEDAGOGY + inference].

## Programming it: the control model

Product specifics belong in the calibration profile, not here [inference].

```yaml
velocity: level, attack hardness, and in most libraries the choice between soft and hard pluck samples
articulation_switching: keyswitches for slides, ghost notes, harmonics, slap and pop, and (double bass) jazz vs. orchestral pizzicato
legato_patches: monophonic, and need overlap to produce a real slide, hammer-on, or fretless glide
release_samples: string release and finger noise; lost when notes are glued end to end
fret_noise: a separate layer; on fretted bass a large part of the realism, absent by construction on fretless and double bass
string_assignment: decides timbre where the library models it; a low note on a high string is different
fretless_pitch_control: where a library exposes continuous per-note pitch (MPE or similar), this is the natural home for glides and micro-intonation
```

This control model is general sample-library convention [inference].

## Programming it: what makes it sound real

- Write the ghost notes, with left-hand deadening as the mechanism, not a soft-velocity substitute.
  [sourced: GHOSTNOTE-PEDAGOGY]
- Vary note length deliberately and leave silence; short is a choice, long is a choice. [inference]
- Use slides into notes, especially at phrase starts and octave jumps. [inference]
- Vary a repeated figure by naming the cause: alternate the plucking finger, use a different string
  for the same pitch where the instrument allows it, or lean on metrical accent, rather than applying
  an unnamed "humanize" amount, applying `shared/HUMAN_PERFORMANCE_SCHEMA.md` section 3 to bass
  specifically. [inference]
- On fretless bass, model small, controlled pitch variation rather than perfect tuning, and reserve
  vibrato for phrase-level expressive moments; never use vibrato to paper over a wrong pitch.
  [sourced: FRETLESS-INTONATION-PEDAGOGY; FRETLESS-VIBRATO-PEDAGOGY]
- On double bass, choose jazz or orchestral pizzicato as a distinct articulation, not a velocity zone
  of the same sample, because the mechanical technique and the wanted amount of fingerboard buzz
  differ between them. [sourced: PIZZICATO-STYLE-PEDAGOGY]
- Decide the kick relationship before writing, and keep it consistent enough to be a feel. [inference]
- Keep one note per string; a three-note chord on bass is possible only in open voicings. [inference]

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Bass-specific tells:

- rectangular blocks glued end to end, which is error 12, and the reason a sampled bass sounds like a
  synth patch; [inference]
- every note at one velocity, which removes the whole groove vocabulary; [inference]
- no ghost notes and no slides anywhere; [inference]
- a repeated root varied only by unnamed randomisation rather than a named cause (finger alternation,
  string choice, metrical accent); [inference]
- close-voiced chords in the bottom octave; [inference]
- notes below the *declared* tuning's lowest string, not just below standard E1; [inference]
- fretless bass with perfect, static intonation and no natural micro-drift, or with vibrato applied
  uniformly regardless of phrase position; [sourced: FRETLESS-INTONATION-PEDAGOGY]
- double bass jazz and orchestral pizzicato treated as the same articulation at different velocities;
  [sourced: PIZZICATO-STYLE-PEDAGOGY]
- a line that ignores the kick entirely and then gets fixed with a sidechain; [inference]
- a heavily compressed bass in a context (jazz, acoustic) where the genre convention is the opposite.
  [inference]

## What the Performance Director needs from this file

- `out_of_range`: checked against the *declared* tuning (standard, drop-D, five-string, or other),
  not a fixed constant; correcting the 2.0 page's assumption of standard tuning only.
- `impossible_voicings`: two notes on one string, and chords above two notes outside open voicings.
- `articulation_unavailable`: slap, pop, ghost notes, and (double bass) jazz-versus-orchestral
  pizzicato are separate recordings/techniques, not velocity zones of one sample.
- `note_length_variation` is a required imperfection here, not an optional one, on all three
  instruments in this file.
- `fret_noise` and `pick_noise` should be requested explicitly on fretted electric bass; fretless and
  double bass substitute finger/fingerboard noise instead.
- Fretless bass intonation risk should be flagged as a distinct feasibility concern, closer to a
  register-strength check than a voicing check: the higher the register, the smaller the absolute
  placement error that still causes an audible pitch problem.
- The kick relationship belongs in the plan, so the Mix Engineer reads an intent rather than guessing.
- Compression convention should be logged as a genre decision in the plan (`realism_target` /
  production style), not assumed.

## Sources and what to verify

Full citations are in `research/sources/INSTRUMENT_SOURCES.md`; claim-level detail and limitations
are in `research/instruments/BASS.md`.

- **Available and used**: pickup-position acoustics extended from guitar (PAIVA-PICKUPS-2012),
  fret-pressure intonation mechanism extended from guitar (VARIESCHI-2009), double bass
  jazz-versus-orchestral pizzicato mechanics (PIZZICATO-STYLE-PEDAGOGY, FOX-DOUBLEBASS-PLUCK),
  fretless intonation and vibrato pedagogy (FRETLESS-VIBRATO-PEDAGOGY,
  FRETLESS-INTONATION-PEDAGOGY), ghost-note mechanics (GHOSTNOTE-PEDAGOGY).
- **To verify**: bass-specific fret-pressure sharpening magnitude (only a guitar/mandolin-geometry
  measurement is available). Low-frequency string decay and pitch-settling physics, in Fletcher and
  Rossing, *The Physics of Musical Instruments* (FLETCHER-ROSSING-1998, not-read).
- **Not available**: measured velocity bands for ghost notes on bass; the drum-kit figure in
  `DRUM_KIT.md` should not be borrowed for this instrument, consistent with the 2.0 page's own
  caution. A section-depth source for genre-specific bass compression norms; the current claim is
  general production knowledge, not a cited text.
