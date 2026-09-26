# Evaluation Protocol

Use this reference when the user asks for scoring, benchmarking, A/B comparison, proof of quality, or whether a prompt or generated result is production-ready.

## Purpose

Separate three different claims that are often confused:

1. the prompt is internally well specified;
2. the prompt is well matched to the selected model;
3. the generated video actually succeeds.

Do not claim generated-output validation when only prompt-level analysis has been performed.

## Automatic pre-generation gate

Mode A prompt lint is mandatory before every final generation prompt is delivered, even when the user does not explicitly request validation.

The internal delivery sequence is:

DRAFT → PROMPT LINT → REFERENCE REALITY CHECK → MODEL FEASIBILITY CHECK → COMPLEXITY REDUCTION WHEN NEEDED → FINAL REWRITE → OUTPUT

Do not expose or label the unreviewed first draft as generation-ready.

The automatic gate must catch and repair obvious issues such as:

- references named in the prompt that will not actually be supplied to the model;
- contradictory camera instructions;
- excessive one-take camera changes;
- impossible or unclear travel direction;
- too many simultaneous actions inside one beat;
- unsupported model-feature dependencies;
- duplicated instructions that compete for model attention;
- timing that cannot plausibly fit the requested duration;
- violation of an explicit user prompt-length limit.

If the draft fails the gate, revise it before delivery rather than waiting for the user to request a second QC pass.

## Evaluation modes

### Mode A — Prompt lint

Use before generation.

Check whether the prompt is executable, internally consistent, and resistant to common generation failures.

### Mode B — Generated-output review

Use after the user provides a generated clip.

Judge what actually appeared on screen rather than what the prompt intended.

### Mode C — A/B benchmark

Compare one of:

- plain user brief vs Luna AI Video Studio prompt
- earlier skill version vs current skill version
- two prompt variants on the same model
- two models using equivalent scene intent

### Mode D — Connected-sequence validation

Use for multi-clip work where continuity matters more than any single clip.

## Fair-test rules

For a meaningful A/B comparison, keep these fixed whenever possible:

- same scene brief
- same source references
- same video model and version
- same duration
- same aspect ratio
- same resolution tier
- same seed when the platform exposes one and the comparison requires it
- same number of generation attempts

If any of these differ, disclose the difference before drawing a strong conclusion.

Do not compare a heavily revised result against a first-pass baseline without reporting the attempt count.

## Mode A scorecard — Prompt lint

Score each category from 0 to 5.

0 = missing or contradictory
1 = severe weakness
2 = weak
3 = usable
4 = strong
5 = excellent

Evaluate:

- brief fidelity
- reference lock
- action clarity
- temporal order
- spatial staging
- camera executability
- performance direction
- dialogue feasibility
- sound planning
- motion and physical evidence
- continuity handoff
- reveal control
- ending state
- model compatibility
- failure prevention

### Prompt-lint hard fails

A prompt cannot be marked generation-ready if any of these remain unresolved:

- contradictory character count
- contradictory camera commands
- impossible or unclear spatial order
- required model feature is known unsupported
- duration cannot plausibly contain the requested actions or dialogue
- authoritative references conflict without assigned roles
- connected shot has no usable handoff state when continuity is required

### Prompt-ready threshold

Generation-ready requires:

- no hard fail
- average score of at least 4.2 / 5
- model compatibility score of at least 4 / 5
- action clarity score of at least 4 / 5

## Mode B scorecard — Generated output

Score from 0 to 5, where higher is always better:

- identity / reference fidelity
- character and prop count
- composition
- camera behavior
- spatial consistency
- action readability
- human or creature motion
- physical believability
- environmental response
- performance
- dialogue / lip-sync when relevant
- sound-image match when relevant
- reveal timing
- ending strength
- artifact cleanliness / absence of visible AI artifacts
- overall generation reliability

### Generated-output critical fails

A result cannot be marked production-ready when any critical requirement fails badly, including:

- wrong identity
- wrong character count
- broken continuity in a connected sequence
- requested primary action does not happen
- major spatial teleportation
- severe camera incoherence
- severe motion failure
- essential product or creature design is incorrect

### Single-clip production-ready threshold

Require:

- no critical fail
- average score of at least 4.2 / 5
- primary-action readability of at least 4 / 5

### Connected-sequence production-ready threshold

Require:

- no critical fail
- average score of at least 4.0 / 5
- continuity score of at least 4.0 / 5
- identity score of at least 4.0 / 5

## Mode C — A/B scoring

For each variant, report:

- prompt-lint score
- generated-output score when clips exist
- number of attempts
- critical fails
- repair passes needed

The stronger system is the one that reaches the target result with better fidelity and fewer severe failures, not the one with the longest prompt.

When generation cost matters, include attempts-to-acceptable-output as a practical metric.

## Mode D — Sequence continuity checks

For every transition from clip N to clip N+1, compare:

- identity
- hairstyle
- wardrobe
- footwear
- accessories
- prop and hand state
- screen direction
- movement direction
- subject velocity and movement phase when motion continues
- camera side, movement direction, and velocity when camera motion continues
- damage / dirt / wetness
- lighting direction
- object placement
- creature or product state
- environmental motion direction and intensity
- audio ambience, room tone, and continuing sound state when native or generated audio is used
- accepted resolution, aspect ratio, framing, and crop when frame handoff is used
- story state

When first-frame conditioning is part of the workflow, verify that the accepted prior final frame or nearest clean accepted frame was carried forward without an unexplained continuity reset.

When clips are stitched, inspect the boundary for duplicated visual frames, repeated motion beats, micro-stutter, abrupt audio discontinuity, or an unintended pause.

Record every unexplained reset.

## Reliability metrics

When enough attempts are available, track:

### First-pass success rate

accepted first generations / total benchmark scenes

### Repair efficiency

average number of repair passes before acceptance

### Continuity survival rate

connected transitions without unexplained reset / total connected transitions

### Critical-failure rate

generations containing at least one critical fail / total generations

Do not present these as statistically robust when the sample is too small. State the sample size.

## Validation claim policy

Use accurate labels:

- `Prompt-validated` means Mode A passed.
- `Output-reviewed` means an actual generated clip was inspected.
- `A/B tested` means comparable variants were generated and scored under the fair-test rules.
- `Production-validated` requires generated-output evidence across a meaningful scene set, not prompt analysis alone.

Never upgrade the label merely because the written instructions look strong.

## Report format

### EVAL REPORT
- mode:
- scene:
- model/version:
- duration/aspect ratio:
- attempts:
- average score:
- hard or critical fails:
- strongest areas:
- weakest areas:
- required repair:
- validation label:
- verdict:

Verdicts:

- Not ready
- Revise before generation
- Generation-ready
- Usable with repair
- Strong
- Production-ready

## A/B report

### A/B BENCHMARK
- baseline:
- candidate:
- fixed test conditions:
- baseline score:
- candidate score:
- baseline attempts:
- candidate attempts:
- critical failures:
- winner:
- reason:
- confidence / limitations:


## Behavior evidence and score limits

The numerical thresholds above are internal acceptance heuristics, not calibrated probabilities of generation success. Mark irrelevant categories N/A and exclude them from the average; report the scored category count. Do not score population-level reliability from one video. Report first-pass success and critical-failure rates only across a stated set of attempts.

Static checks confirm that files and required rules exist. They do not prove that an agent follows those rules. Use `../tests/behavior-cases.json` to collect actual agent responses, and grade each response against its case criteria. Do not use the criteria as part of the agent's request. Record case ID, skill revision, agent/model, actual response, pass/fail evidence, and remaining limitations. An automated contradiction lint may supplement this review, but cannot replace semantic grading.

A passing text-response exercise is prompt-level behavior evidence only. It cannot support Output-reviewed, A/B tested, or Production-validated labels without the required video evidence. CI checks file integrity and case coverage; independent behavioral runs and generated-video trials remain separate gates.
