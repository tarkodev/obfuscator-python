# Imports are not needed since we handle strings directly

# Class for checking palindromes
class PalindromeChecker:
    # Determines if a given string is a palindrome (ignoring non-alphanumeric and case)
    def is_palindrome(self, text: str) -> bool:
        # Clean the text: keep only alphanumeric characters, make lowercase
        processed = ''.join(ch.lower() for ch in text if ch.isalnum())
        # Check if the cleaned text equals its reverse
        return processed == processed[::-1]

    # Processes a list of texts and returns a mapping of each to its palindrome status
    def batch_check(self, texts: list) -> dict:
        return {text: self.is_palindrome(text) for text in texts}

# Logger class for printing messages with a title
class Logger:
    # Initialize with a title to prefix messages
    def __init__(self, title: str):
        self.title = title

    # Print a message prefixed by the title
    def log(self, message: str):
        print(f"[{self.title}]: {message}")

# Main execution function
def main():
    # Instantiate the palindrome checker and logger
    checker = PalindromeChecker()
    logger = Logger("Palindrome Checker")

    # Sample strings to check
    sample_texts = [
        "radar",
        "hello",
        "A man a plan a canal Panama",
        "12321",
        "Python",
        "kayak",
        "yakak"
    ]

    # Check each sample and get results
    results = checker.batch_check(sample_texts)

    # Log the results for each sample
    for text, is_pal in results.items():
        # Determine the appropriate status message
        status = "is" if is_pal else "is not"
        # Log the formatted result
        logger.log(f"'{text}' {status} a palindrome.")

# Entry point check
if __name__ == '__main__':
    main()
