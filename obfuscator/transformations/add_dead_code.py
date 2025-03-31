# obfuscator/transformations/add_dead_code.py
"""
Adds dead code (such as unreachable blocks and useless functions)
to make the code harder to read and understand.
"""

import ast
import random

class AddDeadCode(ast.NodeTransformer):
    """
    Inserts dummy code blocks and functions into the code.
    """

    def visit_FunctionDef(self, node: ast.FunctionDef):
        # Skip functions that are already dummy functions to avoid recursion
        if node.name.startswith("unused_function_"):
            return self.generic_visit(node)

        # Create an 'if False:' block with a print statement
        dead_if = ast.If(
            test=ast.Constant(value=False),
            body=[
                ast.Expr(
                    value=ast.Call(
                        func=ast.Name(id='print', ctx=ast.Load()),
                        args=[ast.Constant(value="This is dead code")],
                        keywords=[]
                    )
                )
            ],
            orelse=[]
        )

        # Create a dummy function with a random name
        dead_func = ast.FunctionDef(
            name=f"unused_function_{random.randint(1000, 9999)}",
            args=ast.arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]),
            body=[
                ast.Expr(value=ast.Constant(value="A useless function")),
                ast.Return(value=ast.Constant(value=42))
            ],
            decorator_list=[]
        )

        # Insert the dead code at the beginning of the function body
        node.body.insert(0, dead_if)
        node.body.insert(1, dead_func)

        return self.generic_visit(node)

    def visit_Module(self, node: ast.Module):
        # Insert a dead code block at the top of the module
        dead_if_top = ast.If(
            test=ast.Constant(value=False),
            body=[ast.Expr(value=ast.Constant(value="Dead code at module level"))],
            orelse=[]
        )
        node.body.insert(0, dead_if_top)
        return self.generic_visit(node)
