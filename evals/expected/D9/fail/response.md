<!-- expected fail response for D9. Hand-written to test the graders, not a model output. -->
<!-- must_fail: latency, invariants, failure, endings -->

Three loops, and the game cuts between them.

```yaml
adaptive_music:
  states:
  - name: a
  - name: b
  - name: c
  transitions:
  - from: a
    to: b
    exit_at: immediate
```
```yaml
session_trace:
  session_mode: CREATE
  interaction_mode: DO IT
  request_class: []
  routes:
  - arranger
  knowledge_loaded: []
  created_material:
  - loops
  modified_user_material: []
  questions_asked: []
  declined: []
```
