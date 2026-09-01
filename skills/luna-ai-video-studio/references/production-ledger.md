# Production Ledger

Use this reference when a project spans multiple clips, requires continuity, or is being revised over time.

Keep the ledger internal unless the user asks to see it.

## Purpose

Track the approved state of the production so later prompts preserve identity, continuity, scene logic, and handoff state instead of resetting the production between clips.

## Global project state

Record only values that matter to future execution:

- project title or working name
- format and genre
- target platform when relevant
- target duration per clip
- aspect ratio
- selected generation model and version when known
- reference assets and the job of each reference
- audio approach
- overall visual language
- continuity sensitivity
- accepted generation resolution when continuity-sensitive
- accepted frame rate or timebase when the workflow exposes it and stitching depends on it

Do not invent fixed values that the user has not approved and that cannot be safely inferred.

## Locked elements

Once a value is approved or clearly established by an authoritative reference, preserve it until the user explicitly changes it.

### Character lock

Track when relevant:

- name or role
- visible identity and facial proportions
- hairstyle and color
- body proportions
- wardrobe and footwear
- accessories and makeup
- props
- hand state
- dirt, damage, blood, wetness, wear, or aging state
- performance tone

### World lock

Track when relevant:

- location and architecture
- time of day
- weather
- lighting direction and identity
- environmental condition
- important foreground, midground, and background objects
- object placement
- product state
- vehicle state
- creature design, scale, visibility, and injury state

### Story lock

Track:

- what has already happened
- current scene state
- information the audience knows
- information that must remain hidden
- unresolved action that must continue in the next clip

## Shot ledger

For every approved connected shot, retain:

- shot or clip identifier
- shot purpose
- start state
- dominant action
- supporting action or reaction
- camera start state
- camera movement and ending position
- subject movement direction, speed, and movement phase when continuity depends on them
- camera movement direction and speed at the handoff when continuity depends on them
- dominant environmental motion direction and intensity
- dialogue state
- important audio event
- ending ambience or room-tone state when audio continues across the transition
- end state
- continuity handoff
- accepted delivered resolution when relevant
- accepted frame rate or timebase when relevant
- known generation risk

## Handoff rule

For directly connected clips, copy the previous final visible state into the next opening state.

When the selected model supports first-frame conditioning or an equivalent start-frame image input, prefer using the accepted previous clip's actual final frame as the next clip's first-frame reference image.

Treat that actual final frame as authoritative for continuity-critical visible state, including:

- facial identity and hairstyle
- wardrobe and accessories
- hand and prop state
- subject position and orientation
- pose or movement phase
- camera side, framing, and relative position
- screen direction and travel direction
- damage, dirt, blood, and wetness
- lighting direction and exposure state
- important object placement
- creature or product state
- environmental state and motion

Do not rely on text-only continuity instructions when a usable accepted final frame is available and the selected model can consume it as a first-frame reference.

If the final frame contains a generation artifact, unwanted blur, deformation, transient muzzle flash, motion smear, occlusion, or other state that should not be preserved, do not blindly carry it forward. Use the nearest clean accepted frame or a corrected continuity reference instead.

If first-frame conditioning is unsupported, unavailable, or would conflict with the intended next-shot composition, preserve the same handoff state through the strongest supported reference method and explicit continuity instructions.

Preserve, when relevant:

- subject position and orientation
- screen direction and travel direction
- camera side
- hand and prop state
- pose or movement phase
- wardrobe state
- damage, dirt, and wetness
- lighting direction
- object placement
- creature state
- environmental motion

Do not reset the world because a new generation begins.

## Resolution handoff

For directly connected clips, preserve the accepted prior shot's delivered pixel dimensions for the next connected generation whenever the selected model supports that resolution.

When first-frame conditioning is used, keep the chosen handoff frame at the same:

- pixel dimensions;
- aspect ratio;
- framing;
- visible crop.

Do not resize, stretch, pad, or recrop the approved handoff frame merely to satisfy a generic resolution preference. Change it only when the selected model, platform, editor, or delivery target requires another supported format.

For workflows described as 1080p, record the actual accepted dimensions rather than assuming all models use the same size.

Never convert 1080p to 1920×1088 merely because 16-pixel alignment exists. Use 1920×1088 only when the selected model or pipeline supports or produces it cleanly and there is a demonstrated workflow reason to preserve that aligned size.

If the selected model or delivery path expects native 1920×1080, preserve 1920×1080 instead.

For 720p connected clips, preserve 1280×720 unless the selected model documents another native size.

If the model internally resizes first-frame or last-frame references, record that behavior when it affects continuity and do not claim pixel-identical handoff.

## Motion handoff

A matching still frame is not enough for a seamless moving transition.

When motion continues across directly connected clips, preserve the previous ending motion state into the next opening state when relevant:

- subject travel direction;
- subject velocity or apparent speed;
- stride, turn, gesture, or action phase;
- camera movement direction;
- camera velocity or apparent tracking speed;
- camera height and distance trend;
- dominant hair and wardrobe secondary motion;
- wind, rain, water, smoke, debris, particles, foliage, reflections, or other continuing environmental motion.

Do not restart a moving subject from a neutral pose merely because a new clip begins.

Do not stop, reverse, or sharply change camera velocity at the boundary unless the edit intentionally calls for that change.

When an exact velocity value is unavailable, preserve the visible motion relationship instead, such as `camera continues retreating at the same apparent speed while the runner maintains the same forward pace`.

If the model cannot reliably preserve a complex moving handoff, simplify the opening action while retaining direction and momentum rather than inventing a physically contradictory transition.

## Audio continuity handoff

When connected clips contain generated or native audio, carry the audible environment across the boundary when the story location and acoustic space have not changed.

Preserve when relevant:

- ambience and room tone;
- weather bed;
- crowd or environmental bed;
- machinery, ventilation, traffic, water, wind, or electrical hum;
- continuing footsteps, breathing, engine, creature, or object sounds;
- reverberation character and apparent room size;
- sound-source distance and screen position;
- the decay tail of a gunshot, impact, alarm, shout, or other event that logically continues across the cut.

Do not restart ambience at a noticeably different loudness, tone, acoustic space, or perspective without an on-screen reason.

If native audio generation cannot preserve exact continuity, keep the intended acoustic state consistent in the next prompt and flag the boundary for editing review rather than pretending sample-accurate continuity is guaranteed.

Do not duplicate a transient sound at both the end of clip N and the beginning of clip N+1 unless the visible action genuinely repeats it.

## Frame rate and timebase handoff

When the workflow exposes a delivered frame rate or timebase and the connected clips will be stitched, preserve it across adjacent clips whenever possible.

Do not invent a frame-rate value when the generator does not expose or document one.

If adjacent clips arrive with different frame rates, record the mismatch and treat conformance as an editing step before claiming a seamless frame-level transition.

## Boundary-frame stitching

Before concatenating directly connected clips, inspect the transition boundary.

If the previous clip's final frame and the next clip's opening frame repeat the same visible moment, trim only the redundant overlap needed to avoid a visible pause, repeated beat, or micro-stutter.

A one-frame trim may be appropriate when exactly one duplicate boundary frame is present, but do not make one-frame trimming automatic. Inspect the actual boundary first.

Also inspect the audio boundary for duplicated transients, abrupt ambience changes, or clipped decay tails when audio is present.

Do not trim away a meaningful action phase, reaction, audio sync point, sound decay, or continuity cue merely to make the cut shorter.

## Update rule

After an approved prompt, accepted revision, or accepted generated clip:

1. update only values that actually changed;
2. preserve every unchanged lock;
3. prefer the accepted generated result over an earlier planned state when the user approves that result;
4. carry the final state forward when continuity matters;
5. when first-frame conditioning is supported, record which accepted final frame should be used as the next clip's start reference;
6. when resolution affects continuity, record the actual accepted delivered dimensions and preserve them across connected clips unless the workflow changes;
7. when motion continues, record the visible subject, camera, and environmental motion state required for the next opening;
8. when audio continues, record the ambience, room tone, important continuing sounds, and transient decay state required for the next opening;
9. when frame rate or timebase is exposed and affects stitching, preserve or record it across the connected sequence.

## Conflict rule

When ledger state conflicts with a new explicit user instruction, the new instruction wins only for the element the user changed.

Do not use one requested change as permission to redesign unrelated approved elements.

## Memory compression

Keep the ledger compact.

Do not store decorative prose, rejected ideas, or details that cannot affect later generation.

When a long project accumulates many shots, preserve current locks plus the handoff state required for upcoming shots rather than repeating the full history in every prompt.

## Visible output

Show ledger information only when it helps the user review continuity or when the user asks for it.

Use:

### SHOT LEDGER UPDATE
- clip:
- locked carryover:
- changed this turn:
- final state:
- next-shot handoff:
- first-frame reference when applicable:
- resolution handoff when applicable:
- motion handoff when applicable:
- audio handoff when applicable:
- frame-rate/timebase note when applicable:
- boundary trim note when applicable:
