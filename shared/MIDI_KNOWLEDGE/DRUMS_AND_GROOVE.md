# Drums and groove: what played and programmed drums actually do

Labels: **Measured** = computed from the corpus (source and n given). **Practice** = established convention, not
measured here. **Inference** = our reading of the numbers. Positions are 16th steps 0–15 in a 4/4 bar (0 = beat 1,
4 = beat 2, 8 = beat 3, 12 = beat 4; odd steps are the "e" and "a"). Full tables: `stats/groove_drums_by_style.json`.

## 1. Two different targets: played feel and programmed feel

**Measured (Groove MIDI, 1,017 human performances on an electronic kit, test split held out):**
- About 90% of notes sit off the exact 16th grid (quantized share: median 0.07–0.12 per style).
- Timing varies in two layers. Each grid position has its own **placement** (a consistent push or pull), and
  hits at the same position vary around it (**jitter**, about 16–26 ms SD per instrument in these long
  click-tracked takes; drift removed).
- **Velocity is about half pattern and half variation.** The share of velocity variance explained by grid
  position ("velocity structure") has a median of 0.35–0.55 for hats and 0.5–0.55 for snares.

**Practice (measured numbers in `local/` when present):** programmed electronic, trap and house drums are
quantized, use 2–3 fixed velocity tiers and get their movement from pattern, rolls and placement on the grid,
not from timing.

**Rule:** decide which target the genre wants before writing a single note.
- Played: funk, soul, neo-soul, boom-bap played or sampled live, jazz, rock, Latin, afrobeat, New Orleans.
- Programmed: trap, drill, house, techno, EDM, most modern pop and R&B production.
- Hybrid (practice): boom-bap and lo-fi are often programmed but swung, with hand-set velocities and an
  unquantized hat or ghost layer.

**Never "humanize" by adding random velocity and random timing to every note.** In the measured data the
variation follows the beat: random noise gives a velocity structure near 0, which no human take has
(p10 is about 0.1–0.2). Faderhand's `midi_check` (when the Faderhand skill is installed) flags it.

## 2. Hi-hats: three velocity tiers that follow the beat

**Measured (Groove, mean velocity by position, beats only):**

| Style | On the beat | "&" (8th offbeat) | "e"/"a" (16ths) |
|---|---|---|---|
| funk (n=37) | 52–57 | 39–44 | 18–34 |
| hip-hop (n=27) | 52–55 | 39–50 | 14–33 |
| afrobeat (n=12) | 50–56 | 54–61 | 12–34 |

- Funk and hip-hop: quarter notes loudest, 8th offbeats a tier down, 16ths quietest, often by half.
- Afrobeat inverts the first two: the offbeat "&" is as loud as or louder than the beat.
- The spread inside each tier is real (hat velocity SD median 19–21 for funk and hip-hop), but it is smaller
  than the gap between tiers.

**Rule:** write hats as tier + variation, with the tier set by position and style. Velocity structure in the
data is 0.35–0.55 (hats), so the variation inside a tier is about as large as the gap between tiers: use an SD of
about 8–12 within each tier, and let a few 16ths jump a tier. Pure tiers (structure above 0.8) read as programmed.
Keep the quietest hats audible: a floor of about 30–35 on most samplers. Groove's e-kit averages of 18–34 on 16ths
are measured on that kit's velocity curve, and on a General MIDI or one-shot hat anything under about 25 disappears. Change the tier
pattern between sections (open the hat on the "&" of 4 into a chorus; drop to quarters in a breakdown).

## 3. The pocket: where each instrument sits against the grid

**Measured (Groove, median placement in ms against the click, beats only):**
- In funk, hats and kicks on the 8th grid run early (about -15 to -21 ms) and the backbeat snare is later
  (-9 to -10 ms). **The snare sits about 10 ms behind the hats.** Hip-hop shows the same, with the backbeat
  about 5–15 ms behind the hats and kick.
- **Off-16ths ("e" and "a") sit later than the 8ths**, by about 15–25 ms in funk and much more in New Orleans
  (hats on the "e" +21 to +38 ms against -15 to -30 ms on the 8ths). That is swing measured as placement.
- 16th swing (long note's share of each 8th, 50 = straight), median: hip-hop 52.5, funk 56, afrobeat 58,
  jazz 59.5, soul 67.6, New Orleans 75. Rock is straight (52).

**Inference:** "laid back" is mostly *relative* placement: snare later than hats, 16ths later than 8ths. It is
not everything late.

**Rule for played feel in a DAW at 85–110 BPM:**
1. Set swing per style (above) on the 16ths.
2. Place the backbeat snare 5–15 ms after the hats. **Anchor the hats and kick within a few ms of the grid** and
   express the pocket as a *later* snare and *later* off-16ths. The Groove numbers have everything early against
   a click, but in a DAW the bass, keys and samples sit on the grid. Early hats against them read as rushing:
   a blind judge said exactly that in evaluation round 2. (Added after round 2; not yet re-evaluated.)
3. Keep jitter small and placement larger. The Groove figures (16–26 ms per instrument) come from long takes
   measured against a fixed click; they include tempo drift and the odd mis-gridded flam, so they overstate what a
   single 4–8 bar groove needs. For a played groove written in MIDI:
   - jitter 4–10 ms SD per instrument;
   - placement offsets of 5–20 ms, chosen per position, not per note;
   - no single note more than about ±25 ms from its position, except a deliberate flam or drag.

   Random-looking offsets of ±40 ms read as sloppy, not human. (Evaluation 2026-11-18: a blind judge marked
   down exactly that.)
4. Check with `midi_check.py --genre funk|soul|boom-bap|hiphop-live`.

## 4. Ghost notes

**Measured (Groove beats):**
- Ghost snares (under 60% of the backbeat velocity) per bar, median: funk 3.7, soul 2.2, New Orleans 2.3,
  hip-hop 1.5, afrobeat 0.8, rock 0.5.
- Most common ghost positions: funk 15, 7, 9, 1, 5; hip-hop 7, 9, 13, 11. That is the "a" before a backbeat or
  downbeat, and the "e" after one.
- Backbeats average 99–112; ghost-position averages run 38–65. That is roughly half the backbeat, never zero.

**Rule:** ghosts lead into and out of the backbeat (step 3 or 7 before it, step 5 or 13 after it). Set them at
25–55 velocity, with the one just before a backbeat a little louder. Vary which ghosts appear from bar to bar.
Never write the same ghost pattern every bar.

## 5. Kick placement

**Measured (Groove, how often each step has a kick):** funk puts a kick on beat 1 in 76% of bars, the "&" of 3
(step 10) 56%, step 2 46%, step 3 33%. Hip-hop has beat 1 74%, then steps 2, 6, 3 and 8 at 32–39%.
Afrobeat: beat 1 always, beat 3 66%.

**Rule (practice, consistent with the data):** anchor beat 1. Make the second kick of the bar the one that
moves: 3, 6, 7, 10 or 11. In live genres, don't double the backbeat with a kick.

## 6. Half-time, four-on-the-floor and the backbeat

**Measured:**
- Groove beats: 61–75% of bars have the snare on both 2 and 4, against about 0% half-time.
- **Practice:** trap and drill put the backbeat on beat 3 (half-time), not on 2 and 4. House, techno and EDM
  put a kick on every quarter (steps 0, 4, 8 and 12). Measured rates for programmed packs are in `local/` when
  present.

## 7. Hi-hat rolls in trap and drill

**Practice:** trap hats run 8ths or 16ths with 32nd and triplet rolls. Drill favours triplet rolls and
sliding 808s.
**Measured (local Zynthion numbers, when present):** see `local/ZYNTHION_FINDINGS.md`: rolls per bar, which
subdivision, which beat they lead into, and the velocity shape.

**Rule:**
- A roll is a gesture into a target: start it on beat 3 or 4 and land on the next strong beat.
- Ramp velocity up across the roll. Use one or two roll types per section, not a different one every bar.
- Leave some bars with none.

## 8. Fills and section boundaries

**Measured (Groove fills, n=574 across styles):** a fill bar carries more snare and tom hits, with wide snare
velocity spread (SD median 18–33). Hats often drop out (hats are present in fewer fill files than beat files).
**Practice:** one-bar electronic fills are built mostly from kick, snare or clap and open hats, with
toms used sparingly (measured numbers in `local/` when present).

**Rule:** mark every section change with something the drums do in the bar before it: a fill, a drop
(remove the kick for a bar), a crash on the downbeat after, or a reversed or riser gesture. Thin the hats
before a fill so the fill reads.

## 9. Anti-patterns `midi_check` flags

- All velocities equal, or two values only.
- Random velocity with no positional structure.
- Every bar identical in a section longer than 4 bars.
- A played genre written on the grid (quantized share above 0.3), or a programmed genre with tens of ms of
  jitter.
- Hat rolls with flat or falling velocity in trap and drill.
- Half-time genres written with the snare on 2 and 4, or the reverse.
