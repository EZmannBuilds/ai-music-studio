<!-- expected pass response for D2. Hand-written to test the graders, not a model output. -->

A dance-derived piece in 7/8 grouped 2+2+3, with the long beat always last. The long beat is not exactly one and a half short beats: in performance the short-to-long ratio varies, roughly between 1:1.3 and 1:1.6 depending on tempo and dancer, and the plan sets it per section.

```yaml
track_state:
  systems:
    rhythm_system:
      meter:
        cycle_length_pulses: 7
        beat_pattern:
        - 2
        - 2
        - 3
```
```yaml
session_trace:
  session_mode: CREATE
  interaction_mode: DO IT
  request_class: []
  routes:
  - composer
  knowledge_loaded:
  - shared/MUSICAL_SYSTEMS/ADDITIVE_METERS_BALKAN_TURKISH.md
  created_material:
  - melody
  - drum part
  modified_user_material: []
  questions_asked: []
  declined: []
```
