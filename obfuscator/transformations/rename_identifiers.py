# obfuscator/transformations/rename_identifiers.py
"""
Renames identifiers (such as variables, function names, and class names) to obfuscate the code.
This transformation avoids renaming built-ins and special names.
"""

import ast
import string
import random

# List of built-in names and other special identifiers that should not be renamed.
BUILTINS_TO_SKIP = set(dir(__builtins__)).union({
    '__name__', '__main__',
    'range', 'print', 'len', 'sum', 'min', 'max', 'open',
    'map', 'zip', 'filter', 'enumerate', 'input', 'sorted',
    'list', 'dict', 'set', 'int', 'float', 'str', 'bool', 'type',
    'object', 'dir', 'id',
    'append', 'extend', 'insert', 'remove', 'pop', 'clear', 'index', 'count', 'sort', 'reverse'
})


class RenameIdentifiers(ast.NodeTransformer):
    """
    Traverses the AST and renames identifiers to make the code less readable.
    """

    def __init__(self):
        super().__init__()
        self.mapping = {}  # Dictionary mapping original names to new names
        self.counter = 0  # Counter to generate unique names

    def generate_name(self) -> str:
        """
        Generates a new, obfuscated name.

        :return: A unique obfuscated identifier.
        """
        rand_part = "".join(random.choices(string.ascii_lowercase, k=5))
        self.counter += 1
        return f"var_{rand_part}_{self.counter}"

    def is_skip(self, name: str) -> bool:
        """
        Checks if a name should be skipped from renaming.

        :param name: The identifier to check.
        :return: True if the name should not be renamed, else False.
        """
        if name == "_obf_decode":
            return True
        if name in BUILTINS_TO_SKIP:
            return True
        if name in ('True', 'False', 'None'):
            return True
        if name.startswith('__') and name.endswith('__'):
            return True
        return False

    def visit_Name(self, node: ast.Name):
        if not self.is_skip(node.id):
            if node.id not in self.mapping:
                self.mapping[node.id] = self.generate_name()
            node.id = self.mapping[node.id]
        return self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef):
        if not self.is_skip(node.name):
            if node.name not in self.mapping:
                self.mapping[node.name] = self.generate_name()
            node.name = self.mapping[node.name]
        # Rename the function arguments
        for arg in node.args.args:
            if not self.is_skip(arg.arg):
                if arg.arg not in self.mapping:
                    self.mapping[arg.arg] = self.generate_name()
                arg.arg = self.mapping[arg.arg]
        return self.generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef):
        if not self.is_skip(node.name):
            if node.name not in self.mapping:
                self.mapping[node.name] = self.generate_name()
            node.name = self.mapping[node.name]
        return self.generic_visit(node)

    def visit_Call(self, node: ast.Call):
        for kw in node.keywords:
            if kw.arg is not None and not self.is_skip(kw.arg):
                if kw.arg not in self.mapping:
                    self.mapping[kw.arg] = self.generate_name()
                kw.arg = self.mapping[kw.arg]
        return self.generic_visit(node)

    def visit_Attribute(self, node: ast.Attribute):
        if not self.is_skip(node.attr):
            if node.attr not in self.mapping:
                self.mapping[node.attr] = self.generate_name()
            node.attr = self.mapping[node.attr]
        return self.generic_visit(node)
