<!-- expected fail response for E7. Hand-written to test the graders, not a model output. -->
<!-- must_fail: no_ensemble_gesture, no_role_assignment, no_orchestral_vocabulary -->

For the chorus, I'll write an ensemble gesture so the four parts build together, and give each layer
a role_assignment so the drums, bass, lead and vocal divide the work the way an orchestral/electronic
hybrid would.

```yaml
session_trace:
  session_mode: CREATE
  interaction_mode: BUILD SOMETHING NEW
  request_class: []
  routes:
  - arranger
  knowledge_loaded: []
  created_material:
  - chorus arrangement
  modified_user_material: []
  questions_asked: []
  declined: []
ensemble_gesture:
  id: g1
  type: crescendo
  origin_bar: 17
  target_bar: 24
  responses:
  - part: drum machine
    lag_beats: 0
    curve: linear
    role: lead
  - part: synth bass
    lag_beats: 1
    curve: linear
    role: follow
  why: bring the chorus in with a shared build
role_assignment:
- bar_range: 17-24
  role: pulse
  instruments:
  - drum machine
- bar_range: 17-24
  role: color
  instruments:
  - synth lead
```

This uses divisi-style role_assignment reasoning to spread the synth pad across register bands.
