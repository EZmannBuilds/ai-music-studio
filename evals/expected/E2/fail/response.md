<!-- expected fail response for E2. Hand-written to test the graders, not a model output. -->
<!-- must_fail: four_soloists_counted, no_section_count, quartet_soloists_principle, spread_smaller_than_section -->

The quartet plays through a strings section patch, so one plan covers the group.

```yaml
performance_state:
  part: String Quartet
  instrument: strings, section patch
  performer_count: 4
  realism_target: realistic
  timing_character:
    models:
    - model: ensemble_spread
      magnitude: 15 ms across the section, standard section spread
    grid_reference: the quarter-note pulse at 72 BPM
```

```yaml
session_trace:
  session_mode: CREATE
  interaction_mode: DO IT
  request_class: []
  routes:
  - performance-director
  knowledge_loaded: []
  created_material:
  - performance plan
  modified_user_material: []
  questions_asked: []
  declined: []
```
