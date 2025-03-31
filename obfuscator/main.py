# obfuscator/main.py
"""
Main entry point for the Python code obfuscation tool.

Usage:
    - Without --gpt:
        Applies AST transformations (if specified) to the input code and writes the obfuscated code.
    - With --gpt:
        Skips local transformations and sends the original input code to GPT for analysis and rewriting.
    - Usage in good order:
        python -m obfuscator.main --input example_input.py --output example_obfuscated.py --transformations remove_all_comments rename_identifiers add_dead_code restructure_loops obfuscate_strings
    - Usage with gpt:
        python -m obfuscator.main --input example_obfuscated.py --output example_gpt.py --gpt


"""

import argparse
import ast
import astor

from obfuscator.transformations.rename_identifiers import RenameIdentifiers
from obfuscator.transformations.add_dead_code import AddDeadCode
from obfuscator.transformations.restructure_loops import RestructureLoops
from obfuscator.transformations.obfuscate_strings import ObfuscateStrings, insert_helper_function
from obfuscator.transformations.remove_all_comments import remove_all_comments
from obfuscator.gpt_integration import call_chatgpt_for_analysis_and_code

# Mapping between transformation names and their corresponding classes.
# Note: 'remove_all_comments' is handled separately before AST parsing.
TRANSFORMATIONS_MAP = {
    "rename_identifiers": RenameIdentifiers,
    "restructure_loops": RestructureLoops,
    "obfuscate_strings": ObfuscateStrings,
    "add_dead_code": AddDeadCode,
}

def apply_transformations(tree: ast.AST, transformations: list) -> ast.AST:
    """
    Applies each specified transformation to the AST.

    :param tree: The abstract syntax tree (AST) of the code.
    :param transformations: A list of transformation names.
    :return: The transformed AST.
    """
    for tname in transformations:
        transform_class = TRANSFORMATIONS_MAP.get(tname)
        if not transform_class:
            print(f"Unknown transformation: {tname}")
            continue
        transformer = transform_class()
        tree = transformer.visit(tree)
    return tree

def main():
    parser = argparse.ArgumentParser(description="CLI for Python code obfuscation")
    parser.add_argument("--input", required=True, help="Path to the input Python file")
    parser.add_argument("--output", required=True, help="Path for the output file")
    parser.add_argument("--transformations", nargs="+", default=[],
                        help="List of transformations to apply (e.g., rename_identifiers, add_dead_code, etc.)")
    parser.add_argument("--gpt", action="store_true",
                        help="If set, skip local transformations and send the input code directly to GPT for analysis")
    args = parser.parse_args()

    # Read the original source code from the input file.
    with open(args.input, "r", encoding="utf-8") as file:
        original_source = file.read()

    # If the --gpt flag is set, bypass all local transformations.
    if args.gpt:
        # Directly send the original source to GPT integration.
        final_response = call_chatgpt_for_analysis_and_code(original_source)
        with open(args.output, "w", encoding="utf-8") as file:
            file.write(final_response)
        print(f"Final file (analysis + GPT code): {args.output}")
        return

    # Otherwise, proceed with local transformations.

    # Optionally remove all comments if specified (applied before parsing AST).
    if "remove_all_comments" in args.transformations:
        original_source = remove_all_comments(original_source)
        # Remove the transformation from the list to avoid duplicate processing.
        args.transformations = [t for t in args.transformations if t != "remove_all_comments"]

    # Parse the (possibly cleaned) source code into an AST.
    tree = ast.parse(original_source)
    ast.fix_missing_locations(tree)

    # Apply all transformations except "obfuscate_strings" first.
    other_transforms = [t for t in args.transformations if t != "obfuscate_strings"]
    tree = apply_transformations(tree, other_transforms)
    ast.fix_missing_locations(tree)

    # If "obfuscate_strings" is requested, insert the helper function first, then apply it.
    if "obfuscate_strings" in args.transformations:
        tree = insert_helper_function(tree)
        tree = ObfuscateStrings().visit(tree)
        ast.fix_missing_locations(tree)

    # Convert the final AST back into source code.
    obfuscated_code = astor.to_source(tree)

    # Write the transformed (obfuscated) code to the output file.
    with open(args.output, "w", encoding="utf-8") as file:
        file.write(obfuscated_code)
    print(f"Obfuscated file: {args.output}")

if __name__ == "__main__":
    main()
