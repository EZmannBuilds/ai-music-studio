# Fusion Protocol
## Version 1.0

Combining musical worlds by function, with a reason they belong together.

Executed by `creative-lab/SKILL.md`, using decompositions from `reference-analyst/SKILL.md`. Read by
Composer, Arranger, Producer and Music Critics.

This extends the Reference Analyst's opportunity space from "traits not present in any one reference"
into a method with a gate.

---

# 1. What fusion is not

```text
Genre A + Genre B = both at once
```

That is a blend, and it produces music where one genre supplies the structure and the other supplies
decoration, usually instruments. The decorative side is interchangeable, which is the tell.

---

# 2. Step 1: decompose each source by function

Not by style. By what each element **does**.

```yaml
source_decomposition:
  source:                      # a genre, a tradition, an artist's practice, a specific record
  rhythm_logic:                # what organises time
  harmonic_principle:          # what governs pitch relations, or what replaces harmony
  form_philosophy:             # what makes a piece end where it ends
  texture_behavior:            # what the layers do to each other
  performance_practice:        # how it is played, and by whom
  production_behavior:         # what the record does that the performance does not
  what_is_identity:            # the parts that are this and nothing else
  what_is_convention:          # the parts shared with its neighbours
  evidence:                    # observed, documented, or inferred
```

The last two fields decide what may be borrowed. Conventions travel. Identity does not: taking the
identity is imitation, not fusion.

---

# 3. Step 2: name the bridge. This is a gate.

**A fusion needs an element both sides already own.** Documented successful hybrids share this: a
rhythmic cycle present in both, a mode both use, an instrument whose physics suits both, a shared
history, or an audience that already listens to both. And they involve a person with standing in both
traditions, through training, residence, collaboration or invitation
(`research/ADAPTIVE_AND_EXPERIMENTAL.md`, section 7).

```yaml
bridge:
  element:                     # the thing both sides already have
  kind: rhythmic | modal | instrumental | historical | audience | textual
  evidence:                    # why this is true, not a convenient assertion
  human_bridge:                # who has standing in both, and how. May be "none".
  status: named | absent
```

**If `status: absent`, stop.** The options are: find a real bridge, find a partner, or do not make
this fusion. The studio says so plainly rather than producing the piece and adding a disclaimer.

A bridge is not a justification written after the fact. "Both have drums" is not a bridge.

---

# 4. Step 3: assign carriers

```yaml
carriers:
  rhythm_logic:                # which source supplies it
  harmonic_principle:
  form_philosophy:
  texture_behavior:
  performance_practice:
  production_behavior:
  melody:                      # new, always
  check: "no single source may carry rhythm, harmony and form"
```

If one source carries rhythm, harmony and form, it is not a fusion. It is that genre with guests.

**The melody is new.** This is the same rule the studio applies to every reference: principles
transfer, identifiable musical objects do not.

---

# 5. Step 4: the provenance check

```yaml
provenance:
  traditions_involved: []
  source_musicians_credited: []
  source_musicians_consulted: []     # and whether they were paid
  recordings_sampled: []             # of whom, with what permission
  restricted_repertoire_avoided: true | false
  how_this_will_be_described:        # the words used publicly; "inspired by" hides a lot
  concerns: []
```

The failure case in the critical literature is specific: a recording of people who are not partners is
sampled or imitated, the sound is detached from the people, and the attribution and the money go
elsewhere. An agent is unusually exposed here, because it can produce a tradition's surface markers
with nobody from that tradition in the room.

Standing rules:

- decline "in the style of" for sacred, ceremonial or community-restricted repertoire;
- never sample a field recording of identifiable people who are not party to the work;
- name the tradition precisely, and never a continent or "world";
- where the user is working inside their own tradition, say so and get out of the way.

---

# 6. Step 5: the strip test

```yaml
strip_test:
  - removed:                   # one source's contribution
    what_survives:
    verdict: load_bearing | decorative
```

Remove each source's contribution in turn. If the piece survives intact without one of them, that one
was decoration. Either make it load-bearing or drop the claim that this is a fusion.

---

# 7. The case card

What a finished fusion carries, so a listener or a collaborator can see the reasoning.

```yaml
fusion_case:
  sources: []
  bridge:
  carriers: {}
  what_changed_on_each_side:   # a real fusion changes both; a graft changes one
  new_material: []
  provenance: {}
  strip_test: {}
  how_to_describe_it:
```

---

# 8. Worked shape

```text
SOURCES     a cyclic timeline tradition; a chamber-string writing practice

BRIDGE      both organise time as a fixed cycle against which parts are heard, and both
            treat the cycle's reference point as an arrival rather than a start
            human bridge: the user studied one and plays in the other

CARRIERS    rhythm logic      from the timeline tradition
            harmonic principle from the string practice (voice leading between few parts)
            form philosophy   from the timeline tradition (cycles, not sections)
            texture behavior  from the string practice (independent lines, not chords)
            production        neither: dry, close, one room
            melody            new

STRIP TEST  remove the timeline: the strings become a slow chamber piece. Load-bearing.
            remove the string writing: the cycle becomes a percussion loop. Load-bearing.

CHANGED     the strings stop playing in bars; the cycle acquires voice leading it did not have
```

---

# 9. What this protocol does not do

- It does not authorise. A completed case card is not consent from anybody.
- It does not make a hybrid good. It makes it coherent and honest.
- It does not apply to working inside one tradition, which needs no bridge.
- It does not settle the wider argument about appropriation. It makes the studio's part of it
  explicit, and gives the user the information to decide.
