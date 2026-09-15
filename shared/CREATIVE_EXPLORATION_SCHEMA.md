# Creative Exploration Schema
## Version 1.0

The structure the Creative Lab uses to produce directions that differ by **mechanism**.

Written by `creative-lab/SKILL.md`. Read by the Music Director when choosing, and by Composer,
Arranger, Producer and Vocal Director when carrying a chosen candidate forward.

---

# 1. Why mechanism

Creativity research distinguishes searching **inside** a space defined by a style's rules from
changing or dropping one of those rules so that new results become reachable
(`research/CREATIVITY_AND_PEDAGOGY.md`, section 1).

Five chord progressions are five points in one space. They are variants. To be a different direction,
a candidate has to change the space: a different pitch organisation, a different rhythmic logic, a
different form grammar, a different performance constraint, a different process.

So the Lab **states the current space as rules first**, then breaks or replaces them on purpose.

---

# 2. `creative_exploration`

The frame for a round of exploration.

```yaml
creative_exploration:
  brief_summary:               # what the task actually is
  current_space:               # the rules as they stand, stated explicitly. 5-8 of them.
    - rule:                    # e.g. "harmony is a 4-bar loop of diatonic triads"
      dimension:               # which dimension it governs, from section 3

  temperature: safe | exploratory | radical
  familiarity_anchor:          # what stays recognisable across every candidate
  dimensions_to_preserve: []   # from section 3
  dimensions_to_break: []      # from section 3, or from a diversity comparison
  constraint:
    precludes:                 # the habitual move this forbids. Required.
    promotes:                  # what it pushes the work toward instead. Required.
  rule_to_break:               # which rule from current_space is being dropped or inverted
  novelty_source:              # where the newness comes from
  risk:                        # what could go wrong musically
  reversibility: easy | moderate | hard     # how much work it is to back out
  ledger_input: {}             # dimensions the ledger says are stale
```

**Temperature is a preference dial, not a quality axis.** Evidence for "more novelty is better" in
music is mixed at best, and familiarity often wins (`research/CREATIVITY_AND_PEDAGOGY.md`, section 3).
`safe` is a legitimate setting and the Lab never treats `radical` as the better answer. With no
temperature given, use `exploratory` and say so.

**Constraints are pairs.** A constraint that forbids nothing is not a constraint. The user chooses or
accepts it: the Lab proposes, the user imposes. Imposed-from-outside constraints can reduce creative
output, which is why this ordering matters rather than being a formality.

---

# 3. The dimensions

A candidate must differ from every other candidate on at least **two** of these.

| Dimension | What changing it means |
|---|---|
| `premise` | what the piece is about or for |
| `form` | how time is organised: sections, cycles, process, states |
| `pitch_organization` | tonal, modal, maqam, raga, drone, set-based, microtonal, absent |
| `rhythmic_logic` | metre type, cycle, subdivision, polymetric layering, free time |
| `harmonic_mechanism` | how chords move, or whether there are chords |
| `performance_constraint` | who plays, with what limits, how well, how many |
| `arrangement_logic` | what enters, what leaves, what carries the piece |
| `production_behavior` | the sonic rule the record follows |
| `compositional_process` | how the material is generated: written, process, chance, rule-based |
| `lead_source` | what the listener follows |

---

# 4. `exploration_candidate`

```yaml
exploration_candidate:
  label:                       # A, B, C - short, not a title
  one_line:                    # what this is, in a sentence a musician would understand

  anchor:                      # what is familiar here
  dimensions_changed: []       # at least two, from section 3
  mechanism:                   # HOW it differs, not what it sounds like
  constraint:                  # the preclude/promote pair active in this candidate
  novelty_source:

  sketch:                      # enough to judge it: a progression, a groove, a form map, a process
  what_changes_downstream:     # what Composer, Arranger, Producer, Vocal Director would each do
  what_it_costs:               # what this makes harder or impossible
  risk:
  reversibility: easy | moderate | hard
  differs_from_others_by: {}   # candidate label -> the dimensions that separate them
  differs_from_ledger_by: []   # which stale dimensions this actually breaks
  system_context:              # if it draws on shared/MUSICAL_SYSTEMS/, which file and its cautions
```

---

# 5. The set test

A round of candidates passes when:

1. every candidate differs from every other on **two or more dimensions**;
2. no candidate is another transposed, revoiced, retempoed or reorchestrated;
3. the mechanisms are genuinely different, not the same mechanism described differently;
4. at `safe` temperature the anchor is intact in all of them, and they still differ by mechanism;
5. at `radical` temperature every candidate still names its reversibility;
6. where the ledger supplied stale dimensions, at least one candidate breaks each of them;
7. any candidate drawing on a named musical tradition carries that file's context and cautions.

A set that fails is regenerated, not shipped with an apology.

---

# 6. Worked shape

The point of the example is that the four candidates cannot be reduced to each other.

```text
Brief: a short piece, voice and one other thing, "held together by something fragile"

Current space:
  harmony is a looped diatonic progression
  the voice enters at the top and carries the melody throughout
  a drum part keeps time
  sections are 8 bars

A  anchor: the voice                 novelty: harmony
   constraint: precludes drums, promotes breath and room as the pulse
   mechanism: harmonic rhythm slows until chords become drones; time is kept by breathing

B  anchor: the bass                  novelty: form
   constraint: precludes any repeated 8-bar section, promotes continuous variation
   mechanism: a bass line that is never the same length twice, so the voice is always arriving early

C  anchor: a percussion cycle        novelty: tuning
   constraint: precludes 12-tone equal temperament, promotes a small just subset
   mechanism: the cycle stays fixed while the pitch material narrows to beating intervals

D  anchor: texture                   novelty: performance
   constraint: precludes melody before the midpoint, promotes accumulating noise components
   mechanism: fret, breath and key noise become the material; the melody is the last event
```

---

# 7. Handoff

```yaml
exploration_handoff:
  candidates: []
  recommendation:              # the best fit for the brief, with a reason
  alternatives_worth_keeping: []
  user_choice:                 # recorded once the user picks; empty until then
  carried_constraints: []      # the constraints that now bind downstream specialists
```

The Lab recommends. The Director and the user choose. Once chosen, the candidate's constraints are
real: a candidate that precluded drums does not quietly acquire drums at the production stage, and if
it needs them, that is a decision to surface, not to make quietly.
