---
name: ai-music-studio
version: 2.1-dev
description: Music creation, development, diagnosis, teaching and finishing studio. Use for any music task, in any genre, with or without a DAW - writing or continuing a song, chords, melody, beats, arrangement, sound design, vocals, lyrics, MIDI, mixing, reference analysis, plugin audits, or finishing a project. Entry point for sixteen specialist skills; start with the Music Director.
---

# AI Music Studio

This is the entry point for the studio. It exists so the pack loads as one skill.

## Start here

1. Read `music-director/SKILL.md` in this folder and follow it. The Music Director is the only
   user-facing role; it locks intent, sets the session and interaction mode, and routes work to the
   fifteen specialists.
2. Load the user's profile if one exists: `profiles/local/<user>.yaml`, plus any verdicts or plugin
   facts files that profile names. Read them before proposing anything.
3. Resolve every path inside the pack relative to this folder.

Do not load every specialist up front. The Director names which ones a task needs; read those when
they are needed.

## The specialists

| Skill | Handles |
| --- | --- |
| `project-guide` | the project over time: thesis, state, gaps, next actions, finishing |
| `creative-lab` | directions that differ by mechanism; seeds, fusion, experimental systems |
| `composer` | chords, melody, bass, rhythm, motifs, form, pitch and rhythm systems |
| `arranger` | section order, contrast, energy, transitions, orchestration, adaptive form |
| `vocal-director` | what the voices do: hierarchy, stacks, ad-libs, flow, breath, silence |
| `performance-director` | how it is played: articulation, phrasing, feel, feasibility |
| `producer` | sound choice, synthesis, layering, effects, automation, sample packs |
| `lyric-generator` | lyrics fitted to a melody: syllables, stress, rhyme, cross-song uniqueness |
| `mix-engineer` | balance, masking, dynamics, stereo, loudness, per-track evidence |
| `reference-analyst` | what a reference or analyzer report shows, and what transfers |
| `music-critics` | originality, theory, groove, performance, diversity, preference-neutral critique |
| `listener-model` | expectation, surprise, memorability, groove, attention, a listener panel |
| `midi-builder` | validated multitrack MIDI that executes a performance plan |
| `plugin-auditor` | what is installed, what it can play and tune, and an optional calibration pass |
| `music-research` | basic or deep research on an artist's creative system, saved as a pack |

Shared protocols and schemas live in `shared/`, DAW adapters in `daw-adapters/`, and release checks
in `tools/`.
