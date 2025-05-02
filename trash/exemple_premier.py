# example_input.py
"""
Example Python script that checks prime numbers
and displays the result using a helper class.
"""

class PrimeChecker:
    """
    Checks if a number is prime.
    """
    def is_prime(self, n: int) -> bool:
        """
        Returns True if n is a prime number, False otherwise.
        """
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def get_primes_up_to(self, limit: int) -> list:
        """
        Returns a list of prime numbers up to the given limit (exclusive).
        """
        return [i for i in range(limit) if self.is_prime(i)]

class DisplayHelper:
    """
    Helper class to display formatted messages.
    """
    def __init__(self, title: str):
        self.title = title

    def show_message(self, message: str):
        """
        Prints a formatted message with a title.
        """
        print(f"[{self.title}]: {message}")

def main():
    checker = PrimeChecker()
    helper = DisplayHelper("Prime Checker")

    limit = 30
    primes = checker.get_primes_up_to(limit)
    helper.show_message(f"Prime numbers below {limit} => {primes}")

if __name__ == "__main__":
    main()
