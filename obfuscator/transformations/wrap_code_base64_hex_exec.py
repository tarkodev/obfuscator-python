# obfuscator/transformations/wrap_code_base64_hex_exec.py

# Import the AST module (not directly used here but commonly needed for AST-based transforms)
import ast

# Import Base64 utilities to encode and decode byte sequences
import base64

# Import textwrap to clean up indentation in multi-line string literals
import textwrap

class WrapCodeBase64HexExec:
    """
    Encodes an entire source file into a hexadecimal representation of its
    Base64-encoded bytes, then reconstructs and executes the original code
    at runtime using exec().
    """

    def transform_source(self, source: str) -> str:
        # Step 1: Convert the source code string into raw bytes (UTF-8 by default)
        b64_bytes = base64.b64encode(source.encode())
        #    - source.encode() turns 'source' into bytes
        #    - base64.b64encode(...) returns Base64-encoded bytes, e.g. b'aGVsbG8='

        # Step 2: Build a flat string of 'xHH' sequences for each byte in the Base64 result
        hex_encoded = ''.join(
            f"x{byte:02x}"       # Format each byte as two lowercase hex digits prefixed by 'x'
            for byte in b64_bytes # Iterate over each integer byte in the b64_bytes sequence
        )

        # Step 3: Assemble a self-decoding Python snippet that will run at runtime
        wrapped = textwrap.dedent(f"""
            import base64
            # Define the hex-encoded Base64 string literal
            s = "{hex_encoded}"
            # Replace each 'x' with '\\x' so Python interprets them as byte escapes
            s = s.replace("x", "\\\\x")
            # Evaluate s as a bytes literal (e.g. b'\\x61\\x47...') and Base64-decode it
            decoded = base64.b64decode(eval(f"b'{{s}}'"))
            # Decode the resulting bytes back to a UTF-8 string
            exec(decoded.decode())
        """).strip()
        #    - textwrap.dedent(...) removes any common leading whitespace
        #    - .strip() trims leading/trailing blank lines

        # Step 4: Return the fully constructed wrapper code
        return wrapped
