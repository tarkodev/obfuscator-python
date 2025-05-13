# obfuscator/gpt.py

# This module integrates with the OpenAI ChatGPT API to analyze and de-obfuscate
# Python code. It sends obfuscated source code to ChatGPT and retrieves both
# a commented analysis and a clean, executable rewrite.

import os                         # For interacting with environment variables
import openai                     # OpenAI Python client for API access
from dotenv import load_dotenv    # Utility to load .env files into os.environ

# Load environment variables from a .env file in the current directory
load_dotenv()

# Retrieve the OpenAI API key from the environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# Configure the OpenAI client with the retrieved key
openai.api_key = OPENAI_API_KEY

def call_chatgpt_for_analysis_and_code(
    obfuscated_code: str,
    model_name: str = "gpt-4o"
) -> str:
    """
    Sends obfuscated Python code to ChatGPT and requests:
      1. A brief analysis inserted as Python comments above or inline with the code.
      2. A full rewrite of the code in a clean, readable, and executable format.

    :param obfuscated_code: The obfuscated source code to analyze.
    :param model_name: The ChatGPT model to use (default "gpt-4o").
    :return: The raw text response from ChatGPT, expected to be valid Python code.
    """

    # If no API key is provided, skip making the API call and warn in a comment
    if not OPENAI_API_KEY:
        return "# No API key found. Skipping ChatGPT analysis.\n"

    # Construct the prompt that will be sent to ChatGPT:
    # - We specify the assistant role as a Python helper.
    # - We ask for two outputs: commented analysis and clean rewrite.
    # - We emphasize no markdown formatting, only plain Python code.
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

    # Send the prompt to the ChatGPT API, using the specified model and user role
    response = openai.chat.completions.create(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
    )

    # Extract and return the content of the first message choice
    return response.choices[0].message.content
