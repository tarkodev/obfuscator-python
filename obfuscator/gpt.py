# obfuscator/gpt.py
"""
Integration with ChatGPT for code analysis.
This module sends the obfuscated code to the ChatGPT API to obtain:
  1. A brief analysis (as comments).
  2. A clean, readable, and executable Python version.
"""

import os
import openai
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def call_chatgpt_for_analysis_and_code(obfuscated_code: str) -> str:
    """
    Sends the obfuscated code to ChatGPT with a prompt asking for:
      - A brief analysis in comments.
      - A rewritten version of the code that is readable and executable.

    :param obfuscated_code: The obfuscated source code.
    :return: The raw response from ChatGPT.
    """
    if not OPENAI_API_KEY:
        return "# No API key found. Skipping ChatGPT analysis.\n"

    prompt = (
        "You are a Python assistant.\n"
        "You will receive obfuscated Python code.\n"
        "Your task is to:\n"
        "1. Provide a short analysis using Python comments (starting with '#') directly above each relevant line.\n"
        "2. Then rewrite the entire code in a clean, readable, and executable format.\n"
        "IMPORTANT:\n"
        "- The response must be valid Python code and should compile.\n"
        "- Do NOT include markdown formatting or triple backticks.\n"
        "- The analysis should be in the form of inline or top comments only.\n"
        "- Do not include any extra explanations outside the Python script.\n\n"
        f"Obfuscated code:\n{obfuscated_code}"
    )

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content
