from chromadb.config import Settings   # import Settings class to configure Chroma client
import chromadb                        # import the chromadb package (vector DB client)
from chromadb.utils import embedding_functions

 # create default embedding function instance
default_ef = embedding_functions.DefaultEmbeddingFunction()

# create a Chroma client instance and tell it to persist data under "chroma_db" folder
chroma_client = chromadb.Client(Settings(persist_directory="chroma_db"))

COLLECTION_NAME = "test_collection"   # name to use for the collection (like a table)

# get the collection if it exists, otherwise create it
collection = chroma_client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=default_ef)

# list of documents to insert; each item has a unique "id" and text content
documents = [
    {"id": "doc1", "text": "Hello, World how are you."},
    {"id": "doc2", "text": "How are you."},
    {"id": "doc3", "text": "Good bye see you again. Never forget to smile."},
    {"id": "doc4", "text": "What is your name."},
    {"id": "doc5", "text": "Where do you live."},
    {"id": "doc6", "text": "When is your birthday."},
]

# upsert each document into the collection (upsert = insert or update if id exists)
for doc in documents:
    collection.upsert(ids=[doc["id"]], documents=[doc["text"]])

# text query to search the collection
QUERY_TEXT = "Where do you live?"
# run a similarity/query operation; query_texts accepts a list (here one query),
# n_results=3 requests the top 3 matches for each query
results = collection.query(query_texts=[QUERY_TEXT], n_results=6)

# print a simple header then each returned document string for the first (and only) query
print(f"Query results for '{QUERY_TEXT}':")
for result in results["documents"][0]:
    print(result)

# print the raw results dict (contains document ids, distances/scores, documents, metadatas, etc.)
print("\nFull results dictionary: ____________________________________")
print(results)


print(f"\nQuery: {query_text}")
for idx, document in enumerate(results["documents"][0]):
    doc_id = results["ids"][0][idx]
    distance = results["distances"][0][idx]
    print(f"Document ID: {doc_id}, Distance: {distance}, Document: {document}")