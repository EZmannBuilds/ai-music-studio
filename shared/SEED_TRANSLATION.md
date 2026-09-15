# Seed Translation
## Version 1.0

Turning something that is not music into music, without landing on the first association.

Executed by `creative-lab/SKILL.md`. Read by Composer, Arranger, Producer, Vocal Director and the
Project Guide, which uses it for character and scene themes.

Seeds include an image, a painting, a character, a story, a dream, a building, an object, a game
mechanic, a poem, a philosophical idea, a place, a movement, weather, a feeling.

---

# 1. The problem this solves

Cross-modal correspondence research documents real average tendencies: high pitch with height and with
smallness, loudness with brightness, angular shapes with sharp attacks. They are weak, they are
asymmetric, and they are **exactly the mappings that are already clichés**
(`research/ADAPTIVE_AND_EXPERIMENTAL.md`, section 6).

So "high" becoming high notes is not wrong. It is just the first thing, and if it is the only thing,
the result is the sound of the idea rather than a piece of music that the idea produced.

Synaesthesia is not the model here. It is idiosyncratic and consciously experienced, and it is not a
claim about what listeners share. What it is useful as is a metaphor for **commitment**: pick a
mapping and hold it.

---

# 2. Step 1: decompose the seed

Do not translate the seed. Translate its parts.

```yaml
seed_decomposition:
  seed:
  surface: []                  # what it looks, sounds or feels like
  behaviour: []                # what it does, how it moves, at what rate
  structure: []                # how it is built; its parts and their relations
  contradictions: []           # what is in tension inside it. Often the richest source.
  context: []                  # where it sits, what surrounds it, what it is for
  process: []                  # how it came to be, or what it does over time
  absence: []                  # what is missing from it, or refused
```

The contradiction line earns its place. "A ruined cathedral" is not translated well by grandeur or by
decay. It is translated by grandeur and decay being true at once, which is a structural problem and
therefore a musical one.

---

# 3. Step 2: generate across channels

Produce **at least five** translations, from **different channels**.

| Channel | Translates | Example of the move |
|---|---|---|
| a. cross-modal default | surface | bright becomes high and thin |
| b. motion | behaviour | approach becomes crescendo and narrowing reverb |
| c. structural | structure and contradiction | two things at once become two incompatible key areas |
| d. behavioural | what it does | a gait becomes a metre and an articulation |
| e. procedural | process | the story's process becomes the music's process |
| f. material | physics | the object's material becomes the instrument's physics |
| g. negation | absence | what is missing becomes what the music refuses to play |

**A candidate that uses only channel (a) is rejected as a candidate.** It may be kept as a layer inside
a stronger one.

```yaml
translation_candidate:
  channel:
  mapping:                     # the specific correspondence
  musical_consequence:         # what actually changes: pitch, rhythm, form, arrangement, production
  cliche_check:                # what the obvious version would have been, and how this differs
  tag: empirical | craft | metaphor
```

The `tag` keeps the studio honest. `empirical` means a documented correspondence. `craft` means
composers do this. `metaphor` means this is a chosen poetic link, which is legitimate and is not
evidence.

---

# 4. Step 3: commit

A translation that is revisited every section is decoration. The chosen mapping becomes an invariant
that the piece is built from.

```yaml
seed_commitment:
  chosen: []                   # one primary translation, optionally one or two supporting layers
  invariant:                   # what stays true across the whole piece
  where_it_is_audible: []      # the moments a listener could actually notice it
  where_it_is_deliberately_hidden: []
  what_it_forbids: []          # constraints this creates downstream
```

The last field matters: a real translation forbids things. If it forbids nothing, it was not a
translation, it was an adjective.

---

# 5. Worked example

The point is that these are not five descriptions of the same idea.

```text
SEED: teleportation

literal structure   abrupt spatial displacement with no traversal

a  surface          a bright transient burst at each jump                      (kept as a layer)
b  motion           the sound of approach is absent: things arrive at full size, already close
c  structural       the destination's harmony is heard before the departure resolves
d  behavioural      phrases restart on an unexpected subdivision, as if a beat were skipped
e  procedural       form reconnects through discontinuity: sections are cut, never transitioned
f  material         the dry signal is replaced by a spectral copy of itself from another room
g  negation         no riser, no fill, no crescendo - the music refuses every device of arrival

COMMIT: (e) as invariant, with (c) supporting and (a) as a layer
FORBIDS: risers, fills, crossfades, any transition that occupies time
```

That last line is why the method works. The piece now has a rule it can be held to, and a critic can
check it.

---

# 6. With a character or a scene

For a character theme, add:

```yaml
character_translation:
  wants:
  fears:
  hides:
  contradiction:
  what_they_would_never_do:    # becomes the music's forbidden device
  how_they_change:             # becomes the theme's transformation across the project
  theme_invariant:             # what stays recognisable when everything else changes
```

Transformation is the point: one identity re-harmonised, re-orchestrated and re-paced across a project
is how themes work in practice, rather than a fixed cue played on entrance. The invariant is declared
so that it survives.

---

# 7. Rules

- **Do not map cliché automatically.** Minor for sad, high for happy, drums for danger and a duduk for
  grief are defaults, not translations. Where a default is the right answer, say that it was chosen.
- **Do not reach for a culture as a colour.** "Ancient", "exotic", "tribal" and "oriental" are not
  musical descriptions. If a real tradition is being used, route through
  `shared/MUSICAL_SYSTEMS/` and carry its context and cautions.
- **Keep the levels apart.** What the seed is, what it suggests, and what the studio chose are three
  different statements, and the studio's existing evidence discipline applies.
- **The seed does not outrank the brief.** A translation that produces music the user did not ask for
  is a failed translation, however elegant.
