# The function decodes a Base64 encoded string to a UTF-8 string
def decode_base64(s):
    import base64
    return base64.b64decode(s).decode('utf-8')

# The class checks if a string is a palindrome and converts a list of strings into a dictionary with boolean values
class PalindromeChecker:

    # The function checks if a given string is a palindrome, ignoring non-alphanumeric characters
    def is_palindrome(self, text: str) -> bool:
        # Whitespace removed and lowercase conversion for non-alphanumeric characters to check palindrome
        filtered_text = ''.join(char.lower() for char in text if char.isalnum())
        return filtered_text == filtered_text[::-1]

    # The function processes a list of strings and returns a dictionary with the string as the key and whether it is a palindrome as the value
    def check_palindromes(self, words: list) -> dict:
        return {word: self.is_palindrome(word) for word in words}

# This class initializes an object with a title and prints messages
class Checker:

    # Initializes the Checker object with a title
    def __init__(self, title: str):
        self.title = title

    # The function prints the title and a given message
    def print_message(self, message: str):
        print(f"[{self.title}]: {message}")

# This function executes the palindrome check logic and prints results
def main():
    checker = PalindromeChecker()
    printer = Checker(decode_base64('UGFsaW5kcm9tZSBDaGVja2Vy'))
    words = [decode_base64('cmFkYXI='), decode_base64('aGVsbG8='), 
             decode_base64('QSBtYW4gYSBwbGFuIGEgY2FuYWwgUGFuYW1h'), 
             decode_base64('MTIzMjE='), decode_base64('UHl0aG9u'), 
             decode_base64('a2F5YWs='), decode_base64('eWFrYWs=')]
    results = checker.check_palindromes(words)
    for word, is_palindrome in results.items():
        status = decode_base64('aXM=') if is_palindrome else decode_base64('aXMgbm90')
        printer.print_message(f"'{word}' {status} a palindrome.")

# If this script is the main script being executed, run the main function
if __name__ == '__main__':
    main()