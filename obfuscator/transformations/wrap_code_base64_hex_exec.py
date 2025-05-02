# obfuscator/transformations/wrap_code_base64_hex_exec.py
import ast
import base64
import textwrap

class WrapCodeBase64HexExec:
    """
    Encode tout le fichier:
      1. bytes → base64
      2. base64 → suite 'xHH'
    Puis reconstruit/décode à l’exécution et exec.
    """
    def transform_source(self, source: str) -> str:
        # 1) source → base64 bytes
        b64_bytes = base64.b64encode(source.encode())          # b'aGVsbG8='
        # 2) base64 → "x61x47x56x73..."
        hex_encoded = ''.join(f"x{byte:02x}" for byte in b64_bytes)
        wrapped = textwrap.dedent(f"""
            import base64
            s = "{hex_encoded}"
            s = s.replace("x", "\\\\x")                  # '\\x61\\x47...'
            decoded = base64.b64decode(eval(f"b'{{s}}'"))
            exec(decoded.decode())
        """).strip()
        return wrapped
