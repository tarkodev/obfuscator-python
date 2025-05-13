# Class for prime number related operations
class PrimeChecker:
    # Determine if a given number is prime
    def is_prime(self, n: int) -> bool:
        # Numbers less than 2 are not prime
        if n <= 1:
            return False
        # 2 is prime
        if n == 2:
            return True
        # Even numbers greater than 2 are not prime
        if n % 2 == 0:
            return False
        # Check odd divisors up to square root of n
        divisor = 3
        # Continue while divisor does not exceed sqrt(n)
        while divisor <= int(n ** 0.5) + 1:
            # If divisor divides n evenly, n is not prime
            if n % divisor == 0:
                return False
            divisor += 2
        # No divisors found; n is prime
        return True

    # Generate a list of prime numbers below a given limit
    def primes_below(self, limit: int) -> list:
        # Use list comprehension to collect primes in range
        return [i for i in range(limit) if self.is_prime(i)]

# Class for printing messages with a title
class TitlePrinter:
    # Store the title for messages
    def __init__(self, title: str):
        self.title = title

    # Print a formatted message with the title prefix
    def print_message(self, message: str):
        print(f"[{self.title}]: {message}")

# Main function to run the prime checking and output
def main():
    # Instantiate the prime checker
    checker = PrimeChecker()
    # Instantiate the printer with a descriptive title
    printer = TitlePrinter("Prime Checker")
    # Define the upper limit for prime generation
    limit = 1000000
    # Generate all primes below the limit
    primes = checker.primes_below(limit)
    # Print the result
    printer.print_message(f"Prime numbers below {limit} => {primes}")

# Execute main if this script is run directly
if __name__ == "__main__":
    main()
