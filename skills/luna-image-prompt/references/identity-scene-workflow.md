# Identity and Scene Workflow

This file supplements Luna Image Prompt; do not automatically include every section in each generation prompt.

## 1. Reference manifest: read before prompting

Record only real available inputs:

| Input | Role | Authoritative properties | Must not control |
| --- | --- | --- | --- |
| IMAGE 1 | ID | face, identity, unique markings, explicitly locked character details | background, camera position from IMAGE 2 |
| IMAGE 2 | SCENE | set geometry, accepted pose, camera, light, mood | identity or facial anatomy |
| optional IMAGE 3 | wardrobe/prop or alternate-angle reference | specifically assigned details | unrelated subject identity |
| optional accepted result | EDIT BASE | pixels/composition the user accepted | unrequested redesign |

If the user labels images differently, use the user's labels. Build the manifest from actual attachments, not imagined files. If the tool accepts only one input, choose the most valuable supported reference and translate missing details into text. Do not pretend unavailable files were connected.

## 2. Optional camera-ready character sheet

Use a full-body front, full-body rear/side, and large face close-up when appropriate. Normalize the environment and light across views, keep character count per panel clear, lock footwear and accessories, and avoid tiny face duplication where it competes with the primary close-up. The original ID reference controls the sheet. Different characters require distinct sheets when possible.

For an animal sheet, include left/right anatomical markings, fur texture, paws, collar/pendant position, and body proportions. Never flip a signature marking because an output panel is mirrored.

## 3. Clean-plate planning

For complex action scenes:
- Stage the empty location and define permanent geometry: walls, doors, passage openings, tables, immovable objects, terrain.
- Define screen-left/right in the chosen camera view; record entry and exit paths, usable floor space, collision point, and sightlines.
- Record scale references (door width, car height, table edge, actor body length) only where useful.
- Keep background coherent: horizon, sunlight, reflections, cast-shadow direction, and lens perspective.
- Add characters to this accepted scene without changing fixed geometry.
- If the video workflow works better from a single opening image, composite the start state into a motion-ready frame. Do not output the empty plate as the final start frame unless requested.

## 4. Surgical edit prompt pattern

BASE: [actual accepted image]
CHANGE: [exact object/region + new target]
KEEP: [face/identity, hair, unaffected wardrobe, pose, framing, lighting, background positions, props, quality]
BOUNDARY: [what cannot spread outside the requested region]
QC: [what visible evidence establishes success]

Example: "Edit only the shoes on the approved character sheet. Change to the attached reference shoes. Keep the same woman's face, hairstyle, height, pose, clothing, shadow direction, camera, and background unchanged. Do not regenerate the body or scene. Review for shoe accuracy and face drift."

Mask-based editing is preferred if supported. Without masking, preservation is a best-effort instruction, not a guarantee.

## 5. Image QA before video

Require a legible start pose, reachable props, no overlapping limbs obscuring critical contact, clear travel direction, plausible obstacle geometry, stable character count, and enough frame space for the next action.

For connected scenes, record the accepted image identifier and major locks in the project's existing production ledger. Proposed images do not become approved merely because they were generated.

## 6. Face-priority A/B test (off by default)

Keep the original identity photo untouched. Test (A) clean character sheet, (B) larger close-up emphasis without obscuration, and only with user approval (C) marked small face. Keep camera/scene, model version, reference order, aspect ratio, and attempt count consistent if possible. Check for rendered grid artifacts, likeness, anatomy, and model-specific failure. Record observations rather than claiming universal success.
