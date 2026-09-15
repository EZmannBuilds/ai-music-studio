<!-- expected pass response for E4. Hand-written to test the graders, not a model output. -->

Bar 12's chord is a C major triad. With the section split a2, the two violin groups each carry a
different tone of it instead of both doubling the same note: the first group holds the root, the
second the third, both inside a comfortable sustained register for eight-desk violin I.

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
      tone_assigned: third
      register: E5
      doubling_of: []
  divisi_reason: tone_distribution
```
```yaml
session_trace:
  session_mode: CREATE
  interaction_mode: DO IT
  request_class: []
  routes:
  - arranger
  knowledge_loaded:
  - shared/ORCHESTRAL_VOICING_SCHEMA.md
  created_material:
  - voicing distribution
  modified_user_material: []
  questions_asked: []
  declined: []
```
