# Brass: research records

What was read, what was not, and the limits of each claim the guide page makes. The page carries
the conclusions; this file carries the evidence.

## Scope and method

Tried and reachable: UNSW Music Acoustics' brass acoustics overview (fetched and read in full via
the page's actual content, not a search snippet); Hirschberg et al. 1996 on trombone shock waves
(PDF, abstract and introduction read directly); Horn Matters' stopping-valve article; two horn
pedagogy forum posts found in search but not independently fetched (not cited); Rimsky-Korsakov's
*Principles of Orchestration* and Forsyth's *Orchestration*, both held as full public-domain text
files and read at the specific passages on stopped/muted brass and the double-bassoon; a PALNI open
brass pedagogy text's "Advanced Techniques" chapter; an ITA-archived trombone vibrato article; a
trumpet-pedagogy blog's glissando article; one trumpet-mute blog reachable only through a search
engine's cached summary (its own site would not resolve by DNS, so it is recorded as `excerpt`, not
`section`).

Unreachable: Adler and Fletcher & Rossing (paywalled/not opened, as the 2.0 page already stated).
The UNSW clarinet and flute pages were fetched too, but they belong to the woodwinds work.

Read depth was judged by what was actually returned to this session: a fetch that returned the
extracted body text of the target page is `section`; a search-engine summary of a page this session
never opened is `excerpt`; a source held as a full downloaded text but only sampled at specific
passages is recorded as `section` for the claims those passages support, not `full`, because the
surrounding hundreds of pages were not read.

## Records

### BRASS-01 Brass sound production and dynamic-timbre coupling
- claim: the lips act as a pressure-controlled valve; loud playing drives the lips into sharper,
  more nonlinear closure, adding high harmonics, and this (not just added amplitude) is why louder
  brass is brighter.
- source: UNSW-BRASS (section)
- source_type: academic acoustics
- confidence: high
- scope: brass lip-reed instruments generally; the UNSW page discusses trumpet and trombone bores
  explicitly and the mechanism (lip valve, nonlinear closure) generalises to the whole family.
- limitations: a general-audience acoustics page, not a peer-reviewed paper; no instrument-by-
  instrument quantification.
- inference: none for the mechanism; the extension "this is why a swell must be programmed as a
  layer crossfade, not a fader move" is the guide's inference from the acoustic fact, not a claim the
  source makes about virtual instruments.

### BRASS-02 Shock-wave formation as the extreme case of dynamic brightening
- claim: at fortissimo, wave propagation inside a trombone's bore becomes nonlinear enough to form
  actual shock waves (stepwise pressure jumps), which is the physical cause of the "brassy"/cuivré
  edge at high dynamics; this is a stronger and separate claim from ordinary spectral brightening.
- source: HIRSCHBERG-1996 (section: abstract and introduction read; the pressure-measurement figures
  in the body were not examined)
- source_type: academic acoustics
- confidence: medium
- scope: measured on a trombone specifically ("the trombone used in our experiments"), at fortissimo.
  The paper frames the finding as relevant to "the brightness of related brass instruments played at
  fortissimo levels," so the authors themselves generalise cautiously.
- limitations: confidence is high for trombone specifically but only medium as a generalisation to
  other brass, so the record is scored at the lower figure. One instrument measured; the guide extends
  the finding qualitatively to brass as a family rather than asserting shock waves occur identically on
  horn or tuba, which have different bore proportions.
- inference: none beyond the paper's own stated generalisation.

### BRASS-03 Stopped horn raises pitch by different amounts on the two sides of a double horn
- claim: hand-stopping raises pitch by roughly a semitone on the F side of a double horn, but by
  roughly three-quarters of a tone on the B-flat side, which is uneven enough that horn makers built
  a stopping valve (extra tubing, engaged only for stopped notes) specifically to correct it.
- source: UNSW-BRASS (section, for the "about a semitone" figure and the acoustic reason: hand
  insertion reduces bell radiation, shifting which resonance is strong); HORNMATTERS-STOPVALVE
  (section, for the differing amounts on F versus B-flat and the existence and purpose of the
  stopping valve); FORSYTH-1914 (section, for a 1914 account already distinguishing the old gradual
  hand-lowering technique from the newer hard-stopped "one true semitone above" and for naming D. J.
  Blaikley's explanation as unresolved at the time)
- source_type: academic acoustics (UNSW), pedagogy (Horn Matters), orchestration (Forsyth)
- confidence: medium
- scope: modern double horns in F/B-flat; single B-flat horns and descants, where the valve problem
  is most acute, are named directly in HORNMATTERS-STOPVALVE.
- limitations: confidence is high for the semitone/three-quarter-tone contrast and the stopping
  valve's purpose (a current, specialist horn-pedagogy source states it plainly) but only medium for
  the acoustic explanation of *why* the two sides differ, which none of the three sources actually
  derives (UNSW gives the general mechanism for hand-stopping, not the F-versus-B-flat asymmetry
  specifically), so the record is scored at the lower figure. None of the three sources gives a
  first-principles acoustic derivation of *why* the B-flat side rises further than the F side; that
  remains to-verify against a horn-acoustics paper rather than a pedagogy page.
- inference: none for the magnitudes; the framing "this is why stopping valves exist" is stated
  directly in HORNMATTERS-STOPVALVE, not inferred.

### BRASS-04 Falls, doits and rips are lip, valve-slide or half-valve glissandi, not simple harmonic-series walks
- claim: a "through the harmonic series" gesture is only one of several mechanisms; players also bend
  with the embouchure alone (small intervals, asymmetric range), use the first/third valve slides for
  a true pitch-continuous glissando on a minor second or smaller, and use half-valve fingering for a
  glissando across intervals the slides and embouchure alone cannot reach.
- source: MODERNTRUMPET-GLISS (section)
- source_type: pedagogy
- confidence: medium
- scope: trumpet specifically; trombone doits/falls are physically simpler because the slide gives a
  true continuous glissando directly, and valved low brass (tuba, valve trombone) share the trumpet's
  valve-slide and half-valve options in principle, but this was not confirmed instrument-by-
  instrument.
- limitations: single pedagogy blog, not cross-checked against a second trumpet source; does not
  cover horn, which has no valve slides usable this way and relies on lip and hand.
- inference: the extension to trombone (true glissando via the slide directly, not needing a
  half-valve analogue) and to horn (lip/hand only) is the guide's inference from the mechanics
  already established in COMMON_ERRORS and BRASS.md's own slide-reach material, not from this source.

### BRASS-05 Brass vibrato is not one technique
- claim: brass players use several distinct vibrato mechanisms — jaw (most common across the family),
  lip, hand (shaking the instrument, trumpet-specific in practice), slide (trombone-specific), and
  diaphragm/air (rare on brass) — and instrument and style predict which is used: jaw vibrato is
  near-universal on euphonium, trombone favours jaw and slide (sometimes combined), jazz trumpet
  favours lip or hand, and most horn teachers do not teach vibrato as a default at all.
  Diaphragm/air vibrato is common on flute but rare on brass.
- source: BRASSPED-PALNI (section); TROMBONE-ORG-VIBRATO (section, trombone detail and the
  jaw+slide "combination" vibrato)
- source_type: pedagogy
- confidence: medium
- scope: modern trumpet, trombone, euphonium/tuba pedagogy, mostly American; the horn-teachers
  finding is reported by the pedagogy text as a mid-1970s survey result, not independently verified
  here.
- limitations: neither source is a peer-reviewed survey; the "most horn teachers don't teach vibrato"
  claim rests on one secondary citation inside BRASSPED-PALNI that this session did not trace to its
  original survey.
- inference: none beyond what the two pedagogy sources state.

### BRASS-06 Mute types are physically distinct devices, not one filter with settings
- claim: straight, cup, harmon and plunger mutes are different physical objects with different
  acoustic effects (straight: bright/nasal/piercing; cup: softer and warmer, adjustable by insertion
  depth; harmon: buzzy and direct with the stem in, capable of the hand/plunger "wah-wah" pitch-and-
  tone bend with the stem removed and the opening covered; plunger: held by hand at the bell, opening
  and closing it changes both loudness and which harmonics radiate), and a practice mute exists purely
  to quiet the instrument for private practice rather than to change its tone for performance.
- source: TRUMPETMUTES-NOTESTEM (excerpt: reached only via a search engine's summary of the page,
  because the page itself did not resolve when fetched directly)
- source_type: performer
- confidence: medium
- scope: trumpet mutes specifically; trombone and horn straight/cup/harmon-style mutes are physically
  larger versions of the same idea and are treated as sharing this behaviour, which is an inference,
  not something the source states for those instruments.
- limitations: the description is consistent with general knowledge of these mutes and with
  RIMSKY-1913's much older but consistent statement that stopped and muted notes both deaden
  resonance and can approach a reed-instrument-like timbre, but the specific source was read only at
  excerpt depth: no acoustic derivation, just a practitioner description.
- inference: extending the trumpet-mute description to trombone mutes of the same names is the
  guide's inference; tuba is noted (following RIMSKY-1913) as rarely muted at all.

### BRASS-07 Stopped notes and mutes were historically available only on instruments the hand can reach
- claim: hand-stopping is physically possible only where a hand can be inserted into the bell
  (historically horn, trumpet, cornet); trombone and tuba bell geometry excludes it, so those
  instruments rely on external mute devices rather than hand technique, and even mutes were applied
  to tuba only rarely.
- source: RIMSKY-1913 (section)
- source_type: orchestration
- confidence: medium
- scope: the orchestral brass section as constituted in the early twentieth century; does not address
  later mute designs (harmon, plunger) that postdate the text.
- limitations: a 1913 practitioner-orchestrator's statement, not an acoustics paper, but consistent
  with the instruments' physical geometry, and read at section depth, which is why the page cites it
  as `sourced` rather than `standard-reference`. Pre-jazz-mute vocabulary; "stopped and muted notes
  are similar in quality" is Rimsky's own impression, not a measurement, and is not upgraded beyond
  what he states.
- inference: none; restated close to the source's own framing.

### BRASS-08 Endurance and the phrase-as-breath model apply across the family, with tuba's low register additionally slow to speak
- claim: no new source materially changed this from the 2.0 page's `musicianship` framing; it is kept
  as inference, not upgraded, because none of the read sources measured phrase length or endurance
  decay directly.
- source: none upgraded; RIMSKY-1913 (section) supports only the general, cross-family statement that
  wind players "cannot manage extremely long sustained passages" and need rest, without brass-specific
  timing.
- source_type: orchestration
- confidence: low
- scope: general wind playing, not brass-specific in Rimsky's statement.
- limitations: low confidence as a quantified claim; kept as `inference` on the page for anything with
  a number or a specific bar count attached. No source read for this project gives a measured brass
  breath duration.
- inference: everything about *how much* endurance costs, and *how quickly* fatigue shows up in
  attack quality, remains the guide's musicianship inference, unchanged from 2.0 except for being
  correctly labelled.

## Corrections to the 2.0 page

- **Stopped horn pitch rise.** 2.0 said hand-stopping "raises the pitch by about a semitone" without
  qualification. That is true on the F side (UNSW-BRASS, HORNMATTERS-STOPVALVE, FORSYTH-1914) but
  understates the B-flat side, which rises nearer three-quarters of a tone — enough that horn makers
  added a dedicated stopping valve to correct it (HORNMATTERS-STOPVALVE). The 2.0 page also gave no
  written-vs-sounding statement for the horn at all; that is added.
- **Falls, doits and rips as "through the harmonic series."** 2.0 stated these are produced by moving
  "through the harmonic series," with no other mechanism named. MODERNTRUMPET-GLISS documents lip
  bending, valve-slide glissando and half-valve technique as the actual mechanisms in use, with the
  harmonic-series overtone glissando as only one option among several and the least flexible for
  interval size.
- **The swell-as-timbre-change claim was `to-verify` and unsupported.** 2.0 flagged this as important
  but unopened. It is now supported directly: UNSW-BRASS gives the general mechanism (nonlinear lip
  closure adding harmonics at higher blowing pressure) and HIRSCHBERG-1996 gives the extreme case
  (measured shock-wave formation in a trombone at fortissimo). The claim moves from `to-verify` to
  `academic`.
- **No written-vs-sounding statement anywhere on the 2.0 page**, despite horn (F, sounding a fifth
  below written) and B-flat/C trumpet both being transposing instruments in the horn's case and the
  B-flat trumpet's case. Added to every relevant `practical_range` row.
- **Mutes described only generically ("a mute changes the tone")**, with no distinction between mute
  types. TRUMPETMUTES-NOTESTEM (excerpt) and RIMSKY-1913 (section) together support naming straight,
  cup, harmon and plunger mutes as physically and acoustically distinct, plus stating that a practice
  mute exists for a different purpose (quieting practice, not shaping performance tone).
- **Vibrato was entirely absent from the 2.0 page.** BRASSPED-PALNI and TROMBONE-ORG-VIBRATO now
  support a `vibrato` row naming the mechanisms per instrument.
- **Half-valve technique and valve/slide noise were absent.** Added from MODERNTRUMPET-GLISS
  (half-valve) and kept as `inference` for the noise itself (no source measured valve or slide
  mechanism noise).

## Still to verify

- The acoustic *reason* the B-flat side of a double horn rises further than the F side when stopped
  (BRASS-03). Settle this against a horn-acoustics paper or the International Horn Society's own
  technical pages, which this session found in search but did not fetch.
- Fletcher and Rossing, *The Physics of Musical Instruments*, for the general, textbook-level account
  of dynamic-dependent spectral brightening across the whole brass family (not only the trombone case
  HIRSCHBERG-1996 measured). Not opened.
- Measured brass phrase/endurance figures (how long a passage before fatigue measurably changes
  attack). No source read here measures this; it remains practitioner inference.
- Trombone- and horn-specific mute acoustic descriptions (TRUMPETMUTES-NOTESTEM covers trumpet only,
  at excerpt depth). A horn- or trombone-specific mute source would let those rows move off inference.
- TRUMPETMUTES-NOTESTEM itself: the live page would not resolve by DNS when this session tried to
  fetch it directly, so it is recorded at excerpt depth via a search engine's cached summary. Refetch
  and re-read directly before relying on it for anything beyond the current, cautious claim.
