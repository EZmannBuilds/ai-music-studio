# Hardanger fiddle: research records

What was read, what was not, and the limits of each claim the guide page makes. The page carries
the conclusions; this file carries the evidence.

## Scope and method

Four sources were read at section depth or more: the Hardanger Fiddle Association of America
(HFAA) hosts David Golber's 1993 American Lutherie article "What You Should Know About the
Hardanger Fiddle" (read in full) and Karin Loberg Code's tuning-name compendium (only its
introductory description of method and sources came through the fetch; the table itself did not
render as plain text, so it is used at `excerpt` depth only, for one weak claim). A peer-reviewed
Transactions of ISMIR dataset paper (Lartillot, Johansson, Elowsson, Monstad and Cyvin, 2023) was
read at section depth for its instrument description and in full for its timing-analysis sections.
Mats Johansson's 2017 critical review in Studia Musicologica Norvegica was read in full.

Two further attempts failed and contribute nothing: a page on Scandinavian dance-music timing was
blocked by an anti-scraper challenge page (Anubis), and a Hardanger fiddle acoustics paper on
ResearchGate returned an access-restricted page. Neither is in the source register, since neither
was actually read; both are noted here so the next pass does not have to rediscover the dead end.

`shared/MUSICAL_SYSTEMS/MODAL_FOLK_SYSTEMS.md` flags that its inherited intonation claim
("conditioned by melodic formulas, local tonal centers... and string resonance") may have been
misattributed to the TISMIR dataset paper when the real source is a different 2019 paper. Having now
read the TISMIR paper directly (section 2.1), **that exact claim, in close to that wording, is
present in the TISMIR paper itself** ("pitch intonations are conditioned by shifting contextual
factors, including melodic formulas, local tonal centers (which often equal the open strings) and
string resonance"). This does not rule out the 2019 paper also making the claim, which remains
unread, but it does mean the TISMIR citation for this specific sentence is not the misattribution
the shared file worried it might be. This is a finding for whoever next edits that file; this
research file does not edit it.

## Records

### HF-01 Construction: four bowed strings, four or five sympathetic understrings, flat bridge and fingerboard
- claim: the instrument has four playing (bowed) strings and four or five sympathetic understrings
  running beneath the fingerboard; the bridge and fingerboard are flatter than a violin's, which is
  what lets double stops be played continuously rather than as an occasional device.
- source: HFAA-GOLBER-1993 (full); TISMIR-LARTILLOT-2023 (section)
- source_type: tradition institution; ethnomusicology
- confidence: high
- scope: Hardanger fiddle construction generally, as described by a luthier writing for the HFAA and
  by the TISMIR dataset's instrument-description section.
- limitations: Golber notes real variation between instruments (four vs. five understrings, older
  vs. modern body outlines, west-coast vs. inland regional preferences in fingerboard roundness and
  bridge shape); neither source gives a single fixed geometry as "the" Hardanger fiddle.
- inference: none for the count of strings; the framing of "this is what enables constant double
  stops as idiom rather than device" restates TISMIR's own framing.
- tradition_scope: Norwegian Hardanger fiddle tradition generally; Golber additionally distinguishes
  west-coast from inland-region practice for fingerboard and bridge shape specifically.

### HF-02 Tuning: A-D-A-E is the predominant tuning, with many further scordatura per piece
- claim: the large majority of Hardanger fiddle tunes use A-D-A-E tuning (about three quarters of the
  repertoire, per Golber); a large number of further named tunings exist, one per piece or small
  group of pieces, and pitch level itself is not fixed (Golber gives the "A" string as ranging from
  about B-flat to C-sharp depending on player preference and instrument).
- source: HFAA-GOLBER-1993 (full); TISMIR-LARTILLOT-2023 (section); KODE-HFAA-TUNINGS (excerpt)
- source_type: tradition institution; ethnomusicology; tradition institution
- confidence: medium
- scope: general Hardanger fiddle repertoire, per two independent tradition-adjacent sources
  agreeing on A-D-A-E as dominant.
- limitations: the exact fraction ("about three quarters") is Golber's own estimate, not a count from
  a corpus. The tuning-name compendium (Karin Loberg Code) is real and evidently extensive -- its own
  introduction lists four separate printed sources it compiled from -- but the actual list of tuning
  names did not come through this pass's fetch, so "many further scordatura" is supported only at
  excerpt depth, i.e. it is standard-reference strength, not sourced strength, for the existence of
  the list; the A-D-A-E dominance claim itself is independently corroborated by TISMIR and does reach
  section depth.
- inference: none.
- tradition_scope: general; Golber notes the tradition is solo music, so "universal agreement on
  pitch is unnecessary" -- pitch level is a per-player, per-instrument decision, not a fixed standard.

### HF-03 Intonation is conditioned by melodic formula, local tonal centre and string resonance, not by a fixed scale
- claim: pitch intonation in Hardanger fiddle music is not derived from a fixed scale or chord
  structure; it is conditioned by shifting contextual factors including melodic formulas, local tonal
  centres (which often coincide with the open strings) and string resonance, and is characterised by
  great variability.
- source: TISMIR-LARTILLOT-2023 (section)
- source_type: ethnomusicology
- confidence: medium
- scope: this is the TISMIR paper's own characterisation of the genre, stated in its instrument
  background section, not a finding the paper sets out to measure and report with its own new data.
- limitations: it is one paper's summary claim rather than a dedicated intonation study; the paper
  itself does not report cent-level measurements of specific intervals against specific references,
  so no cents table can be built from it. `shared/MUSICAL_SYSTEMS/MODAL_FOLK_SYSTEMS.md` names a
  further, more intonation-specific 2019 paper as possibly the better source for this claim; that
  paper was not read in this pass.
- inference: none.
- tradition_scope: general, as stated by the TISMIR paper about the genre it studies; not attributed
  to a named school or player.

### HF-04 Springar has genuinely asymmetric beat cycles, and which position is long is style-specific
- claim: springar tunes (one of the two main dance-tune families, alongside duple-metre
  gangar/rull/halling) are organised in an asymmetric triple metre in which the three beats of a
  measure have systematically different durations, not a rubato deviation from an even triple metre.
  Different regional sub-styles place the long beat differently: in Tele-springar the dancers' downbeat
  (and the long beat) falls together; in Halling-springar the downbeat falls on the short beat. One
  measured example (a professional fiddler's recordings, the "P" performer in the TISMIR dataset,
  across several tunes) gives mean beat durations, by position in the bar, of 399 ms (first), 489 ms
  (second) and 512 ms (third) -- roughly a 1 : 1.2 : 1.3 ratio -- with a mean bar duration of about
  1.4 seconds and beat-to-beat standard deviations of 50-70 ms. A separate strand of older measurement
  work reviewed by Johansson (Groven's analysis of the Tele-springar tune Markensmondagen as played by
  three named fiddlers) gives ratios in the region of 39:33:28 and 34.5:34.4:31 for two of those
  performances.
- source: TISMIR-LARTILLOT-2023, its timing-analysis sections; JOHANSSON-2017
- source_type: ethnomusicology; ethnomusicology
- confidence: medium
- scope: the mechanism (asymmetric triple metre, tied to dance movement rather than to melodic
  accent) is described generally for the springar family, citing Blom 1981 within TISMIR. The actual
  numbers are each one measured instance: one performer across several tunes in TISMIR; named,
  individually identified fiddlers' recordings in the older studies Johansson reviews.
- limitations: **no general "the" ratio exists for springar.** TISMIR's own numbers are from a single
  professional player; Johansson's review is explicit that measured ratios vary by tune, player,
  region and even by methodology (aural estimation versus instrumented measurement), and that this
  variability is itself an open research question, not settled fact. Johansson's paper is a critical
  review of the literature's methodological problems, not a fresh measurement.
- inference: describing this to a Performance Director as "not syncopation, but genuinely unequal
  beats" follows TISMIR's own framing directly, not an inference beyond it.
- tradition_scope: springar generally for the mechanism; Tele-springar and Halling-springar by name
  for the downbeat-placement contrast; the specific ratios are scoped to the named performer(s) in
  each case, not to the sub-style as a whole.

### HF-05 Overall tempo is stable across a tune even though beat duration is not
- claim: across a set of springar performances by one professional player, bar duration is relatively
  stable (mean about 1.4 s, standard deviation about 96 ms) even though beat duration within the bar
  is highly variable (overall standard deviation about 80 ms against a mean beat of 466 ms, more than
  22% mean absolute difference between successive beats).
- source: TISMIR-LARTILLOT-2023
- source_type: ethnomusicology
- confidence: medium
- scope: one performer ("P"), several tunes, in the TISMIR dataset.
- limitations: single-performer measurement; not claimed by the source to generalise to other
  players or styles.
- inference: none.
- tradition_scope: this performer's playing of the tunes in the TISMIR dataset, unnamed player and
  school beyond "a professional musician."

### HF-06 Playing position, action and regional technique differences
- claim: the instrument is traditionally played only in first position (the highest fingered note is
  approximately at the edge of the body); string action is lower than a violin's; and there is a real
  regional split in playing style and instrument setup between west-coast Norway (less use of double
  stops, a more rounded fingerboard and bridge preferred) and the inland regions (heavier, more
  continuous double-stop use, flatter fingerboard and bridge).
- source: HFAA-GOLBER-1993 (full)
- source_type: tradition institution
- confidence: high
- scope: general Hardanger fiddle setup and playing convention, from a luthier's article hosted by
  the HFAA.
- limitations: one author's account, aimed at instrument repair and adjustment rather than
  performance pedagogy as such; it does not itself name individual players or schools within each
  region.
- inference: none.
- tradition_scope: Golber names the split explicitly as "west coast" versus "inland regions" practice.

## Corrections to the 2.0 page

No 2.0 `HARDANGER_FIDDLE.md` page exists in the guide; this is a new page, so there is nothing on
this specific instrument to correct. Two claims already present elsewhere in the pack were checked
against what this pass actually read, rather than corrected:

- `shared/MUSICAL_SYSTEMS/MODAL_FOLK_SYSTEMS.md` treats the TISMIR paper's attribution for the
  intonation claim as uncertain and names a 2019 Folk Music Analysis paper as the likelier source.
  Having read TISMIR directly, the claim (in close to the same words) is genuinely present in TISMIR
  section 2.1, so the TISMIR attribution is not wrong, even if the 2019 paper independently makes a
  related or more detailed claim. See "Scope and method" above.

## Still to verify

- The exact scordatura list beyond A-D-A-E (names, which pieces use which tuning, how many are in
  active use versus historical): the HFAA's own compendium by Karin Loberg Code exists and was
  reached, but its table did not extract as text in this pass. Re-fetching it, or reading a rendered
  copy, would settle this.
- Whether the 2019 Folk Music Analysis paper on Hardanger fiddle intonation measurement
  (`shared/MUSICAL_SYSTEMS/MODAL_FOLK_SYSTEMS.md`'s alternative attribution) adds cents-level detail
  beyond what TISMIR states in prose. Not opened this pass.
- Sympathetic-string count as four versus five: Golber says "four or five"; TISMIR says "five." Which
  is more common, and whether it is a maker-era or regional difference, is unresolved.
- Scordatura and fingering practice specific to named contemporary players or teaching lineages
  (a gharana-equivalent for this tradition): not reached in this pass. The page's ornament and
  ensemble sections are accordingly thinner than the construction and timing sections.
