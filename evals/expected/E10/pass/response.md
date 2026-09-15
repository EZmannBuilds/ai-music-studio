<!-- expected pass response for E10. Hand-written to test the graders, not a model output. -->

Nineteen bars at fortissimo with no rests is past what a brass section can sustain evenly. Bars 40-47
hold full tone. From bar 48 the sound starts to give: the trumpets thin first, since they are working
hardest against the least air reserve, and by bar 54 there is a slight sag toward flat on the held
notes as embouchures tire. Trombone entries after bar 55 land a hair late, a beat where the section is
no longer attacking cleanly together. This is `performer_fatigue`, not a range or tessitura problem —
the passage sits well inside both sections' ranges throughout; it is endurance across nineteen bars
that runs out, not the notes themselves.

```yaml
performance_state:
  part: Trumpets and Trombones (brass section, bars 40-58)
  instrument: brass section
  performer_count: 8
  performer_character: driving, pushed to the edge of endurance
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
    - {bar_beat: '48:1', value: 108}
    - {bar_beat: '58:4', value: 96}
    within_note: []
    note: on a crossfading library this changes timbre, not only level
  timing_character:
    models:
    - phrase_arch
    grid_reference: bar
    marker_parts_excluded: []
  intentional_imperfections:
  - what: performer_fatigue
    why: endurance is finite, and a long loud passage tires
    magnitude: tone thins from bar 48; pitch sags roughly 5-10 cents flat on held notes from bar 54;
      trombone entries land 15-30 ms late from bar 55
    applies_to: bars 48-58, trumpets and trombones
feasibility_report:
  part: Trumpets and Trombones
  breath_or_bow_overruns:
  - 'bars 40-58: 19 bars with no rest exceeds a single breath; staggered breathing assumed'
  status: flags
```
```yaml
session_trace:
  session_mode: CREATE
  interaction_mode: DO IT
  request_class: []
  routes:
  - performance-director
  knowledge_loaded:
  - shared/VIRTUAL_INSTRUMENT_GUIDE/BRASS.md
  created_material:
  - performance plan
  modified_user_material: []
  questions_asked: []
  declined: []
```
