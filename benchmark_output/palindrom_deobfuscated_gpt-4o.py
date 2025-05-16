# Decode a base64 string into a UTF-8 string
def _decode(s):
    import base64
    return base64.b64decode(s).decode('utf-8')


# Class to check if strings are palindromes
class PalindromeChecker:

    # Method to determine if a given string is a palindrome
    def is_palindrome(self, text: str) -> bool:
        # Convert the text to all lowercase and remove non-alphanumeric characters
        processed_text = ''.join(char.lower() for char in text if char.isalnum())
        # Check if the processed text is the same forwards and backwards
        return processed_text == processed_text[::-1]

    # Method to check multiple texts if they are palindromes
    def check_texts(self, texts: list) -> dict:
        # For each text in the list, determine if it is a palindrome
        return {text: self.is_palindrome(text) for text in texts}


# Class to print results with a title
class ResultPrinter:

    # Initialize the ResultPrinter with a title
    def __init__(self, title: str):
        self.title = title

    # Method to print the result message
    def print_result(self, message: str):
        # Print the title followed by the message
        print(f"[{self.title}]: {message}")


# Main function to demonstrate usage
def main():
    # Instantiate the PalindromeChecker
    checker = PalindromeChecker()
    # Create a ResultPrinter with a specific title
    printer = ResultPrinter(_decode('UGFsaW5kcm9tZSBDaGVja2Vy'))
    # List of texts to check
    texts = [
        _decode('cmFkYXI='), _decode('aGVsbG8='),
        _decode('QSBtYW4gYSBwbGFuIGEgY2FuYWwgUGFuYW1h'), _decode('MTIzMjE='),
        _decode('UHl0aG9u'), _decode('a2F5YWs='),
        _decode('eWFrYWs=')
    ]
    # Get results from checking if each text is a palindrome
    results = checker.check_texts(texts)
    # Print results
    for text, is_palindrome in results.items():
        # Choose the appropriate message based on palindrome status
        status = _decode('aXM=') if is_palindrome else _decode('aXMgbm90')
        # Send the result to the printer
        printer.print_result(f"'{text}' {status} a palindrome.")


# Run the main function if the script is executed
if __name__ == '__main__':
    main()