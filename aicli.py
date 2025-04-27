import typer
from OpenAIClient import OpenAIClient
from bedrock import BedrockClient
import requests

app = typer.Typer(name="aicli", help="CLI for interacting with AI services (AWS Bedrock or Azure OpenAI)")

def get_client(service: str):
    """
    Returns the appropriate client based on the service parameter.

    Args:
        service (str): The service to use ("awsbedrock" or "azopenai").

    Returns:
        object: An instance of the relevant client.
    """
    if service == "azopenai":
        return OpenAIClient()
    elif service == "awsbedrock":
        return BedrockClient()
    else:
        raise ValueError(f"Unsupported service: {service}")

@app.command()
def interactive(
    service: str = typer.Option("awsbedrock", help="The service to use (awsbedrock or azopenai).")
):
    """
    Interactive mode: Prompt user for input and display AI response.

    Example:
        python aicli.py interactive --service azopenai
    """
    client = get_client(service)
    while True:
        prompt = input("Enter your prompt (or type 'exit' to quit): ")
        if prompt.lower() == "exit":
            print("Exiting interactive mode.")
            break
        try:
            response = client.send_prompt(prompt)
            print("Response:")
            print(response)
        except Exception as e:
            print(f"An error occurred: {e}")

@app.command()
def inline(
    prompt: str = typer.Argument(..., help="The prompt to send to the AI service."),
    service: str = typer.Option("awsbedrock", help="The service to use (awsbedrock or azopenai).")
):
    """
    Inline mode: Send a single prompt to the AI service and display the response.

    Example:
        python aicli.py inline "What is the capital of France?" --service azopenai
    """
    client = get_client(service)
    try:
        response = client.send_prompt(prompt)
        print("Response:")
        print(response)
    except Exception as e:
        print(f"An error occurred: {e}")

@app.command()
def promptFile(
    file_path: str = typer.Argument(..., help="Path to the text file containing the prompt."),
    service: str = typer.Option("awsbedrock", help="The service to use (awsbedrock or azopenai).")
):
    """
    PromptFile mode: Read a prompt from a file and send it to the AI service.

    Example:
        python aicli.py promptFile /path/to/prompt.txt --service azopenai
    """
    client = get_client(service)
    try:
        with open(file_path, "r") as file:
            prompt = file.read().strip()
        response = client.send_prompt(prompt)
        print("Response:")
        print(response)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

@app.command()
def urlParse(
    url: str = typer.Argument(..., help="The URL of the page to fetch content from."),
    prompt: str = typer.Argument(..., help="The prompt to send to the AI service."),
    service: str = typer.Option("awsbedrock", help="The service to use (awsbedrock or azopenai).")
):
    """
    urlParse mode: Fetch content from a URL and use the AI service to answer questions based on the content.

    Example:
        python aicli.py urlParse "https://example.com" "Summarize this page" --service azopenai
    """
    client = get_client(service)
    try:
        # Fetch the content of the URL
        response = requests.get(url)
        response.raise_for_status()
        page_content = response.text
        
        print("Fetched content from URL:")
        print(page_content[:500])  # Print the first 500 characters of the content

        # Combine the page content with the prompt
        combined_prompt = f"Based on the following content from the URL:\n\n{page_content}\n\n{prompt}"

        # Send the combined prompt to the AI service
        ai_response = client.send_prompt(combined_prompt)
        print("Response:")
        print(ai_response)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL content: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
    
if __name__ == "__main__":
    app()
    
