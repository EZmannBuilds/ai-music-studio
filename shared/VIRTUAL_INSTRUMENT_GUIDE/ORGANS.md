# Organs

Two unrelated instruments that share a keyboard and a name: the pipe organ, and the electromechanical
drawbar organ.

> Evidence: `musicianship` throughout. `excerpt-derived` for the drawbar organ's single-trigger
> percussion behaviour, from programming guidance read as excerpts. `orchestration-text` for pipe
> organ registration conventions, attributed to Adler, *The Study of Orchestration*, not opened for
> this work. No measured figures.

Cross-family failures are in `COMMON_ERRORS.md`. One of them, error 3, applies here in reverse:
uniform velocity is correct on both of these instruments, because neither has velocity at all.

---

## What they share

`musicianship`. **No velocity.** A key is either down or up. Pressing harder changes nothing, because
the key opens a valve or closes a contact and that is all it does.

Everything a pianist does with velocity, an organist does with three other things: **which stops or
drawbars are engaged, how long the note is held, and when the note starts and stops.** Articulation
on an organ is entirely note length and note placement. That is not a limitation to work around, it
is the technique.

---

# Pipe organ

## What the instrument is

`musicianship`. Ranks of pipes fed by a wind supply, selected by stops, played from two or more
manuals and a pedalboard. Each stop is a complete rank across the keyboard, and the combination of
engaged stops is the **registration**.

## Range and register

`musicianship`. Manuals typically span about five octaves; the pedalboard covers roughly two and a
half from the bottom. The sounding range is far wider than the keyboard, because of footages.

**Footages** are the organ's transposition system. A stop labelled by its pipe length sounds at a
fixed relationship to the key.

```text
16'    an octave below the key
8'     at the key's pitch, the reference
4'     an octave above
2'     two octaves above
mixtures   several ranks at once, including fifths, sounding as brightness rather than as pitches
```

## Registration is the dynamic and the timbre

`orchestration-text` and `musicianship`. Adding stops makes the instrument louder **and** brighter and
wider, because it adds ranks rather than amplifying one. Removing them does the reverse. This is the
organ's version of the rule in error 10: loudness and colour are the same control, and they cannot be
separated.

Registration changes are made between phrases, by hand or by a preset mechanism, and they take time.
A registration that changes note by note is not an organ.

## The swell enclosure

`musicianship`. One or more divisions of the instrument sit inside a box with louvred shutters, opened
and closed by a pedal. That is the only **graded** dynamic control the instrument has, and it works by
opening the box, which changes the high frequency content as well as the level. It is expressive and
continuous, and it applies only to the enclosed division.

## Attack, release and wind

`musicianship`.

- **Chiff**, the transient at the start of a pipe's speech, is the organ's attack, and it varies by
  stop and by voicing. It is not velocity-dependent.
- The release is audible: the pipe stops speaking and the room keeps the sound.
- The **wind supply** is not perfectly steady on many instruments, and heavy chords can pull the wind
  slightly, producing a small pitch and level movement. That instability is part of the sound.
- Organs live in large reverberant rooms, and the room is inseparable from the instrument.

## Physical constraints

`musicianship`. Two hands on possibly different manuals, and two feet on the pedalboard. The pedals
are played with both feet, so pedal lines are usually single-voiced and moderate in speed. Registration
changes need a free hand or a foot on a preset.

## Programming it

```yaml
velocity: ignored. Do not write a dynamic curve into it.
dynamics: stop selection, plus a continuous swell pedal control on enclosed divisions
articulation: note length and placement only
registration_changes: between phrases, with time; often separate patches or keyswitches
release: audible; give notes real note-offs
room: part of the instrument, already present in a recorded patch
```

What makes it sound real: vary note length constantly, because that is the phrasing; detach repeated
notes clearly, since there is no attack to distinguish them otherwise; use the swell pedal as a
continuous line rather than a step; change registration at structural points; let the room ring.

---

# Drawbar organ

## What the instrument is

`musicianship`. An electromechanical instrument where rotating wheels generate tones that are mixed by
sliding drawbars, one per harmonic, and amplified. It is normally heard through a **rotary speaker**,
a cabinet with a spinning horn and rotor.

## The drawbars are the sound

`musicianship`. Each drawbar adds a fixed harmonic at a settable level, labelled by footage in the same
system as the pipe organ. The combination **is** the patch: there is no filter and no envelope, so
changing the sound means moving a drawbar, and players do that while playing.

There is no velocity. Dynamics come from the drawbars, from the amplifier being driven harder, and
from the expression pedal.

## Percussion is single-trigger

`excerpt-derived`. The instrument's percussion effect adds a short decaying harmonic to the attack,
and it **re-triggers only after all keys have been released**. In a legato passage it sounds on the
first note of a phrase and then not again until the player lifts. The consequence for programming is
large: **phrasing changes the sound.** A part written with overlapping notes gets percussion once; the
same part played detached gets it on every note. Which behaviour is wanted is a musical decision and
has to be made deliberately, because a sequencer will make it accidentally.

## Key click, vibrato and chorus

`musicianship`. The contacts make an audible **key click** at the start and end of every note, and it
is a defining part of the instrument rather than a fault. The built-in vibrato and chorus settings are
a scanner effect applied to the whole instrument, set for a passage.

## The rotary speaker

`musicianship`. The horn and rotor spin, producing a combination of amplitude and frequency modulation
and a moving room reflection. It has two speeds, slow and fast, and **the change between them is the
gesture.** The horn and the rotor accelerate and decelerate at different rates over a second or more,
and that transition is one of the most recognisable sounds in recorded music.

Programming it as a static effect at one speed throws away the only real-time expressive control the
instrument has after the drawbars. The speed change is a **performance event**, placed at a musical
point, and it needs its acceleration modelled or recorded.

## Programming it

```yaml
velocity: ignored
dynamics: drawbar positions, amplifier drive, expression pedal
percussion: single-trigger; it depends on note overlap, so it depends on the phrasing
key_click: present on note-on and note-off; do not remove it
rotary_speed: a performance automation event with acceleration, not a static setting
overdrive: part of the dynamic range; louder is dirtier
```

What makes it sound real: decide the drawbar registration and keep it, or move it deliberately; write
overlapping and detached passages on purpose because percussion depends on them; place rotary speed
changes at phrase boundaries and let them ramp; play glissandi and smears, which are idiomatic here
and impossible on most keyboards; use the expression pedal as a continuous line.

---

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Organ-specific tells:

- a velocity curve written into a part for an instrument with no velocity, which does nothing on a
  real patch and something wrong on a sampled one;
- uniform note lengths, which removes the entire articulation vocabulary;
- registration changing note by note;
- a swell pedal used as a stepped switch rather than a continuous line;
- a drawbar organ patch with percussion on every note regardless of overlap, or off entirely;
- key click gated away for tidiness, which is error 7;
- a rotary speaker at one fixed speed for a whole track, with no transition;
- notes glued end to end, so the audible releases disappear, which is error 12.

## What the Performance Director needs from this file

- **Velocity is not a dynamic control here.** The plan's `dynamic_arc.control` must be the swell or
  expression pedal, or the registration, and never velocity.
- `note_length_variation` is the primary expressive parameter on both instruments, not a secondary one.
- `limb_or_finger_conflicts`: two hands across manuals plus two feet on a pedalboard, and registration
  changes need a free limb.
- Rotary speed changes and registration changes are **events in the plan**, with time allowed.
- Percussion single-trigger behaviour is a phrasing constraint that the Director should state
  explicitly, because MIDI Builder's note overlap decision changes the timbre.

## Sources and what to verify

- **To verify**: registration conventions, footage nomenclature and pipe organ writing in Adler, *The
  Study of Orchestration*. Not opened for this work.
- **To verify**: pipe speech transients and wind supply behaviour, in Fletcher and Rossing, *The
  Physics of Musical Instruments*. Not opened.
- `excerpt-derived` percussion behaviour came from programming guidance read as search excerpts.
  Confirm against the installed instrument's documentation.
- **Not available**: measured rotary speaker ramp times for the horn and the rotor. Treat any figure
  as a practitioner value, or calibrate.
