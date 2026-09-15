# Contemporary microtonality

## Cultural context

A tuning practice file rather than a tradition file. "Contemporary microtonality" covers
composers, producers and instrument builders working outside 12-tone equal temperament by choice,
using tunings they select or design.

The internal distinctions worth naming:

- **The xenharmonic community**, largely online, which develops and documents EDOs, regular
  temperaments and notation systems collaboratively. The Xenharmonic Wiki, Scale Workshop and a
  scattering of forums and mailing lists are its infrastructure. Treat its output as a living
  community practice, and cite the wiki as a community wiki.
- **The extended just intonation lineage** in Western concert music, from Partch through Ben
  Johnston and onward, with its own notations and its own instrument-building traditions.
- **Electronic and production practice**, where retunable soft synths have made non-12 tunings
  available to anyone, and where the tuning is often chosen for timbral reasons rather than
  theoretical ones.

These overlap, and they disagree about notation, terminology and what matters. There is no single
authority to defer to.

## Pitch organisation

### The timbre and tuning relationship

This is the central idea in the file. Sethares (*Tuning, Timbre, Spectrum, Scale*, 1998, 2nd ed.
2005) argues that the sense of consonance and dissonance does not depend on fixed intervals but on
**how a sound's partials align with the scale being used**. Dissonance curves, built on the Plomp
and Levelt model, answer two questions directly: given a timbre, what scale should it be played
in, and given a desired scale, what timbres suit it.

The consequence for a producer is immediate. For **inharmonic timbres**, bells, many gamelan
instruments, stretched or detuned partials, the "right" scale is not the one that suits a harmonic
timbre. A tuning that sounds rough on a sawtooth can sound consonant on a bell, and the reverse.

**Design timbre and tuning together.** In a studio this is a practical instruction: choose or
synthesise the timbre alongside the scale, and test them as a pair, rather than loading a scale
into whatever patch is already there. `GAMELAN.md` describes a tradition that has always done
this.

### Notation

**Extended just intonation notation systems exist, they differ, and they are not
interchangeable.** Two in common use:

- **Johnston's system**, whose base is a just C major scale in which F-A-C, C-E-G and G-B-D are
  all just major triads, with sharp and flat altering by 25:24 (about 70.67 cents), plus and minus
  altering by 81:80 (about 21.506 cents), a 7 and an inverted 7 for the seventh partial, arrows
  for the eleventh, and the numeral itself for thirteen and above. Fonville's guide (1991) is the
  standard interpreter's reference.
- **The Helmholtz-Ellis system**, a different set of accidentals with different conventions.

A score in one system cannot be read as though it were in the other. State which system is in use.
Where notation matters to a project, open Fonville first.

### Non-octave scales

A scale does not have to repeat at the octave. The **Bohlen-Pierce** scale is the standard
example: a thirteen-tone scale whose period is the **tritave**, a 3:1 ratio, rather than the 2:1
octave. It is designed to emphasise odd-number intervals and chords such as the 3:5:7:9 tetrad,
and exists both as a seven-limit just scale and as thirteen equal divisions of the tritave. It was
found independently by Bohlen, van Prooijen and Pierce.

Non-octave scales connect directly to the timbre argument: a scale built from odd harmonics suits
timbres that lack even partials, such as a clarinet-like spectrum.

## Rhythm and cycle

Not applicable. Some composers extend ratio thinking to rhythm, but that is a separate
compositional choice.

## Phrase structure and form

Not applicable as a system property. A practical observation: because an unfamiliar tuning takes a
listener time to orient in, pieces in new tunings often need more repetition and slower harmonic
pacing than the same material would need in a familiar one.

## Ornamentation

Not applicable.

## The role of improvisation

Possible and increasingly common, bounded by the controller. Improvisation in a non-12 tuning
depends entirely on whether the player has an instrument with a playable mapping, which is why
isomorphic keyboards and continuous controllers are common in this community.

## Ensemble behaviour

Omitted as a tradition practice. The constraint is that every instrument must be in the same
tuning from the same reference, and in a studio that is a technical problem with real solutions,
covered in `shared/TUNING_AND_MPE.md`.

## What generalises

- Consonance is not a fixed property of an interval. It depends on the spectrum. This changes how
  a producer should think about chord voicing and sound design even in 12-tone equal temperament.
- Designing the sound and the pitch system together, rather than sequentially, is a transferable
  working method.
- A period other than the octave is a compositional option, and it makes the octave itself visible
  as a choice.
- Choosing a tuning for what it is good at, and then writing for those intervals, is better
  practice than importing existing material into a new tuning.

## What must not be casually universalised

- Do not treat a microtonal tuning as an effect applied to otherwise unchanged material.
  Transposing a 12-tone part into 31-EDO does not make it a 31-EDO piece.
- Do not mix notation systems, or present accidentals without saying which system they belong to.
- Do not assume the timbre in the project is neutral with respect to the tuning. If it is harmonic
  and the scale is not, that is a decision, and it should be made deliberately.
- Do not use the traditions in this folder as a source of "microtonal" colour. They are systems,
  not tuning tables, and rule 6 in `INDEX.md` applies.
- Do not assume a listener will hear an unfamiliar tuning as intended rather than as mistuned. See
  the Listener Model note below.

## How to start

A workable first project, stated plainly:

1. Pick **one** tuning and keep it for the whole piece: a small EDO (19 or 22 are manageable) or a
   small just subset built on one reference.
2. **Design the timbre with it.** Test the scale on the actual patch, and adjust the patch's
   partials or the scale until the intervals you intend to use sound the way you want.
3. **Write for the intervals the tuning is good at.** Every tuning has strengths; in 22, the
   septimal supermajor third, for example. Build the harmony out of those rather than out of
   approximations of familiar chords.
4. Decide the controller mapping before writing, because it shapes what you will play.
5. State the tuning, the reference pitch and the notation system in the project documentation.

## Working with this in the studio

**Composer** sets: the tuning with its period and reference pitch, the notation system, the subset
of intervals the piece is built on, and the timbral requirement that follows from the tuning.

**Performance Director** needs: the mapping, the notation system, and which intervals carry the
piece.

**MIDI Builder and Plugin Auditor** must check whether each instrument can be retuned, by which
mechanism, whether it supports a non-octave period, whether it supports more than twelve pitches
per period, and whether its filters and effects track the tuning. Several instruments accept a
scale file but retune only the oscillators. Verify the reference pitch per instrument. All of this
belongs to `shared/TUNING_AND_MPE.md`, which is where the mechanisms and the compatibility
questions live. Silent re-quantisation to 12-tone equal temperament is not acceptable.

**Listener Model** should not assume a listener trained on 12-tone equal temperament hears an
unfamiliar interval as a new colour rather than as an error. That is a genuine constraint on the
music, and it is answered by context, repetition and timbre rather than by insisting the listener
is wrong.

## Sources and confidence

- Sethares, *Tuning, Timbre, Spectrum, Scale*, Springer, 1998, 2nd ed. 2005. Open this first. It
  is the source of the timbre and tuning argument and of the dissonance-curve method.
- Fonville, "Ben Johnston's Extended Just Intonation: A Guide for Interpreters", *Perspectives of
  New Music* 29/2 (1991), 106 to 137, for Johnston notation; Gann's summary page is a useful
  secondary.
- Xenharmonic Wiki, for the Bohlen-Pierce scale and for EDO and temperament documentation. A
  community wiki: cite it as one.
- Mathews and Pierce and colleagues (1984 and 1988) for the psychoacoustic work behind
  Bohlen-Pierce.

Confidence: the Sethares argument and the Johnston accidental ratios are reported consistently
across the sources found. **To verify:** the exact base ratios of Johnston's C major scale, in
particular whether D is 10/9 rather than 9/8, which the secondary sources discuss but which was
not confirmed; and the Mathews and Pierce studies, which were not reachable during research.
Sethares was not read in full.
