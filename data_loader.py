from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, RAW_COLLECTION

def load_sample_data():
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    raw_col = db[RAW_COLLECTION]
    sample_data = [
        {"id": "T1003", "technique": "Credential Dumping", "description": "Attackers attempt to dump credentials to obtain account login information."},
        {"id": "T1059", "technique": "Command and Scripting Interpreter", "description": "Execution of arbitrary commands or scripts."},
        {"id": "T1078", "technique": "Valid Accounts", "description": "Use of stolen or guessed credentials to gain access."},
    ]
    raw_col.delete_many({})
    raw_col.insert_many(sample_data)
    print("Sample data loaded successfully.")

if __name__ == "__main__":
    load_sample_data()