# Adaptive and Generative Music
## Version 1.0

Music that responds: to a game state, a player, a parameter, or its own process.

Written by the Arranger (states, transitions and form), the Composer (motif invariants) and the
Producer (layers). Read by MIDI Builder for per-state exports, by the Project Guide for score
projects, and by Music Critics and the Listener Model.

**There is no adaptive-music specialist.** Adaptive form is form, and the Arranger owns form. What was
missing was the representation, which is this page.

---

# 1. Vocabulary, stated tool-neutrally

Middleware names are product facts. The behaviour is the music.

| Neutral term | What it is |
|---|---|
| segment | a musical chunk with a defined start and end, and tails on both sides |
| pre-entry | audio before the segment's musical start, for pickups |
| entry point | where the segment's musical time begins |
| exit point | where its musical time ends |
| post-exit | the tail after the exit, which may sound over the next segment's pre-entry |
| sync point | where a transition is allowed to happen |
| stinger | a short phrase laid over whatever is playing, not replacing it |
| layer | a stem whose presence or level follows a parameter |
| state | a named condition selecting a segment set, a layer mask, or both |
| parameter | a continuous value mapped through a curve to a musical property |
| transition bridge | optional material inserted between leaving one state and arriving at another |

A mapping table to specific middleware vocabularies belongs in the adapter or the project notes, and
should be verified against current documentation rather than remembered.

---

# 2. `adaptive_music`

```yaml
adaptive_music:
  project_type: game | installation | film_cue_system | generative_piece | live_set
  musical_clock: {tempo:, meter:, grid:}      # what sync points are measured against

  states:
    - name:
      function:                # what this state is for, musically
      segments: []
      layer_mask: []           # which layers sound in this state
      loop: true | false
      entry_from: []           # which states can reach this one
      notes:

  layers:
    - name:
      role:                    # anchor, pulse, harmony, lead, texture, tension
      complete_alone: true | false     # can it be heard without the others?
      fade_in_beats:
      fade_out_beats:
      parameter:               # what drives it, if anything

  transitions:
    - from:
      to:
      exit_at: immediate | next_beat | next_bar | next_grid | next_cue | exit_point
      enter_at: entry_point | same_position | nearest_cue | last_exit_position
      bridge:                  # a transition segment, if any
      stinger:                 # laid over, if any
      fade:
      latency_budget:          # section 4
      why:                     # the musical reason this transition works

  timecode_cues: []            # fixed real-time hit points fitted to the grid above; section 8

  parameters:
    - name:
      range: {min:, max:}
      maps_to: []              # what it moves, through what curve
      smoothing:

  motif_invariants: []         # section 3
  allowed_variations: []       # what may differ between repetitions
  loop_rules:
    tail_handling:             # how post-exit audio is kept
    reverb_across_boundary:    # baked into the loop head, or generated on a live bus
    no_immediate_repeat: []    # segments that must not follow themselves
    variation_pool_size:

  stingers:
    - name:
      trigger:
      sync: next_beat | next_bar | immediate
      throttle_seconds:        # so one event cannot machine-gun it
      harmonic_fit:            # which states it works over

  failure_states:
    - event:                   # death, defeat, disconnection, silence
      behavior: resolve | suspend | drop_to_glue | stop
      note: "a hard cut is a choice, not a default"

  glue_state:                  # a neutral state reachable from everywhere
  authored_endings: []         # one per loopable middle
```

---

# 3. Motif invariants

The thing that makes a long adaptive score cohere is a small identity that survives every variation,
while length, layering and order change around it
(`research/ADAPTIVE_AND_EXPERIMENTAL.md`, section 2).

```yaml
motif_invariant:
  id:
  what_is_fixed:               # interval shape, rhythm, timbre, register, harmonic function
  what_may_vary:               # instrumentation, tempo, harmony under it, density, completeness
  appears_in: []               # states
  recognition_test:            # would a player know this is the same theme?
```

State it explicitly, because under recombination the parts that were never declared fixed are the
parts that drift.

---

# 4. Latency budget

The quantity that actually constrains the writing:

```text
latency = time to the next permitted sync point + engine look-ahead
```

Decide it per trigger, because it is a musical decision with a gameplay consequence.

| Trigger | Typical need | What that forces |
|---|---|---|
| combat starts | within a beat | a stinger now, plus a next-beat or next-bar state change under it |
| area changes | within a bar | next-bar exit; write pickups into the pre-entry |
| tension rises | smooth | a parameter on layers, not a state change |
| scene ends | can wait | exit point, authored ending |

Where the budget is tight, add custom sync points **inside** segments rather than shortening the
segments, which would cost the music its phrase lengths.

---

# 5. Rules

**Every layer must be musically complete on its own**, or be declared incomplete and always paired.
A harmony layer that is a suspension with no resolution cannot be the top layer of a mask.

**Every loopable middle gets an authored ending.** Fading out a loop is what a system does when nobody
wrote an ending.

**Endless material avoids strong periodic closure.** A cadence every sixteen bars teaches the listener
to count, and once they count, they hear the loop.

**Probabilistic does not mean random.** In documented practice the material is composed and the
constraints are tight; the system chooses among good options. Variation pools, weights and
no-immediate-repeat rules are how that is expressed.

**Silence is a state.** It needs the same design as any other, including how it is entered and left.

---

# 6. Deliverables

```yaml
adaptive_exports:
  per_state_stems: []          # rendered layers, aligned to the same grid and start
  segment_files: []            # with tails, and the tail lengths recorded
  stinger_files: []
  tempo_and_grid_manifest:
  transition_matrix:           # the table an implementer can read without the project file
  implementation_notes:        # what the target engine has to do
```

Render Verification applies per state, not once for the project: a layer that is silent in one state
is a silent part (`shared/RENDER_VERIFICATION.md`).

---

# 7. Generative pieces without a game

The same schema covers a piece that runs by itself: states become sections or processes, parameters
become time or a sensor, and the failure states become what happens when it is stopped. For the
compositional side of process, chance and indeterminacy, see `shared/EXPERIMENTAL_SYSTEMS.md`. The
question that page insists on applies here too: what is this making audible?

---

# 8. Timecode cue

`musical_clock` (section 2) answers where a moment is in the form: a bar and a beat. A **timecode
cue** answers a different question the adaptive machinery was never built for: where a moment has to
land in real time, against a film or game cue sheet given in hh:mm:ss:ff or seconds. The two are read
together, not one instead of the other: a timecode cue names the nearest grid position on the same
clock `states` and `transitions` already use, and says how to make that position land exactly on the
timecode.

A `timecode_cue` is a sibling of the sync-point vocabulary `transitions[]` already uses (`exit_at`,
`enter_at`, `bridge`, `stinger`, `fade`, `latency_budget`, `why`), for a different trigger: not a state
change, but a fixed point on the timeline the music must hit regardless of what state it is in.

```yaml
timecode_cue:
  timecode:                  # hh:mm:ss:ff or seconds
  nearest_grid_position:     # bar:beat, read against musical_clock
  fit_strategy: tempo_ramp | insert_pause | reharmonize_bar_length
  hit_point_type: sync_point | stinger | hard_hit
```

| Field | |
|---|---|
| `timecode` | the fixed point on the cue sheet, in whatever format the cue sheet uses |
| `nearest_grid_position` | the bar:beat, on the existing `musical_clock` grid, that should coincide with `timecode` |
| `fit_strategy` | how the grid is fitted to the timecode, below |
| `hit_point_type` | reuses section 1's `sync point` and `stinger` where either applies, plus `hard_hit` for a cue with no tolerance because picture or gameplay depends on the exact frame |

## Fit strategies

- **`tempo_ramp`** — a tempo curve between the nearest stable tempo marking and the cue, sized so the
  beat at `nearest_grid_position` falls on `timecode`. Keep it a tempo change a listener would accept
  as one: `shared/RHYTHM_SYSTEMS/METRIC_MODULATION_AND_TEMPO_MORPHING.md` gives the pivot mechanism,
  a worked table of how large a ratio reads as a clear lift versus one that borders on a cut, and the
  rule that the new tempo is computed from the ratio, never guessed. A ramp so steep it reads as a
  splice rather than a tempo change has failed the fit even if the frame is hit.
- **`insert_pause`** — a held bar, a fermata, or silence, so real time passes without the beat grid's
  rate changing at all.
- **`reharmonize_bar_length`** — change one bar's length (an added or dropped beat, a metre change for
  that bar only) so the next downbeat falls on the cue, instead of bending tempo to get there.

Pick the strategy that costs the material the least: a tempo ramp for a small, smooth adjustment; an
inserted pause where a hold or a breath already belongs there dramatically; a bar-length change where
the phrase can absorb an odd bar without sounding wrong. A cue that cannot be fitted without an audible
distortion is a fact to report upstream, not a fit to force through.

## Does not own

A `timecode_cue` does not own the adaptive state machine. `states`, `transitions`, `layers`,
`parameters` and `failure_states` are unchanged by this section: a timecode cue is placed within
whatever state is already playing, and fits the grid to a real-time point without altering what
selected that state or what happens after it.
