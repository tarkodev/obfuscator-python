# obfuscator/utils.py
"""
Utility functions for file parsing and AST transformations.
"""

import ast


def parse_file(file_path: str) -> ast.AST:
    """
    Reads a Python file and returns its abstract syntax tree (AST).

    :param file_path: Path to the Python file.
    :return: AST representation of the file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        source_code = file.read()
    return ast.parse(source_code)


def write_file(tree: ast.AST, output_path: str):
    """
    Reconstructs source code from an AST and writes it to a file.
    (Requires Python 3.9+ for ast.unparse.)

    :param tree: The AST to convert.
    :param output_path: Path to write the output file.
    """
    new_code = ast.unparse(tree)
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(new_code)


def apply_transformations(tree: ast.AST, transformations: list) -> ast.AST:
    """
    Applies a list of AST transformations in sequence.

    :param tree: The AST to transform.
    :param transformations: List of transformation objects.
    :return: The transformed AST.
    """
    for transform in transformations:
        tree = transform.visit(tree)
        ast.fix_missing_locations(tree)
    return tree
