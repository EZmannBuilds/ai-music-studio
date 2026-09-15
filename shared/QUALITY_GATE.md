# Shared Music Quality Gate

Before finalizing substantial musical work, check the relevant dimensions.

## Identity
Does this track have a recognizable musical identity, or could the material belong to hundreds
of unrelated tracks?

## Motif
Is there something memorable that can recur, transform, or be recognized?

## Tension and release
Does the track create expectation and alter it through harmony, rhythm, timbre, arrangement,
or silence?

## Contrast
Do sections differ in function, not merely in loudness or layer count?

## Development
Does repeated material evolve?

## Groove
Do rhythmic layers cooperate intentionally?

## Register
Are important parts fighting for the same pitch region?

## Frequency role
Are low, low-mid, mid, presence, and air roles intentional?

## Space
Does width/depth serve hierarchy rather than make everything large?

## Originality
Is the track's distinctiveness structural, musical, timbral, or performative rather than merely
a strange preset?

## Reference distance
If references were used, were principles transferred without cloning identifiable musical
content?

## Restraint
Did the system add elements because they improve the music, or because empty space made it
nervous?

## Render reality
If audio analysis is available, does the rendered result match the intended design?


## Expectation
Does the track establish patterns clearly enough for deviations to matter?

## Predictive complexity
Is the material too obvious, too unstable, or intentionally positioned at an extreme?

## Hook memory
Can at least one important musical object be recognized after the sound design is stripped back?

## Pulse clarity
Does syncopation create movement without destroying pulse clarity? Where the music uses a cycle, a
non-isochronous metre or layered metres, is the reference layer audible
(`shared/RHYTHM_SYSTEMS/`)?

## Auditory scene
Are important elements perceptually separable? Are intended layers allowed to fuse?

## Cultural assumptions
Are emotion/theory judgments calibrated to the target musical context rather than treated as universal?

## Human preference
Would a blind listener choose this version over the simpler baseline?


## User-neutrality
Did any recommendation come from a previous user's style rather than the current brief?

## Tool-neutrality
Could the musical plan still work if the user used another DAW, synth, or analyzer?

## Goal alignment
Is the track being judged against its actual use case rather than a fixed preferred aesthetic?

## Taste vs defect
Are subjective preferences clearly separated from technical or musical problems?


## Lyric prosody
If lyrics are sung, do syllable counts, lexical stress, phrasing, breaths, and vowel/consonant
choices cooperate with the melody?

## Melody ↔ lyric alignment
If an exact vocal MIDI exists:
- are all syllables mapped;
- are melismas intentional;
- are phrase boundaries compatible with rests;
- are uncertain pronunciations surfaced?

## DAW execution
Did the adapter:
- use native DAW concepts;
- read state before writing;
- preserve/backup existing work;
- verify routing and timing after mutation;
- avoid destructive operations that were not approved?


# Instruments, verification and variety

## Instrument coverage
Was the plugin audit run before production? Does every score part have an instrument that
exists in the installed edition, with every substitution named in its track?

## Calibration consent
Was calibration offered when `plugin-auditor/SKILL.md` required it, and run only after the user
said yes?

## Every note sounds
Did Render Verification run on this pass, with stems? Is every silent note fixed or explicitly
accepted by the user, with the date, time and the user's words recorded?

## Every part is heard
Is every foreground part free of `too_quiet_for_role` and `masked` flags, or accepted by the user?
Were the stems analyzed as well as the mix?

## Melody variety
Did every lead and vocal-guide line pass Composer's melody-variety gate, including the
cross-song comparison, or carry a recorded reason for the exception?
Was "exact fit" reported as a mapping check rather than as a pass?

## Lyric uniqueness
If lyrics were written, was the earlier lyric corpus checked, and is a uniqueness report attached?

## Deliverable
Does the export match the deliverable mode? In an instrumental export, is every vocal-line and
vocal-guide track muted, silent in the mix, and is the file named "Instrumental"?

## Honest status
Is the pass described as "measured, not listened to" until someone has listened to it?


# Performance, voice, diversity and project

## Performance intent
Was a performance plan written, and did MIDI Builder execute it rather than inventing expression
(`shared/HUMAN_PERFORMANCE_SCHEMA.md`)? An artifact with no plan is labelled `unperformed`, which is
honest; an artifact full of invented expression is not.

## Organic, not random
Does every timing and dynamic deviation name a model and a magnitude? Is there anything in the plan
that amounts to a percentage of randomness?

## Deliberate exactness
If the part is grid-exact, is that recorded as the realism target rather than left looking like an
omission?

## Physical feasibility
Was a feasibility report produced? Is every impossible voicing, limb conflict, out-of-range note and
breath overrun either fixed or recorded as intentional?

## Vocal architecture
Does every vocal layer have a function? Does register change across the song, or does the lead sit in
one place? Is silence used, or merely absent? Is the plan inside the singer's declared range?

## No identity imitation
Does any part of the plan aim at reproducing a specific living artist's voice or signature sound,
rather than a transferable mechanism?

## Musical system named
Where the music uses a system other than the default, is it named, and does the work carry that
system's cautions rather than borrowing its surface?

## Tuning reaches the instrument
If the pitch system is not twelve-tone equal temperament, was the instrument's capability checked, was
a mechanism chosen, and does the export state what happens if a receiver ignores it? Was anything
silently quantised?

## Diversity consulted
Was the ledger read before this track, and is every shared dimension classified as accidental
repetition, project motif, genre convention or deliberate callback rather than left unexamined
(`shared/TRACK_DIVERSITY_LEDGER.md`)?

## Project consistency
Where a project exists, does this track serve a function no other track already serves, or is the
doubling deliberate?

## Interaction mode respected
Was the mode the user asked for actually followed? A diagnosis request answered with a rewrite is a
failure even if the rewrite is good.

## Explanation calibrated
Was a beginner buried in terminology? Was an expert given a worked example they did not ask for?
