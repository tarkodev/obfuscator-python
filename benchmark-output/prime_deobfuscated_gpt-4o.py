# Define a function to decode a Base64 encoded string
def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')

# Define a class to perform prime-related operations
class PrimeChecker:
    
    # Check if a given integer is a prime number
    def is_prime(self, number: int) -> bool:
        # Quick cases for small numbers
        if number <= 1:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        # Check divisibility by odd numbers up to sqrt(number)
        divisor = 3
        while divisor < int(number ** 0.5) + 1:
            if number % divisor == 0:
                return False
            divisor += 2
        return True

    # Return a list of prime numbers up to a given limit
    def primes_up_to(self, limit: int) -> list:
        return [num for num in range(limit) if self.is_prime(num)]

# Define a class to manage a title and display messages
class MessageLogger:

    # Initialize with a title
    def __init__(self, title: str):
        self.title = title

    # Print a message prefixed by the title
    def log(self, message: str):
        print(f"[{self.title}]: {message}")

# Function to check and display prime numbers up to a limit
def main():
    prime_checker = PrimeChecker()
    logger = MessageLogger(_obf_decode('UHJpbWUgQ2hlY2tlcg=='))  # "Prime Checker"
    limit = 1000000
    primes_list = prime_checker.primes_up_to(limit)
    logger.log(
        f"{_obf_decode('UHJpbWUgbnVtYmVycyBiZWxvdyA=')}"  # "Prime numbers below "
        f"{limit} => {primes_list}"
    )

# Ensure the main function runs if this is the main module
if __name__ == "__main__":
    main()