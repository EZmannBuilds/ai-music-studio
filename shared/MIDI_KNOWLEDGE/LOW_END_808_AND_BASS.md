# Low end: 808s, basslines and how they lock to the kick

Labels as in `DRUMS_AND_GROOVE.md`: **Measured**, **Practice**, **Inference**. If `local/ZYNTHION_FINDINGS.md`
exists on this machine, read its 808 and bass sections too: they hold measured trap, drill and electronic
numbers that can't ship yet.

## 1. The kick and the low note are one instrument

**Practice:** in trap, drill, house and most modern pop and R&B the kick and the 808 or sub are heard as one
low event. A kick with no low note under it sounds thin. A low note that fights the kick's attack smears.

**Rule:**
- Give every kick a low note (or a deliberate gap, like a drop).
- Then add low notes *between* kicks for movement: pickups into the next kick, a note on the "&" of 4, a slide
  into beat 1.
- Check with `midi_check`: `kick_with_low` near 1.0.
- A fully kick-locked 808 is idiomatic. Movement then comes from pitch (octave jumps, slides, a bII or a leading
  tone), not from extra rhythm. Extra notes between kicks are optional, and should be pickups that lead somewhere.
  (In the local packs about half of the 808 notes fall between kicks, but a blind judge preferred tightly locked
  808s, so lock first.)

## 2. 808 craft (trap, drill)

**Practice, with local measurements when present:**
- **Long notes that run into each other.** Use gate near 1, and overlap consecutive notes to trigger the
  synth's legato or portamento glide. Slides are written as overlaps, not pitch-bend messages.
- **Octave jumps are the 808's main melodic move:** root to the octave above and back, or a slide down an
  octave into the downbeat. Drill uses them more than trap.
- **Keep it inside about an octave and a half,** low enough for the fundamental to sit under 60–80 Hz (MIDI
  roughly 24–40 for the root). Above that, an 808 turns into a bass synth.
- **Rhythm:** about 3–6 notes a bar, following the kick, with one or two moves of its own per bar.
- **Sound side** (calibrated synth units: the Faderhand skill's synth notes): a sine or slightly driven sine with a 2nd harmonic around -20 dB so it
  carries on small speakers. Legato doesn't restart a decaying envelope, so a slid note fades unless sustain
  is high.

## 3. Basslines in played and electronic genres

**Measured (Mutopia and PDMX approved sets, bass parts in classical and folk scores):** stepwise share of bass
motion 0.23–0.33 (median), against 0.35–0.42 for melodies. Basslines leap more than tunes do, mostly between
chord roots and fifths.

**Practice by genre:**
- **House and EDM:** offbeat or octave-bouncing bass, short notes (gate about 0.5). Bass on the "&" leaves the
  kick alone on the beat.
- **Techno:** rolling or offbeat 16ths, a narrow range (often a single note plus its octave), hypnotic
  repetition varied by filter, not by notes.
- **R&B and neo-soul:** stepwise and chromatic approach notes into chord roots, rests that let the kick speak,
  syncopated pickups. Lock about half the bass notes to kicks; the rest answer the snare and chords.
- **Funk:** 16th syncopation around a strong "one", ghosted or muted notes, octave pops, and space on 2 and 4
  for the snare.
- **Lo-fi and boom-bap:** sparse roots that land with the kick, with occasional walk-ups between chords.
- **Afro house and amapiano:** "log drum" bass as a percussive melodic voice, with leaps and octave jumps and
  little stepwise motion.

## 4. Register spacing between bass and chords

**Practice (local measurements when present):** keep a gap of about an octave between the bass and the bottom
of the chords below roughly MIDI 52. Low chord tones muddy the bass.

## 5. Anti-patterns

- Every 808 note on a kick, same length, no slides: a kick with pitch.
- A bassline that repeats one bar unchanged for 8+ bars with no pickup or variation in bar 4 or 8.
- Bass notes landing a 16th after the kick (flams the low end), unless it's a deliberate push.
- Chords voiced into the bass register.
