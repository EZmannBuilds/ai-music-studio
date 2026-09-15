# Mridangam: research records

What was read, what was not, and the limits of each claim the guide page makes. The page carries the
conclusions; this file carries the evidence.

## Scope and method

Two closely related sources by the mridangam vidwan Umayalpuram K Sivaraman, with materials scientist
T Ramasami (and, in the later work, M D Naresh), were read: a 2010 National Institute of Advanced
Studies memorial lecture ("Science for Musical Excellence", read in full) and a 2023 arXiv introductory
review, by a third author, of their subsequent book-length work "Musical Excellence of Mridangam" (read
at section depth: the construction chapter and the tonal-properties chapter in full detail, the
alternative-materials and future-design chapters skimmed for anything bearing on established, rather
than proposed, practice). Sivaraman is one of the most senior living Carnatic mridangam performers and
teachers, which is what supplies this page's practitioner source under
`CULTURALLY_SPECIFIC_INSTRUMENTS.md` step 1. C V Raman's 1920 and 1934/35 papers were read in full (the
1934/35 paper's primary worked example, the "Mridanga", is the classical two-headed barrel drum this
page covers; Raman's "Thabla" is the separate tabla, covered on its own page). Malu and Siddharthan's
2000 arXiv paper, which models the loaded membrane generally across this drum family, was read at
section depth (already read in full for `research/instruments/TABLA.md`; re-cited here for its direct relevance to
the mridangam's shared black-patch mechanism). Two IIT Madras "Science of Musical Instruments"
(ED5321) course materials, hosted at ed.iitm.ac.in as named in the task brief, were read in full: a
short construction sub-page ("Parts of Mridhangam") and a slide deck ("Introduction to Music -
Mridangam", M Ramanathan). David Courtney's tabla/mridangam contrast article, already read in full for
the tabla page, is re-cited here for its direct mridangam claims. No dedicated ethnomusicological
monograph on Carnatic percussion was identified or opened this pass.

## Records

### MRIDANGAM-01 Construction: shared shell, multi-layer valanthalai, unloaded thoppi
- claim: the mridangam is a single wooden barrel shell (traditionally jackfruit-tree wood) with two
  different heads at each end sharing one resonating body; the right head (valanthalai) is a multi-layer
  laminate (ulkaraithattu, kottuthattu/paatuthattu carrying the black patch, vettuthattu) with an annular
  space filled by kucchi (reed strips) or thool (black-patch material); the left head (thoppi) is a
  simpler buffalo-skin membrane, not permanently loaded.
- source: KUMAR-REVIEW-2023 (section); SIVARAMAN-NIAS-2010 (full); IITM-MRIDANGAM-PARTS (full)
- source_type: academic acoustics (KUMAR-REVIEW-2023 reviewing a practitioner-authored book); performer
  (SIVARAMAN-NIAS-2010); tradition institution course material (IITM-MRIDANGAM-PARTS)
- confidence: high
- scope: general Carnatic mridangam construction, corroborated across an independent
  practitioner-authored source, an academic review of the practitioner's fuller work, and an
  institutional course page
- limitations: KUMAR-REVIEW-2023 is itself a secondary review of "Musical Excellence of Mridangam"
  (Sivaraman, Ramasami and Naresh's own book), not that book directly; this page's claims trace to the
  review's account of the book's content, not to the book itself, which was not independently obtained.
  IITM-MRIDANGAM-PARTS includes some claims (mythological origin narrative) this page does not repeat as
  fact, and gives construction-material detail (karanai composition as manganese powder, rice and iron
  powder) that differs slightly in emphasis from KUMAR-REVIEW-2023's account (ferric-oxide powder); both
  are reported rather than silently reconciled.
- inference: none for the core layered-construction claim, which both source lines state directly.
- tradition_scope: general Carnatic mridangam construction; not attributed to one lineage or region in
  either source.

### MRIDANGAM-02 The seven strokes and their harmonic content
- claim: seven named strokes (dheem, chappu, nam, araichappu, dhi, ta, thom, gumki) are each a distinct
  strike, with measured FFT spectra showing genuinely different harmonic content: dheem excites a
  fundamental shifted about 7 percent sharp of the rest of the harmonic series; chappu excites the
  second harmonic and is used to tune the drum to the soloist's Sa; nam excites the third harmonic at the
  membrane's edge; araichappu, unique to the mridangam with no tabla equivalent, is a sharper-timbred
  third-harmonic stroke at the upper-octave Sa; dhi and ta are closed strokes, the former still
  measurably harmonic, the latter not; thom is the open bass stroke, tuned via temporary paste loading;
  gumki modulates thom's harmonicity.
- source: KUMAR-REVIEW-2023 (section)
- source_type: academic acoustics
- confidence: medium
- scope: strokes as played and recorded by one named senior performer (Sivaraman) for one specific
  spectral-analysis study (the review's dedicated seven-strokes chapter); presented in the source as
  representative of standard mridangam technique, not explicitly scoped to a named lineage or school
- limitations: this is a single-performer, studio-recorded dataset per the source's own account (chosen
  specifically to minimise background noise and performer-to-performer variation), not a survey across
  players; the review does not state whether other senior performers' strokes were compared for
  consistency.
- inference: the guide page's claim that these seven stroke names function like tabla bols (a named,
  physically distinct vocabulary rather than a velocity-graded set) is this page's own framing, though
  it follows directly from the source's own point that the strokes are "measurably" distinct by FFT
  rather than merely conventionally named.
- tradition_scope: Carnatic mridangam technique as demonstrated by one senior performer (Umayalpuram K
  Sivaraman); not scoped further by school or region in the source.

### MRIDANGAM-03 Kucchi versus thool: a real construction fork, not a defect
- claim: the annular space between the valanthalai's main membrane and its outer disc is filled either
  with radial reed/pine strips (kucchi) or with black-patch material (thool), a player/lineage
  preference; FFT comparison shows dheem and nam more prominent on thool-filled drums and chappu and
  araichappu more prominent on kucchi-filled drums, because the two fillings suppress different mode
  shapes (nodal-circle modes versus nodal-diameter modes respectively).
- source: KUMAR-REVIEW-2023 (section, the dedicated kucchi-vs-thool subsection)
- source_type: academic acoustics
- confidence: medium
- scope: general Carnatic practice; the source names specific senior performers associated with each
  choice (Sivaraman and Vellore Ramabhadran with kucchi; K Mani, Raghu and T K Moorthy with thool/kappi,
  per IITM-MRIDANGAM-SLIDES's independent naming of the same split) as illustration, not as an exhaustive
  survey
- limitations: the underlying FFT comparison is again built on a limited set of recorded instruments per
  the source's own account (not a large-sample survey); the mode-suppression mechanism is presented as
  the review's own physical interpretation of the source book's findings, not independently verified
  against a separate acoustics paper this pass.
- inference: none stated as fact beyond the source's own claims; this page does not extend the
  mechanism claim beyond what is reported.
- tradition_scope: general Carnatic mridangam construction practice, with named individual performers
  attached to each choice as illustration, not as defining a school.

### MRIDANGAM-04 Ensemble role: no theka, and a shared audience/performer clap-wave reference
- claim: unlike the tabla, which alone carries responsibility for making the tala cycle legible to a
  Hindustani soloist via a fixed theka pattern, Carnatic performance distributes that responsibility
  more broadly through a conventionally established pattern of claps and waves performed by the soloist,
  the mridangam player and, commonly, much of the audience together; the mridangam accordingly has no
  theka and more latitude in what it plays during accompaniment.
- source: COURTNEY-CONTRAST (full)
- source_type: performer
- confidence: medium
- scope: general contrast between Hindustani and Carnatic percussion accompaniment practice, as stated
  by one tabla performer/scholar writing specifically to contrast the two traditions
- limitations: this is Courtney's own comparative account (a tabla specialist's outside view of Carnatic
  practice), not a Carnatic-tradition source describing its own practice from within; it is corroborated
  in its central claim (no theka on the Carnatic side) by the pre-existing sourcing already in
  `shared/MUSICAL_SYSTEMS/RAGA_AND_TALA.md`, which this page treats as the more authoritative Carnatic-
  side confirmation, but Courtney's specific claim about audience clapping carrying the reference was
  not independently cross-checked against a Carnatic-tradition source this pass.
- inference: none beyond what Courtney states, cross-checked against RAGA_AND_TALA.md's existing,
  separately sourced statement that Carnatic mridangam accompaniment is not built on a theka.
- tradition_scope: general contrast between Hindustani tabla and Carnatic mridangam accompaniment
  practice; not scoped to one Carnatic school.

### MRIDANGAM-05 Tani avartanam structure: korvai, korappu, mohra, mukthayam
- claim: the mridangam's (and other percussionists') unaccompanied solo within a kutcheri, the tani
  avartanam, is built from named forms: korvai (a composed, arithmetically resolved concluding phrase,
  often split into poorvanga and uttaranga halves and presented at a given nadai, typically repeated
  three times), korappu (a trading/linking passage used when multiple percussionists perform together),
  mohra (a short flourish) and mukthayam (a concluding cadence); karvai, a sustain or pause, is a
  separate, easily confused term.
- source: IITM-MRIDANGAM-SLIDES (full)
- source_type: tradition institution course material
- confidence: low
- scope: general Carnatic tani avartanam structure, as presented in one university course's slide deck
- limitations: this is slide-deck material (an outline for a lecture, not a full prose treatment), so
  each term is given only a short gloss rather than a worked example or a fuller account of how the
  forms combine in an actual performance; no cross-check against a second, independent source
  (comparable to how Courtney's cyclic/cadential account for tabla was corroborated by Chordia's
  separate essay) was found for this specific claim this pass. Confidence is rated low for this reason,
  even though the individual term glosses are plausible and internally consistent with the mridangam
  review's separate, better-sourced material.
- inference: the guide page's observation that mohra/mohara are cognate-sounding terms across the tabla
  and mridangam pages is this page's own noticing, not a claim either source makes about the other
  tradition.
- tradition_scope: general Carnatic practice; not attributed to a named school or teacher in the
  source.

## Corrections to the 2.0 page

This is a new page for 2.1; there was no 2.0 `MRIDANGAM.md` in the guide (the instrument was listed in
`HAND_PERCUSSION.md`'s routing table as "page in preparation in 2.1"). There is accordingly no prior
page's claims to correct. As with `shared/VIRTUAL_INSTRUMENT_GUIDE/TABLA.md`, the correction this page makes is to a hypothetical
naive treatment: it explicitly states that Carnatic mridangam accompaniment is not built on a theka,
agreeing with (not contradicting) `shared/MUSICAL_SYSTEMS/RAGA_AND_TALA.md`'s existing framing that sam,
khali and theka are Hindustani terms.

## Still to verify

- A dynamics-focused acoustic study of mridangam strokes (how spectral balance shifts with force at a
  fixed stroke).
- Resolution of the thoppi's tuned-pitch discrepancy between "one octave below the right head's Sa"
  (IITM-MRIDANGAM-PARTS) and "Pa of the lower octave" (KUMAR-REVIEW-2023) — these are different claims
  and neither source was cross-checked against the other on this specific point.
- A technique-focused source on the physical mechanism of gumki (comparable to what Kapur et al. 2002
  supplied for the tabla's bāyāṅ bend).
- A technique-focused source on hand alternation in fast nadai figuration.
- A source specifically addressing konnakol/sollukattu as a vocalised performance practice distinct
  from stroke naming; this page deliberately did not claim konnakol as documented on the strength of the
  sources read this pass, which only establish that mridangam strokes carry mnemonic syllable names.
- A recording-engineering source on conventional mridangam miking.
- A source giving the composed/improvised balance specifically within a tani avartanam.
- A dedicated ethnomusicological monograph on Carnatic mridangam technique, lineage or pedagogy,
  comparable to Kippen's tabla study; none was identified or opened this pass, and finding one would be
  the highest-value single addition to this page's sourcing.
- Direct confirmation from a tradition bearer or teacher on whether any mridangam repertoire is
  restricted, ceremonial or lineage-held; this pass found nothing either way and did not seek it
  directly.
