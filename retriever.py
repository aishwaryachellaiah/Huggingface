from pymongo import MongoClient
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from config import MONGO_URI, DB_NAME, RAW_COLLECTION, TRAINED_COLLECTION

model = SentenceTransformer('all-MiniLM-L6-v2')

def train_embeddings():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    raw_col = db[RAW_COLLECTION]
    train_col = db[TRAINED_COLLECTION]

    train_col.delete_many({})

    for doc in raw_col.find():
        text = f"{doc['technique']} - {doc['description']}"
        embedding = model.encode(text).tolist()
        doc['embedding'] = embedding
        train_col.insert_one(doc)

    print("Embeddings trained and stored successfully.")

def retrieve_relevant_context(query, top_k=1):
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    train_col = db[TRAINED_COLLECTION]

    query_embedding = model.encode(query)

    docs = list(train_col.find())
    if not docs:
        return "Knowledge base not trained yet."

    embeddings = [doc['embedding'] for doc in docs]
    texts = [f"{doc['technique']} - {doc['description']}" for doc in docs]

    similarities = cosine_similarity([query_embedding], embeddings)[0]
    top_index = np.argmax(similarities)

    return texts[top_index]