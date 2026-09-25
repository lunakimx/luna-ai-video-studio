# Revision workflow

Use for additions, replacements, deletions, retiming, reordering, and retries. Preserve the approved intent while rebuilding affected dependencies.

## Active state

Load the saved project ledger when one exists. Separate accepted facts, proposed draft values, and the current request. Build one active brief from the latest explicit instructions; do not treat every historical sentence as still active.

## Operations

| Operation | Effect |
| --- | --- |
| ADD | Add a compatible requested detail; check whether it creates a conflict. |
| REPLACE | Retire the old value in the requested scope and adopt the new value. |
| DELETE | Remove the named event or attribute and instructions that depend exclusively on it. |
| REORDER | Retain active events but rebuild their order and all dependent timing. |
| RETIME | Replace the affected intervals consistently across action, camera, focus, and audio. |
| PRESERVE | Keep specified details unless a later explicit instruction supersedes them. |
| RESET | Rebuild only the named scope from the new request. |

User instructions always determine the requested scope. If changing one element makes an explicitly protected requirement impossible, ask one focused question or explain the conflict; do not silently change the protected requirement.

## Dependency cleanup

- Action removal: remove exclusive prop states, sound cues, focus events, reactions, and camera-follow segments. Preserve a prop if it still has another explicit role.
- Camera replacement: recompute start framing, route, speed, subject relation, focus, end framing, and the next beat's starting view. A locked camera cannot retain a former dolly route.
- Lighting replacement: remove stale color temperature, reflections, shadow direction, exposure, and lighting-continuity clauses.
- Music removal: remove score mood, tempo, and music-sync instructions; retain explicitly requested ambience and foley.
- Timing or order change: update all affected channels with the new ranges. Continuous coverage must equal the requested duration, without conflicting overlaps or unexplained gaps.
- Ending replacement: update pose, props, reveal state, camera arrival, audio decay, and next-shot handoff together.
- Reference reassignment: preserve exact source tags; remove obsolete inheritance rules and resolve remaining roles explicitly.

Do not revive retired directions as negative reminders. A deleted action must not reappear in a final constraint list, asset map, or retry note unless the user separately requires that exclusion.

## Final pass

1. Apply the requested operations to the active brief.
2. Remove superseded values and their exclusive dependencies.
3. Rebuild affected timing, spatial relationships, and handoff states.
4. Preserve unrelated approved values and check user-requested output language and format.
5. Return one independently usable prompt, or exactly the requested diagnosis/patch.
6. Save changes as proposed until approved; update accepted ledger state only with evidence of acceptance.

## Example

Earlier plan: approach, pick up a key, unlock a door, enter; the camera pushes toward the pickup and a metallic pickup sound occurs.

Revision: the door is already open, remove the key pickup, and keep the camera fixed.

Result: remove the pickup, unlocking, exclusive key/hand state, metallic pickup sound, key focus, and push-in. Stage approach and entry within the fixed view. Preserve the approved character, location, and duration. Rebuild the final pose and handoff without the retired key.
