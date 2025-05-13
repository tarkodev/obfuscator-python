# Research Project (TER): Python Code Obfuscator

**Protect your Python source code with state-of-the-art AST transformations and GPT-powered de-obfuscation.**

---

## Main CLI Tools

### 1. Obfuscator (`main.py`)

Apply any combination of AST-based transformations:

```bash
python -m obfuscator.main --input ./benchmark_input/fibonacci_input.py  --output ./benchmark_output/fibonacci_obfuscated.py  --transformations remove_all_comments rename_identifiers add_dead_code restructure_loops obfuscate_strings
```

_All transformations are optional and can be mixed or applied individually._

### 2. GPT De-obfuscator (`main.py --gpt`)

Request ChatGPT to analyze and rewrite:

```bash
python -m obfuscator.main  --input ./benchmark_output/fibonacci_obfuscated.py  --output ./benchmark_output/fibonacci_deobfuscated_gpt-4o.py  --gpt  --model gpt-4o
```

### 3. End-to-End Benchmark (`benchmark.py`)

Run performance and correctness tests across the pipeline:

```bash
python benchmark.py  --input-dir benchmark_input  --output-dir benchmark_output  --models gpt-4o o4-mini
```

After completion, detailed timing and comparison reports are saved under `benchmark_output/benchmark-<model>.txt`.

---

## How It Works

The obfuscator works by:

- **Renaming Identifiers:** Replaces variable, function, and class names with meaningless ones.  
- **Inserting Dead Code:** Adds non-functional blocks to confuse reverse engineering.  
- **Removing Comments:** Strips all comments and docstrings.  
- **Restructuring Loops:** Converts `for`-loops into `while`-loops.  
- **Obfuscating Strings:** Encodes string literals in Base64, decoded at runtime.  
- **Wrapping Full File:** Encodes entire script into Base64+hex and executes via `exec()`.

---

## Programmatic API

Import and apply transformations in your Python code:

```python
import ast
from obfuscator.transformations.rename_identifiers import RenameIdentifiers
from obfuscator.transformations.add_dead_code import AddDeadCode
from obfuscator.transformations.restructure_loops import RestructureLoops
from obfuscator.transformations.obfuscate_strings import ObfuscateStrings, insert_helper_function
from obfuscator.transformations.remove_all_comments import remove_all_comments
from obfuscator.transformations.wrap_code_base64_hex_exec import WrapCodeBase64HexExec
from obfuscator.gpt import call_chatgpt_for_analysis_and_code

# Load source
with open("script.py", "r", encoding="utf-8") as f:
    source = f.read()

# Optionally remove comments
clean = remove_all_comments(source)

# Build AST
tree = ast.parse(clean)

# Choose and apply transformations
transforms = [RenameIdentifiers(), AddDeadCode(), RestructureLoops()]
tree = apply_transformations(tree, transforms)

# Optionally obfuscate strings
tree = insert_helper_function(tree)
tree = ObfuscateStrings().visit(tree)

# Optionally wrap full file
wrapped_code = WrapCodeBase64HexExec().transform_source(ast.unparse(tree))

# Use GPT de-obfuscation
clean_code = call_chatgpt_for_analysis_and_code(wrapped_code, model_name="gpt-4o")
print(clean_code)
```

---

## Setup & Requirements

1. **Git Clone**  
   ```bash
   git clone https://github.com/tarkodev/python-code-obfuscator.git
   cd python-code-obfuscator
   ```

2. **Environment Variables**  
   Create a `.env` file in the project root with your OpenAI key:  
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

3. **Install Requirements**  
   ```bash
   pip install -r requirements.txt
   ```

---

## License

This project is open-source and available for everyone to use, modify, and distribute freely.
