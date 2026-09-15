# Human Performance Schema
## Version 1.0

The representation that carries performance decisions from the Composer's notes to a rendered part.

```text
Composer / Arranger          notes, phrasing intent, register
        ↓
Performance Director         performance_state, one per part
Vocal Director               performance_state for voices
        ↓
MIDI Builder                 executes it: velocities, lengths, controller lanes, per-note expression
        ↓
DAW adapter                  automation lanes, articulation switches, tuning
        ↓
Mix Engineer                 reads the intended dynamic shape before touching a fader
```

**MIDI Builder executes this plan. It does not invent expression.**

## Which director writes which plan

```text
the voice, sung or spoken          Vocal Director
everything else                    Performance Director
```

Two cases worth settling, because both come up constantly:

- **A vocal guide played by an instrument** follows the Vocal Director's plan. The part is a voice
  that has not been recorded yet; the flute or synth standing in for it should breathe and phrase
  where the singer will, or the guide teaches the wrong thing to whoever plays it later.
- **A wordless vocal used as a texture**, for example a choir written as an orchestral colour with no
  lyric, is the Vocal Director's if a person sings it and the Performance Director's if it is
  functioning as an instrument the user does not think of as a voice. The deliverable mode decides
  the practical question, which is whether an instrumental export mutes it: the Vocal Director
  declares that per track (`shared/VOCAL_ARCHITECTURE_SCHEMA.md`), and where no plan exists the
  Director asks once and records the answer.

**With no performance plan at all**, MIDI Builder writes plain quantised notes and labels the artifact
`unperformed` (section 6). That is an honest deliverable. An artifact full of invented expression is
not.

---

# 1. The rule this schema exists to enforce

```text
ORGANIC PERFORMANCE
IS NOT
RANDOM HUMANIZATION.
```

Research on microtiming finds that systematic deviations at natural magnitude are roughly as pleasing
as an exact grid, that exaggerated deviation is liked less, and that where looseness is preferred it
has long-range structure rather than being white noise
(`research/PERFORMANCE_AND_EXPRESSION.md`, sections 1 and 3).

**Those studies used short loops, mostly rock and funk stimuli, and mostly Western listeners.** The
research page says so plainly: "quantised rates highest" is a finding about those stimuli, not a law.
Jazz, samba, Malian drumming and neo-soul have documented systematic feels that a grid does not
produce.

What survives the scoping, and what this schema is built on, is narrower and firmer: **a uniform
random offset is not a weak version of a human one.** Human timing is structured and reproducible.
Modelling the structure is available in every style; scattering notes is available in none.

So this schema **has no field named random**, and no field whose value is "amount of humanization".
Every deviation comes from a named model that another specialist can read, argue with, and reproduce.
A deviation with no model is a bug.

---

# 2. `performance_state`

One record per part. Populate what the task needs.

```yaml
performance_state:
  part:                        # the track or voice this describes
  instrument:                  # family and, where known, the assigned instrument
  performer_count: 1           # 1 for solo; a number for a section; affects spread and vibrato
  performer_character:         # e.g. precise, laid_back, driving, ragged, ceremonial, machine
  realism_target: realistic | stylised | deliberately_mechanical
  performance_reference:       # optional, added in 2.1: whose practice the plan follows
    tradition:                 # e.g. Hindustani, Ewe dance-drumming; see shared/MUSICAL_SYSTEMS/
    school_or_lineage:         # a gharana, a regional style, a named teacher's practice, or "unknown"
    repertoire:                # the piece or genre the plan is modelled on
    basis:                     # the source: a guide page, a research record, a named recording

  articulation:
    default:                   # the articulation most notes use
    by_section: {}             # section -> articulation, where it changes
    switching: separate_patch | keyswitch | cc | velocity | host_parameter | none
    map: {}                    # articulation -> how it is selected on this instrument

  phrase:
    boundaries: []             # bar:beat positions where a phrase begins
    breath_or_bow_changes: []  # where the player must breathe, change bow, or re-pick
    longest_phrase_seconds:    # checked against the instrument's limit
    shape: []                  # per phrase: rise, fall, arch, terraced, flat

  dynamic_arc:
    control: velocity | cc1 | cc11 | cc7 | host_parameter | per_note_expression
    points: [{bar_beat:, value:}]
    within_note: []            # swells and decays inside long notes
    note: "on a crossfading library this changes timbre, not only level"

  timing_character:
    models: []                 # from section 3; each entry names its model and magnitude
    grid_reference:            # the pulse or cycle offsets are measured against
    marker_parts_excluded: []  # bell, gong, clap, clave: never displaced
    gesture_ref:                # optional: id of an ensemble_gesture (section 8) this part responds to

  note_overlap:
    legato_overlap_ms:         # positive where the patch needs overlap to trigger a transition
    separation_ms:             # negative space for detached playing
    pedal:                     # for pedalled instruments, as a curve, not a switch

  accent_pattern:
    metrical: []               # accents by position in the bar or cycle
    structural: []             # accents that mark form
    ghost_notes: []            # where, and with which sample or technique

  vibrato:
    kind: none | finger | breath | hand | motor
    onset: immediate | delayed | growing
    control:                   # how it is driven on this instrument
    by_phrase: []              # vibrato is a phrase decision, not a constant

  portamento_and_bends:
    kind: none | portamento | slide | bend | pitch_gesture
    range_cents:
    implementation: sampled_transition | per_note_bend | channel_bend | mts
    note: "declare the bend range wherever bend data is written"

  physical_constraints:
    limbs_or_fingers:          # e.g. 4 limbs, 8 usable fingers, one note per string
    reach:                     # hand span, fret span, string set
    breath_seconds:
    simultaneity_limit:        # how many notes can sound at once, honestly

  intentional_imperfections:
    - what:                    # from section 4
      why:                     # the musical or physical reason. Required.
      magnitude:               # with units
      applies_to:              # which notes or sections

  automation_controls:         # what the DAW adapter has to write
    - target: cc | host_parameter | per_note | tempo
      name:
      curve: [{bar_beat:, value:}]

  virtual_instrument_translation:
    guide_file:                # shared/VIRTUAL_INSTRUMENT_GUIDE/<FAMILY>.md
    calibration_profile_id:    # or "unmeasured"
    known_limits: []           # what this patch cannot do, from the audit
```

`performance_reference` answers the first question the culturally specific instruments protocol asks
(`shared/VIRTUAL_INSTRUMENT_GUIDE/CULTURALLY_SPECIFIC_INSTRUMENTS.md`, step 0): whose practice is
this? A plan for a tabla part that says "Lucknow gharana, accompanying a khayal, from the guide's
TABLA page" can be checked; one that says "tabla" cannot. It is optional, and older plans without it
are unaffected.

---

# 3. Timing models

`timing_character.models` accepts only entries from this table. Each has a documented basis in
`research/PERFORMANCE_AND_EXPRESSION.md` and a magnitude with units.

| Model | What it does | Magnitude | Basis, and the corpus it came from |
|---|---|---|---|
| `phrase_arch` | tempo and dynamics shaped over a phrase, often slower and softer at the ends | no general figure exists; set it per style and record what you set | Todd 1992, described for some classical and romantic piano styles |
| `final_ritard` | parabolic slowing at a structural end | no general figure; the *shape* is the finding, not a depth | Repp 1992, 28 performances of one romantic piano piece |
| `metrical_accent` | accent and slight lengthening by position in the bar or cycle | small | KTH rule system, Western art music |
| `chord_asynchrony` | the louder note of a chord arrives first | the studies report roughly 20-50 ms, clustering near 30 ms, **at the hammer on a piano** | Palmer 1997, Repp 1996, Goebl 2001. Goebl shows it is a consequence of the action, so do not copy the figure to any other instrument |
| `section_offset` | one constant offset between parts, held across a section | no general figure; derive it from the style, or measure it | Friberg & Sundström 2002 found jazz soloists' downbeats lagging the drums with offbeats roughly synchronous. That is the mechanism; the amount is not transferable |
| `swing_ratio` | long-short ratio as a function of tempo | about 3.5:1 at slow tempi to 1:1 at fast, **jazz ride cymbal** | Friberg & Sundström 2002. Not a general fact about rhythm. Other traditions have their own ratios: see `shared/RHYTHM_SYSTEMS/MICROTIMING_AND_GROOVE.md` |
| `microtiming_template` | per-position offsets from a named corpus | 1-5% of the beat; the studied corpora cluster nearer 1-3% | `shared/RHYTHM_SYSTEMS/MICROTIMING_AND_GROOVE.md`, which requires the corpus to be named |
| `ensemble_spread` | several players do not attack at one instant | no measured figure is available in this pack; state and label whatever you use, or calibrate | musicianship |
| `drift_1f` | small long-range-correlated wander, applied last and least | smallest layer of the plan | Hennig 2011, and a drum-track analysis in Räsänen 2015 |
| `accelerando` | tempo rises across a marked span, usually toward a goal | no general figure; the *shape* is the finding, not a rate | Todd 1992, the same phrase-arch literature read for its rising rather than falling half |
| `ritardando_free` | tempo pulls back somewhere inside a phrase, for expressive reasons, without a structural end to arrive at (distinct from `final_ritard`, which is the parabolic shape at a structural close) | no general figure exists; set it per style and record what you set | Repp 1992 describes the family of expressive tempo curves this draws from; this row is the free, non-terminal member of it |
| `fermata` | a held note or rest outstays its written value before the next pulse resumes | no general figure; the hold is a performed decision, not a measured duration | KTH rule system's treatment of fermata as a notated event with a performer-chosen length, not a rubato by-product |
| `caesura` | a brief silence breaks the pulse between two phrases; the next phrase begins from a fresh clock | no general figure; the gap is authored, not derived from a tempo curve | KTH rule system, where the caesura is a distinct notated event from a ritardando |
| `tempo_reset` | after a structural tempo change (a new section, a written tempo mark), the pulse resumes at the new value rather than drifting into it | no general figure; the point of the model is the discontinuity, not a rate | musicianship: this is the row that keeps `phrase_arch` and `final_ritard` from bleeding across a section boundary they do not govern |

**Nine of these models have no number, and that is the honest state of the evidence.** `phrase_arch`,
`final_ritard`, `section_offset`, `ensemble_spread`, `accelerando`, `ritardando_free`, `fermata`,
`caesura` and `tempo_reset` are shapes and mechanisms rather than quantities. Set a value for the
style, write it into the plan, and label it as set rather than measured. Do not borrow a figure from a
neighbouring row: they come from different instruments and different repertoires.

**Where a figure exists, it belongs to a corpus.** A jazz ride cymbal's swing curve, a piano action's
chord asynchrony and a samba sixteenth template are three measurements of three things. None of them
is a general law of performance.

Rules:

- **Natural magnitude is the ceiling.** Scaling past what players do scales into the region listeners
  liked least.
- `drift_1f` is applied last and is the smallest contribution, mirroring the position of performance
  noise in the KTH rule system.
- Marker instruments named in `marker_parts_excluded` receive no timing model at all. They are the
  reference everything else is heard against.
- `chord_asynchrony` is derived from the voicing and the velocities, not stored as a fixed number, and
  it is not copied from a keyboard part to a non-keyboard part.
- **`ensemble_spread` follows the ensemble, not the patch.** A quartet is four soloists, so each part
  carries `performer_count: 1`, and the spread between them is still real and is usually *smaller and
  more deliberate* than a section's: four players listening to each other agree closely and lead each
  other on purpose. A section patch playing one line is the other case, where the spread is recorded
  into the samples and adding more on top double-counts it. Decide which case you are in and say so
  in the plan.

---

# 4. Intentional imperfections

Each entry needs a cause. These are the causes the studio recognises; anything else has to argue for
itself in the `why` field.

| `what` | `why` |
|---|---|
| `melody_lead` | the louder note reaches the string first |
| `phrase_arch` | players breathe and lean across a phrase |
| `final_ritard` | a structural end is approached, not arrived at |
| `double_spread` | two takes are never identical |
| `ensemble_spread` | a section is many players |
| `swing_ratio` | the style's long-short feel at this tempo |
| `drift_1f` | human timing wanders with long-range correlation |
| `fret_noise`, `bow_change`, `breath`, `pick_noise`, `key_noise` | the instrument makes these sounds |
| `velocity_asymmetry` | a hand does not strike evenly, and voicing is intentional |
| `note_length_variation` | releases are decisions |
| `flam` | two limbs arriving fractionally apart |
| `pitch_drift`, `tape_wow`, `tape_flutter` | an unstable pitch source or transport |
| `performer_fatigue` | endurance is finite, and a long loud passage tires |

**`realism_target: deliberately_mechanical` produces an empty `intentional_imperfections` list, and
says so.** Exactness is a legitimate aesthetic. A style built on the grid is not a defect to repair.

---

# 5. `feasibility_report`

Returned with the plan, before anything is written.

```yaml
feasibility_report:
  part:
  impossible_voicings: []      # e.g. six notes on a six-string guitar with a stretch of nine frets
  limb_or_finger_conflicts: [] # e.g. three simultaneous hand strikes plus a foot hi-hat
  out_of_range: []             # pitch, bar:beat, and the range it exceeds
  breath_or_bow_overruns: []   # phrases longer than the player can sustain
  articulation_unavailable: [] # asked for, not present in this instrument
  simultaneity_exceeded: []    # more notes at once than the instrument has voices or hands
  intentional_exceptions: []   # the brief wants the impossible; recorded, not silently allowed
  status: clear | flags | blocked
```

**Whoever wrote the plan writes its feasibility report.** So the Vocal Director produces it for the
voice: a stack above the singer's declared range, a phrase with no breath in it, a line that needs a
register the singer does not use. The Performance Director produces it for everything else. Neither
checks the other's parts, and neither leaves the voice out on the assumption that the other did it.

An impossible part can still be written. What is not allowed is writing it **silently**. The
Director sees the report, and the user decides whether the physical world applies to this track.

---

# 6. Contract with MIDI Builder and the DAW adapter

MIDI Builder:

- reads `dynamic_arc.control` and writes to that control, not to whichever one is habitual;
- applies `note_overlap.legato_overlap_ms` so monophonic legato patches actually trigger transitions;
- applies the velocity floor and minimum note length from the calibration profile **after** the
  performance plan, and reports where the two conflict rather than silently overriding the plan;
- writes `automation_controls` it can carry in a Standard MIDI File, and hands the rest to the DAW
  adapter as a sidecar;
- labels the artifact `unperformed: true` when no `performance_state` exists, in the DAW notes and in
  the track state.

The DAW adapter:

- writes automation lanes and articulation switches for what MIDI cannot carry;
- reports in `daw_capabilities` whether it can write per-note expression, MPE and tuning at all;
- verifies after writing, as `shared/DAW_ADAPTER_CONTRACT.md` requires.

---

# 7. What this schema does not do

- It does not choose notes, harmony or form. That is the Composer.
- It does not choose sounds. That is the Producer.
- It does not set balance. That is the Mix Engineer.
- It does not hold product-specific facts. Those are in the plugin audit and calibration profiles.
- It does not decide whether realism is wanted. The brief does, through `realism_target`.

---

# 8. `ensemble_gesture`

`ensemble_spread`, `section_offset` and `chord_asynchrony` (section 3) are per-part constants: the
same spread, the same offset, or a value derived from voicing, applied identically to every part that
carries the model. None of them can say "violins lead the crescendo, horns enter at bar 9, low brass
waits for the climax" — one authored shape that different parts respond to differently, not
identically. `ensemble_gesture` is that shape: a single gesture, and a curve per part for how that
part answers it.

**Writer:** Performance Director. It defines the gesture and each part's response curve, as part of
the ensemble step of its method (`performance-director/SKILL.md`).

**Readers:** MIDI Builder, which renders each part's own `responses[]` entry — lag, curve, role — into
that part's automation instead of copying one shared curve onto every part; Music Critics, which
checks the gesture's plausibility against what a real ensemble does.

```yaml
ensemble_gesture:
  id:
  type: crescendo | diminuendo | accelerando | ritardando | textural_swell | density_shift
  origin_bar:
  target_bar:
  responses:
    - part:
      lag_beats:           # how far behind (or ahead of) the origin this part enters/peaks
      curve: linear | exponential | stepped | delayed_onset
      role: lead | follow | independent | held_back
  why:                     # the musical reason this shape was chosen
```

A part's own `performance_state.timing_character` block (section 2) carries the other half of the
link: an optional `gesture_ref: <id>` pointing at the `ensemble_gesture` this part is answering.

**Failure behavior.** A part with no `gesture_ref` keeps today's behavior exactly:
`ensemble_spread` and `section_offset` apply as they do now, unchanged, and `ensemble_gesture` never
enters the picture. This is additive. Nothing regresses for a track that never uses a gesture.

**Gating.** `ensemble_gesture` is only meaningful when 2 or more parts are actually playing together.
A solo track has nothing to lead, follow, or wait for, so it never gets one — the same neutrality
`shared/GENERALIZATION_RULES.md` asks for throughout this pack: a mechanism this system offers is not
a default to reach for on a piece that does not call for it. It is invoked because the ensemble needs
it, never because it exists.

This section is bound by the same hard rule section 1 states for the rest of the schema: **"this
schema has no field named random, and no field whose value is 'amount of humanization'. Every
deviation comes from a named model that another specialist can read, argue with, and reproduce. A
deviation with no model is a bug."** `ensemble_gesture` does not relax that. There is no field for how
much a part leads or lags by feel; every `responses[]` entry names a `curve` from the fixed vocabulary
above, and `lag_beats` is a stated quantity, not an amount-of-humanization dial wearing a new name.
