# Decodes a base64-encoded string as UTF-8
def decode_base64_str(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


# Class to compute Fibonacci-related operations
class FibonacciCalculator:

    # Recursive Fibonacci calculation
    def fibonacci(self, n: int) -> int:
        # Computes nth Fibonacci number
        if n < 2:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    # Returns a list of Fibonacci numbers up to count n
    def fibonacci_sequence(self, count: int) -> list:
        # Builds a list of Fibonacci numbers from 0 to count - 1
        return [self.fibonacci(i) for i in range(count)]


# Class representing a program with a title and a printing method
class Program:

    # Initializes with a given title
    def __init__(self, title: str):
        self.title = title

    # Prints a formatted line with the title and message
    def display(self, message: str):
        print(f"[{self.title}]: {message}")


# Main function to run the Fibonacci program
def main():
    fib_calculator = FibonacciCalculator()
    program = Program("Fibonacci Program")
    count = 35
    sequence = fib_calculator.fibonacci_sequence(count)
    program.display(f"Fibonacci sequence of length {count} => {sequence}")


# Entry point check for script execution
if __name__ == "__main__":
    main()
