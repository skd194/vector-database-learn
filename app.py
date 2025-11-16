
from chromadb.config import Settings
import chromadb

chroma_client = chromadb.Client(Settings(persist_directory="chroma_db"))

collection_name = "test_collection"
collection = chroma_client.get_or_create_collection(name=collection_name)

documents = [
    {"id": "doc1", "text": "Hello, World how are you."},
    {"id": "doc2", "text": "How are you."},
    {"id": "doc3", "text": "Good bye see you again. Never forget to smile."},
    {"id": "doc4", "text": "What is your name."},
    {"id": "doc5", "text": "Where do you live."},
    {"id": "doc6", "text": "When is your birthday."},
]

for doc in documents:
    collection.upsert(ids=[doc["id"]], documents=[doc["text"]])

query_text = "Where do you live?"
results = collection.query(query_texts=[query_text], n_results=3)

print(f"Query results for '{query_text}':")
for result in results["documents"][0]:
    print(result)
    
print(results)

data = collection.get(ids=["doc1", "doc2"], include=["embeddings", "documents", "metadatas"])
# print(data["embeddings"])   # list of vectors
print(data["documents"])
print(data["metadatas"])