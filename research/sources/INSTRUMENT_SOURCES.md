# Instrument source register

Every source the instrument pages cite, listed once. A guide page cites a source by its ID; this
register says what the source is and, above all, **how much of it was actually read** for this
pack. The label a claim may carry depends on that (`shared/RESEARCH_RULES.md`): `sourced`,
`academic` and `manual-derived` need `section` or `full`; anything read less is
`standard-reference` at best. `tools/evidence_check.py` holds every page to this table.

| Read depth | Means |
|---|---|
| `full` | the whole work, or the whole of a short work, was read |
| `section` | the part that supports the claim was read |
| `excerpt` | a preview, snippet or quotation elsewhere; not the work itself |
| `abstract` | only the abstract or summary |
| `not-read` | cited by attribution only |

Product names are allowed here, because a manual is a product's manual. They are not allowed in the
guide pages.

A source that could not be reached when it was tried stays in the register with `not-read`, so the
next person knows it was tried. Accessed dates are the date of reading.

## Sources

| id | citation | type | read | url | accessed |
|---|---|---|---|---|---|
| ADLER-1989 | Samuel Adler, The Study of Orchestration | standard reference | not-read | none | 2026-09-15 |
| ADLER-ORCH | Samuel Adler, The Study of Orchestration | standard reference | not-read | none | 2026-09-15 |
| BAVU-TORSIONAL | Eric Bavu, John Smith and Joe Wolfe, "Torsional waves in a bowed string", Music Acoustics, UNSW Sydney | academic acoustics | abstract | https://www.phys.unsw.edu.au/~jw/reprints/Bavuetal.pdf | 2026-09-15 |
| BERLIOZ-STRAUSS-TREATISE | Hector Berlioz and Richard Strauss, Treatise on Instrumentation | standard reference | not-read | none | 2026-09-15 |
| BRASSPED-PALNI | "Advanced Techniques", in Brass Techniques and Pedagogy, PALNI Pressbooks (open course text) | pedagogy | section | https://pressbooks.palni.org/brasstechniquesandpedagogy/chapter/advanced-techniques/ | 2026-09-15 |
| CHORAEGUS-DICTION | "Choral Diction", Choraegus | pedagogy | full | https://www.choraegus.com/learn/choral-diction/ | 2026-09-15 |
| COREY-RESONANCE | Corey (violin teacher), "Sympathetic Resonance - Violin Magic!", CoreyViolin.com | performer | full | https://coreyviolin.com/2023/04/21/sympathetic-resonance/ | 2026-09-15 |
| FLETCHER-ROSSING-1998 | Neville H. Fletcher and Thomas D. Rossing, The Physics of Musical Instruments, 2nd ed. | standard reference | not-read | none | 2026-09-15 |
| FORSYTH-1914 | Cecil Forsyth, Orchestration (1914), Cornell University Library copy | orchestration | section | https://archive.org/details/cu31924022381440 | 2026-09-15 |
| HANSON-PASSAGGIO | Lloyd W. Hanson, "Female and Male Primo Passaggio" | pedagogy | full | https://lloydwhanson.com/voice-passaggio/female-and-male-primo-passaggio/ | 2026-09-15 |
| HIRSCHBERG-1996 | A. Hirschberg, J. Gilbert, R. Msallam and A. P. J. Wijnands, "Shock waves in trombones", Journal of the Acoustical Society of America 99(3), 1754-1758 (1996) | academic acoustics | section | https://doi.org/10.1121/1.414698 | 2026-09-15 |
| HORNMATTERS-STOPVALVE | John Ericson, "The Stopping Valve: The Best Invention Ever", Horn Matters | pedagogy | section | https://www.hornmatters.com/2009/11/the-stopping-valve-the-best-invention-ever/ | 2026-09-15 |
| JOLIVEAU-SOPRANO | Elodie Joliveau, John Smith and Joe Wolfe, "Vocal tract resonances in singing: The soprano voice", Journal of the Acoustical Society of America 116(4), 2004 | academic acoustics | section | https://www.phys.unsw.edu.au/~jw/reprints/Joliveauetal.pdf | 2026-09-15 |
| MODERNTRUMPET-GLISS | Nathan Plante, "Glissandi", The Modern Trumpet | pedagogy | section | https://themoderntrumpet.com/2021/01/15/glissandi/ | 2026-09-15 |
| NCVS-REGISTERS | National Center for Voice and Speech, "Voluntary Register Changes", NCVS Tutorials | pedagogy | section | https://ncvs.org/tutorials/voluntary-register-changes/ | 2026-09-15 |
| PIMENTEL-SAXVIBRATO | Bret Pimentel, "Saxophone vibrato", bretpimentel.com | pedagogy | section | https://bretpimentel.com/saxophone-vibrato/ | 2026-09-15 |
| PIMENTEL-STALEAIR | Bret Pimentel, "Stale air", bretpimentel.com | pedagogy | section | https://bretpimentel.com/stale-air/ | 2026-09-15 |
| PISTON-1955 | Walter Piston, Orchestration | standard reference | not-read | none | 2026-09-15 |
| PISTON-ORCH | Walter Piston, Orchestration | standard reference | not-read | none | 2026-09-15 |
| POLAK-LONDON-2014 | Rainer Polak and Justin London, "Timing and Meter in Mande Drumming from Mali", Music Theory Online 20.1 (2014) | ethnomusicology | section | https://mtosmt.org/issues/mto.14.20.1/mto.14.20.1.polak-london.html | 2026-09-15 |
| RIMSKY-1913 | Nikolay Rimsky-Korsakov, Principles of Orchestration, trans. Edward Agate, ed. Maximilian Steinberg, Project Gutenberg #33900 | orchestration | section | https://www.gutenberg.org/ebooks/33900 | 2026-09-15 |
| SAXJASA-2011 | Jer-Ming Chen, John Smith and Joe Wolfe, "Saxophonists tune vocal tract resonances in advanced performance techniques", Journal of the Acoustical Society of America 129(4), 415-426 (2011) | academic acoustics | section | https://doi.org/10.1121/1.3514423 | 2026-09-15 |
| STRAD-SPICCATO | "Spiccato and sautille: two important bow strokes which are often confused", The Strad | performer | full | https://www.thestrad.com/improve-your-playing/spiccato-and-sautille-two-important-bow-strokes-which-are-often-confused/13970.article | 2026-09-15 |
| STRINGS-LIBRARY-MANUAL-1 | Spitfire Audio, Spitfire Symphonic Strings User Manual (26 pages; the sections on basic principles, legato, performance legato, articulations, round robins and controls) | manual | section | https://spitfire-www-assets.s3.amazonaws.com/manuals/SpitfireSymphonicStrings_UserManual.pdf | 2026-09-15 |
| TAMINGSAX-GROWL | "The saxophone growl", tamingthesaxophone.com | pedagogy | section | https://tamingthesaxophone.com/lessons/effects/growl | 2026-09-15 |
| TAMINGSAX-SUBTONE | "Subtone on the Saxophone", tamingthesaxophone.com | pedagogy | section | https://tamingthesaxophone.com/lessons/tone-sound/saxophone-subtone | 2026-09-15 |
| TERNSTROM-CHOIR-2002 | Sten Ternstrom, "Choir acoustics - an overview of scientific research published to date", TMH-QPSR 43(1), KTH Dept. for Speech, Music and Hearing | academic acoustics | full | https://www.diva-portal.org/smash/get/diva2:1416134/FULLTEXT01.pdf | 2026-09-15 |
| TROMBONE-ORG-VIBRATO | "Vibrato: An Overview for Trombonists", trombone.org (International Trombone Association archive) | pedagogy | section | https://www.trombone.org/articles/view.php?id=276 | 2026-09-15 |
| TRUMPETMUTES-NOTESTEM | "Trumpet Mute Types And How They're Used", Notestem | performer | excerpt | https://www.notestem.com/blog/trumpet-mute-types/ | 2026-09-15 |
| UNSW-BRASS | Joe Wolfe, "Brass instrument acoustics", Music Acoustics, UNSW Sydney | academic acoustics | section | https://newt.phys.unsw.edu.au/jw/brassacoustics.html | 2026-09-15 |
| UNSW-CLARINET-INTRO | Joe Wolfe, "Clarinet acoustics: an introduction", Music Acoustics, UNSW Sydney | academic acoustics | section | https://newt.phys.unsw.edu.au/jw/clarinetacoustics.html | 2026-09-15 |
| UNSW-FLUTE-INTRO | Joe Wolfe, "Flute acoustics: an introduction", Music Acoustics, UNSW Sydney | academic acoustics | section | https://newt.phys.unsw.edu.au/jw/fluteacoustics.html | 2026-09-15 |
| VOICESCIENCE-BELTING | "Belting in Singing: How It Works and How to Belt Safely", Voice Science (citing Estill, Schutte and Miller, Bestebreurtje and Schutte) | pedagogy | full | https://www.voicescience.org/lexicon/belting/ | 2026-09-15 |
| VOICESCIENCE-VIBRATO | "Vibrato Rate: Speed of Pitch Oscillation in Singing", Voice Science (citing Prame 1994, Nix et al. 2016, Glasner and Johnson 2022) | pedagogy | full | https://www.voicescience.org/lexicon/vibrato-rate/ | 2026-09-15 |
| WOLFE-AT2018 | Joe Wolfe, "The Acoustics of Woodwind Musical Instruments", Acoustics Today 14(2), 50-56 (2018) | academic acoustics | section | https://newt.phys.unsw.edu.au/jw/reprints/Wolfe_AT2018.pdf | 2026-09-15 |
| WOLFE-VIOLIN | Joe Wolfe et al., "Violin acoustics: an introduction", Music Acoustics, UNSW Sydney | academic acoustics | section | https://www.phys.unsw.edu.au/jw/violintro.html | 2026-09-15 |
| WOODHOUSE-GUETTLER | Jim Woodhouse, "9.5 Getting that perfect start: Guettler's diagram", Euphonics | academic acoustics | section | https://euphonics.org/9-5-getting-that-perfect-start-guettlers-diagram/ | 2026-09-15 |
| WOODHOUSE-SCHELLENG | Jim Woodhouse, "9.3 How a violinist can go wrong: Schelleng's diagram", Euphonics | academic acoustics | section | https://euphonics.org/9-3-how-a-violinist-can-go-wrong-schellengs-diagram/ | 2026-09-15 |
