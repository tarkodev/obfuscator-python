# Decodes a base64-encoded string to UTF-8
def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


# Class for prime utilities
class PrimeChecker:

    # Checks if a number is prime
    def is_prime(self, n: int) -> bool:
        # Early return for n <= 1
        if n <= 1:
            return False
        # 2 is the only even prime
        if n == 2:
            return True
        # Exclude other even numbers
        if n % 2 == 0:
            return False
        i = 3
        # Test divisibility up to sqrt(n)
        while i < int(n ** 0.5) + 1:
            if n % i == 0:
                return False
            i += 2
        return True

    # Returns list of primes less than n
    def primes_below(self, limit: int) -> list:
        return [i for i in range(limit) if self.is_prime(i)]


# Class for displaying results with a title
class Display:

    # Initialization with a title string
    def __init__(self, title: str):
        self.title = title

    # Prints the results in a formatted way
    def show(self, message: str):
        print(f"[{self.title}]: {message}")


# Main function: finds all primes below 1,000,000 and displays
def main():
    prime_utils = PrimeChecker()
    display = Display("Prime Checker")
    limit = 1000000
    primes = prime_utils.primes_below(limit)
    display.show(f"Prime numbers below {limit} => {primes}")


# Check for script entry point using decoded "__main__"
if __name__ == "__main__":
    main()