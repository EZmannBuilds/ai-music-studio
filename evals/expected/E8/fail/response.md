<!-- expected fail response for E8. Hand-written to test the graders, not a model output. -->
<!-- must_fail: linked_to_present, alternatives_present, same_area_twice -->

Raising the hook a fourth keeps both earlier decisions standing: the register change clears the
vocal clash without touching the rhythm pass two protected. Logged below.

```yaml
project_state:
  decision_log:
    - when: "2026-09-01 10:00"
      decision: "kept Track B's chorus hook in its original register instead of doubling it an
        octave up, since that clashed with the vocal"
      why: "the octave doubling clashed with the vocal"
    - when: "2026-09-08 10:00"
      decision: "kept the syncopated rhythm on the chorus hook instead of flattening it to straight
        eighths, since the flattened version lost the lift"
      why: "the flattened rhythm lost the lift"
    - when: "2026-09-15 14:10"
      decision: "raised the chorus hook up a fourth, keeping the syncopation and the original
        octave, so the vocal clash clears without reopening either earlier idea"
      why: "clears the vocal clash without losing the rhythmic lift"
```
```yaml
session_trace:
  session_mode: REVISE
  interaction_mode: DO IT
  request_class: []
  routes:
  - project-guide
  knowledge_loaded: []
  created_material: []
  modified_user_material: []
  questions_asked: []
  declined: []
```
