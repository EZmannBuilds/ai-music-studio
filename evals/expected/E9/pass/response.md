<!-- expected pass response for E9. Hand-written to test the graders, not a model output. -->

The harmony and the lead swap position between bar 1 and bar 2 — harmony above, then below — and the
second backing line sits in that same stretch of range for both bars. That is a real crossing, not
just movement, so here is the stack with it named and resolved rather than left to fight itself out.

```yaml
vocal_architecture:
  by_section:
  - section: chorus
    stacks:
    - voicing: [lead, harmony above the lead in bar 1 / below it in bar 2, backing line 2]
      count: 3
      pan_plan: harmony center-right, backing line 2 center-left
      vowel: lyric
      purpose: lift the chorus without crowding it
```

```yaml
collision_check:
  lines: [lead, harmony, backing line 2]
  register_overlap: full
  rhythmic_collision: bar 2 beat 1, where the harmony's drop lands on the same syllable as backing
    line 2
  intelligibility_risk: med
  resolution: reassign_register
```

The fix: keep the harmony's bar 1 position above the lead, but instead of letting it drop under the
lead in bar 2, move it up an octave so it stays above both other lines all the way through. Backing
line 2 keeps its range. That removes the full overlap without touching the lead.

```yaml
session_trace:
  session_mode: CREATE
  interaction_mode: DO IT
  request_class: []
  routes:
  - vocal-director
  knowledge_loaded: []
  created_material:
  - vocal stack plan
  - collision check
  modified_user_material: []
  questions_asked: []
  declined: []
```
