# Drone traditions

## Cultural context

A drone is a continuously sounding fixed reference. It appears in many unrelated practices, and
this file covers the shared consequence rather than any one tradition.

Named practices referenced here:

- **Hindustani and Carnatic classical music**, two distinct traditions that both keep the
  **tanpura** (or an electronic sruti box) sounding throughout. See `RAGA_AND_TALA.md`, and
  `shared/VIRTUAL_INSTRUMENT_GUIDE/TANPURA.md` for the instrument itself.
- **The Great Highland bagpipe** of Scotland, with a bass drone and two tenor drones. The instrument's
  physics, gracenotes and pitch are on `shared/VIRTUAL_INSTRUMENT_GUIDE/HIGHLAND_BAGPIPE.md`.
- **Launeddas**, a Sardinian instrument of three single-reed pipes played simultaneously with
  circular breathing: two chanters and one drone, with the chanters moving in thirds and sixths.
- **Minimalism and the drone music of La Monte Young**, where the drone becomes the whole piece.

Other drone practices exist (uilleann pipes with regulators, hurdy-gurdy, Balkan gaida, various
vocal practices) and each has its own repertoire and construction. Name the one you mean.

## Pitch organisation

**With a fixed reference sounding continuously, every melodic note is heard as an interval against
it.** That is the whole system, and several things follow:

1. **Intonation becomes audible.** A note slightly off a simple ratio beats against the drone. The
   ear judges against the drone, not against a keyboard.
2. **Tension comes from scale degree and register**, not from chord change. Sitting on an unstable
   degree creates tension; returning to the first or fifth degree releases it. There is nothing to
   modulate.
3. **The drone's own spectrum matters.** The tanpura's *jivari* bridge produces an extraordinarily
   rich overtone series through grazing contact with a curved bridge, with the grazing point
   shifting as the amplitude decays, producing the characteristic bloom of overtones and the
   dominance of certain harmonics over the fundamental (Raman, 1921, as cited in later acoustic
   studies). Reed drones likewise supply a dense partial series.
4. **Because the drone supplies partials, the melody locks to them**, which is why drone
   traditions tend toward just intervals rather than tempered ones. See `JUST_INTONATION.md`.

The Highland pipe is a concrete case. The bass drone and both tenor drones are tuned to one note,
A. The chanter scale is best modelled as a **just-intonation Mixolydian**, in which D is a 4:3
ratio above low A and the high G is 16:9. **The pipe's "A" is far sharper than A440**: MacPherson
(1998) reports 1990s chanters at 470 to 480 Hz for low A, between B flat and B, and the pitch has
been rising for over a century. Never treat it as A440, and treat any figure as the measurement of
a date, not as the instrument's pitch.

## Rhythm and cycle

Nothing general to say: the drone itself is unmetred and continuous, and the metre belongs to the
tradition layered over it. In Hindustani music the tala governs; in piping, the tune type does; in
minimalism there may be no pulse at all.

## Phrase structure and form

Form is carried by what happens against the drone: register, density, degree choice and, in South
Asian practice, the density gradient described in `RAGA_AND_TALA.md`. Without chord change, the
ordinary Western engines of form (progression, cadence, modulation) are unavailable, and arrival
has to be built out of return to a stable degree, register descent, and density.

In minimalism the drone is the form. La Monte Young's *The Well-Tuned Piano*, begun in 1964, is an
ongoing improvisatory solo piano work requiring a piano tuned in just intonation, performed at
lengths of five to six hours; the *Dream House* sine-wave installation has been permanent in New
York since
1993. Here tuning is the compositional material.

## Ornamentation

Tradition-specific and usually structural. Piping ornament is a system of grace-note figures that
articulate a continuous sound, because the chanter never stops: ornament is the only way to
separate repeated notes. In Hindustani and Carnatic practice, see the gamaka discussion in
`RAGA_AND_TALA.md`.

## The role of improvisation

Varies completely by tradition: extensive and grammar-bounded in Hindustani and Carnatic music,
essentially absent in the fixed repertoire of Highland piping (Hindustani and Carnatic differ
between themselves, see `RAGA_AND_TALA.md`), and central in Young's practice.
The drone itself is never improvised.

## Ensemble behaviour

Usually a soloist or small group over a drone that is either a separate player (tanpura), part of
the same instrument (bagpipe, launeddas, hurdy-gurdy), or electronic. The drone player's job is
constancy. Where a drone is part of the melody instrument, the tuning of the drone and the chanter
is one operation, not two.

## What generalises

- A sustained reference turns a piece into a study of intervals, which is a strong compositional
  constraint and an audible one.
- Tension and release can be produced without any harmonic movement, through degree and register.
- The drone's partial content determines which intervals sound consonant against it, which is the
  same argument as in `CONTEMPORARY_MICROTONALITY.md`. Choose the drone timbre and the tuning
  together.
- Rich-spectrum drones (bowed, reed, resonant-bridge) give a melody far more to lock onto than a
  plain sine or a soft pad, and that changes how tuning is heard.

## What must not be casually universalised

- **A drone is not a pedal tone under chords.** A pedal tone is a device inside progressional
  harmony. A drone replaces progressional harmony.
- **Adding chord changes over a tanpura removes what makes the system work.** The fixed reference
  is what makes every note an interval. Once the reference moves, the intervals are relative to
  something else and the system is gone.
- **The Highland pipe's A is not 440 Hz**, and its scale is not 12-tone equal-tempered Mixolydian.
- **"Drone pad" presets do not represent these instruments.** Launeddas and uilleann regulators
  have specific construction, specific repertoire and specific partial content.
- La Monte Young's tunings are the composer's own system, kept private for a long time. Credit
  them; do not recreate them as generic just intonation.

## Working with this in the studio

**Composer** sets: the drone pitches (commonly the first plus the fifth, or the first plus the
fourth, depending on the tradition and, for the tanpura, on the raga; other tanpura tunings exist
and are to verify against a practitioner source before one is stated for a given raga), the reference frequency
in Hz, the tuning of the melody relative to the drone as ratios or measured values, and the
tension plan expressed as degrees and registers rather than as chords.

**Performance Director** needs: the drone's constancy as an instruction, the ornament vocabulary
for the instrument, and, where relevant, that repeated notes are separated by ornament rather than
by rests.

**MIDI Builder and Plugin Auditor** must check whether the melody instrument can be tuned to the
drone at all, and by which mechanism (scale file, MTS-ESP, per-note bend). Verify the reference
frequency explicitly: a scale file says nothing about which key it starts on, and a synth that
assumes A440 will put a bagpipe tuning in the wrong place. Verify the drone source can be set to a
non-standard frequency. See `shared/TUNING_AND_MPE.md`. Silent re-quantisation to 12-tone equal
temperament is not acceptable.

**Listener Model** should not expect harmonic rhythm, should not read the absence of chord change
as a lack of development, and should not treat beating against the drone as a mix problem.

## Sources and confidence

- On tanpura acoustics: Raman (1921) as cited in later experimental investigations of tanpura
  acoustics, and the literature on the jivari bridge. Open a tanpura acoustics paper first if the
  drone's spectrum matters to the project.
- Ewan MacPherson, "The Pitch and Scale of the Great Highland Bagpipe", 1998,
  publish.uwo.ca/~emacphe3/pipes/acoustics/pipescale.html, for the just Mixolydian model and the
  pitch figures. It reports pitch rising over the century: about 441 Hz for one chanter measured in
  1885, an average of about 459 Hz in the mid-1950s, and 470 to 480 Hz for low A in chanters of the
  1990s. **The figure is dated**: pipe pitch has kept moving, so treat any number as a date's
  measurement, not the instrument's pitch.
- Bentzon, *The Launeddas: A Sardinian Folk-Music Instrument*, Akademisk Forlag, 1969.
- On La Monte Young: *The Well-Tuned Piano* release documentation and the *Dream House*
  installation.

Confidence: the acoustic argument (drone partials leading melodies toward just intervals) is an
inference drawn across these sources rather than a single cited finding, and is labelled as such.
**To verify:** the exact ratios of the full Highland chanter scale beyond the 4:3 and 16:9 cited
here; Young's *Composition 1960 #7*, which is widely documented but was not confirmed in this
research pass. None of these sources were read in full.
