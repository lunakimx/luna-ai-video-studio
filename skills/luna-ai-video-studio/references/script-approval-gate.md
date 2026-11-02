# Script approval gate

Run Mode S before advancing a new or revised story into image composition or generation. This is semantic script review, separate from Mode A final-prompt lint and Mode B output review. For prompt-only work review the inferred beats internally; do not force extra deliverables. For image-only work review the relevant supplied beat without inventing an episode. Diagnosis-only and edit-only requests remain within scope.

## Review record

Read the current project ledger and latest instructions first. Bind the review to an exact script revision and active-brief revision (or content hashes), and list the applicable user requirements. For each timed beat record: trigger, actor and motive/knowledge, action and target, visible emotional response, contact/miss and force response, each character's start/path/end, prop owner/grip/release/landing, and resulting state. Use landmarks and anatomical directions where screen coordinates change. Record concise evidence, not hidden deliberation.

## Nine mandatory checks

| ID | Check | Evidence required in the script |
| --- | --- | --- |
| hook | First second | A legible causal event within 0–1 seconds under a viral brief; honor an explicit calm opening. |
| causality | Cause and effect | Trigger precedes action and visible consequence; no unmotivated reset. |
| motivation | Character motive | Who wants what, who sees the trigger, and why each action follows; intentional mystery may be explicitly bounded. |
| emotion | Emotional response | Visible ears, gaze, posture, recoil or pursuit after the trigger, plus requested feline vocal timing; adjectives alone do not pass. |
| contact | Attack/contact physics | Initiator, target, approach, actual contact or miss, force direction, target response and recovery; a miss cannot propel a target. |
| paths | Character travel | Separate start, route, turn and end for each actor; reachable distance, collision/landing room and stable camera-side logic. |
| ownership | Prop ownership | One tracked prop: owner before/after, grip, forced or voluntary release, trajectory and landing; no duplication or unexplained transfer. |
| climax | Climax timing | Explicit timed decisive beat, enough time for anticipation/contact/reaction and recovery; honor an agreed timestamp, never impose a universal 10-second climax. |
| payoff | Ending reward | A visible resolution, reversal or relational reward caused by earlier action; no unrelated new cast or magic. |

Assign PASS, REVISE, UNVERIFIED or N/A to every check with a beat/time citation and short evidence. N/A requires a brief-based reason (e.g. no contact or explicit silent audio); do not waive an explicit requirement. All applicable checks must PASS, and every active mandatory user requirement must have evidence. Any REVISE or UNVERIFIED blocks Script-validated regardless of average scores. The Mode A 4.2/5 threshold cannot approve a script.

## Repair loop and transitions

DRAFT -> SCRIPT REVIEW -> REVISE -> SCRIPT REVIEW -> SCRIPT PASS -> MINIMUM IMAGE PLAN -> AUTHORIZED IMAGE GENERATION -> IMAGE QA -> FINAL PROMPT QC -> AUTHORIZED VIDEO GENERATION -> OUTPUT REVIEW.

On failure, repair the smallest responsible beat automatically and recheck all nine checks and dependent timing, routes, ownership and ending. Keep successful beats and unrelated locks. Attempt up to three repair passes per run; if contradictions remain, information is unavailable, or a protected decision must change, record BLOCKED with the exact unresolved item and ask only for that missing decision/input. Never approve by exhaustion or lower the bar to proceed. A review-only request reports repairs without applying them.

Store factual gate records under a separate ledger `qc.script_reviews` list: script_revision, brief_revision, checks (id/status/evidence), requirements (requirement/evidence/status), repair_pass, verdict, and evidence_level=`script-text`. A PASS permits planning only for those exact revisions. A changed story, timing, requirement or reference role marks dependent QC stale and requires re-review before further generation. Retain historical approvals and accepted assets; do not overwrite `accepted`, invent user approval, or mark existing media rejected solely because this new gate was added. Previously approved scripts without a current review receive a non-destructive review before new downstream work. Keep proposed repairs distinct from accepted state; internal Script-validated never means user-approved.

If the user has delegated script self-review and image creation, proceed after PASS without asking for the same permission again. A pending explicit user checkpoint still blocks its dependent action. Script-only/prompt-only/image-plan-only, no-regeneration, budget and provider limits remain binding. Script approval does not authorize video generation.

## EP.39 regression contract

Use these checks only for matching snack-theft/retaliation scenes, not every episode. Treat the reported failures as user reports, not inspected video evidence.

- Theft: the rival initiates the snatch while Fia retains/protects the snack; show loss of grip caused by the rival, then the new owner. Fia extending/releasing it to the rival reads as a gift and fails a theft brief.
- Fia: after noticing the loss, direct flattened ears, a tense recoil or forward defensive posture and the requested hiss toward the thief. Do not assign an open-mouth hiss while her mouth still grips the snack. An explicit later silent request removes audible hissing but preserves visible reaction.
- Theo: show his recognition, motivated approach and requested paw strike OR hip bump, actual contact, rival displacement and Theo's recovery. Staring, an offscreen implied strike or a miss with a flying target fails a requested physical retaliation. Do not require both attacks.
- Track the snack through the retaliation and finish with the approved recovery/relationship reward. Do not fix missing contact by adding an unapproved power or extra attacker.

## Image execution handoff

After current SCRIPT PASS, inventory existing approved assets before designing new images. Choose the minimum useful set; zero new images is valid when inputs already suffice. For each necessary image record beat, purpose, available reference IDs and roles, locked identity, motion-ready pose, prop owner, usable movement/contact space, and image QA criteria. Do not generate a fixed storyboard grid by default.

Discover the current tool registry and read the installed imagegen skill when actual generation is authorized. Prefer the available built-in image generation tool (currently exposed in some hosts as `image_gen.imagegen` / `image_gen__imagegen`); never assume the name or schema is portable. In the current schema pass `prompt`, `transparent_background`, and for references either `referenced_image_paths` or `num_last_images_to_include`, never both. Inspect local references before editing. If references cannot be resolved, block identity-dependent generation rather than invent inputs. Do not fabricate API keys, tool arguments or job IDs, install a fallback, or switch providers without authorization.

Recheck revision validity and execution scope immediately before each call. Record tool availability separately from invocation, returned artifact and inspection. Tool discovery is `available-not-executed`; a queued job is not an image; a returned image is not automatically Image-QA PASS. Inspect the actual artifact for identity, anatomy, pose, ownership, space and opening compatibility. Missing inspection remains UNVERIFIED and blocks video readiness. Image failure triggers targeted image repair; a story repair returns to Mode S. Preserve prior accepted assets and obey retry/cost limits. If no usable tool exists, deliver the approved minimum image briefs and state generation is blocked.

A static fixture check, a text behavior exercise, a successful image tool call and reviewed video are four different evidence levels. Never claim generated motion, feline audio, contact or production quality was verified from script review or a still image.
