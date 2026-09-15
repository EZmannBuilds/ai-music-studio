# Strings: research records

What was read, what was not, and the limits of each claim the guide page makes. The page carries
the conclusions; this file carries the evidence.

## Scope and method

The 2.0 page rested on one symphonic strings manual and unopened orchestration texts. For 2.1 the
same manual (Spitfire Symphonic Strings) was reopened in full via its public PDF (23 pages) and is
registered pack-wide as `STRINGS-LIBRARY-MANUAL-1`, read at section depth. Acoustics claims were
pursued through UNSW Music Acoustics (Joe Wolfe's group) and an open string-acoustics resource
written by Jim Woodhouse (Cambridge), both reachable and read at section or abstract depth.
Rimsky-Korsakov's *Principles of Orchestration* (Project Gutenberg #33900) was fetched and its string
chapters read at section depth. Two performer/pedagogy web sources (The Strad magazine; a violin
teacher's blog) were read in full. Adler, Piston, and Fletcher and Rossing remain unopened and are
cited only as `standard-reference`, per the pack's rule for paywalled standard texts. A patent
document and several forum/pedagogy pages on double bass bow grip and bow/bridge geometry were found
but not read at a depth that would support a `sourced` label; the related claims on the page are
`inference` instead.

## Records

### STR-01 Control model: dynamics, expression, legato overlap, onset offset, round robins, divisi voice count
- claim: long notes take dynamics from a continuous control that crossfades recorded dynamic layers
  and is described as the most important control; a separate expression control is a volume trim;
  legato patches are monophonic and need overlapping notes to trigger a transition, and the arriving
  note's velocity selects the transition style; samples are cut close to the true onset so a small
  negative track delay, not earlier notes, keeps written timing; round robins exist to avoid repeated
  identical attacks; a section has a practical voice count (about five for a full string orchestra)
  before divisi is needed.
- source: STRINGS-LIBRARY-MANUAL-1 (section)
- source_type: manual
- confidence: high
- scope: one symphonic strings sample library; the grammar (crossfaded dynamics control, monophonic
  legato with velocity-selected transitions, round robins, onset compensation) is consistent with
  the 2.0 page's cross-vendor excerpts, but this pass verified only this one product at depth.
- limitations: controller numbers, exact latency and exact voice-count figures are this product's
  own facts and are deliberately excluded from the guide page; another library may differ in numeric
  detail while sharing the same grammar.
- inference: none for the core claims; the general "sections have a practical voice count" framing
  is treated as portable instrument behaviour, not only a product fact, because it follows from how
  many players were recorded, not from software design.

### STR-02 Articulation list and technique descriptions (spiccato, sul ponticello, sul tasto, col legno, con sordino, harmonics, tremolo, trills, portamento)
- claim: articulations are distinguished by on-string vs off-string vs not-bowed playing; sul
  ponticello is bright and edged near the bridge, sul tasto is thin and soft over the fingerboard;
  col legno battuto strikes with the bow's wood; con sordino softens and darkens the tone; natural
  harmonics are touched at a node, artificial harmonics are stopped plus touched a fourth above;
  tremolo exists in unmeasured and tempo-locked measured forms; portamento is used both stylistically
  and to cross strings on large intervals; a half-muted "desk split" is a real recording/arranging
  technique.
- source: STRINGS-LIBRARY-MANUAL-1 (section)
- source_type: manual
- confidence: high
- scope: articulation naming and technique description as used by one manufacturer describing London
  session string players; the physical technique descriptions (bow position, mute placement, finger
  action) match standard orchestral practice as described in Rimsky-Korsakov.
- limitations: this is one library's articulation taxonomy; another ensemble or tradition may group
  or name techniques differently. The half-muted "desk split" description is specific to how this
  library was recorded and is not claimed as a universal orchestral default.
- inference: none.

### STR-03 Bowed onset physics: Schelleng and Guettler diagrams, bow force/speed/contact point
- claim: a bowed note's clean onset (Helmholtz motion) depends on the ratio of bow force to bow
  acceleration and on distance from the bridge; too little force gives a loose, surface-y onset, too
  much gives a scratchy one; moving toward the bridge widens the available force range in absolute
  terms but narrows it proportionally and raises the minimum force needed; bow speed, pressure and
  contact point together set both loudness and timbre with no loudness-only control.
- source: WOODHOUSE-SCHELLENG (section); WOODHOUSE-GUETTLER (section)
- source_type: academic acoustics
- confidence: medium
- scope: general bowed-string physics (originally developed for violin, generalises across the
  bowed string family); Schelleng's own force-limit predictions are noted elsewhere in the acoustics
  literature to not fully match later empirical measurements, particularly for minimum force, which
  this page does not repeat as a precise quantity.
- limitations: read through a secondary open web resource rather than Schelleng's or Guettler's own
  papers; no numeric force or timing values are asserted on the guide page, only the qualitative
  relationships, which is what the secondary source itself emphasises as robust.
- inference: applying the general onset-quality relationship (force/acceleration/contact point) to
  viola, cello and double bass by extension from violin, since the underlying stick-slip mechanism is
  the same bowed-string physics, is this page's own extension and is flagged as such in those cards.

### STR-04 Sustain mechanism, body resonance, sympathetic string ringing
- claim: a bowed string is continuously re-energised, so a bowed tone can hold or change freely
  within one stroke, unlike a struck or plucked string, which only decays; the violin body has its
  own resonant frequencies including a low air resonance near 300 Hz; a bowed string's overtones
  interacting with body resonances give the tone character; harmonics shift among resonant and
  non-resonant frequencies as pitch and finger position change.
- source: WOLFE-VIOLIN (section)
- source_type: academic acoustics
- confidence: high
- scope: violin acoustics specifically; extended to viola, cello and double bass by family analogy
  in this page (the excitation mechanism is shared; exact body resonance frequencies are not).
- limitations: the page does not carry instrument-specific body resonance frequencies for viola,
  cello or bass; only the violin's ~300 Hz figure is sourced.
- inference: extending the excitation-mechanism claims to the rest of the bowed string family.

### STR-05 Torsional waves and bowed pitch jitter
- claim: bowing a string with non-zero radius excites torsional (twisting) waves alongside the main
  transverse wave; because the total bow-string contact speed depends on transverse speed plus the
  torsional contribution, torsional waves can introduce small jitter into the transverse wave under
  some bowing conditions, audible as part of the bowed sound's character rather than as mistuning in
  a well-bowed note.
- source: BAVU-TORSIONAL (abstract)
- source_type: academic acoustics
- confidence: low
- scope: measured on one bowed string by an experienced player over a range of tunings, in a
  laboratory setting.
- limitations: only the abstract was read, not the results or discussion; the page states the
  mechanism qualitatively and does not claim a magnitude or a reliable audible threshold. The paper's
  own abstract notes that for a well-bowed string this effect is normally small.
- inference: applying this violin-string finding to viola, cello and double bass strings as a general
  bowed-string phenomenon; the paper's measurements are on one string only.

### STR-06 Sympathetic resonance of open strings
- claim: a note sharing a pitch class with an open string, or one of that string's overtones, sets
  the open string ringing sympathetically, adding fullness; this also functions as a practical
  in-tune check for the player, since exact tuning is what triggers strong sympathetic ringing.
- source: COREY-RESONANCE (full)
- source_type: performer
- confidence: medium
- scope: violin, described by a teaching violinist; the underlying physical principle (shared
  vibrational modes between a bowed string and a free string of the same or related pitch) is general
  string-instrument physics and is extended to viola, cello and bass in this page.
- limitations: this is a pedagogy/performer blog, not a peer-reviewed acoustics source; no measured
  figures are claimed, only the qualitative phenomenon and its use in practice.
- inference: extending the violin-specific description to viola, cello and double bass by analogy.

### STR-07 Spiccato vs. sautillé
- claim: spiccato is a player-controlled bounce (an individual impulse thrown for every note) used
  from slow to moderately fast tempo; sautillé is a bow-controlled bounce, relying on the stick's own
  resilience, used where spiccato runs out of time, and is best played with the bow staying close to
  the string.
- source: STRAD-SPICCATO (full)
- source_type: performer
- confidence: high
- scope: violin/viola-family bow technique as described by cited pedagogues (Galamian, Flesch,
  Dounis, Hodgson) in a professional string-playing magazine; the same distinction is treated in this
  page as applying to cello, with double bass noted separately as a harder case because of string
  mass.
- limitations: no specific tempo boundary is asserted on the guide page beyond "spiccato yields to
  sautillé at speed," since the cited pedagogues' exact tempo markers vary by source.
- inference: extending the distinction to cello without a cello-specific source.

### STR-08 Orchestration-text context: ranges, chords, mutes, harmonics character
- claim: strings can play double stops and chords across three or four strings but the text does not
  describe sustaining a full chord; harmonics narrow dynamic range and give a "cold" or "glassy"
  colour; con sordino reduces volume and can produce a hiss or whistle at loud dynamics; historical
  practical ranges are given for violin, viola, cello and double bass.
- source: RIMSKY-1913 (section)
- source_type: orchestration
- confidence: medium
- scope: late-19th/early-20th-century Russian orchestral practice as codified by Rimsky-Korsakov and
  his editor; ranges and idioms are conservative relative to later 20th- and 21st-century solo and
  film-scoring practice.
- limitations: this text was read via an automated extraction of the relevant chapters rather than
  cover to cover; its practical ranges are narrower than the manual's curated professional-section
  ranges and are used on the page only as historical context, not as the page's primary range table.
- inference: none beyond noting the historical range figures are narrower than the manual's.

### STR-09 Viola body proportion and character (standard-reference)
- claim: the viola's body is proportionally smaller than acoustic theory would predict for its pitch
  range, which is part of why its middle register reads as covered or distinctive rather than as a
  scaled-up violin.
- source: FLETCHER-ROSSING-1998 (not-read)
- source_type: standard reference
- confidence: low
- scope: attributed only; this is a widely cited acoustic fact about the viola in general
  instrument-acoustics literature.
- limitations: not opened for this work; carried only because it is a claim that text is widely known
  to make, per the pack's rule for paywalled standard references.
- inference: none; labelled `standard-reference` rather than `academic` for this reason.

## Corrections to the 2.0 page

- **Chord sustain and open strings.** The 2.0 page said sustained chords of three or more notes are
  broken "unless open strings support it." That is corrected: the bow's flat hair ribbon meeting the
  arched bridge limits continuous contact to at most two adjacent strings regardless of whether the
  strings involved are open or stopped; open strings do not change this geometry. The correction also
  softens the 2.0 page's separate claim that such chords are "always" broken, since a fast attack at
  forte can catch three strings together for a brief instant before the bow settles. Both changes are
  labelled `inference`, since no source at section depth was found that states the bow/bridge
  geometry explicitly; the correction rests on the shared mechanical description found across bowed-
  string acoustics discussion and orchestration texts (Rimsky-Korsakov describes only sustained
  double stops and rolled/arpeggiated full chords, never a sustained triad or tetrad).
- **Vibrato onset.** The 2.0 page said vibrato "develops across a note rather than starting with it."
  This is corrected to a style-dependent choice: the reopened manual records long articulations with
  vibrato present from the start ("molto vib"), absent ("senza vib"), and at an intermediate amount
  ("dolce"), which only makes sense if onset and amount are interpretive choices rather than one
  universal rule. `manual-derived: STRINGS-LIBRARY-MANUAL-1`
- **Range table.** The 2.0 page's range table was unsourced (`orchestration-text`, Adler and Piston,
  neither opened). It is replaced with the manual's own curated professional-section ranges
  (`manual-derived`), with Rimsky-Korsakov's older, narrower historical figures kept as separate
  context (`sourced: RIMSKY-1913`), and Adler/Piston kept only as a `to-verify` pointer for solo
  extremes.
- **Control model and articulation list.** Confirmed and substantially extended from the 2.0 page's
  version: the 2.0 page had the dynamics/expression/legato/onset-delay/round-robin grammar right at a
  high level; this pass adds the specific transition-style-by-velocity mechanism, the full named
  articulation list, and the half-muted desk-split technique, all `manual-derived` from the same
  manual reopened in full.

## Still to verify

- Exact solo-repertoire range extremes (top of violin range in virtuoso writing, cello's highest
  practical harmonics, etc.) against Adler, *The Study of Orchestration*, or Piston, *Orchestration*.
  Neither opened.
- The spectral mechanism behind sul ponticello's brightness (why bowing near the bridge favours
  higher harmonics) against Fletcher and Rossing, *The Physics of Musical Instruments*. Not opened.
- Whether double bass French/German bow grip produces a measurable, generalisable difference in
  spiccato/sautillé response, beyond forum and pedagogy-page anecdote. No source read at section
  depth was found; the page's grip-difference claim is `inference` and should be checked against a
  double bass method book or the International Society of Bassists' materials.
- A measured figure for orchestral string-section attack spread (how many milliseconds a section's
  onsets typically scatter across). Not available in any source opened for this work; recommended
  path is calibration against a real recorded section rather than a literature search.
