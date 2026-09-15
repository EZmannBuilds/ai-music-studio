# Piano and Keyboards: research records

What was read, what was not, and the limits of each claim the guide page makes. The page carries
the conclusions; this file carries the evidence.

## Scope and method

Seven cards: grand piano (with upright differences noted in-row), harpsichord, celesta, accordion
and harmonium/reed organ, tine electric piano, reed electric piano, and clavinet. Fourteen sources
were read at section or excerpt depth, spanning a piano-technician action walkthrough, one academic
acoustics paper read via a university lecture summary, one perception study, two orchestration or
pedagogy resources, a hand-span advocacy page citing measured data, two electromechanical-instrument
mechanism sources, and one peer-reviewed conference paper covering both electric pianos. One official
manufacturer manual (for the tine electric piano) was opened; the reed electric piano and clavinet
material comes from repair-trade and fan-community technical writing rather than a manufacturer
manual, so it is labelled `sourced`, not `manual-derived`, per this pass's rule that `manual-derived`
is reserved for a manufacturer's own manual actually opened.

Not reachable at section depth: Fletcher and Rossing on hammer-felt nonlinearity (paywalled, not
opened, as in the 2.0 page); Adler on register writing conventions (not opened); the Railsback-stretch
JASA paper's full text (paywalled; only search-engine excerpts of its findings were available, so it
is recorded at `excerpt` depth, not `academic`).

## Records

### KEYS-01 Double escapement allows repetition without full key release
- claim: the grand piano's double escapement (repetition) action resets the jack under the hammer
  knuckle as the key rises only partway, so a note can be restruck before the key fully returns; a
  well-regulated action can repeat up to roughly eight times per second. Upright pianos use a single
  escapement without a repetition lever, so they cannot repeat as fast and rely on the key's fuller
  return for the jack to reset.
- source: SMIT-PIANOACTION (section)
- source_type: pedagogy
- confidence: medium
- scope: modern grand piano double-escapement actions generally; upright single-escapement actions by
  contrast, though the source does not detail the upright mechanism itself in the fetched section.
- limitations: a single piano-technician source, not a peer-reviewed acoustics measurement; the
  "eight times per second" figure is a practitioner's stated ceiling, not a controlled study result;
  the explicit upright-vs-grand contrast draws on general keyboard-technique knowledge the source does
  not itself spell out for the upright case.
- inference: none beyond applying the source's grand-action description to state the upright contrast
  it does not detail directly.

### KEYS-02 Coupled unison strings produce a two-stage decay ("aftersound") through bridge coupling
- claim: the two or three strings of one note are dynamically coupled through the bridge. Struck
  strings first decay quickly in a symmetric (in-phase) mode that drives the bridge strongly, then
  settle into a slower antisymmetric (out-of-phase) mode whose forces largely cancel at the bridge,
  producing the long, quiet "aftersound" tail. Deliberately mistuned unisons and the una corda pedal
  both act on this coupling, not on the strings independently.
- source: WEINREICH-1977 (section)
- source_type: academic acoustics
- confidence: medium
- scope: struck three-string (or two-string) unison piano notes generally; treble and mid-register
  notes with multiple strings per key. Does not apply to the single-strung bass.
- limitations: read as a university lecture's summary of the original 1977 journal paper, not the
  paper itself, so exact quantitative detail (for example the magnitude of the loudness jump when one
  string of a pair is stopped) is reported only as the summary presents it.
- inference: none for the coupling mechanism itself; the guide's framing of this as central to
  understanding piano decay, rather than a footnote, is this pack's editorial emphasis.

### KEYS-03 Half-pedalling, flutter pedalling and harmony-following pedal changes are distinct techniques
- claim: half-pedalling partially raises the dampers so bass resonance is kept while upper-register
  clarity is retained; flutter (surface) pedalling uses very quick, shallow pedal movements to reduce
  accumulating blur in fast passages; and syncopated/legato pedalling changes the pedal just after each
  harmonic change, not on the beat or the bar line.
- source: SPANSWICK-PEDAL (section)
- source_type: pedagogy
- confidence: medium
- scope: general piano repertoire and technique; not instrument- or era-specific.
- limitations: a single pedagogy source (one named teacher's instructional page), not a controlled
  study; exact timing of "just after" a harmony change is not quantified.
- inference: the guide's framing of "pedal follows harmony, not bar lines" as a fake-sounding tell is
  this pack's synthesis of the pedagogy, consistent with the 2.0 page's existing claim.

### KEYS-04 Stretch tuning compensates for string inharmonicity
- claim: real piano strings are stiff, so their overtone partials run sharp of an ideal harmonic
  series by a factor that grows with partial number; tuning pure 2:1 octaves against that inharmonicity
  would sound dissonant, so piano technicians stretch octaves (bass flat, treble sharp of 12-tone
  equal temperament) to match perceived consonance to the strings' actual partials. This is the
  Railsback stretch.
- source: RAILSBACK-STRETCH-2015 (excerpt)
- source_type: academic acoustics
- confidence: low
- scope: modern equal-tempered pianos tuned by ear or by ear-trained technicians generally.
- limitations: only search-engine-surfaced characterizations of the paper's abstract and findings were
  read, not the paper itself, which is paywalled; the exact stretch curve (cents per octave by
  register) is not captured here and should not be treated as verified until the paper itself, or
  Fletcher and Rossing, is opened.
- inference: none beyond noting that this replaces the 2.0 page's undeveloped mention of
  "inharmonicity thin" with a named mechanism and a named, if lightly read, source.

### KEYS-05 Comfortable hand span varies enough that "a ninth comfortably" is not a safe default
- claim: a hand span around 6.7 inches makes an octave marginal; roughly 7.6 inches makes an octave
  comfortable and a ninth marginal; roughly 8.5 inches (21.6 cm) is the threshold below which a tenth
  is not comfortably reachable. Adult male hand spans average about one inch (2.5 cm) more than adult
  female hand spans; by the cited figures, about 76% of men but only about 13% of women comfortably
  clear the 8.5-inch tenth threshold, and roughly 87% of adult women cannot comfortably play a tenth
  on the standard keyboard.
- source: PASK-HANDSPAN (section)
- source_type: pedagogy
- confidence: medium
- scope: adult pianists on a standard (non-narrow) keyboard.
- limitations: this is an advocacy organization's page reporting hand-span research, not the original
  study itself, which was not independently opened in this pass; the percentages should be treated as
  the organization's reporting, not an independently re-verified figure.
- inference: the guide page's correction of "a ninth comfortably" to something more conditional is
  this pack's editorial response to this data, not a direct quotation of a single study's conclusion.

### KEYS-06 Harpsichord touch and registration together control dynamics, with registration primary
- claim: (a) a harpsichord's jack-and-plectrum mechanism plucks a string at essentially one strength
  regardless of how hard or soft the key is pressed, so large-scale dynamic contrast is made by
  registration (choosing which string choirs sound, and whether manuals are coupled) rather than by
  touch; (b) a controlled acoustic and perceptual study of a historical harpsichord found that
  "loud/struck" versus "soft/pressed" touch produced measurable loudness differences of up to about
  11 dB on some registers and pitches, and listeners could discriminate the two touches significantly
  better than chance.
- source: ORGANOLOGY-HARPSICHORD (section); HARPSICHORD-TOUCH-STUDY-1 (section)
- source_type: pedagogy; academic acoustics
- confidence: medium
- scope: harpsichords generally for the mechanism; specifically one 18th-century French-style
  instrument for the touch-dynamics figures, which may not generalise in magnitude to other schools of
  harpsichord building.
- limitations: the touch study covers one instrument; its dB figures are not a general constant for
  "the harpsichord" and are reported here as what was found on that instrument, not a universal
  capability.
- inference: the framing that touch dynamics exist but are secondary to registration is this pack's
  synthesis of the two sources together.

### KEYS-07 The celesta is a transposing idiophone with hammers, steel bars and wood resonators, and has a damper
- claim: keys operate felt-wrapped hammers that strike tuned steel bars, each suspended over an
  individual wood resonator box that shapes and reinforces the tone; the instrument is written on a
  piano-style grand staff and sounds one octave higher than written (so it is written one octave below
  sounding pitch); it has a damper pedal that lets the sound ring when depressed and cuts it short when
  released, comparable in function (not mechanism) to a piano's damper pedal; dynamic range is narrow
  and the instrument is used in otherwise quiet textures to be heard at all.
- source: HUGILL-CELESTA (section)
- source_type: orchestration
- confidence: medium
- scope: the standard orchestral celesta.
- limitations: a single source; exact resonator tuning and bar-material detail beyond "steel" was not
  cross-checked against an acoustics source. The damper-pedal claim is a genuine addition versus the
  2.0 page, which did not mention a pedal at all.
- inference: none.

### KEYS-08 Accordion bellows control attack, dynamics, phrasing and direction; reversal is a placed event
- claim: bellows movement (not the reed itself) is the accordion's primary dynamic and expressive
  control, shaping how a note begins, how a phrase's air is spent, and where in the music a bellows
  reversal happens; a reversal is planned at a point the articulation permits, timed with the finger
  action so it does not add an audible extra impulse; softer passages use the available air
  differently from full chords at a stronger dynamic.
- source: WACHTER-ACCORDION (section)
- source_type: pedagogy
- confidence: medium
- scope: general (classical/concert) accordion technique; does not cover free-bass or specific folk
  traditions' bellows conventions.
- limitations: a single pedagogy source; no acoustic measurement of bellows pressure-to-loudness
  curve; the source does not address the bellows shake, which the page therefore carries as inference.
- inference: none for the core claims described.

### KEYS-09 Free reeds are pitch-stable under changing air pressure, unlike a pipe organ's beating reeds
- claim: a free reed vibrates back and forth through a close-fitting frame opening; its pitch is set
  chiefly by its own physical properties (mass, length, stiffness), not by the air pressure driving it,
  so pumping or bellows speed mainly changes loudness rather than pitch. Reed organs come in
  pressure-wind (typically hand-and-foot bellows, European harmonium tradition) and suction-wind
  (typically foot-pumped, American parlor/pump organ tradition) types.
- source: NEWWORLD-REEDORGAN (section)
- source_type: pedagogy
- confidence: medium
- scope: Western hand- or foot-pumped free-reed keyboard instruments (reed organ, harmonium, parlor
  organ, melodeon). Explicitly does not cover the hand-pumped Indian harmonium tradition, which has its
  own playing conventions and is out of scope for this card.
- limitations: a single general-reference source, not an acoustics-specialist text; the
  pressure-versus-suction geography claim is reported as the source states it.
- inference: the explicit scoping-out of the Indian harmonium tradition is this pack's decision, made
  to avoid the "one file for the West, one protocol for everything else" problem named in
  `shared/VIRTUAL_INSTRUMENT_GUIDE/INDEX.md`, not a claim from the source.

### KEYS-10 The clavinet is struck by a rubber-tipped tangent against a fixed anvil, not plucked
- claim: a rubber pad mounted under each key is driven down onto the string, pressing it against a
  fixed metal anvil for the duration of the note; this both starts the string vibrating and divides it
  into a speaking and non-speaking length, with the speaking length's vibration sensed by pickups.
  Release is controlled by a yarn damper resting on the strings, adjustable in position; the
  instrument has no pedal. The mechanism is a striking action against a fixed point, not a plectrum
  plucking a free string, which is the 2.0 page's error.
- source: CLAVINET-FAQ-1 (section)
- source_type: performer
- confidence: medium
- scope: the common Hohner Clavinet models (C, D, D6, E7, Duo) covered by this FAQ; the mechanism
  generalises to the instrument family since there was effectively one manufacturer.
- limitations: not a manufacturer manual, so labelled `sourced` rather than `manual-derived`; pickup
  electronics detail (dual coils, phase switching) is present in the source but excluded from the
  guide page, which keeps controller/product-level specifics out.
- inference: none for the mechanism; this directly corrects the 2.0 page's "plucked" error.

### KEYS-11 Tine and reed electric pianos have a damper mechanism and a sustain pedal, pedalled much like a piano
- claim: on the tine (Rhodes-type) instrument, a felt damper contacts each tine from below at rest and
  is lifted by the key action; a foot-operated damper release bar disengages all dampers at once when
  the sustain pedal is pressed, functionally paralleling a piano's damper pedal even though the
  underlying sound-production mechanism is unrelated. On the reed (Wurlitzer-type) instrument, an
  individual felt-tipped damper arm rests on each reed and is lifted by the key's whip mechanism; a
  pedal-actuated cable and rod lift all damper felts at once for sustain, again functionally like a
  piano pedal. On both instruments, a peer-reviewed physical-model study found that striking with
  higher velocity produces a richer harmonic sound than playing softly, confirming velocity changes
  timbre, not only level, on both electromechanical pianos.
- source: TINE-EPIANO-MANUAL-1 (section); REED-EPIANO-SERVICE-1 (section); PFEIFLE-2017 (section)
- source_type: manual; performer; academic acoustics
- confidence: medium
- scope: the tine-type (Rhodes-type) and reed-type (Wurlitzer-type) electric pianos specifically;
  the academic source measured one example of each.
- limitations: the academic source is a physical-modelling engineering paper, not a performer-pedagogy
  source; it does not address playing technique, only the underlying acoustics and mechanism. The
  comparative claim about sustain length versus an acoustic piano is not directly measured by any
  source read here and stays `to-verify` on the page rather than asserted either way.
- inference: the direct correction of the 2.0 page's claim that the reed piano "sustains longer than
  an acoustic piano" is this pack's conclusion from the absence of any source supporting that claim,
  combined with damper-mechanism evidence showing these instruments are damped like a piano, not
  undamped.

## Corrections to the 2.0 page

1. **Clavinet mechanism (old page location ~137)**: 2.0 correctly avoided calling it a piano but did
   not specify the striking mechanism clearly. Corrected using `CLAVINET-FAQ-1`: struck by a
   rubber-tipped tangent against a fixed anvil, not plucked by a plectrum.
2. **Tine/reed electric piano pedalling (old page location ~142)**: 2.0 implied these instruments are
   not pedalled like a piano. Corrected using `TINE-EPIANO-MANUAL-1`, `REED-EPIANO-SERVICE-1` and
   `PFEIFLE-2017`: both have a damper mechanism and a sustain pedal, and are pedalled comparably to a
   piano, even though the underlying sound-production mechanism differs entirely.
3. **Reed electric piano sustain length (old page location ~134-135)**: 2.0 asserted these sustain
   longer than an acoustic piano. No source read here supports or refutes a specific comparative decay
   time; the page now marks this `to-verify` rather than asserting it.
4. **Sostenuto pedal (old page location ~51)**: not covered by any source read in this pass; added to
   the piano card as `to-verify` rather than invented, since neither `SMIT-PIANOACTION` nor
   `SPANSWICK-PEDAL` describes the sostenuto mechanism specifically.
5. **Hand span "a ninth comfortably" (old page location ~52)**: corrected using `PASK-HANDSPAN`: this
   is generous for a large fraction of hands, especially many women's hands, given cited figures.
6. **"More than five notes in one hand" rule (old page location ~146-147)**: the thumb-takes-two-keys
   point is not something any source read here states directly (it is elementary keyboard-technique
   observation); the guide keeps the correction but labels it `inference`, not `sourced`.
7. **"Up to roughly one hundred velocity layers per key" (old page location ~90)**: removed per the
   instruction to strip specific-sounding capability numbers from the guide; velocity-as-timbre is kept
   as a general behaviour, sourced from `WEINREICH-1977` (string coupling / hammer physics context) and
   `PFEIFLE-2017` (electric pianos specifically) rather than from an unnamed product's claimed layer
   count.
8. **Unison beating, stretch tuning, inharmonicity (thin in 2.0)**: thickened with `WEINREICH-1977`
   (coupling/aftersound) and `RAILSBACK-STRETCH-2015` (stretch tuning), the latter only at excerpt
   depth and labelled accordingly.
9. **Repetition rate and roll spread as "human properties, not calibration ones"**: kept as guide
   content, not moved to calibration, sourced for the repetition-rate mechanism via
   `SMIT-PIANOACTION`; roll spread remains `inference`, as no source read here measured it.

## Still to verify

- Exact repetition-rate figures across different action regulation states (`SMIT-PIANOACTION` gives
  one practitioner figure, not a study).
- The Railsback stretch's actual magnitude by register (only excerpt-depth read; open the JASA paper
  or Fletcher and Rossing directly).
- Whether reed or tine electric pianos genuinely sustain longer, shorter or comparably to an acoustic
  piano at a matched dynamic; no source read here measures this comparison directly.
- The sostenuto pedal's mechanism; no source read in this pass describes it specifically.
- Hammer felt as a nonlinear spring and the exact velocity-to-spectrum mapping, in Fletcher and
  Rossing, not opened for this work.
- Register and tessitura writing conventions in Adler, not opened for this work.
- The Indian hand-pumped harmonium tradition, deliberately scoped out of `NEWWORLD-REEDORGAN`'s
  Western-instrument coverage; would need its own tradition-institution sources under
  `CULTURALLY_SPECIFIC_INSTRUMENTS.md` if written up.
- Any measured figure for typical chord-roll spread or bellows-reversal timing; both are practitioner
  values until calibrated.
