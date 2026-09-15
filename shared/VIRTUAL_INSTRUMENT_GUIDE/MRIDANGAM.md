# Mridangam

Traditions: Carnatic (South Indian) classical music. Context:
`shared/MUSICAL_SYSTEMS/RAGA_AND_TALA.md`.

The mridangam is a single-shell, double-headed barrel drum, the principal percussion instrument of
Carnatic music: one wooden body with two different, purpose-built heads at each end, played by one
seated player, who accompanies a soloist through a kutcheri (concert) and takes an unaccompanied solo,
the tani avartanam, within it. This page does not cover the Hindustani tabla, which descends from a
related archetypal barrel drum but is a separate instrument in a separate tradition with different
construction, tuning practice and accompanying role; see `shared/VIRTUAL_INSTRUMENT_GUIDE/TABLA.md` for the contrast, and do not
mix the two (Handbook rule 27).

> Evidence: read at `full` or `section` depth this pass: two lecture/monograph sources by the mridangam
> vidwan Umayalpuram K Sivaraman together with materials scientist T Ramasami (a 2010 National
> Institute of Advanced Studies memorial lecture, and a 2023 arXiv introductory review of their later
> book-length work "Musical Excellence of Mridangam"), which together are this page's practitioner
> source; C V Raman's two founding acoustics papers (1920, 1934/35), which treat the classical
> "Mridanga" as their primary worked example; one further academic paper modelling the loaded
> membrane generally across the Indian drum family (Malu and Siddharthan 2000); and IIT Madras course
> material on the mridangam (a construction sub-page and a slide deck from the "Science of Musical
> Instruments" course, M Ramanathan, hosted at ed.iitm.ac.in as named in the task brief), read for
> construction and concert-structure detail the acoustics sources do not cover. David Courtney's
> tabla/mridangam contrast piece was also read and is cited where it speaks directly to mridangam
> construction and role, cross-checked against the sources above. No dedicated ethnomusicological
> monograph on Carnatic percussion (comparable to Kippen's tabla study) was opened this pass. Source
> IDs resolve in `research/sources/INSTRUMENT_SOURCES.md`; claims and their limits are in `research/instruments/MRIDANGAM.md`.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## Behaviour cards

### Mridangam (valanthalai and thoppi)

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | One barrel-shaped wooden shell (traditionally jackfruit-tree wood), open at both ends, each end covered by a different multi-layer skin head bound to the shell by buffalo-hide straps: the right head (valanthalai), which carries the permanent black patch (karanai), and the left head (thoppi/edanthalai), which does not. Both heads are tensioned by straps running the length of the shell, so, unlike the tabla's two independent shells, the two membranes share one resonating body and are more directly coupled to each other. | sourced: SIVARAMAN-NIAS-2010; KUMAR-REVIEW-2023 + academic: RAMAN-1935 |
| attack_behavior | Seven named strokes are each a distinct strike position, hand shape and finger combination, not a loudness tier of a smaller set: dheem, chappu, nam and araichappu on the black-patch region of the valanthalai; dhi and ta closer to or on the black patch's centre; thom (open) and gumki (a modulating technique between thom strokes) on the thoppi. | sourced: KUMAR-REVIEW-2023; SIVARAMAN-NIAS-2010 |
| sustain_behavior | Open strokes (dheem, chappu, thom) ring with a genuinely harmonic, sustained decay; closed strokes (ta, dhi) are short and largely non-resonant even though FFT analysis shows dhi still carries measurable harmonic content. Chappu's second-harmonic peak sustains longest of the right-head strokes, for up to a few seconds on a well-made drum. | sourced: KUMAR-REVIEW-2023 |
| release_behavior | As with the tabla, release is a player action rather than a passive decay: an open stroke is allowed to ring, a closed stroke is stopped by hand position at the moment of the strike rather than by a separate damping gesture afterward. | inference |
| dynamic_timbre_change | unresolved: no source read this pass gives a systematic account of how mridangam spectral balance shifts with dynamic level at a fixed stroke; the acoustic sources compare strokes and construction variants (kucchi vs thool, cow-skin vs goat-skin membranes) at a presumably fixed playing dynamic, not dynamic range on one stroke. | to-verify: a dynamics-focused acoustic study of mridangam strokes, not found this pass |
| register_character | The valanthalai is the tuned, harmonically rich treble voice, with chappu (the tuning stroke) and araichappu (an upper-octave stroke with no equivalent on the tabla) its clearest pitched strokes. The thoppi is the bass voice; it is not permanently loaded but, when loaded in performance with a temporary paste, develops genuine measurable harmonic content of its own, broader and less sharp than the valanthalai's. | sourced: KUMAR-REVIEW-2023 |
| practical_range | Not a scale instrument: the valanthalai's chappu stroke is tuned, per performance, to Sa (Shadjam/Aadhara Shadjam), matching the accompanied soloist's tonic, exactly as the tabla's dāyāṅ is tuned to the soloist's Sa. The thoppi's tuned bass note is reported two different ways across the sources read this pass: one IIT Madras course source states its shruti is one octave below the right head's; the review of Sivaraman and Ramasami's later work states the thom stroke is tuned to Pa (the fifth) of the lower octave. These are not the same claim (Sa an octave down versus Pa of the octave down), and this page does not silently resolve the discrepancy. | sourced: IITM-MRIDANGAM-PARTS + academic: KUMAR-REVIEW-2023 + to-verify: or whether both are attested practices |
| tessitura | As with the tabla, not applicable in the melodic-instrument sense: each head sits at one tuned reference pitch for the performance rather than moving through a comfortable middle register. | inference |
| articulation_logic | The seven named strokes (dheem, chappu, nam, araichappu, dhi, ta, thom, gumki) are the primary vocabulary; course material further groups basic strokes under mnemonic names (tha, thi, thom, nam; ta, dhim, chappu-full, chappu-half) that function, like tabla bols, as both the spoken syllable and the name of the physical stroke. Combinations of these form nadai, the running figuration used to follow (accompany) a piece, articulated at different speed tiers (keezhkalam, madhyama kaalam, mel kaalam) and different subdivision counts (chatushram, thisram, kantam, mishram, sankeernam) that match the gati/nadai categories of Carnatic tala theory. | sourced: KUMAR-REVIEW-2023; IITM-MRIDANGAM-SLIDES |
| phrase_limits | Bounded by the same two-hand alternation limits as any hand-struck drum, and by the tala cycle (avartanam) rather than by breath; solo structures built for the tani avartanam (korvai and its relatives) are composed to specific arithmetic lengths that resolve precisely onto the cycle's return point. | sourced: IITM-MRIDANGAM-SLIDES + inference |
| transitions | No legato; every stroke is a discrete strike, as on the tabla. What functions as a phrase-level resolution device is the korvai and the mora/mukthayam family, discussed under Idiomatic phrasing below, not a glide or overlap between notes. | inference |
| repeated_note_behavior | unresolved: no source read this pass gives a mridangam-specific account of how fast repeated figures are distributed across the hands (the equivalent of tabla's rela); nadai figuration is documented as a category (see articulation_logic) but not at the level of sticking/hand-alternation detail. | to-verify: a technique-focused source on mridangam hand alternation in fast figuration |
| vibrato | Not applicable to the valanthalai's fixed-pitch strokes; the thoppi's gumki is a related but distinct technique, covered under pitch_instability. | inference |
| pitch_instability | Gumki is a left-hand technique, played between thom strokes, that modulates the thoppi's harmonicity; Sivaraman himself likens its sound to "the cooing of a dove." It is documented here as a modulation of tonal quality more than a directional pitch bend in the tabla bāyāṅ sense, and no source read this pass gives a mechanical account (force, hand position) comparable to what is available for the tabla's Ga stroke. | sourced: KUMAR-REVIEW-2023 + to-verify: in a technique-focused source |
| resonance | Because both heads share one resonating shell, Raman and later researchers asked whether that coupling is necessary to the drum's harmonic character; a direct FFT comparison against the tabla (whose two heads are only air-coupled through separate shells) found that both instruments can produce harmonic spectra, so the shared shell is not what makes the mridangam harmonic — the loaded black patch is doing that work in both instruments. The valanthalai's dheem stroke excites a fundamental measured about 7 percent sharp of where the rest of the harmonic series would place it, so, as with the tabla, the drum's perceived pitch on some strokes is the ear's extrapolation past a genuinely shifted or absent fundamental. | academic: KUMAR-REVIEW-2023; RAMAN-1935 |
| physical_noise | Hand and finger contact noise is part of stroke identity, as on any hand-struck drum; no source read this pass gives mridangam-specific detail beyond this general point. | inference |
| feasibility | Two hands, one per head; the physical-alternation and simultaneity limits are the same as any hand-struck drum. Whether a given korvai or nadai figure is playable at the intended tempo depends on the same hand-alternation limits documented generally in `HAND_PERCUSSION.md`. | inference |
| ensemble_behavior | The mridangam accompanies a soloist (vocalist or melodic instrumentalist) through the concert's composed pieces (kritis and related forms), typically alongside a violin also accompanying the soloist, and often alongside further percussion (ghatam, kanjira, morsing); within the concert it also takes an unaccompanied solo, the tani avartanam, usually following a major piece. Unlike the tabla, the mridangam does not carry the sole responsibility for making the cycle legible: a conventionally established pattern of audience and performer claps and waves does that job, which is part of why mridangam accompaniment has more latitude than tabla's theka discipline requires. | sourced: COURTNEY-CONTRAST; IITM-MRIDANGAM-SLIDES |
| recording_behavior | unresolved: no source read this pass addresses conventional miking or studio placement for mridangam specifically. | to-verify: a recording-engineering source addressing mridangam miking |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Each stroke is a discrete strike; note length mainly selects between a recorded open decay and a recorded closed/damped decay rather than shaping the sound continuously, as with the tabla. | inference |
| overlap | Not a legato or monophonic-transition instrument. | inference |
| velocity | Should not be the sole selector across the seven-stroke vocabulary; each named stroke (dheem, chappu, nam, araichappu, dhi, ta, thom, gumki) is measurably spectrally distinct by FFT, not a loudness tier of a smaller set, so a faithful instrument needs one articulation per stroke with velocity controlling force within it. | academic: KUMAR-REVIEW-2023 + inference |
| continuous_dynamics | unresolved: no source read this pass describes a continuous in-note control need for the mridangam comparable to the tabla's bāyāṅ bend; gumki (see pitch_instability) may need one, but the mechanism was not sourced clearly enough this pass to specify how. | to-verify: as pitch_instability |
| expression | unresolved: no source addressed an expression/trim lane distinct from velocity for a modelled or sampled mridangam. | to-verify: a virtual-instrument control-mapping source for mridangam |
| articulation_switching | The seven-stroke vocabulary (plus the mnemonic-name groupings in articulation_logic) is large enough that keyswitch or separate-patch selection per stroke is needed to preserve it, exactly as reasoned for the tabla's larger bol set. | sourced: KUMAR-REVIEW-2023 + inference |
| round_robins | Fast nadai figuration repeats short patterns; round robins matter for the same general reason they matter on any fast hand-struck drum, though no source read this pass measured mridangam-specific repetition thresholds. | inference |
| release_samples | The difference between an open stroke's genuine ring and a closed stroke's short, largely non-resonant decay (per sustain_behavior) needs two different recordings, not a gain or EQ variant of one recording. | sourced: KUMAR-REVIEW-2023 + inference |
| pedal_or_breath_behavior | Not applicable; no pedal, no breath component. | inference |
| transition_samples | Not applicable between discrete strokes. Gumki, if modelled, needs its own in-note modulation behaviour rather than a borrowed pitch-bend or legato-transition sample, per pitch_instability, but the mechanism to model was not sourced clearly enough this pass to specify further. | inference |
| mic_or_room_behavior | unresolved: see recording_behavior above. | to-verify: as recording_behavior |
| likely_fake_sounding_errors | Collapsing the seven-stroke vocabulary onto one or two samples and a velocity curve; a thoppi with no temporary-loading behaviour modelled at all, so the bass head is always thin and inharmonic rather than genuinely tuned; a valanthalai tuned to 12-tone-equal rather than to the soloist's actual Sa; accompaniment programmed as a fixed looped pattern in the manner of a tabla theka, which misrepresents a tradition whose mridangam part is not built on a theka at all (see Idiomatic phrasing below and `shared/MUSICAL_SYSTEMS/RAGA_AND_TALA.md`). | sourced: KUMAR-REVIEW-2023 + inference |
| organic_programming_methods | Select articulation by named stroke, not by velocity layer alone, per articulation_switching [academic: KUMAR-REVIEW-2023]. Tune the valanthalai's chappu to the accompanied soloist's actual Sa for the piece, per practical_range [sourced: IITM-MRIDANGAM-PARTS]. Model the thoppi's temporary loading as a real, settable state (a "patch" applied for the performance, not a fixed factory pitch), since the source instrument itself is retuned this way session to session [sourced: KUMAR-REVIEW-2023]. Build accompaniment from Carnatic tala's actual angas and the piece's nadai/gati, not from a borrowed theka concept, since the mridangam does not carry a fixed accompanying pattern the way tabla does [sourced: COURTNEY-CONTRAST]. Where a solo passage is wanted, model it as a korvai (an arithmetically resolved concluding phrase) or a related tani-avartanam form rather than as generic fills [sourced: IITM-MRIDANGAM-SLIDES]. | sourced: IITM-MRIDANGAM-PARTS; COURTNEY-CONTRAST; IITM-MRIDANGAM-SLIDES + academic: KUMAR-REVIEW-2023 |

---

## Tradition and context

### Construction

The shell is a single hollowed barrel, traditionally turned from jackfruit-tree wood, in a small
number of conventional sizes (one source gives roughly 22, 23 and 24 inches; a separate IIT Madras
course source instead distinguishes two named varieties by head diameter, "Thagu Shruthi", roughly 24
to 26 inches, and "Sthaayi Shruthi", roughly 20 to 22 inches — these figures are not necessarily
measuring the same dimension across the two sources, and this page reports both rather than picking
one) [sourced: KUMAR-REVIEW-2023; IITM-MRIDANGAM-SLIDES]. The right head (valanthalai) is a stack of
layers: an inner disc of buffalo-skin parchment (ulkaraithattu) tied directly to the shell; the main
resonating membrane (kottuthattu/paatuthattu), typically goatskin, which carries the black patch; and
an outer disc (vettuthattu), typically cowskin. The annular space between the main membrane and the
outer disc is packed either with radial strips of reed or pine ("kucchi") or with pieces of black-patch
material ("thool"), by player preference — the two give audibly different tonal balance, discussed
under Idiomatic phrasing below. The left head (thoppi/edanthalai) is made from thicker buffalo
parchment and is not permanently loaded [sourced: KUMAR-REVIEW-2023]. Construction uses far more
insertion/lacing points than the tabla: 48 on the right membrane and 36 on the left, for even tension
distribution, with a separate 16-point strap finally joining the two heads across the shell and setting
the working tension — the same sixteen-point figure Raman found essentially universal across this whole
drum family (Mridanga and Thabla alike) [sourced: KUMAR-REVIEW-2023 + academic: RAMAN-1935]. The black
patch (karanai) is a paste of ferric-oxide powder (and, per one IIT Madras source, manganese powder,
rice and iron powder) applied to the kottuthattu in sequential layers over a rice-based adhesive, built
up in a density gradient from centre to edge that is what actually produces the harmonic mode structure
[sourced: KUMAR-REVIEW-2023; IITM-MRIDANGAM-PARTS].

### Tuning

The valanthalai is tuned, via the chappu stroke, to the tonic (Sa/Shadjam) of the soloist being
accompanied, matching that performance's Aadhara Shadjam exactly as the tabla's dāyāṅ is tuned to its
soloist's Sa [sourced: IITM-MRIDANGAM-PARTS + academic: KUMAR-REVIEW-2023]. The thoppi is not
permanently loaded; before a performance it is loaded with a temporary paste of semolina/cream-of-wheat
(rava) mixed with water, adjusted to bring it to its intended bass pitch, and this paste is later
removed — a genuinely different tuning workflow from the valanthalai's fixed black patch. Sources
disagree on exactly what that bass pitch is (see practical_range above: one octave below the right
head's Sa, versus Pa of the lower octave), and this page does not resolve that disagreement [sourced: IITM-MRIDANGAM-PARTS + academic: KUMAR-REVIEW-2023]. As on the tabla, the ear perceives a clear pitch
from strokes whose measured fundamental is shifted or suppressed relative to the harmonic series set by
the higher partials; chappu itself primarily excites the second harmonic, not the fundamental, yet is
the stroke used to tune the drum [academic: KUMAR-REVIEW-2023; RAMAN-1935].

### Note production and technique

The seven strokes named in the behaviour card are the core technical vocabulary; see articulation_logic
and attack_behavior above. Kucchi versus thool construction (see Construction) is also, in effect, a
technique-adjacent choice made once when the drum is built or re-headed rather than per performance: FFT
comparison shows dheem and nam more prominent on thool-filled drums, and chappu and araichappu more
prominent on kucchi-filled drums, because the two filling methods suppress different vibrational mode
shapes (kucchi's radial strips damp modes with nodal circles — dheem and nam — while leaving modes with
nodal diameters, chappu and araichappu, undamped; uniformly distributed thool material does the
reverse) [academic: KUMAR-REVIEW-2023]. Whether the mnemonic stroke names used in teaching and playing
(tha, thi, thom, nam and related syllables) function as a distinct spoken performance practice
(comparable to Hindustani bol-recitation, or to what is more widely called konnakol/sollukattu in
Carnatic contexts) separately from their use as playing instructions was not addressed in depth by any
source read this pass; this page treats the syllables only as stroke names here, and does not claim
konnakol as a documented solo vocal art form on the strength of these sources alone [to-verify: a
source specifically addressing konnakol/sollukattu as vocalised performance, distinct from stroke
naming].

### Idiomatic phrasing and ornamentation

The tani avartanam, the mridangam's (and, where present, other percussionists') unaccompanied solo
within a kutcheri, is built from named forms documented in IIT Madras course material: korvai, a
composed, arithmetically resolved concluding phrase, often organised in two named halves (poorvanga and
uttaranga) and typically presented at a given nadai (rhythmic subdivision) and repeated three times;
korappu, a linking or trading passage used when more than one percussionist performs together; mohra, a
short flourish; and mukthayam, a concluding cadence. A separate, easily confused term, karvai, names a
sustain or held pause rather than korvai's structured phrase — the source that documents this
explicitly flags the two as commonly mixed up. Where a phrase begins relative to the beat (samam, on the
beat, versus eduppu, an offset start) governs how a rendered korvai or accompanying figure is heard
against the cycle [sourced: IITM-MRIDANGAM-SLIDES]. This page found no correspondingly detailed
source-backed account of ornamentation in the melodic-instrument sense (there is none analogous to
gamaka here); the closest analogue is gumki's tonal modulation of the thoppi, covered under
pitch_instability, which remains only lightly sourced this pass.

### Performer interaction and ensemble role

**The mridangam does not play a theka.** Sam, khali and theka are Hindustani terms belonging to tabla
accompaniment (see `shared/VIRTUAL_INSTRUMENT_GUIDE/TABLA.md` and `shared/MUSICAL_SYSTEMS/RAGA_AND_TALA.md`, which already states
this explicitly and which this page is written to agree with, not to quietly contradict). Where the
tabla is solely responsible for keeping the cycle legible to a Hindustani soloist, Carnatic performance
distributes that job more broadly: a conventionally established pattern of claps and waves, performed
by the soloist, the mridangam player and often much of the audience together, carries the cyclic
reference, which is part of why the mridangam has more latitude in what it plays during accompaniment
than tabla's theka discipline allows [sourced: COURTNEY-CONTRAST]. Within a kutcheri the mridangam
follows the soloist's rendering of the kriti and related composed forms via nadai figuration (see
articulation_logic), and takes its own unaccompanied showcase, the tani avartanam, typically after a
major piece, structured around the forms named under Idiomatic phrasing above [sourced: IITM-MRIDANGAM-SLIDES]. A violin is a common further accompanist to the soloist alongside the
mridangam, and further percussion (ghatam, kanjira, morsing) is common in concert alongside it; where
these are present, korappu-style trading passages are part of how multiple percussionists interact
within the tani avartanam [sourced: IITM-MRIDANGAM-SLIDES].

### Repertoire contexts

Accompaniment of the composed forms of a Carnatic kutcheri (kritis and related pieces, and the
improvised sections around and inside them, per `shared/MUSICAL_SYSTEMS/RAGA_AND_TALA.md`), and the
tani avartanam solo, are this page's documented repertoire contexts; no source read this pass names a
dedicated solo-recital format for mridangam comparable to a tabla solo concert, and this page does not
claim one exists.

### Improvisation

The tani avartanam mixes composed material (a fixed korvai, prepared and rehearsed) with real-time
invention within the tala cycle and the nadai/gati framework, bounded the same way tabla solo
improvisation is bounded (per `shared/MUSICAL_SYSTEMS/RAGA_AND_TALA.md`'s general account of
bounded-improvisation in both Hindustani and Carnatic practice): freedom of realisation inside a strict
grammar, not free improvisation. This page does not go further than that general framing; a
tani-avartanam-specific account of how much of a given solo is composed versus invented in real time
was not found in a source read this pass. [to-verify: a source giving the composed/improvised balance
specifically within a tani avartanam]

---

## What virtual implementations commonly get wrong

- **Strokes mapped to velocity only.** As with tabla, collapsing the seven-stroke vocabulary onto one
  or two recordings and a velocity curve loses genuinely distinct, FFT-measurable strokes; dheem, nam,
  chappu and araichappu are not loudness tiers of each other [academic: KUMAR-REVIEW-2023].
- **The valanthalai retuned to 12-TET instead of the soloist's Sa.** The chappu stroke's tuning is
  chosen per performance against the accompanied soloist's actual tonic, not an abstract pitch class
  [sourced: IITM-MRIDANGAM-PARTS].
- **A thoppi treated as a fixed, inharmonic bass sample.** The left head's temporary rava loading gives
  it genuine, measured harmonic content that a fixed, unloaded-membrane sample would lack entirely
  [academic: KUMAR-REVIEW-2023].
- **Accompaniment built as a tabla-style looped theka.** The mridangam's accompanying part is not built
  on a fixed theka; treating it as one imports a Hindustani structural concept into a Carnatic
  instrument that does not use it, which is exactly the error `shared/MUSICAL_SYSTEMS/RAGA_AND_TALA.md`
  and this page both warn against [sourced: COURTNEY-CONTRAST].
- **Perceived pitch treated as measured pitch.** As with tabla, some strokes (dheem in particular) have
  a measurably shifted or effectively absent fundamental, so trusting the loudest spectral peak rather
  than modelling the ear's extrapolation will misidentify the drum's actual tuned note [academic: KUMAR-REVIEW-2023; RAMAN-1935].

## What must not be generalised outside the tradition

- Mridangam construction, tuning and role are specific to Carnatic practice and must not be read onto
  the Hindustani tabla, a related but distinct instrument in a distinct tradition; see `shared/VIRTUAL_INSTRUMENT_GUIDE/TABLA.md`
  [sourced: COURTNEY-CONTRAST].
- The kucchi/thool construction choice is a genuine, audible fork in the tradition's own practice
  (Umayalpuram Sivaraman himself is named as a kucchi player; other named mridangists use kappi/thool)
  and is a matter of personal and lineage preference, not a right-versus-wrong construction choice; this
  page does not treat one as more authentic than the other [sourced: KUMAR-REVIEW-2023; IITM-MRIDANGAM-SLIDES].
- The two disagreeing figures for the thoppi's tuned pitch (one octave below Sa, versus Pa of the lower
  octave) are both stated in sources read this pass; neither should be generalised as "the" answer until
  the discrepancy is resolved (see practical_range).

## Restricted and ceremonial repertoire

No source read this pass identifies mridangam repertoire as sacred, ceremonial or lineage-restricted in
the way `shared/MUSICAL_SYSTEMS/INDEX.md` rule 5 anticipates for some traditions; the repertoire
documented here (kutcheri accompaniment of kritis and related composed forms, and the tani avartanam
solo with its korvai-based structure) is concert and pedagogical material, openly taught, performed and
published, including by the mridangam vidwan whose own work is this page's primary practitioner source.
This page found nothing indicating a restricted category and states plainly that this question was not
independently pursued with a tradition bearer this pass beyond what the read sources themselves state;
if the user or a future agent has reason to believe otherwise for a specific composition or lineage-held
item, treat that as open and ask rather than assuming this page's silence means clearance. [to-verify: direct confirmation from a tradition bearer or teacher was not separately sought this pass]

## What the Performance Director needs from this file

- `articulation_unavailable` is the expected result whenever a general hand-percussion or "world
  percussion" library is asked for named mridangam strokes; report it rather than substituting a
  different tradition's stroke or a pitch-shifted sample.
- Do not build mridangam accompaniment from a tabla-style theka structure or vocabulary; route to
  `shared/MUSICAL_SYSTEMS/RAGA_AND_TALA.md` for Carnatic tala's own angas, and to the nadai/gati
  categories named under articulation_logic here.
- `performance_reference` (`shared/HUMAN_PERFORMANCE_SCHEMA.md`) should record at minimum the
  accompanied soloist's tonic (for valanthalai tuning), whether the thoppi is being modelled as
  freshly loaded for the session, and whether the part is kutcheri accompaniment or a tani avartanam
  solo, since these call for materially different plans.
- The thoppi's disputed tuned pitch (see practical_range) is an open question this file does not
  resolve; a plan that depends on the exact interval should flag it rather than assume either reading
  silently.

## Sources and what to verify

Full citations and read depth are in `research/sources/INSTRUMENT_SOURCES.md`. Left open by this pass, and what would
settle each: a dynamics-focused acoustic study of mridangam strokes (dynamic_timbre_change); resolution
of the thoppi's tuned-pitch discrepancy between "one octave below Sa" and "Pa of the lower octave"
(practical_range); a technique-focused source on the physical mechanism of gumki
(pitch_instability, continuous_dynamics, transition_samples); a technique-focused source on hand
alternation in fast nadai figuration (repeated_note_behavior); a source specifically addressing
konnakol/sollukattu as a vocalised performance practice distinct from stroke naming (Note production
and technique); a recording-engineering source on conventional mridangam miking (recording_behavior,
mic_or_room_behavior); a source giving the composed/improvised balance specifically within a tani
avartanam (Improvisation); direct confirmation from a tradition bearer on restricted repertoire, if any
exists (see above). No dedicated ethnomusicological monograph on Carnatic percussion technique or
lineage (comparable to Kippen's tabla study) was identified or opened this pass; finding and reading one
would be the single highest-value addition to this page.
