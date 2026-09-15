<!-- expected fail response for E1. Hand-written to test the graders, not a model output. -->
<!-- must_fail: diverse_curves, diverse_roles -->

Bars 1 to 24: the whole orchestra builds together, so every choir gets the same crescendo shape,
just started a little later than the last.

```yaml
ensemble_gesture:
  id: buildup-1-24
  type: crescendo
  origin_bar: 1
  target_bar: 24
  responses:
  - part: Strings
    lag_beats: 0
    curve: linear
    role: follow
  - part: Woodwinds
    lag_beats: 4
    curve: linear
    role: follow
  - part: Brass
    lag_beats: 8
    curve: linear
    role: follow
  - part: Percussion
    lag_beats: 12
    curve: linear
    role: follow
  why: the whole orchestra rises together into the tutti
```

```yaml
session_trace:
  session_mode: CREATE
  interaction_mode: DO IT
  request_class: []
  routes:
  - performance-director
  knowledge_loaded:
  - shared/HUMAN_PERFORMANCE_SCHEMA.md
  created_material:
  - ensemble gesture
  modified_user_material: []
  questions_asked: []
  declined: []
```
