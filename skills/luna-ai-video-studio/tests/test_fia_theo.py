"""Static rule and fixture checks. These do not run a model or inspect video."""
from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REFS = ROOT / "references"


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


class FiaTheoIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.skill = read("SKILL.md")
        cls.canon = json.loads(read("references/fia-theo-canon.json"))
        cls.mode = read("references/fia-theo-animation.md")
        cls.bible = read("references/fia-theo-bible.md")
        cls.performance = read("references/fia-theo-performance.md")
        cls.qc = read("references/fia-theo-qc.md")
        cls.cases = json.loads(read("tests/fia-theo-behavior-cases.json"))

    def test_main_routes_mode_once(self) -> None:
        self.assertEqual(self.skill.count("## Fia & Theo Animation Mode"), 1)
        self.assertIn("references/fia-theo-animation.md", self.skill)
        self.assertIn("fia-theo-qc.md", self.skill)
        self.assertIn("## Mandatory pre-generation QC", self.skill)
        self.assertIn("## Fantasy action specialization", self.skill)
        self.assertIn("## Action framing and impact tracking", self.skill)

    def test_reference_files_exist(self) -> None:
        for name in ("fia-theo-bible.md", "fia-theo-canon.json", "fia-theo-performance.md", "fia-theo-qc.md"):
            with self.subTest(name=name):
                self.assertIn(name, self.mode)
                self.assertTrue((REFS / name).is_file())
        for target in re.findall(r"`((?:\.\./)?[a-z0-9/-]+\.(?:md|json|py))`", self.mode + self.bible + self.performance + self.qc):
            with self.subTest(target=target):
                self.assertTrue((REFS / target).is_file(), target)

    def test_anatomical_sock(self) -> None:
        theo = self.canon["characters"]["theo"]
        self.assertEqual(theo["paws"]["right_forepaw"], "white sock")
        self.assertEqual(theo["white_sock_count"], 1)
        self.assertEqual(list(theo["paws"].values()).count("white sock"), 1)
        for paw in ("left_forepaw", "right_hindpaw", "left_hindpaw"):
            self.assertEqual(theo["paws"][paw], "cocoa brown")
        self.assertIn("anatomical", theo["paw_coordinate_system"])
        self.assertIn("Never horizontally flip Theo", self.bible)

    def test_identity_and_owned_accessories(self) -> None:
        chars = self.canon["characters"]
        self.assertEqual(set(chars), {"fia", "theo"})
        self.assertEqual(chars["fia"]["breed"], "Persian")
        self.assertEqual(chars["theo"]["breed"], "British Shorthair")
        self.assertIn("deep-teal house-shaped pendant", chars["theo"]["accessories"])
        self.assertIn("brass keyhole bell", chars["theo"]["accessories"])
        for char in chars.values():
            self.assertEqual(char["tail"]["count"], 1)
            self.assertIsNone(char["reference_asset"])
        self.assertNotEqual(chars["fia"]["eyes"], chars["theo"]["eyes"])

    def test_input_and_scope_guards(self) -> None:
        for phrase in ("There is no fixed image quota", "image approval is not video-generation approval", "not automatically a model input", "Never silently switch languages"):
            self.assertIn(phrase, self.mode)
        self.assertIn("latest explicit", self.mode.lower())
        self.assertEqual(self.canon["series_defaults"]["fantasy_combat"], "off unless the approved scene calls for it")

    def test_contact_and_motion_rules(self) -> None:
        for phrase in ("One actor and one responder", "Prop ownership and release", "A slip is an intentional", "a miss must not cause a hit reaction", "grooming"):
            self.assertIn(phrase.lower(), self.performance.lower())
        self.assertIn("0.3-0.8", self.performance)
        self.assertIn("Do not impose a universal", self.performance)

    def test_audio_override_and_evidence(self) -> None:
        self.assertFalse(self.canon["series_defaults"]["audio"]["human_voices"])
        for phrase in ("no-music", "human gasp", "after visible release", "waveform", "UNVERIFIED"):
            self.assertIn(phrase, self.performance + self.qc)

    def test_edit_and_validation_boundaries(self) -> None:
        for phrase in ("Never regenerate media", "Lanczos/bicubic", "not model behavior", "No paid generation", "actual response", "Do not count an authored expected answer"):
            self.assertIn(phrase, self.qc)
        self.assertIn("under 10,000 Unicode characters", self.mode)

    def test_behavior_fixture_coverage(self) -> None:
        required = {"ft_anatomical_turn", "ft_occluded_paw", "ft_motion_ready_image", "ft_single_groom", "ft_duo_crossing", "ft_fish_release", "ft_cat_audio", "ft_sequential_inputs", "ft_cast_exit", "ft_nonfantasy_scope", "ft_opal_source", "ft_edit_only"}
        ids = [case["id"] for case in self.cases]
        self.assertEqual(set(ids), required)
        self.assertEqual(len(ids), len(set(ids)))
        for case in self.cases:
            with self.subTest(case=case["id"]):
                self.assertIsInstance(case["request"], str)
                self.assertTrue(case["request"].strip())
                self.assertGreaterEqual(len(case["criteria"]), 2)
                self.assertTrue(all(isinstance(c, str) and c.strip() for c in case["criteria"]))
                self.assertNotIn("result", case)

    def test_ci_runs_extension_checks(self) -> None:
        workflow = (ROOT.parents[1] / ".github/workflows/validate-luna-ai-video-studio.yml").read_text(encoding="utf-8")
        self.assertIn("test_fia_theo.py", workflow)
        self.assertIn("validate_skill.py", workflow)
        self.assertIn("contents: read", workflow)


if __name__ == "__main__":
    unittest.main(verbosity=2)
