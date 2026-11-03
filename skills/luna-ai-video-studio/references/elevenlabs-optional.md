# Optional ElevenLabs voice

Default OFF. Analysis, prompt preparation and silent/native-audio production must work without it.
Reviewed 2026-11-02; consult current official docs before live integration:
- https://elevenlabs.io/docs/api-reference/authentication
- https://elevenlabs.io/docs/api-reference/text-to-speech/convert
- https://elevenlabs.io/docs/eleven-creative/voices/voice-cloning
- https://github.com/hypit-ai/hypit/tree/0762c6be56c0af43fff3cdbdb285e21414dd249b/packages/elevenlabs-speech

Hypit's `@hypit/elevenlabs-speech` exposes Voice Design (`eleven_ttv_v3`), producing an audio
reference through a selected Runtime Provider. It does NOT contain direct API authentication or
provide a general TTS/voice-cloning connection. Do not mislabel that package as an authorized account.

For optional direct TTS, use the bundled `scripts/elevenlabs_optional.py`. It creates a request
preview by default with no network and no credentials. Live execution is opt-in; use an existing
voice ID with verified rights. No cloning endpoint is implemented. Supply the secret only through
ELEVENLABS_API_KEY in the execution environment, never in a prompt, source file or command argument.

Required route: POST https://api.elevenlabs.io/v1/text-to-speech/{voice_id}, xi-api-key header,
JSON text/model_id, MP3 output. Configure Text to Speech permission; voice discovery needs Voices
read and model discovery needs Models read. Establish voice access, plan/credit limits, commercial
rights for the intended use and accepted spending scope before synthesis. Do not infer these from
API key presence. Use the account's authorized voice list/metadata when available; access errors
must remain blocked. Voice cloning needs explicit consent/rights and any provider verification;
never clone the reference speaker automatically. Professional cloning has separate account and
verification requirements; follow its current workflow if explicitly requested later.

Example from the skill directory (preview only):
```sh
python3 scripts/elevenlabs_optional.py --text-file dialogue.txt --voice-id APPROVED_VOICE --out narration.mp3
```
Add `--execute --voice-rights-confirmed --spending-authorized` only when the actual session evidence
supports those statements. They are execution guards, not proof of consent or API permissions.
The script sends one request without automatic retries (a timeout may still have been billed).
Live execution requires FFmpeg and decodes the MP3 response before saving.
It fails without publishing an audio artifact on HTTP/network/non-audio errors, and refuses overwrite.
No synthesis has been verified until a successful live response is inspected and heard.

Import the resulting audio as supplied media in the chosen video project. Measure its duration;
re-align changed speech and check pronunciation, speaker identity, pacing and lip sync. Do not
truncate dialogue to match old timestamps or claim word alignment from a TTS MP3 response.
