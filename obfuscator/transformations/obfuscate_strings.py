# obfuscator/transformations/obfuscate_strings.py

"""
Replaces string literals with calls to a helper function that decodes
a Base64-encoded version of the string. This helps hide the original
strings in the code.
"""

import ast      # Python’s built-in Abstract Syntax Tree module
import base64   # Standard library for Base64 encoding/decoding

class ObfuscateStrings(ast.NodeTransformer):
    """
    AST transformer that finds string constants in the code and replaces
    them with calls to a helper function (_obf_decode) which will decode
    Base64-encoded strings at runtime.
    """

    def visit_FunctionDef(self, node: ast.FunctionDef):
        # ------------------------------------------------------------------
        # Skip obfuscation for any function explicitly marked to avoid it.
        # This is useful to prevent the helper function itself from being
        # encoded, or any other functions the user wants to keep intact.
        # The marker is a custom attribute `_no_string_obfuscation`.
        # ------------------------------------------------------------------
        if getattr(node, '_no_string_obfuscation', False):
            return node  # leave the function body unchanged

        # Otherwise, continue walking into the function’s body to find
        # string literals for obfuscation.
        return self.generic_visit(node)

    def visit_Constant(self, node: ast.Constant):
        """
        Called for every constant in the AST. We target string constants
        (instances of str). When we find one, we:
          1. Encode its value in Base64.
          2. Build a new AST node representing a call to _obf_decode(encoded).
          3. Copy the original node’s location so that error reporting
             and tooling still point to the correct line.
        """
        if isinstance(node.value, str):
            # Encode the original string to Base64
            raw_string = node.value
            encoded_bytes = raw_string.encode('utf-8')
            b64_bytes = base64.b64encode(encoded_bytes)
            b64_string = b64_bytes.decode('utf-8')

            # Construct a call node: _obf_decode("encoded_string")
            decode_call = ast.Call(
                func=ast.Name(id='_obf_decode', ctx=ast.Load()),
                args=[ast.Constant(value=b64_string)],
                keywords=[]
            )

            # Preserve the original source location metadata
            return ast.copy_location(decode_call, node)

        # Non-string constants remain untouched
        return node

    def visit_JoinedStr(self, node: ast.JoinedStr):
        """
        Handles f-strings. In an f-string, literal pieces are stored as
        ast.Constant within node.values, while expressions are stored
        as ast.FormattedValue.

        We only encode the literal pieces:
         - Encode each literal piece to Base64.
         - Wrap the decode call in a FormattedValue so it integrates
           properly into the f-string.
        """
        new_values = []
        for part in node.values:
            # Check for literal text segments
            if isinstance(part, ast.Constant) and isinstance(part.value, str):
                literal = part.value
                encoded = base64.b64encode(literal.encode('utf-8')).decode('utf-8')

                # Create a call node for decoding at runtime
                call_node = ast.Call(
                    func=ast.Name(id='_obf_decode', ctx=ast.Load()),
                    args=[ast.Constant(value=encoded)],
                    keywords=[]
                )

                # Wrap the call in FormattedValue for f-string compatibility
                formatted = ast.FormattedValue(
                    value=call_node,
                    conversion=-1,      # default conversion
                    format_spec=None    # no additional format specifier
                )
                new_values.append(formatted)
            else:
                # For expressions or already-visited parts, recurse normally
                new_values.append(self.visit(part))

        # Replace the old list of parts with our new, encoded-aware list
        node.values = new_values
        return node

def insert_helper_function(tree: ast.AST) -> ast.AST:
    """
    Injects the _obf_decode helper function at the top of the module AST.

    This function:
      1. Defines a Python function that takes a Base64 string, decodes it,
         and returns the original text.
      2. Marks that helper function with `_no_string_obfuscation` so that
         our transformer will skip it.
      3. Inserts it as the very first element in the module body so that
         all subsequent decode calls resolve correctly.
    """
    helper_code = """
def _obf_decode(s):
    import base64
    # Decode the Base64-encoded bytes back to the original UTF-8 string
    return base64.b64decode(s).decode('utf-8')
"""
    # Parse the helper code into its own AST
    helper_tree = ast.parse(helper_code)
    helper_func = helper_tree.body[0]  # the FunctionDef node

    # Mark it so the transformer sees the flag and skips obfuscating its body
    setattr(helper_func, '_no_string_obfuscation', True)

    # Insert at the very start of the module
    tree.body.insert(0, helper_func)
    return tree
