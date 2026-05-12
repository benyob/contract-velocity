import chromadb
from app.config import CHROMA_DB_DIR
from app.services.embeddings_service import generate_embedding

client = chromadb.PersistentClient(path=CHROMA_DB_DIR)
collection = client.get_or_create_collection("historical_contracts")


def retrieve_similar_cases(deviations):

    query = " ".join([d['reason'] for d in deviations])

    embedding = generate_embedding(query)

    results = collection.query(
        query_embeddings=[embedding],
        n_results=3
    )

    return results