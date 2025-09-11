from chromadb import PersistentClient
# from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter


# model = SentenceTransformer("all-MiniLM-L6-v2")
client = PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name="my_collection")

def create_chunks(file_name="explain.txt"):
    with open(file_name, "r", encoding="utf-8") as f:
        big_text = f.read()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len
    )
    chunks = text_splitter.split_text(big_text)

    print(f"Total chunks created: {len(chunks)}")

    return chunks



def create_embidings(collection, chunks):
    ids = [f"chunk-{i}" for i in range(len(chunks))]
    # embeddings = model.encode(chunks).tolist()
    collection.add(
        ids=ids,
        # embeddings = embeddings,
        documents=chunks,
        metadatas=[{"chunk_index": i} for i in range(len(chunks))]
    )
    print("✅ All chunks saved to Chroma!")

        
chunks = create_chunks()

create_embidings(collection, chunks)