# obfuscator/transformations/restructure_loops.py
"""
Converts for-loops that use range() into while-loops to make the control flow less obvious.
"""

import ast

class RestructureLoops(ast.NodeTransformer):
    """
    Transforms for-loops into equivalent while-loops.
    """

    def visit_For(self, node: ast.For):
        # Only transform loops that iterate over range()
        if (
            isinstance(node.iter, ast.Call) and
            isinstance(node.iter.func, ast.Name) and
            node.iter.func.id == "range"
        ):
            args = node.iter.args

            # Handle different cases for the range() arguments
            if len(args) == 1:
                start = ast.Constant(value=0)
                stop = args[0]
                step = ast.Constant(value=1)
            elif len(args) == 2:
                start = args[0]
                stop = args[1]
                step = ast.Constant(value=1)
            elif len(args) == 3:
                start, stop, step = args
            else:
                return self.generic_visit(node)

            # Ensure that the loop variable is a simple variable
            if isinstance(node.target, ast.Name):
                var_name = node.target.id
            else:
                return self.generic_visit(node)

            # Create an assignment for initializing the loop variable: i = start
            init_assign = ast.Assign(
                targets=[ast.Name(id=var_name, ctx=ast.Store())],
                value=start
            )

            # Choose the comparison operator based on the step's sign
            if isinstance(step, ast.Constant) and isinstance(step.value, (int, float)) and step.value < 0:
                op = ast.Gt()
            else:
                op = ast.Lt()

            # Build the while-loop condition: while i < stop (or i > stop)
            condition = ast.Compare(
                left=ast.Name(id=var_name, ctx=ast.Load()),
                ops=[op],
                comparators=[stop]
            )

            # Create an increment statement: i += step
            increment = ast.AugAssign(
                target=ast.Name(id=var_name, ctx=ast.Store()),
                op=ast.Add(),
                value=step
            )

            # The body of the while-loop includes the original loop body plus the increment
            new_body = node.body + [increment]

            # Construct the while-loop node
            while_loop = ast.While(
                test=condition,
                body=new_body,
                orelse=node.orelse
            )

            # Return a list of nodes: the initialization assignment and the while-loop
            return [init_assign, while_loop]

        return self.generic_visit(node)
