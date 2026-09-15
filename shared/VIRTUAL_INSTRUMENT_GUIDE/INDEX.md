# Virtual Instrument Guide

What instruments actually do, and what a sampled or modelled version of one needs from the notes in
order to sound like the real thing.

The structure of every file here is defined in `shared/INSTRUMENT_BEHAVIOR_SCHEMA.md`. Read that
first if you are adding or editing a file.

---

# 1. What this folder is, and is not

This folder holds **instrument behaviour**. That is general and portable: it stays true whoever made
the library on the machine. It is not a vendor list, a buying guide or a patch reference.

```text
instrument behaviour     shared/VIRTUAL_INSTRUMENT_GUIDE/   general, portable, here
product capability       plugin audit                       this machine, this edition
measured response        calibration profile                this patch, this version
product names, formats   shared/FREE_INSTRUMENTS.md         acquisition and licensing
```

The three-layer split above is the schema's, not this page's. The line is drawn like this: "a horn
player breathes" belongs here; "this patch's dynamics arrive on a particular controller and its
legato lags a particular number of milliseconds" belongs in a calibration profile, because the next
user has a different library.

**No file in this folder names a commercial product.** Where the research rests on a manufacturer
manual, the files say "one documented library" and label the claim. That is deliberate. A guide that
names products ages into a catalogue and stops being about instruments.

---

# 2. Evidence labels

Every major section of every file carries one. The labels are defined in
`shared/INSTRUMENT_BEHAVIOR_SCHEMA.md` section 3 and repeated here so the folder can be read alone.

| Label | Means |
|---|---|
| `manual-derived` | stated in a manufacturer manual that was read in full for this work |
| `excerpt-derived` | from a search excerpt of a named source, not the full text |
| `orchestration-text` | attributed to a standard reference that was **not** opened for this work |
| `musicianship` | general practice, stated as inference rather than citation |
| `measured` | from a calibration render on the user's own system; not used in this folder |
| `to-verify` | named explicitly, with what a reader should open to confirm it |

When this research was done, **one manufacturer manual was read in full**, a symphonic strings
library. Most other sources were reachable only as search excerpts, or not at all. So the strings
file is the best-supported file here, and much of the rest is labelled `musicianship` or
`orchestration-text`. That is honest, and it is the point. Only `measured` may be reported as
MEASURED under `shared/RESEARCH_RULES.md`.

Numbers in this folder are **typical ranges with a label**, never facts about the reader's
instrument. Where the research gave no range, the files say "typical range, to verify against
<named reference>" rather than inventing one.

The standard references named but not opened: Adler, *The Study of Orchestration*; Piston,
*Orchestration*; Berlioz and Strauss, *Treatise on Instrumentation*; Fletcher and Rossing, *The
Physics of Musical Instruments*; Sundberg, *The Science of the Singing Voice*. Anyone extending this
folder should open those first.

---

# 3. The files

| File | One line |
|---|---|
| `COMMON_ERRORS.md` | the cross-family failure list, held once so family files link instead of repeating |
| `PIANO_AND_KEYBOARDS.md` | velocity as timbre, pedalling, hand span, voicing; electric piano and clav |
| `GUITAR.md` | one note per string, fretboard-first voicings, strum as a spread with a direction |
| `BASS.md` | fingerstyle, pick and slap; ghost notes and slides as groove; the kick relationship |
| `STRINGS.md` | the documented control model: continuous dynamics, monophonic legato, overlap |
| `BRASS.md` | breath, endurance, mutes as sample sets, and why a swell is a timbre change |
| `WOODWINDS.md` | one player one note; register maps; the clarinet break; tonguing versus slurring |
| `DRUM_KIT.md` | four limbs, ghost notes as a different sample, hi-hat openness as a state |
| `PERCUSSION.md` | timpani, cymbals, snare, bass drum; hand percussion stroke vocabularies |
| `MALLETS.md` | marimba, vibraphone, glockenspiel; rolls, motor, dampening, mallet hardness |
| `HARP.md` | seven pitch classes at a time; glissandi are designed; pedal changes take time |
| `CHOIR_AND_VOICE.md` | consonants before the beat, tessitura, passaggio, blend, staggered breath |
| `ORGANS.md` | no velocity; registration is the dynamic; swell box; drawbars and the rotary speaker |
| `SYNTHS_AND_SAMPLERS.md` | organic means response and change, not acoustic imitation |
| `CULTURALLY_SPECIFIC_INSTRUMENTS.md` | a research protocol, not content, and it says so at the top |

---

# 4. Who reads this folder, and for what

| Reader | Uses it for |
|---|---|
| Performance Director | articulation choice, phrase limits, feasibility, what organic means here |
| Producer | character, register colour, ensemble behaviour, recording behaviour |
| Composer | practical range, idiom, what falls under the hand |
| Vocal Director | `CHOIR_AND_VOICE.md`, and the voice sections elsewhere |
| MIDI Builder | note overlap, what velocity means, keyswitches, release handling |
| Plugin Auditor | what to look for in a patch, and what a calibration pass should measure |
| Music Critics | whether a part is playable, and whether "fake" is a real finding |

The Performance Director is the heaviest reader. Every family file ends with a section addressed to
it directly, naming the feasibility checks that file supports in
`shared/HUMAN_PERFORMANCE_SCHEMA.md` section 5.

---

# 5. Standing rules for this folder

1. **Behaviour before programming.** A file that opens with controller numbers has skipped the
   point. The instrument comes first; the virtual instrument is the second half.
2. **Ranges, not constants.** Every number carries a label and a way to check it.
3. **Name what you do not know.** A `to-verify` line is more useful than a confident invention.
4. **Organic is not random.** Humanisation means systematic, caused deviation at natural magnitude.
   The causes the studio recognises are listed in `shared/HUMAN_PERFORMANCE_SCHEMA.md` section 4. An
   imperfection with no cause is a bug, not a feature, and `deliberately_mechanical` is a legitimate
   target that produces an empty imperfection list.
5. **Culturally specific instruments get a protocol, not a summary.** See
   `CULTURALLY_SPECIFIC_INSTRUMENTS.md`, with `shared/MUSICAL_SYSTEMS/INDEX.md` for the governing
   rules and `shared/FUSION_PROTOCOL.md` for the bridge requirement.
6. **No product names.** Ever, in this folder.


## What this folder does not cover, and the shape of that gap

Thirteen of the family files describe instruments of the Western orchestra, the Western band and the
studio. One file covers everything else, and it is a research protocol rather than content.

**That is a lopsided shape, and it is worth naming rather than leaving as an implication.**
`shared/MUSICAL_SYSTEMS/INDEX.md` rule 2 forbids exactly this category ("never 'world', 'ethnic', or
a continent used as a genre"), and a folder with thirteen files on one tradition's instruments and
one on the rest is the structural version of that mistake, whatever the individual files say.

The reason is not that the other instruments matter less. It is that writing them properly needs
sources this work could not reach, and a paragraph written without them would be worse than no
paragraph. `CULTURALLY_SPECIFIC_INSTRUMENTS.md` is a protocol precisely because a summary written
from the available material would have been wrong in ways that read as authoritative.

What follows from that:

- **Do not read the coverage as a judgement of importance.** A file's absence here says something
  about this pack's sources, not about the instrument.
- **Do not treat the thirteen as the general case and the fourteenth as the exception.** A cello is
  as culturally specific as an oud. It is just that this folder's sources happen to describe it.
- **The gap is fillable.** A family file for an instrument the writer actually knows, or can reach
  primary sources for, belongs here under the same evidence discipline as the rest. That is the fix,
  and it is better than the alternative of writing them all thinly.
