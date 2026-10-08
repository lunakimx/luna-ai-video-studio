#!/usr/bin/env python3
"""Read-only ffprobe delivery gate. No pixel repair or visual-quality claims."""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import subprocess
import sys


def ratio(value):
    try:
        result = Fraction(str(value).replace(':', '/'))
        return result if result > 0 else None
    except (ValueError, ZeroDivisionError):
        return None


def probe(path):
    # Local final assets only; do not accidentally inspect a preview URL.
    path = Path(path).resolve(strict=True)
    run = subprocess.run([
        'ffprobe', '-v', 'error', '-select_streams', 'V:0',
        '-show_streams', '-show_frames', '-show_entries',
        'stream:frame=best_effort_timestamp,width,height,sample_aspect_ratio',
        '-of', 'json', str(path)], capture_output=True, text=True, timeout=300)
    if run.returncode or run.stderr.strip():
        raise ValueError('ffprobe failed or reported decoding errors: ' + run.stderr.strip())
    return json.loads(run.stdout)


def inspect(data, size, aspect, fps):
    errors, warnings = [], []
    streams = data.get('streams', [])
    if len(streams) != 1:
        raise ValueError('Expected one selected non-cover video stream')
    s = streams[0]
    w, h = int(s.get('width', 0)), int(s.get('height', 0))
    if w <= 0 or h <= 0:
        raise ValueError('Missing/invalid decoded dimensions')
    sar = ratio(s.get('sample_aspect_ratio'))
    dar = ratio(s.get('display_aspect_ratio'))
    calculated = Fraction(w, h) * sar if sar else None
    if sar != 1:
        errors.append('SAR must be known and 1:1 for this delivery gate')
    if dar is None:
        warnings.append('DAR absent/unknown; computed from width, height and SAR when available')
    elif calculated != dar:
        errors.append('Declared DAR disagrees with dimensions and SAR')
    rotations = []
    for side in s.get('side_data_list', []):
        if 'rotation' in side:
            rotations.append(Fraction(str(side['rotation'])) % 360)
        elif side.get('side_data_type') == 'Display Matrix':
            errors.append('Display matrix has no readable rotation')
    if 'rotate' in s.get('tags', {}):
        rotations.append(Fraction(str(s['tags']['rotate'])) % 360)
    rotation = rotations[0] if rotations else Fraction(0)
    if len(set(rotations)) > 1:
        errors.append('Conflicting rotation metadata')
    if rotation != 0:
        errors.append('Nonzero rotation: normalize orientation before delivery and recheck')
    effective = calculated
    if rotation in (90, 270) and calculated:
        effective = 1 / calculated
    elif rotation not in (0, 180):
        effective = None
    if (w, h) != size:
        errors.append(f'Pixel size mismatch: expected {size[0]}x{size[1]}')
    if effective != aspect:
        errors.append('Effective display aspect mismatch or unknown')
    avg, nominal = ratio(s.get('avg_frame_rate')), ratio(s.get('r_frame_rate'))
    tb = ratio(s.get('time_base'))
    if avg != fps or nominal != fps:
        errors.append('Frame-rate mismatch/unknown (avg_frame_rate or r_frame_rate)')
    if tb is None:
        errors.append('Missing/invalid time_base')
    frames = data.get('frames', [])
    times = []
    for f in frames:
        if (f.get('width'), f.get('height')) != (w, h):
            errors.append('Frame dimensions change within clip')
        fsar = ratio(f.get('sample_aspect_ratio'))
        if fsar != sar:
            errors.append('Frame SAR changes or is unknown within clip')
        try:
            times.append(int(f['best_effort_timestamp']))
        except (KeyError, ValueError, TypeError):
            errors.append('Missing frame timestamp')
    # Inspect all decoded frame PTS; avg == nominal alone cannot prove CFR.
    if len(times) < 3 or len(times) != len(frames) or tb is None:
        errors.append('Insufficient decoded timestamps to verify cadence')
    else:
        period = 1 / fps
        # Allow timestamp quantization by one tick, never a broad FPS tolerance.
        if tb > period / 10:
            errors.append('Timebase too coarse to verify cadence')
        if any(abs((t - times[0]) * tb - n * period) > tb
               for n, t in enumerate(times)):
            errors.append('Cumulative timestamp drift from accepted FPS')
        for a, b in zip(times, times[1:]):
            if b <= a or abs((b - a) * tb - period) > tb:
                errors.append('Variable cadence, timestamp gap, or non-monotonic PTS')
                break
    return {
        'width': w, 'height': h,
        'coded_width': s.get('coded_width'), 'coded_height': s.get('coded_height'),
        'sample_aspect_ratio': s.get('sample_aspect_ratio'),
        'display_aspect_ratio': s.get('display_aspect_ratio'),
        'calculated_dar': str(calculated), 'effective_dar': str(effective),
        'rotation_degrees': str(rotation),
        'rotation_metadata': {'tags': s.get('tags', {}), 'side_data_list': s.get('side_data_list', [])},
        'avg_frame_rate': s.get('avg_frame_rate'), 'r_frame_rate': s.get('r_frame_rate'),
        'time_base': s.get('time_base'), 'decoded_frames': len(frames),
        'errors': list(dict.fromkeys(errors)), 'warnings': warnings,
    }


def compare(current, previous):
    errors, warnings = [], []
    for key in ('width', 'height', 'calculated_dar', 'effective_dar', 'rotation_degrees'):
        if current[key] != previous[key]:
            errors.append('Connected-clip mismatch: ' + key)
    for key in ('sample_aspect_ratio', 'avg_frame_rate', 'r_frame_rate'):
        if ratio(current[key]) != ratio(previous[key]):
            errors.append('Connected-clip mismatch: ' + key)
    if ratio(current['time_base']) != ratio(previous['time_base']):
        warnings.append('Different timebases: conform in editor; do not assume stream-copy concat is safe')
    return errors, warnings


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('video')
    p.add_argument('--size', required=True, help='Explicit accepted width x height, e.g. 1080x1920')
    p.add_argument('--aspect', required=True, help='Explicit display aspect, e.g. 9:16')
    p.add_argument('--fps', required=True, help='Exact accepted rational, e.g. 30000/1001')
    p.add_argument('--previous', action='append', default=[], help='Each adjacent clip; repeat as needed')
    args = p.parse_args(argv)
    report = {'metadata_status': 'ERROR', 'visual_status': 'UNVERIFIED',
              'upscale_provenance': 'UNVERIFIED', 'files': [], 'errors': [], 'warnings': []}
    try:
        size = tuple(int(n) for n in args.size.lower().split('x'))
        aspect, fps = ratio(args.aspect), ratio(args.fps)
        if len(size) != 2 or min(size) <= 0 or not aspect or not fps:
            raise ValueError('Invalid size, aspect, or fps')
        if Fraction(*size) != aspect:
            raise ValueError('Target size must match target aspect with square pixels')
        for path in [args.video] + args.previous:
            item = inspect(probe(path), size, aspect, fps)
            item['file'] = str(Path(path).resolve())
            report['files'].append(item)
            report['errors'].extend(f'{path}: {e}' for e in item['errors'])
            report['warnings'].extend(f'{path}: {w}' for w in item['warnings'])
        for previous in report['files'][1:]:
            errors, warnings = compare(report['files'][0], previous)
            report['errors'].extend(errors)
            report['warnings'].extend(warnings)
        report['metadata_status'] = 'FAIL' if report['errors'] else 'PASS'
        code = 1 if report['errors'] else 0
    except (OSError, ValueError, ZeroDivisionError, TypeError, KeyError, subprocess.SubprocessError) as exc:
        report['errors'].append(str(exc))
        code = 2
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return code


if __name__ == '__main__':
    sys.exit(main())
