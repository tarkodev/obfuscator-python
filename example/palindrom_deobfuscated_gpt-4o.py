# The function _obf_decode decodes a base64 encoded string to a UTF-8 string.
def _obf_decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


# The class checks if strings in a list are palindromes.
class PalindromeChecker:

    # This method checks if a given string is a palindrome, ignoring non-alphanumeric characters.
    def is_palindrome(self, input_str: str) -> bool:
        stripped_str = ''.join(char.lower() for char in input_str if char.isalnum())
        return stripped_str == stripped_str[::-1]

    # This method returns a dictionary where keys are strings and values indicate if they are palindromes.
    def check_palindromes(self, words: list) -> dict:
        return {word: self.is_palindrome(word) for word in words}


# This class manages a title and prints messages with that title.
class TitlePrinter:

    # Initializes the object with a title.
    def __init__(self, title: str):
        self.title = title

    # Prints a message prefixed by the title.
    def print_message(self, message: str):
        print(f"[{self.title}]: {message}")


# This function creates instances of the classes and checks for palindromes in a list.
def main():
    palindrome_checker = PalindromeChecker()
    title_printer = TitlePrinter("Palindrome Checker")
    
    words = ['radar', 'hello', 'A man a plan a canal Panama', '12321', 'Python', 'kayak', 'yakak']
    results = palindrome_checker.check_palindromes(words)
    
    # For each word, print whether it is a palindrome or not.
    for word, is_palindrome in results.items():
        status = "is" if is_palindrome else "is not"
        title_printer.print_message(f"'{word}' {status} a palindrome.")


# Execute main function only if the script is run as the main program.
if __name__ == "__main__":
    main()