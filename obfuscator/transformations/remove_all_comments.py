# obfuscator/transformations/remove_all_comments.py

"""
Removes all comments from the source code, including both inline comments
and docstrings. This cleanup is performed before any other AST-based
transformations to simplify the code and ensure docstrings are not
mistaken for executable code.
"""

import ast       # For parsing source into an Abstract Syntax Tree
import io        # For treating strings as file-like objects
import tokenize  # To break the source text into tokens, including comments
import astor     # To convert an AST back into valid source code

def remove_classic_comments(source: str) -> str:
    """
    Strips out standard Python comments (everything from '#' to end of line)
    by tokenizing the input and filtering out COMMENT tokens.

    :param source: The original source code as a single string.
    :return: A new source string with all inline '#' comments removed.
    """
    # Tokenize the source into a sequence of TokenInfo objects
    tokens = list(tokenize.generate_tokens(io.StringIO(source).readline))
    # Filter out any tokens whose type is COMMENT
    tokens_no_comments = [tok for tok in tokens if tok.type != tokenize.COMMENT]
    # Reassemble the tokens back into source code text
    return tokenize.untokenize(tokens_no_comments)

class RemoveDocstrings(ast.NodeTransformer):
    """
    AST transformer that removes standalone string expressions, which
    in Python are used as docstrings for modules, classes, and functions.

    By deleting these Expr nodes whose value is a string constant,
    we strip out all docstring content before regenerating code.
    """
    def visit_Expr(self, node: ast.Expr):
        # Check if this expression is just a string literal (i.e., a docstring)
        if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
            return None  # Returning None removes this node from the AST
        # Otherwise, recurse normally into any child nodes
        return self.generic_visit(node)

def remove_all_comments(source: str) -> str:
    """
    Orchestrates the full comment-removal process:
      1) Remove inline '#' comments via tokenization.
      2) Parse the result into an AST.
      3) Strip out docstring expressions using RemoveDocstrings.
      4) Fix any missing location info in the AST.
      5) Unparse the cleaned AST back into Python source code.

    :param source: Original Python source code as a string.
    :return: Clean code string without comments or docstrings.
    """
    # Step 1: Eliminate inline comments
    source_no_classic = remove_classic_comments(source)

    # Step 2: Parse the comment-stripped code into an AST
    tree = ast.parse(source_no_classic)

    # Step 3: Remove all standalone string expressions (docstrings)
    remover = RemoveDocstrings()
    tree = remover.visit(tree)

    # Repair any missing location metadata in the modified AST
    ast.fix_missing_locations(tree)

    # Step 4: Convert the cleaned AST back into source code text
    # astor.to_source respects Python formatting conventions
    return astor.to_source(tree)
