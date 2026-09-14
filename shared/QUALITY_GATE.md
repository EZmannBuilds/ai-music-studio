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

## Groove
Does syncopation create movement without destroying pulse clarity?

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
