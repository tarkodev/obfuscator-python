# Decodes a base64-encoded string and returns its UTF-8 string value
def _obf_decode(s):
    import base64
    # 's' is a base64-encoded string; decode to bytes, then to UTF-8 string
    return base64.b64decode(s).decode('utf-8')


# The following dead code is never executed
if False:
    _obf_decode('RGVhZCBjb2RlIGF0IG1vZHVsZSBsZXZlbA==')  # "Dead code at module level"


# Class with palindrome-checking logic
class PalindromeChecker:

    # Checks if the input string (alphanumeric only, case-insensitive) is a palindrome
    def is_palindrome(self, word: str) -> bool:
        # Unreachable, dead code
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))  # "This is dead code"

        # Dead never-used function
        def unused_function_5948():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        # Join the lowercase alphanumeric characters of 'word' into a new string
        filtered = ''.join(ch.lower() for ch in word if ch.isalnum())
        # Return True if 'filtered' is same as its reverse (i.e., palindrome)
        return filtered == filtered[::-1]

    # Takes a list of strings and returns a dictionary mapping each to True/False for being palindrome
    def check_list(self, words: list) -> dict:
        # Unreachable, dead code
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))  # "This is dead code"

        # Unused function, dead code
        def unused_function_9404():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        # Return {word: is_palindrome(word) for word in words}
        return {word: self.is_palindrome(word) for word in words}


# Class for outputting results with a given title
class ResultPrinter:

    # Initializer; stores 'title'
    def __init__(self, title: str):
        # Unreachable, dead code
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))  # "This is dead code"

        # Unused function, dead code
        def unused_function_1058():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        # Save title
        self.title = title

    # Prints a formatted result, using 'title' and a result string
    def print_result(self, result: str):
        # Unreachable dead code
        if False:
            print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))  # "This is dead code"

        # Unused function, dead code
        def unused_function_6493():
            _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
            return 42
        # Output in format: [Title]: result
        print(
            f"{_obf_decode('Ww==')}{self.title}{_obf_decode('XTog')}{result}"
        )


# Main routine to check palindromes and print results
def main():
    # Unreachable dead code
    if False:
        print(_obf_decode('VGhpcyBpcyBkZWFkIGNvZGU='))  # "This is dead code"

    # Unused function, dead code
    def unused_function_5403():
        _obf_decode('QSB1c2VsZXNzIGZ1bmN0aW9u')
        return 42
    # Create palindrome checker
    checker = PalindromeChecker()
    # Create result printer with given title
    printer = ResultPrinter(_obf_decode('UGFsaW5kcm9tZSBDaGVja2Vy'))  # "Palindrome Checker"
    # List of test cases (base64 decoded strings)
    words = [
        _obf_decode('cmFkYXI='),         # "radar"
        _obf_decode('aGVsbG8='),         # "hello"
        _obf_decode('QSBtYW4gYSBwbGFuIGEgY2FuYWwgUGFuYW1h'),  # "A man a plan a canal Panama"
        _obf_decode('MTIzMjE='),         # "12321"
        _obf_decode('UHl0aG9u'),         # "Python"
        _obf_decode('a2F5YWs='),         # "kayak"
        _obf_decode('eWFrYWs=')          # "yakyak"
    ]
    # Compute palindromicity of each word
    results = checker.check_list(words)
    for word, is_palindrome in results.items():
        # Choose correct translation to "is" or "is not"
        status = _obf_decode('aXM=') if is_palindrome else _obf_decode('aXMgbm90')  # "is", "is not"
        # Compose the message: "'word' is (not) a palindrome."
        printer.print_result(
            f"{_obf_decode('Jw==')}{word}{_obf_decode('JyA=')}{status}{_obf_decode('IGEgcGFsaW5kcm9tZS4=')}"
            # "'word' is a palindrome." or "'word' is not a palindrome."
        )


# Run the main routine if this is the main program
if __name__ == "__main__":
    main()
