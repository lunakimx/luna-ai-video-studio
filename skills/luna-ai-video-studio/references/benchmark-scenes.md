# Benchmark Scenes

Use these scenes for repeatable prompt-level and generated-output evaluation.

Keep test conditions fixed when comparing skill versions or prompt methods.

## Benchmark 01 — Dialogue close-up

Create a 7-second close shot of one woman in a quiet room delivering one short emotional line. The acting should remain restrained. Breathing, eyes, jaw, and a small hesitation should carry the performance. No unnecessary camera movement.

Test targets:
- dialogue length control
- lip-sync feasibility
- micro-performance
- close-shot restraint
- sound perspective

Common failures:
- overacting
- long exposition
- excessive head movement
- drifting camera

## Benchmark 02 — Underwater suspense

Create an 8-second shot from inside a moving research submersible. The submersible advances continuously through dark water. Suspended particles, nearby debris, and depth parallax must prove forward movement. A massive hidden lifeform becomes partially visible outside the window near the end, but the full body must stay hidden.

Test targets:
- environmental motion
- parallax
- suspense timing
- partial reveal
- scale
- physically believable water response

Common failures:
- frozen exterior water
- premature full reveal
- background teleportation
- scale collapse

## Benchmark 03 — Comedy timing

Create an 8-second office shot. One worker notices something absurd behind them, freezes for a beat, slowly turns, reacts with contained disbelief, then tries to continue working as though nothing happened.

Test targets:
- setup
- pause
- readable reaction
- aftermath
- camera restraint

Common failures:
- joke happens immediately
- exaggerated acting
- camera movement hides the reaction

## Benchmark 04 — Premium product film

Create an 8-second premium product shot of one engraved metal coin or jewelry object under controlled studio lighting. Preserve product proportions and design. Reflections must move consistently with camera or product movement. Important engraving and material detail should remain readable.

Test targets:
- product fidelity
- material response
- reflection behavior
- camera precision
- text / engraving risk awareness

Common failures:
- warped product geometry
- changing engraving
- random text
- uncontrolled reflections

## Benchmark 05 — Solo dance performance

Create an 8-second full-body performance shot of one solo performer executing one short choreography phrase. Maintain stable identity and outfit. Feet must contact the floor believably, body weight must transfer, and the camera must preserve choreography readability.

Test targets:
- full-body motion
- foot contact
- identity stability
- framing
- secondary motion

Common failures:
- sliding feet
- cropped limbs
- identity drift
- camera overpowering choreography

## Benchmark 06 — Creature partial reveal

Create an 8-second suspense scene in which a large creature is suggested through environmental disturbance, one visible body part, and the human character's reaction. Do not show the full creature.

Test targets:
- reveal discipline
- environmental cause-and-effect
- scale
- reaction timing

Common failures:
- full creature reveal
- generic monster redesign
- reaction before visual cause

## Benchmark 07 — Action geography

Create an 8-second corridor shot. One runner moves forward while the camera tracks backward at a controlled matching speed. Doorways and wall details must pass consistently, preserving travel direction and depth.

Test targets:
- geography
- speed match
- backward tracking
- parallax
- grounded running

Common failures:
- treadmill motion
- changing corridor layout
- accidental zoom
- reversed direction

## Benchmark 08 — Wind and rain response

Create an 8-second exterior shot of one character standing in strong wind and light rain. Hair, clothing, rain direction, loose objects, and nearby foliage must respond coherently to the same wind direction.

Test targets:
- environmental coherence
- secondary motion
- weather direction
- physical evidence

Common failures:
- independent random motion
- static clothing
- rain moving against wind without cause

## Benchmark 09 — Found-footage realism

Create an 8-second late-night handheld clip with one believable camera operator. Movement and shake must be physically motivated by walking and stopping. Sound perspective should feel local and unpolished rather than trailer-like.

Test targets:
- documentary restraint
- motivated handheld movement
- realistic sound
- avoidance of over-cinematic polish

Common failures:
- artificial shake
- impossible camera glide
- dramatic trailer sound design

## Benchmark 10 — Connected two-clip continuity

Clip A ends with one character wearing a wet dark jacket, holding a flashlight in the right hand, moving toward a doorway while the camera tracks backward, with a warm light source coming from frame left and steady rain ambience audible in the same acoustic space.

Clip B must begin from the same visible and moving state and continue the action without resetting identity, wardrobe, hand state, screen direction, lighting, object placement, subject momentum, camera momentum, environmental motion, or audible ambience.

When the selected test model supports first-frame conditioning or an equivalent start-frame image input, use the accepted actual final frame of Clip A as Clip B's first-frame reference. If the exact final frame is visibly corrupted or contains an unwanted transient artifact, use the nearest clean accepted frame and record that choice.

Preserve the accepted connected-shot resolution, aspect ratio, framing, and crop. Do not change to 1920×1088 merely because the workflow is described as 1080p; use the selected model's verified supported dimensions and preserve them consistently across the pair.

If frame rate or timebase is exposed by the workflow, keep it consistent across the two clips. If native or generated audio is present, preserve rain ambience, room or corridor tone, sound perspective, and any continuing decay or movement sounds across the boundary.

After generation, inspect the stitch boundary for a duplicated visual frame, repeated motion beat, micro-stutter, abrupt camera-speed reset, subject-speed reset, environmental-motion reset, duplicated transient sound, or abrupt ambience change.

Test targets:
- shot ledger usage
- accepted final-frame to first-frame handoff
- first-frame conditioning when supported
- hand and prop continuity
- lighting continuity
- resolution / framing / crop continuity
- subject movement direction, speed, and phase continuity
- camera movement direction and apparent speed continuity
- environmental motion continuity
- native or generated audio continuity when present
- boundary-frame and boundary-audio inspection
- story-state continuity

Common failures:
- flashlight changes hands
- jacket becomes dry
- character orientation flips
- lighting direction changes
- next clip starts from a neutral pose instead of the ending movement phase
- camera suddenly stops, reverses, or changes speed without cause
- rain or other environmental motion resets direction or intensity
- handoff frame is unnecessarily resized or recropped
- 1920×1088 is forced without model-specific support or workflow justification
- duplicated boundary frame creates a pause or micro-stutter
- ambience restarts at a different loudness or acoustic character
- a transient sound is duplicated across the boundary

## Benchmark 11 — Stylized animation timing

Create a 6-second stylized animated action with a clear anticipation, impact, and follow-through. Motion and camera behavior must match the selected animation language rather than defaulting to live-action realism.

Test targets:
- animation-language inference
- anticipation
- follow-through
- appropriate exaggeration

Common failures:
- photorealistic motion imposed on stylized animation
- missing anticipation
- no readable impact

## Benchmark 12 — Vertical social hook

Create a 6-second 9:16 social clip with a strong opening image, one dominant visual event, one readable reaction or supporting beat, and an ending frame that lands cleanly.

Test targets:
- immediate visual readability
- short-duration discipline
- vertical composition
- ending strength

Common failures:
- too many events
- weak first frame
- payoff too early
- dead final seconds

## Benchmark execution

For prompt-level testing:

1. use the exact benchmark brief;
2. run the skill's normal production process;
3. score with `evaluation-protocol.md` Mode A;
4. record hard failures and repair requirements.

For generated-output testing:

1. keep model, version, duration, aspect ratio, resolution tier, references, and attempt count fixed between variants whenever possible;
2. generate both variants;
3. score with Mode B or Mode C;
4. record first-pass success and repair passes;
5. do not call the system production-validated without generated-output evidence.
