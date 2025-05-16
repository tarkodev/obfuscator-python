# This function decodes a base64-encoded string
def decode_base64(s):
    # Import base64 for decoding
    import base64
    # Decode and return the string as UTF-8
    return base64.b64decode(s).decode('utf-8')

# This class provides methods to check palindromes
class PalindromeChecker:
    # Checks if a single string is a palindrome
    def is_palindrome(self, text: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
        # Compare the string with its reverse
        return cleaned == cleaned[::-1]

    # Checks a list of strings, returning a dict of string -> bool
    def check_list(self, items: list) -> dict:
        # Map each string to the result of is_palindrome
        return {item: self.is_palindrome(item) for item in items}

# This class logs messages with a given title
class Logger:
    # Initialize the logger with a title
    def __init__(self, title: str):
        # Store the title
        self.title = title

    # Print a message prefixed with the title
    def print_message(self, message: str):
        # Format and print the message
        print(f"[{self.title}]: {message}")

# Main function to demonstrate palindrome checking
def main():
    # Create a PalindromeChecker
    checker = PalindromeChecker()
    # Create a Logger with a title
    logger = Logger("Palindrome Checker")
    # Prepare a list of strings to check
    strings = [
        "radar",
        "hello",
        "A man a plan a canal Panama",
        "12321",
        "Python",
        "kayak",
        "yakak"
    ]
    # Get a dictionary of palindrome results
    results = checker.check_list(strings)
    # Iterate over the results
    for text, is_pal in results.items():
        # Determine if the string is or isn't a palindrome
        verb = "is" if is_pal else "is not"
        # Print the result
        logger.print_message(f"'{text}' {verb} a palindrome.")

# Execute main if script is run directly
if __name__ == "__main__":
    main()