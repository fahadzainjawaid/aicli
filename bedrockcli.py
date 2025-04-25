import typer
import os
import sys



import bedrock

app = typer.Typer(name="genAIcli", help="CLI for interacting with Bedrock AI")

@app.command()
def interactive():
    """
    Interactive mode: Prompt user for input and display Bedrock response.

    Example:
        python bedrockcli.py interactive
    """
    client = bedrock.BedrockClient()
    while True:
        prompt = input("Enter your prompt (or type 'exit' to quit): ")
        if prompt.lower() == "exit":
            print("Exiting interactive mode.")
            break
        try:
            response = client.send_prompt(prompt)
            print("Response from Bedrock:")
            print(response)
        except Exception as e:
            print(f"An error occurred: {e}")

@app.command()
def inline(
    prompt: str = typer.Argument(..., help="The prompt to send to Bedrock. Example: 'What is the capital of France?'")
):
    """
    Inline mode: Send a single prompt to Bedrock and display the response.

    Example:
        python bedrockcli.py inline "What is the capital of France?"
    """
    client = bedrock.BedrockClient()
    try:
        response = client.send_prompt(prompt)
        print("Response from Bedrock:")
        print(response)
    except Exception as e:
        print(f"An error occurred: {e}")

@app.command()
def promptFile(
    file_path: str = typer.Argument(..., help="Path to the text file containing the prompt. Example: '/path/to/prompt.txt'")
):
    """
    PromptFile mode: Read a prompt from a file and send it to Bedrock.

    Example:
        python bedrockcli.py promptFile /path/to/prompt.txt
    """
    client = bedrock.BedrockClient()
    try:
        with open(file_path, "r") as file:
            prompt = file.read().strip()
        response = client.send_prompt(prompt)
        print("Response from Bedrock:")
        print(response)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    app()