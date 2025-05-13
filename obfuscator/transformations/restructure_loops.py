# obfuscator/transformations/restructure_loops.py

# Module docstring:
# Provides an AST transformer that rewrites `for i in range(...)` loops
# into equivalent `while` loops, obscuring the original control flow.
"""
Converts for-loops that use range() into while-loops to make the control flow less obvious.
"""

# Import the AST module to work with Python's abstract syntax tree
import ast

# Define a class that will walk and transform the AST nodes
class RestructureLoops(ast.NodeTransformer):
    """
    Transforms `for` loops into equivalent `while` loops when the loop
    iterates over a `range()` call.
    """

    # Override the method that is called for each `For` node in the AST
    def visit_For(self, node: ast.For):
        # Only proceed if the loop’s iterable is a call to `range()`
        if (
            # Check that `node.iter` is an AST Call node
            isinstance(node.iter, ast.Call)
            # Ensure the call’s function part is a Name (e.g., `range`)
            and isinstance(node.iter.func, ast.Name)
            # Confirm that the function’s identifier is exactly "range"
            and node.iter.func.id == "range"
        ):
            # Extract the positional arguments passed to `range()`
            args = node.iter.args

            # Determine start, stop, and step values based on arg count
            if len(args) == 1:
                # Single-argument form: range(stop)
                start = ast.Constant(value=0)   # default start = 0
                stop  = args[0]                # stop is the sole argument
                step  = ast.Constant(value=1)  # default step = 1
            elif len(args) == 2:
                # Two-argument form: range(start, stop)
                start = args[0]                # explicit start
                stop  = args[1]                # explicit stop
                step  = ast.Constant(value=1)  # default step = 1
            elif len(args) == 3:
                # Three-argument form: range(start, stop, step)
                start, stop, step = args       # unpack all three directly
            else:
                # If `range()` is called with zero or >3 args, skip transformation
                return self.generic_visit(node)

            # Ensure the loop target is a simple variable name (not tuple unpack, etc.)
            if isinstance(node.target, ast.Name):
                var_name = node.target.id       # capture the loop variable’s name
            else:
                # Non-simple targets are not handled; leave unchanged
                return self.generic_visit(node)

            # Create an assignment node: var_name = start
            init_assign = ast.Assign(
                targets=[ast.Name(id=var_name, ctx=ast.Store())],  # left-hand side variable
                value=start                                        # right-hand side initial value
            )

            # Choose the comparison operator based on whether step is negative
            if (
                isinstance(step, ast.Constant)
                and isinstance(step.value, (int, float))
                and step.value < 0
            ):
                op = ast.Gt()   # for negative steps, loop while var > stop
            else:
                op = ast.Lt()   # for positive (or non-constant) steps, loop while var < stop

            # Build the while-loop test: var_name < stop  (or > stop)
            condition = ast.Compare(
                left=ast.Name(id=var_name, ctx=ast.Load()),  # load the loop variable
                ops=[op],                                     # chosen comparison operator
                comparators=[stop]                            # right-hand side of comparison
            )

            # Create an AST node for incrementing the loop variable: var_name += step
            increment = ast.AugAssign(
                target=ast.Name(id=var_name, ctx=ast.Store()), # variable to update
                op=ast.Add(),                                   # '+=' operation
                value=step                                      # amount to add each iteration
            )

            # Combine the original loop body with the new increment at the end
            new_body = node.body + [increment]

            # Construct the AST node for the `while` loop itself
            while_loop = ast.While(
                test=condition,        # the loop condition we just built
                body=new_body,         # the body including original statements + increment
                orelse=node.orelse     # preserve any `else:` block from the original `for`
            )

            # Return a list of two AST nodes: initialization, then the `while` loop
            return [init_assign, while_loop]

        # If not a `range()`-based for-loop, recurse normally without changes
        return self.generic_visit(node)
