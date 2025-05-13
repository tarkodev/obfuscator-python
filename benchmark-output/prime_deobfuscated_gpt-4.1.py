# Decodes a base64-encoded string to UTF-8 text
def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')

# Prime checking and listing class
class PrimeChecker:
    # Checks if a number is prime
    def is_prime(self, n: int) -> bool:
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i < int(n ** 0.5) + 1:
            if n % i == 0:
                return False
            i += 2
        return True

    # Returns a list of all prime numbers below a given limit
    def primes_below(self, limit: int) -> list:
        return [i for i in range(limit) if self.is_prime(i)]

# Class for pretty printing outputs with a title
class OutputPrinter:
    # Assigns a title for subsequent print statements
    def __init__(self, title: str):
        self.title = title

    # Prints the title along with a supplied text
    def print_with_title(self, text: str):
        print(f"[{self.title}]: {text}")

# Main execution function
def main():
    prime_checker = PrimeChecker()
    printer = OutputPrinter("Prime Checker")
    limit = 1000000
    primes = prime_checker.primes_below(limit)
    printer.print_with_title(f"Prime numbers below {limit} => {primes}")

# Executes main if this script is run directly
if __name__ == "__main__":
    main()