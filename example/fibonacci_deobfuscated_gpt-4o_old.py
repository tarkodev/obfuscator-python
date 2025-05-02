# Analysis of the obfuscated code:
# 1. The function `_obf_decode` decodes a base64 encoded string to a UTF-8 string.
# 2. The class `var_mebhx_1` contains two methods:
#    - `var_mbaqo_2`: A recursive method to calculate Fibonacci numbers.
#    - `var_nkmbe_5`: Generates a list of Fibonacci numbers up to a given count.
# 3. The class `var_kcgjy_8` has:
#    - An initializer to set a string attribute.
#    - A method `var_dnkdi_10` to print a formatted message.
# 4. The function `var_xkgov_12` creates instances of the above classes and uses them to print a sequence of Fibonacci numbers.
# 5. The main block checks if the script is run as the main module and calls `var_xkgov_12`.

# Clean and readable version of the code:

import base64

def decode_base64(s):
    """Decode a base64 encoded string to a UTF-8 string."""
    return base64.b64decode(s).decode('utf-8')

class FibonacciCalculator:
    """Class to calculate Fibonacci numbers."""

    def fibonacci(self, n: int) -> int:
        """Calculate the nth Fibonacci number."""
        if n < 2:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def fibonacci_sequence(self, count: int) -> list:
        """Generate a list of Fibonacci numbers up to a given count."""
        return [self.fibonacci(i) for i in range(count)]

class MessagePrinter:
    """Class to print formatted messages."""

    def __init__(self, name: str):
        self.name = name

    def print_message(self, message: str):
        """Print a formatted message."""
        print(f"[{self.name}]: {message}")

def main():
    """Main function to demonstrate Fibonacci calculation and message printing."""
    fib_calculator = FibonacciCalculator()
    message_printer = MessagePrinter(decode_base64('Rmlib25hY2NpIFByb2dyYW0='))  # "Fibonacci Program"
    count = 10
    fib_sequence = fib_calculator.fibonacci_sequence(count)
    message_printer.print_message(
        f"{decode_base64('Rmlib25hY2NpIHNlcXVlbmNlIG9mIGxlbmd0aCA=')}{count}{decode_base64('ID0+IA==')}{fib_sequence}"
    )  # "Fibonacci sequence of length " + count + " => " + fib_sequence

if __name__ == "__main__":
    main()