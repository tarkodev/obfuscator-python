# Provides primality test utilities
class PrimeTester:
    # Check if a number is prime
    def is_prime(self, n: int) -> bool:
        # Numbers less than or equal to 1 are not prime
        if n <= 1:
            return False
        # 2 is prime
        if n == 2:
            return True
        # Even numbers greater than 2 are not prime
        if n % 2 == 0:
            return False
        # Test odd divisors up to sqrt(n)
        i = 3
        while i <= int(n ** 0.5) + 1:
            # If divisible by any i, not prime
            if n % i == 0:
                return False
            i += 2
        # No divisors found, prime
        return True

    # Generate list of primes below a given limit
    def primes_below(self, limit: int) -> list:
        # Return list comprehension of prime numbers < limit
        return [i for i in range(limit) if self.is_prime(i)]


# Simple printer class with a title header
class Printer:
    # Initialize with a title
    def __init__(self, title: str):
        self.title = title

    # Print message with formatted title
    def print_message(self, message: str):
        print(f"[{self.title}]: {message}")


# Main execution function
def main():
    # Instantiate prime tester and printer
    tester = PrimeTester()
    printer = Printer("Prime Checker")
    # Set upper limit for prime generation
    limit = 1000000
    # Generate primes below the limit
    primes = tester.primes_below(limit)
    # Print the result message
    printer.print_message(f"Prime numbers below {limit} => {primes}")


# Run main if script is executed directly
if __name__ == "__main__":
    main()