"""Static routing/fixture integrity only; no model or media execution."""
import json
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
class ScriptGateTests(unittest.TestCase):
    def test_routes_and_state(self):
        for file in ('SKILL.md','references/evaluation-protocol.md','references/fia-theo-qc.md','references/production-ledger.md','references/revision-workflow.md'):
            self.assertIn('script-approval-gate.md', (ROOT/file).read_text())
        text=(ROOT/'references/script-approval-gate.md').read_text()
        for check in ('hook','causality','motivation','emotion','contact','paths','ownership','climax','payoff'):
            self.assertIn('| '+check+' |',text)
        for clause in ('three repair passes','script_revision','brief_revision','available-not-executed','UNVERIFIED','Never approve by exhaustion','never means user-approved'):
            self.assertIn(clause,text)
    def test_regression_requests(self):
        cases=json.loads((ROOT/'tests/fia-theo-behavior-cases.json').read_text())
        ids={c['id'] for c in cases}
        self.assertTrue(ids >= {'ft_ep39_theft','ft_ep39_hiss','ft_ep39_counterattack','ft_script_retry_block','ft_script_approval_preservation','ft_script_silent_override','ft_script_generation_handoff','ft_script_evidence_boundary'})
        self.assertEqual(len(ids),len(cases))
        self.assertTrue(all(len(c['criteria'])>=2 and c['request'].strip() for c in cases))
if __name__=='__main__': unittest.main(verbosity=2)
