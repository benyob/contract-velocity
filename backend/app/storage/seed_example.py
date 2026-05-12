import chromadb
from app.services.embeddings_service import generate_embedding

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("historical_contracts")

examples = [
    {
        "id": "1",
        "text": "Liability cap amendment previously accepted"
    },
    {
        "id": "2",
        "text": "Extended confidentiality period rejected"
    }
]

for ex in examples:

    collection.add(
        ids=[ex["id"]],
        documents=[ex["text"]],
        embeddings=[generate_embedding(ex["text"])]
    )