import importlib.util
import io
import json
import os
from email.message import Message
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

ROOT = Path(__file__).resolve().parents[1]

def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT/'scripts'/f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

evidence = load('reference_evidence')
voice = load('elevenlabs_optional')

class VoiceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.out = Path(self.tmp.name)/'speech.mp3'

    def test_preview_never_calls_network(self):
        with patch.object(voice.request, 'urlopen', side_effect=AssertionError('network')):
            self.assertEqual(voice.synthesize('안녕', 'voice', self.out)['status'], 'preview_only')
        self.assertFalse(self.out.exists())

    def test_guards_and_missing_key(self):
        with patch.dict(os.environ, {}, clear=True):
            for rights, spending in [(False,False), (True,False), (False,True), (True,True)]:
                with self.assertRaises(ValueError):
                    voice.synthesize('Hello', 'v', self.out, execute=True, voice_rights=rights, spending=spending)
        self.assertFalse(self.out.exists())

    @unittest.skipUnless(shutil.which('ffmpeg'), 'FFmpeg required')
    def test_request_and_success_mock_only(self):
        audio = subprocess.run(['ffmpeg','-v','error','-f','lavfi','-i','sine=frequency=440',
                                '-t','0.1','-f','mp3','-'], check=True, capture_output=True).stdout
        response = io.BytesIO(audio)
        response.headers = Message(); response.headers['Content-Type'] = 'audio/mpeg'
        def opener(req, timeout):
            self.assertEqual(req.get_method(), 'POST')
            self.assertEqual(req.get_header('Xi-api-key'), 'test-secret')
            self.assertEqual(json.loads(req.data)['text'], '안녕')
            self.assertIn('voice%2Fid', req.full_url)
            return response
        with patch.dict(os.environ, {'ELEVENLABS_API_KEY':'test-secret'}):
            result = voice.synthesize('안녕', 'voice/id', self.out, execute=True, voice_rights=True, spending=True, opener=opener)
        self.assertEqual(result['status'], 'synthesized_not_reviewed')
        self.assertEqual(self.out.read_bytes(), audio)
        with self.assertRaises(ValueError): voice.synthesize('Hi', 'v', self.out)

    def test_http_failure_redacts_and_does_not_retry(self):
        calls=[]
        def opener(req, timeout):
            calls.append(req)
            raise HTTPError(req.full_url, 403, 'secret body', None, None)
        with patch.dict(os.environ, {'ELEVENLABS_API_KEY':'test-secret'}):
            with self.assertRaisesRegex(ValueError, 'HTTP 403') as caught:
                voice.synthesize('Hi', 'v', self.out, execute=True, voice_rights=True, spending=True, opener=opener)
        self.assertNotIn('secret', str(caught.exception)); self.assertEqual(len(calls),1)
        self.assertFalse(self.out.exists())

    @unittest.skipUnless(shutil.which('ffmpeg'), 'FFmpeg required')
    def test_mislabeled_audio_rejected(self):
        response=io.BytesIO(b'<html>not MP3</html>'); response.headers=Message(); response.headers['Content-Type']='audio/mpeg'
        with patch.dict(os.environ, {'ELEVENLABS_API_KEY':'test-secret'}):
            with self.assertRaisesRegex(ValueError, 'MP3 decoding'):
                voice.synthesize('Hi','v',self.out,execute=True,voice_rights=True,spending=True,opener=lambda *a,**k:response)
        self.assertFalse(self.out.exists())

    def test_non_audio_rejected(self):
        response=io.BytesIO(b'{}'); response.headers=Message(); response.headers['Content-Type']='application/json'
        with patch.dict(os.environ, {'ELEVENLABS_API_KEY':'test-secret'}):
            with self.assertRaises(ValueError):
                voice.synthesize('Hi','v',self.out,execute=True,voice_rights=True,spending=True,opener=lambda *a,**k:response)
        self.assertFalse(self.out.exists())

@unittest.skipUnless(shutil.which('ffmpeg') and shutil.which('ffprobe'), 'FFmpeg required')
class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        self.video=self.root/'sample with spaces.mp4'
        subprocess.run(['ffmpeg','-v','error','-f','lavfi','-i','testsrc2=size=160x120:rate=10',
                        '-f','lavfi','-i','sine=frequency=440:sample_rate=16000','-t','2',
                        '-c:v','mpeg4','-c:a','aac',str(self.video)],check=True)

    def test_audio_and_interval(self):
        result=evidence.extract(self.video,self.root/'evidence',.5,1.5,4)
        self.assertEqual(result['status'],'extracted_not_reviewed')
        self.assertEqual(result['semantic_analysis'],'not_executed')
        self.assertEqual(len(result['frames']),4)
        self.assertTrue((self.root/'evidence'/'inspection.wav').exists())
        self.assertEqual(result['frames'][0]['approx_source_seconds'],.5)

    def test_silent_and_no_overwrite(self):
        silent=self.root/'silent.mp4'
        subprocess.run(['ffmpeg','-v','error','-i',str(self.video),'-an','-c:v','copy',str(silent)],check=True)
        result=evidence.extract(silent,self.root/'silent-evidence')
        self.assertIsNone(result['audio'])
        with self.assertRaises(FileExistsError): evidence.extract(silent,self.root/'silent-evidence')

    def test_bad_ranges_and_missing_file(self):
        for start,end,fps in [(-1,1,1),(1,.5,1),(0,3,1),(0,1,0),(float('nan'),1,1),(0,float('inf'),1)]:
            with self.assertRaises(ValueError): evidence.extract(self.video,self.root/'bad',start,end,fps)
        self.assertFalse((self.root/'bad').exists())
        with self.assertRaises(ValueError): evidence.extract(self.root/'missing',self.root/'bad')

if __name__=='__main__': unittest.main()
