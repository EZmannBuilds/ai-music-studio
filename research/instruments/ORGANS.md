# Organs: research records

What was read, what was not, and the limits of each claim the guide page makes. The page carries
the conclusions; this file carries the evidence.

## Scope and method

Two parts: the pipe organ and the drawbar/tonewheel organ, plus new Ensemble and Recording sections
for both and a rotating-speaker section for the drawbar organ. Eight sources were read at section
depth: two organ-building/performer pedagogy pages (tracker action, pedal technique), one university
organ-department tutorial (swell box), one registration-pedagogy page (flute stops), one technical
white paper on rotary-speaker acoustics, one deep technical-reference page on tonewheel generation and
electronics, one magazine technical-pedagogy article on tonewheel additive synthesis, and one
technical wiki page on percussion retriggering. Audsley's *The Art of Organ-Building* was targeted per
the brief but could not be opened: the archive.org text-view endpoint returned only its viewer
scaffold, not readable text, in this session's fetch tool, and a direct download endpoint required
authentication this session does not have. It stays in the register as `not-read`, exactly the
position the 2.0 page's other named-but-unopened texts (Adler, Fletcher and Rossing) are already in.

The rotary-speaker and tonewheel-electronics sources describe a specific well-known instrument and
accessory in order to explain a general acoustic and electromechanical mechanism; the guide page
below states the mechanism generically ("a rotating speaker," "a drawbar organ") per the pack's
no-product-names rule, while the citations in `research/sources/INSTRUMENT_SOURCES.md` are free to name what was actually
read, per `shared/VIRTUAL_INSTRUMENT_GUIDE/INDEX.md` rule 6.

## Records

### ORG-01 Tracker action lets touch control pallet-opening speed and audible pipe speech (chiff)
- claim: in a mechanically linked (tracker) key action, the organist's finger is in direct contact,
  through levers and trackers, with the pallet valve that admits wind to a pipe; a faster key attack
  opens the pallet more abruptly and produces a more pronounced chiff (the transient at pipe speech
  onset), while a gentler attack smooths the onset. This is a real, graded, player-controlled effect
  on attack character, even though it is not a loudness (velocity) control.
- source: TRACKERACTION-PEDAGOGY-1 (section)
- source_type: pedagogy
- confidence: medium
- scope: mechanical (tracker) key actions specifically; does not extend to electric or pneumatic
  actions, which decouple the finger from the pallet and remove this control.
- limitations: a single organ-building pedagogy source, not an acoustics measurement of pallet
  opening speed versus chiff amplitude; described qualitatively, not quantified.
- inference: none for the mechanism; the guide's framing that this contradicts a flat "no velocity at
  all" claim is this pack's correction of the 2.0 page's overstatement.

### ORG-02 Heel-and-toe pedal technique allows fast, alternating pedal lines
- claim: the toe-toe-heel-heel alternating pattern (and its mirror for descending lines) is the
  standard technique for playing continuous or rapid pedalboard lines, allowing faster passage work
  than toe-only playing; sharp/accidental pedal keys cannot be played with the heel, which affects
  fingering (footing) choices near accidentals.
- source: PEDAL-TECHNIQUE-1 (section)
- source_type: pedagogy
- confidence: medium
- scope: standard concave radiating pedalboards as used on most modern organs.
- limitations: a single manufacturer-hosted pedagogy article, not a conservatory-published method; no
  quantified maximum pedal-line tempo is given.
- inference: the guide's framing that pedal lines "can be fast" (rather than uniformly slow and
  single-voiced) is a direct correction drawn from this source; the further claim that pedal writing
  is typically single-voiced because two feet cannot easily play independent polyphonic lines is this
  pack's inference from ordinary two-foot physical constraints, not a statement in the source.

### ORG-03 The swell box and expression pedal change both loudness and brightness together
- claim: the swell box's shutters open and close as the organist moves the expression pedal (fully
  open toe-forward, closed heel-forward); opening the shutters increases loudness and, because higher
  frequencies are attenuated more by closed shutters than low frequencies are, also increases
  perceived brightness. The two changes (level and colour) are not separable through this control.
- source: SWELLBOX-TUTORIAL-1 (section)
- source_type: pedagogy
- confidence: medium
- scope: enclosed (swell) divisions on pipe organs generally.
- limitations: a single university teaching-resource page, not an acoustic measurement of the
  frequency-dependent attenuation curve of swell shutters.
- inference: none for the mechanism; the parallel the guide draws to registration's simultaneous
  loudness/colour coupling is this pack's synthesis across the two related mechanisms.

### ORG-04 Adding stops, especially 16-foot and flute stops, does not always brighten the sound
- claim: flute-family stops (voiced with heavier nicking and regulated wind at the toe) are
  characteristically dark and fundamental-heavy rather than bright, and are typically added to a
  registration to supply foundational weight and gravity rather than upper brightness; a 16-foot stop
  adds an octave below the manual's normal pitch, again adding gravity rather than brightness.
- source: FLUTE-STOPS-REGISTRATION-1 (section)
- source_type: pedagogy
- confidence: medium
- scope: standard Western pipe-organ flute and principal stop families.
- limitations: a single registration-pedagogy page from one organ-building company; does not cover
  every flute-stop subtype (e.g. harmonic flutes, which are voiced for brighter, more overtone-rich
  solo use) in the depth a full organ-building text would.
- inference: the guide's blanket correction of "adding stops always brightens" to "16-foot and flute
  stops characteristically darken" is this pack's generalisation from this source's specific claims
  about flute voicing and low-pitch stops, applied as the guide's stated correction.

### ORG-05 A drawbar organ's footages are not literal harmonics, and tonewheel gearing is tempered, not just
- claim: a tonewheel-based drawbar instrument's frequencies are generated by fixed mechanical gear
  ratios (integer tooth-count ratios) between a constant-speed motor and each tonewheel, which produce
  frequencies that approximate 12-tone equal temperament closely but not exactly (one specific analysis
  found the note class least well matched, in one octave, to be about 0.69 cents flat of equal
  temperament); the "16-foot" drawbar is a sub-octave (one octave below the fundamental drawbar), not
  a harmonic of it, and higher-numbered drawbars correspond to specific harmonic numbers of the
  fundamental rather than being an arbitrary per-drawbar harmonic series.
- source: TONEWHEEL-TECHNICAL-1 (section)
- source_type: specification
- confidence: medium
- scope: tonewheel-generator electromechanical organs specifically; not applicable to purely digital
  drawbar-organ emulations, whose tuning is a designer choice rather than a mechanical consequence.
- limitations: a single technical-reference page (not a peer-reviewed source), written from a
  reverse-engineering/DIY-electronics perspective rather than an official manufacturer specification;
  the exact cent-deviation figures are as this source reports them and were not independently
  cross-checked against a second source.
- inference: the guide's correction of the 2.0 page's "one drawbar per harmonic" framing to "footages
  including a sub-octave, generated by tempered gearing" is drawn directly from this source; applying
  the general tonewheel-organ mechanism as representative of "a drawbar organ" generically, per the
  pack's no-product-names rule, is this pack's generalisation.

### ORG-06 Drawbar additive mixing constructs registrations from fixed sine-like partials
- claim: each drawbar contributes one nominally sinusoidal partial at a fixed footage/harmonic
  relationship to the fundamental, at a settable level (commonly graduated across eight-or-so steps);
  the combination of all drawbar levels for one manual is the instrument's entire "patch," since there
  is no separate filter or amplitude envelope shaping the combined tone the way a subtractive
  synthesizer has one.
- source: TONEWHEEL-SYNTHESIS-1 (section)
- source_type: pedagogy
- confidence: medium
- scope: tonewheel-generator drawbar organs; the additive-mixing description is general enough to
  apply to digital reproductions of the same drawbar model as well.
- limitations: a single magazine technical-pedagogy article; does not address the tempered-gearing
  point independently (see ORG-05), and the two sources' drawbar-to-harmonic tables differ slightly in
  presentation, which the guide resolves by deferring to `TONEWHEEL-TECHNICAL-1` for the exact
  footage-to-harmonic mapping.
- inference: none for the core additive-mixing description.

### ORG-07 Drawbar-organ percussion is single-triggered: it sounds once per phrase, not once per note
- claim: a drawbar organ's built-in percussion effect (an extra decaying harmonic, 2nd or 3rd,
  layered onto the attack) is triggered only when a note is struck from an all-keys-up state; as long
  as any key of a chord or phrase remains held, striking further notes produces no additional
  percussion attack. It re-triggers only after every key has been released and a new note is struck
  from silence. This makes the effect a function of phrasing (legato versus detached playing), not a
  fixed per-note attribute.
- source: PERCUSSION-RETRIGGER-1 (section)
- source_type: specification
- confidence: medium
- scope: the electromechanical tonewheel organ's built-in single-trigger percussion circuit
  specifically; digital emulations commonly reproduce the same behaviour by design, but that is a
  design choice, not a physical necessity, so the claim is stated here as the historical instrument's
  documented behaviour.
- limitations: a single technical wiki page; consistent with the 2.0 page's existing (excerpt-derived)
  claim on this point, now confirmed at section depth from a dedicated technical source.
- inference: none for the retrigger mechanism itself; the guide's framing of this as a phrasing
  constraint the Performance Director should state explicitly is carried over from the 2.0 page's
  existing correct instinct on this point, now properly sourced.

### ORG-08 A rotating (Leslie-type) speaker's horn and drum/rotor accelerate and decelerate at
different rates when switching speed, and this transition is itself the expressive gesture
- claim: a rotating speaker system uses two rotating elements (commonly a horn for upper frequencies
  and a drum/rotor for lower frequencies) that can each run at a slow and a fast speed; because the
  drum has much greater rotational inertia than the horn, it accelerates and decelerates more slowly
  when the motor speed is switched, so the horn reaches its new speed well before the drum does,
  producing a complex, audibly evolving transition rather than an instant speed change. The horn
  produces mostly frequency-modulation (Doppler) and directional brightness/loudness variation as it
  turns; the drum produces mostly amplitude modulation (a "breathing" tremolo) from a rotating cutout
  in front of a downward-firing driver.
- source: ROTARY-SPEAKER-TECH-1 (section)
- source_type: specification
- confidence: medium
- scope: horn-and-drum rotary speaker systems of the classic two-rotor design; single-rotor or
  digitally modelled variants may differ in detail.
- limitations: a single technical white paper from an effects-pedal manufacturer explaining the
  physics of a rotating speaker generically (not a peer-reviewed acoustics paper); page states the
  mechanism as "a rotating speaker" without naming the product line described in the source, per the
  pack's no-product-names rule.
- inference: none for the acceleration-asymmetry mechanism; the guide's instruction to treat a speed
  change as a placed performance event with modelled acceleration, rather than an instant switch, is
  this pack's programming-consequence conclusion from the acoustic fact.

## Corrections to the 2.0 page

1. **"No velocity at all" overstated for tracker organs (old page locations ~18-19, ~73-74)**:
   corrected using `TRACKERACTION-PEDAGOGY-1`: touch does not select loudness, but on a tracker action
   it does give the player real, graded control over pallet-opening speed and hence chiff/attack
   character. This is now stated explicitly rather than folded into a blanket "no velocity" claim.
2. **"Adding stops always brightens" (old page locations ~54-57)**: corrected using
   `FLUTE-STOPS-REGISTRATION-1`: 16-foot and flute-family stops characteristically darken a
   registration by adding fundamental weight, not brightness.
3. **"One drawbar per harmonic" (old page location ~113)**: corrected using `TONEWHEEL-TECHNICAL-1`:
   the 16-foot drawbar is a sub-octave, not a harmonic, and the tonewheel gearing that generates every
   drawbar's pitch is a tempered approximation of equal temperament, not a pure harmonic series.
4. **Pedal lines assumed uniformly slow (old page locations ~83-84)**: corrected using
   `PEDAL-TECHNIQUE-1`: heel-and-toe technique allows genuinely fast alternating pedal lines.
5. **Ensemble and Recording sections added**, which the 2.0 page lacked entirely, per the brief;
   content in those sections is drawn from the same sources above plus stated `inference` where no
   dedicated ensemble- or recording-practice source for organs was read in this pass.
6. **Rotary speaker acceleration asymmetry**, previously only "to verify: measured rotary speaker ramp
   times... not available" in the 2.0 page, is now sourced from `ROTARY-SPEAKER-TECH-1`, though still
   without an exact millisecond figure (see below).
7. **Single-trigger percussion**, previously `excerpt-derived`, is now confirmed at section depth from
   `PERCUSSION-RETRIGGER-1`.

## Still to verify

- Audsley, *The Art of Organ-Building*: targeted per the brief, attempted via archive.org, not
  reachable in this session (viewer scaffold only, and the direct-download endpoint required
  authentication this session lacks). Registration conventions, footage nomenclature and pipe-speech
  acoustics attributed to it in the 2.0 page remain `to-verify` rather than promoted.
- Exact chiff-amplitude-versus-pallet-opening-speed relationship: described qualitatively in
  `TRACKERACTION-PEDAGOGY-1`, not quantified there or in any other source read here.
- Exact rotary-speaker horn/drum acceleration times in milliseconds: `ROTARY-SPEAKER-TECH-1` describes
  the asymmetry qualitatively; no source read here gives a measured ramp time.
- Wind-supply instability under heavy chords (old page's "wind supply is not perfectly steady"
  claim): not covered by any source read in this pass; carried forward as `inference`.
- Fletcher and Rossing on pipe-speech transients and wind-supply acoustics: not opened for this work.
- Adler on registration conventions and footage-nomenclature writing practice: not opened for this
  work.
