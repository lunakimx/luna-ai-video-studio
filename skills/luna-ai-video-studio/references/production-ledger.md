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
- dialogue state
- important audio event
- end state
- continuity handoff
- accepted delivered resolution when relevant
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

If the verified model or pipeline benefits from 16-pixel-aligned dimensions and accepts 1920×1088 without unwanted crop, stretch, or delivery problems, the connected workflow may use 1920×1088 consistently.

If the selected model or delivery path expects native 1920×1080, preserve 1920×1080 instead.

For 720p connected clips, preserve 1280×720 unless the selected model documents another native size.

If the model internally resizes first-frame or last-frame references, record that behavior when it affects continuity and do not claim pixel-identical handoff.

## Boundary-frame stitching

Before concatenating directly connected clips, inspect the transition boundary.

If the previous clip's final frame and the next clip's opening frame repeat the same visible moment, trim only the redundant overlap needed to avoid a visible pause, repeated beat, or micro-stutter.

A one-frame trim may be appropriate when exactly one duplicate boundary frame is present, but do not make one-frame trimming automatic. Inspect the actual boundary first.

Do not trim away a meaningful action phase, reaction, audio sync point, or continuity cue merely to make the cut shorter.

## Update rule

After an approved prompt, accepted revision, or accepted generated clip:

1. update only values that actually changed;
2. preserve every unchanged lock;
3. prefer the accepted generated result over an earlier planned state when the user approves that result;
4. carry the final state forward when continuity matters;
5. when first-frame conditioning is supported, record which accepted final frame should be used as the next clip's start reference;
6. when resolution affects continuity, record the actual accepted delivered dimensions and preserve them across connected clips unless the workflow changes.

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
- boundary trim note when applicable:
