# Retry and Repair Playbook

Use this reference when reviewing a generated clip, fixing a failed prompt, or preparing a safer retry.

## Goal

Fix the failed behavior with the smallest useful change while preserving everything that already works.

Do not treat every failed generation as a reason to rewrite the entire production.

## Repair priority

Fix problems in this order:

1. reference fidelity and identity
2. character or prop count
3. continuity-critical errors
4. spatial clarity
5. camera behavior
6. motion and environmental response
7. dialogue and lip-sync feasibility
8. timing and ending strength
9. stylistic polish

A beautiful retry is still a failed retry if identity, continuity, or the requested action breaks.

## Diagnostic pass

Before rewriting, identify:

- the failed behavior
- the affected moment or time range when visible
- what already works and must be preserved
- the most likely prompt or capability cause

Classify the likely cause as one or more of:

- ambiguous instruction
- contradictory instruction
- too many simultaneous actions
- excessive camera complexity
- timing overload
- weak spatial staging
- reference ambiguity
- unsupported or uncertain model feature
- weak positive constraints
- continuity reset
- insufficient physical evidence

## Common failure map

### Identity drift

Symptoms:
- face changes
- hairstyle changes
- wardrobe changes
- body proportions shift

Repair:
- restate the authoritative reference
- reduce competing style language
- lock only visible identity-critical attributes
- avoid multiple references competing for the same identity role

### Extra or missing characters

Symptoms:
- duplicated person
- missing person
- unexpected crowd member

Repair:
- state the exact visible character count
- identify each role spatially
- reduce crowd complexity if it is not essential
- prefer positive count language such as `exactly two people remain visible`

### Frozen environment

Symptoms:
- subject moves while the world feels like a still image
- water, wind, debris, reflections, or background depth do not react

Repair:
- add visible physical evidence of movement
- specify parallax and depth change
- connect environmental response to the subject or camera motion

### Weak human motion

Symptoms:
- sliding feet
- floating body
- weightless contact
- robotic stopping

Repair:
- specify foot contact
- weight transfer
- arm and torso response
- stopping behavior
- clothing and hair secondary motion

### Camera drift

Symptoms:
- unwanted zoom
- random orbit
- unstable composition
- wrong ending position

Repair:
- reduce to one primary camera move
- define start position, path, speed, and end position
- remove decorative camera language that does not serve the shot

### Spatial teleportation

Symptoms:
- threat, prop, or person jumps location
- screen direction flips without cause

Repair:
- restate foreground, midground, and background relationships
- lock screen direction
- define where entering objects originate
- preserve camera side

### Overloaded shot

Symptoms:
- only part of the requested sequence happens
- actions merge or disappear
- payoff happens before setup registers

Repair:
- reduce to one dominant action plus one supporting action or reaction
- protect setup time
- split into separate clips when the model or duration cannot carry the full event cleanly

### Weak lip sync

Symptoms:
- mouth motion does not match speech
- line is cut off
- facial performance collapses during dialogue

Repair:
- shorten dialogue
- use pronounceable spoken phrasing
- leave pauses and breathing room
- reduce competing physical action while speaking
- move audio to post when native speech is not reliable or supported

### Premature reveal

Symptoms:
- creature, product feature, gag, or reveal appears too early
- hidden information becomes fully visible

Repair:
- protect anticipation time
- state exactly what remains hidden
- specify the first moment the reveal may become visible
- limit visible body area or information

### Dead ending

Symptoms:
- main action finishes and the remaining clip becomes filler
- clip cuts before the reaction lands

Repair:
- define a readable end state
- reserve time for reaction or visual hold
- make the final image usable for the next connected clip when relevant

## Retry passes

Use progressive simplification rather than adjective stacking.

### Pass 1 — Targeted patch

Change the smallest set of instructions that directly caused the failure.

### Pass 2 — Complexity reduction

If the same failure repeats:

- reduce simultaneous actions
- simplify camera behavior
- shorten dialogue
- strengthen positive constraints
- remove unsupported dependencies

### Pass 3 — Model-safe rebuild

If the failure remains:

- preserve all approved locks
- rebuild the shot around one dominant action
- use a physically clear camera path
- define environmental response
- protect the end state
- remove fragile feature assumptions

Do not repeat an identical prompt and expect a deterministic repair.

## Revision patch output

When useful, provide:

### FAILURE DIAGNOSIS
- failed behavior:
- likely cause:
- affected moment:
- preserve:

### REVISION PATCH
- remove:
- strengthen:
- simplify:
- restate:

### RETRY PROMPT

Provide a corrected prompt that is independently executable.
