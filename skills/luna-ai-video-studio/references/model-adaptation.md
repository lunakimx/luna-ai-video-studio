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

Never invent support for a feature.

## Connected-shot frame handoff

When creating a directly connected next clip and the selected model supports first-frame conditioning or an equivalent start-frame image input, prefer using the accepted previous clip's actual final frame as the next clip's first-frame reference.

This should take priority over text-only continuity instructions when the frame is clean and usable.

Use the carried frame to preserve continuity-critical visible state such as identity, hair, wardrobe, accessories, props, hand state, pose, camera side, framing, screen direction, damage, wetness, lighting, important object placement, creature state, and environment state.

Do not blindly carry a bad transient frame. If the actual final frame contains blur, deformation, occlusion, motion smear, muzzle flash, exposure spikes, or another unwanted artifact, use the nearest clean accepted frame or a corrected continuity reference instead.

If first-frame conditioning is unavailable, use the strongest supported reference method and explicit handoff wording. Never claim frame conditioning is active when the selected model or workflow does not support it.

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
