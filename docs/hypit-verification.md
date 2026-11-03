# Hypit integration verification

The reference workflow preserves existing Luna character, physics, hook and pre-generation QC rules.
It covers media intake, source evidence, action/camera/text/B-roll/VFX/audio timelines, target mapping,
and complete reconstruction prompts. Evidence extraction does not perform semantic analysis.

## Executed

On 2026-11-03, restored the saved integration onto current GitHub main:
- Skill integrity validation: 164 checks passed.
- Python unittest discovery: 19 tests passed, including 9 integration tests.
- Integration tests use actual FFmpeg for audio/silent media extraction and MP3 decoding.
- Voice HTTP responses are mocked; offline default, authorization guards, errors and mislabeled
  MP3 payload rejection are covered.

On 2026-11-02, the earlier remote Linux session installed @hypit/hypit 0.3.1 with Node 24.22.1.
The executable reported version 0.3.1, probed a synthetic 2-second 320x240 10fps clip with audio,
and extracted original-frame grids. Project paths resolved after setting hypit.project=true;
no Runtime Profile was selected. That temporary installation was not recovered after workspace
maintenance and is not claimed as currently installed.

## Unverified / not executed

User Windows installation; separate Hypit skill installation in ChatGPT; live reference semantic
analysis; transcription/alignment; ElevenLabs account scopes, voice rights, quota or real TTS;
Hypit SVML check/build/render; generated-video/audio QC. No credentials or paid jobs were used.
Remote CI status must be checked separately.

## Reproduce

With Python 3 and FFmpeg/ffprobe available:

```sh
python skills/luna-ai-video-studio/tests/validate_skill.py
python -m unittest discover -s skills/luna-ai-video-studio/tests -v
```

See references/hypit-setup.md and references/elevenlabs-optional.md within the skill for installation
and optional voice usage. ElevenLabs remains off by default; live use requires actual session
spending authority and verified voice rights. Command flags do not establish those facts.
