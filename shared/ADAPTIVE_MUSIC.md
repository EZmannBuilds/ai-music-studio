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
