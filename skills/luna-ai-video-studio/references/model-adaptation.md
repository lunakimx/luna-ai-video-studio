# Model Adaptation

Video-model behavior changes quickly. Treat model-specific knowledge as time-sensitive.

When the user names a model, adapt the prompt only to capabilities you can reasonably verify or know with confidence. If current documentation or browsing tools are available and the feature matters to execution, verify it before relying on it.

## Capability verification gate

When the user names a specific model or version and the requested execution depends on a model-specific feature, verify that feature against current official documentation when browsing or documentation access is available.

Prefer official model documentation, release notes, model cards, or first-party product pages over remembered capability information, third-party summaries, or outdated examples.

Treat remembered model specs as provisional when the capability may have changed.

If live verification is unavailable:

- do not present uncertain capabilities as fact;
- do not invent version-specific controls or limits;
- do not assume that a feature from an older or newer model version exists in the named version;
- use the model-neutral fallback when possible;
- phrase uncertain recommendations as optional rather than guaranteed.

Verification should focus on capabilities that materially change execution. Do not browse merely to confirm details that do not affect the prompt or workflow.

## Capability questions

Check whether the selected workflow supports:

- text-to-video
- image-to-video
- one or multiple image references
- character-reference conditioning
- first-frame control
- last-frame control
- native audio
- generated speech
- lip sync
- camera controls
- motion controls
- multi-shot generation
- video extension
- video-to-video
- negative prompting
- duration options
- aspect-ratio options
- resolution options
- frame-rate or timebase options when stitching or motion continuity depends on them

Never invent support for a feature.

## Connected-shot frame handoff

When creating a directly connected next clip and the selected model supports first-frame conditioning or an equivalent start-frame image input, prefer using the accepted previous clip's actual final frame as the next clip's first-frame reference.

This should take priority over text-only continuity instructions when the frame is clean and usable.

Use the carried frame to preserve continuity-critical visible state such as identity, hair, wardrobe, accessories, props, hand state, pose, camera side, framing, screen direction, damage, wetness, lighting, important object placement, creature state, and environment state.

Do not blindly carry a bad transient frame. If the actual final frame contains blur, deformation, occlusion, motion smear, muzzle flash, exposure spikes, or another unwanted artifact, use the nearest clean accepted frame or a corrected continuity reference instead.

If first-frame conditioning is unavailable, use the strongest supported reference method and explicit handoff wording. Never claim frame conditioning is active when the selected model or workflow does not support it.

## Resolution alignment and exceptions

Resolution handling must follow the selected model's verified supported workflow rather than a universal 1080p rule.

For directly connected clips:

- prefer the same delivered pixel dimensions across adjacent clips when continuity matters;
- keep the accepted handoff frame at the same aspect ratio, framing, crop, and pixel dimensions whenever the selected model accepts it;
- avoid unnecessary resizing, padding, or recropping between the previous final frame and the next first-frame reference;
- if the model internally normalizes reference images, treat that behavior as part of the model workflow and do not promise pixel-identical handoff.

For workflows described as 1080p, first check the model's official or verified native input/output dimensions.

Never request 1920×1088 merely because the user asks for 1080p. Use 1920×1088 only when the selected model or pipeline explicitly supports or produces that aligned coded size, the intended framing remains correct, and there is a demonstrated workflow reason to preserve it.

Do not force 1920×1088 when:

- the selected model officially expects or outputs native 1920×1080;
- the platform, API, editor, or delivery target requires 1920×1080;
- 1088-height media would be automatically cropped, stretched, letterboxed, or otherwise mishandled;
- first-frame or last-frame conditioning is internally resized in a way that removes the practical benefit;
- changing dimensions would break a previously accepted connected-shot workflow;
- current documentation or observed workflow behavior does not establish a reason to use 1920×1088.

For 720p workflows, 1280×720 already satisfies 16-pixel alignment and should normally remain unchanged unless the selected model documents another native size.

When capability or behavior is uncertain, prefer the model's documented native resolution and keep the connected-shot workflow consistent rather than forcing 1920×1088.

## Frame rate and timebase

When several generated clips will be stitched into one continuous sequence, preserve the same delivered frame rate or timebase across adjacent clips whenever the workflow exposes or controls it.

Do not invent a frame-rate control when the model does not expose one.

If generated clips arrive with different frame rates, treat normalization as an editing or delivery concern and avoid claiming seamless frame-level handoff until the clips have been conformed and inspected.

A matching resolution does not guarantee a smooth transition when frame cadence differs.

## Resolution decision order

When continuity and delivery stability matter, decide in this order:

1. verify the selected model's supported and native resolution behavior;
2. preserve the accepted connected-shot resolution and framing when possible;
3. verify first-frame or last-frame conditioning behavior when it is being used;
4. preserve compatible frame rate or timebase when the workflow exposes it;
5. consider 16-pixel alignment only when it provides a verified practical benefit;
6. preserve final platform, editor, or delivery requirements.

Use the most stable supported option. Do not convert a model-specific optimization into a global rule.

## Prompt adaptation

Adjust these variables to the model:

- total prompt length
- sentence density
- amount of temporal sequencing
- camera terminology
- number of simultaneous actions
- reference wording
- negative instruction style
- dialogue length
- sound direction
- degree of physical detail

Prefer execution clarity over adjective stacking.

If a model is known to struggle with many concurrent actions, reduce the action count rather than restating the same instruction more forcefully.

If negative prompts are weakly supported, express critical constraints positively. Example: instead of only saying “no extra people,” state “exactly one woman remains visible for the entire shot.”

If audio is not natively generated, keep the visual prompt clean and provide a separate audio note only when the user needs it.

If exact typography is unreliable, move text work to post-production.

## Model-neutral fallback

When current capability is uncertain, write a robust visual prompt that does not depend on special controls:

1. establish subject and reference lock;
2. describe one dominant action;
3. describe the supporting event;
4. define the camera physically;
5. define visible performance;
6. define environmental response;
7. protect the ending state;
8. add concise constraints.

The goal is generation success, not displaying knowledge of every model feature.
