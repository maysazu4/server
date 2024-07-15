from fastapi import FastAPI
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/data")
def get_data():
    return {"message":"data"}