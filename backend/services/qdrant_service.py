from qdrant_client import QdrantClient
from langchain_community.embeddings import SentenceTransformerEmbeddings
import os

# Initialize embeddings
embeddings = SentenceTransformerEmbeddings(model_name=os.getenv("EMBEDDINGS_MODEL"))

# Initialize Qdrant client
client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
)

def search_query(query, collection_name, limit=5):
    query_vector = embeddings.embed_query(query)
    return client.search(collection_name=collection_name, query_vector=query_vector, limit=limit)
