#!/usr/bin/env python
"""
End-to-end benchmark of the obfuscation/de-obfuscation pipeline.

This test script accepts optional CLI parameters. On startup, it allows passing:
  • --input-dir: directory containing input scripts
  • --output-dir: directory to write obfuscated and deobfuscated scripts
  • --models: space-separated list of GPT models
  • --model: (optional) select model directly
  • --no-exec: skip execution comparison

If --model is not provided or invalid, the user is prompted interactively to choose from --models.
Defaults:
  input-dir  = "benchmark-input"
  output-dir = "benchmark-output"
  bases      = ["palindrom", "prime", "fibonacci"]

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
    """Holds execution results for a script run."""
    stdout: str
    stderr: str
    code: int
    duration: float


@dataclass
class CaseReport:
    """Stores timing and result comparisons for a test case."""
    base: str
    obf_time: float
    deobf_time: float
    run_original: StepResult
    run_obfuscated: StepResult
    run_deobfuscated: StepResult
    out_match: bool = field(init=False)
    code_match: bool = field(init=False)

    def __post_init__(self):
        # Compare stdout and exit codes across original, obfuscated, deobfuscated
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
    """Execute a Python script and capture its output, error, and timing."""
    start = time.perf_counter()
    proc = subprocess.run(
        [sys.executable, str(path)], capture_output=True, text=True
    )
    duration = time.perf_counter() - start
    return StepResult(proc.stdout, proc.stderr, proc.returncode, duration)


def obfuscate(
    input_file: Path, obf_file: Path, transformations: List[str]
) -> float:
    """Run local obfuscator on the input file with given transformations."""
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
    duration = time.perf_counter() - start
    if proc.returncode != 0:
        # Propagate error if obfuscation fails
        raise RuntimeError(proc.stderr or "Error during obfuscation")
    return duration


def deobfuscate_gpt(
    obf_file: Path, deobf_file: Path, model: str
) -> float:
    """Use GPT model to de-obfuscate the obfuscated file."""
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
    duration = time.perf_counter() - start
    if proc.returncode != 0:
        # Propagate error if GPT de-obfuscation fails
        raise RuntimeError(proc.stderr or "Error during GPT de-obfuscation")
    return duration


def process_case(
    base: str, input_dir: Path, output_dir: Path, model: str
) -> CaseReport:
    """Process a single test case: obfuscate, de-obfuscate, and run scripts."""
    print(_c(f"\n➡ Processing case: {base}"))
    # Define file paths based on base name
    src = input_dir / f"{base}_input.py"
    obf = output_dir / f"{base}_obfuscated.py"
    deobf = output_dir / f"{base}_deobfuscated_{model}.py"

    # List of transformations to apply
    transformations = [
        "remove_all_comments",
        "rename_identifiers",
        "add_dead_code",
        "restructure_loops",
        "obfuscate_strings",
    ]

    # 1. Obfuscation step
    print("  [1/3] Obfuscation…", end=" ")
    obf_time = obfuscate(src, obf, transformations)
    print(f"{obf_time:.2f}s {OK}")

    # 2. GPT de-obfuscation step
    print("  [2/3] GPT de-obfuscation…", end=" ")
    deobf_time = deobfuscate_gpt(obf, deobf, model)
    print(f"{deobf_time:.2f}s {OK}")

    # 3. Execute original, obfuscated, and de-obfuscated scripts
    print("  [3/3] Execution…")
    orig_res = run_script(src)
    obf_res = run_script(obf)
    deobf_res = run_script(deobf)

    def report(name: str, res: StepResult):
        """Print comparison status for each execution result."""
        status = OK if (res.code == orig_res.code and res.stdout == orig_res.stdout) else FAIL
        print(
            f"    {name:<15} code={res.code:<3} dur={res.duration:.2f}s → {status}"
        )

    report("Original", orig_res)
    report("Obfuscated", obf_res)
    report("Deobfuscated", deobf_res)

    return CaseReport(base, obf_time, deobf_time, orig_res, obf_res, deobf_res)


def choose_model(models: List[str]) -> str:
    """Prompt the user to select a GPT model if not specified."""
    print("Select GPT model:")
    for i, m in enumerate(models, 1):
        print(f"  {i}. {m}")
    while True:
        choice = input(f"Enter choice [1-{len(models)}]: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(models):
            return models[int(choice) - 1]
        print(f"Invalid; choose a number between 1 and {len(models)}.")


def main() -> None:
    """Parse arguments, iterate over cases, and summarize timings."""
    parser = argparse.ArgumentParser(
        description="Benchmark obfuscation + GPT-deobfuscation + execution."
    )
    # Input directory flag renamed
    parser.add_argument("--input-dir", default="benchmark-input")
    parser.add_argument("--output-dir", default="benchmark-output")
    parser.add_argument(
        "--models",
        nargs="+",
        default=["gpt-4o", "gpt-4.1", "o4-mini", "o1"],
        help="List of GPT models",
    )
    parser.add_argument(
        "--model",
        help="Model to use (if omitted, will prompt)",
    )
    parser.add_argument(
        "--no-exec", action="store_true", help="Skip execution comparison"
    )
    args = parser.parse_args()

    # Convert to Path objects, create directories if needed
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    input_dir.mkdir(exist_ok=True)
    output_dir.mkdir(exist_ok=True)
    if not input_dir.is_dir():
        sys.exit("Invalid input-dir")

    # Determine model to use
    model = args.model if args.model in args.models else choose_model(args.models)

    bases = ["palindrom", "prime", "fibonacci"]
    reports: List[CaseReport] = []
    failures = 0

    # Process each test case
    for base in bases:
        try:
            report = process_case(base, input_dir, output_dir, model)
            reports.append(report)
            if not (report.out_match and report.code_match):
                failures += 1
        except Exception as e:
            print(FAIL, base, e)
            failures += 1

    # Prepare summary lines
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

    # Print and write summary to file
    print(_c("\n" + "\n".join(summary_lines)))
    out_file = output_dir / f"benchmark-{model}.txt"
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("\n".join(summary_lines))
    print(_c(f"\nSummary written to: {out_file}"))

    # Exit code based on failures
    if failures:
        sys.exit(f"{FAIL} {failures} failures")
    print(OK, "All passed.")


if __name__ == "__main__":
    main()
