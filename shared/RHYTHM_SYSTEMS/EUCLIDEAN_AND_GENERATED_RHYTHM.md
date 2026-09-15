# Euclidean and Generated Rhythm

## What E(k,n) does

E(k,n) distributes k onsets as evenly as possible over n discrete pulses. "As evenly as
possible" matters: when k divides n the result is trivially regular, and when it does not the
algorithm spreads the onsets so that the gaps between them take only two adjacent values.

```text
E(3,8)   x . . x . . x .
E(5,8)   x . x x . x x .
E(2,5)   x . x . .
E(4,9)   x . x . x . x . .
E(5,16)  x . . x . . x . . x . . . x . .
```

The output is a binary onset string over a fixed pulse count. It has no accents, no dynamics, no
instrumentation and no name.

## Where the algorithm came from

Bjorklund (2003) devised the procedure for timing pulses in a particle accelerator. Toussaint
(2005, "The Euclidean Algorithm Generates Traditional Musical Rhythms") showed that the
procedure coincides with the steps of Euclid's algorithm for the greatest common divisor, and
that its outputs coincide with a number of traditional patterns.

That origin is worth keeping in view. The algorithm was not derived from music. Its outputs
match some musical patterns, which is an observation about the shape of those patterns, not an
account of why they exist.

## The confirmed correspondences

The studio treats three correspondences as confirmed from the research, and no more than three
without checking the source.

```text
E(3,8)    the Cuban tresillo
E(5,8)    the cinquillo
E(5,16)   a bossa nova pattern
```

**Several matches require rotating the generated necklace.** The algorithm produces one starting
point; the tradition uses another. A rotation is not a cosmetic difference: it changes which
onset falls on the reference point, which changes what the pattern is.

The full Toussaint correspondence table is marked **to verify** in `research/RHYTHM.md` and
stays marked here. Do not extend the list above from memory. If a plan needs a fourth
correspondence, someone checks the source first.

## Rotation is where the meaning lives

```yaml
euclidean_pattern:
  k:                      # onsets
  n:                      # pulses
  rotation: 0             # how many pulses the necklace is turned
  pulse_value:            # what one pulse is, e.g. an eighth
  accent_pattern: []      # supplied separately; the algorithm gives none
  claimed_correspondence: # empty unless pattern, rotation and tempo all match a documented case
```

`rotation` is a required parameter, not an option. Writing `E(3,8)` without a rotation is
writing half a pattern.

```text
E(3,8) rotation 0   x . . x . . x .
E(3,8) rotation 1   . x . . x . . x      same necklace, different music
E(3,8) rotation 3   . x . x . . x .
```

Each rotation puts a different gap against the reference point, so each has a different
relationship to the cycle, to the dance and to the downbeat. Rotation is also the cheapest
source of genuine variation in a generated part: hold k and n, move the rotation, and the
material stays related while the feel changes.

## The naming rule

**Never label a generated pattern with the name of a tradition** unless the pattern, its
rotation and its tempo range all match a documented case, and then say which case.

```text
allowed      "E(3,8), rotation 0, at 95 BPM; matches the tresillo as reported by Toussaint 2005"
allowed      "E(5,16), rotation 2; shape only, not claimed as any named pattern"
forbidden    "a tresillo generated with E(3,8)" when the rotation was never checked
forbidden    "an African rhythm" for any generated output whatever
forbidden    naming any tradition on the basis of a shape match alone
```

The rule is not pedantry about credit. A name carries a rotation, a tempo, an accent hierarchy,
an instrument and a function, and a shape match supplies none of those. Applying the name
asserts all of them without evidence. Cultural detail belongs in
`shared/MUSICAL_SYSTEMS/CLAVE_AND_TIMELINES.md` and
`shared/MUSICAL_SYSTEMS/WEST_AFRICAN_POLYRHYTHM.md`, which describe patterns as they are used,
not as they are generated.

## What Euclidean generation does not give you

```text
rotation            the algorithm picks one arbitrarily; the tradition picks a specific one
accent hierarchy    which onsets are strong, and how strong
timbre and role     which instrument plays it, and what it is heard against
tempo range         a shape at 70 BPM and at 160 BPM are different musical objects
dance               what bodies do with it
a name              and everything a name implies
```

A Euclidean pattern is therefore a starting shape for a part, not a finished part. It needs an
accent pattern, an anchor to be heard against (see `POLYMETER_POLYRHYTHM_CROSSRHYTHM.md`) and a
timing template (see `MICROTIMING_AND_GROOVE.md`) before it is music.

## Other generative approaches

The same caution applies to each of these. They produce shapes; they do not produce names.

**Rotation and necklace thinking.** Treat an onset string as a circle rather than a line. Two
patterns that are rotations of one another are the same necklace. This is a useful way to relate
material across a section: state the necklace once, use different rotations in different parts,
and the parts are audibly related without being copies. It is not a claim that the rotations are
interchangeable in any tradition, because they are not.

**Probability-weighted onsets.** Assign each pulse a probability of carrying an onset, weighted
by metrical position, then sample. This produces variation with a controllable density and a
controllable bias toward strong positions. Two constraints: the weights encode a metrical
hierarchy, so they must come from the metre actually in use rather than from a default 4/4
weighting; and the output must be checked against the anchor, because a sampler will cheerfully
place an onset that contradicts the reference at the wrong moment.

**Neither approach is humanisation.** Both operate on the grid. Timing deviation is a separate
layer with its own rules, and it is a template rather than a randomiser.

## What each specialist does with it

**Composer** may generate a shape, but it supplies rotation, accents and a role before the shape
becomes a part. It fills `claimed_correspondence` only when all three conditions hold.

**Performance Director** treats a generated part like any other: it needs an anchor, and if it
is itself the anchor it is not humanised.

**Listener Model** evaluates the result as a pattern against a reference, and does not award it
credit for being algorithmically even. Evenness is not groove.

**MIDI Builder** encodes k, n and rotation in a track note so the pattern can be regenerated and
audited, and never writes a tradition's name into a track name on the basis of a generated
shape.
