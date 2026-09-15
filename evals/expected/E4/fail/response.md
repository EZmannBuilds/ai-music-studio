<!-- expected fail response for E4. Hand-written to test the graders, not a model output. -->
<!-- must_fail: diverse_tones -->

Bar 12's chord is a C major triad, split a2 across the sixteen violins.

```yaml
voicing:
  chord_ref: Composer chord event bar 12, C major
  distribution:
    - instrument_group: Violin I, desks 1-4 (8 players)
      voice_count: 1
      tone_assigned: root
      register: C5
      doubling_of: []
    - instrument_group: Violin I, desks 5-8 (8 players)
      voice_count: 1
      tone_assigned: root
      register: C5
      doubling_of: []
  divisi_reason: unison_strength
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
  - voicing distribution
  modified_user_material: []
  questions_asked: []
  declined: []
```
