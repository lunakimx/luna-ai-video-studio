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
- known generation risk

## Handoff rule

For directly connected clips, copy the previous final visible state into the next opening state.

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

## Update rule

After an approved prompt, accepted revision, or accepted generated clip:

1. update only values that actually changed;
2. preserve every unchanged lock;
3. prefer the accepted generated result over an earlier planned state when the user approves that result;
4. carry the final state forward when continuity matters.

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
