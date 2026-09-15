<!-- expected pass response for D9. Hand-written to test the graders, not a model output. -->

Three states, one motif that survives all of them, and a failure that resolves rather than cuts.

```yaml
adaptive_music:
  project_type: game
  states:
  - name: explore
  - name: tension
  - name: combat
  transitions:
  - from: explore
    to: tension
    exit_at: next_bar
    latency_budget: one bar at 100 BPM
    why: a bar keeps phrasing
  motif_invariants:
  - the four-note horn call
  failure_states:
  - event: death
    behavior: resolve
  authored_endings:
  - victory tag
```
```yaml
session_trace:
  session_mode: CREATE
  interaction_mode: DO IT
  request_class: []
  routes:
  - arranger
  - composer
  knowledge_loaded:
  - shared/ADAPTIVE_MUSIC.md
  created_material:
  - adaptive plan
  modified_user_material: []
  questions_asked: []
  declined: []
```
