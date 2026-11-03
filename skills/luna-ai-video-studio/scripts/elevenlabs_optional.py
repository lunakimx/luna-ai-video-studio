#!/usr/bin/env python3
"""Optional direct ElevenLabs TTS; defaults to a credential-free, offline preview."""
import argparse
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from urllib import request, error, parse


def synthesize(text, voice_id, output, model='eleven_multilingual_v2', execute=False,
               voice_rights=False, spending=False, opener=None):
    if not text.strip() or not voice_id.strip() or not model.strip():
        raise ValueError('Nonempty text, voice ID and model required')
    output = Path(output)
    if output.exists():
        raise ValueError('Output exists; choose a new version')
    if output.suffix.lower() != '.mp3':
        raise ValueError('Output must use .mp3')
    url = 'https://api.elevenlabs.io/v1/text-to-speech/' + parse.quote(voice_id, safe='') + '?output_format=mp3_44100_128'
    body = {'text': text, 'model_id': model}
    if not execute:
        return {'status': 'preview_only', 'endpoint': url, 'model': model, 'characters': len(text),
                'permissions': 'not_checked', 'synthesis': 'not_executed'}
    if not voice_rights or not spending:
        raise ValueError('Live synthesis requires established voice rights and spending authority')
    key = os.environ.get('ELEVENLABS_API_KEY')
    if not key:
        raise ValueError('ELEVENLABS_API_KEY is not configured')
    if not output.parent.is_dir():
        raise ValueError('Output parent directory must exist')
    if not shutil.which('ffmpeg'):
        raise ValueError('FFmpeg is required to validate live audio before saving')
    req = request.Request(url, data=json.dumps(body).encode(), headers={
        'xi-api-key': key, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg'}, method='POST')
    try:
        with (opener or request.urlopen)(req, timeout=90) as response:
            if response.headers.get_content_type() not in ('audio/mpeg', 'audio/mp3'):
                raise ValueError('Provider returned non-MP3 content')
            audio = response.read()
    except error.HTTPError as exc:
        raise ValueError(f'Provider HTTP {exc.code}; verify permissions, voice access and quota. No automatic retry.') from None
    except (error.URLError, OSError):
        raise ValueError('Provider connection failed; billing status unknown. No automatic retry.') from None
    if not audio:
        raise ValueError('Provider returned empty audio')
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(audio)
        result = subprocess.run(['ffmpeg', '-v', 'error', '-xerror', '-nostdin', '-f', 'mp3',
                                 '-i', str(temporary), '-map', '0:a:0', '-f', 'null', '-'],
                                capture_output=True, timeout=90)
        if result.returncode:
            raise ValueError('Provider payload failed MP3 decoding; no output published')
        with output.open('xb') as handle:
            handle.write(audio)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    return {'status': 'synthesized_not_reviewed', 'output': str(output), 'bytes': len(audio)}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--text-file', type=Path, required=True); p.add_argument('--voice-id', required=True)
    p.add_argument('--out', required=True); p.add_argument('--model', default='eleven_multilingual_v2')
    p.add_argument('--execute', action='store_true'); p.add_argument('--voice-rights-confirmed', action='store_true')
    p.add_argument('--spending-authorized', action='store_true')
    a = p.parse_args()
    try:
        result = synthesize(a.text_file.read_text(encoding='utf-8'), a.voice_id, a.out, a.model,
                            a.execute, a.voice_rights_confirmed, a.spending_authorized)
    except (ValueError, OSError, subprocess.SubprocessError) as exc:
        p.exit(1, f'{exc}\n')
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()
