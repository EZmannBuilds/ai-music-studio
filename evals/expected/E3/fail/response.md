<!-- expected fail response for E3. Hand-written to test the graders, not a model output. -->
<!-- must_fail: no_gesture_smuggled_in -->

Bars 1 to 8: a clockwork ostinato, deliberately mechanical. Several sections are playing together,
so an ensemble gesture gives the entrance a touch of shape.

```yaml
performance_state:
  part: Full Orchestra Ostinato
  instrument: strings, woodwinds and brass in rhythmic unison
  realism_target: deliberately_mechanical
  timing_character:
    models: []
    grid_reference: the sixteenth-note pulse at 132 BPM
  intentional_imperfections: []
```

```yaml
ensemble_gesture:
  id: ostinato-entry
  type: accelerando
  origin_bar: 1
  target_bar: 8
  responses:
  - part: Strings
    lag_beats: 0
    curve: linear
    role: lead
  - part: Brass
    lag_beats: 2
    curve: delayed_onset
    role: follow
  why: giving brass a slightly later, softer entrance so the ostinato does not feel like a single
    stamped block
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
  - performance plan
  - ensemble gesture
  modified_user_material: []
  questions_asked: []
  declined: []
```
