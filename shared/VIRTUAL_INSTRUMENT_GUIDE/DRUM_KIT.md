# Drum Kit

The played kit: kick, snare, toms, hi-hat, cymbals, and the four limbs that operate them.

> Evidence: `excerpt-derived` for the ghost note velocity band, the hi-hat controller model and the
> choke implementation, from programming guidance read as excerpts. `musicianship` for everything
> else. The velocity band is a typical range, not a measurement on this system.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## What the instrument is

`musicianship`. Several unrelated percussion instruments arranged so that one person can play them,
and the arrangement is the instrument. What a kit can play is decided by where the drums are and how
many limbs are free, not by what the notes say.

## Range and register

`musicianship`. Not pitched, so "range" means the kit's vocabulary of surfaces and the zones on each.

```text
kick            one surface; beater type and muffling change it more than velocity does
snare           centre, off-centre, rimshot, cross-stick, rim only, brush sweep
toms            two to five, pitched relative to each other, with a falling pitch as they decay
hi-hat          a continuous range from closed to open, plus the foot chick and the foot splash
ride            bow, bell, edge, and crash-ride behaviour at high dynamic
crashes         edge strikes; chokes
```

**Velocity selects the sample, not just the level.** A tap, a normal stroke and a rimshot are three
different recordings on a real kit and in any serious sampled kit. Treating velocity as loudness only
is the root of most fake-sounding programmed drums.

## Articulation and note transitions

`musicianship` and `excerpt-derived`.

**Ghost notes are a different sample, not a quieter one.** They are a light stroke with the stick
barely leaving the head, and they have a different attack and almost no body. `excerpt-derived`:
documented programming guidance places them in a velocity band of roughly 40 to 70 and maps them to a
distinct sample. That band is a typical range and should be checked against the installed kit.

```text
flam        two strokes, one hand fractionally before the other; the grace note is quieter
drag        two quick grace strokes before the main one
buzz        a pressed stroke; the stick bounces multiple times
rimshot     stick hitting head and rim together; loud, cracking
cross-stick the stick laid across the head, struck against the rim; quiet and woody
choke       a cymbal grabbed immediately after striking
```

`excerpt-derived`: chokes are implemented through **note-off or aftertouch depending on the product**.
Which one is a calibration fact.

## Physical constraints

`musicianship`, and the rule the feasibility check exists for.

```text
FOUR LIMBS.
Two hands and two feet, and each can do one thing at a time.
```

A right hand on the hi-hat cannot simultaneously hit a tom across the kit. A left foot holding the
hi-hat closed cannot also play a second kick pedal. The hands cross and uncross, which takes time.
This is a hard validator rule, and it catches more programmed drum errors than anything else.

**Hi-hat openness is a continuous state set by a foot**, not a set of separate instruments. It is
mapped to a controller in most kits, and it persists until the foot moves. Programming open and
closed hats as unrelated notes with no continuous state produces a hat part that has no foot in it.

## Phrase behaviour

`musicianship`. A groove is a repeating pattern with variation inside it, and the variation is
sticking and ghost notes rather than new notes. **Fills must be playable unless the brief wants them
not to be.** A fill is a hand-to-hand sequence across the kit, and one that requires three hands or
an impossible crossing reads as a machine even when every individual hit sounds real.

Cymbals ring. A crash decays for seconds and overlaps whatever follows, and cutting it off with a
note length shorter than the sample is audible.

## Ensemble behaviour

`musicianship`. The kit is the arrangement's timekeeper, so it is usually a marker part in the sense
of `shared/HUMAN_PERFORMANCE_SCHEMA.md`: deviation applied to the kit moves the reference everything
else is measured against. Where a loose kit is wanted, that is a deliberate choice, and the hat or
ride carrying the pulse is normally left tighter than the rest.

The kick and bass relationship is an arrangement decision. See `BASS.md`.

## Recording behaviour

`musicianship`. **Room sound and microphone bleed are part of a recorded kit.** The snare is in the
overheads, the hat is in the snare microphone, and the kit is heard as one instrument in one room.
Sampled kits that offer close, overhead and room microphones are offering the same kit at different
distances, and using only close microphones produces a kit that is detailed and dead.

Bleed also means that the room is triggered by every hit. A kit with a huge room on the snare and no
room on anything else is not a kit in a room.

## Programming it: the control model

`excerpt-derived` and `musicianship`. Product specifics belong in the calibration profile.

```yaml
velocity:
  selects: the sample first, the level second
  zones: tap, normal, accent, rimshot; boundaries are a calibration fact
ghost_notes:
  typical_velocity_band: roughly 40 to 70          # excerpt-derived, typical range
  implemented_as: a distinct sample, not a quiet normal stroke
hi_hat:
  openness: a continuous state on a controller, set by the foot
  extras: foot chick, foot splash, and the closing sound itself
chokes:
  implemented_as: note-off or aftertouch, depending on the product
round_robins:
  essential here; repeated identical snare samples are the clearest machine-gun case
microphones:
  close, overhead, room; bleed is modelled or recorded
```

## Programming it: what makes it sound real

- Validate four limbs before anything else.
- Alternate sticking on repeated notes, and let the two hands have slightly different velocities.
  `velocity_asymmetry` is the cause; a hand does not strike evenly.
- Write ghost notes into the groove, in the kit's ghost band and on the ghost sample.
- Move the hi-hat openness continuously, and let the foot close it audibly.
- Use `flam` where two limbs really would arrive fractionally apart. The magnitude is a practitioner
  default, not a measurement.
- Let cymbals ring for their full sample unless they are choked.
- Keep the fill playable, or record the exception.
- Leave the timekeeping element tighter than the rest, and name marker parts.

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Kit-specific tells:

- the same snare sample repeated at one velocity, which is error 1 in its most obvious form;
- ghost notes made by lowering the velocity of a full stroke;
- open and closed hats with no continuous state and no foot;
- fills that need more than four limbs, which is error 6;
- cymbals truncated by short note lengths, which is error 12;
- close microphones only, with no room and no bleed;
- humanised timekeeping, which is error 13;
- every hit exactly on the grid with no hand-to-hand variation, when the style is not a grid style.

## What the Performance Director needs from this file

- `limb_or_finger_conflicts`: the four-limb rule, applied per tick, including the hi-hat foot.
- `simultaneity_exceeded`: more than four simultaneous hits, or more than two hand strikes.
- `articulation_unavailable`: ghost, rimshot, cross-stick and choke are separate samples; velocity
  substitution is reportable.
- `flam` and `velocity_asymmetry` are the recognised imperfection causes here.
- Marker part declaration: the kit or its pulse element usually belongs in `marker_parts_excluded`,
  and the plan should say which.

## Sources and what to verify

- `excerpt-derived` figures, the ghost velocity band and the choke implementation, came from
  programming guidance read as search excerpts. **Verify against the installed kit's documentation**,
  and prefer a calibration render over the range printed here.
- **To verify**: cymbal decay times and the spectral effect of strike position, in Fletcher and
  Rossing, *The Physics of Musical Instruments*. Not opened for this work.
- **Not available**: a measured flam interval. It is a practitioner default and is labelled as one in
  `shared/HUMAN_PERFORMANCE_SCHEMA.md`.
