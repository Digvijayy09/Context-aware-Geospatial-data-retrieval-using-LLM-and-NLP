import os
from langchain_community.document_loaders import DirectoryLoader, PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Qdrant
from langchain_community.embeddings import SentenceTransformerEmbeddings

# Specify the data folder containing the PDF files
DATA_FOLDER_PATH = "data"

# Initialize the loader to fetch PDFs
print("Loading PDF files...")
loader = DirectoryLoader(
    DATA_FOLDER_PATH, 
    glob="**/*.pdf", 
    loader_cls=PyMuPDFLoader, 
    show_progress=True
)

# Load all documents and print progress
documents = loader.load()
print(f"Loaded {len(documents)} documents.")

# Split loaded documents into chunks
print("Splitting documents into chunks...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=40)
docs = text_splitter.split_documents(documents)
print(f"Split into {len(docs)} chunks.")

# Initialize the SentenceTransformer embedding model
print("Initializing embeddings...")
embeddings = SentenceTransformerEmbeddings(model_name="all-Mpnet-base-v2")  # 768 dimensions

# Qdrant Cloud Configuration
qdrant_cloud_api_key = os.getenv("QDRANT_API")
qdrant_url = os.getenv("QDRANT_URL")

# Push data to Qdrant
print("Uploading to Qdrant...")
qdrant_cloud = Qdrant.from_documents(
    docs,
    embeddings,
    url=qdrant_url,
    prefer_grpc=True,
    api_key=qdrant_cloud_api_key,
    collection_name=os.getenv("QDRANT_COLLECTION_NAME"),
)

print("Data uploaded to Qdrant.")
