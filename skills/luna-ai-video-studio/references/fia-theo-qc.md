# Fia & Theo QC, Repair, and Evaluation

Apply with `evaluation-protocol.md` before final delivery. Evaluate a written prompt, visible images and an actual video as different evidence types. A passing static test validates rule presence and fixture integrity, not model behavior or viewer retention.

## Evidence labels

For each relevant item use PASS, REVISE, UNVERIFIED, or N/A, with the smallest available supporting asset/time range. A hidden paw is UNVERIFIED. Unheard audio is UNVERIFIED. A single still does not prove correct gait, collision timing, or a seamless camera move. Do not substitute pixel similarity or an invented percentage for semantic identity checks.

Prompt QC can verify that an instruction is coherent without claiming the output performed it. For important unresolved inputs or capability constraints, withhold a generation-ready label and state the exact blocker. In generated-output review, a critical failure overrides a flattering average score. Do not claim a view-count probability from a prompt or one clip.

## Mandatory series checks

1. Identity: correct Fia/Theo assignment, fur and eyes, tail attachment, Theo's anatomical right-front white sock only, and distinct owned accessories. Track the real anatomical limb through turns and occlusion. Never approve a screen-corner rule as a body marking.
2. Input reality: actual selected inputs and exact tags, identity versus pose versus background roles, no phantom old video, no assumed six-frame requirement, no start-image/hook mismatch. Approved pictures remain proposed generator inputs until that mapping is known.
3. Image readiness: one legible action/preparation, source state matches the requested motion, usable contact/landing space, room landmarks and scale consistent. Check hidden evidence honestly and revise only authorized assets.
4. Acting and contact: feline posture and locomotion, trigger precedes reaction, one actor plus responder for difficult contact, connected limbs/tails/tongues, no merging muzzles or puppet-like limbs. An intentional jump or slip is valid when its cause and recovery are readable.
5. Duo and props: roster, entry/exit windows, who sees what, initiator/target, fish/key owner, grip/release/trajectory, no identity swap after overlap, no returning departed rival without approval.
6. Camera and timing: coherent subject/camera paths, motivated turns, legible contact, stable camera when required, enough time for response and payoff. Reject a pillar used to hide impossible travel. Keep magic sources in world space as the view changes.
7. Hook and ending: a visible event in the first second under the active viral brief, framing compatible with the input, a causal reveal/payoff that fits the duration. Do not add a new baby, rival or magic explanation to repair a weak ending without approval.
8. Audio: named feline sound source, no accidental human voice, grip-compatible mouth action, contact-aligned Foley, music matches the event and honors any no-music instruction. Audio not actually inspected remains unverified.
9. Delivery: requested stage only, current approved references, one compact prompt, measured user/provider text limit, no automatic language switch, no unsupported model controls, no claims of a successful generation before one exists.

## Visual readability acceptance

Apply the seven checks in `visual-storytelling.md` to the requested evidence level. Check who can see the trigger, approach/block access, relevant prop state and visible change after the action. Perform a caption-hidden pass; preserve requested captions in delivery. For each failure identify the missing visible evidence and smallest repair. Deliberately withheld motives can remain unresolved. A written instruction or still image cannot establish successful event timing; mark that output behavior UNVERIFIED.

## Targeted repair order

First identify the actual critical fault. Default triage is identity and anatomical markings -> broken anatomy or prop ownership -> motion/contact -> route/camera -> emotional cause and payoff -> sound and pacing. A specific user-approved sound-only repair stays sound-only when visuals are accepted.

Freeze successful parts. Fix the smallest responsible input or instruction, then recheck dependent visuals, audio timing and end state. For repeated failures, reduce simultaneous acts and camera movement before adding more negatives. For a bad asymmetrical reference, propose an authorized correction rather than trying to override it with more text. Never regenerate media during review or an edit-only request.

## Edit-only, upscale, and export

Inspect the actual source before selecting changes. Preserve opening recognition time, feline reaction, contact and final reveal. Speed changes need a source-to-output time map and aligned audio, not arbitrary cuts of the same preset intervals in every episode. Check joins for stutter, repeated frames, lost transients and clipped sound tails. Do not assert that a speed ramp improves retention without output evidence.

Preserve the original and create a separate output only when authorized. Keep actual aspect ratio, dimensions and frame cadence explicit. Distinguish AI detail restoration from Lanczos/bicubic resizing and sharpening. Do not report an ordinary resize as an AI restoration job. Confirm the requested provider/tool actually ran and never claim completion from a queued job alone.

When retiming a mixed music/Foley track, inspect pitch, rhythm and sync. Prefer small justified adjustments; do not claim source separation happened unless it did. Use accessible audio analysis for loudness and peaks, but listen or use an appropriate audio-inspection tool before judging whether vocals are human-like. Recheck encoded output; a target setting does not prove the final measurement.

Before delivery verify existence of the exact file/link, playable video and audio, dimensions, duration and timing. Label partial inspection. Do not imply that upgrading GitHub automatically refreshes every installed copy; a consumer must load the updated files.

## Behavior fixtures and video trials

`../tests/fia-theo-behavior-cases.json` contains test requests and grading criteria, not recorded successful runs. `../tests/test_fia_theo.py` checks repository integrity and fixture coverage only. For a behavior test, feed each request to the agent without its criteria, store the actual response with case ID and skill revision, and grade it independently. Do not count an authored expected answer as a model test.

For approved video comparisons use the same model/version, actual reference set, duration, ratio, resolution and comparable attempt count. Prioritize four trials: Theo turning front-to-back, one grooming contact, cats crossing without identity exchange, and fish release/slip/recovery with feline audio. Record unobserved anatomy and audio separately. No paid generation or installation is authorized by the test definitions.

## Integration provenance

These are original user-specific rules informed by the prior comparison of character-consistency, pixar-storyteller, MiniMax animation workflow, sprite-pet and storyboard approaches. No third-party executable code is installed or copied here. Do not inherit those tools' fixed grids, pixel-similarity thresholds, provider limits, API requirements, film-style mandates or upload behaviors. Provider features require their own current verification.
