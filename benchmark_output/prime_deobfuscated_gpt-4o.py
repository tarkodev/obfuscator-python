# Define a helper function to decode a base64-encoded string
def decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')

# Class to handle operations related to prime numbers
class PrimeChecker:

    # Method to check if a number is prime
    def is_prime(self, number: int) -> bool:
        # Check for numbers <= 1
        if number <= 1:
            return False
        # Check if the number is 2
        if number == 2:
            return True
        # Check if the number is even
        if number % 2 == 0:
            return False
        # Check for factors from 3 to sqrt(number)
        factor = 3
        while factor < int(number ** 0.5) + 1:
            if number % factor == 0:
                return False
            factor += 2
        return True

    # Method to generate a list of prime numbers up to a given limit
    def prime_numbers_up_to(self, limit: int) -> list:
        # Return primes within the range using list comprehension
        return [number for number in range(limit) if self.is_prime(number)]

# Class for presenting messages with a title
class Presenter:

    # Initialize with a title
    def __init__(self, title: str):
        self.title = title

    # Method to display a message with the title
    def show_message(self, message: str):
        print(f"[{self.title}]: {message}")

# Main function to demonstrate prime number checking and presentation
def main():
    prime_checker = PrimeChecker()
    presenter = Presenter("Prime Checker")
    limit = 1000000
    primes_below_limit = prime_checker.prime_numbers_up_to(limit)
    presenter.show_message(f"Prime numbers below {limit} => {primes_below_limit}")

# Check if the script is being run directly
if __name__ == "__main__":
    main()