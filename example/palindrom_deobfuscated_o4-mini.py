# Define a utility class for palindrome checking
class PalindromeUtility:
    # Check if a given string is a palindrome
    def is_palindrome(self, text: str) -> bool:
        # Normalize text: lowercase and filter alphanumeric
        cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
        # Compare cleaned string to its reverse
        return cleaned == cleaned[::-1]

    # Check a list of strings for palindrome property
    def check_list(self, texts: list[str]) -> dict[str, bool]:
        # Return a dict mapping each text to its palindrome check result
        return {text: self.is_palindrome(text) for text in texts}


# Define a printer class to display messages with a title
class MessagePrinter:
    # Initialize with a title for messages
    def __init__(self, title: str):
        self.title = title

    # Print a formatted message
    def print_message(self, message: str):
        print(f"[{self.title}]: {message}")


# Main function to coordinate palindrome checking and printing
def main():
    # Instantiate the utility and printer
    checker = PalindromeUtility()
    printer = MessagePrinter("Palindrome Checker")

    # List of sample texts to check
    samples = [
        "radar",
        "hello",
        "A man a plan a canal Panama",
        "12321",
        "Python",
        "kayak",
        "yakak"
    ]

    # Perform palindrome checks
    results = checker.check_list(samples)

    # Print results for each sample
    for text, is_pal in results.items():
        # Choose 'is' or 'is not' based on result
        status = "is" if is_pal else "is not"
        # Format the message with quotes and note about palindrome
        message = f"'{text}' {status} a palindrome."
        printer.print_message(message)


# Entry point
if __name__ == "__main__":
    main()