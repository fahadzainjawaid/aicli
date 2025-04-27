import os
from openai import AzureOpenAI

OPEN_AI_API_KEY = os.environ.get("AZURE_OPENAI_API_KEY")
AZURE_OPEN_AI_API_KEY = OPEN_AI_API_KEY

AZURE_OPENAI_ENDPOINT = os.environ.get("AZURE_OPENAI_ENDPOINT") or "https://aio-demo.openai.azure.com/"
AZURE_OPENAI_MODEL = os.environ.get("AZURE_OPENAI_MODEL") or "oi4-demo"


client = AzureOpenAI(
    api_key=AZURE_OPEN_AI_API_KEY,
    api_version="2024-07-01-preview",
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

class OpenAIClient:
    def __init__(self, api_key=None, model=AZURE_OPENAI_MODEL, max_tokens=512, temperature=0.5, top_p=0.9):
        self.api_key = api_key or AZURE_OPEN_AI_API_KEY
        if not self.api_key:
            raise ValueError("Azure OpenAI API key must be provided or set in the environment variable AZURE_OPENAI_API_KEY.")

        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.top_p = top_p
        
        
        print(f"Model: {self.model}" )

    def send_prompt(self, prompt):
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            top_p=self.top_p
        )
        
        chatResponse = response.choices[0].message
        
        return chatResponse.content.strip()