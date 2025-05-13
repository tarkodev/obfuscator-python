# TER - Python Code Obfuscator

A powerful tool to protect your Python source code using advanced AST transformations. It obfuscates your code while ensuring it still runs as intended.

## Overview

The obfuscator works by:
- **Renaming Identifiers:** Replaces variable, function, and class names with meaningless ones.
- **Inserting Dead Code:** Adds non-functional blocks to confuse reverse engineering.
- **Removing Comments:** Strips all comments and docstrings.
- **Restructuring Loops:** Converts for-loops into while-loops.
- **Obfuscating Strings:** Encodes string literals in Base64, decoded at runtime.

## How to Use

To run a full benchmark of the obfuscation pipeline, use the `test.py` script:

```bash
python benchmark.py
```

Upon execution, you will be prompted to select a model (e.g., `gpt-4o`, `o4-mini`). The script will then proceed to:
1. Locally obfuscate the source files.
2. Use the selected model to deobfuscate the code.
3. Execute and compare the output and performance.

### Requirements

Before running `test.py`, make sure to:

1. Create a `.env` file in the root directory.
2. Add your OpenAI API key:

```
OPENAI_API_KEY=your-api-key-here
```

This is necessary for the GPT deobfuscation step to work properly.

## License

This project is open-source and available for everyone to use, modify, and distribute freely.