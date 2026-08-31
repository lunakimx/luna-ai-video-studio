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

Clip A ends with one character wearing a wet dark jacket, holding a flashlight in the right hand, facing a doorway, with a warm light source coming from frame left.

Clip B must begin from the same visible state and continue the action without resetting identity, wardrobe, hand state, screen direction, lighting, or object placement.

Test targets:
- shot ledger usage
- final-to-first-frame handoff
- hand and prop continuity
- lighting continuity
- story-state continuity

Common failures:
- flashlight changes hands
- jacket becomes dry
- character orientation flips
- lighting direction changes

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
