
##WORK IN PROGRESS##

import sys
import os

import requests
from bs4 import BeautifulSoup

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../compliance"))
sys.path.insert(0, project_root)

print (f"Project root: {project_root}")

import bedrock






class GenerateControlSetDescFromBedrock:

    @staticmethod
    def interactive():
        # Create a new Bedrock client
        client = bedrock.BedrockClient()
        client.__init__(model_id="anthropic.claude-3-haiku-20240307-v1:0", region="ca-central-1")

        # Define the input prompt string
        promptString = input("Enter your prompt: ")

        # Send the prompt to the Bedrock client and get the response
        try:
            response = client.send_prompt(promptString)
            print("Response from Bedrock client:")
            print(response)
        except Exception as e:
            print(f"An error occurred: {e}")

    ##write a method that uses the "sendprompt and collects repsponses "

    @staticmethod
    def parse_web(url, prompt):
        """
        Fetches content from a website URL, uses it as context, and sends the combined
        context and prompt to the Bedrock client.

        Args:
            url (str): The URL of the website to parse.
            prompt (str): The question or prompt to ask based on the website content.

        Returns:
            str: The response from the Bedrock client.
        """
        try:
            # Fetch the content of the website
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for HTTP issues

            # Parse the website content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            text_content = soup.get_text(separator=' ', strip=True)

            # Combine the website content with the prompt
            context_prompt = f"Context: {text_content}\n\nQuestion: {prompt}"

            # Create a new Bedrock client
            client = bedrock.BedrockClient()

            # Send the combined context and prompt to the Bedrock client
            bedrock_response = client.send_prompt(context_prompt)

            return bedrock_response

        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching the URL: {e}")
            raise
        except Exception as e:

            print(f"An error occurred: {e}")
            raise
        finally:
            # Optionally, you can close any resources or connections here
            pass


if __name__ == "__main__":
    # Ensure the script runs only when executed directly



    GenerateControlSetDescFromBedrock.interactive()
