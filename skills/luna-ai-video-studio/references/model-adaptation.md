# Model Adaptation

Video-model behavior changes quickly. Treat model-specific knowledge as time-sensitive.

When the user names a model, adapt the prompt only to capabilities you can reasonably verify or know with confidence. If current documentation or browsing tools are available and the feature matters to execution, verify it before relying on it.

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
