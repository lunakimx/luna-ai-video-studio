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

Resolve aspect ratio before pixel dimensions. Preserve the actual accepted dimensions when supported. Illustrative sizes, not universal provider controls:

| Aspect | 720p example | 1080p example |
| --- | --- | --- |
| 16:9 landscape | 1280×720 | 1920×1080 |
| 9:16 portrait | 720×1280 | 1080×1920 |

For square, cinematic, or other ratios, use the selected provider's supported dimensions. Never force these examples onto a different ratio or claim that a resolution tier guarantees a particular size. Bitstream alignment is an implementation detail; do not change visible framing for it without verified need.

When capability or behavior is uncertain, prefer the model's documented native resolution and keep the connected-shot workflow consistent rather than forcing 1920×1088.

## Frame rate and timebase

When several generated clips will be stitched into one continuous sequence, preserve the same delivered frame rate or timebase across adjacent clips whenever the workflow exposes or controls it.

Do not invent a frame-rate control when the model does not expose one.

If generated clips arrive with different frame rates, treat normalization as an editing or delivery concern and avoid claiming seamless frame-level handoff until the clips have been conformed and inspected.

A matching resolution does not guarantee a smooth transition when frame cadence differs.

## Post-output resolution QC

Keep all resolution examples and model-specific exceptions above. This gate validates an explicitly accepted delivery target; it does not impose 1080p on generation or silently resize source media. Probe the original download, upscale result, subtitle render and final export separately. Keep paths/checksums and the job/export settings in the accepted production ledger so a preview or older file cannot be mistaken for the deliverable.

Use Python 3 and ffprobe on local files. Run from this skill's directory after every authorized output step and before delivery. Require a successful process exit before the next delivery step; do not report a check as run when ffprobe or the file is unavailable.

```bash
python scripts/video_qc.py final.mp4 --size 1080x1920 --aspect 9:16 --fps 30000/1001 > final.qc.json
# Before joining, compare every clip at the accepted connection size/rate:
python scripts/video_qc.py clip-b.mp4 --previous clip-a.mp4 --size 720x1280 --aspect 9:16 --fps 24 > connection.qc.json
```

Choose the actual accepted rational FPS, not a rounded UI label: 30000/1001 and 30 differ. Repeat `--previous` for more adjacent clips; run again on the joined output. The script reads only, emits JSON, and returns 0 for metadata PASS, 1 for a failed delivery gate, or 2 for unavailable/invalid input or probe errors. It does not perform a conversion. A local executor must invoke it after the render/download completes; this document alone does not install a provider webhook.

For manual evidence collection, use:

```bash
ffprobe -v error -select_streams V:0 -show_streams -show_frames -show_entries 'stream:frame=best_effort_timestamp,width,height,sample_aspect_ratio' -of json final.mp4
```

Inspect the primary non-cover video stream (`V:0`); select the intended delivery track separately if the asset has multiple video tracks. Keep width/height (decoded image dimensions) separate from coded_width/coded_height (codec storage/alignment). Do not crop visible content merely because coded dimensions differ.

Gate rules:

- Require exact accepted width and height. For a 9:16 1080p target that is 1080×1920; 1920×1080 or a 512-pixel preview fails. Use explicit dimensions for 480p too: the tier name alone cannot establish the provider's portrait dimensions.
- Require known SAR 1:1 for canonical delivery. Compute unrotated DAR = width / height × SAR; compare declared DAR when present. Missing DAR is reported and derived only when SAR is known. Unknown SAR never silently becomes 1:1.
- Inspect both legacy rotate tags and display-matrix side data. Report effective DAR after 90°/270° rotation by taking its reciprocal. Flag conflicting, unreadable or nonzero rotations for normalization and reinspection. A 1920×1080 file rotated 90° can display vertically but is not a canonical 1080×1920 delivery. This conservative gate may flag otherwise playable sources; preserve them and handle orientation in the authorized edit workflow.
- Check avg_frame_rate, r_frame_rate, time_base and all decoded frame timestamps. Matching rate labels alone do not establish CFR. Fail variable intervals, gaps, non-increasing timestamps, insufficient evidence, and per-frame dimensions/SAR changes. Allow only one timestamp tick of quantization with a sufficiently fine timebase.
- Compare adjacent clips' size, SAR, effective DAR, rotation and rational FPS. A different timebase is a warning to conform in the editor, not proof of a speed change. Resolve it before stream-copy concatenation. Do not silently force FPS, duplicate/drop frames or interpolate motion; use an authorized conform step, then recheck cadence and boundary motion/audio.

### Stretch and crop review

Metadata PASS is not final visual approval. A stretched subject or destructive crop can already be baked into perfectly valid 1080×1920 pixels. Compare source and output opening/middle/ending frames and both sides of each join; inspect faces, circles, body proportions, edge landmarks, intended head/foot room and motion at the boundary. Keep `visual_status: UNVERIFIED` until this separate review is actually done; document its result in the ledger.

Never force arbitrary input directly through `scale=1080:1920`, set an aspect tag to disguise wrong pixels, or use `setsar=1` alone to repair an anamorphic image. Resolve source SAR and orientation first, scale uniformly to fit, then pad only if allowed. Crop-to-fill needs an accepted crop that preserves intended content; never choose it silently. A verified square-pixel, zero-rotation source with the same aspect can be scaled proportionally to the target without cropping. Reprobe and visually inspect the result in the target player/editor; do not rotate twice when the decoder already applied rotation.

### Upscale versus export size

Record these separately: source measured dimensions; requested delivery dimensions; operation/tool/model/settings or job ID; final measured dimensions; visual review. Preserve the source and inspect the actual returned asset.

- A 480p/720p source exported at 1080×1920 has a larger raster if scaling was applied. Ordinary Lanczos/bicubic scaling is resampling; the export setting alone provides no evidence of detail restoration.
- An enhancement/super-resolution workflow from 480p/720p to 1080p needs evidence of that completed operation and a source/output visual comparison. It may infer new detail, introduce artifacts or fail to improve quality. Never claim recovered original detail solely from dimensions.
- A native 1080p generation, a resampled 1080p export, and an enhancement upscale can have identical ffprobe dimensions. ffprobe cannot distinguish their provenance. Keep `upscale_provenance: UNVERIFIED` in the automatic report; establish it from actual job records, never a filename or UI badge.

For the reported 2026-10-07 incidents, the actual affected files were not inspected in this patch investigation. Wrong resize/crop settings, SAR handling, rotation handling, preview selection and source/output mix-ups are hypotheses only. No exact cause has been established.

Reference: [ffprobe documentation](https://ffmpeg.org/ffprobe.html) and [FFmpeg scale/setsar documentation](https://ffmpeg.org/ffmpeg-filters.html). Metadata QC does not replace decoded-frame review or prove a seamless one-take result.

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

