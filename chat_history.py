from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, HISTORY_COLLECTION

def store_chat(query, response):
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    history_col = db[HISTORY_COLLECTION]
    history_col.insert_one({"query": query, "response": response})

def get_history():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    history_col = db[HISTORY_COLLECTION]
    return list(history_col.find({}, {"_id": 0}))