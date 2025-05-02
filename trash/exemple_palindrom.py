# example_input.py
"""
Example Python script that checks if strings are palindromes
and displays the results using a helper class.
"""

class PalindromeChecker:
    """
    Checks whether a given string is a palindrome.
    """
    def is_palindrome(self, text: str) -> bool:
        """
        Returns True if the string is a palindrome, ignoring spaces and case.
        """
        cleaned = ''.join(c.lower() for c in text if c.isalnum())
        return cleaned == cleaned[::-1]

    def test_cases(self, cases: list) -> dict:
        """
        Tests a list of strings and returns a dictionary with the results.
        """
        return {text: self.is_palindrome(text) for text in cases}

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
    checker = PalindromeChecker()
    helper = DisplayHelper("Palindrome Checker")

    cases = ["radar", "hello", "A man a plan a canal Panama", "12321", "Python", "kayak", "yakak"]
    results = checker.test_cases(cases)
    for text, is_pal in results.items():
        verdict = "is" if is_pal else "is not"
        helper.show_message(f"'{text}' {verdict} a palindrome.")

if __name__ == "__main__":
    main()
