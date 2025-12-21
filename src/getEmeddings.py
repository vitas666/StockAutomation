import getpass
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from config import gemini_key

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

