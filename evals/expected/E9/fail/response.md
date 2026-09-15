<!-- expected fail response for E9. Hand-written to test the graders, not a model output. -->
<!-- must_fail: collision_present, lines_named, overlap_addressed -->

Here's the chorus stack: harmony above the lead in bar 1, harmony below the lead in bar 2, and a
second backing line running alongside both.

```yaml
vocal_architecture:
  by_section:
  - section: chorus
    stacks:
    - voicing: [lead, harmony crossing above then below the lead, backing line 2]
      count: 3
      pan_plan: harmony center-right, backing line 2 center-left
      vowel: lyric
      purpose: lift the chorus
```

```yaml
session_trace:
  session_mode: CREATE
  interaction_mode: DO IT
  request_class: []
  routes:
  - vocal-director
  knowledge_loaded: []
  created_material:
  - vocal stack plan
  modified_user_material: []
  questions_asked: []
  declined: []
```
