---
name: luna-image-prompt
description: Plan, prompt, create when explicitly requested, inspect, and surgically revise reference-faithful images for Luna's image-to-video, portrait, character-sheet, scene-still, and reusable two-reference workflows. Preserve identity and previously approved details while preparing motion-ready visual assets.
---

# Luna Image Prompt

Turn a short image idea, supplied references, or an existing image into a coherent, reference-faithful image brief, generation prompt, or review. Support realistic people, animals, stylized characters, cinematic scenes, and reusable community prompts. Use the user's requested language and output format.

A request to analyze, plan, or write prompts does **not** authorize running image generation, editing a user file, publishing, or spending credits. Generate images only after an explicit image-generation/edit request. For revisions, preserve the accepted source and make a new version.

## Instruction order

1. Latest explicit user instructions and requested output.
2. Still-active approved locks, including character identity and scene state.
3. Uploaded visual references only in their assigned roles.
4. Conservative choices that do not conflict with the above.

Never infer a person's exact appearance from a textual description when the user expects a supplied identity reference. Never treat a reference as controlling properties outside its assigned role.

## Default two-image workflow

For reusable prompts designed for two inputs:

- IMAGE 1 = ID: source of identity, facial proportions, age impression, recognizable markings, hair, and other explicitly locked character traits.
- IMAGE 2 = SCENE: source of location, staging, camera geometry, lighting, mood, composition, or approved pose, **not** a second person's face.
- If the user explicitly assigns a different reference order or role, follow that mapping instead.
- Where an editing task provides an accepted scene image, use it as the base image and preserve its accepted visual properties. Restore the identity from the ID reference without rebuilding the whole scene.
- Keep gender-neutral and public-template prompts reusable. Change clothing only when the user requests a gender-conditioned wardrobe branch.
- Do not invent a second character, couple, accessory, prop, caption, watermark, or logo.

For multiple inputs, list each actual attached asset with its exact interface tag and one assigned responsibility. Never write invented @img, @video, panel indices, or file paths in a final model prompt. UI tag numbers follow the tool's actual attachment order; they are not universal.

## Identity-first production

- Preserve recognizable facial geometry, eye and nose placement, lips, jaw, cheek volumes, skin appearance, hairline, realistic anatomy, distinctive markings, and explicitly approved clothing/footwear/accessories.
- Do not replace a supplied person with a generic idealized face or smooth away identity-bearing features. Do not promise perfect facial matching.
- Give the authoritative original identity image priority over a generated turnaround or a later scene still.
- If references disagree, do not blend identities. Prefer the authoritative image and explain any genuine ambiguity that blocks execution.
- For animals, preserve fur patterns, anatomical left/right markings, collar or pendant ownership, body proportions, and species-appropriate poses; do not apply human portrait assumptions.
- When an image contains multiple different people, assign each person a separate authoritative identity reference when available and lock the visible character count.

## Character-sheet decision

Make a sheet only when it adds reliable information and the target image/video workflow can use it as a character reference.

For a new photoreal character sheet intended for video, consider:
- full-body front view for posture, clothing, footwear, and scale;
- full-body rear or side view when the story requires it;
- one large, sharp facial close-up for identity and facial features.

Keep body scale, lighting, clothing, hairstyle, and accessory ownership consistent across panels. The original ID reference remains superior to the sheet. Do not force this layout on two-image public prompts, on a single still, on a video model that interprets a board as its opening frame, or on a user who requested another sheet layout.

## Editing and asset conservation

When changing an approved image:

1. Record the base image and what is already accepted.
2. Identify the smallest requested change region, such as shoes, a sleeve, a hand, a background sign, or a single facial feature.
3. Name the properties to change and the properties that must remain untouched.
4. Prefer localized masking/inpainting or an equivalent supported editing operation. If unavailable, give a precise edit prompt without claiming pixel-perfect preservation.
5. Save the new result as a separate version; never silently erase the last approved result.
6. Review the changed region **and** unintended changes outside it. If the edit changes identity, composition, lighting, or other locks, reject or repair it.

For a multistep change, use accepted base → controlled variation → final scene image rather than rebuilding the character with every new shot. An outfit change must not silently change the face; a shoe change must not change the room.

## Motion-ready scene images

Create a person-free/environment-only clean plate first **when it materially reduces continuity risk** for complex movement, contact, multiple actors, locked obstacles, or set reuse. Do not create extra clean plates for ordinary portraits or simple scenes.

Plan the entry and exit paths, action space, object anchors, body-scale landmarks, obstacle geometry, camera-side logic, lighting direction, contact points, and subject/background depth before adding characters. Explicitly preserve fixed architecture and obstacle openings. Do not confuse the production clean plate with a mandatory opening shot.

For image-to-video handoff, select the minimum useful scene images. A beautiful but motion-impossible pose is not accepted. Check available space, reachability, foot placement, gaze target, prop ownership, and the next action's starting position.

## Quality and revision gate

Before returning a final image prompt or approving a generated image, check:
- correct reference count, source assignment, and true availability of all cited inputs;
- face or character identity, distinctive markings, hair, wardrobe, footwear, accessories;
- exact actor count; no accidental doubles or unrequested companions;
- prompt/pose/background coherence and stable camera geometry;
- hands, feet, paws, contact, prop count and ownership;
- lighting and background perspective; relevant physical scale;
- motion-ready start state and usable subject clearance for video;
- text, sign, and watermarks only where explicitly required;
- no contradictions, duplicate commands, or invented model capabilities;
- preservation of accepted visual elements after revisions.

Review and diagnostics do not prove a future model generation will match the prompt. When a generated image is provided, judge the visible result.

## Experimental face-obscuring technique

A third-party workflow experimented with marking small sheet faces to bias the model toward a larger facial close-up. **This is not a default technique.** Do not add grids, scribbles, masks, or hatching to any face without explicit authorization for a controlled test. They may contaminate the result or discard useful identity information.

If the user asks to test it, compare clean sheet, close-up-priority sheet, and marked small-face sheet using the same inputs/model/settings where possible. Inspect both identity drift and marks transferred into output before deciding whether to keep the technique.

## Output

Return the requested artifact only: concise prompt, sheet plan, scene-image plan, edit instructions, generated image (when explicitly requested), or visual QA. For a revision, provide a complete ready-to-use final prompt when the user requests the full prompt, preserving all unrelated approved details.

For advanced examples and asset handoff checks, read `references/identity-scene-workflow.md`.
