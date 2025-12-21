import sys
import time
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from ingest import load_split_documents
from config import pinecone_api_key


pc = Pinecone(api_key=pinecone_api_key)
if "my-index" not in pc.list_indexes().names():
    pc.create_index(
        name="my-index",
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )
    print('creating pinecone index...')

while not pc.describe_index("my-index").index.status['ready']:
    print('sleeping...')
    time.sleep(1)
print('pinecone index provisioned')
pc.delete_index("my-index")
try:
    # in order to setup the credentials, please follow: https://cloud.google.com/docs/authentication/external/set-up-adc
    # run command: gcloud auth application-default login
    # before running this command, make sure you have installed gcloud sdk: https://cloud.google.com/sdk/docs/install
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
except Exception as e:
    print('Error initializing embeddings:', e)

print('this is embeddings:', embeddings)
index = pc.Index('my-index')
vector_store = PineconeVectorStore(embedding=embeddings, index=index)
print('this is vector_store:', vector_store)
ids = vector_store.add_documents(documents=load_split_documents())
results = vector_store.similarity_search(
    "When does the user plan to retire?",
)

print('this is vector_store result: ', results)

pc.delete_index("my-index")  # For testing purposes, delete existing index for saving the cost

