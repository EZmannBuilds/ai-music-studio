# Strings

Bowed strings: violin, viola, cello, double bass, solo and in orchestral sections. Plucked string
technique on these instruments (pizzicato) is covered here as an articulation, not as a separate
plucked-string family; fretted plucked instruments are in `GUITAR.md` and `BASS.md`.

> Evidence: one symphonic strings manual was reopened this pass (all 23 pages) and is registered at
> section read depth as `STRINGS-LIBRARY-MANUAL-1`; it confirms and extends the control model and
> articulation list. Acoustics claims are `academic`, read at section or abstract depth, from UNSW
> Music Acoustics and a Cambridge acoustics author's open string-instrument resource. Orchestration
> claims are `sourced` from Rimsky-Korsakov, read at section depth for the string chapters, or
> `standard-reference` where attributed to Adler, Piston, or Fletcher and Rossing without being
> opened. Two performer/pedagogy sources (a professional string magazine, a violin teacher's
> resonance article) were read in full. Source IDs resolve in `research/sources/INSTRUMENT_SOURCES.md`; claim-by-claim
> limits are in `research/instruments/STRINGS.md`.

Cross-family failures are in `COMMON_ERRORS.md`. This file covers what is specific to bowed strings.

---

## Behaviour cards

### Violin

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A string under tension, set into stick-slip (Helmholtz) motion by a drawn bow, radiated by a wooden body with its own resonances, including an air (Helmholtz) resonance near 300 Hz that reinforces the low register. | academic: WOLFE-VIOLIN |
| attack_behavior | The bow does not simply "start" the string; a short transient precedes stable (Helmholtz) motion, and its length depends on bow force, bow acceleration and distance from the bridge. Too little force gives a loose, delayed, breathy onset; too much gives a scratchy or raucous one. Near the bridge the usable force range is wide but hard to hit; over the fingerboard it is forgiving but weak. | academic: WOODHOUSE-GUETTLER; WOODHOUSE-SCHELLENG |
| sustain_behavior | Sustain is continuous and bow-fed, not decaying like a struck or plucked string: as long as the bow keeps moving the string keeps receiving energy, which is why a bowed tone can crescendo, hold, or diminuendo freely within one stroke. | academic: WOLFE-VIOLIN |
| release_behavior | The note ends when the bow leaves the string or stops; on a full stroke the ending is audible as a small settling transient, and lifting a stopped left-hand finger rather than the bow produces a softer tail. | inference |
| dynamic_timbre_change | Bow speed, pressure and contact point together set both loudness and colour: closer to the bridge with more pressure is loud and edged, over the fingerboard with a fast light bow is soft and dark. There is no control that changes loudness alone. | academic: WOODHOUSE-SCHELLENG |
| register_character | The G string carries a distinct, covered "throaty" colour even for pitches available higher up; players choose the string, not only the pitch, for colour. The top of the ordinary range thins and needs more bow control to stay centred. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| practical_range | Written and sounding are the same pitch (non-transposing). A professional London section's curated practical range: G3 up to roughly C#7. | manual-derived: STRINGS-LIBRARY-MANUAL-1 + to-verify: in a dedicated orchestration text |
| tessitura | Full, secure tone across roughly two and a half octaves above the open G; the highest positions are for climactic or specialist writing, not a whole part's comfortable range. | inference |
| articulation_logic | Split by whether the bow stays on the string (sustained, detached, slurred, tremolo, accented) or leaves it (spiccato, sautillé, col legno battuto), plus not-bowed playing (pizzicato, struck wood). Slower note-to-note transitions are heard as portamento, ordinary fingered legato, or a heavier bowed change depending on how fast the player crosses the interval; faster transitions are heard as fingered legato with a slight accent or as a fast-run gesture. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| phrase_limits | Bounded by bow length (a full down-to-up or up-to-down stroke) and by left-hand position changes; a bow change is audible and is a phrasing event, not a defect to hide. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| transitions | A slur is several notes on one bow with the left hand changing pitch while the bow keeps moving; it is a different sound from a separately bowed repetition of the same notes, which is why it is recorded rather than synthesised. A bow change under a slur is a small but real inflection. Portamento (audible finger slide) is used stylistically and is also a practical tool for crossing strings on a large interval. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| repeated_note_behavior | The same pitch repeated quickly on one bow direction sounds different from alternating up-and-down strokes or from a bounced stroke; a real player varies which of these is used rather than repeating one identical attack. | inference |
| vibrato | Left-hand oscillation of pitch around the true note, controlled continuously in width and speed by the player. Whether it starts with the note, grows into it, or is absent (senza) is a style and interpretive choice, not one fixed rule; the reference manual records long notes with and without vibrato and at intermediate ("dolce") amounts precisely because it varies by passage. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| pitch_instability | A stopped pitch is only as centred as the fingered position, and string players tune continuously by ear rather than landing on a fixed point, so there is always some settling right after a shift or an attack. Bowing also excites a smaller torsional wave alongside the main transverse one; under some bowing conditions this can add slight periodic jitter to the tone, audible as part of the bowed "grain" of the sound rather than as mistuning. | standard-reference: BAVU-TORSIONAL |
| resonance | Any note sharing a pitch class with an open string, or one of its overtones, sets that string ringing sympathetically, adding fullness beyond the bowed note itself, and playing exactly in tune is what triggers it. The wooden body has its own resonances that favour some pitches over others. | sourced: COREY-RESONANCE + academic: WOLFE-VIOLIN |
| physical_noise | Bow-hair noise on the attack, rosin "hiss" when a soft bow is pushed to its quietest extreme, string noise under a heavy bow near the bridge, and left-hand finger and shift noise are all part of the instrument's sound, not defects. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| feasibility | One bow, four strings; the bow's flat ribbon of hair meets a bridge curved across the strings, so in ordinary playing it rides on at most two adjacent strings at once, briefly three under heavy pressure and a fast stroke. A sustained chord of three or four notes is not available from a single bow stroke regardless of whether the notes are open or stopped strings; it is played broken, or, at forte with a fast attack, can be caught for a brief instant before settling onto fewer strings. | inference |
| ensemble_behavior | See the section card. A solo violin's attacks and transitions are sharp and precisely timed in a way a section's are not. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| recording_behavior | Normally captured with more than one microphone perspective (a close position and one or more room/ambient positions), because the instrument's sound is understood to include the hall it is played in as well as the string and body. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Written note length should reflect the intended bow stroke and release, not just a MIDI on/off; a legato patch additionally needs the next note's overlap regardless of the written length. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| overlap | Legato transitions are monophonic and only trigger when the next note is played while the previous one is still sounding; without overlap the patch plays two separate attacks instead of a slurred change. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| velocity | On short articulations, velocity carries loudness and can also select which recorded attack character is used. On legato transitions, the velocity of the arriving note is read as a playing-speed and style choice, selecting among a slid, a plainly fingered, or a heavier bowed change, not as loudness. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| continuous_dynamics | Long notes take their dynamic shape from a continuous control that crossfades between recorded dynamic layers (soft through loud), changing timbre as well as level; the source manual calls this the most important control in the instrument and instructs the player to always use it on long notes. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| expression | A separate overall-volume trim, layered on top of the dynamics control rather than replacing it. Raising it does not brighten the tone the way the dynamics control does. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| articulation_switching | Articulations are selected by dedicated switches (patch-level or keyswitch), and some products can also switch by how fast the player plays, letting a slower passage default to a plain legato and a fast one to a run-style transition automatically. Switching notes and switch gestures are not sounding pitches in the part. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| round_robins | Multiple recordings of the same repeated note cycle through in turn to avoid two identical attacks in a row; this is a stated design goal, not an incidental feature. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| release_samples | A separate release trigger sounds when a note is genuinely released (not glued to the next one), carrying the bow-off or damping tail; its prominence is adjustable and matters most where phrases are slow enough for the ear to notice endings. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| pedal_or_breath_behavior | Not applicable to a bowed string instrument; there is no pedal or breath control. Bow-change and finger noise are handled under `physical_noise`/`likely_fake_sounding_errors`, not as a pedal. | inference |
| transition_samples | Legato transitions are separately recorded, not interpolated; distinct transition types exist for slid, plainly fingered and heavier bowed changes, and for fast passagework and rapid scalar runs, selected by how the notes are played rather than chosen directly by the writer. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| mic_or_room_behavior | Recorded with a close perspective and at least one more distant, room-inclusive perspective; the mix between them moves the perceived distance from "on the string" to "in the hall," and the room-inclusive positions carry real reverberant tail that stacks with an added reverb if not accounted for. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| likely_fake_sounding_errors | Flat sustains with no dynamic shape; legato fed non-overlapping notes so it plays detached instead of slurred; three- and four-note chords held as if sustained rather than broken; identical vibrato from the first instant of every note regardless of passage; a solo patch's attacks tightened to section-like uniformity, or a section's attacks tightened to soloist sharpness. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| organic_programming_methods | Draw the dynamic shape per phrase, not per bar (`dynamic_arc`, phrase-level). Overlap legato notes by the amount the patch needs and let arriving velocity carry the transition-style choice, not a loudness choice (`note_overlap`). Leave real note-offs so release triggers sound, especially in slow phrases (`note_length_variation`). Vary which repeated-note attack is used rather than repeating one identical sample (`repeated_note_behavior`). Give a bow change room in a long line rather than hiding it (`phrase_arch`). | manual-derived: STRINGS-LIBRARY-MANUAL-1 |

### Viola

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | As the violin: a bowed, tensioned string on a wooden body, but with a body that is proportionally smaller than acoustic theory would want for its pitch range, which is part of why the instrument's own character (sometimes described as covered or nasal in the middle) is heard as distinctive rather than as a scaled-up violin. | standard-reference: FLETCHER-ROSSING-1998 |
| attack_behavior | Same stick-slip onset mechanism and force/speed/contact-point tradeoffs as the violin; the thicker C string in particular needs a settled bow to speak cleanly at a soft dynamic. | academic: WOODHOUSE-SCHELLENG |
| sustain_behavior | As the violin: continuous, bow-fed sustain. | academic: WOLFE-VIOLIN |
| release_behavior | As the violin. | inference |
| dynamic_timbre_change | As the violin: bow speed, pressure and contact point set loudness and colour together. | academic: WOODHOUSE-SCHELLENG |
| register_character | The C string is the family's characteristic dark, inner voice; the top of the range thins and is used for climactic or doubling lines rather than a comfortable solo register. Violas most often carry the harmonically simpler inner or "pedalling" lines in ensemble writing. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| practical_range | Written and sounding are the same pitch. A professional section's curated practical range: C3 up to roughly F#6. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| tessitura | Comfortable through the middle two octaves; the C string's lowest positions and the top of the range both take more effort to sustain quietly. | inference |
| articulation_logic | As the violin. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| phrase_limits | As the violin: bow length and position changes. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| transitions | As the violin. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| repeated_note_behavior | As the violin. | inference |
| vibrato | As the violin: continuously controlled, style-dependent onset. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| pitch_instability | As the violin. | standard-reference: BAVU-TORSIONAL |
| resonance | Sympathetic ringing from open strings and overtones, as the violin, centred on the viola's own open pitches (C, G, D, A). | sourced: COREY-RESONANCE |
| physical_noise | As the violin; the heavier C string carries more audible bow noise at a given dynamic than a violin's strings do. | inference |
| feasibility | As the violin: two adjacent strings sustain under one bow, a third only briefly under pressure; three- and four-note chords are broken regardless of open or stopped strings. | inference |
| ensemble_behavior | See the section card. Violas are the family's most frequent doublers of an inner harmony line, often an octave from cellos or basses. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| recording_behavior | As the violin: close and room-inclusive perspectives normally both offered. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | As the violin. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| overlap | As the violin. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| velocity | As the violin. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| continuous_dynamics | As the violin. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| expression | As the violin. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| articulation_switching | As the violin. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| round_robins | As the violin. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| release_samples | As the violin. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| pedal_or_breath_behavior | Not applicable. | inference |
| transition_samples | As the violin. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| mic_or_room_behavior | As the violin. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| likely_fake_sounding_errors | As the violin, plus: a viola line copy-pasted from a violin part an octave down, which loses the C string's distinct colour and the instrument's own idiomatic string choices. | inference |
| organic_programming_methods | As the violin. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |

### Cello

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | As the violin family: bowed string, wooden body, with resonances proportioned for a lower register; played upright and seated, which affects bow weight and angle rather than the excitation mechanism itself. | academic: WOLFE-VIOLIN |
| attack_behavior | Same onset physics as the violin; the lower, thicker strings need more bow force at a given speed and contact point to reach clean Helmholtz motion, so a soft cello attack is more onset-sensitive than a soft violin attack. | academic: WOODHOUSE-SCHELLENG |
| sustain_behavior | As the violin family: continuous, bow-fed. | academic: WOLFE-VIOLIN |
| release_behavior | As the violin. | inference |
| dynamic_timbre_change | As the violin family. | academic: WOODHOUSE-SCHELLENG |
| register_character | Genuinely three-register: a resonant low voice near the open strings, a "singing" tenor register above that often used for solo melody, and a higher register that thins and needs secure shifting. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| practical_range | Written and sounding are the same pitch, read from bass, tenor and treble clefs as the line rises. A professional section's curated practical range: C2 up to roughly Bb5. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| tessitura | The tenor register (roughly the octave above the open C and G strings) is where a written melodic line sits most comfortably and expressively for long stretches. | inference |
| articulation_logic | As the violin family. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| phrase_limits | As the violin family: bow length, plus position changes that are physically larger than on the smaller instruments. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| transitions | As the violin family; portamento is a familiar and expressive device on cello's singing register, not only a utility for crossing strings. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| repeated_note_behavior | As the violin family. | inference |
| vibrato | As the violin family: continuous, player-controlled, style-dependent onset. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| pitch_instability | As the violin family. | standard-reference: BAVU-TORSIONAL |
| resonance | Sympathetic ringing centred on the cello's own open strings (C, G, D, A), and a proportionally larger, more resonant body than the violin or viola. | sourced: COREY-RESONANCE |
| physical_noise | As the violin family; low-string bow noise and audible shifts on the longer string length are both more prominent than on violin or viola. | inference |
| feasibility | As the violin family: at most two strings sustain under one bow, three briefly under pressure; broken chords for three- and four-note voicings regardless of open strings. | inference |
| ensemble_behavior | See the section card. Cellos frequently double basses at the unison or an octave above, and, with the first violins, are given the most technically demanding orchestral writing. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| recording_behavior | As the violin family. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | As the violin. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| overlap | As the violin. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| velocity | As the violin. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| continuous_dynamics | As the violin. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| expression | As the violin. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| articulation_switching | As the violin. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| round_robins | As the violin. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| release_samples | As the violin. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| pedal_or_breath_behavior | Not applicable. | inference |
| transition_samples | As the violin. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| mic_or_room_behavior | As the violin. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| likely_fake_sounding_errors | As the violin, plus: a solo cello melody written and played entirely on one string when a real player would cross strings for colour, flattening the register contrast that is the instrument's main expressive resource. | inference |
| organic_programming_methods | As the violin. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |

### Double Bass

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A bowed (or plucked) string on the largest, lowest-tuned body in the family; strings are markedly thicker and under higher absolute tension, which changes how much bow force is needed for a given result. | academic: WOLFE-VIOLIN |
| attack_behavior | The heaviest strings in the family are the slowest to settle into clean bowed motion; a soft bass entrance is the most onset-sensitive in the string family, and pizzicato is comparatively fast and reliable by contrast, which is part of why bass pizzicato is idiomatic and common. | academic: WOODHOUSE-GUETTLER |
| sustain_behavior | As the rest of the family when bowed: continuous and bow-fed. Plucked notes decay, faster than a cello's, with more finger-driven damping available. | academic: WOLFE-VIOLIN |
| release_behavior | As the rest of the family when bowed; plucked notes are commonly damped by hand rather than left to ring. | inference |
| dynamic_timbre_change | As the rest of the family: bow speed, pressure and contact point set loudness and colour together, with a narrower comfortable range because of the string mass involved. | academic: WOODHOUSE-SCHELLENG |
| register_character | Low register is the instrument's core identity: resonant, foundational, and where most orchestral writing sits. Upper positions (thumb position) exist and are used for solo and jazz playing but are a specialist register, not the instrument's normal working range. | inference |
| practical_range | Written pitch sounds one octave lower than written (transposing). A professional section's curated practical written range: C1 up to roughly F#3, sounding an octave down; a low extension to written C1 (sounding C0) exists on instruments built with it. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| tessitura | The lower two-plus octaves of the written range is where the instrument is both easiest to play softly and most useful harmonically; thumb position is for melodic or solo writing, not a whole part's comfortable range. | inference |
| articulation_logic | As the rest of the family, with pizzicato used far more prominently as a primary articulation (not only a colour effect) than on the higher strings, particularly outside orchestral writing. Players hold the bow either overhand or underhand; the two grips favour slightly different off-the-string response, which is a player and instrument fact, not one this file can generalise into a single rule. | inference |
| phrase_limits | As the rest of the family: bow length and position changes, with position changes on the long string length taking measurably more time than on a violin. | inference |
| transitions | As the rest of the family; portamento and audible slides are idiomatic, especially in jazz and popular styles. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| repeated_note_behavior | As the rest of the family; pizzicato repeated notes (a walking bass line) are a core idiom and depend on alternating fingers or hand position for a natural repeated attack, not one identical pluck repeated. | inference |
| vibrato | As the rest of the family: continuous, player-controlled; typically narrower and used more sparingly than on the upper strings because of the string mass and the instrument's usual role. | inference |
| pitch_instability | As the rest of the family, and more exposed: the long, heavy strings settle into pitch more slowly after a shift or attack than a violin's do. | standard-reference: BAVU-TORSIONAL |
| resonance | Sympathetic ringing centred on the bass's own open strings (E, A, D, G, plus low C on a five-string or extension instrument); the largest body in the family gives the most room resonance. | sourced: COREY-RESONANCE |
| physical_noise | Bow and string noise are the most prominent in the family at a given relative dynamic because of the string mass; pizzicato string "thump" and finger slap against the fingerboard are audible parts of the sound. | inference |
| feasibility | As the rest of the family: at most two strings sustain under one bow, briefly three under pressure; broken chords for three- and four-note voicings. Double stops are more physically demanding because of string spacing and thickness. | inference |
| ensemble_behavior | See the section card. Basses most often double the cello line at the octave below rather than carrying independent material; when they do go independent, it is a deliberate harmonic or textural choice. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| recording_behavior | As the rest of the family: close and room-inclusive perspectives; the low register couples strongly with room modes, so a dry low pizzicato and a hall-recorded arco line from the same patch family can sit very differently in a mix. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | As the rest of the family. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| overlap | As the rest of the family for bowed legato; pizzicato is not a legato-overlap articulation. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| velocity | As the rest of the family for bowed articulations; on pizzicato, velocity carries pluck strength and may select a harder or softer pluck sample. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| continuous_dynamics | As the rest of the family for bowed long notes. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| expression | As the rest of the family. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| articulation_switching | As the rest of the family; the arco/pizzicato switch is the substitution error 8 in `COMMON_ERRORS.md` warns against treating as free — the two are genuinely different recordings and different instruments to the ear. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| round_robins | As the rest of the family. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| release_samples | As the rest of the family for bowed notes; pizzicato's own decay is its release, so gluing plucked notes end to end removes the natural decay tail. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| pedal_or_breath_behavior | Not applicable. | inference |
| transition_samples | As the rest of the family for bowed legato. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| mic_or_room_behavior | As the rest of the family; low-frequency room coupling makes mic choice audibly more consequential than on the higher strings. | inference |
| likely_fake_sounding_errors | As the rest of the family, plus: pizzicato and arco treated as interchangeable colours for the same line rather than as different idioms; a bass line with no natural decay because pizzicato notes were glued end to end. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| organic_programming_methods | As the rest of the family, plus: let a walking or repeated pizzicato line vary its attack the way alternating fingers would rather than repeating one identical pluck (`repeated_note_behavior`), and give position shifts on long passages the extra settling time the instrument actually needs (`phrase_arch`). | inference |

### Orchestral String Section (vs. Solo)

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | The same bowed-string mechanism as the solo instrument, multiplied across several independently vibrating strings and bodies in one room, which is a genuinely different sound object, not a louder solo instrument. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| attack_behavior | Attacks from several players never land at the exact same instant; a section's onset is a cluster of individually clean (or individually imperfect) onsets, heard together as a soft-edged, "smeared" attack rather than one sharp one. | inference |
| sustain_behavior | As the solo instrument, multiplied; small independent pitch and bow-speed variation across players adds a natural chorus-like richness a single bowed string cannot produce alone. | inference |
| release_behavior | As attack_behavior: releases also spread slightly across players rather than landing on one instant. | inference |
| dynamic_timbre_change | The same bow-speed/pressure/contact-point mechanism as the solo instrument, but a section's louder ceiling and richer top end come from more strings exciting the room, not from any one player playing more aggressively than a soloist would. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| register_character | As the solo instrument for the relevant section (1st violin, 2nd violin, viola, cello, bass); octave doubling between the 1st and 2nd violins, or between cellos and basses, is a common way to add scale to a top or bottom line. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| practical_range | As the solo instrument for that section. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| tessitura | As the solo instrument for that section; a section can sustain an extreme tessitura for longer than one player because individual fatigue is not simultaneous, but it is still audible as strain if the whole section is pushed there for long stretches. | inference |
| articulation_logic | As the solo instrument; a section's off-the-string articulations (spiccato, col legno) smear the same way its attacks do, which is part of what makes them read as section playing rather than one loud soloist. | inference |
| phrase_limits | Bow changes are staggered across the section (some players change bow while others continue), which is how a section sustains a phrase longer than any one player's bow length would allow, invisibly to the listener. | inference |
| transitions | As the solo instrument, smeared the same way attacks are. | inference |
| repeated_note_behavior | As the solo instrument; repeated attacks additionally benefit from the section's natural attack spread, which does some of the work a single player's varied bowing does. | inference |
| vibrato | Individual vibrato widths and speeds differ slightly across players and average into a less pronounced, more blended vibrato character than any one player's own vibrato. | inference |
| pitch_instability | Small, independent pitch variation across players is normal and is part of the section sound; it is a feature of ensemble playing, not a defect, unless it becomes wide enough to read as out of tune. | inference |
| resonance | As the solo instruments, multiplied; a full section's worth of open-string sympathetic ringing and room coupling is part of why a string section reads as large even at a modest dynamic. | inference |
| physical_noise | Individual bow and finger noise mostly cancels into a general texture rather than being individually audible, except where the section attacks very softly, where breath-like bow noise becomes part of the section's character. | inference |
| feasibility | A section functionally has as many independent voices as it has desks of players; writing more simultaneous harmonic lines than the section can support forces `divisi`, thinning the sound of every resulting line rather than adding to it. As a rough orchestration guideline, a full string orchestra is commonly treated as five independent voices (1st violin, 2nd violin, viola, cello, bass) before divisi is needed. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| ensemble_behavior | This is the card's main subject; the individual instrument cards' `ensemble_behavior` rows say who typically doubles whom. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| recording_behavior | Sections are normally recorded in a hall, in the players' actual seating position, with more than one microphone perspective; the recording already carries the room, so it should not be treated as a dry, close source. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | As the solo instrument's virtual programming, for the section patches of the relevant instrument. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| overlap | As the solo instrument. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| velocity | As the solo instrument. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| continuous_dynamics | As the solo instrument; because a section patch already carries the ensemble's blended dynamic character, its curve should still be drawn per phrase rather than left flat. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| expression | As the solo instrument. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| articulation_switching | As the solo instrument. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| round_robins | As the solo instrument; matters as much for a section patch as for a soloist, because a section's recorded round robins stand in for the natural attack variation many real players would otherwise provide. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| release_samples | As the solo instrument. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| pedal_or_breath_behavior | Not applicable. | inference |
| transition_samples | As the solo instrument. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| mic_or_room_behavior | As the solo instrument, more consequential: a section patch is already wide and already reverberant, so treating it as a dry mono source and adding a full reverb on top tends to push it behind the rest of a mix rather than seating it correctly. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| likely_fake_sounding_errors | A section patch asked to play more simultaneous notes than its practical voice count (error 14 in `COMMON_ERRORS.md`); attacks tightened to soloist sharpness, which removes the smear that makes it read as a section; divisi written as if it adds thickness rather than thinning each resulting line. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |
| organic_programming_methods | Do not tighten section attacks; the smear is correct (`ensemble_spread`, following the ensemble rather than the patch, per `shared/HUMAN_PERFORMANCE_SCHEMA.md` section 3). Know the section's practical voice count before writing divisi, and write it as a deliberate thinning. Trust the section patch's own recorded behaviour for staggered bow changes on a long sustained line rather than adding artificial breaks. | manual-derived: STRINGS-LIBRARY-MANUAL-1 |

---

## What the instrument is

A string under tension, excited into a stick-slip (Helmholtz) vibration pattern by a bow drawn across it, and radiated by a wooden body with its own resonant frequencies, including a low-register-reinforcing air resonance. [academic: WOLFE-VIOLIN]

Because the bow continuously re-energises the string, a bowed note can hold, swell or fade indefinitely within one stroke, unlike a struck or plucked string, which only ever decays. [academic: WOLFE-VIOLIN] The player's bowing hand controls four interacting variables — direction, speed, pressure and contact point — and produces dynamics and timbre from the same gesture: there is no control that changes loudness without also changing colour. [academic: WOODHOUSE-SCHELLENG]

A bow has finite length, so a sustained note eventually needs a bow change, which is audible and is a phrasing event rather than a flaw to hide. [manual-derived: STRINGS-LIBRARY-MANUAL-1]

## Range and register

The practical section ranges below are curated for a professional orchestral section rather than absolute solo extremes. [manual-derived: STRINGS-LIBRARY-MANUAL-1] Older, narrower practical ranges for the same instruments are recorded by Rimsky-Korsakov and kept here as historical context. [sourced: RIMSKY-1913] Exact solo extremes are not established here. [to-verify: exact solo-repertoire extremes for each instrument, in a dedicated modern orchestration text]

| Instrument | Practical range (written) | Sounds | Notes |
|---|---|---|---|
| Violin | G3 to roughly C#7 | at written pitch | non-transposing; solo repertoire reaches higher |
| Viola | C3 to roughly F#6 | at written pitch | non-transposing; the C string is the family's darkest voice |
| Cello | C2 to roughly Bb5 | at written pitch | non-transposing; read from bass, tenor and treble clef as it rises |
| Double bass | C1 to roughly F#3 | one octave below written | transposing; some instruments extend to written C1 (sounding C0) |

Range and tessitura are different facts: a part can touch its extreme once, while a part that lives there for many bars asks something a range check alone will not show, especially on the lower strings, which take more bow force to control quietly. [inference]

## Articulation and note transitions

The primary split is whether the bow stays on the string or leaves it. [manual-derived: STRINGS-LIBRARY-MANUAL-1]

```text
on the string      sustained bowing, detached strokes, slurred groups, tremolo, accented attacks
off the string      spiccato, sautillé, col legno battuto, and playing derived from them
not bowed           pizzicato, struck with the wood of the bow
```

**Legato** is a slur: several notes under one bow, the left hand changing pitch while the bow keeps moving. That sound is recorded, not synthesised, in a sampled library, and a bow change under a slur is a small but real inflection of its own. [manual-derived: STRINGS-LIBRARY-MANUAL-1]

**Portamento** is an audible slide of the finger between two pitches. It is a stylistic device in its own right, especially in cello's singing register, and it is also a practical necessity for crossing strings on a large interval, which a plain fingered legato cannot do smoothly. [manual-derived: STRINGS-LIBRARY-MANUAL-1]

**Spiccato and sautillé are not the same stroke and should not be treated as one fast/slow version of each other.** In spiccato the player actively throws and lifts the bow for every note; in sautillé the bow's own resilience does the bouncing and the player mostly gets out of its way. [sourced: STRAD-SPICCATO] Spiccato works from slow to moderately fast tempo; sautillé takes over where spiccato runs out of time, and the best sautillé keeps the bow as close to the string as possible rather than bouncing high. [sourced: STRAD-SPICCATO]

**Harmonics** are of two kinds. A natural harmonic is produced by touching, not pressing, the string at a node while bowing normally, sounding one of the string's own overtones; an artificial harmonic is produced by stopping the string firmly with one finger and lightly touching a fourth above it with another, sounding two octaves above the stopped note. [manual-derived: STRINGS-LIBRARY-MANUAL-1] Both give a glassy, reduced-power tone with little dynamic range compared with a normally stopped note. [sourced: RIMSKY-1913]

**Mutes (con sordino)** clip onto the bridge and damp the tone: softer and less bright in quiet passages, with a faint hiss or whistle if pushed loud. [sourced: RIMSKY-1913] A "half-muted" section effect, some desks muted and some not, blends the mute's softer colour with the open sound's full body; this is a documented recording and arranging choice, not a universal orchestral default. [manual-derived: STRINGS-LIBRARY-MANUAL-1]

**Sul ponticello** (bowing very close to the bridge) gives a brittle, edged, overtone-rich tone; pushed further it becomes a deliberately distorted, grinding sound. **Sul tasto** (bowing over or near the fingerboard) gives a thinner, softer, less overtone-rich tone; pushed to its extreme, most of what is heard is the rosin and bow-hair noise itself rather than the string's fundamental. **Col legno battuto** strikes the string with the wood of the bow rather than drawing hair across it, a percussive effect for which players normally reserve a cheaper bow. [manual-derived: STRINGS-LIBRARY-MANUAL-1]

**Tremolo** exists in an unmeasured form (as fast as possible, no fixed rhythm, shimmering soft and aggressive loud) and a tempo-locked measured form recorded at specific rates, useful where the tremolo needs to lock rhythmically with the rest of a texture. [manual-derived: STRINGS-LIBRARY-MANUAL-1]

**Trills** (by a semitone or a whole tone, sometimes a minor or major third) are genuinely different recordings of the two-note alternation, not a synthesised oscillation between two single notes. [manual-derived: STRINGS-LIBRARY-MANUAL-1]

Moving between bowed and plucked playing needs real preparation time, since the player changes grip; allow at least a beat when switching. [inference]

## Physical constraints

Four strings, one bow. The bow's flat ribbon of hair meeting a bridge arched across the strings means it can sustain at most two adjacent strings continuously, and a third only briefly under a heavy, fast stroke. [inference] **A sustained chord of three or four notes is therefore not available from one bow stroke, whether the notes involved are open strings or stopped ones** — this corrects the idea that open strings let a bow sustain such a chord; they do not change how many strings the bow physically rides on. [inference] In practice such chords are played broken (rolled) almost always, though a fast attack at forte can catch three strings together for a brief instant before the bow settles onto fewer of them, so "always broken" slightly overstates the case at the loudest dynamics. [inference]

Wide double stops are limited by hand span, more so in low positions. A held note longer than a bow length needs a bow change or, in a section, staggered bowing that the section performs invisibly. [manual-derived: STRINGS-LIBRARY-MANUAL-1]

## Phrase behaviour

Phrases are bounded by bow length and by musical shape, and players lean into a phrase, shape its peak, and ease away from its end. [manual-derived: STRINGS-LIBRARY-MANUAL-1] Vibrato is a continuous, player-controlled effect whose presence, width and onset timing are chosen per phrase and per style — sometimes absent at an onset and growing in, sometimes present from the start, sometimes withheld entirely (senza vibrato) — rather than following one fixed rule for how every note begins. [manual-derived: STRINGS-LIBRARY-MANUAL-1]

## Ensemble behaviour

A section is several independently bowing players; its attacks, releases and legato transitions smear where a soloist's are sharp, and that smear is the actual sound of a section rather than a flaw. [inference] A section patch and a solo patch are therefore not interchangeable at any size — tightening a section's attacks to soloist precision, or loosening a soloist's to section smear, both misrepresent the source. [inference]

A section has a practical voice count — commonly treated, for a full string orchestra, as five independent lines (1st violin, 2nd violin, viola, cello, bass) — before it must divide (`divisi`) to add another harmonic line. Writing more simultaneous notes than that does not add players; it replays the same recorded section, and real divisi thins each resulting part rather than thickening the texture. [manual-derived: STRINGS-LIBRARY-MANUAL-1]

Octave doubling between the 1st and 2nd violins, or between cellos and basses, is a standard way to add scale and help a section tune against itself. [manual-derived: STRINGS-LIBRARY-MANUAL-1]

## Recording behaviour

Orchestral string libraries are normally recorded in a hall, in the section's real seating position, with more than one microphone perspective on offer (a close position and one or more room-inclusive positions). [manual-derived: STRINGS-LIBRARY-MANUAL-1] Position changes perceived distance, stereo width, and how much hall is present; a patch recorded this way is already wide and already reverberant, and treating it as a dry source, then adding a full reverb on top, tends to seat the section behind the rest of a mix rather than in it. [manual-derived: STRINGS-LIBRARY-MANUAL-1]

## Programming it: the control model

Controller numbers, velocity zones and latency figures are product facts and belong in the calibration profile, never here. [manual-derived: STRINGS-LIBRARY-MANUAL-1]

```yaml
long_notes:
  dynamics_from: a continuous control that crossfades recorded dynamic layers
  manual_says: the most important control in the instrument; always use it on long notes
expression:
  is: an overall-volume trim, layered on top of dynamics
  is_not: the dynamics control itself
short_notes:
  dynamics_from: velocity
  velocity_may_also: select which recorded attack character is used
legato_patches:
  polyphony: monophonic
  requires: overlapping notes to trigger a recorded transition
  velocity_of_arriving_note: selects the transition style (slid, plainly fingered, or a heavier
    bowed change at slow speed; plain or accented fingered legato at fast speed; a fast-run style
    at very fast speed) — an articulation choice, not a loudness choice
onset:
  the_recorded_sample_is_cut_close_to_the_true_string_onset: so the patch can otherwise sound late
  fix: play tight and compensate with a small negative track delay
  not: dragging the written notes earlier
round_robins: exist specifically to avoid two identical attacks in a row
release_triggers: a separate layer for a genuine note-off; matters most in slow, exposed phrases
sections: have a practical voice count before divisi is needed
```

The manual's own closing standard for string orchestration is worth keeping: **there are no rules, save that of plausibility.** [manual-derived: STRINGS-LIBRARY-MANUAL-1]

## Programming it: what makes it sound real

Draw a dynamic curve on every long note, per phrase rather than per bar; this is the single largest improvement available on a string part. [manual-derived: STRINGS-LIBRARY-MANUAL-1] Overlap legato notes by the amount the patch needs, and treat the arriving note's velocity as a transition-style choice, not a loudness choice. [manual-derived: STRINGS-LIBRARY-MANUAL-1] Compensate the sample's onset offset with a small negative track delay so written timing is preserved, rather than dragging notes earlier. [manual-derived: STRINGS-LIBRARY-MANUAL-1] Vary repeated-note attacks, alternating recorded strokes, instead of repeating one identical sample. [inference] Let vibrato onset vary by phrase and style rather than applying one fixed onset rule to every note. [manual-derived: STRINGS-LIBRARY-MANUAL-1] Keep real note-offs so release triggers sound, especially in slow music. [manual-derived: STRINGS-LIBRARY-MANUAL-1] Break three- and four-note chords rather than writing them as sustained, on any single bowed part. [inference] For a section, do not tighten the attacks; the smear is correct, and staggered bow changes are handled by the section itself. [inference]

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. The string-specific tells:

- flat sustains with no dynamic curve (error 2), the loudest tell in this family; [manual-derived: STRINGS-LIBRARY-MANUAL-1]
- legato patches fed non-overlapping notes, so they play detached rather than slurred (error 5); [manual-derived: STRINGS-LIBRARY-MANUAL-1]
- three- and four-note chords sustained as if the bow could hold them, on any single instrument; [inference]
- one fixed vibrato-onset rule applied to every note regardless of phrase or style; [manual-derived: STRINGS-LIBRARY-MANUAL-1]
- section patches asked for more simultaneous voices than the section supports (error 14); [manual-derived: STRINGS-LIBRARY-MANUAL-1]
- notes dragged earlier to fight sample onset delay, which loses the written timing, instead of a
  negative track delay; [manual-derived: STRINGS-LIBRARY-MANUAL-1]
- bowed and plucked articulations swapped as if interchangeable, with no preparation time between them; [inference]
- spiccato and sautillé treated as one stroke rather than two different mechanisms suited to
  different tempi. [sourced: STRAD-SPICCATO]

## What the Performance Director needs from this file

- `legato_overlap_ms` is required and comes from calibration; this file says only that overlap is mandatory and the patch is monophonic.
- `impossible_voicings`: any sustained chord of three or more notes on one bowed instrument, regardless of whether open strings are involved.
- `simultaneity_exceeded`: chord density above a section's practical voice count (about five independent lines for a full string orchestra before divisi).
- `breath_or_bow_overruns`: sustained notes longer than a bow length, for solo parts; a section hides this through staggered bowing.
- `articulation_unavailable`: on-string versus off-string strokes, and bowed versus plucked, are genuinely different recordings; substituting one for another is a reportable change, not a free choice.
- `ensemble_spread` is the correct imperfection cause for a section's attack smear, and it should not be reduced toward a soloist's precision.
- Vibrato onset and width are phrase-level choices in the plan (`vibrato.by_phrase`), not a single fixed setting for the whole part.

## Sources and what to verify

- Read at section depth this pass: one symphonic strings manual (`STRINGS-LIBRARY-MANUAL-1`), covering the control model, the full articulation list, ensemble and recording guidance, and general orchestration notes.
- Read at section depth: UNSW Music Acoustics' violin introduction (`WOLFE-VIOLIN`); an open acoustics resource's treatment of the Schelleng and Guettler bowing diagrams (`WOODHOUSE-SCHELLENG`, `WOODHOUSE-GUETTLER`); Rimsky-Korsakov's string chapters (`RIMSKY-1913`).
- Read in full: a professional string magazine's spiccato/sautillé article (`STRAD-SPICCATO`); a violin teacher's sympathetic-resonance article (`COREY-RESONANCE`).
- Read at abstract depth: a UNSW paper on torsional waves in a bowed string (`BAVU-TORSIONAL`).
- **To verify**: exact solo range extremes and register descriptions against Adler, *The Study of Orchestration* (`ADLER-1989`), or Piston, *Orchestration* (`PISTON-1955`). Neither was opened for this work.
- **To verify**: the spectral mechanism of bow-contact-point brightness (why sul ponticello is overtone-rich) against Fletcher and Rossing, *The Physics of Musical Instruments* (`FLETCHER-ROSSING-1998`). Not opened.
- **Not available**: a measured figure for section attack spread, or for double bass position-change timing. If either is needed, calibrate.
