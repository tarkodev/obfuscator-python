# Check if a number is prime
def is_prime(n: int) -> bool:
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    # 2 is prime
    if n == 2:
        return True
    # Even numbers greater than 2 are not prime
    if n % 2 == 0:
        return False
    # Check odd divisors up to the square root of n
    i = 3
    while i <= int(n ** 0.5) + 1:
        if n % i == 0:
            return False
        i += 2
    return True

# Generate a list of all primes below a given limit
def primes_below(limit: int) -> list:
    return [i for i in range(limit) if is_prime(i)]

# Class responsible for printing messages with a title
class Printer:
    # Store the title for printouts
    def __init__(self, title: str):
        self.title = title

    # Print a message prefixed by the title
    def print_message(self, message: str):
        print(f"[{self.title}]: {message}")

# Main execution function
def main():
    # Define the upper bound for prime generation
    limit = 1000000
    # Compute all primes below the limit
    prime_list = primes_below(limit)
    # Initialize the printer with a descriptive title
    printer = Printer("Prime Checker")
    # Print the result in the desired format
    printer.print_message(f"Prime numbers below {limit} => {prime_list}")

# Run main if this script is the entry point
if __name__ == "__main__":
    main()