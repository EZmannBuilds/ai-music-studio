# Generation rules: how to write MIDI that sounds played, idiomatic and developed

This is the working checklist the Composer, Performance Director, Arranger and MIDI Builder follow when they
write notes. Each rule points to the page that justifies it. The examples are original and written for this
skill.

## Before writing

1. **Name the target:** genre and subgenre, tempo, and played or programmed feel (`DRUMS_AND_GROOVE.md` §1).
2. **Retrieve, don't load everything:**
   `python3 tools/kb_search.py "<genre> <role> <question>"` returns the 3–6 most relevant sections. Read those.
3. **Sketch 2–3 directions that differ by mechanism** (`ARRANGEMENT_AND_REVISION.md` §3), unless the task is an
   edit.

## Drums

- **Played:** swing per style; backbeat 5–15 ms behind the hats; placement chosen per position (5–20 ms); jitter
  only 4–10 ms SD, with no note more than about ±25 ms off unless it's a deliberate flam.
- **Played velocity:** hats in tiers (beat > "&" > 16ths) with variation inside each tier about as large as the
  gaps between them, and a floor of about 30; snare ghosts 25–55 around backbeats of 95–115 (§2–4).
- **Programmed:** quantized, 2–3 velocity tiers, movement from pattern, rolls and placement on the grid.
- **Trap and drill:**
  - Vary the kick and hat pattern from bar to bar, with at least half the bars differing, and let the lead build
    to a peak around bars 5–7. A short repeated cell is the hook, not the whole loop. (Added after evaluation
    round 2, where a blind judge preferred busier, developing trap loops; not yet re-evaluated.)
  - Backbeat on beat 3.
  - A hat roll every 1–2 bars, ramping up into beat 3 or the next bar: 32nds in trap, triplets in drill.
  - Kicks move between bars.
- **Every 4th or 8th bar** does something the others don't: a fill, a drop, an extra kick, a roll, an open hat.

**Example (original): 2 bars of a played funk hat lane at 100 BPM.** Steps 0–15, velocity, placement in ms
against the grid:

```
step:  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
vel :  58  24  44  30  55  20  41  33  60  27  46  22  54  31  40  26
ms  : -14  +6 -16  +3 -15  +8 -17  +5 -13  +4 -18  +9 -16  +2 -15  +7
```

Bar 2: same tiers, each value moved by ±3–9; step 14 becomes an open hat (vel 48); step 15 drops out.
Snare: 104 on steps 4 and 12 at -4 ms; ghosts of 34 on 7, 41 on 15, 29 on 9.

## Low end

- Every kick gets a low note.
- **Trap and drill 808:** lock to the kicks first. That alone is idiomatic. Then add at most 1–2 notes between
  kicks per bar as pickups or slides, and only where they lead somewhere. Overlap notes for slides, use octave
  jumps, 3–6 notes per bar (`LOW_END_808_AND_BASS.md`).
- **Played genres:** lock about half of the bass to the kick, walk or approach chord roots by step, and leave
  space on the backbeat.
- **Register:** chords an octave above the bass, nothing under about MIDI 52 but the bass.

**Example (original): 1 bar of trap 808 in F minor at 140 BPM.** Kicks on steps 0, 7 and 10.

```
step 0  F1 (29) len 6  (kick)
step 6  F1      len 2  (pickup, overlaps into the next note -> slide)
step 7  F2 (41) len 3  (kick, octave jump)
step 10 Eb2(39) len 4  (kick)
step 14 C2 (36) len 3  (pickup into the next bar, overlaps the next bar's F1 -> slide down)
```

## Melody and hooks

- **Shape:** 40–60% steps, 15–30% leaps, recover leaps by step. Chord tones on strong beats, non-chord tones
  on weak positions (`MELODY_LINES_AND_DEVELOPMENT.md` §1–3).
- **Hook:** a 2–4 note cell, repeated with one change, answered by the 4th statement. A rest every 1–2 bars.
- **Development:** sequence, inversion, rhythmic change, fragmentation. Keep the hook exact where it must be
  recognised.

## Several parts

- Outer voices in contrary motion about a third of the time or more; no parallel fifths.
- One part moves while another holds.
- Register lanes and rhythmic lanes (`ARRANGEMENT_AND_REVISION.md` §2).
- For a vocal: chords sparse and under about MIDI 72.

## Song form

- A section map first, with at least two changes at every boundary (layers, density, register, drum pattern,
  harmony).
- A gesture in the bar before every boundary.
- 48+ bars should change at 3+ of the 8-bar boundaries.

## After writing: measure, read back, revise

```
uv run -q --no-project --with mido python <faderhand skill>/tools/midi_check.py out.mid --genre <genre>
```

1. Fix every REVISE that isn't a deliberate choice.
2. Read back the protected material.
3. Render and listen when you can.
4. Write the notes: what you measured, what you changed, what wasn't heard.

**A file existing is not the end of the task.**

## Originality

The corpus taught distributions, not tunes.
- Never reproduce a melody, bassline or drum pattern from a reference or from memory of a known song.
- If a sketch resembles a known work, change its rhythm and contour (the studio's similarity control in
  `../../music-director/SKILL.md`).
