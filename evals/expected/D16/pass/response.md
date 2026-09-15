<!-- expected pass response for D16. Hand-written to test the graders, not a model output. -->

Sixteen bars of cello, planned so every deviation has a reason a cellist would recognise.

```yaml
performance_state:
  part: Cello
  instrument: solo cello
  realism_target: realistic
  articulation:
    default: legato
    by_section:
      bars 1-8: legato
      bars 9-16: detache
  dynamic_arc:
    control: continuous dynamics
    points:
    - bar_beat: '1:1'
      value: pp
    - bar_beat: '12:1'
      value: mf
    - bar_beat: '16:4'
      value: p
  timing_character:
    models:
    - model: phrase_arch
      magnitude: 2% tempo lean into phrase ends
    - model: final_ritard
      magnitude: last two bars
  note_overlap:
    legato_overlap_ms: 60
  intentional_imperfections:
  - what: bow_change
    why: the slow music exposes it
```
```yaml
feasibility_report:
  part: Cello
  impossible_voicings: []
  limb_or_finger_conflicts: []
  out_of_range: []
  breath_or_bow_overruns: []
  articulation_unavailable: []
  simultaneity_exceeded: []
  intentional_exceptions: []
  status: clear
```
```yaml
session_trace:
  session_mode: CREATE
  interaction_mode: DO IT
  request_class: []
  routes:
  - composer
  - performance-director
  - midi-builder
  knowledge_loaded:
  - shared/VIRTUAL_INSTRUMENT_GUIDE/STRINGS.md
  created_material:
  - cello part
  - performance plan
  modified_user_material: []
  questions_asked: []
  declined: []
```
