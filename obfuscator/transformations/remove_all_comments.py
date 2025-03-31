# obfuscator/transformations/remove_all_comments.py
"""
Removes all comments from the source code, including both inline comments and docstrings.
This is performed before any AST transformations to simplify the code.
"""

import ast
import io
import tokenize
import astor


def remove_classic_comments(source: str) -> str:
    """
    Removes standard comments (lines starting with '#') from the source code.

    :param source: Original source code.
    :return: Source code without inline comments.
    """
    tokens = list(tokenize.generate_tokens(io.StringIO(source).readline))
    tokens_no_comments = [tok for tok in tokens if tok.type != tokenize.COMMENT]
    return tokenize.untokenize(tokens_no_comments)


class RemoveDocstrings(ast.NodeTransformer):
    """
    Removes standalone string expressions that act as docstrings.
    """

    def visit_Expr(self, node: ast.Expr):
        if isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
            return None  # Remove the node entirely
        return self.generic_visit(node)


def remove_all_comments(source: str) -> str:
    """
    Removes both inline comments and docstrings from the code.

    :param source: The original source code.
    :return: Cleaned source code without comments.
    """
    # Step 1: Remove inline comments using tokenize
    source_no_classic = remove_classic_comments(source)
    # Step 2: Parse the cleaned source into an AST
    tree = ast.parse(source_no_classic)
    # Step 3: Remove docstrings from the AST
    remover = RemoveDocstrings()
    tree = remover.visit(tree)
    ast.fix_missing_locations(tree)
    # Step 4: Convert the AST back into source code
    return astor.to_source(tree)
