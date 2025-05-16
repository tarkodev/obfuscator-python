# This function decodes a base64-encoded string
def decode_str(s):
    # Import base64 library for decoding
    import base64
    # Decode from base64, then from UTF-8
    return base64.b64decode(s).decode('utf-8')

# This class provides Fibonacci-related functionalities
class FibonacciCalculator:
    # This method returns the nth Fibonacci number (recursive)
    def fibonacci_number(self, n: int) -> int:
        # Base case for n < 2
        if n < 2:
            return n
        # Recursive case
        return self.fibonacci_number(n - 1) + self.fibonacci_number(n - 2)

    # This method returns a list of Fibonacci numbers up to a given length
    def fibonacci_sequence(self, length: int) -> list:
        # Build list using the fibonacci_number method
        return [self.fibonacci_number(i) for i in range(length)]

# This class prints messages with a stored title
class MessagePrinter:
    # Initialize with a title
    def __init__(self, title: str):
        self.title = title

    # Print a message prefixed by the title
    def print_message(self, message: str):
        print(f"[{self.title}]: {message}")

# Main function to demonstrate Fibonacci functionality
def main():
    # Create a FibonacciCalculator instance
    fib_calc = FibonacciCalculator()
    # Create a MessagePrinter instance with a given title
    printer = MessagePrinter("Fibonacci Program")
    # Define the length for the Fibonacci sequence
    length = 35
    # Generate the Fibonacci sequence
    fib_seq = fib_calc.fibonacci_sequence(length)
    # Print the resulting sequence
    printer.print_message(f"Fibonacci sequence of length {length} => {fib_seq}")

# Entry point check
if __name__ == "__main__":
    main()