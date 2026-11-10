"""Run the demonstration files as subprocesses to verify their public outputs."""
import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


class ExampleTests(unittest.TestCase):
    def test_examples(self):
        for name, expected in (
            ("eop", "EOP result: 42"),
            ("peop", "PEOP result: [42, 200]"),
            ("reop", "REOP result: 42"),
            ("preeop", "PREEOP result: [42, 200]"),
        ):
            with self.subTest(name=name):
                proc = subprocess.run(
                    [sys.executable, str(ROOT / "examples" / f"{name}.py")],
                    text=True, capture_output=True, timeout=10, check=True,
                )
                self.assertIn(expected, proc.stdout)


if __name__ == "__main__":
    unittest.main()
