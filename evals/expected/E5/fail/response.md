<!-- expected fail response for E5. Hand-written to test the graders, not a model output. -->
<!-- must_fail: no_absurd_tempo -->

The sting has to land at 0:42.5, so the tempo ramps from 120 BPM up to 400 BPM for a single beat
right before bar 11, then drops straight back to 120 BPM once the frame is hit. The jump is jarring
against the surrounding material, but it puts the downbeat exactly on the timecode.

```yaml
timecode_cue:
  timecode: '0:42.5'
  nearest_grid_position: '11:1'
  fit_strategy: tempo_ramp
  hit_point_type: stinger
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
  - timecode cue
  modified_user_material: []
  questions_asked: []
  declined: []
```
