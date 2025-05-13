# define a class to check palindromes
class PalindromeChecker:
    # method to check if a single string is a palindrome
    def is_palindrome(self, text: str) -> bool:
        # remove non-alphanumeric characters and convert to lowercase
        filtered = ''.join(ch.lower() for ch in text if ch.isalnum())
        # compare filtered string to its reverse
        return filtered == filtered[::-1]

    # method to check a list of strings and return results as a dict
    def check_list(self, texts: list) -> dict:
        # build dict mapping each text to its palindrome check result
        return {text: self.is_palindrome(text) for text in texts}

# define a simple logger class for titled messages
class Logger:
    # initialize logger with a title
    def __init__(self, title: str):
        # store the title
        self.title = title

    # method to print a message prefixed by the title
    def log(self, message: str):
        # print the formatted log message
        print(f"[{self.title}]: {message}")

# main execution function
def main():
    # instantiate the palindrome checker
    checker = PalindromeChecker()
    # instantiate the logger with a descriptive title
    logger = Logger("Palindrome Checker")
    # list of test strings to evaluate
    words = [
        "radar",
        "hello",
        "A man a plan a canal Panama",
        "12321",
        "Python",
        "kayak",
        "yakak"
    ]
    # check each string for palindrome property
    results = checker.check_list(words)
    # iterate over each test result and log the outcome
    for word, is_pal in results.items():
        # determine status text based on result
        status = "is" if is_pal else "is not"
        # log the result message
        logger.log(f"'{word}' {status} a palindrome.")

# run main if module is executed as script
if __name__ == "__main__":
    main()
