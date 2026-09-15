# Guitar: research records

What was read, what was not, and the limits of each claim the guide page makes. The page carries
the conclusions; this file carries the evidence.

## Scope and method

Steel-string acoustic, nylon-string classical and electric (magnetic-pickup) six-string guitar in
standard and common alternate tunings. Thirteen sources were opened and read at section depth: six
academic acoustics/music-computing papers, one academic dissertation on heavy-metal harmony and
distortion acoustics, two public-domain orchestration treatises (Forsyth 1914, Berlioz/Strauss), one
public-domain pedagogy method (Sor), two UNSW Music Acoustics pages, and two performer-pedagogy web
pages (rasgueado, rest/free stroke). All were fetched and read in this session; none were cited from
memory or from a search snippet alone unless marked `excerpt` or `to-verify` below.

Standard references named in the 2.0 page (Adler, Fletcher and Rossing) were not opened for this
pass either; they are registered as `not-read` `standard reference` rows (ADLER-ORCH,
FLETCHER-ROSSING-1998) and, where the 2.0 page cited them, this pass replaces the claim with an
opened source where one exists, and leaves the rest `to-verify`.

The pedal-foot assignment for harp, confirmed directly against Forsyth's and Rimsky-Korsakov's
orchestration chapters, is recorded in `research/instruments/HARP.md` rather than here; both sources
were read primarily for the harp page.

Not reachable: a controlled, notated study of palm-mute damping time or fret-hand release timing in
milliseconds. No such source could be found; the release-behaviour claims in the page are sourced
only as far as the mechanism (what a player does), not a magnitude.

## Records

### GTR-01 Strum spread is measurable and chord-type dependent
- claim: strummed and arpeggiated chords have a measured, non-zero spread between the attack of
  each string, and the spread differs by chord density, tempo and whether the chord is a block
  chord, a strummed chord, or an arpeggio.
- source: FREIRE-STRUM-2018 (section)
- source_type: academic acoustics (Sound and Music Computing conference)
- confidence: medium
- scope: one nylon-string classical/folk guitar, hexaphonic-pickup capture, three musicians, three
  notated accompaniment excerpts (a slow arpeggiated piece, a guarania pattern, and "Wonderwall").
  Not a cross-genre or cross-instrument sample.
- limitations: three performers, three excerpts. The paper itself frames the numbers as
  "preliminary empirical limits," not a general law, and explicitly invites replication. Figures are
  means per rendition, with real spread within each mean.
- inference: none for the numbers themselves. The page's recommendation to vary spread by chord
  density and tempo, rather than use one constant, is a direct reading of the paper's own framing.

### GTR-02 Repeated/tremolo notes are regular in timing but not perfectly uniform, and regularity tracks skill more than dynamics does
- claim: skilled classical guitarists play tremolo (rapid repeated-note) passages with more rhythmic
  regularity than less-skilled players, but note-duration and dynamic (loudness) regularity do not
  track skill the same way; even trained players do not produce identical repeated notes.
- source: FREIRE-TREMOLO-2013 (section)
- source_type: academic acoustics (Sound and Music Computing conference)
- confidence: medium
- scope: acoustic nylon guitar, hexaphonic pickup, four guitarists of differing experience playing
  five renditions of one tremolo excerpt.
- limitations: small sample (four players), one excerpt, one instrument. A "preliminary" study by
  the authors' own description.
- inference: the page's general claim that tremolo should never be programmed as identical repeated
  samples follows directly; the specific recommendation to model timing regularity as a skill/style
  dial rather than a flat velocity randomisation is this pack's synthesis of the finding, flagged as
  such.

### GTR-03 Plucking point changes spectral content in a predictable, measurable way
- claim: plucking near the bridge (sul ponticello) produces a softer, brighter, harder tone rich in
  high harmonics; plucking near or over the fingerboard (sul tasto) produces a mellower, louder tone
  with fewer high harmonics. The mechanism is that the plucking point is (approximately) a node for
  harmonics that are multiples of the reciprocal of the plucking-point fraction, so those harmonics
  are suppressed.
- source: TRAUBE-2000 (section)
- source_type: academic acoustics (DAFX conference)
- confidence: medium
- scope: classical guitar, ideal and real string plucking models, developed for automatic
  plucking-point estimation from recordings.
- limitations: the mechanism itself rests on standard ideal-string plucking physics (high
  confidence), but the paper is about *estimating* pluck position from audio, not a perceptual study
  of how listeners judge the resulting timbre, and it notes real plucks are not ideal point-plucks;
  the "softer, brighter, sharper" wording is the paper's own descriptive language, carried over
  rather than independently verified perceptually here.
- inference: none for the mechanism. The instruction to treat pluck position as a continuous timbral
  control (not just a dynamic one) is the page's synthesis.

### GTR-04 Electric pickup position changes brightness via a comb-filter mechanism, not just "position feel"
- claim: a magnetic pickup senses string velocity at a fixed point; because the string vibrates in
  standing-wave modes, this produces a comb-filter response, attenuating the harmonics that have a
  node near the pickup. A bridge-position pickup is measurably brighter than a neck-position pickup
  because of where the resulting comb-filter nulls fall, not because of a vague "output level"
  difference.
- source: PAIVA-PICKUPS-2012 (section)
- source_type: academic acoustics (AES Journal)
- confidence: high
- scope: magnetic pickups on steel strings generally (guitar and, by the same electromagnetic
  mechanism, bass); the paper explicitly frames this as a general pickup-position model, not one
  instrument's patch.
- limitations: the paper models an idealised waveguide string and a single pickup; real instruments
  add body resonance and player variability on top. It does not address active/humbucker circuit
  coloration beyond the position effect itself.
- inference: none for the mechanism. Extending the same mechanism to bass pickups (used in BASS.md)
  is a direct, uncontroversial application of the same physics, not a new claim.

### GTR-05 Fretting a string sharpens its pitch, and the amount is measurable
- claim: pressing a string down to a fret stretches it slightly, raising its pitch above the
  theoretical fretted pitch (the "ideal string" calculation). Measured deviation without saddle
  compensation ranged from about 14 to 64 cents sharp across the fretted notes tested; standard
  compensation (moving the saddle back) reduces this to within about ±8 cents, inside the
  instrument's audible pitch-discrimination range.
- source: VARIESCHI-2009 (section)
- source_type: academic acoustics (arXiv, physics education)
- confidence: high
- scope: a purpose-built monochord sonometer strung and fretted like a guitar/mandolin, not a
  production guitar; three strings measured.
- limitations: the instrument is a laboratory model, not a commercial guitar, though built to the
  same geometry. The exact cents figures are specific to that instrument's string gauge and action;
  the *existence and direction* of the sharpening effect, and the order of magnitude, generalise.
- inference: the page's guidance that heavier fretting pressure (e.g. a hard barre, or a bend held
  under pressure) sharpens pitch further, beyond what saddle compensation fixes, is a direct
  extension of the paper's mechanism (more string stretch = more sharpening) rather than a
  separately measured claim, and is labelled inference where stated that way.

### GTR-06 Root-and-fifth power chords under distortion produce consonant, not absent, intermodulation
- claim: nonlinear distortion generates both harmonic distortion (new overtones of each note) and
  intermodulation/combination-tone distortion (sum and difference frequencies between notes sounding
  together). For a root-and-fifth (or root-and-fourth) interval, the resulting combination tones
  closely reinforce the harmonic series of the root, which is why the power chord reads as
  consolidated and "powerful" rather than muddy under heavy gain; a major third under the same gain
  produces combination tones that do not reinforce the series as cleanly, and read as more complex.
- source: LILJA-2009 (section)
- source_type: academic acoustics (PhD dissertation)
- confidence: high
- scope: electric guitar under distortion, low-register open-position power chords, primarily in a
  heavy-metal harmonic-practice context.
- limitations: the acoustic mechanism itself is high confidence (the dissertation includes original
  spectral measurements, credited to Dr. Henri Penttinen, made specifically to test this), but the
  broader "power chord = privileged consonance" framing is the author's own analytical argument built
  on the acoustics, and its consonance/dissonance classification is explicitly presented as the
  author's own division for analysing a specific repertoire, not a universal psychoacoustic law. This
  pack uses only the acoustic claim (combination tones exist and where they fall), not the broader
  harmonic-analysis framework.
- inference: none for the acoustic claim itself, which corrects the old page's implication that
  distorted power chords are acoustically "simple" or empty of interaction.

### GTR-07 Fret-hand release is how a classical guitarist stops or dampens a note, not the picking hand
- claim: to produce a staccato or damped ("buffed"/etouffe) note on guitar, the player does not use
  the picking hand; instead the fretting hand either releases pressure on the string (without
  leaving it) to stop the note, or presses more lightly than normal (not light enough to produce a
  harmonic) to damp it while it continues to sound briefly.
- source: SOR-METHOD (section)
- source_type: pedagogy (public-domain method)
- confidence: medium
- scope: nylon-string (historically gut-string) classical guitar, right/left hand roles as taught by
  Sor.
- limitations: as a description of classical-era technique still taught today, confidence in the
  mechanism is high; but the source is old (early 19th century) and does not cover steel-string or
  electric-specific palm-muting, which is a picking-hand technique on those instruments and is
  treated separately, as inference, on the page.
- inference: none for the mechanism described. The generalisation that "release is a fretting-hand
  decision, not silence" is the page's synthesis of this and general fretted-instrument mechanics.

### GTR-08 Body resonance: the top plate is a radiator, not an amplifier, and has identifiable resonance regions
- claim: the guitar body does not add energy; it converts string vibration (via the bridge) into a
  larger-area, more efficient radiator of the same energy. Most guitars show three strong body
  resonances clustered in roughly the 100-200 Hz region, from top/back plate coupling and the
  Helmholtz (air-cavity) mode enabled by the sound hole; higher-frequency top-plate modes are weaker
  radiators but still colour the tone.
- source: UNSW-GUITAR-INTRO (section); UNSW-GUITAR-MODES (section)
- source_type: academic acoustics (university research-group public pages)
- confidence: medium
- scope: general steel-string and classical guitar body acoustics.
- limitations: these are public-education pages from an active acoustics research group, not the
  underlying peer-reviewed papers themselves, so treated as one step more informal than the
  DAFX/AES/arXiv sources above. The fetched pages did not give exact resonance frequencies for a
  specific instrument (those vary by build), only the general region and mechanism.
- inference: none for the mechanism.

### GTR-09 Open strings vibrate sympathetically with a played string's harmonics
- claim: plucking one string can set another, un-struck open string vibrating if the played string
  produces a harmonic close to the other string's fundamental, driven through the bridge/body rather
  than through the air. Example given: plucking the low E string (anywhere except near its own
  one-third point) can set the B string vibrating sympathetically via a shared harmonic.
- source: UNSW-GUITAR-INTRO (section)
- source_type: academic acoustics
- confidence: medium
- scope: standard-tuned six-string guitar.
- limitations: stated as a general mechanism with one worked example, not a measured survey of which
  string pairs couple most strongly on which instruments; does not quantify how audible or how common
  this is across playing situations, so this pack treats it as a real but secondary resonance effect,
  not a dominant one.
- inference: the recommendation to leave other strings free to ring (not damped) so this coupling can
  happen is the page's synthesis, not a separately sourced recommendation.

### GTR-10 Rasgueado is a sequence of individually flicked fingers striking with the back of the nail, not a strum
- claim: rasgueado differs mechanically from a strum: each finger (typically pinky, ring, middle,
  index in sequence, or a 4-stroke variant omitting the pinky) extends outward and strikes with the
  back of the fingernail, each stroke separate from the next rather than a single continuous sweep,
  producing a rapid, percussive, near-simultaneous-sounding attack.
- source: NIEDT-RASGUEADO (section)
- source_type: performer
- confidence: medium
- scope: flamenco/classical rasgueado technique generally.
- limitations: this is one experienced teacher's description, not a cross-checked academic source;
  no measured timing data on how close together the finger strikes land, so the page states this
  qualitatively (percussive, not smeared) rather than with a number.
- inference: none for the mechanics; the comparison to a strum's string-order spread (contrasting
  rasgueado's finger-order construction) is the page's synthesis.

### GTR-11 Rest stroke and free stroke are mechanically distinct, not two names for the same stroke at different volumes
- claim: in a rest stroke (apoyando), the plucking finger follows through to come to rest on the
  next (lower-pitched) string; in a free stroke (tirando), the finger clears the strings entirely
  and does not land on the next one. Rest stroke is associated with louder, clearer tone (used for
  single-line melody and scale passages); free stroke is required for arpeggios, where the following
  strings must be left free to keep ringing, and its tone quality is shaped by hand/wrist position
  choice.
- source: RESTSTROKE-PEDAGOGY (section)
- source_type: pedagogy
- confidence: medium
- scope: nylon-string classical guitar right-hand technique.
- limitations: this is a teaching-studio web page, not a peer-reviewed source, and gives no
  quantified spectral or loudness difference between the two strokes, only qualitative description
  ("louder and clear" vs. richness depending on hand position); the underlying distinction itself is
  standard, widely-taught classical-guitar pedagogy.
- inference: none for the mechanical description.

### GTR-12 Guitar's classical-era practical range spans about three octaves and a fifth from the low string
- claim: writing for guitar in the treble clef, sounding an octave below written pitch, the
  instrument's practical compass runs roughly three octaves and a fifth above its lowest open
  string.
- source: BERLIOZ-1855 (section)
- source_type: orchestration (public-domain treatise)
- confidence: medium
- scope: 19th-century gut/nylon classical guitar, six strings, standard tuning.
- limitations: Berlioz's guitar chapter describes the instrument as of his period (fewer frets than a
  modern 19-24 fret guitar) and explicitly says composers rarely knew the instrument's real
  capability, so this is a floor, not a ceiling, for a modern instrument; it does not reflect a
  modern guitar's extended fingerboard, which reaches further above the twelfth-fret octave than the
  instrument Berlioz described. This pack's range figure is adjusted upward for a modern fingerboard
  and labelled inference for that adjustment.
- inference: the extension from "three octaves and a fifth" to a modern instrument's fret count is
  the page's own arithmetic (fret count to pitch), not a claim found in Berlioz.

## Corrections to the 2.0 page

- **"Four-note voicings are the practical default for movable chords; six-note voicings exist mainly
  in open position"** (2.0, lines 59-61) is corrected: barre chords built on the low-E and A-string
  root shapes are movable six- and five-note voicings respectively, and are a normal part of the
  vocabulary, not an open-position-only phenomenon. This is basic fretboard geometry (a barre finger
  plus a fixed shape reproduces the open-position shape at any fret) rather than a claim requiring
  an external source; it is corrected on the page as inference from physical constraints already
  established in the same file, supported by Forsyth's description of the barre as "a temporary
  fret" (FORSYTH-1914).
- **Range "E2 to roughly E5"** (2.0, line 23) is corrected using the fret-count arithmetic in GTR-12:
  a modern 19-24 fret guitar reaches into the B5-D6 region above the twelfth-fret octave, not E5.
  Labelled inference (arithmetic from an opened source, not itself directly measured).
- **"Root and fifth do not [produce intermodulation]"** (2.0, lines 93-96) is corrected by GTR-06:
  distortion produces intermodulation (combination-tone) products for any simultaneous interval,
  including a root and fifth; the difference is that the fifth's combination tones reinforce the
  root's harmonic series (consonant), while a third's do not as cleanly. The claim was not that
  intermodulation is absent for a fifth, but that it is well-behaved.
- **No measured strum spread** (2.0, throughout) is replaced by GTR-01's figures, labelled academic
  and scoped to the study that produced them, rather than left as an unsupported "practitioner
  value."
- **Missing release behaviour** (audit finding) is filled by GTR-07 (fret-hand release/damping) plus
  inference for palm muting and string damping generally, which the source (an early-19th-century
  method) does not cover for steel-string/electric technique.

## Still to verify

- **Palm-mute damping "amount" or duration** in milliseconds or dB: not available in any source
  opened. Treated as inference on the page.
- **Adler's range/register description** (ADLER-ORCH, not-read): still not opened. The page states a
  modern-fret-count range as inference rather than citing Adler for it.
- **Alternate-tuning voicing consequences** beyond drop-D and open tunings' general description:
  treated as to-verify; no pedagogy source on alternate-tuning voicing logic was opened at section
  depth.
- **Vibrato-arm/feedback loop phase mechanism**: understood in outline (a sound wave returning to
  the string in phase reinforces its motion) from general acoustics, but no source was read at
  section depth specifically on electric-guitar feedback; labelled inference on the page and flagged
  here as to-verify against Fletcher and Rossing (FLETCHER-ROSSING-1998, not-read) or a dedicated
  electric-guitar acoustics paper.
- **Exact resonance frequencies for a specific guitar body**: general region only (100-200 Hz);
  instrument-specific values are a calibration-profile matter, not a guide-page fact.
