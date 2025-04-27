#run aiocli inline "Hello, world!" command

import os
import sys

import subprocess

# Get the absolute path to aiocli.py
script_dir = os.path.dirname(os.path.abspath(__file__))  # Current script directory
aiocli_path = os.path.join(script_dir, "../aiocli.py")   # Path to aiocli.py

subprocess.run([
    "pip",  "install", "typer[all]"
], check=True)


subprocess.run([
    sys.executable, aiocli_path, "inline", "What is Azure OpenAI?",
], check=True)