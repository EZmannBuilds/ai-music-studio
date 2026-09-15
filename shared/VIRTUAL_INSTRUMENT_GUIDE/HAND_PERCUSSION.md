# Hand Percussion

**This is a frame page, not a content bucket.** Hand-struck drums belong to specific, living
traditions with their own vocabulary, technique, and lineage; there is no single "hand percussion
instrument" any more than there is a single "bowed string instrument" spanning violin, erhu, and
kamancheh. This page covers only the physics that genuinely are shared across most hand-struck
membranes, regardless of tradition, and routes every named drum to its own page. **Do not read the
one behaviour card below as a stroke vocabulary for any specific drum.** It is deliberately thinner
than that.

> Evidence: the shared-physics claims below rest on one acoustics-textbook page on tuned-drum
> membrane vibration modes (source ID WOODHOUSE-TUNED-DRUMS, general physics, read at section depth),
> generalised from a timpani-specific discussion to any struck membrane, since mode shape versus
> strike position is a property of a stretched membrane, not of a genre. Pitch-bending by localised
> tension is stated as a physical mechanism (membrane frequency rises with tension) rather than a
> measured figure for any specific instrument. Nothing tradition-specific here was read at the depth
> the gate in `CULTURALLY_SPECIFIC_INSTRUMENTS.md` requires to write about a named tradition, which is exactly why this page
> routes instead of summarising. Read depth and full citation are in `research/sources/INSTRUMENT_SOURCES.md`;
> the claims and their limits are in `research/instruments/HAND_PERCUSSION.md`.

Cross-family failures are in `COMMON_ERRORS.md`.

---

## Behaviour cards

### Hand-Struck Membranes (shared physics only)

Every row below states what is genuinely shared across hand-struck membranophones. A row that
depends on a specific tradition's technique or vocabulary is marked `varies by tradition: see
<page>` rather than filled in with one tradition's answer presented as universal.

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | A membrane (skin or synthetic head) stretched over a resonating shell, struck with the bare hand. Shell shape, depth, single- versus double-headed construction, and whether the bottom is open or closed all change the sound and are tradition- and instrument-specific. | inference |
| attack_behavior | Where the hand contacts the membrane changes which vibration modes are excited, not just how loud the strike is: a strike near the centre favours the membrane's lowest, most axisymmetric mode (low, round, low-overtone), while a strike nearer the rim excites a richer, brighter mix of higher, non-axisymmetric modes. This is the same physical mechanism documented for timpani strike position, applied here to any stretched membrane. | academic: WOODHOUSE-TUNED-DRUMS |
| sustain_behavior | An open stroke lets the membrane ring after impact; a muted or closed stroke (the hand left resting on the head, or immediately returned to it) damps the ring almost immediately. This open-versus-muted distinction is close to universal, though which strokes a given tradition names, and how many, is tradition-specific. | inference |
| release_behavior | As sustain_behavior: release is either a natural decay (open stroke) or an immediate, hand-damped stop (muted stroke); both are real, controlled techniques, not one default and one failure. | inference |
| dynamic_timbre_change | Harder strikes drive more high-partial energy relative to the fundamental, as with any struck membrane. | inference + to-verify: what would settle this is not recorded |
| register_character | Varies by tradition, drum size, and head tension: see the routing table below. | inference |
| practical_range | Most hand drums are not tuned to a fixed written pitch; some traditions do tune a drum or a drum pair to a reference pitch or to each other. Which applies is tradition-specific. | inference |
| tessitura | Varies by tradition. | inference |
| articulation_logic | Two broadly recurring, physically grounded stroke categories exist across many (not all) hand-drum traditions: an **open stroke** (struck nearer the rim, hand lifts immediately, membrane rings, more high-partial content) and a **bass stroke** (struck nearer the centre with the palm, hand lifts, favours the low fundamental mode, per attack_behavior above). A **slap** (a sharp, cupped-hand strike, usually near the edge, that traps and releases air against the head at the moment of impact for an especially bright, cracking attack) is widely but not universally present. **The specific three-stroke "bass, open, slap" vocabulary is conga and jembe terminology, not a universal hand-drum standard**, and this page does not extend it to traditions that name their strokes differently or divide the technique differently. See the routing table for each tradition's own vocabulary. | academic: WOODHOUSE-TUNED-DRUMS |
| phrase_limits | Two hands alternating sets a practical speed and pattern limit on essentially any hand drum, the same physical constraint as two-hand stick alternation on a snare drum; exact idiomatic patterns are tradition-specific. | inference |
| transitions | No legato; every stroke is a discrete hand contact. | inference |
| repeated_note_behavior | Two-hand alternation is the default mechanism for fast repeated patterns across most traditions; which hand plays which stroke, and any tradition's own sticking-equivalent conventions, are tradition-specific. | inference |
| vibrato | Not applicable in the sustained-pitch sense; see pitch_instability for the closer analogue. | inference |
| pitch_instability | Pressing the heel of the hand, or the fingers, into the membrane (typically near the rim) locally increases tension in that region, which raises the frequency of vibration there and bends the perceived pitch upward, a real, shared physical mechanism (a membrane's vibration frequency rises with its tension). Which traditions use this technique, what they call it, and how far the pitch is bent are tradition-specific. | inference |
| resonance | Shell shape and whether the far end is open, closed, or a second head changes how the membrane couples to an enclosed air volume; this varies enormously by tradition and is not summarised here. | inference |
| physical_noise | Hand-on-skin contact noise, a soft friction or slap sound distinct from the membrane's tuned response, is present on essentially every hand-struck drum and is part of the instrument's identity, not an artifact to filter out. | inference |
| feasibility | Two hands (occasionally a hand plus a stick, or a hand plus a foot, in specific traditions); a pattern needing more simultaneous strikes than hands available, or the same hand twice in immediate succession faster than a real player can re-strike, is not playable. Exact speed limits are drum- and tradition-specific. | inference |
| ensemble_behavior | Varies by tradition, from a solo lead-and-response role to a fixed ensemble part within a named, structured drum choir. | inference |
| recording_behavior | Normally close-miked; hand noise and skin contact are usually audible and are part of the instrument, not to be removed. Further convention is tradition-specific. | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Short notes trigger the sample; a held note does not extend a hand drum's natural decay, which is set by the stroke and the physical damping state, not by note length. | inference |
| overlap | Not a legato instrument. | inference |
| velocity | Should select among genuinely different recorded strokes (open, muted, bass, slap, and any further tradition-specific strokes) where the instrument's vocabulary has them, not only level within one recording; treating stroke type as a single velocity curve collapses the instrument's real vocabulary into one sound. | inference |
| continuous_dynamics | Not applicable to single discrete strokes. | inference |
| expression | Not the primary control for a single stroke. | inference |
| articulation_switching | Each named stroke in a tradition's vocabulary is a separate recorded sample set, not an EQ or gain variant of another stroke. | inference |
| round_robins | Essential; hand-percussion patterns repeat short figures rapidly, and repeated identical strokes are highly exposed. | inference |
| release_samples | The difference between an open stroke's natural ring and a muted stroke's immediate stop is a real release behaviour; collapsing both into one un-damped sample loses the muted technique entirely. | inference |
| pedal_or_breath_behavior | Not applicable to most hand drums; some traditions use a foot or a second player for a bass drum function (see, for instance, `JEMBE_AND_DUNUN.md` for the dunun's role), which is tradition-specific. | inference |
| transition_samples | Not applicable between discrete strokes; a heel-pressure pitch bend, where modelled, needs its own transition behaviour rather than a note-to-note glide built for a different instrument. | inference |
| mic_or_room_behavior | Close-miked by convention, with hand and skin noise intact; further convention is tradition-specific. | inference |
| likely_fake_sounding_errors | A tradition's real stroke vocabulary collapsed into one sample played at different velocities; a muted stroke played as an open stroke turned down instead of a genuinely damped recording; identical repeated strokes with no round robin; one tradition's stroke names or technique applied to a different tradition's drum. | inference |
| organic_programming_methods | Use the specific tradition's own stroke vocabulary and named techniques, sourced from that tradition's own page, rather than a generic "hand drum" model; vary strike contact and force per stroke (`velocity_asymmetry`); alternate hands for repeated patterns. | inference |

---

## What the instrument is

There is no single "hand percussion instrument." This page names only what several unrelated,
tradition-specific instruments share by virtue of all being membranes struck by a bare hand: a strike
excites vibration modes that depend on where and how the hand contacts the head, an open hand lifts
away and lets the membrane ring while a hand left on the head damps it, and two hands alternating is
the near-universal mechanism for fast repeated playing. Everything past that is a specific
tradition's own instrument, technique, and vocabulary. [academic: WOODHOUSE-TUNED-DRUMS + inference]

## Range and register

Not summarised here; register depends entirely on the specific drum, its size, its head tension, and
its tradition's tuning practice (if it has one). See the routing table. [inference]

## Articulation and note transitions

The one genuinely cross-tradition physical fact worth stating plainly: **striking nearer the centre
of a membrane favours its lowest, roundest, most overtone-poor mode, and striking nearer the rim
excites a brighter mix of higher modes.** This is why "a bass tone near the centre, a brighter tone
near the edge" recurs across so many unrelated traditions independently, it is a property of stretched
membranes, not a borrowed convention. **A prior version of `PERCUSSION.md` presented "bass, open,
slap" as the core three strokes on most hand drums.** That is conga and jembe vocabulary, real and
well documented for those traditions, but printed as if it generalised to hand percussion as a whole.
This page corrects that: the underlying bass-versus-open physics generalises, the specific
three-stroke framework, its names, and its exact technique do not, and this page does not repeat the
error by offering a substitute universal vocabulary of its own. [academic: WOODHOUSE-TUNED-DRUMS]

## Physical constraints

Two hands, and each can strike once at a time. This sets a practical alternation-speed limit shared
by essentially every hand drum, the same physical fact that limits two-hand stick alternation on a
snare drum. Exact idiomatic patterns, and any further limbs a specific tradition's ensemble role adds
(a foot, a second player, a stick used alongside the hand), are named on that tradition's own page.
[inference]

## Phrase behaviour

Not summarised here; bounded by damping, by hand alternation, and by whatever structural conventions
(call and response, fixed ensemble parts, cyclic form) the specific tradition uses. See the routing
table. [inference]

## Ensemble behaviour

Not summarised here; varies from a solo, expressive lead role to a fixed part inside a large, named
drum ensemble with its own internal hierarchy. See the routing table. [inference]

## Recording behaviour

Hand percussion is usually close-miked, and hand noise, skin contact, and the body of the drum are
audible and are the instrument, not incidental noise to remove. Further convention is
tradition-specific. [inference]

## Programming it: the control model

```text
velocity: should select a genuinely different recorded stroke where the tradition's vocabulary has
  one, not only level within one stroke
round_robins: essential; short repeated figures are the norm across this whole family
stroke_vocabulary: tradition-specific; do not substitute one tradition's stroke names for another's
pitch_bend: a real, physical technique (localised tension) on drums whose tradition uses it; not a
  generic pitch wheel behaviour borrowed from a melodic instrument
```

[inference]

## Programming it: what makes it sound real

- Identify the specific tradition and drum before writing anything, and go to that tradition's own
  page for its stroke vocabulary, tuning practice, and ensemble role. [inference]
- Use the tradition's own stroke names and technique, not a generic bass/open/slap template borrowed
  from a different tradition. [inference]
- Alternate hands for repeated patterns, and vary contact and force per stroke. [inference]
- Where a heel-pressure or finger-pressure pitch bend is part of the tradition, model it as the real,
  physical mechanism it is (rising tension raising pitch), not as a generic instrument pitch wheel.
  [inference]

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Family-specific tells:

- one tradition's stroke vocabulary (most often conga/jembe's bass-open-slap) applied to a different
  tradition's drum; [inference]
- a muted stroke played as an open stroke turned down, rather than a genuinely damped recording;
  [inference]
- identical repeated strokes with no round robin, especially exposed given how short and repetitive
  most hand-percussion figures are; [inference]
- a generic "world percussion" patch standing in for a specific, named tradition, which is exactly
  the failure `shared/MUSICAL_SYSTEMS/INDEX.md` rule 2 names and this page is built to avoid
  repeating. [inference]

## What the Performance Director needs from this file

- `limb_or_finger_conflicts`: two hands, and a pattern needing a third simultaneous strike (beyond
  any tradition-specific extra limb, named on that tradition's page) is not playable.
- `articulation_unavailable`: each named stroke in a tradition's vocabulary is a separate recording;
  a request for a stroke the instrument or the tradition does not have is reported, not silently
  substituted from a different tradition's vocabulary.
- Route every feasibility and articulation question that depends on a specific tradition's technique
  to that tradition's own page; this file does not answer them.

## Where each tradition's drums are covered

| Drum(s) | Tradition | Page |
|---|---|---|
| Conga (tumbadora), bongó | Cuban | `CUBAN_HAND_PERCUSSION.md` |
| Jembe, dunun | Mande jembe music (Mali, Guinea) | `JEMBE_AND_DUNUN.md` |
| Ewe drums (e.g. sogo, kidi, kagan, atsimevu) | Ewe (Ghana/Togo) | `EWE_DANCE_DRUMS.md` |
| Tabla | Hindustani (North Indian) | `TABLA.md` |
| Mridangam | Carnatic (South Indian) | `MRIDANGAM.md` |
| Frame drums (e.g. bendir, riq, daf, pandeiro, bodhrán) | many independent traditions, each with its own drum and technique | no page yet |
| Darbuka / darbuki / doumbek | several goblet-drum traditions (Arabic, Turkish and others), not one | no page yet |
| Cajón | Afro-Peruvian in origin, later adopted into flamenco practice | no page yet |
| Udu | Igbo (Nigeria) | no page yet |

**"No page yet" is a gap in this project's coverage, not a judgement that the tradition matters
less.** Writing any of these properly requires the same gate as every other tradition page:
the gate in `CULTURALLY_SPECIFIC_INSTRUMENTS.md` section 3: at least two independent specialist sources read at section or
full depth, at least one of them a practitioner, teacher, tradition institution, or ethnomusicological
fieldwork source. That gate was not attempted for these instruments in this pass. [inference]

## Sources and what to verify

- The one `academic` claim on this page (strike position versus excited membrane mode) rests on one
  acoustics-textbook page written about timpani specifically, generalised here to any stretched
  membrane on physical grounds (mode shape versus strike position is a property of the membrane, not
  of the ensemble or tradition it appears in). Full citation in `research/sources/INSTRUMENT_SOURCES.md`.
- **To verify**: driven-membrane non-linearity (why harder strikes brighten the tone), in Fletcher and
  Rossing, *The Physics of Musical Instruments*. Not opened this pass.
- **To verify**: the pitch-bend-by-tension mechanism is standard membrane physics (frequency rises
  with tension) but was not independently measured or read in a source specific to any named
  hand-drum tradition this pass; treat the mechanism as physically sound and the specific magnitude,
  for any given tradition, as unverified until that tradition's own page addresses it.
- **Not available, and correctly absent from this file**: any tradition-specific stroke vocabulary,
  tuning practice, ensemble role, or repertoire content. That is the entire point of a frame page.
