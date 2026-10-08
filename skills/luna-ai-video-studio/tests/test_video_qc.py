"""Synthetic metadata and real ffmpeg files; no user incident media is available."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts/video_qc.py'
spec = importlib.util.spec_from_file_location('video_qc', SCRIPT)
qc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(qc)


def fixture():
    return {'streams': [{'width': 1080, 'height': 1920, 'coded_width': 1088,
                         'coded_height': 1920, 'sample_aspect_ratio': '1:1',
                         'display_aspect_ratio': '9:16', 'avg_frame_rate': '30/1',
                         'r_frame_rate': '30/1', 'time_base': '1/30000'}],
            'frames': [{'width': 1080, 'height': 1920, 'sample_aspect_ratio': '1:1',
                        'best_effort_timestamp': n * 1000} for n in range(8)]}


class MetadataTests(unittest.TestCase):
    def inspect(self, data):
        return qc.inspect(data, (1080, 1920), qc.ratio('9:16'), qc.ratio('30'))

    def test_valid_and_coded_alignment(self):
        self.assertFalse(self.inspect(fixture())['errors'])

    def test_delivery_failures(self):
        for changes in ({'width': 1920, 'height': 1080}, {'width': 512},
                        {'sample_aspect_ratio': '2:1'}, {'sample_aspect_ratio': 'N/A'},
                        {'display_aspect_ratio': '16:9'}, {'avg_frame_rate': '0/0'},
                        {'avg_frame_rate': '30000/1001'}, {'r_frame_rate': '25/1'},
                        {'time_base': '0/0'}, {'tags': {'rotate': '90'}},
                        {'side_data_list': [{'side_data_type': 'Display Matrix', 'rotation': -90}]},
                        {'side_data_list': [{'side_data_type': 'Display Matrix'}]}):
            with self.subTest(changes=changes):
                data = fixture(); data['streams'][0].update(changes)
                self.assertTrue(self.inspect(data)['errors'])

    def test_missing_dar_is_derived(self):
        data = fixture(); del data['streams'][0]['display_aspect_ratio']
        result = self.inspect(data)
        self.assertFalse(result['errors']); self.assertTrue(result['warnings'])

    def test_rotation_effective_aspect_and_conflict(self):
        data = fixture(); data['streams'][0].update(width=1920, height=1080,
            display_aspect_ratio='16:9', tags={'rotate': '90'},
            side_data_list=[{'rotation': 270}])
        result = self.inspect(data)
        self.assertEqual(result['effective_dar'], '9/16')
        self.assertIn('Conflicting rotation metadata', result['errors'])

    def test_hidden_vfr_and_frame_changes(self):
        for key, value in [('best_effort_timestamp', 3500), ('width', 720),
                           ('sample_aspect_ratio', '2:1')]:
            data = fixture(); data['frames'][3][key] = value
            self.assertTrue(self.inspect(data)['errors'])
        for times in ([0, 1000, 1000], [0, 2000, 1000], [0, 1000]):
            data = fixture(); data['frames'] = data['frames'][:len(times)]
            for frame, time in zip(data['frames'], times):
                frame['best_effort_timestamp'] = time
            self.assertTrue(self.inspect(data)['errors'])

    def test_cumulative_drift_and_unknown_frame_sar(self):
        data = fixture()
        for n, frame in enumerate(data['frames']):
            frame['best_effort_timestamp'] = n * 1001
        self.assertTrue(self.inspect(data)['errors'])
        data = fixture(); del data['frames'][2]['sample_aspect_ratio']
        self.assertTrue(self.inspect(data)['errors'])

    def test_connection_comparison(self):
        a = self.inspect(fixture()); b = copy.deepcopy(a)
        b.update(width=720, avg_frame_rate='24/1', time_base='1/24000')
        errors, warnings = qc.compare(a, b)
        self.assertIn('Connected-clip mismatch: width', errors)
        self.assertIn('Connected-clip mismatch: avg_frame_rate', errors)
        self.assertTrue(warnings)


class RealFilesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.folder = Path(cls.tmp.name)
        for name, size, rate, vf in [('portrait', '1080x1920', '30', 'setsar=1'),
                ('landscape', '1920x1080', '30', 'setsar=1'),
                ('preview', '288x512', '30', 'setsar=1'),
                ('sar', '1080x1920', '30', 'setsar=2'),
                ('fps', '1080x1920', '24', 'setsar=1'),
                ('ntsc', '1080x1920', '30000/1001', 'setsar=1'),
                ('vfr', '1080x1920', '30', "select='not(eq(n,4))',setsar=1")]:
            subprocess.run(['ffmpeg', '-v', 'error', '-f', 'lavfi', '-i',
                f'color=c=blue:s={size}:r={rate}:d=0.4', '-vf', vf, '-vsync', '0',
                '-c:v', 'libx264', '-threads', '1', '-preset', 'ultrafast', '-pix_fmt', 'yuv420p',
                str(cls.folder / (name + '.mp4'))], check=True, capture_output=True)
        subprocess.run(['ffmpeg', '-v', 'error', '-i', str(cls.folder/'landscape.mp4'),
            '-c', 'copy', '-metadata:s:v:0', 'rotate=90', str(cls.folder/'rotated.mp4')],
            check=True, capture_output=True)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def run_qc(self, name, *extra):
        run = subprocess.run([sys.executable, str(SCRIPT), str(self.folder/name),
            '--size', '1080x1920', '--aspect', '9:16', '--fps', '30', *extra],
            capture_output=True, text=True)
        return run.returncode, json.loads(run.stdout)

    def test_valid_actual_file(self):
        code, report = self.run_qc('portrait.mp4')
        self.assertEqual(code, 0, report)
        self.assertEqual(report['visual_status'], 'UNVERIFIED')
        self.assertEqual(report['upscale_provenance'], 'UNVERIFIED')

    def test_bad_actual_files(self):
        for name in ('landscape', 'preview', 'sar', 'fps', 'rotated', 'vfr'):
            with self.subTest(name=name):
                code, report = self.run_qc(name + '.mp4')
                self.assertEqual(code, 1, report)

    def test_fractional_fps(self):
        code, report = self.run_qc('ntsc.mp4', '--fps', '30000/1001')
        self.assertEqual(code, 0, report)

    def test_adjacent_files(self):
        self.assertEqual(self.run_qc('portrait.mp4', '--previous', str(self.folder/'portrait.mp4'))[0], 0)
        self.assertEqual(self.run_qc('portrait.mp4', '--previous', str(self.folder/'fps.mp4'))[0], 1)

    def test_missing_corrupt_and_invalid_target(self):
        self.assertEqual(self.run_qc('missing.mp4')[0], 2)
        (self.folder/'corrupt.mp4').write_text('not media')
        self.assertEqual(self.run_qc('corrupt.mp4')[0], 2)
        self.assertEqual(self.run_qc('portrait.mp4', '--size', '1920x1080')[0], 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
