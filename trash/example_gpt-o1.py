# Brief Analysis:
# 1. The code defines a class that recursively calculates the Fibonacci number of a given integer.
# 2. It also provides a method to generate a list of Fibonacci numbers up to a specified length.
# 3. Another class is used to store a string and print messages with a formatted prefix.
# 4. A main function ties everything together, creating instances and printing the Fibonacci sequence.
# 5. The check at the end allows the main function to run when the script is executed directly.

# Clean, Readable, and Executable Code:

def fibonacci_value(n: int) -> int:
    """
    Calculate the nth Fibonacci number using a simple recursive approach.
    """
    if n < 2:
        return n
    return fibonacci_value(n - 1) + fibonacci_value(n - 2)

def fibonacci_sequence(length: int) -> list:
    """
    Return a list of Fibonacci numbers of the specified length.
    """
    return [fibonacci_value(i) for i in range(length)]

class MessagePrinter:
    """
    Stores a prefix and prints messages with that prefix.
    """
    def __init__(self, prefix: str):
        self.prefix = prefix

    def print_message(self, message: str):
        print(f"[{self.prefix}]: {message}")

def main():
    """
    Main function to demonstrate Fibonacci calculation and message printing.
    """
    printer = MessagePrinter("Fibonacci Program")
    length = 10
    fib_list = fibonacci_sequence(length)
    printer.print_message(f"Fibonacci sequence of length {length} => {fib_list}")

if __name__ == "__main__":
    main()