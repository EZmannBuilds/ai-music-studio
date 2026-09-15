# Ewe Dance Drums

Traditions: Ewe dance-drumming of the Anlo Ewe (southeastern Ghana, southern Togo, and adjacent
Benin). Context: `shared/MUSICAL_SYSTEMS/EWE_DANCE_DRUMMING.md`.

This page covers the ensemble of an Anlo-Ewe recreational dance-drumming group: the double bell
**gankogui**, the gourd rattle **axatse**, the high support drum **kagan**, the response drum
**kidi**, the barrel lead drum **sogo**, and the tall lead drum **atsimevu**. It draws its technical
detail mainly from **agbadza**, a social and funerary dance-drumming repertoire, and from **Drum
Gahu**, a purely recreational, historically borrowed social dance; both are public, widely taught
repertoire. It does not draw on **Yewevu**, the drum music of the Yeve religious order, as a source
of technique to imitate: see "Restricted and ceremonial repertoire" below. Further Ewe drums named
in the sources but not covered here in depth (boba, totodzi, kroboto) are listed in "What must not
be generalised outside the tradition." Other traditions in the region, and other Ewe repertoires
such as Kpegisu (a historical war-drum piece), are out of scope for this page.

> Evidence: read at section depth: David Locke's critical edition of **Agbadza**, an
> ethnomusicological transcription and analysis built on his 1975-1977 apprenticeship with Gideon
> Foli Alorwoyie and later fieldwork [LOCKE-AGBADZA-2012]; Locke's Music Theory Online article on
> **Yewevu**, read for its general ensemble-instrumentation material only, not for Yewevu repertoire
> content [LOCKE-YEWEVU-2010]; and the "Drums and Drumming" and "Atsimevu" pages of C. K. Ladzekpo's
> teaching site, read in full, a practising Anlo-Ewe master drummer and UC Berkeley lecturer writing
> in his own voice about his own instrument [LADZEKPO-AMD]. Jeryl Johnston's comparative variation
> study was read at section depth for its agbadza material only [JOHNSTON-2024]. Kofi Agawu's article
> on the standard pattern was attempted and blocked by the publisher's bot check; it is cited only as
> `standard-reference`, not read [AGAWU-2006]. This page passes the gate in
> `shared/VIRTUAL_INSTRUMENT_GUIDE/CULTURALLY_SPECIFIC_INSTRUMENTS.md` section 3: two independent
> specialist sources at section depth or more, both practice (Locke's fieldwork-based ethnomusicology
> and Ladzekpo's own practitioner-teacher site). Source read depth and full citations are in
> `research/sources/INSTRUMENT_SOURCES.md`; claims and their limits are in `research/instruments/EWE_DANCE_DRUMS.md`.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## Behaviour cards

### Gankogui (double bell)

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A double bell forged as two joined bell lobes of different size (and so different pitch), held in the weak hand by an integral handle and struck with a single straight wooden stick held in the strong hand. | sourced: LOCKE-YEWEVU-2010; LOCKE-AGBADZA-2012 |
| attack_behavior | A single stick strike on the outside of one lobe. Which lobe is struck is the main tone choice; there is no reported hand-damping technique for gankogui the way there is for the drums. | sourced: LOCKE-AGBADZA-2012 |
| sustain_behavior | The bell rings out after each stroke; the metal is not damped between strokes in the sources read. | inference |
| release_behavior | Natural metallic decay; no mute stroke is documented in the sources read. | to-verify: whether Anlo-Ewe gankogui practice includes a muted or hand-damped bell stroke, in a source that addresses bell technique directly rather than only the bell's rhythmic phrase |
| dynamic_timbre_change | Not addressed by the sources read. | to-verify: whether stick material, strike force or strike point on the lobe changes the bell's timbre as well as its loudness |
| register_character | Two fixed, contrasting pitches, one per lobe (commonly described as a higher and a lower bell tone), set by the forging of the instrument, not by the player. | sourced: LOCKE-AGBADZA-2012 |
| practical_range | Not a range in the melodic-instrument sense: two fixed relative pitches whose exact frequencies were not given in any source read. | to-verify: measured or notated absolute or relative pitch of the two lobes |
| tessitura | Both lobes are used constantly; there is no register the part avoids. | inference |
| articulation_logic | One stick, two strike points (the two lobes), producing the two-tone bell phrase; no reported second articulation. | sourced: LOCKE-AGBADZA-2012 |
| phrase_limits | None from breath or endurance; the bell plays continuously for the duration of a piece once the time parts enter, which in agbadza is for the whole item after a brief unaccompanied vocal introduction. | sourced: LOCKE-AGBADZA-2012 |
| transitions | No legato; each stroke is a discrete, non-sustained metal attack. | inference |
| repeated_note_behavior | The same lobe can repeat within the phrase; no special technique beyond restriking is documented. | inference |
| vibrato | Not applicable. | inference |
| pitch_instability | None reported; a forged bell's pitch is fixed. | inference |
| resonance | The bell rings in open air; no body cavity or sympathetic resonator is described. | inference |
| physical_noise | Stick-on-metal attack transient distinct from the ring; not separately discussed in the sources read. | inference |
| feasibility | One hand holds the bell, the other strikes; a bell phrase requiring the same lobe struck faster than a single stick can physically re-strike is not playable. | inference |
| ensemble_behavior | The **timeline**: the bell states the seven-stroke standard pattern (in agbadza's twelve-pulse cycle) that every other part is played against, and it is the piece's marker part. It does not vary during a piece. | sourced: LOCKE-AGBADZA-2012 + standard-reference: AGAWU-2006 |
| recording_behavior | Not addressed by the sources read; in ensemble practice the bell is one voice among many percussion and voice parts rather than a spotlighted solo instrument. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short, non-sustaining hits; note length in a sequencer should not extend the metallic decay, which is fixed by the instrument, not by held-note duration. | inference |
| overlap | Not a legato instrument. | inference |
| velocity | Should select loudness within one lobe's recorded strike, and lobe choice should be a separate articulation (which of the two pitches), not a velocity layer. | inference |
| continuous_dynamics | Not applicable to a single discrete metal strike. | inference |
| expression | Not the primary control for a bell part. | inference |
| articulation_switching | Two articulations, one per lobe, each its own sample or sample set; not a pitch-shifted copy of the other. | inference |
| round_robins | Needed: the phrase repeats every cycle for the length of a piece, which can be several minutes, and identical repeated strikes on the same lobe are exposed. | inference |
| release_samples | Not applicable; the bell's natural decay is the release, with no separate release trigger. | inference |
| pedal_or_breath_behavior | Not applicable. | inference |
| transition_samples | Not applicable; no slides or glides between the two fixed pitches are documented. | inference |
| mic_or_room_behavior | Not addressed by the sources read. | to-verify: how the bell is conventionally captured relative to the rest of the ensemble |
| likely_fake_sounding_errors | Treating the bell as a metronome click rather than as a played, humanly struck instrument with its own small timing character; using one sample for both lobes; resetting round robins every cycle, which is exactly the point in the piece a listener attends to most. | inference |
| organic_programming_methods | Model the bell's timing as the reference the rest of the ensemble is heard against, per `COMMON_ERRORS.md` item 13: it normally carries no `timing_character` deviation of its own (`marker_parts_excluded`), unless a named measured template for the specific piece is being followed (see `shared/MUSICAL_SYSTEMS/EWE_DANCE_DRUMMING.md` on the four-and-six matrix). | sourced: LOCKE-AGBADZA-2012 |

### Axatse (gourd rattle)

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A dried gourd covered with an external net of strung beads or seeds; sound comes from the beads striking the gourd's shell as the player moves it, and separately from the gourd striking the player's body. | sourced: LOCKE-YEWEVU-2010; LADZEKPO-AMD |
| attack_behavior | The player moves the rattle in a fixed repeating pattern of downstrokes (gourd hits the player's own thigh) and upstrokes (gourd hits the player's own weak-hand palm); each contact is a distinct, differently-timbred attack. | sourced: LOCKE-AGBADZA-2012 |
| sustain_behavior | The beads continue to hiss briefly after a strike from residual motion; the dominant sound is the contact transient. | inference |
| release_behavior | No separate release action; decay is passive. | inference |
| dynamic_timbre_change | Not addressed directly; a harder strike against thigh or palm is plausibly louder and brighter, following the same struck-object logic as other shaken and struck idiophones. | inference |
| register_character | Not a pitched instrument in the melodic sense; a fixed, noise-like timbre. | inference |
| practical_range | Not applicable; unpitched. | inference |
| tessitura | Not applicable. | inference |
| articulation_logic | Two articulations from one repeating physical figure: a **downstroke** (against the thigh, in unison with the bell) and an **upstroke** (against the palm, between bell strokes); described kinesthetic pattern for one agbadza rattle phrase: down-up-down-down-up-down-up-down-up-down-down. | sourced: LOCKE-AGBADZA-2012 |
| phrase_limits | Continuous for the duration of a piece, like the bell; bounded by the player's stamina rather than breath. | inference |
| transitions | No legato; each stroke is a discrete contact. | inference |
| repeated_note_behavior | The pattern repeats every cycle without special retriggering technique reported. | inference |
| vibrato | Not applicable. | inference |
| pitch_instability | Not applicable; unpitched. | inference |
| resonance | The gourd's cavity shapes the bead-on-shell timbre; not measured in the sources read. | inference |
| physical_noise | The thigh- and palm-contact sounds are two of the instrument's core timbres, not incidental noise; see articulation_logic. | sourced: LOCKE-AGBADZA-2012 |
| feasibility | One hand holds and swings the rattle; the down-up figure sets a practical speed ceiling tied to arm motion, not finger independence. | inference |
| ensemble_behavior | Downstrokes lock to the bell (in unison with it); upstrokes fall between bell strokes and create a distinct two-then-three counter-accent against the common three-then-two handclap pattern. Normally many rattles play in unison on a piece, in enough numbers that the massed rattle sound can outweigh the solitary bell in the mix. | sourced: LOCKE-AGBADZA-2012 |
| recording_behavior | Not addressed by the sources read; described in performance as a section of several players rather than a solo part. | sourced: LOCKE-AGBADZA-2012 + inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short, non-sustaining hits per stroke. | inference |
| overlap | Not a legato instrument. | inference |
| velocity | Should select loudness within one stroke type; downstroke and upstroke are different recorded timbres, not velocity layers of one sample. | inference |
| continuous_dynamics | Not applicable to discrete strokes. | inference |
| expression | Not the primary control. | inference |
| articulation_switching | Two articulations (downstroke against thigh, upstroke against palm), each its own recording. | sourced: LOCKE-AGBADZA-2012 |
| round_robins | Needed, for the same reason as the bell: a short figure repeated for the length of a piece. | inference |
| release_samples | Not applicable. | inference |
| pedal_or_breath_behavior | Not applicable. | inference |
| transition_samples | Not applicable. | inference |
| mic_or_room_behavior | Ensemble performance normally uses several rattle players at once; a single sampled rattle stacked in unison undersells the real section's mass and phase spread. | inference |
| likely_fake_sounding_errors | One rattle sample standing in for the massed-rattle section sound; collapsing the downstroke/upstroke distinction into one timbre; losing the two-then-three counter-accent against the handclap by quantising both to the same grid position. | inference |
| organic_programming_methods | Where the part represents several rattle players, use `ensemble_spread` (`shared/HUMAN_PERFORMANCE_SCHEMA.md` section 3) for the small, deliberate spread among players who lock to the same bell; keep downstrokes aligned to the bell as a non-marker but tightly bell-linked part. | inference |

### Kagan and Kidi (support and response drums)

Both are single-headed, barrel-bodied drums struck with two wooden sticks, smaller and
higher-pitched than the lead drum; they differ mainly in size, pitch, and musical role, so they
share one card, with the differences stated per row. **Kagan** is the smaller, higher-pitched
support drum that marks offbeats; **kidi** is the larger, lower-pitched response drum that answers
the lead drummer's calls. In the Yewevu ensemble instrumentation Locke describes (cited here only
for its general organology, not its repertoire) a comparable high-pitched pair is called
**kaganu**/**adzida**; naming and exact drum count vary by repertoire and ensemble. | sourced:
LOCKE-YEWEVU-2010

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A single membrane head, described elsewhere in the ensemble's instrumentation as goat skin, stretched over a barrel-shaped body, struck with two straight wooden sticks. | sourced: LOCKE-YEWEVU-2010 |
| attack_behavior | Two named stroke types on kidi: a **bounce** stroke (stick rebounds off the head, resonant, louder) and a **press** stroke (stick is held against the head, muted, much quieter). Kagan is played with flat stick strikes that give a dry, "rim shot"-like attack. | sourced: LOCKE-AGBADZA-2012 |
| sustain_behavior | A bounce stroke lets the head ring briefly; a press stroke damps it almost immediately at the point of contact. | sourced: LOCKE-AGBADZA-2012 |
| release_behavior | As sustain_behavior: the bounce/press distinction is also the release distinction. | sourced: LOCKE-AGBADZA-2012 |
| dynamic_timbre_change | Not separately measured; press strokes are reported as quieter as well as shorter than bounce strokes. | sourced: LOCKE-AGBADZA-2012 |
| register_character | Kagan sits high and slender in pitch and timbre, cutting through the texture; kidi is medium-pitched and more resonant/mellow than kagan, lower-pitched and more resonant than kagan but higher than the lead drum. | sourced: LOCKE-AGBADZA-2012 |
| practical_range | Not a melodic pitch range; each drum has one head tuned to its own relative pitch level within the ensemble (kagan highest of the pair, kidi in the middle of the ensemble's overall pitch layout). Absolute tuning method not found in the sources read. | sourced: LOCKE-AGBADZA-2012 + to-verify: what would settle this is not recorded |
| tessitura | Each drum plays in its own fixed relative register throughout a piece; there is no register change within a performance. | inference |
| articulation_logic | Kidi's phrases are built from bounce and press strokes in specific, memorised patterns ("themes"); kagan's part is comparatively simple, built from flat stick strikes marking offbeats, e.g. a widely used figure striking the second and third eighth notes within each dotted-quarter beat. | sourced: LOCKE-AGBADZA-2012 |
| phrase_limits | Both play continuously once the time parts enter; bounded by stick-hand endurance and alternation speed, not breath. | inference |
| transitions | No legato; every stroke is a discrete stick attack. | inference |
| repeated_note_behavior | Fast repeated bounce strokes are produced by stick alternation or single-hand rebound; not separately analysed for either drum in the sources read. | inference |
| vibrato | Not applicable. | inference |
| pitch_instability | Not addressed for either drum in the sources read beyond the bounce/press distinction, which is a timbre and duration change rather than a described pitch bend. | to-verify: whether pressing the stick into the head, or hand pressure on the rim, measurably bends kidi's or kagan's pitch, the way it does on some other Ewe drums (see atsimevu's finger-pressure technique on this page) |
| resonance | Barrel body and single head; no sympathetic strings or second resonating head are described. | inference |
| physical_noise | Stick-on-skin attack noise is part of both drums' identity, especially kagan's dry "rim shot" quality. | sourced: LOCKE-AGBADZA-2012 |
| feasibility | Two sticks, two hands; a kidi or kagan phrase demanding the same stick strike faster than a player can physically re-strike, or more than two simultaneous strikes, is not playable. | inference |
| ensemble_behavior | **Kidi is a response drum: it answers the lead drummer's (sogo's) calls**, choosing among a memorised inventory of response themes tied to particular calls and to specific positions in the bell phrase, rather than either free improvisation or one unchanging, never-varying ostinato. A prior version of this page's family file stated flatly that Ewe support parts do not improvise; that is corrected here: kidi's answering is bounded and repertoire-based, but it is a real, active response to what the lead plays, not inert repetition. Kagan's part is comparatively fixed within a piece and functions mainly as a steady offbeat marker against which the rest of the texture is heard. | sourced: LOCKE-AGBADZA-2012 |
| recording_behavior | Not addressed by the sources read; performed as ensemble parts rather than solo instruments. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short, struck notes; note length should not be used to fake sustain since both drums' sustain is set by the stroke type, not by held duration. | inference |
| overlap | Not a legato instrument. | inference |
| velocity | Should primarily select **which stroke** (bounce versus press on kidi; the flat strike on kagan) rather than only loudness within one recorded stroke. | sourced: LOCKE-AGBADZA-2012 |
| continuous_dynamics | Not applicable to discrete strokes. | inference |
| expression | Not the primary control. | inference |
| articulation_switching | Kidi needs at minimum two articulations (bounce, press), each a separate recording, since a press stroke is not a turned-down bounce stroke; kagan needs its flat-strike articulation. | sourced: LOCKE-AGBADZA-2012 |
| round_robins | Needed for both; response-drum themes and the kagan offbeat figure repeat for a piece's whole duration. | inference |
| release_samples | Kidi's press stroke is effectively its own release behaviour (an immediate hand/stick-damped stop) rather than a separate release layer on the bounce sample; treat bounce and press as different note events, not one sample with two release settings. | sourced: LOCKE-AGBADZA-2012 |
| pedal_or_breath_behavior | Not applicable. | inference |
| transition_samples | Not applicable; no slides between strokes are documented. | inference |
| mic_or_room_behavior | Not addressed by the sources read. | to-verify: conventional close- versus ensemble-miking for kidi and kagan |
| likely_fake_sounding_errors | Kidi played as one fixed ostinato with no relationship to what the lead drum is calling; a press stroke rendered as a turned-down bounce sample instead of a genuinely damped recording; kagan's dry offbeat figure smoothed into a generic hi-hat-like pattern that loses the flat-stick "rim shot" timbre. | inference |
| organic_programming_methods | Program kidi's theme choice as a response to the lead drum's specific calls, from the response-drum inventory for the piece, rather than a fixed loop (`shared/HUMAN_PERFORMANCE_SCHEMA.md` performance_reference names the repertoire and basis this was modelled on); keep kagan steady as a secondary time-keeping part, with `metrical_accent` shaping its offbeat strokes rather than uniform velocity. | sourced: LOCKE-AGBADZA-2012 + inference |

### Sogo (barrel lead drum)

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A single-headed barrel drum, lower-pitched than kidi and kagan, played in agbadza with two bare hands. In the Yewevu ensemble's instrumentation, by contrast, this size of drum (called agbivu or sogo there) is played with two straight sticks, or one stick and one bare hand; which technique applies is repertoire-specific and should not be assumed from the drum's name alone. | sourced: LOCKE-AGBADZA-2012; LOCKE-YEWEVU-2010 |
| attack_behavior | Four named bare-hand strokes in agbadza, each a distinct hand technique and contact point (see articulation_logic). When not playing the lead part, sogo may double the response drum's part instead. | sourced: LOCKE-AGBADZA-2012; LOCKE-YEWEVU-2010 |
| sustain_behavior | Open ("de") and bass ("ga") strokes let the head ring; press ("dzi") strokes damp it at contact. | sourced: LOCKE-AGBADZA-2012 |
| release_behavior | As sustain_behavior; the stroke type sets the release, not a separate action. | sourced: LOCKE-AGBADZA-2012 |
| dynamic_timbre_change | The bass ("ga") and slap ("tsa") strokes are described as full- and variable-volume strokes respectively, each with its own fixed timbre, rather than one timbre played at different loudnesses. | sourced: LOCKE-AGBADZA-2012 |
| register_character | Sogo's low pitch and bare-hand palette give it the widest range of musical effects in the ensemble; it is described as having the greatest freedom for musical invention of any part. | sourced: LOCKE-AGBADZA-2012 |
| practical_range | Not a melodic pitch range: four relative tone/timbre categories (bass, open, mute/press, slap) rather than a scale. Absolute tuning mechanism not found in the sources read. | sourced: LOCKE-AGBADZA-2012 + to-verify: what would settle this is not recorded |
| tessitura | Sits in its own low register for the whole piece. | inference |
| articulation_logic | Four bare-hand strokes, with their vocable names, hand, contact and typical loudness: **ga** (bass tone, low pitch, strong-hand palm, bounce, full volume), **de** (open tone, middle pitch, strong-hand finger bounce, full volume), **dzi** (mute tone, high pitch, either hand, finger press, full volume), **tsa** (slap tone, high pitch, either hand, finger slap, variable volume). Ewe drummers vocalise these as a system of oral notation for teaching and composing lead-drum phrases. | sourced: LOCKE-AGBADZA-2012 |
| phrase_limits | Bounded by hand-alternation speed and by the piece's form (introduction, main playing, a fixed ending signal) rather than by breath. | sourced: LOCKE-AGBADZA-2012 |
| transitions | No legato; every stroke is a discrete hand contact, though fast successive strokes can blur toward a continuous roll (see repeated_note_behavior). | inference |
| repeated_note_behavior | Rolling passages of fast repeated strokes are a distinct, named device sogo uses to cue dancers (for example, to signal them to get ready, or to shape the dance space), not an incidental effect of speed. | sourced: LOCKE-AGBADZA-2012 |
| vibrato | Not applicable. | inference |
| pitch_instability | Not separately analysed beyond the four discrete stroke categories. | to-verify: whether hand or finger pressure bends sogo's pitch continuously, as documented for atsimevu on this page |
| resonance | Barrel body, single head; not otherwise measured in the sources read. | inference |
| physical_noise | Bare-hand-on-skin contact sound is part of the instrument's identity, distinct from a stick attack. | inference |
| feasibility | Two bare hands; a phrase demanding a third simultaneous contact, or the same hand re-striking faster than physically possible, is not playable. | inference |
| ensemble_behavior | Sogo is the lead drum and ensemble leader ("soloist"): it calls, and kidi answers (see the kidi card). Its solo line also complements the singers' tune. Experienced players additionally vocalise drum-language phrases with the mouth as a teaching device ("beating the drum with your mouth"). A fixed ending-signal phrase closes the piece. | sourced: LOCKE-AGBADZA-2012 |
| recording_behavior | Not addressed by the sources read. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short, struck or slapped notes; length in the sequencer should not extend the natural decay, which the stroke type sets. | inference |
| overlap | Not a legato instrument. | inference |
| velocity | Should primarily select which of the four strokes (ga, de, dzi, tsa) is triggered; only tsa (slap) is documented as varying in loudness within its own type. | sourced: LOCKE-AGBADZA-2012 |
| continuous_dynamics | Not applicable to discrete hand strokes. | inference |
| expression | Not the primary control. | inference |
| articulation_switching | At minimum four articulations (ga, de, dzi, tsa), each its own recording; where the alternative stick or stick-and-hand technique from a different repertoire is modelled, that is a further, separate articulation set, not a substitute for the bare-hand one. | sourced: LOCKE-AGBADZA-2012; LOCKE-YEWEVU-2010 |
| round_robins | Needed: sogo recycles standard phrases extensively through a performance. | inference |
| release_samples | dzi (press) is effectively its own release/damping behaviour and should not be represented as a turned-down de (open) sample. | sourced: LOCKE-AGBADZA-2012 |
| pedal_or_breath_behavior | Not applicable. | inference |
| transition_samples | Not applicable; no slides between strokes are documented. | inference |
| mic_or_room_behavior | Not addressed by the sources read. | to-verify: what would settle this is not recorded |
| likely_fake_sounding_errors | Collapsing the four-stroke vocabulary into one sample played at different velocities; using stick-drum samples for a bare-hand agbadza sogo part or vice versa without naming which repertoire's technique is intended; smoothing out the rolling dancer-cue passages into generic fast rolls with no structural function. | inference |
| organic_programming_methods | Build lead-drum phrases from the named stroke vocabulary rather than from generic velocity variation; treat rolling passages as a structural device (a cue), placed where the form calls for one, not scattered for density; where sogo doubles the response-drum part, use kidi's articulation logic for that passage, not sogo's own lead vocabulary. | sourced: LOCKE-AGBADZA-2012 |

### Atsimevu (tall lead drum)

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A carved cylindrical body about four and a half feet tall, expanding to roughly fifteen inches in diameter at the middle, with a drum head about nine inches in diameter, traditionally a deer or antelope skin, and an opening of about eight inches at the bottom that lets the internal air-column vibration out. The drum is tilted into playing position by a stand called **vudetsi**. | sourced: LADZEKPO-AMD |
| attack_behavior | Three families of initiating technique: a full bare-hand strike, a full- or pressed-finger technique, and a stick technique (including a strike on the body itself, not the head; see articulation_logic). Struck at the head's centre (bare hand, basic stick) or its periphery (fingers), a position discovered by aligning the knuckles around the rim with the thumb as a guide. | sourced: LADZEKPO-AMD |
| sustain_behavior | Rebounding ("bouncing") strokes let the head, and the air column inside the body, ring; pressed strokes (fingers or stick held against the head) damp it at contact. | sourced: LADZEKPO-AMD |
| release_behavior | As sustain_behavior; players also control resonance duration directly by damping the periphery with light, firm weak-hand finger pressure after a stroke, described as the drum-language equivalent of closing the mouth after a spoken syllable. | sourced: LADZEKPO-AMD |
| dynamic_timbre_change | The alternate (pressed) stick technique is described as roughly half the intensity of the basic stick technique, at a higher pitch, not simply a quieter version of the same tone. | sourced: LADZEKPO-AMD |
| register_character | A pitch series from low (centre, bare hand) through middle (centre, basic stick or full fingers) to high (periphery, pressed fingers or pressed stick, or the body strike), used as a melodic-rhythmic vocabulary rather than a tuned scale. | sourced: LADZEKPO-AMD |
| practical_range | Not a melodic pitch range in the Western sense: eight distinct named pitches/timbres (plus two combined ones), fixed by technique and strike position rather than by fingering or embouchure. Absolute tuning mechanism for the head was not found in the sources read. | sourced: LADZEKPO-AMD + to-verify: what would settle this is not recorded |
| tessitura | The full pitch series is used throughout a piece; there is no register the technique avoids. | inference |
| articulation_logic | Named pitches and their technique, in the vocal syllables used for teaching and composing: **Ga** (lowest; full bare hand, centre, bounce), **Gi** (middle; full weak-hand fingers, periphery, bounce), **Ki** (higher than Gi; full weak-hand fingers, periphery, pressed), **De**/**Te**/**Ge** (middle; basic stick technique, centre, bounce; De and Te for the strong hand, Ge for the weak hand), **Tsi** (high; alternate stick technique, centre, pressed, about half the intensity of De), **To** (high; strong-hand stick bounces at centre while weak-hand fingers damp the periphery), **Ka** (high, clap-like; strong-hand stick strikes the body's expanded midsection, called **vukogo**, not the head, pressed against the body rather than rebounding). Two combined techniques stack Ka onto a hand-struck tone: **Dza** (Ga plus Ka, a denser low pitch) and **Dzi** (Ki plus Ka, a denser high pitch; note this atsimevu "Dzi" is a different technique from the like-sounding sogo stroke "dzi" on this page's Sogo card, and the two are not interchangeable). Duration modifiers exist for connecting tones at speed (**Gle**, **Vlo**) and for a short, damped duration on a single tone (an "n" suffix, e.g. **Ten**). | sourced: LADZEKPO-AMD |
| phrase_limits | Bounded by hand/stick alternation and by the piece's form; atsimevu's pitch series functions as **vugbe**, "drum speech," a surrogate for spoken language, so phrase boundaries follow linguistic-rhythmic phrasing as much as physical endurance. | sourced: LADZEKPO-AMD |
| transitions | No legato in the sustained-pitch sense; adjoining strokes at speed are named as connected figures (Gle, Vlo) rather than played as one continuous tone. | sourced: LADZEKPO-AMD |
| repeated_note_behavior | Not separately analysed beyond the general stroke vocabulary; fast alternation between named tones (Gle, Vlo) is the documented mechanism for speed. | sourced: LADZEKPO-AMD |
| vibrato | Not applicable. | inference |
| pitch_instability | The periphery-finger and periphery-stick techniques function partly as active pitch/timbre placement (a firm, controlled contact at a found angle) rather than incidental instability; no separate ongoing pitch-bend technique (in the sense of a continuously varying pitch after the attack) is documented. | sourced: LADZEKPO-AMD |
| resonance | The hollowed body's air column reinforces the head's vibration, most audibly for the lowest tone (Ga); the body's own material and construction quality are described as affecting the instrument's overall pitch character. | sourced: LADZEKPO-AMD |
| physical_noise | Not separately addressed beyond the stroke vocabulary itself, several of which (the pressed and body-strike techniques) are themselves noise-inflected, non-ringing sounds by design. | inference |
| feasibility | Two hands (one often on a stick, one bare or fingering) plus, for some techniques, simultaneous periphery damping with the weak hand while the strong hand strikes; a phrase requiring more simultaneous contacts than two hands allow is not playable. Good technique is described as relaxed support from the elbow with the actual stroke motion from the wrist, not the elbow, which bears on how fast and how long a part can be played convincingly. | sourced: LADZEKPO-AMD |
| ensemble_behavior | Atsimevu is "the most visible drum" among Anlo-Ewe instruments, by virtue of its lead-drum role in organising the ensembles it is featured in; as with sogo, the lead drum leads and the response and support drums answer and accompany it (see the kidi and kagan card). | sourced: LADZEKPO-AMD |
| recording_behavior | Not addressed by the sources read. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short, struck notes selected by technique, not extended by held note length. | inference |
| overlap | Not a legato instrument in the sustained-pitch sense; connected fast figures (Gle, Vlo) are named transitions between discrete tones, not a crossfaded glide. | sourced: LADZEKPO-AMD |
| velocity | Should primarily select among the named pitch/technique categories, not loudness within one sample; the alternate stick technique (Tsi) is specifically a different intensity **and** a different pitch from the basic one (De), not a soft De. | sourced: LADZEKPO-AMD |
| continuous_dynamics | Not applicable to discrete struck tones. | inference |
| expression | Not the primary control. | inference |
| articulation_switching | At minimum eight to ten articulations (the named tones Ga, Gi, Ki, De/Te/Ge, Tsi, To, Ka, plus the combined Dza and Dzi), each its own recording; the body-strike tone (Ka) in particular is acoustically a different instrument part (the shell, not the head) and must not be faked from a head sample. | sourced: LADZEKPO-AMD |
| round_robins | Needed: atsimevu recycles and varies its vocabulary extensively as the lead voice of a performance. | inference |
| release_samples | Pressed techniques (Ki, Tsi, To) are their own damped-release behaviour; the documented periphery-damping technique for shortening a tone ("n" suffix, e.g. Ten) is itself a distinct, controlled release action worth representing rather than only a fixed sample decay. | sourced: LADZEKPO-AMD |
| pedal_or_breath_behavior | Not applicable. | inference |
| transition_samples | The named fast connective figures Gle (De-to-Ge) and Vlo (Gi-to-De) are candidates for dedicated transition samples if a library records them; otherwise they are two closely sequenced discrete attacks, not a pitch glide. | sourced: LADZEKPO-AMD |
| mic_or_room_behavior | Not addressed by the sources read; the body strike (Ka) and the head strokes are acoustically different enough that separate close-miking is plausible. | inference |
| likely_fake_sounding_errors | Collapsing the eight-plus-tone vocabulary into a two- or three-velocity-layer patch; playing the body-strike tone (Ka) as a pitched or filtered head sample; treating "Dzi" the atsimevu combined tone and "dzi" the sogo stroke as the same sound because the vocable looks similar. | inference |
| organic_programming_methods | Program from the named tone vocabulary as a phrase grammar (the way a language's phonemes combine), not as a generic drum-roll patch; use the periphery-damping ("n" suffix) technique as a deliberate, notated shortening rather than a fixed release time; keep the body-strike tone (Ka) as its own articulation throughout. | sourced: LADZEKPO-AMD |

---

## Tradition and context

### Construction

Anlo-Ewe drums (**evu**) are traditionally a membrane fastened across the mouth of a cylindrical
body carved from a solid tree trunk; more recently, bodies are also made by coopering curved wooden
slats into a cylindrical shape and binding them with iron hoops. The principal instrument categories
are vibrating membranes (drums), vibrating metals (**gankogui**, the double bell, and **atoke**, a
separate boat-shaped bell not covered by a card on this page), and a vibrating gourd with an
external network of beads (**axatse**). Atsimevu's construction is documented in the most physical
detail of any instrument here: see its behaviour card for dimensions, head material, and the
**vudetsi** playing stand. [sourced: LADZEKPO-AMD; LOCKE-YEWEVU-2010]

### Tuning

No source read here gives a tensioning or tuning mechanism for any of these drum heads (rope
lacing, wooden pegs, or another method), despite fairly detailed technique descriptions for kidi,
sogo and atsimevu. What is documented is **relative pitch by drum**: within an ensemble, atsimevu
and sogo (as lead drums) sit lowest, kidi sits in the middle, and kagan sits highest, and this
relative ordering, not a set of absolute pitches, is what a part needs to respect. Absolute or
even approximately measured pitches for any of these drums were not found. [sourced: LOCKE-AGBADZA-2012 + to-verify: in a source
that addresses drum construction and tuning directly]

### Note production and technique

Every drum here is single-headed and struck, never bowed or blown. The two lead drums (sogo,
atsimevu) carry the most elaborate technique vocabularies, each a named set of hand, finger, and
stick strokes tied to distinct pitches and timbres and taught through vocal syllables (vocables) as
a system of oral notation; see the Sogo and Atsimevu cards for the full stroke vocabularies. The
support and response drums (kagan, kidi) use a simpler two-way distinction, bounce versus press,
built from stick technique. The bell (gankogui) and rattle (axatse) are struck idiophones with no
comparable multi-stroke pitch vocabulary; their variety comes from which part of the instrument is
struck (which lobe of the bell; thigh versus palm for the rattle) rather than from a graded stroke
system. [sourced: LOCKE-AGBADZA-2012; LADZEKPO-AMD]

### Idiomatic phrasing and ornamentation

The tradition's own framing of the lead drum's pitch vocabulary as **vugbe**, "drum speech," is not
decorative language: the drum is described as a surrogate for the human voice, and its phrases are
read and taught as a kind of speech built from named syllables (vocables), with grammar-like
connective figures (Gle, Vlo) and a controlled-duration marker (the "n" suffix) that is explicitly
compared to closing the mouth after a word. Reducing this to "hits at different velocities" removes
the level at which the part is actually organised. On the response side, kidi does not ornament a
melody; it selects among a memorised inventory of response themes keyed to the lead's calls and to
specific points in the bell phrase, which is the tradition's own form of "ornamentation" for a
supporting part: bounded choice, not free decoration and not silence. [sourced: LADZEKPO-AMD; LOCKE-AGBADZA-2012]

### Performer interaction and ensemble role

The lead drum (sogo or atsimevu, depending on the ensemble and piece) calls; the response drum
(kidi) answers, choosing its theme in relation to the call and to the bell; the support drum (kagan)
and the bell and rattle hold the steady time-keeping layer the other parts are read against. This is
a **corrected** picture relative to an earlier version of this pack's material, which stated that
supporting Ewe parts do not improvise. They do not improvise freely, and the bell, rattle, and kagan
parts are indeed close to fixed within a piece, but **kidi's answering is a real, bounded, responsive
practice**, not inert repetition, and sogo itself moves between leading and, when not leading,
doubling the response drum's part. The singers interact with the ensemble through their own
leader-and-group call-and-response, guided in tempo by the bell; that vocal material belongs to
`CHOIR_AND_VOICE.md` and the Vocal Director, not to this page. [sourced: LOCKE-AGBADZA-2012]

### Repertoire contexts

The technical material on this page is drawn from **agbadza**, a social and funerary dance-drumming
repertoire performed openly at community events, and secondarily from **Drum Gahu**, a purely
recreational social dance historically adopted from a neighbouring people; both are public, widely
taught, and the subject of published pedagogical transcription. This page does **not** draw
technique from **Yewevu**, the music of the Yeve religious order, as source material to imitate: see
"Restricted and ceremonial repertoire" below. Further named Ewe drums appear in the sources
(**boba**, **totodzi**, **kroboto**, and the boat-shaped bell **atoke**) without enough detail read
here to card them; they are not covered by this page. [sourced: LOCKE-AGBADZA-2012; LADZEKPO-AMD]

### Improvisation

Freedom in this ensemble is concentrated in the lead drum, sogo or atsimevu, which recycles and
varies a vocabulary of known phrases; one documented lead player's style is described as drawing on
standard phrases for the great majority of playing time, with occasional bridges, rather than
continuous invention. The lead drummer also uses specific rolling passages as dancer cues (not
generic fills) and closes a piece with a fixed ending-signal phrase. Kidi's responsive theme choice,
discussed above, is a second, more bounded site of choice: real but constrained, answering the lead
rather than leading. Bell, rattle, and kagan are not documented as improvising within a piece.
[sourced: LOCKE-AGBADZA-2012; JOHNSTON-2024]

---

## What the instrument is

This is not one instrument but a stratified ensemble: two fixed-pitch idiophones (bell, rattle) that
hold the timeline layer, two barrel drums (kagan, kidi) that hold and answer within a fixed
supporting layer, and one or two bare-hand or stick-and-hand lead drums (sogo, atsimevu) that carry
the piece's most elaborate, speech-like pitch vocabulary and its improvisational freedom. Every part
is timbrally distinct by design, which is how a listener separates the layers in the mix.
[sourced: LOCKE-AGBADZA-2012; LADZEKPO-AMD]

## Range and register

Not a Western pitch range on any instrument here. The bell has two fixed relative pitches; the
rattle is unpitched; kagan, kidi, sogo and atsimevu each carry a small set of named relative
pitches/timbres set by strike technique and position, ordered from lowest (atsimevu/sogo) to highest
(kagan) across the ensemble. No absolute or cents-referenced pitch data was found in the sources
read for any instrument on this page. [sourced: LOCKE-AGBADZA-2012; LADZEKPO-AMD + to-verify: what would settle this is not recorded]

## Articulation and note transitions

No instrument here is legato in the sustained-pitch, crossfaded sense. Kagan and kidi distinguish
bounce (resonant) from press (muted) strokes; sogo distinguishes four bare-hand strokes (ga, de, dzi,
tsa); atsimevu distinguishes eight-plus named strokes across bare hand, fingers, and stick,
including a strike on the drum's body rather than its head. Fast connective figures exist (sogo's
rolling passages; atsimevu's Gle and Vlo) but these are sequences of discrete attacks played close
together, not a glide between two sustained pitches. [sourced: LOCKE-AGBADZA-2012; LADZEKPO-AMD]

## Physical constraints

Every drum here is played with at most two simultaneous points of contact (two hands, two sticks, or
one of each), so a written part asking for more simultaneous strikes than the player has hands, or
the same hand/stick re-striking faster than is physically possible, is not playable. Atsimevu adds a
documented posture constraint: good technique is described as a relaxed, elbow-supported arm with
the actual stroke driven from the wrist, which bears on sustainable speed and endurance for that
instrument specifically. [sourced: LADZEKPO-AMD]

## Phrase behaviour

The bell, rattle, and kagan play essentially continuously once the time parts enter, for the
duration of a piece, with no reported rest. The lead drum's phrasing follows the piece's form
(introduction, main body, dancer cues, a fixed ending signal) and, on atsimevu, is explicitly
compared to spoken phrasing (vugbe, "drum speech"), with its own duration-shortening device (the "n"
suffix) likened to closing the mouth after a syllable. [sourced: LOCKE-AGBADZA-2012; LADZEKPO-AMD]

## Ensemble behaviour

Stratified and interlocking, all ultimately measured against the bell: bell and rattle (plus
handclaps, not covered on this page) hold the timeline; kagan holds a steady offbeat layer; kidi
holds and actively answers, from a memorised theme inventory, in relation to the lead drum's calls;
sogo and/or atsimevu lead, call, and, when not leading, may double the response drum's part instead.
[sourced: LOCKE-AGBADZA-2012]

## Recording behaviour

Not addressed in the sources read for any instrument here beyond the observation that axatse is
normally played by several performers at once, in numbers that can outweigh the solitary bell in the
overall mix. [sourced: LOCKE-AGBADZA-2012]

## Programming it: the control model

```text
velocity: selects which named stroke/technique fires (not primarily loudness within one stroke)
articulation_switching: one articulation per named stroke; press/muted strokes are not a turned-down
  copy of an open/bounce stroke
round_robins: essential on every part; the ensemble repeats short figures for a piece's whole length
marker_parts: the bell (gankogui) carries no expressive timing deviation of its own by default
response_logic: kidi's part should be chosen in relation to the lead drum's calls for the piece being
  modelled, not treated as an independent fixed loop
```
[inference]

## Programming it: what makes it sound real

- Identify which repertoire (agbadza, Gahu, or another named, secular piece) and which lead drum
  (sogo or atsimevu) a part is modelling before writing anything; the same-named drum's technique
  (bare hand versus stick) is not constant across repertoires. [sourced: LOCKE-AGBADZA-2012; LOCKE-YEWEVU-2010]
- Use each instrument's named stroke vocabulary as the articulation set, not a generic
  "ethnic drum" patch with velocity layers standing in for genuinely different strokes.
  [sourced: LOCKE-AGBADZA-2012; LADZEKPO-AMD]
- Write kidi's part as a response to specific sogo or atsimevu calls, chosen from the response
  inventory, rather than as an independent ostinato. [sourced: LOCKE-AGBADZA-2012]
- Keep the bell steady as the reference the rest of the ensemble is heard against, per
  `COMMON_ERRORS.md` item 13, unless a named measured feel template for the specific piece is being
  followed. [sourced: LOCKE-AGBADZA-2012]
- Use sogo's rolling passages and its fixed ending signal as structural devices tied to the piece's
  form (a dancer cue, a close), not as generic fills scattered for density. [sourced: LOCKE-AGBADZA-2012]

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Family-specific tells:

- kidi (or any response part) looping one fixed pattern with no audible relationship to the lead
  drum's calls; [sourced: LOCKE-AGBADZA-2012]
- sogo's or atsimevu's stroke vocabulary collapsed into two or three velocity layers instead of the
  four-plus and eight-plus named strokes documented on their cards; [sourced: LOCKE-AGBADZA-2012; LADZEKPO-AMD]
- atsimevu's body-strike tone (Ka) played as a pitched or filtered head sample instead of a
  distinct shell-strike recording; [sourced: LADZEKPO-AMD]
- a generic hand-drum or "African percussion" patch standing in for this specific, named ensemble,
  which is the failure `shared/MUSICAL_SYSTEMS/INDEX.md` rule 2 names. [inference]

## What virtual implementations commonly get wrong

The most common failure is exactly the one `CULTURALLY_SPECIFIC_INSTRUMENTS.md` names: a
twelve-tone-equal-adjacent sample patch standing in for all six of these instruments, played with
uniform velocity and no relationship between the "lead" and "response" tracks. The specific,
correctable version of that failure here is **flattening the call-and-response relationship between
sogo/atsimevu and kidi into two independently looping parts**, which removes the one piece of
ensemble logic these sources document most clearly. A second common failure is treating drum
technique as portable across repertoires: this page found sogo played bare-handed in agbadza and
with sticks (or stick-and-hand) in the Yewevu ensemble Locke describes, which means "sogo" alone
does not specify a technique. [sourced: LOCKE-AGBADZA-2012; LOCKE-YEWEVU-2010]

## What must not be generalised outside the tradition

- **Ewe dance-drumming is not "African percussion" and not interchangeable with Mande jembe music or
  any other West African ensemble tradition.** See `JEMBE_AND_DUNUN.md` for a differently constructed,
  differently played ensemble from a different people, region, and repertoire. [sourced: LOCKE-AGBADZA-2012; POLAK-JEMBE-2010]
- The four-stroke sogo vocabulary and the eight-plus-stroke atsimevu vocabulary documented here are
  specific to those instruments in the repertoires read (mainly agbadza); do not assume every Ewe
  drum, or every lead drum in the wider region, shares this exact stroke set. [sourced: LOCKE-AGBADZA-2012; LADZEKPO-AMD]
- Do not extend the bare-hand sogo technique documented for agbadza to every piece that uses a
  sogo-sized drum: the Yewevu ensemble instrumentation Locke describes uses sticks, or stick and
  hand, for the comparable drum. [sourced: LOCKE-YEWEVU-2010]
- Boba, totodzi, kroboto and atoke are named in the sources as further instruments of this tradition
  but are not documented in enough depth here to generalise about; they are not covered by this
  page's cards, and nothing on this page should be read as describing them. [sourced: LADZEKPO-AMD]

## Restricted and ceremonial repertoire

**Yewevu, the drumming, singing, and dance of the Yeve religious order, is restricted and this page
declines it as source material to imitate or sample, per `shared/MUSICAL_SYSTEMS/INDEX.md` rule 5.**
Locke's own account, written with the consent of his teacher, states this plainly: Yewe is
"shrouded with secrecy and mystery," knowledge is withheld from the uninitiated, practitioners
"zealously guard their cultural heritage," and "many musical experts refuse to teach it." Locke
himself agreed with his teacher not to seek deep knowledge of Yewe as a religious system, and the
version of Yewevu documented in his article is explicitly a staged, folkloric-troupe arrangement
several removes from shrine practice, offered for its "affective presence" and its analytical value
for the metric-matrix theory, not as performance material for outsiders to reproduce. This page
therefore cites Locke's Yewevu article only for general, non-repertoire ensemble-instrumentation
facts (which instruments are used, and roughly how), never for a Yewevu piece's actual musical
content. **The adjacent, non-restricted repertoire this page draws its technique from instead is
agbadza (public, social and funerary) and Drum Gahu (public, purely recreational).** If a request
specifically asks for Yewevu material, the studio says so and offers agbadza or Gahu instead; where
it is unclear whether a requested Ewe piece is restricted, the studio asks rather than proceeding.
[sourced: LOCKE-YEWEVU-2010]

## What the Performance Director needs from this file

- `performance_reference` should name the specific repertoire (agbadza, Gahu, or another named
  secular piece) and, where relevant, which lead drum (sogo or atsimevu), since technique is not
  constant across repertoires for a same-named drum.
- `marker_parts_excluded` should include the bell (gankogui) by default, per `COMMON_ERRORS.md` item
  13, unless a named measured feel template for the specific piece calls for otherwise.
- `articulation_unavailable` is the expected outcome when a general-purpose percussion library is
  asked for kidi's response-theme vocabulary, sogo's four-stroke vocabulary, or atsimevu's
  eight-plus-stroke vocabulary; report it rather than substituting a generic stroke.
- Any request for Yewevu-specific repertoire content routes to "Restricted and ceremonial
  repertoire" above; the feasibility report should record `blocked` with that reason rather than
  proceeding.
- Kidi's part should be planned in relation to the lead drum's calls for the specific piece, not
  generated independently.

## Sources and what to verify

Full citations and read depth are in `research/sources/INSTRUMENT_SOURCES.md`; the claims and their scope and
limits, record by record, are in `research/instruments/EWE_DANCE_DRUMS.md`. In summary: the strongest, most
detailed material on this page is David Locke's critical edition of Agbadza, an ethnomusicological
transcription built on a named, credited apprenticeship, read at section depth for its construction,
technique, and ensemble-behaviour content; and C. K. Ladzekpo's own teaching pages on atsimevu and
Ewe drum construction generally, a practitioner's first-person account, read in full. Locke's Yewevu
article was read at section depth for general ensemble instrumentation only, deliberately excluding
its Yewevu repertoire content. Johnston's comparative study was read at section depth for its agbadza
material only, not for its unrelated Yoruba dùndún or Akan adowa examples, which are out of scope
for this page. Agawu's article on the standard pattern could not be reached (a bot-check page was
returned instead of the article) and is cited only as `standard-reference`, not read.

**To verify, before this page's claims are extended further:** the head-tensioning and tuning
mechanism for any of these drums; any absolute or cents-referenced pitch data; a bell-technique
source that addresses muting or dynamic timbre change directly, since none of the sources read
described one; and conventional recording/miking practice for the ensemble, which none of the
sources read addressed.
