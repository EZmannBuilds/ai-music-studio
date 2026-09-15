<!-- expected pass response for E2. Hand-written to test the graders, not a model output. -->

Four soloists, not a strings section wearing four track names. A quartet is four soloists, so each
part carries `performer_count: 1`, and the spread between them is smaller and more deliberate than
a section's ensemble spread, because four players listening to each other agree closely and lead
each other on purpose.

```yaml
performance_state:
  part: Violin I
  instrument: violin, solo
  performer_count: 1
  realism_target: realistic
  timing_character:
    models:
    - model: ensemble_spread
      magnitude: 6 ms across the four players, smaller and more deliberate than a section's
        typical 12-20 ms spread
    grid_reference: the quarter-note pulse at 72 BPM
```

```yaml
performance_state:
  part: Violin II
  instrument: violin, solo
  performer_count: 1
  realism_target: realistic
  timing_character:
    models:
    - model: ensemble_spread
      magnitude: 6 ms across the four players, following the first violin's lead by a few
        milliseconds
    grid_reference: the quarter-note pulse at 72 BPM
```

```yaml
performance_state:
  part: Viola
  instrument: viola, solo
  performer_count: 1
  realism_target: realistic
  timing_character:
    models:
    - model: ensemble_spread
      magnitude: 6 ms across the four players
    grid_reference: the quarter-note pulse at 72 BPM
```

```yaml
performance_state:
  part: Cello
  instrument: cello, solo
  performer_count: 1
  realism_target: realistic
  timing_character:
    models:
    - model: ensemble_spread
      magnitude: 6 ms across the four players, anchoring the bottom of the ensemble
    grid_reference: the quarter-note pulse at 72 BPM
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
  - shared/VIRTUAL_INSTRUMENT_GUIDE/STRINGS.md
  created_material:
  - performance plan
  modified_user_material: []
  questions_asked: []
  declined: []
```
