# MIDI knowledge library

What the skill learned from a curated MIDI corpus, written down so it can be used at generation time without
loading the corpus.

- **Measured, not memorised.** The corpus was analysed for rhythm and groove, velocity and timing, register,
  intervals and contour, density, and how parts lock together. Only aggregate numbers and the guidance written
  from them are here. No source MIDI, transcription or per-file pattern is included (`PROVENANCE.md`).
- **Retrieval.** Run `python3 tools/kb_search.py "<what you need>"` from the skill root. It prints only the most
  relevant sections. Open a whole page only when the task is about that page's subject.
- **Labels.** Every claim is marked:
  - **Measured:** computed from the corpus, with n and source.
  - **Practice:** established convention, not measured here.
  - **Inference:** our reading of the numbers.

  Treat inferences as hypotheses.

| Page | Use it for |
|---|---|
| `GENERATION_RULES.md` | **Start here** for any MIDI writing: the checklist and two original worked examples |
| `DRUMS_AND_GROOVE.md` | Played versus programmed feel, hat tiers, the pocket, swing per style, ghost notes, kicks, rolls, fills |
| `LOW_END_808_AND_BASS.md` | 808 craft, kick and bass lock, basslines by genre, register spacing |
| `MELODY_LINES_AND_DEVELOPMENT.md` | Melodic motion, hooks, melody against harmony, arps, counterpoint, motif development, ostinato builds |
| `ARRANGEMENT_AND_REVISION.md` | Section contrast, space between parts, exploring several directions, the revision loop, protecting user material |
| Faderhand's TARGETS page | Where every range in Faderhand's `midi_check` (when the Faderhand skill is installed) comes from |
| `PROVENANCE.md` | Sources, licences, counts, dedup, held-out split, attribution |
| `stats/*.json` | The aggregate numbers behind the pages (approved sources) |
| `local/` | Numbers from sources pending licence clearance. **Present only on the machine that built them; never committed or shipped.** |

## Rebuilding

The corpus lives outside both repositories. Rebuild it with the Faderhand skill's corpus scripts in `tools/corpus/`:
1. fetch_mutopia.py, for the curated selection.
2. Download Groove and PDMX from their own pages, and Zynthion's packs through its site.
3. inventory.py
4. analyze.py
5. build_knowledge.py

The scripts read files; they never run anything downloaded.

## Limits

- The human-timing data is one dataset: Groove, ten drummers on one electronic kit, recorded to a click.
- The modern-genre pattern data (trap, drill, house, techno, afro, R&B loops) is one vendor's programmed packs,
  and is pending clearance.
- The classical data is engraved scores: quantized, with dynamics as fixed levels. It teaches lines, harmony
  and form, not timing.
- There is no data here for vocals, mixing or sound, and nothing measured for drill or UK garage beyond those
  packs.
