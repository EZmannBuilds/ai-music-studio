# Experimental Music Systems
## Version 1.0

Music where conventional melody and harmony are not the centre: process, chance, sound itself.

Read by Composer, Creative Lab, Arranger, Producer, Music Critics and the Project Guide.

---

# 1. The question every entry has to answer

> What is this making audible?

Each of these traditions exists because someone wanted a listener to notice something that ordinary
musical vocabulary did not bring forward. Granular processing is not a texture button, and noise is
not an intensity setting. Used without the question, they become novelty, and the studio's own
originality rules already say that novelty from a strange sound over an otherwise generic structure is
not originality.

**A request for an experimental technique that cannot answer the question in one sentence gets the
question back, not the technique.**

---

# 2. Two families

```text
PROCESS          a rule runs, and the listener is meant to hear it running.
                 Correct means: the process is audible.

GENERATIVE       rules bound a space; every realisation differs.
                 Correct means: the space was explored, and identity survived.
```

They are often confused. A process piece whose rule cannot be heard has failed on its own terms. A
generative piece judged by whether one realisation is the best has been judged by the wrong standard.

---

# 3. The representation

```yaml
experimental_system:
  family: process | generative | indeterminate | sound_based | rule_based_improvisation
  what_it_makes_audible:       # one sentence. Required.
  seed:                        # the material or condition the system starts from
  rules: []                    # few enough to state plainly
  fixed_elements: []           # what does not vary. See section 4.
  variable_elements: []
  stopping_condition:          # when it is over, and who decides
  realisation_log:             # seed, rule version and any choices, so it can be repeated
  listener_experience:         # what someone hears over time, honestly
  failure_mode:                # what it looks like when this does not work
```

---

# 4. The constraint ratio

The identity of an open system comes from what does **not** move. In the documented cases the fixed
part is substantial: a fixed pitch set and a shared pulse; fixed melodic material with only the
timing left open; a fixed text and a fixed room.

**A design with fewer than two fixed elements should expect to lose its identity**, and the studio
says so before building it rather than after. This is CREATIVE INFERENCE from the cases, not a law.

---

# 5. The techniques, with their purposes

| Technique | What it makes audible | Common failure |
|---|---|---|
| process music | a rule unfolding in time | the rule is inaudible, so it is just slow |
| phase shifting | two identical things separating and rejoining | shifted before the pattern was learned |
| chance operations | a structure nobody's taste chose | used to avoid deciding, then edited to taste |
| indeterminate form | performers' judgement as part of the piece | rules so vague they produce deadlock |
| musique concrète | a sound apart from its cause | the source stays recognisable and becomes a joke |
| spectral thinking | harmony derived from an actual spectrum | a chord chart labelled spectral |
| granular composition | the continuum between rhythm and timbre | a wash with no rate that matters |
| prepared instruments | a familiar instrument made strange | preparation with no consequence for the writing |
| noise | saturation, negation, the limit of listening | noise as a loudness setting |
| drone | tuning and duration, heard rather than passed through | a pad with no intonation decisions |
| sound collage | juxtaposition as argument | a playlist |
| field recording | a place, and attention to it | atmosphere behind music that ignores it |
| electroacoustic writing | instruments and their electronic shadows as one body | processing bolted on after |

---

# 6. Rule-based improvisation

Rule sets that work in practice share four properties:

1. they govern **relationships and attention**, not notes;
2. they give players a legible shared vocabulary of signals or actions;
3. they set a state of mind as well as a procedure;
4. they are few enough to hold while playing.

```yaml
rule_set:
  roles: []
  signals: []                  # how players communicate
  permitted_actions: []
  triggering_conditions: []    # what you must HEAR for an action to be available
  override_or_escape:          # how a stuck piece gets unstuck
  ending_condition:
  attention_instruction:       # what to listen for, not only what to do
```

Failure modes to check a rule set against: **vagueness** (nothing is decidable), **deadlock** (nobody
may move first), **dominance** (one role can override everything), **sterility** (the rules permit only
one outcome).

Pair each action instruction with an attention instruction. A rule set that says only what to do
produces parallel monologues.

---

# 7. Working with these in the studio

**Composer.** Chooses the family and writes the rules. Material is designed for the process, not
retrofitted: a pattern for phase shifting needs a shape whose displacement is audible.

**Performance Director.** A process piece's realism target is often `deliberately_mechanical`, and
that is a positive decision. A rule-based improvisation has no fixed performance plan by design; what
it has is the state of mind, which belongs in `performer_character`.

**Producer.** Sound-based work makes the Producer's timbre decisions the composition, not its clothing.
For drone and spectral work, timbre and tuning are one decision
(`shared/TUNING_AND_MPE.md`, section 6).

**Arranger.** Form may be a process or a state machine rather than sections. For state machines, use
`shared/ADAPTIVE_MUSIC.md`.

**Listener Model.** Expectation still applies, on a longer time scale. The question becomes: is there
enough repetition for the listener to learn the pattern before it changes? A process nobody can track
is not surprising, it is uniform.

**Music Critics.** Judge against the family's own standard. "Not memorable" is not a finding about a
piece whose purpose is attention to a room. "The rule is inaudible" is.

**Quality gate.** The identity, motif and hook questions in `shared/QUALITY_GATE.md` are answered
differently here, and answering them differently is not skipping them: a drone piece's identity is its
intonation and duration; its development may be a slow spectral change.

---

# 8. Honesty rules

- **Label chance as chance.** If material came from a chance operation and was then chosen by taste,
  it is a taste-chosen piece that used chance as a generator, and the studio says so.
- **Do not claim a process that was not run.** Describing music as if a system generated it when it
  was written by hand is a false statement about the work.
- **Log the realisation.** Seed, rule version and choices, so the piece can be repeated or varied on
  purpose.
- **Do not present a technique as radical because it is unfamiliar to the user.** Most of these are
  decades old and have a literature. Point at it (`research/ADAPTIVE_AND_EXPERIMENTAL.md`).
- **Ordinary music is not a lesser case.** A user who wants a chorus is not to be talked into a process
  piece.
