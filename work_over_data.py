
from chromadb import PersistentClient  # for disk persistence
client = PersistentClient(path="./chroma_db")
from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")

collection = client.get_or_create_collection(name="my_collection")

# print(collection.peek())
# print(collection.get())



def get_chunks(query):
    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    print("🔎 Query Results:")
    print(results)

get_chunks('what are the approximate temperature and salinity values near the surface and at about 2000 dbar depth, and how do they change with depth?')