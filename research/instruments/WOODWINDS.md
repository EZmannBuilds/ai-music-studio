# Woodwinds: research records

What was read, what was not, and the limits of each claim the guide page makes. The page carries the
conclusions; this file carries the evidence.

## Scope and method

Reachable and read: UNSW Music Acoustics' clarinet-acoustics and flute-acoustics introduction pages
(fetched directly, extracted page content read, not a search snippet); Joe Wolfe's *Acoustics Today*
2018 woodwind overview and Chen, Smith & Wolfe's 2011 saxophone vocal-tract-tuning paper, both held as
full downloaded text and read at the passages relevant to breath/air-flow physics, register mechanics
and altissimo/bend/multiphonic technique; two Bret Pimentel pedagogy articles (oboe stale air,
saxophone vibrato); two tamingthesaxophone.com pedagogy pages (subtone, growl); Rimsky-Korsakov and
Forsyth, both held as full public-domain text and read at the specific passages on woodwind breath,
character and the double-bassoon's history.

Tried and not usable: UNSW's dedicated oboe and double-reed acoustics pages, which state on their face
that detailed double-reed acoustics were not yet written up at the time of the page. Not cited.

Unreachable: Adler, Piston, Fletcher and Rossing — paywalled/not opened, as the 2.0 page already
stated.

Read depth was judged the same way as in the brass work this session also produced: a fetch that
returned the extracted body of the target page is `section`; a source held as a full downloaded text
but sampled only at specific passages is `section` for the claims those passages support, not `full`.

## Records

### WW-01 The oboe's breath problem is stale air, not air hunger — correcting a backwards 2.0 claim
- claim: the oboe's double reed has a very small opening, so air leaves the lungs slowly; this means an
  oboist typically has *too much* air left over at a phrase end, not too little, and the practical
  problem is expelling stale, CO2-rich air rather than running out of breath. This is the opposite of
  the flute, which consumes air quickly and does run short. Some oboists exhale before inhaling at a
  breath mark specifically to clear stale air before taking a fresh breath.
- source: PIMENTEL-STALEAIR (section)
- source_type: pedagogy
- confidence: medium
- scope: oboe primarily; the source notes the same issue "sometimes" affects clarinetists, which is
  kept as a brief aside rather than a full clarinet claim, since it was not elaborated in the source.
- limitations: confidence is high for the mechanism and the oboe-specific practice (exhale-before-
  inhale) but only medium for the general framing "the flute is the air-hungry one," which the source
  implies by contrast rather than stating as a direct comparison, so the record is scored at the lower
  figure. A single pedagogy blog post, not a physiology or acoustics paper; no measured airflow
  figures.
- inference: the explicit contrast with the flute's air consumption is the guide's synthesis of this
  source together with WOLFE-AT2018's general point that mouth air flow "varies with instrument," not a
  side-by-side comparison stated in one place by either source.

### WW-02 Clarinet register structure and the break, with an acoustic reason for the throat register's weakness
- claim: the clarinet has four practically distinct registers (chalumeau, throat, clarion/clarino,
  altissimo); the break sits between A#4 and B4, at the point the speaker key takes over as the register
  hole; the throat register (roughly E4-A#4) is acoustically weaker and less stable than the chalumeau
  register because those notes have only two bore resonances that line up well with their harmonics,
  making their pitch easier to bend/destabilise than chalumeau notes.
- source: UNSW-CLARINET-INTRO (section)
- source_type: academic acoustics
- confidence: high
- scope: B-flat clarinet acoustics generally; the register names and break point are conventional across
  clarinet pedagogy, and the acoustic explanation is specific to how the bore behaves as a closed pipe
  with a register hole.
- limitations: does not separately address the A clarinet or bass clarinet; the register break's exact
  written pitch is assumed to hold across clarinet sizes by convention, which is an inference, not
  independently confirmed for A or bass clarinet in this source.
- inference: extending the same register map (with a transposed break point) to the A clarinet and, at
  a lower absolute pitch, to the bass clarinet is the guide's inference, consistent with how clarinet
  pedagogy generally treats the family, not a claim UNSW-CLARINET-INTRO makes about those instruments.

### WW-03 Clarinet overblows at the twelfth, not the octave, and this is why it is written as it is
- claim: the clarinet, because it is acoustically closed at the reed end, behaves like a stopped pipe
  and its harmonic series contains predominantly odd multiples of the fundamental; opening the register
  hole disrupts the fundamental far more than the higher harmonics, so the instrument jumps to its third
  harmonic (a twelfth above) rather than its second (an octave above) the way an open pipe instrument
  does.
- source: UNSW-CLARINET-INTRO (section)
- source_type: academic acoustics
- confidence: high
- scope: single-reed cylindrical-bore instruments generally (clarinet family); does not extend to
  saxophone, which is conical and overblows at the octave like most other woodwinds.
- limitations: none identified; this is settled acoustics, presented at introductory depth.
- inference: none.

### WW-04 Flute pitch is coupled to blowing pressure, not just loudness — correcting the 2.0 page's account of why
- claim: raising a flute's pitch, especially into the upper register, requires increasing blowing
  pressure to raise jet speed so the jet matches the higher-frequency bore resonance; players are also
  taught to narrow the lip aperture for high notes. Because pitch and blowing pressure are linked this
  way, playing louder (which also usually means blowing harder) tends to sharpen the pitch, and playing
  softer tends to flatten it, unless the player compensates.
- source: UNSW-FLUTE-INTRO (section)
- source_type: academic acoustics
- confidence: medium
- scope: concert flute (and by extension piccolo and alto flute, sharing the same air-jet excitation
  mechanism); not independently confirmed for piccolo/alto flute specifically.
- limitations: confidence is high for the mechanism itself, but the specific claim "a flute playing
  loudly at the bottom of its range fights the instrument" (kept from the 2.0 page) is a reasonable
  extension of this mechanism rather than a form the source states directly, so the record is scored
  at the lower figure. General-audience acoustics page; no measured cents-per-dynamic figure.
- inference: the piccolo/alto flute extension and the specific "fighting the instrument" framing are
  carried as inference from the general mechanism.

### WW-05 Saxophone altissimo, bends and multiphonics are vocal-tract tuning, not just fingering or embouchure alone
- claim: experienced saxophonists control altissimo notes, pitch bends, and multiphonic/chord
  combinations by actively tuning their own vocal tract's acoustic resonance to reinforce a particular
  bore resonance; less experienced players cannot produce a vocal-tract resonance peak strong enough to
  compete with the bore's own resonances and so cannot reliably access these techniques. In ordinary
  playing within the standard range, players do not need to tune the tract this way.
- source: SAXJASA-2011 (section: abstract and the vocal-tract-tuning findings read directly; the
  detailed impedance-spectrum measurement methodology was not examined in depth)
- source_type: academic acoustics
- confidence: high
- scope: saxophone (the paper's own instrument); the general vocal-tract-tuning principle is shared with
  other reed and some brass instruments in the wider acoustics literature, but this source addresses
  saxophone specifically.
- limitations: a measurement study of experienced versus less-experienced players' impedance spectra,
  not a pedagogy text; it explains *why* altissimo is hard for beginners but does not by itself teach
  the technique.
- inference: none for the mechanism; the framing "this is why altissimo is a specialist technique, not
  a fingering chart problem" is the guide's synthesis, consistent with the paper's own framing.

### WW-06 Subtone, growl and jazz/classical vibrato are named, distinct saxophone techniques with different mechanisms
- claim: subtone is an embouchure/voicing technique (relaxed jaw, less mouthpiece in the mouth, often
  played with a breathier legato attack) most effective in the low register, producing a fatter, warmer,
  less edgy tone with reduced upper-mid frequency content; growl is produced by humming or singing a
  *different* pitch (not the fingered pitch) while playing, which creates audible interference/beating
  rather than a vocal distortion effect as such; jaw vibrato (moving the jaw in a small, controlled
  up/down motion) is the primary vibrato mechanism on saxophone; classical vibrato is faster, narrower,
  and begins at the onset of the note, while jazz vibrato is often slower/more variable and frequently
  delayed, added partway through a sustained note ("terminal" vibrato) rather than present from the
  start.
- source: TAMINGSAX-SUBTONE (section, subtone); TAMINGSAX-GROWL (section, growl); PIMENTEL-SAXVIBRATO
  (section, vibrato mechanism and the classical/jazz contrast)
- source_type: pedagogy
- confidence: medium
- scope: saxophone family generally; none of the three sources distinguishes soprano/alto/tenor/
  baritone behaviour for these specific techniques, so the guide treats them as shared across sizes,
  which is an inference.
- limitations: no acoustic measurement of the interference mechanism in growl, or of the spectral change
  in subtone, beyond the qualitative descriptions and the one waveform comparison TAMINGSAX-SUBTONE
  mentions but this session did not independently verify.
- inference: applying all three techniques uniformly across soprano through baritone saxophone.

### WW-07 Written versus sounding pitch was missing across the family and is now stated per instrument
- claim: clarinet in B-flat sounds a major second below written pitch; clarinet in A sounds a minor
  third below written pitch; cor anglais sounds a perfect fifth below written pitch; piccolo sounds an
  octave above written pitch; alto flute sounds a perfect fourth below written pitch; soprano and tenor
  saxophone are B-flat instruments (tenor also down an octave relative to soprano's transposition
  interval); alto and baritone saxophone are E-flat instruments (baritone also down an octave relative
  to alto). Flute, oboe and bassoon are non-transposing (written equals sounding).
- source: ADLER-ORCH (not-read); PISTON-ORCH (not-read). The intervals were checked against a
  transposition reference chart reached via web search summary, but that chart is not independently
  registered as a source: it is not a primary orchestration text, and the underlying page was not
  fetched and read directly.
- source_type: standard reference
- confidence: medium
- scope: standard modern orchestral/band transposition convention.
- limitations: the interval values themselves are uncontested convention and consistent across every
  orchestration source this session has encountered, which is why they are used at all, but neither
  Adler nor Piston was actually opened for this work, so the page cites them only as
  `standard-reference`, not `sourced`.
- inference: none for the interval values; labelled `standard-reference` on the page rather than
  upgraded to `sourced`, specifically because of the shallow read depth.

## Corrections to the 2.0 page

- **The oboe breath claim was backwards.** 2.0 said reed instruments have breath "shorter than a
  singer's... because the reed consumes air," implying the oboe is short of breath like a singer taking
  frequent breaths. In fact the oboe's reed passes very little air, so oboists commonly have air *left
  over* at a phrase end and must manage stale, CO2-rich air rather than running out of breath; the flute
  is the family's genuinely air-hungry instrument. `sourced: PIMENTEL-STALEAIR`.
- **"Key-sensitive in a way string writing is not" was simply wrong** and is removed. String writing is
  strongly key-sensitive (open strings, double-stop fingerings, position changes all depend on key). The
  underlying true claim — that some keys and fingerings are more awkward on woodwinds than others,
  which affects trill and rapid-figure difficulty — is kept, but the false comparison to strings is cut.
  No new source was needed to identify this as an error; it follows directly from `STRINGS.md`'s own
  documented control model, which the 2.0 woodwinds page had not been checked against.
- **"Vary velocity on repeated notes, which is error 1" is replaced with named causes.** The bare
  instruction to vary velocity, with no stated reason, is exactly the kind of unmodelled humanisation
  `HUMAN_PERFORMANCE_SCHEMA.md` section 1 forbids. It is replaced with the two real causes that produce
  repeated-note variation on woodwinds: tonguing alternation in double/triple tonguing (a different
  articulation each repetition, not just a different velocity), and metrical accent (position in the
  bar).
- **Saxophone was named in the family title but never covered.** The 2.0 page's body discussed flute,
  oboe, clarinet and bassoon only. Four saxophone cards are added (soprano, alto, tenor, baritone,
  sharing one card with per-size differences noted), covering range, subtone, growl, bends/altissimo,
  and jazz-versus-classical vibrato, sourced from SAXJASA-2011 and three pedagogy sources.
- **Written-versus-sounding pitch was missing for every transposing instrument in the family**
  (clarinet B-flat/A, cor anglais, piccolo, alto flute, and all four saxophones). Added throughout.
- **Auxiliaries (piccolo, alto flute, cor anglais, bass clarinet, contrabassoon) were named only in
  passing or not at all.** Each now has its own row of differences inside its parent instrument's card.
- **Resonance was not addressed as its own behaviour anywhere in the file.** Added per instrument,
  covering bore resonance and (for saxophone) vocal-tract resonance tuning specifically.

## Still to verify

- The clarinet break's exact written pitch on the A clarinet and bass clarinet (WW-02's inference).
- Whether subtone, growl and the classical/jazz vibrato contrast (WW-06) hold identically across
  soprano, alto, tenor and baritone saxophone, or differ by size; no source read this pass addresses
  register-size differences for these specific techniques.
- The transposition intervals in WW-07 at full read depth, from a primary orchestration source (Adler
  or Piston) rather than a web-search-summarised chart.
- Practical ranges, trill tables and key-sensitivity of figuration in Adler and Piston, neither opened.
- Pitch-dynamic coupling on the flute at the textbook-acoustics level (magnitude in cents per dynamic
  step, not just the mechanism), in Fletcher and Rossing. Not opened.
- Measured typical breath lengths by instrument, register and dynamic. Still not available from any
  source read for this pack; remains practitioner judgement.
