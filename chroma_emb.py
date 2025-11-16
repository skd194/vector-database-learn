# import embedding functions utils
from chromadb.utils import embedding_functions

 # create default embedding function instance
default_ef = embedding_functions.DefaultEmbeddingFunction()

NAME = "Paulo"

# get the embedding vector for the name string
emb = default_ef(NAME)

print(f"Embedding vector for '{NAME}':")
print(emb)  # print the embedding vector (list of floats)
