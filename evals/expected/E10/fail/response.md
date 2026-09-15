<!-- expected fail response for E10. Hand-written to test the graders, not a model output. -->
<!-- must_fail: fatigue_named, fatigue_effect, imperfections_present -->

Trumpets and trombones hold a fortissimo unison line for bars 40 to 58, all notes full value, no
rests. The line sits comfortably in range for both sections throughout, so it is playable start to
finish exactly as written.

```yaml
performance_state:
  part: Trumpets and Trombones (brass section, bars 40-58)
  instrument: brass section
  performer_count: 8
  performer_character: precise
  realism_target: realistic
  articulation:
    default: sustained fortissimo
    by_section: {}
    switching: separate_patch
    map: {}
  dynamic_arc:
    control: cc11
    points:
    - {bar_beat: '40:1', value: 110}
    - {bar_beat: '58:4', value: 110}
    within_note: []
    note: on a crossfading library this changes timbre, not only level
  timing_character:
    models: []
    grid_reference: bar
    marker_parts_excluded: []
  intentional_imperfections: []
feasibility_report:
  part: Trumpets and Trombones
  status: clear
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
