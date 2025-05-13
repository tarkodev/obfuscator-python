#!/usr/bin/env python
"""
End-to-end benchmark of the obfuscation/de-obfuscation pipeline.

This test script accepts optional CLI parameters. On startup, it allows passing:
  • --examples-dir: directory containing input scripts
  • --output-dir: directory to write obfuscated and deobfuscated scripts
  • --models: space-separated list of GPT models
  • --model: (optional) select model directly
  • --no-exec: skip execution comparison

If --model is not provided or invalid, the user is prompted interactively to choose from --models.
Defaults:
  examples-dir = "example"
  output-dir = "example"
  models = ["gpt-4o", "o1-mini"]
  bases  = ["palindrom", "prime", "fibonacci"]

Key features:
  • Dynamic model list and selection
  • Configurable input/output folders
  • Measures times for:
    1) local obfuscation,
    2) GPT de-obfuscation,
    3) execution of original, obfuscated, deobfuscated scripts.
  • Final summary table with detailed timings.
  • Writes the summary to a file named `test-<model>.txt` in the output directory.
  • Returns non-zero exit code on any discrepancy.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import List

# Optional colour support for step outputs
try:
    from colorama import Fore, Style, init as colorama_init

    colorama_init()
    OK = Fore.GREEN + "✔" + Style.RESET_ALL
    FAIL = Fore.RED + "✘" + Style.RESET_ALL
    SECTION = Fore.CYAN + Style.BRIGHT
    RESET = Style.RESET_ALL
except ImportError:
    OK = "OK"
    FAIL = "FAIL"
    SECTION = ""
    RESET = ""


def _c(text: str) -> str:
    """Return coloured heading if colour supported."""
    return f"{SECTION}{text}{RESET}" if SECTION else text


@dataclass
class StepResult:
    stdout: str
    stderr: str
    code: int
    duration: float


@dataclass
class CaseReport:
    base: str
    obf_time: float
    deobf_time: float
    run_original: StepResult
    run_obfuscated: StepResult
    run_deobfuscated: StepResult
    out_match: bool = field(init=False)
    code_match: bool = field(init=False)

    def __post_init__(self):
        self.out_match = (
            self.run_original.stdout == self.run_obfuscated.stdout
            == self.run_deobfuscated.stdout
        )
        self.code_match = (
            self.run_original.code
            == self.run_obfuscated.code
            == self.run_deobfuscated.code
        )


def run_script(path: Path) -> StepResult:
    start = time.perf_counter()
    proc = subprocess.run(
        [sys.executable, str(path)], capture_output=True, text=True
    )
    dur = time.perf_counter() - start
    return StepResult(proc.stdout, proc.stderr, proc.returncode, dur)


def obfuscate(
    input_file: Path, obf_file: Path, transformations: List[str]
) -> float:
    cmd = [
        sys.executable,
        "-m",
        "obfuscator.main",
        "--input",
        str(input_file),
        "--output",
        str(obf_file),
        "--transformations",
        *transformations,
    ]
    start = time.perf_counter()
    proc = subprocess.run(cmd, capture_output=True, text=True)
    dur = time.perf_counter() - start
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr or "Error during obfuscation")
    return dur


def deobfuscate_gpt(
    obf_file: Path, deobf_file: Path, model: str
) -> float:
    cmd = [
        sys.executable,
        "-m",
        "obfuscator.main",
        "--input",
        str(obf_file),
        "--output",
        str(deobf_file),
        "--gpt",
        "--model",
        model,
    ]
    start = time.perf_counter()
    proc = subprocess.run(cmd, capture_output=True, text=True)
    dur = time.perf_counter() - start
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr or "Error during GPT de-obfuscation")
    return dur


def process_case(
    base: str, example_dir: Path, output_dir: Path, model: str
) -> CaseReport:
    print(_c(f"\n➡ Processing case: {base}"))
    input_file = example_dir / f"{base}_input.py"
    obf_file = output_dir / f"{base}_obfuscated.py"
    deobf_file = output_dir / f"{base}_deobfuscated_{model}.py"
    transformations = [
        "remove_all_comments",
        "rename_identifiers",
        "add_dead_code",
        "restructure_loops",
        "obfuscate_strings",
    ]
    print("  [1/3] Obfuscation…", end=" ")
    obf_time = obfuscate(input_file, obf_file, transformations)
    print(f"{obf_time:.2f}s {OK}")
    print("  [2/3] GPT de-obfuscation…", end=" ")
    deobf_time = deobfuscate_gpt(obf_file, deobf_file, model)
    print(f"{deobf_time:.2f}s {OK}")
    print("  [3/3] Execution…")
    ro = run_script(input_file)
    rof = run_script(obf_file)
    rde = run_script(deobf_file)

    def report(name: str, res: StepResult):
        status = OK if res.code == ro.code and res.stdout == ro.stdout else FAIL
        print(
            f"    {name:<15} code={res.code:<3} dur={res.duration:.2f}s → {status}"
        )

    report("Original", ro)
    report("Obfuscated", rof)
    report("Deobfuscated", rde)
    return CaseReport(base, obf_time, deobf_time, ro, rof, rde)


def choose_model(models: List[str]) -> str:
    print("Select GPT model:")
    for i, m in enumerate(models, 1):
        print(f"  {i}. {m}")
    while True:
        c = input(f"Enter choice [1-{len(models)}]: ").strip()
        if c.isdigit() and 1 <= int(c) <= len(models):
            return models[int(c) - 1]
        print(f"Invalid; choose 1 to {len(models)}.")


def main() -> None:
    p = argparse.ArgumentParser(
        description="Benchmark obfuscation + GPT-deobfuscation + execution."
    )
    p.add_argument("--examples-dir", default="example")
    p.add_argument("--output-dir", default="example")
    p.add_argument(
        "--models",
        nargs="+",
        default=["gpt-4o", "o4-mini", "o1"],
        help="List of GPT models",
    )
    p.add_argument(
        "--model",
        help="Model to use (if omitted, will prompt)",
    )
    p.add_argument(
        "--no-exec", action="store_true", help="Skip execution comparison"
    )
    args = p.parse_args()
    example_dir = Path(args.examples_dir)
    output_dir = Path(args.output_dir)
    example_dir.mkdir(exist_ok=True)
    output_dir.mkdir(exist_ok=True)
    if not example_dir.is_dir():
        sys.exit("Invalid examples-dir")
    model = args.model if args.model in args.models else choose_model(args.models)
    bases = ["palindrom", "prime", "fibonacci"]
    reports: List[CaseReport] = []
    fails = 0
    for b in bases:
        try:
            rep = process_case(b, example_dir, output_dir, model)
            reports.append(rep)
            if not (rep.out_match and rep.code_match):
                fails += 1
        except Exception as e:
            print(FAIL, b, e)
            fails += 1

    # Prepare summary
    summary_lines: List[str] = []
    summary_lines.append(f"Summary for model: {model}")
    header = (
        f"{'Case':<15} {'Obf(s)':>7} {'Deobf(s)':>9} {'Orig(s)':>7} "
        f"{'ObfRun(s)':>10} {'DeRun(s)':>9}"
    )
    summary_lines.append(header)
    summary_lines.append("-" * len(header))
    for r in reports:
        line = (
            f"{r.base:<15} {r.obf_time:7.2f} {r.deobf_time:9.2f} "
            f"{r.run_original.duration:7.2f} {r.run_obfuscated.duration:10.2f} "
            f"{r.run_deobfuscated.duration:9.2f}"
        )
        summary_lines.append(line)

    # Print and write summary
    print(_c("\n" + "\n".join(summary_lines)))
    out_file = output_dir / f"test-{model}.txt"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n".join(summary_lines))
    print(_c(f"\nSummary written to: {out_file}"))

    if fails:
        sys.exit(f"{FAIL} {fails} failures")
    print(OK, "All passed.")


if __name__ == "__main__":
    main()
