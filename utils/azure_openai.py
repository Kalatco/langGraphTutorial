import os
from langchain_openai import AzureChatOpenAI

chat = AzureChatOpenAI(
  api_key=os.getenv("AZURE_OPENAI_API_KEY"),
  azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
  deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
  api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
  temperature=0
)
