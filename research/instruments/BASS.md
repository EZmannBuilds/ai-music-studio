# Bass: research records

What was read, what was not, and the limits of each claim the guide page makes. The page carries
the conclusions; this file carries the evidence.

## Scope and method

Electric bass (four- and five-string), fretless electric bass, and double bass played pizzicato in
jazz/pop contexts. Bowed double bass stays out of scope here and is covered in `STRINGS.md`; this
page says so and does not duplicate it. Seven sources were read at section depth: one academic
acoustics paper on magnetic pickups (shared with `GUITAR.md`, since the physics is the same
mechanism applied to bass strings and pickups), one academic paper on fret-pressure intonation
(shared with `GUITAR.md` for the same reason), and five performer-pedagogy web pages covering double
bass pizzicato technique, fretless intonation and vibrato, and ghost-note/muting mechanics.

No manufacturer manual specific to a bass instrument or bass sample library was opened for this pass;
`round_robins` and similar virtual-programming rows are stated as inference (general sample-library
convention) rather than manual-derived, since no bass-specific manual was read.

Not reachable: a controlled acoustic study of low-frequency string decay and pitch settling specific
to bass strings (Fletcher and Rossing was not opened, registered as a not-read standard reference);
a measured velocity distribution for ghost notes; a source distinguishing genre-specific bass
compression norms beyond production-blog consensus.

## Records

### BASS-01 Pickup position affects bass tone by the same comb-filter mechanism as guitar
- claim: a magnetic pickup senses string velocity at a fixed point; the resulting comb-filter
  response removes harmonics with a node near that point, so a bridge-position pickup reads brighter
  and a neck-position pickup reads darker, on bass exactly as on guitar, because the underlying
  physics (a vibrating string sensed magnetically at one point) is the same.
- source: PAIVA-PICKUPS-2012 (section)
- source_type: academic acoustics (AES Journal)
- confidence: medium
- scope: magnetic pickups on steel strings generally.
- limitations: the mechanism itself is high confidence, but the paper does not test a bass
  instrument specifically, so applying it to bass is a model extension rather than a bass-specific
  measurement; bass strings are thicker and lower-tension in different proportions than guitar
  strings, which could shift exact comb-filter frequencies, but not the mechanism itself.
- inference: applying the model to bass (rather than only guitar, where the paper's examples are
  drawn from) is this pack's extension, flagged as such on the page.

### BASS-02 Fret pressure sharpens pitch on a fretted bass by the same mechanism as guitar
- claim: pressing a string down to a fret stretches it, sharpening its pitch above the theoretical
  fretted value; the effect is measured (14-64 cents uncompensated, reduced to about ±8 cents with
  standard compensation) on a laboratory fretted-string instrument, and the mechanism generalises to
  any fretted string under tension, bass included.
- source: VARIESCHI-2009 (section)
- source_type: academic acoustics (arXiv)
- confidence: low
- scope: fretted string instruments generally, tested on a guitar/mandolin-geometry monochord.
- limitations: the tested instrument's strings and tension are closer to a guitar/mandolin than to a
  bass's longer scale and heavier gauge strings, so the magnitude may differ even though the
  direction and existence of the effect generalise; no bass-specific magnitude is available, so this
  pack states the mechanism as sourced and the bass-specific magnitude as to-verify.
- inference: none for the mechanism; the bass-specific magnitude is explicitly left unverified rather
  than assumed equal to the guitar figures.

### BASS-03 Jazz and orchestral double bass pizzicato are mechanically distinct techniques
- claim: orchestral (classical) pizzicato uses fingers roughly perpendicular to the string, plucking
  near the fingertip with less surface area, producing a dry, precise, fast-decaying "timpani-like"
  attack, and deliberately avoids audible fingerboard buzz; jazz pizzicato uses fingers parallel to
  the string, plucking with more of the pad/first joint, pulling through into the next string,
  producing a louder, thumpier, more resonant, woodier tone where the finger's impact against the
  fingerboard is audible and wanted.
- source: PIZZICATO-STYLE-PEDAGOGY (section); FOX-DOUBLEBASS-PLUCK (section)
- source_type: pedagogy
- confidence: medium
- scope: double bass in orchestral versus jazz/pop pizzicato contexts.
- limitations: two independent performer sources agree with each other on the core mechanical
  distinction, which is reassuring, but neither source is peer-reviewed or gives measured spectral
  data; both are experienced-performer descriptions, not independently instrument-measured here.
- inference: none for the mechanical description; the framing of this as a genre-functional choice
  (jazz bass needs an audible attack because it "plays on almost every beat" as a section's time
  foundation, orchestral bass blends into a section) is drawn directly from PIZZICATO-STYLE-PEDAGOGY's
  own stated reasoning, not added by this pack.

### BASS-04 Fretless bass vibrato is a broad, continuous finger-rolling motion, and should not be used to disguise wrong pitch
- claim: on fretless bass, vibrato is produced by a broader, more continuous rolling motion of the
  fingertip than the small oscillation used on a fretted instrument, closer to a string player's
  vibrato than a guitarist's; pedagogically, players are explicitly warned not to use vibrato to
  cover an out-of-tune note, because it masks rather than fixes bad intonation.
- source: FRETLESS-VIBRATO-PEDAGOGY (section); FRETLESS-INTONATION-PEDAGOGY (section)
- source_type: pedagogy
- confidence: medium
- scope: fretless electric bass.
- limitations: consistent advice from two independent performer-pedagogy sources, but no measured
  cents-range or rate for fretless bass vibrato was found; qualitative only.
- inference: none for the description; the general point that vibrato is a phrase decision, not a
  cosmetic fix, generalises the schema's own `vibrato: by_phrase` field
  (`shared/HUMAN_PERFORMANCE_SCHEMA.md`), not a new claim from these sources.

### BASS-05 Fretless intonation is a tactile/muscle-memory skill, and finger angle alone shifts pitch
- claim: without frets as a physical reference, fretless bass intonation depends on developed muscle
  memory for interval spacing (practising double stops in octaves, fifths and fourths to use
  interference beating as feedback) rather than a visual or tactile fret guide; twisting the hand
  angle at a fixed finger position measurably changes the pitch produced, because the effective
  string-stopping point shifts slightly.
- source: FRETLESS-INTONATION-PEDAGOGY (section)
- source_type: pedagogy
- confidence: low
- scope: fretless electric bass.
- limitations: qualitative performer description, not an acoustics measurement of the finger-angle
  pitch effect; no quantification of how much a given hand-angle change shifts pitch.
- inference: none for the description.

### BASS-06 Ghost notes are produced by left-hand string deadening with normal right-hand plucking, and their loudness/ease depends on string tension at the pluck point
- claim: a ghost note is produced by resting the fretting hand across the string(s) to prevent clear
  pitch, then plucking normally with the other hand; playing closer to the bridge, where string
  tension for a given pluck is effectively greater, makes ghost notes louder and easier to control.
  Ghost notes function rhythmically, filling space between main notes to add a sense of forward
  motion to a groove without changing its underlying harmonic content.
- source: GHOSTNOTE-PEDAGOGY (section)
- source_type: pedagogy
- confidence: medium
- scope: electric bass (fretted or fretless), funk/groove-oriented playing.
- limitations: standard technique description from a single teaching source; no measured velocity or
  dynamic-range data for ghost notes; the "closer to the bridge is louder/easier" claim is stated
  qualitatively, not measured.
- inference: none for the mechanism. The generalisation that ghost notes need their own imperfection
  cause in `shared/HUMAN_PERFORMANCE_SCHEMA.md` terms (a distinct articulation, not a velocity
  variant of a normal pluck) is this pack's application of the schema, not a claim from the source.

## Corrections to the 2.0 page

- **"So that the same note is never twice identical"** (2.0, lines 111-112) is removed. It named no
  cause, which `shared/HUMAN_PERFORMANCE_SCHEMA.md` section 1 explicitly forbids ("no field whose
  value is 'amount of humanization'"). Replaced with named causes already available in the schema:
  plucking-finger alternation (index/middle alternation changes attack character note to note),
  string/position choice (the same pitch is often available on two strings with different timbre),
  and metrical accent (`shared/HUMAN_PERFORMANCE_SCHEMA.md` section 3, `metrical_accent`).
- **"An uncompressed bass reads as unfinished"** (2.0, lines 90-91) is corrected to a genre-bound
  claim. Jazz and acoustic-leaning production norms deliberately preserve a wider dynamic range on
  bass (light or no compression); the "reads as unfinished" claim applies mainly to pop/rock/hip-hop
  production conventions, not to bass playing or recording generally. This correction is inference
  (general production knowledge) rather than a section-depth-read source, and is flagged as such
  rather than given a stronger label.
- **"Below E1 on a four-string" as the out-of-range floor** (2.0, line 132) ignored drop-D and other
  common four-string drop tunings, where the lowest string is tuned below standard E1 (drop-D bass
  tunes the low string to D1). This is corrected by stating the floor relative to the *declared*
  tuning rather than assuming standard tuning, consistent with how `GUITAR.md`'s `out_of_range` row
  already handles alternate tunings and capos.
- **Dynamic-to-timbre, fret-hand muting/release, fretless vibrato/intonation, resonance, and round
  robins** were largely absent or thin in 2.0. These are filled by BASS-01 through BASS-06 above.

## Still to verify

- **Bass-specific fret-pressure sharpening magnitude**: the mechanism is sourced (BASS-02) but the
  cents figures are from a guitar/mandolin-geometry instrument, not a bass; a bass-specific
  measurement was not found.
- **Low-frequency string decay and pitch-settling physics** (why a plucked low note has an uneven,
  slightly pitch-drifting decay): still attributed to Fletcher and Rossing, *The Physics of Musical
  Instruments* (FLETCHER-ROSSING-1998, not-read).
- **Measured ghost-note velocity range**: not available; the drum-kit ghost-note figure elsewhere in
  this pack should not be borrowed for bass, consistent with the 2.0 page's own caution.
- **Genre-specific compression norms**: stated as general production knowledge, not sourced to a
  section-depth-read text; a dedicated audio-engineering pedagogy source would strengthen this.
- **Double bass string choice (gut vs. steel/synthetic) and its effect on jazz pizzicato tone**:
  mentioned qualitatively by the performer sources but not measured or deeply sourced here.
