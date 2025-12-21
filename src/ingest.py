from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = TextLoader("data/finance_guide.txt", encoding="utf-8")
docs = loader.load()


def load_all_documents():
    print(f"Total characters: {len(docs[0].page_content)}")
    return docs

def load_split_documents():
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100, add_start_index=True)
    all_splits = splitter.split_documents(docs)
    print(f"Total chunks: {len(all_splits)}")
    return all_splits

# data.txt -> chunking -> embedding -> pinecone
# write 4 functions for each of the utils