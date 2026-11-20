# Provenance and licences

Where every number in this knowledge library comes from, under what licence, and what may ship. Generated on 2026-11-18 from the corpus inventory (Faderhand's corpus inventory script).

**Nothing in this skill contains a downloaded MIDI file, a transcription of one, or a per-file pattern.** It ships aggregate measurements (medians, ranges, counts, average position histograms) and guidance written from them. The examples in `GENERATION_RULES.md` are original.

## Sources

| Source | Where it came from | Licence | Files downloaded | Status for learning | Analysed (train / held out) |
|---|---|---|---|---|---|
| Groove MIDI Dataset v1.0.0 | magenta.tensorflow.org/datasets/groove (MIDI-only zip) | CC BY 4.0, Google LLC | 1150 | approved | 1017 / 128 (the dataset's own test split) |
| Mutopia Project, curated selection | mutopiaproject.org, one page per piece | Public Domain, CC BY 3.0/4.0, CC BY-SA 2.5–4.0 (per piece, below) | 163 MIDI files from 60 pieces | approved | 136 / 14 |
| PDMX (Zenodo record 15571083), MIDI archive | zenodo.org | dataset CC BY 4.0; each score Public Domain mark or CC0 per MuseScore metadata | 254077 listed, 254035 present | approved: 43154; excluded: 31221 licence conflict, 145502 PDMX duplicates, 34200 pop/rock/hip-hop/jazz/soundtrack/untagged arrangements that may copy copyrighted songs | 3805 / 195 (a 4,000-file sample of the approved set) |
| Zynthion free MIDI packs (13 packs) | zynthion.com/free/*, email-gated download link | Zynthion licence: royalty-free use in your own music; no reselling or redistributing the files | 2680 | **pending clearance**: the licence covers making music, not building software from the files. Analysed on this machine only; its numbers stay in `knowledge/local/` (gitignored) | 715 / 108 after removing FL per-drum splits, duplicates and transpositions |
| Slakh2100 | slakh.com | CC BY 4.0 | 0 | not downloaded: its MIDI ships only inside a ~105 GB audio archive, more than the free disk space | – |

Zynthion packs taken: 808 MIDI and hi-hat rolls, arp, bass, melody, drum patterns, drum fills, and the deep house, EDM, house, lo-fi, techno, trance and trap genre packs. The genre packs each include a "Chords and bass" folder; those chord parts were used only as harmonic context for the bass analysis. The chord-progression and chords-and-scales collections were not downloaded.

## Dedup and validation

| Source | Byte-identical duplicates | Same notes, different file | Transpositions of another file | Unreadable | Missing |
|---|---|---|---|---|---|
| groove | 1 | 4 | 0 | 0 | 0 |
| mutopia | 6 | 0 | 7 | 0 | 0 |
| pdmx | 41074 | 196 | 54 | 0 | 42 |
| zynthion | 387 | 329 | 1009 | 0 | 0 |

Analysis skips duplicates, same-note copies and transpositions, so one pattern in twelve keys counts once.

## Held out for evaluation

Files flagged `holdout` never feed the statistics in `stats/`: the Groove test split, about 12% of Mutopia pieces, 5% of PDMX and 15% of Zynthion patterns (by hash). They provide the reference ranges Faderhand's evaluation scorer uses.

## What may ship

- `stats/` and the guidance pages: aggregate numbers from approved sources, plus general practice.
- `local/`: Zynthion-derived numbers. **Not committed and not shipped** until Zynthion confirms that analysing its free packs for a skill is allowed. Where Faderhand's `midi_check` (when the Faderhand skill is installed) uses a trap or drill target range, the range is a rounded convention that those numbers informed; replace or confirm those ranges before a public release.
- No source file, and nothing that can rebuild one.

## Mutopia pieces used (attribution)

Typeset editions by Mutopia Project volunteers. CC BY and CC BY-SA editions require credit; this list is that credit.

| Piece | Composer | Licence | Maintainer | Why it was chosen | Page |
|---|---|---|---|---|---|
| String Quartet No.12 | A. Dvořák (1841–1904) | Public Domain | Sébastien Manen | string quartet: folk-like melody, pentatonic colour, ostinato accompaniment | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=2211 |
| Symphony No. 9 in E minor | A. Dvořák (1841–1904) | Creative Commons Attribution-ShareAlike 3.0 | Keith OHara | orchestration: Romantic symphony, brass and woodwind solos | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=1793 |
| Estate / Summer | A. Vivaldi (1678–1741) | Creative Commons Attribution-ShareAlike 3.0 | smailliw (at) gmail.com | string writing: stillness vs storm, contrast of sections | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=336 |
| L'Inverno / Winter | A. Vivaldi (1678–1741) | Creative Commons Attribution-ShareAlike 3.0 | smailliw (at) gmail.com | string writing: tremolo, pizzicato, programmatic texture | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=351 |
| Première Arabesque | C. Debussy (1862–1918) | Public Domain | Keith OHara | impressionist arpeggio textures, triplets vs duplets | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=1777 |
| Suite Bergamasque: Clair de Lune | C. Debussy (1862–1918) | Public Domain | Keith OHara | impressionist harmony and rubato texture | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=1778 |
| Keyboard Sonata in G Major | D. Scarlatti (1685–1757) | Creative Commons Attribution-ShareAlike 4.0 | Knute Snortum | keyboard figuration and repetition: Scarlatti sonata | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=2104 |
| Aase's Death from Peer Gynt Suite I | E. Grieg (1843–1907) | Public Domain | Deborah Lowrey | string quartet: dynamic swell, homophonic grief | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=247 |
| Gnossienne No. 1 | E. Satie (1866–1925) | Creative Commons Attribution-ShareAlike 4.0 | Knute Snortum | modal melody, no barlines feel, ostinato bass | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=2035 |
| Gymnopédie No. 1 | E. Satie (1866–1925) | Public Domain | Evin Robertson | sparse texture: slow waltz, extended chords, space | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=37 |
| Mazurka: Op.33, No.1 | F. F. Chopin (1810–1849) | Creative Commons Attribution 3.0 | Ryan Prince | dance accent displacement: mazurka second-beat stress | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=1682 |
| Nocturne | F. F. Chopin (1810–1849) | Creative Commons Attribution-ShareAlike 3.0 | Renato Biolcati Rinaldi | expressive melody: ornamented nocturne over wide left-hand arpeggios | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=1590 |
| Prelude: Op. 28, No. 1 | F. F. Chopin (1810–1849) | Creative Commons Attribution-ShareAlike 4.0 | Donald Axel | arpeggio figuration: Chopin prelude 1, rolling 16ths | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=411 |
| Prelude: Op. 28, No. 20 | F. F. Chopin (1810–1849) | Public Domain | Magnus Lewis-Smith | chorale-like progression, dynamics as structure | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=472 |
| Prelude: Op. 28, No. 4 ('Suffocation') | F. F. Chopin (1810–1849) | Public Domain | Magnus Lewis-Smith | harmony: chromatic voice-leading under a static melody | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=468 |
| Prelude: Op. 28, No. 6 | F. F. Chopin (1810–1849) | Public Domain | Magnus Lewis-Smith | melody in the bass, repeated-chord accompaniment | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=469 |
| Prelude: Op. 28, No. 7 | F. F. Chopin (1810–1849) | Public Domain | Magnus Lewis-Smith | short phrase form, dance rhythm | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=470 |
| Valse Op. 64, No. 1 ('Minute Waltz') | F. F. Chopin (1810–1849) | Public Domain | Magnus Lewis-Smith | perpetual motion waltz | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=483 |
| String Quartet in B-flat major | F. J. Haydn (1732–1809) | Creative Commons Attribution 4.0 | Urs Metzger | string quartet: classical balance | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=2213 |
| Auf dem Wasser zu singen | F. Schubert (1797–1828) | Public Domain | Ph. Raynaud | accompaniment figure as image (water), melody over it | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=1052 |
| Du bist die Ruh | F. Schubert (1797–1828) | Public Domain | Ph. Raynaud | slow lyrical vocal line, breath and phrase length | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=1053 |
| Erlkönig | F. Schubert (1797–1828) | Public Domain | Ph. Raynaud | accompaniment as drama: repeated-octave triplet ostinato | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=1030 |
| Waltz No. 15 | J. Brahms (1833–1897) | Public Domain | Brian D. Rude | waltz: lyrical miniature | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=794 |
| The Fairest of the Fair | J. P. Sousa (1854–1932) | Public Domain | Garrett Fitzgerald | concert band orchestration: march form | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=1643 |
| The Stars and Stripes Forever | J. P. Sousa (1854–1932) | Public Domain | Benjamin Bloomfield | march form: trio, breakstrain, stinger | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=626 |
| Canon per 3 Violini e Basso | J. Pachelbel (1653–1706) | Creative Commons Attribution 4.0 | Michael Fischer v. Mollard | ground bass: 2-bar bass under a 3-voice canon (loop-based build) | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=2047 |
| Aus meines Herzens Grunde (Chorale 1) | J. S. Bach (1685–1750) | Public Domain | Laurent Ducos | 4-part chorale voice leading | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=378 |
| BWV 1004 Chaconne | J. S. Bach (1685–1750) | Creative Commons Attribution-ShareAlike 3.0 | Hajo Dezelski | variation on a short harmonic cycle, single instrument implying harmony | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=1426 |
| Brandenburg Concerto No. 2 | J. S. Bach (1685–1750) | Public Domain | Andy Vaught | concerto texture: trumpet, flute, oboe, violin soloists | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=1680 |
| Brandenburg Concerto No. 5 (3rd Movement: Allegro) | J. S. Bach (1685–1750) | Public Domain | Joshua Koo | concerto texture: soloists vs ripieno | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=548 |
| Chromatic Fantasy and Fugue, BWV 903 (Fugue) | J. S. Bach (1685–1750) | Public Domain | Greg Louis | fugue: chromatic subject, 3 voices | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=1604 |
| Fugue in C major | J. S. Bach (1685–1750) | Public Domain | Jacob Lee | fugue: subject/answer entries | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=254 |
| Goldberg Variations - 3 | J. S. Bach (1685–1750) | Creative Commons Attribution-ShareAlike 3.0 | Hajo Dezelski | canon at the unison over a walking bass | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=1384 |
| Goldberg Variations - Aria | J. S. Bach (1685–1750) | Creative Commons Attribution-ShareAlike 3.0 | JD Erickson | variation theme: aria over a bass line | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=979 |
| Invention 1 | J. S. Bach (1685–1750) | Creative Commons Attribution-ShareAlike 3.0 | jeff covey | counterpoint: 2-part invention, motif inversion and sequence | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=40 |
| Invention 10 | J. S. Bach (1685–1750) | Public Domain | Allen Garvin | counterpoint: invention, broken-chord subject | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=62 |
| Invention 11 | J. S. Bach (1685–1750) | Public Domain | Allen Garvin | counterpoint: invention, chromatic bass | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=71 |
| Invention 4 | J. S. Bach (1685–1750) | Public Domain | Allen Garvin | counterpoint: 2-part invention in 3/8, running bass | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=67 |
| Invention 8 | J. S. Bach (1685–1750) | Public Domain | Allen Garvin | counterpoint: 2-part invention, canon at the octave | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=61 |
| Passacaglia | J. S. Bach (1685–1750) | Public Domain | Urs Metzger | ground bass: passacaglia, 8-bar ostinato variations | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=741 |
| Suite 1 for Cello Solo | J. S. Bach (1685–1750) | Public Domain | Andreas Scherer | bass as melody: solo cello suite, implied harmony | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=517 |
| Suite No. 3 in C Major | J. S. Bach (1685–1750) | Public Domain | Stelios Samelis | bass as melody: solo cello suite in C | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=890 |
| Toccata and Fugue in D Minor | J. S. Bach (1685–1750) | Public Domain | Anonymous | organ toccata: gesture, pedal point, dramatic rests | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=1780 |
| Trio Sonata V in C major BWV 529 | J. S. Bach (1685–1750) | Public Domain | Urs Metzger | trio texture: three independent lines (organ trio sonata) | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=703 |
| Overture to Egmont | L. V. Beethoven (1770–1827) | Public Domain | Stelios Samelis | orchestral contrast: slow intro to allegro | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=547 |
| Quartet No. 4 in C Minor: 1. Allegro ma non tanto | L. V. Beethoven (1770–1827) | Public Domain | Stelios Samelis | string quartet: melody/accompaniment trading | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=790 |
| Quartet No. 4 in C Minor: 2. Andante scherzoso quasi allegretto | L. V. Beethoven (1770–1827) | Public Domain | Stelios Samelis | string quartet: fugato scherzo, imitative entries | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=791 |
| Symphony No. 5 - Opus 67 (1st Movement) | L. V. Beethoven (1770–1827) | Public Domain | Stelios Samelis (adapted to 2.16.2 by Johannes Heinecke) | motivic development: 4-note motif through a whole movement | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=941 |
| Symphony No. 7 in A Major (2nd Movement: Allegretto) | L. V. Beethoven (1770–1827) | Public Domain | Stelios Samelis | orchestral build over an ostinato rhythm (layer-by-layer arrangement) | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=595 |
| Etude 1 | M. Carcassi (1792–1853) | Public Domain | Jeff Covey | arpeggio figuration: guitar etude | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=13 |
| Preludes in Progressive Keys from Méthode complète pour Guitare | M. Carcassi (1792–1853) | Public Domain | Jeffrey Olson | arpeggio figuration in progressive keys | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=2209 |
| Bethena | S. Joplin (1868–1917) | Public Domain | Magnus Lewis-Smith | syncopation in 3/4: ragtime waltz | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=463 |
| Elite Syncopations | S. Joplin (1868–1917) | Public Domain | Benjamin Bloomfield | syncopation: ragtime with displaced accents | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=1540 |
| Magnetic Rag | S. Joplin (1868–1917) | Public Domain | Kurt Holtrop | syncopation: late rag, minor section contrast | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=441 |
| Maple Leaf Rag | S. Joplin (1868–1917) | Public Domain | Chris Sawer | syncopation: ragtime right hand against steady stride bass | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=23 |
| The Entertainer | S. Joplin (1868–1917) | Public Domain | Chris Sawer | syncopation: ragtime, call and answer | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=263 |
| Fugue in G Minor KV 401/375e | W. A. Mozart (1756–1791) | Public Domain | Maurizio Tomasi | fugue: Mozart's classical fugue | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=423 |
| Masonic Funeral Music KV 477 | W. A. Mozart (1756–1791) | Public Domain | Maurizio Tomasi | dark wind orchestration, slow harmonic rhythm | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=448 |
| Piano Quartet KV 478 | W. A. Mozart (1756–1791) | Public Domain | Maurizio Tomasi | piano quartet: piano vs strings interplay | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=499 |
| Symphony No. 25 - KV183 (1st Movement) | W. A. Mozart (1756–1791) | Public Domain | Stelios Samelis | syncopated strings, minor-key drive | https://www.mutopiaproject.org/cgibin/piece-info.cgi?id=1380 |

## Citations

- Jon Gillick, Adam Roberts, Jesse Engel, Douglas Eck, David Bamman. *Learning to Groove with Inverse Sequence Transformations.* ICML 2019. Groove MIDI Dataset, CC BY 4.0.
- Phillip Long, Zachary Novack, Taylor Berg-Kirkpatrick, Julian McAuley. *PDMX: A Large-Scale Public Domain MusicXML Dataset for Symbolic Music Processing.* Zenodo record 15571083, CC BY 4.0.
- The Mutopia Project, https://www.mutopiaproject.org/ (licences per piece, above).
