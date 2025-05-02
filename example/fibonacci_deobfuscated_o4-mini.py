# Class to calculate Fibonacci numbers
class FibonacciCalculator:
    # Return the nth Fibonacci number
    def fib(self, n: int) -> int:
        # Base case: return n if less than 2
        if n < 2:
            return n
        # Recursive case: sum of previous two Fibonacci numbers
        return self.fib(n - 1) + self.fib(n - 2)

    # Return a list of Fibonacci numbers of given length
    def fib_sequence(self, length: int) -> list:
        return [self.fib(i) for i in range(length)]

# Class to handle printing with a title
class Printer:
    # Initialize printer with a title
    def __init__(self, title: str):
        self.title = title

    # Print the message prefixed by the title
    def print(self, message: str):
        print(f"[{self.title}]: {message}")

# Main entry point for the program
def main():
    calculator = FibonacciCalculator()
    printer = Printer("Fibonacci Program")
    length = 35
    sequence = calculator.fib_sequence(length)
    printer.print(f"Fibonacci sequence of length {length} => {sequence}")

# Execute main function if this script is run directly
if __name__ == "__main__":
    main()