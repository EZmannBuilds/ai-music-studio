# Choir and Voice

The human voice, solo and in a choir. Read with `shared/VOCAL_ARCHITECTURE_SCHEMA.md` and
`shared/LYRIC_ALIGNMENT_SCHEMA.md`, which carry the studio's vocal structures; this file carries what
the instrument does.

> Evidence: `musicianship` for the consonant placement figure and the breath, blend and tessitura
> material. `to-verify` for the formant claim, against Sundberg, *The Science of the Singing Voice*,
> which was **not opened** for this work. `orchestration-text` for the SATB ranges, attributed to
> Adler, *The Study of Orchestration*, not opened. No measured figures.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## What the instrument is

`musicianship`. Air from the lungs driving the vocal folds, filtered by a throat, mouth and nose that
the singer reshapes continuously. That filter is the point: the resonances it produces are what make
one vowel different from another, and a singer changes them while a note is sounding.

The consequence for programming: **a vowel is not a timbre, it is a changing state.** A sustained
"ah" that never moves is not a voice.

## Range and register

`orchestration-text`, attributed to Adler, not opened. Typical choral ranges, and these vary widely
by singer.

| Part | Typical range | Comfortable tessitura |
|---|---|---|
| Soprano | roughly C4 to A5 | around F4 to F5 |
| Alto | roughly G3 to D5 | around B3 to C5 |
| Tenor | roughly C3 to A4, sounding an octave below written | around F3 to F4 |
| Bass | roughly E2 to D4 | around A2 to C4 |

**Range and tessitura are different things, and tessitura is the one that matters.** A part can reach
its extreme note once. A part that lives at its extreme for sixteen bars will exhaust a real singer
long before the range check notices anything. The Performance Director should check where the line
**sits**, not only where it touches.

**Passaggio.** Every voice has one or two transition zones where the registration shifts, and notes
in those zones are harder to sing evenly and quietly. They sit roughly around the upper third of each
voice's range, and their exact position is individual. A sustained quiet note in the passaggio is a
demanding request; a sampled voice will produce it effortlessly and the part will read as unsung.
**To verify against Sundberg**, not opened.

## Articulation and note transitions

`musicianship`. The voice's articulation is **text**.

**Consonants are placed before the beat so the vowel lands on it.** This is the single most important
programming fact in this file. A singer aiming a word at beat one starts the consonant early enough
that the vowel arrives on the beat, because the vowel is what the ear times. A typical anticipation
is on the order of **10 to 60 milliseconds**, longer for a plosive or a cluster and shorter for a
soft onset. That range is `musicianship`, a practitioner value, not a measurement, and it should be
checked by ear against the actual syllable.

Transitions between notes are:

```text
legato        the vowel continues through the pitch change; no new consonant
portamento    the pitch slides between notes, audibly, as a stylistic choice
rearticulated the same pitch restarted with a consonant or a fresh onset
melisma       many notes on one vowel, with a small re-articulation on each
```

Vibrato is a property of the singer and the style, it develops across a note rather than starting
with it, and it is usually reduced or absent in blended choral singing.

## Physical constraints

`musicianship`.

- **Breath bounds the phrase.** A solo singer's phrase is a breath, and the breath is audible before
  it. Writing one without the other is the fastest way to a synthetic vocal.
- **A choir staggers its breath**, so a choral line can continue past any one singer's capacity while
  the individual singers breathe at different points. That is why a choir sustains and a soloist does
  not, and it is why choral phrase limits are not solo phrase limits.
- One voice, one note. Divisi is more parts, not more notes per singer.

## Phrase behaviour

`musicianship`. A sung phrase has a breath at each end, a shape in the middle, and text driving its
rhythm. Loud is usually also higher in the throat and brighter; quiet at the top of a range is
difficult and is itself expressive.

`to-verify`, against Sundberg, *The Science of the Singing Voice*, not opened: **vowel
intelligibility falls as the fundamental rises past the first formant.** A soprano high in her range
cannot produce distinct vowels the way she can in the middle, because the fundamental has passed
above the resonance that distinguishes them. This is why high soprano text is hard to understand in
performance, and why a high sampled vocal line with crisp diction sounds wrong in a way listeners
notice without being able to say why.

## Ensemble behaviour

`musicianship`. **Blend depends on matched vowel and matched vibrato.** A choir sounds like one
instrument when the singers agree on the shape of the vowel and reduce individual vibrato. Sampled
choirs are recorded that way, which is why they blend and why they are poor at sounding like
individuals.

**Divisi thins each part.** Splitting sopranos into two lines does not double the sound, it halves
the number of singers on each line, and the texture gets lighter and more exposed. This is error 14
in `COMMON_ERRORS.md` applied to voices.

Doubling a choral line with an instrument at the same pitch fuses them and removes the voice's
identity; doubling at the octave keeps it.

## Recording behaviour

`musicianship`. Choirs are recorded at a distance, in a resonant space, as a body. That is part of
the sound, so a sampled choir is already wide and already reverberant. Solo voices are recorded close
and dry, where breath and lip noise are audible and are part of the performance.

## Programming it: the control model

`musicianship`, consistent with the documented model in `STRINGS.md`. Product specifics belong in the
calibration profile.

```yaml
long_notes:
  dynamics_from: a continuous controller that crossfades recorded dynamic layers
vowels:
  selected_by: a controller, a keyswitch, or separate patches, depending on the product
  must: change during a phrase, not only between notes
consonants:
  in_simple_patches: absent entirely
  in_phrase_or_word_builder_approaches: sequenced syllable by syllable
  placement: before the beat, so the vowel lands on it
legato_patches: monophonic, need overlap; the transition is a vowel continuing through a pitch change
breath_noise: an articulation or a layer; do not mute it
release_samples: the phrase ending, including the closing consonant
divisi: more parts, and each part is thinner
```

**Phrase and word builder approaches**, in general terms: some vocal instruments let the writer
assemble a syllable sequence, aligning consonants and vowels to a rhythm, rather than playing a
single sustained vowel. Where such an instrument is available, it is the difference between a vocal
line and a pad. How it is driven is a product fact and belongs in the calibration profile.

## Programming it: what makes it sound real

- Place consonants ahead of the beat, and let the vowel land on it.
- Change vowels within held notes, following the text.
- Write breaths. Leave gaps, keep the breath sample, and stagger them in a choir.
- Draw a dynamic shape on every sustained note.
- Reduce diction and increase the dynamic as the line goes high; the real voice has no choice.
- Keep vibrato off the onset, and reduce it for blend.
- Treat divisi as thinning, and voice it accordingly.

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Voice-specific tells, and the first is the whole problem:

- **a sustained "ah" with no vowel change, no consonants and no breath**, which is precisely why a
  sampled choir reads as a synthesizer pad;
- consonants placed on the beat, so every word arrives late;
- phrases with no breath anywhere;
- flat sustains with no dynamic shape, which is error 2;
- crisp diction at the top of a soprano range;
- divisi written as thicker rather than thinner, which is error 14;
- constant identical vibrato on every note;
- a line that sits at the top of its range for a whole section with no relief.

## What the Performance Director and Vocal Director need from this file

- `breath_or_bow_overruns`: solo phrases longer than a breath. Choir phrases get the staggered-breath
  allowance, and the plan should say which rule was applied.
- **Tessitura check**, not only range: flag a line that sits at an extreme, and flag sustained quiet
  writing in the passaggio.
- `out_of_range`: against the typical ranges above, labelled `orchestration-text`.
- Consonant anticipation belongs in the plan as a per-syllable offset, with its practitioner-value
  label. `shared/LYRIC_ALIGNMENT_SCHEMA.md` carries the alignment itself.
- `breath` is a required imperfection cause here rather than an optional one.
- `simultaneity_exceeded`: one note per singer; divisi is a part count.

## Sources and what to verify

- **To verify**: formant behaviour, the fundamental crossing the first formant, passaggio physiology
  and vibrato rates, in Sundberg, *The Science of the Singing Voice*. **Not opened for this work**,
  and several of this file's claims rest on it.
- **To verify**: choral ranges, tessitura conventions and divisi practice in Adler, *The Study of
  Orchestration*. Not opened.
- **Not available**: a measured distribution of consonant anticipation times. The 10 to 60 ms figure
  is a practitioner value and is labelled as one everywhere it appears.
