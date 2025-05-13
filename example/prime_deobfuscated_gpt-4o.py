# Define a function to decode a base64 encoded string
def decode_base64_string(s):
    import base64
    return base64.b64decode(s).decode('utf-8')

# Define a class for prime number operations
class PrimeChecker:
    # Method to check if a number is prime
    def is_prime(self, number: int) -> bool:
        # Return False for numbers less than or equal to 1
        if number <= 1:
            return False
        # Return True for 2 as it's the smallest prime number
        if number == 2:
            return True
        # Return False for even numbers greater than 2
        if number % 2 == 0:
            return False
        # Start checking for factors from 3 upwards in odd increments
        factor = 3
        while factor < int(number ** 0.5) + 1:
            # If a factor is found, return False
            if number % factor == 0:
                return False
            factor += 2
        # If no factors are found, return True indicating a prime number
        return True

    # Method to find all prime numbers below a certain limit
    def primes_below(self, limit: int) -> list:
        # Return a list of prime numbers below the specified limit
        return [num for num in range(limit) if self.is_prime(num)]

# Define a class for displaying results
class Display:
    # Initialization method for the Display class
    def __init__(self, title: str):
        self.title = title

    # Method to print a formatted message
    def show_message(self, message: str):
        print(f"[{self.title}]: {message}")

# Main execution function
def main():
    prime_checker = PrimeChecker()
    display = Display(decode_base64_string('UHJpbWUgQ2hlY2tlcg=='))
    limit = 1000000
    # Generate a list of prime numbers below the limit
    prime_numbers_below_limit = prime_checker.primes_below(limit)
    # Display the result
    display.show_message(
        f"Prime numbers below {limit} => {prime_numbers_below_limit}"
    )

# Check if the script is running as the main program
if __name__ == "__main__":
    main()