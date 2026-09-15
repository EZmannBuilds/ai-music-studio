<!-- expected pass response for E3. Hand-written to test the graders, not a model output. -->

Bars 1 to 8: a stiff, clockwork ostinato. Exactness is the aesthetic here, not a defect to repair,
so the plan stays grid-exact. Several sections are playing together, which would normally be the
gate for an ensemble gesture, but the explicit mechanical request overrides that gate rather than
the gesture overriding the request: no ensemble_gesture is written, and no section leads or lags
another.

```yaml
performance_state:
  part: Full Orchestra Ostinato
  instrument: strings, woodwinds and brass in rhythmic unison
  realism_target: deliberately_mechanical
  articulation:
    default: marcato
  timing_character:
    models: []
    grid_reference: the sixteenth-note pulse at 132 BPM
  intentional_imperfections: []
```

```yaml
feasibility_report:
  part: Full Orchestra Ostinato
  impossible_voicings: []
  status: clear
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
  modified_user_material: []
  questions_asked: []
  declined: []
```
