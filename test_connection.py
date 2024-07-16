import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE")
MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION")

try:
    client = MongoClient(MONGODB_URI)
    db = client[MONGODB_DATABASE]
    collection = db[MONGODB_COLLECTION]
    print("Connected to MongoDB")
    # Test inserting a document
    collection.insert_one({"test": "success"})
    print("Document inserted successfully")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
