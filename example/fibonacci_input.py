# example_input.py
"""
Example Python script that calculates the Fibonacci sequence
and displays the result using a helper class.
"""

class FibonacciCalculator:
    """
    Calculates the Fibonacci sequence using a recursive approach.
    """
    def fibonacci(self, n: int) -> int:
        """
        Returns the n-th term of the Fibonacci sequence (recursive implementation).
        """
        if n < 2:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def run_sequence(self, length: int) -> list:
        """
        Generates a list containing the Fibonacci sequence from 0 to length-1.
        """
        return [self.fibonacci(i) for i in range(length)]

class DisplayHelper:
    """
    Helper class to display formatted messages.
    """
    def __init__(self, title: str):
        self.title = title

    def show_message(self, message: str):
        """
        Prints a formatted message with a title.
        """
        print(f"[{self.title}]: {message}")

def main():
    calculator = FibonacciCalculator()
    helper = DisplayHelper("Fibonacci Program")

    length = 35
    fib_sequence = calculator.run_sequence(length)
    helper.show_message(f"Fibonacci sequence of length {length} => {fib_sequence}")

if __name__ == "__main__":
    main()
