# obfuscator/transformations/obfuscate_strings.py
"""
Replaces string literals with calls to a helper function that decodes a Base64-encoded version of the string.
This helps hide the original strings in the code.
"""

import ast
import base64

class ObfuscateStrings(ast.NodeTransformer):
    """
    Transforms string constants by encoding them and replacing them with a function call.
    """

    def visit_FunctionDef(self, node: ast.FunctionDef):
        # If the function is marked to avoid string obfuscation, skip it.
        if getattr(node, '_no_string_obfuscation', False):
            return node
        return self.generic_visit(node)

    def visit_Constant(self, node: ast.Constant):
        # For string constants, encode and replace with a call to _obf_decode(encoded_string)
        if isinstance(node.value, str):
            encoded = base64.b64encode(node.value.encode('utf-8')).decode('utf-8')
            new_node = ast.Call(
                func=ast.Name(id='_obf_decode', ctx=ast.Load()),
                args=[ast.Constant(value=encoded)],
                keywords=[]
            )
            return ast.copy_location(new_node, node)
        return node

    def visit_JoinedStr(self, node: ast.JoinedStr):
        # Process f-strings: encode literal parts and keep formatted values intact.
        new_values = []
        for value in node.values:
            if isinstance(value, ast.Constant) and isinstance(value.value, str):
                encoded = base64.b64encode(value.value.encode('utf-8')).decode('utf-8')
                call_node = ast.Call(
                    func=ast.Name(id='_obf_decode', ctx=ast.Load()),
                    args=[ast.Constant(value=encoded)],
                    keywords=[]
                )
                # Wrap the call in a FormattedValue so it fits in the f-string.
                formatted = ast.FormattedValue(
                    value=call_node,
                    conversion=-1,
                    format_spec=None
                )
                new_values.append(formatted)
            else:
                new_values.append(self.visit(value))
        node.values = new_values
        return node

def insert_helper_function(tree: ast.AST) -> ast.AST:
    """
    Inserts the helper function '_obf_decode' at the beginning of the module.
    This function decodes the Base64-encoded strings.
    It is marked to avoid being obfuscated.
    """
    helper_code = """
def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')
"""
    helper_tree = ast.parse(helper_code)
    helper_func = helper_tree.body[0]
    # Mark the helper function so that it is excluded from further obfuscation
    setattr(helper_func, '_no_string_obfuscation', True)
    tree.body.insert(0, helper_func)
    return tree
