#!/usr/bin/env python3
"""Local evidence extraction, never semantic analysis. Requires ffmpeg/ffprobe."""
import argparse
import json
import math
from pathlib import Path
import subprocess


def run(args):
    return subprocess.run(args, check=True, capture_output=True, text=True).stdout


def extract(source, out, start=0.0, end=None, fps=1.0):
    source, out = Path(source).resolve(), Path(out).resolve()
    if not source.is_file():
        raise ValueError('Input must be an existing local file')
    if not math.isfinite(start) or not math.isfinite(fps) or start < 0 or not 0 < fps <= 60:
        raise ValueError('Use finite start >= 0 and 0 < fps <= 60')
    data = json.loads(run(['ffprobe', '-v', 'error', '-show_format', '-show_streams', '-of', 'json', str(source)]))
    if not any(s['codec_type'] == 'video' for s in data['streams']):
        raise ValueError('Input has no video stream')
    duration = float(data['format']['duration'])
    end = duration if end is None else end
    if not math.isfinite(duration) or not math.isfinite(end) or not 0 <= start < end <= duration:
        raise ValueError('Interval must be inside the video duration')
    if (end - start) * fps > 600:
        raise ValueError('Limit extraction to 600 samples; split into intervals')
    out.mkdir(parents=True, exist_ok=False)
    manifest = {'source': str(source), 'metadata': data, 'interval': [start, end],
                'sample_fps': fps, 'status': 'extracting', 'semantic_analysis': 'not_executed',
                'timestamp_note': 'Resampled overview; sample positions are approximate source seconds. Not original-frame PTS.',
                'audio': None}
    report = out / 'evidence.json'
    report.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    try:
        base = ['ffmpeg', '-v', 'error', '-nostdin', '-i', str(source), '-ss', str(start), '-t', str(end-start)]
        run(base + ['-map', '0:v:0', '-vf', f'fps={fps},scale=640:-2', '-frames:v', '600', str(out / 'frame_%05d.jpg')])
        manifest['frames'] = [{'path': p.name, 'approx_source_seconds': start + i / fps}
                              for i, p in enumerate(sorted(out.glob('frame_*.jpg')))]
        if not manifest['frames']:
            raise ValueError('No frames extracted; enlarge interval')
        if any(s['codec_type'] == 'audio' for s in data['streams']):
            run(base + ['-map', '0:a:0', '-vn', '-ac', '1', '-ar', '16000', str(out / 'inspection.wav')])
            manifest['audio'] = 'inspection.wav'
        manifest['status'] = 'extracted_not_reviewed'
    except Exception:
        manifest['status'] = 'failed_partial_output'
        raise
    finally:
        report.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    return manifest


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('source'); p.add_argument('--out', required=True)
    p.add_argument('--start', type=float, default=0); p.add_argument('--end', type=float)
    p.add_argument('--fps', type=float, default=1)
    a = p.parse_args()
    try:
        result = extract(a.source, a.out, a.start, a.end, a.fps)
    except (ValueError, OSError, subprocess.SubprocessError, KeyError) as exc:
        p.exit(1, f'Extraction failed ({type(exc).__name__}); input/output and dependencies need checking.\n')
    print(json.dumps({'status': result['status'], 'frames': len(result['frames']), 'audio': result['audio']}))


if __name__ == '__main__':
    main()
