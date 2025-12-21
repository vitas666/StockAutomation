import os
import getpass
from dotenv import load_dotenv
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from config import pinecone_api_key
from callGemini import AIResponse
from langchain.embeddings import GoogleGenerativeAIEmbeddings
from langchain.chat_models import init_chat_model

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

pc = Pinecone(api_key=pinecone_api_key)

assistant = pc.assistant.create_assistant(
    assistant_name="example-assistant", 
    instructions="Answer in polite, short sentences. Use American English spelling and vocabulary.", 
    timeout=30 # Wait 30 seconds for assistant operation to complete.
)

def get_response_from_assistant(user_input: str) -> str:
    input = AIResponse(user_input)
    
    
# our goat is to build a bot that can answer questions about stock trading according to the user's finiancial situation
# flow: dataset.txt -> chunking -> embedding -> pinecone vector store -> llm to answer questions based on context from vector store
