# Compute Fibonacci number recursively (original var_cpyqz_2)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Generate the Fibonacci sequence of given length (original var_qztin_5)
def fibonacci_sequence(length: int) -> list[int]:
    return [fibonacci(i) for i in range(length)]

# Class handling title and printing (original var_ozbuk_8)
class Program:
    def __init__(self, title: str):
        self.title = title

    # Print a message prefixed with the program title (original var_tuwmd_9)
    def print_message(self, message: str) -> None:
        print(f"[{self.title}]: {message}")

# Main execution flow (original var_cgihi_11)
def main() -> None:
    length = 35
    sequence = fibonacci_sequence(length)
    program = Program("Fibonacci Program")
    program.print_message(f"Fibonacci sequence of length {length} => {sequence}")

# Entry point check (original if __name__ == '__main__')
if __name__ == "__main__":
    main()