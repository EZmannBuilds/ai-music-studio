# Choir and Voice: research records

What was read, what was not, and the limits of each claim the guide page makes. The page carries
the conclusions; this file carries the evidence.

## Scope and method

No manufacturer manual for a virtual/sampled vocal instrument was found and opened at a depth that
would support `manual-derived`, so the page's `virtual_programming` rows are `inference`, following
the general control-model grammar documented for other instruments in this pack rather than a
voice-specific reading. Voice-science claims were pursued through the National Center for Voice and
Speech's open tutorials, a UNSW/JASA peer-reviewed paper on soprano resonance, and a KTH peer-reviewed
overview of choir acoustics research read in full. Two secondary pedagogy pages (Voice Science's
belting and vibrato-rate lexicon entries) were read in full; both cite and summarise primary
peer-reviewed studies (Estill; Schutte and Miller; Bestebreurtje and Schutte; Prame 1994; Nix et al.
2016; Glasner and Johnson 2022) that were not themselves opened, so those primary studies are recorded
as `standard-reference`-adjacent attributions carried through a source that was itself read directly,
not as `academic` claims in their own right. A passaggio-pedagogy page and a choral-diction pedagogy
page were each read in full. Sundberg's *The Science of the Singing Voice* and Adler's *The Study of
Orchestration* were not opened and are cited only as `standard-reference`.

## Records

### CHOIR-01 Register mechanics: chest, head, falsetto, and belt/mix
- claim: chest voice is thyroarytenoid-dominant with most fold tissue vibrating; head voice is
  cricothyroid-leaning with mainly the cover layers vibrating; falsetto is cricothyroid-only with
  minimal tissue in vibration; contemporary belt/mix blends both systems and is commonly defined by a
  closed quotient above roughly 50-52 percent.
- source: NCVS-REGISTERS (section); VOICESCIENCE-BELTING (full)
- source_type: pedagogy
- confidence: medium
- scope: general voice-science description of laryngeal mechanism, applicable across voice types;
  the closed-quotient threshold for belt is drawn from cited perceptual-identification studies
  (Schutte and Miller 1993; Bestebreurtje and Schutte 2000) that were not opened directly.
- limitations: NCVS's own tutorial does not address mix/belt; that material comes only from the
  second source. Neither source is a peer-reviewed acoustics paper in its own right; both are
  pedagogy/science-communication pages that cite primary literature.
- inference: none for the mechanism description; the closed-quotient number is carried at the
  confidence of the secondary source that reported it.

### CHOIR-02 Soprano formant tuning and vowel intelligibility at high pitch
- claim: as a soprano's fundamental frequency rises above its speech-range value, she raises her
  first vocal-tract resonance to track it; this causes vowel formant positions to converge and
  overlap across different vowels at high pitch, which is measured to reduce vowel distinguishability
  and is why high soprano text is hard to understand.
- source: JOLIVEAU-SOPRANO (section)
- source_type: academic acoustics
- confidence: high
- scope: nine trained sopranos (five professional, four student), Western classical singing style,
  measured on sustained soft vowels at a range of pitches.
- limitations: only the abstract and introduction were read, not the full results section with
  numeric formant-frequency data; the page states the qualitative mechanism and its consequence for
  intelligibility without quoting specific formant frequencies.
- inference: none for the mechanism; applying "vowel intelligibility falls at high pitch" to sampled
  or synthesised vocal instruments as a fake-sounding-error tell is this page's own extension.

### CHOIR-03 Choir acoustics: pitch dispersion, blend, spacing, self-to-other balance, solo-vs-choral production
- claim: listeners tolerate roughly plus-or-minus 14 cents of pitch standard deviation across a
  unison section before it reads as out of tune, though a preference for zero scatter is common when
  given the choice; sung major thirds in ensemble average around 395 cents, between just (386) and
  equal-tempered (400) intonation; blend depends on matched vowel formants and reduced individual
  vibrato; trained singers measurably reduce singer's-formant emphasis and vibrato extent when
  singing in choral mode compared with solo mode, while untrained singers can instead brighten under
  ensemble conditions; singers monitor a self-to-other loudness ratio that varies with choir position
  (roughly +1 to +8 dB) and prefer it higher (+6 dB on average) than typical measured conditions
  provide (+3 to +4 dB); singers and listeners both tend to prefer wider spacing between choir
  singers than close conventional formation; individually measured choir-singer dynamic range runs
  roughly 11-33 dB SPL, with trained singers distinguished mainly by their ability to sing more
  softly.
- source: TERNSTROM-CHOIR-2002 (full)
- source_type: academic acoustics
- confidence: high
- scope: a peer-reviewed overview compiling many individual choir-acoustics studies (Ternstrom's own
  KTH research programme plus others it cites: Daugherty, Rossing et al., Coleman, Nordmark and
  Ternstrom, and more), predominantly Western classical/concert choral singing.
- limitations: this is a review article; several of the specific figures (14 cents, +6 dB preferred
  SOR, 11-33 dB dynamic range, 395-cent thirds) are each drawn from one underlying study cited within
  it, not independently re-verified here, and the review itself flags some of the underlying work
  (e.g. a soloistic-versus-choral listening test using an anechoic recording) as methodologically
  imperfect. Figures should be read as typical findings from specific studies of specific choirs, not
  universal constants.
- inference: applying "vibrato reduced in choral mode" and "formant scatter reads as a blend problem"
  to programming guidance for a virtual instrument is this page's own extension of the research
  findings.

### CHOIR-04 Vibrato rate and extent in trained singers
- claim: measured vibrato rates in trained singers cluster in roughly the 4.6-6.0 Hz range across
  several studies (a large normative study of college vocal majors averaging about 5.0-5.2 Hz; ten
  professional singers averaging 6.0 Hz with about a 15 percent increase at phrase endings; twenty
  professional opera singers averaging 5.3 Hz); vibrato extent is not given a single settled figure
  by this source but is described as somewhat larger in solo than choral singing.
- source: VOICESCIENCE-VIBRATO (full)
- source_type: pedagogy
- confidence: medium
- scope: trained Western classical singers, predominantly college-level and professional opera
  singers, across several independent studies (Nix et al. 2016; Prame 1994; Glasner and Johnson
  2022), none of which were opened directly.
- limitations: the primary studies were not opened; the figures are carried at the confidence of a
  secondary pedagogy page that summarises them, and the page notes it found no explicit numeric
  extent-in-cents figure to report. No claim is made on the guide page about popular-music vibrato
  rates, which were not covered by this source.
- inference: none for the reported figures; noting that "vibrato reduced in choral mode" corroborates
  and combines with TERNSTROM-CHOIR-2002's independent finding is this page's synthesis.

### CHOIR-05 Passaggio location, especially for female voices
- claim: the female primo passaggio sits low in the overall vocal range rather than in its "upper
  third": commonly cited around Eb4 for soprano, roughly E4/F4 for mezzo-soprano, and G4 for
  contralto, with lighter voices' passaggio sitting lower because their middle register extends
  further down, and heavier voices' passaggio sitting higher because of a larger chest-voice range.
- source: HANSON-PASSAGGIO (full)
- source_type: pedagogy
- confidence: medium
- scope: classical female voice pedagogy (soprano, mezzo-soprano, contralto); the source also gives
  rough male chest-voice ceilings by voice type but does not name a single "primo passaggio" pitch
  for male voices as precisely as for female voices.
- limitations: a single pedagogy author's stated positions, not a peer-reviewed acoustic measurement;
  individual passaggio location varies by singer, and the source itself notes vowel choice shifts the
  perceived location.
- inference: none for the specific pitches; generalising "female passaggio sits low in the range" as
  a correction to a flat "upper third of the range" claim is this page's synthesis of the source.

### CHOIR-06 Choral consonant handling
- claim: consonants define a choir's rhythm; a consonant ending one syllable is commonly attached to
  the beginning of the next syllable across a word boundary; sibilants are deliberately shortened and
  softened in performance so a section's collective "s" sound does not dominate the texture.
- source: CHORAEGUS-DICTION (full)
- source_type: pedagogy
- confidence: medium
- scope: general choral diction practice as taught in one choral-pedagogy resource; broadly
  consistent with standard choral-conducting pedagogy but not cross-checked against a second
  independent choral-diction source in this pass.
- limitations: a single web pedagogy source; it does not give numeric lead-time values for any
  consonant type, and its "attach the consonant to the next syllable" rule is a different concern
  from the pre-beat lead-time question the 2.0 page's claim was about (see corrections below).
- inference: none for the direct claims; the connection to the "sibilants need the longest lead
  time" correction is `inference`, reasoned from general phonetics (a fricative/sibilant is a
  continuant that needs duration to be identified; a plosive's release is a brief transient), not
  read from this or any other source at section depth.

### CHOIR-07 Choral and solo vocal ranges (standard-reference)
- claim: typical SATB ranges and comfortable tessiturae as given in the range table.
- source: ADLER-1989 (not-read)
- source_type: standard reference
- confidence: low
- scope: widely used pedagogical figures for choral ranges in Western choral/orchestral writing.
- limitations: not opened for this work; carried at the pack's `standard-reference` label because it
  is the kind of range table this text is widely known to provide, matching the figures already on
  the 2.0 page, which were also attributed to Adler without being opened.
- inference: the popular-music voice-category ranges added to the table (mix/belt ranges for
  contemporary female and male voices) are this page's own `inference`, not drawn from Adler or any
  other source opened for this work.

## Corrections to the 2.0 page

- **Passaggio location.** The 2.0 page said passaggi sit "roughly around the upper third of each
  voice's range." This is corrected, especially for female voices: the primo passaggio commonly sits
  low in the range (around Eb4-F4 for soprano/mezzo), not in the upper third, because it marks the
  chest-to-middle transition rather than a point near the top of the range. `sourced: HANSON-PASSAGGIO`
- **Consonant lead time by type.** The 2.0 page said anticipation is "10 to 60 milliseconds, longer
  for a plosive or a cluster." This is corrected: a plosive's burst is a brief transient, while
  sibilants, fricatives and clusters are continuants that need real duration to be heard as
  themselves, so it is those sounds that typically need the longest lead, not plosives. `inference`,
  since no source read at section depth gives a direct singing-specific ranking; the correction rests
  on general phonetic reasoning about consonant duration, which the page states plainly rather than
  overclaiming as measured.
- **Dynamics and diction at the top of the range.** The 2.0 page said to "reduce diction and increase
  the dynamic as the line goes high; the real voice has no choice." This is corrected: real voices
  have head voice, falsetto, and messa di voce (a controlled swell and decrease) as options at the
  top of the range, so "no choice" overstates the case; what is true, and kept, is that vowel
  intelligibility genuinely falls as pitch rises past the first vocal-tract resonance.
  `academic: JOLIVEAU-SOPRANO` for the intelligibility mechanism; `inference` for the corrected framing.
- **Unison instrumental doubling.** The 2.0 page said doubling a choral line with an instrument at
  the unison "removes the voice's identity." This is corrected to note that how rigidly the doubling
  follows the voice matters: a mechanical unison doubling can fuse and reduce identity, but a
  colla-parte doubling that follows the vocal line's own phrasing is a standard supportive technique,
  not one that erases the voice by definition. `inference`
- **Vibrato onset.** The 2.0 page said vibrato "develops across a note rather than starting with it."
  This is corrected to a style- and singer-dependent choice, consistent with the same correction made
  on `STRINGS.md`, rather than one fixed onset behaviour for every note. `academic: TERNSTROM-CHOIR-2002`
  for the solo-versus-choral vibrato-extent contrast that supports treating vibrato as variable.

## Still to verify

- Numeric consonant-anticipation lead times by consonant type in a dedicated phonetics-of-singing
  source (Sundberg, or a peer-reviewed diction/intelligibility study). Not found at section depth for
  this work; the ordering correction is reasoned, not measured.
- Formant-frequency and passaggio-physiology detail generally, against Sundberg, *The Science of the
  Singing Voice*. Not opened for this work.
- Full choral range and tessitura conventions against Adler, *The Study of Orchestration*. Not opened.
- Whether the belt closed-quotient threshold (50-52 percent) and formant-tuning strategy generalise
  outside Western contemporary commercial music pedagogy. Only Western CCM/musical-theatre pedagogy
  sources were read for this work.
