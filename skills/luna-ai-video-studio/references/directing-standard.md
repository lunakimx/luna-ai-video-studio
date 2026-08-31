# Directing Standard

Use this reference when the request is complex, reference-sensitive, continuity-heavy, multi-shot, or the user asks for maximum precision.

## 1. Production detection

Infer or determine:

- live action, animation, mixed media, or another form
- genre and visual language
- scene purpose and intended audience feeling
- duration and aspect ratio
- character count
- environment, time, weather, and lighting behavior
- primary action, supporting action, and reaction
- dialogue, sound, and music needs
- camera language
- continuity and reference-fidelity demands
- ending moment
- likely generation failures

Do not force the user to fill a production template when the missing choices can be inferred professionally.

## 2. Reference lock

Protect visible and requested details that define continuity or identity:

- face and facial proportions
- hairstyle and color
- body proportions
- wardrobe, shoes, accessories, makeup
- props and hand state
- character count
- creature design and scale
- product design and materials
- environment and architecture
- color and lighting identity
- damage, dirt, wetness, aging, wear

If multiple references are supplied, assign each a job before combining them. Treat an explicitly designated exact character reference as authoritative for visible identity.

## 3. Genre behavior

### Horror

Favor withheld information, negative space, slow audience discovery, restrained acting, delayed reveals, local environmental sound, and controlled camera movement. Do not automatically use screaming, rapid cuts, trailer impacts, or full creature reveals.

### Comedy

Protect action readability, setup, pause, reaction, and aftermath. Do not bury the joke under camera movement or overacting.

### Drama

Give micro-expression, breath, silence, hesitation, and reaction enough screen time to register.

### Action

Maintain geography, momentum, contact, cause-and-effect, weight, and readable direction. Let camera motion support action rather than obscure it.

### Romance

Use gaze, interpersonal distance, gesture, timing, atmosphere, and controlled proximity changes.

### Music video

Respect musical phrasing, beat placement, performance energy, choreography readability, and image progression.

### Product film

Allow materials, surfaces, reflections, edges, logos when requested, and interaction details enough time to register. Preserve product proportions and construction.

### Documentary / found footage

Avoid overly polished cinematic behavior unless requested. Camera limitations and imperfections should feel physically motivated.

## 4. Time-beat design

Silently distribute the duration before writing the prompt.

A useful short-form rhythm may be:

- opening image registers
- setup develops
- main event arrives
- reaction becomes readable
- ending image holds long enough to land

Do not mechanically use equal time blocks. Let genre and action complexity determine timing.

Prevent two common failures:

1. The payoff happens immediately and the remaining clip becomes filler.
2. The setup consumes the clip and the payoff never becomes readable.

## 5. Single-shot vs multi-shot

Prefer a continuous shot when it protects identity, environment, spatial logic, or reference fidelity.

Use multiple shots only when each cut has a clear job and the selected model can handle the complexity without resetting the world.

Avoid random cinematic cutting inside short generations.

## 6. Spatial staging

Before camera movement, establish:

- foreground / midground / background
- subject side and screen direction
- distance between subjects
- camera side
- travel direction
- background reveal position
- important off-screen source
- what may enter or leave frame

Do not allow background threats, props, vehicles, or characters to teleport.

For a reveal behind a foreground character, preserve visual legibility for both.

## 7. Camera

Choose camera according to story, emotion, scale, movement, reveal timing, spatial clarity, reference fidelity, and generation reliability.

Possible approaches include locked-off, dolly, push-in, pull-back, forward tracking, backward tracking, lateral tracking, arc, orbit, handheld, shoulder follow, crane, pan, tilt, POV, FPV, overhead, low-angle tracking, high-angle tracking, over-the-shoulder, foreground reveal, and rack focus.

Define only what helps:

- shot size
- starting position
- height
- angle
- subject distance
- lens feel
- movement path
- speed
- relationship to subject motion
- focus behavior
- ending position

Prefer one clear primary camera move per shot. Never substitute vague phrases such as “dynamic cinematic camera movement” for physical direction.

## 8. Composition and focus

Use intentional subject placement, headroom, lead room, negative space, foreground obstruction, scale contrast, silhouette clarity, eyeline, horizon, reflections, windows, doorways, and depth.

Do not use extreme shallow depth of field when the viewer must read foreground acting and background action at the same time.

Use rack focus only when the focus shift carries information.

## 9. Performance

Direct visible actions:

- gaze and eye movement
- blinking
- breath
- lips, jaw, swallowing
- head and shoulder movement
- hands
- posture
- weight shift
- hesitation
- reaction delay
- walk/run rhythm
- stopping behavior
- object interaction

Avoid generic AI overacting. Close shots usually need smaller acting than wide shots.

Fear can be shown through shorter breath, tightened posture, delayed turning, jaw tension, eye control, hand tension, unfinished speech, or slowing movement.

## 10. Dialogue

Preserve exact dialogue supplied by the user unless asked to rewrite it.

When generating dialogue:

- make it sound spoken rather than written
- avoid exposition
- avoid describing visible action
- avoid translation-like phrasing
- leave room for pauses and breath
- keep lines short enough for the available clip
- reduce speech during physically demanding movement

For visible mouths and speech-capable models, favor short and pronounceable lines.

## 11. Sound

Treat sound as part of direction.

Choose among ambience, foley, action sound, environmental sound, dialogue, music, and silence.

Do not add music automatically.

Match sound perspective to camera distance. A close camera may reveal breath, fabric, mouth, and hand-object details. A wide camera should carry more room, street, crowd, wind, water, or environmental space.

Synchronize important sound events with their causes.

For massive nearby events, prefer plausible low-frequency environmental response such as structural resonance, glass vibration, water displacement, distant metal stress, or pressure response instead of an unrelated trailer hit.

## 12. Motion and physics

Movement must leave evidence in the world.

### Human movement

Feet contact surfaces, weight transfers, clothing and hair react, arms respond, breath may change, and background displacement must match travel.

### Vehicles

Use speed-dependent parallax, terrain movement, reflections, wheel/track behavior, and plausible vibration.

### Underwater

Use moving particles, depth parallax, light-particle interaction, debris response, water displacement, and coherent fabric/hair behavior. Avoid frozen water outside a moving viewpoint.

### Wind

Hair, fabric, foliage, dust, smoke, and loose objects should respond consistently.

### Touch

Hands should meet surfaces correctly. Object movement must follow the contact and weight transfer.

Prevent sliding feet, floating bodies, frozen backgrounds, incorrect parallax, impossible contact, disappearing props, inconsistent scale, or unexplained movement.

## 13. Continuity

For connected shots preserve:

- identity
- hairstyle
- wardrobe and footwear
- accessories and props
- character count
- hand state
- screen and movement direction
- damage, dirt, wetness
- lighting direction
- environment and object placement
- creature state
- story state

Carry the previous ending into the next opening when scenes connect directly.

## 14. Animation

Infer the intended animation language: 2D, anime, 3D, cel-shaded, stop-motion, clay, painterly, motion graphics, mixed media, or another style.

Match motion, acting, timing, exaggeration, camera behavior, physics, and secondary motion to that style.

Use anticipation, follow-through, squash and stretch, smear frames, impact frames, speed lines, limited animation, 2.5D parallax, or multiplane camera only when they fit.

## 15. Editing awareness

Every shot needs a job: hook, setup, orientation, escalation, reveal, reaction, detail, payoff, transition, or ending image.

Do not cut away before the action reads. Do not hold finished action for dead time unless the hold creates useful suspense, drama, discomfort, or comedy.

## 16. Text and graphic control

Unless requested, prevent random subtitles, captions, watermarks, interface overlays, gibberish signage, accidental logos, and floating typography.

If exact lettering is essential but the generator is unreliable at text, recommend adding it in post.

## 17. Scale and reveal

Communicate scale using familiar reference objects such as people, windows, doors, vehicles, buildings, furniture, or terrain.

For partial reveals, state what appears and what remains hidden. Do not let a partial eye, hand, silhouette, tentacle, or reflection become an unintended full creature or subject reveal.

## 18. Failure prevention checklist

Before output, check for:

- identity drift
- extra or missing characters
- missing or duplicated props
- wardrobe drift
- hand deformation
- weak movement
- frozen environment
- wrong scale
- spatial teleportation
- camera drift
- unwanted zoom
- reversed screen direction
- overacting
- unnatural or overlong dialogue
- weak lip-sync conditions
- audio-image mismatch
- too many simultaneous actions
- unsupported features
- contradictory instructions
- unwanted text or logos
- premature reveal
- incomplete ending
- continuity reset

Revise the prompt before sending it when clearer direction can prevent the failure.
