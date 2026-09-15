# Harp

The concert pedal harp. A short note on the lever harp closes the file; it is not a full second
instrument card.

> Evidence: six sources read at section depth for this pass: two public-domain orchestration
> treatises with primary harp chapters (Forsyth 1914, Rimsky-Korsakov), one further treatise chapter
> on the historical single-action harp (Berlioz/Strauss, used for context, not for modern-instrument
> facts), one dedicated orchestration-research page on harp technique, one pedagogy page comparing
> lever and pedal mechanisms, and the American Harp Society's public "Getting Started" page. **This
> replaces the 2.0 page's reliance on an unnamed, excerpt-only "public orchestration academy"
> source**: the pedal mechanism, the enharmonic-unison repeated-note technique, and the glissando
> construction are now traced to primary orchestration texts read directly. Source IDs resolve in
> `research/sources/INSTRUMENT_SOURCES.md`; the claims and their limits are recorded in
> `research/instruments/HARP.md`.

Cross-family failures are in `COMMON_ERRORS.md`. The harp adds a constraint no other instrument in
this folder has, and it is the reason this file exists.

---

## Behaviour cards

### Pedal Harp

| instrument_behavior | behaviour | evidence |
|---|---|---|
| physical_sound_source | Forty-seven strings, one per diatonic degree across the range, plucked by the fingers; seven pedals, each raising or lowering every string of one letter name at once, three positions per pedal (flat, natural, sharp) | sourced: AHS-GETTINGSTARTED; FORSYTH-1914 |
| attack_behavior | A plucked attack whose loudness and colour depend on how forcefully the string is drawn and where along its length the finger contacts it; harpists pluck with the thumb held up, above the fingers, unlike a pianist's opposed thumbs | sourced: HARP-THUMB-HANDPOSITION |
| sustain_behavior | Strings ring until damped by hand or by the next chord change; in the middle and lower octaves resonance is slightly prolonged and dies away gradually rather than stopping cleanly | sourced: RIMSKY-1913 |
| release_behavior | The player's hand physically stops the string's vibration (muffling/étouffé); in quick modulation this is not always feasible, and an un-damped chord bleeding into the next produces a discordant mixture, which is why clear figuration is mostly confined to the upper register where strings are shorter and quieter | sourced: RIMSKY-1913 |
| dynamic_timbre_change | Louder plucking is the primary dynamic control; finger position along the string (nearer the tip versus more finger contact) is reported to shift brightness versus warmth independent of loudness, though this specific claim was not independently verified at section depth for harp | to-verify: a harp pedagogy source, read at section depth, confirming that finger position along the string changes brightness independent of loudness |
| register_character | The bottom octave is thick wire, slow to speak; the top is short, bright, and decays fast; the middle is the singing register and carries most idiomatic writing | inference |
| practical_range | Full compass C-flat1 to F-sharp7; only the first to fourth octave of that span is used in ordinary practice, with the extremes reserved for special effect or octave doubling | sourced: RIMSKY-1913 |
| tessitura | Most sonorous and controllable roughly in the second through fourth octave of the range; extreme registers are usable but thin (top) or slow (bottom) | inference |
| articulation_logic | Plucked (default), près de la table (close to the soundboard, dry and thin), bisbigliando (whispered tremolo, alternating fingers on one note), natural harmonics (touched at the midpoint, sounding an octave up, soft), muffling/étouffé (the only way to actively stop the ring) | inference |
| phrase_limits | Bounded by pedal setting, not breath: the practical writing unit is a passage that lives inside one pedal configuration, with changes made at the seams, in rests, or under cover of the ensemble | sourced: FORSYTH-1914 |
| transitions | No true legato; one pitch stops sounding only when damped or when its energy decays; movement between pitches is a sequence of discrete plucks, never a slur in the wind/string sense | inference |
| repeated_note_behavior | Quickly repeating one string is poor technique: each new pluck damps the string's previous vibration before it has fully spoken, giving a weak result. Rapid repeated *sounds* are instead produced by alternating between two adjacent strings tuned to the same pitch via an enharmonic-unison pedal setting | sourced: FORSYTH-1914 |
| vibrato | Not a standard technique in the string-instrument sense; expressive shading comes from dynamics, pedal timing, and damping choices rather than pitch oscillation | inference |
| pitch_instability | None in normal use once a pedal is set; a pedal change itself briefly and audibly shifts the pitch of a still-ringing string, and the mechanical action is not always silent | sourced: FORSYTH-1914 |
| resonance | Strings ring sympathetically and by design until damped; the instrument's resonance is structural to its sound rather than incidental, which is why undamped writing "accumulates" and is sometimes the intended effect and sometimes an unnoticed mistake | inference |
| physical_noise | The pedal mechanism itself produces a small, sometimes audible click or noise on change, separate from any string sound | sourced: FORSYTH-1914 |
| feasibility | Two hands, eight fingers, but the little fingers are not used in the standard hand position, so four notes maximum per hand and eight at the absolute limit; the pedal constraint is a second, independent feasibility axis unique to this instrument | sourced: FORSYTH-1914 |
| ensemble_behavior | Quiet and easily covered; functions as harmonic colour, arpeggiated texture, and attack-doubling for a line; multiple harps are used partly for volume and partly because dividing pedal-change responsibility between two players makes otherwise-unplayable passages feasible | sourced: RIMSKY-1913 |
| recording_behavior | Recorded at a distance that lets the soundboard speak; close miking emphasises finger and mechanism noise over the intended blended tone | inference |

| virtual_programming | behaviour | evidence |
|---|---|---|
| note_length | Strings ring until damped or decayed; a note held past its natural decay without a damping event does not represent real harp behaviour | inference |
| overlap | Not a legato instrument; overlap is not the relevant control the way it is for a bowed or fretted legato patch | inference |
| velocity | Level and pluck character; often selects the sample directly rather than crossfading a timbral layer | inference |
| continuous_dynamics | No sustained-note dynamic shape exists on harp the way it does on a bowed or blown instrument, because a plucked string's level is set at the attack and then only decays; per-note velocity carries the dynamic plan instead | inference |
| expression | Not a standard continuous control on this instrument in the acoustic sense; where a library exposes one it is a level trim | inference |
| articulation_switching | Keyswitches or separate patches for près de la table, bisbigliando, harmonics, and muffled/étouffé notes; each is a distinct technique, not a velocity zone of the default pluck | inference |
| round_robins | Needed; arpeggios and repeated figures expose identical repeated samples quickly, especially given how central rapid figuration is to idiomatic harp writing | inference |
| release_samples | The damping/muffling sound is a real, audible event; lost when notes are glued end to end with no explicit damping written | inference |
| pedal_or_breath_behavior | The pedal state is normally **not modelled** by a sampler at all: nothing in the patch enforces the seven-pitch-class constraint, so a written pedal conflict will simply play, silently wrong | inference |
| transition_samples | A glissando is normally either a single recorded gliss articulation at a fixed pedal setting, or a written run of individual notes at a chosen sweep rate; neither substitutes for the other, and the pedal setting behind a glissando must be decided before the notes are, since the pitches available are a direct consequence of that setting | sourced: FORSYTH-1914 |
| mic_or_room_behavior | Orchestral libraries typically place the harp already reverberant, at hall distance, rather than close and dry | inference |
| likely_fake_sounding_errors | Two spellings of one letter name sounding "at once" (physically impossible); a chromatic glissando; pedal changes faster than two feet can manage; more than four notes in one hand or eight total; a written glissando with no pedal setting decided, so the sampled pitches are simply whatever the patch happened to record | inference |
| organic_programming_methods | Write the pedal diagram before the notes, one setting per passage, and check every note against it; build repeated notes as alternation between an enharmonic-unison string pair rather than one string re-triggered rapidly; build glissandi from a declared pedal setting and accept the pitches it yields; let the thumb, held above the fingers, take the top note of a hand's figure by default, adjusting loudness of that note as a deliberate voicing choice rather than an automatic law | sourced: FORSYTH-1914; HARP-THUMB-HANDPOSITION |

---

## What the instrument is

Forty-seven strings, one per diatonic degree across the range, plucked by the fingers, with seven
pedals that raise or lower every string of one letter name at once
[sourced: AHS-GETTINGSTARTED; FORSYTH-1914]. That is the whole instrument in one sentence, and
everything below follows from it [inference].

## The pedal constraint

This is the most important section in the file [inference].

```text
seven pedals            one per letter name: B C D on the left foot, E F G A on the right foot
three positions each    flat (up), natural (middle), sharp (down)
7 x 3 = 21 pitches      available from seven string classes
```
[sourced: FORSYTH-1914]

**Only seven pitch classes sound at any moment.** Not seven notes, seven pitch **classes**. If the D
pedal is natural, every D on the instrument is a D natural, everywhere, until the foot moves. A
passage that needs both D flat and D natural simultaneously is impossible, and one that needs them
successively requires a pedal change between them [sourced: FORSYTH-1914].

The pedals are divided between two feet, confirmed directly against a primary orchestration source:
Forsyth describes "the B-, C-, and D-pedals" on the left and "the E-, F-, G-, and A-pedals" on the
right, radiating outward from the player [sourced: FORSYTH-1914]. So two pedals can change at once
only if they are on different feet; three changes need two moves [inference].

**A pedal change takes time and is slightly audible.** In Forsyth's own words, depressing a pedal
"requires a small but appreciable fraction of time, and is not always free from noise"
[sourced: FORSYTH-1914]. No source opened for this pass gives a measured millisecond figure; this
pack keeps the description qualitative rather than inventing one
[to-verify: a harp manufacturer source with a measured pedal-change time]. Changes are made in
rests, on strong beats where the harp is not sounding, or deliberately under cover of the orchestra
[inference].

## Range and register

Full compass C-flat1 to F-sharp7 [sourced: RIMSKY-1913]. Only the notes from the first to the fourth
octave of that span are used in ordinary practice; the extreme notes at either end are reserved for
special circumstances and octave doubling [sourced: RIMSKY-1913]. **This corrects the 2.0 page's
`C1-G7` figure**, attributed there to an unopened Adler citation; the figure above is instead read
directly from Rimsky-Korsakov's own orchestration text [sourced: RIMSKY-1913]. The bottom octave is
thick wire and slow to speak; the top is short, bright and decays fast; the middle is the singing
register [inference].

## Repeated notes and enharmonic-string technique

Quickly repeating one string is poor technique on this instrument: each new pluck damps the string's
still-ringing previous vibration before it has fully spoken, and a string needs to be plucked a fair
distance out of true to produce a good tone, so a rapid re-pluck of the same string is unsatisfactory
[sourced: FORSYTH-1914]. Composers and players instead achieve rapid repeated *sounds* by alternating
between two adjacent strings tuned, via an enharmonic-unison pedal setting, to the same pitch (for
example, one string left as C-sharp while the adjacent string is raised from D-flat to the same
pitch); this is the mechanism behind figures that look, on paper, like a single repeated note but are
actually played on two strings [sourced: FORSYTH-1914].

Nine such enharmonic-unison pairs are available (not twelve, because three of the twelve chromatic
notes cannot be reached by the double-action mechanism at all): B-sharp/C-flat, C-sharp/D-flat,
D-sharp/E-flat, E-flat/F-flat, E-sharp/F-natural, F-sharp/G-flat, G-sharp/A-flat, A-sharp/B-flat, and
B-natural/C-flat [sourced: FORSYTH-1914]. The same mechanism, applied across a full octave, is how
glissando chords other than a plain diatonic scale are built (see below) [inference].

## Glissandi are designed, not requested

A harp glissando is the player sweeping across all the strings. The pitches that result are
**whatever the pedals are set to**, so a glissando is a compositional object built by choosing a
pedal setting first, not a notational request the instrument fulfils on demand
[sourced: FORSYTH-1914; RIMSKY-1913].

Because there are seven string classes and (with enharmonic doubling) up to nine reachable unison
pairs, a pedal setting can eliminate some pitches from a straight diatonic sweep and leave a smaller,
repeating set behind. Common sonorities built this way include dominant sevenths, diminished
sevenths, and the upper portions of major ninths and elevenths [sourced: FORSYTH-1914]. Every such
chord-glissando still touches all seven string classes; the enharmonic pairs simply mean some classes
sound the same pitch as their neighbour, which is what produces the chord rather than a scale
[inference].

**A chromatic glissando does not exist.** There are seven strings per octave, and no pedal setting
raises a string by more than a whole tone total (the "double action"), so the instrument cannot sweep
twelve pitches [sourced: FORSYTH-1914]. Writing a glissando therefore means writing the pedal
diagram, not the note heads [inference].

## The pedal harp's diatonic character

With all pedals in one setting, the harp produces a diatonic scale (or, via enharmonic doubling, some
other fixed seven-note collection); a full chromatic scale requires setting and resetting several
pedals within a single octave and is impractical at any but a slow tempo
[sourced: RIMSKY-1913; FORSYTH-1914]. Rimsky-Korsakov states plainly that the harp "does
not lend itself to rapid modulation," and that the usual remedy in orchestral writing is to use two
harps alternately when the harmony moves faster than one instrument's feet can follow
[sourced: RIMSKY-1913]. The older single-action harp Berlioz describes was considerably more
restricted still — playable cleanly in only eight keys — but that description predates the modern
double-action mechanism becoming standard, and is kept here as historical context for *why* the
instrument earned its "anti-chromatic" reputation, not as a constraint on the modern instrument
[sourced: BERLIOZ-1855].

## Articulation and note transitions

```text
plucked (default)     the normal tone; strings ring until damped
près de la table      plucked close to the soundboard; dry, thin, guitar-like
bisbigliando          a whispered tremolo, the same note taken with alternating fingers, very quiet
harmonics              a string touched at its midpoint and plucked; sounds an octave above, soft
muffling / étouffé    the hand laid on the strings to stop them; the only way to stop the ring
```
[inference]

There is no legato in the string- or wind-instrument sense: one pitch stops only by damping or decay,
and moving to the next pitch is a fresh, discrete pluck [inference]. Dynamics are set primarily by
how forcefully the string is drawn; finger position along the string is also reported to shift
brightness versus warmth, though this specific claim was not confirmed at section depth for harp in
this pass [to-verify: a harp pedagogy source, read at section depth, on finger-position-to-tone].

## Physical constraints

```text
two hands, eight usable fingers. Harpists pluck with the thumb held UP, above the fingers -
    unlike a pianist's opposed thumbs - and the little fingers are NOT used.
four notes maximum per hand, so eight simultaneous notes at the absolute limit
one string per finger, and adjacent strings need adjacent fingers
two feet, on seven pedals split three (left: B C D) and four (right: E F G A)
```
[sourced: HARP-THUMB-HANDPOSITION; FORSYTH-1914]

Because the thumb sits above the fingers rather than opposing them, the span from thumb to index
finger is the largest interval a hand comfortably reaches, and **the thumb naturally takes the
highest, not the lowest, note of a hand's chord or arpeggio group** [sourced: HARP-THUMB-HANDPOSITION].
**This corrects the 2.0 page's claim that "the thumb is stronger, so the lowest note of a hand's
group is usually the loudest."** The thumb is not positioned to play the lowest note at all; it plays
the top note [sourced: HARP-THUMB-HANDPOSITION]. Whether that top note is also the loudest is a
separate, genuinely dynamic decision the player makes, not an automatic consequence of the thumb
being "stronger" [inference].

Eight notes at once is a theoretical maximum, not a normal texture; five or six is already a large
chord [inference]. **Strings ring unless muffled.** A harp part with no damping indications is a part
where everything accumulates, which is sometimes the intended sound and sometimes a mistake nobody
noticed [inference].

## Phrase behaviour

Phrases are bounded by pedal settings, not by breath. The practical unit of harp writing is a passage
that lives inside one pedal configuration, with changes made at the seams — in rests, on strong beats
where the harp is not sounding, or under cover of the orchestra [sourced: FORSYTH-1914]. A part that
modulates every bar is a part that is changing pedals every bar, and the player has two feet
[inference].

## Ensemble behaviour

The harp is quiet and easily covered. In the orchestra it functions almost entirely as a harmonic or
accompanying instrument: chords, and the florid figures springing from them [sourced: RIMSKY-1913].
It works as colour, as arpeggiated texture, and as doubling of a line's attack [inference]. Two or
more harps are written where the harmonic pace exceeds what one player's pedal changes can manage — a
real, traditional division of labour, not only a matter of volume [sourced: RIMSKY-1913].

## Recording behaviour

Recorded at a distance that lets the soundboard speak; close-miking emphasises finger noise, string
buzz, and the pedal mechanism's own small mechanical noise [inference]. Orchestral libraries
typically place the harp already reverberant, at hall distance [inference].

## Programming it: the control model

Product specifics belong in the calibration profile [inference].

```yaml
velocity: level and pluck character; often selects the sample directly
polyphony: high, and the patch will happily play what the instrument cannot
pedal_state: NOT modelled in most libraries. The writer is the pedal check.
glissando: either a recorded gliss articulation at a fixed setting, or written notes at a chosen sweep rate
round_robins: needed; arpeggios expose repeated identical samples quickly
release_samples: the damping sound; lost when notes are glued end to end
harmonics: a separate recording, sounding an octave above the written string
```
[inference]

The line that matters: **the sampler does not enforce the pedal constraint, so nothing will stop an
impossible part except the feasibility check** [inference].

## Programming it: what makes it sound real

- Write the pedal diagram before the notes, one per passage, and check every note against it.
  [inference]
- Build glissandi from a stated pedal setting, and accept the pitches it gives.
  [sourced: FORSYTH-1914]
- Build rapid repeated *sounds* as alternation between an enharmonic-unison string pair rather than
  one string re-triggered rapidly, matching how the technique actually works.
  [sourced: FORSYTH-1914]
- Keep chords inside eight notes and four per hand, and let the thumb, held above the fingers, take
  the top note of the figure by default. [sourced: HARP-THUMB-HANDPOSITION]
- Let strings ring, and write the muffling where the ring should stop. [inference]
- Vary velocity deliberately across an arpeggio as a chosen voicing decision, not by assuming the
  thumb is automatically loudest, correcting the 2.0 page. [inference]
- Use harmonics sparingly and quietly, and remember they sound an octave up. [inference]

## What sounds fake here

The general list is in `COMMON_ERRORS.md`. Harp-specific tells:

- two spellings of one letter name sounding at once, which is physically impossible; [sourced: FORSYTH-1914]
- chromatic glissandi; [sourced: FORSYTH-1914]
- pedal changes at a rate two feet cannot manage; [inference]
- nine or ten note chords, or five notes in one hand, which is error 6; [sourced: FORSYTH-1914]
- arpeggios at one velocity, or with the bottom note assumed loudest because "the thumb is strong,"
  which mis-locates where the thumb actually sits in the hand; [sourced: HARP-THUMB-HANDPOSITION]
- a rapid repeated note played as one string re-triggered instead of two enharmonic-unison strings
  alternating, which reads as thin and technically wrong to anyone who knows the instrument;
  [sourced: FORSYTH-1914]
- everything damped instantly by short note lengths, which is error 12, or nothing ever damped;
  [inference]
- a written glissando with no pedal setting behind it, so the sampled pitches are whatever the patch
  happened to record. [sourced: FORSYTH-1914]

## What the Performance Director needs from this file

- A **pedal feasibility pass** is the harp's version of the four-limb rule. Track the seven pedal
  states across the part, flag any simultaneous conflict, and flag any change rate exceeding two
  feet.
- `impossible_voicings`: more than four notes per hand, more than eight total, or two pitch classes
  on one letter name sounding together.
- `out_of_range`: against C-flat1 to F-sharp7, with the first-to-fourth-octave band flagged as the
  practical working range and anything outside it flagged as a special-effect exception, not a
  default.
- `articulation_unavailable`: harmonics, près de la table, and bisbigliando are separate recordings.
- Damping is a written decision here, so `note_length_variation` carries real musical meaning.
- Repeated-note figures should be checked against the enharmonic-unison pair mechanism, not assumed
  playable as a single re-triggered string.

## Sources and what to verify

Full citations are in `research/sources/INSTRUMENT_SOURCES.md`; claim-level detail and limitations
are in `research/instruments/HARP.md`.

- **Available and used**: pedal mechanism, pedal-foot assignment, pedal-change timing/noise,
  enharmonic-unison repeated-note technique, and glissando construction, all read directly from two
  primary orchestration treatises (FORSYTH-1914, RIMSKY-1913); full range and ensemble role
  (RIMSKY-1913); thumb position and its consequence for which note in a hand's group is highest
  (HARP-THUMB-HANDPOSITION); string count and the pedal/lever distinction (AHS-GETTINGSTARTED);
  lever-harp mechanism and its mid-phrase-change limitation (LEVERHARP-PEDAL-PEDAGOGY).
- **To verify**: the finger-position-to-tone claim (fleshy pluck warmer, tip pluck brighter/louder)
  was found only via a search summary, not opened at section depth for harp specifically, and is kept
  to-verify rather than sourced.
- **To verify**: Salzedo and Lawrence's *Method for the Harp* was not opened directly; hand-position
  claims are corroborated instead through HARP-THUMB-HANDPOSITION and general search consensus.
  Opening the Salzedo method directly would strengthen the thumb-position claim further.
- **Not available**: a measured pedal-change time in milliseconds. Forsyth's "small but appreciable
  fraction of time" is the strongest available statement; treat any specific number as invented.

## A short note on the lever harp

A lever (folk/Celtic) harp typically carries 24 to 36 strings, fewer than a concert grand pedal
harp's forty-seven, and replaces the seven foot pedals with one hand-operated lever per string
[sourced: LEVERHARP-PEDAL-PEDAGOGY; AHS-GETTINGSTARTED]. Each lever raises its single
string by one half step; there is no double-action equivalent, so a lever harp cannot reach flat,
natural and sharp on one string the way a pedal does — only two of those three positions on any given
string at a time [sourced: LEVERHARP-PEDAL-PEDAGOGY].

Because levers are hand-operated, changing one takes a free hand and a beat or two of time, unlike a
pedal harp, where both hands stay on the strings while the feet work [sourced: LEVERHARP-PEDAL-PEDAGOGY].
This is the practical reason pedal-harp repertoire with frequent mid-phrase accidentals is generally
not playable on a lever harp without rewriting, while music written with the lever harp's constraints
in mind (much Celtic and folk repertoire) is [sourced: LEVERHARP-PEDAL-PEDAGOGY]. Treat a lever harp
as a distinct instrument for feasibility purposes, not a budget pedal harp: its pedal-feasibility pass
above does not apply, and a lever-change feasibility check (a free hand, and enough time) should be
used instead where a part specifically calls for a lever harp [inference].
