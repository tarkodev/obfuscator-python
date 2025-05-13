# obfuscator/transformations/add_dead_code.py
import ast  # Abstract Syntax Trees: used to parse and manipulate Python code at the syntactic level
import random  # Provides utilities for random value generation

class AddDeadCode(ast.NodeTransformer):
    """
    A transformer that injects "dead" (unreachable) code into Python AST nodes.
    This can help obfuscate code by adding blocks and functions never executed at runtime.
    """

    def visit_FunctionDef(self, node: ast.FunctionDef):
        # Avoid adding dead code into functions that are already marked as dummy
        if node.name.startswith("unused_function_"):
            # Continue generic visitation for consistency
            return self.generic_visit(node)

        # --------------------------------------------------------------------
        # 1) Construct an `if False:` block that will never execute
        # --------------------------------------------------------------------
        dead_if = ast.If(
            test=ast.Constant(value=False),  # `if False` ensures this block is never entered
            body=[
                # Add a print statement inside the dead block
                ast.Expr(
                    value=ast.Call(
                        func=ast.Name(id='print', ctx=ast.Load()),  # print(...)
                        args=[ast.Constant(value="This is dead code")],  # message literal
                        keywords=[]
                    )
                )
            ],
            orelse=[]  # No `else` branch needed
        )

        # --------------------------------------------------------------------
        # 2) Define a dummy function with a randomized name and trivial return
        # --------------------------------------------------------------------
        random_suffix = random.randint(1000, 9999)  # Generate a random number for uniqueness
        dummy_name = f"unused_function_{random_suffix}"
        dead_func = ast.FunctionDef(
            name=dummy_name,
            args=ast.arguments(
                posonlyargs=[],  # No positional-only args
                args=[],         # No normal args
                kwonlyargs=[],   # No keyword-only args
                kw_defaults=[],  # No default values for kw args
                defaults=[]       # No default values for positional args
            ),
            body=[
                # A simple constant expression (has no effect)
                ast.Expr(value=ast.Constant(value="A useless function")),
                # Return a meaningless constant
                ast.Return(value=ast.Constant(value=42))
            ],
            decorator_list=[]  # No decorators on the dummy function
        )

        # --------------------------------------------------------------------
        # 3) Inject the constructed dead code snippets at the start of the function
        # --------------------------------------------------------------------
        node.body.insert(0, dead_if)     # Place `if False: print(...)` as the first statement
        node.body.insert(1, dead_func)   # Insert the dummy function immediately after

        # Continue to traverse deeper AST nodes
        return self.generic_visit(node)

    def visit_Module(self, node: ast.Module):
        # ------------------------------------------------------------------------
        # Add a dead code block at the very top of the module file
        # ------------------------------------------------------------------------
        dead_if_top = ast.If(
            test=ast.Constant(value=False),  # Always false condition
            body=[
                # Expression with a constant literal; safe and harmless
                ast.Expr(value=ast.Constant(value="Dead code at module level"))
            ],
            orelse=[]  # No alternative branch
        )

        # Prepend this dead block before any other top-level statements
        node.body.insert(0, dead_if_top)

        # Continue generic visitation for all module-level nodes
        return self.generic_visit(node)
