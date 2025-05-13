# Function to decode a base64 encoded string
def decode_base64(s):
    import base64
    return base64.b64decode(s).decode('utf-8')

# Class to perform palindrome checking
class PalindromeChecker:
    # Method to check if a given string is a palindrome
    def is_palindrome(self, text: str) -> bool:
        # Join alphanumeric characters from the string in lowercase
        cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
        # Check if the cleaned string is equal to its reverse
        return cleaned_text == cleaned_text[::-1]

    # Method to create a dictionary to check palindrome status of a list of strings
    def check_palindromes(self, text_list: list) -> dict:
        # Return a dictionary with each string and its palindrome status
        return {text: self.is_palindrome(text) for text in text_list}

# Class to print results based on a title
class ResultPrinter:
    # Initialize with a title
    def __init__(self, title: str):
        self.title = title

    # Method to print a message with the title
    def print_result(self, message: str):
        print(f"[{self.title}]: {message}")

# Main function to execute the checking and printing
def main():
    # Create instances of the classes
    palindrome_checker = PalindromeChecker()
    result_printer = ResultPrinter(decode_base64('UGFsaW5kcm9tZSBDaGVja2Vy'))
    
    # List of test strings decoded from base64
    test_strings = [
        decode_base64('cmFkYXI='),
        decode_base64('aGVsbG8='),
        decode_base64('QSBtYW4gYSBwbGFuIGEgY2FuYWwgUGFuYW1h'),
        decode_base64('MTIzMjE='),
        decode_base64('UHl0aG9u'),
        decode_base64('a2F5YWs='),
        decode_base64('eWFrYWs=')
    ]
    
    # Get palindrome status for each test string
    palindrome_results = palindrome_checker.check_palindromes(test_strings)
    
    # Loop through results and print each
    for text, is_palindrome in palindrome_results.items():
        result = "is" if is_palindrome else "is not"
        result_printer.print_result(f"'{text}' {result} a palindrome.")

# Execute main function if the script is run directly
if __name__ == "__main__":
    main()