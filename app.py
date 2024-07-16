import os
from dotenv import load_dotenv
import random
from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE")
MONGODB_COLLECTION = os.getenv("MONGODB_COLLECTION")

client = MongoClient(MONGODB_URI)
db = client[MONGODB_DATABASE]
collection = db[MONGODB_COLLECTION]


load_dotenv()
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/data")
def get_data():
    return {"message":"data"}



@app.get("/generate")
def generate_number():
    try:
        print(collection)
        number = random.randint(1, 100)
        collection.insert_one({"number": number})
        return {"message": "Number saved successfully", "number": number}
    except ConnectionFailure:
        raise HTTPException(status_code=500, detail="Failed to connect to MongoDB")
    