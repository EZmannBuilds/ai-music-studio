# Woodwinds

Flute (with piccolo and alto flute), oboe (with cor anglais), clarinet in B-flat and A (with bass
clarinet), bassoon (with contrabassoon), and the saxophones (soprano, alto, tenor, baritone). Recorder
and other fipple flutes, and non-Western reed and flute traditions, are out of scope; see
`CULTURALLY_SPECIFIC_INSTRUMENTS.md`.

> Evidence: read at section depth: UNSW Music Acoustics' clarinet-acoustics and flute-acoustics
> introductions (register structure, the break, pitch-dynamic coupling); Joe Wolfe's 2018 woodwind
> acoustics overview and a 2011 peer-reviewed saxophone paper on vocal-tract tuning for altissimo, bends
> and multiphonics; a woodwind pedagogue's articles on oboe breath and saxophone vibrato; two saxophone
> pedagogy pages on subtone and growl; Rimsky-Korsakov and Forsyth on woodwind character, breath and the
> double-bassoon. UNSW's own oboe and double-reed acoustics pages were tried and found to state that
> detailed double-reed acoustics were not yet written up there; not used. Transposition intervals are
> `standard-reference`, from a chart reached only at excerpt depth. Practical ranges remain
> `standard-reference`, attributed to Adler and Piston, neither opened. Source IDs resolve in
> `research/sources/INSTRUMENT_SOURCES.md` (here, `research/sources/INSTRUMENT_SOURCES.md`); the claims and their limits
> are recorded in `research/instruments/WOODWINDS.md` (here, `research/instruments/WOODWINDS.md`).

Cross-family failures are in `COMMON_ERRORS.md`.

---

## Behaviour cards

### Flute (with piccolo and alto flute)

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | An air jet from the player's lips crosses the embouchure hole and excites resonances in the bore; no reed. Piccolo is a smaller flute an octave higher; alto flute is a larger flute a fourth lower, with a proportionally larger, more air-hungry embouchure hole. | academic: WOLFE-AT2018 |
| attack_behavior | The jet takes a moment to lock onto a resonance, so the onset is a brief noise-into-tone transition rather than an instant pitch; articulated by tonguing that interrupts the airstream. | academic: WOLFE-AT2018 |
| sustain_behavior | Sustained by continuous breath; because pitch is coupled to blowing pressure, a sustain that changes dynamic without compensation will also drift in pitch. | academic: UNSW-FLUTE-INTRO |
| release_behavior | Audible but soft; the flute has the least mechanism noise of the family at release since there is no reed to stop vibrating and no key click comparable to the others' loudest examples. | inference |
| dynamic_timbre_change | Flute brightens somewhat with dynamic but far less dramatically than a reed or brass instrument; the more audible dynamic-linked change is pitch, not timbre (see `pitch_instability`). | academic: UNSW-FLUTE-INTRO |
| register_character | Low register is weak and easily covered by anything else in the texture; top register is brilliant, loud, and the family's most penetrating extreme alongside piccolo. Piccolo's playing range sits in the ear's most sensitive band, so it is heard above a full orchestra even at moderate dynamic. | academic: WOLFE-AT2018 + inference |
| practical_range | Flute (concert, C): written and sounding both roughly C4 to C7 (non-transposing). Piccolo: written roughly D4 to C7, sounding one octave higher. Alto flute: written roughly B3 to C7, sounding a perfect fourth lower. | standard-reference: ADLER-ORCH; PISTON-ORCH |
| tessitura | The clear, stable middle-to-upper register (roughly the octave above the staff) is the flute's most reliable and most-used tessitura; the bottom octave is weak and exposed. | inference |
| articulation_logic | Tongued (single, double and triple — the flute is one of only two instruments in this family group that can double/triple tongue, since it has no reed to interrupt), slurred (true legato, fingers alone changing pitch on one continuous airstream), staccato, flutter (rolled tongue or throat), multiphonics (special fingerings, an extended technique). | sourced: RIMSKY-1913 |
| phrase_limits | A phrase is a breath, and the flute is the genuinely air-hungry instrument of this family: the embouchure hole passes a fast jet continuously, so breath runs out faster here than on the double reeds. | sourced: PIMENTEL-STALEAIR |
| transitions | Slurred is the real legato: one continuous airstream, fingers alone changing pitch, no new attack. Tongued and slurred groups read as different phrasing, not just different articulation marks. | inference |
| repeated_note_behavior | Rapid repeated notes are possible via double/triple tonguing, uniquely reliable in this family because there is no reed to reset between attacks. | sourced: RIMSKY-1913 |
| vibrato | A breath/throat (diaphragm) vibrato applied across the note rather than present from onset; on flute this is also the vibrato mechanism most other families borrow the term "air vibrato" from. | inference |
| pitch_instability | **Pitch is directly coupled to blowing pressure.** Raising pitch, especially into the upper register, requires increasing jet speed via higher blowing pressure (and usually a narrower lip aperture); this means playing louder tends to sharpen the note and playing softer tends to flatten it unless the player actively compensates. A flute playing loudly at the bottom of its range is fighting the instrument in both dynamic and pitch at once. | academic: UNSW-FLUTE-INTRO |
| resonance | Bore resonance only; no reed or pad system adds sympathetic buzz the way a reed does. Open-hole (French model) flutes have a slightly different resonance character than closed-hole, but this was not independently confirmed this pass. | academic: WOLFE-AT2018 + inference |
| physical_noise | Key mechanism noise and breath/air noise at the embouchure are both part of the instrument's characteristic sound. | inference |
| feasibility | One player, one note; a flute "chord" on one patch is a misuse (see `COMMON_ERRORS.md` #14). | inference |
| ensemble_behavior | Needs to sit above the texture or it disappears, especially in its lower register; pairs well with clarinet in unison or close harmony. | inference |
| recording_behavior | Close microphones capture key noise and breath; distance captures tone and room. Orchestral libraries are recorded at hall position and already reverberant. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short notes from velocity; long notes need the dynamic-layer control. | inference |
| overlap | Legato patches monophonic, need overlap to trigger a recorded transition. | inference |
| velocity | May select tongued versus slurred articulation as well as loudness on short notes. | inference |
| continuous_dynamics | Long notes take dynamics from a crossfading control; because real flute dynamic and pitch are coupled, a convincing swell on a well-built patch should read as a very slight upward pitch drift at the loudest point, where the product supports it. | academic: UNSW-FLUTE-INTRO |
| expression | Separate trim control, distinct from the dynamic-layer control. | inference |
| articulation_switching | Keyswitches select articulation; keyswitch notes are non-sounding. Flutter and multiphonics, where sampled, are separate patches. | inference |
| round_robins | Prevent machine-gun repeats, especially exposed on flute's clean, low-noise attack. | inference |
| release_samples | Present and short. | inference |
| pedal_or_breath_behavior | Breath noise is part of the instrument. No pedal. | inference |
| transition_samples | Legato transition samples are distinct from a re-tongued attack. | inference |
| mic_or_room_behavior | Close mics foreground key and breath noise; section/solo patches usually recorded already reverberant. | inference |
| likely_fake_sounding_errors | Loud, exposed writing in the bottom octave, which the sample plays happily at any dynamic the real instrument cannot sustain there (error 4); a swell with no correlated pitch behaviour at all, on a product capable of per-note pitch. | inference |
| organic_programming_methods | Keep the bottom octave quiet and covered rather than exposed and loud (cause: register weakness, musicianship). Draw dynamic shapes per phrase, remembering that real dynamic and pitch are linked (cause: pitch-dynamic coupling, UNSW-FLUTE-INTRO). Alternate tongued and slurred groups by phrasing, not by habit (cause: articulation logic, musicianship). | academic: UNSW-FLUTE-INTRO + inference |

### Oboe (with cor anglais)

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A double reed (two cane blades vibrating against each other) excites a narrow conical bore; the reed opening is very small compared with a flute's embouchure hole or a clarinet's single-reed aperture. Cor anglais (English horn) is a larger, lower double-reed instrument with a bulbed bell, sharing the oboe's basic mechanism. | academic: WOLFE-AT2018 |
| attack_behavior | A reedy, immediate onset; the double reed speaks readily but the narrow bore makes soft, low entries less forgiving than on flute. | inference |
| sustain_behavior | Sustained by continuous, carefully metered breath; because the reed passes so little air, an oboist can very easily oversupply air to a sustained phrase if not managing it deliberately. | sourced: PIMENTEL-STALEAIR |
| release_behavior | Audible, reedy decay. | inference |
| dynamic_timbre_change | Brightens with dynamic like other reed instruments, though this was not independently measured for oboe in the sources read this pass. | inference |
| register_character | Low register loud and reedy; very high register thin and effortful. Cor anglais has a rounder, more veiled tone than oboe throughout its range, owing to its bulbed bell. | standard-reference: ADLER-ORCH; PISTON-ORCH |
| practical_range | Oboe: written and sounding both roughly B-flat3 to G6 (non-transposing). Cor anglais: written roughly E4(B3 extended) to A6, sounding a perfect fifth lower than written. | standard-reference: ADLER-ORCH; PISTON-ORCH |
| tessitura | The middle register is the oboe's characteristic, most secure voice; extremes cost control in opposite ways — low is loud and hard to play quietly, high is thin and effortful. | inference |
| articulation_logic | Tongued (single only in ordinary practice — double/triple tonguing is not idiomatic on reed instruments the way it is on flute and trumpet), slurred, staccato, flutter (extended technique). | sourced: RIMSKY-1913 |
| phrase_limits | **The oboe's breath problem is stale air, not air hunger.** Because the reed passes air so slowly, an oboist typically has air left over at a natural phrase end rather than running short; the practical difficulty is expelling CO2-rich "stale" air before the next breath, sometimes managed by exhaling without inhaling at a breath mark, then inhaling fresh air at the next one. This is close to the opposite of the flute's problem. | sourced: PIMENTEL-STALEAIR |
| transitions | Slurred: one continuous airstream, fingers alone change pitch. Tongued and slurred groups read as distinct phrasing, as on the rest of the family. | inference |
| repeated_note_behavior | Single-tongued repeats only; no double/triple tonguing in ordinary practice. | sourced: RIMSKY-1913 |
| vibrato | Breath/throat vibrato applied across the note, generally used more continuously on oboe in orchestral playing than the more selective clarinet tradition. | inference |
| pitch_instability | Sustained notes drift slightly with breath pressure, as on the rest of the family; the very narrow reed opening makes fine pitch control partly an embouchure-pressure skill distinct from the flute's jet-speed mechanism. | inference |
| resonance | Conical bore resonance, reed buzz; cor anglais's bulb-shaped bell changes the radiated resonance compared with the oboe's flared bell, contributing to its rounder tone. | inference |
| physical_noise | Reed and key noise; the oboe's small reed opening also makes audible breath control effort more present than on flute. | inference |
| feasibility | One player, one note. | inference |
| ensemble_behavior | The oboe cuts through almost any texture and is the traditional tuning reference for that reason; cor anglais blends more readily as a solo colour than as a cutting lead voice. | sourced: RIMSKY-1913 |
| recording_behavior | Close mics capture reed noise and breath management prominently; distance captures the characteristic nasal carrying tone. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short notes from velocity; long notes from the dynamic-layer control. | inference |
| overlap | Legato patches monophonic, need overlap. | inference |
| velocity | Loudness and possibly attack hardness on short notes; oboe has no articulation-switching role for tonguing speed the way flute's does, since double/triple tonguing does not apply. | inference |
| continuous_dynamics | Long notes need the crossfading dynamic-layer control. | inference |
| expression | Separate trim control. | inference |
| articulation_switching | Keyswitches select articulation; non-sounding keyswitch notes. | inference |
| round_robins | Prevent machine-gun repeats. | inference |
| release_samples | Present, reedy. | inference |
| pedal_or_breath_behavior | Breath and reed noise are part of the instrument; a real oboe part should include occasional exhale gaps at phrase ends consistent with stale-air management, not just inhale gaps. | sourced: PIMENTEL-STALEAIR |
| transition_samples | Legato transitions distinct from re-tongued attacks. | inference |
| mic_or_room_behavior | Close mics foreground reed and breath noise. | inference |
| likely_fake_sounding_errors | Breath marks placed only where the player would run out of air, ignoring that oboe phrase breaks are at least as often about clearing stale air as about air supply (a subtler, oboe-specific version of error 7); loud sustained low writing with no acknowledgment of the register's naturally loud, reedy character. | sourced: PIMENTEL-STALEAIR + inference |
| organic_programming_methods | Place phrase breaks where an oboist would manage stale air, not only where breath would run out (cause: reed air-flow physics, PIMENTEL-STALEAIR). Keep the low register loud/reedy and the top register thin by default rather than uniform across the range (cause: register_character, standard-reference). | sourced: PIMENTEL-STALEAIR + inference |

### Clarinet in B-flat and A (with bass clarinet)

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A single reed against a mouthpiece excites a nearly cylindrical bore, which acoustically behaves as a closed pipe. Bass clarinet is a larger, lower-pitched clarinet, typically in B-flat, sharing the same single-reed mechanism and closed-pipe behaviour at a lower register. | academic: UNSW-CLARINET-INTRO; WOLFE-AT2018 |
| attack_behavior | Reed onset, generally softer-edged than a double reed's; the clarinet "can reduce volume of tone to a mere breath," giving it the family's widest dynamic range at very soft levels. | sourced: RIMSKY-1913 |
| sustain_behavior | Sustained by continuous breath; pitch drifts slightly with breath pressure as on the rest of the family, and the throat register is specifically more prone to this (see `pitch_instability`). | academic: UNSW-CLARINET-INTRO + inference |
| release_behavior | Audible reed decay. | inference |
| dynamic_timbre_change | Timbre shifts across the break in a way tied to register more than to dynamic alone: the chalumeau register is dominated by odd harmonics (a "hollow" character), while above the break, once the speaker key acts as the register hole, the odd/even harmonic imbalance almost disappears and the tone becomes brighter and clearer. | academic: UNSW-CLARINET-INTRO |
| register_character | **Four registers, more distinct than any other instrument in this family.** Chalumeau (low): dark, rich, hollow, the instrument's most characteristic colour. Throat (roughly E4-A#4): weak, dull, least stable. Clarion/clarino (above the break): ringing, clear, the melodic register. Altissimo (top): piercing, effortful. | academic: UNSW-CLARINET-INTRO |
| practical_range | B-flat clarinet: written roughly E3 to C7, sounding a major second lower. A clarinet: same written range convention, sounding a minor third lower. Bass clarinet: written roughly the same shape as soprano clarinet transposed down, sounding (typically) a major ninth below written (an octave plus the B-flat clarinet's own major second). | standard-reference: ADLER-ORCH; PISTON-ORCH |
| tessitura | The clarion register is the clarinet's most secure, most melodically used tessitura; the throat register just below it is deliberately avoided for exposed sustained writing. | academic: UNSW-CLARINET-INTRO |
| articulation_logic | Tongued (single; double/triple tonguing is not idiomatic on a reed instrument), slurred (true legato), staccato, flutter (extended technique). | sourced: RIMSKY-1913 |
| phrase_limits | A phrase is a breath; the clarinet's very small reed opening at soft dynamics can extend phrase length similarly to the oboe's stale-air dynamic at extremely quiet playing, though this was not independently confirmed for clarinet in the sources read this pass. | inference |
| transitions | **The break, between A#4 and B4, is genuinely harder to slur across than any other transition in the family.** It is simultaneously a timbre change (odd/even harmonic balance shifts) and a fingering change (several fingers and the thumb move together, and the register hole itself changes which hole is acting as the speaker). A fast slurred line crossing it repeatedly is difficult in a way a piano roll does not show. | academic: UNSW-CLARINET-INTRO |
| repeated_note_behavior | Single-tongued repeats only. | sourced: RIMSKY-1913 |
| vibrato | Traditionally used much less in orchestral clarinet playing than on flute or oboe; where used, it is a breath vibrato applied selectively by phrase. | inference |
| pitch_instability | **The throat register is acoustically less stable than the chalumeau register, and this is now explained rather than just asserted:** throat-register notes have only two bore resonances that line up well with their harmonics, so their pitch is comparatively easy to "bend" or destabilise compared with the more strongly reinforced chalumeau notes. | academic: UNSW-CLARINET-INTRO |
| resonance | The clarinet's odd-harmonic-dominant chalumeau spectrum, and the near-disappearance of that imbalance once the speaker key is engaged, is itself a resonance phenomenon (which harmonics the closed-pipe bore reinforces), not a separate coloration layered on top. | academic: UNSW-CLARINET-INTRO |
| physical_noise | Reed and key noise. | inference |
| feasibility | One player, one note. | inference |
| ensemble_behavior | Pairs and blends by register with the rest of the woodwind section; bass clarinet is increasingly used as a bridge to low reeds and saxophone in wind and jazz ensembles, though this specific ensemble role was not independently sourced this pass. | inference |
| recording_behavior | Close mics capture key noise and reed buzz; distance captures the instrument's characteristic evenness of tone. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short notes from velocity; long notes from the dynamic-layer control. | inference |
| overlap | Legato patches monophonic, need overlap; a transition crossing the break, if sampled at all, is a distinct and harder-to-execute transition than one that stays within a register. | sourced: UNSW-CLARINET-INTRO + inference |
| velocity | Loudness on short notes; the clarinet's unusually wide soft-dynamic range (RIMSKY-1913) means a patch's quietest velocity layer matters more here than on louder-floored instruments. | sourced: RIMSKY-1913 |
| continuous_dynamics | Long notes from the crossfading control. | inference |
| expression | Separate trim control. | inference |
| articulation_switching | Keyswitches select articulation; non-sounding keyswitch notes. | inference |
| round_robins | Prevent machine-gun repeats. | inference |
| release_samples | Present. | inference |
| pedal_or_breath_behavior | Breath and key noise are part of the instrument. | inference |
| transition_samples | A break-crossing legato transition, where sampled, should be treated as its own case, not assumed to behave like an ordinary same-register legato. | inference |
| mic_or_room_behavior | Close mics foreground key/reed noise. | inference |
| likely_fake_sounding_errors | Sustained exposed writing in the throat register, which the sample plays at any dynamic the real instrument cannot hold stably there; fast slurred lines crossing the break repeatedly, played by the patch with no acknowledgment that this is the hardest transition on the instrument. | academic: UNSW-CLARINET-INTRO |
| organic_programming_methods | Avoid sustained exposed writing in the throat register, or use it deliberately for its acknowledged weak, unstable character (cause: WW-02's acoustic explanation, UNSW-CLARINET-INTRO). Treat break crossings as a harder transition, e.g. by slowing or thinning writing there (cause: same). Keep vibrato selective and phrase-based rather than constant (cause: tradition, musicianship). | academic: UNSW-CLARINET-INTRO + inference |

### Bassoon (with contrabassoon)

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A double reed on a long, folded conical bore (the tube is doubled back on itself to keep the instrument a manageable length). Contrabassoon is built the same way at roughly double the bassoon's length, sounding an octave lower. | sourced: FORSYTH-1914 + academic: WOLFE-AT2018 |
| attack_behavior | A reedy onset, generally slower to speak than oboe given the larger reed and longer bore, most noticeably at the bottom of the range. | inference |
| sustain_behavior | Sustained by continuous breath; drifts slightly as on the rest of the family. | inference |
| release_behavior | Audible, reedy, with a longer perceptible tail at the bottom of the range given the longer bore. | inference |
| dynamic_timbre_change | Brightens somewhat with dynamic as a reed instrument, not independently measured for bassoon in sources read this pass. | inference |
| register_character | The tenor register is the lyrical, most exposed solo register; the low register is dark and reedy; very high bassoon is thin, effortful and comedic in the orchestral tradition ("an atmosphere of senile mockery" in the major, "a sad, ailing quality" in the minor, in one orchestrator's characterisation). | sourced: RIMSKY-1913 |
| practical_range | Bassoon: written and sounding both roughly B-flat1 to E-flat5 (non-transposing). Contrabassoon: written the same shape as bassoon, sounding one octave lower; historically, the extreme bottom two to four semitones of that octave-lower range were difficult or unavailable on many instruments, though modern construction has narrowed this gap. | sourced: FORSYTH-1914 + inference |
| tessitura | The tenor register (roughly the octave above the bass clef) is the bassoon's characteristic lyrical voice; the extremes are used more for colour (low: reedy gravity; high: comic/strained) than for sustained melody. | sourced: RIMSKY-1913 |
| articulation_logic | Tongued (single only — no double/triple tonguing on a reed instrument), slurred, staccato (the double reed gives a distinct, articulate staccato). | sourced: RIMSKY-1913 |
| phrase_limits | A phrase is a breath, as on the rest of the double-reed family; the bassoon's larger reed and bore likely share some of the oboe's low-air-consumption character, though this was not independently confirmed for bassoon in the sources read this pass. | inference |
| transitions | Slurred: one continuous airstream, fingers alone change pitch; distinct octave-key mechanics affect how cleanly register changes slur, similar in spirit to (though less severe than) the clarinet's break. | inference |
| repeated_note_behavior | Single-tongued repeats only. | sourced: RIMSKY-1913 |
| vibrato | Breath vibrato, used more sparingly in orchestral bassoon tradition than on flute or oboe. | inference |
| pitch_instability | Drifts with breath pressure as on the rest of the family; the contrabassoon's much longer bore makes precise intonation slower to settle after an attack, especially low. | inference |
| resonance | Long, folded conical bore resonance; the fold itself does not change the acoustic length but does affect practical fingerings and hand position. | inference |
| physical_noise | Reed and key noise; the bassoon's extensive key mechanism (more keys/rods than oboe or clarinet) is audibly present at close range. | inference |
| feasibility | One player, one note. | inference |
| ensemble_behavior | Provides the traditional bass line of the woodwind section and blends readily with cello/bass and with horn; contrabassoon doubles the bassoon an octave down the way double bass doubles cello. | sourced: FORSYTH-1914 + inference |
| recording_behavior | Close mics capture reed and extensive key noise prominently; distance captures the instrument's characteristic dark, reedy warmth. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short notes from velocity; long notes from the dynamic-layer control; low contrabassoon notes may need a longer minimum length to let the fundamental speak, mirroring its slower real-world attack. | inference |
| overlap | Legato patches monophonic, need overlap. | inference |
| velocity | Loudness/attack hardness on short notes. | inference |
| continuous_dynamics | Long notes from the crossfading control. | inference |
| expression | Separate trim control. | inference |
| articulation_switching | Keyswitches select articulation; non-sounding keyswitch notes. | inference |
| round_robins | Prevent machine-gun repeats. | inference |
| release_samples | Present, with a longer perceptible tail at the bottom of the range. | inference |
| pedal_or_breath_behavior | Breath and key noise are part of the instrument. | inference |
| transition_samples | Legato transitions distinct from re-tongued attacks. | inference |
| mic_or_room_behavior | Close mics foreground reed/key noise; contrabassoon benefits especially from room capture to read as genuinely low rather than just quiet. | inference |
| likely_fake_sounding_errors | Contrabassoon's lowest notes triggered with an instantly clean attack, ignoring the real instrument's historically slow-speaking bottom register; comic/strained high bassoon writing played with a "safe," generic tone that misses the register's actual character. | sourced: FORSYTH-1914 + inference |
| organic_programming_methods | Give the contrabassoon's lowest notes a slightly longer, softer onset rather than an instant transient (cause: historically slow low-register speech, FORSYTH-1914). Reserve the tenor register for lyrical writing and let the extremes carry their traditional character rather than smoothing them out (cause: register_character, RIMSKY-1913). | sourced: FORSYTH-1914; RIMSKY-1913 |

### Saxophones (soprano, alto, tenor, baritone)

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A single reed on a conical metal bore (unlike the clarinet's cylindrical bore), which is why the saxophone overblows at the octave like most other woodwinds rather than at the twelfth. Soprano, alto, tenor and baritone are the same mechanism at four sizes/pitches. | academic: WOLFE-AT2018; UNSW-CLARINET-INTRO |
| attack_behavior | Reed onset; can be shaped from a hard, edgy classical attack to a soft, breathy jazz attack via embouchure and voicing choices (see `dynamic_timbre_change` and `subtone` material below). | inference |
| sustain_behavior | Sustained by continuous breath, drifting slightly as on the rest of the reed family unless deliberately controlled. | inference |
| release_behavior | Audible reed decay; can be shaped (a "fall-off" release) as a idiomatic jazz gesture. | inference |
| dynamic_timbre_change | Beyond ordinary reed brightening with dynamic, saxophone has two deliberately controllable extra timbre techniques: **subtone**, which removes edge from the sound (most effective low in the range) via a relaxed jaw and less mouthpiece in the mouth, producing a fatter, warmer, breathier tone with reduced upper-mid content; and **growl**, produced by humming or singing a pitch *different* from the fingered note while playing, which creates audible interference/beating and a dark, gritty, distorted timbre. Humming the identical pitch does not work; the growl depends on the mismatch. | sourced: TAMINGSAX-SUBTONE; TAMINGSAX-GROWL |
| register_character | Warm, vocal low-to-middle register; a bright, projecting upper register; altissimo (above the normal fingered range) is a genuinely separate technical regime, not just "higher notes" (see `pitch_instability`). | academic: SAXJASA-2011 + inference |
| practical_range | Soprano (B-flat): written roughly A-flat3 to E6, sounding a major second lower. Alto (E-flat): written the same shape, sounding a major sixth lower (an E-flat instrument, one octave and a step down from written in absolute terms). Tenor (B-flat): written the same shape, sounding a major ninth lower (an octave below soprano's transposition). Baritone (E-flat): written the same shape, sounding an octave and a sixth lower (an octave below alto's transposition). Altissimo extends all four upward by a sixth or more above the written range, as a specialist technique. | academic: SAXJASA-2011 + inference |
| tessitura | The middle-to-upper written range is each horn's characteristic, most secure tessitura; subtone is idiomatic in the low register specifically; altissimo is idiomatic only for players who have developed the vocal-tract-tuning skill it requires. | academic: SAXJASA-2011 + inference |
| articulation_logic | Tongued (single; double/triple tonguing is not idiomatic on a single-reed instrument), slurred (true legato), staccato, growl and subtone as timbre-shaping techniques layered onto normal articulation rather than separate articulations in themselves. | sourced: RIMSKY-1913; TAMINGSAX-GROWL; TAMINGSAX-SUBTONE |
| phrase_limits | A phrase is a breath, as on the rest of the reed family; no saxophone-specific air-consumption finding was read this pass, so this is carried as a family-general inference rather than sourced specifically for saxophone. | inference |
| transitions | Slurred legato as on clarinet; **pitch bends are a controlled, idiomatic technique** (not an error or an uncontrolled slip), achieved by tuning the vocal tract to pull the sounding pitch away from the bore's own resonance peak — the same underlying skill that enables altissimo and multiphonics. | academic: SAXJASA-2011 |
| repeated_note_behavior | Single-tongued repeats only. | sourced: RIMSKY-1913 |
| vibrato | **Jaw vibrato (a small, controlled up-and-down jaw motion) is the primary mechanism.** Classical vibrato is comparatively fast, narrow, and begins at the onset of the note. Jazz vibrato is typically slower and more variable in speed, and is very often delayed — applied partway through or toward the end of a sustained note ("terminal" vibrato) rather than present from the start, which lets the note begin with tension that vibrato then releases. | sourced: PIMENTEL-SAXVIBRATO |
| pitch_instability | **Altissimo, extreme pitch bends, and multiphonics/chords are all products of the same skill: tuning the vocal tract's own acoustic resonance to reinforce a chosen bore resonance rather than the one the fingering would normally favour.** Experienced players can produce a vocal-tract resonance peak strong enough to compete with the bore's; less experienced players cannot, which is why altissimo and controlled multiphonics are late-developing, specialist techniques rather than available to any player who has the fingering chart. In ordinary playing within the standard range, no active tract-tuning is needed. | academic: SAXJASA-2011 |
| resonance | Bore resonance, plus (uniquely in this family) the player's own vocal-tract resonance as an active, controllable second resonator for altissimo, bends and multiphonics. | academic: SAXJASA-2011 |
| physical_noise | Reed and key noise; growl technique deliberately adds vocal noise as part of the intended sound rather than as an incidental byproduct. | sourced: TAMINGSAX-GROWL |
| feasibility | One player, one note in ordinary use; multiphonics are a genuine exception, producing more than one simultaneous pitch by design, but remain a specialist extended technique, not a chord voicing tool. | academic: SAXJASA-2011 |
| ensemble_behavior | A saxophone section (commonly two alto, two tenor, one baritone in jazz big-band scoring) blends closely within itself; in classical/concert-band contexts the family covers a soprano-to-baritone choir role comparable to strings. | inference |
| recording_behavior | Close mics capture reed, key and (where used) growl/vocal noise prominently; distance captures the instrument's characteristic vocal warmth. Jazz and classical recording conventions differ noticeably in typical mic distance and the amount of room captured. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short notes from velocity; long notes from the dynamic-layer control. | inference |
| overlap | Legato patches monophonic, need overlap. | inference |
| velocity | Loudness/attack hardness on short notes; does not by itself select subtone or growl, which are timbral techniques layered on top rather than velocity-selected articulations. | inference |
| continuous_dynamics | Long notes from the crossfading control. | inference |
| expression | Separate trim control. | inference |
| articulation_switching | Keyswitches select articulation; subtone and growl, where sampled at all, are separate patches or layers, not derivable from an ordinary sustain patch by EQ or filtering. | inference |
| round_robins | Prevent machine-gun repeats. | inference |
| release_samples | Present; a fall-off release is a distinct, deliberately shaped gesture where available. | inference |
| pedal_or_breath_behavior | Breath, key, and (for growl) vocal noise are part of the instrument. | sourced: TAMINGSAX-GROWL + inference |
| transition_samples | Legato transitions distinct from re-tongued attacks; a bend, where sampled as a transition, should reflect a tract-tuning-style pitch pull rather than a generic pitch-wheel slide. | academic: SAXJASA-2011 + inference |
| mic_or_room_behavior | Close mics foreground reed/key/vocal noise; jazz and classical conventions differ in typical distance. | inference |
| likely_fake_sounding_errors | Classical vibrato's steady onset-to-onset shape applied to a jazz phrase, or vice versa, with no attention to onset timing; a "growl" implemented as a static distortion effect rather than an interval-mismatched hummed pitch, which misses the beating character the real technique produces; altissimo notes triggered as if they were ordinary fingered notes with no acknowledgment that the real technique is late-developing and effortful. | sourced: PIMENTEL-SAXVIBRATO; TAMINGSAX-GROWL + academic: SAXJASA-2011 |
| organic_programming_methods | Delay vibrato onset and vary its speed for jazz phrasing; keep it fast, narrow and present from the note's start for classical phrasing (cause: named vibrato mechanisms, PIMENTEL-SAXVIBRATO). Use subtone deliberately in the low register for a warmer, breathier idiom rather than only for quiet dynamics (cause: TAMINGSAX-SUBTONE). Treat altissimo and extreme bends as requiring their own layer or patch, not a pitch-shifted version of the ordinary range (cause: vocal-tract-tuning mechanism, SAXJASA-2011). | sourced: PIMENTEL-SAXVIBRATO; TAMINGSAX-SUBTONE + academic: SAXJASA-2011 |

---

## What the instrument is

A woodwind is a tube with holes, excited either by an air jet across an edge (flute family) or by one
or a pair of vibrating reeds (everything else). Opening and closing holes changes the effective tube
length. [academic: WOLFE-AT2018] Overblowing jumps to a higher harmonic — the octave for most of the
family, but the **twelfth** for the cylindrical-bore, closed-pipe-behaving clarinet, because a closed
pipe's harmonic series favours odd multiples of the fundamental. [academic: UNSW-CLARINET-INTRO] The
player controls pitch, dynamic and colour with breath pressure, embouchure and (on saxophone,
distinctively) active vocal-tract tuning, essentially all at once. [inference]

**These are solo instruments. One player, one note.** A woodwind pad is not an instrument, it is several
players, and it has to be written as several parts with slightly different entries. This remains the
single most common misuse of a sampled woodwind, unchanged from the 2.0 page. [inference]

## Range and register

The ranges below are attributed to Adler and Piston, not opened. [standard-reference: ADLER-ORCH; PISTON-ORCH] Typical practical ranges, with written and sounding pitch stated separately wherever the
instrument transposes.

| Instrument | Written range | Sounding range | Register notes |
|---|---|---|---|
| Flute | roughly C4-C7 | same (non-transposing) | low weak and coverable; top brilliant and loud |
| Piccolo | roughly D4-C7 | one octave higher | the family's most penetrating extreme, in the ear's most sensitive band |
| Alto flute | roughly B3-C7 | a fourth lower | darker, breathier, more air-hungry per note than concert flute |
| Oboe | roughly B-flat3-G6 | same (non-transposing) | low loud and reedy; very high thin and effortful |
| Cor anglais | roughly E4-A6 | a fifth lower | rounder, more veiled than oboe throughout |
| Clarinet (B-flat) | roughly E3-C7 | a major second lower | four distinct registers, see the card above |
| Clarinet (A) | roughly E3-C7 | a minor third lower | as B-flat clarinet, a semitone lower in sounding pitch |
| Bass clarinet | roughly (soprano shape, down an octave) | a major ninth lower | as soprano clarinet, an octave-plus-second lower overall |
| Bassoon | roughly B-flat1-E-flat5 | same (non-transposing) | tenor register lyrical; low dark and reedy |
| Contrabassoon | as bassoon | one octave lower | historically weak/absent lowest semitones; improved on modern instruments |
| Soprano sax | roughly A-flat3-E6 | a major second lower | brightest, most oboe-adjacent saxophone timbre |
| Alto sax | roughly A-flat3-E6 | a major sixth lower | the family's most common solo/section voice |
| Tenor sax | roughly A-flat3-E6 | a major ninth lower | the classic jazz-lead saxophone range |
| Baritone sax | roughly A-flat3-E6 | an octave and a sixth lower | the section's foundation voice |

**Transposing instruments state written and sounding ranges as two separate facts, and this was largely
missing from the 2.0 page.** Only the clarinet's register map appeared there in any transposition-aware
form; cor anglais, piccolo, alto flute and all four saxophones had no written-versus-sounding statement
at all. [standard-reference: ADLER-ORCH; PISTON-ORCH]

**The clarinet's four registers** remain the most distinct register map in this family, and the
acoustic reason is now sourced rather than asserted. [academic: UNSW-CLARINET-INTRO]

```text
chalumeau (low)      dark, rich, hollow; the instrument's most characteristic colour
throat (middle low)  weak, dull and least stable; two bore resonances reinforce these notes, not more
clarion (middle high) ringing, clear, the melodic register; speaker key acts as the register hole
altissimo (top)      piercing and effortful
```

The **break**, between the throat register and the clarion, is a change of harmonic and of fingering at
once, and slurring across it is genuinely harder than slurring anywhere else in the family.
[academic: UNSW-CLARINET-INTRO]

On the flute, **pitch is coupled to dynamic**, because raising pitch, particularly into the upper
register, requires raising blowing pressure (which raises jet speed) and usually narrowing the lip
aperture. [academic: UNSW-FLUTE-INTRO] A flute playing loudly at the bottom of its range is fighting
the instrument in pitch as well as dynamic. [inference]

## Articulation and note transitions

Only flute can genuinely double- or triple-tongue; every reed instrument in this family is limited to
single tonguing in ordinary practice. [sourced: RIMSKY-1913]

```text
tongued        the tongue interrupts the air to start each note; only flute can double/triple tongue,
               because it alone has no reed to reset between rapid repeated attacks
slurred        one continuous airstream, fingers alone changing the pitch; the real legato
staccato       short and tongued, with the air still supporting
flutter        rolled tongue or throat against the airstream; an extended technique
multiphonics   special fingerings (or, on saxophone, vocal-tract tuning) producing several pitches at
               once; an extended technique
bend/growl/subtone   saxophone-specific timbre and pitch techniques; see the saxophone card
```

**Only flute can genuinely double- or triple-tongue.** Every reed instrument in this family (oboe,
clarinet, bassoon, saxophone) is limited to single tonguing in ordinary practice, because the reed does
not reset cleanly enough for rapid double articulation the way a reedless airstream does. [sourced: RIMSKY-1913] This was correctly implied but not stated as sharply on the 2.0 page. [inference]

Tonguing and slurring are audibly different, and the difference is the phrasing. A melodic line written
as slurred groups separated by tongued entries is a woodwind phrase; the same notes all tongued, or all
slurred, is not. [inference]

## Physical constraints

**Breath length is not uniform across the family, and the old page's account of why was backwards.**
The flute is the genuinely air-hungry instrument here: its embouchure hole passes a continuous, fast air
jet, and it runs short of breath the way the family's reputation for "short reed-instrument breath"
actually describes. The oboe has close to the opposite problem: its very small reed opening passes air
so slowly that an oboist typically has air *left over* at a natural phrase end, and the practical
difficulty is managing stale, CO2-rich air rather than running out — sometimes solved by exhaling
without inhaling at a breath mark, then taking a fresh breath at the next one. [sourced: PIMENTEL-STALEAIR] Clarinet and bassoon, sharing more air-efficient reed mechanisms than the flute, are
treated as closer to the oboe's side of this contrast, though this was confirmed directly only for
oboe and is carried as inference elsewhere in the family. [inference]

**Circular breathing exists and is rare**: it is a specialist technique, and writing a part that requires
it means writing for a specialist. Say so rather than assuming it. [inference]

Fingerings that cross a register break, or that need several fingers to move together, limit speed.
Idiomatic woodwind writing is genuinely key-sensitive — some keys and fingerings are more awkward than
others — but this is **not** a property woodwind writing has and string writing lacks. String writing is
also strongly key-sensitive, through open strings, double-stop fingerings and position changes; the 2.0
page's claim to the contrary is removed as simply wrong, not softened. [inference]

## Phrase behaviour

A phrase runs from breath to breath and is shaped by air pressure across its length. Sustained notes
move, because air pressure is never constant, and on flute this pitch movement is a direct, coupled
consequence of any dynamic change rather than an incidental side effect. [academic: UNSW-CLARINET-INTRO] Vibrato on flute and oboe is a breath and throat vibrato applied across the note
rather than present from the onset; the clarinet traditionally uses much less in orchestral playing;
saxophone vibrato is a distinct jaw-based mechanism whose onset timing (immediate for classical, often
delayed for jazz) is itself a stylistic choice, not a fixed property of the instrument. [sourced: PIMENTEL-STALEAIR + inference]

## Ensemble behaviour

The woodwind section blends by pairing and by register: two of a kind blend, and unlike instruments in
the same register colour each other. The oboe cuts through almost anything and is the traditional
tuning reference for that reason. The flute needs to be above the texture or it disappears. [sourced: RIMSKY-1913] A saxophone section blends closely within itself and, in jazz scoring, typically follows
a two-alto/two-tenor/one-baritone convention. [inference]

A sustained woodwind texture is written as **separate parts with separate breaths**, entering and
leaving at slightly different points, which is also how the texture stays alive. [inference]

## Recording behaviour

Close microphones capture key noise, breath, reed and (on saxophone) growl noise; distance captures the
tone and the room. Key and reed mechanism noise is part of the instrument and should not be gated away.
Orchestral libraries are recorded at the section's hall position and are already reverberant; jazz
saxophone recording conventions typically favour closer, drier placement than classical woodwind
recording. [inference]

## Programming it: the control model

consistent with the documented model in `STRINGS.md`. Product specifics belong in the
calibration profile. [inference]

```yaml
long_notes:
  dynamics_from: a continuous controller that crossfades recorded dynamic layers
  flute_note: real flute dynamic and pitch are physically coupled; a convincing swell may need a
    correlated pitch drift where the product supports per-note pitch control
short_notes:
  dynamics_from: velocity, which may also select tongued versus slurred
legato_patches: monophonic, need overlap; the transition is a slur with no new attack
break_transitions:
  clarinet: crossing the register break is a harder transition than an ordinary same-register slur,
    both in real playing and, where sampled, as a distinct transition type
polyphony: one note. A chord on one patch is a misuse, not a voicing (multiphonics are a documented
  exception, and are themselves an extended technique, not a chord tool)
keyswitches: articulation selection; keyswitch notes are non-sounding
saxophone_techniques:
  subtone: a separate patch/layer, low-register-idiomatic, not derivable from filtering a sustain patch
  growl: vocal noise plus interference, not a static distortion effect
  bend_and_altissimo: a vocal-tract-tuning-based pitch/register technique, not a generic pitch-wheel
    slide or an ordinary fingered note played higher
breath_noise: part of the instrument
key_noise: part of the instrument
release_samples: present, and generally short
extended_techniques: flutter and multiphonics are separate recordings where they exist at all
```

## Programming it: what makes it sound real

- Write one line per instrument, and breathe. A pad is several parts, offset. [inference]
- Draw dynamic shapes per phrase on long notes, and remember the register limits: a quiet high oboe and
  a loud low flute are both fighting the instrument, whatever the sample will play. [inference]
- On flute specifically, treat dynamic and pitch as linked, not independent. [academic: UNSW-FLUTE-INTRO]
- Alternate tongued and slurred groups the way the phrasing requires; remember only flute can genuinely
  double/triple tongue. [sourced: RIMSKY-1913]
- Place oboe (and, cautiously, clarinet/bassoon) breath marks with stale-air management in mind, not
  only air-supply running out. [sourced: PIMENTEL-STALEAIR + inference]
- Avoid sustained exposed writing in the clarinet's throat register, or use it deliberately for its
  acknowledged weak, unstable character. [academic: UNSW-CLARINET-INTRO]
- Treat clarinet break crossings as a harder transition than same-register writing. [academic: UNSW-CLARINET-INTRO]
- On saxophone, use subtone deliberately in the low register, growl as an interval-mismatched vocal
  technique rather than a static effect, and give altissimo/extreme bends their own programming layer.
  [sourced: TAMINGSAX-SUBTONE; TAMINGSAX-GROWL + academic: SAXJASA-2011]
- Vary repeated notes by a named cause (tonguing alternation where double/triple tonguing applies,
  metrical accent everywhere else), not by an unexplained percentage of velocity randomness. [inference]
- Leave key noise and breath audible. [inference]

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Woodwind-specific tells:

- chords played on a single solo woodwind patch, which is error 14 in its purest form (multiphonics on
  saxophone are the one real exception, and are themselves a specialist technique). [academic: SAXJASA-2011 + inference]
- a sustained texture with no breaths anywhere, which is error 7. [inference]
- flat sustains, which is error 2. [inference]
- loud sustained writing in the flute's bottom octave, or a flute swell with no correlated pitch
  behaviour at all. [academic: UNSW-FLUTE-INTRO]
- exposed lyrical writing in the clarinet's throat register. [academic: UNSW-CLARINET-INTRO]
- long fast slurred lines crossing the clarinet break repeatedly with no acknowledgment of the added
  difficulty. [academic: UNSW-CLARINET-INTRO]
- oboe breath marks placed only for air-supply reasons, never for stale-air management. [sourced: PIMENTEL-STALEAIR]
- constant vibrato from the first millisecond of every note, or classical and jazz vibrato onset timing
  swapped. [sourced: PIMENTEL-SAXVIBRATO]
- a saxophone growl implemented as a static distortion effect rather than an interval-mismatched hum.
  [sourced: TAMINGSAX-GROWL]
- altissimo triggered like an ordinary fingered note, with no sense that the real technique is
  late-developing and effortful. [academic: SAXJASA-2011]
- one articulation for a whole melody, which is error 8. [inference]
- double or triple tonguing implied on any instrument but flute. [sourced: RIMSKY-1913]

## What the Performance Director needs from this file

- `breath_or_bow_overruns`: phrases longer than a breath, instrument-specific — flute runs short
  fastest, oboe (and cautiously clarinet/bassoon) manages stale air rather than running short. A note on
  whether circular breathing is being assumed; if it is, that is an `intentional_exception`, not a
  silent allowance.
- `simultaneity_exceeded`: any chord on a solo woodwind patch, saxophone multiphonics excepted and
  flagged as an extended technique rather than assumed available.
- `out_of_range`: against the ranges above, checking written versus sounding pitch for every
  transposing instrument in the family (clarinet B-flat/A, cor anglais, piccolo, alto flute, all four
  saxophones), labelled `standard-reference`.
- Register warnings rather than hard blocks for the flute's low register, the oboe's extreme top and the
  clarinet's throat register. These are weak, not impossible.
- `breath` and `key_noise` are recognised imperfection causes and should be requested here.
- `articulation_unavailable`: double/triple tonguing requested on any instrument but flute; subtone,
  growl, bends and altissimo requested on saxophone with no supporting layer or patch.

## Sources and what to verify

- **Corrected**: the 2.0 page's oboe breath claim was backwards. The oboe is not short of breath "because
  the reed consumes air" — its reed passes very little air, and the practical problem is stale air, not
  air supply. The flute is the genuinely air-hungry instrument. `sourced: PIMENTEL-STALEAIR`.
- **Corrected and removed**: "key-sensitive in a way string writing is not." String writing is strongly
  key-sensitive; the comparison was simply false and has been cut rather than softened.
- **Corrected**: "vary velocity on repeated notes, which is error 1" is replaced with two named causes —
  tonguing alternation in double/triple tonguing, and metrical accent — per
  `shared/HUMAN_PERFORMANCE_SCHEMA.md`'s rule against unmodelled humanisation.
- **Added**: saxophone was named in the family title on the 2.0 page but never actually covered. Four
  saxophone sizes now share one card with range, subtone, growl, bends/altissimo and jazz-versus-
  classical vibrato, sourced primarily from a peer-reviewed vocal-tract-tuning paper and named pedagogy
  sources.
- **Added**: written-versus-sounding pitch for every transposing instrument in the family, previously
  present only for the clarinet's register map and missing everywhere else.
- **Added**: auxiliaries (piccolo, alto flute, cor anglais, bass clarinet, contrabassoon), previously
  named only in the family title or not at all, now have their own rows inside each parent card.
- **Added**: resonance as its own row per instrument, including saxophone's distinctive active
  vocal-tract resonance for altissimo, bends and multiphonics.
- **To verify**: the clarinet break's exact written pitch on the A clarinet and bass clarinet (assumed
  to transpose with the instrument; not independently confirmed).
- **To verify**: practical ranges, trill tables and key-sensitivity of figuration in Adler, *The Study of
  Orchestration*, and Piston, *Orchestration*. Neither was opened for this work.
- **To verify**: the transposition intervals used throughout this page, at full read depth from a
  primary orchestration source rather than a web-search-summarised chart (currently `standard-reference`
  at excerpt depth).
- **To verify**: pitch-dynamic coupling on the flute at the textbook-acoustics level (a magnitude in
  cents per dynamic step, not just the mechanism), in Fletcher and Rossing, *The Physics of Musical
  Instruments*. Not opened.
- **Not available**: measured typical breath lengths by instrument, register and dynamic, beyond the
  oboe's qualitative stale-air account. These remain practitioner judgements until calibrated.
