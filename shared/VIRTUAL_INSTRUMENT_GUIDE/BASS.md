# Bass

Electric bass guitar first. Double bass is covered as a bowed instrument in `STRINGS.md`; its
plucked behaviour overlaps with this file.

> Evidence: `musicianship` throughout, with `excerpt-derived` for the string and fret counts repeated
> across programming guidance. No measured figures. Ranges are typical and labelled.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## What the instrument is

`musicianship`. A long-scale fretted instrument, plucked or struck, sounding an octave below the
guitar's lower strings. Its job in most music is two things at once: the harmonic floor, and half of
the rhythmic engine. Which of those a part is serving decides almost every programming choice in this
file.

## Range and register

`excerpt-derived` and `musicianship`. Typical ranges, to verify against a current instrument spec.

| Instrument | Typical range | Notes |
|---|---|---|
| Four-string | E1 to about G4, with 20 to 24 frets | standard tuning E1 A1 D2 G2 |
| Five-string | adds a low B0 | the low fifth is felt more than heard on small speakers |

Written an octave above sounding pitch, like the guitar. The fundamental of the lowest notes is below
what most playback systems reproduce, so the register's audibility depends on harmonics, which is why
a clean low B often disappears and a slightly overdriven one does not.

The register above the twelfth fret is thin and is used melodically rather than as a floor.

## Articulation and note transitions

`musicianship`.

```text
fingerstyle     alternating index and middle; round, with a soft attack; the default for most music
pick            harder, brighter, more consistent attack; cuts through dense arrangements
slap and pop    thumb struck against the low strings, fingers pulled off the high ones; percussive
ghost note      a muted, pitchless click on a rhythmic subdivision
dead note       the same idea used as an articulation inside a line
slide           audible movement between positions, and a standard way to approach a note
hammer-on and pull-off   softer than a plucked note, as on guitar
```

**Ghost notes and slides carry the groove. They are not decoration.** A bass line written as pitches
on the beat with everything between them silent is a harmonic part, not a bass part. The muted
sixteenths between the notes are what makes a line feel like it is played rather than entered.

Plucking position changes timbre continuously: near the bridge is thin and articulate, over the neck
is round and full, and a player moves between them within a song.

## Physical constraints

`musicianship`. **One note per string**, four or five strings, so double stops are possible and
chords above two notes are rare and voiced open. The scale length is long, so the fretting hand spans
fewer frets than on a guitar in low positions, typically three or four. Position shifts are audible
and often deliberately so.

## Phrase behaviour

`musicianship`. A plucked low note has a long, uneven decay: a strong initial transient, a bloom, and
a slow tail with a slightly moving pitch as the string settles. **It does not behave like the
rectangular block a piano roll draws.** Note length on bass is an articulation choice, and a line
written with every note ending exactly at the next is a line with no groove, because the silences
between the notes are where the groove is.

## Ensemble behaviour

`musicianship`. The bass and the kick drum occupy the same frequency range and the same rhythmic
territory, and the relationship between them is an arrangement decision, not a mix problem to be
solved afterwards.

```text
locked        bass notes land with the kick; heavy, unified low end
answering     bass fills where the kick does not; busier, more linear
ahead/behind  bass consistently placed fractionally early or late against the kick; feel, not error
```

Whichever is chosen, it should be chosen. Doubling the bass with a low synth layer thickens the
register quickly and usually needs one of the two to give up its low fundamental.

## Recording behaviour

`musicianship`. Usually a direct signal, an amplifier, or both blended. The direct signal carries the
low fundamental and the finger noise; the amplifier carries the midrange and the character. Pickup
position matters as on guitar. Compression is so standard on this instrument that an uncompressed
sampled bass with a wide dynamic range reads as unfinished rather than as expressive.

## Programming it: the control model

`musicianship`. Product specifics belong in the calibration profile.

```yaml
velocity: level, attack hardness, and in most libraries the sample selection between soft and hard plucks
articulation_switching: keyswitches for slides, ghost notes, harmonics, slap and pop
legato_patches: monophonic, and need overlap to produce a real slide or hammer-on
release_samples: string release and finger noise; lost when notes are glued end to end
fret_noise: a separate layer; on bass it is a large part of the realism
string_assignment: decides timbre where the library models it; a low note on a high string is different
```

## Programming it: what makes it sound real

- Write the ghost notes. A groove line without muted subdivisions is half-written.
- Vary note length deliberately, and leave silence. Short is a choice; long is a choice.
- Use slides into notes, especially at phrase starts and octave jumps.
- Vary velocity across a repeated figure so that the same note is never twice identical, which is
  error 1 in `COMMON_ERRORS.md`.
- Decide the kick relationship before writing, and keep it consistent enough to be a feel.
- Keep one note per string. A three-note chord on bass is possible only in open voicings.
- Let the first note of a phrase be louder than the notes inside it.

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Bass-specific tells:

- rectangular blocks glued end to end, which is error 12, and the reason a sampled bass sounds like a
  synth patch;
- every note at one velocity, which removes the whole groove vocabulary;
- no ghost notes and no slides anywhere;
- the same repeated root at identical velocity, which is error 1;
- close-voiced chords in the bottom octave;
- notes below the instrument's lowest string on a four-string patch, which is error 4;
- a line that ignores the kick entirely and then gets fixed with a sidechain.

## What the Performance Director needs from this file

- `out_of_range`: below E1 on a four-string, below B0 on a five-string, declared per instrument.
- `impossible_voicings`: two notes on one string, and chords above two notes outside open voicings.
- `articulation_unavailable`: slap, pop and ghost notes are separate recordings, not velocity zones.
- `note_length_variation` is a required imperfection here rather than an optional one.
- `fret_noise` and `pick_noise` should be requested explicitly.
- The kick relationship belongs in the plan, so the Mix Engineer reads an intent rather than guessing.

## Sources and what to verify

- **To verify**: string counts, fret counts and tuning conventions against a current instrument
  specification. The figures here are typical and `excerpt-derived`.
- **To verify**: low-frequency decay behaviour and pitch settling of a struck string, in Fletcher and
  Rossing, *The Physics of Musical Instruments*. Not opened for this work.
- **Not available**: measured velocity bands for ghost notes on bass. The drum-kit figure in
  `DRUM_KIT.md` should not be borrowed for this instrument.
