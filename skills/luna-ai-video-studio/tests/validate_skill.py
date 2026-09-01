from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
REFS = ROOT / "references"

errors: list[str] = []
checks = 0


def require(condition: bool, message: str) -> None:
    global checks
    checks += 1
    if not condition:
        errors.append(message)


def read(path: Path) -> str:
    require(path.exists(), f"Missing file: {path.relative_to(ROOT)}")
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


skill = read(SKILL)

# Agent Skill frontmatter
require(skill.startswith("---\n"), "SKILL.md must start with YAML frontmatter")
frontmatter_match = re.match(r"^---\n(.*?)\n---\n", skill, flags=re.S)
require(frontmatter_match is not None, "SKILL.md frontmatter is not closed correctly")
frontmatter = frontmatter_match.group(1) if frontmatter_match else ""
require(re.search(r"^name:\s*luna-ai-video-studio\s*$", frontmatter, flags=re.M) is not None,
        "Frontmatter name must be luna-ai-video-studio")
require(re.search(r"^description:\s*.+$", frontmatter, flags=re.M) is not None,
        "Frontmatter description is required")

required_references = [
    "directing-standard.md",
    "model-adaptation.md",
    "production-ledger.md",
    "retry-repair.md",
    "evaluation-protocol.md",
    "benchmark-scenes.md",
]

for filename in required_references:
    path = REFS / filename
    require(path.exists(), f"Missing required reference: references/{filename}")
    require(f"references/{filename}" in skill,
            f"SKILL.md does not route to references/{filename}")

required_skill_sections = [
    "## Production workflow",
    "## Reference fidelity",
    "## Camera direction",
    "## Sound",
    "## Motion and physical evidence",
    "## Continuity",
    "## Resolution and connected-shot handoff",
    "## Model adaptation",
    "## Retry and repair",
    "## Silent QA",
    "## Validation and benchmarking",
    "## Review mode",
    "## Revision rule",
]

for heading in required_skill_sections:
    require(heading in skill, f"Missing SKILL.md section: {heading}")

for phrase in [
    "preserve subject direction and apparent speed",
    "preserve ambience, room tone",
    "Never request 1920×1088 merely because the user asks for 1080p",
    "do not pretend to have reviewed moments",
    "When inspection is partial",
]:
    require(phrase in skill, f"SKILL.md missing continuity/review safeguard: {phrase}")

ledger = read(REFS / "production-ledger.md")
for phrase in [
    "## Handoff rule",
    "## Resolution handoff",
    "## Motion handoff",
    "## Audio continuity handoff",
    "## Frame rate and timebase handoff",
    "## Boundary-frame stitching",
    "## Update rule",
    "## Conflict rule",
    "final visible state",
    "first-frame reference image",
    "screen direction",
    "hand and prop state",
    "camera movement direction",
    "ambience and room tone",
    "Do not duplicate a transient sound",
    "do not make one-frame trimming automatic",
]:
    require(phrase in ledger, f"Production ledger missing required rule: {phrase}")

repair = read(REFS / "retry-repair.md")
for phrase in [
    "## Diagnostic pass",
    "## Common failure map",
    "### Pass 1 — Targeted patch",
    "### Pass 2 — Complexity reduction",
    "### Pass 3 — Model-safe rebuild",
    "Frozen environment",
    "Camera drift",
    "Premature reveal",
]:
    require(phrase in repair, f"Retry playbook missing required rule: {phrase}")

evaluation = read(REFS / "evaluation-protocol.md")
for phrase in [
    "### Mode A — Prompt lint",
    "### Mode B — Generated-output review",
    "### Mode C — A/B benchmark",
    "### Mode D — Connected-sequence validation",
    "Prompt-validated",
    "Output-reviewed",
    "A/B tested",
    "Production-validated",
    "First-pass success rate",
    "Critical-failure rate",
    "where higher is always better",
    "artifact cleanliness / absence of visible AI artifacts",
    "subject velocity and movement phase",
    "audio ambience, room tone",
    "duplicated visual frames",
]:
    require(phrase in evaluation, f"Evaluation protocol missing required rule: {phrase}")

benchmarks = read(REFS / "benchmark-scenes.md")
benchmark_ids = re.findall(r"^## Benchmark (\d{2}) —", benchmarks, flags=re.M)
require(len(benchmark_ids) == 12, f"Expected 12 benchmark scenes, found {len(benchmark_ids)}")
require(benchmark_ids == [f"{i:02d}" for i in range(1, 13)],
        f"Benchmark IDs must run 01-12 in order, found: {benchmark_ids}")

benchmark_coverage = [
    "Dialogue close-up",
    "Underwater suspense",
    "Comedy timing",
    "Premium product film",
    "Solo dance performance",
    "Creature partial reveal",
    "Action geography",
    "Wind and rain response",
    "Found-footage realism",
    "Connected two-clip continuity",
    "Stylized animation timing",
    "Vertical social hook",
]
for title in benchmark_coverage:
    require(title in benchmarks, f"Benchmark coverage missing: {title}")

for phrase in [
    "accepted actual final frame of Clip A",
    "first-frame conditioning when supported",
    "resolution / framing / crop continuity",
    "camera movement direction and apparent speed continuity",
    "native or generated audio continuity when present",
    "duplicated boundary frame creates a pause or micro-stutter",
    "1920×1088 is forced without model-specific support",
]:
    require(phrase in benchmarks, f"Connected continuity benchmark missing: {phrase}")

model_adaptation = read(REFS / "model-adaptation.md")
for phrase in [
    "## Capability verification gate",
    "Prefer official model documentation",
    "Never invent support for a feature",
    "## Connected-shot frame handoff",
    "## Resolution alignment and exceptions",
    "Never request 1920×1088 merely because the user asks for 1080p",
    "## Frame rate and timebase",
    "## Resolution decision order",
    "## Model-neutral fallback",
]:
    require(phrase in model_adaptation, f"Model adaptation missing safety rule: {phrase}")

directing = read(REFS / "directing-standard.md")
for phrase in [
    "## 4. Time-beat design",
    "## 6. Spatial staging",
    "## 7. Camera",
    "## 11. Sound",
    "## 12. Motion and physics",
    "## 13. Continuity",
    "## 18. Failure prevention checklist",
]:
    require(phrase in directing, f"Directing standard missing required coverage: {phrase}")

if errors:
    print(f"Luna AI Video Studio validation FAILED: {len(errors)} error(s), {checks} checks run")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print(f"Luna AI Video Studio validation PASSED: {checks} checks run")
print("Static validation label: Prompt-system integrity validated")
print("Note: generated-video quality still requires output benchmark runs per evaluation-protocol.md")
