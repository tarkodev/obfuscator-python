# Class responsible for Fibonacci computations
class FibonacciCalculator:
    # Recursive computation of the nth Fibonacci number
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n - 1) + self.fib(n - 2)

    # Generate a list of Fibonacci numbers of given length
    def sequence(self, count: int) -> list[int]:
        return [self.fib(i) for i in range(count)]

# Class for printing messages with a title prefix
class MessagePrinter:
    # Store the title for message output
    def __init__(self, title: str):
        self.title = title

    # Print a formatted message with the stored title
    def print_message(self, message: str):
        print(f"[{self.title}]: {message}")

# Main program logic
def main():
    # Instantiate Fibonacci calculator and message printer
    fib_calculator = FibonacciCalculator()
    printer = MessagePrinter("Fibonacci Program")

    # Define how many Fibonacci numbers to generate
    count = 35

    # Compute the Fibonacci sequence list
    fib_sequence = fib_calculator.sequence(count)

    # Output the result with a descriptive message
    printer.print_message(f"Fibonacci sequence of length {count} => {fib_sequence}")

# Execute main when run as a script
if __name__ == "__main__":
    main()