# Function to decode a base64 encoded string
def decode_base64(s):
    import base64
    return base64.b64decode(s).decode('utf-8')

# Class that handles Fibonacci sequence calculations
class FibonacciCalculator:

    # Method to calculate the nth Fibonacci number
    def fibonacci(self, n: int) -> int:
        # Base cases for the Fibonacci sequence
        if n < 2:
            return n
        # Recursive call to calculate Fibonacci number
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    # Method to generate a list of Fibonacci numbers up to n
    def fibonacci_sequence(self, n: int) -> list:
        # List comprehension to generate Fibonacci sequence
        return [self.fibonacci(i) for i in range(n)]

# Class that handles printing a formatted title and message
class MessagePrinter:

    # Constructor to initialize the class with a title
    def __init__(self, title: str):
        self.title = title

    # Method to print a message with the class title
    def print_message(self, message: str):
        print(f"[{self.title}]: {message}")

# Main function to demonstrate Fibonacci calculation and message printing
def main():
    fib_calc = FibonacciCalculator()
    message_printer = MessagePrinter(decode_base64('Rmlib25hY2NpIFByb2dyYW0='))  # "Fibonacci Program"
    n = 35
    fib_sequence = fib_calc.fibonacci_sequence(n)
    message_printer.print_message(
        f"{decode_base64('Rmlib25hY2NpIHNlcXVlbmNlIG9mIGxlbmd0aCA=')}{n}{decode_base64('ID0+IA==')}{fib_sequence}"
    )

# Check if the script is being run as the main program
if __name__ == "__main__":
    main()