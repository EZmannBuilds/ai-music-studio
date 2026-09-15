# Choir and Voice

The human voice, solo and in a choir. Read with `shared/VOCAL_ARCHITECTURE_SCHEMA.md` and
`shared/LYRIC_ALIGNMENT_SCHEMA.md`, which carry the studio's vocal structures; this file carries what
the instrument does.

> Evidence: no manufacturer manual for a virtual vocal instrument was opened for this pass, so
> `virtual_programming` rows are `inference` unless stated otherwise. Voice-science claims are
> `academic`, read at section or full depth, from a US voice-science tutorial centre, a UNSW/JASA
> paper on soprano vocal-tract resonance, and a peer-reviewed KTH overview of choir acoustics read
> in full. Two pedagogy-adjacent web sources (a vibrato-rate and a belting reference page, both
> secondary but read in full and citing primary studies) and one choral-diction pedagogy page are
> `sourced`. Choral ranges remain `standard-reference`, attributed to Adler, not opened. Source IDs
> resolve in `research/sources/INSTRUMENT_SOURCES.md`; claim-by-claim limits are in
> `research/instruments/CHOIR_AND_VOICE.md`.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## Behaviour cards

### Solo Voice

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Air from the lungs drives the vocal folds into vibration; the resulting sound is filtered by the pharynx, mouth and nose (the vocal tract), whose resonances (formants) the singer reshapes continuously to produce different vowels and to fit pitch. | academic: JOLIVEAU-SOPRANO |
| attack_behavior | Onset is set by how the vocal folds come together relative to the breath: a simultaneous (coordinated) onset, a breathy onset where air precedes full closure, or a hard glottal onset where the folds close before breath pressure releases them, producing an audible click. | inference |
| sustain_behavior | Sustain is breath-driven and continuous, like a bowed string and unlike a struck one: the singer can crescendo, hold or diminuendo within one breath, and the vocal tract's shape (hence the vowel) keeps changing while the note sounds. | academic: JOLIVEAU-SOPRANO |
| release_behavior | A note ends with the breath easing, the folds parting, or a closing consonant; which one happens is a text and phrasing decision, not incidental. | inference |
| dynamic_timbre_change | Louder singing raises subglottal pressure and typically shifts laryngeal and resonance strategy, not just level: classically trained voices add power in the 2-4 kHz "singer's formant" region in solo projection, and contemporary belting uses a distinct, higher-closed-quotient fold configuration with its own formant-tuning strategy, both different from a simple volume increase. | sourced: VOICESCIENCE-BELTING + academic: TERNSTROM-CHOIR-2002 |
| register_character | Chest, head, mix and falsetto are named for differing balances of the two main laryngeal muscle systems and how much fold tissue vibrates: chest is thyroarytenoid-dominant with most of the fold in vibration; head is cricothyroid-leaning with only the folds' cover layers moving; falsetto is cricothyroid-only with minimal tissue in vibration; contemporary "mix"/belt blends both systems, commonly defined by a closed quotient above roughly 50 percent. | sourced: NCVS-REGISTERS; VOICESCIENCE-BELTING |
| practical_range | See the range table in prose; ranges vary substantially by voice, training and style, and are given there by voice type for classical and by common popular-music categories. | standard-reference: ADLER-1989 |
| tessitura | Where a line sits for long stretches matters more than its extremes; the passaggio (register-transition zone) is the hardest part of the range to sustain quietly and evenly, and for many female voices it sits low, not centrally, in the overall range. | sourced: HANSON-PASSAGGIO |
| articulation_logic | The voice's articulation is text: vowels carry pitch and sustain, consonants carry rhythm and are, in effect, the instrument's attack transients. | inference |
| phrase_limits | Breath bounds the phrase; a solo phrase is one breath, and the breath itself is audible just before the phrase begins. | inference |
| transitions | Legato (the vowel continuing through a pitch change with no new consonant), portamento (an audible pitch slide as a stylistic choice), rearticulation (a fresh onset or consonant on a repeated or new pitch), and melisma (many pitches on one vowel, lightly re-articulated) are the four ways one sung syllable connects to the next. | inference |
| repeated_note_behavior | A repeated pitch is normally re-articulated, by breath pulse or a light consonant, rather than replayed identically; how strong the re-articulation is depends on the text. | inference |
| vibrato | A continuous, singer-controlled oscillation in pitch; measured rates across recent studies of trained singers cluster around 4.6-5.4 Hz on average with individual and stylistic spread, and vibrato extent is typically somewhat larger in solo singing than in blended choral singing. | sourced: VOICESCIENCE-VIBRATO + academic: TERNSTROM-CHOIR-2002 |
| pitch_instability | Small, fast pitch fluctuation ("flutter," on the order of 20 cents or less) and slower pitch drift ("wow") are normal in every human voice, not a defect; they are part of what makes a single voice sound different from an electronically doubled one. | academic: TERNSTROM-CHOIR-2002 |
| resonance | The vocal tract's resonances (formants) are what make one vowel distinct from another; a soprano singing high deliberately raises her first resonance to track the rising pitch, which is why very high sung vowels sound different from the same vowel spoken. | academic: JOLIVEAU-SOPRANO |
| physical_noise | Breath noise, a glottal attack's onset noise, and lip/tongue consonant noise are audible parts of a close-recorded solo voice, not defects to remove. | inference |
| feasibility | One voice, one note: a solo singer cannot produce a chord, and one phrase is bounded by one breath. | inference |
| ensemble_behavior | A solo voice doubled by an instrument at the unison tends to fuse with it and can read as less distinctly "a voice"; doubling at the octave, or a light colla parte doubling that follows the vocal line's phrasing, preserves the voice's identity better than a rigid unison doubling does. | inference |
| recording_behavior | Normally recorded close and comparatively dry, so that breath, consonant and lip noise remain audible and are treated as part of the performance rather than removed. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Written note length should reflect where the vowel actually starts and ends, including any closing consonant, not only a MIDI on/off. | inference |
| overlap | A legato vocal transition (the vowel continuing through a pitch change) is a monophonic behaviour and needs the same kind of note overlap a monophonic instrument's legato patch needs, where the product supports it. | inference |
| velocity | On a sampled or synthesised voice, velocity commonly carries attack strength and may also select an onset type (breathy versus more pressed) rather than only loudness. | inference |
| continuous_dynamics | A sustained sung note needs a drawn dynamic shape, on whatever continuous control the instrument reads, because a real sustained vowel is never at one constant loudness and colour. | inference |
| expression | Where a product separates an overall trim from the dynamics control, the trim changes level only; it does not carry the vowel or register change that real dynamic singing carries. | inference |
| articulation_switching | Vowel and consonant selection is product-specific: a controller, a keyswitch, separate patches, or (in more advanced approaches) a syllable sequencer that assembles a whole word. Switching events are not sounding pitches in the part. | inference |
| round_robins | Where a product records multiple takes of a syllable or vowel attack, they exist for the same reason as any other instrument's: to avoid an identical repeated attack. | inference |
| release_samples | A closing consonant or a breath release is the vocal equivalent of a release sample; gluing notes end to end loses it just as it does for a bowed or blown instrument. | inference |
| pedal_or_breath_behavior | Breath noise is a controllable layer on some instruments and should not be muted by default; there is no sustain pedal for a voice. | inference |
| transition_samples | Where a product offers recorded portamento or legato transitions between vowels, they are recordings of an actual glide or connection, not an interpolation the writer can assume is generic. | inference |
| mic_or_room_behavior | A close, dry solo-voice recording and a distant, reverberant choir recording are different starting points; treating a dry solo patch as if it were already in a room, or a wide choir patch as a dry mono source, both misrepresent what was captured. | inference |
| likely_fake_sounding_errors | A sustained vowel with no vowel movement, no consonants and no breath, which is the main reason a simple sampled or synthesised voice reads as a pad rather than a singer; consonants placed exactly on the beat rather than ahead of it, so every word arrives late; crisp, unmodified diction held at the top of a high, loud passage where a real voice's vowel would have shifted. | inference |
| organic_programming_methods | Place consonants ahead of the beat so the vowel lands on it (a phrase-level text decision, not a fixed millisecond rule — see `articulation_logic` and the prose section below). Change the vowel's resonance within a held note as pitch and dynamic change, rather than holding one static vowel shape (`dynamic_timbre_change`). Write a breath before each phrase and keep the breath sample rather than muting it (`phrase_limits`, cause `breath`). Vary vibrato onset and extent by phrase and style rather than one constant setting (`vibrato`, cause `phrase_arch`). | inference |

### Choir (SATB)

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | The same breath-driven, vocal-tract-filtered mechanism as the solo voice, multiplied across many singers in one room; several independent, never-quite-identical voices are what create the sound, not a louder single voice. | inference |
| attack_behavior | As a string section: attacks from individual singers do not land at the same instant, so a choir's onset is a soft-edged cluster rather than one sharp attack. | inference |
| sustain_behavior | Staggered breathing lets a choral line continue past any one singer's breath capacity, because singers breathe at different points; this is why a choir can sustain where a soloist cannot, and choral phrase limits are not solo phrase limits. | inference |
| release_behavior | As attack_behavior: releases and closing consonants also spread slightly across singers rather than landing on one instant, unless the choir deliberately drills a synchronized cutoff. | inference |
| dynamic_timbre_change | Individually measured choir-singer dynamic ranges span roughly 11 to 33 dB SPL, with most of the difference between trained and untrained singers coming from the trained singers' ability to sing more softly rather than a higher ceiling. | academic: TERNSTROM-CHOIR-2002 |
| register_character | Blend depends on singers converging on a matched vowel (matched formant frequencies) and reduced individual vibrato; when formants scatter across singers, listeners perceive it as a vowel-unity problem before they perceive it as an intonation problem. | academic: TERNSTROM-CHOIR-2002 |
| practical_range | See the range table in prose; SATB ranges are typical, not fixed, and any individual choir's real ranges depend on its singers. | standard-reference: ADLER-1989 |
| tessitura | As the solo voice: a part that sits at an extreme for long stretches, or sustains quietly in a passaggio, is harder than a range check alone shows, even though a choir's staggered breathing raises its endurance ceiling. | inference |
| articulation_logic | Consonants define the choir's rhythm and are treated more aggressively than in solo singing: sibilants are shortened and softened so they do not stand out as a mass of "s" sounds, and a consonant that ends one syllable is commonly attached to the start of the next, across a word boundary, for rhythmic clarity. | sourced: CHORAEGUS-DICTION |
| phrase_limits | Choral phrase limits follow the staggered-breath allowance rather than any one singer's breath capacity, provided singers actually stagger rather than all breathing together. | inference |
| transitions | As the solo voice, applied per singer; a choir's overall transition (e.g. a choral portamento or scoop) is the sum of many individual ones and reads as smoother or more diffuse than one voice doing it. | inference |
| repeated_note_behavior | As the solo voice, with the section's natural onset spread doing some of the work a single singer's varied attack would do. | inference |
| vibrato | Individual vibrato is commonly reduced for blend; measured comparisons of the same singers in solo versus choral mode show smaller vibrato extent and reduced singer's-formant emphasis in choral mode, while untrained voices can do the opposite and brighten under ensemble conditions. | academic: TERNSTROM-CHOIR-2002 |
| pitch_instability | Choirs drift without an instrumental reference. Listeners tolerate roughly plus-or-minus 14 cents of standard deviation across a unison section before it reads as poorly tuned, though most prefer zero scatter when given the choice; separately, sung thirds in ensemble are measured wider than just intonation and narrower than equal temperament, not at either "pure" value. | academic: TERNSTROM-CHOIR-2002 |
| resonance | Many voices that are never exactly in unison produce a slow, complex amplitude modulation between their partials, perceived as the "chorus effect" that makes massed voices sound different from one voice; choir spacing (distance between singers) measurably changes both the choir's own sound and how much of their own and others' voices singers hear. | academic: TERNSTROM-CHOIR-2002 |
| physical_noise | Individual breath and consonant noise mostly blend into a general texture rather than being heard as one singer's noise, except in very soft or very exposed choral passages. | inference |
| feasibility | One voice, one note, per singer; divisi is a reduced number of singers per resulting part, not more notes from the same singers. | inference |
| ensemble_behavior | Singers monitor a self-to-other loudness ratio (how loud they hear themselves against the rest of the choir) that varies by position in the ensemble (roughly +1 to +8 dB depending on how many neighbours a singer has) and that singers prefer noticeably louder, on average, than typical measured conditions provide; singers and listeners both tend to prefer wider spacing between singers than close conventional choir formation. | academic: TERNSTROM-CHOIR-2002 |
| recording_behavior | Normally recorded at a distance, in a resonant room, as a body of sound; a close, dry recording approach suited to a solo voice misrepresents how a choir is meant to be heard. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | As the solo voice, applied to whichever voicing (unison, SATB divisi) the patch represents. | inference |
| overlap | As the solo voice, where the product offers a monophonic legato transition. | inference |
| velocity | As the solo voice. | inference |
| continuous_dynamics | As the solo voice; a choir patch's dynamic shape should still be drawn per phrase even though the patch already carries the ensemble's blended character. | inference |
| expression | As the solo voice. | inference |
| articulation_switching | As the solo voice, with the addition that a product's SATB or divisi split is itself effectively an articulation/voicing choice, not a free re-doubling of the same recorded singers. | inference |
| round_robins | As the solo voice; matters for a choir patch because recorded round robins stand in for the natural onset spread real singers would otherwise provide. | inference |
| release_samples | As the solo voice. | inference |
| pedal_or_breath_behavior | As the solo voice; no sustain pedal. | inference |
| transition_samples | As the solo voice. | inference |
| mic_or_room_behavior | A choir patch is normally already wide and reverberant from how it was recorded; stacking a full reverb on top of it risks the same "pushed behind the mix" problem a string section patch has. | inference |
| likely_fake_sounding_errors | Divisi written as if it thickens the texture rather than thinning each resulting part (this is error 14 in `COMMON_ERRORS.md` applied to voices); a choir patch asked to sing more independent parts than its recorded singer count supports; individual voices in a "choir" patch left completely unvaried, with no flutter, wow or attack spread at all. | inference |
| organic_programming_methods | Stagger breath points across a choral line rather than breathing every part together, following the ensemble's real singer count (`phrase_limits`, cause `ensemble_spread`). Know the section's practical singer-per-part count before writing divisi, and write it as thinning (`feasibility`). Let choir vibrato and formant emphasis sit lower than a solo patch's, rather than layering several solo-voice patches and expecting them to blend (`vibrato`, cause `ensemble_spread`). | inference |

---

## What the instrument is

Air from the lungs drives the vocal folds into vibration, and that sound is filtered by a vocal tract the singer reshapes continuously, whose resonances are what distinguish one vowel from another. [academic: JOLIVEAU-SOPRANO] The consequence for programming: a vowel is not a fixed timbre, it is a changing state, and a sustained "ah" that never moves is not doing what a voice does. [inference]

## Range and register

Typical ranges by voice type, given as guidance rather than a fixed boundary, since real singers vary. [standard-reference: ADLER-1989]

| Voice type | Typical range | Comfortable tessitura |
|---|---|---|
| Soprano | roughly C4 to A5 | around F4 to F5 |
| Alto | roughly G3 to D5 | around B3 to C5 |
| Tenor | roughly C3 to A4, sounding an octave below written | around F3 to F4 |
| Bass | roughly E2 to D4 | around A2 to C4 |

Contemporary/popular voice categories are commonly described by comfortable belt and mix range rather than a classical fach; a typical adult female popular-music voice mixes and belts usefully through roughly the octave above middle C, extending higher in a lighter mix or head voice, while a typical adult male popular voice belts usefully through a comparable range an octave down, extending into falsetto above it. [inference]

**Range and tessitura are different facts.** A part can touch its extreme once; a part that lives there for many bars will exhaust a real singer long before a bare range check notices anything, and the Performance Director should check where a line sits, not only where it touches. [inference]

**Passaggio.** Every voice has one or two register-transition zones, and notes there are harder to sing evenly and quietly. For many female voices the primary passaggio sits low in the overall range rather than centrally — commonly cited in the roughly Eb4-F4 area for soprano and mezzo voices, not "the upper third" of the range — because a lighter voice's middle register extends comfortably downward, while a heavier voice's larger chest-voice range pushes its passaggio somewhat higher. [sourced: HANSON-PASSAGGIO] A sustained quiet note in the passaggio is a demanding request; a sampled or synthesised voice will produce it effortlessly, and the part will read as unsung. [inference]

## Articulation and note transitions

The voice's articulation is text. [inference]

**Consonant placement is a lead-time decision, and different consonant types need different amounts of it.** A singer aiming a word at a beat starts the consonant early enough that the vowel, which is what the ear times, arrives on the beat. [inference] This corrects a common oversimplification that a plosive needs the longest lead: a stop consonant's burst (p, t, k, b, d, g) is a brief transient, while a sibilant, a fricative or a consonant cluster (s, sh, f, v, and clusters built from them) is a continuant that needs real duration to be heard as itself, so it is the sibilants, fricatives and clusters that typically need the *longest* lead, not the shortest. [inference] Choral diction practice separately treats sibilants as needing active shortening and softening in performance so a whole section's "s" sounds do not dominate the texture, which is a different, later-stage concern from how much lead time the consonant needs. [sourced: CHORAEGUS-DICTION]

Transitions between notes are:

```text
legato        the vowel continues through the pitch change; no new consonant
portamento    the pitch slides between notes, audibly, as a stylistic choice
rearticulated the same pitch restarted with a consonant or a fresh onset
melisma       many notes on one vowel, with a small re-articulation on each
```

[inference]

**Vibrato is a property of the singer and the style, and its onset is not fixed.** It is a continuous, player-controlled oscillation whose presence, extent and onset timing vary by phrase, singer and idiom; it is measured as somewhat larger in extent in solo singing than in blended choral singing, where it is commonly reduced for blend, and it is not accurate to say it always grows into a note rather than starting with it, since that too depends on the singer and the passage. [academic: TERNSTROM-CHOIR-2002]

## Physical constraints

**Breath bounds the phrase.** A solo singer's phrase is a breath, and the breath itself is audible just before it. [inference] **A choir staggers its breath**, so a choral line can continue past any one singer's capacity while the individual singers breathe at different points; this is why a choir sustains where a soloist does not, and choral phrase limits are not solo phrase limits. [inference] One voice, one note: divisi is more singers' worth of parts, not more notes per singer. [inference]

## Phrase behaviour

A sung phrase has a breath at each end, a shape in the middle, and text driving its rhythm. [inference] Loud is usually also a different laryngeal and resonance strategy, not simply "louder," and quiet at the top of a range is difficult and is itself expressive. [sourced: VOICESCIENCE-BELTING]

**Vowel intelligibility falls as the fundamental frequency rises toward and past the first vocal-tract resonance.** A soprano singing high must raise that resonance to track her rising pitch for efficient loudness, and as she does, the resonance positions of different vowels converge, which is measured to reduce how distinctly the vowels can be told apart. This is why high soprano text is hard to understand in performance, and why a high sampled or synthesised vocal line with crisp, unmodified diction sounds wrong in a way listeners notice without being able to say why. [academic: JOLIVEAU-SOPRANO]

## Ensemble behaviour

**Blend depends on matched vowel resonance and reduced individual vibrato.** A choir reads as one instrument when singers converge on the same vowel formants and moderate their own vibrato; measured choral formant scatter is audible mainly as a vowel-unity problem, and trained singers measurably "hold back" their solo projection strategy (including singer's-formant emphasis and vibrato extent) when singing in choral mode. [academic: TERNSTROM-CHOIR-2002]

**Divisi thins each part.** Splitting sopranos into two lines does not double the sound; it halves the number of singers on each line, and the texture gets lighter and more exposed. This is error 14 in `COMMON_ERRORS.md` applied to voices. [inference]

**Doubling a choral or solo line with an instrument is not one universal effect.** A rigid unison doubling can fuse with and reduce a voice's distinct identity; doubling at the octave keeps more of it, and a light colla parte doubling that follows the vocal line's own phrasing (rather than playing it mechanically) is a standard technique for supporting a voice without erasing it, which corrects the idea that unison doubling always removes the voice's identity — it depends on how rigidly the doubling follows the voice. [inference]

**Singers monitor how loud they hear themselves against the rest of the ensemble**, and this self-to-other balance varies measurably with a singer's position in the choir and with the choir's spacing; singers and listeners both tend to prefer more space between singers than conventional close formation provides. [academic: TERNSTROM-CHOIR-2002]

## Recording behaviour

Choirs are recorded at a distance, in a resonant space, as a body of sound; that is part of the sound, so a sampled or synthesised choir is already wide and already reverberant. [inference] Solo voices are recorded close and comparatively dry, where breath and lip noise are audible and are part of the performance. [inference]

## Programming it: the control model

No manufacturer manual for a vocal instrument was opened this pass; the model below follows the general grammar documented for other continuously-controlled instruments in this pack (see `STRINGS.md`) applied to the voice by inference, not by a voice-specific reading. [inference] Product specifics belong in the calibration profile.

```yaml
long_notes:
  dynamics_from: a continuous control that, on a well-built instrument, should crossfade recorded
    dynamic layers or otherwise change timbre with level, not only volume
vowels:
  selected_by: a controller, a keyswitch, or separate patches, depending on the product
  must: change during a phrase, not only between notes
consonants:
  in_simple_patches: often absent entirely
  in_phrase_or_word_builder_approaches: sequenced syllable by syllable
  placement: ahead of the beat, with lead time driven by the consonant's own type (see "Articulation
    and note transitions" above), so the vowel lands on the beat
legato_patches: monophonic where offered, need overlap; the transition is a vowel continuing through
  a pitch change
breath_noise: an articulation or a layer; do not mute it
release_samples: the phrase ending, including a closing consonant
divisi: more parts, and each part is thinner
```

[inference]

## Programming it: what makes it sound real

Place consonants ahead of the beat, with more lead for a sibilant, fricative or cluster than for a plosive, and let the vowel land on the beat. [inference] Change vowels within held notes, following the text. [inference] Write breaths: leave gaps, keep the breath sample, and stagger them in a choir. [inference] Draw a dynamic shape on every sustained note, and let register or resonance strategy shift with it rather than only level. [sourced: VOICESCIENCE-BELTING] Keep vibrato extent and onset variable by phrase and style, and reduce it for choral blend rather than applying one constant setting everywhere. [academic: TERNSTROM-CHOIR-2002] Treat divisi as thinning, and voice it accordingly. [inference]

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Voice-specific tells, and the first is the whole problem:

- **a sustained "ah" with no vowel change, no consonants and no breath**, which is precisely why a
  sampled or synthesised choir reads as a pad; [inference]
- consonants placed on the beat instead of ahead of it, so every word arrives late, and a sibilant
  given the same short lead as a plosive instead of a longer one; [inference]
- phrases with no breath anywhere, or a choir breathing all together instead of staggering; [inference]
- flat sustains with no dynamic shape, which is error 2; [inference]
- crisp, unmodified diction held at the top of a soprano's range; [academic: JOLIVEAU-SOPRANO]
- divisi written as thicker rather than thinner, which is error 14; [inference]
- one constant, unvarying vibrato on every note regardless of phrase, singer count or style; [academic: TERNSTROM-CHOIR-2002]
- a line that sits at the top of its range, or sustains quietly in the passaggio, for a whole section
  with no relief. [sourced: HANSON-PASSAGGIO]

## What the Performance Director needs from this file

The Vocal Director produces the `feasibility_report` for voice parts; the Performance Director does
not check them. See `shared/HUMAN_PERFORMANCE_SCHEMA.md` section 5.

- `breath_or_bow_overruns`: solo phrases longer than a breath. Choir phrases get the staggered-breath allowance, and the plan should say which rule was applied.
- **Tessitura check**, not only range: flag a line that sits at an extreme, and flag sustained quiet writing in the passaggio.
- `out_of_range`: against the typical ranges above, labelled `standard-reference`.
- Consonant lead time belongs in the plan as a per-syllable offset that varies by consonant type (longer for sibilants, fricatives and clusters; shorter for plosives), labelled `inference`. `shared/LYRIC_ALIGNMENT_SCHEMA.md` carries the alignment itself.
- `breath` is a required imperfection cause here rather than an optional one.
- `simultaneity_exceeded`: one note per singer; divisi is a part count.
- `ensemble_spread` and reduced vibrato/formant emphasis are the correct causes for a choir's blended character; they should not be reduced toward a soloist's projection.

## Sources and what to verify

- Read in full: a peer-reviewed KTH overview of choir acoustics research (`TERNSTROM-CHOIR-2002`), covering pitch dispersion, blend, spacing, self-to-other balance, and solo-versus-choral voice production.
- Read at section depth: a US voice-science tutorial centre's register-mechanics tutorial (`NCVS-REGISTERS`); a UNSW/JASA paper on soprano vocal-tract resonance tuning (`JOLIVEAU-SOPRANO`); a passaggio-pedagogy page giving specific female passaggio pitches (`HANSON-PASSAGGIO`).
- Read in full: a belting/CQ reference page citing Estill, Schutte, Bestebreurtje and others (`VOICESCIENCE-BELTING`); a vibrato-rate reference page citing Prame, Nix, and Glasner and Johnson (`VOICESCIENCE-VIBRATO`); a choral-diction pedagogy page (`CHORAEGUS-DICTION`).
- **To verify**: exact numeric consonant-anticipation lead times by consonant type, in a dedicated phonetics-of-singing source. Not found at section depth for this work; the ordering correction (sibilants/fricatives/clusters need more lead than plosives) rests on general phonetic reasoning about continuant versus transient consonants, not a measured singing-specific source.
- **To verify**: choral ranges, tessitura conventions and divisi practice against Adler, *The Study of Orchestration* (`ADLER-1989`). Not opened for this work.
- **Not available**: a measured distribution of consonant anticipation times specific to singing. The ordering above is `inference`; a numeric default should be checked by ear against the actual syllable, as the 2.0 page also said.
