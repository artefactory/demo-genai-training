import os
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# Azure Chat OpenAI
LLM = AzureChatOpenAI(
    azure_endpoint=os.environ.get("AZURE_CHAT_OPENAI_ENDPOINT"),
    azure_deployment=os.environ.get("AZURE_CHAT_OPENAI_DEPLOYMENT"),
    api_version="2024-02-01",
)

EMBEDDINGS = AzureOpenAIEmbeddings(
    azure_endpoint=os.environ.get("AZURE_CHAT_OPENAI_ENDPOINT"),
    azure_deployment=os.environ.get("AZURE_EMBEDDINGS_OPENAI_DEPLOYMENT"),
    api_version="2024-02-01",
)
