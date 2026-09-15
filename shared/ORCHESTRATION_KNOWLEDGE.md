# Orchestration Knowledge

A reference page, maintained across releases rather than written per session by any specialist at
runtime — the same register as `shared/GENERALIZATION_RULES.md` and the `shared/MUSICAL_SYSTEMS/`
files. It holds knowledge about how instruments combine, what orchestral gestures are and how they
are built, and how an orchestral layer and an electronic layer divide functional roles in a hybrid
arrangement. It does not hold new per-instrument facts: those stay in
`shared/VIRTUAL_INSTRUMENT_GUIDE/`, and this file points at them rather than repeating them.

> Evidence: read at section depth this pass, newly, for combination and colour content specifically
> (not reused from the per-family read): Rimsky-Korsakov's *Principles of Orchestration* (RIMSKY-1913,
> already registered at `section` depth for per-instrument chapters read in earlier passes) —
> Chapter I's "Comparison of Resonance in Orchestral Groups and Combination of Different Tone
> Qualities", the group-combination subsections of Chapter II ("Melody in Different Groups
> Combined") and Chapter III ("Harmony in Combined Groups"), and Chapter IV's "Chords of Different
> Tone Quality Used Alternately", "Amplification and Elimination of Tone Qualities", "Crescendo and
> Diminuendo", "Diverging and Converging Progressions", "Economy in Orchestral Colour" and "Use of
> Percussion Instruments for Rhythm and Colour". Fetched via the Gutenberg plain-text edition
> (https://www.gutenberg.org/cache/epub/33900/pg33900.txt) this pass. **Cecil Forsyth's
> *Orchestration* (FORSYTH-1914) was also fetched this pass** (archive.org full text), specifically
> searching for its Brass and Wood-Wind "Preliminary" sections, where a combination discussion would
> most likely sit; those sections were not reachable within what the fetch tool returned, so no new
> Forsyth combination claim is added here — this is recorded honestly rather than papered over, and
> those two sections are named `to-verify` below. Section 3 (percussion roles) reuses, and does not
> re-derive, facts already established in `shared/VIRTUAL_INSTRUMENT_GUIDE/DRUM_KIT.md`, `shared/VIRTUAL_INSTRUMENT_GUIDE/PERCUSSION.md` and `shared/VIRTUAL_INSTRUMENT_GUIDE/MALLETS.md`. Section 2
> (register-character index) adds no instrument facts at all; it is pointers. Section 5 (hybrid
> orchestra+electronic roles) is `inference`/synthesis and is labelled as such throughout, per
> `shared/RESEARCH_RULES.md`. Piston (`PISTON-1955`/`PISTON-ORCH`) and Adler
> (`ADLER-1989`/`ADLER-ORCH`/`ADLER-STUDYOFORCH`) remain `standard-reference` only; neither was opened
> this pass or any prior one. Source IDs resolve in `research/sources/INSTRUMENT_SOURCES.md`.

Cross-family failures are in `shared/VIRTUAL_INSTRUMENT_GUIDE/COMMON_ERRORS.md`. They still apply.

---

## 0. What this file is for, gating, and failure behavior

**Gating.** Every section below applies only when the brief's instrumentation actually calls for it —
an orchestral or hybrid orchestral/electronic ensemble genuinely on the page, checked instrument by
instrument, never triggered by genre name or by "this sounds like it wants strings." This is the same
gate `shared/MUSICAL_SYSTEMS/` files use and the same one `shared/ORCHESTRAL_VOICING_SCHEMA.md`
section 2 uses for divisi: a condition an arrangement either has or does not have. Per
`shared/GENERALIZATION_RULES.md`, no genre or instrumentation is a default; this file is read when the
instrumentation is orchestral or hybrid, not because a track "feels cinematic."

**Failure behavior.** This is a reference page, not a required step. **Absence of an entry here means
Arranger falls back to its existing, generic `instrument_role` reasoning
(`arranger/SKILL.md`, "Instrument role map"), exactly as today.** Producer's existing "Sound-role
thinking" (`producer/SKILL.md`) is likewise unchanged where this file is not consulted. Nothing here
is a required gate on either skill; it is additional knowledge to draw on when the instrumentation
warrants it.

**Who writes what.** Arranger is the primary author of `color_combination` and `gesture` entries and
of the instrumental side of `role_assignment` (section 3, and the orchestral half of section 5).
Producer authors the electronic-layer half of `role_assignment` in a hybrid brief (section 5). Neither
skill's mission changes; this file is a new input each already knows how to use in its existing
`instrument_role` / sound-role vocabulary.

---

## 1. Color combination knowledge

```yaml
color_combination:
  instruments: []
  register:
  blend: []                 # e.g. "clarinet fills flute's weak low register"
  projection:
  useful_for: []
  risks: []
  evidence:                 # per RESEARCH_RULES.md
```

### Horn + bassoon

```yaml
color_combination:
  instruments: [horn, bassoon]
  register: middle
  blend:
  - "the horn's middle notes resemble the bassoon's in colour, and the two blend well together"
  - "the horn is the named link between the brass and wood-wind groups; the bassoon is its usual
    wood-wind partner in that role"
  projection: moderate; a blend rather than a doubling for power
  useful_for: [bridging a wood-wind passage into brass without a hard timbral seam, a middle-register
    duet that reads as one composite colour]
  risks: [both instruments are comparatively weak in forte tutti (see the power-ratio entry below);
    the blend favours middle dynamics and register more than extremes]
  evidence: "sourced: RIMSKY-1913"
```

### Stopped/muted horn and trumpet + oboe/English horn

```yaml
color_combination:
  instruments: [horn (stopped), trumpet (muted), oboe, english horn]
  register: middle to upper-middle
  blend:
  - "stopped and muted notes in horns and trumpets take on a quality similar to the oboe and English
    horn, and blend tolerably well with the latter instrument"
  projection: reduced by the mute/stopping itself; see BRASS.md for the pitch-rise this technique
    also causes on horn, which this entry does not repeat
  useful_for: [a covered, reedy brass colour standing in for or doubling a double-reed line without
    the brass simply overpowering it]
  risks: [a mute or stopping change needs real setup time, per BRASS.md's Physical constraints
    section; this is a deliberate colour choice, not a free substitute for an open brass tone]
  evidence: "sourced: RIMSKY-1913 + sourced: UNSW-BRASS (for the stopped-horn mechanism itself, cross-
    referenced from BRASS.md, not re-derived here)"
```

### String harmonics + flute/piccolo

```yaml
color_combination:
  instruments: [violin/viola/cello harmonics, flute, piccolo]
  register: upper
  blend:
  - "the relationship between string harmonics and the flute or piccolo's own tone is named as a
    link between the string and wood-wind groups at the top of the range"
  projection: both are comparatively thin and reduced-power at this register; STRINGS.md notes
    harmonics give "a glassy, reduced-power tone with little dynamic range"
  useful_for: [a cool, glassy high colour built from two families rather than one, where a single
    instrument's top register would sound thin alone]
  risks: [neither element projects strongly; this is a colour combination for a quiet or mid-dynamic
    passage, not for cutting through a tutti]
  evidence: "sourced: RIMSKY-1913 + manual-derived: STRINGS-LIBRARY-MANUAL-1 (harmonics' own reduced
    power, cross-referenced from STRINGS.md)"
```

### Viola, bassoon and clarinet chalumeau register (a middle-register family)

```yaml
color_combination:
  instruments: [viola, bassoon, clarinet (chalumeau register)]
  register: middle
  blend:
  - "the viola's timbre is vaguely compared to the bassoon's middle register and to the clarinet's
    lowest (chalumeau) compass, naming all three as occupying a related colour in the middle of the
    orchestra"
  projection: covered, not brilliant; the character these three instruments share at this register
  useful_for: [an inner-voice colour that reads as one family regardless of which of the three
    actually carries it, useful for a held middle line under a more active outer texture]
  risks: [a comparison of vague resemblance, not identical timbre — treat as a family relationship
    that justifies substitution or doubling, not as literal interchangeability]
  evidence: "sourced: RIMSKY-1913"
```

### A single wind added to a full string section, and the reverse

```yaml
color_combination:
  instruments: [any one wood-wind instrument, full string department (e.g. all first violins)]
  register: any, matched
  blend:
  - "one wind instrument added to a full department of strings in unison thickens the resonance of
    the strings; the wood-wind's own timbre is largely lost in the process"
  - "conversely, one department of strings added to the wood-wind in unison produces a sweet, coherent
    quality in which the wood-wind timbre still predominates"
  projection: asymmetric — the larger group's character wins in both directions, but a string
    department outweighs a single wind instrument more than the reverse
  useful_for: [reinforcing a string line's body without changing its colour (add one wind); adding
    warmth to a wood-wind melody without covering its identity (add one string department)]
  risks: [treating the two directions as symmetrical — the combination reads differently depending on
    which group is "added to" the other, not only on which instruments are named]
  evidence: "sourced: RIMSKY-1913"
```

### Strings and brass in unison (a deliberate non-blend)

```yaml
color_combination:
  instruments: [string section, brass section]
  register: any, matched
  blend:
  - "strings and brass do not blend so well together as either does with wood-wind; each is heard too
    distinctly, so the combination reads as two groups juxtaposed rather than one fused colour"
  - "uniting all three groups — strings, wood-wind and brass — on the same material produces a rich,
    mellow and coherent tone the two-group strings+brass combination does not reach on its own"
  projection: high (both groups are individually strong); clarity of the seam, not fusion, is the
    actual effect
  useful_for: [a deliberately layered, non-fused tutti texture where the two groups' separateness is
    the point; as the named fix, adding wood-wind as the third group when a fused, blended tutti is
    wanted instead]
  risks: [expecting strings-plus-brass alone to fuse the way strings-plus-wood-wind or wood-wind-plus-
    brass do; it does not, on this source's own account]
  evidence: "sourced: RIMSKY-1913"
```

### Power balance across families (a combination-planning fact, not a mixing fact)

```yaml
color_combination:
  instruments: [horn, trumpet, trombone, tuba, clarinet, oboe, flute, bassoon, string department]
  register: any
  blend:
  - "at forte, 1 trumpet = 1 trombone = 1 tuba = 2 horns in relative power; a single horn is
    comparably matched by roughly 2 clarinets, 2 oboes, 2 flutes, or 2 bassoons"
  - "at piano, all wind instruments — wood or brass — are of fairly equal balance with each other"
  - "a full department of one string part (e.g. all first violins) is equivalent in strength to about
    one wind instrument at piano, but needs roughly two wind instruments to match it at forte"
  projection: this is a compositional balance fact, decided before any fader is touched — it says how
    many instruments of one kind are needed to match another in the notated dynamic, not a mix level
  useful_for: [choosing how many players double a line so that two different-family unisons actually
    sound balanced against each other at the intended dynamic; deciding how many wind parts a solo
    string department needs to be matched by, or vice versa]
  risks: [this is Rimsky-Korsakov's own late-Romantic orchestra as the working example; ratios are a
    planning heuristic, not a measured acoustic law, and are `to-verify` against Fletcher and Rossing
    or a measured source before being treated as precise]
  evidence: "sourced: RIMSKY-1913 + to-verify: a measured-power-ratio source (Fletcher and Rossing was
    not opened for this pack)"
```

---

## 2. Register-character index

This section adds no new instrument facts. It is pointers into the already-researched family pages,
so a color-combination or gesture decision above can be checked against a specific instrument's actual
register behaviour without this file repeating it and risking drift from the family page's own
research.

| Family | Page | Row to check |
|---|---|---|
| Violin, viola, cello, double bass, string section | `shared/VIRTUAL_INSTRUMENT_GUIDE/STRINGS.md` | `register_character`, `practical_range`, `tessitura` per instrument card |
| Horn, trumpet, trombone, tuba, brass section | `shared/VIRTUAL_INSTRUMENT_GUIDE/BRASS.md` | `register_character`, `practical_range`, `tessitura` per instrument card |
| Flute, oboe, clarinet, bassoon, saxophone and section | `shared/VIRTUAL_INSTRUMENT_GUIDE/WOODWINDS.md` | `register_character`, `practical_range`, `tessitura` per instrument card |
| Harp | `shared/VIRTUAL_INSTRUMENT_GUIDE/HARP.md` | `register_character`, `practical_range` |
| Choir and solo voice | `shared/VIRTUAL_INSTRUMENT_GUIDE/CHOIR_AND_VOICE.md` | `register_character`, `practical_range`, `tessitura` |
| Piano and keyboards | `shared/VIRTUAL_INSTRUMENT_GUIDE/PIANO_AND_KEYBOARDS.md` | `register_character`, `practical_range` |
| Marimba, vibraphone, xylophone, glockenspiel, tubular bells, crotales | `shared/VIRTUAL_INSTRUMENT_GUIDE/MALLETS.md` | `register_character`, `practical_range` (mind written-vs-sounding octave for xylophone/glockenspiel/crotales) |
| Timpani, orchestral snare, bass drum, cymbals, tam-tam, triangle, tambourine, blocks, castanets | `shared/VIRTUAL_INSTRUMENT_GUIDE/PERCUSSION.md` | `register_character`, `practical_range` where pitched |
| Kick, snare, toms, hi-hat, ride/crash | `shared/VIRTUAL_INSTRUMENT_GUIDE/DRUM_KIT.md` | `register_character` |
| Synths and samplers (the electronic-layer half of section 5) | `shared/VIRTUAL_INSTRUMENT_GUIDE/SYNTHS_AND_SAMPLERS.md` | `register_character` |

**How to use this table.** Before writing a `color_combination` or `gesture` entry that names a
specific register (e.g. "cello's tenor register", "the top of the violin's range"), check the family
page's own card rather than restating a remembered figure — practical ranges in this pack are
periodically corrected (STRINGS.md and BRASS.md both record corrections to a prior release's numbers),
and this index exists specifically so that correction only has to happen in one place. [inference]

---

## 3. Orchestral-percussion role layer

A role layer built on top of the facts `shared/VIRTUAL_INSTRUMENT_GUIDE/DRUM_KIT.md`, `shared/VIRTUAL_INSTRUMENT_GUIDE/PERCUSSION.md` and `shared/VIRTUAL_INSTRUMENT_GUIDE/MALLETS.md` already
establish — this section does not re-derive timbre, technique or evidence those pages already carry;
it names the *function* a percussion part serves in an ensemble or orchestral texture, which those
pages deliberately leave to arrangement.

Rimsky-Korsakov draws exactly this rhythm/colour split for unpitched percussion: instruments
"producing indeterminate sounds play no melodic or harmonic part, their functions being purely
rhythmical," naming kettle-drums, side drum and bass drum for that rhythmic role, while triangle,
castanets, cymbals and the gong are "ornamental instruments pure and simple," with "no intrinsic
musical meaning" of their own beyond colour. The same source cautions that percussion "should only be
employed at reasonable intervals," and that constant elaborate combinations produce "a dull, neutral
texture" where simpler, sparing use gives "infinitely greater scope for variety in colour."
[sourced: RIMSKY-1913]

```yaml
role_assignment:
  bar_range:
  role: pulse | transition | impact | tension | color | emotion_carrier | movement | scale_extender
  instruments: []
```

### Pulse

```yaml
role_assignment:
  bar_range: "throughout a march or a driving passage"
  role: pulse
  instruments: [timpani (single strokes or a held roll under the beat), orchestral or kit snare,
    bass drum]
```

Named directly as the rhythmic-function group. [sourced: RIMSKY-1913] `shared/VIRTUAL_INSTRUMENT_GUIDE/DRUM_KIT.md`'s own finding —
that a kit's timekeeping element is often, but not always by default, the part carrying the least
timing deviation — extends cleanly to an orchestral pulse part: whichever instrument is named `pulse`
here is the candidate for `marker_parts_excluded` in `shared/HUMAN_PERFORMANCE_SCHEMA.md`, decided per
track as `shared/VIRTUAL_INSTRUMENT_GUIDE/DRUM_KIT.md` "Ensemble behaviour" already argues, not assumed. [inference, extending
sourced: RASANEN-2015 as read for `shared/VIRTUAL_INSTRUMENT_GUIDE/DRUM_KIT.md`]

### Transition

```yaml
role_assignment:
  bar_range: "the last bar or two of a section before a new one lands"
  role: transition
  instruments: [suspended cymbal (soft-stick roll, building), snare roll leading into a downbeat]
```

`shared/VIRTUAL_INSTRUMENT_GUIDE/PERCUSSION.md`'s suspended-cymbal card documents the soft-stick roll as usable at any dynamic with a
"deep, gong-like quality," which is what makes it a connective, not a struck-event, colour; its own
long ring already reads as forward motion into whatever follows. [sourced: FORSYTH-1914, as read for
`shared/VIRTUAL_INSTRUMENT_GUIDE/PERCUSSION.md`] The orchestral snare's roll conventionally ends on a written, detached finishing
stroke rather than an unmarked stop, which is exactly the shape a transition into a downbeat needs.
[sourced: FORSYTH-1914, as read for `shared/VIRTUAL_INSTRUMENT_GUIDE/PERCUSSION.md`]

### Impact

```yaml
role_assignment:
  bar_range: "the downbeat a buildup lands on"
  role: impact
  instruments: [bass drum, clashed cymbals, tam-tam (single stroke, used once)]
```

The clashed-cymbal-and-bass-drum pairing is the named conventional impact combination, though the
source itself calls the pairing "a habit without a clear musical reason" and warns that overused
together they can bury harmony and melody in noise — using it as a deliberate, occasional impact
event rather than a reflex is the reading this file carries forward. [sourced: FORSYTH-1914, as read
for `shared/VIRTUAL_INSTRUMENT_GUIDE/PERCUSSION.md`] A single tam-tam stroke is a distinct, heavier-weight impact option, usable
"effectively only once in a work" because of its dramatic weight. [sourced: FORSYTH-1914, as read for
`shared/VIRTUAL_INSTRUMENT_GUIDE/PERCUSSION.md`]

### Tension

```yaml
role_assignment:
  bar_range: "a held passage before a structural arrival"
  role: tension
  instruments: [tam-tam (graduated crescendo roll), suspended cymbal roll, timpani roll with a drawn
    crescendo]
```

The tam-tam's graduated roll — building from a real, continuous, time-evolving attack rather than a
single stroke — is the source's own primary technique for its p to ff range, and is a distinct event
from the single-stroke impact use above, not a longer version of it. [sourced: FORSYTH-1914, as read
for `shared/VIRTUAL_INSTRUMENT_GUIDE/PERCUSSION.md`] A timpani roll is the family's own sustained-crescendo device and "can carry the
most gradual crescendo or diminuendo in the percussion section." [sourced: RIMSKY-1913, as read for
`shared/VIRTUAL_INSTRUMENT_GUIDE/PERCUSSION.md`]

### Color

```yaml
role_assignment:
  bar_range: "a single bright event marking a phrase change or harmonic shift"
  role: color
  instruments: [triangle, glockenspiel, crotales, tambourine (thumb tremolo), castanets]
```

These are the instruments named as ornamental rather than structural — "no intrinsic musical
meaning" beyond the colour itself. [sourced: RIMSKY-1913] The triangle card in `shared/VIRTUAL_INSTRUMENT_GUIDE/PERCUSSION.md` names
this exact structural use: "a single bright event that 'sets free' a new phrase at a change of harmony
or colour, used once, not repeated at every similar structural moment." [sourced: FORSYTH-1914, as
read for `shared/VIRTUAL_INSTRUMENT_GUIDE/PERCUSSION.md`]

**Failure behavior, restated for this section specifically.** With no `role_assignment` entry for a
percussion part, it is written and evaluated exactly as `shared/VIRTUAL_INSTRUMENT_GUIDE/DRUM_KIT.md`/`shared/VIRTUAL_INSTRUMENT_GUIDE/PERCUSSION.md`/`shared/VIRTUAL_INSTRUMENT_GUIDE/MALLETS.md`
already do on their own — this role layer is additive framing for *why* a part exists in the
arrangement, not a new requirement those pages' own behaviour cards and feasibility checks depend on.

---

## 4. Orchestral-gesture mechanisms

```yaml
gesture:
  name:                     # string swell, brass bloom, woodwind cascade, etc.
  musical_function:
  construction:
  dynamic_behavior:
  typical_risks:
  evidence:
```

### Orchestral crescendo by addition

```yaml
gesture:
  name: orchestral crescendo by addition
  musical_function: build toward a structural arrival by growing the ensemble, not only by growing
    each existing part's dynamic marking
  construction: "progressively introduce additional instrumental groups into a held or repeating
    idea, rather than relying on individual-instrument dynamics alone to carry a crescendo; the
    converse device withdraws instruments one by one for a diminuendo, rather than a uniform dynamic
    decrease across a static instrumentation"
  dynamic_behavior: cumulative — mass increases in discrete steps as each new group enters, layered on
    top of, not instead of, each individual part's own written dynamic shape
  typical_risks: "every group entering at the same written dynamic and the same curve, which produces
    E1's near-miss (`evals/cases/performance/E1.yaml`) — one shared curve copied onto every part rather
    than a real hierarchy of who leads and who is held back"
  evidence: "sourced: RIMSKY-1913"
```

### String swell

```yaml
gesture:
  name: string swell
  musical_function: connective tissue under a woodwind or brass entrance, or a held crescendo that
    does not itself need a new attack
  construction: "a bowed string section's own continuous, bow-fed sustain (STRINGS.md,
    sustain_behavior) drawn as a phrase-level dynamic curve on a held or slowly-moving chord; because
    the bow keeps re-energising the string, the swell has no natural decay to fight the way a struck
    or plucked gesture does"
  dynamic_behavior: continuous and controllable in real time by bow speed, pressure and contact point
    together, per STRINGS.md's control model; a section's version of this smears its onset slightly
    across players (`ensemble_spread`), which is correct and should not be tightened
  typical_risks: "a flat sustain with no drawn shape, STRINGS.md error 2 in its clearest form; treating
    the swell as available from a single bow stroke on a full chord, which STRINGS.md's `feasibility`
    row rules out for three- or four-note chords regardless of open strings"
  evidence: "manual-derived: STRINGS-LIBRARY-MANUAL-1 (cross-referenced from STRINGS.md) + sourced:
    RIMSKY-1913 (the crescendo-by-addition mechanism this gesture is often layered under)"
```

### Brass bloom

```yaml
gesture:
  name: brass bloom
  musical_function: mark a climax or arrival with a disproportionate increase in brightness, not only
    loudness — the sound itself changes character at the peak, not merely its level
  construction: "a brass section's dynamic increase, drawn as a crossfading dynamic-layer control per
    BRASS.md rather than a single sample turned up; louder brass playing drives the lips into sharper,
    nonlinear closure, adding high-harmonic content the ear also hears as louder, and at the extreme
    this has been measured, on trombone specifically, as actual shock-wave formation in the bore"
  dynamic_behavior: "brightness and loudness rise together and cannot be separated — there is no brass
    control that changes one without the other (BRASS.md, academic: UNSW-BRASS)"
  typical_risks: "building the bloom as a volume fader move on a loud sample, which keeps the bright
    spectrum of a loud attack at a quiet level and is BRASS.md's/COMMON_ERRORS.md error 10 in its
    clearest brass form; reserving the technique for every climax rather than sparingly, which
    Rimsky-Korsakov's economy-of-colour argument below applies to brass as much as to percussion"
  evidence: "academic: UNSW-BRASS + academic: HIRSCHBERG-1996 (both cross-referenced from BRASS.md) +
    sourced: RIMSKY-1913 (economy of colour, read this pass)"
```

### Woodwind cascade

```yaml
gesture:
  name: woodwind cascade
  musical_function: a single running line — a scale, an arpeggio, a rapid figure — handed from one
    wood-wind instrument to the next as it crosses the ensemble's combined register, so the figure
    keeps one continuous contour while its colour changes underneath it
  construction: "the handoff point is chosen where the outgoing instrument's own register starts to
    thin or become effortful and the incoming instrument's register is comfortable — check each named
    instrument's own register_character/tessitura row via section 2's index rather than assuming a
    fixed handoff pitch, since practical ranges differ by instrument and by library"
  dynamic_behavior: "each instrument carries its own dynamic layer across its segment of the figure;
    a cascade with one flat dynamic imposed across every instrument's segment loses the shape a single
    player would give their own portion of a fast passage"
  typical_risks: "an audible seam at the handoff if the two instruments' dynamic layers do not meet at
    a matched level; a handoff placed at a pitch that is comfortable on neither instrument rather than
    strong on the outgoing one and secure on the incoming one"
  evidence: "inference — built from the register-thinning pattern this pack's family pages document
    for every instrument (see section 2), and from general orchestral practice, but the specific
    Rimsky-Korsakov section most directly on point, 'Transference of Passages and Phrases' (Chapter
    IV), was not successfully reached in this pass's fetches; treat the naming and the general
    mechanism as inference until that section is read. [to-verify: Rimsky-Korsakov, Principles of
    Orchestration, Chapter IV, 'Transference of Passages and Phrases']"
```

### Colour alternation

```yaml
gesture:
  name: colour alternation
  musical_function: keep one harmonic idea from going stale by presenting it through a different
    instrumental colour each time it recurs, without changing the harmony itself
  construction: "the same chord or short progression is passed between instrumental groups —
    strings, then wood-wind, then brass — rather than sustained in one colour throughout its
    repetitions"
  dynamic_behavior: "not itself a dynamic device; it can be combined with, but is distinct from,
    crescendo-by-addition above — colour changes while level need not"
  typical_risks: "alternating so quickly or so often that the ear stops registering each colour as
    distinct, which is the same fatigue Rimsky-Korsakov's economy-of-colour argument (below) warns
    against for percussion and, on this evidence, generalises to any repeated colour device"
  evidence: "sourced: RIMSKY-1913"
```

### Diverging/converging registral gesture

```yaml
gesture:
  name: diverging/converging registral gesture
  musical_function: an expressive and architectural device independent of harmonic function — widen
    the ensemble's registral space outward for an opening, expansive feeling, or narrow it inward for
    compression or conclusion
  construction: "outer voices move apart toward extreme registers (diverging) or move together toward
    a central range (converging), tracked across whichever instruments currently hold the outer
    voices, which may change hands as the gesture crosses instrument ranges"
  dynamic_behavior: "independent of loudness; a diverging gesture is not automatically a crescendo, and
    combining the two (register opening outward while mass and level also increase) is a deliberate
    stacking of two named devices, not one device"
  typical_risks: "treating registral spread as automatically louder or more energetic — the source
    names it as an architectural/expressive tool distinct from dynamics, and stacking it with
    crescendo-by-addition without noticing is stacking two devices as if they were one"
  evidence: "sourced: RIMSKY-1913"
```

**Economy of colour, as a cross-cutting rule for this whole section.** Continuous use of elaborate
combinations "exhausts listener attention and diminishes impact of significant moments"; reserving a
gesture — a bloom, a swell, a cascade, a colour alternation — for the passage that actually needs it,
and using simpler means elsewhere, is what makes the reserved use land. [sourced: RIMSKY-1913] This is
the same principle `shared/VIRTUAL_INSTRUMENT_GUIDE/PERCUSSION.md` already states for the tam-tam and triangle specifically; here it
is named as general practice across every gesture in this section.

---

## 5. Hybrid orchestra+electronic functional-role vocabulary

**This section is inference and synthesis, not sourced orchestration pedagogy.** No source read for
this pack addresses how an orchestral layer and an electronic layer should divide function in a hybrid
arrangement — that combination postdates every text in the register by a century or more. Everything
below is `inference`: reasoned extension of the roles named in sections 1, 3 and 4 above (all of which
are genuinely sourced) to an electronic layer that has no equivalent literature in this register. Do
not present this section's conclusions with a confidence sections 1, 3 or 4 have earned and it has
not.

**Gating, restated.** This section applies only to a brief whose instrumentation genuinely combines
an orchestral or acoustic layer with an electronic one — synth, sampler, sub, programmed drums, a
processed or synthetic texture — sounding together, not to an orchestral piece alone (use sections 1–4)
or an electronic piece alone (Producer's existing sound-role thinking is unchanged and sufficient).

The fixed role vocabulary from section 3 continues here unchanged: `pulse | transition | impact |
tension | color | emotion_carrier | movement | scale_extender`. Sections 1–4 showed orchestral
instruments filling `pulse`, `transition`, `impact`, `tension` and `color`; a hybrid brief typically
also needs `emotion_carrier`, `movement` and `scale_extender`, and an electronic layer is often the
more natural home for some of them.

```yaml
role_assignment:
  bar_range: "the section a solo or featured line carries the emotional weight"
  role: emotion_carrier
  instruments: [solo cello, solo violin, lead vocal or vocal texture layer, a lead synth patch]
```

An `emotion_carrier` can be orchestral or electronic; the deciding factor is which element the
arrangement is actually asking the listener to feel through, not which family it belongs to.
[inference]

```yaml
role_assignment:
  bar_range: "a passage that needs continuous internal motion under a held harmony"
  role: movement
  instruments: [harp arpeggiation, a synth arpeggiator or sequenced pluck, tremolo strings]
```

Orchestral and electronic instruments both have idiomatic ways to fill `movement` — a harp figure and
a sequenced arpeggiator do the same job with different means — so this role is genuinely open to
either layer, decided by the sound wanted rather than by mechanism. [inference]

```yaml
role_assignment:
  bar_range: "throughout, wherever the orchestral bass register needs to extend"
  role: scale_extender
  instruments: [sub bass (synthesized or sampled)]
```

This is the clearest orchestra/electronic asymmetry in the vocabulary. `shared/VIRTUAL_INSTRUMENT_GUIDE/STRINGS.md`'s own curated
double bass range bottoms out at written C1 (sounding an octave down), with a low extension to
sounding C0 on some instruments; a synthesized sub bass has no such acoustic floor and is the natural
`scale_extender` when a hybrid arrangement wants weight below what the acoustic bass register reaches.
[inference, extending manual-derived: STRINGS-LIBRARY-MANUAL-1 as read for STRINGS.md] The reverse
almost never applies — an acoustic instrument is rarely asked to extend an electronic layer's range
upward or downward, because synthesis has no comparable ceiling or floor to extend past.

**Working example, and how it differs from stacking every layer identically.** A hybrid cue combining
strings, a synth pad, a sub bass, brass stabs and a wordless vocal-texture layer does not default every
element to the same role. A plausible distinct assignment: strings as `emotion_carrier` (the melodic,
expressive weight), synth pad as `color` (harmonic wash, not the lead), sub bass as `scale_extender`
(the low end no acoustic instrument in the cue reaches), brass stabs as `impact` (structural accents,
per section 3's impact entry generalised to a hybrid context), and the vocal-texture layer as `tension`
(a sustained, wordless build under the rest). **Assigning every element `emotion_carrier`, or leaving
any element's role unstated, is the near-miss this section exists to prevent** — it collapses a
five-part functional arrangement into one undifferentiated wash, the direct hybrid analogue of the
uniform-curve failure `evals/cases/performance/E1.yaml` names for an orchestral buildup. [inference]

---

## Who reads this

| Reader | What it gets |
|---|---|
| Arranger | `color_combination` entries when choosing which instruments double, blend or deliberately don't blend; `gesture` entries when writing an orchestral buildup, climax or connective passage; the orchestral half of `role_assignment` (sections 3 and 5) when the instrumentation calls for it |
| Producer | the electronic-layer half of `role_assignment` (section 5) for a hybrid brief's sound-role thinking (`producer/SKILL.md`, "Sound-role thinking"); no other section is Producer's to author |
| Performance Director | `gesture` entries as context for what an ensemble passage is trying to do, the same light cross-reference role it already has for `shared/ORCHESTRAL_VOICING_SCHEMA.md` (section 5 there); it does not own gesture construction |
| Mix Engineer | none of this directly; hierarchy implied by `role_assignment` (what should be foreground vs. support) is useful context, consistent with how it already reads Arranger's `foreground_level` |

## Sources and what to verify

- Newly read at section depth this pass, specifically for combination/colour content: Rimsky-Korsakov,
  *Principles of Orchestration* — Chapter I's resonance-comparison section, Chapter II's and Chapter
  III's group-combination sections, and five named sections of Chapter IV (`RIMSKY-1913`).
- Attempted and not reached this pass: Forsyth's Brass and Wood-Wind "Preliminary" sections
  (`FORSYTH-1914`, already `section` depth from other chapters read for `shared/VIRTUAL_INSTRUMENT_GUIDE/BRASS.md`, `shared/VIRTUAL_INSTRUMENT_GUIDE/DRUM_KIT.md` and
  `shared/VIRTUAL_INSTRUMENT_GUIDE/PERCUSSION.md`); Rimsky-Korsakov's "Transference of Passages and Phrases" (Chapter IV), which would
  most directly support the woodwind-cascade gesture. Both are named `to-verify` at their point of use
  above rather than silently assumed.
- Left at `standard-reference`, not opened: Piston, *Orchestration* (`PISTON-1955`/`PISTON-ORCH`);
  Adler, *The Study of Orchestration* (`ADLER-1989`/`ADLER-ORCH`/`ADLER-STUDYOFORCH`).
- Section 2 (register-character index) makes no independent claim and needs no source of its own; it
  points at pages that already carry theirs.
- Section 3 (percussion roles) adds no new instrument fact; every `sourced` tag there names the same
  source and read depth already recorded in `shared/VIRTUAL_INSTRUMENT_GUIDE/DRUM_KIT.md`, `shared/VIRTUAL_INSTRUMENT_GUIDE/PERCUSSION.md` or `shared/VIRTUAL_INSTRUMENT_GUIDE/MALLETS.md`.
- Section 5 (hybrid roles) is `inference` throughout, stated as such at the section's opening and not
  repeated as a per-line tag on every sentence within it, since no line in that section claims more
  than the section-level label already states.
- **Not available**: a measured, rather than late-Romantic-treatise, power-ratio table for family
  balance (the power-balance entry in section 1 names this explicitly as `to-verify`).
