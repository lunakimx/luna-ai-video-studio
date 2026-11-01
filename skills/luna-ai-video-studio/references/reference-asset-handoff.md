# Reference Asset and Connected-Clip Handoff

This workflow supplements Luna AI Video Studio's existing reference, continuity, visual-storytelling, model-adaptation, and production-ledger rules. Preserve all established first-second hook and one-take gates.

## When to apply

Use for a character-sheet-plus-scene workflow, multiple image references, an accepted scene still, localized character/wardrobe correction, multi-clip work, or extension of an existing generated video. Do not impose extra assets on simpler shots.

## Asset role declaration

Before producing a model-ready prompt, map each actually attached input to one role:
- ID: authoritative source of a specific character's face/body/markings and approved wardrobe.
- SCENE: accepted environment, staging, camera side, lighting, props, obstacle geometry.
- START FRAME: actual first visible frame if the selected workflow uses first-frame conditioning.
- END FRAME: actual last visible frame if last-frame conditioning is supported.
- PRIOR VIDEO: actual existing clip to extend or use as video-to-video reference, only where supported.
- AUDIO: supplied sound/music/voice with approved timing and usage.

The final tags must match the actual generation interface, connection order, and asset types. `@img1`, `@img2`, and `@video1` are **illustrative placeholders only** until confirmed by the selected tool. Never invent missing tags or pretend an earlier conversation file has been uploaded to a new workflow.

For a public two-image prompt, retain IMAGE 1 = ID and IMAGE 2 = SCENE unless the user assigns another mapping. A character sheet is not automatically a story frame. Keep identity, background, and camera responsibilities separate; no face blending across references.

## Character sheet and environment preparation

If a sheet improves stability, prefer a sharp large facial close-up alongside the front and rear/side body information relevant to the shot. The original authoritative ID image still wins on identity.

For movement through tight spaces or complex action, consider first constructing a stable, people-free clean plate with fixed obstacles, floor geometry, entry/exit routes, collision zone, and scale landmarks. Then prepare one motion-ready composite frame with the actors in a feasible start state. Avoid adding images that do not improve the actual video conditioning.

Preserve the approved scene plate's immovable geometry when inserting or correcting people. For a one-shot edit, change only the requested region and preserve unrelated approved details.

## Connected-video selection

1. Inspect the previous accepted clip's real final visible and audible state: identities, hands, props, marks, damage/wetness, gaze, camera side, moving direction, light, music/ambience, and motion phase.
2. If the selected product supports **prior-video conditioning or direct extension**, attach the accepted real video plus any supported character reference. Use verified controls and explicitly continue from the existing ending rather than replaying the setup.
3. Otherwise, if supported, use its actual clean final frame as the next clip's start frame. Reject warped, blurred, transitional, or duplicated handoff frames; use the nearest clean accepted frame or a repaired still.
4. If neither mode is supported, write explicit text-only handoff details and disclose that continuity is less controlled. Do not claim actual prior-video continuity when only text is available.
5. Preserve screen travel, subject pace, camera movement, environmental motion, and audio phase across the seam. Avoid resetting actors to a neutral pose or duplicating the last moment.
6. Inspect the stitched seam for repeated frames, jump cuts, mismatched resolution/aspect ratio, audible glitches, and interrupted audio tails before accepting the connected sequence.

No generic fixed-length recipe (for example, 8+15+25+4 seconds) should override the user's requested duration, first-second hook, pacing, or a model's verified limits. A one-take remains a one-take when explicitly requested.

## Explicit speaker and reaction mapping

For multi-person dialogue, attach the dialogue line to the correct character and available ID reference. Identify speaker, timing, gaze target, mouth motion, listener reaction, prop ownership, and camera position. Do not assume an arbitrary tag will automatically resolve the right voice or face. Keep lines short enough to fit the generated duration.

## Face-obscuration experiment

Do not introduce crosshatching or scribbles on face references by default. Only test with the user's explicit approval, compare clean and marked sheets under matched settings, and inspect generated clips for transferred marks or identity changes.

## Pre-generation mini-check

- Are all named inputs attached and are tags real?
- Is the authoritative character identity separate from scene/style?
- Is the clean plate actually needed and geometry stable?
- Is the opening image viable for the intended first action and hook?
- Is the previous clip or usable handoff frame truly available?
- Does the selected model actually support the chosen conditioning/extension mode?
- Does the prompt preserve the accepted last state, audio, travel and camera direction?
- Have we preserved approved elements rather than asking for a full regeneration?
- Did we keep existing one-take, causal story, motion physics, prompt lint and scene QC?

If any answer fails, simplify or use a supported fallback before delivering the final prompt.
