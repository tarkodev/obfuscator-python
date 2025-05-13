# Define a function to decode a base64 encoded string
def _obf_decode(s):
    import base64
    # Decode the base64 string and return its UTF-8 representation
    return base64.b64decode(s).decode('utf-8')


# Define a class with methods for calculating Fibonacci numbers
class FibonacciCalculator:

    # Recursive Fibonacci calculation method
    def fibonacci(self, n: int) -> int:
        # Return n if n is less than 2, as base cases
        if n < 2:
            return n
        # Recursive call to calculate the Fibonacci series
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    # Method to return a list of Fibonacci numbers up to a given count
    def fibonacci_sequence(self, count: int) -> list:
        # List comprehension to generate a list of Fibonacci numbers
        return [self.fibonacci(i) for i in range(count)]


# Define a Printer class to display messages
class Printer:

    # Constructor to initialize the title
    def __init__(self, title: str):
        self.title = title

    # Method to print the formatted message
    def print_message(self, message: str):
        # Print the title and message
        print(f"[{self.title}]: {message}")


# Main function to demonstrate the functionality
def main_program():
    # Create an instance of FibonacciCalculator
    fibonacci_calculator = FibonacciCalculator()
    # Create a Printer instance with a decoded title
    printer = Printer(_obf_decode('Rmlib25hY2NpIFByb2dyYW0='))
    # Define the length of the Fibonacci sequence to calculate
    length_of_sequence = 35
    # Calculate the Fibonacci sequence
    fibonacci_sequence = fibonacci_calculator.fibonacci_sequence(length_of_sequence)
    # Use printer to display the Fibonacci sequence
    printer.print_message(
        f"Fibonacci sequence of length {length_of_sequence} => {fibonacci_sequence}"
    )


# Execute the main_program function if this script is the main program
if __name__ == "__main__":
    main_program()