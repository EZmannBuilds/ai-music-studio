# Brass

Horn in F (double horn), trumpet (B-flat and C), tenor and bass trombone, and tuba. Euphonium and
cornet are close relatives of trombone and trumpet respectively and are not covered as separate cards
here; their behaviour mostly follows the nearer relative. Non-Western brass and natural (valveless)
horn and trumpet are out of scope; see `CULTURALLY_SPECIFIC_INSTRUMENTS.md`.

> Evidence: read at section depth: UNSW Music Acoustics' brass acoustics page (lip-reed mechanism,
> dynamic brightening, mute and stopped-horn acoustics), Hirschberg et al. 1996 on measured shock-wave
> formation in a trombone, a Horn Matters article on the stopping valve, Rimsky-Korsakov and Forsyth on
> stopped/muted brass, a PALNI brass-pedagogy chapter and an ITA-archived article on vibrato mechanisms,
> and a trumpet-pedagogy article on glissando mechanisms. One trumpet-mute source was reachable only as
> a search-engine excerpt (its page would not resolve directly) and is marked `excerpt` throughout.
> Practical ranges remain `standard-reference`, attributed to Adler and to Berlioz and Strauss, neither
> opened. Source IDs resolve in `research/sources/INSTRUMENT_SOURCES.md` (here, `research/sources/INSTRUMENT_SOURCES.md`);
> the claims and their limits are recorded in `research/instruments/BRASS.md` (here, `research/instruments/BRASS.md`).

Cross-family failures are in `COMMON_ERRORS.md`.

---

## Behaviour cards

### Horn (double horn, F and B-flat)

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A column of air in a long, mostly conical tube, excited by the lips acting as a pressure-controlled valve. The player selects a resonance (a partial) with embouchure tension; valves add tubing to change which harmonic series is available. A double horn gives the player two tubings (F and B-flat) selected by the thumb valve. | sourced: UNSW-BRASS |
| attack_behavior | Tongued or breath-only start; a quiet low entry speaks slowly, a loud high one has a hard front edge. The horn's partials sit closer together than the other brass in its main playing range, so attacks there are more prone to landing on the wrong partial ("cracking"). | sourced: UNSW-BRASS + inference |
| sustain_behavior | Sustained by continued breath and embouchure; pitch is a live joint decision, not a fixed mechanical state, so a held note drifts slightly without correction. | inference |
| release_behavior | Audible, unless deliberately choked with the hand or tongue-stopped; a release carries the last breath's decay. | inference |
| dynamic_timbre_change | Louder playing drives the lips into sharper, more nonlinear closure, adding high harmonics; the horn brightens with dynamic like the rest of the family, though its narrower, more conical bore makes it generally mellower at a given dynamic than trumpet or trombone. | academic: UNSW-BRASS |
| register_character | Wide range; the upper middle is the singing, most-used register and also the most tiring. Low horn is broad and can be covered easily by other parts; very high horn is bright and effortful. | standard-reference: ADLER-ORCH; BERLIOZ-STRAUSS-TREATISE |
| practical_range | Written (F horn) roughly B1 to F5, sounding a perfect fifth lower, roughly E1 to B4. The B-flat side of a double horn adds security above the staff at the cost of the F side's characteristic dark low range; players choose sides note to note. | standard-reference: ADLER-ORCH; BERLIOZ-STRAUSS-TREATISE |
| tessitura | The comfortable, expressive tessitura sits in the upper-middle register (written roughly F3-C5); this is also where fatigue accumulates fastest. | inference |
| articulation_logic | Tongued, slurred, accented, flutter-tongued; falls, rips and doits exist but are less idiomatic than on trumpet because the horn lacks valve slides usable for a true glissando (see `transitions`). | inference |
| phrase_limits | A phrase is a breath. Register and endurance interact: a passage comfortable once is not comfortable across sixteen bars, especially in the upper middle. | inference |
| transitions | Slurred: air keeps moving, lips/valves change pitch, no new attack. Lip trills exist and are easiest between adjacent partials in the upper middle register, most reliably as whole tones; lower down the partials are too far apart to trill with the lip alone. A true glissando is limited: the horn has no slide, so continuous pitch motion is a lip/hand gesture (see `pitch_instability`), not a valve-slide effect as on trumpet. | sourced: HORNMATTERS-STOPVALVE + inference |
| repeated_note_behavior | Single tonguing repeats reliably; rapid repeated notes are possible but the horn is not built for the speed a trumpet's smaller mouthpiece allows. | inference |
| vibrato | Most horn teachers do not teach vibrato as a default technique at all, unlike the rest of the brass family; where used, it is typically a slow hand or lip vibrato, applied by phrase rather than held constantly. | sourced: BRASSPED-PALNI |
| pitch_instability | Embouchure controls pitch continuously within a partial's range, so pitch can be "lipped" up or down around the nominal note; this is also how the old gradual (non-valve-era) hand-stopping glissando worked. Closely spaced partials in the main register raise real risk of landing on the wrong one. | sourced: FORSYTH-1914 + academic: UNSW-BRASS |
| resonance | Bell shape and hand position (even when not stopping) shape the radiated spectrum; a hand habitually rests in or near the bell on the horn, unlike other brass. | inference |
| physical_noise | Valve click, breath noise, and (for stopped notes) hand-on-bell friction. | inference |
| feasibility | One note per player; a horn "dyad" is two players. Stopped and muted notes are separate techniques from open playing and need setup. | inference |
| ensemble_behavior | Horns sit between woodwinds and heavy brass and are used to join the two; a horn section blends tightly with itself and is the traditional bridge voice in orchestration. | sourced: RIMSKY-1913 |
| recording_behavior | Often recorded bell-away or bells-up depending on hall and repertoire; distance changes the balance between direct buzz and hall reflection substantially because the bell is highly directional. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short notes take dynamics from velocity; a note held to the next attack with no gap loses its release. | inference |
| overlap | Legato patches are monophonic and need overlapping notes to trigger a recorded transition. | inference |
| velocity | Selects attack character/dynamic layer on short notes; on long notes it should not carry the whole dynamic. | inference |
| continuous_dynamics | Long notes take dynamics from a continuous controller that crossfades recorded dynamic layers, because loudness and brightness change together. | academic: UNSW-BRASS |
| expression | A separate trim control exists on documented libraries and is not the same as the dynamic-layer control. | inference |
| articulation_switching | Stopped horn and muted horn are separate sample sets or keyswitches, not a filter applied to the open patch. | sourced: RIMSKY-1913 + inference |
| round_robins | Exist to avoid repeated identical samples on repeated notes; do not reset every bar. | inference |
| release_samples | Present; a horn note's end is audible unless deliberately choked. | inference |
| pedal_or_breath_behavior | Breath noise is part of the instrument and should not be muted; there is no sustain pedal. | inference |
| transition_samples | Lip-trill and gliss transitions, where recorded, are separate from ordinary legato transitions. | inference |
| mic_or_room_behavior | Orchestral libraries are usually recorded at the section's hall position, already wide and reverberant, given the horn's directional bell. | inference |
| likely_fake_sounding_errors | Stopped horn and straight mute used interchangeably; a stopped-horn transposition ignored (see `Errors` below); flat sustains (error 2); lip trills written low, where partials are too far apart to trill. | to-verify: (stopped-horn transposition convention against a horn pedagogy source); inference (the rest) |
| organic_programming_methods | Draw a dynamic curve that brightens with level (cause: nonlinear lip closure, UNSW-BRASS). Model fatigue after a long loud high passage (cause: `performer_fatigue`, `HUMAN_PERFORMANCE_SCHEMA.md`). Keep stopped/muted changes plausible with rest bars for the switch. Do not align section attacks exactly (cause: `ensemble_spread`). | academic: UNSW-BRASS + inference |

### Trumpet (B-flat and C)

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A lip-reed valve exciting a mostly cylindrical bore (more cylindrical than horn or tuba), with three piston valves changing tube length. The more cylindrical bore is part of why trumpet and trombone show shock-wave brightening more readily than the more conical horn and tuba. | academic: UNSW-BRASS; HIRSCHBERG-1996 |
| attack_behavior | The smallest mouthpiece in the family, which is why only trumpet and cornet can execute genuine double and triple tonguing at speed and rapid tremolando. Attack hardens and brightens with dynamic and register. | sourced: RIMSKY-1913 |
| sustain_behavior | Held notes are not perfectly flat; air pressure and embouchure both drift slightly without correction. | inference |
| release_behavior | Audible unless deliberately clipped; a mute change requires the note to actually end first. | inference |
| dynamic_timbre_change | Brightens strongly with dynamic; at fortissimo the same nonlinear-propagation mechanism measured on trombone can push toward shock-wave formation in narrow cylindrical bore sections, which is the acoustic root of a "blatty" fortissimo trumpet sound. | academic: HIRSCHBERG-1996 |
| register_character | Thick and less agile at the bottom; brilliant and increasingly effortful above the staff. | standard-reference: ADLER-ORCH; BERLIOZ-STRAUSS-TREATISE |
| practical_range | Written roughly F#3 to C6 on both B-flat and C trumpet. The B-flat trumpet sounds a major second lower than written; the C trumpet sounds as written (non-transposing in pitch, though still "in C" by convention). | standard-reference: ADLER-ORCH; BERLIOZ-STRAUSS-TREATISE |
| tessitura | Comfortable, confident tessitura sits below the top of the staff; the top few notes above the staff are available but increasingly effortful and fatiguing. | inference |
| articulation_logic | Tongued (single/double/triple by speed), slurred, accented, flutter-tongued. Falls, rips and doits are gestures, not one mechanism: see `transitions`. | sourced: MODERNTRUMPET-GLISS + inference |
| phrase_limits | A phrase is a breath; the small mouthpiece does not change this. | inference |
| transitions | Slurred passages are a true legato with no new attack. Falls/doits/rips/glissandi are produced three different ways: embouchure-only "lipping" (small intervals, asymmetrically easier lipping down than up), first/third valve-slide glissando (true pitch-continuous, limited to a minor second or smaller), and half-valve technique (partially depressed valve, gives a semi-pure glissando across larger intervals by deliberately mistuning the bore, with audible harmonic "breaks" possible). A harmonic-series overtone glissando (jumping cleanly between partials with no valve or lip change) is a fourth, more limited option, usable only where the needed partials happen to lie between the start and end pitch. | sourced: MODERNTRUMPET-GLISS + academic: UNSW-BRASS |
| repeated_note_behavior | Single tonguing repeats reliably at speed; double/triple tonguing allow genuinely fast repeated-note passages unavailable to the rest of the family (bar the horn, marginally). | sourced: RIMSKY-1913 |
| vibrato | Style-dependent and instrument-specific in mechanism: jazz players commonly favour lip vibrato, classical/orchestral players more often favour hand vibrato (rocking the horn slightly, commonly with the right-hand pinky through the finger hook), and jaw vibrato is also used. Vibrato is a phrase decision, not constant. | sourced: BRASSPED-PALNI |
| pitch_instability | Embouchure lips notes up or down around the resonance; half-valve fingering deliberately destabilises pitch for effect. | sourced: MODERNTRUMPET-GLISS + academic: UNSW-BRASS |
| resonance | Bell and mute interact strongly; mutes introduce their own resonant formants (see `Programming it`). | academic: UNSW-BRASS |
| physical_noise | Valve click and breath noise; mute insertion/removal noise if not muted between phrases. | inference |
| feasibility | One note per player; a "trumpet dyad" is two players. Mute changes need rest bars. | inference |
| ensemble_behavior | The brightest, most cutting voice in the brass section; traditionally the section's melodic lead in tutti brass writing. | sourced: RIMSKY-1913 |
| recording_behavior | Highly directional; close mics capture bell buzz and valve noise, distant mics capture the room the trumpet is driving. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short notes from velocity; notes glued end to end lose the release. | inference |
| overlap | Legato patches monophonic, need overlap to trigger a recorded transition. | inference |
| velocity | May select attack type as well as loudness on short-note patches. | inference |
| continuous_dynamics | Long notes need a crossfading dynamic-layer control so brightness tracks level, especially given how strongly trumpet brightens. | academic: UNSW-BRASS; HIRSCHBERG-1996 |
| expression | Separate trim control, distinct from the dynamic-layer control. | inference |
| articulation_switching | Mutes are separate sample sets or keyswitches; half-valve and lip-bend effects, where sampled at all, are separate patches, not a pitch-bend applied to an open patch. | sourced: MODERNTRUMPET-GLISS + inference |
| round_robins | Prevent machine-gun repeats on the family's fastest, most repeat-capable instrument. | inference |
| release_samples | Present; matters especially for short, tongued figures. | inference |
| pedal_or_breath_behavior | Breath and valve noise are part of the instrument. | inference |
| transition_samples | Where sampled, valve-slide and half-valve glissandi are distinct transition types from a slurred legato. | sourced: MODERNTRUMPET-GLISS |
| mic_or_room_behavior | Close mics foreground valve and breath noise; section patches are usually recorded already wide. | inference |
| likely_fake_sounding_errors | A "gliss" implemented as a pitch-bend wheel slide instead of the actual valve-slide/half-valve/lip mechanism; a fortissimo swell built by turning up a quiet sample rather than crossfading brighter layers (error 10). | academic: HIRSCHBERG-1996 + inference |
| organic_programming_methods | Draw a dynamic curve that brightens with level, most aggressively of the family (cause: nonlinear closure and, at extremes, shock-wave formation, UNSW-BRASS/HIRSCHBERG-1996). Alternate round robins on repeated notes (cause: `double_spread`/round-robin grammar, not a velocity-only fix). Model fatigue on long high passages (cause: `performer_fatigue`). | academic: UNSW-BRASS; HIRSCHBERG-1996 + inference |

### Trombone (tenor and bass)

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A lip-reed valve exciting a largely cylindrical bore (the most cylindrical of the family, along with trumpet) with pitch changed by a slide rather than valves; bass trombone adds one or two dependent rotary valves extending the low range and filling gaps the slide alone cannot reach smoothly. | academic: HIRSCHBERG-1996 + inference |
| attack_behavior | Attack hardens and brightens with dynamic like the rest of the family; the slide adds a portamento option into or out of an attack that no valved brass instrument has. | inference |
| sustain_behavior | Held notes are not perfectly flat; slide position drift is a further, trombone-specific source of pitch movement on a sustain. | inference |
| release_behavior | Audible; can be released with an outward slide motion for a falling-off effect. | inference |
| dynamic_timbre_change | Trombone is the instrument this was actually measured on: nonlinear wave propagation in its narrow, largely cylindrical bore produces true shock-wave formation (stepwise pressure jumps) at fortissimo, which is the physical root of the "brassy"/cuivré edge. | academic: HIRSCHBERG-1996 |
| register_character | Full and vocal in the middle; the pedal register (below the normal range, using the fundamental of the harmonic series) is a special effect, not part of normal playing. | standard-reference: ADLER-ORCH; BERLIOZ-STRAUSS-TREATISE |
| practical_range | Tenor trombone roughly E2 to B4 (non-transposing, written = sounding). Bass trombone extends the low end further, roughly down to B0-C1 with the valve(s) engaged, at the cost of slower response on the lowest notes. | standard-reference: ADLER-ORCH; BERLIOZ-STRAUSS-TREATISE |
| tessitura | The comfortable, "singing" tessitura is the middle range; both extremes cost more air and control. | inference |
| articulation_logic | Tongued, slurred, accented, flutter-tongued. A slide portamento is available as a genuine continuous pitch effect that other brass can only approximate. | inference |
| phrase_limits | A phrase is a breath, as for the rest of the family. | inference |
| transitions | A true glissando is limited by slide reach: it is only available between notes reachable within the seven slide positions on the same harmonic. Anything larger is a valve-style leap (on bass trombone, using the valve) or a lip movement, not a slide glissando. Half-valve technique does not apply to a slide instrument in the trumpet sense; the slide itself already gives continuous pitch motion. | inference |
| repeated_note_behavior | Single tonguing repeats reliably; double/triple tonguing are less idiomatic than on trumpet. | inference |
| vibrato | Two genuinely distinct mechanisms are both idiomatic: slide vibrato (rocking the slide fractionally in and out of position, roughly 10-15 cents, historically associated with 1930s-40s jazz trombone and still used in both jazz and some classical playing) and jaw vibrato (works across styles but can destabilise high notes). The two are sometimes combined for a wider, more intense effect. Orchestral section players generally use little or no vibrato. | sourced: TROMBONE-ORG-VIBRATO |
| pitch_instability | Slide position is a continuous control, so trombone pitch is less fixed by mechanism than valved brass; accurate intonation depends entirely on ear and slide placement, with no valve to fall back on for a "close enough" position. | inference |
| resonance | Bell and any mute interact as on the rest of the family; the slide's open construction gives more mechanism noise than a valved instrument. | inference |
| physical_noise | Slide friction and slide-stop noise are characteristic and should not be removed. | inference |
| feasibility | One note per player; slide movement between distant positions takes real time and can conflict with a fast passage that a valved instrument would find trivial. | inference |
| ensemble_behavior | Blends within the brass section; a trombone section (typically two tenor, one bass) balances differently from a horn or trumpet section because of the bass trombone's extended low range. | inference |
| recording_behavior | Highly directional, as the rest of the family; the slide's forward-backward motion also physically moves the bell's position over a phrase, a small effect real recordings capture and samples generally do not. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short notes from velocity; long notes need the crossfading control. | inference |
| overlap | Legato patches monophonic, need overlap. | inference |
| velocity | May select attack type; a glissando-capable patch may map velocity or a separate control to gliss speed. | inference |
| continuous_dynamics | Especially important here: this is the instrument shock-wave brightening was actually measured on. | academic: HIRSCHBERG-1996 |
| expression | Separate trim control from the dynamic-layer control. | inference |
| articulation_switching | True slide glissando is a distinct sample/transition type from an ordinary slurred legato and should not be substituted for one. | inference |
| round_robins | Prevent machine-gun repeats. | inference |
| release_samples | Present; a slide release can carry an audible pitch fall if the patch supports it. | inference |
| pedal_or_breath_behavior | Breath and slide noise are part of the instrument. | inference |
| transition_samples | Where available, slide glissando samples are distinct from valve-style leaps and from ordinary legato. | inference |
| mic_or_room_behavior | Directional bell; section patches usually recorded already wide/reverberant. | inference |
| likely_fake_sounding_errors | A glissando played as a pitch bend with no slide-position logic (e.g. crossing a position the seven-position slide cannot reach in the time given); a swell as a fader move (error 10) on the instrument shock-wave brightening was actually measured on. | academic: HIRSCHBERG-1996 + inference |
| organic_programming_methods | Draw a dynamic curve that brightens with level (cause: measured shock-wave/nonlinear propagation, HIRSCHBERG-1996). Give slide glissandi real time proportional to the distance moved, not an instant pitch ramp (cause: physical slide travel). Alternate slide and jaw vibrato by style rather than defaulting to one (cause: named mechanisms, TROMBONE-ORG-VIBRATO). | sourced: TROMBONE-ORG-VIBRATO + academic: HIRSCHBERG-1996 |

### Tuba

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A lip-reed valve exciting the family's widest, most conical bore, with three to six valves depending on the model. The more conical bore is part of why the tuba brightens less dramatically with dynamic than trumpet or trombone. | academic: HIRSCHBERG-1996 |
| attack_behavior | The bottom of the range is slow to speak and needs time and air to establish; attacks lower and softer are the slowest-speaking in the family. | standard-reference: ADLER-ORCH; BERLIOZ-STRAUSS-TREATISE |
| sustain_behavior | Held notes drift slightly without correction, as elsewhere in the family; sustaining the lowest notes costs more air per second than the same dynamic higher up. | inference |
| release_behavior | Audible; low notes can have a longer perceived decay because the fundamental takes longer to establish and disestablish. | inference |
| dynamic_timbre_change | Brightens with dynamic like the rest of the family, but less sharply, consistent with its wider, more conical bore being less prone to the nonlinear cylindrical-bore effects measured on trombone. | academic: HIRSCHBERG-1996 |
| register_character | The bottom is powerful but slow to speak; the tuba is the harmonic and rhythmic foundation of the section more often than a melodic lead. | standard-reference: ADLER-ORCH; BERLIOZ-STRAUSS-TREATISE |
| practical_range | Roughly D1 to F4, non-transposing in the sense that tuba parts are normally written at sounding pitch (though different tuba sizes, e.g. F versus B-flat/CC/BB-flat tuba, are pitched differently as instruments; this is an instrument-family choice, not a written-vs-sounding transposition convention in the part). | standard-reference: ADLER-ORCH; BERLIOZ-STRAUSS-TREATISE |
| tessitura | The comfortable tessitura sits above the extreme bottom, where response is faster and tone is fuller. | inference |
| articulation_logic | Tongued, slurred, accented; rapid articulation is possible but costs more air management than on the smaller-mouthpiece brass. | inference |
| phrase_limits | A phrase is a breath; low, loud tuba playing is especially air-hungry, shortening practical phrase length at the bottom of the range and at high dynamics. | inference |
| transitions | Slurred legato as elsewhere in the family; true glissando is valve-based (a fast run through available fingerings) rather than slide- or lip-based, and is less agile than on trombone. | inference |
| repeated_note_behavior | Rapid repeated notes are possible but slower and less crisp than on trumpet, consistent with the larger air column's slower response. | inference |
| vibrato | Not conventionally used in orchestral tuba playing; where used (some solo and jazz contexts), it follows the same jaw/lip/hand vocabulary as the rest of the family. | inference |
| pitch_instability | As with the rest of the family, embouchure lips pitch around the resonance; the closer partial spacing at the very bottom of the range makes low notes more prone to instability, not less. | inference |
| resonance | The widest bell in the family; mutes exist but are rare in practice. | sourced: RIMSKY-1913 |
| physical_noise | Valve noise and breath noise, proportionally louder relative to the instrument's own sound than on the smaller brass because of the air volume involved. | inference |
| feasibility | One note per player; a tuba section is usually one to two players, so "tuba chords" do not occur in a normal ensemble. | inference |
| ensemble_behavior | Foundation voice; doubles the double bass or cello/bass line as often as it plays independently. | inference |
| recording_behavior | The most omnidirectional-feeling of the family at close range because of the bell's size and orientation, but still directional at a distance; room capture matters a great deal for a convincing low end. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Low notes may need a longer minimum note length to let the fundamental actually speak, mirroring the real instrument's slow low-register attack. | inference |
| overlap | Legato patches monophonic, need overlap; transition latency may be longer at the bottom of the range given slower real-world response. | inference |
| velocity | Selects attack type/dynamic layer; very low velocities on the bottom notes should still respect the instrument's slow-speaking floor rather than triggering an instantly clean attack. | inference |
| continuous_dynamics | Long notes need the crossfading dynamic-layer control; the brightening is real but less extreme than trumpet/trombone. | academic: HIRSCHBERG-1996 |
| expression | Separate trim control from the dynamic-layer control. | inference |
| articulation_switching | Rare mute use should be a deliberate, separate patch choice, not a default. | sourced: RIMSKY-1913 |
| round_robins | Prevent machine-gun repeats, though tuba's naturally slower repeated-note speed makes the failure mode slightly less common than on trumpet. | inference |
| release_samples | Present, with a longer perceptible tail at the bottom of the range. | inference |
| pedal_or_breath_behavior | Breath and valve noise are part of the instrument, proportionally prominent. | inference |
| transition_samples | Valve-run glissandi, where sampled, are a distinct transition type. | inference |
| mic_or_room_behavior | Room capture is unusually important for a convincing low end; a too-close, too-dry tuba reads as small. | inference |
| likely_fake_sounding_errors | Low notes triggered with the same instant attack as a trumpet, ignoring the real instrument's slow low-register speech; a fortissimo built as a level increase only (error 10), understating how much brightening actually occurs even though it is less than trumpet's. | academic: HIRSCHBERG-1996 + inference |
| organic_programming_methods | Give the bottom of the range a slightly longer, softer-onset attack rather than an instant transient (cause: slow low-register speech, standard-reference). Draw a dynamic curve that brightens with level, more moderately than trumpet or trombone (cause: wider, more conical bore, HIRSCHBERG-1996 by extension). Budget more air/phrase-length caution at the bottom of the range and at loud dynamics (cause: higher air cost). | academic: HIRSCHBERG-1996 + inference |

### Brass section (ensemble card)

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A brass section is several independent lip-reed instruments played by separate people, not one instrument scaled up; each player makes their own resonance and dynamic-brightening decisions. | inference |
| attack_behavior | Section attacks are not simultaneous even when written on one tick; they cluster within a small spread that tightens with rehearsal and dynamic confidence. | inference |
| sustain_behavior | A held chord from a section drifts collectively, not identically, which is part of what makes a section sound like a section rather than a stacked solo patch. | inference |
| release_behavior | Section releases spread the same way attacks do. | inference |
| dynamic_timbre_change | A full brass section at full dynamic covers essentially everything else in the arrangement; this is a compositional fact about brass power, not a mixing problem to solve after the fact. | sourced: RIMSKY-1913 |
| register_character | Horns sit between woodwinds and heavy brass and are the traditional bridge voice used to join the two families. | sourced: RIMSKY-1913 |
| practical_range | The section's usable range is the union of its members' ranges, but a written chord voiced across the section must still respect each individual instrument's own practical range and register strength, not just the outer limits. | inference |
| tessitura | Sectional blend is strongest where all members are in their own comfortable tessitura simultaneously; pushing one instrument to its extreme while others sit comfortably unbalances the blend. | inference |
| articulation_logic | A section reads as one instrument only when players match attack type and vibrato; mismatched articulation across parts is audible as disunity, not as intentional counterpoint, unless the counterpoint is actually independent lines. | sourced: RIMSKY-1913 |
| phrase_limits | Staggered breathing lets a section sustain longer than any one player's breath would allow, invisibly, if the writing allows small overlaps rather than demanding every player breathe at the same instant. | inference |
| transitions | Section glissandi/falls read cleanly only if all players execute a compatible gesture (same mechanism, similar timing); a mixed valve-slide-and-lip gliss across a section smears rather than reads as one gesture. | inference |
| repeated_note_behavior | A section repeating a note gains natural variation for free from the players' individual micro-timing and micro-intonation differences, which a single-patch stack does not have unless it is deliberately added. | inference |
| vibrato | A section reads as unified when players match vibrato choice (or its absence); mismatched vibrato mechanisms across a section (some jaw, some lip, some none) read as poor blend rather than as texture. | inference |
| pitch_instability | Section intonation is the sum of each player's individual pitch control; a section patch's fixed tuning is not a substitute for the ensemble drift and correction real sections exhibit. | inference |
| resonance | A section's mutes, where used, are normally matched across the section (all straight, all cup, etc.); mixed mute types across a section chord is unusual and reads as a deliberate effect if used at all. | inference |
| physical_noise | Section noise (valve clatter, breath, slide friction) accumulates audibly and is part of a "big" brass sound at close mic range. | inference |
| feasibility | Section size sets a hard ceiling on simultaneous independent notes; a four-player section cannot play a six-note chord without doubling, and doubling changes the balance, not just the note count. | inference |
| ensemble_behavior | Brass blends with itself more readily than with any other family; horns are the usual link to woodwinds. | sourced: RIMSKY-1913 |
| recording_behavior | Orchestral brass-section libraries are usually recorded at the section's actual hall position, already wide and reverberant; layering a close solo patch under a section patch without accounting for this mismatches the implied space. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | As for individual instruments; a section patch's own recorded note lengths already carry some of the section's natural spread. | inference |
| overlap | Legato section patches are still monophonic per voice; do not expect polyphonic legato from a single section patch. | inference |
| velocity | Section-patch velocity typically maps to the whole section's dynamic layer at once, not to individual players; do not expect per-player velocity control from a section patch. | inference |
| continuous_dynamics | A section's dynamic-layer control should still be used for swells; the brightening effect is the sum of every player's individual brightening. | academic: HIRSCHBERG-1996; UNSW-BRASS |
| expression | Separate trim control, as for solo patches. | inference |
| articulation_switching | A section patch's articulation keyswitches apply to the whole section at once; independent articulation per section member requires either divisi patches or separate tracks. | inference |
| round_robins | Especially important on repeated-note section writing, since a section patch's identical repeats are more exposed than a solo instrument's. | inference |
| release_samples | Present; matters for a convincing section cutoff. | inference |
| pedal_or_breath_behavior | Section breath noise is part of the recorded patch and should not be gated away. | inference |
| transition_samples | Section glissando/fall samples, where they exist, model the ensemble smear described above; a solo instrument's transition sample stacked and detuned is not the same thing. | inference |
| mic_or_room_behavior | Section patches carry their own room; combining a section patch with solo patches recorded in a different space is a common source of an unconvincing blend. | inference |
| likely_fake_sounding_errors | Every section attack aligned on one tick with one velocity (error 3); a section patch stacked to more voices than the recorded section actually has (error 14); mismatched vibrato or articulation choices across simultaneously-written parts that are meant to read as one section. | inference |
| organic_programming_methods | Spread section attacks in a small window rather than aligning them exactly (cause: `ensemble_spread`, `HUMAN_PERFORMANCE_SCHEMA.md`). Match articulation and vibrato choice across simultaneous section parts unless deliberate independence is wanted (cause: named mechanisms above). Respect the section's real voice count before adding divisi. | inference |

---

## What the instrument is

A brass instrument is a column of air excited by the player's lips acting as a pressure-controlled
valve, not a passive reed or a struck string: mouth pressure exceeds mouthpiece pressure, the lips are
driven open, air escapes, and the cycle repeats at a frequency the player's embouchure tension selects
among the bore's available resonances. [academic: UNSW-BRASS] Valves (horn, trumpet, tuba) or a slide
(trombone) change which harmonic series is available; the lips still select which member of that
series actually sounds, so pitch is always a joint decision between mechanism and player, never purely
mechanical. This is why brass intonation is a live skill rather than a fixed property of the
instrument, and why "lipping" a note up or down around its nominal pitch is a real, continuous
capability on every instrument in the family, not an error to be corrected out. [inference]

Two consequences recur through the whole family. **Breath bounds the phrase.** **Embouchure fatigue
accumulates**: a high, loud passage costs the player something that is not repaid until they rest, and
the cost is cumulative across a piece, not reset at each barline. [inference]

## Range and register

The ranges and character notes below are attributed to Adler and to Berlioz and Strauss, neither
opened for this work. [standard-reference: ADLER-ORCH; BERLIOZ-STRAUSS-TREATISE]

| Instrument | Written range | Sounding range | Character |
|---|---|---|---|
| Horn (F side) | roughly B1 to F5 | roughly E1 to B4 (down a fifth) | wide; upper middle is the singing, most tiring register |
| Trumpet (B-flat) | roughly F#3 to C6 | roughly E3 to B5 (down a major second) | brilliant above the staff, thick and less agile low |
| Trumpet (C) | roughly F#3 to C6 | same as written | as B-flat trumpet, without the transposition |
| Tenor trombone | roughly E2 to B4 | same as written | full and vocal in the middle; pedal register is a special effect |
| Bass trombone | extends tenor's range downward, roughly to B0-C1 with valve(s) | same as written | as tenor, with a slower-speaking extended low end |
| Tuba | roughly D1 to F4 | same as written | powerful but slow to speak at the bottom |

**Horn and trumpet are transposing instruments; a part's written pitch is not its sounding pitch.**
The horn in F sounds a perfect fifth below what is written; the B-flat trumpet sounds a major second
below what is written; the C trumpet sounds as written. Trombone and tuba parts are conventionally
written at sounding pitch. [standard-reference: ADLER-ORCH; BERLIOZ-STRAUSS-TREATISE] This distinction
was entirely missing from the 2.0 page and is one of the corrections this pass makes (see
`research/instruments/BRASS.md`). [inference]

The horn plays in a high, closely spaced part of its own harmonic series relative to its fundamental,
which is why it is the least secure of the family and why cracked notes are traditionally most
associated with horn. The 1914 text already discusses the closely spaced partials as the reason for
stopped-note and hand-technique complexity in this register. [sourced: FORSYTH-1914]

Register and endurance interact: a passage comfortable once is not comfortable for sixteen bars. Write
rests, and mean them. [inference]

## Articulation and note transitions

The gesture vocabulary below draws on trumpet and brass pedagogy sources read this pass. [sourced: MODERNTRUMPET-GLISS; BRASSPED-PALNI]

```text
tongued          a clean consonant start; single, double or triple tonguing by speed and mouthpiece size
slurred          the air keeps moving and the lips or valves change the pitch; no new attack
accented         a harder tongue and more air, which is also a brighter sound
lipping/bending  embouchure alone bends pitch around a resonance; asymmetric range (down more than up)
half-valve       a valve held partway; deliberately mistunes the bore for a flexible, semi-pure glissando
valve/slide gliss  first/third trumpet valve slides give a true, pitch-continuous glissando on small
                 intervals; a trombone slide gives a true glissando within a harmonic's seven positions
overtone gliss   a clean jump between adjacent partials with no lip, valve or slide change
flutter          rolled tongue against the airstream
```

**Falls, doits and rips are not one mechanism.** The 2.0 page described them only as movement "through
the harmonic series." That is one option (the overtone glissando above) among at least three others
players actually use, each with a different sound and a different interval range: lip bending,
valve-slide glissando, and half-valve technique. [sourced: MODERNTRUMPET-GLISS]

**Attack character changes with dynamic and with register.** A quiet low entry speaks slowly and
softly; a loud high one has a hard, bright front edge. A library that plays one recorded attack at all
dynamics is the thing the dynamic-layer crossfade exists to fix. [inference]

## Physical constraints

- A phrase is a breath. Long tied passages are impossible for one player and are covered in a section
  by staggered breathing, which is invisible but real. [inference]
- Endurance is finite and cumulative. `performer_fatigue` is a recognised imperfection cause in
  `shared/HUMAN_PERFORMANCE_SCHEMA.md`. [inference]
- **Mutes are physical objects, and stopped horn is a physical hand technique, not a mute.** Fitting or
  removing a mute takes time; a mute change needs rest bars. [inference] Hand-stopping the horn raises
  pitch by roughly a semitone on the F side of a double horn, but by roughly **three-quarters of a tone
  on the B-flat side** — enough of a difference that horn makers built a dedicated stopping valve
  (extra tubing, engaged only for stopped notes) specifically to correct it, rather than requiring the
  player to transpose by ear. [sourced: UNSW-BRASS; HORNMATTERS-STOPVALVE; FORSYTH-1914] This corrects
  the 2.0 page, which stated a flat "about a semitone" with no side-of-the-horn qualification.
  [inference]
- Trombone glissando is limited by **slide reach**: a true glissando is only available between notes on
  the same harmonic within the seven slide positions. Anything else is a valve-style leap (bass
  trombone) or a lip movement, not a slide. [inference]
- Horn lip trills are easiest where the harmonics are close together, which is the upper middle
  register, and easiest as **whole tones**. Lower down the harmonics are too far apart to trill with
  the lip alone. Carried forward from 2.0 unchanged because no source read this pass addressed it
  directly. [to-verify: a horn pedagogy source on lip trills]
- **Half-valve technique** exists on any valved brass instrument. On trumpet it is documented directly.
  [sourced: MODERNTRUMPET-GLISS] Trombone does not need it, since the slide already gives continuous
  pitch motion; tuba and horn share the mechanism in principle but were not independently confirmed
  this pass. [inference]

## Phrase behaviour

A brass phrase has a breath at each end and an air-driven shape in the middle. Held notes move: air
pressure is never perfectly constant, and players lean into and out of long notes as a matter of
course. A perfectly flat brass sustain does not occur. [inference]

**A swell is a timbre change, not a volume fade, and this is now supported at two depths of evidence.**
At the general level, brass spectra brighten with dynamic because louder playing drives the lips into
sharper, more nonlinear closure, adding high harmonics the ear also hears as louder because they fall
in a more sensitive hearing range. [academic: UNSW-BRASS] At the extreme, on a trombone specifically,
this nonlinearity has been **measured** to produce actual shock waves (stepwise pressure jumps) in the
bore at fortissimo — the acoustic root of the "cuivré"/sizzle players and listeners both describe.
[academic: HIRSCHBERG-1996] A loud recorded note turned down with a fader is a loud tone played
quietly, which is audibly wrong: it keeps the bright spectrum of a loud attack at a quiet level. This is
error 10 in `COMMON_ERRORS.md`, and on brass it is not a subtle effect. [inference]

## Ensemble behaviour

Brass blends with itself more readily than with anything else, and a brass section is heard as one
instrument when the players match attack and vibrato. Horns sit between the woodwinds and the heavy
brass and are used to join them. [sourced: RIMSKY-1913] A brass section at full dynamic covers
everything else in the arrangement, which is a compositional fact rather than a mix problem.
[inference]

## Recording behaviour

Brass is directional and loud, so distance and angle change the sound enormously. Close
microphones capture the bell and the buzz; distant ones capture the room being driven by the
instrument, which is where most of the impression of power comes from. Orchestral libraries are usually
recorded at the section's hall position, already wide and already reverberant. [inference]

## Programming it: the control model

consistent with the documented model in `STRINGS.md`. Product specifics belong in the
calibration profile. [inference]

```yaml
long_notes:
  dynamics_from: a continuous controller that crossfades recorded dynamic layers
  because: the timbre must brighten with the level, or the swell is a fade; measured directly on
    trombone at fortissimo as shock-wave formation (HIRSCHBERG-1996)
short_notes:
  dynamics_from: velocity, which may also select the attack type
mutes:
  are: separate sample sets per mute type (straight, cup, harmon, plunger, practice), loaded and
    keyswitched, each with a distinct acoustic effect, not one filter with settings
  are_not: a filter or an EQ curve applied to an open patch
  require: rest bars in the part for the physical change
stopped_horn:
  is: a distinct hand technique and sample set, not a mute preset; raises pitch roughly a semitone
    on the F side and roughly three-quarters of a tone on the B-flat side of a double horn
glissando:
  trumpet_mechanisms: lip bending (small intervals), valve-slide (true, small intervals), half-valve
    (larger intervals, deliberately mistuned, audible breaks possible), overtone gliss (harmonic jumps)
  trombone_mechanism: the slide itself, within a harmonic's seven positions; larger leaps are valve
    (bass trombone) or lip, not slide
legato_patches: monophonic, need overlap, and the transition is a slur with no new attack
release_samples: present; brass note ends are audible
breath_noise: part of the instrument; do not mute it
```

## Programming it: what makes it sound real

- Draw a dynamic curve on every long note, and let the loudest point be the brightest — this is not
  optional stylistic advice, it is the measured acoustic behaviour of the instrument. [academic: UNSW-BRASS; HIRSCHBERG-1996]
- Write breaths. Put real gaps where a player would take one, and vary their length. [inference]
- Model fatigue: after a long loud high passage, let the next entry be a little less confident (the
  named cause is `performer_fatigue` in `shared/HUMAN_PERFORMANCE_SCHEMA.md`). [inference]
- Keep mute and stopped-horn changes plausible and leave bars for them; treat different mute types as
  different patches, not one filtered patch. [standard-reference: TRUMPETMUTES-NOTESTEM + inference]
- Use the attack that fits the register and the dynamic, not one attack everywhere. [inference]
- Build glissandi from the actual mechanism available on the instrument (lip, valve-slide, half-valve,
  slide, or overtone jump), not a generic pitch-bend ramp. [sourced: MODERNTRUMPET-GLISS]
- Match vibrato mechanism to instrument and style: jaw is closest to a default across the family; horn
  most often uses none at all; trombone alone has a genuine slide-vibrato option. [sourced: BRASSPED-PALNI; TROMBONE-ORG-VIBRATO]
- Alternate round robins on repeated notes, and vary velocity by cause (metrical accent, phrase
  position), not by a flat percentage. [inference]
- In a section, do not align the attacks exactly; the named cause is `ensemble_spread` in
  `shared/HUMAN_PERFORMANCE_SCHEMA.md`. [inference]

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Brass-specific tells:

- swells made with a volume fader, which is error 10, and which is now a measured failure on brass
  specifically. [academic: HIRSCHBERG-1996]
- phrases longer than a breath, with no gaps anywhere in a part. [inference]
- mute changes with no time to make them, and mutes implemented as filters rather than distinct
  patches. [inference]
- stopped horn and straight mute used interchangeably, or stopped horn's pitch rise applied uniformly
  to both sides of a double horn when it is not uniform. [sourced: UNSW-BRASS; HORNMATTERS-STOPVALVE]
- a gliss/fall/doit rendered as a pitch-wheel slide with no reference to which real mechanism (lip,
  valve-slide, half-valve, slide) would actually produce it. [sourced: MODERNTRUMPET-GLISS]
- a trombone glissando across an interval the slide cannot reach in position. [inference]
- horn lip trills written wide, or written low where the harmonics are too far apart. [to-verify: a horn pedagogy source on lip trills]
- flat sustains, which is error 2. [inference]
- a section attacking on one tick with one velocity, which is error 3. [inference]
- mismatched vibrato mechanisms across simultaneous section parts meant to read as one voice.
  [inference]

## What the Performance Director needs from this file

- `breath_or_bow_overruns`: any phrase longer than a plausible breath, per instrument and register.
- `out_of_range`: against the ranges above, noting written versus sounding for horn and B-flat trumpet
  specifically, and that the ranges themselves are `standard-reference`.
- `articulation_unavailable`: mutes, stopped horn, and the specific glissando mechanisms are separate
  sample sets; substitution (e.g. a pitch-bend standing in for a valve-slide gliss) is reportable.
- `impossible_voicings`: one note per player. A brass dyad is two players.
- `performer_fatigue` is a recognised cause and should be applied to long high loud passages.
- Mute and stopped-horn changes should be reported as `limb_or_finger_conflicts` when there is no time
  to make them.
- A gliss/fall/doit requested across an interval no real mechanism on that instrument can reach (e.g. a
  trombone slide gliss wider than the seven positions allow within one harmonic) should be reported,
  not silently substituted with a synth-style pitch ramp.

## Sources and what to verify

- **Now supported, not `to-verify`**: the swell-as-timbre-change claim, previously flagged as
  load-bearing and unsourced on the 2.0 page. `academic: UNSW-BRASS` gives the general mechanism;
  `academic: HIRSCHBERG-1996` gives a direct measurement of shock-wave formation on trombone at
  fortissimo.
- **Corrected**: stopped horn's pitch rise is not a flat "about a semitone." It is roughly a semitone on
  the F side and roughly three-quarters of a tone on the B-flat side of a double horn, which is why
  horn makers added a stopping valve. `sourced: UNSW-BRASS; HORNMATTERS-STOPVALVE; FORSYTH-1914`.
- **Corrected**: falls, doits and rips are not produced by one mechanism ("through the harmonic
  series"). At least four distinct mechanisms are documented for trumpet: lip bending, valve-slide
  glissando, half-valve glissando, and overtone (harmonic-series) glissando. `sourced:
  MODERNTRUMPET-GLISS`.
- **To verify**: the acoustic reason the B-flat side of a double horn rises further than the F side when
  stopped. None of the sources read this pass derives this from first principles; settle it against a
  horn-acoustics paper or the International Horn Society's technical pages.
- **To verify**: practical ranges in Adler, *The Study of Orchestration*, and Berlioz and Strauss,
  *Treatise on Instrumentation*. Neither was opened.
- **To verify**: the general, textbook-level account of dynamic-dependent spectral brightening across
  the whole brass family (not only the trombone case actually measured), in Fletcher and Rossing, *The
  Physics of Musical Instruments*. Not opened.
- **Excerpt-depth only**: trumpet mute type descriptions (straight, cup, harmon, plunger, practice),
  reached via a search engine's summary because the source page would not resolve directly when
  fetched. Worth a direct refetch before treating mute acoustic detail as firmly `sourced`.
- **Not available**: measured attack times by register and dynamic; measured brass phrase/endurance
  duration before fatigue changes attack quality. Calibrate if a part depends on either.
