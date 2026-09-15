# Historical temperaments

## Cultural context

A tuning theory file, so the heading means something different here. These are **keyboard
practices**, tied to particular repertoires, particular instruments and particular pitch
standards, mostly in Europe between roughly the fifteenth and the nineteenth centuries.

Two things follow from "keyboard practices":

- A temperament is a solution to the problem of having **twelve fixed pitches per octave** and
  wanting to play in more than one key. Singers, string players and trombonists do not have that
  problem in the same way, and did not necessarily play what the keyboard played.
- A temperament travels with a repertoire and a pitch standard. Historical pitch standards varied
  widely by place and period, so "which A" is a separate question from "which temperament", and
  both have to be answered before a historically informed claim can be made.

The names in this file (meantone, Werckmeister, and the well temperaments generally) are not a
chronological ladder ending in 12-tone equal temperament. They are different trades.

## Pitch organisation

**Every tuning trades pure intervals against note count against transposability.** That sentence
is the whole subject. With twelve fixed pitches you cannot have pure fifths, pure thirds and free
transposition at once, because the commas described in `JUST_INTONATION.md` do not vanish.

| Family | What it buys | What it pays |
|---|---|---|
| Pythagorean | pure fifths | very wide thirds |
| Quarter-comma meantone | pure major thirds (5/4) | a wolf fifth; remote keys unusable |
| Well temperaments | all twelve keys usable | no key is pure; each key sounds different |
| 12-tone equal | uniformity; free transposition | no pure third; every key identical |

**Meantone buys thirds and loses keys.** Quarter-comma meantone narrows the fifths so that four of
them stack to a pure major third. Twelve such fifths overshoot, and the error collects in one
interval, the **wolf fifth**, which is unusable. Keys that need the wolf are off limits. The
repertoire written for meantone instruments stays inside the usable keys, which is why that
repertoire's key range looks narrow to a modern eye.

**Well temperaments make every key usable at the cost of making them different.** Werckmeister III
is the standard example: four fifths (C-G, G-D, D-A and B-F sharp) are narrowed by a quarter of a
Pythagorean comma each and the other eight are left pure. Four quarters make one comma, which is
exactly the excess of twelve pure fifths over seven octaves, so the circle closes. Unlike
quarter-comma meantone, there is no wolf fifth and all twelve notes can serve as a tonic. The keys
are usable but they are not equivalent: each has its own distribution of interval sizes.

**12-tone equal temperament buys uniformity.** Every fifth is equally slightly narrow, every third
equally wide, every key identical, every transposition exact. It is a trade, and describing it as
the absence of a trade is the error this file exists to prevent.

**Specific cent values are to verify.** The narrowing schemes and the resulting interval sizes
should be checked against a tuning reference before any file or output prints numbers. Barbour,
*Tuning and Temperament* (1951) and Duffin, *How Equal Temperament Ruined Harmony* (2007) are the
standard references, and neither was read during research.

## Key character

**Key character is a real historical phenomenon, not a superstition.** In any unequal temperament,
C major and F sharp major genuinely contain different interval sizes, so they genuinely sound
different, and the written descriptions of key affect from those periods describe something that
was audible.

In 12-tone equal temperament, key character survives only as instrument register, string and
open-string behaviour, and listener association. The interval sizes are identical. Do not carry a
historical key affect table into an equal-tempered project and present it as acoustics.

## Rhythm and cycle

Not applicable.

## Phrase structure and form

Not applicable directly, but there is a real consequence: composers writing for unequal
temperaments choose keys and modulations partly for their colour, and a modulation to a remote key
is an event because the key sounds remote. Re-tuning such a piece to 12-tone equal temperament
removes that event.

## Ornamentation

Not applicable.

## The role of improvisation

Not applicable as a system property, beyond the constraint that improvisation on a meantone
keyboard stays inside the usable keys.

## Ensemble behaviour

Omitted as an ensemble practice. The practical point is that where a keyboard is fixed and other
players are flexible, the ensemble negotiates: the flexible instruments adjust to the keyboard, or
the keyboard is retuned for the programme.

## What generalises

- Naming the trade (pure intervals, note count, transposability) is a transferable way to evaluate
  any tuning decision, including modern microtonal ones.
- Key colour as a compositional resource is available whenever the tuning is unequal, which
  includes most of the systems in this folder.
- A tuning that makes some keys unusable is a constraint that shapes repertoire, which is a useful
  thing to know when writing inside any restricted system.
- The idea that a widely adopted standard is a trade rather than a neutral baseline applies well
  beyond tuning.

## What must not be casually universalised

- Do not treat 12-tone equal temperament as the neutral default against which the others are
  historical curiosities.
- Do not apply a historical temperament to repertoire it does not belong to and call the result
  historically informed. The temperament, the repertoire and the pitch standard go together.
- Do not carry key-affect tables into equal-tempered music as if the affects were acoustic.
- Do not print cent values for a named temperament without checking them against a tuning
  reference.
- Do not describe these as "before equal temperament". Several were in use alongside it.

## Working with this in the studio

**Composer** sets: the temperament by name, the reference pitch in Hz, the key or keys, and
whether the piece exploits key colour or merely tolerates it. If the piece modulates, check that
the destination keys are usable in the chosen temperament.

**Performance Director** needs: which intervals are wide or narrow in the chosen keys, since that
changes how a player voices and balances a chord, and whether any player is expected to adjust
against the keyboard.

**MIDI Builder and Plugin Auditor** must check whether the instrument can load a temperament at
all and by which mechanism, and whether the reference pitch can be set independently of the scale.
Some hosts ship named historical temperaments as presets: verify the preset's values against a
reference rather than trusting the name, because implementations differ. Verify also that the
tuning applies to every instrument in the project and not only to the one that loaded it. See
`shared/TUNING_AND_MPE.md`.

**Listener Model** should not score the wide thirds of a Pythagorean tuning or the wolf fifth as
errors, and should not assume a modern listener hears key colour without being told where to
listen.

## Sources and confidence

- Barbour, *Tuning and Temperament: A Historical Survey*, 1951. Open first.
- Duffin, *How Equal Temperament Ruined Harmony*, 2007, for an argumentative modern treatment.
- On Werckmeister III: the fifths narrowed by a quarter Pythagorean comma, the absence of a wolf
  fifth and the usability of all twelve tonics come from secondary technical sources, not from
  Werckmeister. **2.0 printed five narrowed fifths, which is arithmetically impossible**: five
  quarters of a comma overshoot the one comma the circle needs. 2.1 corrects it to the four-fifth
  scheme of the standard accounts (Barbour, not read; the arithmetic is checkable without him).

Confidence: the framing of tuning as a trade and the meantone and well-temperament trade-offs are
consistent across the sources found; the Werckmeister III scheme is the standard account and its
arithmetic is checked. **Explicitly
unverified:** all specific cent values, including those for quarter-comma meantone, which are to
be checked against a tuning reference before printing. Barbour and Duffin were not read during
research.
