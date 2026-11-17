# Sketch Round Protocol
## Version 1.0

**Explore before committing.** For a new composition, the studio renders several short, genuinely different
sketches, judges them as audio, and decides KEEP, REVISE, RECOMBINE or REJECT before it writes a full
arrangement. A weak arrangement can't always be rescued by performance, EQ, compression or mastering, so
the studio stops spending its effort polishing the first idea it had.

Run by the Music Director. Candidates come from the Creative Lab (`shared/CREATIVE_EXPLORATION_SCHEMA.md`);
sounds from the Producer; performance from the Performance Director; rendering through the DAW adapter.
Records are `sketch_round` JSON (`schemas/sketch_round.schema.json`, checked by
`tools/validate_records.py sketch_round`).

---

# 1. When it runs

| Situation | Sketch round |
|---|---|
| A new composition, any genre | **yes, by default: three sketches** |
| The user names a single, fully specified idea and says to build it | no; say that the round was skipped and why |
| A revision of an existing song | only when the diagnosis says the problem is the idea itself (section 6) |
| A short cue, jingle or loop under 45 seconds | the cue *is* the sketch; render two or three versions instead |
| No DAW or renderer available | a reduced round on paper, labelled **unrendered**; its decisions are provisional |

The Director may choose two to five sketches and says how many and why. More than five dilutes the user's
listening time.

---

# 2. What a sketch is

- **30 to 45 seconds of rendered audio**, at the tempo and key it would really have, on the sounds it would
  really use. Not a piano demo, not General MIDI, not a description.
- **The idea's most characteristic passage**: usually the hook section, with enough of what leads into it
  to judge the arrival. Not an intro.
- **Produced enough to judge**: real instrument choices, the performance approach the idea needs,
  rough balance and the defining processing. Not mixed or mastered.
- **Kept apart from approved work**: its own project or set, its own folder, never a copy written over a
  song that matters.

## Distinctness

Every pair of sketches differs on **at least two** of these, and the record says which:

`groove` · `harmony_and_melody` · `instrumentation` · `production_texture` · `density` · `structure` ·
`emotional_character`

These sit on top of the Creative Lab's mechanism dimensions; a sketch carries its exploration candidate's
label. **Three presets on the same notes is one sketch, not three.** The Director runs the set test
(`shared/CREATIVE_EXPLORATION_SCHEMA.md`, section 5) before anything is rendered.

---

# 3. Rendering and comparison

1. Render each sketch's main output (and its stems, where the adapter can).
2. Run render verification (`shared/RENDER_VERIFICATION.md`): silent notes, octave errors, clipping, a
   part that cannot be heard. A sketch that fails verification is fixed or re-rendered before anyone
   judges it. **Nobody judges a broken render.**
3. **Loudness-match the audition copies** (integrated loudness, the same target for all, at least
   6 LU below full scale so nothing is limited). Louder reads as better; an unmatched comparison is not
   a comparison.
4. Name the files by label (`A`, `B`, `C`), not by quality order, and say what each is in one line.
5. Measure what can be measured (loudness, bands, width, the lead against the rest, density over time)
   and report it as **measurement**.

---

# 4. Who judges, and with what

**Be exact about the basis of every judgment:**

| Basis | What it is | What it can establish |
|---|---|---|
| `listened_by_user` | the user heard the loudness-matched files | taste, realism, whether it works. **Final.** |
| `audio_model` | an audio-capable model analysed the render | only what that model has been shown to detect reliably; label its findings as its own |
| `measured` | analyzer and script numbers | properties: level, balance, timing, pitch, width |
| `inferred` | reasoning from the notes, the plan or the numbers | a hypothesis, never a verdict |

**A text model reasoning about MIDI or measurements is not listening.** It never writes "sounds", "feels
warm", "sounds realistic" or "sounds fake" on its own authority. It may write "the measurements suggest"
or "the user said". Where no reliable listener is available, the decision waits for the user, with the
files ready.

The listener model (`listener-model/SKILL.md`) contributes expectations and risks as `inferred`.
Measurements can block a sketch (it is broken) but cannot crown one (it is good).

---

# 5. The four decisions

| Decision | Meaning | What happens next |
|---|---|---|
| **KEEP** | strong enough to develop as it is | goes to full composition and arrangement; the rest of the round is archived |
| **REVISE** | the idea works, with named problems | one targeted revision of **this sketch**, re-rendered and re-judged before any full build. Name the change and the stage it belongs to |
| **RECOMBINE** | compatible elements from two or more sketches make a stronger idea | a new sketch (a new label) is built from the named elements, rendered and judged like the others. Record the source of each element |
| **REJECT** | not worth continuing | archived with the reason. **A rejected sketch is never polished further**, and its material is not quietly reused in the keeper |

Rules:
- A round ends with **exactly one** KEEP, or with the user choosing to stop or to run a new round.
- REVISE and RECOMBINE produce new renders. A decision made on an old render isn't carried over to a new one.
- Every decision records its **basis** (section 4) and **who decided** (`user`, or `director_provisional`
  when the user delegated the choice). A provisional KEEP is shown to the user before the full build.
- Two rounds in a row with no KEEP is a signal about the brief, not the sketches: go back to the intent
  lock with the user.

---

# 6. Returning upstream during production

The sketch round is the first loop, not the only one. After any later render, when the diagnosis points
upstream, **go back to the stage that owns the cause** instead of compensating downstream
(`music-director/SKILL.md`, "Revise the cause, not the symptom").

| Symptom (from the user, or from measurement) | Look first at | Not first at |
|---|---|---|
| "Childish", "cartoonish", "theatrical" | register, orchestration, articulation, harmony, the hook's rhythm | EQ |
| "Artificial", "fake", "MIDI-sounding" | the sound engine, the performance method, whether the part is playable on its instrument | reverb or humanisation alone |
| "Flat", "nothing happens" | arrangement (entries, exits, contrast), harmony, the lead's phrasing | compression or loudness |
| The drums lack impact | the sample, the pattern, competing parts, then the mix | the fader |
| A bass too slow for its part | the part or the sound (envelope, engine) | EQ |

**An adjective is evidence, not a diagnosis.** "Artificial" has meant a busy lead, the wrong kind of
realism, a quiet master and an over-full midrange at different times. Record it as the user's words,
form hypotheses, test them with renders, and keep the ones the next verdict supports.

---

# 7. The archive

Every sketch is kept with its record: the intention, the candidate label, the instruments and processing,
the render, the measurements, the decision, the basis and the reason. Archived ideas can be offered in later
work **as ideas**: their melodies, riffs and motifs aren't reused unless the user asks.

---

# 8. Record

```json
{
  "id": "round id, unique in the project",
  "when": "date and time",
  "project": "project or song name",
  "brief": "the locked intent, one or two sentences",
  "sketch_count_reason": "why this many sketches",
  "candidates": [
    {
      "label": "A",
      "one_line": "what this is, in a sentence a musician would understand",
      "exploration_label": "the Creative Lab candidate it realises",
      "differs_on": ["groove", "instrumentation"],
      "instruments": ["the actual sounds used"],
      "render": "path to the rendered audition file",
      "measurements": {},
      "decision": "KEEP | REVISE | RECOMBINE | REJECT | PENDING",
      "basis": "listened_by_user | audio_model | measured | inferred",
      "decided_by": "user | director_provisional | pending",
      "reason": "why",
      "revision_plan": "for REVISE: what changes, at which stage",
      "recombine_sources": {"element": "source label"}
    }
  ],
  "outcome": "the kept label, or 'new round', or 'stopped'",
  "unrendered": false
}
```

`PENDING` is a legal state while the user listens. A round whose decisions are all `PENDING` is an open
round, not a finished one.
