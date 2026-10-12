import json, os, pathlib, subprocess, sys, tempfile, unittest
from clock_quorum_window.core import run

CASES = [({'sources': [{'id': 'a', 'lower': 0, 'upper': 10}], 'quorum': 1}, {'windows': [[0, 10]], 'ambiguous': False}), ({'sources': [{'id': 'a', 'lower': 0, 'upper': 4}, {'id': 'b', 'lower': 4, 'upper': 8}], 'quorum': 2}, {'windows': [[4, 4]]}), ({'sources': [{'id': 'a', 'lower': 0, 'upper': 1}, {'id': 'b', 'lower': 2, 'upper': 3}], 'quorum': 2}, {'windows': []}), ({'sources': [{'id': 'a', 'lower': 0, 'upper': 10}, {'id': 'b', 'lower': 2, 'upper': 4}, {'id': 'c', 'lower': 6, 'upper': 8}], 'quorum': 2}, {'windows': [[2, 4], [6, 8]], 'ambiguous': True}), ({'sources': [{'id': 'a', 'lower': -5, 'upper': 5}, {'id': 'b', 'lower': -2, 'upper': 2}], 'quorum': 2}, {'windows': [[-2, 2]]}), ({'sources': [{'id': 'a', 'lower': 0, 'upper': 0}], 'quorum': 1}, {'windows': [[0, 0]]}), ({'sources': [{'id': 'a', 'lower': 0, 'upper': 2}, {'id': 'b', 'lower': 2, 'upper': 3}], 'quorum': 1}, {'windows': [[0, 3]]}), ({'sources': [{'id': 'a', 'lower': 2, 'upper': 1}], 'quorum': 1}, 'error'), ({'sources': [{'id': 'a', 'lower': 0, 'upper': 1}, {'id': 'a', 'lower': 0, 'upper': 1}], 'quorum': 1}, 'error'), ({'sources': [], 'quorum': 1}, 'error'), ({'sources': [{'id': 'a', 'lower': 0, 'upper': 1}], 'quorum': True}, 'error'), ({'sources': [{'id': 'a', 'lower': False, 'upper': 1}], 'quorum': 1}, 'error')]

class ContractTests(unittest.TestCase):
    def test_cli_demo(self):
        r=subprocess.run([sys.executable,"-c","from clock_quorum_window.cli import main; raise SystemExit(main())","example.json"],text=True,capture_output=True)
        self.assertEqual(r.returncode,0,r.stderr)
        self.assertIsInstance(json.loads(r.stdout),dict)

    def test_cli_malformed(self):
        with tempfile.TemporaryDirectory() as d:
            path=pathlib.Path(d)/"bad.json";path.write_text("[broken")
            r=subprocess.run([sys.executable,"-c","from clock_quorum_window.cli import main; raise SystemExit(main())",str(path)],text=True,capture_output=True)
            self.assertEqual(r.returncode,2)
            self.assertEqual(r.stdout,"")
            self.assertIn("input error",r.stderr)

def make_case(data,expected):
    def test(self):
        before=json.dumps(data,sort_keys=True)
        if expected=="error":
            with self.assertRaises(ValueError): run(data)
        else:
            result=run(data)
            if expected=="opaque":
                self.assertEqual(set(result["paths"]),{"d","d/new","other"})
                self.assertEqual(result["whiteouts"][0]["removed"],["d/a"])
            elif expected=="order":
                self.assertEqual([r["start"] for r in result["requests"]],[50,0])
                self.assertEqual(result["coverage"],[[0,9],[50,59]])
            else:
                for key,value in expected.items(): self.assertEqual(result[key],value)
        self.assertEqual(json.dumps(data,sort_keys=True),before,"input mutated")
    return test
for i,(data,expected) in enumerate(CASES):
    setattr(ContractTests,"test_contract_%02d"%i,make_case(data,expected))

if __name__=="__main__": unittest.main()
