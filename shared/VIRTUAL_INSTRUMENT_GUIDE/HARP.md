# Harp

The concert pedal harp.

> Evidence: `excerpt-derived` for the pedal mechanism and glissando construction, from a public
> orchestration academy's harp articles read as search excerpts. `orchestration-text` for range and
> notation conventions, attributed to Adler, *The Study of Orchestration*, and Berlioz and Strauss,
> *Treatise on Instrumentation*, neither opened for this work. `musicianship` elsewhere.

Cross-family failures are in `COMMON_ERRORS.md`. The harp adds a constraint no other instrument in
this folder has, and it is the reason this file exists.

---

## What the instrument is

`musicianship`. Forty-seven strings, one per diatonic degree across the range, plucked by the
fingers, with seven pedals that raise or lower **every string of one letter name at once**.

That is the whole instrument in one sentence, and everything below follows from it.

## The pedal constraint

`excerpt-derived`. This is the most important section in the file.

```text
seven pedals            one per letter name: D C B on the left, E F G A on the right
three positions each    flat (up), natural (middle), sharp (down)
7 x 3 = 21 pitches      available from seven string classes
```

**Only seven pitch classes sound at any moment.** Not seven notes, seven pitch **classes**. If the D
pedal is natural, every D on the instrument is a D natural, everywhere, until the foot moves. A
passage that needs both D flat and D natural simultaneously is impossible, and one that needs them
successively requires a pedal change between them.

The pedals are divided between two feet:

```text
left foot    D  C  B
right foot   E  F  G  A
```

So two pedals can change at once only if they are on different feet. Three changes need two moves.

**A pedal change takes time and is slightly audible**, a mechanical click and, if the string is
ringing, a pitch shift. Changes are made in rests, on strong beats where the harp is not sounding, or
deliberately under cover of the orchestra.

## Glissandi are designed, not requested

`excerpt-derived`. A harp glissando is the player sweeping across all the strings. The pitches that
result are **whatever the pedals are set to**, so a glissando is a compositional object built by
choosing a pedal setting first.

Because there are seven string classes and twenty-one available pitches, **enharmonic doubling** is
how chords other than a plain diatonic scale are produced in a glissando. Setting C sharp and D flat,
for example, makes two string classes sound the same pitch, which removes a note from the sweep and
leaves a smaller set repeating. Common sonorities built this way include various seventh chords and
pentatonic collections.

**A chromatic glissando does not exist.** There are seven strings per octave. The instrument cannot
sweep twelve pitches, and no pedal setting will produce one.

Writing a glissando therefore means writing the pedal diagram, not the note heads.

## Range and register

`orchestration-text`, attributed to Adler, not opened. Roughly C1 to G7 across the full instrument.
The bottom octave is thick wire and slow to speak; the top is short, bright and decays fast. The
middle is the singing register.

## Articulation and note transitions

`musicianship` and `excerpt-derived`.

```text
plucked (default)     the normal tone; strings ring until damped
près de la table      plucked close to the soundboard; dry, thin, guitar-like
bisbigliando          a whispered tremolo, the same note taken with alternating fingers, very quiet
harmonics             a string touched at its midpoint and plucked; sounds an octave above, soft
muffling / etouffe    the hand laid on the strings to stop them; the only way to stop the ring
```

There is no legato. There is no sustain control other than damping.

## Physical constraints

`musicianship`.

```text
two hands, eight usable fingers. The little fingers are NOT used.
four notes maximum per hand, so eight simultaneous notes at the absolute limit
one string per finger, and adjacent strings need adjacent fingers
two feet, on seven pedals split three and four
```

Eight notes at once is a theoretical maximum, not a normal texture. Five or six is already a large
chord.

**Strings ring unless muffled.** A harp part with no damping indications is a part where everything
accumulates, which is often the intended sound and sometimes a mistake nobody noticed.

## Phrase behaviour

`musicianship`. Phrases are bounded by pedal settings, not by breath. The practical unit of harp
writing is a passage that lives inside one pedal configuration, with changes at the seams. A part
that modulates every bar is a part that is changing pedals every bar, and the player has two feet.

## Ensemble behaviour

`musicianship`. The harp is quiet and is easily covered. It works as colour, as arpeggiated texture,
and as a doubling of a line's attack. Two harps are written where one cannot manage the pedal changes
alone, which is a real and traditional reason rather than a matter of volume.

## Recording behaviour

`musicianship`. Recorded at a distance that lets the soundboard speak; close-miking emphasises finger
noise and string buzz. Orchestral libraries place it in the hall, already reverberant.

## Programming it: the control model

`musicianship`. Product specifics belong in the calibration profile.

```yaml
velocity: level and pluck hardness; often selects the sample
polyphony: high, and the patch will happily play what the instrument cannot
pedal_state: NOT modelled in most libraries. The writer is the pedal check.
glissando: either a recorded gliss articulation in fixed settings, or written notes at a sweep rate
round_robins: needed; arpeggios expose repeated identical samples quickly
release_samples: the damping sound; lost when notes are glued end to end
harmonics: a separate recording, sounding an octave above the written string
```

The line that matters: **the sampler does not enforce the pedal constraint, so nothing will stop an
impossible part except the feasibility check.**

## Programming it: what makes it sound real

- Write the pedal diagram before the notes, one per passage, and check every note against it.
- Build glissandi from a stated pedal setting, and accept the pitches it gives.
- Keep chords inside eight notes and four per hand, and spread them upward by default.
- Let strings ring, and write the muffling where the ring should stop.
- Vary velocity across an arpeggio; the thumb is stronger than the fingers, so the lowest note of a
  hand's group is usually the loudest.
- Use harmonics sparingly and quietly, and remember they sound an octave up.

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Harp-specific tells:

- two spellings of one letter name sounding at once, which is physically impossible;
- chromatic glissandi;
- pedal changes at a rate two feet cannot manage;
- nine or ten note chords, or five notes in one hand, which is error 6;
- arpeggios at one velocity, which is error 1;
- everything damped instantly by short note lengths, which is error 12, or nothing ever damped;
- a written glissando with no pedal setting behind it, so the sampled pitches are whatever the patch
  happened to record.

## What the Performance Director needs from this file

- A **pedal feasibility pass** is the harp's version of the four-limb rule. Track the seven pedal
  states across the part, flag any simultaneous conflict, and flag any change rate exceeding two feet.
- `impossible_voicings`: more than four notes per hand, more than eight total, or two pitch classes
  on one letter name.
- `out_of_range`: against the typical range above, labelled `orchestration-text`.
- `articulation_unavailable`: harmonics, near-the-soundboard tone and the whispered tremolo are
  separate recordings.
- Damping is a written decision here, so `note_length_variation` carries real musical meaning.

## Sources and what to verify

- `excerpt-derived` pedal and glissando material came from a public orchestration academy's harp
  articles, read as search excerpts only. **Verify the pedal-foot assignment and the standard
  glissando settings against a harp method or Adler.**
- **To verify**: full range, notation of pedal diagrams, and idiomatic writing in Adler, *The Study
  of Orchestration*, and Berlioz and Strauss, *Treatise on Instrumentation*. Neither was opened.
- **Not available**: a measured pedal change time. Treat it as a practitioner judgement.
