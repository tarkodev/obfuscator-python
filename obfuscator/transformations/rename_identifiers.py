# obfuscator/transformations/rename_identifiers.py

# This module renames Python identifiers to obfuscate source code readability.
# It targets names like variables, functions, classes, attributes, and keyword args,
# while preserving built-ins, magic names, and our own helper.

import ast          # Import Python’s Abstract Syntax Tree library for code parsing/manipulation
import string       # Import string constants (e.g., ascii_lowercase) for name generation
import random       # Import random utilities to pick random characters for obfuscated names

# Build a set of names we must never rename to avoid breaking functionality
BUILTINS_TO_SKIP = set(dir(__builtins__)).union({  # Start with all built-in identifiers
    '__name__', '__main__',                         # Module metadata variables
    'range', 'print', 'len', 'sum', 'min', 'max',    # Common built-in functions
    'open',                                          # File I/O
    'map', 'zip', 'filter', 'enumerate', 'input',    # Functional tools and input
    'sorted',                                        # Sorting utility
    'list', 'dict', 'set', 'int', 'float',           # Core types
    'str', 'bool', 'type', 'object', 'dir', 'id',    # More built-ins
    # Common methods on built-in container types:
    'append', 'extend', 'insert', 'remove', 'pop',
    'clear', 'index', 'count', 'sort', 'reverse'
})

class RenameIdentifiers(ast.NodeTransformer):
    """
    AST transformer class that renames identifiers throughout the code.
    """

    def __init__(self):
        super().__init__()  # Initialize the base NodeTransformer
        self.mapping = {}   # Dictionary to map original names to obfuscated names
        self.counter = 0    # Counter to guarantee unique name suffixes

    def generate_name(self) -> str:
        """
        Create a new unique obfuscated identifier each time it’s called.
        """
        # Choose 5 random lowercase letters
        random_letters = "".join(random.choices(string.ascii_lowercase, k=5))
        self.counter += 1  # Increment counter for uniqueness
        # Combine prefix, random letters, and counter to form the new name
        return f"var_{random_letters}_{self.counter}"

    def is_skip(self, name: str) -> bool:
        """
        Determine if `name` should be excluded from obfuscation.
        """
        if name == "_obf_decode":                                # Protect our decode helper
            return True
        if name in BUILTINS_TO_SKIP:                             # Skip any built-in or known name
            return True
        if name in ('True', 'False', 'None'):                    # Skip literal constants
            return True
        if name.startswith('__') and name.endswith('__'):        # Skip magic (dunder) names
            return True
        for t in (str, list, dict, set):                         # Skip attributes of built-in types
            if hasattr(t, name):
                return True
        return False                                             # Otherwise, safe to rename

    def visit_Name(self, node: ast.Name):
        """
        Called for every occurrence of a bare identifier in expressions.
        """
        original = node.id                                       # Grab the original name
        if not self.is_skip(original):                           # If it’s not protected
            if original not in self.mapping:                     # And we haven’t mapped it yet
                self.mapping[original] = self.generate_name()    # Generate and store a new name
            node.id = self.mapping[original]                     # Replace with the obfuscated name
        return self.generic_visit(node)                          # Continue traversal

    def visit_FunctionDef(self, node: ast.FunctionDef):
        """
        Called for each function definition in the AST.
        """
        # Rename the function itself if it’s not in the skip list
        if not self.is_skip(node.name):
            if node.name not in self.mapping:                    # Map new name if needed
                self.mapping[node.name] = self.generate_name()
            node.name = self.mapping[node.name]                  # Apply the obfuscated name

        # Iterate over positional arguments in the function signature
        for arg in node.args.args:
            arg_name = arg.arg                                  # Original argument name
            if not self.is_skip(arg_name):                      # If not protected
                if arg_name not in self.mapping:                # Map if unseen
                    self.mapping[arg_name] = self.generate_name()
                arg.arg = self.mapping[arg_name]                # Rename the argument

        return self.generic_visit(node)                         # Recurse into the function body

    def visit_ClassDef(self, node: ast.ClassDef):
        """
        Called for each class definition in the AST.
        """
        if not self.is_skip(node.name):                         # If class name is not protected
            if node.name not in self.mapping:                    # Map if unseen
                self.mapping[node.name] = self.generate_name()
            node.name = self.mapping[node.name]                  # Rename the class
        return self.generic_visit(node)                         # Recurse into class body

    def visit_Call(self, node: ast.Call):
        """
        Called for each function/method call in the AST.
        """
        # Handle keyword arguments in calls (e.g., foo(bar=1))
        for kw in node.keywords:
            if kw.arg is not None and not self.is_skip(kw.arg):  # Skip **kwargs and protected args
                if kw.arg not in self.mapping:                   # Map if unseen
                    self.mapping[kw.arg] = self.generate_name()
                kw.arg = self.mapping[kw.arg]                    # Rename the keyword argument
        return self.generic_visit(node)                          # Continue traversal

    def visit_Attribute(self, node: ast.Attribute):
        """
        Called for attribute access (e.g., obj.attr).
        """
        attr_name = node.attr                                    # Original attribute name
        if not self.is_skip(attr_name):                          # If attribute is not protected
            if attr_name not in self.mapping:                    # Map if unseen
                self.mapping[attr_name] = self.generate_name()
            node.attr = self.mapping[attr_name]                  # Apply obfuscated name
        return self.generic_visit(node)                          # Recurse into the object part
