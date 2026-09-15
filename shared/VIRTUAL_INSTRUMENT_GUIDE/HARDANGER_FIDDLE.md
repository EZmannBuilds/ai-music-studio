# Hardanger Fiddle

Traditions: Norwegian Hardanger fiddle (hardingfele) solo dance and slått tradition. Context:
`shared/MUSICAL_SYSTEMS/MODAL_FOLK_SYSTEMS.md`.

This page covers the hardingfele itself: its construction, tuning practice, technique and its role
in the slått repertoire. It does not cover the plain Norwegian violin (vanlig fele) used in regions
where the Hardanger fiddle is not played, or Swedish and other Scandinavian fiddle traditions, which
`shared/MUSICAL_SYSTEMS/MODAL_FOLK_SYSTEMS.md` names as separate practices.

> Evidence: read at full depth: a luthier's article hosted by the Hardanger Fiddle Association of
> America (HFAA) [HFAA-GOLBER-1993], and a 2017 ethnomusicological review of Scandinavian
> asymmetric-rhythm research [JOHANSSON-2017]. Read at section depth: a 2023 peer-reviewed dataset
> paper on Hardanger fiddle recordings [TISMIR-LARTILLOT-2023]. A tuning-name compendium hosted by
> the HFAA was reached but its data table did not extract as text, so it is used only at excerpt
> depth [KODE-HFAA-TUNINGS]. Two further attempts (a dance-timing paper, a ResearchGate acoustics
> paper) were blocked by access restrictions and contributed nothing. Source IDs resolve in
> `research/sources/INSTRUMENT_SOURCES.md`; the claims and their limits are recorded in
> `research/instruments/HARDANGER_FIDDLE.md`.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## Behaviour cards

### Hardanger Fiddle

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Four bowed strings excite the top plate as on a violin, but the sound is coloured by four or five unbowed sympathetic understrings running beneath the fingerboard, which vibrate in response to the bowed strings and thicken the tone with a resonant halo. | sourced: HFAA-GOLBER-1993; TISMIR-LARTILLOT-2023 |
| attack_behavior | A bow attack on any bowed string simultaneously excites some response in the sympathetic strings tuned to related pitches, so even a single note carries a faint resonant onset beyond the bowed string's own attack. | inference |
| sustain_behavior | Sustained by continuous bowing, as with any bowed string instrument; the sympathetic strings add a low-level continuous halo for as long as a related pitch keeps them excited, not only at the attack. | inference |
| release_behavior | Ends with the bow lifting or stopping; because the sympathetic strings keep ringing briefly after the bowed note stops, the release is not as clean a cutoff as an unstrung fiddle's would be. | inference |
| dynamic_timbre_change | unresolved: how strongly dynamic level changes the balance between the bowed strings and the sympathetic resonance | to-verify: a Hardanger-fiddle-specific acoustics or pedagogy source measuring or describing this, not opened this pass |
| register_character | unresolved: where the instrument is strongest or thinnest across its range | to-verify: a performer or pedagogy source addressing register colour specifically, not opened this pass (Golber's article covers construction and adjustment, not register colour) |
| practical_range | Golber gives the four playing strings as tuned, in the most common scheme, in the region of a violin's own range shifted up roughly a whole step overall (violin EADG raised: the lowest string up a whole tone, then the whole instrument up about a further whole tone), with the "A" (kvart) string itself ranging from about B-flat to C-sharp by player and instrument preference. Playing is confined to first position, so the practical upper range is narrower than a violin's despite the higher tuning. | sourced: HFAA-GOLBER-1993 |
| tessitura | unresolved: where within the range a slått idiomatically sits, beyond the first-position constraint under feasibility | to-verify: a pedagogy or repertoire-analysis source, not opened this pass |
| articulation_logic | Bowed articulation as on a violin (separate bow strokes, slurs), but continuous double-stopping is the idiomatic default rather than an occasional device, made possible by the flatter bridge and fingerboard; a melody note is very often sounded together with an open or fingered string beneath or above it, frequently a drone-like open string. | sourced: HFAA-GOLBER-1993; TISMIR-LARTILLOT-2023 |
| phrase_limits | unresolved: typical phrase length or bow-change placement in slått playing (bow length and bow changes bound a phrase as on any bowed instrument, but this was not measured for this tradition specifically this pass) | to-verify: a pedagogy source or transcription study naming bow-change points, not opened this pass |
| transitions | Slurred and separate-bow transitions as on a violin; ornament (see "Idiomatic phrasing and ornamentation" below) frequently substitutes for or accompanies a bow change at a transition, since ornament in this tradition changes rhythmic articulation as well as pitch. | sourced: JOHANSSON-2017 + inference |
| repeated_note_behavior | unresolved: how a repeated melody note is typically separated (re-bow, ornament, or both) | to-verify: a pedagogy source on slått bowing technique, not opened this pass |
| vibrato | unresolved: whether, and how, vibrato is used (`shared/MUSICAL_SYSTEMS/MODAL_FOLK_SYSTEMS.md` treats ornament, not vibrato, as this repertoire's primary expressive device, which argues against assuming continuous vibrato, but no source read this pass states a vibrato convention directly) | to-verify: a pedagogy or performer source addressing vibrato use directly, not opened this pass |
| pitch_instability | Intonation is not derived from a fixed scale or chord structure; it is conditioned by shifting contextual factors including melodic formulas, local tonal centres (which often coincide with the open strings) and string resonance, and is described as showing great variability rather than converging on one fixed set of pitches. | academic: TISMIR-LARTILLOT-2023 |
| resonance | The defining resonance mechanism of this instrument: four or five sympathetic understrings beneath the fingerboard ring in response to the bowed strings, amplifying and colouring the sound; the TISMIR paper's authors note this resonance is strong enough to blur automated pitch-tracking of the fundamental, though it did not disturb expert listeners annotating the same recordings by ear. | sourced: HFAA-GOLBER-1993 + academic: TISMIR-LARTILLOT-2023 |
| physical_noise | Not sourced this pass beyond ordinary bow noise common to bowed strings. | inference |
| feasibility | Traditionally played only in first position (the highest fingered note is approximately at the edge of the instrument's body); four fingers of the left hand, one bow; continuous double-stopping is idiomatic rather than exceptional, so writing it as a rare special case misrepresents the instrument. | sourced: HFAA-GOLBER-1993 |
| ensemble_behavior | Traditionally a solo instrument for couple dancing; TISMIR's dataset itself is of solo recordings. Whether and how two fiddles, or a fiddle with other instruments, interact is unresolved: not addressed by any source read this pass. | sourced: TISMIR-LARTILLOT-2023 + to-verify: not opened this pass |
| recording_behavior | unresolved: conventional close-mic or room approach for this instrument | to-verify: a recording or production source specific to this instrument, not opened this pass |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Held notes should not decouple from bow control: a virtual note's sounding length should track an implied bow stroke, and unlike a struck or plucked instrument a Hardanger fiddle note does not decay on its own while the bow continues, so a sustained control (see continuous_dynamics) matters more than note length as such. | inference |
| overlap | Monophonic on any one bowed string at a time in the sense that one bow produces one line on that string, but the idiomatic constant double-stopping (articulation_logic) means two strings are very often sounding together as a real, written texture, not a legato transition between single notes; a patch or arrangement that reduces this to a single melodic line the way a solo violin sample often is used loses the instrument's basic idiom. | sourced: HFAA-GOLBER-1993 + inference |
| velocity | unresolved: velocity-to-dynamic mapping for a modelled or sampled Hardanger fiddle | to-verify: a manufacturer manual for a Hardanger-fiddle-specific virtual instrument, not opened this pass |
| continuous_dynamics | Not sourced this pass; general bowed-string practice (a continuous dynamic control crossfading recorded dynamic layers, per `COMMON_ERRORS.md` item 2) is assumed to generalise here as it does to other bowed instruments, but this is not itself Hardanger-fiddle-specific evidence. | inference |
| expression | Not sourced this pass. | inference |
| articulation_switching | Not sourced this pass for a specific product; conceptually, an ornament-as-articulation model (see organic_programming_methods) is what the tradition needs, not a bowed/pizzicato-style switch list borrowed from an orchestral strings patch. | inference |
| round_robins | Not sourced this pass for this instrument specifically; `HAND_PERCUSSION.md`-style reasoning (repeated short figures expose identical samples) plausibly applies to repeated drone or open-string strokes here too, but this is carried over by analogy, not read for this instrument. | inference |
| release_samples | Because the sympathetic strings keep ringing briefly after a bowed note stops (release_behavior above), a patch with no distinct release/decay tail loses a real, audible part of this specific instrument's identity, more than it would for an unstrung violin. | inference |
| pedal_or_breath_behavior | Not applicable in the pedal or breath sense; bow control is the closest analogue and is covered under note_length and continuous_dynamics. | inference |
| transition_samples | Not sourced this pass. Ornament figures (see "Idiomatic phrasing and ornamentation") are the tradition's real "transition" vocabulary between notes and are not the same as a violin patch's recorded slide or portamento library. | inference |
| mic_or_room_behavior | unresolved: recording convention for this instrument | to-verify: a recording or production source specific to this instrument, not opened this pass |
| likely_fake_sounding_errors | Tuning the sample or model to twelve-tone equal temperament and treating A-D-A-E as if it were the only tuning; writing a single melodic line with no double stops, which misrepresents an instrument whose idiom is constant double-stopping; omitting sympathetic-string resonance entirely, which a reverb send does not substitute for since the resonance is pitch-selective, not a generic decay; writing a springar part on an even triple-metre grid, which erases the asymmetric beat structure that is the genre's defining feature (see "What virtual implementations commonly get wrong"). | sourced: HFAA-GOLBER-1993 + academic: TISMIR-LARTILLOT-2023 |
| organic_programming_methods | Model the asymmetric springar beat as a `microtiming_template` per `shared/HUMAN_PERFORMANCE_SCHEMA.md` section 3, naming the specific measured corpus it is drawn from (see "Idiomatic phrasing and ornamentation"), never as a generic percentage of swing; write ornament as real pitch-and-rhythm content on the score, not as a humanisation layer, since `shared/VIRTUAL_INSTRUMENT_GUIDE/CULTURALLY_SPECIFIC_INSTRUMENTS.md` step 2.3 treats ornament in traditions like this one as structural, not decorative. | academic: TISMIR-LARTILLOT-2023; JOHANSSON-2017 |

---

## Tradition and context

### Construction

The Hardanger fiddle's body construction is basically that of a violin, but with far more
instrument-to-instrument variation than is normal for the violin family: older instruments tend to
smaller, more arched bodies, while instruments from around 1850 onward increasingly follow a
standard violin outline. Older instruments used native spruce, maple or black alder, with the
fingerboard and tailpiece faced in cowhorn and inlay in bone and mother-of-pearl; modern makers more
often use standard violin tonewoods and ebony. Four bowed (playing) strings run over the
fingerboard, and four or five further sympathetic understrings run beneath it, unbowed, tuned to
ring in response to the bowed strings. The bridge and fingerboard are markedly flatter across their
width than a violin's, a difference that is itself what makes constant double-stopping playable
rather than exceptional; there is a real regional split here, since west-coast Norwegian players use
less double-stopping and prefer a somewhat more rounded fingerboard and bridge than the flatter
setup preferred inland. [sourced: HFAA-GOLBER-1993]

### Tuning

The large majority of Hardanger fiddle tunes -- Golber estimates about three quarters of the
repertoire -- use A-D-A-E tuning (the bowed strings from low to high), with the highest understring
tuned to match the "A"/kvart string and the others tuned to the piece. This is corroborated
independently by the TISMIR dataset paper, which likewise states the vast majority of its recorded
tunes are in D tonality with A-D-A-E tuning. Beyond that majority tuning, **the instrument is tuned
in many different ways depending on the specific piece being played**: a substantial named-tuning
compendium exists (compiled by Karin Loberg Code for the HFAA from several earlier printed sources),
though its actual tuning-by-tuning content was not reachable in this research pass. Absolute pitch
level is not fixed: the "A" string is reported ranging roughly from B-flat to C-sharp by player and
instrument preference, with the rest of the instrument tuned proportionally, since this is solo
music with no ensemble-tuning requirement to standardise against. **Never assume A-D-A-E is the only
tuning, and never assume a fixed reference pitch for "A."** [sourced: HFAA-GOLBER-1993 + academic: TISMIR-LARTILLOT-2023 + standard-reference: KODE-HFAA-TUNINGS]

### Note production and technique

Notes are produced by bowing, exactly as on a violin, with the addition that the sympathetic
understrings colour every bowed note with resonance at related pitches (see the resonance row
above). Playing stays in first position; the highest fingered note is approximately at the edge of
the body. Continuous double-stopping -- sounding a melody note together with an adjacent string,
frequently an open drone string -- is the ordinary texture of the music, not a special device
reserved for cadences or climaxes, which follows directly from the flat bridge and fingerboard
described under Construction. [sourced: HFAA-GOLBER-1993]

### Idiomatic phrasing and ornamentation

`shared/MUSICAL_SYSTEMS/MODAL_FOLK_SYSTEMS.md` states the tradition's ornament principle directly:
Hardanger trills and other ornament figures change the rhythmic articulation of a note as much as
its pitch, and are how a regional style is recognised, which this page does not repeat in full --
see that file. What this page adds, from sources read specifically about this instrument, is the
rhythmic side of phrasing: the springar dance-tune family is organised in a **genuinely asymmetric
triple metre**, in which the three beats of a bar have systematically different durations, and this
asymmetry is tied to the associated dance's cycle of movement rather than to a melodic accent
pattern. Different named sub-styles place the long beat differently -- in Tele-springar the dancers'
downward movement (and the long beat) coincide, while in Halling-springar the downbeat falls on the
short beat -- so the same travelling melody can be felt with its "first beat" in a different metrical
position depending on which regional style is playing it. One measured example, a professional
fiddler's recordings analysed across several tunes in the TISMIR dataset, gives mean beat durations
by position in the bar of about 399 ms, 489 ms and 512 ms (roughly a 1 : 1.2 : 1.3 ratio), against a
fairly stable mean bar duration of about 1.4 seconds; Johansson's review of the older measurement
literature reports comparably uneven ratios for named recordings of the Tele-springar tune
Markensmondagen (in the region of 39:33:28 and 34.5:34.4:31 for two different fiddlers). **These are
each one measured instance, not a general law of springar timing**: Johansson's whole review is a
critical account of how much that ratio varies by tune, player, region and even by how it was
measured, and warns against extracting a single figure to stand for the genre. The correct model in
`shared/HUMAN_PERFORMANCE_SCHEMA.md` terms is `microtiming_template`, named to its specific source
recording or corpus, never a fixed percentage applied uniformly. [academic: TISMIR-LARTILLOT-2023; JOHANSSON-2017]

### Performer interaction and ensemble role

Traditionally a solo instrument, used for solo dance accompaniment, recreation and ceremonial
functions in rural Norwegian communities; the TISMIR dataset itself consists of solo recordings.
Whether, and how, two fiddles or a fiddle with other instruments interact in this tradition was not
addressed by any source read this pass. [sourced: TISMIR-LARTILLOT-2023]

### Repertoire contexts

The repertoire is overwhelmingly dance tunes (slåttar), divided into triple-metre springar types and
duple-metre gangar/rull/halling types, with strong regional "dialects" -- small but consistent
differences in repertoire, playing style and dance style, most pronounced within the springar family
itself, where the basic metre differs by named sub-style (Tele-springar, Halling-springar and
others). The music also serves ceremonial and recreational functions beyond dancing. [sourced: TISMIR-LARTILLOT-2023]

### Improvisation

Not addressed by any source read this pass; `shared/MUSICAL_SYSTEMS/MODAL_FOLK_SYSTEMS.md`'s general
account of tune-family variation across the modal-folk group (a tune existing as a family of variants
across players and regions, rather than a fixed text) plausibly extends to this tradition, but no
Hardanger-fiddle-specific source confirms how far a given player varies a slått between repetitions.
[to-verify: a pedagogy or ethnomusicological source addressing variation practice specifically for
this instrument]

---

## What the instrument is

A four-stringed, bowed folk fiddle of western and south-central Norway, built like a violin but with
four or five additional sympathetic strings beneath the fingerboard and a flatter bridge and
fingerboard that make continuous double-stopping the ordinary texture of the music rather than an
occasional device. [sourced: HFAA-GOLBER-1993 + academic: TISMIR-LARTILLOT-2023]

## Range and register

See practical_range above: roughly a violin's range shifted up about a whole step in the most common
tuning, confined to first position, with the exact pitch level a matter of player and instrument
preference rather than a fixed standard. Register colour across that range (where the instrument is
strong or thin) was not addressed by any source read this pass. [sourced: HFAA-GOLBER-1993 + to-verify: not opened this pass]

## Articulation and note transitions

Bowed articulation as on a violin, with the idiomatic difference that a melody line is very
frequently doubled with an adjacent, often open, string rather than played as a single line; ornament
carries much of the tradition's rhythmic and pitch-transition vocabulary and is treated as structural
rather than decorative, per `shared/MUSICAL_SYSTEMS/MODAL_FOLK_SYSTEMS.md` and
`shared/VIRTUAL_INSTRUMENT_GUIDE/CULTURALLY_SPECIFIC_INSTRUMENTS.md` step 2.3. [sourced: HFAA-GOLBER-1993 + inference]

## Physical constraints

One bow, four left-hand fingers, first position only. [sourced: HFAA-GOLBER-1993]

## Phrase behaviour

Not addressed by a source specific to this instrument this pass beyond the general bow-change
constraint any bowed instrument has. [to-verify: bow-change and phrase-length convention in slått
playing, not opened this pass]

## Ensemble behaviour

Traditionally solo. [sourced: TISMIR-LARTILLOT-2023 + to-verify: not opened
this pass]

## Recording behaviour

Not addressed by any source read this pass. [to-verify: recording convention specific to this
instrument, not opened this pass]

## Programming it: the control model

```text
tuning: A-D-A-E is the majority case, never the only case; state the tuning explicitly per piece,
  through shared/TUNING_AND_MPE.md, and never silently default to it or to 12-tone equal temperament
double_stops: written as real, simultaneous two-string texture, not as an occasional ornament layered
  onto a single melodic line
sympathetic_resonance: a real, pitch-selective resonance from four or five understrings, not a
  generic reverb tail; verify a chosen instrument actually models or samples it (see
  "What virtual implementations commonly get wrong")
springar_timing: an asymmetric triple metre with a named `microtiming_template`, scoped to a stated
  performer or corpus, never a uniform swing percentage or an even triple-metre grid
```
[sourced: HFAA-GOLBER-1993 + academic: TISMIR-LARTILLOT-2023]

## Programming it: what makes it sound real

- State the tuning per piece rather than assuming A-D-A-E, and route it through
  `shared/TUNING_AND_MPE.md` rather than quantising silently to 12-tone equal temperament. [sourced: HFAA-GOLBER-1993]
- Write the double-stopped texture the instrument actually plays, not a single melodic line with
  occasional double stops added as ornament. [sourced: HFAA-GOLBER-1993]
- Where a springar part is wanted, model the beat asymmetry as a named `microtiming_template`
  (`shared/HUMAN_PERFORMANCE_SCHEMA.md` section 3) scoped to a stated performer or corpus, and choose
  the correct sub-style's downbeat placement (Tele-springar versus Halling-springar are not
  interchangeable) rather than applying one generic "springar feel." [academic: TISMIR-LARTILLOT-2023; JOHANSSON-2017]
- Preserve ornament as real pitch-and-rhythm content in the part, per
  `shared/MUSICAL_SYSTEMS/MODAL_FOLK_SYSTEMS.md`, rather than as a humanisation layer added after the
  fact. [sourced: JOHANSSON-2017 + inference]

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Family- and tradition-specific tells:

- a twelve-tone-equal patch playing A-D-A-E (or another named tuning) as if it were just another
  violin tuning, with no audible sympathetic resonance; [sourced: HFAA-GOLBER-1993 + academic: TISMIR-LARTILLOT-2023]
- a single melodic line where the idiom calls for constant double stops; [sourced: HFAA-GOLBER-1993]
- a springar part quantised to an even triple metre, which removes the genre's defining asymmetry and
  is audible to anyone who knows the style, the same way a crossed clave orientation is audible in
  Cuban practice; [academic: TISMIR-LARTILLOT-2023; JOHANSSON-2017]
- applying the wrong sub-style's downbeat placement (treating a Halling-springar's short-beat downbeat
  as if it were Tele-springar's long-beat downbeat, or vice versa). [academic: JOHANSSON-2017]

## What virtual implementations commonly get wrong

The task brief's own framing names the core failure directly: a Hardanger fiddle patch played with no
sympathetic resonance modelled at all. Because the resonance is pitch-selective -- it depends on
which understrings are tuned to which related pitches, and which bowed pitch is exciting them -- a
generic reverb or convolution tail does not substitute for it; a reverb send colours everything played
through it equally, while sympathetic resonance responds more to some pitches than others depending on
the tuning in use that piece. [sourced: HFAA-GOLBER-1993 + academic: TISMIR-LARTILLOT-2023]

The second common failure is textural: treating the instrument as a solo violin voice and writing a
single melodic line, when constant double-stopping is the ordinary texture this instrument's flat
bridge and fingerboard exist to make possible. A "Hardanger-flavoured" single melodic line over
Western pop harmony, with no double stops, no scordatura and no springar asymmetry, is exactly the
"exotic flavour" failure `shared/MUSICAL_SYSTEMS/INDEX.md` rule 6 names, applied to this instrument.
[sourced: HFAA-GOLBER-1993 + inference]

The third is rhythmic: quantising a springar part to an even 3/4, or applying one generic "Nordic
folk swing" percentage regardless of sub-style, tune or performer, where the sourced material above
shows the asymmetry is real, systematic, and varies by named sub-style and by performer rather than
converging on one figure. [academic: TISMIR-LARTILLOT-2023; JOHANSSON-2017]

## What must not be generalised outside the tradition

- **A-D-A-E is the majority tuning, not "the" tuning.** Golber's own estimate is about three
  quarters of the repertoire; a substantial further set of named, piece-specific scordatura exists
  and should not be flattened into one default. [sourced: HFAA-GOLBER-1993]
- **The springar asymmetry figures in this page are each one measured instance** (one performer's
  recordings in TISMIR; specific named fiddlers' recordings in the older studies Johansson reviews),
  never "the" springar ratio, per `shared/MUSICAL_SYSTEMS/INDEX.md` rule 7. Johansson's review is
  explicit that this is an open, actively debated research question, not a settled number.
  [academic: TISMIR-LARTILLOT-2023; JOHANSSON-2017]
- **Tele-springar and Halling-springar place their downbeats differently**; do not apply one
  sub-style's convention to a tune associated with the other, and do not assume every springar tune
  belongs to only one sub-style, since Johansson notes the same melody can travel between regions and
  be felt differently in each. [academic: TISMIR-LARTILLOT-2023]
- **Do not extend this page's claims to the plain Norwegian violin tradition (vanlig fele) or to
  other Scandinavian fiddle traditions** (the Swedish polska traditions in particular), which
  `shared/MUSICAL_SYSTEMS/MODAL_FOLK_SYSTEMS.md` names as separate practices with their own
  construction and repertoire. [inference]
- **This page's technique claims (first position, west-coast versus inland setup) come from one
  luthier's article** aimed at instrument adjustment; they are not confirmed against a named
  performer or teaching lineage in this pass. [sourced: HFAA-GOLBER-1993]

## Restricted and ceremonial repertoire

The sources read this pass describe the slått repertoire as serving dancing, recreation and
ceremonial functions in rural Norwegian communities, without identifying any specific tunes,
occasions or repertoire as sacred, restricted, or closed to outsiders. **No source read in this pass
states that any part of the Hardanger fiddle repertoire is restricted in the way
`shared/MUSICAL_SYSTEMS/INDEX.md` rule 5 addresses**, but the absence of a finding is not the same as
a confirmed absence of restriction: none of the sources read this pass was a tradition bearer
specifically addressing this question, and the "ceremonial functions" mentioned in passing by the
TISMIR paper are not elaborated. This page therefore states plainly that it found nothing either
way, and treats the question as open rather than resolved. [to-verify: whether any named slått,
occasion or lineage-held tune carries restrictions, per a tradition-bearer or teacher source, not
opened this pass]

## What the Performance Director needs from this file

- `articulation_unavailable` is the expected outcome when a general-purpose bowed-string library is
  asked for this instrument's double-stopped, sympathetically-resonant texture; report it rather than
  approximating with a standard solo-violin patch.
- Do not proceed on an unanswered tuning check: per
  `shared/VIRTUAL_INSTRUMENT_GUIDE/CULTURALLY_SPECIFIC_INSTRUMENTS.md` step 0/2.1, name the piece's
  tuning before writing anything, and treat "A-D-A-E, unless stated otherwise" as a default to
  confirm, not to assume silently.
- A springar part's `timing_character.models` entry must be `microtiming_template`, named to a
  specific corpus or performer per `shared/HUMAN_PERFORMANCE_SCHEMA.md` section 3, with the correct
  sub-style's downbeat placement stated in the plan; treat a request for "springar feel" with no
  sub-style named as an unanswered check, per
  `shared/VIRTUAL_INSTRUMENT_GUIDE/CULTURALLY_SPECIFIC_INSTRUMENTS.md` section 8.
- Texture (double stops as the default, not the exception) and the sympathetic-resonance requirement
  belong in the plan as constraints, not stylistic preferences.

## Sources and what to verify

Full citations and read depth are in `research/sources/INSTRUMENT_SOURCES.md`; claim-by-claim
evidence and limits are in `research/instruments/HARDANGER_FIDDLE.md`. Left open by this pass, in
order of what would most improve the page: the HFAA's own scordatura-name compendium (reached, but
its table did not extract as text); register colour and phrase-length/bow-change convention (no
source read this pass addressed either); ensemble and duet practice; recording convention; vibrato
use; and whether any part of the repertoire is restricted or ceremonial in a way this pass's sources
did not surface.
