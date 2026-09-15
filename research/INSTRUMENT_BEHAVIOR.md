# Research: Instrument Behaviour and Virtual Instruments

## Purpose

The research behind `shared/INSTRUMENT_BEHAVIOR_SCHEMA.md` and `shared/VIRTUAL_INSTRUMENT_GUIDE/`.

The guiding question:

> What is this instrument actually like, and what does a sampled or modelled version of it need from
> the notes in order to sound like one?

## Why this is separate from the Plugin Auditor

The Plugin Auditor knows what is installed, what it claims to do and what it measured. `FREE_INSTRUMENTS`
knows products, formats and terms. Neither knows what a cello does. This page and the guide behind it
hold **general instrument behaviour**, which is true regardless of who made the library. Product-specific
facts stay in calibration profiles.

```text
instrument behaviour        shared/VIRTUAL_INSTRUMENT_GUIDE/     general, portable
product capability          plugin audit                          this machine, this edition
measured response           calibration profile                   this patch, this version
```

## Evidence note, and what it means for the guide

When this page was written, one manufacturer manual was read in full (a symphonic strings library) and
most other sources were reachable only as search excerpts or not at all. A good deal of the guide is
therefore standard musicianship rather than verified citation.

**Every section of every guide file carries an evidence label**, and numbers are presented as typical
ranges with a pointer to verify:

```text
manual-derived       stated in a manufacturer manual read for this work
excerpt-derived      from a search excerpt of a named source, not the full text
orchestration text   attributed to a standard reference that was not opened
musicianship         general practice, stated as inference
to verify            named explicitly, with the host that was unreachable
```

This matches the studio's existing MEASURED / RESEARCH-SUPPORTED / CREATIVE INFERENCE discipline. A
guide that presents inference as fact would be worse than no guide, because the Performance Director
acts on it.

---

# 1. One control model, documented, that generalises

From the strings manual read in full, and consistent with excerpts from three other vendors:

- long notes take dynamics from a continuous controller that **crossfades recorded dynamic layers**;
  the manual calls this the most important controller and instructs the player to always use it on
  long notes;
- a separate expression controller acts as a volume trim and is not the same thing;
- short notes take their dynamic from velocity, which may also select the articulation;
- legato patches are monophonic and need **overlapping notes** to trigger a recorded transition; in
  that library the velocity of the arriving note selects which transition is used;
- samples are cut from the true onset, so notes sound late; the fix is to play tight and apply a
  negative track delay rather than to drag the notes;
- round robins exist to prevent repeated identical samples, and release triggers matter in slow music;
- section writing has a practical voice count before the sections must divide;
- the manual's own summary rule is worth keeping: "there are no rules, save that of plausibility".

This is the reference model in `shared/INSTRUMENT_BEHAVIOR_SCHEMA.md`. Controller numbers, velocity
zones and latencies differ per product and belong in calibration.

---

# 2. Family findings that change how notes are written

**Piano.** Velocity changes timbre as well as level, because hammer felt is a nonlinear spring
(acoustics reference to verify). One sampled product documents up to one hundred velocity layers per
key, sympathetic resonance with and without pedal, half-pedalling and re-pedalling, and a soft pedal
that changes colour rather than only level. Practical constraints: a hand spans a ninth comfortably and
a tenth at a stretch; repeated notes are limited by the action; melody notes are voiced above inner
parts; pedal follows harmony, not bar lines.

**Guitar and bass.** One note per string, a span of about four frets in low positions, and a strum that
is a spread rather than a chord. Strum direction determines the order of the strings. Timbre changes
with plucking position and with the pickup that senses the string. Distortion is why power chords
exist. On bass, ghost notes and slides carry the groove, and low notes sustain differently from the
blocks a piano roll suggests. No source giving a measured strum spread in milliseconds could be opened;
any default the guide gives is labelled a practitioner value.

**Bowed strings.** Bow direction, speed, pressure and contact point produce both dynamics and timbre.
Articulations are distinguished by whether the bow leaves the string and how the note is started. A
section is many slightly unsynchronised players, so its transitions smear where a soloist's are sharp.
Vibrato is shaped across a phrase and is often absent at an onset. Chords beyond two notes are broken
unless open strings help.

**Brass and woodwinds.** A phrase is a breath, and endurance is finite. Attack character changes with
dynamic and register. Brass spectra brighten with dynamic, so a swell is a timbre change and a volume
fade on a loud sample never sounds like a quiet note. Clarinet registers differ sharply in strength and
colour, and a slur across the break is genuinely harder. Flute's low register is easily covered; the
oboe's is loud and reedy. These are solo instruments: one player, one note.

**Percussion and drum kit.** Four limbs. Ghost notes are a different sample, not a quieter one. Hi-hat
openness is a continuous state set by a foot. Cymbals ring unless choked. Fills have to be playable
unless the brief wants them not to be. Room sound and microphone bleed are part of a recorded kit.

**Harp.** Seven pedals in three positions give twenty-one pitches from seven string classes, so only
seven pitch classes sound at any moment. A glissando is *designed* by choosing enharmonic doublings;
a chromatic glissando does not exist. Pedal changes take time and are divided between two feet. Two
hands give eight usable fingers.

**Choir and voice.** Consonants are placed before the beat so the vowel lands on it. Vowel
intelligibility falls as the fundamental rises past the first formant (to verify). Breath bounds
phrases, and choirs stagger it. A sustained vowel with no consonants, no vowel change and no breath is
the reason a sampled choir sounds like a synthesizer pad.

**Organs.** No velocity. Dynamics come from registration and from a swell enclosure. On a drawbar
organ the registration *is* the sound, the percussion effect re-triggers only after a gap, and the
rotary speaker's speed change is a performance gesture with its own acceleration.

**Synthesizers and samplers.** Organic does not mean imitating an acoustic instrument. It means
response and change over time: velocity and aftertouch mapped to more than volume, per-voice drift,
envelope variation, nonlinear saturation so that louder is also different, and macro gestures that
move several parameters at once. A static preset with one envelope and no modulation is the electronic
equivalent of a machine-gunned sample.

**Culturally specific instruments.** The guide provides a **research protocol**, not summaries: name
the region, school and repertoire; route to practitioner and tradition-run sources; check the tuning
system, whether the instrument is monophonic, the ornament vocabulary and the rhythmic framework
before writing a note. The common failure is a twelve-tone-equal sample library patch played with
keyboard chords and constant vibrato.

---

# 3. The errors that make a good part sound fake

| Error | Fix |
|---|---|
| repeated identical samples | round robins, velocity variety, alternate articulations |
| no continuous dynamics on long notes | draw a shape per phrase |
| every chord tone at one instant and one velocity | spread and voice, biased by instrument |
| notes outside the practical range | range and register tables |
| legato written without overlap | overlap the notes; the patch is monophonic |
| six-note guitar voicings | solve the fretboard first |
| no releases, no breaths, no noise | leave gaps; keep release samples |
| uniform velocity | velocity by role: melody above inner parts above pads |

`shared/VIRTUAL_INSTRUMENT_GUIDE/COMMON_ERRORS.md` holds this list, and every family file links to it.

---

# 4. Sources

Read in full: one symphonic strings user manual. Read as excerpts: orchestral library manuals and help
pages from three other vendors, a modelled-piano manual and forum, a public orchestration academy's
horn and harp articles, a nineteenth-century orchestration treatise, and instrument pedagogy pages.

Named but **not opened**, and therefore cited only as attributions to verify: Adler, *The Study of
Orchestration*; Piston, *Orchestration*; Berlioz and Strauss, *Treatise on Instrumentation*; Fletcher
& Rossing, *The Physics of Musical Instruments*; Benade, *Fundamentals of Musical Acoustics*; Rossing,
*The Science of Sound*; Sundberg, *The Science of the Singing Voice*.

Anyone extending the guide should start by opening those.
