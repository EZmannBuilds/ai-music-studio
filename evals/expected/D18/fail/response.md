<!-- expected fail response for D18. Hand-written to test the graders, not a model output. -->
<!-- must_fail: no_rewrite, user_material_untouched, options_offered, diagnosis_first, not_taken_over -->

## A better second verse

Here is the new second verse:

The ferry leaves at seven and I'm waiting like I did
The weather's getting colder and I'm standing by the door
I think about you often and I miss you every day

And the rest of the song, finished: after the second chorus, a bridge and a final chorus.
```yaml
session_trace:
  session_mode: CREATE
  interaction_mode: DO IT
  request_class: []
  routes:
  - lyric-generator
  knowledge_loaded: []
  created_material:
  - lyric
  modified_user_material:
  - what: verse 2
    on_copy: false
  questions_asked: []
  declined: []
```
