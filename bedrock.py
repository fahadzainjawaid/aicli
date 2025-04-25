#work in progress

import os
import boto3

class BedrockClient:
    def __init__(self, model_id=None, region=None, max_retries=3):
            """
            Initialize the Bedrock client.
            
            Args:
                model_id (str): The ID of the model to use (defaults to settings)
                region (str): AWS region (defaults to settings)
                max_retries (int): Maximum number of retry attempts for transient errors
            """
            self.model_id = model_id or os.environ.get('BEDROCK_MODEL_ID', 'anthropic.claude-3-haiku-20240307-v1:0')
            self.region = region or os.environ.get('BEDROCK_REGION', 'ca-central-1')
            self.max_retries = max_retries

            self.max_tokens = os.environ.get('BEDROCK_MAX_TOKENS', 512)
            self.temperature = os.environ.get('BEDROCK_TEMPERATURE', 0.5)
            self.top_p = os.environ.get('BEDROCK_TOP_P', 0.9)
            
            # Get credentials from connectors
            aws_access_key = os.environ.get('BEDROCK_ACCESS_KEY', None)
            aws_secret_access_key = os.environ.get('BEDROCK_SECRET_KEY', None)
            endpoint_url = os.environ.get('BEDROCK_ENDPOINT_URL', "https://bedrock-runtime.ca-central-1.amazonaws.com")

            try:
                # Initialize client with proper credentials
                if aws_access_key and aws_secret_access_key:
                    self.bedrock_runtime = boto3.client(
                        service_name='bedrock-runtime',
                        region_name=self.region,
                        aws_access_key_id=aws_access_key,
                        aws_secret_access_key=aws_secret_access_key,
                        endpoint_url=endpoint_url
                    )
                else:
                    # Use instance profile or environment variables
                    self.bedrock_runtime = boto3.client(
                        service_name='bedrock-runtime',
                        region_name=self.region,
                        endpoint_url=endpoint_url
                    )
                    
                print(f"Initialized Bedrock client with model {self.model_id} in region {self.region}")
            except Exception as e:
                print(f"Failed to initialize Bedrock client: {str(e)}")
                raise

    def send_prompt(self, prompt):
        """
        Simulates sending a prompt to the Bedrock client and receiving a response.

        Args:
            prompt (str): The input prompt string.

        Returns:
            str: A simulated response from the Bedrock client.
        """
        if not prompt:
            raise ValueError("Prompt cannot be empty.")


        user_message = prompt
        conversation = [
            {
                "role": "user",
                "content": [{"text": user_message}],
            }
        ]

        client = self.bedrock_runtime



        try:
            # Send the prompt to the Bedrock runtime
            response = client.converse(
                modelId=self.model_id,
                messages=conversation,
                inferenceConfig={"maxTokens": self.max_tokens, "temperature": self.temperature, "topP": self.top_p},
            )

            # Extract and print the response text.
            response_text = response["output"]["message"]["content"][0]["text"]
            return response_text

        except Exception as e:
            print(f"An error occurred while sending the prompt: {str(e)}")
            raise