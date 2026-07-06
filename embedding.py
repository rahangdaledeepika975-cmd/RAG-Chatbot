from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import pickle

# Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2",
    encode_kwargs={"normalize_embeddings": True},
)

# Load chunks
with open("chunks.pkl", "rb") as file:
    texts = pickle.load(file)

# Create embeddings
vectors = embeddings.embed_documents(texts)

# Save vectors
with open("vectors.txt", "w") as file:
    for vector in vectors:
        file.write(str(vector) + "\n")

# Create Chroma database
vector_store = Chroma.from_texts(
    texts=texts,
    embedding=embeddings,
    persist_directory="./chroma_langchain_db",
)

# Search
while True:
    query = input("User: ")

    if query.lower() == "exit":
        print("Exiting...")
        break

    results = vector_store.similarity_search(query, k=2)

    for i, result in enumerate(results, 1):
        print(f"{i}. {result.page_content}")