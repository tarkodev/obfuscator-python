# TER - Python Code Obfuscator

A powerful tool to protect your Python source code using advanced AST transformations. It obfuscates your code while ensuring it still runs as intended.

## Overview

The obfuscator works by:
- **Renaming Identifiers:** Replaces variable, function, and class names with meaningless ones.
- **Inserting Dead Code:** Adds non-functional blocks to confuse reverse engineering.
- **Removing Comments:** Strips all comments and docstrings.
- **Restructuring Loops:** Converts for-loops into while-loops.
- **Obfuscating Strings:** Encodes string literals in Base64, decoded at runtime.

## Installation

You can run `test.py` for testing purpose^^